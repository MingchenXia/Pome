# Actual incremental coverage — 2026-11-11 — §20.5 monomial finite-map pushforwards

**Finding:** `POME-CYCLE-MONOMIAL-FINITE-MAP-GCD-001` (low / verified conditional deduction); **reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **ToC:** 25 chapters / 747 numbered sections. [Report](../reports/2026-11-11-monomial-finite-map-curve-sheet-gcd.md) · [ledger](../ledger/2026-11-11-monomial-finite-map-sheet-gcd.md).

| Section and main blob | Exact integrated passage inspected | Extent and outstanding dependencies |
| --- | --- | --- |
| §20.5 `dae567406b2030e550664ca57b1fe77911d956d4` | Lemma .3 source `demailly-complex-geometry:FF68839A` / permanent `323D5DA3E240`: lines 27–31, 36–59, especially proper generic-sheet coefficient. | New complete monomial-curve normalized generic sheet computation and full finite ambient inverse-image factorization; **not** a verification of general Remmert proper image proof. |
| Same §20.5 | Theorem .5 source `:D58680EB` / permanent `F1C928146DBC`: lines 64–75, 80–127, especially Eq. 20.5.9 `74331B0B45F1` (104–116). | New explicit local divisor order/projection check. General normalized PL current theorem is an **internal conditional dependency**, not globally certified. |
| Same §20.5 | Theorem .10 source `:34D8935D` / permanent `DDB973C0C1DD` lines 133–150; Example .11 source `:1764A64B` / permanent `FF4839E28893` line 155. | Statement/context and cusp calibration only; **no** new review of all intersection-current hypotheses. |

§20.5 was already visited at proof level before this run: **0 new first section visits; 0 fully certified sections**. Other Chapter 20 passages mentioned in the report are *dependent candidates*, not visits or certifications. Prior two-singular-branch and moving-collision findings are unchanged. Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof completion remain **deferred-by-user**. No full source/theorem-chain, software build or formal check was performed.
