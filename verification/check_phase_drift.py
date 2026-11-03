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
            "Finite algebra, covariance, and entropy diagnostics; "
            "no numerical inference of asymptotic capacity."
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
        ],
    }
    counts = {
        "selected_slot_kernels": len(results["up_to_three_slots"]),
        "block_factorizations": len(results["independent_block_twirling"]),
        "gaussian_entropy_bounds": len(results["entropy_bounds"]),
        "bridge_moments": len(results["bridge_moments"]),
        "four_slot_witnesses": 1,
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
    print(json.dumps(summary, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
