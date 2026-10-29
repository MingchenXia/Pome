# 2026-10-30 — Exact Gauduchon radial root-volume deficit and endpoint determinant-density collapse

## Source version, exact scope and exclusions

- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; audit destination <code>review/mathematical-audit</code>. No source, canonical registry, permanent tags, main, CI, publication, or website changes.
- **Primary integrated reading edition:** §24.4.7–14, <code>docs/sections/problems-in-hermitian-pluripotential-theory--closed-positivity-and-geometric-equations/index.html</code>, main blob <code>38793fe10e89d1e4aebe46d639f48211285007d9</code>. Proposition **24.4.8**, original source <code>non-kahler-pluripotential-theory:198A704F</code>, permanent tag <code>8E5CAA6E5122</code>, physical lines **122–175**; Proposition **24.4.13**, source <code>non-kahler-pluripotential-theory:47F8F6B3</code>, permanent tag <code>3D0A0BF3A375</code>, lines **276–309**; open Problem **24.4.14**, source <code>non-kahler-pluripotential-theory:A226FB65</code>, permanent tag <code>B341DA2B6EFE</code>, lines **311–319**.
- **Nonexcluded determinant convention:** Eq. **12.7.1**, source <code>non-kahler-pluripotential-theory:919BAA56</code>, permanent <code>A99038CD10B4</code>, <code>docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html</code>, main blob <code>1c0f7efb92914b8a55754bd5039d7319392fb03b</code>, physical lines **12–31**; determinant-density/endpoint statements §§12.9.1–2, <code>docs/sections/a-gauduchon-variational-volume--integrability-of-gauduchon-determinant-measures/index.html</code>, main blob <code>42dae52119ba2bf793f104280abe615d9b25f09d</code>, physical lines **7–17, 62–85**. Only the definitions/normalizations and the printed claims are crosschecked here, not the full upstream duality/PDE proofs.
- **Additional first statement-level inventory:** open Problem **24.11.1**, source <code>non-kahler-pluripotential-theory:A6F8C69E</code>, permanent <code>A63319B4B931</code>, <code>docs/sections/problems-in-hermitian-pluripotential-theory--equations-on-singular-spaces/index.html</code>, blob <code>95fe41df613a9b40e64fdd1f5992492e2add31f1</code>, lines **7–26**. This is a quantifier/dependency inventory only, not a solution.
- The 2026-10-17 user exclusion is absolute: no Demailly approximation or regularization, no dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof work. None was used in the proofs below.

## Finding POME-PRIMGAUD-ROOT-DEFICIT-001

**Severity:** low. **Status:** verified conditional deduction, not a false theorem, proof gap, or general repair. Proposition 24.4.13 is correct. The only standing input is its explicit primitive elliptic-bundle geometry and wedge/normalization identities, which are independently algebraically verified below.

Let \(X=L^\times/q^\mathbb Z\) be the compact complex threefold over a compact Kähler surface \((B,\eta)\), with primitive Chern representative \(c\) satisfying \(\eta\wedge c=0\). With \(t=\log|w|^2\pmod{T}\), \(D=dt\wedge d^ct\), \(\omega=\pi^*\eta+D\), \(A=\int_B\eta^2\), and \(V=3TA\), consider the smooth positive \(\mathrm{dd}^c\)-closed complementary test
\[
 \Gamma=a\eta^2+g(t)\eta\wedge D,\qquad a>0,\quad g>0\text{ smooth and }T\text{-periodic}.
\]
(The pullback symbols are suppressed.) Since \(D^2=0\), \(\eta\wedge c=0\), and \(dg\wedge D=0\), the \(g\)-term is in fact \(d\)-closed. Its unique positive square root is
\[
 \gamma=\sqrt a\,\eta+\frac{g(t)}{2\sqrt a}D,\qquad
 \gamma^2=\Gamma.
\]
Writing \(\bar g=T^{-1}\int_0^T g(t)\,dt\), direct wedge products and fiber integration yield
\[
 d_\Gamma=\int_X\omega\wedge\Gamma=TA(a+\bar g),\qquad
 \int_X\gamma^3=\frac32 TA\sqrt a\,\bar g .
\]
These are the printed identities in the proof of Proposition 24.4.13, not a transitive certification of Proposition 24.4.8.

Set \(s=a+\bar g\), \(x=\sqrt{3a/s}\in(0,\sqrt3)\), and normalize the **root-volume deficit**
\[
 \mathcal E(\Gamma)
 :=1-\frac{\int_X\gamma^3}{d_\Gamma^{3/2}/\sqrt V}.
\]
There is an **exact factorization**:
\[
 \frac{\int_X\gamma^3}{d_\Gamma^{3/2}/\sqrt V}
 =\frac{3\sqrt3}{2}\frac{\sqrt a\,\bar g}{(a+\bar g)^{3/2}}
 =\frac{3x-x^3}{2},
 \qquad
 \boxed{\ \mathcal E(\Gamma)=\frac12(x-1)^2(x+2).\ }
\]
Indeed \(3x-x^3=3\sqrt{3a/s}- (3a/s)^{3/2}\), and \(x^3-3x+2=(x-1)^2(x+2)\). Since \(x>0\), this yields the quantitative, **sharp algebraic** estimate
\[
 \mathcal E(\Gamma)\geq \left(\sqrt{\frac{3a}{a+\bar g}}-1\right)^2
\]
and equality \(\mathcal E=0\) **if and only if** \(\bar g=2a\). The exact cubic factorization, rather than this weaker inequality, gives the full optimal deficit for every allowed pair \((a,\bar g)\). It controls the average ratio \(a/(a+\bar g)\), **not** any oscillation or concentration of the nonconstant function \(g\).

**Possible optional insertion:** an algebraic stability remark immediately after Proposition 24.4.13. **Affected dependents:** interpreting the sharp radial test bound in §24.4 and comparing degree-normalized complementary tests in §§12.7, 12.9. This neither proves a uniform positive lower Monge–Ampère mass for arbitrary potentials nor resolves Problem 24.4.14.

## Finding POME-PRIMGAUD-ENDPOINT-ESCAPE-001

**Severity:** low. **Status:** verified conditional deduction for this explicit radial family. It is distinct from the already registered fixed-Kähler-root concentration calculations in <code>POME-GAUD-FIXED-ROOT-STABILITY-001</code> and <code>POME-GAUD-CONCENTRATION-LQ-VS-LP-001</code>: here the background can be a genuinely **non-Kähler primitive elliptic bundle**, all complementary tests are exact **root-volume equality cases**, their smooth determinant measures actually tend to **zero**, and their endpoint \(L^{3/2}\) norms stay strictly positive. Neither the fixed-root functional nor its maximizers are being identified with the root-volume functional.

Fix \(a>0\) on a primitive bundle with \(c_1(L)\neq0\) in real cohomology (for instance a primitive nontrivial line bundle over \(\mathbb P^1\times\mathbb P^1\)); Proposition 24.4.8 gives a non-Kähler background. Fix \(t_0\in\mathbb R/T\mathbb Z\). Let \(\rho_\varepsilon\) be a nonnegative smooth periodic approximate identity of integral \(1\), supported in an arc of length \(O(\varepsilon)\), with height comparable to \(\varepsilon^{-1}\) on a subarc of length comparable to \(\varepsilon\). For \(0<\varepsilon\ll1\), put
\[
 g_\varepsilon(t)=2a\bigl(\varepsilon+(1-\varepsilon)T\rho_\varepsilon(t-t_0)\bigr)>0,\qquad
 \Gamma_\varepsilon=a\eta^2+g_\varepsilon(t)\eta\wedge D.
\]
Then \(\bar g_\varepsilon=2a\), so every \(\Gamma_\varepsilon\) is smooth strictly positive and \(d\)-closed, its degree is the fixed \(d=Va\), and every root \(\gamma_\varepsilon\) **exactly** saturates \(\int\gamma_\varepsilon^3=d^{3/2}/\sqrt V\). The sequence of probability measures
\[
 \frac{\gamma_\varepsilon^3}{\int_X\gamma_\varepsilon^3}
 =\frac{g_\varepsilon}{2a}\frac{\omega^3}{V}
\]
concentrates weakly on the real level hypersurface \(t=t_0\). Thus saturation of the root-volume bound alone provides no uniform integrability of these normalized **root-volume measures** above \(L^1\).

Now take the smooth **probability** reference \(\mathrm dV=\omega^3/V\) in Eq. 12.7.1, and let the normalized Gauduchon test be \(S_\varepsilon=\Gamma_\varepsilon/d\), so \(\int_X\omega\wedge S_\varepsilon=1\). The equation for the determinant measure is a *different functional* from \(\gamma_\varepsilon^3\). For a smooth \(S=\gamma^2\), Eq. 12.7.1 gives
\[
 \frac{d\Gamma_0(S)}{dV}
 =\left(\frac{\gamma^3}{dV}\right)^{2/3}.
\]
The formula is homogeneous of degree one in \(S\). Since \(\omega^3=3\eta^2\wedge D\) and \(\gamma_\varepsilon^3=\tfrac32\sqrt a\,g_\varepsilon\eta^2\wedge D\), the **exact** determinant density is
\[
 \boxed{\quad k_\varepsilon
 =\frac1d\left(\frac{V\sqrt a}{2}\,g_\varepsilon\right)^{2/3}.\quad}
\]
The pushforward of \(dV\) under \(t:X\to\mathbb R/T\mathbb Z\) is \(dt/T\). Consequently
\[
 \|k_\varepsilon\|_{L^{3/2}(dV)}^{3/2}
 =\frac{V\sqrt a}{2d^{3/2}}\bar g_\varepsilon
 =V^{-1/2},\qquad
 \boxed{\ \|k_\varepsilon\|_{L^{3/2}(dV)}=V^{-1/3}\ }\quad\text{for every }\varepsilon .
\]
For each \(1\le q<3/2\), the explicit spike and floor give
\[
 \|k_\varepsilon\|_{L^q(dV)}^q
 \le C_q\bigl(\varepsilon^{\,1-2q/3}+\varepsilon^{\,2q/3}\bigr)\longrightarrow0,
\]
whereas for every \(q>3/2\), the lower spike estimate yields
\[
 \|k_\varepsilon\|_{L^q(dV)}^q
 \asymp_q\varepsilon^{\,1-2q/3}\longrightarrow+\infty.
\]
In particular the positive measures \(\Gamma_0(S_\varepsilon)=k_\varepsilon\,dV\) tend **to zero in total variation**, but not strongly in the critical \(L^{3/2}\) space, despite the exact degree and root-volume equalities for \(S_\varepsilon\). The normalized currents \(S_\varepsilon\) themselves converge weakly to the sum of the smooth rank-one current \(a\eta^2/d\) and a singular current proportional to \(\delta_{t_0}\eta\wedge D\). The determinant measure of this limit vanishes (each mutually singular coefficient part has matrix rank \(<3\)); this is consistent with the singular-part convention of §12.9.1.

This does **not** violate the printed endpoint bound in Theorem 12.9.2. Its bound controls \(\|k_\varepsilon\|_{3/2}\), which is here exactly constant, not strong endpoint convergence. Nor does the calculation imply \(v_-(\omega)=0\): varying dual Gauduchon test densities is not constructing a sequence of admissible Monge–Ampère **potentials** with collapsing mass. Problem 24.4.14 remains open.

**Possible optional insertion:** an explicit, reproducible radial-test contrast after Proposition 24.4.13, with a reference to the definition (12.7.1) and an explicit warning that the root-volume integral and determinant-measure mass are different. **Affected dependents:** §24.4.6 endpoint integrability discussion; §§12.7–12.9 determinant compactness; §24.4.14 interpretation of candidate lower-mass obstructions. No external black-box mathematical result is used beyond the printed elementary primitive-bundle construction and its conventions.

## Exact coverage and disposition

**New direct nonexcluded mathematical review:** integrated §24.4 Proposition 24.4.13 (source lines 276–309), with the selected bundle identities of Proposition 24.4.8 (lines 122–175), the interpretation of open Problem 24.4.14, and the determinant definitions (12.7.1) / endpoint statements (§12.9.1–2) checked in their exact units. First statement-only inventory of §24.11.1; navigation-only content confirmed for §§10.32 and 10.45, not counted as theorem review. No full section, chapter, global Gauduchon lower-mass claim, or PDE proof was certified. The baseline inventory remains **25 chapters / 747 actual numbered ToC entries / zero complete-section certifications**. All historical confirmed errors, proof gaps, external inputs and user-deferred work retain their previous status.

**Explicitly deferred-by-user, neither resolved nor examined:** the entire Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. No project build, tests, formalization, website publication or source/main modifications were performed.
