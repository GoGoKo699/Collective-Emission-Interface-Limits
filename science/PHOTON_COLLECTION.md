# Mean-photon collection and state transfer

[Scientific route](README.md) · [Common-mode boundary](COMMON_MODE_BOUNDARY.md) · [Interpretation](INTERPRETATION.md)

A mean photon fraction is a bounded-observable question within each number sector.
It does not require every photon, number amplitude and coherence to occupy the same
receiving oscillator. The following estimate uses the exact source of [Model](MODEL.md),
the [uniform pulse approximation](MATCHED_PULSES.md), and the constructive common
pulse $`f_*=f_{a_*}`$ with $`a_*=(3M/4-1)/N`$ for $`M\geq2`$.
The $`M\leq1`$ codes transfer exactly; the collection fraction is defined only
for inputs with nonzero mean photon number.

## Mean collected fraction

On the $`m`$-photon sector, $`E_m=I-\hat n_{f_*}/m`$ is a positive contraction. The triangle inequality for $`\sqrt{E_m}`$ gives

```math
\sqrt{\langle E_m\rangle_{\Psi_m}}
\leq\sqrt{1-K(u_m-u_*)^2}+\varepsilon_m.
```

Put $`b_M=1-(M-1)/N`$. From $`\ln[\sinh(z/2)/(z/2)]\leq z^2/24`$,

```math
\sqrt{1-K(z)^2}\leq |z|/\sqrt{12},\qquad
|u_m-u_*|\leq\frac{|m-3M/4|}{Nb_M}.
```

Using $`|m-3M/4|+\sqrt{m(m-1)}\leq5M/4`$ yields

```math
\frac{\langle\hat n_{f_*}\rangle_m}{m}
\geq1-\min\left\{1,\frac{25M^2}{192N^2b_M^2}\right\}.
```

For a general nonvacuum code input, the ratio $`\langle\hat n_{f_*}\rangle/\langle\hat n_{\rm total}\rangle`$ is a photon-number-weighted average of these sector ratios. Cross-number coherences do not contribute to number-preserving observables. The same bound therefore holds, including with reference entanglement.

It tends to one for every $`M=o(N)`$. Taking $`M=\lfloor N^{3/4}\rfloor`$ simultaneously gives vanishing excitation density, uniformly near-complete mean photon collection, and vanishing optimized whole-code transfer fidelity. The photon-number estimate follows directly from the positive-contraction bound above.

The [observable-control details](PROOF_DETAILS.md#6-photon-count-and-observable-control)
explain why the proof uses a positive contraction rather than applying a
trace-distance estimate to an unbounded number operator. The
[interpretation](INTERPRETATION.md) connects this separation to the excitation
budget for a fixed target state-transfer fidelity.
