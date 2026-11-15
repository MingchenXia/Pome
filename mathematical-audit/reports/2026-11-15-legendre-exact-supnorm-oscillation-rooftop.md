# Exact Legendre sup-norm/oscillation isometry and finite rooftop stability

**2026-11-15; reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Finding ID:** \`POME-CONVEX-DUAL-LINF-OSC-ROOFTOP-001\`. **Severity/status:** low / **verified conditional deduction**. No original theorem error or completed full-chain certification.

## Anchors in the current integrated reading edition

- \`docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html\`, main blob \`347fa1f0fc35c13b1d1c45193ab997ed456966e4\`: Theorem 21.3.2, source \`foundations-of-pluripotential-theory:DD2DB654\`, permanent \`011FA81B0000\`, physical lines 24–58 (the actual Fenchel–Moreau proof); Proposition 21.3.3(2), source \`:E93FCB56\`, permanent \`53A9D470F1AC\`, lines 64–76 and 110–123.
- \`docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html\`, main blob \`56a9a1c19e7234e2aa258d5ad1b66a5679ace190\`: Definition 21.4.1, source \`:CF692075\`, permanent \`E8746DA689A7\`, lines 11–16; Proposition 21.4.2, source \`:67A1B562\`, permanent \`D6E7C0B06FAD\`, lines 20–46.
- \`docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html\`, main blob \`b3b4e34fff767a717df812a381f905589b257fb3\`: Lemma 21.6.1, source \`:30FFD831\`, permanent \`FCDAD9CEC8CE\`, lines 10–27 (finite convex-envelope identity and attainment).

## Exact global order-interval theorem

Let \(V\) be finite dimensional and \(F,G:V\to(-\infty,+\infty]\) be **proper closed convex functions with the same nonempty effective domain** \(C\). Assume \(F-G\) is bounded on \(C\), and write
\[
 m=\inf_C(F-G),\qquad M=\sup_C(F-G).
\]
The effective domains of \(F^*\) and \(G^*\) coincide; call the common domain \(C^*\). Then
\[
\boxed{\inf_{C^*}(F^*-G^*)=-M,\qquad
\sup_{C^*}(F^*-G^*)=-m.}\tag{1}
\]
In particular, conjugation **exactly preserves** both the global sup norm and the oscillation of the difference:
\[
\boxed{\|F-G\|_{L^\infty(C)}
=\|F^*-G^*\|_{L^\infty(C^*)},\qquad
\operatorname{osc}_C(F-G)=\operatorname{osc}_{C^*}(F^*-G^*).}\tag{2}
\]
These are suprema and infima; there is no assertion of extremizer existence. Differences of extended-real functions are taken **only on their common finite domains**, never as \(\infty-\infty\).

**Complete proof.** By definition of \(m,M\), the extended-real inequalities on \(V\) are \(G+m\leq F\leq G+M\). Conjugation reverses order and translates constants with opposite signs, giving
\[
G^*-M\leq F^*\leq G^*-m.\tag{3}
\]
In particular their finite domains agree. Let \(m^*=\inf_{C^*}(F^*-G^*)\) and \(M^*=\sup_{C^*}(F^*-G^*)\); (3) gives \(m^*\geq-M\), \(M^*\leq-m\). Closedness is used now: the integrated Theorem 21.3.2 gives \(F^{**}=F\) and \(G^{**}=G\). Applying (3) to the pair \(F^*,G^*\), we get \(G-M^*\leq F\leq G-m^*\), hence \(m\geq-M^*\) and \(M\leq-m^*\). Combined with the first two inequalities, these force \(m^*=-M\) and \(M^*=-m\). This proves (1), and taking absolute extrema and ranges proves (2). The proof uses no approximation theorem or limiting interchange.

**Optimality / exact example.** In one dimension take \(F(x)=\max(0,x)\), \(G(x)=\max(1,x)\). They share the full real effective domain and \(F-G\) ranges from \(-1\) to \(0\). Both dual effective domains equal \([0,1]\); \(F^*(p)=0\), \(G^*(p)=p-1\) on that interval. Thus \(F^*-G^*=1-p\) ranges from \(0\) to \(1\): every endpoint and norm/oscillation coefficient in (1)–(2) is attained and sharp. Constant translations give sharpness in all dimensions. **Closedness matters:** the convex indicator of \((0,\infty)\) and the indicator of \([0,\infty)\) have the same conjugate but differ as primal functions; without closedness, conjugation cannot be injective.

## Finite convex dual-rooftop consequence (sharp)

Fix a compact convex body \(P\subset V^*\) and finitely many \(F_i,\widetilde F_i\in\mathcal E^\infty(V,P)\) (Definition 21.4.1), with \(\max_i\|F_i-\widetilde F_i\|_\infty\leq\varepsilon\). Write \(A=\max_iF_i\), \(\widetilde A=\max_i\widetilde F_i\). They remain in \(\mathcal E^\infty(V,P)\). Let \(H\) and \(\widetilde H\) be the convex envelopes of the families \((F_i^*)_i\) and \((\widetilde F_i^*)_i\). Lemma 21.6.1 and Proposition 21.3.3(2) give \(H=A^*\) and \(\widetilde H=\widetilde A^*\). Applying (1)–(2) to \(A,\widetilde A\) gives
\[
\boxed{\|H-\widetilde H\|_{L^\infty(P)}
=\|A-\widetilde A\|_{L^\infty(V)}
\leq\max_i\|F_i-\widetilde F_i\|_\infty\leq\varepsilon.}\tag{4}
\]
Also \(\operatorname{osc}_P(H-\widetilde H)=\operatorname{osc}_V(A-\widetilde A)\) exactly. The coefficient one is optimal: translate each \(\widetilde F_i=F_i+c\) (e.g. all \(F_i=h_P\)); then \(\widetilde H=H-c\), and equality holds with \(|c|\). The common fixed slope body and global bounded differences are essential to apply this as an ordinary finite-norm statement.

**Boundary of conclusion:** (4) is global \(L^\infty\) stability. It does **not** assert that merely local-uniform convergence yields uniform convergence of conjugates on the dual boundary, nor that narrow convergence of real Monge–Ampère measures upgrades to Wasserstein convergence. That latter failure already has the **separate, previously recorded** ID \`POME-TORIC-FULLMASS-WASSERSTEIN-NONUPGRADE-001\` (2026-11-05); it is **not** new work here. The earlier 2026-11-02 boundary dual nonattainment finding is likewise unchanged.

## Audit classification, proposed use and completeness limits

The new theorem (1)–(4) is a **verified conditional deduction** from the printed biconjugation/finite-rooftop inputs, **not** a verified repair of a false theorem. Suggested audit-only annotation: next to Lemma 21.6.1, record the sharp perturbation estimate (4), and caution that local-uniform or mixed-normalization comparisons do not supply its hypotheses. Downstream toric §§21.12–21.13 are **potential** uses only, not transitively certified. All source/historical labels and prior unresolved proof gaps stay unchanged.

**Actual scope:** direct rereading of selected integrated §§21.3.2, 21.3.3(2), 21.4.1–2 and 21.6.1; all these numbered sections had already been partially audited. **0 first-visited sections; 0 fully certified sections; current actual ToC 25 chapters / 747 numbered sections.** No separate project build, tests, CI, formalization, or website publication. User-excluded Demailly approximation/regularization, specialized Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion, and all their old notes remain **deferred-by-user**, not resolved/certified. No \`main\`, source, body, registry, canonicalization or permanent-tag changes.
