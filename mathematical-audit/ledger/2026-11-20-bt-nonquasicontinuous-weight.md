# Classified ledger — 2026-11-20 fixed non-quasi-continuous weight

**Finding ID:** \`POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001\`  
**Status:** verified conditional deduction (counterexample to an unprinted weakening).  
**Severity:** low.  
**Original statements:** §7.5 Lemma 7.5.7(2) \`foundations-of-pluripotential-theory:39398ED2 / 880C30054932\` and Theorem 7.5.8 \`:2B1AA42A / 42828E3BDDFA\`, mathematical physical lines 124–187, main file blob \`464778b7ca6f1a456e36b24ecb4a0c93ab6948d3\`.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Hypotheses tested:** locally bounded smooth psh \(u_\varepsilon\to u\) uniformly; fixed bounded Borel \(f_\varepsilon=f\) converges trivially in capacity; **quasi-continuity of the limiting weight deliberately deleted**.  
**Exact counterexample:** \(u_\varepsilon=(x+\sqrt{x^2+\varepsilon^2})/2\), \(u=\max(x,0)\), \(f=1_{\{x=0\}}\) on a disc in \(\mathbb C\). Then \(f\,dd^cu_\varepsilon=0\) for every \(\varepsilon\), while \(f\,dd^cu=(4\pi)^{-1}\delta_{\{x=0\}}\otimes dy\ne0\). Quasi-continuity of \(f\) fails by the separately verified capacity domination of §7.5.7(1) plus the continuous-extension argument.  
**Proposed correction:** None to the printed theorem; explicitly retain quasi-continuity in downstream weighted convergence applications.  
**Affected dependents:** every application of §7.5.7(2) or §7.5.8 to a discontinuous Borel test function; §§7.6 and later mixed-product comparison proofs should preserve the stated weight condition.  
**Prior work:** independent from the 2026-11-16 oscillation-capacity result, 2026-11-18 \(L^p\)-weight result, and the 2026-11-20 fixed divisor capacity-collapse counterexample. Those are preserved, not reclassified.  
**Complete proof:** [dated report](../reports/2026-11-20-bt-discontinuous-weight-hyperplane-concentration.md).  
**Remaining gaps:** the fully transitive proof chains for Hartogs compactness, the capacity comparison inequalities, the proper-cycle statements of §20.5, and the smooth factoriality input of §§20.6–20.7 are not certified.  
**Deferred-by-user:** Demailly approximation/regularization, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss work, not resolved. No other new confirmed error, proof gap or duplication was established by this run.
