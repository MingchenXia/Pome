# Two singular plane branches: exact local intersection multiplicity

**Date:** 2026-11-01. **Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Stable finding:** `POME-CYCLE-TWO-BRANCH-NORM-INTERSECTION-001`.
**Severity/status:** **low / verified conditional deduction**. The printed theorems have **not** been shown false; this is an exact new model, **not** a repair or complete proof-chain certification.

## Exact integrated reading-edition anchors

- `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html`, main blob `dae567406b2030e550664ca57b1fe77911d956d4`.
  - **Theorem 20.5.5**, source `demailly-complex-geometry:D58680EB`, permanent tag `F1C928146DBC`, lines **63–76**. Its cycle Poincaré–Lelong equation **20.5.6**, source `demailly-complex-geometry:B5FA389B`, permanent tag `14ADBD4BFF7F`, lines **65–68**; its pushforward equation **20.5.9**, source `demailly-complex-geometry:51A40A6D`, permanent tag `74331B0B45F1`, lines **104–116**.
  - **Theorem 20.5.10**, source `demailly-complex-geometry:34D8935D`, tag `DDB973C0C1DD`, statement lines **133–138**, proof **140–151**, requires proper codimension for **every subfamily** of divisor supports; the two branches below do meet properly.
  - **Lemma 20.5.2**, source `demailly-complex-geometry:72B4BF94`, tag `551A781E3A1C`, lines **10–22**, requires the limit holomorphic function to be nonzero on every relevant connected component.
  - **Example 20.5.11**, source `demailly-complex-geometry:1764A64B`, tag `FF4839E28893`, lines **154–158**, concerns a *single cusp cut by a smooth line*, not the present **two singular branches**.
- `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, blob `d4817ac64b1365bd967d42cd474fec169f992e28`: **Definition 20.6.2**, source `demailly-complex-geometry:AFD209B1`, tag `BE0C86A8DD65`, line **8**, is a definition-only consistency check.

The historic source prefix `demailly-complex-geometry` is an attribution identifier for ordinary analytic cycles. **No work on the excluded Demailly approximation/regularization programme was performed.**

## A two-branch exact theorem

Let \((x,y)\) be coordinates near \(0\in\mathbb C^2\). Choose coprime integer pairs
\[
2\le p<q,\qquad 2\le r<s,\qquad
\gcd(p,q)=\gcd(r,s)=1,
\]
and \(\lambda\in\mathbb C^\times\). Put
\[
 f=y^p-x^q,\quad g=y^r-\lambda x^s,\quad
 Z_1=\{f=0\},\quad Z_2=\{g=0\}.
\]
Assume \(Z_1\ne Z_2\) as analytic germs, i.e. **not both** \((p,q)=(r,s)\) and \(\lambda=1\).
Then \(Z_1,Z_2\) are irreducible singular curve germs, their support intersection near the origin is exactly \(\{0\}\), and the classical proper divisor product is
\[
\boxed{[Z_1]\wedge[Z_2]=\min\{qr,ps\}\,[\{0\}].}
\]
This is the current coefficient with Pome's \(dd^c=(i/2\pi)\partial\bar\partial\); no additional \(2\pi\) or factorial is present.

### First complete proof: normalization and cycle Poincaré–Lelong

The coprimality of \((p,q)\) makes \(f\) irreducible; its normalization is
\[
\nu:(\Delta,0)\to(Z_1,0),\qquad x=t^p,\quad y=t^q.
\]
Similarly \(g\) is irreducible. Distinct irreducible plane curve germs share no one-dimensional component, so their local intersection is zero-dimensional, and after shrinking it is precisely \(0\). Thus the subfamily codimension conditions of Theorem 20.5.10 hold.

On the normalization,
\[
g\circ\nu=t^{qr}-\lambda t^{ps}.
\]
If \(qr\ne ps\), the lower power occurs with a nonzero coefficient and has order \(k=\min(qr,ps)\). If \(qr=ps\), then the reduced fractions \(q/p=s/r\) imply \((p,q)=(r,s)\). The distinctness assumption forces \(\lambda\ne1\), hence \(g\circ\nu=(1-\lambda)t^{qr}\) has that same order \(k=qr=ps\). Theorem 20.5.5, in the precise pushforward form 20.5.9, now yields
\[
 dd^c\bigl(\log|g|^2[Z_1]\bigr)
   =\nu_*[\operatorname{Div}(g\circ\nu)]
   =k[0].
\]
Theorem 20.5.10 identifies this with the properly defined symmetric classical intersection. This proves the formula, including the exact normalization factor and positivity.

### Second independent calculation: local algebra and a norm determinant

Let \(R=\mathbb C\{x\}\) and \(A=R[y]/(y^p-x^q)\). Division by the monic polynomial shows that \(A\) is free of rank \(p\) over the DVR \(R\), with basis \(1,y,\dots,y^{p-1}\). Distinctness of the germs makes \(g\) a nonzero divisor in the domain \(A\), so multiplication \(m_g:A\to A\) is injective with finite-length cokernel. Smith normal form over \(R\) gives
\[
 \dim_{\mathbb C} A/gA
  =\operatorname{ord}_x\det_R(m_g).
\]
After scalar extension from \(\operatorname{Frac}(R)\) to its \(x\)-adic completion \(\mathbb C((x))\), the rank-\(p\) algebra becomes the field extension \(\mathbb C((t))/\mathbb C((x))\), with \(x=t^p,y=t^q\). This completion does not change the matrix determinant or its \(x\)-adic valuation. The determinant is the field norm
\[
\det_R(m_g)
 =N_{\mathbb C((t))/\mathbb C((x))}
    (t^{qr}-\lambda t^{ps})
 =\prod_{\zeta^p=1}
    \left(\zeta^{qr}t^{qr}-\lambda\zeta^{ps}t^{ps}\right).
\]
Each nonzero factor has \(t\)-order \(k=\min(qr,ps)\) by the same coprimality/distinctness argument. Their product has \(t\)-order \(pk\), which is \(x\)-order \(k\). Therefore
\[
\boxed{\dim_{\mathbb C}
 \frac{\mathbb C\{x,y\}}
 {(y^p-x^q,\ y^r-\lambda x^s)}
 =\min(qr,ps).}
\]
This separately recovers the proper local intersection number, without assuming the result from the preceding current computation.

### Small reproducible arithmetic checks; failed endpoint hypothesis

Independent SymPy resultant calculations gave:

| \((p,q;r,s;\lambda)\) | \(\operatorname{ord}_x\operatorname{Res}_y(f,g)\) | \(\min(qr,ps)\) |
| --- | ---: | ---: |
| \((2,3;3,5;1)\) | 9 | 9 |
| \((2,3;2,3;2)\) | 6 | 6 |
| \((3,5;2,7;1)\) | 10 | 10 |
| \((3,7;4,9;3)\) | 27 | 27 |

The first resultant is \(x^9(x-1)\) and the second \(x^6\). These are **small finite algebraic crosschecks**, not full project tests, builds, or formal verification.

In the family \((r,s)=(p,q)\), \(\lambda\ne1\), the coefficient is \(pq\), even though both branches are singular and tangent. At the endpoint \(\lambda=1\), \(g=f\) vanishes **identically on \(Z_1\)**: the proper-intersection hypothesis in Theorem 20.5.10 is lost, and the nonzero-on-components hypothesis for logarithmic \(L^1\)-convergence in Lemma 20.5.2 fails. The finite proper intersection cannot be passed to this endpoint as a self-intersection current without a distinct construction.

## Classification, possible correction and actual coverage

**`POME-CYCLE-TWO-BRANCH-NORM-INTERSECTION-001` — low / verified conditional deduction.** No original false theorem, newly discovered proof gap, or applied source repair is asserted. An **optional, separately reviewable addition** after Example 20.5.11 would record the formula and the degenerate self-intersection boundary. Preserve all historical attributions and permanent tags. Relevant dependents are §§20.5–20.6 proper Cartier intersections and §9 singular-space local intersection models; no other result is automatically certified.

**Only additional selected mathematical checks** were made in previously partly reviewed §20.5: Theorems 20.5.5 and 20.5.10, the normalization pushforward, and the boundary of Lemma 20.5.2. §20.6 supplied definition-level context only. The broad collection remains **25 chapters, 747 current numbered sections, zero fully mathematically certified sections**. Existing error/proof-gap/external/duplication statuses remain unchanged; the user-deferred approximation, regularization, Bergman, L², OT, multiscale-atlas and positivity-loss items remain **deferred-by-user**, not resolved. No production main, source text, tags, registry, published docs, CI, full build, or formalization was modified or run.
