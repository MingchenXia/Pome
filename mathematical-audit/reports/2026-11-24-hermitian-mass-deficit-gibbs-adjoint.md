# Hermitian mass deficit controls the Gibbs–adjoint discrepancy

Date: 2026-11-24. Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**POME-HERMITIAN-MASS-DEFICIT-GIBBS-ADJOINT-001** — low / verified conditional deduction; not a false printed theorem. In a genuinely nonclosed background, a small deficit from the positive lower Monge–Ampère mass forces every supporting probability (including the smooth Gauduchon adjoint) to be close in total variation to the normalized Monge–Ampère density. There is no assertion that these measures always coincide.

## Exact source and coverage anchors

All paths below are relative to the pinned main SHA, not the moving audit branch. Physical HTML line numbers are one-based.

- `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html`, blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`: whole mathematical lines 7–86; Lemma 11.37.1 (2E4E82F8C3FC), lines 20–50; Eq. 11.37.2 (803909FECEC0), lines 54–61; Proposition 11.37.3 (33DF3CE1122A), lines 65–76.
- `docs/sections/normalization-and-weak-adjoint-measures--entropy-bounds/index.html`, blob `d124ce19af09af2d0a65d655fe611e7b45804c3d`: whole mathematical lines 7–138, Proposition 11.38.1 (170451FB65CB), lines 11–48; Proposition 11.38.3 (A3720120A48C), lines 60–91; Corollary 11.38.5 (A13D502ACAAC), lines 103–128. Line 90 cites Theorem 5.32.1: the smooth approximation input is recorded but its proof programme is deferred-by-user. The new estimate below does not require the approximation or the sharpness part of Proposition 11.38.3.
- `docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html`, blob `9a4ba5a98abd3273a6872c68beccf764e936d3f0`: whole mathematical lines 7–82, repeat/context; Eq. 11.35.1 (FFB47018170B), Eq. 11.35.3 (88A1B49C1D77), Proposition 11.35.2 (0C21983AC42D), Theorem 11.35.4 (6830F8DE9750).
- `docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html`, blob `a8afa97be049b56b6c7d18302499364022feaa39`: selected lines 7–235 only; Eq. 11.34.1 (4DA0C1CF8861), Theorem 11.34.2 (86A7D85266AA), Proposition 11.34.5 (792D6FEF2F3C), Theorem 11.34.7 (A4850266BE73), Theorem 11.34.9 (7E60599DA339), Theorem 11.34.11 (F4FDB7BC8A03), Proposition 11.34.13 (D2CCD76890C8). The latter continuous-Hessian argument uses local product continuity and the Sobolev annihilator; no new certification of these or any approximation input.
- `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, blob `fff86de757578ed2be369ba752123f62f3d31044`: selected lines 7–64, Eq. 11.33.1 (9D47DB96B6E3).
- `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, blob `519e50338be6560f6b2856fddce212738f5109bc`: selected lines 7–68, Eq. 11.23.1 (BEA90D7B5428), Proposition 11.23.2 (0B0003A3A873), Eq. 11.23.3 (9140CF590948), Proposition 11.23.4 (A914D4D9C6CB).
- `docs/sections/non-pluripolar-monge-ampere-measures/index.html`, blob `5d0f652ffaaaef81cf74d1786082e429f71b3b89`: Definition 13.14.14 (EB45638CBB2C), lines 223–231, only.
- `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, line 123: connected compact complex manifold convention.

## Deduction and proof

Let X be connected compact, omega Hermitian, and take the zero reference as in Proposition 11.38.1. Fix a smooth positive probability volume dV. Assume the existence/uniqueness of the scalar and supporting probability facts stated in §§11.33–35, not their complete upstream chains. For F continuous real, write

    Z_F = integral exp(F) dV,
    M_F = exp(B_0(F)) Z_F,
    g_F = exp(F) dV / Z_F.

Thus M_F is the mass of any bounded solution at F; g_F is its normalized Monge–Ampère measure. Let H=H_0 and E=Ent_dV. For any probability nu of finite entropy (hence H finite by Proposition 11.38.1), define the nonnegative Fenchel defect

    delta_F(nu) = H(nu) - integral F dnu - B_0(F).

An elementary change of density, using that F is bounded and g_F has everywhere positive continuous density, gives

    D(nu || g_F) = E(nu) - integral F dnu + log Z_F.

Subtracting the two identities proves the exact formula

    delta_F(nu) - D(nu || g_F) = H(nu) - E(nu) - log M_F.     (1)

It holds in nonclosed backgrounds; the right-hand side is generally not zero. The previous closed-case identity is precisely the fixed-mass specialization and is not counted anew.

Put m=v_-(omega) and V=v_+(omega). If m>0, the mass definition and the equation imply, for every G continuous,

    B_0(G) >= log m - log Z_G.

Taking suprema in Eq. 11.35.1 and using Lemma 11.37.1 gives H(nu)-E(nu)>=log m for finite-entropy nu. If V is finite the opposite inequality H(nu)-E(nu)<=log V follows in the same manner. In particular (1) yields

    log(m/M_F) <= delta_F(nu)-D(nu || g_F) <= log(V/M_F),     (2)

where a zero lower mass or infinite upper mass supplies only the corresponding trivial extended bound. No identification of bounded and smooth mass extrema was needed for these inequalities.

For every supporting probability nu at F, delta_F(nu)=0 by Proposition 11.35.2. Its entropy is finite by Proposition 11.38.1. Consequently if m>0,

    D(nu || g_F) <= log(M_F/m).                               (3)

More generally, for any finite-entropy approximate minimizer with delta_F(nu)<=epsilon, (1) gives

    D(nu || g_F) <= epsilon + log(M_F/m).                      (4)

The full signed total-variation norm (not the half-norm distance) is bounded by

    ||nu-g_F||_TV <= sqrt(2(epsilon + log(M_F/m))).            (5)

Here is a direct proof of the probability inequality used in (5). Let r=dnu/dg_F, A={r>=1}, a=nu(A), b=g_F(A). Then ||nu-g_F||_TV=2(a-b). If b=0 or 1, absolute continuity and the definition of A imply equality of the probabilities. Otherwise Jensen on A and its complement gives D>=a log(a/b)+(1-a)log((1-a)/(1-b)). As a function of a, the right-hand side has value and first derivative zero at b and second derivative 1/a+1/(1-a)>=4 on (0,1). Integrating twice and extending to the endpoints by continuity gives D>=2(a-b)^2. This establishes (5), including the norm convention.

In particular, for *any* family of continuous log densities F_i, including a net, with M_{F_i}->m>0, and supporting probabilities nu_i, the difference ||nu_i-g_{F_i}||_TV tends to zero. Neither sequence compactness nor convergence of F_i nor a common modulus of continuity is needed. The same holds for approximate minimizers of defects tending to zero. This is a distance-between-pairs statement, not a strong compactness assertion about either family individually. Moreover the full TV diameter of the supporting set at any F is at most 2 sqrt(2 log(M_F/m)) by the triangle inequality. If a bounded solution with continuous positive density attains m, its supporting set is the singleton {g_F}, hence the scalar is Gateaux differentiable by Proposition 11.34.5.

For a smooth potential u with eta=omega+dd^c u>0, set F=log(eta^n/dV); then B_0(F)=0 and M_F=integral eta^n. By Theorem 11.34.9 and Proposition 11.23.2 its supporting probability is mu_u=rho_u eta^n. For n>=2 and any smooth real h, its stationarity and Eq. 11.23.1 give

    |n integral h dd^c(eta^(n-1))| / M_F
       = |integral L_u h dg_F|
       = |integral L_u h d(g_F-mu_u)|
       <= ||L_u h||_infty sqrt(2 log(M_F/m)).                (6)

The first equality is integration by parts on the compact manifold. In particular a smooth strictly positive minimizer of the bounded-potential mass must be Gauduchon; this also follows directly from the first variation at an interior minimum. The quantitative version (6) is the additional conclusion. It controls the normalized torsion test against the *varying* linearized-operator norm; no uniform ordinary C^2 estimate for degenerating eta is asserted. In dimension one the discrepancy vanishes by Stokes and the printed scalar formula.

At the other endpoint, if V<infinity then the Gibbs probability itself satisfies

    0 <= delta_F(g_F) <= log(V/M_F).

This follows by taking D=0 in (1) and using the upper bound in (2). Thus near maximal mass the Gibbs probability is an approximate dual minimizer, without an assertion of closeness to the particular adjoint unless additional stability is known. The distinction between the upper and lower endpoints is essential.

## Proof-check details and disposition

The entropy variational proof correctly handles singular measures with compact cutoffs, finite or infinite absolutely continuous entropy by truncation, and non-normalized volumes in §11.37. The change of reference volume shifts both entropy and H by the same integral. The two estimates in §11.38.1 use the correct signs and exponents: qG for the lower bound and G/n for the upper bound. The scalar comparison for the larger Hermitian background in §11.38.5 uses the bounded supersolution's smaller-background envelope; its strict-domination conclusion is conditional on the cited principle. The opposite sharpness tests in Proposition 11.38.3 (Gibbs versus smooth adjoint) have the correct direction. Its approximation premise remains deferred, not certified. The support proof in the selected portion of §11.34 has the correct signs for both one-sided derivatives, and the Baire argument uses the actual compact metrizability of X, not an unrestricted sequential-compactness assertion. The §11.35 sublevel argument first fixes a bounded test approximant and uses uniform absolute continuity to pass to the limit; the same estimate works for nets.

Remaining upstream inputs: bounded scalar existence, mixed-product concavity, scalar continuity, the density lower bound of Theorem 14.19.19, Gauduchon trace inequality 11.5.6, strict domination and the prescribed-reference bound of Lemma 15.12.2, and the smooth scalar derivative/adjoint theorem for (6). The closed-background mass identity of Theorem 13.8.7 is a dependency of §11.37, not of the new nonclosed estimate. These inputs are not transitively certified here. The Demailly approximation, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain deferred-by-user in full; no expansion of their prerequisites was undertaken.

Proposed change: optional quantitative corollary after Proposition 11.38.3, with the smooth consequence linked to §11.23.2. Affected related statements: §§11.34.5, 11.34.9, 11.35.2, 11.38.3; none is refuted. No source/registry/tag modifications. No tests, builds, CI or publication. Existing closed-case KL/Fenchel, cyclic-support, entropy logarithmic modulus and non-strong-compactness findings are distinct and not relogged. Whole direct current mathematical sections §§11.37–38, whole context repeat §11.35, selected §§11.34, 11.33, 11.23, 13.14 and 1.1. Historical first-visit status is not inferred from unreconciled coverage.
