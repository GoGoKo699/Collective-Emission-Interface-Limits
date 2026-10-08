# Preparation evidence: conditional symmetric-state constructions

Lemr–Fiurasek and Chen et al. provide two conditional constructions for symmetric atomic targets. This note identifies their controls, approximations and relation to the input resource of the interface theorem. P03/P04 refer to the [source register](SOURCE_EVIDENCE.md).

## P03: Lemr and Fiurasek

Published paper: *Conditional preparation of arbitrary superpositions of atomic Dicke states*, PRA 79, 043808 (2009), DOI 10.1103/PhysRevA.79.043808. The inspected full text is the ten-page author preprint **arXiv:0812.0507v1**, titled *Conditional preparation of arbitrary atomic Dicke states*.

[Author preprint](https://arxiv.org/pdf/0812.0507) · [Published identifier](https://doi.org/10.1103/PhysRevA.79.043808)

Section II, Eqs. (2)-(7), replaces a collective spin component by its mean and uses canonical quadratures. Photon-subtracted squeezed light, QND interaction, homodyne selection and atomic displacements implement conditional filters. Sections III-V analyze acceptance windows and fidelity/success tradeoffs. Section VI, Eqs. (26)-(35), explicitly solves complex three-component targets and discusses higher extensions. Section VII, Eqs. (36)-(40), instead tailors a light state to the desired atomic target; the stated success accounting excludes preparation of that non-Gaussian light.

This construction engineers a specified symmetric target in an oscillator description, with controls chosen for that target. The preprint uses distinct symbols for the highest target number and the atom number.

## P04: Chen et al.

*Carving Complex Many-Atom Entangled States by Single-Photon Detection*, PRL 115, 250502 (2015). Equation references use the complete five-page published article linked below.

[Published full text](https://eapg.mit.edu/wp-content/uploads/2018/03/prl115_quantum_state_carving.pdf) · [Published identifier](https://doi.org/10.1103/PhysRevLett.115.250502)

Equations (1)-(3) specify a uniformly coupled dispersive three-level ensemble and an initial coherent spin state. In Eqs. (4)-(5), spectral amplitudes and photon detection multiply its known Dicke coefficients. Equations (6)-(9) explain the detection-time-dependent phase and collective rotation. Equations (10)-(12) account for finite cooperativity and imperfect spectral discrimination; weak illumination or a single photon limits unobserved-scattering damage.

This finite-spin, heralded target-preparation proposal uses an initial distribution and selected spectrum tailored to the desired state. Its resource accounting includes the success probability, linewidth and conditioning.

## Relation to the interface input

Together with S01/P01/P02 in the [source register](SOURCE_EVIDENCE.md), these papers supply five related preparation approaches, including conditional and approximate constructions.

For the interface theorem, preparing a classically specified target, preparing it on a heralded branch, and coherently accepting an unknown state entangled with a reference are different operational statements. For example, a success operator that multiplies number components by unequal magnitudes changes their relative amplitudes and makes success input-dependent. Preparation of every chosen target by separately selected controls does not by itself establish one input-independent isometry on their span. Conversely, a heralded operation can preserve an unknown code if its successful action is proportional to an isometry there.

The interface theorem starts with an arbitrary input in its declared symmetric space, with coefficients unknown to the receiver. This input may be entangled with an external reference. Realizing that resource from another carrier requires an input-independent encoding, which differs from selected-target control.

The [physical account](../research/STORY.md) explains how these preparation resources relate to the conditional source-to-memory result.
