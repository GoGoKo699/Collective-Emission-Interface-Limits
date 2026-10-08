# Direct comparison of the fixed interface theorem

This comparison identifies the source models, optimized quantities and asymptotic guarantees in the closest references. Identifiers refer to the [source register](SOURCE_EVIDENCE.md).

## The exact question

The result concerns the finite-spin Dicke decay ladder, one waveform chosen before the input is known, canonical number transfer into one retained linear oscillator, worst-input entanglement fidelity over a growing code, and a uniform error estimate.

## Universal linearized quantum memory

Gorshkov et al. (R04), Sec. IV, Eq. (14), derive retrieval efficiency $`C/(1+C)`$, independent of control shape for complete retrieval. Appendix A replaces the ground population by $`N`$ and works to first order in the signal before Eqs. (3)–(5); Eqs. (A17)–(A18) give bosonic commutators and Eqs. (A20)–(A23) specify an occupied field envelope.

The linear vacuum-noise model transfers the quantum state of that mode. Our question retains the number-dependent finite-spin rates discarded in that linearization and controls channel accuracy uniformly on a growing code. The models therefore use different approximations and source dynamics.

## Nonlinear emission and selected-mode capture

Khanahmadi et al. (A02), Sec. IV, distinguish vacuum plus one populated number from two populated numbers. Sec. V, Eqs. (15)–(16), models a capture oscillator; Eq. (17) evaluates selected Fock/cat fidelities, with target cat amplitude varied. Sec. V A optimizes a drive parameter for selected inputs. Number-dependent pulse shapes, degraded superposition transfer, and state-specific optimization are inherited.

Kiilerich and Molmer (R03), Eqs. (2)–(6), supply full quantum-state calculations for any selected output pulse through virtual cascaded oscillators. Our numerical capture calculations apply that method; the common-waveform converse and controlled growing-code limit are established in the [theorem](../research/THEOREM.md).

## Law–Lee: optimized occupation and whole-state fidelity

In the six-page article (A03), Eqs. (10)–(17) optimize mean photon occupation by diagonalizing a first-order field correlation kernel; Eqs. (18)–(21) define its normalized purity and effective mode number. Its regression formula covers general diagonal Dicke preparations, and its examples include both full inversion and half excitation.

The [full-text comparison](LAW_LEE_FULL_TEXT.md) identifies the precise differences and overlap. Its optimized observable is mean occupation, whereas the theorem here optimizes worst-code fidelity and bounds the emitted-isometry error uniformly. Exact rank-one correlation does imply genuine single-mode support; approximate concentration must be translated with a photon-number-dependent error bound. The half-excited semiclassical pulse matches the $`a\to1/2`$ shape limit of our reference family, but that does not extend our $`m=o(N)`$ norm theorem to half filling.

Direct predecessors include its harmonic-oscillator argument (opening of Sec. III and note [16]), dominant two-mode occupation (Sec. III B), and semiclassical hyperbolic-secant pulse (Sec. III C). Its time-dependent modes at a fixed collection time define receiving envelopes in the same sense used here.

## Tziperman: full-state transfer with an input-selected mode

The [main-article and supplement reading](TZIPERMAN_FULL_TEXT.md) directly credits
their collective source, dominant-mode selection, full output density matrix and
selected-state transfer calculations. The cavity-free symmetric limit overlaps our
source. Their fixed-cat emitter-number study and constant-excitation discussion address
selected-input transfer. They use occupation to select a mode and then calculate
its full quantum state. The common-receiver theorem adds a uniform guarantee and
a matching converse for a growing unknown input code.

## Other controlled limits and attribution anchors

The [additional source comparisons](PREWRITING_SEARCH_2026_10_05.md) cover Porras–Cirac's
bosonic atom-to-light mapping, Perarnau-Llobet et al.'s full-state few-mode
projections, and Belliardo et al.'s optimized parameter readout, with equations
and source versions. These tasks respectively concern bosonic state mapping,
few-mode representations and parameter estimation.

Lemberger–Molmer (S04), Sec. 2.2, Eq. (7), analyze mean radiation eigenmode occupations. Malz–Trivedi–Cirac (S06) establish controlled large-$`N`$ reduced atomic dynamics from full inversion. The theorem here controls the outgoing-field isometry and worst-input transfer fidelity rather than these reduced observables.

Paulisch (A01) supplies the exact cascade, conventional exponential overlap, useful-channel collection product, and prior discussion of number-state mapping and pulse shaping. The conventional cubic correction already suggests the $`N^{2/3}`$ scale. The result here gives the optimized uniform boundary at that scale.

## Contribution and scope

The contribution is the sharp optimized uniform distinction between faithful canonical state transfer and mean-photon collection for the stated collective source and one linear memory. It builds on the cascade, natural-mode optimization, number-dependent pulses, oscillator comparison and capture formalisms attributed above.

The [physical account](../research/STORY.md) explains the transfer-versus-collection distinction; the [physical analysis](../research/PHYSICAL_SCOPE.md) quantifies receiver and source resources.
