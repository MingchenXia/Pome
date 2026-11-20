# One-mixture mass rigidity and full readings of §§17.6 and 19.9 (2026-11-21)

**Baseline:** current main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. This is an audit of the **integrated reading edition**, not a source-repository edit. User-excluded Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work is **deferred-by-user**; none was revisited or certified.

## Scope and provenance

- **Full direct §17.6**: \`docs/sections/relative-energy-and-perron-segments--singularity-envelopes-at-arbitrary-mass/index.html\`, blob \`addc238e2dc806ff14a69fa8c8e5bdf46da448f2\`, mathematical lines 7–181; Proposition **17.6.1**, source label \`1031B084\`, permanent tag \`DC1056C1A4A1\`, lines 17–126; Definition **17.6.4**, permanent \`0C3B4338E463\`, lines 131–136; Theorem **17.6.5**, source label \`402BEA9A\`, permanent tag \`C6C3A19AAB0D\`, lines 140–181. Checked the normalized tail estimate (17.6.2), comparison/contact inequalities (17.6.3), order of limits in Step 6, and the positive-mass interpolation argument.
- **Full direct §19.9**: \`docs/sections/flags-convex-bodies-and-section-growth/index.html\`, blob \`83557f0e15275253661fe679c75407e6636d497c\`, mathematical lines 7–592. Includes valuation and Gauduchon-degree estimates (lines 17–102); lattice/counting and transcendence degree (110–270); Moishezon/mass and blowup (273–380); curvature-rank bounds, twists and Riemann–Roch (386–548); Hopf flag body (550–592). Theorem **19.9.9**, source \`4EE23942\`, permanent \`CC2BF9294FA3\`, lines 194–233; Proposition **19.9.19**, source \`77A30A69\`, permanent \`C8B2CB1B6819\`, lines 395–427.
- **Selected non-transitive prerequisite checks**: Corollary **13.8.8**, \`docs/sections/non-pluripolar-products--mass-comparison-and-projective-fibers/index.html\`, blob \`dd89e44c511fd6f6bdd164a09a77c1637c42b410\`, lines 249–262, source \`A8BA63307F6C\` (mixed mass monotonicity). Proposition 16.21.2(3), Theorem 16.22.11 and Proposition 16.22.14 were checked at their invocations in §17.6, but **not** independently re-proved end-to-end. Theorem 19.7.20 (semigroup counting), analytic Hirzebruch–Riemann–Roch and Moishezon's projective-modification theorem are **not** certified here. Hironaka principalization/resolution is an expressly permitted external input.

## Finding POME-ENVELOPE-ONE-MIXTURE-MASS-RIGIDITY-001

**Severity:** low. **Status:** verified conditional deduction (a new precise consequence, **not a false printed theorem**). **Affected dependents:** equivalence tests for model envelopes and singularity ceilings from §§16.21–16.22 and §17.6; no source correction required.

**Statement.** Let \(X\) be a connected compact Kähler \(n\)-fold, let \(\theta\) be a smooth closed real \((1,1)\)-form in a big class, and put \(V=V_\theta\). Suppose \(u,v\in\mathrm{PSH}(X,\theta)\) satisfy \(u\preceq v\) (i.e. \(u\le v+O(1)\)). For \(0<t<1\) define
\[
M_u(t)=\int_X\left\langle\theta_{(1-t)u+tV}^{\,n}\right\rangle,\qquad
M_v(t)=\int_X\left\langle\theta_{(1-t)v+tV}^{\,n}\right\rangle.
\]
Then the following are equivalent:

1. \(P_\theta[u]=P_\theta[v]\).
2. \(M_u(t_0)=M_v(t_0)\) for **one** \(t_0\in(0,1)\).
3. \(M_u(t)=M_v(t)\) for **every** \(t\in(0,1)\).
4. For all \(0\le k\le n\),
\[
\int_X\langle\theta_u^k\wedge\theta_V^{n-k}\rangle
=\int_X\langle\theta_v^k\wedge\theta_V^{n-k}\rangle.
\]
In particular, the possibly zero top Monge–Ampère mass at \(t=0\) does not prevent a **single strictly positive perturbation** from detecting equality of singularity envelopes, provided the singularities are ordered.

**Proof.** Denote the two mixed masses in clause 4 by \(a_k(u),a_k(v)\). By Corollary 13.8.8 (applied to \(k\) copies of \(u\preceq v\) and \(n-k\) identical copies of \(V\)),
\(0\le a_k(u)\le a_k(v)<\infty\).
Multilinearity, Proposition 13.2.6, gives
\[
M_v(t)-M_u(t)
=\sum_{k=0}^n {n\choose k}(1-t)^kt^{n-k}
       (a_k(v)-a_k(u)).
\]
All coefficients \({n\choose k}(1-t_0)^kt_0^{n-k}\) are strictly positive at \(0<t_0<1\). Every difference is nonnegative, so equality of the total masses at one \(t_0\) forces **every** \(a_k(v)-a_k(u)=0\). This proves \(2\Rightarrow4\); multilinearity gives \(4\Rightarrow3\Rightarrow2\).

For \(4\Rightarrow1\), shift \(u,v\) by constants so that \(v\le0\), without changing mixed masses, the order relation, or the envelope. The two mixed-mass lists agree and \(u\preceq v\), so \(v\in\mathcal F_u\) as defined in 17.6.4. Theorem 17.6.5 yields \(v\le P_\theta[u]\). Envelope monotonicity gives \(P_\theta[u]\le P_\theta[v]\), while the reverse inequality follows from \(P_\theta[v]\le P_\theta[P_\theta[u]]=P_\theta[u]\). Finally, \(1\Rightarrow4\) follows from mixed-mass preservation under replacement of each argument by its singularity envelope (Proposition 16.21.2(3)), using \(P_\theta[V]=V\). This proves the equivalences, **conditional on the cited integrated prerequisite theorems**.

**Why the ordering hypothesis is necessary.** On \(\mathbb P^1\), normalize \(\int\omega_{\mathrm{FS}}=1\), take distinct \(p,q\), and \(0<a<1\). Let
\(u_p=a\log(|\ell_p(Z)|^2/\|Z\|^2)\), with \(\ell_p\) a unit linear form vanishing at \(p\), and similarly \(u_q\). With \(V=0\),
\(\omega_{\mathrm{FS}}+dd^cu_p=(1-a)\omega_{\mathrm{FS}}+a[p]\), so its non-pluripolar mass is \(1-a\); the same holds for \(q\). For every \(t\in(0,1)\), both perturbed masses equal \(1-a(1-t)\), but \(P_\omega[u_p]\) has a pole at \(p\), whereas \(P_\omega[u_q]\ge u_q\) is finite at \(p\). Thus the envelopes differ. The example prevents extending the criterion to unordered pairs of potentials.

**Proposed addition:** optional corollary after Theorem 17.6.5 stating the one-mixture equivalence with the explicit order hypothesis. No change to the original theorem, proof, tag or source is authorized by this audit.

## Finding POME-OKOUNKOV-MOISHEZON-EXTERNAL-INPUT-001

**Severity:** low documentation/dependency risk. **Status:** external dependency (not a demonstrated false theorem or a demonstrated proof gap in the mathematical claim). §19.9 lines 273–313 and 365–380 use the **Moishezon theorem** that a compact complex \(n\)-fold with \(n\) algebraically independent meromorphic functions has a smooth projective modification. The result is invoked to deduce bounded mass via Lemma 19.9.12, specifically in Theorem **19.9.13** (permanent \`0F8B7237A1BA\`, lines 303–313) and Corollary **19.9.17** (permanent \`EECB2B1DF1A4\`, lines 365–380). §25.9 supplies historical/source attribution, which should be retained; that attribution alone does not certify an internal proof. **Proposed action:** retain the named theorem and its attribution, mark it as a genuine external analytic/algebraic input until a separate internal proof is audited; do not mislabel Hironaka's permitted resolution theorem as proving the Moishezon projective-modification statement. A full replacement proof is **not supplied** in this run.

## Other mathematical checks / limits

- The §17.6 normalized tail \(r(A)\to0\) has finitely many non-pluripolar reference measures; the comparison estimate divides by \(m_\varepsilon>0\) **before** the \(A\to\infty\), \(B\to\infty\) limits. This avoids an unjustified uniform positive-mass lower bound as \(\varepsilon\downarrow0\). No new confirmed printed error found in §17.6.
- In §19.9, the degree bound permits negative Gauduchon degrees through absolute values in \(C_i\) (19.9.4), the intrinsic lattice/degree period is essential for lower-dimensional semigroups (19.9.9), and the curvature-rank proof uses a section multiplier vanishing on the *critical-value image* (19.9.19). The Hopf body has ambient \(n\)-volume zero but intrinsic \((n-1)\)-volume \(k^{n-1}/(n-1)!\) for \(k>0\); none of these is re-counted as a new error or standalone novelty.
- No complete transitive verification of the comparison theorem, the semigroup counting theorem, global projective modification, analytic HRR, or other upstream dependencies; no claim about tests, builds, CI or formal verification.
