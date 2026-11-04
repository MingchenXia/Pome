# Classified incremental findings — 2026-11-04 — NA inverse-limit indexing

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Complete evidence:** [Kähler diagonal and semipositive countermodels](../reports/2026-11-04-nonarchimedean-diagonal-cofinality-and-degenerate-pullbacks.md).

| Finding ID | Severity | Status | Exact anchors | Disposition |
| --- | --- | --- | --- | --- |
| `POME-NA-DIAGONAL-KAHLER-COFINALITY-001` | low | **verified conditional deduction** | Main `docs/sections/non-archimedean-pluripotential-theory/index.html` blob `8448d710690ebe1cc28040f9611d05c9d008a961`, §22.1.15 source `sgpt:176139CE` permanent `3943AA7119C5`, lines 268–308; §22.1.14 `sgpt:5A9D4C43`/`CCAAC9DA4E2F`, lines 256–264 | Kähler two-parameter inverse family is recovered via cofinal half-diagonal. Proof uses explicit commuting transition squares and positive pointwise lower bound on finitely many Kähler forms. Depends on internal §17.14.6. No printed error; optional explanatory insertion only. |
| `POME-NA-SEMIPOSITIVE-NONCOFINALITY-001` | low | **verified conditional deduction** (unprinted shortcut refuted; §22.1.17 **not refuted**) | Same main blob; §22.1.17 `sgpt:D30D14E9`/`817C1BB3E570` lines 312–319; §22.1.19 `sgpt:93D7BBCD`/`347399E47277` lines 323–337; §16.4.4 `sgpt:DE839E2D`/`048490BEAC8C`, tag entry blob `9e66a1fbda45995c256b709f91a6c505e6a15717` | Semipositive big forms are not cofinal in reverse by Kähler forms; explicit `P^1` vanishing conformal form, and pullback `Bl_p P^2` with exceptional null directions. §22.1.17 instead needs analytic extension using §16.4.4; precise model-test-curve extension not certified. Proposed explanatory paragraph and exact internal dependencies; **no confirmed gap/false theorem**. |

**Coverage increment:** selected earlier §22.1.14–19 + §16.4.4 dependency statement; both previously partially reviewed sections, no whole-section certification. All old resolved/unresolved and user-deferred statuses persist unchanged. No regularization/Bergman/L2/OT/multiscale/positivity-loss research reopened. Documentation only on audit branch; no source or main changes.
