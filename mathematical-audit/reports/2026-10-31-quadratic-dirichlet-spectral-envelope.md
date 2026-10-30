# Quadratic boundary data: exact spectral Dirichlet envelope and strict concavity

**Date:** 2026-10-31. **Finding:** `POME-BT-QUADRATIC-DIRICHLET-EIGENVALUE-001`. **Severity:** low. **Status:** **verified conditional deduction** (new exactly solvable family; **not** a false theorem, complete proof repair, or certification of the parent theorem). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit-only branch:** `review/mathematical-audit`.

## Integrated reading-edition anchors and scoped dependencies

- **Exact main file:** `docs/sections/bedford-taylor-products-and-local-capacity--the-homogeneous-dirichlet-problem-and-balayage/index.html`; blob `928f3d3e36f2d03a42623b91487ecec7d189e6c7`; section 7.7 permanent tag `22EC1FF0BE9D`.
- **Theorem 7.7.4 (homogeneous ball Dirichlet existence/uniqueness):** source `foundations-of-pluripotential-theory:FEE18534`, permanent tag `9181532558D7`; statement **physical lines 104–108**, construction/uniqueness **113–135**.
- **Corollary 7.7.5 (ball balayage):** source `foundations-of-pluripotential-theory:A118D214`, permanent tag `2E8B947536C1`; statement **140**, construction **145–154**.
- **Definition 7.7.6 of maximality:** source `foundations-of-pluripotential-theory:4A1DBBE1`, tag `FD8547B922C9`, **line 160**.
- **Theorem 7.7.7 (maximality iff zero Bedford–Taylor mass for locally bounded psh):** source `foundations-of-pluripotential-theory:5C75D8E4`, tag `BCFDDA1FCB7A`; statement **165**, proof **170–174**.
- **Lemma 7.7.2 determinant normalization:** source `foundations-of-pluripotential-theory:2473754C`, tag `0E5A3E632224`, physical lines **58–69**, proof **75–99**.
- **Comparison input:** Theorem 7.3.11, source `foundations-of-pluripotential-theory:A7DD3972`, tag `D0AF90DDC7A5`, `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html`, blob `96a9e39e85fab5774ebdac0c6d9d006338a4e42c`, statement at physical line **304**. Used only as an existing internal uniqueness/comparison input; its full proof chain is not certified here.
- **Normalization:** `dd^c=i/(2*pi) partial barpartial`, as in the integrated reading edition; `(dd^cH)^n=(n!/pi^n)det(H_{j bar k})dV_{2n}` for smooth potentials (Lemma 7.7.2).

This inspection specifically adds a fresh check of Theorem 7.7.7's maximality/comparison logic and an exact quadratic family. Earlier examination of §7.7.1–5 and the previously registered boundary sup-norm isometry `POME-BT-PERRON-ISOMETRY-001` are **not** counted again.

## Exact spectral formula (all Hermitian quadratic boundary data)

Let (B={zinmathbb C^n:|z|<1}), (nge 1), (A=A^*) an arbitrary Hermitian (n	imes n) matrix (not assumed positive), (P(z)) a holomorphic polynomial of degree at most two and (cinmathbb R). Consider the real boundary data
[
 arphi_A(z)=z^*Az+2operatorname{Re}P(z)+cquad (|z|=1).
]
Set (lambda(A)=minoperatorname{Spec}(A)). Then the unique Perron solution of the **homogeneous** Bedford–Taylor Dirichlet problem in Theorem 7.7.4 is
[
 oxed{H_A(z)=z^*Az+2operatorname{Re}P(z)+c
          +lambda(A)(1-|z|^2).}
]

**Complete direct model computation.** The added term vanishes on the sphere. Since the holomorphic real part is pluriharmonic, the Hermitian complex Hessian of (H_A) is the **constant** matrix (A-lambda(A)I), which is positive semidefinite and has at least one zero eigenvalue. Therefore (H_A) is smooth psh on (B), and its top exterior product vanishes *identically*:
[
 (dd^cH_A)^n={n!over pi^n}det(A-lambda(A)I),dV_{2n}=0.
]
It has exactly the required boundary values. The **uniqueness** part of integrated Theorem 7.7.4 (equivalently its cited BT comparison input, 7.3.11) identifies it as the Perron envelope. In dimension one the entire Hermitian Hessian vanishes, so this reduces to the harmonic extension. No limiting, smoothing, non-pluripolar or regularization argument is used in this model computation.

## Exact nonlinear interpolation defect, and its equality condition

Fix the same (P,c) in the two boundary functions and let (A,B) be Hermitian. For (0le tle1), the homogeneous solution operator satisfies the **exact** formula
[
egin{aligned}
 H_{(1-t)A+tB}(z)-((1-t)H_A(z)+tH_B(z))
 &=Delta_t(A,B)(1-|z|^2),\
 Delta_t(A,B)&=lambda((1-t)A+tB)
                 -(1-t)lambda(A)-tlambda(B)ge0.
end{aligned}
]
The inequality follows without spectral continuity: for every unit vector (v),
(langle Av,vanglegelambda(A)) and
(langle Bv,vanglegelambda(B)); minimize their weighted sum.
For (0<t<1), **equality holds if and only if** the minimal-eigenvalue eigenspaces of (A) and (B) have a nonzero common vector. To prove necessity, take a unit minimizer of the convex-combination Rayleigh quotient. Equality of the weighted lower bound forces equality in *both* nonnegative summands. Sufficiency is immediate from a common minimum eigenvector.

More generally, for arbitrary continuous boundary data (arphi,psi) on the sphere, the Perron characterization shows
(H_{(1-t)arphi+tpsi}ge (1-t)H_arphi+tH_psi):
the right side is psh and has the interpolated boundary values, hence is a valid competitor. This **concavity** is distinct from the previously recorded **isometric sup-norm stability**.

**Strictness, explicitly in complex dimension two.** Take (P=c=0), (A=operatorname{diag}(0,1)), (B=operatorname{diag}(1,0)), and (t=1/2). The separate envelopes are (|z_2|^2) and (|z_1|^2). Their averaged boundary data are identically (1/2) on (partial B), and their envelope is the constant (1/2). Thus the gap is exactly
[
 H_{(A+B)/2}(z)-	frac12(H_A(z)+H_B(z))
 =	frac12(1-|z|^2)>0 quad(zin B).
]
The homogeneous Perron solution is **not an affine function of boundary data** for (nge2); this is not a failure of uniqueness, comparison, or concavity.

## Explicit whole-space balayage for quadratic psh obstacles

If (Age0), the global quadratic (u(z)=z^*Az+2operatorname{Re}P(z)+c) is psh on any neighborhood (Omegasupsetoverline B). The exact ball replacement of Corollary 7.7.5 is
[
 widehat u(z)=
 egin{cases}
 u(z)+lambda(A)(1-|z|^2), & |z|<1,\
 u(z),&zinOmegasetminus B.
 end{cases}
]
Indeed, its restriction to (B) is the proven Dirichlet envelope with boundary values (u|_{partial B}); the corollary provides global psh gluing, while the top Bedford–Taylor mass is zero **inside** the ball. No claim is made that the boundary carries no additional positive current.

## Mathematical verdict and publication boundary

- The integrated Theorems 7.7.4 and 7.7.7 and Corollary 7.7.5 are **not shown false**. The quadratic formula and spectral/equality analysis are self-contained **model calculations**, with the identification as *unique global Perron solution* conditional on the stated existing internal comparison/uniqueness result.
- **Proposed optional insertion:** a quadratic-data example after Theorem 7.7.4, with the exact spectral formula, non-affine two-dimensional example, and explicit quadratic balayage; do not alter any source label, permanent tag or original proof. Affected interpretive dependents: maximality tests §7.7.7 and obstacle/replacement examples in §5.47. No indirect dependency chain is certified.
- **New actual review:** integrated §7.7.4 uniqueness use, §7.7.5 boundary replacement, **first specific direct check of §7.7.6–7.7.7 maximality proof** and the new Hermitian quadratic family, with §7.3.11 only as conditional comparison. Not a complete-section certification; overall matrix remains **25 chapters / 747 numbered sections / zero fully certified mathematical sections**.
- Companion script `../checks/check_quadratic_dirichlet_spectral.py` passed **five** finite exact-rational diagonal-matrix checks. These are sanity tests, **not** a mathematical proof, build, CI, or formalization.
- The author's excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes remain strictly **deferred-by-user**, without new examination or any claim of resolution. Production main, sources, registry, permanent tags and published site are untouched.
