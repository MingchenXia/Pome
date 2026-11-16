# Dense-set convergence of convex nets: eventual local boundedness and locally uniform limits

**Date:** 2026-11-17. **Stable finding ID:** POME-CONVEX-DENSE-NET-LOCAL-UNIFORM-001.
**Classification:** low / **verified conditional deduction** (self-contained at the convex-analysis level, using the printed elementary convex-hull and subgradient results). **No false printed theorem and no new established proof gap.**
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Integrated reading edition:** \`docs/sections/convex-analysis-and-toric-potentials--closed-convex-functions-and-supporting-slopes/index.html\` (blob \`66bfd5b3f6cdfaced77dc1741a995e22768141f1\`).
**Source and permanent locators:** §21.2 permanent section tag \`5430067C9C99\`; Proposition 21.2.6 source \`data-tag="57C22F00"\`, permanent \`EAC7AAEC7279\`, statement physical HTML line 159, printed sequence proof lines 177–181; the cube estimate (21.2.2) \`data-tag="D1805A42"\`, permanent \`C59E34BB3C43\`, lines 38–45; elementary separation Lemma 21.2.3 \`data-tag="5D4512D3"\`, permanent \`34526AA883B2\`, lines 49–89. Cross-checks: Proposition 21.2.4 permanent \`72D7B299EAB8\`, lines 94–154; Proposition 21.2.8 permanent \`909102168A21\`, lines 197–230; Corollary 21.2.9 lines 235–258.

## Precisely reviewed statement and new strengthening

The **printed last assertion of Proposition 21.2.6** assumes a **sequence** of finite convex functions \((F_j)\) on a nonempty open convex set \(\Omega\subset\mathbb R^n\), converging to a finite scalar limit at every point of a dense subset \(S\subset\Omega\), and concludes locally uniform convergence to a finite convex function.

**Additional result (net version).** Let \(I\) be any directed set and \(F_i:\Omega\to\mathbb R\), \(i\in I\), be finite convex functions. Suppose that for every \(s\) in a dense subset \(S\subset\Omega\), the *entire net* \(F_i(s)\) converges to a finite real number \(g(s)\). Then there is a unique finite continuous convex \(F:\Omega\to\mathbb R\), extending \(g\), such that \(F_i\to F\) uniformly on every compact subset of \(\Omega\). No countable cofinal subset, sequence/subnet extraction, or a priori locally uniform bound is assumed.

The proof must use **eventual** bounds, not the false general claim that an arbitrary convergent scalar net is bounded over all its indices.

## Direct proof

Fix \(x\in\Omega\) and choose \(\rho>0\) with the closed coordinate cube \(Q(x,2\rho)\subset\Omega\). For each of the \(2^n\) vertices \(v\) of \(Q(x,\rho)\), select \(s_v\in S\) at coordinate distance less than \(\rho/2\) from \(v\); write \(S_0=\{s_v\}\) and \(H=\operatorname{conv}S_0\). Every \(s_v\) belongs to \(Q(x,2\rho)\).

**Claim:** \(Q(x,\rho/2)\subset H\). Indeed, if a point of the smaller cube were outside the compact convex set \(H\), strict separation in Lemma 21.2.3(1) would supply a nonzero linear functional \(\ell(y)=\sum a_jy_j\) with \(\ell(z)>\sup_H\ell\). Choose the original vertex \(v=x+\rho(\operatorname{sgn}a_j)_j\) maximizing \(\ell\) on \(Q(x,\rho)\). Its selected \(s_v\) satisfies
\[
\ell(s_v)>\ell(x)+\frac{\rho}{2}\sum_j|a_j|
=\sup_{Q(x,\rho/2)}\ell,
\]
a contradiction. This checks the quantitative convex-hull step of the printed proof independently.

Pick \(s_*\in S\cap Q(x,\rho/8)\). Since the finitely many scalar nets \(F_i(s)\), \(s\in S_0\cup\{s_*\}\), converge to finite numbers, directedness supplies **one index \(i_0\)** and \(M<\infty\) such that
\[
|F_i(s)|\le M \quad (i\ge i_0,\ s\in S_0\cup\{s_*\}).
\]
The finite Jensen inequality gives \(F_i\le M\) on \(H\), hence on \(Q(x,\rho/2)\). For \(y\in Q(s_*,3\rho/8)\), also \(2s_*-y\) lies there, so midpoint convexity and \(F_i(s_*)\ge-M\) give
\[
F_i(y)\ge 2F_i(s_*)-F_i(2s_*-y)\ge-3M.
\]
As \(Q(x,\rho/4)\subset Q(s_*,3\rho/8)\), for \(i\ge i_0\) we have \(|F_i|\le B:=\max(M,3M)\) on \(Q(x,\rho/4)\). The printed oscillation inequality (21.2.2), with inner cube \(Q(x,\rho/8)\), gives for all tail indices a common Lipschitz constant \(L=16B/\rho\) in Euclidean coordinate norm. If \(L=0\), the functions are constant on this cube and the following step is immediate.

For any \(\varepsilon>0\), density of \(S\) and compactness of \(Q(x,\rho/8)\) supply a **finite** set \(T_\varepsilon\subset S\cap Q(x,\rho/8)\) whose points are within \(\varepsilon/(4L)\) of every point of the cube (take a slightly finer covering if needed). Pointwise scalar convergence at this finite set and directedness give \(i_\varepsilon\ge i_0\) with
\[
|F_i(t)-F_j(t)|<\varepsilon/2
\quad(t\in T_\varepsilon,\ i,j\ge i_\varepsilon).
\]
For any \(y\) in the cube choose \(t\in T_\varepsilon\) with \(|t-y|<\varepsilon/(4L)\); then
\[
|F_i(y)-F_j(y)|
\le L|y-t|+\varepsilon/2+L|t-y|<\varepsilon.
\]
Thus the original net is uniformly Cauchy on this cube. The Banach completeness of bounded real functions on a compact set gives a uniform limit; uniqueness on overlaps patches the local limits to a finite continuous function \(F\) on \(\Omega\), with \(F|_S=g\). Convexity passes to the scalar limits. Every compact \(K\subset\Omega\) is covered by finitely many such cubes; directedness again combines their indices, proving uniform convergence on \(K\), **for the entire net**. Uniqueness follows from continuity and density of \(S\).

This also proves **eventual local equiboundedness and equi-Lipschitz continuity** under only dense-set pointwise convergence, an explicit auxiliary conclusion useful when dealing with nonsequential analytic nets.

## Why a sequential proof cannot be copied verbatim without changing one quantifier

For \(I\) the finite subsets of \(\mathbb N\), ordered by inclusion, let \(F_A(x)\) be the constant \(|A|\) if \(1\notin A\), and \(0\) if \(1\in A\). This is a net of finite convex functions converging *eventually identically to zero* on \(\mathbb R^n\), but the scalar set \(\{F_A(x):A\in I\}\) is unbounded for every \(x\). Consequently, the printed line 179 inference “convergent sequences are bounded (for all indices)” cannot simply be transplanted to arbitrary nets; replacing it by one common **tail** over the finite control set is essential. This is a caution for the extension, **not an error in the printed sequential proof**.

## Additional direct audit and dependencies

The selected §21.2 printed proofs were read at proof level: Lemma 21.2.3(1)–(4), lines 75–89 (Euclidean nearest-point separation, boundary support, Carathéodory reduction, and the relative-boundary measure-zero dilation argument); Proposition 21.2.4, lines 117–154 (relative-interior subgradient, one-sided slopes, differentiability and Fubini); Proposition 21.2.6, lines 164–181 (closed epigraph and dense-set control); Proposition 21.2.8, lines 203–230 (translation-invariant psh/convex correspondence); Corollary 21.2.9, lines 249–258 (exponential pullback and local logarithmic inverse). The claims as printed have no counterexample arising from the steps checked. The proof of the net extension independently checks the finite convex-hull geometry and the local Lipschitz mechanism rather than merely citing the sequence statement.

The invariant-psh arguments use the separately printed positive-distribution and mollification theorems in §§2.5,3.4,5.9 and the pullback rule, **not independently reverified here**. General downstream real Monge–Ampère continuity (notably §21.5), toric pluripotential theory, or those analytic inputs must not be called certified from this local result. In particular, no excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was opened.

**Proposed action:** optionally record the arbitrary-net strengthening immediately after Proposition 21.2.6 in a separately reviewable mathematical PR; retain original sequence statement and stable tags. This report makes **no source/body/registry/canonicalization edits**. **Coverage delta:** §21.2 first substantive direct visit **+1**; full-section/transitive certification **+0**. Previously recorded generated ToC totals: **25 chapters / 747 numbered sections** (this run checked the actual chapter-21 ToC but did not recount all chapters). No build, test suite, CI, or publication.
