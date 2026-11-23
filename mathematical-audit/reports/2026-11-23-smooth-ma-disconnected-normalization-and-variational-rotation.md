# Smooth Hermitian Monge–Ampère equations: componentwise normalization and variational comparison

**Date:** 2026-11-23. **Baseline main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **Scope:** full current reading-edition §§14.1–14.4 and 14.6–14.7; opening/structural checks in §14.5 only; selected §§17.5.2–17.5.11 and the beginning of §17.5.12, not the entire §17.5. Historical first-visit status remains unreconciled.

## Core observation: connectedness is not a global convention

The actual integrated convention in docs/sections/conventions/index.html, lines 11–23, specifies that a *domain* is connected but merely says that a *complex manifold* is paracompact. It does not impose connectedness on compact complex manifolds. The chapter-opening docs/sections/smooth-monge-ampere-equations/index.html, lines 7–17, introduces a Hermitian form on X and a positive volume form without a connectedness qualification. A compact disjoint union of two compact connected complex manifolds therefore satisfies these explicit premises. The three consequences below concern different printed claims and are not a re-registration of the earlier §11.26/§11.27 connectedness findings.

### POME-SMOOTH-MA-DISCONNECTED-GLOBAL-SCALAR-001
**Classification:** medium / **confirmed error in the theorem as stated**, not a proof gap in the connected version.

**Target:** docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html, source label non-kahler-pluripotential-theory:3EE16849; permanent tag F33DA8C9DF9F; **Theorem 14.2.1**, lines 10–15. Background equation: docs/sections/smooth-monge-ampere-equations/index.html, Eq. 14.1.1, source tag 2BED92DC / permanent C5FA7F078BB6, lines 7–14. Main blobs 3f96829e18befc845df40c6d4bca13c977ae9cea and e35eb98bdc1c62c4938155964945f4d6495b4ee4.

The printed theorem promises a single scalar b and an everywhere normalized smooth solution u for every smooth F. Take X = X_1 ⊔ X_2, where both X_i are copies of the Riemann sphere with the same smooth area form ω_i, let dV = ω, and set F|X_1 = 0 and F|X_2 = log 2. In complex dimension one every Hermitian ω is closed. If
\[
\omega+dd^c u=e^{F+b}\omega,
\]
integration on each closed component separately gives
\[
\int_{X_i}\omega=e^{F|_{X_i}+b}\int_{X_i}\omega,
\]
so e^b = 1 from X_1 and e^b = 1/2 from X_2, a contradiction. No choice of u, normalized or otherwise, exists. The dimension-one paragraph at line 15 integrates over X as a whole, whereas the Poisson compatibility condition must hold on *each* connected component.

**Proposed correction:** require connected X in this theorem and in its chapter setup. Alternatively, formulate independent componentwise equations with a distinct normalization scalar b_i on each component; a common scalar is possible only under additional compatibility conditions. This does not refute Tosatti–Weinkove under the usual connected compact setting. **Affected dependent arguments:** §14.2.1's dimension-one justification, §14.4.1's global smooth solution map, §14.6's continuity-method conclusion, and applications that presume a single scalar for arbitrary disconnected data.

### POME-SMOOTH-MA-DISCONNECTED-UNIQUENESS-001
**Classification:** low / **confirmed error in an unqualified clause**; the scalar-equality clause survives.

**Target:** same §14.2 HTML, **Proposition 14.2.4**, source label non-kahler-pluripotential-theory:E26E18C6; permanent tag 366AA2E61158; line 50, proof lines 55–64; blob 3f96829e18befc845df40c6d4bca13c977ae9cea.

Take the same disconnected X, F ≡ 0, dV = ω, u ≡ 0, and v = 0 on X_1 but v = −1 on X_2. Both are smooth, strictly admissible, solve the same equation with b=c=0, and even satisfy sup_X u = sup_X v = 0. Nevertheless, u−v is zero on X_1 and one on X_2; it is not constant on X. The final use of the strong maximum principle in line 64 establishes only that the difference is **constant on each connected component**. The preceding maximum/minimum comparison still establishes b=c, even without connectedness.

**Proposed correction:** retain b=c; replace “u−v is constant” with “u−v is locally constant (constant on each connected component)” or assume X connected. Do not identify distinct solutions merely by the one global sup-normalization on a disconnected space. **Dependents:** uniqueness assertion at §14.2.1 and the final sentence of §14.6.

### POME-SMOOTH-MA-DISCONNECTED-C0-ESTIMATE-001
**Classification:** medium / **confirmed error in the displayed uniform estimate**, not in the componentwise weighted gradient inequality.

**Target:** docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html, **Theorem 14.3.5**, source label non-kahler-pluripotential-theory:C569075E; permanent tag EEF74F1DEBB8; lines 108–112, proof lines 117–149. Main blob f774b702e65736ce8a23847dbb3409c6b31b0211.

On the same disjoint union, for every M>0 define u_M|X_1=0 and u_M|X_2=−M. Then
\[
\sup_Xu_M=0,\qquad \omega+dd^cu_M=\omega>0,\qquad
(\omega+dd^cu_M)^n=\omega^n\le 1\cdot\omega^n,
\]
but \(\|u_M\|_\infty=M\to\infty\). Thus the claimed constant C_1 depending only on fixed ω and Λ=1 cannot exist. The weighted integration and Moser iteration give a lower-bound *relative to each component's additive constant*, not to an unrelated component's global supremum. The cited normalized L¹ compactness theorem 5.25.2 (line 143) cannot supply a global uniform L¹ bound for this disconnected family.

**Proposed correction:** require connected X, or require an independent additive normalization on each connected component, e.g. sup_{X_i} u=0. For compact disconnected X there are finitely many components; apply the connected estimate componentwise and take a maximum of finitely many bounds. **Dependents:** §14.6 line 26 (closedness through C⁰ and elliptic estimates), and any subsequent uniform estimates relying on this exact version.

## Further direct checks, not additional registered findings

* §14.2.2, lines 18–29: the extremum bound on b is valid on disconnected X as a necessary bound when a solution happens to exist. §14.2.3, lines 33–46: the closed-background *whole-X* integral identity is necessary but is not a substitute for componentwise Poisson compatibility.
* §14.3.1–2, lines 10–103: inspected the diagonal Young inequality, dT = n Σ η^k ω^{n-k−2}∧dω, the Stokes sign at line 57, the δ=K/p absorption, and the finite recurrence for the weighted mixed masses. The displayed algebra is consistent under the stated positivity and torsion bounds; no complete upstream analytic proof-chain certificate is claimed.
* §14.4.1, lines 7–39: a single ∫_X u dV = 0 condition does **not** remove the componentwise-constant kernel on disconnected X. At a solvable disconnected reference point, the derivative (v,a) ↦ L_u v−a has a kernel of dimension at least number-of-components minus one. Moreover each component gives a separate adjoint-mean compatibility condition, while only one scalar a is available. Thus the implicit-function step needs connected X or a componentwise re-formulation. This is an affected consequence of the same missing setup, not counted again as a novel counterexample.
* §14.6, lines 7–27: the open/closed continuation explicitly relies on §14.4.1 and §14.3.5; the failure is structural for disconnected X. §14.7, lines 7–61: importantly, the **different exponential equation** with λ>0 has a negative zeroth-order term and does not have this additive-shift defect. Its comparison proof works componentwise; do **not** propagate the counterexample to §14.7.2.
* §14.5: only the introduction, statement of Lemma 14.5.1 and the trace-estimate setup were selected for dependency orientation; no complete direct review is claimed.
* §17.5: reviewed lines 7–215 (definitions and the first sequence of variational results), including the envelope tangent sandwich in Proposition 17.5.4 (lines 46–67), the maximizer criterion (lines 72–97), and the bounded-density existence route (lines 102–121). These rely on their own singularity/mass hypotheses; no assertion that the entire §17.5 or its transitive inputs have been certified. In particular no part of Demailly's excluded regularization programme was investigated.

## Verification status and scope boundaries

There are **three distinct confirmed errors in statements as printed** (one existence, one constant-vs-locally-constant uniqueness clause, one C⁰ estimate), with a fourth downstream implicit-function issue explained but not separately counted. The connected-case proofs are not disproved. No original integrated content, source, tag, registry, canonicalization, or website was edited. No project tests, compilation, CI or browser rendering were run, and no complete transitive mathematical proof chain was certified. The user-excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion subjects remain **deferred-by-user**, neither resolved nor certified.
