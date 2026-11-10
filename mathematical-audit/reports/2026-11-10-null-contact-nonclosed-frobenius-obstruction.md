# A smooth positive constant-rank null distribution without integral leaves

**Finding ID:** `POME-NULL-CONTACT-NONCLOSED-FROBENIUS-001`  
**Review date:** 2026-11-10  
**Severity / status:** low / **verified conditional deduction** (sharpness of a printed hypothesis; **no original theorem is refuted**).  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Review branch starting HEAD:** to be recorded by the Git history of this report.

## Exact reading-edition anchors and assumptions

- `docs/sections/integral-leaves-of-constant-rank-null-distributions/index.html`, blob `564667ab5d008b0ffa1d29f5b7ecc578c19d2f04`; Theorem **7.15.3**, source `klimek-pluripotential-theory:FB2152E8`, permanent tag `8FE75D79B9CA`, physical lines **51–79**. Its hypotheses require (i) a constant-dimensional *common real* nullspace and (ii) `d alpha_j(X,Y,Z)=0` whenever (X,Y) are tangent to that nullspace. For closed forms the second condition is automatic.
- Same file: Proposition **7.15.4**, source `klimek-pluripotential-theory:3B18B0CF`, permanent tag `992E9692EF3B`, physical lines **84–107**. With reducible (alpha), real semipositive (eta), and the three exterior-power conditions, it computes a constant complex null dimension (n-p-q), and only *conditionally* invokes Theorem 7.15.3 when the exterior-derivative condition also holds.
- Structural proof context (read, not globally recertified): Frobenius Proposition **7.15.1**, `klimek-pluripotential-theory:8305DF08` / `0E3D24D5541E`, physical lines **11–34**; complex immersed-leaf Proposition **7.15.2**, `klimek-pluripotential-theory:D96E34E4` / `C2EBFD69CEA4`, lines **39–46**.
- Printed Example **7.15.5**, `klimek-pluripotential-theory:D21B8572` / `849194DD5398`, lines **115–120**, drops (eta)'s semipositivity. Our model instead **keeps both forms semipositive and reducible** but drops exactly the differential nullspace condition; these are different sharpness issues.

## Explicit model and full check

Work on (Omega=mathbb C^4) with standard coordinates (z_1,z_2,z_3,z_4), and put
[
	heta=dz_3-z_1,dz_2,qquad
alpha=rac{i}{2}	hetawedgeoverline	heta,qquad
eta=rac{i}{2}dz_4wedge doverline z_4.
]
These are smooth **real, semipositive** ((1,1))-forms: their coefficient matrices are Hermitian positive semidefinite of rank exactly one, hence reducible (their kernels agree with those of their adjoints). Neither (	heta) nor (dz_4) vanishes, and they are complex-linearly independent at every point, since the (dz_3)-coefficient of (	heta) is one and (	heta) has no (dz_4)-component.

Take (p=q=1). Directly,
[
alphawedgeeta
=-rac14	hetawedgeoverline	hetawedge dz_4wedge doverline z_4
e0,quad
alpha^2=0,quad alphawedgeeta^2=0.
]
Thus **every algebraic premise** of Proposition 7.15.4 holds at every point; the predicted common complex null dimension is (4-1-1=2), and this *dimension conclusion is correct*. Since both forms are semipositive, the common real nullspace is the real underlying distribution of
[
D^{1,0}=ker	hetacapker dz_4
=operatorname{span}_{mathbb C}left{
 X=partial_{z_1}, Y=partial_{z_2}+z_1partial_{z_3}ight}.
]
Both fields are globally holomorphic and tangent to the null distribution. Yet
[
[X,Y]=partial_{z_3},qquad 	heta([X,Y])=1,
]
so the distribution is **not involutive at any point**. In particular, there is no immersed complex surface with tangent spaces equal to (D^{1,0}) on any nonempty open set. This can also be seen without appealing to Frobenius: on a hypothetical holomorphic integral surface (S), (	heta|_S=0) would imply (d	heta|_S=0), whereas
[
 d	heta=-dz_1wedge dz_2,qquad d	heta(X,Y)=-1.
]

The missing condition is quantitatively witnessed by (alpha). Setting (Z=partial_{z_3}), the complex-linear extension of exterior differentiation gives
[
 dalpha(X,Y,overline Z)
=rac{i}{2}d	heta(X,Y)overline	heta(overline Z)
=-rac{i}{2}
e0,
]
while (deta=0). The nonzero complex evaluation guarantees that the real-vector version of Theorem 7.15.3's hypothesis fails. We have therefore isolated **exactly** the differential hypothesis omitted in the invalid strengthening; constant rank, smoothness, positivity, reducibility and exterior-power vanishing do not supply it.

For the smaller one-form-only version, take (mathbb C^3), the same (	heta) and (alpha), and (eta=0,p=1,q=0). The failure already occurs for a single rank-one semipositive form. The nondegenerate (mathbb C^4) model above additionally rules out an objection that the (q=0) endpoint is responsible.

## Classification, proposed text, dependencies, and audit boundary

**Original Theorem 7.15.3 is correct under its printed derivative hypothesis.** Proposition 7.15.4 correctly states only the constant-null-dimension conclusion and expressly conditions the foliation conclusion on the preceding theorem's derivative hypothesis. This finding is **not a confirmed error** and is not a replacement proof for the entire Frobenius theorem. The new result is a concrete *counterexample to dropping a hypothesis*, with a complete local algebraic and differential verification.

Suggested *proposed*, **not applied**, addition after Example 7.15.5: mention the positive rank-one contact form above to show that the exterior-derivative nullspace hypothesis of Theorem 7.15.3 is independent of the algebraic wedge/rank criterion in Proposition 7.15.4. In particular, no downstream argument may infer foliation solely from a semipositive constant-rank but **nonclosed** form. Conversely, when a form is (dd^c u), closedness automatically removes this obstruction, so the printed constant-rank PSH corollary at line 111 is unaffected.

**Affected dependents:** the conditional implication Proposition 7.15.4 (Rightarrow) Theorem 7.15.3, and any future use of a constant-rank semipositive null distribution lacking `d alpha|_{D,D,T}=0`. Theorem 7.15.3's proof at lines 61–79 is used only to verify how the counterexample violates its stated hypothesis; its general analytic dependencies are not certified here.

**Exact coverage:** new explicit nonclosed-form sharpness audit of §7.15.3–5 plus the Frobenius and complex-immersion statements as dependency context. §7.15 was already proof-level sampled in prior checkpoints, so **0 newly first-visited numbered sections**, **0 fully mathematically certified sections**. Current ToC baseline is **25 chapters / 747 numbered sections**. This is not a rerun of `POME-NULL-ALPHA-REDUCIBILITY-001` (that finding drops reducibility while keeping a closed form), nor of `POME-BT-LEVI-RANKJUMP-NORMALCROSSING-001` (that finding drops constant rank for a closed Levi form).

Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user, neither resolved nor certified**. No mathematical body, provenance/canonicalization, permanent tag, production main, website, tests, build, GitHub Actions or formal verification is changed or claimed.
