# Audit — a Weil/Cartier quantifier conflict between §§20.6 and 20.7

**Date:** 2026-11-10. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Stable finding:** `POME-WEIL-CARTIER-DIVISOR-SCOPE-001`.
**Classification:** confirmed error **in the unqualified divisor-to-line-bundle clause under the collection's reduced-complex-space convention**; severity **medium**. The classical statement on a **complex manifold** and the Poincaré–Lelong identity for a line bundle on a manifold are **not refuted**. If the intended scope of Proposition 20.7.3 was already restricted to manifolds by an unprinted contextual convention, the issue is a missing explicit ambient hypothesis / cross-section scope mismatch, not a false manifold theorem. No production repair has been applied.

## Exact integrated locations and data

- `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, physical line **11**: “A complex space is always assumed to be reduced, paracompact and Hausdorff.” This global convention does **not** require smoothness.
- `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, blob `d4817ac64b1365bd967d42cd474fec169f992e28`. Definition **20.6.2**, source data-tag `BE0C86A8`, permanent tag `BE0C86A8DD65`, line **8**, defines Weil divisors on reduced pure-dimensional spaces. Proposition **20.6.4**, source data-tag `BD1D45B4`, permanent tag `AA96C35C8290`, lines **29–41**, distinguishes Cartier cycles and explicitly asserts the equivalence of Weil and Cartier divisors *on a complex manifold*. Example **20.6.5**, source data-tag `E054C396`, permanent tag `0C462992AB3A`, lines **47–74**, proves an effective Weil divisor on a reduced normal quadric is **not Cartier**.
- `docs/sections/meromorphic-sections-and-divisor-classes/index.html`, blob `d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8`. Proposition **20.7.3**, source data-tag `00A05C89`, permanent tag `ACC6D09EDDD9`, lines **13–17**, contains an unqualified clause: every locally finite integral hypersurface divisor `D` determines a holomorphic line bundle `O(D)` with meromorphic section of divisor `D`. Its proof, lines **25–27**, assumes all irreducible hypersurfaces have local equations and uses the sheaf surjection `M* -> Div`, which holds for **Cartier** divisors in general, not arbitrary Weil divisors on a singular space.
- The previous [§20.7 report](2026-10-26-guillemin-stratum-hessian-and-nonprincipal-null-chern-divisors.md) treated a different question, the kernel of the Chern-class map on an elliptic curve, and explicitly did *not* claim anything about singular complex spaces. This scope conflict is **not a recurrence** of that earlier finding.

## Counterexample, with a complete internal contradiction argument

Let
[
X={(x_1,x_2,x_3,x_4)inmathbb C^4:x_1x_2+x_3x_4=0},
qquad
A={x_1=x_3=0}subset X.
]
The quadric is reduced and irreducible of pure complex dimension three; its only singular point is the origin (the gradient vanishes there only). Thus `A` is an integral effective Weil divisor in the exact sense of Definition 20.6.2. Example 20.6.5 states and proves that `A` is **not Cartier at the origin**. For completeness, its non-Cartier argument can be checked directly:

The surjective rank-one parametrization
[
F:mathbb C^4longrightarrow X,quad
(a,b,c,d)longmapsto(ac,bd,ad,-bc)
]
is a submersion onto the smooth locus away from ({a=b=0}cup{c=d=0}), a set of complex codimension two. If a meromorphic germ (f) on (X) had divisor ([A]), then the divisor of (fcirc F) away from those codimension-two sets would be exactly ([a=0]), with multiplicity one and no other zero or pole hypersurfaces. Ordinary local factoriality of holomorphic germs in (mathbb C^4) consequently gives (fcirc F=a,e) for a holomorphic *unit* (e) near the origin; a divisor cannot be supported only in the exceptional codimension-two set. Yet
[
F(ta,tb,t^{-1}c,t^{-1}d)=F(a,b,c,d)qquad(tinmathbb C^*).
]
Cancelling (a) in the resulting identity for (fcirc F) gives
(e(a,b,c,d)=t,e(ta,tb,t^{-1}c,t^{-1}d)).
At the origin this reads (e(0)=t,e(0)), impossible for (t
e1) because (e(0)
e0). Hence no such meromorphic germ exists, which is exactly the failure of the Cartier condition. This argument uses only the ordinary smooth local factorization already cited in §20.6 and does **not** invoke the excluded Demailly regularization programme.

Now apply the **unqualified** sentence in Proposition 20.7.3 to (D=A) on (X). If it supplied a holomorphic line bundle (mathcal O(A)) and a canonical meromorphic section (s) with (operatorname{div}s=A), trivializing that line bundle near the origin would write (s=f e) for a meromorphic function (f), with (operatorname{div}f=A). This contradicts the just-verified non-Cartierness. Thus that unqualified sentence cannot hold for all integral Weil divisors on reduced complex spaces, a category expressly introduced in the immediately preceding §20.6. **This disproves only the overly broad scope, not the smooth-manifold divisor theorem.**

## Mathematical diagnosis and exact correction

The local equations (u_i) used in §20.7 line 25 exist for a **Cartier divisor**. A non-Cartier Weil divisor need not be principal on any neighborhood of its singular points; therefore (u_j/u_i) need not be a holomorphic unit, and the stated line bundle cocycle cannot be constructed. Likewise, in §20.7 line 27 the quotient sheaf of (mathcal M^*) by (mathcal O^*) is the **Cartier divisor sheaf**. Replacing it by the Weil divisor sheaf on a singular normal complex space makes the alleged sheaf sequence nonexact at its right endpoint.

**Suggested production patch, not applied:** qualify Proposition 20.7.3 explicitly with “Let (X) be a complex manifold” before its analytic current identity and divisor statement. Alternatively separate its manifold-valued current assertion from the purely sheaf-theoretic claim: on a general reduced space, restrict (D) to **Cartier divisors** and use the exact sequence
[
1longrightarrow mathcal O_X^*
longrightarrow mathcal M_X^*
overset{mathrm{div}}{longrightarrow}
mathrm{CaDiv}_Xlongrightarrow0.
]
For a normal singular space, the sheaf associated to a Weil divisor can be rank-one reflexive without being locally free; **do not identify it with a holomorphic line bundle** without checking the Cartier condition. The globally stated comparison (mathcal O(D_1)simeqmathcal O(D_2)) and the principal-divisor kernel remain true for Cartier divisors, or for all integral Weil divisors when (X) is smooth. Preserve the existing historical source attribution and permanent tags.

**Dependents to inspect (not certified here):** references to §20.7.3 in §20.8 restricted-volume and divisor-class arguments, and any §9 complex-space applications that implicitly upgrade a Weil divisor to a line bundle; the general divisor/current identity on singular spaces also requires an appropriate interpretation, not the unrestricted smooth differential-form proof. No other dependent theorem is declared false without reading its hypotheses.

## Precise coverage and limitations

First direct **scope/quantifier comparison** between Definition 20.6.2, Proposition 20.6.4, Example 20.6.5, and Proposition 20.7.3; independent check of the pullback/scaling non-Cartier proof and one-line contradiction to the latter's broad divisor-to-line-bundle clause. §20.7 and §20.6 had already received *selected* mathematical audit in previous sessions, so this is **0 newly first proof-visited numbered sections and 0 whole-section mathematical certifications**. The catalogue remains 25 chapters / 747 numbered sections (recorded catalogue baseline). The local Poincaré–Lelong formula, all divisor class constructions on manifolds, and downstream restricted volume statements have **not** been re-proved transitively. No external paid inputs, private materials, source/body edits, canonicalization, tests, builds, CI or website publication. The user-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, neither certified nor resumed.
