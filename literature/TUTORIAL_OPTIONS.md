# Three single-source tutorial options

**3 October 2026. Recommendation pending the owner's choice.** Each option is one external source, not one item in a three-source syllabus. The goal is to put a reader close to the fixed source-to-memory result, not to find a source that already proves its candidate new theorem. No tutorial-dependent reorganization has been performed.

## Recommendation

**Choose Kiilerich and Mølmer (2020), *Quantum interactions with pulses of radiation*.** It gives the shortest verified operational path from a traveling quantum pulse through a local source to the state captured in a selected oscillator. Its introduction explicitly says that it reviews and expands the preceding Letter. It is a tutorial-style review-and-method paper, not a textbook or a journal article formally classified here as a review.

The other two options are genuine broad reviews. Raymer–Walmsley is gentler on what a temporal mode means; Combes–Kerckhoff–Sarovar is stronger and longer on network mathematics and approximation assumptions. The recommendation reflects this project's bottleneck, not a universal ranking of the sources.

| Single source | Most useful strength | Remaining bridge to this repository | Relative burden |
|---|---|---|---|
| Kiilerich–Mølmer 2020 | Full quantum state of an input/output pulse; cascaded oscillator realization | Symmetric Dicke cascade, canonical worst-input fidelity and uniform converse | Shortest route to the actual task |
| Raymer–Walmsley 2020 | Temporal modes, quantum states, mode-selective storage and manipulation | Master-equation cascade plus the whole channel/proof layer | Gentlest conceptual entrance |
| Combes–Kerckhoff–Sarovar 2017 | Markov input–output networks, passive systems, stochastic dynamics and limitations | Specialize the source and derive the waveform minimax | Most systematic; substantially longer |

The gap columns are intentional. None of these sources, by itself, contains the sharp optimized growing-code result. The repository should supply the short missing derivations rather than quietly require another external book.

## Option 1 — closest to the source-to-memory operation

**Alexander Holm Kiilerich and Klaus Mølmer, *Quantum interactions with pulses of radiation*, Physical Review A 102, 023717 (2020).**

[Author preprint, arXiv:2003.04573](https://arxiv.org/abs/2003.04573) · [Published identifier](https://doi.org/10.1103/PhysRevA.102.023717)

**Access checked:** the complete 15-page arXiv PDF was available; the reading recommendation is tied to its section and equation labels. The publisher record confirms the published title and identifier. A line-by-line comparison between author and publisher versions is not claimed.

### Read this route inside the one source

1. **Section I:** distinguish a cavity eigenmode from a traveling pulse. The photon number and wavepacket shape can change together in a nonlinear interaction; mean field and intensity need not specify the emitted quantum state.
2. **Section II A, Eqs. (2)–(12):** a Lindblad source and a time-dependent virtual input oscillator; input–output relations; how a normalized envelope becomes a quantum mode.
3. **Section II B, Eqs. (13)–(15):** intensity, regression and the most populated natural modes.
4. **Section II C:** a selected output pulse represented by an absorbing oscillator, with other output modes traced out. This is the closest entrance to our actual receiver.
5. **Section III:** several pulse modes and their joint state. Read this to understand the supporting two-mode discussion, without making multimode decoding the new project.

Sections IV–V provide further applications, including blockade and thermal fields, but are not required to understand the present vacuum-channel result. Their additional controls are not silently part of our receiver class.

### What the reader would already understand

After this route, a reader can identify the quantum system, useful channel, normalized pulse, selected memory and discarded output. They can understand why a photon-number-dependent pulse is problematic for an unknown superposition and how to compute its selected-mode density matrix. They also see that full-state output calculations, rather than just mean occupations, are established prior art.

### What we would add after the choice

The bridge should introduce the exact symmetric ladder and its labeled-time cascade, then the canonical number map and squared entanglement fidelity. It should derive why positive number-lowering channels reduce the optimized worst-input problem to number-state overlaps. Finally it should present the uniform pulse approximation and finite all-waveform bounds as the project-specific step. The reader need not take an additional course in general stochastic network synthesis.

**Prerequisites:** ordinary quantum mechanics, density matrices, oscillator creation operators and basic differential equations. The source starts from a master equation; it is not a first introduction to quantum mechanics. Our repository can explain the needed dissipator and fidelity identities locally.

**Main limitation:** this source does not teach a full Dicke multiphoton cascade or the information-theoretic uniform proof. It is the closest operational tutorial, not the closest source of every formula.

## Option 2 — clearest entry to modes versus quantum states

**Michael G. Raymer and Ian A. Walmsley, *Temporal modes in quantum optics: then and now*, Physica Scripta 95, 064002 (2020).**

[Review preprint, arXiv:1911.06771](https://arxiv.org/abs/1911.06771) · [Published identifier](https://doi.org/10.1088/1402-4896/ab6153)

**Access checked:** the complete 29-page arXiv PDF. The theory page displaying Fock/coherent/squeezed states in one temporal mode was also inspected visually; numerical values from experimental figures are not used as device evidence here.

### Read this route inside the one source

Begin with **Section 3, “Temporal Modes Theory—Discretizing the Continuum”**, particularly Eqs. (6)–(13). Continue through **Section 4** on bipartite oscillator interactions, **Section 6, “Quantum Optical Memory”**, and **Section 7** on temporal-mode selectivity. Sections 1–2 provide historical motivation and correlation-mode background. Section 5's frequency-conversion examples are useful illustrations, not mandatory additional physics.

### Why it fits

This review is especially good for a reader who is comfortable with quantum computing but has not internalized why one optical port can contain many temporal oscillators. It keeps the distinction between the mode function and the quantum state carried by that function visible. Its memory and mode-selection discussion makes the receiver restriction intelligible before confronting the source dynamics.

### What would still be missing

We would have to add the collective Lindblad ladder, exact emitted field, cascaded capture equations and quantum-channel proof. Its use of mode transformations and nonlinear optical media must be translated at the effective operator level: a number-preserving beam-splitter transformation is not the same resource as gain or squeezing. The review's experimental memories do not prove a joint Dicke-source apparatus.

**Best reason to choose it:** a gentler conceptual front door. **Reason it ranks second here:** the bridge to the actual source-to-capture calculation is longer than in Option 1.

## Option 3 — strongest systematic mathematical foundation

**Joshua Combes, Joseph Kerckhoff and Mohan Sarovar, *The SLH framework for modeling quantum input-output networks*, Advances in Physics: X 2, 784–888 (2017).**

[Review preprint, arXiv:1611.00375](https://arxiv.org/abs/1611.00375) · [Published identifier](https://doi.org/10.1080/23746149.2017.1343097)

**Access checked:** the complete 69-page arXiv PDF, including its table of contents and relevant theory sections. Page numbers below are the arXiv manuscript's printed numbers, not the journal's 784–888 pagination.

### Read this route inside the one source

Use **Section III, pp. 7–12**, for input–output relations and cascaded systems. Read **Section IV, pp. 13–16**, for the stochastic notation when needed; **Section V A and V D**, for the $(S,L,H)$ description and its master equation; and **Section VI A, beginning p. 29**, for passive linear networks. **Section VII A**, especially its Fock-state discussion, supplies quantum-input context. The loss and adiabatic-elimination parts of Section VII are useful for the source-realization boundary, not prerequisites for the ideal minimax.

### Why it fits

This is the most systematic single reference for the receiving-network reduction, vacuum noise, cascading, coherent feedback and the approximations behind the model. It explicitly separates passive and active linear systems. It is a good choice for a control theorist or a reader who wants to reconstruct network equations rather than start from a virtual-cavity recipe.

### What would still be missing

The review does not provide our Dicke-specific emitted pulse, exact reference kernel or growing-code minimax. Its broad network machinery is substantially more than the main proof needs. Source-changing feedback and active networks appearing in the review remain outside our fixed theorem. In this review, $S$ in the SLH triple is a scattering operator, not the collective spin.

**Best reason to choose it:** rigorous network and approximation bookkeeping. **Reason it ranks third for this task:** a longer learning investment before reaching the distinctive result.

## Why the dissertation is an attribution anchor rather than a fourth syllabus

Paulisch's *Waveguide Quantum Electrodynamics* dissertation is the closest existing source for several inherited source formulas. Chapter 0.3 introduces waveguide light–matter dynamics; Chapter 1.1–1.2 and Appendix 1.A supply generation and input–output context. The exact cascade, conventional-pulse overlap, loss product and pulse-shaping discussion must be credited there and in the associated papers.

That makes it a crucial scientific reference. It is a doctoral research thesis rather than the textbook/review category requested for the single learning anchor, and its source-generation emphasis does not by itself supply the whole receiver and fidelity route. It is not being made an undeclared second prerequisite to any option above. The short needed source derivation will live in the repository's bridge.

## Selection and the next stage

The owner should choose one source before the reading order, examples and notation are furnished around it. At that stage preserve the existing theorem and provenance, use the chosen source's terminology where compatible, and explicitly translate differing rate, field and fidelity conventions. Keep the bridge limited to what that one source omits. Do not manufacture a percentage-of-coverage score or imply that learning a review establishes novelty.

This recommendation concerns pedagogy. The newly identified Tziperman et al. construction-level comparison and the separate critical reading remain scientific tasks regardless of which tutorial is chosen; see [BACKGROUND_AUDIT.md](BACKGROUND_AUDIT.md).
