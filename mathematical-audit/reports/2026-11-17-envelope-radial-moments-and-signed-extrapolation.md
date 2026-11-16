# Radial jet moments and signed fourth-order cancellation for the envelope averaging kernel

**Date:** 2026-11-17. **Stable finding ID:** `POME-ENV-RADIAL-JET-MOMENT-EXTRAPOLATION-001`.
**Status:** **verified conditional deduction** (low severity). This is *not* a confirmed error, proof gap, a proof of the printed joint Levi estimate, or a repair of the excluded regularization programme.
**Main baseline:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated text:** `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--smoothing-and-its-joint-complex-hessian/index.html`, blob `6937b0461ba82017332b58024c80edfc60baaf79`.
**Section:** 16.17, permanent tag `B73B45463F24`; Lemma 16.17.1, original source `foundations-of-pluripotential-theory:C62EF841`, permanent tag `B48E71C5ACA1`. Equation (16.17.6), source `foundations-of-pluripotential-theory:67F76B17`, permanent tag `F605A97417F4`.

## Exact selected reading coverage and scope

Directly checked the setup and normalization at physical HTML lines 10–28 and 45–55, the radial map and kernel at lines 102–125, and the second-order jet/moment/adjoint-kernel calculation at lines 403–427. Read lines 63–100 for the jet conventions and lines 333–397 solely as context. The separate Step 2–6 joint-Hessian, curvature-loss and atlas estimates were **not certified** and are not part of this deduction. Lemma 16.15.3, permanent tag `23CF8D2A3054`, at `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--penalized-equations-and-metric-laplacian-envelopes/index.html` lines 76–90, was checked only for the closed Kähler background required for the normal coordinates, without certifying its downstream nonlinear PDE.

The work below concerns a radial **moment identity of an already constructed kernel**, independent of the positivity-loss programme. No Demailly approximation, Bergman, Ohsawa–Takegoshi, $L^2$ or multiscale positivity-loss argument was attempted. All such historical work remains **deferred-by-user**, not resolved or certified.

## Result 1: explicit normalizing and second/fourth moments

Use the actual printed choice
[
chi(t)=C_n(1-t)^{-2}exp[-1/(1-t)]mathbf 1_{t<1}
]
and ordinary Lebesgue measure on (mathbb C^n), normalized by (intchi(|zeta|^2),dzeta=1). Set
[
I_j=int_1^infty e^{-v}(1-v^{-1})^j,dvqquad(jge0).
]
Then **exactly**
[
 C_n=rac{(n-1)!}{pi^n I_{n-1}},qquad
 a_chi=rac{I_n}{n I_{n-1}},qquad
 int_{mathbb C^n}|zeta|^4chi(|zeta|^2),dzeta=rac{I_{n+1}}{I_{n-1}}.
]
Indeed polar integration in real dimension (2n) gives
[
int_{mathbb C^n}g(|zeta|^2),dzeta
 =rac{pi^n}{(n-1)!}int_0^infty t^{n-1}g(t),dt.
]
The substitution (v=(1-t)^{-1}) sends
(t^{n-1+j}(1-t)^{-2}e^{-1/(1-t)}dt)
to (e^{-v}(1-v^{-1})^{n-1+j}dv), proving all three identities without asymptotic approximation.

For (n=1), letting (E_1(1)=int_1^infty e^{-v}dv/v),
[
a_chi=1-eE_1(1)=0.4036526376768059ldots,quad
b_chi:=int_{mathbb C}|zeta|^4chi(|zeta|^2)dzeta
=2-3eE_1(1)=0.2109579130304178ldots.
]
The numerical values were independently checked by quadrature; they are supplementary to the exact identities.

## Result 2: a fourth-order signed cancellation for smooth test functions

Keep the **same** smooth fiber map (F(x,zeta)) constructed in the printed section; in a holomorphic coordinate chart the two-jet at (x) is
[
F(x,zeta)=x+zeta-	frac12Gamma_x(zeta,zeta)+O(|zeta|^3).
]
The quadratic term is holomorphic in (zeta). Define
[
Psi_f(x,r)=int_{T_xX} f(F(x,rzeta))chi(|zeta|_h^2)dzeta_h.
]
For (fin C^4(X,mathbb R)), fixed (lambda>1) and (0<r<r_0/lambda), let
[
mathcal R_{lambda,r}f
=rac{lambda^2Psi_f(cdot,r)-Psi_f(cdot,lambda r)}{lambda^2-1}.
]
Then
[
oxed{|mathcal R_{lambda,r}f-f|_{C^0(X)}
 le C_{f,lambda,chi,F},r^4 .}
]
The coefficient of (r^2) in (Psi_f) is precisely
(a_chi D_h f), with (D_h f=sum h^{iar j}f_{iar j}), because the angular first and holomorphic second moments vanish and the mixed moment is
(intzeta_iarzeta_jchi,dzeta=a_chidelta_{ij}).
The weight is invariant under (zetamapsto-zeta). Therefore (Psi_f(x,-r)=Psi_f(x,r)). The smooth fiber map and compactness of (X) give a uniform fourth-order Taylor remainder, and odd coefficients vanish:
[
Psi_f(x,r)=f(x)+a_chi r^2 D_hf(x)+O_f(r^4).
]
Substituting (r) and (lambda r) cancels the entire (r^2D_h f) term, giving the claimed estimate.

The exponent four is sharp already in one flat complex coordinate. Take (F(z,zeta)=z+zeta) near zero and (f(z)=|z|^4) on a neighborhood of zero (with any smooth cutoff outside). At (z=0),
[
Psi_f(0,r)=b_chi r^4,qquad
(mathcal R_{lambda,r}f)(0)-f(0)
=-lambda^2 b_chi r^4
e0.
]
Thus no uniform (o(r^4)) statement for all (C^4) tests follows from these hypotheses.

## Result 3: arbitrary (L^1) inputs, distributional second-order cancellation

Equation (16.17.6), with its **actual** Step 7 adjoint proof at HTML lines 415–427, establishes for any (uin L^1(X))
[
(Psi_u(cdot,r)-u)/r^2 longrightarrowa_chi D_hu quad	ext{in }mathcal D'(X).
]
Consequently, without assuming any convergent sequence or subsequence,
[
oxed{(mathcal R_{lambda,r}u-u)/r^2
  longrightarrow 0quad	ext{in }mathcal D'(X)
  	ext{ as }rdownarrow0.}
]
Indeed
[
mathcal R_{lambda,r}u-u
=rac{lambda^2(Psi_u(r)-u)-(Psi_u(lambda r)-u)}
       {lambda^2-1},
]
and the distributional second-order terms (a_chilambda^2r^2D_hu) cancel. This does **not** imply an (L^1), sup-norm or monotone estimate for arbitrary (u).

The extrapolated operator is **signed** because the coefficient of
(Psi_u(lambda r)) is negative. It generally does not preserve positivity, plurisubharmonicity or admissible curvature lower bounds, and **must not** be substituted for the original positive averaging kernel in any envelope or approximation argument. No such substitution is proposed.

## Adjudication, dependencies, affected material and correction

- **Printed result:** no false theorem or proof defect identified in the *selected* moment/adjoint passage. Equation (16.17.6) retains its original hypotheses and normalization.
- **Status:** low / **verified conditional deduction**, conditional on the published smooth, unit-mass fiber kernel and equation (16.17.6); not a verification of the long Steps 1–6, particularly the joint positivity/curvature estimates.
- **Affected dependents:** at most future uses of the radial moment and weak distributional generator. This calculation supplies an independent normalization check for the coefficient (a_chi); it does not strengthen the positivity claim (16.17.2) or the later big-class envelope theorems.
- **Proposed correction:** none to the printed theorem. Optional expository note only: record the exact radial moment constants and the signed extrapolation as a limitation/consistency check; do not alter tags or canonicalization.
- **Unresolved:** full integrated proof of the joint Levi estimate and the downstream big-class envelope regularity not certified; any independent external inputs stay logged. The separate user-excluded Demailly regularization/Bergman/$L^2$/OT/multiscale/positivity-loss programme remains **deferred-by-user**.

**Coverage increment:** one numbered section (§16.17) newly directly visited in a carefully delimited moment/adjoint subsector; no whole-section or chapter certificate. Actual current main ToC count remains 25 chapters and 747 numbered sections. No project build, test suite, GitHub Actions, publication or production edits performed.
