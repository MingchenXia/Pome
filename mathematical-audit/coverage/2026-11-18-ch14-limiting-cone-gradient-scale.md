# 2026-11-18 chapter 14 direct coverage and matrix delta

**Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Main table of contents `docs/chapters/index.html`: freshly read **25 chapters, 747 distinct section links**. Status is a *direct reading* status and never an upstream proof-chain certificate.

| Actual current section | Prior status checked | Work done in this run | Honest status |
| --- | --- | --- | --- |
| §14.15 A Liouville theorem for the limiting cone | Previously sampled: the 2026-11-04 radial nonmaximality model, finding `POME-GAUD-LIOUVILLE-MAXIMALITY-NECESSARY-001`; that finding is **not** new here | Full printed Lemma 14.15.1 and Theorem 14.15.2 proof directly traced, lines 10–154, including perturbation, dimension reduction, directional-energy dichotomy, annulus and comparison | **Entire direct section proof read**; higher dependency certification pending |
| §14.16 The gradient bound by rescaling | No previous proof-level review found in accessible dated audit summaries; matrix-wide historical count not independently established | Complete Proposition 14.16.1 and closing derivative-bound inference lines 7–73; new independent determinant-sensitive consequence `POME-GAUD-GRADIENT-DETERMINANT-SCALE-001` | **Entire direct section proof read**, upstream §14.14/§14.11 not certified |
| §14.13 Matrix structure | Previously sampled | Checked only Eq. 14.13.1 and the fixed linear first-order torsion term, lines 16–35 | **Dependency context**, not a new whole-section check |
| §14.17 Existence for the Gauduchon ansatz | Not reviewed here | Only named as a possible dependent | **Not visited** |

**Increment this run:** one newly targeted nonexcluded section (§14.16) and one prior partially reviewed section completed at *direct* proof level (§14.15). Two complete direct-section readings, **zero** complete transitive theorem-chain certifications. The pre-existing 747-section master matrix is preserved unchanged; this exact dated table is a **non-destructive matrix delta** because the >1 MiB `mathematical-audit/SECTION_MATRIX.md` cannot be retrieved as nonempty text from the available GitHub contents reader in this run. No claims about additional first-ever visits or exact historical master-matrix counts beyond the crosschecked dated summaries.

**Source anchors/blobs:** §14.15 `2a5f42ad68db1f5091a0c2e0c5a29e2c3887cdec` (Lemma `6E3495B1A225` lines 31–47, Theorem `AC61FE141521` lines 51–154); §14.16 `4081db05fb0a989451c4e536f8e285501c399e81` (Proposition `EFE7268223F4` lines 13–73); §14.13 `6e1faedde219b856c0bf5ecaf566403ae999772e` (Eq. `D281466AD7B7` lines 16–35). [Proof](../reports/2026-11-18-gauduchon-gradient-determinant-scale.md) · [ledger](../ledger/2026-11-18-gauduchon-gradient-determinant-scale.md).

Excluded Demailly approximation/regularization plus dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme stays **deferred-by-user**, neither resolved nor certified. No mathematical-body edits, tests/builds, CI or publication.
