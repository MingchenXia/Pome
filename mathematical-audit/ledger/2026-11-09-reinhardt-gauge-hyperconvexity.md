# POME-REINHARDT-HYPERCONVEX-GAUGE-001

- Date: 2026-11-09
- Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- Integrated source: `docs/sections/reinhardt-domains-and-logarithmic-convexity/index.html` (blob `51d14c9874a7f3ec3a4886644749db8ddb82d923`)
- Stable anchors: `demailly-complex-geometry:D34443BE` / `B7A5F2850576` (Proposition 9.62.2, lines 17–34); `demailly-complex-geometry:C667FC59` / `9179B3F88EE7` (Lemma 9.62.3, lines 38–82); `demailly-complex-geometry:463F81C1` / `2A0C2847FC1E` (Theorem 9.62.6, lines 86–108).
- Severity: **low**.
- Classification / status: **verified conditional deduction**; printed results **correct**; no confirmed error, no claimed source repair.
- Hypotheses: (D\subset\mathbb R^n) nonempty open, convex, downward closed; (\Omega=\widetilde\Omega_D\) as in equation 9.62.4.
- Proven: (\Omega) bounded iff each (\sup_D x_j) finite; then the continuous global homogeneous PSH gauge (p_D=e^{\inf\{t:\log|z|-t\mathbf1\in D\}}) (extended at zero-coordinate strata) satisfies (\Omega=\{p_D<1\}), (p_D^{-1}(0)=\{0\}), and (p_D-1) is a bounded negative PSH exhaustion. Conversely a missing coordinate upper bound gives a whole entire axis, excluding hyperconvexity / Kobayashi and Carathéodory hyperbolicity.
- Proof: [complete source-anchored derivation](../reports/2026-11-09-reinhardt-gauge-hyperconvexity.md).
- Suggested correction: **no correction needed**; optional standalone corollary/remark after Theorem 9.62.6 with the coordinatewise-upper-bound hypothesis explicitly stated. Preserve source label, permanent tags and attribution.
- Dependencies: convex monotone logarithmic-composition extension of Lemma 9.62.3 (rederived locally in report), Liouville, Schwarz–Pick. No Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss dependencies.
- Affected dependents: §9.62 complete Reinhardt/hyperconvex model comparisons as an optional stronger statement; **no identified false downstream theorem**.
- Coverage: previously partly audited §9.62; first numbered-section visits **0**, complete mathematical-section certifications **0**. Existing error/gap/deferred ledgers unchanged; excluded programme stays **deferred-by-user**.
