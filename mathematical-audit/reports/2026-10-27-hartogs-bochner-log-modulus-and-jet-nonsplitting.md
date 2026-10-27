# Mathematical audit — Hartogs–Bochner boundary modulus, jet bundles, and polar curvature
Date: 2026-10-27. Reviewed integrated main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Existing audit branch before this session: b71610cf5edf7ad06ac8f1be1d9ad4d522247c18.

## Scope and evidence

The **current integrated reading edition**, rather than historical theorem-number matches, was checked in three formerly inventory-only sections. The source files, original labels, permanent tags, blobs and physical line anchors are:

1. Section 9.36: docs/sections/boundary-levi-geometry-and-holomorphic-extension--holomorphic-extension-of-tangential-cr-data/index.html, main blob 347aaab0f394502449fd1cc1fdd151bf31c9dfa8; Theorem 9.36.1, source demailly-complex-geometry-569D8499, permanent tag E17A6BD70890, lines 7–49. Hypotheses at line 8; distributional boundary argument lines 14–35; current homotopy and kernel bound lines 36–45; complement connectivity lines 46–48.
2. Supporting, **previously reviewed** section 5.49: docs/sections/complex-homotopy-operators-and-hartogs-extension/index.html, main blob e0aea9511e5f9e427463ae94002b38da8919ac94; Proposition 5.49.1, source klimek-pluripotential-theory-4FD27637, permanent tag 7ACDC1AF162C, lines 16–35; kernel normalization line 10. This is a dependency crosscheck, **not a new section-wide review**.
3. Section 10.93: docs/sections/vector-bundles-and-jets/index.html, main blob 700125246737bba920fbeda2970f50de8a5b4441; Proposition 10.93.1, source demailly-complex-geometry-FFBD8F68, permanent tag 24324B70E319, lines 6–14; Proposition 10.93.3, source demailly-complex-geometry-DD92067B, permanent tag 79E5312B02F1, lines 29–51; Definition 10.93.4, source demailly-complex-geometry-D5957496, permanent tag 1AEDB3FDC003, lines 53–55.
4. Section 5.46: docs/sections/plurisubharmonic-functions-and-singularities--polar-curvature/index.html, main blob 334a5f34230c1da094a6822f30408e669f052b4b; Lemma 5.46.1, source non-kahler-pluripotential-theory-43D9FD13, permanent tag 8F61C8BDD569, lines 10–26; Lemma 5.46.2, source non-kahler-pluripotential-theory-98A2FD1E, tag EB97F93DAD74, lines 28–55; Proposition 5.46.3, source non-kahler-pluripotential-theory-F9AAD931, tag 09F56C9DE42C, lines 57–85; Lemma 5.46.4, source non-kahler-pluripotential-theory-13E3C540, tag 3B857D475432, lines 87–103; Proposition 5.46.5, source non-kahler-pluripotential-theory-FD27352E, tag 5AAB9E80546A, lines 105–127; Proposition 5.46.7 tag 4A6AA259F9D8, lines 130–171, **statement only** for context, not its chain-rule proof.

These are three selected proof/statement passes, not an assertion that any complete section, all analytic prerequisites, or all 747 catalogued sections are certified. No software build or formal verification was run. The excluded Demailly approximation/regularization programme and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion were not audited, not extended, and stay **deferred-by-user**. A historical attribution to Demailly for distinct classical results is not such an excluded mathematical input.

## POME-CR-BOUNDARY-LOGMODULUS-001

**Severity: low. Status: verified conditional deduction. Theorem 9.36.1 as printed is not false.** Dependents: quantitative Hartogs–Bochner extension at C² boundaries, boundary regularity claims, compact-support Dolbeault homotopy in Section 5.49. Proposed disposition: optional quantitative corollary after Theorem 9.36.1, retaining its connected-boundary hypothesis.

**Statement.** Under precisely Theorem 9.36.1's assumptions, there is a constant C depending on the fixed domain, dimension and an enclosing radius R > 2 diam(closure Omega), but not on f, such that the solution F constructed in its proof satisfies, for all x,y in closure Omega with h=|x-y| and 0<h<R/4,

$$
 |F(x)-F(y)|\leq C\|f\|_{C^1(\partial\Omega)}
 h\bigl(1+\log(R/h)\bigr).
$$

Consequently F belongs to C^{0,alpha}(closure Omega) for **each** alpha in (0,1). This is a modulus estimate, not a claim of uniform Lipschitz regularity and not a claim that the logarithmic factor is sharp for every domain.

**Complete deduction.** A fixed tubular neighborhood of the C² boundary admits a C¹ nearest-point projection with bounded derivative on a smaller collar. A fixed signed-distance cutoff therefore makes the compact C¹ extension f_0 from the printed proof with ||f_0||_{C¹} <= C_Omega ||f||_{C¹(boundary)}. Its compactly supported coefficient form v=1_Omega * dbar(f_0) has ||v||_infinity <= C_Omega||f||_{C¹}, with support in one fixed ball. The printed boundary-CR calculation establishes dbar v=0, and the already internal current homotopy gives u=Kv and dbar u=v. In Section 5.49 the scalar kernel is explicitly

$$
k_j(z)=\frac{(n-1)!}{\pi^n}\frac{\bar z_j}{|z|^{2n}},
\quad |k_j(z)|\leq C_n|z|^{1-2n},
\quad |\nabla_{\mathbb R^{2n}}k_j(z)|\leq C_n|z|^{-2n}\;(z\ne0).
$$

Fix x,y, h=|x-y|. On the union of radius-2h balls about x and y, each kernel convolution contribution to u(x)-u(y) has magnitude at most C||v||_infinity * integral_0^{3h} r^{1-2n}r^{2n-1}dr <= C||v||_infinity h. Outside these balls, the real mean-value theorem on each segment from x-z to y-z bounds |k_j(x-z)-k_j(y-z)| by C h |x-z|^{-2n} after harmless adjustment to the distance threshold. The support of v is in a fixed radius-R ball, and integration over annuli gives

$$
 C\|v\|_\infty h\int_{2h}^{CR}r^{-1}\,dr
 \leq C_{R,n}\|v\|_\infty h(1+\log(R/h)).
$$

If the outer annulus is empty, only the already bounded near contribution remains. Summing finitely many coefficients and adding the Lipschitz function f_0 yields the displayed bound for F=f_0-u. Crucially, the **connected exterior** argument in lines 46–48 and continuity of u make u=0 on the exterior and on its boundary, hence the printed f is indeed F's boundary value. Finally, h^(1-alpha)(1+log(R/h)) is bounded on (0,R/4), proving the Hölder consequence.

**Sharp need for the topological hypothesis (separate counterexample to a would-be strengthening).** Let Omega = {1<|z|<2} in C^n, n>=2. On its two disjoint smooth boundary components prescribe f=1 on the inner sphere, f=0 on the outer sphere. The function f is smooth tangential-CR separately on both. If F were holomorphic in Omega and continuous on closure Omega, then t -> F(t,0,...,0) would be holomorphic on 1<|t|<2. For every 1<r<2 its Laurent constant coefficient equals the circular average of F(re^{i theta},0,...,0), independent of r. This average tends to 1 as r decreases to 1 and to 0 as r increases to 2, contradiction. Thus the printed connectedness is essential; its retention is not a missing hypothesis. No Hartogs theorem is invoked in this counterexample.

The ambient convolution kernel/homotopy identity and C² tubular regularity remain declared upstream inputs: they were crosschecked in the printed passages but not fully independently reconstructed.

## POME-JET-EXACT-NONSPLIT-001

**Severity: low. Status: verified conditional deduction. Proposition 10.93.3 and Definition 10.93.4 remain correct.** Dependents: jet bundles, very ampleness via one-jets and pairs, holomorphic connections, global section evaluation. Proposed disposition: add an elementary exact sequence and a non-splitting example near Proposition 10.93.3.

**Statement.** For a holomorphic vector bundle E of rank r on a complex n-fold, and k>=1, the jet bundles constructed in Proposition 10.93.3 have a natural exact sequence of holomorphic bundles

$$
0\longrightarrow \operatorname{Sym}^k\Omega_X^1\otimes E
\longrightarrow J^kE\longrightarrow J^{k-1}E
\longrightarrow 0.
$$

For k=1 this sequence splits holomorphically if and only if E admits a holomorphic connection.

**Proof.** In any coordinate chart and holomorphic frame, the fiber of J^kE consists of Taylor polynomials through total degree k in z-z(x), as constructed at lines 39–49. The forgetful map deletes all degree-k terms and is surjective. Its kernel is precisely the homogeneous degree-k coefficients of E-valued polynomials; a degree-k homogeneous polynomial transforms under a holomorphic coordinate change by its *linear derivative at the basepoint* and under a frame change by the frame matrix at that point, since every higher term acquires order at least k+1. This is the transition law of Sym^k Omega^1 tensor E. Holomorphic dependence and the cocycle law follow from the same coefficient argument as the printed proposition. For k=1, the holomorphic jet map j¹ is C-linear and satisfies j¹(fs)=f j¹(s)+df tensor s. If sigma:E -> J¹E is a holomorphic right inverse to the forgetful map, define nabla(s)=j¹(s)-sigma(s), valued in Omega¹ tensor E. It satisfies the Leibniz rule and is a holomorphic connection. Conversely a holomorphic connection nabla yields sigma(s)=j¹(s)-nabla(s), an O-linear right inverse. All these are sheaf-local identities and hence global.

**Concrete non-splitting despite jet generation.** For X=P¹ and E=O(1), the global sections of O(1) are the two linear homogeneous polynomials. At every point their map to the complete first jet is injective: a degree-one section vanishing to order >=2 is zero. The source and target fibers both have complex dimension two, so global first-jet evaluation is an isomorphism everywhere and determines a holomorphic bundle isomorphism J¹O(1) = O^2. But the exact sequence reads

$$
0\longrightarrow O(-1)\longrightarrow O^2\longrightarrow O(1)\longrightarrow0.
$$

It cannot split holomorphically, because any splitting O(1)->O² would be a nonzero holomorphic map yet Hom(O(1),O²)=H⁰(P¹,O(-1))²=0. Moreover O(1) separates distinct points and first jets, hence is very ample in the exact sense of Definition 10.93.4; nevertheless it has no holomorphic connection. The original jet theorem asserts no splitting and is not refuted. Projective section identification is the p=0 case of the internally stated Proposition 10.51.5, not an excluded approximation proof.

## POME-POLAR-AFFINE-REWEIGHT-001

**Severity: low. Status: verified conditional deduction. Proposition 5.46.3 remains correct.** Dependents: invariance of polar curvature under bounded perturbations and scalar changes of singularity type. Proposed disposition: optional conditional corollary following Proposition 5.46.3; no analytic regularization input.

**Statement and complete proof.** Let U be a coordinate domain, let u<=0 be plurisubharmonic there and S={u=-infinity}. Let chi:(-infinity,0] -> R be convex and nondecreasing, with chi(t)=c t+O(1) as t->-infinity for one constant c>0. Define chi(u) by its upper-semicontinuous extension at the pole set, so chi(-infinity)=-infinity. Then

$$
\mathbf 1_S\,dd^c(\chi\circ u)=c\,\mathbf 1_S\,dd^c u.
$$

The standard convex-composition line test shows chi(u) is psh (or use local decreasing smooth approximations *only as an established elementary psh composition fact*, without reopening the excluded Demailly programme). As u is locally upper bounded and tends to -infinity only at S, the stipulated bounded affine tail implies chi(u)-cu is locally bounded: on the finite interval between any fixed negative threshold and zero, both functions are bounded, while on the negative tail their difference is O(1). Both have exactly pole set S because c>0. Applying the *already proved* Proposition 5.46.3 to the pair chi(u),cu gives equality of their dd^c coefficient restrictions to S, and dd^c(cu)=c dd^c u. This proof does **not** claim the conclusion if only chi(t)/t->c without a bounded error, or if c=0. Its value is an exact scaling formula for the whole polar current, not merely its Lelong number.

Independent direct checks: Lemma 5.46.1's energy inequality properly bounds local W^{1,2} gradients of a bounded distribution with signed-measure Laplacian; Lemma 5.46.2's logarithmic cutoffs use vanishing Sobolev capacity of compact pole subsets; Proposition 5.46.3's Hahn/Jordan argument compares coefficient measures rather than solely scalar traces; Proposition 5.46.5's proper projection respects Borel coefficient restrictions. These specific proof transitions showed no additional definite false assertion. Proposition 5.46.7's cutoff proof chain was **not** audited.

## Coverage, unresolved premises, and scope controls

**Precisely upgraded from inventory-only:** §5.46.1–5 (selected argument and source checks), §9.36.1 (complete printed proof passage and newly derived modulus with distinct annulus counterexample), §10.93.1/.3–4 (local-free atlas proof and jet-Taylor proof). §5.49.1 was crosschecked as an **already selected** homotopy prerequisite, not counted as new coverage. All three new finding IDs describe **verified conditional deductions**, not false printed statements or independent certification of analytic or sheaf-theoretic prerequisites. Outstanding upstream items: C² collar construction, homotopy distributional identity, elementary psh convex composition, and projective H⁰(O(d)) identification; no new external black-box input is asserted resolved. No existing unresolved or resolved statuses were changed. The 747-row current table-of-contents inventory remains, with **zero complete-section certifications**. The Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme and its historical records remain **deferred-by-user**, neither reopened nor certified. No main/source/body/registry/tag/CI/build/formalization/published-site changes.
