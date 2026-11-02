# Uniform cofactor ellipticity despite vanishing determinant — selected mathematical audit

**Finding ID:** POME-MA-COFACTOR-ZERO-DENSITY-001  
**Status:** verified conditional deduction (an independent local exact model), **severity:** low.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Audit date:** 2026-11-02.  
**Scope:** The integrated reading edition, not a source-only restatement. This is **not** a counterexample to a printed theorem or a completed global uniqueness proof.

## Pinpointed reading-edition evidence

- File: docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html; main-branch blob SHA 044f55457f10b2f640052854a7f5f14b8403be82; section 14.21, permanent section tag 6267D9D97C43, source variant non-kahler-pluripotential-theory, source section tag 528A0D7E.
- Equation 14.21.1 (common determinant), line 10–14, source tag 84F3F379, permanent tag 93A49A38E101.
- Theorem 14.21.3, lines 28–50 and proof lines 133–171, source tag 61B8DD0F, permanent tag 6EB399397505; its uniform-positivity region E_unif is defined in lines 17–24, equation 14.21.2, permanent tag E391B921798A.
- Lemma 14.21.5 (almost-everywhere upper contacts), lines 54–74, source tag F0F5D947, permanent tag 59B8A4C8DA05.
- Lemma 14.21.6 (measurable-coefficient strong maximum principle), lines 79–104, source tag E67FD2CF, permanent tag 96D40C4808C2.
- Cofactor form Q and wedge comparison, lines 108–129: equation 14.21.7 source 445DEDC5 / permanent 57588F1C3107; equation 14.21.8 source BDBE4297 / permanent 144125DEDD1C; equation 14.21.9 source A73BA233 / permanent CEEE110C45FE.

The edition fixes the convention $dd^c=(i/2\pi)\partial\bar\partial$. Throughout this report "uniformly elliptic" refers to the *linearized cofactor* quadratic form, not to the individual complex Hessians.

## New exact, nonregularization model

On any ball in $\mathbb C^2$, write
\[
\eta_j=dd^c|z_j|^2,\quad \omega=\eta_1+\eta_2,\quad
u_\varepsilon=(1-\varepsilon)(|z_1|^2-|z_2|^2),\quad
v_\varepsilon=-u_\varepsilon,\qquad 0\leq\varepsilon\leq1 .
\]
The corresponding semipositive forms are
\[
A_\varepsilon=\omega+dd^cu_\varepsilon
 =(2-\varepsilon)\eta_1+\varepsilon\eta_2,\qquad
B_\varepsilon=\omega+dd^cv_\varepsilon
 =\varepsilon\eta_1+(2-\varepsilon)\eta_2 .
\]
All coefficients are smooth and bounded, and direct exterior multiplication yields
\[
A_\varepsilon^2=B_\varepsilon^2
 =2\varepsilon(2-\varepsilon)\eta_1\wedge\eta_2.
\]
Thus, with $dV=\eta_1\wedge\eta_2$, these solve the *same* local determinant equation with the smooth nonnegative density
$f_\varepsilon=2\varepsilon(2-\varepsilon)$, tending uniformly to zero as $\varepsilon\downarrow0$.

For the two-dimensional polarization appearing in equation 14.20.1,
\[
H_\varepsilon=A_\varepsilon+B_\varepsilon
 =2(\eta_1+\eta_2),\qquad
T_\varepsilon=A_\varepsilon+B_\varepsilon=H_\varepsilon .
\]
The cofactor form $Q_\varepsilon(\xi)dV=i\,\xi^{1,0}\wedge\overline{\xi^{1,0}}\wedge T_\varepsilon$ is therefore *strictly positive and independent of $\varepsilon$*. Its ellipticity constants, for the fixed Euclidean metric, have no dependence on the determinant density. In particular, at $\varepsilon=0$ both $A_0$ and $B_0$ have rank one and determinant zero, while $H_0$ and $Q_0$ remain strictly positive. Hence the local region $E_{\rm unif}$ can strictly contain the local positive-density set $U=\{f>0\}$: here $E_{\rm unif}$ is the entire ball but $U$ is empty at $\varepsilon=0$.

The difference $w_\varepsilon=u_\varepsilon-v_\varepsilon$ is nonconstant when $\varepsilon<1$ and nevertheless satisfies exactly
\[
dd^cw_\varepsilon\wedge T_\varepsilon
=4(1-\varepsilon)(\eta_1-\eta_2)
 \wedge(\eta_1+\eta_2)=0,
\]
since $\eta_j\wedge\eta_j=0$ and $\eta_1\wedge\eta_2=\eta_2\wedge\eta_1$.

**Interpretation and strict limits.** A zero Monge–Ampère determinant of each endpoint does **not** force the polarized cofactor operator to lose ellipticity. It would be wrong to identify $E_{\rm unif}$ with $\{f>0\}$ or to infer cofactor degeneracy from vanishing $f$. The printed Theorem 14.21.3 makes neither error: it deliberately uses $E_{\rm unif}$, records only $U\subset E_{\rm unif}$, and invokes compactness plus contact extrema to force global constancy. This local-ball construction is **not** a counterexample to the compact-manifold theorem; a nonconstant harmonic-type function on a ball need not attain its extrema in the interior.

For $n\geq3$ the same algebraic phenomenon persists with
$A=\operatorname{diag}(0,1,\ldots,1)$ and
$B=\operatorname{diag}(1,0,1,\ldots,1)$ in a unitary frame. Each top determinant vanishes, while $A+B=\operatorname{diag}(1,1,2,\ldots,2)>0$, and equation 14.21.8 implies $T\geq2^{-(n-1)}(A+B)^{n-1}>0$.

## Fresh proof-level checks beyond the earlier density-threshold samples

**Lemma 14.21.5:** The proof's full-measure selection is justified, not merely heuristic. If $N$ is the null complement of $E$, the gradient $F=\nabla[g-\delta|x-p|^2]$ is Lipschitz and hence $F(N)$ is Lebesgue null in the *same* real dimension. Choose $s\in B(0,\delta\rho)\setminus F(N)$. A maximum of
$g(x)-\delta|x-p|^2-s\cdot(x-p)$ cannot occur at distance $\geq\rho$ from $p$, as its value is then below the value at $p$ by
$-\delta|x-p|^2+|s||x-p|<0$.
At an interior maximum $F(x)=s$, so $x\notin N$. The existing second-order Taylor expansion then gives $D^2g(x)\leq2\delta I$. This does not rely on choosing a "generic" contact point without a null-image argument.

**Lemma 14.21.6:** Let $\lambda I\leq a\leq\Lambda I$ a.e. on the compact annulus $r/2\leq|x-y|\leq r$. For
$b=e^{-\alpha|x-y|^2}-e^{-\alpha r^2}$, one directly has
\[
a^{ij}b_{ij}\geq e^{-\alpha r^2}
    \bigl(\alpha^2\lambda r^2-2\alpha m\Lambda\bigr)>0
\]
when $\alpha$ is large. The strict weak comparison used to bound $z+\eta b$ follows from Lemma 14.21.5 with $2\delta m\Lambda<\eta\kappa$, and does not differentiate the measurable coefficients. At the outer touching point, $\nabla z=0$ while the inward radial derivative of $b$ equals $2\alpha r e^{-\alpha r^2}>0$, contradicting $z+\eta b\leq\sup z$. The compact annulus and the inner-sphere strict deficit suffice to choose $\eta>0$. These selected analytic steps are correct as written.

**Equation 14.21.8:** In complex dimension two the upper inequality is an identity $T=A+B=H$; our model confirms it exactly, including its semipositive rank-deficient limit. The $n\geq3$ extension uses only the positive wedge inequalities already displayed in the edition.

## Disposition, dependencies, and coverage accounting

- **Status:** low / verified conditional deduction; **no confirmed source error**, no applied repair and no new unproved external mathematical premise for this specific model. The two selected elementary analytic proofs were checked directly.
- **Suggested nonessential editorial addition:** after equation 14.21.9, an explicit complementary-rank local model could illustrate why $E_{\rm unif}$ rather than merely $U$ is the natural ellipticity set. Do not change Theorem 14.21.3, its quantifiers, or the source tags.
- **Affected dependent reasoning (not amended):** the cofactor localization step of Theorem 14.21.3 and its use in Theorem 14.21.13 and the subsequent §14.22 propagation discussion. Those global arguments and all their antecedent regularity/existence results are *not* certified by this example.
- **Actual newly examined material:** proof details of Lemmas 14.21.5–6 and the rank-deficient limit of equations 14.21.7–9 in the already partially sampled §14.21. Theorem 14.21.3 was read for exact hypotheses and the distinction between its local and global assertions. No first-covered numbered section or entire-section certificate is claimed.
- **Collection status:** the actual current ToC has 25 chapters and 747 numbered sections; zero complete mathematical-section certifications. Prior confirmed errors, proof gaps, candidate dependencies, duplicate findings, and deferred findings retain their earlier classifications.
- **User-deferred subjects:** No Demailly approximation/regularization, Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof-completion was opened. No source, generated docs, canonicalization, registry, permanent tag, CI, build, formalization or website change was made.
