# Uniform-proof audit and endpoint repair

**3 October 2026. Author-side audit, not an independent reader report.** The source, receiver, canonical target and theorem statement are unchanged. This pass checks the six mathematical questions in [CRITICAL_READING.md](https://github.com/GoGoKo699/Collective-Emission-Interface-Limits/blob/1e64a433150e63ea2dcfb8a49b94d4bf4efb2e3b/research/CRITICAL_READING.md) against the actual proof. The reference version is commit `1e64a433150e63ea2dcfb8a49b94d4bf4efb2e3b`, whose theorem blob is `e25ccc8f692f5ca739d995dca66cd414c95b5c9a`.

## Outcome

**The main theorem is preserved; a compressed converse argument is repaired at an endpoint.** The earlier Section 5 replaced an additive source-state error by a multiplicative $`1+o(1)`$ correction involving $`\sqrt{-\ln F}`$. That replacement is valid when the limiting fidelity is strictly between zero and one. It was not justified by the stated condition 'positive limiting fidelity' alone, which also permits a limit of one.

The replacement below is a finite inequality, valid before taking any limit. It handles the zero- and unit-fidelity endpoints and a supremum that need not be attained. The constants and domains of the main result, the mean-collection result, and the two-sector witness do not change. The older finite angle bounds and all seven saved numerical suites remain valid and unchanged. The new elementary envelope is for a transparent proof, not a claim of better finite numerical constants.

The correction is not another physical discovery or a reason to enlarge the project. It closes a specific proof obligation. The final attribution paragraph of THEOREM.md is also updated: Law–Lee full-text access was already resolved in PR #4, although that paragraph still described the older access gap.

## 1. Ordered-time normalization

For ordered times $`0\lt t_1<\cdots\lt t_m`$, put $`s_i=t_i-t_{i-1}`$ and $`k=m-i+1`$. Directly from the stated symmetric amplitude,

```math
m!\,\Psi_{N,m}^2=\prod_{i=1}^m\ell_{m-i+1}e^{-\ell_{m-i+1}s_i},\qquad
\ell_k=k[1-(k-1)/N].
```

Indeed $`\prod_k\ell_k=m!C_{N,m}^2`$, and collecting the coefficients of each spacing gives its positive rate. This proves normalization on the ordered simplex; the labeled cube has $`m!`$ congruent regions. The reference Fock wavefunction $`\prod_i f(t_i)`$ has the same labeled convention. Sorting loses only a uniform labeling shared by both probability laws, so the relative-entropy comparison is unchanged. There is no missing factorial and no independent-photon approximation to the true field.

## 2. Channel fidelity, complex pulses and a reference

For a nonnegative pulse, the empty-complement Kraus operator is diagonal and nonnegative. Its contribution gives $`F_e(\rho)\geq\min_m A_m^2`$ for every density operator. Other Kraus contributions are nonnegative and are not discarded. A number-state input at the minimizing diagonal entry has zero target overlap for every number-lowering Kraus outcome and attains the bound. Purifying $`\rho`$ includes any untouched reference automatically.

It would be false to assert this minimum formula for every complex-pulse channel without addressing phases: a diagonal unitary with entries $`1,-1`$ has unit Fock fidelities but zero fidelity on the equal superposition. The proof instead uses positivity to bound the arbitrary complex pulse's worst fidelity by its Fock overlaps, bounds those by the pointwise-modulus pulse's overlaps, and notes that the positive pulse attains that minimum. This proves equality after receiver optimization, which is exactly the claimed objective. No input-dependent phase correction is introduced.

## 3. Uniform field approximation

The relative-entropy direction is $`D(Q\Vert P)`$, with $`Q`$ the product reference and $`P`$ the exact cascade. Under $`Q`$, the survivor count is binomial. Weighting its law by $`K`$ replaces $`K-1`$ by an independent $`\mathrm{Bin}(m-1,S)`$ variable and gives

```math
\mathbb E\{K[K-1-(m-1)S]^2\}=m(m-1)S^2(1-S).
```

Together with $`\min(x,y)\geq Kb`$, where $`b=1-(m-1)/N>0`$, and $`dt=-dS/[S(1-aS)]`$, this gives the bound in THEOREM.md Section 3. The $`K=0`$ integrand is defined to be zero, and the endpoint integral is finite. Positivity of both amplitudes makes their inner product equal to the classical Hellinger affinity, so the entropy bound controls vectors rather than only probability distributions.

Both source maps preserve total photon number. Their difference on distinct input number sectors therefore has orthogonal ranges. Consequently its operator norm is the largest sector vector error, not the sum; tensoring with an arbitrary reference preserves that operator norm. This verifies the uniform code statement.

For the remaining argument it is enough to use

```math
b_M=1-(M-1)/N,\quad B_M=\frac{M(M-1)}{12N^2b_M^2},\quad
\epsilon=\sqrt{2(1-e^{-B_M/2})}.
```

The bound $`B_{N,m}\leq B_M`$ follows by increasing the numerator and decreasing the denominator, for $`m\leq M`$. Thus every sector vector error is at most $`\epsilon`$.

## 4. Finite constructive bound, with no interchange of minimum and limit

Let $`M\geq2`$ and choose the existing pulse with $`a_*=(3M/4-1)/N`$. For $`m\geq1`$,

```math
|u_m-u_*|\leq\frac{|m-3M/4|}{Nb_M},\qquad
\ln K(z)\geq-z^2/24.
```

The latter inequality is elementary. For $`x\geq0`$, $`(1+x^2/3)\sinh x-x\cosh x`$ starts at zero and has derivative $`(x/3)(x\cosh x-\sinh x)\geq0`$. Hence $`\coth x-1/x\leq x/3`$; integrating yields $`\ln(\sinh x/x)\leq x^2/6`$. Set $`x=|z|/2`$.

Since $`\max_{0\leq x\leq1}x(x-3/4)^2=1/16`$, the reference-product overlap amplitude is bounded below, simultaneously for every sector, by $`\exp[-M^3/(384N^2b_M^2)]`$. Subtracting the vector error gives

```math
\boxed{\mathcal F_{N,M}\geq
L_{N,M}:=\left[\max\{0,e^{-M^3/(384N^2b_M^2)}-\epsilon\}\right]^2.}
```

This is a finite all-code bound, not a pointwise expansion followed by an unjustified minimum. Vacuum transfers exactly. The codes $`M=0,1`$ are separately exact and do not require the trial formula.

## 5. Finite all-waveform converse

Choose any integer $`1\leq q\lt M`$. Put

```math
\theta=\arccos K(u_M-u_q),\qquad
S=q^{-1/2}+M^{-1/2},\qquad X=\theta^2/S^2.
```

For a receiving pulse whose true overlaps on both numbers have squared modulus at least $`F`$, the reference-product amplitudes are at least $`\sqrt F-\epsilon`$. If this number is nonpositive, the bound below is automatic. Otherwise write $`s=\sqrt F-\epsilon\in(0,1]`$. The two single-photon overlaps with that same receiving pulse are at least $`s^{1/q}`$ and $`s^{1/M}`$.

The projective-angle triangle inequality and $`\arccos(e^{-t})\leq\sqrt{2t}`$ give

```math
\theta\leq\arccos(s^{1/q})+\arccos(s^{1/M})
\leq\sqrt{-2\ln s}\,S.
```

For completeness, the last elementary inequality follows by integrating $`\tan x\geq x`$: $`-\ln\cos x\geq x^2/2`$. Rearranging before taking any limit yields

```math
\boxed{\mathcal F_{N,M}\leq
U_{N,M}(q):=\min\{1,[\epsilon+e^{-X/2}]^2\}.}
```

The bound holds for each waveform, including complex pulses and directions outside the span of the two reference modes, so it also holds for the supremum. No maximizing waveform needs to exist. It also bounds the two-sector code directly; no monotonicity inference from the full code to that easier task is used.

### The endpoint that needed repair

Vanishing additive error does not imply a vanishing *relative* logarithmic error when $`F`$ tends to one. For example, $`F_N=1-N^{-2}`$ and $`\epsilon_N=N^{-1/3}`$ give

```math
\frac{-2\ln(\sqrt{F_N}-\epsilon_N)}{-\ln F_N}\longrightarrow\infty.
```

This is a counterexample to the earlier asymptotic substitution, not a proposed attainable source fidelity. The finite inequality avoids that substitution entirely.

### Joint and supercritical limits

At $`q=\lfloor M/4\rfloor`$ and $`M/N^{2/3}\to c>0`$, $`b_M\to1`$, $`\epsilon\to0`$ and

```math
X=\frac{M^3}{192N^2}[1+o(1)]\longrightarrow c^3/192.
```

The lower and upper bounds therefore converge to $`e^{-c^3/192}`$. This includes possible sequences of achieved fidelities approaching zero or one; the proof has no separate unhandled endpoint. The subcritical conclusion follows from $`L_{N,M}\to1`$.

For the full code in an arbitrary supercritical sequence, use a fixed-critical consecutive subcode and then let its fixed critical coefficient grow. Do not extrapolate the critical formula to all supercritical sequences. For the particular two-sector witness with $`M=N^{3/4}`$, the finite upper bound instead gives $`X\to\infty`$ and $`\epsilon\to0`$ directly, hence vanishing two-sector fidelity.

## 6. Photon count and the limits of the audit

On each fixed-number sector, $`I-\hat n_f/m`$ is a positive contraction. Applying its square root to the vector approximation gives the triangle estimate used in the mean-collection proof. A general number-coherent input contributes only its number-diagonal weights to these observables, so the ratio is a photon-number-weighted average. The proof does not infer an unbounded photon-number moment from trace distance. The vacuum ratio is undefined, while vacuum transfer itself is exact.

These checks answer the listed normalization, channel, uniformity, converse, count and two-sector questions on the stated premises. They do not certify every possible imperfection, the optional microscopic realization, the two-mode appendix under new scaling regimes, or exhaustive priority. The source/receiver assumptions and the completed [Law–Lee comparison](../literature/LAW_LEE_FULL_TEXT.md) remain as recorded. That article already optimizes mean-occupation modes; the distinction is not optimization versus no optimization.

The remaining preparation evidence is not replaced by proof checks. Manuscript drafting stays on hold.

## Reproduction and change record

`tests/08_uniform_proof_audit/checks.py` imports no earlier scientific module. Its five groups check exact ordered-time and binomial identities, channel/reference controls, complex-mode geometry, the failed near-unit logarithmic substitution, the new finite envelopes against small complete cascades, their scalar limits, and the orthogonal-sector norm. Large integer examples evaluate formulas only; they do not simulate huge ensembles.

The original seven scripts and result files are unchanged. Their fresh baseline run matched every reference byte-for-byte. The current suite is an additional diagnostic, not a regeneration of those expected values. The canonical proof is edited only to expose the constructive finite envelope, replace the endpoint-sensitive converse passage, and correct its stale full-text-access status. The asymptotic law and previously reported finite angle-bound values are unchanged.
