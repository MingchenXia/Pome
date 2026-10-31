# Multipole Green weight stability and oscillation-controlled relative capacity
Date: 2026-10-31 (Asia/Shanghai). Audit-only mathematical note.
Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Reviewed audit branch: `review/mathematical-audit` (preserved; no source/registry/published modifications).

## POME-GREEN-MULTIPOLE-WEIGHT-STABILITY-001

**Status:** low / **verified conditional deduction**. Proposition 7.19.5 is **not** disproved or independently recertified.

**Integrated source:** `docs/sections/symmetric-envelopes-and-finite-collections-of-poles/index.html`; production blob `8e33a409fa4a7c6eea29ab48727741ed9b1e167d`. Proposition **7.19.5**, original source `klimek-pluripotential-theory:00AC0DAE`, permanent tag `A3DBF2B9E6B2`, physical lines **77–90** (statement at 78–82, proof at 87–90). Section tag `5D2B9AF5042C`. Propositions 7.19.1–7.19.4 are context only (same file lines 8–75).

**Precise claim.** Fix one bounded connected domain $D\subset\mathbb C^n$ and one ordered set of distinct poles $a_1,\dots,a_N\in D$. For each positive vector $\alpha=(\alpha_j)$ let $G_\alpha$ be the negative PSH multipole envelope of Proposition 7.19.5, with upper logarithmic type $\alpha_j\log|z-a_j|+O(1)$ at $a_j$. For another vector $\beta_j>0$, set
$$
r_-=\min_j\frac{\beta_j}{\alpha_j},\qquad
r_+=\max_j\frac{\beta_j}{\alpha_j}.
$$
Then on all of $D$ (with the usual extended-valued interpretation at poles),
$$
\boxed{r_+G_\alpha\ \leq\ G_\beta\ \leq\ r_-G_\alpha.} \tag{A}
$$
In particular, with $a=\min_j\alpha_j>0$ and $\delta=\|\beta-\alpha\|_{\ell^\infty}$,
$$
\boxed{|G_\beta(z)-G_\alpha(z)|
\leq\frac{\delta}{a}|G_\alpha(z)|,\quad z\in D\setminus\{a_1,\dots,a_N\}.} \tag{B}
$$
For every compact $K\Subset D\setminus\{a_j\}$ this gives an explicit local uniform Lipschitz bound in the weights:
$$
\|G_\beta-G_\alpha\|_{L^\infty(K)}
\leq\frac{\delta}{a}\,\|G_\alpha\|_{L^\infty(K)}.
$$
The classical atomic mass formula in Proposition 7.19.5 further yields the exact signed-measure variation
$$
\boxed{\|M_{G_\beta}-M_{G_\alpha}\|_{\mathrm{TV}}
=2^{-n}\sum_{j=1}^N|\beta_j^n-\alpha_j^n|
\leq 2^{-n} nM^{n-1}\sum_j|\beta_j-\alpha_j|,} \tag{C}
$$
where $M=\max_j\{\alpha_j,\beta_j\}$; the poles must remain distinct and fixed for this particular total-variation identity.

**Complete order proof, not relying on a PDE limit.** Multiplying a negative PSH competitor by any $c>0$ bijects the admissible families for weights $\alpha$ and $c\alpha$; positive multiplication commutes with USC regularization, so $G_{c\alpha}=cG_\alpha$. More generally $\beta_j\geq r_-\alpha_j$ at all poles, hence every $\beta$-admissible function satisfies the weaker singularity restrictions for $r_-\alpha$; therefore $G_\beta\leq G_{r_-\alpha}=r_-G_\alpha$. Likewise $\beta_j\leq r_+\alpha_j$, so all $r_+\alpha$-competitors are $\beta$-competitors and $r_+G_\alpha\leq G_\beta$. This proves (A). Since $G_\alpha\leq0$ and $|r_\pm-1|\leq\delta/a$, (B) follows from (A), without an extra bounded-variation or uniform-integrability assumption. Away from the pole set $G_\alpha$ is locally bounded by Proposition 7.19.5. Formula (C) follows by subtracting the explicitly supported positive atomic measures and applying the mean-value bound $|b^n-a^n|\leq n\max(a,b)^{n-1}|b-a|$.

**Optimality/model and limits.** For $D=B(0,1)$, $N=1$, $a_1=0$, $G_\alpha=\alpha\log|z|$, and (A) is equality. If $\beta=\alpha+\delta$, then (B) is equality at every $0<|z|<1$. Thus the factor $\delta/a$ cannot be decreased in a uniform inequality that covers the one-pole case. Neither global uniform boundedness across the poles nor continuity when a pole disappears ($\alpha_j\to0$) is claimed. This is **not** a new theorem about moving pole locations, joint continuity, or the initial Bedford–Taylor residual-mass construction.

**Dependencies and proposal.** Order and homogeneity follow directly from the envelope definition. The local boundedness and the signed-measure statement are conditional on the integrated Proposition 7.19.5 and its one-point residual-mass normalization $2^{-n}$; they are not independently certified. Optional corollary after that proposition; preserve its source attribution, permanent tag, and original version. Affected uses include multipole Green-function comparison and finite-pole mass continuity, but no existing downstream proof is declared repaired.

## POME-RELCAP-OSCILLATION-001

**Status:** low / **verified conditional deduction**. Proposition 16.25.6 remains correct; its printed constant is valid but can be made invariant under adding constants to the reference potentials.

**Integrated source:** `docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html`; production blob `4207ba03590b2988456f1df4da4123e1e572c8de`. Proposition **16.25.6**, source `foundations-of-pluripotential-theory:2C3BA6F2`, permanent tag `1587DBB4654F`, physical lines **112–136** (printed $(2C+1)^n$ at 117–120, proof at 129–135). Definition 16.25.5 at lines **103–109**, permanent tag `E9BD67F94210`. Related comparison 16.25.4 and tail 16.25.7 are contextual, not recertified. Section tag `2B1B1CB179EE`.

**Precise claim.** In the compact big-class setting of Section 16.25, suppose $\phi,\psi\in\mathrm{PSH}(X,\theta)$ have globally bounded difference outside their pole sets. Define finite
$$
m=\inf_{X\setminus P}(\phi-\psi),\quad M=\sup_{X\setminus P}(\phi-\psi),\quad
\omega=M-m,\qquad P=\{\phi=-\infty\}\cup\{\psi=-\infty\}.
$$
The almost-everywhere inequalities extend as PSH order inequalities, giving a common pole set. For every Borel set $A$,
$$
\boxed{(1+\omega)^{-n}\operatorname{Cap}_{\theta,\psi}(A)
\leq\operatorname{Cap}_{\theta,\phi}(A)
\leq(1+\omega)^n\operatorname{Cap}_{\theta,\psi}(A).} \tag{D}
$$
Here $\omega=\operatorname{osc}_{X\setminus P}(\phi-\psi)$, which is insensitive to replacing either potential by an additive constant. If the capacity is positive, the logarithms obey
$$
\big|\log \operatorname{Cap}_{\theta,\phi}(A)-\log \operatorname{Cap}_{\theta,\psi}(A)\big|
\leq n\log(1+\omega).
$$
The comparison implies that either both capacities vanish or neither does.

**Proof with explicit competitor map.** Set $t=(1+\omega)^{-1}$. Given any $v\in\mathrm{PSH}(X,\theta)$ with $\phi-1\leq v\leq\phi$, define
$$
q=(1-t)\psi+tv-tM.
$$
Since $\psi+m\leq\phi\leq\psi+M$ and $\phi-1\leq v\leq\phi$,
$$
q\leq\psi,\qquad
q\geq \psi+t(m-1-M)=\psi-1.
$$
Consequently $q$ is a competitor for $\operatorname{Cap}_{\theta,\psi}$, and
$\theta_q=(1-t)\theta_\psi+t\theta_v$ is a positive convex combination of positive currents. Positivity and multilinearity of non-pluripolar products give $\mu_q\geq t^n\mu_v$ as Borel measures, including across their respective non-polar loci. Taking the supremum over all $v$ gives the right inequality of (D). Swapping $\phi,\psi$ (with the same oscillation $\omega$) gives the left one. No net/sequence passage or approximation theorem is needed for this new algebraic step.

**Strict improvement over the recorded form, and limits.** The printed $(2C+1)^n$ uses an absolute difference bound $|\phi-\psi|\leq C$ and is recovered from $\omega\leq2C$. If $\phi-\psi$ is a constant $c\neq0$, the new factor is **1** (exact equality), whereas the printed estimate with $C=|c|$ yields $(2|c|+1)^n$. This is a strengthening, **not** a claim that $(1+\omega)^n$ is optimal for all classes or domains. No capacity continuity for varying underlying currents, and no proof of the upstream mixed non-pluripolar multilinearity theorem, is asserted.

**Dependencies and proposal.** Uses Definition 16.25.5, pointwise PSH-order extension and the already integrated mixed non-pluripolar positivity principle appearing in Proposition 16.25.6. Optional sharpened remark after that proposition, preserving the original correct comparison. Affected dependents: relative-capacity changes of reference potential in Sections 16.25–16.27, if their hypotheses are otherwise satisfied.

## Coverage, exclusions, and verification boundary

These are two **new deductions** in previously sampled, nonexcluded §7.19.5 and §16.25.6. Contextually read §7.19.1–4, §16.25.4–5/.7, and previously logged issue inventories. No existing finding is declared resolved. **Theorem false? no. Proof gap established? no. Complete proof of the two stated deductions? yes, conditional only on the explicitly indicated integrated construction/measure facts.** No claim of whole-section certification, build, CI, formalization or mathematical verification of upstream dependency chains. The actual current ToC remains **25 chapters / 747 numbered sections / 0 fully certified entire mathematical sections**. All user-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work stays **deferred-by-user**; no such work was reopened. No changes to production `main`, source bodies, registries, permanent tags or published website.
