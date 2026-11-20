# 2026-11-20 — Gauduchon affine deficit and equation display duplication

## POME-GAUD-ROOT-AFFINE-GREEN-DEFECT-001
**Status:** verified conditional deduction. **Severity:** low. **Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Not a false printed theorem or proof gap.**
**Integrated anchor:** §12.4 Proposition 12.4.1, source non-kahler-pluripotential-theory:C55D0CC4 / permanent 67FDDBC10DBD, lines 23–63, blob 4992f82c6e84918ead47a972eab7e3238a147655. §12.3.1 source 6B1A74F2 / permanent 2220E0C47510, lines 11–29, blob d94e3fc055b0642a86495c27ad8f5af6f24f17d1.
**Claim and justification:** For the affine segment of strictly positive-background classes \(\theta_s\), with smooth Monge–Ampère solution \(\Omega_s\) and adjoint probability \(\nu_s\), put \(Q_s=(\lambda_s/n)\int\|\Omega_s^{-1}(\chi+dd^c\dot u_s)-(\lambda_s'/\lambda_s)I\|^2\,d\nu_s\). Then \(-\lambda_s''=Q_s\), and the exact Jensen gap is \(\int_0^1K(t,s)Q_sds\), with \(K(t,s)=\min(t,s)(1-\max(t,s))\). In particular it is at least \(q_*t(1-t)/2\); \(q_*=\min Q_s>0\) if the endpoints are not positive-projectively \(dd^c\)-equivalent. Full proof, rigidity and quantifiers in [report](../reports/2026-11-20-gauduchon-affine-concavity-exact-green-defect.md). **Upstream conditional:** smooth MA family and adjoint probability; complete transitive proofs not re-certified.
**Proposed correction:** Optional new quantitative corollary after §12.4.1, not a source change. **Affected dependents:** affine variation/stability statements; no existing theorem invalidated.

## POME-GAUD-SECOND-VARIATION-VISIBLE-DUPLICATE-001
**Status:** genuine duplication (visible reading equation only). **Severity:** low. **Main SHA:** same.
**Integrated anchor:** same §12.4 blob. One formula (12.4.3) appears at lines 24–27 (source non-kahler-pluripotential-theory:86F8F24F / permanent E544AEC2FDDB) and again at physical line 79 (source 3217D224 / permanent 88A03DC67E97). These duplicate exactly the same differential identity. **Proposed patch:** canonical single visible equation, preserving both source labels, permanent tags, external links and historical attribution. **Affected dependents:** reading display, equation links, numbering; mathematical truth of 12.4.1 and 12.4.4 unchanged. No production patch applied.

**Coverage:** whole §§12.3 (lines 7–59), 12.4 (7–79), 12.5 (7–48); selected §12.2 and §12.6 context; +0 complete upstream chains; no historical first-visit assertion. The Demailly-related excluded programmes remain **deferred-by-user**.
