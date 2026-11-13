# Exact selected coverage — 2026-11-13 — Chapter 20 trace masses under contractions

**Reviewed current production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Current main table of contents:** 25 chapters, 747 numbered sections.  
**New first-visited numbered sections:** **0** (§20.2 was already partly audited).  
**New entire sections certified mathematically:** **0**. No claim that §20.2, its transitive dependency chain, or the complete project is verified.

| Section / item | Main integrated path / blob | Source label / permanent tag | Exact physical lines | What was newly examined |
| --- | --- | --- | --- | --- |
| §20.2.29 standing geometry and restricted volume | `docs/sections/the-trace-operator/index.html`, `1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a` | `sgpt:32BCCE77` / `A437169E35B2`; Eq 20.2.31 `sgpt:BDB42FF6` / `03AF8A775E35` | 660–685 | Connected compact Kähler X, smooth connected Y, big class; distinction between non-nef and non-Kähler loci, including the CT22 historical attribution |
| Proposition 20.2.32 (context comparison only) | same | `sgpt:3CF28B36` / `AFC4F39F65CF` | 688–744 | Stronger `Y not subset nK(alpha)` hypothesis; observed mathematical external dependency Matsumura Cor 4.11 at line 733, not proved |
| Theorem 20.2.34 and Eq 20.2.35 | same | `sgpt:30FD148B` / `7EFDFA26519B`; `sgpt:0E153B6A` / `3C4F71AC116E` | 746–786, 813–823 | **New exact** smooth semipositive-pullback trace-mass vanishing order `dim Y - dim f(Y)`, existence versus undefined positive-mass trace, sharp blowup examples; not a counterexample to the theorem |
| Eqs 20.2.36–37, final squeeze | same | `sgpt:6906F73C` / `6EEF71F49B54`; `sgpt:879E21DE` / `E74D68200A33` | 788–817 | Checked selection `epsilon_j<1/j`, fixed-background convergence, sandwich `M<=B_j<=A_j`, and monotonicity passage purely **conditional** on printed `d_S` / NPP inputs |
| Definition 20.2.10 | same | `sgpt:4261C2F9` / `5239E9ADD0FF` | 254–264 | Distinction between ordinary trace and normalized **positive-mass** trace, indispensable in zero-mass example |
| Examples 20.2.15 and 20.2.17 | same | `sgpt:050DD15F` / `917FA516701F`; `sgpt:628E430C` / `2272C87A04CE` | 310–315; 327–337 | Smooth restriction/type baseline and conditional positive-mass criterion; no excluded proof re-read |

**New stable finding:** `POME-TRACE-CONTRACTION-RANK-MASS-ORDER-001`, **low / verified conditional deduction**. The polynomial argument is direct for smooth forms. The unreviewed general `d_S` trace construction, product comparison, and positivity of general non-pluripolar masses must **not** be inferred from this model. See [complete report](../reports/2026-11-13-trace-contraction-rank-mass-vanishing.md) and [classified ledger](../ledger/2026-11-13-trace-contraction-rank-mass.md).

**Deferred-by-user:** the Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme is unchanged, not resolved. No build, tests, GitHub Actions CI, website publication, or source/main/registry/tag changes.
