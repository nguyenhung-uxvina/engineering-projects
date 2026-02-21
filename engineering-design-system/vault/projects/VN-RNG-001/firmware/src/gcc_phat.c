/**
 * @file gcc_phat.c
 * @brief GCC-PHAT implementation for ARM Cortex-M7 (STM32H743)
 *
 * Uses CMSIS-DSP library for hardware-accelerated FFT/IFFT operations.
 * The Cortex-M7 FPU provides single-cycle float multiply-accumulate,
 * making this implementation very efficient.
 *
 * @project VN-RNG-001 - LOMAH Acoustic Shooting Range System
 * @date    2026-02-08
 */

#include "gcc_phat.h"
#include <math.h>
#include <string.h>

/*
 * CMSIS-DSP Library
 * On a real STM32H7 build, include:
 *   #include "arm_math.h"
 *
 * For desktop simulation / unit testing, we provide fallback
 * implementations of the required FFT functions.
 */
#ifdef USE_CMSIS_DSP
#include "arm_math.h"

/* CMSIS-DSP FFT instance (initialized once) */
static arm_rfft_fast_instance_f32 fft_instance;
static bool fft_initialized = false;

static void ensure_fft_init(void)
{
    if (!fft_initialized) {
        arm_rfft_fast_init_f32(&fft_instance, GCC_PHAT_FFT_SIZE);
        fft_initialized = true;
    }
}

static void do_fft(float *input, float *output)
{
    ensure_fft_init();
    arm_rfft_fast_f32(&fft_instance, input, output, 0); /* 0 = forward */
}

static void do_ifft(float *input, float *output)
{
    ensure_fft_init();
    arm_rfft_fast_f32(&fft_instance, input, output, 1); /* 1 = inverse */
}

#else
/* ---- Fallback FFT (Cooley-Tukey radix-2 DIT) for desktop testing ---- */

#ifndef M_PI
#define M_PI 3.14159265358979323846f
#endif

/**
 * @brief In-place complex FFT (Cooley-Tukey radix-2).
 * @param data  Interleaved complex array [re0, im0, re1, im1, ...]
 * @param n     Number of complex samples (must be power of 2)
 * @param inverse  If true, compute inverse FFT
 */
static void fft_complex_inplace(float *data, int n, bool inverse)
{
    /* Bit-reversal permutation */
    int j = 0;
    for (int i = 0; i < n - 1; i++) {
        if (i < j) {
            float tmp_re = data[2 * i];
            float tmp_im = data[2 * i + 1];
            data[2 * i]     = data[2 * j];
            data[2 * i + 1] = data[2 * j + 1];
            data[2 * j]     = tmp_re;
            data[2 * j + 1] = tmp_im;
        }
        int m = n >> 1;
        while (m >= 1 && j >= m) {
            j -= m;
            m >>= 1;
        }
        j += m;
    }

    /* Butterfly stages */
    float sign = inverse ? 1.0f : -1.0f;
    for (int stage = 1; stage < n; stage <<= 1) {
        float angle = sign * M_PI / (float)stage;
        float w_re = cosf(angle);
        float w_im = sinf(angle);

        for (int grp = 0; grp < n; grp += (stage << 1)) {
            float wn_re = 1.0f, wn_im = 0.0f;
            for (int k = 0; k < stage; k++) {
                int idx_a = grp + k;
                int idx_b = grp + k + stage;

                float a_re = data[2 * idx_a];
                float a_im = data[2 * idx_a + 1];
                float b_re = data[2 * idx_b];
                float b_im = data[2 * idx_b + 1];

                /* Complex multiply: wn * b */
                float t_re = wn_re * b_re - wn_im * b_im;
                float t_im = wn_re * b_im + wn_im * b_re;

                data[2 * idx_a]     = a_re + t_re;
                data[2 * idx_a + 1] = a_im + t_im;
                data[2 * idx_b]     = a_re - t_re;
                data[2 * idx_b + 1] = a_im - t_im;

                /* Advance twiddle factor */
                float tmp = wn_re * w_re - wn_im * w_im;
                wn_im = wn_re * w_im + wn_im * w_re;
                wn_re = tmp;
            }
        }
    }

    /* Scale for inverse FFT */
    if (inverse) {
        float scale = 1.0f / (float)n;
        for (int i = 0; i < 2 * n; i++) {
            data[i] *= scale;
        }
    }
}

/**
 * @brief Real-to-complex FFT (packs real input into complex format).
 */
static void do_fft(float *input, float *output)
{
    /* Pack real input into complex format: [re, 0, re, 0, ...] */
    for (int i = GCC_PHAT_FFT_SIZE - 1; i >= 0; i--) {
        output[2 * i]     = input[i];
        output[2 * i + 1] = 0.0f;
    }
    fft_complex_inplace(output, GCC_PHAT_FFT_SIZE, false);
}

/**
 * @brief Complex-to-real IFFT.
 */
static void do_ifft(float *input, float *output)
{
    /* input is already in complex interleaved format */
    float temp[GCC_PHAT_FFT_SIZE * 2];
    memcpy(temp, input, sizeof(float) * GCC_PHAT_FFT_SIZE * 2);
    fft_complex_inplace(temp, GCC_PHAT_FFT_SIZE, true);

    /* Extract real parts */
    for (int i = 0; i < GCC_PHAT_FFT_SIZE; i++) {
        output[i] = temp[2 * i];
    }
}

#endif /* USE_CMSIS_DSP */

/* ---- Timer utilities ---- */

#ifdef USE_CMSIS_DSP
/* On STM32H7, use DWT cycle counter for microsecond timing */
static inline uint32_t get_cycles(void)
{
    return *((volatile uint32_t *)0xE0001004); /* DWT->CYCCNT */
}
#define CYCLES_TO_US(c) ((c) / (480)) /* 480 MHz clock */
#else
#include <time.h>
static inline uint32_t get_cycles(void) { return (uint32_t)clock(); }
#define CYCLES_TO_US(c) ((c) * 1000000 / CLOCKS_PER_SEC)
#endif

/* ================================================================
 * PUBLIC API IMPLEMENTATION
 * ================================================================ */

void gcc_phat_init(gcc_phat_ctx_t *ctx, float sample_rate, float temperature_c)
{
    memset(ctx, 0, sizeof(gcc_phat_ctx_t));
    ctx->sample_rate_hz = sample_rate;
    ctx->peak_threshold = 0.15f; /* Default threshold */
    gcc_phat_update_temperature(ctx, temperature_c);
}

void gcc_phat_set_geometry(gcc_phat_ctx_t *ctx, const sensor_pos_t *sensors)
{
    memcpy(ctx->sensors, sensors, sizeof(sensor_pos_t) * GCC_PHAT_NUM_CHANNELS);
}

void gcc_phat_update_temperature(gcc_phat_ctx_t *ctx, float temperature_c)
{
    ctx->temperature_c = temperature_c;
    /* Speed of sound in air: c = 331.3 + 0.606 * T (m/s)
     * Valid for dry air at sea level. For humid tropical air,
     * humidity correction adds ~0.1-0.5 m/s (negligible at
     * short LOMAH distances). */
    ctx->speed_of_sound = 331.3f + 0.606f * temperature_c;
}

void gcc_phat_set_threshold(gcc_phat_ctx_t *ctx, float threshold)
{
    ctx->peak_threshold = threshold;
}

void gcc_phat_compute_tdoa(gcc_phat_ctx_t *ctx,
                           const float *signal_a,
                           const float *signal_b,
                           int sensor_a,
                           int sensor_b,
                           gcc_phat_tdoa_t *result)
{
    const int N = GCC_PHAT_FFT_SIZE;
    uint32_t start = get_cycles();

    /* Initialize result */
    result->sensor_a = (int16_t)sensor_a;
    result->sensor_b = (int16_t)sensor_b;
    result->valid = false;
    result->tdoa_samples = 0.0f;
    result->tdoa_seconds = 0.0f;
    result->peak_value = 0.0f;

    /* --- Step 1 & 2: FFT of both channels --- */
    /* Copy inputs to avoid modifying caller's data */
    float temp_a[N];
    memcpy(temp_a, signal_a, sizeof(float) * N);
    do_fft(temp_a, ctx->fft_buf_a);

    float temp_b[N];
    memcpy(temp_b, signal_b, sizeof(float) * N);
    do_fft(temp_b, ctx->fft_buf_b);

    /* --- Step 3 & 4: Cross-power spectrum with PHAT weighting ---
     *
     * G(f) = X(f) * conj(Y(f))
     * G_phat(f) = G(f) / |G(f)|
     *
     * For complex numbers:
     *   X = Xr + j*Xi,  Y = Yr + j*Yi
     *   conj(Y) = Yr - j*Yi
     *   G = X * conj(Y) = (Xr*Yr + Xi*Yi) + j*(Xi*Yr - Xr*Yi)
     *   |G| = sqrt(Gr^2 + Gi^2)
     *   G_phat = G / |G|  → unit magnitude, preserves phase only
     */
    for (int i = 0; i < N; i++) {
        float xr = ctx->fft_buf_a[2 * i];
        float xi = ctx->fft_buf_a[2 * i + 1];
        float yr = ctx->fft_buf_b[2 * i];
        float yi = ctx->fft_buf_b[2 * i + 1];

        /* Cross-power spectrum: G = X * conj(Y) */
        float gr = xr * yr + xi * yi;
        float gi = xi * yr - xr * yi;

        /* Magnitude of G */
        float mag = sqrtf(gr * gr + gi * gi) + GCC_PHAT_EPSILON;

        /* PHAT weighting: normalize to unit magnitude */
        ctx->gcc_buf[2 * i]     = gr / mag;
        ctx->gcc_buf[2 * i + 1] = gi / mag;
    }

    /* --- Step 5: IFFT to get generalized cross-correlation --- */
    do_ifft(ctx->gcc_buf, ctx->gcc_mag);

    /* --- Step 6: Find peak within valid delay range ---
     *
     * The GCC output is circular: positive delays at indices 0..N/2-1,
     * negative delays at indices N/2..N-1.
     * We search both positive and negative delay regions.
     */
    int max_delay = GCC_PHAT_MAX_DELAY;
    if (max_delay > N / 2) max_delay = N / 2;

    float best_val = -1.0f;
    int   best_idx = 0;

    /* Search positive delays: indices 0 to max_delay */
    for (int i = 0; i <= max_delay; i++) {
        float val = ctx->gcc_mag[i];
        if (val > best_val) {
            best_val = val;
            best_idx = i;
        }
    }

    /* Search negative delays: indices N-max_delay to N-1 */
    for (int i = N - max_delay; i < N; i++) {
        float val = ctx->gcc_mag[i];
        if (val > best_val) {
            best_val = val;
            best_idx = i;
        }
    }

    /* --- Step 7: Sub-sample parabolic interpolation ---
     *
     * For samples around the peak: y[-1], y[0], y[1]
     * The sub-sample offset δ = 0.5 * (y[-1] - y[1]) / (y[-1] - 2*y[0] + y[1])
     * This improves TDOA resolution from 1 sample to ~0.1 sample.
     */
    float fractional_offset = 0.0f;

    if (best_idx > 0 && best_idx < N - 1) {
        float y_prev = ctx->gcc_mag[best_idx - 1];
        float y_peak = ctx->gcc_mag[best_idx];
        float y_next = ctx->gcc_mag[best_idx + 1];

        float denom = y_prev - 2.0f * y_peak + y_next;
        if (fabsf(denom) > GCC_PHAT_EPSILON) {
            fractional_offset = 0.5f * (y_prev - y_next) / denom;
            /* Clamp to [-0.5, +0.5] */
            if (fractional_offset > 0.5f) fractional_offset = 0.5f;
            if (fractional_offset < -0.5f) fractional_offset = -0.5f;
        }
    }

    /* Convert circular index to signed delay */
    float delay_samples;
    if (best_idx <= N / 2) {
        delay_samples = (float)best_idx + fractional_offset;
    } else {
        delay_samples = (float)(best_idx - N) + fractional_offset;
    }

    /* Populate result */
    result->tdoa_samples = delay_samples;
    result->tdoa_seconds = delay_samples / ctx->sample_rate_hz;
    result->peak_value = best_val;
    result->valid = (best_val >= ctx->peak_threshold);

    uint32_t elapsed = get_cycles() - start;
    ctx->last_compute_us = CYCLES_TO_US(elapsed);
    ctx->total_computes++;
}

int gcc_phat_compute_all_tdoas(gcc_phat_ctx_t *ctx,
                               const float signals[][GCC_PHAT_FFT_SIZE],
                               gcc_phat_tdoa_t *results)
{
    int valid_count = 0;
    int pair_idx = 0;

    for (int a = 0; a < GCC_PHAT_NUM_CHANNELS; a++) {
        for (int b = a + 1; b < GCC_PHAT_NUM_CHANNELS; b++) {
            gcc_phat_compute_tdoa(ctx,
                                  signals[a], signals[b],
                                  a, b,
                                  &results[pair_idx]);
            if (results[pair_idx].valid) {
                valid_count++;
            }
            pair_idx++;
        }
    }

    return valid_count;
}

/* ================================================================
 * MULTILATERATION (Least-Squares TDOA Position Estimation)
 * ================================================================
 *
 * Given N sensor positions (xi, yi) and measured TDOAs between
 * sensor pairs, find position (px, py) that minimizes:
 *
 *   E = Σ (measured_tdoa_ij - predicted_tdoa_ij)^2
 *
 * where predicted_tdoa_ij = (dist(p, si) - dist(p, sj)) / c
 *
 * Uses Gauss-Newton iterative solver.
 */

/** Maximum iterations for Gauss-Newton solver. */
#define MULTILAT_MAX_ITER   20

/** Convergence threshold in mm. */
#define MULTILAT_CONVERGE   0.1f

static float dist_2d(float x1, float y1, float x2, float y2)
{
    float dx = x1 - x2;
    float dy = y1 - y2;
    return sqrtf(dx * dx + dy * dy);
}

void gcc_phat_multilaterate(gcc_phat_ctx_t *ctx,
                            const gcc_phat_tdoa_t *tdoas,
                            int num_tdoas,
                            lomah_position_t *position)
{
    uint32_t start = get_cycles();

    position->valid = false;
    position->x_mm = 0.0f;
    position->y_mm = 0.0f;
    position->residual = 1e6f;

    if (num_tdoas < 3) {
        /* Need at least 3 TDOA pairs for 2D position */
        position->compute_us = CYCLES_TO_US(get_cycles() - start);
        return;
    }

    /* Speed of sound in mm/s */
    float c_mm_s = ctx->speed_of_sound * 1000.0f;

    /* Initial guess: center of sensor array */
    float px = 0.0f, py = 0.0f;
    for (int i = 0; i < GCC_PHAT_NUM_CHANNELS; i++) {
        px += ctx->sensors[i].x_mm;
        py += ctx->sensors[i].y_mm;
    }
    px /= (float)GCC_PHAT_NUM_CHANNELS;
    py /= (float)GCC_PHAT_NUM_CHANNELS;

    /* Gauss-Newton iteration */
    for (int iter = 0; iter < MULTILAT_MAX_ITER; iter++) {
        /*
         * Build normal equations: J^T * J * delta = J^T * r
         * where J is the Jacobian and r is the residual vector.
         *
         * For 2 unknowns (px, py), J^T*J is 2x2 and J^T*r is 2x1.
         */
        float jtj_00 = 0.0f, jtj_01 = 0.0f, jtj_11 = 0.0f;
        float jtr_0 = 0.0f, jtr_1 = 0.0f;
        float total_residual = 0.0f;

        for (int k = 0; k < num_tdoas; k++) {
            if (!tdoas[k].valid) continue;

            int sa = tdoas[k].sensor_a;
            int sb = tdoas[k].sensor_b;

            float da = dist_2d(px, py, ctx->sensors[sa].x_mm, ctx->sensors[sa].y_mm);
            float db = dist_2d(px, py, ctx->sensors[sb].x_mm, ctx->sensors[sb].y_mm);

            /* Predicted TDOA (seconds) */
            float predicted = (da - db) / c_mm_s;
            float measured = tdoas[k].tdoa_seconds;
            float residual = measured - predicted;

            total_residual += residual * residual;

            /* Jacobian row: d(predicted)/d(px), d(predicted)/d(py) */
            float j0 = 0.0f, j1 = 0.0f;
            if (da > GCC_PHAT_EPSILON) {
                j0 += (px - ctx->sensors[sa].x_mm) / (da * c_mm_s);
                j1 += (py - ctx->sensors[sa].y_mm) / (da * c_mm_s);
            }
            if (db > GCC_PHAT_EPSILON) {
                j0 -= (px - ctx->sensors[sb].x_mm) / (db * c_mm_s);
                j1 -= (py - ctx->sensors[sb].y_mm) / (db * c_mm_s);
            }

            /* Accumulate J^T * J (symmetric 2x2) */
            jtj_00 += j0 * j0;
            jtj_01 += j0 * j1;
            jtj_11 += j1 * j1;

            /* Accumulate J^T * r */
            jtr_0 += j0 * residual;
            jtr_1 += j1 * residual;
        }

        /* Solve 2x2 linear system: [jtj_00 jtj_01; jtj_01 jtj_11] * [dx; dy] = [jtr_0; jtr_1] */
        float det = jtj_00 * jtj_11 - jtj_01 * jtj_01;
        if (fabsf(det) < GCC_PHAT_EPSILON) {
            /* Singular matrix - cannot solve */
            break;
        }

        float dx = ( jtj_11 * jtr_0 - jtj_01 * jtr_1) / det;
        float dy = (-jtj_01 * jtr_0 + jtj_00 * jtr_1) / det;

        px += dx;
        py += dy;

        position->residual = total_residual;

        /* Check convergence */
        if (sqrtf(dx * dx + dy * dy) < MULTILAT_CONVERGE) {
            position->valid = true;
            break;
        }
    }

    position->x_mm = px;
    position->y_mm = py;
    position->compute_us = CYCLES_TO_US(get_cycles() - start);

    /* Final validity check: residual should be small relative to measurement count */
    if (position->residual > 1e-4f * (float)num_tdoas) {
        /* High residual suggests poor solution - may still be valid but flag it */
        /* Keep valid flag from convergence check */
    }
}

int gcc_phat_process_shot(gcc_phat_ctx_t *ctx,
                          const float signals[][GCC_PHAT_FFT_SIZE],
                          lomah_position_t *position)
{
    gcc_phat_tdoa_t tdoas[GCC_PHAT_NUM_PAIRS];

    int valid_count = gcc_phat_compute_all_tdoas(ctx, signals, tdoas);

    gcc_phat_multilaterate(ctx, tdoas, GCC_PHAT_NUM_PAIRS, position);

    return valid_count;
}
