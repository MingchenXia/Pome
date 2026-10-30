# Weighted projective products: exact Gauduchon volume, minimizing rays, and complete flat Hessian cones

- **Finding:** `POME-GAUD-WEIGHTED-PRODUCT-FLAT-001`.
- **Classification:** **low / verified conditional deduction**. The new statement is an explicit higher-dimensional model corollary, **not** a false printed theorem, a repaired general proof, or a certification of the global elliptic dependency chain.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (30 October 2026).
- **Audit scope:** newly derive the arbitrary-number-of-factors and arbitrary-factor-dimensions formulas from the *integrated reading edition*. The previously printed two-dimensional `P^1 x P^1` example in §12.6.2 is not re-registered.
- **Excluded:** all Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**, neither repaired nor certified.

## Exact integrated anchors

1. `docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html`, main blob `9ec67161d46b3ba20afa1b1c9a0c84f29322763e`: denominator `D_mu` lines 7–13, Definition 12.2.1 source `non-kahler-pluripotential-theory:6E1DBC11`, permanent tag `0C4AF7E2CEBB`, lines 16–21; Theorem 12.2.3 source `non-kahler-pluripotential-theory:876DF057`, tag `2DB664A6EFDF`, lines 58–77. Its all-density conclusion depends on the separately printed smooth equation §14.2.1.
2. `docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html`, main blob `4992f82c6e84918ead47a972eab7e3238a147655`: Proposition 12.4.1 source `non-kahler-pluripotential-theory:C55D0CC4`, permanent tag `67FDDBC10DBD`, lines 22–74; Hessian metric formula 12.4.4 tag `6BCEC0329DE5`, lines 67–74.
3. `docs/sections/a-gauduchon-variational-volume--the-hessian-metric-and-its-completion/index.html`, main blob `23a7f2a1dab791569c39a0ff5f056f52bfc200fe`: Proposition 12.6.1 source `non-kahler-pluripotential-theory:9494E2B6`, tag `88C1708A920C`, lines 25–62; printed two-factor model §12.6.2 source `non-kahler-pluripotential-theory:FA1370DB`, permanent tag `5429610F6E7A`, lines 66–92.

## Statement

Let `k >= 2`, `d_1,...,d_k >= 1`, `n=sum_j d_j`, and let
`X=prod_{j=1}^k P^{d_j}`. Write `alpha_j` for the pullback of the normalized Fubini–Study form from factor `j`, so that `int_{P^{d_j}} omega_FS^{d_j}=1`. Put

```text
mu_0 = alpha_1^{d_1} wedge ... wedge alpha_k^{d_k},   integral_X mu_0 = 1,
theta_a = sum_j a_j alpha_j,                             a_j>0,
C = n! / (d_1! ... d_k!).
```

On the **factor-subspace** positive cone `C_fac=(0,infinity)^k` of distinct smooth background classes, the variational root volume for the fixed probability `mu_0` is exactly

```text
lambda_{mu_0}(theta_a) = C^{1/n} product_j a_j^{d_j/n}.
V_{mu_0}(theta_a) = C product_j a_j^{d_j}.
```

Every minimizing Gauduchon metric for this fixed `mu_0` is a positive constant multiple of `theta_a`. The Hessian metric `g=-D^2 log lambda` restricted to the factor cone is

```text
g = sum_j (d_j/n) (da_j/a_j)^2 .
d_g(a,b)^2 = sum_j (d_j/n) [log(b_j/a_j)]^2 .
```

It is **flat and metrically/geodesically complete**; its unique minimizing geodesic between `a` and `b` is the coordinatewise geometric interpolation `a_j(t)=a_j^{1-t} b_j^t`. The unit-root-volume slice `lambda=1`, with induced metric, is an affine Euclidean hyperplane after the weighted logarithmic coordinate change and is complete. The same formula for `lambda_mu` holds for any other smooth positive probability `mu` **conditional on** the integrated smooth Monge–Ampère existence theorem used by §12.2.3; this extra all-density statement is not needed for the direct `mu_0` proof.

## Independent proof for mu_0 (no PDE existence assumption)

By dimension counting and the multinomial theorem, the only term of bidegree `(d_j,d_j)` in every factor that survives in `theta_a^n` has multiplicity `C`. Hence

```text
theta_a^n = C (product_j a_j^{d_j}) mu_0 = V(a) mu_0.
```

For any Hermitian metric `gamma`, the pointwise matrix arithmetic–geometric mean inequality (with wedge products normalized as in the reading edition) gives

```text
theta_a wedge gamma^{n-1}
 >= [(theta_a^n / gamma^n)^{1/n}] gamma^n
 = V(a)^{1/n} (mu_0 / gamma^n)^{1/n} gamma^n.
```

When `gamma` is Gauduchon, integrate and divide by the positive denominator `D_{mu_0}(gamma)` of Definition 12.2.1. This proves `lambda_{mu_0}(theta_a) >= V(a)^{1/n}`. But `theta_a` is Kähler, hence itself Gauduchon, and substitution `gamma=theta_a` attains pointwise equality. The opposite inequality follows **without using** the smooth existence theorem, regularization, or any approximation.

Equality in the integrated arithmetic–geometric mean forces the eigenvalues of `theta_a` relative to `gamma` to agree everywhere, because the nonnegative pointwise defect is smooth and has zero integral. Thus any minimizer has `gamma=e^h theta_a`. The Gauduchon condition reduces to
`dd^c(e^{(n-1)h}) wedge theta_a^{n-1}=0`; its scalar Kähler Laplacian is zero on compact connected `X`, so `h` is constant. This proves the minimizer-ray statement. (All `d_j>=1`, `k>=2`, hence `n>=2`.)

The classes `[alpha_j]` are linearly independent modulo smooth `dd^c)-exact forms: integrate over a projective line in the `j`-th factor with all other factor coordinates fixed. A `dd^c)-exact form has integral zero over every such curve; `int alpha_i=delta_{ij}`. Thus the coefficient coordinates `a_j` give a genuine finite-dimensional positive cone of background classes.

Taking logarithms of the exact volume gives

```text
-log lambda(a) = -(log C)/n - sum_j (d_j/n) log a_j.
```

Differentiating **in affine class coordinates `a_j`**, not in logarithmic coordinates, yields `g` above. Define `x_j=sqrt(d_j/n) log a_j`; then `g=sum_j dx_j^2` globally on all of `R^k`. The Euclidean geodesic, distance and completeness formulas follow. In these coordinates,
`log lambda=(log C)/n + sum_j sqrt(d_j/n) x_j`, and `sum_j d_j/n=1`, so the normal vector to every volume level has Euclidean norm one. The level `lambda=1` is therefore a complete affine Euclidean hyperplane of dimension `k-1`.

A useful **fixed-volume boundary test**: fix all other coefficients and take
`a_1(t)=exp(-t)`, `a_2(t)=exp((d_1/d_2)t)`, `t>=0`. Then `lambda` remains constant even though `a_1` approaches zero and `a_2` diverges; the intrinsic distance traveled from `t=0` is exactly
`t sqrt[(d_1/n)(1+d_1/d_2)]`. Thus a constant-root-volume degeneration still goes infinitely far in the positive cone. This is a direct higher-dimensional check of the product splitting in §12.6.1, not a new proof of that general proposition.

For an arbitrary smooth positive probability `mu`, the separately printed Theorem 12.2.3 gives `lambda_mu^n=c_theta(mu)`. Since `theta_a` is closed, any smooth solution `Omega=theta_a+dd^c u` is closed and cohomologous to it, so `int Omega^n=int theta_a^n=V(a)`; as `int mu=1`, its constant is `c_theta(mu)=V(a)`. This **last all-density extension is conditional on §14.2.1**. No such input was needed for the fixed `mu_0` conclusion.

## Adjudication, downstream scope and proposal

- **Mathematical verdict:** printed Definitions 12.2.1, Propositions 12.4.1/12.6.1 and the printed §12.6.2 two-factor example are consistent with the exact calculation; **no false theorem or proof gap is claimed**.
- **Distinctness:** the printed example explicitly handles only `P^1 x P^1` with two unit weights. The new derivation treats any number of factors and arbitrary positive factor dimensions, identifies the unique minimizing Gauduchon rays at the fixed product probability, gives every intrinsic distance and geodesic, and proves that even a fixed-volume boundary can be infinitely distant. Do not re-register the old example.
- **Optional change:** append a standalone corollary after §12.6.2 (no source, registry, canonicalization or permanent-tag edits in this audit). Affected discussions: §§12.2–12.6, Hessian completion and Kähler-class examples. The calculation does not verify global existence, positivity-cone classification outside this finite-dimensional subspace, or the project-wide variational theory.
- **Actually inspected:** the exact printed quotient and equality proof §§12.2.1/3; the displayed Hessian formulas §§12.4.1/4 and 12.6.1; comparison against the already printed §12.6.2. Additional §8.2 cone estimates were inspected as context but are not new certified coverage. No complete mathematical section or upstream theorem chain was certified.
- **Checks:** hand proof with explicit multinomial factors and weighted Euclidean coordinates; no code, numerical tests, build, CI, formalization, website publication or automated source modification. Coverage ledger stays **25 current chapters / 747 numbered ToC sections / zero fully certified mathematical sections**.
