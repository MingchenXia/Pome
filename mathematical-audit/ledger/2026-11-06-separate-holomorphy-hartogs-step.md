# Classified mathematical audit ledger — 2026-11-06 — separate holomorphy

**POME-SEPHOL-HARTOGS-SUBMEAN-FATOU-001** — **low / verified repair** (audit-only proposed self-contained step, no false printed theorem).

- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Exact target:** docs/sections/separate-holomorphy/index.html, blob 2eafedb77d4a45f0133a5d92e27ad16b0be44ffd. Theorem 9.12.1 source klimek-pluripotential-theory:120C7FB1; permanent 362351A63FB6; lines 8, 22–28, 36–50; especially Hartogs lemma invocation at 39–42.
- **Claim verified:** for locally uniformly upper-bounded real subharmonic v_j and pointwise limsup v_j≤c everywhere, \(\limsup_j\sup_Kv_j\le c\) for every compact K. Direct proof by moving-center submean, a fixed inner ball, nonnegative Fatou and δ↓0. Applied to \(v_j=\log|c_j|/j\) to justify the uniform coefficient bound for every s<R.
- **Proposed correction:** insert the elementary self-contained lemma in place of, or immediately after, the untagged named Hartogs-lemma invocation; preserve the theorem statement, source attribution and permanent tags. Endpoint s=R requires extra multiplicative control and is not valid with coefficient 1 (the example \((1-w/R)^{-2}\) has coefficients \((j+1)R^{-j}\)).
- **Scope/status:** closes only the explicit analytic dependency step. Remaining original Baire and recentering arguments inspected, not all external underpinnings or the whole section certified. Existing report of 2026-10-24 is not overwritten or relabelled; existing confirmed errors and user-deferred work stay unchanged.
- **Full proof:** ../reports/2026-11-06-separate-holomorphy-submean-fatou-quantitative-hartogs.md. **Exact coverage:** ../coverage/2026-11-06-ch9-separate-holomorphy-hartogs-step.md.
