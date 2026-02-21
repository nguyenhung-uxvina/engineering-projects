/**
 * @file gcc_phat.h
 * @brief GCC-PHAT (Generalized Cross-Correlation with Phase Transform)
 *        for LOMAH acoustic TDOA estimation on ARM Cortex-M7
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @target  STM32H743 (ARM Cortex-M7, 480 MHz, FPU, DSP instructions)
 * @author  VN-RNG-001 Firmware Team
 * @date    2026-02-08
 * @version 1.0
 *
 * Algorithm Reference:
 *   C. Knapp and G. Carter, "The Generalized Correlation Method for
 *   Estimation of Time Delay," IEEE Trans. ASSP, vol. 24, no. 4, 1976.
 *
 * GCC-PHAT Overview:
 *   1. Capture N samples from two microphone channels (x, y)
 *   2. Compute FFT of both channels: X = FFT(x), Y = FFT(y)
 *   3. Compute cross-power spectrum: G = X * conj(Y)
 *   4. Apply PHAT weighting: G_phat = G / |G|  (phase-only)
 *   5. Compute IFFT: R = IFFT(G_phat)
 *   6. Find peak of R → peak index = sample delay τ
 *   7. Convert τ to time delay: Δt = τ / Fs
 *
 * Performance Targets:
 *   - FFT size: 1024 points (configurable)
 *   - Sample rate: 1 MHz (1 μs resolution)
 *   - Processing time: <500 μs per pair on Cortex-M7 @ 480 MHz
 *   - TDOA resolution: ±1 μs (±0.343 mm at 343 m/s sound speed)
 */

#ifndef GCC_PHAT_H
#define GCC_PHAT_H

#include <stdint.h>
#include <stdbool.h>

/* ---- Configuration ---- */

/** FFT size (must be power of 2). Larger = better resolution, slower. */
#ifndef GCC_PHAT_FFT_SIZE
#define GCC_PHAT_FFT_SIZE       1024
#endif

/** Sample rate in Hz. 1 MHz gives 1 μs TDOA resolution. */
#ifndef GCC_PHAT_SAMPLE_RATE
#define GCC_PHAT_SAMPLE_RATE    1000000
#endif

/** Number of sensor channels (8 for dual-delta LOMAH array). */
#ifndef GCC_PHAT_NUM_CHANNELS
#define GCC_PHAT_NUM_CHANNELS   8
#endif

/** Maximum expected TDOA in samples. Limits peak search window.
 *  At 1 MHz, max sensor spacing ~0.3m → max TDOA = 0.3/343 ≈ 875 μs.
 *  Set to 1024 to allow wider search. */
#ifndef GCC_PHAT_MAX_DELAY
#define GCC_PHAT_MAX_DELAY      900
#endif

/** Epsilon for PHAT normalization to avoid division by zero. */
#ifndef GCC_PHAT_EPSILON
#define GCC_PHAT_EPSILON        1e-10f
#endif

/** Number of unique sensor pairs: C(8,2) = 28 for 8 sensors. */
#define GCC_PHAT_NUM_PAIRS      ((GCC_PHAT_NUM_CHANNELS * (GCC_PHAT_NUM_CHANNELS - 1)) / 2)

/* ---- Data Types ---- */

/** Result of a single TDOA estimation between two sensors. */
typedef struct {
    int16_t  sensor_a;          /**< Index of first sensor (0-7) */
    int16_t  sensor_b;          /**< Index of second sensor (0-7) */
    float    tdoa_samples;      /**< TDOA in fractional samples (sub-sample interpolation) */
    float    tdoa_seconds;      /**< TDOA in seconds */
    float    peak_value;        /**< Normalized correlation peak (0-1, confidence) */
    bool     valid;             /**< True if peak exceeds threshold */
} gcc_phat_tdoa_t;

/** Result of multilateration: estimated (X, Y) position. */
typedef struct {
    float x_mm;                 /**< X position in mm relative to array center */
    float y_mm;                 /**< Y position in mm relative to array center */
    float residual;             /**< Least-squares residual (quality metric) */
    bool  valid;                /**< True if solution converged */
    uint32_t compute_us;        /**< Total computation time in microseconds */
} lomah_position_t;

/** Sensor position in the array (known, fixed geometry). */
typedef struct {
    float x_mm;                 /**< X position of sensor in mm */
    float y_mm;                 /**< Y position of sensor in mm */
} sensor_pos_t;

/** GCC-PHAT processing context (persistent state). */
typedef struct {
    /* FFT buffers (CMSIS-DSP requires specific alignment) */
    float fft_buf_a[GCC_PHAT_FFT_SIZE * 2];   /**< Complex FFT of channel A */
    float fft_buf_b[GCC_PHAT_FFT_SIZE * 2];   /**< Complex FFT of channel B */
    float gcc_buf[GCC_PHAT_FFT_SIZE * 2];      /**< Complex GCC result */
    float gcc_mag[GCC_PHAT_FFT_SIZE];          /**< Real GCC magnitude (after IFFT) */

    /* Configuration */
    float    sample_rate_hz;
    float    speed_of_sound;     /**< m/s, updated by temperature compensation */
    float    peak_threshold;     /**< Minimum peak value for valid TDOA */

    /* Sensor geometry */
    sensor_pos_t sensors[GCC_PHAT_NUM_CHANNELS];

    /* Temperature compensation */
    float    temperature_c;      /**< Current ambient temperature */

    /* Performance tracking */
    uint32_t last_compute_us;
    uint32_t total_computes;
} gcc_phat_ctx_t;

/* ---- API Functions ---- */

/**
 * @brief Initialize GCC-PHAT context with default parameters.
 * @param ctx           Pointer to context structure
 * @param sample_rate   ADC sample rate in Hz (e.g., 1000000)
 * @param temperature_c Ambient temperature in Celsius for speed-of-sound calc
 */
void gcc_phat_init(gcc_phat_ctx_t *ctx, float sample_rate, float temperature_c);

/**
 * @brief Set sensor array geometry (must be called after init).
 * @param ctx     Context
 * @param sensors Array of sensor positions (GCC_PHAT_NUM_CHANNELS elements)
 */
void gcc_phat_set_geometry(gcc_phat_ctx_t *ctx, const sensor_pos_t *sensors);

/**
 * @brief Update temperature for speed-of-sound compensation.
 *        c(T) = 331.3 + 0.606 * T  (m/s, T in Celsius)
 * @param ctx           Context
 * @param temperature_c New temperature in Celsius
 */
void gcc_phat_update_temperature(gcc_phat_ctx_t *ctx, float temperature_c);

/**
 * @brief Set the correlation peak threshold for valid detection.
 * @param ctx       Context
 * @param threshold Value between 0.0 and 1.0 (default: 0.15)
 */
void gcc_phat_set_threshold(gcc_phat_ctx_t *ctx, float threshold);

/**
 * @brief Compute TDOA between two sensor channels using GCC-PHAT.
 *
 * This is the core algorithm:
 *   1. FFT(signal_a) → X
 *   2. FFT(signal_b) → Y
 *   3. G = X * conj(Y)
 *   4. G_phat = G / |G|
 *   5. R = IFFT(G_phat)
 *   6. Find peak → TDOA
 *   7. Parabolic interpolation for sub-sample accuracy
 *
 * @param ctx       Context (provides buffers and config)
 * @param signal_a  Sensor A samples (GCC_PHAT_FFT_SIZE floats)
 * @param signal_b  Sensor B samples (GCC_PHAT_FFT_SIZE floats)
 * @param sensor_a  Index of sensor A
 * @param sensor_b  Index of sensor B
 * @param result    Output TDOA result
 */
void gcc_phat_compute_tdoa(gcc_phat_ctx_t *ctx,
                           const float *signal_a,
                           const float *signal_b,
                           int sensor_a,
                           int sensor_b,
                           gcc_phat_tdoa_t *result);

/**
 * @brief Compute all pairwise TDOAs for the sensor array.
 *
 * Processes all C(N,2) sensor pairs from a single shockwave event.
 * For 8 sensors: 28 pairs.
 *
 * @param ctx       Context
 * @param signals   Array of N channel buffers [N][GCC_PHAT_FFT_SIZE]
 * @param results   Output array of TDOA results (GCC_PHAT_NUM_PAIRS elements)
 * @return          Number of valid TDOA pairs (above threshold)
 */
int gcc_phat_compute_all_tdoas(gcc_phat_ctx_t *ctx,
                               const float signals[][GCC_PHAT_FFT_SIZE],
                               gcc_phat_tdoa_t *results);

/**
 * @brief Estimate (X, Y) position from TDOA measurements via multilateration.
 *
 * Uses iterative least-squares to find the position that best fits
 * the measured TDOAs given known sensor positions and speed of sound.
 *
 * @param ctx       Context (sensor geometry and speed of sound)
 * @param tdoas     Array of TDOA results from gcc_phat_compute_all_tdoas
 * @param num_tdoas Number of valid TDOA measurements
 * @param position  Output estimated position
 */
void gcc_phat_multilaterate(gcc_phat_ctx_t *ctx,
                            const gcc_phat_tdoa_t *tdoas,
                            int num_tdoas,
                            lomah_position_t *position);

/**
 * @brief Full pipeline: from raw samples to (X, Y) position.
 *
 * Convenience function that calls:
 *   gcc_phat_compute_all_tdoas() → gcc_phat_multilaterate()
 *
 * @param ctx       Initialized context with geometry set
 * @param signals   Raw ADC samples [N_CHANNELS][FFT_SIZE]
 * @param position  Output position estimate
 * @return          Number of valid TDOA pairs used
 */
int gcc_phat_process_shot(gcc_phat_ctx_t *ctx,
                          const float signals[][GCC_PHAT_FFT_SIZE],
                          lomah_position_t *position);

#endif /* GCC_PHAT_H */
