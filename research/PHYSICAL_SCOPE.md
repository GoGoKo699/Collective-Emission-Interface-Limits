# Physical scope, error mechanism, and realization limits

**Consolidated 3 October 2026.** These are supporting consequences and assumption checks, not new independent headline claims. Their original numerical implementations are retained under `tests/03_passive_receiver` through `tests/06_source_realization`.

## A. What the receiver restriction means

A predetermined, number-preserving linear network maps annihilation operators linearly. If auxiliary inputs are vacuum and one canonical oscillator is retained, its final operator is a normalized signal temporal mode plus a vacuum mode, with attenuation. This is a standard passive-systems fact, not a no-go theorem for arbitrary quantum memories; see Yamamoto and James, arXiv:1403.1698.

Finite coupling and time constraints reduce the realizable kernels. Adding auxiliaries may improve that constrained engineering problem, but it cannot exceed the optimum over all ideal normalized kernels. Active Gaussian processing, nonlinear decoding, nonvacuum resources, receiver-to-source feedback, or retaining multiple output modes changes the stated class.

A receiving oscillator with coupling rate $\kappa_\varepsilon(t)=|f(t)|^2/[\varepsilon+F(t)]$, where $\varepsilon>0$ and $F(t)=\int_0^t|f(s)|^2ds$, and coupling phase matched to $f$, captures the normalized truncated pulse with transmission $q_T=F(T)/[\varepsilon+F(T)]$ when $F(T)>0$. The rate alone specifies capture of a nonnegative pulse; a general complex pulse also requires its phase. Perfect finite-time onset can require singular initial coupling. The ideal optimization is a supremum, not a hardware guarantee. Nurdin, James, and Yamamoto, arXiv:1609.05643, directly discuss this control issue.

## B. The leading mismatch has a simple structure

For the pulse coordinate $u=-\ln(1-a)$, its overlap kernel is $K(z)=z/[2\sinh(z/2)]$. The normalized tangent mode at the common pulse is

$$g_* = \sqrt{12}\,\partial_u f_u\big|_{u_*}.$$

It is orthogonal to $f_*$. A number-specific reference pulse projects onto their span with coefficients $K(z_m)$ and $-\sqrt{12}K'(z_m)$, $z_m=u_m-u_*$. The missed one-photon weight is $z_m^4/180+O(z_m^6)$.

At $M=O(N^{2/3})$, the whole code approaches a two-mode encoding, with an operator-norm isometry error of order at most $N^{-1/3}$. If $M/N^{2/3}\to c>0$ and $m/M\to x>0$, the second-mode photon count converges to a Poisson law with parameter

$$\lambda(x)=\frac{c^3}{12}x(x-3/4)^2.$$

The smallest zero-count probability recovers $e^{-c^3/192}$. This explains the common-mode error without claiming that radiation spreads over an ever-growing number of unrelated modes.

Two retained modes are an additional quantum resource. Their occupied direction depends on excitation number, so a fixed linear rotation cannot compress the entire encoding into one canonical oscillator. No nonlinear decoder is supplied. The full field remains an isometric encoding of the source.

## C. Scalar source pulse shaping

Prescribed controls $L(t)=e^{i\phi(t)}\sqrt{\Gamma(t)/N}\,S_-$ and $H(t)=\omega(t)\hat n$ preserve the complete-emission problem when $\Gamma(t)\geq0$ and the accumulated clock $\tau(t)=\int_0^t\Gamma(s)\,ds$ tends to infinity. Under these conditions they reparametrize and rephase every emitted photon through the same one-particle isometry:

```math
f(\tau)\longmapsto
\sqrt{\Gamma(t)}\,
e^{i\phi(t)-i\int_0^t\omega(s)\,ds}\,f(\tau(t)).
```

Once the receiver optimization allows all waveforms, these controls do not change its value. A finite accumulated clock leaves residual source excitation and does not satisfy this complete-emission invariance statement.

They can change duration or match a constrained receiver. A multilevel protocol must first be reduced to its actual ladder; it is not automatically described by this jump. A number-dependent coupling that makes the ladder rates linear is outside the scalar class. A harmonic oscillator is the successful simple comparator and emits all number states in one common exponential mode.

## D. Independent atomic loss

The optional audit model adds independent inaccessible decay at rate $\gamma_i$ to useful collective decay $\gamma_c\mathcal D[S_-]$. Set $r=\gamma_i/\gamma_c$ and $Q=N+r$.

The established probability that all $m$ photons enter the useful channel is

$$p_{N,m}=\prod_{j=0}^{m-1}\frac{N-j}{N+r-j}.$$

This formula and its collective suppression are already in Paulisch's thesis, Eq. (1.6). The maximal-collected-number amplitude equals $\sqrt{p_{N,m}}$ times the ideal $Q$-ladder amplitude, with the corresponding time scale. $Q$ is a real analytic parameter, not extra physical atoms. The rest of the channel is present and loses photons; the process is not heralded.

The canonical receiver fidelity is bounded by

$$p_{N,M}\mathcal F_{\rm id}(Q,M)\leq\mathcal F_{\rm ind}(N,M)
\leq\min\{p_{N,M},\mathcal F_{\rm id}(Q,M)\}.$$

At fixed positive $\gamma_c/\gamma_i$ and critical code scaling, the additional penalty tends to one. This does not claim that a physical device can hold all effective rates independently fixed.

## E. Bandwidth and duration

For resonant emitters coupled to a rapidly damped cavity, the conventional elimination gives $\gamma_c\simeq4g^2/\kappa$ with a separation such as $\kappa\gg g\sqrt N$. If $R=\kappa/(g\sqrt N)$, holding $g/\gamma_i$ fixed makes the effective ratio $\gamma_c/\gamma_i=4g/(R\gamma_i\sqrt N)$ decrease. The simple fixed-parameter cavity family therefore need not realize the favorable fixed-ratio asymptotic limit.

These relationships are conventional; Koppenhöfer et al., arXiv:2111.15647, supplies the cited cavity model. Its usual elimination condition is not asserted to control the full emitted field uniformly over an increasing code. The small full-cavity tests concern collected-photon probabilities, not a theorem proving optimized temporal-mode fidelity for every microscopic scaling path.

Off-resonant mapping that slows useful and unwanted rates together is an existing alternative in González-Tudela et al., arXiv:1504.07600. It preserves the rate ratio but changes duration and has additional level/control assumptions. It must not be omitted to manufacture a universal implementation no-go.

## F. External loss and source preparation

An additional independent link transmission $\eta$ imposes $F_{\rm worst}\leq\eta^M$ on the uncorrected canonical target. Losing one photon from the highest number gives the wrong number. This simple ceiling can dominate practical experiments; it does not remove the ideal mode-mismatch limit.

Symmetric preparation and the whole-code input promise are not established by reproducing intensity data or by demonstrating one excited state. The two-sector witness reduces the logical dimension needed to exhibit the mismatch, not the challenge of preparing high excitation numbers.

None of the source or receiver literature is claimed to demonstrate all assumptions jointly at the illustrative large $N$. The code uses the effective model as an explicit idealization. Repository development is not a declaration of a completed device design.

## Primary references

- V. Paulisch, *Waveguide Quantum Electrodynamics* (2018), Chapter 1: https://edoc.ub.uni-muenchen.de/22151/1/Paulisch_Vanessa.pdf
- N. Yamamoto and M. R. James, arXiv:1403.1698: https://arxiv.org/abs/1403.1698
- H. I. Nurdin, M. R. James, N. Yamamoto, arXiv:1609.05643: https://arxiv.org/abs/1609.05643
- M. Koppenhöfer et al., arXiv:2111.15647v3: https://arxiv.org/abs/2111.15647
- A. González-Tudela et al., Physical Review Letters 115, 163603 (2015): https://arxiv.org/abs/1504.07600
