# One source, two notions of an accurate interface

The model, code, receiver and fidelity convention are defined in
[THEOREM.md](THEOREM.md).

## The transfer task

The result identifies when a weakly excited collective spin is an adequate oscillator for transferring an unknown quantum state.

Take a symmetric ensemble of $`N`$ two-level emitters. Its stored excitations radiate into one useful spatial channel. A receiver is configured in advance and retains one oscillator, corresponding to one temporal pulse shape. The receiver must preserve an unknown superposition of excitation numbers, not merely capture its average photon number. A single spatial channel still contains many temporal modes.

## The mechanism

The ideal collective ladder has decay rates $`\gamma k(N-k+1)`$, rather than the oscillator's $`\gamma Nk`$. The finite-spin correction slightly changes the pulse as the excitation number changes. An individually known subextensive number $`m`$ can be matched to its own excellent pulse. This does not imply one pulse works equally well for several possible populated numbers.

The intuitive scaling is simple. A pulse-shape difference of order $`M/N`$ gives a missed fraction of order $`(M/N)^2`$. A many-photon state is sensitive to whether even one photon occupies a different mode; a number of order $`M`$ amplifies that small mismatch to an effect of order $`M^3/N^2`$. This is an explanation of the proved result, not a substitute for its all-waveform converse. The exact photons are not assumed independent; the uniform approximation justifies the product-pulse comparison.

## The result

For the complete code of excitation numbers $`0`$ through $`M`$, optimize the worst-input entanglement fidelity over every common receiving waveform. Within the declared ideal source and passive linear receiver class,

```math
M/N^{2/3}\longrightarrow c>0
\quad\Longrightarrow\quad
\mathcal F_{N,M}\longrightarrow e^{-c^3/192}.
```

The fidelity tends to one below this scale and to zero above it. In contrast, one fixed waveform collects a mean photon fraction tending to one throughout $`M=o(N)`$. Choosing $`M=\lfloor N^{3/4}\rfloor`$ simultaneously makes the excitation density vanish, the mean collected fraction approach one, and the optimized worst-input state-transfer fidelity approach zero. The failing statement is a uniform channel guarantee, not a claim that every input fails.

This is not an artifact of a badly chosen exponential pulse: the converse allows every waveform. Nor must logical dimension grow: the two populated numbers $`\lfloor M/4\rfloor`$ and $`M`$ already witness the critical limit. Their physical excitation numbers do grow. Vacuum plus one populated number is a different, successful sparse-code comparator; see [TWO_SECTOR_WITNESS.md](TWO_SECTOR_WITNESS.md).

## What the result changes

A measurement showing nearly complete mean-photon collection does not establish a faithful canonical one-oscillator interface. Low excitation density is not a sufficient uniform criterion for that task. The result supplies the optimized boundary and a constructive receiver waveform on the successful side, rather than merely describing one source of distortion.

For an explicit excitation budget, fix a target squared entanglement fidelity $`F_0\in(0,1)`$ independent of $`N`$. Let $`K_N(F_0)`$ be the largest integer $`0\leq M\leq N`$ for which the ideal optimized fidelity satisfies $`\mathcal F_{N,M}\geq F_0`$. The critical law implies

```math
\begin{gathered}
\frac{K_N(F_0)}{N^{2/3}}\longrightarrow c_0,
\\
c_0=(-192\ln F_0)^{1/3}.
\end{gathered}
```

To see this, choose any fixed $`0\lt c_-\lt c_0\lt c_+`$. The critical limits at $`M=\lfloor c_-N^{2/3}\rfloor`$ and $`M=\lfloor c_+N^{2/3}\rfloor`$ lie strictly above and below $`F_0`$, respectively. The optimized fidelity cannot increase when the code is enlarged, so these cutoffs bracket $`K_N(F_0)`$ for sufficiently large $`N`$. Letting the margins approach zero gives the limit. Below a fixed margin, the constructive common pulse reaches the target; above a fixed margin, no allowed waveform does.

This is an asymptotic corollary of the existing theorem. It supplies neither a finite-$`N`$ pass/fail decision at the boundary nor a relative-error estimate for a target tending to one with $`N`$. A finite system must use the bounds in THEOREM.md. The source, calibration, preparation, capture and loss assumptions remain necessary; this is not a hardware specification.

The intended contribution is a domain-of-validity statement for a physical approximation and a recognized memory resource. It is not a universal quantum-capacity limit. The complete emitted field retains the input information, and additional retained modes or nonlinear decoding change the task. Receiver controls, bandwidth, source preparation and loss remain real resources; [PHYSICAL_SCOPE.md](PHYSICAL_SCOPE.md) states those boundaries.

## Relation to known physics

The Dicke cascade, conventional cubic mismatch, number-dependent pulses, occupation
optimization and linear capture are inherited ingredients. They already explain
why multiphoton mismatch accumulates. The result here controls that accumulation
uniformly over an unknown excitation code and excludes every better common waveform
in the critical limit.

The [direct comparison](../literature/COMPARISON.md) and
[Law–Lee reading](../literature/LAW_LEE_FULL_TEXT.md) distinguish that task from
selected-state and mean-occupation optimization. Those results are not contradicted.
The excitation budget is a corollary of the same boundary, not a second result.

## What belongs in the supporting evidence

The uniform field approximation and the unrestricted converse are the proof. The logical-qubit example clarifies scope. The two-mode description explains the leading error. Finite-cavity and independent-decay analyses delimit realizations. Preparation papers establish related control methods, not an implemented unknown-input interface. None of these is a separate headline needed to make the central result seem larger.

**One sentence:** A collective source can look nearly oscillator-like to photon collection while no prechosen linear memory faithfully receives its whole excitation code; the two tasks have different, sharply characterized validity ranges.

The theorem remains conditional; a joint large-code realization is not established. See [Purpose and contact](../README.md#purpose-and-contact) for the repository's learning role and discussion details.
