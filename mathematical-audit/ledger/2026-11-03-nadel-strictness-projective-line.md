# Classified increment — 2026-11-03 — strictness of positivity in singular-metric vanishing

| Finding ID | Severity | Status | Exact evidence | Proposed action | Dependent scope |
| --- | --- | --- | --- | --- | --- |
| `POME-NADEL-STRICT-POLE-JUMP-001` | low | **verified conditional deduction** (not a false theorem or proof repair) | main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/strictly-positive-singular-metrics/index.html`, blob `0816e58d94c6cdd7dd6ee5d1de369ffcdf473b43`, §10.102.1, source `cao-paun-foliations:274E8A7B`, tag `4F4355678C85`, physical lines 8–13 and 27–33. (h_a=h_{FS}^d\exp[-a\log|s_p|^2]), (0\le a\le d), has curvature ((d-a)\omega+a[p]), ideal (mathcal O(-\lfloor a\rfloor p)), and exact (h^1=\max(\lfloor a\rfloor-d+1,0)): zero for (a<d), one for (a=d). | Optionally document the endpoint example; **retain** strict (delta>0). Verify any downstream invocation that drops strictness. | §10.102.1 hypothesis boundary only; no downstream misuse established. |

[Full mathematical argument, source labels and conditional boundaries](../reports/2026-11-03-singular-positive-metric-threshold-on-projective-line.md).

**Resolved/unresolved/deferred discipline.** This is an independent verified model, not certification of the original proof. Existing confirmed errors, unresolved gaps, external inputs and resolved repairs are not changed. In particular, strong openness and singular/complete L² input have **not** been re-proved. Every user-excluded Demailly approximation/regularization and dedicated Bergman/weighted-L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion item stays **deferred-by-user**. First selected §10.102 review only; **25 chapters / 747 sections / 0 fully certified sections**.
