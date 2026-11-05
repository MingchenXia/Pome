# Uniform boundary Hopf lower bound and the maximal power-exhaustion exponent

**Finding ID:** POME-BOUNDARY-NEG-PSH-HOPF-LINEAR-001  
**Date:** 2026-11-05  
**Severity:** low  
**Classification:** verified conditional deduction (not a false printed theorem, proof gap, or completed repair).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading edition:** \`docs/sections/boundary-levi-geometry-and-holomorphic-extension--bounded-power-exhaustions-at-a-smooth-pseudoconvex-boundary/index.html\`, main blob \`3c2f1e7af53a9f7c86ca718d47e5054679ff75a7\`, physical lines **7–16** (definition and statement), **21–74** (the printed argument). Theorem **9.35.1** source label \`demailly-complex-geometry:8B2CF5E4\`, permanent tag **AC8A460928B4**. The supporting signed-distance collar occurs in Theorem **9.34.2**, source \`demailly-complex-geometry:3D6302E9\`, permanent tag **8F39CE9F0DBB**, \`docs/sections/boundary-levi-geometry-and-holomorphic-extension--boundary-levi-geometry/index.html\`, main blob \`fe5ebfa26a59b083027a10b66fcc13bddad8acbc\`, physical lines **47–61**.

## Statement established in this audit

Let \(\Omega\subset\mathbb C^n\) be a nonempty bounded domain with compact \(C^2\) boundary. Let \(v\in C(\overline\Omega)\) be **real subharmonic** (in the \(2n\)-dimensional real sense) on \(\Omega\), with \(v<0\) throughout \(\Omega\) and \(v=0\) on \(\partial\Omega\). Then for some constants \(c>0\) and \(\varepsilon>0\), both dependent on \(v\) and \(\Omega\),
\[
                    -v(z)\ \geq\ c\,\delta_\Omega(z),
       \qquad 0<\delta_\Omega(z)<\varepsilon. \tag{1}
\]
Consequently a negative psh exhaustion satisfying the boundary conditions of printed Theorem 9.35.1 **cannot** satisfy an upper estimate
\[
                -v(z)\leq C\,\delta_\Omega(z)^\gamma
                \quad\hbox{in a full boundary collar} \tag{2}
\]
for any exponent \(\gamma>1\). This is a genuine upper bound on *any* possible boundary power exponent; it does not claim that the endpoint \(\gamma=1\) is obtainable for every pseudoconvex \(\Omega\).

The endpoint is attained on the unit ball \(B\subset\mathbb C^n\) by \(v(z)=|z|^2-1\):
\[
         \delta_B(z)\leq-v(z)=(1+|z|)\delta_B(z)\leq2\delta_B(z).
\]
Moreover for every \(0<\eta\leq1\), \(v_\eta=-(1-|z|^2)^\eta\) is strictly psh and exhibits the power \(\eta\). Thus **one is the maximal possible exponent in the class of bounded smooth pseudoconvex domains**, and this upper bound is sharp already on the ball. The original existence assertion with some \(\eta\in(0,1)\) remains correct.

## Complete elementary proof of (1)

Fix a uniform interior tangent-ball radius \(R>0\), obtainable from compact \(C^2\) boundary: for each \(p\in\partial\Omega\), with outward Euclidean unit normal \(\nu(p)\), the closed ball \(\overline B(c_p,R)\), \(c_p=p-R\nu(p)\), meets \(\partial\Omega\) only at \(p\) and its open interior is contained in \(\Omega\). Decrease \(R\) if needed so that points of boundary distance \(t<\varepsilon\) have the unique normal representation \(z=p-t\nu(p)\), with \(\varepsilon<R/2\). These are standard consequences of the compact \(C^2\) signed-distance collar (the geometry in integrated 9.34.2); no potential approximation theorem enters here.

Set \(r=R/2\), \(d=2n\) and \(K=\{z\in\overline\Omega:\delta_\Omega(z)\geq r\}\). This set is compact, lies in the interior, and is nonempty. Since \(v<0\), \(a=-\max_K v>0\). Every point \(y\in\partial B(c_p,r)\) has \(\delta_\Omega(y)\geq R-r=r\): the entire open tangent ball belongs to \(\Omega\). Hence \(v(y)\leq-a\), uniformly in \(p\).

On the annulus \(A_p=\{r<|z-c_p|<R\}\), introduce \(h_p(z)=-a Q_d(|z-c_p|)\), where
\[
 Q_d(s)=
 \begin{cases}
 \displaystyle\frac{\log(R/s)}{\log(R/r)}, &d=2,\\[6pt]
 \displaystyle\frac{s^{2-d}-R^{2-d}}{r^{2-d}-R^{2-d}}, &d\geq3.
 \end{cases}
\]
This is harmonic, equals \(-a\) on the inner sphere and \(0\) on the outer sphere. On the outer sphere, \(v\leq0\); on the inner, \(v\leq-a\). The subharmonic maximum principle therefore gives \(v\leq h_p\) on \(A_p\). The outer sphere may meet \(\partial\Omega\) at \(p\), but continuity on \(\overline\Omega\) makes the same comparison valid there.

Now \(Q_d'(s)<0\) and \(-Q_d'(s)\geq-Q_d'(R)\) for \(r\leq s\leq R\). For \(z=p-t\nu(p)\), \(0<t<\varepsilon\), we have \(|z-c_p|=R-t\) and \(\delta_\Omega(z)=t\). Thus
\[
 -v(z)\geq aQ_d(R-t)
       =a\int_{R-t}^{R}[-Q_d'(s)]\,ds
       \geq a[-Q_d'(R)]\,t.
\]
The explicit positive uniform constant is
\[
 c=
 \begin{cases}
       a/(R\log2),& d=2,\\
       a(d-2)/[R(2^{d-2}-1)],& d\geq3.
 \end{cases}
\]
This proves (1). If (2) held with \(\gamma>1\), dividing \(c t\leq C t^\gamma\) by \(t\) and letting \(t\downarrow0\) would be impossible.

For completeness the ball examples are checked by differentiating with \(s=1-|z|^2\):
\[
 \partial\bar\partial v_\eta
  \equiv\eta s^{\eta-1}I+
        \eta(1-\eta)s^{\eta-2}\,\bar z\otimes z
\]
in the complex Hessian matrix convention. This is positive definite for \(0<\eta\leq1\). No Bedford–Taylor limits, Demailly regularization, Bergman kernels, weighted \(L^2\), Ohsawa–Takegoshi, or positivity-loss argument is used.

## Classification, scope and suggested edit

Theorem 9.35.1 is **not false** and no part of its original proof is claimed to be repaired. This is a new quantitative boundary obstruction complementing, but mathematically distinct from, the earlier audit \`POME-PSH-BOUNDARY-COMPLETE-METRIC-001\`: that work used the produced exhaustion to construct a complete Kähler metric; here the comparison principle proves a universal *upper* limit for possible decay exponents without requiring pseudoconvexity.

**Suggested reading-edition addition, as a proposed patch only:** after Theorem 9.35.1, add a short remark distinguishing existence of some \(0<\eta<1\) from the sharp global ceiling \(\eta\leq1\), with the tangent-ball harmonic barrier and unit-ball endpoint. Do not imply existence of a global psh defining function at \(\eta=1\) on every smooth pseudoconvex domain. The only affected downstream interpretation is any attempt to strengthen the theorem to boundary power \(>1\); no printed dependent result is shown false.

**Actual audit coverage:** one new complete proof of the boundary obstruction tied to the hypotheses of Theorem 9.35.1, direct re-reading of the theorem and its collar Hessian calculation, and the signed-distance geometric hypothesis in 9.34.2. Not an independent certification of Oka's criterion, global Richberg gluing, Theorem 9.34.2, all of 9.35, or Chapter 9. Historical attribution and stable tags remain unchanged. **25 chapters / 747 numbered sections / zero fully mathematically certified sections.**
