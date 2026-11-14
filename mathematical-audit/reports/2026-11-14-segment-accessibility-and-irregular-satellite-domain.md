# Segment accessibility, L-regularity, and a genuinely open-set satellite counterexample

Date: 2026-11-14. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Scope: the integrated reading edition, Chapter 16, §16.32, with the polar-obstacle result in §16.31 as context. All excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes are **deferred-by-user**, neither checked nor certified here.

## Exact source coordinates and statuses

- Integrated **docs/sections/maps-and-regularity-of-global-extremals/index.html**, main blob **b20154011d37d46a4d0cc7751863207e5debf183**; section permanent tag **9D8F31A4DFA0**.
- **Proposition 16.32.7**, source label **klimek-pluripotential-theory:BC2EEB85**, permanent tag **5886156A306E**: printed statement at physical lines **136–138**, proof **142–145**. The printed segment lemma and C¹-domain conclusion remain correct.
- **Proposition 16.32.8**, source label **klimek-pluripotential-theory:4FCB31A8**, permanent tag **7C8B2A4D660E**: statement **150–151**, equal-dimensional C¹ critical-value and smooth-domain approximation proof **156–161**. No false theorem established.
- Context: **docs/sections/logarithmic-families-and-a-fixed-ball-capacity/index.html**, main blob **98d00aa7b2db4f81163a56d6f448946fd0c75499**; **Proposition 16.31.2**, source **klimek-pluripotential-theory:A0CCE53C**, permanent **A76B9D558430**, physical lines **36–53** (pluripolar obstacle invariance). The counterexample below gives a direct pole-perturbation proof instead of requiring a new certificate for this proposition.

### Finding POME-LREG-INTERIOR-SEGMENT-001

**Severity:** low. **Status:** verified conditional deduction. **Correct theorem strengthened, not refuted.**

Let Ω be a nonempty bounded open subset of C^n. Assume that for **each** a in ∂Ω there exist a vector v_a ≠ 0 and ε_a > 0 such that

    a + t v_a ∈ Ω  for every 0 < t ≤ ε_a.

Then the compact set K = closure(Ω) is L-regular, in the sense used in the integrated §16.32: the raw Siciak extremal is continuous (and its upper regularization is zero on K). In particular **every bounded Lipschitz domain has L-regular closure**, without requiring C¹ boundary. Neither a uniform choice of direction nor a uniform segment length is required.

**Proof.** For each x∈Ω, choose a closed Euclidean ball B_x ⊂ Ω with x in its interior. By inclusion monotonicity, 0 ≤ V_K^*(x) ≤ V_{B_x}^*(x)=0. Thus V_K is continuous and zero along every affine segment contained in Ω. Fix a∈∂Ω and choose the affine holomorphic map h(ζ)=a+ε_a ζ v_a on a neighborhood of [0,1]. For every real 0<t≤1, V_K is continuous and zero at h(t). The **actual** first assertion of Proposition 16.32.7 applies, giving continuity and value zero at a. The compact-extremal lower-semicontinuity and zero-star criterion invoked in the second paragraph of its printed proof yield L-regularity of K. Every bounded Lipschitz domain has an interior cone at each boundary point, hence a suitable interior segment.

The nonthinness of a real segment for planar subharmonic functions, the norm-ball Siciak profile, and the compact zero-star criterion are the existing §16.32.7 inputs; this run does **not** transitively certify their entire underlying potential-theory chains. The deduction itself is fully scoped to those inputs.

**Proposed correction/addendum:** No change to the printed proposition is required. A separately reviewable explanatory addendum may replace “C¹ boundary” in the corollary with the weaker segment-accessibility hypothesis (and mention the Lipschitz case), preserving source attribution and tags. **Affected dependents:** any use of boundary regularity in §§16.31–16.32 and later extremal estimates; their stronger general conclusions are not certified by this local argument.

### Finding POME-LREG-OPEN-CLOSURE-SATELLITES-001

**Severity:** low. **Status:** verified conditional deduction (a direct counterexample to an unauthorized strengthening, **not** to Proposition 16.32.7 or 16.32.8).

In complex dimension one, there exists a bounded open Ω such that K=closure(Ω) is **not** L-regular at a point of ∂Ω, even though Ω is a countable union of pairwise disjoint round discs, one of them the unit disc. The boundary point is a limit of genuine interior components; it is not a merely adjoined isolated polar point.

**Explicit construction and complete proof.** Put p=4, p_k=4+1/k (k≥1), a_k=2^{-k-2}, and s=Σ_{k≥1}a_k=1/4. Let

    U(z)=(1/(1+s)) [ log|z| + Σ_{k≥1}a_k log|z-p_k| - s log6 ].

This is the normalized logarithmic potential of the finite positive measure δ_0+Σ a_k δ_{p_k}, plus a constant, and so is subharmonic and lies in the logarithmic growth class L: the measure has compact support and total mass 1+s. It is not a Demailly regularization argument. On the closed unit disc, log|z|≤0 and |z-p_k|≤6, hence U≤0. At each p_k the potential is −∞; by upper semicontinuity choose pairwise disjoint sufficiently small closed discs D_k=closure(B(p_k,r_k)), disjoint from the unit disc and p, with U≤0 on each D_k. For instance additionally demand r_k < 1/[10k(k+1)]; shrink further if necessary to ensure the inequality.

At p the potential is finite and **strictly positive**:

    U(4) = (4/5)[ log4 - Σ_{k≥1}a_k log k - (1/4)log6 ]
         ≥ (4/5)[ log4 - 1/2 - (1/4)log6 ] > 0,

because log k≤k and Σ a_k k=1/2 (the displayed lower bound is approximately 0.35068). Set

    Ω = B(0,1) ∪ ⋃_{k≥1} B(p_k,r_k),
    E = closure(B(0,1)) ∪ ⋃_{k≥1} D_k,
    K = closure(Ω) = E ∪ {4}.

For every ε>0 let b(z)=log(|z−4|/6) and U_ε=(U+ε b)/(1+ε). Since |z−4|≤6 on E, both U and b are nonpositive there; b(4)=−∞. Thus U_ε belongs to L and is nonpositive on **all of K**, so is a legitimate raw extremal competitor. For every z≠4, letting ε↓0 gives V_K(z)≥U(z), including wherever U(z)=−∞.

Along the vertical approach z_t=4+it (t↓0), none of the poles p_k are met and

    log|z_t−p_k| = (1/2)log(t²+k^{-2}) → −log k.

For 0<t≤1 the absolute values are dominated by log k + log(√2), summable against a_k. Dominated convergence therefore gives U(z_t)→U(4)>0. It follows directly from upper regularization that

    V_K^*(4) ≥ limsup_{t↓0} V_K(4+it) ≥ U(4) > 0,

whereas **V_K(4)=0** because 4∈K and the zero function is an admissible competitor. Hence K is not L-regular at 4. Every disc in Ω has smooth boundary, but their accumulation geometry fails the pointwise interior-segment condition at 4. Note that K has nonempty interior and positive logarithmic capacity: the counterexample does not rely on a polar compact set.

This explicit perturbation also proves the needed **single-pole obstacle invariance locally in this example**, without merely citing §16.31.2 or assuming a false continuity property of the unregularized extremal.

**Proposed correction/addendum:** Keep the printed C¹ and smooth-neighborhood hypotheses. Add the explicit example as a warning against inferring L-regularity from “bounded open set” alone or from smoothness of each connected component. **Affected dependents:** applications of Proposition 16.32.7 or 16.32.8 after weakening boundary hypotheses.

## Selected proof audit of Proposition 16.32.8

The printed equal-dimensional C¹ critical-value lemma at line 157 uses a rank-deficient derivative at each critical point. On cubes of side h its first-order image fits into an (m−1)-dimensional O(h) box thickened by o(h) in the null direction; with O(h^(−m)) such cubes, the total outer m-volume tends to zero. This is the correct C¹, equal-dimensional threshold, and does **not** appeal to a general high-codimension Sard theorem. Applied to F=∇g for smooth g, a regular value a makes each critical point of g−a·x nondegenerate and isolated. On the compact level band there are finitely many, so a regular level can be chosen. The distance-function convolution bounds in lines 159–161 correctly confine the resulting smooth domain to the η-neighborhood of K. For a subset of C^n this invokes m=2n real coordinates. No error was found in these selected steps.

## Exact coverage, nonclaims, and provenance

New proof-level passages actually examined: §16.32.7 lines 136–145 and §16.32.8 lines 150–161, plus the contextual §16.31.2 statement and its pole perturbation lines 36–53. Earlier audit work had already examined selected §§16.32.1, 16.32.5, and Example 16.32.6; this report does not recast that work as new. **New first-visited numbered sections: 0; newly certified complete numbered sections: 0.** Actual production contents remain **25 chapters / 747 numbered sections**. This is a two-proposition incremental review, not certification of all §16.32. No production/source/registry/permanent-tag changes, no build, tests, CI, or publication claimed.
