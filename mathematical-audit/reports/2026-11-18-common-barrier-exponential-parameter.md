# A free positive exponent in common-barrier Monge–Ampère compactness — direct §15.9 audit

**Finding:** POME-MA-COMMON-BARRIER-EXP-B-CRITERION-001  
**Date:** 2026-11-18  
**Severity/status:** low / **verified conditional deduction**. The printed theorem, proposition, and corollary are *not* refuted. This is an additional family of sufficient criteria, proved relative to their explicitly named internal analytic dependencies.  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Audit branch parent:** 21d5f14a93211e7a44b4eeffb3045fee4f95fb57  
**Actual current table of contents:** 25 chapters, 747 numbered sections (recounted from docs/chapters/index.html).

## Exact source and direct coverage

Integrated reading edition: docs/sections/equations-with-prescribed-singularities--compactness-with-a-common-lower-barrier/index.html, blob **2d4d8889cbe39cf880723c59abcb6461b26812f7**, entire physical lines **5–102**.

- §15.9 title/permanent **D6040BDF0454**, lines 5–9.
- Theorem 15.9.1, source **non-kahler-pluripotential-theory:805DF158**, permanent **A15C1A7CB4F8**, statement lines 11–20, full proof lines 25–49; exponential error Equation 15.9.2, source **non-kahler-pluripotential-theory:F81301C1**, permanent **B172EB5C34CB**, lines 16–18.
- Proposition 15.9.3, source **non-kahler-pluripotential-theory:786C08E2**, permanent **EFAF50966FDF**, statement lines 54–58, proof 63–71.
- Corollary 15.9.4, source **non-kahler-pluripotential-theory:C466047F**, permanent **F856D22ADF4C**, lines 76–98.
- Exact dependency-level reading, not transitive certification: Lemma 13.14.8 (permanent **64174941A7D1**), Lemma 5.29.19 (**505602F4CB54**), Theorem 15.2.2 (**D70D1E469F9D**), Lemmas 5.44.2 (**983B3E6349BB**) and 5.44.7 (**27CEBF2AA643**), Theorem 13.15.23 (**18CDC482A9DD**). The finite-rooftop contact support/ordered contact invoked at printed line 32 is an **uncertified dependency**; its §15.8 regularization-based continuity input remains **deferred-by-user** and was not reopened.

## New exact criterion and proof

Let \(X\) and \(\theta\) satisfy the standing compact semipositive-big assumptions of Theorem 15.9.1. Let \(0<\delta<1\), \(\varphi\in\operatorname{PSH}(X,\theta)\), \(P_{\delta\theta}(\varphi)\not\equiv-\infty\), and fix \(C\ge0\). Suppose

\[
 \varphi-C\le u_j\le\varphi+C,\qquad u_j\longrightarrow u\quad\text{in }L^1(X).
\]

**Claim. For every fixed \(b>0\),** the hypothesis

\[
 I_j^{(b)}:=\int_X\bigl|e^{b u_j}-e^{b u}\bigr|\,
                       \operatorname{MA}^{\mathrm{ext}}_\theta(u_j)
                       \longrightarrow0
\]

implies \(u_j\to u\) in capacity. The conclusion of Proposition 15.9.3 remains valid with \(I_j^{(b)}\) in place of its \(b=1\) error, under its *different* assumptions \(\varphi-C\le u_j\le C\) and \(u\preceq\varphi\). Neither assertion assumes finite total extended Monge–Ampère mass.

**Proof relative to the printed contact, weighted lower-semicontinuity and singular-domination inputs.** The exponential \(e^{bt}\) is bounded and Lipschitz on \((-\infty,M]\), with value zero at \(t=-\infty\), for the common upper bound \(M\) of all the potentials. Hence every \(e^{bp_{j,N}}\) is bounded and quasi-continuous; its capacity convergence follows from the monotone capacity convergence of \(p_{j,N}\). Take a subsequence so \(I_j^{(b)}\le2^{-j}\) and \(u_j\to u\) a.e. The same finite rooftop \(p_{j,N}=P_\theta(\min(u_j,\ldots,u_N))\) is above the common barrier \(\varphi-C\). On each first-contact piece \(p_{j,N}=u_\ell\), the positive measure of \(p_{j,N}\) is bounded by that of \(u_\ell\); the equality also gives \(e^{bp_{j,N}}=e^{bu_\ell}\). Thus

\[
 \int_X|e^{bp_{j,N}}-e^{bu}|\,
       \operatorname{MA}^{\mathrm{ext}}_\theta(p_{j,N})
 \le \sum_{\ell=j}^NI_\ell^{(b)}
 \le 2^{1-j}.
\]

Use the two monotone limits \(p_{j,N}\downarrow p_j\) and \(p_j\uparrow p\) with Lemmas 5.29.19 and 13.14.8. Their bounded quasi-continuous exponential weights converge in capacity. Applying weighted lower semicontinuity first in \(N\) and then \(j\) yields

\[
 \int_X|e^{bp}-e^{bu}|\,
       \operatorname{MA}^{\mathrm{ext}}_\theta(p)=0.
\]

The common-barrier argument gives \(p\le u\) and \(p\sim u\sim\varphi\). The extended Monge–Ampère measure does not charge the common pole set, and strict monotonicity of \(e^{bt}\) for finite real \(t\) implies
\(\operatorname{MA}^{\mathrm{ext}}_\theta(p)(\{p<u\})=0\).
Theorem 15.2.2 with coefficient zero then yields \(p=u\); squeeze \(p_j\le u_j\le(\sup_{\ell\ge j}u_\ell)^*\) to obtain capacity convergence. Under Proposition 15.9.3's hypotheses the same construction works, because the finite rooftops still have the lower barrier and the *limit* \(u\) has the same ordinary type as \(\varphi\); no upper type comparison for individual \(u_j\) is silently used. The proof makes no approximation/regularization claim.

**Exact weighted calibration (only for the two-sided bounds of Theorem 15.9.1).** On the common finite locus, the mean value theorem gives

\[
 b e^{-bC}e^{b\varphi}|u_j-u|
 \ \le\ |e^{b u_j}-e^{b u}|
 \ \le\ b e^{bC}e^{b\varphi}|u_j-u|.
\]

On the common pole set define the weighted difference to be zero; both measures ignore that set. Thus \(I_j^{(b)}\to0\) is **equivalent** to

\[
 \int_Xe^{b\varphi}|u_j-u|\,\operatorname{MA}^{\mathrm{ext}}_\theta(u_j)\to0 .
\]

In particular, \(b=1\) is not intrinsic to the compactness argument; the positive parameter calibrates how errors near the pole set are discounted. A uniform *reverse* comparison with the unweighted self-error requires a lower bound for \(\varphi\), and is not asserted for singular references. At \(b=0\), the exponential difference vanishes identically and the proof's strict-monotonicity step fails; the extension is specifically for \(b>0\).

## Direct checks of the printed arguments

1. **15.9.1 (lines 25–49):** subsequence reduction, finite first-contact partition, monotone rooftop bounds, both capacity-limit passages, nonpolar equality detection, smaller-background domination, and upper-tail squeezing were compared with their actual cited lemmas. The infinity-of-mass issue is handled via positive-measure inequalities, not subtraction of infinities. No new false theorem or independent proof gap established.
2. **15.9.3 (lines 63–71):** the upper barrier is only a uniform constant for the approximants; the needed type equivalence is proved for \(p_j,p,u\), not assumed for \(u_j\). No hidden propagation of the stronger two-sided hypothesis.
3. **15.9.4 (lines 76–98):** the first domination is by a fixed finite nonpolar measure; the second uses uniformly bounded \(\omega\)-psh \(w_j\), their capacity convergence, and the bounded-current capacity domination. The tail inclusion \(\{u_j<-T\}\subset\{\varphi<C-T\}\) is in the correct direction. The conclusion of weak convergence additionally uses Theorem 13.15.23; not independently certified here.

## Classification, correction and affected dependents

**POME-MA-COMMON-BARRIER-EXP-B-CRITERION-001:** low / **verified conditional deduction**, generalizes the error gauge in Theorem 15.9.1 and Proposition 15.9.3 to every fixed positive exponent. Proposed optional mathematical addition: append the displayed \(b\)-parameter criterion and weighted calibration after Equation 15.9.2. This is a **proposed note**, not a required correction; the original \(b=1\) statements are correct. Direct dependents affected only by optional strengthening: §15.9.3 and §15.9.4; the latter's existing conclusion is unchanged.

**Unresolved/conditional:** finite rooftop contact and ordered-contact inputs in §15.8; Lemma 13.14.8 capacity-weighted lower semicontinuity; singular domination 15.2.2; final extended-mass weak-continuity 13.15.23. Their exact roles were examined, not fully audited transitively. **Deferred-by-user:** Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work, including the regularization-related prerequisite of §15.8. No certification, no reopening.

**Actual coverage:** entire current integrated §15.9 (three numbered statements and all proof paragraphs) directly read; six linked upstream entries read only to check hypotheses and how they enter. **+1 direct entire-section reading; +0 complete transitive proof-chain certifications.** This was absent from the existing central short-form coverage ledger; the oversized historical SECTION_MATRIX.md was preserved without claiming an unverified aggregate first-visit count. No source, registry, permanent-tag, site, main, build, tests, CI or publication changes.
