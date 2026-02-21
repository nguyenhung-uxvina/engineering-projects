/**
 * @file adc_capture.h
 * @brief 8-channel ADC capture with DMA double-buffer for LOMAH shockwave sensing
 *
 * Hardware Configuration:
 *   ADC1 + ADC2 in dual regular simultaneous mode (12-bit)
 *   TIM2 TRGO triggers both ADCs at 4 MHz
 *   DMA1_Stream0 reads from ADC12_CDR (common data register)
 *   Circular DMA with half/complete transfer interrupts
 *
 * DMA Data Format:
 *   Each uint32_t word: [ADC2_result:16 | ADC1_result:16]
 *   Scan sequence per trigger cycle:
 *     trigger 0 → (CH0, CH4) — simultaneous
 *     trigger 1 → (CH1, CH5) — simultaneous
 *     trigger 2 → (CH2, CH6) — simultaneous
 *     trigger 3 → (CH3, CH7) — simultaneous
 *   4 consecutive uint32_t = one complete 8-channel sample at 1 MHz effective.
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz)
 * @date    2026-02-14
 */

#ifndef ADC_CAPTURE_H
#define ADC_CAPTURE_H

#include "bsp.h"
#include <stdint.h>
#include <stdbool.h>

/* ---- Types ---- */

/** Capture module state. */
typedef enum {
    ADC_CAP_STOPPED = 0,
    ADC_CAP_RUNNING,
    ADC_CAP_ERROR
} adc_capture_state_t;

/** Capture statistics for diagnostics. */
typedef struct {
    uint32_t dma_half_count;        /**< Half-transfer interrupt count */
    uint32_t dma_full_count;        /**< Full-transfer interrupt count */
    uint32_t dma_error_count;       /**< DMA transfer error count */
    uint32_t adc_overrun_count;     /**< ADC data overrun count */
    uint32_t awd_trigger_count;     /**< Analog watchdog trigger count */
} adc_capture_stats_t;

/** DMA half/complete callback. Called from ISR — must be fast. */
typedef void (*adc_dma_cb_t)(uint32_t completed_half_index);

/** Analog watchdog callback. Called from ISR with DMA position at trigger instant. */
typedef void (*adc_awd_cb_t)(uint32_t dma_index_at_trigger);

/* ---- Public API ---- */

/**
 * @brief Initialize ADC1+ADC2 dual mode, DMA1, TIM2, and analog watchdog.
 *
 * Configures all peripherals but does NOT start conversions.
 * Call adc_capture_start() to begin.
 *
 * Init sequence:
 *   1. Enable peripheral clocks (ADC12, DMA1, TIM2, GPIOA)
 *   2. Run ADC self-calibration (single-ended mode)
 *   3. Configure ADC1: 12-bit, scan 4 channels, ext trigger TIM2 TRGO
 *   4. Configure ADC2: 12-bit, scan 4 channels, slave to ADC1
 *   5. Configure dual regular simultaneous mode (ADC12_COMMON)
 *   6. Configure DMA1_Stream0: circular, word-size, half+complete IRQs
 *   7. Configure TIM2: 4 MHz update rate, TRGO on update event
 *   8. Configure analog watchdog 1 on ADC1 CH0
 */
void adc_capture_init(void);

/**
 * @brief Start continuous ADC capture.
 *
 * Enables DMA first, then starts ADC1+ADC2, then TIM2.
 * Order ensures DMA is ready before first conversion completes.
 */
void adc_capture_start(void);

/**
 * @brief Stop ADC capture.
 *
 * Stops TIM2 first (no more triggers), then ADC, then DMA.
 */
void adc_capture_stop(void);

/**
 * @brief Get current module state.
 */
adc_capture_state_t adc_capture_get_state(void);

/**
 * @brief Get pointer to raw DMA circular buffer (read-only).
 *
 * Buffer resides in AXI SRAM. Contains BSP_DMA_FULL_SIZE uint32_t words.
 * Each word: [ADC2:16 | ADC1:16].
 *
 * @return Pointer to dma_buffer[0]
 */
const uint32_t *adc_capture_get_buffer(void);

/**
 * @brief Get current DMA write position in circular buffer.
 *
 * Reads DMA NDTR register: position = FULL_SIZE - NDTR.
 * Used by shot trigger to timestamp events relative to the buffer.
 *
 * @return Write index (0 to BSP_DMA_FULL_SIZE-1)
 */
uint32_t adc_capture_get_write_index(void);

/**
 * @brief Register callback for DMA half/complete transfer.
 *
 * Called from ISR context with the index of the completed half:
 *   0 = first half (indices 0..HALF-1) completed
 *   1 = second half (indices HALF..FULL-1) completed
 *
 * @param cb  Callback function, or NULL to disable
 */
void adc_capture_set_dma_callback(adc_dma_cb_t cb);

/**
 * @brief Register callback for analog watchdog trigger.
 *
 * Called from ISR with the DMA index at the trigger instant.
 *
 * @param cb  Callback function, or NULL to disable
 */
void adc_capture_set_awd_callback(adc_awd_cb_t cb);

/**
 * @brief Set analog watchdog high threshold.
 *
 * AWD fires when any sample on the monitored channel exceeds this value.
 * Typical: quiet baseline ~2048, shockwave peak > 2500-3500.
 *
 * @param threshold_raw  12-bit value (0-4095)
 */
void adc_capture_set_awd_threshold(uint16_t threshold_raw);

/**
 * @brief Enable or disable analog watchdog interrupt.
 *
 * @param enable  true to enable, false to disable (mask interrupt)
 */
void adc_capture_awd_enable(bool enable);

/**
 * @brief Deinterleave a capture window from DMA format to float channels.
 *
 * Extracts BSP_SAMPLES_PER_CHANNEL (1024) samples starting at start_index
 * from the circular DMA buffer. Unpacks the interleaved ADC1+ADC2 data
 * into 8 separate float channels with DC offset removal.
 *
 * Conversion per raw value:
 *   float_val = ((float)raw_12bit - 2048.0f) / 2048.0f → normalized [-1, +1]
 *
 * Handles circular buffer wrap-around automatically using bitmask.
 *
 * @param dma_buf       Pointer to circular DMA buffer
 * @param start_index   Starting index (uint32_t units), must be aligned to
 *                      BSP_DMA_XFERS_PER_SAMPLE (4-word boundary)
 * @param signals_out   Output: float[8][BSP_SAMPLES_PER_CHANNEL]
 */
void adc_capture_deinterleave(const uint32_t *dma_buf,
                               uint32_t start_index,
                               float signals_out[][BSP_SAMPLES_PER_CHANNEL]);

/**
 * @brief Get capture statistics.
 */
void adc_capture_get_stats(adc_capture_stats_t *stats);

/**
 * @brief Reset all statistics counters to zero.
 */
void adc_capture_reset_stats(void);

#endif /* ADC_CAPTURE_H */
