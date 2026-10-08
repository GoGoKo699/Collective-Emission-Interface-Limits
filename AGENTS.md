# Repository maintenance

Work only in `GoGoKo699/Collective-Emission-Interface-Limits`. Read `README.md`,
`STATUS.md`, `research/THEOREM.md` and `provenance/SUITES.json` before editing.

## Scientific integrity

- Preserve the collective source, excitation code, canonical number map and passive one-oscillator receiver unless a different scientific task is explicitly authorized.
- Credit the primary sources for inherited cascade, waveform, memory and preparation results. Distinguish proofs, numerical checks and source evidence.
- Prefer analytic arguments and small decisive calculations. Do not introduce a QRAM premise or a large cloud simulation.
- Keep protected scripts and results unchanged. Record an explicit correction and preserve the original evidence if scientific changes are needed; never regenerate references or widen tolerances to obtain passing checks.
- Address mathematical objections with a proof location, correction or counterexample.

## Reader-facing documentation

- Present the model, results, proofs, examples and references as a complete account.
- State the assumptions and limitations needed to interpret a claim accurately. Do not add development narratives, work plans, lists of unperformed work, or notices about absent reports or certifications.
- Keep maintenance instructions here, outside the scientific reading route. Preserve dated scientific audits and execution evidence as records, with links to the revisions they describe.
- State established answers directly with evidence links. Include future research questions only when explicitly requested.
- Preserve the Purpose and contact wording and clickable author email.
- Use protected GitHub inline and fenced display mathematics. Inspect rendered expressions after mathematical edits; structural checks do not replace rendering or proof review.
- Keep target journals, source-paper PDFs, secrets, private correspondence and unrelated projects out of the repository.
- Manuscript drafting, submission and contact with researchers require explicit instruction.

## Verification

Before changing scientific code, run `python verify.py`. Run the existing checks
for repository changes and report their actual outcomes:

```sh
python tools/test_reproduction.py
python tools/test_verifier.py
python tools/check_presentation.py --self-test
python verify.py --integrity-only
python verify.py --artifacts-dir verification-artifacts --require-reference
python tools/check_loss_competition.py --output loss-competition-report.json
```

Use fresh output paths. The eight scientific suites cover 39 groups and 612 cases;
the 50 loss checks are supplementary. The [reproduction policy](provenance/REPRODUCTION_POLICY.md)
distinguishes passing assertions, reference agreement and execution provenance.
Do not describe numerical execution as an independent proof review.
