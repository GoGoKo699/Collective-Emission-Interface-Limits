# State transfer with a bounded receiving coupling

[Scientific route](README.md) · [Source and target](MODEL.md) · [Ideal common-mode limit](COMMON_MODE_BOUNDARY.md) · [Physical scope](PHYSICAL_SCOPE.md)

An ideal receiving mode can have nonzero amplitude at the first possible arrival. A passive oscillator that starts in vacuum cannot absorb that onset without reflection at finite coupling. This page determines how the resulting error competes with the number-dependent pulse mismatch of the Dicke source.

## Sharp coupling and duration requirements

Keep the [fixed Dicke source and canonical output](MODEL.md). The predetermined passive receiver retains one oscillator, starts in vacuum, and couples to a single signal port with intensity rate at most $`B`$ in source time $`\tau=N\gamma t`$. The receiver can adjust the coupling and its phase as functions of time. Write $`\mathcal F_{N,M}(B,T)`$ for the optimal worst-input squared entanglement fidelity when capture ends at time $`T`$. Write $`T=\infty`$ when the capture duration is unrestricted. An equivalent class permits auxiliary vacuum oscillators and passive linear processing, with the cap imposed on the **total** intensity coupling to the signal port.

**Theorem.** Suppose $`M/N^{2/3}\to c\in(0,\infty)`$ and $`B/M\to r\in(0,\infty)`$. Set

```math
A=\frac{c^3}{12},\qquad C=2\log 2-1,\qquad
E(A,\lambda)=\lambda+\frac{(A/4-\lambda)_+^2}{A}.
```

For unrestricted duration or $`T-\log M\to+\infty`$, the fidelity converges to $`\exp[-E(A,C/r)]`$. For a capture window with $`T-\log M\to s\in\mathbb R`$, it converges to

```math
\boxed{\displaystyle
\mathcal F_{N,M}(B,T)\longrightarrow
\exp[-E(A,C/r+e^{-s})].}
```

The explicit oscillator schedule below attains both limits. With unrestricted duration, $`B/M\to\infty`$ recovers the ideal critical fidelity $`e^{-c^3/192}`$, and $`B/M\to0`$ forces the fidelity to zero. A window with $`T-\log M\to-\infty`$ forces the fidelity to zero at any coupling. The physical scales are a receiving rate of order $`N\gamma M`$ and a duration of order $`\log M/(N\gamma)`$. The rate is an intensity decay rate, so its square root is the field coupling amplitude.

## Exact receiver constraint and channel reduction

The signal kernel of one oscillator read out at time $`T`$ has modulus

```math
|h(\tau)|=\sqrt{\kappa(\tau)}\exp\!\left[-\frac{1}{2}\int_\tau^T\kappa(u)\,\mathrm du\right]
\quad(0\le\tau\le T).
```

Here $`\kappa`$ is the intensity rate, and $`h`$ is zero after $`T`$. Define $`q(\tau)=1-\int_\tau^T|h|^2`$. The intensity bound gives

```math
q'=|h|^2\le Bq,\qquad q(T)=1,\qquad q(0)=1-\lVert h\rVert_2^2.
```

Conversely, a kernel satisfying this inequality is realized with $`\kappa=|h|^2/q`$ and the phase of $`h`$. For finite $`T`$, $`q(0)\ge e^{-BT}>0`$. The same formulas hold for an infinite window with $`q(\infty)=1`$; a nonzero admissible kernel again has $`q(0)>0`$ by the differential inequality. Thus the receiver class can be optimized directly over kernels.

For a passive linear network, propagate the final output oscillator backward through the homogeneous one-particle evolution, starting from a unit vector. If the backward vector is $`v(\tau)`$ and the signal coupling row is $`g(\tau)`$, then $`h=g v`$ up to a convention for conjugation. The passive drift has Hermitian part given by minus one half of the sum of the port coupling squares. Consequently $`(\lVert v\rVert^2)'=|h|^2`$ for a single port, or $`(\lVert v\rVert^2)'\ge|h|^2`$ in the presence of additional vacuum ports. Since $`\lVert v(T)\rVert^2=1`$, Cauchy–Schwarz and $`\lVert g\rVert^2\le B`$ imply $`|h|^2\le Bq`$. The one-oscillator realization then attains the same feasible kernels. For an unrestricted-duration receiver the converse applies to every finite readout time and passes to the supremum.

Positivity of the emitted wavefunctions allows us to take $`h\ge0`$. Pointwise absolute value preserves the cap and cannot decrease any number-sector overlap modulus. For nonnegative $`h`$, the [vacuum-complement Kraus argument](MODEL.md#reduction-of-the-channel-objective) applies with diagonal entries $`\langle h^{\otimes m},\Psi_{N,m}\rangle`$. The worst-input fidelity is the minimum of their squares, attained by a number input and valid with an untouched reference. No measurement or postselection is used.

The [uniform matched-pulse bound](MATCHED_PULSES.md#uniform-individually-matched-pulse-approximation) replaces $`\Psi_{N,m}`$ by $`f_{a_m}^{\otimes m}`$, where $`a_m=(m-1)/N`$ for $`m\ge1`$, with vector error tending to zero uniformly for $`m\le M=o(N)`$. Since $`\lVert h\rVert_2\le1`$, the minimum fidelity and its optimum change by at most twice that vector error. The vacuum sector is exact. In this product-pulse problem put

```math
D_m=q(0)+\lVert h-f_{a_m}\rVert_2^2
    =2\bigl(1-\langle h,f_{a_m}\rangle\bigr).
```

When $`D_m=O(M^{-1})`$ uniformly, the fidelity exponent in sector $`m`$ is $`mD_m+o(1)`$ uniformly, from the expansion of $`-2m\log(1-D_m/2)`$.

## Converse

Let $`\delta=M/N`$, so $`M\delta^2\to c^3`$. Along a subsequence whose optimized product-pulse fidelity stays bounded away from zero, take kernels whose worst fidelity approaches the optimum. The sector $`m=M`$ implies $`D_M=O(M^{-1})`$. The matched pulses differ from $`f_0`$ by $`O(\delta)`$ in norm, uniformly in $`m`$. It follows that $`q(0)=O(M^{-1})`$, $`\lVert h-f_0\rVert_2=O(\delta)`$, and $`D_m=O(M^{-1})`$ uniformly. A subsequence with fidelity tending to zero already satisfies the upper bound.

### Initial reflection

Set $`\ell=\log 4`$ and $`I=[0,\ell/B]`$. The cap gives $`h(\tau)\le y e^{B\tau/2}`$, where $`y=\sqrt{Bq(0)}`$. On $`I`$, $`f_{a_m}=1+O(\delta+B^{-1})`$ uniformly. Since $`|I|=O(M^{-1})`$ and $`\lVert h-f_{a_m}\rVert_{L^2(I)}=O(M^{-1/2})`$, replacing $`f_{a_m}`$ by one changes the squared error on $`I`$ by $`o(M^{-1})`$. Hence

```math
q(0)+\lVert h-f_{a_m}\rVert_{L^2(I)}^2\ge
\frac{1}{B}\left[y^2+\int_0^\ell(1-ye^{z/2})_+^2\,\mathrm dz\right]+o(M^{-1}).
```

The bracket equals $`\ell-4y+4y^2`$ for $`0\le y\le1/2`$, $`-2\log y-3+4y`$ for $`1/2\le y\le1`$, and $`y^2`$ for $`y\ge1`$. Its minimum $`C=\ell-1`$ occurs at $`y=1/2`$.

### Smooth pulse mismatch and the missing tail

In the coordinate $`u=-\log(1-a)`$, the pulse tangent at zero is

```math
w(\tau)=e^{-\tau/2}(1/2-e^{-\tau}),\qquad \lVert w\rVert_2^2=1/12.
```

Writing $`x=m/M`$, the Taylor expansion in $`L^2`$ is $`f_{a_m}=f_0+\delta x w+O(\delta^2+N^{-1})`$, uniformly for $`1\le m\le M`$. Use the central interval $`J=(\ell/B,T]`$, with upper endpoint infinity if no readout time is imposed. Project $`h-f_0`$ onto $`w|_J`$ and write $`b_N\delta`$ for its coefficient. The uniform norm bound and $`\lVert w\rVert_{L^2(J)}^2\to1/12`$ imply $`b_N=O(1)`$. Therefore

```math
\lVert h-f_{a_m}\rVert_{L^2(J)}^2
\ge \frac{\delta^2}{12}(x-b_N)^2+o(M^{-1}).
```

For finite $`T`$, the exact missing tail is

```math
\lVert f_{a_m}\rVert_{L^2(T,\infty)}^2
=\frac{e^{-T}}{1-a_m+a_m e^{-T}}.
```

Multiplying by $`M`$ gives $`e^{-s}+o(1)`$ uniformly if $`T-\log M\to s`$. The contribution vanishes on this scale if $`T-\log M\to+\infty`$. The onset, central interval and tail are disjoint. Adding their bounds and passing to a subsequence with $`b_N\to b`$ bounds the worst-sector exponent from below by

```math
\max_{0\le x\le1} x[\lambda+A(x-b)^2],
```

where $`\lambda=C/r+e^{-s}`$ for a finite offset and $`\lambda=C/r`$ otherwise. The excitation grid becomes dense, and the estimates are uniform. This gives a lower bound on the exponent for every sequence of allowed receivers, including ones whose kernels have no smooth limit.

## Attaining schedule

Fix $`b\in[3/4,1]`$ and, for sufficiently large $`M`$, use the target pulse $`f=f_{(bM-1)/N}`$. It is decreasing in the considered regime because its parameter tends to zero. Set $`\tau_0=\ell/B`$ and

```math
d=\left(\int_{\tau_0}^\infty f^2+\frac{f(\tau_0)^2}{B}\right)^{-1/2},\qquad
h_\infty(\tau)=
\begin{cases}
d f(\tau_0)e^{B(\tau-\tau_0)/2},&0\le\tau\le\tau_0,\\
d f(\tau),&\tau>\tau_0.
\end{cases}
```

At the switch, $`q_\infty(\tau_0)=h_\infty(\tau_0)^2/B`$. The rate is exactly $`B`$ before the switch. Afterwards $`h_\infty^2`$ decreases and $`q_\infty`$ increases, so $`\kappa=h_\infty^2/q_\infty\le B`$. To end at time $`T>\tau_0`$, turn off this coupling at $`T`$. The resulting signal kernel is $`h_T=\mathbf 1_{[0,T]}h_\infty/\sqrt{q_\infty(T)}`$. This normalization follows from the one-oscillator evolution and leaves the coupling on $`[0,T]`$ unchanged.

Here $`d=1+O(B^{-1})`$ and, for the windows under consideration, $`q_\infty(T)=1-O(M^{-1})`$. The onset kernel tends to $`e^{(z-\ell)/2}`$ in the variable $`z=B\tau`$, and $`Bq(0)\to1/4`$. Thus the onset cost attains $`C/B+o(M^{-1})`$. On the central interval the receiver differs from $`f`$ by $`O(M^{-1})`$ in norm, so the squared difference from $`f_{a_m}`$ is $`\delta^2(x-b)^2/12+o(M^{-1})`$ uniformly. The tail contributes its exact norm above. The schedule attains the same worst-sector exponent as the converse for the chosen $`b`$.

### Optimizing the balance

For completeness, put $`z=\lambda/A`$. If $`0\le z\le1/4`$, use $`p=1/4+z`$ and $`b=p+1/2`$. Then

```math
p^2-x[z+(x-b)^2]=(1-x)(x-p)^2.
```

The maximum exponent is $`Ap^2`$, attained at $`x=p`$ and $`x=1`$. Any smaller $`b`$ increases the exponent at one, while any larger $`b`$ increases it at $`p`$. If $`z\ge1/4`$, $`b=1`$ gives $`x[z+(x-1)^2]\le z`$ because $`x(1-x)\le1/4`$. The exponent at one is at least $`\lambda`$ for every $`b`$. Both cases give $`E(A,\lambda)`$. The scalar optimization is the same as in the [prescribed uniform-loss theorem](LOSS_COMPETITION.md#2-joint-critical-limit); the derivation above identifies the losses imposed by the receiver itself.

For $`B/M\to0`$ or $`B/M\to\infty`$, compare by monotonicity to caps $`rM`$ at fixed $`r`$ and then take $`r\downarrow0`$ or $`r\to\infty`$. The ideal unrestricted-mode result supplies the upper bound in the latter case for unrestricted duration. To see why short windows force zero at any coupling, Cauchy–Schwarz bounds the top-sector product fidelity by $`(1-\lVert f_{a_M}\rVert_{L^2(T,\infty)}^2)^M`$. Its limit is zero if $`T-\log M\to-\infty`$; the uniform Dicke approximation transfers this conclusion.

## Exact check for one exponential photon

For a known normalized pulse $`f_0(\tau)=e^{-\tau/2}`$, the optimal overlap of a bounded oscillator with unrestricted duration has an exact solution. Its nonnegative stored amplitude obeys $`y'=u f_0-u^2 y/2`$, where $`u=\sqrt\kappa\in[0,\sqrt B]`$. For each current $`y`$, the derivative is maximized by $`u=\min\{\sqrt B,f_0/y\}`$, using $`\sqrt B`$ at $`y=0`$. The maximized derivative is Lipschitz in $`y`$ with constant at most $`B/2`$. Scalar differential comparison shows that this control maximizes $`y`$ at every readout time. It can be computed in advance from the known pulse.

The rate starts at $`B`$ and switches when $`y=f_0/\sqrt B`$, at time

```math
\tau_B=\frac{2}{B-1}\log\frac{2B}{B+1}\quad(B\ne1),\qquad \tau_1=1.
```

After the switch, $`(y^2)'=f_0^2`$, so $`y`$ increases while $`f_0`$ decreases and the cap remains satisfied. The exact single-photon capture probability is

```math
\eta_B=(1+B^{-1})e^{-\tau_B},\qquad
B(1-\eta_B)\longrightarrow 2\log 2-1.
```

For example, $`\eta_1=2/e`$ and $`\eta_2=27/32`$. The same onset coefficient controls the growing code, while the many-sector calculation is needed to combine it with pulse mismatch.

## Relation to earlier receiver controls

[Nurdin, James and Yamamoto](https://arxiv.org/abs/1609.05643) derive ideal single-photon capture with a singular initial coupling. Their Sec. 3.3 truncates the singular control and evaluates capture numerically for an exponential photon. [Sete, Mlinar and Korotkov](https://doi.org/10.1103/PhysRevB.91.144509) analyze initial build-up at maximum receiver coupling followed by reflection cancellation in two-resonator transfer. Their protocol also controls the emitting envelope. [Jähne, Yurke and Gavish](https://doi.org/10.1103/PhysRevA.75.010301) optimize one time-dependent oscillator coupler in harmonic-oscillator transfer. These works supply the relevant impedance-matching and bounded-control precedents. Here the emitted field is fixed, its waveform varies with the unknown excitation number, and optimality concerns one receiver on the entire coherent Dicke code.

The result applies to a fixed Markov signal presented at the receiver port. [Dispersion engineering](https://doi.org/10.1103/m2md-rxkv) can reshape a photon before reception and changes that input. The [multimode theorem](MULTIMODE_RECEIVER.md) instead uses a coherent number-dependent decoder after capture, outside the passive one-oscillator class. No slew-rate limit, distributed dispersive preprocessor, or microscopic implementation of the large coupling is assumed.
