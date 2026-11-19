# Precise coverage: 2026-11-20 §3.9

**Baseline:** current production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated file:** `docs/sections/planar-boundary-distance-and-convexity/index.html`; Git blob `25fd0fd57d3e51f9224a25341ace77584b2a1a2a`; lines **7–107**. **Whole directly reviewed:** yes, all three propositions and every argument, excluding page metadata. **Prior status:** previously selected partial reads; no first-ever visit claim.

| Location and stable labels | Actually examined | Classification |
| --- | --- | --- |
| §3.9.1, `klimek-pluripotential-theory:79D31B13 / 964B6728E795`, lines 7–33 | Polygonal triangle, supporting-point separation, supermean contradiction; concavity of convex-domain boundary distance | Direct full printed proof review; no new confirmed error |
| §3.9.2, `klimek-pluripotential-theory:219D9DEC / 59D258340230`, lines 37–87 | Distributional semiconcavity, eikonal Hessian, real-dimension-two argument, local convexity, continuous retraction, **unlinked local-to-global lemma at line 78** | Direct full printed proof review; self-contained audit-only verified repair `POME-PLANAR-DISTANCE-LOCAL-CONVEX-GEODESIC-001` |
| §3.9.3, `klimek-pluripotential-theory:366D2F88 / BBEB233BF8A4`, lines 91–107 | Connected collar plus interior argument; two-disk disconnected-collar counterexample | Direct full printed proof review, dependent on §3.9.2 |
| Independent proof | Closed connected locally convex ⇒ convex by minimal-length polygonal geodesic and straightening; firm nonexpansivity and C^{1,1} squared distance | Complete independent algebraic/geometric proof in [report](../reports/2026-11-20-planar-distance-local-convexity-and-firm-projection.md) |

**Deltas:** +1 complete direct reading (not historical first visit), +0 complete transitive proof-chain certificates, +0 original printed false theorem, +1 audit-only self-contained proof repair, +1 conditional derivative/projection deduction. Sources and prior partial reports preserved. No build, tests, CI, publishing, tag, registry or main updates. The user-excluded Demailly/Bergman/L²/OT/multiscale/positivity-loss programmes stay **deferred-by-user**, not certified.
