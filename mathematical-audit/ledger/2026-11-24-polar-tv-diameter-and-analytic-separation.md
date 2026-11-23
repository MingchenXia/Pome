# POME-ZERO-VOLUME-POLAR-TV-SHARP-DIAMETER-001 — exact polar-model diameter and nonseparable zero-volume analytic locus

- **Date:** 2026-11-24
- **Status:** **low / verified conditional deduction** (not a printed-theorem error; general compact-curve extension conditional on the established curve model/Green classification)
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Precisely anchored source:** `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--divisorial-products-and-zero-volume/index.html`, blob `203607fc492e0027cbfd8f71d64ec6c0b3c57bf3`, physical lines 133–181 and 189–278. Definition 18.15.6–7 (source `non-kahler-pluripotential-theory:8A7CC477`, permanent `F217B40D9074`), Proposition 18.15.8 (source `non-kahler-pluripotential-theory:4766BD27`, permanent `6DEB26AFE67E`), Corollaries 18.15.9–10 (permanents `DFCE5415EAB5`, `13B4DE048053`).
- **Hypotheses and conclusion:** compact connected curve, smooth positive `eta` of mass `A>0`, divisor-fibration locus `S_Psi` of §18.15; its total-variation polar metric has **exact diameter `2A`**, including on the ideal locus. It contains an uncountable `2A`-separated family; for `P^1` with probability Fubini–Study, the family is explicitly of analytic singularity type. Every pair has zero `d_Theta`, and moving poles can converge in `L^1` without converging in `rho_Psi`.
- **Proof:** [full formulas and verification](../reports/2026-11-24-polar-model-tv-diameter-and-degenerate-volume.md). Upper bound is TV triangle inequality; lower bound is by Green potentials with polar curvatures `A delta_x` and `A delta_y`; the model property is checked by removable subharmonic extension and compact maximum principle. Explicit `P^1` formula independently establishes the analytic case.
- **Proposed correction:** none required; optional *remark* following Proposition 18.15.8 (not a source or registry patch).
- **Affected dependents:** metric models in §§18.15.8–10, interpretations of curve polar-TV models in §13.28. Distinct from prior trace-metric nonseparability `POME-TRACE-MOVING-ATOMS-NONSEPARABLE-L1-001`.
- **Upstream status:** source theorem and its general dependency chain not certified; no test/build/CI.
- **Deferred-by-user:** Demailly/regularization, Bergman, L², OT, multiscale-atlas, positivity-loss programmes unchanged.
