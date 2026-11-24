# Normal-fiber classical masses: uniform truncation and upper semicontinuous jumps

Date: 2026-11-24. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Finding: **POME-NORMAL-FIBER-UNIFORM-VAGUE-JUMP-001** — low / verified conditional deduction (not a false printed theorem).
Scope: four whole direct readings of current nonexcluded sections, one selected collar-identity dependency and statement-level checks of two further dependencies. Historical first visits remain unreconciled; no complete transitive certification.

## Immutable integrated anchors

All paths below are relative to `docs/sections/`, with suffix `/index.html`. Prefix `lelong-densities-generalized-masses-and-multiplicity--` is common to the first five rows.

| Section and suffix | Blob | Physical mathematical lines and stable tags |
|---|---|---|
| 6.43 finite-germs-and-their-actual-integer-degree | e2a86c5438c7770a8766f6bedf779e1879ead4c0 | 7–55; 6.43.1 AD7655D0958A / F459CB6C, 6.43.2 B1AA1442D441 / E27EA362 |
| 6.46 proper-direct-images-and-finite-map-upper-bounds | 1f44c5feb546ecfe43ec1bc752d3fd0bff501613 | 7–63; 6.46.1 86EB492BC979 / 8BBE1973, 6.46.2 751F9003E019 / 784313F4 |
| 6.47 monomial-maps-and-the-sharp-directional-comparison | bad5cd9bb63a90871462700f5c1f7080c597ee99 | 7–45; 6.47.1 0A17C5BE0625 / F608EF8B, 6.47.2 240191846A51 / 9E33C486 |
| 6.48 normal-fiber-masses-and-integral-logarithmic-coefficients | 5b1dff0cd7287091c55d59bdd990f1869e61c224 | 7–97; 6.48.1 D0453276E370 / AA87475F (esp. lines 31–56), 6.48.4 DBE978B1362A / 1D3F3B08 |
| 6.34 weights-and-generalized-lelong-masses | 3bfe070c28159bff5f2e90a3f8d8ba695bde26e4 | 7–40 selected, Lemma 6.34.1 ECBFCBBB5EF1 |
| 6.40 siu-decomposition-in-arbitrary-bidimension (same prefix) | 76094d2efe4c1a0c306f19d592c1e11029a6a5d9 | 20–29 statement of 6.40.2 5C624FF7D159 only |
| 7.31 classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current | 86de377d6e6f17fc1a08a6e789a681ddfaabfac5 | 70–77 Corollary 7.31.4 EBA900FA96EF and cited theorem, not its upstream proof |

## New deduction

Keep precisely the assumptions of Lemma 6.48.1: u is extended-continuous PSH on D x W, with pole set exactly {0} x W, where D is a centered normal ball in C^q and W is a connected parameter ball. Let u_m=max(u,-m), and let mu_{m,w} and mu_w be their full classical fiberwise top products. Use the printed normalization dd^c=i/(2pi) partial bar-partial. Then:

1. For every compact L in W and continuous compactly supported f on D x W, the fiber integrals of f(z,w) against mu_{m,w} converge **uniformly on L** to those against mu_w. In particular w -> mu_w is vaguely continuous at every parameter, not just almost everywhere.
2. The function a(w)=mu_w({0}) is upper semicontinuous. With lambda the constant coefficient of the printed lemma, a(w)>=lambda for every w, and equality holds off a meagre Lebesgue-null set. The possible exceptional set is a countable union of relatively closed nowhere dense sets. For the holomorphic integer tuple in Theorem 6.48.4 the normal-fiber degrees are positive integers and the exceptional set is relatively closed and null.
3. In general the individual point atoms cannot converge continuously. The full weak continuity in (1) retains the disappearing or concentrating nearby diffuse mass.

### Proof of uniformity

Fix a radius R with closure B_R in D, containing the normal support of the tests under consideration strictly inside it. In the q=n case the parameter is a singleton. The printed collar and CLN argument, lines 31–50, supplies a uniform bound C for mu_{m,w}(B_R), m sufficiently large and w in L; if necessary work with a slightly larger buffered radius to bound the limit measure on B_R as well. All estimates below concern the same fixed compact L.

For any small r>0 with 2r<R, u is finite continuous on the compact annulus r<=|z|<=R over L (and on a buffer beyond R). Thus for all m>=M(r,L) the functions u_m and all later truncations agree with u there. Locality, also for the full classical product on the bounded region away from the pole, gives equality of mu_{m,w} and mu_w on r<|z|<R. To avoid any assumption about sphere masses, choose a fixed smooth radial cutoff chi, equal to one on B_r and supported in B_{2r}. For k>=m the measures mu_{k,w} and mu_{m,w} agree away from B_r in B_R. The bounded collar identity 6.34.1 on B_R gives equality of their total masses there, including when the boundary sphere is charged (the primitive is compactly supported inside). Hence their integrals against chi are equal. For each fixed w, let k go to infinity using the printed classical decreasing continuity (7.31.4), with this compactly supported continuous test. We obtain equality of the integrals against chi for mu_w and mu_{m,w}; since they agree on the support outside the central ball, their signed difference in B_R has total mass zero and is supported in the closed ball of radius r. Equivalently one can directly keep the cutoff throughout, which avoids any restriction of a weak limit to a ball.

It follows for the compactly supported f, with zero extension near the boundary of B_R, that

    |int f(z,w) d(mu_{m,w}-mu_w)(z)|
      = |int chi(z)(f(z,w)-f(0,w)) d(mu_{m,w}-mu_w)(z)|
      <= 2 C sup_{w in L, |z|<=2r} |f(z,w)-f(0,w)|.

The right side tends to zero by uniform continuity on a compact product. For every fixed r the inequality holds for all m>=M(r,L), proving the asserted uniform limit. No claim of uniform convergence of the atoms or uniform convergence in total variation is involved.

For fixed m, u_m is jointly continuous and locally bounded. As w approaches w0, its restrictions to normal fibers converge locally uniformly; bounded Bedford–Taylor uniform continuity gives vague continuity of the resulting measures. For varying tests f(z,w), the uniform CLN bound on their normal support controls the difference from f(z,w0). These arguments hold for nets as well, via uniform continuity on compact parameter neighborhoods and the usual local uniform topology of bounded continuous potentials; equivalently here the parameter domain is metrizable. Uniform convergence of the integrals on compact neighborhoods now proves (1).

### Atom jumps and sharp example

For a sequence of continuous radial cutoffs decreasing to the indicator of {0}, their integrals against mu_w are continuous by (1). Their infimum is a(w) by continuity from above. Thus a is upper semicontinuous. The printed a.e. identity a=lambda implies that the equality locus is dense; upper semicontinuity implies a>=lambda everywhere. The sets {a>=lambda+1/j}, j>=1, are closed in W, have zero Lebesgue measure and therefore have empty interior. Their union is precisely {a>lambda}. This proves (2). For an integer tuple all a(w) are positive integers by Proposition 6.43.1. In that case lambda is also an integer and the exceptional set equals {a>=lambda+1}. No assertion of analyticity of the jump locus is made.

For any q>=1 and one complex parameter w, take

    u(z,w)=log(|z_1|^4+|w z_1|^2+sum_{j=2}^q |z_j|^2).

This is extended-continuous PSH, has exactly the stated pole set, and comes from a holomorphic tuple. For fixed w!=0 the potential differs by a bounded function near zero from log(sum |z_j|^2): the coefficient of |z_1|^2 is bounded above and below there. At w=0 it is the logarithm of the squared norm of (z_1^2,z_2,...,z_q). The bounded-change and isolated finite degree results of 6.43.1 give a(w)=1 for w!=0 and a(0)=2, by independent root counts. Thus lambda=1, the exceptional point is genuine, and one cannot replace the printed a.e. coefficient formula by equality at every parameter. By (1), the full fiberwise products still converge vaguely at w=0. This also shows that uniform vague convergence of truncations cannot be upgraded to atom convergence uniform in the parameter (for every m the bounded products have no point atom by the bounded Bedford–Taylor noncharging property).

## Other direct reading checks

- 6.43: proper local representative follows from a boundary lower bound; finiteness of compact analytic fibers, generic sheet degree and image multiplicity are kept distinct. Coordinate divisor intersections have the required proper codimension by successively imposing the remaining equations. The local degree calculation uses proper pushforward before taking the decreasing-product limit, not convergence of individual atoms without support control. Remmert, the analytic multiplicity theorem 6.38.3, 20.5.3/10 and 7.31 remain dependencies, not independently certified here.
- 6.46: the proof correctly uses clopen neighborhoods of singleton components, not an assertion of isolated points of the entire fiber. Compactness separates finitely many pieces, and the finite-subsums formulation allows arbitrary fibers. The codimension estimate for a competing target germ follows from the local intersection dimension inequality and finite composite; the infimum is over a nonempty set with positive denominators. No integer upper-multiplicity claim. The local weight comparison, augmentation and generic slice inputs remain conditional.
- 6.47: generic plane and target projection give the component-order lower bound without pretending the system is triangular. Upper bound uses the total mass on a fixed ball, not semicontinuity of isolated degree with moving zeros alone. The common-multiple composition yields the upper directional constant and coordinate planes attain both extremes. The real-coefficient approximation is squeezed multiplicatively for strictly positive coefficients, not by an unproved limit of generalized measures.
- 6.48: codimension for repeated factors holds up to q, the fixed collar produces an actual mass identity, and the two dominated-convergence passages in the printed proof are separate. Extracting atoms through continuous cutoffs of fixed measures is legitimate. The bounded difference of the two logarithms in 6.48.4 uses the elementary sum-of-squares inequality, and the two directions of the comparison preserve the coefficient.

No newly confirmed printed theorem error or unresolved new proof gap. Proposed correction is an optional supplementary remark after 6.48.1 and 6.48.4 distinguishing vague continuity, a.e. generic atoms and upper semicontinuous jumps; original assertions stand. Affected dependents: coefficient interpretation in 6.48.4 and any later application that would require all-fiber equality rather than a.e. equality; no such downstream error is established in this run. Full transitive verification remains open, including the cited classical decreasing-product, support, and finite-degree theorems. No Demailly approximation, dedicated Bergman/L2/OT/multiscale/positivity-loss programme reviewed; all remain deferred-by-user. No source or registry changes, no build, tests, CI or publication.
