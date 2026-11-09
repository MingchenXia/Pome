# Integral two-forms on tori: Pfaffian intersection numbers and finite lattice duality

**Date:** 2026-11-10. **Stable finding:** `POME-TORUS-INTEGRAL-PFAFFIAN-DUALITY-001`. **Severity/status:** low / **verified conditional deduction**; **neither original printed statement is shown false**, and no existing proof is certified in full. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

## Exact integrated anchors and scope

Read the actual integrated reading-edition `docs/sections/spectral-sequences-support-and-cup-products--integral-two-periods-on-a-real-torus/index.html`, Git blob `5919e95b6add69bc972ee1fb6d7c587a4dac46eb`:

- Theorem **10.65.1**, source `demailly-complex-geometry:65DC255F`, permanent `19630A31AE86`, physical lines **7–13** (integer two-period criterion), **18–36** (connection-period sign), **38–50** (explicit lattice cocycle and connection).
- Proposition **10.65.2**, source `demailly-complex-geometry:8570E91C`, permanent `769E96CD43B2`, physical lines **55–75**, especially **62–74** (averaging homotopy, uniqueness of the invariant representative, preservation of type and positivity).

This note checks the **new top-degree and lattice-duality consequences** of those exact hypotheses, with their factorials, orientation and endpoints. The original statements only assert integrality of degree-two coefficients and averaging, not these Pfaffian/kernel conclusions. The topological finite-kernel construction below is **not** being identified with a holomorphic polarization isogeny without additional input.

## Statement

Fix an oriented lattice basis `gamma_1,...,gamma_{2n}` of `Gamma` and dual periodic coordinates `x_1,...,x_{2n}`, with `n>=1`. Let `T=V/Gamma` and let `eta` be a smooth **closed** real two-form with integral de Rham class as in Theorem 10.65.1. By Proposition 10.65.2 it is cohomologous to its unique constant representative

```text
alpha = sum_{i<j} A_ij dx_i wedge dx_j,
A_ji = -A_ij, A_ii = 0, A_ij in Z.
```

Define the integer Pfaffian using perfect matchings (indices in increasing order within each pair):

```text
Pf(A) = (1/(2^n n!)) sum_{sigma in S_{2n}}
         sgn(sigma) product_{k=1}^n A_{sigma(2k-1),sigma(2k)}.
```

Then:

1. **Exact top intersection:** `int_T eta^n/n! = Pf(A) in Z`, with sign relative to the chosen lattice orientation. For closed integral `eta_1,...,eta_n` with constant matrices `A_1,...,A_n`, the exact mixed intersection is
   ```text
   int_T eta_1 wedge ... wedge eta_n
       = [t_1 ... t_n] Pf(t_1 A_1 + ... + t_n A_n).
   ```
   Here `[t_1 ... t_n]` means **coefficient extraction**, with no additional `n!`. In particular `det A = Pf(A)^2`.

2. **Dual lattice morphism:** `B(v,w)=alpha(v,w)` has integer values on `Gamma x Gamma`. It induces a continuous homomorphism of **real** tori
   ```text
   b_alpha : V/Gamma --> V^*/Gamma^vee,
   [v] |--> [B(v, -)],
   Gamma^vee = Hom(Gamma,Z).
   ```
   If `Pf(A) != 0`, this is a finite covering with
   ```text
   #ker(b_alpha) = [Gamma^vee : B(Gamma, -)]
                 = |det A| = Pf(A)^2.
   ```
   If `Pf(A)=0`, its kernel contains a positive-dimensional torus; a finite kernel **requires** nondegeneracy.

3. **Sharp Kähler lower bound and unimodular endpoint:** If `T` is a complex torus, `eta` is Kähler, and the lattice basis agrees with complex orientation, its invariant representative `alpha` is strictly positive of type `(1,1)`. Consequently `Pf(A)` is a **positive integer**, so
   ```text
   int_T eta^n/n! >= 1.
   ```
   Equality holds exactly when `B:Gamma -> Gamma^vee` is a unimodular perfect alternating pairing. In that case there is an **integral symplectic lattice basis** `u_1,v_1,...,u_n,v_n` with `B(u_i,u_j)=B(v_i,v_j)=0` and `B(u_i,v_j)=delta_ij`; the real torus map `b_alpha` is an isomorphism. This is an arithmetic statement, **not** a claim about constructing holomorphic line bundles or a full classification of polarizations.

## Proof

**(1) Averaging and top-degree invariance.** Proposition 10.65.2 gives a globally defined one-form `beta` with `eta=alpha+d beta`, since `eta` is closed. Let `eta_t=alpha+t d beta`. Its derivative is exact:
```text
d/dt (eta_t^n/n!) =
 (d beta) wedge eta_t^(n-1)/(n-1)!
 = d(beta wedge eta_t^(n-1)/(n-1)!).
```
All `eta_t` are closed. Stokes on the compact boundaryless real torus shows that `int eta^n/n!=int alpha^n/n!`. The same argument, varying any one input while holding the other closed two-forms fixed, proves that all mixed intersections depend only on the constant representatives. This does not assume any interchange of unrelated limits.

Because the coordinate one-forms form an oriented volume basis, `int_T dx_1 wedge ... wedge dx_{2n}=1`. Expanding `alpha^n` produces only perfect matchings of the indices. Each matching contributes `n!` permutations of its pairs, while switching the entries in a pair cancels the antisymmetry sign. Thus the coefficient of `dx_1 wedge ... wedge dx_{2n}` in `alpha^n/n!` is exactly `Pf(A)`. Since each `A_ij` is an integer by Theorem 10.65.1, the perfect-matching polynomial is integer valued. Applied to `sum t_j alpha_j`, the same identity, and commutativity of wedge products of degree two, identify the coefficient `t_1...t_n` on both sides as `int alpha_1 wedge...wedge alpha_n` (NOT `n!` times that number). This proves the first two displayed claims of (1).

For completeness, `det A=Pf(A)^2` needs no external classification: for a nondegenerate alternating bilinear form over the **real** vector space, pick a nonzero vector `u`, choose and rescale `v` so `B(u,v)=1`, split off their `B`-orthogonal complement, and iterate. In the resulting real basis the matrix is `J=diag([[0,1],[-1,0]],...,[[0,1],[-1,0]])`. If `P` is the change-of-basis matrix, `P^T A P=J`. The top-wedge formula gives `det(P) Pf(A)=Pf(J)=1`, while `det(P)^2 det A=det J=1`. Hence `det A=Pf(A)^2`. The identity extends to singular `A` by polynomial continuity.

**(2) The dual map and its exact kernel.** Since `A` is integral, `B(Gamma,Gamma) subset Z`: replacing `v` by a lattice vector changes `B(v,-)` by an integral linear functional. Thus `b_alpha` is well defined. In the chosen coordinates it is induced by the real matrix `A^T` (the sign choice `-A` for the opposite slot gives the same determinant). If `det A != 0`, its kernel is `(A^T)^{-1} Z^{2n}/Z^{2n}`, equivalently `Z^{2n}/A^T Z^{2n}`. The latter finite quotient has order `|det A|`: translate a unit fundamental domain for `Z^{2n}` within the fundamental parallelepiped for the sublattice `A^T Z^{2n}`; the lattice covolume ratio is `|det A|`. No Smith-normal-form premise is needed. If `det A=0`, any nonzero real vector in `ker A^T` generates a positive-dimensional connected subgroup of the kernel, contradicting finiteness. Combine with (1).

**(3) Positivity and integral basis at the endpoint.** Translation averaging in Proposition 10.65.2 preserves closedness, type `(1,1)`, and strict pointwise positivity. Thus if the original closed `eta` is Kähler, `alpha` is a translation-invariant Kähler form. Its top power `alpha^n/n!` is a strictly positive density in complex orientation, hence the integer `Pf(A)` is at least one if the lattice orientation agrees. Equality is equivalent to `det A=1`, i.e. `A` is invertible over `Z`, and therefore to a perfect pairing `Gamma ~= Gamma^vee`.

Here is an **integral**, not merely real, symplectic Gram–Schmidt proof of the claimed basis. Take any primitive `u in Gamma`. Since the pairing matrix is unimodular, the functional `B(u,-):Gamma->Z` is primitive, so choose `v in Gamma` with `B(u,v)=1`. Define
```text
Gamma_0 = {x in Gamma : B(u,x)=B(v,x)=0}.
x_0 = x - B(u,x) v + B(v,x) u.
```
Then `x_0 in Gamma_0`, and
```text
x = B(u,x) v - B(v,x) u + x_0.
```
The three components give the **direct sum over integers** `Gamma=Z u direct_sum Z v direct_sum Gamma_0`. Since the original pairing is perfect and `B(u,v)=1`, its restriction to `Gamma_0` is again a perfect integral alternating pairing. Apply induction in dimension `2n-2` to obtain `u_i,v_i` for the complement. The resulting full lattice basis has matrix `J`; it is compatible with the chosen orientation because both Pfaffians are `1`. Conversely a standard symplectic lattice basis has determinant one and Pfaffian one. This proves the sharp endpoint without citing a classification theorem.

## Explicit factorial and determinant checks

For `n=1`, `alpha=p dx_1 wedge dx_2` gives `Pf(A)=p` and `#ker b_alpha=p^2` when `p != 0`, and the complex-orientation Kähler condition forces `p>0`.

For `n=2`, if `alpha=p dx_1 wedge dx_2+q dx_3 wedge dx_4`, then `alpha^2/2=pq,dx_1 wedge dx_2 wedge dx_3 wedge dx_4`, so `Pf(A)=pq`, `det A=(pq)^2` and `#ker b_alpha=(pq)^2` when `pq !=0`. For example `p=2,q=3` gives integral Kähler volume `6` and exact dual-kernel size `36`, **not** `72` or `6`. In a general 4-by-4 skew matrix, `Pf(A)=A_12 A_34-A_13 A_24+A_14 A_23`; this checks the alternating sign, not merely the diagonal-block case.

## Judgment, proposed change and dependency limits

**Status:** low / **verified conditional deduction**. The period integrality, quotient bundle connection sign, averaging homotopy and positive `(1,1)` conclusion of printed Theorem 10.65.1 and Proposition 10.65.2 are **consistent** with these exact intersection and lattice tests; no false original theorem or proof gap is established. The combinatorial Pfaffian, lattice-index and integer-splitting steps are independently justified above. Applying this to arbitrary smooth forms uses the **internal** averaging/period results and Stokes, whose transitive proof chains have not been fully certified.

**Proposed separately reviewable edit, NOT performed:** An optional corollary after Proposition 10.65.2 stating the integral Pfaffian top-intersection formula, the finite kernel order and the unimodular Kähler endpoint. Retain the existing historical attribution, all source labels, tags and convention distinctions. Possible dependents for cross-check, **not audited by this report:** §§10.79–10.81 (periods/projectivity/lattice quotients) and §10.75 (projective integral ring comparisons). No identification of real dual lattice morphism with a holomorphic polarization morphism is claimed without extra complex-geometric hypotheses.

**Actual coverage:** Theorem 10.65.1's exact coefficient/connection signs and Proposition 10.65.2's averaging/cohomology/positivity were inspected at the pinned lines, with a new complete arithmetic special-case proof. §10.65 had prior selected mathematical reading, so **zero new first-visited numbered sections**; **zero entire-section certifications**. §10.75 and §§10.79–10.81 are dependency links only, **not credited as freshly reviewed**. Directory inventory remains **25 chapters / 747 numbered sections / zero fully certified sections**. No project build, test suite, formal verification, GitHub Actions CI, website publication, source-body, registry, canonicalization, or main edits. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remain **deferred-by-user**, not solved.
