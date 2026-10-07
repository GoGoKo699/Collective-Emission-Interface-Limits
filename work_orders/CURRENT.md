# Current work order: preserve the completed conditional research package

**Updated 5 October 2026 after the requested prewriting scientific-research pass.**
The source, canonical number map, code and receiver remain fixed. The main ideal
theorem is unchanged. The selected single teaching anchor remains Kiilerich–Mølmer
(2020). Manuscript drafting has not begun.

**Teaching update, 6 October 2026.** The owner reconfirmed Kiilerich–Mølmer as the
single external source. The reading guide and local bridge now furnish the route
with worked calculations and a final lesson on the established loss/capture bounds.
This pedagogical pass does not reopen the completed scientific work order.

## Completed research

The [claim and evidence map](../research/CLAIM_EVIDENCE_MAP.md) is the entry point.
It separates the main result, essential proof lemmas, supporting consequences,
inherited ingredients, and stronger claims that the project does not make.

- The ideal uniform field approximation, channel reduction, arbitrary-waveform
  converse, excitation boundary and photon-collection contrast have internal
  claim-level proof reviews. The historical [proof correction](../research/PROOF_AUDIT.md)
  remains visible.
- The [two-sector witness](../research/TWO_SECTOR_WITNESS.md) and
  [fixed-target excitation budget](../research/STORY.md) delimit the result's meaning.
- The [loss-competition proof](../research/LOSS_COMPETITION.md) resolves whether
  ordinary transmission loss masks the common-mode penalty. It includes finite
  certificates and a new, separately counted supplementary checker.
- [Physical scope A](../research/PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means)
  now derives the finite-window and regularization error across the entire code,
  using the receiver construction already tested in the preserved suite.
- The Law–Lee, preparation and Tziperman readings remain preserved. The
  [dated additional comparison](../literature/PREWRITING_SEARCH_2026_10_05.md) adds
  Porras–Cirac, Perarnau-Llobet et al., and Belliardo et al., with source versions,
  actual reading scope and screened recent titles.
- The [reading guide](../docs/README.md) and [local bridge](../REVIEW.md) retain the
  owner's tutorial choice. The [sanity record](../research/SANITY_CHECK_2026_10_05.md)
  and [prewriting provenance](../provenance/PREWRITING_2026_10_05.json) distinguish
  analytic review, numerical execution and literature evidence.

## Scientific closure and remaining decisions

No outstanding internal proof obligation or subsuming construction was identified
for the fixed conditional theorem. The supporting loss and capture questions are
now quantified. This completes the bounded internal research required for those
claims; it is not an external validation or exhaustive priority certificate.

The [established answers and open questions](../research/CRITICAL_READING.md)
link settled mathematical issues to their proofs and identify unresolved preparation,
joint-resource and significance questions. Correctness, non-subsumption
by inspected sources, and physical significance remain distinct.

Unknown reference-preserving upload, calibration robustness, uniform microscopic
elimination, fixed control bandwidth and a compatible joint device remain conditional
and are not claimed. They are separate research tasks if a device claim is later
requested; component references cannot establish them by accumulation.

Respond to a precise objection with a proof location, correction or counterexample.
Record a newly subsuming source directly. Without a new objection or changed claim,
stop extending this package: more examples or broader receivers do not close the
significance question. No manuscript, submission, invitation or outside contact
without an explicit user instruction.

## Verification and evidence

Read WORKSPACE.md and AGENTS.md. Before changing scientific code, run `python verify.py`.
Keep inherited scripts and references unchanged unless an explicit correction is
recorded. Never regenerate references or widen tolerances to obtain passing CI.

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
report. The eight preserved scientific suites remain 39 groups and 612 cases. The
50 loss checks are supplementary and do not silently revise that historical baseline.
The [reproduction policy](../provenance/REPRODUCTION_POLICY.md) distinguishes assertions,
exact bytes, reviewed numerical agreement and actual execution provenance.

Use native GitHub inline and fenced display mathematics. Inspect rendered expressions
after mathematical edits; structural checks do not substitute for rendering or proof
review. No source-paper PDFs, private contacts or unrelated projects belong here.
