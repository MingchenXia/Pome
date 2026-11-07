# Degree scaling of relative Bedford–Taylor capacity under finite proper holomorphic maps

**Audit date:** 2026-11-07. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Finding ID:** `POME-CAP-PROPER-FINITE-DEGREE-001` — **low / verified conditional deduction**. This is a verified consequence of two *correctly qualified* printed results, not a false theorem, a duplicate, or a completed certification of their upstream Bedford–Taylor proof chain.

## Pinpointed reading-edition sources

- `docs/sections/relative-extremals-on-bounded-hyperconvex-domains/index.html`, main blob `c6560283c5ff9e2587ffe93f7f2e7ba687105243`; section 7.16 permanent tag `554C8622D718`.
- Proposition **7.16.4**, source label `klimek-pluripotential-theory:2CB6C014`, permanent tag `CF1B00103D5B`, physical lines **96–105**: proper surjective same-dimensional holomorphic maps preserve the *raw* and *USC-regularized* relative extremal under inverse image.
- Theorem **7.16.5**, source label `klimek-pluripotential-theory:68BF935A`, permanent tag `08DA18E923C1`, physical lines **110–115** (claim), **118–174** (proof): for any relatively compact subset of a bounded connected hyperconvex domain, outer Bedford–Taylor capacity equals the total mass of the regularized relative extremal. The main page's normalization check for a round disc occurs at physical lines **177–184**.
- The standard bounded Bedford–Taylor decreasing-continuity input is used **conditionally**. This audit gives a direct local approximation argument for the finite-map measure identity but does *not* recertify the entire original relative-capacity theorem.

## Exact degree formula

Let \(\Omega,\Omega'\subset\mathbb C^n\) be bounded, connected hyperconvex domains, and let
\[
 f:\Omega\longrightarrow\Omega'
\]
be a proper surjective holomorphic map of topological degree \(d\geq1\). Its fibers are finite. For every \(E\Subset\Omega'\), including arbitrary non-Borel sets under the outer-capacity convention, put \(E'=f^{-1}(E)\). Properness implies \(E'\Subset\Omega\). Then
\[
 H_{E',\Omega}=H_{E,\Omega'}\circ f,
 \qquad
 \boxed{\operatorname{Cap}_{\Omega}^{*}(E')
    =d\,\operatorname{Cap}_{\Omega'}^{*}(E).}
\]
More precisely, writing \(u=H_{E,\Omega'}\) and \(dd^c=\frac{i}{2\pi}\partial\bar\partial\),
\[
 \boxed{f_*\!\left((dd^c(u\circ f))^n\right)=
       d\,(dd^c u)^n.}
\]
The measure identity is valid for **every locally bounded PSH** \(u\) on \(\Omega'\), without any hyperconvexity assumption; hyperconvexity and relative compactness enter only when converting its total mass to capacity.

### Proof of the measure identity, including ramification

First suppose \(u\) is smooth PSH on the target. On a regular-value open set, the proper holomorphic map consists of exactly \(d\) local biholomorphic inverse sheets (multiplicity counted). Since \(dd^c(u\circ f)=f^*dd^c u\), ordinary change of variables gives
\[
 f_*(dd^c(u\circ f))^n=d(dd^c u)^n.
\]
The Jacobian determinant is a nonzero holomorphic function on each source component (surjectivity and the finite-map openness result prohibit generic rank loss). Its zero set has real Lebesgue measure zero. Since a holomorphic map is locally Lipschitz, the image of this null set is null in the target. Smooth top-degree forms therefore assign the critical values zero mass. Thus the identity holds across branch values as a measure equality, not merely away from them.

For general locally bounded PSH \(u\), fix a relatively compact coordinate ball \(B\Subset\Omega'\) and choose standard radial convolution approximants \(u_j\) on a slightly larger ball, smooth PSH and decreasing pointwise to \(u\). Then \(u_j\circ f\) decreases to \(u\circ f\) on \(f^{-1}(B)\). Bounded Bedford–Taylor decreasing continuity gives weak convergence of the top products **both downstairs and upstairs**. For a continuous test function \(\varphi\) compactly supported in \(B\), properness makes \(\varphi\circ f\) compactly supported in \(f^{-1}(B)\). Passing to the limit in the already-proved smooth identity yields
\[
 \int_{\Omega}(\varphi\circ f)\,(dd^c(u\circ f))^n
 =d\int_{\Omega'}\varphi\,(dd^c u)^n.
\]
A local cover and partition of unity prove the claimed equality of Radon measures. **No mass is silently discarded at ramification**: the equality holds in the weak limit on the entire target. This elementary convolution is standard local Bedford–Taylor continuity; it is **not** the user-deferred Demailly approximation/positivity-loss programme.

By printed Proposition 7.16.4, \(H_{E',\Omega}=u\circ f\). Both functions lie in \([-1,0]\). Printed Theorem 7.16.5 gives their finite total Monge–Ampère masses as the corresponding outer capacities. Taking total masses in the pushforward identity gives the formula, with no limiting interchange of unbounded energies or unspecified approximation loss.

### Exact one-dimensional normalization and sharpness

For \(0<r<1\) on \(\mathbb D\), the printed round-disc extremal is
\[
 H_{\overline{\mathbb D}_r,\mathbb D}(z)
 =\max\left\{-1,\frac{\log|z|}{\log(1/r)}\right\}.
\]
The outer radial derivative jumps by \(1/(r\log(1/r))\) at \(|z|=r\); hence its distributional real Laplacian has mass \(2\pi/\log(1/r)\) on the circle. With \(4\pi dd^c=\Delta\) in complex dimension one,
\[
 \operatorname{Cap}_{\mathbb D}(\overline{\mathbb D}_r)
 =\frac1{2\log(1/r)}.
\]
For the degree-\(d\) map \(f_d(z)=z^d\), the preimage of \(\overline{\mathbb D}_r\) is \(\overline{\mathbb D}_{r^{1/d}}\), so
\[
 \operatorname{Cap}_{\mathbb D}
       \bigl(f_d^{-1}(\overline{\mathbb D}_r)\bigr)
 =\frac1{2\log(r^{-1/d})}
 =\frac{d}{2\log(1/r)}
 =d\,\operatorname{Cap}_{\mathbb D}(\overline{\mathbb D}_r).
\]
In particular, the tempting stronger assertion that relative capacity is *unchanged* by finite proper inverse image is **false for every \(d>1\)**; this is **not** a counterexample to either printed result, both of which remain correctly stated.

## Status, corrections and dependencies

**Classification:** verified conditional deduction, severity low. The proof of the local pushforward identity is complete **given the standard bounded Bedford–Taylor decreasing-continuity theorem**. The general identity is then combined with the already printed finite-map extremal equality and compact relative-capacity mass formula, whose full transitive proofs have not been certified in this increment. No printed theorem is labelled erroneous. **Proposed content correction:** none; an optional separate exposition patch could append the degree formula beside §7.16.5, without modifying permanent tags or canonical entries in the audit branch. **Affected applications:** proper finite pullbacks in local capacity estimates and relative extremals must carry the precise topological-degree factor; use this to distinguish capacity of preimages from equality of extremal *functions*. Existing historical attributions are retained.

**Actual coverage:** new direct verification of the complete *additional* finite-map pushforward argument, and exact one-dimensional radial normalization, in an already partly audited §7.16. Selected lines only; **0 new section first visits, 0 full mathematical-section certifications**. Current ToC baseline: **25 chapters / 747 numbered sections / 0 entirely certified**. Existing false-theorem/proof-gap/candidate/external-dependency/duplication classifications unchanged. User-excluded Demailly regularization, Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remains **deferred-by-user** and was not reopened. No source, main, tag, registry, build, test, CI, formalization, or site-publication change.
