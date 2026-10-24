# 2026-10-25 — Stein open unions, psh-exhaustion obstruction, and local homogeneous replacement

## Immutable review scope

- Reviewed main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**; audit branch head on entry: **e48a94aa1a6fcde1518d433c1ab504904e687c5c**.
- Direct integrated mathematical passages (no source-manuscript editing): §§9.26.1–2; 9.27.1; 9.32.6/8 as a *dependency*; §§15.7.1–2; §§15.8.4–6 and **only the post-continuity contact argument** in 15.8.1. In §15.8.1, the regularization-based proof of continuity and its analytic barrier preparation were **not audited**, nor were §§15.5–6.
- Findings below concern mathematical content and proof dependencies, **not** whole-section certification. Historical source attribution is retained. All user-excluded Demailly approximation / regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains *deferred-by-user*.

## POME-STEIN-UNION-NO-PSH-EXHAUST-001

**Severity:** low. **Status:** verified conditional deduction (in fact proved directly from the displayed example). **Not a false theorem.**

**Primary source and stable anchors:** Example **9.27.1**, source label **demailly-complex-geometry-BBFF78A8**, permanent tag **F00C66A8D202**, integrated
[docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html](../../docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html), main blob **26b2e856fc24b04616b0840caec5c688cc045ffa**, physical HTML lines **8–12, 32–46**. The example is a nonholomorphically-convex increasing union of smooth connected affine Stein surfaces.

**Strengthened conclusion.** This explicit open union admits **no plurisubharmonic exhaustion, even one that is merely upper semicontinuous and extended-real-valued**. Thus it is not even weakly pseudoconvex in the exhaustion sense of §9.26, a stronger obstruction than failure of holomorphic convexity.

**Complete proof.** In the example, let
\[
X_\nu=\{(z,w,t)\in\mathbb C^3:wt=p_\nu(z)\},\qquad
p_\nu(z)=\prod_{j=1}^{\nu}(z-1/j),
\]
with inclusions \(j_\nu(z,w,t)=(z,w,t(z-1/(\nu+1)))\), and let \(X=\bigcup X_\nu\).
The holomorphic map \(\pi=(z,w):X\to\mathbb C^2\) has image
\[
\pi(X)=(\mathbb C\times\mathbb C^*)\cup\{(1/j,0):j\geq1\},
\quad(0,0)\notin\pi(X).
\]
The compact set
\[
K=\pi^{-1}\{(z,w):|z|\leq1,\ |w|=1\}
\]
is compact because \(\pi\) is a biholomorphism over \(w\ne0\). For every \(\nu\), the analytic disc
\[
d_\nu:\overline{\Delta}\to X_\nu,\qquad d_\nu(\zeta)=(1/\nu,\zeta,0)
\]
has boundary in \(K\). Take **any** psh function \(\psi\) on \(X\). Since \(\psi\) is upper semicontinuous on compact \(K\), \(M=\sup_K\psi<+\infty\) (possibly \(M=-\infty\)). The subharmonic maximum principle applied to \(\psi\circ d_\nu\) gives
\[
\psi(d_\nu(\zeta))\leq M \qquad (|\zeta|<1,\ \nu\geq1).
\]
Choose any real \(c>M\) (any \(c\) if \(M=-\infty\)). Then all
\[
x_\nu=d_\nu(1/\nu)=(1/\nu,1/\nu,0)
\]
belong to \(\{\psi<c\}\). However \(\pi(x_\nu)\to(0,0)\notin\pi(X)\). If \(\{x_\nu\}\) were contained in a compact subset \(C\subset X\), the compact set \(\pi(C)\subset\mathbb C^2\) would contain \((0,0)\), impossible. Thus \(\{\psi<c\}\) is **not** relatively compact, and \(\psi\) cannot be an exhaustion. No global strictness or regularity of \(\psi\) was assumed.

**Proposed addition / affected dependents:** an optional corollary beside Example 9.27.1 distinguishing *failure of smooth/continuous psh exhaustions* from merely failure of Steinness; the natural dependent is the definition of weak pseudoconvexity preceding Proposition 9.26.2. No change to the example or its permanent tags is warranted.

## POME-HOLOCONV-PSH-EXHAUST-BRIDGE-001

**Severity:** low. **Status:** verified repair / explicit acyclic proof bridge **proposed only**, not an integrated source patch or a new false-theorem allegation.

**Primary anchors:** Theorem **9.26.1**, source label **demailly-complex-geometry-57C45FF9**, tag **C1041DBBD4EC**, main blob **c04701d0358d43a3a3f1aed61e7cdd2a48305417**, [§9.26 integrated file](../../docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html), lines **14–32**, especially line **32** invoking "plurisubharmonic exhaustions from holomorphic convexity." An actual internal version exists: Proposition **9.32.8**, source label **demailly-complex-geometry-4C2DB7E3**, tag **A13AE3DAF423**, main blob **169e9d3bc872e9fd89d5135e69204e33fccd3783**, [§9.32](../../docs/sections/separation-strict-exhaustions-and-coverings--convexity-and-stein-spaces/index.html), lines **127–145**. It proves the broader complex-space case using an intrinsic coherent-section-topology lemma. This is **not** a mathematical duplicate to be deleted: the earlier result is for manifolds with local-separation assumptions; Proposition 9.32.8 includes potentially nonreduced complex spaces.

**Self-contained proof for the precise manifold dependency.** Let \(X\) be Hausdorff, second countable, locally compact and holomorphically convex. Pick compact holomorphically convex hulls \(K_j\) of an increasing sequence of compact neighborhoods, inductively arranged so that \(K_{j-1}\subset\operatorname{int}K_j\) and \(\bigcup K_j=X\). This is possible because each hull is compact and taking the hull of a sufficiently large compact neighborhood preserves containment.

For \(j\geq4\) put \(A_j=K_j\setminus\operatorname{int}K_{j-1}\). It is compact and disjoint from \(K_{j-2}\). By holomorphic convexity of \(K_{j-2}\), every \(x\in A_j\) admits a global holomorphic function \(f_x\), rescaled so that
\[
\sup_{K_{j-2}}|f_x|<1<|f_x(x)|.
\]
Compactness of \(A_j\) gives finitely many \(f_{j,l}\), a common \(q_j<1\) bounding all of them on \(K_{j-2}\), and \(b_j>1\) such that \(\max_l|f_{j,l}|\geq b_j\) on \(A_j\). Empty \(A_j\) contributes an empty block.

Choose \(N_j\) large and set \(v_j=\sum_l|f_{j,l}|^{2N_j}\). Since \(b_j>1\), one can ensure \(v_j\geq j\) throughout \(A_j\). Simultaneously, because \(|f_{j,l}|\leq q_j<1\) on the neighborhood \(K_{j-2}\supset\operatorname{int}K_{j-2}\supset K_{j-3}\), the elementary Cauchy estimates on finitely many coordinate patches show that all derivatives of \(v_j\) of order \(\leq j\) are \(O(N_j^Cq_j^{2N_j-C})\) on \(K_{j-3}\). Increasing \(N_j\) makes their chosen seminorms at most \(2^{-j}\). The series
\[
\rho=\sum_{j\geq4}v_j
\]
therefore converges in \(C^\infty\) on every compact subset of \(X\), is nonnegative, and is psh because every summand is a sum of squared holomorphic moduli. If \(x\notin K_M\), let \(j>M\) be the first index with \(x\in K_j\). Then \(x\in A_j\) and \(\rho(x)\geq v_j(x)\geq j>M\). Thus every finite closed sublevel is contained in a compact \(K_M\), making \(\rho\) a smooth psh exhaustion.

This replaces the otherwise unnamed input at §9.26.1 by a proof using **only holomorphic convexity, compactness and elementary holomorphic Cauchy estimates**, with no potential dependency on the later Stein criterion. The integrated Proposition 9.32.8 remains a valid, more general internal alternative; its nonreduced/coherent-extension proof was **not** recertified here.

**Proposal:** explicitly cite Proposition 9.32.8 in the §9.26.1 dependency map, or add this elementary manifold proof as an internal argument if chronological acyclicity is desired. No source/canonicalization changes made.

## POME-HOM-DIRICHLET-SMOOTH-EXT-001

**Severity:** medium. **Status:** external dependency, **not** a confirmed false statement and **not** an established gap in the *subsequent* limiting argument.

**Primary anchors:** Lemma **15.7.1**, source **non-kahler-pluripotential-theory-6A868117**, tag **5C54B7FA3A8B**, [§15.7](../../docs/sections/equations-with-prescribed-singularities--homogeneous-replacement-on-a-coordinate-ball/index.html) main blob **a9db59d6db0717cd2da92f3c0120b494fa4f731e**, HTML lines **14–28**; Theorem **15.7.2**, label **non-kahler-pluripotential-theory-95D653E5**, tag **B0FDBEE3B071**, same blob lines **32–89**. The lemma invokes the **Guan–Li smooth strictly positive Hermitian Monge–Ampère Dirichlet existence theorem** in complex dimension \(n\geq2\), allowing a smooth real \((1,1)\)-background \(\theta\) **not assumed closed**, arbitrary smooth boundary values, and a strict smooth subsolution.

**Exact dependency boundary:** The current internal Theorem **7.9.2**, source **klimek-pluripotential-theory-69935D4D**, tag **A092925717E1**, [§7.9](../../docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html), main blob **ff1d5dfff1913156b45875eabf921f60af553b99**, HTML line **41 onward**, gives unique **continuous** solutions, locally \(C^{1,1}\) for \(C^2\) data, in the **closed \(dd^c u\)** background. It does **not** directly give the asserted globally smooth solution for a general non-\(d\)-closed \(\theta\). Merely replacing "Guan–Li" by "7.9.2" would therefore silently weaken hypotheses and regularity, and is not a valid proof replacement.

**Selected independent checks of Theorem 15.7.2:** Its Step 1 uses two boundary barriers; Step 2 compares shifted positive determinant matrices after adding \(C|h|\beta\), with the correct sign; Step 3 sends \(\varepsilon\downarrow0\), using a uniform Lipschitz bound and local Bedford–Taylor uniform-convergence continuity; Step 4 gives supnorm contraction for continuous boundary values; Step 5 correctly uses the *upper-test* characterization of strict \(\theta\)-psh \(p+\delta(|z|^2-R^2)\) and \(\varepsilon<\delta^n\) to prove domination. **These deductions are conditional** on the quoted smooth Dirichlet existence and the internal local bounded-product/test-function lemmas. No counterexample to the homogeneous replacement was found.

**Proposed resolution and affected dependents:** retain an explicit, accurately scoped Guan–Li existence input until a fully internal proof for the nonclosed smooth-background Dirichlet problem is available; alternatively develop a genuinely independent Perron/viscosity proof without assuming a globally smooth solution. The major dependent is §15.8.1's **contact-support** half, plus §§15.8.4–6. We checked the support-vanishing steps of §§15.8.4–6 using fixed quasi-continuous weights and signed-product truncations, but we did not independently certify their upstream measure-continuity lemmas. In §15.8.1 its regularization-derived *continuity* half and all corresponding dependencies are **deferred-by-user**; only the subsequent local homogeneous replacement contact argument was read. Do not confuse the external smooth Dirichlet dependency with that deliberately excluded programme.

## Verified/non-verified scope

- §9.26: direct proof inspection of Theorem 9.26.1 and Proposition 9.26.2, including regularized-max branch deletion, locally convergent sum, product/submanifold hull inequalities and psh sublevel composition. The later §9.32.8 was matched by **content**, not theorem number.
- §9.27: direct full proof inspection of Example 9.27.1; new psh-exhaustion obstruction above.
- §15.7: selected complete statement and all five proof steps of Theorem 15.7.2; genuine smooth-PDE external input recorded rather than relabeled resolved.
- §15.8: *only* contact, lower-semicontinuous and quasi-continuous obstacle monotonicity/truncation arguments selected. The continuity subproof and all dedicated Demailly regularization material were left untouched/deferred.
- No full chapter certified. No tests, complete build, CI, website publication, formal verification, source/registry/tag changes, or merge performed. Audit findings are proposals on the review branch only.
