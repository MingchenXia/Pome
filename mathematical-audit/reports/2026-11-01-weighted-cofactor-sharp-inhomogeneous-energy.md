# Sharp inhomogeneous weighted-cofactor energy stability

**Date:** 2026-11-01. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Finding:** **POME-GAUD-SURFACE-SHARP-TV-ENERGY-001 — low / verified conditional deduction**. The original printed theorems are not asserted to be false. This is an optional quantitative corollary with a genuine general-dimensional hypothesis and an unconditional pluriclosed-surface specialization.

## Exact integrated source anchors

- **14.20.1**, at docs/sections/uniqueness-for-degenerate-equations/index.html, main blob **0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208**, physical lines 10–23, source **non-kahler-pluripotential-theory:AA4FA8E3**, permanent **2EA7CA32AE91**: the algebraic polarization identity.
- **14.22.1**, at docs/sections/uniqueness-for-degenerate-equations--polarized-cofactors-and-propagation/index.html, main blob **56645140ee2a5e1f97f3288e31ad9a48161e73e5**, lines 13–30, source **non-kahler-pluripotential-theory:DC121A4C**, permanent **919310C73DBE**: positive continuous weight and cofactor closedness. Its equation **14.22.5**, source **:02BFB727**, permanent **A2BD70AF14EC**, lines 43–55 gives the exact square product rule.
- **14.22.13–15** in the same file, lines 165–202: Proposition source **non-kahler-pluripotential-theory:9858A450**, permanent **F563CACF5D7D**; equation 14.22.14 source **:D784A3BD**, permanent **475D4376A313**; Corollary source **:F2E44751**, permanent **EAC3CF41BD99**. These assume *equal* top measures; the new deduction below does not.
- **14.23.1**, at docs/sections/uniqueness-for-degenerate-equations--integral-rigidity-in-dimensions-two-and-three/index.html, main blob **e67714c2fe599f71be40618f9586b6b31095275e**, source **non-kahler-pluripotential-theory:29282980**, permanent **AF9D036E600F**, lines 13–65: supporting Stokes calculation only, not recertified.

Throughout use $dd^c=(i/(2\pi))\partial\bar\partial$ and $dw\wedge d^cw=(i/(2\pi))\partial w\wedge\bar\partial w$, as in the integrated equations.

## A new exact identity for *unequal* Monge–Ampère measures

Let $X$ be a connected compact complex $n$-fold, $n\ge 2$, let $\omega$ be a smooth Hermitian form, and let $u,v\in C^2(X,\mathbb R)$ satisfy
\[
A:=\omega+dd^cu\ge 0,\qquad B:=\omega+dd^cv\ge0.
\]
Put $w=u-v$, $T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}$, and assume there is a **continuous** $h>0$ with $dd^c(hT)=0$ in the sense of distributions. Set the signed top-degree measure $F:=A^n-B^n$; **do not assume $F=0$**. Then
\[
\int_X hF=0,\qquad
\boxed{\mathcal E_h(w):=\int_X h\,dw\wedge d^cw\wedge T
=-\int_X h(w-c)F\quad\text{for every }c\in\mathbb R.}
\]
Moreover,
\[
\boxed{0\le \mathcal E_h(w)\le
\frac{\operatorname{osc}_X w}{2}
\int_X h\,|A^n-B^n|.}\tag{1}
\]
Here the right-hand integral is the **weighted total variation of the signed measure**, not the absolute difference of its total masses.

**Self-contained proof of the new deduction.** Polynomial polarization, valid without $d\omega=0$, yields
\[
dd^cw\wedge T=(A-B)\wedge T=A^n-B^n=F.
\]
Test $dd^c(hT)=0$ first against $w$, then against $w^2$. These tests are valid for $C^2$ functions by approximation in the $C^2$ norm by smooth functions: $hT$ has continuous coefficients, so the pairing is continuous in this norm. The first test gives $\int hF=0$. The product rule
\[
dd^c(w^2)=2w\,dd^cw+2dw\wedge d^cw
\]
then yields $0=2\int hwF+2\mathcal E_h(w)$. Since both $T$ and $dw\wedge d^cw$ are positive in the requisite bidegrees, $\mathcal E_h(w)\ge0$. Subtract any constant from $w$ using $\int hF=0$. The optimal centering $c=(\sup w+\inf w)/2$ obeys $|w-c|\le\operatorname{osc}(w)/2$, giving (1). The closedness assumption applies to **$hT$**; it must not be weakened to $dd^cT=0$ for an arbitrary unrelated $h$.

**Unconditional surface case.** For any compact pluriclosed Hermitian **surface**, $dd^c\omega=0$ and $n=2$ imply
\[
T=A+B=2\omega+dd^c(u+v),\qquad dd^cT=0.
\]
Consequently $h=1$ is valid for **every** smooth semipositive pair, regardless of whether $A^2$ and $B^2$ coincide or vanish somewhere. In particular, the unweighted inequality in (1) requires no nondegeneracy of their densities. If $F=0$, the result reduces to the printed energy identity of Proposition 14.22.13. Vanishing energy alone does not make $w$ constant where $T$ is degenerate; the original sufficient density/orbit conditions remain necessary for that deduction.

## The coefficient $1/2$ is sharp, even on smooth Kähler surfaces

Take $X=E\times E$, $E=\mathbb C/(\mathbb Z+i\mathbb Z)$, with $\omega=\omega_1+\omega_2$, $\omega_j=(i/2)dz_j\wedge d\bar z_j$, and $\int_X\omega_1\wedge\omega_2=1$. Set $v=0$, $u=\varepsilon f(x_1)$ where $f$ is smooth and real periodic of period one. If $1+\varepsilon f''/(4\pi)>0$, both $A$ and $B$ are strictly positive. Direct computation gives
\[
A=\left(1+\frac{\varepsilon f''}{4\pi}\right)\omega_1+\omega_2,\quad
B=\omega_1+\omega_2,\quad
F=\frac{\varepsilon f''}{2\pi}\omega_1\wedge\omega_2,
\]
\[
\mathcal E_1(w)=\frac{\varepsilon^2}{2\pi}\int_0^1(f')^2\,dx,\qquad
\|F\|_{\mathrm{TV}}=\frac{|\varepsilon|}{2\pi}\int_0^1|f''|\,dx.
\]
Therefore the ratio between the left and right sides of (1) is
\[
R(f)=\frac{2\int_0^1(f')^2\,dx}
{\operatorname{osc}(f)\int_0^1|f''|\,dx}.
\]
Consider the periodic triangular function $f_0(x)=2\min(x,1-x)$ for $x\in[0,1]$. In the distributional sense $f_0''=4\delta_0-4\delta_{1/2}$. Convolve periodically with a nonnegative $C^\infty$ unit-mass bump $\rho_\delta$, supported within circle distance $\delta<1/8$, and put $f_\delta=\rho_\delta*f_0$. Then the two terms of
\[
f_\delta''=4\rho_\delta(x)-4\rho_\delta(x-1/2)
\]
have disjoint supports, so $\int_0^1|f_\delta''|=8$ **exactly**. Also $\operatorname{osc}(f_\delta)\to1$ and $\int_0^1(f_\delta')^2\to4$, by elementary uniform/L² convergence under convolution. Choose $\varepsilon_\delta=\delta^2>0$ with a fixed-scale mollifier, so $\|f_\delta''\|_\infty=O(\delta^{-1})$ and $1+\varepsilon_\delta f_\delta''/(4\pi)>0$ for small $\delta$. Thus $A_\delta,B_\delta$ remain smooth strictly positive Kähler forms, while $R(f_\delta)\to 2\cdot4/(1\cdot8)=1$. No universal coefficient smaller than $1/2$ works, even in the strictly positive Kähler surface subclass. This constructs **asymptotic sharpness**, not a nonconstant smooth equality case.

## Mathematical verdict, coverage and proposed insertion

**Severity/status:** low / **verified conditional deduction**. No printed theorem is disproved; no source proof is labeled repaired. The useful optional addition is a quantitative corollary after Corollary **14.22.15**, retaining original tags and historical attribution and recording the general cofactor-closedness assumption explicitly. In dimensions above two, the Gauduchon condition $dd^c\omega^{n-1}=0$ does **not** automatically imply $dd^c(hT)=0$; no such generalization is claimed. Likewise, inequality (1) is an energy control, **not** a global $L^\infty$ uniqueness/stability theorem without additional ellipticity or coercivity.

**Affected dependents:** energy and degenerate-density comparison in §§14.20–14.25, and pluriclosed surface energy comparisons in chapter 11. **Actually examined:** the algebraic identity 14.20.1, square rule 14.22.5, weighted argument of 14.22.1, equal-density comparison 14.22.13–15, and the relevant surface Stokes passages of 14.23.1. These sections were previously sampled: this is **additional selected proof-level review**, not first coverage and not a complete theorem or section certification. **Main table of contents remains 25 chapters / 747 numbered sections / zero completely mathematically certified sections**. No project build, CI, formalization, publication, or source/registry/canonicalization/permanent-tag/main edits. All Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, never resolved or certified by this report.
