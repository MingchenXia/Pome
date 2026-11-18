# 2026-11-19 — Chapter 3 coverage delta, §3.6

Baseline: published main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, actual Pome Chapter 3 `docs/chapters/classical-potentials/index.html` (10 section links, including §3.6), previously maintained global table-of-contents baseline 25 chapters / 747 numbered sections. The original `mathematical-audit/SECTION_MATRIX.md` is preserved verbatim.

| Numbered section | Integrated path and blob | Direct statement/proof coverage in this run | Dependency context | Certification status |
| --- | --- | --- | --- | --- |
| **3.6 Separate harmonicity and subharmonicity** | `docs/sections/separate-harmonicity-and-subharmonicity/index.html`, `1d3c9ebe0d7093f0f069dc2b25b0a47f700f907a` | **Whole section, lines 7–93**: Theorem 3.6.1 `58AAF98CC15E`, lines 7–35; unnumbered real-trace result, lines 37–46; Theorem 3.6.2 `95AFE3B73B3D`, lines 49–93. | §3.7 example only as previously documented contrast; psh-envelope, harmonic extension, subharmonic compactness, Weyl/Baire are conditional inputs, not new direct section readings. | **Direct whole-section review complete for this main SHA; upstream proof chain not certified.** |
| 3.7 Polynomial approximation and separate-subharmonic example | `docs/sections/polynomial-approximation-and-a-separate-subharmonic-example/index.html`, `a4a17c61ef30efb6fc6e20f105baeca052bbed43` | No new complete proof review; used only to exclude conflation of the different hypotheses. | Earlier partial review unchanged. | **No coverage increment.** |

**Counts this run:** +1 entire direct section, +0 full-chain certifications. Global first-direct-visit count unasserted because earlier hypothesis crosschecks do not by themselves establish first visits. No project-wide certification claim.

**Classification:** `POME-REALTRACE-VARIABLE-OBSTACLE-HARTOGS-001` — low, verified conditional deduction, original printed theorems not refuted. **Excluded user-deferred work:** unchanged. No tests/build/CI or publication.

[Audit report](../reports/2026-11-19-separate-harmonic-variable-real-trace.md) · [ledger](../ledger/2026-11-19-separate-harmonic-variable-real-trace.md).
