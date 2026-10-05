# When ordinary loss masks the common-mode limitation

**Internal supporting derivation, 5 October 2026.** This answers a physical-scope
question already raised in [PHYSICAL_SCOPE.md](PHYSICAL_SCOPE.md): when does mode
mismatch reduce the best uniform fidelity beyond the ordinary transmission ceiling?
It uses the existing source, canonical number target and passive one-output receiver.
It is a consequence of the pulse approximation and geometry in
[THEOREM.md](THEOREM.md), not an additional headline novelty claim or a device proposal.

## 1. Specified loss channel and exact objective

Add a prescribed pure-loss channel with intensity transmission $0\leq\eta\leq1$,
independent of photon number and uniform over the temporal modes. Its inaccessible
input is vacuum. Such loss commutes with passive mode selection and can equivalently
be placed after selection. Spectral filtering, mode-dependent attenuation and
independent atomic decay are not this channel. There is no conditioning on a
successful transmission event.

For a nonnegative normalized receiving pulse, write
$A_m(f)=\langle m_f|\Psi_{N,m}\rangle\geq0$. The no-discarded-photon Kraus operator
has diagonal entries $\eta^{m/2}A_m(f)$. All other Kraus operators lower the output
number. The channel reduction in the theorem therefore gives exactly

$$\mathcal F^{(\eta)}_{N,M}
=\sup_{\|f\|_2=1}\min_{0\leq m\leq M}\eta^m|A_m(f)|^2.$$

As in the lossless theorem, the supremum may be restricted to nonnegative pulses:
taking the absolute value of a complex pulse improves every Fock overlap, and the
positive pulse attains its displayed worst-input value, including reference-entangled
inputs. Extra discretionary attenuation cannot improve this optimum. In particular,

$$\mathcal F^{(\eta)}_{N,M}\leq\eta^M.$$

For $M\geq1$ and $\eta=0$ the fidelity is zero; the vacuum-only code has fidelity one.
The following nontrivial limits and finite brackets use $\eta>0$.

## 2. Joint critical limit

Consider sequences with

$$\begin{gathered}
\frac{M}{N^{2/3}}\longrightarrow c>0,\\
\Lambda_N=-M\log\eta_N\longrightarrow\lambda\in[0,\infty),\\
A=\frac{c^3}{12},\qquad\delta=\frac{\lambda}{A}.
\end{gathered}$$

Then the optimized squared worst-input entanglement fidelity obeys

$$\boxed{\begin{gathered}
\mathcal F^{(\eta_N)}_{N,M}\longrightarrow e^{-E(A,\lambda)},\\
E(A,\lambda)=\lambda+\frac{(A/4-\lambda)_+^2}{A}.
\end{gathered}}$$

Here $(y)_+=\max(y,0)$. A receiving pulse from the existing family suffices:

$$\begin{gathered}
a_N=\frac{b_*M-1}{N},\\
b_* = \min\{1,3/4+\delta\}.
\end{gathered}$$

This is an asymptotically optimal choice, not an asserted exact finite-size optimizer.
The lossless endpoint gives $E(A,0)=A/16=c^3/192$ as required.

### Uniform reduction to product pulses

The theorem provides $\varepsilon_N\to0$ such that, simultaneously for all
$1\leq m\leq M$,

$$\begin{gathered}
\bigl\|\Psi_{N,m}-|m_{f_{a_m}}\rangle\bigr\|\leq\varepsilon_N,\\
a_m=(m-1)/N\quad(m\geq1).
\end{gathered}$$

For every normalized $f$, the difference between its exact sector fidelity and
the product-reference sector fidelity is at most $2\varepsilon_N$:

$$\left|\eta_N^m|A_m(f)|^2
-\eta_N^m|\langle f,f_{a_m}\rangle|^{2m}\right|
\leq2\varepsilon_N.$$

The same bound holds after a minimum over sectors and a supremum over pulses.
Thus no sum over the growing code dimension appears. Vacuum is treated exactly.

### Construction and scalar certificate

For a fixed $b\in[3/4,1]$, choose $a=(bM-1)/N$. With $x=m/M$, the kernel
$K(z)=z/[2\sinh(z/2)]$ and $\log K(z)=-z^2/24+O(z^4)$ give, uniformly over the code,

$$\eta_N^m K(u_m-u)^{2m}
\longrightarrow\exp\{-\lambda x-Ax(x-b)^2\}.$$

For $0\leq\delta\leq1/4$, set $t=\delta+1/4$ and $b=t+1/2$. The exact identity

$$t^2-x[\delta+(x-b)^2]=(1-x)(x-t)^2\geq0
\qquad(0\leq x\leq1)$$

shows that the largest exponent is $At^2$, attained at $x=t$ and $x=1$.
For $\delta\geq1/4$, choose $b=1$. Then

$$\delta-x[\delta+(x-1)^2]
=(1-x)[\delta-x(1-x)]\geq0,$$

so the largest exponent is $A\delta=\lambda$, attained at $x=1$.
These constructions give the claimed limiting lower bound on fidelity.

### Converse for every waveform

Use approximate maximizers; existence of an optimal waveform is unnecessary.
Along any subsequence with limiting fidelity $F>0$, put $E=-\log F$.
The exact loss ceiling implies $E\geq\lambda$. For any fixed $r\in(0,1)$,
take $q=\lfloor rM\rfloor$. Uniform product-state control, the projective Hilbert
angle triangle inequality through the arbitrary receiving pulse, and
$\arccos(e^{-s})\leq\sqrt{2s}$ give in the limit

$$\sqrt A(1-r)
\leq\sqrt{E/r-\lambda}+\sqrt{E-\lambda}.$$

More explicitly, if the approximate receiver's exact worst fidelity is $F_N$,
its product-reference fidelity is at least
$G_N=\max\{0,F_N-2\varepsilon_N\}$. For large $N$, $G_N>0$ and the finite
inequality before taking the limit is

$$\sqrt M\,\arccos K(u_M-u_q)
\leq\sqrt{\frac{M}{q}(-\log G_N)-\Lambda_N}
+\sqrt{-\log G_N-\Lambda_N}.$$

Both radicands are nonnegative because $G_N\leq F_N\leq\eta_N^M$.
The left-hand side tends to $\sqrt A(1-r)$.

For $0\leq\delta<1/4$, choose $r=t=\delta+1/4$. At $E=At^2$ the right-hand
side equals

$$\sqrt A\,[1/2+(1/4-\delta)]=\sqrt A(1-t).$$

It is strictly increasing in $E$ on its allowed domain, so $E<At^2$ is impossible.
For $\delta\geq1/4$, $E\geq\lambda$ already matches the construction. A zero
limiting fidelity automatically satisfies the upper bound. This proves the limit
for arbitrary waveforms, including complex ones, and closes the scalar optimization
without assuming the optimizer belongs to the pulse family.

## 3. Finite certificates

The asymptotic limit does not replace finite-size checks. A closed constructive
bound avoids a scan over sectors. For $M\geq2$, set

$$\begin{gathered}
b_M=1-(M-1)/N,\\
B_M=\frac{M(M-1)}{12N^2b_M^2},\\
\varepsilon=\sqrt{2(1-e^{-B_M/2})},
\end{gathered}$$

$$\begin{gathered}
A_N=\frac{M^3}{12N^2b_M^2},\qquad\Lambda_N=-M\log\eta,\\
b=\min\{1,3/4+\Lambda_N/A_N\}.
\end{gathered}$$

Choose $a=(bM-1)/N$. The inequalities
$|u_m-u|\leq|m-bM|/(Nb_M)$ and $\log K(z)\geq-z^2/24$, together with the scalar
certificate above, give a weighted product-overlap amplitude of at least
$e^{-E(A_N,\Lambda_N)/2}$ in every sector. Uniform vector error then gives

$$\boxed{\displaystyle
\mathcal F^{(\eta)}_{N,M}\geq
\left[\max\{0,e^{-E(A_N,\Lambda_N)/2}-\varepsilon\}\right]^2.}$$

This is a finite bound, with a finite pulse choice, valid throughout
$2\leq M\leq N$. It converges to the critical law's constructive side. For $M=1$,
the exact optimum is $\eta$.

Sharper sectorwise bounds keep the theorem's
$\beta_m=\arccos(e^{-D_{N,m}/2})$ and define $\cos_+(y)=\cos y$ for
$0\leq y\leq\pi/2$, and zero for $y>\pi/2$.
For any chosen family pulse $f_a$, a constructive certificate is

$$\mathcal F^{(\eta)}_{N,M}\geq
\min_{1\leq m\leq M}\eta^m
\cos_+^2\!\left\{\arccos[K(u_m-u)^m]+\beta_m\right\}.$$

Vacuum contributes the value one. For $M\geq2$ and a proposed simultaneous fidelity
$0\leq F\leq\eta^M$, define

$$R_{m,\eta}(F)=\arccos\!\left\{
\cos_+\!\left[\arccos\sqrt{F/\eta^m}+\beta_m\right]^{1/m}
\right\}.$$

Every common receiving waveform achieving at least $F$ must obey, for each
$1\leq q<M$,

$$R_{q,\eta}(F)+R_{M,\eta}(F)\geq\arccos K(u_q-u_M).$$

Solving this scalar necessary condition, together with $F\leq\eta^M$, gives a
finite all-waveform upper certificate. These are the existing angle brackets with
the sector-dependent transmission factor inserted; they need not coincide at
finite $N$.

## 4. What changes in an interface assessment

The extra exponent beyond ordinary loss is

$$E(A,\lambda)-\lambda=\frac{(A/4-\lambda)_+^2}{A}.$$

When $\lambda<c^3/48$, common-mode incompatibility lowers the asymptotic optimized
fidelity below the transmission ceiling. The two limiting constraining excitation
fractions are $x=1/4+12\lambda/c^3$ and $x=1$, and the best pulse moves toward the
highest-excitation pulse as loss increases.

When $\lambda\geq c^3/48$, the leading optimized fidelity equals the ordinary-loss
ceiling. Matching the highest sector leaves enough fidelity margin in the lower
sectors. This does not mean that their mode mismatch vanishes, that finite-size
fidelity reaches the ceiling exactly, or that loss improves transfer: $E(A,\lambda)$
is nondecreasing in $\lambda$.

The balance requires $\eta_N\to1$. Any fixed $\eta<1$ with $M\to\infty$, or more
generally $-M\log\eta_N\to\infty$, forces fidelity to zero by the loss ceiling
alone. Consequently the ideal common-mode boundary is not automatically the dominant
limitation of a high-excitation device. This supporting result supplies a precise
comparison within the already specified effective model; it does not establish
source preparation, calibrated microscopic rates or a combined implementation.
