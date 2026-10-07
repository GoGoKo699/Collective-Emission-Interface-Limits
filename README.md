# Collective Emission Interface Limits

**Almost complete photon collection does not guarantee faithful quantum-state transfer.**

A symmetric ensemble stores an unknown quantum state and releases its excitations as light.
A receiver, configured before the input is known, retains one oscillator. The question is
when the collective spin can be treated as a harmonic oscillator for this transfer—not
merely for the average number of photons it delivers.

| Read next | Purpose |
|---|---|
| [Reading guide](docs/README.md) · [Tutorial-to-theorem bridge](REVIEW.md) | Learn from one external tutorial and local worked examples |
| [Theorem](research/THEOREM.md) · [Claim and evidence map](research/CLAIM_EVIDENCE_MAP.md) | Follow the result, proof dependencies and supporting consequences |
| [Physical scope](research/PHYSICAL_SCOPE.md) · [Prior-work comparison](literature/COMPARISON.md) | Check receiver restrictions, realization limits and attribution |
| [Verification](#evidence-and-reproduction) · [Scope and evidence](STATUS.md) | Inspect executable evidence and the remaining limits |
| [LLM guide](llms.txt) · [Workspace](WORKSPACE.md) | Identify relevant questions and authoritative files for further reading |

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
[standalone theorem](research/THEOREM.md) supplies the construction, unrestricted-waveform
converse and finite bounds; the [explicit proof correction](research/PROOF_AUDIT.md)
remains part of the record.

## Why the two criteria differ

The collective ladder decays at $`\gamma k(N-k+1)`$, rather than the oscillator rate
$`\gamma Nk`$. Each known subextensive photon number can be matched to an excellent
individual pulse. But different numbers prefer slightly different pulses.

A pulse difference of order $`M/N`$ produces a one-photon mismatch of order
$`(M/N)^2`$. Requiring all photons in a many-photon component to occupy the receiving
mode amplifies this into the scale $`M^3/N^2`$. The proof controls the correlated emitted
field before making that product-pulse comparison; independence is not assumed.

Even one logical qubit can witness the critical limit: use the populated numbers
$`\lfloor M/4\rfloor`$ and $`M`$. Their physical excitation numbers grow. Vacuum plus one
populated number is a different, successful comparator. See the
[two-sector witness](research/TWO_SECTOR_WITNESS.md).

## One tutorial, then this result

The selected learning anchor is:

> A. H. Kiilerich and K. Mølmer, **Quantum interactions with pulses of radiation**,  
> *Physical Review A* **102**, 023717 (2020).  
> [Author tutorial, arXiv:2003.04573](https://arxiv.org/abs/2003.04573) ·
> [Published article](https://doi.org/10.1103/PhysRevA.102.023717)

Its virtual input/output cavities give the physical language of the interface. The
[reading guide](docs/README.md) maps its sections to this repository. The
[tutorial-to-theorem bridge](REVIEW.md) supplies the missing Dicke-ladder, fidelity and
uniform-bound steps locally; no second external tutorial is required.
Worked emission, mode-mismatch and coherence examples lead into the proof;
loss and finite capture follow as supporting lessons. The
[documentation map](docs/README.md#repository-map) locates the supporting material.

## Boundaries and prior work

The ideal source is symmetric, has known $`N`$, and emits completely into one vacuum
Markov channel. The receiver retains one oscillator after fixed passive processing.
The full emitted field retains the information; several retained modes, nonlinear
decoding or a different encoding change the task. Preparation, loss, duration and
bandwidth are real resources, not a demonstrated joint apparatus.

The Dicke cascade, conventional-pulse cubic mismatch, number-dependent temporal modes,
mean-occupation optimization and pulse-capture formalism have direct predecessors.
The [comparison](literature/COMPARISON.md) and [background dossier](literature/BACKGROUND.md)
separate those ingredients from the optimized uniform limit. The
[Tziperman comparison](literature/TZIPERMAN_FULL_TEXT.md) examines its overlapping
collective source and selected-state transfer construction. No subsumption of the
uniform common-code theorem was found in the inspected versions. The
[scope and evidence page](STATUS.md) links the physical limits and verification records.

## Evidence and reproduction

```sh
python -m pip install -r requirements.txt
python tools/check_presentation.py
python tools/check_loss_competition.py
python verify.py --integrity-only
python verify.py --artifacts-dir verification-artifacts --require-reference
```

The eight scientific suites cover 39 groups and 612 cases. The scientific scripts and
saved results are preserved; generated outputs are compared without rewriting references.
The [reproduction policy](provenance/REPRODUCTION_POLICY.md) distinguishes exact bytes,
reviewed numerical agreement and passing assertions. None is independent proof review.
The presentation check is separate from the scientific test count.
The supplementary loss-competition checks are also counted separately; their
[execution record](provenance/PREWRITING_2026_10_05.json) identifies methods and limitations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) describes relevant research questions, search terms and the
authoritative reading order for automated assistants and other readers.
The [workspace](WORKSPACE.md) and [current work order](work_orders/CURRENT.md) describe
continuing work. Code is available under the [MIT license](LICENSE).
