# Radial Gauduchon volume reconstruction: explicit linear response at a constant density

**Finding:** `POME-LCK-RADIAL-LEE-PERIOD-LINEARIZATION-001` — **low / verified conditional deduction** (not a false theorem or a repair of an existing proof).
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (2026-11-06).
**Integrated reading text:** `docs/sections/locally-conformally-kahler-geometry/index.html`, main Git blob `6ebf8e604b45d3eb748037af506145273ca3875d`.
**Exact anchors:** Lemma 23.2.37 and equations 23.2.36–39, physical lines 614–670; Lemma 23.2.40, lines 675–685; Theorem 23.2.41 and equation 23.2.42, lines 689–711; Proposition 23.2.43, lines 713–736. Source labels/permanent tags: `non-kahler-pluripotential-theory:607AB9B7`/`AE38387ABD03`; `:5E017ACB`/`1D02D96B9AF2`; `:D7D6D255`/`C4C3411B46C3`; `:9BB13FEF`/`503628CC8BE5`.

## Statement of new result

Put `m=n-1>=1`, and use the radial ansatz `omega=C(r)alpha+D(r)beta` on the scalar Hopf manifold of §23.2.35, with `r` of period 2. A radial Gauduchon solution with prescribed density `F=C^m D>0` and Lee period `L<0` satisfies

```text
C^m C' = k C + F,        D = F/C^m,
L = - integral_0^2 F/C^(m+1) dr,      k<0.             (A)
```

Fix a constant density `F_0=f>0` and a Lee period `L_0<0`. Its unique solution is

```text
C_0 = (-2f/L_0)^(1/(m+1)),
k_0 = -f/C_0,       ell = k_0/C_0^m = L_0/2 <0,
D_0 = f/C_0^m.
```

For an arbitrary smooth real 2-periodic perturbation `F_epsilon=f+epsilon g`, and **the same** Lee period `L_0`, the reconstructed `(C_epsilon,k_epsilon)` depends smoothly on `epsilon` near zero. Let `h= dC_epsilon/depsilon|_0`, `q=dk_epsilon/depsilon|_0`, and define `g_j=(1/2) integral_0^2 g(r) exp(-i pi j r) dr`. Then

```text
h_0 = C_0 g_0/((m+1)f),              q = -m g_0/((m+1)C_0),
h_j = C_0^(-m) g_j/(i pi j - ell)  (j != 0).           (B)
```

In particular a mean-zero perturbation of the prescribed radial volume density has **zero first variation of k**; its metric coefficient C gains one derivative at the linearized level (Fourier multiplier `(i pi j-ell)^(-1)`). The first variations of `D=F/C^m` and the Lee coefficient `l=kC^(-m)` are, with Fourier coefficients indexed by j,

```text
dD_0 = C_0^(-m) g_0/(m+1),
dD_j = C_0^(-m) g_j [i pi j+(m-1)ell]/[i pi j-ell]   (j != 0),
dl_0 = 0,
dl_j = -m ell C_0^(-m-1) g_j/[i pi j-ell]             (j != 0). (C)
```

Thus the Lee class is fixed while its pointwise representative changes; the nonzero modes of its variation also gain one derivative.

## Complete proof

The constant solution to (A) has `0=k_0 C_0+f`, and the period condition gives `L_0=-2f/C_0^(m+1)`, yielding the displayed constants. To justify differentiation (rather than merely formally differentiating a unique solution), for any integer `s>=1` consider the smooth map from `C_per^(s+1) x R x C_per^s` into `C_per^s x R` given by

```text
G(C,k,F) = (C^m C' - k C - F,
            - integral_0^2 F/C^(m+1) dr - L_0).
```

It is smooth where `C>0`. At `(C_0,k_0,f)`, its derivative in the unknowns `(h,q)` is

```text
(C_0^m h' - k_0 h - C_0 q,
  (m+1)f C_0^(-m-2) integral_0^2 h dr).
```

This is an isomorphism `C_per^(s+1) x R -> C_per^s x R`. To see this directly, the second component specifies the mean of h; integrating the first then specifies q; the remaining mean-zero first-order equation `h'-ell h=a(r)` has a unique 2-periodic solution because `ell<0` (its homogeneous multiplier over one period is `exp(2ell) !=1`). Standard integration of a smooth right-hand side supplies the claimed Banach-space bounded inverse. The implicit-function theorem produces a unique nearby smooth branch, and higher regularity follows by the ODE or by applying the argument in higher s. Theorem 23.2.41 identifies this local branch with its unique globally classified Gauduchon solution.

Differentiate (A), with `F'=g` and `L'=0`. At the constant background:

```text
h' - ell h = C_0^(1-m) q + C_0^(-m) g,             (D)
0 = integral_0^2 [g/C_0^(m+1)
                  -(m+1) f h/C_0^(m+2)] dr.        (E)
```

Equation (E) gives `h_0=C_0 g_0/((m+1)f)`. Taking the average of (D), then using `ell=-f/C_0^(m+1)`, gives `q=-m g_0/((m+1)C_0)`. For every `j !=0`, (D) has Fourier coefficient `(i pi j-ell)h_j=C_0^(-m)g_j`, proving (B). Differentiating `D=F/C^m` gives `delta D=C_0^(-m)g+m ell h`; differentiating `l=k/C^m` gives `delta l=C_0^(-m)q-m ell h/C_0`. Substituting (B) gives exactly (C), including the cancellation of its zero mode. This also checks the prescribed-period constraint `integral_0^2 delta l=0` directly.

## Classification and dependencies

The proof uses ordinary first-order ODE theory, the implicit-function theorem, and elementary periodic Fourier analysis; none belongs to the owner-excluded Demailly approximation, Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale, or positivity-loss programme. It uses the **printed** radial metric/Lee/volume conversion of Lemma 23.2.37 and uniqueness in Theorem 23.2.41, which have been checked here at the displayed equations but not independently certified with all preceding geometry. No premise about general nonradial LCK uniqueness is introduced. A reader-facing optional addition would be a short post-Theorem 23.2.41 remark giving (B) as a local-stability cross-check. No correction to the theorem, source labels, historical attribution, permanent tags or production text is requested. Affected *possible dependents*: radial uniqueness and twisted-potential reconstruction in §23.2.43–45. They are **not** newly certified.

**Coverage:** selected new calculation in previously unreviewed §23.2.35; printed identities 23.2.36–42 and their direct uses at 23.2.43–45. Not the rest of §23.2, not a whole-section audit, and not a verification of the project.
