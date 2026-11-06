# Mathematical audit — 2026-11-06 — Kähler variance identity and duplicated second-variation display

**Production main reviewed:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.  
**Scope:** First selected substantive examination of current ToC §14.8, with targeted §14.1, §14.2.3, and §14.4.1 dependencies. All Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work remains **deferred-by-user** and was not examined.

## Pinning and statement identity

- Integrated continuous reading edition: <code>docs/sections/smooth-monge-ampere-equations--variation-of-the-normalization-scalar/index.html</code>, main blob <code>34526fcac6d5f30e71a98cadc88a4c76817546c4</code>, physical lines **10–19** (data and statement), **24–48** (proof), **53–68** (Corollary 14.8.4), and **70** (separate duplicate).
- Section §14.8 source <code>non-kahler-pluripotential-theory:BFC48217</code>, permanent <code>9541740AAFDC</code>. Theorem 14.8.1 source <code>non-kahler-pluripotential-theory:C70BE558</code>, permanent <code>C611B2CA264A</code>. Its combined formula source <code>non-kahler-pluripotential-theory:4CC64AAD</code>, permanent <code>11F81D837A44</code>. The separate displayed equation source <code>non-kahler-pluripotential-theory:3CBF8D7E</code>, permanent <code>578022E3660A</code>. Corollary 14.8.4 source <code>non-kahler-pluripotential-theory:E5122287</code>, permanent <code>B9C312CB7069</code>.
- Equation 14.1.1: <code>docs/sections/smooth-monge-ampere-equations/index.html</code>, blob <code>e35eb98bdc1c62c4938155964945f4d6495b4ee4</code>, source <code>non-kahler-pluripotential-theory:2BED92DC</code>, permanent <code>C5FA7F078BB6</code>, physical lines **6–17** (equation and Hermitian background). Kähler mass formula 14.2.3: <code>docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html</code>, blob <code>3f96829e18befc845df40c6d4bca13c977ae9cea</code>, lines **33–46**. The parameter-smoothness input Proposition 14.4.1: <code>docs/sections/smooth-monge-ampere-equations--the-linearized-equation-and-smooth-dependence/index.html</code>, blob <code>2f9ebecbd5bd079eb8573b4bb97df0fb5ab1bdfb</code>, lines **20–39**.

## POME-MA-KAHLER-NORMALIZATION-VARIANCE-001

**Status:** verified conditional deduction. **Severity:** low (an exact strengthening and a sharp quantitative bound, **not** a false statement or completed repair of Theorem 14.8.1).

**Assumptions:** X is a connected compact Kähler manifold of complex dimension n≥1, the fixed Hermitian background ω is **closed**, dV is a smooth positive volume form, F and G are smooth real-valued, and the smooth positive solutions of (14.1.1) along F_t=F+tG exist. The background's closedness is essential to the following reduction. No claim is made that the same variance formula holds for arbitrary nonclosed Hermitian backgrounds.

Put V=∫_Xω^n>0, Z_t=∫_Xexp(F+tG)dV, η_t=ω+dd^c u_t and ν_t=η_t^n/V. Stokes' theorem gives ∫_Xη_t^n=V, so (14.1.1) forces

\[
 b_t=\log V-\log Z_t,\qquad
 d\nu_t=\frac{\exp(F+tG)dV}{Z_t}.
\]

Consequently direct differentiation (without assuming the second-variation theorem) yields

\[
 \dot b_t=-\mathbb E_{\nu_t}G,\qquad
 \boxed{\ddot b_t=-\operatorname{Var}_{\nu_t}(G)
  =-\int_X\bigl(G-\mathbb E_{\nu_t}G\bigr)^2d\nu_t.}
\]

This also gives the **exact** Kähler interpretation of the square in printed (14.8.3). For f=∂_t u_t, set A=η_t^{-1}dd^c f. Differentiating the determinant equation once and substituting the first identity gives

\[
 \operatorname{tr}A=\operatorname{tr}_{\eta_t}(dd^cf)
 =G-\mathbb E_{\nu_t}G.
\]

For n≥2, pointwise diagonalization of the Hermitian endomorphism gives the elementary wedge identity

\[
  \big((\operatorname{tr}A)^2-\operatorname{tr}(A^2)\big)\eta_t^n
 = n(n-1)(dd^cf)^2\wedge\eta_t^{n-2}.
\]

Because η_t is closed and f smooth, the latter form is exact:
\[
 (dd^cf)^2\wedge\eta_t^{n-2}
 = d\bigl(d^cf\wedge dd^cf\wedge\eta_t^{n-2}\bigr),
\]
whose integral vanishes by Stokes. In n=1 the two traces agree pointwise, so no wedge argument is needed. Thus, in every dimension,

\[
 \boxed{\int_X\operatorname{tr}(A^2)\,d\nu_t
        =\operatorname{Var}_{\nu_t}(G).}
\]

This is independent of taking (14.8.3) on faith: it uses the first differentiated equation and the Kähler Stokes identity. It also checks the normalization and sign of (14.8.3) against the closed-background scalar formula 14.2.3.

**Optimal universal oscillation estimate.** If m=min_XG and M=max_XG, the elementary inequality (G-m)(M-G)≥0 implies E(G²)≤(M+m)E(G)-mM and hence

\[
  0\le -\ddot b_t=\operatorname{Var}_{\nu_t}(G)
    \le \frac{(M-m)^2}{4}.
\]

For nonconstant continuous G on connected X, strict positivity of the smooth measure and continuity give **both inequalities strictly**. The upper factor 1/4 nevertheless cannot be lowered uniformly over smooth data: on X=ℙ¹ with normalized Fubini–Study volume dV=ω_FS and F=0 at t=0, let

\[
 h([Z_0:Z_1])
  =\frac{|Z_0|^2-|Z_1|^2}{|Z_0|^2+|Z_1|^2},\qquad
 G_N=\tanh(Nh).
\]

Interchanging Z_0 and Z_1 preserves ν_0 and negates G_N, so E_{\nu_0}G_N=0. The equator {h=0} has zero area, while |G_N|→1 almost everywhere; dominated convergence gives Var_{\nu_0}(G_N)→1. Yet osc G_N=2 tanh N→2, so

\[
 \frac{\operatorname{Var}_{\nu_0}(G_N)}
      {(\operatorname{osc}G_N)^2}\longrightarrow\frac14.
\]

Products ℙ¹×Y with any compact Kähler (n−1)-fold Y and product metrics give the same optimal factor in every n≥1.

**Impact and proposed note:** Theorem 14.8.1 and Corollary 14.8.4 remain correct. Optionally add the boxed Kähler-only variance identity and sharp oscillation curvature bound immediately after Theorem 14.8.1; explicitly state dω=0 rather than silently exporting this identity to the Hermitian setting. This is conditional on the smooth-solution hypothesis supplied by Theorem 14.2.1 / Proposition 14.4.1 and is **not** an independent existence proof.

## POME-MA-SECOND-VARIATION-RENDER-DUPLICATE-001

**Status:** genuine duplication **in the integrated reading edition only** (editorial/rendering, not a mathematically false theorem). **Severity:** low.

At physical line **17** the source/permanent pair <code>4CC64AAD / 11F81D837A44</code> renders a two-line <code>align</code> containing both (14.8.2) and (14.8.3). At physical line **70**, after the end of the §14.8 exposition, the separate <code>reading-chunk</code> with source/permanent pair <code>3CBF8D7E / 578022E3660A</code> repeats the **same** formula for \(\ddot b_t\), including the displayed number (14.8.3). It is not an independent lemma or a distinct hypothesis/conclusion. The second chunk additionally wraps a full <code>align</code> within <code>aligned</code> inside display math: <code>\[\begin{aligned}\begin{align} ... \end{align}\end{aligned}\]</code>. This is invalid nesting under standard amsmath; **no browser or MathJax rendering test was performed**, so actual frontend failure is a candidate symptom, not certified.

**Proposed correction, not applied:** retain both distinct source labels and permanent tags, including direct links to the latter, but canonicalize the **visible** mathematical display to a single equation 14.8.3. If the separate permalink must remain, make its entry an alias/anchor to the canonical equation rather than a second display, and avoid nested alignment environments. This is a suggested separately reviewable rendering/registry patch; do not delete permanent tags or conflate the source items.

## Actual audit boundary

New examination covers only §14.8.1, (14.8.2)–(14.8.3), §14.8.4, and the duplicate reading chunk, with §14.1.1 / §14.2.3 / §14.4.1 inspected for the precise input assumptions. The global Tosatti–Weinkove existence proof, Hermitian adjoint-measure theory, nonlinear estimates in §§14.3–14.7, and the Gauduchon ansatz §§14.9–14.18 are **not verified** here. No integration of a current, build, CI, browser test, formal verification, source/registry change, or website publication is claimed. Total collection on the current ToC: 25 chapters, 747 numbered sections, **zero whole-section mathematical certifications**. Earlier findings and owner-deferred scope are untouched.
