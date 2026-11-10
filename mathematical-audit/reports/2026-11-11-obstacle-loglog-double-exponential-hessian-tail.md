# Mathematical audit — exact double-exponential Hessian tail in the bounded-metric-Laplacian obstacle

**Date:** 2026-11-11. **Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\`. **Stable finding:** \`POME-ENV-LOGLOG-HESSIAN-DOUBLEEXP-TAIL-001\`. **Severity:** low. **Status:** verified conditional deduction; no printed assertion is refuted, and no entire theorem chain is certified.

## Main reading-edition anchors and hypothesis boundaries

- **Directly inspected:** \`docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--obstacles-with-bounded-metric-laplacian/index.html\`, Git blob \`e9ce0caf7bd8b123062d9cb6fffd49fdfd0d5ffb\`.
- **Equation 16.14.1:** source \`foundations-of-pluripotential-theory:8C0DAB94\`, permanent tag \`B47D0EFD195A\`, physical lines **10–17**. The convention is \`Lf=-4π sum h^{i bar j} f_{i bar j}\` for the **nonnegative** metric Laplacian.
- **Example 16.14.2:** source \`foundations-of-pluripotential-theory:A21EFF6F\`, permanent tag \`74EA4AAF7D98\`, lines **20–46**. Its precise hypothesis is complex dimension **n >= 2**, fixed Kähler metric, a centered coordinate chart normalized by \`h_{i bar j}(0)=delta_ij\`, cutoff equal to one on a small ball, and
  \`f=chi (|z_1|^2-|z_2|^2) log(-log|z|)\`.
  The example establishes bounded metric Laplacian, but unbounded complex Hessian.
- **Lemma 16.14.4:** source \`foundations-of-pluripotential-theory:EC5E698D\`, permanent tag \`75E3F7AC3FA0\`, lines **66–113**; **Proposition 16.14.9:** source \`foundations-of-pluripotential-theory:71B5D060\`, permanent tag \`F9586D89B24F\`, lines **204–255**; **Corollary 16.14.11:** source \`foundations-of-pluripotential-theory:E96D4CC3\`, permanent tag \`E3B684F226D1\`, lines **260–278**. Their printed conclusions concern \`W^{2,p}\` for every *finite* \`p\` and weak Hessian wedge integrability; they assert no double-exponential endpoint.
- **Structural/background only:** \`docs/sections/envelopes-and-model-potentials/index.html\`, blob \`decb273ec97fcb9bb0ace2e0b90270723ecbea3e\`, introduction source \`foundations-of-pluripotential-theory:F1167A9F\`, permanent section tag \`CC5E34310EEC\`, physical lines **5–16**; this is expository, not a new proof-level section visit.

No Demailly approximation/regularization, specialized Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion argument is used.

## New explicit distribution theorem

Let \`n>=2\` and retain **exactly the local function and cutoff of printed Example 16.14.2**. Work on a fixed centered Euclidean ball \`B_rho\` with \`0<rho<r_0/2\`. Set
\[
r=|z|,\qquad L=-\log r,\qquad
H(z)=\partial_{z_1}\partial_{\bar z_1}f(z)
\]
as the a.e. weak complex-Hessian coefficient away from \`z=0\`. For a unit vector \(\zeta\in S^{2n-1}\), write
\[
a=|\zeta_1|^2,\quad b=|\zeta_2|^2,\quad
c(\zeta)=-a-\frac{a-b}{2}+\frac{(a-b)a}{2},
\quad d(\zeta)=(a-b)a.
\]
Then for every \`L>-\log rho\`, **exactly**
\[
\boxed{
H(e^{-L}\zeta)=\log L+\frac{c(\zeta)}{L}
                       -\frac{d(\zeta)}{4L^2}. }\tag{1}
\]
In particular \(\exp H=L+c(\zeta)+O(L^{-1})\), uniformly in the angular variable.

**Claim A (sharp Orlicz threshold for this coefficient).** For every real \(\lambda>0\),
\[
\boxed{\displaystyle
\int_{B_\rho}\exp\bigl(\lambda \exp(H(z))\bigr)\,dV_{2n}(z)<\infty
\quad\Longleftrightarrow\quad 0<\lambda<2n.}\tag{2}
\]
At \(\lambda=2n\), the integral diverges (not just for \(\lambda>2n\)). In contrast, \(\int_{B_\rho}\exp(pH)\,dV_{2n}<\infty\) for every finite \(p>0\), and all polynomial moments of \(H\) are finite.

**Claim B (exact high-threshold level-volume asymptotic).** With ordinary Euclidean volume in the chosen chart and its standard sphere area measure \(d\sigma\),
\[
\boxed{\displaystyle
\lim_{t\to\infty}e^{2ne^t}
\,\mathrm{Vol}_{2n}\{z\in B_\rho:H(z)>t\}
=\frac{1}{2n}\int_{S^{2n-1}}e^{2n c(\zeta)}\,d\sigma(\zeta)\in(0,\infty).}\tag{3}
\]
This is an **exact angular prefactor**, not just the estimate \(\mathrm{Vol}\asymp\exp(-2ne^t)\).

## Verification of the formula and both claims

Write \(\ell=\log L\), \(P=|z_1|^2-|z_2|^2\), and \(\phi=P\ell\). On \`B_rho\` the published cutoff is one and \(f=\phi\). With \(\partial_{z_1}P=\bar z_1\), \(P_{1\bar1}=1\) and
\[
\ell_{z_1}=-\frac{\bar z_1}{2r^2L},\qquad
\ell_{1\bar1}=-\frac1{2r^2L}
+\frac{(L-\tfrac12)|z_1|^2}{2r^4L^2},
\]
the product rule gives
\[
\begin{aligned}
H
 &=\ell+(\partial_{z_1}P)\ell_{\bar z_1}
       +(\partial_{\bar z_1}P)\ell_{z_1}+P\ell_{1\bar1}\\
 &=\log L-\frac{a}{L}-\frac{a-b}{2L}
 +\frac{(a-b)a}{2L}-\frac{(a-b)a}{4L^2},
\end{aligned}
\]
which proves (1) for all angular directions. These derivatives are the **distributional** derivatives by Example 16.14.2, physical lines **36–41**, not merely formal punctured-ball coefficients. The same printed calculation, lines **42–46**, gives bounded \(Lf\) using \(h^{1\bar1}-h^{2\bar2}=O(r)\); the cutoff shell is smooth. The computation does not require \(f\) to be psh.

Because \(a,b\in[0,1]\), \(|c|+|d|\) is uniformly bounded. Hence
\[
e^{H(e^{-L}\zeta)}
 =L\exp(c(\zeta)/L-d(\zeta)/(4L^2))
 =L+c(\zeta)+O(L^{-1})
\]
uniformly for \(L\to\infty\). There is a fixed \(C>0\) such that
\(L-C\le e^H\le L+C\) for all large \(L\). In polar coordinates
\(dV_{2n}=r^{2n-1}dr\,d\sigma=e^{-2nL}dL\,d\sigma\).
Thus the double-exponential integral is bounded from above and below,
up to positive constants, by \(\int^\infty e^{(\lambda-2n)L}\,dL\).
This proves the **if and only if**, including divergence at equality.
For each finite \(p\), \(e^{pH}\le C_p L^p\), proving the stated lower
integrability contrast.

For (3), the exact formula (1) is strictly increasing as a function of
\(L\), uniformly for sufficiently large \(L\):
\[
\partial_L H=\frac1L-\frac{c}{L^2}+\frac{d}{2L^3}>0.
\]
For every sufficiently large \(t\), each direction has a unique threshold
\(L_t(\zeta)\) with \(H(e^{-L_t}\zeta)=t\).
The preceding expansion is uniform in \(\zeta\) and gives
\[
L_t(\zeta)=e^t-c(\zeta)+O(e^{-t}).
\]
The radius interval with \(H>t\) is \(0<r<e^{-L_t(\zeta)}\).
Integrating its polar volume **exactly** gives
\[
\mathrm{Vol}_{2n}\{H>t\}
=\frac1{2n}\int_{S^{2n-1}}e^{-2nL_t(\zeta)}\,d\sigma(\zeta).
\]
The uniform remainder permits passage to the limit after multiplying
by \(e^{2ne^t}\), proving (3).

## Classification, corrections, dependents, and precise coverage

- **Low / verified conditional deduction, not a confirmed error.** The original Example 16.14.2, Proposition 16.14.9 and Corollary 16.14.11 remain correct in the inspected steps. The \(W^{2,p}\)-for-all-finite-\(p\) estimate neither implies nor asserts a general double-exponential bound; (2) is the **specific printed countermodel's exact threshold**. Do not generalize the numerical constant \(2n\) to arbitrary functions or coordinate normalizations.
- **Optional proposed text, NOT applied:** add after Example 16.14.2 a remark with (2) and (3). This makes the integrability strength/limitations of the \(L^\infty\)-Laplacian hypothesis quantitative without changing the original theorem or a permanent tag.
- **Affected dependents for future checks:** the Hessian-product interpretation of 16.14.11 and the envelope regularity tools in §§16.15–16.16 should use **finite-\(p\)** arguments, not an unproved global endpoint Orlicz claim. Their complete upstream PDE/weighted-capacity proof chains have **not** been re-certified.
- **Actual scope:** direct detailed local derivative, trace, and endpoint-integrability inspection of **Example 16.14.2 (lines 20–46)**; selected verification of **16.14.4, 16.14.9 and 16.14.11**; §16.10 introductory claims only, with no mathematical proof on that page. §16.14 had previous partial proof-level coverage: **0 newly first-visited numbered sections and 0 whole-section certifications**. The actual main ToC has **25 chapters / 747 numbered sections**; no other rows are claimed checked.
- The user-excluded Demailly regularization, Bergman, weighted L2, OT, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user**, not resolved. The audit changes no production source, math-body, registry, tags, canonicalization, main, CI, test, build or published website.
