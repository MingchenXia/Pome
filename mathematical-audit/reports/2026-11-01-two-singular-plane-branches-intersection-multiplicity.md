# Two singular plane branches: exact local Cartier intersection multiplicity

**Audit date:** 2026-11-01. **Production main examined:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-CYCLE-TWO-BRANCH-NORM-INTERSECTION-001`.
**Severity / status:** **low / verified conditional deduction**, not an error in the printed theorem, not a completed proof of all its dependencies, and not a production repair.
**Scope:** nonexcluded analytic cycles, normalized Poincaré–Lelong, and proper divisor intersections. The Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes were not examined; their older audit records remain **deferred-by-user**.

## Exact integrated reading-edition anchors

- `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html`, main blob `dae567406b2030e550664ca57b1fe77911d956d4`.
  - Theorem **20.5.5**, source **`demailly-complex-geometry:D58680EB`**, permanent tag **`F1C928146DBC`**, physical lines **63–76**. Its cycle Poincaré–Lelong formula, Eq. **20.5.6**, source **`demailly-complex-geometry:B5FA389B`**, tag **`14ADBD4BFF7F`**, lines **65–68**, and the pushforward formula Eq. **20.5.9**, source **`demailly-complex-geometry:51A40A6D`**, tag **`74331B0B45F1`**, lines **104–116**.
  - Theorem **20.5.10**, source **`demailly-complex-geometry:34D8935D`**, permanent tag **`DDB973C0C1DD`**, physical lines **132–153** (statement at **133–138**, proof at **140–151**). Its hypothesis requires the support intersections of **every subfamily** to have the expected codimension; the example below is a proper intersection of two distinct irreducible plane curves.
  - Lemma **20.5.2**, source **`demailly-complex-geometry:72B4BF94`**, permanent tag **`551A781E3A1C`**, lines **10–22**, requires the limiting holomorphic function to be nonzero on each connected component. That restriction becomes essential in the degeneration described below.
  - Example **20.5.11**, source **`demailly-complex-geometry:1764A64B`**, tag **`FF4839E28893`**, lines **154–158**, concerns a single singular cusp cut by the smooth coordinate line; the present result has **two singular branches** and is not that example repeated.
- `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, main blob `d4817ac64b1365bd967d42cd474fec169f992e28`: Definition **20.6.2**, source `demailly-complex-geometry:AFD209B1`, tag `BE0C86A8DD65`, physical line **8**, supplies the effective analytic-cycle conventions. This is a **definition check**, not a new proof audit of §20.6.

The source namespace `demailly-complex-geometry` here identifies the **classical analytic-cycle material** and does not authorize or reopen the excluded approximation programme.

## Exact theorem for an explicitly singular–singular intersection

Let `(x,y)` be coordinates on a small neighborhood of the origin in `C²`. Take coprime integer pairs
[
2le p<q,qquad 2le r<s,qquad gcd(p,q)=gcd(r,s)=1,
]
and (lambdainmathbb C^	imes). Let
[
 f=y^p-x^q,qquad g=y^r-lambda x^s,qquad
 Z_1={f=0},quad Z_2={g=0}.
]
Assume the two analytic germs are distinct; equivalently, exclude
[
 (p,q)=(r,s)quad	ext{and}quadlambda=1
]
**simultaneously**. Then both branches are irreducible and singular at the origin, their local support intersection is the point ({0}), and the properly defined classical current product is
[
 oxed{[Z_1]wedge[Z_2]
       =min{qr,ps},[{0}]}
]
as germs of positive ((2,2))-currents. In particular the integer coefficient has **no extra factorial or (2pi) factor** with the Pome convention (dd^c=rac{i}{2pi}partialarpartial).

### Proof 1: normalization and the integrated cycle formula

Since (p,q) are coprime, (f) is irreducible, and the normalization of (Z_1) is given near the origin by
[
 
u:(Delta,0)longrightarrow(Z_1,0),
 qquad x=t^p,quad y=t^q.
]
Likewise (g) defines an irreducible branch because (r,s) are coprime. Distinct irreducible plane curve germs cannot have a common one-dimensional component, so their local intersection is zero-dimensional and is exactly the origin after shrinking. The subfamily-codimension condition of Theorem 20.5.10 is therefore satisfied.

Pull back the second equation:
[
 gcirc
u=t^{qr}-lambda t^{ps}.
]
If (qr
e ps), the order is (min(qr,ps)), because the coefficient of the smaller power is nonzero. If (qr=ps), then (q/p=s/r). Reduced fractions force ((p,q)=(r,s)); distinctness then forces (lambda
e1), and (gcirc
u=(1-lambda)t^{qr}) has order (qr). Thus the order formula holds without exception under the hypotheses.

Theorem 20.5.5, specifically Eq. 20.5.9, computes the divisor intersection current by pushing forward the Poincaré–Lelong divisor of (gcirc
u). The normalization map has one point above the origin and degree one over the smooth part of (Z_1). The current coefficient at the origin is therefore precisely its vanishing order; it is (min(qr,ps)). Positivity and independence of order agree with Theorem 20.5.10. No smoothing or regularization is used.

### Proof 2: independent algebraic intersection-length calculation

Put (R=mathbb C{x}), the convergent power-series DVR, and
[
 A=R[y]/(y^p-x^q).
]
Division by the monic polynomial makes (A) a free (R)-module with basis (1,y,ldots,y^{p-1}). Because the two curve germs are distinct, multiplication by (g) on (A) is injective and its cokernel is a finite-length (R)-module. By Smith normal form over (R),
[
 dim_{mathbb C}A/gA
 =operatorname{ord}_xdet_R(m_g).
]
The fraction-field extension is (mathbb C((t))/mathbb C((x))), with (x=t^p,y=t^q). The determinant is the field norm:
[
 det_R(m_g)
   =N_{mathbb C((t))/mathbb C((x))}
       (t^{qr}-lambda t^{ps}).
]
The conjugates (tmapstozeta t), (zeta^p=1), each have (t)-order (k=min(qr,ps)); none vanishes identically under the distinctness condition. Their product has (t)-order (pk), hence (x)-order (k). Consequently
[
 dim_{mathbb C}rac{mathbb C{x,y}}
                         {(y^p-x^q, y^r-lambda x^s)}
 =k=min(qr,ps).
]
This independently reproduces the current-theoretic intersection multiplicity; the two proofs use different calculations, not independent certification of the whole resolution/Poincaré–Lelong dependency chain.

### Exact examples, limited checks, and a necessary hypothesis

- ((p,q,r,s,lambda)=(2,3,3,5,1)): (k=9), and (operatorname{Res}_y(f,g)=x^9(x-1)).
- ((2,3,2,3,2)): (k=6), and the resultant is (x^6).
- ((3,5,2,7,1)): (k=10).
- ((3,7,4,9,3)): (k=27).

The four orders were separately checked with a finite SymPy `resultant` and lowest-(x)-degree calculation. Those computations are **small arithmetic crosschecks**, not formal proof or a project test/build.

The case ((r,s)=(p,q)), (lambda
e1) is particularly instructive: two distinct *isomorphic* singular germs have proper-intersection coefficient (pq). However, as (lambda	o1), the second defining function tends to (f), which **vanishes identically on (Z_1)**. Theorem 20.5.5's nonzero-on-components hypothesis and the proper-intersection premise of Theorem 20.5.10 fail at (lambda=1); one must **not** infer a classical self-intersection current by taking this limit. In particular, the local (L^1([Z_1])) convergence of logarithms from Lemma 20.5.2 is inapplicable at that endpoint.

## Finding classification, proposed addition, dependents and limitations

**`POME-CYCLE-TWO-BRANCH-NORM-INTERSECTION-001`: low / verified conditional deduction.** The printed Theorems **20.5.5** and **20.5.10** are **not shown false**; the new result adds an exact and independently length-checked singular–singular model. A possible **separately reviewable editorial addition** is a short example after Example 20.5.11 explicitly recording the min formula, the proper-intersection restriction, and the endpoint failure. This is **not an applied source/registry/website patch**. Mathematical dependents are interpretation of proper divisor intersections in §§20.5–20.6 and local intersection multiplicity in §9's singular-space models. Existing singularity, Cartier, and b-divisor tags and all historical attributions must remain untouched.

**Coverage actually performed:** newly checked the use of the printed cycle-theoretic pushforward, the subfamily intersection hypothesis, the independent local algebra length formula, and the (L^1)-limit boundary of Lemma 20.5.2; these are **additional selected steps of the previously partially audited §20.5**, not a first visit and not a completed theorem, section, or upstream dependency certification. §20.6 was definition-only supporting context. The collection remains **25 chapters / 747 numbered sections / 0 complete mathematical-section certifications**. No repository tests, build, CI, formal verification or site publication were run, and production `main` was not modified.
