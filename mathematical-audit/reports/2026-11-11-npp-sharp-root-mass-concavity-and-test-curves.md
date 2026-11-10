# Sharp non-pluripolar mass-root concavity and test-curve profiles

**Date:** 2026-11-11. **Stable ID:** POME-NPP-MASS-ROOT-POWER-SHARPNESS-001.  
**Severity:** low. **Status:** verified conditional deduction, NOT complete certification of the mixed-mass input or a repair to a false theorem.  
**Pinned main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Main was freshly read with AGENTS.md and documentation/proof-expansions.md; audit README, LATEST and existing section matrix read on review/mathematical-audit. No user-excluded regularization work is covered.

## Inspected integrated text and stable locators

- Theorem 13.13.5, source label **sgpt:5DEDC013**, permanent **7F7BE8292E76**, lines **50–59** in **docs/sections/non-pluripolar-products--properties-of-non-pluripolar-products/index.html**, blob **4ace6181d3767e6d5ac3a681c36e392e33b717a2**. It prints both concavity of log mass and the mixed non-pluripolar inequality
  \[
    \int_X\langle T_1\wedge\cdots\wedge T_n\rangle
       \geq \prod_{j=1}^n
         \left(\int_X\langle T_j^n\rangle\right)^{1/n}
  \]
  for positive closed (1,1)-currents on a connected compact Kähler manifold. **DDNL19log** is explicitly cited for its proof: an *actual external mathematical input*, not independently verified here; preserve historical attribution.
- Proposition 13.11.4, source **sgpt:B86D7001**, permanent **9E81D36B1290**, lines **33–97**, especially pluripolar-null clause lines **79–80** and multilinearity clause lines **85–93**, **docs/sections/non-pluripolar-products--the-non-pluripolar-products/index.html**, blob **054a7661c855824b86eb749e211fc3da88a599de**.
- Theorem 13.13.11, source **sgpt:00CC32E0**, permanent **0E5F6133B048**, lines **107–117**; and Corollary 13.13.12, source **sgpt:CDCC4217**, permanent **37623491DEDC**, lines **123–165**, in the same §13.13 integrated file and blob.
- Definition 17.12.1, source **sgpt:ECCF19D5**, permanent **C8399F09D86D**, lines **11–35**; Lemma 17.12.6, source **sgpt:95575DAE**, permanent **348ACDBCB24E**, lines **81–128**; Proposition 17.12.9, source **sgpt:37ECD68D**, permanent **B7CD1B90CFDA**, lines **133–144**, **docs/sections/test-curves--the-notion-of-test-curves/index.html**, blob **6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7**.
- Proposition 20.7.3 smooth Poincaré–Lelong normalization, source **demailly-complex-geometry:00A05C89** (integrated source suffix **00A05C89**), permanent **ACC6D09EDDD9**, lines **13–23**, **docs/sections/meromorphic-sections-and-divisor-classes/index.html**, blob **d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8**. Only the smooth-manifold formula is used; separately recorded non-Cartier assertions on singular reduced spaces play no role.

## Conditional Theorem A: root mass is concave

Let \(X\) be connected compact Kähler, \(\dim_\mathbb C X=n\geq1\), and let \(\theta\) be a smooth closed real (1,1)-form. For \(u_0,u_1\in\operatorname{PSH}(X,\theta)\), put
\[
  T_j=\theta+dd^cu_j,\qquad
  M(u)=\int_X\langle(\theta+dd^cu)^n\rangle,\qquad
  u_t=(1-t)u_0+tu_1.
\]
Then for all \(0\leq t\leq1\), including **zero-mass endpoints**,
\[
  \boxed{M(u_t)^{1/n}\geq
       (1-t)M(u_0)^{1/n}+tM(u_1)^{1/n}.}\tag{A}
\]
More generally \(M^\alpha\) is concave along these segments for every \(0<\alpha\leq1/n\).

**Complete finite derivation relative to the explicitly named inputs.**
Multilinearity (Proposition 13.11.4(6)) gives
\[
 M(u_t)=\sum_{k=0}^{n}\binom nk(1-t)^{n-k}t^k
     \int_X\langle T_0^{\,n-k}\wedge T_1^{\,k}\rangle .
\]
The mixed inequality printed in Theorem 13.13.5 gives, for \(0<k<n\),
\[
 \int_X\langle T_0^{\,n-k}\wedge T_1^{\,k}\rangle
  \geq M(u_0)^{(n-k)/n}M(u_1)^{k/n};
\]
at \(k=0,n\), use the equality directly, so no \(0^0\) issue appears. All summands are nonnegative. By the binomial theorem,
\[
 M(u_t)\geq\left[(1-t)M(u_0)^{1/n}
                     +tM(u_1)^{1/n}\right]^n,
\]
and taking the nonnegative root proves (A). Composition with the increasing concave function \(s\mapsto s^{n\alpha}\) proves the power range. This argument involves **no limiting operation**, Demailly approximation, Bergman construction, or hidden change of topology.

The published **logarithmic** concavity alone would NOT imply (A); the distinct mixed-mass inequality is essential. This is a strengthening of the source statement under its actual hypotheses, not a correction.

## Exact sharpness for every n, without zero endpoint masses

On \(X=\mathbb P^n\), use \(\omega=\omega_{\rm FS}\) normalized by \(\int_X\omega^n=1\). Choose a hyperplane \(D=(s=0)\) and a smooth metric \(h\) on \(\mathcal O(1)\) with \(c_1(\mathcal O(1),h)=\omega\). Set \(v=\log|s|_h^2\) and \(v_a=a\,v\), \(0\leq a\leq1\). With the integrated normalization \(dd^c=i/(2\pi)\partial\bar\partial\), Poincaré–Lelong gives
\[
 \omega+dd^cv_a=(1-a)\omega+a[D]\geq0.
\]
Outside the pluripolar hypersurface \(D\) the current equals \((1-a)\omega\), and the non-pluripolar top power gives no mass to \(D\). Consequently,
\[
 \boxed{\langle(\omega+dd^cv_a)^n\rangle=(1-a)^n\omega^n,\qquad
         M(v_a)=(1-a)^n.}\tag{B}
\]
No unwarranted full exterior power of the singular divisor current is taken. The affine segment in \(v_a\) satisfies **equality** in (A). For any \(\alpha>1/n\), on \(0\leq a\leq1/2\) *all masses remain positive*, but
\[
 \frac{d^2}{da^2}M(v_a)^\alpha
    =n\alpha(n\alpha-1)(1-a)^{n\alpha-2}>0.
\]
Thus \(M^\alpha\) is strictly convex on a legitimate positive-mass PSH segment and cannot be universally concave. The exponent \(1/n\) is optimal. This is not the previously audited bounded-Dirichlet **solution-density root concavity** theorem, which concerns a different mapping.

## Conditional Corollary C: positive model-test-curve mass profiles

For a test curve \(\Gamma\in\operatorname{TC}(X,\theta)_{>0}\) as in Definition 17.12.1, define
\[
  H(\tau)=M(\Gamma_\tau)^{1/n},\qquad
  -\infty<\tau<\Gamma_{\max}.
\]
Then **H is positive, finite, concave and continuous** on that open interval, and its extension to \(\tau=-\infty\) is continuous with \(H(-\infty)=M(\Gamma_{-\infty})^{1/n}>0\).

Indeed \(\Gamma_{(1-t)\tau_0+t\tau_1}\geq(1-t)\Gamma_{\tau_0}+t\Gamma_{\tau_1}\) by concavity of a test curve. Theorem 13.13.11 gives the corresponding mass inequality; apply (A) to the right-hand combination. Positivity is Lemma 17.12.6; an everywhere finite concave function on an open interval is continuous. The endpoint mass convergence is the **already printed** Corollary 13.13.12 and Proposition 17.12.9 dependency; continuity of the positive root finishes. We do **not** claim that the hyperplane segment (B) is a normalized model test curve, or that the general Ross–Witt Nyström correspondence has been newly verified.

## Disposition and proposed text insertion

**Status: low / verified conditional deduction**, rather than confirmed false theorem, proof-gap repair, mathematical duplication, or complete upstream verification. None of Theorems 13.13.5 / 13.13.11, Proposition 13.11.4, Corollary 13.13.12, Lemma 17.12.6, Proposition 17.12.9 is refuted by the checks above. The source **DDNL19log** proof of the mixed inequality remains a genuine unverified mathematical dependency. The external reference must not be silently dropped as mere history.

**Proposed, not applied:** optional corollary (A) and hyperplane sharpness example after Theorem 13.13.5, and conditional cross-reference at Proposition 17.12.9. Preserve all original sources, stable tags, the precise \(dd^c\) and \(n!\) conventions, and current source-body statements. Affected downstream constructions include only eligible positive-model test-curve mass profiles (§§17.12–17.18), not unconditional proofs of those sections.

**Exact coverage:** selected already partly reviewed §§13.11, 13.13 and 17.12; §20.7.3 used only for smooth sign normalization. **0 new first proof-level section visits; 0 whole mathematical sections certified; 25 chapters/747 sections in actual current ToC.** The excluded Demailly regularization, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remains **deferred-by-user**, not certified. No changes to main, body, registry, source repositories, permanent tags, CI, builds, tests, or published site.
