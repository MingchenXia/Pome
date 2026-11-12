# Exact proof-level coverage: 2026-11-12 one-sided moving-mass capacity rate

**Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit.

| Actual numbered section | Integrated file, blob | New inspected statements and physical line anchors | Verified scope | Still not certified |
| --- | --- | --- | --- | --- |
| 7.11 Local energy moments | docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html, e619f7aa95f80ce11aa676193b054db3180e59d4 | Lemma 7.11.19, tag 546063653198, lines 386–425; Proposition 7.11.22, tag 1036F9F7DDDA, lines 428–483; Theorem 7.11.24, tag D25577E2BC26, especially lines 486–533; Theorem 7.11.11 used as internal input | Fresh fixed-index one-sided rate \(2^{2n+2}\delta^{-(n+1)}\varepsilon_j\), proof in [dated report](../reports/2026-11-12-one-sided-capacity-mu-l1-rate.md) | Upstream BT comparison, capacity convergence, subsolution existence and all other section proofs |
| 7.5 Quasi-continuity and convergence in capacity | docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html, 464778b7ca6f1a456e36b24ecb4a0c93ab6948d3 | Lemma 7.5.4, source 34043611/permanent 56B45ADBA326, physical lines 62–78 | Direct specialisation to positive part of a bounded quasi-continuous difference, with appropriate outer capacity | General quasi-continuity and all capacity theorems |

**Finding:** POME-BT-ONE-SIDED-MOVING-MASS-CAPACITY-RATE-001 — low / verified conditional deduction; printed Theorem 7.11.24 not refuted. [Ledger](../ledger/2026-11-12-one-sided-capacity-mu-l1-rate.md).

The two sections were already partially visited, so **0 first-time proof-level numbered-section visits** and **0 full mathematical-section certifications**; the actual ToC remains **25 chapters and 747 numbered sections**. This is a new selected proof step, not a whole-chapter sign-off. Dedicated Demailly approximation/regularization and Bergman/L2/OT/multiscale/positivity-loss remain **deferred-by-user**, not solved.
