# Componentwise top-degree duality, dualizing Ext and one-point curvature vanishing

Date: 2026-10-28. **Freshly read production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** f134fde1c03070e7c70c23f5fc9bc04feae70261. Scope: selected integrated reading-edition arguments, never complete section or full dependency-chain certification.

This audit is **outside** Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme, all **deferred-by-user**. No original mathematical statement has been shown false below.

## Reviewed sources and stable anchors

1. **§10.71, orientation and cap duality:** docs/sections/spectral-sequences-support-and-cup-products--orientation-classes-and-cap-duality/index.html, main blob **88ed77871455097c456cafaba2cca34986f3a3fb**. Lemma 10.71.1, permanent tag **603753CCA942**, physical lines **8–32**; Theorem 10.71.5, permanent tag **9EC6A8A9270A**, source **demailly-complex-geometry:87D6C3E7**, lines **77–103**; Theorem 10.71.7, permanent tag **211197321C0C**, source **demailly-complex-geometry:726E10E1**, lines **133–158**.
2. **§10.72, dualizing complex:** docs/sections/spectral-sequences-support-and-cup-products--the-dualizing-complex-and-cohomological-duality/index.html, blob **6b6c9fc091feb1d437ae0e3858f32feb11cba68a**. Proposition 10.72.1, tag **9E818639205F**, source **demailly-complex-geometry:11705A2E**, lines **8–38**; Proposition 10.72.2, tag **13DBDC23AA55**, source **demailly-complex-geometry:AA116797**, lines **44–60**; Theorem 10.72.3, tag **3968AEF4C8FE**, source **demailly-complex-geometry:14A61A97**, lines **66–87**; Corollary 10.72.4, tag **9C9125F4F2EE**, source **demailly-complex-geometry:3F7B3578**, lines **92–108**.
3. **§10.92, one-point vanishing:** docs/sections/one-point-curvature-positivity-and-vanishing--one-point-vanishing-on-compact-complex-manifolds/index.html, blob **92bd47c3486213df134952fce23f4291c3ae81ca**. Corollary 10.92.1, tag **B3500F172230**, source **demailly-complex-geometry:269B809F**, lines **8–29**; Corollary 10.92.2, tag **D736EC97F02B**, source **demailly-complex-geometry:AC1F8542**, lines **34–69**.
4. **Previously audited dependency (§10.91):** docs/sections/one-point-curvature-positivity-and-vanishing--one-point-positivity-and-modification-descent/index.html, blob **95b3f78a729e01664c4a24d3ef8aa96143ead523**. Proposition 10.91.1, tag **35E27213FA56**, source **demailly-complex-geometry:CAB0AEA4**, lines **8–40**; Theorem 10.91.2, tag **8532D3ED47E8**, source **demailly-complex-geometry:156BC1D4**, lines **46–71**. This dependency crosscheck is NOT a newly reviewed section.
5. **§9.55 was consulted only to compare scope.** Its arithmetic evaluation basis was already recorded as POME-ARITH-EVAL-BASIS-ORDERS-001, and is neither repeated as a new finding nor counted as new coverage. Its separate extension/\(L^2\) proof chain was not opened.

## POME-TOP-COHOM-COMPONENT-PRODUCT-001

**Severity:** low. **Status:** verified conditional deduction; the printed connected noncompact vanishing theorem is correct. **Affected dependents:** Theorem 10.71.7, Corollary 10.72.4, statements about top-degree ordinary versus compact-support cohomology for possibly disconnected spaces.

**Proposition (conditional on the printed cap/local-system results).** Let \(X\) be a paracompact Hausdorff real smooth \(n\)-manifold, not necessarily connected, \(A\) a locally constant \(R\)-module sheaf, and \(X_i\) its open connected components. Let \(\tau_i\) be each orientation system. Then
\[
H^n(X,A)\ \cong\
\prod_{i:\ X_i\ \mathrm{compact}}
\Big((\tau_i\otimes A_{x_i})_{\pi_1(X_i,x_i)}\Big).
\]
The subscript denotes coinvariants for parallel transport. An empty product of \(R\)-modules is the zero module. This also works in dimension \(n=0\).

**Proof.** A manifold's connected components are open. Sheaf sections over a disjoint union are the product of sections over its components. Choose componentwise flabby (e.g. Godement) resolutions; products of exact sequences of modules are exact. Taking degree-\(n\) cohomology therefore gives \(H^n(X,A)=\prod_i H^n(X_i,A|_{X_i})\), not a direct sum in the presence of infinitely many components. By Theorem 10.71.7, each connected **noncompact** component contributes zero. On each compact component, ordinary and compact-support cohomology agree. By Theorem 10.71.5, cap product identifies its top-degree cohomology with \(H_0(X_i,\tau_i\otimes A)\); Corollary 10.72.4 computes this group by loop coinvariants. This proves the formula without assuming sequential compactness of any inverse system.

**Connectedness is essential for the original unrestricted assertion:** \(X=\mathbb R\sqcup S^1\) with \(n=1,A=\underline{\mathbb Z}\) is noncompact, but \(H^1(X,A)=0\times\mathbb Z\cong\mathbb Z\ne0\). For countably many compact oriented \(n\)-manifold components, \(H^n\) is the **product** of their top classes, whereas \(H_c^n\) is the **direct sum**. These explicit distinctions are not counterexamples to the correctly qualified printed result.

**Proposed correction/addition:** Optional precise componentwise corollary after §10.71.7. Do **not** delete its connectedness hypothesis; do **not** substitute direct sum for product. The proof uses the collection's cap duality and soft/flabby comparison conditionally, without an independent full certification of those prerequisites.

## POME-DUALIZING-EXT-STALK-ENDPOINT-001

**Severity:** low. **Status:** verified conditional deduction, genuine boundary of the coefficient hypothesis, not a false printed theorem. **Affected dependents:** Propositions 10.72.1–2 and Theorem 10.72.3; interpretations of the two-row dualizing complex as an actual resolution.

Consider \(R=\mathbb Z\), \(X=\mathbb R\) (real dimension \(n=1\)), the constant local system \(A=\underline{\mathbb Z/2}\) and \(M=\mathbb Z\). The elementary free resolution
\[
0\longrightarrow\mathbb Z\xrightarrow{\ \times2\ }\mathbb Z
\longrightarrow\mathbb Z/2\longrightarrow0
\]
shows
\[
\operatorname{Hom}_{\mathbb Z}(\mathbb Z/2,\mathbb Z)=0,\qquad
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,\mathbb Z)=\mathbb Z/2.
\]
Since \(\mathbb R\) has trivial orientation local system, the correctly stated Proposition 10.72.2 therefore gives
\[
\mathcal H^0(F^\bullet)=0,\qquad
\mathcal H^1(F^\bullet)=\underline{\mathbb Z/2}\ne0.
\]
The nonzero second row cannot be discarded. Globally, compact cohomology is
\(H_c^1(\mathbb R,\underline{\mathbb Z/2})=\mathbb Z/2\) and \(H_c^0=0\).
At \(q=1\), the exact sequence of Proposition 10.72.1 reads
\[
0\longrightarrow\underbrace{\operatorname{Ext}^1(H_c^1,\mathbb Z)}_{\mathbb Z/2}
\longrightarrow H^1(\Gamma(\mathbb R,F^\bullet))
\longrightarrow\underbrace{\operatorname{Hom}(H_c^0,\mathbb Z)}_{0}
\longrightarrow0,
\]
hence \(H^1(\Gamma(F^\bullet))=\mathbb Z/2\), although the degree-zero Hom coefficient sheaf is zero. The local algebraic Ext calculation is independent; the identification of compact cohomology uses the printed one-dimensional orientation/compact-support calculation.

**Proposed addition:** Optional coefficient counterexample after §10.72.2. Preserve the \(\operatorname{Ext}_R(L,M)=0\) hypothesis of the resolution assertion and Theorem 10.72.3, and its **noncanonical** splitting, without mistaking a nonzero Ext row for a failure of Proposition 10.72.1.

## POME-ONEPOINT-VANISH-EACH-COMPONENT-001

**Severity:** low. **Status:** verified conditional deduction, not a false printed theorem. **Affected dependents:** Corollaries 10.92.1–2; any proposed use of one-point curvature vanishing on a disconnected compact complex space without a strict point per component.

Let \(X=\mathbb P^1_a\sqcup\mathbb P^1_b\), of dimension \(n=1\), and set
\(F|_{\mathbb P^1_a}=\mathcal O(1)\),
\(F|_{\mathbb P^1_b}=\mathcal O\).
Give the first line a positive Fubini–Study metric and the second the flat metric. Then curvature is semipositive **everywhere**, strictly positive at a point of \(X\), and \(m=r=q=n=1\) falls exactly in the printed vanishing range, but
\[
\begin{aligned}
H^{1,1}_{\bar\partial}(X,F)&\simeq
H^1(\mathbb P^1,\Omega^1\otimes\mathcal O(1))
\oplus H^1(\mathbb P^1,\Omega^1)\\
&\simeq H^1(\mathbb P^1,\mathcal O(-1))
\oplus H^1(\mathbb P^1,\mathcal O(-2))
=0\oplus\mathbb C\ne0.
\end{aligned}
\]
Similarly take \(\mathcal O(-1)\) with negative curvature on the first component and \(\mathcal O\) on the second. Curvature is seminegative everywhere, strictly negative somewhere, but \(H^{0,0}_{\bar\partial}(X,F)\ne0\) due to the flat component. Thus **dropping connectedness while retaining only a single global strict point** would be false. The printed Corollary 10.92.1 explicitly assumes compact **connected** \(X\), hence is not contradicted.

**Correct sufficient extension:** A compact complex manifold has finitely many connected components. If the relevant semipositivity/seminegativity holds on all components and every component has some strict point in the specified rank regime, apply Corollary 10.92.1 separately and take the finite direct sum of Dolbeault cohomologies. The same applies to Corollary 10.92.2 with the hypotheses checked componentwise. This condition is **sufficient**, not a claimed necessary criterion for vanishing. It remains conditional on the full Kähler-modification and curvature vanishing inputs used by §10.91, which were NOT reproved here.

**Proposed addition:** A concise componentwise remark after §10.92.1. Do not alter the correct connected theorem or treat its geometric premise as established independently.

## Additional proof inspections and precise coverage

- §10.71: checked the construction of the orientation twist, compact fundamental class transport, cap boundary sign and the displayed top-degree exhaustion/Mittag–Leffler step; did not transitively certify the whole sheaf comparison.
- §10.72: checked the degrees of \(D=\delta_I+(-1)^p f\,d_L\), the stated Ext/Hom cohomology rows and distinction of its natural short exact sequence from its nonnatural splitting; did not certify every derived Hom prerequisite.
- §§10.91–10.92: checked the determinant curvature trace implication, rank preservation through modification at critical points and the formula for the vector-valued current pushforward; the compact Kähler vanishing theorem is still a conditional input.
- First selected proof-level coverage was performed in previously inventory-only **§§10.71, 10.72, 10.92** only. §10.91 and §9.55 were crosschecks of already reviewed material. The coverage matrix continues to retain **747 actual ToC section IDs**. **Zero** complete sections or chapters were certified.
- No new confirmed false printed theorem, no project tests, builds, symbolic test runs, formal verification, source/body/registry/permanent-tag edits, changes to main, CI or website publication. Historical unresolved and resolved findings, and all **deferred-by-user** excluded-programme notes, are preserved without reclassification.

## Next broad review candidates

Move to previously inventory-only nonexcluded §§9.33–9.34 (Levi boundary geometry), §§10.76/10.83–10.87 (complex cohomology and modifications), and §§16.17–16.18 (model-envelope arguments), rather than repeatedly cycling through the same topological prerequisites.

