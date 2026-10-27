# 2026-10-27 — Uniform Hölder-reference Monge–Ampère interpolation and the curve boundary of Gauduchon determinant separation

**Reviewed integrated reading-edition \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit head at the start of this session:** \`c5174d2febe6dbc34110438dba394fec5b3e2f56\`. **Scope:** first *selected*, not exhaustive, proof-level inspection of §§9.50, 10.97, 15.25 and the already-integrated statements used explicitly below. No whole section or transitive upstream analytic result is certified. All dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**, untouched.

## POME-HOLDER-DOMINATED-MA-UNIFORM-INTERPOLATION-001

**Status:** verified conditional deduction. **Severity:** low (useful quantitative strengthening; no false printed theorem).

**Exact integrated anchors:** \`docs/sections/equations-with-prescribed-singularities--the-homogeneous-equation-with-a-holder-reference/index.html\`, blob \`0defdec5270db7ff34625b638c9ac2a31264ca4a\`, Theorem 15.25.1, source \`non-kahler-pluripotential-theory-6A4C8C89\`, permanent tag \`8CE230CD94D4\`, physical lines 10–19 and proof lines 25–70, especially the capacity/Hölder/stability chain at 47–69. The exact established inputs are \`docs/sections/plurisubharmonic-functions-and-singularities--hermitian-capacity/index.html\`, blob \`77a9098e9bb922425d11c5b04d8927a3997ad44e\`, Corollary 5.29.9 permanent tag \`F701C1999BDC\`, lines 165–176, and Proposition 5.29.13 tag \`D00B685B1791\`, lines 261–282; and \`docs/sections/continuous-solutions-and-normalization/index.html\`, blob \`e4a9ece552056fdc387f170362cc1cc5c5fd4091\`, Proposition 14.19.23 tag \`3B70BD39881D\`, lines 370–408. Those named inputs are assumed with their printed hypotheses, not independently certified in full here.

**Additional precise assertion.** Fix a connected compact complex Hermitian $n$-fold $(X,h)$, $n\ge1$, a smooth positive volume form $\mathrm dV$, and constants $0<\alpha\le1$, $N,M>0$ and $H\ge1$. Let $I$ be an **arbitrary index set**, and for each $i\in I$ let
\[
 \varphi_i\in\mathrm{PSH}(X,h)\cap C(X),\quad
 \sup_X\varphi_i=0,\quad -H\le\varphi_i\le0,
\]
and let $v_i\in\mathrm{PSH}(X,h)\cap C^{0,\alpha}(X)$ have uniformly bounded $C^{0,\alpha}$ norm $\|v_i\|_{C^{0,\alpha}}\le N$. Assume, for every $i$,
\[
 \mu_i=(h+dd^c\varphi_i)^n\ \le\ M(h+dd^cv_i)^n.
\]
Then a constant $C=C(X,h,\mathrm dV,\alpha,N,M,H)$ independent of $i,j$ satisfies
\[
 \boxed{\|\varphi_i-\varphi_j\|_{C^0(X)}
 \le C\,\|\varphi_i-\varphi_j\|_{L^1(\mathrm dV)}^{\beta}},
 \qquad
 \boxed{\beta=\frac{\alpha}{(\alpha+2n)(6n+1)}}.
\]
In particular, the implication from $L^1$ Cauchyness to **uniform Cauchyness** holds for any family/net under these common bounds; no sequential compactness or unjustified exchange of limits is needed.

**Complete conditional derivation.** Proposition 5.29.13, applied uniformly to the given $v_i$, gives $(h+dd^cv_i)^n(E)\le C_2\operatorname{Cap}_h(E)^2$ for every Borel $E$, with $C_2$ independent of $i$. Hence $\mu_i(E)\le MC_2\operatorname{Cap}_h(E)^2$. Corollary 5.29.9, applied with the two bounded functions $\varphi_i,\varphi_j$ (common smooth lower curvature bound $-h$), gives
\[
 \int_X|\varphi_i-\varphi_j|\,\mathrm d\mu_i
 \le MC_3\|\varphi_i-\varphi_j\|_{L^1(\mathrm dV)}^{\alpha/(\alpha+2n)}.
\]
Apply Proposition 14.19.23 with its normalized $u=\varphi_i$, competitor $v=\varphi_j$, capacity exponent $\alpha_{\rm cap}=1$, uniform $A=MC_2$ and the stated $H$. Its stability exponent is precisely $1/(6n+1)$:
\[
 \sup_X(\varphi_j-\varphi_i)_+
 \le C_4\!\left(\int_X(\varphi_j-\varphi_i)_+\,\mathrm d\mu_i\right)^{1/(6n+1)}
 \le C_5\|\varphi_i-\varphi_j\|_{L^1}^{\beta}.
\]
Exchange $i,j$ to bound the other sign. The maximum of the two bounds proves the displayed estimate, including the zero-error case. No continuity of $i\mapsto v_i$, common Monge–Ampère mass, or sequence assumption is used.

**Disposition/proposed addition:** A short quantified lemma immediately before or after Theorem 15.25.1, or after Proposition 14.19.23, would make the pairwise modulus used in its Step 3 explicit. Affects the uniform limiting argument in §15.25 and applications of §14.19.23 to uniformly Hölder-dominated varying measures. **Exclusion boundary:** Theorem 15.25.1 Step 1 invokes Lemma 5.42.7 for smooth approximants (a user-deferred regularization dependency). This report **does not inspect, complete, validate, or reopen that proof**, and the asserted pairwise inequality only assumes its stated Hölder references already exist.

## POME-GAUD-DETERMINANT-DIM1-EXACT-001

**Status:** verified conditional deduction. **Severity:** low (exact dimension-one extension and equality rigidity, not a correction to the $n\ge2$ statement).

**Exact integrated anchors:** \`docs/sections/determinant-bounds-and-gauduchon-separation/index.html\`, main blob \`21ee4c9d517250bec607fa5ebd5630b41a7bd658\`; Lemma 10.97.1, source \`transcendental-positive-cones-6F0D5B86\`, permanent tag \`EFEC3AC4D264\`, lines 10–40; Proposition 10.97.4, source \`transcendental-positive-cones-538E99DD\`, tag \`970E2C8817B1\`, hypotheses lines 44–55, Hahn–Banach proof 60–112. The proposition itself deliberately assumes $n\ge2$.

**Additional exact one-dimensional statement.** Let $X$ be a connected compact Riemann surface, $\psi$ a smooth real $(1,1)$-form (automatically closed), and $\nu$ a smooth strictly positive $(1,1)$-form. The following are equivalent:

1. For **every** Gauduchon metric $\chi$ there exists a positive real $(1,1)$-current $\xi_\chi$ such that $(\xi_{\chi,\mathrm{ac}})^1\ge\nu$ and $\int_X\xi_{\chi,\mathrm{ac}}\wedge\chi^0\le\int_X\psi\wedge\chi^0$.
2. $\int_X\psi\ge\int_X\nu$.
3. There exists a **smooth** positive representative $R=\psi+dd^cu$ with $R\ge\nu$.

If $\int_X\psi=\int_X\nu$, every positive current in the class $\psi+dd^c\mathcal D'(X)$ whose absolutely continuous part dominates $\nu$ is necessarily **exactly** $R=\nu$; the potential is unique modulo constants.

**Proof.** In complex dimension one, $\chi^{n-1}=\chi^0=1$ and every Hermitian metric is Gauduchon, so the testing inequality is independent of $\chi$. For a positive current, $\xi_{\chi,\mathrm{ac}}\ge\nu$ implies $\int_X\xi_{\chi,\mathrm{ac}}\ge\int_X\nu$, proving (1)$\Rightarrow$(2). Conversely, (2) makes the fixed smooth $\xi_\chi=\nu$ an admissible witness for every $\chi$, proving (2)$\Rightarrow$(1). Choose an arbitrary smooth positive $(1,1)$-form $\omega_0$ with $\int_X\omega_0=1$ and set $a=\int_X\psi-\int_X\nu\ge0$ and $R=\nu+a\omega_0$. Then $R\ge\nu$ and $\int_X(R-\psi)=0$. On the compact connected Riemann surface, every smooth real $(1,1)$-form of total integral zero is $dd^c$ of a smooth real function: write it as a zero-average scalar times $\omega_0$ and solve the zero-average Laplace equation using its Green operator (unique modulo constants). Thus $R=\psi+dd^cu$, proving (2)$\Rightarrow$(3). Finally (3) clearly implies (2) by integrating. In the equality case any admissible positive current $S$ has decomposition $S=S_{\mathrm{ac}}+S_s$, with $S_{\mathrm{ac}}\ge\nu$ and $S_s\ge0$; total mass $\int_X S=\int_X\psi=\int_X\nu$ forces both $S_s=0$ and $S_{\mathrm{ac}}=\nu$. Its $dd^c$ potential differs from that of $\nu$ only by a global harmonic function and hence by a constant. No higher-dimensional current-separation argument is imported.

**Disposition/proposed addition:** a dimension-one addendum after Proposition 10.97.4 recording the exact mass condition and equality rigidity, retaining the original $n\ge2$ Gauduchon separation proof and attribution. Potential dependents: determinant-current duality and its endpoint cases. This is **not** a claim that an arbitrary $n\ge2$ determinant bound reduces to total volume.

## Independent selected scope check: §9.50 (no additional finding ID)

The integrated \`docs/sections/convex-neighborhoods-and-coherent-vanishing--bundle-cohomology-on-strongly-convex-exhaustions/index.html\`, main blob \`dad21663dd676575d42f1b996e7c900285ec878c\`, was read at Lemma 9.50.1 (source \`demailly-complex-geometry-50D3C93C\`, permanent tag \`8646B8C271A2\`, lines 10–41), Lemma 9.50.3 (\`demailly-complex-geometry-B90E56CE\`, \`E85E2E5CB1FF\`, lines 45–84), Theorem 9.50.5 (\`demailly-complex-geometry-C29780EC\`, \`8AB8E8F1EBBE\`, lines 88–156) and Theorem 9.50.8 (\`demailly-complex-geometry-059052F5\`, \`7B8A55FF470A\`, lines 160–178). Selected checks: the spectral construction uses a smooth local lower bound for the $q$th eigenvalue and produces $\gamma_q=\cdots=\gamma_n=1$; the conformal factor makes the exhaustion Lipschitz and the metric complete; the weighted bundle curvature trace is positive on degrees $\ge q$. The complete-Hermitian Hilbert-complex $L^2$ input is **not reopened or certified**, and no full vanishing theorem is certified.

Sharp distinction in Theorem 9.50.8: **density is not surjectivity**. With $M=\mathbb C$, $U=\{|z|<1\}$, $q=1$, $E$ trivial and exhaustion $\psi(z)=|z|^2$, every compact $L\Subset U$ lies in $\{\psi<b\}\Subset U$ for some $b<1$, so the stated $1$-Runge condition holds. The holomorphic function $h(z)=1/(1-z)$ does not extend to an entire function: if $F$ extended it, $(1-z)F(z)$ would be identically $1$ but would vanish at $z=1$. Yet the global polynomials $\sum_{k=0}^N z^k$ converge with every derivative uniformly on compact subsets of $U$. This verifies exactly the claimed Fréchet-density scope without inventing a surjectivity theorem or treating the example as a newly false Pome theorem.

## Coverage, distinctions, and integrity

Exactly **three** previously inventory-only ToC rows, §§9.50, 10.97 and 15.25, receive the selected anchors above. The §5.29 and §14.19 statements are previously existing conditional dependencies, **not** new full-section audits. The actual matrix retains **747** distinct ToC section identifiers; no complete-section certification. Neither printed theorem is disproved. Both stable findings are **low / verified conditional deduction**; the §9.50 Runge sharpness check has no additional finding ID. No edits to source/body, reading edition, canonicalization, registry, permanent tags, \`main\`, website, CI or formalization are proposed here. All historical Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss records remain **deferred-by-user**, not resolved and not certified.
