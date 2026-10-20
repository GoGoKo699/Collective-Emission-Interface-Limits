# Source, receiver and channel objective

[Scientific route](README.md) · [Conventions](CONVENTIONS.md) · [Matched pulses](MATCHED_PULSES.md)

The interface transfers an unknown symmetric collective-spin state into one
preconfigured receiving oscillator. This page fixes the source, allowed receiver,
canonical target and reference-inclusive fidelity before any approximation is made.
The [common-mode theorem](COMMON_MODE_BOUNDARY.md) optimizes this same task over all
receiving waveforms; [photon collection](PHOTON_COLLECTION.md) measures a different
observable of the same output.

## Source, output normalization, and target

There are $`N`$ identical two-level emitters in the permutation-symmetric Dicke ladder. Their initial state is arbitrary in

```math
\mathcal C_M=\mathrm{span}\,\{|D_N^m\rangle:0\leq m\leq M\},\qquad M\leq N.
```

Complete emission into one vacuum Markov channel has jump $`\sqrt\gamma S_-`$. There is no extra Hamiltonian or inaccessible decay in this theorem. In time $`\tau=N\gamma t`$, the rates are $`\ell_k=k[1-(k-1)/N]`$.

The emitted $`m`$-photon state has a positive symmetric wavefunction in the normalized labeled-time convention:

```math
\begin{aligned}
\Psi_{N,m}(\boldsymbol{\tau})
&=C_{N,m}e^{-\sum_i\tau_i/2}\\
&\quad\times\exp\!\left[\frac{1}{N}\sum_{i\lt j}\min(\tau_i,\tau_j)\right],\\
C_{N,m}^2&=\prod_{j=0}^{m-1}(1-j/N).
\end{aligned}
```

Its squared modulus integrates to one on $`[0,\infty)^m`$. The factor from the $`m!`$ ordered time regions is already accounted for. The product-mode Fock state corresponds to $`\prod_i f(\tau_i)`$ for $`\|f\|_2=1`$. This cascade and its physical origin are inherited from existing Dicke-output theory, especially [Paulisch](README.md#primary-sources).

The receiver retains one mode $`f`$, chosen before learning the input, and traces the orthogonal modes. A predetermined photon-number-preserving linear receiver with vacuum auxiliaries reduces to

```math
c_{\rm out}=\sqrt q\,b_f+\sqrt{1-q}\,v,
```

with vacuum $`v`$ and $`0\leq q\leq1`$, by passive input-output structure [Yamamoto–James](README.md#primary-sources). The ideal optimization takes $`q=1`$. Auxiliary modes are allowed internally, but only one final oscillator is retained. Feedback changing the source, active Gaussian operations, nonvacuum ancillary inputs, measurement feedback, nonlinear decoding, and alternative encodings are not included.

The target is $`|D_N^m\rangle\mapsto|m\rangle_f`$, not merely conservation of energy or a classical number label. Fidelity means squared entanglement fidelity, allowing an untouched reference.

## Reduction of the channel objective

For nonnegative $`f`$, write $`A_m(f)=\langle m_f|\Psi_{N,m}\rangle\geq0`$. The vacuum-complement Kraus operator is diagonal, $`K_0=\mathrm{diag}(A_0,\ldots,A_M)`$. Every other Kraus operator lowers the number retained in the oscillator.

For every input density matrix,

```math
F_e(\rho)=\sum_\nu|\mathrm{Tr}(\rho K_\nu)|^2
\geq\left(\sum_m\rho_{mm}A_m\right)^2\geq\min_m A_m^2.
```

A number state attaining the smallest diagonal value saturates this inequality, since every nonvacuum discarded field gives the wrong output number. Therefore the exact optimum is

```math
\boxed{\mathcal F_{N,M}=\sup_{\|f\|_2=1}\min_{m\leq M}|\langle m_f|\Psi_{N,m}\rangle|^2.}
```

For a complex $`f`$, replacing it by $`|f|`$ cannot reduce any overlap modulus, because the emitted amplitudes are positive. Fock-state inputs bound its worst fidelity from above, and the corresponding positive waveform realizes the resulting minimum. Optimizing over all complex waveforms thus does not evade the reduction.

The environment decomposition is used only in the proof. There is no postselection. For a nonnegative receiving waveform with attenuation, the worst-input fidelity is $`\min_m q^m|A_m(f)|^2`$. The same positivity argument permits this restriction when optimizing the attenuated receiver; this equality is not asserted for each arbitrary complex waveform.

The [normalization and channel details](PROOF_DETAILS.md#1-ordered-time-normalization)
verify the ordered-time factors and the role of complex phases. The next step is a
[uniform approximation of the correlated emitted field](MATCHED_PULSES.md), which
makes the common-waveform optimization tractable without assuming independent
photons.
