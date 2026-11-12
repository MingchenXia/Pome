# 2026-11-12 — classified mathematical audit ledger

## POME-MA-DISCONNECTED-COMPONENT-SCALAR-001

- **Severity / status:** **high / confirmed error** (omitted connectedness in the integrated Chapter 14 scope). This is an actual counterexample to the statements *without* connectedness, not a claimed counterexample to the intended connected case.
- **Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit.
- **Integrated anchors:** §14.1 line 7 and equation 14.1.1 lines 9–14, original/permanent `non-kahler-pluripotential-theory:2BED92DC/C5FA7F078BB6`; §14.2 Theorem 14.2.1 lines 10–15 `:3EE16849/F33DA8C9DF9F`; Proposition 14.2.4 lines 49–65 `:E26E18C6/366AA2E61158`; §14.3 Theorem 14.3.5 lines 107–149 `:C569075E/EEF74F1DEBB8`; §14.4 Proposition 14.4.1 lines 19–38 `:E0953F19/2AD3CD874EA4`; §14.6 proof lines 9–26. Exact paths and blob SHA are in the linked report.
- **Counterexample:** \(X=(\mathbb P^1)^n\sqcup(\mathbb P^1)^n\), Kähler \(\omega\), \(dV=\omega^n\); \(F=(0,\log2)\) makes a single \(b\) impossible by componentwise Stokes. With \(F=0\), \(u_A=(0,-A)\), \(b=0\) contradict uniqueness and uniform \(C^0\) bounds. Mean-zero, nonzero componentwise constants give kernel of the asserted linear inverse.
- **Correction proposed, not applied:** explicitly assume compact **connected** \(X\) throughout smooth Chapter 14, or use componentwise scalars and normalizations in a disconnected version.
- **Dependents:** 14.2.1, 14.2.4, 14.3.5, 14.4.1, proof §14.6; inspect later scalar variation separately.
- **No full proof certification:** intended connected-manifold theorem and other analytic dependencies have not been newly certified.
- **Report:** [2026-11-12 disconnected component counterexamples](../reports/2026-11-12-disconnected-hermitian-ma-normalization-counterexample.md).
- **Actual coverage:** [2026-11-12 Chapter 14 selected review](../coverage/2026-11-12-ch14-disconnected-normalization.md).

### Deferred-by-user

The previously recorded Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**. No prior unresolved or deferred findings are changed to resolved or certified.
