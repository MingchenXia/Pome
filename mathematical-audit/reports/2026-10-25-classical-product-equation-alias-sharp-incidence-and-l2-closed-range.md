# 2026-10-25 — classical-product equation alias, sharp incidence dimension, and nonclosed L2 range

**Observed UTC time:** 2026-10-24T19:01:57.100Z. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Existing review head before this report:** 54d1a2a3bfd77ad8e789fd5485a95f3e2e8d8118. Review target: integrated reading-edition source at the exact pinned main, with prior review-ledger and 747-section matrix consulted first. The owner-excluded Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme was **not** examined or resumed. Any regularization references in nearby arguments are dependencies only.

## POME-CLASSICAL-COLLAR-ALIGN-DUP-001

**Severity:** medium. **Status:** confirmed error **in reading-edition equation integration**, not a false current-product estimate.

**Precise source:** Lemma 7.29.1, source label **demailly-complex-geometry-828A36D4**, permanent tag **438B9224299E**, at
**docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-with-compact-unbounded-loci/index.html**, main blob **65666651048e9ada933a763b7d381766f8b43965**, lines **11–21**. The two-row complete, valid displayed align expression for equations (7.29.2) and (7.29.3) has source label **demailly-complex-geometry-FCD3E0F0**, permanent tag **9135B1E39C61**, lines **12–14**.

**Confirmed defect:** at **line 187** the same section separately re-exports only the second row, namely (7.29.3), under source label **demailly-complex-geometry-6BC3A163**, permanent tag **F8A095BBD0A5**, with invalid nested TeX
\[
\texttt{\textbackslash[ \textbackslash begin\{aligned\}\textbackslash begin\{align\}\ \cdots\
\textbackslash end\{align\}\textbackslash end\{aligned\}\textbackslash]} .
\]
Its standalone **docs/tag/F8A095BBD0A5/index.html** has main blob **361958398849302b7fbd5943a7df9a875216489f** and independently reproduces the malformed alias. This is an additional independently pinned occurrence of the same **class of exporter defect** previously documented for three Gauduchon equations; do not count those old occurrences as new findings.

**Recommended repair, not applied:** preserve both source labels and **all** permanent tags; anchor tag F8A095BBD0A5 to the actual second row of the existing complete align display, or give its standalone tag view a single valid formula while avoiding an extra truncated reading-section chunk. In particular, do not rewrite the mathematical inequality or delete an equation number. The confirmed damage affects canonicalization, MathJax rendering, source traceability and permalinks; it does **not** refute the estimate
\[
\int_B(-f_0)\,dd^cf_1\wedge\cdots\wedge dd^cf_r\wedge T\wedge\omega^{p-r}
\leq \|\psi\|_\infty A^{r+1}\!\int_B T\wedge\omega^p
\quad(0\leq r\leq p-1,\ A>0).
\]
The assumptions include a common collar where every locally bounded \(f_j=A\psi\), with \(T\) closed positive of bidimension \((p,p)\).

## POME-INCIDENCE-HAUSDORFF-SHARP-001

**Severity:** low. **Status:** verified conditional deduction (sharpness/independent counterexample to a stronger *hypothetical* statement), not an error in the printed lemma.

**Source and hypotheses:** Lemma 7.29.6, label **demailly-complex-geometry-A5A5FB86**, tag **7EADA0AAC4F2**, same section and blob **65666651048e9ada933a763b7d381766f8b43965**, lines **138–170**. Here \(0\leq s<n\), \(F\subset\mathbb C^n\) is closed with \(\mathcal H^{2s+1}(F)=0\), and \(V=\{0\}^s\times\mathbb C^{n-s}\). The lemma concludes that for almost every \(g\in U(n)\) and almost every \(r>0\), the sphere \(g(V)\cap\{|z|=r\}\) avoids \(F\).

**Exact optimality of the Hausdorff exponent:** Put
\[
W=\mathbb C^s\times\mathbb R\times\{0\}^{n-s-1}\subset\mathbb C^n,
\qquad F=W .
\]
This is a closed real-linear subspace of real dimension \(2s+1\). For every \(g\in U(n)\), the elementary Grassmann inequality gives
\[
\dim_{\mathbb R}(W\cap gV)
\geq \dim_{\mathbb R}W+\dim_{\mathbb R}gV-2n
=(2s+1)+2(n-s)-2n=1.
\]
Pick a nonzero \(w\in W\cap gV\). Because the intersection is real-linear, \(rw/|w|\) belongs to \(F\cap g(V\cap\{|z|=r\})\) for **every \(r>0\)**. On the other hand,
\[
\mathcal H^\alpha(F)=0
\quad\text{for every }\alpha>2s+1
\]
(the unbounded subspace is a countable union of bounded Lipschitz images of \(\mathbb R^{2s+1}\)). Thus replacing the printed zero-\(\mathcal H^{2s+1}\) assumption by zero \(\mathcal H^\alpha\) for any \(\alpha>2s+1\), or merely by \(\dim_HF\leq2s+1\), makes the conclusion false in the strongest possible way: **every** \((g,r)\) is bad.

**Proposed optional addition:** a one-paragraph sharpness remark after Lemma 7.29.6. **Dependents:** the geometric incidence lemma and the Hausdorff-intersection route to the classical Bedford–Taylor products in §§7.28–7.31. The assertion is independent of smoothing, curvature-loss regularization and limit interchanges.

## POME-L2-UNREDUCED-NONCLOSED-001

**Severity:** low. **Status:** verified conditional deduction (self-contained example delimiting the printed theorem), not an error.

**Source and hypotheses:** Corollary 2.21.5, label **demailly-complex-geometry-63A1AB33**, tag **A76DD53006C1**, **docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html**, main blob **93b74f8a110bb6c45a7e53cdaed0910af7eb5118**, lines **86–103**, with complete Riemannian metric and a flat metric connection. Theorem 2.21.3, label **demailly-complex-geometry-CDC5D23B**, tag **CE09CDC33E77**, same blob lines **41–80**, establishes the required maximal-Laplacian and harmonic-domain facts. The corollary explicitly warns that the ranges need not be closed.

**A sharp elementary example:** Take \(M=\mathbb R\) with the Euclidean metric and the trivial flat complex line bundle. In degree zero,
\[
d:H^1(\mathbb R)\longrightarrow L^2(\mathbb R)\,dx,
\qquad u\longmapsto u'(x)\,dx .
\]
Let \(f(x)=(1+x^2)^{-1}\). Then \(f\in L^1\cap L^2\) and \(\int f=\pi\). If \(f=u'\) with \(u\in H^1(\mathbb R)\), local absolute continuity forces \(u(x)=\arctan(x)+c\). No constant \(c\) can make both limits \(c\pm\pi/2\) vanish; thus \(u\notin L^2\) and \(f\,dx\notin\operatorname{Ran}d\).

Choose \(\chi\in C_c^\infty(\mathbb R)\) with \(0\leq\chi\leq1\), \(\chi=1\) on \([-1,1]\), and \(\eta\in C_c^\infty(\mathbb R)\) with \(\int\eta=1\). For \(R\to\infty\), put
\[
\chi_R(x)=\chi(x/R),\quad
\eta_R(x)=R^{-1}\eta(x/R),\quad
m_R=\int_{\mathbb R}\chi_R f\,dx,\quad
f_R=\chi_R f-m_R\eta_R.
\]
Each \(f_R\) is smooth and compactly supported with integral zero, hence
\(u_R(x)=\int_{-\infty}^x f_R(t)\,dt\) belongs to \(C_c^\infty(\mathbb R)\), and \(du_R=f_R\,dx\). Yet
\[
\|f_R-f\|_2
\leq\|(1-\chi_R)f\|_2+
|m_R|R^{-1/2}\|\eta\|_2\ \longrightarrow 0,
\]
since \(m_R\to\pi\). Therefore \(\operatorname{Ran}d\) is **not closed**.

Its orthogonal complement is \(\ker d^*\), consisting of distributionally constant \(L^2\) functions, hence zero. Thus \(\overline{\operatorname{Ran}d}=L^2(\mathbb R)\,dx\). As every one-form on a real line is closed,
\[
H^1_{(2),\mathrm{unreduced}}(\mathbb R)
=L^2(\mathbb R)\,dx/\operatorname{Ran}d\ne0,
\qquad
\overline H^1_{(2)}(\mathbb R)=0=\mathcal H^1_{(2)}(\mathbb R).
\]
This gives a concrete nonzero unreduced class whose reduced class vanishes and verifies that the closure bars in Corollary 2.21.5 are indispensable, even with zero curvature.

**Proposed optional addition:** place this Euclidean-line example beside the reduced-cohomology statement. **Dependents:** readings of Hodge decompositions, range-closedness implications and \(L^2\) cohomology in §§2.21 and 10; no assertion of a gap in the printed proof.

## Other newly inspected nonexcluded proofs (no separate issue ID)

- **§2.19** at **docs/sections/concrete-completed-tensor-products/index.html**, main blob **358f584ab4004b3531629e87f1dd73bdea1256d4**. Proposition 2.19.1 source **demailly-complex-geometry-E56C631F**, tag **84C71E271314**, lines **11–28**: finite-support matrix truncation and exact projective \(\ell^1\)-norm. Proposition 2.19.2 source **demailly-complex-geometry-4D711A6B**, tag **96A052277244**, lines **33–52**: injective norm on \(c_0\), dual \(\ell^1\) norm and explicit polar qualification. Proposition 2.19.3 source **demailly-complex-geometry-C614F79A**, tag **C9CDFE118A86**, lines **57–81**: injective tensor and \(C(K\times L)\), **including non-Hausdorff compact factors**. For the latter, one checks that \(x\mapsto a(x,\cdot)\in C(L)\) is continuous by compactness of \(L\), then uses a finite norm-ball cover of its compact image and continuous \(\max\{\varepsilon-\|a_x-a_{x_i}\|_\infty,0\}\) weights. Dirac evaluation and dual norm bounds establish the isometric finite-sum equality. No Hausdorff separation of \(K,L\) is smuggled in. The upstream tensor-norm conventions in §2.13 were matched only as premises, not re-certified.
- **§7.29** selected Lemma 7.29.1 (collar mass formula and integrability exchange, lines **11–41**) and Theorem 7.29.5 source **demailly-complex-geometry-B0311B48**, tag **8FBB0E4DE397**, lines **47–132** (recursive degree restrictions, fixed trace bounds, weighted weak-limit comparisons). Conditional selected proof reading, **not** a full certification of the theorem's smoothing and all upstream bounded-product inputs.
- **§7.31** read *only as context*: Theorem 7.31.2 and Corollaries 7.31.3–4, main blob **86de377d6e6f17fc1a08a6e789a681ddfaabfac5**, lines **28–77**. The proof explicitly invokes Lemma 7.31.1, whose dedicated approximation/vanishing-curvature-error dependency is **deferred-by-user**. Its proof was **not** audited or repaired, and the section is not newly marked proof-covered.

## Status discipline and next coverage

Actual new selected proof-level coverage: previously inventory-only **§§2.19, 2.21, 7.29**. Incidence geometry and an explicit \(L^2\) nonclosed-range calculation are verified independently; the equation-alias issue is a **confirmed rendering/canonicalization error**, not a false theorem. No additional chapter or full dependency chain certified. §7.31 remains contextual/deferred at its regularization dependency. Existing confirmed errors, proof gaps, external dependencies and deferred records are unchanged.

The manuscript source, published docs, permanent tags, proof registry, main branch, website, CI and GitHub Actions were not modified. No repository build, formal verification or full-project test was performed. The only proposed changes concern future separately reviewable source/rendering work or optional mathematical examples.