# Finite polar punctures: Perron invariance, harmonic measure, and the strict boundary-zero Green obstruction

**Finding:** POME-CLASS-FINITE-PUNCTURE-PERRON-HMEASURE-GREEN-001  
**Date:** 2026-11-12  
**Severity / status:** low / **verified conditional deduction** (the printed theorems are not refuted).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading edition:** \`docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html\`, blob \`fc02188d6e246a21aa07acd8bf6d3712761ba6e5\`.

## Precisely reviewed source anchors

- The bounded-domain comparison and Perron setup: Lemma **3.1.24**, source \`foundations-of-pluripotential-theory:5564A480\`, permanent tag \`3F83842AEB11\`, physical lines **486–509**.
- Harmonicity, linearity and boundary comparison of the Perron envelope: Theorems **3.1.25 / 3.1.27**, sources \`foundations-of-pluripotential-theory:6EC9A4AF\` / \`:2949A188\`, permanent tags \`537ACE84788C\` / \`8FE1B604CDA2\`, physical lines **512–530 / 551–579**.
- Regularity/barrier criterion and the *single*-puncture example: Theorem **3.1.29**, source \`:3442F8BF\`, permanent tag \`C1B72E118338\`, lines **589–617**; Example **3.1.31**, source \`:71FEA63C\`, permanent tag \`8C85C3D68394\`, lines **636–640**.
- The regular-domain harmonic measure and Green assertions: Proposition **3.1.33**, source \`:37E4271C\`, permanent tag \`C5D6FBB32967\`, lines **650–669**; Theorem **3.1.34**, source \`:497FD574\`, permanent tag \`476CFD04AAC6\`, lines **671–735**. The ball Poisson solution is Theorem **3.1.18**, source \`:330E7C21\`, permanent tag \`08ED9D7CF1CF\`, lines **329–365**.

All colon-prefixed labels above are from \`foundations-of-pluripotential-theory\`.

## Statement and exact scope

Let \(d\ge 2\), let \(B=B(0,1)\subset\mathbb R^d\), and let \(F=\{a_1,\dots,a_m\}\subset B\) be a **nonempty finite set of distinct points**. Put \(\Omega=B\setminus F\). Then \(\Omega\) is a bounded connected domain and \(\partial\Omega=\partial B\sqcup F\), where every puncture is an isolated point of the boundary.

For every real \(f\in C(\partial\Omega)\), with the *bounded-domain* Perron envelope defined in §3.1.23,
\[
\boxed{U_f^\Omega(x)=H_B(f|_{\partial B})(x)\qquad(x\in\Omega).} \tag{A}
\]
Thus *arbitrary* changes in the boundary values at the finitely many punctures leave the interior solution unchanged. The unique representing probability measure for the positive linear functional \(f\mapsto U_f^\Omega(x)\) on \(C(\partial\Omega)\) is
\[
\boxed{\omega_x^\Omega=\iota_*\omega_x^B,\quad
\omega_x^\Omega(F)=0,} \tag{B}
\]
where \(\iota:\partial B\hookrightarrow\partial\Omega\) is inclusion and \(\omega_x^B\) is the ball's Poisson harmonic measure.

The restriction **to regular domains** in the formulation of printed Theorem 3.1.34 is essential for its *zero limit at every boundary point* characterization. In fact, fix \(x\in\Omega\). There exists **no** locally integrable \(G\) on \(\Omega\), harmonic on \(\Omega\setminus\{x\}\), with \(-\Delta G=\delta_x\) on \(\Omega\), and limits \(G(y)\to0\) at **every** point of \(\partial\Omega\). This is **not** a denial of the usual Green function on the irregular domain: its limit at a deleted polar point need not vanish.

## Detailed proof of (A)

The explicit radial fundamental solution \(\Gamma_d(r)\) appearing in Proposition 3.1.13 is strictly decreasing in \(r>0\), harmonic away from its pole, and tends to \(+\infty\) as \(r\downarrow0\) for \(d\ge2\). Define on \(\Omega\)
\[
g_i(y)=\Gamma_d(|y-a_i|)-\Gamma_d(1+|a_i|),\qquad
g(y)=\sum_{i=1}^m g_i(y).
\]
Because \(|y-a_i|<1+|a_i|\) for \(y\in B\), all \(g_i>0\) on \(\Omega\). The function \(g\) is harmonic on \(\Omega\), nonnegative even at the outer sphere in the sense of boundary limits, and blows up at every \(a_i\).

First let \(h\in C(\partial\Omega)\) be **nonnegative and supported on \(F\)**, i.e. \(h=0\) on \(\partial B\). For \(v\in\mathcal S_h^\Omega\), Lemma 3.1.24 gives \(v\le M:=\max_{\partial\Omega}h\). Fix \(\varepsilon>0\). Choose mutually disjoint closed balls \(\overline{B(a_i,\delta_i)}\subset B\) so small that \(\varepsilon g\ge M\) on every inner boundary sphere; this is possible because each \(g_i\to+\infty\) uniformly as \(|y-a_i|=\delta_i\downarrow0\). On the bounded open domain
\[
\Omega_{\boldsymbol\delta}
 =B\setminus\bigcup_i\overline{B(a_i,\delta_i)}
\]
the function \(v-\varepsilon g\) is a continuous subsolution: subtracting the harmonic \(\varepsilon g\) preserves subsolutions. At the outer sphere its boundary upper limit is at most \(0\), since \(h=0\) there and \(g\ge0\); at each inner sphere it is at most \(M-\varepsilon g\le0\). Lemma 3.1.24 now gives \(v\le\varepsilon g\) throughout \(\Omega_{\boldsymbol\delta}\). Shrinking the finitely many radii to zero gives \(v\le\varepsilon g\) on all of \(\Omega\), and then \(\varepsilon\downarrow0\) yields \(v\le0\). Since \(0\in\mathcal S_h^\Omega\), \(U_h^\Omega=0\). Decomposing any **signed** datum supported on \(F\) into its positive and negative parts and using the proven linearity of \(U\) (Theorem 3.1.27), we conclude
\[
U_h^\Omega=0\quad\text{for every real }h
 \text{ with }h|_{\partial B}=0. \tag{C}
\]

For arbitrary \(f\in C(\partial\Omega)\), put \(\varphi=f|_{\partial B}\) and \(H=H_B\varphi\). The ball is regular by Theorem 3.1.29, hence \(H\in C(\overline B)\) is harmonic on \(B\). Define \(f_H\in C(\partial\Omega)\) by \(f_H=\varphi\) on \(\partial B\) and \(f_H(a_i)=H(a_i)\) for each puncture. Theorem 3.1.25 yields \(U_{f_H}^\Omega=H|_\Omega\), since \(H|_\Omega\) is harmonic with the prescribed continuous extension to \(\partial\Omega\). The function \(f-f_H\) is supported on \(F\), so (C) and Theorem 3.1.27 show \(U_f^\Omega=U_{f_H}^\Omega+U_{f-f_H}^\Omega=H|_\Omega\). This proves (A) without any invocation of regularization.

## Proof of (B)

For each \(x\in\Omega\), the ball Poisson harmonic measure \(\omega_x^B\) is a probability on \(\partial B\) representing \(H_B\varphi(x)\), by Theorem 3.1.18 and Proposition 3.1.33 **on the regular ball**. Its pushforward by inclusion therefore represents \(U_f^\Omega(x)\) for every \(f\in C(\partial\Omega)\), by (A). Any two finite Borel probability measures on the compact boundary \(\partial\Omega\) agreeing on all continuous functions coincide, by the uniqueness part of the Riesz representation used in §2.3. Thus (B) is exact. We have **not** applied the printed Proposition 3.1.33 directly to an irregular domain; rather, its representing measure is constructed independently in this explicit case.

## Proof of the sharp Green boundary obstruction

**Removability lemma (proved here).** If \(u\) is harmonic on \(B(a,r)\setminus\{a\}\) in \(d\ge2\), and is bounded near \(a\), then it extends harmonically across \(a\). Take a smaller closed ball contained in the original one and let \(h\) be the Poisson extension of the continuous boundary values of \(u\) there. Then \(w=u-h\) is bounded and harmonic on its punctured interior, with zero values on the outer sphere. The positive harmonic function \(\psi(y)=\Gamma_d(|y-a|)-\Gamma_d(r')\) blows up at \(a\) and vanishes on that sphere. For every \(\varepsilon>0\), on a sufficiently small inner sphere, both \(w-\varepsilon\psi\) and \(-w-\varepsilon\psi\) are nonpositive, and they have zero outer boundary limits. The harmonic maximum principle on the intervening annulus yields \(|w|\le\varepsilon\psi\). Shrinking the inner sphere and then letting \(\varepsilon\downarrow0\) gives \(w\equiv0\); thus \(u=h\) and is removable. This argument uses only printed harmonic comparison and ball Poisson solutions.

Suppose the asserted strict boundary-zero \(G\) existed for \(x\in B\setminus F\). Near each \(a_i\), it is harmonic and tends to \(0\), hence bounded and removable by the lemma. Its harmonic extension across each puncture takes value \(0\) at that puncture. The resulting \(\widetilde G\) is locally integrable in \(B\), harmonic off \(x\), satisfies \(-\Delta\widetilde G=\delta_x\) on \(B\) (no new atoms at the removable points), and has zero limits on \(\partial B\). The uniqueness clause of Theorem 3.1.34 **applied to the regular ball** then forces \(\widetilde G(y)=G_B(x,y)\) for \(y\ne x\). But the same theorem gives \(G_B(x,a_i)>0\) for every \(a_i\ne x\), contradicting \(\widetilde G(a_i)=0\). Hence no such \(G\) exists.

## Classification, limits, proposed editorial action

**Classification:** verified conditional deduction, **not** confirmed error in the printed propositions. The known single-puncture Example 3.1.31 is not relogged: the new content is the finite-set invariance of **all** continuous Perron data, the precise representing harmonic measure, and a separately proved obstruction to exporting the *regular-domain* Green boundary characterization to those irregular domains.

**Dependencies actually used:** §3.1.13 fundamental solution; §3.1.18 ball Poisson solution; §3.1.24 comparison; §§3.1.25/27 Perron harmonicity and linearity; §3.1.34 regular-ball uniqueness/positivity; §2.3 Riesz uniqueness. These dependencies were inspected only as indicated, **not transitively certified**. The removable-point proof is included in full. No Demailly approximation/regularization, Bergman, \(L^2\), OT, multiscale, or positivity-loss work was touched.

**Suggested correction/addition (not applied):** add a note after §3.1.31 on finite polar puncture invariance; when citing §3.1.33 for an irregular domain, state separately the available positive functional and representing measure; retain the regularity hypothesis in §3.1.34 and explain that a classical Green function on a punctured domain need not have zero pointwise limits at polar boundary points.

**Affected downstream reading:** boundary-regularity and barrier discussions in §3.1; any use of §3.1.33 on nonregular domains; §3.1.34 Green boundary-limit claims. No specific downstream theorem has yet been certified as incorrect.

**Actual coverage:** direct new proof-level reading of the specified assertions/proof steps in **§3.1**; the section has historical partial audits, so **0 newly first-visited numbered sections**, **0 fully certified sections**. Current production ToC: **25 chapters / 747 numbered sections**. Neither the entire chapter nor the whole project is verified. No project build, tests, CI, website publication, or source modification was performed.
