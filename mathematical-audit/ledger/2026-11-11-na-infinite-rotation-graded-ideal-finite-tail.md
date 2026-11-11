# POME-NA-FG-TAIL-NONNOETHERIAN-SHARPNESS-001

**Date:** 2026-11-11. **Severity:** low. **Status:** verified conditional deduction; not a false theorem or a full mathematical certification. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Exact integrated anchor:** `docs/sections/non-archimedean-pluripotential-theory/index.html`, Git blob `8448d710690ebe1cc28040f9611d05c9d008a961`. Lemma 22.1.94: `sgpt:AB6FE74C`, permanent `76252E7717AC`, line 1403; equation 22.1.95: `sgpt:EC9FB89B`, permanent `6126C03E6587`, lines 1404–1406; proof 1412–1414. Dependent Proposition 22.1.98: `sgpt:4D7EEB4A` / `6A232EAE791C`, lines 1446–1475, equation 22.1.99 / permanent `9186BF0A5F55` lines 1468–1473.

**Novelty boundary:** `POME-NA-ONE-GENERATOR-GRADING-001` (2026-10-30) **already** established the one-infinite-order-scalar criterion and root-of-unity example, while the canonical graded coefficients, finite Noetherian tail and generic-fiber description were already known from `POME-NA-GRADED-CANON-001`, `POME-NA-TAIL-GENERIC-FIBER-001` (2026-10-31) and `POME-NA-S1-IDEAL-TORSION-FLATNESS-001` (2026-11-02). These are **context, not new audit progress**. The *new* contribution is a uniform bound `D` equal to the maximum `t`-degree of any fixed finite generating list, independent of Noetherianity of `R`, with a sharp non-fg boundary.

**Verified combined statement (prior grading, new uniform degree bound):** An ideal `I⊂R[t]` over **any** complex algebra `R`, preserved by substitution `t↦λt` for a single scalar `λ` of infinite multiplicative order (or by every scalar in any infinite set), is exactly graded: `I=⊕_{j≥0}J_jt^j`, `J_j={a∈R:at^j∈I}`. Finite-degree Vandermonde inversion proves this without Noetherianity, topology or reverse-inclusion hypotheses. For finitely generated `I`, the coefficient-ideal chain stabilizes no later than the maximum polynomial degree `D` among a fixed finite generating family; the precise finite-tail expression is
\[
I=\bigoplus_{j=0}^{D-1}J_jt^j\ \oplus\ J_Dt^DR[t].
\]
The terminal `I_m(t^m)` in printed (22.1.95) is read as this **full tail ideal**, not just one homogeneous degree.

**Sharp boundaries:** the **previously established** finite-order rotation obstruction (not counted again) is (`I=(t^q-1)⊂C[t]`); **new explicit non-fg boundary**: without finite generation the eventual-stabilization claim fails (`R=C[x_1,x_2,\ldots]`, `I=(x_jt^j:j≥1)`, `J_j=(x_1,\ldots,x_j)`). These refute weakened variants, **not** printed Lemma 22.1.94.

**Proposed optional clarification:** display the tail and mention one-infinite-order-scaling criterion, preserving all existing wording, source attribution, permanent tags and alternate valid forms. **Potential dependent:** Proposition 22.1.98's construction of finitely many coherent coefficient ideal sheaves (22.1.99). Analytic gluing/GAGA (Lemma 22.1.96) is an **external dependency**, not certified or replaced here; no claim that the full non-Archimedean theorem is proved.

**Actual coverage:** new selected proof check within already partially visited §22.1: Lemma 22.1.94 and its application in Proposition 22.1.98; Lemma 22.1.96 dependency-only. **+0 first section visits; +0 whole-section certificates.** Inventory from unchanged main: 25 chapters / 747 numbered sections. User-excluded Demailly approximation/regularization and dedicated Bergman, L2, OT, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**. No build, tests, formal verification, CI, site publish, source edits, main edits, or tag/canonicalization edits.

[Complete anchored proof](../reports/2026-11-11-na-infinite-rotation-graded-ideal-finite-tail.md).
