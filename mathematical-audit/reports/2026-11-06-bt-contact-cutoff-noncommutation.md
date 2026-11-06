# 2026-11-06 — contact-set restriction does not commute with a smooth Bedford–Taylor limit

**Finding:** \`POME-BT-CONTACT-CUTOFF-NONCOMMUTATION-001\`; **severity:** low; **status:** verified conditional deduction (the measures and the failure of restriction continuity are computed directly; no printed Pome proposition is false). **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch:** \`review/mathematical-audit\`. This is a *new contact-restriction limit test*, **not** a new claim that maxima can create hypersurface mass: that simpler phenomenon was already recorded as \`POME-HESS-MAX-CONTACT-SINGULAR-EXCESS-001\` in the distinct §8.12 Hessian audit.

## Exact integrated reading-edition anchors and dependencies

- \`docs/sections/bedford-taylor-products-and-local-capacity--bounded-complex-hessians-and-contact-sets/index.html\`, main blob \`e2697dc465a2b639120974188eaeb6c446ed8071\`, Lemma **7.13.1** source \`foundations-of-pluripotential-theory:B80A5A22\`, tag \`8736729F21D9\`, physical lines **13–42**; Lemma **7.13.2** source \`foundations-of-pluripotential-theory:0CFF4F56\`, tag \`D57C89462C1B\`, lines **48–82**; Proposition **7.13.3**, source \`foundations-of-pluripotential-theory:AF82FB9E\`, tag \`C006456D2AFC\`, lines **91–101**; Proposition **7.13.4**, source \`foundations-of-pluripotential-theory:D9CC767A\`, tag \`1466731348C1\`, lines **109–133**; the application to local potential shifts, line **138**.
- \`docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html\`, blob \`18bd2395f3b76941b2c677079c09eb6accc5a9cb\`, Proposition **7.2.6**, source \`foundations-of-pluripotential-theory:C5608495\`, tag \`2F39A3F97E8E\`, physical lines **125–154** (locally uniform continuous-potential convergence; crosscheck, not independent proof certification).
- §8.12 prior model: \`docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html\`, blob \`8750df56019c14e16704607ca20fa8b90f137fb0\`, Theorem **8.12.2** tag \`655B0BBF4F9C\`; older audit \`reports/2026-11-03-hessian-contact-hyperplane-maxima-excess.md\` is preserved, neither duplicated nor reclassified.

## Precise local model and measure identity

Fix an integer \(n\ge1\). On \(\mathbb C^n\) write \(z_j=x_j+iy_j\), use \(dd^c=(i/2\pi)\partial\bar\partial\), and put
\[
v_1=x_1,\qquad u_1=(x_1)_+=\max\{x_1,0\},\qquad
u_j=v_j=|z_j|^2\quad(2\le j\le n).
\]
All \(u_j\) are continuous, locally bounded psh; all \(v_j\) are smooth and pluriharmonic for \(j=1\) or strictly psh for \(j\ge2\). Their common contact set is the *closed* halfspace
\[
E=\bigcap_{j=1}^n\{u_j=v_j\}=\{x_1\ge0\}.
\]
It includes the real hypersurface \(H=\{x_1=0\}\). In one complex variable, for any real convex function \(g(x)\),
\[
dd^c g(x)=\frac{1}{4\pi}g''(x)\,dx\wedge dy
\]
as a distributional current. Since the second derivative of \(x_+\) is the unit Dirac mass at zero, while \(dd^c|z_j|^2=dx_j\wedge dy_j/\pi\), the Bedford–Taylor mixed product equals the locally finite positive measure
\[
\mu:=dd^c u_1\wedge\cdots\wedge dd^c u_n
 =\frac{1}{4\pi^n}\,\delta_0(dx_1)\,dy_1
    \prod_{j=2}^n dx_j\,dy_j. \tag{1}
\]
The empty product is \(1\) when \(n=1\). The identity can be obtained without multiplying singular distributions: approximate **only** the first factor by the smooth convex functions below and wedge with the fixed smooth transverse forms. Thus \(\mu\) is supported on \(H\subset E\), and \(\mathbf1_E\mu=\mu\ne0\). By contrast \(dd^c v_1=0\), so the smooth-obstacle mixed discriminant \(D((v_j)_{a\bar b})\) is identically zero.

This **does not refute Proposition 7.13.4**: its hypothesis specifically requires \(u_1\) to have locally bounded measurable complex Hessian, whereas \(u_1\) has a hypersurface Dirac derivative and is not \(W^{2,1}_{\mathrm{loc}}\). Mere local Lipschitz regularity of \(u_1\) is insufficient to extend the printed contact-set density identity.

## A stronger noncommutation check: exactly one half of the mass

For \(\varepsilon>0\) set
\[
u_{1,\varepsilon}(x_1)
   =\varepsilon\log(1+e^{x_1/\varepsilon}),\qquad
u_{j,\varepsilon}=u_j\quad(j\ge2).
\]
These potentials are smooth psh and
\(0\le u_{1,\varepsilon}-(x_1)_+\le\varepsilon\log2\) *uniformly on all of* \(\mathbb C^n\). Write
\[
k_\varepsilon(x)
 =u_{1,\varepsilon}''(x)
 =\frac{e^{-x/\varepsilon}}
        {\varepsilon(1+e^{-x/\varepsilon})^2}
 =\frac{1}{4\varepsilon}\operatorname{sech}^2(x/(2\varepsilon)).
\]
The kernels are even, nonnegative, have total integral \(1\), and
\(\int_0^\infty k_\varepsilon(x)\,dx=1/2\). They form an approximate identity at zero. Hence
\[
\mu_\varepsilon
 :=dd^c u_{1,\varepsilon}\wedge\cdots\wedge dd^c u_{n,\varepsilon}
 =\frac{k_\varepsilon(x_1)}{4\pi^n}\,dV_{2n}
 \ \rightharpoonup\ \mu, \tag{2}
\]
while restriction to the **fixed contact set of the limit** obeys
\[
\boxed{\quad
\mathbf1_E\mu_\varepsilon\rightharpoonup\frac12\mu
  \ne\mathbf1_E\mu=\mu.\quad} \tag{3}
\]
Indeed, for every compactly supported continuous \(\varphi\), the integrals over \(x_1\ge0\) converge by the half-sided approximate-identity identity to precisely one half of its trace on \(H\). The test \(\varphi\) may vary in all other \(2n-1\) coordinates; dominated convergence in those coordinates completes the proof. The Hessian \(L^\infty\) norms of the first approximants diverge as \(k_\varepsilon(0)=1/(4\varepsilon)\), so they are **not uniformly** bounded.

Formula (3) pinpoints a failure that cannot be repaired merely by locally uniform convergence of continuous psh potentials or weak convergence of their Bedford–Taylor products: multiplication by \(\mathbf1_E\) is not continuous when the limiting measure charges \(\partial E\). For \(\varepsilon>0\), the *approximating* contact set \(\{u_{1,\varepsilon}=v_1\}\) is empty, so applying Proposition 7.13.4 with that set yields zero and is not being contradicted. The half-mass is genuinely a **fixed-limit-set restriction** phenomenon, not a counterexample to Bedford–Taylor weak continuity.

## Classification, correction direction and exact coverage

- **Classification:** low / **verified conditional deduction**. Equations (1)–(3) are direct distributional/approximate-identity calculations. The general Bedford–Taylor construction and Proposition 7.2.6 remain conditional for the full collection; their particular conclusion in (2) is independently proved by the explicit densities.
- **Suggested nonproduction clarification:** an optional warning adjacent to Proposition 7.13.4 should state that the bounded-complex-Hessian assumption is essential for replacing the restricted measure by an a.e. Hessian determinant. Even when smooth psh approximants converge uniformly, restriction to the contact set of the *limit* need not commute with weak convergence if that set's boundary carries limiting mass. Do not weaken the proposition's hypotheses or modify its source or tag.
- **Potential dependents:** applications in envelope/contact-measure sections, including §16.10 and §16.13, must justify restriction to fixed contact sets separately; unqualified use of weak product convergence is insufficient. This is a warning about a possible reasoning step, **not** a claim that a specific downstream theorem is false.
- **Actual inspection:** Lemmas 7.13.1/2 and Propositions 7.13.3/4 read at the listed physical lines; new exact smooth-cutoff calculation and normalized mixed-product check for §7.13.4; Proposition 7.2.6 and the prior §8.12 model consulted narrowly. No full §7.13, §7.2, §8.12 or envelope chapter certification.
- **Out of scope:** Demailly approximation/regularization and its dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programme remain **deferred-by-user**, not resolved. No CI, build, test suite, formal verification or publication was performed.
