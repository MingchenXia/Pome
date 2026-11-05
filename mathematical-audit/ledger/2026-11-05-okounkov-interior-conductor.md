# Classified finding — 2026-11-05

**Stable ID:** POME-OKO-UNIFORM-INTERIOR-SEMIGROUP-CONDUCTOR-001  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Severity:** medium (two central non-Hironaka proof inputs); no printed theorem refuted.  
**Status:** **verified repair**, **audit-only proposed proof replacement** — not integrated into the production proof. The original printed arguments cite valid named external results, so this is *not* a confirmed theorem error or an assertion that the counting theorem has been proved.

**Primary anchors:** \`docs/sections/almost-semigroups/index.html\`, blob \`33898b2963ad0f8b7e30bf414276642f60925b74\`, Lemma 19.7.25, source \`sgpt:4791A323\`, permanent \`E41D68AC6F7C\`, lines 372–389 (external use at 382). \`docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html\`, blob \`33212916f9ea7754f51f8194cfb76c2fcbe8efab\`, Theorem 19.2.5, source \`sgpt:D2CDA8AC\`, permanent \`37D86D761E81\`, lines 92–111; its repeated proof at \`docs/sections/almost-semigroups/index.html\` lines 401–410. Internal Lemma 19.7.7, source \`sgpt:E50EA8A4\` / permanent \`5C4A19C5ED0B\`, lines 66–94.

**Hypotheses:** additive semigroups in \(\mathbb Z^d\) generating the *entire* ambient lattice; a full-dimensional closed generated cone; compact conical directions strictly **inside** that cone. Both full-lattice and interior restrictions are necessary.

**Complete proof:** [finite-generator/polyhedral-cone and integer-residue conductor lemma](../reports/2026-11-05-okounkov-elementary-interior-semigroup-conductor.md). It yields eventual inclusion of *all* lattice points in compact interior conical sectors and proves (1) the full-group and cone intersection conclusions in Lemma 19.7.25, and (2) the interior lattice filling step of Theorem 19.2.5, without invoking KK12 Theorem 1 or WN14 Lemma 4.8.

**Unresolved/external remaining:** Kaveh–Khovanskii **counting/volume Theorem 19.7.20**, source \`sgpt:282DA4DD\` / permanent \`85641516C8CA\`, lines 299–319, is not replaced or certified. References to KK12/WN14/Kho92 retain historical attribution. Lemmas 19.7.27–29, Theorem 19.7.32, Corollary 19.2.8, §§19.4/19.9 are **affected dependents**, not certified by the present isolated replacement.

**Proposal:** replace *only* the two externally supported interior-saturation proof steps in a **separate reviewable patch/PR**, leaving statements, hypotheses, source tags and history unchanged. No body/registry/canonicalization edits in this audit. No excluded regularization work reopened. Historical status remains zero fully verified mathematical sections.
