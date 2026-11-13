# Equal-partition Hermitian normalization scalars on a flat complex two-torus

**Finding:** \`POME-HERM-EQUAL-PARTITION-SCALAR-SEPARATION-001\`  
**Classification:** low severity / **verified conditional deduction** (the explicit smooth calculation is unconditional; identifying it with the general normalization functional uses the scalar-uniqueness input of §11.33.2). **No printed result is false.**  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`, 2026-11-14.  
**Scope:** Chapter 11, §§11.32–11.34, with the closed-background comparison in §11.42. Demailly regularization and all user-deferred Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss subprogrammes are outside this review.

## Exact integrated locations and stable identifiers

| Statement | Integrated path and pinned blob | Source label and permanent tag | Physical lines |
| --- | --- | --- | --- |
| Standing positive-background/model hypotheses (§11.32) | \`docs/sections/normalization-and-weak-adjoint-measures/index.html\`, \`031b5d62d25d7ff03d95e4a14988399527cc946a\` | \`non-kahler-pluripotential-theory:75571769\`; \`7091FEDB43F0\` | 5–11 |
| Defining scalar equation (11.33.1) | \`docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html\`, \`fff86de757578ed2be369ba752123f62f3d31044\` | \`non-kahler-pluripotential-theory:19974F5F\`; \`9D47DB96B6E3\` | 9–22 |
| Scalar uniqueness and translation, Proposition 11.33.2 | same §11.33 blob | \`non-kahler-pluripotential-theory:6D175DAF\`; \`2770AB03C0D2\` | 26–51 |
| Smooth adjoint probability, Theorem 11.34.9 | \`docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html\`, \`a8afa97be049b56b6c7d18302499364022feaa39\` | \`non-kahler-pluripotential-theory:CDAC8220\`; \`7E60599DA339\` | 138–161 |
| **Closed**-background mass formula, Theorem 11.42.1 | \`docs/sections/normalization-and-weak-adjoint-measures--the-mass-determined-by-the-functional/index.html\`, \`9766d5ddf698ae153a6ba635ab9933d471356d67\` | \`non-kahler-pluripotential-theory:190967B6\`; \`1DCF668EBCCF\` | 7–48 |
| Nonclosed residual context, Example 11.42.4 | same §11.42 blob | \`non-kahler-pluripotential-theory:D749A384\`; \`0B7F3ACBCCC4\` | 74–81 |

## New self-contained smooth example

Fix the complex two-torus
\[
 X=(\mathbb C/(\mathbb Z+i\mathbb Z))^2,\qquad
 \omega_j=\frac i2 dz_j\wedge d\bar z_j,\quad
 \omega=\omega_1+\omega_2,\quad dV=\omega_1\wedge\omega_2.
\]
Thus \(\int_XdV=1\). Use the **Pome convention** \(dd^c=\frac i{2\pi}\partial\bar\partial\). Let
\[
 v=\cos(2\pi\operatorname{Re}z_1),\qquad
 a=2+v,\qquad
 \beta=a\omega,\qquad \varphi=0.
\]
The smooth form \(\beta\) is strictly positive and nonclosed, and \(\varphi=0\) meets the §11.32 model-reference conditions: \(P_\beta[0]=0\) and \(P_{\varepsilon\beta}(0)=0\) for every \(0<\varepsilon<1\). By direct differentiation,
\[
 dd^c v=-\pi v\,\omega_1,\qquad
 \beta+tdd^cv=(a-\pi tv)\omega_1+a\omega_2>0
 \quad(0<t<1/(2\pi)).
\]
Consequently \(u_t=tv\) is a smooth solution at the explicitly defined logarithmic density
\[
 F_t=\log\bigl(2a(a-\pi tv)\bigr),\qquad
 (\beta+dd^cu_t)^2=e^{F_t}dV
 \tag{A}
\]
with scalar \(c_\beta(F_t)=1\). Write \(F_0=\log(2a^2)\). The integrals are exact:
\[
 \int_Xa^2\,dV=4+\tfrac12=\tfrac92,\qquad
 \int_Xav\,dV=\tfrac12,
 \qquad
 Z_t:=\int_Xe^{F_t}\,dV=9-\pi t,\quad Z_0=9.
 \tag{B}
\]
Set
\[
 G_t=F_t+\log\frac9{9-\pi t}.
\]
Then \(G_t,F_0\) are both smooth and have **identical** exponential partition function
\[
 \int_Xe^{G_t}dV=\int_Xe^{F_0}dV=9,
 \tag{C}
\]
whereas the *same* smooth potential \(u_t\) solves the equation at \(G_t\) with scalar \((9-\pi t)/9\). The unique scalar and the translation rule from §11.33.2 therefore give
\[
 B_\beta(F_0)=0,\qquad
 B_\beta(G_t)=\log\left(1-\frac{\pi t}{9}\right)<0.
 \tag{D}
\]
This establishes **two distinct scalar values at exactly the same partition function on a fixed positive Hermitian background**, without singular poles, limiting procedures, or any regularization argument. In the smooth class the scalar is also unique directly: comparison at a maximum/minimum of the difference of two smooth solutions with the same density and constant scalar factors forces both inequalities between the factors. The general ordinary-type uniqueness is the separately recorded §11.33.2 input.

## Exact adjoint probability and first derivative

At \(F_0\), the solution is \(u=0\). The smooth logarithmic Monge–Ampère linearization is
\[
 Lh=\operatorname{tr}_\beta(dd^ch)
   =\frac{1}{4\pi a}\Delta_{\mathbb R^4}h .
\]
Its stationary probability is
\[
 \mu_0=\frac a{\int_X a\,dV}dV=\frac a2dV,
 \qquad \int_X a\,dV=2,
 \tag{E}
\]
because \(\int_X Lh\,a\,dV=(4\pi)^{-1}\int_X\Delta h\,dV=0\). It is unique: any stationary density \(p\) solves \(\Delta(p/a)=0\), hence \(p/a\) is constant on the connected torus. This agrees with Theorem 11.34.9. In contrast, the *Gibbs probability* one would obtain from the formula of Theorem 11.42.1 **without its closedness hypothesis** is
\[
 \frac{e^{F_0}}{Z_0}dV=\frac{2a^2}{9}dV\ne\frac a2dV.
 \tag{F}
\]
Indeed
\[
 G'_0=-\frac{\pi v}{a}+\frac{\pi}{9},
 \quad\int_XG'_0\frac{2a^2}{9}dV=0,\quad
 \int_XG'_0\frac a2dV=\frac{\pi}{9},
\]
while (D) yields \(B'_\beta(G_t)|_{t=0}=-\pi/9\). Thus the Gauduchon adjoint predicts the **correct nonzero first-order scalar response along an exactly equal-\(Z\) family**, and the closed-case Gibbs measure does not.

## Sharp scope, dependent statements, and proposed change

- **No false theorem:** Theorem 11.42.1 explicitly requires a **closed** background and is not contradicted; Theorems 11.33.2 and 11.34.9 remain correct. Example 11.42.4 concerns moving divisorial types with identical residual form; it does not supply the present equal-partition-function separation.
- **Why the assumption matters:** When the background is closed, Stokes and fixed singularity type give the constant top mass, and the scalar depends only on \(Z_F\); here \(dd^c\beta\ne0\), and even the smooth total mass in (B) varies linearly with the potential. Nonclosedness alone is not logically equivalent to failure in every dimension or every background; the present explicit example establishes failure in the allowed Hermitian class.
- **Dependencies:** Only the normalization scalar's uniqueness from §11.33.2 is imported to identify (A)–(D) with the full ordinary-type functional. Formula (E) is independently checked by elementary torus Laplacian calculus, with Theorem 11.34.9 used for the identification of the supporting probability. No general Monge–Ampère existence proof, NPP limit theorem, or excluded regularization programme is certified here.
- **Suggested optional insertion:** After Theorem 11.42.1, retain the closedness hypothesis and add this two-torus equal-\(Z\) example as a short nonclosed contrast. Do **not** patch the integrated source/registry or the published reading edition directly.

**Coverage:** §§11.32 (standing setup only), 11.33.1/2 (definition/translation and smooth uniqueness), 11.34.9 (stationary cofactor), 11.42.1/4 (hypothesis/contrast). Sections 11.33, 11.34 and 11.42 were previously sampled; the orientation-only §11.32 contains no proof. **+0 first proof-visited numbered sections, +0 whole-section certifications.** Current pinned ToC still 25 chapters / 747 numbered sections. No software build, test, CI or site publication.
