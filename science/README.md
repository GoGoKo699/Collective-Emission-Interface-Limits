# Scientific account

[Project overview](../README.md) · [Learning route](../learning/README.md) · [30 milestones](../learning/MILESTONES.md) · [Verification](../verification/README.md)

The question is when a weakly excited collective spin can serve as an oscillator
for transferring an unknown quantum state. Near-complete mean-photon collection
and faithful canonical transfer into one retained oscillator impose different
requirements. The scientific account develops their optimized separation for one
fixed collective source and one predetermined passive receiver.

## Specialist reading route

| Read | Scientific role |
|---|---|
| [Model](MODEL.md) and [conventions](CONVENTIONS.md) | Fix the collective ladder, emitted-state normalization, canonical number target, reference-inclusive fidelity and passive receiver class. |
| [Matched pulses](MATCHED_PULSES.md) | Control the product-pulse approximation uniformly and derive the exact pulse-overlap kernel. |
| [Common-mode boundary](COMMON_MODE_BOUNDARY.md) | Prove the constructive lower bound and all-waveform converse, including finite envelopes and the critical limit. |
| [Photon collection](PHOTON_COLLECTION.md) | Bound the mean collected fraction and exhibit the low-density separation from channel fidelity. |
| [Two-sector witness](TWO_SECTOR_WITNESS.md) | Expose the obstruction with two populated number levels and distinguish the vacuum-plus-number comparator. |
| [Physical scope](PHYSICAL_SCOPE.md) and [loss competition](LOSS_COMPETITION.md) | Derive finite-capture resources, the tangent-mode mechanism, scalar-control invariance and the stated loss limits. |
| [Interpretation](INTERPRETATION.md) | Connect the theorem to a fixed-fidelity excitation budget and the physical distinction between collection and transfer. |

The [claim and evidence map](CLAIM_EVIDENCE_MAP.md) joins the result statements to
their proof locations and supporting suites. [Proof details](PROOF_DETAILS.md)
expose normalization factors, phase restrictions, uniformity and endpoint arguments.

## Proof dependencies

| Conclusion | Required ingredients |
|---|---|
| Exact optimized channel objective | Positive emitted amplitudes; one retained passive mode; the number-lowering Kraus structure; a pointwise-modulus comparison for complex pulses. |
| Uniform matched-pulse approximation | The exact cascade; a full counting-process relative-entropy bound; positive-amplitude Hellinger control; orthogonal output number sectors. |
| Optimized common-mode boundary | Uniform source-state control; the exact kernel; a common constructive pulse; a projective-angle converse valid for every waveform. |
| Photon-collection separation | The matched-pulse error and a positive-contraction estimate for the fractional missed number; no product assumption about the exact photons. |
| Two-sector critical law | The same constructive pulse and a converse that already uses only the two populated constraining sectors. |
| External-loss critical law | The mode-independent pure-loss objective; uniform field approximation; a scalar minimax certificate and an all-waveform angle bound. |

The canonical model includes all number amplitudes and coherences and allows an
external reference. Its complete output field retains the input information.
The limitation concerns transfer into the stated single retained oscillator.
Additional retained modes, nonlinear decoding and source-changing controls alter
the physical task. The [assumption register](../references/ASSUMPTIONS.md) and
[physical scope](PHYSICAL_SCOPE.md) state the consequential premises and resource
requirements.

## Attribution

The emitted cascade, conventional exponential overlap, nonlinear-emission mode dependence and passive-capture framework are prior results [P1–P4]. The $`N^{2/3}`$ scale follows from the cubic mismatch. The theorem gives its all-waveform, whole-code, uniform optimization and the observable/channel distinction.

The [Law–Lee comparison](../references/LAW_LEE_FULL_TEXT.md) credits mean-occupation
optimization, the oscillator comparator, dominant few-mode behavior and the
semiclassical pulse. It distinguishes that occupation objective from the uniform
common-code fidelity optimized here. The [prior-art register](../references/PRIOR_ART.md)
gives the source-by-source attribution.

## Primary sources

[P1] V. Paulisch, *Waveguide Quantum Electrodynamics*, dissertation (2018), Chapter 1. https://edoc.ub.uni-muenchen.de/22151/1/Paulisch_Vanessa.pdf

[P2] N. Yamamoto and M. R. James, *Zero-dynamics principle for perfect quantum memory in linear networks*, arXiv:1403.1698. https://arxiv.org/abs/1403.1698

[P3] M. Khanahmadi et al., *Multimode character of quantum states released from a superconducting cavity*, Physical Review Research 5, 043071 (2023). https://research.chalmers.se/publication/538258/file/538258_Fulltext.pdf

[P4] H. I. Nurdin, M. R. James, and N. Yamamoto, *Perfectly capturing traveling single photons of arbitrary temporal wavepackets with a single tunable device*, arXiv:1609.05643 (2016). https://arxiv.org/abs/1609.05643

[P5] C. K. Law and S. K. Y. Lee, *Dynamic photon-mode selection in Dicke superradiance*, Physical Review A 75, 033813 (2007). https://doi.org/10.1103/PhysRevA.75.033813
