# Two separated Newtonian balls: quantitative interaction of equilibrium charges

**Finding ID:** `POME-CLASS-TWO-BALL-CAPACITY-INTERACTION-001`  
**Date:** 2026-11-15  
**Severity / classification:** low / **verified conditional deduction**. The printed theorems are **not refuted**. This is a new independently checked two-conductor quantitative consequence of the indicated capacity and domination principles, not a certification of their full upstream proofs.

## Reviewed repository evidence

- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (freshly read on 2026-11-15).
- **Integrated reading edition:** `docs/sections/polar-sets-capacity-and-sweeping/index.html`, Git blob `aa814f26482e8ed27e51c945e9202c797449158b`.
- **Section permanent tag:** `AEB997E884B4` (§4.3).
- **Theorem 4.3.7:** source `classical-potential-theory:5388371B`, permanent `ABDF7610F7B2`; statement / variational formula at **physical lines 60–69**, proof of greatest-potential property and mass reciprocity at **74–79**, strong subadditivity at **81–82**, and Choquet/polar continuation at **83–94**.
- **Theorem 4.3.10:** source `classical-potential-theory:FA6C8523`, permanent `C4F5D8B270EB`; domination statement at **121–122**, proof at **127–130**.
- **Convention:** `G_{\mathbb R^d}(x,y)=\kappa_d |x-y|^{2-d}` for a positive kernel constant `\kappa_d`; the argument is invariant under its normalization. We use a **Greenian and admissible** whole space `\Omega=\mathbb R^d`, necessarily `d\ge3`. This does **not** concern planar logarithmic capacity.

## Quantitative assertion

Fix an integer `d\ge3`, radius `r>0`, centers `c_1,c_2\in\mathbb R^d`, and distance `R=|c_1-c_2|>2r`. Let `K_i=\overline{B(c_i,r)}`, `K=K_1\cup K_2`, and write `C_r=C(K_i)=r^{d-2}/\kappa_d`. Then

```text
       2 C_r                           2 C_r
 -----------------------  <= C(K) <= -----------------------
 1 + (r/(R-r))^(d-2)                 1 + (r/(R+r))^(d-2).
```

In particular `C_r<C(K)<2C_r`. For fixed `d\ge3,r>0` as `R\to\infty`,

```text
 C(K) = 2 C_r - 2 C_r (r/R)^(d-2)
        + O_d(C_r [ (r/R)^(d-1) + (r/R)^(2d-4) ]).
```

Equivalently the leading negative interaction term is exactly
`-2\kappa_d C_r^2 R^{2-d}`. The coefficient 2 is determined by **matching lower and upper bounds**; no exact finite-distance formula is asserted.

## Complete calculation

**(1) The single-ball equilibrium measure.** Let `\sigma_{c,r}` be normalized Euclidean surface-area measure on `S(c,r)`. Rotational symmetry gives a radial Newtonian potential `U(\rho)=G\sigma_{c,r}`. Off the sphere it is harmonic. On `\rho<r`, a radial harmonic function regular at the center is constant; on `\rho>r`, harmonicity, decay at infinity and unit total mass give `U(\rho)=\kappa_d\rho^{2-d}`. The potential is continuous across the sphere: its local singularity is integrable against the `(d-1)`-dimensional sphere measure, uniformly in a neighborhood of the sphere. Therefore `U(\rho)=\kappa_d r^{2-d}` for `\rho\le r`. Consequently the positive measure
`\eta_{c,r}=C_r\sigma_{c,r}`, `C_r=r^{d-2}/\kappa_d`, has

```text
 G eta_{c,r}(x) = 1                          if |x-c| <= r,
                  (r/|x-c|)^(d-2)           if |x-c| >= r.
```

It is an admissible mass-`C_r` competitor for the variational capacity formula. Conversely, for any positive `\lambda` supported on `\overline B(c,r)` with `G\lambda\le1`, positivity, Tonelli and symmetry give
`\lambda(K_i)=\int G\eta_{c,r}\,d\lambda=\int G\lambda\,d\eta_{c,r}\le C_r`.
Thus the displayed `C_r` is *exactly* the capacity with the chosen Green normalization. No assertion about arbitrary boundary measures is used here.

**(2) Lower bound.** Set `\eta_i=\eta_{c_i,r}` and `b=(r/(R-r))^{d-2}<1`. On `K_i`, `G\eta_i=1` and `G\eta_{3-i}(x)=(r/|x-c_{3-i}|)^{d-2}\le b`. Hence `\lambda=(\eta_1+\eta_2)/(1+b)` has `G\lambda\le1` on `K`. In `\mathbb R^d\setminus K`, the same potential is harmonic, continuous at `\partial K`, and tends to zero at infinity; the exterior maximum principle gives `G\lambda\le1` globally. (Theorem 4.3.10 also gives this conclusion.) Therefore the Theorem 4.3.7 variational formula yields
`C(K)\ge\lambda(K)=2C_r/(1+b)`.

**(3) Upper bound.** Let `\nu=\nu_1+\nu_2` be the capacity measure of `K`, with each `\nu_i` supported on `K_i`, and `m_i=\nu_i(K_i)`. Theorem 4.3.7 gives `G\nu\le1` and `m_1+m_2=C(K)`. By reciprocity and the exact single-ball potential,

```text
 int G nu d eta_i = int G eta_i d nu
                   = m_i + int_(K_(3-i)) G eta_i d nu_(3-i).
```

For `y\in K_{3-i}` one has `|y-c_i|\le R+r`, so `G\eta_i(y)\ge a:=(r/(R+r))^{d-2}>0`. Since `G\nu\le1`,
`m_i+a m_{3-i}\le\int 1\,d\eta_i=C_r`.
Adding the inequalities gives
`(1+a)C(K)\le2C_r`, as claimed. Notice that integrating against the *known ball charge* avoids an unjustified assumption that the unknown union equilibrium charge is uniformly distributed on each sphere.

**(4) Asymptotics and strictness.** Put `q=(r/R)^{d-2}`, `h=r/R\to0`. Uniformly for fixed integer `d\ge3`,
`a=q(1+h)^{-(d-2)}=q+O_d(qh)` and `b=q(1-h)^{-(d-2)}=q+O_d(qh)`.
Both reciprocal bounds equal
`2C_r[1-q+O_d(qh+q^2)]`, giving the stated exact first interaction coefficient. Because `0<a<b<1` for `R>2r`, their lower and upper capacity bounds imply `C_r<C(K)<2C_r` without an assumption of additivity or equality in strong subadditivity.

## Audited dependency logic and limits of the check

- Directly rechecked the *precise hypotheses* and the positivity / Tonelli reciprocity used in the integrated **Theorem 4.3.7**, physical lines 61–77, and the compact-support, everywhere-finite setting needed to invoke **Theorem 4.3.10**, lines 122–130. For these smooth spherical measures, domination can alternatively be replaced by the exterior maximum principle, making the lower bound independent of the delicate general Lusin restriction argument at line 130.
- A genuine test of **nonadditivity**: despite the ordinary strong subadditivity `C(K_1\cup K_2)\le C(K_1)+C(K_2)`, interaction is strictly negative and has the displayed sharp leading order. This does not contradict any printed Pome statement.
- The general polar boundary minimum theorem, full Choquet extension, arbitrary-potentials reduction theorem, and Lusin continuous-potential decomposition **were not audited transitively**. The upper bound uses the printed variational existence statement as an established conditional input. No statement about infinite-dimensional, noncompact, or directed-net capacity convergence follows.
- **No proposed source repair**: retain both original statements, source attribution, permanent tags, and their hypotheses. The optional mathematical addition is this separate two-ball quantitative example, not a rewritten or canonicalized source theorem.
- **Affected dependencies:** §4.3.7 equilibrium/capacity reciprocity and §4.3.10 potential domination, as benchmark examples for their downstream Newtonian capacity, balayage, and energy estimates; no certification of those downstream arguments.
- User-excluded Demailly regularization/approximation and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme: **deferred-by-user**, not opened, resolved, or certified.

**Scope count:** §4.3 was previously partly visited; **0 newly first-visited numbered sections, 0 whole-section certifications**, current main table of contents 25 chapters / 747 sections. No project tests, build, CI, website publication or production source/registry edit was performed.
