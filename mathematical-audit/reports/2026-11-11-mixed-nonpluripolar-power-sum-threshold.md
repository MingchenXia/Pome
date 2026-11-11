# Exact mixed non-pluripolar mass threshold for two distinct zero-Lelong power-logarithmic potentials

**11 November 2026. Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Stable finding:** `POME-NPP-MIXED-POWER-SUM-THRESHOLD-001` — **low / verified conditional deduction**. The original Lemma 13.2.2, Proposition 13.2.6, and Example 13.2.9 are **not refuted**. This extends the already recorded **2026-10-30 single-potential square threshold** `POME-NPP-POWER-SINGULARITY-THRESHOLD-001` to genuinely **mixed, unequal parameters**, and does not re-register the diagonal case as a new finding.

## Precise current integrated sources

- `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, main blob **`81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`**.
- Lemma **13.2.2**, source `foundations-of-pluripotential-theory:CE1D6DA5`, permanent **`D59675D9F6D8`**, physical lines **34–52**, especially local-finiteness trace criterion Eq. **13.2.3**, source `:F86748C9`, permanent **`E88E33ACAD5B`**, lines **36–40**.
- Proposition **13.2.6**, source `foundations-of-pluripotential-theory:E82F0D73`, permanent **`7F7123F92478`**, lines **80–125**, especially positivity, plurifine locality and mixed multilinearity.
- Example **13.2.9**, source `foundations-of-pluripotential-theory:2F8E45A2`, permanent **`6F4C920FEDCA`**, lines **151–165**, with the square-root endpoint.
- The smooth determinant convention is Eq. **7.2.4**, permanent **`706A589A680C`**, in `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html` (previously pinned blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`); the normalization is `dd^c = (i/2π)∂∂bar`. The §13.3 closedness theorem is an **upstream dependency**, not independently certified here.

## Claim, hypotheses and sharp threshold

Fix two **independent** real numbers `0 < a,b < 1` and a number `0<c<min(1-a,1-b)`. Let
[
U_{a,b,c}={(x,y)inmathbb C^2: |x|^2<c, |y|<e^{-1}},quad L=-log|y|.
]
Define on `y≠0`, and extend by `-∞` on `y=0`,
[
u_a=(|x|^2-1)L^a,qquad u_b=(|x|^2-1)L^b .
]
Both functions are plurisubharmonic. Each has **zero Lelong number** on the axis `y=0`. Nevertheless, the **mixed** non-pluripolar product
[
langle dd^cu_awedge dd^cu_bangle
]
is locally finite on `U_{a,b,c}` **if and only if `a+b<1`**. In particular, the mixed product can be locally finite even when **one of the two self-products is not locally finite**. No condition involving only the Lelong numbers can detect this threshold.

More precisely, put `r=|x|²` and
[
A=a(1-a)+b(1-b),qquad B_{a,b}(r)=A(1-r)-2ab,r.
]
On `y≠0`, and extended by zero on the polar axis, the mixed cutoff-limit Borel measure is
[
oxed{quad dmu_{a,b}=rac{B_{a,b}(|x|^2)}{4pi^2|y|^2L^{,2-a-b}},dA(x)dA(y).quad}
]
For `a+b<1`, any `0<R²<c` and `T>1` with `e^{-T}<e^{-1}` give the **exact compact-cylinder mass**
[
oxed{quad
mu_{a,b}{,|x|le R, |y|le e^{-T},}
=rac{A R^2-rac12(A+2ab)R^4}{2(1-a-b)},T^{a+b-1}.quad}
]
When `a+b=1`, the mass of the annular truncation `e^{-S}le|y|le e^{-T}` grows as a **positive constant times `log(S/T)`**; for `a+b>1`, it grows as a positive constant times `(S^{a+b-1}-T^{a+b-1})/(a+b-1)`. Hence the threshold is **strict**.

## Complete calculation

On `y≠0`, for `s` equal to `a` or `b`, differentiation gives
[
(u_s)_{xar x}=L^s,qquad
(u_s)_{xar y}=-rac{sar x}{2ar y}L^{s-1},qquad
(u_s)_{yar y}=rac{s(1-s)(1-r)}{4|y|^2}L^{s-2},
]
and
[
det H_s=rac{s(1-s-r)}{4|y|^2}L^{2s-2}>0
qquad (r<c<1-s).
]
The first principal minor `L^s` is positive, so each Hessian is positive definite off the axis. The functions are locally bounded above, tend uniformly to `-∞` toward the axis on compact subsets in `x`, and extend there as psh functions by the same removable-polar-set argument used in Example 13.2.9. At a point `(x_0,0)`, the radial upper growth is of order `-(log(1/ho))^s` on small balls; after division by `log ρ`, it tends to zero since `s<1`. This proves zero Lelong number, regardless of the precise factor in its chosen convention.

For smooth complex Hessians `H_a,H_b`, the mixed coefficient is the **polarization** of determinant, not the product of two determinants:
[
egin{aligned}
D(H_a,H_b)&=(H_a)_{xar x}(H_b)_{yar y}
+(H_b)_{xar x}(H_a)_{yar y}\
&quad -(H_a)_{xar y}(H_b)_{yar x}
 -(H_b)_{xar y}(H_a)_{yar x}\
&=rac{A(1-r)-2ab r}{4|y|^2}L^{a+b-2}.
end{aligned}
]
The coefficient `B_{a,b}(r)>0` because the two Hessians are positive definite. With `dd^c=(i/2π)∂∂bar`, the wedge density equals `D(H_a,H_b)/π²`; setting `b=a` recovers `2det(H_a)/π²`, verifying the normalization against the old square-model audit.

For every compact set disjoint from the axis, sufficiently high Bedford–Taylor truncations agree with the smooth psh functions, hence with the displayed mixed wedge. Plurifine locality ensures the cutoff limit agrees there. The axis is pluripolar and, by Lemma 13.2.2, the cutoff measure assigns it zero outer mass. Thus the formula for `dmu_{a,b}` is exact on the finite locus and on the whole domain after zero extension, whether or not it is locally finite.

Polar coordinates `y=ho e^{iartheta}`, `t=-logho`, give
[
int_{0<|y|le e^{-T}}rac{dA(y)}{|y|^2L^{2-a-b}}
=2piint_T^infty t^{a+b-2},dt.
]
The integral is finite **exactly for `a+b<1`**. Integrating `B_{a,b}(r)` in `x` over `|x|le R` gives
[
int_{|x|le R}B_{a,b}(|x|^2),dA(x)
=pileft(A R^2-rac{A+2ab}{2}R^4ight).
]
Multiplying proves the boxed exact cylinder mass. For `a+bge1` that same positive density has infinite mass near every point of the axis. This is precisely failure of the trace-bound criterion Eq. 13.2.3, whereas when `a+b<1` local density integrability verifies it.

## Nontrivial mixed-versus-diagonal distinction

Take **`a=1/8`**, **`b=3/4`**, and `0<c<1/4`. Then **`a+b=7/8<1`**, so the **mixed** product is locally finite, while **`2b=3/2>1`**, so the **self-product of `u_b` is not**. Conversely, taking `a=b=3/4` leaves both Lelong numbers zero but makes the mixed product non-locally-finite. The first example is **not obtainable from the former diagonal power threshold alone without a new mixed polarization computation**.

## Classification, dependency boundary and proposed annotation

**Status: verified conditional deduction; severity: low.** Original Lemma 13.2.2, Proposition 13.2.6, Example 13.2.9, and the earlier `POME-NPP-POWER-SINGULARITY-THRESHOLD-001` retain their prior statuses. No theorem is claimed false, no general integration-by-parts/Bedford–Taylor construction is independently certified. The only invoked upstream mathematics is psh extension across a polar hypersurface, bounded BT locality, smooth `dd^c` determinant polarization and the existing local-finiteness criterion. All are nonexcluded internal dependencies.

**Proposed source-body change (not applied):** optionally add an adjacent mixed-parameter remark after Example 13.2.9, stating the strict threshold `a+b<1` and emphasizing that one mixed product may exist while a diagonal product does not. Potential dependents: definition and multilinearity of products in §§13.2–13.5, local-to-global assumptions in §13.14, and energy products relying on local finiteness; none is newly certified or invalidated.

**Actual scope:** incremental proof-level visit to **§13.2, Lemma .2, Proposition .6, Example .9**, with §13.3.1 used only as conditional background. This was already a previously visited numbered section: **0 newly first-visited sections, 0 whole-section certifications**. Existing ToC inventory remains **25 chapters / 747 sections**. The owner-deferred Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work was not reopened. No build, CI, publication, source, registry, or permanent-tag change.
