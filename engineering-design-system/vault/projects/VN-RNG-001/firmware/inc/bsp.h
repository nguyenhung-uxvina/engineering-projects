/**
 * @file bsp.h
 * @brief Board Support Package for VN-RNG-001 LOMAH sensor bar
 *
 * Central hardware abstraction defining pin mappings, clock configuration,
 * memory section macros, and peripheral instance assignments.
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743VIT6 (LQFP100) / STM32H743ZIT6 (LQFP144)
 * @date    2026-02-14
 */

#ifndef BSP_H
#define BSP_H

#ifdef USE_CMSIS_DSP
#include "stm32h7xx_hal.h"
#else
/* Desktop build stubs */
#include <stdint.h>
#include <stdbool.h>
#endif

/* ================================================================
 * CLOCK CONFIGURATION
 * ================================================================
 *
 * HSE  = 25 MHz crystal
 * PLL1 : SYSCLK = 480 MHz, HCLK = 240 MHz, APB1/APB2 = 120 MHz
 * PLL2 : ADC kernel clock → PLL2P = 72 MHz, prescaler /2 = 36 MHz
 *
 * ADC timing at 12-bit, boost enabled:
 *   Conversion = 7.5 + 1.5 sampling = 9 ADC cycles
 *   9 / 36 MHz = 250 ns per conversion → fits 4 MHz trigger period
 */
#define BSP_HSE_FREQ_HZ            25000000U
#define BSP_SYSCLK_HZ              480000000U
#define BSP_HCLK_HZ                240000000U
#define BSP_APB1_HZ                120000000U
#define BSP_APB2_HZ                120000000U
#define BSP_ADC_KERNEL_CLK_HZ      36000000U

/* ================================================================
 * MEMORY SECTION MACROS (linker script placement)
 * ================================================================
 *
 * DTCM     (0x20000000, 128 KB): Zero-wait-state, CPU-only, no DMA
 * AXI SRAM (0x24000000, 512 KB): DMA-accessible, D-cacheable by default
 *
 * Linker script must define:
 *   .dtcm     (NOLOAD) : { *(.dtcm) }     > DTCM
 *   .axi_sram (NOLOAD) : { *(.axi_sram) } > AXI_SRAM
 */
#ifdef USE_CMSIS_DSP
#define BSP_SECTION_DTCM        __attribute__((section(".dtcm")))
#define BSP_SECTION_AXI_SRAM    __attribute__((section(".axi_sram")))
#define BSP_ALIGN_32            __attribute__((aligned(32)))
#else
#define BSP_SECTION_DTCM
#define BSP_SECTION_AXI_SRAM
#define BSP_ALIGN_32
#endif

/* ================================================================
 * ADC PIN ASSIGNMENTS
 * ================================================================
 *
 * Dual regular simultaneous mode:
 *   ADC1 scans: CH0, CH1, CH2, CH3  (microphones 0-3)
 *   ADC2 scans: CH4, CH5, CH6, CH7  (microphones 4-7)
 *
 * TIM2 TRGO triggers both ADCs at 4 MHz.
 * Each trigger → ADC1 converts next channel, ADC2 converts simultaneously.
 * 4 triggers = one complete 8-channel sample → 1 MHz effective per channel.
 *
 * Intra-group skew = 3 × 250 ns = 750 ns = 0.26 mm at 343 m/s.
 * Cross-group pairs (ch0+ch4, ch1+ch5, ...) are truly simultaneous.
 *
 * Pin mapping (LQFP100/144):
 *   PA0 → ADC1_INP0  (MIC 0)
 *   PA1 → ADC1_INP1  (MIC 1)
 *   PA2 → ADC1_INP2  (MIC 2)
 *   PA3 → ADC1_INP3  (MIC 3)
 *   PA4 → ADC2_INP4  (MIC 4)
 *   PA5 → ADC2_INP5  (MIC 5)
 *   PA6 → ADC2_INP6  (MIC 6)
 *   PA7 → ADC2_INP7  (MIC 7)
 */
#define BSP_MIC_GPIO_PORT           GPIOA
#define BSP_MIC_GPIO_PINS           (GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_2 | GPIO_PIN_3 | \
                                     GPIO_PIN_4 | GPIO_PIN_5 | GPIO_PIN_6 | GPIO_PIN_7)

/* ADC1 channel sequence (microphones 0-3) */
#define BSP_ADC1_NUM_CHANNELS       4
#define BSP_ADC1_CH0                0   /* ADC_CHANNEL_0 */
#define BSP_ADC1_CH1                1   /* ADC_CHANNEL_1 */
#define BSP_ADC1_CH2                2   /* ADC_CHANNEL_2 */
#define BSP_ADC1_CH3                3   /* ADC_CHANNEL_3 */

/* ADC2 channel sequence (microphones 4-7) */
#define BSP_ADC2_NUM_CHANNELS       4
#define BSP_ADC2_CH0                4   /* ADC_CHANNEL_4 */
#define BSP_ADC2_CH1                5   /* ADC_CHANNEL_5 */
#define BSP_ADC2_CH2                6   /* ADC_CHANNEL_6 */
#define BSP_ADC2_CH3                7   /* ADC_CHANNEL_7 */

/* ================================================================
 * TIMER CONFIGURATION (ADC trigger source)
 * ================================================================
 *
 * TIM2: 32-bit general-purpose timer on APB1
 * Timer clock = 2 × APB1 = 240 MHz (when APB1 prescaler > 1)
 * TRGO = Update event → triggers ADC1 (+ ADC2 as slave)
 *
 * For 4 MHz trigger: ARR = 240 MHz / 4 MHz - 1 = 59
 */
#define BSP_ADC_TIMER_INSTANCE      TIM2
#define BSP_ADC_TIMER_CLK_HZ       240000000U
#define BSP_ADC_TRIGGER_FREQ_HZ    4000000U
#define BSP_ADC_TIMER_ARR          ((BSP_ADC_TIMER_CLK_HZ / BSP_ADC_TRIGGER_FREQ_HZ) - 1U) /* 59 */
#define BSP_ADC_TIMER_PSC          0U

/* ================================================================
 * DMA CONFIGURATION
 * ================================================================
 *
 * ADC1+ADC2 dual mode → read from ADC12_COMMON->CDR:
 *   CDR[31:16] = ADC2 conversion result
 *   CDR[15:0]  = ADC1 conversion result
 *
 * DMA1_Stream0, peripheral-to-memory, circular, 32-bit word transfers.
 * Buffer must reside in AXI SRAM (D1 domain) for DMA access.
 */
#define BSP_ADC_DMA_INSTANCE        DMA1_Stream0
#define BSP_ADC_DMA_REQUEST         DMA_REQUEST_ADC1
#define BSP_ADC_DMA_IRQn            DMA1_Stream0_IRQn

/* ================================================================
 * BUFFER SIZING
 * ================================================================
 *
 * Each DMA transfer = 1 uint32_t (ADC1[15:0] | ADC2[31:16])
 * 4 DMA transfers = 1 complete 8-channel sample
 * 1024 samples per channel × 4 transfers = 4096 DMA words per half
 * Double buffer = 8192 DMA words total
 */
#define BSP_SAMPLES_PER_CHANNEL     1024
#define BSP_DMA_XFERS_PER_SAMPLE    4       /* 4 ch per ADC, scanned sequentially */
#define BSP_DMA_HALF_SIZE           (BSP_SAMPLES_PER_CHANNEL * BSP_DMA_XFERS_PER_SAMPLE) /* 4096 */
#define BSP_DMA_FULL_SIZE           (BSP_DMA_HALF_SIZE * 2)  /* 8192 */
#define BSP_DMA_FULL_SIZE_MASK      (BSP_DMA_FULL_SIZE - 1)  /* 8191, for fast modulo */

/* ================================================================
 * INTERRUPT PRIORITIES (lower number = higher priority)
 * ================================================================ */
#define BSP_IRQ_PRIO_ADC_AWD       1    /* Analog watchdog — shot trigger (highest) */
#define BSP_IRQ_PRIO_DMA           2    /* DMA half/complete transfer */
#define BSP_IRQ_PRIO_UART          5    /* Communications */
#define BSP_IRQ_PRIO_SYSTICK       15   /* SysTick (lowest) */

/* ================================================================
 * DEBUG / STATUS PINS
 * ================================================================ */
#define BSP_LED_PORT                GPIOB
#define BSP_LED_PIN                 GPIO_PIN_0
#define BSP_DEBUG_PORT              GPIOB
#define BSP_DEBUG_PIN               GPIO_PIN_1  /* Toggle for oscilloscope timing */

/* ================================================================
 * ADC CALIBRATION
 * ================================================================ */
#define BSP_ADC_RESOLUTION_BITS     12
#define BSP_ADC_MAX_VALUE           4095    /* 2^12 - 1 */
#define BSP_ADC_MID_SCALE           2048    /* DC offset for AC-coupled signal */

/* ================================================================
 * BSP FUNCTION PROTOTYPES
 * ================================================================ */

#ifdef USE_CMSIS_DSP

/**
 * @brief Initialize system clocks.
 *
 * Configures: HSE → PLL1 (SYSCLK 480 MHz), PLL2 (ADC kernel clock 36 MHz),
 * AHB/APB prescalers, flash wait states, voltage scaling (VOS0).
 */
void bsp_clock_init(void);

/**
 * @brief Initialize GPIO pins.
 *
 * PA0-PA7 as analog (no pull), PB0 as output (LED), PB1 as output (debug).
 */
void bsp_gpio_init(void);

/**
 * @brief Enable DWT cycle counter for microsecond timing.
 *
 * Used by gcc_phat.c via direct DWT->CYCCNT register read.
 */
void bsp_dwt_init(void);

/**
 * @brief Configure MPU to mark DMA buffer region as non-cacheable.
 *
 * Prevents D-cache coherency issues between DMA writes and CPU reads.
 * Must be called before enabling caches.
 */
void bsp_mpu_init(void);

/**
 * @brief Microsecond delay using DWT cycle counter.
 */
void bsp_delay_us(uint32_t us);

/** Toggle debug pin (for oscilloscope timing measurements). */
static inline void bsp_debug_toggle(void)
{
    BSP_DEBUG_PORT->ODR ^= BSP_DEBUG_PIN;
}

/** Set debug pin high. */
static inline void bsp_debug_high(void)
{
    BSP_DEBUG_PORT->BSRR = BSP_DEBUG_PIN;
}

/** Set debug pin low. */
static inline void bsp_debug_low(void)
{
    BSP_DEBUG_PORT->BSRR = (uint32_t)BSP_DEBUG_PIN << 16U;
}

#endif /* USE_CMSIS_DSP */

#endif /* BSP_H */
