# Model and proof of the common-mode boundary

**Consolidated on 3 October 2026; endpoint-safe proof clarification the same day.** This is an edited, standalone presentation of the preceding collective-emission calculations. It introduces no new source or receiver. The complete primitive identities and numerical benchmarks are covered by the preserved standalone suites. Statements below are mathematical claims within the declared model; the priority and physical-scope checks are separate.

## 1. Source, output normalization, and target

There are $N$ identical two-level emitters in the permutation-symmetric Dicke ladder. Their initial state is arbitrary in

$$\mathcal C_M=\mathrm{span}\,\{|D_N^m\rangle:0\leq m\leq M\},\qquad M\leq N.$$

Complete emission into one vacuum Markov channel has jump $\sqrt\gamma S_-$. There is no extra Hamiltonian or inaccessible decay in this theorem. In time $\tau=N\gamma t$, the rates are $\ell_k=k[1-(k-1)/N]$.

The emitted $m$-photon state has a positive symmetric wavefunction in the normalized labeled-time convention:

```math
\begin{aligned}
\Psi_{N,m}(\boldsymbol{\tau})
&=C_{N,m}e^{-\sum_i\tau_i/2}\\
&\quad\times\exp\!\left[\frac{1}{N}\sum_{i<j}\min(\tau_i,\tau_j)\right],\\
C_{N,m}^2&=\prod_{j=0}^{m-1}(1-j/N).
\end{aligned}
```

Its squared modulus integrates to one on $[0,\infty)^m$. The factor from the $m!$ ordered time regions is already accounted for. The product-mode Fock state corresponds to $\prod_i f(\tau_i)$ for $\|f\|_2=1$. This cascade and its physical origin are inherited from existing Dicke-output theory, especially Paulisch [P1].

The receiver retains one mode $f$, chosen before learning the input, and traces the orthogonal modes. A predetermined photon-number-preserving linear receiver with vacuum auxiliaries reduces to

$$c_{\rm out}=\sqrt q\,b_f+\sqrt{1-q}\,v,$$

with vacuum $v$ and $0\leq q\leq1$, by passive input-output structure [P2]. The ideal optimization takes $q=1$. Auxiliary modes are allowed internally, but only one final oscillator is retained. Feedback changing the source, active Gaussian operations, nonvacuum ancillary inputs, measurement feedback, nonlinear decoding, and alternative encodings are not included.

The target is $|D_N^m\rangle\mapsto|m\rangle_f$, not merely conservation of energy or a classical number label. Fidelity means squared entanglement fidelity, allowing an untouched reference.

## 2. Reduction of the channel objective

For nonnegative $f$, write $A_m(f)=\langle m_f|\Psi_{N,m}\rangle\geq0$. The vacuum-complement Kraus operator is diagonal, $K_0=\mathrm{diag}(A_0,\ldots,A_M)$. Every other Kraus operator lowers the number retained in the oscillator.

For every input density matrix,

$$F_e(\rho)=\sum_\nu|\mathrm{Tr}(\rho K_\nu)|^2
\geq\left(\sum_m\rho_{mm}A_m\right)^2\geq\min_m A_m^2.$$

A number state attaining the smallest diagonal value saturates this inequality, since every nonvacuum discarded field gives the wrong output number. Therefore the exact optimum is

$$\boxed{\mathcal F_{N,M}=\sup_{\|f\|_2=1}\min_{m\leq M}|\langle m_f|\Psi_{N,m}\rangle|^2.}$$

For a complex $f$, replacing it by $|f|$ cannot reduce any overlap modulus, because the emitted amplitudes are positive. Fock-state inputs bound its worst fidelity from above, and the corresponding positive waveform realizes the resulting minimum. Optimizing over all complex waveforms thus does not evade the reduction.

The environment decomposition is used only in the proof. There is no postselection. For a nonnegative receiving waveform with attenuation, the worst-input fidelity is $\min_m q^m|A_m(f)|^2$. The same positivity argument permits this restriction when optimizing the attenuated receiver; this equality is not asserted for each arbitrary complex waveform.

## 3. A uniform individually matched pulse approximation

For $0\leq a<1$, define

$$f_a(\tau)=\frac{\sqrt{1-a}\,e^{-\tau/2}}{1-a+a e^{-\tau}},\qquad a_m=(m-1)/N.$$

Use the vacuum for $m=0$ and $a_1=0$. Let $P=|\Psi_{N,m}|^2$ and $Q=\prod_i|f_{a_m}|^2$. For $m\geq2$, $a=a_m$, $b=1-a$,

$$D(Q\Vert P)=m\left[-\frac{b}{a}\ln b-1\right]-\sum_{j=0}^{m-1}\ln(1-j/N)=D_{N,m}.$$

This exact expression is cancellation-prone; the code evaluates it with high precision. A positive integral representation yields the uniform bound

$$0\leq D_{N,m}\leq B_{N,m}:=\frac{m(m-1)}{12N^2[1-(m-1)/N]^2}.$$

### Bound via the full counting process

The survival function for the product reference is $S(t)=e^{-t}/(b+a e^{-t})$, with $S'=-S(1-aS)$. Under that reference the surviving count $K$ is binomial with parameters $m,S$. Its intensity is $x=K(1-aS)$, while the true ladder intensity is $y=K[1-(K-1)/N]$.

The pointwise inequality

$$x\ln(x/y)-x+y\leq\frac{(x-y)^2}{2\min(x,y)}$$

and the exact size-biased binomial identity

$$\mathbb E\{K[K-1-(m-1)S]^2\}=m(m-1)S^2(1-S)$$

give

$$D(Q\Vert P)\leq\frac{m(m-1)}{2N^2b}\int_0^1\frac{S(1-S)}{1-aS}\,dS
\leq B_{N,m}.$$

This compares the full dependent emission process with the product reference; it does not treat the true photons as independent.

Since amplitudes are positive, Jensen's inequality for their Hellinger overlap implies

$$F_m(f_{a_m})\geq e^{-D_{N,m}}\geq e^{-B_{N,m}}.$$

The vector difference from the reference product state is at most

$$\varepsilon_m\leq\sqrt{2(1-e^{-B_{N,m}/2})}\leq\sqrt{B_{N,m}}.$$

Distinct photon-number sectors are orthogonal. The operator-norm error of the entire source isometry is therefore bounded by $\max_{m\leq M}\varepsilon_m$, not a sum over the code. It tends to zero uniformly for $M=o(N)$, and the same control holds with a reference system.

Thus each separately known $m=o(N)$ can be matched with fidelity tending to one. The common waveform requirement is the additional constraint.

## 4. Exact pulse geometry

Set $u=-\ln(1-a)$. Direct integration gives

$$K(u-v)=\langle f_u,f_v\rangle=\frac{u-v}{2\sinh[(u-v)/2]},\qquad
\ln K(z)=-z^2/24+O(z^4).$$

For $M\geq2$, choose $a_*=(3M/4-1)/N$. If $M/N^{2/3}\to c>0$ and $m/M=x$, the reference-product fidelity converges uniformly over the code to

$$K(u_m-u_*)^{2m}\longrightarrow
\exp\!\left[-\frac{c^3}{12}x(x-3/4)^2\right].$$

The maximum of $x(x-3/4)^2$ on $[0,1]$ is $1/16$, attained at $x=1/4$ and $x=1$. The construction therefore gives limiting worst fidelity $e^{-c^3/192}$. Uniform source-state control transfers this lower bound to the true field.

### A finite lower envelope

The preceding construction can be bounded before taking any limit. Define

$$b_M=1-(M-1)/N,\qquad B_M=\frac{M(M-1)}{12N^2b_M^2},\qquad
\epsilon=\sqrt{2(1-e^{-B_M/2})}.$$

Every sector vector error is at most $\epsilon$. The exact inequalities $\ln K(z)\geq-z^2/24$ and $|u_m-u_*|\leq |m-3M/4|/(Nb_M)$ give, for $M\geq2$,

$$\boxed{\mathcal F_{N,M}\geq
\left[\max\{0,e^{-M^3/(384N^2b_M^2)}-\epsilon\}\right]^2.}$$

This is uniform over the entire code and avoids interchanging a sector minimum with a pointwise limit. Vacuum and the $M\leq1$ codes transfer exactly. An elementary proof of the kernel inequality is in [the proof audit](PROOF_AUDIT.md).

## 5. Converse for every waveform

Take an integer $1\leq q<M$ and set

$$\theta=\arccos K(u_M-u_q),\qquad S=q^{-1/2}+M^{-1/2},\qquad X=\theta^2/S^2.$$

If a receiver has true fidelity at least $F$ on both $q$ and $M$, its reference-product overlap amplitudes are at least $\sqrt F-\epsilon$. When $s=\sqrt F-\epsilon>0$, its one-photon overlaps with the reference modes are at least $s^{1/q}$ and $s^{1/M}$. The projective Hilbert-space triangle inequality through the arbitrary receiver and $\arccos(e^{-t})\leq\sqrt{2t}$ imply

$$\theta\leq\arccos(s^{1/q})+\arccos(s^{1/M})
\leq\sqrt{-2\ln s}\,S.$$

Rearranging gives the finite all-waveform upper bound

$$\boxed{\mathcal F_{N,M}\leq
\min\{1,[\epsilon+e^{-X/2}]^2\}.}$$

For $\sqrt F\leq\epsilon$ the bound is automatic. It holds for every waveform, so no optimizer needs to exist and complex phases cannot evade it. The same bound directly applies to the two-sector code. This elementary envelope is used for proof clarity, not in place of the sharper numerical angle brackets below.

At $q=\lfloor M/4\rfloor$ and $M/N^{2/3}\to c>0$,

$$b_M\to1,\qquad\epsilon\to0,\qquad
X=\frac{M^3}{192N^2}[1+o(1)]\to c^3/192.$$

The finite constructive and converse bounds therefore squeeze the optimum to

$$\boxed{M/N^{2/3}\to c>0\quad\Longrightarrow\quad
\mathcal F_{N,M}\to e^{-c^3/192}.}$$

This argument includes the unit-fidelity endpoint. The earlier compressed multiplicative-error argument required an additional justification there; the finite inequality supplies it. The [audit](PROOF_AUDIT.md) records that proof-level correction explicitly. The theorem statement and its coefficient are unchanged.

For $M=o(N^{2/3})$, the constructive lower envelope tends to one. For $M/N^{2/3}\to\infty$, restrict the full consecutive code to a subcode with cutoff near $cN^{2/3}$ for any fixed $c$. Monotonicity gives $\limsup\mathcal F\leq e^{-c^3/192}$ for every $c$, hence zero. This does not extend the critical exponential as an asymptotic equality throughout every supercritical regime. The two-sector code requires its own direct converse rather than this full-code monotonicity argument.

### Finite brackets

Define $\beta_m=\arccos(e^{-D_{N,m}/2})$. The chosen pulse gives

$$F_m(f_a)\geq\cos_+^2\!\left[\arccos K(u_m-u)^m+\beta_m\right].$$

For an all-waveform upper bound on simultaneous fidelity $F$, define

$$r_m(F)=\arccos\left\{\cos_+\left[\arccos\sqrt F+\beta_m\right]^{1/m}\right\}.$$

It is necessary that $r_q(F)+r_M(F)\geq\arccos K(u_q-u_M)$. Solving this scalar condition gives the finite converse used in the tests. Here $\cos_+$ is clipped to zero when the angle reaches $\pi/2$. These bounds need not coincide at finite $N$.

## 6. Mean photon collection has a larger domain of validity

On the $m$-photon sector, $E_m=I-\hat n_{f_*}/m$ is a positive contraction. The triangle inequality for $\sqrt{E_m}$ gives

$$\sqrt{\langle E_m\rangle_{\Psi_m}}
\leq\sqrt{1-K(u_m-u_*)^2}+\varepsilon_m.$$

Put $b_M=1-(M-1)/N$. From $\ln[\sinh(z/2)/(z/2)]\leq z^2/24$,

$$\sqrt{1-K(z)^2}\leq |z|/\sqrt{12},\qquad
|u_m-u_*|\leq\frac{|m-3M/4|}{Nb_M}.$$

Using $|m-3M/4|+\sqrt{m(m-1)}\leq5M/4$ yields

$$\frac{\langle\hat n_{f_*}\rangle_m}{m}
\geq1-\min\left\{1,\frac{25M^2}{192N^2b_M^2}\right\}.$$

For a general nonvacuum code input, the ratio $\langle\hat n_{f_*}\rangle/\langle\hat n_{\rm total}\rangle$ is a photon-number-weighted average of these sector ratios. Cross-number coherences do not contribute to number-preserving observables. The same bound therefore holds, including with reference entanglement.

It tends to one for every $M=o(N)$. Taking $M=\lfloor N^{3/4}\rfloor$ simultaneously gives vanishing excitation density, uniformly near-complete mean photon collection, and vanishing optimized whole-code transfer fidelity. This does not infer an unbounded moment from trace-distance convergence alone, nor assert failure of every low-excitation approximation.

## 7. Status and attribution

The emitted cascade, conventional exponential overlap, nonlinear-emission mode dependence, and passive-capture framework are prior results [P1–P4]. The optimized exponent is not claimed to be the first appearance of the $N^{2/3}$ scale. The candidate additional result is its all-waveform, whole-code, uniform optimization and the observable/channel distinction.

The calculations and proof have author-side audits but no independent report. The [Law–Lee full-text comparison](../literature/LAW_LEE_FULL_TEXT.md) is complete: mean-occupation optimization, the oscillator comparator, dominant few-mode behavior and the semiclassical pulse are credited directly. That scoped comparison did not establish subsumption of this uniform common-code theorem; it is not exhaustive priority certification. The [endpoint-safe proof audit](PROOF_AUDIT.md) records the current clarification and its limits. See also the [prior-art register](../literature/PRIOR_ART.md) and [physical boundaries](PHYSICAL_SCOPE.md). No joint large-code experiment is asserted.

[P1] V. Paulisch, *Waveguide Quantum Electrodynamics*, dissertation (2018), Chapter 1. https://edoc.ub.uni-muenchen.de/22151/1/Paulisch_Vanessa.pdf

[P2] N. Yamamoto and M. R. James, *Zero-dynamics principle for perfect quantum memory in linear networks*, arXiv:1403.1698. https://arxiv.org/abs/1403.1698

[P3] M. Khanahmadi et al., *Multimode character of quantum states released from a superconducting cavity*, Physical Review Research 5, 043071 (2023). https://research.chalmers.se/publication/538258/file/538258_Fulltext.pdf

[P4] H. I. Nurdin, M. R. James, and N. Yamamoto, *Perfectly capturing traveling single photons of arbitrary temporal wavepackets with a single tunable device*, arXiv:1609.05643 (2016). https://arxiv.org/abs/1609.05643

[P5] C. K. Law and S. K. Y. Lee, *Dynamic photon-mode selection in Dicke superradiance*, Physical Review A 75, 033813 (2007). https://doi.org/10.1103/PhysRevA.75.033813
