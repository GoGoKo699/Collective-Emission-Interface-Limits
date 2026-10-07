# Questions for a separate critical reading

**Updated 5 October 2026. No external report has been received.** This is a checklist for the fixed result in [THEOREM.md](THEOREM.md), not a request to extend the physical model. Mathematical and attribution objections should identify a precise proof location, correction, counterexample or source construction. Passing numerical checks alone is not an answer to an all-code or all-waveform question.

## Mathematical checks

1. **Normalization and fidelity convention.** In Sections 1–2, does the labeled emission-time wavefunction have the same normalization as the product-mode Fock state? Verify the ordered-domain factor explicitly. Does the vacuum-complement Kraus operator give the unconditional worst-input entanglement fidelity, including an untouched reference? Are all other Kraus contributions properly retained rather than postselected away?

2. **Positive-waveform reduction.** Does replacing an arbitrary complex receiving waveform by its pointwise modulus suffice for the optimized channel objective, rather than only the number-state overlaps? Check the direction of both inequalities and the attainment of the lower bound on a number state. Distinguish a phase convention from an input-dependent correction.

3. **Uniform state approximation.** In Section 3, verify the direction of the relative entropy, the counting-process intensities, the size-biased binomial identity, and the positive lower-rate bound. Treat the zero-survivor endpoint by continuity. Does the Hellinger argument bound vectors, not just probability densities? Why is the entire-code error the largest sector error rather than the sum? Does this remain valid after adjoining a reference?

4. **Joint limit and unrestricted converse.** In Sections 4–5, supply a uniform remainder over the discrete code when $`M/N^{2/3}`$ tends to a positive constant. Does the arbitrary-waveform angle inequality retain that accuracy after the $`m`$th roots? Make explicit how sequences with limiting fidelity zero or one are treated. The supercritical conclusion for the full consecutive code should follow by restricting to a fixed-critical subcode, not by extrapolating an asymptotic formula outside its proven regime.

5. **Photon collection versus state transfer.** In Section 6, check that the positive operator is a contraction separately in each fixed-number sector. Does the square-root estimate avoid assuming convergence of an unbounded photon-number moment from trace-distance convergence? Verify the extension as a photon-number-weighted average, including mixed and number-coherent inputs. The vacuum has no defined photon fraction but transfers trivially.

6. **The logical-qubit witness.** In [TWO_SECTOR_WITNESS.md](TWO_SECTOR_WITNESS.md), check that the restricted two-number channel has the same critical converse. Do not infer its supercritical limit merely by monotonicity of the full code. Preserve the successful vacuum-plus-one-populated-number comparator and the distinction between fixed logical dimension and growing physical energy.

## Physical and attribution checks

The receiver in [PHYSICAL_SCOPE.md](PHYSICAL_SCOPE.md) retains one oscillator after predetermined passive linear processing of a fixed emitted field. Determine whether any step inadvertently permits feedback into the source, nonvacuum auxiliaries, conditioning on the input number, or nonlinear decoding. The ideal supremum need not be attainable at a fixed control bandwidth or duration.

Compare the actual claim with the sources in [PRIOR_ART.md](../literature/PRIOR_ART.md): an optimized common waveform for a growing code is not automatically the same problem as a dominant mean-occupation mode of one selected state. Conversely, a change of fidelity objective does not prove novelty. An equation-level subsumption by existing work would be a substantive outcome, not something to evade by changing terminology.

The source audit is conditional on its own rate model. Confirm that an effective-size parameter is not being interpreted as additional physical atoms, and that cavity photon-collection checks are not presented as a uniform emitted-field theorem. The fixed-rate and fixed-microscopic-device scaling families must remain distinct.

The [loss-competition consequence](LOSS_COMPETITION.md) adds only prescribed,
mode-independent vacuum attenuation. Check that its arbitrary-waveform converse
survives the uniform approximation before taking the limit, and that the loss ceiling
is not mistaken for disappearance of mode mismatch. The finite-window bound in
PHYSICAL_SCOPE.md must charge both truncation and capture error across the code;
its finite amplitudes do not establish fixed modulation bandwidth.

## A separate significance judgment

Does the all-waveform converse change how a specialist would assess a collective source feeding one preconfigured linear memory, beyond the already known accumulation of number-dependent mode mismatch? The fixed-fidelity excitation budget in [STORY.md](STORY.md) states the operational consequence, but is only an inversion of the existing critical law. Do not count it as a second result.

Distinguish three judgments: the theorem is correct; it is not subsumed by the inspected sources; its added content matters physically. The first two do not imply the third. Identify a concrete interface claim or design decision affected by the common-receiver guarantee, or explain why the uniform optimization is mainly a technical completion. Do not impute an incorrect uniform-transfer claim to predecessors who studied selected states. A negative significance judgment is a valid outcome even without a counterexample to the proof.

## Expected output of a reading

A useful report should separate mathematical validity, inherited results, possible new contributions, and physical relevance. State exactly which sections were read, any unavailable full text, and the scope of every objection. Do not mark an assumption register complete by counting component papers as joint devices.

The present repository does not contain a completed independent review, a hardware realization, or exhaustive priority certification. No invitation or correspondence has been sent as part of preparing this checklist.
