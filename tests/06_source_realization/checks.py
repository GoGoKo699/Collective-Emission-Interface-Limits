#!/usr/bin/env python3
"""Checks of an implementation audit, not a new unrestricted noisy-interface model.

The ideal source/receiver theorem is preserved. Independent atomic decay is used
as an explicit test of a discarded-process assumption. Its useful-output weight
is known prior physics. The effective-size reparametrization and all-code bounds
are derived in RESULT.md. Full-cavity checks concern collection probability, not
its optimized temporal-mode fidelity or a uniform cavity-elimination theorem.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.special import gammaln

SEED=2026100306
RNG=np.random.default_rng(SEED)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def near(a,b,message,tol=2e-10):
    error=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    require(np.isfinite(error) and error<=tol,f'{message}: {error} > {tol}')
    return error


def log_success(N:int,m:int,r:float)->float:
    if not isinstance(N,int) or not isinstance(m,int) or not 0<=m<=N or r<0:
        raise ValueError('Require integer 0<=m<=N and r>=0.')
    return float(-np.log1p(r/(N-np.arange(m,dtype=float))).sum())


def success(N,m,r):
    return float(np.exp(log_success(N,m,r)))


def exponential_overlap_squared(N,m,r,beta):
    """Unconditional all-m photon overlap with f(t)=sqrt(beta)exp(-beta*t/2), gamma_c=1."""
    j=np.arange(m,dtype=float)
    return float(np.exp(np.log(4*beta*(N-j)/(N+r-j+beta)**2).sum()))


def jump_amplitude(N,m,r,intervals):
    k=np.arange(m,0,-1,dtype=float)
    c=k*(N-k+1)
    total=k*(N+r-k+1)
    return np.prod(np.sqrt(c))*np.exp(-.5*np.dot(total,intervals))


def test_exact_branch_and_pulse():
    rows=[];max_residual=0.
    for N in [2,5,20,100]:
        for m in sorted(set([1,min(2,N),min(5,N)])):
            for r in [0.,.1,1.,4.]:
                Q=N+r
                for _ in range(3):
                    k=np.arange(m,0,-1,dtype=float)
                    intervals=RNG.exponential(1/(k*(Q-k+1)))
                    actual=jump_amplitude(N,m,r,intervals)
                    ideal=jump_amplitude(Q,m,0.,intervals)
                    max_residual=max(max_residual,near(actual,np.sqrt(success(N,m,r))*ideal,'Amplitude factorization',1e-8))
                near(success(N,m,r),np.prod([(N-j)/(N+r-j) for j in range(m)]),'Branching probability')
                require(np.exp(-m*r/(N-m+1))-1e-13<=success(N,m,r)<=np.exp(-m*np.log1p(r/N))+1e-13,'Finite probability envelopes')
                beta=.7*Q
                direct=exponential_overlap_squared(N,m,r,beta)
                effective=success(N,m,r)*exponential_overlap_squared(Q,m,0,beta)
                near(direct,effective,'Pulse-overlap factorization')
                rows.append(dict(N=N,m=m,r=r,all_collected_probability=success(N,m,r)))
    # Independent ordered two-photon integration, not an algebraic substitution.
    integrals=[]
    for N,r,beta in [(3,.2,2.),(7,4.,5.),(20,1.,14.)]:
        def integral_t1(t2):
            f2=np.sqrt(beta)*np.exp(-beta*t2/2)
            inner=quad(lambda t1: jump_amplitude(N,2,r,[t1,t2-t1])*np.sqrt(beta)*np.exp(-beta*t1/2),
                       0.,t2,epsabs=1e-12,epsrel=1e-11)[0]
            return np.sqrt(2)*f2*inner
        A=quad(integral_t1,0.,np.inf,epsabs=2e-11,epsrel=2e-10)[0]
        exact=exponential_overlap_squared(N,2,r,beta)
        near(A*A,exact,'Ordered two-photon overlap',2e-10)
        integrals.append(dict(N=N,r=r,beta=beta,numerical_overlap_squared=A*A,analytic=exact))
    return dict(cases=len(rows)+len(integrals),max_amplitude_residual=max_residual,
                parameter_cases=rows,independent_integrals=integrals,
                scope='Complete-emission maximal collected-number branch; no experimental postselection.')


def atomic_operators(N):
    d=2**N;lower=[]
    for j in range(N):
        op=np.zeros((d,d),complex)
        for x in range(d):
            if (x>>j)&1:op[x^(1<<j),x]=1
        lower.append(op)
    number=sum(op.conj().T@op for op in lower)
    return lower,sum(lower),number


def test_full_atomic_space():
    rows=[]
    # All local jump anticommutators are included; their recycled outputs are
    # intentionally separate failing branches. Trace equals their complement's probability.
    for N in [2,3,4]:
        lower,S,number=atomic_operators(N);d=2**N
        for m in [1,min(2,N),N]:
            for r in [.1,1.]:
                c=S.conj().T@S+r*number
                generator=np.kron(S.conj(),S)-.5*(np.kron(np.eye(d),c)+np.kron(c.T,np.eye(d)))
                v=np.array([float(x.bit_count()==m) for x in range(d)],complex)
                v/=np.linalg.norm(v)
                rho=np.outer(v,v.conj())
                # All non-ground sectors have hazard at least r; the selected
                # small cases have much faster collective decay. Explicit tail check.
                out=(expm(60*generator)@rho.ravel(order='F')).reshape(d,d,order='F')
                actual=float(out[0,0].real)
                expected=success(N,m,r)
                near(actual,expected,'Full physical spin space versus exact product',2e-9)
                near(np.trace(out),actual,'Remaining excited trace',2e-9)
                rows.append(dict(N=N,m=m,r=r,full_spin_ground_probability=actual,product_probability=expected))
    return dict(cases=len(rows),full_spin_cases=rows,
                scope='A trace-decreasing no-uncollected-photon block of the full Lindblad channel. Missing trace is retained as failure, not normalized away.')


def cavity_probabilities(N,M,g,kappa,gamma_i):
    E=np.ones((1,1),complex);probs=[];max_res=0.
    for n in range(1,M+1):
        q=np.arange(n+1);k=n-q
        h=g*np.sqrt((q[:-1]+1)*k[:-1]*(N-k[:-1]+1))
        H=np.diag(h,1)+np.diag(h,-1)
        A=-1j*H-.5*np.diag(kappa*q+gamma_i*k)
        J=np.zeros((n,n+1),complex)
        for i in range(1,n+1):J[i-1,i]=np.sqrt(kappa*i)
        B=J.conj().T@E@J
        E=solve_continuous_lyapunov(A.conj().T,-B)
        max_res=max(max_res,near(A.conj().T@E+E@A,-B,'Cavity effect equation',1e-8))
        E=(E+E.conj().T)/2
        ev=np.linalg.eigvalsh(E)
        require(ev.min()>-1e-10 and ev.max()<1+1e-10,'Effect positivity and contraction')
        probs.append(float(E[0,0].real))
    return probs,max_res


def full_cavity_ode(N,m,g,kappa,gamma_i):
    # Explicit individual-spin basis, not a symmetric-spin representation.
    basis=[(s,q) for s in range(2**N) for q in range(m+1) if s.bit_count()+q<=m]
    lookup={b:i for i,b in enumerate(basis)};d=len(basis)
    a=np.zeros((d,d),complex);H=np.zeros((d,d),complex)
    ns=np.zeros(d)
    for column,(s,q) in enumerate(basis):
        ns[column]=s.bit_count()
        if q:a[lookup[s,q-1],column]=np.sqrt(q)
        for j in range(N):
            if (s>>j)&1:
                row=lookup[s^(1<<j),q+1]
                H[row,column]+=g*np.sqrt(q+1)
                H[column,row]+=g*np.sqrt(q+1)
    L=np.sqrt(kappa)*a
    damping=L.conj().T@L+gamma_i*np.diag(ns)
    v=np.array([float(q==0 and s.bit_count()==m) for s,q in basis],complex)
    v/=np.linalg.norm(v)
    rho=np.outer(v,v.conj())
    def rhs(t,y):
        x=y.reshape(d,d)
        return (-1j*(H@x-x@H)+L@x@L.conj().T-.5*(damping@x+x@damping)).ravel()
    slow=min(g*g*N/kappa,kappa)
    T=100/max(.05,slow)
    sol=solve_ivp(rhs,(0,T),rho.ravel(),method='DOP853',rtol=3e-10,atol=2e-12)
    require(sol.success,sol.message)
    out=sol.y[:,-1].reshape(d,d)
    return float(out[lookup[0,0],lookup[0,0]].real),float(np.trace(out).real),d


def test_cavity_checks():
    one=[]
    for N in [1,4,16]:
        for kappa in [1.,4.,20.]:
            g=1.;gi=.1;G2=N*g*g
            formula=kappa/(kappa+gi)*4*G2/(4*G2+kappa*gi)
            exact,_=cavity_probabilities(N,1,g,kappa,gi)
            near(exact[0],formula,'Exact one-excitation cavity collection')
            one.append(dict(N=N,kappa=kappa,formula=formula,lyapunov=exact[0]))
    physical=[]
    for N,m,kappa in [(2,1,3.),(2,2,4.),(3,2,5.)]:
        p,trace,d=full_cavity_ode(N,m,1.,kappa,.1)
        exact,_=cavity_probabilities(N,m,1.,kappa,.1)
        near(p,exact[-1],'Full independent-spin cavity ODE',3e-8)
        near(trace,p,'Vanishing transient',3e-8)
        physical.append(dict(N=N,m=m,kappa=kappa,hilbert_dimension=d,full_ODE=p,effect_recursion=exact[-1]))
    finite=[]
    for R in [1.,3.,10.,30.,100.]:
        N=16;m=4;g=1.;gi=.01;kappa=R*g*np.sqrt(N);r=gi*kappa/(4*g*g)
        p,res=cavity_probabilities(N,m,g,kappa,gi)
        finite.append(dict(N=N,m=m,g=1.,gamma_i=.01,R=R,kappa=kappa,
                           single_emitter_cooperativity=1/r,
                           eliminated_all_collected_probability=success(N,m,r),
                           full_cavity_all_collected_probability=p[-1],
                           effect_residual=res))
    # Exact no-independent-decay control: every excitation exits useful port.
    for N,M,kappa in [(4,4,1.),(8,5,20.)]:
        p,_=cavity_probabilities(N,M,1.,kappa,0.)
        near(p,np.ones(M),'Lossless useful cavity channel',1e-9)
    return dict(cases=len(one)+len(physical)+len(finite)+2,one_excitation=one,
                independent_physical_ODE=physical,finite_bandwidth_table=finite,
                scope='Output photon-number success only. No temporal-mode fidelity or uniform all-code elimination claim is inferred from this check.')


def test_rate_scaling():
    fixed_C=[]
    for N,M in [(1000,200),(1000000,10000)]:
        for C in [1.,10.,100.]:
            fixed_C.append(dict(N=N,M=M,C=C,all_collected_probability=success(N,M,1/C),
                                exponent_first_order=M/(C*N)))
    micro=[]
    for N in [1000,1000000,1000000000]:
        M=int(round(N**(2/3)));R=10.;g_over_gi=100.
        r=R*np.sqrt(N)/(4*g_over_gi)
        micro.append(dict(N=N,M=M,R=R,g_over_gamma_i=g_over_gi,r=r,
                          eliminated_probability=success(N,M,r),
                          leading_negative_log_probability=r*M/N,
                          label='Formal effective-rate consistency test, not a proved large-code limit of the full cavity.'))
    fixed=[]
    for N in [1000,1000000,1000000000]:
        M=int(round(N**(2/3)))
        p=success(N,M,1.)
        near(p,1-M/(N+1),'Exactly telescoping C=1')
        fixed.append(dict(N=N,M=M,C=1.,probability=p))
    # Independent propagation loss acts after emission; it does not enjoy collective enhancement.
    external=[dict(eta=eta,M=200,all_photon_transmission=eta**200) for eta in [.99,.999,.9999]]
    return dict(cases=len(fixed_C)+len(micro)+len(fixed)+len(external),fixed_cooperativity=fixed_C,
                fixed_microscopic_ratios=micro,telescoping_control=fixed,propagation_control=external,
                scope='No hardware parameter set or changed source-control design is asserted experimentally available.')


def test_unconditional_code_structure():
    # Independent finite isometry example: success amplitudes already include
    # any source and extraction loss; other Kraus outcomes lower number.
    M=5;d=M+1;amplitude=np.array([1.,.99,.96,.94,.88,.91])
    K0=np.diag(amplitude)
    Kraus=[K0]
    for m in range(1,d):
        K=np.zeros((d,d));K[0,m]=np.sqrt(1-amplitude[m]**2);Kraus.append(K)
    near(sum(K.conj().T@K for K in Kraus),np.eye(d),'Kraus completeness')
    floor=float(min(amplitude**2));sample_min=1.
    for _ in range(40):
        X=RNG.normal(size=(d,d))+1j*RNG.normal(size=(d,d));rho=X@X.conj().T;rho/=np.trace(rho)
        Fe=float(sum(abs(np.trace(rho@K))**2 for K in Kraus))
        require(Fe>=floor-1e-13,'Reference-entangled fidelity lower bound')
        sample_min=min(sample_min,Fe)
    q=int(np.argmin(amplitude))
    rho=np.diag(np.arange(d)==q)
    near(sum(abs(np.trace(rho@K))**2 for K in Kraus),floor,'Worst number state saturation')
    # Lossless oscillator + independent oscillator loss is a common temporal mode
    # with binomial attenuation, not a nonlinear Dicke pulse family.
    oscillator=[]
    for m in [1,2,5]:
        col=2.;ind=.3
        p=(col/(col+ind))**m
        beta=col+ind
        ordered_product=np.prod([4*(k*col)*(k*beta)/(k*(col+ind)+k*beta)**2 for k in range(1,m+1)])
        near(ordered_product,p,'Linear ladder reference')
        oscillator.append(dict(m=m,all_collected_probability=p,common_pulse_rate=beta))
    return dict(cases=42+len(oscillator),minimum_fidelity=floor,minimum_sampled_fidelity=sample_min,
                oscillator=oscillator,
                scope='Structural test with arbitrary lowering Kraus operators. It is not a full many-photon field simulation.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('exact_source_branch',test_exact_branch_and_pulse),('physical_atomic_space',test_full_atomic_space),
                    ('finite_cavity',test_cavity_checks),('rate_family_consistency',test_rate_scaling),
                    ('unconditional_code',test_unconditional_code_structure)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-03',seed=SEED,groups=groups,group_count=len(groups),
                cases=sum(v['cases'] for v in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                qualification='Author-side checks of an assumption audit; inherited ideal theorem remains separate and no uniform microscopic realization is claimed.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
