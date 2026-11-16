# 2026-11-17 — dense-set convergence for arbitrary convex nets

- **ID:** `POME-CONVEX-DENSE-NET-LOCAL-UNIFORM-001`.
- **Severity:** low.
- **Status:** **verified conditional deduction**, not an original-statement error or a repaired gap.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Location:** `docs/sections/convex-analysis-and-toric-potentials--closed-convex-functions-and-supporting-slopes/index.html`, blob `66bfd5b3f6cdfaced77dc1741a995e22768141f1`; §21.2 tag `5430067C9C99`; Proposition 21.2.6 source `57C22F00`, permanent `EAC7AAEC7279`, lines 159, 177–181; (21.2.2) source `D1805A42`, permanent `C59E34BB3C43`, lines 38–45; Lemma 21.2.3 `5D4512D3` / `34526AA883B2`, lines 49–89.
- **Finding:** the printed sequential dense-limit theorem also holds for all directed nets, provided **eventually** bounded finite control sets are used. A convergent net need not be globally bounded across incomparable early indices; explicit finite-subsets-of-\(\mathbb N\) example in report. No sequential subnet/cofinality assumption.
- **Correction:** optional nonproduction insertion of an arbitrary-net corollary beside the original statement; no alteration to its sequence conclusion.
- **Dependents:** possible convex-envelope, toric, and real Monge–Ampère applications requiring convergence of an original net; no verification of their additional hypotheses.
- **Other direct reading:** Lemma 21.2.3, Proposition 21.2.4, Proposition 21.2.8 and Corollary 21.2.9 checked; none certified transitively because analytic §§2.5,3.4,5.9 remain separate inputs.
- **Full proof:** [anchored report](../reports/2026-11-17-convex-dense-set-net-local-uniform.md).
- **Scope:** Demailly approximation and all dedicated related proof-completion work remain **deferred-by-user**, neither resolved nor certified.
