# From a quantum pulse to the interface boundary

[Overview](README.md) · [Reading guide](docs/README.md) · [Complete proof](research/THEOREM.md)

This is the local bridge from **Kiilerich–Mølmer, Quantum interactions with pulses of
radiation (2020)**, abbreviated **KM**, to the existing interface theorem. Section and
equation labels refer to the [author version](https://arxiv.org/pdf/2003.04573v1).
The pulse and capture framework comes from KM. The Dicke specialization, channel objective
and uniform estimates below are the repository's recorded argument with their existing
attributions; they are not claimed to appear in the tutorial. No new result is introduced.

Read Sections 1–4 for the physical task, then Sections 5–7 for the proof mechanism.
Section 8 connects the result to loss and finite capture. The worked calculations
below are elementary consequences of the stated models, not additional research claims.

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

For example, a cavity with constant population-decay rate $`r>0`$ releases the
normalized envelope $`f(t)=\sqrt r\,e^{-rt/2}`$. Every initial number state uses
this same envelope, so linearity transfers an arbitrary superposition of number states
without choosing a new pulse for each component. KM Eqs. (4)–(7) give this construction.

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

### Worked calculation: one photon, then two

For one excitation, $`\ell_1=1`$ in scaled time. The waiting-time **probability
density** is $`e^{-\tau}`$, so its positive wavefunction is
$`\Psi_{N,1}(\tau)=e^{-\tau/2}`$. The amplitude decays at half the population rate.

For two excitations and $`N\geq2`$, the first and second emissions have rates
$`\ell_2=2(1-1/N)`$ and $`\ell_1=1`$. Their ordered detection density is

```math
\begin{aligned}
p_{\rm ord}(\tau_1,\tau_2)
&=\ell_2e^{-\ell_2\tau_1}e^{-(\tau_2-\tau_1)},\\
&\qquad 0\leq\tau_1<\tau_2.
\end{aligned}
```

This density integrates to one on the ordered region. The symmetric wavefunction
used in this repository integrates over the whole quadrant, with two orderings.
Consequently it obeys $`2|\Psi_{N,2}|^2=p_{\rm ord}`$ on that region. Taking
the positive square root and extending symmetrically gives

```math
\begin{aligned}
\Psi_{N,2}(\tau_1,\tau_2)
&=\sqrt{1-1/N}\,e^{-(\tau_1+\tau_2)/2}\\
&\quad\times e^{\min(\tau_1,\tau_2)/N}.
\end{aligned}
```

The last factor couples the two detection times. For finite $`N`$ this is not
exactly a product of two identical one-photon envelopes. Section 5 will bound the
error of a product approximation instead of assuming independent photons.

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

### Worked calculation: a nearly matched pulse

Take two orthonormal temporal modes $`f,h`$ and a normalized pulse
$`g=\sqrt p\,f+\sqrt{1-p}\,h`$, with $`0\leq p\leq1`$. For this example
only, start with the product-mode Fock state $`|m\rangle_g`$. Expanding its creation
operator gives

```math
\begin{gathered}
|m\rangle_g=\sum_{k=0}^m d_k|k\rangle_f|m-k\rangle_h,\\
d_k=\sqrt{\binom{m}{k}}\,
p^{k/2}(1-p)^{(m-k)/2}.
\end{gathered}
```

After discarding $`h`$, the collected number is binomial: the mean fraction is
$`p`$, while fidelity with $`|m\rangle_f`$ is $`p^m`$. With $`p=0.99`$ and
$`m=100`$, the receiver collects 99% of the mean photon number but its squared
fidelity is $`0.99^{100}\simeq0.366`$. This is an illustrative two-mode calculation,
not a numerical result for the collective source. The uniform estimate in Section 5
is what makes this mechanism applicable to the correlated source field.

### Preserving an unknown state

Our added demand is **one waveform for an unknown input** in
$`\mathcal C_M=\operatorname{span}\{\lvert D_N^m\rangle:0\leq m\leq M\}`$.
We compare the output with the canonical map
$`\lvert D_N^m\rangle\mapsto\lvert m\rangle_f`$ while leaving any reference untouched.
Entanglement fidelity means the squared overlap with that ideal joint output after
purifying the input. This fixes both number amplitudes and relative coherences; it is not
an optimization over a different target state for each trial.

The receiver may depend on known $`N`$ and the declared cutoff $`M`$. It cannot
depend on the actual excitation component $`m`$, the unknown coefficients, or an
untouched reference. Choosing a pulse separately for every known number therefore
does not solve this transfer task.

To see why coherences matter, consider a different channel that sends
$`|0\rangle\mapsto|0\rangle`$ and $`|1\rangle\mapsto-|1\rangle`$.
Both number-state fidelities are one, but it sends
$`(|0\rangle+|1\rangle)/\sqrt2`$ to an orthogonal state. Our reduction to
number-sector overlaps must therefore be proved using the actual channel structure.

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

In this argument, a Kraus operator records one possible discarded-field outcome;
the physical channel sums over all of them. A reference system is a spectator
initially entangled with the input. Testing that joint state checks that transfer
preserves quantum correlations, as well as states prepared without a spectator.

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
These are classical probability densities for all detection times. Their relative
entropy is $`D(Q\Vert P)=\int Q\ln(Q/P)`$, with natural logarithms.
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

The scaling can be understood before its coefficient. Across the declared code,
the individually matched pulse changes by order $`M/N`$. A normalized one-photon
overlap then loses order $`(M/N)^2`$. The worked Fock-state calculation above
raises that overlap to a power of order $`M`$, giving the accumulated scale
$`M^3/N^2`$. The following exact overlap calculation and converse turn this
scaling argument into the theorem.

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
number can be correlated. The later [close-source comparison](literature/TZIPERMAN_FULL_TEXT.md)
is complete at its documented versions; separate external critical reading remains
open. Manuscript writing remains on hold.

## 8. Loss and finite capture after the ideal theorem

These are supporting consequences of the same interface task. Read them after the
ideal boundary; neither changes the one-oscillator receiver or canonical target.

**Transmission loss.** For mode-independent pure loss with intensity transmission
$`\eta`$, a number-$`m`$ component keeps all its photons with probability
$`\eta^m`$. Thus the positive-pulse objective becomes
$`\min_{m\leq M}\eta^m|A_m(f)|^2`$. In particular, the highest number imposes
the ceiling $`\eta^M`$, even with perfect mode matching. This is why fixed
nonzero loss can hide the mode-mismatch effect as the code grows. The
[loss-competition proof](research/LOSS_COMPETITION.md) solves the reoptimization
when both effects survive at critical scaling: its Sections 1–2 give the result
and proof, and Section 3 gives finite bounds. Independent atomic loss is a different model.

**Finite capture.** The ideal coupling in Section 2 above may diverge at its onset.
For the normalized pulse $`f(\tau)=e^{-\tau/2}`$, its rate in scaled units is

```math
\kappa(\tau)=\frac{e^{-\tau}}{1-e^{-\tau}}
=\frac{1}{e^\tau-1}.
```

The divergence at $`\tau=0`$ is already visible in this simple example.
Adding $`\varepsilon>0`$ to the denominator's integrated intensity and stopping
at a finite time make capture finite, at the cost of attenuation and a changed mode. With
$`P_T=\int_0^T|f(\tau)|^2d\tau`$, the recorded construction has attenuation
$`q_T=P_T/(\varepsilon+P_T)`$. A growing code is sensitive to $`q_T^M`$,
so a small single-photon error must shrink as the code grows. The proved
[whole-code bound](research/PHYSICAL_SCOPE.md#a-finite-receiving-window-on-the-same-code)
controls both this attenuation and the discarded tail. It permits increasing
duration and coupling resources; it does not establish a fixed bandwidth or a
joint device realization.
