# An explicit indefinite Monge–Ampère mass Hessian at a balanced non-Kähler metric

**Finding ID:** `POME-HERM-BALANCED-MASS-SADDLE-001` — **low / verified conditional deduction** (new smooth model, not a false theorem or an upstream proof certification).  
**Date:** 2026-11-04. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Pinned integrated reading text and prior-coverage separation

- `docs/sections/torsion-and-the-variation-of-mass/index.html`, main blob `9abec9685e33a1b40f9c0765381408eb52b325d3`: Theorem **11.1.5** and its mass polynomial, source `non-kahler-pluripotential-theory:D4902E5B`, permanent `2B3316345A4A`, physical lines **68–94**; Chiose Theorem **11.1.7**, source `non-kahler-pluripotential-theory:5CD99CBA`, permanent `FB90FC741F25`, physical lines **99–157**; Proposition **11.1.8** and first-variation Equation **11.1.9**, source `non-kahler-pluripotential-theory:940AB63B`, permanent `5C29873687ED`, physical lines **161–174**.
- `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, main blob `519e50338be6560f6b2856fddce212738f5109bc`: existing Example **11.23.5**, source `non-kahler-pluripotential-theory:324594DA`, permanent `28F39F2B7C2C`, physical lines **76–99**. Its printed perturbation establishes *failure of Gauduchon persistence*. The previously recorded `POME-GEO-UNIVERSAL-TORSION-KAHLER-001` checks its balanced/non-Kähler torsion; `POME-HERM-GAUD-PERSIST-TWO-TORSION-001` checks persistence criteria. **Neither is re-entered as a new finding.** The new computation below is the *exact indefinite Hessian of the total mass*, and shows why the original one-parameter perturbation does not itself exhibit a mass change.

## Statement and exact formulas

Let \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(X=E^3\), with \(z_j=x_j+i y_j\) and \(\eta_j=(i/2)dz_j\wedge d\bar z_j=dx_j\wedge dy_j\). Let
\[
b(x_1)=e^{\cos(2\pi x_1)},\qquad c(x_1)=b(x_1)^{-1}=e^{-\cos(2\pi x_1)},\qquad
\omega=\eta_1+b\eta_2+c\eta_3.
\]
Then \(\omega>0\), \(d\omega^2=0\) (indeed \(bc=1\)), but \(d\omega\ne0\).
For any real smooth periodic \(f=f(x_1)\), let \(g(x_2)=\cos(2\pi x_2)\) and \(u_\epsilon=\epsilon f(x_1)g(x_2)\). For sufficiently small \(|\epsilon|\), \(u_\epsilon\in\mathcal H_\omega\), and the following formula is **exact**, not an asymptotic:
\[
\boxed{\int_X(\omega+dd^c u_\epsilon)^3
=6-\frac{3\epsilon^2}{8}\int_0^1f(x)^2c''(x)\,dx.}\tag{A}
\]
In particular, \(D M_\omega(0)=0\) in **every** smooth real direction (balanced implies Gauduchon), but the quadratic form \(D^2M_\omega(0)\) has **both signs**:

1. \(f_+(x)=c(x)\) gives \(\int c''c^2=-2\int c(c')^2<0\), whence
\[
M_\omega(\epsilon f_+g)=6+\frac{3\epsilon^2}{4}\int_0^1c(c')^2\,dx>6\quad(\epsilon\ne0\text{ small}).
\]
2. For \(0<\delta<1\), put \(f_-(x)=1+\delta\cos(2\pi x)\). Integration by parts and \(c'=2\pi c\sin(2\pi x)\) yield
\[
\int_0^1 f_-^2c''\,dx
=8\pi^2\delta\int_0^1 f_-(x)c(x)\sin^2(2\pi x)\,dx>0,
\]
so \(M_\omega(\epsilon f_-g)<6\) for every sufficiently small nonzero \(\epsilon\).

Thus \(u=0\) is a **genuine smooth saddle** of the Monge–Ampère mass on the positive-potential domain, although its first variation vanishes in all directions. For the *specific* printed perturbation in Example 11.23.5 one takes \(f\equiv1\), so \(\int c''=0\) and (A) gives \(M_\omega(\epsilon g)\equiv6\), **even though the perturbed metric is no longer Gauduchon**. Constancy along one ray does not imply universal mass invariance or vanishing of all first variations at every point of that ray.

## Independent proof (including the off-diagonal Hessian term)

With Pome's convention \(dd^c=(i/2\pi)\partial\bar\partial\), a smooth function of the real \(x_1,x_2\) coordinates has Hermitian \(dd^c\) matrix \((\partial^2_{x_ix_j}u)/(4\pi)\) relative to the \(\eta_j\) basis. Therefore the Hermitian matrix of \(\omega+dd^c u_\epsilon\) is
\[
\begin{pmatrix}
1+\epsilon f''g/(4\pi)&\epsilon f'g'/(4\pi)&0\\
\epsilon f'g'/(4\pi)&b+\epsilon fg''/(4\pi)&0\\
0&0&c
\end{pmatrix}.
\]
The determinant, multiplying \(\eta_1\eta_2\eta_3\) and accounting for \(3!=6\), is
\[
6c\left[b+\frac{\epsilon}{4\pi}(bf''g+fg'')
+\frac{\epsilon^2}{16\pi^2}(ff''gg''-(f')^2(g')^2)\right].
\]
The \(\epsilon\)-term integrates to zero because \(\int_0^1g=\int_0^1g''=0\). Also
\[
\int_0^1gg''=-2\pi^2,\qquad
\int_0^1(g')^2=2\pi^2,\qquad bc=1.
\]
Integration in \(x_2\), followed by periodic integration by parts in \(x_1\), gives
\[
M_\omega(u_\epsilon)
=6-\frac{3\epsilon^2}{4}\int_0^1c(ff''+(f')^2)
=6+\frac{3\epsilon^2}{4}\int_0^1c'ff'
=6-\frac{3\epsilon^2}{8}\int_0^1c''f^2,
\]
proving (A) and the two signs. The vanishing first variation independently follows from \(dd^c(\omega^2)=0\) and Equation 11.1.9. Positivity for both signs of \(\epsilon\) follows from compactness and the strict positivity of \(\omega\), without any singular approximation or external lemma.

## Classification, dependents and proposed change

**Severity:** low. **Status:** verified conditional deduction (an exact additional smooth computation). The statements and proofs of Theorem 11.1.5, Chiose Theorem 11.1.7, Proposition 11.1.8, and Example 11.23.5 are **not refuted**. No false theorem or new unfilled proof step is claimed. The Chiose equivalence is respected because \(dd^c\omega\ne0\). The bounded-potential part of Theorem 11.1.7 cites regularization and is expressly **deferred-by-user**; it is not used or reviewed here.

**Suggested optional reading-edition addition:** after Example 11.23.5 (or following the dimension-three discussion of §11.1.10) include the exact saddle formula (A) and emphasize that failure of Gauduchon persistence is not the same as mass variation along the *particular* perturbation used to exhibit it. Preserve both old permanent tags and Chiose attribution. **Affected dependents:** interpretation of §11.1.5–9, smooth mass-versus-torsion tests in §11.23.4–5, and any assertion of local convexity or concavity of Hermitian total mass.

**Actual coverage:** new explicit determinant/polarization/first-variation comparison for the already sampled §§11.1.5–9 and 11.23.5; no complete theorem-dependency or whole-section certification. All previous errors/gaps/external dependencies/repairs remain classified as before. No project builds, test suites, CI, website publication, source/body/registry edits, or formal verification.
