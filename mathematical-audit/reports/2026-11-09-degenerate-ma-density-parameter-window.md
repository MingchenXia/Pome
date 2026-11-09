# Parameter window for degenerate Monge–Ampère densities without interior \(C^{1,1}\)

**Date:** 2026-11-09. **Stable finding:** \`POME-MA-DEGENERATE-C2-PARAMETER-WINDOW-001\`. **Status:** verified conditional deduction. **Severity:** low. **Original Proposition 7.24.1 is not false.** This is a new parameter-family verification of the *integrated* proof, not an upstream certification.

**Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Target:** \`docs/sections/degenerate-densities-and-interior-second-derivatives/index.html\`, blob \`fafeab3a344243fe04f24265022bd921f3a4d375\`, Proposition 7.24.1, source label \`klimek-pluripotential-theory:5F0EDAF7\`, permanent tag \`D0960BD969B2\`, physical lines **10–16**; proof lines **20–33** (density and \(C^2\)), **35–67** (radial contact), and **69–99** (anisotropic blowup and mass bound). The theorem in the reading edition uses \(dd^c=i\partial\bar\partial/(2\pi)\).

## Statement and the genuine parameter domain

Fix \(n\geq 3\), and real parameters \(\alpha>1\), \(\beta>0\) with

\[
 2\alpha<\beta<2(n-1)(\alpha-1). \tag{1}
\]

Let \(\eta:[0,\infty)\to[0,\infty)\) be the smooth cutoff

\[
 \eta(t)=\begin{cases}\exp(-1/(1-t^2)),&0\leq t<1,\\0,&t\geq1.\end{cases}
\]

For \(z'\in\mathbb C^{n-1}\) and \(w\in\mathbb C\), define

\[
 f_{\alpha,\beta}(z',w)
 =\begin{cases}|z'|^\beta\eta(|w|/|z'|^\alpha),&z'\neq0,\\0,&z'=0.\end{cases} \tag{2}
\]

Then \(f_{\alpha,\beta}\) is a nonnegative \(C^2\) function on all of \(\mathbb C^n\). Let \(u_{\alpha,\beta}\in \operatorname{PSH}(B)\cap C(\bar B)\) be the unique continuous Dirichlet solution of
\[
 (dd^cu_{\alpha,\beta})^n=f_{\alpha,\beta}\,dV_{2n},\qquad
 u_{\alpha,\beta}|_{\partial B}=0,\quad B=B(0,1).
\]
Writing \(s(t)=u_{\alpha,\beta}(0,t)\), there exist \(t_j\downarrow0\) and a constant \(c>0\) (depending on the parameters) such that
\[
 s(t_j)-s(0)\ \geq\ c\,t_j^{E},\qquad
 E=\frac{2\alpha+2(n-1)+\beta}{n\alpha}<2. \tag{3}
\]
In particular \(u_{\alpha,\beta}\notin C^{1,1}\) on any neighborhood of \(0\).

The open window (1) is nonempty **exactly when** \(n\geq3\) and \(\alpha>(n-1)/(n-2)\), for this sufficient \(C^2\)-plus-scaling argument. No claim is made that all parameter choices outside (1) give regular solutions, or that \(n=2\) enjoys a general \(C^{1,1}\) theorem. The printed choice \(\alpha=4,\ \beta=6n-7\) lies in (1) for all \(n\ge3\) and yields \(E=2-1/(4n)\). An additional simple \(n=3\) instance is \((\alpha,\beta)=(3,7)\), with \(E=17/9\).

## Derivative and degeneracy check

The cutoff \(\eta\) is smooth and flat at \(1\), and \(\eta(|w|/|z'|^\alpha)\) is smooth at \(w=0\) for \(z'\ne0\) because \(\eta\) is an even smooth function of the real argument near zero. Where \(f\ne0\), one has \(|w|<|z'|^\alpha\). By the real chain rule and the compactly supported bounded derivatives of the cutoff, for \(j=0,1,2\), \(0<|z'|\leq1\),
\[
 |D^jf_{\alpha,\beta}(z',w)|\leq C_j|z'|^{\beta-j\alpha}. \tag{4}
\]
Indeed each \(w\)-differentiation costs at most \(|z'|^{-\alpha}\), while each \(z'\)-differentiation costs at most \(|z'|^{-1}\), which is no larger in this range. These bounds extend through the cutoff boundary by flatness. At \((0,w_0)\) with \(w_0\ne0\), the function is identically zero in a neighborhood. At the origin, \(\beta>2\alpha\) makes the zero extensions of all derivatives of orders at most two continuous. Difference quotients inductively identify them as genuine derivatives. Thus \(f\in C^2\).

## Contact radii, with no assumption of an a priori smooth solution

The continuous Dirichlet solution and uniqueness are supplied by the **stated** Theorem 7.9.2; its general proof is *not certified here*. By \(U(n-1)\times U(1)\)-invariance write \(u(z',w)=U(|z'|,|w|)\). Subharmonicity on centered complex lines implies that \(U\) is nondecreasing in each radius. In particular \(u(0)\) is its minimum, \(u<0\) in \(B\), and \(s(1)=0\). Convexity of \(h(x)=s(e^x)\) on \((-\infty,0)\) follows from subharmonicity on the punctured \(w\)-axis.

For \(0<t<1\), put
\[
 R(t)=\min\{t^{1/\alpha},\sqrt{1-t^2}\},\qquad b(t)=U(R(t),t)\ge s(t).
\]
If \(b(t)>s(t)\) on a neighborhood of a particular \(t\), choose a short closed interval \([t_1,t_2]\) on which the affine chord \(L(\log\tau)\) of \(h\) stays strictly below \(b(\tau)\). On
\[
 D_{t_1,t_2}=\{t_1<|w|<t_2,\quad |z'|^\alpha<|w|\}\cap B,
\]
the density (2) is zero. On its annular ends \(u\ge L\) by radial monotonicity; on the inner interface \(|z'|^\alpha=|w|\), the same holds by the strict \(b\)-gap; and on the sphere it holds because \(u=0\) and \(L\le0\). The maximal-PSH comparison principle (with the relatively compact annular portion, or its standard exhaustion) yields \(u\ge L(\log|w|)\). Along the \(w\)-axis, convexity gives the reverse inequality \(s(t)\le L(\log t)\), so \(h=L\) on the short interval. Thus **\(h\) is locally affine wherever \(b>s\)**. This is the actual analytic contact step, not a limit exchange.

Moreover \(s(t)>s(0)\) for all \(t>0\). Otherwise let \(t_0>0\) be the endpoint of an initial constant interval for \(s\). Since \(s(1)=0>s(0)\), \(t_0<1\). If \(b(t_0)=s(0)\), radial monotonicity would make \(u\) constant on \(\{|z'|<R(t_0),|w|<t_0\}\), contradicting positivity of \(f\) on a nonempty open subset of this product. Hence \(b(t_0)>s(t_0)\); local affinity of \(h\) together with constancy on the left contradicts the maximality of \(t_0\).

There must therefore be a sequence \(t_j\downarrow0\) with \(b(t_j)=s(t_j)\): otherwise \(h\) would be affine on a half-line \((-\infty,\log\delta)\), hence constant there because it has the finite limit \(s(0)\), again a contradiction. This argument works for every \(\alpha>1\); the exponent \(\beta\) does not enter the contact analysis except through positivity on some open set.

## Exact anisotropic scaling and exponent

For a contact radius \(\varepsilon=t_j\) sufficiently small, let \(\lambda=\varepsilon^{1/\alpha}\), so \(R(\varepsilon)=\lambda\). Radial monotonicity and contact give
\[
 u(0)\le u(z',w)\le s(\varepsilon)
 \quad(|z'|\le\lambda,\ |w|\le\varepsilon).
\]
Define \(d=(\varepsilon\lambda^{n-1})^{2/n}\) and \(v(\zeta',\zeta_n)=[u(\lambda\zeta',\varepsilon\zeta_n)-s(\varepsilon)]/d\) on \(B(0,1)\). Then \(v(0)\le v\le0\), and precisely because
\(d^n=\varepsilon^2\lambda^{2(n-1)}\), biholomorphic covariance with the specified \(dd^c\) gives **no missing Jacobian factor**:
\[
 (dd^cv)^n=f_{\alpha,\beta}(\lambda\zeta',\varepsilon\zeta_n)\,dV_{2n}(\zeta). \tag{5}
\]

Take the fixed positive-volume set
\[
 K_0=\{1/8<|\zeta'|<1/4,\quad
       |\zeta_n|<\tfrac12\,8^{-\alpha}\}\Subset B(0,1/2)
\]
(shrink the strict bounds slightly if a closed compact set is desired). There \(|\varepsilon\zeta_n|/|\lambda\zeta'|^\alpha\le1/2\) and \(|\lambda\zeta'|^\beta\ge\lambda^\beta 8^{-\beta}\), hence the integral of (5) over \(K_0\) is at least \(c_0\lambda^\beta\).

The **stated** Chern–Levine–Nirenberg Theorem 7.2.5 on concentric balls bounds the total mass on \(B(0,1/2)\) by \(C_n\|v\|_{L^\infty(B(0,3/4))}^n\le C_n(-v(0))^n\). Consequently
\[
 c_0\lambda^\beta
 \le C_n\big((s(\varepsilon)-s(0))/d\big)^n,
\]
and (3) follows, since
\[
 d\lambda^{\beta/n}
 =\lambda^{[2\alpha+2(n-1)+\beta]/n}
 =\varepsilon^{[2\alpha+2(n-1)+\beta]/(n\alpha)}.
\]
If \(u\) were \(C^{1,1}\) near the origin, the \(w\)-rotation symmetry would force the \(w\)-gradient to vanish at the origin; its Lipschitz gradient would give \(s(t)-s(0)=O(t^2)\), impossible because \(E<2\).

## Exact dependency and disposition

* **Internal input, not re-proved:** Theorem 7.9.2, \`docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html\`, blob \`ff1d5dfff1913156b45875eabf921f60af553b99\`, source/permanent \`foundations-of-pluripotential-theory:69935D4D/A092925717E1\`, physical lines 41–50.
* **Internal input, not re-proved:** Theorem 7.2.5 (bounded CLN estimate), \`docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html\`, blob \`18bd2395f3b76941b2c677079c09eb6accc5a9cb\`, source/permanent \`foundations-of-pluripotential-theory:103AB333/2A84C325AB58\`, physical lines 99–117.
* **Other theorem-level input:** maximality/comparison for locally bounded MA-zero PSH functions on the annular region; the integrated Proposition 7.24.1 already invokes it. Its full dependency chain is not certified in this report.

**Verdict:** Proposition 7.24.1 is mathematically correct at the checked steps; the derivation above is a **verified conditional deduction** from the stated classical Dirichlet, CLN, and comparison inputs. The parameter inequalities and Jacobian calculation are independently checked. Recommend an optional remark after Proposition 7.24.1 with (1)–(3), preserving its exact original source label, permanent tag, and historical attribution. Do **not** modify main or count §7.24 as fully certified. This is unrelated to the owner-excluded approximation/regularization/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme, which remains **deferred-by-user**, not resolved. No software test, build, formal verification, CI or site publication is claimed.
