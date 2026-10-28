# Cone-adapted analytic multiplicity and a malformed Jensen-equation alias — 28 October 2026

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch at start:** 4264019bb6a9cbee7d007d53542f0bf2e1861aa6. **Scope:** first directly selected proof passages in §§6.35, 6.36, 6.38; limited crosscheck of the previously inspected §6.34 comparison theorem. The excluded Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme were **not** inspected. Previous related records remain **deferred-by-user**, not certified. Exact integrated HTML on the pinned main is the source of the claims below.

## POME-JENSEN-EQ-ALIAS-NESTED-001 — medium; confirmed error (rendering/integration, NOT a false mathematical theorem)

**Main source:** docs/sections/lelong-densities-generalized-masses-and-multiplicity--boundary-measures-and-the-weighted-jensen-formula/index.html, blob a341258d025614e3f8d6852f170f519df7362554. Theorem 6.36.3 is source demailly-complex-geometry:F9891B8A, permanent tag B30AA438CFC2, beginning at physical line 40. Its proof contains the complete, mathematically meaningful two-row display (6.36.6) at physical line 66. Equation source demailly-complex-geometry:9BE6EC5A, permanent tag 6343DCE084B8. The same section has an additional independent reading chunk at physical line **148**, after the surrounding section's normal mathematical prose, with this payload:

    \[\begin{aligned}\begin{align} & =\int_a^r M_{dd^c V}(\varphi,t)\,dt.\tag{6.36.6}\end{align}\end{aligned}\]

This latter display is both *truncated* (only the second equality, starting with an alignment ampersand and no left-hand expression) and syntactically invalid LaTeX (an align environment nested in aligned inside display delimiters). The canonical full proof display already contains both equalities and the tag. The exact same defective standalone content occurs at docs/tag/6343DCE084B8/index.html, blob bf3bb77280e631edcd8982d0c6d8c6aaa64dc15e, physical line 13 (the separate equation permalink page). These are not two valid mathematical formulas requiring separate canonical entries.

**Reproduction performed:** read both current-main HTML blobs; directly compared the full theorem-proof equation at section line 66 against the extra section chunk at line 148 and the equation's own tag page. The second payload starts with the terminal equality and contains the literal sequence \begin{aligned}\begin{align}, whereas the canonical proof display is a normal \begin{align} with both rows. No browser rendering, math-engine execution, build, or automated test was performed.

**Proposed correction (NOT applied):** retain the full canonical (6.36.6) only once in the §6.36 reading flow, and make the permanent equation tag 6343DCE084B8 resolve to the complete meaningful two-row formula (or an exact single anchor pointing to it); remove the truncated double-rendered fragment and invalid nesting without deleting the tag, historical source identity, theorem proof or attribution. Inspect source-variant/equation alias composition rather than rewriting the mathematics. Related affected locations include Theorem 6.36.3 proof references to (6.36.6), the standalone tag page, and future cross-reference rendering. The general nested-align category was noted elsewhere in prior audits, but this specific equation and page pair were not previously recorded.

## POME-CONE-PROJECTION-SHEET-UNBOUNDED-001 — low; verified conditional deduction (printed statements correct)

**Main sources and anchors:**
- docs/sections/lelong-densities-generalized-masses-and-multiplicity--holomorphic-maps-and-weights/index.html, blob d815e0a11cf3aab85abcebd9d5a943ba72c1dedb. Corollary 6.35.2, source demailly-complex-geometry:A83110AE, permanent tag 22D3ABC6CFCD, physical lines 30–44; proper projection number equals its sheet count.
- docs/sections/lelong-densities-generalized-masses-and-multiplicity--analytic-multiplicity-and-ordinary-density/index.html, blob a74bd5c4cecc4d310f4b7b08af1b96bc8ff667e0. Lemma 6.38.1 and cone inequality (6.38.2), tag CD38640A3802, physical lines 8–44; Theorem 6.38.3, source demailly-complex-geometry:8BE55493, tag 673FC5FBB2C8, lines 46–81; Corollary 6.38.5, source :ABDB2F19, tag CF13884F31CB, lines 83–102.

Let integers m≥2 and k>m be coprime, and take the reduced irreducible plane curve germ

\[
  C_{m,k}=\{(x,y)\in\mathbf C^2:y^m=x^k\},\qquad
  t\longmapsto (t^m,t^k).
\]

Its normalization is injective off the origin because gcd(m,k)=1. A finite projection onto the x-axis has **m** distinct sheets over generic nonzero x: the m roots of t^m=x give distinct y=t^k. Similarly projection onto the y-axis has **k** sheets, from the k roots of t^k=y. Both maps are finite, proper on sufficiently small representatives, and have a singleton fiber over zero. These claims follow directly from the displayed parametrization and the coprimality condition.

But the x-projection is cone-adapted: on C, |y|=|x|^{k/m}≤C|x| locally. In contrast the y-projection is **not** cone-adapted, because |x|/|y|=|t|^{m-k}→+∞. Hence Theorem 6.38.3 and Corollary 6.35.2 distinguish exactly

\[
  \nu([C_{m,k}],0)=m,\qquad
  \nu([C_{m,k}],\log|x|^2)=m,\qquad
  \nu([C_{m,k}],\log|y|^2)=k.
\]

The ordinary Lelong number is also directly seen from the normalization: its generic tangent line is the x-axis with leading multiplicity m, and the cone inequality makes log(|x|²+|y|²)−log|x|² bounded on the punctured curve. The weighted quantities follow by pushforward of the integration current under the two finite projections (m or k sheets); their exceptional zero sets have zero regular-locus area. For fixed m, k=jm+1 tends to infinity as j→∞. Thus, **if one drops cone-adaptedness**, a finite projection's degree can exceed the *ordinary* multiplicity by an arbitrarily large factor (k/m). For example (m,k)=(2,7) gives ordinary density 2 but y-projection weight number 7. The printed theorem is correct because it explicitly requires the cone hypothesis; this example must not be logged as a false theorem.

**Proposed optional addition:** insert this local model as a sharp hypothesis warning beside §6.38.3, cross-link §6.35.2, and preserve the ordinary/projected weighted multiplicity distinction in any canonicalization. It affects finite-map degree comparisons and interpretation of §6.43 degree data, but neither the analytic normalization theorem nor generic-coordinate proof is newly certified here. The finite-projection formula and bounded weight comparison are recorded as internal conditional inputs.

## Independent Jensen boundary check; not a new finding ID

Source §6.36.3 tag B30AA438CFC2 and §6.36.7 tag 5736E627F741, same §6.36 main file, physical lines 40–110. Check the full-pole extended-value convention in complex dimension one with the ordinary normalization dd^c log|z|²=δ₀. Take \(\varphi(z)=V(z)=\log|z|^2\), any r<0 and r₀<r. The radial boundary measure \(\mu_r\) is probability on \(|z|=e^{r/2}\), so \(\mu_r(V)=r\). The inner measure \(\sigma=\delta_0\) integrates V to −∞ on every sublevel, whereas \(M_{dd^cV}(\varphi,t)=1\) for every finite t. Thus equation (6.36.4) reads \(+\infty=\int_{-\infty}^r1\,dt=+\infty\) in the explicitly specified extended interpretation, not an illicit \(\infty-\infty\). By contrast the finite annular formula (6.36.5) reads \(r-r_0=\int_{r_0}^r1\,dt\). This independently verifies the necessity and compatibility of the two distinct conventions; it is *not* a full proof of the general theorem. In particular, the theorem's cited smoothing Lemma 7.31.1 is an upstream **deferred-by-user** input and was neither read nor extended.

## Actual coverage and limits

This session newly inspected selected nonexcluded integrated proof passages in §6.35 (projection formula and finite-sheet number), §6.36 (boundary/finite-versus-extended Jensen equations, canonical equation markup, the specific radial check), and §6.38 (cone-adapted projections, ordinary density, regularity/multiplicity criterion). §6.34 was an upstream comparison cross-reference only. The previous selected §§6.43–6.48 were **not** claimed as first coverage, and no other source project was edited. All 747 unique current chapter-ToC section identifiers remain in the matrix; **zero full sections/chapters certified**. This audit does not verify the full Remmert, analytic parametrization, current integration, weighted CLN, or Bedford–Taylor dependency chains. The excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss programme remains **deferred-by-user**. No tests/builds/CI/formal proof or website publishing were performed.

**GitHub policy:** only audit Markdown on review/mathematical-audit. Main, mathematical source bodies, registries, permanent tags, production site, CI and publication are unchanged. Existing audit PR #9 is already closed/merged, so no repeat PR was created.