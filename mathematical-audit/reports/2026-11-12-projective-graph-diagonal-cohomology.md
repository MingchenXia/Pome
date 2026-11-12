# Integral graph and diagonal classes in projective space (2026-11-12)

**Finding ID:** `POME-PROJ-GRAPH-DIAGONAL-INTEGRAL-SIGNS-001`  
**Classification:** low / **verified conditional deduction**; the printed Lemma 10.75.1 and Theorem 10.75.2 are **not refuted**.  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Actual integrated reading edition:** `docs/sections/spectral-sequences-support-and-cup-products--the-integer-cohomology-ring-of-projective-space/index.html`, blob `cb90abebae459659c273b9de67848f3feded35e3`.
**Stable source/permanent anchors:** Lemma 10.75.1, `demailly-complex-geometry:1EB6C39D` / `419BAFBD0FA6`, physical HTML lines 16–41; Theorem 10.75.2, `demailly-complex-geometry:FF8EE3A7` / `0CD4D885B4B4`, lines 46–79. The exact-sign relation for the two de Rham comparison conventions is in section opening lines 7–13. Relevant internal dependencies cited in the integrated proof: §§10.40.2, 10.40.5, 10.50.3, 10.58.9/11, 10.71.5, 10.72.4, and 10.73.1. These are **context/dependency references**, not new certification of those entire sections.

## Precise assertion and hypotheses

Let `n >= 1`, `X = P^n_C` with its complex orientation, and let
`h = c_1^Z(O_X(1))` **in the signed frame/exponential convention actually used by Pome**. Theorem 10.75.2 states

```text
H*(X,Z) = Z[h]/(h^(n+1)),  tr_X(h^n) = (-1)^n.
```

Consequently `x = -h` is the positive complex-orientation hyperplane generator, with `tr_X(x^n)=1`. For a holomorphic map `f:X -> X` assume `f*h = d h` for an integer `d >= 0` (this holds with `d=0` for constants, and with usual algebraic degree `d>0` for projective endomorphisms). Write `h_1 = p_1*h` and `h_2 = p_2*h` on `X x X`. Let `Gamma_f={(z,f(z))}` be the graph, and `Delta=Gamma_id` the diagonal. Then their **integral** Poincare dual classes are

```text
[Gamma_f]^vee = (-1)^n sum_{j=0}^n d^j h_1^j h_2^(n-j),
[Delta]^vee   = (-1)^n sum_{j=0}^n h_1^j h_2^(n-j).
```

The `j=0` term has coefficient 1, including when `d=0`. These are not merely rational or real equalities. They yield exact integral intersection numbers

```text
int_(X x X) [Delta]^vee cup [Gamma_f]^vee = 1+d+...+d^n,
int_(X x X) [Gamma_f]^vee cup [Gamma_f]^vee = (n+1)d^n.
```

When `Gamma_f` is transverse to `Delta` (equivalently all fixed points are simple), the first number counts the fixed points without multiplicity. Without transversality it is only the cohomological intersection number; no assertion about the number of distinct fixed points is made.

## Independent argument

1. **Integral basis; no torsion loss.** `P^n` has a CW decomposition with one cell of each even real dimension `0,2,...,2n` and none in odd degrees, hence its integral cellular differential vanishes. The product CW structure on `X x X` likewise has only even-dimensional cells. The cellular cross-product Kunneth map is an isomorphism here because the cellular groups and all cohomology groups are free abelian. Combined with Theorem 10.75.2 this gives an *integral* ring basis `h_1^a h_2^b` for `0<=a,b<=n`, with `h_i^(n+1)=0`. (The elementary product-cell/Kunneth comparison is the explicit topology input; this run does not certify all of Pome's underlying duality theory.)
2. **Product orientation and signed trace.** The Pome trace formula gives `tr_X(h^n)=(-1)^n`. By product orientation and Fubini/compatibility of the integral cross product,
   `tr_(X x X)(h_1^n h_2^n)=(-1)^n(-1)^n=1`. Thus the displayed monomials in total degree `2n` are an integral basis, and their complementary-degree monomials form a perfect integral pairing. No de Rham comparison map is silently stripped of its sign.
3. **Graph pairing.** The embedding `i_f:X -> X x X`, `z -> (z,f(z))`, is holomorphic and has a smooth complex normal bundle even if `f` has critical points. Its oriented fundamental class has Poincare dual `D_f` satisfying
   `tr_(X x X)(D_f cup p_1^*a cup p_2^*b)=tr_X(a cup f^*b)`.
   Take `a=h^(n-j)`, `b=h^j`. The right side is `d^j(-1)^n`. If `D_f=sum_(k=0)^n c_k h_1^k h_2^(n-k)`, the left side is exactly `c_j`, by the product trace above and vanishing of powers above `n`. Therefore `c_j=(-1)^n d^j`. This determines `D_f` integrally, not just after tensoring with `R`. Setting `d=1` and `f=id` gives the diagonal class.
4. **Intersection checks.** In the two products `D_f D_id` and `D_f^2`, only terms whose first-factor exponents sum to `n` contribute. The `(-1)^n` coefficients occur twice, while `tr(h_1^nh_2^n)=1`, so
   `tr(D_f D_id)=sum_(j=0)^n d^j` and `tr(D_f^2)=sum_(j=0)^n d^j d^(n-j)=(n+1)d^n`. These identities remain valid for `d=0`, `n>=1`.
5. **Geometric independent sign check.** The graph normal bundle is canonically `N_(Gamma_f/(X x X)) ~= f^* T_X`, because the quotient map `T_X ⊕ f^*T_X -> f^*T_X`, `(v,w) -> w-df(v)`, has the graph differential as its kernel. The projective Euler sequence gives `c_n(T_X)=(n+1)x^n=(n+1)(-1)^n h^n`. Its pullback and integral are `(n+1)d^n`, matching the computed self-intersection without switching conventions. The Euler-sequence computation is an auxiliary elementary crosscheck, not a claim to certify another section's proof.

For `n=1,d=2`, the graph class is `-(h_2+2h_1)`, its diagonal intersection is 3 and its self-intersection is 4. For `n=2,d=2`, its class is `h_2^2+2h_1h_2+4h_1^2`, with diagonal intersection 7 and self-intersection 12. These examples check both the dimension-dependent `(-1)^n` sign and the exponent position `d^j`. Replacing `h` by the usual positive generator `x=-h` removes the global sign from the displayed graph-class polynomial; applying the unsigned positive-hyperplane formula directly to Pome's `h` would be a convention error.

## Disposition and affected dependents

**Status:** verified conditional deduction. This audit verifies the graph/diagonal calculations **conditional on** the integrated integral cohomology theorem, oriented Poincare duality, and elementary integral cellular cross-product comparison. It does **not** independently reprove those complete internal chains, establish a false theorem in §10.75, or certify all of §§10.40–10.75. Suggested optional insertion: a new post-Theorem-10.75.2 example recording the signed graph class and intersection numbers; **no source/body/registry/tag/canonicalization edit is authorized or made**. Affected future consistency checks: diagonal Gysin signs, projective holomorphic Lefschetz intersection counts, projective endomorphism normal bundles, integer (not merely real) intersection products.

**Actual coverage:** direct re-examination of integrated §10.75 opening conventions, Lemma 10.75.1, Theorem 10.75.2 and its proof (physical lines 7–79); selected independent graph/duality computation. §10.75 was previously inspected for comparison normalization, so **0 first-visited numbered sections** and **0 complete-section certifications**; main ToC still **25 chapters / 747 sections**. All older confirmed errors and gaps remain unchanged. Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion work remain **deferred-by-user**, neither revisited nor certified. No build, tests, CI, publication or main modifications.
