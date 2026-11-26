# 2026-11-26 — Nonclosed Griffiths lower bounds and exact boundary flux

Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit-only notes, no edits to reading text, registry, tags or website. The designated Demailly approximation/regularization, Bergman, L2, OT, multiscale and positivity-loss proof-completion programmes remain deferred-by-user. No tests, build or CI performed.

## POME-SINGULAR-DETERMINANT-NONCLOSED-LOWER-BOUND-001

**Medium / local proof gap; verified local repair conditional on the zero-bound assertion of the same lemma. Not a false theorem.**

- `docs/sections/determinants-of-singular-bundle-metrics/index.html`, blob `901d6104f4a5ba01b188270bd6e2377ee4baeb9d`, Lemma 10.104.1, permanent EC118288B440, source 2FBA7F63, statement line 9, proof 15–18.
- `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, line 123: omega is Hermitian, closedness must be explicitly stated.
- Immediate dependent: `docs/sections/tautological-metrics-and-maximal-slopes/index.html`, blob `313098e0ab266ca5696a16775bc5277539dfe889`, line 46, which cites this lemma for the determinant of a singular direct-image metric. Only that dependency sentence was inspected, not the external direct-image existence/curvature theorem.

The final sentence at line 17 invokes a local potential of C omega. Such a potential need not exist for a nonclosed Hermitian form. For example, on C^2 the Hermitian form i exp(Re z2) dz1 wedge dbar z1 + i dz2 wedge dbar z2 is not closed, and cannot equal dd^c of a scalar on any open ball. This is a gap in the indicated argument, not in the conclusion. If the intended lower-bound definition already imposes closedness, the printed proof works in that narrower case; the following argument covers the actual general scalar-current interpretation.

Let H* be the local dual matrix of the given a.e. finite positive definite metric of rank r. Assume, in the current sense, dd^c log(v*H*v) >= -C omega for every nonzero local holomorphic dual section v (identically zero sections impose no condition), with the logarithms locally integrable. Here C >= 0. Work in a coordinate ball with a fixed strictly positive constant form beta. For every eta > 0 and point x choose a smaller ball V such that

    -eta beta <= C(omega(y)-omega(x)) <= eta beta, y in V.

Regard C omega(x) as a constant form in these coordinates. The constant form A = C omega(x)+eta beta dominates C omega(y) on V. It has a real quadratic potential q with dd^c q=A. Replace H* by exp(q) H*. The scalar dual logarithms of this matrix have nonnegative curvature by the assumed inequality and admit PSH representatives. Apply the zero-bound assertion of Lemma 10.104.1 on V. It proves local integrability of log det H* and

    dd^c(log det H* + r q) >= 0.

Consequently dd^c log det H* >= -r A >= -r C omega -2r eta beta on V. The same construction covers the coordinate domain; nonnegative partitions of unity on the support of any positive test form give the inequality there (multiplication is on the test form, no differentiation of the partition). Let eta tend to zero. This proves the exact bound dd^c log det H* >= -r C omega for nonclosed omega. Frame changes add a pluriharmonic logarithm to log det H*, so this is the determinant curvature globally. The rank factor is sharp already for smooth scalar multiples of the identity with a constant background and curvature exactly -C omega.

The zero-bound argument in lines 15–17 was directly checked: constant sections bound the matrix locally by the submean bound; positivity of the logarithm after positive averaging follows from the submean inequality and the integral version of Holder (or finite positive sums and passage to the integral). Smooth positive definite averaged matrices give the trace curvature inequality. The radial averaging of each constant-section squared norm is monotone in radius because it is subharmonic; the a.e. matrix convergence and the decreasing PSH logarithmic determinants then identify the local integrable weight. This check is not a new Demailly regularization programme and is not a certificate of every upstream smooth bundle curvature identity. The repair uses only the zero-bound statement and smooth constant-form twisting, not a singular approximation theorem. Proposed replacement: use the constant-form domination argument in the last sentence of line 17; do not change the theorem, permanent tag or external direct-image attribution.

## POME-NONPROPER-BOUNDARY-FLUX-POLYNOMIAL-001

**Low / verified deduction and explicit mass-normalization bridge; not a false printed theorem.**

- `docs/sections/boundary-flux-and-nonproper-mass-comparison/index.html`, blob `b9a79bd1d3254676b65d10031e314a2de1d5a0c4`, Proposition 16.43.1, permanent A9104D666EA7, source ED092E5C, lines 8–38; Corollary 16.43.2, permanent BD99C3A4D1ED, source C328B16E, lines 44–51.
- Boundary orientation input: `docs/sections/polynomial-families-and-equilibrium-null-obstacles/index.html`, blob `568257f81e9f31491e0cdde36ba8efb357423cd7`, Proposition 16.35.5, permanent 6F70A6B34439, source 5DEAA8D5, lines 82–89 (selected repeat).
- Mass citation: `docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html`, blob `943517743538820940559eae8469ce98ecf5fcd5`, Proposition 13.5.1, permanent 06A36B9354A5, source 187A0EF4, lines 11–26. This is a compact cohomological mass statement; the noncompact application at 16.43.1 line 38 needs the compactification bridge below, not a change of locator. Existence of a smooth proper biholomorphic image in Theorem 9.22.2, permanent CE10A564601F, is an existing input (statement only, line 50 of `docs/sections/a-smooth-boundary-for-a-proper-biholomorphic-image/index.html`, blob `1279ba00791fa992f753ddd35a63cfc0fa36973f`).

Let Omega have the indicated smooth patch; no global smoothness or boundedness is needed. Use the original notation gamma=log(1+|w|^2)/2, omega=dd^c gamma, psi=chi r with r<0 on Omega in the chart, chi nonnegative smooth compactly supported there and positive at a boundary point. For sufficiently small real t, omega_t=omega+t dd^c psi is strictly positive. Define M(t)=integral_Omega omega_t^n. Every coefficient in the difference is integrable because its support is compact and the background mass is finite. The exact polynomial is

    M(t)-M(0) = sum_{k=1}^n binom(n,k) t^k
       integral_{partial Omega intersect U} chi^k d^c r
                    wedge (dd^c r)^{k-1} wedge omega^{n-k}.

Indeed binomial expansion and closedness give for each k>=1 the exterior derivative of psi's compactly supported flux form d^c psi wedge (dd^c psi)^{k-1} wedge omega^{n-k}. Stokes in the smooth chart, with artificial boundary outside the support, identifies its integral with the boundary flux. On the real tangent bundle of r=0, dr vanishes and d^c psi=chi d^c r. The restricted dd^c psi equals chi dd^c r+d chi wedge d^c r. Every term containing the second summand dies when wedged with d^c r. The asserted formula follows with precisely chi^k. This reasoning requires neither global boundary regularity nor a limit interchange.

In particular

    M'(0)=n integral_{partial Omega intersect U} chi d^c r wedge omega^{n-1}>0.

The strict sign follows from the checked oriented-boundary calculation at 16.35.5, since omega is strictly positive. If the patch is Levi-flat (or merely the support of chi on the patch is Levi-flat), all coefficients with k>=2 vanish: d^c r on the real tangent hyperplane annihilates its complex tangent hyperplane, and the wedge with d^c r reads the restriction of the other factors to that complex hyperplane, where dd^c r vanishes. Hence M(t)=M(0)+t M'(0) **exactly** for all sufficiently small t, not just to first order. If instead the patch is Levi-semipositive relative to the outward defining function, all displayed coefficients are nonnegative. No Levi-flat hypothesis is needed for the printed strict inequality at small t. The exact formula applies conditionally to any such patch; it does not recertify the earlier Fatou–Bieberbach construction.

For completeness the full-space mass calculation uses Pome's dd^c=i/(2 pi) partial dbar convention. The Hermitian Hessian matrix of log(1+|w|^2) has eigenvalues (1+|w|^2)^(-1) with multiplicity n-1 and (1+|w|^2)^(-2) in the radial complex direction, including the limiting value at zero. Thus

    omega^n = 2^(-n) n! pi^(-n) (1+|w|^2)^(-n-1) dV.

Integrating in polar coordinates gives integral_C^n (1+|w|^2)^(-n-1) dV = pi^n/n! (substitute s=|w|^2 and then s/(1+s)). Therefore integral_C^n omega^n=2^(-n). Each higher term in the expansion of the full-space mass difference is the exterior derivative of a compactly supported form, hence integrates to zero. So integral_C^n omega_t^n=2^(-n) exactly. Alternatively extend psi by zero across the hyperplane at infinity in P^n and apply 13.5.1 to the smooth Fubini–Study background divided by two. This supplies the missing compactification explanation for the existing citation. The strict PSH pullbacks are as in the source; compactness of the boundary-separated sets {|psi|>=a} in Omega proves uniform decay of psi composed with the biholomorphism at infinity. Both masses remain finite and the polynomial gives their precise difference. Corollary 16.43.2 remains intact, conditional on 9.22.2.

## Actual scope and limits

- Whole current mathematics directly read and checked: §§10.104 (lines 9–18), 16.43 (8–51). One local proof gap with repair, one independent exact deduction, no false theorem.
- Selected dependency checks: §§1.1 (123–129), 13.5.1 (11–26), 16.35.5 (82–89), 9.22.2 (statement line 50), 10.108 (dependency line 46 only). §10.106 lines 8–89 re-read; prior whole-review status preserved, no new coverage credit. The ACC input in 10.106.1 not independently certified here. §16.18 was inspected for scope but not counted: it is adjacent to the smoothing programme, and no further proof-completion work was done on it. §10.102/10.105 were scope screens only, not audit coverage; excluded proof programmes not reopened.
- Current main table of contents (`docs/index.html`) has 747 section IDs. The pre-update matrix had exactly 747 distinct rows and every ID matched the TOC. Historical first visits remain unreconciled.
- No complete upstream chains certified; no reclassification of previously deferred work. No source patches or publication.
