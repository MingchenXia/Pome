# Direct coverage delta: Chapter 11, §11.5 (2026-11-19)

- **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated source:** `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html`, blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`. **Every mathematical paragraph in lines 5–82** directly read.
- **Original statement/proof coverage:** §11.5.1 Proposition (trace conservation, 11–27), §11.5.3 Corollary (uniform trace bounds, 36–46), §11.5.4 Proposition (Hermitian AM–GM and normalization bound, 57–75); introductions and the warning about full-vs-non-pluripolar pole mass (5–7, 32, 50–53, 80) also read.
- **Stable source/permanent tags:** `non-kahler-pluripotential-theory:0D4A42C8/828FAD1A35BF`, `7E4B1B3F/A9609E0AE7B9`, `C78BBFF1/BFC1330527CA`; equations `DF6E472D/97DCB5703B01`, `671B7CA8/1F99A7154650`, `D615B576/B78F87EF7411`.
- **New conditional mathematical result:** `POME-GAUDUCHON-TRACE-AMGM-SQRT-DEFICIT-001`, pointwise sharp square-root matrix deficit with global integrated version and closed-background equality rigidity. [Detailed argument](../reports/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md); [classification](../ledger/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md).
- **Actual delta:** +1 fully directly read section; +0 transitive upstream proof chains completely certified. Former matrix state `LEGACY-UNRECONCILED` is *not* proof of no prior reading, so **no first-visit increment claimed**.
- **Not reviewed:** Gauduchon's existence theorem in §11.4.2 (only its use as assumed structure was noted), the full original distributional-calculus chain, §13.14.12's singular density bound, or adjacent Chapter 11 sections.
- **Excluded/deferred:** the user-excluded Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains deferred-by-user, not resolved or certified.
- **Technical checks:** self-contained eigenvalue computation, extremizing diagonal family, integrated trace formula, and maximum-principle rigidity verified by direct calculation; no Python/JS checks, build, CI, formalization, or website publication attempted.
