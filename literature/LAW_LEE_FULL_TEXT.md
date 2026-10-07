# Law–Lee 2007: full-text comparison of the fixed interface result

C. K. Law and S. K. Y. Lee, *Dynamic photon-mode selection in Dicke superradiance*, Physical Review A 75, 033813 (2007), DOI [10.1103/PhysRevA.75.033813](https://doi.org/10.1103/PhysRevA.75.033813). This comparison covers the complete six-page article: Eqs. (1)–(30), figures/captions and notes [16]–[17], with mathematical typography and figures checked against rendered pages. The article has no separate appendix.

Law–Lee establishes optimized mean-occupation modes, the oscillator comparator, dominant two-mode behavior and the semiclassical hyperbolic-secant pulse. The distinction developed below is between those results and uniform canonical transfer of an unknown growing code.

## 1. What the paper actually optimizes

Section II A, Eqs. (7)–(15), defines field modes and diagonalizes the positive one-photon correlation kernel $`W`$. Its eigenvalues are the mean mode populations,

```math
\lambda_j=\langle b_j^\dagger b_j\rangle.
```

The paragraph following Eq. (13) explicitly identifies the first eigenmode as maximizing the average photon number, followed by the largest occupation subject to orthogonality, and so on. This is an optimization over mode functions, not a calculation restricted to an arbitrary exponential. It must not be described as lacking mode optimization.

For approximately frequency-independent coupling, Eqs. (16)–(17) translate the construction into temporal modes of the two-time dipole correlation. Section II B, Eqs. (18)–(21), defines the mode purity

```math
\mathcal P_F=\frac{\sum_j\lambda_j^2}{N_\gamma^2},\qquad N_\gamma=\sum_j\lambda_j,
```

and its inverse as an effective mode number. This is the purity of the normalized one-photon correlation operator, not the purity or fidelity of the full multiphoton density operator.

The repository instead optimizes

```math
\sup_{\|f\|=1}\min_{m\leq M}|\langle m_f|\Psi_{N,m}\rangle|^2,
```

with one waveform chosen for the entire unknown input code and the canonical number-state target. The complete-emission limit of their temporal-mode construction is directly relevant. Calling their modes time dependent and ours fixed is **not** the substantive difference: fixing a final collection time produces an ordinary temporal envelope in their construction too.

## 2. The models overlap; normalization conventions must be translated

The article's Eq. (1) uses identical collective spin coupling to a one-dimensional field continuum. Section II C derives the Born–Markov master equation, neglects dipole–dipole terms, and discusses a Raman/bad-ring-cavity route to the idealization. These are direct predecessors for the source convention, not experimental evidence that every growing-code assumption is jointly realized.

Their Eq. (22) writes the dissipator as

```math
\gamma_{\rm LL}(2J_-\rho J_+-J_+J_-\rho-\rho J_+J_-).
```

With the convention $`\mathcal D[L]\rho=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$, the repository parameter is $`\gamma_{\rm repo}=2\gamma_{\rm LL}`$. Hence $`\tau=N\gamma_{\rm repo}t=2N\gamma_{\rm LL}t`$. This is a notation conversion, not a correction to the article.

Equation (25) obtains the two-time correlation from a general diagonal initial Dicke population. Although Eq. (5) introduces the fully excited case, the paper is not confined to that preparation: Section III C explicitly treats the half-excited state. The matrix elements relevant to its number-preserving correlation do not constitute a reference-entangled channel-fidelity calculation.

## 3. Results that must be credited directly

| Location | Established result | Consequence for our presentation |
|---|---|---|
| Section II A, Eqs. (10)–(17) | Optimal mean-occupation modes from the full correlation kernel | Do not claim first waveform optimization or a new natural-mode method. |
| Section III A, Eq. (26), Fig. 1 | Analytic two-atom correlation and its nonfactorability; leading normalized populations about 0.957 and 0.0345 | The two-photon multimode example is inherited. |
| Section III B, Figs. 2–3, Eq. (27) | Fully inverted large ensembles with limiting mode purity about 0.82; the first two modes hold about 98% of the total mean photon number in the illustrated case | A few dominant modes or two-mode superradiant light is not new. This is not our uniform two-mode encoding theorem for subextensive codes. |
| Opening of Section III and note [16] | Replacing the spin by one harmonic oscillator makes the emitted radiation exactly single mode, by linear Heisenberg evolution | The successful oscillator comparator is explicitly already in this paper. |
| Section III C, Eqs. (29)–(30) | Half-excited semiclassical factorization and a hyperbolic-secant pulse; numerical checks of mode purity | The familiar semiclassical pulse must not be relabeled a newly invented waveform. |
| Section II C, final paragraph | Dipole-interaction omission, Raman suppression, and a well-defined cavity output channel | This supports a model idealization, not a uniform microscopic realization theorem. |

The percentages in this table are reported by the article's prose and captions. They refer to occupations or mode purity, not to successful all-photon capture events. The numerical discussion and large-$`N`$ formula in Section III B concern initially fully inverted ensembles, whereas our critical code has vanishing maximal excitation fraction.

## 4. Why high mode purity is relevant but not sufficient

The distinction between metrics should be demonstrated, not used as a verbal escape. On a fixed $`m`$-photon sector define

```math
p_f=\frac{\langle n_f\rangle}{m},\qquad F_f=\Pr(n_f=m).
```

For a pure output $`F_f`$ is the squared overlap with $`|m_f\rangle`$. The elementary operator inequalities

```math
I-\Pi_{n_\perp=0}\leq n_\perp\leq m(I-\Pi_{n_\perp=0}),\qquad n_\perp=m-n_f,
```

give

```math
\boxed{\max\{0,1-m(1-p_f)\}\leq F_f\leq p_f.}
```

Thus exact rank-one correlation, $`p_f=1`$, really does imply support on one field mode. We do **not** dispute the exact separability criterion. At fixed finite $`m`$, occupation tending to one also forces full-mode fidelity to one. The nonuniformity appears when $`m`$ grows: $`p_f\to1`$ alone does not imply $`m(1-p_f)\to0`$.

For the normalized natural occupations $`p_j=\lambda_j/m`$, $`\mathcal P_F=\sum_jp_j^2`$ satisfies $`p_1^2\leq\mathcal P_F\leq p_1`$. The leading mode consequently has

```math
F_{f_1}\geq\max\{0,1-m(1-\mathcal P_F)\}.
```

This is a legitimate route from a sufficiently accurate occupation theorem to state fidelity. The supplied paper does not furnish that uniformly vanishing full-state error over one shared growing code, or an upper bound ruling out all common waveforms.

As a purely mathematical control, for orthogonal modes $`f,g`$ and $`m\geq3`$, the two pure states

```math
|m-1,1\rangle_{f,g},\qquad
\sqrt{1-1/m}|m,0\rangle_{f,g}+m^{-1/2}|0,m\rangle_{f,g}
```

have identical one-photon correlation operators and mode purities. Their probabilities of all photons lying in $`f`$ are respectively zero and $`1-1/m`$. These are not asserted to be Dicke outputs. They show why a first-order correlation kernel alone cannot determine the general multiphoton objective.

There is a useful exception: for a pure two-photon field the symmetric Schmidt (Takagi) decomposition makes the maximum product-mode Fock overlap equal to the largest normalized natural occupation. The two-atom example is therefore not evidence that these objectives are unrelated in every sector. This special equality does not extend the paper into a uniform common-code theorem.

## 5. The half-excited result is compatible, and its pulse is an exact shape correspondence

Section III C uses the semiclassical approximation for an initially half-excited system and obtains $`v_1(t)\propto\mathrm{sech}(N\gamma_{\rm LL}t)`$. The source explicitly marks Eq. (29) as approximate and reports finite numerical purities, not an exact finite-$`N`$ full-field identity.

For our comparison pulse family, direct substitution gives

```math
f_{1/2}(\tau)=\frac{1}{\sqrt{2}}\mathrm{sech}(\tau/2).
```

Using the rate conversion above, this is the same normalized shape on the positive time axis. For $`m=N/2`$, the repository parameter $`a_m=(m-1)/N`$ tends to $`1/2`$, but is not exactly $`1/2`$ at finite $`N`$.

This shape correspondence is our algebraic comparison; the paper does not assert the repository's general pulse-family or uniform-entropy theorem. Conversely, our controlled product-state approximation is for $`m=o(N)`$ and must not be extended to $`m=N/2`$ just because its trial pulse has the correct semiclassical limit. The article studies one half-excited preparation with its own optimal mode, not a receiver committed to one mode for every unknown number component.

## 6. What survives the comparison

The full article does not state the following combined result: a uniform norm approximation of the emitted isometry over a growing number code; an optimization of canonical worst-input state-transfer fidelity over every common waveform; and a matching constructive/converse critical law. The quantities optimized in Eqs. (13) and (18), the initial conditions in Section III, and the observables controlled in Eqs. (27) and (29) do not supply that combination by substitution.

This conclusion does not claim that their methods could never be extended to address the question. Nor does it make a changed objective, by itself, a substantial contribution. The candidate contribution remains the **sharp optimized uniform boundary between canonical state transfer and mean-photon collection for the specified collective source and one linear memory**.

The paper is a foundational predecessor for several explanatory ingredients. The theorem, its $`N^{2/3}`$ scaling domain, the receiver restriction, and its proof are unchanged by this comparison. We do not claim a new Dicke model, first oscillator comparison, first two-mode description, or first semiclassical pulse matching.

The [canonical proof](../research/THEOREM.md) gives the finite inequalities and quantifiers for the uniform result; the [assumption register](ASSUMPTIONS.md) states its preparation and realization scope.
