# Strong Hodge decomposition descends under generically finite holomorphic maps

**Finding ID:** POME-HODGE-GENERICALLY-FINITE-DESCENT-001  
**Date:** 2026-11-08  
**Severity / status:** low / **verified conditional deduction** (a strict extension of a correct printed theorem; no source error asserted).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Target:** docs/sections/general-complex-cohomology-and-modifications--strong-hodge-structure-under-modifications/index.html, blob 6414dd82e72d4af59e4706e105c4752501e9829f.  
**Anchor:** Theorem 10.87.1, source label **demailly-complex-geometry:451F3847**, permanent tag **C4B9BA82F24B**, physical HTML lines **16–27**; natural maps and definitions lines **7–13**, the projection-and-descent proof lines **23–27**. Source naming is provenance, not part of the owner-excluded regularization programme.

## Printed statement and new statement

The printed theorem says that, if a modification \(\mu:\widetilde X\to X\) has strongly Hodge-decomposed source, then \(X\) has strong Hodge decomposition. It also establishes smooth/current pushforwards on Bott–Chern, Dolbeault and de Rham cohomology and their commutation with the natural comparison maps.

**Verified extension.** Let \(f:Y\to X\) be a **proper, surjective, generically finite holomorphic map** of positive generic degree \(d\) between **connected compact complex manifolds of the same complex dimension**. If \(Y\) has strong Hodge decomposition in the precise sense of the displayed maps of §10.87, then \(X\) has strong Hodge decomposition. In particular this applies to ramified finite covers and to generically finite holomorphic maps from compact Kähler manifolds. No Kähler assumption is imposed on \(X\), and no unramifiedness or birationality is required.

## Proof

1. **The degree identity.** For every smooth complex-valued differential form \(\alpha\) on \(X\), one has the equality of currents
   \[
       f_*f^*\alpha=d\,\alpha. \tag{1}
   \]
   Indeed, against every smooth test form \(\beta\) of complementary real degree,
   \[
       (f_*f^*\alpha)(\beta)
       =\int_Y f^*(\alpha\wedge\beta)
       =d\int_X\alpha\wedge\beta.
   \]
   For the second equality, remove the analytic discriminant of the proper generically finite holomorphic map. On its complement the map is a proper local biholomorphism and hence a covering with \(d\) positively oriented sheets; ordinary change of variables gives the equality there. The critical set is a proper analytic subset (the local complex Jacobian vanishes), so it has real volume zero. Its image is a proper analytic subset by the internal proper-image theorem (§9.7.2) and the local dimension statement (§9.3); it too has zero real volume. The preimage of the discriminant is a proper analytic subset and is null. Thus all deleted sets contribute zero to the integral of a smooth top-degree form. This is the **degree \(d\)** version of the change-of-variables argument already printed in the proof of Theorem 10.87.1. In complex dimension zero the assertion reduces to the connected-point case \(d=1\).

   Equivalently, the second equality follows from the elementary topological-degree formula for compact oriented smooth manifolds: holomorphic regular local degrees equal \(+1\). No product of singular currents or interchange of singular limits enters (1).

2. **Pass to the correct cohomologies.** Holomorphicity makes \(f^*\) commute with \(\partial,\bar\partial\) and \(d\) on smooth forms. Properness makes the pushforward of currents well-defined and commuting with the same operators, with the same bidegree in relative dimension zero. Smooth/current comparisons in Corollary 10.43.11 and Theorem 10.85.2 transport the pushforward to Dolbeault, de Rham and Bott–Chern groups. Equation (1) therefore gives
   \[
       f_*f^*=d\,\operatorname{id}                         \tag{2}
   \]
   in **each** of these three theories, separately in each bidegree. The natural maps
   \[
     j_X^{p,q}:H_{\rm BC}^{p,q}(X)\longrightarrow H_{\bar\partial}^{p,q}(X),
     \qquad
     k_X^r:\bigoplus_{p+q=r}H_{\rm BC}^{p,q}(X)\longrightarrow H_{\rm dR}^r(X,\mathbb C)
   \]
   commute with both \(f^*\) and \(f_*\), since they are defined by the same closed-form representatives. The direct-sum comparison in \(k^r\) respects the \((p,q)\) decomposition under holomorphic pullback and pushforward.

3. **Injectivity and surjectivity, without an unsupported direct-summand claim.** Write \(D_X\) for any one of \(j_X^{p,q}\) or \(k_X^r\) and \(D_Y\) for its counterpart. By hypothesis \(D_Y\) is an isomorphism. If \(D_X a=0\), then
   \(D_Y(f^*a)=f^*(D_Xa)=0\), so \(f^*a=0\), and (2) gives \(d\,a=0\). Since these are complex vector spaces and \(d>0\), \(a=0\): \(D_X\) is injective. Conversely, for any \(b\) in the target of \(D_X\), lift \(f^*b\) across \(D_Y\), writing \(D_Yc=f^*b\). Then
   \[
        D_X(d^{-1}f_*c)=d^{-1}f_*D_Yc
          =d^{-1}f_*f^*b=b.
   \]
   Thus \(D_X\) is surjective. This works individually for every \((p,q)\) and \(r\), so \(X\) has strong Hodge decomposition.

4. **Consequences and normalization.** Taking \(d=1\) recovers the stated modification-descent argument. For a degree-two holomorphic isogeny of complex tori, (2) reads \(f_*f^*=2\operatorname{id}\), not \(\operatorname{id}\). The factor \(d^{-1}\) in the surjectivity argument is therefore essential. Applying Theorem 10.47.13 to a Kähler source, and Theorem 10.84.1 to the resulting strong Hodge decomposition on the target, yields the same Hodge symmetry and first-page Frölicher degeneration conclusions as in the printed theorem. These are **conditional on** the cited internal current-comparison, proper-image and Hodge theorems, whose transitive proof chains are not certified by this focused audit.

## Diagnosis, proposed patch, dependent scope

The printed Theorem 10.87.1 is **correct**; its modification hypothesis is sufficient, not asserted necessary. This report supplies a **new stronger deduction**, not a repaired counterexample and not a verified change to the production text. Optional proposed manuscript amendment: following Theorem 10.87.1, add a separately tagged corollary stating the generically finite version and the degree-\(d\) current identity, while retaining the original theorem, attribution, source tag, permanent tag and modification proof. The argument directly concerns §10.87 and interfaces with §§10.43, 10.47, 10.84–10.85 and the Fujiki/Kähler-source consequences; no blanket verification of these sections is asserted.

**Review boundary:** One selected theorem and its displayed proof were audited in the actual current reading edition; the internal current-comparison and proper-image results were checked only as dependencies. No entire section, chapter or transitive proof chain was mathematically certified. The Demailly approximation/regularization and its dedicated Bergman, L2, OT, multiscale-atlas and positivity-loss work remain **deferred-by-user**, not solved. No build, tests, CI, formal verification or website publication was run.
