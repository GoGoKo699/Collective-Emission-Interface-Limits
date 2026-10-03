# Collective Emission Interface Limits

**Almost complete photon collection does not guarantee faithful quantum-state transfer.**

This project studies a symmetric ensemble of two-level emitters releasing an unknown quantum state into a traveling field. A receiver is chosen before the input is known and retains one bosonic memory mode. We determine when the finite spin can be treated as a linear oscillator for that task—not merely for its average emitted intensity.

## The central result

Let $N$ be the number of emitters and let the stored state occupy Dicke excitation numbers $0,\ldots,M$. For complete ideal collective decay and a predetermined, photon-number-preserving linear receiver with vacuum auxiliaries, define $\mathcal F_{N,M}$ as the best worst-input entanglement fidelity for the canonical number map into one oscillator.

The recorded derivation gives

$$
\frac{M}{N^{2/3}}\longrightarrow c>0
\quad\Longrightarrow\quad
\mathcal F_{N,M}\longrightarrow e^{-c^3/192}.
$$

The optimum tends to one for $M=o(N^{2/3})$ and to zero when $M/N^{2/3}\to\infty$. Nevertheless, one fixed waveform collects a mean photon fraction tending to one throughout every $M=o(N)$ code. For example, $M=\lfloor N^{3/4}\rfloor$ has vanishing excitation density and asymptotically complete mean collection, but vanishing worst-input one-mode transfer fidelity.

This is a distinction between an intensity observable and a quantum channel. It is not destruction of information in the complete emitted field, a quantum-capacity bound, or a limitation on every possible nonlinear receiver.

## A small logical code already exposes the limitation

The critical limit is already witnessed by the two-dimensional code spanned by excitation numbers $\lfloor M/4\rfloor$ and $M$. Its two states become individually well matched to different pulses, but no single pulse handles both better than the critical bound. The number of logical basis states need not grow. Their excitation energies do grow.

The new finite two-sector calculation is in [the scope note](research/TWO_SECTOR_WITNESS.md). This is a corollary of the existing two-sector converse, not a separate claimed physical mechanism or an optimization over all encodings.

## Read the science

| Document | Role |
|---|---|
| [Model and proof](research/THEOREM.md) | The source, fidelity convention, uniform state approximation, all-waveform converse, and mean-collection comparison |
| [Proof audit and correction](research/PROOF_AUDIT.md) | Endpoint-safe finite bounds, answers to the proof checklist, and explicit author-side review limits |
| [Two-sector witness](research/TWO_SECTOR_WITNESS.md) | Why one logical qubit suffices; finite constructive and converse bounds |
| [Physical scope](research/PHYSICAL_SCOPE.md) | Passive reception, two-mode error structure, loss, bandwidth, and known ways outside the theorem |
| [Prior results and open comparisons](literature/PRIOR_ART.md) | Exact attribution and access status, not a priority certificate |
| [Law–Lee full-text comparison](literature/LAW_LEE_FULL_TEXT.md) | Completed equation-level comparison; inherited oscillator, few-mode and pulse results, and the remaining interface claim |
| [Assumption register](literature/ASSUMPTIONS.md) | Model idealizations, receiver restrictions, and unfinished implementation checks |
| [Status](STATUS.md) | Completed author-side results and remaining research tasks |

## Reproduce

The numerical work consists of small exact cascades, finite matrices, scalar bounds, and analytical controls. No external service, large many-body simulation, or quantum random-access memory is required.

```sh
python -m pip install -r requirements.txt
python verify.py --integrity-only
python verify.py --output verification-report.json
```

The eight standalone suites cover waveform overlap, common-mode optimization, passive capture, the leading second temporal mode, photon collection, source-rate consistency, the two-sector witness, and the endpoint-safe proof audit. The seven pre-existing scripts and reference results are preserved byte-for-byte; the eighth supplies explicit finite proof controls. The runner never overwrites saved reference results.

The reference environment is Python 3.13.5 with the pinned dependencies. Exact-byte equality is a reproducibility property of that environment, not a proof of analytical claims. Numerical tails and integration tolerances are distinguished in the tests. Neither code execution nor this repository substitutes for independent scientific assessment.

## Boundaries that stay visible

The ideal theorem assumes a known symmetric source, one accessible vacuum Markov channel, and a particular downstream receiver class. Individually matched emissions, sparse encodings, parameter estimation, and full-field nonlinear decoding are different tasks. The preparation and receiving controls are not free, and the large-$N$ limit is not a fixed-bandwidth, fixed-time device claim.

The fidelity exponent suggested by a standard exponential pulse, the Dicke cascade, nonlinear-emission mode dependence, and passive-capture theory all have direct predecessors. The candidate contribution is the optimized **uniform** interface boundary and the comparison with mean photon collection.

**Manuscript writing is on hold.** Collaboration inquiries are welcome; contact Ruge Lin.
