# One source, two notions of an accurate interface

**3 October 2026. Explanatory research note; not a manuscript or a new result.** The model, code, receiver and fidelity convention are those of [THEOREM.md](THEOREM.md), including the recorded [proof correction](PROOF_AUDIT.md).

## The question

When is a weakly excited collective spin an adequate oscillator for transferring an unknown quantum state?

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

The intended contribution is a domain-of-validity statement for a physical approximation and a recognized memory resource. It is not a universal quantum-capacity limit. The complete emitted field retains the input information, and additional retained modes or nonlinear decoding change the task. Receiver controls, bandwidth, source preparation and loss remain real resources; [PHYSICAL_SCOPE.md](PHYSICAL_SCOPE.md) states those boundaries.

## What belongs in the supporting evidence

The uniform field approximation and the unrestricted converse are the proof. The logical-qubit example clarifies scope. The two-mode description explains the leading error. Finite-cavity and independent-decay analyses delimit realizations. Preparation papers establish related control methods, not an implemented unknown-input interface. None of these is a separate headline needed to make the central result seem larger.

The inherited ingredients include the Dicke cascade, conventional-pulse cubic mismatch, number-dependent temporal modes, mode-occupation optimization and linear capture. Law and Lee genuinely optimize mean occupation; their task is not dismissed as unoptimized. The [direct comparison](../literature/COMPARISON.md) and [full-text reading](../literature/LAW_LEE_FULL_TEXT.md) identify the specific remaining contribution without claiming exhaustive priority.

**One sentence:** A collective source can look nearly oscillator-like to photon collection while no prechosen linear memory faithfully receives its whole excitation code; the two tasks have different, sharply characterized validity ranges.

The theorem remains conditional. The separate critical-reader report and a joint large-code realization remain absent. Manuscript writing and outreach remain on hold.
