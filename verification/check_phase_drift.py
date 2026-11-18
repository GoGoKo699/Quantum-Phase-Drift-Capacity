#!/usr/bin/env python3
"""Finite diagnostics for the phase-drift proofs, not capacity simulations.

Run from any working directory:
    python verification/check_phase_drift.py
    python verification/check_phase_drift.py --output results.json

The program prints a JSON summary. The optional output file contains every
checked case, tolerances, and dependency versions. Importing this module runs
no diagnostics and writes no files. All checks are deterministic enumerations
or quadrature of an analytically evaluated integral.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
import platform
from typing import Any

import numpy as np
import scipy
from scipy.integrate import quad


ALGEBRA_TOL = 1e-12
ENTROPY_TOL = 1e-10
INTEGRAL_TOL = 1e-6


class DiagnosticFailure(RuntimeError):
    """A finite numerical check failed its stated tolerance."""


def require(condition: bool, message: str) -> None:
    """Raise even when Python is run with optimization enabled."""
    if not condition:
        raise DiagnosticFailure(message)


def max_abs(array: np.ndarray) -> float:
    return float(np.max(np.abs(array), initial=0.0))


def bits(n: int) -> np.ndarray:
    require(n >= 1, "The number of carriers must be positive.")
    return np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int64)


def differences(n: int) -> np.ndarray:
    strings = bits(n)
    return strings[:, None, :] - strings[None, :, :]


def schur(
    n: int, kappa: float, kind: str, gaps: list[int] | None = None
) -> np.ndarray:
    """Stationary Brownian/reset Schur matrix on selected carrier slots."""
    require(kind in ("brownian", "reset"), f"Unknown model: {kind}")
    require(math.isfinite(kappa) and kappa >= 0, "Invalid kappa.")
    gap_array = np.ones(n - 1, dtype=np.int64)
    if gaps is not None:
        raw_gaps = np.asarray(gaps)
        require(raw_gaps.shape == (n - 1,), "Incorrect number of slot gaps.")
        require(
            bool(np.all(np.isfinite(raw_gaps)))
            and bool(np.all(raw_gaps > 0))
            and bool(np.all(raw_gaps == np.rint(raw_gaps))),
            "Selected-slot gaps must be positive integers.",
        )
        gap_array = raw_gaps.astype(np.int64)
    diff = differences(n)
    suffix = np.flip(np.cumsum(np.flip(diff, axis=2), axis=2), axis=2)
    neutral = suffix[:, :, 0] == 0
    charges = suffix[:, :, 1:]
    costs = charges**2 if kind == "brownian" else charges != 0
    action = costs @ gap_array
    return neutral * np.exp(-0.5 * kappa * action)


def gaussian_schur(covariance: np.ndarray, common_twirl: bool) -> np.ndarray:
    """Schur matrix of Gaussian phases, optionally with a uniform common phase."""
    n = covariance.shape[0]
    diff = differences(n)
    quadratic = np.einsum("abi,ij,abj->ab", diff, covariance, diff)
    matrix = np.exp(-0.5 * quadratic)
    if common_twirl:
        matrix *= diff.sum(axis=2) == 0
    return matrix


def entropy(eigenvalues: np.ndarray, context: str) -> float:
    """Entropy of a normalized spectrum, checking numerical positivity."""
    values = np.asarray(eigenvalues, dtype=float)
    require(bool(np.all(np.isfinite(values))), f"{context}: nonfinite spectrum.")
    require(
        float(values.min()) >= -ALGEBRA_TOL,
        f"{context}: negative eigenvalue {values.min():.6g}.",
    )
    require(
        abs(float(values.sum()) - 1.0) <= ENTROPY_TOL,
        f"{context}: spectrum is not normalized.",
    )
    positive = values[values > 0]
    return float(-np.dot(positive, np.log2(positive)))


def binary_entropy(p: float) -> float:
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def binomial_entropy(n: int) -> float:
    probabilities = np.array([math.comb(n, j) / (2**n) for j in range(n + 1)])
    return entropy(probabilities, f"Binomial({n}, 1/2)")


def bose_entropy(occupation: float) -> float:
    """Thermal bosonic entropy, evaluated without large-occupation cancellation."""
    if occupation == 0:
        return 0.0
    require(occupation > 0, "Negative thermal occupation.")
    log_one_plus = math.log1p(occupation)
    if occupation < 1:
        second_term = occupation * (log_one_plus - math.log(occupation))
    else:
        second_term = occupation * math.log1p(1 / occupation)
    return (log_one_plus + second_term) / math.log(2)


def occupation_from_variance(a: float) -> float:
    """(sqrt(1+a)-1)/2, rationalized to avoid cancellation at small a."""
    return a / (2 * (math.sqrt(1 + a) + 1))


def check_selected_slots() -> list[dict[str, Any]]:
    results = []
    for n in (1, 2, 3):
        for kappa in (0.001, 0.1, 0.7):
            gaps = [j + 2 for j in range(n - 1)]
            error = max_abs(
                schur(n, kappa, "brownian", gaps)
                - schur(n, kappa, "reset", gaps)
            )
            require(error < ALGEBRA_TOL, f"{n}-slot equality failed at {kappa}.")
            results.append(
                {"n": n, "kappa": kappa, "gaps": gaps, "max_difference": error}
            )
    return results


def check_four_slot_witness() -> dict[str, float]:
    kappa = 0.2
    brownian = float(schur(4, kappa, "brownian")[3, 12])
    reset = float(schur(4, kappa, "reset")[3, 12])
    require(
        abs(brownian - math.exp(-3 * kappa)) < ALGEBRA_TOL,
        "Four-slot Brownian witness failed.",
    )
    require(
        abs(reset - math.exp(-1.5 * kappa)) < ALGEBRA_TOL,
        "Four-slot reset witness failed.",
    )
    require(reset > brownian, "Four-slot witness did not distinguish the models.")
    return {
        "kappa": kappa,
        "brownian": brownian,
        "reset": reset,
        "specified_probe_success_probability": 0.5 + (reset - brownian) / 4,
    }


def check_block_factorization() -> list[dict[str, Any]]:
    results = []
    for kind in ("brownian", "reset"):
        for n1, n2 in ((1, 2), (2, 2), (2, 3)):
            strings = bits(n1 + n2)
            weights1 = strings[:, :n1].sum(axis=1)
            weights2 = strings[:, n1:].sum(axis=1)
            neutral1 = weights1[:, None] == weights1[None, :]
            neutral2 = weights2[:, None] == weights2[None, :]
            joint = schur(n1 + n2, 0.17, kind) * neutral1 * neutral2
            product = np.kron(schur(n1, 0.17, kind), schur(n2, 0.17, kind))
            error = max_abs(joint - product)
            require(error < ALGEBRA_TOL, f"{kind} block factorization failed.")
            results.append(
                {"kind": kind, "blocks": [n1, n2], "max_difference": error}
            )
    return results


def check_four_slot_optimum() -> list[dict[str, Any]]:
    """Check the full four-slot channel difference and its reference-assisted witness."""
    results = []
    cases = (
        (0.0, [1, 1, 1]),
        (0.2, [1, 1, 1]),
        (0.1, [3, 7, 2]),
        (0.01, [1, 92, 1]),
    )
    for kappa, gaps in cases:
        delta = math.exp(-0.5 * kappa * sum(gaps)) * -math.expm1(-1.5 * kappa * gaps[1])
        expected = np.zeros((16, 16))
        expected[3, 12] = expected[12, 3] = delta
        difference = schur(4, kappa, "reset", gaps) - schur(4, kappa, "brownian", gaps)
        kernel_residual = max_abs(difference - expected)
        require(kernel_residual < ALGEBRA_TOL, "Unexpected four-slot Schur entry.")

        # Use a common or an orthogonal private reference for the two branches.
        residuals = []
        for weight, reference_branch in ((0.5, 0), (0.5, 1), (0.2, 1)):
            state = np.zeros((16, 2), dtype=complex)
            state[3, 0] = math.sqrt(weight)
            state[12, reference_branch] = 1j * math.sqrt(1.0 - weight)
            output_difference = difference[:, None, :, None] * np.einsum(
                "ir,js->irjs", state, state.conj()
            )
            eigenvalues = np.linalg.eigvalsh(output_difference.reshape(32, 32))
            trace_norm = float(np.abs(eigenvalues).sum())
            residual = abs(trace_norm - 2 * delta * math.sqrt(weight * (1.0 - weight)))
            require(residual < ALGEBRA_TOL, "Four-slot trace-norm identity failed.")
            residuals.append(residual)
        results.append({
            "kappa": kappa,
            "gaps": gaps,
            "kernel_residual": kernel_residual,
            "reference_checks": len(residuals),
            "trace_norm_residual": max(residuals),
            "optimal_equal_prior_success": 0.5 + delta / 4,
        })
    return results


def check_group_moments() -> list[dict[str, Any]]:
    """Compare the phase covariance by two routes and evaluate count moments."""
    results = []
    cases = (
        (1, 5, 0.04, 4),
        (1, 7, 0.02, 2),
        (2, 4, 0.02, 2),
        (3, 3, 0.006, 2),
        (5, 4, 0.001, 2),
    )
    for m, groups, kappa, divisor in cases:
        half = m * groups
        carriers = 2 * half
        weights = np.zeros((groups, carriers), dtype=np.int64)
        for group in range(groups):
            early = slice(group * m, (group + 1) * m)
            late = slice(half + early.start, half + early.stop)
            weights[group, early] = 1
            weights[group, late] = -1
        require(
            bool(np.all(weights.sum(axis=1) == 0)),
            "Probe group is sensitive to common phase.",
        )
        steps = np.arange(carriers)
        clock_cov = kappa * np.minimum.outer(steps, steps)
        phase_cov = weights @ clock_cov @ weights.T
        suffix = np.cumsum(weights[:, ::-1], axis=1)[:, -2::-1]
        covariance_residual = max_abs(phase_cov - kappa * (suffix @ suffix.T))
        require(covariance_residual < ALGEBRA_TOL, "Group phase covariance mismatch.")
        variances = phase_cov.diagonal()
        lower = kappa * m**2 * (half - m + 1)
        upper = kappa * m**2 * half
        require(
            bool(np.all(variances >= lower - ALGEBRA_TOL))
            and bool(np.all(variances <= upper + ALGEBRA_TOL)),
            "Group phase variance lies outside its analytic bounds.",
        )

        # The readout indicators are independent given the trajectory.
        # Their unconditional pair moments retain correlated phases.
        cosine_mean = np.exp(-variances / 2)
        means = (1.0 - cosine_mean) / divisor
        cosine_products = np.outer(cosine_mean, cosine_mean) * np.cosh(phase_cov)
        pair_moments = (
            1.0 - cosine_mean[:, None] - cosine_mean[None, :] + cosine_products
        ) / divisor**2
        np.fill_diagonal(pair_moments, means)
        first_moment = float(means.sum())
        second_moment = float(pair_moments.sum())
        gaussian_bound = first_moment + 3 * float(variances.sum())**2 / (4 * divisor**2)
        require(
            second_moment <= gaussian_bound + ALGEBRA_TOL,
            "Count second-moment bound failed.",
        )
        require(second_moment >= first_moment**2, "Inconsistent count moments.")
        results.append({
            "probe": "product_singlets" if divisor == 4 else "balanced_cats",
            "m": m,
            "groups": groups,
            "kappa": kappa,
            "carrier_count": carriers,
            "covariance_residual": covariance_residual,
            "phase_variance": float(variances[0]),
            "mean_count": first_moment,
            "second_moment": second_moment,
            "second_moment_upper_bound": gaussian_bound,
            "paley_zygmund_detection_lower_bound": first_moment**2 / second_moment,
        })
    return results


def check_private_reference_overlap() -> list[dict[str, Any]]:
    """Exercise the deterministic group-overlap inequality with entangled private references."""
    results = []
    for group_sizes, phase_scale in (((1, 1, 1), 0.03), ((2, 2), 0.12), ((3, 1, 2), 0.3)):
        states = []
        rotated = []
        group_losses = []
        group_variances = []
        phase_bound = 0.0
        next_carrier = 0
        for size in group_sizes:
            occupations = bits(size)
            phase = phase_scale * np.arange(next_carrier, next_carrier + size)
            angles = occupations @ phase
            amplitudes = np.column_stack(
                (np.arange(1, 2**size + 1), 1j * (-1.0)**occupations.sum(axis=1))
            )
            amplitudes /= np.linalg.norm(amplitudes)
            probabilities = (np.abs(amplitudes)**2).sum(axis=1)
            variance = float(np.dot(probabilities, (angles - probabilities @ angles)**2))
            shifted = amplitudes * np.exp(1j * angles[:, None])
            loss = 1.0 - abs(np.vdot(amplitudes, shifted))**2
            bound = size * float(phase @ phase) / 4
            require(
                loss <= variance + ALGEBRA_TOL and variance <= bound + ALGEBRA_TOL,
                "Group overlap bound failed.",
            )
            states.append(amplitudes.ravel())
            rotated.append(shifted.ravel())
            group_losses.append(loss)
            group_variances.append(variance)
            phase_bound += bound
            next_carrier += size
        state = np.array([1.0])
        shifted_state = np.array([1.0])
        for block, shifted_block in zip(states, rotated, strict=True):
            state = np.kron(state, block)
            shifted_state = np.kron(shifted_state, shifted_block)
        loss = 1.0 - abs(np.vdot(state, shifted_state))**2
        require(
            loss <= sum(group_losses) + ALGEBRA_TOL,
            "Product overlap loss is not bounded by group losses.",
        )
        results.append({
            "group_sizes": group_sizes,
            "phase_scale": phase_scale,
            "overlap_loss": loss,
            "sum_group_variances": sum(group_variances),
            "phase_quadratic_bound": phase_bound,
        })
    return results


def check_depth_schedule() -> list[dict[str, Any]]:
    """Check uniform rounding on both sides of the depth-saturation scale."""
    results = []
    for kappa in (1 / 64, 1e-4, 1e-8):
        inverse_cube_root = (1 / kappa)**(1 / 3)
        max_half = max(1, math.floor(inverse_cube_root / 2 + ALGEBRA_TOL))
        for depth in (1, 2, 5, 31, 513):
            m = 1 if depth == 1 else min(depth // 2, max_half)
            groups = math.ceil((kappa * m**3)**-0.5)
            carriers = 2 * m * groups
            scale = max(inverse_cube_root, (kappa * depth)**-0.5)
            phase_count_scale = kappa * m**3 * groups**2
            require(depth == 1 or 2 * m <= depth, "Construction exceeds entanglement depth.")
            require(groups >= 2, "Construction has no gap between groups.")
            require(
                1.0 - ALGEBRA_TOL <= phase_count_scale <= 2.0,
                "Unexpected phase-count scaling.",
            )
            require(1.0 <= carriers / scale <= 8.0, "Unexpected carrier-count scaling.")
            results.append({
                "kappa": kappa,
                "depth": depth,
                "m": m,
                "groups": groups,
                "carrier_count": carriers,
                "carrier_count_over_target_scale": carriers / scale,
                "phase_count_scale": phase_count_scale,
            })
    return results


def check_gaussian_entropy_bounds() -> list[dict[str, Any]]:
    results = []
    for n in (2, 3, 4, 6):
        indices = np.arange(1, n + 1)
        covariance = np.minimum.outer(indices, indices)
        for kappa in (0.01, 0.1, 0.5):
            gram = schur(n, kappa, "brownian") / (2**n)
            actual = entropy(np.linalg.eigvalsh(gram), f"Brownian n={n}")
            gaussian = sum(
                bose_entropy(occupation_from_variance(kappa * eigenvalue))
                for eigenvalue in np.linalg.eigvalsh(covariance)
            )
            bound = binomial_entropy(n) + gaussian
            require(
                actual <= bound + ENTROPY_TOL,
                f"Gaussian entropy bound failed: n={n}, kappa={kappa}.",
            )
            results.append(
                {
                    "n": n,
                    "kappa": kappa,
                    "environment_entropy_bits": actual,
                    "gaussian_bound_bits": bound,
                }
            )
    return results


def check_bridge_moments() -> list[dict[str, Any]]:
    results = []
    for length in (2, 3, 4, 6):
        kappa = 1 / (length * length - 1)
        indices = np.arange(1, length)
        covariance = kappa * (
            np.minimum.outer(indices, indices) - np.outer(indices, indices) / length
        )
        diff = differences(length - 1)
        quadratic = np.einsum("abi,ij,abj->ab", diff, covariance, diff)
        mean = float(quadratic.mean())
        second = float((quadratic**2).mean())
        purity = float(np.exp(-quadratic).mean())
        require(
            abs(mean - kappa * (length * length - 1) / 12) < ALGEBRA_TOL,
            f"Bridge mean failed for L={length}.",
        )
        require(
            second <= 3 * mean * mean + ALGEBRA_TOL,
            f"Bridge second-moment bound failed for L={length}.",
        )
        require(
            1 - purity >= mean - 1.5 * mean * mean - ALGEBRA_TOL,
            f"Bridge purity bound failed for L={length}.",
        )
        results.append(
            {
                "L": length,
                "kappa": kappa,
                "mean_Z": mean,
                "second_Z": second,
                "purity": purity,
            }
        )
    return results


def check_brownian_degradation() -> list[dict[str, Any]]:
    """Check the independent bridge plus interpolation/tail reconstruction."""
    results = []
    for n, length, kappa in ((2, 2, 0.03), (5, 2, 0.2), (6, 3, 0.5), (7, 3, 0.07)):
        complete_blocks, tail = divmod(n, length)
        cumulative = np.tril(np.ones((n, n)))
        interpolation = np.zeros((n, n))
        target_bridge_covariance = np.zeros((n, n))
        for block in range(complete_blocks):
            start, end = block * length, (block + 1) * length
            start_coefficients = (
                np.zeros(n) if start == 0 else cumulative[start - 1]
            )
            end_coefficients = cumulative[end - 1]
            for local_index in range(1, length + 1):
                fraction = local_index / length
                interpolation[start + local_index - 1] = (
                    (1 - fraction) * start_coefficients
                    + fraction * end_coefficients
                )
            indices = np.arange(1, length)
            target_bridge_covariance[start : end - 1, start : end - 1] = kappa * (
                np.minimum.outer(indices, indices)
                - np.outer(indices, indices) / length
            )
        # The enhanced channel transmits the final tail noiselessly; the
        # postprocessing supplies its original, jointly sampled phases.
        interpolation[complete_blocks * length :] = cumulative[
            complete_blocks * length :
        ]
        residual = cumulative - interpolation
        original_covariance = kappa * cumulative @ cumulative.T
        bridge_covariance = kappa * residual @ residual.T
        post_covariance = kappa * interpolation @ interpolation.T
        cross_covariance = kappa * residual @ interpolation.T

        bridge_error = max_abs(bridge_covariance - target_bridge_covariance)
        cross_error = max_abs(cross_covariance)
        reconstruction_error = max_abs(
            original_covariance - bridge_covariance - post_covariance
        )
        min_bridge = float(np.linalg.eigvalsh(bridge_covariance).min())
        min_post = float(np.linalg.eigvalsh(post_covariance).min())
        require(
            bridge_error < ALGEBRA_TOL
            and cross_error < ALGEBRA_TOL
            and reconstruction_error < ALGEBRA_TOL,
            f"Brownian covariance decomposition failed: N={n}, L={length}.",
        )
        require(
            min_bridge >= -ALGEBRA_TOL and min_post >= -ALGEBRA_TOL,
            f"Brownian decomposition has a negative covariance: N={n}, L={length}.",
        )
        composed = gaussian_schur(bridge_covariance, common_twirl=False) * (
            gaussian_schur(post_covariance, common_twirl=True)
        )
        channel_error = max_abs(composed - schur(n, kappa, "brownian"))
        require(
            channel_error < ALGEBRA_TOL,
            f"Brownian channel degradation failed: N={n}, L={length}.",
        )
        results.append(
            {
                "n": n,
                "L": length,
                "kappa": kappa,
                "complete_blocks": complete_blocks,
                "tail_slots": tail,
                "bridge_covariance_max_difference": bridge_error,
                "bridge_post_cross_covariance_max": cross_error,
                "covariance_reconstruction_max_difference": reconstruction_error,
                "minimum_bridge_covariance_eigenvalue": min_bridge,
                "minimum_post_covariance_eigenvalue": min_post,
                "channel_max_difference": channel_error,
            }
        )
    return results


def check_reset_enumeration() -> list[dict[str, Any]]:
    """Enumerate reset patterns, their exact twirls, and coherent environments."""
    results = []
    for n, p in ((1, 0.1), (2, 0.05), (4, 0.2), (5, 0.6)):
        strings = bits(n)
        input_dimension = 2**n
        enumerated_channel = np.zeros((input_dimension, input_dimension))
        environment_blocks = []
        conditional_entropy_average = 0.0
        pattern_probability_sum = 0.0
        for pattern in itertools.product((0, 1), repeat=n - 1):
            resets = sum(pattern)
            probability = p**resets * (1 - p) ** (n - 1 - resets)
            boundaries = [0]
            boundaries.extend(index for index in range(1, n) if pattern[index - 1])
            boundaries.append(n)
            lengths = np.diff(boundaries)
            weights = np.column_stack(
                [
                    strings[:, left:right].sum(axis=1)
                    for left, right in zip(boundaries[:-1], boundaries[1:])
                ]
            )
            conditional = np.all(
                weights[:, None, :] == weights[None, :, :], axis=2
            )
            enumerated_channel += probability * conditional

            labels = list(itertools.product(*(range(int(size) + 1) for size in lengths)))
            label_index = {label: index for index, label in enumerate(labels)}
            block = np.zeros((len(labels), input_dimension))
            for column, weight_vector in enumerate(weights):
                block[label_index[tuple(weight_vector)], column] = math.sqrt(probability)
            environment_blocks.append(block)
            conditional_entropy_average += probability * sum(
                binomial_entropy(int(size)) for size in lengths
            )
            pattern_probability_sum += probability

        require(
            abs(pattern_probability_sum - 1) < ALGEBRA_TOL,
            f"Reset pattern probabilities do not sum to one for n={n}.",
        )
        kappa = -2 * math.log1p(-p)
        channel_error = max_abs(enumerated_channel - schur(n, kappa, "reset"))
        require(
            channel_error < ALGEBRA_TOL,
            f"Reset enumeration/Schur disagreement for n={n}, p={p}.",
        )

        # Columns are the normalized environment vectors |e_x>. Distinct
        # reset-pattern blocks are coherent before pinching the flag.
        environment_vectors = np.vstack(environment_blocks)
        gram_error = max_abs(
            environment_vectors.T @ environment_vectors - enumerated_channel
        )
        require(
            gram_error < ALGEBRA_TOL,
            f"Coherent reset-environment Gram matrix failed for n={n}.",
        )
        environment_state = (
            environment_vectors @ environment_vectors.T / input_dimension
        )
        pinched_state = np.zeros_like(environment_state)
        offset = 0
        for block in environment_blocks:
            size = block.shape[0]
            pinched_state[offset : offset + size, offset : offset + size] = (
                block @ block.T / input_dimension
            )
            offset += size
        eigenvalues = np.linalg.eigvalsh(environment_state)
        actual_entropy = entropy(eigenvalues, f"Reset environment n={n}")
        pinched_entropy = entropy(
            np.linalg.eigvalsh(pinched_state), f"Pinched reset environment n={n}"
        )
        gram_entropy = entropy(
            np.linalg.eigvalsh(enumerated_channel / input_dimension),
            f"Reset normalized Gram matrix n={n}",
        )
        analytical_bound = (n - 1) * binary_entropy(p) + conditional_entropy_average
        pinch_error = abs(pinched_entropy - analytical_bound)
        require(
            abs(actual_entropy - gram_entropy) <= ENTROPY_TOL,
            f"Reset environment/Gram entropy disagreement for n={n}.",
        )
        require(
            pinch_error <= ENTROPY_TOL,
            f"Reset pinching entropy formula failed for n={n}.",
        )
        require(
            actual_entropy <= pinched_entropy + ENTROPY_TOL,
            f"Reset environment entropy upper bound failed for n={n}.",
        )
        results.append(
            {
                "n": n,
                "p": p,
                "reset_patterns": 2 ** (n - 1),
                "environment_dimension": environment_state.shape[0],
                "channel_max_difference": channel_error,
                "environment_gram_max_difference": gram_error,
                "minimum_environment_eigenvalue": float(eigenvalues.min()),
                "environment_entropy_bits": actual_entropy,
                "pinched_entropy_bits": pinched_entropy,
                "analytical_entropy_upper_bound_bits": analytical_bound,
                "pinched_entropy_formula_difference": pinch_error,
                "entropy_bound_slack_bits": pinched_entropy - actual_entropy,
            }
        )
    return results


def check_integral() -> dict[str, float]:
    def integrand_u(u: float) -> float:
        if u == 0:
            return 0.0  # Its value at this single integrable endpoint is immaterial.
        return bose_entropy(occupation_from_variance(u**-2))

    value, estimated_error = quad(
        integrand_u, 0, np.inf, epsabs=1e-8, limit=500
    )
    target = math.pi**2 / (4 * math.log(2))
    require(
        math.isfinite(value) and abs(value - target) < INTEGRAL_TOL,
        f"Asymptotic entropy integral failed: value={value}, target={target}.",
    )
    return {
        "value_bits": value,
        "target_bits": target,
        "estimated_error": estimated_error,
        "absolute_difference": abs(value - target),
        "coefficient_bound": value / math.pi,
    }


def run_checks() -> dict[str, Any]:
    results: dict[str, Any] = {
        "scope": (
            "Finite algebra, covariance, entropy, and discrimination diagnostics; "
            "analytic results remain in the scientific account."
        ),
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "tolerances": {
            "algebra": ALGEBRA_TOL,
            "entropy": ENTROPY_TOL,
            "integral": INTEGRAL_TOL,
        },
        "up_to_three_slots": check_selected_slots(),
        "four_slot_witness": check_four_slot_witness(),
        "four_slot_optimum": check_four_slot_optimum(),
        "group_phase_moments": check_group_moments(),
        "private_reference_overlap": check_private_reference_overlap(),
        "depth_schedule": check_depth_schedule(),
        "independent_block_twirling": check_block_factorization(),
        "entropy_bounds": check_gaussian_entropy_bounds(),
        "bridge_moments": check_bridge_moments(),
        "brownian_covariance_degradation": check_brownian_degradation(),
        "reset_pattern_enumeration": check_reset_enumeration(),
        "asymptotic_integral": check_integral(),
        "limitations": [
            "Finite selected cases do not prove the universal channel identities.",
            "Entropy upper bounds and conservative converse constants are not optimal capacities.",
            "Quadrature checks an analytically derived integral; it is not an asymptotic proof.",
            "No coding simulation, capacity fit, or uniform finite-length/small-noise claim is made.",
            "Finite discrimination checks do not optimize arbitrary inputs or fit the depth exponents.",
        ],
    }
    counts = {
        "selected_slot_kernels": len(results["up_to_three_slots"]),
        "block_factorizations": len(results["independent_block_twirling"]),
        "gaussian_entropy_bounds": len(results["entropy_bounds"]),
        "bridge_moments": len(results["bridge_moments"]),
        "four_slot_witnesses": 1,
        "four_slot_optima": len(results["four_slot_optimum"]),
        "group_phase_moments": len(results["group_phase_moments"]),
        "private_reference_overlaps": len(results["private_reference_overlap"]),
        "depth_schedules": len(results["depth_schedule"]),
        "asymptotic_integrals": 1,
        "brownian_covariance_degradations": len(results["brownian_covariance_degradation"]),
        "reset_pattern_enumerations": len(results["reset_pattern_enumeration"]),
    }
    counts["total"] = sum(counts.values())
    results["case_counts"] = counts
    results["status"] = "passed"
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON path for all checked cases; no file is written by default.",
    )
    args = parser.parse_args(argv)
    results = run_checks()
    if args.output is not None:
        args.output.write_text(
            json.dumps(results, indent=2, allow_nan=False) + "\n", encoding="utf-8"
        )
    summary = {
        key: results[key]
        for key in (
            "status",
            "versions",
            "case_counts",
            "four_slot_witness",
            "asymptotic_integral",
        )
    }
    summary["maximum_brownian_degradation_channel_error"] = max(
        case["channel_max_difference"]
        for case in results["brownian_covariance_degradation"]
    )
    summary["maximum_reset_enumeration_channel_error"] = max(
        case["channel_max_difference"]
        for case in results["reset_pattern_enumeration"]
    )
    summary["maximum_reset_pinching_formula_error"] = max(
        case["pinched_entropy_formula_difference"]
        for case in results["reset_pattern_enumeration"]
    )
    summary["maximum_four_slot_trace_norm_error"] = max(
        case["trace_norm_residual"] for case in results["four_slot_optimum"]
    )
    summary["maximum_group_phase_covariance_error"] = max(
        case["covariance_residual"] for case in results["group_phase_moments"]
    )
    print(json.dumps(summary, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
