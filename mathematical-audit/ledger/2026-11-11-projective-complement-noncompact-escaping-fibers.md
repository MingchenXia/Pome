# Confirmed error — POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001

**Date:** 2026-11-11. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Severity:** **high**. **Status:** **confirmed error** (noncompact statement of Theorem 11.18.2); **verified repair** conditional on adding compactness of $X$; not a completed source patch.

**Main anchor:** docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html, blob fab309d460a8411fefcd1ef32a094927d6feea10, **lines 10–25, 51–68**; source **non-kahler-pluripotential-theory:9BF81039**, permanent **B93CB03C68B7**.

**Counterexample:** $X=\mathbb P^d\times\mathbb C$ for $d\ge2$, $E=\operatorname{pr}_1^*\mathcal O(1)$, rank $r=1$, pulled-back Fubini–Study metric; curvature has $s=d$ positive eigenvalues everywhere at nonzero fiber vectors. Printed theorem predicts $U_E$ **2-convex**, requiring $d+1$ positive Levi eigenvalues off a compact set. Escaping compact infinity-divisor fibers $Y_t\simeq\mathbb P^d$ force at most **2** positive directions at a maximum on $Y_t$ outside that compact set. **False conclusion, not merely a proof gap.**

**Correction proposed only:** require compact $X$ in Theorem 11.18.2. Then the printed cutoff is proper and gives the claimed convexity. Qualify dependent Corollary 11.18.4 (source non-kahler-pluripotential-theory:B119F64B, permanent 18D33491ABFD); **that weaker corollary is not refuted**. Corollary 11.18.5 is on compact base and is unaffected.

**Prior classification:** stronger successor to POME-PROJ-COMP-BASE-PROPER-001 (2026-10-23, *proof gap only*); preserve that record, supersede the *assessment* of the theorem's noncompact validity.

**Complete proof:** [2026-11-11 report](../reports/2026-11-11-projective-complement-noncompact-escaping-compact-fibers.md). Previously visited §§11.17/11.18, **0 new first visits / 0 full section certifications / ToC 25/747**. Demailly and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains deferred-by-user. No publication, tests or source edits.
