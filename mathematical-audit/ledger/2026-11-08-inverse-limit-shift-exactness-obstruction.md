# 2026-11-08 classified finding — inverse-limit exactness obstruction

| Stable ID | Classification | Severity | Truth status and exact scope | Proposed action |
| --- | --- | --- | --- | --- |
| `POME-INV-LIM-DENSE-DEGREE-NONEXACT-001` | **verified conditional deduction** | **low** | An explicit countable two-term complex of complex Banach spaces has **dense bonding maps in both degrees** and vanishing stagewise `H^1`, yet nonzero `H^1` in the inverse limit. Theorem 2.14.4's **conditional injectivity**, Theorem 2.14.6(3) and Proposition 2.14.7 remain **correct as printed**; removing their separate preceding-cohomology/kernel-density assumptions is false. | Optionally add the Hilbert right-shift example after Proposition 2.14.7, without changing statements or permanent tags. |

**Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated file:** `docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html`, blob `30e6e5800601450ce52d9c01dc5abea06a403d6e`. Source/permanent labels, physical line anchors, full construction, and independent density and nonsurjectivity proofs: [report](../reports/2026-11-08-inverse-limit-shift-exactness-obstruction.md).

**Impacted dependents:** precisely the hypotheses in §§2.14.4, 2.14.6(3), and 2.14.7. No established downstream theorem is reclassified; no false original theorem, proof gap, or genuine duplication is claimed. Earlier errors and missing dependencies are **unchanged**. User-excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved or certified. No production, CI, build or site change.
