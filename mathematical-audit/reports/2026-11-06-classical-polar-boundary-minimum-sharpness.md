# Two independent sharpness tests for the classical polar-boundary minimum principle

**Findings:** POME-CLASSICAL-MINIMUM-INFINITY-NECESSARY-001; POME-CLASSICAL-MINIMUM-LOWERBOUND-NECESSARY-001.  
**Both:** low / **verified conditional deduction**. The printed theorem is **correct**; these are explicit counterexamples only to *unprinted weakened hypotheses*.  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** \`docs/sections/polar-sets-capacity-and-sweeping/index.html\`, blob \`aa814f26482e8ed27e51c945e9202c797449158b\`.  
**Primary location:** §4.3.3, Theorem 4.3.4, physical lines **24–27** (statement), **30–38** (proof).  
**Source label / permanent tag:** \`classical-potential-theory:B6612815\` / \`09FD5942CD4F\`.  
**Nearby downstream checks:** §4.3.7 (Theorem 4.3.7, lines 60–93; source \`classical-potential-theory:5388371B\`, permanent \`ABDF7610F7B2\`); §4.3.10 (Theorem 4.3.10, lines 121–130; source \`classical-potential-theory:FA6C8523\`, permanent \`C4F5D8B270EB\`). Only their *uses* of the boundary principle were inspected, not their entire proofs.

## Exact printed statement and quantifier boundary

Theorem 4.3.4 considers a Greenian open set \(\Omega\subset\mathbb R^d\), \(d\ge2\), a **superharmonic function bounded below** on \(\Omega\), and a fixed real \(\alpha\). It assumes
\[
 \liminf_{\Omega\ni x\to z}u(x)\ge\alpha
 \quad\text{for each }z\in\partial\Omega\setminus Z,
 \qquad Z\text{ polar}.
\]
It concludes \(u\ge\alpha\) when \(d=2\) or \(\Omega\) is bounded. In the remaining case, when \(d\ge3\) and \(\Omega\) is unbounded, it explicitly **also assumes**
\[
 \liminf_{\substack{x\in\Omega\\|x|\to\infty}}u(x)\ge\alpha.
\]
Both bold qualifications are present in the integrated statement; the following calculations show independently why dropping either would break the conclusion. No change in its hypotheses, conclusion, or proof is indicated.

## A. Infinity is a real boundary in \(d\ge3\), even for bounded harmonic functions

For **every** integer \(d\ge3\), set
\[
 \Omega_{\rm ext}=\{x\in\mathbb R^d:|x|>1\},
 \qquad u_{\rm ext}(x)=|x|^{2-d}-1,
 \qquad \alpha=0,\quad Z=\varnothing.
\]
This is a smooth connected exterior domain with compact \(C^\infty\) boundary. It is Greenian: any open set in \(d\ge3\) has a positive Newtonian Green kernel, as already stated in §3.5.5. For a radial \(C^2\) function,
\[
 \Delta f(r)=f''(r)+\frac{d-1}{r}f'(r),
 \qquad
 \Delta r^{2-d}=(2-d)(1-d)r^{-d}+(d-1)(2-d)r^{-d}=0.
\]
Thus \(u_{\rm ext}\) is smooth **harmonic**, hence superharmonic, on all of \(\Omega_{\rm ext}\). Furthermore
\[
 -1<u_{\rm ext}(x)<0,\quad
 \lim_{\substack{\Omega_{\rm ext}\ni x\to z\\|z|=1}}u_{\rm ext}(x)=0,
 \quad
 \lim_{|x|\to\infty}u_{\rm ext}(x)=-1.
\]
It satisfies *every other* stated hypothesis, with **no exceptional boundary points**, but it violates \(u\ge0\) everywhere. In particular even the stronger assumption \(u\in L^\infty(\Omega_{\rm ext})\) does **not** replace the infinity condition in \(d\ge3\).

The family \(u_c=c(|x|^{2-d}-1)\), \(c>0\), prescribes any negative limiting deficit \(-c\) at infinity while retaining zero finite-boundary values. Equivalently, \(1-|x|^{2-d}\) is the exact harmonic escape barrier of the exterior unit ball; the missing infinity datum is not a technical artifact of exhaustion.

**Scope:** This does not contradict the unbounded *planar* clause: for \(d=2\) the radial harmonic functions are \(A+B\log r\), and the positive logarithmic barrier used in the printed proof is qualitatively different from the bounded \(d\ge3\) escape barrier. It does not establish any claimed theorem for arbitrary other unbounded domains.

## B. The lower bound is independently necessary when a polar boundary exception is permitted

For **every** integer \(d\ge2\), let
\[
 \Omega_{\rm punct}=\{x\in\mathbb R^d:0<|x|<1\},\qquad
 Z=\{0\}\subset\partial\Omega_{\rm punct},\qquad\alpha=0
\]
and define
\[
 u_{\rm punct}(x)=
 \begin{cases}
    \log|x|,& d=2,\\
    1-|x|^{2-d},& d\ge3.
 \end{cases}
\]
The domain is bounded, connected and Greenian (§3.5.5). Directly,
\[
 \Delta\log r=\frac{-1}{r^2}+\frac1r\frac1r=0
 \quad(d=2);
 \qquad \Delta(1-r^{2-d})=0\quad(d\ge3)
\]
for \(0<r<1\). Therefore \(u_{\rm punct}\) is smooth harmonic (in particular superharmonic) throughout \(\Omega_{\rm punct}\). Every *nonexceptional* boundary point lies on \(|x|=1\), where its full boundary limit is exactly zero. The singleton \(\{0\}\) is polar: the positive fundamental superharmonic function \(-\log|x|\) in dimension two, respectively \(|x|^{2-d}\) in higher dimension, has a pole at zero. These are local polar witnesses; the elementary global fundamental potentials give the same classification.

Yet
\[
 u_{\rm punct}(x)<0\quad\text{at every }x\in\Omega_{\rm punct},
 \qquad \lim_{x\to0}u_{\rm punct}(x)=-\infty.
\]
The lower-boundedness hypothesis fails, and without it the asserted minimum principle would fail **even on a bounded Greenian domain and in dimension two**, while keeping precisely the stated permission to ignore a polar subset of the finite boundary. Since the domain is bounded, this failure is entirely independent of the infinity condition from part A.

The example does **not** show that a lower bound is necessary when **no** polar exceptional boundary set is allowed; that is a different question. It shows its necessity for the exact generality of the printed theorem, which allows a nonempty polar exception.

## Cross-check of original proof and downstream interfaces

The integrated proof of Theorem 4.3.4 (lines 33–38) uses the global lower bound precisely to ensure the perturbation \(u+\varepsilon v\) has the requisite boundary inequalities at points in \(Z\), where \(v=+\infty\); and, for unbounded planar domains, to make \(u+\varepsilon\log(|x-z_0|/r)\) large on outer truncation spheres. The bounded-domain reduction and outer-sphere exhaustion are consistent with both models above. The theorem is not being declared *proved from scratch*: its upstream polar-globalization and classical minimum-principle inputs were not independently reconstructed in this run.

Theorem 4.3.7 invokes this boundary principle at physical lines 75–81 to compare equilibrium potentials and prove capacities; it carries the separate **admissible-domain** boundary hypothesis at line 61. Theorem 4.3.10 invokes it at line 128 for \(w-p\) outside the measure's compact support; its preliminary case has \(p\) continuous and bounded, and a nonnegative superharmonic \(w\), so \(w-p\) is bounded below. Compact-support decay is used at infinity. Neither is refuted by these models. The separate claim that arbitrary Greenian domains admit the needed boundary limits remains an **unreviewed dependency**, not a newly verified repair.

## Disposition and future verification

- **Status of each ID:** low / **verified conditional deduction**; the explicit harmonic counterexample is complete and dimension-uniform in the stated range. **No confirmed error** in Theorem 4.3.4, and no complete certificate for §4.3.
- **Proposed optional correction to exposition:** append two short examples after Theorem 4.3.4, distinguishing the exterior \(r^{2-d}-1\) escape mode from the punctured-ball \(\log r\) / \(1-r^{2-d}\) polar blowdown. Retain the original theorem and all labels.
- **Affected dependents:** §4.3.7 and §4.3.10 continue to need the finite-boundary/polar-exception principle with the original qualifications; no dependence is invalidated. Do not infer that their more extensive balayage, Choquet capacity or potential decomposition proofs have been audited.
- **Remaining work:** examine all uses of §4.3.4 under noncompact or varying-domain passages, and independently check the general Greenian boundary-decay premise when outside the excluded regularization scope. No Demailly approximation, Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was opened; all remain **deferred-by-user**.
- **Verification performed:** analytic Laplacian and boundary-limit calculations only; no repository tests, build, CI, website publication or formal verification. The current whole-project ToC remains 25 chapters and 747 numbered sections, with zero *complete mathematical-section* certifications.
