# Parametric Kodaira LCK flat gauges: exact Gauduchon criterion and unbounded divergence

**Finding:** \`POME-KODAIRA-FLAT-GAUDUCHON-FREQUENCY-001\`
**Classification:** low / **verified conditional deduction**. Printed Example 23.2.53 and Theorem 23.2.47 are **not** contradicted. The parametric construction, flat-gauge uniqueness, and divergence are checked directly. The optional antisymmetric-Hessian norm comparison invokes printed Theorem 23.2.47 *conditionally*, without certifying its entire proof.

## Provenance, precise scope and anchors

- Production \`main\` commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated reading edition: \`docs/sections/locally-conformally-kahler-geometry/index.html\`, blob \`6ebf8e604b45d3eb748037af506145273ca3875d\`.
- Example 23.2.53: source \`non-kahler-pluripotential-theory:F3D1120B\`, permanent tag \`E37387C4675B\`. Statement physical lines 906–908; quotient and complex structure 913–937; invariant metric 939–951; flat conformal gauge 953–965; printed numerical instance 967–979; conformal uniqueness 981–982.
- Theorem 23.2.47: source \`non-kahler-pluripotential-theory:C87CCD5B\`, permanent tag \`C4981F6B1F78\`; statement lines 785–795 and integrated Bianchi/Bochner argument 799–889.
- Definition 23.2.2 (Lee convention): source \`non-kahler-pluripotential-theory:FE5EDE37\`, permanent tag \`48F6C713AFE3\`, lines 22–28.
- Only selected new proof steps of §23.2.53 are certified here. All other LCK cases, full Theorem 23.2.47 proof, and every user-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programme are out of scope.

## Exact new statement

Work on the compact primary Kodaira surface with the invariant coframe and complex structure of Example 23.2.53:
\[
de^1=de^2=de^4=0,\qquad de^3=-e^1\wedge e^2,\qquad
\phi^1=e^1+ie^2,\quad \phi^2=e^3+ie^4.
\]
Fix **any** real smooth 1-periodic \(f(x)\) with
\[
C(x)=1-f''(x)>0.
\]
Define
\[
\lambda_1=-e^4+f'e^1,\quad
\eta_1=e^3+f'e^2,\quad
\omega_1=\lambda_1\wedge\eta_1+C e^1\wedge e^2,\quad
H=C^{-1/2},\quad \omega=H\omega_1.
\]

**(A) Entire periodic family.** The metric \(\omega_1\) is strictly LCK and Vaisman, and \(\omega\) is strictly LCK and Chern–Ricci flat, with
\[
[\lambda_\omega]=[-e^4],\qquad \omega^2/2=e^{1234}.
\]
Every Chern–Ricci-flat Hermitian metric conformal to \(\omega_1\) is a constant positive multiple of \(\omega\), even when the conformal factor is allowed to depend on every point of the surface.

**(B) Exact rigidity criterion.** If \(g\) is the Riemannian metric associated with \(\omega\), its Lee divergence is
\[
q=d_g^*\lambda_\omega=-\operatorname{div}_g(\lambda_\omega^\sharp)=-H''(x)
=-\frac{d^2}{dx^2}(1-f''(x))^{-1/2}.
\]
Consequently the unique flat conformal gauge is **Gauduchon iff \(f\) is constant**. In the constant case it is Vaisman. In the nonconstant case it is not Gauduchon, hence not Vaisman; this last implication also follows directly because every Vaisman metric is Gauduchon. Thus every nonconstant \(f\) in this open positivity family strengthens the printed single-function example.

**(C) Unbounded defect at fixed volume, Lee class, and uniformly equivalent metrics.** Fix \(0<a<1\), and for \(k\in\mathbb N_{>0}\) take
\[
f_k(x)=\frac{a}{(2\pi k)^2}\cos(2\pi kx),\quad
C_k(x)=1+a\cos(2\pi kx),\quad H_a(s)=(1+a\cos s)^{-1/2}.
\]
The metrics \(\omega_k=H_a(2\pi kx)\omega_{1,k}\) are all uniformly equivalent in \(C^0\) with respect to the same globally defined positive reference coframe metric. They share the *identical* volume form \(e^{1234}\) and Lee cohomology class \([-e^4]\), while
\[
\|d^*_{g_k}\lambda_k\|_{L^2(d\mathrm{vol}_{g_k})}^2
=(2\pi k)^4J(a),\qquad
J(a)=\frac1{2\pi}\int_0^{2\pi}|H_a''(s)|^2\,ds>0.
\]
In particular \(\|q_k\|_{L^2}\) grows exactly at order \(k^2\). **Only conditional on** the separately printed Theorem 23.2.47 does one additionally have
\[
\|S^-_k\|_{L^2}^2=\tfrac12(2\pi k)^4J(a).
\]

## Direct proof (no regularization or PDE existence)

The group quotient \(\Gamma\backslash(\mathrm{Heis}_3\times\mathbb R)\) and invariant coframe are fixed in Example 23.2.53, lines 913–937. In particular, \(e^1=dx,e^2=dy,e^3=dz-x\,dy,e^4=dt\); all periodic functions of \(x\) descend. Integrability follows directly from \(d\phi^1=0\) and \(d\phi^2=-(i/2)\phi^1\wedge\overline{\phi^1}\). The nowhere-vanishing closed \((2,0)\)-form \(\Sigma=\phi^1\wedge\phi^2\) trivializes the canonical bundle.

Compute
\[
d\lambda_1=0,\quad d\eta_1=(f''-1)e^1\wedge e^2=-C e^1\wedge e^2,\quad d(Ce^1\wedge e^2)=0.
\]
Therefore \(d\omega_1=\lambda_1\wedge\omega_1\). The associated Riemannian metric and volume are
\[
g_1=\lambda_1^{\otimes2}+\eta_1^{\otimes2}
+C\bigl((e^1)^{\otimes2}+(e^2)^{\otimes2}\bigr),\qquad
\omega_1^2/2=C e^{1234}.
\]
The \(g_1\)-dual of \(\lambda_1\) is \(-E_4\). Since \(E_4=\partial_t\) is Killing and \(d\lambda_1=0\), the symmetric tensor \(\nabla^{g_1}\lambda_1\) is also antisymmetric and hence zero. The nonzero \(t\)-circle Lee period \(-1\) shows strictness.

The holomorphic trivialization \(\Sigma\) has constant nonzero volume density relative to \(e^{1234}\). The Chern–Ricci form in the project's \(dd^c\) convention is therefore
\[
\mathrm{Ric}^{\mathrm{Ch}}(h\omega_1)=-dd^c\log(Ch^2)
\]
for every globally defined smooth positive \(h\), not merely radial \(h\). Taking \(h=H=C^{-1/2}\) gives zero. Conversely flatness forces the real globally defined function \(\log(Ch^2)\) to be pluriharmonic. On connected compact \(X\) it is constant by the maximum principle. Thus \(h=cH\) for a positive constant \(c\). Moreover \(d\mathrm{vol}_g=\omega^2/2=H^2C e^{1234}=e^{1234}\).

The Lee form of \(g=H g_1\) is
\[
\lambda_\omega=\lambda_1+d\log H=-e^4+(f'+H'/H)e^1.
\]
The \(g_1\)-dual of \(e^1\) equals \((E_1+f'E_4)/C\), where \(C=H^{-2}\). Hence
\[
A=\lambda_\omega^\sharp
=H'E_1+(f'H'-H^{-1})E_4.
\]
The globally defined frame fields \(E_1=\partial_x\) and \(E_4=\partial_t\) have zero divergence against the volume \(e^{1234}=dx\,dy\,dz\,dt\), so \(\operatorname{div}_g A=H''\), proving \(q=-H''\).

Since \(H\) is periodic, \(H''\equiv0\) implies \(H\) is constant. Therefore \(C=1-f''\) is constant. Its mean is \(1\) because \(f'\) is periodic, so \(f''=0\); periodicity of \(f\) forces \(f\) constant. The converse is immediate. The equivalence between co-closed Lee form and the Gauduchon condition is the already printed Proposition 23.2.7; no use of the Chern–Ricci Bianchi/Bochner theorem is required to establish the criterion.

For the Fourier family, \(C_k\in[1-a,1+a]\), \(|f_k'|\le a/(2\pi k)\), and \(H_k\) stays between positive constants independent of \(k\). The sum-of-squares expression for \(g_{1,k}\) gives uniform upper and lower metric bounds in the fixed invariant coframe. It also gives \(d\mathrm{vol}_{g_k}=e^{1234}\) and \([\lambda_k]=[-e^4]\). Finally,
\[
q_k(x)=-(2\pi k)^2 H_a''(2\pi kx).
\]
The integer-lattice quotient has an \(x,y,z,t\) fundamental set with unit coordinate ranges and \(e^{1234}=dx\,dy\,dz\,dt\). By periodicity,
\[
\int_X q_k^2\,d\mathrm{vol}_{g_k}
=(2\pi k)^4\int_0^1|H_a''(2\pi kx)|^2\,dx
=(2\pi k)^4J(a).
\]
Here \(H_a''(0)=\tfrac a2(1+a)^{-3/2}>0\), so \(J(a)>0\). This is an **exact** identity for all integers \(k\), not an asymptotic estimate or a numerical fit.

## Status, optional correction and dependents

**Severity low; status verified conditional deduction.** There is no false printed theorem, no proven gap in Example 23.2.53, and no new external analytic prerequisite. Optional documentation improvement: after Example 23.2.53 record the general \(f\)-criterion and high-frequency fixed-volume family; this is a proposed addition only, **not a source patch**. The existing example and permanent tags remain unchanged.

**Affected context:** Proposition 23.2.7, Example 23.2.53, and the purely conditional \(S^-\)-comparison in Theorem 23.2.47. The entire theorem's analytic proof is not certified. The review is selected **new** work in an already partly inspected §23.2; it adds **zero** first-visited numbered sections and **zero** complete section certifications (current actual ToC: 25 chapters / 747 numbered sections). Prior confirmed errors, proof gaps, external dependencies and user-deferred items retain their prior classifications. No production/main/registry/tag/CI/build/publication change.