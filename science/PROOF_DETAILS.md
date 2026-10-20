# Normalization, uniformity and endpoint details

[Scientific route](README.md) · [Model](MODEL.md) · [Matched pulses](MATCHED_PULSES.md) · [Common-mode boundary](COMMON_MODE_BOUNDARY.md)

These supporting derivations make explicit the ordered-time convention, channel
phase control, uniform approximation and endpoint estimates used by the central
proof. The [claim map](CLAIM_EVIDENCE_MAP.md) locates each result and its finite
checks. The source, receiver and fidelity are those of [Model](MODEL.md).

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

Together with $`\min(x,y)\geq Kb`$, where $`b=1-(m-1)/N>0`$, and $`dt=-dS/[S(1-aS)]`$, this gives the [matched-pulse bound](MATCHED_PULSES.md#uniform-individually-matched-pulse-approximation). The $`K=0`$ integrand is defined to be zero, and the endpoint integral is finite. Positivity of both amplitudes makes their inner product equal to the classical Hellinger affinity, so the entropy bound controls vectors rather than only probability distributions.

Both source maps preserve total photon number. Their difference on distinct input number sectors therefore has orthogonal ranges. Consequently its operator norm is the largest sector vector error, not the sum; tensoring with an arbitrary reference preserves that operator norm. This establishes the uniform code statement, including an external reference.

For the remaining argument it is enough to use

```math
b_M=1-(M-1)/N,\quad B_M=\frac{M(M-1)}{12N^2b_M^2},\quad
\epsilon=\sqrt{2(1-e^{-B_M/2})}.
```

The bound $`B_{N,m}\leq B_M`$ follows by increasing the numerator and decreasing the denominator, for $`m\leq M`$. Thus every sector vector error is at most $`\epsilon`$.

## 4. Finite constructive bound, with no interchange of minimum and limit

Let $`M\geq2`$ and choose the common pulse with $`a_*=(3M/4-1)/N`$. For $`m\geq1`$,

```math
|u_m-u_*|\leq\frac{|m-3M/4|}{Nb_M},\qquad
\ln K(z)\geq-z^2/24.
```

The latter inequality is elementary. For $`x\geq0`$, $`(1+x^2/3)\sinh x-x\cosh x`$ starts at zero and has derivative $`(x/3)(x\cosh x-\sinh x)\geq0`$. Hence $`\coth x-1/x\leq x/3`$; integrating yields $`\ln(\sinh x/x)\leq x^2/6`$. Set $`x=|z|/2`$.

Since $`\max_{0\leq x\leq1}x(x-3/4)^2=1/16`$, the reference-product
overlap amplitude is at least $`\exp[-M^3/(384N^2b_M^2)]`$ simultaneously
for every sector. Subtracting the uniform vector error gives the
[finite lower envelope](COMMON_MODE_BOUNDARY.md#a-finite-lower-envelope).
Write this lower envelope as $`L_{N,M}`$. Its minimum is controlled at finite
$`N`$ before taking any limit. Vacuum and the $`M=0,1`$ codes transfer exactly
and do not require the trial formula.

## 5. Finite all-waveform converse

The [finite converse](COMMON_MODE_BOUNDARY.md#converse-for-every-waveform)
uses the projective-angle triangle inequality through an arbitrary receiver,
followed by $`\arccos(e^{-t})\leq\sqrt{2t}`$. The latter follows by integrating
$`\tan x\geq x`$ on $`0\leq x<\pi/2`$ to obtain
$`-\ln\cos x\geq x^2/2`$. Write the resulting upper envelope as
$`U_{N,M}(q)`$.

The argument holds for each waveform, including complex pulses and directions
outside the span of the two reference modes, so it also bounds the supremum.
No maximizing waveform needs to exist. It directly bounds the two-sector code;
no monotonicity inference from the full code to that easier task is used.

### Why the converse uses a finite inequality

Vanishing additive error does not imply a vanishing *relative* logarithmic error when $`F`$ tends to one. For example, $`F_N=1-N^{-2}`$ and $`\epsilon_N=N^{-1/3}`$ give

```math
\frac{-2\ln(\sqrt{F_N}-\epsilon_N)}{-\ln F_N}\longrightarrow\infty.
```

This example shows why an additive approximation error cannot be replaced by a relative logarithmic error near unit fidelity. The finite inequality avoids that substitution and applies uniformly at the endpoint.

### Joint and supercritical limits

At $`q=\lfloor M/4\rfloor`$ and $`M/N^{2/3}\to c>0`$, $`b_M\to1`$, $`\epsilon\to0`$ and

```math
X=\frac{M^3}{192N^2}[1+o(1)]\longrightarrow c^3/192.
```

The lower and upper bounds therefore converge to $`e^{-c^3/192}`$. This includes possible sequences of achieved fidelities approaching zero or one; the proof has no separate unhandled endpoint. The subcritical conclusion follows from $`L_{N,M}\to1`$.

For the full code in an arbitrary supercritical sequence, use a fixed-critical consecutive subcode and then let its fixed critical coefficient grow. Do not extrapolate the critical formula to all supercritical sequences. For the particular two-sector witness with $`M=N^{3/4}`$, the finite upper bound instead gives $`X\to\infty`$ and $`\epsilon\to0`$ directly, hence vanishing two-sector fidelity.

## 6. Photon count and observable control

On each fixed-number sector, $`I-\hat n_f/m`$ is a positive contraction. Applying its square root to the vector approximation gives the triangle estimate used in the mean-collection proof. A general number-coherent input contributes only its number-diagonal weights to these observables, so the ratio is a photon-number-weighted average. The proof does not infer an unbounded photon-number moment from trace distance. The vacuum ratio is undefined, while vacuum transfer itself is exact.

## Numerical checks

[Suite 08](../tests/08_uniform_proof_audit/checks.py) checks ordered-time and binomial
identities, channel/reference controls, complex-mode geometry, the near-unit
logarithmic example, finite envelopes against small complete cascades, scalar
limits and the orthogonal-sector norm. Its large integer examples evaluate formulas;
they do not simulate ensembles of those sizes. These finite checks support the
analytical arguments under the [declared model](MODEL.md).
