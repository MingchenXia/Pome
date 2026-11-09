# Finding POME-ENVELOPE-MOVING-ENDPOINT-LIPSCHITZ-001

- **Status:** verified conditional deduction. **Severity:** low.
- **Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Source / tag:** `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--a-minimum-with-a-varying-upper-radius/index.html` (blob `879fd87eacb65755ae0e7a9ffc95e71d1c262d39`); `foundations-of-pluripotential-theory:1E3A3A35` / permanent `93E8FFBE7FEB`; Lemma 16.18.1 physical lines 10–55.
- **Exact hypothesis and claim:** Under (H_s\ge0), (H_{ss}>0), bounded-below-at-(-\infty) and (c>0), the infimum (V_H(b)=\inf_{s\le b}(H(s)-cs)) satisfies (0\le V_H(b_1)-V_H(b_2)\le c(b_2-b_1)) for (b_1\le b_2), exact endpoint derivative (V'_H(b)=\min\{H_s(b)-c,0\}), and two-data error (|V_{H_1}(b_1)-V_{H_2}(b_2)|\le\delta+c|b_1-b_2|) when (|H_1-H_2|\le\delta) on the common domain. Constants are sharp; proof uses competitor clipping and the slope bound. **Printed lemma remains correct.**
- **Previously reported, not counted again:** `POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001` concerns the penalization rate and Hessian coefficient, not endpoint value variation.
- **Proposed correction:** none required. Optional new Remark (not applied in production): record the explicit endpoint sensitivity and sharp Lipschitz stability.
- **Potential dependents:** §§16.19–16.20 may use this only with the original slope/common-domain hypotheses; their joint-Hessian and upstream PDE chains are **not certified**. No excluded Demailly proof chain reopened.
- **Proof:** [full report](../reports/2026-11-09-envelope-moving-endpoint-lipschitz.md); **coverage:** [exact increment](../coverage/2026-11-09-ch16-moving-endpoint-lipschitz.md).
- **Coverage count:** existing §16.18 selected review +1 distinct mathematical deduction; **0 first numbered-section visits / 0 full-section certifications**. Owner-excluded material stays **deferred-by-user**.
