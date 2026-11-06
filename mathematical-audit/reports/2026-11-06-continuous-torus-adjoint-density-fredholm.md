# Exact adjoint densities for continuous Hermitian trace operators on a non-Kähler torus

**Date:** 2026-11-06. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding ID:** `POME-HERM-FREDHOLM-ROUGH-ADJOINT-DENSITY-001`.
**Severity:** low. **Status:** verified conditional deduction; **no false printed theorem**.
**Scope:** a new selected-model review of §11.24.1, not a proof of the general continuous-coefficient Fredholm theorem and not an audit of all Chapter 11.

## Exact integrated anchors and provenance

- `docs/sections/gauduchon-metrics-and-linear-mass--fredholm-theory-for-a-continuous-hermitian-form/index.html`; main blob `8fd933d027ecdba0c2df8efe7524e3984613857a`.
- **Lemma 11.24.1**, source `non-kahler-pluripotential-theory:2FF004A4`, permanent tag `DEA6C8EFE702`: physical HTML lines 10–15 (continuous positive coefficients, `p>2n`, Fredholm index zero, constants as kernel and one-dimensional `L^{p'}` annihilator). Lines 20–33 contain its frozen-coefficient `W^{2,p}` argument; lines 36–57 the maximum-principle proof; lines 59–66 the compact-perturbation/Fredholm conclusion.
- Relevant downstream comparison, **Proposition 11.23.2**, `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, main blob `519e50338be6560f6b2856fddce212738f5109bc`, physical lines 14–29 and 34–43: for a *smooth* form the adjoint measure is smooth. **Proposition 11.25.1**, `docs/sections/gauduchon-metrics-and-linear-mass--limits-of-adjoint-measures/index.html`, main blob `48117e4e5901381d5ae692cfd29f2cf5f1325abc`, source `non-kahler-pluripotential-theory:A07C226C`, permanent `3E5CF25D6E23`, lines 10–21: its non-pluripolar/BT hypothesis is deliberately *not* tested here.
- Current §11.24 section tag `DB480BD29A98`, source section `non-kahler-pluripotential-theory:F945144E`. §11.24 is present in the actual current Chapter 11 navigation (chapter HTML `docs/chapters/hermitian-torsion/index.html`, blob `4334685938df6b4b83cc024e3fd9245e49c5197d`).

## Exact continuous-coefficient model

Let \(n\ge 2\), \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(X=E^n\), and
\[
\beta_j=\frac i2\,dz_j\wedge d\bar z_j=dx_j\wedge dy_j,\qquad
dV=\beta_1\wedge\cdots\wedge\beta_n,\qquad \int_XdV=1.
\]
Fix the positive, smooth, nonconstant one-periodic function
\[
b(x_1)=2+\tfrac14\sin(2\pi x_1).
\]
For **any** positive continuous one-periodic function \(a(x_1)\) define
\[
\sigma_a=a(x_1)\beta_1+b(x_1)\beta_2+\sum_{j=3}^n\beta_j,
\qquad \bar a=\int_0^1a(t)\,dt.
\]
The metric is uniformly positive on compact \(X\), and is generally not closed:
\[
d\sigma_a=b'(x_1)\,dx_1\wedge\beta_2\not\equiv0,
\]
because \(da\wedge\beta_1=0\) even for continuous \(a\) (distributionally). The model is thus genuinely Hermitian and non-Kähler; no approximation, extension, or Bergman input is involved.

The Pome convention \(dd^c=\frac i{2\pi}\partial\bar\partial\) yields, on every smooth real \(v\),
\[
L_{\sigma_a}v=
\frac1{4\pi}\left[
a(x_1)^{-1}\Delta_1v+b(x_1)^{-1}\Delta_2v+
\sum_{j=3}^n\Delta_jv\right],
\qquad
\Delta_j=\partial_{x_j}^2+\partial_{y_j}^2.
\]
Off-diagonal complex Hessian entries do not enter the diagonal trace. The function
\[
q_a(x)=a(x_1)/\bar a
\]
is a strictly positive, continuous **probability density relative to the fixed smooth \(dV\)**, and it annihilates the range. Indeed,
\[
\begin{aligned}
4\pi\int_X(L_{\sigma_a}v)q_a\,dV
&=\frac1{\bar a}\int_X\left[
\Delta_1v+\frac{a(x_1)}{b(x_1)}\Delta_2v
+\sum_{j=3}^na(x_1)\Delta_jv\right]dV\\
&=0.
\end{aligned}
\]
Each term integrates to zero by periodic integration in **the variable whose Laplacian it contains**; no derivatives of \(a\) or \(b\) are used. The identity extends from smooth functions to \(W^{2,p}\) by strong Sobolev approximation and boundedness of \(L_{\sigma_a}\). Since \(q_a\in C^0\subset L^{p'}\), **if** the general Fredholm and one-dimensional annihilator assertion of printed Lemma 11.24.1 holds, this \(q_a\) spans its entire annihilator, independently of \(p>2n\). The explicit annihilation is proved here; the general Fredholm assertion is *not* independently reconstructed.

Consequently the family realizes **every** positive continuous one-variable probability density \(q(x_1)\) as the unique normalized range-annihilating density of a continuous positive Hermitian trace operator: simply choose \(a=q\).

## Sharp regularity barrier, including smooth coefficient families

1. Choose
   \[
   a_*(x_1)=1+\tfrac12|\sin(2\pi x_1)|,\qquad \bar a_*=1+1/\pi.
   \]
   Then \(\sigma_{a_*}\) has continuous, uniformly positive coefficients; its normalized adjoint density \(q_{a_*}=a_*/(1+1/\pi)\) is **not \(C^1\)** along the real hypersurfaces \(x_1=0\) and \(x_1=1/2\) in \(E^n\). Thus Lemma 11.24.1's conclusion \(\text{annihilator}\subset L^{p'}\) cannot be strengthened to *smooth fixed-volume densities* under its bare continuity hypothesis. This says nothing against smoothness when the coefficients themselves are smooth.
2. Even restricting to smooth metrics, put
   \[
   a_N(x_1)=1+N^{-1/2}\cos(2\pi N x_1),\qquad N\ge4.
   \]
   These positive smooth \(\sigma_{a_N}\) converge uniformly to the **nonclosed** smooth metric \(\sigma_1\), and \(\bar a_N=1\). Their **exact** normalized adjoint densities satisfy
   \[
   \|q_{a_N}-1\|_{C^0}=N^{-1/2}\to0,\qquad
   \|\partial_{x_1}q_{a_N}\|_{L^\infty}=2\pi\sqrt N\longrightarrow\infty.
   \]
   Thus \(C^0\) convergence of uniformly elliptic Hermitian coefficients does **not** give a uniform \(C^1\) bound for normalized adjoint densities relative to a fixed smooth volume, even on a fixed flat complex torus with smooth approximants.

The choice of reference measure matters. In this model
\[
\sigma_a^n=n!\,a(x_1)b(x_1)\,dV,\qquad
q_a\,dV=\frac1{n!\bar a b(x_1)}\,\sigma_a^n.
\]
The *multiplier relative to \(\sigma_a^n\)* equals \(1/(n!\bar a b)\), which may be smooth even when the density \(q_a\) relative to the fixed smooth volume is not. Therefore the example must **not** be misquoted as asserting nonsmoothness of every Gauduchon multiplier. Nor is \(q_a\,dV\) generally the normalized Monge–Ampère volume \(\sigma_a^n/\int\sigma_a^n\); that latter identification requires the corresponding Gauduchon hypotheses, absent here.

## Mathematical classification and downstream implications

- **Verified conditional deduction / low**, not confirmed error or proof gap. The displayed operator, annihilation identity, normalization, nonclosure, cusp regularity, and exact smooth-frequency norms are unconditional direct calculations. Uniqueness of the annihilator uses only the explicitly stated conclusion of Lemma 11.24.1 and is therefore marked *conditional on that lemma*. The printed lemma is consistent with the example.
- **Suggested optional reading-edition note, not a source change:** after Lemma 11.24.1, say that its annihilator lies in \(L^{p'}\), and that even with a continuous positive coefficient matrix one cannot infer smoothness of the density relative to a fixed smooth volume. An elementary torus model gives an explicit witness; coefficient \(C^0\) convergence alone does not give \(C^1\) adjoint-density stability. Keep the distinct smooth adjoint-density statement at §11.23 and the distinct Gauduchon-dependent §11.25 limit result unchanged.
- **Affected/related:** any later use that would attempt to promote the \(L^{p'}\) annihilator of §11.24 to a smooth fixed-volume density **without additional coefficient hypotheses**, and any derivative-level stability argument based solely on a \(C^0\) family of trace matrices. There is no demonstrated such false inference in the printed dependent propositions.
- **Not checked:** the general continuous-coefficient Calderón–Zygmund/Fredholm proof (including its external order-zero multiplier and smooth elliptic-theory inputs), positivity for arbitrary adjoint annihilators, general entropy flows, any nonlinear or non-pluripolar limit passage, and entire-section dependencies. No build/test/formalization/CI or site publication was performed. The owner's excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not reviewed or resolved.

**Coverage accounting:** this is a first selected substantive §11.24.1 model check, with a limited §11.23.2 smooth-reference comparison and §11.25.1 assumptions read only as context. **No full theorem or mathematical section certified**; existing 25-chapter/747-numbered-section matrix and previous statuses remain intact.
