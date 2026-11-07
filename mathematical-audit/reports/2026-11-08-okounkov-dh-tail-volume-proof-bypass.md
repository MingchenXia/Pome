# 2026-11-08 — Direct tail-volume proof of Okounkov Duistermaat–Heckman convergence

**Finding POME-DH-TAIL-VOLUME-PROOF-001 — medium / verified repair (proposed replacement proof, not yet integrated).**
**Finding POME-DH-HEAVYTAIL-NOT-MOMENT-001 — low / verified conditional deduction.**

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Audit branch at inspection:** review/mathematical-audit, head e038d56fa610c413982df97a37d73f8129088665.
**Excluded scope:** No Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss arguments were consulted or attempted.

## Exact integrated locations

1. docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html, main blob 20ff3089e62dd1c8349e8bcc077ec64605a9788b: Definition 19.6.1 (physical lines 17–48; source sgpt:26A94CBB, permanent ACD722F45231); Proposition 19.6.4 (lines 56–92; sgpt:5FBEF833, permanent 29A7DDA38CA2); Definition 19.6.7 (lines 113–133; sgpt:2E276BD3, permanent 7B20D9977149); Proposition 19.6.16 (lines 278–326; sgpt:5E98C990, permanent D70EFA3100C9); Definition 19.6.18 (lines 329–335; sgpt:09132002, permanent 51940EF88F4F); Lemma 19.6.22 (lines 371–409; sgpt:B9C8ADE8, permanent 9C05354365F4); Lemma 19.6.23 (lines 411–444; sgpt:19978809, permanent 22B2EF8281A7).
2. docs/sections/non-archimedean-pluripotential-theory/index.html, main blob 8448d710690ebe1cc28040f9611d05c9d008a961: Definition 22.1.55 (lines 908–914; sgpt:115B0C00, permanent 9ADEFD2FF381), Theorem 22.1.56 (lines 916–1008, contextual), Proposition 22.1.60 (lines 1012–1093; sgpt:3E4F1C70, permanent 492A145E9067), its second alternative (source clause sgpt:6F9C2E90, permanent 75E1B24CB49A), and Eq. 22.1.62 (sgpt:969A6D8B, permanent 636AFE1086C1).

## Proof risk in the printed argument

The printed proof of Lemma 19.6.23 explicitly invokes the pointwise convergence Proposition 19.6.16 to establish convergence of the concave transforms almost everywhere. Proposition 19.6.16 has a **pre-existing, separately recorded confirmed-error classification** in the audit. This audit does not reopen or reclassify that statement and does **not** infer that Lemma 19.6.23 itself is false. Its stated measure convergence has a direct proof that bypasses Proposition 19.6.16 entirely. The same argument covers Lemma 19.6.22 and the specific use of 19.6.23 in Proposition 22.1.60(2).

## Replacement proof: a distribution identity

Let K be an n-dimensional convex body and (K_t)_{t<b} an Okounkov test curve of Definition 19.6.1, with concave transform G and finite positive measure μ=G_*(1_K dx). For each t<b,

\[
\boxed{\quad \mu([t,\infty))=\operatorname{vol}_n(K_t).\quad} \tag{A}
\]

Indeed, x in K_t implies G(x)≥t. Conversely, if G(x)≥t, then x belongs to K_s for every s<t (use the downward nesting and the definition as a supremum, also when G(x)=t). The left-continuity identity K_t=intersection_{s<t}K_s, established in Proposition 19.6.4, gives x in K_t. Thus {G≥t}=K_t, including boundary points; the test function can equal -∞ only on a Lebesgue-null subset of the boundary because it is finite in the interior.

**Elementary moving-body input.** If compact convex bodies K_i converge to K in Hausdorff distance, their volumes converge. For completeness, all K_i lie in a common compact ball; 1_{K_i}→1_K at every interior and exterior point of K. Interior membership eventually follows by separating a supposedly omitted point a∈Int K from K_i: its positive distance to every supporting hyperplane of K contradicts uniform convergence of support functions h_{K_i}→h_K. Exterior exclusion is immediate from Hausdorff convergence. The boundary of a convex body has Lebesgue measure zero; dominated convergence proves volume convergence. The same argument works for fixed-level bodies, and for sequences it needs no unproved sequential compactness assertion about a different space.

Now suppose the hypotheses of either Lemma 19.6.22 (decreasing family) or Lemma 19.6.23 (increasing family). Write K_i, b_i, K^i_t and G_i for the base bodies, terminal parameters, levels and transforms, and K,b,K_t,G for their limits. By hypothesis, b_i→b, K_i→K and, for every t<b, K^i_t→K_t in Hausdorff distance (eventually t<b_i). Hence by (A) and moving-body volume continuity,

\[
\mu_i([t,\infty))=\operatorname{vol}_n(K^i_t)
\longrightarrow \operatorname{vol}_n(K_t)=\mu([t,\infty)),\qquad t<b.
\]

For t>b both tails eventually vanish because b_i→b. In addition,

\[
\mu_i(\mathbb R)=\operatorname{vol}_n(K_i)\longrightarrow
\operatorname{vol}_n(K)=\mu(\mathbb R).
\]

For t<b the tail of μ is continuous: Proposition 19.6.4 shows t↦K_t Hausdorff-continuous and thus t↦vol(K_t) continuous, so μ has no atom there. For t>b the tail is identically zero. A possible atom **at the terminal value b** must not be discarded; the portmanteau/distribution-function criterion requires convergence only at continuity points. The displayed tail and total-mass limits therefore give **narrow convergence of finite measures**, not merely vague convergence. Alternatively, mass convergence plus the tail identity gives tightness toward -∞, while b_i is eventually uniformly bounded above.

This verifies both convergence lemmas by their own stated hypotheses, without evaluating G_i at any single point of K and without invoking Proposition 19.6.16. It also avoids unjustified interchange of an increasing limit with a terminal truncation.

## Consequence for the non-Archimedean passage

The *specific* downstream use in Proposition 22.1.60(2), physical line 1090, invokes Lemma 19.6.23. Once the latter is replaced by the distribution proof above, this particular downstream step no longer depends on the previously disputed pointwise transform statement. This does **not** certify Proposition 22.1.60 in full: verifying that its non-Archimedean increasing limits satisfy the required flag-wise Hausdorff level convergence and base-body convergence remains a separate analytic/geometric dependency (in particular the cited §§16.4, 16.9 and 19.5 inputs). Theorem 22.1.56, which also uses Lemma 19.6.22, benefits from the same local proof replacement, without obtaining a full theorem-chain certification.

The factor n! in Definition 22.1.55 simply rescales these finite measures, so the tail proof is compatible with the published DH normalization. It proves no general moment convergence.

## Sharp moment limitation in the abstract convex test-curve category

On K=[0,1], put

\[
G_i(x)=-\frac{1}{x+1/i},\qquad G(x)=
\begin{cases}-1/x,&0<x\leq1,\\-\infty,&x=0.\end{cases}
\]

Every G_i and G is concave and upper semicontinuous, and is finite on Int K. Let K^i_t={G_i≥t}, K_t={G≥t}. Each defines an Okounkov test curve by Definition 19.6.7 and Lemma 19.6.9. Their terminal parameters b_i=-i/(i+1) decrease to b=-1, and for every t<-1,

\[
K^i_t=\left[\max\{0,-1/t-1/i\},1\right]
\ \searrow\ K_t=[-1/t,1]
\]

in Hausdorff distance. Thus Lemma 19.6.22 applies and μ_i=(G_i)_*dx converges narrowly to μ=G_*dx. However,

\[
\int_{\mathbb R}|s|\,d\mu_i(s)
=\int_0^1\frac{dx}{x+1/i}
=\log(i+1)\longrightarrow+\infty,\qquad
\int_{\mathbb R}|s|\,d\mu(s)=+\infty.
\]

Consequently **narrow DH convergence does not imply convergence in W_1 or finite first moments**, even with one fixed base body and monotone, continuous, bounded test functions approximating an admissible unbounded test function. This is an abstract Okounkov-body example: **no assertion** is made that this particular curve arises from an I-model potential on a compact Kähler manifold.

## Proposed text-only repair (NOT applied to the reading edition)

Replace the proof of Lemma 19.6.23 by identity (A) plus convergence of convex-body volumes and finite total masses; optionally use the same concise proof for Lemma 19.6.22. Preserve both original lemmas, their alternative proof histories, source attribution, source and permanent tags, and all reader links. Keep the separate original Proposition 19.6.16 error open: a measure-level replacement is **not** a pointwise repair of that proposition. Add a caution that DH convergence alone has no moment or optimal-transport conclusion without uniform integrability.

**Coverage:** new proof-level inspection of the exact displayed statements/arguments cited above; §§19.6 and 22.1 were already partially sampled, so zero newly first-visited sections and zero fully certified sections. Inventory remains 25 chapters, 747 numbered sections, zero complete mathematical section certifications. No production files, source, canonicalization, tags, build, tests, CI, formalization or publication changed.
