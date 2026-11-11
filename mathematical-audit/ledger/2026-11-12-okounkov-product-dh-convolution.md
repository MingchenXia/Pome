# 2026-11-12 — Product DH convolution ledger

- **ID:** POME-OKO-DH-PRODUCT-CONVOLUTION-001
- **Status:** verified conditional deduction (abstract Okounkov test-curve proof complete; geometric NA exterior-product realization not established)
- **Severity:** low
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Anchors:** §19.6 Definitions 19.6.1/5/7/18 (source `sgpt:26A94CBB/9E9C0297/2E276BD3/09132002`, permanent `ACD722F45231/F0D4BAA63D8A/7B20D9977149/51940EF88F4F`; integrated file blob `20ff3089e62dd1c8349e8bcc077ec64605a9788b`, lines 16–44, 90–126, 329–334); §22.1 Definition 22.1.55 (`sgpt:115B0C00` / `9ADEFD2FF381`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`, lines 902–912).
- **Precise result:** for independent product roofs in dimensions `n1,n2`, unnormalized `n!`-weighted DH measure is `binom(n1+n2,n1)` times the convolution of the separately `ni!`-weighted measures; normalizing by total masses removes this coefficient. On the square with `G(x,y)=-x-y`, total mass `2`, raw first moment `-2`, raw second moment `7/3`.
- **Error versus gap:** no original theorem refuted; geometric product compatibility and full §22.1.56 remain **not verified**.
- **Suggested correction:** optional conditional corollary spelling out the binomial normalization once product compatibility is established. Do not silently claim geometric realization.
- **Dependents:** §19.6.18, §22.1.55/56 and possible geometric product-volume/moment applications.
- **Proof:** [dated report](../reports/2026-11-12-okounkov-product-dh-convolution.md).
- **Dedup:** not the prior §19.6 heavy-tail, moment or §22.1 flag-independence findings; all statuses preserved.
- **Scope exclusion:** Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work **deferred-by-user**, neither resolved nor certified.
