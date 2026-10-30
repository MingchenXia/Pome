# A pluriclosed metric with invariant mass and an explicitly nonconservative Monge–Ampère one-form

**Date:** 2026-10-30. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Branch:** `review/mathematical-audit`. **Finding:** `POME-HERM-TORUS-CURL-001`; **severity:** low; **status:** verified conditional deduction. This is an independent, smooth compact model, *not* a false Pome theorem, a proof-gap adjudication, or a repair of a general theorem.

## Pinned reading-edition targets and scope

- `docs/sections/torsion-and-the-variation-of-mass/index.html`, production blob `9abec9685e33a1b40f9c0765381408eb52b325d3`: Theorem **11.1.5**, source `non-kahler-pluripotential-theory:D4902E5B`, permanent tag `2B3316345A4A`, lines **69–92**; Theorem **11.1.7** (Chiose), source `non-kahler-pluripotential-theory:5CD99CBA`, tag `FB90FC741F25`, lines **100–147** (smooth mass-equivalence clauses only); Corollary **11.1.10**, source `non-kahler-pluripotential-theory:9CD9DB11`, tag `2C05FFD39C6D`, lines **185–189**.
- `docs/sections/monge-ampere-energy-and-torsion/index.html`, production blob `fe1ca06167b8f5bc9868e9a9876397afad4e7ff5`: Monge–Ampère one-form §**11.2.1**, section tag `49D0776D0F6B`, lines **12–26**; Lemma **11.2.2**, source `non-kahler-pluripotential-theory:37DA4A81`, permanent tag `8A9C3139B5B5`, lines **29–49**; Theorem **11.2.4**, source `non-kahler-pluripotential-theory:788EACD6`, tag `7D069B347672`, lines **68–94**; radial-energy definition **11.2.7**, lines **98–111**; Proposition **11.2.10**, source `non-kahler-pluripotential-theory:0618CCAD`, tag `4793125897B2`, lines **146–175**; Proposition **11.2.12**, source `non-kahler-pluripotential-theory:7B725E3F`, tag `0009683E4137`, lines **180–205**, especially Eq. **11.2.13**, tag `173E9E78941E`, lines **184–194**.

The independent new calculation below checks the distinction between constant *total mass* and integrability of the *Monge–Ampère one-form*. Earlier §11.1 surface-mass and §11.2 radial-energy records remain separate; this is the first explicit constant nonzero curl/circulation model in this audit ledger. No bounded-psh approximation or other user-excluded regularization argument is revisited.

## Explicit Gauduchon metric on a complex torus

Let
\[
 X=\mathbb C^2/(\mathbb Z+i\mathbb Z)^2,\qquad
 z_j=x_j+iy_j,\quad
 dV=dx_1\wedge dy_1\wedge dx_2\wedge dy_2,
 \quad f(x_1)=\cos(2\pi x_1),
\]
and fix \(0<\varepsilon<1\). Define
\[
 \omega_\varepsilon=\frac i2\left(
 dz_1\wedge d\bar z_1+dz_2\wedge d\bar z_2
 +\varepsilon f(x_1)
 (dz_1\wedge d\bar z_2+dz_2\wedge d\bar z_1)\right).
\]
The Hermitian matrix \(\bigl(\begin{smallmatrix}1&\varepsilon f\\
\varepsilon f&1\end{smallmatrix}\bigr)\) has eigenvalues
\(1\pm\varepsilon f>0\). The sole nonconstant coefficients depend on
\(x_1\); in \(\partial\bar\partial\omega_\varepsilon\), their Hessian
\(dz_1\wedge d\bar z_1\) wedges either with \(dz_1\) or with
\(d\bar z_1\), so *both* terms vanish. Thus
\[
 dd^c\omega_\varepsilon=0,\qquad d\omega_\varepsilon\ne0
\]
(the latter because \(f\) is nonconstant). The complex torus itself
admits the flat Kähler form, so the nonclosed obstruction belongs to
this **chosen metric**, not to the complex manifold.

Writing \(\omega_{\varepsilon,u}=\omega_\varepsilon+dd^cu\), integration
by parts, as in the *smooth* part of Corollary 11.1.10, yields for **every**
smooth real \(u\)
\[
 \int_X\omega_{\varepsilon,u}^2
 =\int_X\omega_\varepsilon^2
 =2\int_X(1-\varepsilon^2 f^2)dV
 =\boxed{2-\varepsilon^2}.
\]
No bounded-potential convergence assertion is needed.

## Constant two-form curl and exact nonzero circulation

Use the Pome normalization \(dd^c=\frac{i}{2\pi}\partial\bar\partial\).
For a real periodic function \(h=h(x_1,x_2)\),
\[
 dd^ch=\frac{i}{8\pi}\sum_{j,k=1}^2
 h_{x_jx_k}\,dz_j\wedge d\bar z_k,\qquad
 dd^ch\wedge\omega_\varepsilon
 =\frac{h_{11}+h_{22}-2\varepsilon f h_{12}}{4\pi}\,dV.
 \tag{*}
\]
On the open convex set
\(\mathcal H_{\omega_\varepsilon}=\{u:\omega_{\varepsilon,u}>0\}\),
put \(\alpha_u(h)=\int_Xh\,\omega_{\varepsilon,u}^2\).
Its directional derivative is
\[
 D_a\alpha_u(b)=2\int_Xb\,dd^ca\wedge(\omega_\varepsilon+dd^cu).
\]
For any smooth real \(a,b,u\), the two terms containing \(dd^cu\)
cancel in the antisymmetrization, because \(dd^cu\) is \(d\)-closed and
the integration-by-parts pairing of Lemma 11.2.2 is symmetric. Hence
\[
 (d\alpha)_u(a,b)
 :=D_a\alpha_u(b)-D_b\alpha_u(a)
 =2\int_X(b\,dd^ca-a\,dd^cb)\wedge\omega_\varepsilon.
 \tag{**}
\]
**This curl is independent of \(u\)**, not merely at one base point.

Take the globally defined real trigonometric functions
\[
 v=\sin(2\pi x_1)\sin(2\pi x_2),
 \qquad w=\cos(2\pi x_2).
\]
Here \(v_{12}=4\pi^2\cos(2\pi x_1)\cos(2\pi x_2)\) and
\(w_{12}=0\). The terms involving the flat Laplacian in (*) cancel by
periodic integration by parts, and
\[
 \int_X f\,w\,v_{12}\,dV
 =4\pi^2\left(\int_0^1\cos^2(2\pi x_1)\,dx_1\right)
 \left(\int_0^1\cos^2(2\pi x_2)\,dx_2\right)=\pi^2.
\]
Consequently
\[
 \boxed{(d\alpha)_u(v,w)=-\varepsilon\pi}
 \qquad\text{for every }u\in\mathcal H_{\omega_\varepsilon}.
 \tag{1}
\]

For sufficiently small \(s,t>0\), the whole rectangle
\(u=r v+q w\), \(0\le r\le s\), \(0\le q\le t\), lies in
\(\mathcal H_{\omega_\varepsilon}\). Traverse its boundary in the order
\(0\to sv\to sv+tw\to tw\to0\), identifying \(\alpha\) with its
restriction to this two-plane. Stokes' formula on the parameter
rectangle and (1) give the **exact, finite** line integral
\[
 \boxed{\oint_{\partial[0,s]\times[0,t]}\alpha
       =-\varepsilon\pi st\ne0}.                 \tag{2}
\]
Thus, even though **the entire smooth Monge–Ampère mass is constant**,
the one-form is not locally exact. This is fully consistent with the
correct Theorem 11.2.4 and supplies a Kähler-admitting compact example,
where the printed explanatory example instead uses a manifold with no
Kähler metric.

## Independent radial-energy crosscheck

In complex dimension two, the printed radial energy has
\[
 E_\omega(u)=\int_X u\omega^2+
 \int_Xu\omega\wedge dd^cu+
 \frac13\int_Xu(dd^cu)^2.
\]
Differentiation and integration by parts with the closed \(dd^cu\)
show *exactly*
\[
 DE_{\omega,u}(b)-\alpha_u(b)
 =\int_X(u\,dd^cb-b\,dd^cu)\wedge\omega.
 \tag{3}
\]
For \(u=sv\), \(b=w\), the same Fourier calculation gives
\[
 \boxed{DE_{\omega_\varepsilon,sv}(w)
       -\alpha_{sv}(w)=\tfrac12\varepsilon\pi s}. \tag{4}
\]
This is also the specialization of the torsion expression
Eq. 11.2.13: its \(u\,dd^c\omega\) term is zero in this model,
but its first-order torsion terms remain nonzero. In particular,
the radial energy does not magically integrate \(\alpha\) when
\(dd^c\omega=0\) but \(d\omega\ne0\).

## Adjudication, dependents, and coverage

**Status:** low / **verified conditional deduction**. The original
Theorem 11.2.4, Corollary 11.1.10, and Propositions 11.2.10/12 are
correct in this model. **No false theorem, demonstrated proof gap,
general conditional repair, or full-section certification is claimed.**
Suggested nonproduction enhancement: optionally insert this explicit
torus/Fourier model after Theorem 11.2.4, with the short exact
radial-energy identity after Proposition 11.2.12. Retain Chiose
attribution, original source variants, permanent tags, all conventions
and source history. Dependents: the interpretation of smooth
mass-invariance §11.1.7/.10, local exactness §11.2.2/.4, and torsion
variation §11.2.10/.12. No canonicalization or duplicate deletion is
proposed.

**Actual work in this pass:** reread main integrated statements/proof
steps §11.1.5/.7/.10 and §11.2.1–.4/.7/.10/.12; derived (1)–(4)
directly on the compact torus. Midpoint quadrature on a 100-by-100
periodic grid for \(\varepsilon=.1,.3,.7\) independently reproduced
\(-\varepsilon\pi\) and \(2-\varepsilon^2\); it was not a project test or
formal proof. No full chapter or section, no transitive smooth
elliptic/analytic prerequisites, and specifically **no bounded-psh
approximation** is certified. The standing actual table of contents
has **25 chapters and 747 numbered sections**; zero complete-section
certifications. Historical open/verified/resolved entries are unchanged.
Demailly approximation/regularization and the dedicated Bergman,
\(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss
proof-completion work stay strictly **deferred-by-user**, unexamined.
No source/body, canonical registry, site, main, CI, build, publication,
or formalization changes.
