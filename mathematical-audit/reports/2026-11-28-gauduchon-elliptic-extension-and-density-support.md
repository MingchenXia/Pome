# Gauduchon ansatz: elliptic extension, a stale regularity reference, and density support

Baseline main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only, 2026-11-28.

## POME-GAUD-EK-HISTORY-XREF-001 — low / confirmed reference error

File: docs/sections/smooth-monge-ampere-equations--existence-for-the-gauduchon-ansatz/index.html, blob cc78a3bf05b3a384737ab0bfac89c68e594400e8. Lemma 14.17.1 (source non-kahler-pluripotential-theory:883D7160; permanent 19E4D601D907), physical line 45: "in the formulation given in section 25.6", link data-tag 03AFF04F, permanent target E1BC130DDD5C. The redirect at docs/tag/E1BC130DDD5C/index.html (blob 578bdabc34e2ee3b334524260a45cde8692b76d6) points to the history section docs/sections/history--monge-ampere-and-hessian-equations/index.html (blob 540eccc1cc56edc6f1ab69f99214d7a4736f3529). Its entire exposition, lines 6–10, does not state an Evans–Krylov estimate. The link therefore does not justify the advertised formulation. This is a confirmed reference defect, not a counterexample to the regularity lemma.

Proposed patch (not applied): explicitly invoke the concave uniformly elliptic interior Evans–Krylov–Caffarelli estimate in the formulation stated in §8.5, docs/sections/complex-hessian-equations--bounded-complex-hessians-and-elliptic-extensions/index.html (blob fdd9225b1d778e1debaf94f75ef65175d4bd4484), immediately before Proposition 8.5.4 (permanent 6FBA7BB8AC94). Preserve the historical link in its actual historical role rather than removing attribution. The estimate is still an external proof input (already recorded as POME-HESSIAN-EKC-REGULARITY-EXTERNAL-001); the correction does not eliminate it. Linear W^{2,p}, Schauder, and Fredholm theory are also used, not reproved here. Affected dependent: existence/closedness in Theorem 14.10.1 (source 3E8336C1, permanent 76AF759A4024), proof in §14.17 lines 59–73.

## Direct conditional check of §14.17

All mathematical lines 7–73 read. The complex Hessian bounds and determinant lower bound imply fixed spectral bounds aI <= Q <= bI. In the tangent-plane infimum at lines 23–37, concavity follows from affine dependence on A, and the plane at Q attains equality at each actual Hessian. For real N>=0, the principal-symbol increment is tr(B^{-1}P_n(H_x(N))). Since P_n preserves trace and positivity, this is between tr(H_x(N))/b and tr(H_x(N))/a, which by the coordinate comparison yields genuine real uniform ellipticity on the entire symmetric matrix space, not merely on the admissible cone. Uniform Hölder dependence on x follows from the fixed compact set of B and the smooth metric coefficients, with the stated linear growth in ||A||. The W^{2,p} step only needs the fixed Laplacian bound, not a previously bounded real Hessian. Bootstrapping uses the smooth original equation, not differentiability of the infimum extension. Openness uses the negative adjoint mean for the scalar; closedness uses a sequence because the parameter interval is metrizable. Positivity survives through the uniform lower eigenvalue bound. Uniqueness follows by the integrated linearization and maximum principle, on connected X. These checks are conditional on the stated a priori estimates and the analytic inputs; no transitive certification.

## POME-GAUD-ANSATZ-DENSITY-SUPPORT-001 — low / verified conditional deduction

An optional strengthening of Theorem 14.18.2 (permanent F90961841CA0, lines 32–62, docs/sections/smooth-monge-ampere-equations--normalization-for-the-gauduchon-equation/index.html, blob 07303e817cd642d6f34b8ff2c1b876a4b299c4ac). Retain all hypotheses of Theorem 14.10.1: connected compact complex manifold, n>=2, fixed Hermitian gamma_0, fixed Gauduchon gamma; smooth real F,G and the normalized positive solutions. Put a=(n-1)/n, b_F=b_gamma(F), and mu_F=mu_{u_F}^gamma.

The exact finite-difference upper bound is

    b_G-b_F <= -(1/a) log int exp(a(G-F)) dmu_F.

Indeed, Q is affine in u and positive. By the adjoint identity (14.12.2, permanent 62F6382D2CAC), together with (14.13.1, permanent D281466AD7B7),

    int tr(Q_F^{-1}Q_G) dmu_F = n,
    (det Q_G/det Q_F)^{1/n} = exp(a(G-F+b_G-b_F)).

The first identity follows by applying the linearization of log det Q/(n-1) to u_G-u_F and using its zero adjoint mean; there is no derivative of mu_F. Pointwise AM–GM for Q_F^{-1/2}Q_G Q_F^{-1/2} gives the bound upon integration. Equality holds exactly when Q_G is a pointwise positive scalar multiple of Q_F; no further equality classification is required here.

In particular the positive-density functional S(r)=exp(-a b_gamma((log r)/a)), defined on smooth strictly positive r, has the representation

    S(r)=sup_{s smooth, s>0} S(s) int (r/s) dmu_{(log s)/a}.

Each upper bound on b gives a lower bound on S and s=r realizes equality. Thus S is convex, positively homogeneous and subadditive on the positive cone. This is a support representation for the scalar ansatz of §14.10; no identification with the separate variational volume functional in Chapter 12 is asserted.

A differential corollary also follows directly from §14.18.2. On the affine line F+tH, write B=Q^{-1/2} dot Q Q^{-1/2}. Then tr B=(n-1)(H-int H dmu), so tr(B^2)>=(tr B)^2/n implies

    -d²b_gamma(F+tH)/dt² >= (n-1)/n Var_mu(H).

No optimality claim for this coefficient. The surface special case with Gauduchon gamma_0 has the sharper exact variance formula already printed in Example 14.18.3 and previously reviewed. The new finite-difference estimate is for the scalar ansatz in arbitrary n>=2, not a repetition of the surface KL identity or the different Chapter 12 support-volume finding. Neither singular solutions nor weak adjoint uniqueness are asserted. Suggested optional insertion after Theorem 14.18.2; downstream use: quantitative scalar concavity and positive-density interpolation.

## Coverage and exclusions

- §14.17 entire direct conditional lines 7–73, previously legacy-unreconciled.
- §25.6 entire historical exposition, lines 6–10, checked as the actual destination; not a proof certificate.
- §§14.10, 14.12, 14.13, 14.18 directly reread, previously covered; no new whole-section counts for these repeats. Blobs respectively 3a16d6685c70f1a5448c2a9c09b240d6fd44ed83, de0b040ee22f128bf16c89048267075a01f15e66, 6e1faedde219b856c0bf5ecaf566403ae999772e, 07303e817cd642d6f34b8ff2c1b876a4b299c4ac. §8.5 selected lines 90–125 only.
- 1 confirmed reference error, 1 conditional deduction, no newly demonstrated false theorem or full upstream certificate. Demailly approximation and all dedicated excluded programmes remain deferred-by-user. No builds, tests, CI, production changes, or publication.
