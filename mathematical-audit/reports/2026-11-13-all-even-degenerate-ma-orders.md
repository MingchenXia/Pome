# All even finite orders of density vanishing in the smooth non-Kähler Monge–Ampère nonuniqueness model

**Finding:** POME-DEGENMA-EVEN-ORDER-FLAT-SLOPE-001  
**Classification:** low / **verified conditional deduction** (not a counterexample to the printed theorem).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Current integrated file:** \`docs/sections/uniqueness-for-degenerate-equations--quadratic-density-zeros/index.html\` (Git blob 7a70517262563acf523940c261daa8ec11a8cb55).  
**Source and permanent anchors:** Theorem 14.28.1 = \`non-kahler-pluripotential-theory:EC99526C\` / \`9C11A9E88B60\`, physical lines 10–24, 139–153; coefficient Equation 14.28.2 = \`non-kahler-pluripotential-theory:689AB380\` / \`ACD0920D4D78\`, lines 28–35; Lemma 14.28.3 = \`non-kahler-pluripotential-theory:A5AC3FD9\` / \`624B2CF7FBA2\`, lines 65–134; scalar ODE 14.28.4 = \`non-kahler-pluripotential-theory:8FF0501E\` / \`3D1CCE4952BA\`, lines 67–75. The rank-one and Hessian identities used below are §§14.26.3–6, in \`docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html\` (blob \`7240d97e9192c70acf09f755ec90a5420bc11ef7\`), physical lines 23–66; permanent tags \`71DFC7D0861C\` (14.26.4), \`1C52D8C53893\` (14.26.5), and \`DE71ED12948B\` (14.26.6).

## New parametric statement

For every integer \(m\geq1\), the same projective \(X=\mathbf P^3\) construction as Theorem 14.28.1, with **only** the change
\[
 p_m(r)=(1-r^2)^{2m}
\]
in Equation 14.28.2 (and all occurrences of \(p\) thereafter), gives a smooth **nonclosed** Hermitian background \(\omega_m>0\), a globally smooth \(g_m\geq0\), and an uncountable family of pairwise distinct normalized smooth \(\omega_m\)-psh solutions to
\[
(\omega_m+dd^c u)^3=g_m\omega_X^3.
\]
The zero set is exactly the two disjoint real hypersurfaces \(M_\pm=\{r=\pm1\}\); \(g_m\) vanishes to **exact order \(2m\)** transversely to either. This does not claim a real-analytic density or a new uniqueness theorem.

For any one of the nonzero negative slopes \(h=h_{m,\eta}\) used to generate these solutions, put \(d(r)=1-|r|\), \(r\in(-1,1)\). In fact the decay exponent can be determined sharply:
\[
\boxed{\displaystyle
 \lim_{r\to-1^+}d(r)^{2m-1}\log(-h(r))
 =\lim_{r\to1^-}d(r)^{2m-1}\log(-h(r))
 =-\frac{1}{2^{2m}(2m-1)}.}
\tag{A}
\]
In particular every endpoint jet vanishes.

With the standard normalized Fubini–Study volume (\(\int_X\omega_X^3=1\)), writing \(s_0=\sigma'(1)=e/(1+e)^2\), the density has the **exact sublevel leading coefficient**
\[
\boxed{\displaystyle
 \lim_{s\downarrow0}s^{-1/(2m)}
 \int_{\{g_m\leq s\}}\omega_X^3
 =12\,s_0^{\,2+1/m}.}
\tag{B}
\]
Thus \(g_m^{-\alpha}\in L^1(X,\omega_X^3)\) precisely for \(\alpha<1/(2m)\) (with \(\alpha>0\)), while at the endpoint
\[
g_m^{-1/(2m)}\in L^{1,\infty}\setminus L^1,\qquad
 \lim_{\lambda\to\infty}\lambda\,
  \operatorname{Vol}_{\omega_X^3}\{g_m^{-1/(2m)}>\lambda\}
 =12s_0^{\,2+1/m}.
\]
The source text's \(m=1\) assertions about quadratic zeros remain valid; this family and its precise logarithmic slope constant are additional deductions.

## Proof: background and determinant

Keep the source's smooth \(a(r),b(r)=a(-r),\chi(r),\kappa(r)\), the rank-one \(P,Q,R\), and \(\sigma(r)=e^r/(1+e^r)\). Set
\[
x=(1-\chi)(p_m+a)+\chi\sigma,\quad
y=(1-\chi)(p_m+b)+\chi\sigma(-r),\quad
z=1-\chi+\chi\sigma'.
\]
All coefficients are positive except \(y(-1)=x(1)=0\), and are exactly Fubini–Study coefficients outside \(|r|\geq3/2\). Because \(p_m\) is nonnegative, smooth and even, and \(p_m' (0)=0\), the original strict positivity proof for
\[
\omega_m=xP+yQ+zR+dd^c[\varepsilon(r^2-1)\kappa(r)]
\]
works verbatim for sufficiently small \(\varepsilon>0\): on the central band the corrected coefficients are \(x+2\varepsilon r,y-2\varepsilon r,z+2\varepsilon\), and on the compact transition they remain positive by uniform perturbation. At \(r=0\), \(x'=y'=0,z=1\), so the printed exterior-derivative formula \(\,d\omega_m=dr\wedge[-P+Q]\neq0\). Define \(g_m\omega_X^3=(xP+yQ+zR)^3\). It is globally smooth because these forms coincide with \(\omega_X\) at the projective ends. On neighborhoods of both hypersurfaces,
\[
(x,y,z)=
\begin{cases}
(1+p_m,p_m,1),&r\sim-1,\\
(p_m,1+p_m,1),&r\sim1,
\end{cases}\qquad
g_m(r)=\frac{p_m(r)(1+p_m(r))}{\sigma'(r)^2}.
\tag{C}
\]
This proves exact transverse order \(2m\), positivity off the hypersurfaces, and smoothness without using any excluded regularization programme.

## Proof: barriers, continuation, and sharp flatness

For \(0<\eta\ll1\), solve
\[
h'=\frac{xyz}{(x+h)(y-h)}-z,\qquad h(0)=-\eta.
\tag{D}
\]
The zero slope is a solution. Fix \(0<c<1\) and test \(h=-cp_m\). At the left endpoint \(F(r,-cp_m)+cp_m'\to-c/(1+c)<0\); at the right endpoint this expression tends to \(c/(1-c)>0\). These signs use only \(p_m,p_m'\to0\). Continuous dependence near the zero solution on an interior compact interval, no-crossing, the backwards left and forwards right barriers, and ODE continuation therefore give the full interval \((-1,1)\) with
\[
-cp_m<h<0
\tag{E}
\]
on fixed endpoint neighborhoods, and \(-x<h<y\) everywhere.

The equation factors, exactly as printed,
\[
h'=hL(r,h),\qquad
L(r,h)=\frac{z(x-y+h)}{(x+h)(y-h)}.
\tag{F}
\]
On the left \(L=(1+h)/[(1+p_m+h)(p_m-h)]\ge C/p_m\); on the right \(L=(-1+h)/[(p_m+h)(1+p_m-h)]\le-C/p_m\). Integrating \((\log(-h))'=L\) from an interior point gives
\[
0<-h(r)\le C_\eta\exp[-A_m d(r)^{-(2m-1)}]
\]
at both ends. Hence \(h=o(p_m)\). Substitution back into the *exact* rational expressions in (F) improves the estimate to
\[
p_mL\longrightarrow1\quad(r\to-1^+),\qquad
p_mL\longrightarrow-1\quad(r\to1^-).
\]
Since \(p_m(r)\sim(2d)^{2m}\), elementary integration proves (A), including its numerical leading constant. All partial derivatives of \(L\) along the trapped graph grow at most polynomially in \(d^{-1}\), because \(p_m-h\ge p_m\) on the left and \(p_m+h\ge(1-c)p_m\) on the right. Repeated differentiation of (F) yields \(|h^{(j)}|\le C_j e^{-A_m d^{-(2m-1)}}d^{-N_j}\). Thus extension of \(h\) by zero is \(C^\infty\) and flat at both endpoints.

Take a primitive \(G_{m,\eta}\) of this extended slope, constant near both projective ends. Put \(u_{m,\eta}=G_{m,\eta}(r)-\varepsilon(r^2-1)\kappa(r)\). The solution form is
\[
(x+h)P+(y-h)Q+(z+h')R,
\qquad z+h'=\frac{xyz}{(x+h)(y-h)}>0
\]
on \((-1,1)\); outside, it equals \(xP+yQ+zR\). On \(M_\pm\) it is the original rank-two semipositive form. By the rank-one wedge identity, its cube equals \(g_m\omega_X^3\) everywhere. Distinct \(\eta\) give distinct \(h(0)\), so their potentials cannot differ by constants; supremum normalization retains uncountably many. The separate bounded-mass assertion uses the same existing §13.14.15 input as the printed theorem; that upstream general theorem is **not independently certified** here.

## Proof: exact small-level coefficient

The radial coordinate \(t=\sigma(r)=|A|^2/(|A|^2+|B|^2)\) has beta \(\mathrm{Beta}(2,2)\) distribution under normalized Fubini–Study volume on \(\mathbf P(\mathbf C^2\oplus\mathbf C^2)\). Indeed, the squared norms of the two complex two-dimensional blocks have gamma shape parameters \(2,2\), so \(t\) has density \(6t(1-t)\); equivalently \(r\) has density \(6\sigma'(r)^2\,dr\). This follows directly from the unit-sphere parametrization, independently of a PDE existence theorem.

At \(r=\pm1\), formula (C) and \(d=1-|r|\) yield
\[
g_m(r)\sim \frac{2^{2m}}{s_0^2}d^{2m},\qquad
6\sigma'(r)^2\longrightarrow 6s_0^2.
\]
For \(s\downarrow0\), the sublevel set consists of four one-sided collars, each of radial width
\(\frac12s_0^{1/m}s^{1/(2m)}(1+o(1))\); away from them the density has a positive lower bound. Their four weighted lengths give precisely (B). Layer-cake integration and the change \(s=\lambda^{-2m}\) prove the integrability and weak endpoint assertions.

## Status, dependencies, and correction

- **Verified conditional deduction / low.** No printed theorem or proof is refuted; no edit to source, canonical registry or permanent tags is warranted. The proposed **optional** addition is the parametric even-order statement (and explicit logarithmic/sublevel coefficients), *not* a replacement of Theorem 14.28.1.
- **Directly checked:** algebraic rank-one determinant reduction; all-\(m\) coefficient positivity; ODE barrier signs/continuation; all-jet flatness; sharp logarithmic asymptotic; coarea/beta sublevel asymptotics. **Reused internal inputs:** the geometric \(P,Q,R\) decomposition, \(dd^cG(r)\) and projective extension identities in §§14.26.2–6; no independent verification of the general bounded-mass theorem §13.14.15 or the global uniqueness machinery.
- **Affected mathematical comparisons:** §14.28.1's finite-order model is the \(m=1\) case; §14.21.13 inverse-density uniqueness threshold stays unrefuted; §14.29's real-analytic density is a separate construction and is **not** claimed for \(m>1\). Earlier §14.27 log-tail and §14.29 fixed-density continuum findings are unchanged.
- **Coverage:** direct proof-level revisit of §14.28.1, Lemma 14.28.3 and displayed formulae §§14.28.2/4/5/6; §§14.26.2–6 only dependency checks and §14.21.13 a statement-scope comparison. Previously partly reviewed §14.28, so **0 newly first-visited numbered sections, 0 complete certifications**. Current ToC remains **25 chapters, 747 numbered sections**. All author-excluded Demailly approximation/regularization, dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remains **deferred-by-user**, not solved or reopened.
