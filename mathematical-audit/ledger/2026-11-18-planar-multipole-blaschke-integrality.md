# 2026-11-18 — POME-PLANAR-MULTIPOLE-BLASCHKE-INTEGRALITY-001

- **Severity/status:** low / **verified conditional deduction**. Printed Theorem 3.8.1 remains correct; no confirmed false theorem and no proof gap certified.
- **Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **integrated blob:** `bfee348bb5f4bbfaa4515e5c9333789a13dae861`; path `docs/sections/planar-green-functions-and-conformal-maps/index.html`.
- **Source anchors:** intro Green normalization line 7; Theorem 3.8.1 `klimek-pluripotential-theory:B1C110E2` / permanent `E2B11E803D94`, lines 11–13, 19–48. Proposition 3.8.2 `886FBC1A` / `3F05222ECC9E` lines 54–69 and Example 3.8.3 `02455EF4` / `FADCC209A003` lines 74–83 are context only.
- **Precise assertion:** for a bounded simply connected planar domain and distinct poles, \(\sum t_jG_D(\cdot,a_j)=-\log|B|\) for a holomorphic disc map exactly when all \(t_j\) are positive integers. Then \(B\) is a finite Blaschke product of the Riemann map, proper of degree \(\sum t_j\), unique modulo phase; every proper disc map has this form.
- **Proof/obstruction:** disc automorphism identity, integer zero orders, factorization, boundary maximum principle; \(B=z^2\) realizes a double pole whereas the exponent \(1/2\) is impossible. Distributional normalization \(-\Delta U=2\pi\sum t_j\delta_{a_j}\).
- **Disposition:** proposed optional corollary after §3.8.1, *not* a direct edit. Depends conditionally on printed Riemann map, Green uniqueness, holomorphic factorization and elementary maximum principle. No unrelated theorem or external analytic input certified.
- **Affected dependents:** only possible future finite-cover/multipole representations; none known false.
- **Actual coverage:** existing partly reviewed §3.8, +0 newly first-visited sections / +0 fully certified; remaining higher generality and upstream Dirichlet/Green theory open. Excluded programmes stay **deferred-by-user**.
- **Proof:** [report](../reports/2026-11-18-planar-green-multipole-blaschke-integrality.md); [coverage](../coverage/2026-11-18-ch3-planar-multipole-blaschke.md).
