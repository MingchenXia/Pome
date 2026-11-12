# A constructive Kelvin reflection across a zero Dirichlet sphere

**Finding:** POME-HARM-KELVIN-SPHERE-EXPLICIT-COLLAR-001  
**Date:** 2026-11-13  
**Classification:** low; **verified conditional deduction** (a strictly more explicit conclusion than the printed theorem, **not** a source error).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Exact source and scope

* Integrated mathematical reading edition: docs/sections/classical-harmonic-analysis/index.html, blob 75e982788e627af602981823a82863cbd36ee712, §3.3.15 heading, **physical line 215**; Theorem **3.3.17**, original label classical-potential-theory:2BBE313C, permanent tag **14F410C2E770**, statement **lines 229–231**, integrated replacement proof **lines 233–241**.
* Related local classification: Lemma **3.3.16**, original classical-potential-theory:6C6775C3, permanent **B0CFE200676D**, lines **217–226**. Its Riesz/Bocher proof is **not required** for the construction below.
* Kelvin transform: docs/sections/kelvin-transforms-and-half-space-potentials/index.html, blob f2615a5393af724c3996978212162f94911ff9d9, Theorem **3.2.2**, original classical-potential-theory:B1AA5815, permanent **97BA27062B9F**, lines **16–49**, especially Laplacian identity **3.2.3**, original 074F2D29, permanent **0E9BCA99B831**, lines **18–20**.

The printed Theorem 3.3.17 asserts extension only to some $r<|x-a|<R+\varepsilon$. The following direct *fixed-center* formula extends throughout a deterministically specified larger annulus. The original theorem and its existing proof were already partly sampled in an earlier audit; this report does not relabel that historical review as a first visit.

## Verified constructive strengthening

Let $d\ge2$, $0<r<R$, $a\in\mathbb R^d$, and let $h$ be real-valued, continuous on the closed annulus
\[
 A_{r,R}=\{x:r\le |x-a|\le R\},
\]
harmonic on its interior, with $h=0$ on the outer sphere $|x-a|=R$.

Write $\rho=|x-a|$ and
\[
 I(x)=a+\frac{R^2(x-a)}{|x-a|^2}.
\]
Define
\[
 H(x)=
 \begin{cases}
 h(x), &r<\rho\le R,\\
 -\left(\dfrac R\rho\right)^{d-2}h(I(x)),
   &R<\rho<R^2/r.
 \end{cases} \tag{1}
\]
The factor is identically $1$ in dimension $d=2$. **Then $H$ is harmonic on the entire open annulus $r<|x-a|<R^2/r$.** No positivity assumption on $h$, and no a priori boundary derivatives, are needed.

### Proof

**1. Harmonicity on either side and continuity at the interface.** For $\rho>R$, the inversion point $I(x)$ has radius $s=R^2/\rho\in(r,R)$. The second branch is the negative Kelvin transform of $h$ with center $a$ and radius $R$; the printed Theorem 3.2.2 makes it harmonic on $R<\rho<R^2/r$. The first branch is harmonic by hypothesis. As $\rho\downarrow R$, the inversion point approaches the same boundary point, $h$ approaches $0$, and the prefactor approaches $1$, so the two branches join continuously with value zero.

**2. A uniform linear boundary bound, obtained without smooth boundary regularity.** Choose $r<r_0<R$ and set $M=\max_{|x-a|=r_0}|h(x)|$. On $r_0\le \rho\le R$, introduce the radial harmonic barrier
\[
 b(\rho)=
 \begin{cases}
 {\log(R/\rho)}/{\log(R/r_0)},&d=2,\\
 {(\rho^{2-d}-R^{2-d})}/{(r_0^{2-d}-R^{2-d})},&d\ge3.
 \end{cases}
\]
It satisfies $b(r_0)=1$, $b(R)=0$, $b>0$ in between. Apply the maximum principle to both $h-Mb$ and $-h-Mb$. Hence
\[
 |h(x)|\le Mb(\rho)\le C(R-\rho)\quad\text{for $\rho$ sufficiently close to $R$.} \tag{2}
\]
The interior harmonic gradient estimate, which follows by differentiating the ball Poisson formula, yields
\[
 |\nabla h(x)|\le C_d\delta^{-1}
    \sup_{B(x,\delta/2)}|h|\le C',
 \qquad\delta=R-\rho, \tag{3}
\]
for all points sufficiently close to the outer sphere. Indeed every $y$ in that ball has $R-|y-a|\le 3\delta/2$, so (2) controls the displayed supremum. The estimates are uniform in angle. By differentiating the *explicit outer formula*, the same bounded-gradient and linear-vanishing estimates hold just outside $R$.

**3. Distributional gluing with no assumed normal-derivative trace.** It suffices to test $\Delta H$ against a compactly supported smooth $\varphi$ in the larger annulus. Fix $s=R-\varepsilon$ and the paired outer radius $t=R^2/s$. Green's formula applies on the smooth subannuli cut off at $s$ and $t$. The portions with $s<\rho<t$ have vanishing contribution in the limit because $H$ and its first derivatives are locally bounded there, and the width is $O(\varepsilon)$.

Let $h_s(s,\theta)$ be the radial derivative inside at radius $s$. At paired outer points the *exact* radial derivative is
\[
 \partial_\rho H(t,\theta)
 =\left(\frac{s}{R}\right)^d h_s(s,\theta)
  +\frac{d-2}{t}\left(\frac{s}{R}\right)^{d-2}h(s,\theta). \tag{4}
\]
In Green's identity the inner interface contributes $-s^{d-1}\varphi(s,\theta)h_s(s,\theta)$; the outer interface contributes $+t^{d-1}\varphi(t,\theta)\partial_\rho H(t,\theta)$, with surface factors taken relative to $d\theta$. The terms involving $h\,\partial_\rho\varphi$ or $H\,\partial_\rho\varphi$ are $O(\varepsilon)$ by (2). For the radial-gradient terms, (3) bounds $h_s$, $\varphi(t,\theta)-\varphi(s,\theta)=O(\varepsilon)$ uniformly, and
\[
 t^{d-1}(s/R)^d=sR^{d-2}
       =s^{d-1}+O(\varepsilon).
\]
The final term in (4) is also $O(\varepsilon)$ after multiplication by the smooth surface factor, because $h(s,\theta)=O(\varepsilon)$. Thus the *sum* of all interface integrals tends to zero. The two piecewise Laplacians vanish, giving
\[
 \int H\,\Delta\varphi\,dx=0.
\]
Weyl's lemma now gives smooth harmonicity across $\rho=R$, proving the claim.

The proof used no unwarranted boundary $C^1$ regularity: estimate (3) and the *paired-sphere flux cancellation* justified passing to the interface.

## Consequences and limitations

1. The existing local existence conclusion of Theorem 3.3.17 follows with any $0<\varepsilon<R^2/r-R$; indeed the explicit formula provides the whole larger annulus.
2. For nonnegative $h$, the continuation is nonpositive on the exterior side, matching the sign obtained in the original inversion/reflection argument; positivity was not necessary.
3. This is a **constructive strengthening**, not proof that the printed Theorem 3.3.17 or Lemma 3.3.16 is false. It does not claim extension through the image of the inner boundary $|x-a|=R^2/r$, and it does not certify the other harmonic, Riesz or capacity theorems of the chapter.
4. Dependencies actually used are the internally stated Kelvin identity 3.2.3, the elementary annular maximum principle, the ball-Poisson interior gradient bound, Green's formula and Weyl's lemma. These are identified, not asserted to have been transitively fully audited here. No Demailly approximation, Bergman/$L^2$/OT, atlas smoothing or positivity-loss argument appears.

**Proposed source/body change:** optional *separately reviewable* replacement of the present lengthy proof of Theorem 3.3.17 by (1)–(4), with the stronger annulus as a clearly marked corollary. No production or canonical source content was modified. **Affected dependents:** users of Theorem 3.3.17's sphere-reflection operation; no other specific downstream theorem was certified or altered.

**Coverage:** newly checked the entire constructive claim and proof above against the stated hypotheses, plus the exact original 3.3.17 proof and the Kelvin transform identity; Lemma 3.3.16 was read only for dependency contrast. §3.3 already had selected prior coverage: **+0 first-visited numbered sections, +0 fully certified sections**, current actual main table of contents **25 chapters / 747 numbered sections**. No numerical experiment, build, test, CI, website publication, or formal verification performed.
