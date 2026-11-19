# 2026-11-19 — §21.6 complete direct proof audit: compactly indexed envelopes versus countable nonclosure

## Immutable reading baseline and scope

- **Reviewed `main` SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading text:** `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, blob `b3b4e34fff767a717df812a381f905589b257fb3`, **entire mathematical portion, physical lines 5–47**.
- **Source and permanent anchors:** `foundations-of-pluripotential-theory:30FFD831` / `FCDAD9CEC8CE` (Lemma 21.6.1, lines 10–29); `foundations-of-pluripotential-theory:55EDF0D7` / `F2FABB0A312F` (Lemma 21.6.2, lines 32–47).
- **Crosschecked but not fully certified:** `docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html`, blob `347fa1f0fc35c13b1d1c45193ab997ed456966e4`, Proposition 21.3.3(2), source `foundations-of-pluripotential-theory:E93FCB56` / tag `53A9D470F1AC` (lines 63–123); `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, Theorem 21.5.2, source `foundations-of-pluripotential-theory:6403CF44` / tag `F4072D9ED060` (lines 43–87).
- **Result:** No false statement or independent proof gap found in either printed lemma. The two findings below extend or delimit Lemma 21.6.1; they do **not** change its finite-family hypothesis. They are separate from the previously recorded **noncompact-domain** counterexample `POME-CONVEX-NONCOMPACT-HULL-NONATTAIN-001` and from the existing full-mass Wasserstein nonupgrade.

## Finding POME-CONVEX-COMPACT-PARAMETER-ENVELOPE-001

**Severity:** low. **Status:** verified conditional deduction. **Location:** §21.6.1, lines 10–29; use Proposition 21.3.3(2), lines 63–123. **Proposed use:** optional separately reviewed supplement, not an alteration of the printed theorem. **Affected dependents:** any later use of compactly parameterized convex families, including toric-envelope constructions; no unverified direct citation asserted.

**Statement.** Let \(W\) be a finite-dimensional real vector space of dimension \(d\), \(K\subset W\) compact, and \(T\) a nonempty **compact metric** parameter space. For every \(t\in T\), let \(G_t:W\to(-\infty,+\infty]\) be proper lower-semicontinuous convex, with \(\operatorname{dom}G_t\subset K\). Assume the map
\[
(t,x)\longmapsto G_t(x)
\]
is **jointly lower semicontinuous** on \(T\times K\). Let \(H\) be the convex envelope in Proposition 21.3.3(2), using arbitrary finite admissible barycentric combinations from the indexed family. Then \(H\) is proper, closed and convex, **each finite value \(H(x)\) is attained by a combination of at most \(d+2\) terms**, and
\[
H=H^{**}=\bigl(\sup_{t\in T}G_t^*\bigr)^*.
\]
No assumption of a finite number of distinct functions is needed, but compactness of the index and *joint* l.s.c. are part of the claim.

**Proof.**

1. Joint l.s.c. and compactness of \(T\times K\), with no value \(-\infty\), provide a **common finite lower bound** \(B\) on all \(G_t|_K\). Indeed otherwise a sequence \((t_j,x_j)\) with \(G_{t_j}(x_j)\le-j\) has a convergent subsequence and violates joint l.s.c. at its limit. Each \(G_t\) is proper, so the family has a finite value somewhere; therefore \(B\le H\) and \(H\) is not identically \(+\infty\).
2. An admissible finite combination with value \(s=\sum_i\lambda_i G_{t_i}(x_i)\) represents the point \((x,s)\) as a convex combination of points \((x_i,G_{t_i}(x_i))\in W\times\mathbb R\). **Carathéodory's elementary reduction** in dimension \(d+1\) replaces this combination by one of at most \(d+2\) such points without changing \((x,s)\). For completeness, if more than \(d+2\) points occur, an affine dependence \(\sum_i c_i=0\), \(\sum_i c_i(x_i,G_{t_i}(x_i))=0\) permits replacing \(\lambda_i\) by \(\lambda_i-\varepsilon c_i\) until one nonnegative weight vanishes; iterate. Thus all infima may be computed using at most \(d+2\) terms.
3. Suppose \(x_j\to x\) and \(H(x_j)\to L<+\infty\), after taking a subsequence realizing a finite liminf. Choose combinations of at most \(d+2\) terms, each with value between \(H(x_j)\) and \(H(x_j)+1/j\); pad with zero weights using a fixed finite-domain pair. Since \(T\times K\) and the weight simplex are compact **metric**, pass to a subsequence with \(t_{i,j}\to t_i\), \(x_{i,j}\to x_i\), \(\lambda_{i,j}\to\lambda_i\) for every \(i\). Terms with \(\lambda_i=0\) disappear from the barycenter, while for terms with \(\lambda_i>0\) the common lower bound and bounded total cost imply finite limit cost; joint l.s.c. implies
\[
\sum_{\lambda_i>0}\lambda_iG_{t_i}(x_i)
 \le\liminf_j\sum_i\lambda_{i,j}G_{t_{i,j}}(x_{i,j})=L.
\]
The limiting positive-weight points are admissible and have barycenter \(x\). Hence \(H(x)\le L\), proving l.s.c. (the case of an infinite liminf is automatic). Convexity and \(H^*=\sup_tG_t^*\) are precisely Proposition 21.3.3(2). The lower bound and a finite value make \(H\) proper.
4. Apply the same compactness argument to a sequence of admissible combinations with fixed barycenter \(x\) and costs decreasing to a finite \(H(x)\). Its limit is an admissible combination with cost at most \(H(x)\), hence exactly \(H(x)\): **attainment**. Finally, the Fenchel–Moreau identity for the now closed proper convex \(H\) gives the displayed conjugacy.

This argument uses sequences only in the explicitly **compact metric** product \(T\times K\); it makes no sequential-compactness assertion for arbitrary compact parameter spaces, and does not interchange unrelated limits.

## Finding POME-CONVEX-COUNTABLE-COMPACT-DOMAIN-NONCLOSED-001

**Severity:** low. **Status:** verified conditional deduction (explicit counterexample to a *hypothetical* infinite-family extension, **not** to printed Lemma 21.6.1). **Location:** §21.6.1, lines 10–29; §21.3.3(2), lines 63–123. **Correction/boundary:** retain the printed finite-family quantifier; for the generalization above require a compact index with joint l.s.c.

On \(W=\mathbb R\) let \(K=[0,1]\) and for every integer \(n\ge1\) define the closed proper convex indicator
\[
G_n=I_{\{1/n\}},\qquad
I_A(x)=\begin{cases}0,&x\in A,\\+\infty,&x\notin A.\end{cases}
\]
Every \(\operatorname{dom}G_n=\{1/n\}\subset K\), and the family has the uniform lower bound (0). An admissible *finite* barycentric combination of these singleton domains has a positive barycenter at most (1). Conversely every \(x\in(0,1]\) belongs to the convex hull of two sufficiently chosen \(1/n\)'s (the endpoint \(x=1\) is also one of them). Since all costs are zero, the exact convex envelope is
\[
H=I_{\((0,1]\)}.
\]
This is proper and convex but **not lower semicontinuous at (0)**, despite compact common domain containment and every individual \(G_n\) being closed. Its finite infima happen to be attained, showing that *closure* fails even without an attainment failure.

Indeed \(G_n^*(y)=y/n\), so
\[
H^*(y)=\sup_{n\ge1}y/n=\max(y,0),\qquad
\bigl(\sup_nG_n^*\bigr)^*=I_{[0,1]}\ne H.
\]
This exactly identifies the missing boundary point. One can realize the same family with a compact metric index \(T=\{0\}\cup\{1/n:n\ge1\}\) by assigning \(G_0=I_{\{1\}}\); the resulting family is **not jointly l.s.c.** at \((0,0)\), where \(G_{1/n}(1/n)=0\) tends to a point with \(G_0(0)=+\infty\). Thus neither the mere compactness of all spatial domains nor a compact index *without* joint l.s.c. ensures closure.

## Entire direct §21.6 proof assessment

- **Lemma 21.6.1:** Verified the lower-bound argument via the l.s.c. open cover of \(K\), merging repeated *finite* function indices by Jensen's inequality, compactness of the finite weight simplex, the lower-semicontinuity liminf (including vanishing weights), attainment by a constant barycenter sequence, and the conjugacy via §§21.3.2–3 and 21.4.2. No claim of closure for infinite families appears in the actual theorem.
- **Lemma 21.6.2:** For vague convergence plus convergence of total finite positive masses, the compact-support cutoff \(\eta\) makes \(\int(1-\eta)\,d\mu_j\to\int(1-\eta)\,d\mu\), giving eventual tightness and hence narrow convergence. The subsequent full-mass Alexandrov/real-MA application invokes Theorem 21.5.2 for vague convergence and the common mass \(n!\operatorname{vol}P\). This last transitive proof chain was **not** independently certified here. There is no assertion of \(W_1\), moment, or setwise convergence (previously documented counterexamples are not recounted as new findings).

**Audit accounting:** §21.6 was already partially visited, so **+0 first section visits, +1 full direct section proof reading, +0 complete transitive dependency certifications**. The actual ToC matrix remains **25 chapters / 747 numbered sections**. The prior noncompact-domain warning and all other ledger entries are retained. Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss programmes remain **deferred-by-user**, neither resumed nor certified. No source edits, build, test, Actions CI, or publication.
