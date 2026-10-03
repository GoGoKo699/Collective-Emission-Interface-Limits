#!/usr/bin/env python3
"""Operational receiver checks for the existing ideal Dicke emission result.

This script independently implements finite-dimensional passive optics, a
regularized tunable capture cavity, and cascaded open-system dynamics. It does
not import prior scientific code or independently certify the prior asymptotic
proof. See RESULT.md for the receiver class and the limits of the claims.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from functools import lru_cache
import itertools
import json
import math
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm

SEED = 2026100203
RNG = np.random.default_rng(SEED)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def near(a, b, label, tol=2e-9):
    err = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    require(np.isfinite(err) and err <= tol, f'{label}: {err:g} exceeds {tol:g}')
    return err


def pulse(t, a):
    t = np.asarray(t)
    return np.sqrt(1-a)*np.exp(-t/2)/(1-a+a*np.exp(-t))


def cumulative(t, a):
    # Stable near t=0, where the regularization is most important.
    return (1-a)*(-np.expm1(-np.asarray(t)))/(1-a+a*np.exp(-np.asarray(t)))


def receiver_rate(t, a, epsilon):
    require(0 <= a < 1 and epsilon > 0, 'Valid pulse and positive regularization required')
    return pulse(t, a)**2/(epsilon+cumulative(t, a))


def rates(N, m, harmonic=False):
    require(0 <= m <= N, 'Need 0 <= m <= N')
    k = np.arange(m, -1, -1)
    ell = k.astype(float) if harmonic else k*(1-(k-1)/N)
    ell[-1] = 0.
    return ell


@lru_cache(None)
def direct_overlap(N, m, a, T=32., harmonic=False):
    """Ordered-time overlap recursion, independent implementation of baseline formula."""
    if not m:
        return 1.
    ell = rates(N, m, harmonic)
    coupling = np.sqrt(np.arange(m, 0, -1)*ell[:-1])
    def rhs(t, x):
        dx = -.5*ell*x
        dx[1:] += pulse(t, a)*coupling*x[:-1]
        return dx
    y = np.zeros(m+1); y[0] = 1
    s = solve_ivp(rhs, (0., T), y, method='DOP853', rtol=3e-11, atol=3e-14, max_step=.12)
    require(s.success, s.message)
    return float(s.y[-1, -1])


@lru_cache(None)
def capture_amplitude(N, m, a, epsilon, T=32., harmonic=False):
    """All-excitations retained amplitude of a cascaded Dicke source and linear cavity.

    The target event has the full input photon number in the cavity. A radiated
    photon makes that event impossible, so its unconditional probability equals
    the squared no-output amplitude. No experiment is postselected here.
    """
    ell = rates(N, m, harmonic)
    j = np.arange(m+1)
    feeding = np.sqrt(j[1:]*ell[:-1])
    def rhs(t, v):
        kap = receiver_rate(t, a, epsilon)
        dv = -.5*(ell+kap*j)*v
        dv[1:] += np.sqrt(kap)*feeding*v[:-1]
        return dv
    v = np.zeros(m+1);v[0] = 1
    s = solve_ivp(rhs, (0., T), v, method='DOP853', rtol=3e-11, atol=3e-14, max_step=.12)
    require(s.success, s.message)
    return float(s.y[-1, -1])


def reduced_last_mode(psi, states, M):
    """Retain last mode and an optional untouched reference index."""
    if psi.ndim == 1:
        psi = psi[:, None]
    nr = psi.shape[1]
    groups = defaultdict(lambda: np.zeros((M+1, nr), complex))
    for index, occ in enumerate(states):
        groups[occ[:-1]][occ[-1], :] += psi[index, :]
    rho = np.zeros(((M+1)*nr, (M+1)*nr), complex)
    for v in groups.values():
        x = v.reshape(-1)
        rho += np.outer(x, x.conj())
    return rho


def passive_fock_unitary(U, M):
    """Second quantization by creation-operator polynomial expansion."""
    modes = U.shape[0]
    states = [n for n in itertools.product(range(M+1), repeat=modes) if sum(n) <= M]
    where = {n: i for i, n in enumerate(states)}
    out = np.zeros((len(states), len(states)), complex)
    for col, occupation in enumerate(states):
        terms = {(0,)*modes: 1.+0j}
        for source in range(modes):
            for _ in range(occupation[source]):
                updated = defaultdict(complex)
                for n, value in terms.items():
                    for target in range(modes):
                        k = list(n);k[target] += 1
                        updated[tuple(k)] += value*U[target, source]
                terms = updated
        factor = math.prod(math.factorial(x) for x in occupation)
        for n, value in terms.items():
            out[where[n], col] = value*np.sqrt(math.prod(math.factorial(x) for x in n)/factor)
    near(out.conj().T@out, np.eye(len(states)), 'Second-quantized unitarity', 5e-12)
    return out, states


def test_passive_reduction():
    rows = []
    for _ in range(6):
        X = RNG.normal(size=(3, 3))+1j*RNG.normal(size=(3, 3))
        H = (X+X.conj().T)/2
        U = expm(-1j*H)
        h = U[2, :2];eta = float(np.vdot(h, h).real)
        near(eta+abs(U[2, 2])**2, 1., 'Signal plus vacuum commutator')
        f = h/np.sqrt(eta)
        W = np.array([[-f[1].conjugate(), f[0].conjugate()], [f[0], f[1]]])
        phase = U[2, 2]/abs(U[2, 2])
        B = np.array([[np.sqrt(1-eta), -np.sqrt(eta)*phase], [np.sqrt(eta), np.sqrt(1-eta)*phase]])
        W3 = np.eye(3, dtype=complex);W3[:2, :2] = W
        B3 = np.eye(3, dtype=complex);B3[1:, 1:] = B
        V = B3@W3
        near(V[2, :], U[2, :], 'Selected-mode-plus-loss row')
        UF, states = passive_fock_unitary(U, 3)
        VF, _ = passive_fock_unitary(V, 3)
        initial = np.zeros((len(states), 2), complex)
        for i, n in enumerate(states):
            if n[-1] == 0:
                initial[i] = RNG.normal(size=2)+1j*RNG.normal(size=2)
        initial /= np.linalg.norm(initial)
        actual = reduced_last_mode(UF@initial, states, 3)
        predicted = reduced_last_mode(VF@initial, states, 3)
        err = near(actual, predicted, 'Reduced state with untouched entangled reference', 3e-12)
        rows.append(dict(signal_transmissivity=eta, joint_memory_reference_error=err))
    return dict(cases=len(rows), rows=rows,
                scope='Finite tests of the general one-row passive-dilation proof, including number superpositions and temporal-mode correlations.')


def test_cavity_kernel():
    rows = []
    for a, eps, T in [(0., .1, 8.), (.2, .01, 16.), (.6, .001, 32.)]:
        F = float(cumulative(T, a))
        eta = F/(eps+F)
        integral = quad(lambda t:receiver_rate(t, a, eps), 0, T, epsabs=1e-11)[0]
        near(np.exp(-integral), eps/(eps+F), 'Retained initial-vacuum coefficient', 2e-12)
        for t in [0., .05, .4, 2., T]:
            future = quad(lambda s:receiver_rate(s, a, eps), t, T, epsabs=1e-11)[0]
            kernel = np.sqrt(receiver_rate(t, a, eps))*np.exp(-future/2)
            near(kernel, pulse(t, a)/np.sqrt(eps+F), 'Exact tunable-cavity input kernel', 2e-11)
        norm = quad(lambda t:(pulse(t, a)/np.sqrt(eps+F))**2, 0, T, epsabs=1e-11)[0]
        near(norm, eta, 'Finite memory capture efficiency')
        rows.append(dict(a=a, epsilon=eps, horizon=T, target_mode_mass=F,
                         mode_transmissivity=eta, coupling_rate_at_start=(1-a)/eps,
                         initial_memory_vacuum_weight=1-eta))
    return dict(cases=len(rows), rows=rows, scope='Explicit regularization, not an optimized bounded-coupling control.')


def test_actual_cascade():
    rows = []
    N, M = 40, 10
    a = (.75*M-1)/N
    for eps in [.1, .01, .001]:
        T = 32.;F = float(cumulative(T, a));eta = F/(eps+F)
        values = []
        for m in range(M+1):
            overlap = direct_overlap(N, m, a, T)
            emitted_truncated = overlap/F**(m/2)
            predicted = eta**(m/2)*emitted_truncated
            actual = capture_amplitude(N, m, a, eps, T)
            near(actual, predicted, 'Open source-cavity cascade versus emitted-mode overlap', 2e-9)
            values.append(dict(m=m, finite_mode_fidelity=emitted_truncated**2,
                               actual_memory_fidelity=actual**2, prediction=predicted**2))
        rows.append(dict(N=N,M=M,a=a,epsilon=eps,horizon=T,
                         mode_capture_efficiency=eta,peak_rate_candidate=(1-a)/eps,
                         minimum_input_fidelity=min(v['actual_memory_fidelity'] for v in values),values=values))
    for m in [1,2,5,10]:
        eta=float(cumulative(24.,0.)/(.01+cumulative(24.,0.)))
        amp=capture_amplitude(20,m,0.,.01,24.,True)
        # Harmonic emitter pulse is exactly f0, with missed late photons charged.
        prediction=(eta*cumulative(24.,0.))**m
        near(amp**2,prediction,'Harmonic oscillator control',2e-9)
    return dict(cases=len(rows)+4, rows=rows,
                scope='Complete cascade amplitudes, no discarded successful-only normalization; actual minimum scanned over all eleven code number states.')


def full_master(N, M, a, eps, T, initial):
    states = [(k,j) for k in range(M+1) for j in range(M+1-k)]
    index = {n:i for i,n in enumerate(states)};D=len(states)
    S = np.zeros((D,D),complex);b = np.zeros_like(S)
    for col,(k,j) in enumerate(states):
        if k:S[index[k-1,j],col]=np.sqrt(k*(1-(k-1)/N))
        if j:b[index[k,j-1],col]=np.sqrt(j)
    nr = initial.shape[1]
    S=np.kron(S,np.eye(nr));b=np.kron(b,np.eye(nr));dim=D*nr
    psi=initial.reshape(-1);rho=np.outer(psi,psi.conj())
    def rhs(t,y):
        r=y.reshape(dim,dim);R=-np.sqrt(receiver_rate(t,a,eps))*b
        L=S+R;H=(R.conj().T@S-S.conj().T@R)/(2j);K=L.conj().T@L
        return (-1j*(H@r-r@H)+L@r@L.conj().T-.5*(K@r+r@K)).reshape(-1)
    sol=solve_ivp(rhs,(0,T),rho.reshape(-1),method='DOP853',rtol=2e-10,atol=2e-13,max_step=.12)
    require(sol.success,sol.message);out=sol.y[:,-1].reshape(dim,dim)
    near(np.trace(out),1.,'Unconditional master-equation trace',3e-10)
    require(np.linalg.eigvalsh((out+out.conj().T)/2).min()>-1e-9,'Master density positivity')
    memory=np.zeros(((M+1)*nr,(M+1)*nr),complex)
    for (k,j),ii in index.items():
        for jj in range(M+1-k):
            kk=index[k,jj]
            memory[j*nr:(j+1)*nr,jj*nr:(jj+1)*nr]+=out[ii*nr:(ii+1)*nr,kk*nr:(kk+1)*nr]
    return memory,states


def test_master_reference():
    N,M,a,eps,T=12,3,.1,.03,24.
    states=[(k,j) for k in range(M+1) for j in range(M+1-k)]
    idx={x:i for i,x in enumerate(states)};rows=[]
    for m in [1,3]:
        initial=np.zeros((len(states),1),complex);initial[idx[m,0],0]=1
        rho,_=full_master(N,M,a,eps,T,initial)
        amp=capture_amplitude(N,m,a,eps,T)
        near(rho[m,m].real,amp**2,'Unconditional master equation versus no-output target probability',2e-9)
        rows.append(dict(m=m,memory_fock_fidelity=float(rho[m,m].real),amplitude_prediction=amp**2))
    initial=np.zeros((len(states),2),complex)
    initial[idx[0,0],0]=1/np.sqrt(2);initial[idx[3,0],1]=1/np.sqrt(2)
    memory,_=full_master(N,M,a,eps,T,initial)
    target=np.zeros((M+1,2),complex);target[0,0]=target[3,1]=1/np.sqrt(2)
    v=target.reshape(-1);fidelity=float(np.vdot(v,memory@v).real)
    A=capture_amplitude(N,3,a,eps,T)
    near(fidelity,((1+A)/2)**2,'Reference-entangled canonical map fidelity',2e-9)
    return dict(cases=3,fock_rows=rows,entangled_reference_fidelity=fidelity,
                entangled_reference_prediction=((1+A)/2)**2,
                scope='No output-field measurement, heralding, or subsequent nonlinear recovery.')


def test_loss_and_finite_bounds():
    rows=[]
    for M in [10,100,200,300]:
        for eta in [.99,.999,.9999]:
            rows.append(dict(M=M,independent_extra_transmissivity=eta,loss_only_fidelity_ceiling=eta**M))
    requirements=[dict(M=M,target=.9,necessary_transmissivity=float(np.exp(np.log(.9)/M))) for M in [100,200,300]]
    # Inherited source lower bounds; values copied as conservative truncated decimals,
    # not recomputed or strengthened by the present receiver calculation.
    receiver=[]
    for N,M,L in [(1000,100,.98812112),(1000,200,.90687697),(1000,300,.68130538)]:
        a=(.75*M-1)/N;T=32.;eps=1e-5
        F=float(cumulative(T,a));p=F/(eps+F)
        tail=np.sqrt(max(0.,M*(1-F)))
        lower=p**M*max(0.,L-tail)
        receiver.append(dict(N=N,M=M,baseline_mode_lower=L,epsilon=eps,horizon=T,
                             capture_efficiency=p,rate_at_start=(1-a)/eps,
                             truncated_pulse_penalty_bound=tail,complete_receiver_lower=lower))
    return dict(cases=len(rows)+len(requirements)+len(receiver),loss_ceilings=rows,
                necessary_requirements=requirements,finite_receiver_lower_bounds=receiver,
                scope='Loss-only necessary condition for the uncorrected canonical code, not a fault-tolerant logical bound or an optimized rate-limited receiver.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=ap.parse_args();groups={}
    for name,fn in [('passive_network_reduction',test_passive_reduction),
                    ('bounded_cavity_kernel',test_cavity_kernel),
                    ('dicke_source_and_receiver',test_actual_cascade),
                    ('unconditional_master_equation',test_master_reference),
                    ('loss_and_bandwidth_accounting',test_loss_and_finite_bounds)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-02',seed=SEED,group_count=len(groups),
                parameter_cases=sum(g['cases'] for g in groups.values()),groups=groups,
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                scope='Independent finite receiver checks of the documented model; no experimental results, universal decoder no-go, or independent novelty certification.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output)


if __name__=='__main__':main()
