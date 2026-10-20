# Individually matched pulses and their geometry

[Scientific route](README.md) · [Model](MODEL.md) · [Common-mode boundary](COMMON_MODE_BOUNDARY.md)

The exact collective emission is correlated. A product-pulse comparison is useful
only after its error is controlled uniformly over the input code. This page proves
that control for the [source and fidelity convention](MODEL.md), then computes the
geometry of the number-dependent reference pulses.

## Uniform individually matched pulse approximation

For $`0\leq a<1`$, define

```math
f_a(\tau)=\frac{\sqrt{1-a}\,e^{-\tau/2}}{1-a+a e^{-\tau}},\qquad a_m=(m-1)/N.
```

Use the vacuum for $`m=0`$ and $`a_1=0`$. Let $`P=|\Psi_{N,m}|^2`$ and $`Q=\prod_i|f_{a_m}|^2`$. For $`m\geq2`$, $`a=a_m`$, $`b=1-a`$,

```math
D(Q\Vert P)=m\left[-\frac{b}{a}\ln b-1\right]-\sum_{j=0}^{m-1}\ln(1-j/N)=D_{N,m}.
```

This exact expression is cancellation-prone; the code evaluates it with high precision. A positive integral representation yields the uniform bound

```math
0\leq D_{N,m}\leq B_{N,m}:=\frac{m(m-1)}{12N^2[1-(m-1)/N]^2}.
```

### Bound via the full counting process

The survival function for the product reference is $`S(t)=e^{-t}/(b+a e^{-t})`$, with $`S'=-S(1-aS)`$. Under that reference the surviving count $`K`$ is binomial with parameters $`m,S`$. Its intensity is $`x=K(1-aS)`$, while the true ladder intensity is $`y=K[1-(K-1)/N]`$.

The pointwise inequality

```math
x\ln(x/y)-x+y\leq\frac{(x-y)^2}{2\min(x,y)}
```

and the exact size-biased binomial identity

```math
\mathbb E\{K[K-1-(m-1)S]^2\}=m(m-1)S^2(1-S)
```

give

```math
D(Q\Vert P)\leq\frac{m(m-1)}{2N^2b}\int_0^1\frac{S(1-S)}{1-aS}\,dS
\leq B_{N,m}.
```

This compares the full dependent emission process with the product reference; it does not treat the true photons as independent.

Since amplitudes are positive, Jensen's inequality for their Hellinger overlap implies

```math
F_m(f_{a_m})\geq e^{-D_{N,m}}\geq e^{-B_{N,m}}.
```

The vector difference from the reference product state is at most

```math
\varepsilon_m\leq\sqrt{2(1-e^{-B_{N,m}/2})}\leq\sqrt{B_{N,m}}.
```

Distinct photon-number sectors are orthogonal. The operator-norm error of the entire source isometry is therefore bounded by $`\max_{m\leq M}\varepsilon_m`$, not a sum over the code. It tends to zero uniformly for $`M=o(N)`$, and the same control holds with a reference system.

Thus each separately known $`m=o(N)`$ can be matched with fidelity tending to one. The common waveform requirement is the additional constraint.

## Exact pulse geometry

Set $`u=-\ln(1-a)`$. Direct integration gives

```math
K(u-v)=\langle f_u,f_v\rangle=\frac{u-v}{2\sinh[(u-v)/2]},\qquad
\ln K(z)=-z^2/24+O(z^4).
```



Here $`f_u`$ denotes $`f_{1-e^{-u}}`$, and the kernel is continued to
$`K(0)=1`$. For $`m\geq1`$, write $`u_m=-\ln(1-a_m)`$. The vacuum is
handled separately. The [convention map](CONVENTIONS.md) distinguishes this scalar
coordinate from pulse labels in the educational anchor.

The quadratic fall of the one-photon overlap becomes an exponent proportional
to photon number for product-mode Fock states. The
[common-mode proof](COMMON_MODE_BOUNDARY.md) balances this mismatch across the
whole code and then uses the uniform vector bound to return to the true field.
The [proof details](PROOF_DETAILS.md#3-uniform-field-approximation) give the
size-biased binomial calculation and its endpoint conventions.
