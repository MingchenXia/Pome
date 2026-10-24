# 2026-10-24 — Positive-volume comparison: complete net uniformity and uniform Lelong control

**Baseline:** main commit b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit branch at start: a2b15d37528ac44513466941ed339b40fea0fd92. This report concerns the **integrated reading edition** only. The user-deferred Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme was neither read nor pursued; old related findings remain **deferred-by-user**, not resolved.

## Exact integration locations and actual scope

| Reading location | Integrated main source (Git blob SHA) | Stable source label, permanent tag and physical HTML anchors | Scope |
| --- | --- | --- | --- |
| §13.18.3, quantitative comparison | docs/sections/volumes-under-bounded-mass--volume-deficits-and-relative-full-mass/index.html (28323e5b08b0f7e53567f641bd9e4223472bc331) | non-kahler-pluripotential-theory-0442EA52 / 169DBA6BAF3B, lines 53–73 | Dependency: checked the precise order, lower-volume, deficit hypotheses and constant uniform in the point on each **fixed** modification. Not a new certification of the stretching lemma. |
| §13.19.1, .4–.5, .8 | docs/sections/volumes-under-bounded-mass--domination-and-ordinary-envelopes/index.html (aa11cda5105062bb7d7b5eaaa1396940c679e097) | .1 non-kahler-pluripotential-theory-214ED53E / B390F0847B3A, lines 10–41; .4 non-kahler-pluripotential-theory-2A0EEDDB / 50A87754E163, lines 64–93; .5 non-kahler-pluripotential-theory-66EB0216 / CB29AE1DFDA3, lines 97–126; .8 non-kahler-pluripotential-theory-CD933D3B / B0CCD40EE4B7, lines 204–215 | Read contact-support/domination and ordinary-envelope volume arguments; .6 lines 133–200 was additionally inspected for context, **not** certified. |
| §13.21.1–.3 | docs/sections/volumes-under-bounded-mass--monotone-limits/index.html (2aa812a8962e7108459c80492c893c0c64a70b6d) | .1 non-kahler-pluripotential-theory-3DA9EA38 / 453D4DA50352, lines 10–76; .2 non-kahler-pluripotential-theory-1220EC31 / BE27C58EE55B, lines 82–198; .3 non-kahler-pluripotential-theory-1500C241 / EE58E71478F6, lines 203–221 | Selected monotone model/volume proofs; the later trace corollary .5 (lines 247–273) was read only for boundary of scope and its excluded approximation input was not reopened. |
| §13.22.1, .4, .5, .7 | docs/sections/volumes-under-bounded-mass--cauchy-convergence-of-model-potentials/index.html (390f280e62ce8ba01de30f6b1ed52b4aa7fb10e4) | .1 non-kahler-pluripotential-theory-82BBCEC3 / A220D62C8412, lines 10–20; .4 non-kahler-pluripotential-theory-6F23D12A / 38359A611D4C, lines 55–90; .5 non-kahler-pluripotential-theory-13BB878E / 412DBAD823B9, lines 97–134, equation 13.22.6 tag DBE56A98BF3E lines 99–101; .7 non-kahler-pluripotential-theory-54605E21 / 62ECCE0A41E6, lines 138–196 | Direct proof reading of the comparison, separation, quasi-triangle and sequential completion. Example .8 lines 203–217 checked for strict-volume-bound necessity only. |
| §13.23.1–.3 | docs/sections/volumes-under-bounded-mass--rooftops-and-capacity-convergence/index.html (2b0162752e9800061002119630703701c814a2ec) | .1 non-kahler-pluripotential-theory-126FCF2C / 2B568CD72F9D, lines 10–42; .2 non-kahler-pluripotential-theory-06C3A6D1 / 1542F41C8A51, lines 49–90; .3 non-kahler-pluripotential-theory-0A2EE475 / 7D5F8FB5CFAB, lines 97–160; equation 13.23.4 tag 00C1CF12A199 lines 152–154 | Inspected stretching-to-rooftop and capacity-sandwich passages; upstream mass/locality results remain conditional. |

These are selected proof passages, **not** complete certification of five sections or their dependencies. The exact current table of contents still contains 747 sections. §13.20 was *not* promoted to proof-level review. No new false printed theorem was established.

## POME-VOLCOMP-UNIFORM-NETS-001

**Severity:** low. **Status:** verified conditional deduction, not a false theorem and not a correction to a printed theorem. **Prerequisites:** Proposition 13.22.4 (separation on positive lower-volume models), Proposition 13.22.5 / (13.22.6) (controlled quasi-triangle), Theorem 13.22.7 (sequential completeness). Their own upstream bounded-mass/stretching proofs are not independently certified here.

Fix a compact Hermitian background with the bounded mass property and \(\delta>0\). Write
\[
 \mathcal M_\delta(\theta)
 =\{u=P_\theta[u]:\underline{\operatorname{vol}}_\theta(u)\geq\delta\},
 \qquad
 d(u,v)=2U(\max(u,v))-U(u)-U(v).
\]
This comparison is symmetric, finite and nonnegative, but in general **does not obey the triangle inequality**. Put
\[
 \psi(s)=2nM\min\{1,(2s/\delta)^{1/n}\}.
\]
Equation (13.22.6) says
\[
 d(x,z)\leq d(x,y)+d(y,z)+\psi(d(y,z)).
 \tag{1}
\]

**Claim.** The sets \(V_\varepsilon=\{(x,y):d(x,y)<\varepsilon\}\), \(\varepsilon>0\), form a countably based **Hausdorff uniformity** on \(\mathcal M_\delta(\theta)\). Every Cauchy **directed net** for this uniformity converges to an element of \(\mathcal M_\delta(\theta)\); equivalently, this uniformity is complete.

**Proof.** The diagonal lies in every \(V_\varepsilon\), symmetry is immediate, and Proposition 13.22.4 gives \(\bigcap_{\varepsilon>0}V_\varepsilon=\Delta\). Given \(\varepsilon>0\), choose \(\eta>0\) with \(2\eta+\psi(\eta)<\varepsilon\); this is possible since \(\psi(s)\to0\) as \(s\downarrow0\). Formula (1) yields
\[
 V_\eta\circ V_\eta\subset V_\varepsilon.
\]
Thus the entourages define a Hausdorff uniformity, with countable base \(V_{1/k}\).

Let \((x_i)_{i\in I}\) be a Cauchy net, where \(I\) is any directed set. For each positive integer \(k\), choose \(j_k\in I\) such that \(d(x_i,x_{i'})<1/k\) whenever \(i,i'\geq j_k\). By directedness choose increasing indices \(i_1\leq i_2\leq\cdots\) with \(i_k\geq j_k\) for each \(k\). The sequence \(x_{i_k}\) is \(d\)-Cauchy: if \(p,q\geq k\), then \(d(x_{i_p},x_{i_q})<1/k\). Theorem 13.22.7 supplies \(x\in\mathcal M_\delta(\theta)\) with \(d(x_{i_k},x)\to0\).

For **every** \(i\geq i_k\), (1), with intermediate point \(x_{i_k}\), gives
\[
 d(x_i,x)\leq \frac1k+d(x_{i_k},x)
                 +\psi(d(x_{i_k},x)).
\]
The right side tends to zero independently of \(i\geq i_k\); hence the entire directed net converges to \(x\). No countable cofinal subset of \(I\), nor sequential compactness of a general net, has been assumed. Uniqueness follows from the entourage separation and (1). \(\square\)

**Proposed optional addition:** a corollary after §13.22.7 stating this complete uniform structure, explicitly distinguishing it from a metric triangle inequality. This is a **new consequence** of the printed estimates, not a replacement of the sequential theorem. **Affected downstream topics:** nets of ordinary model potentials, directed approximation comparisons, and convergence statements where a true net-level notion of completeness is useful.

## POME-VOLCOMP-LELONG-HOLDER-001

**Severity:** low. **Status:** verified conditional deduction, not a false printed theorem. **Prerequisites:** the monotonicity of upper/lower singularity volumes, the definition of \(d_\theta\), and Proposition 13.18.3 (ordered volume-deficit Lelong bound). None of the latter's stretching inputs is newly certified.

**Claim.** For **any** \(u,v\in\mathrm{PSH}(X,\theta)\) with
\[
 \underline{\operatorname{vol}}_\theta(u)\geq\delta>0,\qquad
 \underline{\operatorname{vol}}_\theta(v)\geq\delta,
\]
and any **fixed** smooth compact modification \(\pi:Z\to X\), the constant \(C_\pi\) from Proposition 13.18.3 satisfies
\[
 \boxed{\sup_{z\in Z}|\nu(u\circ\pi,z)-\nu(v\circ\pi,z)|
 \ \leq\ C_\pi\min\{1,(d_\theta(u,v)/\delta)^{1/n}\}.}
 \tag{2}
\]
The same bound holds for generic divisorial Lelong numbers on \(Z\). In particular, a \(d_\theta\)-convergent net of positive-lower-volume models has **uniformly convergent Lelong profiles** on each fixed modification.

**Proof.** Set \(m=\max(u,v)\), \(D_u=U(m)-U(u)\geq0\), and \(D_v=U(m)-U(v)\geq0\). Monotonicity gives \(\underline{\operatorname{vol}}_\theta(m)\geq\delta\), while
\[
 D_u+D_v=d_\theta(u,v),\qquad 0\leq D_u,D_v\leq d_\theta(u,v).
\]
Both ordered pairs \(u\preceq m\) and \(v\preceq m\) satisfy the hypotheses of Proposition 13.18.3, with reference \(m\). Consequently, for every \(z\in Z\),
\[
 A_z:=\nu(u\circ\pi,z)-\nu(m\circ\pi,z)\in[0,L],\quad
 B_z:=\nu(v\circ\pi,z)-\nu(m\circ\pi,z)\in[0,L],
\]
where \(L=C_\pi\min\{1,(d_\theta(u,v)/\delta)^{1/n}\}\). Hence
\(|\nu(u\circ\pi,z)-\nu(v\circ\pi,z)|=|A_z-B_z|\leq L\);
notably this incurs **no extraneous factor two**. Taking suprema proves (2). Generic divisorial values obey the same argument, or follow from the pointwise bound. For convergent nets, apply (2) to each term and its \(d_\theta\)-limit. \(\square\)

On \(\mathcal M_\delta(\theta)\), (2) makes the Lelong-profile map into bounded functions on any fixed modification uniformly \(1/n\)-Hölder near zero for the volume-comparison uniformity. Combining with the first claim, each \(d_\theta\)-Cauchy net converges in \(d_\theta\) **and** uniformly in Lelong profile after any fixed modification. This does **not** claim a bound uniform in all modifications: \(C_\pi\) depends on \(\pi\). It also does not assert multiplier-ideal equality or reopen the excluded approximation programme.

**Proposed optional addition:** a corollary adjoining §13.22.5 or §13.23.3, with the order-free \(\max(u,v)\) proof. **Affected downstream topics:** trace and divisorial data, ordinary model completions, and comparisons under fixed birational models. The \(1/n\) exponent is already visible in the **previously** checked isolated-pole volume deficit; that older calculation is not counted as a fresh result here.

## Additional selected review and limitations

- Theorem 13.21.2: checked the fixed-background stretching and the varying-background convex correction at physical lines 98–195, in particular \(c_j=d/(d+\varepsilon_j)\), \(\theta+\mathrm{dd}^c f_j\geq c_j(\theta_j+\mathrm{dd}^c q_j)\), and the volume squeeze. No unproved interchange of directed nets was inserted.
- Theorem 13.22.7: checked its use of a fast **sequence** and the positive-mass rooftop tail, without silently treating that sequence as a cofinal subnet of an arbitrary net. The net extension above uses the quantitative quasi-triangle instead.
- Theorem 13.23.3: checked the finite rooftop and monotone upper/lower sandwiches, equations (13.23.4) and capacity conclusion. Its pre-existing locality/monotone-capacity prerequisites were not fully reproved.
- Ordinary versus ideal models, permanent/source tags, normalizations, and the fact that \(d_\theta\) is not a metric are kept distinct. No new duplication/circularity or false theorem was confirmed in the selected passages. There is no claim of whole-section, whole-chapter or whole-project verification.

**No scripts, test suites, site builds, CI, publishing, source-branch edits or tag/registry/body changes were undertaken.** The historical deferred-by-user Demailly work remains deferred rather than resolved or certified.
