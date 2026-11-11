# POME-HIRZ-EXT-SLOPE-JUMP-001 — classified finding

- Date: 2026-11-11
- Severity: low
- Status: **verified conditional deduction** (not a confirmed error, not a full-section certification).
- Reviewed production main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Integrated reading file: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--stable-extensions-approaching-the-split-comparison-bundle/index.html, blob 03559e82ef17c97d04258775312d994ec217e376; Proposition 11.14.1, source non-kahler-pluripotential-theory:D386B065, permanent A195B6162A49, lines 25–86.
- Internal hypothesis source: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--ample-comparison-quotients-on-hirzebruch-surfaces/index.html, blob 6d836a2ed19f76c26311025602fb44a56713e390; Lemma 11.13.1, source non-kahler-pluripotential-theory:9A9AA541, permanent 8FE2AABC7334, lines 26–51.
- Hypotheses: Hirzebruch surface F_e, e>=0; L_1=O(5S-f), L_2=O(-S+(12e+5)f), P=4S+(12e+3)f; nonzero extension alpha in W=Ext^1(L_2,L_1), dim W=105e+35.
- Exact new result: the stability margin mu_P(V_alpha)-sup_{rank-one M subset V_alpha}mu_P(M) is **1** exactly when some ruling fiber F_a has vanishing pullback of alpha under L_2(-F_a) -> L_2; otherwise it is **3**. Each such pullback kernel is 7-dimensional. Their projectivized union is closed irreducible dimension 7, codimension 105e+27. Distinct kernels meet only at zero. The split endpoint has margin -3.
- Reason: rank-one double-dual reduction; any injection M -> L_2 has effective zero divisor D with mu(M)=mu(V)+3-D.P. Apart from the excluded e=0 class S, only D=f can have D.P<6. The obstruction is the multiplier map H^1(F) -> H^1(F(f)); seven ruling summands each contribute a one-dimensional kernel, identified by Serre duality with distinct point evaluations.
- Proposed correction: **none** to the printed mathematical statements; optional quantitative remark after Proposition 11.14.1, not applied.
- Affected dependents: Proposition 11.14.3 and Theorem 11.15.5 (the latter's Walter prioritary-stack input is still explicitly external/unverified).
- No duplication with earlier §11.14 stability existence audit: the **exact margin 1/3 dichotomy and the codimension of its jumping locus** are new.
- Entire English proof: [report](../reports/2026-11-11-hirzebruch-nonsplit-extension-slope-gap-jump.md).
- Coverage: previously partially reviewed §§11.13–11.14; no new first numbered section and no fully certified section; [exact coverage](../coverage/2026-11-11-ch11-hirzebruch-extension-slope-jump.md).
- User-excluded Demailly approximation/regularization, Bergman/L2/OT/multiscale/positivity-loss work stays deferred-by-user, not resolved.
