# 2026-11-17 — Local non-pluripolar mixed bounds and finite-current mixtures

**Finding ID:** \`POME-NPP-LOCAL-FINITE-MIXTURE-001\`  
**Classification:** low / **verified conditional deduction** (the printed results are **not** false).  
**Main audited:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Reading-edition blob:** \`docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html\` at \`943517743538820940559eae8469ce98ecf5fcd5\`.

## Anchors and precise review scope

- Proposition **13.5.8**, source \`foundations-of-pluripotential-theory:13A73596\`, permanent tag \`A93A2F4C95C2\`: statement at physical lines **132–141**, local truncation argument **144–165**, integrability clause **167–175**.
- Corollary **13.5.10**, source \`foundations-of-pluripotential-theory:63A53022\`, permanent tag \`7FDDF6925B80\`: lines **179–195**.
- Corollary **13.5.11**, source \`foundations-of-pluripotential-theory:238BF8AA\`, permanent tag \`43C93EF28279\`: lines **199–216**.
- Local bounded Bedford–Taylor density inequality, Theorem **7.12.1**, source \`foundations-of-pluripotential-theory:046CCCD5\`, permanent tag \`AAD1BC0CC6C4\`, in \`docs/tag/AAD1BC0CC6C4/index.html\` (the actual integrated statement and the opening of its proof were read). This remains an **internal upstream dependency**, not independently certified in full.
- Plurifine truncation locality, Lemma **13.2.2**, source \`foundations-of-pluripotential-theory:CE1D6DA5\`, permanent tag \`D59675D9F6D8\`; NPP multilinearity and finiteness, Proposition **13.2.6**, source \`foundations-of-pluripotential-theory:E82F0D73\`, permanent tag \`7F7123F92478\`. Their integrated statements and proof openings were inspected. These remain internal dependencies.

The existing Proposition 13.5.8 assumes compact Kähler X, but its **actual lower-bound proof** at lines 147–165 consists entirely of local truncation, the local bounded mixed inequality, plurifine restriction, and removal of a pluripolar set. Its cohomological finiteness is used to guarantee that the products exist as finite measures, not to prove the local inequality itself. We separate the hypotheses required for the latter from those required for global finiteness.

## Deduction: a local theorem and a finite-mixture inequality

Let X be **any** complex manifold of pure complex dimension n≥1, not necessarily compact or Kähler. Let T_1,...,T_r be closed positive (1,1)-currents, and let ν be a positive locally finite Radon measure. Assume:

1. The non-pluripolar self-products \(\langle T_i^n\rangle\) and **every** mixed n-fold product of the T_i occurring below are locally finite Radon measures.
2. There are nonnegative Borel functions f_i such that \(\langle T_i^n\rangle\ge f_i\nu\) as measures.
3. The coefficients \(\lambda_i\ge0\) are finitely many and \(\sum_i\lambda_i=1\).

Then the non-pluripolar top product of \(T_\lambda=\sum_i\lambda_i T_i\) is locally finite, and
\[
\boxed{\quad
\left\langle T_\lambda^n\right\rangle
\ge\left(\sum_{i=1}^{r}\lambda_i f_i^{1/n}\right)^n\nu .
\quad} \tag{A}
\]
This includes the case n=1, vanishing coefficients, zero densities, and singular currents. Finite values of f_i can be selected ν-almost everywhere: the local finiteness of \(\langle T_i^n\rangle\) implies \(f_i\in L^1_{\mathrm{loc}}(\nu)\). Expressions on ν-null sets can be fixed arbitrarily.

**Proof of the local n-tuple mixed inequality.** Fix a relatively compact coordinate open set W carrying local psh potentials \(T_i=dd^c a_i\), chosen bounded above there, and first consider any n-tuple of the T_i (with repetitions allowed). Let
\(G_k=\bigcap_{j=1}^n\{a_j>-k\}\) and \(a_{j,k}=\max(a_j,-k)\).
Plurifine locality (Lemma 13.2.2) gives the equality of the bounded Bedford–Taylor self-products and the NPP self-products on G_k; the latter dominate \(1_{G_k} f_j\nu\). Theorem 7.12.1 applied to the bounded \(a_{j,k}\) and to the Borel densities \(1_{G_k}f_j\) gives
\[
dd^c a_{1,k}\wedge\cdots\wedge dd^c a_{n,k}
\ge 1_{G_k}\prod_{j=1}^n f_j^{1/n}\,\nu.
\]
Restrict to G_k, use again the NPP truncation definition, and obtain
\[
\langle T_{i_1}\wedge\cdots\wedge T_{i_n}\rangle
\ge 1_{G_k}\prod_{j=1}^n f_{i_j}^{1/n}\,\nu.
\]
On \(P=X\setminus\bigcup_kG_k\), a finite union of pole sets, every locally finite NPP self-measure vanishes; the self-measure dominance therefore forces \(f_i=0\) ν-a.e. on P, **for each i**. By monotone convergence on every Borel set, \(1_{G_k}\) may be deleted. This proof is local: no Kähler form, cohomological intersection number, or compactness of X is used. The local hypotheses retain precisely the product finiteness needed to interpret the inequalities.

**Proof of (A).** The verified form of NPP multilinearity (Proposition 13.2.6) and the finiteness assumptions give
\[
\left\langle T_\lambda^n\right\rangle
=\sum_{\alpha_1+\cdots+\alpha_r=n}
\frac{n!}{\alpha_1!\cdots\alpha_r!}
\Bigl(\prod_i\lambda_i^{\alpha_i}\Bigr)
\langle T_1^{\alpha_1}\wedge\cdots\wedge T_r^{\alpha_r}\rangle .
\]
The preceding local inequality bounds each summand below by
\(\prod_i f_i^{\alpha_i/n}\nu\); the **multinomial theorem** now gives (A). This proves the claim without requiring a limiting argument in r. The weighted root sum is locally ν-integrable after raising to power n: convexity yields
\((\sum_i\lambda_i f_i^{1/n})^n\le\sum_i\lambda_i f_i\).

## Sharp singular example and an obstruction to a converse

On \(X=\mathbf P^n\), let \(\omega=\omega_{\mathrm{FS}}\) and choose any hyperplanes H_i and constants \(c_i>0,\ a_i>0\). Set
\[
T_i=c_i\omega+a_i[H_i],\qquad \nu=\omega^n,\qquad f_i=c_i^n .
\]
On the complement of the union of hyperplanes, all T_i are exactly the smooth forms \(c_i\omega\); all non-pluripolar products give zero mass to the union, which is pluripolar. Hence for every n-tuple
\[
\langle T_{i_1}\wedge\cdots\wedge T_{i_n}\rangle
=\Bigl(\prod_{j=1}^n c_{i_j}\Bigr)\omega^n,
\]
and
\[
\left\langle(\sum_i\lambda_i T_i)^n\right\rangle
=(\sum_i\lambda_i c_i)^n\omega^n .
\]
Thus **equality holds in (A) even with genuine divisorial poles and positive discarded polar mass**. The coefficient 1 is sharp; it cannot be improved uniformly.

Conversely, individual top self-products do not provide **upper** control of mixed products. On \(\mathbf P^1\times\mathbf P^1\), put \(T_1=\pi_1^*\omega_{\mathrm{FS}}\) and \(T_2=\pi_2^*\omega_{\mathrm{FS}}\). These are smooth semipositive currents with \(T_1^2=T_2^2=0\), whereas \(T_1\wedge T_2>0\) and
\[
\bigl((T_1+T_2)/2\bigr)^2=\tfrac12\,T_1\wedge T_2>0 .
\]
The lower-bound statement therefore must not be misquoted as a two-sided comparison or a reverse upper estimate.

## Classification, dependents, and unresolved inputs

**Status: verified conditional deduction; severity: low.** No error is identified in Proposition 13.5.8 or Corollary 13.5.11. Their printed compact-Kähler version remains valid. A **proposed separately reviewable enhancement**, not a source edit, is to state the local finite-products version as a remark after 13.5.8 and the finite-r mixture variant after 13.5.11, with the local-finiteness and Radon hypotheses explicit. Direct dependents are Corollaries 13.5.10/11 and any application of mixed density lower bounds. No existing dependent is refuted by this deduction.

The full proof of the analytic Bedford–Taylor inequality 7.12.1, the entire NPP multilinearity proof, and global finiteness outside the compact Kähler hypotheses were **not** independently certified. This report does not claim that local finiteness of every mixed product follows merely from finiteness of the pure products; it is an **explicit additional hypothesis**. No global Hermitian finiteness claim is made. No Demailly approximation/regularization or dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof work was consulted or extended.

## Scope and checks actually performed

Read the current main source, AGENTS.md, documentation/proof-expansions.md, the existing audit status/coverage matrix, the integrated proof lines above, and the three upstream integrated statements. Audited the local removal of the Kähler assumption, multinomial combinatorics, and two explicit smooth/singular witnesses by direct mathematical calculation. **No tests, builds, external source audit, CI, site publication, or full mathematical-section certification**. §13.5 already had selected proof-level coverage: **0 newly first-visited sections / 0 newly fully certified sections**; current main table of contents was independently counted as **25 chapters / 747 sections**. Previous findings remain unchanged, and user-excluded work remains **deferred-by-user**, not resolved.
