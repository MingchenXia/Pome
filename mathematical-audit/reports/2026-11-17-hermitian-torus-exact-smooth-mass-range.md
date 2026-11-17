# Exact full smooth Hermitian Monge–Ampère mass range for the nonclosed two-torus background

**Date:** 2026-11-17. **Finding:** `POME-HERM-TORUS-EXACT-SMOOTH-MASS-INTERVAL-001`, **low / verified conditional deduction**; the printed results are correct. This is a sharp global optimization for the *specific* integrated torus model, not a general upper-volume theorem or a certification of nonsmooth product continuity.

**Reviewed production main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit target:** `review/mathematical-audit`.
**Integrated reading edition:** `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`, §11.1 (permanent section tag `7B453010B5B8`).
**Pinned source anchors:** Lemma 11.1.2 (`non-kahler-pluripotential-theory:7DC882C7`, permanent `3B0A8DD950AD`, physical lines 15–31); Theorem 11.1.5 (`non-kahler-pluripotential-theory:D4902E5B`, permanent `2B3316345A4A`, lines 69–92); Corollary 11.1.10 (`non-kahler-pluripotential-theory:9CD9DB11`, permanent `2C05FFD39C6D`, lines 185–196); Example 11.1.12 (`non-kahler-pluripotential-theory:028A9E19`, permanent `F336FEED9D87`, lines 214–239) and its equation 11.1.13 (`non-kahler-pluripotential-theory:F1D489BD`, permanent `914CB776FFB8`, lines 227–236); Proposition 11.1.20 (`non-kahler-pluripotential-theory:0BFF54D7`, permanent `682711871907`, lines 308–325). The bounded-potential extension of Theorem 11.1.7, line 147, was **not inspected**.

## Precisely scoped new claim

Let (E=\mathbb C/(\mathbb Z+i\mathbb Z)), (X=E\times E), and take exactly the source's smooth forms
\[
 \beta_j=\frac{i}{2\pi}dz_j\wedge d\bar z_j,\qquad
 b(x_1)=2+\cos(2\pi x_1),\qquad
 \omega=\beta_1+b(x_1)\beta_2,\qquad
 B=\int_X\beta_1\wedge\beta_2>0.
\]
Write (\mathcal H_\omega=\{u\in C^\infty(X,\mathbb R):\omega+dd^cu>0\}) and (M(u)=\int_X(\omega+dd^cu)^2). Then **the full image**, over *all* smooth admissible potentials (not just the one-parameter cosine perturbations in Example 11.1.12), is exactly
\[
 \boxed{\quad M(\mathcal H_\omega)=(2B,6B).\quad}
\]
In particular
\[
 \inf_{u\in\mathcal H_\omega}M(u)=2B,\qquad
 \overline v_{\rm sm}(\omega)=\sup_{u\in\mathcal H_\omega}M(u)=6B,
\]
and neither extremum is attained. Both bounds are sharp through smooth positive admissible potentials. The result is a **new exact endpoint calculation**, not a second claim of the already audited general fact that non-pluriclosed surface mass ranges are open intervals (`POME-GAUD-SURFACE-VOLUME-RANGE-OPTIMIZERS-001`, 2026-11-01).

## Proof: an arbitrary potential is controlled by a positive circle density

We use only the printed normalization (dd^c=i\partial\bar\partial/(2\pi)) and compact Stokes integration by parts. Normalize Haar measure on each of the four real coordinate circles to total mass one. For (u\in\mathcal H_\omega), let
\[
 f(x_1)=\int_{(y_1,x_2,y_2)\in(\mathbb R/\mathbb Z)^3}
       u(x_1,y_1,x_2,y_2)\,dy_1\,dx_2\,dy_2.
\]
This is a smooth real one-periodic function. In the (\beta_1,\beta_2) frame, the diagonal coefficient of (\omega_u=\omega+dd^cu) in the first direction is
\[
 1+\partial_{z_1}\partial_{\bar z_1}u
 =1+\tfrac14(u_{x_1x_1}+u_{y_1y_1})>0.
\]
Averaging over the other three circles eliminates (u_{y_1y_1}) and gives
\[
 \rho(x_1):=1+\frac{f''(x_1)}4>0,\qquad
 \int_0^1\rho(x_1)\,dx_1=1.
\]
Thus **every** admissible smooth potential defines a strictly positive smooth probability density (\rho) on the (x_1)-circle. Mixed or off-diagonal second derivatives do not change the mass identity below.

Indeed (dd^c\omega=(b''/4)\beta_1\wedge\beta_2). The printed surface mass formula (Corollary 11.1.10), proved there by Stokes, gives
\[
 \begin{aligned}
 M(u)&=\int_X\omega^2+2\int_Xu\,dd^c\omega
       =4B+\frac B2\int_0^1 f(x)b''(x)\,dx\\
     &=4B+\frac B2\int_0^1f''(x)b(x)\,dx
       =2B\int_0^1 b(x)\rho(x)\,dx.\tag{*}
 \end{aligned}
\]
The second equality uses two periodic integrations by parts and the exact product-Haar normalization (\int_X g(x_1)\beta_1\wedge\beta_2=B\int_0^1g(x_1)dx_1). Since (1\le b\le3), with equality only at isolated circle points, and (\rho) is everywhere positive,
\[
 2B<M(u)<6B.
\]
These inequalities are strict even for unrestricted four-real-variable smooth potentials.

## Proof: every intermediate mass is attainable, and the endpoints are sharp

Conversely, let (\rho>0) be any smooth one-periodic function with (\int_0^1\rho=1). The mean-zero condition on (4(\rho-1)) gives a smooth real one-periodic solution to
\[
 f''=4(\rho-1).
\]
For example, integrate once and choose the additive constant in (f') to make the second primitive periodic; the derivatives match automatically at the endpoints. Put (u(z_1,z_2)=f(x_1)). Then
\[
 \omega_u=\rho(x_1)\beta_1+b(x_1)\beta_2>0,
\]
so this (u) is admissible and formula (*) applies. Hence the exact mass range coincides with (2B\int b\rho) as (\rho) varies through smooth strictly positive circle probability densities.

For (k>0) consider
\[
 \rho_k^+(x)=
 \frac{e^{k\cos(2\pi x)}}{\int_0^1e^{k\cos(2\pi t)}dt},
 \qquad
 \rho_k^-(x)=
 \frac{e^{-k\cos(2\pi x)}}{\int_0^1e^{-k\cos(2\pi t)}dt}.
\]
These smooth strictly positive densities concentrate respectively at the unique maximum (x=0) and minimum (x=1/2) of (b). The elementary concentration proof: for each fixed neighborhood of the extremum, (\cos(2\pi x)) is uniformly smaller outside than on a smaller neighborhood inside, so the outside-to-inside exponential mass ratio is (O(e^{-ck})). By bounded continuity of (b),
\[
 \int_0^1b\rho_k^+\longrightarrow3,\qquad
 \int_0^1b\rho_k^-\longrightarrow1.
\]
The associated (x_1)-dependent smooth admissible potentials have masses tending to (6B) and (2B). For any (m\in(2B,6B)), choose (k) so that (M(\rho_k^-)<m<M(\rho_k^+)), and choose (0<t<1) with
\[
 \rho=(1-t)\rho_k^-+t\rho_k^+,\qquad 2B\int b\rho=m.
\]
This is still smooth, strictly positive, and of unit integral; the periodic ODE above supplies the required (u\in\mathcal H_\omega). Thus **every** intermediate mass is realized, completing the proof.

**Normalization crosscheck with the printed example.** For the source's (u_t=t\cos(2\pi x_1)), (\rho_t=1-\pi^2t\cos(2\pi x_1)), and (*) yields
\[
 M(u_t)=2B\left(2-\frac{\pi^2t}{2}\right)=(4-\pi^2t)B,
\]
exactly equation 11.1.13. The source's restricted (|t|<\pi^{-2}) example exhibits only a proper subset of the full interval.

## Classification, prior-work separation, dependents and limitations

**Status/severity:** **low / verified conditional deduction**. The elementary torus calculation is complete given the printed (dd^c) and Stokes conventions, independently checked in the selected source lines. **No printed theorem or example is false.** The old generic open-interval finding `POME-GAUD-SURFACE-VOLUME-RANGE-OPTIMIZERS-001` is retained, not restated as a new result. No duplicate/canonicalization change is recommended.

**Proposed optional correction/addition (not made to the body):** after Example 11.1.12 or Proposition 11.1.20 add the sharp special-background equality (\overline v_{\rm sm}(\omega)=6B) and the open range, preserving the existing source attribution, labels and permanent tags. The directly affected dependent is the smooth upper mass in §11.1.20; §§12.2,12.15 variational-volume uses and §13.14 mass comparisons are **only candidate downstream applications**, not verified here. For singular/bounded potentials and the full non-pluripolar mass there is **no claim**, nor any use of approximation theorems. The passage from smooth strict potentials to bounded potentials in Theorem 11.1.7 line 147 is **deferred-by-user insofar as it invokes excluded regularization**, neither resolved nor certified.

**Actual coverage:** selected direct reading/normalization check of Lemma 11.1.2, Corollary 11.1.10, Example 11.1.12, Eq. 11.1.13 and Proposition 11.1.20 in already partly reviewed §11.1, plus relevant mass-polynomial line anchors. **First-time numbered sections: 0. Entirely certified numbered sections: 0.** The current main collection has **25 chapters / 747 numbered sections** by its existing direct ToC inventory. General analytic upper-volume, uniform bounded-potential, and full dependency-chain claims were not audited here. **No tests, project build, CI, browser check or formal verification were run.** All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved. Audit Markdown only, no main/source/registry/permanent-tag/site changes.
