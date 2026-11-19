# Classified audit finding — 2026-11-19 — general graded semigroup counting

**POME-OKO-GENERAL-LATTICE-INDEX-COUNTING-001** — **medium / verified repair**, audit-only proposed proof replacement; **not** a confirmed error in the theorem and **not** a merged repair.

**Printed input:** Theorem 19.7.20 (Kaveh–Khovanskii), source \`sgpt:282DA4DD\`, permanent \`85641516C8CA\`, \`docs/sections/almost-semigroups/index.html\` lines 299–319, main blob \`33898b2963ad0f8b7e30bf414276642f60925b74\`; referenced by Theorem 19.2.5, source \`sgpt:D2CDA8AC\`, permanent \`37D86D761E81\`, \`docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html\` lines 92–111, blob \`33212916f9ea7754f51f8194cfb76c2fcbe8efab\`. Baseline main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Exact result:** For \(G=\langle S\rangle_\mathbb Z\), rank \(G=n+1\), degree image \(g\mathbb Z\), horizontal lattice \(\Lambda=G\cap(\mathbb Z^n\times\{0\})\), the counts on degrees divisible by \(g\) satisfy
\[
\lim_{g\mid N,\ N\to\infty}N^{-n}|S_N|
=\operatorname{vol}\Delta(S)/[\mathbb Z^n:\Lambda].
\]
Other degrees have empty slices; lower rank gives limiting zero. This proves the full printed general limsup/periodic limit, its full-lattice specialization, and convex-body lattice counting using elementary moving-coset tilings, prior **already verified** finite-residue interior saturation, and inner-volume squeezing. Positive-volume/full-lattice conditions are not silently weakened.

**Status boundaries:** Historical KK12 attribution retained; genuine external counted-volume premise can be replaced by this proof, but its integration remains **proposed**, not completed. The older conductor finding \`POME-OKO-UNIFORM-INTERIOR-SEMIGROUP-CONDUCTOR-001\` (2026-11-05) is a prerequisite, **not newly rediscovered**. Source theorem not false; downstream §19.7.32 and §19.4 remain independently unverified. Demailly and specified analytic programmes remain **deferred-by-user**.

**Proposed action:** Add a reviewed proof next to Theorem 19.7.20 in a separate future source-edit PR, retaining [KK12] historical credit and all tags. No direct body, main, registry, permanent tag, site or CI changes authorized for this run.

[Complete self-contained argument](../reports/2026-11-19-full-semigroup-volume-lattice-index-proof.md) · [exact coverage](../coverage/2026-11-19-ch19-full-semigroup-counting.md)
