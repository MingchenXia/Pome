# Selected integrated coverage: logarithmic planar Martin model (2026-11-14)

Reviewed **main b6933b772f41b45918f7e25ed1afbbb1fd892272**, not the evolving audit branch. Actual current ToC: **25 chapters, 747 numbered sections**.

| Numbered section | Integrated target and blob | Exact passages rechecked at proof level | Classification and limits |
| --- | --- | --- | --- |
| **3.2** | docs/sections/kelvin-transforms-and-half-space-potentials/index.html; **f2615a5393af724c3996978212162f94911ff9d9** | $d\ge2$ line 7; Poisson (3.2.5), source classical-potential-theory:2C60ADF3 / permanent 21F1298C637C, lines 57–62; Theorem 3.2.6 source classical-potential-theory:1C8A330A / permanent 6BC86EEF03A9; (3.2.7)/(3.2.8) tags F3ED29BBAD39/8F7C774A9D89, lines 65–75; weighted representation proof lines 80–131 | Newly checked $d=2$ logarithmic Green/Poisson cross-normalization and weighted vague trace; representation **existence** remains a conditional upstream input, no whole-section certification |
| **4.5** | docs/sections/green-energy-and-martin-boundaries/index.html; **976a90f2a5eba299658f73a1eee8b9d3fef8020f** | Martin construction line 106; Theorem 4.5.9 classical-potential-theory:1677A9F0 / permanent 9D6B5CF5E0CF lines 110–122; Theorem 4.5.12 classical-potential-theory:57D18B4C / permanent 6736FBE7368C lines 166–185; Theorem 4.5.13 classical-potential-theory:854603A2 / permanent 0E65F552B1A6 lines 190–213 | New planar one-point boundary, all minimal kernels, tangential escape, normalized Cauchy harmonic measure; general Martin proof not certified |

**New finding:** POME-MART-HALFPLANE-LOG-GREEN-001, **low / verified conditional deduction**. [Full report](../reports/2026-11-14-planar-halfplane-logarithmic-martin-boundary.md) / [resolved-unresolved-deferred ledger](../ledger/2026-11-14-planar-halfplane-martin-boundary.md).

**Precise increments:** 0 numbered sections first visited, 0 whole sections newly certified; §§3.2 and 4.5 had prior selected coverage. The earlier $d\ge3$ upper-halfspace calculation is *not* repeated as a new finding; the logarithmic $d=2$ case was explicitly left out. The user-excluded Demailly approximation/regularization and dedicated Bergman/$L^2$/OT/multiscale/positivity-loss programme remains **deferred-by-user**. Audit text only; no source, main, tag, registry, build, tests, GitHub Actions or publication.
