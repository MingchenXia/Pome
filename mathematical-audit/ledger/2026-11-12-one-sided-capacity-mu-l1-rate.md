# POME-BT-ONE-SIDED-MOVING-MASS-CAPACITY-RATE-001

- Date: 2026-11-12.
- Severity: **low**.
- Status: **verified conditional deduction** (not confirmed error, not proof gap, and not a complete analytic certification).
- Production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Exact integrated file: docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html (blob e619f7aa95f80ce11aa676193b054db3180e59d4).
- Primary anchor: Theorem 7.11.24, original foundations-of-pluripotential-theory:3CB9FBEE, permanent D25577E2BC26, physical lines 486–544, especially 499–511 and 515–533.
- Supporting anchor: Lemma 7.5.4, original foundations-of-pluripotential-theory:34043611, permanent 56B45ADBA326, docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html (blob 464778b7ca6f1a456e36b24ecb4a0c93ab6948d3), lines 62–78.
- Hypotheses: relabeled canonical Dirichlet sequence of Theorem 7.11.24, \(\varepsilon_j=\int|U_j-u|\,d\mu_j\to0\) and \(E_2=\sup_j e_2(U_j)<\infty\).
- New conclusion: \(\operatorname{Cap}_B^*(K\cap\{U_j<u-\delta\})\le 2^{2n+2}\delta^{-(n+1)}\varepsilon_j\) for every compact \(K\Subset B\), \(\delta>0\), each \(j\).
- Justification: one-sided positive-part application of Lemma 7.5.4, published Step 1 truncation comparison, two \(E_2\) deep-sublevel bounds, and **fixed-index** \(T\to\infty\). [Complete proof](../reports/2026-11-12-one-sided-capacity-mu-l1-rate.md).
- Proposed change: optional quantified *one-sided* corollary after Theorem 7.11.24 Step 3; **no correction to the printed theorem**, no source/body/registry edit.
- Affected dependents: selected capacity convergence uses in §§7.11–7.12; **upper** deviation has no matching estimate proved here.
- Exclusion: regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss permanently **deferred-by-user** until owner changes scope.
- Actual added coverage: previously partly sampled §§7.11 and 7.5; **+0 first numbered-section visits; +0 entire-section certifications**. Current ToC 25/747.
