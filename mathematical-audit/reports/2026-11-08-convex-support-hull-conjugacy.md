# Arbitrary-set support conjugacy: a self-contained replacement for §21.11.25

- **Finding:** `POME-CONVEX-SUPPORT-HULL-CONJUGACY-001`.
- **Severity/status:** low; **verified repair** (a complete *proposed* internal proof for a cited external input); the printed Example 21.11.25 is correct, not a false theorem. The additional arbitrary-set identity is a verified conditional deduction from finite-dimensional convex separation.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **integrated file:** `docs/sections/convex-functions-and-convex-bodies/index.html`; **blob:** `2a123a863642a5a75caa173f0f73aff439a02ea4`.
- **Precise targets:** Definition 21.11.22 (`sgpt:8B018B53`, permanent `2E5E29E9A58B`, physical lines 214–220); conjugate equation 21.11.23 (`sgpt:E288ED21`, permanent `E1AD8A1437E2`, lines 216–220); Example 21.11.25 (`sgpt:8297B2F5`, permanent `1A7C0B007516`, lines 234–239). Context: Theorem 21.11.24 (`sgpt:1A7E065D`, permanent `258227E5D497`, lines 223–232).
- **Existing proof dependency:** Example 21.11.25 cites Rockafellar 1970, Theorem 13.2 rather than proving this specific identity. This audit replaces **only that finite-dimensional support/indicator identity**, not the general Fenchel–Moreau theorem, the entirety of Rockafellar, or all convex-analytic arguments elsewhere.
- **Permitted change:** proposed audit proof only; no edit of a canonical statement, historical attribution, source, permanent tag, proof registry, or production HTML.

## Complete elementary argument (including nonclosed, nonconvex and empty sets)

Let `M` be a finite-dimensional real vector space, `N=M^*` its dual, and `S⊂M` an *arbitrary* subset. Define the support function
[
h_S(n)=sup_{sin S}langle s,nangle,
]
with the extended-real convention (suparnothing=-infty). Put (chi_S(m)=0) on (S) and (+infty) outside it. Write (K=overline{operatorname{conv}}S), with (K=arnothing) for (S=arnothing). The claimed strengthened identities are
[
oxed{quad (chi_S)^*=h_S,qquad (h_S)^*=chi_K,qquad
(chi_S)^{**}=chi_K.quad}
]
The conjugate of (chi_S) is (h_S) immediately from its definition, including the empty-set convention. Every linear functional has the same supremum on (S), its convex hull, and its closure (allowing (+infty)); hence (h_S=h_K).

Suppose first that (S
earnothing), so (K) is nonempty, closed, convex. For (min K), (h_K(n)gelangle m,nangle) for every (n), and equality is obtained in the conjugate supremum at (n=0). Thus (h_K^*(m)=0).

For (m
otin K), choose any Euclidean inner product on (M). A point (pin K) minimizing (|m-p|) exists: restrict the closed set (K) to a sufficiently large compact ball, using any fixed point of (K) for a distance bound. Let (v=m-p
e0), and identify (v) with a functional (n_vin N) by (n_v(q)=langle v,qangle_{m Euc}). For every (qin K), the point (p+t(q-p)) belongs to (K) for (0le tle1). Minimality of (p) and the right derivative at (t=0) of the squared distance imply
[
langle v,q-pangle_{m Euc}le0.
]
Consequently (h_K(n_v)=n_v(p)<+infty), and
[
n_v(m)-h_K(n_v)=|m-p|^2>0.
]
By positive homogeneity, replacing (n_v) by (tn_v), (t	o+infty), makes this difference arbitrarily large. Hence (h_K^*(m)=+infty). This proves (h_S^*=chi_K) and the biconjugate assertion.

If (S=arnothing), then (h_Sequiv-infty), (h_S^*equiv+infty=chi_arnothing), and ((chi_arnothing)^*equiv-infty), so the same three equations hold. No sequential compactness, interchange of infinite limits, unquoted separation theorem, or regularization is used.

### Sharp hypothesis diagnostics

For (M=mathbb R), (S=(0,1)), one computes (h_S(n)=max{0,n}), so (h_S^*=chi_{[0,1]}
echi_S): **closedness cannot be dropped** from the printed Example. For (S={-1,1}), (h_S(n)=|n|), so (h_S^*=chi_{[-1,1]}
echi_S): **convexity cannot be dropped**. The general formula correctly restores the closed convex hull in both cases. Neither case contradicts the printed closed-convex example.

## Disposition, dependents and coverage

The proposed correction is to insert the Euclidean projection proof immediately after Example 21.11.25 while **retaining** the historical Rockafellar citation. No change to its mathematical statement is needed. The result is also applicable to indicator functions of nonclosed or nonconvex sets if a later argument encounters them, but no direct downstream citation was established in this review. Theorem 21.11.24 and the remaining §21.11 convex duality are **not** certified by this isolated argument. The review consisted of the displayed definition/conjugate and Example 21.11.25, its cited reference, and nearby Theorem 21.11.24 as context; no other §21.11 propositions were newly rechecked.

**Scope boundary:** all user-deferred Demailly approximation/regularization and its dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, neither proved nor certified. No project tests, builds, formal verification, CI, source edits or website publication were performed.
