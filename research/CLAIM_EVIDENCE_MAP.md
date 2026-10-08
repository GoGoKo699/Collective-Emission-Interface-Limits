# Claim and evidence map

This map links the theoretical claims to their proofs, numerical checks and physical
assumptions. The source, canonical target and allowed receiver are defined in the
[theorem](THEOREM.md).

## 1. The central result

A symmetric collective source can deliver almost all its mean photon number to one
preconfigured receiving mode while failing to transfer its unknown excitation code
faithfully to that mode. The limitation survives optimization over every common
waveform. For complete ideal collective decay, uniform canonical transfer succeeds
below the excitation scale $`N^{2/3}`$ and fails above it; the critical limit is
$`\exp(-c^3/192)`$ when $`M/N^{2/3}\to c>0`$.

The complete output field retains the input information. The theorem concerns a fixed
canonical number map into one passive retained oscillator, with an unknown and
possibly reference-entangled input.

## 2. Claims, dependencies and evidence

| Role | Claim | Analytic source | Executed-check coverage |
|---|---|---|---|
| Task reduction | Positive receiving pulses reduce the optimized unconditional worst-input entanglement fidelity to the smallest number-sector overlap; arbitrary complex competitors cannot improve it. | [Theorem, Section 2](THEOREM.md#2-reduction-of-the-channel-objective) | Suites 03 and 08 exercise reference inputs, passive capture and phase controls. |
| Essential lemma | Each number sector has an individually matched product-pulse approximation, uniformly across the code for $`M=o(N)`$. | [Theorem, Section 3](THEOREM.md#3-a-uniform-individually-matched-pulse-approximation) | Suites 01, 02 and 08 check normalization, entropy, overlap and the sector-maximum norm. The exact field remains correlated. |
| Main theorem | A constructive common pulse and an all-waveform converse give the same critical fidelity and the subcritical/supercritical alternatives. | [Theorem, Sections 4–5](THEOREM.md#4-exact-pulse-geometry) | Suites 02 and 08 test finite envelopes and endpoint controls through scalar evaluations. |
| Main physical contrast | One common mode collects a fraction tending to one throughout $`M=o(N)`$, a larger range than faithful uniform transfer. | [Theorem, Section 6](THEOREM.md#6-mean-photon-collection-has-a-larger-domain-of-validity) | Suites 05 and 08 exercise bounded-operator and photon-weighted estimates. Collection alone does not certify the channel. |
| Scope witness | Two populated number levels suffice to witness the critical obstruction; vacuum plus one populated number is a successful comparator. | [Two-sector proof](TWO_SECTOR_WITNESS.md) | Suite 07; fixed logical dimension still requires growing excitation number. |
| Error explanation | At critical scaling the leading leakage occupies a tangent mode and has a Poisson count limit. | [Physical scope, B](PHYSICAL_SCOPE.md#b-the-leading-mismatch-has-a-simple-structure) | Suite 04 tests the tangent-mode expansion and leakage distribution. |
| Operational corollary | A fixed target fidelity determines an asymptotic excitation cutoff. | [Story](STORY.md#what-the-result-changes) | Follows analytically by monotonicity and strict margins at fixed target fidelity. |
| Loss boundary | Mode-independent external loss changes the optimal pulse and can mask the mode-mismatch penalty. | [Loss competition](LOSS_COMPETITION.md) | [Supplementary checks](../tools/check_loss_competition.py) compare independent scalar optimization, finite cascade calculations and finite bounds. This is a supporting scope result. |
| Capture resources | Finite window and onset regularization give an explicit whole-code error budget. | [Physical scope, A](PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means) | Suite 03 tests the conservative form and unconditional capture dynamics. Duration and coupling requirements depend on the code size. |

The proof chain is source normalization, positive-channel reduction, uniform field
approximation, pulse geometry, and matching finite bounds. The photon-fraction result
uses a separate bounded-observable estimate.

## 3. Loss and finite capture

For uniform pure loss with $`-M\log\eta_N\to\lambda`$ at critical code scaling,
the [loss-competition proof](LOSS_COMPETITION.md) gives an additional mismatch
exponent precisely below $`\lambda=c^3/48`$. Above that
threshold the highest-number loss ceiling fixes the leading optimum. This comparison
uses the specified mode-independent pure-loss channel.

The finite-capture derivation also makes the ideal supremum operationally precise:
each finite code admits arbitrarily close finite-window, finite-coupling capture,
while growing-code accuracy demands improving truncation and capture tolerances.
The required duration and coupling can grow. A discontinuous switch does not provide
a bound on modulation bandwidth or slew rate.

## 4. What the literature establishes

The [background dossier](../literature/BACKGROUND.md) supplies the inherited optics,
and the [direct comparison](../literature/COMPARISON.md) identifies the closest tasks.
The [source search record](../literature/PREWRITING_SEARCH_2026_10_05.md)
identifies the inspected predecessors, source versions and reading depth.

The cascade, conventional cubic mismatch, number-dependent pulses, occupation
optimization, few-mode descriptions and selected-state capture are inherited.
The result here is the controlled uniform common-receiver optimization and its
separation from photon-fraction accuracy. Selected-target or metrological success
is compatible with failure of the canonical worst-input task.

## 5. Model assumptions

| Component | Specification |
|---|---|
| Source | Identical emitters in the symmetric ladder, known atom number and complete decay into one vacuum Markov channel |
| Input | An arbitrary state in the declared excitation code, possibly entangled with an external reference |
| Target and receiver | The canonical number map into one oscillator retained after predetermined passive processing with vacuum auxiliaries |
| Supporting loss models | External mode-independent attenuation and independent atomic decay under their respective stated effective-rate assumptions |

The [assumption register](../literature/ASSUMPTIONS.md) relates these premises to
the literature. The [physical account](STORY.md) explains their consequences, and
[verification provenance](../provenance/README.md) records the numerical evidence.
