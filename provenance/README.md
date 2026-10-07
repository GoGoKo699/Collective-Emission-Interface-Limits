# Provenance and reproducibility

## Current audit

The [prewriting research record](PREWRITING_2026_10_05.json) maps the subsequent
claim audit, source refresh, finite-capture proof and loss-competition derivation.
The new supporting checker has 50 supplementary cases, counted separately from
the preserved eight-suite baseline. It imports the existing continuum-overlap ODE
with attribution and checks new scalar optimization and finite bounds; it is not
an independent derivation of that ODE or an interval-certified numerical proof.
The raw new [loss-check result](prewriting_2026_10_05/loss-check.json) is retained.

The active registry contains **eight scientific suites, 39 groups and 612 cases**.
The [5 October sanity record](../research/SANITY_CHECK_2026_10_05.md) and
[machine-readable evidence map](SANITY_2026_10_05.json) document fresh baseline and
repaired-runner verification. All scientific scripts and references are preserved.
The reporting tools now have 25 focused infrastructure tests; mathematical presentation
has a separate 22-test checker. These counts are not added to the scientific cases.
The 7 October reader-notice update added three link-integrity fixtures for email
links and the LLM guide. The verifier accepts `mailto:` addresses and checks root
`llms.txt` while continuing to reject broken local links. Scientific suite hashes
and reference comparisons are unchanged.

The 7 October display repair replaces rejected operator notation with upright text,
makes fraction and bold-symbol arguments explicit, and uses a TeX relation instead
of an HTML-like less-than token. Protected inline and fenced display delimiters
keep Markdown from stripping mathematical braces or turning spacing commands into
punctuation. Ten new presentation fixtures cover these compatibility patterns.
Local TeX compilation alone did not catch the reported GitHub failures; the checker
remains a limited structural and compatibility check, not a substitute for
inspecting the rendered page.

The eighth suite and endpoint proof repair are recorded in [PROOF_AUDIT.json](PROOF_AUDIT.json).
The following import account and its seven-suite execution record are historical.

## Original import account

The six original scientific scripts and their `results.json` files under `tests/01_*` through `tests/06_*` are exact copies from the supplied aggregate archive. `SUITES.json` records each source package hash and the per-file hashes. All six nested source archives were also compared to their separately uploaded versions and matched.

The seventh suite is the new two-sector scope audit. Its analytic statement is a corollary of the preceding converse; its finite trial calculation and controls are newly executed. None of the old scientific modules is imported by that suite.

The canonical README and research documents are **edited standalone consolidations**, not claimed to be byte-identical archival notes. No change to the source model, fidelity convention, or earlier result is intended by those edits. Historical scouting opinions and target-journal statements are not public scientific premises. The original aggregate archive remains unmodified in the conversation; no third-party paper is redistributed here.

`VERIFICATION.json` records the completed local execution of all seven suites. The reference environment is pinned in `requirements.txt`. The runner writes outputs to temporary files and compares them with references without overwriting them. Exact numerical equality in that environment is evidence of reproducibility, not proof of universal statements or prior-art independence.

If a future change is needed, make it explicit in this ledger and preserve the corresponding original file or its source hash. A failed numerical check must not be “fixed” by silently replacing its expected output. No formal proof assistant or independent reviewer has certified the results.

## Activation in the live repository

The initial import commit is `ff4e1577b18cbfbf759e11c61cc86efe268eb59e`. At that revision, every one of the 32 starter files matches the supplied package byte-for-byte; the pre-existing MIT license is the only additional file. `FILE_MANIFEST.json`, `VERIFICATION.json`, and `DELIVERY_VALIDATION.json` describe that original starter. In particular, the historical `new_remote_repository_created: false` field describes preparation of the seed, not the current repository state.

Later onboarding edits are recorded separately in [IMPORT.md](IMPORT.md). The starter file manifest is intentionally not relabeled as a current-tree or CI-success certificate. `SUITES.json` remains the active per-script/per-reference integrity check. The automated workflow writes its own execution report and never refreshes reference results. Numerical tests can pass on another environment without exact-byte agreement; the runner records that distinction explicitly.
