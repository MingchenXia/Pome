# Classified finding — 2026-11-11 — mixed NPP power sum

- **ID:** `POME-NPP-MIXED-POWER-SUM-THRESHOLD-001`
- **Severity/status:** low / **verified conditional deduction**. Neither the integrated Example 13.2.9 nor Lemma 13.2.2 / Proposition 13.2.6 is erroneous.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated file/blob:** `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html` / `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`.
- **Anchors:** Lemma 13.2.2 `foundations-of-pluripotential-theory:CE1D6DA5` / `D59675D9F6D8`, lines 34–52; criterion Eq. 13.2.3 `:F86748C9` / `E88E33ACAD5B`, lines 36–40; Proposition 13.2.6 `:E82F0D73` / `7F7123F92478`, lines 80–125; Example 13.2.9 `:2F8E45A2` / `6F4C920FEDCA`, lines 151–165.
- **Hypotheses:** `u_s=(|x|²-1)(-log|y|)^s` on `|x|²<c<min(1-a,1-b)`, `0<a,b<1`; extend `-∞` on `y=0`. Both psh with zero Lelong number.
- **New conclusion:** the mixed NPP wedge is locally finite **iff `a+b<1`**, with exact explicit density/cylinder mass and sharp logarithmic endpoint. Taking `a=1/8,b=3/4` proves a locally finite mixed product can coexist with a non-locally-finite self-square.
- **Distinctness:** the registered 2026-10-30 `POME-NPP-POWER-SINGULARITY-THRESHOLD-001` already proved **only the diagonal `a=b`** threshold; preserve it, do not duplicate it.
- **Proof and proposed correction:** [full source-anchored derivation](../reports/2026-11-11-mixed-nonpluripolar-power-sum-threshold.md); optional adjacent mixed-case remark only, **no source/body edit**.
- **Affected dependents:** local-finiteness hypotheses in §§13.2–13.5 and §13.14; neither downstream theorem failure nor independent certification asserted.
- **Unresolved/conditional:** general BT/plurifine locality, psh-extension, global finite-mass assumptions; existing error/gap/duplication ledgers untouched.
- **Deferred-by-user:** Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss proof programme; still excluded, not certified.
- **Coverage:** additional selected proof passages in previously visited §13.2; **+0 first proof-level numbered sections, 0 complete sections**, ToC 25/747.
