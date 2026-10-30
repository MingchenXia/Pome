# Classical fine neighborhoods are density-one neighborhoods, but not conversely

**Audit date:** 2026-10-30.
**Pinned production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit branch:** \`review/mathematical-audit\` (notes only).
**Disposition:** two **low / verified conditional deduction** findings. Neither asserts an incorrect printed theorem, a repaired proof, or complete verification of either reading section.

## Actual integrated passages and provenance

1. \`docs/sections/fine-topology-and-balayage/index.html\`, production blob \`d4c8eed09391441b4b6d13e2fa402a60da70be0d\`, section **4.2** permanent tag \`8618E9B4AA3D\`. Definition 4.2.2, source \`foundations-of-pluripotential-theory:F5342A6A\`, permanent tag \`C067468FA3F0\`, physical lines **29–37**, describes the subbasis of the classical fine topology. Proposition **4.2.4**, source \`foundations-of-pluripotential-theory:D80928DD\`, permanent tag **\`CAAD6BABA60C\`**, lines **51–80**, reduces every fine neighborhood to one strict superlevel \`{u>a}\` of a subharmonic function. Proposition **4.2.5**, source \`foundations-of-pluripotential-theory:01F6C408\`, permanent tag **\`9E787ECDB068\`**, lines **85–99**, proves the weaker positive-volume property for the same sets.
2. Same file, Theorem **4.2.22**, source \`foundations-of-pluripotential-theory:333EA4BE\`, permanent tag **\`730413AAC920\`**, physical lines **approximately 495–520** (find by the permanent tag if the HTML changes), proves completed Lebesgue measurability of fine-open sets. It is used only for the statement about the density topology; its Choquet/capacity dependencies are not recertified.
3. \`docs/sections/perron-theory-and-fine-boundary-limits/index.html\`, main blob **\`4bc2fb9317e2b6f6bb5b2d90208c677da8275eba\`**, Theorem **4.4.22**, source \`classical-potential-theory:A2D0D838\`, permanent tag **\`2B657EA5CC09\`**, physical lines **304–314**. It characterizes nonthinness of a closed set at a boundary point by existence of a positive superharmonic barrier on its complement that tends to zero there. We use this precise implication, without rechecking the full Perron or Wiener proof.

The established \`POME-FINE-HYP-001\` compares classical fine and plurifine traces on a complex hyperplane; \`POME-FINE-QL-001\` concerns polar-exception countability/quasi-openness. Both are different from the Lebesgue *density topology* and are unchanged.

## POME-FINE-LEBESGUE-DENSITY-001

**Severity/status:** low / **verified conditional deduction**. The printed Proposition 4.2.5 is correct, but its conclusion admits a quantitative strengthening.

**Statement (all real dimensions \`d >= 2\`).** Let \(\Omega\subset\mathbb R^d\) be open, \(x\in\Omega\), and \(N\) any classical fine neighborhood of \(x\). There exist an ordinary neighborhood \(V\ni x\), \(u\in\mathrm{SH}(V)\), and a real \(a<u(x)\) with
\[
  E=V\cap\{u>a\}\subset N.
\]
For all sufficiently small \(r>0\), set \(M_r=\sup_{\overline{B(x,r)}}u\). Then \(M_r<\infty\) and
\[
 \boxed{\quad
 \frac{|B(x,r)\setminus N|^*}{|B(x,r)|}
 \le
 \frac{|B(x,r)\setminus E|}{|B(x,r)|}
 \le \frac{M_r-u(x)}{M_r-a}
 \xrightarrow[r\downarrow0]{}0 .
 \quad}
\]
Here the outer Lebesgue measure \(|\cdot|^*\) avoids assuming that an arbitrary neighborhood \`N\` is measurable; \(E\) is Borel. In particular every **fine-open** set is density-open for completed Lebesgue measure, and each finely continuous map to a metric space is approximately continuous (with respect to Lebesgue density) at every point.

**Complete short proof.** Proposition 4.2.4 supplies \(E\). The inequality \(u(x)>a\) implies that \(u(x)\) is finite. Upper semicontinuity on a compact ball gives \(M_r<\infty\) and
\[
 M_r\searrow u(x)\quad(r\downarrow0).
\]
Put \(B=B(x,r)\) and \(q=|B\setminus E|/|B|\). On \(E\cap B\), \(u\le M_r\); on \(B\setminus E\), \(u\le a\). Since the ball submean inequality applies at \(x\),
\[
  u(x)\le\frac1{|B|}\int_Bu
       \le(1-q)M_r+qa
       =M_r-(M_r-a)q.
\]
Thus \(0\le q\le(M_r-u(x))/(M_r-a)\to0\), as \(M_r-a\to u(x)-a>0\). The inclusion \(E\subset N\) proves the outer-measure bound. For a fine-open set, completed Lebesgue measurability is furnished by Theorem 4.2.22. If \(f\) is finely continuous, then \(N_\varepsilon=f^{-1}(B_Y(f(x),\varepsilon))\) is a fine neighborhood for every \(\varepsilon>0\); the quantitative bound shows
\[
 \frac{|\{y\in B(x,r):d_Y(f(y),f(x))\ge\varepsilon\}|^*}{|B(x,r)|}\to0.
\]
This is approximate continuity, with extended-valued targets handled through any compatible metric on the extended reals.

**Proposed nonmandatory addition:** after Proposition 4.2.5, add the displayed quantitative density-one estimate and an optional corollary that the fine topology is contained in the Lebesgue density topology. **Affected dependents:** §4.2.22–23 fine-open measurability/quasi-openness, §4.4.19 fine limits, §5.47 plurifine comparison. Neither the statement nor its proof needs regularization.

## POME-FINE-DENSITY-STRICT-001

**Severity/status:** low / **verified conditional deduction**, conditional only on the printed nonthinness/barrier equivalence in Theorem 4.4.22. This proves that the inclusion above is **strict**, already in dimension two.

**Explicit example and justification.** Take \(\Omega=\mathbb R^d\), \(d\ge2\), let
\[
 H=\{x\in\mathbb R^d:x_1=0\},\qquad
 E=H\setminus\{0\},\qquad U=\mathbb R^d\setminus E .
\]
The set \(U\) is Lebesgue measurable. At every \(x\in U\setminus\{0\}\) it contains an ordinary Euclidean neighborhood; at \(x=0\) its complement \(E\) has Lebesgue measure zero. Hence \(U\) has Lebesgue density one at **every** point of \(U\): it is density-open.

Nevertheless \(U\) is **not** fine-open at \(0\). On \(B(0,1)\setminus H\), the function
\[
 w(x)=|x_1|
\]
is positive and harmonic **on each component**, hence positive superharmonic on the whole open complement, and \(w(x)\to0\) as \(x\to0\) through that complement. Applying Theorem 4.4.22 to the **closed** set \(H\) gives that \(H\) is nonthin at \(0\). Thinness at \(0\) depends only on \(H\setminus\{0\}=E\) by Definition 4.2.3/Proposition 4.2.4; thus \(E\) is nonthin at \(0\). If \(U\) contained a fine neighborhood of \(0\), that neighborhood would miss \(E\) and Proposition 4.2.4 would imply that \(E\) is thin at \(0\), a contradiction. No sequential compactness, exceptional-set equality, or limit exchange is used.

**Optional correction/remark:** none required to the mathematical statements, which are correct. A remark distinguishing Lebesgue density neighborhoods from fine neighborhoods prevents overreading Proposition 4.2.5 as an equivalence. Dependents: §4.2 fine topology, §4.4 thinness/barriers and related (distinct) §4.2.25 classical-versus-plurifine comparison. This is **not** an alternative proof of the general Wiener criterion.

## Limits of this audit and reproducibility

The direct checked mathematical passages were **Propositions 4.2.4–5**, the neighborhood subbasis in **Definition 4.2.2**, and the explicit **Theorem 4.4.22** barrier implication. Theorem 4.2.22 was consulted only for measurability. Their full historical sources, the general fine-topology/capacity theory, all of §4.2 and all of §4.4 remain **uncertified**. The topological comparison is a **conditional deduction**, not a claim that printed Pome theorems are false. In particular the already recorded §4.2.25 and §4.4.26 findings are not being counted again.

The standing inventory is **25 chapters / 747 numbered current-ToC sections / zero entire-section certifications**; all resolved/unresolved/deferred statuses are preserved. Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme are excluded by the user's instruction and remain **deferred-by-user**, not resolved. No changes to \`main\`, generated reading edition, source bodies, permanent tags, registry, website, PRs, or CI; no builds or formal-verification runs.
