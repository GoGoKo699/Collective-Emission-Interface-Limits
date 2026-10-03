#!/usr/bin/env python3
"""A fixed optical-mode interface for an ideal Dicke ladder.

Checks exact density-relative-entropy identities, all-code fidelity bounds,
a joint asymptotic limit, the complete emission-amplitude recursion, a
state-independent time/phase change, and the receiver-channel argument.
No earlier scientific module is imported. See RESULT.md for proofs and scope.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from math import pi
from pathlib import Path
import platform
import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.stats import binom

mp.mp.dps = 65
SEED = 2026100202
RNG = np.random.default_rng(SEED)


def need(test, message):
    if not test:
        raise AssertionError(message)


def near(a, b, label, tol=2e-10):
    error = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    need(np.isfinite(error) and error <= tol, f'{label}: {error:g} > {tol:g}')
    return error


def pulse(t, a):
    if not 0 <= a < 1:
        raise ValueError('Mode parameter must be in [0,1).')
    return np.sqrt(1-a)*np.exp(-np.asarray(t)/2)/(1-a+a*np.exp(-np.asarray(t)))


def log_inner(a, b):
    z = float(np.log1p(-b)-np.log1p(-a))
    if abs(z) < 1e-3:
        # log[z/(2 sinh(z/2))], continuous at zero.
        return -z*z/24+z**4/2880-z**6/181440+z**8/9676800
    return float(np.log(abs(z))-np.log(2*np.sinh(abs(z)/2)))


def angle_logcos(value):
    """Stable arccos(exp(value)) for value<=0."""
    if value > 1e-12:
        raise ValueError('Cosine cannot exceed one.')
    value = min(0., value)
    return float(np.arctan2(np.sqrt(-np.expm1(2*value)), np.exp(value)))


@lru_cache(None)
def relative_entropy(N: int, m: int):
    if not 0 <= m <= N:
        raise ValueError('Need 0<=m<=N.')
    if m <= 1:
        return 0.
    n = mp.mpf(N)
    a = mp.mpf(m-1)/n
    b = 1-a
    logC = mp.loggamma(n+1)-mp.loggamma(n-m+1)-m*mp.log(n)
    answer = m*(-b/a*mp.log(b)-1)-logC
    need(answer >= -mp.mpf('1e-50'), 'Negative relative entropy')
    return float(max(0, answer))


def entropy_bound(N, m):
    if m <= 1:
        return 0.
    b = 1-(m-1)/N
    return m*(m-1)/(12*N*N*b*b)


def full_overlap(N, m, a, T=42., rtol=1e-10, oscillator=False):
    """Exact continuum overlap ODE; return finite horizon and a separate tail bound."""
    if m == 0:
        return dict(fidelity=1., amplitude=1., cutoff=T, omitted_fidelity_bound=0.)
    k = np.arange(m, -1, -1)
    ell = k.astype(float) if oscillator else k*(1-(k-1)/N)
    ell[-1] = 0.
    coupling = np.sqrt(np.arange(m, 0, -1)*ell[:-1])
    def rhs(t, z):
        dz = -.5*ell*z
        dz[1:] += coupling*pulse(t, a)*z[:-1]
        return dz
    initial = np.zeros(m+1)
    initial[0] = 1.
    out = solve_ivp(rhs, (0., T), initial, method='DOP853', rtol=rtol,
                    atol=2e-15, max_step=.18)
    need(out.success, out.message)
    amplitude = float(out.y[-1, -1])
    rmin = 1. if oscillator else 1-(m-1)/N
    late_true = min(1., m*np.exp(-rmin*T))
    late_target = min(1., m*np.exp(-T)/(1-a+a*np.exp(-T)))
    late_amp = np.sqrt(late_true*late_target)
    return dict(fidelity=amplitude**2, amplitude=amplitude, cutoff=T,
                omitted_fidelity_bound=float(2*late_amp+late_amp**2),
                ode_rtol=rtol, ode_atol=2e-15)


def matched_beta(N, m):
    return angle_logcos(-relative_entropy(N, m)/2)


def fixed_mode_guarantee(N, M, all_m=True):
    """Guaranteed lower bound, not the exact finite minimax optimum."""
    if M <= 1:
        return dict(lower=1., mode_a=0., source='exact vacuum/one-photon code')
    a = (.75*M-1)/N
    if all_m:
        values = []
        for m in range(1, M+1):
            angle = angle_logcos(m*log_inner((m-1)/N, a))+matched_beta(N, m)
            values.append(np.cos(angle)**2 if angle < pi/2 else 0.)
        return dict(lower=float(min(values)), mode_a=a, worst_bound_number=int(np.argmin(values)+1),
                    source='all photon numbers evaluated in analytic angle bound')
    b = 1-(M-1)/N
    product_logamp = -M**3/(384*N*N*b*b)
    angle = angle_logcos(product_logamp)+angle_logcos(-entropy_bound(N, M)/2)
    return dict(lower=float(np.cos(angle)**2 if angle < pi/2 else 0.), mode_a=a,
                source='closed all-code lower bound; no photon-number scan')


def all_mode_upper(N, M):
    """Analytic two-sector obstruction valid for every normalized receiver mode."""
    if M <= 1:
        return 1.
    q = max(1, M//4)
    separation = angle_logcos(log_inner((q-1)/N, (M-1)/N))
    def radius(F, m):
        total = angle_logcos(np.log(F)/2)+matched_beta(N, m)
        if total >= pi/2:
            return pi/2
        return angle_logcos(float(np.log(np.cos(total))/m))
    def residual(F):
        return radius(F,q)+radius(F,M)-separation
    if residual(1.) >= 0:
        return 1.
    return float(brentq(residual, 1e-14, 1., xtol=3e-13, rtol=1e-13))


def test_exact_entropy():
    rows = []
    for N,m in [(10,2),(12,4),(50,10),(100,10),(1000,100),(1000,200),(10000,300)]:
        D = relative_entropy(N,m)
        B = entropy_bound(N,m)
        need(D <= B+2e-14, 'Uniform entropy upper bound')
        row = dict(N=N,m=m,exact_relative_entropy=D,entropy_upper_bound=B,
                   guaranteed_matched_fidelity=float(np.exp(-D)))
        if m <= 10:
            a = (m-1)/N
            ks = np.arange(1,m+1)
            def integrand(S):
                if S <= 0:
                    return 0.
                h = 1-a*S
                rates = 1-(ks-1)/N
                terms = h*np.log(h/rates)-h+rates
                return np.sum(binom.pmf(ks,m,S)*ks*terms)/(S*h)
            path_integral, _ = quad(integrand, 0., 1., epsabs=2e-12, epsrel=2e-11)
            row['independent_counting_process_integral'] = float(path_integral)
            near(path_integral,D,'Independent complete-path relative entropy',3e-12)
        numerical = full_overlap(N,m,(m-1)/N)
        need(numerical['fidelity']+3e-9 >= np.exp(-D), 'Entropy-to-fidelity guarantee')
        row['exact_cascade_fidelity'] = numerical['fidelity']
        row['late_tail_bound'] = numerical['omitted_fidelity_bound']
        rows.append(row)
    overlaps = []
    for a,b in [(0.,.1),(.2,.5),(.7,.9),(.1,.10001)]:
        integral, _ = quad(lambda t:pulse(t,a)*pulse(t,b),0,np.inf,epsabs=2e-12)
        analytic = np.exp(log_inner(a,b))
        near(integral,analytic,'Normalized waveform overlap',2e-11)
        overlaps.append(dict(a=a,b=b,integral=integral,formula=analytic))
    for a in [0.,.2,.8]:
        norm,_=quad(lambda t:pulse(t,a)**2,0,np.inf,epsabs=2e-12)
        near(norm,1.,'Waveform normalization')
    # Stable exact gamma-function formula checked at more than one precision.
    with mp.workdps(90):
        N,m=10**9,10**6
        a=mp.mpf(m-1)/N;b=1-a
        D=m*(-b/a*mp.log(b)-1)-(mp.loggamma(N+1)-mp.loggamma(N-m+1)-m*mp.log(N))
        near(relative_entropy(N,m),float(D),'Large-integer entropy cancellation',2e-16)
    return dict(cases=len(rows)+len(overlaps)+4,entropy=rows,mode_overlaps=overlaps)


def test_code_bounds():
    small = []
    for N,M in [(20,6),(50,12),(100,24)]:
        g = fixed_mode_guarantee(N,M)
        upper = all_mode_upper(N,M)
        values=[full_overlap(N,m,g['mode_a'])['fidelity'] for m in range(M+1)]
        need(g['lower']<=min(values)+2e-9,'Constructive guarantee below actual worst code state')
        need(min(values)<=upper+2e-9,'All-mode upper bound')
        small.append(dict(N=N,M=M,analytic_lower=g['lower'],analytic_upper=upper,
                          evaluated_all_numbers=True,fixed_mode_worst_fidelity=min(values),
                          minimizing_number=int(np.argmin(values)),a=g['mode_a']))
    large=[]
    for N,M in [(1000,100),(1000,200),(1000,300),(8000,400),(8000,800)]:
        lo=fixed_mode_guarantee(N,M)
        hi=all_mode_upper(N,M)
        sampled_numbers=sorted(set([1,M//4,M//2,M]))
        tested=[]
        for m in sampled_numbers:
            F=full_overlap(N,m,lo['mode_a'])
            need(F['fidelity']>=lo['lower']-3e-9,'Sampled state violates all-code guarantee')
            tested.append(dict(m=m,**F))
        need(lo['lower']<=hi+1e-12,'Analytic bracket order')
        need(min(x['fidelity'] for x in tested)<=hi+3e-9,'Witness sectors against any-mode bound')
        large.append(dict(N=N,M=M,constructive_lower=lo['lower'],all_modes_upper=hi,
                          chosen_a=lo['mode_a'],sampled_numbers=tested,
                          scope='Bounds cover all m; displayed ODEs cover only listed m, not a finite-N global optimization.'))
    return dict(cases=len(small)+len(large),small_codes=small,finite_brackets=large)


def test_joint_limit():
    rows=[]
    for c in [1,2,3]:
        target=float(np.exp(-c**3/192))
        for N in [1000,10**6,10**9]:
            base={1000:100,10**6:10000,10**9:1000000}[N]
            M=c*base
            lo=fixed_mode_guarantee(N,M,all_m=False)['lower']
            hi=all_mode_upper(N,M)
            need(lo<=hi+1e-10,'Joint-limit analytic bracket')
            rows.append(dict(N=N,M=M,c=c,guaranteed_lower=lo,guaranteed_upper=hi,
                             limiting_value=target,bracket_width=hi-lo))
        need(abs(rows[-1]['guaranteed_lower']-target)<.002 and
             abs(rows[-1]['guaranteed_upper']-target)<.002,'Joint-limit consistency')
        need(rows[-1]['bracket_width']<rows[-2]['bracket_width']<rows[-3]['bracket_width'],
             'Converging analytic brackets')
    examples=[]
    for N,M in [(10**6,100),(10**9,10000)]:
        examples.append(dict(N=N,M=M,lower=fixed_mode_guarantee(N,M,all_m=False)['lower']))
    # No probability wavefunction at a billion-body dimension is numerically stored.
    return dict(cases=len(rows)+len(examples),critical_sequences=rows,subcritical_examples=examples,
                scope='Scalar evaluations of proved finite bounds, not huge-emitter simulations or a fitted exponent.')


def test_scalar_control():
    rows=[]
    N=30;a=.12
    for m in [1,3,8]:
        k=np.arange(m,-1,-1);ell=k*(1-(k-1)/N);ell[-1]=0
        coefficients=np.sqrt(np.arange(m,0,-1)*ell[:-1])
        gamma=lambda t:.85+.15*np.cos(2*t)
        clock=lambda t:.85*t+.075*np.sin(2*t)
        phi=lambda t:.3*np.sin(t)
        omega=.23
        T=50.
        def rhs(t,z):
            Gamma=gamma(t);tau=clock(t)
            f=np.sqrt(Gamma)*pulse(tau,a)*np.exp(1j*(phi(t)-omega*t))
            dz=(-Gamma*ell/2-1j*omega*k)*z
            dz[1:]+=coefficients*np.sqrt(Gamma)*np.exp(1j*phi(t))*f.conjugate()*z[:-1]
            return dz
        initial=np.zeros(m+1,complex);initial[0]=1
        out=solve_ivp(rhs,(0,T),initial,method='DOP853',rtol=3e-11,atol=2e-14,max_step=.1)
        need(out.success,out.message)
        standard=full_overlap(N,m,a,T=clock(T),rtol=3e-11)
        err=near(out.y[-1,-1],standard['amplitude'],'Lab shaped/phase evolution versus common-clock mode',2e-10)
        rows.append(dict(N=N,m=m,lab_end_time=T,common_clock_horizon=clock(T),
                         ordinary_fidelity=standard['fidelity'],controlled_fidelity=float(abs(out.y[-1,-1])**2),
                         amplitude_error=err))
    # Nonlinear ladder compensation is not scalar modulation: verify its matrix elements.
    n=11;Gamma=1.7
    spin=np.zeros((n+1,n+1))
    for k in range(1,n+1):spin[k-1,k]=np.sqrt(k*(n-k+1))
    compensation=np.diag(1/np.sqrt(n-np.arange(n+1)+1))
    L=np.sqrt(Gamma)*spin@compensation
    ideal=np.diag(np.sqrt(Gamma*np.arange(1,n+1)),1)
    near(L,ideal,'Declared number-dependent ladder linearization')
    for m in [1,3,10]:
        near(full_overlap(max(20,m),m,0.,oscillator=True)['fidelity'],1.,'Harmonic reference',3e-9)
    return dict(cases=len(rows)+4,time_change=rows,
                linearized_ladder_scope='An algebraic control outside the allowed scalar class, not a hardware implementation or new oscillator-emission principle.')


def test_receiver_semantics():
    """Structural Kraus check, not a fabricated simulation of the whole Dicke field."""
    rows=[]
    # Generic photon-number-preserving isometries on receiver plus environment.
    # Positive K0 entries are the only structure needed by the analytical theorem.
    for cutoff in [2,4,8]:
        for _ in range(6):
            A=RNG.uniform(.2,1.,cutoff+1);A[0]=1
            K=[np.diag(A).astype(complex)]
            for ell in range(1,cutoff+1):
                K.append(np.zeros((cutoff+1,cutoff+1),complex))
            for m in range(1,cutoff+1):
                weights=RNG.dirichlet(np.ones(m))*(1-A[m]**2)
                for ell,w in enumerate(weights,1):
                    K[ell][m-ell,m]=np.sqrt(w)*np.exp(1j*RNG.uniform(-pi,pi))
            near(sum(x.conj().T@x for x in K),np.eye(cutoff+1),'Number-conserving receiver is trace preserving')
            lower=float(min(A)**2)
            for _ in range(12):
                X=RNG.normal(size=(cutoff+1,cutoff+1))+1j*RNG.normal(size=(cutoff+1,cutoff+1))
                rho=X@X.conj().T;rho/=np.trace(rho)
                Fe=float(sum(abs(np.trace(rho@x))**2 for x in K))
                need(Fe>=lower-2e-12,'Receiver worst entanglement-fidelity lower bound')
            m=int(np.argmin(A));rho=np.zeros((cutoff+1,cutoff+1));rho[m,m]=1.
            saturated=float(sum(abs(np.trace(rho@x))**2 for x in K))
            near(saturated,lower,'Fock basis attains worst receiver fidelity')
            rows.append(dict(cutoff=cutoff,min_no_environment_amplitude_squared=lower,
                             saturating_number=m,entanglement_fidelity=saturated))
    return dict(cases=len(rows),generic_number_conserving_channels=rows,
                scope='Tests the general Kraus argument with constructed channels; these are not substituted for an exact Dicke reduced-field simulation.')


def test_refinement():
    rows=[]
    for N,m,a in [(1000,100,.074),(1000,200,.149),(1000,300,.224)]:
        a0=full_overlap(N,m,a,T=42.)
        a1=full_overlap(N,m,a,T=48.,rtol=2e-12)
        err=near(a0['fidelity'],a1['fidelity'],'ODE tolerance/horizon refinement',3e-8)
        need(max(a0['omitted_fidelity_bound'],a1['omitted_fidelity_bound'])<5e-12,'Tail error budget')
        rows.append(dict(N=N,m=m,a=a,first=a0,refined=a1,fidelity_difference=err))
    return dict(cases=len(rows),rows=rows,
                scope='Tail bounds are analytic; solve_ivp integration error is assessed by convergence, not enclosed by the tail bound.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    groups={}
    for name,fn in [('entropy_and_waveforms',test_exact_entropy),('finite_code_fidelity',test_code_bounds),
                    ('joint_limit',test_joint_limit),('source_controls',test_scalar_control),
                    ('receiver_channel',test_receiver_semantics),('numerical_refinement',test_refinement)]:
        groups[name]=fn();print('PASS',name,flush=True)
    result=dict(status='PASS',date='2026-10-02',seed=SEED,groups=groups,
                group_count=len(groups),cases=sum(x['cases'] for x in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),
                scope='Independent author-side diagnostics for the stated derivation. No independent review, experimental observation, or exhaustive novelty certification.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
