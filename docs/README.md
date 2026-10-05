# Reading guide

[Project overview](../README.md) · [Tutorial-to-theorem bridge](../REVIEW.md) · [Proof](../research/THEOREM.md)

The single external teaching anchor is **Kiilerich and Mølmer, Quantum interactions with
pulses of radiation (2020)**: [arXiv:2003.04573v1](https://arxiv.org/pdf/2003.04573v1).
The route below uses the section and equation labels in that 15-page author version.
It is a tutorial-style review-and-method article, not a textbook. The original
[three-option comparison](../literature/TUTORIAL_OPTIONS.md) records the choice; the other
sources are references, not additional prerequisites.

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

The only assumed background is ordinary quantum mechanics with density matrices,
creation and annihilation operators, and basic calculus. The needed dissipator,
reference-system fidelity and entropy-to-overlap step are explained locally. The full
counting-process estimate is in the proof; understanding the bridge does not substitute
for checking it.

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
