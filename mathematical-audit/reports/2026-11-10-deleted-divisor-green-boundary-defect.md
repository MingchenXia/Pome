# Mathematical audit — Green functions on a polydisc with a deleted analytic divisor (2026-11-10)

**Stable finding:** `POME-GREEN-POLAR-DELETION-BOUNDARY-DEFECT-001`. **Severity:** low. **Status:** verified conditional deduction / explicit sharpness model; **no false published theorem identified**.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; audit branch `review/mathematical-audit`. The actual production table of contents contains 25 chapters and 747 distinct numbered sections. This is a selected cross-section review, not an entire-section certification.

## Exact integrated reading-edition anchors

1. `docs/sections/boundary-zero-green-functions-and-hyperconvexity/index.html` (blob `4680003b95a90211015a03b44bd634eb331fb426`): Proposition **7.25.1** source `klimek-pluripotential-theory:22DDEF74`, permanent `B63D9FDC459B`, lines **8–33**; Theorem **7.25.2** source `klimek-pluripotential-theory:10813A3E`, permanent `033C98D473B9`, lines **38–58**. The theorem asserts equivalence, for a bounded domain, between continuous negative PSH exhaustion and boundary-zero Green envelopes (for one or every pole).
2. `docs/sections/isolated-pole-green-envelopes-and-continuity/index.html` (blob `e82b6baaa0061f55aeea2f88ec0567d9653ecd61`): Proposition **7.17.1**, source `klimek-pluripotential-theory:02864DC1`, permanent `3360BE3E2E50`, lines **7–29** (Green competitor definition and pluripolar-deletion invariance expressly noted in its proof); Proposition **7.17.2**, source `klimek-pluripotential-theory:75CBD17E`, permanent `7B9EA3C07531`, lines **35–47** (the polydisc formula).
3. `docs/sections/plurisubharmonic-functions--extension-across-closed-exceptional-sets/index.html` (blob `fdcb827646cee9efcdeae37dfc8d6daf1c2a225b`): Theorem **5.11.1**, source `foundations-of-pluripotential-theory:4FA8E03B`, permanent `C910F1109424`, lines **11–36** (PSH extension across an analytic set under an upper bound).

## Independent explicit model and complete verification of its conditional deduction

Fix any integer (n\geq 2), set
[
  P=\mathbb D^n,\qquad H=\{z\in P:z_1=0\},\qquad D=P\setminus H=\mathbb D^*\times\mathbb D^{n-1},
]
and choose (a=(a_1,\ldots,a_n)\in D), so (0<|a_1|<1). Write
[
\varphi_b(\zeta)=\frac{\zeta-b}{1-\overline b\zeta}.
]
Then the **exact pluricomplex Green envelope on the deleted-divisor domain** is
[
\boxed{\quad
 g_D(z,a)=g_P(z,a)=\max_{1\leq j\leq n}\log|\varphi_{a_j}(z_j)|,\quad z\in D.
\quad} \tag{A}
]
In particular, for **every** (w\in\mathbb D^{n-1}), the interior deleted-boundary limit exists and is
[
\boxed{\quad
 \lim_{D\ni z\to(0,w)}g_D(z,a)
 =\max\left\{\log|a_1|,\; \max_{2\le j\le n}\log|\varphi_{a_j}(w_j)|\right\}<0.
\quad} \tag{B}
]
Taking (w=(a_2,\ldots,a_n)) makes this limit **exactly** (\log|a_1|<0). Thus the zero-boundary hypothesis in Theorem 7.25.2 cannot be weakened to mere bounded pseudoconvexity, and the failure is quantitative at each point of the removed hypersurface. No theorem in §7.25 is contradicted.

**Step 1 — extension and equality of competitor families.** Let (u\in\mathrm{PSH}(D)) be any negative Green competitor with a logarithmic pole at (a). Since (u\le0), it is locally bounded above near (H). The set (H) is closed analytic in (P), so Theorem 5.11.1 extends (u) uniquely to (\widetilde u\in\mathrm{PSH}(P)). Its bound (\widetilde u\le0) follows directly from the upper-limit formula. The pole condition near (a\notin H) is unchanged. Therefore (\widetilde u) is an admissible competitor for (g_P(\cdot,a)), and (u\le g_P|_D). Conversely, restricting any Green competitor from (P) to (D) gives a competitor on (D), hence (g_P|_D\le g_D). Equality follows without any Monge–Ampère mass passage, approximation, Bergman kernel, or excluded regularization argument.

The extension step is also visible directly: on (D), (u_\epsilon=u+\epsilon\log|z_1|\) extends as (-\infty) across (H) and is PSH by the one-dimensional puncture-removability criterion on transverse complex lines (it is identically (-\infty) on a line contained in (H)); (u_\epsilon\uparrow u) as (\epsilon\downarrow0) off (H), and upper regularization gives the unique extension. This is a specialization of the verified internal statement, **not** a claim to reprove all its other cases.

**Step 2 — polydisc Green formula and boundary defect.** The coordinate automorphisms (z_j\mapsto\varphi_{a_j}(z_j)) take (a) to zero. At zero, the balanced-domain bound from Proposition 7.17.2 with the max norm (h(z)=\max_j|z_j|) gives (g_P(z,0)=\log\max_j|z_j|). Its logarithm is PSH, so the bound is attained; coordinate biholomorphic invariance gives (A). Taking the limit of this explicit finite maximum at ((0,w)) gives (B). Every term is strictly negative for (w\in\mathbb D^{n-1}), while the first is finite, so the maximum is a finite negative number.

**Step 3 — bounded pseudoconvexity does not suffice.** The function
[
 \Phi(z)=-\log|z_1|^2-\sum_{j=1}^n\log(1-|z_j|^2)
]
is smooth PSH and proper on (D): the first summand is pluriharmonic away from (H), each other summand is PSH, and a bounded sublevel keeps (|z_1|) bounded below and all (|z_j|) bounded away from one. Thus (D) is a bounded pseudoconvex domain with a smooth PSH exhaustion (unbounded above). Nevertheless no **negative** PSH exhaustion (q<0) exists on (D). Indeed, for (p=(0,w)\in H), relative compactness of every negative sublevel forces (q(z)\to0) as (D\ni z\to p). Extend (q\le0) across (H) as in Step 1; the extension has an interior maximum (\widetilde q(p)=0). The PSH maximum principle on the connected polydisc makes (\widetilde q\equiv0), contradicting (q<0) on (D). This gives a second direct proof that Theorem 7.25.2 correctly excludes (D).

**Scope and dependencies.** The two explicit equalities (A)–(B) follow from the displayed polydisc formula and the analytic-set removable theorem; only their *selected* passages were independently reconciled here. No full certification of the general §5.11 extension proof, arbitrary-domain Green comparison, or the §7.25 hyperconvexity equivalence is asserted. The analytic divisor is not a singularity of the Green function at the fixed retained pole (a); the obstruction is solely a new boundary stratum. This differs from previously audited **planar compact-set extremal boundary outliers** and from the known §7.17.1 abstract deletion-invariance assertion by giving the all-dimensional precise boundary values, the smooth pseudoconvex exhaustion, and an independent negative-exhaustion obstruction.

**Proposed addition (not applied):** Append an explicit example after Theorem 7.25.2 stating (A), (B), and the distinction between positive proper PSH exhaustions and negative PSH exhaustions. Keep the theorem, its assumptions, its labels, attribution and the proof unchanged.

**Potentially relevant dependents (not deemed erroneous):** the use of hyperconvexity in §7.17.7 and the single-pole implication in §7.25.2. The example warns future readers not to infer either hypothesis from pseudoconvexity alone.

**Excluded scope / operational record:** Demailly approximation or regularization, and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain `deferred-by-user` (not resolved). No source text, production main, registries, canonicalization, permanent tags, private scans, builds, tests, CI or website publication were changed or run.
