# Weighted Monge–Ampère addition, strict-barrier comparison, and singularity-envelope support — 2026-11-23

## Revisions and exact scope

Production main inspected: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Initial audit branch: **ec688d75f6842be59c2cdf275b0859fdea0bb2ea**. This review uses the actual integrated reading edition and does not certify all prior or transitive dependencies.

- Entire present-main §15.11, **Adding weighted Monge–Ampère measures**: docs/sections/equations-with-prescribed-singularities--adding-weighted-monge-ampere-measures/index.html; blob **0bc4468db8261e5203d311a2181bde8acf16c1df**, physical mathematical lines **6–100**. Theorem 15.11.1: source **non-kahler-pluripotential-theory:382EF8B0**, permanent **7A54D08FEB18**, statement lines 10–20, replacement proof lines 22–100.
- Entire present-main §15.13, **Comparison above a strict singular barrier**: docs/sections/equations-with-prescribed-singularities--comparison-above-a-strict-singular-barrier/index.html; blob **db560c935a7d651803427b6243957ea1f957b468**, mathematical lines **6–120**. Lemma 15.13.1 source **F564C83F**, permanent **E6E5D71344DD**, lines 13–43; Theorem 15.13.2 source **241F3E4D**, permanent **F71978C42841**, lines 45–98; Corollary 15.13.3 source **3262185F**, permanent **24CD508AEB8D**, lines 100–120.
- Entire present-main §16.21, **Singularity envelopes**: docs/sections/envelopes-and-model-potentials--singularity-envelopes/index.html; blob **8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a**, mathematical lines **6–81**. Definition 16.21.1 source **BF5AA585**, permanent **99168E437529**, lines 10–16; Proposition 16.21.2 source **92AD249D**, permanent **037CA226D141**, lines 19–59; Proposition 16.21.3 source **38793463**, permanent **5ADA09DD223E**, lines 61–81.
- Only selected upstream statement/proof passages: §15.9.3 at docs/sections/equations-with-prescribed-singularities--compactness-with-a-common-lower-barrier/index.html, blob **2d4d8889cbe39cf880723c59abcb6461b26812f7**, lines 53–65, source **786C08E2**, permanent **EFAF50966FDF**; and §16.28.55 at docs/sections/envelopes-and-volumes-of-singularities/index.html, blob **0bdddc04cbc0cefd05591fdffc0796f3405b2a69**, lines 943–955, source **EB19DA85**, permanent **9BBE1DE257CB**. These selected observations are NOT entire-section audits.

## POME-WEIGHTED-MA-LOGSUMEXP-SEMIGROUP-001

**Severity/status:** low / **verified conditional deduction** from the stated weighted-addition and uniqueness principles. This is **not a confirmed printed error**, not a complete transitive proof-chain certification, and not a new theory of regularization.

**Hypotheses.** Let the setting and assumptions of §15.11.1 hold: a semipositive big background form θ, a reference type φ such that P_{δθ}(φ) is nontrivial for some 0<δ<1, and λ>0. On the ordinary type of φ define

\[
 M_\lambda(u):=e^{-\lambda u}\operatorname{MA}^{\mathrm{ext}}_\theta(u),
 \qquad
 \mathscr D_{\varphi,\lambda}
 :=\{u\in\operatorname{PSH}(X,\theta):u\sim\varphi,\ M_\lambda(u)(X)<\infty\}.
\]

Weights are evaluated off pole sets; the measures give no mass to the pole sets. The finite-mass assumption is indispensable: it is *not* inferred for arbitrary singular potentials.

**Statement.** For any u,v in this class, the unique a furnished by §15.11.1 for the measure Mλ(u)+Mλ(v) defines u ⊞λ v=a. This is a **closed, commutative, associative, cancellative operation** on the finite-weighted-measure class. It is translation equivariant:
\[
 (u+t)\boxplus_\lambda(v+t)=(u\boxplus_\lambda v)+t,\quad t\in\mathbb R.
\]
For any k≥1 and real constants c₁,…,c_k, with u∈\mathscr D, repeated addition gives the *exact* log-sum-exp formula
\[
 \boxed{\quad (u+c_1)\boxplus_\lambda\cdots\boxplus_\lambda(u+c_k)
 =u-\lambda^{-1}\log\Big(\sum_{i=1}^k e^{-\lambda c_i}\Big).\quad}
\]
In particular, u ⊞λ u=u−(log 2)/λ. Writing m=min_i c_i, one has the sharp comparison
\[
 m-\frac{\log k}{\lambda}\le
 -\frac1\lambda\log\sum_i e^{-\lambda c_i}\le m.
\]
The lower bound is attained when all c_i=m; the upper bound is approached as all other c_i−m tend to +∞. No metric contraction, preservation of the pointwise order for arbitrary pairs, or existence of a neutral element is asserted.

**Complete conditional proof.** Adding a real constant changes no curvature current or non-pluripolar product; hence Mλ(u+t)=e^{−λt}Mλ(u), and it preserves ordinary type and finite weighted mass. For any u,v, Theorem 15.11.1 supplies exactly one a∼φ with Mλ(a)=Mλ(u)+Mλ(v); its right-hand side is finite, so a∈\mathscr D. Commutativity is immediate. Each parenthesization of the triple operation has the same measure Mλ(u)+Mλ(v)+Mλ(w), and uniqueness in the ordinary type gives associativity. If u⊞λ w=v⊞λ w, cancellation of the common finite positive measure Mλ(w) yields Mλ(u)=Mλ(v). Both u and v solve MAθ^{ext}(x)=e^{λx}Mλ(u), so the exponential uniqueness principle used at the end of §15.11 (Corollary 15.2.3, with the theorem's hypotheses) gives u=v. The translation formula follows by the scaling identity and uniqueness. Finally, the sum of the k translated weighted measures is (\sum_i e^{−λc_i})Mλ(u), exactly the weighted measure of the displayed translated candidate. Repeated application of the theorem and uniqueness gives the identity. The comparison inequalities follow from 1≤\sum_i e^{−λ(c_i−m)}≤k, with the stated equality/limit models. No interchange of limits, compactness of nets, or new analytic input is used in this algebraic deduction.

**Proposed addition / affected dependents.** An optional structural corollary after §15.11.1, documenting the exact normalization of repeated weighted addition; potentially useful to check the mass-augmentation argument in §15.12. There is **no correction** to the original theorem or its permanent source label. Any editorial integration belongs in a separately reviewed source/reader PR, not this audit branch.

## Independent audits of the printed arguments

**§15.11.** The mixed-product inequality of lines 33–39 has the factor 2^n, while the lower barrier uses D=C/2+n(log 2)/λ (lines 45–63). Indeed MAθ((u_j+v_j)/2)≥2^{−n}(MAθ(u_j)+MAθ(v_j)), and the bounded type difference controls |s_j−u_j|, |s_j−v_j|≤C/2. These yield the stated lower weighted domination, rather than an incorrectly reversed comparison. On E_j={min(u,v)>−j}, μ_j=μ by locality; since a_j≤0, the displayed e^{a_j} auxiliary error (not e^{λa_j}) is still bounded by its integral against μ because 0<e^{λa_j}≤1 for *every* λ>0. On X\E_j, both a_j and the limit a are ≤−j; the polynomial mass bound cited from §13.15.2 controls the e^{−j} tail. Identification under the bounded quasi-continuous cutoff in lines 85–97 invokes bounded product capacity continuity. These upstream principles are *recorded*, not independently proved in this increment. No new confirmed theorem error.

**§15.13.** The strict coefficient c<1 in Theorem 15.13.2 is essential, not a dispensable proof artifact: on a compact connected Kähler manifold with θ=ω, choose the permitted strict barrier ρ=0 and constant potentials u=−1, v=0. The lower-barrier and finite-difference hypotheses hold, and MAθ(u)=MAθ(v), so the inequality with c=1 holds on the whole {u<v}=X while the conclusion u≥v is false. This is a counterexample **only to the unprinted relaxation c≤1**, not to the stated theorem. The proof's choice (1−δ)^n>c and the strictly θ-psh local bump have the correct comparison direction. The existence of the analytic strict barrier cited as §5.36.5 is an external/upstream dependency of this reading, not a premise we have re-proved; any connection to the user-excluded approximation programme remains **deferred-by-user**.

**§16.21.** The competitor condition v≼u permits constants depending on v; the increasing rooftops of 16.21.2 need not share one singularity bound independent of k. Mixed non-pluripolar mass conservation in 16.21.2 is conditional on §13.8.8–9, including increasing-limit continuity. Proposition 16.21.3 combines contact support and monotone mass continuity. For C={Pθ[u]=Vθ}, its two printed propositions imply, whenever the totals are finite,
\[
 \mu_u(X)=\mu_{P_\theta[u]}(X)\le\mu_{V_\theta}(C),
 \qquad
 \mu_{V_\theta}(X)-\mu_u(X)\ge\mu_{V_\theta}(X\setminus C).
\]
This is an immediate **conditional check** of their combined direction, not a second finding and not a claim of pointwise equality of envelopes from equality of masses. §16.13.5, §16.12.1 and §13.8.8–9 are not transitively certified.

## Coverage, limitations, and disposition

- New complete direct present-main mathematical readings: **3 sections** (§§15.11, 15.13, 16.21); selected upstream excerpts: **2**. Historical first visits remain unreconciled, and this run certifies **zero full upstream proof chains**.
- New classified finding: **1 low verified conditional deduction**. New confirmed printed error: **0**; confirmed false theorem: **0**; verified full replacement: **0**. The c=1 countermodel tests a proposed weaker hypothesis only.
- The current **747-section inventory** and all prior findings are preserved. This does not say the other 744 sections have been fully checked.
- User-excluded **Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion** stay **deferred-by-user** (not certified). In particular, the smoothing-radius and regularization-specific sections were not claimed as reviewed or extended in this report.
- No build, project tests, Actions CI, main/source/registry/canonicalization/permanent-tag edits, merge, or website publication performed.
