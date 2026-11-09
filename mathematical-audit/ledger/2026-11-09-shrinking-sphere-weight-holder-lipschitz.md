# Ledger: `POME-SPHERE-WEIGHT-HOLDER-LIPSCHITZ-001` (2026-11-09)

- **Status:** verified conditional deduction (low); **printed result is correct**.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html` blob `354dfdf5224fac8896103ec09aa5936351021914`.
- **Source anchors:** equation 15.26.1 `non-kahler-pluripotential-theory:4C0F3404` / `938F2C76C18A` (12–15); Proposition 15.26.2 `non-kahler-pluripotential-theory:92442012` / `8F3C95237950` (26–67); Corollary 15.26.3 `BBB972F3` / `AB5B44EC4BDD` (69–82); Theorem 15.26.4 `7EBE40DC` / `6076D6F3256C` (84–102). Lemma 5.27.25 `961DE4FB` / `3242D4BA1F13` is a **cited internal dependency**, not newly certified.
- **Hypotheses:** compact complex `n>=2`, any smooth Hermitian `h`, fixed chart/cutoff and radii `r_j=r_0 2^{-j}`, arbitrary `s>0`.
- **Result:** density weights `r_j^(ns)`; uniform positive background `h+dd^c u_s>=h/2` and `MA_h(u_s)>=(S_s/Z_s^n)rho_s`; global `C^{0,s}` for `s<1` and Lipschitz for `s>=1`; exact `r_N^s` radial increment shows sharpness for `s<1`; positive one-sided radial derivative jump forbids `C^1` at each sphere.
- **Proof:** [source-pinned complete algebra/radial argument](../reports/2026-11-09-shrinking-sphere-weight-holder-lipschitz.md).
- **Proposed correction:** optional additional Remark after Proposition 15.26.2, **not** a change to the printed theorem.
- **Dependents:** §§15.26.3–4 via existing subsolution/existence theorems (conditional); no end-to-end theorem verification.
- **Coverage delta:** §15.26 newly investigated parameters; prior selected §15.26 already exists, so 0 first visits and 0 complete section certifications. §5.27.25 normalization context only.
- **Excluded scope:** Demailly regularization and dedicated Bergman, L², OT, multiscale atlas, positivity-loss work remains `deferred-by-user`, not resolved.
