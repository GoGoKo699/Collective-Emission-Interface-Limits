# Hosted reproduction: retained differences classified

**3 October 2026. Issue #7 follow-up.** No scientific script, saved result, suite registry, theorem or physical assumption is changed. This is source-informed numerical review and evidence retention, not independent proof review.

## Chronology and outcome

PR #6's run `37138835832` passed all scientific assertions but reported different JSON for all eight suites. Its raw per-suite output was discarded. The unchanged [old summary](HOSTED_REPRODUCTION_PREVIOUS.json) does not identify the differences, and those missing values have not been recovered.

The first retained run `37140146773` reproduced every reference byte-for-byte. Run `37140435037` separately used the exact original runner, with only temporary-output capture added externally, and the new evidence-retaining runner. Both paths also reproduced every reference. Those successful runs initially failed to reproduce the symptom; they did not explain the old discrepancy.

**Run `37140915684` then reproduced the all-eight-suite mismatch. The new reference gate failed and the branch was not merged.** Every unchanged scientific assertion still passed. Its raw artifact was downloaded, its SHA-256 verified, and all differences inspected. There are 431 changed numeric fields: 429 floating-point values and two solver-work counters. There are no metadata, schema, status or nonnumeric scientific differences.

This retained recurrence supports a concrete numerical classification. It does not prove that the discarded PR #6 values were identical to it or isolate the exact processor/library operation responsible.

## What actually differed

| Suite | Changed numeric fields | Largest absolute floating-value change | Interpretation |
|---|---:|---:|---|
| 01 Pulse matching | 89 | 1.688e-8 | Largest changes are in the deliberately rescaled diagnostic N squared times infidelity. |
| 02 Common-mode limit | 75 | 3.732e-12 | Scalar bracket and calculation differences. |
| 03 Passive receiver | 101 | 5.4e-15 | Computed overlaps and residuals. |
| 04 Two-mode structure | 67 | 2.341e-11 | Largest change is an angle-inequality numerical slack close to zero. |
| 05 Photon collection | 47 | 1.66e-14 | Includes two additional integer changes in solver work, excluded from this floating maximum. |
| 06 Source realization | 24 | 2.274e-13 | Largest change is an equation residual. |
| 07 Two-sector scope | 24 | 4.592e-12 | Scalar fidelity-bound values. |
| 08 Uniform proof audit | 4 | 3.7e-15 | Small full-cascade diagnostic differences. |
| **Total** | **431** | — | 429 floating values and two work counters; all 612 scientific cases pass. |

### Rescaled infidelity is not the original fidelity

The current source `tests/01_pulse_matching/checks.py`, lines 142–148 and 184–189, explicitly stores `N*N*(1-fidelity)`. Eleven of the raw gate's thirteen alerts came from that rescaling, not a fidelity change of the same absolute size.

For example, at N=2000 a scaled value changes from 6.311468865760617 to 6.311468848885227. The raw difference is 1.6875390e-8; in the underlying infidelity it is **4.21884750e-15**. The original scientific checks compare these finite coefficients with their analytic predictions within 2 or 2.5 percent, as stated in their source. They pass without any modification. Last digits of the rescaled diagnostic do differ; the record does not call these files exact replicas.

The revised review layer therefore also compares these two explicitly named field families in original infidelity units. It checks that N itself is unchanged. It does not apply a blanket tolerance to arbitrary derived numbers or replace their raw values.

### Solver work is not a physical result

Two fields in suite 05 store `sol.nfev` directly at line 90. Their values are 30422 versus 30290, and 37634 versus 37610. This is the number of right-hand-side evaluations performed by the ODE solver, not the number of scientific cases, emitters, or photons. Only the documented suite/path combinations receive that interpretation. Other changed integer counters still fail the reference gate.

### The central numerical example is stable at its reported precision

For the N=1000, M=300, m=300 example:

| Quantity | Saved reference | Retained rerun |
|---|---:|---:|
| Mean photon fraction in the selected mode | 0.9991012722790275 | 0.999101272279029 |
| All-photons-in-mode probability | 0.786518745124638 | 0.7865187451246546 |

The reported contrast, approximately **99.9101% photon collection versus 78.6519% all-photon overlap**, is unchanged. No theorem constant or physical benchmark conclusion required correction. This is a comparison of executions, not a rigorous integration-error certificate. Near-zero residuals can change sign, so relative differences are retained with their absolute scale instead of being called large physical errors.

## Why the reference gate now has two layers

The generic field comparator remains unchanged. Its raw `REVIEW_REQUIRED` labels and thirteen alerts remain in the artifact. After the failed run, a separate source-informed review was added for exactly the scaled-infidelity and solver-work families above. The general default tolerance, 1e-10 absolute plus 1e-9 symmetric relative, was not widened. The source-unit interpretation is explicitly an added policy, not something claimed to have been selected before observing the fields.

Both the raw and reviewed reports are retained. Every other structural or numerical alert still fails. A replay of the actual retained outputs tests the reviewed acceptance end to end; a negative control changing an ordinary fidelity by 0.001 still fails even though its fixture says PASS. Fifteen infrastructure unit tests check the reporting policy. Neither replay fixtures nor tooling tests are counted as new scientific evidence.

Details are in [REPRODUCTION_POLICY.md](REPRODUCTION_POLICY.md); run identities, hashes and raw alert values are in [HOSTED_REPRODUCTION.json](HOSTED_REPRODUCTION.json). The failed artifact is `11279509209`, SHA-256 `782b690988df7f224dd4b5e5821774c6a871a376ab5faf1000bba257bd35068a`. Normal hosted artifacts expire after fourteen days; the durable record preserves the numerical classification and relevant values, not a promise of perpetual artifact access.

## Environment, preservation and limits

The exact runs used AMD EPYC 9V45 and 9V74 processors; the retained differing run used an EPYC 7763. All report Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and single-thread numerical settings. This establishes different execution environments, not a controlled attribution of the discrepancy to one CPU instruction or library dispatch path.

Container Git cloning failed on DNS. The local scientific-only reconstruction, recovered from the supplied starter and retained eighth-suite artifact, was matched to live Git tree identities. It is not a complete local repository checkout. Its completed original-runner execution reproduced all eight references exactly; one earlier enclosing-command timeout was not counted as success. Hosted verification supplies current full-tree execution.

The tests tree remains `217d1d8d07fc74d9b94e52f47b953df6dce3845e`. All eight science scripts and reference files, the suite registry, research and literature trees, license and historical manifests are unchanged. The final branch and merge results must be reported from their actual runs; this note does not predeclare either.

**Resolution:** the retained recurrence is classified and future discrepancies are inspectable. Exact bytes are environment-specific; reviewed numerical agreement is reported separately. The cause of the discarded PR #6 differences is not retroactively proven. The scientific core is preserved, not independently validated by this maintenance work. A separate critical reading, manuscript hold and outreach hold remain unchanged.
