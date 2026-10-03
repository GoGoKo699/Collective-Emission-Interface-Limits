#!/usr/bin/env python3
"""Independent finite diagnostics of the endpoint-safe common-mode proof.

No earlier scientific module or result file is imported. Finite checks are not
proofs of the universal statements; those are derived in research/PROOF_AUDIT.md.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import json
from math import comb, factorial
from pathlib import Path
import platform
import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

mp.mp.dps = 70
SEED = 2026100308


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def close(x, y, message, tolerance=2e-11):
    error = float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    require(np.isfinite(error) and error <= tolerance, f'{message}: {error}')
    return error


def kernel(z):
    z = mp.mpf(z)
    return z/(2*mp.sinh(z/2)) if z else mp.mpf(1)


def envelope(N, M, q=None):
    if not (1 <= N and 0 <= M <= N):
        raise ValueError('Require 1<=N and 0<=M<=N.')
    if M <= 1:
        return mp.mpf(1), mp.mpf(1), mp.mpf(0), mp.mpf(0)
    n, m = mp.mpf(N), mp.mpf(M)
    b = 1-(m-1)/n
    B = m*(m-1)/(12*n*n*b*b)
    eps = mp.sqrt(-2*mp.expm1(-B/2))
    lower = max(mp.mpf(0), mp.exp(-m**3/(384*n*n*b*b))-eps)**2
    if q is None:
        q = max(1, M//4)
    if not 1 <= q < M:
        raise ValueError('Require 1<=q<M for a two-sector converse.')
    z = mp.log((1-mp.mpf(q-1)/n)/(1-(m-1)/n))
    theta = mp.acos(kernel(z))
    S = 1/mp.sqrt(q)+1/mp.sqrt(M)
    X = (theta/S)**2
    upper = min(mp.mpf(1), (eps+mp.exp(-X/2))**2)
    return lower, upper, eps, X


def cascade(N, m, a, T=45.):
    if m == 0:
        return 1.
    remaining = np.arange(m,-1,-1)
    rates = remaining*(1-(remaining-1)/N)
    coefficients = np.sqrt(remaining[:-1]*rates[:-1])
    def rhs(t, y):
        f = np.sqrt(1-a)*np.exp(-t/2)/(1-a+a*np.exp(-t))
        dy = -.5*rates*y
        dy[1:] += coefficients*f*y[:-1]
        return dy
    initial = np.zeros(m+1); initial[0] = 1.
    sol = solve_ivp(rhs,(0.,T),initial,method='DOP853',rtol=1e-11,atol=2e-15,max_step=.2)
    require(sol.success, sol.message)
    return float(sol.y[-1,-1]**2)


def test_normalization_and_entropy_identity():
    normalization = 0
    for m in range(1,10):
        for N in sorted(set([m,2*m,10*m])):
            prefactor = Q(factorial(m))
            product_rate = Q(1)
            for k in range(1,m+1):
                b = Q(N-k+1,N)
                prefactor *= b
                product_rate *= k*b
            require(prefactor/product_rate == 1, 'Ordered-time norm')
            normalization += 1
    moments = 0
    for m in range(2,10):
        for S in [Q(1,7),Q(1,2),Q(6,7)]:
            lhs = sum(Q(comb(m,k))*S**k*(1-S)**(m-k)*k*(k-1-(m-1)*S)**2 for k in range(m+1))
            require(lhs == m*(m-1)*S*S*(1-S), 'Size-biased binomial identity')
            moments += 1
    return dict(cases=normalization+moments,exact_ordered_normalizations=normalization,
                exact_size_biased_moments=moments,scope='Rational finite identities; full derivation is in the note.')


def test_channel_and_reference():
    rng = np.random.default_rng(SEED)
    cases = []
    for d in [2,3,5,7]:
        matrices = [np.zeros((d,d),complex) for _ in range(d)]
        for m in range(d):
            amplitudes = rng.uniform(.1,1.,m+1)
            amplitudes /= np.linalg.norm(amplitudes)
            for lost,amp in enumerate(amplitudes):
                matrices[lost][m-lost,m] = amp
        close(sum(K.conj().T@K for K in matrices),np.eye(d),'Kraus completeness')
        minimum = float(np.min(np.abs(np.diag(matrices[0]))**2))
        C = rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        C /= np.linalg.norm(C)
        rho = C@C.conj().T
        trace_formula = sum(abs(np.trace(rho@K))**2 for K in matrices)
        reference_formula = sum(abs(np.vdot(C,K@C))**2 for K in matrices)
        close(trace_formula,reference_formula,'Untouched-reference formula')
        require(trace_formula >= minimum-1e-13, 'Positive no-loss branch lower bound')
        mstar = int(np.argmin(abs(np.diag(matrices[0]))))
        v = np.eye(d)[:,mstar]
        close(sum(abs(v@K@v)**2 for K in matrices),minimum,'Worst number state attains minimum')
        cases.append(dict(dimension=d,minimum=minimum,reference_input_fidelity=float(reference_formula)))
    # A complex phase channel shows why the positive-waveform reduction is needed.
    phase = np.diag([1.,-1.]); v = np.ones(2)/np.sqrt(2)
    close(abs(v@phase@v)**2,0.,'Fock fidelities alone do not bound an arbitrary phase channel')
    return dict(cases=len(cases)+1,channels=cases,phase_control=dict(number_fidelities=[1,1],superposition_fidelity=0),
                scope='No environment measurement or postselection; random channels test the structural lemma, not a new physical source.')


def test_endpoint_safe_geometry():
    rng = np.random.default_rng(SEED+1)
    rows = []
    for q,M in [(1,4),(3,12),(25,100)]:
        for theta in [.01,.2,.8]:
            S = q**-.5+M**-.5
            upper = np.exp(-(theta/S)**2)
            root = brentq(lambda x:q*np.log(np.cos(x))-M*np.log(np.cos(theta-x)),0.,theta)
            exact_product = np.cos(root)**(2*q)
            require(exact_product <= upper+2e-13, 'Finite projective bound')
            u = np.array([1.,0.,0.]); w = np.array([np.cos(theta),np.sin(theta),0.])
            for _ in range(12):
                f = rng.normal(size=3)+1j*rng.normal(size=3); f /= np.linalg.norm(f)
                actual = min(abs(np.vdot(f,u))**(2*q),abs(np.vdot(f,w))**(2*M))
                require(actual <= upper+1e-13, 'Complex off-span receiving mode')
            rows.append(dict(q=q,M=M,theta=theta,product_optimum=float(exact_product),upper=float(upper)))
    controls=[]
    for N in [10**3,10**6,10**9]:
        eps=mp.mpf(N)**(-mp.mpf(1)/3); F=1-mp.mpf(N)**(-2)
        ratio=-2*mp.log(mp.sqrt(F)-eps)/(-mp.log(F))
        controls.append(dict(N=N,source_error=float(eps),trial_fidelity=float(F),log_error_ratio=float(ratio)))
    require(controls[-1]['log_error_ratio']>controls[0]['log_error_ratio']*1e8,'Nonuniform near-unit-fidelity substitution')
    return dict(cases=len(rows)+len(controls),geometry=rows,endpoint_negative_control=controls,
                scope='The endpoint sequence is a counterexample to a relative-error substitution, not an attainable Dicke receiver.')


def test_finite_envelopes_and_limits():
    rows=[]
    for N,M in [(12,4),(30,8),(60,12)]:
        low,high,eps,X=envelope(N,M)
        a=(.75*M-1)/N
        fidelities=[cascade(N,m,a) for m in range(M+1)]
        actual=min(fidelities)
        require(float(low)<=actual+2e-10 and actual<=float(high)+2e-10,'Full-cascade finite envelope')
        rows.append(dict(N=N,M=M,lower=float(low),trial_worst=actual,upper=float(high)))
    critical=[]
    for c in [1,2,3]:
        target=np.exp(-c**3/192)
        previous=None
        for N,scale in [(1000,100),(10**6,10000),(10**9,10**6),(10**12,10**8)]:
            M=c*scale;lo,hi,eps,X=envelope(N,M)
            width=float(hi-lo)
            require(lo<=hi,'Finite envelope ordering')
            if previous is not None:require(width<previous,'Critical envelope convergence')
            previous=width
            critical.append(dict(N=N,M=M,c=c,lower=float(lo),upper=float(hi),epsilon=float(eps),target=float(target)))
        require(abs(float(lo)-target)<.0003 and abs(float(hi)-target)<.0003,'Matching critical limits')
    supercritical=[]
    for N in [10**8,10**12,10**16]:
        M=int(mp.mpf(N)**mp.mpf('.75'));lo,hi,eps,X=envelope(N,M)
        supercritical.append(dict(N=N,M=M,two_sector_upper=float(hi),source_error=float(eps)))
    require(supercritical[-1]['two_sector_upper']<.001,'Two-sector supercritical control')
    return dict(cases=len(rows)+len(critical)+len(supercritical),finite=rows,critical=critical,
                supercritical=supercritical,scope='Huge N entries evaluate scalar inequalities only, not physical simulations.')


def test_isometry_and_collection():
    rng=np.random.default_rng(SEED+2)
    errors=[.01,.04,.02,.03]
    V=np.zeros((8,4));W=V.copy()
    for m,delta in enumerate(errors):
        V[2*m,m]=1
        overlap=1-delta*delta/2
        W[2*m,m]=overlap;W[2*m+1,m]=np.sqrt(1-overlap*overlap)
    operator_error=float(np.linalg.norm(V-W,2))
    close(operator_error,max(errors),'Code norm is maximum, not sum',1e-12)
    R=rng.normal(size=(4,6))+1j*rng.normal(size=(4,6));R/=np.linalg.norm(R)
    require(np.linalg.norm((V-W)@R)<=operator_error+1e-13,'Arbitrary reference dimension')
    for m in [2,5,20]:
        miss=.2
        mean_fraction=1-miss/m
        all_in_probability=1-miss
        require(max(0,1-m*(1-mean_fraction))<=all_in_probability+1e-14<=mean_fraction+1e-14,
                'Absolute missed count, not just fractional concentration')
    return dict(cases=5,code_operator_error=operator_error,largest_sector_error=max(errors),
                scope='Block-orthogonality and occupation/fidelity controls, not a new mode-selection theorem.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    groups={}
    for name,fn in [('normalization_and_entropy_identity',test_normalization_and_entropy_identity),
                    ('channel_and_reference',test_channel_and_reference),
                    ('endpoint_safe_geometry',test_endpoint_safe_geometry),
                    ('finite_envelopes_and_limits',test_finite_envelopes_and_limits),
                    ('isometry_and_collection',test_isometry_and_collection)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-03',group_count=len(groups),cases=sum(v['cases'] for v in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),
                groups=groups,scope='Author-side finite proof diagnostics; neither independent review nor a new physical model.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
