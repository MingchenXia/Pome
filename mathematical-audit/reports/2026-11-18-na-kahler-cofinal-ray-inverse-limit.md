# Countable cofinal Kähler rays in the non-Archimedean inverse limit

- Audit date: 2026-11-18.
- Finding: **POME-NA-KAHLER-COFINAL-RAY-INVLIMIT-001**.
- **Severity: low; status: verified conditional deduction**. This is an exact cofinality/reconstruction result and independent check of the indexing logic, **not** a false printed theorem and **not** a claim of an entirely certified §22.1.
- Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- Actual integrated reading text: `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob **8448d710690ebe1cc28040f9611d05c9d008a961**.
- Source: `sgpt` (the source-variant attribute). Primary stable source labels and permanent tags:
  - §22.1.1 opening reverse order of Kähler forms, physical line **26**.
  - Definition 22.1.2, source `sgpt:B01CC65A`, permanent tag **657951EB240B**, lines **30–43**; transition equation 22.1.3, source `sgpt:93C71D7B`, permanent **A99876729E5F**, lines **34–43**.
  - Definition 22.1.7, source `sgpt:6F37B588`, permanent **A92D6DFAC0CF**, lines **118–123** (volume net).
  - Lemma 22.1.9, source `sgpt:DA29B884`, permanent **587EEDE88F4F**, lines **142–171**, and Lemma 22.1.10, source `sgpt:7CAC00AD`, permanent **9A2678C2C223**, lines **175–225**.
  - Definition 22.1.14, source `sgpt:5A9D4C43`, permanent **CCAAC9DA4E2F**, lines **256–266**; Proposition 22.1.15, source `sgpt:176139CE`, permanent **3943AA7119C5**, lines **270–315**; equation 22.1.16, source `sgpt:40CA45E4`, permanent **29D3530031C6**, lines **272–279**.
- Explicit upstream checked only for statements/typing: `docs/tag/BF40FB71C62C/index.html`, Proposition 17.14.6, source `sgpt:3F2306F9` (transition maps); `docs/tag/6CC72AA0EA90/index.html`, Definition 17.14.1, source `sgpt:06C25A3F` (positive-mass I-model test curves). The deeper analytic arguments in §§16–18 are not re-proved.

## New exact result: a single shrinking Kähler ray suffices

Let \((X,\theta)\) have the hypotheses of Definition 22.1.2: \(X\) connected compact Kähler, and \(\theta\) smooth closed real \((1,1)\) with pseudo-effective class. Fix **any** Kähler form \(\omega_0\), and put \(\omega_j=2^{-j}\omega_0\) for \(j\ge0\). Let
\[
 A_\omega:=\mathrm{PSH}^{\mathrm{NA}}(X,\theta+\omega)_{>0},
 \quad \pi_{\alpha,\beta}:A_\beta\longrightarrow A_\alpha
 \quad(\alpha\ge\beta)
\]
be the actual I-envelope transitions of equation 22.1.3. Assuming their compatibility, the restriction map
\[
 \boxed{\;
 \varprojlim_{\omega\in\mathrm{K\ddot ah}(X)}A_\omega
 \ \xrightarrow{\ \simeq\ }\
 \varprojlim_{j\ge0}
 [\,A_{\omega_0}\leftarrow A_{\omega_1}
           \leftarrow A_{\omega_2}\leftarrow\cdots\,]\; }
\]
is a **canonical bijection of sets**, for every choice of \(\omega_0\). This is not a claim that arbitrary directed nets possess countable cofinal subsets.

**Proof of cofinality.** The order in the printed text is reversed: \(\alpha\preceq\beta\) means \(\alpha\ge\beta\) pointwise. For any Kähler form \(\alpha\), compactness of \(X\) and positive definiteness give a uniform constant \(c_\alpha>0\) with
\[
\alpha\ge c_\alpha\omega_0.
\]
For \(j\) sufficiently large, \(2^{-j}\le c_\alpha\); hence \(\alpha\ge\omega_j\), or \(\alpha\preceq\omega_j\). This is precisely cofinality in the author's chosen directed order. No sequential-compactness principle has been invoked.

**Explicit inverse map.** Suppose \(g_j\in A_{\omega_j}\) satisfy \(g_j=\pi_{\omega_j,\omega_k}(g_k)\) for \(k\ge j\). For any Kähler form \(\alpha\), choose \(j\) with \(\alpha\ge\omega_j\), and set
\[
 g_\alpha:=\pi_{\alpha,\omega_j}(g_j).
\]
If \(j,k\) are two admissible indices, choose \(\ell\ge\max(j,k)\). Then
\(\alpha\ge\omega_j\ge\omega_\ell\) and
\(\alpha\ge\omega_k\ge\omega_\ell\), so functoriality gives
\[
 \pi_{\alpha,\omega_j}g_j
 =\pi_{\alpha,\omega_\ell}g_\ell
 =\pi_{\alpha,\omega_k}g_k.
\]
Thus \(g_\alpha\) is independent of \(j\). For \(\alpha\ge\beta\), choose \(j\) with \(\beta\ge\omega_j\); then
\(\pi_{\alpha,\beta}g_\beta
=\pi_{\alpha,\omega_j}g_j=g_\alpha\).
This proves existence and compatibility. Restriction and extension are inverse on the nose. It also shows that two full NA objects are equal **if and only if** their components agree along this one sequence.

## The volume limit is exactly a decreasing real sequence

Writing \(M(\omega)=\int_X(\theta+\omega+dd^c\Gamma^{\theta+\omega}_{-\infty})^n\), Definition 22.1.7 and its printed monotonicity identify the net limit with its infimum. Cofinality proves the exact identity
\[
 \boxed{\;
 \operatorname{vol}\Gamma
 =\inf_{\omega\in\mathrm{K\ddot ah}(X)}M(\omega)
 =\inf_{j\ge0}M(\omega_j)
 =\lim_{j\to\infty}M(\omega_j). \;}
\]
The last sequence is decreasing under the printed monotonicity input. Hence
\(\operatorname{vol}\Gamma>0\) **iff** this sequence has strictly positive infimum. This last reformulation is distinct from, and does not re-prove, Lemma 22.1.10's substantive positive-volume lifting to an unaugmented positive-mass test curve. The limit formula is independent of the reference form \(\omega_0\) because both rays are cofinal in the same directed index set.

The same order-theoretic argument checks the diagonal step in the printed Proposition 22.1.15: \((\omega_j/2,\omega_j/2)\) is cofinal in the **product** of two reverse-ordered Kähler index sets. Indeed for any pair \((\alpha,\beta)\), sufficiently large \(j\) satisfies both \(\alpha\ge\omega_j/2\) and \(\beta\ge\omega_j/2\). The product-system transition compatibility therefore permits the double inverse limit to be reconstructed from the diagonal values
\(\Gamma^{\omega_j/2,\omega_j/2}\in A_{\omega_j}\).
This gives a precise cofinality explanation for the \(\omega/2,\omega/2\) formula at the end of Proposition 22.1.15, not a second independent proof of all its analytic prerequisites.

## Audit disposition

**Printed statement/proof check.** Definition 22.1.2 uses the correct **reverse** order; the domain and codomain in (22.1.3) match the increasing-form projection. The I-envelope compatibility invoked immediately afterward supplies the exact composition rule used above. The proof of Lemma 22.1.9 expands the difference of larger-class mixed masses, retaining the nonnegative top-power term; the sign is consistent **conditional on** the stated mixed non-pluripolar mass monotonicity. Lemma 22.1.10 employs that inequality to keep a fixed positive mass deficit along \(k^{-1}\omega\); the mass infimum is a genuine **directed** infimum, though this special poset admits our cofinal sequence. The diagonal reconstruction in Proposition 22.1.15 has no index-direction error. No local false theorem is established.

**Dependencies deliberately not certified.** Transition maps actually preserve the required positive-mass I-model class by Proposition 17.14.6. Their functoriality rests on the printed I-envelope theory in §§16.4, 16.6, 16.8 and 17.14, and mass monotonicity in the non-pluripolar theory. The deeper positive-volume lifting argument of Lemma 22.1.10 also cites §18.1; its unreviewed analytic premises remain **external/conditional internal dependencies**, and must not be marked resolved. Any reference to excluded Demailly approximation or its dedicated Bergman/L²/OT/multiscale/positivity-loss programme is retained only as **deferred-by-user**; no work in that programme was undertaken.

**Proposed optional correction (not applied).** Insert a short remark after Definition 22.1.2: "For a fixed Kähler form \(\omega_0\), the sequence \(2^{-j}\omega_0\) is cofinal for the reverse order, so the inverse limit and volume can be computed on this sequence." Preserve the original all-forms definition, its permanent tag and the genuinely directed-index formulation.

**Affected dependents.** Definition 22.1.7, Lemma 22.1.10, Proposition 22.1.15, and later inverse-limit constructions in §22.1 may use this countable-coordinate reformulation. Nothing here verifies their nonlinear analytic conclusions. It does not license replacing arbitrary nonsequential nets elsewhere in Pome by sequences.

**Exact coverage:** selected new direct argument for §22.1.1, Definition 22.1.2, Definition 22.1.7, Lemmas 22.1.9–10 and Proposition 22.1.15, with context-only §§17.14.1/17.14.6. The whole 22.1 section has many other subsections (including valuations, DH and analytification) **not certified**. §22.1 was already partly sampled by earlier audit reports, so this run adds **0 first-visited numbered sections, 0 whole-section proof certifications, 0 fully certified transitive dependency chains**. The existing 25-chapter/747-numbered-section master matrix is retained unchanged; this report is the durable selected-coverage delta. No build, test, CI, website publication, source/main/body/registry or permanent-tag edit has been performed.
