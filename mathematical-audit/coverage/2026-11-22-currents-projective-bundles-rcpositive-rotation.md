# Precise coverage checkpoint — 2026-11-22

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch:** \`review/mathematical-audit\`. Scope labels mean the *current integrated mathematical text* was read; they do not mean every upstream dependency or prior historical review was reconciled.

| Section | Main blob / exact path | Current run scope | Outcome |
|---|---|---|---|
| §5.63 | \`cb4c3d4e9d653b216cff05eaf23aafb2a01425ec\`, \`docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html\` | **CURRENT-DIRECT-FULL**, mathematical lines 5–108 | Phase coefficient bound, vague upper weak limit, support maximum; 0 new errors, smoothing dependency not certified |
| §6.53 | \`3bf371940d1159461d77d04b3a6e6ba8e5d0f065\`, \`docs/sections/projective-bundle-integration/index.html\` | **CURRENT-DIRECT-FULL**, lines 5–61 | Generic line, blowup minimum and fiber integration; 0 new errors, potential gluing and slicing not certified |
| §11.26 | \`d54016b202422bde3bc5e2c6e493e4618918a7d7\`, \`docs/sections/gauduchon-metrics-and-linear-mass--conformal-changes-and-directional-curvature-positivity/index.html\` | **CURRENT-DIRECT-FULL**, lines 5–109 | Two global counterexamples: missing connectedness of spreading theorem; missing compactness of flat-determinant obstruction |
| §16.10 | \`decb273ec97fcb9bb0ace2e0b90270723ecbea3e\`, \`docs/sections/envelopes-and-model-potentials/index.html\` | **CURRENT-DIRECT-FULL-INTRODUCTION**, lines 5–18 only | Roadmap, not certification of any linked theorem |
| §11.4 | \`ecb4bf9e593dfb25f1644f0561d1aa65bf096b10\`, \`docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html\` | **SELECTED RECHECK** of 11.4.2, lines 20–56; older FULL status preserved | One confirmed missing compact/connected hypothesis in the printed global formulation |
| §§11.3/1.1 | \`docs/sections/gauduchon-metrics-and-linear-mass/index.html\` and \`docs/sections/conventions/index.html\` | **SELECTED scope check** (standing assumptions, §11.3 line 7, §1.1 line 23) | No general compact or connected default for complex manifolds in the current reader |

**Net new recorded current full reads:** 3 substantive sections + 1 introduction; 1 selected formerly full section and 2 standing-hypothesis checks. **New classified findings:** 3 medium confirmed formulation errors; **fully transitive certificates:** 0; **historical first-ever visits:** unknown.

**Explicitly deferred:** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion. Existing records unchanged in meaning; no source or website edit, CI, build or project test.
