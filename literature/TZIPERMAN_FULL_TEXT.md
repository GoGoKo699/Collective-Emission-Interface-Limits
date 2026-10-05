# Tziperman et al.: construction-level comparison

**5 October 2026.** The previously missing reading is now completed for the versions below. This is an internal literature comparison, not an independent proof report or exhaustive novelty certification. The source, receiver, code, target and theorem remain fixed.

## Sources and reading scope

Offek Tziperman et al., *Nonlinear Quantum Light Generation in Collective Spontaneous Emission*, ACS Nano **19**, 21260–21270 (2025), [DOI](https://doi.org/10.1021/acsnano.4c15257); associated preprint [arXiv:2306.11348](https://arxiv.org/abs/2306.11348).

The [authors' laboratory publication list](https://kaminer.net.technion.ac.il/publications-list/) supplies the [main article](https://kaminer.net.technion.ac.il/files/2025/06/tziperman-et-al-2025-nonlinear-quantum-light-generation-in-collective-spontaneous-emission.pdf) and [supplement](https://kaminer.net.technion.ac.il/files/2025/06/nn4c15257_si_001.pdf). Both complete PDFs were downloaded and inspected. The main file is an 11-page publisher-formatted early-online copy with printed letters A–K and placeholder issue pagination; it was not compared line by line with a final issue PDF or the arXiv versions. SI has 23 PDF pages. Page numbers below count PDF pages from one.

The main scientific body and SI Sections I–VI were read, with particular attention to II, IV and VI. Main pages 4/D, 5/E and 8/H, and SI pages 9, 14, 16 and 17 were rendered to check equations and the fixed-target construction. Neither third-party PDF is redistributed here.

## Direct evidence

| Question | Located construction |
|---|---|
| Source | Main Section 2.3, p. 5/E, replaces the source cavity operator by $`S_-`$. Section 2.4, p. 7/G, identifies wavelength-spaced emitters with zero mediated interaction as the Dicke limit. |
| Pulse selection | Main Section 2.2.2, p. 4/D, diagonalizes the first-order field kernel and selects its largest-occupation mode. |
| Output state | Main Eq. (4), p. 4/D, calculates the selected mode's density matrix while tracing unwanted modes. This is a full-state calculation. |
| Large-system statement | Main Section 2.5, p. 8/H, discusses increasing emitter number while holding excitation number constant. |
| Receiver | SI II.3–II.4, pp. 7–9, Eqs. (S13)–(S23), uses the Kiilerich–Mølmer unidirectional virtual oscillator with prescribed capture coupling. |
| Shared collective channel | SI IV.2, p. 14, Eq. (S45), gives $`L_0=\sqrt{\Gamma_{1D}}S_-+g_0^*(t)a_0`$. |
| Number-map target | SI IV.4, pp. 16–17 and Fig. S7, fixes an even cat with $`\alpha=2`$, copies truncated, renormalized Fock coefficients into the Dicke basis, and varies $`N`$. |
| Input examples | SI VI, pp. 21–22, Eqs. (S76)–(S79), specifies prepared cat, GKP and squeezed states. |

## What follows for this project

After removing carrier rotation, matching rate and phase conventions and imposing the lossless symmetric case, the shared source has our ladder rates $`\gamma m(N-m+1)`$. The source cannot be dismissed as a different model. The coefficient-copying example also overlaps our canonical number target. The paper deserves direct credit for collective full-state transfer, number-dependent mode distortion and selected-mode capture.

The mode-selection procedure is applied to the radiation from a specified initial state. Thus its calculation allows the chosen waveform to depend on that preparation. Our optimization instead chooses one waveform before an arbitrary, possibly reference-entangled input in $`\mathcal C_M`$. A numerical method supporting arbitrary initial conditions is not itself a uniform accuracy guarantee with this quantifier order.

The virtual oscillator is an ideal calculation of a selected-mode state. It overlaps the allowed linear receiver; it does not establish a finite-bandwidth apparatus attaining every waveform. We found no adaptive or nonlinear recovery needed for the compared construction.

**Fidelity convention remains unresolved:** no explicit squared-versus-root fidelity definition was located in either inspected file. Their reported percentages are therefore not equated to this repository's squared entanglement fidelity. This does not prevent the construction comparison.

The fixed-cat sweep and constant-excitation discussion do not establish a growing-code minimax limit. No uniform emitted-isometry bound on $`\mathcal C_M`$, all-waveform common-receiver converse, or matching $`e^{-c^3/192}`$ critical law was found in these versions. Selected-input success is compatible with a failing worst-input guarantee.

**Outcome:** no subsumption or correction of the fixed theorem was established by this comparison. Its candidate additional contribution remains the controlled all-waveform, whole-code boundary and its separation from mean photon collection. The access gap is closed for the inspected versions; exhaustive priority, independent critical reading and a joint device realization remain separate obligations.
