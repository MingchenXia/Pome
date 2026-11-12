# Exact vague-to-narrow criterion for positive Radon nets

**Date:** 2026-11-12 (Asia/Shanghai). **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Finding:** \`POME-MEASURE-VAGUE-MASS-NARROW-NET-001\` — **low / verified conditional deduction**.
**Scope:** new proof-level examination of the integrated §2.6, especially Propositions 2.6.2–2.6.3; context checks of Proposition 2.6.1, Example 2.6.4, and Theorem 2.6.5. The printed statements are **not refuted**.

## Exact integrated provenance

- Reading-edition file: \`docs/sections/measures-and-distributions--weak-convergence-of-measures/index.html\`, main blob \`45720b2399a645a1a9a8148873fdc01c634fc5d7\`.
- Proposition **2.6.2**, source \`foundations-of-pluripotential-theory:6031A2A1\`, permanent tag \`132090FCDF4A\`, physical lines **37–55**: open-set liminf and compact-set limsup for vague **nets**.
- Proposition **2.6.3**, source \`foundations-of-pluripotential-theory:A9ED3F7E\`, permanent tag \`54258F39AC23\`, physical lines **57–72**: eventual uniform tightness plus vague convergence implies finite narrow limit.
- Example **2.6.4**, source \`foundations-of-pluripotential-theory:B49233FD\`, permanent tag \`81B4A3D092FF\`, physical lines **75–77**: positive escape-of-mass examples, **not newly registered** here.
- Theorem **2.6.5**, source \`foundations-of-pluripotential-theory:C9B16608\`, permanent tag \`F9F4241C5BD2\`, physical lines **80–102**: diagonal extraction for **sequences**, not automatically nets.
- Additional internal dependencies: §2.2 Radon inner regularity and compact cutoffs, and §2.6.2–3 as above. None is declared transitively certified.

## The exact three-way equivalence (new deduction)

Let \(\Omega\subset\mathbb R^d\) be open. Let \((\mu_i)_{i\in I}\) be an **arbitrary directed net of finite positive Radon measures** on \(\Omega\), converging vaguely against \(C_c(\Omega)\) to a **finite positive Radon measure** \(\mu\). Then the following are equivalent:

1. **Narrow convergence:** \(\int f\,d\mu_i\to\int f\,d\mu\) for all \(f\in C_b(\Omega)\).
2. **No loss of total mass:** \(\mu_i(\Omega)\to\mu(\Omega)\).
3. **Eventual uniform tightness:** for every \(\varepsilon>0\) some compact \(K\Subset\Omega\) and index \(i_\varepsilon\) satisfy \(\mu_i(\Omega\setminus K)<\varepsilon\) whenever \(i\ge i_\varepsilon\).

In fact, if only \(\mu_i(\Omega)\to m<\infty\) is assumed, then the vague limit is automatically finite with \(\mu(\Omega)\le m\), and conditions 1–3 hold precisely when \(m=\mu(\Omega)\).

**Proof (no sequence extraction).** Under 1, use the bounded continuous test \(f=1\) to get 2. Assume 2 and put \(M_i=\mu_i(\Omega)\), \(M=\mu(\Omega)\). Fix \(\varepsilon>0\). By inner regularity of the finite Radon measure \(\mu\), choose compact \(K\Subset\Omega\) with \(\mu(\Omega\setminus K)<\varepsilon\). Choose \(\eta\in C_c(\Omega)\), \(0\le\eta\le1\), \(\eta=1\) on \(K\), and set \(L=\operatorname{supp}\eta\). Then
\[
M-\int\eta\,d\mu\le\mu(\Omega\setminus K)<\varepsilon.
\]
Vague convergence and \(M_i\to M\) give a common tail of the **directed net** on which
\[
|M_i-M|<\varepsilon,\qquad
\left|\int\eta\,d\mu_i-\int\eta\,d\mu\right|<\varepsilon.
\]
For each such \(i\),
\[
\mu_i(\Omega\setminus L)
\le M_i-\int\eta\,d\mu_i
=(M_i-M)+\left(M-\int\eta\,d\mu\right)
-\int\eta\,d(\mu_i-\mu)<3\varepsilon.
\]
The compact set \(L\) proves 3, after rescaling \(\varepsilon\). This argument invokes no sequential compactness, no common initial bound over all net indices, and no interchange of two independent limits. The implication 3 \(\Rightarrow\) 1 is exactly printed Proposition 2.6.3 (the finite vague limit is given here). Finally, if \(M_i\to m<\infty\), the open-set liminf of printed Proposition 2.6.2 with \(U=\Omega\) gives \(\mu(\Omega)\le m\); thus \(\mu\) is finite. The equivalence then applies. \(\square\)

**Finite-index error control.** For any \(f\in C_b(\Omega)\) and \(0\le\eta\le1\) in \(C_c(\Omega)\), positivity gives
\[
\begin{aligned}
\left|\int f\,d(\mu_i-\mu)\right|
&\le\left|\int f\eta\,d(\mu_i-\mu)\right|\\
&\quad+\|f\|_\infty
\left[\,|M_i-M|+
\left|\int\eta\,d(\mu_i-\mu)\right|
+2\left(M-\int\eta\,d\mu\right)\right].
\end{aligned}\tag{*}
\]
Indeed the uncut integrals are bounded by \(\|f\|_\infty\) times the nonnegative remainders \(\mu_i(\Omega)-\mu_i(\eta)\) and \(\mu(\Omega)-\mu(\eta)\), and the first remainder is rewritten using \(M_i-M\) and the compact-test error. Choosing \(\eta\) with a small \(\mu\)-tail and then letting the net index grow proves narrow convergence directly and quantitatively for each fixed bounded continuous test. This is a useful replacement for arguments that incorrectly exchange compact exhaustion and net limits.

## Exact sign and topology boundaries

The positive-measure hypothesis cannot be silently dropped. On \(\mathbb R\), let \(\nu_j=\delta_j-\delta_{j+1}\) be **signed** finite Radon measures. Then \(\nu_j\to0\) vaguely and \(\nu_j(\mathbb R)=0\) for every \(j\), but for the bounded continuous function \(f(x)=\cos(\pi x)\),
\[
\int f\,d\nu_j=2(-1)^j
\]
does not converge. Thus mass conservation plus vague convergence alone is **false for signed measures**; one needs control of total variation tails in the analogous argument. This is a scope counterexample to an *unsupported extension*, **not** a counterexample to the positive-measure statements of Pome.

Nor does the equivalence give convergence in total variation. For example, \(\delta_{1/j}\to\delta_0\) narrowly on \(\mathbb R\), with constant mass one, yet \(\|\delta_{1/j}-\delta_0\|_{\rm TV}=2\) (the variation norm convention).

## Disposition and affected dependents

**Proposed correction:** no change to any printed theorem. An optional corollary after Proposition 2.6.3 may record the converse and the three-way equivalence for **finite positive** measures on the stated Euclidean domain, as well as the finite-index cutoff bound (*). For uses in current/measure compactness, the proper downstream check is whether one has control of total **positive** mass or of **variation** for signed objects; equality of signed masses alone does not suffice. No specific downstream theorem is asserted false on this basis.

**Certification boundary:** Proposition 2.6.3 and its referenced Radon/Portmanteau inputs are used as established internal statements, not audited transitively. This selected argument does not certify the whole of §2.6 or the project's measure/convergence chapter. The preexisting §2.7 vague metrizability/diagonal audit and §2.8 distributional-Hessian audit are distinct and are not counted again.

**Excluded by author:** Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**; no prerequisite replay was attempted. No project source, main, registry, canonical tags, CI, build, tests, or website publication was changed by this audit.