# Exact toric rooftop energy as an L1 distance of Legendre duals

**Date:** 2026-11-01. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Stable finding ID:** POME-TORIC-ROOFTOP-DUAL-L1-001. **Severity/status:** low / **verified conditional deduction**. This is neither a newly false Pome theorem nor a repair of a printed proof. No source, production, tag or canonicalization edit is applied.

## Precise integrated mathematical sources

All source passages below are in the **actual main reading edition**, not merely an underlying book copy.

- File: docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html; main blob SHA 56a1a55dfc8185aee0e6d495a6a93d8a2313d76b.
- Theorem **21.12.13**, source **sgpt:E09727EF**, permanent **8B5B73657BF7**, physical HTML lines 238–282: torus-invariant omega-psh potentials and convex Legendre duals.
- Proposition **21.12.20**, source **sgpt:83878EA6**, permanent **D60ADA8CEE9B**, physical lines 375–388: shifts send F to F+C and G to G-C.
- Proposition **21.12.21**, source **sgpt:E2F47062**, permanent **419A1D9F18A9**, physical lines **390–415**, especially the proof at 397–413: for nontrivial rooftop u, its dual is the convex maximum G_u = G_phi vee G_psi. (The operator vee is the *pointwise supremum* of convex functions, not the infimal convex envelope.)
- Proposition **21.12.39**, source **sgpt:B3280F36**, permanent **75730375E037**, physical lines **893–984**, in particular equation **21.12.40**, source **sgpt:4A4855E9**, permanent **F02AE1451B98**, physical lines **895–898**: E_omega(phi) = n! integral_P (G_0-G_phi) dm. Its proof checks the convex first variation at lines 920–959, followed by the decreasing truncation passage at 961–981.
- File: docs/sections/convex-functions-and-convex-bodies/index.html; main blob SHA 2a123a863642a5a75caa173f0f73aff439a02ea4. Definitions **21.11.10**, source **sgpt:05FE0DDE**, permanent **6561D15F1216**, physical lines 80–89, and **21.11.11**, source **sgpt:59330ADD**, permanent **4D25259F16EC**, lines 89–98, distinguish convex meet from pointwise convex join.

## New theorem (deduced from the identified internal results)

Let X be a compact smooth polarized toric n-fold, L ample, P its full-dimensional moment polytope with covolume-one lattice Lebesgue measure, omega the reference torus-invariant positive curvature form, and phi, psi **bounded torus-invariant omega-psh potentials**. The connected compact toric setup and reference choices are those of §21.12. Set u=P_omega(phi,psi), the upper-regularized omega-psh rooftop. Define the **rooftop-energy functional**

\[
D_\omega(\phi,\psi):=E_\omega(\phi)+E_\omega(\psi)-2E_\omega(u).
\]

Writing G_phi, G_psi for the closed convex Legendre duals on P, one has the **exact formula**

\[
\boxed{D_\omega(\phi,\psi)=n!\int_P |G_\phi-G_\psi|\,dm.}
\]

Consequently D_omega is a genuine metric on the bounded torus-invariant omega-psh potentials (without quotienting by additive constants). If G_t=(1-t)G_phi+tG_psi, 0<=t<=1, the biconjugate F_t=G_t^* determines another bounded toric potential phi_t, and

\[
D_\omega(\phi_s,\phi_t)=|s-t|D_\omega(\phi,\psi),
\qquad
E_\omega(\phi_t)=(1-t)E_\omega(\phi)+tE_\omega(\psi).
\]

This is a metric-geodesic assertion for the explicitly defined rooftop functional; **it does not independently identify phi_t with the weak Mabuchi/complex homogeneous Monge–Ampère geodesic**, whose PDE requires separate checking.

Finally, with V=int_X omega^n=n!vol(P),

\[
0\le D_\omega(\phi,\psi)\le V\,\|\phi-\psi\|_{L^\infty(X)}.
\]

The coefficient V is optimal: replacing psi by psi+c gives equality for any nonzero real constant c. No regularization theorem, L2 estimate, Bergman construction, or external analytic input is used in this deduction.

## Complete deduction and qualifications

**Nontrivial bounded rooftop.** Since phi,psi are bounded, there exists a common constant -A below both. The constant -A is omega-psh, hence a rooftop competitor, and -A<=u<=min(phi,psi); in particular u is nontrivial and bounded. We may invoke precisely the nontrivial-rooftop clause of 21.12.21, yielding G_u=max(G_phi,G_psi), with max taken pointwise.

**Energy identity.** Apply the printed 21.12.40 to each of phi, psi, u and cancel G_0:

\[
\begin{aligned}
D_\omega(\phi,\psi)
 &=n!\int_P (2G_u-G_\phi-G_\psi)\,dm\\
 &=n!\int_P(2\max(G_\phi,G_\psi)-G_\phi-G_\psi)\,dm\\
 &=n!\int_P|G_\phi-G_\psi|\,dm.
\end{aligned}
\]

There is no factor 1/2 or extraneous binomial coefficient: the measure normalization and n! are exactly those printed after Proposition 21.12.24 (physical lines 466–481) and in Eq. 21.12.40. Boundedness implies |G_phi-G_0| and |G_psi-G_0| are uniformly bounded by the dual order-reversal argument, so these integrals are finite.

**Definiteness.** Positivity, symmetry and the triangle inequality now follow from the ordinary L1 norm. If D=0, G_phi=G_psi almost everywhere on P. The functions are finite closed convex functions on P and are continuous in the interior; thus they agree at every interior point. Closedness and convexity determine their boundary values by limits along segments to an interior point, so they agree throughout P. Biconjugation gives F_phi=F_psi; Theorem 21.12.13 gives phi=psi. This proof does not invoke sequential compactness of a space of potentials.

**Straight dual interpolation.** The convex functions G_phi and G_psi are finite and differ from the reference dual G_0 by bounded amounts on P, and equal +infinity off P. Therefore G_t=(1-t)G_phi+tG_psi is proper lower-semicontinuous convex with the same bounded-reference property, and its biconjugate F_t is within a uniform additive bound of F_0. By 21.12.13 it defines a bounded toric omega-psh phi_t, with endpoints phi,psi. The pointwise linear difference G_t-G_s=(t-s)(G_psi-G_phi) yields the exact constant-speed distance formula; linearity of the energy integral gives the affine energy formula. **No claim is made that this proves the geodesic PDE.**

**Sharp uniform bound.** The toric dense-orbit correspondence gives sup over the dense orbit of |phi-psi| equal to sup_N |F_phi-F_psi|, which is at most the essential supremum on X. Order reversal in Fenchel conjugation gives |G_phi-G_psi|<=sup_N|F_phi-F_psi| pointwise on P. Integrating gives D<=V||phi-psi||_infinity. For phi=psi+c, Proposition 21.12.20 gives G_phi=G_psi-c and the equality D=V|c|. This also shows constants are **not** collapsed by the metric; quotient-by-constants would require a separate definition.

## Scope, dependents, and proposed source change

This run newly checked the integrated proofs of **21.12.21** and **21.12.39** and the compatibility of definitions **21.11.10–11**, Theorem **21.12.13**, Proposition **21.12.20**, and the normalization in **21.12.24**. The key source results are treated as **conditional internal inputs**, not fully recertified upstream theorems; §21.12 had already been sampled in previous sessions. A future review may compare the explicit dual interpolation against the separately constructed weak geodesic in chapter 17. No such identification, unrelated global finite-energy extension, or complete-section certification is claimed here.

**Proposed optional reader corollary** immediately after Proposition 21.12.39: state the bounded-toric dual L1 identity and its sharp comparison, with the constant-speed dual interpolation explicitly qualified as a metric construction. Preserve original source tags, permanent links, distinct stronger/weaker versions, and attribution. Affected mathematical dependents: toric rooftop metric calculations (§21.12), energy comparisons, and any later chapter-17 metric/geodesic comparison. No production changes made.

**Exclusions and prior ledger:** the Demailly approximation/regularization programme, plus its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion lines, remain **deferred-by-user**, not reopened, resolved or certified. All previous confirmed errors, unresolved proof gaps, external dependencies, duplication classifications and conditional results retain their prior status. There is **no** claim that tests, builds, CI, formal verification or website publication ran. Collection size remains **25 chapters, 747 numbered sections, zero fully certified mathematical sections**.
