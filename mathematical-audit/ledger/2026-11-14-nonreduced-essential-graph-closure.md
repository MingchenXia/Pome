# POME-NONRED-GRAPH-ESSENTIAL-NILPOTENT-001

- Date: 2026-11-14
- Status: **verified conditional deduction**; severity **medium / definition-interface scope**.
- Source: main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/meromorphic-maps-and-analytic-graphs/index.html` blob `f7dfea961fe6ec171c08c1532a8d0ab8e11b8a8c`, lines **7, 11–30, 35–41, 47–51**; permanent tags `BC1BD33555B1`, `33B246500570`, `97D17B3FB015`; source labels `demailly-complex-geometry:754994AC`, `demailly-complex-geometry:C8A637FA`, `demailly-complex-geometry:E391EEEA`.
- Hypothesis: doubled analytic disk `O_D[epsilon]/epsilon²`, deleted origin, affine-line morphism `w↦epsilon exp(1/z)`.
- Conclusion: Definition 9.67.4 admits this meromorphic-map representative; scalar coefficient is not a germ in `M_X` at 0, and no full analytic graph extension with the given reduced support exists. Full coherent-module contradiction in [report](../reports/2026-11-14-nonreduced-essential-graph-closure.md).
- Impact: avoid inferring coordinatewise meromorphicity/full graph from reduced-graph analyticity in nonreduced settings. Theorem 9.67.2 remains valid in its **reduced** scope, Proposition 9.67.3 is valid on `U`.
- Proposed action: document distinction near Definition 9.67.4; future downstream users must declare which notion they require. **No main-source change requested or made.**
- Outstanding: downstream dependence survey; no claim of full proof-chain certification.
- Excluded by user: Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss completion remain **deferred-by-user**, neither repaired nor certified.
