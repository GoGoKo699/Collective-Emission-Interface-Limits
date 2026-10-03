# Research status

**3 October 2026 · Dedicated development candidate · Manuscript on hold.**

The source, canonical number map, excitation code, receiver class and theorem are unchanged.

## Current tutorial and presentation

The owner selected **Kiilerich–Mølmer (2020), Quantum interactions with pulses of radiation**
as the single teaching anchor. The [reading guide](docs/README.md) follows the source's
pulse/input-output/occupation/capture organization. The [technical bridge](REVIEW.md)
adds the Dicke ladder, canonical fidelity and uniform-bound steps locally, without
requiring a second external tutorial. [TUTORIAL_OPTIONS.md](literature/TUTORIAL_OPTIONS.md)
now records the completed choice and keeps the alternatives as optional references.

The front page presents the physical task, theorem and reading routes before the audit
records. GitHub-native inline math and display blocks are checked separately from the
scientific suites. The [presentation record](provenance/TUTORIAL_FURNISHING.json) identifies
typography-only changes to existing research notes and the actual validation scope.

The [background dossier](literature/BACKGROUND.md), [convention map](research/CONVENTIONS.md)
and [bibliography](literature/REFERENCES.bib) remain the source-to-proof support. The anchor
is not credited with the project-specific uniform theorem.

**Still open:** the full construction-level comparison with Tziperman et al., ACS Nano 19,
21260–21270 (2025), arXiv:2306.11348. The [background audit](literature/BACKGROUND_AUDIT.md)
records the accessible abstracts and missing complete reading. Furnishing the repository
does not resolve this priority question or create a separate critical-reader report.

## Reproducibility outcome already established

The follow-up to issue #7 is recorded in [HOSTED_REPRODUCTION.md](provenance/HOSTED_REPRODUCTION.md). Two initial hosted checks reproduced all references exactly, including an execution of the unmodified old runner. A subsequent run reproduced the mismatch and failed the new reference gate before merging. Its complete output was retained and inspected.

The retained recurrence changes 429 floating values and two solver-work counts, with no metadata, schema or status differences. Eleven raw alerts concern N-squared-rescaled infidelity; the largest corresponds to a 4.22e-15 change of the original infidelity. Two alerts are solver evaluation counts, not physical or test-case counts. Other floating differences fall within the previously declared general threshold. The main finite photon-collection/fidelity contrast retains its reported precision; every original scientific assertion passes.

A source-informed review distinguishes those two identified field families while retaining every raw value and raw failed verdict. The general tolerance and all science assertions are unchanged. [REPRODUCTION_POLICY.md](provenance/REPRODUCTION_POLICY.md) defines the two-layer gate and its fifteen infrastructure unit tests. The scientific count remains eight suites, 39 groups and 612 cases.

**The retained recurrence is classified; the discarded PR #6 values remain unavailable.** Their precise cause is not retrospectively established. Exact bytes are not promised across machines, and numerical agreement is not independent proof review. Each new branch and merge must be assessed from its actual workflow results.

## Scientific core and remaining evidence

[STORY.md](research/STORY.md) states the physical account: a dilute collective source can approach an oscillator for mean-photon collection without faithfully transferring its whole excitation code into one fixed linear memory. The optimized all-waveform converse matters, rather than failure of an arbitrarily selected exponential.

[THEOREM.md](research/THEOREM.md) includes the endpoint-safe proof correction in [PROOF_AUDIT.md](research/PROOF_AUDIT.md). The uniform approximation, critical boundary, mean-collection comparison and two-sector witness are unchanged. The two-mode explanation and source-realization analyses remain supporting results within their stated regimes.

The [Law–Lee reading](literature/LAW_LEE_FULL_TEXT.md) and [preparation readings](literature/PREPARATION_EVIDENCE.md) are complete at their documented versions. Their inherited contributions remain credited. The [assumption register](literature/ASSUMPTIONS.md) does not convert five related preparation methods into five joint-device demonstrations.

A separate mathematical/physical report is still absent. Reader candidates were identified privately, but no invitation or report is implied by this public repository. Whole-code preparation, reference-preserving encoding, atom-number calibration, microscopic bandwidth/rate scaling and joint realization remain conditional for a device claim.

The [work order](work_orders/CURRENT.md) records the completed teaching route and retains the close-source comparison and separate-reading tasks. No new model or manuscript is introduced to avoid those questions.

This furnishing pass changes navigation, explanatory material and mathematical presentation, and adds a separate presentation checker plus tracked-source retention in CI. All eight scientific scripts/results, the suite registry, numerical comparison policy, MIT license and historical manifests remain unchanged. Existing proof statements, equations and arguments are not altered by the delimiter changes; their source identities are recorded separately. Manuscript writing and outreach remain on hold.
