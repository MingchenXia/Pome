# Quantitative logarithmic mass of bounded Bedford–Taylor cone decompositions

**Date:** 2026-11-01. **Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Status:** selected, proof-level audit; no complete section or prerequisite-chain certification. **Severity:** low.
**Finding:** **POME-BT-LOGMASS-ASYMPTOTIC-001 — verified conditional deduction**. The printed proposition is not false, and the proposed strengthening has **not** been incorporated into the reading edition.

## Exact reading-edition anchors and scope

- **Main path:** \`docs/sections/unbounded-potentials-and-dependence-on-regularization/index.html\`; pinned main blob \`431e66dcee4efdf3c4aac592aaee1490156da2b9\`.
- **Section §7.23:** source \`klimek-pluripotential-theory:91597462\`, permanent \`32DC47BECC3E\`, physical line 5.
- **Example 7.23.1:** source \`klimek-pluripotential-theory:6E737739\`, permanent \`20D8C7C9B243\`, physical lines 7–41.
- **Proposition 7.23.2 (principal review):** source \`klimek-pluripotential-theory:80EFAB5F\`, permanent \`EC436652E435\`, statement lines 45–46; local Hessian/gradient argument lines 51–98; bounded cone decomposition lines 100–119; positivity and contradiction lines 120–132.
- **Example 7.23.3:** source \`klimek-pluripotential-theory:8EC23CC0\`, permanent \`C89C030AFB89\`, physical lines 137–145.
- **Contextual, introductory-only first reads:** \`docs/sections/bedford-taylor-products-and-local-capacity/index.html\`, §7.1, main blob \`41bc964bad8bf8505892c2cb3762e5cce2071ae6\`, source \`foundations-of-pluripotential-theory:6DA2347F\`, permanent \`2F5912FF9FEA\`, lines 7–16; and \`docs/sections/complex-spaces-and-modifications/index.html\`, §9.1, blob \`65a26de54d52679ab76f293f0fc75795d38a3822\`, source \`foundations-of-pluripotential-theory:1823FC9F\`, permanent \`B64C7FEAE2E7\`, lines 7–16. These two pages are introductions, **not newly certified theorem proofs**.

This audit treats the **elementary failure of unrestricted unbounded Bedford–Taylor products**. Although the title of §7.23 refers to dependence on regularization, it does **not** revisit Demailly approximation or its dedicated Bergman/L²/OT/multiscale/positivity-loss programme, which remains **deferred-by-user**.

## Printed statements: independent mathematical checks

The two smooth decreasing sequences in Example 7.23.1 have different limiting top wedge measures for the same singular potential. For \(F(z)=z_1\cdots z_n\), the Hermitian matrix of \(\log(|F|^2+\varepsilon)\) is \(\varepsilon\,\partial F\,(\partial F)^*/(|F|^2+\varepsilon)^2\) and has rank at most one, so its top wedge vanishes when \(n\ge2\). For the coordinatewise smoothing, \(dd^c\log(|z|^2+\varepsilon)=\varepsilon\,dA/(\pi(|z|^2+\varepsilon)^2)\) has mass \(R^2/(R^2+\varepsilon)\) on the radius-\(R\) disk. The \(n\) coordinate currents therefore give \(n!\delta_0\), including the required factorial and the normalization \(dd^c=i\partial\bar\partial/(2\pi)\). This checks the specified model but not every source-level monotone-continuity dependency.

In Example 7.23.3, \(u=\log|z|\) has top isolated-point classical mass \(2^{-n}\delta_0\), whereas the non-pluripolar truncation discards all pole-supported mass; the ordinary smooth Hessian has rank \(n-1\) on \(\mathbb C^n\setminus\{0\}\). The two constructions are **different products on unbounded inputs**, not duplicate versions to canonicalize or contradictory claims. In dimension one, the distributional \(dd^cu\) is a Radon measure but the non-pluripolar convention still removes the atom.

## New quantitative statement

Keep **exactly the displayed local model and bounded cone decomposition** of Proposition 7.23.2. On
\[
 \Omega=\{|x|<1/4,\ |y|<e^{-1},\ |z'|<1\}\subset\mathbb C^2\times\mathbb C^{n-2},
\]
write \(L=-\log|y|\), \(u=(|x|^2-1)\sqrt L\) for \(y\ne0\), and
\[
 U=u+|z'|^2-2,\qquad
 \kappa=\frac1{18},\qquad
 f_j(s)=\frac{\kappa j s}{j-s},\qquad \psi_j=f_j(U).
\]
The \(z'\)-terms and their factors are omitted for \(n=2\). On \(y=0\), \(\psi_j=-\kappa j\). The printed argument proves that \(\psi_j\) is locally bounded psh, \(U-\psi_j\) is psh, and \(U=\psi_j+(U-\psi_j)\).

Fix \(0<a<1/4\), \(0<R<e^{-1}\), and, when \(n>2\), \(0<b<1\). Let
\[
 K_{a,b,R}=\{|x|\le a,\ |y|\le R,\ |z'|\le b\}\Subset\Omega,
\]
where \(K_{a,b,R}=\{|x|\le a,|y|\le R\}\) for \(n=2\). Then
\[
 \boxed{\displaystyle
 \lim_{j\to\infty}\frac{1}{\log j}
 \int_{K_{a,b,R}}(dd^c\psi_j)^n
 =
 \frac{n(n-1)}4\,\kappa^n(a^2-a^4)b^{2(n-2)}.}
 \tag{*}
\]
For \(n=2\) the factor \(b^{2(n-2)}\) is \(1\), and the constant reduces to \(\kappa^2(a^2-a^4)/2\). The leading logarithmic coefficient is independent of the fixed inner \(y\)-radius \(R\). Consequently the printed **qualitative infinite-mass contradiction has an explicit logarithmic growth rate** already on each such compact product set.

### Full calculation of (*)

**1. Strict positivity and the gradient control.** Off \(y=0\), \(H_U\) is strictly positive definite; \(H_U=\operatorname{diag}(H_u,I_{n-2})\), where the printed exact determinant (lines 60–69) is
\[
 \det H_U=\frac{1-2|x|^2}{16|y|^2L}.
\]
Its printed pointwise gradient estimate (lines 72–95) is
\[
 |\partial U(v)|^2\le4(-U)H_U(v,\bar v).
\]
Put \(\sigma=-U=(1-|x|^2)\sqrt L+2-|z'|^2\) and
\(Q=(\partial U)^*H_U^{-1}\partial U\). Thus
\[
 0\le Q\le4\sigma,\qquad
 (1-a^2)\sqrt L\le\sigma\le\sqrt L+2
\]
uniformly on the chosen product set.

**2. Exact density.** By the chain rule and the rank-one determinant identity,
\[
 H_{\psi_j}=f'_j(U)H_U+f''_j(U)\,\partial U(\partial U)^*,
\quad
 \det H_{\psi_j}=(f'_j(U))^n\det H_U
       \left(1+\frac{f''_j(U)}{f'_j(U)}Q\right).
\]
Here
\[
 f'_j(U)=\frac{\kappa j^2}{(j+\sigma)^2},
 \qquad \frac{f''_j(U)}{f'_j(U)}=\frac{2}{j+\sigma}.
\]
Consequently, with Euclidean volume \(dV_{2n}\),
\[
 (dd^c\psi_j)^n
 =\frac{n!}{16\pi^n}
   \frac{1-2|x|^2}{|y|^2L}\,
   F_j(L,x,z')\,dV_{2n},\qquad
 F_j=\left(\frac{\kappa j^2}{(j+\sigma)^2}\right)^n
      \left(1+\frac{2Q}{j+\sigma}\right)
\]
on \(y\ne0\). The **locally bounded** Bedford–Taylor product does not charge the pluripolar hypersurface \(\{y=0\}\). This established bounded-product non-charging property is an explicit upstream dependency, **not independently re-proved or certified in this run**; it ensures that the smooth-density integral gives the entire measure of \(K_{a,b,R}\).

**3. Logarithmic shell asymptotics, uniformly in the transverse variables.** Set \(L_0=-\log R>1\). The \(y\)-polar area formula yields
\[
 \frac{dA_y}{|y|^2L}=2\pi\,\frac{dL}{L}.
\]
For each fixed \(0<\epsilon<1\), on \(L_0\le L\le j^{2-\epsilon}\) one has \(\sigma=O(j^{1-\epsilon/2})\), \(Q\le4\sigma\), and hence \(F_j=\kappa^n(1+o(1))\) **uniformly** for \(|x|\le a,|z'|\le b\). The logarithmic length of this interval is \((2-\epsilon)\log j+O(1)\).

On the transition interval \(j^{2-\epsilon}<L<j^2\), the inequalities \(f'_j\le\kappa\) and \(Q\le4\sigma\) give \(0\le F_j\le9\kappa^n\), so the contribution divided by \(\log j\) is bounded by \(9\kappa^n\epsilon\). On \(L\ge j^2\), the lower bound \(\sigma\ge(1-a^2)\sqrt L\) gives
\[
 F_j\le9\kappa^n(1-a^2)^{-2n}(j^2/L)^n,
\]
whose integral against \(dL/L\) is \(O(1)\), uniformly in \(j,x,z'\), since \(\int_{j^2}^\infty(j^2/L)^n\,dL/L=1/n\).

Let \(j\to\infty\), then \(\epsilon\downarrow0\). The lower and upper estimates prove, uniformly over the transverse product,
\[
 \frac1{\log j}\int_{L_0}^\infty F_j(L,x,z')\,\frac{dL}{L}
 \longrightarrow 2\kappa^n .
\]
No exchange of a divergent integral with a pointwise limit, or uncontrolled uniform-integrability assertion, occurs.

**4. Exact integration and the \(n!\) factor.** The remaining transverse integrals are
\[
 \int_{|x|\le a}(1-2|x|^2)dA_x=\pi(a^2-a^4),
 \qquad
 \operatorname{vol}_{2(n-2)}\{|z'|\le b\}
       =\frac{\pi^{n-2}b^{2(n-2)}}{(n-2)!}.
\]
Multiplying by the density factor \(n!/(16\pi^n)\), by \(2\pi\) from \(y\), and by \(2\kappa^n\) from the logarithmic shell gives
\[
 \frac{n!}{16\pi^n}\cdot2\pi\cdot2\kappa^n
       \cdot\pi(a^2-a^4)\cdot
       \frac{\pi^{n-2}b^{2(n-2)}}{(n-2)!}
 =\frac{n(n-1)}4\kappa^n(a^2-a^4)b^{2(n-2)}.
\]
This proves (*), subject only to the explicitly stated locally bounded Bedford–Taylor non-charging input.

## Interpretation, severity and disposition

- **Finding ID:** \`POME-BT-LOGMASS-ASYMPTOTIC-001\`.
- **Severity/status:** **low / verified conditional deduction**; this is neither a false theorem nor a newly discovered proof gap. It sharpens the *example used inside the proof* of the correct Proposition 7.23.2.
- **Proposed production correction:** optional quantitative remark following the obstruction proof, with the constant, compact restrictions, normalization and dependency stated exactly; **no production/body, source, registry, tag or canonicalization edit authorized in this audit**.
- **Affected dependents:** interpretations of how severely unrestricted positive \(n\)-linear BT extensions fail (§7.23.2), and the distinction between classical and non-pluripolar products (§7.23.3, §13.1). It **does not** extend the BT product to unbounded potentials or establish any Demailly regularization result.
- **Conditional dependencies:** the local \(C^2\) determinant/gradient bounds printed in §7.23.2 are checked algebraically for this model; the general locally bounded Bedford–Taylor non-charging-of-pluripolar-sets statement (§§7.2–7.5) is used only as a stated established premise. No upstream complete section is declared certified.
- **Actual new coverage:** §7.23.1/.2/.3 selected normalization, positivity and measure proofs, with the new quantitative local-mass argument; §§7.1 and 9.1 were opened as contextual *expository-only* current-main pages. No completed theorem dependency chain.
- **Project-level audit state:** the matrix remains **25 chapters / 747 numbered current-main sections / zero entire mathematical sections certified**; all historical findings and deferred-by-user work persist unchanged.
- **Execution boundary:** no complete repository build, project test suite, CI, formalization, website publication, main/source change, or external service. The only proposed write is audit Markdown on \`review/mathematical-audit\`.
