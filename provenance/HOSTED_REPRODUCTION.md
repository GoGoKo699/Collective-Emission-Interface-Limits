# Hosted reproduction: evidence retained, discrepancy not reproduced

**3 October 2026. Resolution of the bounded follow-up in issue #7.** No theorem, physical assumption, scientific test script, saved result or suite registry is changed by this pass.

## What was known before this pass

PR #6's workflow run `37138835832` passed all eight scientific suites but reported false byte-equality and JSON-equality flags for each. Its artifact `11279691529` contained a summary, not the generated per-suite JSON. The original runner deleted those temporary files at exit.

That report is preserved unchanged as [HOSTED_REPRODUCTION_PREVIOUS.json](HOSTED_REPRODUCTION_PREVIOUS.json). It does not reveal the differing fields. The old values cannot be recovered from it, and neither a rounding explanation nor a metadata explanation has been established. A new successful run does not retrospectively explain a discarded output.

## What was actually tested

The first instrumented run, `37140146773`, retained scripts, references, generated results, field comparisons and a runtime report. Every generated result was byte-identical to its unchanged reference. The artifact was downloaded and its declared SHA-256 verified before inspecting every comparison locally.

A second hosted run, `37140435037`, tested both execution paths in the same checkout:

- The exact original runner blob `be56c4cd9971405b75e2363a49c88a27378c20ef`, with only a wrapper copying temporary outputs immediately before their normal deletion.
- The new evidence-retaining runner with its reference-comparison gate enabled.

Both paths passed all eight scientific suites. Every generated file from both paths was byte-identical to its saved reference. The downloaded raw files were compared again locally; their field-comparison records agree with the independently reexecuted comparison. This rules out the new reporting code merely normalizing or hiding the observed values in these reruns. It does not identify the cause of the older run's discrepancy.

| Scientific suite | Numeric fields compared | Numeric differences in each retained execution | Other scientific or metadata differences |
|---|---:|---:|---:|
| 01 Pulse matching | 306 | 0 | 0 |
| 02 Common-mode limit | 474 | 0 | 0 |
| 03 Passive receiver | 277 | 0 | 0 |
| 04 Two-mode structure | 438 | 0 | 0 |
| 05 Photon collection | 149 | 0 | 0 |
| 06 Source realization | 477 | 0 | 0 |
| 07 Two-sector scope | 125 | 0 | 0 |
| 08 Uniform proof audit | 194 | 0 | 0 |
| **Total per execution** | **2440** | **0** | **0** |

The scientific count remains **eight suites, 39 diagnostic groups and 612 cases**. Repeating their execution does not create additional scientific evidence categories. All recorded benchmark values are unchanged in the retained runs, including their displayed digits; no rounding policy was needed to obtain these equalities.

The two hosted machines report AMD EPYC 9V45 and 9V74 processors, respectively, with Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0. Their full numerical-library configuration is in the artifacts. The CPU difference does not establish anything about the unrecorded old environment or which operation, if any, caused its mismatch.

## Preservation and local scope

The full scientific tests tree still has Git identity `217d1d8d07fc74d9b94e52f47b953df6dce3845e`. The eight source/result pairs and active suite registry are unchanged. Research and literature trees, the license and historical manifests are untouched.

Container Git cloning failed on DNS resolution. The first seven local suites came from the supplied starter, and the eighth was recovered from the newly retained hosted artifact. Their complete reconstructed tests tree and registry were matched to the live Git identities. This is a scientific-only local reconstruction, not a full repository checkout. The original runner's completed local eight-suite run also reproduced all reference files exactly.

One earlier local aggregate invocation exceeded its enclosing command's time limit and is not counted as a successful run. A subsequent captured execution completed all eight suites. The separate eighth-suite execution also completed. No expected output was changed in response.

## What changes going forward

The [reproduction policy](REPRODUCTION_POLICY.md) separates assertion success, preserved-source integrity, exact bytes and numerical agreement. The workflow retains all raw outputs and comparisons, including on failure. Structural scientific changes, changed counters/statuses, invalid output and numerical deviations beyond predeclared alert thresholds fail the reference gate.

Twelve infrastructure unit tests and an end-to-end negative control test that reporting logic. They are not scientific proof checks and are not added to the 39-group count. The temporary double execution of old and new runners is removed from the normal workflow; the optional capture helper remains available for an explicit diagnostic.

## Resolution and remaining uncertainty

**Current result: the discrepancy did not recur; current raw outputs reproduce exactly. Historical cause: undetermined because the old generated values were not retained.** This is not a finding that the old discrepancy was harmless roundoff, and it is not a recovered classification of its missing fields.

The bounded action in issue #7 is complete: outputs are now retained, field-level comparisons are enforced, and the current numerical evidence is checked without rewriting references. A recurrence with retained differing values would be new actionable evidence and should be investigated rather than assigned a cause in advance. Endless repetitions of exact runs cannot resolve the missing historical information.

This changes the auditability of the research, not the theorem, its novelty assessment, or the absent separate mathematical/physical review. Manuscript writing and outreach remain on hold.
