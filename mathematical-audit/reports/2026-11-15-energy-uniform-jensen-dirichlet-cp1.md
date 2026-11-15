# Mathematical audit — 2026-11-15 — quantitative smooth energy concavity and the exact \(\mathbf P^1\) midpoint defect

**Finding:** POME-ENERGY-SMOOTH-JENSEN-DIRICHLET-001. **Severity:** low. **Status:** verified conditional deduction, not a confirmed error or a repaired printed proof. The original Proposition 17.3.4 and Proposition 17.3.9 are correct in the smooth specialization examined. This is a new quantitative strict-concavity and normalization check, not a certification of the full relative finite-energy theory.

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Integrated reading page:** docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html; Git blob 16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1.

| Stable source label | Permanent tag | Printed item and physical lines |
| --- | --- | --- |
| foundations-of-pluripotential-theory:582D55DC | 240EF1DE5889 | Definition 17.3.2, energy normalization (17.3.3), lines 32–37 |
| foundations-of-pluripotential-theory:44639882 | 9086ABF36774 | Proposition 17.3.4, first variation (17.3.5) and cocycle (17.3.6), lines 41–52, proof 57–93 |
| foundations-of-pluripotential-theory:A392067F | 46190A7C1B2F | Equation 17.3.5, lines 43–45 |
| foundations-of-pluripotential-theory:A4AB3054 | 356D15D0C316 | Proposition 17.3.9, second variation and tangent inequalities (17.3.10), lines 95–118 |

## Exact claim and hypotheses

Let \(X\) be a **connected compact Kähler** manifold of complex dimension \(n\geq1\). Let \(\theta\) and \(\omega\) be smooth Kähler forms and \(u,v\in C^\infty(X,\mathbb R)\) satisfy \(\theta_u:=\theta+dd^cu>0\), \(\theta_v>0\). For the model reference \(\phi=V_\theta=0\), consider the energy \(E=E_\theta^0\) of equation (17.3.3). Define
\[
h=v-u,\quad u_s=(1-s)u+sv,\quad
D_\omega(h)=\int_X dh\wedge d^ch\wedge\omega^{n-1}\geq0.
\]
Suppose more specifically that there are \(0<\lambda\leq\Lambda<\infty\) with
\(\lambda\omega\leq\theta_u,\theta_v\leq\Lambda\omega\). Then for every \(t\in[0,1]\),
\[
\boxed{\quad
\frac{n\lambda^{n-1}}{2}t(1-t)D_\omega(h)
\ \leq\
E(u_t)-(1-t)E(u)-tE(v)
\ \leq\
\frac{n\Lambda^{n-1}}{2}t(1-t)D_\omega(h).
\quad}
\tag{A}
\]
In particular \(E\) is strictly concave along any nonconstant smooth segment modulo additive constants: for \(0<t<1\), equality in the ordinary concavity inequality implies \(v-u\) is constant. A constant difference gives equality in both sides (all three terms vanish).

In **complex dimension one** the comparison hypotheses \(\lambda,\Lambda\) can be dropped, and the two sides agree exactly:
\[
\boxed{\quad E((1-t)u+tv)-(1-t)E(u)-tE(v)
=\frac{t(1-t)}2\int_X d(v-u)\wedge d^c(v-u).\quad}
\tag{B}
\]
The coefficient \(1/2\) is therefore exact and cannot be increased. No assertion of sharpness of \(\lambda^{n-1}\), \(\Lambda^{n-1}\) for \(n>1\) is made.

## Complete smooth proof (no excluded approximation input)

The polynomial first-variation identity (17.3.5), verified for smooth forms directly by expanding \(\theta_{u_s}^n\), gives
\[
g'(s)=\int_Xh\,\theta_{u_s}^n,\qquad g(s)=E(u_s).
\]
As \(d\theta_{u_s}=0\), differentiating under the integral and using ordinary Stokes on compact \(X\) yields the exact second variation
\[
g''(s)=n\int_Xh\,dd^ch\wedge\theta_{u_s}^{n-1}
=-n\int_Xdh\wedge d^ch\wedge\theta_{u_s}^{n-1}.
\tag{C}
\]
Here \(dd^c=i(2\pi)^{-1}\partial\bar\partial\) and
\(dh\wedge d^ch=i(2\pi)^{-1}\partial h\wedge\bar\partial h\geq0\);
there are no hidden \(n!\) or \(\pi\) factors.

A twice continuously differentiable \(g:[0,1]\to\mathbb R\) obeys the **exact Green-kernel identity**
\[
g(t)-(1-t)g(0)-tg(1)
=\int_0^1 K_t(s)[-g''(s)]\,ds,\quad
K_t(s)=
\begin{cases}(1-t)s,&s\leq t,\\t(1-s),&s\geq t.\end{cases}
\tag{D}
\]
Indeed both sides vanish at \(t=0,1\) and have the same second derivative in \(t\). The kernel is nonnegative and \(\int_0^1K_t(s)\,ds=t(1-t)/2\).
The endpoint form bounds imply \(\lambda\omega\leq\theta_{u_s}\leq\Lambda\omega\) for all \(s\). Monotonicity of wedge products of semipositive forms implies
\[
n\lambda^{n-1}D_\omega(h)\leq -g''(s)
\leq n\Lambda^{n-1}D_\omega(h).
\]
Integrating this against \(K_t\) proves (A). Positivity of the Kähler metric implies \(D_\omega(h)=0\) exactly when \(dh=0\); connectedness then makes \(h\) constant. When \(n=1\), the factor \(\theta_{u_s}^{n-1}\) in (C) is identically \(1\), giving (B) without uniform form bounds.

## Exact normalization and strictness model on \(\mathbf P^1\)

Use the Fubini–Study form of total mass one
\[
\omega=dd^c\log(1+|z|^2)
=\frac{i}{2\pi}\frac{dz\wedge d\bar z}{(1+|z|^2)^2}
\]
on \(\mathbf P^1\), and the globally smooth nonconstant function
\(f(z)=|z|^2/(1+|z|^2)\) (with \(f(\infty)=1\)). Write \(r=|z|^2\). Direct differentiation gives
\[
dd^cf=\frac{1-r}{1+r}\omega,\qquad
\int_X f\,\omega=\int_0^\infty\frac{r}{(1+r)^3}\,dr=\frac12,\qquad
\int_Xdf\wedge d^cf=\int_0^\infty\frac{r}{(1+r)^4}\,dr=\frac16.
\]
For \(u=0\) and \(v=\varepsilon f\), \(0<\varepsilon<1\), one has
\(\omega_{\varepsilon f}\geq(1-\varepsilon)\omega>0\). From (17.3.3) and Stokes,
\[
E_\omega(\varepsilon f)=\frac{\varepsilon}{2}
-\frac{\varepsilon^2}{12},\qquad
E_\omega(\varepsilon f/2)-\frac{E_\omega(0)+E_\omega(\varepsilon f)}2
=\frac{\varepsilon^2}{48}.
\tag{E}
\]
The explicit tangent bounds are
\[
\int_X\varepsilon f\,\omega_{\varepsilon f}
=\frac\varepsilon2-\frac{\varepsilon^2}6
\leq E_\omega(\varepsilon f)-E_\omega(0)
=\frac\varepsilon2-\frac{\varepsilon^2}{12}
\leq\int_X\varepsilon f\,\omega=\frac\varepsilon2.
\]
All constants agree with the printed curvature normalization and inequalities (17.3.10). The exact rational beta-integral arithmetic for (E) was also run independently, using the elementary identity \(B(a,b)=(a-1)!(b-1)!/(a+b-1)!\); see the separate small check. That check does not verify the analytic arguments or the full repository.

## Mathematical verdict, dependencies, and limits

**Verified conditional deduction.** The selected smooth specialization of the printed first/second variation is valid; (A) is a quantitative strengthening, and (B)/(E) provide a sharp, independently computed one-dimensional control example. No missing hypothesis was identified **in those printed statements**. The proposed addition is an optional lemma or remark after Proposition 17.3.9, preserving existing source labels and tags. The main repository and reading edition remain unchanged.

The proof uses compact Kähler Stokes and elementary positive-form wedge monotonicity, not any Demailly approximation, Bergman kernel, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme. It does **not** extend the quantitative inequality to arbitrary singular finite-energy endpoints, nor independently certify Theorem 17.2.5, Lemma 17.2.7, the non-pluripolar polynomial calculus, Proposition 17.3.19, or downstream geodesic-energy assertions (§§17.7–17.9). Their transitive proof dependencies are unaffected. Prior audit findings and deferred-by-user statuses are preserved.

**Coverage:** direct inspection of §17.3.2/.4/.9 and equations (17.3.3/.5/.6/.10) at the above physical lines; no first visit to an unreviewed section and no complete section or chapter certification. Current main ToC: 25 chapters, 747 numbered sections. No build, CI, formal verification, publication or main/source/registry edit.
