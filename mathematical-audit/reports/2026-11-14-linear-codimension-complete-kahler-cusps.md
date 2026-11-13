# A complete Kähler logarithmic cusp along every linear subspace: the codimension threshold

- **Finding ID:** `POME-LINEAR-CODIM-COMPLETE-KAHLER-CUSP-001`.
- **Review date:** 2026-11-14.
- **Status / severity:** **verified conditional deduction / low**. Neither the printed theorem nor its example is refuted; this is an independent, stronger explicit family. The internal pseudoconvexity/domain-of-holomorphy equivalence is used only at the final classification step and is not independently certified here.
- **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Reading edition:** `docs/sections/separation-strict-exhaustions-and-coverings--complete-kahler-metrics-on-regular-open-sets/index.html`, Git blob `3faaef942f4822127e09c63a463d654d346696c2`, **Example 9.31.2**, source `demailly-complex-geometry:12510407`, permanent tag `D80B90CDCDA1`, physical HTML lines **25–42**. **Theorem 9.31.1**, source `demailly-complex-geometry:232F4B65`, permanent tag `214C6B3DF885`, lines **7–23**. Internal domain-of-holomorphy equivalences are cited there but are an independent analytic input for the classification.
- **Scope:** complex-space / Kähler geometry, not Demailly approximation. No Bergman, L2, Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof programme is opened.

## Statement

Let `1 <= k <= n`, let `z=(u,v) in C^k x C^(n-k)`, and let `Z={u=0}`. On `Omega=C^n\Z` set `s=|u|^2`, `t=log s` and define the smooth function on `R`

```text
q(t) = sqrt(1+t^2) - t
a(t) = 1/(1+q(t))
phi(t) = integral_0^t a(x) dx
Phi(u,v) = |u|^2+|v|^2+phi(log |u|^2).
```

With Pome's convention `dd^c=(i/2pi)partial barpartial`, the form `omega=dd^c Phi` is a **complete Kähler metric** on `Omega`. On any bounded tangential region `E subset C^(n-k)` of finite positive Euclidean volume, the `omega^n`-mass of the shrinking normal collar `{0<|u|<epsilon, v in E}` is finite for small epsilon and has **sharp order** `Theta((log(1/epsilon))^(-k))`. If `k>=2`, every holomorphic function on `Omega` extends across `Z`, so this complete Kähler domain is **not pseudoconvex**. If `k=1`, it **is** pseudoconvex, in fact Stein. Thus the non-pseudoconvexity threshold for the whole explicit linear-complement family is exactly complex codimension two.

This goes beyond the already audited `Z={0}` (codimension `n`) finite-cusp example: the missing locus may have **arbitrary positive dimension**, while the collar-volume exponent is the **normal codimension**, not the ambient dimension. No new claim is made about the earlier point-cusp formula.

## Proof of Kähler positivity and completeness

Since `q'(t)=t/sqrt(1+t^2)-1<0`, we have `a(t)>0` and `a'(t)=-q'(t)/(1+q(t))^2>0` for every real `t`. Consequently `phi'>0` and `phi''>0`. In normal coordinates the Hermitian form associated with `dd^c phi(log s)` has `k-1` tangential eigenvalues `phi'(t)/s` and one radial eigenvalue `phi''(t)/s`. This follows directly from

```text
partial barpartial phi(log s)
 = phi''(t) partial t wedge barpartial t
   + phi'(t) partial barpartial log s,
```

and `partial barpartial log s=(I-uu*/s)/s`. The Euclidean summand is positive definite and the new summand is positive semidefinite (indeed positive on all normal directions), so `omega` is Kähler.

As `t->-infinity`,

```text
phi'(t) ~ 1/(2|t|),   phi''(t) ~ 1/(2t^2).
```

Let `g` be the associated Riemannian metric. Positivity of the radial Hessian gives `length_g(path) >= c integral sqrt(phi''(t)) |dt|` for some fixed `c>0`. Therefore the pathwise length needed to reach `s=0` is infinite, because `integral^infinity dT/T=infinity`. More precisely `F(t)=integral_0^t sqrt(phi''(x)) dx` is globally Lipschitz with respect to the metric distance up to a constant and satisfies `F(t)->-infinity` at `Z`. Meanwhile `g` dominates a positive multiple of the Euclidean metric, so a metric-Cauchy sequence has a Euclidean limit and cannot escape to infinity. If this limit lay in `Z`, its `F` values would diverge, contradicting metric Cauchyness. Otherwise local equivalence of smooth metrics gives convergence in `Omega`. Hence `g` is complete.

## Exact normal-volume exponent

Relative to the standard Euclidean Hermitian matrix, the eigenvalues of `omega` are `1+phi'/s` (multiplicity `k-1`), `1+phi''/s` (radial), and `1` (multiplicity `n-k`). Thus the determinant ratio is **exactly**

```text
D(s) = (1+phi'(log s)/s)^(k-1)
       (1+phi''(log s)/s).
```

As `s->0` this is `(1+o(1))/(2^k s^k |log s|^(k+1))`. The polar-coordinate density in the normal `C^k` factor is a fixed positive multiple of `s^(k-1) ds`. Therefore the collar mass is comparable to

```text
integral_0^(epsilon^2) ds/[s |log s|^(k+1)]
 = (1/k)|log(epsilon^2)|^(-k).
```

This establishes the claimed sharp finite-volume order, with constants depending on the choice of normalizing `dd^c`, `n,k` and the positive Euclidean measure of `E`. No global finite-volume assertion at spatial infinity is made.

## Codimension dichotomy without analytic division or regularization

For `k>=2`, fix any point of `Z` and a sufficiently small product polydisc in the normal and tangential coordinates. For `f in O(Omega)`, integrate `f(z_1,z_2,...,z_k,v)` against the Cauchy kernel on a small fixed circle `|zeta_1|=r`, with `(z_2,...,z_k,v)` varying in a smaller polydisc. The contour avoids the deleted locus, so it defines a holomorphic function on the **full** smaller polydisc. Whenever `(z_2,...,z_k)!=0`, the ordinary Cauchy formula identifies it with `f`; the identity theorem yields agreement also when `(z_2,...,z_k)=0` away from the origin. These extensions agree on overlaps by uniqueness, and hence every global holomorphic function extends across `Z`. This excludes the domain-of-holomorphy property; by the original internal Cartan–Thullen equivalence used in Theorem 9.31.1 it excludes pseudoconvexity.

For `k=1`, `Omega=C^* x C^(n-1)`. The function `|z|^2+|z_1|^{-2}` is a smooth strictly plurisubharmonic exhaustion (it is a squared holomorphic norm plus the Euclidean potential); hence this domain is Stein/pseudoconvex by the existing internal criterion. The geometric codimension threshold is sharp.

## Audit classification / dependencies

- **Affected results:** independent validation and sharp enlargement of the boundary phenomenon in Example 9.31.2; Theorem 9.31.1 is **not contradicted**, because `Int cl(Omega)=C^n != Omega` for every deleted nonempty proper linear subspace.
- **External/internal analytic inputs not transitively certified here:** standard Cauchy formula and the domain-of-holomorphy/pseudoconvexity equivalence already used by §9.31. Their use is clearly separated from the fully explicit metric/determinant/completeness calculation.
- **Proposed addition if desired (not a source edit):** a concise optional example after Example 9.31.2 describing arbitrary linear codimension and the `|log epsilon|^{-k}` collar law.
- **No claim** of full §9.31 verification, analytic-division validation, project builds/tests, formal proof, or certification of other lemmas. Earlier point-puncture results retain their separate stable IDs.
