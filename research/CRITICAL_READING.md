# Established results and open questions

The [theorem](THEOREM.md) and [claim and evidence map](CLAIM_EVIDENCE_MAP.md)
record the answers established within the fixed source, canonical target and
one-oscillator receiver model. The questions below concern the remaining limits
of that account.

## Established mathematical answers

| Topic | Answer and proof location |
|---|---|
| Normalization and unconditional fidelity | The labeled-time wavefunction and product-mode Fock state use the same full-domain normalization, including the ordered-domain factor. The Kraus argument retains every discarded-field outcome and permits an untouched reference. See [theorem, Sections 1–2](THEOREM.md#1-source-output-normalization-and-target) and [proof audit](PROOF_AUDIT.md). |
| Positive receiving waveform | Replacing a complex waveform by its modulus cannot decrease any squared number overlap. For a nonnegative waveform, their minimum equals its worst-input squared entanglement fidelity. This proves the optimized reduction, without asserting it for each fixed complex waveform. See [theorem, Section 2](THEOREM.md#2-reduction-of-the-channel-objective). |
| Uniform state approximation | The counting-process relative-entropy estimate and positive-amplitude Hellinger bound control state vectors. Orthogonal number sectors make the whole-code error the largest sector error; the bound also holds with a reference. See [theorem, Section 3](THEOREM.md#3-a-uniform-individually-matched-pulse-approximation). |
| Joint limit and unrestricted converse | The finite angle bounds keep the approximation error explicit and handle the zero- and unit-fidelity endpoints. The supercritical full-code conclusion follows by restriction to a fixed-critical subcode. See [theorem, Sections 4–5](THEOREM.md#4-exact-pulse-geometry) and the [endpoint correction](PROOF_AUDIT.md). |
| Photon collection | A sectorwise bounded-operator estimate extends by photon-number weighting to mixed and number-coherent inputs. It does not infer an unbounded moment from trace-distance convergence. The vacuum transfers trivially and has no photon fraction. See [theorem, Section 6](THEOREM.md#6-mean-photon-collection-has-a-larger-domain-of-validity). |
| Two-sector witness | Two populated number levels witness the critical obstruction. Vacuum plus one populated number is a successful comparator; fixed logical dimension does not mean fixed physical excitation. See [two-sector proof](TWO_SECTOR_WITNESS.md). |

The [loss-competition proof](LOSS_COMPETITION.md) already gives the optimized
bound for prescribed mode-independent vacuum attenuation. The
[finite-capture bound](PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means)
already charges both truncation and attenuation across the code. Neither establishes
fixed modulation bandwidth or a compatible microscopic device.

The [source comparisons](../literature/COMPARISON.md) identify inherited cascade,
pulse-shape, occupation and capture results. No subsumption was found in the
inspected constructions; that finding does not establish exhaustive priority.
The receiver restriction and the distinction between effective-rate and microscopic
scaling families remain explicit in [physical scope](PHYSICAL_SCOPE.md).

## Questions that remain open

1. **Unknown-input preparation.** Can an input-independent encoder load the growing
   symmetric excitation code in a source realization compatible with this model,
   while preserving an external reference, with uniform error bounds and accounted
   resource costs? The
   [preparation evidence](../literature/PREPARATION_EVIDENCE.md) covers related
   constructions, not this complete input resource.
2. **Compatible device resources.** Is there one microscopic scaling family with a
   controlled full emitted-field approximation that meets preparation, calibration,
   loss, control bandwidth and duration requirements together? The
   [physical-scope analysis](PHYSICAL_SCOPE.md) treats component limits; their joint
   compatibility is not established.
3. **Practical significance.** Which concrete interface design or operating decision
   benefits from the all-waveform uniform guarantee beyond the familiar accumulation
   of number-dependent mode mismatch? The [excitation budget](STORY.md) states the
   asymptotic consequence, but is a corollary of the critical law rather than another
   result or a hardware specification.

A mathematical objection to an established answer should identify a precise proof
location, correction or counterexample. A subsumption claim should identify the
existing source construction. Numerical checks, scoped source comparisons and
physical significance support different judgments. Further research should address
one of these concrete gaps or a new objection under the [current work order](../work_orders/CURRENT.md).
