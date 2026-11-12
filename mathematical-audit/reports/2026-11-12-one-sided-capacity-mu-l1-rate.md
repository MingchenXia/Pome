# An explicit one-sided capacity rate from moving Monge–Ampère measures

**Date:** 2026-11-12. **Finding:** POME-BT-ONE-SIDED-MOVING-MASS-CAPACITY-RATE-001.
**Classification:** low / verified conditional deduction. This is not an error in the printed theorem.
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Reading edition:** docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html, blob e619f7aa95f80ce11aa676193b054db3180e59d4.

## Exact anchors and hypotheses

Theorem 7.11.24, original source label foundations-of-pluripotential-theory:3CB9FBEE, permanent tag D25577E2BC26, physical lines 486–544 (in particular Step 1, lines 499–511; Step 3, lines 515–533). Equation 7.11.20 has permanent tag B1ADA2B95634 and is used at lines 505–508. Proposition 7.11.22, source foundations-of-pluripotential-theory:871210E1, permanent tag 1036F9F7DDDA, lines 428–483 (especially the two tails in equation 7.11.23, permanent tag 52F9E68B74CF). Theorem 7.11.11, permanent tag 78EB0192D174, gives convergence of moving-measure L1 discrepancies. The local outer-capacity bridge is Lemma 7.5.4, original foundations-of-pluripotential-theory:34043611, permanent tag 56B45ADBA326, in docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html, blob 464778b7ca6f1a456e36b24ecb4a0c93ab6948d3, physical lines 62–78.

Use the exact setting of Theorem 7.11.24: B is a ball in C^n, n>=1; a finite compactly supported positive measure mu is bounded above by the Monge–Ampère measure of a bounded psh subsolution; mu_j are the cubical averages; the relabeled canonical solutions U_j in E_0(B), satisfying (dd^c U_j)^n=mu_j, converge in L1(B) to a nonpositive psh representative u. Put

\[
\varepsilon_j=\int_B|U_j-u|\,d\mu_j,\qquad
E_2=\sup_j\int_B(-U_j)^2(dd^cU_j)^n<\infty.
\]

Both finiteness and \(\varepsilon_j\to0\) are **existing internal inputs**, not reproved here. They are stated and used in the printed proof.

## New quantitative deduction

For **every** compact \(K\Subset B\), \(\delta>0\), and every index of the relabeled sequence,

\[
\boxed{
\operatorname{Cap}_B^*\bigl(K\cap\{U_j<u-\delta\}\bigr)
\le
2^{2n+2}\delta^{-(n+1)}
\int_B|U_j-u|\,d\mu_j .
}
\tag{A}
\]

No convergence in ordinary Lebesgue \(L^1\) supplies the numerical rate on the right; it is the **moving Monge–Ampère measure** discrepancy from Theorem 7.11.11. There is no assertion here of a corresponding symmetric finite-index estimate for \(\{U_j>u+\delta\}\).

### Proof

Fix \(j\), \(K\Subset B\), \(\delta>0\) and \(T>0\), and abbreviate
\(a=\max(U_j,-T)\), \(b=\max(u,-T)\). Both are bounded psh, so the bounded real function \(h=(b-a)_+\) is quasi-continuous. Choose a compact \(L\Subset B\) with \(K\subset\operatorname{Int}L\).

Applying the **printed** Lemma 7.5.4 to \(h\), rather than to \(|a-b|\), gives the one-sided outer-capacity transfer
\[
\operatorname{Cap}_B^*(K\cap\{a<b-\delta\})
\le \operatorname{Cap}_B(L\cap\{a<b-\delta/2\})
\le \operatorname{Cap}_B(\{a<b-\delta/2\}).
\tag{B}
\]
By Step 1 of the printed proof of Theorem 7.11.24, applied with threshold \(\delta/2\), and its use of the truncation total-variation estimate (7.11.20),
\[
\operatorname{Cap}_B(\{a<b-\delta/2\})
\le 2^{n+1}(\delta/2)^{-(n+1)}
\left(\varepsilon_j+\frac{2E_2}{T}\right)
=2^{2n+2}\delta^{-(n+1)}
\left(\varepsilon_j+\frac{2E_2}{T}\right).
\tag{C}
\]

Away from the two deep sublevel sets \( \{U_j<-T\}\) and \(\{u<-T\}\), the two truncations equal their respective untruncated functions. Thus
\[
\begin{split}
K\cap\{U_j<u-\delta\}\subset&
\bigl(K\cap\{a<b-\delta\}\bigr)\\
&{}\cup\{U_j<-T\}\cup\bigl(K\cap\{u<-T\}\bigr).
\end{split}
\]
By subadditivity, (B)–(C), and Proposition 7.11.22 with \(p=2\), the outer capacity of the left side is bounded, **for every \(T>0\)**, by
\[
2^{2n+2}\delta^{-(n+1)}
\left(\varepsilon_j+\frac{2E_2}{T}\right)
+\frac{2^{n+2}(n+1)!E_2}{T^{n+2}}
+\frac{C_{K,2}E_2^{2/(n+2)}}{T^2}.
\tag{D}
\]
Let \(T\to\infty\) **with \(j\) fixed**, rather than taking a sequential limit in \(j\) first. This proves (A), including when \(\varepsilon_j=0\). The use of outer capacity is indispensable because \(\{U_j<u-\delta\}\) need not be open. \(\square\)

## Scope, dependents, and correction proposal

This is a quantitative **one-sided** supplement to the qualitative locally-in-capacity convergence of printed Theorem 7.11.24, not an alternate proof of all its analytic dependencies. Its usefulness is that the *lower* deviation is controlled at each individual index by an explicit moving-mass \(L^1\) error; the *upper* deviation in printed Step 2 still uses Hartogs and quasi-continuity qualitatively. There is no replacement needed for the original theorem. A possible optional reading-edition corollary after Step 3 is equation (A) with the preceding conditions and the caveat on asymmetry.

The internal dependencies are Lemma 7.10.1 (capacity comparison), Lemma 7.11.19/equation 7.11.20 (truncation TV), Proposition 7.11.22 (uniform deep-level capacity), Theorem 7.11.11 (moving-mass convergence), and Lemma 7.5.4 (outer-capacity transfer). They have not been transitively certified by this report. Consequent proofs using capacity convergence in §§7.11–7.12 may cite this bound for lower deviations alone, but are **not** thereby completely verified. No excluded Demailly approximation, Bergman/L2/OT, multiscale, or positivity-loss programme was used or reopened.

## Coverage and uniqueness

New direct proof-level examination: selected Step 1 and Step 3 of Theorem 7.11.24 (lines 497–533), associated Lemma 7.11.19 and Proposition 7.11.22 (lines 386–483), and the precise use of Lemma 7.5.4 in §7.5 (lines 62–78). This revisits previously partially sampled numbered sections §7.11 and §7.5: **0 first-visited numbered sections, 0 whole-section certifications**, against the unchanged actual ToC of **25 chapters/747 numbered sections**. Previous records checked for the specific one-sided moving-measure inequality; previous capacity or energy bounds are not relabeled as new work. No tests, build, formalization, CI, website publication or source/registry/tag changes were performed.
