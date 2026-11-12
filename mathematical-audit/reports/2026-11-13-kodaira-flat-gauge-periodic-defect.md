# Parametric Kodaira LCK flat gauges: exact Gauduchon criterion and unbounded divergence

**Finding:** `POME-KODAIRA-FLAT-GAUDUCHON-FREQUENCY-001`
**Classification:** low / **verified conditional deduction**. The printed Example 23.2.53 and Theorem 23.2.47 are **not** contradicted. The parametric construction and divergence below are checked directly; the final optional antisymmetric-Hessian norm comparison invokes printed Theorem 23.2.47 conditionally, without certifying its entire upstream chain.

## Provenance and scope

- Production `main` commit: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading-edition file: `docs/sections/locally-conformally-kahler-geometry/index.html`; blob `6ebf8e604b45d3eb748037af506145273ca3875d`.
- Example 23.2.53: source `non-kahler-pluripotential-theory:F3D1120B`, permanent tag `E37387C4675B`; statement physical lines 906–908, constructed nilmanifold and complex structure 913–937, invariant metric 939–951, flat conformal gauge 953–965, particular example 967–979, conformal uniqueness 981–982.
- Theorem 23.2.47: source `non-kahler-pluripotential-theory:C87CCD5B`, permanent tag `C4981F6B1F78`; statement lines 785–795, Bianchi/Bochner and rigidity argument 799–889. Its general tensor identity is a conditional internal dependency only.
- Lee convention: Definition 23.2.2, source `non-kahler-pluripotential-theory:FE5EDE37`, permanent tag `48F6C713AFE3`, lines 22–28.
- Not reviewed: all non-Kodaira LCK cases, the entire proof of 23.2.47, or any Demailly approximation/regularization/Bergman/L2/OT/multiscale/positivity-loss programme.

## New parametric statement

Use exactly the Kodaira nilmanifold, coframe, and complex structure of Example 23.2.53:
[
de^1=de^2=de^4=0,quad de^3=-e^1wedge e^2,quad
phi^1=e^1+ie^2,quad phi^2=e^3+ie^4.
]
Fix **any** real smooth 1-periodic function (f(x)) with
[
C(x)=1-f''(x)>0.
]
Set
[
lambda_1=-e^4+f'e^1,quad
eta_1=e^3+f'e^2,quad
omega_1=lambda_1wedgeeta_1+C e^1wedge e^2,quad H=C^{-1/2},quad omega=Homega_1.
]
Then:

1. (omega_1) is a strictly LCK Vaisman metric with Lee class ([-e^4]), and (omega) is strictly LCK, Chern–Ricci flat, with the **same** Lee class and
   [
   rac{omega^2}{2}=e^{1234}.
   ]
   Every Chern–Ricci-flat metric conformal to (omega_1) is a constant multiple of (omega), even when an arbitrary (not necessarily (x)-dependent) conformal factor is allowed.
2. With (q=d_g^*lambda=-operatorname{div}_g(lambda^sharp)) for (g) associated to (omega), one has the exact global identity
   [
   q(x)=-H''(x)=-rac{d^2}{dx^2}(1-f''(x))^{-1/2}.
   ]
   Consequently the unique Chern–Ricci-flat conformal gauge is Gauduchon (equivalently Vaisman by the **conditional** original Theorem 23.2.47) **if and only if** (f) is constant. Every nonconstant (f) in this open positivity family gives a Chern–Ricci-flat but non-Gauduchon gauge, strengthening the single printed trigonometric example.
3. More quantitatively, fix (0<a<1) and for each integer (kge1) take
   [
   f_k(x)=rac{a}{(2pi k)^2}cos(2pi kx),quad C_k=1+acos(2pi kx),quad
   H_a(s)=(1+acos s)^{-1/2}.
   ]
   The metrics (omega_k=H_a(2pi kx)omega_{1,k}) are uniformly positive and uniformly bounded in the global coframe (e^1,ldots,e^4), all have the same volume form (e^{1234}) and Lee class ([-e^4]), but their Gauduchon defects satisfy
   [
   |d^*_{g_k}lambda_k|_{L^2(dmathrm{vol}_{g_k})}^2
   =(2pi k)^4 J(a),qquad
   J(a)=rac1{2pi}int_0^{2pi}|H_a''(s)|^2,ds>0.
   ]
   Thus their (L^2) divergence norm grows exactly like (k^2), despite a common smooth volume, Lee class, and uniformly equivalent (C^0) Hermitian metrics. **Only conditionally on** the integrated Theorem 23.2.47, this also yields
   (|S^-_k|_{L^2}^2=	frac12(2pi k)^4J(a)).

## Direct proof

The quotient of the real Heisenberg group times a circle by its integer lattice is compact. Its coframe is globally defined (Example 23.2.53, lines 913–937); the same lines prove integrability via (dphi^2=-(i/2)phi^1wedgearphi^1), and the nowhere-vanishing closed ((2,0))-form (Sigma=phi^1wedgephi^2) trivializes the canonical bundle. All functions below descend since they are 1-periodic in (x).

First, (dlambda_1=0), (deta_1=(-1+f'')e^1wedge e^2=-C e^1wedge e^2), and (d(C e^1wedge e^2)=0). Hence (domega_1=lambda_1wedgeomega_1). In the displayed coframe,
[
g_1=lambda_1^2+eta_1^2+C((e^1)^2+(e^2)^2),quad
omega_1^2/2=C e^{1234}.
]
The dual of (lambda_1) is (-E_4), a Killing field since all metric coefficients are independent of (t). A closed Killing 1-form is parallel, proving the Vaisman claim. The (t)-circle has Lee period (-1).

The (Sigma)-volume is a fixed positive multiple of (e^{1234}), so in the stated (dd^c) convention the normalized Chern–Ricci curvature of any conformal metric (homega_1) is
[
mathrm{Ric}^{mathrm{Ch}}(homega_1)=-dd^clog(Ch^2).
]
For (h=H=C^{-1/2}) it vanishes. Conversely a Chern-flat (homega_1) has globally pluriharmonic (log(Ch^2)). Every real pluriharmonic function on compact connected (X) is constant; thus (h=cH) for (c>0). Notice this argument does not assume that (h) depends only on (x).

For (h=H), the Lee form is
[
lambda=-e^4+(f'+H'/H)e^1.
]
The (g_1)-dual of (e^1) is ((E_1+f'E_4)/C), and (C=H^{-2}); hence its (g=H g_1) dual is
[
A=lambda^sharp
=H'E_1+(f'H'-H^{-1})E_4.
]
Because (dmathrm{vol}_g=H^2C e^{1234}=e^{1234}), while the invariant frame fields (E_1,E_4) have zero divergence, (operatorname{div}_g A=H''). This proves (q=-H'') without invoking the rigidity theorem. Since (H) is 1-periodic, (qequiv0) iff (H) is constant. Then (C=1-f'') is constant; its average is (1), so (f''=0), and periodicity forces (f) to be constant. The converse is immediate. Proposition 23.2.7 supplies the already printed equivalence (q=0) iff Gauduchon.

Finally, (C_kin[1-a,1+a]), (|f_k'|_inftyle a/(2pi k)), and (H_k) stays between fixed positive constants. The displayed sum-of-squares formula for (g_{1,k}) gives uniform positive upper and lower metric bounds in the invariant coframe. The divergence formula gives
[
q_k(x)=-(2pi k)^2 H_a''(2pi kx).
]
The quotient fundamental domain has unit coordinate lengths in (x,y,z,t), and (e^{1234}=dx,dy,dz,dt). Integration over its (x)-coordinate yields the exact (J(a)) formula. As
[
H_a''(0)=rac a2(1+a)^{-3/2}>0,
]
one has (J(a)>0). No limiting interchange, compactness argument, or numerical approximation is needed.

## Classification, correction and impact

**Status:** verified conditional deduction; **severity:** low. There is **no confirmed false source statement** and no purported replacement of Example 23.2.53 or Theorem 23.2.47. Suggested *optional* documentation addition: a brief parametric corollary after Example 23.2.53 saying that the flat gauge is Gauduchon precisely for constant periodic (f), and noting that the fixed-volume/Lee-class family has unbounded divergence even with uniform metric equivalence. Do **not** modify the reading edition or its stable tags as part of this audit.

**Affected context:** Example 23.2.53 and the (q=0) characterization in Proposition 23.2.7; the (S^-)-norm consequence is explicitly conditional on Theorem 23.2.47. General Chern–Ricci rigidity, PDE existence, other Kodaira surfaces, and any user-deferred regularization chain are not certified here. This is *new selected proof-level work* in previously partly inspected §23.2, not full-section or chapter verification.