# Direct bounded Bedford–Taylor proof of the positive-current support maximum

**Finding ID:** `POME-CURRENT-SUPPORT-MAX-DIRECT-BT-001`. **Classification:** low / verified repair of a proof route (not a false theorem; full transitive internal Bedford–Taylor foundations are not certified). **Date:** 2026-11-07. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Reading-edition anchors and prior scope

- `docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html`, main blob `cb4c3d4e9d653b216cff05eaf23aafb2a01425ec`: **Theorem 5.63.4**, source `demailly-complex-geometry:A8039435`, permanent tag `949B825CA873`, exact physical lines **82–87**; proof lines **90–108**, particularly the bounded-product argument at **93–105** and the smooth-decreasing-majorant invocation at **107**. The statement is **correct**. The alternative below replaces only the passage from smooth to arbitrary psh without revisiting or relying on the dedicated excluded regularization programme.
- `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, main blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`: **Definition 7.2.1**, source `foundations-of-pluripotential-theory:DE7531DE`, permanent `254CDCCCAB5E`, lines **16–25**; **Proposition 7.2.2**, source `foundations-of-pluripotential-theory:D16BD033`, permanent `D9911E035563`, lines **29–54**, including positive closedness and locality. These are **identified internal inputs**, not independently certified in their full proof chain.
- Current table-of-contents section tag `D5078EF0D73A` (§5.63). The audit matrix already recorded selected checks of Proposition 5.63.2 / Lemma 5.63.3; this is **new direct coverage of Theorem 5.63.4**, not a first section visit.

## Proof: no smoothing of the original psh function is needed

Let `Omega={psi<0}` be relatively compact with smooth strictly psh `psi` near its closure, `psi=0` on the boundary, and put `omega=dd^c psi>0`. Let `T` be a positive closed current of **bidimension (p,p)**, with `p>=1`, on a neighborhood of the closure. Let `u` be an **arbitrary** psh function there, possibly discontinuous or identically `-infinity` on some subsets.

Define `B=sup_(boundary Omega intersect Supp T) max(u,0)`, with the specified empty-set convention `B=0`. Fix any real `b>B` (hence `b>0`) and any `epsilon>0`. Put

```text
v = max(u - b + epsilon*psi, 0).
```

**Key elementary observation:** `v` is *locally bounded psh*, even if `u` is unbounded below. Both arguments of the maximum are psh; the maximum is psh; `v>=0`; and upper semicontinuity of `u` gives a finite upper bound on each compact set. This is a pointwise local boundedness claim, not a smoothing or limiting statement.

At each point of `boundary Omega intersect Supp T`, `u<=B<b`; by upper semicontinuity and continuity of `psi`, the strict inequality `u-b+epsilon*psi<0` holds in a neighborhood. Hence `v=0` on a neighborhood of that compact boundary-support intersection. At any other boundary point the current `T` vanishes locally. Compactness of the boundary gives that `vT` is supported in a compact subset of `Omega`.

By the bounded Bedford–Taylor product (Definition 7.2.1 and Proposition 7.2.2),

```text
S := dd^c(v T)
```

is a **positive closed** current of bidimension `(p-1,p-1)`. Since `omega` is smooth and closed, compact-support Stokes implies

```text
integral_Omega S wedge omega^(p-1) = 0.
```

Its integrand is a positive measure, so the measure `S wedge omega^(p-1)` vanishes identically on `Omega`.

On the open set `E={u-b+epsilon*psi>0} intersect Omega`, the function `u` is locally bounded **below** by `b-epsilon*psi` and locally bounded above by psh upper semicontinuity. Therefore `u` is locally bounded on `E`, and locality plus additivity of the bounded BT product give

```text
S|_E = dd^c(u T)|_E + epsilon * omega wedge T|_E
     >= epsilon * omega wedge T|_E.
```

Wedge with `omega^(p-1)` and use positivity to conclude that `(T wedge omega^p)|_E=0`. Because `omega` is **strictly positive**, its trace measure `T wedge omega^p` has exactly the same support as the positive current `T`. Consequently `E intersect Supp T` is empty.

It follows that `u<=b-epsilon*psi` throughout `Omega intersect Supp T`. Let `epsilon` decrease to zero and then let `b` decrease to `B`: we obtain `u<=B` on `Omega intersect Supp T`. On the boundary the same inequality holds by definition of `B`; since `B>=0`, `u_+<=B` everywhere on `closure Omega intersect Supp T`. The reverse inequality for suprema is immediate from boundary inclusion. This proves **exactly** the displayed identity in Theorem 5.63.4, including the case of empty boundary support and the case of psh functions with poles. No smooth-decreasing majorant is invoked, constructed, or checked.

## Sharpness of the actual hypotheses

1. **Bidimension p>=1 is essential:** on the unit disk take `T=delta_0` of bidimension `(0,0)`, which is a positive closed top-degree current, and `u=1`. The interior-support supremum is 1, whereas the boundary-support supremum is 0.
2. **Closedness is essential:** on the unit disk take `p=1`, `T=rho` for a nonzero nonnegative smooth bump `rho` supported strictly inside the disk. This is a positive `(0,0)` current but is not closed unless `rho` is constant. For `u=1` the two suprema are again 1 and 0.
3. Strict positivity of `omega` is used exactly at the implication `T wedge omega^p=0` on an open set `=>` that set misses `Supp T`. Mere semipositivity does not justify that implication.

These examples are **not counterexamples to the printed theorem**: they violate the respective hypotheses.

## Decision / dependencies

**Verified repair of an unnecessary dependency in the proof route, not a theorem correction.** The printed theorem and its existing proof remain mathematically unrefuted. The sole proposed change, if independently reviewed later, is to replace the proof's general-psh approximation paragraph at physical line 107 by the direct bounded-truncation argument above. No production file, source, permanent tag or registry is changed in this audit.

**Internal dependencies:** established BT positive-product and locality statements (7.2.1–2), compact-support Stokes, and the elementary fact that `T wedge omega^p` detects the support of a positive `(p,p)`-bidimension current when `omega` is strictly positive. Their entire transitive proofs were not re-audited. **Excluded:** all Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion work stays **deferred-by-user**; the preexisting approximation notes are not upgraded to resolved/certified.

**Coverage:** selected Theorem 5.63.4, its stated hypotheses and proof lines 82–108, plus directly used BT 7.2.1–2 only; **0 new first-visited sections / 0 completely certified sections**. Current project ToC baseline: **25 chapters / 747 numbered sections / 0 fully certified sections**. No tests/build/CI/formalization/publication were performed.
