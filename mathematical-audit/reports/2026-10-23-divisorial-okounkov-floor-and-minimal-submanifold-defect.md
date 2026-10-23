# Pome mathematical audit — divisorial Okounkov floors, minimal-submanifold mean-value defects, and Cao–Păun boundaries

**Date:** 2026-10-23, Asia/Shanghai. **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch before this session:** 408d3e0816e2b72756c8bf27a5ae3eae54ecc51c. Read main AGENTS.md (blob eda69505b93b4782290d9cfac07c8651dedd17c5), documentation/proof-expansions.md (8b37e218c74d5a93637e0f092cf5f29cc338a94d), the chapter index (c0c07abf4d8f7575b54cff2ec694fcf987f51cf8), and review-branch README.md (7967ffabeccea69fd80a5ec5d364e0a8e6bca137) and mathematical-audit/LATEST.md (d46ffbe1e7540612f807c7e756384e043e0ffa78). The current 25-chapter/747-section count is an inventory, not an audit certification.

**Scope actually read:** selected integrated text in §§19.1, 10.103–10.105, 10.108, 9.77; restricted mathematical-definition crosschecks §§19.2/19.4. No entire section was certified, and no original source, tag, reader or main file was modified. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remain **deferred-by-user**. No attempt was made to prove the relative Bergman, singular L² direct-image or extension theorems invoked elsewhere.

## POME-OKO-DIV-FLOOR-SERIES-001 — verified conditional deduction, low severity

**Precise source:** docs/sections/the-theory-of-okounkov-bodies/index.html, blob e58bf2e05976402030964165451485a4c57a330f, source sgpt:350F3C2E, permanent section tag 2DF8DA44EB89, lines 22–35, specifically the graded ideal series and assertion of nonclosure in lines 26–29. Comparison: docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html, blob 33212916f9ea7754f51f8194cfb76c2fcbe8efab, Defs. 19.2.4/9 and Thm. 19.2.10 (tag 2534E787147E); docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html, blob c661e264cab0995a2a344453039940028feff8e0, Thm. 19.4.16 (A653D079A694, lines 251–256) and Eq. 19.4.20 (3DAADFC49A31, lines 274–282).

**Result, with all hypotheses:** On \(X=\mathbb P^1\), \(L=\mathcal O(d)\), integer \(d\ge1\), flag at \(D\in X\), and \(0\le c<d\), normalize \(dd^c=(i/2\pi)\partial\bar\partial\), \(\int\omega_{\rm FS}=1\). Fix a smooth metric of curvature \(d\omega_{\rm FS}\) on \(L\), put \(\phi=c\log|s_D|_{h_{\rm FS}}^2\), and multiply that metric by \(e^{-\phi}\). Its curvature is
\[
T=(d-c)\omega_{\rm FS}+c[D]\ge0.
\]
For each \(k\ge1\), local integrability of \(|z|^{2(a-kc)}\) shows
\[
\mathcal I(k\phi)=\mathcal O(-\lfloor kc\rfloor D),\quad
\Gamma_k=\{a\in\mathbb Z:\lfloor kc\rfloor\le a\le dk\},
\quad h^0(L^k\otimes\mathcal I(k\phi))=dk-\lfloor kc\rfloor+1.
\]
Each order is realized by a homogeneous monomial on \(\mathbb P^1\).

**Exact semigroup test:** For \(k,\ell\ge1\), the minimum-order product misses the next multiplier ideal by
\[
\delta_{k,\ell}=\lfloor(k+\ell)c\rfloor-\lfloor kc\rfloor-\lfloor\ell c\rfloor
\in\{0,1\},
\]
equal to 1 precisely when \(\{kc\}+\{\ell c\}\ge1\). Thus the raw graded set \(\Gamma\) is a semigroup iff \(c\) is an integer. Indeed, if \(\{c\}=\delta\in(0,1)\), take \(k=1\) for \(\delta\ge1/2\), or \(k=\lceil1/(2\delta)\rceil\) otherwise; then \(1/2\le\{kc\}<1\) and the square of a section of valuation \(\lfloor kc\rfloor\) fails the \(2k\) condition by one. For integral \(c\), lower vanishing orders add.

**Exact almost-semigroup model (stronger check):** The genuinely closed semigroup
\[
S=\{(a,k):k\ge1,\;\lceil kc\rceil\le a\le dk\}
\]
is additive because \(\lceil kc\rceil+\lceil\ell c\rceil\ge\lceil(k+\ell)c\rceil\). Its degree-\(k\) slice differs from \(\Gamma_k\) by at most one point, so the actual pseudometric of §19.2 satisfies
\[
d_{\rm sg}(\Gamma,S)=\limsup_{k\to\infty}k^{-1}|\Gamma_k\triangle S_k|=0.
\]
Since \(c<d\), the semigroup cone has positive two-dimensional volume. Its level-one slice, and therefore the partial Okounkov body of this example, is
\[
\boxed{\Delta_D(L,\phi)=[c,d]},\qquad
\operatorname{vol}_{\mathbb R}\Delta=d-c.
\]
The non-pluripolar measure in complex dimension one drops the atom \(c[D]\), giving total mass \(d-c\), exactly as in Eq. 19.4.20. Independently,
\[
k^{-1}h^0(L^k\otimes\mathcal I(k\phi))
=d-c+\bigl(1+\{kc\}\bigr)/k\longrightarrow d-c.
\]
**Boundary:** \(c=d\) has zero mass and is excluded to respect the positive-volume premise in §19.2. This is a new exact example of a **correct** source statement, not a false theorem or a general replacement for §19.4.16. Preserve all distinct source versions and attribution. Proposed addition: a separate worked example following §19.1 or §19.2; downstream checks §§19.4 and 21.13 remain conditional.

## POME-REL-MINIMAL-SUBMEAN-DEFECT-001 — verified conditional deduction, low severity

**Precise source:** docs/sections/relative-canonical-positivity/index.html, blob 2086034ec824b4e9f54143086fda8d8f7fecd297, Lemma 10.105.1, source cao-paun-foliations:3C2C311D, permanent tag 7D9646B80F78, statement lines 12–23, proof/Green identity lines 25–32; downstream occurrence in Theorem 10.105.2 (tag 81245ECD3476), lines 117–120. The relative Bergman and extension arguments in the latter theorem were **not** reexamined.

Let \(M\subset B(a,R)\subset\mathbb C^N\) be a relatively closed smooth complex \(d\)-fold with \(a\in M\), \(n=2d\), \(s=|z-a|\), and \(w\ge0\) smooth and subharmonic. Put
\(I(r)=\int_{M\cap B(a,r)}w\,dV_M\) and \(\Phi(r)=r^{-n}I(r)\).
At every regular radius (hence a.e. radius), the **exact** defect of the monotonicity inequality is
\[
\boxed{\begin{aligned}
r^{n+1}\Phi'(r)
&=r\int_{M\cap\partial B(a,r)}
w\bigl(|\nabla_Ms|^{-1}-|\nabla_Ms|\bigr)\,dA\\
&\quad+\frac12\int_{M\cap B(a,r)}
(r^2-s^2)\Delta_Mw\,dV_M\ge0.
\end{aligned}}
\tag{A}
\]
**Complete derivation:** The printed Green identity gives
\(2r\int_{\partial M_r}w|\nabla_Ms|=2nI(r)+\int_{M_r}(r^2-s^2)\Delta_Mw\).
The exact coarea derivative is
\(I'(r)=\int_{\partial M_r}w/|\nabla_Ms|\,dA\).
Subtract half the former identity from \(rI'(r)\) and use
\(\Delta_Ms^2=2n\), \(|\nabla_Ms|\le1\), \(\Delta_Mw\ge0\).
Since \(\lim_{r\downarrow0}\Phi(r)=v_n w(a)\), \(v_n=\pi^d/d!\), integration of (A) yields the exact nonnegative gap
\[
\frac{I(r)}{v_n r^n}-w(a)
=\frac1{v_n}\int_0^r t^{-n-1}\biggl[
 t\int_{\partial M_t}w(|\nabla_Ms|^{-1}-|\nabla_Ms|)\,dA
+\frac12\int_{M_t}(t^2-s^2)\Delta_Mw\,dV_M
\biggr]dt.
\tag{B}
\]
If \(w(a)>0\) and this gap vanishes at \(r_0>0\), both terms vanish a.e. below \(r_0\). It follows that \(w\) is harmonic, hence strictly positive on the component through \(a\), and \(|\nabla_Ms|=1\) there. Therefore the ambient radial vector is tangent to \(M\). Its inward flow and smoothness at \(a\) force this component inside \(B(a,r_0)\) to coincide with the affine complex plane \(a+T_aM\). Other components, if any, can contribute only with \(w\equiv0\). The converse holds for positive harmonic functions on the affine plane. This rigidity concerns only the nonnegative smooth-subharmonic preliminary step, **not** every continuous \(q\) in the final weighted lemma.

Two sharp checks distinguish the terms. On flat \(M=\mathbb C^d\), \(w=1+\lambda|z|^2\) (\(\lambda\ge0\)), \(I(r)/v_n=r^n+\lambda n r^{n+2}/(n+2)\), so \(rI'-nI=2\lambda n v_n r^{n+2}/(n+2)\), exactly the Laplacian term. On the curved holomorphic graph \(M=\{(z,z^2)\}\subset\mathbb C^2\), \(w=1\), write \(r^2=t+t^2\); induced area integration gives \(I(r)=\pi(t+2t^2)\), hence \(I(r)/(\pi r^2)=(1+2t)/(1+t)>1\), increasing with derivative \(1/(1+t)^2\). Thus curvature alone produces a strict geometric defect. Proposed correction: optional exact identity after the existing Green/coarea proof. **The original lemma was not shown false.**

## POME-TAUT-MODEL-METRIC-EXT-001 — candidate, medium severity

**Precise source:** docs/sections/tautological-metrics-and-maximal-slopes/index.html, blob 313098e0ab266ca5696a16775bc5277539dfe889. Approximate-pseudoeffectivity definition lines 7–9; Theorem 10.108.2, source cao-paun-foliations:E0E0E4DB, permanent tag 9CD904E0945C, lines 28–89; critical open-to-compact passage lines 34–40. Lemma 10.108.1 (source cao-paun-foliations:C1E90EFE, tag C0B465266C15, lines 12–25) only sampled for context.

**Exact unproved transition requiring examination:** The definition supplies a singular tautological metric with curvature at least \(-\varepsilon\Omega_P\) **on an open projective-bundle locus**. The proof then uses its pullback and multiplier ideal on the whole compact common smooth model \(Q\), without an explicit lemma ensuring an extendible quasi-psh weight and the stated uniform error. An open-locus lower curvature bound alone does not imply the desired extension: on a punctured disc, \(u(t)=-\log|t|^2\) has \(dd^c u=0\) yet \(u\to+\infty\), so it cannot extend quasi-psh across the missing divisor (quasi-psh is locally bounded above). This is a **local diagnostic of a missing inference**, *not* a counterexample to Theorem 10.108.2: a controlled alternative choice of metric on its specific model might well exist. Before marking this a true proof gap, establish either a metric-selection/extension lemma with quantitative control as \(m\to\infty\), or an open-locus direct-image approach with rigorous extension of determinants and exceptional corrections. Dependent parts are the definition of \(G_m\), its determinant bound and final saturation-to-\(X\) argument. The separately quoted HPS2017 singular L² direct-image theorem (lines 44–48) is an **unreviewed external/user-deferred analytic input**, not an object of this audit session. Classification remains **candidate**, not a confirmed error or a repair.

## POME-UNIR-FUJIKI-DEFORMATION-INPUT-001 — external dependency, medium severity

**Precise source:** docs/sections/deformation-of-the-canonical-pseudo-effective-cone/index.html, blob 3acd67247638c32f4b4f98f4f5311f0ff554eda1, input paragraph lines 7–10; Corollary 9.77.1, source cao-paun-foliations:73704007, permanent tag 11B2C808741A, lines 12–19. Corollary 9.77.1 uses a quoted **Fujiki1981, Proposition 2.3** deformation theorem for uniruledness in Kähler-dominated smooth proper families. The inference is valid **conditional** on that theorem and the previously tracked §9.76.2: a non-pseudoeffective fiber is uniruled; uniruledness propagates to the central fiber; this contradicts central pseudo-effectivity. The deep relative cycle-space/deformation theorem is neither proved in these passages nor replaceable by mere openness of free rational curves. Retain exact external input and historical attribution; do not relabel Corollary 9.77.1 false. A true internal replacement would need the full stated Kähler family scope.

## Additional actual proof reading and limits

Newly selected checks in §§10.103–10.104: Lemma 10.103.1, source cao-paun-foliations:885C5EE8, permanent tag E897B72A71BA, docs/sections/euler-characteristics-under-flat-twists/index.html, blob 99c65b6051fef34b6ec0b8822c973ab5470bb30a, lines 9–17: finite locally free resolution and Fredholm-index continuity of flat twists. Lemma 10.104.1, source cao-paun-foliations:2FBA7F63, tag EC118288B440, docs/sections/determinants-of-singular-bundle-metrics/index.html, blob 901d6104f4a5ba01b188270bd6e2377ee4baeb9d, lines 9–19: upper bounded dual-matrix entries, convolution scalarization, determinant-trace sign and decreasing limit. These are targeted checks, not complete certification; no new error is claimed. They do not reopen the owner's excluded Demailly/Bergman proof-completion programme.

The new small Python audit check was **actually run**: 266,539 exact rational Hilbert/carry identities, 2,184 distinct nonintegral carry witnesses, seven exact flat-radial identities, and one exact curved-graph derivative passed. Such checks do not prove analytic extension, a general Okounkov theorem, a Fredholm theorem or a geometric deformation theorem. Prior findings, permanent tags, normalization conventions and arbitrary-net requirements are retained. No main/source/registry/tag edits, merge, PR, CI or publication are authorized; proposed fixes belong in a separately reviewable patch.