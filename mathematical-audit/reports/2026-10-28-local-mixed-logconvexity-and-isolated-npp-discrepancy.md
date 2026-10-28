# Local mixed residual masses and an isolated classical/non-pluripolar mass discrepancy

**Date:** 2026-10-28 (Asia/Shanghai). **Pinned production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting mathematical-audit HEAD:** 6d65a806d4ce26e4745b11045a94df9f782cd799.

## Scope and provenance

This is a targeted mathematical audit of previously inventory-only §§6.50 and 6.51, with a narrow cross-check against the already selected Definition 13.11.1. The actual integrated reading edition was inspected, not merely the source names or theorem numbering.

* **§6.50**: docs/sections/isolated-singularities-with-zero-lelong-number/index.html, main blob 046c83fa3c876c8a6d98642662ded103d6c78eec. Theorem 6.50.11, source isolated-plurisubharmonic-singularities:5C61AE34, permanent tag 367D36FB36A0, physical lines 134–189 (especially the mass limit at 150–162 and vanishing-Lelong sequence at 164–188); Corollary 6.50.14, source isolated-plurisubharmonic-singularities:BA029FA9, permanent ECF3A574075A, lines 195–239 (separated max and bounded truncations). Also inspected Lemma 6.50.2 lines 15–54, Lemma 6.50.5 lines 60–86 and Proposition 6.50.8 lines 92–106.
* **§6.51**: docs/sections/radial-growth-and-residual-mass/index.html, main blob 3b7a7a2965306db7a2bde4c5f91c171bae685546. Lemma 6.51.1, source isolated-plurisubharmonic-singularities:21929182, permanent BE4AE95DA940, lines 11–58; its log-convexity formula lines 13–17 and weighted Cauchy–Schwarz proof lines 24–57. Also read the exact statement/proof of Lemma 6.51.4 lines 72–126, Theorem 6.51.6 (source isolated-plurisubharmonic-singularities:2DB46145, permanent E8283D7F161B) lines 131–155 and Proposition 6.51.7 lines 160–171.
* **§13.11**: docs/sections/non-pluripolar-products--the-non-pluripolar-products/index.html, main blob 054a7661c855824b86eb749e211fc3da88a599de. Definition 13.11.1, source sgpt:FCFE372A, permanent 1A52175C3D64, physical lines 14–28, including the increasing cutoffs O_k and zero extension; the no-pluripolar-mass clause of Proposition 13.11.4, lines 77–83.
* **Dependency-only context**: §6.49.4, docs/sections/polynomial-iterates-and-residual-mass/index.html, tag DDF1EA12A4BF, lines 103–132. No new proof certification is assigned to §6.49. No Demailly approximation/regularization, dedicated Bergman or L2 estimates, Ohsawa–Takegoshi, multiscale atlases, or positivity-loss proof completion was opened or used.

No theorem in these inspected passages is shown false. The following two results are deliberately labeled conditional deductions, rather than full independent certifications of upstream classical-product continuity, proper-map mass, Crofton, or swept-boundary formulas.

## POME-LOCAL-MIXED-MASS-LOGCONVEX-SHARP-001

**Status:** verified conditional deduction. **Severity:** low. **Printed Lemma 6.51.1:** correct in the tested isolated analytic model; not a complete certification of its arbitrary-psh proof. **Affected dependents:** the residual-mass propagation in §6.51.4 and later vanishing claims based on the local log-convex inequality; comparisons with global Khovanskii–Teissier-type inequalities. **Proposed action:** optional model remark; preserve the direction of the local inequality, and do not canonicalize it with a global log-concavity statement having different hypotheses.

On a bidisc centered at the origin, take positive integers p,q and the isolated analytic weights

\[
a_{p,q}(z,w)=\log(|z|^{2p}+|w|^{2q}),\qquad
b(z,w)=\log(|z|^2+|w|^2).
\]

Both are finite and smooth away from the origin, and their classical mixed residual measures at the origin are well-defined. With m_j=((dd^c a_{p,q})^j\wedge(dd^c b)^{2-j})(\{0\}), we have the *exact* values

\[
\boxed{m_0=1,\qquad m_1=\min(p,q),\qquad m_2=pq.}
\]

Here dd^c=(i/2\pi)\partial\bar\partial and dd^c\log|f|^2=[f=0] in the Poincaré–Lelong convention.

**Proof of the local masses.** If F=(f_1,f_2), unitary invariance of normalized spherical measure on the coefficient sphere gives

\[
\int_{S^3}\log|\lambda_1f_1+\lambda_2f_2|^2\,d\lambda
=\log(|f_1|^2+|f_2|^2)+c,
\]

with a constant c independent of F\ne0. Thus the current dd^c\log\|F\|^2 is the average of the divisor currents of the generic linear combinations, by Poincaré–Lelong. For two independent generic coefficients, the atom of the classical product is the local proper-intersection multiplicity. The exchange of the averaging and local intersection may be justified by bounded truncation on a fixed boundary collar and positive-current Fubini; this is the same classical isolated-intersection input used elsewhere in this collection, and is explicitly kept conditional here.

For a_{p,q} twice, generic combinations of z^p and w^q generate exactly the ideal (z^p,w^q); its quotient local algebra has basis z^i w^j for 0<=i<p and 0<=j<q, hence intersection multiplicity pq. For b twice, the two independent generic linear forms cut the origin with multiplicity one. For one of each, a generic linear form is z=t w with t\ne0, and the other generic equation restricts to c t^p w^p+d w^q. Its order at zero is min(p,q); if p=q, the leading coefficient is generically nonzero. Hence m_2=pq, m_0=1 and m_1=min(p,q).

It follows that

\[
\frac{m_1^2}{m_0m_2}
=\frac{\min(p,q)}{\max(p,q)}\le1,
\]

which verifies the **log-convex**, not log-concave, direction of §6.51.1. Equality occurs for p=q; choosing p=1, q=N sends the ratio to 0 as N grows, so the inequality can be arbitrarily strict. This is a mixed-residual *local* statement, not the cohomological inequality for nef or ample classes on compact manifolds. The full weighted Cauchy–Schwarz/boundary-collar argument of printed Lemma 6.51.1 was read; no independent audit of all its upstream convergence and boundary inputs was claimed.

## POME-ZERO-LELONG-CLASSICAL-NPP-SPLIT-001

**Status:** verified conditional deduction. **Severity:** low. **Printed §6.50.11/.14 and §13.11.1:** compatible and correct given the printed construction and classical-product identities. **Affected dependents:** use of residual Monge–Ampère mass in §§6.50–6.51 and contrasts with full/non-pluripolar mass in §§13.11–13.14 and subsequent energy or envelope comparisons. **Proposed action:** an optional explicit convention warning: a classical isolated-pole atom is not the non-pluripolar product of the same weight. Do not merge or silently exchange the two notions.

For every n>=2, let U_n be the explicit psh weight in Corollary 6.50.14, constructed from Theorem 6.50.11 by a separated maximum. It satisfies, in the printed theorem,

\[
U_n^{-1}(-\infty)=\{0\},\qquad e^{U_n}\in C^0,\qquad
\nu(U_n,0)=0,\qquad (dd^cU_n)^n_{\rm classical}=\delta_0.
\]

The last assertion is the printed classical-product identity and is not here re-proved independently of its §6.49 degree and §6.50 swept-boundary/separated-maximum inputs. However, **Definition 13.11.1 implies exactly**

\[
\boxed{\langle(dd^cU_n)^n\rangle_{\rm nonpluripolar}=0.}
\]

Indeed, set O_k={U_n>-k} and U_{n,k}=\max(U_n,-k). Every point of O_k is outside the only pole. By bounded Bedford–Taylor locality on O_k, (dd^cU_{n,k})^n restricted to O_k agrees with the classical (dd^cU_n)^n there. The latter is the measure \delta_0, and 0 is not in O_k. Therefore

\[
{\bf1}_{O_k}(dd^cU_{n,k})^n=0
\quad\text{for every }k.
\]

In particular the local mass boundedness condition of Definition 13.11.1 is satisfied with bound zero, and its increasing-cutoff construction returns the zero measure on the entire bidisc/polydisc. There is no interchange of unproven limits here: **each restricted truncated measure is already zero**, and by definition the product assigns no mass to the excluded pole set.

Thus the same isolated zero-Lelong potential has classical residual mass one and non-pluripolar mass zero. This is a concrete cross-chapter distinction in every complex dimension n>=2, not a contradiction or a false theorem. It must not be conflated with the alternative assertion that classical and non-pluripolar products coincide for locally bounded potentials: U_n is not locally bounded at zero.

## Actual coverage, open boundaries, and scope

**New directly inspected nonexcluded passage sets:** §§6.50 and 6.51, previously marked inventory-only. **Incremental comparison:** Definition 13.11.1, already covered in earlier selected reviews. §6.49 is dependency context only. No complete section, chapter, entire construction, upstream proper-map projection formula, boundary sweeping formula, local Crofton argument, or global analytic proof chain is newly certified. The 25-chapter/747-distinct-section ToC inventory remains unchanged. No software tests, builds, formal verification, CI, site publication, source/body edits, canonical registry or permanent-tag changes took place.

**External-input boundary:** The local analytic intersection/Poincaré–Lelong calculation above invokes standard proper-intersection identification and a positive-current averaging passage; the printed residual-mass construction invokes its own previously stated classical-product continuity and swept-boundary formulas. Neither is represented as newly proved in complete generality by this audit. Historical attribution must be preserved in any future edited reading text.

All user-excluded Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss findings remain **deferred-by-user**, neither resolved nor certified. All older confirmed errors, proof gaps, candidates, and external dependencies retain their prior status.

**Write discipline:** audit Markdown only on review/mathematical-audit; no production main, published docs, original mathematical body, canonicalization, source repositories, tags, issues, PR duplication, or automated publication.
