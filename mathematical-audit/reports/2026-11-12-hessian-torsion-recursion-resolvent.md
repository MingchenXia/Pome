# Resolvent form of the mixed Hessian torsion recursion

**Date:** 2026-11-12. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding:** `POME-HESS-TORSION-RECURRENCE-RESOLVENT-001` — **low / verified conditional deduction**. The printed Lemma 8.13.7 and Theorem 8.13.8 are **not** refuted. This note audits a previously unreviewed algebraic step and records a more explicit quantitative consequence, without claiming that the entire analytic construction is certified.

## Exact integrated reading anchors

- `docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html`, main blob `580d3bc2b10ebd01d880b2a31fc6930436570aac`: **Lemma 8.13.7**, source `non-kahler-pluripotential-theory:D2B92D4C`, permanent tag `0F8C3F6B0122`, physical lines **173–221**, especially the torsion estimate **183–194**, the maximum/Stokes argument **196–220**, and the two stated recurrences **174–178**.
- Same file/blob: **Theorem 8.13.8**, source `non-kahler-pluripotential-theory:AEE5FFB9`, permanent tag `B83D4B8CE619`, physical lines **226–273**, especially the recursive estimates **236–272**.
- Contextual analytic premises, **not fully recertified**: `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`, **Lemma 8.2.7** permanent `B0643A9A1173`, lines **160–179** (absolute coefficient domination for degrees strictly below m); `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html`, blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`, **Theorem 8.11.12** permanent `C044CD1C65C4`, lines **282–293** (joint decreasing products); `docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html`, blob `8750df56019c14e16704607ca20fa8b90f137fb0`, **Lemma 8.12.4** permanent `3A8C156268BF`, lines **97–110** (weighted signed torsion measures).

## Assumptions and precise improvement

Work on the same compact Hermitian complex manifold as in §8.13, with `1 <= m <= n`. Let `u,v` be **bounded admissible potentials**, `0<alpha<1`, `eta=1-alpha`, `V=alpha v`, `S=inf_X(u-V)`, and `E_s={u<V+S+s}`. As in the printed proof define the finite nonnegative mixed masses

\[
 b_{p,q}=M_{p,q}(E_s),\qquad a_k=b_{k,0}\quad(0\leq k\leq m).
\]

The following refinement is **conditional on the two inequalities actually established in Lemma 8.13.7**, rather than on any unexamined smoothing argument:

\[
\tag{A}
b_{p,q+1}\le b_{p+1,q}
 +C_0s\sum_{a+d\le p+q}b_{a,d},
\qquad p+q<m;
\]
\[
\tag{B}
\eta a_k\le a_{k+1}
+C_3s(a_k+a_{k-1}+a_{k-2}),\quad
0\le k<m,\quad a_{-1}=a_{-2}=0.
\]

There exist explicit positive constants `C_1=C_0m^2` and `C_2=C_1(1+C_1)^{m-1}`, depending only on the Lemma's fixed torsion constant and `m`, for which, whenever

\[
0<s\le1,\qquad \delta:=C_3s\eta^{-3},
\qquad 3m\delta<1,
\]
one has the **resolvent-type comparison**
\[
\boxed{\quad
b_{0,m}\le
\left[
 1+\frac{C_2s}{1-3mC_3s\eta^{-3}}
   \sum_{j=1}^{m}\eta^{-j}
\right]a_m.
\quad}
\tag{R}
\]
In particular this holds **without dividing by `a_m`** when `a_m=0`. For fixed `eta` and small `s` it directly implies the printed `1+C s/eta^m` estimate. It retains the full geometric sum instead of bounding every term by `eta^{-m}`, and it tracks the positive absorption denominator instead of silently replacing it by 2. It is a refinement of the **algebraic conclusion**, not an assertion that the `eta^3` condition is geometrically sharp.

## Complete algebraic proof, with all indices visible

Define
\[
A_r=\max_{p+q=r}b_{p,q}\quad(0\le r\le m);
\qquad A_0=a_0.
\]
At fixed total degree `r`, apply (A) at most `r` times to move each `V` slot to a `u` slot. The right-hand error at each move is bounded by
\[
C_0s\sum_{d=0}^{r-1}(d+1)A_d.
\]
Since `r<=m`, `d+1<=m`, this proves for `r>=1`
\[
A_r\le a_r+C_1s\sum_{d<r}A_d,\qquad C_1=C_0m^2.
\tag{1}
\]
**No comparison between masses of different degrees has been used yet.**

By elementary induction on `r`, (1) gives the explicit finite discrete Grönwall bound
\[
A_r\le a_r+C_1s\sum_{k=0}^{r-1}
                 (1+C_1s)^{r-1-k}a_k.
\tag{2}
\]
For `0<s<=1`, set `C_2=C_1(1+C_1)^{m-1}`. Taking `r=m` and using `b_{0,m}<=A_m` gives
\[
b_{0,m}\le a_m+C_2s\sum_{k<m}a_k.
\tag{3}
\]
This checks the printed multi-slot recurrence independently of any degree-lowering argument.

Now define `B_k=eta^{m-k}a_k` for `0<=k<=m`, and `B_{-1}=B_{-2}=0`. Multiplication of (B) by `eta^{m-k-1}` yields exactly
\[
B_k\le B_{k+1}
 +C_3s\left(\eta^{-1}B_k+
                 \eta^{-2}B_{k-1}+
                 \eta^{-3}B_{k-2}\right).
\]
Because `0<eta<1`, each coefficient is at most `delta=C_3s eta^{-3}`; hence
\[
B_k\le B_{k+1}
 +\delta(B_k+B_{k-1}+B_{k-2}).
\tag{4}
\]
Let `M=max_{0<=k<m}B_k`. Summing (4) for `k=j,...,m-1` gives, for every `j<m`,
\[
B_j\le B_m+3m\delta M.
\]
It follows that
\[
(1-3m\delta)M\le B_m
\quad\Longrightarrow\quad
a_k\le
\frac{\eta^{-(m-k)}}{1-3m\delta}\,a_m,\quad k<m.
\tag{5}
\]
This includes `a_m=0`: if the denominator is positive, (5) forces **all** lower diagonal masses to vanish, with no illicit division by zero. Sum (5) for `k=0,...,m-1` and substitute into (3). This gives (R), exactly.

A useful separate check at Hessian degree one is that the single diagonal inequality already yields
\[
a_0\le\frac{a_1}{\eta-C_3s}
\quad\text{if }C_3s<\eta;
\]
thus the cubic smallness condition is a **uniform all-degree sufficient condition**, not an optimal numerical threshold for `m=1`.

## What the analytic proof still requires

The algebra above assumes (A)–(B), which are precisely the printed Lemma 8.13.7's consequences. The original proof of (A) uses: positivity/locality for mixed maxima in §8.12.2; degree-`<m` coefficient control via §8.2.7; Stokes and *weighted* signed-current convergence (§8.12.4) for the difference of two decreasing potentials, which need **not** decrease; and joint measure convergence (§8.11.12). A mere weak convergence of unweighted measures does **not** justify multiplication by the moving `w_j-u_j`. These analytic inputs and any referenced admissible smoothing/existence mechanisms have **not been independently certified** in this checkpoint. In particular this report does not reopen the owner-excluded Demailly approximation/regularization or the Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programmes; any related dependency remains **deferred-by-user**.

## Classification, proposed action, dependents and coverage

- **Finding status:** `verified conditional deduction` (**low**). The finite-recursion implication and its constants are proved here; no false theorem, independent analytic repair, formal verification, or full-source proof certification is claimed.
- **Proposed correction:** optional explanatory remark immediately after Theorem 8.13.8 giving (R) as a sharper algebraic comparison **conditional on Lemma 8.13.7**; **no production/source/canonicalization edit was made**.
- **Affected dependents:** Theorem 8.13.10's strict domination argument (and Corollary 8.13.11) uses the weaker printed estimate. Its use remains valid; (R) may replace that input with a more explicit prefactor but is not required for its correctness. No new analytic comparison principle is claimed.
- **Actual coverage:** First new *proof-level subresult* inspection of **§8.13.7–8** in this checkpoint, plus a contextual hypothesis/dependency crosscheck of §§8.2.7, 8.11.12, 8.12.4. §8.13 and those other numbered sections were **already partly visited** in previous audit records: **0 new first-visited numbered sections, 0 entire-section certifications**. Current main ToC: **25 chapters and 747 numbered sections**. No tests, build, CI, publication or site edit performed.
- **Duplication check:** Earlier `POME-HESS-ONESIDED-MEASURE-001` concerns one-sided domination; `POME-HESS-GAUD-TRACE-SECOND-MASS-001` concerns a Gauduchon but non-`dd^c`-closed torus example. Neither supplies the resolvent-type all-degree recursion (R). Those findings are unchanged.
