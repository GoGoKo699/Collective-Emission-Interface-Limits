# Verification and reproduction

[Overview](../README.md) · [Scientific account](../science/README.md) · [Claim and evidence map](../science/CLAIM_EVIDENCE_MAP.md)

The analytic arguments establish the uniform statements. The executable suites
check finite identities, constructions, approximations and physical consequences.
Their scripts and saved results are protected by the
[suite registry](../provenance/SUITES.json); a reproduction run writes fresh
outputs and compares them with the preserved references.

## Run the checks

Run from the repository root with Python 3.12 or later. The hosted workflow
uses Python 3.13.5 and the exact package versions in
[requirements.txt](../requirements.txt).

```sh
python -m pip install -r requirements.txt
python tools/test_reproduction.py
python tools/test_verifier.py
python tools/check_presentation.py --self-test --output presentation-report.json
python verify.py --integrity-only
python verify.py --output verification-report.json \
  --artifacts-dir verification-artifacts --require-reference
python tools/check_loss_competition.py --output loss-competition-report.json
```

Use a fresh directory for `--artifacts-dir` on every run. The full run writes
`verification-report.json` plus each suite's original script, reference output,
fresh output, raw comparison and reviewed comparison under that directory.
The loss checker writes its separate report. Neither command rewrites saved
scientific results.

For one named suite, add `--suite 08_uniform_proof_audit` or another exact name
from the table below. The default per-suite timeout is 240 seconds. The runner
sets `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1` for its child processes and
records the effective numerical environment.

## What the eight scientific suites check

| Suite | Main finite checks | Groups | Cases | Scientific account |
|---|---|---:|---:|---|
| `01_pulse_matching` | Individually matched pulses, overlap and fixed-sector approximation | 5 | 71 | [Matched pulses](../science/MATCHED_PULSES.md) |
| `02_common_mode_limit` | Common-pulse minimax scaling and finite bounds | 6 | 62 | [Common-mode boundary](../science/COMMON_MODE_BOUNDARY.md) |
| `03_passive_receiver` | Passive selection, attenuation and finite capture | 5 | 37 | [Model](../science/MODEL.md), [capture resources](../science/PHYSICAL_SCOPE.md) |
| `04_two_mode_structure` | Tangent mode and the leading two-mode error structure | 5 | 97 | [Physical error mechanism](../science/PHYSICAL_SCOPE.md) |
| `05_photon_collection` | Mean collected fraction and its separation from transfer fidelity | 4 | 86 | [Photon collection](../science/PHOTON_COLLECTION.md) |
| `06_source_realization` | Scalar shaping, independent loss and finite source-realization models | 5 | 144 | [Physical scope](../science/PHYSICAL_SCOPE.md) |
| `07_two_sector_scope` | Two populated sectors and successful sparse-code comparators | 4 | 24 | [Two-sector witness](../science/TWO_SECTOR_WITNESS.md) |
| `08_uniform_proof_audit` | Uniform bounds, endpoint-safe converse and photon-count estimates | 5 | 91 | [Boundary proof](../science/COMMON_MODE_BOUNDARY.md), [proof details](../science/PROOF_DETAILS.md) |
| **Total** | **Preserved scientific cases** | **39** | **612** | [Protected identities](../provenance/SUITES.json) |

The [loss-competition checker](../tools/check_loss_competition.py) has **50
supplementary checks** of the scalar certificate, shifted common pulse and
finite loss bounds. Its [analytic derivation](../science/LOSS_COMPETITION.md)
specifies the mode-independent pure-loss channel; the checks do not broaden
that model.

## Read the results accurately

| Output or check | What a successful result establishes |
|---|---|
| Integrity check | The eight scientific script/result pairs match their registered hashes, and local file links resolve. |
| Scientific assertions | The finite cases encoded in the eight suites pass; expected totals are 8 suites, 39 groups and 612 cases. |
| `--require-reference` | The fresh results pass the declared source-informed comparison with the preserved references. |
| Exact-byte and JSON fields | Whether the fresh and stored outputs are identical at those levels, reported separately from reference agreement. |
| Presentation checker | Markdown/TeX delimiters, tables and targeted GitHub rendering hazards pass structural checks. |
| Hosted visual inspection | The inspected pages and mathematical expressions display correctly at the inspected revision. |

A passing reference comparison can coexist with different raw bytes or a raw
`REVIEW_REQUIRED` label. The [reproduction policy](../provenance/REPRODUCTION_POLICY.md)
explains the two narrowly defined reporting conventions for rescaled infidelities
and solver evaluation counts; all raw differences remain available. Numerical
thresholds are regression alerts, not physical error budgets or certified solver
accuracy. A failed assertion or unresolved scientific difference fails the run.

The reproduction comparator and verifier have **25 infrastructure tests**.
The presentation checker has **22 fixtures**, counted separately from the
scientific cases. The output guards protect `science/`, `learning/`,
`references/`, `verification/` and the other maintained source and evidence
paths. Generated reports must use their documented output locations.

## Proof and evidence routes

The [claim map](../science/CLAIM_EVIDENCE_MAP.md) connects each conclusion to its
analytical proof and finite checks. In particular, an excitation scan does not
prove a uniform limit, an optimized pulse-family scan does not exclude all other
waveforms, and finite full-cavity photon probabilities do not establish a
uniform emitted-field approximation for a growing code.

The [provenance index](../provenance/README.md) links dated executions, protected
reference data and the revisions they describe. The
[hosted workflow](../.github/workflows/verify.yml) runs the same gates and retains
raw outputs and comparisons as its `verification-evidence` artifact. Its
configured retention period is 14 days. Current scientific statements are
organized under [science/](../science/README.md).
