# Bounded Bedford–Taylor truncation yields an essential support maximum, not automatically the pointwise theorem

**Finding ID:** `POME-CURRENT-SUPPORT-MAX-DIRECT-BT-001`.
**Status:** verified conditional deduction (low severity); **not** a theorem refutation and **not** a complete replacement proof of Theorem 5.63.4.
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Date:** 2026-11-07.

> **Audit correction within this run.** An initial proposed bypass of the smooth-decreasing-majorant step incorrectly treated the strict superlevel of an upper semicontinuous plurisubharmonic function as Euclidean open. Upper semicontinuity does **not** justify that. This corrected report retracts that claimed pointwise proof and retains only the rigorously proved essential-support statement below. The printed theorem has **not** been shown false or incomplete.

## Exact integrated source anchors

- `docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html`, main blob `cb4c3d4e9d653b216cff05eaf23aafb2a01425ec`; **Theorem 5.63.4**, source `demailly-complex-geometry:A8039435`, permanent tag `949B825CA873`, physical lines **82–87**; integrated proof lines **90–108**. The printed argument for nonsmooth `u` invokes a smooth decreasing majorant at line **107**. Its hypotheses and source proof have **not** been audited here.
- `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, main blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`; Definition **7.2.1**, source `foundations-of-pluripotential-theory:DE7531DE`, permanent `254CDCCCAB5E`, physical lines **16–25**; Proposition **7.2.2**, source `foundations-of-pluripotential-theory:D16BD033`, permanent `D9911E035563`, physical lines **29–54** (positive closedness and locality). Their full transitive proofs are not newly certified.
- Current ToC §5.63 permanent section tag `D5078EF0D73A`; earlier audit of §5.63 selected Proposition 5.63.2 and Lemma 5.63.3, **not** this new essential bound.

## Verified deduction: the boundary supremum controls the trace-measure essential supremum

Assume exactly the printed hypotheses: `Omega={psi<0}` is a smoothly bounded relatively compact domain in a complex manifold, `psi` is smooth strictly psh near its closure, `dpsi!=0` on its boundary, and `T` is a positive closed current of bidimension `(p,p)`, `p>=1`, near the closure. Let `u` be any psh function near the closure, without a continuity or lower-boundedness assumption. Write `omega=dd^c psi>0` and let `mu_T=T wedge omega^p`, a positive Radon measure on the closure that detects the current's support locally. Define

```text
B = sup_(boundary Omega intersect Supp T) max(u,0)
```

using the printed convention `B=0` if the boundary support is empty. (The compact upper-semicontinuity of `u` makes `B` finite.) **Claim:**

```text
mu_T({ x in Omega : u(x) > B }) = 0 .
```

Equivalently, `ess sup_(mu_T|Omega) u_+ <= B`. This statement is weaker than the printed **pointwise** support maximum, since no assertion is made about exceptional points inside the support where `mu_T` assigns zero mass.

**Proof.** Fix any `b>B` (so `b>0`) and `epsilon>0`. Define

```text
v=max(u-b+epsilon*psi,0).
```

Both entries of the maximum are psh; their maximum is psh. Since `v>=0` and any psh function is locally bounded above, `v` is locally bounded (even where `u=-infinity`). Thus the bounded Bedford–Taylor definition is applicable, giving a positive closed current `S=dd^c(vT)` of bidimension `(p-1,p-1)`.

At every boundary point of `Supp T`, `u<=B<b`. Upper semicontinuity of `u` and continuity of `psi` give a neighborhood on which `v=0`; at boundary points outside `Supp T`, `T=0` locally. Compactness of the boundary therefore implies that `vT` has compact support **strictly inside** `Omega`. Multiplication by `v` is well-defined because `v` is locally bounded. Choose a smooth cutoff equal to 1 on a neighborhood of this compact support.

The smooth closed form `omega`, compact-support Stokes and positivity yield

```text
0 = integral_Omega dd^c(vT) wedge omega^(p-1)
  = integral_Omega S wedge omega^(p-1).
```

Since `S` is positive and `omega` strictly positive, its trace measure vanishes and hence `S=0` on `Omega`. Testing this equality against `psi*omega^(p-1)`, with a cutoff equal to 1 near `Supp(vT)`, and using `dd^c(psi*omega^(p-1))=omega^p`, gives

```text
0 = integral_Omega v T wedge omega^p = integral_Omega v d(mu_T).
```

As `v>=0`, the set `{u-b+epsilon*psi>0}` has `mu_T`-measure zero. Since `psi<0` on `Omega`, for every point there with `u>b` the inequality `u-b+epsilon*psi>0` holds for all sufficiently small `epsilon>0`. Consequently

```text
{u>b} intersect Omega
= union_(j>=1) {u-b+psi/j>0} intersect Omega,
```

and this set has `mu_T`-measure zero by countable subadditivity. Let `b` decrease through a countable sequence to `B`; the claim follows. The entire argument uses only the bounded BT product for `v`, positivity of closed currents, and compact-support Stokes. **No smoothing, Bergman, L2, OT, multiscale or positivity-loss construction occurs.** `QED`

## Why this does not finish the printed pointwise theorem

The strict superlevel `{u-b+epsilon*psi>0}` of an upper semicontinuous psh function is **not in general Euclidean open**. Thus ordinary Euclidean-open locality of the BT product (Proposition 7.2.2(2)) cannot be applied on that set without an additional fine-locality argument, and even vanishing trace measure there does not alone prove that this set misses every point of `Supp T`. One must justify the **pointwise** promotion separately; for example, the printed proof invokes a smooth-decreasing-majorant result at its line 107. That original dependency has **not** been resolved or certified by this audit, and no claim about its validity is made.

In particular, `POME-CURRENT-SUPPORT-MAX-DIRECT-BT-001` records a verified conditional deduction and the exact limitation of an attempted stronger proof, **not** a verified repair, complete theorem proof, or evidence that the printed theorem is false. The original printed Theorem 5.63.4 remains unrefuted.

## Sharpness and dependents

The actual assumptions matter even for the weaker statement. With `p=0`, take a positive Dirac point mass current `T=delta_0` in the unit disk and `u=1`: its interior essential supremum is 1 and its boundary support is empty. Without closedness, let `p=1` and `T=rho` be any nonzero nonnegative smooth bump function supported in the disk, `u=1`; the same contradiction occurs. These violate the **printed hypotheses**, not the theorem.

**Affected dependents:** any use of the printed Theorem 5.63.4 in a pointwise support argument must retain the printed smooth-decreasing-majorant input or an independently justified replacement. The essential bound above can be used with trace-measure integrals, not substituted for pointwise support maximum. **Proposed correction to the proof route:** do not replace the general-psh step by Euclidean locality on a strict superlevel; either retain the original justification or prove the missing pointwise upgrade with valid additional input. **No production patch** is made.

**Coverage:** new selected audit of §5.63.4 and the exact §7.2.1–2 premises; no new first-visited ToC section, no whole section certification. Baseline **25 chapters / 747 numbered sections / 0 fully mathematically certified sections**. All user-excluded Demailly approximation/regularization and dedicated Bergman, weighted-L2, OT, multiscale and positivity-loss programmes remain **deferred-by-user**. No tests, builds, CI, formal verification or website publication.
