# Exact pairwise essential-extremal speed of weak geodesics

**Audit date:** 2026-10-31. **Production `main` reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch starting HEAD:** `d5db8140c940a9e6ad5e2729129ac641e4670936`.

**Stable finding ID:** `POME-GEO-PAIRWISE-EXTREMAL-SPEED-001`. **Severity:** low. **Status:** **verified conditional deduction**; the two printed propositions used below are not shown false, and the deduction is a proposed additional corollary, not an integrated proof or a certification of their prerequisites.

## Exact integrated sources, stable identifiers, and physical line anchors

1. Main reading-edition file `docs/sections/relative-energy-and-perron-segments--extremal-slopes-and-long-perron-segments/index.html`, Git blob `023e78b3da0fd8f33d39177dba02f410b10f376c`. **Proposition 17.9.1**, original source `foundations-of-pluripotential-theory:58E4D688`, permanent tag `0583958ACA6D`: hypothesis and two one-endpoint essential-extremum identities at **physical HTML lines 10–15**, proof at **18–26**. **Proposition 17.9.2**, source `foundations-of-pluripotential-theory:2B4D191D`, permanent `A6533ED6CC68`, **lines 33–46 and 49–75**, was checked for its endpoint/comparison conventions only; its long-ray asymptotic is **not** re-claimed as a new result.
2. Internal dependency `docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html`, Git blob `662f60d73fc585b6ea3b710f2a3472bac1de8a7c`. **Theorem 17.7.8**, source `foundations-of-pluripotential-theory:108758A0`, permanent `2FECBE87C487`, **lines 186–190 and 195–209**, especially **190 and 206**, identifies every restriction of the geodesic as the weak geodesic between its slice endpoints. **Proposition 17.7.9**, source `foundations-of-pluripotential-theory:470B93BF`, permanent `DD04D189A4D3`, **lines 214–235**, especially **220**, gives time reversal and affine-shift compatibility.
3. Independent cross-chapter check (no new finding or complete certification): `docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html`, main blob `d234ab96e33bfd24ad1d53d29332b2c021cddeff`: **Lemma 13.4.1**, source `foundations-of-pluripotential-theory:4EEFCE9D`, permanent `263D0F5AEE0A`, **lines 10–68** (weighted positive-current integration by parts and auxiliary-dimension reduction); **Lemma 13.4.2**, source `foundations-of-pluripotential-theory:12132441`, permanent `5D93FCFBA57F`, **lines 72–94** (zero pluripolar mass under a locally bounded factor); **Proposition 13.4.3**, source `foundations-of-pluripotential-theory:38D341C7`, permanent `90E0E28D9A95`, **lines 98–126** (bounded-factor NPP locality); **Lemma 13.4.4**, source `foundations-of-pluripotential-theory:C504A6B9`, permanent `CA3A887474EE`, **lines 133–153** (Borel disintegration); and **Lemma 13.4.5**, source `foundations-of-pluripotential-theory:638C435E`, permanent `4AD0BFC1BFCD`, **lines 157–190** (fiberwise Bedford–Taylor Fubini), including Equation **13.4.6** at **163–165**, source `foundations-of-pluripotential-theory:917DDB45`, permanent `7F078C7DCBDD`. These selected analytical transitions were inspected for current hypotheses, but their external or internal precursor chain was **not** transitively verified.

## New exact statement

Let `X` be the compact complex manifold, `theta` the background, and `phi` the reference potential under the standing hypotheses of the printed weak-geodesic Theorem 17.7.8. Let `u,v\in\mathcal E(X,\theta,\phi)` have **equivalent ordinary singularities** `u\sim v`, so their difference is bounded on the common finite locus. Let `G_t=G_t(u,v)` be their weak geodesic, with `G_0=u` and `G_1=v`. Put
\[
 C=\operatorname*{ess\,sup}_X(v-u),\qquad
 c=\operatorname*{ess\,inf}_X(v-u),\qquad -\infty<c\le C<\infty.
\]
Then **for every pair** `0\le s\le t\le1`, not merely from the initial endpoint,
\[
 \boxed{\operatorname*{ess\,sup}_X(G_t-G_s)=(t-s)C,\qquad
 \operatorname*{ess\,inf}_X(G_t-G_s)=(t-s)c.}\tag{1}
\]
The essential extrema can equally be taken on the common finite locus and after deletion of any pluripolar subset, under the printed Proposition 17.9.1's representative convention. In particular the essential uniform distance between slices satisfies
\[
 d_{\infty}(G_s,G_t):=\operatorname*{ess\,sup}_X|G_t-G_s|
 =(t-s)\max\{C,-c\}
 =(t-s)d_{\infty}(u,v).\tag{2}
\]
Also
\[
 \operatorname*{ess\,osc}_X(G_t-G_s)=(t-s)(C-c).\tag{3}
\]
Thus the chosen weak-geodesic path is a **constant-speed isometric embedding** for the bounded-difference essential-uniform distance on this fixed ordinary-singularity class, assuming the printed geodesic construction. No statement about the Darvas `d_1` metric, global existence between distinct singularity classes, or completion of the full metric space is implied.

## Complete deduction from the two identified printed results

Fix `0\le s<1`. By time reversal (17.7.9(2)),
\[
 G_s(u,v)=G_{1-s}(v,u).
\]
Since `u\sim v`, apply **both** exact essential-extremum identities of Proposition 17.9.1 to the reversed pair `(v,u)`. Its endpoint difference is `u-v`, whose essential supremum is `-c` and infimum is `-C`. Thus
\[
 \operatorname*{ess\,sup}_X(G_s-v)=-(1-s)c,
 \quad
 \operatorname*{ess\,inf}_X(G_s-v)=-(1-s)C.
\]
Negating gives
\[
 \operatorname*{ess\,sup}_X(v-G_s)=(1-s)C,
 \quad
 \operatorname*{ess\,inf}_X(v-G_s)=(1-s)c.\tag{4}
\]
These bounds also prove `G_s\sim v` by the printed quasi-everywhere/essential-representative identification; in particular Proposition 17.9.1 can be applied again to `(G_s,v)`. Theorem 17.7.8's restriction theorem identifies, for `s\le t\le1`,
\[
 G_t(u,v)=G_{(t-s)/(1-s)}(G_s,v).
\]
Applying Proposition 17.9.1 to this new pair and substituting (4), with `\tau=(t-s)/(1-s)`, yields
\[
 \operatorname*{ess\,sup}_X(G_t-G_s)=\tau(1-s)C=(t-s)C,
\]
and identically the essential infimum `=(t-s)c`. When `s=t` both assertions are zero; the sole case `s=1` forces `s=t=1`. Formula (2) is the maximum of the absolute values of the two extrema; subtracting them proves (3). No interchange of a weak-current limit, directed-net/sequence compactness, or averaging with a singular measure enters this argument.

**Sharpness / sanity model.** If `v=u+a` for a real scalar `a`, the affine-shift identity in Proposition 17.7.9 gives `G_t=u+at`. Hence `c=C=a`, and (1)–(2) hold pointwise with equality for every `s,t`, including `a<0`. Nonconstant bounded perturbations produce `c<C`, in which case (3) measures a genuine signed oscillation; no additional smoothness or approximation assumptions are made.

## Assessment, proposed patch, and exact review coverage

**Classification:** low / verified conditional deduction, not a confirmed theorem error and not a claim of independent transitive certification. **Proposed separately reviewable text:** an optional corollary immediately after Proposition 17.9.1 giving (1)–(3), invoking the restriction identity in Theorem 17.7.8. Retain both original statements, source tags, permanent tags, mathematical conventions and attribution. **Affected dependents:** interpretations of finite weak-geodesic speed in §§17.7–17.9 and the distinction between the essential-uniform geometry and the `d_1`/ray geometry of §17.10; no reorganization or canonical deduplication proposed. This **does not repeat** the earlier endpoint-only `POME-GEO-SLOPES-001` or upper-bound-only `POME-GEODESIC-FULL-TIME-LIPSCHITZ-001`; it proves **exact signed pairwise** identities.

**New actual review:** the essential-extremum argument of §17.9.1 and its §17.7.8 subinterval/reversibility inputs; §17.9.2 read for comparison conventions only. Independently selected transitions §§13.4.1–5 (weighted CLN, no-polar-mass, NPP bounded factors, measure kernel and fiber Fubini) were checked as written, without classifying them as fully verified, or re-registering old issues. **No complete mathematical section** is certified by this review. Production main still has **25 chapters, 747 numbered ToC sections, zero complete mathematical-section certifications**. Earlier confirmed errors, proof gaps, external dependencies, verified-but-not-integrated repairs, and historical attributions preserve their prior statuses. The entire user-excluded Demailly approximation/regularization, dedicated Bergman, weighted `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, neither resolved nor reopened.

**Verification limitation:** mathematical identities (1)–(3) were established by the explicit two-step deduction above; no project tests, builds, CI, website publication, formal verification, or independent certification of the upstream geodesic-existence theorem was performed. No production `main`, source, permanent-tag, registry, canonicalization, or published-site file is to be modified by this audit.
