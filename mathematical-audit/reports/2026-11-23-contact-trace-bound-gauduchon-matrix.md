# Sharp trace-product domination for contact Monge–Ampère measures; adjoint and Gauduchon matrix rotation

Date: 2026-11-23. Main reviewed: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit branch: review/mathematical-audit (existing history preserved).

## Exact reading-edition objects and scope

1. Entire current §16.14, docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--obstacles-with-bounded-metric-laplacian/index.html, Git blob e9ce0caf7bd8b123062d9cb6fffd49fdfd0d5ffb, mathematical physical lines 5–281. In particular Proposition 16.14.6, source foundations-of-pluripotential-theory:7A1567B2, permanent CB0B256B92D7, lines 122–154; Corollary 16.14.11, source foundations-of-pluripotential-theory:E96D4CC3, permanent E3B684F226D1, lines 264–279. Examined the logarithmic trace-only example, two-cutoff W^(2,2) argument, local contact Hessian identification, frozen-coefficient L^p estimate, and global weak-form products.
2. Entire current §14.12, docs/sections/smooth-monge-ampere-equations--the-adjoint-equation-for-gauduchon-volume/index.html, Git blob de0b040ee22f128bf16c89048267075a01f15e66, mathematical lines 5–110. Proposition 14.12.1 (non-kahler-pluripotential-theory:1A082A94; permanent 706EB82AB6A2; lines 10–44) and Proposition 14.12.3 (non-kahler-pluripotential-theory:DAC00F18; permanent 029A1D30A55E; lines 60–103): determinant-root derivative, positivity of principal symbol, Fredholm/adjoint kernel, and the torsion-corrected formal adjoint.
3. Entire current §14.13, docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html, Git blob 6e1faedde219b856c0bf5ecaf566403ae999772e, mathematical lines 7–180. Lemma 14.13.2 (non-kahler-pluripotential-theory:57B6169B, permanent 6168D5D4EF96, lines 38–106); Lemma 14.13.5 (permanent DBC2334A4FC0, lines 108–151); Eq. 14.13.8 (permanent 677E6AB0568A, lines 159–171). Rechecked the torsion-index exclusions, P_gamma matrix normalization, coefficient inequalities, and log-det concavity.
4. Previously whole-reviewed §§3.9, 17.2, 20.7 and supporting §20.6 were revisited to compare ambient hypotheses or proof mechanisms. These are REPEATS and do not enlarge the first-visit count. The non-Cartier quadric in §20.6 is not a new issue in §20.7: the existing audit treats the latter's local-factorial argument on a manifold.

## New finding: POME-CONTACT-MIXED-MA-SHARP-TRACE-PRODUCT-001

Status: **verified conditional deduction**; severity: **low**. This is an additional sharp quantitative consequence, **not** a claim that Proposition 16.14.6 or Corollary 16.14.11 is wrong.

Let X be a complex n-dimensional Kähler manifold with fixed Kähler form omega. On an open set U let theta_j be closed smooth real (1,1)-forms and u_j continuous theta_j-psh functions with locally bounded distributional metric Laplacian L u_j. Put T_j=theta_j+dd^c u_j and tau_j=tr_omega T_j=tr_omega theta_j-(L u_j)/(4 pi). Each tau_j is an almost-everywhere nonnegative locally bounded function. Then, as positive measures on U,

\[
 0\ \le\ T_1\wedge\cdots\wedge T_n\
 \le\ \frac{1}{n!}\prod_{j=1}^n\tau_j\,\omega^n. \tag{A}
\]

If f_j are real Borel W^(2,1)_loc obstacles and E is the intersection of the contact sets {u_j=f_j}, then

\[
 0\le {\bf1}_E\,T_1\wedge\cdots\wedge T_n
 \le \frac{{\bf1}_E}{n!}\prod_{j=1}^n\tau_j\,\omega^n. \tag{B}
\]

The same right-hand side on E may use the traces of the weak Hessian forms theta_j+dd^c f_j, which equal those of T_j almost everywhere on E by the contact-set Hessian identity. Do not infer any positivity of the obstacle forms away from E. The factor 1/n! in (A) and (B) is optimal even for smooth potentials and compact flat tori.

### Complete pointwise algebraic proof (conditional only on the stated Pome contact-density input)

On a coordinate ball write omega=(i/(2 pi)) sum h_(a bar b) dz_a wedge dbar z_b, H=(h_(a bar b)) positive definite, and T_j=(i/(2 pi)) sum (A_j)_(a bar b) dz_a wedge dbar z_b. Proposition 16.14.6 proves A_j are positive semidefinite and essentially bounded, and its mixed Bedford–Taylor product is the almost-everywhere determinant density. Define C_j=H^(-1/2) A_j H^(-1/2). These are positive semidefinite, with tr C_j=tau_j, and invariance of mixed discriminants under simultaneous congruence gives

\[
 T_1\wedge\cdots\wedge T_n=D(C_1,\ldots,C_n)\,\omega^n.
\]

For rank-one matrices C_j=v_j v_j^*, the coefficient of t_1 ... t_n in det(sum t_j C_j) is |det[v_1,...,v_n]|^2. By the definition det(sum t_j C_j)=sum_(i_1,...,i_n) t_(i_1)...t_(i_n) D(C_(i_1),...,C_(i_n)), this coefficient is n! D(C_1,...,C_n). Hadamard's determinant inequality yields

\[
 0\le D(v_1v_1^*,...,v_nv_n^*)
 =\frac{|\det[v_1,\ldots,v_n]|^2}{n!}
 \le\frac{\prod_j\|v_j\|^2}{n!}.
\]

For general positive semidefinite C_j, expand each in a finite sum of positive rank-one matrices using the spectral theorem. The mixed discriminant is multilinear and all coefficients in that expansion are nonnegative; summing the rank-one bounds yields

\[
 0\le D(C_1,...,C_n)\le \frac1{n!}\prod_j\operatorname{tr}C_j.
\]

This proves (A) on every coordinate ball, hence globally. Multiply by the Borel indicator of E and use the almost-everywhere equality of the weak Hessians on E from Proposition 16.14.6 to obtain (B).

Sharpness: on the product of n flat elliptic curves, take omega=sum_j theta_j with theta_j=(i/(2 pi))dz_j wedge dbar z_j, u_j=f_j=0 and E=X. In the omega-unitary frame C_j=e_j e_j^*, so tau_j=1 and T_1 wedge ... wedge T_n=omega^n/n!. Equality holds throughout; no smaller universal coefficient works. For n=1 equality is immediate.

Hypothesis/dependency boundary: this verifies the finite-dimensional determinant argument and its deduction from the printed mixed-product density. The full preceding Bedford–Taylor/contact Sobolev chain (Proposition 7.13.4, Lemma 16.14.4, the metric Laplacian identities in §10.2, and local smoothing and elliptic inversion) has NOT been independently certified transitively. No regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme was entered.

Proposed improvement: optionally add the sharp estimate and torus equality model after Proposition 16.14.6 in a separately reviewable text change; no source or reading-edition patch is made by this audit. Dependents potentially benefiting: §16.14.11 and later §16.15 obstacle/contact measure comparisons. The estimate is local, so it neither supplies new existence theorems nor removes their assumptions.

## Existing findings checked but NOT re-registered

The original legacy display label 9.29 on the full Eq. 14.13.3 (physical lines 40–43) and a separately addressable truncated nested-alignment chip (source non-kahler-pluripotential-theory:8A591D0B, permanent A6EC7DDEACFB, physical line 180) were reobserved. They are **already recorded** in the 2026-10-24 POME-GAUD-ALIGN-SPLIT-001 integration finding. Their correct repair should preserve both permanent tags while attaching the orphan tag to the complete canonical display; neither is counted as a new defect. The complete torsion formula and matrix inequalities have not been shown false. Prior 2026-11-15 effective-coercivity work is likewise not relogged.

## Coverage, limitations, and repository operations

This session directly reread three entire current integrated mathematical sections (§§14.12, 14.13, 16.14); the whole reading is a new CURRENT checkpoint, not proof of a first-ever historical visit. Other sections mentioned above are contextual repeats. New findings: 1 verified conditional deduction; newly confirmed printed mathematical errors: 0; new presentation findings: 0 (old split merely reconfirmed); complete transitive upstream proof-chain certificates: 0. The 747-section matrix remains a ledger of actual per-section coverage, NOT a statement that all 747 sections are verified.

Only English mathematical-audit Markdown is proposed for review/mathematical-audit. No builds, tests, GitHub Actions, publication, main/source/body/registry changes, permanent tag deletion, or PR merge have been performed. Every specified excluded research programme remains **deferred-by-user**, neither resolved nor certified.
