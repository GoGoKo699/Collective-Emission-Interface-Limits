# Scientific background for the fixed interface result

This guide explains the collective-emission model, traveling modes, passive reception and channel-fidelity tools underlying the theorem. Bibliographic keys refer to [REFERENCES.bib](REFERENCES.bib). Kiilerich–Mølmer (2020) is the single tutorial anchor; the [reading guide](../docs/README.md) and [local bridge](../REVIEW.md) connect it to the result. [TUTORIAL_OPTIONS.md](TUTORIAL_OPTIONS.md) explains the choice and lists optional references.

## 1. Collective emission and the oscillator approximation

Dicke's collective-emission model [Dicke1954] organizes identical emitters by collective angular momentum. In the permutation-symmetric sector,

```math
S_-|D_N^m\rangle=\sqrt{m(N-m+1)}\,|D_N^{m-1}\rangle.
```

With jump operator $`\sqrt\gamma S_-`$ and the dissipator convention in [CONVENTIONS.md](../research/CONVENTIONS.md), the decay rate from that level is $`\gamma m(N-m+1)`$. The exact ladder and cascade are developed in Paulisch's dissertation [Paulisch2018Thesis], Chapter 1, for multiphoton generation, and [Paulisch2019] treats the emitted field and its use in metrology.

On the truncated oscillator number space, the Holstein–Primakoff representation [HolsteinPrimakoff1940] can be written

```math
S_-=\sqrt{N-\hat n}\,a,\qquad S_+=a^\dagger\sqrt{N-\hat n}.
```

The operator order matters: $`a`$ acts first, giving the factor $`\sqrt{m(N-m+1)}`$. Replacing the square root by $`\sqrt N`$ gives the familiar linear oscillator approximation. A small occupied fraction controls the relative ladder correction. Uniform control of the many-photon field on an expanding input space requires the accumulated correction estimated in the theorem.

The source is conditional on identical effective couplings, a symmetric input, a known $`N`$, and one useful vacuum Markov channel. The source papers S01–S07 in the [evidence register](SOURCE_EVIDENCE.md) describe the collective-decay mechanism and its realization regimes.

## 2. A traveling mode is a degree of freedom, not a prescribed photon number

A single propagation channel contains a continuum of temporal modes. For a narrow-band field envelope with $`[b(t),b^\dagger(t')]=\delta(t-t')`$, a normalized waveform defines

```math
b_f^\dagger=\int f(t)b^\dagger(t)\,dt,\qquad \int|f(t)|^2dt=1.
```

The mode can contain vacuum, a Fock state, a superposition, or a mixed state. Raymer–Walmsley [RaymerWalmsley2020], Section 3, develops this distinction explicitly; Sections 4, 6 and 7 connect it to beam-splitter-like interactions, memories and temporal-mode selectivity. Neither one spatial channel nor a narrow spectrum proves occupation of one temporal mode. Conversely, a time-dependent wavepacket can be a perfectly well-defined single mode.

In the normalized symmetric labeled-time convention,

```math
|\Psi_m\rangle=\frac{1}{\sqrt{m!}}\int \Psi_m(t_1,\ldots,t_m)b^\dagger(t_1)\cdots b^\dagger(t_m)|0\rangle\,d^mt.
```

The full-domain wavefunction has norm one. For $`|m_f\rangle`$, it is $`\prod_i f(t_i)`$. Ordered photon-emission amplitudes are equivalent, but the ordering factor cannot be counted twice. The repository fixes this convention before forming overlaps; [PROOF_AUDIT.md](../research/PROOF_AUDIT.md) checks the normalization.

A collective jump and no-jump propagation generate a dependent emission cascade. Multiplying its ordered waiting-time amplitudes and symmetrizing gives the exact wavefunction used in [THEOREM.md](../research/THEOREM.md). Paulisch is the direct source-theory anchor; Kiilerich–Mølmer [KiilerichMolmer2020] supplies a pedagogical alternative description through cascaded source and output oscillators. Treating the exact photons as independent would remove the very correction that our uniform approximation must bound.

## 3. Mode occupation does not determine the complete field state

Law–Lee [LawLee2007], Eqs. (10)–(17), optimize the mean photon occupation by diagonalizing a first-order correlation kernel. The eigenvalues are $`\langle b_j^\dagger b_j\rangle`$. Their purity is the purity of the normalized one-photon correlation operator, not the density-matrix purity of the complete radiation. Lemberger–Mølmer [LembergerMolmer2021] pursues the same occupation-eigenmode objective using a later treatment of the correlations.

Their complete-decay modes are candidate receiving envelopes. The [Law–Lee comparison](LAW_LEE_FULL_TEXT.md) also locates their oscillator comparator, dominant few-mode behavior and semiclassical pulse.

The quantities are different but not unrelated. For a fixed $`m>0`$ define $`p_f=\langle n_f\rangle/m`$ and $`F_f=\Pr(n_f=m)`$. Then

```math
\max\{0,1-m(1-p_f)\}\leq F_f\leq p_f.
```

Indeed, the integer number outside the mode is zero on the all-in-mode event and between one and $`m`$ otherwise. For a pure field, $`F_f=|\langle m_f|\Psi_m\rangle|^2`$. Exact $`p_f=1`$ does imply complete one-mode support. Merely proving $`p_f\to1`$ while $`m`$ grows does not imply $`F_f\to1`$ without controlling the absolute missed-photon scale. A second issue is whether the same waveform works for different possible occupied numbers.

Kiilerich–Mølmer [KiilerichMolmer2020], introduction and Section II C, distinguish mean field/intensity from the quantum state of a selected output pulse. That article also describes how nonlinear dynamics correlate number with pulse shape.

## 4. The receiving operation and its physical limits

Quantum input–output and cascaded-system theory connect a source to an absorbing oscillator without replacing the traveling field by an initially occupied cavity eigenmode. The SLH review [Combes2017], Sections III–VI, systematically states the Markov approximations, network composition and passive linear equations. Kiilerich–Mølmer [KiilerichMolmer2019; KiilerichMolmer2020] uses virtual cavities to calculate the quantum state of any specified output mode, not only its first moments.

The receiver allowed here is predetermined, photon-number preserving and linear, with vacuum ancillary inputs and one final retained oscillator. A linear Heisenberg output has an incoming-field term plus vacuum contributions. Normalizing the field coefficient gives

```math
c_{\rm out}=\sqrt q\,b_f+\sqrt{1-q}\,v,\qquad0\leq q\leq1.
```

This reduction applies the established passive-network framework [YamamotoJames2014; Combes2017]. Extra internal cavities and prescribed linear mixing may help implement a waveform under engineering constraints, but cannot outperform a supremum already taken over all normalized $`f`$ with $`q=1`$.

Ideal arbitrary-wavepacket absorption can demand singular control at its onset. Nurdin–James–Yamamoto [Nurdin2016] explicitly treats this issue. The finite receiving-cavity construction in our physical-scope note regularizes this coupling and quantifies its amplitude and duration.

Gorshkov et al. [Gorshkov2007] is an important successful comparator. Its linearized vacuum-noise memory model transfers the state occupying a specified pulse, not merely its intensity. Appendix A replaces the ground-state population by $`N`$ and keeps the signal to first order. Our finite-spin result instead retains the number-dependent ladder correction and bounds its accumulated field error uniformly.

## 5. Quantum-state fidelity and a reference system

Schumacher [Schumacher1996] defines entanglement fidelity by purifying the input into an untouched reference. For Kraus operators $`K_\nu`$, the standard formula is

```math
F_e(\rho)=\sum_\nu|\mathrm{Tr}(\rho K_\nu)|^2.
```

The repository compares the received channel with the canonical number isometry, not with an independently optimized target or recovery. It uses squared fidelity. Preparing a selected target, preserving an unknown input, estimating a parameter, and achieving quantum capacity are distinct tasks.

The reduction of our optimized worst-input objective to a minimum of number-state overlaps is a property of this channel, not a general fidelity identity. The no-discarded-photon Kraus operator is positive diagonal for nonnegative receiving pulses; the other Kraus operators lower the retained number. This gives the lower bound for arbitrary inputs, including reference entanglement, and a number state attains it. Positivity of the emitted amplitudes then justifies the optimized reduction from complex pulses to their moduli. A generic phase-distorting channel need not preserve superpositions just because it preserves basis-state fidelities.

Tracing the unwanted field gives an unconditional channel. For transmission $`q`$, the corresponding number-state contribution includes $`q^m`$; this factor accounts for loss separately from mode matching. THEOREM.md and PROOF_AUDIT.md give the channel-specific proof and a phase counterexample.

## 6. Mathematical tools and where the project's proof begins

The uniform proof compares the exact dependent photon-time density $`P`$ with an explicitly chosen product reference $`Q`$. The direction is $`D(Q\Vert P)`$, where the expectation is over the simpler reference. The particular counting-process likelihood, size-biased binomial identity and finite bound are derived in the canonical proof.

A standard information-theoretic step turns that density estimate into a state estimate. The order-$`1/2`$ Rényi divergence is $`-2\ln\int\sqrt{PQ}`$ and is no larger than the Kullback–Leibler divergence. The order monotonicity and definitions are in van Erven–Harremoës [vanErven2014], especially Theorem 3 and the order-one limit. Since our wavefunctions have nonnegative amplitudes in the declared convention,

```math
|\langle\Psi_P|\Psi_Q\rangle|^2\geq e^{-D(Q\Vert P)}.
```

Positivity is essential. Matching photon-time probabilities would not control arbitrary unobserved phases. The resulting vector error controls the whole emitted isometry because different photon-number sectors are orthogonal. Its operator norm is the largest sector error, not the sum over the growing code, and remains controlled upon adjoining a reference.

The receiving-waveform converse uses the projective Hilbert-space angle $`\arccos|\langle f,g\rangle|`$, its triangle inequality, and elementary scalar inequalities. It applies to waveforms outside the span of the reference modes. Finite bounds are derived before the joint limit: an additive overlap error cannot simply be called a small relative logarithmic error near fidelity one. PROOF_AUDIT.md gives the endpoint argument and negative control.

The exact reference-pulse kernel, its minimax placement, the matching uniform converse and the growing-code photon-collection contrast form the uniform interface theorem. The [local bridge](../REVIEW.md) derives these additional steps from the optical framework of the tutorial.

## 7. Preparation and effective source rates

The [preparation evidence](PREPARATION_EVIDENCE.md) describes five related constructions, including classically specified targets, heralded preparation and oscillator reductions. The theorem takes an arbitrary state in its symmetric code as input; an encoding of that resource must preserve its coherence with an external reference.

The independent-loss product, collective enhancement and Raman rate control already have direct predecessors in the source papers. In a simple rapidly damped cavity, useful decay, cavity bandwidth and microscopic coupling are related. Enlarging $`N`$ at fixed microscopic parameters is not identical to keeping the effective useful-to-loss ratio fixed. The [physical analysis](../research/PHYSICAL_SCOPE.md) makes this rate distinction explicit.

The [assumption register](ASSUMPTIONS.md) states the known-$`N`$ source premise and the preparation, rate and receiver resources used by the effective model.

## 8. Claim-to-source map

| Statement | Primary basis and precise role | Interpretation |
|---|---|---|
| Symmetric collective ladder and correlated multiphoton cascade | Dicke; Paulisch thesis Chapter 1 and Appendix 1.A; Paulisch et al. 2019 | Exact inherited source model and emitted-state solution |
| A mode can carry an arbitrary quantum state | Raymer–Walmsley Section 3; Kiilerich–Mølmer 2020 Sections II–III | One mode is not one photon; one spatial port is not one temporal mode |
| Natural modes optimize mean occupations | Law–Lee Eqs. (10)–(21); Lemberger–Mølmer Sections 2.1–2.2 | First-order field observable |
| Full selected-output-mode calculations and number-dependent pulse distortion | Kiilerich–Mølmer 2019/2020; Khanahmadi et al. 2023 Sections IV–V | Selected-mode full-state calculations |
| One-oscillator passive reception | Yamamoto–James; Nurdin et al.; Combes et al. VI A | Predetermined passive receiver with one retained oscillator |
| Quantum-channel benchmark | Schumacher plus the channel-specific proof here | Canonical transfer with an untouched reference |
| Uniform approximation and all-waveform critical limit | THEOREM.md and PROOF_AUDIT.md | Uniform control on a growing code and matching converse |
| Realization and preparation context | Existing S/R/P registers and PHYSICAL_SCOPE.md | Source and receiver component models |
| Closest collective-light comparison | Tziperman et al. 2025: main article and supplement inspected | Shared source and target, with input-dependent mode selection |

## 9. The close Tziperman comparison

[Tziperman2025], published as *Nonlinear Quantum Light Generation in Collective Spontaneous Emission*, has an arXiv precursor titled *The quantum state of light in collective spontaneous emission*. The publisher abstract explicitly concerns transferring emitter correlations to traveling single-mode non-Gaussian states, with cavity, waveguide and array examples, losses, interactions and beyond-Markov effects.

The [full-text note](TZIPERMAN_FULL_TEXT.md) records the source, input, mode-selection, target and asymptotic comparison. Their cavity-free collective source overlaps ours. They select a mode from the first-order correlation of the specified input and then calculate its full quantum state. The theorem here instead fixes one receiver for a growing unknown code and establishes a matching minimax converse.

The [additional source comparisons](PREWRITING_SEARCH_2026_10_05.md) cover
Porras–Cirac, Perarnau-Llobet et al., and Belliardo et al. The
[claim map](../research/CLAIM_EVIDENCE_MAP.md) connects the literature to the proof
and physical scope.
