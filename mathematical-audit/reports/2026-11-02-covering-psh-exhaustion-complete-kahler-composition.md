# Complete Kähler metrics obtained from covering-space strictly psh exhaustions

**Finding:** POME-COVER-PSH-COMPLETE-KAHLER-COMPOSITION-001  
**Classification:** low / verified conditional deduction (**not** a false theorem, not an applied repair).  
**Production main inspected:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-11-02).  
**Proof scope:** a new direct proof of the composition/completeness lemma, conditional on the already printed existence of the strict psh exhaustion in Theorem 9.28.5. Selected checks of Proposition 9.28.3's sheet-uniform positive-order derivative cancellation and Theorem 9.28.5's properness argument; no certification of their complete dependency chains. This is not Demailly approximation or regularization work.

## Exact integrated anchors and provenance

- <code>docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html</code>, blob <code>ef92b5dc5bb4c143345621ea60ca52f3ca7d1872</code>. Proposition 9.28.3: source <code>demailly-complex-geometry:09F8EE91</code>, permanent <code>7808CCD76C79</code>, physical lines 48–50 and 57–98. Theorem 9.28.5: source <code>demailly-complex-geometry:F653208F</code>, permanent <code>73159A8CF2BB</code>, lines 104 and 110–140; in particular lines 134–140 establish strict Levi positivity and properness of the constructed exhaustion.
- Comparison only: <code>docs/sections/separation-strict-exhaustions-and-coverings--complete-kahler-metrics-on-regular-open-sets/index.html</code>, blob <code>3faaef942f4822127e09c63a463d654d346696c2</code>; Theorem 9.31.1, source <code>demailly-complex-geometry:232F4B65</code>, permanent <code>214C6B3DF885</code>, physical lines 7–20. Its direction and regular-open domain hypotheses are different, so no duplicate/canonicalization claim is made.
- Structural orientation only: <code>docs/sections/separation-strict-exhaustions-and-coverings/index.html</code>, blob <code>89f1c30a6df3c3df624fd05943a5cc64460824b8</code>, §9.25. This is a navigation heading, not an additional theorem reviewed.

## A self-contained metric-completeness lemma

Let Y be a complex manifold and let F:Y→R be a **smooth strictly plurisubharmonic exhaustion**, i.e. all closed sublevels are compact. In the Pome convention
\[
dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
Let φ be smooth on an interval containing F(Y), with φ'>0 and φ''≥0. Suppose that for a fixed t0 below the range of F,
\[
\int_{t_0}^{+\infty}\sqrt{\phi''(t)}\,dt=+\infty.
\]
Then
\[
\omega_\phi=dd^c(\phi\circ F)
 =\phi'(F)\,dd^c F+\frac{i}{2\pi}\phi''(F)\,\partial F\wedge\bar\partial F
\]
is a **complete Kähler metric** on Y.

**Proof.** Strict positivity follows from φ'>0 and positivity of dd^cF. Since ωφ is globally dd^c-exact it is closed. Let gφ(v,v)=ωφ(v,Jv) be the associated real Riemannian metric. For every real tangent vector v the rank-one term gives
\[
g_\phi(v,v)\geq \frac{\phi''(F)}{4\pi}
\bigl((dF(v))^2+(dF(Jv))^2\bigr)
\geq\frac{\phi''(F)}{4\pi}(dF(v))^2.
\]
Define G(t)=∫_{t0}^t√φ''(s) ds. Thus
\[
|d(G\circ F)(v)|\leq 2\sqrt{\pi}\,|v|_{g_\phi}.
\]
Consequently G∘F is globally 2√π-Lipschitz in the path metric. The assumption G(t)→∞ makes G∘F proper (F is proper, and all relevant sublevel sets are closed). Every gφ-Cauchy sequence therefore remains in a compact F-sublevel: the values of G∘F are bounded by the Lipschitz estimate. Compactness provides a convergent subsequence; the metric topology equals the manifold topology, so Cauchyness forces the full sequence to converge. This proves completeness. No Hopf–Rinow converse, a priori bounded geometry, or global zero-order bound on covering sheets is used. □

In particular, choosing **φ(t)=e^t** gives a complete Kähler metric
\[
\boxed{\omega=dd^c(e^F)=e^F\bigl(dd^cF+\tfrac{i}{2\pi}\partial F\wedge\bar\partial F\bigr).}
\]
By the strict exhaustion constructed in Theorem 9.28.5, **every connected unramified holomorphic covering of a connected strongly pseudoconvex manifold therefore admits a complete Kähler metric**. The derivation is independent of the analytic L²/OT/Bergman programme explicitly deferred by the user.

## Why simply taking dd^cF is not sufficient

The strict-psh-exhaustion assumption does **not** itself make dd^cF complete. On Y=C take
\[
F(z)=\log(1+|z|^2).
\]
It is smooth, strictly subharmonic and proper, while
\[
dd^c F=\frac{i}{2\pi}\frac{dz\wedge d\bar z}{(1+|z|^2)^2}.
\]
The real radial ray has finite metric length, proportional to
\(\int_0^\infty (1+r^2)^{-1}dr=\pi/2\).
Thus dd^cF is incomplete. By contrast
\[
dd^c(e^F)=dd^c(1+|z|^2)=\frac{i}{2\pi}dz\wedge d\bar z
\]
is the complete flat metric. This explicitly separates proper potential, strict Levi positivity and Riemannian completeness.

## A checked proof step in the integrated covering construction

In Proposition 9.28.3, the mollified sheet functions have sheet-uniform bounds on **positive** derivatives only (lines 59–74). The delicate terms in D^νδ where all derivatives hit a partition coefficient are
\[
\sum_\alpha D^\nu\theta_\alpha\,\delta_\alpha
=\sum_\alpha D^\nu\theta_\alpha\,(\delta_\alpha-\delta_0),
\qquad |\nu|\ge1,
\]
using ∑D^νθα=0. This is a pointwise algebraic cancellation and **does not differentiate** the Lipschitz function δ0. The remaining summands are controlled by the mollified positive-order estimates; the lower Hermitian Hessian bound on the base follows by locally finite patching (lines 84–98). The step checked here is correct; no complete proof-chain certification follows. Infinite-fiber zero-order limitations were separately recorded earlier and are **not** asserted as a new finding here.

## Assessment and proposed editorial addition

- **Severity/status:** low / verified conditional deduction; the printed Proposition 9.28.3, Theorem 9.28.5 and Theorem 9.31.1 are **not** refuted. No complete theorem proof or excluded approximation proof is claimed.
- **Proposed correction:** no correction needed. Optionally insert the general completeness lemma or the explicit exponential-composition corollary after Theorem 9.28.5, with the one-dimensional F=log(1+|z|²) example to guard against an invalid shortcut from strict psh exhaustion to completeness of dd^cF.
- **Dependents:** possible downstream use when a complete Kähler background is needed on an unramified cover; no existing dependent proposition was certified or edited. Theorem 9.31.1 is a hypothesis/conclusion comparison, not a proof input.
- **Coverage:** new complete proof of the displayed composition criterion; newly selected detailed examination of §9.28.3 derivative cancellations and §9.28.5 final Levi/properness step; §9.31.1 statement comparison; §9.25 orientation only. **No numbered section completely mathematically certified.**
- **Deferred-by-user:** Demailly approximation/regularization, dedicated Bergman, weighted L², OT, multiscale-atlas and positivity-loss proof completion remain deferred rather than solved.
- **Verification boundary:** pen-and-paper formulas checked against the printed reading edition; no source or tag modification, build, test suite, CI, formalization, or website publication.
