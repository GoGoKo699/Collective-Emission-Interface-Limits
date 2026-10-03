#!/usr/bin/env python3
"""Collective emission: a fixed optical mode versus number-specific mode matching.

The known Dicke decay law and exponential-mode overlap are attributed in RESULT.md.
This script propagates the complete ordered-emission amplitudes, not a sampled
record and not a postselected master equation. It imports no earlier project code.
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
from scipy.optimize import brentq, minimize_scalar


def require(ok: bool, message: str) -> None:
    if not ok: raise AssertionError(message)


def near(x: float, y: float, message: str, tol: float=2e-10) -> float:
    err=float(abs(x-y));require(err<=tol, f'{message}: {err} > {tol}');return err


def log_exponential_fidelity(N: int,m: int,speed: float=1.) -> float:
    if not isinstance(N,int) or not isinstance(m,int) or N<1 or not 0<=m<=N or speed<=0:
        raise ValueError('Require integers 0 <= m <= N and positive mode speed.')
    if m==0:return 0.
    r=1-np.arange(m,dtype=float)/N
    return float(np.sum(np.log(4*r*speed/(r+speed)**2)))


def best_exponential(N: int,m: int):
    if m==0:return 1.,1.
    r=1-np.arange(m,dtype=float)/N
    speed=1. if m==1 else brentq(lambda s:np.sum((r-s)/(r+s)),float(min(r)),1.,xtol=1e-14)
    return speed, math.exp(log_exponential_fidelity(N,m,speed))


def mode(t: float,kind: str,parameter: float) -> float:
    if kind=='exponential':return math.sqrt(parameter)*math.exp(-parameter*t/2)
    if kind=='reshaped':return math.sqrt(1-parameter)*math.exp(-t/2)/(1-parameter+parameter*math.exp(-t))
    raise ValueError(kind)


@lru_cache(None)
def cascade_fidelity(N: int,m: int,kind: str='exponential',parameter: float=1.,
                     duration: float=42.,tol: float=2e-11,harmonic: bool=False):
    if not 0<=m<=N:raise ValueError('Require 0 <= m <= N.')
    if kind=='reshaped' and not 0<=parameter<1:raise ValueError('Shape parameter must lie in [0,1).')
    if kind=='exponential' and parameter<=0:raise ValueError('Positive rate needed.')
    if m==0:return dict(fidelity=1.,amplitude=1.,tail_fidelity_bound=0.,nfev=0)
    remaining=np.arange(m,-1,-1,dtype=float)
    rates=remaining.copy() if harmonic else remaining*(1-(remaining-1)/N)
    rates[-1]=0
    coupling=np.sqrt(remaining[:-1]*rates[:-1])
    def rhs(t,z):
        dz=-rates*z/2
        dz[1:]+=coupling*mode(t,kind,parameter)*z[:-1]
        return dz
    initial=np.zeros(m+1);initial[0]=1.
    sol=solve_ivp(rhs,(0,duration),initial,method='DOP853',rtol=tol,atol=2e-15,max_step=.15)
    require(sol.success,sol.message)
    amplitude=float(sol.y[-1,-1])
    # Compare the omitted ordered-amplitude integral by Cauchy-Schwarz on the
    # event that at least one photon is late. The death process is dominated by
    # independent rate-rmin emissions; the target-mode union bound is explicit.
    rmin=1. if harmonic else 1-(m-1)/N
    emitted_tail=min(1.,m*math.exp(-rmin*duration))
    if kind=='exponential':single_tail=math.exp(-parameter*duration)
    else:single_tail=math.exp(-duration)/(1-parameter+parameter*math.exp(-duration))
    target_tail=min(1.,m*single_tail)
    overlap_tail=math.sqrt(emitted_tail*target_tail)
    fidelity=amplitude**2
    require(-1e-12<=fidelity<=1+3e-9,'Unphysical full-state overlap')
    return dict(fidelity=fidelity,amplitude=amplitude,
                tail_fidelity_bound=2*overlap_tail+overlap_tail**2,nfev=sol.nfev)


def two_photon_quadrature(N: int,a: float) -> float:
    pref=math.sqrt(1-1/N)
    def ratio(u):return math.sqrt(1-a)/(1-a+a*u)
    def integral_ratio(u):
        return u if a==0 else math.sqrt(1-a)/a*math.log1p(a*u/(1-a))
    amp=2*pref*quad(lambda u:u**(-1/N)*ratio(u)*integral_ratio(u),0.,1.,epsabs=2e-12,epsrel=2e-12)[0]
    return amp*amp


def local_loss_coefficient(m: int,b: float) -> float:
    return m*(m-1-b)**2/12 + m*(m-1)/24


def minimax_coefficient(M: int):
    ms=np.arange(1,M+1,dtype=float)
    fun=lambda b:float(np.max(ms*(ms-1-b)**2/12+ms*(ms-1)/24))
    result=minimize_scalar(fun,bounds=(0.,float(M-1)),method='bounded',options={'xatol':1e-10})
    b=float(result.x); vals=ms*(ms-1-b)**2/12+ms*(ms-1)/24
    return b,float(result.fun),[int(i+1) for i in np.where(vals>=result.fun*(1-1e-6))[0]]


def test_exact_baselines():
    cases=[]
    for N,m in [(2,2),(10,2),(20,5),(100,10),(100,50),(1000,100)]:
        for s in [1.,best_exponential(N,m)[0]]:
            calc=cascade_fidelity(N,m,'exponential',s)
            exact=math.exp(log_exponential_fidelity(N,m,s))
            err=near(calc['fidelity'],exact,'Cascade versus exact overlap product',2e-9)
            cases.append(dict(N=N,m=m,speed=s,fidelity=calc['fidelity'],product=exact,error=err))
    quads=[]
    for N in [3,10,50]:
        for a in [0.,(2-1)/N,.3]:
            val=two_photon_quadrature(N,a)
            calc=cascade_fidelity(N,2,'reshaped',a)['fidelity']
            err=near(calc,val,'Independent two-photon integral',2e-10)
            quads.append(dict(N=N,shape=a,fidelity=calc,quadrature=val,error=err))
    for m in [1,2,20,100]:
        near(cascade_fidelity(max(m,1),m,harmonic=True)['fidelity'],1.,'Harmonic oscillator fixed-mode comparator',3e-9)
    return dict(cases=len(cases)+len(quads)+4,product_controls=cases,two_photon_integrals=quads,
                meaning='Oscillator rates k*Gamma give exactly one common mode for every initial photon number.')


def test_perturbation_moments():
    # Under X,Y iid Exp(1), h=min(X,Y), h1=1/2-exp(-X).
    # h2=min(X,Y)-3/2+exp(-X)+exp(-Y) is degenerate in either argument.
    var1=quad(lambda x:math.exp(-x)*(.5-math.exp(-x))**2,0,np.inf,epsabs=1e-12)[0]
    def inner(x):
        return quad(lambda y:math.exp(-y)*(min(x,y)-1.5+math.exp(-x)+math.exp(-y))**2,
                    0,x,epsabs=1e-12)[0]
    var2=2*quad(lambda x:math.exp(-x)*inner(x),0,np.inf,epsabs=1e-11)[0]
    near(var1,1/12,'One-body shape component variance',2e-12)
    near(var2,1/12,'Irreducible pair component variance',2e-11)
    conditional=[]
    for x in [.1,1.,3.,7.]:
        v=quad(lambda y:math.exp(-y)*(min(x,y)-1.5+math.exp(-x)+math.exp(-y)),0,x)[0]
        v+=quad(lambda y:math.exp(-y)*(min(x,y)-1.5+math.exp(-x)+math.exp(-y)),x,np.inf)[0]
        near(v,0.,'Degenerate pair kernel conditional mean',2e-11);conditional.append(v)
    rows=[]
    for m in [2,5,10]:
        predicted=m*(m-1)/24
        for N in [1000,2000]:
            value=cascade_fidelity(N,m,'reshaped',(m-1)/N,tol=3e-12)['fidelity']
            coefficient=(1-value)*N*N
            require(abs(coefficient/predicted-1)<.025,'Fixed-m shape-adapted coefficient')
            rows.append(dict(N=N,m=m,fidelity=value,scaled_loss=coefficient,predicted_fixed_m_coefficient=predicted))
    return dict(cases=2+len(conditional)+len(rows),var_h1=var1,var_h2=var2,fixed_m_checks=rows,
                limitation='Fixed-m expansion; not a uniform large-m theorem.')


def test_finite_comparison():
    rows=[]
    for N,m in [(100,10),(100,50),(1000,100),(1000,200),(1000,300)]:
        speed,best=best_exponential(N,m)
        shape=(m-1)/N
        custom=cascade_fidelity(N,m,'reshaped',shape)
        refined=cascade_fidelity(N,m,'reshaped',shape,duration=48.,tol=4e-12)
        err=near(custom['fidelity'],refined['fidelity'],'Tolerance and horizon refinement',2e-9)
        require(custom['fidelity']>best,'Shape comparator did not improve exponential family')
        rows.append(dict(N=N,m=m,fixed_exponential=math.exp(log_exponential_fidelity(N,m)),
                         best_exponential=best,best_exponential_speed=speed,
                         reshaped_mode_parameter=shape,reshaped_fidelity=custom['fidelity'],
                         tail_fidelity_bound=custom['tail_fidelity_bound'],refinement_difference=err))
    return dict(cases=len(rows),rows=rows,
                meaning='Same emitted state, different normalized receiving mode. No filtering or selection of successful runs is used.')


def test_one_mode_for_several_numbers():
    N=1000;ms=[1,10,100,200,300];shapes=[.099,.199,.299];rows=[]
    for m in ms:
        rows.append(dict(m=m,fidelities=[cascade_fidelity(N,m,'reshaped',a)['fidelity'] for a in shapes]))
    values=[cascade_fidelity(N,m,'reshaped',.199)['amplitude'] for m in [100,200]]
    superposition=(sum(values)/2)**2
    require(superposition<.97,'Number-superposition comparison unexpectedly too high')
    coefficients=[]
    for M in [4,10,30,100,1000,10000]:
        b,c,active=minimax_coefficient(M)
        coefficients.append(dict(M=M,b=b,coefficient=c,coefficient_over_Mcubed=c/M**3,active_numbers=active))
    near(coefficients[-1]['coefficient_over_Mcubed'],1/192,'Large-M limit of fixed-M coefficient',1e-5)
    # Independent pointwise minimax shape lower bound at first order, then check
    # the finite-N cascade at the active endpoints/interior of a small code.
    M=10;b,c,active=minimax_coefficient(M);N=2000
    losses=[(1-cascade_fidelity(N,m,'reshaped',b/N,tol=3e-12)['fidelity'])*N*N for m in range(1,M+1)]
    require(abs(max(losses)/c-1)<.02,'Small-code perturbative minimax coefficient')
    return dict(cases=len(rows)+len(coefficients)+M,common_shapes=shapes,number_rows=rows,
                equal_superposition_numbers=[100,200],equal_superposition_fidelity_common_shape_0199=superposition,
                local_minimax_coefficients=coefficients,small_code=dict(N=N,M=M,b=b,leading_coefficient=c,exact_scaled_losses=losses),
                limitation='The 1/192 coefficient is an ordered fixed-M then large-M limit; no uniform finite-N minimax claim.')


def test_normalization_and_exact_state():
    rows=[]
    for a in [0.,.1,.3,.7]:
        norm=quad(lambda t:mode(t,'reshaped',a)**2,0,np.inf,epsabs=1e-11)[0]
        near(norm,1.,'Analytic receiving pulse normalization',1e-11)
        rows.append(dict(shape=a,norm=norm))
    # Known exact exponential reference: first nonzero norm-squared tangent term.
    asym=[]
    for m in [2,5,10,20]:
        coefficient=m*(m-1)*(2*m-1)/24
        N=20000
        loss=-math.expm1(log_exponential_fidelity(N,m))
        require(abs(loss*N*N/coefficient-1)<.002,'Known fixed-mode perturbative coefficient')
        asym.append(dict(m=m,N=N,exact_scaled_loss=loss*N*N,coefficient=coefficient))
    # Direct first-photon decay of the Dicke ladder depends on starting m;
    # equalized linear-oscillator ladder is a separately specified physical model.
    return dict(cases=len(rows)+len(asym),mode_norms=rows,known_reference_asymptotics=asym)


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('independent_overlap_checks',test_exact_baselines),('orthogonal_error_components',test_perturbation_moments),
                    ('finite_same_source_comparator',test_finite_comparison),('one_mode_number_superpositions',test_one_mode_for_several_numbers),
                    ('normalizations_and_known_limit',test_normalization_and_exact_state)]:
        groups[name]=fn();print('PASS',name,flush=True)
    data=dict(status='PASS',date='2026-10-02',group_count=len(groups),cases=sum(v['cases'] for v in groups.values()),
              environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),groups=groups,
              scope='Fresh analytic scout with finite diagnostics. No old research package imported, no external proof review, no experimental or priority certificate.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
