# POME-GREEN-JENSEN-LEVEL-CONVEXITY-001

**Date:** 2026-11-22. **Status:** low / verified conditional deduction, **not** a source theorem error. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Location:** `docs/sections/green-level-measures-and-boundary-representation/index.html`, §7.20 Proposition 7.20.2, permanent `351C8FCB17FF`, blob `895dbdfaa3c78ce41abe556f573644d857ab7517`, lines 48–80 (exact level integral at 68–80).

For bounded hyperconvex (D), pole (a), Green function (g), and (v\in\mathrm{PSH}(D)\cap C(D)), Proposition 7.20.2 defines the positive classical mixed measure (\nu=dd^c v\wedge(dd^cg)^{n-1}). With (F(r)=\int v\,d\beta_r), (\beta_r=(dd^c\max(g,r))^n), and (H(r)=\nu(\{g<r\})), its exact Jensen integral is
[
F(r)=2^{-n}v(a)+\int_{-\infty}^r H(t)dt.
]
The finite weighted integral proves local finiteness of (H). Increasing sublevels give its left continuity, and finite-measure continuity from above gives (H(r+)=\nu(\{g\le r\})). Therefore (F) is continuous and convex on ((-\infty,0)), (F'_-=H), (F'_+=H(r+)), and the positive distribution (F'') equals the pushforward (g_*(\nu|_{D\setminus\{a\}})) on **finite levels**. Slope jump at (r) equals (\nu(\{g=r\})). No level-set atomlessness assumption is made.

**Sharpness:** in the unit disc, (g=\log|z|), (v=\max(g,c)) for (c<0), (F(r)=\tfrac12\max(r,c)), hence (F''=\tfrac12\delta_c). A general (C^1) claim would be false.

**Proposal:** optional adjacent corollary; leave original Proposition 7.20.2 unchanged. **Dependents:** §7.20.3–4 and further Green-level boundary arguments, only as stronger information. **Unresolved upstream:** construction of the classical one-point full mixed measure (§7.18/§7.20.2) is taken as an established internal input, not globally recertified. **No other new finding from the five-section rotation.** [Detailed proof](../reports/2026-11-22-green-jensen-level-convexity-and-volume-domination-review.md).
