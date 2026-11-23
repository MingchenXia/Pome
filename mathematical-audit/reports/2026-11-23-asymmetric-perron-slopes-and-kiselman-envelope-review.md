# Mathematical audit — envelope operators, the minimum principle, and asymmetric Perron slopes

Date: 2026-11-23. Reviewed **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Working audit branch: \`review/mathematical-audit\`. This report assesses the integrated reader, not merely statement titles or historical source numbering. It does not edit the reading edition.

## Exact direct coverage

- **Complete mathematical §5.40**: \`docs/sections/plurisubharmonic-functions-and-singularities--obstacle-envelopes/index.html\`, main blob \`30716faee83d2ac0ec84b3684e319210980bd14f\`, physical lines 7–326. In particular Lemma 5.40.1 (source \`non-kahler-pluripotential-theory:9A752415\`, permanent \`294BB4EEA84F\`, lines 44–65); Proposition 5.40.3 (\`ACF08E79\`/\`630365A8F8B8\`, lines 97–113); Lemma 5.40.5 (\`6BA759F3\`/\`44FD5A853A0A\`, lines 142–161); Proposition 5.40.6 (\`F8E56269\`/\`F031A16FF76F\`, lines 169–198); Lemma 5.40.7 (\`1F642B5B\`/\`4798FCFAC293\`, lines 206–232); Proposition 5.40.10 (\`76760C7D\`/\`B986B6AE211B\`, lines 250–279); and Proposition 5.40.12 (\`3CD5936B\`/\`1709375DAB71\`, lines 293–321).
- **Complete mathematical §5.41**: \`docs/sections/plurisubharmonic-functions-and-singularities--the-minimum-principle/index.html\`, main blob \`3a96ad51514a61efa6802d09305f90a4c9cbef2d\`, physical lines 7–160. Lemma 5.41.1 (\`909C5329\`/\`ADD743D2224C\`, lines 11–18); Proposition 5.41.3 (\`9EFFCF0A\`/\`ED1DA0551379\`, lines 35–62); Lemma 5.41.5 (\`3F11F21A\`/\`742009E66DA3\`, lines 74–103); Lemma 5.41.8 (\`30DCC863\`/\`FAE98D3A3F69\`, lines 122–132); and Theorem 5.41.9 (\`F5C5A87A\`/\`5EA08D4F62B2\`, lines 137–160).
- **Complete mathematical §17.16**: \`docs/sections/perron-interpolation-and-the-geodesic-equation/index.html\`, main blob \`dc8dc381257360c94fe1c792499bb1ddf1bf5997\`, physical lines 7–629. Its principal envelope and variation statements, Hopf reduction, raw-action counterdirections, explicit smooth rays and singular finite-energy threshold were directly read; see the checkpoints below.
- **Selected nonexcluded §20.8 only**, \`docs/sections/divisorial-restricted-volumes/index.html\`, main blob \`8eb1127568e77d6d045098361c366ceeb846b909\`: algebraic perturbation and mass inequalities in Lemma 20.8.1 lines 19–25, displayed Legendre volume/restriction identities lines 99–135, and selected nonregularization conservation and radial/scaling calculations lines 145–179. **Not** a whole §20.8 audit, transitive proof certificate, or investigation of gentle analytic regularization, even where §20.8 cites it.

## POME-PERRON-ASYMMETRIC-TIME-SLOPE-001

**Severity:** low. **Status:** verified conditional deduction (sharpening, **not** a false printed theorem). **Exact target:** Theorem 17.16.7, source \`non-kahler-pluripotential-theory:CADEDF46\`, permanent \`66E38862017F\`, main blob \`dc8dc381257360c94fe1c792499bb1ddf1bf5997\`, lines 110–138; using the local product convexity of Lemma 5.41.1 (source \`909C5329\`, permanent \`ADD743D2224C\`) and Proposition 17.16.6 (source \`071B00B3\`, permanent \`5D2A9C4885B8\`, lines 79–102).

**Statement.** Let \(X\) be a connected compact complex manifold; let \(\theta\) be a smooth real \((1,1)\)-form, **not necessarily closed**; and let \(u_0,u_1\in\mathrm{PSH}(X,\theta)\) be of the same ordinary singularity type. Choose the optimal real constants
\[
m=\sup\{a\in\mathbb R:u_0+a\le u_1\},\qquad
M=\inf\{b\in\mathbb R:u_1\le u_0+b\}.
\]
They are finite and \(m\le M\). If \(u_t^{\rm P}\) is their Perron segment, then for \(0\le s<t\le1\), **on the common finite locus**
\[
\boxed{\quad m(t-s)\le u_t^{\rm P}-u_s^{\rm P}\le M(t-s).\quad} \tag{A}
\]
The corresponding two global inequalities of extended-valued \(\theta\)-psh functions, with constants added rather than differences at poles, are valid everywhere. In particular \(u_t^{\rm P}-mt\) is nondecreasing in \(t\) and \(u_t^{\rm P}-Mt\) is nonincreasing in \(t\) (interpreted as pointwise order for potentials). Moreover
\[
\boxed{\quad
u_0+mt\le u_t^{\rm P}\le u_0+Mt,\qquad
u_1-M(1-t)\le u_t^{\rm P}\le u_1-m(1-t).
\quad} \tag{B}
\]
If \(u_1=u_0+a\) for a constant \(a\), then \(m=M=a\), the Perron segment is \(u_0+at\), and both slope bounds are sharp. In particular one gets monotone Perron segments when \(m\ge0\) or \(M\le0\). Unlike the earlier symmetric \(\max(|m|,|M|)\)-Lipschitz estimate, (A) preserves **orientation and the separate one-sided slope constants**.

**Proof.** By definition \(u_0+m\le u_1\le u_0+M\), and the endpoint inequalities also hold on the common pole set in the extended sense. The affine paths
\[
a_t=u_0+mt,\qquad b_t=u_1-M(1-t)
\]
are subgeodesics on \(X\times S_{(0,1)}\): the \(t\)-affine terms are pluriharmonic in the strip variable and each fixed spatial potential is \(\theta\)-psh. Their endpoint values lie below the prescribed \(u_0,u_1\). They are therefore admissible in Proposition 17.16.6, giving \(u_t^{\rm P}\ge \max(a_t,b_t)\). By the convex chord upper bound in Proposition 17.16.3, \(u_t^{\rm P}\le(1-t)u_0+tu_1\le u_0+Mt\) and \(\le u_1-m(1-t)\), establishing (B).

Fix a point \(x\) outside the common pole locus. By Lemma 5.41.1, \(f(t)=u_t^{\rm P}(x)\) is finite convex in \(t\in(0,1)\). The lower barriers and upper chord in (B) imply \(f(t)\to f(0):=u_0(x)\) as \(t\downarrow0\) and \(f(t)\to f(1):=u_1(x)\) as \(t\uparrow1\). For \(0<s<t<1\), monotonicity of convex secant slopes gives
\[
m\ \le\ \frac{f(s)-f(0)}s\ \le\
\frac{f(t)-f(s)}{t-s}\ \le\
\frac{f(1)-f(t)}{1-t}\ \le\ M.
\]
The first and last inequalities are exactly the two affine barriers in (B). Continuity handles \(s=0\) or \(t=1\). Adding constants and comparing potentials yields the global, well-defined extended-valued inequalities, including poles. For \(u_1=u_0+a\), the two bounds in (B) coincide and give \(u_t^{\rm P}=u_0+at\), proving sharpness and the monotonicity claims.

**Comparison with prior ledger.** \`POME-GEODESIC-TIME-LIPSCHITZ-INTERPOLATION-001\` (2026-11-21, §17.7) already proves the symmetric \(|G_t-G_s|\le C|t-s|\), sharp affine endpoint perturbation, and energy estimate for a related closed-background weak geodesic. These are **not** being relogged. This new item isolates the signed/asymmetric rate \(m\le \partial_t u_t^{\rm P}\le M\) for the **nonclosed Hermitian Perron construction** of §17.16, including monotonicity when the endpoint order is one-sided. It is a direct deduction **conditional on** the printed Perron existence and convexity statements; no general upstream chain is newly certified.

**Suggested optional correction/addition:** a short corollary after Theorem 17.16.7 giving (A)–(B) while retaining the original theorem, conventions, citation provenance, source tags and all valid endpoint cases. **Affected dependents:** bounded-type interpolation and temporal control in §§17.16–17.17; no assertion of new Hölder regularity, energy affineness, or action minimizing property.

## Remaining direct checks and risk boundaries

1. **§5.40, compact envelope arguments.** In Lemma 5.40.1 the normalized \(\ell^1\)-weighted psh sum remains nontrivial by uniform \(L^1\) control, while it has poles on all of a non-pluripolar compact \(K\) under a hypothetical failure of uniform heights; contradiction is valid. The q.e.-to-pointwise perturbation in Lemma 5.40.5 uses the common big strict potential and a global Josefson pole function; its \(\theta\)-lower bound follows from \(s=t/\kappa\), not from a closedness assumption. The hyperplane Green formula (5.40.11), smooth remainder and finite-obstacle bounds (5.40.13–14) have the correct normal disk radius, sign and \(e^{-t/m}\) scale. Proposition 5.40.3 explicitly invokes Theorem 5.32.1, within the **user-excluded regularization programme**: its proof dependency is **deferred-by-user, not certified**. We did not inspect or reconstruct that prerequisite.
2. **§5.41, nonclosed minimum and duality.** Freezing the spatial coefficients incurs an \(O(\eta)\) lower-curvature error, removed after obtaining the local Kiselman infimum; the bounded strip excludes an identically \(-\infty\) infimum because finite convex fiber restrictions have affine minorants on a bounded interval. Endpoint continuation in Lemma 5.41.5, rational-parameter measurability, and the Fubini/pointwise dual reconstruction in Theorem 5.41.9 were directly inspected. The proof quotes a classical **local Kiselman minimum principle from SGPT**; this is a named nonexcluded upstream input, not independently reproved here. The proper treatment of \(-\infty\) slices is essential.
3. **§17.16, nonclosed geometric computations.** The Schur complement of the product coefficient matrix has the factor \(1/4\), yielding the homogeneous Monge–Ampère equation (17.16.10) with \(n\,d\dot u\wedge d^c\dot u\wedge\eta^{n-1}\). The first variation (17.16.13) contains both torsion first-derivative terms and the \(\frac n2 \dot u^2 dd^c\eta^{n-1}\) term; a constant-in-space Perron path is stationary exactly for a Gauduchon endpoint metric. The Hopf basic measure normalization \(n\beta\wedge\pi^*\mathrm{MA}_\kappa\) and \(\int_{\pi^{-1}(y)}\beta=2\) give factor \(2n\), not \(n\) or \(1\). The raw-action Hessian (17.16.26) supports negative Fourier directions while the basic metric retains its CAT(0) property. The radial \(E^2\) threshold in Proposition 17.16.30 is \(a<d/(d+2)\), from integrability of \(T^{2a-d(1-a)-1}\). No newly confirmed printed false theorem is identified.
4. **Upstream genuine external dependency, not automatically a proof gap:** Theorem 17.16.19 explicitly imports the classical closed-Kähler \(L^2\)-completion/CAT(0) theorem and the finite-energy geodesic endpoint theorem, attributed in §25.10. Their precise proof chain is not reproduced in this review. Theorem 17.16.29 also cites closed-Kähler bounded Dirichlet uniqueness. Historical attribution is preserved, but these are true mathematical inputs, not a substitute for proof if the collection's self-contained goal is to be completed outside the excluded programme.
5. **§20.8 boundary:** Classical restricted volume and modification formulas are sampled only. Their proof explicitly invokes gentle analytic regularization in several places. Those dependencies are recorded as **deferred-by-user** and were not investigated, justified by alternative prerequisites, or labeled resolved. Algebraic identities and relative mass equations sampled there do **not** establish the rest of the theorem.

**Accounting:** three complete current integrated mathematical sections (§§5.40, 5.41, 17.16); one selected-only nonexcluded section (§20.8); one new low-severity verified **conditional** deduction; **zero** newly confirmed false printed theorems; **zero** independently certified transitive upstream chains. Prior historical first visits are not inferred from matrix \`LEGACY-UNRECONCILED\`. No tests, builds, CI, source-body, tags, registry, production branch edits, PR merge, or website publication in this audit. All explicitly excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**, not resolved.
