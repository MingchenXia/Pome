# Arbitrarily slow convergence for one fixed L1 heat test (2026-11-15)

**New stable finding:** \`POME-HEAT-ARBITRARILY-SLOW-FIXED-L1-001\` (**low / verified conditional deduction**; original printed lemmas correct).  
**Main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Main integrated file:** \`docs/sections/heat-kernels-on-compact-manifolds/index.html\`, blob \`c59a1b3fab9433f1aae95db99adb4821857b5d8d\`.  
**Section:** 3.10, source \`transcendental-positive-cones:FD9C3E46\`, permanent tag \`B8A97FFD89FE\`.  
**Directly read:** Lemma 3.10.1, source \`transcendental-positive-cones:327DDB8B\`, permanent \`126365F8EBD6\`, physical lines 11–13 and proof 19–79 (supporting heat Gaussian normalization); Lemma 3.10.5, source \`transcendental-positive-cones:DD00B1CA\`, permanent \`56A174D59425\`, physical lines 85–105 (critical Frostman hypothesis, fixed-$L^1$ limit and truncation proof).

## Relation to earlier findings and correction to this audit increment

**No new $L^p$ duality or sharp $L^p$ operator-norm result is claimed.** The exact $1<p<\infty$ operator-norm exponent, its sharp flat-torus leading coefficient, the fixed-$L^p$ little-$o$ improvement, and their $p=1,\infty$ boundary cases had already been proved in **\`POME-HEAT-CRITICAL-LP-DUAL-RATE-001\`** ([2026-11-08 report](2026-11-08-critical-heat-lp-dual-sharp-rate.md)). The $p=1$ failure of uniform norm convergence and explicit power/logarithmic *individual* $L^1$ tests had already been proved in the [2026-11-06 report](2026-11-06-flat-torus-codimension-two-heat-endpoint.md). A preliminary 2026-11-15 note inadvertently described part of this established $L^p$ work as new; the present corrected report removes that novelty claim. The genuinely new result below is a uniform diagonal construction beating **every** prescribed positive convergence modulus with **one fixed nonnegative normalized $L^1$ test**.

## Precise new assertion

Let $X=\mathbb R^2/\mathbb Z^2$ be the unit flat two-torus with Euclidean area $dV$, let $o=[0]$, and put $\rho=\delta_o$. It satisfies the exact codimension-two growth hypothesis of Lemma 3.10.5 with $m=2$ and $A=1$:
\[
 \rho(B_r(x))\le1=A r^{m-2}\quad(x\in X,\ r>0).
\]
Define, for $F\ge0$,
\[
 I_t(F)=t\int_X(h_t\rho)F\,dV=t\int_Xh_t(o,y)F(y)\,dy.
\]
The printed Lemma 3.10.5 proves $I_t(F)\to0$ for *each fixed* $F\in L^1_+(X)$. Its qualitative convergence admits **no positive rate modulus valid for all fixed $L^1$ tests**, even if a constant depending on the individual test is allowed:

> For every function $\omega:(0,1]\to(0,\infty)$ satisfying $\omega(t)\to0$ as $t\downarrow0$, there exist one *fixed* $F\in L^1_+(X)$ with $\int_XF\,dV=1$ and a sequence $t_j\downarrow0$ such that
> \[
> \boxed{\lim_{j\to\infty}\frac{I_{t_j}(F)}{\omega(t_j)}=+\infty.}\tag{1}
> \]
> This does not contradict $I_t(F)\to0$, and is stronger than the absence of a universal **polynomial** rate shown by particular log-singular profiles.

## Complete elementary proof

The heat kernel on the flat torus is the periodized Euclidean Gaussian
\[
 h_t(o,y)=\frac1{4\pi t}\sum_{k\in\mathbb Z^2}
 \exp\left(-\frac{|y+k|^2}{4t}\right).\tag{2}
\]
The normally convergent series solves the heat equation, is nonnegative with torus integral one, and has delta initial data; uniqueness follows by Fourier coefficients. In particular, for any $t<1/64$ and any $y$ represented by $|y|\le\sqrt t$ in the central fundamental square,
\[
 t h_t(o,y)\ge\frac1{4\pi}
 \exp\left(-\frac{|y|^2}{4t}\right)
 \ge c_0:=\frac{e^{-1/4}}{4\pi}>0.\tag{3}
\]

Fix any positive $\omega(t)\to0$, with no monotonicity or continuity assumptions. Inductively choose strictly decreasing $t_j\in(0,1/64)$ so that, with $r_j=\sqrt{t_j}$,
\[
 r_{j+1}<r_j/4,\qquad \omega(t_j)\le16^{-j}/j^2.
\]
This is possible solely because $\omega(t)\to0$. The Euclidean annuli
\[
 A_j=\{y\in X:r_j/2\le |y|\le r_j\}
\]
are nonempty, pairwise disjoint and contained in a single torus coordinate chart. Set
\[
 a_j=j\omega(t_j),\qquad
 F_j=\frac{a_j}{|A_j|}\mathbf1_{A_j}.
\]
The mass series is strictly less than one:
\[
 0<\sum_j a_j\le \sum_{j\ge1}\frac{16^{-j}}j<1.
\]
Choose any $G\in C^\infty(X)$ nonnegative and supported away from $o$, normalized so that
$\int_XG\,dV=1-\sum_j a_j$. Define
\[
 F=G+\sum_{j\ge1}F_j .
\]
Then $F\ge0$, $F$ is a **single fixed** measurable function, and monotone convergence gives $\|F\|_1=1$. Neither $G$ nor any $F_j$ varies with the heat time once $F$ is constructed.

For $t=t_j$, every $y\in A_j$ has $|y|\le r_j=\sqrt{t_j}$, so by (3) and positivity,
\[
 I_{t_j}(F)
 \ge\int_{A_j}t_jh_{t_j}(o,y)F(y)\,dy
 \ge c_0\int_{A_j}F_j\,dy
 =c_0 j\,\omega(t_j).
\]
Thus $I_{t_j}(F)/\omega(t_j)\ge c_0j\to\infty$, proving (1). Separately, the printed Lemma 3.10.5 still guarantees $I_t(F)\to0$ for this fixed $F$. The construction requires only positive unit-$L^1$ mass and a critical-growth heat test; no extra regularity is claimed.

## Classification, dependencies, action and coverage

**Severity/status:** low / **verified conditional deduction**. The printed Lemmas 3.10.1 and 3.10.5 are correct. The new assertion is fully justified by the elementary Gaussian (2)–(3) and disjoint-annulus construction; the broader compact-manifold heat/Nash/Davies construction remains an uncertified internal dependency, not a detected proof gap.

**Proposed optional clarification, not applied:** after Lemma 3.10.5, state that fixed-test $L^1$ convergence can be arbitrarily slow even for nonnegative normalized $F$, while quantitative uniform $L^p$ results and their sharp constants already belong to \`POME-HEAT-CRITICAL-LP-DUAL-RATE-001\`. This matters only to dependents actually requiring a convergence rate; no uninspected theorem is declared false, and no new canonical duplicate is created.

**Actual coverage:** reread the displayed Lemma 3.10.5 and its fixed-$F$ truncation step and supporting §3.10.1 Gaussian convention. §3.10 had prior selected proof-level coverage: **0 new first-visited sections and 0 entire-section certifications**; current ToC remains **25 chapters / 747 numbered sections**. No build, test suite, CI, formal verification or website publication was performed. Source bodies, proof registries, canonicalization, permanent tags and \`main\` remain untouched. The excluded Demailly regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss proof-completion programme remain **deferred-by-user**, not resolved or certified.
