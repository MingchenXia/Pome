# Quantitative one-sided convex slopes, mixed Alexandrov proof reuse, and nonclosed residual classes

**Review date:** 2026-11-23 (Asia/Shanghai). **Production main audited:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **Status:** one low-severity verified conditional deduction; no newly confirmed false theorem or source error; no completed transitive proof-chain certificate.

## Exact integrated reading-edition coverage

1. **Complete present-main mathematical direct reading:** §21.11, **docs/sections/convex-functions-and-convex-bodies/index.html**, blob **2a123a863642a5a75caa173f0f73aff439a02ea4**, physical mathematical lines **9–925**, containing all five current subsections 21.11.1, 21.11.21, 21.11.40, 21.11.49, 21.11.59. Section permanent tag **9A65EFDDFA3F**, source **sgpt**. This is complete *reading and stepwise audit*, not a certification of every transitive cited premise, nor a claim of first-ever historic coverage.
2. **Selected nonexcluded direct reading only:** §10.30, **docs/sections/classes-with-a-nonclosed-background/index.html**, blob **3cebca63712deb760cf2399c06ca1b5a37b6d851**, mathematical lines **7–120 and 192–209**. Section permanent tag **FB4254C93740**, source **non-kahler-pluripotential-theory**. §10.30.6–8, lines **122–190**, contain the user's expressly excluded approximation/regularization programme and have **not** been audited or certified. They remain **deferred-by-user**. This is NOT a whole-section review.
3. **Selected cross-proof comparison only:** §21.5.4, **docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html**, blob **7089aa41ae2422b1bd6b5094e46668cbc8ed37be**, lines **99–156**. This was extensively reviewed in earlier audit sessions; its re-use here does not count as a new whole-section review.

## New finding: POME-CONVEX-ONE-SIDED-SLOPE-QUADRATIC-MODULUS-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false statement in Pome. **Anchor:** §21.11.63, source label **sgpt:F7AADC82**, permanent tag **66B643EAC79A**, lines **865–925**. The printed lemma assumes pointwise upper-limit control and equality at zero, and correctly obtains convergence of derivatives without a rate. The following is a separate finite-error variant with stronger **uniform** hypotheses.

**Proposition.** Let \(\rho>0\), \(L\ge0\), \(\eta,\delta\ge0\). Suppose \(f\) is finite convex and differentiable at \(0\) on an open interval containing \([-\rho,\rho]\), \(g\) is differentiable at \(0\), and
\[
g(t)\le g(0)+g'(0)t+\frac L2t^2\qquad (|t|\le\rho).
\]
Suppose further that \(f(0)\ge g(0)-\eta\) and \(f(t)\le g(t)+\delta\) for every \(|t|\le\rho\). Then, with \(a=f'(0)-g'(0)\), for **every** \(0<h\le\rho\),
\[
\boxed{|a|\le \frac L2h+\frac{\eta+\delta}{h}.}\tag{A}
\]
If \(L>0\) and \(\eta+\delta\le L\rho^2/2\), optimization gives the **sharp**
\[
\boxed{|f'(0)-g'(0)|\le\sqrt{2L(\eta+\delta)}.}\tag{B}
\]
For \(L=0\), (A) gives \(|a|\le(\eta+\delta)/\rho\). The general nonoptimized bound (A) remains valid outside the small-error range.

**Complete proof.** Convexity and differentiability of \(f\) give \(f(t)\ge f(0)+f'(0)t\). The two majorizations and the lower normalization of \(f(0)\) yield
\[
a\,t\le g(t)+\delta-f(0)-g'(0)t
\le \eta+\delta+\tfrac L2t^2.
\]
For \(a\ne0\), put \(t=h\,\operatorname{sgn}(a)\); for \(a=0\) the inequality is automatic. Division by \(h\) proves (A). For \(L>0\), the right side is minimized at \(h=\sqrt{2(\eta+\delta)/L}\); the stated restriction ensures \(h\le\rho\), and gives (B). If \(\eta+\delta=0\), apply (A) and let \(h\downarrow0\) to obtain \(a=0\).

**Optimality, including the numeric constant and exponent.** Let \(L>0\), choose \(|a|\le L\rho\), and set \(g(t)=Lt^2/2\), \(f(t)=at\), \(\eta=0\), \(\delta=a^2/(2L)\) on all of \(\mathbb R\). Both functions are smooth convex, \(f(0)=g(0)=0\), and
\[
g(t)+\delta-f(t)=\tfrac L2(t-a/L)^2\ge0
\]
for every \(t\). Then \(|f'(0)-g'(0)|=|a|=\sqrt{2L\delta}\), so neither the constant \(\sqrt2\) nor the exponent \(1/2\) can be improved under these hypotheses. For \(L=0\), the linear model \(g=0,\ f(t)=at,\ \delta=|a|\rho\) saturates the endpoint bound (with \(\eta=0\)).

**Interpretation and dependency:** This is a quantitative, uniform-barrier corollary adjacent to the qualitative convex derivative convergence of §21.11.63. **Uniform** error control near zero is essential for (A)/(B); the weaker pointwise limsup hypothesis of the printed lemma does **not** furnish these rates. The proof above is elementary, independent of Demailly regularization and of the mixed-Monge–Ampère input. No amendment to the original lemma is required. Potential downstream applications: variational one-sided derivative arguments in **§11.34–11.38** and differentiating geodesic energy in **§17.16**, but no such application has been certified here. Suggested optional change: a separate reviewable quantitative remark, not a source/registry edit.

## Cross-source equivalence and genuine duplicate-control check (NO NEW DEFECT)

- §21.11.58, source **sgpt:AE125FCA**, permanent **59E2455286B4**, lines **741–769**, asserts a positive symmetric multilinear mixed real Alexandrov measure for **every n-tuple of finite convex functions on the full \(N_\mathbb R\)**, with \(n!\) normalization, diagonal identity, and polynomial expansion.
- §21.5.4, source **foundations-of-pluripotential-theory:EAD83A50**, permanent **5D8A7A7D734E**, lines **99–156**, already constructs that same normalized object under the **same finite-convex domain and positivity hypotheses**, proves the symmetric multilinearity and diagonal identity, and additionally supplies vague continuity. Its tagged polarization formula is §21.5.5, source **foundations-of-pluripotential-theory:24CC29A7**, permanent **D38381F0AC43**, lines **143–156**. The factor is exactly \(1/n!\).
- Crucially, the actual **replacement proof** at §21.11 lines **767–768** already contains **data-proof-entry=5D8A7A7D734E** and cites that internal construction. Thus this is **intentional, already internally bridged, mathematically equivalent cross-source coverage**, not a fresh uncaught duplication defect or an occasion to delete one version. Both permanent tags, the stronger continuity clause, the source attribution [CLM22, TW02, PR04], and provenance are preserved. There is no new finding ID for the existing overlap.

Also checked the distinct boundary/domain hypotheses of §21.11.12, §21.11.13 (decreasing **nets**, not sequences), §21.11.24 (improper conjugates), §21.11.36–38 (relative interiors and common closed domains), §21.11.47 (compactness of the first dual slope body), §21.11.53 (zero-volume bodies), §21.11.55 (vague, not narrow, convergence), §21.11.57 (almost-everywhere dual gradient), and §21.11.60–63 (convex hull and signed finite-slope tests). These checks do **not** convert source-cited deep convex-analysis theorems into fully certified transitive proofs.

## Separate nonclosed-background rotation (selected only)

**§10.30.2**, source **non-kahler-pluripotential-theory:E64A72AA**, permanent **5F6B6BF8B562**, lines **33–54**. The affine identification
\[
\mathscr A_Z(\theta)=\{\pi^*\theta\}+H^{1,1}_{BC}(Z,\mathbb R)
\]
and modification formulas are compatible with the prescribed exterior derivative. Pushforward of the smooth pulled-back background under the proper degree-one map is the original background as a current; translation by **closed** Bott–Chern classes then gives \(g_*g^*=\mathrm{id}\). We specifically did **not** replace the required smooth-pullback definition by an arbitrary singular-current pullback.

**§10.30.4–5**, source labels **BB7B408A / 01E705E1**, permanent tags **28C8F709D1CC / 9157A5A52988**, lines **64–111**. For the trace current identity \(S_{Z'}=g^*S_Z+[E_g]\) with **effective exceptional** \(E_g\), subtracting gives the **minus sign**
\[
\mathbb B_{Z'}=g^*\mathbb B_Z-\{[E_g]\}_{BC}.
\]
All terms have prescribed derivative \(\pi'^*d\theta\) because \(S_Z\) and \([E_g]\) are closed. The proof is a correct **conditional** deduction of §20.4.26; that full predecessor chain remains unresolved.

**§10.30.10**, source label **67D67B9B**, permanent tag **6436A9863EBA**, lines **194–209**. Trivial multiplier ideals imply vanishing divisorial orders and equality of the residual affine class of \(U\) and the smooth zero potential. The infinite extended mass assertion remains **conditional on §13.14.18**; equal affine divisor data alone do not bound extended Monge–Ampère mass. No new false theorem was established.

**Explicit exclusion boundary:** §10.30.7–8's analytic-singularity approximation and residual-current limit, lines **122–190**, are **deferred-by-user**, not resolved, not audited via their premises and not silently used to certify the above independent checks. The same applies to the dedicated Demailly, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes.

## Actual count and remaining gaps

**One** new entire direct §21.11 reading; **one** selected §10.30 nonexcluded review; **one** selected §21.5.4 repeat comparison (not new full coverage); **one** new low-severity verified conditional deduction; **zero** new confirmed printed errors; **zero** fully certified transitive proof chains. No assertions about historical first visits or total project verification.

Remaining nonexcluded dependencies include the fine details of §21.11.17/24 finite-dimensional closed-duality and §20.4.26 exceptional trace cocycles, plus §13.14.18's infinite-mass example. Previous ledger findings remain as recorded, including unresolved items and user-deferred categories. No builds, tests, CI, publication, main/source/proof-registry/permanent-tag changes, or PR creation/merge were performed. Existing audit PR #9 was observed **closed/merged**; no duplicate PR was created.
