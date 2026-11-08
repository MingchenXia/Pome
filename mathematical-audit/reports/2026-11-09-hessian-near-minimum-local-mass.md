# Local Hessian mass at near-minimum sets on Hermitian manifolds

**Date:** 2026-11-09. **Finding:** POME-HESS-NEARMIN-LOCAL-MASS-001. **Severity/status:** low / verified conditional deduction; neither a false printed theorem nor a complete certification of the underlying Hessian-current construction.

## Exact production anchors and scope

Reviewed production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The current subject range is compact connected Hermitian manifolds of dimension \(n\) with \(2\le m<n\); \(\omega\) is not assumed closed.

- Primary: docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html, blob **580d3bc2b10ebd01d880b2a31fc6930436570aac**. Lemma **8.13.7**, source **non-kahler-pluripotential-theory:D2B92D4C**, permanent **0F8C3F6B0122**, physical lines **174–224**; Theorem **8.13.8**, source **non-kahler-pluripotential-theory:AEE5FFB9**, permanent **B83D4B8CE619**, lines **226–280**. The former is the mixed-current torsion recursion; the latter is the modified comparison inequality.
- Local input: docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html, blob **8750df56019c14e16704607ca20fa8b90f137fb0**, Lemma **8.12.3**, source **non-kahler-pluripotential-theory:B518F16E**, permanent **132BB9E1B1F5**, lines **67–96**.
- Representative input: docs/sections/complex-hessian-equations--the-admissible-cone/index.html, blob **925e6109ab7d800cde9bec4b0487842b2e6877a8**, Lemma **8.2.10**, source **non-kahler-pluripotential-theory:6FFAAFB0**, permanent **A1FFEE061CF5**, lines **262–end**.
- The printed global strict-domination proof is Theorem **8.13.10**, permanent **A532C77D7D0C**, lines **282–305**. Its use of the same positive-volume step was crosschecked, not re-certified in full.

## New quantitative deduction

Let \(u,v\) be bounded \(m\)-admissible potentials in their canonical representatives, let \(0<\alpha<1\), \(\eta=1-\alpha\), and let \(C\ge1\) be the constant from the **printed** Theorem 8.13.8. Put
\[
 V=\alpha v,\qquad S=\inf_X(u-V),\qquad
 E_s=\{x\in X:u(x)<V(x)+S+s\}.
\]
For every \(0<s<\eta^3/C\), one has the **strictly positive** quantitative estimate
\[
\boxed{
 0<\frac{\eta^m}{1+Cs\eta^{-m}}\int_{E_s}\omega^n
 \le \int_{E_s}H_m(u).
}
\tag{A}
\]
There is no assumption that \(E_s\) is topologically open, no Kähler assumption, and no assumption that \(u\) attains its infimum. The coefficient in (A) is explicit relative to the constant of the printed theorem; it is **not** claimed optimal.

**Proof.** Since \(u\) and \(V\) are bounded, \(S\) is a finite infimum and \(E_s\ne\varnothing\). More is needed: if \(\int_{E_s}\omega^n=0\), then \(u\ge V+S+s\) almost everywhere. The second potential is bounded admissible by Lemma 8.12.3 and constant-shift invariance. Lemma 8.2.10, applied to this **almost-everywhere inequality of canonical representatives**, upgrades it to \(u\ge V+S+s\) everywhere. This contradicts the definition of \(S\). Thus
\(\int_{E_s}\omega^n>0\). This argument deliberately uses the actual order-detection lemma, not an unjustified assertion that \(E_s\) must be open.

Lemma 8.12.3 gives
\[
H_m(V)=H_m(\alpha v)\ge \alpha^mH_m(v)+\eta^m\omega^n
\ge\eta^m\omega^n.
\]
Theorem 8.13.8 gives
\[
\int_{E_s}H_m(V)
\le(1+Cs\eta^{-m})\int_{E_s}H_m(u).
\]
Combining these measure inequalities and the strictly positive volume yields (A). All restrictions are to the **fixed Borel set \(E_s\)**; no limit of moving restrictions and no sequential compactness assertion is used. QED.

### A localized strengthening of positive total Hessian mass

Taking \(v=u\), \(\alpha=1/2\), and writing \(t=2s\), one obtains for **every bounded admissible \(u\)** and every \(0<t<1/(4C)\),
\[
\boxed{
\int_{\{u<\inf_Xu+t\}}H_m(u)
\ge
\frac{2^{-m}}{1+C\,2^{m-1}t}
\int_{\{u<\inf_Xu+t\}}\omega^n
>0.
}
\tag{B}
\]
Indeed \(S=\frac12\inf_Xu\) and \(E_s=\{u<\inf_Xu+2s\}\). For **any** \(t>0\), even beyond the small range, choose \(0<t_0<\min\{t,1/(4C)\}\). The inclusion of sublevel sets and positivity of \(H_m(u)\) imply
\[
\int_{\{u<\inf_Xu+t\}}H_m(u)
\ge\int_{\{u<\inf_Xu+t_0\}}H_m(u)>0.
\]
This strictly localizes the positive-total-mass statement of Proposition 8.12.5: every strict neighborhood *in value* of the infimum carries positive Hessian mass. It does **not** assert uniform positive mass independent of \(u\) or \(t\).

## Independent algebraic check of the printed recursion

The printed 8.13.7–8 proof was read directly, rather than inferred from a theorem title. Set \(b_{p,q}=\int_{E_s}\sigma_u^p\sigma_V^q\omega^{n-p-q}\), \(a_k=b_{k,0}\), and \(A_r=\max_{p+q=r}b_{p,q}\). Lemma 8.13.7 supplies, with \(r=p+q\),
\[
 b_{p,q}\le a_r+C_1s\sum_{d<r}A_d.
\]
Induction for \(s\le1\) yields \(A_r\le a_r+K_rs\sum_{k<r}a_k\); in particular
\(b_{0,m}\le a_m+C_2s\sum_{k<m}a_k\).
Using the positive \(\eta\omega\) component in \(\sigma_V=\alpha\sigma_v+\eta\omega\), the *diagonal* 8.13.7 estimate gives
\[
\eta a_k\le a_{k+1}+C_3s(a_k+a_{k-1}+a_{k-2}).
\]
The exponents after multiplying by \(\eta^{m-k-1}\) are **respectively** \(\eta^{-1},\eta^{-2},\eta^{-3}\). Thus, with \(B_k=\eta^{m-k}a_k\) and \(\delta=C_3s\eta^{-3}\), the written recurrence
\(B_k\le B_{k+1}+\delta(B_k+B_{k-1}+B_{k-2})\)
is consistent. If \(3m\delta<1/2\), summing backwards gives \(B_k\le2B_m\) for \(k<m\), hence \(\sum_{k<m}a_k\le2m\eta^{-m}a_m\). No division by \(a_m\) is used, so the **zero-top-mass case is included**. This audit confirms the finite-dimensional recursion *conditionally on* the stated torsion and weighted-current estimates. It does not reprove the difficult \(8.11.12\)/\(8.12.4\) construction.

## Verdict, proposal, and dependents

**Verified conditional deduction / low**: printed Lemma 8.13.7 and Theorem 8.13.8 survive the checked algebra; (A) and (B) are new consequences of their exact hypotheses. No **confirmed error**, **proof gap**, or **verified repair** to production is asserted here. A possible independently tagged remark after Theorem 8.13.8 is to record (A), with (B) as its specialization, and to emphasize the canonical-representative argument for positive volume. Potential direct readers are the strict-domination Theorem 8.13.10 and the positive-total-mass Proposition 8.12.5; neither is modified or re-certified. The underlying Hermitian torsion/current construction and all other mathematical sections remain open to separate audit.

**Excluded-by-user:** Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme were not examined. Existing findings on them remain **deferred-by-user**, not resolved. No private source/scans, source/registry/tag/canonicalization changes, build, CI, formal verification or website publication are involved.
