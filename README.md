# Collective Emission Interface Limits

**Almost complete photon collection does not guarantee faithful quantum-state transfer.**

A symmetric ensemble stores an unknown quantum state and releases its excitations as light.
A receiver configured in advance must reproduce every excitation amplitude and
coherence in one output oscillator. A single passive mode has a sharp transfer
limit. Capturing several modes and coherently combining them raises that limit.

| Read next | Purpose |
|---|---|
| [Scientific account](science/README.md) · [Model and objective](science/MODEL.md) | Enter the connected account through its definitions and proof dependencies |
| [Common-mode boundary](science/COMMON_MODE_BOUNDARY.md) · [Multimode receiver](science/MULTIMODE_RECEIVER.md) | Compare the sharp limits and receiver constructions |
| [Learning route](learning/README.md) · [30 milestones](learning/MILESTONES.md) · [Source bridge](learning/KIILERICH_MOLMER_BRIDGE.md) | Build understanding from one educational anchor and local worked examples |
| [Bounded receiver](science/BOUNDED_RECEIVER.md) · [Physical scope](science/PHYSICAL_SCOPE.md) · [References](references/README.md) | Find the sharp receiving-rate and time costs, realization limits and attribution |
| [Verification guide](verification/README.md) | Reproduce the scientific checks and interpret the evidence |
| [LLM guide](llms.txt) | Identify relevant questions and authoritative files for further reading |

## Model and transfer task

| Task | What one receiving pulse must preserve |
|---|---|
| Photon collection | Nearly all the mean photon number |
| Canonical quantum-state transfer | Every number amplitude and coherence in the declared input space, including correlations with an external reference |

The source has $`N`$ emitters and supports excitation numbers $`0,\ldots,M`$, with $`M\leq N`$.
The intended map uses the **same** normalized temporal mode $`f`$ for every input:

```math
\sum_{m=0}^{M}c_m\lvert D_N^m\rangle
\longmapsto
\sum_{m=0}^{M}c_m\lvert m\rangle_f.
```

One spatial output channel can contain many temporal modes. Capturing the beam is not
therefore the same operation as storing its state in one oscillator.

## The common-mode boundary

Let $`\mathcal F_{N,M}`$ be the optimized worst-input squared entanglement fidelity for
complete ideal collective decay and a predetermined, photon-number-preserving linear
receiver with vacuum auxiliaries. The optimization allows **every common waveform**.

```math
\boxed{
\frac{M}{N^{2/3}}\longrightarrow c>0
\quad\Longrightarrow\quad
\mathcal F_{N,M}\longrightarrow e^{-c^3/192}
}
```

The fidelity tends to one for $`M=o(N^{2/3})`$ and to zero when
$`M/N^{2/3}\to\infty`$. In contrast, one fixed waveform collects a mean photon fraction
tending to one throughout $`M=o(N)`$. Taking $`M=\lfloor N^{3/4}\rfloor`$ gives

```math
\begin{aligned}
M/N &\longrightarrow 0,\\
\text{mean collected photon fraction} &\longrightarrow 1,\\
\text{optimal worst-input fidelity} &\longrightarrow 0.
\end{aligned}
```

This is a uniform channel limitation, not a statement that every input fails. The
[boundary proof](science/COMMON_MODE_BOUNDARY.md) supplies the construction,
all-waveform converse and finite bounds. The
[photon-collection proof](science/PHOTON_COLLECTION.md) establishes the larger
domain for the mean collected fraction.

## How receiving controls limit the single oscillator

Let $`B`$ be the receiver's maximum intensity in the source clock
$`\tau=N\gamma t`$. At $`M/N^{2/3}\to c>0`$, the optimized single-oscillator
fidelity with $`B/M\to r>0`$ tends to

```math
\exp\!\left[-\lambda-\frac{(A/4-\lambda)_+^2}{A}\right],
\qquad A=\frac{c^3}{12},\qquad \lambda=\frac{\ln 4-1}{r}.
```

When the cap grows more slowly than $`M`$, fidelity vanishes. A cap growing
faster than $`M`$ recovers the ideal common-mode limit. If the receiver also
stops at $`T=\ln M+s+o(1)`$ in the source clock, add $`e^{-s}`$ to
$`\lambda`$. The [bounded-receiver proof](science/BOUNDED_RECEIVER.md)
gives an explicit control and a converse for every allowed coupling schedule.
The physical rate cap is $`N\gamma B`$.

## How additional modes extend the excitation ceiling

The [multimode receiver](science/MULTIMODE_RECEIVER.md) passively captures a fixed
$`K`$-dimensional temporal subspace. Its decoder then rotates the captured modes
coherently according to their total photon number and writes the state into one
oscillator. The rotation preserves coherences between different numbers without
measuring them.

For fixed $`K\geq1`$, the optimized worst-input fidelity satisfies

```math
\frac{M}{N^{2K/(2K+1)}}\longrightarrow c>0
\quad\Longrightarrow\quad
\mathcal F^{(K)}_{N,M}\longrightarrow
\exp\!\left[-\frac{c^{2K+1}}{16^K(2K+1)\binom{2K}{K}^2}\right].
```

| Captured modes | Critical excitation scale | Fidelity at the critical scale |
|---:|---|---|
| 1 | $`N^{2/3}`$ | $`\exp(-c^3/192)`$ |
| 2 | $`N^{4/5}`$ | $`\exp(-c^5/46080)`$ |
| 3 | $`N^{6/7}`$ | $`\exp(-c^7/11468800)`$ |

For example, at $`M=\lfloor N^{3/4}\rfloor`$ the single-mode fidelity tends to
zero and the two-mode fidelity tends to one. The proof gives explicit waveforms,
a converse over every common capture subspace and a finite capture construction.
A receiver whose entire optical processing stays linear and ends in one oscillator
still has the one-mode bound.

## Why the two criteria differ

The collective ladder decays at $`\gamma k(N-k+1)`$, rather than the oscillator rate
$`\gamma Nk`$. Each known subextensive photon number can be matched to an excellent
individual pulse. But different numbers prefer slightly different pulses.

A pulse difference of order $`M/N`$ produces a one-photon mismatch of order
$`(M/N)^2`$. Requiring all photons in a many-photon component to occupy the receiving
mode amplifies this into the scale $`M^3/N^2`$. The [matched-pulse argument](science/MATCHED_PULSES.md) controls the correlated
emitted field before making that product-pulse comparison; independence is not assumed.

Even one logical qubit can witness the critical limit: use the populated numbers
$`\lfloor M/4\rfloor`$ and $`M`$. Their physical excitation numbers grow. Vacuum plus one
populated number is a different, successful comparator. See the
[two-sector witness](science/TWO_SECTOR_WITNESS.md).

## One tutorial, then this result

The selected learning anchor is:

> A. H. Kiilerich and K. Mølmer, **Quantum interactions with pulses of radiation**,  
> *Physical Review A* **102**, 023717 (2020).  
> [Author tutorial, arXiv:2003.04573](https://arxiv.org/abs/2003.04573) ·
> [Published article](https://doi.org/10.1103/PhysRevA.102.023717)

Its virtual input/output cavities give the physical language of the interface. The
[learning guide](learning/README.md) maps its sections to this repository. The
[source-to-project bridge](learning/KIILERICH_MOLMER_BRIDGE.md) supplies the additional Dicke-ladder, fidelity and
uniform-bound steps locally; no second external tutorial is required.
Worked emission, mode-mismatch and coherence examples lead into the proof;
loss and finite capture supply the physical qualifications.

The [30-milestone map](learning/MILESTONES.md) has two phases. M01–M12 assemble
the pulse, source and channel framework; M13–M30 connect the controlled field
approximation, receiver optimization and physical consequences into the whole
result, including the multimode extension. Each milestone states a central question, understanding target,
dependencies, conceptual connection and source pointers. It is a shared map of
the science, independent of a reader's prior knowledge or learning history.

## Boundaries and prior work

The ideal source is symmetric, has known $`N`$, and emits completely into one vacuum
Markov channel. Both receiver classes output one oscillator. The multimode
class additionally uses several capture oscillators and a number-dependent
coherent decoder.
The input is an arbitrary state in the symmetric excitation code, including its
correlations with a reference. The full emitted field retains that information;
the theorem quantifies transfer into the specified single receiving oscillator.
The [physical analysis](science/PHYSICAL_SCOPE.md) gives the loss, duration and
coupling requirements for capture.

The [loss-competition result](science/LOSS_COMPETITION.md) also identifies when
prescribed mode-independent transmission loss masks the common-mode limitation.
Its pure-loss channel is distinct from independent atomic decay and from
mode-dependent filtering. Finite capture is quantified on the same excitation
code, with coupling and duration allowed to scale with that code.

The Dicke cascade, conventional-pulse cubic mismatch, number-dependent temporal modes,
mean-occupation optimization and pulse-capture formalism have direct predecessors.
The [comparison](references/COMPARISON.md) and [background account](references/BACKGROUND.md)
separate those ingredients from the optimized uniform limit. The
[Tziperman comparison](references/TZIPERMAN_FULL_TEXT.md) examines its overlapping
collective source and selected-state transfer construction alongside the uniform
common-code guarantee. The
[interpretation](science/INTERPRETATION.md) connects the consequences, while the
[verification guide](verification/README.md) locates their executable checks.

## Evidence and reproduction

```sh
python -m pip install -r requirements.txt
python tools/check_presentation.py --self-test
python verify.py --integrity-only
python verify.py --artifacts-dir verification-artifacts --require-reference
python tools/check_loss_competition.py --output loss-competition-report.json
python tools/check_bounded_receiver.py
python tests/09_multimode_receiver/checks.py --output multimode-receiver-report.json
```

The eight scientific suites cover 39 groups and 612 cases. The scientific scripts and
saved results are preserved; generated outputs are compared without rewriting references.
The [reproduction policy](provenance/REPRODUCTION_POLICY.md) distinguishes exact bytes,
reviewed numerical agreement and passing assertions.
The presentation check is separate from the scientific test count.
The loss-competition and multimode receiver checks are supplementary. The
[verification guide](verification/README.md) explains the commands, expected
outputs and the distinction between finite calculations and analytical proof.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) describes relevant research questions, search terms and the
authoritative reading order for automated assistants and other readers.
Code is available under the [MIT license](LICENSE).
