# Classified finding — POME-PLANAR-ISOLATED-POLAR-BOUNDARY-EXCEPTION-001

- **Date / main:** 2026-11-06 / `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Status / severity:** **verified conditional deduction / low**. This is an independent extremal sharpness example, **not** a false printed theorem, proof-gap certification, or mathematical repair.
- **Primary target:** `docs/sections/planar-green-functions-and-conformal-maps/index.html`, main blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`, Proposition 3.8.2, lines 53–69; `klimek-pluripotential-theory:886FBC1A` / permanent `3F05222ECC9E`.
- **Crosschecks:** Example 3.8.3, same blob, lines 73–83, `klimek-pluripotential-theory:02455EF4` / `FADCC209A003`. Theorem 16.30.5, `docs/sections/polynomial-descriptions-of-logarithmic-envelopes/index.html` blob `15d7e0207da1d72653382a1512ca380311b5d5e3`, lines 93–115; `klimek-pluripotential-theory:485FC789` / `E171A0405847`.
- **Hypotheses:** compact nonpolar `K=S^1∪{R}` with real `R>1`, exterior component `Omega={|z|>1}\setminus{R}`, logarithmic-growth subharmonic envelope.
- **Exact result:** `V_K=log⁺|z|` outside `R`, but `V_K(R)=0`; `V_K^*=log⁺|z|` everywhere. The **canonical bounded-near-boundary** harmonic extremal has positive boundary limit `log R` at the polar point `R` and zero on `S^1`. The exceptional set in Proposition 3.8.2 cannot be dropped. `ddᶜV_K^*=(4π)⁻¹ ds_{S¹}`.
- **Justification:** annular subharmonic maximum principle upper bound, admissible polynomials `z^m(z-R)/(R+1)` lower bound, direct radial flux. [Full report](../reports/2026-11-06-isolated-polar-outlier-planar-extremal.md).
- **Correction / affected dependents:** no statement correction; optional explanatory example. Only uses that would strengthen §3.8.2's q.e. boundary condition to everywhere are cautioned; no theorem invalidity shown.
- **Unresolved / deferred:** general boundary minimum principle, Myrberg and general Siciak theorem not certified; all prior findings retained. The excluded regularization and dedicated Bergman/weighted-L²/OT/multiscale/positivity-loss work stays `deferred-by-user`.
