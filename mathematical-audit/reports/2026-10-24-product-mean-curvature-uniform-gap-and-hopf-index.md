# Product mean-curvature gap and the Hermitian–Einstein existence dependency

**Checkpoint:** 2026-10-24; **reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Actual scope:** newly selected integrated proofs in §§11.20–11.21, contextual prerequisites §§11.17–11.18, not whole sections.

## Exact integrated source anchors (on the reviewed main)

1. docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--external-tensor-products-and-complement-convexity/index.html; blob 95d0c68d98cac2c63e819f870b9786caf8a4cc24. Lemma 11.20.1: source non-kahler-pluripotential-theory-36A46C8B, permanent tag B46ABA0FEC10, HTML lines 19–42. Theorem 11.20.2: source non-kahler-pluripotential-theory-2A5C9D23, tag 0B75DFE662A7, lines 44–61. Corollary 11.20.3: source non-kahler-pluripotential-theory-02928079, tag F8F43BAF4F9A, lines 63–71.
2. docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html; blob fab309d460a8411fefcd1ef32a094927d6feea10. Theorem 11.18.2 tag B93CB03C68B7, lines 51–75; Corollary 11.18.4: source non-kahler-pluripotential-theory-B119F64B, tag 18D33491ABFD, lines 91–109 (Hermitian–Einstein input at line 99); Corollary 11.18.5 tag E2EF3C8673FC, lines 111–125.
3. docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--homogeneous-plurisubharmonic-functions-and-hopf-complements/index.html; blob 64aaae0cd5320ede513a1dfbda5bf79a80863519. Proposition 11.21.1 source non-kahler-pluripotential-theory-C8EC3706, tag 1204B7FDAE31, lines 19–65; Example 11.21.4 source non-kahler-pluripotential-theory-425BE5B9, tag 8F043288C182, lines 116–153; Proposition 11.21.5 source non-kahler-pluripotential-theory-3A3E3293, tag F38A90B57ECC, lines 159–187.
4. Context only: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--concave-neighborhoods-and-dual-norms/index.html; blob d49b7d4f2a213c8b70abfe2f337562202bb58dfb; Lemma 11.17.3, tag 9020E77B2318 (closed-submanifold lower bound).

## POME-PROD-MEAN-UNIFORM-SPECTRAL-001

**Classification:** verified conditional deduction; **severity:** low; **not** an error in Theorem 11.20.2.

Retain the precise assumptions of §11.20: connected compact complex factors \(X_i\) of dimensions \(n_i\geq1\), Hermitian bundles \((E_i,h_i)\), Hermitian base forms \(\omega_i\), product \(X=\prod_i X_i\), external tensor product \(E=\bigotimes_i p_i^*E_i\) with product metric \(h\). Put \(\Omega=\sum_i p_i^*\omega_i\), \(n=\sum_i n_i\), \(r=\prod_i\operatorname{rank}E_i\). Suppose each mean-curvature endomorphism obeys \(K_i=\Lambda_{\omega_i}(\mathrm iF_{h_i})\geq \kappa_i I\) for some \(\kappa_i>0\). Define \(\delta=\min_i\kappa_i/n_i\). For the Hermitian coefficient form \(\alpha_{h,v}=\mathrm i\,h(F_hv,v)\), eigenvalues relative to \(\Omega\) ordered decreasingly obey
\[
 \boxed{\lambda_k(\alpha_{h,v};\Omega)\geq\delta h(v,v)\quad\text{for every }v\ne0.}
\]
The hypothesis of Theorem 11.20.2 (positive definite \(K_i\) on compact \(X_i\)) supplies uniform positive \(\kappa_i\). The conclusion persists for **every sufficiently small \(C^2\) perturbation** of the product metric \(h\) on the same bundle \(E\), even when the perturbed metric is not a tensor product. Therefore the projective complement remains \((n+r-k)\)-convex.

**Proof.** Lemma 11.20.1 proves that \(\alpha_{h,v}\) is block diagonal for \(T^{1,0}_xX=\bigoplus_iT^{1,0}_{x_i}X_i\) and that the trace of block \(i\) is \(h(\widehat K_i v,v)\). Since \(\widehat K_i-\kappa_iI\) is positive semidefinite **on the entire tensor-product fiber**, including nondecomposable tensors, this trace is at least \(\kappa_i h(v,v)\). The maximum eigenvalue of an \(n_i\)-dimensional Hermitian matrix is at least its trace divided by \(n_i\). Each orthogonal block thus contributes one eigenvalue \(\geq\delta h(v,v)\), proving the \(k\)-th-eigenvalue inequality.

On the compact \(h\)-unit sphere bundle, the Hermitian curvature coefficients depend continuously on the metric in \(C^2\): in local frames, \(F_{h'}=\bar\partial(M'^{-1}\partial M')\). Hence there is a \(C^2\) neighborhood in which the operator norm of \(\alpha_{h',v}-\alpha_{h,v}\), relative to the fixed \(\Omega\), is less than \(\delta/2\) for every \(h\)-unit vector \(v\). The min-max eigenvalue perturbation inequality then gives \(\lambda_k(\alpha_{h',v};\Omega)\geq\delta/2>0\) on that sphere, and quadratic homogeneity extends positivity to every nonzero \(v\). Theorem 11.18.2 applies with \(s=k\). No new existence theorem is used in this argument.

For the Hermitian–Einstein choices made in Corollary 11.20.3, if \(K_i=\lambda_iI\), the exact degree convention of §11.18.4 implies
\[
 \lambda_i=\frac{2\pi n_i\deg_{\omega_i}(E_i)}{\operatorname{rank}(E_i)\int_{X_i}\omega_i^{n_i}},
 \qquad
 \delta=\min_i\frac{2\pi\deg_{\omega_i}(E_i)}{\operatorname{rank}(E_i)\int_{X_i}\omega_i^{n_i}}.
\]
This numerical expression is **conditional on existence** of the Hermitian–Einstein metrics, which this audit does not establish. There is no additional factorial, multinomial coefficient, or tensor-rank factor.

**Proposed action:** optional quantitative remark after Theorem 11.20.2, preserving the original statement, tags and provenance. **Affected possible dependents:** metric-perturbation stability of the \(q\)-convexity bound and curvature estimates used in the stable-degree corollary. The proof is finite-dimensional after the established curvature identity and Theorem 11.18.2, whose original hypotheses are retained.

## POME-GAUD-HERMITEIN-INPUT-001

**Classification:** external dependency; **severity:** medium for the stated preference for self-contained proofs. **Not** a counterexample or a confirmed false theorem.

At Corollary 11.20.3 (tag F8F43BAF4F9A, HTML lines 63–70), the passage from stable, positive Gauduchon-degree bundles to metrics of positive definite mean curvature invokes existence of Hermitian–Einstein metrics. The actual source of this invocation is Corollary 11.18.4 (tag 18D33491ABFD, lines 91–108), whose proof expressly cites the **classical existence theorem** rather than providing a proof. Its exact mathematical input is: for compact complex \(X\) with Gauduchon \(\omega\), a slope-stable holomorphic bundle \(E\) admits a smooth Hermitian metric \(h\) such that
\[
 \Lambda_\omega(\mathrm iF_h)=\lambda I_E,\qquad
 \lambda\,\operatorname{rank}(E)\int_X\omega^n
 =2\pi n\deg_\omega(E).
\]
The positivity of \(\lambda\) for positive degree and all later trace/eigenvalue deductions **are valid conditional on this external theorem**. The cited passage contains no internal proof of that theorem. This audit does not claim to have excluded the possibility that a separate proof exists elsewhere in the 747-section collection. The allowed Hironaka exception does not cover this input, and historical attribution by itself is not a substitute for proof.

**Proposed correction:** name and track the theorem as a genuine analytic input, check any independently integrated full proof by stable labels and exact hypotheses, and otherwise retain the dependency explicitly pending an independent proof. A replacement by Theorem 11.20.2 alone would be circular: its direct hypothesis is already a metric with positive mean curvature. **Affected dependents:** stable-positive-degree clause of Corollary 11.18.4, Corollary 11.18.5, and Corollary 11.20.3 (including its Hirzebruch application). Theorem 11.20.2 under its direct curvature hypothesis is unaffected.

## Other genuinely selected integrated proof checks

**§11.21.1 (tag 1204B7FDAE31):** \(G(cv)=|c|^2G(v)>0\) gives compact regular levels \(\Sigma_t\), using compactness of the unit sphere bundle. For any alleged \((N-1)\)-convex exhaustion \(\psi\), the maximum \(M(t)=\max_{\Sigma_1}\psi([1:tv])\) is locally Lipschitz and diverges as \(t\downarrow0\). Somewhere its derivative is negative. At a maximizing point the multiplier \(\lambda=M'(t)/(2t)<0\). On the complex tangent hyperplane to \(\Sigma_t\), the real Hessian maximum test gives \(\mathcal L_\psi\leq\lambda\mathcal L_G\leq0\), ruling out two positive Levi eigenvalues. This selected proof step is consistent with the printed conclusion.

**§11.21.4 (tag 8F043288C182):** for \(0<q<1\), \(b=-\log|a|/\log q\), the sign of \(-b\) matches the stated degree sign, and \(\mathrm{dd}^c\log|z|^2\) has rank \(n-1\) and radial kernel. The compact elliptic-fiber restriction supplies the low-index obstruction when \(|a|<1\); when \(|a|\geq1\) the squared norm is homogeneous psh, supplying the opposite extremal index. The printed discontinuity at \(|a|=1\) is real, not a sign error.

**§11.21.5 (tag F38A90B57ECC):** the curvature sign of the direct-sum metric and closed elliptic-fiber lower bound were checked in the all-positive-degree/all-nonpositive-degree regimes. The **mixed-sign** line 179 onward gives only \(\max\{r+1,n+t\}\leq\kappa(F)\leq n+r\), with \(t=\#\{j:|a_j|\geq1\}\); this audit does **not** supply an exact formula in the mixed case.

**§11.17.3:** the dimension count for transfer from a closed complex submanifold was checked as a contextual dependency. No full section or transitive analytic prerequisite was certified. Earlier §11.22 findings on Hodge currents and positive-harmonic fibers already exist in the ledger and are **not** re-registered.

## Limits and deferred scope

The 25 chapters and 747 coverage-matrix sections are table-of-contents inventory, not an audited fraction or completed verification. No arithmetic scripts, full build, repository tests, GitHub Actions, website publication, formal proof checker, PR/merge, source-body edit, registry edit, or permanent-tag modification was performed. All historical unresolved entries retain their prior states. The user's **excluded** Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion program remains **deferred-by-user**, not resumed, resolved or certified.
