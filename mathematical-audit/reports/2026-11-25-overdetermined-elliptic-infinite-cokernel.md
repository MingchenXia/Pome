# General unequal-rank obstruction for injective-symbol differential operators

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit parent: 69a1fdf6ae77eb83c667dae8890edec1e06e024a.
Finding: **POME-ELL-INJECTIVE-SYMBOL-GENERAL-RANK-OBSTRUCTION-001** — low / verified conditional deduction, not a false printed theorem. This generalizes, rather than relogs, the 2026-11-11 flat-torus gradient example POME-ELL-OVERDETERMINED-GRADIENT-COKERNEL-001.

## Anchors and scope

- docs/sections/differential-operators-and-elliptic-regularity--elliptic-operators-of-arbitrary-order/index.html, blob 24bf19943a31d603485b8e14f63fe05b1f55dd47: entire mathematical lines 7–187. Lemma 2.18.1 (0D76F8A1E29B, source tag 90E5290C), 29–55; Lemma 2.18.2 (3C443B01B6F3, E3EC92A3), 60–117; Theorem 2.18.3 (DB125476638D, 5AEC3D70), 122–151; Theorem 2.18.4 (912C25048C3D, E1228506), 156–187.
- docs/sections/differential-operators-and-elliptic-regularity--unique-continuation-for-scalar-principal-elliptic-systems/index.html, blob 41cad93307ca4c9ed8936118c03aa0106c5a0947: entire mathematical lines 7–128. Lemmas 2.16.1 (46A46C598F5E), 11–67, and 2.16.5 (0300AC2D4EAB), 72–110; Theorem 2.16.7 (F0BF9030844C), 115–128.
- docs/sections/open-maps-nuclear-spaces-and-inverse-limits--nuclear-spaces-and-completed-tensor-products/index.html, blob ecbf01a4ed81461ba32f1e0c88c6a550ebaa8135: selected mathematical lines 7–111 and 139–160 (tensor seminorms, Lemma 2.13.1 tag 67761F6CDA64, Proposition 2.13.2 D02C4838DC99, Theorem 2.13.3 A46D09531259, and Theorem 2.13.5 7434BE36F417). No claim to audit the Bergman-restriction part, lines 115–134.
- Heading-only §§2.11 (15F1008AA372, blob 99adde997e94fb2b2265f34f30ed566a3ceaa45c) and 2.15 (73E021597E92, blob 1d365c77d3f0306ab0fac8e87c65c2f5781d32aa), each line 5 of the correspondingly named section page. The headings have no mathematical body.

## General theorem

Let M be a nonempty compact smooth manifold without boundary of positive dimension, with smooth density and bundle metrics. Let P:E→F have positive order d, smooth coefficients and injective principal symbol at every nonzero real covector. Suppose ranks are constant, with rank F > rank E (for varying ranks it suffices that strict inequality holds on one positive-dimensional component). Then for every real s:

1. P:H^{s+d}(E)→H^s(F) has finite-dimensional smooth kernel K and closed range.
2. There is a bounded projection R_s onto this range on H^s(F), independent of s on common domains. It is the L²-orthogonal projection when s=0, maps smooth sections to smooth sections, and its complementary range is exactly the distributional kernel of P* in H^s(F).
3. The complementary range is infinite dimensional, and already contains infinitely many linearly independent smooth sections. In particular P is not Fredholm. Under injectivity of the principal symbol, the equal-rank condition in 2.18.4 is thus necessary for Fredholmness, not just a convenient sufficient assumption.

The zero-rank source case is immediate, so assume positive source rank. The proof below is conditional on the printed Sobolev and elliptic results 2.18.1–4, whose local arguments were directly read but whose full transitive dependencies are not certified.

### Projection and closed range

Put Q=P*P, of order 2d and invertible principal symbol, since the Fourier principal symbol is p_d(x,ξ)*p_d(x,ξ). Theorem 2.18.3 implies all distributional Q-null solutions are smooth. By integration by parts ker Q=ker P=K. Q is formally self-adjoint. Theorem 2.18.4 applied to Q gives, for every t, a bounded inverse G_t of Q from the annihilator of K in H^t(E) to the K-orthogonal complement in H^{t+2d}(E); extend by zero on K. Boundedness is also immediate from line 179 applied to Q. The inverses agree on overlapping domains by uniqueness. Here orthogonality in negative order is distributional pairing against smooth K.

Set R_s = P G_{s-d} P*. The formal adjoint P*:H^s(F)→H^{s-d}(E) has image in the annihilator of K since P K=0. Thus Q G_{s-d} P*=P*. Boundedness follows from the displayed orders, and R_s P u=P u for every u∈H^{s+d}(E) by GQ=I−Π_K. Consequently R_s is a projection, its range is precisely the image of P, and P*(I−R_s)=0; conversely R_s f=0 if P*f=0. At s=0 the range and complementary range are orthogonal by the adjoint identity. Elliptic regularity for Q makes G take smooth data to smooth sections. The kernel of P is finite-dimensional since it equals ker Q. No closed-range assumption for P* is needed.

### Infinite-dimensional cokernel: a local high-frequency argument

Choose a coordinate ball with a fixed nonzero real covector ξ0=dx_1. Since rank F>rank E, ker p_d(x,ξ0)* has positive rank. It is a smooth subbundle locally: the matrix projection I−p_d(p_d* p_d)^{-1}p_d* is smooth, and applying it to a fixed nonzero vector at the center gives a nonvanishing local section after shrinking the ball. Choose a nonzero smooth compactly supported section a in that subbundle in the ball and normalize ||a||_2=1. All symbols here are evaluated in local frames with the indicated bundle metrics. Define f_k=e^{2πikx_1}a, extended by zero. The sequence has L² norm one and tends weakly to zero. Indeed against any smooth test section the compactly supported integral tends to zero by integration by parts in x_1; smooth density in L² and the unit norm extend this to every test in L².

The leading k^d coefficient of P*f_k vanishes by the choice of a. Leibniz's rule gives P*f_k=e^{2πikx_1} Σ_{j=0}^{d−1} k^j b_j(x) with smooth compactly supported b_j independent of k. For each such fixed b, in the coordinate Fourier norm,

||e^{2πikx_1}b||²_{H^{-d}} = ∫ <η+k e_1>^{-2d}|b̂(η)|² dη = O(k^{-2d}).

On |η|≤k/2 the weight is O(k^{-2d}); on its complement use weight ≤1 and rapid Fourier decay of b, obtained by repeated integration by parts. The global bound follows from the equivalent localized norms of 2.18.1 (use a cutoff equal to one on the compact support). Thus ||P*f_k||_{H^{-d}}=O(k^{-1}). Since P G_{-d}:H^{-d}→L² is bounded, ||R_0 f_k||_2=O(k^{-1}).

The smooth sections h_k=(I−R_0)f_k belong to ker P*, converge weakly to zero in L², and have norms tending to one. If their linear span were finite dimensional, weak convergence would force norm convergence to zero (test against an orthonormal basis of the span). This contradiction proves the infinite-dimensional smooth cokernel. These smooth sections lie in every H^s, with I−R_s acting identically on them; the cokernel is infinite dimensional at every order.

The argument does not invoke the general pseudodifferential composition calculus, spectral asymptotics, approximation, or any excluded regularization programme.

## Direct proof checks and limits

§2.18: the Fourier 2π factor in the principal symbol, positive P*P extension by χ(Q−Q0)χ, compact-x Fourier kernel estimate (integrability requires N>|s−μ|+m), transposition and one-order gain, nested-cutoff iteration, compact lower-order embedding and finite-dimensional projection were checked. For fractional Sobolev coordinate invariance, the localized bi-Lipschitz argument and duality preserve both signs of s; the compactness proof only uses sequential compactness in metrizable Hilbert spaces. No new demonstrated error. The Fourier inversion/Plancherel, density and Riesz/Hilbert facts cited in the section are internal references or premises, not independently certified here.

§2.16: the Carleman commutator signs and factors in (2.16.4) are consistent with Δ=div grad, S self-adjoint and A skew-adjoint. The term −4at Re⟨Sv,v⟩ is absorbed by 1/2||Sv||²+8a²t²||v||²; the remaining positive t³ term controls the lower-order matrix perturbation. The ball-boundary weight is decreasing in x_1 on the shrunk chart and strictly negative on the closed nonzero-side annulus, giving the required exponential gap. The nearest-support-point argument uses compact Euclidean chart closure and connectedness. The Dolbeault principal-symbol application remains conditional on Theorem 10.46.6; no claim concerning arbitrary matrix-valued principal symbols. No new demonstrated error.

§2.13 selected: nuclear series factor through Banach spaces by the quotient of ℓ¹ by the synthesis kernel, and through ℓ² in the Banach case; the latter uses Cauchy–Schwarz, not injectivity of the tensor-to-operator map. The Hilbertian seminorm construction requires skipping indices, as printed. For strict exactness, the injective closed embedding and projective quotient are used at their respective topologies, then nuclearity identifies the topologies. The separation functional descends using the infimum over the closed subspace. The open-mapping/successive-correction proof and dominated extension in §2.12 are cited internal dependencies, not rereviewed transitively. The selected scope excludes the Bergman restriction discussion. No new demonstrated error.

## Proposed disposition

Keep 2.18.3–4 unchanged; optionally add the general rank-obstruction theorem as a separate corollary, retaining the existing gradient example as illustration. The equal-rank hypothesis should not be silently removed in any dependent Fredholm or index assertion. No downstream theorem is refuted or source patch proposed; exhaustive reverse-dependency enumeration not performed. No full transitive certificate. Two whole mathematical sections, two heading-only checks, one selected section; historical first-visit status not asserted. No project tests, builds, CI, source changes, registry changes, or publication. All user-excluded Demailly approximation, dedicated Bergman/L²/OT/multiscale/positivity-loss work remains deferred-by-user.
