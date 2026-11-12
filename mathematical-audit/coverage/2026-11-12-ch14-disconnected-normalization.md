# 2026-11-12 — precise incremental coverage: Chapter 14 connectivity scope

**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Current ToC:** 25 chapters, 747 numbered sections.

**Finding:** POME-MA-DISCONNECTED-COMPONENT-SCALAR-001; high / confirmed error in the printed scope without connectedness. The correct connected-manifold theorem was not refuted or independently certified.

| Integrated section / file | Blob SHA | Actually inspected | Result |
|---|---|---|---|
| §14.1 \`docs/sections/smooth-monge-ampere-equations/index.html\` | \`e35eb98bdc1c62c4938155964945f4d6495b4ee4\` | chapter-wide scope lines 7–17, Eq. 14.1.1 lines 9–14 | no connectedness declared |
| §14.2 \`docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html\` | \`3f96829e18befc845df40c6d4bca13c977ae9cea\` | Theorem 14.2.1 lines 10–15, Prop. 14.2.2 lines 18–29, Prop. 14.2.4 lines 49–65 | explicit disconnected Kähler counterexamples to existence/uniqueness and global constancy |
| §14.3 \`docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html\` | \`f774b702e65736ce8a23847dbb3409c6b31b0211\` | Lemma 14.3.1 lines 10–30, Lemma 14.3.2 lines 32–105, Thm. 14.3.5 lines 107–149; deeper check of final connected \(L^1\) dependency lines 143–149 | counterexample to global \(C^0\) bound; no claim to certify all Cherrier steps |
| §14.4 \`docs/sections/smooth-monge-ampere-equations--the-linearized-equation-and-smooth-dependence/index.html\` | \`2f9ebecbd5bd079eb8573b4bb97df0fb5ab1bdfb\` | Proposition 14.4.1 lines 19–38 | explicit kernel under mean-zero normalization; inverse not available on disconnected \(X\) |
| §14.6 \`docs/sections/smooth-monge-ampere-equations--the-continuity-method/index.html\` | \`81d74e60560d2241c9e3cc0dacf583d080b8bdd8\` | Theorem 14.2.1 proof lines 9–26 | example has solvable path set exactly \(\{0\}\), so openness fails on this scope |

**Supporting crosschecks only:** §1.1 conventions \`docs/sections/conventions/index.html\`, blob \`ef778e54d8d7413242387e95c52269b3c7d42cae\`, lines 17–25; §5.22 opening connectedness clause \`docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html\`, blob \`bf6e5ca74ac04a3d79565bb58bda8d968a68be68\`, line 7; §5.25 Theorem 5.25.2 connected-cover proof \`docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html\`, blob \`d7ff8eafea43197c77de4bfd335bed0764ab4f69\`, lines 31–51.

**Counting discipline:** these numbered Chapter 14 sections had previous selected audit coverage. **+0 first proof-level numbered-section visits, +0 fully mathematically certified sections.** No assertion about complete Chapter 14 or whole Pome verification. No source, permanent tag, registry, main, CI, builds or website were changed.

**Full report:** [disconnected Hermitian Monge–Ampère scalar obstruction](../reports/2026-11-12-disconnected-hermitian-ma-normalization-counterexample.md). **Ledger:** [classified error](../ledger/2026-11-12-disconnected-hermitian-ma-normalization.md). Demailly approximation/regularization and the associated owner-excluded proof programme remain **deferred-by-user**.
