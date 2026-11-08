# Ledger entry — 2026-11-08 — proper divisor collision

| ID | Area | Severity | Status | Printed result | Evidence | Proposed action |
|---|---|---|---|---|---|---|
| `POME-CYCLE-TRANSVERSE-COLLISION-NONUNIQUE-001` | §20.5, especially 20.5.2, 20.5.5, 20.5.10 | low | **verified conditional deduction** | All inspected printed statements remain correct; no incorrect proof step established | Two proper-intersection families \(x=0\) and \(x+\varepsilon P(y)=0\) converge to the same divisor pair while products converge to \(0\), \([(0,0)]\), or other supported integral zero-cycles | Optional warning next to Theorem 20.5.10; do not redefine ill-posed \([D]\wedge[D]\). |

Main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Reading file: `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` blob `dae567406b2030e550664ca57b1fe77911d956d4`. Theorem 20.5.10: source `demailly-complex-geometry:34D8935D`, permanent `DDB973C0C1DD`, physical lines 132–152. Lemma 20.5.2: `demailly-complex-geometry:72B4BF94`, permanent `551A781E3A1C`, lines 10–21. Theorem 20.5.5: `demailly-complex-geometry:D58680EB`, permanent `F1C928146DBC`, lines 63–129.

**Dependencies and boundaries.** Uses the local integrability/Poincaré–Lelong normalization already stated in §20.5; the concrete restricted computation is self-contained. No limit interchange of weak current products is asserted. Future reviewers should search for this *specific* unauthorized limit interchange rather than marking §7.28 or §20.6 invalid merely because they use intersection theory. No prior ledger status changed. The owner's explicitly excluded regularization-related programme remains **deferred-by-user**.

[Complete proof and exact sharpness model](../reports/2026-11-08-proper-divisor-collision-nonunique-wedge.md).
