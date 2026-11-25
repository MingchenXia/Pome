# Stationary discs: strong exposure of the infinitesimal indicatrix

2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 8c798b09058f5eda9cdfa4b0ead367844d0e03f0.

## Finding POME-STATIONARY-DISC-STRONG-EXPOSURE-001

Low / verified conditional deduction (not a false theorem or a demonstrated proof gap). Anchors: docs/sections/smooth-green-functions-on-strongly-convex-domains/index.html, blob e19df8fd1692c138eddd5f2fff8822de588e03ec, Lemma 9.24.2 (CB9F3D62BE1C, lines 55–84), Proposition 9.24.4 (495B56CEC1A8, source tag 791F5048, lines 107–172), Theorem 9.24.5 (A2E9734AB1F5, source 176EB905, lines 177–202). This is not the earlier parametric Green smoothness deduction (2026-11-14).

Let D be bounded strongly real convex with smooth boundary, r a defining function negative inside, and (f,g,rho) a smooth stationary disc as in Proposition 9.24.4, with positive rho, a=f(0), b=g(0) and g=ζ rho r_z(f) on the circle. All pairings of complex covectors and vectors are complex bilinear; real dual pairing is their real part. Integrate with normalized angular measure dm. For every holomorphic F:Δ→D with F(0)=a, there is a constant c_f>0 independent of F such that

    Re b·(f'(0)-F'(0)) >= c_f ||f-F||_{H²}².                 (1)

Here H² denotes the Hardy norm, not angular Sobolev order two. In particular f uniquely maximizes this linear functional over all discs with the given center; f'(0) is a strongly exposed point of the closed infinitesimal velocity body K_a=closure{F'(0): F(0)=a, F:Δ→D holomorphic}. More precisely the right side of (1) bounds c_f|f'(0)-F'(0)|². This is quantitative even for approximating maximizers, not merely uniqueness among smooth stationary discs.

Proof: uniformly for p on ∂D and q in closure D,

    Re r_z(p)·(p-q) >= c |p-q|².

Indeed replace r locally by r+M r², with fixed large M, so its real Hessian is positive definite on a compact collar (normal and tangential block estimate); its first derivative on the boundary is unchanged. Taylor's theorem along short segments and the nonpositive value at q give the inequality near the diagonal, with the factor two from dr=2 Re r_z. Away from the diagonal the strict supporting-plane inequality is positive: if a supporting plane contains another point of closure D, the segment between them lies in the boundary, contradicting strictly positive real second fundamental form near p. Compactness gives a uniform positive lower bound for the ratio there. Multiplying by rho, whose minimum is positive, proves the desired pointwise inequality for f on the circle. First apply it to F_s(ζ)=F(sζ), 0<s<1, then integrate. Since v=f-F_s vanishes at zero, g·v/ζ is holomorphic with value b·v'(0) at zero. Its circle mean equals that value. Thus (1) holds with F_s in place of F. Boundedness of F gives square summable Taylor coefficients by Parseval at radii below one and monotone convergence; hence F_s→F in Hardy norm by dominated convergence on the coefficient sum. Also F_s'(0)→F'(0). This proves (1). Taking limits of derivatives proves the quantitative exposed-point estimate on K_a. Convexity of D makes the velocity set convex by convex combinations of discs, and boundedness of D and Cauchy's estimate make K_a compact. No claim about attainment for arbitrary directions is required.

## Local curvature of the support function

Write H_a(b')=sup_{w in K_a} Re b'·w. On an open real neighborhood of b, Proposition 9.24.4 supplies stationary f_{a,b'} with positive multiplier, holding a fixed, without imposing the optional normalization |b'|=1. Apply (1) to each of them: H_a(b')=Re b'·f_{a,b'}'(0), so H_a is smooth there. Its differential is

    dH_a(b')[δb] = Re δb·f_{a,b'}'(0).

Indeed for v=∂_δb f, tangency is Re r_z(f)·v=0 on the circle and v(0)=0. The mean identity applied to g·v/ζ gives Re b'·v'(0)=0. Differentiating again along the straight real line in the covector parameter and using lines 127–136 of Proposition 9.24.4, with φ=ξ=a_1=0, yields

    D²H_a(b')[δb,δb] = Re δb·v'(0)
       = B(v,v) = (1/2)∫ rho D²r(f)[v,v] dm >= c_f' ||v||_{H²}².

All signs here use the real Hessian and the exact positive multiplier in the integrated proof. Equality implies v=0. The linearized stationary equation then gives h=(λ/rho)g on the circle, where h=∂_δb g and λ is real. The holomorphic wedge h∧g vanishes on the boundary, hence identically. The nowhere-zero lift (Lemma 9.24.2) lets the ratios glue to a holomorphic scalar with real boundary values, therefore a real constant. Thus δb=h(0) is a real multiple of b'. Conversely such a variation is obtained by positive scaling of g,rho, leaving f unchanged; local uniqueness in Proposition 9.24.4 shows v=0. Consequently the Hessian has exactly the real radial kernel R b' and is positive definite on its Euclidean orthogonal complement. This gives a local curvature statement for the support function at every covector admitting the stated stationary disc; it does not assert global existence of a stationary disc with every prescribed covector or certify the upstream geodesic existence proof.

Further, for nearby b_1,b_2 with fixed a, apply (1) in both directions and add. The constants are uniformly positive after shrinking the parameter neighborhood (rho varies continuously in H^s, s>=2). With f_i=f_{a,b_i},

    2c_* ||f_1-f_2||_{H²}²
        <= Re (b_1-b_2)·(f_1'(0)-f_2'(0))
        <= |b_1-b_2| ||f_1-f_2||_{H²}.

Thus a quantitative Hardy-norm Lipschitz estimate holds, with constant (2c_*)^{-1}. This also directly rules out two distinct smooth stationary discs with the same a,b, without a local restriction. Their lifts are identical as well by the real-ratio argument and equality of g(0).

Suggested insertion: corollary after Proposition 9.24.4, with the preceding hypotheses and explicit local qualifier. No source/body edit. Theorem 9.24.5 continues unchanged; any application to a global indicatrix curvature theorem must separately establish that the stationary covectors cover all nonzero covectors. Conditional on the actual preceding stationary-disc results, not a full transitive certificate.

## Other actual coverage

* §9.24: whole direct mathematical lines 7–202 (blob above). Checked finite-order almost-analytic inverse estimates in Lemma 9.24.1 (EEFBD40AC261), reflection distributional boundary cancellation, total reality of projectivized conormal graph and positive radial derivative in Lemma 9.24.2, translation-invariant compressed coercivity in Lemma 9.24.3 (106A14BC1AFE), the right inverse and Fourier orthogonality signs, holomorphic frame ODE, and parameter inverse differential in Theorem 9.24.5. No new confirmed error or demonstrated proof gap. Historical selected review from 14 November retained.
* §9.20: selected Theorem 9.20.5, lines 173–205, tag 7264782B9A80, docs/sections/complex-geodesics-on-bounded-convex-domains/index.html, blob 406faf6cf759c6aa6ed9b0cee3792ba6b5a85f65. Checked convex exhaustion and Green pole comparison; preceding extremal existence and stationary-lift proofs not certified here.
* §10.10: whole introductory mathematical lines 8–20, docs/sections/bott-chern-classes-and-singular-loci/index.html, blob d7e500c4b129e9e54b4d9d606cbda70beba65c69. Overview only; regularization-dependent assertions recorded as premises, not reopened.
* §10.19: selected nonexcluded mathematical lines 7–137 and 178–289, docs/sections/bott-chern-classes-and-singular-loci--currents-on-the-elliptic-threefold/index.html, blob 412042bdf10c98ab00bb1cb589bb0d4b0373f6c1. Lemma 10.19.1 (464DA68EB4DA/C0D1D555), Proposition 10.19.2 (24BCA82D5034/1A9B20A5), Proposition 10.19.4 (2555699F5657/4D5717F0), Proposition 10.19.8 (141C0ACF5576/594F13F8), Proposition 10.19.11 (983D2EEDBE68/AB84E173). Checked positivity plus Stokes descent conditional on Lemma 11.22.4, BC injectivity by compact connected fiber harmonicity, trace factor 8π(a+b), envelope supremum/usc pullback and truncated cube vanishing conditional on the cited product lemma, cubic volume factor 24π, Gauduchon square trace 8π(xy+xz+yz), rank-two square obstruction and denominator exponent q/3. For minimizing metrics and perturbation independence retain Theorem 12.2.3 and Proposition 12.20.1 as conditional inputs. Lines 139–176 on weighted sections and kernels not counted; excluded programme not reopened. No new confirmed error or demonstrated gap in the reviewed portions.
* §9.26: repeated direct lines 7–67, blob c04701d0358d43a3a3f1aed61e7cdd2a48305417, docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html. Checked countable smooth sum, proper closed graph and sublevel exhaustion; earlier 24 November whole review not counted as new coverage. Fixed regularized maximum premise not reopened.

Totals: one whole mathematical section, one whole introduction, two selected sections, one repeated whole-section check. One new conditional deduction, zero new confirmed printed errors, zero demonstrated proof gaps, zero complete transitive certificates. Historical first visits not asserted. No project tests/build/CI, publication, production edits, or changes to source/registry/tags. Demailly regularization and all designated completion programmes remain deferred-by-user. Matrix row count preserved; full TOC re-comparison was not completed in this run.
