#!/usr/bin/env python3
"""Independent proof diagnostics and a two-temporal-mode explanation.

The source, code, and linear one-mode task are unchanged. New derivations are in
RESULT.md. No preceding scientific module is imported. Finite tests and numerical
optimization do not replace the analytic converse or certify novelty.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
from functools import lru_cache
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.optimize import minimize
from scipy.special import roots_legendre, gammaln
from scipy.stats import binom, poisson
import mpmath as mp

SEED=2026100204
RNG=np.random.default_rng(SEED)


def need(ok: bool,msg: str)->None:
    if not ok:raise AssertionError(msg)


def near(x,y,msg,tol=3e-10):
    e=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    need(np.isfinite(e) and e<=tol,f'{msg}: {e} > {tol}')
    return e


def validate_nm(N,m):
    if not isinstance(N,int) or not isinstance(m,int) or not 0<=m<=N:
        raise ValueError('Integer 0 <= m <= N is required.')


def u_number(N,m):
    validate_nm(N,m)
    return -np.log1p(-max(0,m-1)/N)


def u_receiver(N,M):
    validate_nm(N,M)
    if M<=1:return 0.
    return -np.log1p(-(.75*M-1)/N)


def entropy(N,m):
    validate_nm(N,m)
    if m<=1:return 0.
    with mp.workdps(65):
        n=mp.mpf(N);k=mp.mpf(m);a=(k-1)/n;b=1-a
        value=k*(-b/a*mp.log(b)-1)-(mp.loggamma(n+1)-mp.loggamma(n-k+1)-k*mp.log(n))
        return float(value)


def entropy_bound(N,M):
    if M<=1:return 0.
    return M*(M-1)/(12*N*N*(1-(M-1)/N)**2)


def mode_y(y,u):
    """f(t)=sqrt(y)*h(y), y=exp(-t); inner products are integrals of h over dy."""
    b=np.exp(-u);den=b+(1-b)*y
    h=np.sqrt(b)/den
    tangent=np.sqrt(12)*h*(-.5+b*(1-y)/den)
    return h,tangent


def mode_t(t,u):
    y=np.exp(-t);h,g=mode_y(y,u)
    return np.sqrt(y)*h,np.sqrt(y)*g


def geometry(z):
    """Exact overlap, tangent coefficient, and two-mode projected weight."""
    with mp.workdps(65):
        x=mp.mpf(float(z))
        if x==0:return 1.,0.,1.
        I=x/(2*mp.sinh(x/2))
        Ip=(1-(x/2)/mp.tanh(x/2))/(2*mp.sinh(x/2))
        B=-mp.sqrt(12)*Ip
        p=I*I+B*B
        return float(I),float(B),float(p)


def two_mode_guarantee(N,M):
    """Finite uniform guarantee from explicitly bounded second derivative and inherited KL."""
    if M<=1:return dict(retention_lower=1.,isometry_norm_error=0.,source_norm_bound=0.,curvature_residual=0.)
    us=u_receiver(N,M)
    zmax=max(us,abs(u_number(N,M)-us))
    r=min(1.,7*zmax**4/960)
    B=entropy_bound(N,M)
    source=np.sqrt(2*(-np.expm1(-B/2)))
    outside=np.sqrt(min(1.,M*r))
    product=np.sqrt(2*min(1.,M*r))
    return dict(retention_lower=max(0.,1-(source+outside)**2),
                isometry_norm_error=min(2.,source+product),source_norm_bound=float(source),
                curvature_residual=float(r),max_mode_distance=zmax)


def continuum_amplitudes(N,m,M,cap=8,T=38.,rtol=2e-11,max_step=.1,oscillator=False):
    """Exact projected amplitudes for k<=cap photons in g, m-k in f.

    The j-emitted stage is scaled by sqrt(binomial(m,j)); its terminal scale is
    one. This prevents loss of exponentially small early amplitudes. No final
    count is discarded from the source evolution: upper k rows do not feed down.
    A sum over the reported terminal outcomes is a lower bound on retention.
    """
    validate_nm(N,m);validate_nm(N,M)
    if not m:return np.array([1.])
    cap=min(m,int(cap));us=u_receiver(N,M)
    shape=(m+1,cap+1);j,k=np.indices(shape)
    remaining=np.arange(m,-1,-1)
    rates=remaining.astype(float) if oscillator else remaining*(1-(remaining-1)/N)
    steps=np.arange(1,m+1)
    feed=np.r_[0,np.sqrt(rates[:-1]*(m-steps+1)/steps)]
    first=np.sqrt(np.maximum(j-k,0))*feed[:,None]
    second=np.sqrt(k)*feed[:,None]
    initial=np.zeros(shape);initial[0,0]=1.
    def rhs(t,flat):
        x=flat.reshape(shape);f,g=mode_t(t,us)
        out=-.5*rates[:,None]*x
        out[1:]+=first[1:]*f*x[:-1]
        out[1:,1:]+=second[1:,1:]*g*x[:-1,:-1]
        return out.ravel()
    sol=solve_ivp(rhs,(0,T),initial.ravel(),method='DOP853',rtol=rtol,atol=2e-15,max_step=max_step)
    need(sol.success,sol.message)
    out=sol.y[:,-1].reshape(shape)[m]
    need(float(np.sum(out*out))<=1+2e-8,'Projected probability exceeds one; unsafe integration')
    return out


def one_mode_overlap(N,m,M,T=38.,rtol=2e-11):
    """Independent scalar cascade for the k=0 comparison."""
    if m==0:return 1.
    us=u_receiver(N,M);k=np.arange(m,-1,-1);ell=k*(1-(k-1)/N)
    couplings=np.sqrt(k[:-1]*ell[:-1])
    def rhs(t,x):
        f,_=mode_t(t,us)
        out=-ell*x/2;out[1:]+=couplings*f*x[:-1]
        return out
    x=np.zeros(m+1);x[0]=1
    sol=solve_ivp(rhs,(0,T),x,method='DOP853',atol=2e-15,rtol=rtol,max_step=.1)
    need(sol.success,sol.message)
    return sol.y[-1,-1]


def ordered_two_photon_amplitudes(N,M):
    """Direct double integral in y coordinates, independent of the cascade ODE."""
    us=u_receiver(N,M);out=[];C=np.sqrt(1-1/N)
    for k in range(3):
        def integrand(y):
            f,g=mode_y(y,us)
            def inner(v):
                h,l=mode_y(y*v,us)
                if k==0:return 2*f*h
                if k==1:return np.sqrt(2)*(f*l+g*h)
                return 2*g*l
            return C*y**(1-1/N)*quad(inner,0,1,epsabs=2e-12,epsrel=2e-12)[0]
        out.append(quad(integrand,0,1,epsabs=2e-11,epsrel=2e-11)[0])
    return np.array(out)


def test_proof_ingredients():
    rows=[];max_error=0.
    for u in [0.,.15,.6,-.4]:
        f2=quad(lambda y:mode_y(y,u)[0]**2,0,1,epsabs=2e-12)[0]
        g2=quad(lambda y:mode_y(y,u)[1]**2,0,1,epsabs=2e-12)[0]
        fg=quad(lambda y:np.prod(mode_y(y,u)),0,1,epsabs=2e-12)[0]
        max_error=max(max_error,near([f2,g2,fg],[1,1,0],'Orthonormal f and tangent mode'))
        for z in [-.3,-.01,0.,.2]:
            I,B,p=geometry(z)
            i=quad(lambda y:mode_y(y,u)[0]*mode_y(y,u+z)[0],0,1,epsabs=2e-12)[0]
            b=quad(lambda y:mode_y(y,u)[1]*mode_y(y,u+z)[0],0,1,epsabs=2e-12)[0]
            max_error=max(max_error,near([i,b],[I,B],'Overlap kernel and its derivative'))
            need(1-p<=7*z**4/960+1e-14,'Global Taylor residual bound')
    for N,m in [(5,2),(16,3),(40,10),(1000,300),(10**6,30000)]:
        # Ordered waiting-time density normalization, with exact finite product.
        ell=[mp.mpf(k)*(1-mp.mpf(k-1)/N) for k in range(1,m+1)] if m<500 else None
        if ell is not None:
            with mp.workdps(45):
                coeff=mp.factorial(m)*mp.fprod([1-mp.mpf(j)/N for j in range(m)])
                near(float(coeff/mp.fprod(ell)),1.,'Labeled density normalization')
        D=entropy(N,m);B=entropy_bound(N,m)
        need(-1e-14<=D<=B+1e-12,'Uniform entropy bound')
        rows.append(dict(N=N,m=m,exact_KL=D,upper_KL=B))
    # Direct expectation of log(Q/P) for m=2 uses a smooth ordered double integral.
    for N in [5,20]:
        m=2;a=1/N;b=1-a;u=-np.log(b);C2=1-1/N
        def outer(y):
            h=mode_y(y,u)[0]
            def inner(v):
                l=mode_y(y*v,u)[0]
                log_ratio=2*np.log(h)+2*np.log(l)-np.log(C2)+2*np.log(y)/N
                return 2*y*h*h*l*l*log_ratio
            return quad(inner,0,1,epsabs=2e-12)[0]
        d=quad(outer,0,1,epsabs=2e-11,epsrel=2e-11)[0]
        max_error=max(max_error,near(d,entropy(N,m),'Independent two-time KL integral',5e-10))
    return dict(cases=27,maximum_integral_error=max_error,entropy_rows=rows,
                scope='Finite checks of stated identities; the all-N proof is analytical.')


def test_all_mode_converse():
    rows=[]
    nodes,w=roots_legendre(64);y=(nodes+1)/2;weights=w/2
    for N,M in [(50,12),(128,32),(1000,100)]:
        modes=np.array([mode_y(y,u_number(N,m))[0]*np.sqrt(weights) for m in range(1,M+1)])
        near(np.sum(modes*modes,axis=1),1.,'Quadrature mode normalization')
        mvals=np.arange(1,M+1);trial=mode_y(y,u_receiver(N,M))[0]*np.sqrt(weights)
        t0=float(max(-2*mvals*np.log(modes@trial)))
        x0=np.r_[trial,t0*1.001+1e-8]
        def constraint(z):return np.r_[1-z[:-1]@z[:-1],modes@z[:-1]-np.exp(-z[-1]/(2*mvals))]
        def jac(z):
            J=np.zeros((M+1,len(z)));J[0,:-1]=-2*z[:-1]
            J[1:,:-1]=modes;J[1:,-1]=np.exp(-z[-1]/(2*mvals))/(2*mvals)
            return J
        grad=np.r_[np.zeros(64),1.]
        res=minimize(lambda z:z[-1],x0,jac=lambda z:grad,method='SLSQP',
                     constraints={'type':'ineq','fun':constraint,'jac':jac},
                     bounds=[(None,None)]*64+[(0,None)],options={'ftol':2e-12,'maxiter':400})
        need(res.success,res.message)
        need(min(constraint(res.x))>=-2e-9,'Finite waveform optimization infeasible')
        F=np.exp(-res.fun);q=max(1,M//4)
        I=geometry(u_number(N,M)-u_number(N,q))[0]
        lhs=np.arccos(I)
        rhs=np.arccos(F**(1/(2*q)))+np.arccos(F**(1/(2*M)))
        need(lhs<=rhs+3e-8,'Two-hypothesis arbitrary-waveform converse')
        need(F+2e-10>=np.exp(-t0),'Optimized waveform worse than supplied feasible trial')
        rows.append(dict(N=N,M=M,trial_product_fidelity=float(np.exp(-t0)),
                         finite_grid_product_optimum=float(F),photon_pair_used=[q,M],
                         angle_slack=float(rhs-lhs),minimum_constraint=float(min(constraint(res.x))),
                         grid_dimension=64))
    return dict(cases=len(rows),rows=rows,
                scope='Finite-dimensional product-state optimization is a diagnostic, not the exact Dicke optimum or proof of the infinite-dimensional converse.')


def test_critical_two_mode_law():
    rows=[]
    for c in [1.,2.,3.]:
        for root in [10,100,1000]:
            N=root**3;M=int(c*root**2);us=u_receiver(N,M)
            bound=two_mode_guarantee(N,M)
            for x in [.25,.75,1.]:
                m=max(1,round(x*M));I,B,p=geometry(u_number(N,m)-us)
                prob=B*B/p
                lam=c**3*x*(x-.75)**2/12
                n=np.arange(41);pb=binom.pmf(n,m,prob);pp=poisson.pmf(n,lam)
                tv=.5*(np.sum(abs(pb-pp))+binom.sf(40,m,prob)+poisson.sf(40,lam))
                rows.append(dict(N=N,M=M,m=m,c=c,x=x,product_photons_in_tangent_mean=float(m*prob),
                                 limiting_poisson_parameter=lam,binomial_Poisson_TV=float(tv),
                                 product_no_tangent_probability=float((1-prob)**m),
                                 guaranteed_all_code_two_mode_retention=bound['retention_lower'],
                                 all_code_isometry_norm_error_bound=bound['isometry_norm_error']))
            if root==1000:
                need(rows[-1]['binomial_Poisson_TV']<.003,'Slow limiting count convergence')
                need(bound['retention_lower']>.999,'Two-mode uniform fidelity bound')
    # The maximization yielding 1/192 is checked algebraically at all stationary points.
    for x in [0.,.25,.75,1.]:
        need(x*(x-.75)**2<=1/16+1e-14,'Minimax cubic polynomial')
    return dict(cases=len(rows),rows=rows,
                caution='Poisson convergence is in distribution/TV, not by itself convergence of the unbounded exact finite-N photon-count mean. These rows evaluate the controlled product approximants and separate rigorous approximation bounds.')


def test_exact_output():
    integral_rows=[]
    for N,M in [(8,4),(20,10)]:
        ode=continuum_amplitudes(N,2,M,cap=2,T=40.)
        direct=ordered_two_photon_amplitudes(N,M)
        err=near(ode,direct,'ODE versus independent ordered-wavefunction integral',3e-9)
        integral_rows.append(dict(N=N,M=M,error=err,amplitudes=ode.tolist()))
    # In the oscillator comparator the input already has one exact mode, so all
    # output coefficients equal a multinomial projection of that known product.
    for m in [1,2,5,12]:
        N=80;M=20;z=-u_receiver(N,M);I,B,p=geometry(z)
        expected=np.array([math.sqrt(math.comb(m,k))*I**(m-k)*B**k for k in range(m+1)])
        out=continuum_amplitudes(N,m,M,cap=m,oscillator=True,T=40.)
        near(out,expected,'Oscillator full two-mode projection',3e-8)
    rows=[]
    for N,M,m,cap in [(128,50,12,8),(128,50,50,8),(1000,300,75,8),(1000,300,300,8)]:
        A=continuum_amplitudes(N,m,M,cap=cap)
        p=A*A;single=one_mode_overlap(N,m,M)
        # Analytic Cauchy-Schwarz tail correction: |g|^2 <= 3 |f|^2.
        T=38.; us=u_receiver(N,M); amin=1-(m-1)/N
        Sf=np.exp(-T)/(np.exp(-us)+(1-np.exp(-us))*np.exp(-T))
        tail=np.sqrt(min(1.,m*np.exp(-amin*T))*np.minimum(1.,(m+2*np.arange(len(A)))*Sf))
        lower=np.maximum(0.,np.abs(A)-tail)**2
        near(A[0],single,'Separate one-mode recursion',4e-8)
        good=sum(lower)
        fraction=float(np.dot(m-np.arange(len(p)),lower)/m)
        rows.append(dict(N=N,M=M,m=m,max_tangent_count_evaluated=cap,
                         all_photons_in_main_mode=float(p[0]),
                         probability_all_photons_in_two_modes_lower=float(good),
                         main_mode_mean_photon_fraction_lower=fraction,
                         resolved_probabilities=p.tolist(),
                         maximum_amplitude_late_time_bound=float(max(tail))))
    refined=continuum_amplitudes(1000,300,300,cap=8,T=44.,rtol=3e-12,max_step=.05)
    reference=np.sqrt(np.array(rows[-1]['resolved_probabilities']))
    # Squared amplitudes avoid an irrelevant sign convention in this refinement.
    err=near(refined*refined,reference*reference,'Time and tolerance refinement',2e-8)
    return dict(cases=len(integral_rows)+4+len(rows)+1,independent_integrals=integral_rows,
                finite_Dicke_rows=rows,refinement_probability_error=err,
                scope='No trajectory or photon-count postselection. The count cutoff produces a conservative subevent sum, not a renormalized distribution. These numbers are numerical rather than interval-certified bounds.')


def test_reference_safe_approximation():
    N=80;M=12;us=u_receiver(N,M);errors=[]
    for m in range(M+1):
        if m==0:errors.append(0.);continue
        A=continuum_amplitudes(N,m,M,cap=m,T=38.)
        I,B,p=geometry(u_number(N,m)-us)
        normalized=np.array([math.sqrt(math.comb(m,k))*(I/np.sqrt(p))**(m-k)*(B/np.sqrt(p))**k for k in range(m+1)])
        inner=float(normalized@A)
        error2=max(0.,2-2*inner)
        D=entropy(N,m)
        source=np.sqrt(2*(-np.expm1(-D/2)))
        projection=np.sqrt(2*(1-p**(m/2)))
        need(np.sqrt(error2)<=source+projection+2e-8,'Exact code-state approximation inequality')
        errors.append(error2)
    maxerror=np.sqrt(max(errors));bound=two_mode_guarantee(N,M)['isometry_norm_error']
    need(maxerror<=bound+2e-8,'Uniform isometry bound')
    # Orthogonal number sectors also remain orthogonal when coefficients are vectors in a reference.
    for _ in range(16):
        coefficients=RNG.normal(size=(M+1,3))+1j*RNG.normal(size=(M+1,3))
        coefficients/=np.linalg.norm(coefficients)
        squared_error=float(np.sum(abs(coefficients)**2*np.array(errors)[:,None]))
        need(squared_error<=max(errors)+1e-13,'No input-dimension factor on reference-entangled code')
    return dict(cases=M+1+16,N=N,M=M,maximum_exact_isometry_error=maxerror,
                analytic_uniform_isometry_error=bound,
                explanation='The exact error norm is evaluated through continuum overlap amplitudes; reference-safe extension follows from orthogonality of distinct total-photon-number sectors.')


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('proof_identity_audit',test_proof_ingredients),('arbitrary_waveform_diagnostic',test_all_mode_converse),
                    ('critical_error_mechanism',test_critical_two_mode_law),('full_output_amplitudes',test_exact_output),
                    ('reference_safe_encoding',test_reference_safe_approximation)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-02',seed=SEED,group_count=len(groups),cases=sum(g['cases'] for g in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),
                groups=groups,scope='Author-side independent formulations and new limiting-mode consequences. No external peer review, exhaustive priority certificate, or physical device observation.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
