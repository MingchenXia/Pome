# 2026-11-22 finding ledger: Hopf radial period and Hermitian torsion glyphs

Reviewed main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Integrated source files, tags, line anchors, and proofs are recorded in [the report](../reports/2026-11-22-hopf-radial-period-monodromy-and-hermitian-torsion-glyphs.md).

## POME-HOPF-RADIAL-PERIOD-MONODROMY-001
- **Severity:** low. **Status:** verified conditional deduction, **not** false theorem / proof gap.
- **Path:** \`docs/sections/locally-conformally-kahler-geometry/index.html\`, SHA \`6ebf8e604b45d3eb748037af506145273ca3875d\`, lines 625–711; source \`non-kahler-pluripotential-theory\`; stable tags \`0452243D80CF\`, \`9A128F70476F\`, \`1D02D96B9AF2\`, \`C4C3411B46C3\`.
- **Hypotheses:** \`F>0\` smooth 2-periodic; \`m=n-1>=1\`, \`k<0\`; unique smooth positive 2-periodic \`C\` solving \`C^mC'=kC+F\`.
- **Verified result:** Poincaré derivative at periodic solution is \`exp(L)\in(0,1)\`; \`H=\partial_kC>0\` solves \`(C^mH)'=kH+C\`; \`L'(k)=\int(C^{-m}-mk C^{-m-1}H)>0\`. Smooth diffeomorphism \`k\mapsto L\` and smooth finite-dimensional data response follow.
- **Correction:** none required. Optional supplementary proof note after Theorem 23.2.41. **Dependents:** §§23.2.41, .43–.45. Not an assertion of global/nonradial uniqueness or certified upstream proof chain.

## POME-HERMITIAN-TORSION-DOUBLEPRIME-GLYPH-001
- **Severity:** low. **Status:** confirmed error **of integrated equation glyphs only**, not a mathematically false original theorem.
- **Path:** \`docs/sections/hermitian-torsion-and-the-bochner-identity/index.html\`, SHA \`4656b430de6ec989ef121eca550afda0be407222\`; main equation (11.48.5) line 27, tag \`8C926C4A6B4A\`; main equation (11.48.18) line 162, tag \`2F5B471E480A\`; their standalone repeat chunks on line 247, tags \`1E5D7A00D2DA\` and \`CC4EDB6E65CB\`. Source \`demailly-complex-geometry\`.
- **Exact reproducible check:** the UTF-8 text has two occurrences of literal \`\\delta ”\` and two of \`\\Delta ”\` (U+201D). Defined \`D''\`, \`\delta''\` and \`\Delta''\` elsewhere in the same section show the intended expressions are \`\delta ''\` and \`\Delta ''\`.
- **Proposed correction:** in a separate reviewed rendering/canonicalization patch, replace all four malformed tokens in their generating source, preserving equation numbers and permanent tags. **Dependents:** Hermitian commutator and Bochner identities §§11.48.3, .9, .15 and their readers. No dedicated L² proof-completion was attempted.

Existing user-deferred entries remain **deferred-by-user**; existing \`movable-tensor-semistability\` external input remains in \`proofs/open-dependencies.json\`, not newly rediscovered.
