# Surface Monge–Ampère: exact anisotropy defect in determinant root concavity

**Audit date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Pre-write review branch:** 92da3541f58b970580a4c75740151f5fc4032eb5. **Scope:** a new smooth complex-dimension-two quantitative refinement of already-correct mixed Bedford–Taylor inequalities; not a general singular-product result.

## 1. Production evidence and precise coverage

- **Reading edition:** docs/sections/bedford-taylor-products-and-local-capacity--density-lower-bounds-and-mixed-products/index.html, main blob **0284d93a0ac26e28746e95afda5e6875f9feaba3**.
- **Source and tags:** foundational Lemma 7.8.1, source **foundations-of-pluripotential-theory:2844C025**, permanent tag **BB19C89586B1**, physical lines **22–63**, including the mixed determinant polynomial, eigenvalue argument and AM–GM estimate; Proposition 7.8.3, **foundations-of-pluripotential-theory:183E5B3C**, tag **EB2AFC8FB17C**, lines **114–181**, read for viscosity/distribution/measure hypotheses; Corollary 7.8.4, **foundations-of-pluripotential-theory:66F302D3**, tag **EADDEAF9FAD9**, lines **183–209**, including its coefficient normalization and stated extension to locally bounded potentials. Section normalization **eta = dd^c |z|²**, lines **7–16**, uses **(dd^c u)^n = det H(u) eta^n** for smooth potentials.
- **Other genuinely checked steps:** the constant-coefficient real elliptic reduction of Lemma 7.8.2, source **foundations-of-pluripotential-theory:2D6E0212**, tag **1BE242B641AA**, physical lines **65–97**, and the explicit pointwise-to-distribution comparison at Proposition 7.8.3, lines **133–178**. These upstream proofs are only *selected-step checks*, not independent certification of their complete dependency graphs.
- **Not newly covered or re-certified:** §7.5 capacity convergence, §7.12 finite Minkowski and §14.21 cofactor comparisons were already audited; none is re-registered as a new result here. All user-excluded Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion pathways remain **deferred-by-user** and untouched.

## 2. POME-BT-SURFACE-MINKOWSKI-ANISOTROPY-001

**Severity:** low. **Status:** verified conditional deduction (a complete elementary smooth-matrix identity anchored in the reading edition), **not a confirmed error** or a proof repair.

Let Omega be open in C², and let u and v be real C² strictly plurisubharmonic functions on Omega. At a point x, write

\[
 A=\mathcal H(u)(x)>0,\qquad B=\mathcal H(v)(x)>0,\qquad
 a=\det A,\quad b=\det B,
\]
and let lambda_1, lambda_2 > 0 be the eigenvalues of A^{-1/2} B A^{-1/2}. For all nonnegative real s,t, the following is an **exact identity**, with all Monge–Ampère densities measured relative to eta²:

\[
\boxed{\ \det(tA+sB)-
 (t\sqrt a+s\sqrt b)^2
 =st\,a(\sqrt{\lambda_1}-\sqrt{\lambda_2})^2.\ }
\tag{1}
\]

Equivalently, writing r=lambda_1/lambda_2,

\[
\boxed{\
 \det(tA+sB)-(t\sqrt a+s\sqrt b)^2
 =2st\sqrt{ab}\,[\cosh(\tfrac12\log r)-1]
 \ge \frac{st\sqrt{ab}}4(\log r)^2.\
}
\tag{2}
\]

The constant **1/4** in the logarithmic lower bound is optimal *as a universal coefficient*, in the limit r to 1. For s,t>0 equality in (1)'s usual determinant-root Minkowski inequality holds precisely when lambda_1=lambda_2, or equivalently **B=cA** for some c>0. If either scalar coefficient is zero, equality holds trivially.

Thus, pointwise on Omega,

\[
(dd^c(tu+sv))^2
=
(t\sqrt{\det\mathcal H(u)}+s\sqrt{\det\mathcal H(v)})^2\,\eta^2
+st\det\mathcal H(u)\,
 (\sqrt{\lambda_1}-\sqrt{\lambda_2})^2\,\eta^2.
\tag{3}
\]

The rightmost positive term is an explicit **smooth anisotropy defect**, not an asserted positive Radon measure under merely bounded or singular potentials.

### Complete independent proof

Because A is positive definite, the Hermitian matrix C=A^{-1/2}BA^{-1/2} is positive definite. Spectral invariance of determinant gives

\[
\det(tA+sB)=a\det(tI+sC)
=a(t+s\lambda_1)(t+s\lambda_2).
\]

Also b=a lambda_1 lambda_2. Hence the determinant is
\(t^2a+st a(\lambda_1+\lambda_2)+s^2b\), while the claimed Minkowski square equals
\(t^2a+2st a\sqrt{\lambda_1\lambda_2}+s^2b\). Subtracting proves (1).
It follows from elementary algebra that
\[
\frac{(\sqrt{\lambda_1}-\sqrt{\lambda_2})^2}
{\sqrt{\lambda_1\lambda_2}}
=\sqrt r+r^{-1/2}-2
=2(\cosh(\tfrac12\log r)-1).
\]
Since \(\cosh y-1\ge y^2/2\) for every real y, (2) follows.
The ratio of its exact defect to \(st\sqrt{ab}(\log r)^2\) tends to \(1/4\) as \(r\to1\), proving optimality of that coefficient. For s,t>0 the defect vanishes iff both positive eigenvalues have the same square root, so C=cI and B=cA. Finally the reading-edition §7.8 lines 7–13 supply the normalization of (3). This completes the **local smooth calculation** without an external mathematical input.

### Sharp nonproportional models

For quadratic strictly PSH potentials on C² with constant Hermitian Hessians A=diag(1,4), B=diag(4,1), one has a=b=4 and, for s=t=1,

\[
\det(A+B)=25,\quad(\sqrt a+\sqrt b)^2=16,\quad
\text{exact defect}=9.
\]
The eigenvalues of A^{-1/2}BA^{-1/2} are 4 and 1/4. The defect is exactly \(4(2-\tfrac12)^2=9\). For a noncommuting pair A=[[2,1],[1,2]], B=diag(3,1), one has a=b=3 and \(\det(A+B)=14\), with exact gap 2. For B=2A, the defect is identically zero; hence no strictly positive anisotropy bound independent of the relative spectrum is possible.

### Distinctness, dependencies and proposal

The previously recorded **POME-BT-FINITE-MINKOWSKI-001** gives the correct *nonnegative* determinant-root bound in substantially broader singular Radon-measure settings (based on §7.12). The present finding is **not that inequality again**: its new content is the **exact nonzero defect**, iff proportionality and optimal logarithmic spectral coercivity in the *smooth strictly positive complex-surface* setting. Original Lemma 7.8.1 and Corollary 7.8.4 remain correct and correctly include semipositive and locally bounded cases for their weaker inequality; we do not claim their stronger singular equality characterizations. The earlier §7.8 lower-semicontinuous density extension and its external/internal dependencies are preserved, not redone.

**Proposed documentation-only amendment (not applied to production):** an optional smooth-dimension-two remark after §7.8.4, preserving existing source attribution, canonical entry and permanent tags. **Potential downstream dependents:** strict PSH models for §7.9 ball Dirichlet subsolutions, §7.12 mixed-product comparison and surface Monge–Ampère variational equality cases. No downstream theorem is asserted repaired or fully verified by this observation.

## 3. Verification and limits

Five exact symbolic/rational Hermitian 2x2 checks were **executed** using SymPy, including two diagonal strictly anisotropic examples, a noncommuting example, a proportional equality case and a complex Hermitian case; see checks/check_bt_surface_anisotropy.py. They check the exact polynomial cross coefficient, equality defect and sample values; they are **not** formal verification or project tests. No build, CI, website publication, source edit, tag/registry alteration or mathematical-section certification was performed. The current collection inventory remains **25 chapters / 747 numbered sections / zero whole sections certified**, and all earlier open/false/deferred statuses are preserved.
