# 2026-11-21: model-envelope one-mixture mass test and section-growth external input

Main SHA: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Full current §17.6 blob \`addc238e2dc806ff14a69fa8c8e5bdf46da448f2\`, §19.9 blob \`83557f0e15275253661fe679c75407e6636d497c\`. [Complete proof and exact anchors](../reports/2026-11-21-one-mixture-envelope-rigidity-and-okounkov-growth.md).

| Finding ID | Severity | Status | Evidence and disposition | Affected dependents |
| --- | --- | --- | --- | --- |
| POME-ENVELOPE-ONE-MIXTURE-MASS-RIGIDITY-001 | low | **verified conditional deduction** | §§17.6.1/17.6.5 + 13.8.8: for ordered \(u\preceq v\), equality of one \(M_u(t_0)\), \(M_v(t_0)\), \(0<t_0<1\), implies equality of all mixed masses by positive-coefficient polarization; hence equality of \(P_\theta[u]\), \(P_\theta[v]\). Conversely envelope equality gives all mass equalities. Distinct poles on \(\mathbb P^1\) disprove the unordered variant. No printed error. | §17.6 singularity ceilings; §16.21–16.22 model envelopes. Optional corollary proposed, no body edit. |
| POME-OKOUNKOV-MOISHEZON-EXTERNAL-INPUT-001 | low | **external dependency** | §19.9.13 lines 303–313, §19.9.17 lines 365–380: projective-modification form of Moishezon theorem used to infer bounded mass. Attribution in §25.9 is not a self-contained proof; no claim of incorrectness, no substitute proof supplied. | §19.9.13, §19.9.17. Retain historical attribution and flag the genuine theorem input for later independent proof audit. |
| USER-EXCLUDED-DEMAILLY-PROGRAMME (existing deferred category, not new discovery) | n/a | **deferred-by-user** | Dedicated regularization, Bergman, L2, OT, multiscale-atlas and positivity-loss proof completion intentionally untouched; neither resolved nor certified. | Any theorem explicitly citing these remains dependency-conditional. |

No resolved original mathematical error, no new confirmed false printed theorem, and no independently certified full prerequisite chain in this pass. No tests/build/CI/site or main/source changes.
