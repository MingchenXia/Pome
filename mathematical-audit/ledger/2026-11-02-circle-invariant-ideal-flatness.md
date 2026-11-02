# Classified audit ledger — 2026-11-02 — invariant polynomial ideals

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Review branch:** `review/mathematical-audit`. This increment is additive and does not supersede any existing findings, resolutions, proof gaps or user-deferred work.

| Stable ID | Severity | Status | Verified conclusion | Correction and dependent scope |
| --- | --- | --- | --- | --- |
| **POME-NA-S1-IDEAL-TORSION-FLATNESS-001** | low | **verified conditional deduction** | For a Noetherian \(\mathbb C\)-algebra \(R\) and an \(S^1\)-invariant ideal \(I\subset R[t]\) with trivial action on \(R\), the stabilized coefficient ideal \(J_\infty\) gives \((I:t^\infty)=J_\infty R[t]\); the \(t\)-torsion is \(\bigoplus_{q\ge0}(J_\infty/J_q)t^q\); flatness over \(\mathbb C[t]\) holds exactly if \(J_q=J_0\) for all \(q\), so \(I=J_0R[t]\). The example \(I=(z^2,tz)\) is generically reduced and nonflat at the double special fiber. | Optional corollary after Lemma 22.1.94; guard downstream equivariant ideal arguments against inferring flatness from a punctured product. No theorem/body/registry/tag edit made. |

**Source identity and precise anchors:** `docs/sections/non-archimedean-pluripotential-theory/index.html`, main blob `8448d710690ebe1cc28040f9611d05c9d008a961`, Lemma 22.1.94 source `sgpt:AB6FE74C` / permanent tag `76252E7717AC` (physical lines 1402–1414); equation 22.1.95 source `sgpt:EC9FB89B` / permanent tag `6126C03E6587` (lines 1404–1406). Context only: Lemma 22.1.96 source `sgpt:0D0A3D2C` / tag `AF0C82DE24E9` (lines 1418–1426). Full proof, exact hypothesis boundaries and proposed addition: [dated report](../reports/2026-11-02-circle-invariant-ideals-flatness-and-torsion.md).

**Status distinctions:** The original Lemmas 22.1.94 and 22.1.96 are **not false**. The example refutes only a stronger inference **not stated** in either lemma. Lemma 22.1.96's GAGA invocation is an **external mathematical input**, not an attribution-only citation or a newly verified internal replacement; no new external-dependency ID is opened until its precise integrated replacement and dependents are assessed. Later steps are **unreviewed**. No confirmed error, proof gap or genuine duplication is newly registered.

**Coverage:** first selected direct proof-level review of §22.1.94 and exact-hypothesis crosscheck of §22.1.96. This is not the first review of §22.1, not a complete proof of §22.1.96 and not a certificate for any numbered section. Current actual collection: 25 chapters, 747 numbered sections, zero fully certified. The previously excluded Demailly approximation/regularization, Bergman/weighted-L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**; these matters were not examined in this increment.
