# Project understanding map: 30 milestones

[Learning route](README.md) · [Kiilerich–Mølmer bridge](KIILERICH_MOLMER_BRIDGE.md) · [Scientific account](../science/README.md)

This map organizes the complete scientific story into exactly **30 milestones**.
Its understanding targets and dependencies are defined by the project and are common
to every reader, including an LLM.

The allocation is **12 background/preliminaries milestones** and **18
narrative/innovation milestones**. The background joins the collective spin,
traveling field and receiving channel into one precise transfer task. The narrative
needs more room to connect the controlled field approximation, the matching bounds,
the collection contrast and the physical resource consequences. Each phase moves
from local objects or arguments to an integrated account.

The single educational anchor is **Kiilerich and Mølmer, *Quantum interactions with
pulses of radiation* (2020)**. The [learning route](README.md) identifies its version
and sections; the [bridge](KIILERICH_MOLMER_BRIDGE.md) supplies notation translations,
worked examples and the additional project arguments. The science pages remain
authoritative for exact hypotheses and complete proofs. The milestones support
global understanding; specialist calculations remain in those sources.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M06 | Temporal modes, collective decay and the oscillator comparator |
| Background/preliminaries | M07–M12 | Receiver resources, collection, coherence and the complete operational question |
| Narrative/innovation | M13–M19 | Channel reduction, uniform approximation and the optimized boundary |
| Narrative/innovation | M20–M23 | Photon collection, a two-sector witness and a successful sparse comparator |
| Narrative/innovation | M24–M28 | Field structure, source controls, loss and finite capture resources |
| Narrative/innovation | M29–M30 | Attribution, verification and the complete scientific interpretation |

## Phase I: background/preliminaries

### M01 A temporal mode is an oscillator

**Central question.** What does it mean for a traveling pulse to carry a quantum state?

**Understanding target.** Use a normalized temporal envelope to define a bosonic mode operator. Distinguish the mode function from the occupation or quantum state in that mode, and distinguish one spatial channel from one temporal oscillator.

**Dependencies and story role.** None within this map. This identifies the local field object retained by the receiver.

**Conceptual connection.** A beam can occupy many mutually orthogonal pulse shapes even when it travels along one spatial path. The receiver selects an oscillator from that continuum.

**Sources.** KM Introduction and II A, especially Eq. (6); [bridge 1](KIILERICH_MOLMER_BRIDGE.md#1-the-quantum-pulse); [temporal normalization](../science/CONVENTIONS.md#temporal-modes-and-normalization).

### M02 Many photons in one mode

**Central question.** How does one pulse represent an arbitrary photon number?

**Understanding target.** Interpret a mode's Fock state and its normalized product wavefunction in labeled detection times. Distinguish a one-photon overlap amplitude from the squared overlap of two many-photon Fock states.

**Dependencies and story role.** M01. This relates a local pulse shape to the full state whose transfer will be judged.

**Conceptual connection.** A small one-photon mismatch is raised to a large power when all photons must occupy the same receiving mode. Product-wavefunction notation applies to a mode Fock state; the emitted collective field still needs its own derivation.

**Sources.** [Mode and fidelity conventions](../science/CONVENTIONS.md); [worked pulse-mismatch calculation](KIILERICH_MOLMER_BRIDGE.md#worked-calculation-a-nearly-matched-pulse).

### M03 The symmetric collective spin

**Central question.** What quantum state is stored before emission?

**Understanding target.** Identify the symmetric Dicke states and distinguish the physical atom count, the excitation number and the declared excitation cutoff. Explain the lowering matrix element and why a finite collective spin differs from a bosonic annihilation operator.

**Dependencies and story role.** M02. This supplies the source whose number amplitudes must enter the optical oscillator.

**Conceptual connection.** Small excitation density makes an individual ladder-rate correction small, but it does not yet control the fidelity of a complete emitted state or a whole code.

**Sources.** [Bridge 3](KIILERICH_MOLMER_BRIDGE.md#3-the-exact-source-is-a-finite-collective-spin); [source and target](../science/MODEL.md#source-output-normalization-and-target).

### M04 Vacuum Markov emission and waiting times

**Central question.** How does the collective lowering operator determine emission times?

**Understanding target.** Interpret the dissipator with jump operator $`\sqrt\gamma S_-`$, the population-decay rates and the half-rate decay of no-jump amplitudes. Translate physical time to the scaled clock $`\tau=N\gamma t`$ without losing the pulse-normalization factor.

**Dependencies and story role.** M01 and M03. This connects source dynamics to the field wavefunction.

**Conceptual connection.** A sequence of waiting-time amplitudes determines the emitted state. The vacuum-channel and complete-emission assumptions are part of that construction.

**Sources.** KM opening of Section II, Eq. (2); [one- and two-photon calculation](KIILERICH_MOLMER_BRIDGE.md#worked-calculation-one-photon-then-two); [time and rate conventions](../science/CONVENTIONS.md#source-time-and-rates).

### M05 The exact field is correlated

**Central question.** Why are collective photons not exactly independent copies of a pulse?

**Understanding target.** Relate ordered waiting times to the normalized symmetric labeled-time wavefunction. Identify its pair-time factor and account for ordering once, without adding an extra factorial.

**Dependencies and story role.** M02 and M04. This establishes the exact state that an approximation must control.

**Conceptual connection.** The two-photon calculation exposes temporal correlations already at finite atom number. Any later product-pulse description is a proved approximation, not an assumption about independent emissions.

**Sources.** [Source wavefunction](../science/MODEL.md#source-output-normalization-and-target); [bridge 3](KIILERICH_MOLMER_BRIDGE.md#3-the-exact-source-is-a-finite-collective-spin); [normalization details](../science/PROOF_DETAILS.md).

### M06 The successful oscillator comparator

**Central question.** Why can a linear oscillator emit an unknown state into one pulse?

**Understanding target.** Explain how a fixed linear decay law releases every initial Fock component into the same envelope and therefore preserves arbitrary superpositions. Compare its linear ladder rates with the finite-spin rates.

**Dependencies and story role.** M01–M05. This joins the pulse and source descriptions through a physical benchmark.

**Conceptual connection.** Number-dependent source dynamics can change the preferred temporal waveform. A known number can therefore be easier to transfer than an unknown superposition of possible numbers.

**Sources.** KM II A, Eqs. (4)–(9); [constant-rate oscillator example](KIILERICH_MOLMER_BRIDGE.md#1-the-quantum-pulse); [source comparison](../references/LAW_LEE_FULL_TEXT.md).

### M07 Capturing a selected output pulse

**Central question.** What state does the receiving oscillator contain?

**Understanding target.** Interpret the virtual output cavity as a representation of the selected traveling mode's reduced state. Distinguish a coupling amplitude from its squared population-decay rate, and explain why tracing other modes is unconditional.

**Dependencies and story role.** M01, M04 and M06. This gives the field-to-memory part of the transfer task.

**Conceptual connection.** The selected-mode state contains more information than its mean occupation. An ideal capture formula can require a singular onset coupling; a mathematical mode selection and a finite-control implementation need separate resource statements.

**Sources.** KM II C, Eqs. (17)–(19), and opening of II D; [bridge 2](KIILERICH_MOLMER_BRIDGE.md#2-the-receiving-oscillator); [receiver scope](../science/PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means).

### M08 The complete passive receiver class

**Central question.** Which apparatuses are included in the common-waveform optimization?

**Understanding target.** Reduce predetermined number-preserving linear processing with vacuum auxiliaries and one final retained oscillator to a normalized signal mode plus vacuum attenuation. Distinguish internal auxiliary cavities from additional retained outputs.

**Dependencies and story role.** M02 and M07. This states the resource boundary before comparing receivers.

**Conceptual connection.** An all-waveform bound includes elaborate passive networks in the specified class. Nonvacuum inputs, active operations, feedback to the source and nonlinear decoding require different models.

**Sources.** [Receiver definition](../science/MODEL.md#source-output-normalization-and-target); [resource conventions](../science/CONVENTIONS.md#receiver-resources); [bridge 2](KIILERICH_MOLMER_BRIDGE.md#2-the-receiving-oscillator).

### M09 One canonical map for an unknown input

**Central question.** What must remain fixed while the input varies?

**Understanding target.** State the canonical Dicke-number to oscillator-number map on the entire declared code. Allow the receiver to depend on known atom count and cutoff, while requiring the same waveform for all unknown amplitudes and number components.

**Dependencies and story role.** M03, M06 and M08. This joins source and receiver into an operational state-transfer task.

**Conceptual connection.** Matching a pulse separately to each known number or choosing a different target for every trial does not establish a uniform channel guarantee.

**Sources.** [Preserving an unknown state](KIILERICH_MOLMER_BRIDGE.md#preserving-an-unknown-state); [canonical target](../science/MODEL.md#source-output-normalization-and-target).

### M10 Mean collection and full-number success

**Central question.** Why does collecting nearly all photons fail to certify state transfer?

**Understanding target.** Distinguish the mean collected fraction from the probability that every photon occupies the selected mode. Explain the example with mean fraction $`p`$ and full-state fidelity $`p^m`$, and the finite-sector bounds relating these two quantities.

**Dependencies and story role.** M02, M05 and M07. This identifies the observable distinction central to the project.

**Conceptual connection.** Missing a small fraction of a growing photon population may leave a substantial probability of missing at least one photon. The illustrative product-state calculation must later be connected to the correlated collective field.

**Sources.** KM II B, Eqs. (13)–(15), for occupation modes; [bridge 4](KIILERICH_MOLMER_BRIDGE.md#4-photon-collection-is-not-the-transfer-objective); [four distinct quantities](../science/CONVENTIONS.md#four-quantities-that-must-not-share-a-label).

### M11 Coherence and an untouched reference

**Central question.** How is faithful transfer of quantum information assessed?

**Understanding target.** Interpret squared entanglement fidelity relative to the fixed number map, including an untouched reference entangled with the source. Explain the Kraus sum and why successful number-state tests alone do not protect coherences for an arbitrary channel.

**Dependencies and story role.** M07, M09 and M10. This strengthens an observable criterion into the required channel criterion.

**Conceptual connection.** A number-dependent phase can preserve every number-state fidelity while destroying a superposition. The reduction to sector overlaps therefore needs the actual positivity and number-lowering structure of this receiver.

**Sources.** [Coherence counterexample and channel explanation](KIILERICH_MOLMER_BRIDGE.md#preserving-an-unknown-state); [channel objective](../science/MODEL.md#reduction-of-the-channel-objective).

### M12 The complete operational question

**Central question.** Which source, input, receiver, target and error criterion are being compared?

**Understanding target.** Assemble the symmetric vacuum-channel source, arbitrary code input, predetermined passive receiver, canonical target and reference-inclusive fidelity into one model. Contrast that model with the easier goal of accurate mean-photon collection and the successful oscillator comparator.

**Dependencies and story role.** M01–M11. This synthesizes the background before the proof mechanism begins.

**Conceptual connection.** A proposed improvement must preserve the complete task to challenge its boundary. Retaining more modes, changing the encoding or learning the input changes what has been established.

**Sources.** [Model](../science/MODEL.md); [assumption register](../references/ASSUMPTIONS.md); [scientific reading route](../science/README.md).

## Phase II: narrative/innovation

### M13 Reducing the optimized channel to sector overlaps

**Central question.** Why is the worst-input fidelity exactly a minimum over number sectors here?

**Understanding target.** Use the positive diagonal vacuum-complement Kraus operator and the number-lowering remaining operators to derive a lower bound attained by a number input. Explain why replacing a complex waveform by its modulus permits the optimized reduction without discarding any channel outcomes.

**Dependencies and story role.** M05, M08, M11 and M12. This turns the operational question into the quantity used by the proof.

**Conceptual connection.** Positivity justifies this reduction for the optimized channel; it is not a general identification of basis fidelity with channel fidelity, nor a postselected no-loss process.

**Sources.** [Exact reduction](../science/MODEL.md#reduction-of-the-channel-objective); [bridge channel argument](KIILERICH_MOLMER_BRIDGE.md#preserving-an-unknown-state); [phase and endpoint details](../science/PROOF_DETAILS.md).

### M14 A matched pulse from a full-process comparison

**Central question.** How can a correlated emitted state be approximated without assuming independence?

**Understanding target.** Identify the normalized reference family $`f_a`$ with sector choice $`a_m=(m-1)/N`$. Follow the comparison between the reference and true counting-process intensities, its size-biased binomial identity and the resulting relative-entropy bound.

**Dependencies and story role.** M04, M05 and M13. This supplies the controlled approximation on which the geometric argument rests.

**Conceptual connection.** The reference process has independent pulse times; the true process need not. Relative entropy compares their complete detection-time laws before the approximation is used.

**Sources.** [Uniform matched-pulse approximation](../science/MATCHED_PULSES.md#uniform-individually-matched-pulse-approximation); [counting-process bound](../science/MATCHED_PULSES.md#bound-via-the-full-counting-process); [bridge 5](KIILERICH_MOLMER_BRIDGE.md#5-individually-matched-pulses-the-approximation-that-needs-proof).

### M15 Uniform control of the whole source map

**Central question.** Why does the approximation remain valid for an expanding unknown-state code?

**Understanding target.** Convert relative entropy to overlap using positive amplitudes and Jensen's inequality, then obtain a vector-error bound. Use orthogonality of different photon-number sectors to bound the source-isometry error by the largest sector error rather than a sum.

**Dependencies and story role.** M11 and M14. This upgrades individual pulse matching to a uniform comparison that can be used inside a minimax problem.

**Conceptual connection.** The same isometry control covers a reference-entangled input. Uniformity permits optimization and a minimum over growing codes; pointwise convergence alone would not.

**Sources.** [Matched-pulse error bound](../science/MATCHED_PULSES.md#uniform-individually-matched-pulse-approximation); [Jensen and orthogonality bridge](KIILERICH_MOLMER_BRIDGE.md#5-individually-matched-pulses-the-approximation-that-needs-proof); [probability conventions](../science/CONVENTIONS.md#probability-and-information-conventions).

### M16 Exact pulse geometry and cubic accumulation

**Central question.** Where does the scale $`M^3/N^2`$ come from?

**Understanding target.** Reparameterize the reference pulses by $`u=-\ln(1-a)`$, use the exact overlap kernel and identify its quadratic small-separation logarithm. Combine pulse displacement across the code with the many-photon overlap power.

**Dependencies and story role.** M02, M14 and M15. This connects a local one-photon geometry to a macroscopic transfer error.

**Conceptual connection.** The scalar coordinate $`u`$ is not KM's incoming pulse label. The cubic scale combines a squared small pulse difference with a growing photon number; its coefficient and optimality still require bounds.

**Sources.** [Exact pulse geometry](../science/MATCHED_PULSES.md#exact-pulse-geometry); [bridge 6](KIILERICH_MOLMER_BRIDGE.md#6-one-receiving-pulse-must-compromise); [notation conventions](../science/CONVENTIONS.md#temporal-modes-and-normalization).

### M17 Constructing a common compromise pulse

**Central question.** Which one waveform gives a uniform achievable guarantee?

**Understanding target.** Explain the choice $`a_*=(3M/4-1)/N`$ and the equal leading constraints at one-quarter and full cutoff. Follow the finite lower envelope with its explicit source-approximation error, including exact vacuum and single-excitation cases.

**Dependencies and story role.** M13, M15 and M16. This constructs the attainable side of the boundary.

**Conceptual connection.** Balancing $`x(x-3/4)^2`$ identifies the common pulse, while the finite uniform inequality justifies taking a worst-sector limit. A successful construction by itself cannot exclude a better waveform.

**Sources.** [Constructive common waveform](../science/COMMON_MODE_BOUNDARY.md#constructive-common-waveform); [finite lower envelope](../science/COMMON_MODE_BOUNDARY.md#a-finite-lower-envelope); [bridge 6](KIILERICH_MOLMER_BRIDGE.md#6-one-receiving-pulse-must-compromise).

### M18 A converse for every receiving waveform

**Central question.** Why can no waveform improve the critical limiting fidelity?

**Understanding target.** Use the projective-angle triangle inequality through an arbitrary receiver and the two constraining reference pulses. Keep the additive source error explicit to derive the finite upper envelope, including the case where that error already exceeds the overlap guarantee.

**Dependencies and story role.** M13, M15–M17. This turns a trial-pulse result into an optimization over the complete allowed class.

**Conceptual connection.** The argument does not assume an optimizer exists, restrict it to the reference-pulse family, or assume fidelity stays away from one. Complex waveforms do not evade the converse.

**Sources.** [All-waveform converse](../science/COMMON_MODE_BOUNDARY.md#converse-for-every-waveform); [finite endpoint argument](../science/PROOF_DETAILS.md#why-the-converse-uses-a-finite-inequality); [finite angle brackets](../science/COMMON_MODE_BOUNDARY.md#finite-brackets).

### M19 The sharp boundary and excitation budget

**Central question.** What do the matching bounds establish across excitation scales?

**Understanding target.** Derive the critical limit $`e^{-c^3/192}`$, subcritical success and supercritical failure for the full consecutive code. Use code monotonicity to translate the critical law into the asymptotic excitation budget at fixed target fidelity.

**Dependencies and story role.** M17 and M18. This integrates the core proof into its exact asymptotic conclusion.

**Conceptual connection.** A fixed positive critical ratio, a ratio tending to zero, a ratio tending to infinity and a target fidelity tending to one are distinct limits. The critical exponential is not an asserted asymptotic equality for every supercritical sequence.

**Sources.** [Common-mode boundary](../science/COMMON_MODE_BOUNDARY.md); [fixed-fidelity excitation budget](../science/INTERPRETATION.md#what-the-result-changes).

### M20 A separate bound for photon collection

**Central question.** Why does the mean collected fraction remain accurate over a larger range?

**Understanding target.** Use the fractional missed-number operator as a positive contraction to transfer a mean-collection estimate from the product reference to the exact field. Explain why the uniform sector bound extends by photon-number weighting to every nonvacuum code input.

**Dependencies and story role.** M10, M15 and M17. This supplies the second quantity needed for the physical contrast.

**Conceptual connection.** Number-preserving observables have no cross-number contributions. The collection ratio is undefined for a vacuum-only input, while its state transfer remains exact.

**Sources.** [Mean-collected-fraction proof](../science/PHOTON_COLLECTION.md#mean-collected-fraction); [observable-control details](../science/PROOF_DETAILS.md#6-photon-count-and-observable-control); [bridge 7](KIILERICH_MOLMER_BRIDGE.md#7-the-interface-boundary).

### M21 Low density does not guarantee a faithful interface

**Central question.** Can vanishing excitation density coexist with vanishing optimized transfer fidelity?

**Understanding target.** Combine the bounds along $`M=\lfloor N^{3/4}\rfloor`$: excitation density vanishes, one common mode collects an asymptotically complete mean fraction, and optimal worst-input canonical fidelity vanishes.

**Dependencies and story role.** M19 and M20. This makes the theorem's observable-versus-channel distinction explicit in one scaling example.

**Conceptual connection.** Failure of a worst-input guarantee does not say every input fails. The emitted field still retains the quantum information; the limitation concerns the specified one-oscillator interface.

**Sources.** [Collection separation](../science/PHOTON_COLLECTION.md); [physical interpretation](../science/INTERPRETATION.md#the-result); [bridge 7](KIILERICH_MOLMER_BRIDGE.md#7-the-interface-boundary).

### M22 Two populated sectors witness the obstruction

**Central question.** Does the limitation require a growing logical dimension?

**Understanding target.** Define the logical qubit on the populated numbers $`\lfloor M/4\rfloor`$ and $`M`$. Explain why the same construction and two-input converse give the critical limit, and why its low-density failure uses a direct angle argument.

**Dependencies and story role.** M17–M19 and M21. This isolates the physical excitation resource from logical dimension.

**Conceptual connection.** Restricting a code can improve its worst fidelity, so full-code supercritical failure alone does not prove failure of a sparse subcode. The two-sector proof supplies the needed direct obstruction.

**Sources.** [Two-sector witness](../science/TWO_SECTOR_WITNESS.md); [all-waveform angle argument](../science/COMMON_MODE_BOUNDARY.md#converse-for-every-waveform).

### M23 A successful sparse code and a finite witness

**Central question.** Which sparse-code comparison reveals what causes the conflict?

**Understanding target.** Explain why vacuum plus one known populated number transfers asymptotically faithfully for subextensive cutoff, while two distinct populated numbers can impose incompatible pulse requirements. Interpret the finite two-sector construction and its analytic upper bracket without calling a balanced trial a finite-size optimum.

**Dependencies and story role.** M14, M18 and M22. This separates the mechanism from an overbroad claim about all sparse encodings.

**Conceptual connection.** Vacuum is common to every mode; it creates no competing waveform requirement. Numerical evaluations, analytic ceilings and a universal optimization statement establish different things.

**Sources.** [Finite witness and vacuum control](../science/TWO_SECTOR_WITNESS.md); [finite brackets](../science/COMMON_MODE_BOUNDARY.md#finite-brackets); [verification guide](../verification/README.md).

### M24 The leading error occupies a tangent mode

**Central question.** Where does the state information go when the receiving mode is insufficient?

**Understanding target.** Identify the normalized tangent mode to the pulse family, its orthogonality to the common pulse and the controlled two-mode approximation at critical scaling. Relate the Poisson count of tangent-mode photons to the probability that none leave the selected mode.

**Dependencies and story role.** M15, M16, M19 and M21. This gives a field-level explanation of the boundary.

**Conceptual connection.** A nearly two-mode encoding can preserve information in the field while a one-mode receiver loses fidelity. The occupied direction depends on excitation number, so a fixed linear rotation does not compress the whole code into one canonical oscillator.

**Sources.** [Tangent-mode structure](../science/PHYSICAL_SCOPE.md#b-the-leading-mismatch-has-a-simple-structure); [bridge 9](KIILERICH_MOLMER_BRIDGE.md#9-field-structure-controls-and-the-complete-interpretation). KM Section III supplies optional multimode context.

### M25 What scalar source shaping preserves

**Central question.** Can slowing or rephasing collective emission remove the optimized mismatch?

**Understanding target.** Explain why the stated scalar rate and phase controls act as the same one-particle isometry on every emitted pulse under complete emission. Distinguish preserved pulse geometry from changes in physical duration and receiver-control requirements.

**Dependencies and story role.** M04, M08, M16 and M19. This identifies the scope of an important control comparison.

**Conceptual connection.** An unbounded accumulated emission clock is required. A finite clock leaves residual excitation, and number-dependent ladder engineering is outside the scalar-control statement.

**Sources.** [Scalar source pulse shaping](../science/PHYSICAL_SCOPE.md#c-scalar-source-pulse-shaping); [bridge interpretation](KIILERICH_MOLMER_BRIDGE.md#9-field-structure-controls-and-the-complete-interpretation).

### M26 Optimizing in the presence of transmission loss

**Central question.** When does ordinary photon loss hide the common-mode penalty?

**Understanding target.** Incorporate mode-independent pure loss through the factor $`\eta^m`$ in each sector. Interpret the joint critical exponent, the shift in optimal common waveform and the threshold at which the highest-number loss ceiling determines the leading optimum.

**Dependencies and story role.** M13, M15 and M17–M19. This extends the same canonical task under one specified additional channel.

**Conceptual connection.** The code experiences accumulated loss $`-M\log\eta`$, not merely single-photon transmission. The all-waveform converse remains necessary after the pulse is reoptimized.

**Sources.** [Loss-competition proof and finite certificates](../science/LOSS_COMPETITION.md); [bridge 8](KIILERICH_MOLMER_BRIDGE.md#8-loss-and-finite-capture-after-the-ideal-theorem).

### M27 Atomic loss and microscopic realization

**Central question.** Which effective loss assumptions survive a concrete source implementation?

**Understanding target.** Distinguish inaccessible atomic decay during the cascade from loss of an already emitted field. Interpret the useful-channel branching product and shifted analytic ladder parameter, then compare a fixed effective rate ratio with the bandwidth and duration assumptions of microscopic cavity models.

**Dependencies and story role.** M03, M04, M19 and M26. This connects an effective-model result to its physical implementation conditions.

**Conceptual connection.** The shifted ladder parameter does not add physical atoms. Collected-photon simulations do not alone control the emitted-field approximation uniformly on an expanding quantum code.

**Sources.** [Independent atomic loss](../science/PHYSICAL_SCOPE.md#d-independent-atomic-loss); [bandwidth and duration](../science/PHYSICAL_SCOPE.md#e-bandwidth-and-duration); [source assumptions](../references/ASSUMPTIONS.md).

### M28 Finite capture has a code-dependent cost

**Central question.** How can the ideal receiving mode be approached with finite controls?

**Understanding target.** Follow onset regularization and time truncation to the unconditional whole-code capture bound. Track both the accumulated attenuation and discarded pulse tail, and translate scaled duration and coupling rate back to physical units.

**Dependencies and story role.** M07–M09, M17, M25 and M26. This joins the ideal theorem with an explicit receiver error and resource budget.

**Conceptual connection.** Finite resources exist for each finite code, while accuracy on growing codes requires shrinking tail and attenuation errors. The construction permits changing coupling and duration bounds and does not establish a fixed slew-rate or modulation-bandwidth guarantee.

**Sources.** [Finite receiving window](../science/PHYSICAL_SCOPE.md#a-finite-receiving-window-on-the-same-code); [finite-capture example](KIILERICH_MOLMER_BRIDGE.md#8-loss-and-finite-capture-after-the-ideal-theorem); [receiver checks](../verification/README.md).

### M29 Attribution and the strength of the evidence

**Central question.** Which ingredients are inherited, and what establishes each conclusion here?

**Understanding target.** Separate known cascade, waveform, occupation-optimization and capture results from the controlled uniform common-code optimization. Distinguish analytical proofs, finite numerical checks, reference agreement and source-reading evidence.

**Dependencies and story role.** M12–M28. This connects the scientific conclusions to their sources and verification routes.

**Conceptual connection.** An occupation optimum or a successful selected-state transfer can coexist with a failed canonical worst-input guarantee. Passing finite suites supports the checked identities and implementations; it does not replace a uniform proof or establish exhaustive priority.

**Sources.** [Prior-work comparison](../references/COMPARISON.md); [Law–Lee comparison](../references/LAW_LEE_FULL_TEXT.md); [Tziperman comparison](../references/TZIPERMAN_FULL_TEXT.md); [claim map](../science/CLAIM_EVIDENCE_MAP.md); [verification guide](../verification/README.md).

### M30 The complete interface story

**Central question.** What does the optimized boundary change about treating a collective spin as an oscillator?

**Understanding target.** Explain the chain from number-dependent collective decay through uniformly controlled pulse geometry to the common-waveform boundary. Join that result to near-complete mean collection, the logical-qubit witness, the fixed-fidelity excitation budget and the capture/loss qualifications.

**Dependencies and story role.** M12 and M19–M29. This synthesizes the narrative into the full contribution and its domain of validity.

**Conceptual connection.** State accuracy depends on the complete source, encoding, receiver and error criterion. The full field retains the information; the proved limitation belongs to the predetermined passive one-oscillator canonical interface, with the exact physical and asymptotic conditions stated in its sources.

**Sources.** [Scientific account](../science/README.md); [interpretation and excitation budget](../science/INTERPRETATION.md); [claim and evidence map](../science/CLAIM_EVIDENCE_MAP.md); [complete learning bridge](KIILERICH_MOLMER_BRIDGE.md).
