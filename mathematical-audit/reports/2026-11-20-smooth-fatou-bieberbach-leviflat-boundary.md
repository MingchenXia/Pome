# Chapter 9: complete direct audits of §§9.19, 9.22 and 9.23 (20 November 2026)

**Baseline:** production main b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** integrated reading-edition HTML at the precise paths below. Earlier selected reviews of these sections are preserved, not claimed as first visits. This is a current full *section-text* reading, not certification of the complete dependency graph. No Demailly approximation/regularization, or dedicated Bergman/L²/OT/multiscale/positivity-loss programme, is opened.

## New finding: POME-FB-LEVI-FLAT-JACOBIAN-VOLUME-001

- **Status:** verified conditional deduction (not a false printed theorem).
- **Severity:** low (useful geometric consequence).
- **Location:** Theorem 9.22.2, source label klimek-pluripotential-theory:BDF5266C, permanent tag CE10A564601F; integrated file docs/sections/a-smooth-boundary-for-a-proper-biholomorphic-image/index.html, blob 1279ba00791fa992f753ddd35a63cfc0fa36973f, physical lines 49–96, especially 55–62 (shear Jacobians), 80–83 (smooth limit boundaries), and 85–95 (inverse biholomorphisms). Local stability is Lemma 9.22.1, source D16FE002, permanent tag 9D4AAB621920, lines 7–45.
- **Precise claim:** the specific smooth proper Fatou–Bieberbach domain Ω constructed in the integrated proof has (i) **Levi-flat smooth boundary**, (ii) **infinite Euclidean four-volume**, and (iii) **nonconvexity**. None of these assertions is a contradiction to the printed existence theorem.

### Complete deduction: boundary Levi-flatness

The recursive construction has polynomial automorphism coordinates (P_j,P_{j-1}), with D_j={|P_j|<T_j}. Because P_j is one coordinate of an automorphism, dP_j does not vanish. Near any point of ∂D_j, P_j≠0, so

\[
r_j(z)=\log|P_j(z)/T_j|
\]

is a smooth local defining function with dr_j≠0. It is **pluriharmonic**, since P_j is nonzero holomorphic there:

\[
\partial\bar\partial r_j=0.
\]

Thus the intrinsic Levi form of ∂D_j is identically zero. This is independent of the choice of local defining function: two smooth defining functions with the same negative side differ by a positive smooth factor on the boundary, and their Levi forms on complex tangents differ by that factor.

Lines 71, 80–83 construct real ambient diffeomorphisms Φ_j, C^j-close to the identity with summable errors, locally identifying D_{j-1} and D_j. Their compositions and inverses converge in C^m on each fixed compact set, for every m; in particular, near each limit boundary point the hypersurfaces ∂D_j can be expressed as graphs in a fixed real chart converging in C² to a graph of ∂D_∞. The intrinsic Levi form is a continuous expression in the first two derivatives of that graph and in the complex tangent projection. Passing to the limit from identically zero Levi forms gives

\[
\boxed{\mathcal L_{\partial D_\infty}\equiv0.}
\]

The chosen component Ω⊂D_∞ has boundary patches equal to patches of ∂D_∞ by the smooth local-sidedness argument on line 83. Therefore

\[
\boxed{\mathcal L_{\partial\Omega}\equiv0.}
\]

No convergence of the unnormalized functions log|P_j/T_j| is assumed or required; only the already constructed C² convergence of the *hypersurfaces* is used. The conclusion says smooth Levi-flat, **not** strictly pseudoconvex.

### Complete deduction: infinite Euclidean volume

Each F_j is a composition of alternating triangular polynomial shears and has complex Jacobian determinant identically 1 (line 56). The locally uniform holomorphic limit F:Ω→ℂ² therefore satisfies det_ℂ DF=1, as recorded on line 91. Lines 93–95 prove F is a biholomorphism onto ℂ², with inverse G. The real Jacobian of a holomorphic map is |det_ℂ DF|², hence the real change-of-variables theorem gives

\[
\boxed{\operatorname{Vol}_{\mathbb R^4}(\Omega)
=\int_\Omega |\det_{\mathbb C}DF|^2\,dV
=\operatorname{Vol}_{\mathbb R^4}(\mathbb C^2)
=+\infty.}
\]

Thus Ω is unbounded. This is a property of this exact Jacobian-one construction, **not** a claim about all possible Fatou–Bieberbach domains.

### Complete deduction: nonconvexity

If a nonempty proper open convex subset U⊊ℂ² were biholomorphic to ℂ², it would lie in a proper real affine half-space. One elementary justification: the closure of U is proper (otherwise the open convex set would contain every point as the interior of a simplex with vertices in U); project an exterior point onto the closed convex set to obtain a nonzero separating real-linear functional. Every real-linear functional on ℂ² is Re L for a complex-linear L. Thus Re L<C on U for some nonzero L.

For an entire biholomorphism G:ℂ²→U, exp(L∘G) would be a bounded entire function, hence constant by Liouville. Because G is surjective and L is nonzero, this is impossible. Applying this to Ω proves its nonconvexity. This argument does not assume boundary regularity.

- **Proposed optional text addition:** after Theorem 9.22.2, a remark that the constructed domain has smooth Levi-flat boundary and infinite Euclidean volume, with the boundary-limit and constant-Jacobian explanations above. Do not edit mathematical source/body or tags directly.
- **Affected dependents:** Theorem 9.22.2's geometric interpretation; examples referencing its Fatou–Bieberbach domain, including selected §16.43 applications. The theorem itself remains valid.
- **Upstream status:** relies on the printed local C^∞ hypersurface convergence and inverse-limit construction, both directly checked here, plus elementary Levi calculus and change of variables. No independent verification of every global/topological result in the repository is implied.

## Full reading of §9.22 (lines 7–98)

Lemma 9.22.1: verified the exponent estimates on the band ||P/S|−1|<2/(16√N), where |(P/S)^N| is bounded below exponentially in −√N and the Q/T error is smaller; the derivative loss is at most polynomial in N, absorbed by e^{−c√N}. Outside the narrower band the signs of the two defining functions agree. The Moser-type time-dependent vector field X_t=−e_N ∇r_t/|∇r_t|² transports the zero levels on fixed balls. The spatial cutoff and summable C^m control are required and appear explicitly.

Theorem 9.22.2: checked the inverse-shear smallness from T_{j−1}>2(j+1) and log T_j=O(√N_j), the local C^∞ domain limit, forward normal-family contraction on compact connected neighborhoods containing the origin, and convergence of the inverse maps on target balls. The limit maps are inverse by taking limits in their mutual identities only on fixed compact sets. **No new confirmed printed error** or asserted full external proof-chain certificate.

## Full reading of §9.19 (lines 7–37)

Proposition 9.19.1: for s²=(ρ−R)²+|y|² and m≥3, the integrated proof uses the exact cylindrical calculation

\[
\Delta s_\varepsilon=
\frac{m-1-R/\rho}{s_\varepsilon}
+\frac{\varepsilon^2}{s_\varepsilon^3}.
\]

On the tube s<r<R/2 one has ρ>R−r>R/2, giving strict positivity; the decreasing limit defines the distributional subharmonic function s−r even at the core circle. Distances to the boundary in the tube and in the exterior collar follow from the 1-Lipschitz inequality and normal segments. Connectedness of the exterior uses the nonempty y-coordinate for m≥3. **No new confirmed printed error.** The previously logged **POME-TUBE-RADIUS-SHARP-001** gives the exact sharp radius threshold and must not be counted as a new result here.

## Full reading of §9.23 (lines 7–71)

Theorem 9.23.1: checked the Hardy-space orthogonal projection, Toeplitz coercivity T=P(W·)≥cI, minimizer with specified constant coefficient, identity P(WF)=constant, and the actual difference-quotient/Sobolev induction giving boundary C^∞ regularity. From F*WF constant and positivity, F is invertible on the circle; division by the Blaschke factor at a hypothetical interior zero reduces the weighted energy by |a|² and contradicts minimality. Finally H=A^{1/2}F^{-1} is a smooth invertible spectral factor, unique up to left constant unitary multiplication. **No new confirmed printed error.** The earlier **POME-CIRCLE-SPECTRAL-FACTOR-ORDER-001** already records Loewner monotonicity, concavity and exact determinant mean identity; none is rediscovered or re-credited here. Selected input: Proposition 9.20.1, source klimek-pluripotential-theory:0D2877F2, permanent 659A580EE96C, checked for Fourier/Hardy calculus, not its entire longer proof chain.

## Reproducible anchors, scope and open ledger

- §9.19: docs/sections/boundary-distance-counterexamples-in-higher-dimension/index.html; blob e078f8041dbae929c9d2076e62a72326622c158d; source klimek-pluripotential-theory:7EB9EC12 / permanent EF227A55DB12; full mathematical physical lines **7–37**.
- §9.22: docs/sections/a-smooth-boundary-for-a-proper-biholomorphic-image/index.html; blob 1279ba00791fa992f753ddd35a63cfc0fa36973f; lemma source D16FE002 / permanent 9D4AAB621920 and theorem source BDF5266C / permanent CE10A564601F; full mathematical physical lines **7–98**.
- §9.23: docs/sections/smooth-positive-matrix-factorization-on-the-circle/index.html; blob 04780d065ee474f3bb3255db297ac435e00485a1; source klimek-pluripotential-theory:02D391FB / permanent 35AF621E1787; full mathematical physical lines **7–71**.
- **Coverage delta:** +3 complete direct section readings, +1 selected Proposition 9.20.1 input, +0 complete transitive upstream-chain certifications. The three sections previously had selected/historical visits, so this makes **no first-ever-visit claim**. Other unreviewed or historically unreconciled sections are not marked reviewed.
- **Classification ledger:** new finding confirmed as a conditional deduction from the printed construction; no false original theorem, no asserted new proof gap, no duplicate claim. Historical sharp tube radius and spectral-factor order/determinant findings unchanged. Excluded Demailly and dedicated programmes remain **deferred-by-user** rather than resolved or certified.
- **Operations:** Markdown audit notes only. No tests, builds, GitHub Actions, publication, original math/source/registry/canonicalization/permanent-tag changes.
