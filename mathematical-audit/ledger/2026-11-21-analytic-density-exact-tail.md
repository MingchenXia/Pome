# 2026-11-21: analytic density distribution and degenerate uniqueness

## POME-P3-ANALYTIC-DENSITY-EXACT-TAIL-001
**Severity:** low. **Status:** verified conditional deduction (not a false printed theorem; not a certified complete proof chain).  
**Baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Primary anchor:** \`docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html\`, lines 11–20 and 199–206; §14.29.1 permanent \`DD001DBBE659\`, equation (14.29.2) tag \`B358F4101DED\`, (14.29.16) tag \`C72BCF7334A2\`, blob \`2f00a81edc49855971bb3a6d774603ee5bbf40db\`.  
**Secondary dependent:** §14.21.13 tag \`61851D05B072\` (square-root sharpness).  
**Exact finding:** With \(c=\mathrm e/(1+\mathrm e)^2\), \(\Delta=(\mathrm e-1)/(1+\mathrm e)\), normalized Fubini–Study volume sends \(q=t(1-t)\) to \(12q(1-4q)^{-1/2}dq\), and \(f_*=(q-c)^2\). Thus
\[
 \frac{\operatorname{Vol}\{f_*\le s\}}{\operatorname{Vol}(X)}
 = \frac{24c}{\Delta}\sqrt{s}+\frac{16(1-c)}{\Delta^5}s^{3/2}+O(s^{5/2}).
\]
The precise critical divergence constants are \(12c/\Delta\) for \(\log(1/\varepsilon)\) at exponent \(1/2\), and \(24c/\Delta\) for the pole \((1-2\alpha)^{-1}\) as \(\alpha\uparrow1/2\).  
**Proof and hypotheses:** [full derivation](../reports/2026-11-21-analytic-density-tails-and-degenerate-ma-review.md), including exact integral and the normalized higher-dimensional product. The scalar distribution is directly proved; application to nonunique smooth Monge–Ampère solutions is conditional on §14.29.1's construction.  
**Proposed change:** optional supplementary corollary after (14.29.16), *not* a correction to its valid statement.  
**Coverage:** whole §§14.25,14.27,14.29; selected §§14.21,14.26,14.28. No first-visit claim; no additional complete transitive verification; user-excluded programmes remain **deferred-by-user**.
