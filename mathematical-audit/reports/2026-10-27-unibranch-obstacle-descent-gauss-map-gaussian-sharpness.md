# 2026-10-27 — Unibranch obstacle descent, convex Gauss maps, and sharp complete-Hermitian dual energy

**Pinned integrated reading-edition main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `cf7cc8c49f2fd2b51bd085ae89429a9db2ad2684`. **Scope:** first *selected* mathematical/proof inspection of §§9.10, 9.16, 9.53 and 11.49. No complete-section or upstream theorem-chain certification. Original source text was not needed: the indicated current integrated reading-edition passages and exact displayed proofs were read. No Demailly approximation/regularization, nor its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion programme, was reopened. Historical records of those subjects stay **deferred-by-user**, not resolved.

## POME-UNIBRANCH-CONTINUOUS-OBSTACLE-DESCENT-001

**Status:** verified conditional deduction. **Severity:** low; this is a precise application, not a false printed theorem.

**Anchors and inputs:** `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html`, main blob `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`. Theorem 9.10.5, source `sgpt`, internal label `sgpt-... ` (use the stable tag below rather than guessing the missing source ID), permanent tag `E707851D5DBA`, lines 39–64; quoted disk criterion Theorem 9.10.13, source label `sgpt-59A3C1AA`, permanent tag `48473380B913`, lines 126–139; Theorem 9.10.14, source `sgpt-EEFC0C9A`, permanent tag `C69D2F0ABA4F`, lines 140–214; Corollary 9.10.16, source `sgpt-D36D019A`, permanent tag `2DA8FD7B7A99`, lines 216–249. Corollary 9.10.16, and standard existence of a continuous-obstacle psh envelope on a smooth compact Kähler manifold, are *explicit conditional inputs*. Existing `POME-UNI-EXT-FN-001` (Fornæss–Narasimhan disk-test converse) remains an **unresolved external dependency**; neither its proof nor any user-excluded approximation argument is treated as established by this report.

**Precise deduction.** Suppose (pi:Y	o X) is a proper bimeromorphic morphism, (Y) a smooth compact Kähler manifold and (X) a connected compact **unibranch** Kähler space. Let (	heta) be a smooth closed real ((1,1))-form on (X), assume (mathrm{PSH}(X,	heta)
earnothing), and let (fin C^0(X,mathbb R)). Let (P_	heta(f)) and (P_{pi^*	heta}(fcircpi)) denote the *largest* psh minorants of their respective continuous obstacles. Then
[
 oxed{pi^*P_	heta(f)=P_{pi^*	heta}(fcircpi).}
]
In particular the downstairs envelope exists as a (	heta)-psh function; this proof does **not** require unproved commutation of upper-semicontinuous regularization with the quotient map.

**Proof.** Since (mathrm{PSH}(X,	heta)
earnothing), the upstairs admissible family is nonempty: a downstairs (	heta)-psh candidate may be lowered by a constant to lie under (f), and its pullback is admissible under (fcircpi). Because (fcircpi) is continuous, the standard upper-regularized supremum (w=P_{pi^*	heta}(fcircpi)) is itself (pi^*	heta)-psh and remains pointwise (le fcircpi): local upper regularization cannot exceed a continuous majorant. By Corollary 9.10.16, the psh function (w) is the pullback of a unique (vinmathrm{PSH}(X,	heta)). Surjectivity of (pi) and (wle fcircpi) imply (vle f). For any (uinmathrm{PSH}(X,	heta)) with (ule f), (pi^*ule w=pi^*v), whence (ule v) by surjectivity. Thus (v) is the largest minorant on (X), proving the formula. This is an order argument for an arbitrary (even uncountable) family; it neither assumes sequential compactness nor interchanges limiting operations.

**Disposition/dependents.** Optional continuous-obstacle birational functoriality lemma near §9.10.16 or the envelope definitions in §16. The preservation of the obstacle's continuity and the exact unibranch/proper hypotheses are essential to the derivation. This is *not* an audit or repair of excluded approximation inputs, nor a certification of all pluripotential operations on singular spaces.

## POME-STRICT-CONVEX-GAUSS-DIFFEO-001

**Status:** verified conditional deduction. **Severity:** low; strengthens the printed extreme-point conclusion, which remains correct.

**Anchors:** `docs/sections/local-convexity-and-defining-functions/index.html`, main blob `55354bba1d289fc34e69e2c9746bb3cbe9b2d059`, source `klimek-pluripotential-theory`; Proposition 9.16.1, label `klimek-pluripotential-theory-BAA922F2`, permanent tag `3269D913190D`, physical lines 8–28; Proposition 9.16.2, label `klimek-pluripotential-theory-C7D4500D`, tag `2822D619E8BC`, lines 30–48. The cap construction in Proposition 9.16.3, label `klimek-pluripotential-theory-1E9F70D8`, tag `623CAE0176D7`, lines 50–94, was separately checked at the stated (C^2) cutoff/Hessian and sign-preservation steps; it gives no new defect or third convexity finding.

**Precise deduction and proof.** Under *all* hypotheses of Proposition 9.16.2, with real dimension (mge2), not only is (Dsubsetmathbb R^m) convex with all boundary points extreme, but **every boundary point is exposed**, and the outward Gauss map
[
 
u:partial Dlongrightarrow S^{m-1},
 qquad 
u(p)=rac{
abla q(p)}{|
abla q(p)|}
]
is a **(C^1) diffeomorphism**. Convexity gives the supporting hyperplane (H_p={x:
u(p)cdot(x-p)=0}) at (p). If another (rinoverline Dcap H_p), the entire segment ([p,r]) lies in the supporting hyperplane and (overline D), hence in (partial D); this contradicts the proven extreme-point conclusion. Thus the hyperplane exposes (p) uniquely, showing injectivity of (
u). Given (ein S^{m-1}), maximize (ecdot x) over compact (overline D); a maximizing boundary point has outward normal (e), proving surjectivity. On (T_ppartial D=
u(p)^perp),
[
 D
u_p(w)=rac{(I-
u(p)otimes
u(p))D^2q(p)w}{|
abla q(p)|},
 quad
 langle D
u_p(w),wangle
 =rac{D^2q(p)[w,w]}{|
abla q(p)|}>0
 quad (w
e0).
]
Hence the differential on the ((m-1))-dimensional tangent space is an isomorphism. The inverse function theorem and the global bijection make (
u) a (C^1) diffeomorphism. Nothing here invokes complex Hessian regularization; it is an elementary convex-geometric strengthening.

**Disposition/dependents.** Optional consequence after Proposition 9.16.2, potentially useful in boundary convexification and support-function arguments. It does not claim a (C^2) inverse Gauss map from merely (C^2) boundary data.

## POME-COMPLETE-HERM-GAUSSIAN-SHARPNESS-001

**Status:** verified conditional deduction. **Severity:** low; certifies optimality of an existing coefficient in an explicit admissible example, *not* the entire analytic solvability proof.

**Anchors:** `docs/sections/complete-hermitian-laplacians-and-dual-energy/index.html`, main blob `5bf728a2fa3b558bf7d922d30ea25a449c70b68b`, source `demailly-complex-geometry`, Corollary 11.49.2 label `demailly-complex-geometry-456C31C4`, tag `28AC2C7FBC2B`, lines 8–23; Theorem 11.49.3 label `demailly-complex-geometry-C84B45BB`, tag `D6CB928B58CE`, hypotheses lines 25–46 and energy/graph-domain proof lines 48–69. The printed Bochner–Kodaira–Nakano identity `11.48.19` and its graph-core closure premise remain *conditional inputs*. This audit checks the next exact model and the algebraic energy consequence, **not** the excluded Demailly-approximation L² proof-completion chain.

**Exact sharp model.** Take (X=mathbb C), (omega=i,dzwedge dar z) (complete flat Kähler metric), (E=X	imesmathbb C) with its standard holomorphic frame (e) and smooth metric (|e|_h^2=e^{-lambda |z|^2}) for (lambda>0). Here (iTheta(E)=lambdaomega), the torsion operator is zero, and on (E)-valued ((0,1))-forms (A=[iTheta(E),Lambda_omega]=lambda I). For (g=dar zotimes e), (arpartial g=0) and (u=ar z,e) solves (arpartial u=g). With (dV_omega=omega=2,dx,dy) and (|dar z|_omega^2=1),
[
 |g|_2^2=4piint_0^infty r e^{-lambda r^2},dr
       =rac{2pi}{lambda},qquad
 |u|_2^2=4piint_0^infty r^3 e^{-lambda r^2},dr
       =rac{2pi}{lambda^2}
       =int_mathbb C|g|_{A^{-1}}^2,dV_omega.
]
Moreover (u) is the **minimum-norm solution**, not merely a solution attaining the upper bound: if (F) is any entire holomorphic function in the same weighted (L^2) space, the angular average of (ar z,overline{F(z)}) vanishes at every fixed radius (the power series of (overline F) contains only nonpositive Fourier modes). Cauchy–Schwarz makes its full weighted integral absolutely convergent. Hence (uperpkerarpartial), and every other solution is (u+F), so the bound is an equality for the minimizer. Thus the universal coefficient (1) in Theorem 11.49.3 cannot be reduced, even for flat complete Kähler base and a smooth *strictly* positive line-bundle metric.

**Related conditional spectral consequence.** If, on some fixed ((p,q)) degree with (qge1), the theorem's exact endomorphism satisfies (A(x)gelambda_0 I) for a uniform constant (lambda_0>0), the displayed energy inequality and joint graph core yield
[
 |arpartial v|_2^2+|arpartial^*v|_2^2
 gelambda_0|v|_2^2
]
for each (v) in the full joint graph domain. Thus the nonnegative selfadjoint Laplacian associated with this closed quadratic form has spectrum in ([lambda_0,infty)). The printed solution estimate gives (|u_{min}|_2lelambda_0^{-1/2}|g|_2) for closed (g), and the (unreduced) (L^2) cohomology in that degree vanishes. The Gaussian example above saturates this factor in degree ((0,1)). This invokes only the stated integrated energy theorem conditionally; no theorem-chain certification or excluded completion work is claimed.

**Disposition/dependents.** Optional sharpness example and spectral-gap corollary after Theorem 11.49.3. Do not strengthen to a positive uniform spectral gap when only (A(x)gelambda(x)I>0) with (inflambda=0).

## Separate selected proof inspection without a new defect: §9.53

**Anchor:** `docs/sections/formal-integrability-and-smooth-complex-coordinates/index.html`, main blob `218b71104a05350a9bb37b63c64638efecbd1e42`, source `demailly-complex-geometry`; Proposition 9.53.2 label `demailly-complex-geometry-EF13FDD7`, permanent tag `7D9D38C5DA0E`, lines 10–42; Lemma 9.53.5 label `demailly-complex-geometry-... ` (refer to stable tag `30126C7FDE2C`), lines 45–76; Lemma 9.53.7 tag `53F867AC87E1`, lines 80–107. We *specifically* checked tensoriality under ([fX,gY]), the (-artheta') sign detected on ((0,1))-forms, and the polynomial (arpartial)-homotopy step (partial_{ar z_k}Q_j=P_{jk}). The corrected coordinates have (d''(z_j-Q_j)=O(|z|^{s+1})) because the residual (partial_{z_k}Q_j,d''z_k) is (O(|z|^{2s})) and (2sge s+1). The separate Levi estimate of Lemma 9.53.7 is controlled by (O(r^{s-2})), uniform in (epsilon), for (sge3). These are limited checks, **not** a complete verification of the local/global analytic (L^2) route to Newlander–Nirenberg (Theorem 9.53.13), which was not re-proved or certified.

## Coverage, historic statuses, and writing boundary

The four previously inventory-only ToC rows **§§9.10, 9.16, 9.53 and 11.49** are upgraded only to the *specific* theorem/proof passage scopes above; the other **743** rows retain their prior classifications. There remain **747 unique ToC section identifiers**, and **zero entire sections** certified by this pass. Three low-severity **verified conditional deductions** were added; no newly false printed theorem and no new mathematical duplicate were established. Fornæss–Narasimhan's disk criterion remains open as prior `POME-UNI-EXT-FN-001`; other prior unresolved/resolved/deferred matters are unchanged. All historical dedicated Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss entries retain **deferred-by-user**. No source/body/registry/tag/main edits, builds, GitHub Actions, tests, formal verification or website publishing are claimed.
