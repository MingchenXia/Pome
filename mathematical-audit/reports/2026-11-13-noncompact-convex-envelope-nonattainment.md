# Noncompact convexification: loss of closedness and of an attained infimum

**Date:** 2026-11-13  
**Stable finding:** POME-CONVEX-NONCOMPACT-HULL-NONATTAIN-001  
**Severity / status:** low / **verified conditional deduction** (sharp scope counterexample; **not** an error in the printed lemma).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact integrated anchors

- `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, blob `b3b4e34fff767a717df812a381f905589b257fb3`; **Lemma 21.6.1**, source `foundations-of-pluripotential-theory:30FFD831`, permanent tag `FCDAD9CEC8CE`, statement physical lines **10–12**, replacement/reading proof **14–30** (in particular compactness and lower-bound use lines **17–25**).
- `docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html`, blob `347fa1f0fc35c13b1d1c45193ab997ed456966e4`; **Proposition 21.3.3(2)**, source `foundations-of-pluripotential-theory:E93FCB56`, permanent tag `53A9D470F1AC`, starting physical line **64** and convexification proof through **122**; **Theorem 21.3.2**, source `foundations-of-pluripotential-theory:DD2DB654`, permanent tag `011FA81B0000`, statement line **24**.
- Current main `docs/navigation.json` has **25 chapters and 747 numbered sections**. This run reviewed the *selected proof and its sharp noncompact scope*, not the complete section or its entire dependency chain.

## Question being tested

Lemma 21.6.1 assumes **finitely many closed proper convex extended-real-valued functions with effective domains in one compact set**. It proves that their greatest convex minorant is closed, that the infimum in the finite-barycenter formula is attained at every finite point, and hence that this minorant equals the conjugate of the maximum of their conjugates. Is mere closedness/properness, even with a common finite lower bound, sufficient without the compact-domain hypothesis?

**Answer: no, for both closedness and attainment, already for two functions on \(\mathbb R^2\).**

## Explicit closed convex inputs

Work on \(V=\mathbb R^2\), writing \(z=(x,y)\). Put
\[
C=\{(x,y):x>0,\ y\ge 1/x\},\qquad
G_1=I_{\{(0,0)\}},\qquad G_2=1+I_C,
\]
where \(I_A\) is \(0\) on \(A\), and \(+\infty\) outside.

1. \(C\) is nonempty and convex: \(x\mapsto 1/x\) is convex for \(x>0\), and \(C\) is its epigraph. It is **closed in \(\mathbb R^2\)**: a convergent sequence in \(C\) cannot have \(x\to0^+\) while \(y\ge 1/x\) remains finite. Thus both \(G_i\) are closed, proper and convex.
2. Both \(G_i\) are everywhere bounded below by \(0\). The domain of \(G_2\) is unbounded, so the one common-compact-domain hypothesis in the printed lemma fails.

By Proposition 21.3.3(2), the greatest convex function \(H\le\min(G_1,G_2)\) is the infimum over *finite* barycentric combinations of points from the two domains, weighted by the respective function values. Convexity of \(C\) reduces every relevant combination to
\[
z=(1-\lambda)(0,0)+\lambda c=\lambda c,\quad
0\le\lambda\le1,\ c\in C,\qquad
\text{cost } \lambda.
\]
For \(z\ne0\), necessarily \(\lambda>0\). Conversely, if \(x>0,y>0\), every \(0<\lambda\le\min(1,\sqrt{xy})\) satisfies \(c=(x/\lambda,y/\lambda)\in C\), since
\[
\frac y\lambda \ge \frac{\lambda}{x}
\quad\Longleftrightarrow\quad xy\ge\lambda^2.
\]
Hence \(z\) admits a representation of cost \(\lambda\) for arbitrarily small positive \(\lambda\), but no representation of cost \(0\). For \(z=0\), the first domain realizes cost \(0\). No other point admits a barycentric representation.

It follows **exactly** that
\[
\operatorname{conv}(C\cup\{0\})
=\{0\}\cup\bigl((0,\infty)\times(0,\infty)\bigr)=:S,
\qquad
H=I_S.
\]
In particular
\[
H(1,1)=0
\quad\text{but its barycentric infimum is not attained},\qquad
H(1,0)=+\infty,\qquad
\lim_{j\to\infty}H(1,1/j)=0.
\]
Thus \(H\) is **not lower semicontinuous**, and **every nonzero point where \(H\) is finite is a failure of attainment**. This is stronger than failure of closedness alone.

## Independent conjugate computation and exact relaxation

For \(p,q\in\mathbb R\), the conjugates are
\[
G_1^*(p,q)=0,\qquad
G_2^*(p,q)=
\begin{cases}
-1-2\sqrt{(-p)(-q)},&p\le0,\ q\le0,\\
+\infty,&\text{otherwise}.
\end{cases}
\]
Indeed, \(q>0\) allows \(y\to+\infty\); \(p>0\) allows \(x\to+\infty\) with \(y=1/x\). For \(p=-a\le0,q=-b\le0\), taking \(y=1/x\) gives \(\sup_{x>0}(-ax-b/x)-1=-1-2\sqrt{ab}\), including the \(a=0\) or \(b=0\) boundary by limits.

Therefore
\[
\max(G_1^*,G_2^*)=I_{(-\infty,0]^2},\qquad
(\max(G_1^*,G_2^*))^*=I_{[0,\infty)^2}.
\]
This is \(H^{**}=\operatorname{cl}H\), **not \(H\)**: in particular the relaxed value at \((1,0)\) is \(0\) rather than \(+\infty\). The failure is neither a defective convention about conjugation nor a sign error: it is precisely the nonclosed convex-hull/escape-to-infinity phenomenon.

## Assessment of the integrated proof and dependency boundary

- The printed **Lemma 21.6.1 remains correct as stated**. Its proof uses compact \(K\) exactly to get bounded-below \(G_i\), convergent chosen barycenters and limit points for positive-weight terms. In this example the lower bound survives, but the barycenters \(c=z/\lambda\) escape to infinity as \(\lambda\downarrow0\); thus no compactness subsequence can be extracted. There is **no verified error** in its argument at lines 17–29.
- Proposition 21.3.3(2)'s finite-combination formula is independently tested by the explicit infimum and is consistent with the conjugacy identity. The closed hull comes from taking the biconjugate, not from the finite-combination formula itself.
- **Proposed correction for any future generalization only:** retain the common compact-domain hypothesis (or prove an appropriate independent level-compactness / no-escape condition); do **not** assert closedness or attainment from properness, lower semicontinuity and a common lower bound alone. No source patch or change to the printed lemma is proposed.
- **Affected comparison targets:** §21.6.1 (hypothesis sharpness), §21.3.3(2) (raw convexification versus closure), §21.3.2 (biconjugacy). §21.6.2's vague/narrow statement is logically unrelated and is **not** reaudited here. No claims are made about arbitrary noncompact extended-valued envelopes beyond this explicit counterexample.
- **Scope exclusion:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not resolved or verified.

**Proof-level coverage credit:** newly checked selected Lemma 21.6.1 and its duality inputs; the numbered §21.6 previously had a different selected §21.6.2 audit, therefore **0 new first-visited sections, 0 complete section certifications**. No code tests, builds, CI, formal verification or publication were performed.
