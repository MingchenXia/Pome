# 2026-10-28 audit: Newton polyhedra of monomial multiplier ideals and the sharp elliptic relative-embedding power

**Source pinned:** Pome production `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`; audit branch starting HEAD `3c8eab9c71d11875033be6435db7ef5e61bcf4f2`. **Scope:** genuinely new direct model proofs in previously inventory-only §6.12, plus an independent sharpness proof for the previously selected §9.71. No complete section or transitive theorem-chain certification. Neither finding is an error in the printed theorem. All Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion tasks remain **deferred-by-user**, neither reopened nor declared resolved.

## POME-MONOMIAL-NEWTON-MULTIPLIER-001

**Severity:** low. **Status:** verified conditional deduction (independent monomial analytic verification of a correct integrated theorem, not a proof of all cases). **Target:** Theorem **6.12.8**, original source `foundations-of-pluripotential-theory:17D7A591`, permanent reader tag `5BA222439952`; strict divisor condition Eq. **6.12.9**, source `foundations-of-pluripotential-theory:DD8A324C`, tag `2874465D0AEF`; sheaf formula Eq. **6.12.10**, source `foundations-of-pluripotential-theory:6DB88FC2`, tag `784A47900871`; Example **6.12.19**, source `foundations-of-pluripotential-theory:C4F4BAF9`, tag `B10A1F1C864B`. Current reading-edition file `docs/sections/lelong-numbers-and-multiplier-ideals--birational-change-of-variables-and-logarithmic-thresholds/index.html`, blob `5336b9d58df5b21518d7436a7c42d2d7be253340`, physical lines **137–171, 291–294**. Earlier integrability change-of-variables input is at lines 94–126. The named log-resolution is an allowed Hironaka input in the integrated proof, but is **not** needed for the model below.

**Precise statement.** Let (mathfrak a=(z^{a^{(1)}},ldots,z^{a^{(s)}})subsetmathcal O_{mathbb C^n,0}) be a nonzero monomial ideal, with (a^{(j)}inmathbb N^n), (c>0), and
[
phi=clogBig(sum_{j=1}^s |z^{a^{(j)}}|^2Big),qquad
P=operatorname{conv}{a^{(1)},ldots,a^{(s)}}+mathbb R_{ge0}^n.
]
With the project's (mathcal I(phi)={f:|f|^2e^{-phi}in L^1_{m loc}}) convention,
[
oxed{quadmathcal I(phi)_0
 =ig(z^b: binmathbb N^n, b+mathbf1inoperatorname{Int}_{mathbb R^n}(cP)ig).quad}
]
The interior is **ordinary full-dimensional interior**; the inequality on each lower supporting facet is strict. This is a direct Newton-polyhedron model for the genuine discrepancy and floor effects in Theorem 6.12.8, and is not a restatement of its general log-resolution proof.

**Proof without approximation or L² estimates.** Fix a sufficiently small polydisc, put (t_i=-log|z_i|^2) and integrate first over the angles. Up to bounded positive factors, the radial integrand for a monomial (z^b) is
[
exp{-F_b(t)},dt_1cdots dt_n,qquad
F_b(t)=langle b+mathbf1,tangle-cmin_jlangle a^{(j)},tangle,qquad t_igg1.
]
Indeed, (sum_j e^{-langle a^{(j)},tangle}) lies between (e^{-min_jlangle a^{(j)},tangle}) and (s,e^{-min_jlangle a^{(j)},tangle}); the complex polar Jacobian contributes (e^{-sum_i t_i}). The continuous positively homogeneous, piecewise linear (F_b) is bounded below by a positive multiple of (|t|) on the positive cone precisely when
[
langle b+mathbf1,vangle>cmin_jlangle a^{(j)},vangle
quad	ext{for every }vinmathbb R_{ge0}^nsetminus{0}.
]
This is equivalent, by the supporting-halfspace description of (P), to (b+mathbf1inoperatorname{Int}(cP)). If strict positivity fails on a ray, the integral diverges: for a negative value it grows exponentially along a narrow cone; for a zero value a fixed-width infinite cylinder near that ray has (F_b) uniformly bounded above (piecewise linearity gives a uniform Lipschitz constant). Such a cylinder lies inside the translated positive cone after choosing a fixed positive offset, so it has infinite volume. Thus monomial membership is **if and only if**, including the boundary case.

For a general holomorphic germ (f=sum_b c_bz^b), angular orthogonality and Tonelli give the integral as a sum of nonnegative monomial radial integrals weighted by (|c_b|^2). Necessity excludes every forbidden exponent with (c_b
eq0). Conversely the set of allowed exponents is upward closed and has finitely many minimal generators (Dickson's lemma), so an analytic germ supported entirely on allowed exponents belongs to the finitely generated corresponding monomial ideal: regroup its absolutely convergent power series according to an allowed monomial divisor, on a smaller polydisc. The ideal's finitely many generators already have locally integrable weighted squared norms, and their holomorphic coefficients are locally bounded. This proves sufficiency and the boxed ideal identity.

**Endpoint check.** For (mathfrak a=(x^2,y^3)), (P={(u,v)inmathbb R_{ge0}^2:u/2+v/3ge1}), so
[
x^py^qinmathcal I(clog(|x|^4+|y|^6))_0
iff rac{p+1}{2}+rac{q+1}{3}>c.
]
The constant is integrable exactly when (c<5/6). Thus (operatorname{lct}(mathfrak a)=5/6), with **failure at equality**; at (c=5/6) and (c=1), (mathcal I(phi)=(x,y)). This independently checks the strict (>) sign and the (+1) discrepancy shift in the printed result. Do not conflate these ideal orders with the ordinary generic Lelong number or with a dedicated Demailly approximation.

**Dependents and proposed action:** use this exact monomial endpoint as an optional, self-contained model in §§6.12, 6.54 and 16.6 where analytic singularities and multiplier ideal jumps are compared; retain all pre-existing source and permanent tags. **No correction** of the printed Theorem 6.12.8 is indicated. The full general integrability-resolution chain is not certified by this model.

## POME-RELATIVE-ELLIPTIC-POWER-OPTIMAL-001

**Severity:** low. **Status:** verified conditional deduction (sharp model, printed Lemma 9.71.1 correct). **Target:** Lemma **9.71.1**, original source `cao-paun-foliations:4BE67CB0`, permanent tag `A53CEC220C70`; `docs/sections/local-projectivity-from-relative-positivity/index.html`, blob `f17614b598855bda6fc15f266135d6fe238638cf`, physical **lines 8–11, 17–36**. The printed proof invokes Kodaira and Grauert base change (line 24), and an upstream vanishing theorem (line 18); their proof chains are **not** certified here. Internal curve Riemann–Roch is Theorem **10.78.9**, tag `7F8CC797059F`, `docs/sections/compact-curves-periods-and-complex-tori--divisors-and-riemann-roch-on-a-compact-curve/index.html`, blob `58c04d3cf4408fcdb140162e03a9052d3620610a`, physical lines **133–145**.

**Precise sharpness assertion.** Let (E) be a complex elliptic curve, (L) a holomorphic line bundle of degree one with smooth positive curvature, (M=E	imesDelta), (p=operatorname{pr}_Delta), and (A=operatorname{pr}_E^*L). The hypotheses of Lemma 9.71.1 hold on every fiber. The **minimum possible tensor power** in its relative embedding conclusion is (k=3). Thus replacing the printed existential (k>0) by (k=1) or even (kle2) is false, without any degeneration of the family or positivity.

**Proof.** On an elliptic curve (K_Esimeqmathcal O_E). For (kge1), Riemann–Roch and the absence of sections of negative-degree line bundles give (h^0(E,L^k)=k), (h^1(E,L^k)=0). A morphism (E	omathbb P^N) satisfying (G^*mathcal O(1)=L^k) is defined by a basepoint-free linear subsystem of (H^0(E,L^k)); its image is contained in a projective linear subspace of dimension at most (k-1). For (k=1) the map is constant (indeed the unique degree-one section has a zero); for (k=2) its image lies in (mathbb P^1), and a compact genus-one curve cannot embed in (mathbb P^1). For (k=3), Riemann–Roch gives, for distinct (x,yin E), (h^0(L^3)=3, h^0(L^3(-x))=2, h^0(L^3(-x-y))=1, h^0(L^3(-2x))=1). These dimension drops show basepoint-freeness, separation of distinct points, and separation of tangent directions. Hence the complete linear system of (L^3) gives an embedding (Ehookrightarrowmathbb P^2). Taking its product with (operatorname{id}_Delta) is the desired closed relative embedding, and pulls back (mathcal O_{mathbb P^2}(1)) to (A^3).

**Dependents and proposed action:** optional sharpness remark at §9.71.1, clarifying why a sufficiently high power is necessary even in a trivial smooth family. The existing Grauert base-change and Kodaira arguments remain distinct prerequisites; no claim of having proved the lemma in arbitrary families, and no body, source, or permanent-tag edit.

## Coverage, invariants, and deferred scope

- **New selected proof-level coverage:** §6.12, specifically Theorem 6.12.8, Eqs. 6.12.9–10, and Example 6.12.19, via a complete independent monomial model, not the whole section. The earlier §6.12.4 change-of-variables statement was read only for normalization.
- **Incremental coverage in an already reviewed section:** §9.71.1, positive elliptic-fiber model and exact minimum power; §10.78.9 is an explicitly named internal Riemann–Roch input, **not** newly certified here.
- **Context-only:** current §7.1 introductory Bedford–Taylor definition/normalization (physical lines 7–13, blob `41bc964bad8bf8505892c2cb3762e5cce2071ae6`), no theorem-level review and no claim of first selected proof coverage.
- The existing **25-chapter / 747-section** actual table-of-contents matrix is preserved; **zero** complete sections or chapters certified. No other prior finding, repair, contradiction, circularity or external-input status is changed.
- All user-excluded Demailly approximation/regularization plus dedicated Bergman/L²/OT/multiscale-atlas/positivity-loss programme remains **deferred-by-user**, not reopened or resolved. The printed §9.71 relative vanishing input is explicitly **deferred**, and Grauert base change remains a quoted external dependency. Historical attribution must be retained.
- No mathematical source/body/canonicalization/registry/tag/published website edits; no build, CI, automated deployment, software tests, or formal verification conducted.
