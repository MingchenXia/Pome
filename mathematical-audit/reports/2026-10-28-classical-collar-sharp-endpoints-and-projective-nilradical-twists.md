# Mathematical audit — 28 October 2026: classical collar endpoints and projective nilradical twists

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting `review/mathematical-audit` HEAD:** `2f9bca2d9bf51ea9aecffca37a5b36da5189c9a1`. All conclusions below concern the actually integrated reading edition, not an inferred source-book numbering. **Status of each new ID: low / verified conditional deduction; no false printed theorem or newly certified proof chain.** Neither source bodies nor `main` were changed.

## Checked files, source provenance and exact scope

1. `docs/sections/classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current/index.html`, blob `86de377d6e6f17fc1a08a6e789a681ddfaabfac5`:
   - Theorem **7.31.2**, source label `demailly-complex-geometry-6CBD358C`, permanent tag `F6EE68FA9FDA`, statement lines **28–32**, collar/local-product arguments **37–46**.
   - Corollary **7.31.3**, source label `demailly-complex-geometry-AE90937D`, permanent tag `CF64F301AEAF`, statement lines **52–53**, signed integration-by-parts calculation **57–64**.
   - Corollary **7.31.4**, source label `demailly-complex-geometry-4876F9E5`, permanent tag `EBA900FA96EF`, statement line **70**, analytically small pole-locus reduction **75–76**.
2. `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--products-closed-subspaces-and-projective-charts/index.html`, blob `4373897c66d3fae21cab98bec91fff3457d23ade`: Theorem **9.59.2**, source `demailly-complex-geometry-979A59BB`, permanent tag `4D90B8C4C837`, statement **28–29**, graded chart and projective embedding proof **33–46**. Proposition **9.59.1**, source `demailly-complex-geometry-20E582B2`, tag `476B5A661E43`, lines **11–19**, checked for the distinction between an ordinary/reduced union and an ideal-theoretic thickening.
3. Context only: `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--analytic-local-models-and-infinitesimal-information/index.html`, blob `7a3c24deaab8602c3d2b4be2e31d739f02b5a657`: Proposition **9.60.1**, source `demailly-complex-geometry-2090FB67`, tag `57433F7B0D87`, lines **11–31**, states that analytic nilpotent germs are retained, not discarded.

**Exclusion boundary:** Lemma **7.31.1** (source label `demailly-complex-geometry-...`, permanent tag `FDDB630F0AA9`, lines **8–23**) is the cited smoothing input; its construction and any Demailly regularization, Bergman, weighted-L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof-completion work were **not audited**. The statements of Theorem 7.31.2 and Corollary 7.31.3 are taken **conditionally** on their pre-existing, unverified analytic prerequisites. The proof checks below concern only the stated nonexcluded product-degree, current, and distributional calculations. The report makes no claim of proof completion for Lemma 7.31.1 or Theorem 7.29.5.

## POME-COLLAR-WEIGHT-TOP-ENDPOINT-001

**Status:** low / **verified conditional deduction**; the printed Corollary 7.31.3 is correct in its stated range, and the excluded upper endpoint is genuinely impossible. **Affected:** Corollary 7.31.3 (tag `CF64F301AEAF`), the trace-measure interpretation of Theorem 7.31.2 (tag `F6EE68FA9FDA`), and comparisons of classical with non-pluripolar top products. **Proposed action:** optionally add this sharpness remark; keep `1\le q\le n-1`, without changing canonical labels or the theorem.

Let \(\mathbb B\subset\mathbb C^n\), \(n\ge2\), be the unit ball, \(\omega_0=dd^c|z|^2>0\), and take all \(u_j(z)=V(z)=\log|z|^2\). These functions are plurisubharmonic on a neighborhood of the closed unit ball, nonidentically \(-\infty\), and their unbounded locus is precisely \(\{0\}\), so the boundary-incidence hypothesis \(\partial\mathbb B\cap L(u_j)=\varnothing\) holds. The ball admits a smooth strict psh exhaustion.

For \(1\le q<n\), on the punctured ball the Hermitian matrix of \(dd^c\log|z|^2\) has one zero radial eigenvalue and \(n-1\) tangential eigenvalues proportional to \(|z|^{-2}\). Thus, for the smooth Kähler trace,
\[
(dd^c\log|z|^2)^q\wedge\omega_0^{n-q}
\asymp |z|^{-2q}\,dV
\qquad(0<|z|\ll1),
\]
with positive dimensional constants. The \(q<n\) trace has no atom at \(0\), by its classical definition/positive-current mass dimension, so its logarithmically weighted local mass is finite:
\[
\int_{|z|<\varepsilon}|\log|z|^2|\,
(dd^c\log|z|^2)^q\wedge\omega_0^{n-q}
\asymp \int_0^\varepsilon |\log r|\,r^{2(n-q)-1}\,dr<\infty.
\]
For \(q=n\), in contrast, the **classical isolated-pole product** in the same \(dd^c=(i/2\pi)\partial\bar\partial\) convention is \((dd^c\log|z|^2)^n=\delta_0\) (standard radial Stokes mass-one identity; this is also the previously recorded classical/non-pluripolar distinction). Therefore \(\int|V|\,d\delta_0=\infty\). The conclusion of Corollary 7.31.3 is false with \(q=n\), even for an isolated pole and a strictly pseudoconvex ball. This does **not** contradict the correct separate existence statement for a classical top product.

Additionally, **conditionally on Corollary 7.31.3**, every corresponding trace measure \(R\wedge\omega^{n-q}\) for \(q<n\) annihilates a complete pluripolar set \(E=\{V=-\infty\}\) whose psh defining function \(V\) is available near \(\overline D\): the asserted \(V\in L^1_{\mathrm{loc}}(R\wedge\omega^{n-q})\) immediately forces the measure of \(E\) to vanish. This is deliberately **not** asserted for arbitrary merely local polar sets or for \(q=n\).

**Direct proof-step check, not analytic certification.** For the source equation at lines **57–64**, with \(\chi=-\psi\) on \(\Omega_\delta\), compactly supported \(\chi\), \(R=A^q\omega^q\) on the outer collar, and \(R,\omega\) closed, the distributional identity
\[
\int_\Omega\chi\,dd^cV_k\wedge R\wedge\omega^{n-q-1}
=\int_\Omega V_k\,dd^c\chi\wedge R\wedge\omega^{n-q-1}
\]
splits into the inner integral \(-\int_{\Omega_\delta}V_k R\wedge\omega^{n-q}\) and outer term \(A^q\int_{\Omega\setminus\Omega_\delta}V_k\,\omega^{n-1}\wedge dd^c\chi\). Rearrangement gives the printed sign exactly. The factor \(\omega^{n-q-1}\) is well typed **only for \(q\le n-1\)**. Uniform estimates and limit passage remain conditional on the already cited earlier inputs; we did not reproduce the excluded approximation proof.

## POME-COLLAR-ANALYTIC-LOCUS-DIM-ENDPOINT-001

**Status:** low / **verified conditional deduction**; printed Corollary 7.31.4 remains correct. **Affected:** its coefficient-integrability and \(dd^c(uT)\) assertions (tag `EBA900FA96EF`, lines **70–76**), and downstream classical products with controlled pole incidence. **Proposed action:** optional explicit extremal example; do **not** weaken the hypothesis \(\dim_{\mathbb C}A\le p-1\) to \(\dim_{\mathbb C}A\le p\).

For any integers \(n\ge2\) and \(1\le p\le n-1\), set
\[
A=\{z_{p+1}=\cdots=z_n=0\}\subset\mathbb C^n,\qquad
T=[A],\qquad u(z)=\log|z_{p+1}|^2.
\]
The analytic integration current \(T\) is closed positive of bidimension \((p,p)\), and \(u\) is a genuine psh function, not identically \(-\infty\) on the ambient manifold. But \(L(u)\cap\mathrm{supp}\,T=A\) has **dimension \(p\)**, and the restriction of \(u\) to all of \(A\) equals \(-\infty\). Hence the coefficient integral \(\int_K|u|\,d\|T\|\) is infinite on any relatively open piece of \(A\) of positive \(2p\)-volume, so \(uT\) is not a current defined by coefficient integrability. Consequently the universal bound \(p-1\) is sharp for \(1\le p<n\). The special top-dimensional \(p=n\) case is not claimed to share the same counterexample. No analytic regularization, source expansion, or Hironaka argument is involved.

## POME-PROJ-NILRADICAL-GLUING-TWIST-001

**Status:** low / **verified conditional deduction**; Theorem 9.59.2 and Proposition 9.60.1 are correct as printed. **Affected:** the nonreduced-\(\operatorname{Proj}_{cl}\) examples under tag `4D90B8C4C837` and nilpotent analytic local models under tag `57433F7B0D87`; canonical comparison of apparently identical reduced projective supports. **Proposed action:** optionally add the following completely explicit graded test; **do not canonical-merge** different nonreduced ringed spaces merely because their reductions or all affine formal local models have matching appearances.

Fix an algebraically closed field \(k\). Consider two graded \(k\)-algebras, both generated by finite-dimensional \(B_0,B_1\), satisfying exactly Theorem 9.59.2:
\[
B_{\mathrm{tw}}=k[x_0,x_1,e]/(e^2),\quad
\deg x_0=\deg x_1=\deg e=1,
\]
and
\[
B_{\mathrm{tr}}=(k[\eta]/(\eta^2))[x_0,x_1],\quad
\deg x_0=\deg x_1=1,\quad\deg\eta=0.
\]
Both \(\operatorname{Proj}_{cl}\) constructions have the same reduced ringed space \(\mathbb P^1_k\), since quotienting by their nilradical yields \(k[x_0,x_1]\). In the first case the chart \(x_0\ne0\) has coordinate \(z=x_1/x_0\), square-zero element \(t=e/x_0\); the \(x_1\ne0\) chart has \(w=x_0/x_1=1/z\), \(s=e/x_1\). On their overlap \(t=z\,s\). Therefore the square-zero nilradical sheaf is the nontrivial line bundle \(\mathcal O_{\mathbb P^1}(-1)\). This can be checked without invoking a line-bundle classification: a global nilpotent section would be \(a(z)t=b(w)s\) with polynomials \(a,b\), forcing
\[
 b(w)=w^{-1}a(w^{-1}),
\]
hence \(a=b=0\) and \(H^0(\mathbb P^1,\mathcal N_{\mathrm{tw}})=0\).

For \(B_{\mathrm{tr}}\), the analogous chart nilpotent is simply \(\eta\), independent of coordinate and unchanged on overlaps, so \(\mathcal N_{\mathrm{tr}}\simeq\mathcal O_{\mathbb P^1}\) and \(H^0(\mathbb P^1,\mathcal N_{\mathrm{tr}})=k\eta\ne0\). Consequently the two nonreduced projective ringed spaces are **not isomorphic**, despite having the same reduced projective line and locally identical dual-number descriptions. The distinction is intrinsic to gluing, not a proof duplicate, and is invisible to any comparison of reduced support alone. No claim is made about projective varieties outside the generated-in-degrees-\(0,1\) hypotheses.

## Coverage, conditions and write boundary

- **First newly selected nonexcluded section:** §**7.31**, restricted to Theorem 7.31.2's compact relative-collar and support/degree bookkeeping, Corollary 7.31.3's signed current identity, and Corollary 7.31.4's analytic pole-dimensional boundary. Lemma 7.31.1's smoothing programme **deferred-by-user**, not inspected.
- **Incremental previously selected section:** §**9.59**, precise graded-chart/gluing and nilradical examples; §**9.60.1** context only, not recounted as new coverage.
- Retain the current actual table-of-contents inventory of **25 chapters / 747 distinct numbered sections**, with **zero** full-section or chapter certifications. This run compared actual current chapter 7 and chapter 9 paths and the preexisting coverage matrix; it did **not** independently re-count all 25 chapters. Historical unresolved/verified/deferred findings are preserved.
- Three low conditional deductions; no new confirmed false theorem, no full analytic chain verification, no duplicate canonicalization, and no project suite, site build, CI, browser rendering test or formal proof run.
- The entire Demailly approximation/regularization and dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, not resolved, certified or reopened.
