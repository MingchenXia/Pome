# Classified finding — 2026-11-05 — atomic endpoint and long-Perron cutoff

**Stable ID:** POME-GEO-ATOMIC-LONG-PERRON-CUTOFF-001

| Field | Audit record |
| --- | --- |
| Reviewed production main | b6933b772f41b45918f7e25ed1afbbb1fd892272 |
| Status | **verified conditional deduction**; neither confirmed error nor complete repair |
| Severity | **low** |
| Main body | docs/sections/relative-energy-and-perron-segments--extremal-slopes-and-long-perron-segments/index.html (blob 023e78b3da0fd8f33d39177dba02f410b10f376c), lines **11–25, 34–72** |
| Anchored statements | Proposition **17.9.1**: foundations-of-pluripotential-theory:58E4D688 / permanent **0583958ACA6D**; Proposition **17.9.2**: foundations-of-pluripotential-theory:2B4D191D / permanent **A6533ED6CC68** |
| Hypotheses | $X=\mathbb P^1$, $\theta=\omega_{\rm FS}$, $\phi=0$, $u=\log(|z|^2/(1+|z|^2))\le0$ ($\omega+dd^cu=\delta_0$), $T>0$, $0\le s\le T$ |
| Verified new calculation | $R_s=\log((e^{-s}+|z|^2)/(1+|z|^2))$ is the explicit long-Perron limit; $R_s-s\log(2-e^{-T})/T\le L_s^{u,T}\le R_s$; exact extrema $-s,0$; exact cutoff energy $E(u_T)=-T/2-(1-e^{-T})/2$ |
| Conditional dependent | Theorem 17.8.3 (source foundations-of-pluripotential-theory:907171A2 / tag **678A18D6D406**) gives $E(L_s^{u,T})=-s/2-s(1-e^{-T})/(2T)$; upstream general energy-affinity proof is not certified |
| Other crosschecks | §17.7.8–9 endpoint comparison/affine shifts; §17.17.11 smooth reference ray, with previous work not counted anew |
| Proposed change | Optional explicit example after 17.9.2; no source/registry/permanent-tag edit authorized in audit |
| Affected dependents | Long Perron singularity-type construction, extremal endpoint slopes, bounded energy-affinity consistency |
| Scope limit | Selected model/proof arithmetic only; 25 chapters / 747 numbered sections / zero full mathematical-section certificates |

[Full self-contained model and conditional energy argument](../reports/2026-11-05-atomic-long-perron-uniform-cutoff-and-energy.md). Older findings are unchanged. All user-excluded regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved.