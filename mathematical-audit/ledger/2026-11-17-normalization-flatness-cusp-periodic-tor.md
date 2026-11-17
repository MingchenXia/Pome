# 2026-11-17 — Normalization flatness and the cusp's periodic Tor

**Stable ID:** POME-NORM-CUSP-PERIODIC-TOR-NONFLAT-001  
**Classification:** low / **verified conditional deduction**; no false printed theorem identified.

**Anchors:** production main b6933b772f41b45918f7e25ed1afbbb1fd892272, docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html blob 06439f43d1ce8e83d2529682c9a630bffa3d9c22. Theorem 9.4.6 tag 7042BB57 / permanent 12A47DB401E2 lines 142–159; Definition 9.4.8 tag C9F1CBB2 / 0E1E539882AD line 180; Example 9.4.10 tag 680F3928 / 60A14C7A1845 lines 197–199.

**Verified deduction.** For any reduced analytic local ring A, its finite normalization B is flat over A if and only if B=A. On the cusp A=C{x,y}/(y^2-x^3), B=C{t} has a minimal exact 2-periodic free resolution with differential M=[[-y,-x^2],[x,y]], M^2=(y^2-x^3)I; hence Tor_i^A(B,C)=C^2 for every i>=0. This strictly distinguishes finite normalization from finite flat morphisms and from the topological one-point fiber. The node provides a separate two-branch check.

**Not counted as new:** prior semigroup conductors, delta-invariants, normalization countable-cover defect/repair, and branch-monodromy calculations. They keep their original status.

**Proposed action:** optional explicit nonflatness caution adjacent to the example; do not alter a theorem's hypotheses or falsely label it incorrect. Future algebraic pullbacks along normalization need independent Tor-vanishing if tensor exactness is used. No unexamined downstream result is declared false.

**Upstream:** finite normalization and its integral-closure identification from Theorem 9.4.6 remain conditional; elementary matrix-factorization exactness here is self-contained. **Coverage:** +0 first numbered sections, +0 entire certifications, selected §9.4.6/.8/.10 only. **Deferred-by-user:** full excluded regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme. No CI/build/production writes.

[Full proof](../reports/2026-11-17-normalization-flatness-cusp-periodic-tor.md) · [coverage](../coverage/2026-11-17-ch9-normalization-flatness-periodic-tor.md).
