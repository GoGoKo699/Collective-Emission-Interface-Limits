# How many temporal modes are needed for collective state transfer?

The one-mode boundary comes from the dependence of the emitted pulse on the initial excitation number. A receiver can correct more of this dependence by capturing several predetermined temporal modes and coherently rotating them according to the total photon number. Two captured modes raise the critical excitation scale from $`N^{2/3}`$ to $`N^{4/5}`$. The general fixed-mode result gives the sharp fidelity at the crossover and an explicit choice of receiving modes.

[Source and target](MODEL.md) · [One-mode boundary](COMMON_MODE_BOUNDARY.md) · [Pulse approximation](MATCHED_PULSES.md)

## Receiver and figure of merit

Use the same ideal Dicke decay, one vacuum Markov field and input code $`\mathcal C_M=\mathrm{span}\{|D_N^m\rangle:0\le m\le M\}`$ as in the [source model](MODEL.md). The canonical output is one oscillator in $`|m\rangle`$, with every input superposition and its reference correlations included in squared entanglement fidelity.

The capture stage takes a known $`K`$-dimensional subspace $`S`$ of the one-photon temporal Hilbert space. It retains the corresponding oscillators and traces its orthogonal complement. The choice of $`S`$ may depend on $`N,M,K`$ and is made before the input arrives. A fixed number-preserving local unitary then acts on the $`K`$ oscillators. It can apply a different operation within each total-number sector while preserving coherence between sectors. The receiver keeps the first oscillator and traces the other $`K-1`$. The operation is deterministic, with no number measurement, extra photons or feedback to the source. Denote the optimized worst-input fidelity by $`\mathcal F^{(K)}_{N,M}`$.

The sector-dependent decoding is a resource beyond passive linear optics. With only passive linear mixing after capture, the first output annihilation operator is still one fixed linear combination of the captured mode operators. The complete receiver then reduces to the original one-mode model. In particular, simply adding a second storage oscillator does not give the two-mode result for transfer into one final oscillator.

## Sharp mode-count law

For every fixed integer $`K\ge1`$, define

```math
\alpha_K=\frac{2K}{2K+1},\qquad
D_K=2^{4K}(2K+1)\binom{2K}{K}^{2}.
```

Then the optimized fidelity has the following limits as $`N\to\infty`$:

```math
\boxed{\begin{aligned}
M=o(N^{\alpha_K})&\quad\Longrightarrow\quad \mathcal F^{(K)}_{N,M}\longrightarrow1,\\
M/N^{\alpha_K}\longrightarrow c\in(0,\infty)&\quad\Longrightarrow\quad
\mathcal F^{(K)}_{N,M}\longrightarrow\exp[-c^{2K+1}/D_K],\\
M/N^{\alpha_K}\longrightarrow\infty&\quad\Longrightarrow\quad \mathcal F^{(K)}_{N,M}\longrightarrow0.
\end{aligned}}
```

The converse holds over all complex $`K`$-dimensional capture spaces and all allowed decoders. At $`K=1`$, the constant $`D_1=192`$ agrees with the one-mode theorem. At $`K=2`$, $`D_2=46080`$. For example, with $`M=\lfloor N^{3/4}\rfloor`$, one-mode fidelity tends to zero and two-mode fidelity tends to one. The fixed-$`K`$ limits do not establish a uniform formula for $`K`$ growing with $`N`$.

## Exact reduction to complete capture

Write $`\Psi_{N,m}`$ for the exact emitted state in the $`m`$-photon sector, and let $`P_{S,m}`$ be the orthogonal projector onto $`\mathrm{Sym}^m S`$. Set $`b_m(S)=\lVert P_{S,m}\Psi_{N,m}\rVert`$ and $`b_0=1`$.

On a number-state input $`m`$, any photon in the discarded field leaves fewer than $`m`$ photons for the decoder. A number-preserving decoder cannot then overlap with the $`m`$-photon target. This gives an upper bound $`b_m(S)^2`$ for that input. Conversely, in every $`m`$-photon block choose a unitary that sends the normalized projected state to $`|m,0,\ldots,0\rangle`$ with positive real amplitude. A block with $`b_m=0`$ can use any unitary. The direct sum is one fixed unitary. Its vacuum-environment Kraus operator has diagonal entries $`b_0,\ldots,b_M`$. All other Kraus operators lower the output number. For every input density matrix $`\rho`$, the vacuum-environment contribution to entanglement fidelity is $`(\sum_m\rho_{mm}b_m)^2`$, which is at least $`\min_m b_m^2`$. A minimizing number input attains the bound. Therefore

```math
\mathcal F^{(K)}_{N,M}=\sup_{\dim S=K}\min_{0\le m\le M}b_m(S)^2.
```

For $`K=1`$, the decoder could only adjust number-sector phases. Taking the absolute value of a single waveform attains the same optimum without those adjustments, by positivity of the emitted amplitudes. [One-mode reduction](MODEL.md#reduction-of-the-channel-objective)

For $`m\ge1`$, use $`a_m=(m-1)/N`$ and the normalized [matched pulse](MATCHED_PULSES.md) $`f_{a_m}`$. The existing uniform source bound gives

```math
\begin{aligned}
\left|b_m(S)-\lVert P_S f_{a_m}\rVert^m\right|&\le \epsilon_{N,M},\\
\epsilon_{N,M}&=\sqrt{2(1-e^{-B_{N,M}/2})},\\
B_{N,M}&=\frac{M(M-1)}{12N^2[1-(M-1)/N]^2}.
\end{aligned}
```

Here $`\epsilon_{N,M}=0`$ for $`M=0,1`$. For other $`M\le N`$, the bound is uniform in $`S`$ and $`m`$. Both quantities inside the difference belong to $`[0,1]`$. Thus the squared-amplitude optima in the exact and product-pulse models differ by at most $`2\epsilon_{N,M}`$. This error vanishes whenever $`M=o(N)`$. It controls amplitudes absolutely, which is sufficient for the crossover and for the fixed subcodes used on the supercritical side.

## Pulse geometry and the optimal construction

Set $`\delta=M/N`$ and consider $`M\ge1`$. The change of variables $`z=1-e^{-\tau}`$ identifies the pulse Hilbert space with $`L^2([0,1],dz)`$ by writing $`f(\tau)=e^{-\tau/2}g(z)`$. The matched family becomes

```math
g_a(z)=\frac{\sqrt{1-a}}{1-az}=\sum_{j=0}^{\infty}a^j v_j(z).
```

On a fixed real neighborhood of $`a=0`$ the Taylor remainder is uniform in $`z\in[0,1]`$. Each $`v_j`$ is a monic polynomial of degree $`j`$. Set $`J=\mathrm{span}(v_0,\ldots,v_{K-1})`$. The degree-$`K`$ direction missed by $`J`$ is the monic shifted Legendre polynomial $`w=(I-P_J)v_K`$. Its squared norm is

```math
h_K=\lVert w\rVert^2=\frac{1}{(2K+1)\binom{2K}{K}^2}.
```

Choose $`r_1,\ldots,r_K`$ to be the roots in $`(0,1)`$ of the following monic polynomial, defined at zero by continuity. Here $`T_j`$ is the Chebyshev polynomial of the first kind.

```math
p_K(x)=2^{-2K}\frac{T_{2K+1}(\sqrt{x})}{\sqrt{x}},\qquad
S_\delta=\mathrm{span}\{f_{\delta r_1},\ldots,f_{\delta r_K}\}.
```

Use any real orthonormal basis of this span for the captured modes. One stable basis procedure is to apply the inverse Vandermonde matrix at the $`r_i`$, then divide its $`j`$th output by $`\delta^j`$ for $`j=0,\ldots,K-1`$. In the $`z`$ representation the resulting basis vectors equal $`v_j+O_K(\delta^{K-j})`$ uniformly. Orthonormalizing these vectors is well conditioned for small $`\delta`$, and the resulting projectors satisfy $`\lVert P_{S_\delta}-P_J\rVert=O_K(\delta)`$ in that representation.

If $`L_i(x)`$ are the Lagrange basis polynomials for the nodes $`r_i`$, the Taylor coefficients of degree below $`K`$ cancel in the interpolation residual. The degree-$`K`$ error is exactly monic. Projecting onto the orthogonal complement of $`S_\delta`$ yields, uniformly in $`x\in[0,1]`$,

```math
(I-P_{S_\delta}) g_{\delta x}=\delta^K p_K(x)w+O_K(\delta^{K+1}).
```

The same symbol $`S_\delta`$ denotes the subspace in either unitarily equivalent representation. The product-pulse squared capture amplitude is $`(1-\lVert (I-P_{S_\delta})g_{a_m}\rVert^2)^m`$. With $`x_m=(m-1)/M`$, the critical limit has $`M\delta^{2K}\to c^{2K+1}`$, and its negative logarithm is uniformly

```math
M\delta^{2K}h_K x_m|p_K(x_m)|^2+o(1).
```

This follows from $`m/M=x_m+1/M`$ and the uniform logarithm expansion at a leakage probability of order $`\delta^{2K}`$. The maximum of $`x|p_K(x)|^2`$ on $`[0,1]`$ is $`2^{-4K}`$, and the excitation grid becomes dense in the critical limit. In the subcritical regime, $`M\delta^{2K}\to0`$ and the uniform residual bound makes the complete-capture probability tend to one.

For two modes the polynomial is $`p_2(x)=x^2-5x/4+5/16`$. Its two roots are $`(5\pm\sqrt5)/8`$. The three excitation fractions that give the largest leading leakage are $`1`$ and $`(3\pm\sqrt5)/8`$. For one mode this construction chooses the excitation fraction $`3/4`$ to leading order and yields the earlier crossover coefficient.

## Converse for every capture subspace

Work at critical scaling. Take a sequence of capture spaces $`S`$ along a subsequence where the product-pulse worst fidelity is bounded below by a positive constant. The case of fidelity tending to zero already satisfies the desired upper bound. At $`K`$ distinct fixed positive fractions in $`(0,1]`$, take the nearest excitation-grid points $`x_i`$. Then $`m_i\asymp M`$ and

```math
\lVert (I-P_S)g_{\delta x_i}\rVert=O(M^{-1/2})=O(\delta^K).
```

Indeed, $`(1-d^2)^{m_i}\le e^{-m_i d^2}`$ for the corresponding distance $`d`$. Inserting the Taylor expansion and inverting the $`K\times K`$ Vandermonde matrix gives

```math
\lVert (I-P_S)v_j\rVert=O(\delta^{K-j}),\qquad j=0,\ldots,K-1.
```

The matrix inverses stay bounded because their nodes approach distinct limits. Since $`v_0,\ldots,v_{K-1}`$ are a fixed basis of $`J`$, this bounds the gap from $`J`$ to $`S`$ by $`O(\delta)`$. Their dimensions are equal, so the gap in the other direction is also $`O(\delta)`$. For example, the projected basis $`P_Sv_j`$ spans $`S`$ and is uniformly well conditioned for small $`\delta`$. In particular $`P_S=P_J+O(\delta)`$ in operator norm even when $`S`$ depends on $`N`$ and is complex.

Test the residual against the unit vector $`w/\sqrt{h_K}`$. The preceding estimates and Taylor expansion give, after dividing out $`\delta^K\sqrt{h_K}`$,

```math
\frac{\langle w/\sqrt{h_K},(I-P_S)g_{\delta x}\rangle}{\delta^K\sqrt{h_K}}
=x^K+\sum_{j=0}^{K-1}c_{j,N}x^j+O(\delta),\qquad |c_{j,N}|=O(1).
```

The degree-$`K`$ coefficient tends to one because $`(I-P_S)v_K=w+O(\delta)`$. This expansion is uniform on $`[0,1]`$. The norm is at least the modulus of this scalar component. Multiplying a monic polynomial $`p(x)`$ of degree $`K`$ by the weight $`\sqrt{x}`$ amounts to considering the monic odd polynomial $`t p(t^2)`$ on $`[-1,1]`$. For complex coefficients, taking the real part preserves the real leading coefficient and can only decrease the uniform norm. The alternating extrema of $`T_{2K+1}`$ show that the minimum monic norm on this interval is $`2^{-2K}`$. A polynomial improving that norm would differ from the scaled Chebyshev polynomial by a degree-$`2K`$ polynomial changing sign across each of its $`2K+1`$ alternating intervals. The minimizing Chebyshev polynomial is odd, so the same minimum applies in the odd class.

The bounded coefficients make the polynomial estimate uniform when the discrete excitation grid replaces the interval. At some $`m\in\{1,\ldots,M\}`$ it follows that the product-pulse fidelity is at most

```math
\exp\!\left[-M\delta^{2K}\bigl(h_K2^{-4K}-o(1)\bigr)\right].
```

This proves the sharp upper bound. The product-pulse error transfers the two critical bounds back to the exact emitted state. For supercritical $`M`$, restrict to a consecutive subcode of cutoff $`\lfloor cN^{\alpha_K}\rfloor`$ at any fixed $`c>0`$. Its optimal fidelity upper bounds the larger code's fidelity, even when the receiver was designed for the larger code. Take the limit at fixed $`c`$ before sending $`c`$ to infinity. That order avoids using the product approximation at extensive excitation.

## Receiver construction and finite checks

### Coherent decoding from one-photon data

The asymptotic construction does not need the exact correlated $`m`$-photon wavefunctions. In an orthonormal basis of $`S_\delta`$, calculate the unit vector $`q_m=P_{S_\delta}f_{a_m}/\lVert P_{S_\delta}f_{a_m}\rVert`$ and choose a real orthogonal transformation $`V_m`$ that takes $`q_m`$ to the first basis vector. The direct sum of $`\mathrm{Sym}^m(V_m)`$ takes the product-reference complete-capture component to $`|m,0,\ldots,0\rangle`$ with amplitude $`\lVert P_{S_\delta}f_{a_m}\rVert^m`$. When a projection vanishes, the rotation in that sector is arbitrary. For the exact source, the vacuum-environment amplitude differs from this nonnegative number by at most $`\epsilon_{N,M}`$ in every sector. The worst-input squared fidelity of this implementable block rule is therefore at least

```math
\left[\max\left\{0,\min_{1\le m\le M}\lVert P_{S_\delta}f_{a_m}\rVert^m-\epsilon_{N,M}\right\}\right]^2.
```

For $`M=0`$ the transfer is exact. Mode overlaps for the calculation follow from $`\langle f_a,f_b\rangle=K(-\log(1-a)+\log(1-b))`$, where $`K(u)=u/[2\sinh(u/2)]`$ is the kernel in [Matched pulses](MATCHED_PULSES.md#exact-pulse-geometry). Equivalently the squared projection is $`k^\dagger G^{-1}k`$, where $`G_{ij}=\langle f_{\delta r_i},f_{\delta r_j}\rangle`$ and $`k_i=\langle f_{\delta r_i},f_{a_m}\rangle`$. An orthonormal basis or high precision avoids conditioning problems as the snapshot pulses approach one another.

The control can also use a single polynomial in the total-number operator. Choose the first oscillator axis along $`P_{S_\delta}f_0`$ and a real orthonormal basis for the rest. The direction of $`P_{S_\delta}f_a`$ is analytic near $`a=0`$ and equals the first axis at zero. Its norm is bounded away from zero uniformly as $`\delta\to0`$. A rotation taking that direction to the first axis is analytic and equals the identity at zero. One explicit choice for real unit vectors $`q=q(a)`$ and $`e_1`$ is $`I+A+A^2/(1+e_1^Tq)`$, where $`A=e_1q^T-qe_1^T`$. The analytic logarithm of this rotation is real skew-symmetric. Replacing it with its degree-$`K`$ Taylor polynomial incurs $`O_K(\delta^{K+1})`$ one-photon angular error on $`0\le a\le\delta`$. Since both rotations are real, the loss of the target-axis overlap is $`O_K(\delta^{2K+2})`$. On the code this loses at most $`O_K(M\delta^{2K+2})`$ in vacuum-environment amplitude, which vanishes throughout the critical and subcritical regimes.

Second-quantize this polynomial one-photon generator with $`a=(\hat n-1)/N`$, where $`\hat n`$ is the total number on the captured register. The number operator commutes with every bilinear mode-mixing generator, and the vacuum block is automatic. For two modes this is a beam-splitter rotation with an angle quadratic in $`(\hat n-1)/N`$. The construction charges the ability to implement this nonlinear coherent control. It does not give a bound on its gate count, coupling duration or accuracy on a specified detector platform.

### A finite all-subspace upper envelope

Whenever $`M\ge K+1`$, choose any $`K+1`$ distinct positive excitation numbers $`m_i\le M`$. Compute the weighted pulse Gram matrix

```math
H_{ij}=\sqrt{m_i m_j}\,\langle f_{a_{m_i}},f_{a_{m_j}}\rangle.
```

For any $`K`$-dimensional $`S`$, the sum of squared distances of the vectors $`\sqrt{m_i} f_{a_{m_i}}`$ from $`S`$ is at least $`\lambda_{\min}(H)`$. This follows by summing the discarded eigenvalues of their one-photon frame operator, whose nonzero eigenvalues are those of $`H`$. At least one of their weighted squared distances is therefore at least $`\lambda_{\min}(H)/(K+1)`$. The exponential bound on product complete capture and the uniform source approximation give

```math
\mathcal F_{N,M}^{(K)}\le\min\!\left\{1,\left[\epsilon_{N,M}+
\exp\!\left(-\frac{\lambda_{\min}(H)}{2(K+1)}\right)\right]^2\right\}.
```

This finite envelope applies to the declared receiver class. It need not have the sharp constant, which comes from the polynomial minimax argument.

### Passive capture with bounded controls and a finite window

Ideal capture of an orthonormal set of modes can use a serial network of receiving oscillators whose couplings account for the pulse reshaping at earlier oscillators. That construction is inherited from Kiilerich and Mølmer. The result here determines which subspace to capture for the common unknown code and what number-coherent processing gives its fidelity. [Kiilerich and Mølmer, Appendix, Eqs. (35)–(43)](https://arxiv.org/abs/2003.04573)

A finite-window version can use $`K`$ coupled passive oscillators and one Markov input. In the scaled time of the source, put the conjugate envelopes of an orthonormal basis into a column $`\psi(t)`$, and define, for a fixed regularization $`\eta>0`$,

```math
Q(t)=\eta I+\int_0^t\psi(s)\psi(s)^\dagger\,ds,\qquad
R(t)=Q(t)^{1/2},\qquad
A(t)=-R(t)^{-1}\dot R(t),\qquad \beta(t)=R(t)^{-1}\psi(t).
```

The linear equation for the oscillator annihilation column $`c`$ is $`dc=A c\,dt+\beta\,db_{\rm in}`$. Differentiating $`R^2=Q`$ gives $`A+A^\dagger=-\beta\beta^\dagger`$. Thus it has a passive realization with vacuum initial oscillators, coupling row $`-\beta^\dagger`$ and one-particle Hamiltonian $`i(A-A^\dagger)/2`$. Integrating the equation after multiplying by $`R(t)`$ gives the exact capture map

```math
c(T)=Q(T)^{-1/2}\left[\sqrt\eta\,c(0)+\int_0^T\psi(t)\,db_{\rm in}(t)\right].
```

At complete capture time the regularization gives transmissivity $`1/(1+\eta)`$ on each basis mode. For the fixed-$`K`$ spaces above, the same stable interpolation basis used in the proof gives orthonormal envelopes bounded by $`C_K e^{-t/2}`$ for small $`\delta`$. The matched input envelopes have the same type of bound. As $`T\to\infty`$ and $`\eta\to0`$, the Gram matrix satisfies $`Q(T)=I+O_K(\eta+e^{-T})`$. Consequently the oscillator amplitude vector for each matched one-photon input differs from its ideal amplitude by $`O_K(\eta+e^{-T})`$. Composing with the coherent rotations gives a uniform $`O_K(M(\eta+e^{-T}))`$ change in product-reference target amplitudes. The uniform source bound then transfers the estimate to the exact Dicke field.

For growing $`M`$, one can take $`T=\log M+\omega(1)`$ and $`\eta=o(1/M)`$ so these errors vanish. The squared coupling norm and the Hamiltonian norm are bounded by $`O_K(1/\eta)`$ in scaled units for this construction. For the Hamiltonian bound, the derivative of the square root solves $`R\dot R+\dot R R=\dot Q`$, and $`R\ge\sqrt\eta I`$. The required control strength may thus grow with the code. This implementation assumes adjustable couplings and oscillator mixing and does not impose a slew-rate constraint or prove optimal control costs.

## Relation to existing receiver models

The Dicke cascade and the uniform matched-pulse approximation are inherited from the [existing source account](MATCHED_PULSES.md). Previous mode analyses identify occupied temporal modes, calculate their joint state or optimize transfer of selected preparations. The present optimization concerns a predetermined span for every unknown number superposition and its reference, followed by number-coherent conversion to one oscillator. The sharp constant comes from the best approximation of the complete number-dependent pulse family in that span. [Existing primary-source comparison](../references/COMPARISON.md) · [Kiilerich and Mølmer, 2020](https://doi.org/10.1103/PhysRevA.102.023717)
