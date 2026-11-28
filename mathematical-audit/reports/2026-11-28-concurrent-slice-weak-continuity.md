# Weak continuity of normalized concurrent slices

Date: 2026-11-28. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Finding **POME-CONCURRENT-SLICE-NORMALIZED-LIFT-CONTINUITY-001** — low / verified conditional deduction, not a printed error or a mandatory source change.

## Exact reading-edition anchors and scope

- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--concurrent-slices-of-positive-currents/index.html`, blob a851fa12c59217cbf13efd381fd44524388fcfdc: whole direct mathematical lines 7–278. Lemma 6.41.1 (source 59B332CD, permanent CACB97220D52), 11–28; Theorem 6.41.2 (05D6D4BD, 53506FB921EB), 33–53; Proposition 6.41.5 (DF50783B, F5E0CCA7AC78), 70–106, normalized lift equation 6.41.6 (D383A0E4, 6A499DD7511C); Lemma 6.41.7 (42D1CA7F, 2A216A0952DC), 111–128; Proposition 6.41.9 (CE3E3EB2, BAA80DBD5575), 133–159; Lemmas 6.41.11 (362F03AB, CE378B92124B), 164–197, and 6.41.13 (265B19B3, A33ABBC95853), 202–232; Theorem 6.41.14 (1B549607, 5BC026092C60), 237–278.
- `docs/sections/real-currents-submersions-and-homotopies--normal-currents-supported-on-a-differentiable-submanifold/index.html`, blob f89355e610fd1711a2397855116df4d1325d58df, Theorem 5.56.3, permanent D47CED9844B5, selected lines 75–102: support and normal-current descent.
- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--lelong-densities-of-positive-currents/index.html`, blob 48bb9c525a826e4d1e337b755fac22aaa3016e66, Theorem 6.33.1, permanent 7ACCEC6E0526, selected lines 26–52: open-ball density and annular identity.
- `docs/sections/positive-current-extension-and-analytic-integration--extension-of-positive-currents-across-complete-pluripolar-sets/index.html`, blob 6b5be95436780409c8ab09f7f344899ac9047e7a, Theorem 5.60.3, permanent BB0A0DD22A5E, selected lines 70–96: zero extension premise and first closedness step.
- `docs/sections/bott-chern-classes-and-singular-loci--minimal-multiplicities-and-the-non-nef-locus/index.html`, blob 4d539e9ebfc9a442d4c93b9fe72c07e9e65d2802: nonexcluded lines 7–31, 38–53, nef-to-vanishing implication at line 55 and qualification at 60. Definition 10.12.1 (67B41EFA, 72E9AF170CBA), Proposition 10.12.2 (F84812AE, 4075D8C83DE1). The reverse implication uses 5.36.3 (lines 34,55); that regularization programme remains deferred-by-user. Analyticity of Lelong level sets (5.34.2) is a conditional input.

## Statement

Keep the normalization and hypotheses of 6.41.5 and 6.41.9: T is a closed positive (c,c)-current on B(0,R) in C^n, p=n-c, c<=q<=n, d=q-c, G=G(q,n) with invariant probability nu_q, and Y the tautological rank-q bundle restricted over the ball. Write pi(z,S)=z, sigma(z,S)=S, E=pi^{-1}(0), beta=dd^c |z|^2. For any net of closed positive currents T_i converging weakly to T on the ball, the *normalized* incidence lifts hat(T_i) converge weakly to hat(T) on Y. In particular, for every smooth compactly supported form theta of bidegree (d,d) on Y,

    integral_G | (T_i)_S(theta|_S) - T_S(theta|_S) | d nu_q(S) -> 0.

Slice pairings here denote their individual L^1 equivalence classes, not a single full-measure set for an uncountable collection of indices. Neither convergence of Lelong numbers nor full-sequence almost-everywhere convergence is assumed or asserted.

## Proof

### 1. Local compactness and uniqueness away from the critical codimension

The endpoint q=n is the identity lift; c=0 is the nonnegative-constant-current case on a connected ball (including q=0), so the assertion about lifts is immediate there. Otherwise put N=(q-1)(n-q) and use the Kahler form omega_Y of 6.41.5. Fix radii 0<a<b<R. Eventual boundedness of the trace mass of T_i on B_b follows from testing against a nonnegative cutoff times beta^p, with support in a slightly larger ball. By 6.33.1, D_i(s)<=D_i(b) for s<=b, where D_i(s)=s^(-2p)(T_i wedge beta^p)(B_s).

In the trace formula of 6.41.5, lines 89–103, the k=0 punctured term is D_i(a)-nu(T_i,0), bounded by D_i(b). For k>=1, alpha<=|z|^(-2)beta and the same dyadic annuli as in the printed proof give a summable uniform bound by a constant times D_i(b) times sum_l (2^(-l)a)^(2k). All constants depend only on the fixed incidence geometry and radii, not on i. If q=c, the added term nu(T_i,0)[E] also has uniformly bounded trace mass on compact sets because nu(T_i,0)<=D_i(b). The fibers of pi are compact; consequently the normalized lifts have an eventual uniform trace bound on pi^{-1}(B_a).

For an arbitrary net, work on any fixed smaller ball first: the positive coefficient measures with this total trace bound lie in a weakly compact set on the smaller open incidence domain, by coefficient domination and weak-* compactness of bounded Radon measures. This avoids a simultaneous eventual bound on countably many compact sets or any sequential compactness assumption on an arbitrary topology. Any cluster current U is closed positive and agrees with the submersion pullback of T off E, by weak continuity of submersion pullback. If q>c, U=hat(T) by the closed order-zero uniqueness assertion in 6.41.5, line 105. A net in a compact Hausdorff set having just one cluster point converges to it. As the smaller radius is arbitrary, this proves local weak convergence.

### 2. Critical codimension q=c: the compensating atom is essential

For 0<c=q<n, the difference U-hat(T) is a closed order-zero current supported on E with real dimension exactly dim_R E. Theorem 5.56.3 gives its unique representation as the pushforward of a closed top-dimensional current on E. In oriented coordinate charts that top-dimensional current is a distribution with all first derivatives zero, hence constant by mollification. Since E is the connected Grassmannian, U-hat(T)=k[E] for one real constant k. No positivity of this difference is needed.

Choose a smooth radial cutoff h:[0,R)->[0,1], equal to 1 near 0, nonincreasing and zero outside a radius strictly smaller than the local compactness radius. For any normalized lift L=hat(A) in this critical codimension, the positive Radon measure M_A=pi_*(L wedge sigma^*nu_q) has

    M_A(B_s)=D_A(s)

by 6.41.9, because the fibers' slices are measures (d=0). The pushforward is proper on the ball. By the layer-cake identity and Tonelli,

    L(h(|pi|) sigma^*nu_q)
      = integral_0^R (-h'(s)) D_A(s) ds
      = integral_{B_R} H(|z|) (A wedge beta^p),
    H(t)=integral_t^R (-h'(s)) s^(-2p) ds.

H(|z|) is a smooth compactly supported function: h' vanishes near 0 and outside a compact subinterval. Therefore the right side converges directly under weak convergence of the original currents, *also for nets*, without an unjustified dominated-convergence theorem for nets. The left test evaluates on [E] to 1. Passing along any cluster subnet gives k=0. The same compactness argument now proves convergence of the entire lift net.

This is a compensation phenomenon, not continuity of nu(T,0). For example in C^2 with c=q=1, take T_j=[z_1=1/j] and T=[z_1=0]. The Lelong numbers at 0 are respectively 0 and 1. The normalized lift of T includes the zero-section term, and the conclusion nevertheless holds. The unnormalized zero extensions cannot converge to the unnormalized zero extension of T in this example: the former equal the normalized lifts, whereas the latter differs from the limit by [E].

### 3. L^1 convergence of smooth slice pairings

Apply the local convolution decomposition of 6.41.1 to the already established weak convergence of the lifted positive closed currents. The proof at lines 23–27 works for nets on each fixed buffered compact chart: choose the L^1 kernel approximation first using the eventual coefficient variation bound, then use finitely many smooth tests from the uniformly compact family of translated smooth kernels. This gives L^1 coefficient convergence of the corresponding U_i,V_i on the smaller chart.

Use finitely many submersion product charts covering supp(theta), with a smooth partition of unity on a neighborhood of that support. In each chart the restriction to a fiber is U_vert+d_z V_vert, as in 6.41.2. Fiber integration by parts bounds the absolute difference of the pairings by the integrals of the differences of the coefficients of U_vert and V_vert times bounded test coefficients and bounded first fiber derivatives. Integrating this bound over the base using the smooth density nu_q and Fubini bounds it by a fixed constant times the local L^1 coefficient differences. Finite summation proves the stated L^1 limit. This controls every fixed compactly supported smooth test, not an uncountable simultaneous exceptional-set assertion. The endpoint lifts satisfy the same slicing argument.

## Audit assessment and proposed action

The direct read checked the coefficient Laplace homotopy sign, vertical Fubini and distributional closedness, all endpoints c=0/q=n/q=c, the incidence dimension N+p versus dim E, the punctured k=0 term, dyadic shell exponents, the annular primitive in 6.41.7, the invariant probability constant, the beta integral in 6.41.11 (including d=1 integrability), the pole-preserving primitive in 6.41.13, and the exact use of uniqueness in the GL_n averaging argument of 6.41.14. The latter is the original local group averaging used to prove slicing, not the excluded Demailly approximation programme. The strengthening uses no such approximation of the input. The printed assertion of only subsequential a.e. convergence is not false. Proposed optional addition after 6.41.9 or 6.41.14: the normalized-lift weak continuity and fixed-test L^1 stability just proved; potential applications to passing to limits in concurrent-slice constructions. No source change proposed as mandatory.

In 10.12, decreasing allowed negative error indeed gives increasing minimal Lelong numbers, the two background metrics yield cofinal families, and the countable union uses the correct positive thresholds. The nef-to-vanishing implication follows directly from the bounded normalized envelope. The converse proof's regularization input is explicitly deferred, not audited or certified. No new confirmed printed mathematical error or demonstrated proof gap was found in the reviewed portions. The minor duplicated wording 'fundamental solution ... of fundamental solutions' at 6.41.1 line 17 is editorial, not a mathematical error.

Upstream conditions retained: local current compactness and trace domination, 5.56.3, 5.60.3, 6.33.1, invariant averaging 5.57.11, the classical products/generalized Lelong mass results 7.31.2, 6.34.11 and 6.33.8, and coordinate invariance and semicontinuity 6.33.10/13. The present proof uses only the relevant downstream consequences; no full transitive certification. No tests, build, CI, production changes, or Demailly/Bergman/L2/OT/multiscale/positivity-loss programme work. Historical first visits remain unreconciled.
