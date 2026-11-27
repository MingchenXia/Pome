# Albanese dual polarization: the exact denominator

Date: 2026-11-27. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## POME-ALBANESE-DUAL-POLARIZATION-EXPONENT-001

Severity: low. Status: verified conditional deduction (not a false printed theorem). The original projectivity proof works with its stated square multiplier; the following identifies the least positive integer multiplier for the particular transported Hermitian form.

Target: `docs/sections/compact-curves-periods-and-complex-tori--projectivity-and-integral-periods/index.html`, blob `f9b42d19c3b216883c147bc8b47f7af4b22bf026`, Theorem 10.80.4, source label `354EFEF2`, permanent tag `183B8F4BFE57`, physical lines 99–150, especially 113–147. Inputs: the integral trace lemma 10.80.3 (tag `5A4C95A96C6B`, lines 65–94), torus criterion 10.80.2 (tag `826013CCAFEC`, lines 37–60), degree-one evaluation Theorem 10.79.2 (tag `F90F5D542AFB`, lines 27–54), Picard and Albanese lattices 10.79.4–5 (tags `C1FB3F157E12`, `99C9CC069FA0`, lines 59–111 in the section file named below).

### Proof

Keep exactly the connected projective manifold, normalized integral Kähler form omega, Hodge spaces W and V, full lattices Lambda and Gamma, linear-first positive Hermitian form h and complex-linear isomorphism B of 10.80.4. The zero-dimensional torus case is vacuous; take exponent 1 for the trivial group.

Write Q(gamma,delta) = integral_X gamma wedge delta wedge omega^(n-1) for real harmonic degree-one forms. By lines 125–128, E=Im h obeys E(pr^(0,1)gamma,pr^(0,1)delta)=-Q(gamma,delta). The real projection is an isomorphism, so the same formula holds for all real classes, not merely integral ones. Let Lambda^# = {w in W : E(w,Lambda) is contained in Z}. E is nondegenerate (h is positive); the integer trace lemma gives Lambda subset Lambda^#.

For w=pr^(0,1)gamma and lambda=pr^(0,1)delta in Lambda, put v=delta^(1,0). The precise evaluation identity is the following. The real functional associated to a in V* in 10.79.5 is evaluated on [Re u] as Re a(u). For the real class delta, take u=2 delta^(1,0), so Re u=delta. By type and complex conjugation,
Re B(w)(2 delta^(1,0))=2 Re integral_X gamma^(0,1) wedge delta^(1,0) wedge omega^(n-1)=Q(gamma,delta).
Hence the evaluation functional associated to B(w) on the integral lattice is exactly -E(w,lambda). The factor two is essential. Theorem 10.79.2 identifies Gamma with all integer-valued functionals on that lattice, not only a subgroup. Thus B(Lambda^#)=Gamma.

Under B, the finite isogeny J(X) -> A(X) has kernel K=Lambda^#/Lambda, with no additional appeal to integral Poincare duality. Its order is the absolute determinant of the integral alternating matrix of E in a basis of Lambda. Indeed the E-pairing identifies Lambda^# with the integer dual of Lambda, and Lambda maps to it by the integral matrix of E. The determinant/index identity follows from fundamental parallelotope volumes. Moreover E modulo Z descends to a perfect alternating pairing on K: both arguments lie in Lambda^#, and changing either by Lambda changes the value by an integer. Its radical is zero because (Lambda^#)^#=Lambda. For the latter equality, choose a real basis of Lambda and write E(x,y)=x^t M y with nonsingular alternating M; the dual lattice is M^(-t) Z^r, and dualizing again yields Z^r (a harmless global minus sign). The quotient is finite since M is nonsingular and integral.

Set h_A(a,b)=h(B^(-1)a,B^(-1)b), exactly as in line 147. For a positive integer k,
k Im h_A is integral on Gamma x Gamma
iff k E(Lambda^#,Lambda^#) is integral
iff k Lambda^# is contained in (Lambda^#)^#=Lambda.
Consequently the least positive integer k is the exponent e of K, the least positive integer annihilating every element of K. In particular e Im h_A is integral, and e h_A is a positive Hermitian form. This replaces the square of an annihilator m in the printed proof by m itself; taking the least annihilator gives the optimal integer multiplier for this specific transported form, not necessarily the least polarization of A among all possible forms.

The distinction is real already in dimension one: for an elliptic curve with primitive integral symplectic form E0 on its Picard lattice, replacing E0 by d E0 makes Lambda^#=(1/d)Lambda, K=(Z/dZ)^2 and the least integer multiplier d. Such a scaled pairing in higher dimension occurs, for example, on a product of an elliptic curve and P^1 with a product very ample polarization of degree at least three on the curve and degree d>=1 on P^1; on its degree-one cohomology the trace pairing is multiplied by d, since all degree-one forms come from the curve and the curve-factor component of omega wedges to zero. The example is illustrative; the lattice proof does not require a product computation.

Proposed correction: optionally replace lines 145–147 by the exact dual-lattice argument and use e instead of m^2. Keep the original conclusion, historical attribution, and permanent tag. No downstream theorem is invalidated. In particular the curve lattice equality of 10.79.11/13 is compatible with e=1. Hodge decomposition, Serre duality, Kodaira projectivity, and the integral-period comparisons are used as already stated internal inputs, not independently certified here.

## Coverage

- Whole direct conditional §10.79, `docs/sections/compact-curves-periods-and-complex-tori--integral-periods-picard-tori-and-albanese-maps/index.html`, blob `81ec78509629e15d648cfd3b686fe4d691437330`, physical mathematical lines 7–252. Checked finite graph generation, torsion-free evaluation, monodromy sign, real dual of Hodge projection, open-path current type and sign, divisor logarithm derivative via Cauchy, integer collars and the torsion argument, genus-zero and projective-space line bundle arguments. The cited cohomological comparisons and analytic prerequisites remain conditional.
- Whole direct conditional §10.80, same path prefix, `projectivity-and-integral-periods/index.html` and blob above, lines 7–150. Checked rational positive approximation, Hermitian sign, incidence dimension for smooth hyperplane sections, cup comparison sign, positivity and integrality of h, evaluation map and isogeny. No new printed error found.
- Whole direct conditional §10.81, same path prefix, `complex-lattice-quotients/index.html`, blob `bf4f45ec25bac897ca8248be581a52ef82f4e62f`, lines 8–15. Checked discreteness, Hausdorff quotient charts, compact fundamental parallelotope and constant Kähler metric.
- Current main docs/index.html has 747 section links; existing SECTION_MATRIX has 747 distinct section IDs, none missing. These three were legacy-unreconciled; no historical first-visit claim. Three new whole direct reads; zero complete upstream certificates, zero new confirmed errors or demonstrated proof gaps; one conditional deduction.
- Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user, not resolved. No excluded proof work, production edits, build, test, CI or publication performed.
