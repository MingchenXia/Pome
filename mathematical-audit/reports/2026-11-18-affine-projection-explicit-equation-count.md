# A fixed effective list of equations for linearly bounded finite analytic projections

**Date:** 2026-11-18. **Finding:** `POME-AFFINE-PROJECTION-EXPLICIT-EQUATION-COUNT-001`. **Severity:** low; **status:** **verified conditional deduction**. The printed §9.61 statements remain correct. The new part is a *uniform explicit finite selection of linear forms*, avoiding the nonconstructive Noetherian selection used in the printed converse. This is not a claim of complete certification of upstream Remmert/finite-map theorems.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.

## Integrated source and precise anchors

- `docs/sections/affine-algebraicity-and-linear-growth/index.html`, main blob `8f2301f7696a0b230950918ae20a7f9e57be768b`. §9.61 heading permanent `5E34E9D63326`; subsection 9.61.1 permanent `C47741356AF4`, lines **5–8**. Lemma **9.61.2**, source `demailly-complex-geometry:F8362024`, permanent `D8FA405BDFAC`, lines **10–29**, with cone condition 9.61.3 source `demailly-complex-geometry:7EDA0F03`, permanent `D6D620F9E57D`, lines **12–16**. Theorem **9.61.4**, source `demailly-complex-geometry:A33B88FE`, permanent `D15F5F84A74A`, lines **31–63**, especially coefficients/finite fiber argument lines **44–60**. Corollary **9.61.5**, source `demailly-complex-geometry:853EA48D`, permanent `A30D3E21C6D2`, lines **65–79**; Proposition **9.61.6**, source `demailly-complex-geometry:E636F24A`, permanent `05AC0FB85B88`, lines **81–93**.
- Conditional internal inputs in §9.61.2 lines 22–26: finite-open-map theorem (proof entry `776A532CD79E`), analytic critical locus (§6.38.1), Remmert proper mapping theorem (proof entry `0FC675348681`), dimension bounds (`A814C831E915`), and connectivity of the complement (`AA4164301998`). Section 9.58.2 is the internal Noetherian/Nullstellensatz input; the new finite selection below does **not** need its Noetherian part.

## Exact strengthened statement

Let \(1\le p<n\) and \(r=n-p\). Let \(A\subset \mathbb C^p_z\times\mathbb C^r_w\) be a **nonempty, closed, reduced, pure p-dimensional analytic set** satisfying
\[
 |w|\le C(1+|z|)\qquad ((z,w)\in A).
\]
As in printed Lemma 9.61.2, the projection \(\pi:A\to\mathbb C^p\) is finite, proper, surjective, and has \(d\ge1\) distinct sheets away from its proper analytic branch set. Put
\[
 N=d(r-1)+1
\]
and choose **any N distinct** complex scalars \(t_1,\ldots,t_N\). Define the fixed vertical linear forms
\[
 \ell_t(w)=w_1+t w_2+\cdots+t^{r-1}w_r.
\]
For every selected \(t=t_j\), let \(P_t(z,T)\) be the monic degree-\(d\) polynomial of fiber values of \(\ell_t\), extended holomorphically across the discriminant as in printed Theorem 9.61.4, and define
\[
 F_t(z,w):=P_t(z,\ell_t(w)).
\]
Then **every \(F_t\) is a polynomial of total degree at most \(d\)**, and the entire analytic set has an explicit presentation
\[
 \boxed{A=\bigcap_{j=1}^{d(r-1)+1}\{F_{t_j}=0\}.}
\]
Thus at most \(d(r-1)+1\) explicitly chosen degree-at-most-\(d\) polynomials suffice. This is an *upper bound*, not a universal minimal number of defining equations. In the case \(r=1\), a single monic degree-\(d\) polynomial suffices. For \(p=0\), the same argument works directly with \(d=\#A\) and no branch set; if \(r=0\), the nonempty pure \(n\)-dimensional closed analytic set is all of \(\mathbb C^n\) and needs no equations.

## Complete finite-selection proof

**1. The common polynomial construction and degree.** Over the unbranched locus the d-sheeted fiber gives
\[
 P_t(z,T)=\prod_{a\in\pi^{-1}(z)}(T-\ell_t(a_w))
        =T^d+\sum_{j=1}^d c_{t,j}(z)T^{d-j}.
\]
The cone inequality bounds each fiber root by \(C\|\ell_t\|(1+|z|)\). The symmetric functions therefore obey
\[
 |c_{t,j}(z)|\le {d\choose j}(C\|\ell_t\|)^j(1+|z|)^j.
\]
Local bounded removability across the proper analytic branch set makes \(c_{t,j}\) entire; Cauchy's estimates on arbitrarily large polydiscs imply
\(\deg c_{t,j}\le j\), exactly as in the printed proof at physical lines 50–56. Consequently \(F_t(z,w)=\sum_{j=0}^dc_{t,j}(z)\ell_t(w)^{d-j}\), with \(c_{t,0}=1\), has **total degree at most d**. The proof uses neither an unproved exchange of limits nor a regularization theorem.

**2. The root-set containment at branch fibers.** Fix \(z_0\) in the base, possibly in the branch set. Choose unbranched \(z_\nu\to z_0\). By the uniform cone bound and properness, all d points of \(\pi^{-1}(z_\nu)\), counted on the generic sheets, lie in a compact set after shrinking the base neighborhood. Label them arbitrarily and pass to a diagonal subsequence so all d converge to points of the closed fiber \(\pi^{-1}(z_0)\), repetitions allowed. Coefficient continuity then implies **every root** of \(P_t(z_0,T)\) is \(\ell_t(a_w)\) for some \(a\in\pi^{-1}(z_0)\). In particular the fiber has at most d distinct points. Conversely \(P_t(z,\ell_t(w))=0\) for all \((z,w)\in A\): it is true on the dense unbranched part and extends by continuity; density follows from pure dimensionality and local openness as established in Lemma 9.61.2.

**3. A predetermined finite list separates every outsider.** Fix \((z_0,b)\notin A\). Its base fiber has \(q\le d\) distinct vertical points \(a_1,\ldots,a_q\), none equal to \(b\). For each difference \(v_i=b-a_i\ne0\), the scalar polynomial
\[
 Q_i(t):=\ell_t(v_i)=\sum_{k=1}^r(v_i)_k t^{k-1}
\]
is nonzero and has degree at most \(r-1\). Hence at most \(r-1\) of the N preselected distinct t-values obey \(\ell_t(b)=\ell_t(a_i)\). The union of these forbidden values over all \(q\le d\) points has cardinality at most \(d(r-1)\), strictly less than \(N\). Choose a remaining \(t_j\). Its value \(\ell_{t_j}(b)\) differs from the values of \(\ell_{t_j}\) on **every** point of the fiber. By the preceding root-set description,
\[
 F_{t_j}(z_0,b)=P_{t_j}(z_0,\ell_{t_j}(b))\ne0.
\]
Thus no outsider belongs to all N zero sets. Together with the inclusion in step 2, the boxed equality follows.

The proof is elementary after the **explicitly named internal finite-projection and holomorphic-extension inputs**. It replaces the Noetherian last step in the printed proof with a finite Vandermonde-type separation count. It does not assert these finitely many polynomial equations generate the *full nonreduced defining ideal*; they define the same **reduced zero set**, respecting the source's analytic/algebraic distinction.

## Direct audit of the other three statements and dependency boundary

- **Lemma 9.61.2 (lines 21–27):** the cone bound gives properness, compact analytic fibers are finite, the finite-open-map theorem gives surjectivity, and critical image removal produces a finite covering. The component count via finitely many local branches in a fixed fiber is logically valid. Remmert, dimension and finite-open-map inputs remain *internal results assumed*, not independently re-established.
- **Forward Theorem 9.61.4 (lines 37–42):** projective closure and generic kernel avoidance yield the uniform cone bound; the incidence estimate has dimension at most \(np-1\) against an \(np\)-dimensional matrix parameter space. Analytic closure and stratification are explicit inputs, not certified from scratch.
- **Corollary 9.61.5 (lines 71–77):** induction by defining polynomials correctly handles mixed dimensions, empty components and the pure codimension-one zero set of a nontrivial polynomial. Its conclusion that algebraic and analytic irreducible components agree is conditional on the proved finite-cover/algebraicity inputs.
- **Proposition 9.61.6 (lines 87–91):** polynomial factoriality via Gauss lemma and the strong Nullstellensatz imply distinct irreducible factors have prime radical ideals. The global analytic component conclusion then uses Corollary 9.61.5; none of these implications confuses irreducible schemes with nilpotent multiplicities.

These are **full direct checks of all displayed proof arguments in §9.61**, while the full network of their named upstream inputs is not certified. No printed mathematical error or proof gap was found in the inspected steps. The earlier finding `POME-AFFINE-FINITE-GROWTH-EXPONENT-001` (2026-11-03) independently extends the exponent \(s\) and sharpens coefficient-degree bounds; **it does not give this predetermined finite equation-count bound**, and its previous status is unchanged.

## Classification, dependents, proposal, coverage

**Status:** low / verified conditional deduction. The concrete finite equation list and total-degree bound are fully proved conditional on printed §9.61.2/4 input lemmas; the **whole section's direct proofs** were inspected, but no transitive global proof certificate is claimed. No false theorem, missing regularization proof, incompatible canonicalization, or genuine duplicated existing theorem was established.

**Proposed optional patch (not applied):** after Theorem 9.61.4, state the fixed \(d(r-1)+1\) evaluation-grid corollary as a separate remark, retaining source labels, historical attribution and old permanent tags. It may make §9.61's set-theoretic algebraicity certificate effective. Potential dependents include §9.61.5 and §9.61.6 (component and factorization logic) and future finite-projection algorithmic uses; **not** claims of a bound on minimal generators of an analytic ideal or the number of local branches.

**Coverage:** §9.61.1–6 were all directly checked in the present reading; §9.58.2 and named proper finite map/Remmert/analytic closure inputs were only identified/assumed. The previous §9.61 audit was selected, so **+0 first proof-visited numbered sections, +1 whole-section *direct* proof inspection (§9.61), +0 full upstream-chain certification**. Baseline ToC 25 chapters/747 numbered sections (not independently recounted in this report). No project tests, builds, CI, formal verification, or publication. Demailly approximation and dedicated Bergman/L2/OT/multiscale-atlas/positivity-loss proof programme remains **deferred-by-user**.
