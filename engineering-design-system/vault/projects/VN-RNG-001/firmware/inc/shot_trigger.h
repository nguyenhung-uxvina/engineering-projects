/**
 * @file shot_trigger.h
 * @brief Shot detection state machine for LOMAH shockwave trigger
 *
 * State Machine:
 *
 *   IDLE ──(arm)──> ARMED ──(AWD IRQ)──> TRIGGERED
 *     ^                                      |
 *     |                         (post-trigger samples collected)
 *     |                                      v
 *     └──(result delivered)── PROCESSING <───┘
 *
 * Timing:
 *   Pre-trigger:  256 samples (256 us) — baseline before shockwave
 *   Post-trigger: 768 samples (768 us) — shockwave + decay
 *   Total window: 1024 samples = 1.024 ms
 *   Processing:   ~15 ms (28 FFT pairs + multilateration)
 *   Rearm:        Immediate after processing (natural lockout ~15 ms)
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz)
 * @date    2026-02-14
 */

#ifndef SHOT_TRIGGER_H
#define SHOT_TRIGGER_H

#include "bsp.h"
#include "gcc_phat.h"
#include <stdint.h>
#include <stdbool.h>

/* ---- Configuration ---- */

/** Samples to include BEFORE the trigger point.
 *  Provides baseline context for FFT windowing. */
#define SHOT_PRE_TRIGGER_SAMPLES    256

/** Samples to capture AFTER the trigger point.
 *  Contains the shockwave N-wave and decay. */
#define SHOT_POST_TRIGGER_SAMPLES   (BSP_SAMPLES_PER_CHANNEL - SHOT_PRE_TRIGGER_SAMPLES)

/** Default analog watchdog threshold (12-bit raw).
 *  Quiet baseline ~2048, shockwave peak typically 2500-3500. */
#define SHOT_DEFAULT_AWD_THRESHOLD  2500

/* ---- Types ---- */

/** State machine states. */
typedef enum {
    SHOT_STATE_IDLE = 0,    /**< Not armed, ignoring events */
    SHOT_STATE_ARMED,       /**< Waiting for shockwave (AWD enabled) */
    SHOT_STATE_TRIGGERED,   /**< Counting post-trigger samples */
    SHOT_STATE_PROCESSING   /**< Deinterleaving + GCC-PHAT running */
} shot_state_t;

/** Shot event metadata. */
typedef struct {
    uint32_t trigger_dma_index;     /**< DMA buffer index at trigger instant */
    uint32_t window_start_index;    /**< Start of 1024-sample window (pre-trigger) */
    uint32_t trigger_timestamp_us;  /**< DWT-based microsecond timestamp */
    uint32_t shot_number;           /**< Sequential shot counter */
} shot_event_t;

/** Result callback — called from main loop context (not ISR).
 *  Delivers position estimate and TDOA validity count. */
typedef void (*shot_result_cb_t)(const shot_event_t *event,
                                  const lomah_position_t *position,
                                  int valid_tdoa_pairs);

/* ---- Public API ---- */

/**
 * @brief Initialize shot trigger module.
 *
 * Registers AWD and DMA callbacks with adc_capture module.
 * Initial state: IDLE.
 *
 * @param gcc_ctx    Pointer to initialized GCC-PHAT context (must persist)
 * @param result_cb  Callback for shot results (NULL to disable)
 */
void shot_trigger_init(gcc_phat_ctx_t *gcc_ctx, shot_result_cb_t result_cb);

/**
 * @brief Arm the shot detector.
 *
 * IDLE → ARMED. Enables analog watchdog interrupt.
 * Must be called after adc_capture_start().
 */
void shot_trigger_arm(void);

/**
 * @brief Disarm the shot detector.
 *
 * Any state → IDLE. Disables analog watchdog interrupt.
 */
void shot_trigger_disarm(void);

/**
 * @brief Get current state.
 */
shot_state_t shot_trigger_get_state(void);

/**
 * @brief Set detection threshold.
 *
 * @param threshold_raw  12-bit ADC value (0-4095)
 */
void shot_trigger_set_threshold(uint16_t threshold_raw);

/**
 * @brief Poll for completed shot — MUST be called from main loop.
 *
 * When a complete capture window is ready, this function:
 *   1. Transitions to PROCESSING state
 *   2. Deinterleaves DMA buffer → float signals[8][1024]
 *   3. Calls gcc_phat_process_shot()
 *   4. Invokes result callback with position
 *   5. Re-arms the detector
 *
 * All heavy processing runs here (not in ISR).
 *
 * @return true if a shot was processed in this call
 */
bool shot_trigger_poll(void);

/**
 * @brief Get total shot count since init/reset.
 */
uint32_t shot_trigger_get_shot_count(void);

/**
 * @brief Reset shot counter to zero.
 */
void shot_trigger_reset_count(void);

#endif /* SHOT_TRIGGER_H */
