# POME-FINE-NEIGHBORHOOD-LEBESGUE-DENSITY-ONE-001

**Date:** 2026-11-21. **Status:** low / verified conditional deduction. **Printed-error status:** none; the original proposition is true. **Transitive certification:** no.

**Main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Primary anchors:** \`docs/sections/fine-topology-and-balayage/index.html\`, main blob \`d4c8eed09391441b4b6d13e2fa402a60da70be0d\`: §4.2.4 lines 52–81 (source \`D80928DD\`, permanent \`CAAD6BABA60C\`), §4.2.5 lines 86–99 (source \`01F6C408\`, permanent \`9E787ECDB068\`), §4.2.22 lines 491–518 (source \`333EA4BE\`, permanent \`730413AAC920\`). Cross-chapter reading: \`docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html\`, main blob \`1b600ca8444edebc8e05e300cb86ae371e9f8535\`, §2.8.3 lines 80–117 (source \`01CADB42\`, permanent \`CF98893DE93E\`).

**Hypotheses and conclusion:** on any open \`\Omega\subset\mathbb R^d\`, \`d\ge2\`, every fine-open \`U\` has ordinary Euclidean Lebesgue density 1 at every \`x\in U\`. Given a fine-neighborhood witness \`E=\{u>a\}\cap V\ni x\`, with \`u\in SH(V)\` and \`a<u(x)\`, write \`M(r)=\sup_{\overline B(x,r)}u\`. Then
\[
1-\frac{|E\cap B(x,r)|}{|B(x,r)|}\le \frac{M(r)-u(x)}{M(r)-a}\to0.
\]
This follows from the ball submean inequality and upper semicontinuity; completed measurability of fine-open \`U\` comes from §4.2.22. For an arbitrary *possibly nonmeasurable* fine neighborhood, assert only existence of a Borel density-one subset, not its own completed measurability.

**Proposed source change:** optional corollary after §4.2.5; neither the existing positive-measure claim nor permanent tags need modification. **Affected dependents:** §4.2.5 fine-neighborhood non-isolation; the measurable fine-open/density-topology comparison; §2.8.3 only as conceptual contrast. **Open dependencies:** submean theorem §3.4.5 and measurability §4.2.22 not recursively certified. No Demailly-related excluded work reopened.

[Complete English proof and direct review](../reports/2026-11-21-fine-density-one-and-differentiation-review.md) · [exact coverage](../coverage/2026-11-21-ch2-differentiation-ch4-fine-topology.md).
