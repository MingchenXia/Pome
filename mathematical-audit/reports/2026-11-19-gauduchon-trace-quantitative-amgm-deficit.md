# Gauduchon trace: a sharp square-root anisotropy deficit

**Finding:** `POME-GAUDUCHON-TRACE-AMGM-SQRT-DEFICIT-001`  
**Date:** 2026-11-19  
**Severity/status:** low / **verified conditional deduction** (not a confirmed error, not a repair, and not an upstream-chain certification).  
**Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading section:** `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html`, blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, **mathematical lines 5–82 directly read**.  
**Source collection:** `non-kahler-pluripotential-theory`.

## Permanent anchors and scope

- Section `non-kahler-pluripotential-theory:874B62BA` / permanent `A21D56C40154`, lines 5–7.
- Proposition 11.5.1, source `0D4A42C8` / permanent `828FAD1A35BF`, and its equation source `DF6E472D` / permanent `97DCB5703B01`, lines 11–27.
- Corollary 11.5.3, source `7E4B1B3F` / permanent `A9609E0AE7B9`, lines 36–46.
- Proposition 11.5.4, source `C78BBFF1` / permanent `BFC1330527CA`, equation `671B7CA8` / permanent `1F99A7154650`, lines 57–75.
- Its integrated equation source `D615B576` / permanent `B78F87EF7411`, lines 62–75, is the global application sharpened here.

All the printed statements and proofs in the above section were checked, including the distinction between the full distributional positive current (which retains pole mass) and the non-pluripolar product (which can discard pole mass). **No new confirmed original error or standalone proof gap was found.** The existing Gauduchon-metric existence theorem (§11.4), underlying distributional pairing calculus, and the singular unbounded-potential statement cited in §13.14.12 were not transitively certified.

## The sharpened pointwise theorem

Let `n >= 2`, and let `eta` and `gamma` be arbitrary **strictly positive** Hermitian `(1,1)`-forms on a complex `n`-dimensional vector space. Write

```text
B = gamma^{-1/2} eta gamma^{-1/2}  (positive Hermitian matrix),
q = (det B)^{1/n} = (eta^n/gamma^n)^{1/n}.
```

Then the exact, coordinate-independent inequality is

```text
eta ^ gamma^(n-1) / gamma^n - q
   >= (1/n) ||B^(1/2) - sqrt(q) I||_HS^2 >= 0.        (A)
```

The `^` in this displayed text denotes exterior product. Equality in either the first inequality or in the printed arithmetic–geometric mean bound holds **if and only if** `eta = q gamma`. The coefficient `1/n` in front of the squared Hilbert–Schmidt norm is **optimal as a universal coefficient**, for every `n >= 2`.

**Proof.** Let `lambda_1,...,lambda_n > 0` be the eigenvalues of `B`. Proposition 11.5.4 identifies the left side of (A) as

```text
A - G,  A = (1/n) sum lambda_j,  G = q = (prod lambda_j)^(1/n).
```

Set `m = (1/n) sum sqrt(lambda_j)`. The ordinary AM–GM inequality applied to the square roots gives `m >= sqrt(G)`. Direct expansion (without ellipticity assumptions or limiting operations) gives

```text
A - G - (1/n) sum (sqrt(lambda_j)-sqrt(G))^2
      = 2 sqrt(G) (m - sqrt(G)) >= 0.
```

The sum of squares is precisely the matrix norm in (A). Vanishing of `A-G` is equivalent to equality of all positive eigenvalues; likewise, equality in the **first** inequality in (A) is equivalent to `m=sqrt(G)`, which by AM–GM forces all eigenvalues equal.

To see sharpness of `1/n`, take `B_T=diag(T,1,...,1)` and `T->infinity`. Then

```text
 A_T - G_T = (T+n-1)/n - T^(1/n) = (T/n)(1+o(1)),
 (1/n)||sqrt(B_T) - T^(1/(2n))I||_HS^2 = (T/n)(1+o(1)).
```

Any coefficient strictly greater than `1/n` is therefore false for large `T`. This sharpness assertion is **pointwise**; it does not assert optimization among solutions in a prescribed global cohomology class.

For `n=1`, the printed AM–GM inequality is an identity and the squared matrix deviation vanishes, so (A) is trivially true but has no nontrivial sharpness meaning.

## Integrated global estimate and equality rigidity

Let `X` be a connected compact complex `n`-fold (`n >= 2`) and `gamma` any smooth Gauduchon metric. Let `theta` be a smooth real `(1,1)`-form and `u` a real smooth function such that
`eta = theta + dd^c u > 0` and `eta^n = c f dV`, where `c>0`, `f>0` is smooth and `dV>0` is a smooth volume form. Define

```text
q(x) = (c f(x) dV(x)/gamma^n(x))^(1/n),
B(x) = gamma(x)^(-1/2) eta(x) gamma(x)^(-1/2).
```

By integrating (A) and the already printed distributional Gauduchon trace identity (11.5.2), we obtain

```text
int_X theta ^ gamma^(n-1)
 - c^(1/n) int_X (f dV/gamma^n)^(1/n) gamma^n

 >= (1/n) int_X ||sqrt(B)-sqrt(q) I||_HS^2 gamma^n >= 0.   (B)
```

In particular, the **deficit** in the published inequality (11.5.6) quantitatively controls the full L2 square-root anisotropy of the solution tensor relative to `gamma`, without bounds on the individual eigenvalues. Since the right integrand is continuous and nonnegative, **equality in the integrated published bound holds iff** `eta=q gamma` at every point.

There is a further rigidity conclusion **only under additional closedness assumptions**: if `gamma` is Kähler, `d theta=0`, and `n>=2`, equality forces `q` to be constant. Indeed `d eta=0` and `eta=q gamma` imply `d q ^ gamma=0`; wedging by `gamma^(n-2)` yields `dq ^ gamma^(n-1)=0`, and the symplectic Lefschetz map from real one-forms to `(2n-1)`-forms is injective. Consequently `eta=q gamma`, `[theta]=q[gamma]`, and `f dV=(q^n/c)gamma^n`. If the prescribed volume density is not proportional to `gamma^n`, the published integrated inequality is necessarily strict in this Kähler/closed-background situation. **No constancy of `q` is asserted for arbitrary non-Kähler Gauduchon metrics.**

## Classification, dependents, and next audit obligations

- **Finding classification:** verified conditional deduction, low severity; the printed Proposition 11.5.4 is correct but its unrecorded sharp stability remainder and equality case are additional results. There is no original theorem to strike out and no production patch applied.
- **Affected dependents:** any use of the Gauduchon degree to bound smooth Monge–Ampère normalization constants via Proposition 11.5.4 / Equation 11.5.6, and any argument claiming equality in that bound. The proposed enhancement is optional and does not modify their hypotheses; equality statements must retain the Kähler/closed-background qualifiers above.
- **Dependencies:** the elementary matrix spectral theorem and AM–GM are supplied explicitly here; the global step uses the printed Proposition 11.5.1 (directly checked in this run) and Stokes/distributional integration by parts. Gauduchon's existence theorem (§11.4) was not reproved; the singular-potential density inequality cited in §13.14.12 was *not* re-audited. No Demailly regularization or related excluded programme is used.
- **Coverage delta:** §11.5 every mathematical paragraph directly read this run; **+1 whole direct section**, **+0 fully certified transitive upstream proof chains**. The historical first-visit count is deliberately not inferred from the former `LEGACY-UNRECONCILED` status.
- **Verification:** hand derivation of the exact square-root identity, pointwise extremizing family, integrated formula and Kähler equality rigidity. No automated tests, compilation, site build, CI or formal verification were performed. Audit record only; no source/registry/permanent-tag/main changes.

