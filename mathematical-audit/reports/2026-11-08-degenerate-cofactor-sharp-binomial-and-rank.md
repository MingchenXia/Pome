# Sharp polarized cofactor comparison and its rank strata in degenerate Monge–Ampère equations

**Finding:** `POME-DEGEN-COFACTOR-SHARP-RANK-001`.  
**Classification:** **low / verified conditional deduction**. No printed statement or proof is asserted false.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Scope:** independent pointwise Hermitian linear algebra attached to the actual integrated §§14.21–14.22, followed by a smooth *local* model. No general PDE uniqueness certification.

## Exact integrated sources, tags, and anchors

1. `docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html`, main blob `044f55457f10b2f640052854a7f5f14b8403be82`: Theorem **14.21.3** (`non-kahler-pluripotential-theory:61B8DD0F`, permanent `6EB399397505`), physical lines 27–50, proof context lines 131–170; the real cofactor form **(14.21.7)** (permanent `57588F1C3107`), lines 108–115; the printed comparison **(14.21.8)** (`non-kahler-pluripotential-theory:BDBE4297`, permanent `144125DEDD1C`), lines 115–120; the cofactor eigenvalue formula **(14.21.9)** (`non-kahler-pluripotential-theory:A73BA233`, permanent `CEEE110C45FE`), lines 121–129.
2. `docs/sections/uniqueness-for-degenerate-equations--polarized-cofactors-and-propagation/index.html`, main blob `56645140ee2a5e1f97f3288e31ad9a48161e73e5`: Theorem **14.22.1** (`non-kahler-pluripotential-theory:DC121A4C`, permanent `919310C73DBE`), physical lines 13–31; the Hermitian cofactor and real-symbol formulas **(14.22.9–10)** (`non-kahler-pluripotential-theory:500F61C6` / permanent `04DC9E828E52`, and `non-kahler-pluripotential-theory:9A3B77CC` / permanent `7A7369E544A8`), lines 79–107; exterior-ball flow/orbit proof, lines 108–154, consulted to check the precise implication only.

The user-excluded Demailly approximation/regularization and dedicated Bergman, weighted-$L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes were not opened. Earlier notes about these subjects remain **deferred-by-user**, not certified.

## The sharp coefficient

Let $n\ge2$, $A,B$ be *arbitrary semipositive real $(1,1)$-forms on a Hermitian complex vector space of dimension $n$*, set $H=A+B$ and use precisely the unnormalized polarized cofactor of (14.20.1) and (14.21.8):
$$
T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}.
$$
Define
$$
M_n=\binom{n-1}{\lfloor(n-1)/2\rfloor}.
$$
Then in the strong-positive $(n-1,n-1)$ cone,
$$
\boxed{M_n^{-1}H^{n-1}\ \le\ T\ \le\ H^{n-1}.}\tag{1}
$$
Both coefficients are optimal **even under the equal-Monge–Ampère-density restriction $A^n=B^n$** (both sides may then vanish). When $n=2$, $T=H$ exactly. This sharp bound is stronger than the *valid but nonoptimal* $2^{-(n-1)}H^{n-1}\le T$ printed in (14.21.8).

**Proof.** The binomial formula and positivity of all mixed products yield
$$
H^{n-1}=\sum_{j=0}^{n-1}\binom{n-1}{j}A^j\wedge B^{n-1-j}.
$$
For every $j$, $1\le\binom{n-1}{j}\le M_n$. Subtracting $T$ from $H^{n-1}$, or subtracting $H^{n-1}$ from $M_nT$, gives sums of strongly positive forms with nonnegative coefficients. This proves (1) without any limiting argument or determinant assumptions.

For optimality of the lower coefficient, let $r=\lfloor(n-1)/2\rfloor$, work in $\mathbb C^n$, and define
$$
A=\mathrm i\sum_{j=1}^{r}dz_j\wedge d\bar z_j,\qquad
B=\mathrm i\sum_{j=r+1}^{n-1}dz_j\wedge d\bar z_j.
$$
(Empty sums are allowed.) Thus $H$ has rank $n-1$ and nonzero $(n-1)$-st power. Every mixed $(n-1)$-fold wedge vanishes except $A^r\wedge B^{n-1-r}$, so
$$
H^{n-1}=M_n A^r\wedge B^{n-1-r},\qquad
T=A^r\wedge B^{n-1-r}.
$$
In particular $T=M_n^{-1}H^{n-1}\ne0$. Both $A^n$ and $B^n$ are zero. For the upper coefficient, take $A=0$ and any $B$ of rank $n-1$; then $T=H^{n-1}\ne0$ and again $A^n=B^n=0$. No strictly positive definite example is claimed to realize the lower equality: these are necessarily degenerate extremal models.

## Exact rank strata of the cofactor symbol

Let $Q_T$ be the quadratic form in (14.21.7), with $Q_T(\xi)dV=\mathrm i\xi^{1,0}\wedge\overline{\xi^{1,0}}\wedge T$, and let $a$ be its real coordinate symbol in (14.22.10). Since (1) compares their positive semidefinite Hermitian matrices, it gives the **same kernel** for $Q_T$ and $Q_{H^{n-1}}$, and hence the same ranges and ranks. Write $r_H=\operatorname{rank}_{\mathbb C}H$ at the point. In a unitary coframe diagonalizing $H$ with eigenvalues $\lambda_1,\ldots,\lambda_n\ge0$, (14.21.9) identifies the cofactor eigenvalues, up to a *common strictly positive normalization constant*, as
$$
\mu_k=\prod_{\ell\ne k}\lambda_\ell.
$$
Consequently, for $n\ge2$ there are **exactly three possibilities**:
$$
\begin{array}{c|c|c|c}
r_H& \operatorname{rank}_{\mathbb C}Q_T&
\operatorname{rank}_{\mathbb R}a&
\operatorname{im}Q_T^{\sharp}\\\hline
0\le r_H\le n-2&0&0&\{0\}\\
r_H=n-1&1&2&\text{the complex null line of }H\\
r_H=n&n&2n&TX
\end{array}\tag{2}
$$
The middle row follows because the only nonzero $(n-1)$-fold product omits the **single zero eigenvalue**, so the symbol sees derivatives in precisely that *null* complex direction, not in the positive directions. The last row is uniformly elliptic locally exactly where $H$ has a local positive essential lower bound, as stated in the reading edition; (2) by itself does **not** establish any global reachability.

On the positive-definite stratum, (1) sharpens the comparison of $Q_T$ with $Q_{H^{n-1}}$:
$$
M_n^{-1}Q_{H^{n-1}}\le Q_T\le Q_{H^{n-1}}.
$$
The pointwise condition number satisfies
$$
M_n^{-1}\operatorname{cond}(H)\le\operatorname{cond}(Q_T)
\le M_n\operatorname{cond}(H)
$$
where $\operatorname{cond}$ is the ratio of the largest to smallest eigenvalue relative to the same auxiliary Hermitian metric. Indeed the reciprocal-product cofactor eigenvalues of $H^{n-1}$ have ratio $\max_k\lambda_k/\min_k\lambda_k=\operatorname{cond}(H)$, and the two quadratic-form comparisons pass to largest and smallest eigenvalues. The realification in (14.22.10) doubles complex ranks and eigenvalue multiplicities but leaves the ratio unchanged. For the family $A=B=H_\varepsilon/2$, $H_\varepsilon=\operatorname{diag}(1,\dots,1,\varepsilon)$, $0<\varepsilon<1$, one has $T=(n/2^{n-1})H_\varepsilon^{n-1}$, so
$$
\operatorname{cond}(a_\varepsilon)=\varepsilon^{-1}.
$$
Thus no epsilon-independent ellipticity follows as the smallest Hessian eigenvalue vanishes. **For $n=1$**, $T=1$ and the real symbol is positive regardless of $H$, as the printed text already notes; (2) is explicitly restricted to $n\ge2$.

## Local smooth PDE compatibility check; not a global counterexample

Take a ball in $\mathbb C^n$ with flat $\omega=dd^c\sum_{j=1}^n|z_j|^2$ and set
$$
u=-|z_n|^2,\qquad v=\sum_{j=1}^{n-1}|z_j|^2-|z_n|^2.
$$
These are smooth $\omega$-psh potentials, with
$$
A=\omega+dd^c u=dd^c\sum_{j<n}|z_j|^2,
\qquad
B=\omega+dd^c v=2A,\qquad
A^n=B^n=0.
$$
The difference $w=u-v=-\sum_{j<n}|z_j|^2$ is **nonconstant**, while $Q_T$ has range the $z_n$-plane and its integral curves keep the first $n-1$ coordinates fixed. Hence the control orbits are not dense, exactly as the hypotheses of Theorem 14.22.1 require. This example is **local and noncompact** and is **not** a counterexample to any printed compact-manifold uniqueness theorem. It distinguishes vanishing determinant, rank-$n-1$ cofactor and full ellipticity without an illicit maximum-principle application.

## Disposition, dependents, and verification boundary

- **Class:** low / verified conditional deduction. Neither (14.21.8), (14.21.9), Theorem 14.21.3 nor Theorem 14.22.1 is false by this calculation. The old constant is **valid but nonsharp**, not an error or a proof gap.
- **Proposed non-production amendment:** optionally replace the lower coefficient $2^{-(n-1)}$ in (14.21.8) by $M_n^{-1}$, appending (2) as a quantitative remark, with its degenerate/equal-density equality models. Keep the existing theorems, proofs, historical attribution, source labels and permanent tags.
- **Affected dependents:** the ellipticity comparison in the proof of Theorem 14.21.3, and the real-symbol/range/orbit interpretation of Theorem 14.22.1. These implications gain a sharper constant or rank description but **do not** gain the global reachability or PDE regularity hypotheses necessary for full uniqueness. Remaining complex Hessian / stochastic compactness / strong maximum-principle dependencies are not recertified.
- **Actual checks:** manual wedge-binomial coefficients, explicit rank-$n-1$ diagonal extremizers, eigenvalue products, symbol realification, and a local flat-potential model; direct reading-edition statements and specified proof passages. **No software tests, project build, CI, formalization, or site publication** were performed. No source/body/registry/permanent-tag/canonicalization modification.

**Coverage accounting:** §§14.21 and 14.22 were already partially reviewed before this run. Here **0 first visits** and **0 complete mathematical-section certifications**; the unchanged main table of contents has **25 chapters and 747 numbered sections**. Existing confirmed errors, proof gaps, genuinely external inputs and user-deferred records keep their previous statuses.
