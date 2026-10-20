# State mapping, few-mode descriptions and parameter readout

These comparisons locate the collective interface theorem among related quantum-optical
tasks. They preserve the source versions and reading scope documented on 5 October 2026.
The result being compared is the [uniform common-waveform boundary](../science/COMMON_MODE_BOUNDARY.md)
for the [specified source, code and receiver](../science/MODEL.md).
The [direct comparison](COMPARISON.md) treats the closest single-mode transfer and
occupation results.

## Porras–Cirac: quantum-state mapping after bosonic approximation

D. Porras and J. I. Cirac, *Collective generation of quantum states of light by
entangled atoms*, Physical Review A **78**, 053816 (2008),
[DOI](https://doi.org/10.1103/PhysRevA.78.053816),
[arXiv:0808.2732v1](https://arxiv.org/abs/0808.2732v1), submitted 20 August 2008.

The comparison uses the introduction, Section II's mapping, Section IV's ensemble
and multiphoton construction, Section V's entangled-state application, and Appendix B
in the 15-page [author version](https://arxiv.org/pdf/0808.2732v1). Its scope is the
state-mapping construction, rather than every spatial calculation in the paper.

Section II A, Eq. (1), assumes small per-atom excitation before replacing spin
operators by bosons. Eqs. (4)–(7) and (19) then map general atomic quantum states
through a linear transformation. Section IV C, Eqs. (75)–(77), treats an
$`M`$-photon target and purity under $`M\ll N`$; Appendix B concerns averaging atomic
positions.

This deserves credit for full-state transfer, including entangled states. The
inspected construction supplies no finite-spin, growing-code norm error or
all-waveform converse. Our interpretation is that uniform accuracy needs its own
estimate; our theorem does not invalidate their different spatial and
Lambda-system protocols.

## Perarnau-Llobet et al.: few-mode states and their overlaps

M. Perarnau-Llobet, A. González-Tudela and J. I. Cirac, *Multimode Fock states with
large photon number: effective descriptions and applications in quantum metrology*,
Quantum Science and Technology **5**, 025003 (2020),
[DOI](https://doi.org/10.1088/2058-9565/ab6ce5),
[arXiv:1910.03323v2](https://arxiv.org/abs/1910.03323v2), revised 18 February 2020.

The comparison uses Sections 1–6 and Appendix A.5 of the published
[institutional copy](https://pure.mpg.de/rest/items/item_3215481_3/component/file_3215508/content),
which has 23 PDF pages including a cover. Equation and section locations below refer
to that copy. The 19-page arXiv version supplies a second bibliographic identifier.
The reading supports the stated mode and state-projection constructions; it does not
independently rederive the other recurrence subsections.

Section 2, Eqs. (6)–(7), covers the same collective ladder and exact emitted state.
Section 4.2, Eqs. (14)–(19), selects modes by occupation. Section 4.4, Eqs. (22)–(24),
and Appendix A.5 calculate full-state projections into two or three modes. This is
not occupation-only work. Their explicit superradiant examples start fully inverted.

No common-waveform minimax over a growing excitation code is supplied. Their
few-mode description and distinction between photon fraction and state overlap
must receive credit; the present uniform norm/converse statement remains separate.

## Belliardo et al.: an information-optimal mode can contain few photons

F. Belliardo, A. Chu, M. Koppenhöfer and A. A. Clerk, *Extracting information from
a superradiant burst using simple measurements*,
[arXiv:2603.13130v2](https://arxiv.org/abs/2603.13130v2), revised 31 March 2026.

The comparison uses Sections I–VII and the task discussion in Appendices I–J
of the 28-page [author version v2](https://arxiv.org/pdf/2603.13130v2). It identifies
the measurement objective and scaling statements; the full appendix proofs are
not independently rederived.

Equation (2) at zero spin interaction has our collective dissipator. Equation (3)
encodes a local parameter around full inversion. Eqs. (25)–(27) optimize the
homodyne signal-to-noise ratio over temporal modes. Section IV C, Eq. (31), finds
sublinear occupation of that mode numerically; the reported fractional exponent
near $`-0.37`$ is a fit, not our sharp $`N^{2/3}`$ code boundary. Appendix I explicitly
distinguishes this optimization from optimizing the selected mode's quantum Fisher
information.

The task is parameter readout, not canonical unknown-state transfer. Our theorem
does not imply that useful metrological information disappears. Occupation,
parameter-estimation performance and channel fidelity are distinct objectives.

## Related source models

| Source and access depth | Relation to the stated interface model |
|---|---|
| Yadav–Yavuz, *Quantum statistics of single-mode radiation emitted by superradiant Dicke states*, [arXiv:2508.09962v1](https://arxiv.org/abs/2508.09962v1), 13 August 2025; published Physical Review A **112**, 063713, [DOI](https://doi.org/10.1103/gfl1-dq9m). Read the [HTML](https://arxiv.org/html/2508.09962v1) model and photon-statistics construction, Eqs. (1), (21), (25)–(26). | The assumed field is one closed Tavis–Cummings oscillator. Its unitary dynamics are not emission into a Markov continuum followed by temporal-mode selection. |
| Liedl et al., *Observation of Superradiant Bursts in a Cascaded Quantum System*, Physical Review X **14**, 011020 (2024), [DOI](https://doi.org/10.1103/PhysRevX.14.011020), [arXiv:2211.08940v2](https://arxiv.org/abs/2211.08940v2), 26 June 2023. Read the [HTML](https://arxiv.org/html/2211.08940v2) experimental setup, first-order coherence, model and conclusion. | The measured temporal coherence is relevant context, but Eqs. (2)–(4) include a directional cascaded Hamiltonian and free-space losses. It is not a validation or counterexample for this repository's symmetric lossless source. |
| Holzinger et al., *Solving Dicke superradiance analytically: A compendium of methods*, [arXiv:2503.10463v3](https://arxiv.org/abs/2503.10463v3), 19 March 2025. Read the [HTML](https://arxiv.org/html/2503.10463v3) setup, Section I and the trajectory construction. | Same collective ladder; Eqs. (12)–(13) extend population solutions to any initial Dicke state or mixture. No outgoing-field common-code theorem was identified in that inspected construction. |
| Holzinger et al., *Symbolic Quantum-Trajectory Method for Multichannel Dicke Superradiance*, [arXiv:2511.02390v4](https://arxiv.org/abs/2511.02390v4), 27 August 2026. Read the [HTML](https://arxiv.org/html/2511.02390v4) model and stated results. | Competing collective branches of multilevel emitters and initially inverted populations; a different question. This was a scope screen, not a full-paper subsumption audit. |

## Scope of the comparison

The three construction comparisons distinguish bosonic atom-to-light mapping,
few-mode full-state projection and parameter estimation from canonical transfer
of every state in a growing code. The related-source table uses narrower model
and result readings where stated. These construction differences do not amount
to an exhaustive novelty claim.

Source-version identification and retrieval evidence are preserved in the
[dated source record](../provenance/source-records/LITERATURE_SEARCH_2026_10_05.md).
The source and receiver remain those of the [model](../science/MODEL.md); their
physical implementation requirements are in [physical scope](../science/PHYSICAL_SCOPE.md).
