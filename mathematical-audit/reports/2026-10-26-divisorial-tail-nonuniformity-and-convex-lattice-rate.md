# 2026-10-26 — Unbounded modification-wise divisor tails and a quantitative lattice count for every convex body

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Review scope:** first selected nonexcluded proof-level audit of §13.24.6–10 (countable divisor current, fixed-modification valuation tails, residual mass and explicit nonclosed surface example); incremental direct review of §19.7.4–14 and §19.7.20; §14.20.1 was checked solely as a normalization/dependency identity. **No review** of §13.24.1–5's analytic approximation construction, §18.7 or the author-excluded Demailly approximation/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme. Any cited excluded result remains deferred-by-user, neither resolved nor independently certified.

## POME-COUNTABLE-DIV-TAIL-NONUNIFORM-001

- **Status:** verified conditional deduction; **severity:** low as to the printed theorem, medium caution for future attempts at uniform valuative convergence. No Pome theorem refuted.
- **Integrated source:** `docs/sections/volumes-under-bounded-mass--volumes-of-multiplier-ideal-envelopes/index.html`, blob `0b4c115fa8ffbe1cdfa4fcac49875a76fa44fffc`, §13.24.6 at lines 176–190, Lemma **13.24.7**, current tag `487BF774470F` (source tag `F763B26D`), lines 191–225; Proposition **13.24.8**, tag `20027E32C14E`, lines 230–294. The original proof specifically **fixes** one modification `π` and one divisor `E` before introducing its tail constant at lines 212–225.
- **Hypotheses:** `X=P²`, countably infinitely many *distinct* projective lines `H_j`, positive coefficients `a_j` with `A=Σ a_j<∞`; use the original normalized potential `u=Σ a_j log(|s_j|²/||Z||²)-sup`. For a prime divisor E on a smooth modification π write `b_N(E)=Σ_{j>N} a_j ord_E(π*H_j)` and `b(E)=Σ_{j≥1}a_j ord_E(π*H_j)`.
- **Exact result:** For **every** N with a positive tail,
  [
    sup_{(pi:Esubset Z)} b_N(E)=+infty,
    qquad sup_{(pi:Esubset Z)}b(E)=+infty.
  ]
  The suprema range over all smooth compact modifications of P² and their prime divisors. Therefore the fixed-(π,E) convergence of Lemma 13.24.7 has **no globally uniform tail bound** over all divisorial valuations, even though `A_N=Σ_{j>N}a_j→0`. This does not contradict the lemma.
- **Proof:** Fix N and m>N. On H_m choose a point p outside `⋃_{j≠m}(H_j∩H_m)`, possible because that is a countable subset of the complex projective line. Blow up p, then repeatedly blow up the intersection of the strict transform of H_m and the newest exceptional curve. Let E_r be the new exceptional curve at the r-th blowup, and π_r the composite. Inductively the total transform of H_m has coefficient r along E_r: E_1 has coefficient one, and at the next transverse crossing the new exceptional multiplicity is the sum of the coefficients of the meeting strict H_m (one) and E_r (r). Every H_j with j≠m misses the original center p, so its pullback has coefficient zero along every E_r. Consequently
  [
     b_N(E_r)=a_m r=b(E_r)quad	ext{for every }rge1.
  ]
  Letting r grow proves both statements. Under the conclusion of the printed Lemma 13.24.7, the same values are the generic Lelong numbers `ν(u∘π_r,E_r)`; this interpretation, unlike the algebraic order calculation, is conditional on that lemma.
- **Why there is no conflict:** The lemma bounds `ν(r_N∘π,E) ≤ A_N C(π,E)`, with `C(π,E)=∫_Zπ*κ∧γ/∫_Eγ`. The constant varies with the modification and exceptional divisor; an estimate uniform over all π,E was never stated. The direct blowup calculation proves that such an estimate **cannot** be inferred.
- **Other selected checks:** The normalized Fubini–Study line-section potential satisfies `ddᶜℓ_j=[H_j]−κ`; the stated integral is `2∫_0^1(1-x)log x dx=−3/2`. The displayed equality `R=θ−Aκ>0` and `ddᶜθ=0` are sufficient for positive residual `R`. For the explicit §13.24.10 example, `τ=∂\bar α+\bar∂α` is real, `ddᶜτ=0`, while on the unit-cutoff chart its exterior differential equals the displayed nonzero 3-form. The full upstream all-weights ideal-equivalence theorem and extended-MA mass comparison are **not** certified here.
- **Proposed correction:** None to Lemma 13.24.7 or Proposition 13.24.8; optionally append a warning that the valuative tail convergence is pointwise in E, not uniform over all modifications. Preserve the original theorem's all-divisors quantifier and the historical attribution. **Affected dependents:** any attempt to swap the `N→∞` limit with an unrestricted supremum over prime divisors, or to infer a global modulus for divisorial profiles from summability alone. No such invalid exchange has been identified in the selected printed proof.

## POME-CONVEX-ALLBODIES-LATTICE-RATE-001

- **Status:** verified conditional deduction / optional self-contained quantitative strengthening; **severity:** low. Not a false printed theorem. Unlike the earlier internal lattice-count repair and the separate toric *polytope* facet-rate note, the assertion here gives an explicit inradius-based bound for **every full-dimensional compact convex body**, without any polytope or smoothness assumption.
- **Integrated source:** `docs/sections/almost-semigroups/index.html`, blob `33898b2963ad0f8b7e30bf414276642f60925b74`, Theorem **19.7.20**, current tag `85641516C8CA` (source tag `282DA4DD`), lines 299–319, especially the convex-body lattice conclusion at lines 314–318; convex geometry conventions in §19.7.2–7. The general Kaveh–Khovanskii semigroup-volume theorem retains its distinct historical and mathematical dependency; we do **not** claim to re-prove it.
- **Exact bound and hypotheses:** Let `K⊂R^n` be compact, convex, with positive n-volume, and suppose `x₀+ρ B̄⊂K` for an Euclidean ball of radius `ρ>0`. For every integer `k>√n/ρ`, put `ε=√n/k`. Then
  [
  (1-arepsilon/ho)^noperatorname{vol}(K)
  le k^{-n}#(kKcapmathbb Z^n)
  le(1+arepsilon/ho)^noperatorname{vol}(K).
  ]
  In particular `k^{-n}#(kK∩Z^n)=vol(K)+O_{K,n}(k^{-1})`. The same proof applies after a fixed invertible linear change of lattice, with the inradius measured in the transported norm.
- **Proof (elementary, without KK12):** Let `U_k` be the disjoint (modulo boundaries) union of half-open cubes `z/k+[0,1/k)^n` for `z∈kK∩Z^n`. Then `vol(U_k)=k^{-n}#(kK∩Z^n)`. Each such cube lies in the ε-neighborhood `K+ε B̄`. Conversely, if `x+ε B̄⊂K`, the floor-lattice corner `z/k=(⌊kx_1⌋,...,⌊kx_n⌋)/k` of the containing cube is at distance ≤ε from x and therefore belongs to K; hence x belongs to U_k. With `K_{-ε}={x:x+ε B̄⊂K}`, this gives `K_{-ε}⊂U_k⊂K+ε B̄`.
  
  Set `s=ε/ρ<1`. Convexity and the inball imply
  [
     x_0+(1-s)(K-x_0)subset K_{-arepsilon},
     qquad
     K+arepsilonoverline Bsubset x_0+(1+s)(K-x_0).
  ]
  For the first, write `x=(1-s)y+sx₀` and note `x+εB̄⊂(1-s)y+s(x₀+ρB̄)⊂K`. For the second, write any `y+v` with y∈K, |v|≤ε as `x₀+(1+s)(z-x₀)`, where `z=(y+s(x₀+v/s))/(1+s)∈K`. Volumes give the asserted sandwich. No interchange of nonmonotone limits, regularization or external counting theorem is needed.
- **Order sharpness:** For the unit cube `K=[0,1]^n`, the count is exactly `(k+1)^n`, so the normalized discrepancy is `n/k+O(k^{-2})`; an `o(k^{-1})` universal bound is false.
- **Proposed correction:** Optional quantitative corollary after the lattice clause of Theorem 19.7.20, retaining KK12 for the genuinely more general arbitrary-semigroup assertion. **Affected dependents:** numerical approximations of Okounkov bodies by lattice sections where the convex body has a fixed inball. No claim of such a rate for arbitrary almost semigroups.

## Additional actual checking, limits, and coverage

- Independently checked the algebraic polarisation `ddᶜ(u−v)∧Σ_{j=0}^{n−1}A^j B^{n−1−j}=A^n−B^n` in §14.20.1, current tag `2EA7CA32AE91` (source tag `AA4FA8E3`), `docs/sections/uniqueness-for-degenerate-equations/index.html`, blob `0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208`, lines 5–31. It uses algebra of even-degree forms and does **not** require `dω=0`; for bounded products, the displayed use remains conditional on the established Bedford–Taylor conventions. This section has only an introductory formula, not a full uniqueness proof.
- Selected passages of §13.24.6–10 and §19.7.2–7/.20 checked; earlier §19.7 findings `POME-OKO-SLICE-001` (subsequence gap), `POME-OKO-COUNT-INTERNAL-001` (KK12 replacement candidate), and toric polytope counting were located in the ledger and **not** refiled as new errors. Nothing in §13.24.1–5's approximation proof was reviewed.
- **Coverage update:** §13.24 first selected nonexcluded proof-level entry; §14.20 first selected formula-level entry; §19.7 incremental quantitative independent check, **not** a new first-review entry. All 747 current-ToC rows stay distinct; no full section, upstream non-pluripolar regularity theorem, semigroup saturation, or MA uniqueness argument is certified.
- **Status summary:** No new false Pome theorem identified. Two new conditional/quantitative deductions, with exactly stated dependencies and no extrapolation to unrestricted suprema.
- **Exclusions and operations:** Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remains **deferred-by-user**, untouched. This report proposes documentation only on `review/mathematical-audit`; no main/source/registry/permanent-tag modification, builds, tests, formal proofs, CI, or website publication.
