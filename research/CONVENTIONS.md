# Conventions connecting the background to the theorem

**3 October 2026. Explanatory reference; no scientific result is changed.** The canonical definitions are in [THEOREM.md](THEOREM.md). These translations prevent superficially identical symbols from producing factor-of-two or fidelity errors when using the background sources.

## Source, time and rates

The dissipator is

$$\mathcal D[L]\rho=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.$$

For $L=\sqrt\gamma S_-$, the $m$-excitation population leaves at rate $\gamma m(N-m+1)$. With $\tau=N\gamma t$, the dimensionless rate is $\ell_m=m[1-(m-1)/N]$. A no-jump amplitude decays at half the corresponding population rate.

Law–Lee's Eq. (22) writes the collective dissipator with coefficient $\gamma_{\rm LL}$ multiplying $2J_-\rho J_+-\{J_+J_-,\rho\}$. Thus $\gamma=2\gamma_{\rm LL}$, and $\tau=2N\gamma_{\rm LL}t$. Their amplitude/rate notation must not be equated by matching the letter gamma alone. The [completed reading](../literature/LAW_LEE_FULL_TEXT.md) records this translation and the hyperbolic-secant correspondence.

$N$ is the physical number of emitters; $M$ is the largest allowed input excitation. In the independent-loss appendix the effective ladder parameter $Q=N+C^{-1}$ is not an increased physical atom count. In the SLH review, $S$ is a scattering operator in a network triple and is not the collective lowering operator $S_-$.

## Temporal modes and normalization

Use $[b(t),b^\dagger(t')]=\delta(t-t')$ and

$$b_f=\int f^*(t)b(t)dt,\qquad \|f\|_2=1,\qquad |m_f\rangle=(b_f^\dagger)^m|0\rangle/\sqrt{m!}.$$

The amplitude $f(t)$ has units of inverse square root of time. Under the dimensionless clock, a normalized real-time pulse is

$$f_{\rm physical}(t)=\sqrt{N\gamma}\,f_{\rm dimensionless}(N\gamma t).$$

Multiplying the argument by $N\gamma$ without the square-root prefactor would not preserve its norm. The labeled-time $m$-photon wavefunction used in THEOREM.md integrates to one over the full $m$-fold time domain. Its product-mode representative is $\prod_i f(t_i)$. Ordered jump amplitudes are an alternative convention, not an extra $m!$ normalization to apply afterward.

For $u=-\ln(1-a)$ the notation $f_u$ means the same pulse family reparameterized as $f_{1-e^{-u}}$. The exact overlap is $K(u-v)=(u-v)/(2\sinh[(u-v)/2])$, continued to $K(0)=1$. The vacuum is treated separately; a normalized waveform need not be assigned to zero emitted photons.

## Four quantities that must not share a label

| Quantity | Definition and meaning |
|---|---|
| Pulse overlap amplitude | $\langle f,g\rangle$; one-photon Hilbert-space overlap |
| Product $m$-photon fidelity | $|\langle f,g\rangle|^{2m}$; only for two product-mode Fock states |
| Mean collected fraction | $\langle n_f\rangle/\langle n_{\rm total}\rangle$; undefined for vacuum-only input |
| Canonical transfer fidelity | Squared entanglement fidelity relative to the prescribed number map, minimized over code inputs and optimized over one prechosen receiver |

The exact dependent emission does not acquire a product form by notation. Its replacement by an individually matched product pulse requires the uniform theorem. For fixed $m$, the probability $\Pr(n_f=m)$ equals the overlap with $|m_f\rangle$; the natural-mode eigenvalue is instead $\langle n_f\rangle$.

For superpositions, number-state fidelities alone do not determine channel fidelity. The positive diagonal/no-number-gain Kraus structure is what makes the optimized reduction work here. An input-dependent phase correction is not implicit in choosing a phase convention. The target oscillator states share one consistent phase reference.

## Receiver resources

“Passive linear” means number-preserving linear transformations of signal annihilation operators with vacuum auxiliaries. A driven frequency converter can have such an effective signal transformation even when pumps supply energy; an amplifier or squeezer mixing creation operators is outside it. The Hamiltonian and noise operators, not a device's marketing name, decide membership.

Only one oscillator is retained at the end. Several internal cavities may be used; retaining two output modes or adding a nonlinear decoder changes the task. Virtual-cavity couplings in a tutorial specify a mathematical mode map and can be singular. They are not automatically finite-bandwidth hardware controls.

## Probability and information conventions

The proof uses classical densities $P=|\Psi|^2$ and $Q=\prod|f|^2$, with $D(Q\Vert P)=\int Q\ln(Q/P)$ in nats. The Hellinger amplitude is $\int\sqrt{PQ}$; its square equals the quantum fidelity only because the compared amplitudes are nonnegative in this convention. The Rényi relation is $D_{1/2}\leq D_1$, yielding $F\geq e^{-D(Q\Vert P)}$.

State-specific preparation, heralded success probability, photon transmission, mean occupation, worst-input fidelity and quantum capacity remain distinct. A supremum over ideal waveforms is not a statement that every pulse can be captured perfectly at fixed time and bandwidth. The [background dossier](../literature/BACKGROUND.md) and [assumption register](../literature/ASSUMPTIONS.md) retain those boundaries.
