#!/usr/bin/env python3
"""Two-sector consequence of the preserved Dicke common-mode theorem.

This is a scope audit of the existing theorem, not a new source or receiver.
The only new numerics are trial-waveform witnesses for a two-dimensional code.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from pathlib import Path
import platform
import numpy as np
import scipy
import mpmath as mp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

mp.mp.dps=70


def require(ok, message):
    if not ok: raise AssertionError(message)


def near(a,b,message,tol=3e-10):
    e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    require(e<=tol,f'{message}: {e} > {tol}')
    return e


def log_overlap(a,b):
    z=np.log1p(-a)-np.log1p(-b)
    if abs(z)<1e-3:
        return float(-z*z/24+z**4/2880-z**6/181440+z**8/9676800)
    return float(np.log(abs(z)/(2*np.sinh(abs(z)/2))))


def angle_from_log(logcos):
    v=min(0.,float(logcos))
    return float(np.arctan2(np.sqrt(-np.expm1(2*v)),np.exp(v)))


@lru_cache(None)
def entropy(N,m):
    if m<=1:return 0.
    n=mp.mpf(N); a=mp.mpf(m-1)/n;b=1-a
    val=m*(-b/a*mp.log(b)-1)-(mp.loggamma(n+1)-mp.loggamma(n-m+1)-m*mp.log(n))
    require(val>=-mp.mpf('1e-50'),'Negative relative entropy')
    return float(max(val,0))


def universal_upper(N,M):
    q=max(1,M//4)
    separation=angle_from_log(log_overlap((q-1)/N,(M-1)/N))
    def radius(F,m):
        total=angle_from_log(np.log(F)/2)+angle_from_log(-entropy(N,m)/2)
        if total>=np.pi/2:return np.pi/2
        return angle_from_log(np.log(np.cos(total))/m)
    fn=lambda F:radius(F,q)+radius(F,M)-separation
    if fn(1)>=0:return 1.
    return float(brentq(fn,1e-14,1.,xtol=2e-13))


def analytic_trial_lower(N,M):
    a=(.75*M-1)/N
    candidates=[]
    for m in [max(1,M//4),M]:
        theta=angle_from_log(m*log_overlap((m-1)/N,a))+angle_from_log(-entropy(N,m)/2)
        candidates.append(float(max(0,np.cos(theta))**2) if theta<np.pi/2 else 0.)
    return min(candidates)


@lru_cache(None)
def exact_amplitude(N,m,a,T=48.,rtol=3e-11):
    if m==0:return 1.
    if not (1<=m<=N and 0<=a<1):raise ValueError('Invalid model parameters')
    k=np.arange(m,-1,-1,dtype=float)
    rates=k*(1-(k-1)/N); rates[-1]=0
    coupling=np.sqrt(k[:-1]*rates[:-1])
    def rhs(t,y):
        f=np.sqrt(1-a)*np.exp(-t/2)/(1-a+a*np.exp(-t))
        dy=-rates*y/2
        dy[1:]+=coupling*f*y[:-1]
        return dy
    initial=np.zeros(m+1);initial[0]=1
    sol=solve_ivp(rhs,(0,T),initial,method='DOP853',rtol=rtol,atol=3e-15,max_step=.18)
    require(sol.success,sol.message)
    return float(sol.y[-1,-1])


def group_asymptotic_geometry():
    # A general fixed ratio is a check on the two-point minimax geometry, not an
    # additional physical source theorem. r=1/4 reproduces the inherited constant.
    rows=[]
    for r in [.01,.04,.1,.25,.5,.81]:
        b=1-np.sqrt(r)+r
        objective=lambda x:max(r*(x-r)**2,(1-x)**2)
        numerical=minimize_scalar(objective,bounds=(r,1),method='bounded',options={'xatol':1e-14})
        formula=r*(1-np.sqrt(r))**2
        near(objective(b),formula,'Analytic equal-radius optimum',1e-13)
        near(numerical.fun,formula,'Independent one-dimensional minimax',1e-8)
        rows.append(dict(lower_number_fraction=r,compromise_fraction=float(b),weighted_radius_squared=formula))
    near(.25*(1-np.sqrt(.25))**2/12,1/192,'Original exponent coefficient',1e-14)
    return dict(cases=len(rows)+1,rows=rows)


def group_finite_pair():
    rows=[]
    for N,M in [(100,24),(1000,300)]:
        q=M//4
        root=brentq(lambda a:exact_amplitude(N,q,float(a))**2-exact_amplitude(N,M,float(a))**2,
                    (q-1)/N,(M-1)/N,xtol=1e-10)
        Aq=exact_amplitude(N,q,root);AM=exact_amplitude(N,M,root)
        fidelity=min(Aq*Aq,AM*AM)
        upper=universal_upper(N,M)
        near(Aq*Aq,AM*AM,'Balanced two-state trial',1e-9)
        require(fidelity<=upper+1e-10,'Trial exceeds all-waveform upper bound')
        a0=(.75*M-1)/N
        ref=[exact_amplitude(N,q,a0)**2,exact_amplitude(N,M,a0)**2]
        if N==1000:
            near(ref,[.8257267086527,.7865187451234],'Preserved full-cascade values',2e-9)
        refined=[exact_amplitude(N,q,root,60.,2e-12),exact_amplitude(N,M,root,60.,2e-12)]
        err=near(refined,[Aq,AM],'Horizon and tolerance refinement',2e-9)
        late_true=M*np.exp(-(1-(M-1)/N)*48)
        late_target=M*np.exp(-48)/(1-root+root*np.exp(-48))
        tail_amp=np.sqrt(late_true*late_target)
        rows.append(dict(N=N,M=M,lower_number=q,trial_mode_a=float(root),trial_number_fidelities=[Aq*Aq,AM*AM],
                         trial_worst_entanglement_fidelity=fidelity,all_waveforms_upper=upper,
                         maximally_reference_entangled_trial_fidelity=(Aq+AM)**2/4,
                         original_trial_fidelities=ref,refinement_amplitude_error=err,
                         analytic_fidelity_tail_allowance=float(2*tail_amp+tail_amp**2),
                         scope='Constructive numerical trial, not an exact finite-N optimum or interval enclosure.'))
    return dict(cases=len(rows),rows=rows)


def group_joint_limit():
    rows=[]
    for c in [1,2,3]:
        for N,base in [(10**3,100),(10**6,10000),(10**9,1000000)]:
            M=c*base; lo=analytic_trial_lower(N,M);hi=universal_upper(N,M)
            require(lo<=hi+1e-10,'Two-sector analytic bracket reversed')
            rows.append(dict(N=N,M=M,q=M//4,lower=lo,upper=hi,target=float(np.exp(-c**3/192))))
        require(abs(rows[-1]['lower']-rows[-1]['target'])<.002 and abs(rows[-1]['upper']-rows[-1]['target'])<.002,
                'Critical two-sector bracket failed to approach inherited limit')
    # Vacuum plus a known number is not the same hard encoding.
    vacuum=[]
    for N,m in [(100,10),(1000,300),(1000000,10000)]:
        vacuum.append(dict(N=N,m=m,known_number_lower=float(np.exp(-entropy(N,m)))))
    return dict(cases=len(rows)+len(vacuum),critical_sequences=rows,vacuum_plus_number_controls=vacuum)


def group_reference_channel():
    # Two-mode product approximants supply an exactly tractable channel control.
    # These are not substituted for a full Dicke output field simulation.
    rows=[]
    rng=np.random.default_rng(2026100307)
    for q,M in [(1,4),(2,8),(3,12)]:
        amp=[.9,.85]
        K=[np.zeros((M+1,2),complex) for _ in range(M+1)]
        for j,m in enumerate([q,M]):
            K[0][m,j]=amp[j]
            p=rng.dirichlet(np.ones(m))*(1-amp[j]**2)
            for loss,w in enumerate(p,1): K[loss][m-loss,j]=np.sqrt(w)
        near(sum(k.conj().T@k for k in K),np.eye(2),'Trace preservation')
        T=np.zeros((M+1,2),complex);T[q,0]=T[M,1]=1
        effective=[T.conj().T@k for k in K]
        rho=np.eye(2)/2
        Fe=sum(abs(np.trace(rho@k))**2 for k in effective)
        near(Fe,(sum(amp)/2)**2,'Maximally entangled reference input')
        for _ in range(8):
            X=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));r=X@X.conj().T;r/=np.trace(r)
            measured=sum(abs(np.trace(r@k))**2 for k in effective)
            require(measured>=min(amp)**2-1e-12,'Worst-input lower bound')
        rho=np.diag([0.,1.]);worst=sum(abs(np.trace(rho@k))**2 for k in effective)
        near(worst,min(amp)**2,'Number input saturates bound')
        rows.append(dict(q=q,M=M,entangled_input_fidelity=float(Fe),worst_fidelity=float(worst)))
    return dict(cases=len(rows),rows=rows,scope='Structural channel example; not a new optical simulation.')


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('two_point_geometry',group_asymptotic_geometry),('finite_pair_code',group_finite_pair),
                    ('joint_limit_and_encoding_control',group_joint_limit),('reference_channel_structure',group_reference_channel)]:
        groups[name]=fn();print('PASS',name,flush=True)
    out=dict(status='PASS',date='2026-10-03',group_count=len(groups),cases=sum(g['cases'] for g in groups.values()),groups=groups,
             environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),
             scope='Consequences and finite checks of the existing source theorem; no new code-capacity or hardware claim.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)

if __name__=='__main__':main()
