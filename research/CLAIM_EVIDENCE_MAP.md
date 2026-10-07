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
possibly reference-entangled input. It is not a capacity theorem or an impossibility
of decoding with extra quantum resources.

## 2. Claims, dependencies and evidence

| Role | Claim | Analytic source | Executed-check coverage and limitation |
|---|---|---|---|
| Task reduction | Positive receiving pulses reduce the optimized unconditional worst-input entanglement fidelity to the smallest number-sector overlap; arbitrary complex competitors cannot improve it. | [Theorem, Section 2](THEOREM.md#2-reduction-of-the-channel-objective) | Suites 03 and 08 exercise reference inputs, passive capture and phase controls. They do not replace the Kraus proof. |
| Essential lemma | Each number sector has an individually matched product-pulse approximation, uniformly across the code for $`M=o(N)`$. | [Theorem, Section 3](THEOREM.md#3-a-uniform-individually-matched-pulse-approximation) | Suites 01, 02 and 08 check normalization, entropy, overlap and the sector-maximum norm. The exact field remains correlated. |
| Main theorem | A constructive common pulse and an all-waveform converse give the same critical fidelity and the subcritical/supercritical alternatives. | [Theorem, Sections 4–5](THEOREM.md#4-exact-pulse-geometry), [recorded correction](PROOF_AUDIT.md) | Suites 02 and 08 test finite envelopes and endpoint controls. Large-system scalar evaluations are not large-system simulations. |
| Main physical contrast | One common mode collects a fraction tending to one throughout $`M=o(N)`$, a larger range than faithful uniform transfer. | [Theorem, Section 6](THEOREM.md#6-mean-photon-collection-has-a-larger-domain-of-validity) | Suites 05 and 08 exercise bounded-operator and photon-weighted estimates. Collection alone does not certify the channel. |
| Scope witness | Two populated number levels suffice to witness the critical obstruction; vacuum plus one populated number is a successful comparator. | [Two-sector proof](TWO_SECTOR_WITNESS.md) | Suite 07; fixed logical dimension still requires growing excitation number. |
| Error explanation | At critical scaling the leading leakage occupies a tangent mode and has a Poisson count limit. | [Physical scope, B](PHYSICAL_SCOPE.md#b-the-leading-mismatch-has-a-simple-structure) | Suite 04; this supplies no nonlinear decoder. |
| Operational corollary | A fixed target fidelity determines an asymptotic excitation cutoff. | [Story](STORY.md#what-the-result-changes) | Follows analytically by monotonicity and strict margins; no finite-size or shrinking-target inversion is asserted. |
| Loss boundary | Mode-independent external loss changes the optimal pulse and can mask the mode-mismatch penalty. | [Loss competition](LOSS_COMPETITION.md) | [Supplementary checks](../tools/check_loss_competition.py) compare independent scalar optimization, finite cascade calculations and finite bounds. This is a supporting scope result. |
| Capture resources | Finite window and onset regularization give an explicit whole-code error budget. | [Physical scope, A](PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means) | Existing suite 03 tests the conservative form and unconditional capture dynamics. No fixed control bandwidth is guaranteed. |

The proof chain is source normalization, positive-channel reduction, uniform field
approximation, pulse geometry, and matching finite bounds. The photon-fraction result
uses a separate bounded-observable estimate. Neither the finite examples nor the
implementation discussion is a premise of the ideal theorem.

## 3. Loss and finite capture

For uniform pure loss with $`-M\log\eta_N\to\lambda`$ at critical code scaling,
the [loss-competition proof](LOSS_COMPETITION.md) gives an additional mismatch
exponent precisely below $`\lambda=c^3/48`$. Above that
threshold the highest-number loss ceiling fixes the leading optimum. This comparison
uses the already specified loss channel; it does not assert a general noisy-source
optimization.

The finite-capture derivation also makes the ideal supremum operationally precise:
each finite code admits arbitrarily close finite-window, finite-coupling capture,
while growing-code accuracy demands improving truncation and capture tolerances.
The required duration and coupling can grow. A discontinuous switch does not provide
a bound on modulation bandwidth or slew rate.

## 4. What the literature establishes

The [background dossier](../literature/BACKGROUND.md) supplies the inherited optics,
and the [direct comparison](../literature/COMPARISON.md) identifies the closest tasks.
The [source search record](../literature/PREWRITING_SEARCH_2026_10_05.md)
documents the inspected predecessors and the date-limited coverage. Source versions and reading
depth are recorded; a search result is not treated as a full-text comparison.

The cascade, conventional cubic mismatch, number-dependent pulses, occupation
optimization, few-mode descriptions and selected-state capture are inherited.
The candidate contribution is the controlled uniform common-receiver optimization
and its separation from photon-fraction accuracy. An existing paper need not use
our terminology to subsume that result. Conversely, selected-target or metrological
success is compatible with failure of our canonical worst-input task.

The absence of a subsuming theorem in inspected sources is a scoped finding. It does
not certify exhaustive priority, and no claimed contradiction of those authors is
needed for the result.

## 5. Premises and claims deliberately left conditional

| Item | Status for the present theoretical claim | What would be needed for a device claim |
|---|---|---|
| Symmetric identical emitters, known atom number and vacuum Markov collective decay | Explicit source premises, supported as community models in the [assumption register](../literature/ASSUMPTIONS.md) | Error bounds for inhomogeneity, calibration, delay and omitted interactions |
| Arbitrary unknown input in the excitation code | Input promise of the channel task | An input-independent encoding preserving an external reference, with its cost and error |
| One predetermined passive retained oscillator | Specified receiver resource with established capture formalism | Compatible couplings, control bandwidth, duration and loss |
| Independent atomic decay and cavity elimination | Separate audits with explicit effective-rate assumptions | A controlled full-field limit for one consistent microscopic scaling family |
| Joint realization | Not claimed | A demonstration or design meeting the premises together |

The last column describes extensions outside the conditional theorem. Known-target
preparation does not supply the unknown-input promise, and intensity data alone do
not establish a uniform field bound.
The [physical scope](PHYSICAL_SCOPE.md) and [preparation evidence](../literature/PREPARATION_EVIDENCE.md)
remain the detailed source of these qualifications.

## 6. Interpretation and records

The [physical account](STORY.md) explains the consequence of the uniform boundary.
[Scope extensions](CRITICAL_READING.md) distinguish future realization work from
that result. The [proof audit](PROOF_AUDIT.md) preserves the endpoint correction;
[verification provenance](../provenance/README.md) records the numerical evidence.
