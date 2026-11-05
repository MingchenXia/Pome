# Exact optimality of both relative-energy comparison constants on projective space

**Finding ID:** POME-ENER-PROJECTIVE-BOTH-CONSTANTS-SHARP-001  
**Classification:** low / **verified conditional deduction** (the published theorem and proof are not false).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Audit scope:** integrated Chapter 17, Section 17.3, Definition 17.3.2 / Eq. 17.3.3 and Theorem 17.3.14 / Eq. 17.3.15.  
**Primary reading file:** docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html; blob SHA **16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1**.  
**Physical source lines:** 7–25 (standing model/mass hypotheses), 30–37 (energy definition), 180–190 (theorem, both coefficients), 194–216 (proof), 220–231 (previous different one-dimensional example).  
**Source labels / permanent tags:** Definition 17.3.2: foundations-of-pluripotential-theory:582D55DC / 240EF1DE5889; Eq. 17.3.3: foundations-of-pluripotential-theory:8C7506A6 / F19AAFA93177; Theorem 17.3.14: foundations-of-pluripotential-theory:CF717230 / 69E7D1FEF207; Eq. 17.3.15: foundations-of-pluripotential-theory:14754AD3 / AE35DCCFE783.

## Statement under inspection

The printed inequality, for a positive-mass model potential \(\phi\), \(u\in\mathcal E^1(X,\theta,\phi)\) with \(u\le\phi\), is
\[
 \frac{1}{n+1}\int_X(\phi-u)\,\mu_u
 \ \le -E_\theta^\phi(u)\ \le
 \int_X(\phi-u)\,\mu_u,                 \tag{17.3.15}
\]
where \(\mu_u=\langle(\theta+dd^cu)^n\rangle\), and \(dd^c=(i/2\pi)\partial\bar\partial\). The existing proof of these inequalities is consistent with this normalization. The question **not addressed there** is whether either dimension-dependent coefficient can be improved **uniformly even for smooth strictly positive metrics**.

## Complete all-dimensional smooth projective sharpness model

Let \(n\ge1\), \(X=\mathbf P^n\), \(\theta=\omega=\omega_{\mathrm{FS}}\), normalized by \(\int_X\omega^n=1\), and \(\phi=V_\omega=0\). Write homogeneous coordinates \([Z_0:Z_1:\cdots:Z_n]\). For \(0<t<1\) set
\[
 u_t([Z])=\log\frac{t|Z_0|^2+\sum_{i=1}^n|Z_i|^2}
                   {\sum_{i=0}^n|Z_i|^2}\le0,\qquad
 \omega_t=\omega+dd^c u_t.
\]
Both expressions are globally defined: the ratio is homogeneous of degree zero. The form \(\omega_t\) is the Fubini–Study metric pulled back by the projective linear automorphism
\[
 A_t[Z_0:Z_1:\cdots:Z_n]=[\sqrt t\,Z_0:Z_1:\cdots:Z_n].
\]
Hence \(\omega_t>0\), \(\int_X\omega_t^n=1\), and every \(u_t\) is smooth, bounded, and **strictly \(\omega\)-psh**. The reference \(0\) is a model potential; thus \(u_t\in\mathcal E^\infty(X,\omega,0)\subset\mathcal E^1(X,\omega,0)\). No singular potential or regularization theorem is needed.

Put
\[
 J_j(t)=\int_X(-u_t)\,\omega_t^j\wedge\omega^{n-j},
 \qquad 0\le j\le n.
\]
These integrals are nonnegative. The printed energy definition, without any limit theorem, gives the **exact identities**
\[
 I_t:=\int_X(-u_t)\,\mu_{u_t}=J_n(t),
 \qquad
 -E_\omega(u_t)=\frac{1}{n+1}\sum_{j=0}^nJ_j(t).       \tag{1}
\]

**Top term.** On the affine chart \(Z_0=1\), let \(z=(Z_1,\ldots,Z_n)\). Then
\[
 u_t(z)=\log\frac{t+|z|^2}{1+|z|^2},\quad
 \omega_t=dd^c\log(t+|z|^2).
\]
Under \(z=\sqrt t\,w\), \(\omega_t^n\) becomes the standard probability measure \(\omega_{\rm FS}^n(w)\) on \(\mathbf C^n\). Consequently
\[
 \begin{aligned}
 J_n(t)
 &=\int_{\mathbf C^n}
 \left[\log(1/t)+\log(1+t|w|^2)-\log(1+|w|^2)\right]
 \omega_{\rm FS}^n(w)\\
 &=\log(1/t)-H_n+o(1),\qquad
 H_n=\sum_{k=1}^n\frac1k.                              \tag{2}
 \end{aligned}
\]
For a direct normalization check,
\[
 \omega_{\rm FS}^n=\frac{n!}{\pi^n}
       \frac{dV_{2n}(w)}{(1+|w|^2)^{n+1}},\qquad
 \int_{\mathbf C^n}\omega_{\rm FS}^n=1.
\]
The radial variable \(x=|w|^2\) has probability density
\(n x^{n-1}(1+x)^{-n-1}\,dx\). Substituting \(s=x/(1+x)\) turns this into
\(n s^{n-1}\,ds\), so
\[
 \int\log(1+|w|^2)\,\omega_{\rm FS}^n
 =n\int_0^1s^{n-1}[-\log(1-s)]\,ds=H_n.
\]
Since \(0\le \log(1+t|w|^2)\le\log(1+|w|^2)\) and the last function is integrable, dominated convergence proves (2). The hyperplane \(Z_0=0\) has zero \(\omega_t^n\)-mass; the chart computation is therefore global.

**All lower mixed terms stay bounded.** Fix a small coordinate ball about \(p=[1:0:\cdots:0]\), write \(r=|z|\), and let \(\beta\) denote a standard Euclidean Kähler form. The complex Hessian of \(\log(t+r^2)\) is positive semidefinite with operator norm at most \(C/(t+r^2)\), hence
\[
 0\le \omega_t^j\wedge\omega^{n-j}
 \le C_{n,j}(t+r^2)^{-j}\,dV_{2n},
 \qquad 0\le j<n.
\]
For \(0<r<1\),
\[
 0\le -u_t
 \le\log\frac{1+r^2}{r^2}
 \le C+2|\log r|.
\]
Thus the local integral for \(J_j(t)\) is uniformly bounded by
\[
 C'\int_0^1 r^{2n-1-2j}(1+|\log r|)\,dr<\infty,
 \qquad j<n.                                            \tag{3}
\]
Off \(p\) the functions \(u_t\) and the forms \(\omega_t\) are uniformly smooth and bounded as \(t\downarrow0\), so (3) proves \(J_j(t)=O(1)\) for every \(j<n\). This is exactly where **\(j<n\)** is needed; the corresponding dominating integral at \(j=n\) diverges.

Combining (1)–(3),
\[
 I_t=\log(1/t)+O(1),\qquad
 -E_\omega(u_t)=\frac{\log(1/t)}{n+1}+O(1),
\]
so
\[
 \boxed{\lim_{t\downarrow0}
 \frac{-E_\omega(u_t)}
      {\int_X(-u_t)\,\mu_{u_t}}=\frac1{n+1}.}             \tag{4}
\]
In particular, replacing \(1/(n+1)\) in the **left** side of (17.3.15) by any larger uniform constant is false, *already on smooth strictly positive metrics on projective space*.

**The right coefficient is attained.** Still take \(X=\mathbf P^n\), \(\phi=0\), and \(u=-c\) for any \(c>0\). Then \(\mu_u=\omega^n\),
\[
 -E_\omega(-c)=c=\int_X(0-(-c))\,\mu_{-c}.
\]
Hence replacing the coefficient \(1\) on the **right** side by any smaller uniform constant is false; equality holds for every constant negative shift.

**Conclusion.** Both numbers \(1/(n+1)\) and \(1\) in the printed (17.3.15) are optimal in every complex dimension \(n\ge1\), even if one restricts to the Fubini–Study class and smooth strictly positive Kähler metrics. The argument directly checks the normalizations and distinguishes (4), an asymptotic equality, from the genuine equality for constant shifts. It does not assert equality at the left endpoint for a fixed smooth nonconstant \(u\).

## Status, action, dependencies and exclusion

**Status:** verified conditional deduction / low; **not** a confirmed error and **not** a repaired theorem. The computation is self-contained modulo elementary Fubini–Study formulas and the existing definition (17.3.3). No external Bergman, weighted \(L^2\), Ohsawa–Takegoshi, Demailly approximation or regularization input is used.

**Proposed optional reading-edition note:** immediately after (17.3.15), state that both constants are optimal, with the smooth Fubini–Study family above and constant shifts as witnesses; do not change the theorem, proof, original source, tag, or numbering. The bound is used in relative-energy comparisons and finite-energy tail estimates; no existing dependent result is invalidated. In particular, it rules out improving quantitative arguments that treat (17.3.15) as a universal black box without additional hypotheses.

**Exact newly checked scope:** 17.3.2/3 energy definition; 17.3.14/15 coefficient and hypothesis consistency; selected proof lines 194–216, plus the direct smooth projective computation. Section 17.3 was already partially reviewed in older audit reports. Neither this note nor the elementary model verifies the complete finite-energy characterization, arbitrary-big-class comparison, monotone nets, or the other theorems in §17.3. Whole-section mathematical certification remains **absent**. The owner-excluded regularization and its dedicated programmes stay **deferred-by-user**, not resolved.
