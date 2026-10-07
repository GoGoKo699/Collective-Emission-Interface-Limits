# Direct comparison of the fixed interface theorem

**Updated 5 October 2026 after the bounded prewriting source refresh.** The source, receiver, target map and theorem are unchanged; the repository preserves eight scientific suites. This is a construction-level literature comparison, not independent proof review or exhaustive priority certification. Identifiers refer to the [source register](SOURCE_EVIDENCE.md).

## The exact question

The result concerns the finite-spin Dicke decay ladder, one waveform chosen before the input is known, canonical number transfer into one retained linear oscillator, worst-input entanglement fidelity over a growing code, and a uniform error estimate. A terminology change or a different objective alone does not establish originality.

## Universal linearized quantum memory

Gorshkov et al. (R04), Sec. IV, Eq. (14), derive retrieval efficiency $C/(1+C)$, independent of control shape for complete retrieval. Appendix A replaces the ground population by $N$ and works to first order in the signal before Eqs. (3)–(5); Eqs. (A17)–(A18) give bosonic commutators and Eqs. (A20)–(A23) specify an occupied field envelope.

This is not just a one-photon or intensity result: the linear vacuum-noise model transfers the quantum state of that mode. Our question retains the number-dependent finite-spin rates discarded in that linearization and asks for uniform channel accuracy. The earlier memory result neither supplies that estimate nor is contradicted by its absence. Our bound is not automatically a theorem about their different Lambda-control protocol.

## Nonlinear emission and selected-mode capture

Khanahmadi et al. (A02), Sec. IV, already distinguish vacuum plus one populated number from two populated numbers. Sec. V, Eqs. (15)–(16), models a capture oscillator; Eq. (17) evaluates selected Fock/cat fidelities, with target cat amplitude varied. Sec. V A optimizes a drive parameter for selected inputs. Number-dependent pulse shapes, degraded superposition transfer, and state-specific optimization are inherited.

Kiilerich and Molmer (R03), Eqs. (2)–(6), supply full quantum-state calculations for any selected output pulse through virtual cascaded oscillators, not only intensity. Our numerical capture calculations apply that method. Neither inspected construction states the present all-waveform worst-Dicke-code converse and controlled joint limit. This does not mean those methods cannot be extended to investigate it.

## Law–Lee: the missing comparison is now complete

The entire six-page article (A03) has been inspected. Its Eqs. (10)–(17) optimize mean photon occupation by diagonalizing a first-order field correlation kernel; Eqs. (18)–(21) define its normalized purity and effective mode number. Its regression formula covers general diagonal Dicke preparations, and its examples include both full inversion and half excitation. It is inaccurate to dismiss the paper as only a fixed-mode or fully inverted calculation.

The [full-text comparison](LAW_LEE_FULL_TEXT.md) identifies the precise differences and overlap. The article does not contain the common-waveform worst-code optimization, a uniform emitted-isometry error over the growing code, or the matching critical converse. Exact rank-one correlation does imply genuine single-mode support; approximate concentration must be translated with a photon-number-dependent error bound. The half-excited semiclassical pulse matches the $a\to1/2$ shape limit of our reference family, but that does not extend our $m=o(N)$ norm theorem to half filling.

Direct attribution now includes its harmonic-oscillator argument (opening of Sec. III and note [16]), dominant two-mode occupation (Sec. III B), and semiclassical hyperbolic-secant pulse (Sec. III C). None is advertised as a new discovery. Its time-dependent modes at a fixed collection time also define receiving envelopes, so 'dynamic versus fixed' is not our novelty distinction.

## Tziperman: full-state transfer with an input-selected mode

The [main-article and supplement reading](TZIPERMAN_FULL_TEXT.md) directly credits
their collective source, dominant-mode selection, full output density matrix and
selected-state transfer calculations. The cavity-free symmetric limit overlaps our
source. Their fixed-cat emitter-number study and constant-excitation discussion do
not state the uniform growing-code/all-waveform boundary. The difference is not
that they study only photon occupation: they use occupation to select a mode and
then calculate its full quantum state. No subsumption of the present theorem was
found in these inspected constructions; that is a scoped conclusion.

## Other controlled limits and attribution anchors

The [prewriting comparison](PREWRITING_SEARCH_2026_10_05.md) adds Porras–Cirac's
bosonic atom-to-light mapping, Perarnau-Llobet et al.'s full-state few-mode
projections, and Belliardo et al.'s optimized parameter readout. It records their
equations and source versions, credits the inherited capabilities, and explains
why these inspected constructions do not supply the present common-code theorem.
The result does not imply failure of useful metrological readout.

Lemberger–Molmer (S04), Sec. 2.2, Eq. (7), analyze mean radiation eigenmode occupations. Malz–Trivedi–Cirac (S06) establish controlled large-$N$ reduced atomic dynamics from full inversion. Without additional bounds those observables do not give a uniform outgoing-field isometry or the present worst-input transfer fidelity.

Paulisch (A01) supplies the exact cascade, conventional exponential overlap, useful-channel collection product, and prior discussion of number-state mapping and pulse shaping. The conventional cubic correction already suggests the $N^{2/3}$ scale. The candidate advance is the optimized uniform boundary, not the first appearance of that exponent.

## Outcome

**The core is preserved against the inspected full-text comparisons, including Law–Lee and Tziperman; no theorem correction or subsumption was established.** The named missing-source tasks are resolved. This does not establish exhaustive novelty or submission readiness.

The strongest remaining contribution is the sharp optimized uniform distinction between faithful canonical state transfer and mean-photon collection for the stated collective source and one linear memory. Explicitly excluded claims include a new Dicke cascade, first mode optimization, first recognition of number-dependent pulses, first two-mode description, a new oscillator comparator or capture formalism, failure of established linearized memory theory, and limits on unrestricted nonlinear decoding.

Remaining work is a separate critical reading of [THEOREM.md](../research/THEOREM.md) and the specific preparation/realization evidence deficits. No outside contact has occurred. No new Hamiltonian or receiver class has been introduced to avoid those questions. See [Purpose and contact](../README.md#purpose-and-contact) for the repository's learning role and discussion details.
