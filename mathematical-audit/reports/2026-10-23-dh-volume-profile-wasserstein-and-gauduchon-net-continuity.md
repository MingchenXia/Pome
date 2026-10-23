# Mathematical audit: DH volume profiles and Gauduchon-normalized current nets

**Checkpoint:** 2026-10-23, 18:00–18:05 Asia/Shanghai (actual work in this session; not a claim of inter-session computation). **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** selected nonexcluded proofs in §22.1 (DH measures, §§22.1.54–22.1.60) and §20.4 (Bott–Chern/Gauduchon normalization, §§20.4.19–20.4.24). This is not a complete review of either section or their upstream analytic theory. The chapter inventory remains 25 chapters / 747 reader sections.

The required main AGENTS.md, documentation/proof-expansions.md and current table of contents, plus review/mathematical-audit README.md and mathematical-audit/LATEST.md, were freshly read. The specific integrated sources and supporting proofs below were read from **current main**, not merely from historical source manuscript numbering.

## Exact integrated source anchors and dependencies

- docs/sections/non-archimedean-pluripotential-theory/index.html, blob 8448d710690ebe1cc28040f9611d05c9d008a961: Definition 22.1.55, source sgpt:115B0C00, permanent tag 9ADEFD2FF381, lines 907–912; Theorem 22.1.56, source sgpt:420C36E9, tag 0AD7F80A793D, lines 915–997; Eq. 22.1.57 tag A51020D58E6F, lines 917–919; Proposition 22.1.60 tag 492A145E9067, lines 1012–1091. Rechecked its finite-first-moment boundary and the role of mass conservation in monotone DH convergence. The proof of the full partial-body continuity theorem was **not** independently established here.
- docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html, blob 20ff3089e62dd1c8349e8bcc077ec64605a9788b: Definition 19.6.18, source sgpt:09132002, tag 51940EF88F4F, lines 328–334 (DH as concave-transform pushforward); Proposition 19.6.19, source sgpt:DE3D564A, tag F397AFA38927, lines 337–365 (extended moments); Definition 19.6.1 tag ACD722F45231, lines 9–44 (nested convex bodies); Proposition 19.6.4 tag 29A7DDA38CA2, lines 48–60 (interior continuity).
- docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html, blob a53c6b2f80c3775e9d646f57808425823ec4a4ac: Theorem 19.5.26, source sgpt:9B46A73A, tag 944BC14A8246, lines 311–339, especially Eq. 19.5.27, tag E0BB6985CB53, lines 313–318 (body volume equals non-pluripolar mass divided by n!). The comparison/continuity and its excluded upstream approximation inputs remain conditional.
- docs/sections/divisorial-currents-on-compact-modifications/index.html, blob 79d6e21f9d3784bf3761846f77f90ad075253644: Lemma 20.4.20, source non-kahler-pluripotential-theory:281A4711, tag 721E66DF8C88, lines 381–429; Eq. 20.4.21 tag 641BFD39D2E5, lines 388–390; Proposition 20.4.22, tag D7373D3639FA, lines 437–464; Corollary 20.4.24, tag AC7947F570DB, lines 469–480. The finite-dimensional elliptic normal form was checked at the proof-step level, not its entire elliptic Fredholm prerequisite.
- docs/sections/gauduchon-traces-and-the-topology-of-potentials/index.html, blob 1516feb665870be31c5be159edb6c2cf1898db8c: Green inverse Eq. 11.31.3, tag 67B93429179F, lines 65–73 (context only).

The history includes POME-NA-DH-STOCH-001, already establishing stochastic order for ordered curves with a common left-end model. **The result below is the distinct, quantitative absolute-value / optimal-transport identity**, not a relabeling of that earlier finding. Prior exceptional-coefficient weighted-ell-one estimates from §20.4.26 are likewise not recounted.

## POME-NA-DH-W1-PROFILE-001

**Status:** verified conditional deduction; **severity:** low. Not a false source theorem. **Suggested location:** a new corollary after Theorem 22.1.56, with Definition 19.6.18 and Theorem 19.5.26 as internal dependencies.

Let X be a connected compact Kähler n-fold, let θ represent a big class, and let Γ and Λ be two positive-mass non-Archimedean model test curves in PSH^NA(X,θ)_{>0}, with **the same left-end model** Γ_{-∞}=Λ_{-∞}. Let M=vol Γ=vol Λ>0 and μ=DH(Γ), ν=DH(Λ). Assume the **finite first absolute moments** ∫|x|dμ(x)<∞ and ∫|x|dν(x)<∞; in the finite-energy conventions of §19.6, this is precisely the necessary tail integrability condition. Put

\[
V_\Gamma(t)=\mu([t,\infty)),\qquad V_\Lambda(t)=\nu([t,\infty)).
\]

For t<Γ_max one has the exact survival identity

\[
V_\Gamma(t)=n!\operatorname{vol}_{\mathbb R^n}\Delta_{Y_\bullet}(\theta,\Gamma_t)
=\operatorname{vol}(\theta+\mathrm{dd}^{\mathrm c}\Gamma_t).
\tag{A}
\]

At t=Γ_max the mass of the terminal atom is

\[
\mu(\{\Gamma_{\max}\})=\lim_{t\uparrow\Gamma_{\max}}
\operatorname{vol}(\theta+\mathrm{dd}^{\mathrm c}\Gamma_t),
\tag{B}
\]

and V_Γ(t)=0 for t>Γ_max; analogous assertions hold for Λ. These formulas do not depend on the flag.

**Exact metric identity.** For the one-dimensional Wasserstein distance with cost |x-y|,

\[
\boxed{
W_1(\mu/M,\nu/M)=\frac1M\int_{\mathbb R}
\left|V_\Gamma(t)-V_\Lambda(t)\right|\,\mathrm dt.
}
\tag{C}
\]

In particular, if Γ≤Λ in the test-curve order, the pre-existing stochastic order gives V_Γ≤V_Λ and

\[
\boxed{
M W_1(\mu/M,\nu/M)
=\int_{\mathbb R}x\,\mathrm d\nu(x)
-\int_{\mathbb R}x\,\mathrm d\mu(x).
}
\tag{D}
\]

Thus, for ordered equal-left-end curves of finite energy, the transport distance is **exactly** the difference of their DH first moments divided by the common mass. The constant is optimal; for two constant-in-τ left-end curves whose DH measures are Mδ_a and Mδ_b with a<b, equality is W1=b-a.

**Proof of (A)–(B).** For an Okounkov test curve Δ_t, the concave transform is G(x)=sup{t:x∈Δ_t}. Since the nested compact convex bodies vary continuously at every interior t (Proposition 19.6.4), the superlevel set {G≥t} equals Δ_t, up to boundary sets of Lebesgue measure zero (in fact equality holds with the standard endpoint convention). By Definition 19.6.18, μ=n!G_*(Lebesgue|Δ), so μ([t,∞))=n!vol Δ_t. Theorem 19.5.26(1) proves the second equality in (A). As t increases to Γ_max, the compact sets decrease to the terminal level Δ_{Γ_max}, and ordinary continuity from above for finite Lebesgue measure proves (B). The equality (A) is also valid in the presence of atoms at interior t, with the **closed** superlevel convention; no atom is discarded. The finite-first-moment assumption is not required for (A)–(B).

**Proof of (C) without external optimal transport theory.** Write p=μ/M, q=ν/M. For any coupling (X,Y) with laws p,q, the pointwise layer-cake identity

\[
|X-Y|=\int_{\mathbb R}|\mathbf1_{\{X\ge t\}}-\mathbf1_{\{Y\ge t\}}|\,\mathrm dt
\]

and Tonelli give

\[
\mathbb E|X-Y|\ge\int_{\mathbb R}
|p([t,\infty))-q([t,\infty))|\,\mathrm dt.
\]

Conversely, let U be uniform on (0,1) and let X=F_p^{-1}(U), Y=F_q^{-1}(U) be the left-continuous generalized quantile functions. At any fixed threshold t, the events {X≥t} and {Y≥t} are upper intervals in U and hence are nested, so the above triangle inequality is an equality after expectation. This coupling attains the lower bound, proving (C). Finite first moments ensure both sides are finite. For Γ≤Λ, superlevel inclusions give the previously recorded stochastic order V_Γ≤V_Λ, and the ordinary layer-cake expression for the difference of the expectations yields (D). **QED.**

**Consequence and precise boundary:** equation (C) is an isometry between equal-mass DH probability measures and their distributional survival profiles in L1(dt). It does not claim injectivity of Γ↦DH(Γ), nor W1 convergence from vague convergence alone. Positive mass and equal left-end mass are essential for the particular normalization. There is no claim of finite W1 for arbitrary positive-mass curves without the moment hypothesis. **Affected dependents:** §§22.1.56, 22.1.60, 19.6.19, and later finite-energy NA metric comparisons.

## POME-BC-GAUD-NET-L1-001

**Status:** verified repair (of a missing net-topology justification, **not** a false statement); **severity:** low. **Exact location:** Lemma 20.4.20, especially the sequence-only compactness argument at lines 420–428, although the statement says continuity on the full weak topology. No claim that the lemma as stated is false.

**Claim:** If (T_α) is an **arbitrary directed net** of positive closed real (1,1)-currents converging weakly to T on a connected compact complex manifold Y, and γ is a fixed Gauduchon metric, then the normalized distributions u_α=v_γ(T_α) converge to u=v_γ(T) in L1(Y,γ^n), without a sequential-cofinality assumption. The smooth harmonic representatives B_γ(T_α) also converge to B_γ(T) in every C^l norm.

**Complete topological bridge.** The pairing m(T)=∫_Y T∧γ^{n-1} is a continuous scalar functional, so m(T_α) is eventually bounded. The proof of Lemma 20.4.20 constructs B_γ by an elliptic projection onto the finite-dimensional smooth kernel of P, continuous on distributions; hence B_γ(T_α)→B_γ(T) smoothly, and all later B_γ(T_α) are uniformly bounded. From T_α≥0 follows dd^c u_α≥-B_γ(T_α)≥-Cγ for one fixed C on a tail, while ∫u_α γ^n=0. The classical compactness theorem for quasi-psh functions with a common smooth lower bound and fixed mean (the same compactness invoked in the printed proof via Theorem 5.25.2) makes this entire tail **relatively compact in L1**, not merely sequentially convergent along a chosen extraction. The normalized elliptic inverse, continuous in distributions, simultaneously gives u_α→u in the distribution topology. Every L1-convergent subnet must therefore have limit u. If the original net failed to converge to u in L1, some L1-open neighborhood U of u would be avoided cofinally, furnishing a subnet entirely outside U; relative compactness supplies an L1-convergent further subnet with limit u, a contradiction. Therefore u_α→u in L1. This argument uses genuine net compactness and never selects a countable cofinal sequence. **QED.**

**Proposed correction:** append the last compactness/unique-cluster paragraph to the proof of Lemma 20.4.20; Proposition 20.4.22 can then cite actual L1 continuity for nets as well as for sequences, while any additional pullback continuity beyond the proven Lemma 5.43.19 must retain its own hypotheses. The current positive-current statement is correct conditional on the cited compactness and Fredholm inputs. Do not change labels, proof registry, main, sources, or published HTML in this audit branch.

## Coverage, exclusions, and checks

- Substantive first proof-level review for **22.1.54–22.1.60** (DH construction/moments/ordered convergence); first detailed net-topology audit of **20.4.19–20.4.24**. §19.6.18–19.6.19 and §19.5.26(1) were exact statement/dependency crosschecks. §11.31.3 was context-only. No section was completely certified, and the 747-section matrix is a catalog rather than a verification count.
- No independent proof was supplied here for the general partial Okounkov-body map or deep non-Archimedean analytic theorems (BJ22 etc.). Pre-existing corrections to §19.6.16 and the §22.1.88 left-tail recursion remain **unchanged and unresolved**; their proofs were not silently certified by this report.
- **Explicitly excluded/deferred-by-user:** Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme. Mentions of such upstream inputs were not followed. No project build, CI, website publishing, merging, source/registry/permanent-tag changes or formal verification was carried out.
- The independent finite rational-distribution check (if included beside this report) exercises only elementary one-dimensional transportation arithmetic, not any global non-Archimedean or elliptic theorem.
