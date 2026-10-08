# Law–Lee 2007: full-text comparison of the fixed interface result

C. K. Law and S. K. Y. Lee, *Dynamic photon-mode selection in Dicke superradiance*, Physical Review A 75, 033813 (2007), DOI [10.1103/PhysRevA.75.033813](https://doi.org/10.1103/PhysRevA.75.033813). This comparison covers the complete six-page article: Eqs. (1)–(30), figures/captions and notes [16]–[17].

Law–Lee establishes optimized mean-occupation modes, the oscillator comparator, dominant two-mode behavior and the semiclassical hyperbolic-secant pulse. The distinction developed below is between those results and uniform canonical transfer of an unknown growing code.

## 1. What the paper actually optimizes

Section II A, Eqs. (7)–(15), defines field modes and diagonalizes the positive one-photon correlation kernel $`W`$. Its eigenvalues are the mean mode populations,

```math
\lambda_j=\langle b_j^\dagger b_j\rangle.
```

The paragraph following Eq. (13) explicitly identifies the first eigenmode as maximizing the average photon number, followed by the largest occupation subject to orthogonality, and so on. The optimization ranges over mode functions.

For approximately frequency-independent coupling, Eqs. (16)–(17) translate the construction into temporal modes of the two-time dipole correlation. Section II B, Eqs. (18)–(21), defines the mode purity

```math
\mathcal P_F=\frac{\sum_j\lambda_j^2}{N_\gamma^2},\qquad N_\gamma=\sum_j\lambda_j,
```

and its inverse as an effective mode number. This is the purity of the normalized one-photon correlation operator, not the purity or fidelity of the full multiphoton density operator.

The repository instead optimizes

```math
\sup_{\|f\|=1}\min_{m\leq M}|\langle m_f|\Psi_{N,m}\rangle|^2,
```

with one waveform chosen for the entire unknown input code and the canonical number-state target. The complete-emission limit of their temporal-mode construction is directly relevant. Fixing a final collection time produces an ordinary temporal envelope in their construction too.

## 2. The models overlap; normalization conventions must be translated

The article's Eq. (1) uses identical collective spin coupling to a one-dimensional field continuum. Section II C derives the Born–Markov master equation, neglects dipole–dipole terms, and discusses a Raman/bad-ring-cavity route to the idealization. These are direct predecessors for the source convention.

Their Eq. (22) writes the dissipator as

```math
\gamma_{\rm LL}(2J_-\rho J_+-J_+J_-\rho-\rho J_+J_-).
```

With the convention $`\mathcal D[L]\rho=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$, the repository parameter is $`\gamma_{\rm repo}=2\gamma_{\rm LL}`$. Hence $`\tau=N\gamma_{\rm repo}t=2N\gamma_{\rm LL}t`$. This is a notation conversion, not a correction to the article.

Equation (25) obtains the two-time correlation from a general diagonal initial Dicke population. Although Eq. (5) introduces the fully excited case, the paper is not confined to that preparation: Section III C explicitly treats the half-excited state. The matrix elements relevant to its number-preserving correlation do not constitute a reference-entangled channel-fidelity calculation.

## 3. Established ingredients

| Location | Established result | Relation to the interface theorem |
|---|---|---|
| Section II A, Eqs. (10)–(17) | Optimal mean-occupation modes from the full correlation kernel | The natural-mode method optimizes occupation. |
| Section III A, Eq. (26), Fig. 1 | Analytic two-atom correlation and its nonfactorability; leading normalized populations about 0.957 and 0.0345 | The two-photon multimode example is inherited. |
| Section III B, Figs. 2–3, Eq. (27) | Fully inverted large ensembles with limiting mode purity about 0.82; the first two modes hold about 98% of the total mean photon number in the illustrated case | Dominant two-mode occupation precedes the uniform two-mode encoding result for subextensive codes. |
| Opening of Section III and note [16] | Replacing the spin by one harmonic oscillator makes the emitted radiation exactly single mode, by linear Heisenberg evolution | This supplies the oscillator comparator. |
| Section III C, Eqs. (29)–(30) | Half-excited semiclassical factorization and a hyperbolic-secant pulse; numerical checks of mode purity | The pulse has the shape correspondence derived below. |
| Section II C, final paragraph | Dipole-interaction omission, Raman suppression, and a well-defined cavity output channel | This specifies the source idealization. |

The percentages in this table are reported by the article's prose and captions. They refer to occupations or mode purity, not to successful all-photon capture events. The numerical discussion and large-$`N`$ formula in Section III B concern initially fully inverted ensembles, whereas our critical code has vanishing maximal excitation fraction.

## 4. Why high mode purity is relevant but not sufficient

On a fixed $`m`$-photon sector define

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

Thus exact rank-one correlation, $`p_f=1`$, really does imply support on one field mode. At fixed finite $`m`$, occupation tending to one also forces full-mode fidelity to one. The nonuniformity appears when $`m`$ grows: $`p_f\to1`$ alone does not imply $`m(1-p_f)\to0`$.

For the normalized natural occupations $`p_j=\lambda_j/m`$, $`\mathcal P_F=\sum_jp_j^2`$ satisfies $`p_1^2\leq\mathcal P_F\leq p_1`$. The leading mode consequently has

```math
F_{f_1}\geq\max\{0,1-m(1-\mathcal P_F)\}.
```

This translates a sufficiently accurate occupation bound into state fidelity. A uniform common-code bound additionally controls the photon-number dependence and uses one shared waveform.

As a purely mathematical control, for orthogonal modes $`f,g`$ and $`m\geq3`$, the two pure states

```math
|m-1,1\rangle_{f,g},\qquad
\sqrt{1-1/m}|m,0\rangle_{f,g}+m^{-1/2}|0,m\rangle_{f,g}
```

have identical one-photon correlation operators and mode purities. Their probabilities of all photons lying in $`f`$ are respectively zero and $`1-1/m`$. This general field-state example shows why a first-order correlation kernel alone cannot determine the multiphoton objective.

There is a useful exception: for a pure two-photon field the symmetric Schmidt (Takagi) decomposition makes the maximum product-mode Fock overlap equal to the largest normalized natural occupation. This equality applies to the two-photon sector; the growing-code problem also requires a common waveform across sectors.

## 5. The half-excited result is compatible, and its pulse is an exact shape correspondence

Section III C uses the semiclassical approximation for an initially half-excited system and obtains $`v_1(t)\propto\mathrm{sech}(N\gamma_{\rm LL}t)`$. The source explicitly marks Eq. (29) as approximate and reports finite numerical purities, not an exact finite-$`N`$ full-field identity.

For our comparison pulse family, direct substitution gives

```math
f_{1/2}(\tau)=\frac{1}{\sqrt{2}}\mathrm{sech}(\tau/2).
```

Using the rate conversion above, this is the same normalized shape on the positive time axis. For $`m=N/2`$, the repository parameter $`a_m=(m-1)/N`$ tends to $`1/2`$, but is not exactly $`1/2`$ at finite $`N`$.

This algebraic shape correspondence has a precise domain: our controlled product-state approximation is for $`m=o(N)`$ and must not be extended to $`m=N/2`$ just because its trial pulse has the correct semiclassical limit. The article studies one half-excited preparation with its own optimal mode, not a receiver committed to one mode for every unknown number component.

## 6. Relation to the uniform theorem

Law–Lee optimizes the occupation quantities in Eqs. (13) and (18) and analyzes the selected preparations in Section III through Eqs. (27) and (29). The theorem here establishes a uniform norm approximation of the emitted isometry over a growing number code, optimizes canonical worst-input fidelity over every common waveform, and gives a matching constructive/converse critical law.

The resulting **sharp optimized boundary between canonical state transfer and mean-photon collection** occurs on the $`N^{2/3}`$ scale for the specified collective source and one linear memory. The cascade model, oscillator comparator, dominant two-mode occupation and semiclassical pulse are inherited ingredients, as detailed above.

The [canonical proof](../research/THEOREM.md) gives the finite inequalities and quantifiers for the uniform result; the [assumption register](ASSUMPTIONS.md) states its preparation and realization scope.
