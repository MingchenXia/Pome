# Sharp Hausdorff stability of real-convex Siciak extremals

**Audit date:** 2026-10-24 (Asia/Shanghai). **Freshly read main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `e543f66bdfa7475a80d56233c6d3c02584334469`.

**Scope and exclusions.** First selected proof-level direct reading of integrated §§16.30, 16.31 and 16.33. The separate §7.10.1–2 Bedford–Taylor capacity/Dirichlet proof was checked for cross-context (not newly marked as an unreviewed section and not re-registered as a new finding). No entire section, external analytic predecessor, or completed source theorem chain is certified. In particular, the dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**, neither repaired nor certified. No part of that programme was examined.

## Exact integrated anchors and prerequisites

1. **Theorem 16.33.6**, label `klimek-pluripotential-theory-545185F6`, permanent tag `A1B73D6E87D0`, `docs/sections/real-compact-sets-and-explicit-extremal-formulas/index.html`, **main blob `a5f8e9cd6aa60a22f344aadbdf8370422ce3220a`, physical HTML lines 101–126**. For a real compact convex centrally symmetric body \(E\subset\mathbb R^n\) containing \(0\) in its real interior, it states the **unregularized** formula
   \[
   V_E(z)=\max_{y\in E^\circ}g(y\cdot z),
   \]
   where \(g=V_{[-1,1]}\) is the continuous one-variable Joukowski extremal defined just before Proposition 16.33.3 (same path, lines 37–48). We checked the polar-separation argument, the filled-ellipse inverse, the real boundary condition \(J_c(S^1)\subset E\), and the exterior puncture removable-singularity/maximum-principle step. It remains an *internal theorem used conditionally*, not a complete transitive certification.
2. **Propositions 16.33.1, 16.33.3–5, 16.33.7**, respective permanent tags `C39B105D9256`, `227A1367C31C`, `D47F294B7F7D`, `F36E879B8976`, `E41A4DC7736D`; same HTML, lines 7–28, 49–100 and 127–153. Selected checks: real quadratic polynomial separators; the exterior \(J_c\) injectivity factorization; the radial harmonic annulus and integral winding step; disc subharmonic comparison; covariance and the degree-two preimages of the simplex and cross. We did not claim a complete proof audit of all interpolation/functional analytic predecessors elsewhere.
3. **Theorem 16.30.5**, label `klimek-pluripotential-theory-485FC789`, tag `E171A0405847`, `docs/sections/polynomial-descriptions-of-logarithmic-envelopes/index.html`, blob `15d7e0207da1d72653382a1512ca380311b5d5e3`, **lines 93–129**. Directly checked the polynomial-norm extremal convention, zero-polynomial/zero-norm cases, and the \(P^t\) elimination of subexponential binomial factors for products. The norm-ball formula (Proposition 16.30.1, tag `F5C5050EEDEB`, lines 10–34) and compact-extremal regularity (Proposition 16.30.2, tag `F983146D5FCD`, lines 35–52) were checked as context; the domain-of-holomorphy inputs in Theorems 16.30.3–4, lines 53–92, remain genuine unverified upstream inputs.
4. **Theorem 16.31.3**, label `klimek-pluripotential-theory-A80EBCDF`, tag `E215D05E52EC`, `docs/sections/logarithmic-families-and-a-fixed-ball-capacity/index.html`, blob `98d00aa7b2db4f81163a56d6f448946fd0c75499`, **lines 58–85**: the fixed-test-ball generalized capacity \(\alpha_B(E)=\exp(-\sup_BV_E^*)\). **Proposition 16.31.4**, label `klimek-pluripotential-theory-1AB9C13A`, tag `4146861A3795`, same blob, **lines 86–109**, defines \(c(E)=\exp(-\gamma(E))\), \(\gamma(E)=\limsup_{|z|\to\infty}(V_E^*(z)-\log|z|)\). Selected proof checks: compact upper-semicontinuous maxima along decreasing sequences; the distinction between raw and regularized envelopes; projective extension at infinity, without certifying the preceding canonical-discrepancy theorem.
5. **Cross-context only:** Lemma 7.10.1 (source `foundations-of-pluripotential-theory-74804636`, tag `C09E42A43E93`, lines 10–36) and Theorem 7.10.2 (source `foundations-of-pluripotential-theory-9C25B561`, tag `C9116FCEFCD2`, lines 37–109), `docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html`, blob `762b841b0cb243784dc988f04dbf2779da66c469`. Checked the strict \(t^n\) factor from mixed-product positivity, bounded density barriers, lower-tail capacity bound, and uniqueness via strict \(\varepsilon^n\) perturbation. Older ledger findings on §7.10 are not repeated. This is **not** the user-excluded smoothing programme.

## POME-REALCONVEX-SCALE-001 — exact norm of homothetic extremal displacement

**Severity:** low. **Status:** verified conditional deduction; no false Pome theorem alleged. **Proposed correction:** optional short corollary to Theorem 16.33.6. **Affected dependents:** quantitative estimates for real convex-body logarithmic extremals and their generalized capacities, not a correction to the printed theorem.

**Statement.** Let \(E\subset\mathbb R^n\) be compact, centrally symmetric and convex with \(0\in\operatorname{int}_{\mathbb R^n}E\). For \(0<s\le1\), throughout \(\mathbb C^n\),
\[
0\le V_{sE}(z)-V_E(z)\le A_s,\qquad
A_s:=\operatorname{arcosh}(s^{-1})=
\log\left(s^{-1}+\sqrt{s^{-2}-1}\right).
\]
Moreover,
\[
\boxed{\ \sup_{z\in\mathbb C^n}(V_{sE}(z)-V_E(z))=A_s.\ }
\]
For \(s<1\) equality holds at **every real boundary point of \(E\)**. Equivalently, for \(t\ge1\),
\[
\boxed{\ \|V_{tE}-V_E\|_{L^\infty(\mathbb C^n)}
=\operatorname{arcosh}t,\ }
\]
with equality at every point of \(\partial_{\mathbb R^n}(tE)\). These are differences of **finite continuous** extremals, so the global sup norm is meaningful even though each individual extremal has logarithmic growth.

**Proof.** The scalar \(g=V_{[-1,1]}\) is continuous, vanishes on \([-1,1]\), and is harmonic on \(\mathbb C\setminus[-1,1]\), with \(g(\xi)=\log|\xi|+\log2+o(1)\) at infinity. For \(\lambda\ge1\), set \(h_\lambda(\xi)=g(\lambda\xi)-g(\xi)\). On \(\mathbb C\setminus[-1,1]\), both terms are harmonic, because \(\lambda\xi\notin[-1,1]\) there. On the slit boundary, \(h_\lambda(x)=g(\lambda x)\in[0,g(\lambda)]\) for \(x\in[-1,1]\); at infinity \(h_\lambda\to\log\lambda\), and \(\log\lambda\le g(\lambda)=\operatorname{arcosh}\lambda\). Apply the maximum **and minimum** principles on growing slit discs, then exhaust: on the slit and its complement,
\[
0\le g(\lambda\xi)-g(\xi)\le\operatorname{arcosh}\lambda .
\tag{*}
\]
No differentiability across the slit, or interchange of unproved limits, is used.

The real polar obeys \((sE)^\circ=s^{-1}E^\circ\). By the *printed* real-convex formula in Theorem 16.33.6,
\[
V_{sE}(z)=\max_{y\in E^\circ}g(s^{-1}y\cdot z),\qquad
V_E(z)=\max_{y\in E^\circ}g(y\cdot z).
\]
Apply (*) pointwise in \(y\) and pass to maxima, obtaining both inequalities. For \(x\in\partial E\), a supporting functional \(y_0\in E^\circ\) has \(y_0\cdot x=1\), while central symmetry gives \(|y\cdot x|\le1\) for every \(y\in E^\circ\). Thus \(V_E(x)=0\) and \(V_{sE}(x)=g(1/s)=A_s\), proving sharpness at **every** real boundary point. To obtain the \(t\)-formula, apply the result to the body \(tE\) and \(s=1/t\). \(\square\)

## POME-REALCONVEX-HAUS-001 — sharp global half-Hölder stability in Hausdorff distance

**Severity:** low. **Status:** verified conditional deduction, not a theorem defect. **Proposed correction:** optional quantitative continuity corollary after Theorem 16.33.6 or in §16.31; maintain the original theorem's attribution. **Affected dependents:** extremal-function comparison under variation of real convex obstacles, capacities of changing obstacles, and quantitative real-convex approximation.

**Statement and exact bound.** Let \(E,F\subset\mathbb R^n\) be nonempty compact centrally symmetric convex sets with the **same centre \(0\)** and a common inball \(r\overline{\mathbb B}_{\mathbb R^n}\subset E\cap F\), \(r>0\). Put \(\varepsilon=d_H(E,F)\) using Euclidean distance. Then
\[
\boxed{\quad \sup_{z\in\mathbb C^n}|V_E(z)-V_F(z)|
\le \operatorname{arcosh}\left(1+\frac{\varepsilon}{r}\right).\quad}
\tag{1}
\]
The bound is *sharp for every* \(\varepsilon\ge0\): take \(E=r\overline{\mathbb B}_{\mathbb R^n}\) and \(F=(r+\varepsilon)\overline{\mathbb B}_{\mathbb R^n}\). In particular, the worst-case small-distance modulus is exactly of square-root order:
\[
\operatorname{arcosh}(1+\varepsilon/r)
=\sqrt{2\varepsilon/r}+O((\varepsilon/r)^{3/2}).
\]
A uniform linear-in-\(d_H\) estimate is therefore false even for homothetic smooth real balls, while the half-Hölder modulus is optimal at a fixed common inradius.

**Proof.** Hausdorff inclusion gives \(F\subset E+\varepsilon\overline{\mathbb B}_{\mathbb R^n}\subset(1+\varepsilon/r)E\), and symmetrically \(E\subset(1+\varepsilon/r)F\), since \(r\overline{\mathbb B}\) is contained in both bodies and Minkowski sums of positive homothetic copies of a convex body add exactly. Put \(t=1+\varepsilon/r\). The inclusions yield \(t^{-1}E\subset F\subset tE\). Raw extremals reverse obstacle inclusion, hence
\[
V_{tE}\le V_F\le V_{t^{-1}E}.
\]
The preceding *exact* homothetic estimate bounds each difference with \(V_E\) by \(\operatorname{arcosh}t\), proving (1). In the homothetic-ball example \(d_H(E,F)=\varepsilon\), and the \(t\)-equality at \(\partial F\) gives equality in (1). The asymptotic follows from \(\cosh a=1+a^2/2+O(a^4)\). \(\square\)

**Capacity crosscheck (same hypotheses).** For every fixed positive-radius closed complex test ball \(B\), the first estimate gives
\[
e^{-A_s}\alpha_B(E)\le\alpha_B(sE)\le\alpha_B(E),\qquad (0<s\le1),
\]
and (1) implies
\[
e^{-A}\alpha_B(E)\le\alpha_B(F)\le e^A\alpha_B(E),\quad A=\operatorname{arcosh}(1+\varepsilon/r).
\]
Here \(\alpha_B\) is the precise capacity in §16.31.3, not Bedford–Taylor relative capacity. The Robin quantity in §16.31.4 has the **different exact scaling law** \(c(sE)=s\,c(E)\): use \(V_{sE}(z)=V_E(z/s)\), subtract \(\log|z|\) at infinity, and exponentiate. No claim of a linear Hausdorff modulus for \(\alpha_B\) or of a uniform bound across varying inradii follows.

## Independent proof-path checks and limitations

- §16.30.1–2: norm-ball barrier gives the polynomial degree exponent exactly, and thickening \(K_\eta\) is regular by interior ball inclusion; compact-point raw/star regularization is not silently conflated. §16.30.5: its product formula concerns nonempty compact sets, with pluripolar cases handled by infinite extremals and the bounded \(L^2\) polynomial expansion argument otherwise. §16.30.6: taking powers removes a multiplicative \(M\) without assuming \(M=1\) a priori.
- §16.31.1–4: explicitly checked the non-pluripolar finite-set alternative, polar-set perturbation \(u_\delta=(u+\delta b)/(1+\delta)\) preserving the growth class, decreasing compact/increasing bounded-set quantifiers, and the **different** roles of \(c\) and \(\alpha_B\). No assertion of Choquet continuity for arbitrary unbounded unions has been imported.
- §16.33.1–7: real convexity and central symmetry are **essential** for the polar formula; the one-dimensional slit Green harmonicity is used only off the cut. Support functionals exist since the real inball makes the polar compact. No conclusion is claimed for arbitrary complex convex bodies or for nonsymmetric real compacts.
- The earlier audit ledger already contains unrelated real-convex infinitesimal Baran-type bounds in §16.39 and §7.10 capacity work. Those findings and their statuses are **unchanged**, not re-presented as new. This report adds precisely the two distinct homothetic/Hausdorff statements above.
- **Status discipline:** these are complete deductions **conditional on** Pome's current Theorem 16.33.6 and the scalar Joukowski description. No new confirmed error/proof gap, no complete mathematical certification, no automated proof check, no source edit, no CI, build, PR, merge or publication.

**Next high-dependency rotation:** unreviewed §§7.29/7.31 should be handled only outside the excluded regularization dependency; alternatives include fresh §8 Hessian comparison or non-Archimedean §22.1 portions not already tracked. The dedicated user-deferred programme stays deferred, not revived by prerequisite review.
