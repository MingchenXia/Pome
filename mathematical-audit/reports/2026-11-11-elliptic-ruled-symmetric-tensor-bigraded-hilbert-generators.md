# Bigraded Hilbert series and exact weight-one indecomposables for the split elliptic ruled surface

**Date:** 2026-11-11. **Stable finding:** POME-RULED-SYMTENSOR-BIGRADED-HILBERT-INDECOMP-001. **Severity/status:** low / verified conditional deduction, **not** a false printed theorem, a source repair, or a complete upstream certification.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Precisely checked reading edition and hypotheses

- Integrated file: docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--symmetric-tensors-on-split-elliptic-ruled-surfaces/index.html, main blob f361ebba006461edd8e2aca3b48a501938510e2e.
- Lemma 12.31.1, source non-kahler-pluripotential-theory:EA1E9CBB, permanent 2604E6F7AC76, physical lines 28–75: the entire weight decomposition and multiplicative grading.
- Lemma 12.31.2, source non-kahler-pluripotential-theory:4B3CCF12, permanent 711AF6E8C0D8, lines 80–129: the nontrivial rank-two extension, dimensions and leading-coefficient exact sequence.
- Theorem 12.31.3, source non-kahler-pluripotential-theory:81C41791, permanent 654B70C2AFD7, lines 137–160: total symmetric-tensor dimensions and volume.
- Theorem 12.31.4, source non-kahler-pluripotential-theory:38263A71, permanent 3B7C9C492833, lines 165–193: the square-zero quotient proving non-finite generation.
- Geometric input: docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--cotangent-torsors-on-split-elliptic-ruled-surfaces/index.html, main blob 2a3e0f45924a48f701cf8de0526f0945824c0574. Introduction lines 5–7 sets M=P_lines(O_E plus A) with E elliptic and deg(A)=d>0. Lemma 12.30.2, source non-kahler-pluripotential-theory:F0217EE5, permanent 68FEC9C7A0BC, lines 49–56 supplies the factors of automorphy.

We use the printed weight convention: a negative C-star weight -k is recorded by a nonnegative second grading k. No statement is made about the abstract section algebra of an arbitrary ruled surface.

## New quantitative consequence

Let E be a compact elliptic curve, A a line bundle of degree d>0, M=P_lines(O_E plus A), and

$$
R=\bigoplus_{r\geq 0}H^0(M,\operatorname{Sym}^r T_M)
 =\bigoplus_{r\geq0}\bigoplus_{k=0}^r R_{r,k},
$$

where the second index k denotes the *negative* C-star weight -k. Then the exact bigraded Hilbert series, as a formal power series in x and y, is

$$
\boxed{\mathcal H_R(x,y)=\sum_{r,k}\dim_{\mathbb C}R_{r,k}\,x^r y^k
=\frac1{1-x}+\frac{dxy}{(1-x)^2(1-xy)^2}.}
$$

In particular, the ordinary Hilbert series is the rational function

$$
\boxed{\mathcal H_R(x,1)=\frac1{1-x}+\frac{dx}{(1-x)^4}.}
$$

Put R_+=\bigoplus_{r>0}R_r and Q=R_+/(R_+)^2. For **every** r>=1 there is a canonical, leading-coefficient-induced identification

$$
\boxed{Q_{r,1}\ \cong\ H^0(E,A),\qquad\dim_{\mathbb C}Q_{r,1}=d.}
$$

Consequently every homogeneous generating family for R needs at least d linearly independent generators of bidegree (r,1) **for every** r>=1. For the degree-N truncation R^{\leq N}, with all products of total degree >N set equal to zero, every algebra generating family has at least dN+1 elements for N>=1: d in each of the N weight-one bidegrees, and one for the weight-zero class of h in tensor degree one. This is a **lower bound**, not an assertion that there are no other indecomposable generators in higher weights.

Thus a big tautological line bundle on a projective threefold has a rational (indeed elementary) Hilbert series while its section ring is not finitely generated. Rationality of a Hilbert series alone must not be used as a finite-generation criterion.

## Proof (finite, independent algebraic manipulation after the internal geometric lemmas)

Lemma 12.31.1 identifies R_{r,0}=C h^r and, for 1<=k<=r,

$$
R_{r,k}\cong H^0(E,A^k\otimes\operatorname{Sym}^{r-k}U).
$$

Lemma 12.31.2, using its elliptic Riemann–Roch/Serre duality and filtration argument, gives

$$
\dim R_{r,0}=1,\qquad \dim R_{r,k}=kd(r-k+1)\quad(1\leq k\leq r),
$$

with no positive C-star weights. Writing s=r-k yields the factorization

$$
\begin{aligned}
\mathcal H_R(x,y)
&=\sum_{r\geq0}x^r
 +d\sum_{k\geq1}\sum_{s\geq0} k(s+1)x^{k+s}y^k\\
&=\frac1{1-x}
 +d\left(\sum_{k\geq1} k(xy)^k\right)
  \left(\sum_{s\geq0}(s+1)x^s\right)\\
&=\frac1{1-x}+\frac{dxy}{(1-xy)^2(1-x)^2}.
\end{aligned}
$$

The specialization y=1 is valid coefficientwise in x because each total-degree piece contains only finitely many weights. Its coefficient is exactly 1+d r(r+1)(r+2)/6, agreeing with Theorem 12.31.3, but the bigraded formula retains all weight information rather than merely repeating that total count.

Because all weights occurring in R have nonnegative second index, a product of two elements of R_+ whose total second index is one must have weight indices zero and one. The entire positive-degree weight-zero subalgebra is h C[h]. Therefore, for r>=2,

$$
(R_+^2)_{r,1}=hR_{r-1,1};
$$

for r=1 both sides are zero by the convention R_{0,1}=0. The leading-coefficient sequence in Lemma 12.31.2, with s=r-1,

$$
0\longrightarrow A\otimes\operatorname{Sym}^{s-1}U
\xrightarrow{h}A\otimes\operatorname{Sym}^sU\longrightarrow A\longrightarrow0,
$$

induces a surjection on H^0 whose kernel is exactly multiplication by h because H^1(E,A\otimes Sym^{s-1}U)=0. When s=0, the identity H^0(E,A)=R_{1,1} supplies the same conclusion. Hence Q_{r,1}=R_{r,1}/hR_{r-1,1}=H^0(E,A), of dimension d.

For a connected, nonnegatively graded algebra R with R_0=C, images of any homogeneous algebra generators span Q. In the finite truncation the quotient by products in positive degree has the same bidegrees Q_{r,k} for all r<=N, since discarded products have larger total degree; Q_{1,0}=C h supplies one further independent generator. Summing dimensions gives dN+1. This algebraic argument does not assert finite generation, formalization or upstream theorem verification.

**Finite coefficient crosscheck, not a proof substitute:** for d=1 and r=0,...,8, summing 1+sum_{k=1}^r k(r-k+1) gives respectively 1,2,5,11,21,36,57,85,121, the coefficients of 1/(1-x)+x/(1-x)^4.

## Classification, dependency and proposed action

- **Status:** verified conditional deduction; **severity low**. Nothing in the checked Lemmas 12.31.1–2 or Theorems 12.31.3–4 has been refuted. In particular this finding **does not repeat** their existing qualitative square-zero non-finite-generation argument: it records a new explicit two-variable series and uniform per-degree lower bounds on homogeneous generators.
- **Dependencies not newly certified:** the cotangent-coordinate transition of Lemma 12.31.1 (lines 38–75); non-splitting, elliptic cohomology and exact leading coefficient of Lemma 12.31.2 (lines 98–129); the base line-bundle automorphy factors of Lemma 12.30.2. They were inspected but their entire surrounding geometric proof chain was not independently re-established. Hironaka and excluded regularization programmes are not used.
- **Affected dependents:** optional strengthening immediately after Theorem 12.31.4, and the canonical-extension section-algebra comparisons in §12.32 if one elects to track generators by bidegree. No existing theorem needs weakening.
- **Proposed correction:** no source-body correction. Optionally add a corollary with the displayed Hilbert series and Q_{r,1} calculation, preserving the original theorem, permanent tags, different valid versions and historical attribution. This report alone makes no source or registry changes.
- **Scope bookkeeping:** §12.31 was already partly proof-reviewed in the previous POME-RULED-ALG-INDECOMP-001 audit. This run checks the exact integrated printed inputs and adds **one new focused algebraic implication**; §12.30.2 is normalization/context only. **Zero new first-visited numbered sections, zero fully certified sections.** The actual current main ToC remains 25 chapters / 747 numbered sections.
- **Deferred unchanged:** Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme are deferred-by-user, not resolved or certified. No CI/build/site publication, or main/source/permanent-tag edits have been performed in this review.
