# Reproduction evidence and source-informed review

**3 October 2026.** This policy addresses issue #7 without changing any scientific calculation or saved reference. It is not a proof or a rigorous numerical-error certificate.

## Run and retain the evidence

```sh
python tools/test_reproduction.py
python tools/test_verifier.py
python verify.py --output verification-report.json \
  --artifacts-dir verification-artifacts --require-reference
```

Choose a new artifact directory for each run. It contains every suite's unchanged script and reference, actual generated output, full raw field comparison and separate reviewed comparison. An allowlisted runtime report records package/build/CPU details and thread settings without dumping credentials. The workflow retains artifacts even on failure; normal hosted retention is fourteen days.

Scientific assertion success, source/reference preservation, exact-byte equality and reviewed numerical agreement are separate report fields. None is silently substituted for another. Raw field comparisons and byte flags remain visible even when a reviewed difference is accepted.

## Generic comparison

Only top-level `environment` and `date` values are metadata. Duplicate keys, nonfinite/invalid JSON, scientific schema or type changes, changed status strings and integer counters trigger review. Every numeric difference records both values, an absolute difference and a symmetric relative difference. A reference-relative difference is undefined for zero references rather than reported as a misleading infinite percentage.

Before the first retained run, the branch declared the general review threshold

$$|a-b|\leq10^{-10}+10^{-9}\max(|a|,|b|).$$

That threshold is unchanged. It is a regression alert, not solver accuracy, an allowable physical infidelity or a proof that all changes within it are harmless. Every raw difference is preserved, not just threshold violations.

## Explicit source-informed interpretations

The retained recurrence first failed the generic gate. Source inspection then established two narrow reporting conventions. `tools/reviewed_fields.py` implements them without changing the generic verdict.

**Rescaled infidelity:** only suite 01's `fixed_m_checks/*/scaled_loss` and `small_code/exact_scaled_losses/*` values are known from the unchanged source to be `N*N*(1-fidelity)`. The review compares their original infidelity units using the same numerical threshold, provided both records have the same positive integer N. Raw scaled differences remain in `comparison.json`. Parameter, type and unrelated result changes are not hidden by rescaling.

**Solver work:** only suite 05's `finite_rows/*/mean/nfev` and `refined_largest_case/nfev` are the stored `solve_ivp` evaluation counts. Nonnegative integer differences there are classified as workload, not physics. The same field name elsewhere, changed types, missing values, test counts and physical integers still require review.

These rules were added after inspecting the retained failure. They are not a generic permission to relax comparison whenever a result differs. No scientific assertion, reference file or general tolerance was changed. Any further exception requires its own source justification and preserved failing evidence.

With `--require-reference`, unresolved raw alerts fail the run. The two justified families receive an explicit `reviewed-comparison.json` record. The original scientific assertions run separately and must also pass. An artifact may therefore contain a raw `REVIEW_REQUIRED` label alongside accepted source-unit review; this is deliberate and explained, not exact-byte equality.

## Controls

The original fifteen tooling unit tests covered invalid data, duplicate keys, zeros, large integers, types, metadata, changes to N, scoped work counts, rescaled physical errors and evidence preservation. The 5 October audit adds two comparator/environment tests and five verifier fixtures: **22 current infrastructure tests**. Nonfinite numeric overflow is rejected even inside metadata; reports carry real UTC start/end times and the effective suite thread settings. Summary output paths cannot replace maintained source files or retained raw evidence. The fixtures include a deliberately invalid result that reports PASS but must fail the reference gate while retaining its original bytes.

The earlier local end-to-end replay of the captured output passes the declared review while retaining its false exact-byte flags. Altering an ordinary fidelity by 0.001 makes the gate fail even if the replayed script reports PASS. These fixtures test infrastructure, not the science. Historical execution reports remain unchanged, including their original dates and environment fields; the current audit identifies the provenance limitations of the old runner.

The optional `tools/capture_previous_runner.py` verifies the old runner's blob and copies its temporary output immediately before cleanup. Its hosted cross-check reproduced all references exactly. It cannot recover values discarded by a historical job and is not run on every normal commit.

## Reporting limits

The old PR #6 summary remains evidence of a mismatch with missing raw outputs. The later retained PR #8 recurrence can be classified; it does not establish the exact values or causal instruction path of that earlier run. Different CPUs coincided with different numerical results, but no controlled causal CPU/library diagnosis has been performed.

See [HOSTED_REPRODUCTION.md](HOSTED_REPRODUCTION.md) for the actual observed fields and scientific interpretation. Never regenerate a saved reference to match a machine. Future changed benchmarks need a calculation-specific investigation, not a blanket rounding explanation. Independent proof reading and joint-device evidence remain separate tasks.
