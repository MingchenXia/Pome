# 2026-11-21: Chapter 7 and Chapter 9 coverage accounting

Main snapshot `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This is direct reading coverage, **not** transitive proof certification.

| Current ToC row | Actual work | Physical file/lines | Assessment |
| --- | --- | --- | --- |
| §7.6 Increasing limits and exceptional envelopes | **FULL direct mathematical section**, statements and proofs 7.6.1–7.6.2 | `docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html`, blob `5e763bdc928794938c37dc3c7a51cc406472d076`, **7–80** | Monotone weak products, fixed quasi-continuous weights, collar/trace argument, local capacity, countable exceptional envelope checked. No newly confirmed printed error; cited inputs not transitively verified |
| §9.7 Proper images and relative principalization | **PARTIAL only**, entire 9.7.5 proof | `docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html`, blob `b44fe157b8c01363da7799990b8ef6ed82525553`, **89–127**; Step 3 line **120** | POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001, a false *proof-only* extra claim; theorem itself valid. §9.7.1–9.7.4 not fully read |
| §9.6 Blowups and resolution | **SELECTED premise**, Theorem 9.6.7 and its divisor explanation | `docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html`, blob `f452f4b1abe5cdfe348ae11fcd934febcfdd570b`, **91–107** | Principalization allowed as an external Hironaka premise; its proof not certified |

**Coverage delta:** +1 complete directly read section, +1 selected theorem/proof section, +1 selected reference section; **+0 independently verified complete upstream proof chains**. All 747 current ToC section rows and prior reports stay in force, with LEGACY-UNRECONCILED history preserved. Do not count previously visited rows as new first visits.

**Finding:** [POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001](../reports/2026-11-21-relative-principalization-residual-divisor-and-increasing-bt.md) is a confirmed, concrete error in a proof sentence, repaired by restricting it to disjointness of (H'), not a counterexample to Theorem 9.7.5. Deferred-by-user Demailly/Bergman/L2/OT/multiscale/positivity-loss programme remains deferred and not certified.

No tests, build, CI, website publication or non-audit modifications.
