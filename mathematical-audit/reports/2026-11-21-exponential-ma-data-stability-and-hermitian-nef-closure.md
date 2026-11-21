# Audit: quantitative exponential Monge–Ampère comparison and the Hermitian nef cone

Date: 2026-11-21. Repository: MingchenXia/Pome. **Reviewed main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. This report reviews the **integrated reading edition**, not source theorem numbers in isolation. It is an audit-only note for \`review/mathematical-audit\`.

## Exact coverage and anchors

1. **Entire §15.2, “Domination with a smaller background”**: \`docs/sections/equations-with-prescribed-singularities--domination-with-a-smaller-background/index.html\`, main blob \`95dc2dd6ba0061e2c096947087c5125b9bad85b0\`, mathematical lines 5–99. Checked Lemma 15.2.1 (source label \`805C891D\`, permanent tag \`E9045CC3F2A3\`, line 14), Theorem 15.2.2 (\`1F4338C0\`, \`D70D1E469F9D\`, lines 44–85), Corollary 15.2.3 (\`8F6F638A\`, \`AF890AD49AC5\`, lines 86–99). Compared hypotheses and the actual contact/measure argument. This is a direct section reading, **not** certification of all referenced upstream comparison and envelope results.

2. **Entire §10.11, “Closed classes with Hermitian lower bounds”**: \`docs/sections/bott-chern-classes-and-singular-loci--closed-classes-with-hermitian-lower-bounds/index.html\`, blob \`cee2450e039f1efe8c32083ee516fdc67737249a\`, mathematical lines 5–57. Checked Proposition 10.11.1 (\`4FDF9D6A\`, \`7F12058085DC\`, lines 20–37) and Proposition 10.11.2 (\`8278956A\`, \`A8D846A01D78\`, lines 38–57).

3. **Selected supporting portions only of §20.4**, \`docs/sections/divisorial-currents-on-compact-modifications/index.html\`, blob \`79d6e21f9d3784bf3761846f77f90ad075253644\`: Bott–Chern quotient and Gauduchon pairing (lines 156–242); Lemma 20.4.20 (source \`281A4711\`, permanent \`721E66DF8C88\`, lines 382–436); Proposition 20.4.22 (\`B3489943\`, \`D7373D3639FA\`, lines 437–468); Theorem 20.4.26 (\`4D5BC429\`, \`400A4F39FD56\`, lines 489–553), focusing on linearity, pullback, mass, the exceptional cocycle and finite exceptional support. **Not** a whole-section direct audit. The §20.4.17–.18 analytic regularization proof and the §20.4 opening approximant construction have been expressly **excluded by the user** and were not audited or certified.

## Finding POME-EXP-MA-MULTIPLICATIVE-DATA-STABILITY-001

**Status:** verified conditional deduction; **severity:** low; **not** a printed theorem error. **Relevant anchors:** Theorem 15.2.2, lines 44–85; Corollary 15.2.3, lines 86–99. **Affected dependents:** exponential Monge–Ampère uniqueness and data perturbation within a fixed ordinary singularity type; no change to the underlying source statement is needed.

**Hypotheses.** Let \(X\) be a compact complex manifold with the background hypotheses of §15.2: \(\theta\) is a smooth semipositive and big closed real \((1,1)\)-form. Let \(u,v\in\operatorname{PSH}(X,\theta)\), assume \(v\preceq u\), and suppose \(P_{\delta\theta}(u)\not\equiv-\infty\) for some \(0<\delta<1\). Let \(\lambda>0\) and \(A\geq1\). Assume that, off the common pole sets (or on the locus where the weights are finite),

\[
 e^{-\lambda u}\operatorname{MA}^{\mathrm{ext}}_\theta(u)
 \ \leq\ A e^{-\lambda v}\operatorname{MA}^{\mathrm{ext}}_\theta(v)
\tag{1}
\]

as positive measures. The \(\operatorname{MA}^{\mathrm{ext}}\) convention is the one in §15.2, and no measures are multiplied by an undefined infinite weight at a pole.

**Claim.** Under (1),

\[
 \boxed{u\geq v-\frac{\log A}{\lambda}}\qquad\text{on }X.
\tag{2}
\]

**Full conditional proof.** Fix \(t>(\log A)/\lambda\). On the plurifine comparison locus \(E_t=\{u<v-t\}\), the positivity of the weights permits multiplication of (1) by \(e^{\lambda u}\); hence

\[
 \mathbf1_{E_t}\operatorname{MA}^{\mathrm{ext}}_\theta(u)
 \leq A e^{\lambda(u-v)}\mathbf1_{E_t}
       \operatorname{MA}^{\mathrm{ext}}_\theta(v)
 \leq A e^{-\lambda t}\mathbf1_{E_t}
       \operatorname{MA}^{\mathrm{ext}}_\theta(v-t).
\]

The constant \(c=Ae^{-\lambda t}\) is strictly less than one. The pair \((u,v-t)\) obeys the order \(v-t\preceq u\) and the smaller-background-envelope hypothesis for \(u\). Apply the *actual* Theorem 15.2.2 (rather than presuming its entire upstream chain has been independently verified): it yields \(u\geq v-t\) globally. Let \(t\downarrow(\log A)/\lambda\) to obtain (2). If the scalar factor is \(A=1\), this recovers the corresponding direction of §15.2.3.

**Symmetric stability.** If \(u,v\) belong to the *same ordinary singularity type*, the smaller-background-envelope property is shared by both (the statement immediately before Lemma 15.2.1). If, off their common pole set, \(\mu=e^{-\lambda u}\operatorname{MA}^{\mathrm{ext}}_\theta(u)\) and \(\nu=e^{-\lambda v}\operatorname{MA}^{\mathrm{ext}}_\theta(v)\) satisfy \(\mu\leq e^\rho\nu\) and \(\nu\leq e^\rho\mu\), with \(\rho\geq0\), apply (2) in both directions to get
\[
 \boxed{|u-v|\leq \rho/\lambda}
\tag{3}
\]
on their common finite locus, equivalently as the two global inequalities between extended-valued quasi-psh functions. In particular, (3) applies to two equations \(\operatorname{MA}_\theta(u)=e^{\lambda u}\mu\), \(\operatorname{MA}_\theta(v)=e^{\lambda v}\nu\), provided the equations use the non-pluripolar convention and the data are mutually \(e^\rho\)-comparable off the common poles. A measure charging the pole set does not enter the argument.

**Sharpness.** Take a positive Kähler form \(\theta\), \(u=0\), \(v=c>0\) constants and \(\mu=\theta^n\), \(\nu=e^{-\lambda c}\theta^n\). Both are solutions of their respective exponential equations, the optimal mutual data factor is \(e^{\lambda c}\), and \(\sup|u-v|=c=\lambda^{-1}\log(e^{\lambda c})\). Thus the coefficient \(1/\lambda\) in (3) cannot be improved.

**Proposed action:** retain the original statements. Optionally add (2)–(3) as a separately reviewed corollary to §15.2 or a cross-reference in its future data-stability discussion; do **not** edit the reader on this audit branch. **Remaining dependency:** the full proof-chain audit of the contact-support and domination inputs to Theorem 15.2.2 (§16.28.5, §16.28.55–.56), as well as the interpretation of extended measures in each particular application.

## Finding POME-HERMITIAN-BC-NEF-CONE-CLOSED-001

**Status:** verified conditional deduction; **severity:** low; **not** a printed theorem error. **Relevant anchors:** Proposition 10.11.1, lines 20–37; Proposition 10.11.2, lines 38–57; Lemma 20.4.20, lines 382–436. **Affected dependents:** Bott–Chern positivity and limits of nef classes on compact non-Kähler manifolds, and the choice of nef Cartier realizations of b-divisorial classes.

**Hypotheses.** Fix a connected compact complex manifold \(X\), a Hermitian form \(\omega\), and a Gauduchon form \(\gamma\). Equip the finite-dimensional \(H^{1,1}_{\mathrm{BC}}(X,\mathbf R)\) with its usual topology, as constructed by the smooth linear representative \(B_\gamma\) in Lemma 20.4.20.

**Claim A: closure.** The nef cone defined in §20.4.16 by smooth \(\varepsilon\)-semipositive representatives is closed in \(H^{1,1}_{\mathrm{BC}}(X,\mathbf R)\). In particular its normalized Gauduchon slice
\[
 \{\alpha\ \text{nef}:\ \ell_\gamma(\alpha)=1\}
\tag{4}
\]
is compact (possibly empty).

**Proof.** Let a net of nef classes \(\alpha_i\to\alpha\). The canonical representatives \(B_i=B_\gamma(\alpha_i)\) converge to \(B=B_\gamma(\alpha)\) in every \(C^k\) norm by Lemma 20.4.20. For each \(i\), choose a smooth closed representative \(R_i\in\alpha_i\) with \(R_i\geq-\epsilon_i\omega\), where the positive numbers \(\epsilon_i\to0\) are freely chosen along the net (or work with the product directed set \(I\times\mathbb N\) if arbitrary \(I\) has no preferred numerical gauge). Then
\[
 R'_i=R_i-B_i+B\in\alpha,\qquad
 R'_i\geq-(\epsilon_i+\delta_i)\omega,
 \quad \delta_i:=\sup_X\|B_i-B\|_\omega\to0
\]
(up to a fixed norm-equivalence constant absorbed in \(\delta_i\)). This is precisely nefness of \(\alpha\). Equivalently, fix an arbitrary \(\epsilon>0\), take one sufficiently late \(i\) with \(\|B_i-B\|_\omega<\epsilon/2\), and select \(R_i\geq-(\epsilon/2)\omega\); no construction of \(\epsilon_i\) on an arbitrary directed set is necessary. Proposition 10.11.2 already proves that the pseudoeffective cone has a compact \(\ell_\gamma=1\) slice and that nef classes are pseudoeffective. The slice (4) is its closed subset and is compact.

**Claim B: varying-class almost-positive current compactness.** Let \(\alpha_i\to\alpha\) be a net of Bott–Chern classes and let \(\epsilon_i\geq0\) be a net of real numbers with \(\epsilon_i\to0\). Suppose that \(T_i\in\alpha_i\) are closed real \((1,1)\)-currents satisfying \(T_i\geq-\epsilon_i\omega\). Then \((T_i)\) is weakly relatively compact, and **every** weak cluster current is closed positive and represents \(\alpha\). This does not assert uniqueness or convergence of the entire net.

**Proof.** The currents \(Q_i=T_i+\epsilon_i\omega\geq0\) satisfy
\[
 \int_XQ_i\wedge\gamma^{n-1}
 =\ell_\gamma(\alpha_i)+\epsilon_i\int_X\omega\wedge\gamma^{n-1},
\]
which is bounded along a tail (and on the full net if one restricts to that tail; arbitrary early indices are irrelevant to convergence). Positivity bounds all coefficient measures uniformly. Banach–Alaoglu for coefficient measures and finite coverings gives weak precompactness of that tail; no sequential-compactness assumption is made. Since \(\epsilon_i\omega\to0\), every cluster current \(T\) is positive, closed and has canonical smooth representative \(B_\gamma(T)=\lim_i B_\gamma(\alpha_i)=B_\gamma(\alpha)\), so \(\{T\}_{\mathrm{BC}}=\alpha\). This sharpens the **fixed-class** mass bound in Proposition 10.11.1 for varying classes without claiming any convergence of the full net.

**Proposed action:** optional explicitly stated nef-closedness corollary in §10.11 and an application to b-divisor models, in a separately reviewed source patch. **Remaining dependency:** the integrated proof of Lemma 20.4.20 uses the Fredholm/elliptic inverse and smooth Bott–Chern representatives. The present proof is complete **relative to** those internal inputs; it is not an independent certification of their transitive dependencies.

## Review checks and exclusions

- In §15.2, verified the order \(v\preceq u\), the strict constant \(0\leq c<1\), the contact set localization, and the final \(t\downarrow0\) transition. There is no interchange of unrelated limits in the new proof.
- In §10.11, checked Gauduchon Stokes pairing, positivity, the non-Kähler Bott–Chern setting, and the difference between first-order trace mass and nonlinear Monge–Ampère mass.
- In selected §20.4.20/.22/.26, checked current-class continuity, proper-pullback handling of \(L^1\) potentials, and the effective exceptional-divisor cocycle *as stated*, but **did not** audit the Demailly regularization programme or treat its quoted analytic approximants as certified.
- No new confirmed false printed theorem is asserted. Both new findings are **verified conditional deductions**, not repairs of a false result. No entire transitive dependency chain was newly certified; earlier deferred-by-user findings remain deferred.
- No tests, builds, code edits, canonicalization edits, CI, main writes, PR merges or website publication were performed.
