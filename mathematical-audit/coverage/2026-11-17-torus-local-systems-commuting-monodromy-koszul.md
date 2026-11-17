# Exact coverage increment — 2026-11-17 — torus local-system cohomology

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. ToC inventory from the existing current-main audit matrix: **25 chapters, 747 numbered sections**. This is not a claim of exhaustive review.

| Scope | Directly inspected | Status |
| --- | --- | --- |
| §10.43, `docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html` (blob `7a67c86dfb218e1846f0735a8f24f57b65f431fd`) | Proposition 10.43.2 finite-cover local-system restriction **lines 41–59** for convention; Lemma 10.43.15 **282–290** and Theorem 10.43.16 **296–310** for total-complex/Čech comparison. Source `demailly-complex-geometry:B5A98C8B`, permanent `678E4157C53F`. | Selected proof checks, not complete section certification |
| §10.70, `docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html` (blob `66ca556aac90cacad01dec69e61943398c888865`) | Theorem 10.70.3 local-system comparison **approximately lines 72–103**, read as a declared **conditional input**; source `demailly-complex-geometry:223C7EB2`, permanent `9E4C37619D42`. | Context/dependency only, not an independent reproof |
| Original earlier §10.43/10.70 circle audit | `POME-CIRCLE-LOCAL-MONODROMY-001` (2026-10-24) | Not recounted as a new result |

**New outcome:** `POME-TORUS-LOCAL-PAIR-KOSZUL-TORSION-001` / low / **verified conditional deduction**. Detailed finite rectangular Čech reduction for two commuting monodromies; explicit (H^0,H^1,H^2), integral torsion in both positive degrees, invertible-monodromy acyclicity, and proof that commutativity is necessary. No printed theorem refuted.

**Counts:** §10.43 was already proof-reviewed in part, and §10.70 had been inspected before. **+0 first-visited numbered sections, +0 entire sections certified**, no others credited. The explicit monodromy calculation is new; the earlier one-circle result is not new progress.

**Deferred-by-user:** All Demailly approximation/regularization and dedicated Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion topics remain deferred, neither reopened nor certified.

**Scope of repository change:** Audit-only Markdown notes on `review/mathematical-audit`; no edits to source bodies, canonicalization, permanent tags, main, workflows, or published website; no tests/build/CI run.

[Report](../reports/2026-11-17-torus-local-systems-commuting-monodromy-koszul.md) · [Ledger](../ledger/2026-11-17-torus-local-systems-commuting-monodromy-koszul.md)
