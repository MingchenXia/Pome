# Guillemin entropy scaling, Hermitian completion energy, and compactness of nets

**Date:** 2026-11-21. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.
**Classification:** mathematical audit; no production patch or independent transitive theorem certification.

## Precise integrated reading scope

The actual current 25-chapter / 747-section table of contents and the existing coverage matrix were consulted before choosing these four sections. These are **four entire direct mathematical section readings**, not claims of first-ever visits or of the validity of all their cited prerequisites:

| Current section | Exact integrated file on reviewed main | Blob SHA | Mathematical physical lines | Stable source / permanent labels checked |
| --- | --- | --- | --- | --- |
| §2.7, Nets and compactness | `docs/sections/measures-and-distributions--nets-and-compactness/index.html` | `7e4a226a48f88a97b3db1a8dd7d8582c909aeea1` | 5–91 | Prop. 2.7.1 `CE53601F` / `4603E36ECC71`; Lemma 2.7.2 `E265537C` / `8734A1486521`; Theorem 2.7.3 `5470287F` / `DF30CEF15D17`; Prop. 2.7.4 `C7F49DCE` / `2963E35FB0D3` |
| §11.2, Monge–Ampère energy and torsion | `docs/sections/monge-ampere-energy-and-torsion/index.html` | `fe1ca06167b8f5bc9868e9a9876397afad4e7ff5` | 5–419 | Lemma 11.2.2 `37DA4A81` / `8A9C3139B5B5`; Thm. 11.2.4 `788EACD6` / `7D069B347672`; Prop. 11.2.17 `F8C97F67` / `AE6CE389C569`; Thm. 11.2.19 `69225BEF` / `04BD04D6C676` |
| §19.10, Section growth of semipositive line bundles | `docs/sections/section-growth-of-semipositive-line-bundles/index.html` | `41526a319c45c861a8303776f155096d1f36614a` | 5–22 | Cor. 19.10.1 `4B096A2D` / `F31884F26A29`; equation 19.10.2 `15584614` / `2B3916324C79` |
| §21.10, The Guillemin reference metric | `docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html` | `4458eef6df84ef46d601d39506017387ed292e08` | 5–92 | Thm. 21.10.1 `E94A20D6` / `B471B994CE64`; Step 2 lines 37–66, Step 4 lines 75–88 |

The sections' cited results were not counted as fresh full-section reviews. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale, and positivity-loss completion programmes are **deferred-by-user** and were neither inspected nor certified.

## New finding: POME-GUILLEMIN-ENTROPY-FACET-SCALING-RIGIDITY-001

**Severity:** low. **Status:** verified conditional deduction; **not** a claim of error in Theorem 21.10.1.
**Anchor:** §21.10, Theorem 21.10.1, Step 2 lines 37–66 and Step 4 lines 75–88, source/permanent labels `E94A20D6` / `B471B994CE64`.

**Hypotheses.** Let (P\subset M_{\mathbb R}) be a full-dimensional smooth (Delzant) lattice polytope with nonempty boundary, with the same primitive facet functions (\ell_\rho\) and vertex charts as §21.10. For a scalar (a>0), put
\[
G_a(m)=a\sum_\rho\ell_\rho(m)\log\ell_\rho(m)
\quad(m\in P),\qquad G_a=+\infty\ (m\notin P),
\]
and (F_a=G_a^*\). On the dense torus, use the *fixed* line bundle (L=L_P\) and its same vertex frames to define
\[
H_{v,a}(z)=F_a(\operatorname{Trop}z)-\log|\chi^v(z)|^2 .
\]
Note that changing (a\) does **not** change the recession/support function (h_P\) or the line bundle/frame convention.

**Deduction.** The weights (H_{v,a}\) extend to continuous (T_c\)-invariant Hermitian metrics on (L\) for every (a>0\). They are smooth in all the toric vertex charts **if and only if**
\[
\boxed{\quad 1/a\in\mathbb Z_{>0}.\quad}
\]
Among these smooth metrics, their curvature is positive definite everywhere on (X_P\) **if and only if (a=1\)**, the coefficient in printed Theorem 21.10.1. For (a=1/p\), (p\geq2\) an integer, the curvature is smooth semipositive, strictly positive on the dense torus but degenerate in the normal direction along every toric boundary divisor. For (1/a\notin\mathbb Z_{>0}\), the weights are not (C^\infty\) across a generic toric divisor. This is the sharp facet-entropy coefficient rigidity of the *given* toric line-bundle charts; no rescaling of frames or lattice is allowed.

**Complete local proof.** For a vertex (v\), let (t_i=\ell_i(m)\) and (w_i=\chi^{e_i}(z)\), so (x_i=\log|w_i|^2\). At a boundary point with vanishing-coordinate set (I\), write
\[
G_0(t)=\sum_{i\in I}t_i\log t_i+g(t)
\]
near the unique constrained minimizer (q\) on the corresponding face; the other facet functions are strictly positive there, and (g\) is smooth. The original Step 2 verifies positivity of the relevant (J\times J\) Hessian block. Since (F_a(x)=aF_0(x/a)\), the stationarity equations become
\[
x_i/a=\log t_i+1+g_i(t)\ (i\in I),\qquad
x_j/a=g_j(t)\ (j\in J).
\]
Set (r_i=\exp(x_i/a)=|w_i|^{2/a}\). The implicit system
\[
r_i=t_i\exp(1+g_i(t)),\qquad x_j/a=g_j(t)
\]
has the **same invertible block Jacobian** as the system of Step 2: a positive diagonal (I\times I\) block and the positive definite (J\times J\) block (g_{jk}(q)\). Thus (t\) and the logarithms-cancelled expression for (H_{v,a}\) are smooth functions of ((r_I,x_J/a)\), including at (r_I=0\). This yields continuous weights for all (a>0\) and smooth weights whenever (1/a=p\in\mathbb Z_{>0}\), as (r_i=(w_i\bar w_i)^p\) is then smooth. Compatibility of the weights on chart overlaps follows from the unchanged character-frame transition law (Step 5 of the printed proof).

To prove the converse and the curvature assertion, take a point in the open part of one boundary divisor, so (I=\{i\}\), with nonzero tangential (w_J\). Differentiating the Legendre expression in the scalar variable (r_i\) gives
\[
\frac{\partial H_{v,a}}{\partial r_i}
=\frac{\partial H_{v,a}}{\partial x_i}\frac{\partial x_i}{\partial r_i}
=t_i\frac a{r_i}
=a\exp(-1-g_i(t)).
\]
At the boundary this has the **strictly positive** value (A(w_J)=a\exp(-1-g_i(q))\). Therefore, along a transverse complex coordinate (w_i\),
\[
\boxed{\quad
H_{v,a}(w_i,w_J)
=H_{v,a}(0,w_J)+A(w_J)|w_i|^{2/a}
+O(|w_i|^{4/a}),\qquad A(w_J)>0 .
\quad}
\]
More precisely, the weight is a smooth real function of (r_i=|w_i|^{2/a}\) with a nonzero first derivative at (r_i=0\). Such a radial composition is smooth at the origin only when (1/a\) is a positive integer: if (p=1/a\notin\mathbb Z_{>0}\), the leading (|w_i|^{2p}\) term has a nonintegral even radial order and cannot be (C^\infty\); the smooth one-variable change of variables with nonzero derivative rules out cancellation by higher orders. If (p\geq2\), (\partial_{w_i}\partial_{\bar w_i}H_{v,a}\) and its mixed normal blocks vanish at the divisor; positive definiteness fails there. If (p=1\), the printed Step 4 proves positive definiteness on all charts. Conversely, when (p\geq2\), the Hessian is positive definite on the dense torus (Legendre strict convexity) and extends smoothly; hence it is semipositive by continuity.

**Independent explicit check on (\mathbb P^1\).** Take (P=[0,1]\) and (G_a(t)=a[t\log t+(1-t)\log(1-t)]\). Direct Legendre calculation gives
\[
F_a(x)=a\log(1+e^{x/a}),\qquad
H_{0,a}(w)=a\log(1+|w|^{2/a}) .
\]
The opposite chart has the same expression in (w^{-1}\). This displays the complete smoothness/curvature trichotomy without any abstract toric lemma.

**Proposed action and dependents.** Keep Theorem 21.10.1 unchanged. If scalar-multiple entropy references are later used, state the coefficient-rigidity qualification in §21.10 or a separate addendum. The potential affected dependents are toric boundary metric constructions in §§21.8–21.14; none is declared incorrect, and the original (a=1\) theorem remains valid. No mathematical body or permanent tag was edited.

## Other direct checks

### §2.7 (physical lines 5–91)

- The introductory binary-digit sequence on the nonmetrizable compact product already supplies a **nonsequential** compactness example; it was not rediscovered as a new finding.
- Proposition 2.7.1's directed triples ((i,U,k)\), increasing/final map to the original index set, and convergent Willard subnet were checked in both directions, including the open-cover counter-net.
- Lemma 2.7.2 uses ultrafilter/Zorn choice explicitly, including the projection ultrafilters and finite-coordinate cylinder neighborhoods.
- Theorem 2.7.3 bounds each real compactly supported test against some (M_r\) and identifies the image by positivity, linearity, and closed coordinate inequalities. This relies on the earlier Radon representation Theorem 2.3.3: its full proof was **not** re-audited.
- Proposition 2.7.4 establishes total boundedness of equicontinuous pointwise-bounded families and compactness in the complete uniform metric. The compact-metric sequence conclusion is not extrapolated to the uncountable product in §2.7's introduction.

No newly confirmed printed error, duplicate, or missing hypothesis was identified in these steps.

### §11.2 (physical lines 5–419)

- Lemma 11.2.2's symmetry criterion correctly requires (mathrm d\Omega=0\), not just (mathrm{dd}^c\Omega=0\). Its first-jet test annihilates (ar\partial\Omega\); Lemma 11.2.3 polarizes positive ((1,1)\)-forms before applying nondegeneracy. Hence Theorem 11.2.4 tests the one-form on an **open set** of potentials, not a single Gauduchon potential.
- Proposition 11.2.8 telescopes the mixed-energy variation only when the background is closed. Proposition 11.2.10's (nt\) integral correctly measures the torsion defect; the surface specialization 11.2.12 preserves the two first-order torsion terms even for Gauduchon (omega\).
- For Hermitian-symplectic fourfolds, the canonical completion is the orthogonal minimizer in a finite-dimensional affine space; the completion is unchanged by (dd^c\)-potential variation because the norm difference is independent of the completion. The expansion
  (int\Theta_\zeta^4/4!=V(\omega)+\tfrac12\int\zeta\wedge\bar\zeta\wedge\omega^2+\tfrac14\int\zeta^2\wedge\bar\zeta^2\)
  has the correct multinomial coefficients.
- Theorem 11.2.19's potential Hessian is
  \[
  H_\omega(dd^c\varphi,dd^c\varphi)
  =\tfrac12\int_X dd^c(\omega^2)\wedge d\varphi\wedge d^c\varphi.
  \]
  Its infinite positive/negative index conclusion requires a **nonzero** (dd^c(\omega^2)\) and the Stokes/tracial sign argument; the disjoint-bump high-frequency directions establish arbitrarily high finite indices, not a claim about diagonalization of an infinite-dimensional operator.
- As a check on all coefficients, the exact potential-line identity implicit in 11.2.17–11.2.20 is
  \[
  F(\omega+dd^c\varphi)-F(\omega)=
  -\frac16\int_X\varphi\,dd^c(\omega^3)
  +\frac14\int_Xdd^c(\omega^2)\wedge d\varphi\wedge d^c\varphi,
  \]
  whenever the endpoint is positive. It follows from the *exactly quadratic* potential-line restriction, its first derivative in 11.2.17, and its Hessian in 11.2.20; it is an internal consistency check, **not** an additional proof-chain certificate or independent novel finding.
- The explicit two-torus product computations of 11.2.23–24 were checked against the top-degree factorization (alpha_s^2/2=(1-s^2)\mu_0\) and (ho_s\wedge\bar\rho_s=s^2\mu_0\). Both examples remain conditional on the stated integration/holomorphic form facts, not re-certified from first principles.

### §19.10 (physical lines 5–22)

Corollary 19.10.1's asymptotic is correctly obtained from the weak (q=0\) and strong (q=1\) holomorphic Morse inequalities when (i\Theta_L\geq0\); the (n=1\) endpoint is handled by the Euler equality. The strict-at-one-point assumption supplies positive integral because curvature semipositivity holds everywhere. The **upstream holomorphic Morse inequalities are recorded as dependencies only**; no excluded approximation/L²/Bergman proof-completion chain was reopened. Source attribution is retained. No new printed error was confirmed.

## Status / verification boundaries

**New:** one low-severity *verified conditional deduction* `POME-GUILLEMIN-ENTROPY-FACET-SCALING-RIGIDITY-001`; **confirmed false printed theorems:** zero; **new confirmed proof-only errors:** zero; **new complete transitive proof-chain certifications:** zero.

**Open dependencies:** §2.7's Radon representation input; §11.2's Stokes/product, smooth Aeppli variation, and bounded-potential total mass inputs; §19.10's weak and strong holomorphic Morse inputs; §21.10's earlier Delzant toric charts and divisor/line-bundle transition constructions. These are not classified as false or resolved. Hironaka remains the permitted external resolution input; the user-excluded programmes remain **deferred-by-user**, never verified.

No tests, builds, Python/JS checks, CI, publication, main-branch edit, source-registry edit, permanent-tag edit, merge, or website changes were performed. This file documents a mathematical reading/reasoning audit only.
