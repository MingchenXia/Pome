# Sharp inhomogeneous weighted-cofactor energy stability

**Date:** 2026-11-01. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-GAUD-SURFACE-SHARP-TV-ENERGY-001` — **low / verified conditional deduction**. This is an additional theorem under an explicitly stated cofactor-closedness hypothesis, **not** a false printed theorem, a general degenerate-Monge–Ampère uniqueness theorem, or a production repair.

## Exact integrated source anchors

- `docs/sections/uniqueness-for-degenerate-equations/index.html`, main blob `0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208`, lines 7–26, Eq. **14.20.1**, source `non-kahler-pluripotential-theory:AA4FA8E3`, permanent tag `2EA7CA32AE91`: (dd^c w\wedge T=A^n-B^n). The original source uses the normalization (dd^c=i/(2\pi)\partial\bar\partial).
- `docs/sections/uniqueness-for-degenerate-equations--polarized-cofactors-and-propagation/index.html`, main blob `56645140ee2a5e1f97f3288e31ad9a48161e73e5`: Theorem **14.22.1** `non-kahler-pluripotential-theory:DC121A4C`, tag `919310C73DBE`, lines 13–30; the (w^2) product identity **14.22.5**, source `:02BFB727`, tag `A2BD70AF14EC`, lines 43–55; Proposition **14.22.13**, source `:9858A450`, permanent `F563CACF5D7D`, lines 165–188; displayed **14.22.14**, source `:D784A3BD`, permanent `475D4376A313`, lines 167–169; surface Corollary **14.22.15**, source `:F2E44751`, permanent `EAC3CF41BD99`, lines 190–202.
- `docs/sections/uniqueness-for-degenerate-equations--integral-rigidity-in-dimensions-two-and-three/index.html`, main blob `e67714c2fe599f71be40618f9586b6b31095275e`, Theorem **14.23.1**, source `non-kahler-pluripotential-theory:29282980`, permanent `AF9D036E600F`, lines 13–23, and surface Stokes discussion lines 37–65, **context only**.

## Newly verified statement: the unequal-data identity and best coefficient

Let (X) be a connected compact complex manifold of dimension (n\ge 2), (omega) a smooth Hermitian form, and (u,v\in C^2(X,\mathbb R)) such that (A=\omega+dd^c u\ge0), (B=\omega+dd^c v\ge0). Put (w=u-v), (T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}), and let (h>0) be continuous with (dd^c(hT)=0) in distributions. **The top powers need not agree.** Write (F=A^n-B^n), a signed real top-degree measure. Then

\[
\int_X hF=0,\qquad
\boxed{\mathcal E_h(w):=\int_X h\,dw\wedge d^cw\wedge T
=-\int_X h(w-c)F\quad(c\in\mathbb R),}
\]

and the sharp total-variation estimate is

\[
\boxed{0\le\mathcal E_h(w)\le
\frac{\operatorname{osc}_X w}{2}\int_X h\,|A^n-B^n|.}
\tag{*}
\]

**Proof.** The algebraic telescoping identity, requiring no closedness of (omega), gives (dd^cw\wedge T=F). Test the distribution (dd^c(hT)=0) successively against (w) and (w^2); (C^2) test functions are allowed by uniform (C^2)-smooth approximation because (hT) is continuous. The first test gives (\int hF=0). The second test, using (dd^c(w^2)=2w\,dd^cw+2dw\wedge d^cw), gives (0=2\int hwF+2\mathcal E_h(w)). Positivity of the ((n-1,n-1)) mixed cofactor and (dw\wedge d^cw=(i/(2\pi))\partial w\wedge\bar\partial w\ge0) proves the lower bound. Choose (c=(\sup_X w+\inf_X w)/2) and use (|w-c|\le\operatorname{osc}(w)/2) to prove (*). Note that (\int hF=0) is indispensable for this centered coefficient; assuming only (dd^c T=0) without the weight would not justify it for a different (h).

For **every compact pluriclosed Hermitian surface** (n=2), (dd^c\omega=0) implies (T=A+B=2\omega+dd^c(u+v)) and (dd^cT=0), so (h=1) is available for **all smooth semipositive pairs**, with no common-density or strictly-positive-density assumption. Thus the unweighted form of (*) is unconditional in this surface regime. When (F=0), the identity specializes to Proposition 14.22.13; the established density or orbit hypotheses remain necessary to infer constancy from vanishing energy.

## Sharpness even for strictly positive Kähler metrics

Let (X=E\times E), (E=\mathbb C/(\mathbb Z+i\mathbb Z)), and (\omega=\omega_1+\omega_2), (\omega_j=(i/2)\,dz_j\wedge d\bar z_j), normalized so (\int_X\omega_1\wedge\omega_2=1). Take (v=0), (u=\varepsilon f(x_1)) with (f\in C^\infty(\mathbb R/\mathbb Z)) and (1+\varepsilon f''/(4\pi)>0). Direct coefficient calculation gives

\[
A=(1+\varepsilon f''/(4\pi))\omega_1+\omega_2,\quad B=\omega_1+\omega_2,\quad
F=\frac{\varepsilon f''}{2\pi}\omega_1\wedge\omega_2,
\]
\[
\mathcal E_1(w)=\frac{\varepsilon^2}{2\pi}\int_0^1(f')^2\,dx,\quad
\|F\|_{\rm TV}=\frac{|\varepsilon|}{2\pi}\int_0^1|f''|\,dx.
\]

Consequently the ratio of the two sides in (*) is exactly
\[
\frac{\mathcal E_1}{\frac12\operatorname{osc}(w)\|F\|_{\rm TV}}
=\frac{2\int_0^1(f')^2}
{\operatorname{osc}(f)\int_0^1|f''|}\le1.
\]

Choose the periodic triangular profile (f_0(x)=2\min(x,1-x)) on ([0,1]) and convolve periodically with nonnegative smooth unit-mass bumps of radius (\delta<1/8). The smooth (f_\delta) satisfy (\int(f_\delta')^2\to4), (\operatorname{osc}(f_\delta)\to1), and (\int|f_\delta''|=8): indeed (f_0''=4\delta_0-4\delta_{1/2}) and the two smoothed supports are disjoint. Choose (arepsilon_\delta=\delta^2>0) (or smaller if needed), so (\varepsilon_\delta\|f_\delta''\|_\infty\to0), guaranteeing (A>0) and (B>0). The ratio tends to (2\cdot4/(1\cdot8)=1). Hence **the factor (1/2) cannot be decreased**, even in the smooth strictly positive Kähler surface subclass. This sharpness proof does not claim an exactly attained nonconstant smooth extremizer.

## Verdict, scope, and optional patch

- **Status:** low / **verified conditional deduction**; the weighted cofactor hypothesis is genuine in general dimensions, while on pluriclosed surfaces it is automatic with (h=1). The original Theorem 14.22.1, Proposition 14.22.13, Corollary 14.22.15, and Theorem 14.23.1 are **not disproved**.
- **Proposed correction/addition:** an optional new quantitative corollary after **14.22.15**, preserving original permanent tags and historical attribution. It controls the energy by the total-variation difference of potentially unequal Monge–Ampère measures; it does **not** imply a global (L^\infty) bound without extra coercivity/ellipticity. In higher dimensions, neither (dd^c\omega^{n-1}=0) nor mere Gauduchon normalization automatically supplies (dd^c(hT)=0); this must not be silently generalized.
- **Affected dependents:** the integral-energy comparison in §§14.22–14.23, smooth degenerate-density stability discussion §§14.20–14.25, and surface Gauduchon background comparisons in chapter 11. No theorem-proving dependency on the user-excluded Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme.
- **Actual reviewed scope:** direct new computation of unequal-RHS extension of **14.20.1**, **14.22.5**, **14.22.13–15** and the flat torus sharpness family; §14.22.1 weighted identity and §14.23.1 surface Stokes read for exact assumptions. These sections had prior **selected** checks, and this report is **not** first section coverage, an entire-section certification, a full smooth uniqueness theorem certification, or a software/project build. No source/registry/canonicalization/tag/main edits. Current main ToC: **25 chapters, 747 numbered sections, zero fully certified mathematical sections**. All excluded topics remain **deferred-by-user**, not resolved.
