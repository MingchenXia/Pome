# 2026-11-06 — finite curve double covers: conductor and monodromy

**ID:** \`POME-CURVE-DOUBLE-COVER-MONODROMY-CONDUCTOR-001\`. **Severity:** low. **Status:** **verified conditional deduction** (self-contained exact examples; original printed results correct; general theorem chains not certified).

Reviewed production main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Source anchors:** §9.5 integrated \`docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html\` (blob \`2c725646172203283ac4564bddd46213d9a75cbe\`), Proposition 9.5.1 lines 10–11, Lemma 9.5.5 lines 84–101; §9.4 integrated \`docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html\` (blob \`06439f43d1ce8e83d2529682c9a630bffa3d9c22\`), Proposition 9.4.3 lines 52–78, Theorem 9.4.6 lines 142–159, Example 9.4.10 lines 197–199. Source/permanent tags in [full proof](../reports/2026-11-06-double-cover-nodal-tangency-versus-unibranch-cusp.md).

**Verified:** For each \(m\ge1\), the reduced two-branch curve \(y(y-x^m)=0\) (nodal when \(m=1\), tangent when \(m\ge2\)) and irreducible cusp \(y^2=x^{2m+1}\) share generic degree 2, set-theoretic fiber counts (2 off zero / 1 at zero), critical image \(\{0\}\), and normalization-quotient length \(\delta=m\), but their normalized singular fibers have respectively 2 and 1 point and the punctured-cover monodromies are respectively trivial and transposition. Conductors are \(x^m\widetilde{\mathcal O}\), with optimal \(x^m\) denominators in both examples. Full ring calculations and proofs: [report](../reports/2026-11-06-double-cover-nodal-tangency-versus-unibranch-cusp.md).

**False theorem / proof gap?** Neither; *no printed theorem is refuted* and no claim about the general proof's certification is made. **Proposed action:** audit-only explanatory comparison; do not edit main/source/registry/tags. **Affected dependencies:** any finite-projection argument inferring number of branches from generic degree, original set-theoretic fibers, or \(\delta\) (including context §§9.4, 9.5, 9.9); no such unjustified inference is attributed here to a particular printed proposition.

**Previously recorded:** earlier pinch-point normalization/conductor and codimension-two PSH branch models retain their independent statuses; this ID does not supersede them. Owner-excluded Demailly approximation, Bergman, weighted L², OT, multiscale and positivity-loss work stays **deferred-by-user**, not resolved.

**Coverage:** first selected §9.5.1/.5 plus cross-check §9.4.2/.3/.6/.10; zero entire mathematical-section certifications, inventory still 25 chapters / 747 numbered sections. No builds, tests, CI, publication, or production changes.
