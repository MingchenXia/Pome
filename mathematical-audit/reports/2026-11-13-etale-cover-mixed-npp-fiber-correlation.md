# An étale cover with identical averaged currents but different averaged mixed products

**Date:** 2026-11-13. **Finding ID:** `POME-NPP-ETALE-FIBER-CORRELATION-001`. **Severity:** low. **Status:** **verified conditional deduction** (sharp limitation on a *proposed* non-birational generalization); **not** a false printed proposition, **not** a repair or whole-theorem certification.

**Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated file:** `docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html` (blob `9954a43d90d5cae8ef744968636d7a5912348fce`). **Anchor:** Proposition **13.6.3**, source `foundations-of-pluripotential-theory:3F4A3A88`, permanent `0811FFDF15B7`, statement at physical lines **35–44** and proof at **49–54**. Section §13.6 is **previously partially sampled**; the separately published 2026-11-03 `POME-NPP-FINITE-DEGREE-PUSH-SECOND-FAIL-001` is retained, not re-registered.

## What the printed proposition says

For a proper **bimeromorphic modification** `π: X̃ → X` between compact Kähler manifolds and closed positive (1,1)-currents, Proposition 13.6.3 has the pullback/pushforward non-pluripolar-product identities. Its argument uses the **single** biholomorphic sheet over the complement of an analytic set and the zero mass of non-pluripolar products on pluripolar exceptional sets. There is no error in the printed, bimeromorphic scope.

The prior 2026-11-03 report established the generic degree factor in the *first* identity and refuted the unnormalized *second* identity for finite covers using total masses (on a branched self-map of projective space). The issue considered here is stronger and mathematically different: **even after division by the covering degree**, all individual pushforward currents and *total top-degree mass* can agree while their averaged mixed-product **measures differ locally**. It occurs for a smooth **unramified** cover, so branching and pole sets play no role.

## Explicit degree-two étale model

Let `E = ℂ/(ℤ+iℤ)`, with complex coordinates `z=x+iy`, `w=s+it` on `Y=E×E`. The fixed-point-free holomorphic involution
[
	au(z,w)=(z+	frac12,w)
]
defines an étale quotient `X=Y/⟨τ⟩` and a degree-two holomorphic covering `π:Y→X`. The standard translation-invariant Kähler form
[
Omega_Y=rac{i}{2}(dzwedge dar z+dwwedge dar w)
]
descends to a Kähler form `Ω` on `X`, so `π^*Ω=Ω_Y`.

Define a smooth real function on `Y` by
[
f(z,w)=cos(2pi x)cos(2pi s),qquad
H=dd^cf,quad dd^c=rac{i}{2pi}partialarpartial.
]
Since `f∘τ=-f`, we have `τ^*H=-H`. For every sufficiently small `ε>0`, the two smooth closed real forms
[
R_+=Omega_Y+arepsilon H,qquad
R_-=Omega_Y-arepsilon H
]
are **strictly positive**: the eigenvalues of `H` relative to `Ω_Y` are uniformly bounded on the compact manifold, so choose `ε` below the reciprocal of the bound. Thus all non-pluripolar products below coincide with the ordinary smooth wedge products; no truncation or regularization is involved.

As a current, the pushforward satisfies `π_*Ω_Y=2Ω`. For every test form `ξ` on `X`, the deck transformation gives `π_*H=π_*(τ^*H)=-π_*H`, hence `π_*H=0`. Consequently
[
oxed{rac12pi_*R_+=rac12pi_*R_-=Omega.}	ag{1}
]
Yet `τ^*(Hwedge H)=Hwedge H`, so there is a unique smooth real `(2,2)`-form `β` on `X` with `π^*β=H^2`, and `π_*H^2=2β`. Therefore
[
oxed{rac12pi_*langle R_+wedge R_-angle
=Omega^2-arepsilon^2eta

e Omega^2
=leftlangle	frac12pi_*R_+wedge	frac12pi_*R_-ightangle.}	ag{2}
]

Here the inequality is **proved**, not inferred from degree counting. At `(z,w)=(0,0)`, the two diagonal entries of the complex Hessian of `f` are both `-π²` and the mixed entries vanish, giving
[
H(0,0)=-piOmega_Y(0,0),qquad
H^2(0,0)=pi^2Omega_Y^2(0,0)
e0.
]
Thus `β` is a nonzero smooth top-degree form, positive at the image of the origin. In fact `∫_Xβ=(1/2)∫_Y(dd^cf)^2=0` by Stokes and `dH=0`. Hence the two measures in (2) **have the same total mass**, although they are not equal (and `β` necessarily changes sign). This distinguishes the new example from the prior unequal-total-mass test.

## Interpretation, dependency and correction boundary

The pushforward operation averages over the two sheets. Wedge products do not commute with this averaging: `(π_*R_+ /2)wedge(π_*R_-/2)` includes cross-sheet correlations, whereas `π_*(R_+wedge R_-)/2` averages the *same-sheet* products. Degree normalization alone cannot repair the non-birational second identity. One sufficient special case is `R_j=π^*T_j`, when the first identity, with degree two, implies the **averaged** product equality; this special case is not a statement about arbitrary `R_j`.

**Suggested editorial scope note (proposed only):** retain “modification” in Proposition 13.6.3 and state that a generically finite replacement is not valid for arbitrary upstairs currents, **even after normalizing pushforward by generic degree** and even when all upstairs forms are smooth, positive, closed and the map is étale. Do not alter theorem, source, canonical registry or permanent tags.

**Affected dependents:** any extension of §13.6.3 to generically finite maps; any finite-cover comparison of relative Monge–Ampère energies or mixed products that substitutes a wedge of separately averaged currents for the averaged wedge; any proposed canonicalization identifying these operations. This does not invalidate the existing birational or pulled-back-current statements.

**Inputs/limits:** elementary smooth Kähler calculus, degree-two covering pushforward and Stokes; the equality of smooth and non-pluripolar products follows from their local truncation definition (§13.2). The full Bedford–Taylor analytic chain, Theorem 13.5.4, and all remaining §13.6 statements are **not** transitively certified. Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remain **deferred-by-user**, untouched. No tests, build, CI, site publication or formal verification were performed.

**Coverage:** exact new proof-level §13.6.3 comparison plus contextual §13.2 smooth-product definition; **+0 newly first-visited numbered sections, +0 completely certified sections**; present ToC **25 chapters / 747 numbered sections**.
