# Quadratic ellipticity loss, infinitely flat solution differences, and a duplicate equation anchor in §14.29

**Date:** 2026-11-07. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Findings:**
- `POME-MA-ANALYTIC-FLAT-NULL-JETS-001` — **low / verified conditional deduction** (complete *local* calculation from the printed explicit coefficients; existence of the global constructed forms relies on the stated construction).
- `POME-MA-ANALYTIC-ALIGN-ALIAS-001` — **low / genuine duplication of a rendered equation**, **not** a duplicate mathematical theorem. A possible display/MathJax failure is only a **candidate** pending an actual browser check.

## Precise main-version anchors

1. `docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html`, blob `2f00a81edc49855971bb3a6d774603ee5bbf40db`:
   - Theorem 14.29.1, physical lines 11–20, source `non-kahler-pluripotential-theory:3ADFF2BE`, permanent tag `DD001DBBE659`.
   - Coefficients (14.29.6)–(14.29.7), lines 56–73, joint source `non-kahler-pluripotential-theory:EDC080E0` / tag `14762A8A84D0`; triple (14.29.9), lines 76–89, source `:67BD1F7C` / tag `025CE4264442`; determinant equality (14.29.10), lines 92–105, source `:B91BE3E6` / tag `17DDFD1D68B2`.
   - Distinct standalone source `non-kahler-pluripotential-theory:2A55FD4B`, permanent `7FEE08922F33`, at physical line 107; its displayed mathematical content is *literally* the equation (14.29.7) already included at line 66.
   - The extension and perturbation, lines 109–165 (particularly (14.29.13), source `:BF19C5B7`, permanent `1FC5DA40EAF0`); zero-level description (14.29.15) lines 172–179 and inverse-density integrability (14.29.16) lines 199–206, sources `:E088E352` / `E3CA723897C6` and `:5D15E8A7` / `C72BCF7334A2`.
2. `docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html`, blob `7240d97e9192c70acf09f755ec90a5420bc11ef7`, §14.26.2: rank-one equations (14.26.3)–(14.26.6), sources `:48F853BE` / `6970E9123EB5`, `:7BBBEE11` / `71DFC7D0861C`, `:99713047` / `1C52D8C53893`, `:C78CE2C9` / `DE71ED12948B`. These fix the exact differential-form convention, not merely an analogous theorem elsewhere.
3. Actual chapter table of contents: `docs/chapters/monge-ampere-equations/index.html`, blob `7dadada1581ce063e940294be021f4f281a142e9`; §14.29 is the currently integrated section.

## New quantitative mathematical deduction

On the open set `U={A != 0, B != 0}` of `X=P(C² ⊕ C²)=P³`, put

\[
r=\log(|A|^2/|B|^2),\quad
P=dd^c\log|A|^2,\quad Q=dd^c\log|B|^2,\quad
R=dr\wedge d^cr.
\]

These are independent rank-one semipositive forms with `P^2=Q^2=R^2=0` and `P∧Q∧R>0`. The Fubini–Study metric is

\[
\omega_X=\sigma(r)P+\sigma(-r)Q+\sigma'(r)R,
\qquad \sigma(r)=\frac{e^r}{1+e^r}.
\]

In §14.29, the function `p(r)=exp(-1/(1-r²))` for `|r|<1`, extended by zero, and its derivative `q=p'` vanish **to infinite order** at `r=\pm1`. Write `z_b=(q²+2H_*²)^{1/2}>0`, `S_*=(r²+4p²+2z_b(1-r²)²)^{1/2}`, `x_b=(S_*-r)/2`, `y_b=(S_*+r)/2`. The two solution forms have coefficients

\[
A_0=(x_b-p)P+(y_b+p)Q+(z_b-q)R,\qquad
B_0=(x_b+p)P+(y_b-p)Q+(z_b+q)R
\]
on the central band. Their determinant products are equal exactly as printed in (14.29.10).

**Theorem for this explicit model.** Let `H_+={r=1}`, `H_-={r=-1}`, and let `d(x,H_\pm)` denote distance for any fixed smooth Riemannian metric on `X`. For either `G=A_0` or `G=B_0`, in a sufficiently small neighborhood of `H_+\cup H_-`, outside these hypersurfaces, its smallest eigenvalue relative to `omega_X` satisfies

\[
c\,d(x,H_+\cup H_-)^2\ \leq\
\lambda_{\min}(\omega_X^{-1}G)(x)
\ \leq\
C\,d(x,H_+\cup H_-)^2.
\]

Consequently its inverse, regarded as a measurable endomorphism `G^{-1}\omega_X` away from the zero set, has

\[
\|G^{-1}\omega_X\|\in L^s_{\mathrm{loc}}\quad\Longleftrightarrow\quad 0<s<\frac12
\]
in every neighborhood intersecting a zero level, relative to **any smooth positive volume form**. Globally on the compact `X` the same threshold holds. It is of weak `L^{1/2}` class at the critical endpoint, with two-sided tail estimate `Vol{||G^{-1}omega_X||>T}\asymp T^{-1/2}` for large `T`. In addition, **all jets** of `A_0-B_0` vanish on both `H_\pm` although the two forms are distinct; the smooth potentials differ by a function that, after subtracting a possibly different constant at each hypersurface, is infinitely flat there.

**Proof.** At the right endpoint `r=1`, `p,q=O(|r-1|^N)` for every `N`, `z_b(1)=\sqrt2 H_*(1)>0`, and `S_*\to1`. Rationalize the expression for the coefficient that vanishes:

\[
x_b=\frac{S_*^2-r^2}{2(S_*+r)}
 =\frac{2p^2+z_b(1-r^2)^2}{S_*+r}.
\]

Therefore

\[
\lim_{r\to1}\frac{x_b(r)\pm p(r)}{(r-1)^2}
=2z_b(1)>0.
\]

The other two coefficients tend to `1` and `z_b(1)>0`. Near the left endpoint `r=-1`, rationalization instead gives

\[
y_b=\frac{2p^2+z_b(1-r^2)^2}{S_*-r},\qquad
\lim_{r\to-1}\frac{y_b(r)\pm p(r)}{(r+1)^2}
=2z_b(-1)>0,
\]

and the other two coefficients tend to `1` and `z_b(-1)>0`. These limits are uniform tangentially because all coefficients depend only on `r`, and the forms `P,Q,R` are independent near the compact level hypersurfaces. Relative to their common rank-one coframe, `G` and `omega_X` are diagonal, so their generalized eigenvalues are exactly their respective `P,Q,R` coefficient ratios. The reference coefficients `sigma(r),sigma(-r),sigma'(r)` are strictly positive near `r=\pm1`. Hence precisely one eigenvalue has a quadratic zero and the other two remain uniformly positive. Since `dr\ne0` along the compact regular levels, `|r\mp1|\asymp d(x,H_\pm)`. This proves the claimed two-sided ellipticity estimate.

For every smooth volume form, a tubular chart has volume `J(t,\xi)dt\,d\xi` with `0<c_0<J<C_0` and `t=r\mp1`. Therefore `||G^{-1}omega_X||^s\asymp |t|^{-2s}` and its integral converges precisely for `2s<1`. The same comparison gives the weak endpoint distribution law by measuring the tube `|t|\lesssim T^{-1/2}`. Away from the two compact hypersurfaces both solution forms are positive definite; there is no other inverse singularity.

Finally `A_0-B_0=-2[p(P-Q)+qR]=-dd^cF`, with `F'(r)=2p(r)`. Every derivative of `p` and `q` vanishes at `r=\pm1`, so every derivative of this tensor difference vanishes there. The normalized potentials differ by `-F(r)` plus a constant; since `F` is constant on both outer intervals and is infinitely flat at their endpoints, the potential difference has the asserted infinite-order local constancy. Distinctness follows from `p>0` on the middle band. The same proof in `P^3\times P^{n-3}` gives exactly one transverse quadratic null eigenvalue and positive additional factors, for all `n\ge4`. \(\square\)

This calculation *sharpens the degeneracy geometry* of printed Theorem 14.29.1; it does **not** dispute the theorem, nor does it recertify its global patching and background construction. It is logically different from previously recorded exact distribution calculations for the scalar `f_*(t)`: it controls the **inverse of the solution form and its full flat jets**.

## Distinct rendered-equation duplication (no tag deletion)

Physical line **66** displays both labeled equations (14.29.6) and (14.29.7) in the shared `align` environment, with `x_b=(S_*-r)/2,\ y_b=(S_*+r)/2` as the second line. Physical line **107** displays the **same formula again** under the separate permanent tag `7FEE08922F33`, source `non-kahler-pluripotential-theory:2A55FD4B`; that second display is textually wrapped in `\\[\\begin{aligned}\\begin{align} ... \\end{align}\\end{aligned}\\]`. This is a **genuine duplicate rendered mathematical expression**, not evidence that two mathematically distinct statements are duplicates. The nested math environments are a **candidate** rendering fault, not a browser-tested failure.

**Proposed separately reviewable integration patch:** retain both source labels and both permanent tags, including all incoming links; place the additional tag/anchor on the existing second row of the display (or a non-rendered compatibility anchor) instead of showing the formula twice. Check MathJax output in a separate authorized rendering review before claiming a display failure. No change to (14.29.6), (14.29.7), scalar coefficient values or canonical mathematical content is proposed here.

## Status, affected dependents, and coverage discipline

- **Mathematics:** verified conditional deduction `POME-MA-ANALYTIC-FLAT-NULL-JETS-001`. The local theorem above is fully justified from explicit coefficients and rank-one decomposition. The **global existence** of the cited pair remains dependent on the full printed §14.29 proof (especially the product-preserving outer gluing and strictly positive background).
- **Reader duplication:** genuine rendered-expression duplication `POME-MA-ANALYTIC-ALIGN-ALIAS-001`, and **candidate** MathJax nesting issue only. Neither status means an error in Theorem 14.29.1.
- **Affected downstream comparisons:** §14.21.13's inverse-density uniqueness threshold, §14.29.15–16's quadratic zero/integrability, and any proposed elliptic regularity argument relying on inverse solution metrics being in `L^{1/2}`. The new form-inverse threshold does **not** alone prove, extend or refute such general theorems.
- **Precise coverage newly added:** §§14.29.6–10 coefficient limits, both zero strata, §14.29.13 potential adjustment, and comparison with §14.26.3–6; textual duplicate at main §14.29 line 107. Section §14.29 and §14.26 already partly audited. **0 first-visited sections / 0 whole-section certificates**; current ToC baseline **25 chapters / 747 numbered sections / 0 fully certified sections**. Previously registered errors/gaps/external dependencies/repairs remain unchanged. All user-excluded Demailly approximation/regularization, dedicated Bergman/weighted L²/Ohsawa–Takegoshi/multiscale/positivity-loss work stays **deferred-by-user**, not resolved.
- **Checks actually performed:** exact symbolic rationalization, endpoint limits, rank-one generalized eigenvalue comparison, one-dimensional transverse integrability. **No numerical computation, build, CI, website publication or formal verification.** No production source, adapter, body, registry, permanent tag or main-branch edits.
