# POME-TORIC-OKOUNKOV-LEGACY-1228-EQ-LABEL-001

**Date:** 2026-11-22. **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Status:** confirmed error, low severity, unresolved proposed patch. **Kind:** equation-number *display* / legacy locator, **not false mathematics**.

In `docs/sections/toric-pluripotential-theory-on-big-line-bundles/index.html`, blob `d77d383b4bee977cca473ea43627ee7ac449cfda`, Proposition **21.13.33**, source `sgpt-DBC3BA0C`, stable label `DBC3BA0C`, permanent tag `0ED70BB2A7D0`, physical lines 433–463, the second displayed equation has bare label `12.28` at lines **440–442**. The current reading section is §21.13. The preceding properly tagged Eq. **21.13.34**, source `sgpt-C00149C5`, source label `C00149C5`, tag `35302703CBCC`, is at lines 435–437. Under `AGENTS.md` old source numbers are provenance only, never reader equation numbers.

The second equation's **mathematical identity** `Δ_{Y•}(L)=Φ_R(P_D)` is correct: normalized toric character valuation is `k^{-1}ν(s_m)=Φ_R(m/k)`, and distinct character monomials have distinct lowest valuation vectors. No proof gap or false theorem is claimed. The printed label can mislead equation navigation/citation.

**Proposed fix only:** remove the displayed legacy `12.28` on the presently untagged equation or, in a separate reviewed canonicalization patch, supply a stable source label and reader-generated current §21.13 equation numbering. Preserve the equation, source history, attribution and existing permanent tags. Mathematical dependents remain unchanged; citation/navigation is affected. Do not change main/source/registry/published docs in the audit branch. [Detailed proof and checks](../reports/2026-11-22-toric-okounkov-legacy-equation-and-na-net-comparison.md).

Excluded Demailly/Bergman/L²/OT/multiscale/positivity-loss programme continues **deferred-by-user**. No fully certified upstream chain.
