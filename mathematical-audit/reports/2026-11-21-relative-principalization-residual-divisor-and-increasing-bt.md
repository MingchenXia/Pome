# 2026-11-21: increasing Bedford–Taylor convergence and a nonexceptional principalization residual

**Current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`. The audit applies to the current integrated reading edition, not original source repositories. The user-excluded Demailly approximation/regularization programme and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof work were not examined.

## Precise scope and locators

- **Entire mathematical §7.6**, `docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html`, blob `5e763bdc928794938c37dc3c7a51cc406472d076`, physical mathematical lines **7–80** (file 91 lines). Section permanent tag `E5550B44EC7B`; Theorem 7.6.1 source `foundations-of-pluripotential-theory:36787F42`, permanent `A4C45B704647`, theorem/proof lines **11–59**; Corollary 7.6.2 source `foundations-of-pluripotential-theory:2ACED3F4`, permanent `D865A8538D7D`, lines **63–80**.
- **Selected §9.7.5 theorem and its entire proof, not the whole §9.7:** `docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html`, blob `b44fe157b8c01363da7799990b8ef6ed82525553`, Theorem 9.7.5 source `foundations-of-pluripotential-theory:1524D010`, permanent `689628C7AF7F`, statement **89–97**, proof **100–127**, offending Step 3 line **120**. This section also contains Remmert–Stein/Remmert and other results **not** read end-to-end this run.
- **Selected input**, principalization Theorem 9.6.7 and its accumulated-divisor explanation: `docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html`, blob `f452f4b1abe5cdfe348ae11fcd934febcfdd570b`, lines **91–107**, source `foundations-of-pluripotential-theory:B74A86AD`, permanent `24330D25741D`. The source convention in Definition 9.6.1 (permanent `757D038DF549`) was also consulted, not the entire section.

## Finding POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001

**Severity: low. Status: confirmed error in a proof sentence; not a false theorem.** Theorem 9.7.5 only demands that (H) be exceptional for (f) and that (H') be disjoint from (W'). These requirements are consistent and the printed construction establishes them. However, in the proof's Step 3 (physical line 120), immediately after the principalization of the residual ideal (mathfrak a_t), the text additionally asserts that **(H') is supported on the exceptional divisors of (g)**. This extra assertion is false when (mathfrak a_t) already contains divisorial zero components away from (W_t); principalization does not make the strict transforms of those components exceptional.

**Explicit counterexample satisfying all theorem hypotheses.** Let (M=mathbb P^2), let (W={p}) be a point, choose a projective line (Lsubsetmathbb P^2) with (p
otin L), and put
[
mathfrak a=mathcal I_L=mathcal O_M(-L).
]
The restriction (mathfrak amathcal O_W=mathcal O_W) is nonzero. Since (W) has dimension zero, Step 1 has no centers, so (t=0), (M_t=M), (W_t=W), (H_t=0), and (mathfrak a_t=mathcal I_L). Blowup of the Cartier divisor (L) is canonically isomorphic to (M) (locally the blowup of a principal nonzerodivisor has its graph in (mathbb P^0), hence is the identity); this one legitimate marked-ideal principalization step gives unit transform and residual (H'=L). Its composite (g) is an isomorphism, so (g) contracts no divisor, whereas (H'
eq0). More invariantly, **every** permitted principalization must retain a divisor mapping dominantly onto (L) with multiplicity one, because (mathcal I_Lmathcal O_{M'}=mathcal O_{M'}(-H')) and the generic point of (L) cannot disappear under a bimeromorphic modification. Such a divisor is not exceptional for (g).

For the identity realization (M'=M), (f=g=mathrm{id}), (H=0), (H'=L), all three asserted identities (9.7.6)–(9.7.8) hold:
[
mathcal I_W=mathcal O_M(-H)mathcal I_{W'},quad
mathfrak a=mathcal O_M(-H-H'),quad
(mathfrak amathcal O_W)mathcal O_{W'}=mathcal O_{W'}(-H|_{W'}),
]
and (H'cap W'=arnothing). The **theorem remains true**; only the surplus assertion about (H') being (g)-exceptional is refuted. Notice that calling (E_i) a "blowup exceptional factor" in the marked-ideal transformation (9.6.8) does not mean that its image has codimension at least two: a blowup along a smooth Cartier divisor is the identity.

**Verified local repair (not a completed upstream certification).** Replace the false sentence by:
> The divisor (H') is supported on (g^{-1}(V(mathfrak a_t))), which is disjoint from (W'=g^{-1}(W_t)) because (mathfrak a_t) is the unit ideal near (W_t).

Indeed, (V(mathfrak a_tmathcal O_{M'})=g^{-1}V(mathfrak a_t)), and (mathfrak a_tmathcal O_{M'}=mathcal O_{M'}(-H')) implies
(operatorname{Supp}H'=V(mathfrak a_tmathcal O_{M'})).
This proves precisely the disjointness used later, without the unsupported exceptionalness. Step 4 independently proves that **(H)** is (f)-exceptional by mapping its components into codimension-at-least-two centers lying in (W). Thus deleting the extra assertion leaves the printed proof strategy intact, conditional on the Hironaka principalization input.

**Affected dependents / proposed action:** Theorem 9.7.5's Step 3 explanation; any future argument that tries to treat (H') as exceptional must use the weaker disjointness statement instead. No such downstream misuse was independently established by this focused check. Proposed *reviewable source patch* only; no change to the theorem's conditions, original provenance or permanent tags. Do not globally canonicalize (H) and (H') or identify their distinct geometric roles.

## Full §7.6 mathematical audit, with no additional confirmed printed error

1. **Monotone local bounds and induction (lines 11–25).** Almost-everywhere convergence of increasing psh functions to a locally bounded psh (u_l) yields (u_{l,j}le u_l) pointwise by uniqueness of psh representatives. This provides common compact bounds. The (q=0) weighted assertion follows from dominated convergence; applying (dd^c) to the weighted (q-1)-factor convergence produces unweighted (q)-factor convergence. It does not assume that monotone psh convergence is pointwise at the exceptional pluripolar set.
2. **Collar and weak-current comparison (approximately lines 26–49).** The maximum with the quadratic collar barrier has the claimed locality and provides fixed near-boundary currents. With (S_j	o S), relative positivity ((u_0-u_{0,j})S_jge0) produces the weak-limit **upper** bound (Thetale u_0S). The sign is correct despite the negative normalization. CLN bounds give weak precompactness, and the collar turns local weak convergence into convergence of the full displayed integrals on (B).
3. **Mass equality via fixed quasi-continuous weights (lines 40–54).** The monotonicity (u_{0,j}ge u_{0,k}), weighted continuity with the fixed (u_{0,k}), the bounded-current integration-by-parts identity, and the already established unweighted convergence yield (int_BThetawedgeeta^{n-q}geint_B u_0Swedgeeta^{n-q}). The positive compactly supported current (u_0S-Theta) therefore has zero trace mass and vanishes. The subsequence contradiction then legitimately yields convergence of the whole sequence.
4. **Capacity and exceptional envelope (lines 55–80).** The local capacity estimate with (q=n) bounds (operatorname{Cap}_D{u_l-u_{l,j}>delta}) by a difference of weighted integrals, both of which converge by previously proved assertions and fixed-weight quasi-continuity. Corollary 7.6.2 uses a **countable** subfamily, then countable unions of the capacity-zero strict gaps after truncating at (-m); it does not require the unregularized pointwise supremum to be measurable. The given example (max{j^{-1}log|z_1|,-1}) correctly exhibits a nonempty polar exceptional gap.

**Certification limit:** These checks validate the internal logic **conditional on** the displayed referenced theorems, including the weighted quasi-continuous integration lemma 7.5.7, the CLN bound 7.2.5, the local capacity bound 7.4.6, and the psh envelope/representative results 5.9.1 and 5.10.2. This session did not independently reconstruct their complete proofs. The Hironaka principalization of 9.6.7 remains an explicitly permitted **external dependency**, not audited or supplied with an invented proof.

## Resolution / unresolved / deferred

- **Confirmed proof-only error (open, suggested repair verified locally):** `POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001`. The printed theorem is not false.
- **No additional confirmed error:** §7.6 entire section, including 7.6.1 and 7.6.2. No new external theorem imported into that section.
- **Unresolved upstream certification:** §7.6 references listed above; full 9.7.1–9.7.4 and all downstream 9.7/9.8 uses beyond the selected 9.7.5 proof; principalization remains Hironaka external input.
- **Deferred-by-user (unchanged, not certified):** Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work.
- **Actual new scope:** +1 whole direct mathematical section (§7.6), +1 selected theorem/proof (§9.7.5), +1 selected reference statement/explanation (§9.6.7), +0 certified transitive chains; no assertion that either section was never previously visited.
- **Execution:** direct source-based mathematical reading only; no tests, builds, GitHub Actions, publication, tags, registry, source, or main modifications.
