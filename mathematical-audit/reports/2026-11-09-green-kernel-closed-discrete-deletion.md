# Minimal Green kernels do not see closed discrete interior deletions

**Date:** 2026-11-09. **Finding:** POME-GREEN-PUNCTURE-INVARIANCE-001.
**Status:** verified conditional deduction (low severity); *none of the printed theorems inspected is false*.

## Exact source and scope

Reviewed production <code>main</code> SHA: <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.

Integrated reading file:
<code>docs/sections/green-functions-and-potentials/index.html</code>,
blob <code>63c74d1c4a0958633b42903a0e3a4526f42b7588</code>,
section permanent tag <code>16EB8324A3E2</code>.

- Theorem 3.5.5, source label <code>classical-potential-theory:772DDE67</code>, permanent tag <code>F3C6870EA9A8</code>, physical lines 38–57 (minimal kernel, Greenian domains and nonexistence on the plane minus closed discrete sets).
- Theorem 3.5.6, source label <code>classical-potential-theory:093A6B54</code>, permanent tag <code>9E37095B7A8A</code>, physical lines 60–83 (domain monotonicity, joint continuity away from the diagonal).
- Theorem 3.5.12, source label <code>classical-potential-theory:1DF5E8AD</code>, permanent tag <code>9CF388990FE4</code>, physical lines 155–172 (boundary vanishing conditional on decay of a one-pole Green function).
- Context only: Theorem 3.5.8, source label <code>classical-potential-theory:1CC53DC8</code>, permanent tag <code>977ECF0867E0</code>, lines 90–115, for the potential interpretation.

This audit checks a **different** phenomenon from the earlier finding POME-PLANAR-GREEN-POLAR-BOUNDARY-SPIKE-001: the earlier finding concerns a *raw logarithmic polynomial envelope at an added polar boundary point*. Here the object is the **minimal classical Green kernel of a punctured domain**, its harmonic removability and its positive boundary trace.

## Proposition proved here

Let \(d\ge2\), let \(\Omega\subset\mathbb R^d\) be any Greenian open set (not necessarily bounded or connected), and let \(A\subset\Omega\) be relatively closed and discrete (every compact subset of \(\Omega\) meets \(A\) in finitely many points). Write \(\Omega'=\Omega\setminus A\). Then \(\Omega'\) is Greenian and, for every \(a,x\in\Omega'\),
\[
             G_{\Omega'}(a,x)=G_\Omega(a,x),
\]
including the diagonal convention \(G(a,a)=+\infty\).

Consequently, for \(D=\{z\in\mathbb C:|z|<1\}\) and \(D^*=D\setminus\{0\}\), every \(a,z\in D^*\) satisfy
\[
G_{D^*}(z,a)=\log\left|\frac{1-\bar a z}{z-a}\right|.
\]
For each fixed \(a\in D^*\),
\[
           \lim_{z\to0,\ z\in D^*}G_{D^*}(z,a)
                 =\log\frac1{|a|}>0.
\]
In particular the isolated boundary point \(0\in\partial D^*\) is not a Green-regular boundary point, although \(D^*\) is Greenian.

More concretely, take the **bounded** density \(f\equiv1\) on \(D^*\) (also in \(L^1(D^*)\)). Then
\[
   (G_{D^*}f)(z)=\int_{D^*}G_{D^*}(z,a)\,dA(a)
              =\frac{\pi}{2}(1-|z|^2),\qquad z\in D^*,
\]
and hence its boundary limit at the puncture is \(\pi/2\), not zero. This demonstrates that the one-pole Green-decay condition of printed Theorem 3.5.12 cannot simply be dropped, *even for a bounded domain and a bounded integrable density*. It does not contradict that theorem, because its stated decay hypothesis fails.

## Complete proof of harmonic removability used above

Let \(h\) be bounded harmonic on \(B_R(0)\setminus\{0\}\) in real dimension \(d\ge2\). Fix \(0<\rho<R\) and let \(H\) be the ordinary harmonic Dirichlet solution in \(B_\rho(0)\) with boundary data \(h|_{\partial B_\rho}\). Put \(k=h-H\). Then \(|k|\le M\) on the punctured closed ball for some finite \(M\), and \(k=0\) on \(|x|=\rho\).

On the annulus \(\varepsilon<|x|<\rho\) introduce the radial harmonic barrier
\[
 b_\varepsilon(x)=
 \begin{cases}
 \displaystyle\frac{\log(\rho/|x|)}{\log(\rho/\varepsilon)},&d=2,\\[5pt]
 \displaystyle\frac{|x|^{2-d}-\rho^{2-d}}
                     {\varepsilon^{2-d}-\rho^{2-d}},&d>2.
 \end{cases}
\]
It equals one at the inner sphere, zero at the outer sphere, and is nonnegative. The elementary maximum principle applied to \(M b_\varepsilon\pm k\) shows
\[
                |k(x)|\le M b_\varepsilon(x)
               \quad(\varepsilon<|x|<\rho).
\]
For every fixed \(0<|x|<\rho\), \(b_\varepsilon(x)\to0\) as \(\varepsilon\downarrow0\). Thus \(k=0\). The bounded harmonic function extends uniquely as \(H\) across the puncture. Only ball Dirichlet solvability, the explicit radial harmonic barriers and the elementary maximum principle are used here; there is **no approximation/regularization input**.

## Kernel invariance under locally finite deletion

For any pole \(a\in\Omega'\), restriction of the kernel \(G_\Omega(a,\cdot)\) to \(\Omega'\) is an admissible nonnegative Green competitor. Printed domain monotonicity therefore gives
\[
       0\le G_{\Omega'}(a,x)\le G_\Omega(a,x)
       \quad (x\in\Omega',\ x\ne a).
\]
In particular \(\Omega'\) is Greenian.

For each deleted point \(p\in A\), choose a closed ball about \(p\) contained in \(\Omega\) containing neither \(a\) nor another point of \(A\). The function \(G_{\Omega'}(a,\cdot)\) is nonnegative harmonic on the punctured ball, and is bounded above there by \(G_\Omega(a,\cdot)\), which is finite and harmonic near \(p\). The preceding removable-singularity argument extends it harmonically across \(p\). Since \(A\) is locally finite, all these extensions agree with the original kernel away from \(A\) and produce a harmonic extension \(\widetilde G\) on \(\Omega\setminus\{a\}\). It is nonnegative; at the pole \(a\) it has the same fundamental logarithmic/Newtonian singularity and a harmonic correction.

Hence \(\widetilde G\) belongs to the admissible class for the minimal kernel on \(\Omega\). Minimality yields
\[
             G_\Omega(a,\cdot)\le\widetilde G.
\]
Combined with the opposite restriction inequality, this proves equality on \(\Omega'\), and at the pole both sides are \(+\infty\). No sequential compactness, convergence of measures or limiting interchange is required.

## Explicit disc calculation and the boundary condition

For \(a,z\in D\), define
\[
 g(z,a)=\log|1-\bar a z|-\log|z-a|.
\]
Its correction to \(-\log|z-a|\) is harmonic in \(z\), since \(1-\bar a z\ne0\) on \(D\). The identity
\[
 |1-\bar a z|^2-|z-a|^2=(1-|a|^2)(1-|z|^2)>0
\]
shows \(g>0\) off the pole; \(g\to0\) on \(\partial D\). Any nonnegative competitor with the same pole has harmonic difference from \(g\), with nonnegative boundary lower limits, hence dominates \(g\) by the harmonic minimum principle. Therefore \(g=G_D\). Kernel invariance gives \(G_{D^*}=g|_{D^*\times D^*}\) and the stated strictly positive limit at the puncture.

To evaluate the bounded-density potential, write \(\rho=|z|\) and use the angular mean formulas
\[
\frac1{2\pi}\int_0^{2\pi}
       \log|1-\bar a z|\,d\arg a=0,\qquad
\frac1{2\pi}\int_0^{2\pi}
       \log|z-a|\,d\arg a=\log\max(\rho,|a|).
\]
They follow by the harmonic mean property after factoring out whichever modulus is larger (with continuity at equality). The Green singularity is integrable in two dimensions; Tonelli applies to the nonnegative kernel. Hence
\[
\begin{aligned}
\int_D g(z,a)\,dA(a)
 &= 2\pi\left[
    \int_0^\rho r\log(1/\rho)\,dr
    +\int_\rho^1 r\log(1/r)\,dr\right]\\
 &=\frac\pi2(1-\rho^2).
\end{aligned}
\]
Deleting the area-null point does not change the integral. The positive value at \(z\to0\) verifies failure of the **hypothesis** \(G_{\Omega'}(z,a_0)\to0\) for one pole in Theorem 3.5.12, not failure of its **conclusion under the hypothesis**.

## Classification and proposed addition

**Severity:** low. **Status:** verified conditional deduction, with all new component proofs given explicitly above, conditional only on the internally stated minimal-kernel existence/monotonicity and ball harmonic Dirichlet principle. **Printed statement error:** none. **Proof gap in those printed theorems established here:** none. **External dependency:** none introduced. **Duplication:** none identified; the earlier planar polar polynomial-envelope result addresses a different operator.

**Proposed patch, not applied:** add an independently tagged Example/Remark immediately after Theorem 3.5.12 (or beside Theorem 3.5.5) giving puncture invariance, the disc formula, and the bounded-density boundary trace. Retain the original one-pole boundary-decay hypothesis, source attribution, canonical entry versions and permanent tags. No source/registry/body or main-branch change is authorized by this record.

**Affected dependents:** any attempted boundary-vanishing corollary for a punctured or closed-discrete-deletion domain that infers boundary decay from Greenianity alone. No printed downstream theorem has been shown false or even identified as making that inference; downstream references remain unverified.

**Coverage:** direct selected proofs and clauses of §§3.5.5, 3.5.6, 3.5.12, with contextual use of §3.5.8; the entire §3.5 was previously sampled, so this is **not** a first numbered-section visit. The remaining arguments of §3.5 and their upstream chains are **not** certified. Project-level count remains 25 chapters, 747 numbered ToC sections, zero fully certified mathematical sections. The owner-excluded Demailly approximation/regularization and Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved.
