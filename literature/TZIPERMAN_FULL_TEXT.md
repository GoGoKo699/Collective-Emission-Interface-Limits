# Tziperman et al.: construction-level comparison

Tziperman et al. use collective emission and a selected temporal mode to transfer specified emitter states into quantum light. This comparison identifies the shared source and target, and the additional uniform guarantee established by the common-receiver theorem.

## Source versions

Offek Tziperman et al., *Nonlinear Quantum Light Generation in Collective Spontaneous Emission*, ACS Nano **19**, 21260–21270 (2025), [DOI](https://doi.org/10.1021/acsnano.4c15257); associated preprint [arXiv:2306.11348](https://arxiv.org/abs/2306.11348).

The [authors' laboratory publication list](https://kaminer.net.technion.ac.il/publications-list/) supplies the [main article](https://kaminer.net.technion.ac.il/files/2025/06/tziperman-et-al-2025-nonlinear-quantum-light-generation-in-collective-spontaneous-emission.pdf) and [supplement](https://kaminer.net.technion.ac.il/files/2025/06/nn4c15257_si_001.pdf). The comparison uses the 11-page publisher-formatted early-online main article with printed letters A–K and placeholder issue pagination, together with its 23-page SI. Page numbers below count PDF pages from one.

The relevant constructions are in the main scientific body and SI Sections I–VI, especially II, IV and VI.

## Direct evidence

| Ingredient | Located construction |
|---|---|
| Source | Main Section 2.3, p. 5/E, replaces the source cavity operator by $`S_-`$. Section 2.4, p. 7/G, identifies wavelength-spaced emitters with zero mediated interaction as the Dicke limit. |
| Pulse selection | Main Section 2.2.2, p. 4/D, diagonalizes the first-order field kernel and selects its largest-occupation mode. |
| Output state | Main Eq. (4), p. 4/D, calculates the selected mode's density matrix while tracing unwanted modes. This is a full-state calculation. |
| Large-system statement | Main Section 2.5, p. 8/H, discusses increasing emitter number while holding excitation number constant. |
| Receiver | SI II.3–II.4, pp. 7–9, Eqs. (S13)–(S23), uses the Kiilerich–Mølmer unidirectional virtual oscillator with prescribed capture coupling. |
| Shared collective channel | SI IV.2, p. 14, Eq. (S45), gives $`L_0=\sqrt{\Gamma_{1D}}S_-+g_0^*(t)a_0`$. |
| Number-map target | SI IV.4, pp. 16–17 and Fig. S7, fixes an even cat with $`\alpha=2`$, copies truncated, renormalized Fock coefficients into the Dicke basis, and varies $`N`$. |
| Input examples | SI VI, pp. 21–22, Eqs. (S76)–(S79), specifies prepared cat, GKP and squeezed states. |

## Relation to the common-receiver theorem

After removing carrier rotation, matching rate and phase conventions and imposing the lossless symmetric case, the shared source has our ladder rates $`\gamma m(N-m+1)`$. The coefficient-copying example also overlaps our canonical number target. The paper gives collective full-state transfer calculations for selected inputs, including number-dependent mode distortion and selected-mode capture.

The mode-selection procedure is applied to the radiation from a specified initial state. Thus its calculation allows the chosen waveform to depend on that preparation. Our optimization instead chooses one waveform before an arbitrary, possibly reference-entangled input in $`\mathcal C_M`$. The quantifier order distinguishes a selected-state calculation from a uniform channel guarantee.

The virtual oscillator calculates the ideal selected-mode state using a prescribed passive linear coupling, within the receiver class considered here.

The comparison uses the source, target and mode-selection construction. Its reported fidelity percentages have an unspecified squared-versus-root convention in these versions, so a numerical conversion to squared entanglement fidelity would require that definition.

Their asymptotic discussion holds excitation number fixed. The theorem here instead controls the emitted isometry uniformly on $`\mathcal C_M`$, optimizes over every common waveform and gives the matching $`e^{-c^3/192}`$ critical law. Selected-input success is compatible with a failing worst-input guarantee.

The additional result here is the controlled all-waveform, whole-code boundary and its separation from mean photon collection. The comparison is restricted to the documented constructions and versions above.
