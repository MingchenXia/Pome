# Exact coverage increment — 2026-11-05 — Chapter 2 ordinal-plank sequential defect

**Actual current main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Current integrated Pome table of contents: **25 chapters, 747 numbered sections**; **zero whole mathematical sections certified**. Coverage in this increment is **part of existing, previously sampled §2.23**, and **not a new first-reviewed or fully certified section**.

| Current section / entries | Integrated file, main blob, physical line anchors | Source labels / permanent tags | What was newly done | What remains |
| --- | --- | --- | --- | --- |
| **§2.23**, Lemma **2.23.3** | \`docs/sections/completions-and-locally-convex-quotients/index.html\`; \`e2c6d25d35020ccefa739f04aa893e173f73c17e\`, **49–93** (definition of \(X,A\); compact sets in \(V\); existing nonextension and net) | \`demailly-complex-geometry:69616994\` / \`5F1410BEA2F7\` | Completely checked a distinct, explicit **ordinary Cauchy sequence** in \(F=r(C_k(X))\) without limit; proved eventual equality on every compact; proved nonextension directly. [Proof](../reports/2026-11-05-ordinal-plank-sequential-incompleteness.md). | Previously proven openness/completeness and other Lemma 2.23.3 dependencies were not transitively re-certified. |
| **§2.23**, Example **2.23.4** | Same file and blob, **95–107** | \`demailly-complex-geometry:8F41A0A7\` / \`B0973308F142\` | New sequence gives an explicit sequentially approximable point missing from the completed scalar-projective-tensor map, under the printed \(G\widehat\otimes_\pi\mathbb C=\widehat G\) identification. | General tensor theorem and §2.23.5 Fréchet proof not reverified. |

**Finding:** \`POME-LCS-ORDINAL-PLANK-SEQUENTIAL-DEFECT-001\` — **low / verified conditional deduction**, no false theorem. New result is **not** the previously recorded net-based proof, nor the bornological finite-support observation of \`POME-FINEST-LCS-BOUNDED-SUPPORT-001\`, nor a claim of sequential cofinality for \(\omega_1\). Suggested body patch only; **no** direct source edits.

**Other sections:** No new proof review credited in any other numbered section. All previous matrix rows and open/deferred ledger items retained, including owner-excluded Demailly approximation/regularization, Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss work (**deferred-by-user**).
