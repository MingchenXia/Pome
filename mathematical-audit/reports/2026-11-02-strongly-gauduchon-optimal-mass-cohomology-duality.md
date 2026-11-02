# Optimal cohomological mass gap for strongly Gauduchon manifolds

**Finding ID:** POME-SG-MASS-OPTIMAL-DUAL-001  
**Date:** 2026-11-02  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Status:** verified conditional deduction (low; neither a false printed theorem nor an applied repair).  
**Audit branch:** review/mathematical-audit

## Exact integrated anchors and scope

- Current-main reading edition: `docs/sections/locally-conformally-kahler-geometry/index.html`, Git blob `6ebf8e604b45d3eb748037af506145273ca3875d`.
- Definition 23.2.68, source `non-kahler-pluripotential-theory:18572B0D`, permanent tag `ADA9E5EAD64C`, physical lines 1224–1235: positive closed complementary-degree representative and the strongly Gauduchon condition.
- Proposition 23.2.69, source `non-kahler-pluripotential-theory:40B2088A`, permanent tag `4CCB765ECCA2`, lines 1238–1270: the absence of nonzero positive de Rham-exact \((1,1)\)-currents is equivalent to existence of a strongly Gauduchon metric.
- Corollary 23.2.70, source `non-kahler-pluripotential-theory:811BE385`, permanent tag `86E2247D209D`, lines 1280–1303, and equation 23.2.71, source `non-kahler-pluripotential-theory:8F1CE001`, permanent tag `24F2C25D4A8F`, lines 1282–1284: qualitative cohomological mass bound and compactness.
- Theorem 23.2.60, source `non-kahler-pluripotential-theory:B41AA0AF`, permanent tag `DB27896B9A96`, lines 1083–1111: contextual Lee–Gauduchon duality, not needed for the calculation below.

The new proof directly checks the normalized positive-current compactness and the de Rham pairing step used in Corollary 23.2.70, and the Hahn–Banach / exact-current separation logic of Proposition 23.2.69. It does not certify all analytic and cohomological prerequisites, all of §23.2, or the overall project.

## Sharp statement

Let \(X\) be a connected compact complex manifold of complex dimension \(n\ge 2\), \(h\) any Hermitian metric, and \(\|\cdot\|\) an arbitrary norm on the finite-dimensional real vector space \(H^2_{\mathrm{dR}}(X,\mathbb R)\). Write
\[
  M_h(T):=\int_X T\wedge h^{n-1},\qquad
  \mathscr B_h:=\{T:\ T\text{ is a real positive closed }(1,1)\text{-current},\ M_h(T)=1\}.
\]
There are **two separate cases**.

1. If \(\mathscr B_h=\varnothing\), then \(X\) has no nonzero positive closed \((1,1)\)-current at all. Proposition 23.2.69 implies that \(X\) is strongly Gauduchon, and the mass bound is vacuous. There is no minimizing normalized current or positive attained best coefficient; do not silently divide by an infimum over the empty set.
2. If \(\mathscr B_h\ne\varnothing\), its image
\[
  B_h:=\{[T]_{\mathrm{dR}}:T\in\mathscr B_h\}
  \subset H^2_{\mathrm{dR}}(X,\mathbb R)
\]
is a **nonempty compact convex** set, so
\[
  \delta_h:=\min_{T\in\mathscr B_h}\|[T]_{\mathrm{dR}}\|
\]
is attained. The following are equivalent:
\[
 \delta_h>0
 \quad\Longleftrightarrow\quad
 \mathscr B_h\text{ contains no de Rham-exact current}
 \quad\Longleftrightarrow\quad
 X\text{ admits a strongly Gauduchon metric}.
\]
If \(\delta_h=0\), there actually exists a **nonzero positive exact current** of mass one. It is not merely possible to find classes tending to zero while evading an exact-current limit.

In the strongly Gauduchon case with \(\mathscr B_h\ne\varnothing\), the **smallest possible constant** in equation 23.2.71 is
\[
  C_{\mathrm{opt}}(h,\|\cdot\|)=\delta_h^{-1}.
\]
Its sharpness is witnessed by an actual normalized positive closed current \(T_0\), not merely an approximating sequence.

Moreover, there is a smooth real **closed** \((2n-2)\)-form \(\Theta_*\) whose de Rham class defines a norm-one functional on \(H^2_{\mathrm{dR}}(X,\mathbb R)\), such that **one fixed cohomological functional** realizes this optimum:
\[
  \int_X T\wedge\Theta_*
   \ \ge\ \delta_h\,M_h(T)
 \qquad\text{for every real positive closed }(1,1)\text{-current }T,
\]
with equality for a mass-one minimizer \(T_0\). This statement concerns pairings against **closed** positive currents. It does **not** assert that the particular smooth form \((\Theta_*)^{n-1,n-1}\) is pointwise semipositive, and is not a replacement construction of a strongly Gauduchon metric.

## Complete argument for the new quantitative claims

**Normalization and compactness.** Positivity of \(h^{n-1}\) implies \(M_h(T)>0\) for every nonzero positive \((1,1)\)-current \(T\), so every such closed current can be scaled to \(\mathscr B_h\). In local holomorphic charts the coefficients of a positive current are measures, and each is locally dominated by a fixed dimensional multiple of the trace measure \(T\wedge h^{n-1}\). Thus uniformly bounded \(M_h\) yields uniformly bounded coefficient measures. On compact \(X\), weak compactness of those measures, a finite partition of unity, and compatibility of chart overlaps give weak compactness of positive currents of bounded mass. Positivity and \(\mathrm dT=0\) pass to weak limits because they are conditions against fixed smooth test forms; the normalization passes to the limit because \(h^{n-1}\) is fixed and smooth. Hence \(\mathscr B_h\) is weakly compact, with no need to assume that an arbitrary net has a convergent subsequence.

For a finite basis \(\alpha_1,\dots,\alpha_b\) of smooth closed \((2n-2)\)-forms representing \(H^{2n-2}_{\mathrm{dR}}(X,\mathbb R)\), the coordinates of \([T]_{\mathrm{dR}}\) are obtained via \(\int_XT\wedge\alpha_i\) and Poincaré duality. Each coordinate is weakly continuous. Therefore the image \(B_h\) is compact, and it is convex because both positivity, closedness, and \(M_h(T)=1\) are stable under convex combinations. The continuous norm attains its minimum at some \(c_0=[T_0]\in B_h\).

**Exactness and the positive gap.** The equality \(\delta_h=0\) holds precisely when \(0\in B_h\), by compactness and attainment. A positive closed current in \(\mathscr B_h\) has de Rham class zero precisely when it is de Rham exact in the complex of currents. This is the exact-current obstruction appearing in Proposition 23.2.69. If no such current exists, the compact set \(B_h\) avoids zero and \(\delta_h>0\); no unproved interchange of varying currents and test functions occurs.

**Optimal mass estimate.** Given \(T\ne0\), divide it by \(M_h(T)\). The definition of \(\delta_h\) yields
\[
   \|[T]_{\mathrm{dR}}\|
   =M_h(T)\left\|\left[T/M_h(T)\right]_{\mathrm{dR}}\right\|
   \ \ge\ \delta_h M_h(T).
\]
At \(T=T_0\), equality holds. Hence no coefficient smaller than \(1/\delta_h\) can satisfy the mass estimate uniformly.

**An optimal dual class.** Work in the finite-dimensional space \(E=H^2_{\mathrm{dR}}(X,\mathbb R)\). The compact convex set \(B_h\) lies outside the open norm ball \(U=\{c\in E:\|c\|<\delta_h\}\). By separation of a compact convex set and a disjoint open convex set, a nonzero linear functional \(\ell\) satisfies
\[
  \inf_{b\in B_h}\ell(b)\ \ge\ \sup_{u\in U}\ell(u)
    =\delta_h\|\ell\|_*.
\]
After normalization to \(\|\ell\|_*=1\), it follows that \(\ell(b)\ge\delta_h\) for all \(b\in B_h\). On the minimizer \(c_0\), duality gives \(\ell(c_0)\le\|c_0\|=\delta_h\), hence equality. Poincaré duality represents \(\ell\) by a class in \(H^{2n-2}_{\mathrm{dR}}(X,\mathbb R)\), for which a smooth closed real representative \(\Theta_*\) may be chosen. Homogeneity then proves the asserted pairing for every positive closed current. This is a finite-dimensional separation step, independent of any claim about smooth pointwise positivity of \(\Theta_*\).

**Explicit normalization check.** Let \(X=\mathbb P^n\), \(h\) a Fubini–Study form normalized by \(\int_Xh^n=1\), and assign \(\|a[h]\|=|a|\) to its one-dimensional \(H^2_{\mathrm{dR}}\). Every positive closed \(T\) has \([T]=a[h]\), with \(a=M_h(T)\ge0\); consequently \(B_h=\{[h]\}\), \(\delta_h=1\), and \(C_{\mathrm{opt}}=1\). The bound is attained by \(T=h\). The normalization agrees exactly with equation 23.2.71 and does not hide a factor \(n!\).

## Assessment of the printed proof and dependencies

- **No confirmed false printed statement or missing proof step** was found in the selected lines of Proposition 23.2.69 and Corollary 23.2.70. In Proposition 23.2.69, the kernel of \(\mathrm d\) among smooth complementary-degree forms is a closed subspace of the Fréchet space, and the cone of forms with strictly positive \((n-1,n-1)\)-part is open and convex. The separation functional is a degree-two current; its annihilation of all closed forms forces it to be both closed and de Rham exact, while nonnegativity on the cone forces type \((1,1)\) and positivity. This is a valid separation scheme; its functional-analytic background is not wholly recertified here.
- In Corollary 23.2.70, the use of a **fixed** Hermitian trace form and **fixed smooth cohomology tests** justifies passing to weak limits. It does not justify arbitrary varying-test convergence; none is required.
- The new optimal constant and optimal cohomology functional are **additional deductions**, not a patch to either original result. If inserted, they fit after equation 23.2.71, with the empty normalized-current case stated explicitly.
- Theorem 23.2.60 and the wider Lee–Gauduchon cone material were checked for compatibility, not newly certified. The preexisting Calabi–Eckmann/positive-exact-current model of Example 23.2.72 is not registered anew as a finding.

**Affected dependents:** Corollary 23.2.70's mass inequality, compact-base and closed-image-cone claims, plus uses of a cohomological mass gap for weak compactness. The printed results remain unchanged. The foundational positive-current compactness and Poincaré duality are accepted as existing internal inputs; there is **no** reliance on the author-deferred Demailly regularization, Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof programmes.

**Coverage:** direct selected proof-level check of §§23.2.68–70, including the exact empty-set case and dual optimizer; §23.2 was already partially reviewed. No first-reviewed numbered section, full-section certification, CI/build/test/formal verification, or production change.
