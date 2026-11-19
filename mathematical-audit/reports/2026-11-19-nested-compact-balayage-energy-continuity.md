# Nested compact balayage: exact energy increments, continuity, and a capacitary boundary

**Finding ID:** POME-CLASSICAL-NESTED-COMPACT-SWEEP-ENERGY-001  
**Date:** 2026-11-19  
**Severity/status:** low / **verified conditional deduction** (not a false printed theorem, not a completed transitive dependency audit).  
**Main baseline:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading file:** \`docs/sections/green-energy-and-martin-boundaries/index.html\`, blob \`976a90f2a5eba299658f73a1eee8b9d3fef8020f\`.  
**Directly checked statements:** Theorem 4.5.2 (permanent \`CC3D1AD9179B\`, source \`classical-potential-theory:AEA69819\`, lines 17–42); Theorem 4.5.4 (permanent \`CE0D5F4DF7B2\`, source \`classical-potential-theory:5FB19CB2\`, lines 47–68); Theorem 4.5.6 (permanent \`B15EFD960FD5\`, source \`classical-potential-theory:9D70EB64\`, lines 77–88). Example 4.5.5 (permanent \`61A5D2A82793\`, source \`classical-potential-theory:898691BF\`, lines 70–75) was also compared for nonredundancy.  
**Scope:** selected proofs and exact consequences in §4.5; NOT an entire-section proof audit and NOT an audit of the Martin boundary theorems 4.5.8–4.5.13.

## Precise setting

Let \(\Omega\subset\mathbb R^d\) be connected and Greenian, with its positive symmetric Green kernel \(G_\Omega\) and the normalization in §4.5.1. Write \(\mathcal E^+\) for positive Radon measures of finite Green energy and
\[
\langle\alpha,\beta\rangle=I(\alpha,\beta)
=\iint_{\Omega^2}G_\Omega(x,y)\,d\alpha(x)\,d\beta(y).
\]
For compact \(K\subset\Omega\), let \(\mu^K\) denote the unique projection of \(\mu\in\mathcal E^+\) onto the closed convex cone of finite-energy positive measures supported on \(K\), as in Theorem 4.5.6; if \(K=\varnothing\), put \(\mu^\varnothing=0\). In particular
\[
G\mu^K\le G\mu \quad\text{everywhere},\qquad
G\mu^K=G\mu\quad\text{quasi-everywhere on }K,
\]
and finite-energy measures give no mass to polar sets (Theorem 4.5.2).

## Result A: exact nested energy identity

For any two nested compact sets \(K\subset L\subset\Omega\),
\[
\boxed{\quad
\langle\mu^K,\mu^L\rangle=\|\mu^K\|^2,\qquad
\|\mu^L-\mu^K\|^2=\|\mu^L\|^2-\|\mu^K\|^2.
\quad} \tag{A}
\]
Indeed \(\mu^K\) is supported on \(K\subset L\), does not charge polar sets, and \(G\mu^L=G\mu\) quasi-everywhere on \(L\). Hence
\[
\langle\mu^K,\mu^L\rangle
=\int_K G\mu^L\,d\mu^K
=\int_K G\mu\,d\mu^K
=\langle\mu,\mu^K\rangle
=\|\mu^K\|^2,
\]
where the last equality is the projection orthogonality in §4.5.6. Expanding the square proves (A). In particular \(K\mapsto\|\mu^K\|^2\) is monotone under inclusion, and (A) supplies a sharp unit-coefficient modulus rather than only convergence.

## Result B: decreasing compact sets need no regularity hypothesis

Let \(K_1\supset K_2\supset\cdots\) be compact subsets of \(\Omega\), with \(K=\bigcap_jK_j\). Then
\[
\boxed{\mu^{K_j}\longrightarrow\mu^K
\quad\text{strongly in Green energy}.} \tag{B}
\]
For \(i<j\), formula (A) with \(K_j\subset K_i\) says
\(\|\mu^{K_i}-\mu^{K_j}\|^2
=\|\mu^{K_i}\|^2-\|\mu^{K_j}\|^2\).
The nonincreasing bounded nonnegative sequence of squared norms converges, so the sweeps are energy Cauchy. Completeness of \(\mathcal E^+\), Theorem 4.5.4, yields a strong limit \(\lambda\). Strong convergence entails vague convergence; compact nested supports imply \(\operatorname{supp}\lambda\subset K\). For every \(\nu\in\mathcal E^+\) supported on \(K\), each \(K\subset K_j\) gives
\[
\langle\mu-\mu^{K_j},\nu\rangle=0.
\]
Taking the energy limit gives \(\langle\mu-\lambda,\nu\rangle=0\), which characterizes the projection onto the cone supported on \(K\); hence \(\lambda=\mu^K\). The argument covers polar or empty intersections and uses no continuity of the pointwise reduced potential.

## Result C: increasing compact exhaustion with polar remainder

Let \(K_1\subset K_2\subset\cdots\subset K\), all compact, and suppose the Borel set
\[
N=K\setminus\bigcup_{j\ge1}K_j
\]
is polar. Then
\[
\boxed{\mu^{K_j}\longrightarrow\mu^K
\quad\text{strongly in Green energy}.} \tag{C}
\]
Again (A) and boundedness \(\|\mu^{K_j}\|\le\|\mu\|\) make the sweeps strongly Cauchy; call their limit \(\lambda\). Since all supports lie in \(K\), so does \(\operatorname{supp}\lambda\). For any \(\nu\in\mathcal E^+\) supported on \(K\), no-polar-mass gives \(\nu(N)=0\), so \(\nu_j=\nu|_{K_j}\uparrow\nu\) and
\[
\|\nu-\nu_j\|^2
=\iint G_\Omega(x,y)\,d(\nu-\nu_j)(x)\,d(\nu-\nu_j)(y)
\longrightarrow 0
\]
by dominated convergence against the finite measure \(G_\Omega\,d\nu\,d\nu\). As \(\nu_j\) is supported on \(K_j\),
\(\langle\mu-\mu^{K_j},\nu_j\rangle=0\).
By Cauchy–Schwarz and strong convergence we obtain
\(\langle\mu-\lambda,\nu\rangle=0\) for all such \(\nu\). Since \(\lambda\) belongs to the same support cone, it is its projection of \(\mu\), hence equals \(\mu^K\).

The polar-remainder condition is a *sufficient* assumption, not claimed to be logically necessary for every individual \(\mu\) or compact exhaustion.

## Sharp warning: Hausdorff-dense compact exhaustion is insufficient

Take \(\Omega=\mathbb R^3\) and \(K=\overline{B(0,1)}\). Choose a countable dense subset \(\{x_j\}\subset K\) and put \(K_j=\{x_1,\dots,x_j\}\). Then \(K_j\) is compact, \(K_j\uparrow\) and \(d_H(K_j,K)\to0\), but each \(K_j\) is finite and polar. The only finite-energy positive measure supported on \(K_j\) is zero, so \(\mu^{K_j}=0\) for every \(\mu\in\mathcal E^+\). Choose the nonzero finite-energy equilibrium measure \(\mu=\mu_K\) of the nonpolar compact ball. Since \(\mu\) is supported on \(K\), its projection is \(\mu^K=\mu\ne0\). Therefore \(\mu^{K_j}\not\to\mu^K\), even weakly in energy. Ordinary Hausdorff convergence cannot replace the capacitary control in (C). This elementary compact-set example is distinct from the previously recorded Martin boundary half-space/strip models and the signed-energy incompleteness Example 4.5.5.

## Status, dependents, and audit accounting

The exact identities and continuity deductions (A)–(C) are proved **conditionally on** the printed internal finite-energy facts: no mass on polar sets and Cauchy–Schwarz (4.5.2), completeness/strong-to-vague convergence of \(\mathcal E^+\) (4.5.4), and existence/uniqueness/orthogonality/quasi-everywhere contact for compact-set projections (4.5.6). These statements and their relevant proof paragraphs were directly read, but all earlier potential-theoretic prerequisites and their transitive proof chains have not been certified; record them as conditional dependencies, **not** as a diagnosed false theorem or an independently confirmed proof gap. Compact sweeps and monotone-domain potential approximations are the mathematical dependents; the correction is to state (B)/(C) with their exact distinct hypotheses, and never infer (C) from Hausdorff convergence alone. No source statement, permanent tag, attribution, or canonicalization is to be changed in this audit commit.

**Coverage delta:** §4.5 selected direct proof check (Theorems 4.5.2/4/6 and Example 4.5.5), **+0 whole sections**, **+0 complete upstream chains**; its historical first-visit status remains unreconciled. The 25-chapter / 747-section table-of-contents inventory remains as recorded by \`SECTION_MATRIX.md\`. All Demailly regularization/approximation and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, neither reviewed nor certified here. No tests, build, CI, main changes or website publication performed.
