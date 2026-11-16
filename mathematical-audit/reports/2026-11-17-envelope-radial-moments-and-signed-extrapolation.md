# Radial jet moments and signed fourth-order cancellation for the envelope averaging kernel

**Date:** 2026-11-17. **Stable finding ID:** POME-ENV-RADIAL-JET-MOMENT-EXTRAPOLATION-001.

**Status:** low / **verified conditional deduction**, not a confirmed error, a proof gap, an independent verification of the printed joint Levi estimate, or a repair of the user-excluded regularization programme.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Integrated reading-edition file:** docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--smoothing-and-its-joint-complex-hessian/index.html, main blob 6937b0461ba82017332b58024c80edfc60baaf79. Section 16.17 permanent tag **B73B45463F24**; Lemma 16.17.1 source label **foundations-of-pluripotential-theory:C62EF841**, permanent tag **B48E71C5ACA1**; Equation (16.17.6) source **foundations-of-pluripotential-theory:67F76B17**, permanent tag **F605A97417F4**.

## Exact direct reading and exclusion boundary

Directly inspected the kernel statement and normalization at physical HTML lines **10–28, 45–55**, the fiber map and kernel at **102–125**, and the moment/adjoint distributional passage at **403–427**. Lines **63–100 and 333–397** were consulted only for jet and proof-context conventions; the many intermediate joint-Levi computations were **not** independently checked or certified. For Kähler normal coordinates, checked only the **closed** Kähler form hypothesis of Lemma 16.15.3 (permanent tag **23CF8D2A3054**) in docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--penalized-equations-and-metric-laplacian-envelopes/index.html, lines **76–90**.

The new derivations concern only the already printed radial **moments** and the signed behavior of a differential-kernel consistency test. The user-excluded Demailly approximation/regularization, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes are **deferred-by-user** and were not reopened.

## Result 1: explicit normalized moments

For the radial weight actually printed in §16.17,
\[
\chi(t)=C_n(1-t)^{-2}\exp[-1/(1-t)]\mathbf{1}_{t<1}
\]
on ordinary Euclidean Lebesgue space $\mathbb C^n$, define for integers $j\ge0$
\[
I_j:=\int_1^\infty e^{-v}(1-v^{-1})^j\,dv.
\]
Then **exactly**
\[
\boxed{ C_n=\frac{(n-1)!}{\pi^n I_{n-1}}, \qquad
a_\chi=\frac{I_n}{nI_{n-1}},\qquad
\int_{\mathbb C^n}|\zeta|^4\chi(|\zeta|^2)\,d\zeta
=\frac{I_{n+1}}{I_{n-1}}. }
\]
These are not guessed normalization constants. Real $2n$-dimensional polar integration gives
\[
\int_{\mathbb C^n}g(|\zeta|^2)\,d\zeta
=\frac{\pi^n}{(n-1)!}\int_0^\infty t^{n-1}g(t)\,dt.
\]
The substitution $v=(1-t)^{-1}$ sends
$t^{n-1+j}(1-t)^{-2}\exp[-1/(1-t)]\,dt$ to
$\exp(-v)(1-v^{-1})^{n-1+j}dv$. This yields $C_n$ and the second and fourth moments. The stated $a_\chi$ agrees with the printed definition
\[
a_\chi=\frac1n\int_{\mathbb C^n}|\zeta|^2\chi(|\zeta|^2)\,d\zeta.
\]

In dimension one, with $E_1(1)=\int_1^\infty e^{-v}v^{-1}\,dv$,
\[
a_\chi=1-eE_1(1)=0.4036526376768059\ldots
\]
and
\[
b_\chi:=\int_\mathbb C|\zeta|^4\chi(|\zeta|^2)\,d\zeta
=2-3eE_1(1)=0.2109579130304178\ldots.
\]
The decimal values were independently evaluated with high-precision quadrature. Exact formulas, not numerics, justify the claim.

## Result 2: fourth-order cancellation on smooth inputs

Keep the very **same** smooth fiber map $F(x,\zeta)$ of the existing printed section. Its coordinate two-jet is, for a closed Kähler background,
\[
F(x,\zeta)=x+\zeta-\tfrac12\Gamma_x(\zeta,\zeta)+O(|\zeta|^3),
\]
where the quadratic term is holomorphic in the fiber variable. Let
\[
\Psi_f(x,r)=\int_{T_xX}f(F(x,r\zeta))
  \chi(|\zeta|_h^2)\,d\zeta_h.
\]
For every fixed real $\lambda>1$ and $f\in C^4(X,\mathbb R)$ define, when $0<r<r_0/\lambda$,
\[
\mathcal R_{\lambda,r}f=
\frac{\lambda^2\Psi_f(\cdot,r)-\Psi_f(\cdot,\lambda r)}
{\lambda^2-1}.
\]
Then
\[
\boxed{\ \|\mathcal R_{\lambda,r}f-f\|_{L^\infty(X)}
  \le C_{f,\lambda,\chi,F}\,r^4.\ }
\]

**Proof.** The first moments of the radial kernel vanish; by the phase-rotation symmetry its purely holomorphic second moments vanish. The mixed second moment is
\[
\int_{\mathbb C^n}\zeta_i\bar\zeta_j\chi(|\zeta|^2)\,d\zeta
=a_\chi\delta_{ij}.
\]
Since the quadratic term in the displayed two-jet of $F$ is purely holomorphic, it contributes no second-order mean drift. Taylor expansion yields
\[
\Psi_f(x,r)=f(x)+a_\chi r^2D_hf(x)+O(r^3),
\qquad D_hf=\sum_{i,j}h^{i\bar j}f_{i\bar j},
\]
as in the printed Step 7, physical lines 405–413.

For the claimed sharper remainder use an additional **independent observation**: by the substitution $\zeta\mapsto-\zeta$,
\[
\Psi_f(x,-r)=\Psi_f(x,r)
\]
for real $r$ near zero. The smoothness of $F$, compact support of $\chi$, compactness of $X$ and the $C^4$ regularity of $f$ give a **uniform** fourth-order Taylor remainder. The first and third Taylor coefficients vanish by evenness. Thus
\[
\Psi_f(x,r)=f(x)+a_\chi r^2D_hf(x)+O_f(r^4)
\]
uniformly on $X$. Substitution at radii $r$ and $\lambda r$ cancels the entire $r^2D_hf$ term, yielding the box above. This uses no subsequence argument and no nonlinear regularization theorem.

The order $r^4$ cannot generally be improved. In a **local** flat complex coordinate let $F(z,\zeta)=z+\zeta$ near the origin and choose a smooth $f$ equal to $|z|^4$ in that coordinate neighborhood. For all sufficiently small radii,
\[
\Psi_f(0,r)=b_\chi r^4,\qquad
\mathcal R_{\lambda,r}f(0)-f(0)=-\lambda^2b_\chi r^4\neq0.
\]
This establishes exact sharpness in the stated local smooth test class. It does not depend on a globally defined polynomial on a compact complex manifold.

## Result 3: cancellation in distributions for arbitrary $L^1$ inputs

Equation **(16.17.6)** and its actual adjoint-kernel proof at physical HTML lines **415–427** give for arbitrary integrable $u$
\[
\frac{\Psi_u(\cdot,r)-u}{r^2}
  \longrightarrow a_\chi D_hu
  \quad\text{in }\mathcal D'(X).
\]
Therefore, for fixed $\lambda>1$,
\[
\boxed{\ \frac{\mathcal R_{\lambda,r}u-u}{r^2}
  \longrightarrow0\quad\text{in }\mathcal D'(X)
  \quad(r\downarrow0).\ }
\]
Indeed the difference equals
\[
\frac{\mathcal R_{\lambda,r}u-u}{r^2}
=\frac{\lambda^2(\Psi_u(r)-u)/r^2
-(\Psi_u(\lambda r)-u)/r^2}{\lambda^2-1},
\]
and the two distributional limits are respectively
$\lambda^2a_\chi D_hu$ and $\lambda^2a_\chi D_hu$.
No sequential compactness, exchange of two independent limits or uniform $L^1$ bound for the normalized difference is asserted.

The extrapolator $\mathcal R_{\lambda,r}$ is **signed**: the larger-radius averaging kernel has a negative coefficient. It generally does **not** preserve positivity, plurisubharmonicity, convexity, monotone envelope bounds or curvature lower bounds. No use of this operator for the excluded positivity-loss programme is proposed.

## Classification, dependencies and proposed action

**Status:** low / **verified conditional deduction**, not a new error in the integrated Lemma 16.17.1. The argument depends on the printed existing fiber map, the printed $L^1$ distributional generator (16.17.6), and elementary radial moment integration and even Taylor expansions. Only the **selected** Step 7 calculation was checked at proof level; the complete kernel construction and the joint complex Hessian bound (16.17.2) are **not transitively certified**. Later big-class envelopes were not audited here.

**Proposed correction:** no change to the printed theorem. Optionally add the exact normalization and signed cancellation as an expository consistency check *without* using the signed combination for positivity.

**Affected dependents:** only possible future use of the second-order generator and kernel moment normalization. This does not repair or verify any later curvature-loss or analytic approximation argument.

**Scope/coverage:** one newly first-directly-visited nonexcluded numbered section, §16.17, **only** in its kernel-moment/adjoint subsection. Zero newly complete section or chapter certificates. The current main table of contents is 25 chapters / 747 numbered sections. Historical excluded Demailly work remains **deferred-by-user, not resolved or certified**. No project build, test suite, GitHub Actions CI, source/registry/canonicalization edit or website publication was performed.
