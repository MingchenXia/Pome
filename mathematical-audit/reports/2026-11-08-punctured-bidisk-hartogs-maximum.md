# 2026-11-08 — punctured bidisk sharpness of closedness and holomorphic convexity

**Finding:** `POME-STEIN-PUNCTURED-BIDISK-HARTOGS-MAX-001`, **low / verified conditional deduction (sharpness example)**. Neither original printed theorem is false.

**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated reading text examined directly:
- `docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html`, blob `c04701d0358d43a3a3f1aed61e7cdd2a48305417`. Theorem 9.26.1, source `demailly-complex-geometry:57C45FF9`, permanent tag `C1041DBBD4EC`, physical lines 7–14 and 19–37; Proposition 9.26.2, source `demailly-complex-geometry:310AF940`, permanent `A1FE9ED85940`, physical lines 40–66.
- Navigation-only §9.25: `docs/sections/separation-strict-exhaustions-and-coverings/index.html`, blob `89f1c30a6df3c3df624fd05943a5cc64460824b8`, tag `D10F3B8AA2A1`, physical line 5.
- Structural crosschecks: §16.2 `docs/sections/the-envelope-operators--p-envelopes/index.html`, blob `912f81b3bccf3e1ead96fd18005261a708dfcb4e`, section tag `A6FA63C034E6`, source `sgpt:189A8E0C`, lines 5–9; §16.10 `docs/sections/envelopes-and-model-potentials/index.html`, blob `decb273ec97fcb9bb0ace2e0b90270723ecbea3e`, tag `CC5E34310EEC`, source `foundations-of-pluripotential-theory:F1167A9F`, lines 5–16. These introductory pages contain no new theorem proof certification.

## Complete elementary argument

Let `A=C^2\{0}`, an **open, nonclosed** complex submanifold of `X=C^2`. The restrictions of the coordinate functions separate all pairs of points in A. The smooth function `|z|^2+|w|^2` is nonnegative and strictly plurisubharmonic on A, but not an exhaustion there.

We show that **A has no plurisubharmonic exhaustion at all**. Choose `r,s>0` and the compact cylinder
`K={(z,w): |z|=r, |w|<=s}`, which does not intersect the deleted origin. Let u be any finite-valued smooth PSH function on A and `M=max_K u`. For fixed `0<|w|<s`, the function `z->u(z,w)` is subharmonic on the closed disk `|z|<=r` (its disk avoids the origin); the one-variable maximum principle gives `u(z,w)<=M` for `|z|<r`. For fixed `0<|z|<r`, the disk `|w|<=s` also avoids the origin, and its boundary already satisfies this bound. Hence `u(z,0)<=M` too. Thus
```
u(z,w) <= M for (z,w) in (D_r x D_s) \ {(0,0)}.
```
The same proof works for a nonidentically-minus-infinity upper-semicontinuous PSH function when `M=sup_K u` is finite; an exhaustion that is smooth/finite is sufficient for the application. If u were an exhaustion in the precise sense of §9.26.1 line 7 (strict sublevels relatively compact), for every finite c all points sufficiently close to the missing origin would satisfy `u>=c`. Otherwise a sequence approaching the origin inside `{u<c}` would contradict relative compactness in A. Therefore u would tend to `+infinity` as `(z,w)->0` within A, contradicting the uniform upper bound M. This proves the failure of **weak and strong pseudoconvexity**, even though A carries a global strict PSH function.

For **holomorphic convexity**, apply the same pair of disk maximum principles to the subharmonic function `|f|` for each `f in O(A)`. It yields
```
(D_r x D_s) \ {(0,0)} subset holomorphic_hull_A(K).
```
The hull contains `(r/(j+2),0)` for all j, a sequence without a convergent subsequence in A. Hence the hull is noncompact. This is a direct holomorphic-hull proof without assuming Hartogs extension, Hironaka, or any external Stein theorem.

The ambient X is holomorphically convex: coordinate functions show that the holomorphic hull of each compact set is bounded, and the hull is closed, hence compact. Global coordinates locally separate points, and `|z|^2+|w|^2` is a smooth strict PSH exhaustion of X. Thus **all four properties** enumerated in §9.26.2 (holomorphic convexity; holomorphic convexity with local holomorphic separation; smooth PSH exhaustion; smooth strict PSH exhaustion) fail to pass from X to an arbitrary **nonclosed** submanifold, even though the proposition correctly asserts inheritance for *closed* submanifolds.

The countermodel also demonstrates the indispensability of **holomorphic convexity** in the exhaustion conclusion of §9.26.1: local separation alone still gives the first, nonproper, strict PSH function. It does **not** contradict the separate finite-intersection clause of §9.26.2: that clause assumes each input submanifold already has the relevant property, whereas A does not.

For comparison, `C^*=C\{0}` has a smooth strictly subharmonic exhaustion `rho(z)=|z|^2+|z|^{-2}`. Its real Laplacian is `4+4|z|^{-4}>0`, and rho tends to infinity at both ends. The punctured-plane failure above genuinely begins in complex dimension two.

## Judgment, dependencies and proposed action

**Status verified conditional deduction; severity low.** This proves a sharp necessary-assumption model, not a failure of Theorem 9.26.1 or Proposition 9.26.2. Suggested exposition-only patch: state the punctured-`C^2` example after §9.26.2, retaining all source labels, attributions and permanent tags. A proposed patch must be reviewed separately; this audit changes no mathematical source or published page. Downstream uses of local separation as though it implied a *proper* strict PSH potential, or of nonclosed submanifold inheritance, must retain the missing hypothesis.

This check does not reverify the previously audited Richberg smoothing and convex-to-PSH-exhaustion dependency chains in §9.26.1; the current proof uses elementary one-variable maximum principles only. Historical attribution is retained; the source-book name is provenance, not a request to restart the explicitly excluded regularization programme. All user-excluded Demailly approximation/regularization, dedicated Bergman/L2/Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**. No other pre-existing ledger status is changed.

**Coverage:** §§9.26.1–2 selected hypothesis sharpness; §9.25 navigation only; §§16.2/16.10 direct structural intros only. There were zero newly completed mathematical sections and no new first theorem-proof visits. No tests, build, CI, browser rendering, formal verification or publication.
