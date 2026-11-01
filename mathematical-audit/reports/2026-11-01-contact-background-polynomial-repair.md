# A missing background-positivity step in the mixed contact-set proof

**Date:** 2026-11-01. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** selected new proof-step inspection of Theorem 13.13.57, especially Step 3; not a full verification of §13.13, the theorem, or its upstream approximation/PDE arguments.

## Finding POME-NPP-DNT-CONTACT-BACKGROUND-001

**Severity:** medium. **Status:** **confirmed proof gap; verified conditional repair proposed, not applied**. The printed theorem has **not** been disproved. The replacement below closes the particular background mismatch **conditional on the previously stated Step 2 contact identity, the non-pluripolar mixed-product polynomial law, and the cited regularity of the envelope**; those inputs are not certified by this run.

**Exact integrated anchor:** `docs/sections/non-pluripolar-products--properties-of-non-pluripolar-products/index.html`, production blob `4ace6181d3767e6d5ac3a681c36e392e33b717a2`. Theorem 13.13.57, source `sgpt:CDA82187`, permanent tag `6245F87DD88E`, statement at line 1167, Step 2.2 at lines 1285–1293, Step 3 at lines **1295–1315**, particularly the unsupported invocation “However, Step 2 implies” at **1308–1312**. Lemma 13.13.51, source `sgpt:2ED2C8D7`, permanent tag `9453F71CEE8F`, statement at lines 1054–1073 and Eq. 13.13.52 (tag `93FB8527BF9B`). Proposition 13.13.50, source `sgpt:5B387752`, permanent tag `4BEA034735FD`, lines 1049–1054. Theorem 13.13.49, source `sgpt:03EBC438`, permanent tag `FE0721C3DE01`, lines 1037–1047, is an explicitly quoted **external PDE regularity input** (Tosatti and Chu–Zhou) rather than a self-contained proof. Preserve that substantive attribution and dependency.

### The exact missing hypothesis

Step 2 establishes the contact identity for a `C^{1,\bar 1}` barrier `g` that is itself `\theta`-psh. Step 3 sets
[
q=P_{	heta+omega}(f), qquad arphile qle f,
]
where (omega>0) is chosen so (	heta+omega>0), and then applies Step 2 to (arphi) and (q) **with background (	heta)**. But (qinmathrm{PSH}(X,	heta+omega)) need not belong to (mathrm{PSH}(X,	heta)). The existing source footnote 8 at line 1318 itself notes this lack of (	heta)-psh positivity, while not supplying the required bridge. Consequently that invocation does not follow as written.

This is a genuine nonimplication, not just missing notation. Take (X=mathbb P^1), (	heta=0), (arphi=0), and let (omega) be the Fubini–Study form. Choose a nonzero, nonnegative smooth bump (b) supported in a proper coordinate disc, and set (f=epsilon b) with (epsilon>0) so small that (omega+dd^cfgeomega/2). Then (f) is (omega)-psh, hence (q=P_omega(f)=f), but (q) is nonconstant and thus is **not** (0)-psh on compact connected (mathbb P^1). Moreover ({arphi=q}supset Xsetminusoperatorname{supp}(b)) has nonempty interior, so the issue is not eliminated by an empty contact set. This example does **not** contradict the desired contact identity: it only disproves Step 3's unqualified application of Step 2.

### Conditional replacement of the missing line

Retain (q=P_{	heta+omega}(f)) and (C={arphi=q}). By the integrated envelope regularity (Proposition 13.13.50, with the same obstacle twice), (qin C^{1,ar1}); in particular ((	heta+dd^cq)^n) is meaningful as a *signed* measure even if (q) is not (	heta)-psh. For every real (tge1),
[
	heta_t=	heta+tomega
]
is Kähler and both (arphi) and (q) are (	heta_t)-psh, since
[
	heta_t+dd^carphi=(	heta+dd^carphi)+tomegage0,qquad
	heta_t+dd^cq=(	heta+omega+dd^cq)+(t-1)omegage0.
]
Also (arphile q). Step 2 is therefore **legitimately applicable in the background (	heta_t)**, giving the equality of measures restricted to the fixed contact set (C):
[
mathbf1_Ciglangle(	heta+tomega+dd^carphi)^nigangle
=mathbf1_C(	heta+tomega+dd^cq)^n,qquad tge1. 	ag{*}
]
For fixed (C), testing both sides against any smooth function gives two polynomials in (t) of degree at most (n): on the left by multilinearity of non-pluripolar mixed products with the fixed smooth nonnegative (omega), and on the right by ordinary multilinearity for the bounded-coefficient form (dd^cq). The polynomials agree on ([1,infty)), so their coefficients and values at (t=0) agree. Thus
[
oxed{mathbf1_Clangle(	heta+dd^carphi)^nangle
=mathbf1_C(	heta+dd^cq)^n.} 	ag{**}
]
This is precisely the identity that the printed Step 3 asserts without the bridge. On the smaller contact set ({arphi=f}={arphi=q=f}subset Ccap{q=f}), Lemma 13.13.51 gives the almost-everywhere second-order contact of (q) and (f), hence the equality of their bounded-coefficient signed top-degree forms. Restricting (**) then yields Eq. 13.13.59 and completes this **one** gap, subject to the indicated Step 2 and regularity inputs.

Do **not** infer a priori that (	heta+dd^cqge0), or that ((	heta+dd^cq)^n) is a non-pluripolar positive measure. It is a signed measure whose definition and equality arise from the (C^{1,ar1}) bound and polynomial continuation. In particular, no illicit evaluation of the positive-current contact theorem at (t=0) is needed.

### Dependency and exclusion audit

- **Internal conditional inputs:** Step 2 of Theorem 13.13.57; polynomial dependence of non-pluripolar mixed products with a smooth semipositive factor; Lemma 13.13.51 and Proposition 13.13.50 for regularity and contact Hessians. Only their required conclusions were used, not a claim of transitive proof certification.
- **Genuine external input:** the globally quoted C1,1 envelope estimate Theorem 13.13.49 (Tosatti, Chu–Zhou) underlying the contact regularity route; it is not a historical-only citation. Its PDE proof is not supplied or audited here.
- **Explicitly excluded:** Step 2.1 contains a decreasing smooth approximation of a psh function (around lines 1220–1230). This was **neither reviewed, repaired, nor treated as certified**; all Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**. This repair is conditional on Step 2 as a previously printed lemma, not a way to resume that programme.
- **Affected dependents:** Theorem 13.13.57, its contact formula Eq. 13.13.58 (tag `F5A7BEAB8003`) and Corollary 13.13.61 (tag `77CAD5891555`), plus downstream uses of the Di Nezza–Trapani contact identity. The theorem is **not** classified false; no current proof/body/source/registry/canonicalization/permanent-tag change is applied.

### Coverage accounting and proposed patch

This is **first new selected proof-step verification of Step 3 of 13.13.57** within §13.13, which already had other selected passages reviewed. Step 2.2 was read for the matching polynomial technique, and the displayed statements of 13.13.49–51 were checked as dependencies. Not a first section visit; neither an entire theorem nor section has been certified. The current inventory remains **25 chapters, 747 numbered sections, 0 wholly mathematically certified sections**. Proposed production patch: replace the assertion at lines 1308–1312 by the (	heta_t) argument (*)–(**) while retaining all tags, historic attribution, and the external PDE citation. This audit only records the patch for separate review. No build, tests, CI, formalization or publication were performed.
