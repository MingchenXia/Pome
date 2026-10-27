# 2026-10-28: bounded exponential equations and resolved blowup densities

**Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Review branch:** \`review/mathematical-audit\`. This note audits only specified integrated reading-edition passages; it does not certify the full sections or their upstream analytic dependencies.

## Scope and exact integrated sources

1. \`docs/sections/equations-with-prescribed-singularities--a-bounded-subsolution-theorem/index.html\`, blob \`6240b6dc071d12eac1476ed548736d012c1a4fa2\`: Theorem **15.10.1**, permanent tag **BA5CB37AAAC1**, lines **11–17**; fixed-reference mixed inequality (15.10.2), permanent equation tag **25E63CEC282C**, lines **66–79**; Step 2 uniform bound/limit argument, lines **58–107**.
2. \`docs/sections/equations-with-prescribed-singularities--equations-with-resolved-logarithmic-poles/index.html\`, blob \`bec2abe4e9b361a37adbf668837da42726b6dcda\`: resolved-logarithmic hypotheses (15.22.1), tag **1B942D170060**, lines **10–17**; Theorem **15.22.2**, tag **3B5397268E44**, lines **21–49**; Example **15.22.7**, tag **0362BBF11A0B**, lines **64–78**; Proposition **15.22.10**, tag **D1ADF0EFDD30**, lines **87–105**.
3. \`docs/sections/equations-with-prescribed-singularities--minimal-singularities-in-an-arbitrary-big-background/index.html\`, blob \`4805502723e87defe8ae12616a3d2d550fb8dd75\`: Theorem **15.16.2**, tag **352C3567BAAD**, lines **63–140**, **only** Steps 2–3, lines **87–140**, as comparison context.

These are permanent *reading-edition tags*. Their individual upstream original-source labels were not independently reconstructed during this run; no source-label mapping is conjectured. The mathematical hypotheses and proofs below are keyed to the stated integrated version, not to a same-numbered historical theorem.

## POME-BOUNDED-EXP-DENSITY-L1-STABILITY-001

**Severity:** low. **Status:** verified conditional deduction. **Printed Theorem 15.10.1 is not asserted false.**

Let \((X,\theta)\) satisfy the exact compact, semipositive and big hypotheses of Theorem 15.10.1. Fix a bounded \(\theta\)-psh function \(\psi\), its finite non-pluripolar measure \(\nu=\operatorname{MA}_\theta(\psi)\), and \(\lambda>0\). Suppose
\[
0\leq f_j,f\leq L\quad\nu\text{-a.e.},\qquad
\|f_j-f\|_{L^1(\nu)}\longrightarrow0,\qquad
\int_X f\,d\nu>0 .
\]
Eventually \(\int f_j\,d\nu>0\). Let \(u_j,u\) be the unique bounded solutions supplied by Theorem 15.10.1:
\[
\operatorname{MA}_\theta(u_j)=e^{\lambda u_j}f_j\nu,\qquad
\operatorname{MA}_\theta(u)=e^{\lambda u}f\nu.
\]
Then
\[
u_j\longrightarrow u\text{ in }L^1(X)\text{ and in }\theta\text{-capacity},\qquad
\|\operatorname{MA}_\theta(u_j)-\operatorname{MA}_\theta(u)\|_{\mathrm{TV}}\longrightarrow0 .
\]
Here total-variation norm of a signed measure with density \(g\) means \(\int|g|\,d\nu\). This assertion is **sequential**, and does not silently upgrade compactness to arbitrary nets.

**Proof, using precisely printed nonexcluded Step 2 dependencies.**
For a fixed sufficiently large \(C\), the inequality
\(e^{\lambda(\psi-C)}f_j\leq1\) gives
\(\operatorname{MA}_\theta(\psi-C)=\nu\geq e^{\lambda(\psi-C)}f_j\nu\).
Bounded exponential comparison therefore yields \(u_j\geq\psi-C\) uniformly.

We check that \(\sup_Xu_j\) is uniformly bounded above, even though no positive lower bound is assumed for \(f_j\). Otherwise take a subsequence with \(M_j=\sup_Xu_j\to+\infty\), put \(v_j=u_j-M_j\), and extract an \(L^1(X)\) limit \(v\) from normalized \(\theta\)-psh compactness. The exact integrated mixed inequality (15.10.2) (printed lines 66–79) gives
\[
e^{\lambda M_j/n}\int_X e^{\lambda v_j/n}f_j^{1/n}\,d\nu
\ \leq\ \int_X\theta_{v_j}\wedge\theta_\psi^{\,n-1}
\ \leq C_\psi .
\]
Lemma 5.44.2, used at printed lines 81–93, gives convergence of the exponentials in \(L^1(\nu)\). Since \(|a^{1/n}-b^{1/n}|^n\leq|a-b|\) for nonnegative \(a,b\), \(f_j^{1/n}\to f^{1/n}\) in \(L^1(\nu)\) as well, and all factors are uniformly bounded. Thus the displayed integral converges to
\(\int e^{\lambda v/n}f^{1/n}\,d\nu>0\):
\(\nu\) does not charge the pole set of the normalized psh limit and \(\int f\,d\nu>0\).
This contradicts \(M_j\to+\infty\). The right-hand trace bound is the exact previously established Lemma 5.29.20 used in the printed proof, not a theorem newly certified here.

Now the \(u_j\) lie between a fixed bounded lower barrier and a fixed upper constant. Each subsequence has an \(L^1\)-convergent subsubsequence, say \(u_{j_k}\to w\). The uniform domination
\(\operatorname{MA}_\theta(u_{j_k})\leq C\nu\)
permits application of the printed Corollary 15.9.4 to obtain capacity convergence and continuity of bounded Monge–Ampère products. Again by Lemma 5.44.2, \(e^{\lambda u_{j_k}}\to e^{\lambda w}\) in \(L^1(\nu)\), and
\[
\begin{split}
\int_X|e^{\lambda u_{j_k}}f_{j_k}-e^{\lambda w}f|\,d\nu
&\leq e^{\lambda M}\|f_{j_k}-f\|_{L^1(\nu)}\\
&\quad+L\|e^{\lambda u_{j_k}}-e^{\lambda w}\|_{L^1(\nu)}
\longrightarrow0 .
\end{split}
\]
(The constant \(M\) is the already established uniform upper bound.) Identifying the capacity-limit measure gives
\(\operatorname{MA}_\theta(w)=e^{\lambda w}f\nu\).
Uniqueness in Theorem 15.10.1 implies \(w=u\). If the full sequence did not converge in \(L^1\), or in capacity, it would contain a subsequence bounded away from its claimed limit, contradicting the just-established convergent-subsubsequence property. The displayed density estimate proves total-variation convergence for the full sequence.

**Proposed addition:** an explicitly *conditional* stability corollary following Theorem 15.10.1, with uniform density bounds and the positive limiting mass stated, and with proof dependencies 5.44.2, 5.29.20, 15.9.4 retained. **Affected dependents:** bounded exponential equation families, comparisons with §15.16 normalized solutions and §15.15 stability. This is not an independent proof of any underlying existence result.

## POME-BLOWUP-PUSHFORWARD-LP-CODIM-001

**Severity:** low. **Status:** verified conditional deduction. **Printed Example 15.22.7 is correct; this extends its point-center calculation.**

Let \(X\) be a compact complex \(n\)-fold with a smooth positive Hermitian form \(h\), let \(Z\subset X\) be a smooth complex submanifold of codimension \(r\geq2\), and let \(\pi:Y=\operatorname{Bl}_ZX\to X\) be its blowup. For **any** smooth strictly positive real \((1,1)\)-form \(S\) on \(Y\), define \(f\geq0\) off \(Z\) by
\[
f\circ\pi=\frac{S^n}{\pi^*h^n}
\qquad \text{on }Y\setminus E,\quad E=\pi^{-1}(Z).
\]
Assign an arbitrary value to \(f\) on \(Z\). Then
\[
\boxed{ f\in L^p(X,h^n)\quad\Longleftrightarrow\quad
1\leq p<\frac{r}{r-1}. }
\]
At \(p=r/(r-1)\) the divergence is logarithmic. In particular, the threshold depends on the **complex codimension of the center**, not on \(\dim_{\mathbb C}X\) unless the center is a point.

**Proof.** In a standard blowup chart near the exceptional divisor write normal coordinates on \(X\) as
\(x_1=t,\ x_2=tw_2,\ldots,x_r=tw_r\),
and retain the \(n-r\) tangential coordinates \(y\) unchanged. The holomorphic Jacobian determinant is \(t^{r-1}\). Consequently, on any sufficiently small relatively compact subchart intersecting \(E\), smooth positive bounded-equivalence factors give
\[
\pi^*h^n\asymp |t|^{2(r-1)}\,dV_Y,\qquad S^n\asymp dV_Y .
\]
Change variables, ignoring the measure-zero exceptional divisor:
\[
\int_Xf^p h^n
=\int_Y (S^n)^p(\pi^*h^n)^{1-p}
\asymp \int_0^\varepsilon
\rho^{\,1-2(r-1)(p-1)}\,d\rho
\]
locally near any positive-volume open set of \(E\). The radial integral is finite exactly when
\(1-2(r-1)(p-1)>-1\), which is the displayed strict inequality. Away from \(Z\), the density is smooth. A finite exceptional-coordinate cover proves global sufficiency, and any one chart intersecting \(E\) proves necessity. Positivity of \(S\) prevents cancellation at the critical exponent.

For the point blowup \(r=n\), this recovers exactly the exponent \(p<n/(n-1)\) in printed Example 15.22.7, lines 64–78. An independent local symbolic check computed the Jacobian determinant \(t^{r-1}\) for \(r=2,\ldots,6\); this is only an arithmetic cross-check of the written proof, not formal verification or a project test suite.

**Proposed addition:** a codimension-\(r\) observation immediately following the point-blowup example. **Affected dependents:** the \(L^p\) eligibility of Jacobian-weighted pushforward measures in Theorem 15.22.2 and related smooth-center modification examples. No claim is made that arbitrary \(S\) arises as the residual of a specified logarithmic singularity or that the excluded existence/regularization programme is proved.

## POME-RESOLVED-REMAINDER-FIBER-CRITERION-001

**Severity:** low. **Status:** verified conditional deduction, not a claim that the printed Hölder-on-\(Y\) theorem is false.**

Let \(\pi:Y\to X\) be a proper surjective modification of complex spaces, biholomorphic over \(X\setminus A\) for a proper analytic subset \(A\). For \(v\in C(Y)\), define
\(w(x)=v(\pi^{-1}(x))\) only for \(x\in X\setminus A\), using the single point in the fiber. Then
\[
\boxed{\;w\text{ has a continuous extension to }X
\quad\Longleftrightarrow\quad
v\text{ is constant on each fiber }\pi^{-1}(x).\;}
\]
**Proof.** If \(w\) extends continuously to \(W\in C(X)\), then \(v=\pi^*W\) on the dense set \(Y\setminus\pi^{-1}(A)\); continuity gives equality everywhere, so \(v\) is fiber-constant. Conversely, if \(v\) is fiber-constant, there is a well-defined function \(W:X\to\mathbb R\) with \(v=W\circ\pi\). A proper surjective map is closed and hence a quotient map; since \(v\) is continuous, \(W\) is continuous. It extends the original off-\(A\) function.

Apply this purely topological criterion to the Hölder-continuous **upstairs** remainder \(v=(u-\psi)\circ\pi\) of Theorem 15.22.2 (only defined as a difference off the poles, not by subtracting two values \(-\infty\) on \(A\)). Smooth \(v\) nonconstant on the exceptional \(\mathbb P^{n-1}\), explicitly allowed in Example 15.22.7, prevents any continuous downstairs extension of \(u-\psi\). Conversely a fiber-constant \(v\) gives a continuous downstairs remainder, but mere proper descent **does not** preserve a Hölder exponent; no downstairs Hölder estimate is claimed.

**Proposed addition:** an optional short remark distinguishing Hölder regularity of the lifted remainder from continuity of the singularity remainder on the base. **Affected dependents:** resolved-logarithmic equation regularity, ordinary singularity comparisons, and singularity-remainder descent through compact modifications.

## Other mathematical inspection and limits

- In Proposition 15.22.10 (tag **D1ADF0EFDD30**, lines 87–105), checked the algebra \(H^n-\beta^n=(H-\beta)\sum_{i=0}^{n-1}H^i\beta^{n-1-i}\); \(\partial\bar\partial H^k=0\) and closedness of \(C=H-\beta\) make every mixed form \(H^i\beta^{n-1-i}\) \(\partial\bar\partial\)-closed. Integration by parts against the total divisor current gives the printed strictly positive mass defect. The smooth power condition is essential; the general nonclosed case is **not** assigned this mass formula. This is a **selected consistency check**, not a new proof certification of the upstream mass theorem.
- In Theorem 15.16.2 (tag **352C3567BAAD**, lines 87–140), directly examined the use of uniform barriers, disjoint first-contact partition to avoid an artificial factor \(N\), and monotone capacity-product passage. No definite new defect was established. **Step 1, lines 72–85, depends on the explicitly excluded regularization theorem and was not audited.** The later results remain conditional on that upstream input.
- Theorem 15.22.2 invokes Theorem 15.5.1 for Hölder regularity, and Theorem 15.10.1's first step cites a regularization procedure. Those dependencies are recorded, **not reopened**. In particular, no work on Demailly approximation/regularization or the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme was carried out. Historical entries remain **deferred-by-user**, not resolved.
- New first selected **nonexcluded** proof-level coverage: §§**15.10**, **15.16** (Steps 2–3 only), **15.22** (geometry, mass algebra, example). No complete section, chapter, or collection certification; the ToC inventory retains **747 unique section IDs**.
- No confirmed new false printed theorem, no source/body/registry/permanent-tag edits, and no build, CI, website publication, or formalization. Only the stated symbolic local Jacobian check was run.

## Disposition

Retain all earlier finding IDs and their statuses without duplication. All three new IDs are **low-severity verified conditional deductions**. Proposed explanatory additions belong in a **separately reviewable** future body patch, not in this audit-only branch commit. The incomplete analytic input chains remain incomplete; the user-excluded chain remains **deferred-by-user**.
