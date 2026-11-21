# Okounkov Duistermaat–Heckman convergence with mismatched bases; analytic divisor and toric review

**Audit date:** 2026-11-21. **Read-only main baseline:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Working branch:** review/mathematical-audit. No theorem, source, registry, permanent-tag, published-page or main-branch changes are made by this report.

## Exact integrated source and scope

- Full current §19.6, docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html, mathematical lines 7–512, Git blob 20ff3089e62dd1c8349e8bcc077ec64605a9788b. Primary source variant **sgpt**, Proposition 19.6.14, source tag BC456E2F / permanent **7B4552909292** (lines 237–273); Definition 19.6.18, permanent **51940EF88F4F** (329–334); Lemma 19.6.22, source tag B9C8ADE8 / permanent **9C05354365F4** (371–405); increasing analogue Lemma 19.6.23 (410–443), test-curve/Legendre foundations (17–232), moment identities (338–365) and geometric construction (447–508).
- Full current §20.5, docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html, mathematical lines 7–158, Git blob dae567406b2030e550664ca57b1fe77911d956d4. Demailly-complex-geometry source, Theorem 20.5.5 source tag D58680EB / permanent **F1C928146DBC**, lines 64–128; Theorem 20.5.10 permanent **DDB973C0C1DD**, lines 133–150.
- Full current §20.7, docs/sections/meromorphic-sections-and-divisor-classes/index.html, mathematical lines 5–31, Git blob d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8. Demailly-complex-geometry source, Proposition 20.7.3 source tag 00A05C89 / permanent **ACC6D09EDDD9**, lines 12–30.
- Full current §21.9, docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, mathematical lines 7–170, Git blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c. Foundations-of-pluripotential-theory, Theorem 21.9.5 source tag BD98CC5B / permanent **69D3D97E7701** (139–167); propositions on normal fans, toric orbit strata and affine overlaps (7–106), Laurent-series lemma (113–134).

All full-section labels describe **fresh direct reading of these four actual integrated sections**, not the first historical examination. Upstream chains are not certified in full.

## Finding POME-OKOUNKOV-DH-BASE-MISMATCH-VAGUE-001

**Severity:** low. **Status:** verified conditional deduction (new *weakening* of a hypothesis of Lemma 19.6.22, not an error in that lemma). **Affected dependents:** §19.6.18/.22/.23 Duistermaat–Heckman convergence, and comparisons of §22.1.54 non-Archimedean DH measures. The previously recorded non-Archimedean special example is not counted as a new finding here.

**Statement.** Let \(n\ge1\), and let \((K_j)_{j\ge1}\) be a **decreasing sequence** of convex bodies contained in \(K_1\), with a full-dimensional convex body \(\Delta\subseteq\bigcap_jK_j\). Suppose \(\Gamma^j_\bullet\in\mathrm{TC}(K_j)\) is a decreasing sequence, \(\Gamma_\bullet\in\mathrm{TC}(\Delta)\), \(\Gamma^j_{\max}\to\Gamma_{\max}\in\mathbb R\), and
\[
 \Gamma^j_t\xrightarrow{d_{\mathrm{Haus}}}\Gamma_t\quad\text{for each fixed }t<\Gamma_{\max}.
\]
These are the *sequence* specialization of Proposition 19.6.14. **No assumption** that \(K_j\to\Delta\) is imposed. Then
\[
 \mathrm{DH}(\Gamma^j_\bullet)\ \longrightarrow\
 \mathrm{DH}(\Gamma_\bullet)\quad\text{vaguely on }\mathbb R
 \quad(\text{against all }f\in C_c(\mathbb R)).
\]
Writing \(K_\infty=\bigcap_jK_j\), the exact mass discrepancy is
\[
 \lim_j\mathrm{DH}(\Gamma^j_\bullet)(\mathbb R)
       -\mathrm{DH}(\Gamma_\bullet)(\mathbb R)
   =\operatorname{vol}(K_\infty)-\operatorname{vol}(\Delta)\ge0.
\]
No mass can escape to \(+\infty\), since the maximal levels tend to a finite number. If this discrepancy is nonzero, convergence against all bounded continuous functions is impossible. If it is zero, vague convergence plus convergence of total masses **does** give bounded-continuous weak convergence. This is an exact tightness criterion, not a statement about arbitrary directed nets.

**Proof.** Set \(G_j=G[\Gamma^j_\bullet]\) and \(G=G[\Gamma_\bullet]\), using the Legendre conventions in Definition 19.6.7. These are finite on the interiors of their bases and may equal \(-\infty\) on measure-zero boundaries. Proposition 19.6.14 gives \(G_j(x)\downarrow G(x)\) for every \(x\in\Delta\). Now fix \(x\in K_1\setminus\Delta\). If \(x\notin K_j\) for some \(j\), the decreasingness of the bases means it is absent thereafter. Otherwise \(x\in K_j\) for all \(j\). For each fixed \(t<\Gamma_{\max}\), the compact limit \(\Gamma_t\) lies in \(\Delta\), hence \(d(x,\Gamma_t)>0\); Hausdorff convergence then implies \(x\notin\Gamma^j_t\) eventually. As \(t\) is arbitrary, \(G_j(x)\to-\infty\).

For \(f\in C_c(\mathbb R)\), extend \(f\) continuously by \(f(-\infty)=0\), and put \(H_j(x)=\mathbf1_{K_j}(x)f(G_j(x))\) on \(K_1\). The pointwise argument gives \(H_j(x)\to\mathbf1_\Delta(x)f(G(x))\) except on measure-zero boundary sets. Since \(|H_j|\le\|f\|_\infty\) on the fixed compact \(K_1\), the **ordinary sequential** dominated convergence theorem gives
\[
 \int_{K_j}f(G_j)\,dx\ \longrightarrow\ \int_\Delta f(G)\,dx.
\]
The pushforward definition of DH proves vague convergence. Separately, the finite-measure continuity-from-above theorem applied to the decreasing compact sets \(K_j\) gives \(\operatorname{vol}(K_j)\to\operatorname{vol}(K_\infty)\). The total-mass formula (19.6.21) gives the discrepancy. Convergence of the right-hand maxima excludes escape to \(+\infty\). For zero discrepancy, choose a compact cutoff whose integral captures all but an arbitrarily small part of the limit DH mass; vague convergence and convergence of total masses then yield uniform tightness of the tails, which upgrades compactly supported tests to all bounded continuous tests.

**Sharp one-dimensional example.** Take \(K_j=[0,2]\), \(\Delta=[0,1]\), \(\Gamma_{\max}^j=\Gamma_{\max}=0\), and concave test functions
\[
 G_j(x)=-j(x-1)_+\quad(0\le x\le2), \qquad G(x)=0\quad(0\le x\le1).
\]
The inverse Legendre test curves are
\[
 \Gamma_t^j=[0,\min\{2,1-t/j\}],\quad
 \Gamma_t=[0,1]\qquad(t<0).
\]
They decrease with \(j\), each \(\Gamma_t^j\) tends to \([0,1]\) at fixed \(t<0\), and each family tends to its own base as \(t\to-\infty\). Their DH laws are exactly
\[
 \mathrm{DH}(\Gamma_\bullet^j)=\delta_0+
      \frac1j\mathbf1_{[-j,0]}(s)\,ds,\qquad
 \mathrm{DH}(\Gamma_\bullet)=\delta_0.
\]
Thus compact-test convergence holds, yet the masses remain \(2\) versus \(1\), so even the bounded test \(f\equiv1\) separates them. The single unit of excess mass escapes to \(-\infty\). This explicitly verifies why the **extra base-Hausdorff-convergence hypothesis in the printed Lemma 19.6.22 must be retained** if “weak convergence” means bounded-continuous/narrow convergence. Importantly, that printed lemma **already assumes** \(K_j\to\Delta\), so neither its statement nor its proof is refuted.

**Proposed action:** add an optional separate corollary for the base-mismatch *vague* version; keep the printed Lemma 19.6.22 and its base-convergence hypothesis unchanged. Use the terms *vague* and *bounded-continuous weak* explicitly. Do not replace sequential dominated convergence by an unproved arbitrary-net version.

## Other full-section checks (no new confirmed printed error)

**§20.5.** Checked the distinction between a reduced integration current and an effective integral cycle, proper pushforward of prime divisors in Lemma 20.5.3 (rank drop versus positive integer degree), the resolution-based proof of \(dd^c(\log|f|^2[A])\) and its positive integer multiplicities, coefficient-integrable logarithmic limits without monotonicity, proper-intersection hypotheses for classical divisor products, and the cusp order-two check in Example 20.5.11. The proof genuinely uses the separately declared resolution-of-singularities input (permitted Hironaka exception). The theorem is not thereby transitively certified; relevant proper-mapping, analytic-purity and classical-product inputs remain to audit independently.

**§20.7.** Checked both signs in \(dd^c\log|s|_h^2=[\operatorname{div}s]-c_1(L,h)\), local cancellation of meromorphic quotient divisors, the transition \(e_i=(u_j/u_i)e_j\), and the principal-divisor kernel. The proposition correctly **restricts the image** of \(D\mapsto\mathcal O(D)\) to line bundles admitting a componentwise nonzero meromorphic section; it does not assert that every line bundle has one. Local purity and Poincaré–Lelong remain upstream dependencies.

**§21.9.** Checked inward normal orientation (orders \(\langle m,u_\rho\rangle\)), inclusion reversal for orbit closures, toric chart overlap \(\chi^{v'-v}\ne0\), the normal-convergence estimate in the multi-Laurent proof, finite global-section decomposition for \(kP\cap M\), and the \(k=0\) bounded-polytope case. The action weight of \(\chi^m s_0^k\) is \(-m\) under the stated *left action on sections*, consistent with the proof. Results of §§21.7–21.8 and the line-bundle/divisor identification remain as named internal dependencies, not wholly certified chains.

## Status and verification boundary

**Actual current-turn scope:** four entire mathematical sections directly read; zero new whole upstream proof chains certified; one new conditional generalization with a complete sequential argument and sharp example; zero new confirmed printed theorem errors. Existing historical matrix statuses remain unreconciled unless separately substantiated. Excluded Demailly approximation/regularization, dedicated Bergman/L2/OT/multiscale-atlas/positivity-loss completion notes remain **deferred-by-user**, not resolved or certified. The Demailly-origin §20.5/§20.7 *divisor* mathematics is outside that excluded subject. No builds, tests, CI, publication, or production edits were performed.
