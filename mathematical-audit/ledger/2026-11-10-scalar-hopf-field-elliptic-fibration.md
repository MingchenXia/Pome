# POME-HOPF-SCALAR-MEROMORPHIC-FIBRATION-001 — ledger (2026-11-10)

- **Status:** verified conditional deduction. **Severity:** low. **False theorem:** none. **Proof gap newly alleged:** none.
- **Target:** printed Theorem 23.3.3, source `demailly-complex-geometry:371996B7`, permanent `D81E3145A1B4`, `docs/sections/contracting-hopf-quotients/index.html` main blob `d09d9bac3785b78b557ff5178ad7a52b34b20dac` lines 8–21, 44–50. Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Statement proved:** for scalar \(qI\), \(0<|q|<1\), \(\mathcal M(X_q)=\mathbb C(z_1/z_2)\), and \(X_q\to\mathbb P^1\) is a principal elliptic \(E_q=\mathbb C^*/q^\mathbb Z\) bundle without a continuous section.
- **Exact proof:** homogeneous lowest Taylor terms of a Hartogs-extended invariant meromorphic germ, followed by principal-bundle local trivializations and the fundamental-group obstruction. [Full report](../reports/2026-11-10-scalar-hopf-meromorphic-field-and-elliptic-fibration.md).
- **Dependency:** Theorem 9.38.5 (source `demailly-complex-geometry:7716022D`, tag `F35BA7139EC4`, blob `fa09a923ef076a99d638d038020ddd3b884afaa7`, lines 89–111) supplies the **codimension-two meromorphic extension**, with complete transitive certification not claimed. This is a genuine internal theorem dependency; the general Remmert–Stein premise it cites remains unverified transitively here.
- **Duplicates:** previous Hopf meromorphic-character section-existence criterion, holomorphic tensor spectra and automorphism centralizers left unchanged; none determines this entire meromorphic function field or the sectionless principal bundle.
- **Proposed body correction:** none. Optional scalar Hopf corollary; never modify `main`/source/registry/tags via audit branch.
- **Affected themes:** §23.3, §9.38 extension, §20.7 divisor/Picard applications; no change to any certified theorem status.
- **Coverage:** §23.3 proof-level scalar specialization extended; §9.38.5 prerequisite read but not certified; +0 first numbered sections, +0 completed numbered sections; 25/747 ToC. Excluded Demailly/Bergman/weighted L2/OT/multiscale/positivity-loss programme stays **deferred-by-user**.
