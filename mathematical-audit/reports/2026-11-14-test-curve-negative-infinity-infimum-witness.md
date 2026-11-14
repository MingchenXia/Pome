# Noncommuting decreasing test-curve infima and negative-infinity endpoints

**Finding:** `POME-TC-DECREASING-INF-NEGATIVE-INFTY-NONCOMMUTE-001`  
**Date:** 2026-11-14. **Severity:** low. **Status:** verified conditional deduction (explicit witness to the *correctly printed warning*, not a false theorem).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Integrated statements and immutable anchors

1. `docs/sections/test-curves--operations-on-test-curves/index.html`, blob `3da617be8f58713f764d49ba22f49b803149a5e8`. Section 17.15 permanent tag `9D751AA26579`. Definition 17.15.37 source `sgpt:2102B018`, permanent `BDCF69FED30F`, lines 813–839; its two assumptions (17.15.38)–(17.15.39), sources `sgpt:96121742`, `sgpt:DE1857D4`, permanent `48E9DB47C37C`, `C2C47DDCADA4`, lines 815–822. Proposition 17.15.40 source `sgpt:06038274`, permanent `82DA4D86CC78`, lines 843–858. Crucially, lines **862–866** expressly warn that `(inf_i Gamma^i)_{-infinity}=inf_i Gamma^i_{-infinity}` need not hold. Lemma 17.15.41 source `sgpt:C9AAF985`, permanent `E141137C118E`, lines 868–898.
2. `docs/sections/test-curves--the-notion-of-test-curves/index.html`, blob `6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7`. Definition 17.12.1 source `sgpt:ECCF19D5`, permanent `C8399F09D86D`, lines 10–35, including regularization of the negative-infinity supremum.
3. `docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html`, blob `97681f31628eb362950837daaadde67d10507a2f`. Envelope Definition 16.3.4 source `sgpt:15C6153F`, permanent `395DB7860949`, lines 79–85; model Definition 16.3.17 source `sgpt:A6D9D88E`, permanent `6623E38E5FC2`, lines 289–291.

## Statement proved

For every `0<c<1`, there is a decreasing **sequence of genuine model test curves** `Gamma^j` on `P^1`, with each `Gamma^j_max=0` and with a **uniform strictly positive non-pluripolar mass floor** `1-c`, such that

```math
(\inf_j\Gamma^j)_{-\infty}=u_c\ne0=\inf_j\Gamma^j_{-\infty}.
```

The mass of the left-hand endpoint is `1-c`, whereas the right-hand endpoint has mass `1`. Thus even the hypotheses of Proposition 17.15.40 do **not** justify interchanging a decreasing infimum with the endpoint at `-infinity`. This is precisely consistent with the source's warning after the proposition.

## Direct construction of model potentials on P¹

Normalize `theta=omega_FS` so `int_{P^1}theta=1`, and use `dd^c=(i/2pi)partial barpartial`. On the affine coordinate chart write `r=log|z|²` and `F(r)=log(1+exp r)`. For `0<a<1`, define

```math
r_a=\log\frac a{1-a},\qquad H(a)=-a\log a-(1-a)\log(1-a),
\qquad
F_a(r)=\begin{cases}ar+H(a)&r\le r_a,\\ F(r)&r\ge r_a,\end{cases}
\qquad u_a(z)=F_a(r)-F(r).
```

Set `u_a(0)=-infinity`, `u_a(infinity)=0`, and `u_0=0`. Since `F'(r_a)=a` and `F(r_a)-a r_a=H(a)`, the pieces are joined with equal value and first derivative, and `F_a` is convex. Hence `theta+dd^c u_a` is positive. Its exact current is

```math
\theta+dd^c u_a=a\delta_0+\mathbf 1_{\{r>r_a\}}\theta,
```

with **no spurious circle-boundary mass** (the slope is continuous at `r_a`). The non-pluripolar product discards the atom at the polar point `0`; the Fubini–Study radial mass on `r>r_a` is `1-F'(r_a)=1-a`. Consequently

```math
\int_{P^1}\langle\theta+dd^c u_a\rangle=1-a>0.
```

**Model property, not assumed.** The potential `u_a` is normalized by `sup u_a=0`. If `v in PSH(P^1,theta)` is any envelope competitor (`v<=0` and `v preceq u_a`), then its Lelong number at zero is at least `a`. On the disk `r<r_a`, `v+F(r)-ar` therefore extends subharmonically across zero. At `r=r_a` it is at most `F(r_a)-ar_a=H(a)`. The subharmonic maximum principle gives `v<=ar+H(a)-F(r)=u_a` inside that disk. Outside, `v<=0=u_a`. As `u_a` is itself an admissible competitor, `P_theta[u_a]=u_a`. Together with the positive mass formula this establishes the *exact* model condition of §16.3.17 with no regularization or analytic Bergman input.

For fixed finite `r`, let `p=F'(r)=e^r/(1+e^r)`. The map `a mapsto u_a(r)` is `0` for `a<=p`, and for `a>p` equals `ar+H(a)-F(r)` with derivatives

```math
\frac{d u_a(r)}{da}=r-\log\frac a{1-a}<0,\qquad
\frac{d^2u_a(r)}{da^2}=-\frac{1}{a(1-a)}<0.
```

The first derivative matches zero at `a=p`. Thus `a mapsto u_a` is pointwise **nonincreasing and concave**; its limit as `a downarrow0` equals zero away from `z=0`, and the upper-semicontinuous regularization of that limit is zero everywhere.

## Genuine decreasing test curves with positive mass

For each integer `j>=1`, put

```math
\Gamma^j_{\max}=0,\qquad
\Gamma^j_\tau=u_{a_j(\tau)},\qquad a_j(\tau)=c e^{\tau/j}\quad (\tau<0).
```

The scalar function `a_j(tau)` is convex and increasing, with range `(0,c)`; composition with the pointwise concave nonincreasing `u_a` is concave and nonincreasing in `tau`. Every finite slice is a normalized model of positive mass `1-a_j(tau)`. At `tau -> -infinity`, `a_j(tau)->0` and the *regularized* supremum (17.12.2) equals `0` even at the polar point `z=0`. Therefore `Gamma^j_{-infinity}=0` with mass `1`, and all conditions in the actual Definition 17.12.1 are met.

For every fixed `tau<0`, `a_j(tau)` increases with `j`; since `u_a` decreases in `a`, we have `Gamma^{j+1}_tau<=Gamma^j_tau`. Their terminal parameters are identical, so the family is decreasing under the **full order definition** in §17.15.1. The exact required bounds are

```math
\inf_j\Gamma^j_{\max}=0>-\infty,\qquad
\inf_j\int_{P^1}\langle\theta+dd^c\Gamma^j_{\tau_0}\rangle
=\inf_j(1-ce^{\tau_0/j})=1-c>0
\quad(\tau_0<0).
```

At each fixed finite `tau<0`, `a_j(tau)uparrow c` and `inf_j Gamma^j_tau=u_c`. The resulting limit test curve is constant `u_c` for all `tau<0`, and has endpoint `u_c`. But each individual endpoint is `0`; hence the desired strict inequality and the mass gap `1-c` versus `1`.

## Status, consequences, and boundaries of the audit

This supplies a **concrete example for the printed warning**, not a counterexample to Proposition 17.15.40 or Lemma 17.15.41. In particular, the latter avoids this illegal interchange by proving slice-level `d_S` convergence. The potential failure affects *hypothetical dependent arguments* that replace a decreasing infimum endpoint by the infimum of endpoints, changing even its non-pluripolar mass. An optional explanatory example after lines 862–866 is proposed; this audit does **not** change production source/body, canonicalization, registry or permanent tags.

This is mathematically different from the already logged `POME-TC-CHOQUET-DEAD-SLICES-001` proof gap in §17.15.31 and from mass-collapse cases **without** a uniform positive-mass bound. No full certification of §17.15 or of the project's general NPP proof chain is claimed. User-deferred Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion are **not inspected, reopened, or certified**. No project builds, tests, GitHub Actions or website publication were run.
