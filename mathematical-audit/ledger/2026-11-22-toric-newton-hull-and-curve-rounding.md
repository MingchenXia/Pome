# Findings — 2026-11-22 toric Newton envelope and curve-section gap

Baseline main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Complete proof and exact scope: [report](../reports/2026-11-22-toric-newton-hull-and-curve-section-rounding.md), [coverage](../coverage/2026-11-22-toric-convex-sections-divisor-rotation.md).

## POME-TORIC-NEWTON-SUP-CONVEX-HULL-001
- **Severity / status:** low / verified conditional deduction (not a false statement or complete upstream certification).
- **Integrated file:** docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html, blob 56a1a55dfc8185aee0e6d495a6a93d8a2313d76b.
- **Anchors:** 21.12.13 permanent 8B5B73657BF7 (239–279); 21.12.23 permanent 73034E124A9A (443–462); 21.12.27 permanent CC64AE504A19 (535–545); 21.12.24 permanent 725063C1ED05 (466–480); example permanent 2B1E84EAAE13 (418–439). Convex duality 21.3.2 permanent 011FA81B0000.
- **Hypotheses:** nonempty arbitrary family of toric \(\omega\)-psh potentials, uniformly bounded above, compact ample toric background. No sequential index hypothesis.
- **Statement/complete conditional proof:** Newton body of the usc supremum is the closed convex hull of the union of Newton bodies; normalized mass is \(n!\) times that hull's volume. In \(\mathbb P^1\), opposite endpoint-pole potentials individually have zero mass but their bounded maximum has full mass. Full Fenchel conjugate/domain proof in report.
- **Proposed correction:** no printed theorem requires correction; optionally add corollary after 21.12.23 and its mass consequence after 21.12.24, without changing source or canonicalization.
- **Affected dependents:** toric envelopes/maxima, Newton-body full-mass tests including 21.12.38.
- **Limitations:** 21.12.24 is accepted only conditionally; no transitive certification.

## POME-CURVE-SECTION-ROUNDING-GAP-001
- **Severity / status:** low / verified conditional deduction.
- **Integrated file:** docs/sections/holomorphic-sections-and-hermitian-mass/index.html, blob 5f00431e7986d899dc833c89175686b75f09371d.
- **Anchors:** §19.8.10–11 lines 255–288, source tag CB9DFB6A, permanent 1E6D5AA611CC.
- **Hypotheses:** compact Riemann surface, logarithmic poles \(c_j>0\), \(d=\sum c_j\leq\ell=\deg L\); eventual exactness assumes \(\ell>d\).
- **Statement/proof:** all-degree \(0\leq \dim\mathcal H_m-\dim\mathcal W_m\leq\#\{j:mc_j\notin\mathbb Z\}\); equality for sufficiently large \(m\) if \(\ell>d\), with exact Riemann–Roch formulas and rational-coefficient quasipolynomial behavior. A skyscraper-sheaf exact sequence plus \(H^1\)-vanishing proves it.
- **Proposed correction:** optional counting corollary, no change to the correct Theorem 19.8.11.
- **Affected dependents:** curve graded-section counting and vanishing-order comparisons.
- **Limits:** Riemann–Roch/Serre are used as existing inputs; the dedicated Bergman/regularization programme was not examined.

**Previously logged items:** §20.6 non-Cartier quadric obstruction remains old, not duplicated as new. Excluded programmes remain deferred-by-user.
