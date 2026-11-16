# POME-MART-STRIP-TWO-END-MINIMAL-001: the two minimal Martin ends of the infinite strip

**Date:** 2026-11-16. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Classification:** **low / verified conditional deduction**, **not** a false printed theorem or an unconditional certification of its full upstream proof.

## Source anchors and scope

- `docs/sections/green-energy-and-martin-boundaries/index.html` (main blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`): Lemma 4.5.8, lines 94–101, source `classical-potential-theory:AB110663`, tag `D878F27BAB16`; Theorem 4.5.9, lines 106–121, source `classical-potential-theory:1677A9F0`, tag `9D6B5CF5E0CF`; Theorem 4.5.12, lines 165–185, source `classical-potential-theory:57D18B4C`, tag `6736FBE7368C`; Theorem 4.5.13, lines 189–212, source `classical-potential-theory:854603A2`, tag `0E65F552B1A6`.
- `docs/sections/kelvin-transforms-and-half-space-potentials/index.html` (blob `f2615a5393af724c3996978212162f94911ff9d9`): Theorem 3.2.6, lines 64–75 and 80–129, source `classical-potential-theory:1C8A330A`, tag `6BC86EEF03A9`. The existence part of its weighted positive half-plane Poisson representation is an **internal conditional input**; its uniqueness is proved below for this application.
- Excluded user-deferred Demailly approximation, specialized Bergman/weighted-L²/OT, multiscale atlas and positivity-loss completion programmes were not examined.

## Statement

Consider \(S=\{(s,t):s\in\mathbb R,\ 0<t<\pi\}\) with \(a=(0,\pi/2)\). The **entire** Martin compactification is the strip together with its two finite horizontal boundary lines and **two distinct end points**, denoted \(+\infty\) and \(-\infty\). Every boundary point is minimal. Normalizing all kernels to take value one at \(a\), the two end kernels are
\[
 K_{+\infty}(s,t)=e^s\sin t,\qquad K_{-\infty}(s,t)=e^{-s}\sin t.
\]
For finite \(r\in\mathbb R\), the side kernels are
\[
 K_{(r,0)}(s,t)=\frac{(1+e^{2r})e^s\sin t}{e^{2s}+e^{2r}-2e^{s+r}\cos t},\quad
 K_{(r,\pi)}(s,t)=\frac{(1+e^{2r})e^s\sin t}{e^{2s}+e^{2r}+2e^{s+r}\cos t}.
\]
Every nonnegative harmonic \(h\) on \(S\) admits a **unique** representation
\[
 h=c_+K_{+\infty}+c_-K_{-\infty}+
 \int_{\mathbb R}K_{(r,0)}\,d\nu_0(r)+
 \int_{\mathbb R}K_{(r,\pi)}\,d\nu_\pi(r),
\]
with nonnegative \(c_\pm\), finite positive \(\nu_0,\nu_\pi\), and
\(c_++c_-+\nu_0(\mathbb R)+\nu_\pi(\mathbb R)=h(a)\).
These are normalized **Martin** boundary measures; unnormalized Euclidean Poisson measures can have infinite mass.

## Proof of the complete compactification and all four kernels

The conformal bijection \(\Phi(s,t)=e^{s+it}\) sends \(S\) to the upper half-plane \(\mathbb H\) and \(a\) to \(i\). In real dimension two, its Green function is
\[
 G_{\mathbb H}(w,z)=\frac1{2\pi}\log\left|\frac{w-\bar z}{w-z}\right|
 =\frac1{4\pi}\log\left(1+\frac{4\operatorname{Im}w\operatorname{Im}z}{|w-z|^2}\right),
\quad G_S(x,y)=G_{\mathbb H}(\Phi(x),\Phi(y)).
\]
Section 4.5 defines \(K(y,x)=G_S(y,x)/b(y)\), where the cutoff \(b\) **equals** \(G_S(y,a)\) outside a fixed compact set (physical line 106). Thus for boundary approaches its \(K\) is the usual ratio \(G_S(x,y)/G_S(a,y)\); no cutoff normalization is silently changed.

For \(z\to\xi\in\mathbb R\), the Green ratio converges, locally uniformly in \(w\), to
\[
 K_\xi(w)=\frac{(1+\xi^2)\operatorname{Im}w}{|w-\xi|^2}.
\]
The limit holds even for arbitrary tangential approaches, because the logarithmic expression above is asymptotic to \((\operatorname{Im}w\operatorname{Im}z)/(\pi|w-\xi|^2)\), with an analogous denominator at \(i\). For \(|z|\to\infty\) through **arbitrary** upper-half-plane approaches,
\[
 G_{\mathbb H}(w,z)\sim \frac{\operatorname{Im}w\operatorname{Im}z}{\pi|w-z|^2},
 \qquad \frac{|i-z|^2}{|w-z|^2}\to1,
\]
uniformly on compact sets of \(w\); hence \(K_\infty(w)=\operatorname{Im}w\).
The point \(\xi=0\) corresponds to \(s\to-\infty\) (independent of \(t\)); the point \(\infty\) corresponds to \(s\to+\infty\). The two finite boundary components correspond to \(\xi=e^r\) and \(\xi=-e^r\). Substitution gives exactly the four formulas in the statement, including their values one at \(a\).

The closed upper half-plane with its single additional point \(\infty\) is compact. The normalized Green kernels extend continuously over it in the topology of locally uniform convergence. They separate boundary points (as proved below by the uniqueness of their representing atoms), and interior points are distinguished by their Green poles. Consequently the resulting continuous map to the §4.5 evaluation-kernel compactification is an injective map of compact Hausdorff spaces, and surjective by density of the interior. It is therefore a homeomorphism. This proves completeness of the boundary classification and makes no assumption of sequential compactness: the same asymptotics establish convergence of **nets**.

## Proof of measure uniqueness and minimality

The internally stated Theorem 3.2.6 supplies for \(H\ge0\) harmonic on \(\mathbb H\):
\[
 H(u+iv)=cv+\frac1\pi\int_{\mathbb R}
 \frac{v}{(u-\xi)^2+v^2}\,d\mu(\xi),\quad
 c\ge0,\quad\int_{\mathbb R}(1+\xi^2)^{-1}\,d\mu(\xi)<\infty.
\]
This pair is unique. Indeed, testing \(H(\cdot,v)\) against compactly supported continuous boundary functions as \(v\downarrow0\) recovers \(\mu\): locally this is the Poisson approximate identity, and the measure tails are \(O(v)\) by the displayed weight. Next,
\[
 \frac{H(iT)}T=c+\frac1\pi\int_{\mathbb R}\frac{d\mu(\xi)}{T^2+\xi^2}\longrightarrow c
\quad(T\to\infty)
\]
by dominated convergence. Thus both parts of the representation are determined.

Set \(d\sigma(\xi)=[\pi(1+\xi^2)]^{-1}d\mu(\xi)\), and assign \(\sigma(\{\infty\})=c\). Then \(\sigma\) is finite, \(H(w)=\int K_\xi(w)\,d\sigma(\xi)\), and \(\sigma(\mathbb R\cup\{\infty\})=H(i)\). The atom at \(0\) becomes \(c_-\); the atom at \(\infty\) becomes \(c_+\). Push the restrictions to \(\xi>0\) and \(\xi<0\) forward by \(r=\log|\xi|\). They become the finite measures \(\nu_0\) and \(\nu_\pi\), proving the stated unique formula for \(h=H\circ\Phi\).

Finally let \(0\le v\le K_\xi\) be any harmonic function, for any \(\xi\in\mathbb R\cup\{\infty\}\). By uniqueness the nonnegative normalized representing measures of \(v\) and \(K_\xi-v\) sum to \(\delta_\xi\). Each is therefore a scalar multiple of this same point mass; hence \(v=\lambda K_\xi\), \(0\le\lambda\le1\). All boundary kernels are extreme rays, so the entire Martin boundary is minimal.

## Audit significance and limitations

The **ambient one-point compactification** of the Euclidean plane sends \(s\to+\infty\) and \(s\to-\infty\) to the same point, but the strip Martin boundary **must distinguish** them: \(e^s\sin t\) and \(e^{-s}\sin t\) are nonproportional. This differs materially from the previously reviewed exterior-ball model `POME-MART-EXTERIOR-BALL-INFINITY-001`, which has just one unbounded end. Do not conflate these compactifications or import the exterior-ball result as proof.

**Verified:** the exact conformal Green computation, all boundary Green ratios (without nontangential restrictions), full strip Martin topology for arbitrary nets, normalized representation/uniqueness, and minimality. **Conditional:** general half-plane representation existence in 3.2.6, and the abstract Martin sweeping arguments in 4.5; no transitive general proof certification. **Affected dependents:** §§4.5.9/.12/.13 (explicit model consistency), §3.2.6 (conditional input). **Proposed correction:** no change to printed theorem; retain this independent model as an audit note. No formal verification, project build/tests/CI, source-body modification, main update, or website publication was performed.
