# 2026-11-06 — exact disc Green energies and sweeping

**ID:** `POME-GREEN-DISC-CIRCLE-ENERGY-PROJECTION-001`; **status:** verified conditional deduction; **severity:** low; **printed theorem:** none refuted.

**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Reviewed reading-edition:** `docs/sections/green-energy-and-martin-boundaries/index.html` (blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`), §4.5.1 lines 5–13, Theorem 4.5.2 lines 16–29 (source/permanent `classical-potential-theory:AEA69819 / CC3D1AD9179B`), Theorem 4.5.4 lines 46–65 (`:5FB19CB2 / CE0D5F4DF7B2`), Theorem 4.5.6 lines 76–86 (`:9D70EB64 / B15EFD960FD5`). Crosschecked §3.8.1 `klimek-pluripotential-theory:B1C110E2 / E2B11E803D94`, blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`, lines 10–15.

**Finding:** The exact disc circle Green kernel yields \(I(\mu_r,\mu_s)=\min\{\log(1/r),\log(1/s)\}\). For \(0<R<r<1\), the unrestricted positive energy projection onto measures supported on \(K=\overline D_R\) is \(\nu=(a/b)\mu_R\), with \(a=\log(1/r)\), \(b=\log(1/R)\), mass \(a/b\), residual squared norm \(a-a^2/b\), and Green capacity \(C_D(K)=1/b\). Strong energy convergence may have fixed total-variation distance \(2\), and mass one may escape through the boundary while energy tends to zero.

**Dependents/correction:** No mathematical statement correction. The model supports the conventions and logical boundaries of Theorems 4.5.2, 4.5.4, 4.5.6. Optional English example alongside §4.5.6 only, not a production change. Exact kernel computations are direct; the *unrestricted* nearest-point identity uses the internal positive-definite energy result; the general theorem is not independently certified.

**Still unresolved:** general finite-energy cone completeness, global Green potential domination and Martin boundary remain unreviewed or only context-read. All earlier error/gap/candidate/external/deferred categories stay unchanged. Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss remain **deferred-by-user**, neither resolved nor reopened.

[Proof](../reports/2026-11-06-disc-circle-green-energy-balancing-projection.md) · [coverage](../coverage/2026-11-06-ch4-disc-circle-energy-balayage.md).
