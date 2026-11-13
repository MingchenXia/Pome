# Explicit minimal Martin boundary and representing measures of the upper half-space (2026-11-14)

**Finding:** \`POME-MART-HALFSPACE-ALL-MINIMAL-POISSON-001\`  
**Classification:** low / **verified conditional deduction**. The printed theorems are **not** counterexamples or confirmed errors. The geometry and asymptotics below are proved directly; the existence part of the representation invokes the already printed half-space representation theorem, which is not transitively certified in this audit.

## Immutable source record and scope

- Reviewed production \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated Chapter 4: \`docs/sections/green-energy-and-martin-boundaries/index.html\`, blob \`976a90f2a5eba299658f73a1eee8b9d3fef8020f\`: Martin normalization and cutoff, **line 106**; Theorem **4.5.9** source \`classical-potential-theory:1677A9F0\`, permanent \`9D6B5CF5E0CF\`, **lines 110–122**; Theorem **4.5.12** source \`classical-potential-theory:57D18B4C\`, permanent \`6736FBE7368C\`, **lines 166–185**; Theorem **4.5.13** source \`classical-potential-theory:854603A2\`, permanent \`0E65F552B1A6\`, **lines 190–213**, checked for the distinct ball model and topology.
- Integrated Chapter 3: \`docs/sections/kelvin-transforms-and-half-space-potentials/index.html\`, blob \`f2615a5393af724c3996978212162f94911ff9d9\`: Poisson kernel **(3.2.5)** \`classical-potential-theory:2C60ADF3\`, permanent \`21F1298C637C\`, **lines 57–62**; half-space representation Theorem **3.2.6**, source \`classical-potential-theory:1C8A330A\`, permanent \`6BC86EEF03A9\`, and integrability **(3.2.7)–(3.2.8)**, permanent \`F3ED29BBAD39\` / \`8F7C774A9D89\`, **lines 65–76**.
- Substantive newly selected proof-level work: the full explicit half-space Martin-boundary classification, normalized kernels, minimality and measure identification; inspection of the above original statements and normalization. The earlier **exterior-ball** model (2026-11-02) and 2026-11-13 vague half-space boundary trace are inputs/contrasts, not counted as new work.

## Statement

Let \(\Omega=H=\mathbb R^{d-1}\times(0,\infty)\), \(d\ge3\), \(a=(0,1)\). Take the Martin normalization in §4.5.7: \(b=\phi(G_H(\cdot,a))\), with \(b(y)=G_H(y,a)\) off a compact neighborhood of \(a\), and \(k_y(x)=G_H(y,x)/b(y)\). Then the associated compactification is homeomorphic to the **one-point compactification** of the Euclidean closed half-space. Its Martin boundary consists of \(\mathbb R^{d-1}\cup\{\infty\}\), with all boundary points minimal, and the normalized kernels are
\[
 K_\xi(x',t)=t\left(\frac{1+|\xi|^2}{|x'-\xi|^2+t^2}\right)^{d/2},
 \qquad K_\infty(x',t)=t.
 \tag{1}
\]
In particular \(K_\xi\to K_\infty\) locally uniformly as \(|\xi|\to\infty\).

For any nonnegative harmonic \(h\), the pair \((c,\nu)\) from printed (3.2.7) corresponds **exactly** to its finite normalized Martin measure
\[
 \boxed{\quad \mu_h=c\,\delta_\infty+
 P_H(a,\xi)\,d\nu(\xi),\qquad
 P_H(a,\xi)=\frac{2}{s_{d-1}}(1+|\xi|^2)^{-d/2};\quad}
 \tag{2}
\]
one has \(h(x)=\int K_y(x)\,d\mu_h(y)\) and \(\mu_h(\Delta)=h(a)<\infty\). Conversely every finite positive Borel measure on this compact boundary defines a positive harmonic function via (1). Equation (2) is a measure identity, not a claim that the possibly infinite-total-mass Radon measure \(\nu\) is finite.

## Proof, without unproved exchanges of limits

**1. Exact Green reflection and boundary asymptotics.** Write \(x=(x',t)\), \(y=(\eta,s)\), \(y^*=(\eta,-s)\), \(p=(d-2)/2\), \(c_d=1/((d-2)s_{d-1})\). The standard reflected fundamental solution, checked directly to vanish on \(t=0\), is
\[
 G_H(y,x)=c_d\bigl(A^{-p}-B^{-p}\bigr),\quad
 A=|x'-\eta|^2+(t-s)^2,\quad B=A+4ts.
 \tag{3}
\]
Its harmonicity and Riesz normalization follow from the fundamental-solution convention of §3.1, and uniqueness is the ordinary half-space Green uniqueness input; no positivity or constant is obtained by assuming Martin representation. For fixed \(x\in H\), as \(y\to(\xi,0)\),
\[
 \frac{G_H(y,x)}s\longrightarrow
 4c_dp\,\frac{t}{(|x'-\xi|^2+t^2)^{d/2}}
 =\frac{2}{s_{d-1}}\frac{t}{(|x'-\xi|^2+t^2)^{d/2}}
 =P_H(x,\xi).
 \tag{4}
\]
The convergence is uniform when \(x\) ranges in a compact subset of \(H\) and \(\xi\) stays in a fixed compact boundary set. Since \(b(y)=G_H(y,a)\) near the Euclidean boundary, taking ratios in (4) proves \(K_\xi=P_H(x,\xi)/P_H(a,\xi)\), the first formula in (1).

**2. The single infinity kernel, including tangential escapes.** The exact integral identity
\[
 G_H(y,x)=4c_dpts\int_0^1
 \bigl(|x-y|^2+4rts\bigr)^{-d/2}\,dr
 \tag{5}
\]
shows that, for \(x\) on an arbitrary fixed compact subset of \(H\),
\[
 G_H(y,x)=\frac{2}{s_{d-1}}\frac{ts}{|y|^d}(1+o(1))
 \quad\text{as }|y|\to\infty.
 \tag{6}
\]
The \(o(1)\) is uniform for such \(x\) and for \(0<s\le |y|\): all denominators in (5) equal \(|y|^2(1+o(1))\). Thus (6) covers both vertical and arbitrarily tangential approaches with \(s/|y|\to0\). Dividing the formula for \(x\) by its counterpart for \(a\), and using \(b(y)=G_H(y,a)\) outside a compact set, gives \(K_\infty=t\), with local uniform convergence. Also the finite-boundary formula satisfies \(K_\xi(x)\to t\) as \(|\xi|\to\infty\).

**3. Topology: no hidden Martin points.** Every escaping sequence \(y_j\in H\) has a subsequence either converging to a finite Euclidean boundary point or with \(|y_j|\to\infty\). Equations (4)–(6) identify the corresponding Martin-coordinate limits, locally uniformly on \(H\). Different finite points \(\xi\) have distinct normalized Poisson kernels (their singular boundary behavior differs), and none equals \(t\); distinct interior points are distinguished by their Green poles. Hence the continuous map from the compact Euclidean one-point closure to the compactification specified by Lemma 4.5.8 is injective and surjective, and therefore a homeomorphism. This directly realizes §4.5.9 in this model without assuming sequential compactness for an arbitrary Martin compactification.

**4. Minimality of every boundary point.** Invoke the printed Theorem 3.2.6 for the existence of \(h=ct+P_H\nu\), where \(\nu\) is positive Radon with the stated weight. Its boundary trace is uniquely \(\nu\), because \(h(\eta,s)d\eta\to\nu\) vaguely as \(s\downarrow0\): for \(f\in C_c\), split the Poisson integral into a compact \(\xi\)-region (approximate identity) and its complement (an \(O(s)\) bound by the weighted integral); the \(ct\) term tends to zero on compact tests. This elementary passage was established separately in the 2026-11-13 half-space audit and is invoked here only with its exact weighted hypothesis.

If \(0\le h\le K_\infty=t\), the vague boundary trace must vanish, giving \(\nu=0\) and \(h=ct\), \(0\le c\le1\). Thus \(K_\infty\) is minimal. If \(0\le h\le K_\xi=P_H(\cdot,\xi)/P_H(a,\xi)\), the same vague domination gives \(\nu\le \delta_\xi/P_H(a,\xi)\). The remaining \(ct\) term vanishes: as \(R\to\infty\), \(cR\le h(0,R)\le K_\xi(0,R)=O(R^{1-d})\), whence \(c=0\). Consequently \(h=\lambda K_\xi\), \(0\le\lambda\le1\). Every finite Martin point is minimal. This confirms \(\Delta_1=\Delta\) in the explicit model, **conditionally on** the printed positive harmonic representation rather than a circular appeal to Theorem 4.5.12.

**5. Precise representing measure, without finiteness assumption on \(\nu\).** Equation (1) rewrites the Poisson integral exactly as \(\int K_\xi P_H(a,\xi)\,d\nu(\xi)\); the remaining \(ct\) equals \(cK_\infty\). The weight (3.2.8) is exactly the finiteness condition on the first measure in (2). Its mass plus \(c\) is \(h(a)\). Uniqueness follows from the vague trace (recovering \(\nu\)) and from the large-height limit
\[
 c=\lim_{R\to\infty}\frac{h(0,R)}R.
\]
Indeed the divided Poisson integrand equals \((2/s_{d-1})(|\xi|^2+R^2)^{-d/2}\), tends to zero for each \(\xi\), and for \(R\ge1\) is bounded by the integrable weight in (3.2.8); dominated convergence applies. This also proves uniqueness of the normalized finite Martin measure in this model.

## Scope, status and dependents

- **No false theorem** and **no full section certificate**: the claimed addition is an exact half-space realization of the general §4.5.9/12/13 statements. The printed general Martin construction and all its analytic prerequisites are not transitively certified; Theorem 3.2.6's existence remains an identified upstream proof input. Formula (3)'s Green uniqueness and elementary Poisson approximate-identity property are explicit classical inputs, not Demailly regularization.
- **Proposed patch:** audit-only optional self-contained example after Theorem 4.5.13, with (1)–(2), the tangential infinity estimate (5)–(6), and the independence of finite \(\nu\)-mass. No source, canonicalization, permanent-tag or production edit is made.
- **Dependents:** the half-space instance of the Martin representation Theorem 4.5.12, boundary Perron Theorem 4.5.13 and the positive harmonic representation Theorem 3.2.6. No extension to general Greenian \(\Omega\), to \(d=2\), or to arbitrary signed harmonic data is claimed.
- **Audit counts:** §4.5 and §3.2 were previously partly proof-reviewed; newly first-visited numbered sections **0**, fully certified whole sections **0**; current production inventory **25 chapters / 747 sections**.
- **Explicitly deferred:** all Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Nothing in that scope is reopened, silently discharged or certified.
- No build, test, CI, GitHub Action, publishing or production/source edit was run.
