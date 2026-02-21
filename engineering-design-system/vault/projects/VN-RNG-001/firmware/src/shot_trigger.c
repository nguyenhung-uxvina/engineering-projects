/**
 * @file shot_trigger.c
 * @brief Shot detection state machine implementation
 *
 * Manages the lifecycle of a shot event:
 *   AWD interrupt → capture window → deinterleave → GCC-PHAT → result
 *
 * ISR responsibilities (fast, <1 us):
 *   - Snapshot DMA index at trigger instant
 *   - Calculate capture window boundaries
 *   - Set ready flag for main loop
 *
 * Main loop responsibilities (heavy, ~15 ms):
 *   - D-cache invalidation
 *   - Deinterleave DMA → float channels
 *   - GCC-PHAT processing
 *   - Result delivery and re-arm
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz)
 * @date    2026-02-14
 */

#include "shot_trigger.h"
#include "adc_capture.h"
#include <string.h>

/* ================================================================
 * PROCESSING BUFFER (DTCM — fastest memory, no DMA access needed)
 * ================================================================ */
static float processing_signals[GCC_PHAT_NUM_CHANNELS][GCC_PHAT_FFT_SIZE]
    BSP_SECTION_DTCM BSP_ALIGN_32;

/* ================================================================
 * MODULE STATE
 * ================================================================ */
static volatile shot_state_t  s_state = SHOT_STATE_IDLE;
static volatile shot_event_t  s_current_event;
static volatile bool          s_window_ready = false;
static volatile uint32_t      s_post_trigger_target;

static gcc_phat_ctx_t        *s_gcc_ctx   = NULL;
static shot_result_cb_t       s_result_cb = NULL;
static uint32_t               s_shot_count = 0;

/* ================================================================
 * ISR CALLBACKS (registered with adc_capture)
 * ================================================================ */

/**
 * @brief Analog watchdog callback — called from ADC ISR.
 *
 * Fires when shockwave amplitude exceeds threshold on ADC1 CH0.
 * Must execute in <1 us. Only sets state and computes indices.
 */
static void on_awd_trigger(uint32_t dma_index_at_trigger)
{
    if (s_state != SHOT_STATE_ARMED) return;

    s_state = SHOT_STATE_TRIGGERED;

    /* Record event metadata */
    s_current_event.trigger_dma_index = dma_index_at_trigger;
    s_current_event.shot_number = ++s_shot_count;

#ifdef USE_CMSIS_DSP
    /* Timestamp from DWT cycle counter */
    s_current_event.trigger_timestamp_us =
        DWT->CYCCNT / (BSP_SYSCLK_HZ / 1000000U);
#else
    s_current_event.trigger_timestamp_us = 0;
#endif

    /* Calculate window start: go back PRE_TRIGGER samples in DMA buffer.
     * Each sample = BSP_DMA_XFERS_PER_SAMPLE (4) DMA words. */
    uint32_t pre_xfers = SHOT_PRE_TRIGGER_SAMPLES * BSP_DMA_XFERS_PER_SAMPLE;

    if (dma_index_at_trigger >= pre_xfers) {
        s_current_event.window_start_index = dma_index_at_trigger - pre_xfers;
    } else {
        /* Wrap around circular buffer */
        s_current_event.window_start_index =
            BSP_DMA_FULL_SIZE - (pre_xfers - dma_index_at_trigger);
    }

    /* Calculate DMA index where post-trigger window completes */
    uint32_t post_xfers = SHOT_POST_TRIGGER_SAMPLES * BSP_DMA_XFERS_PER_SAMPLE;
    s_post_trigger_target =
        (dma_index_at_trigger + post_xfers) & BSP_DMA_FULL_SIZE_MASK;

    /* Disable AWD to prevent re-trigger during capture */
    adc_capture_awd_enable(false);
}

/**
 * @brief DMA half/complete callback — called from DMA ISR.
 *
 * Used to detect when post-trigger window is fully captured.
 * Fires every BSP_DMA_HALF_SIZE (4096) DMA transfers.
 */
static void on_dma_complete(uint32_t completed_half_index)
{
    (void)completed_half_index;

    if (s_state != SHOT_STATE_TRIGGERED) return;

    /* Check if DMA has advanced past the post-trigger target.
     * Since the DMA callback fires every 4096 transfers and we need
     * 768 × 4 = 3072 post-trigger transfers, one callback after
     * trigger is sufficient in most cases. */
    uint32_t current = adc_capture_get_write_index();
    uint32_t trigger_idx = s_current_event.trigger_dma_index;
    bool complete;

    if (s_post_trigger_target >= trigger_idx) {
        /* No wrap: target is ahead of trigger in buffer */
        complete = (current >= s_post_trigger_target) ||
                   (current < trigger_idx);  /* Wrapped past end */
    } else {
        /* Target wrapped: target < trigger in buffer */
        complete = (current >= s_post_trigger_target) &&
                   (current < trigger_idx);
    }

    if (complete) {
        s_state = SHOT_STATE_PROCESSING;
        s_window_ready = true;  /* Signal main loop */
    }
}

/* ================================================================
 * PUBLIC API
 * ================================================================ */

void shot_trigger_init(gcc_phat_ctx_t *gcc_ctx, shot_result_cb_t result_cb)
{
    s_gcc_ctx   = gcc_ctx;
    s_result_cb = result_cb;
    s_state     = SHOT_STATE_IDLE;
    s_window_ready = false;
    s_shot_count = 0;

    memset((void *)&s_current_event, 0, sizeof(s_current_event));

    /* Register callbacks with ADC capture module */
    adc_capture_set_awd_callback(on_awd_trigger);
    adc_capture_set_dma_callback(on_dma_complete);

    /* Set default threshold */
    adc_capture_set_awd_threshold(SHOT_DEFAULT_AWD_THRESHOLD);
}

void shot_trigger_arm(void)
{
    if (s_state != SHOT_STATE_IDLE) return;

    s_window_ready = false;
    s_state = SHOT_STATE_ARMED;
    adc_capture_awd_enable(true);
}

void shot_trigger_disarm(void)
{
    adc_capture_awd_enable(false);
    s_window_ready = false;
    s_state = SHOT_STATE_IDLE;
}

shot_state_t shot_trigger_get_state(void)
{
    return s_state;
}

void shot_trigger_set_threshold(uint16_t threshold_raw)
{
    adc_capture_set_awd_threshold(threshold_raw);
}

bool shot_trigger_poll(void)
{
    if (!s_window_ready) return false;
    s_window_ready = false;

#ifdef USE_CMSIS_DSP
    /* 1. Invalidate D-cache for DMA buffer to ensure CPU sees DMA-written data.
     *    If MPU is configured to mark DMA buffer as non-cacheable, this is a no-op
     *    but harmless to keep for safety. */
    SCB_InvalidateDCache_by_Addr(
        (uint32_t *)adc_capture_get_buffer(),
        BSP_DMA_FULL_SIZE * sizeof(uint32_t));
#endif

    /* 2. Deinterleave DMA buffer → float signals[8][1024] in DTCM */
    adc_capture_deinterleave(
        adc_capture_get_buffer(),
        s_current_event.window_start_index,
        processing_signals);

    /* 3. Run GCC-PHAT full pipeline: TDOA + multilateration */
    lomah_position_t position;
    int valid_pairs = gcc_phat_process_shot(
        s_gcc_ctx,
        (const float (*)[GCC_PHAT_FFT_SIZE])processing_signals,
        &position);

    /* 4. Deliver result via callback */
    if (s_result_cb) {
        s_result_cb(&s_current_event, &position, valid_pairs);
    }

    /* 5. Re-arm for next shot.
     * The ~15 ms processing time provides natural lockout against
     * double-triggering from shockwave reflections.
     * At max 1200 RPM (50 ms between shots), this leaves 35 ms margin. */
    s_state = SHOT_STATE_ARMED;
    adc_capture_awd_enable(true);

    return true;
}

uint32_t shot_trigger_get_shot_count(void)
{
    return s_shot_count;
}

void shot_trigger_reset_count(void)
{
    s_shot_count = 0;
}
