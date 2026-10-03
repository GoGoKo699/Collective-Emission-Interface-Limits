# Reproduction evidence and reporting policy

**3 October 2026.** This policy addresses issue #7 without changing the physical model, scientific calculations, or saved scientific results. It is not a proof review.

## Three separate questions

1. Did every scientific assertion in the standalone suites pass?
2. Were the scientific scripts and saved references preserved exactly?
3. How do the newly generated outputs compare with those references?

A green assertion run answers the first question, not automatically the third. The previous runner recorded byte/JSON equality flags but discarded the actual temporary outputs. The new runner keeps those flags and additionally compares every JSON field.

## Retained evidence

Run from the repository root, choosing an output directory that does not already exist:

```sh
python tools/test_reproduction.py
python verify.py --output verification-report.json \
  --artifacts-dir verification-artifacts --require-reference
```

For every suite the artifact contains its unchanged script, unchanged reference JSON, actual generated JSON, and complete field comparison. An allowlisted environment report records Python/package versions, CPU model, numerical-library build information and thread controls. It does not dump credentials or the full process environment. The workflow uploads evidence even when a check fails; normal hosted artifact retention is fourteen days.

The classifications distinguish exact bytes, serialization-only changes, metadata-only changes, numerical differences within the review threshold, and differences requiring review. Only the top-level `environment` and `date` fields are metadata. Changes of seeds, integer counters, booleans, strings, structure, or number types are not waved through as floating-point roundoff. Duplicate keys and nonfinite/invalid outputs require review.

Every differing numerical field retains both values, its absolute difference, and a symmetric relative difference. A reference-based relative difference is explicitly undefined when the reference is zero. This avoids reporting a tiny absolute residue as an unexplained infinite percentage. All differences remain visible, even when they do not trigger failure.

## Thresholds and what they do not prove

The initial branch declared the default alert rule before inspecting its hosted results:

$$|a-b|\leq10^{-10}+10^{-9}\max(|a|,|b|).$$

These are operational regression thresholds, not rigorous errors of an integrator, an allowed physical infidelity, or proof that a changed result is harmless. `--require-reference` fails the workflow on a scientific structural change or a numeric alert. The independent scientific assertions still run unchanged. Current byte-identical runs do not use this tolerance to make nonidentical results appear equal.

Tolerances can be specified explicitly for investigation. Any future change to the workflow defaults must be justified against the affected calculation, with both outputs retained; it must not be widened merely to restore a green job. A large relative difference at a near-zero residual can be benign or significant depending on the quantity, so a report must identify its path and scale rather than offer a blanket rounding explanation.

The comparator has twelve infrastructure unit tests, including changed values, nonfinite data, type/structure errors, large integers, reference zeros, metadata and evidence preservation. These are not additional scientific groups. An end-to-end negative control confirms that a script reporting `PASS` can nevertheless fail the new reference gate when its synthetic fidelity changes from 0.9 to 0.901.

## Historical limitations

The old PR #6 report remains evidence that equality flags were false. Its raw generated values were discarded, so later successful reruns cannot retrospectively identify those differences. Do not call the old discrepancy rounding, metadata, a proven bug, or a theorem failure without the missing evidence. The current recorded investigation is in [HOSTED_REPRODUCTION.md](HOSTED_REPRODUCTION.md).

The optional `tools/capture_previous_runner.py` checks the exact original runner blob and copies its temporary outputs immediately before their normal cleanup. It permits a separate reproduction of the old execution path without modifying scientific scripts. It cannot recover files from a completed historical run. It is not part of every normal workflow run.

No saved result is regenerated to match a machine. Historical exact-byte executions remain historical; new executions state their own equality result and environment. Separate mathematical/physical reading and joint-device evidence remain outside the scope of these checks.
