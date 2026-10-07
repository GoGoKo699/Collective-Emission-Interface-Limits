# Bounded literature refresh before manuscript work

**5 October 2026.** This internal search tests the fixed claim in
[THEOREM.md](../research/THEOREM.md): symmetric Markov collective decay, the
canonical number map, one passive retained oscillator with a waveform chosen
before an unknown input, and a uniform growing-code fidelity boundary. It supplements
the [existing comparisons](COMPARISON.md). It is neither a systematic review nor
an exhaustive priority certificate.

**Outcome:** no subsumption was located in the constructions inspected below.
Three sources strengthen attribution and limit interpretation. Established work
already provides full atom-to-light quantum-state mappings, few-mode full-state
approximations, and distinctions between photon occupation and useful information.
The candidate contribution remains the optimized uniform channel boundary for the
specified source and receiver. These comparisons do not establish its broader
scientific importance.

## Search record and stopping rule

Searches used two web indexes, then primary arXiv, publisher and institutional
copies. The cutoff is 5 October 2026; actual arXiv version histories, rather than
search-engine relative dates or regenerated PDF datelines, determine version dates.
Discovery queries included:

- `"collective emission" "temporal modes" quantum state transfer`
- `"Dicke superradiance" "fidelity" "mode"`
- `"superradiance" "N" "2/3" photon mode`
- `Dicke superradiance emitted quantum state temporal modes fidelity 2025 2026`
- `collective emission single mode Fock state fidelity uniform approximation`
- `superradiant emitted photon wavefunction single temporal mode approximation fidelity N two thirds`
- `Dicke state transfer waveform independent excitation number fidelity quantum memory`
- `collective spontaneous emission worst case entanglement fidelity single mode`
- `superradiance multiphoton wavefunction mean field norm convergence Holstein Primakoff`

The first index's broad quoted queries returned substantial irrelevant material;
they are not treated as negative evidence. The second index and exact-title searches
located the candidates. Exact-title follow-ups covered the three substantive
comparisons and the screened papers below. Recent-query windows of 730 or 900 days
were supplemented by unrestricted searches and backward citation following.
Perarnau-Llobet et al. was specifically selected as a missing direct comparison;
its reference 10 led to Porras–Cirac. Belliardo et al. previously had only a
supplementary mention here.

The pass stops after resolving the relevant construction differences of these
three sources and screening the additional close titles. No citation-count
threshold or unsuccessful search is used to establish originality. No outside
researcher was contacted.

## Three construction comparisons

### Porras–Cirac: quantum-state mapping after bosonic approximation

D. Porras and J. I. Cirac, *Collective generation of quantum states of light by
entangled atoms*, Physical Review A **78**, 053816 (2008),
[DOI](https://doi.org/10.1103/PhysRevA.78.053816),
[arXiv:0808.2732v1](https://arxiv.org/abs/0808.2732v1), submitted 20 August 2008.

Read the introduction, Section II's mapping, Section IV's ensemble and multiphoton
construction, Section V's entangled-state application, and Appendix B in the
15-page [author PDF](https://arxiv.org/pdf/0808.2732). This is a targeted full-text
construction reading, not verification of every spatial calculation. PDF pages 2
and 10 were rendered.

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

### Perarnau-Llobet et al.: few-mode states and their overlaps

M. Perarnau-Llobet, A. González-Tudela and J. I. Cirac, *Multimode Fock states with
large photon number: effective descriptions and applications in quantum metrology*,
Quantum Science and Technology **5**, 025003 (2020),
[DOI](https://doi.org/10.1088/2058-9565/ab6ce5),
[arXiv:1910.03323v2](https://arxiv.org/abs/1910.03323v2), revised 18 February 2020.

Read the published [institutional PDF](https://pure.mpg.de/rest/items/item_3215481_3/component/file_3215508/content):
Sections 1–6 and Appendix A.5; other recurrence subsections were located, not
independently rederived. The file has 23 PDF pages including a cover. PDF pages 4
and 8 were rendered. The 19-page arXiv PDF was also checked for source identification;
section locations here refer to the published copy.

Section 2, Eqs. (6)–(7), covers the same collective ladder and exact emitted state.
Section 4.2, Eqs. (14)–(19), selects modes by occupation. Section 4.4, Eqs. (22)–(24),
and Appendix A.5 calculate full-state projections into two or three modes. This is
not occupation-only work. Their explicit superradiant examples start fully inverted.

No common-waveform minimax over a growing excitation code is supplied. Their
few-mode description and distinction between photon fraction and state overlap
must receive credit; the present uniform norm/converse statement remains separate.

### Belliardo et al.: an information-optimal mode can contain few photons

F. Belliardo, A. Chu, M. Koppenhöfer and A. A. Clerk, *Extracting information from
a superradiant burst using simple measurements*,
[arXiv:2603.13130v2](https://arxiv.org/abs/2603.13130v2), revised 31 March 2026.

Read Sections I–VII and the task/claim discussion in Appendices I–J of the
28-page [author PDF](https://arxiv.org/pdf/2603.13130); their full appendix proofs
were not rederived. Pages 6, 8 and 22 were rendered, with page 8 visually inspected
for the fitted scaling qualification.

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

## Additional titles screened

| Source and access depth | Reason not promoted to a central comparison |
|---|---|
| Yadav–Yavuz, *Quantum statistics of single-mode radiation emitted by superradiant Dicke states*, [arXiv:2508.09962v1](https://arxiv.org/abs/2508.09962v1), 13 August 2025; published Physical Review A **112**, 063713, [DOI](https://doi.org/10.1103/gfl1-dq9m). Read the [HTML](https://arxiv.org/html/2508.09962v1) model and photon-statistics construction, Eqs. (1), (21), (25)–(26). | The assumed field is one closed Tavis–Cummings oscillator. Its unitary dynamics are not emission into a Markov continuum followed by temporal-mode selection. |
| Liedl et al., *Observation of Superradiant Bursts in a Cascaded Quantum System*, Physical Review X **14**, 011020 (2024), [DOI](https://doi.org/10.1103/PhysRevX.14.011020), [arXiv:2211.08940v2](https://arxiv.org/abs/2211.08940v2), 26 June 2023. Read the [HTML](https://arxiv.org/html/2211.08940v2) experimental setup, first-order coherence, model and conclusion. | The measured temporal coherence is relevant context, but Eqs. (2)–(4) include a directional cascaded Hamiltonian and free-space losses. It is not a validation or counterexample for this repository's symmetric lossless source. |
| Holzinger et al., *Solving Dicke superradiance analytically: A compendium of methods*, [arXiv:2503.10463v3](https://arxiv.org/abs/2503.10463v3), 19 March 2025. Read the [HTML](https://arxiv.org/html/2503.10463v3) setup, Section I and the trajectory construction. | Same collective ladder; Eqs. (12)–(13) extend population solutions to any initial Dicke state or mixture. No outgoing-field common-code theorem was identified in that inspected construction. |
| Holzinger et al., *Symbolic Quantum-Trajectory Method for Multichannel Dicke Superradiance*, [arXiv:2511.02390v4](https://arxiv.org/abs/2511.02390v4), 27 August 2026. Read the [HTML](https://arxiv.org/html/2511.02390v4) model and stated results. | Competing collective branches of multilevel emitters and initially inverted populations; a different question. This was a scope screen, not a full-paper subsumption audit. |

## Fetch provenance and limits

All three substantive PDFs were retrieved on 5 October 2026. They remain outside
the repository; neither source PDFs nor page images are redistributed here.

| Inspected file | Bytes | SHA-256 |
|---|---:|---|
| Porras–Cirac arXiv PDF | 431085 | `b31f3e002dec561c7f3ad531577935dffb74f31ba3146336c0883fd3f461e864` |
| Perarnau-Llobet et al., published institutional PDF | 1649733 | `2f0de2efe07087e2379a8d5bf5ce99c823f2bdb4dfcb9f384a3e639040fb7298` |
| Belliardo et al., arXiv v2 PDF | 8428462 | `ff4466c567b74349491de676e0b94e027fe3c86e2f21fdda757fc8eedc12771b` |

Belliardo's versioned HTML and one versioned PDF web request failed; the unversioned
PDF succeeded and visibly identifies v2. The institutional Perarnau-Llobet web
parser failed, but a direct PDF retrieval succeeded. Porras–Cirac's PDF has a
regenerated 2018 dateline while its margin and arXiv history identify the 2008 v1;
the dateline is not evidence of a later version. No final publisher copy of that
paper was compared line by line. Likewise, regenerated dates in arXiv HTML were
not treated as revision dates.

The scoped outcome is **survival of the fixed candidate claim against these
additional constructions**, with stronger attribution and explicit limits on the
physical interpretation. Independent critical reading, exhaustive priority and a
combined device realization are not supplied by this search.
