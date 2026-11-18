# 2026-11-18 — POME-CPN-KAHLER-TARGET-RANK-RIGIDITY-001

- **Severity:** low.
- **Status:** verified conditional deduction.
- **Printed theorem classification:** The integral cohomology Lemma 10.75.1 and Theorem 10.75.2 are correct, and their complete integrated proofs were checked. **Not** a confirmed error or a proof-gap declaration.
- **Source and exact anchors:** main b6933b772f41b45918f7e25ed1afbbb1fd892272; docs/sections/spectral-sequences-support-and-cup-products--the-integer-cohomology-ring-of-projective-space/index.html (blob cb90abebae459659c273b9de67848f3feded35e3); source demailly-complex-geometry:1EB6C39D / permanent 419BAFBD0FA6 lines 17–42, and source demailly-complex-geometry:FF8EE3A7 / permanent 0CD4D885B4B4 lines 47–80.
- **New result:** a nonconstant holomorphic f:P^n→Y into a compact Kähler manifold has [f*η]=c[ω_FS] with c>0, rank(df)=n somewhere and no positive-dimensional fibers; consequently dim_C Y<n forces f constant. Proof uses positive trace, (f*η)^n=c^nω^n and integration over any hypothetical compact fiber component.
- **Prior-work distinction:** POME-PROJ-GRAPH-DIAGONAL-INTEGRAL-SIGNS-001 (2026-11-12) already computed self-map graph intersections and d^n degrees. The present arbitrary-Kähler-target rank/fiber obstruction does not duplicate those numerical computations.
- **Proposed correction/addition:** Optional standalone corollary after 10.75.2; no current printed text requires correction.
- **Affected dependents:** potential use in projective charts/flags or projective maps (§§9.59, 10.40, 19.9); none certified or refuted by this new implication.
- **Remaining exact dependencies:** Pome's integral cap duality/support comparison (§§10.69, 10.71), functorial multiplicative Θ/Ψ signs (§10.58), Chern convention (§10.40), Fubini–Study normalization (§10.50), closed integration-current pairing for analytic subvarieties (§20.6). These are conditional inputs, not whole-section certifications.
- **Coverage:** 0 first-visited sections; 1 newly full directly audited (§10.75); 0 full transitive dependency certifications; main TOC 25/747.
- **Deferred-by-user:** all Demailly approximation/regularization and associated dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion work remains excluded and uncertified.
- **Report:** [2026-11-18-projective-kahler-target-rank-rigidity.md](../reports/2026-11-18-projective-kahler-target-rank-rigidity.md).
