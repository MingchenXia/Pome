# Mathematical audit — 2026-11-01: directed-domain harmonic measures and a mixed-mass background switch

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit-only branch:** \`review/mathematical-audit\`. This is a local mathematical review, not an endorsement of every upstream dependency or of either entire section. The expressly user-deferred Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme were neither inspected nor resumed.

## POME-HARM-MEAS-DIRECTED-EXIT-001 — low / verified conditional deduction

**Source and exact anchors.** Production \`docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html\`, Git blob \`fc02188d6e246a21aa07acd8bf6d3712761ba6e5\`; Proposition **3.1.33**, source \`foundations-of-pluripotential-theory:37E4271C\`, permanent tag \`C5D6FBB32967\`, physical lines **651–670**. Contextual inputs: Theorem **3.1.29** (permanent \`C1B72E118338\`), its regular-domain continuous Dirichlet solution and boundary values; Theorem **3.1.34** (source \`foundations-of-pluripotential-theory:497FD574\`, permanent \`476CFD04AAC6\`, physical lines **672–746**), used for comparison with the *historically recorded* directed Green-exhaustion audit only. No reliance on a sequential compactness assertion.

**Precise new deduction.** Let \(D\subset\mathbb R^d\) be a bounded regular domain. Let \((D_\alpha)_{\alpha\in A}\) be an *increasing directed net by inclusion* of nonempty bounded regular domains (or regular open sets) such that \(\bigcup_{\alpha\in A}D_\alpha=D\). Let \(F\in C(\overline D;\mathbb C)\), and write
\[
h=H_D(F|_{\partial D}),\qquad
h_\alpha=H_{D_\alpha}(F|_{\partial D_\alpha}),\qquad
e_\alpha=\sup_{z\in\partial D_\alpha}\operatorname{dist}(z,\partial D).
\]
Then \(e_\alpha\to0\) along the *original net*, and
\[
\boxed{\displaystyle
\sup_{x\in D_\alpha}|h_\alpha(x)-h(x)|
\leq \sup_{\substack{z\in\overline D\\
\operatorname{dist}(z,\partial D)\leq e_\alpha}}|F(z)-h(z)|
\longrightarrow0.}
\]
For complex-valued \(F\), the same modulus inequality follows directly from the Poisson/harmonic-measure probability representation: the difference is the integral of the complex boundary datum \(F-h\), so its absolute value is bounded by its boundary supremum. For real data, it also follows from the harmonic maximum principle.

Consequently, for every fixed \(x\in D\), the Borel probability measures \(\omega_x^{D_\alpha}\) of Proposition 3.1.33, regarded as measures on the *common compact space* \(\overline D\) by extending them by zero off \(\partial D_\alpha\), converge weakly to \(\omega_x^D\):
\[
\int_{\overline D}F\,d\omega_x^{D_\alpha}
\;\longrightarrow\;
\int_{\overline D}F\,d\omega_x^D\qquad(F\in C(\overline D)).
\]
The measures are defined eventually for fixed \(x\); no subsequence, Brownian-motion representation, or net-to-sequence reduction is needed.

**Complete proof of the new step.** Fix \(\delta>0\) and set \(K_\delta=\{z\in\overline D:\operatorname{dist}(z,\partial D)\geq\delta\}\). Because \(D\) is bounded, \(K_\delta\) is compact and lies in \(D\). The increasing open cover \(\{D_\alpha\}\) of \(K_\delta\) has a finite subcover; directedness gives \(\alpha_\delta\) for which \(K_\delta\subset D_\alpha\) whenever \(\alpha\geq\alpha_\delta\). Thus \(\partial D_\alpha\cap K_\delta=\varnothing\) eventually (the boundary of an open set cannot meet an interior compact subset contained in that open set), proving \(e_\alpha\leq\delta\) eventually. The function \(h\) is harmonic on \(D\) and continuous on \(\overline D\), and equals \(F\) on \(\partial D\). Hence \(m(\varepsilon)=\sup_{\operatorname{dist}(z,\partial D)\leq\varepsilon}|F(z)-h(z)|\to0\) by compactness and continuity. The difference \(h_\alpha-h|_{D_\alpha}\) is harmonic on \(D_\alpha\), continuous on its closure, and has boundary values \(F-h\). The maximum principle (or the probability representation for complex data) gives the displayed bound \(m(e_\alpha)\). Proposition 3.1.33 identifies the point evaluations of \(h_\alpha,h\) as the integrals in the final display.

**Exactness and restrictions.** On \(D=B(0,1)\), \(D_r=B(0,r)\) with \(r\uparrow1\) and \(F(z)=|z|^2\), the extensions are \(h\equiv1\), \(h_r\equiv r^2\). The domain-uniform error and the right-hand collar supremum both equal \(1-r^2\), so the bound can be attained and admits no universal improvement in its order without a modulus assumption on \(F-h\). This is **not** a new proof of the Green-exhaustion result already recorded as \`POME-CLASS-GREEN-DIRECTED-EXHAUST-001\`; the present result concerns the *varying boundary harmonic measures* and their continuous test functions. Neither Proposition 3.1.33 nor Theorem 3.1.34 is disproved. A proposed optional corollary after Proposition 3.1.33 would serve comparisons of harmonic measures, Perron solutions, and domain exhaustion. No current published source/body edit was made.

## POME-VOL-BG-ZERO-TEST-001 — low / proof gap (missing background qualification), with a verified proposed local repair

**Source and exact anchors.** Production \`docs/sections/volumes-under-bounded-mass--strict-barriers-and-background-variation/index.html\`, Git blob \`2fb8697ad0f1e916245d9adafde27f40f97b46f3\`; Proposition **13.20.6**, source \`non-kahler-pluripotential-theory:95AB9149\`, permanent tag \`F4C607C7C503\`, statement physical lines **135–143**, proof **148–155**. The cited mixed-mass estimate occurs in Lemma **13.20.1**, source \`non-kahler-pluripotential-theory:1DBB631B\`, permanent \`EDD01F5B65E5\`, especially the hypothesis \(s,t\in\mathrm{PSH}(X,\theta)\) and the binomial estimate at physical lines **44–54**. The standing convention in \`docs/sections/volumes-under-bounded-mass/index.html\` (blob \`94d79bfca61602054b9d09b79a76306e11a67d79\`) expressly permits a big, non-semipositive \(\theta\). The needed non-pluripolar mixed positivity is Lemma **13.14.2**, permanent \`D36A46B4DD86\`, and bounded-mass upper bound is Proposition **13.14.16**, permanent \`1342466C71A9\`, in \`docs/sections/non-pluripolar-monge-ampere-measures/index.html\` (blob \`5d0f652ffaaaef81cf74d1786082e429f71b3b89\`, physical lines **24–43**, **255–265**).

**Exact missing justification.** Proposition 13.20.6 writes: “the mixed-mass estimate in the proof of lemma 13.20.1, applied to \(s=v\) and \(t=0\), together with \(\omega\leq\Omega\)”. As written, the estimate from Lemma 13.20.1 assumes both \(s,t\in\mathrm{PSH}(X,\theta)\), but **\(0\) need not be \(\theta\)-psh**. The theorem is **not shown false**: one must instead make the positive **\(\Omega\)-background** switch explicit before applying the estimate. It is possible the displayed shorthand intended precisely this switch, but the stated lemma hypotheses do not justify its literal invocation.

**Concrete witness to the missing premise.** On \(X=\mathbb P^1\times\mathbb P^1\), let \(\omega_i\) be pullbacks of normalized Fubini–Study forms, let \(\omega=\omega_1+\omega_2\), and take the globally smooth \(f=-2|z_1|^2/(1+|z_1|^2)\) in the first-factor affine chart, extended smoothly through infinity. Put \(\theta=\omega+dd^cf\). At \(z_1=0\), \(dd^c f=-2\omega_1\), hence \(\theta=-\omega_1+\omega_2\) at that point: \(0\notin\mathrm{PSH}(X,\theta)\). Nevertheless \(-f\in\mathrm{PSH}(X,\theta)\) and \(\theta+dd^c(-f)=\omega>0\), so \(\theta\) is big, and the Kähler compact manifold has bounded mass. Thus this is a legitimate background under the actual chapter hypotheses.

**Self-contained correction of the specific step (using the listed internal dependencies).** Choose any positive Hermitian form \(\Omega\geq\theta,\omega\). For each \(v\in\mathrm{PSH}(X,\theta)\) we have **\(v,0\in\mathrm{PSH}(X,\Omega)\)**. On the non-pluripolar locus put \(T_\theta=\theta+dd^cv\), \(T_\Omega=\Omega+dd^cv\). By monotonicity of mixed positive products and \(\omega\leq\Omega\),
\[
\begin{aligned}
\binom nk\int_X\langle T_\theta^{\,n-k}\wedge\omega^k\rangle
&\leq \binom nk\int_X\langle T_\Omega^{\,n-k}\wedge\Omega^k\rangle\\
&\leq 2^n\int_X\mathrm{MA}_\Omega(v/2)
\leq 2^n v_+(\Omega),\qquad 1\leq k\leq n.
\end{aligned}
\]
For the middle inequality, \(\Omega+dd^c(v/2)=\frac12(T_\Omega+\Omega)\); the \(k\)-th mixed term is one of the nonnegative terms in the binomial expansion of its non-pluripolar top power (equivalently apply the identity to bounded truncations and pass via monotone non-pluripolar definitions). The final bound is precisely the integrated bounded-mass hypothesis. Expanding \((\theta+\varepsilon\omega+dd^cv)^n\) on the non-polar locus and using \(\varepsilon^k\leq\varepsilon\) for \(0\leq\varepsilon\leq1\), \(k\geq1\), yields the *same stated constant*
\[
\int_X\mathrm{MA}_{\theta+\varepsilon\omega}(v)
-\int_X\mathrm{MA}_{\theta}(v)
\leq n2^n v_+(\Omega)\,\varepsilon .
\]
The rest of the lower-volume argument in Proposition 13.20.6 then proceeds unchanged. The proposed **proof-only** repair is to specify “apply the mixed-mass bound with \(s=v\), \(t=0\) in the \(\Omega\)-background, where both are \(\Omega\)-psh”, rather than applying the \(\theta\)-background hypothesis to zero. This local proof step is repaired conditionally on the established internal mixed-product and bounded-mass statements; neither the whole proposition nor their full transitive proof chains have been certified. Background-variation estimates and their users in §§13.20–13.26 are potentially affected. No change to main, sources, proof registry, canonicalization, tags, or published site is authorized.

## Actual review and limitations

New proof-level work: harmonic-measure Proposition **3.1.33** and its domain-net consequence; precise previously unchecked \(t=0\) admissibility inside Proposition **13.20.6**. Context inspected but **not** certified: §3.1.29/.34 (including the already known directed Green limit), §13.16 standing hypotheses, Lemma 13.20.1, §13.14.2/.16, selected §13.17–13.19 volume/contact statements, and §13.29 curve backgrounds. These latter sections have historical partial coverage and are **not** double-counted as first inspections. The previously recorded \`POME-CLASS-GREEN-DIRECTED-EXHAUST-001\` and \`POME-STRICT-BARRIER-NONPOS-BG-001\` remain separate unchanged historical findings.

The current table of contents still has **25 chapters / 747 numbered sections**. **Zero entire mathematical sections or whole upstream chains are certified.** There is no claim of project build, test suite, formal verification, CI run, or website publication. All prior ledger statuses remain unchanged; Demailly approximation/regularization and the specifically excluded supporting programme remain **deferred-by-user**.
