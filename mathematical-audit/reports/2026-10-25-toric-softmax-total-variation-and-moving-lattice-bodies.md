# 2026-10-25 — Toric softmax: narrow but not total-variation convergence; moving convex-body lattice sums

**Status:** mathematical-audit note only, on review/mathematical-audit. **Pinned main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Checkpoint:** 2026-10-24T20:00:00Z. No mathematical-source, registry, permanent-tag, website, CI, or main change is proposed as an accepted repair. Neither finding below alleges a false printed theorem.

## POME-TORIC-SOFTMAX-TV-001 — low; verified conditional deduction

**Integrated source:** docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html, blob 7089aa41ae2422b1bd6b5094e46668cbc8ed37be, lines 11–39, 44–94, 99–158. Theorem 21.5.1: source label foundations-of-pluripotential-theory-4A0FAEB3, permanent tag 409656CC47D4; Theorem 21.5.2: foundations-of-pluripotential-theory-6403CF44, tag F4072D9ED060; Proposition 21.5.4: foundations-of-pluripotential-theory-EAD83A50, tag 5D8A7A7D734E. The §21.1 coordinate, lattice and volume conventions at docs/sections/convex-analysis-and-toric-potentials/index.html:7–18, blob e875ab348461c739ae3799c6906f8f13b9050ba7, are used. This is a topological sharpness result, not a correction of Theorem 21.5.2 or a replacement of its proof.

Fix n >= 1, take the standard lattices in R^n and the standard simplex
\[
P=\{(p_1,\dots,p_n):p_i\geq0,\ \sum_{i=1}^n p_i\leq1\},
\qquad n!\operatorname{vol}(P)=1.
\]
For t>0 define the globally smooth, strictly convex function
\[
F_t(x)=t\log\bigl(1+\sum_{i=1}^n e^{x_i/t}\bigr).
\]
Then
\[
0\leq F_t(x)-h_P(x)\leq t\log(n+1),
\qquad h_P(x)=\max(0,x_1,\dots,x_n),
\]
uniformly on all of R^n. Both F_t and h_P have exactly the slope body P and are full-mass relative to P. Nevertheless,
\[
\operatorname{MA}_{\mathbb R}(F_t)\ \Longrightarrow\ \delta_0
=\operatorname{MA}_{\mathbb R}(h_P)
\]
narrowly, while for every t>0
\[
\bigl|\operatorname{MA}_{\mathbb R}(F_t)-\delta_0\bigr|(\mathbb R^n)=2.
\]
Here |signed measure| denotes total variation; the probability-theory distance \(\sup_A|\mu(A)-\nu(A)|\) is 1.

**Complete calculation.** Put \(Z=1+\sum_j e^{x_j/t}\), \(p_i=e^{x_i/t}/Z\) and \(p_0=1/Z=1-\sum_i p_i\). We have
\[
\nabla F_t=(p_1,\ldots,p_n),\quad
D^2F_t=t^{-1}(\operatorname{diag}(p)-pp^{\mathsf T}),\quad
\det D^2F_t=t^{-n}p_0\prod_{i=1}^n p_i,
\]
the determinant identity following from the matrix determinant lemma (and remaining valid for n=1). Each p_i and p_0 is strictly positive, so the Hessian is positive definite: for v nonzero,
\[
v^{\mathsf T}(\operatorname{diag}(p)-pp^{\mathsf T})v
=\sum_i p_i v_i^2-(\sum_i p_i v_i)^2
\geq p_0\sum_i p_i v_i^2>0.
\]
The gradient is a diffeomorphism from R^n to the interior of P, with inverse
\[
x_i=t\log(p_i/p_0).
\]
Thus Proposition 21.5.4 and change of variables give the exact smooth probability density
\[
d\mu_t(x)=n!t^{-n}p_0\prod_i p_i\,dx,
\quad \mu_t(\mathbb R^n)=n!\operatorname{vol}(P)=1.
\]
Equivalently, its Legendre dual is \(F_t^*(p)=t\sum_{i=0}^n p_i\log p_i\) on P (with \(0\log0=0\)), infinite off P, and Theorem 21.5.1 yields
\[
\int f\,d\mu_t=n!\int_{P^\circ}
 f\!\left(t\log(p_1/p_0),\ldots,t\log(p_n/p_0)\right)\,dp.
\]
For any bounded continuous f, dominated convergence on the finite-volume simplex gives the narrow limit f(0). The support function h_P has \(\partial h_P(0)=P\), while for x != 0 its subgradients lie in proper exposed faces of P, of n-volume zero; hence Theorem 21.5.1 gives \(\operatorname{MA}_{\mathbb R}(h_P)=n!\operatorname{vol}(P)\delta_0=\delta_0\). The smooth \(\mu_t\) has no atom at 0, so \(\mu_t\) and \(\delta_0\) are mutually singular, proving the asserted exact variation norm 2.

**Proposed disposition:** optional adjacent example after Example 21.5.3, explicitly distinguishing vague, narrow and total-variation convergence. Preserve the printed theorems and their tags. This also constrains any strengthening of §21.6.2 or the mixed-measure continuity assertion of §21.5.4: equal full mass and globally uniform convergence do not imply variation convergence. No Demailly/Bergman/L2/extension/positivity-loss approximation result is involved; the displayed family is simply an explicit elementary toric function.

## POME-LATTICE-MOVING-BODY-001 — low; verified conditional deduction

**Integrated source:** docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html, blob 5d209b7f4d2156c19bc3fb300303405df6321230, lines 10–54 and 58–90; Proposition 21.7.2, source foundations-of-pluripotential-theory-5E9AEE47, tag EDD78BC61BD7, and Theorem 21.7.3, source foundations-of-pluripotential-theory-364BCD30, tag 831AEEB7084F.

Let n >= 1. Suppose nonempty compact convex bodies K_k in the normalized lattice space M_R converge in Hausdorff distance to a nonempty compact convex body K (allowing empty interiors). Let \(a_k\in M_{\mathbb R}\) be arbitrary translations, \(r_k\geq0\), \(r_k/k\to0\). Then for every continuous \(f:M_{\mathbb R}\to\mathbb R\),
\[
\boxed{\lim_{k\to\infty} k^{-n}
 \sum_{m\in(kK_k)^{r_k}\cap(M+a_k)}f(m/k)
=\int_K f(p)\,dp.}
\]
The convergence is uniform over *all* choices of translations. This extends Theorem 21.7.3 from a fixed K to moving bodies K_k. It includes bodies with empty interior; for n=0 everything is the single point and the assertion is immediate.

**Complete proof.** Put \(\delta_k=d_H(K_k,K)\to0\), \(c=\sqrt n\), and use the half-open lattice cells \(m/k+k^{-1}[0,1)^n\). Let U_k be the union of cells with anchors \(m/k\in (K_k)^{r_k/k}\). The Hausdorff support-function identity in Proposition 21.7.2 implies
\[
K_{\delta_k}\subset K_k\subset K^{\delta_k}.
\]
Indeed for \(x\in K_{\delta_k}\), for every unit normal v,
\(\langle x,v\rangle+\delta_k\le h_K(v)\le h_{K_k}(v)+\delta_k\); separation yields \(x\in K_k\). A selected cell lies within c/k of its anchor, giving the uniform sandwich
\[
\boxed{K_{\delta_k+c/k}\subset U_k
\subset K^{\delta_k+(r_k+c)/k}.}
\]
The first inclusion is valid even when the inner set is empty: any point x therein has its cell anchor within c/k, so that anchor lies in \(K_{\delta_k}\subset K_k\). The right-hand inclusion follows by the triangle inequality.

The inner and outer radii tend to zero. By continuity of convex-body volume under inner and outer parallel sets (§21.7.2), \(\operatorname{vol}(U_k\triangle K)\to0\), uniformly in translations. For all sufficiently large k the cells lie in the fixed compact K^1. If \(\omega_f\) is a modulus of continuity of f on K^1, the cellwise Riemann-sum error is at most \(\omega_f(c/k)\operatorname{vol}(U_k)\to0\). Also
\[
\left|\int_{U_k}f-\int_K f\right|
\leq \|f\|_{C(K^1)}\operatorname{vol}(U_k\triangle K)\to0.
\]
These bounds prove the assertion. For K of empty interior the inner sets are empty but the shrinking outer volumes tend to zero, so no full-dimensionality hypothesis has been smuggled in.

**Proposed disposition:** optional corollary following Theorem 21.7.3, useful for varying Okounkov polytopes and toric section counts only when the stated Hausdorff convergence has independently been established. It neither proves an arbitrary Okounkov-body convergence theorem nor repairs or certifies §19.7 semigroup-counting inputs.

## Actual scope, ledger and exclusions

Read current main AGENTS.md and documentation/proof-expansions.md; review-branch README.md, previous LATEST.md, LEDGER.md, SECTION_MATRIX.md and pinned current main. Confirmed from integrated reading HTML the §21.1 conventions, every displayed proof step of §§21.5.1–4 and 21.7.2–4, and the §17.11 introductory dependency map (docs/sections/test-curves/index.html:5–20, blob 0ece4d0eccf9c5e35e7ae6c4bc55335897e74e80, tag BA6AA7598BE3). §17.11 and §21.1 are *orientation/conventions only*, with no claimed theorem-level verification; §§21.5 and 21.7 receive additional exact model tests, not whole-section or transitive certification. §19.9 was used only to locate existing semigroup-counting dependencies; pre-existing POME-OKO-COUNT-INTERNAL-001 is not re-entered as a new discovery.

Historical approximation/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss issues remain **deferred-by-user**, not reopened, certified, or resolved. No build, CI, website publication, formal verification, or broad code test is claimed. A separate pure-standard-library arithmetic sanity check for the softmax covariance determinant and moving 1D lattice grid ran locally; that check is not a mathematical proof.
