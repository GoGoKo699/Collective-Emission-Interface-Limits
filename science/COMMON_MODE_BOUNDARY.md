# The optimized common-mode boundary

[Scientific route](README.md) · [Exact task](MODEL.md) · [Pulse approximation](MATCHED_PULSES.md) · [Photon collection](PHOTON_COLLECTION.md)

For the fixed collective source and passive one-oscillator target, a constructive
common pulse and an all-waveform converse have the same critical limit. The proof
uses the normalized family $`f_a`$, coordinate $`u=-\ln(1-a)`$, overlap kernel
$`K(u-v)`$ and uniform source-state error established in
[Matched pulses](MATCHED_PULSES.md). The optimized channel objective is squared
worst-input entanglement fidelity, with the input allowed to share an untouched
reference; the proof also uses the corresponding sector and product-pulse overlaps.

## Constructive common waveform

For $`M\geq2`$, choose $`a_*=(3M/4-1)/N`$. If $`M/N^{2/3}\to c>0`$ and $`m/M=x`$, the reference-product fidelity converges uniformly over the code to

```math
K(u_m-u_*)^{2m}\longrightarrow
\exp\!\left[-\frac{c^3}{12}x(x-3/4)^2\right].
```

The maximum of $`x(x-3/4)^2`$ on $`[0,1]`$ is $`1/16`$, attained at $`x=1/4`$ and $`x=1`$. The construction therefore gives limiting worst fidelity $`e^{-c^3/192}`$. Uniform source-state control transfers this lower bound to the true field.

### A finite lower envelope

The preceding construction can be bounded before taking any limit. Define

```math
b_M=1-(M-1)/N,\qquad B_M=\frac{M(M-1)}{12N^2b_M^2},\qquad
\epsilon=\sqrt{2(1-e^{-B_M/2})}.
```

Every sector vector error is at most $`\epsilon`$. The exact inequalities $`\ln K(z)\geq-z^2/24`$ and $`|u_m-u_*|\leq |m-3M/4|/(Nb_M)`$ give, for $`M\geq2`$,

```math
\boxed{\mathcal F_{N,M}\geq
\left[\max\{0,e^{-M^3/(384N^2b_M^2)}-\epsilon\}\right]^2.}
```

This is uniform over the entire code and avoids interchanging a sector minimum with a pointwise limit. Vacuum and the $`M\leq1`$ codes transfer exactly. The [supporting derivation](PROOF_DETAILS.md#4-finite-constructive-bound-with-no-interchange-of-minimum-and-limit) proves the kernel inequality directly.

## Converse for every waveform

Take an integer $`1\leq q\lt M`$ and set

```math
\theta=\arccos K(u_M-u_q),\qquad S=q^{-1/2}+M^{-1/2},\qquad X=\theta^2/S^2.
```

If a receiver has true fidelity at least $`F`$ on both $`q`$ and $`M`$, its reference-product overlap amplitudes are at least $`\sqrt F-\epsilon`$. When $`s=\sqrt F-\epsilon>0`$, its one-photon overlaps with the reference modes are at least $`s^{1/q}`$ and $`s^{1/M}`$. The projective Hilbert-space triangle inequality through the arbitrary receiver and $`\arccos(e^{-t})\leq\sqrt{2t}`$ imply

```math
\theta\leq\arccos(s^{1/q})+\arccos(s^{1/M})
\leq\sqrt{-2\ln s}\,S.
```

Rearranging gives the finite all-waveform upper bound

```math
\boxed{\mathcal F_{N,M}\leq
\min\{1,[\epsilon+e^{-X/2}]^2\}.}
```

For $`\sqrt F\leq\epsilon`$ the bound is automatic. It holds for every waveform, so no optimizer needs to exist and complex phases cannot evade it. The same bound directly applies to the two-sector code. This elementary envelope is used for proof clarity, not in place of the sharper numerical angle brackets below.

At $`q=\lfloor M/4\rfloor`$ and $`M/N^{2/3}\to c>0`$,

```math
b_M\to1,\qquad\epsilon\to0,\qquad
X=\frac{M^3}{192N^2}[1+o(1)]\to c^3/192.
```

The finite constructive and converse bounds therefore squeeze the optimum to

```math
\boxed{M/N^{2/3}\to c>0\quad\Longrightarrow\quad
\mathcal F_{N,M}\to e^{-c^3/192}.}
```

The finite inequality remains valid as fidelity approaches one, so the converse includes the unit-fidelity endpoint. The [endpoint example](PROOF_DETAILS.md#why-the-converse-uses-a-finite-inequality) explains why a relative logarithmic approximation would not suffice.

For $`M=o(N^{2/3})`$, the constructive lower envelope tends to one. For $`M/N^{2/3}\to\infty`$, restrict the full consecutive code to a subcode with cutoff near $`cN^{2/3}`$ for any fixed $`c`$. Monotonicity gives $`\limsup\mathcal F\leq e^{-c^3/192}`$ for every $`c`$, hence zero. This does not extend the critical exponential as an asymptotic equality throughout every supercritical regime. The two-sector code requires its own direct converse rather than this full-code monotonicity argument.

### Finite brackets

Define $`\beta_m=\arccos(e^{-D_{N,m}/2})`$. The chosen pulse gives

```math
F_m(f_a)\geq\cos_+^2\!\left[\arccos K(u_m-u)^m+\beta_m\right].
```

For an all-waveform upper bound on simultaneous fidelity $`F`$, define

```math
r_m(F)=\arccos\left\{\cos_+\left[\arccos\sqrt F+\beta_m\right]^{1/m}\right\}.
```

It is necessary that $`r_q(F)+r_M(F)\geq\arccos K(u_q-u_M)`$. Solving this scalar condition gives the finite converse used in the tests. Here $`\cos_+`$ is clipped to zero when the angle reaches $`\pi/2`$. These bounds need not coincide at finite $`N`$.

## Physical interpretation

The complete code must use one pulse for all its number amplitudes and coherences.
The constraining sectors approach $`M/4`$ and $`M`$, which also gives a
[two-level logical witness](TWO_SECTOR_WITNESS.md). The
[mean-photon estimate](PHOTON_COLLECTION.md) shows why low excitation density can
still suffice for near-complete collection when it no longer suffices for uniform
state transfer. [Loss and capture](PHYSICAL_SCOPE.md) state the resource assumptions
needed to interpret the ideal receiving-mode optimum physically.
