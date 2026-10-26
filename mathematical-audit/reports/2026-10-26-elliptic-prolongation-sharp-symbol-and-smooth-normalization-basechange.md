# Selected audit: elliptic-system prolongation and smooth-base normalization

**Date:** 2026-10-26 (Asia/Shanghai). **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** first focused proof-level review of nonexcluded §§2.20 and 9.11, with an incremental §9.4 normalization crosscheck. Not a whole-section certification, and not a verification of every transitive dependency.

The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, neither reopened nor certified. The elliptic operator in §2.20 is a separate PDE/unique-continuation subject, not that excluded programme.

## POME-ELLIPTIC-PROLONG-EXACT-DEGEN-001

**Severity:** low. **Status:** verified conditional deduction (printed proposition correct). **Proposed placement:** optional remark after Proposition 2.20.11. **Affected dependents:** quantitative domains on which the rank-three elliptic prolongation can be used; not the support/flatness construction in Theorem 2.20.4.

**Precise current reading edition:** docs/sections/elliptic-systems-and-unique-continuation/index.html, blob 7e1c07728654308341d90c33f05873112c53052c. Proposition **2.20.11**, source label **demailly-complex-geometry-099B86A5**, permanent tag **CE8EC0706B26**, lines 178–259; its principal-symbol calculation and determinant occur in the proof, approximately lines 208–255. Theorem **2.20.4**, source **demailly-complex-geometry-F727EAB3**, permanent tag **2D8A7E49E474**, lines 54–174, supplies the application.

**Exact improvement.** The printed proposition establishes ellipticity on any open subset of the strip |t|<1. The *same* operator formula has an elliptic principal symbol at every point with t²≠2, including the regions |t|>sqrt(2). The only possible degeneracy occurs at t=±sqrt(2), and is attained.

**Proof.** At a real covector (tau,xi), the lower triangular second-order principal matrix has diagonal (b,b,a), with

\[
 a=(\tau-i\xi)^2+i t^2\xi^2,\qquad
 b=(\tau-i\xi)^2-i t^2\xi^2.
\]

Consequently det sigma₂ = b²a, independently of the lower-order coefficient f and of the off-diagonal entry q. If xi=0 and tau≠0, then a=b=tau²≠0. If xi≠0, put r=tau/xi and k=t²≥0. Direct expansion gives

\[
 \xi^{-2}a=(r^2-1)+i(k-2r),\qquad
 \xi^{-2}b=(r^2-1)-i(k+2r).
\]

Thus a=0 requires r²=1 and k=2r, hence **r=1, k=2**. Similarly b=0 requires r²=1 and k=-2r, hence **r=-1, k=2**. Conversely these covectors give zeros. This is an exact characterization; in particular ellipticity returns on the other side of the two degenerate t-levels. On each compact subset of the complement of those levels, continuity of the normalized symbol on the unit cotangent circle gives a positive uniform lower singular-value bound. No claim of a uniform bound across t²=2 is possible.

A small independent symbolic check was **actually run**, using SymPy on a polynomial test function: the source's operator identity
AB = D⁴+t⁴∂x⁴−4it∂x²D−2i∂x²
and the ensuing identity P₀=AB+Q∂x both simplified to zero residual. This checks these algebraic identities on that test function, **not** a general formal proof or project build. The exact zero-set proof above is independent and symbolic.

**Limits.** This does not change the statement of Proposition 2.20.11, and it does not extend the specially constructed modes or their gluing past the original small interval. The source's sufficient restriction |t|<1 is valid, merely not optimal for principal-symbol ellipticity.

## POME-NORMALIZATION-SMOOTH-BASE-001

**Severity:** low. **Status:** verified conditional deduction, *conditional on the validity of the normalization theorem*; does not resolve an existing proof defect. **Proposed placement:** optional lemma after Theorem 9.4.6 or as a prerequisite note to the singular-space descent §9.11. **Affected dependents:** normalizations of analytic families obtained by adjoining a smooth parameter; comparison of singular-space constructions with smooth parameter factors.

**Precise current reading edition:** docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html, blob 06439f43d1ce8e83d2529682c9a630bffa3d9c22: Proposition 9.4.3 (source foundations-of-pluripotential-theory-AC231B8D; permanent tag **36422A732754**), lines 55–79; normality criterion and Lemma 9.4.4 (source foundations-of-pluripotential-theory-E60680A7; permanent tag **D73CC9F08C05**), lines 83–108; Theorem **9.4.6** (source foundations-of-pluripotential-theory-7042BB57; permanent tag **12A47DB401E2**), lines 141–160. Related resolution descent is Theorem **9.11.5** (source non-kahler-pluripotential-theory-1FFF5E71; permanent tag **F4C06D21AA94**), docs/sections/potentials-and-equations-on-unibranch-spaces/index.html, blob fa1475ba7cd3b71cf195e91c45b5719b517bb0ae, lines 61–95.

**Precise assertion.** Let X be any reduced complex space in the stated conventions, let nu: Xtilde→X be its normalization, and let S be a complex manifold. Then

\[
 \nu\times \mathrm{id}_S:
 \widetilde X\times S\longrightarrow X\times S
\]

is a normalization. No properness or compactness of S is required. This is a product with a **smooth complex parameter**, not an assertion about arbitrary singular base changes.

**Proof.** First prove that the product of a normal complex space Z with a manifold S is normal, directly from the weakly holomorphic criterion of §9.4. Work locally with S a polydisc D centered at 0. Let F be weakly holomorphic on Z×D. On the dense manifold Z_reg×D it is holomorphic. Near any (z₀,0) choose a smaller V×D_R on which F is bounded on (V∩Z_reg)×D_R (shrinking around the compact parameter torus gives a uniform bound M). For each multi-index alpha define on V∩Z_reg the Cauchy coefficient

\[
 c_\alpha(z)=\frac{1}{(2\pi i)^m}
 \int_{|\zeta_1|=R_1}\cdots\int_{|\zeta_m|=R_m}
 \frac{F(z,\zeta)}{\prod_j\zeta_j^{\alpha_j+1}}\,
 d\zeta_1\cdots d\zeta_m .
\]

The coefficient is holomorphic on V∩Z_reg and locally bounded near Z_sing, hence weakly holomorphic on V and therefore extends holomorphically to V by normality. The Cauchy bound |c_alpha|≤M product R_j^{-alpha_j} remains true on V by density and continuity. Consequently the power series sum c_alpha(z)w^alpha converges uniformly on V×D_r for every r_j<R_j; its sums are holomorphic on the complex space product, and on Z_reg×D_r it equals F by Cauchy's formula. This gives an ordinary holomorphic extension of every weakly holomorphic germ on Z×D, proving normality by Proposition 9.4.3 and the stated criterion.

Next, nu×id_S is finite: finite fibers are unchanged, and properness follows by viewing the inverse image of a compact K⊂X×S as a closed subset of the compact set nu^{-1}(pr_X K)×pr_S K. It is bimeromorphic and an isomorphism over X_reg×S. Since its source is normal, Theorem 9.4.6's uniqueness characterization identifies it as the normalization of X×S. Fiber cardinalities and irreducible-branch counts are unchanged upon adjoining S. QED.

**Verification boundary.** This is **not** a repair or certification of the pre-existing **POME-NORM-COUNTABLE-COVER-001** defect in the globalization/countability step of the printed proof of Theorem 9.4.6. That earlier ID and its unresolved status remain intact. The theorem itself is used here as a conditional input; the local product-normality calculation is independent of the globalization step.

## Other passages actually checked (no new error ID)

- **§2.20:** Lemma 2.20.1 (tag **CB1875F07408**, lines 7–53), including positive fourth-order modes and monotone comparison; Theorem 2.20.4 (tag **2D8A7E49E474**, lines 54–177), including the scaling Δ_n~(11/16)n^{-27/16}, G_n~(11/16)^{1/4}n^{29/16}, r_nG_n~constant n^{1/8}, cutoff dominance and flat extension; Proposition 2.20.11 (tag **CE8EC0706B26**, lines 178–261), especially commutator sign and triangular principal symbol; Corollary 2.20.12 (tag **1ADDDDB90B14**, lines 262–273). These are *selected proof checks*, not independent PDE theorem certification. No new false statement was found.
- **§9.11:** Definition 9.11.2 (tag **76A75EB639CB**, lines 37–44), Lemma 9.11.3 (tag **E7163CA56764**, lines 45–55), Theorem 9.11.5 (tag **F4C06D21AA94**, lines 61–95), Proposition 9.11.7 (tag **622B386B559D**, lines 101–124). Checked the local smooth correction for a nonclosed Hermitian background, the use of connected proper fibers and disk lifting, and the proof that usc envelope regularization commutes with pullback via both inequalities on preimages of neighborhoods. The Fornaess–Narasimhan converse of §9.10.13 (tag **48473380B913**) is the **existing unresolved external dependency POME-UNI-EXT-FN-001**, not reclassified as proved.
- **§9.4:** Precisely the indicated normalization statements, only as an incremental crosscheck for the second new deduction. The existing 9.4 proof-gap status is preserved. No complete chapter or full transitive dependency chain certified.

**Editorial decisions:** only suggest mathematical additions; do not change source HTML, canonicalization, registry, fixed tags, main, PRs, CI or publication. Earlier findings remain unchanged.