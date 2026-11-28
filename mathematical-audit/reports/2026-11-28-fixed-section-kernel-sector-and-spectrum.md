# Fixed selected spaces: optimal complex sector and exact Berezin spectrum

Date: 2026-11-28. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 901db16741325232fde7c0327dd3d9d17fe03ab4.

## Scope and anchors

This is a finite-dimensional Hilbert-space audit of partial equilibrium at a *fixed* degree and fixed selected space, not the deferred Demailly regularization, Bergman approximation or L2-extension completion programme. No estimate for approximation of a singular potential is undertaken.

- Whole mathematical text of §18.30, `docs/sections/partial-kernels-and-quotient-equilibrium--selected-spaces-and-partial-bergman-kernels/index.html`, lines 7–37, blob 81983c5cf4bb50d5de9006906d9fdab07137e6f4, permanent section F62F806EF43E. Norm, extremal formula, trace, inclusion and metric gauge all agree.
- Whole mathematical text of §18.34, `docs/sections/partial-kernels-and-quotient-equilibrium--the-determinant-functional/index.html`, lines 7–450 (through final example and concluding paragraph), blob 626a4c74bb7f5e6659320052c54ec29902646b61, permanent section 3AC0CF30AE00. Reviewed first and second determinant derivatives, analyticity in the uniform norm, ordered inverse Taylor compositions, Gevrey bounds, diagonal derivative, disk counterexample, positive Markov coupling, logistic TV bound, sharp rank-one example and product-fiber example. Signs, normalization and finite-dimensional operations agree. The Taylor-composition order is immaterial to the summed formula because reversal permutes all compositions.
- §18.29, `docs/sections/partial-kernels-and-quotient-equilibrium/index.html`, blob 2e76f1e5ddab36aa10c2c517390b8aed6ab81e84, line 8 supplies connectedness and positive dimension; selected convention at line 29. Other introductory statements do not constitute proof verification.
- §18.35, `docs/sections/partial-kernels-and-quotient-equilibrium--partial-kernels-under-a-modification/index.html`, blob fd1ca7e3112c41d229b3d37faff948a8012e5985, lines 14–67 and 113–137: direct check of envelope competitor identification conditional on 5.43.18, 5.43.23, 18.32.2; non-pluripolar locality and no analytic-set mass; Jacobian metric and section isometry conditional on 5.43.22. Cor. 18.35.6's dominated-convergence deduction is correct conditional on 18.35.5. The external SGPT 14.3.1 Kähler quantization input in 18.35.5 (line 96) is recorded, not certified or reopened; any excluded approximation proof stays deferred-by-user.

## POME-PARTIAL-KERNEL-OPTIMAL-COMPLEX-SECTOR-001

Severity low; status verified conditional deduction (optional improvement, not a false printed theorem). Proposition 18.34.22, permanent 4F99D774A693, source non-kahler-pluripotential-theory:824CFD61, lines 401–422 (see also 18.34.5 lines 98–135, permanent 81FC6A666EC9). Preserve the original valid smaller-radius version.

Let X, h, nu, m and V=V_m be as in 18.29–30, N=dim V>0, v real continuous. Denote the normalized probability by mu_v. The complex perturbation f of the scaled weight v+f/m admits a holomorphic extension to the open domain

\[
 \Omega=\{f\in C(X,\mathbb C): \operatorname{osc}_X \Im f<\pi\}.
\]

It is invariant under complex constants. Writing a=Re f, b=Im f, delta=osc b/2, the extended complex measure satisfies the dimension-independent bound

\[
 |\mu_{v+f/m}|\le \sec(\delta)\,\mu_{v+a/m},\qquad
 \|\mu_{v+f/m}\|_{\rm TV}\le\sec(\delta).
\]

Proof. Use the real weight u=v+a/m and center b by a real constant c=(sup b+inf b)/2. With P_u the orthogonal projection and the convention linear in the first entry, let T=P_u(exp(-i(b-c)) dot)|_V. For every s in V,

\[
 \Re\langle Ts,s\rangle_u\ge \cos(\delta)\|s\|_u^2.
\]

Cauchy–Schwarz gives ||Ts||>=cos(delta)||s||. Finite dimensionality yields invertibility and ||T^{-1}||<=sec(delta). Before centering, the compressed multiplication differs by the scalar exp(-ic), which cancels in the diagonal formula. The holomorphic formula from 18.34.5 can instead be formed at the fixed weight v: T_v(f)=P_v(exp(-f) dot)|_V. If S=P_v(exp(-a) dot)|_V then T_v(f)=S T_u(ib) as operators on V, by testing against every vector with the v inner product. Thus invertibility just proved holds on all Omega. Holomorphic inversion is local on the invertible finite matrices; the diagonal evaluation and the passage to measures are bounded linear operations as in 18.34.5. The result agrees with the real measure on real weights. Applying the formula at u, with the Riesz vector k_{u,x}, gives a density bounded in modulus by exp(-mu(x)) ||T^{-1}|| ||k_{u,x}||_u^2/N relative to nu. This is precisely the claimed measure domination. Here exp(-mu(x)) means exp(-m times u(x)), not the measure mu_u. At common zeros both densities vanish.

In particular the universal open complex sup-norm ball about any real weight in the scaled variable f has radius pi/2, and for a real q with oscillation d>0 and any 0<R<pi/2,

\[
 \left\|\left.\frac{d^k}{dt^k}\right|_{0}\mu_{v+tq}\right\|_{\rm TV}
 \le k!\sec(R)(md/(2R))^k .
\]

This follows by subtracting the midpoint constant of q and applying Cauchy on the circle |t|=2R/(md); the imaginary oscillation of mtq is at most 2R. Constant directions have zero derivatives.

Sharp universal radius (not a claim about the radius for each fixed space). Use X=P^1, trivial bundle and selecting potential zero, v=0, N=1 and normalized Fubini–Study area. Let H be the smooth height coordinate with range [-1,1], whose law is symmetric and whose equator has area zero. Put q_j=tanh(j H)/tanh(j), a smooth real function with sup norm 1, oscillation 2, odd under the area-preserving equator reflection. For the scaled complex direction f=i t q_j, the normalizing denominator Z_j(t)=integral exp(-it q_j) dnu=integral cos(t q_j) dnu is real. At t=pi/2 it is strictly positive (|q_j|<1 off the poles); for each pi/2<t_0<pi, Z_j(t_0) tends to cos(t_0)<0 by dominated convergence. Hence for large j a first positive zero occurs in (pi/2,t_0). The density exp(-it q_j)/Z_j(t) has TV=1/|Z_j(t)| for real t before that zero, and is unbounded as the zero is approached. No holomorphic measure-valued extension through it exists, by uniqueness of analytic continuation along this line. Since t_0 can approach pi/2, no larger universal ball is possible even for smooth data on a curve. No singularity at the endpoint itself for every weight is asserted.

Affected dependents: the derivative estimate in 18.34.22 can use the new bound; 18.34.18's real TV modulus and Example 18.34.21's optimal real bound are unchanged. No asymptotic m-uniform unscaled differentiability is asserted.

## POME-PARTIAL-KERNEL-BEREZIN-EXACT-RANK-GAP-001

Severity low; status verified conditional deduction, optional extension of Lemma 18.34.16, permanent 66CB6C16A6B7, source non-kahler-pluripotential-theory:C7EB694C, lines 265–306, and Prop. 18.34.1, permanent A1D3D26087E7, source 576F8072, lines 20–55.

At fixed real weight v, let Q=Q_v on complex L2(mu_v) be the positive selfadjoint Markov operator of 18.34.16. Its exact rank is N^2, its operator trace is N, and eigenvalue 1 is simple. Consequently, writing gamma_v=1 minus the largest eigenvalue on the orthogonal complement of constants (zero if that restricted operator is zero, i.e. gamma_v=1 in this case), gamma_v>0, and

\[
 -\frac{d^2}{dt^2}\bigg|_0 \mathcal F_m^{(r)}(v+tq)
 \ge \frac{r!N}{m^{r-1}}\gamma_v \operatorname{Var}_{\mu_v}(q).
\]

Proof. With the notation F_i, B of 18.34.16, set g_ij=F_i conjugate(F_j)/B off the common zero set, and zero on it. These functions are bounded and well-defined independent of the unit-frame phase. Relative to mu_v, the kernel of Q is N |C_v(x,y)|^2/(B(x)B(y)) = N sum_ij g_ij(x) conjugate(g_ij(y)). Hence Q=N sum_ij g_ij tensor g_ij^*, and trace Q=N integral sum_ij |g_ij|^2 dmu_v=N.

For exact rank, suppose sum a_ij g_ij=0 in L2(mu_v). In a coordinate ball with a local holomorphic frame, write the sections as f_i(z) times that frame. Cancel the positive scalar from the metric and weight and multiply by B. Since mu_v is equivalent to the smooth positive volume away from the common analytic zero set, continuity gives sum a_ij f_i(z) conjugate(f_j(z))=0 on the ball. Complexify the real-analytic identity by Taylor coefficients in z and conjugate(z): sum a_ij f_i(z) conjugate(f_j(w))=0 for z,w in a smaller ball. The values (f_i(z)) span C^N there; otherwise a nontrivial constant linear combination of the global sections vanishes on a ball and hence on connected X. Applying this twice gives all a_ij=0. Thus the N^2 vectors are independent and the positive finite sum has precisely that rank.

For simplicity of the eigenvalue 1, for each x off the common zero set, the Riesz section k_{v,x} is nonzero; its analytic zero set in the y-variable has smooth-volume measure zero. Therefore the symmetric joint measure J_v of 18.34.16 is equivalent to mu_v tensor mu_v, by Fubini. If Qg=g, then integral |g(x)-g(y)|^2 dJ_v=2(<g,g>-Re<Qg,g>)=0. Equivalence implies g constant almost everywhere. Since Q is positive, finite-rank and selfadjoint, its largest eigenvalue on the mean-zero space is strictly below 1. The displayed inequality follows by rewriting the printed Hessian (18.34.1) as -(r!N/m^{r-1}) <q,(I-Q)q> and applying the spectral bound to q minus its mean. This is stronger than the printed pointwise strict-concavity assertion in that it gives an L2 variance coercivity constant for each fixed space and weight, not a constant uniform as m grows. In particular Q has N^2-1 positive nonconstant eigenvalues when N>1; their sum is N-1. No uniform lower bound for gamma_v over degrees or all selected spaces is claimed.

Affected dependents: Prop. 18.34.1 and Lemma 18.34.16; optional refinement of the real linearization in Prop. 18.34.18. No mandatory correction.

## Coverage and remaining dependencies

The current chapter 18 index has 47 sections, and the matrix previously marks 18.30, 18.34 and 18.35 LEGACY-UNRECONCILED. Record two whole current direct mathematical sections (18.30, 18.34) and selected direct 18.29/18.35; do not assert historical first visits. The fixed-space arguments require no Demailly approximation or construction of global sections with prescribed estimates. Zero new confirmed printed errors, zero demonstrated proof gaps, two optional verified deductions, zero complete transitive proof-chain certifications. All previously excluded work remains deferred-by-user. No source edits, project builds, tests, CI, publishing or merge.
