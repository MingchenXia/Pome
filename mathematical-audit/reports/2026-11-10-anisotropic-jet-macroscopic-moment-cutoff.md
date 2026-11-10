# §18.44: macroscopic anisotropic point-jet selection as a moment-polytope truncation

**Date:** 2026-11-10. **Finding ID:** \`POME-ANISOTROPIC-JETS-MACROSCOPIC-MOMENT-CUTOFF-001\`.  
**Classification:** low severity; **verified conditional deduction**, not a printed-theorem error, not a certified replacement of the whole section.

## Fixed source, tags and scope

Reviewed production \`main\` commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. The integrated reading page is
\`docs/sections/partial-kernels-and-quotient-equilibrium--anisotropic-point-jets-and-isolated-poles-on-fibrations/index.html\`, blob \`1eefb2e68f8091fcd531535ed38b9003774a2f95\`.

- §18.44 introductory metric, curvature, and order convention: physical lines 7–46, section permanent tag \`44BF9B7D0141\`; Equation 18.44.1 source \`non-kahler-pluripotential-theory:69BE25F3\`, permanent \`7FB2622EF514\`, lines 30–37.
- Theorem 18.44.2 source \`non-kahler-pluripotential-theory:BC433784\`, permanent \`7840E247F9D5\`, physical lines 47–60; its monomial basis, probability factorization, interior saddle expansion, and full-kernel total-variation proof are lines 61–115. Equation 18.44.5 source \`non-kahler-pluripotential-theory:5CD68BC7\`, permanent \`238CE4ED10CD\`, lines 74–80; equation 18.44.4 source \`non-kahler-pluripotential-theory:A3BD0A95\`, permanent \`4219416A5981\`, lines 54–58.
- Proposition 18.44.8 source \`non-kahler-pluripotential-theory:9383A964\`, permanent \`443408C4E29A\`, physical lines 132–161, **context only**: its small-center scaling does not address the macroscopic regime here.
- Theorem 18.44.11 source \`non-kahler-pluripotential-theory:6C7F82CE\`, permanent \`154EDD25787A\`, lines 182–213, **context only**; its small-coefficient quasi-PSH deduction must not automatically be extended to the regime below.

This is the **first direct proof-level mathematical visit** to §18.44 in the section matrix (previously an inventory row). This report reviews the explicit product-of-curves monomial calculation, not its entire surrounding proof chain, and does not reopen the user-excluded Demailly approximation/regularization, Bergman–L²–Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme. The finite-dimensional orthogonal monomial projection in this already published example is a separate mathematical question.

## Precise new assertion

Retain **exactly** the data of §18.44: \(q\ge2\), integers \(r_j\ge2\) with at least two unequal, \(d_j=r_j+1\), \(\varepsilon_j>0\),
\[
 Y=(\mathbb P^1)^q,\quad L=\boxtimes_{j=1}^q\mathcal O(d_j),\quad
 \psi_j(t)=\log(1+t^{r_j}+\varepsilon_jt^{d_j}),\quad
 a_j(t)=(1+t)^{-2},
\]
with volume \(\nu_Y=\prod_j a_j(t_j)dA_j\). Write
\[
 H_j(t)=t\psi'_j(t),\qquad G_j(t)=tH'_j(t)>0,\qquad
 g_j(t)=H'_j(t)=G_j(t)/t.
\]
Unlike printed Theorem 18.44.2, allow integers \(k_m\) satisfying
\[
 \frac{k_m}{m}\longrightarrow \kappa\in\Bigl(0,\sum_{j=1}^q d_j\Bigr).
\]
Put \(V_m=H^0(Y,L^m\otimes\mathfrak m_x^{k_m})\), let \(B_m\) be its orthogonal projection kernel density, and define
\[
 P=\prod_j[0,d_j],\quad
 P_\kappa=\{u\in P:\ \sum_j u_j\ge\kappa\},\quad
 U(z)=\sum_j H_j(|z_j|^2).
\]
Then the following hold.

**(A) A sharp macroscopic cut-off in total variation:**
\[
 \boxed{\quad
  m^{-q}B_m\,\nu_Y
  \ \xrightarrow{\mathrm{TV}}\ 
  \mathbf1_{\{U\ge\kappa\}}\frac{\theta^q}{q!}.
 \quad}
\]
The right-hand measure has mass
\[
 \boxed{\quad
 D_\kappa=\operatorname{Vol}_q(P_\kappa)
 =\prod_j d_j-\frac1{q!}
   \sum_{S\subseteq\{1,\dots,q\}}(-1)^{|S|}
        \Bigl(\kappa-\sum_{j\in S}d_j\Bigr)_+^q>0 .
 \quad}
\]
Furthermore \(N_m/m^q\to D_\kappa\), where \(N_m=\dim V_m\); hence the probability measures \(N_m^{-1}B_m\nu_Y\) converge in total variation to
\(D_\kappa^{-1}\mathbf1_{\{U\ge\kappa\}}\theta^q/q!\).

**(B) Interior Gaussian boundary layer at a fixed, nondegenerate point.** Fix \(z\in(\mathbb C^*)^q\) with each \(t_j=|z_j|^2\in(0,\infty)\), and set \(U=\sum_jH_j(t_j)\), \(V_0=\sum_jG_j(t_j)>0\). If the integer cutoffs satisfy
\[
 \frac{mU-k_m}{\sqrt{mV_0}}\longrightarrow\tau\in\mathbb R,
\]
then
\[
 \boxed{\quad
 \frac{\pi^q a(t) B_m(z)}{m^q\prod_jg_j(t_j)}
 \longrightarrow\Phi(\tau).
 \quad}
\]
This is a **different** asymptotic regime from §18.44.2: here \(t_j\) are fixed away from the degenerate coordinate divisors and \(k_m\) is of order \(m\); in the printed theorem the radii shrink to zero and \(k_m=o(m)\). The assertion is for the fixed metric/product model only, not a general Bergman expansion.

## Proof: exact orthogonal projection and concentration

For every \(m,k_m\), and **without** assuming \(k_m=o(m)\), holomorphic sections of \(L^m\) are polynomials
\(z^\ell e^m\) with \(0\le\ell_j\le d_jm\). The power \(\mathfrak m_x^{k_m}\) imposes precisely
\(\sum_j\ell_j\ge k_m\). Orthogonality follows from independent circle rotations. With the original integrals
\[
 J_{j,m,\ell}=\pi\int_0^\infty
       t^\ell e^{-m\psi_j(t)}a_j(t)\,dt,\quad
 w_{j,m,\ell}(t)=t^\ell e^{-m\psi_j(t)}/J_{j,m,\ell},\quad
 K_{j,m}(t)=\sum_{\ell=0}^{d_jm}w_{j,m,\ell}(t),
\]
let \(L_{j,m}\) be independent discrete random variables whose probabilities equal
\(w_{j,m,\ell}(t_j)/K_{j,m}(t_j)\). Direct orthogonal summation, with no asymptotic interchange, gives **exactly**
\[
 B_m(z)=\prod_jK_{j,m}(t_j)\,
          \mathbb P\{\sum_j L_{j,m}\ge k_m\}.
 \tag{1}
\]
This is equation 18.44.5 with no restriction on the order; the original order restriction is needed for its particular *asymptotics*, not for this identity.

Fix \(t\in(0,\infty)\) in one factor, writing \(K_m,\psi,H,G\). For every small **real** \(s\),
\[
 \mathbb E(e^{s L_m})
 =e^{m[\psi(te^s)-\psi(t)]}
       \frac{K_m(te^s)}{K_m(t)}. \tag{2}
\]
This follows by multiplying each summand \(t^\ell/J_{m,\ell}\) by \(e^{s\ell}\); no probabilistic approximation is involved. The **interior**, uniformly-on-compact-subsets Laplace estimate established in physical lines 91–110 of the integrated page yields
\[
 \frac{K_m(v)}m\longrightarrow\frac{g(v)}{\pi a(v)}>0
 \quad\text{locally uniformly for }v\in(0,\infty). \tag{3}
\]
Consequently the logarithm of the ratio in (2) is \(O(1)\) for fixed small \(s\). The Taylor expansion
\[
 \psi(te^s)-\psi(t)=sH(t)+\tfrac12s^2G(t)+O(s^3)
\]
and Chernoff's bound (choose small positive/negative \(s\) according to the tail) show that, for every \(\delta>0\),
\[
 \mathbb P\bigl(|L_m/m-H(t)|>\delta\bigr)\le C_\delta e^{-c_\delta m}.
 \tag{4}
\]
For fixed \(t_1,\ldots,t_q\), (4), a union bound, and \(k_m/m\to\kappa\) imply
\[
 \mathbb P\{\sum_jL_{j,m}\ge k_m\}
 \longrightarrow \mathbf1_{\{U(t)>\kappa\}}
 \quad\text{whenever }U(t)\ne\kappa. \tag{5}
\]

## Proof: the full-density limit implies total variation of the cut-off

Let \(F_m=m^{-q}\prod_jK_{j,m}\) be the full kernel density with respect to \(\nu_Y\), and write \(F=\prod_j g_j/(\pi a_j)\) on the affine product chart. Equation (3) gives \(F_m\to F\) almost everywhere. Moreover
\[
 \int_YF_m\,d\nu_Y
  =m^{-q}\prod_j(d_jm+1)\longrightarrow\prod_jd_j
  =\int_Y F\,d\nu_Y.
\]
The last equality follows **directly** from polar coordinates and
\(\int_0^\infty g_j(t)\,dt=H_j(\infty)-H_j(0)=d_j\).
For nonnegative functions with equal limiting total mass, the identity
\(\|F_m-F\|_1=\int F_m+\int F-2\int\min(F_m,F)\)
and dominated convergence on \(\min(F_m,F)\le F\) prove \(F_m\to F\) in \(L^1(\nu_Y)\). No uniform pointwise domination of \(F_m\) is asserted.

Because \(g_j(t)>0\), the map \(t\mapsto U(t)=\sum_j H_j(t_j)\) has a nonzero derivative in each radial coordinate. Thus \(\{U=\kappa\}\) has \(\nu_Y\)-measure zero (also by Fubini); coordinate charts at infinity/coordinate zero affect only a null set. Put \(P_m(t)=\mathbb P(\sum_j L_{j,m}\ge k_m)\) and \(P(t)=\mathbf1_{\{U(t)\ge\kappa\}}\). From (5), \(P_m\to P\) almost everywhere and \(0\le P_m\le1\), so
\[
 \|F_mP_m-FP\|_{L^1(\nu_Y)}
 \le \|F_m-F\|_{L^1(\nu_Y)}
      +\int_YF|P_m-P|\,d\nu_Y\longrightarrow0.
\]
By (1), this is exactly assertion (A), not merely weak convergence.

The angle variables have normalized Haar measure under \(\theta^q/q!\), and the moment change of variables
\(u_j=H_j(t_j)\) has \(du_j=g_j(t_j)\,dt_j\). Hence the pushforward of \(\theta^q/q!\) by
\(H=(H_1,\dots,H_q)\) is ordinary Lebesgue measure on \(P\). This proves that the limiting mass is
\(\operatorname{Vol}(P_\kappa)\). For the explicit formula, inclusion-exclusion translates the box constraints in
\(\{u_j\ge0,\ \sum u_j<\kappa\}\), giving
\[
 \operatorname{Vol}\{u\in P:\sum u_j<\kappa\}
 =\frac1{q!}\sum_{S}(-1)^{|S|}(\kappa-\sum_{j\in S}d_j)_+^q.
\]
Separately, the exact monomial dimension is the **lattice-point count**
\[
 N_m=\#\{\ell\in\mathbb Z^q:\ 0\le\ell_j\le d_jm,\ \sum_j\ell_j\ge k_m\}.
\]
Its Riemann sums converge to \(\operatorname{Vol}(P_\kappa)\), since the boundary of \(P_\kappa\) has zero \(q\)-volume. This proves the dimension and probability normalization claims. The **sublinear-only** binomial count (18.44.4) must not be reused when \(k_m\) crosses a coordinate upper bound \(d_jm+1\).

## Proof of the fixed-interior Gaussian boundary layer

In (2) take \(s=u/\sqrt m\), for any fixed real \(u\), and center by \(mH(t)\). By the Taylor expansion, while the locally uniform positive limit in (3) makes
\(\log[K_m(te^{u/\sqrt m})/K_m(t)]\to0\), we get
\[
 \log\mathbb E\exp\Bigl(u\frac{L_m-mH(t)}{\sqrt m}\Bigr)
       \longrightarrow \tfrac12u^2G(t).
 \tag{6}
\]
Convergence of moment-generating functions on an interval around zero yields convergence in law to
\(N(0,G(t))\): equivalently, bounded exponential moments give tightness and uniform integrability of moments, and the Gaussian moment sequence determines its distribution. Independence gives
\[
 \frac{\sum_jL_{j,m}-mU}{\sqrt{mV_0}}\Longrightarrow N(0,1).
\]
The moving threshold \((k_m-mU)/\sqrt{mV_0}\to-\tau\) and continuity of the normal distribution imply
\(\mathbb P\{\sum_jL_{j,m}\ge k_m\}\to\Phi(\tau)\). Equation (3) and the exact factorization (1) yield (B). This is a standard elementary exponential-moment argument, not a claim of general uniform heat-kernel or Bergman regularity.

## Checks, qualifications, and suggested treatment

- Explicit two-factor check: \(q=2,(r_1,r_2)=(2,3)\), hence \((d_1,d_2)=(3,4)\). For \(\kappa=7/2\), \(\operatorname{Vol}(P_\kappa)=12-\frac12((7/2)^2-(1/2)^2)=6\). The exact lattice counts divided by \(m^2\) at \(m=20\) and \(100\) are \(6.2525\) and \(6.0501\), respectively. These are sanity checks only; the proof is the preceding change-of-variables and Riemann-sum argument.
- **No contradiction with Theorem 18.44.2:** its hypotheses expressly require \(k_m=o(m)\), so its full-mass limit \(\theta^q/q!\) is correct. Here a positive proportional jet threshold removes a nonzero \(\theta^q/q!\)-mass region.
- **Boundary of scope:** Theorem 18.44.11's special selecting potentials \((k_m+N-1)\chi_p/m\) are \(\omega_X\)-PSH for large \(m\) **because** \(k_m/m\to0\). For proportional orders, that argument fails and must not be cited to lift our limit to a quasi-PSH multiplier-ideal selection on an arbitrary fibration. The algebraic pullback section identity for the prescribed ideal \(\mathfrak m_p^{k_m}\) is a separate matter. Do not label this a repair of Theorem 18.44.11.
- The nonlinear, non-diagonal, general-weight versions and global mixed-dimensional multiplier-ideal comparison remain **unreviewed**. The source's one-factor interior estimate (3) and ordinary Laplace/measure-theoretic principles are used as internal/elementary inputs; the full §18.42 proof chain is **not independently certified** in this report.
- **Proposed addition, not applied:** an optional remark after Theorem 18.44.2 giving the moment-half-space limit, inclusion-exclusion dimension formula, and fixed-interior Gaussian boundary layer, explicitly distinguishing \(k_m/m\to\kappa>0\) from the theorem's \(o(m)\) regime. No source file, canonical registry, permanent tag, main branch, build, CI, or published site is changed.

**Coverage accounting:** §18.44: first direct selected proof-level visit (**+1** numbered section), focused on the monomial basis and probability factorization (physical lines 47–115), with explicit contextual checks of Proposition 18.44.8 and Theorem 18.44.11 (lines 132–219). No entire section certified. Existing audit statuses and the excluded programme remain untouched and \`deferred-by-user\`. At this main revision the table of contents still has **25 chapters and 747 distinct numbered sections**.
