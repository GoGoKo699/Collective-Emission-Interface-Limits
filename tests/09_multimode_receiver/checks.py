#!/usr/bin/env python3
"""Independent finite checks for the fixed-K multimode receiver.

Run with Python 3, NumPy and SciPy. The asymptotic converse is analytic.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from math import comb, sqrt
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad, solve_ivp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_polynomials():
    expected = {1: Fraction(1, 192), 2: Fraction(1, 46080), 3: Fraction(1, 11468800)}
    maximum_alternation_error = 0.0
    rows = []
    for count in range(1, 9):
        degree = 2 * count + 1
        previous, current = [1], [0, 1]
        for order in range(2, degree + 1):
            following = [0] + [2 * coefficient for coefficient in current]
            for power, coefficient in enumerate(previous):
                following[power] -= coefficient
            previous, current = current, following
        polynomial = [Fraction(current[power], 4**count) for power in range(1, degree + 1, 2)]
        require(all(coefficient == 0 for coefficient in current[::2]), "Chebyshev parity")
        require(polynomial[-1] == 1, "Monic weighted minimax polynomial")

        y = np.cos(np.arange(count + 1) * np.pi / degree)
        alternation = y * np.polynomial.polynomial.polyval(y**2, polynomial).astype(float)
        relative_error = float(np.max(abs(alternation * 4**count - (-1.0) ** np.arange(count + 1))))
        maximum_alternation_error = max(maximum_alternation_error, relative_error)
        require(relative_error < 2e-6, "Weighted alternating extrema")

        leading_coefficient = comb(2 * count, count)
        legendre = [
            Fraction((-1) ** (count - power) * comb(count, power) * comb(count + power, power),
                     leading_coefficient)
            for power in range(count + 1)
        ]
        for power in range(count):
            inner_product = sum(coefficient / (power + index + 1)
                                for index, coefficient in enumerate(legendre))
            require(inner_product == 0, "Shifted Legendre orthogonality")
        norm_squared = sum(left * right / (i + j + 1)
                           for i, left in enumerate(legendre)
                           for j, right in enumerate(legendre))
        require(norm_squared == Fraction(1, degree * leading_coefficient**2),
                "Exact monic Legendre norm")
        constant = norm_squared / 16**count
        if count in expected:
            require(constant == expected[count], "Known low-order critical constant")
        rows.append({"modes": count, "minimax_polynomial": list(map(str, polynomial)),
                     "critical_constant": str(constant)})
    return {"exact_checks": rows, "maximum_relative_alternation_error": maximum_alternation_error}


def snapshot_nodes(count):
    return np.cos((2 * np.arange(count) + 1) * np.pi / (4 * count + 2))**2


def snapshot_basis(z, roots, h):
    """A divided-difference basis spanning the same modes as the snapshots."""
    factors = 1 - h * z[:, None] * roots
    return z[:, None] ** np.arange(len(roots)) / np.cumprod(factors, axis=1)


def projection_residual(z, weights, roots, h, fractions):
    count = len(roots)
    square_root_weights = np.sqrt(weights)
    basis = snapshot_basis(z, roots, h)
    orthonormal, _ = np.linalg.qr(square_root_weights[:, None] * basis)
    denominator = 1 - h * z[:, None] * fractions
    pulse = square_root_weights[:, None] * np.sqrt(1 - h * fractions) / denominator
    pulse_norm_error = np.max(abs(np.sum(pulse**2, axis=0) - 1))
    require(pulse_norm_error < 3e-14, "Normalized matched pulse")

    # Subtract the exact Lagrange interpolant, which lies in the capture subspace.
    # This avoids resolving the small h**count residual by cancellation.
    scaled_difference = pulse * z[:, None] ** count / np.prod(1 - h * z[:, None] * roots, axis=1)[:, None]
    scaled_difference *= np.prod(fractions[:, None] - roots, axis=1)
    scaled_residual = scaled_difference - orthonormal @ (orthonormal.T @ scaled_difference)
    direct_residual = pulse - orthonormal @ (orthonormal.T @ pulse)
    agreement = float(np.max(abs(direct_residual - h**count * scaled_residual)))
    require(agreement < 2e-14, "Direct projection agrees with interpolation residual")
    return np.sum(scaled_residual**2, axis=0), agreement


def check_snapshot_geometry():
    fractions = np.linspace(0, 1, 1201)
    widths = [0.2, 0.1, 0.05, 0.025, 0.0125]
    rules = []
    for order in (48, 96):
        z, weights = leggauss(order)
        rules.append(((z + 1) / 2, weights / 2))

    rows = []
    for count in (1, 2, 3):
        roots = snapshot_nodes(count)
        constant = 1 / (16**count * (2 * count + 1) * comb(2 * count, count)**2)
        ratios = []
        max_rule_gap = 0.0
        max_projection_gap = 0.0
        for h in widths:
            residuals = []
            for z, weights in rules:
                squared_residual, projection_gap = projection_residual(z, weights, roots, h, fractions)
                residuals.append(squared_residual)
                max_projection_gap = max(max_projection_gap, projection_gap)
            rule_gap = float(np.max(abs(residuals[0] - residuals[1])) / constant)
            max_rule_gap = max(max_rule_gap, rule_gap)
            ratios.append(float(np.max(fractions * residuals[1]) / constant))
        errors = np.abs(np.asarray(ratios) - 1)
        require(np.all(errors[1:] < errors[:-1]), "Finite-width ratios converge toward one")
        require(errors[-1] < 0.075, "Finest-grid ratio is close to the critical constant")
        require(max_rule_gap < 2e-11, "48/96-point quadrature agreement")
        rows.append({"modes": count, "widths": widths, "ratios_to_critical_constant": ratios,
                     "maximum_quadrature_gap_over_constant": max_rule_gap,
                     "maximum_direct_projection_error": max_projection_gap})
    return rows


def two_mode_basis(z, weights, h):
    roots = snapshot_nodes(2)
    basis = snapshot_basis(z, roots, h)
    combination = basis.T @ weights
    primary = basis @ np.linalg.solve(basis.T @ (weights[:, None] * basis), combination)
    primary /= np.sqrt(np.dot(weights, primary**2))
    secondary = basis[:, 1] - np.dot(weights, primary * basis[:, 1]) * primary
    secondary /= np.sqrt(np.dot(weights, secondary**2))
    return np.column_stack((primary, secondary))


def check_quadratic_decoder():
    nodes, weights = leggauss(64)
    z, weights = (nodes + 1) / 2, weights / 2
    ratios = []
    for h in (0.2, 0.1, 0.05, 0.025):
        basis = two_mode_basis(z, weights, h)
        coefficients = basis.T @ (weights[:, None] * np.column_stack((np.ones_like(z), z - 0.5,
                                                                     z**2 - z / 2 - 1 / 8)))
        first, second = coefficients
        require(abs(second[0]) < 1e-13, "Second mode is orthogonal to the zero-parameter pulse")
        linear = second[1] / first[0]
        quadratic = second[2] / first[0] - second[1] * first[1] / first[0]**2
        parameters = np.linspace(0, h, 257)
        pulses = np.sqrt(1 - parameters) / (1 - z[:, None] * parameters)
        amplitudes = basis.T @ (weights[:, None] * pulses)
        angles = np.arctan2(amplitudes[1], amplitudes[0])
        errors = abs(angles - linear * parameters - quadratic * parameters**2)
        ratios.append(float(np.max(errors) / h**3))

        # Carry an actual m-photon state through one target-number block.
        angle_error = float(errors[-1])
        photons = 16
        state_error = sqrt(-2 * np.expm1(photons * np.log1p(-2 * np.sin(angle_error / 2)**2)))
        require(state_error <= sqrt(photons) * angle_error * (1 + 1e-10),
                "Product Fock state error is bounded by sqrt(m) times the rotation error")
    require(max(ratios) < 1, "Uniform cubic rotation-angle error on the checked widths")
    return {"maximum_angle_error_over_width_cubed": ratios}


def check_exact_two_photon_projection():
    """Compare the exact Dicke two-photon field with a separate cascade ODE."""
    emitters, h = 16, 0.3
    nodes, weights = leggauss(96)
    roots = snapshot_nodes(2)
    z, weights = (nodes + 1) / 2, weights / 2
    basis = snapshot_basis(z, roots, h)
    _, triangular = np.linalg.qr(np.sqrt(weights)[:, None] * basis)
    basis_transform = np.linalg.inv(triangular)

    def modes(z_values):
        values = np.atleast_1d(z_values)
        return snapshot_basis(values, roots, h) @ basis_transform

    def ordered_integral(left, right):
        # Reorder the two photon labels over the triangle z_low <= z_high.
        def outer(z_low):
            low_modes = modes(z_low)[0]

            def inner(z_high):
                high_modes = modes(z_high)[0]
                return low_modes[left] * high_modes[right] + low_modes[right] * high_modes[left]

            return (1 - z_low)**(-1 / emitters) * quad(inner, z_low, 1, epsabs=2e-13)[0]

        factor = sqrt(1 - 1 / emitters) * (1 if left == right else sqrt(2))
        return factor * quad(outer, 0, 1, epsabs=2e-13)[0]

    direct = np.array([ordered_integral(0, 0), ordered_integral(0, 1), ordered_integral(1, 1)])
    rate_two = 2 * (1 - 1 / emitters)

    def cascade_rhs(t, amplitudes):
        remaining_two, single_first, single_second, _, _, _ = amplitudes
        envelope = np.exp(-t / 2)
        first, second = envelope * modes(-np.expm1(-t))[0]
        first_feed = sqrt(rate_two) * remaining_two
        return np.array([
            -rate_two * remaining_two / 2,
            first * first_feed - single_first / 2,
            second * first_feed - single_second / 2,
            sqrt(2) * first * single_first,
            second * single_first + first * single_second,
            sqrt(2) * second * single_second,
        ])

    initial = [1, 0, 0, 0, 0, 0]
    solved = solve_ivp(cascade_rhs, (0, 42), initial, method="DOP853", rtol=1e-11, atol=2e-14)
    require(solved.success, solved.message)
    maximum_error = float(np.max(abs(solved.y[3:, -1] - direct)))
    require(maximum_error < 1e-10, "Independent exact projected two-photon amplitudes")
    probability = float(np.dot(direct, direct))
    require(0 < probability <= 1 + 1e-12, "Full-capture probability")
    return {"emitters": emitters, "photons": 2, "capture_probability": probability,
            "maximum_amplitude_error": maximum_error}


def check_sector_decoder():
    """Check the decoder on complex finite Fock sectors, including a reference."""
    rng = np.random.default_rng(2026112311)
    dimension = 6
    kraus = defaultdict(lambda: np.zeros((dimension, dimension), dtype=complex))
    capture_probabilities = []
    decoders = []
    for photons in range(dimension):
        emitted = rng.normal(size=(photons + 1, photons + 1)) + 1j * rng.normal(size=(photons + 1, photons + 1))
        # Index by lost photons and photons in the second captured mode.
        for lost in range(photons + 1):
            emitted[lost, photons - lost + 1:] = 0
        emitted /= np.linalg.norm(emitted)
        full_capture = emitted[0]
        capture_norm = np.linalg.norm(full_capture)
        spanning = np.column_stack((full_capture / capture_norm, np.eye(photons + 1)[:, 1:]))
        unitary, _ = np.linalg.qr(spanning)
        unitary[:, 0] = full_capture / capture_norm
        decoder = unitary.conj().T
        decoded_capture = decoder @ full_capture
        require(np.max(abs(decoded_capture - capture_norm * np.eye(photons + 1)[:, 0])) < 1e-12,
                "Coherent positive compression in each retained-number block")
        capture_probabilities.append(float(capture_norm**2))
        decoders.append(decoder)
        for lost in range(photons + 1):
            retained = photons - lost
            # Apply the decoder keyed by retained number, including to lower sectors.
            for garbage, amplitude in enumerate(decoders[retained] @ emitted[lost, :retained + 1]):
                kraus[lost, garbage][retained - garbage, photons] = amplitude

    completeness = sum(operator.conj().T @ operator for operator in kraus.values())
    require(np.max(abs(completeness - np.eye(dimension))) < 1e-12, "Decoded channel remains trace preserving")
    no_loss = np.diag(np.sqrt(capture_probabilities))
    require(np.max(abs(kraus[0, 0] - no_loss)) < 1e-12, "Common vacuum-environment Kraus operator")
    worst = min(capture_probabilities)
    number_input = np.eye(dimension)[:, int(np.argmin(capture_probabilities))]
    number_fidelity = sum(abs(np.vdot(number_input, operator @ number_input))**2 for operator in kraus.values())
    require(abs(number_fidelity - worst) < 1e-12, "Worst number state realizes the minimum")
    reference = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    reference /= np.linalg.norm(reference)
    fidelity = sum(abs(np.vdot(reference, operator @ reference))**2 for operator in kraus.values())
    require(fidelity >= worst - 1e-12, "Untouched-reference fidelity obeys the sector minimum")
    phase_flip = np.diag([1, -1])
    equal_superposition = np.ones(2) / sqrt(2)
    require(abs(np.vdot(equal_superposition, phase_flip @ equal_superposition)) < 1e-12,
            "Uncorrected relative phase can erase fidelity on a superposition")
    return {"number_sectors": dimension, "worst_number_fidelity": float(number_fidelity),
            "reference_fidelity": float(fidelity)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON results to this path.")
    args = parser.parse_args()
    report = {
        "polynomials": check_polynomials(),
        "snapshot_geometry": check_snapshot_geometry(),
        "quadratic_decoder": check_quadratic_decoder(),
        "exact_two_photon_projection": check_exact_two_photon_projection(),
        "sector_decoder": check_sector_decoder(),
    }
    formatted = json.dumps(report, indent=2)
    if args.output is not None:
        args.output.write_text(formatted + "\n", encoding="utf-8")
    print(formatted)


if __name__ == "__main__":
    main()
