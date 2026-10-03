# From a quantum pulse to the interface boundary

[Overview](README.md) · [Reading guide](docs/README.md) · [Complete proof](research/THEOREM.md)

This is the local bridge from **Kiilerich–Mølmer, Quantum interactions with pulses of
radiation (2020)**, abbreviated **KM**, to the existing interface theorem. Section and
equation labels refer to the [author version](https://arxiv.org/pdf/2003.04573v1).
The pulse and capture framework comes from KM. The Dicke specialization, channel objective
and uniform estimates below are the repository's recorded argument with their existing
attributions; they are not claimed to appear in the tutorial. No new result is introduced.

## 1. The quantum pulse

Start with KM's Introduction and Sections II–II A. For a traveling field, a normalized
pulse selects one oscillator from a continuum:

```math
\begin{aligned}
b_f^\dagger&=\int_0^\infty f(t)b^\dagger(t)\,dt,\\
\int_0^\infty\lvert f(t)\rvert^2dt&=1,\qquad
[b_f,b_f^\dagger]=1.
\end{aligned}
```

The same oscillator can carry $`\lvert0\rangle_f`$, $`\lvert m\rangle_f`$, or a
superposition. Its mode function and quantum state are different objects. In KM's virtual
cavity construction, a chosen coupling releases the cavity's initial state into a chosen
wavepacket. That gives the successful comparator: a linear oscillator can release every
number component into the same pulse.

A collective spin need not do so. Its finite excitation capacity changes its decay
ladder. The question is not whether its light is quantum, but how accurately a fixed
receiving oscillator reproduces the stored state.

## 2. The receiving oscillator

KM Section II C represents a chosen output pulse $`v(t)`$ with a downstream virtual
oscillator $`\hat a_v`$. Write the pulse as $`f(t)`$ here. Equation (17) specifies

```math
g_f(t)=-\frac{f^*(t)}{
\sqrt{\int_0^t\lvert f(s)\rvert^2ds}}.
```

This is a coupling **amplitude**; its squared modulus is a decay rate. The ideal
expression can be singular when capture begins. It defines a mode-selection operation,
not a claim of unlimited physical control. The finite-rate treatment belongs in
[Physical scope A](research/PHYSICAL_SCOPE.md#a-what-the-receiver-restriction-means).

For our source there is no incoming prepared quantum pulse. Following the opening of
KM Section II D, omit the virtual input cavity from Eqs. (18)–(19), keep the emitter and
output oscillator, and specialize $`\hat c`$ to $`S_-`$. The output oscillator's reduced
state is the state of the selected traveling mode. Orthogonal output modes are traced
out, not selected away by a heralding event.

The theorem allows more than one literal receiving cavity. Any predetermined
number-preserving linear receiver with vacuum auxiliary inputs and **one final retained
oscillator** reduces to

```math
c_{\mathrm{out}}=\sqrt q\,b_f+\sqrt{1-q}\,v,
\qquad 0\leq q\leq1,
```

where $`v`$ is a vacuum mode. This uses the passive-network result already attributed in
[the proof](research/THEOREM.md), not a restriction on every system KM discusses.
The ideal optimization allows $`q=1`$ and every normalized $`f`$. Finite control limits
can reduce performance, not invalidate that upper bound. Nonlinear decoding, nonvacuum
ancillas, source-changing feedback or several retained modes change the task.

## 3. The exact source is a finite collective spin

The symmetric $`m`$-excitation state of $`N`$ emitters is $`\lvert D_N^m\rangle`$.
Its lowering matrix element is

```math
S_-\lvert D_N^m\rangle
=\sqrt{m(N-m+1)}\,\lvert D_N^{m-1}\rangle.
```

Use the same dissipator convention as KM Eq. (2):

```math
\begin{aligned}
\dot\rho&=\mathcal D[\sqrt\gamma S_-]\rho,\\
\mathcal D[L]\rho
&=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
\end{aligned}
```

There is no extra Hamiltonian or inaccessible decay in the ideal theorem. With $`k`$
excitations remaining, the population decay rate is $`\gamma k(N-k+1)`$. A harmonic
oscillator would give $`\gamma Nk`$. Low excitation density makes their relative
instantaneous difference small; it does not yet control a full many-photon state.

In $`\tau=N\gamma t`$, the exact cascade rates are
$`\ell_k=k[1-(k-1)/N]`$. Multiplying the ordered waiting-time amplitudes and accounting
once for the ordering factor gives the normalized symmetric labeled-time wavefunction

```math
\begin{aligned}
\Psi_{N,m}(\boldsymbol\tau)
&=C_{N,m}e^{-\sum_i\tau_i/2}\\
&\quad\times\exp\!\left[\frac1N\sum_{i<j}\min(\tau_i,\tau_j)\right],\\
C_{N,m}^2&=\prod_{j=0}^{m-1}(1-j/N).
\end{aligned}
```

The full-domain integral of $`\lvert\Psi_{N,m}\rvert^2`$ is one. A Fock state in one
pulse has wavefunction $`\prod_i f(\tau_i)`$. The pair-time term above makes the exact
emission dependent. The cascade is inherited source theory, with Paulisch credited in
[the background](literature/BACKGROUND.md); no additional external reading is needed to
use this formula here. Its normalization is checked in the existing proof audit.

## 4. Photon collection is not the transfer objective

KM Section II B finds occupation modes from a two-time correlation kernel. Law–Lee's
[completed comparison](literature/LAW_LEE_FULL_TEXT.md) also genuinely optimizes mean
occupation. In a fixed $`m`$-photon sector, define

```math
p_f=\frac{\langle n_f\rangle}{m},
\qquad F_m(f)=\Pr(n_f=m).
```

The number outside the mode is zero on success and between one and $`m`$ otherwise, so

```math
\max\{0,1-m(1-p_f)\}\leq F_m(f)\leq p_f.
```

Exact $`p_f=1`$ implies all photons occupy the mode. Approximate collection needs care
when $`m`$ grows. For the pure emitted state,
$`F_m(f)=\lvert\langle m_f\vert\Psi_{N,m}\rangle\rvert^2`$.
This elementary comparison is not a new general distinction between intensity and state.

Our added demand is **one waveform for an unknown input** in
$`\mathcal C_M=\operatorname{span}\{\lvert D_N^m\rangle:0\leq m\leq M\}`$.
We compare the output with the canonical map
$`\lvert D_N^m\rangle\mapsto\lvert m\rangle_f`$ while leaving any reference untouched.
Entanglement fidelity means the squared overlap with that ideal joint output after
purifying the input. This fixes both number amplitudes and relative coherences; it is not
an optimization over a different target state for each trial.

For nonnegative $`f`$, the Kraus operator associated with vacuum in the discarded modes
is positive diagonal, with entries $`A_m=\langle m_f\vert\Psi_{N,m}\rangle`$. All other
Kraus operators lower the retained number. The standard expression
$`F_e(\rho)=\sum_\nu\lvert\operatorname{Tr}(\rho K_\nu)\rvert^2`$
is therefore at least $`\min_m A_m^2`$, and the corresponding number input attains it.
The exact positive emission amplitudes also mean that replacing a complex receiving
pulse by its modulus cannot reduce any number-overlap modulus. Together these facts give

```math
\mathcal F_{N,M}
=\sup_{\lVert f\rVert_2=1}\min_{0\leq m\leq M}
\lvert\langle m_f\vert\Psi_{N,m}\rangle\rvert^2.
```

This reduction is particular to the optimized channel here. Perfect basis-state
fidelities would not protect superpositions under an arbitrary phase-distorting channel.
The discarded-vacuum Kraus term is a proof device: no photon-loss events are removed from
the actual output.

## 5. Individually matched pulses: the approximation that needs proof

The explicit normalized reference family is

```math
f_a(\tau)=
\frac{\sqrt{1-a}\,e^{-\tau/2}}{1-a+a e^{-\tau}},
\qquad a_m=\frac{m-1}{N}.
```

For $`m\geq1`$, the existing uniform proof establishes

```math
\begin{aligned}
F_m(f_{a_m})&\geq e^{-B_{N,m}},\\
B_{N,m}&=\frac{m(m-1)}{12N^2[1-(m-1)/N]^2}.
\end{aligned}
```

Thus a known $`m=o(N)`$ has an individually excellent pulse. The vacuum transfers
trivially. This is not obtained by assuming independent emissions.

Here is the bridge to the proof's information-theoretic step. Set
$`P=\lvert\Psi_{N,m}\rvert^2`$ and $`Q=\prod_i\lvert f_{a_m}\rvert^2`$.
The counting-process estimate proves $`D(Q\Vert P)\leq B_{N,m}`$.
Since both amplitudes are nonnegative,

```math
\int\sqrt{PQ}
=\mathbb E_Q\exp\!\left[\tfrac12\ln(P/Q)\right]
\geq e^{-D(Q\Vert P)/2}.
```

This is Jensen's inequality. Squaring gives the fidelity bound; squaring the norm of the
difference of the two positive-phase unit vectors gives a vector-error bound.
The nontrivial full-process estimate is in [Theorem, Section 3](research/THEOREM.md#3-a-uniform-individually-matched-pulse-approximation).
It is not taught by KM and is not hidden behind a second prerequisite textbook.

Different number inputs emit into orthogonal photon-number sectors. The norm error of
the entire source map is consequently the largest sector error, not the sum over an
expanding code. This also controls a reference-entangled input. The uniformity is what
permits the comparison for an unknown quantum state.

## 6. One receiving pulse must compromise

For the scalar pulse coordinate $`u=-\ln(1-a)`$—not KM's incoming pulse label—the exact
reference overlap is

```math
\begin{aligned}
K(z)&=\frac{z}{2\sinh(z/2)},\qquad K(0)=1,\\
\ln K(z)&=-z^2/24+O(z^4).
\end{aligned}
```

For $`M\geq2`$, the common choice $`a_*=(3M/4-1)/N`$ balances the most demanding
populated numbers. A product $`m`$-photon overlap is the one-photon overlap raised to
power $`2m`$. With $`m/M=x`$ and $`M/N^{2/3}\to c>0`$, this construction gives

```math
F_m(f_*)\longrightarrow
\exp\!\left[-\frac{c^3}{12}x(x-3/4)^2\right].
```

The limiting statement here uses the previously controlled replacement of the true
field. The largest $`x(x-3/4)^2`$ on $`[0,1]`$ is $`1/16`$, attained at $`x=1/4`$
and $`x=1`$. This explains the constructive value $`e^{-c^3/192}`$.

A construction alone cannot exclude a better waveform. The converse uses the angle
between the individually matched pulses for $`q=\lfloor M/4\rfloor`$ and $`M`$.
Any common receiver must lie close enough to both. A Hilbert-space angle triangle
inequality gives a finite upper bound for every normalized waveform, including complex
ones outside their span. The [endpoint-safe proof](research/PROOF_AUDIT.md) keeps the
additive approximation error explicit before taking the limit. It does not assume
fidelity stays away from one in order to exclude perfect transfer.

Construction and converse yield the sharp boundary

```math
\boxed{
\frac{M}{N^{2/3}}\longrightarrow c>0
\quad\Longrightarrow\quad
\mathcal F_{N,M}\longrightarrow e^{-c^3/192}
}
```

The finite bounds, subcritical success, and supercritical failure for the complete
consecutive code are in the standalone proof. The same two populated sectors witness
the critical limit; vacuum plus one populated number is a successful different code.

## 7. What the result changes—and what it does not

The uniform mean-collection bound tends to one for $`M=o(N)`$, beyond the
$`M=o(N^{2/3})`$ regime of faithful canonical transfer. Hence choosing
$`M=\lfloor N^{3/4}\rfloor`$ makes the excitation density vanish and the mean collected
fraction approach one while optimal worst-input transfer fidelity approaches zero.
This is a domain-of-validity statement for a particular interface approximation.

The full outgoing field retains the quantum information. A second retained pulse or a
nonlinear decoder is an additional resource, not a violation of the one-memory theorem.
Likewise, neither a virtual-cavity equation nor a heralded target-preparation example
establishes the complete growing-code apparatus. The physical-scope and assumption notes
remain necessary for a device claim.

KM supplies the operational language and full selected-pulse state calculation. Existing
Dicke, pulse-shape and occupation results remain credited. The uniform optimization is
the candidate additional contribution, not the discovery that mode shape and photon
number can be correlated. The open [close-source comparison](literature/BACKGROUND_AUDIT.md#the-newly-open-close-source-task)
and separate critical reading are not resolved by this exposition. Manuscript writing
remains on hold.
