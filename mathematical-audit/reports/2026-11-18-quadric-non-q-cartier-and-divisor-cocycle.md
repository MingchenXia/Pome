# Direct audit of §§20.6–20.7: the quadric divisor has infinite local Cartier index

- Date: 2026-11-18.
- Finding: **POME-CARTIER-QUADRIC-NON-Q-CARTIER-001**.
- Severity: **low**. Status: **verified conditional deduction**. This strengthens a correct printed example; **no false statement or missing printed proof is asserted**.
- Reviewed **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (the current main head on this run).
- Integrated reading-edition files (main):
  - \`docs/sections/analytic-cycles-and-cartier-cycles/index.html\`, blob \`d4817ac64b1365bd967d42cd474fec169f992e28\`: Definition 20.6.2, source \`demailly-complex-geometry:AFD209B1\`, permanent \`BE0C86A8DD65\`, physical lines 7–9; Proposition 20.6.3, source \`demailly-complex-geometry:02B65FA7\`, permanent \`FD8966432506\`, lines 12–24; Proposition 20.6.4, source \`demailly-complex-geometry:BD1D45B4\`, permanent \`AA96C35C8290\`, lines 28–42; Example 20.6.5, source \`demailly-complex-geometry:E054C396\`, permanent \`0C462992AB3A\`, lines 46–74.
  - \`docs/sections/meromorphic-sections-and-divisor-classes/index.html\`, blob \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\`: Definition 20.7.2, source \`demailly-complex-geometry:37374C87\`, permanent \`F9B013D39957\`, lines 7–9; Proposition 20.7.3, source \`demailly-complex-geometry:00A05C89\`, permanent \`ACC6D09EDDD9\`, lines 12–28.
- Context only, **not** an entire-section certificate: \`docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html\`, blob \`dae567406b2030e550664ca57b1fe77911d956d4\`, Theorem 20.5.5 source \`demailly-complex-geometry:D58680EB\`, permanent \`F1C928146DBC\`, lines 64–127; Proposition 20.5.10 permanent \`DDB973C0C1DD\`, lines 133–150.
- Scope exclusion obeyed: no Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss argument was examined or replayed.

## Claim (local infinite Cartier index, not merely non-Cartierness)

Consider the analytic germ at the origin of
\[
 X=\{x_1x_2+x_3x_4=0\}\subset\mathbb C^4,
 \qquad
 A=\{x_1=x_3=0\}\subset X,\qquad
 B=\{x_1=x_4=0\}\subset X.
\]
The germ \(X\) is an irreducible normal threefold with an isolated singularity at \(0\). Both \(A,B\) are reduced irreducible effective Weil divisors. For **every integer** \(m>0\), neither \(mA\) nor \(mB\) is Cartier near \(0\). In particular, **\(A\) and \(B\) are not \(\mathbb Q\)-Cartier at the vertex**. In the local Weil-divisor quotient by local Cartier divisors,
\[
 [A]\text{ has infinite order},\qquad [B]=-[A],
 \qquad \operatorname{div}(x_1)=A+B.
\]
No assertion that the *entire* local class group is \(\mathbb Z\) is necessary or proved here.

## Complete proof of the new claim

1. The original Example 20.6.5 proves irreducibility, purity, smoothness off the origin, and the surjective analytic parametrization
\[
 F:\mathbb C^4_{a,b,c,d}\to X,\quad
 (a,b,c,d)\mapsto(ac,bd,ad,-bc).
\]
For completeness, its fibers over the vertex are
\(F^{-1}(0)=\{a=b=0\}\cup\{c=d=0\}\), a union of codimension-two linear subspaces in the parameter space. Off this set \(F\) is a holomorphic submersion onto \(X_{\mathrm{reg}}\), with one-dimensional scaling fibers. The quadric hypersurface has an isolated singularity and is Cohen–Macaulay; it is regular in codimension one, hence normal (Serre's \(R_1+S_2\) criterion). Normality is background context, not used in the non-\(\mathbb Q\)-Cartier contradiction.

2. Suppose that some \(mA\), \(m\ge 1\), were Cartier as a cycle near \(0\). By the **actual** definition and Proposition 20.6.4, there would be a germ of a meromorphic function \(f=g/h\), with \(g,h\) holomorphic and \(h\not\equiv0\) on \(X\), whose Weil divisor is \(mA\). Local surjectivity of \(F\) ensures \(h\circ F\not\equiv0\), so \(f\circ F\) is meromorphic. On the complement of \(F^{-1}(0)\), \(A\) pulls back to the reduced hypersurface \(\{a=0\}\), since \(x_1=ac,x_3=ad\) and at least one of \(c,d\) is nonzero there. Since \(F\) is a submersion, the divisor of the pullback meromorphic function off that codimension-two exceptional set is exactly \(m\{a=0\}\).

3. A meromorphic function on a smooth manifold has a divisorial zero/pole set. No additional divisorial component can be contained entirely in \(F^{-1}(0)\). Consequently, as **germs at \(0\in\mathbb C^4\)**,
\[
 \operatorname{div}(f\circ F)=m\{a=0\}.
\]
The convergent power-series ring \(\mathbb C\{a,b,c,d\}\) is factorial (the local analytic hypersurface factorization already used in the printed proof at §20.6, lines 71–72). Canceling numerator and denominator factors gives
\[
 f\circ F=a^m e
\]
for a holomorphic unit \(e\) at the origin. This is a unit assertion, not merely a nowhere-zero function on a punctured set.

4. For any fixed \(t\in\mathbb C^*\) close to \(1\), let \(\rho_t(a,b,c,d)=(ta,tb,t^{-1}c,t^{-1}d)\). Since \(F\circ\rho_t=F\), equality of meromorphic germs yields
\[
 a^m e=(ta)^m(e\circ\rho_t).
\]
Cancel \(a^m\) and evaluate at the origin: \(e(0)=t^m e(0)\). A unit has \(e(0)\ne0\), and a sufficiently small real \(t>1\) satisfies \(t^m\ne1\). Contradiction. Thus no positive multiple \(mA\) is Cartier. For negative multiples take the inverse of a hypothetical defining meromorphic function.

5. The hypersurface \(\{x_1=0\}\cap X\) is the union \(A\cup B\), because there \(x_3x_4=0\). At the generic smooth point of either component, \(x_1\) is a transverse local coordinate (for \(A\) use the chart \(x_4\ne0\), for \(B\) the chart \(x_3\ne0\)). Both generic multiplicities are **one**, so \(\operatorname{div}(x_1)=A+B\), not a multiple of one component. Since this is principal, \([B]=-[A]\); if some \(mB\) were Cartier, so would \(mA=m(A+B)-mB\), impossible. Both classes have infinite order.

## Direct audit of the complete printed §§20.6–20.7

- **§20.6.2–3 (definition, cycle sheaf):** Checked the pure-dimensional and locally finite hypotheses, restriction through irreducible local branches, compatibility of germ coefficients, sheaf gluing, and coefficientwise lattice operations. A locally finite collection has finitely many branches at each stalk; restriction does not identify distinct global components that share an analytic germ, by the identity theorem. No new counterexample.
- **§20.6.4 (Cartier cycles):** Checked that the singular locus has codimension at least two and therefore does not contain a prime Weil divisor, principal orders add at generic regular points, and a manifold is locally factorial. The codimension hypothesis must **not** be dropped without reexamining the definition of generic vanishing orders. No new gap found.
- **§20.6.5 (rank-one quadric):** Checked the rank-one parametrization, codimension-two exceptional preimage, submersion, factorial cancellation, and scaling-equivariance contradiction. Its original non-Cartier assertion remains true; the new proof works simultaneously for *every* positive multiple, which the original did not state.
- **§20.7.2–3 (meromorphic sections, divisor line bundle):** Checked holomorphic-frame covariance (not smooth-frame covariance), the sign in \(dd^c\log|s|_h^2=[\operatorname{div}s]-c_1(L,h)\) against \(c_1(L,h)=-dd^c\log|e|_h^2\), local quotient cancellation, transition functions \(e_i=1/u_i,\ e_i=(u_j/u_i)e_j\), and the connecting cocycle for \(1\to\mathcal O^*\to\mathcal M^*\to\operatorname{Div}\to0\). The line-bundle construction is **stated for complex manifolds** and must not automatically be extended to all Weil divisors on a singular normal space. No printed proposition was refuted.

This also provides a precise canonicalization boundary: the same reduced support \(A\) with its Weil-divisor structure is *not* interchangeable at the singular vertex with an integral Cartier divisor or a locally free invertible sheaf. On \(X_{\rm reg}\) the divisor becomes Cartier, but the vertex obstructs every positive Cartier multiple. Keep the valid smooth-manifold statement in §20.7 distinct from the singular Weil theory of §20.6; do not change source labels, permanent tags, or historical attribution.

## Dependencies, repair classification and coverage

- **Verified conditional deduction:** new infinite-index result, conditional on the printed analytic factorization/submersion facts of Example 20.6.5, complex analytic UFD of the smooth parameter germ, and the local Cartier/Weil definition. The calculation is complete under those explicit standard inputs.
- **External mathematical inputs:** factoriality of convergent power series in a regular analytic local ring, Serre normality criterion for the optional normality assertion, and existence of the local principal divisor formalism. These are named, not silently certified as newly proved from scratch. No Hironaka or regularization input is used in the new argument.
- **No confirmed error, no unresolved *new* printed proof gap, no claimed full dependency-chain certification.** The new result is a stronger corollary, not a proof repair and not a contradiction of Example 20.6.5.
- **Proposed optional mathematical-text change (not applied):** after Example 20.6.5 state that \(A\) has infinite Cartier index and \(\operatorname{div}(x_1)=A+B\), with the argument above. This is an additive precision upgrade. No source, registry, tags or publishing changes are authorized on the audit branch.
- **Affected dependents:** the scope distinction between §20.6 singular Weil cycles and §20.7.3 line-bundle divisor correspondence; any attempted automatic Weil-to-Cartier canonicalization, fractional Cartier assertion, or extension of the manifold's \(\mathcal O(D)\) construction to this vertex. This is a risk boundary, **not evidence that an actual canonicalization bug currently exists**.
- **Exact inspection:** all substantive paragraphs/proofs of §§20.6–20.7 directly read; §20.5.5 and §20.5.10 as conditional context only. Both target sections had **previous partial audit visits** (including the separate 2026-11-17 cyclic-quotient *finite* Cartier index finding): **0 new first visits, 2 newly completed full direct-section reviews, 0 fully certified transitive proof chains**. The main table of contents was re-counted from its current index: 25 chapters and 747 unique section slugs.
- This new infinite-index isolated threefold result is distinct from \`POME-CARTIER-CYCLIC-QUOTIENT-INDEX-001\`, which gave finite index \(k\) on a normal surface cyclic quotient. Neither old result is reclassified as new.
- No tests, builds, GitHub Actions, merge, publication, or main/source edits have been performed.
