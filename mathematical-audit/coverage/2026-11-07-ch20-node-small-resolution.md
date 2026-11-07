# 2026-11-07 — Chapter 20, new small-resolution geometry at §20.6.5

**Current production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Actual current ToC inventory:** 25 chapters / 747 numbered sections / zero mathematically certified entire sections.
**Previously sampled section:** §20.6, analytic cycles and Cartier cycles; **not a first visit**.

**Integrated text actually consulted:** <code>docs/sections/analytic-cycles-and-cartier-cycles/index.html</code> (main blob d4817ac64b1365bd967d42cd474fec169f992e28):
- lines **12–27**: Proposition 20.6.3 (source demailly-complex-geometry:02B65FA7, permanent FD8966432506), cycle sheaf and global/local-branch conventions — context only.
- lines **28–45**: Proposition 20.6.4 (source demailly-complex-geometry:BD1D45B4, permanent AA96C35C8290), Cartier cycles defined by local meromorphic divisors — precise convention read and used, not an entire proof certification.
- lines **46–75**: Example 20.6.5 (source demailly-complex-geometry:E054C396, permanent 0C462992AB3A), quadratic node, its rank-one cover, non-Cartier ruling and existing proof — mathematical hypothesis, conclusion, and algebraic argument checked against the new geometry.

**Substantive new work:** a complete explicit chart construction of the proper small resolution \(Y=\mathrm{Tot}(\mathcal O(-1)^{\oplus2})\to X\); strict transforms of A=(x,z) and B=(x,w); exceptional normal bundle and exact line-bundle degrees \(+1\) and \(-1\) on \(E\); independent degree obstruction for every nonzero Cartier multiple. No reliance on Hironaka or the excluded regularization programme. See [full report](../reports/2026-11-07-node-small-resolution-cartier-degree.md) and [status ledger](../ledger/2026-11-07-node-small-resolution-cartier-degree.md).

**Not new / not certified:** the older POME-CYCLE-FOURRULING-CARTIER-001 already detects the infinite cyclic subgroup of supported classes; no repeat claim. No full §20.6, complete local analytic divisor-class group, other modification chain, Chapter 20, project build, CI, formalization, or website certification. All earlier findings keep their prior classifications; Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work stays **deferred-by-user**.
