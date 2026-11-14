# POME-LG-ETALE-TRANSFER-DUAL-CONE-001

- **Date:** 2026-11-14.
- **Status:** verified conditional deduction; **severity:** low.
- **Printed theorem false?** No. This is an independent finite étale transfer statement, not covered by the bimeromorphic theorem and not a claim of a proof flaw.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **integrated blob:** `6ebf8e604b45d3eb748037af506145273ca3875d`; path: `docs/sections/locally-conformally-kahler-geometry/index.html`.
- **Anchors:** §§23.2.55–60 and 23.2.61–66; Definition 23.2.57 `non-kahler-pluripotential-theory:19904244 / FC269BC81E64`; Theorem 23.2.60 `non-kahler-pluripotential-theory:B41AA0AF / DB27896B9A96`; Theorem 23.2.64 `non-kahler-pluripotential-theory:CDA139E7 / 403FA017D33B`; see [complete proof](../reports/2026-11-14-finite-etale-lee-gauduchon-transfer.md) for physical lines and other tags.
- **Hypotheses:** connected compact complex manifolds, dimension n>=2, finite **étale** map of degree d>0.
- **Claim:** `p_*LG(Y)=LG(X)`; `p^*C_X=C_Y cap p^*H^1(X)` and likewise for K; the zero-class condition and balanced-metric existence are finite-étale invariant.
- **Proof:** finite smooth trace of positive dd^c-closed (n-1)-powers; unique Hermitian root; current trace and projection formula in Bott–Chern; pullback/trace for balanced powers.
- **Limitations:** finite ramified maps are not covered; no surjectivity of p^* on H^1; no assertion that 0 in LG characterizes balanced metrics.
- **Affected existing results:** §§23.2.59–60/64/66 only as an **optional corollary**; no production edit. Upstream Hermitian root remains a named internal dependency; not a whole-project or whole-section certificate.
- **Deferred-by-user:** all dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss work stays deferred, not resolved or certified.
