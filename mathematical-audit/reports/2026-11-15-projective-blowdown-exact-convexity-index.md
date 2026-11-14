# Exact smooth convexity index of a product tautological blowup

**Date:** 2026-11-15. **Stable finding:** POME-PROJ-COMP-BLOWDOWN-EXACT-Q-001. **Severity/status:** low / verified conditional deduction (an exact geometric strengthening of an already documented counterexample, *not* a newly detected false theorem). **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit.

## Pinned integrated edition and distinct earlier work

- Section 11.18, file docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html; blob fab309d460a8411fefcd1ef32a094927d6feea10. The projective-line convention and the removed zero section are at physical lines 19–25. Lemma 11.18.1 (source non-kahler-pluripotential-theory:F8D5B741; permanent tag 5022159B8350), lines 28–45, concerns curvature/Levi eigenvalues. Theorem 11.18.2 (source non-kahler-pluripotential-theory:9BF81039; permanent tag B93CB03C68B7), lines 50–68, claims (n+r-s)-convexity without stating compactness of the base; its proof uses compactness at line 67. Corollary 11.18.4 (source non-kahler-pluripotential-theory:B119F64B; permanent tag 18D33491ABFD), lines 91–105, cites it.
- Section 11.17, file docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--concave-neighborhoods-and-dual-norms/index.html, blob d49b7d4f2a213c8b70abfe2f337562202bb58dfb, physical line 129: a complex N-fold is q-convex when it admits a smooth proper exhaustion with at least N-q+1 positive Levi eigenvalues outside a compact subset.
- **Historical finding retained, not recounted:** POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001, high / confirmed error, in reports/2026-11-11-projective-complement-noncompact-escaping-compact-fibers.md. That report proved non-2-convexity for a family with a one-dimensional noncompact factor, and proposed the compact-base repair. The present finding computes the **entire optimal convexity threshold for any number of noncompact affine factors**, and supplies a globally proper, explicitly ranked Levi exhaustion. It neither replaces nor weakens the earlier high-severity finding.

## Exact theorem and hypotheses

Fix integers d,m >= 1. Set
\[
 B=\mathbf P^d,\qquad X=B\times\mathbf C^m,\qquad
 E=\mathrm{pr}_B^*\mathcal O_{\mathbf P^d}(1),\qquad r=1 .
\]
Take the pulled-back Fubini–Study Hermitian metric h on E and let
\[
 U_E=\mathbf P(\mathcal O_X\oplus E)\setminus\mathbf P(\mathcal O_X).
\]
Then the least smooth convexity index of U_E, in the **precise definition of §11.17, line 129**, is
\[
 \boxed{\quad q_{\min}(U_E)=d+1 .\quad}
\]
The curvature coefficient form appearing in Theorem 11.18.2 has exactly d strictly positive directions and m null directions at every nonzero fiber vector. The unqualified printed theorem would therefore yield q=m+1; this is false whenever d>m. That false consequence is a parameterized instance of the **previously confirmed error**, not a second discovery of that error.

## Complete geometric identification

The projective-bundle convention used on line 25 of §11.18 parametrizes lines in \(\mathcal O_X\oplus E\). A point of U_E has homogeneous notation \([u:v]\) with \(v\in E_x\setminus\{0\}\) (whereas the removed section is \(v=0\)). Dividing by v gives the fiber-independent linear map \(v\mapsto u\), i.e. a point in \(E_x^*=\mathcal O_{\mathbf P^d}(-1)_{[z]}\). In local trivializations this is a holomorphic change of coordinates with holomorphic inverse; hence
\[
 U_E\simeq \mathrm{Tot}(\mathcal O_{\mathbf P^d}(-1))\times\mathbf C^m.
\]
The tautological line bundle is the closed incidence variety
\[
 Y=\{([z],w,t)\in\mathbf P^d\times\mathbf C^{d+1}\times\mathbf C^m:
                  w\in\mathbf C z\}.
\]
Here z is any nonzero representative of [z]; the relation \(w_i z_j=w_j z_i\) shows that Y is a closed complex submanifold of dimension \(N=d+m+1\). Its map
\[
 \pi:Y\longrightarrow\mathbf C^{d+1}\times\mathbf C^m,\qquad
       ([z],w,t)\longmapsto(w,t)
\]
is holomorphic and **proper**. Indeed for a compact K in the target, \(\pi^{-1}(K)\) is closed in the compact space \(\mathbf P^d\times K\). Over w nonzero the projective direction [z]=[w] is forced, and \(\pi\) is a biholomorphism. Its exceptional locus is
\[
 D=\{w=0\}\simeq\mathbf P^d\times\mathbf C^m.
\]
This is the blowup of the affine subspace \(\{0\}\times\mathbf C^m\) in \(\mathbf C^{d+m+1}\), but the proof does **not** depend on any blowup theorem.

## Constructive upper bound: a globally proper exhaustion with exact Levi rank

Define
\[
 \Phi([z],w,t)=\|w\|^2+\|t\|^2.
\]
Because \(\pi\) is proper and the squared Euclidean norm is a proper function on the affine target, \(\Phi\) is a **smooth proper exhaustion of all of U_E**, with no compact exception necessary. Its Levi form is the pullback by \(\pi\) of the positive Euclidean Hermitian form on \(\mathbf C^{d+m+1}\). Thus its number of positive eigenvalues is the complex rank of \(d\pi\).

Off D, \(\pi\) is biholomorphic, so the rank is N. At a point of D choose the affine chart \([z]=[1:\zeta_1:\cdots:\zeta_d]\) and the tautological fiber coordinate \(\lambda\), so that
\[
 w=\lambda(1,\zeta_1,\ldots,\zeta_d),\qquad
 \pi(\zeta,\lambda,t)=\bigl(\lambda,\lambda\zeta_1,\ldots,
                     \lambda\zeta_d,t_1,\ldots,t_m\bigr).
\]
At \(\lambda=0\), all d derivatives with respect to \(\zeta_i\) vanish, the derivative in \(\lambda\) is nonzero, and the m derivatives in t are independent. Hence
\[
 \operatorname{rank}_{\mathbf C}d\pi=
 \begin{cases}
 d+m+1,&\lambda\ne0,\\
 m+1,&\lambda=0.
 \end{cases}
\]
Equivalently the Levi form of \(\Phi\) has **exactly m+1 positive directions on D and N positive directions off D**, including the points at projective infinity in the original projective-bundle presentation. Since
\(N-(d+1)+1=m+1\), this proves \((d+1)\)-convexity.

This calculation is not the printed radial cutoff \(\chi(G)/G\), which is not proper over a noncompact base; it is an independent global exhaustion descending from the blowdown.

## Optimal lower bound against every possible exhaustion

Let \(\Psi\) be **any** smooth real exhaustion on U_E and let K be **any** compact subset. The projection of K to the \(\mathbf C^m\) coordinate is compact. Choose \(t\in\mathbf C^m\) outside that projection, and let
\[
 Y_t=\{([z],0,t):[z]\in\mathbf P^d\}\simeq\mathbf P^d\subset U_E.
\]
It is a compact complex submanifold disjoint from K. The restriction of \(\Psi\) to \(Y_t\) has a global maximum at some p. Consequently the ambient Levi form of \(\Psi\) at p is nonpositive on the d-dimensional complex tangent \(T_pY_t\). A positive-definite complex subspace for that Levi form has zero intersection with \(T_pY_t\), and therefore dimension at most \(N-d=m+1\). Thus \(\Psi\) has at most m+1 positive Levi eigenvalues somewhere outside **every** compact K.

If q<=d, q-convexity would demand at least \(N-q+1\ge N-d+1=m+2\) positive Levi eigenvalues outside a suitable compact K, a contradiction. Thus q>=d+1 for every smooth q-convex exhaustion. Together with the constructed \(\Phi\), this gives \(q_{\min}=d+1\).

## Comparison with the printed curvature criterion and dependents

The curvature of the pulled-back Fubini–Study metric on E is positive definite along the d-dimensional projective factor and vanishes in the m affine-base directions. Therefore the form \(\alpha_{h,v}\) of §11.18 has exactly s=d positive eigenvalues at every nonzero v. With n=d+m and r=1, the printed Theorem 11.18.2 predicts q=n+r-s=m+1. The exact calculation shows it is valid for this model only when \(m+1\ge d+1\), i.e. m>=d, and fails when d>m. This reinforces **the same existing theorem error**, without reclassifying it or pretending to find another independent false theorem.

**Proposed textual correction (not applied):** require compact X in Theorem 11.18.2 and have Corollary 11.18.4 inherit that hypothesis, or prove an appropriately different noncompact theorem with a base exhaustion and explicit mixed Levi count. The true model-specific statement proved here remains valid for arbitrary d,m>=1. The compact-base replacement proved in the 2026-11-11 report is unaffected. Potential downstream uses of §11.18 in §§11.19–11.21 must retain the compact-base caveat; these have not been transitively reviewed in this session.

## Classification, exact coverage and exclusions

**POME-PROJ-COMP-BLOWDOWN-EXACT-Q-001:** **low / verified conditional deduction** (with an elementary self-contained proof of the model), not a new separate confirmed error or an automatic repair of the printed theorem. The parameterized family, global proper blowdown exhaustion, Levi rank m+1 on the exceptional locus, and *optimal* q=d+1 were verified. The already known high-severity POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001 remains a separate, unchanged **confirmed error**. Both §§11.17 and 11.18 were already partially inspected: **0 new first proof-level section visits and 0 whole-section certifications**. The current chapter/section catalogue remains 25/747, with no claim of all-section proof checking. No builds, software tests, CI, formalization or site publication were run; no main, source, registry, canonical tag or mathematical body was edited. All owner-excluded Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss projects remain **deferred-by-user**, neither repaired nor certified.
