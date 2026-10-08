# Scope and evidence

This repository contains the model, proofs, supporting physical analysis, source
comparisons and reproducible checks for collective emission into one passive
receiving oscillator. The [overview](README.md) gives the physical result; the
[claim and evidence map](research/CLAIM_EVIDENCE_MAP.md) connects each claim to its
proof and tests.

## Results and scope

- The [theorem](research/THEOREM.md) gives the optimized uniform transfer boundary
  and distinguishes it from near-complete mean-photon collection.
- The [two-sector witness](research/TWO_SECTOR_WITNESS.md) shows that two populated
  number levels can expose the critical obstruction.
- The [loss analysis](research/LOSS_COMPETITION.md) and
  [finite-capture bounds](research/PHYSICAL_SCOPE.md) quantify supporting limits
  within their stated effective models.
- The [source comparisons](literature/COMPARISON.md) distinguish inherited
  ingredients from the uniform common-receiver result and identify the versions
  and constructions compared.

The theorem assumes a known symmetric collective source, an arbitrary input state
in the declared excitation code, complete ideal emission and a predetermined passive
receiver retaining one oscillator. The fidelity includes correlations with an
external reference. The [assumption register](literature/ASSUMPTIONS.md) relates
these premises to source and receiver models; the
[physical analysis](research/PHYSICAL_SCOPE.md) treats capture and loss resources.

## Verification

| Evidence | Location |
|---|---|
| Eight scientific suites: 39 groups, 612 cases | [Suite registry](provenance/SUITES.json), [verification commands](README.md#evidence-and-reproduction) |
| 50 supplementary loss checks | [Loss checker](tools/check_loss_competition.py) |
| Reference agreement and evidence protection | [Reproduction policy](provenance/REPRODUCTION_POLICY.md) |
| Mathematical formatting and local links | [Presentation checker](tools/check_presentation.py), [integrity verifier](verify.py) |
| Execution records and protected reference data | [Provenance index](provenance/README.md) |

Numerical checks exercise identities and finite cases; the analytic proofs establish
the uniform limits. Reproduction runs compare fresh outputs with the protected
references.

## Reading

The [reading guide](docs/README.md) uses Kiilerich–Mølmer (2020) as its single
external teaching source. The [local bridge](REVIEW.md) supplies worked examples
and the additional proof steps.

See [Purpose and contact](README.md#purpose-and-contact) for the repository's role
and discussion details.
