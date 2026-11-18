> **Overlap correction (2026-11-18):** The conceptual phenomenon here is **NOT a newly discovered independent counterexample**. It was already recorded as `POME-HESS-GAUD-TRACE-SECOND-MASS-001` in `mathematical-audit/reports/2026-11-03-gauduchon-trace-versus-second-hessian-mass.md`, which gave a Gauduchon three-torus with stationary but varying **m=2** mass, and as `POME-HERM-BALANCED-MASS-SADDLE-001` in `mathematical-audit/reports/2026-11-04-balanced-hermitian-mass-saddle-on-three-torus.md`, which used the **same b=exp(cos), c=1/b, f=c cos** geometry for **m=3** mass. The calculation below is an exact **m=2 coefficient cross-check on that already known family**, not a new conceptual failure or new coverage. **Ledger classification corrected to genuine duplication of the conceptual finding**; its separately computed numerical wedge coefficient remains mathematically verified. It must **not** be counted as a newly discovered theorem or new distinct counterexample. Neither earlier ID is replaced or resolved.

# Gauduchon is not enough: a stationary but nonconstant intermediate Hessian mass

**Date:** 2026-11-18. **Finding ID:** `POME-HESS-GAUDUCHON-FIRSTVAR-NOT-MASSCONST-001`. **Severity:** low. **Status:** **genuine duplication of an already recorded conceptual boundary**, with a separately verified m=2 numerical cross-check; not an independent new finding, confirmed error, or proposed repair.

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit-only branch:** `review/mathematical-audit`.

## Exact reading-edition anchors and scope

- `docs/sections/complex-hessian-equations/index.html`, main blob `5331b937ccdaba51f1ec006d5e72dc84f7addfbf`, physical line 7: Chapter 8 assumes a connected compact Hermitian n-fold with **2 <= m < n**. This example takes **n=3, m=2**.
- `docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html`, main blob `580d3bc2b10ebd01d880b2a31fc6930436570aac`. Lemma **8.13.1**, source `non-kahler-pluripotential-theory:A6052F07`, permanent `69692CE9985B`, lines **19–38**, and its total-mass identity **8.13.2**, source `non-kahler-pluripotential-theory:412E15D4`, permanent `B8626F362B85`, lines **21–25**. Theorem **8.13.4**, source `non-kahler-pluripotential-theory:776C8B26`, permanent `53F870DE5980`, lines **69–123**, especially polynomial/polarization proof **97–120**. Example **8.13.5**, source `non-kahler-pluripotential-theory:870AB319`, permanent `0DB9D80DE230`, lines **128–152**.
- The comparison implications in Theorem 8.13.4 were checked as *conditional* deductions from earlier locality and mixed-mass inputs; no claim to have certified those upstream products or all of §8.13.

## Exact m=2 cross-check of an **already documented** unprinted weakening

On the compact flat complex three-torus
\[
X=(\mathbb C/(\mathbb Z+i\mathbb Z))^3,\qquad
\beta_j=\frac{i}{2\pi}dz_j\wedge d\bar z_j,\quad
B=\int_X\beta_1\wedge\beta_2\wedge\beta_3>0,
\]
let \(\varepsilon>0\), with all real \(x_j\) of period one, and set
\[
c(x_1)=e^{-\varepsilon\cos(2\pi x_1)},\quad b(x_1)=c(x_1)^{-1},
\qquad \omega=\beta_1+b\beta_2+c\beta_3 .
\]
This is a smooth strictly positive Hermitian metric. The book's normalization \(dd^c=i\partial\bar\partial/(2\pi)\) implies
\[
dd^c h(x_1)=\tfrac14h''(x_1)\beta_1.
\]
Since \(bc\equiv1\),
\[
\omega^2=2b\beta_1\beta_2+2c\beta_1\beta_3+
             2\beta_2\beta_3,
\qquad \boxed{dd^c\omega^2=0},
\]
where juxtaposition denotes wedge products. On the other hand,
\[
dd^c\omega=\tfrac14b''\beta_1\beta_2+
              \tfrac14c''\beta_1\beta_3\ne0.
\]
Thus the background is **Gauduchon but not pluriclosed**, and it lies exactly inside Chapter 8's scope.

Define the smooth periodic test potential
\[
f(z)=c(x_1)\cos(2\pi x_2).
\]
For all sufficiently small real \(t\), \(\omega+t dd^cf>0\), hence \(tf\) is strictly admissible. Write
\[
M(t)=\int_X (\omega+t dd^cf)^2\wedge\omega.
\]
The exact quadratic polynomial and Stokes identity are
\[
M(t)=\int_X\omega^3+
  2t\int_X dd^cf\wedge\omega^2+
  t^2\int_X(dd^cf)^2\wedge\omega,
\qquad
\int_Xdd^cf\wedge\omega^2=\int_Xf\,dd^c\omega^2=0.
\]
In fact **the linear variation vanishes for every smooth real direction** \(f\), not just our choice, because \(dd^c\omega^2=0\). The second coefficient need not vanish. By Stokes,
\[
\begin{aligned}
J&=\int_X(dd^cf)^2\wedge\omega
 =\int_X f\,dd^cf\wedge dd^c\omega\\
 &=-\frac{\pi^2 B}{8}\int_0^1 c(x)^2c''(x)\,dx
  =\frac{\pi^2 B}{4}\int_0^1c(x)(c'(x))^2\,dx>0.
\end{aligned}
\]
For the first equality on the second line, only the \(\beta_2\)-coefficient
\(dd^cf|_{\beta_2}=-\pi^2c(x_1)\cos(2\pi x_2)\beta_2\)
can wedge nontrivially with the \(\beta_1\beta_3\) component
\(c''\beta_1\beta_3/4\) of \(dd^c\omega\); the normalized \(x_2\)-average of \(\cos^2\) is \(1/2\). The second equality is integration by parts on the \(x_1\)-circle:
\(\int c^2c''=-2\int c(c')^2\).
Nonconstancy of \(c\) gives strict positivity. More explicitly,
\[
\boxed{M(t)=6B+
  \pi^4\varepsilon^2 B\,t^2
  \int_0^1e^{-3\varepsilon\cos(2\pi x)}
                 \sin^2(2\pi x)\,dx>6B
       \quad(t\ne0,\ |t|\text{ small}).}
\]

Consequently, **vanishing of the first variation of the smooth m-Hessian total mass at zero in every direction does not imply its constancy on smooth admissible potentials** when \(m\ge2\). It detects \(dd^c\omega^{n-1}=0\) but not the additional \(dd^c\omega^{n-2}=0\) condition at \(n=3,m=2\). The printed Theorem 8.13.4 correctly requires *all* of its powers, and its proof correctly tests *all polynomial coefficients*. This example is different from printed Example 8.13.5, where the first variation is already nonzero, and from prior smooth Hermitian mass-range reports in dimension two.

## Audit diagnosis, status, proposed addition, dependents

- **No false printed statement:** Theorem 8.13.4, Lemma 8.13.1 and Example 8.13.5 remain correct in the passages directly checked. The new counterexample applies only to a possible, **unprinted** replacement of the full mass-independence hypothesis by a first-order stationarity hypothesis.
- **Suggested optional addition (not implemented):** a remark after the proof of Theorem 8.13.4 illustrating why first-order tests alone cannot replace the coefficients of its degree-\(m\) polynomial. Preserve its source attribution and permanent tags. This is an explanatory boundary, **not** a proof repair.
- **Potential downstream interpretation:** smooth Hessian energy variation and use of the unmodified comparison principle must distinguish the Gauduchon condition \(dd^c\omega^{n-1}=0\) from the stronger system \(dd^c\omega^{n-q}=0\) for every \(q\le m\). No dependent statement is declared erroneous without its own audit.
- **Actual coverage:** direct review of the displayed mass identity and the *smooth* polynomial/polarization argument in §8.13.1, §8.13.4, with §8.13.5 compared for nonduplication; §8.1 only for ambient hypotheses. **Zero first-time numbered sections; zero whole-section certifications; zero transitive dependency-chain certifications.** Existing ToC baseline: **25 chapters / 747 numbered sections**; not recounted in this finding. No project test/build/CI/formal verification/site publication.
- **Excluded programme:** Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**, neither resolved nor reopened. This argument uses only smooth differential forms and compact Stokes.
