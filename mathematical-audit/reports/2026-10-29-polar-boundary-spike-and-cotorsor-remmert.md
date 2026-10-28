# A polar boundary spike for a nonpolar compact; Remmert reduction of a zero-ruling cotangent torsor

**Date:** 2026-10-29 (Asia/Shanghai).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Starting review-branch HEAD:** 558b2abca69b5f2e2d118a0cbcb03478bf7413f4.  
**Scope:** the specified nonexcluded proofs and explicit models of §§3.8.2 and 12.33.3. Neither complete section, nor its upstream proof chain, is certified.

## POME-PLANAR-GREEN-POLAR-BOUNDARY-SPIKE-001

**Severity / status:** low / **verified conditional deduction**. The printed Proposition 3.8.2 remains correct; this is not an error report.

**Exact source.** Integrated reading edition at docs/sections/planar-green-functions-and-conformal-maps/index.html, main blob bfee348bb5f4bbfaa4515e5c9333789a13dae861, physical lines 53–69. Proposition **3.8.2**, source label klimek-pluripotential-theory-886FBC1A, permanent tag **3F05222ECC9E**. Example 3.8.3, tag FADCC209A003, lines 73–82, was consulted only for comparison.

**Hypotheses and explicit example.** Take the **nonpolar** compact planar set

$$
K=\overline{\mathbb D}\cup\{2\}.
$$

Let $V_K$ denote the raw polynomial logarithmic extremal envelope, and $V_K^*$ its upper-semicontinuous regularization. If $\deg p=d\ge1$ and $\sup_K|p|\le1$, applying the exterior maximum modulus principle to $p(z)/z^d$ (including infinity) gives

$$
|p(z)|\le |z|^d\quad (|z|\ge1).
$$

Hence $V_K(z)\le\log^+|z|$. Conversely, for each integer $N\ge1$,

$$
p_N(z)=\frac{z-2}{3}z^N,\qquad \deg p_N=N+1
$$

has supremum at most one on the disk and vanishes at the other point $2$. For each fixed $|z|>1$ with $z\ne2$,

$$
\lim_{N\to\infty}\frac{\log|p_N(z)|}{N+1}=\log|z|.
$$

The constant polynomial one gives the universal lower bound zero. On $K$, every normalized polynomial has absolute value at most one. It follows **exactly** that

$$
V_K(z)=
\begin{cases}
\log^+|z|,&z\ne2,\\
0,&z=2,
\end{cases}
\qquad
V_K^*(z)=\log^+|z|\quad\text{for every }z.
$$

In particular, $V_K(2)=0$ but $V_K^*(2)=\log 2>0$. The unbounded connected component of $\mathbb C\setminus K$ is

$$
\Omega=\{\,|z|>1\,\}\setminus\{2\},
$$

and the **isolated boundary point** $2\in\partial\Omega$ is polar. Nevertheless,

$$
\lim_{\Omega\ni z\to2}V_K^*(z)=\log2\ne0.
$$

Thus the polar exceptional set in the boundary claim of Proposition 3.8.2 **cannot be omitted even for nonpolar $K$**. The positive harmonic function $V_K^*|_\Omega$ remains bounded near every finite boundary point, so adding bounded-boundary hypotheses does not erase this exceptional-point phenomenon.

**Proposed correction / dependents.** No theorem correction is required. An optional example after Proposition 3.8.2 should distinguish $V_K|_K=0$ from the generally false assertion $V_K^*|_{\partial\Omega}=0$ everywhere. Preserve the original quasi-everywhere qualifier in Green/equilibrium arguments. This example is distinct from the existing Example 3.8.3 on *nonuniqueness* caused by added positive harmonic boundary spikes.

**Proof boundary.** The computation uses the polynomial extremal definition and elementary maximum modulus. It does **not** independently certify all equilibrium-support, Myrberg, or polar-boundary minimum-principle inputs used elsewhere in §3.8.2.

## POME-COTORSOR-A1-REMMERT-001

**Severity / status:** low / **verified conditional deduction**. The printed Proposition 12.33.3 is correct in the stated model; this is not a false-theorem finding.

**Exact source.** Integrated reading edition at docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--cotangent-extensions-with-zero-ruling-component/index.html, main blob 67f63edb723e3cfd5ddb9723cc6061190e473feb, physical lines 75–99. Proposition **12.33.3**, source label non-kahler-pluripotential-theory-B736897D, permanent tag **0414E2D53266**. Its zero-ruling charts are on lines 7–20; the already-reviewed graded section algebra of Proposition 12.33.2 (tag A78CB65BF75E) is a separate assertion.

**Conditional input.** The printed proposition identifies the torsor's universal cover as

$$
\widetilde T_W\simeq\mathbb C^2\times\operatorname{Tot}(\mathcal O_{\mathbb P^1}(-2)).
$$

We accept that global identification here and **do not claim to have independently proved the elliptic-lattice quotient construction**.

**Explicit blowdown.** On the finite chart of $\operatorname{Tot}(\mathcal O(-2))$ let $t$ be the base coordinate and $y$ the fiber coordinate. The opposite chart has

$$
v=t^{-1},\qquad y_\infty=-t^2y.
$$

The three functions $A=y$, $B=ty$, $C=t^2y$ are holomorphic on both charts: on the second chart they become

$$
(A,B,C)=(-v^2y_\infty,-vy_\infty,-y_\infty).
$$

They satisfy $AC=B^2$, giving a holomorphic map

$$
q:\operatorname{Tot}(\mathcal O_{\mathbb P^1}(-2))
\longrightarrow Q:=\{(A,B,C)\in\mathbb C^3:AC=B^2\}.
$$

If $A\ne0$, its inverse reads $t=B/A$, $y=A$; if $C\ne0$, its inverse reads $v=B/C$, $y_\infty=-C$. These inverses agree on the overlap. Thus $q$ is biholomorphic away from the zero section and the cone vertex; its entire fiber over the vertex is the exceptional $\mathbb P^1$. The map is **proper**: the base $\mathbb P^1$ is compact, and on the finite-base and infinite-base compact charts the respective fiber coordinates are bounded by the coordinates $A$ and $C$ on the preimage of a compact subset of $Q$. Hence $q$ contracts exactly the rational curve whose normal bundle is $\mathcal O_{\mathbb P^1}(-2)$, with self-intersection $-2$.

**Descent of global holomorphic functions.** Every holomorphic function on the total space is constant on the compact exceptional $\mathbb P^1$, and its restriction off the exceptional curve descends through the explicit biholomorphism to $Q\setminus\{0\}$. The quotient parametrization

$$
\mathbb C^2\longrightarrow Q,\qquad (s,t)\longmapsto(s^2,st,t^2)
$$

identifies $Q$ with the finite holomorphic quotient $\mathbb C^2/\{\pm1\}$ and proves its normality. Lift a holomorphic function from $Q\setminus\{0\}$ to an even holomorphic function on $\mathbb C^2\setminus\{0\}$. Hartogs extension across the origin yields an even entire function, which descends to $Q$. The same argument works **with arbitrary holomorphic dependence on the untouched $\mathbb C^2$ factor** (use Hartogs locally with that factor as a parameter). Thus pullback gives an isomorphism

$$
H^0(\mathbb C^2\times Q,\mathcal O)
\xrightarrow{\;\sim\;}
H^0(\mathbb C^2\times\operatorname{Tot}(\mathcal O(-2)),\mathcal O).
$$

The cone $Q$ is a closed analytic subspace of affine space and is Stein. Consequently $\operatorname{id}_{\mathbb C^2}\times q$ is the **proper Remmert reduction** of the stated universal cover: it has connected fibers, Stein target, and pushforward structure sheaf equal to the target's structure sheaf. The cover is therefore holomorphically convex but **not** holomorphically separable, exactly because a compact projective line contracts over each point of $\mathbb C^2\times\{0\}$.

**Proposed correction / dependents.** Optional geometry corollary after Proposition 12.33.3. Preserve the distinction from the case of nonzero ruling component and do not infer that two torsors are isomorphic, or equally Stein, from their identical graded section algebras in §§12.32.2 and 12.33.2. The contraction calculation uses only the printed explicit charts and elementary complex geometry outside the excluded programme.

**Proof boundary.** This does **not** prove the original torsor on the elliptic ruled surface is holomorphically convex; it computes the Remmert reduction only for the **identified universal cover**.

## Actual coverage and standing exclusions

Selected new nonexcluded passages: **§3.8.2** (first direct polynomial-boundary example) and **§12.33.3** (first direct universal-cover contraction model). §§3.8.1 and 12.33.2 served as context without reopening or repeating earlier findings. Two conditional deductions, **no** newly confirmed false theorem, certified complete proof, or entire section. Existing coverage inventory is **25 chapters / 747 numbered sections**, unchanged because production main is unchanged; it was not re-counted from scratch here. All previous open, repaired, duplicate, external-input and deferred statuses are retained.

All dedicated **Demailly approximation/regularization**, **Bergman**, **$L^2$**, **Ohsawa–Takegoshi**, **multiscale-atlas**, and **positivity-loss** proof-completion projects remain **deferred-by-user**, not certified or re-opened. No edits to source manuscripts, mathematical bodies, canonical registries, permanent tags, main, or published website; no build, CI, formalization, or project test was run.
