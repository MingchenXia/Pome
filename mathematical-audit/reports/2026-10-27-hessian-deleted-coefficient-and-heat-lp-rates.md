# Mathematical audit — a sharp deleted-coordinate Hessian coefficient and heat-trace \(L^p\) rates
**Review date:** 27 October 2026  
**Pinned integrated main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Audit branch:** review/mathematical-audit  
**Scope:** additional selected proof-level inspection in §§8.2 and 3.10, first selected proof-level inspection of §10.88. Neither the Demailly approximation/regularization programme nor its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss prerequisites were inspected. Historical related findings retain status **deferred-by-user**.

## POME-HESS-DELETED-COEFF-SHARP-001
**Severity/status:** low / **verified conditional deduction** (sharpness of a correct printed lemma, *not* a false theorem).  
**Integrated file:** docs/sections/complex-hessian-equations--the-admissible-cone/index.html, Git blob 925e6109ab7d800cde9bec4b0487842b2e6877a8, lines 186–221.  
**Exact statement:** Lemma 8.2.8, original source label non-kahler-pluripotential-theory:E5B04592, permanent tag 8673FC834527. Its proof uses the unnormalized Newton inequality and the exact deleted-coordinate identity, lines 200–221. Its ambient chapter assumption is \(2\leq m<n\), stated in §8.1 at docs/sections/complex-hessian-equations/index.html:7 (blob 5331b937ccdaba51f1ec006d5e72dc84f7addfbf).  
**Hypotheses inspected:** \(\lambda\in\overline{\Gamma_m}\), \(1\leq q\leq\min(m-1,n-2)\), \(i\neq j\), \(N=n-2\), \(c_{N,q}=q(N-q)/((q+1)(N-q+1))\).

**Exact extremizer and proof.** In the permitted intermediate Hessian range take
\[
 n=4,\quad m=2,\quad q=1,\quad (i,j)=(1,2),\quad
 a=\sqrt3-2,\quad \lambda=(a,a,1,1).
\]
The unnormalized elementary symmetric polynomials satisfy
\[
 S_1(\lambda)=2a+2=2(\sqrt3-1)>0,\qquad
 S_2(\lambda)=a^2+4a+1=0.
\]
Thus \(\lambda\in\partial\Gamma_2\subset\overline{\Gamma_2}\): adding \(\varepsilon\mathbf1\) places it in the open cone for every sufficiently small \(\varepsilon>0\). Here \(N=2\), \(c_{2,1}=1/4\), and direct deletion of coordinates yields
\[
 S_{1;12}(\lambda)=2,\qquad S_{1;1}(\lambda)
 =S_{1;2}(\lambda)=a+2=\sqrt3.
\]
Hence equality holds, with both sides exactly four:
\[
 |S_{1;12}|^2=4
 =\frac{(\sqrt3)(\sqrt3)}{1-\frac14}.
\]
Consequently the multiplier \((1-c_{N,q})^{-1}=4/3\) in Lemma 8.2.8 **cannot be decreased uniformly**, already for the fixed valid triple \((n,m,q)=(4,2,1)\). By continuity, interior vectors \(\lambda+\varepsilon\mathbf1\in\Gamma_2\) make the quotient \(|S_{1;12}|^2/(S_{1;1}S_{1;2})\) arbitrarily close to \(4/3\). The proof also identifies the two mechanisms of equality in the displayed proof: the deleted list is \((1,1)\), attaining Newton equality, and \(S_2(\lambda)=0\), eliminating the nonnegative remainder \(A S_{q+1}(\lambda)\) in the line-218 splitting formula.

**Proposed disposition / dependents:** preserve Lemma 8.2.8 unchanged; optionally append this four-eigenvalue equality case after the lemma, or use it as a numerical/algebraic regression example for the \(q=1\) torsion coefficient bound. The §8.11 coefficient/weighted-Hessian applications are context, not re-proved or certified here. This does not resurrect previous \(m=1\) audit allegations, which are **outside** the actual §8.1 range. A small independent SymPy exact-arithmetic check of \(S_1\), \(S_2\), and the ratio \(4/3\) passed; no build, CI, formal verification, or full proof-chain test was run.

## POME-HEAT-CODIM2-LP-RATE-SHARP-001
**Severity/status:** low / **verified conditional deduction** (quantitative consequence and optimal polynomial exponent for the correct heat-measure lemma). Distinct from historical POME-HEAT-FROSTMAN-CODIM-001, which treated a family of Frostman codimensions and the qualitative \(L^1\) limit.  
**Integrated file:** docs/sections/heat-kernels-on-compact-manifolds/index.html, Git blob c59a1b3fab9433f1aae95db99adb4821857b5d8d, Lemma 3.10.1 (original classical proof) lines 11–79 and Lemma 3.10.5 lines 85–105.  
**Exact label/tag for Lemma 3.10.5:** transcendental-positive-cones:DD00B1CA / 56A174D59425.  
**Hypotheses:** compact Riemannian manifold of real dimension \(d\geq2\), finite positive measure \(\rho\), \(\rho(B_r(x))\leq A r^{d-2}\) for \(0<r\leq r_0\); symmetric, positivity-preserving, mass-one scalar heat kernel. Write \(B=C_X(A+\rho(X))\) for the existing bound \(\|h_t\rho\|_\infty\leq B/t\), \(0<t\leq1\). This statement is conditional on that printed lemma; no new semigroup construction is claimed.

**Uniform quantitative deduction.** Because the heat kernel is symmetric and stochastic,
\[
 \|h_t\rho\|_{L^1(dV)}=\rho(X),\qquad
 \|h_t\rho\|_{L^\infty}\leq B/t.
\]
For \(1<p\leq\infty\), put \(p'=p/(p-1)\) (with \(p'=1\) at \(p=\infty\)). Hölder and the elementary \(L^1\)-\(L^\infty\) interpolation inequality give, for every \(F\in L^p(dV)\),
\[
 \boxed{\quad
 t\left|\int_X(h_t\rho)F\,dV\right|
 \leq B^{1/p}\rho(X)^{1-1/p}\,
       t^{1-1/p}\|F\|_{L^p(dV)}.\quad}
\]
At \(p=\infty\) the prefactor \(B^{1/p}\) is interpreted as one. In particular \(L^p\) data give an explicit uniform \(O(t^{1-1/p})\) rate, while the printed \(p=1\) conclusion is the qualitative \(o(1)\) obtained by truncation.

**Sharpness (one fixed function, not merely \(t\)-dependent test functions).** On the unit flat two-torus choose \(\rho=\delta_0\); the codimension-two ball growth condition holds with \(A=1\). The kernel is the periodization of
\[
 (4\pi t)^{-1}\exp(-|x|^2/(4t)),
\]
so for \(|x|\leq\sqrt t\ll1\) it is bounded below by \(c/t\). Let \(1<p<\infty\) and \(\gamma>1/p\). A nonnegative function supported in \(|x|<1/8\), given in this chart by
\[
 F_p(x)=|x|^{-2/p}(\log(e/|x|))^{-\gamma},
\]
belongs to \(L^p\), since its \(p\)-th power integrates radially as \(\int_0^{1/8} dr/[r(\log(e/r))^{\gamma p}]<\infty\). Integrating only over \(\frac12\sqrt t\leq |x|\leq\sqrt t\) yields
\[
 t(h_tF_p)(0)\geq c_p\,t^{1-1/p}(\log(1/t))^{-\gamma}.
\]
Thus no universal power \(1-1/p+\delta\), \(\delta>0\), works for all fixed \(L^p\) functions, even on this single manifold with fixed \(\rho\). For \(p=\infty\), take \(F\equiv1\), giving \(t(h_tF)(0)=t\), again sharp.

At the endpoint \(p=1\), the fixed integrable function
\[
 F_1(x)=\frac{\mathbf1_{\{|x|<1/8\}}}
 {|x|^2(\log(e/|x|))^2}
\]
satisfies
\[
 t(h_tF_1)(0)\geq c\int_{|x|<\sqrt t}F_1\,dx
 \asymp \frac{1}{\log(1/t)}.
\]
Hence the existing \(o(1)\) in Lemma 3.10.5 cannot be upgraded to any positive uniform polynomial rate for arbitrary fixed \(L^1\) data. These examples extend to any flat real dimension \(d\geq2\) by taking \(\rho=\delta_0\otimes \mathrm{Haar}_{\mathbb T^{d-2}}\) on \(\mathbb T^2\times\mathbb T^{d-2}\), and \(F\) depending only on the first two variables. All estimates then factor exactly through the two-torus model.

**Proposed disposition / dependents:** optional \(L^p\) corollary after Lemma 3.10.5, with the \(p=1\) rate obstruction stated explicitly. This may help quantitative trace estimates, but no application is asserted without checking its hypotheses. The historical Frostman-\(\beta\) finding remains unchanged; this is a different regularity-of-test-function axis. No part of the excluded Demailly approximation/regularization programme was read.

## Independent first selected proof check — §10.88, without a new defect
**Integrated file:** docs/sections/local-sheaf-interfaces-and-regular-function-coherence/index.html, blob c9612e989bb20e042a971bdc48e0b5ab27be9656, Proposition 10.88.2 (demailly-complex-geometry:3A637A7E; permanent 5809CC1BC6C9), lines 7–17.  
The proof's étalé-space argument is correct: equality of two local sections is open, Hausdorffness makes it relatively closed, and local connectedness permits the converse separation of different germs on connected representatives. The local-polynomial sheaf on \(\mathbb C^n\) really is the constant sheaf of rings \(\mathbb C[z_1,\ldots,z_n]\); Noetherian kernel finite generation proves coherence as a sheaf of rings and modules over **that** ring sheaf. Exactness of inverse image similarly preserves finite algebraic presentations of the regular-function localization sheaf on the ordinary topology. Importantly, as the printed proof itself warns, this is *not* coherence as a module over the full analytic holomorphic structure sheaf: the locally polynomial sections are not even closed under multiplication by arbitrary entire functions such as \(e^z\). We did not inspect every upstream algebraic sheaf-coherence theorem or analytic comparison. No confirmed error or duplicate is registered for this selected check.

## Coverage, outstanding limits, and repository operations
The actual current reading ToC contains **747 unique numbered sections**. Newly raised from inventory-only to **selected proposition-proof reading**: **§10.88 only**, namely its Proposition 10.88.2 and lines 7–17. The previously partially reviewed §§8.2 and 3.10 receive *new* sharpness and \(L^p\) checks; neither is counted again as newly opened. No entire section/chapter, all external analytic inputs, or the full project is certified. Outstanding unrelated findings and the historical deferred ledger retain their statuses.

This note proposes changes to reading-edition wording only; it does **not** edit main, manuscript bodies, source repositories, canonicalization registries, stable tags, HTML, or website. No build, GitHub Actions, CI, formalized proof, or publication was run.
