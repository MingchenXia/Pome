# Hyperplane restriction of twisted differential forms; integral trace rotation

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Finding: **POME-PROJECTIVE-HORIZONTAL-HYPERPLANE-RESTRICTION-001** — low / verified conditional deduction, not a printed-theorem error.

## Anchors and actual coverage

- `docs/sections/hodge-theory-curvature-and-compact-vanishing--twisted-differential-forms-on-projective-space/index.html`, blob 1099020d78b8b36519f68ba31ce180c0d843f518: whole mathematical lines 7–149. Equations 10.51.1–2 (permanent 63641BE1C835, 796E28946350; source B0B10BC1, 1D75D102), Lemma 10.51.3 (CA86EAF3228C; D4085D2A), Proposition 10.51.5 (74AA0E1253DB; E45C60C7), Theorem 10.51.6 (BEB304EB7449; EAA2912D). Earlier partial visit on November 13 is preserved; this is a whole direct reread, not a first visit.
- `docs/sections/spectral-sequences-support-and-cup-products--the-trace-in-de-rham-cohomology/index.html`, blob 1e9f8a101aedc20796ea0c47caa03f452e2c6b9a: whole mathematical lines 7–44, Theorem 10.73.1 (7ECFE434A83A; 4380D9A9).
- `docs/sections/spectral-sequences-support-and-cup-products--integral-degree-one-homology-and-integration-currents/index.html`, blob 385bebe2af8332cfa8d7974b990798670e60ce36: whole mathematical lines 8–80, Lemmas 10.74.1–2 (53C4601E9CF2, 67B6FD6C1574; 634935B7, 2322873D), Theorem 10.74.3 (87DFB6289F81; B0CE285C).
- Selected dependency: §10.72.3, lines 66–86, statement and cap/Ext identification only. No whole §10.72 claim.

The current TOC and matrix have 747 distinct section identifiers each, with equal identifier sets. Historical first-visit status of the two topology sections is not established.

## Exact restriction and branching formula

Let V be a complex vector space of dimension n+1, n >= 1, W a hyperplane, V = W ⊕ L for a chosen one-dimensional complement L, 0 <= p <= n, and integer k > p. Set m=k-p. Use lines as in 10.51.5. Write Z^{p,k}(W*) for homogeneous horizontal polynomial forms, allowing zero spaces, even when dim W=1. The natural restriction

\[
r:H^0(\mathbb P(V),\Omega^p(k))\longrightarrow
H^0(\mathbb P(W),\Omega^p(k))
\]

(pullback of differential forms, with the induced twist) is onto, with the following GL(W) × GL(L)-equivariant decomposition for the chosen splitting:

\[
Z^{p,k}(V^*)\simeq Z^{p,k}(W^*)\oplus
\bigoplus_{j=1}^{m}
\left(\Lambda^pW^*\otimes\operatorname{Sym}^{m-j}W^*
\otimes (L^*)^{\otimes j}\right).
\]

Restriction is projection onto the first summand. In particular

\[
\dim\ker r=\binom{n}{p}\binom{k-p+n-1}{n}.
\]

Proof: choose a coordinate t on L, write z for W coordinates, and let gamma_W contract with the W Euler field. Every polynomial p-form of coefficient degree m decomposes uniquely as

\[
A=\sum_{j=0}^m t^j a_j(z)+dt\wedge\sum_{j=0}^m t^j b_j(z)
\]

where a_j and b_j have coefficient degree m-j and exterior degrees p and p-1. For p=0 omit the b_j and interpret contraction of a scalar as zero. The full Euler contraction is

\[
\gamma A=\sum t^j\gamma_W a_j+\sum t^{j+1}b_j
-dt\wedge\sum t^j\gamma_W b_j.
\]

Thus horizontality is equivalent to gamma_W a_0=0, b_{j-1}=-gamma_W a_j for 1<=j<=m, and b_m=0. The dt coefficients then vanish automatically by gamma_W^2=0. Conversely these identities give a horizontal form. Hence the inverse to the displayed decomposition is

\[
(a_0,a_1,\ldots,a_m)\mapsto a_0+
\sum_{j=1}^m(t^j a_j-t^{j-1}dt\wedge\gamma_W a_j).
\]

The two terms of each summand have the same L weight j, so the formula is independent of the chosen basis of L when written using (L*)^j. It is equivariant for the block-diagonal action; no splitting independent of the choice of L is asserted. Restricting to W removes both t and dt terms, leaving a_0. Proposition 10.51.5 identifies these with the claimed section spaces. When n=1, the target is a point: for p=0 the homogeneous scalar of degree k on W gives exactly Sym^k W*, and for p>0 both target and horizontal W space vanish. This endpoint uses the point convention of 10.51.6 rather than the n>=1 statement on P(W). Finally dim Sym^{m-j} W* = binom(n+m-j-1,n-1). Summing over j gives the displayed rank by Pascal's identity, including m=1 and p=n. For p=n it equals the dimension of the entire source, as it must.

The explicit summands refine the earlier 2026-11-13 GL-equivariant character/Hilbert-series finding: that finding computes traces, not the actual kernel of the geometric restriction with an explicit inverse. The restriction is canonical, the complement-dependent splitting is not. By composing the surjections along a flag, surjectivity also holds for any nonzero linear subspace in the same positive weight range. Do not extrapolate to negative twists on a projective point.

## Review notes, dependencies and limitations

* §10.51: the homogeneous degree identity d gamma + gamma d = kI gives both inverse identities in 10.51.2 (weight zero separately). The factorial pairing transposes multiplication and differentiation, and wedge and contraction, so the projection is transpose to the corresponding projection on dual variables. The rank recurrence has numerator (n-p+1)(k-p)+p(k+n-p+1)=k(n+1). The negative homogeneous degree argument uses a line not through the puncture, possible only for dim V>=2; the dimension-zero exception is correctly stated. The positive twist vanishing is conditional on the cited Nakano tangent and parallel tensor curvature statements (10.34.10 and 10.34.6), Dolbeault identification and vanishing (10.43.11,10.33.14); the negative twist uses analytic Serre duality (10.46.7) and the perfect polynomial pairing. Untwisted diagonal cohomology uses 10.50.3. These upstream proofs are not certified here. The new restriction deduction requires only the horizontal identification, not the vanishing chain. Proposed addition after 10.51.5, no statement replacement or production edit.
* §10.73: the adjacent overlap cover has a finite-support difference map with image exactly the zero-sum finite sequences; indefinite sums preserve finite support precisely for zero total. The local step-function coboundary and the partition derivative -d psi_0 both evaluate +1 in the multiplicative augmentation convention. In the cube triangulation only the increasing coordinate order contributes to the front/back cup evaluation; the sign there is +1. Partition-of-unity decomposition of compact top forms is finite. The real-coefficient Ext term in 10.72.3 vanishes because vector spaces over a field are injective. Full algebraic duality here is the compact-first pairing, not a claim that the reverse map to the double algebraic dual is onto. Dependencies 10.44.14, 10.56.9, 10.58.9/11/13, 10.68.1, 10.72.3 remain conditional, not fully checked.
* §10.74: the based-path correction cancels at each endpoint of a cycle and kills simplex boundaries in the abelianization. Piecewise smooth path replacement requires a finite subdivision of the compact parameter interval; no general sequential compactness is used. The tubular-map inverse function estimate and uniform injectivity use the compact metrizable circle and finite-dimensional normal bundle, where subsequences are legitimate. The oriented normal framing follows by connecting the transition in GL^+(r,R); smooth gluing can be achieved with a reparameterization constant near its endpoints. For the tube Thom representative, transverse-degree m-1 form wedged before the oriented tangent form has sign (-1)^(m-1) in tangent-first orientation, as printed. Cap duality proves the integral class including torsion; pairing with real periods proves only its real image. The compact current comparison, cap naturality, compact external product and degree-one evaluation are conditional internal inputs. No new printed error or demonstrated gap here; none of these results is asserted to have a fully audited upstream proof chain.

This session: three whole direct conditional readings (one prior partial revisit), one selected dependency, one new conditional deduction; zero new confirmed errors, demonstrated proof gaps, genuine duplications or complete transitive certifications. No Demailly regularization, Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme reopened; those remain deferred-by-user, not resolved. No build, tests, CI, source, registry, permanent-tag or published-site changes.
