# Provenance and reproducibility

The six original scientific scripts and their `results.json` files under `tests/01_*` through `tests/06_*` are exact copies from the supplied aggregate archive. `SUITES.json` records each source package hash and the per-file hashes. All six nested source archives were also compared to their separately uploaded versions and matched.

The seventh suite is the new two-sector scope audit. Its analytic statement is a corollary of the preceding converse; its finite trial calculation and controls are newly executed. None of the old scientific modules is imported by that suite.

The canonical README and research documents are **edited standalone consolidations**, not claimed to be byte-identical archival notes. No change to the source model, fidelity convention, or earlier result is intended by those edits. Historical scouting opinions and target-journal statements are not public scientific premises. The original aggregate archive remains unmodified in the conversation; no third-party paper is redistributed here.

`VERIFICATION.json` records the completed local execution of all seven suites. The reference environment is pinned in `requirements.txt`. The runner writes outputs to temporary files and compares them with references without overwriting them. Exact numerical equality in that environment is evidence of reproducibility, not proof of universal statements or prior-art independence.

If a future change is needed, make it explicit in this ledger and preserve the corresponding original file or its source hash. A failed numerical check must not be “fixed” by silently replacing its expected output. No formal proof assistant or independent reviewer has certified the results.

## Live repository import

[IMPORT.md](IMPORT.md) records the baseline commit, retained license, exact starter archive, and administrative changes. [BOOTSTRAP_VERIFICATION.json](BOOTSTRAP_VERIFICATION.json) is the new local verification record. The starter's manifest is retained separately; the active manifest is regenerated for the repository tree without changing any scientific test or reference.
