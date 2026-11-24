"""Finite checks of the capped single-oscillator receiver and product-pulse limit."""

import math

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


SWITCH_SCALE = math.log(4)
ONSET_COEFFICIENT = SWITCH_SCALE - 1


def check_exponential_pulse():
    for cap, expected in ((1.0, 2 / math.e), (2.0, 27 / 32), (100.0, None)):
        switch = (
            1.0 if cap == 1 else 2 * math.log(2 * cap / (cap + 1)) / (cap - 1)
        )
        amplitude_at_switch = quad(
            lambda t: math.sqrt(cap) * math.exp(-t / 2 - cap * (switch - t) / 2),
            0,
            switch,
        )[0]
        assert math.isclose(amplitude_at_switch, math.exp(-switch / 2) / math.sqrt(cap))
        fidelity = amplitude_at_switch**2 + math.exp(-switch)
        if expected is None:
            assert abs(cap * (1 - fidelity) - ONSET_COEFFICIENT) < 2 / cap
        else:
            assert math.isclose(fidelity, expected, rel_tol=1e-12)
        print(f"Exponential pulse, K={cap:g}: capture probability {fidelity:.9f}")


def integrated_onset_cost(z):
    end = min(SWITCH_SCALE, -math.log(z)) if 0 < z < 1 else SWITCH_SCALE
    integral = quad(
        lambda s: max(0, 1 - math.sqrt(z) * math.exp(s / 2)) ** 2,
        0,
        end,
    )[0]
    return z + integral


def onset_cost(z):
    if z <= 1 / 4:
        return SWITCH_SCALE - 4 * math.sqrt(z) + 4 * z
    if z <= 1:
        return -math.log(z) - 3 + 4 * math.sqrt(z)
    return z


def check_onset_cost():
    for z in (0, 0.01, 0.1, 0.249, 0.25, 0.251, 0.5, 0.999, 1, 1.1, 2):
        assert math.isclose(integrated_onset_cost(z), onset_cost(z), abs_tol=1e-13)
    minimum = minimize_scalar(integrated_onset_cost, bounds=(0, 2), method="bounded")
    assert minimum.success
    assert abs(minimum.x - 0.25) < 2e-5
    assert abs(minimum.fun - ONSET_COEFFICIENT) < 1e-9
    print(f"Onset cost: minimum {minimum.fun:.9f} at z={minimum.x:.7f}")


def pulse(parameter, t):
    y = math.exp(-t)
    return math.sqrt((1 - parameter) * y) / (1 - parameter + parameter * y)


def tail_mass(parameter, t):
    y = math.exp(-t)
    return y / (1 - parameter + parameter * y)


def pulse_overlap(left, right):
    shift = math.log1p(-left) - math.log1p(-right)
    return shift / (2 * math.sinh(shift / 2)) if shift else 1.0


def pulse_tail_overlap(left, right, stop):
    # Change variables to y = exp(-t), so the tiny tail has a smooth integrand.
    return quad(
        lambda y: math.sqrt((1 - left) * (1 - right))
        / ((1 - left + left * y) * (1 - right + right * y)),
        0,
        math.exp(-stop),
    )[0]


def check_product_receiver(emitters, ceiling, cap, center, stop):
    """Check the physical rate and sample the constructed product fidelity."""
    parameter = (center * ceiling - 1) / emitters
    switch = SWITCH_SCALE / cap
    scale = 1 / math.sqrt(tail_mass(parameter, switch) + pulse(parameter, switch)**2 / cap)
    switch_amplitude = scale * pulse(parameter, switch)
    switch_mass = switch_amplitude**2 / cap
    vacuum_at_stop = 1 - scale**2 * tail_mass(parameter, stop)
    assert 0 < switch < stop and 0 < vacuum_at_stop <= 1

    def kernel(t):
        if t < switch:
            return switch_amplitude * math.exp(cap * (t - switch) / 2)
        return scale * pulse(parameter, t)

    def vacuum(t):
        if t < switch:
            return switch_mass * math.exp(cap * (t - switch))
        # Integrating the squared late pulse as a CDF increment avoids a
        # subtraction of nearly equal numbers close to the switch.
        start_y, y = math.exp(-switch), math.exp(-t)
        denominator = (1 - parameter + parameter * start_y) * (1 - parameter + parameter * y)
        increment = (1 - parameter) * (start_y - y) / denominator
        return switch_mass + scale**2 * increment

    for t in np.concatenate((np.linspace(0, switch, 11), np.linspace(switch, stop, 61))):
        assert 0 < vacuum(t) <= 1 + 1e-12
        assert kernel(t)**2 <= cap * vacuum(t) * (1 + 1e-12)
    assert math.isclose(vacuum(stop), vacuum_at_stop, rel_tol=1e-12)

    # The same rate profile stopped early implements h / sqrt(q(stop)).
    masses = [quad(lambda t: kernel(t)**2, a, b)[0] for a, b in ((0, switch), (switch, stop))]
    assert math.isclose(sum(masses) + vacuum(0), vacuum_at_stop, rel_tol=1e-11)

    fractions = np.linspace(1, ceiling, 121)
    sectors = np.unique(np.rint(fractions).astype(int))
    fidelity = 1.0
    for number in sectors:
        source = (number - 1) / emitters
        early = quad(lambda t: kernel(t) * pulse(source, t), 0, switch)[0]
        omitted = quad(lambda t: pulse(parameter, t) * pulse(source, t), 0, switch)[0]
        late = pulse_overlap(parameter, source) - omitted - pulse_tail_overlap(parameter, source, stop)
        amplitude = (early + scale * late) / math.sqrt(vacuum_at_stop)
        assert 0 < amplitude <= 1 + 1e-12
        fidelity = min(fidelity, math.exp(2 * number * math.log(amplitude)))
    return fidelity


def check_product_convergence():
    critical_ratio = 2
    bulk_coefficient = critical_ratio**3 / 12
    for cap_ratio, shift in ((0.5, None), (3, None), (20, None), (20, 0.0), (20, 2.0)):
        tail_coefficient = 0 if shift is None else math.exp(-shift)
        loss_coefficient = ONSET_COEFFICIENT / cap_ratio + tail_coefficient
        center = min(1, 3 / 4 + loss_coefficient / bulk_coefficient)
        exponent = loss_coefficient + max(bulk_coefficient / 4 - loss_coefficient, 0)**2 / bulk_coefficient
        expected = math.exp(-exponent)
        errors = []
        for emitters in (10**3, 10**6, 10**9):
            ceiling = round(critical_ratio * emitters**(2 / 3))
            stop = 2 * math.log(ceiling + 1) if shift is None else math.log(ceiling) + shift
            fidelity = check_product_receiver(emitters, ceiling, cap_ratio * ceiling, center, stop)
            errors.append(abs(fidelity - expected))
        assert errors[2] < errors[1] < errors[0]
        assert errors[-1] < 0.0015
        window = "long" if shift is None else f"log(M) + {shift:g}"
        print(f"K/M={cap_ratio:g}, window {window}: sampled {fidelity:.9f}, limit {expected:.9f}")


if __name__ == "__main__":
    check_exponential_pulse()
    check_onset_cost()
    check_product_convergence()
