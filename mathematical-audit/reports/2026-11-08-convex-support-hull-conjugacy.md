# Arbitrary-set support conjugacy: an internal proof for Example 21.11.25

**Stable finding ID:** POME-CONVEX-SUPPORT-HULL-CONJUGACY-001. **Severity:** low. **Status:** verified repair, proposed only (replacement proof for a genuine cited external input, not a correction of a false theorem). The stronger arbitrary-set statement below is a verified conditional deduction.

**Production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated file:** docs/sections/convex-functions-and-convex-bodies/index.html, blob 2a123a863642a5a75caa173f0f73aff439a02ea4. Exact targets: Definition 21.11.22, source sgpt:8B018B53, permanent 2E5E29E9A58B (physical lines 214–220); equation 21.11.23, source sgpt:E288ED21, permanent E1AD8A1437E2 (216–220); Example 21.11.25, source sgpt:8297B2F5, permanent 1A7C0B007516 (234–239). Theorem 21.11.24, source sgpt:1A7E065D / permanent 258227E5D497 (223–232), was consulted for context only.

The actual printed Example 21.11.25 correctly asserts \(h_P^*=\chi_P\), \(\chi_P^*=h_P\) for **closed convex** \(P\) (where \(h_P=\operatorname{Supp}_P\)). It cites Rockafellar 1970, Theorem 13.2. The following self-contained proof covers precisely this identity, without importing general finite-dimensional Fenchel–Moreau theory. The historical citation is **retained**.

## Full argument: any subset, including the empty set

Let \(M\) be a finite-dimensional real vector space, \(N=M^*\). For an **arbitrary** \(S\subset M\) define
\[
 h_S(n)=\sup_{s\in S}\langle s,n\rangle,\qquad
 \chi_S(m)=\begin{cases}0&m\in S,\\+\infty&m\notin S,\end{cases}
 \qquad K=\overline{\operatorname{conv}}S.
\]
Adopt \(\sup\varnothing=-\infty\) and \(K=\varnothing\) if \(S=\varnothing\). Then
\[
\boxed{\quad (\chi_S)^*=h_S,\qquad (h_S)^*=\chi_K,\qquad
  (\chi_S)^{**}=\chi_K.\quad} \tag{*}
\]
By the definition of conjugacy, \((\chi_S)^*=h_S\) directly. The support function is unchanged when a set is replaced by its convex hull or closure, since a linear functional takes the same extended supremum on all three; hence \(h_S=h_K\).

Suppose \(S\ne\varnothing\), so \(K\) is nonempty, closed and convex. For \(m\in K\), \(h_K(n)\geq\langle m,n\rangle\) for every \(n\); the supremum in the conjugate is at most zero, and \(n=0\) attains zero. Thus \(h_K^*(m)=0\).

For \(m\notin K\), choose a Euclidean inner product on \(M\). There exists a nearest point \(p\in K\): intersection with a sufficiently large closed ball reduces minimization to a nonempty compact set, since \(K\) is closed. Set \(v=m-p\ne0\), and identify \(v\) with the functional \(n_v(q)=\langle v,q\rangle_{\mathrm{Euc}}\) on \(M\). Every \(q\in K\) satisfies \(p+t(q-p)\in K\) for \(0\leq t\leq1\). Differentiating at \(t=0^+\) the inequality
\[
 \|m-p-t(q-p)\|^2\geq\|m-p\|^2
\]
gives \(\langle v,q-p\rangle_{\mathrm{Euc}}\leq0\). Therefore \(h_K(n_v)=n_v(p)<+\infty\), so
\[
 \langle m,n_v\rangle-h_K(n_v)=\|m-p\|^2>0.
\]
Scaling \(n_v\) by \(t\to+\infty\) proves \(h_K^*(m)=+\infty\). Thus \(h_S^*=\chi_K\) on all \(M\), establishing (*).

If \(S=\varnothing\), then \(h_S\equiv-\infty\) and its conjugate is \(+\infty=\chi_\varnothing\); conversely the conjugate of \(\chi_\varnothing\equiv+\infty\) is \(-\infty=h_S\). Formula (*) still holds. This uses no sequential compactness, exchanged limits, unproved separation theorem, or smoothing.

### Sharpness of the original hypotheses

For \(M=\mathbb R\) and \(S=(0,1)\), \(h_S(n)=\max\{0,n\}\); its conjugate is \(\chi_{[0,1]}\ne\chi_S\). Thus closedness is necessary if one wants the indicator of **the original set**, rather than its closed convex hull. For \(S=\{-1,1\}\), \(h_S(n)=|n|\) and \(h_S^*=\chi_{[-1,1]}\ne\chi_S\); convexity is likewise necessary. Neither example contradicts the printed closed-convex identity.

## Mathematical disposition and dependency boundaries

**Proposed insertion:** place the projection argument after Example 21.11.25, preserve Rockafellar attribution, and keep all original source labels/permanent tags. The proof removes the need to *invoke* Roc70, Theorem 13.2, **for this one example only**; it does not prove the general Fenchel–Moreau theorem, certify Theorem 21.11.24, or verify uninspected §21.11 arguments. No explicit downstream invocation of 21.11.25 was established in this run; the only identified immediate dependent is that example's proof. No prior finding is reclassified.

**Actual review:** Def. 21.11.22 and equation 21.11.23, Example 21.11.25, contextual statement/proof of 21.11.24. Section 21.11 was previously partially visited, so **0 new first visits and 0 entire section certifications** (current table of contents 25 chapters/747 sections). User-excluded Demailly regularization/approximation and the dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss project remain **deferred-by-user**, not resolved. No production edits, build, tests, CI, formal verification or website publication.
