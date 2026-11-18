# Finding ledger — 2026-11-19 — §17.2

| Finding ID | Status | Severity | Main SHA | Complete upstream verification? |
| --- | --- | --- | --- | --- |
| POME-NPP-IBP-DIRICHLET-SEMINORM-001 | **verified conditional deduction** | low | b6933b772f41b45918f7e25ed1afbbb1fd892272 | **No** |

**Hypotheses:** Compact Kähler X, dimension n>=1; arbitrary closed positive (1,1)-currents T_1,...,T_{n-1}; non-pluripolar wedge R (or R=1 for n=1); real bounded quasi-psh differences a,b modulo pluripolar changes. Their presentations have matching singularity types.

**Result:** The well-defined form Q_R(a,b) = -∫ a dd^c b ∧ R is symmetric, positive semidefinite and obeys Q_R(a,b)^2 <= Q_R(a,a) Q_R(b,b). The resulting seminorm is sharp with coefficient one, and the null-space quotient is an inner-product space; it is *not* claimed to be complete. Smooth positive R and b=ca supply sharpness. This neither refutes nor corrects the printed integration-by-parts theorem.

**Integrated anchor:** docs/sections/relative-energy-and-perron-segments--integration-by-parts-for-bounded-differences/index.html, blob 5779ef1a17a52e02052c7485a7aa04adf606aace. Signed factor 17.2.1 source foundations-of-pluripotential-theory:563C886F, permanent 6B17AADE0338, lines approx. 20–35. Symmetry Theorem 17.2.5 source :609B8782, permanent 3E698B84D63D, lines 155–195. Positivity Lemma 17.2.7 source :D31C3788, permanent 52C5A516B8C8, lines 198–230.

**Justification and proposed disposition:** Linear presentation independence follows from 17.2.1; Theorem 17.2.5 supplies symmetry; Lemma 17.2.7 gives positivity; the discriminant argument gives Cauchy–Schwarz and the kernel claim. Proposed optional addition: a new corollary after 17.2.7, only by a separately reviewable production patch. No source or registry edit made.

**Dependents:** §17.3 energy concavity and the general family of relative-energy estimates; conditional on the underlying locality/mass/capacity inputs (13.2.6, 13.5.4, 13.8.8–9, 16.25.6 and 16.27.17–18). Printed proof's Step 3 original-potential 4lambda/5 calculation was inspected and found correct; no new confirmed error.

**Coverage/status:** All mathematical paragraphs of §17.2 directly read (+1 entire direct section; +0 transitive chain certificates), historical first visit not asserted. Demailly approximation/regularization and its specified Bergman/L²/OT/multiscale/positivity-loss proof programme is **deferred-by-user**, not resolved or certified. Older findings are unchanged.

[Complete anchored report](../reports/2026-11-19-bounded-qpsh-difference-dirichlet-seminorm.md).
