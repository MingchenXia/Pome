# Classified mathematical audit ledger — 2026-11-14

## POME-NPP-APOLLONIUS-MAX-TRANSPORT-001

- **Classification:** verified conditional deduction; **severity:** low.
- **False theorem?** No. **Proof gap?** None newly established in the checked printed statements. **Repair?** No repair of a false result claimed.
- **Pin:** production main b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated source anchors:** §5.24.1 (non-kahler-pluripotential-theory:8EAEF1E9 / 729BA86BCC7C, lines 10–25); §10.6.7 (foundations-of-pluripotential-theory:E51945FB / 4CE1D9D7D803, lines 108–115); §13.2.4 (foundations-of-pluripotential-theory:9D8E4DD8 / D79952D7E272, lines 57–63); §13.7.5/.6/.8 (foundations-of-pluripotential-theory:AB4EBE3B / 67C4F7EC316E, lines 106–134; :D5678E03 / ACAEA8D8BE87, lines 138–140; :8CF7A9C6 / 4B60F7F33590, lines 147–171).
- **Hypotheses and exact verification:** distinct finite a,b on P1, normalized FS class, v_c=max(u_a,u_b+c); both input point currents have NPP mass zero, whereas the bounded max has NPP mass one. Full Apollonius/Möbius measure, W1 integrals, exact W1 ratio and two endpoint coefficients proved in the dated report.
- **Dependency boundary:** Uses selected printed monotone-capacity proposition as conditional upstream input; no independent chain certification. Hironaka, regularization, Bergman, L2, OT, gluing and positivity-loss programmes are not used.
- **Distinction from previous work:** previously verified unit-circle max curvature POME-FS-MAX-CIRCLE-CURVATURE-001 and single-pole truncation transport POME-NPP-CP1-TRUNCATION-SHELL-W1-001 remain unchanged, not counted again.
- **Proposed correction/addition:** optional explanatory worked example beside §13.7.6; no incorrect printed theorem to change.
- **Affected dependents:** interpretation of max stability §5.24, FS max metrics §10.6, pole exclusion §13.2, and mass-drop hypothesis §13.7. No broader results certified.
- **Status ledger:** resolved = the independent model computation only; unresolved = upstream general capacity/NPP proof-chain verification; deferred-by-user = Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss completion.
- **Source:** [full English mathematical proof](../reports/2026-11-14-two-pole-apollonius-maximum-transport.md); [exact coverage](../coverage/2026-11-14-ch5-ch10-ch13-two-pole-apollonius.md).
