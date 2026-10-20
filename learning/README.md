# Learning route

[Project overview](../README.md) · [30 milestones](MILESTONES.md) · [Local bridge](KIILERICH_MOLMER_BRIDGE.md) · [Scientific account](../science/README.md)

The learning route follows one question: **when does a collective spin transfer an
unknown quantum state faithfully into one preconfigured receiving oscillator?**
It begins with pulses, emission and capture, then connects the controlled field
approximation to the optimized boundary and its physical meaning.

The [30-milestone map](MILESTONES.md) defines the common understanding targets and
their dependencies. Its 12 background milestones assemble the source, field and
channel model; its 18 narrative milestones join the proof, collection contrast,
witnesses and implementation resources. The
[local bridge](KIILERICH_MOLMER_BRIDGE.md) supplies worked calculations and explains
the steps between the anchor and this project's result. Specialists can go directly
to the [scientific reading route](../science/README.md).

## One selected educational anchor

**A. H. Kiilerich and K. Mølmer, *Quantum interactions with pulses of radiation*,
Physical Review A 102, 023717 (2020).**

[Author version, arXiv:2003.04573v1](https://arxiv.org/abs/2003.04573v1) ·
[15-page PDF](https://arxiv.org/pdf/2003.04573v1) ·
[HTML text](https://arxiv.org/html/2003.04573v1) ·
[Published article](https://doi.org/10.1103/PhysRevA.102.023717)

This tutorial-style review-and-method article is abbreviated **KM** below. The
section and equation pointers use the pinned author version. Its virtual input and
output cavities provide the physical language of a pulse carrying a quantum state
and an oscillator retaining a selected output mode. The collective-spin
specialization, channel objective and uniform estimates are supplied locally.

Start with ordinary quantum mechanics, density matrices, creation and annihilation
operators, and basic calculus. The bridge explains the dissipator, reference-system
fidelity and entropy-to-overlap step. The full proof also uses elementary
probability, relative entropy and asymptotic estimates; its
[counting-process comparison](../science/MATCHED_PULSES.md#bound-via-the-full-counting-process)
is written in the scientific account.

## Read from local objects to the complete result

| Part of the map | Read | Understanding developed |
|---|---|---|
| M01–M06: pulse and source | KM Introduction and II A; [bridge 1](KIILERICH_MOLMER_BRIDGE.md#1-the-quantum-pulse) and [bridge 3](KIILERICH_MOLMER_BRIDGE.md#3-the-exact-source-is-a-finite-collective-spin) | A pulse is one oscillator; finite-spin ladder rates generate a correlated emitted field; the linear oscillator provides a successful comparator. |
| M07–M12: complete transfer task | KM II B–C and opening of II D; [bridge 2](KIILERICH_MOLMER_BRIDGE.md#2-the-receiving-oscillator) and [bridge 4](KIILERICH_MOLMER_BRIDGE.md#4-photon-collection-is-not-the-transfer-objective) | One receiving mode must preserve the unknown number amplitudes, coherences and reference correlations; mean occupation alone does not certify that task. |
| M13–M19: matching proof bounds | [Bridge 5–6](KIILERICH_MOLMER_BRIDGE.md#5-individually-matched-pulses-the-approximation-that-needs-proof); [matched pulses](../science/MATCHED_PULSES.md); [common-mode boundary](../science/COMMON_MODE_BOUNDARY.md) | A full-process estimate makes the product comparison uniform, and an arbitrary-waveform angle converse matches the constructive critical fidelity. |
| M20–M23: physical separation and witnesses | [Bridge 7](KIILERICH_MOLMER_BRIDGE.md#7-the-interface-boundary); [photon collection](../science/PHOTON_COLLECTION.md); [two-sector witness](../science/TWO_SECTOR_WITNESS.md) | Low density and near-complete mean collection coexist with vanishing worst-input fidelity; two populated levels already expose the obstruction. |
| M24–M28: field and apparatus resources | [Bridge 8–9](KIILERICH_MOLMER_BRIDGE.md#8-loss-and-finite-capture-after-the-ideal-theorem); [physical scope](../science/PHYSICAL_SCOPE.md); [loss competition](../science/LOSS_COMPETITION.md) | The tangent mode locates the leading error; scalar shaping, loss, duration and capture coupling retain their distinct assumptions and costs. |
| M29–M30: scientific synthesis | [Interpretation](../science/INTERPRETATION.md); [claim map](../science/CLAIM_EVIDENCE_MAP.md); [source comparison](../references/COMPARISON.md); [verification](../verification/README.md) | The result gives an excitation budget at fixed target fidelity, with explicit attribution, evidence and scope. |

The milestone map provides finer dependencies within these groups. Its final
background milestone assembles the operational question; its final narrative
milestone joins the result, proof mechanism and physical qualifications.

## Use the anchor's physical organization

| Read in Kiilerich–Mølmer | Carry forward | Where it enters here |
|---|---|---|
| Introduction and opening of Section II | Traveling fields have a continuum of modes; the local quantum system has a master equation and an input–output field. | [The quantum pulse](KIILERICH_MOLMER_BRIDGE.md#1-the-quantum-pulse) |
| Section II A, Eqs. (4)–(9) | A virtual cavity releases its initial quantum state in a specified envelope. | The linear-oscillator comparator in M06 |
| Section II B, Eqs. (13)–(15) | Intensity, two-time correlation and occupation-eigenmode analysis. | [Collection and transfer](KIILERICH_MOLMER_BRIDGE.md#4-photon-collection-is-not-the-transfer-objective) |
| Section II C, Eqs. (17)–(19) | A downstream virtual cavity captures a selected pulse and represents its reduced state. | [The receiving oscillator](KIILERICH_MOLMER_BRIDGE.md#2-the-receiving-oscillator) |
| Opening of Section II D | Omit the virtual input cavity when no incident quantum pulse is prepared. | The stored collective state emits into a vacuum channel. |
| Section III, optional supporting context | Several selected output modes can be retained jointly. | [Tangent-mode structure](../science/PHYSICAL_SCOPE.md#b-the-leading-mismatch-has-a-simple-structure), with a different retained-mode resource |

KM already supplies selected-mode quantum states and recognizes that optimizing
occupation need not optimize another property. Those capabilities are inherited.
The additional question here is whether one receiver succeeds uniformly before
the input is known. Its later photon-blockade and thermal-input applications are
not prerequisites for the vacuum-channel model.

## Translate notation before comparing formulas

| Anchor notation | This repository | Meaning to retain |
|---|---|---|
| Local system operator $`\hat c`$ | Collective lowering operator $`S_-`$ | Keep the finite-spin matrix elements in the exact source. |
| Selected outgoing pulse $`v(t)`$ | Receiving pulse $`f(t)`$ | Choose it once for the entire input code. |
| Virtual output oscillator $`\hat a_v`$ | One retained memory oscillator | Its reduced state is the receiving channel's output. |
| Coupling amplitude $`g_v(t)`$ | Amplitude with rate $`\kappa(t)=\lvert g_v(t)\rvert^2`$ | Distinguish amplitude from population-decay rate. |
| Physical time $`t`$ | Scaled clock $`\tau=N\gamma t`$ | Include the square-root prefactor when rescaling a normalized pulse. |
| Input/output pulse labels $`u(t),v(t)`$ | Scalar coordinate $`u=-\ln(1-a)`$ only in the pulse-family proof | The scalar coordinate does not introduce an incident pulse to the vacuum source. |

The [convention map](../science/CONVENTIONS.md) also fixes the labeled-time
normalization, squared-fidelity convention and distinction between photon fraction
and channel accuracy.

## What the bridge supplies locally

| Anchor foundation | Local connection |
|---|---|
| Traveling-mode operators and virtual cavities | The exact Dicke ladder and one- and two-photon emission calculation |
| Occupation modes and selected-mode quantum states | The common canonical map, reference-inclusive fidelity and coherence example |
| A framework for pulse-state calculations | The full-process relative-entropy comparison and uniform source-isometry control |
| Ideal output capture | The all-waveform converse, collection separation and code-dependent finite-capture bound |

The [bridge](KIILERICH_MOLMER_BRIDGE.md) distinguishes these source-derived
foundations from the project arguments. Its nearly matched pulse example has 99%
mean collection but about 36.6% full-state fidelity for 100 photons; it is an
illustrative product-state calculation, while the scientific proof controls the
actual correlated source. The coherence example explains why the optimized
channel reduction requires its positive Kraus structure.

This is one educational source, with research references retained for attribution
and proof dependencies. The locally supplied material includes inherited Dicke and
receiver results as well as this project's conclusions; it is not a list of
novelty claims.

## Repository map

| Reader's question | Authoritative route |
|---|---|
| What is the physical contribution? | [Interpretation](../science/INTERPRETATION.md) |
| What exactly is optimized? | [Model](../science/MODEL.md) and [conventions](../science/CONVENTIONS.md) |
| What proves the boundary? | [Matched pulses](../science/MATCHED_PULSES.md), [common-mode proof](../science/COMMON_MODE_BOUNDARY.md) and [proof details](../science/PROOF_DETAILS.md) |
| What separates collection from transfer? | [Collection estimate](../science/PHOTON_COLLECTION.md) and [two-sector witness](../science/TWO_SECTOR_WITNESS.md) |
| What resources does physical capture require? | [Physical scope](../science/PHYSICAL_SCOPE.md) and [loss competition](../science/LOSS_COMPETITION.md) |
| Which source supplies each ingredient? | [Reference guide](../references/README.md), [comparison](../references/COMPARISON.md) and [bibliography](../references/REFERENCES.bib) |
| How are claims checked? | [Claim map](../science/CLAIM_EVIDENCE_MAP.md), [verification guide](../verification/README.md) and [reproduction policy](../provenance/REPRODUCTION_POLICY.md) |
| Where should an automated reader begin? | [LLM guide](../llms.txt) |

At the end of this route, a reader can state the full transfer task, explain why
individually excellent number-specific pulses need not share one excellent
receiver, and connect the constructive and converse bounds to their physical
meaning. The [30 milestones](MILESTONES.md) make those understanding targets explicit.

See [Purpose and contact](../README.md#purpose-and-contact) for the repository's
role and discussion details.
