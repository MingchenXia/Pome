# Actual chapter-20 coverage increment — 2026-11-05

Reviewed production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; current ToC still **25 chapters, 747 numbered sections**, with **zero fully mathematically certified sections**. Chapter 20 has exactly eight numbered sections (§20.1–§20.8). This run adds *selected proof/statement coverage within §20.1*, not a certification of the section.

| Current ToC section and exact anchor | New examination | Classification / outstanding work |
| --- | --- | --- |
| **§20.1.5–9**, `docs/sections/the-theory-of-b-divisors/index.html` main blob `4a793dfd462badcb351f54a36cb030cde14a399b`, physical lines 39–119; specifically Lemma **20.1.7** `sgpt:54FCB4C1` / `F5B2C1F1E318` and Example **20.1.9** `sgpt:048A0D73` / `7AF528B0FB3B` | Direct nefness check of `pi^*H-aE`, exact monomial count `1-a^2`, fixed-model trace convergence for merely pairwise distinct moving points, arbitrary prescribed oscillating **big** nef volumes. | `POME-BDIV-MOVING-POINT-ARBITRARY-VOLUME-001`: **low / verified conditional deduction**. Printed statements correct, optional sharpness improvement. General upper-semicontinuity theorem not globally certified. |
| **§20.1.39–43**, same HTML/blob, lines **737–831**; Definition **20.1.39** `sgpt:6AA949A3` / `BFB26AC5F975`; Lemma **20.1.40(3)** `sgpt:B89A01E8` / `6704C2A24387`; Definition **20.1.41** `sgpt:8F1B53C8` / `60343D71D40A`; Proposition **20.1.43(3)** `sgpt:5189BD1D` / `AEC81016D4BC` | Logical domain/type audit of scalar homogeneity at `lambda=0`, and check later extension's domain. | `POME-BDIV-BIG-PRODUCT-ZERO-SCALAR-TYPE-001`: **low / confirmed error limited to typing**; propose `lambda>0` in earlier lemma, retaining later `lambda>=0`. No false intersection identity claimed. |

[Full English proof](../reports/2026-11-05-bdiv-moving-points-arbitrary-volume-and-scalar-endpoint.md) · [resolved/unresolved/deferred ledger](../ledger/2026-11-05-bdiv-moving-volume-and-zero-scalar-typing.md).

**Excluded work:** no Demailly approximation/regularization, Bergman, weighted L2, OT, multiscale-atlas or positivity-loss proof programme; deferred-by-user remains deferred. **No other sections of Chapter 20 added as new mathematical coverage**; previous §20.3 audits retained separately. Audit-only Markdown; no build, CI or publication.
