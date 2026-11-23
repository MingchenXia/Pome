# 2026-11-23: resolved poles and blowup density endpoints

Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; audit branch `review/mathematical-audit`.

## POME-DISCONNECTEDNESS-AUDIT-CONVENTION-RETRACTION-001
- **Status:** verified correction / withdrawn audit false-positive. **No source theorem error**.
- **Precise overriding convention:** §1.1, `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, line 123: by default `X` is a **connected** compact complex manifold.
- **Withdrawn §15.22 allegation:** `POME-RESOLVED-POLES-DISCONNECTED-MASS-SCALAR-001`, Theorem 15.22.2 permanent `3B5397268E44`, blob `bec2abe4e9b361a37adbf668837da42726b6dcda`, lines 21–50. The disconnected `P^2 ⊔ P^2` example is **outside** the printed hypotheses.
- **Also retracted as claimed source errors:** `POME-SMOOTH-MA-DISCONNECTED-GLOBAL-SCALAR-001` (§14.2.1, permanent `F33DA8C9DF9F`), `POME-SMOOTH-MA-DISCONNECTED-UNIQUENESS-001` (§14.2.4, `366AA2E61158`), and `POME-SMOOTH-MA-DISCONNECTED-C0-ESTIMATE-001` (§14.3.5, `EEF74F1DEBB8`). Neither §14.2 nor §14.3 overrides the convention.
- **Consequence:** no source/body repair is warranted on these grounds; deep connected-case proof chains remain uncertified. Preserve prior audit text with explicit superseding classification.
- **Proof and verified anchors:** [report](../reports/2026-11-23-blowup-density-weak-endpoint-and-resolved-poles-connectedness.md).

## POME-BLOWUP-PUSHFORWARD-WEAK-LQ-ENDPOINT-001
- **Severity/status:** low / verified conditional deduction; not an original theorem error.
- **Anchor:** `docs/sections/equations-with-prescribed-singularities--minimal-singularities-on-blowups/index.html` blob `884c20eb0ab2b613129a84232e9b6688f3aba993`; Theorem 15.23.5 `66FFA0C36433`, displayed (15.23.7) `7E7FF8A6A54E`, physical 61–85; Theorem 15.23.10 `37D35D78F0C6`, physical 103–123.
- **Hypotheses:** blowup of codimension `r>=2` smooth center, smooth positive reference volumes, `f>=0` in upstairs `L^p`, `1<p<=infinity`; for tower, finite sequence of such blowups.
- **Result:** pushforward density belongs to weak `L^{q}`, `q=rp/((r-1)p+1)`, with homogeneous weak-norm estimate `<=C||f||_p`; for tower `R=product r_j`, exponent `q_R=Rp/((R-1)p+1)`.
- **Complete argument:** Jacobian gives base distortion weight `dist(y,Z)^{-2(r-1)}` in weak `L^{r/(r-1)}`, hence `pi_*mu(A)<=C nu(A)^{1/r}`; upstairs Hölder on `{F>t}` yields `t nu{F>t}^{1/q}<=C||f||_p`. The logarithmic power model `f~t^{-2/p}(log(e/t))^{-gamma}`, `1/p<gamma<=1/q`, disproves strong `L^q` universally; `f=1` does so for `p=infinity`. Towers compose the set-distortion exponents.
- **Correction status:** optional internal remark only; no proof deficiency asserted for source theorem, and no direct source edit.
- **Affected dependents:** integrability thresholds for the normalized target Hermitian MA solver §§14.19.2, 15.5.1 when applied after blowup. These inputs themselves not transitive-certified.
- **Details:** [full proof](../reports/2026-11-23-blowup-density-weak-endpoint-and-resolved-poles-connectedness.md).

All Demailly/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**.
