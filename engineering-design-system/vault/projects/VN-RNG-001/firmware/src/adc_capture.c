/**
 * @file adc_capture.c
 * @brief ADC dual-mode capture with DMA for STM32H743
 *
 * Implements 8-channel simultaneous sampling at 1 MHz effective rate
 * using ADC1+ADC2 dual regular simultaneous mode with TIM2 trigger.
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz)
 * @date    2026-02-14
 */

#include "adc_capture.h"
#include <string.h>

/* ================================================================
 * DMA BUFFER (AXI SRAM — DMA-accessible, non-cacheable via MPU)
 * ================================================================ */
static uint32_t dma_buffer[BSP_DMA_FULL_SIZE]
    BSP_SECTION_AXI_SRAM BSP_ALIGN_32;

/* ================================================================
 * MODULE STATE
 * ================================================================ */
static volatile adc_capture_state_t s_state = ADC_CAP_STOPPED;
static volatile adc_capture_stats_t s_stats;
static adc_dma_cb_t                 s_dma_callback = NULL;
static adc_awd_cb_t                 s_awd_callback = NULL;

#ifdef USE_CMSIS_DSP

/* HAL peripheral handles */
static ADC_HandleTypeDef  hadc1;
static ADC_HandleTypeDef  hadc2;
static DMA_HandleTypeDef  hdma_adc1;
static TIM_HandleTypeDef  htim2;

/* ================================================================
 * PERIPHERAL INITIALIZATION
 * ================================================================ */

/** Configure ADC1 as master (4 channels, ext trigger TIM2). */
static void init_adc1(void)
{
    hadc1.Instance = ADC1;
    hadc1.Init.ClockPrescaler           = ADC_CLOCK_ASYNC_DIV2; /* PLL2P/2 = 36 MHz */
    hadc1.Init.Resolution               = ADC_RESOLUTION_12B;
    hadc1.Init.ScanConvMode             = ADC_SCAN_ENABLE;
    hadc1.Init.EOCSelection             = ADC_EOC_SEQ_CONV;
    hadc1.Init.LowPowerAutoWait         = DISABLE;
    hadc1.Init.ContinuousConvMode       = DISABLE;
    hadc1.Init.NbrOfConversion          = BSP_ADC1_NUM_CHANNELS;
    hadc1.Init.DiscontinuousConvMode    = DISABLE;
    hadc1.Init.ExternalTrigConv         = ADC_EXTERNALTRIG_T2_TRGO;
    hadc1.Init.ExternalTrigConvEdge     = ADC_EXTERNALTRIGCONVEDGE_RISING;
    hadc1.Init.ConversionDataManagement = ADC_CONVERSIONDATA_DMA_CIRCULAR;
    hadc1.Init.Overrun                  = ADC_OVR_DATA_OVERWRITTEN;
    hadc1.Init.OversamplingMode         = DISABLE;
    HAL_ADC_Init(&hadc1);

    /* Channel scan sequence: CH0 → CH1 → CH2 → CH3 */
    ADC_ChannelConfTypeDef ch_cfg = {0};
    ch_cfg.SamplingTime = ADC_SAMPLETIME_1CYCLE_5;
    ch_cfg.SingleDiff   = ADC_SINGLE_ENDED;
    ch_cfg.OffsetNumber = ADC_OFFSET_NONE;

    ch_cfg.Channel = ADC_CHANNEL_0;
    ch_cfg.Rank    = ADC_REGULAR_RANK_1;
    HAL_ADC_ConfigChannel(&hadc1, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_1;
    ch_cfg.Rank    = ADC_REGULAR_RANK_2;
    HAL_ADC_ConfigChannel(&hadc1, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_2;
    ch_cfg.Rank    = ADC_REGULAR_RANK_3;
    HAL_ADC_ConfigChannel(&hadc1, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_3;
    ch_cfg.Rank    = ADC_REGULAR_RANK_4;
    HAL_ADC_ConfigChannel(&hadc1, &ch_cfg);
}

/** Configure ADC2 as slave (4 channels, synced to ADC1). */
static void init_adc2(void)
{
    hadc2.Instance = ADC2;
    hadc2.Init.ClockPrescaler           = ADC_CLOCK_ASYNC_DIV2;
    hadc2.Init.Resolution               = ADC_RESOLUTION_12B;
    hadc2.Init.ScanConvMode             = ADC_SCAN_ENABLE;
    hadc2.Init.EOCSelection             = ADC_EOC_SEQ_CONV;
    hadc2.Init.LowPowerAutoWait         = DISABLE;
    hadc2.Init.ContinuousConvMode       = DISABLE;
    hadc2.Init.NbrOfConversion          = BSP_ADC2_NUM_CHANNELS;
    hadc2.Init.DiscontinuousConvMode    = DISABLE;
    hadc2.Init.ConversionDataManagement = ADC_CONVERSIONDATA_DMA_CIRCULAR;
    hadc2.Init.Overrun                  = ADC_OVR_DATA_OVERWRITTEN;
    hadc2.Init.OversamplingMode         = DISABLE;
    /* No external trigger — ADC2 is slaved to ADC1 via dual mode */
    HAL_ADC_Init(&hadc2);

    /* Channel scan sequence: CH4 → CH5 → CH6 → CH7 */
    ADC_ChannelConfTypeDef ch_cfg = {0};
    ch_cfg.SamplingTime = ADC_SAMPLETIME_1CYCLE_5;
    ch_cfg.SingleDiff   = ADC_SINGLE_ENDED;
    ch_cfg.OffsetNumber = ADC_OFFSET_NONE;

    ch_cfg.Channel = ADC_CHANNEL_4;
    ch_cfg.Rank    = ADC_REGULAR_RANK_1;
    HAL_ADC_ConfigChannel(&hadc2, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_5;
    ch_cfg.Rank    = ADC_REGULAR_RANK_2;
    HAL_ADC_ConfigChannel(&hadc2, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_6;
    ch_cfg.Rank    = ADC_REGULAR_RANK_3;
    HAL_ADC_ConfigChannel(&hadc2, &ch_cfg);

    ch_cfg.Channel = ADC_CHANNEL_7;
    ch_cfg.Rank    = ADC_REGULAR_RANK_4;
    HAL_ADC_ConfigChannel(&hadc2, &ch_cfg);
}

/** Configure ADC1+ADC2 dual regular simultaneous mode. */
static void init_dual_mode(void)
{
    ADC_MultiModeTypeDef multimode = {0};
    multimode.Mode            = ADC_DUALMODE_REGSIMULT;
    multimode.DMAAccessMode   = ADC_DMAACCESSMODE_32_10_10;
    multimode.TwoSamplingDelay = ADC_TWOSAMPLINGDELAY_1CYCLE;
    HAL_ADCEx_MultiModeConfigChannel(&hadc1, &multimode);
}

/** Configure analog watchdog 1 on ADC1 CH0. */
static void init_analog_watchdog(void)
{
    ADC_AnalogWDGConfTypeDef awd = {0};
    awd.WatchdogNumber = ADC_ANALOGWATCHDOG_1;
    awd.WatchdogMode   = ADC_ANALOGWATCHDOG_SINGLE_REG;
    awd.Channel        = ADC_CHANNEL_0;
    awd.ITMode         = ENABLE;
    awd.HighThreshold  = 2500;  /* Default, adjustable via API */
    awd.LowThreshold   = 0;
    HAL_ADC_AnalogWDGConfig(&hadc1, &awd);
}

/** Configure DMA1_Stream0 for ADC dual-mode circular transfer. */
static void init_dma(void)
{
    __HAL_RCC_DMA1_CLK_ENABLE();

    hdma_adc1.Instance                 = BSP_ADC_DMA_INSTANCE;
    hdma_adc1.Init.Request             = BSP_ADC_DMA_REQUEST;
    hdma_adc1.Init.Direction           = DMA_PERIPH_TO_MEMORY;
    hdma_adc1.Init.PeriphInc           = DMA_PINC_DISABLE;
    hdma_adc1.Init.MemInc              = DMA_MINC_ENABLE;
    hdma_adc1.Init.PeriphDataAlignment = DMA_PDATAALIGN_WORD;
    hdma_adc1.Init.MemDataAlignment    = DMA_MDATAALIGN_WORD;
    hdma_adc1.Init.Mode                = DMA_CIRCULAR;
    hdma_adc1.Init.Priority            = DMA_PRIORITY_VERY_HIGH;
    hdma_adc1.Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
    HAL_DMA_Init(&hdma_adc1);

    /* Link DMA to ADC1 */
    __HAL_LINKDMA(&hadc1, DMA_Handle, hdma_adc1);

    /* Enable DMA interrupt */
    HAL_NVIC_SetPriority(BSP_ADC_DMA_IRQn, BSP_IRQ_PRIO_DMA, 0);
    HAL_NVIC_EnableIRQ(BSP_ADC_DMA_IRQn);
}

/** Configure TIM2 as 4 MHz trigger source for ADC. */
static void init_timer(void)
{
    __HAL_RCC_TIM2_CLK_ENABLE();

    htim2.Instance               = BSP_ADC_TIMER_INSTANCE;
    htim2.Init.Prescaler         = BSP_ADC_TIMER_PSC;
    htim2.Init.CounterMode       = TIM_COUNTERMODE_UP;
    htim2.Init.Period            = BSP_ADC_TIMER_ARR;
    htim2.Init.ClockDivision     = TIM_CLOCKDIVISION_DIV1;
    htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_ENABLE;
    HAL_TIM_Base_Init(&htim2);

    /* TRGO = Update event → triggers ADC */
    TIM_MasterConfigTypeDef master = {0};
    master.MasterOutputTrigger  = TIM_TRGO_UPDATE;
    master.MasterSlaveMode      = TIM_MASTERSLAVEMODE_DISABLE;
    HAL_TIMEx_MasterConfigSynchronization(&htim2, &master);
}

/* ================================================================
 * PUBLIC API
 * ================================================================ */

void adc_capture_init(void)
{
    memset((void *)&s_stats, 0, sizeof(s_stats));
    s_state = ADC_CAP_STOPPED;

    /* Enable peripheral clocks */
    __HAL_RCC_ADC12_CLK_ENABLE();
    __HAL_RCC_GPIOA_CLK_ENABLE();

    /* Configure GPIO PA0-PA7 as analog inputs */
    GPIO_InitTypeDef gpio = {0};
    gpio.Pin  = BSP_MIC_GPIO_PINS;
    gpio.Mode = GPIO_MODE_ANALOG;
    gpio.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(BSP_MIC_GPIO_PORT, &gpio);

    /* Initialize peripherals */
    init_dma();
    init_adc1();
    init_adc2();
    init_dual_mode();
    init_analog_watchdog();
    init_timer();

    /* ADC self-calibration (improves accuracy) */
    HAL_ADCEx_Calibration_Start(&hadc1, ADC_CALIB_OFFSET, ADC_SINGLE_ENDED);
    HAL_ADCEx_Calibration_Start(&hadc2, ADC_CALIB_OFFSET, ADC_SINGLE_ENDED);

    /* Enable ADC interrupt for analog watchdog */
    HAL_NVIC_SetPriority(ADC_IRQn, BSP_IRQ_PRIO_ADC_AWD, 0);
    HAL_NVIC_EnableIRQ(ADC_IRQn);
}

void adc_capture_start(void)
{
    if (s_state == ADC_CAP_RUNNING) return;

    /* 1. Start DMA (must be ready before first ADC conversion) */
    HAL_ADCEx_MultiModeStart_DMA(&hadc1,
                                  (uint32_t *)dma_buffer,
                                  BSP_DMA_FULL_SIZE);

    /* 2. Start ADC2 slave (must start before master) */
    HAL_ADC_Start(&hadc2);

    /* 3. Start TIM2 → triggers begin flowing */
    HAL_TIM_Base_Start(&htim2);

    s_state = ADC_CAP_RUNNING;
}

void adc_capture_stop(void)
{
    /* Reverse order: stop trigger first, then ADC, then DMA */
    HAL_TIM_Base_Stop(&htim2);
    HAL_ADC_Stop(&hadc2);
    HAL_ADCEx_MultiModeStop_DMA(&hadc1);

    s_state = ADC_CAP_STOPPED;
}

adc_capture_state_t adc_capture_get_state(void)
{
    return s_state;
}

const uint32_t *adc_capture_get_buffer(void)
{
    return dma_buffer;
}

uint32_t adc_capture_get_write_index(void)
{
    /* NDTR counts DOWN from BSP_DMA_FULL_SIZE to 0 */
    uint32_t ndtr = __HAL_DMA_GET_COUNTER(&hdma_adc1);
    return BSP_DMA_FULL_SIZE - ndtr;
}

void adc_capture_set_dma_callback(adc_dma_cb_t cb)
{
    s_dma_callback = cb;
}

void adc_capture_set_awd_callback(adc_awd_cb_t cb)
{
    s_awd_callback = cb;
}

void adc_capture_set_awd_threshold(uint16_t threshold_raw)
{
    /* Update AWD high threshold register directly for speed.
     * ADC1->HTR1 holds the high threshold for AWD1.
     * Shift left by (16 - resolution) for left-aligned comparison.
     * At 12-bit: shift left by 4. But in right-aligned data mode,
     * the threshold register also uses right-aligned format. */
    ADC_AnalogWDGConfTypeDef awd = {0};
    awd.WatchdogNumber = ADC_ANALOGWATCHDOG_1;
    awd.WatchdogMode   = ADC_ANALOGWATCHDOG_SINGLE_REG;
    awd.Channel        = ADC_CHANNEL_0;
    awd.ITMode         = ENABLE;
    awd.HighThreshold  = threshold_raw;
    awd.LowThreshold   = 0;
    HAL_ADC_AnalogWDGConfig(&hadc1, &awd);
}

void adc_capture_awd_enable(bool enable)
{
    if (enable) {
        /* Enable AWD1 interrupt */
        __HAL_ADC_ENABLE_IT(&hadc1, ADC_IT_AWD1);
    } else {
        /* Disable AWD1 interrupt (AWD still monitors, just doesn't fire IRQ) */
        __HAL_ADC_DISABLE_IT(&hadc1, ADC_IT_AWD1);
    }
}

void adc_capture_get_stats(adc_capture_stats_t *stats)
{
    /* Disable interrupts briefly for consistent snapshot */
    uint32_t primask = __get_PRIMASK();
    __disable_irq();
    *stats = *(const adc_capture_stats_t *)&s_stats;
    __set_PRIMASK(primask);
}

void adc_capture_reset_stats(void)
{
    uint32_t primask = __get_PRIMASK();
    __disable_irq();
    memset((void *)&s_stats, 0, sizeof(s_stats));
    __set_PRIMASK(primask);
}

/* ================================================================
 * ISR HANDLERS
 * ================================================================ */

/** DMA1 Stream0 interrupt handler. */
void DMA1_Stream0_IRQHandler(void)
{
    HAL_DMA_IRQHandler(&hdma_adc1);
}

/** HAL callback: DMA half-transfer complete. */
void HAL_ADC_ConvHalfCpltCallback(ADC_HandleTypeDef *hadc)
{
    (void)hadc;
    s_stats.dma_half_count++;
    if (s_dma_callback) {
        s_dma_callback(0); /* First half completed */
    }
}

/** HAL callback: DMA full-transfer complete. */
void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef *hadc)
{
    (void)hadc;
    s_stats.dma_full_count++;
    if (s_dma_callback) {
        s_dma_callback(1); /* Second half completed */
    }
}

/** HAL callback: ADC error (overrun). */
void HAL_ADC_ErrorCallback(ADC_HandleTypeDef *hadc)
{
    (void)hadc;
    s_stats.adc_overrun_count++;
    s_state = ADC_CAP_ERROR;
}

/** ADC interrupt handler (includes analog watchdog). */
void ADC_IRQHandler(void)
{
    /* Check analog watchdog 1 flag first (highest priority) */
    if (__HAL_ADC_GET_FLAG(&hadc1, ADC_FLAG_AWD1)) {
        __HAL_ADC_CLEAR_FLAG(&hadc1, ADC_FLAG_AWD1);
        s_stats.awd_trigger_count++;

        if (s_awd_callback) {
            uint32_t trigger_index = adc_capture_get_write_index();
            s_awd_callback(trigger_index);
        }
    }

    /* Let HAL handle remaining ADC interrupts */
    HAL_ADC_IRQHandler(&hadc1);
}

#endif /* USE_CMSIS_DSP */

/* ================================================================
 * DEINTERLEAVE (portable — used on both target and desktop)
 * ================================================================ */

void adc_capture_deinterleave(const uint32_t *dma_buf,
                               uint32_t start_index,
                               float signals_out[][BSP_SAMPLES_PER_CHANNEL])
{
    const float inv_scale = 1.0f / (float)BSP_ADC_MID_SCALE; /* 1/2048 */

    for (uint32_t n = 0; n < BSP_SAMPLES_PER_CHANNEL; n++) {
        for (uint32_t k = 0; k < BSP_DMA_XFERS_PER_SAMPLE; k++) {
            /* Circular buffer index with fast bitmask wrap */
            uint32_t idx = (start_index + n * BSP_DMA_XFERS_PER_SAMPLE + k)
                           & BSP_DMA_FULL_SIZE_MASK;

            uint32_t raw = dma_buf[idx];

            /* Unpack: lower 16 bits = ADC1 (ch 0-3), upper 16 = ADC2 (ch 4-7) */
            uint16_t adc1_val = (uint16_t)(raw & 0xFFFFU);
            uint16_t adc2_val = (uint16_t)((raw >> 16) & 0xFFFFU);

            /* Convert to float [-1, +1] with DC removal */
            signals_out[k][n]     = ((float)adc1_val - (float)BSP_ADC_MID_SCALE) * inv_scale;
            signals_out[k + 4][n] = ((float)adc2_val - (float)BSP_ADC_MID_SCALE) * inv_scale;
        }
    }
}
