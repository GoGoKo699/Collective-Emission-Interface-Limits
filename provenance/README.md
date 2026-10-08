# Provenance and reproducibility

The [suite registry](SUITES.json) protects the scientific scripts and reference
results by hash. Eight suites cover 39 groups and 612 cases; the loss checker has
50 supplementary cases. Reproduction runs compare fresh outputs with these
references. The [reproduction policy](REPRODUCTION_POLICY.md) defines the comparison
and evidence rules.

## Verification records

Each dated record identifies the revision, environment and checks it covers.

| Record | Contents |
|---|---|
| [Release sanity check, 7 October 2026](RELEASE_2026_10_07.json) | Numerical reproduction, protected hashes, documentation and content checks |
| [Research verification, 5 October 2026](PREWRITING_2026_10_05.json) | Claim/source comparisons and the loss and finite-capture calculations |
| [Loss-check output](prewriting_2026_10_05/loss-check.json) | The 50 supplementary scalar-optimization and finite-bound checks |
| [Sanity evidence map](SANITY_2026_10_05.json) and [analysis](../research/SANITY_CHECK_2026_10_05.md) | Numerical reproduction and verifier diagnostics |
| [Proof audit record](PROOF_AUDIT.json) and [derivations](../research/PROOF_AUDIT.md) | Endpoint correction, finite inequalities and the eighth scientific suite |
| [Import record](IMPORT.md) | Original source packages and repository import |

## Reference data

The six original script/result pairs under `tests/01_*` through `tests/06_*` are
exact copies from the supplied source packages. Their package and file hashes are
recorded in `SUITES.json`, alongside the two-sector and uniform-proof suites.

[FILE_MANIFEST.json](FILE_MANIFEST.json), [VERIFICATION.json](VERIFICATION.json)
and [DELIVERY_VALIDATION.json](DELIVERY_VALIDATION.json) describe the original
32-file starter at commit `ff4e1577b18cbfbf759e11c61cc86efe268eb59e`.
The active `SUITES.json` registry governs scientific-file integrity; CI preserves
its own execution reports and raw comparisons.

## Documentation checks

The reproduction and verifier tools have 25 focused tests. Mathematical
presentation has 22 separate fixtures covering delimiters, table structure and
known GitHub rendering hazards. These counts are separate from the scientific
cases. The integrity verifier checks local Markdown and LLM-guide links.

Protected inline and fenced display mathematics preserve TeX through GitHub's
Markdown processing. The presentation checker tests structure and compatibility
patterns; visual inspection checks the rendered page.
