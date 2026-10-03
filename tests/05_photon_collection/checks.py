#!/usr/bin/env python3
"""Uniform photon collection versus full-state transfer in the fixed Dicke model.

The only new analytical claim tested here is a corollary for the photon fraction
in the already specified common mode. The previous optimized-code theorem is
retained, not redefined. No inherited scientific module is imported.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp

SEED = 2026100305
RNG = np.random.default_rng(SEED)


def need(condition: bool, text: str) -> None:
    if not condition:
        raise AssertionError(text)


def near(a, b, text: str, tolerance: float = 2e-10) -> float:
    error = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    need(np.isfinite(error) and error <= tolerance, f'{text}: {error} > {tolerance}')
    return error


def parameters(N: int, M: int) -> tuple[float, float]:
    if not isinstance(N, int) or not isinstance(M, int) or N < 1 or M < 0 or M > N:
        raise ValueError('Need integers 0 <= M <= N with N >= 1.')
    return (0. if M <= 1 else (.75*M-1)/N), 1-(M-1)/N


def mode(t, a: float):
    if not 0 <= a < 1:
        raise ValueError('Need 0 <= a < 1.')
    y = np.exp(-np.asarray(t))
    return np.sqrt(1-a)*np.exp(-np.asarray(t)/2)/(1-a+a*y)


def kernel(z: float) -> float:
    if abs(z) < 1e-3:
        return 1-z*z/24+7*z**4/5760-31*z**6/967680
    return z/(2*np.sinh(z/2))


def missed_fraction_bound(N: int, M: int) -> float:
    _, b = parameters(N, M)
    return 0. if M <= 1 else min(1.,25*M*M/(192*N*N*b*b))


@lru_cache(None)
def exact_mean_fraction(N: int, m: int, a: float, T: float = 70.,
                        rtol: float = 2e-10, oscillator: bool = False) -> dict:
    """Integrate exact source populations and regression coherences.

    x_k = integral_0^t f(s) [ exp(L(t-s))(rho(s)L^dagger) ]_(k,k-1) ds.
    The scalar accumulator is the photon number in the unnormalized truncated
    pulse 1_[0,T] f. It is not conditioned on photon detection or source decay.
    """
    if N < m or m < 1 or T <= 0 or rtol <= 0 or not 0 <= a < 1:
        raise ValueError('Invalid N, m, pulse, integration horizon, or tolerance.')
    k = np.arange(m+1,dtype=float)
    ell = k if oscillator else k*(1-(k-1)/N)
    ell[0] = 0
    root = np.sqrt(ell[1:])
    decay = .5*(ell[1:]+ell[:-1])
    feed = np.sqrt(ell[2:]*ell[1:-1])
    initial = np.zeros(2*m+2); initial[m] = 1.
    def rhs(t,y):
        p=y[:m+1];x=y[m+1:-1];f=mode(t,a)
        dp=-ell*p;dp[:-1]+=ell[1:]*p[1:]
        dx=-decay*x+f*root*p[1:];dx[:-1]+=feed*x[1:]
        return np.r_[dp,dx,2*f*np.dot(root,x)]
    sol=solve_ivp(rhs,(0,T),initial,method='DOP853',rtol=rtol,atol=rtol/200)
    need(sol.success,sol.message)
    final=sol.y[:,-1]
    near(np.sum(final[:m+1]),1.,'Source probability conservation',4e-10)
    value=float(final[-1]/m)
    need(-2e-10<=value<=1+2e-10,'Nonphysical normalized mean')
    tail=np.exp(-T)/(1-a+a*np.exp(-T))
    # Bound for any m-photon state: || |f><f|-|f_T><f_T| || <= 2 sqrt(tail)+tail.
    return dict(fraction=value,T=T,rtol=rtol,nfev=sol.nfev,
                one_photon_mode_tail=float(tail),
                absolute_fraction_tail_allowance=float(2*np.sqrt(tail)+tail),
                remaining_source_mean=float(np.dot(k,final[:m+1])),
                source_probability_residual=float(abs(np.sum(final[:m+1])-1)))


def all_in_mode_probability(N: int,m: int,a: float,T: float=40.) -> float:
    """Independent exact amplitude recurrence, not extracted from mean photons."""
    k=np.arange(m,-1,-1,dtype=float);ell=k*(1-(k-1)/N)
    couplings=np.sqrt(k[:-1]*ell[:-1])
    initial=np.zeros(m+1);initial[0]=1.
    def rhs(t,y):
        out=-ell*y/2
        out[1:]+=couplings*mode(t,a)*y[:-1]
        return out
    sol=solve_ivp(rhs,(0,T),initial,method='DOP853',rtol=2e-11,atol=2e-15,max_step=.1)
    need(sol.success,sol.message)
    return float(sol.y[-1,-1]**2)


def test_scalar_bound() -> dict:
    rows=[];max_integral_error=0.;cases=0
    for N,M in [(2,2),(10,3),(40,10),(128,50),(1000,100),(1000,300),(10000,1000)]:
        a,b=parameters(N,M)
        for m in sorted(set([1,max(1,M//4),max(1,3*M//4),M])):
            am=(m-1)/N
            z=np.log1p(-a)-np.log1p(-am)
            angular=math.sqrt(max(0.,1-kernel(z)**2))
            need(angular<=abs(z)/np.sqrt(12)+2e-13,'Pulse metric bound')
            need(abs(z)<=abs(m-.75*M)/(N*b)+2e-13,'Uniform logarithm bound')
            eps=math.sqrt(m*(m-1))/(math.sqrt(12)*N*b)
            exact_bound=(angular+eps)**2
            formula=(abs(m-.75*M)+math.sqrt(m*(m-1)))**2/(12*N*N*b*b)
            need(exact_bound<=formula+1e-12,'Sector algebraic bound')
            need(formula<=25*M*M/(192*N*N*b*b)+1e-12,'Max over the number code')
            cases+=1
        rows.append(dict(N=N,M=M,common_mode_a=a,guaranteed_photon_fraction=1-missed_fraction_bound(N,M)))
    # Independent integral in y=exp(-tau): f_a f_b d tau = sqrt((1-a)(1-b))/(...)(...) dy.
    for a,b in [(0.,.2),(.01,.8),(.224,.299),(.5,.5)]:
        integral=quad(lambda y:np.sqrt((1-a)*(1-b))/((1-a+a*y)*(1-b+b*y)),0,1,
                      epsabs=1e-12,epsrel=1e-12)[0]
        z=np.log1p(-b)-np.log1p(-a)
        max_integral_error=max(max_integral_error,near(integral,kernel(z),'Direct pulse overlap'))
        cases+=1
    return dict(cases=cases,rows=rows,maximum_overlap_integral_error=max_integral_error,
                scope='Checks of analytic inequalities, not an enumeration proof for all N.')


def test_exact_regression_controls() -> dict:
    rows=[]
    for N,a in [(2,0.),(10,.2),(100,.75)]:
        value=exact_mean_fraction(N,1,a)
        target=kernel(-np.log1p(-a))**2
        err=near(value['fraction'],target,'One-photon exact mode overlap',2e-10)
        rows.append(dict(control='one photon',N=N,a=a,fraction=value['fraction'],analytic=target,error=err))
    # Direct two-photon marginal integration evaluated analytically for f_0.
    for N in [2,3,10,100]:
        a=1/N;b=1-a
        analytic=(1-2*a/(1+b)+a*a/(1+2*b))/b
        value=exact_mean_fraction(N,2,0.)
        err=near(value['fraction'],analytic,'Two-photon exact marginal',2e-10)
        rows.append(dict(control='two-photon marginal',N=N,fraction=value['fraction'],analytic=analytic,error=err))
    for m,a in [(2,0.),(8,0.),(20,.2)]:
        value=exact_mean_fraction(max(m,20),m,a,oscillator=True)
        target=kernel(-np.log1p(-a))**2
        err=near(value['fraction'],target,'Harmonic-oscillator all-number common mode',3e-10)
        rows.append(dict(control='linear oscillator',m=m,a=a,fraction=value['fraction'],analytic=target,error=err))
    return dict(cases=len(rows),controls=rows,
                scope='QRT mean occupation checked against exact one- and two-photon formulas and linear emission.')


def test_full_finite_examples() -> dict:
    rows=[]
    for N,M,m in [(128,50,12),(128,50,50),(1000,300,75),(1000,300,300)]:
        a,_=parameters(N,M)
        mean=exact_mean_fraction(N,m,a)
        full=all_in_mode_probability(N,m,a)
        need(full<=mean['fraction']+2e-10,'All-in-mode probability exceeds mean fraction')
        floor=1-missed_fraction_bound(N,M)
        need(mean['fraction']>=floor-1e-10,'Uniform mean-fraction guarantee')
        rows.append(dict(N=N,M=M,m=m,receiving_mode_a=a,mean=mean,
                         all_in_mode_probability=full,uniform_code_mean_fraction_lower=floor))
    # Repeating the hardest displayed moment with tighter tolerance and a later horizon.
    refined=exact_mean_fraction(1000,300,.224,T=80.,rtol=2e-12)
    difference=near(refined['fraction'],rows[-1]['mean']['fraction'],'Mean integration refinement',3e-10)
    return dict(cases=len(rows)+1,finite_rows=rows,refined_largest_case=refined,
                refinement_difference=difference,
                scope='Known exact model solved numerically; not interval-certified decimals or experimental data.')


def test_positive_contractions_and_code() -> dict:
    # Numerical diagnostics of the purification/triangle step, including mixed states.
    margins=[]
    for dimension in [4,9,20]:
        for _ in range(10):
            raw=RNG.normal(size=(dimension,dimension))+1j*RNG.normal(size=(dimension,dimension))
            E=raw@raw.conj().T;E/=np.linalg.norm(E,2)
            phi=RNG.normal(size=dimension)+1j*RNG.normal(size=dimension);phi/=np.linalg.norm(phi)
            psi=phi+.1*(RNG.normal(size=dimension)+1j*RNG.normal(size=dimension));psi/=np.linalg.norm(psi)
            actual=math.sqrt(max(0.,np.vdot(psi,E@psi).real))
            upper=math.sqrt(max(0.,np.vdot(phi,E@phi).real))+np.linalg.norm(psi-phi)
            need(actual<=upper+1e-12,'Positive contraction triangle inequality')
            margins.append(float(upper-actual))
    # Arbitrary coherences in a finite code do not change expectation of a number-preserving observable.
    N,M=40,6;a,_=parameters(N,M)
    captured=[0.]+[m*exact_mean_fraction(N,m,a)['fraction'] for m in range(1,M+1)]
    min_ratio=1.
    for _ in range(12):
        R=RNG.normal(size=(M+1,M+1))+1j*RNG.normal(size=(M+1,M+1))
        rho=R@R.conj().T;rho/=np.trace(rho)
        total=float(np.trace(rho@np.diag(np.arange(M+1))).real)
        selected=float(np.trace(rho@np.diag(captured)).real)
        ratio=selected/total;min_ratio=min(min_ratio,ratio)
        need(ratio>=1-missed_fraction_bound(N,M)-1e-11,'Ratio of means for a mixed code input')
    return dict(cases=len(margins)+12,minimum_triangle_slack=min(margins),
                mixed_code_minimum_photon_fraction=min_ratio,
                scope='The analytical block-diagonal argument, not sampled states, covers arbitrary reference entanglement.')


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('uniform_collection_bound',test_scalar_bound),
                    ('regression_controls',test_exact_regression_controls),
                    ('finite_mean_and_fidelity',test_full_finite_examples),
                    ('state_independent_extension',test_positive_contractions_and_code)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-03',seed=SEED,
                group_count=len(groups),cases=sum(g['cases'] for g in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                groups=groups,
                scope='New mean-collection corollary and finite checks; inherited optimization theorem remains separately attributed. Not external review, novelty certification, or hardware data.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)


if __name__=='__main__':
    main()
