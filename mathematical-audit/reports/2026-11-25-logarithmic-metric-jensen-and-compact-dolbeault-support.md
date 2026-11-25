# Jensen-improved logarithmic metric modulus and compact Dolbeault support

Date: 2026-11-25. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 6a28e2f0aff6482626fd4638b51e5aaa2e71844a.

## POME-METRIC-LOG-MODULUS-JENSEN-IMPROVEMENT-001

Low / verified conditional deduction; the printed sufficient conditions are correct. No assertion of optimality of the new threshold.

**Anchors.** Integrated `docs/sections/plurisubharmonic-functions-and-singularities--potential-regularity-and-metric-distance/index.html`, blob `26695e8698b9114b97108efb16ec94f3984ee308`, whole mathematical lines 7–161. Theorem 5.39.1 (non-kahler-pluripotential-theory:EF691FCE / permanent 230882F1D833), lines 10–43; Theorem 5.39.6 (97B8A37E / 21429B9E1BF3), lines 52–105; Corollary 5.39.7 (2F17E044 / 380EB17A4350), lines 110–131; Corollary 5.39.8 (017413AB / D3B517FBCE4F), lines 136–161. The actual printed exponent in the logarithmic corollary is \(1-a/2\), with \(a>2\); the proof estimates every annulus separately. One can instead use a cumulative Jensen estimate.

**Claim.** Retain the local hypotheses of Theorem 5.39.6 except replace its square-root Dini condition by the modulus bound \(m(r)\le C(\log(1/r))^{-a}\) for some \(a>1\) and small \(r\). Then
\[
d_\eta^U(x,y)\le C'(\log(1/|x-y|))^{-(a-1)/2}
\]
for sufficiently close regular points in a fixed small chart. In particular all the completion conclusions of that theorem hold under this weaker hypothesis. The family compactness conclusion of 5.39.8 also holds with a common such logarithmic modulus and the same background bounds (including its lower metric bound when assumed).

**Proof.** Write \(d=2n\), \(\mu=T\wedge\omega_E^{n-1}\). On a fixed relatively compact chart, the smooth background bound gives \(0\le\mu\le C\,\Delta w_x\) in the sense of measures, where \(w_x(z)=v(z)+B|z-x|^2\) and a sufficiently large fixed \(B\) is chosen. Here the constant incorporates the Euclidean normalization of \(dd^c\), and \(\Delta w_x\) is nonnegative; closedness of the background is not used. For balls centered at \(x\), the real spherical mean formula yields
\[
\int_0^R t^{1-d}\mu(B(x,t))\,dt
\le C\big(m(R)+R^2\big).
\tag{1}
\]
Indeed for a smooth \(w\) the derivative of its normalized spherical mean is \(|S^{d-1}|^{-1}t^{1-d}\int_{B(x,t)}\Delta w\), by the divergence theorem. Integrate from zero to \(R\). For continuous \(w_x\), ordinary nonnegative Euclidean convolution on the interior converges uniformly on compact sets, and the positive Laplacian measures converge distributionally and hence vaguely (local mass bounds follow by positive cutoffs). For each open ball their liminf dominates the limiting mass by continuous inner cutoffs. Fatou proves the inequality for \(w_x\); the difference of spherical mean and center value is bounded by \(m(R)+BR^2\). This elementary scalar mean argument is not analytic-singularity or positivity-loss regularization.

Fix small \(s_0\), \(s_k=2^{-k}s_0\), and \(b_k=s_k^{2-d}\mu(B(x,s_k))\). The intervals \([s_k,2s_k]\) have disjoint interiors, and on each interval monotonicity of the ball mass gives an integral at least \(c_d b_k\), including \(d=2\) where the factor is \(\log 2\). Thus (1) implies
\[
\sum_{k\ge N}b_k\le C[m(2s_N)+s_N^2]\le C'(1+N)^{-a}.
\tag{2}
\]
All constants are uniform in regular centers in a smaller chart. As at printed lines 82–91, the contribution of each dyadic annulus to the mean segment-length bound is at most \(C\sqrt{b_k}\): Cauchy–Schwarz, the annulus volume bound, and \(\tau\,d\lambda\le C\mu\) give exactly \(s_k^{1-d}s_k^{d/2}\mu(B(x,s_k))^{1/2}\).

For \(N\ge1\), group the indices into blocks \([2^jN,2^{j+1}N-1]\), rather than bounding each \(b_k\) separately. Cauchy–Schwarz and (2) give
\[
\sum_{k=2^jN}^{2^{j+1}N-1}\sqrt{b_k}
\le C(2^jN)^{(1-a)/2}.
\]
The geometric series converges precisely for the claimed range \(a>1\) of this argument. Consequently the average segment length to points of a ball of radius \(R\) is bounded by \(C(\log(1/R))^{(1-a)/2}\): choose \(N\) with \(R\le s_N<2R\), and use the printed polar integration bound on that ball (or compare its volume to the slightly larger ball). For \(x,y\) average the two segments over the midpoint ball of radius \(|x-y|/2\), as in lines 39–41 and 102. Its volume is comparable to the balls of radius \(2|x-y|\) at the endpoints. Almost every segment avoids the analytic set: its local strata have real codimension at least two and their cones from a regular point have zero \(d\)-dimensional volume. The average is finite, so some admissible broken segment realizes the bound. Shrinking the chart ensures the segments remain inside \(U\).

The new bound tends to zero and is uniform in the stated families. Hence the exact compactness, completion, and lower-bound arguments in lines 104 and 145–160 apply without change, replacing \(D\) by this modulus. Compactness here uses the global connected compact convention §1.1, not a noncompact counterexample. For incompleteness, an escaping sequence near a deleted point cannot converge to a regular point because a small closed coordinate ball there has a positive lower metric bound. All conclusions are conditional on the printed trace/stratification framework; this does not certify its full dependency chain.

**Correction proposal and dependents.** No correction of a false claim is needed. Add this as a stronger logarithmic clause to 5.39.7 and an alternative family hypothesis to 5.39.8. In particular \(1<a\le2\) is covered even though the square-root Dini integral of this specified modulus is infinite. For \(a>2\) the new rate is also stronger. No necessity or sharpness claim at \(a=1\) is made. Any subsequent use of these metric compactness statements can use the improved sufficient modulus; no production citations changed.

## POME-DOLBEAULT-COMPACT-CURRENT-FILLED-SUPPORT-001

Low / verified conditional deduction; not a false printed theorem.

**Anchors.** Integrated `docs/sections/complex-homotopy-operators-and-hartogs-extension/index.html`, blob `e0aea9511e5f9e427463ae94002b38da8919ac94`, mathematical lines 7–137. Proposition 5.49.1 (klimek-pluripotential-theory:4FD27637 / 7ACDC1AF162C), lines 7–36; Theorem 5.49.4 (411BC839 / 4DB91EC236EA), lines 110–123; Theorem 5.49.5 (8068BB5B / 5617D4B2FDA2), lines 128–137. The printed higher-dimensional compact-support assertion explicitly starts with smooth data.

**Claim.** Let \(n\ge2\) and \(\alpha\) be a compactly supported closed \((p,1)\)-current, with support in a compact set \(E\subset\mathbb C^n\). Define \(E^{\mathrm{fill}}\) as the complement of the unbounded connected component of \(\mathbb C^n\setminus E\). Then the unique compactly supported distributional \((p,0)\)-primitive is \(K\alpha\), its support lies in \(E^{\mathrm{fill}}\), and if the current has order at most \(s\) its primitive has local order at most \(s\). The primitive is \(C^s\) for compact \(C^s\) data. The filled-set bound is universally sharp for arbitrary compactly supported currents with support contained in \(E\), for each \(0\le p\le n\).

**Proof.** The printed Proposition 5.49.1 gives \(\bar\partial K\alpha=\alpha\), since the other term vanishes by closedness. Every compact distribution has finite order on a fixed compact neighborhood of its support. Outside a sufficiently large ball each coefficient of \(K\alpha\) is a distributional pairing against the explicit kernel \(k_j(z-\zeta)\) and a fixed smooth cutoff near \(E\). All derivatives of order \(l\) of \(k_j\) satisfy \(O(|z|^{1-2n-l})\) away from zero, by homogeneity and smoothness on the sphere. Derivatives landing on the fixed cutoff still give \(O(|z|^{1-2n})\). The distribution bound therefore gives the same decay \(O(|z|^{1-2n})\) as for smooth data. Differentiating in output variables is legitimate away from \(E\), because the kernel is smooth there and these pairings are locally uniform. The coefficients are holomorphic on the complement of \(E\) by the equation.

Choose \(R\) containing \(E\). For every fixed \(z'\in\mathbb C^{n-1}\) with \(|z'|>R\), the restriction in \(z_n\) is entire and tends to zero as \(|z_n|\to\infty\). Liouville gives zero, and the identity theorem on the connected exterior of the ball gives zero throughout that exterior. Any unbounded component of the complement meets this exterior, which is connected and contained in the complement; hence there is exactly one unbounded component. Analytic continuation gives zero on it. The filled set is closed and bounded, proving compactness of the support. The regularity and order bounds are exactly those of 5.49.1. If two compact primitives exist, their difference is a compact distribution with closed \((p,0)\) coefficients. Convolving with a compact smooth approximate identity gives compactly supported entire coefficients, hence zero. Convergence in distributions gives zero difference. This uses only elementary convolution, not the excluded programme.

For sharpness, every bounded complementary component \(G\) has boundary contained in \(E\). Its indicator function times any constant nonzero holomorphic \(p\)-form is a compact distribution \(u\); its derivative \(\alpha=\bar\partial u\) is supported in \(\partial G\subset E\), and is closed. Uniqueness forces the primitive to be \(u\), nonzero on the entire component. For a point in the interior of \(E\), a smooth bump near the point times the same form gives a primitive nonzero there. Finally for any point \(x\in E\), one may take \(u=\delta_x\) times a constant \(p\)-form, understood coefficientwise as a distributional \((p,0)\)-form; its derivative is supported at \(x\) and uniqueness gives that very primitive. Thus every point of \(E^{\mathrm{fill}}\) occurs in the support of a primitive in the unrestricted current class. This last sharpness statement is not a smooth-data sharpness assertion.

**Proposal and dependents.** Strengthen the higher-dimensional clause of 5.49.4 using the already printed distributional homotopy, and distinguish the bounded holes from a chosen enclosing ball. The Hartogs argument in 5.49.5 remains valid as printed and now has an explicit support refinement. The dimension-one moment obstruction in 5.49.4 is distinct and unchanged.

## Direct coverage and normalization checks

- §5.39: full direct lines 7–161, including cutoff trace estimate, coefficient domination, sharp local power example, segment avoidance, square-root Dini annuli, log integration and family pseudometric convergence. No original error found.
- §5.48: full direct `docs/sections/stokes-formula-and-homotopies/index.html`, blob `bd3ba3b5150ff2a60c265f67706f74f9c980333c`, lines 7–70, Theorems 5.48.1 (klimek-pluripotential-theory:3D6DA517 / 8F5E6DB87531) and 5.48.2 (6D21AD1E / 5FF0038BBA5C). The outward normal of \(x_j\le0\) is \(+\partial_{x_j}\); insertion into the oriented volume gives the sign \((-1)^{j-1}\). In the product homotopy decomposition \(a+dt\wedge b\), the \(dt\) coefficient of its derivative is \(\partial_t a-d_M b\); integration proves the endpoint identity, also for degree zero. No new printed error or gap.
- §5.49: full direct lines 7–137, including \(\bar\partial D+D\bar\partial=-\Delta/4\), distribution-order estimates, Bochner–Martinelli sign, Cauchy–Pompeiu boundary sign, edge cutoff estimate, polydisc induction and dimension-one moment characterization. For the BM sign at lines 43–52, moving the new antiholomorphic differential past the \(n\) holomorphic ones contributes \((-1)^n\); its insertion among the other antiholomorphic differentials cancels the displayed \((-1)^{j-1}\). Conversion of the grouped volume form to real volume contributes \((-1)^{n(n-1)/2}(-2i)^n\); combined with the displayed coefficient the density is positive \(n!/\pi^n\) times the stated radial factor. At lines 78–84 the derivative of the indicator pairs as minus the outward boundary integral, consistent with the printed one-variable kernel. Proposition 5.49.2 (357960EE / 65D5B333E685) and Theorem 5.49.3 (DD0E6E8E / 72B026809F75) were also read directly. No original error found.

Three whole current direct sections; two verified conditional deductions; zero new confirmed false printed theorems, zero newly demonstrated proof gaps, zero transitive proof-chain certificates. Historical first visits are not asserted. Demailly approximation/regularization and all its dedicated programmes stay deferred-by-user. No builds, tests, CI, source, permanent-tag, registry, main or website changes.
