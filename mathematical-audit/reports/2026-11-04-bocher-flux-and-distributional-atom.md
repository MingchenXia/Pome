# Auditing Bôcher's isolated-pole lemma: exact flux and atomic Laplacian

**Date:** 2026-11-04 (Asia/Shanghai).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Finding:** POME-HARM-BOCHER-FLUX-ATOM-001.  
**Severity/status:** low / **verified conditional deduction**; no false theorem or existing proof defect established.  
**Exact new coverage:** first selected independent proof-level check of Lemma 3.3.16, *not* a complete review or certification of §3.3 or the classical potential-theory dependency graph.

## Pinned integrated statement and proof

- Reading edition: docs/sections/classical-harmonic-analysis/index.html, blob 75e982788e627af602981823a82863cbd36ee712; physical lines **215–227**.
- Lemma **3.3.16**, source **classical-potential-theory:6C6775C3**, permanent tag **B0CFE200676D**, actual statement lines **217–219** and replacement proof lines **221–226**.
- It asserts that for a nonnegative harmonic function on a punctured neighborhood of a point in real dimension d ≥ 2, one has h = c Φ + v with c ≥ 0, where v extends harmonically across the point, Φ(r)=log(1/r) in dimension 2 and Φ(r)=r^(2-d) in dimensions d ≥ 3.
- The printed proof invokes local Riesz decomposition, local integrability, and Weyl's lemma. It is consistent; this audit supplies an independent direct route through spherical means, annular Harnack estimates, and distributional flux, including an additional normalization absent from the printed lemma.

Relevant *established internal* inputs, crosschecked for exact mathematical content, not recertified:
docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html, blob fc02188d6e246a21aa07acd8bf6d3712761ba6e5:
Theorem 3.1.7 (interior derivative estimate (3.1.8)), permanent A60BA3B2DBFC, physical lines **136–149**; Proposition 3.1.19 (local Harnack), permanent DAC835A39525, physical lines **365–414**; Theorem 3.1.11 (Weyl's lemma), permanent C9127FBA9AE8, physical lines **210 onward**. Their proofs are *dependencies*, not newly independently certified here.

## Precise strengthening

Put s_(d-1) = area(S^(d-1)) and
\[
\kappa_d =
\begin{cases}
2\pi, & d=2,\\
(d-2)s_{d-1}, & d\ge3.
\end{cases}
\]
Let 0 < r < r_0 and let \(\nu\) be the radial outward unit normal from a. For any nonnegative harmonic h on B(a,r_0)\{a}, its locally integrable extension across a has the exact distributional identity
\[
-\Delta h=\kappa_d c\,\delta_a,
\qquad
c=-\frac1{\kappa_d}\int_{\partial B(a,r)}\partial_\nu h\,dS\ge0.
\]
The flux is *independent of r*. If M(r) denotes the normalized spherical average, then
\[
 c=\lim_{r\downarrow0}\frac{M(r)}{\log(1/r)} \quad(d=2),
 \qquad
 c=\lim_{r\downarrow0}r^{d-2}M(r) \quad(d\ge3).
\]
Equivalently, c=0 if and only if the puncture is removable for h. The sign and normalization are exact, rather than only up to a positive factor.

## Direct proof (no Riesz decomposition, no approximation programme)

1. Translate a to 0. Define M(r) as the sphere average of h(rθ) over |θ|=1. Smoothness of h and Δh=0, integrated in polar coordinates, give
\[
 (r^{d-1}M'(r))'=0.
\]
Solving this ordinary differential equation yields M(r)=A+c log(1/r) for d=2, and M(r)=A+c r^(2-d) for d≥3. Because M(r)≥0 for all sufficiently small r, c≥0.

2. Fix an annulus (1/2)<|x|<2 and rescale h_r(x)=h(rx). By a fixed finite Harnack chain on S^(d-1), using the actual local Harnack proposition 3.1.19, there is a dimensional constant C such that
\[
 \sup_{|x|=r}h(x)\le C\,M(r).
\]
The local derivative estimate 3.1.8, on balls of radii comparable to r inside the annulus, likewise yields
\[
 \sup_{|x|=r}|\nabla h(x)|\le C\,M(r)/r.
\]
These constants are uniform in r; **this uniformity is essential**. Consequently h is locally integrable at 0 (integrate its nonnegative spherical mean), and
\[
 r^{d-1}M(r)\longrightarrow0
\]
as r↓0: the expression is O(r log(1/r)) when d=2 and O(r) when d≥3, plus a vanishing O(r^(d-1)) term.

3. The radial flux is constant and *calculable*:
\[
 \int_{\partial B_r}\partial_\nu h\,dS
 =s_{d-1}r^{d-1}M'(r)=-\kappa_d c.
\]
Let η be an arbitrary compactly supported smooth real test function on B_(r_0). Green's identity on B_(r_0)\B̄_r, with zero outer-boundary contribution, gives
\[
 \int_{|x|>r}h\,\Delta\eta\,dx
 =\int_{\partial B_r}(-h\,\partial_r\eta+\eta\,\partial_r h)\,dS.
\]
The first term tends to zero since its absolute value is at most O(r^(d-1)M(r)). For the second, replacing η(x) by η(0) introduces an error bounded by
\[
 O(r)\,s_{d-1}r^{d-1}\sup_{\partial B_r}|\nabla h|
 =O(r^{d-1}M(r))\to0.
\]
Thus the limit equals \(-\kappa_d c\,\eta(0)\). This proves, without assuming anything about a boundary value of h at 0,
\[
 \langle\Delta h,\eta\rangle=-\kappa_d c\,\eta(0).
\]
The same direct computation for Φ proves \(\Delta\Phi=-\kappa_d\delta_0\); therefore \(\Delta(h-c\Phi)=0\) distributionally.

4. Weyl's lemma 3.1.11 gives a smooth harmonic representative v of h-cΦ on the entire ball. Since both v and h-cΦ are continuous away from 0, equality a.e. there improves to equality at every punctured point, obtaining the exact decomposition in the printed Lemma 3.3.16. Taking spherical means and the already computed flux proves uniqueness of c and all formulas above. If c>0 then cΦ diverges to +∞ uniformly in angle while v stays bounded, so h cannot have a finite limit along *any* approach to the puncture.

## Hypotheses, checks, and status

The nonnegativity or an available one-sided lower bound is crucial for the uniform annular Harnack estimate. If it is dropped, e.g. \(h(x)=x_1/|x|^d\) for d≥2 (the directional derivative of a fundamental potential, up to a scalar), h is harmonic on the punctured ball, changes sign, and has a higher-order singularity; it is not of the form cΦ+v. For d=2 the model x_1/|x|² likewise works. The assumption d≥2 is implicit in the printed choice of fundamental kernels and is made explicit in this audit.

This is a **verified conditional deduction** (the condition being the locally established Harnack/interior-estimate/Weyl inputs), not a newly discovered false statement, not a missing-proof finding, and not a transitive certification of any earlier PDE theorem. Its additional conclusion is the exact atomic Laplacian and flux coefficient; the decomposition itself is already correctly printed. No excluded Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion material was opened.

## Proposed action and affected dependents

Optionally add the normalized flux/Dirac-mass formulas as a corollary immediately after Lemma 3.3.16 and retain the existing valid Riesz-based proof and all historical attribution. This is a proposed reading-edition addition, **not** a direct production-source change. The numerical constant may be useful to compare the conventions of §3.4 (Riesz measures) and §4.5 (Martin kernels), but those propositions and their dependencies were **not** reviewed here. No tests, build, CI, formal verification, or website operation was performed.
