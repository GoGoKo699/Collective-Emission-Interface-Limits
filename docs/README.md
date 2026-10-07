# Reading guide

[Project overview](../README.md) · [Tutorial-to-theorem bridge](../REVIEW.md) · [Proof](../research/THEOREM.md)

The single external teaching anchor is **Kiilerich and Mølmer, Quantum interactions with
pulses of radiation (2020)**: [arXiv:2003.04573v1](https://arxiv.org/pdf/2003.04573v1).
The route below uses the section and equation labels in that 15-page author version.
It is a tutorial-style review-and-method article, not a textbook. The original
[three-option comparison](../literature/TUTORIAL_OPTIONS.md) records the choice; the other
sources are references, not additional prerequisites.

The owner reconfirmed this single-source choice on 6 October 2026. A reader who
knows ordinary quantum mechanics can use the sequence below to reach the physical
statement, then decide how deeply to inspect its proof. Studying the source alone
does not supply the sharp boundary: the project-specific steps are taught here.

## A guided route

| Stage | Read | Check your understanding |
|---|---|---|
| 1. A pulse carries a state | KM Introduction and II A; [bridge 1–2](../REVIEW.md#1-the-quantum-pulse) | Can one fixed envelope carry both a one-photon state and a superposition of number states? |
| 2. The source is a finite spin | [Bridge 3](../REVIEW.md#3-the-exact-source-is-a-finite-collective-spin), including the one- and two-photon calculation | Why does the two-photon wavefunction contain a term depending on both detection times? |
| 3. State the transfer task | KM II B–C and the opening of II D; [bridge 4](../REVIEW.md#4-photon-collection-is-not-the-transfer-objective) | Why can 99% mean photon collection coexist with much lower state fidelity? Why must one pulse serve every input? |
| 4. Understand the boundary | [Bridge 5–7](../REVIEW.md#5-individually-matched-pulses-the-approximation-that-needs-proof), then [theorem](../research/THEOREM.md) | Which estimate justifies the product-pulse approximation, and which argument excludes every better common waveform? |
| 5. Interpret the physical resources | [Bridge 8](../REVIEW.md#8-loss-and-finite-capture-after-the-ideal-theorem), then the linked loss and capture bounds | Why must loss and capture tolerances improve with the excitation cutoff? |

The worked calculations in the bridge answer these questions. Stages 1–3 establish
the model and the observable distinction. Stage 4 reaches the result; Stage 5
explains its supporting physical qualifications. KM Section III is optional
context for retaining more than one mode, which changes the transfer task.

## Start with the source's physical organization

| Read in Kiilerich–Mølmer | What to carry forward | Where it enters here |
|---|---|---|
| Introduction and the start of Section II | A traveling pulse is not a discrete cavity eigenmode; the local system has a master equation and an input–output field | [Bridge: the quantum pulse](../REVIEW.md#1-the-quantum-pulse) |
| Section II A, especially Eqs. (4)–(9) | A virtual cavity can release an arbitrary quantum state in a specified envelope | The successful linear-oscillator comparator |
| Section II B, Eqs. (13)–(15) | Intensity, two-time correlation and occupation-eigenmode analysis | [Bridge: collection versus transfer](../REVIEW.md#4-photon-collection-is-not-the-transfer-objective) |
| Section II C, Eqs. (17)–(19) | A downstream virtual cavity captures a selected pulse and gives its reduced quantum state | [Bridge: the receiving oscillator](../REVIEW.md#2-the-receiving-oscillator) |
| Opening of Section II D | When there is no incident quantum pulse, omit the virtual input cavity | Our source starts in a stored atomic state and emits into vacuum |
| Section III, as optional supporting context | Several selected output modes can be retained jointly | The [two-mode error explanation](../research/PHYSICAL_SCOPE.md#b-the-leading-mismatch-has-a-simple-structure), not a new decoder task |

Read Sections II B and II C as different questions, not competing methods. The tutorial
already supplies full selected-mode states and recognizes that an occupation-optimal mode
need not optimize another property. Those capabilities are inherited. Our added question
is whether one receiver works **uniformly before the input is known**.

The later photon-blockade and thermal-input applications are not needed for this
vacuum-channel result. Their additional Hamiltonians and resources do not become part
of our theorem merely because they occur in the anchor.

## What the local bridge supplies

[REVIEW.md](../REVIEW.md) specializes the source to the symmetric Dicke ladder, fixes the
canonical number map, and explains the unconditional fidelity calculation. It then
connects the exact correlated emission to the individually matched pulses and the
common-waveform converse. Source-derived pulse/capture statements and project-specific
proof steps are identified separately.

To start, assume ordinary quantum mechanics with density matrices, creation and
annihilation operators, and basic calculus. The bridge explains the dissipator,
reference-system fidelity and entropy-to-overlap step. Checking the full proof also
uses elementary probability, relative entropy and asymptotic estimates; its
counting-process comparison is written in [Theorem, Section 3](../research/THEOREM.md#3-a-uniform-individually-matched-pulse-approximation).
These are local proof obligations, not an unstated second external course.

| Supplied by the tutorial | Supplied by this repository |
|---|---|
| Traveling-mode operators and virtual emission/capture cavities | Exact finite-spin ladder and correlated emitted wavefunction |
| Occupation modes and full selected-mode quantum states | One receiver for the entire unknown input space, including a reference |
| A framework for single- and multiple-output pulse calculations | Uniform product approximation, all-waveform converse and sharp excitation scale |
| Ideal pulse-capture construction | Code-dependent finite-capture bounds and the optimized loss competition |

The right column describes what this learning route must explain locally. It is
not a list of novelty claims: inherited Dicke and receiver results retain their
attributions in the bridge and literature comparisons.

## Translate notation before comparing formulas

| Anchor notation | This repository | Important distinction |
|---|---|---|
| Local system operator $`\hat c`$ | Collective lowering operator $`S_-`$ | It is not replaced by a bosonic annihilator in the exact source |
| Selected outgoing pulse $`v(t)`$ | Receiving pulse $`f(t)`$ | It is fixed for the entire input space |
| Virtual output oscillator $`\hat a_v`$ | One retained memory oscillator | Its reduced state is the receiving channel's output |
| Coupling amplitude $`g_v(t)`$ | Capture amplitude, with rate $`\kappa(t)=\lvert g_v(t)\rvert^2`$ | An amplitude is not a population-decay rate |
| Physical time $`t`$ | $`\tau=N\gamma t`$ in the exact ladder proof | Include the square-root factor when rescaling a normalized pulse |

The complete [convention map](../research/CONVENTIONS.md) also distinguishes the anchor's
pulse labels $`u,v`$ from the scalar coordinate $`u=-\ln(1-a)`$ used later in the proof.
Neither occurrence of $`u`$ denotes a new physical input to our vacuum source.

## Repository map

| Need | Read |
|---|---|
| Relevance, search terms and authoritative sources for an automated reader | [LLM guide](../llms.txt) |
| The compact physical account | [Story](../research/STORY.md) |
| Claims, proof dependencies and the boundary of research closure | [Claim and evidence map](../research/CLAIM_EVIDENCE_MAP.md) |
| Exact model, uniform approximation and all-waveform theorem | [Theorem](../research/THEOREM.md) |
| The correction and its finite-bound replacement | [Proof audit](../research/PROOF_AUDIT.md) |
| Logical-qubit witness and successful sparse comparator | [Two-sector note](../research/TWO_SECTOR_WITNESS.md) |
| Receivers, second mode, loss, rates and bandwidth | [Physical scope](../research/PHYSICAL_SCOPE.md) |
| When transmission loss masks the common-mode limitation | [Loss competition](../research/LOSS_COMPETITION.md) |
| Inherited ingredients and closest comparisons | [Background](../literature/BACKGROUND.md), [direct comparison](../literature/COMPARISON.md), [bibliography](../literature/REFERENCES.bib) |
| Dated additional predecessor and recent-source checks | [Prewriting source comparison](../literature/PREWRITING_SEARCH_2026_10_05.md) |
| What the assumptions have and have not established | [Assumptions](../literature/ASSUMPTIONS.md), [preparation evidence](../literature/PREPARATION_EVIDENCE.md) |
| Review and evidence boundaries | [Reading checklist](../research/CRITICAL_READING.md), [status](../STATUS.md), [reproduction policy](../provenance/REPRODUCTION_POLICY.md) |

## At the end of this route

A reader should be able to explain why a mode is not a photon, why mean collection and
canonical transfer differ, why independently excellent pulses need not share one receiving
mode, and why the theorem must optimize over every waveform. They should also know what
additional receivers or encodings the theorem does not restrict.

The completed [Tziperman comparison](../literature/TZIPERMAN_FULL_TEXT.md) and remaining
external critical reading are recorded in the [work order](../work_orders/CURRENT.md).
The [sanity-check record](../research/SANITY_CHECK_2026_10_05.md) separates the internal
review from that external task; readers need not reconstruct the exploratory history.

For the repository's role and discussion details, see [Purpose and contact](../README.md#purpose-and-contact).
