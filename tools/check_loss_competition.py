#!/usr/bin/env python3
"""Supplementary diagnostics for research/LOSS_COMPETITION.md; not a proof.

Imports the preserved suite 02 continuum ODE, never its result file. The scalar
minimax search is independent of the stated optimizer. No high-dimensional
cascade is run for the large-N certificate checks. Output paths are exclusive.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import platform
import time
import mpmath as mp
import numpy as np
import scipy
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tests/02_common_mode_limit/checks.py'
spec = importlib.util.spec_from_file_location('preserved_common_mode', SOURCE)
legacy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(legacy)
mp.mp.dps = 70


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def exponent(A, lam):
    return lam if A == 0 else lam + max(0, A/4-lam)**2/A


def scalar_checks():
    rows = []
    for A in [0.02, 2/3, 16/3]:
        for delta in [0., .125, .25-1e-6, .25, .25+1e-6, .5, 2.]:
            lam = A*delta
            def objective(b):
                # Exact stationary points of x[delta+(x-b)^2], not a grid.
                candidates = [0., 1.]
                disc = b*b-3*delta
                if disc >= 0:
                    candidates += [x for x in [(2*b-np.sqrt(disc))/3,
                                                (2*b+np.sqrt(disc))/3] if 0 <= x <= 1]
                return max(x*(delta+(x-b)**2) for x in candidates)
            opt = minimize_scalar(objective, bounds=(0., 1.), method='bounded',
                                  options={'xatol': 1e-14, 'maxiter': 500})
            require(opt.success, 'Scalar optimizer failed')
            value, b = min([(opt.fun, opt.x), (objective(0.), 0.), (objective(1.), 1.)])
            expected_b = min(1., .75+delta)
            err = abs(A*value-exponent(A, lam))
            # Bounded minimization's sqrt(machine epsilon) position floor near
            # the kink sets this tolerance; stationary x values are not sampled.
            require(err <= 3e-8*A and abs(b-expected_b) <= 3e-7, 'Scalar minimax mismatch')
            rows.append(dict(A=A, lambda_=lam, delta=delta, numerical_b=float(b),
                             predicted_b=expected_b, numerical_exponent=float(A*value),
                             predicted_exponent=exponent(A, lam), absolute_error=err))
    for lam in [0., .7]:
        # For A=0 the objective is lambda*x and every b is a minimizer.
        require(exponent(0., lam) == max(0., lam), 'Zero-A endpoint')
        rows.append(dict(A=0., lambda_=lam, exponent=lam, optimizer='any b in [0,1]'))
    return rows


def kernel(z):
    return z/(2*mp.sinh(z/2)) if z else mp.mpf(1)


@lru_cache(None)
def entropy(N, m):
    if m <= 1:
        return mp.mpf(0)
    n = mp.mpf(N)
    a = mp.mpf(m-1)/n
    # The same proved relative-entropy identity as suite 02, evaluated at 70 dps.
    value = m*(-(1-a)/a*mp.log1p(-a)-1) - (
        mp.loggamma(n+1)-mp.loggamma(n-m+1)-m*mp.log(n))
    require(value >= 0, 'Negative relative entropy')
    return value


def certificates(N, M, lam, q, scan=False):
    n, m, lam = mp.mpf(N), mp.mpf(M), mp.mpf(lam)
    density_gap = 1-(m-1)/n
    A = m**3/(12*n*n*density_gap**2)
    B = m*(m-1)/(12*n*n*density_gap**2)
    epsilon = mp.sqrt(-2*mp.expm1(-B/2))
    b = min(mp.mpf(1), mp.mpf(3)/4+lam/A)
    a = (b*m-1)/n
    lower = max(mp.mpf(0), mp.exp(-exponent(A, lam)/2)-epsilon)**2
    ceiling = mp.exp(-lam)
    def u(k):
        return -mp.log1p(-mp.mpf(k-1)/n)
    def cosplus(theta):
        return mp.cos(theta) if theta < mp.pi/2 else mp.mpf(0)
    def beta(k):
        return mp.acos(mp.exp(-entropy(N, k)/2))
    def radius(F, k):
        # This algebraic form is exactly one at F=ceiling, k=M, avoiding
        # exp(-lambda)*exp(lambda)>1 from roundoff without clipping a cosine.
        relative_fidelity = (F/ceiling)*mp.exp(-lam*(m-k)/m)
        require(0 <= relative_fidelity <= 1, 'Invalid fidelity in angle radius')
        angle = mp.acos(mp.sqrt(relative_fidelity))+beta(k)
        return mp.acos(cosplus(angle)**(mp.mpf(1)/k))
    separation = mp.acos(kernel(u(M)-u(q)))
    def residual(F):
        return radius(F, q)+radius(F, M)-separation
    if residual(ceiling) >= 0:
        upper = ceiling
    else:
        lo, hi = mp.mpf(0), ceiling
        for _ in range(100):
            mid = (lo+hi)/2
            if residual(mid) >= 0:
                lo = mid
            else:
                hi = mid
        upper = hi
    require(0 <= lower <= upper <= ceiling <= 1, 'Invalid finite certificate order')
    result = dict(closed_lower=float(lower), angle_upper=float(upper),
                  loss_ceiling=float(ceiling), mode_a=float(a), pair_q=q)
    if scan:
        pulse_u = -mp.log1p(-a)
        result['sector_angle_lower'] = float(min(
            mp.exp(-lam*k/m)*cosplus(mp.acos(kernel(u(k)-pulse_u)**k)+beta(k))**2
            for k in range(1, M+1)))
    return result


def finite_checks():
    rows = []
    for N, M in [(12, 4), (30, 8), (60, 12)]:
        for delta in [0., .125, .5]:
            lam = delta*M**3/(12*N*N)
            q = max(1, int((.25+delta)*M)) if delta < .25 else M//2
            cert = certificates(N, M, lam, q, scan=True)
            raw = [legacy.full_overlap(N, k, cert['mode_a'], T=48., rtol=1e-10)
                   for k in range(1, M+1)]
            weights = np.exp(-lam*np.arange(1, M+1)/M)
            fidelities = [float(w*r['fidelity']) for w, r in zip(weights, raw)]
            trial = min(fidelities)
            tail = max(float(w*r['omitted_fidelity_bound']) for w, r in zip(weights, raw))
            # Numerical consistency allowance, not a rigorous ODE enclosure.
            require(max(cert['closed_lower'], cert['sector_angle_lower']) <= trial+tail+2e-9,
                    'Constructive lower bound exceeds the trial')
            require(trial <= cert['angle_upper']+2e-9, 'Trial exceeds universal upper bound')
            row = dict(N=N, M=M, delta=delta, lambda_=lam, **cert,
                       trial_fidelity=trial, sector_fidelities=fidelities,
                       analytic_fidelity_tail_allowance=tail, ode_T=48., ode_rtol=1e-10,
                       ode_atol=2e-15)
            if (N, M, delta) == (60, 12, 0.):
                refined = [legacy.full_overlap(N, k, cert['mode_a'], T=60., rtol=2e-12)
                           for k in range(1, M+1)]
                error = max(abs(r['fidelity']-s['fidelity']) for r, s in zip(raw, refined))
                require(error <= 2e-9, 'Stricter integration changed the result')
                row['refinement'] = dict(T=60., rtol=2e-12, atol=2e-15,
                                         maximum_sector_fidelity_change=error,
                                         maximum_tail_allowance=max(
                                             r['omitted_fidelity_bound'] for r in refined))
            rows.append(row)
    return rows


def convergence_checks():
    rows = []
    for c in [2, 4]:
        for delta in [0., .125, .5]:
            lam = mp.mpf(delta)*c**3/12
            target = float(mp.exp(-exponent(mp.mpf(c**3)/12, lam)))
            series = []
            for N, base in [(10**3, 100), (10**6, 10000), (10**9, 1000000)]:
                M = c*base
                q = int((.25+delta)*M) if delta < .25 else M//2
                cert = certificates(N, M, lam, q)
                row = dict(N=N, M=M, c=c, delta=delta, lambda_=float(lam),
                           limiting_fidelity=target, **cert)
                rows.append(row)
                series.append(row)
            first, last = series[0], series[-1]
            # Fixed tests at these declared scales: a one-percentage-point
            # absolute endpoint criterion and a fivefold width contraction.
            require(max(abs(last[k]-target) for k in ['closed_lower', 'angle_upper']) < .01,
                    'Finite certificates have not approached the critical law')
            require(last['angle_upper']-last['closed_lower'] <
                    (first['angle_upper']-first['closed_lower'])/5, 'Insufficient bracket contraction')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error('Refusing to replace an existing output file.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.perf_counter()
    groups = dict(scalar_minimax=scalar_checks(), finite_cascade=finite_checks(),
                  scalar_certificate_convergence=convergence_checks())
    report = dict(status='PASS', supplementary_cases=sum(map(len, groups.values())),
                  started_at=started, finished_at=datetime.now(timezone.utc).isoformat(),
                  runtime_seconds=time.perf_counter()-clock,
                  versions=dict(python=platform.python_version(), numpy=np.__version__,
                                scipy=scipy.__version__, mpmath=mp.__version__),
                  method=dict(precision_digits=mp.mp.dps, imported_ode=str(SOURCE.relative_to(ROOT)),
                              minimax='Exact cubic stationary points; bounded scalar minimization plus endpoints',
                              angle_upper='70-digit scalar bisection, 100 iterations'),
                  limitations=['Supplementary cases are separate from the eight preserved scientific suites.',
                               'Finite checks and numerical brackets are not proofs or interval enclosures.',
                               'The continuum ODE and entropy identity are inherited, not independent derivations.',
                               'No high-dimensional large-N simulation or exact finite-size optimization.'],
                  groups=groups)
    payload = json.dumps(report, indent=2, allow_nan=False)+'\n'
    if args.output:
        with args.output.open('x') as handle:
            handle.write(payload)
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
