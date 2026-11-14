# Smooth dependence of strongly convex Green functions on the domain

Date: 2026-11-14 (Asia/Shanghai). Finding: **POME-STRCONVEX-GREEN-PARAMETRIC-SMOOTH-001**. Severity: **low**. Status: **verified conditional deduction** (not a false printed theorem and not a full certification of the upstream geodesic existence proof).

## Exact source and scope

Reviewed main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The directly inspected integrated reading edition is:

- **docs/sections/smooth-green-functions-on-strongly-convex-domains/index.html**, blob **e19df8fd1692c138eddd5f2fff8822de588e03ec**, section permanent tag **D1E419621675**, original source label **klimek-pluripotential-theory:90BAB568**.
- Lemma **9.24.2**, source **klimek-pluripotential-theory:2D8E2E2A**, permanent tag **CB9F3D62BE1C**, lines **54–84**: smooth nonvanishing positive stationary lifts, positive constant pairing.
- Lemma **9.24.3**, source **klimek-pluripotential-theory:8C00762F**, permanent tag **106A14BC1AFE**, lines **88–102**: uniformly positive compressed boundary operators preserve Sobolev regularity.
- Proposition **9.24.4**, source **klimek-pluripotential-theory:791F5048**, permanent tag **495B56CEC1A8**, lines **106–172**: boundary linearization, its coercive inverse (lines 113–161), smooth Banach parameter dependence (lines 163–171).
- Theorem **9.24.5**, source **klimek-pluripotential-theory:176EB905**, permanent tag **A2E9734AB1F5**, lines **176–202**: finite-dimensional local inverse in the normalized lift variables (lines 183–199), smooth Green function off the diagonal.
- **docs/sections/complex-geodesics-on-bounded-convex-domains/index.html**, blob **406faf6cf759c6aa6ed9b0cee3792ba6b5a85f65**; Theorem **9.20.5**, source **klimek-pluripotential-theory:5E98FA95**, permanent tag **7264782B9A80**, lines **173–205**, provides retract discs and the Green identity. Its deep stationary-disc existence input is not transitively re-proved in this increment.

This is a **new parameter-extension consequence**, not a previously recorded fixed-domain §9.24 proof check or a repetition of the product-domain invariants in §9.17.

## Precise statement

Let \(S\subset\mathbb R^m\) be open and \(n\ge 2\). Let \(r(s,z)\) be real-valued and \(C^\infty\) jointly in \((s,z)\) on a common neighborhood of the closures of the domains under discussion. Suppose locally in \(s\) that
\(D_s=\{z:r(s,z)<0\}\) is a nonempty connected bounded domain with smooth boundary and positive real second fundamental form, hence strongly real convex, and that the closures remain in a common compact subset of this coordinate neighborhood. The gradient of \(r_s\) is assumed nonzero on the boundary. Then on the open incidence set

\[
\mathcal U=\{(s,z,a):s\in S,\ z,a\in D_s,\ z\ne a\}
\]

the function

\[
G(s,z,a)=g_{D_s}(z,a)
\]

is **jointly \(C^\infty\)**. In particular, all mixed derivatives in the domain parameters and the two interior points exist and are continuous off the diagonal. The conclusion is local in \(s\); no uniform boundary or pole-diagonal bounds are asserted. For an arbitrary compact subset of \(\mathcal U\), the mixed derivatives are bounded there by smoothness and compactness (not by an explicit universal constant).

## Proof: promote the two existing inverse functions to parameter-dependent inverses

Fix \((s_0,z_0,a_0)\in\mathcal U\). By Theorem 9.20.5, the strongly real convex domain \(D_{s_0}\) admits a stationary complex geodesic \(f_0\) with \(f_0(0)=a_0\) and \(f_0(t_0)=z_0\) for \(0<t_0<1\), with nonzero smooth positive stationary lift \(g_0\). Normalize \(b_0=g_0(0)\) by \(|b_0|=1\), scaling the lift and positive boundary multiplier together. Lemma 9.24.2 assures that these are smooth boundary data.

**First inverse.** In any fixed angular Sobolev space \(H^k\), \(k\ge2\), use the boundary map, with \(s\) now an additional finite-dimensional parameter,

\[
\mathcal F_s(f,g,\rho)=
\big(r_s(f),\quad g/\zeta-\rho (r_s)_z(f),\quad f(0),\quad g(0)\big).
\]

This is \(C^\infty\) in \(s\) and all Banach variables by the joint smoothness of \(r\), the \(H^k\) algebra and composition properties, and the fact that the stationary boundary values stay in a fixed coordinate neighborhood. Crucially, at the base point the derivative in **the unknown variables** \((f,g,\rho)\) is *exactly* the bounded linear isomorphism established in the printed Proposition 9.24.4, lines 113–161. The derivative in \(s\) need not be inverted. Applying the same contraction/inverse-function argument as in lines 163–171 gives a unique local \(C^\infty\) family

\[
(s,a,b)\longmapsto (f_{s,a,b},g_{s,a,b},\rho_{s,a,b}).
\]

The strictly positive boundary multiplier persists by \(H^k\hookrightarrow C^0\), and the supporting-hyperplane maximum principle places each nonconstant disc in \(D_s\), exactly as in line 171. These are actual stationary discs for the *varying* domains, not merely formal boundary solutions.

**Second inverse.** Restrict \(b\) to the real sphere \(|b|=1\) and let \(t\in(0,1)\). The joint evaluation map

\[
\mathcal E(s,a,b,t)=\big(s,a,f_{s,a,b}(t)\big)
\]

is smooth. Its derivative at the base point is block triangular, with the identity in the \(s\)-coordinates. The remaining \((a,b,t)\)-derivative is the square isomorphism proven by the original Theorem 9.24.5, lines 189–197: a kernel variation has \(\dot a=0\), then the constant pairing \(g\cdot f'=\alpha>0\) forces \(\dot t=c=0\); Poisson positivity and the strictly convex boundary Hessian force the disc variation to vanish; and lift normalization kills the remaining real scaling direction. The ordinary finite-dimensional inverse-function theorem therefore supplies a joint \(C^\infty\) local inverse \((s,a,z)\mapsto(b(s,a,z),t(s,a,z))\) near \((s_0,a_0,z_0)\).

**Identify the scalar.** The stationary left inverse makes each nearby \(f_{s,a,b}\) a complex geodesic. The exact Green identity of Theorem 9.20.5 holds for *each* domain \(D_s\):

\[
g_{D_s}(f_{s,a,b}(t),a)=\log t.
\]

Consequently \(G(s,z,a)=\log t(s,a,z)\), smooth as \(t>0\). Since the base triple was arbitrary, this proves the claim on all of \(\mathcal U\). No interchanging of weak limits, sequential compactness assertions, or regularization results are needed.

## Exact normalization check

For a smooth positive radius \(R(s)\), take the balls \(D_s=B(0,R(s))\). At pole \(a=0\),

\[
g_{D_s}(z,0)=\log|z|-\log R(s),\qquad 0<|z|<R(s),
\]

so \(\partial_sg_{D_s}(z,0)=-R'(s)/R(s)\). This agrees with the parametric conclusion and exhibits a generally **nonzero** shape derivative even though the complex Monge–Ampère measure vanishes off the pole. For the radial discs the normalized Green identity is \(\log t\) with \(t=|z|/R(s)\), matching the above sign exactly.

## Verdict, dependencies, proposed addition, and limits

- **Status:** verified conditional deduction; **severity:** low. No contradiction to Proposition 9.24.4 or Theorem 9.24.5. It extends fixed-domain regularity to smooth families.
- **Precisely conditional inputs:** smooth stationary disc/lift and invertible Banach boundary linearization in §9.24.2–4; local evaluation injectivity in §9.24.5; the Lempert retract-disc and Green identity in §9.20.5. The existence part of §9.20.5 is **not certified** here.
- **Proposed correction/addendum (not made to the mathematical body):** append the parameter-dependent statement and two-inverse argument after Theorem 9.24.5, with the above shared defining-function and strict-convexity hypotheses. If the original proof is reorganized, retain historical attribution and both stable source/permanent tags.
- **Affected dependents:** domain-variation uses of §§9.17, 9.20 and 9.24 involving Green functions, complex geodesics and stationary lifts can invoke the addendum locally. It does **not** extend to merely convex, arbitrary pseudoconvex, degenerating-curvature, non-smooth, or varying singular domains.
- **Actual coverage:** newly checked the parameter dependence of precisely the displayed operator, positive multiplier, evaluation inverse and Green identity; inspected main §9.24 lines 54–84, 88–102, 106–202 and §9.20 lines 173–205. Both numbered sections had prior selected reviews: **0 new first-visited numbered sections; 0 completely certified sections**. The persistent 25-chapter/747-section matrix stays in force.
- **Exclusion respected:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programs are **deferred-by-user**, not checked or certified. No production changes, repository test suite, build, GitHub Actions CI or website publication were involved.
