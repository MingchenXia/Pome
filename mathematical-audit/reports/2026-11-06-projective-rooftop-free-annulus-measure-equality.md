# Audit 2026-11-06 — exact free annulus for a smooth projective rooftop

**Finding ID:** POME-ENV-CP1-ROOFTOP-FREE-ANNULUS-001  
**Status / severity:** verified conditional deduction / low.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--concentration-on-the-contact-set/index.html, blob 840ebcb98be09245369315fa0c0288b936040098, physical lines 69–74 (Theorem 16.13.4), 153–165 (Corollary 16.13.5), and 10–27 (Lemma 16.13.1).  
**Source / permanent tags:** foundations-of-pluripotential-theory:DDE3B556 / 38E18A798D6B (Theorem 16.13.4); foundations-of-pluripotential-theory:FE439A00 / 7FE9391D7A51 (Corollary 16.13.5); foundations-of-pluripotential-theory:86AF9332 / 15A418789279 (Lemma 16.13.1). The obstacle definition is foundations-of-pluripotential-theory:7FB6072B / A4F165851008 (Definition 16.11.3), integrated in docs/sections/envelopes-and-model-potentials--obstacles-and-rooftops/index.html, blob e9129aaaab9e9f172da9704bffe939839f8afeb6, physical lines 76–84.  
**Scope:** first selected, explicit-model check of §16.13.4–5 and radial envelope compatibility; not a complete verification of §16.13 or its imported capacity arguments. No Demailly regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale atlas, or positivity-loss argument is used.

## Statement and hypotheses actually tested

Let $X=\mathbf P^1$ with $z=Z_1/Z_0$ on the standard affine chart and
$\theta=\omega_{\mathrm{FS}}=dd^c\log(1+|z|^2)$, where $dd^c=(i/2\pi)\partial\bar\partial$ and $\int_X\theta=1$.
The two globally smooth, strictly $\theta$-psh potentials are
\[
u(z)=0,\qquad
v(z)=\log\frac{4+|z|^2}{1+|z|^2}-\log2.
\]
Indeed, $\theta+dd^cv=dd^c\log(4+|z|^2)$ on the affine chart, the pullback of Fubini–Study by the projective automorphism $[Z_0:Z_1]\mapsto[2Z_0:Z_1]$; it is strictly positive also at infinity. The obstacle $f=\min\{u,v\}$ is bounded and continuous, and the competitor family is nonempty (a sufficiently negative constant lies below $f$). The big-class, quasi-continuity, bounded-above, and nontrivial-rooftop hypotheses of the printed Theorem 16.13.4 and Corollary 16.13.5 are therefore satisfied without any singular-potential or regularization assumption.

## Exact envelope

Put $t=\log|z|^2$ on $\mathbf C^*$, with $F_0(t)=\log(1+e^t)$, $F_1(t)=\log(4+e^t)-\log2$.
The global envelope $w=P_\theta(f)$ is explicitly
\[
 w(z)=
 \begin{cases}
  0,&|z|\le1,\\
  \log2+\tfrac12\log|z|^2-\log(1+|z|^2),&1\le|z|\le2,\\
  v(z),&|z|\ge2 .
 \end{cases} \tag{A}
\]
The boundary points $z=0,\infty$ use their smooth limiting formulas.

**Derivation, without assuming a radial envelope formula.**
For a rotation-invariant $\theta$-psh function $\psi$, the function $H(t)=F_0(t)+\psi(e^{t/2})$ is convex: on $\mathbf C^*$, $dd^cH(\log|z|^2)\ge0$ is equivalent to $H''\ge0$ as a distribution. Conversely a continuous convex $H$ with the displayed projective end behavior defines a global bounded $\theta$-psh potential.

The two strictly convex functions $F_0,F_1$ have a common supporting affine function
$\ell(t)=\log2+t/2$ touching $F_0$ at $a=0$ and $F_1$ at $b=\log4$. Direct differentiation gives
$F'_0(0)=F'_1(\log4)=1/2$, $F_0(0)=\ell(0)=\log2$, and
$F_1(\log4)=\ell(\log4)=\log4$.
Also $F_0\le F_1$ for $t\le\log2$, whereas $F_1\le F_0$ for $t\ge\log2$.
Therefore
\[
 H(t)=\begin{cases}
 F_0(t)&t\le0,\\
 \ell(t)&0\le t\le\log4,\\
 F_1(t)&t\ge\log4
 \end{cases}
\]
is convex, globally $C^1$, and lies below $F=\min(F_0,F_1)$.
It is the **largest convex minorant** of $F$: any convex $K\le F$ obeys
$K(t)\le F_0(t)=H(t)$ for $t\le0$ and $K(t)\le F_1(t)=H(t)$ for $t\ge\log4$;
for $0<t<\log4$, the convexity inequality between endpoints bounds $K(t)$ by the chord $\ell(t)=H(t)$.
Thus $H-F_0$ is a $\theta$-psh competitor.

For completeness, the *unrestricted* envelope is rotation invariant: rotations preserve $\theta$, $f$, and the family of competitors, hence preserve its pointwise supremum and its USC regularization. For a bounded continuous obstacle $f$, any PSH competitor $\psi\le f$ quasi-everywhere actually satisfies $\psi\le f$ everywhere: in a coordinate disk, apply the submean inequality to $\psi$ after adding a local smooth potential for $\theta$, remove the negligible pluripolar exceptional set from the area integral, and use continuity of $f$ while shrinking the disk. Hence the unrestricted envelope, which is itself a competitor by Proposition 16.11.4, is a radial convex minorant and cannot exceed $H-F_0$. Since $H-F_0$ is already a competitor, (A) follows. The reliance on the stated envelope-existence/USC property is an **internal dependency**, not a complete independent reconstruction of Proposition 16.11.4.

## Exact measure and free boundary

Because the complex dimension is one and $w$ is bounded, the non-pluripolar Monge–Ampère measure is the ordinary positive current
$\mu_w=\theta+dd^cw=dd^cH(\log|z|^2)$.
The matching first derivatives at $t=0$ and $t=\log4$ show that the distributional second derivative has **no Dirac masses** on either boundary circle. The middle branch is affine in $t$ and therefore pluriharmonic on the annulus. In Euclidean area $dA=dx\,dy$,
\[
 d\mu_w
 = \mathbf1_{\{|z|<1\}}\frac{dA}{\pi(1+|z|^2)^2}
   +\mathbf1_{\{|z|>2\}}\frac{4\,dA}{\pi(4+|z|^2)^2}. \tag{B}
\]
Neither circle $|z|=1$ nor $|z|=2$ carries mass; the smooth point at infinity carries none.
Direct polar integration gives
\[
 \mu_w(\{|z|\le1\})=\int_0^1\frac{2r}{(1+r^2)^2}\,dr=\tfrac12,\qquad
 \mu_w(\{|z|\ge2\})=\int_2^\infty\frac{8r}{(4+r^2)^2}\,dr=\tfrac12.
\]
There is a **nonempty open free annulus** $\{1<|z|<2\}$ on which $w<f$ strictly, and $\mu_w$ vanishes identically there.
The contact sets are exactly $\{w=u\}=\{|z|\le1\}$ and $\{w=v\}=\{|z|\ge2\}$.
Consequently the printed domination estimate in Corollary 16.13.5 is an **exact equality** in this model,
\[
 \boxed{\;\mu_w=\mathbf1_{\{w=u\}}\mu_u+\mathbf1_{\{w=v\}}\mu_v\;},
\]
with two nonzero, mutually singular summands of mass $1/2$ each.
The contact-set concentration of Theorem 16.13.4 is likewise exact, and its statement must **not** be strengthened to say that the contact set is connected or that the free region has zero area.

## Mathematical classification and downstream relevance

**Verified conditional deduction / low**, not a printed theorem error, proof gap, or general theorem certification. The explicit formula (A), the convex envelope calculation, the distributional boundary check and the exact masses (B) are independent computations; identifying them with the globally defined $P_\theta$ uses the integrated Proposition 16.11.4 (USC envelope belongs to the competitor class). The finding tests the sharp possibility of equality in the measure inequality of §16.13.5 with both terms simultaneously nonzero, and illustrates §16.13.4's distinction between support of $\mu_w$ and the much larger unconstrained free set. Affected conceptual dependents include contact-measure formulas in §16.14 and rooftop mass estimates in §16.23, **not** independently reviewed here.

**Proposed correction:** none to the printed theorem or its proof. Optional explanatory example after Corollary 16.13.5, retaining every historical attribution and permanent tag. This is a new selected examination of §16.13.4–5 only, not a claim about the rest of §16.13, its Bedford–Taylor prerequisites, or other project sections. All user-deferred approximation/regularization and dedicated auxiliary proof work remains deferred-by-user.

**Check performed:** exact derivative and radial integration by hand in the above proof. No software test, build, browser rendering, CI, publication, or formal mathematical verification was performed.