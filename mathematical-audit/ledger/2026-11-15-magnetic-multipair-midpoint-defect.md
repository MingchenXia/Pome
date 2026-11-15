# Ledger entry — 2026-11-15 — multipair magnetic zero-field deficit

**Stable ID:** POME-MAGNETIC-MULTIPAIR-MIDPOINT-DEFECT-001  
**Severity/status:** low / verified conditional deduction.  
**Printed source verdict:** Lemma 2.24.6 and Proposition 2.24.8 are not refuted.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Source locations:** docs/sections/magnetic-models-and-spectral-localization/index.html blob ee89de7d23cc96a8546c736ac7d068546b126f3a, lines 31–54, 59–71, 76–110; source labels and permanent tags are individually pinned in the [report](../reports/2026-11-15-magnetic-multipair-zero-field-midpoint-defect.md).

**New mathematical content:** For n>=2, all b_j>=0 and E>=0, the zero-field convolution Riesz mean dominates the magnetic mean and the deficit is at most E^(n-1) sum(b_j^2)/[8pi(2pi)^(n-1)]. In n=2 with one nonzero field, the complete oscillatory cubic-remainder identity proves a strictly positive limiting deficit coefficient E/(96pi^2) after division by b^2; the quadratic power is optimal. This is **not** the previously logged 2026-10-27 one-pair defect; that finite-sum formula is reused only as input.

**Reason/repair:** midpoint Jensen convexity, exact finite odd-square sums, positive-measure Tonelli and a telescoping replacement argument; no unsupported interchange or unproved regularization. Optional new corollary to be considered in a separate source/body PR, not patched in main.

**Dependents/limits:** strengthens the constant magnetic-field comparison behind §§2.24.6/2.24.8; does not certify the underlying oscillator completeness, manifold localization or general Morse inequalities. Actual first-visited sections +0, full section certification +0; chapter/section inventory 25/747. Dedicated Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**. Neither a false theorem nor a completed proof replacement is asserted.
