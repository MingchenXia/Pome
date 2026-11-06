# Independent arbitrary-net Legendre minimax check (§22.1)

Date: 2026-11-06. Finding: **POME-NA-ORDERED-NET-LEGENDRE-MINIMAX-001**. Severity: **low**. Status: **verified repair (final proof step only)**; the printed proposition is not refuted. Production main reviewed: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.

## Source-pinned scope

1. Integrated file: docs/sections/non-archimedean-pluripotential-theory/index.html, main blob **8448d710690ebe1cc28040f9611d05c9d008a961**. Proposition 22.1.109 at physical lines **1618–1623**, proof **1625–1674**, particularly Eq. (22.1.110), lines **1636–1639**, the valuation limit **1641–1656**, the varying-endpoint handling **1659–1671**, and the convex-duality invocation **1673**. Original source key and tag: **sgpt:0D711EA7**, permanent **9F673331DE01**; Eq. (22.1.110) **sgpt:67271763**, permanent **115AEB4414B4**.
2. Same file, Definition 22.1.41 and guard (22.1.42), lines **677–689**, source/permanent **sgpt:0A4E21E4 / 65E2E07550F1** and **sgpt:CF7B00D2 / 827FE14EA1A0**. Theorem 22.1.111, lines **1678–1722**, **sgpt:0558A92C / 9B811DBD89E3**, is a downstream dependent, not certified by this work.
3. docs/sections/test-curves--the-notion-of-test-curves/index.html, blob **6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7**, Definition 17.12.1 lines **10–39**, source/permanent **sgpt:ECCF19D5 / C8399F09D86D**. Its decreasing-in-parameter clause has permanent tag **D665BBFA648A**.
4. docs/sections/convex-functions-and-convex-bodies/index.html, blob **2a123a863642a5a75caa173f0f73aff439a02ea4**, Proposition 21.11.36 lines **380–389**, **sgpt:24FD3947 / 7A76E56311F5**.

At line 1673, the integrated proof uses the arbitrary-family convex conjugation identity from Proposition 21.11.36. The cited formula for the conjugate of a supremum contains a **closure** of an infimum of conjugates, while the proof needs its value at a particular slope. The text also does not explicitly bound the possible contribution from the varying upper endpoints of individual test curves. The following direct argument supplies both missing justifications without claiming that the cited convex result or the printed theorem is false.

## Finite-grid minimax lemma, valid for every directed set

Let I be an arbitrary nonempty directed set, let a be a finite real number, and let h_i:(-infinity,a) -> [-infinity,C], i in I, be functions such that

- h_j(t) <= h_i(t) for j >= i;
- h_i(t') <= h_i(t) whenever t < t' < a.

Then, as an identity of extended real numbers,
\[
\boxed{\quad \sup_{t<a}\bigl(\inf_i h_i(t)+t\bigr)
=\inf_i\sup_{t<a}\bigl(h_i(t)+t\bigr).\quad} \tag{A}
\]
There is **no** requirement of continuity or concavity of h_i, a sequential cofinal subset of I, or compactness of the index set.

**Proof.** Write H_i(t)=h_i(t)+t, S=sup_{t<a} inf_i H_i(t), T=inf_i sup_{t<a} H_i(t). Clearly S<=T. Suppose S is finite. Fix epsilon>0 and choose R<a with C+R<=S+epsilon. Partition the ordinary compact interval [R,a] into finitely many subintervals [t_j,t_{j+1}] of length less than epsilon, with t_m=a. At every left endpoint t_j, j<m, select i_j such that H_{i_j}(t_j)<=S+epsilon. Since only finitely many indices occur, directedness gives k dominating all i_j. For any t in [t_j,t_{j+1}),
\[
H_k(t) \le h_{i_j}(t_j)+t_{j+1}
=H_{i_j}(t_j)+(t_{j+1}-t_j)\le S+2\epsilon.
\]
For t<R, the common upper bound gives H_k(t)<=C+t<=S+epsilon. Therefore T<=sup_{t<a} H_k(t)<=S+2epsilon, and letting epsilon decrease to zero proves T<=S. If S=-infinity, use any arbitrary real B in place of S+epsilon, choose R with C+R<B, and select indices with H_{i_j}(t_j)<B; the same argument yields T<=B+epsilon for *every* B, so T=-infinity. S cannot be +infinity since S<=C+a. This proves (A). No interchange of an arbitrary net with a sequential limit has occurred. QED.

## A genuinely necessary endpoint check

For the actual family set a_i=(Gamma_i)_max and a=inf_i a_i > -infinity as required in (22.1.42); each a_i is finite. Let h_i be defined until a_i and nonincreasing in the curve parameter. Put
\[
A_i=\sup_{t<a}(h_i(t)+t),\qquad
B_i=\sup_{t<a_i}(h_i(t)+t).
\]
For a<=t<a_i and any s<a, parameter monotonicity gives
\[
h_i(t)+t\le h_i(s)+s+(t-s)\le A_i+(t-s).
\]
Sending s upward to a shows the **non-subtractive** extended-real estimate
\[
A_i\le B_i\le A_i+(a_i-a). \tag{B}
\]
This is meaningful even if A_i=-infinity. Given epsilon>0, choose i_0 with a_{i_0}<a+epsilon (by the definition of infimum). Since the endpoints decrease along the directed set, on the cofinal upper cone i>=i_0 one has a_i-a<epsilon. Taking infima in (B) and sending epsilon down to zero proves
\[
\inf_i B_i=\inf_i A_i. \tag{C}
\]
Combining (A) and (C) proves exactly the last minimax interchange in the printed equation (22.1.110), even when the individual right-hand supremums have different cutoffs.

### Counterexample to an illegitimate generalization

The *direction of parameter monotonicity* cannot simply be dropped. For t<0 define h_j(t)=jt, j=1,2,... . These functions are affine (hence concave), uniformly bounded above by zero, have a common finite upper endpoint, and decrease in j; however they **increase** in t. Directly,
\[
\inf_j\sup_{t<0}(h_j(t)+t)=0,\qquad
\sup_{t<0}\bigl(\inf_jh_j(t)+t\bigr)=-\infty.
\]
This does not contradict the printed Proposition 22.1.109: the functions are not admissible test curves by Definition 17.12.1.

## Application and precise limitation

For v in X^div set h_i(t)=(Gamma_{i,t})^An(v). Test-curve monotonicity (Definition 17.12.1) and order of the decreasing net make h_i nonincreasing in both variables. Divisorial valuations of the normalized model potentials (sup_X Gamma_{i,t}=0) are nonnegative, hence their negative analytifications h_i have the common upper bound C=0. One could instead bound the cofinal upper cone by a fixed initial test curve. Formulas (A)–(C) consequently justify the final exchange of the infimum over I and the Legendre supremum over t, including arbitrary directed I and all finite endpoints a_i.

**Not proved in this note:** the previous identity
\[
(\inf_i\Gamma_{i,t})^{\mathrm{An}}(v)
=\inf_i(\Gamma_{i,t})^{\mathrm{An}}(v)
\]
in lines 1641–1656. The integrated argument obtains it from 17.15.41, 16.4.4, 16.9.14 and 16.9.55 through mass and d_S convergence. Those are **uncertified dependencies here**. The entire Proposition 22.1.109, Theorem 22.1.111, and the later trace theorem 22.1.113 are **not** newly certified. A false mathematical theorem has not been identified.

**Proposed patch (not applied):** add the finite-grid proof (A) and the variable-endpoint bound (B)–(C) as an explicit justification after (22.1.110); retain the original proposition, all historical attribution, tags, conventions and references. No source/body/registry/canonicalization or published-file edit was made.

**Coverage accounting:** first new proof-level verification of this specific §22.1.109 exchange; context-only reads of §22.1.41, §17.12.1, §21.11.36 and §22.1.111. The actual table of contents still has **25 chapters / 747 numbered sections / zero complete mathematical-section certifications**. All previous findings retain their statuses. The user-excluded Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user**. No builds, tests, CI, formal verification or website publication were performed.
