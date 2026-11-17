# Classified finding — 2026-11-17 — two commuting torus monodromies

- **ID:** `POME-TORUS-LOCAL-PAIR-KOSZUL-TORSION-001`
- **Severity:** low
- **Status:** **verified conditional deduction**. No false printed theorem, proof repair, canonical duplication, or full source-chain certification.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Primary integrated anchor:** `docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html`, blob `7a67c86dfb218e1846f0735a8f24f57b65f431fd`; Theorem 10.43.16 source `demailly-complex-geometry:B5A98C8B`, permanent `678E4157C53F`, physical lines 296–310; Lemma 10.43.15 source `demailly-complex-geometry:40652A02`, permanent `9D23E3CA1553`, lines 282–290.
- **Supporting conditional input:** `docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html`, blob `66ca556aac90cacad01dec69e61943398c888865`; Theorem 10.70.3 `demailly-complex-geometry:223C7EB2`, permanent `9E4C37619D42`, lines about 72–103.
- **New mathematics:** For any commuting (R)-module automorphisms (A,B), a finite rectangular Čech reduction gives the two-torus cochain complex (L\to L^2\to L) with (d^0=(A-I,B-I)) and (d^1(x,y)=(B-I)x-(A-I)y). For (L=\mathbb Z^2), (A=\left(\begin{smallmatrix}1&m\\0&1\end{smallmatrix}\right)), (B=I), its (H^1\cong\mathbb Z^2\oplus\mathbb Z/m), (H^2\cong\mathbb Z\oplus\mathbb Z/m). Distinct from prior **circle** finding `POME-CIRCLE-LOCAL-MONODROMY-001`.
- **Proposed correction / affected dependents:** Optional new worked torus example for 10.43/10.70; **no theorem correction necessary**. Relevant to local-system/Čech calculations with integral coefficients. General sheaf comparisons are conditional inputs, not fully certified.
- **Coverage:** previously partly reviewed §10.43; newly inspected double-complex proof lines 282–310 and linked local-system comparison; **+0 first numbered sections, +0 whole-section certificates**. Excluded programme deferred-by-user.
- [Full anchored proof](../reports/2026-11-17-torus-local-systems-commuting-monodromy-koszul.md) · [Coverage](../coverage/2026-11-17-torus-local-systems-commuting-monodromy-koszul.md)
