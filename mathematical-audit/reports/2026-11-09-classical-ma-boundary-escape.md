# Classical Monge–Ampère mass escaping to the boundary under monotone uniform perturbations

**Finding:** POME-CLASSICAL-MA-BOUNDARY-ESCAPE-001  
**Date:** 2026-11-09  
**Status:** verified conditional deduction; **severity:** low.  
**Printed results:** Proposition 7.18.1, Proposition 7.18.2, and Theorem 7.28.1 are **not refuted**. This is a counterexample only to an unprinted strengthening that would promote local weak convergence of classical Monge–Ampère measures to convergence of their total masses without boundary tightness.

## Exact reading-edition targets

Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.

- Primary: **docs/sections/classical-monge-ampere-measures-at-one-exceptional-point/index.html**, blob **902375361e37c15e45e7f4b7055bfe4cd6a6db9d**. Proposition 7.18.1, source **klimek-pluripotential-theory:E69DEC85**, permanent **00C5CD9B3208**, physical lines **42–54**, especially the mass-preserving *truncation* proof at lines **46–52**. Proposition 7.18.2, source **klimek-pluripotential-theory:E1312773**, permanent **AD17D2D77F97**, physical lines **56–72**. The reading edition also presents its residual-mass argument for boundedly equivalent poles at lines **34–40**.
- Dependency inspection only: **docs/sections/classical-products-with-controlled-unbounded-loci/index.html**, blob **21dc39a9b02a4c1820f081a0c3a82e9f8ffca727**: Theorem 7.28.1, source **demailly-complex-geometry:F96C3380**, permanent **1BBBF8109419**, lines **5–10** (local classical products and *decreasing* continuity). This is unrelated to Demailly approximation.
- Normalization crosscheck only: **docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html**, blob **18bd2395f3b76941b2c677079c09eb6accc5a9cb**: formula (7.2.4), source **foundations-of-pluripotential-theory:01D6FA68**, permanent **706A589A680C**, lines **89–95**.

Throughout, use the printed convention
\[
dd^c=\frac{i}{2\pi}\partial\bar\partial,\qquad
(dd^c|z|^2)^n=\frac{n!}{\pi^n}\,dV_{2n}.
\]

## Statement and fully explicit family

Let \(n\ge1\), let \(B=\{|z|<1\}\subset\mathbb C^n\), and for \(a_j>0\) put
\[
u(z)=\log|z|,\qquad
u_j(z)=\log|z|+a_j(|z|^{2j}-1), \quad j\ge1.
\]
All are plurisubharmonic and continuous and finite on \(\overline B\setminus\{0\}\); each equals \(-\infty\) at the origin and has zero boundary value. Indeed, \(|z|^{2j}\) is smooth plurisubharmonic. Moreover,
\[
u_j<u\quad (0<|z|<1),\qquad
\sup_{B\setminus\{0\}}|u_j-u|=a_j.
\]
The difference extends continuously to the origin with value \(-a_j\); no subtraction of extended-real values at the pole is intended.

For every \(0<R<1\), the **classical**, pole-mass-retaining Monge–Ampère measure satisfies the exact formula
\[
\boxed{\;M_{u_j}(B_R)=\left(\frac12+j a_j R^{2j}\right)^n,\qquad
M_u(B_R)=2^{-n}.\;}
\tag{1}
\]
In particular,
\[
\boxed{\;M_{u_j}(B)=\left(\frac12+j a_j\right)^n,\qquad M_u(B)=2^{-n}.\;}
\tag{2}
\]
These are *classical* measures, not non-pluripolar products, which discard the atom at zero.

Set \(a_j=c/j\) for any fixed \(c>0\). Then \(u_j\uparrow u\) pointwise and its finite difference from \(u\) tends uniformly to zero, but
\[
M_{u_j}\ \rightharpoonup\ 2^{-n}\delta_0
\quad\text{vaguely on }B,
\qquad
M_{u_j}(B)=\left(\frac12+c\right)^n
\ne 2^{-n}=M_u(B).
\tag{3}
\]
The mass defect \((\frac12+c)^n-2^{-n}\) is exactly a boundary layer. If measures are regarded on the **closed** unit ball by assigning zero mass to its boundary, they converge weakly to
\[
2^{-n}\delta_0+
\left[\left(\frac12+c\right)^n-2^{-n}\right]\sigma_{\partial B},
\tag{4}
\]
where \(\sigma_{\partial B}\) is normalized rotation-invariant surface measure. By taking \(c\) arbitrarily large, the finite defect is arbitrarily large despite vanishing uniform perturbation. With \(a_j=j^{-1/2}\), the same uniform convergence and local weak measure convergence hold but \(M_{u_j}(B)=(\frac12+\sqrt j)^n\to\infty\); **this latter family is not claimed to be monotone**.

## Proof of the radial mass identity

Write \(t=|z|^2\) and \(q_j(t)=\frac12\log t+a_j(t^j-1)\). At \(t>0\),
\[
q_j'(t)=\frac1{2t}+j a_j t^{j-1},
\quad
q_j'(t)+tq_j''(t)=j^2a_jt^{j-1}>0.
\]
The complex Hessian has \(n-1\) tangential eigenvalues \(q_j'(t)\) and one radial eigenvalue \(q_j'(t)+tq_j''(t)\). Thus \(u_j\) is *strictly* plurisubharmonic away from its single pole and its smooth part has density
\[
(dd^cu_j)^n\big|_{B\setminus\{0\}}
=\frac{n!}{\pi^n}\,
\bigl(q_j'(t)\bigr)^{n-1}
\bigl(q_j'(t)+tq_j''(t)\bigr)\,dV_{2n}.
\tag{5}
\]

Using the area \(2\pi^n/(n-1)!\) of the unit sphere and \(t=r^2\), its mass on the punctured radius-\(R\) ball is
\[
\begin{aligned}
\int_{0<|z|<R}(dd^cu_j)^n
&=n\int_0^{R^2}t^{n-1}
(q_j')^{n-1}(q_j'+tq_j'')\,dt\\
&=\int_0^{R^2}\frac{d}{dt}(tq_j'(t))^n\,dt\\
&=\left(\frac12+j a_jR^{2j}\right)^n-2^{-n}.
\end{aligned}
\tag{6}
\]
There is **no missing \(n!\), \(2^n\), or sphere-area factor**: the normalization was checked directly against \(q(t)=t\), where \(\int_{B_R}(dd^c|z|^2)^n=R^{2n}\).

By Proposition 7.18.2, \(M_{\log|z|}=2^{-n}\delta_0\). The difference \(u_j-\log|z|\) is bounded near zero. The residual-mass invariance argument printed in §7.18, lines 34–40, therefore gives \(M_{u_j}(\{0\})=2^{-n}\). Add this atom to (6) to obtain (1). Let \(R\uparrow1\) in the *fixed* measure \(M_{u_j}\) to obtain (2); this step is monotone convergence of sets for a fixed measure, not interchange of the index \(j\) with a boundary limit.

## Monotonicity and exact limiting measure

For \(0\le t<1\),
\[
\frac{1-t^j}{j}=(1-t)\frac{1+t+\cdots+t^{j-1}}j.
\]
The arithmetic means on the right are nonincreasing in \(j\), since \(1,t,t^2,\ldots\) is nonincreasing. Hence for \(a_j=c/j\),
\(u_j=u-c(1-t^j)/j\) is **increasing** and \(0\le u-u_j\le c/j\) off the pole.

For any fixed \(R<1\), (6) shows
\[
M_{u_j}(B_R\setminus\{0\})
=\left(\frac12+cR^{2j}\right)^n-2^{-n}\longrightarrow0.
\]
The origin atom is fixed, so positive-measure domination on compact supports proves vague convergence in (3). The full-ball mass in (2) remains constant. The smooth remainder is \(U(n)\)-invariant; its mass in every \(\overline B_R\) tends to zero, while its total mass is fixed. Consequently its closed-ball weak limit is exactly that total mass times the unique \(U(n)\)-invariant probability on \(\partial B\), which proves (4). When \(a_j=j^{-1/2}\), \(j a_jR^{2j}=\sqrt j\,R^{2j}\to0\) for fixed \(R<1\), while \(j a_j\to\infty\), proving the final claim.

## Interpretation, dependency status, and proposed correction

**No printed assertion is false.** Proposition 7.18.1 compares total masses when two **fixed** potentials have the specified strict order and boundary agreement. Applied to \(u_j<u\), it predicts \(M_u(B)\le M_{u_j}(B)\), consistent with (2). Its proof uses a special *mass-preserving lower truncation*, not arbitrary small perturbations or a limit \(j\to\infty\). Theorem 7.28.1 provides *local* weak convergence under **decreasing** approximations; the constant-defect example is **increasing** and only establishes local weak convergence by explicit calculation. Formula (7.2.4) is used only for the smooth form on \(B\setminus\{0\}\), never for an undefined naive self-product at zero.

The conclusion that fails is
\[
u_j-u\to0\ \text{uniformly off their common isolated pole},
\quad M_{u_j}\rightharpoonup M_u\ \text{on }B
\quad\centernot\Longrightarrow\quad
M_{u_j}(B)\to M_u(B).
\]
An additional condition controlling mass in collars approaching \(\partial B\) (e.g. uniform tightness) is needed for this upgrade. This also illustrates why annular *interior* control is not a global mass bound up to the domain boundary.

**Suggested change only:** add an explanatory Example or Remark following §7.18.1 showing (1)–(4), and warn future users of §§7.18/7.28 that local weak measure convergence alone cannot exchange an approximation limit with exhaustion of the whole open domain. Preserve every original hypothesis, permanent tag, and historical attribution. Do not change mathematical source text or production main on this audit branch.

**Exact coverage:** first selected direct examination of §7.18, specifically its lines 5–72 and the mass-preserving proof at 46–52; §7.28.1 and §7.2.4 were inspected only for the stated dependencies. This does not certify the full proof chains or all statements in any section. The project remains 25 chapters, 747 numbered sections, and zero fully mathematically certified sections. All previously recorded findings are unchanged; the owner-excluded Demailly approximation/Bergman/L2/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved. No build, tests, CI, formal verification, source/registry modifications or website publication were performed.