# 2026-11-07 — small resolution and Cartier degrees on a threefold node

**Stable finding ID:** POME-NODE-SMALL-RESOLUTION-DEGREE-001.
**Severity:** low.
**Status:** verified conditional deduction (original Proposition 20.6.4 and Example 20.6.5 correct; NOT a false theorem or proposed unconditional full-section repair).
**Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Exact reading file and blob:** <code>docs/sections/analytic-cycles-and-cartier-cycles/index.html</code> — d4817ac64b1365bd967d42cd474fec169f992e28.
**Anchors:** physical lines 28–45 (Proposition 20.6.4; source demailly-complex-geometry:BD1D45B4, permanent AA96C35C8290), 46–75 (Example 20.6.5; source demailly-complex-geometry:E054C396, permanent 0C462992AB3A), and context 12–27 (Proposition 20.6.3, source 02B65FA7, permanent FD8966432506).

**Statement, hypotheses and mathematical determination.** On the ordinary analytic threefold node \(X=\{xy+zw=0\}\), the explicit projective small resolution of the column-image direction has smooth total space \(\mathrm{Tot}(\mathcal O_{\mathbb P^1}(-1)^{\oplus2})\), exceptional curve \(E=\mathbb P^1\) with normal bundle \(\mathcal O(-1)^{\oplus2}\), and no exceptional divisor. The strict transforms of the two Weil rulings \(A=(x,z)\), \(B=(x,w)\) have degrees \(+1,-1\) on E, while \(\mathrm{div}_Y(x)=\widetilde A+\widetilde B\). As no local Cartier divisor pulled back from the vertex can have a nonzero degree on the contracted curve, no nonzero multiple of A or B is Cartier at 0. Full affine charts, overlap transitions, the codimension-two argument, and line-bundle-degree justification appear in the [English proof](../reports/2026-11-07-node-small-resolution-cartier-degree.md).

**Prior finding reconciliation:** the non-torsion Cartier class was already established by POME-CYCLE-FOURRULING-CARTIER-001, so it is **not counted again as a newly discovered error or class-group computation**. New information is the explicit proper small resolution and its opposing intersection degrees, yielding a geometrically independent proof. Source statements remain correct.

**Proposed text amendment:** optional short geometric example after Example 20.6.5; no source, integrated body, canonical registry, permanent tag, or main modification. **Dependents:** §20.6.4–5 and Chapter 20's Cartier/b-divisor interpretation, not certified wholesale. **External inputs:** only elementary divisor/line-bundle correspondence and \(\deg\mathcal O_{\mathbb P^1}(m)=m\); no deep resolution theorem, L2, or regularization.

**Status boundaries:** no whole-section certification; preserve all previous statuses. Excluded Demailly approximation/regularization and its Bergman, weighted-L2, OT, multiscale, and positivity-loss completion programme remains **deferred-by-user**.
