# Positive-current extension cones and finite pluripolar restriction calculus

**Audit checkpoint:** 2026-10-24, selected integrated reading-edition inspection.  
**Reviewed current `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Permitted scope:** Skoda–El Mir extension, restriction of positive currents, integration currents, and ordinary current pushforward signs. **Not inspected:** the user-deferred Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale gluing, or positivity-loss completion programmes. This report does not certify those dependencies.

## Primary finding: POME-ELMIR-EXTENSION-CONE-001

**Status:** verified conditional deduction; **severity:** low. This is a formal consequence of established results, **not** a false theorem or independent certification of the Skoda–El Mir proof.

**Pinned integrated source:**
- Theorem 5.60.3 (Skoda–El Mir), original source id `demailly-complex-geometry-21C67190`, permanent tag `BB0A0DD22A5E`, `docs/sections/positive-current-extension-and-analytic-integration--extension-of-positive-currents-across-complete-pluripolar-sets/index.html`, main blob `6b5be95436780409c8ab09f7f344899ac9047e7a`, physical lines **69–107**.
- Corollary 5.60.6, source id `demailly-complex-geometry-3BEFC986`, permanent tag `53F93547F96E`, same file/blob, lines **109–118**.
- Lemma 5.60.2, source id `demailly-complex-geometry-3696536E`, permanent tag `899DA22762FD`, same file/blob, lines **18–67**; the local pole-cutoff construction is **not** re-opened as a regularization project.
- Context: Theorem 5.61.2, source id `demailly-complex-geometry-D713D40C`, permanent tag `B7EB7069B315`, `docs/sections/positive-current-extension-and-analytic-integration--integration-over-analytic-sets/index.html`, blob `4c8c14a1b438c49f4d43f63e9f54ed1756d09b4f`, physical lines **41–57**.

### Exact theorem and proof

Let $X$ be a complex manifold and $E\subset X$ closed and **locally complete pluripolar**. Let $T$ be a positive $d$-closed current of bidimension $(p,p)$ on $X\setminus E$ whose coefficient mass is locally finite up to $E$. Write $T^0$ for the coefficientwise **zero extension** given by Theorem 5.60.3 and define
$$
\mathcal C_E^p(X)=\{R\geq0:\ dR=0,\ R\text{ has bidimension }(p,p),\ \operatorname{supp}R\subseteq E\}.
$$
Then the set of all positive closed extensions $S$ of $T$ to $X$ is exactly the affine cone
$$
\boxed{\operatorname{Ext}^+(T;X)=T^0+\mathcal C_E^p(X).}
$$
Moreover, $T^0$ is the **unique** positive closed extension with zero trace mass on $E$.

**Proof.** Theorem 5.60.3 makes $T^0$ positive closed, equal to $T$ on the complement, and of zero coefficient mass on $E$. For any other positive closed extension $S$, Corollary 5.60.6 makes both $\mathbf1_ES$ and $\mathbf1_{X\setminus E}S$ positive closed. Coefficientwise restriction away from $E$ identifies $\mathbf1_{X\setminus E}S$ with $T^0$, since both restrict to $T$ and have zero coefficient mass on $E$. Consequently
$$
 S=T^0+\underbrace{\mathbf1_ES}_{R\in\mathcal C_E^p(X)}.
$$
Conversely, $T^0+R$ is positive closed and restricts to $T$ for every $R\in\mathcal C_E^p(X)$. Disjoint coefficient supports make $R$ unique. The zero-$E$-mass condition forces $R=0$, because every coefficient variation of a positive current is controlled locally by its trace measure. $\square$

The zero-mass qualification is essential. In dimension one take $X=\mathbb C$, $E=\{0\}$, $p=0$, and $T=0$ off $E$. Both $0$ and $c\delta_0$ ($c>0$) are positive closed bidimension-$(0,0)$ extensions; $\delta_0$ is top bidegree and is automatically $d$-closed. There is **no unconditional uniqueness** of positive closed extensions.

### Finite Boolean identities for coefficient restrictions

If $E,F$ are closed locally complete pluripolar, then $E\cup F$ and $E\cap F$ are also closed locally complete pluripolar. Locally, choose locally integrable psh functions $u,v$ whose exact pole sets are $E,F$. The psh functions $u+v$ and $\max(u,v)$ have exact pole sets $E\cup F$ and $E\cap F$, respectively. They are not identically $-\infty$: a finite union of pluripolar sets has no interior. Closure is preserved by finite union and intersection.

For every positive closed current $S$ on $X$, put $P_E(S)=\mathbf1_ES$, where restriction is taken **coefficientwise**. Corollary 5.60.6 proves that all terms remain positive closed, while elementary indicator identities give
$$
\boxed{P_E(P_F(S))=P_{E\cap F}(S),\qquad
P_E(S)+P_F(S)=P_{E\cup F}(S)+P_{E\cap F}(S).}
$$
Also $P_E^2=P_E$, $0\le P_E(S)\le S$ in the positive-current cone, and $S=P_E(S)+\mathbf1_{X\setminus E}S$ splits the trace into mutually singular positive measures. These are **additive, positively homogeneous maps of cones**; no unjustified claim of a continuous linear projection on arbitrary signed currents is made.

**Dependents and proposed correction:** an optional separately tagged corollary after 5.60.6, referencing the pinned theorem/corollary without replacing their statements, permanent labels, historical attribution, or proofs. This is useful for Siu/divisorial-current decompositions, support restrictions, and b-divisor trace arguments. The mathematical body is unchanged, and no additional analytic extension theorem is assumed.

## Other selected proof checks (none is whole-section certification)

1. **§5.60.3, physical lines 73–107.** The printed $p=1$ argument bounds the mass of $dv_k\wedge d^cv_k\wedge T$ and then eliminates $\theta'(v_k)dv_k\wedge T$ using Cauchy–Schwarz and dominated convergence against the *zero-extended* trace measure. The general $p$ reduction wedges with constant strongly positive $(p-1,p-1)$-forms. The bidegrees and local finite-mass usage were checked; local Richberg smoothing was **not** rederived and the extension theorem is not certified in full.
2. **§5.61.1–2, physical lines 7–55**, tags `8C07385777E6` (source `demailly-complex-geometry-C265E60E`) and `B7EB7069B315`. For each local finite projection of a $p$-dimensional analytic branch, a $q$-sheeted covering gives the projected $(p,p)$-form integral off the discriminant. A basis of decomposable positive forms bounds the Euclidean trace, yielding locally finite mass. Theorem 5.61.2 applies 5.60.3 to the **singular locus**, not all of $A$. Finite analytic parametrization, singular-stratum dimension and smooth integration-current results remain **conditional internal dependencies**, not independently certified.
3. **§5.53.1–2, physical lines 10–76**, `docs/sections/real-currents-submersions-and-homotopies--currents-on-real-manifolds-and-fiber-signs/index.html`, main blob `188386272430128f7ae086f28d5e685ce45dec3c`, permanent tags `CCE8A237C582` and `01AAD02BF915`. The sign $d(F_*T)=(-1)^{m_1-m_2}F_*dT$ agrees with a degree-$q$ current acting on $(m_1-q)$-tests: the target degree is $m_2-(m_1-q)$, and the derivative exponents differ by $m_1-m_2$. The submersion pullback factor $(-1)^{rq}$ agrees with fiber-first orientation. Selected sign check only.
4. **§5.44.7, physical lines 92–185**, `docs/sections/plurisubharmonic-functions-and-singularities--integration-against-non-pluripolar-measures/index.html`, main blob `15c449ab02d6f8df98edfa07f5286af7ac8e72d1`, permanent tag `27CEBF2AA643`. For smooth bounded potentials, the torsion product rule at equation `5.44.8` follows by applying $d$ to $d^c(hT)$ with the graded Leibniz signs. The passage to bounded nonsmooth potentials and upstream capacity-continuity inputs were **not** certified; no excluded approximation proof was inspected.

**Findings:** one new verified conditional deduction (the extension-cone classification and finite Boolean calculus), no newly established false theorem or proof gap. Existing ledger findings are untouched. All results remain conditional on the explicitly cited upstream theorems. **Not run:** Pome build, CI, website publishing, full mathematical certification, numeric scripts, or formal proof verification.
