# 2026-11-22: scalar mass distribution of a finite-energy test curve

**POME-TESTCURVE-MASS-LOSS-STIELTJES-MOMENT-001** — **low / verified conditional deduction, not a printed theorem error**.

Main SHA b6933b772f41b45918f7e25ed1afbbb1fd892272. Direct integrated §17.12, path docs/sections/test-curves--the-notion-of-test-curves/index.html, blob 6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7. Source/permanent anchors: Definition 17.12.10 sgpt:38A406EF / 69529F41AA18; Equation 17.12.12 sgpt:50A4CAA5 / 942AC971E484; Proposition 17.12.9 sgpt:37ECD68D / B7CD1B90CFDA.

Given a test curve with \(a=\Gamma_{\max}\), \(m=M(-\infty)>0\), and \(M(t)=\int_X\mathrm{MA}(\Gamma_t)\), define a positive Stieltjes measure on \((-\infty,a]\) by \(\sigma((t,a])=M(t)\). Its endpoint atom is \(\sigma(\{a\})=M(a^-)\) and its total mass is \(m\). Then
\[
 \mathbf E^\phi(\Gamma)=\int_{(-\infty,a]}t\,d\sigma(t).
\]
This is an extended-real identity, with no signed-integral ambiguity because \(t\le a\). Finite energy is equivalent to \(\int(a-t)d\sigma(t)<\infty\), implying \(m-M(a-T)=o(1/T)\). A constant test curve gives \(m\delta_a\), checking the necessary endpoint atom.

**Proof:** Stieltjes construction from the continuous decreasing mass function, then Tonelli on the nonnegative kernel \(a-t\). For the tail write \(F=m-M\) and \(\frac{T}{2}F(a-T)\le\int_{a-T}^{a-T/2}F\le\int_{-\infty}^{a-T/2}F\to0\). **Affected dependents:** normalization comparisons with §17.13 ray energy, and any later attempt to identify test-curve mass distributions with DH measures. **Proposed change:** optional derived lemma; do not change the original definition or its historic attribution. **Upstream status:** relies on §13.13.11 and §17.12.9 as internal cited statements, neither transitively certified in this pass. [Full proof](../reports/2026-11-22-test-curve-stieltjes-moments-and-legendre-recheck.md).

§17.18 was already directly reviewed on 2026-11-19; this run's product/normalization example is a **repeat check, not a second new finding**. All excluded regularization work stays deferred-by-user.
