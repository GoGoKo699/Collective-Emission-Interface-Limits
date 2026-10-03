# Current work order: preserve the teaching route and resolve the close-source comparison

**Updated 3 October 2026 after the owner's tutorial selection.** The learning anchor is
Kiilerich–Mølmer, *Quantum interactions with pulses of radiation* (2020). The source,
canonical number map, code, receiver and theorem remain fixed.

## Completed pedagogical work

[README.md](../README.md) gives the task and main result. [docs/README.md](../docs/README.md)
maps the selected source's Sections I–II D and optional III to the repository.
[REVIEW.md](../REVIEW.md) supplies the missing Dicke cascade, canonical fidelity and
uniform-bound bridge. These are an explanation of the existing result, not a manuscript
or a second external syllabus. The alternatives in TUTORIAL_OPTIONS.md are no longer a
pending choice.

Preserve source terminology and distinguish the virtual output-cavity construction from
an unlimited-bandwidth apparatus. The [convention map](../research/CONVENTIONS.md)
translates pulse labels, ladder operators, rates, normalization and fidelity. The canonical
proof and physical-scope notes remain byte-for-byte unchanged; the notation bridge and
explanatory story receive the documented presentation edits, not new scientific claims. The explicit earlier proof repair remains visible.

Use GitHub-supported inline math and fenced display math. Avoid literal vertical bars
inside table cells, code-formatted equations and long unbroken inline formulas. Run
`python tools/check_presentation.py` and inspect rendered mathematics after future edits.
The structural checker is not a substitute for rendering or a proof audit.

## Required construction-level comparison

Obtain and inspect Tziperman et al., *Nonlinear Quantum Light Generation in Collective
Spontaneous Emission*, ACS Nano 19, 21260–21270 (2025), DOI 10.1021/acsnano.4c15257;
author preprint arXiv:2306.11348, *The quantum state of light in collective spontaneous
emission*. The [background audit](../literature/BACKGROUND_AUDIT.md) records the abstract-level
access and the failed full-text routes. The complete Law–Lee and preparation readings
remain completed; they are not fresh missing-source tasks.

Identify the new paper's source ladder, input space, pulse-selection rule, target and
fidelity, receiving resources, and any controlled growing-code/all-waveform conclusion.
Keep a genuine subsumption or a precise distinction. Do not infer novelty from inaccessible
text or repeat failed retrievals as progress. This furnishing pass did not claim to close
that comparison.

## Separate critical reading

Use [CRITICAL_READING.md](../research/CRITICAL_READING.md), [THEOREM.md](../research/THEOREM.md),
[PROOF_AUDIT.md](../research/PROOF_AUDIT.md), [STORY.md](../research/STORY.md) and the source
comparisons. Distinguish correctness, inherited results, significance and device assumptions.
An identified candidate is not a received report; another internal rerun is not a separate
reading. No outside contact without explicit user instruction.

Whole-code/reference-preserving preparation, calibrated atom number, consistent
bandwidth/rates, duration and losses remain conditional for a joint device claim.

## Evidence preservation

Read WORKSPACE.md and AGENTS.md. Before changing scientific code, run `python verify.py`.
Retain outputs with `python verify.py --artifacts-dir verification-artifacts --require-reference`
in a fresh directory. Do not rewrite references or widen tolerances for green CI. The
source-informed numerical review and the historical missing PR #6 values remain documented
in [HOSTED_REPRODUCTION.md](../provenance/HOSTED_REPRODUCTION.md).

The eight scientific suites are distinct from presentation and reproduction-infrastructure
checks. Tutorial selection does not authorize another Hamiltonian, decoder, encoding,
noise campaign, manuscript or outreach. Preserve the compact source-to-memory claim.
