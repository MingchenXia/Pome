# 2026-11-20: planar distance, local convexity and firm metric projection

- **ID:** `POME-PLANAR-DISTANCE-LOCAL-CONVEX-GEODESIC-001`
- **Severity/status:** **low / verified repair (audit-only)**, plus a **verified conditional deduction**. **No printed false theorem**; this is a replacement proof for the unlinked classical local-to-global convexity input in §3.9.2, not a blanket assertion that no other internal proof exists.
- **Main and integrated blob:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/planar-boundary-distance-and-convexity/index.html` (`25fd0fd57d3e51f9224a25341ace77584b2a1a2a`), all mathematical lines 7–107. Source/permanent: `klimek-pluripotential-theory:219D9DEC / 59D258340230`; §3.9.1 `79D31B13 / 964B6728E795`; §3.9.3 `366D2F88 / BBEB233BF8A4`.
- **Input:** nonempty proper closed F⊂R², connected open G⊃F, and subharmonicity of d_F on G. Existing proof establishes local convexity and a retraction P:G→F, then invokes the closed connected locally convex ⇒ convex lemma without a proof in that paragraph (line 78).
- **Verified repair:** complete shortest-polygonal-geodesic proof of the local-to-global convexity lemma. **New conditional consequence:** unique global projection is firmly nonexpansive; D=d_F²/2 belongs to C^{1,1}(R²) with gradient I−P_F globally 1-Lipschitz, universal constant sharp.
- **Dependents:** §3.9.2 conclusion and §3.9.3 boundary-neighborhood implication. A report-level proof and optional proposed editorial insertion only; main and source unchanged.
- **Dedup:** prior 2026-11-13 nonconvex-circle result is about a hypothetical dimension≥3 extension, and the older §3.9 slab result is not counted as new.
- **Scope:** whole current §3.9 mathematical text reviewed, one section added to direct-full records, zero completed upstream chains, no claim of first historic visit. Demailly and dedicated related programme **deferred-by-user**.
- **Full reasoning:** [dated report](../reports/2026-11-20-planar-distance-local-convexity-and-firm-projection.md); [coverage](../coverage/2026-11-20-planar-distance-local-convexity-and-firm-projection.md).
