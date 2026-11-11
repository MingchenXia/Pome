# 2026-11-12 ledger — coprime plane-branch normalization and conductor

| Stable finding ID | Severity | Classification | Disposition |
| --- | --- | --- | --- |
| POME-NORM-COPRIME-PQ-SEMIGROUP-CONDUCTOR-001 | low | **verified conditional deduction** | New exact \(p\ge3\) cusp semigroup/gap symmetry, conductor \(t^{(p-1)(q-1)}\mathbb C\{t\}\), \(p\) minimal conductor generators, \(\delta=(p-1)(q-1)/2\), and Jacobian colength \(2\delta\). **No printed error.** |

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Reading-edition source:** docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html, blob 06439f43d1ce8e83d2529682c9a630bffa3d9c22. **Anchors:** Prop. 9.4.3, foundations-of-pluripotential-theory:AC231B8D / 36422A732754, lines 52–79; Thm. 9.4.6, :7042BB57 / 12A47DB401E2, lines 142–159; Ex. 9.4.10, :680F3928 / 60A14C7A1845, lines 197–199. [Complete hypotheses and proof](../reports/2026-11-12-coprime-plane-branch-semigroup-conductor-symmetry.md).

**Affected interpretation / proposed correction:** none to the printed statement or proof. For §§9.5, 9.9 and 20.5, retain separate invariants for normalization branch number, coordinate-projection degree, semigroup gaps, and conductor; if a later expository example is added, make it a separate reviewable patch, not an audit-branch body edit.

**Prior entry retained, not reproduced as new:** POME-CURVE-DOUBLE-COVER-MONODROMY-CONDUCTOR-001 (2026-11-06), \(p=2,q=2m+1\) comparison with a two-branch curve. POME-NORM-COUNTABLE-COVER-001 is an earlier independent countability finding; its status is unchanged.

**Unresolved / conditional:** general normalization Theorem 9.4.6 and higher-dimensional finiteness/coherence proof chain not certified by this model; elementary Weierstrass division is the explicit analytic input. **Deferred-by-user:** Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof programme. No completed repair is claimed.

**Actual coverage:** selected re-review of §9.4.3/.6/.10; 0 newly first-visited numbered sections, 0 fully certified sections. ToC: 25 chapters / 747 sections. No production, source, registry, CI, tests, build, publication or tag changes.
