/**
 * @file main.c
 * @brief LOMAH sensor bar main application — bare-metal, no RTOS
 *
 * System architecture:
 *   1. BSP init (clocks 480 MHz, GPIO, DWT, MPU)
 *   2. ADC capture init (ADC1+ADC2 dual mode, DMA circular, TIM2 4 MHz)
 *   3. GCC-PHAT init (FFT context, sensor geometry, speed of sound)
 *   4. Shot trigger init (state machine, AWD callback)
 *   5. Start capture + arm detector
 *   6. Main loop: poll trigger, handle results, service comms
 *
 * Processing timeline per shot:
 *   t=0:     AWD fires (shockwave detected)
 *   t+768us: Post-trigger capture complete
 *   t+~50us: Deinterleave DMA → float[8][1024]
 *   t+~14ms: GCC-PHAT 28 pairs + multilateration
 *   t+~15ms: Result ready, re-armed for next shot
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz)
 * @date    2026-02-14
 */

#include "bsp.h"
#include "adc_capture.h"
#include "shot_trigger.h"
#include "gcc_phat.h"
#include <string.h>

#ifdef USE_CMSIS_DSP
#include <stdio.h>
#endif

/* ================================================================
 * GCC-PHAT CONTEXT (DTCM — zero-wait-state, ~28 KB)
 * ================================================================ */
static gcc_phat_ctx_t gcc_ctx BSP_SECTION_DTCM;

/* ================================================================
 * SENSOR GEOMETRY
 * ================================================================
 *
 * Dual-delta array, 8 microphones:
 *
 *        S2 (0, 260)
 *       / \
 *  S0 (-150,130)   S1 (150,130)
 *       \ /
 *    S3 (0, 130)
 *    ─────────────  ← array center (0, 0)
 *    S7 (0, -130)
 *       / \
 *  S4 (-150,-130)  S5 (150,-130)
 *       \ /
 *        S6 (0, -260)
 *
 * Matches geometry used in test_gcc_phat.c
 */
static const sensor_pos_t sensor_geometry[GCC_PHAT_NUM_CHANNELS] = {
    { .x_mm = -150.0f, .y_mm =  130.0f },  /* S0 */
    { .x_mm =  150.0f, .y_mm =  130.0f },  /* S1 */
    { .x_mm =    0.0f, .y_mm =  260.0f },  /* S2 */
    { .x_mm =    0.0f, .y_mm =  130.0f },  /* S3 */
    { .x_mm = -150.0f, .y_mm = -130.0f },  /* S4 */
    { .x_mm =  150.0f, .y_mm = -130.0f },  /* S5 */
    { .x_mm =    0.0f, .y_mm = -260.0f },  /* S6 */
    { .x_mm =    0.0f, .y_mm = -130.0f },  /* S7 */
};

/* ================================================================
 * RESULT HANDLING
 * ================================================================ */
static volatile bool     result_pending = false;
static lomah_position_t  last_position;
static int               last_valid_pairs;
static shot_event_t      last_event;

/**
 * @brief Shot result callback — called from shot_trigger_poll() in main loop.
 */
static void on_shot_result(const shot_event_t *event,
                           const lomah_position_t *position,
                           int valid_tdoa_pairs)
{
    last_event       = *event;
    last_position    = *position;
    last_valid_pairs = valid_tdoa_pairs;
    result_pending   = true;

#ifdef USE_CMSIS_DSP
    /* Toggle debug pin for oscilloscope timing measurement */
    bsp_debug_toggle();
#endif
}

/**
 * @brief Transmit shot result via UART (placeholder).
 *
 * TODO: Replace with actual UART/Ethernet/WiFi transmission.
 * Output format: compact ASCII for integration with scoring system.
 */
static void transmit_result(void)
{
#ifdef USE_CMSIS_DSP
    if (last_position.valid) {
        /* Example output:
         * SHOT,42,80.5,-42.3,24,13500,0.000012
         * Fields: SHOT, number, x_mm, y_mm, valid_pairs, compute_us, residual */
        printf("SHOT,%lu,%.1f,%.1f,%d,%lu,%.6f\r\n",
               (unsigned long)last_event.shot_number,
               last_position.x_mm,
               last_position.y_mm,
               last_valid_pairs,
               (unsigned long)last_position.compute_us,
               last_position.residual);
    } else {
        printf("MISS,%lu,%d,%.4f\r\n",
               (unsigned long)last_event.shot_number,
               last_valid_pairs,
               last_position.residual);
    }
#endif
}

/* ================================================================
 * BSP IMPLEMENTATIONS (only for target build)
 * ================================================================ */

#ifdef USE_CMSIS_DSP

void bsp_clock_init(void)
{
    /* Enable power supply configuration */
    HAL_PWREx_ConfigSupply(PWR_LDO_SUPPLY);

    /* Voltage scaling VOS0 for 480 MHz operation */
    __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE0);
    while (!__HAL_PWR_GET_FLAG(PWR_FLAG_VOSRDY)) {}

    /* HSE oscillator */
    RCC_OscInitTypeDef osc = {0};
    osc.OscillatorType = RCC_OSCILLATORTYPE_HSE;
    osc.HSEState       = RCC_HSE_ON;
    osc.PLL.PLLState   = RCC_PLL_ON;
    osc.PLL.PLLSource  = RCC_PLLSOURCE_HSE;

    /* PLL1: 25 MHz / 5 × 192 / 2 = 480 MHz SYSCLK */
    osc.PLL.PLLM = 5;
    osc.PLL.PLLN = 192;
    osc.PLL.PLLP = 2;
    osc.PLL.PLLQ = 4;    /* 240 MHz for potential USB */
    osc.PLL.PLLR = 2;
    osc.PLL.PLLRGE   = RCC_PLL1VCIRANGE_2;  /* 4-8 MHz input */
    osc.PLL.PLLVCOSEL = RCC_PLL1VCOWIDE;     /* Wide VCO 192-836 MHz */
    osc.PLL.PLLFRACN  = 0;
    HAL_RCC_OscConfig(&osc);

    /* PLL2: ADC kernel clock → 25 / 5 × 72 / 5 = 72 MHz PLL2P
     * ADC prescaler /2 → 36 MHz ADC clock */
    RCC_PeriphCLKInitTypeDef periph = {0};
    periph.PeriphClockSelection = RCC_PERIPHCLK_ADC;
    periph.PLL2.PLL2M = 5;
    periph.PLL2.PLL2N = 72;
    periph.PLL2.PLL2P = 5;
    periph.PLL2.PLL2Q = 2;
    periph.PLL2.PLL2R = 2;
    periph.PLL2.PLL2RGE   = RCC_PLL2VCIRANGE_2;
    periph.PLL2.PLL2VCOSEL = RCC_PLL2VCOWIDE;
    periph.PLL2.PLL2FRACN  = 0;
    periph.AdcClockSelection = RCC_ADCCLKSOURCE_PLL2;
    HAL_RCCEx_PeriphCLKConfig(&periph);

    /* Bus clocks: HCLK=240, APB1=120, APB2=120 */
    RCC_ClkInitTypeDef clk = {0};
    clk.ClockType = RCC_CLOCKTYPE_HCLK  | RCC_CLOCKTYPE_SYSCLK |
                    RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2  |
                    RCC_CLOCKTYPE_D1PCLK1 | RCC_CLOCKTYPE_D3PCLK1;
    clk.SYSCLKSource   = RCC_SYSCLKSOURCE_PLLCLK;
    clk.SYSCLKDivider  = RCC_SYSCLK_DIV1;
    clk.AHBCLKDivider  = RCC_HCLK_DIV2;      /* 480/2 = 240 MHz */
    clk.APB1CLKDivider = RCC_APB1_DIV2;       /* 240/2 = 120 MHz */
    clk.APB2CLKDivider = RCC_APB2_DIV2;       /* 240/2 = 120 MHz */
    clk.APB3CLKDivider = RCC_APB3_DIV2;
    clk.APB4CLKDivider = RCC_APB4_DIV2;
    HAL_RCC_ClockConfig(&clk, FLASH_LATENCY_4);
}

void bsp_gpio_init(void)
{
    /* Analog pins PA0-PA7 are configured in adc_capture_init() */

    /* Debug / LED pins */
    __HAL_RCC_GPIOB_CLK_ENABLE();

    GPIO_InitTypeDef gpio = {0};
    gpio.Pin   = BSP_LED_PIN | BSP_DEBUG_PIN;
    gpio.Mode  = GPIO_MODE_OUTPUT_PP;
    gpio.Pull  = GPIO_NOPULL;
    gpio.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    HAL_GPIO_Init(GPIOB, &gpio);

    /* Start with LED off, debug low */
    HAL_GPIO_WritePin(BSP_LED_PORT, BSP_LED_PIN, GPIO_PIN_RESET);
    HAL_GPIO_WritePin(BSP_DEBUG_PORT, BSP_DEBUG_PIN, GPIO_PIN_RESET);
}

void bsp_dwt_init(void)
{
    /* Enable trace subsystem (required for DWT) */
    CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;

    /* Reset and enable DWT cycle counter */
    DWT->CYCCNT = 0;
    DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;
}

void bsp_mpu_init(void)
{
    /* Disable MPU during configuration */
    HAL_MPU_Disable();

    /* Region 0: DMA buffer in AXI SRAM — non-cacheable
     * Prevents D-cache coherency issues between DMA writes and CPU reads. */
    MPU_Region_InitTypeDef mpu = {0};
    mpu.Enable           = MPU_REGION_ENABLE;
    mpu.Number           = MPU_REGION_NUMBER0;
    mpu.BaseAddress      = 0x24000000;            /* AXI SRAM base */
    mpu.Size             = MPU_REGION_SIZE_64KB;   /* Covers DMA buffer (32 KB + margin) */
    mpu.AccessPermission = MPU_REGION_FULL_ACCESS;
    mpu.IsBufferable     = MPU_ACCESS_NOT_BUFFERABLE;
    mpu.IsCacheable      = MPU_ACCESS_NOT_CACHEABLE;
    mpu.IsShareable      = MPU_ACCESS_SHAREABLE;
    mpu.TypeExtField     = MPU_TEX_LEVEL1;
    mpu.SubRegionDisable = 0;
    mpu.DisableExec      = MPU_INSTRUCTION_ACCESS_DISABLE;
    HAL_MPU_ConfigRegion(&mpu);

    /* Enable MPU with default memory map for regions not covered */
    HAL_MPU_Enable(MPU_PRIVILEGED_DEFAULT);

    /* Enable I-cache and D-cache */
    SCB_EnableICache();
    SCB_EnableDCache();
}

void bsp_delay_us(uint32_t us)
{
    uint32_t start = DWT->CYCCNT;
    uint32_t cycles = us * (BSP_SYSCLK_HZ / 1000000U);
    while ((DWT->CYCCNT - start) < cycles) {}
}

#endif /* USE_CMSIS_DSP */

/* ================================================================
 * MAIN APPLICATION
 * ================================================================ */

int main(void)
{
#ifdef USE_CMSIS_DSP
    /* ---- 0. HAL initialization (SysTick, NVIC priority grouping) ---- */
    HAL_Init();

    /* ---- 1. System clocks: HSE → PLL1 (480 MHz), PLL2 (ADC) ---- */
    bsp_clock_init();

    /* ---- 2. GPIO: analog inputs + debug pins ---- */
    bsp_gpio_init();

    /* ---- 3. DWT cycle counter for microsecond timing ---- */
    bsp_dwt_init();

    /* ---- 4. MPU: mark DMA buffer region as non-cacheable ---- */
    bsp_mpu_init();
#endif

    /* ---- 5. GCC-PHAT algorithm context ---- */
    gcc_phat_init(&gcc_ctx, (float)GCC_PHAT_SAMPLE_RATE, 30.0f);
    gcc_phat_set_geometry(&gcc_ctx, sensor_geometry);
    gcc_phat_set_threshold(&gcc_ctx, 0.10f);

#ifdef USE_CMSIS_DSP
    /* ---- 6. ADC + DMA capture ---- */
    adc_capture_init();

    /* ---- 7. Shot trigger state machine ---- */
    shot_trigger_init(&gcc_ctx, on_shot_result);

    /* ---- 8. Start capture and arm detector ---- */
    adc_capture_start();
    shot_trigger_arm();

    /* LED on = system ready */
    HAL_GPIO_WritePin(BSP_LED_PORT, BSP_LED_PIN, GPIO_PIN_SET);
#endif

    /* ================================================================
     * MAIN LOOP
     * ================================================================
     *
     * Architecture: super-loop (no RTOS)
     * - shot_trigger_poll() does all heavy processing when a shot occurs
     * - Between shots, the CPU is mostly idle (ADC+DMA run autonomously)
     * - WFI can be used for power saving between interrupts
     */
    while (1) {
        /* Poll shot trigger (deinterleave + GCC-PHAT when window ready) */
        bool shot_processed = shot_trigger_poll();

        /* Handle result */
        if (result_pending) {
            result_pending = false;
            transmit_result();
        }

        /* Periodic tasks (driven by SysTick or simple counter) */
        /* TODO: Read temperature sensor every ~10s, update speed of sound:
         *   float temp = read_temperature_sensor();
         *   gcc_phat_update_temperature(&gcc_ctx, temp);
         */

        /* TODO: Service UART/Ethernet for:
         *   - Threshold adjustment commands
         *   - Geometry calibration updates
         *   - Status queries
         *   - Firmware update
         */

        /* TODO: Self-diagnostics:
         *   - Check ADC noise floor (baseline should be ~2048 ± 20)
         *   - Monitor DMA error count
         *   - Watchdog feed
         */

        /* Power saving: sleep until next interrupt */
        if (!shot_processed && !result_pending) {
#ifdef USE_CMSIS_DSP
            __WFI();
#endif
        }
    }
}
