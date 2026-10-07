# One logical qubit can witness the common-mode limit

**3 October 2026. Scope consequence of the recorded theorem, with new finite checks.** The source, passive receiver, and canonical excitation-number map are unchanged. This note does not claim another general information theorem or an optimized bosonic encoding.

## 1. The question

The original statement requires a receiver to handle every Dicke excitation number from zero to $M$. One might ask whether the loss of fidelity is only an artifact of demanding simultaneous performance on an increasingly large logical space.

It is not. For $M\geq4$, define $q=\lfloor M/4\rfloor$ and the two-dimensional input code

$$|0_L\rangle=|D_N^q\rangle,\qquad |1_L\rangle=|D_N^M\rangle.$$

The target is the same unknown superposition of $|q\rangle$ and $|M\rangle$ in one preselected oscillator mode. The receiver is not allowed to choose a waveform after learning which basis state was prepared.

Its optimized worst-input entanglement fidelity is

$$\mathcal G_{N,M}=\sup_f\min\{F_q(f),F_M(f)\},\qquad
F_m(f)=|\langle m_f|\Psi_{N,m}\rangle|^2.$$

The same positive vacuum-complement Kraus argument used for the whole code proves this equality, including a reference entangled with the logical qubit.

## 2. The critical law is already saturated by these two inputs

For $M/N^{2/3}\to c>0$,

$$\boxed{\mathcal G_{N,M}\longrightarrow e^{-c^3/192}.}$$

The proof needs no new asymptotic approximation. The whole-code receiving pulse works on this subcode, so $\mathcal G_{N,M}\geq\mathcal F_{N,M}$. Conversely, the whole-code all-waveform proof already uses only these two numbers. Its upper bound therefore also applies to $\mathcal G_{N,M}$. The same critical limit follows by squeezing the bounds.

This is a corollary of the original proof, not an independent source of novelty. Its role is to clarify the physical demand: the receiving limitation can be exposed with a single logical qubit, although the physical excitation numbers are large and grow with $N$.

### Why the quarter-number state appears

For a generic fixed lower fraction $r\in(0,1)$, the leading product-state minimax problem is

$$\min_b\max\{r(b-r)^2,(1-b)^2\}.$$

Balancing its two terms gives $b=1-\sqrt r+r$ and the optimal value $r(1-\sqrt r)^2$. This is largest at $r=1/4$, where $b=3/4$ and the value is $1/16$. Dividing by the pulse-geometric coefficient 12 gives $1/192$.

This scalar calculation explains the witness selected in the existing converse. It is not a claim that no other encoding, source control, or receiver can do better.

## 3. A finite test within an explicit pulse family

At $N=1000$ and $M=300$, the two input basis states have 75 and 300 excitations. Solving only for a balance point within the known family $f_a$ gives

$$a=0.22964923849\ldots.$$

The full emitted-amplitude calculation yields:

| Input | Squared full-state overlap with its target Fock state in this same pulse |
|---|---:|
| 75 excitations | 0.8125124786 |
| 300 excitations | 0.8125124786 |

This is a constructive numerical witness for the entire two-dimensional code. It is not merely a comparison of two individually chosen pulses. Their equality also makes the maximally reference-entangled input's entanglement fidelity equal to the displayed value, since that fidelity is $(A_q+A_M)^2/4$ with positive amplitudes.

The prior analytic all-waveform angle bound gives

$$\mathcal G_{1000,300}\leq0.84394780\ldots.$$

Thus the finite two-sector optimum is bracketed by the explicit approximately 81.25% achievable value and the approximately 84.39% universal ceiling. The lower value is numerically evaluated, with a separate analytic tail allowance and tolerance refinement. These decimals are not interval-certified. The root search locates a balanced trial in $f_a$; it does not prove global finite-$N$ optimality even within that family.

For comparison, the original asymptotic trial $a=0.224$ gives fidelities 0.8257267087 and 0.7865187451 for the two numbers. The slightly different trial here improves their minimum. Neither set of two values certifies the minimum over every intermediate excitation number in the original full code.

## 4. A one-qubit low-density separation

Along $M=\lfloor N^{3/4}\rfloor$, both basis excitation fractions vanish. Each known number still has an individually matched pulse with fidelity tending to one, and the same common pulse captures a mean photon fraction tending to one for every state in this subcode.

Nevertheless, the two-sector angle argument forces $\mathcal G_{N,M}\to0$. If a positive limiting fidelity existed, the source approximation errors vanish, while the angle mismatch would require a positive constant to be at least of order $M^{3/2}/N=N^{1/8}$, a contradiction.

This separates increasing logical dimension from increasing excitation energy. The example has fixed logical dimension two; it is not a fixed-energy or fixed-duration limit.

## 5. A control that must not be omitted

The sparse code $\mathrm{span}\,\{|D_N^0\rangle,|D_N^M\rangle\}$ is different. Choose the receiving pulse for the known nonvacuum number. Vacuum is the same in every mode. The uniform matched-state bound then gives asymptotically unit fidelity whenever $M=o(N)$.

Therefore “all sparse codes obey the cutoff” would be false. The positive lower-number component in the witness forces incompatible pulse requirements. This basic distinction between vacuum and two different populated number components is also discussed for specific nonlinear-cavity states in Khanahmadi et al. (2023). The corollary here quantifies it for the optimized Dicke interface; it does not claim the qualitative observation was unknown.

## 6. What an experimental test would and would not need

To witness the minimax upper bound within the trusted source model, the two number-state inputs suffice; a high-dimensional unknown superposition need not be prepared merely to expose incompatible receiving modes. Testing a few particular receiving pulses experimentally does not, on its own, prove the all-waveform upper bound. That bound rests on the model and the controlled mode-state comparison.

Preparing high-number Dicke states, knowing $N$, and measuring full-Fock overlap can still be demanding. Ordinary photon loss can dominate this canonical target. The corollary is not an inexpensive experiment proposal or a replacement for the source-assumption audit.

## 7. Checks

`tests/07_two_sector_scope/checks.py` checks the scalar minimax balance, the complete emission-amplitude cascade for two finite code choices, horizon/tolerance refinement, the exact two-input analytic bound, convergence of its critical brackets, a vacuum-plus-number control, and the reference-channel Kraus logic. The new suite imports none of the six archived scientific scripts.

The source theorem and the nonlinear-cavity qualitative predecessor are credited in [the prior-art register](../literature/PRIOR_ART.md). No independent mathematical reader report has been received.
