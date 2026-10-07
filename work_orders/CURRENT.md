# Maintenance scope

The repository records a conditional theorem for a fixed collective source,
canonical number map, excitation code and passive one-oscillator receiver.
The [claim and evidence map](../research/CLAIM_EVIDENCE_MAP.md) defines the claims
and their dependencies. Kiilerich–Mølmer (2020) is the single teaching anchor.

## Scientific boundary

Preserve the theorem, its assumptions and the attribution of inherited results.
The [scope and evidence page](../STATUS.md) is the reader-facing summary.
Unknown reference-preserving upload, calibration robustness, uniform microscopic
elimination, fixed control bandwidth and a compatible joint device are
extensions outside this conditional result. Reopen them only for an explicitly
requested device claim.

Respond to a specific mathematical objection with a proof location, correction
or counterexample. Record a newly subsuming source directly. Additional examples
or broader receivers are not prerequisites for the present theorem.
Manuscript drafting, submission and outside contact require explicit instruction.

## Documentation

Write current pages as a finished account of the model, results and limitations.
Keep dated development narratives, superseded access labels, failed attempts and
execution history in the existing audit and provenance records. Do not erase
those records or repeat their progress notices in the reading route.
State known answers with evidence links; reserve questions for unresolved issues.

## Verification

Read WORKSPACE.md and AGENTS.md. Before changing scientific code, run
`python verify.py`. Keep inherited scripts and references unchanged unless an
explicit correction is recorded. Never regenerate references or widen tolerances
to obtain passing CI.

Run:

```sh
python tools/test_reproduction.py
python tools/test_verifier.py
python tools/check_presentation.py --self-test
python verify.py --integrity-only
python verify.py --artifacts-dir verification-artifacts --require-reference
python tools/check_loss_competition.py --output loss-competition-report.json
```

Use fresh output paths; the supplementary checker refuses to overwrite an existing
report. The eight scientific suites cover 39 groups and 612 cases. The 50 loss
checks are supplementary. The [reproduction policy](../provenance/REPRODUCTION_POLICY.md)
distinguishes assertions, exact bytes, numerical agreement and execution provenance.

Use protected GitHub inline and fenced display mathematics. Inspect rendered
expressions after mathematical edits; structural checks do not replace rendering
or proof review. No source-paper PDFs, private correspondence or unrelated
projects belong here.
