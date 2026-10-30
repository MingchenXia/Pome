# Quadratic boundary data: exact spectral Dirichlet envelope and strict concavity

**Date:** 2026-10-31. **Stable finding:** POME-BT-QUADRATIC-DIRICHLET-EIGENVALUE-001. **Severity:** low. **Status:** verified conditional deduction; no false printed theorem or general proof repair. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Proposed findings only on `review/mathematical-audit`.

## Precisely inspected reading-edition statements

The integrated source is `docs/sections/bedford-taylor-products-and-local-capacity--the-homogeneous-dirichlet-problem-and-balayage/index.html`, main blob `928f3d3e36f2d03a42623b91487ecec7d189e6c7`, parent section 7.7 tag `22EC1FF0BE9D`.

| Item | Original source label / permanent tag | Physical HTML lines |
| --- | --- | --- |
| Lemma 7.7.2, Hessian determinant formula | `foundations-of-pluripotential-theory:2473754C` / `0E5A3E632224` | 58–69; proof 75–99 |
| Theorem 7.7.4, homogeneous Dirichlet existence and uniqueness | `foundations-of-pluripotential-theory:FEE18534` / `9181532558D7` | 104–108; proof 113–135 |
| Corollary 7.7.5, ball balayage | `foundations-of-pluripotential-theory:A118D214` / `2E8B947536C1` | 140–154 |
| Definition 7.7.6, maximality | `foundations-of-pluripotential-theory:4A1DBBE1` / `FD8547B922C9` | 160 |
| Theorem 7.7.7, maximality iff vanishing mass | `foundations-of-pluripotential-theory:5C75D8E4` / `BCFDDA1FCB7A` | 165–174 |

The uniqueness/comparison input is Theorem 7.3.11, source `foundations-of-pluripotential-theory:A7DD3972`, permanent tag `D0AF90DDC7A5`, line **304** of `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html`, main blob `96a9e39e85fab5774ebdac0c6d9d006338a4e42c`. Its general proof chain is **not** certified by this review. This run freshly checked the maximality proof steps in §7.7.6–7 (especially the boundary comparison in line 171 and global ball replacement in line 173), while the prior §7.7.4/5 review is retained without recounting it.

## Exact formula for quadratic boundary data

Let $B=\{z\in\mathbb C^n:|z|<1\}$, $n\geq 1$, and let $A=A^*$ be an arbitrary complex Hermitian $n\times n$ matrix (it need not be semipositive). Fix a holomorphic polynomial $P$ of degree at most two and a real constant $c$, and put

$$
\varphi_A(z)=z^*Az+2\operatorname{Re}P(z)+c
\qquad (z\in\partial B).
$$

Set $\lambda(A)=\lambda_{\min}(A)$. Then the homogeneous Bedford–Taylor Dirichlet solution on $B$ is

$$
\boxed{H_A(z)=z^*Az+2\operatorname{Re}P(z)+c
             +\lambda(A)(1-|z|^2).}
$$

**Direct verification.** On $\partial B$, the final term vanishes. The real part of $P$ is pluriharmonic, so the Hermitian complex Hessian of $H_A$ has the same spectrum as $A-\lambda(A)I$, which is positive semidefinite and singular. Thus $H_A$ is a globally smooth plurisubharmonic function on $B$, and

$$
(dd^c H_A)^n=\frac{n!}{\pi^n}
 \det(A-\lambda(A)I)\,dV_{2n}=0,
$$

with the normalization $dd^c=i\partial\bar\partial/(2\pi)$. Its boundary values are precisely $\varphi_A$. The **uniqueness** assertion of integrated Theorem 7.7.4 (whose comparison proof uses §7.3.11) identifies this explicit solution with the Perron envelope. The model verification itself requires no Demailly approximation or any excluded proof programme. In $n=1$ the Hessian vanishes, recovering the harmonic solution.

## Sharp interpolation gap: Perron concavity, not affinity

Keep $P,c$ fixed, and let $A,B$ be Hermitian. Write $A_t=(1-t)A+tB$, where $0\leq t\leq1$. Linearity of the boundary values and the preceding formula give an **identity at every interior point**:

$$
\begin{aligned}
&H_{A_t}(z)-\bigl((1-t)H_A(z)+tH_B(z)\bigr)\\
&\quad=\Delta_t(A,B)(1-|z|^2),\\
&\Delta_t(A,B)=\lambda_{\min}(A_t)
 -(1-t)\lambda_{\min}(A)-t\lambda_{\min}(B)\geq0.
\end{aligned}
$$

The inequality follows by minimizing the Rayleigh quotient:
$\langle Av,v\rangle\geq\lambda_{\min}(A)$ and
$\langle Bv,v\rangle\geq\lambda_{\min}(B)$ for each unit $v$.
For $0<t<1$, equality holds **if and only if** the minimal-eigenvalue eigenspaces of $A$ and $B$ contain a common nonzero vector. Indeed, take any unit minimizing eigenvector for $A_t$. Equality in the weighted sum of two nonnegative Rayleigh gaps with strictly positive weights forces both gaps to vanish. Conversely a common minimum eigenvector realizes equality.

**Explicit strict case.** In complex dimension two choose
$A=\operatorname{diag}(0,1)$, $B=\operatorname{diag}(1,0)$, $P=c=0$ and $t=\frac12$. Then $H_A=|z_2|^2$ and $H_B=|z_1|^2$, whereas the averaged boundary data are identically $\frac12$ and $H_{(A+B)/2}=\frac12$. Consequently

$$
H_{(A+B)/2}(z)-\frac{H_A(z)+H_B(z)}2
=\frac{1-|z|^2}{2}>0
\qquad(z\in B).
$$

For **arbitrary continuous** boundary data $\varphi,\psi$, rather than only these quadratics, the Perron envelope is concave:

$$
H_{(1-t)\varphi+t\psi}
\geq(1-t)H_\varphi+tH_\psi.
$$

The right-hand side is a plurisubharmonic competitor with the correct boundary data, so the inequality follows from the envelope characterization. This concavity, which is strict for the displayed quadratic pair, is **not** the previously registered sup-norm boundary isometry `POME-BT-PERRON-ISOMETRY-001`; the two findings are logically distinct.

## Exact quadratic balayage

If $A\geq0$, define the entire smooth psh function
$u(z)=z^*Az+2\operatorname{Re}P(z)+c$. In any open $\Omega$ with $\overline B\subset\Omega$, the ball replacement supplied by Corollary 7.7.5 is exactly

$$
\widehat u(z)=
\begin{cases}
u(z)+\lambda_{\min}(A)(1-|z|^2),&|z|<1,\\
u(z),&z\in\Omega\setminus B.
\end{cases}
$$

Its inside has zero top Bedford–Taylor mass, its trace equals $u$ on $\partial B$, and global plurisubharmonicity follows from the already printed ball-gluing assertion. We make **no** claim that there is no boundary-supported current created by gluing.

## Disposition, dependencies, and coverage

Theorem 7.7.4 and Theorem 7.7.7 remain **correct in the mathematical steps checked**. The new formula is an exact independent model calculation, but its **unique-Perron identification** and the global balayage interpretation remain **conditional on the existing comparison/gluing results**. Theorem 7.3.11 is a genuine internal dependency, not a new external quotation or a certified proof. The model is a **verified conditional deduction**, neither a false theorem nor a complete repair.

An optional insertion immediately after Theorem 7.7.4 could record this explicit family, its nonaffinity and the gluing example, keeping the original source attribution and permanent labels. Affected interpretative dependents include the maximality test §7.7.7 and relative extremal/obstacle constructions in §5.47. **No modification** to the manuscript, proof registry, canonicalization, permanent tags or production `main` is proposed as already implemented.

**Actual new coverage:** selected §7.7.4 and §7.7.5 comparison, **fresh specific §7.7.6–7.7.7 maximality proof inspection**, §7.3.11 only a conditional comparison statement. This does **not** certify a whole numbered section, upstream Bedford–Taylor theory or the entire collection. The chapter/section matrix remains **25 chapters, 747 current ToC sections, zero wholly certified mathematical sections**. The companion standard-library exact rational check `mathematical-audit/checks/check_quadratic_dirichlet_spectral.py` passed **five** diagonal matrix sanity checks; no project build, CI, website publication or formal verification was performed. All prior findings persist unchanged. Demailly approximation/regularization and the Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes remain **deferred-by-user** without review or certification.
