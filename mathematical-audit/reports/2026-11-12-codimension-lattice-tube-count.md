# 2026-11-12 — Sharp codimension-dependent lattice-tube counts

**Finding ID:** POME-TORIC-LATTICE-CODIMENSION-TUBE-001  
**Status:** verified conditional deduction (the elementary estimate below is proved directly; no source theorem is refuted).  
**Severity:** low (quantitative sharpening and hypothesis-boundary check, not a production defect).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Exact integrated source and provenance

- File: docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html; blob 5d209b7f4d2156c19bc3fb300303405df6321230.
- Proposition 21.7.2, source foundations-of-pluripotential-theory:5E9AEE47, permanent tag EDD78BC61BD7, physical lines 27–55: support-function/Hausdorff and volume continuity, including empty-interior cases.
- Theorem 21.7.3, source foundations-of-pluripotential-theory:364BCD30, permanent tag 831AEEB7084F, physical lines 57–91: lattice sums in sublinear outer neighborhoods, uniform in arbitrary lattice translations.
- Corollary 21.7.4, source foundations-of-pluripotential-theory:D6B87DCB, permanent tag CF4226A5034F, physical lines 93–107: intermediate lattice sets and leading volume. Its proof invokes the previous theorem.
- Theorem 21.9.5 is referenced in the introduction at physical line 7 only as motivation (permanent tag 69D3D97E7701); its toric section-space identification is not reverified here.

This is distinct from the 2026-10-25 moving-convex-body Hausdorff convergence and from the 2026-10-30 translated-lattice boundary checks. Those results address the leading n-dimensional limit; the present calculation isolates a **sharp rate controlled by affine codimension for a fixed zero-volume body**, including r=0, and does not refile their findings.

## New precise statement

Let n≥1, 0≤d<n, and let K be a nonempty compact set contained in an affine d-dimensional subspace V of Euclidean R^n. Fix the standard lattice Z^n, though V need not be rational with respect to it. For integer k≥1, real r≥0 and arbitrary a∈R^n, define

\[
N(k,r,a;K)=\#\bigl((kK)^r\cap(\mathbb Z^n+a)\bigr),
\qquad (kK)^r=\{x:\operatorname{dist}(x,kK)\le r\}.
\]

There exists C=C(K,n)>0, **independent of k,r,a**, such that

\[
\boxed{N(k,r,a;K)\le C(k+r+1)^d(1+r)^{n-d}.}\tag{A}
\]

For any sequence r_k≥0 with r_k=o(k), this becomes, for all sufficiently large k,

\[
\boxed{\sup_{a\in\mathbb R^n} k^{-n}N(k,r_k,a;K)
 \le C'\left(\frac{1+r_k}{k}\right)^{n-d}\longrightarrow0.}\tag{B}
\]

For bounded f, the same upper bound multiplied by \(\|f\|_\infty\) controls the absolute value of the normalized weighted lattice sum. In particular this supplies a quantitative zero-volume case of Theorem 21.7.3 **uniformly over translations**, without supposing that V has any rational direction.

The exponents d and n−d are simultaneously optimal as a universal upper bound. With \(K=[0,1]^d\times\{0\}^{n-d}\), \(a=0\), integer k, and q=n−d, one has

\[
N(k,r,0;K)\ge(k+1)^d\left(2\left\lfloor
 \frac r{\sqrt q}\right\rfloor+1\right)^q
 \ge c_{n,d}\,k^d(1+r)^q.
\tag{C}
\]

For r=0 this has order k^d. For 1≪r=o(k), it has order \(k^d r^{n-d}\). The lower estimate is **an example**, not a claim of a uniform lower bound for irrational affine subspaces or translated lattices.

## Full proof

Let \(Q=[0,1)^n\), and for each \(m\in\mathbb Z^n+a\), let \(Q_m=m+Q\). These disjoint half-open cells tile R^n and have volume exactly one, independently of a. If m lies in \((kK)^r\), every point of Q_m is at distance at most \(r+\sqrt n\) from kK, since \(\operatorname{diam}Q=\sqrt n\). Therefore the disjoint union of the selected cells is contained in \((kK)^{r+\sqrt n}\). Its volume equals the number of selected cells, so

\[
N(k,r,a;K)\le\operatorname{vol}_n((kK)^{r+\sqrt n}).\tag{1}
\]

Choose a point \(x_0\in V\), write \(V=x_0+W\) with \(\dim W=d\), and choose D>0 such that \(K\subset x_0+\{w\in W:|w|\le D\}\). Orthogonally decompose R^n as \(W\oplus W^\perp\). If \(x\in(kK)^s\), then, relative to the center \(kx_0\), its W-coordinate has norm at most kD+s, while its perpendicular coordinate has norm at most s. Hence \((kK)^s\) lies in the product of the d-ball of radius kD+s and the (n−d)-ball of radius s. Fubini gives

\[
\operatorname{vol}_n((kK)^s)
 \le v_d v_{n-d}(kD+s)^d s^{n-d},\tag{2}
\]

where \(v_j\) is the Euclidean unit-ball volume in dimension j and \(v_0=1\). Put \(s=r+\sqrt n\). For k≥1, \(kD+r+\sqrt n\le C_D(k+r+1)\) and \(r+\sqrt n\le C_n(1+r)\). Combining (1)–(2) proves (A). If \(r_k/k\to0\), then \(r_k\le k\) eventually, so the first factor is bounded by \(Ck^d\); divide by k^n to obtain (B). Neither step uses the orientation of V nor the translation a.

For sharpness set \(K=[0,1]^d\times\{0\}^q\) and a=0. Every integer point \(m=(m',m'')\) with \(m_i'\in\{0,\dots,k\}\) and \(|m_j''|\le r/\sqrt q\) lies at distance at most r from kK, because the tangential projection \(m'\) itself lies in \([0,k]^d\) and \(|m''|_2\le r\). Counting these points proves the first inequality of (C). For all r≥0, \((2\lfloor r/\sqrt q\rfloor+1)/(1+r)\) has a strictly positive lower bound depending on q only (for r≤2√q use 1; for r>2√q use the floor estimate). This proves the second inequality. The upper and lower estimates therefore match up to constants.

For the weighted statement use the triangle inequality:
\[
\left|k^{-n}\sum_{m\in(kK)^{r_k}\cap(\mathbb Z^n+a_k)}f(m/k)\right|
\le \|f\|_\infty\,k^{-n}N(k,r_k,a_k;K).
\]
When f is merely continuous globally, for sufficiently large k all anchors m/k belong to the fixed compact \(K^1\), hence \(\sup_{K^1}|f|\) replaces \(\|f\|_\infty\). This proves the full continuous-test version in the original theorem's zero-volume case.

## Audit classification, correction and dependents

**Classification:** low / verified conditional deduction (completely proved finite-dimensional estimate; its identification as a refinement of §21.7.3 assumes only the printed coordinate/lattice conventions). Theorem 21.7.3 remains correct, and no source-text correction is needed. An optional independent corollary after 21.7.3 could state (B), with the precise affine-dimension and r_k=o(k) hypotheses, while preserving the original n-dimensional theorem and all permanent tags. The bound may inform applications to lower-dimensional slope bodies and restricted section counts, but does **not** prove new toric Hilbert identities, and no affected downstream theorem is claimed false.

**Actual coverage:** newly checked integrated §§21.7.2–4 and the cell-count/measure argument at physical lines 27–107; full derivation of (A)–(C). §21.7 was already partially reviewed in prior audit reports: **0 first-visited numbered sections, 0 entirely certified sections** in this run. Broader §21.7 support-function/Hausdorff theorem, §§21.8–21.9 geometry, and unreviewed dependency chains are not certified here. Current actual ToC baseline: 25 chapters, 747 numbered sections. All Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale-atlas/positivity-loss programme remain **deferred-by-user**, untouched.

**Operational scope:** review-branch Markdown only; no edits to main, canonical registry, source repositories, theorem tags, generated pages, CI, build or publication.
