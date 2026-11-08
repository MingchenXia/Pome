# Exact weak-star homogenization obstruction for the normalization scalar (2026-11-09)

**Stable finding ID:** \`POME-SCALAR-WEAKSTAR-HOMOGENIZATION-001\`. **Severity:** low. **Status:** verified conditional deduction (a sharpness counterexample to an *unprinted* weakening, **not** a false theorem or repair).

**Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Integrated anchors:** \`docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html\`, blob \`fff86de757578ed2be369ba752123f62f3d31044\`, Theorem 11.33.5, source label \`non-kahler-pluripotential-theory:D502EBBF\`, permanent tag \`5E3583383688\`, physical lines 88–121 (hypotheses 88–91, proof 94–121). Also \`docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html\`, blob \`0710d0732ae7ef81de3d3d62206a0f9c6b5d321f\`, Eq. 11.37.2, source label \`non-kahler-pluripotential-theory:65FF799F\`, permanent tag \`803909FECEC0\`, physical lines 50–61, especially 56–59.

## Explicit example and exact result

Take the unit-area flat elliptic curve
\[
E=\mathbb C/(\mathbb Z+i\mathbb Z),\quad z=x+iy,\quad
\omega=\frac{i}{2}dz\wedge d\bar z=dx\wedge dy,\quad \int_E\omega=1.
\]
Use the Kähler background \(\theta=\omega\), volume \(dV=\omega\) and reference model potential \(\varphi=0\). These obey the positive-volume and smaller-background-envelope hypotheses of §11.32: the zero potential is an admissible model reference and remains admissible under \(\varepsilon\omega\), \(0<\varepsilon<1\).

Fix \(a>0\) and, for \(j=1,2,\ldots\), set
\[
F_j(x+iy)=a\cos(2\pi jx),\qquad
J(a)=\int_0^1 e^{a\cos(2\pi t)}\,dt>1,\qquad
\rho_j=\frac{e^{F_j}}{J(a)}.
\]
The strict inequality is Jensen's inequality, since the nonconstant cosine has average zero.

All \(F_j\) are **smooth and uniformly bounded**, with \(F_j\rightharpoonup^*0\) in \(L^\infty(E,dV)\). Nonetheless,
\[
B_0(F_j)=-\log J(a)<0=B_0(0)\qquad\text{for every }j.
\]
Furthermore their normalized smooth Monge–Ampère solutions converge **uniformly** to the normalized solution at zero with rate \(O(j^{-2})\), while the corresponding Monge–Ampère measures and **unique supporting probabilities** converge weakly to \(dV\), but do not converge in total variation.

## Direct Poisson proof (no general MA-existence dependency)

For the convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), any real 1-periodic function \(h(x)\) satisfies
\[
dd^ch=\frac{h''(x)}{4\pi}\omega.
\]
The smooth 1-periodic function \(q(x)=e^{a\cos(2\pi x)}/J(a)-1\) has mean zero. Hence there exists a smooth 1-periodic real \(v\), unique modulo an additive constant, solving
\[
v''(x)=4\pi q(x).
\]
Define the global smooth functions
\[
u_j(x+iy)=j^{-2}\bigl(v(jx)-\max_{\mathbb R/\mathbb Z}v\bigr).
\]
Then \(\sup_Eu_j=0\) and
\[
\omega+dd^cu_j=\bigl(1+q(jx)\bigr)\omega
=\rho_j\omega>0.
\]
Thus \(u_j\) are genuine smooth \(\omega\)-psh solutions of
\[
\operatorname{MA}_\omega(u_j)=c_j e^{F_j}dV,
\qquad c_j=J(a)^{-1}.
\]
Integrating over \(E\) and using Stokes proves the constant is *forced*; for \(F=0\), the normalized solution is \(u=0\), with \(c_0=1\). Accordingly \(B_0(F_j)=\log c_j=-\log J(a)\), independently crosschecking the closed-background formula (11.37.2). Moreover
\[
\|u_j\|_{C^0(E)}
=\frac{\max v-\min v}{j^2}\longrightarrow0.
\]

For each \(g\in L^1(E,dV)\), integration against \(a\cos(2\pi jx)\) tends to zero by the Riemann–Lebesgue lemma (first integrate \(g\) over \(y\)). Thus \(F_j\rightharpoonup^*0\) in \(L^\infty\); but
\[
\int_E|F_j|dV=\frac{2a}{\pi}
\]
does not tend to zero. The periodic densities \(\rho_j\) have mean one. For each continuous \(g\), trigonometric approximation, or partition of the \(x\)-circle into \(j\) cells, gives
\[
\int_E g\rho_j\,dV\longrightarrow\int_Eg\,dV.
\]
Eq. 11.37.2 identifies the unique supporting probability at \(F_j\) as \(\rho_jdV\), so the supporting probabilities and the MA measures converge weakly. But their \(L^1\) discrepancy is **constant and strictly positive**:
\[
\int_E|\rho_j-1|\,dV
=\int_0^1\left|\frac{e^{a\cos(2\pi t)}}{J(a)}-1\right|dt>0.
\]
If total variation is defined using the half-\(L^1\) convention, divide the displayed value by two. Strict positivity follows because \(\rho_j\) is nonconstant.

## Mathematical assessment and affected dependents

**Printed Theorem 11.33.5 remains correct.** It requires **strong \(L^1(dV)\)** convergence of uniformly bounded logarithmic densities, which this example violates. The nonlinear distinction is \(F_j\rightharpoonup^*0\) but \(e^{F_j}\rightharpoonup^*J(a)\ne1\). In particular, not even *uniform potential convergence plus weak measure convergence* repairs the missing normalization information.

Eq. **11.37.2** is checked by an independent smooth Poisson solution; no singular MA solvability, Demailly regularization, Bergman estimates or Ohsawa–Takegoshi input is invoked. This is distinct from earlier KL/Fenchel and strong-\(L^1\)/TV estimates, which do not address weak-star oscillatory data with a fixed scalar gap.

**Proposed correction (not applied):** insert an optional sharpness example after Theorem 11.33.5; preserve the theorem, original source/provenance, historical attribution, and permanent tags. Any *hypothetical* weak-star-only extension of §§11.34–11.36 needs extra control of the integrals of the exponential densities; no printed dependent theorem is declared false or recertified.

**Precise scope:** newly checked selected statements in previously partially audited §§11.33 and 11.37, contextual mention of §§11.34–11.36 only; no whole-section certification. Older classifications remain unchanged. The owner-excluded regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss programme stays **deferred-by-user**, not resolved. No main/source/registry/canonicalization/tag edit, CI, build, formalization or publication.
