# Support-family sharpness and infinite-dimensional Kummer semipositivity

**Checkpoint:** 2026-10-25 (Asia/Shanghai), 2026-10-24T23:03:27Z (UTC).  
**Reviewed integrated `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Starting audit head:** `8271f45fb6762fa2372d5c4e5d5cd072ee02bf60`.  
**Scope:** fresh selected proof-level reviews of §§10.27, 10.54–10.56; an explicit, separately identified recheck of §10.26. This is not a certification of any complete section, the rest of the collection, or all upstream dependencies. The author's deferred Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof programme was **not opened**.

## Finding POME-SUPPORT-ENLARGE-SHARP-001

**Status:** verified conditional deduction, **low** severity. The printed theorem is **correct**. The conclusion is a sharpness obstruction to omitting its support-enlargement hypothesis, not a counterexample to the theorem as stated.

**Precise source:** Theorem 10.56.2, source label `demailly-complex-geometry-3F06E0BE`, permanent tag `DE3B76CEB62B`, `docs/sections/spectral-sequences-support-and-cup-products--sheaf-cohomology-with-prescribed-supports/index.html`, blob `69cfb501098d00134ef6fe08d485e946af87fc76`, physical lines **7–20, 41–57** (definition of support family, enlargement, statement and proof); Theorem 10.56.1 label `demailly-complex-geometry-008F9010`, tag `391CCB0E8947`, lines **26–38** (flabby supported acyclicity). Internal crosschecks: Godement Theorem 10.43.5 tag `E24E008710DC`, `docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html`; soft-sheaf Theorem 10.44.7 tag `695AD5517AC4`, `docs/sections/sheaf-cohomology-and-acyclic-resolutions--soft-sheaves-and-paracompact-comparison/index.html`. These sections are used for the specified facts only.

**Construction.** Set `X=R`, `Z={0}`, `U=R\setminus Z`, and let `Phi_Z={emptyset,Z}` be the family of closed supports contained in `Z`. This family is **not enlargable**: no member of `Phi_Z` contains `Z` in its interior in `R`. Take `F=C_R`, the sheaf of continuous real-valued functions. It is soft on `R` and on `U`: a real-valued continuous function on a closed subset of a real interval extends across complementary intervals by linear interpolation (constant continuation on unbounded complementary intervals). This gives a direct extension argument without a hidden boundedness hypothesis.

For the iterated Godement resolution `C^q F=G^{q+1}F`, every term is flabby, and its open restriction is the Godement resolution of `F|_U` (Theorem 10.43.5). Hence, degree by degree, restriction gives the **short exact sequence of complexes**
[
0longrightarrowGamma_Z(X,C^ullet F)
longrightarrowGamma(X,C^ullet F)
longrightarrowGamma(U,C^ullet F|_U)
longrightarrow0.
]
The last arrow is onto because the Godement terms are flabby. The kernel consists exactly of sections supported in `Z` because `Z` is closed. Taking cohomology and using the ordinary acyclicity of the continuous-function sheaf on `R` and `U` yields
[
H_Z^0(mathbb R,F)=0,qquad
H_Z^1(mathbb R,F)simeq
rac{C(mathbb Rsetminus{0},mathbb R)}
{operatorname{res} C(mathbb R,mathbb R)},qquad
H_Z^q(mathbb R,F)=0quad(qge2).
]
The degree-zero group vanishes because a continuous function supported at one point vanishes identically. The class of `x\mapsto1/x` is nonzero. Thus a **soft** sheaf need not be `Phi`-acyclic when `Phi` is not enlargable.

Indeed the failure is maximally large as a real vector-space example:
[
oxed{dim_{mathbb R}H_Z^1(mathbb R,F)=2^{aleph_0}.}
]
For each `a` in `(0,1)`, the classes of `|x|^{-a}` are linearly independent: in a nontrivial finite combination, the term with largest exponent dominates as `x\to0`, so the combination does not continuously extend. Conversely continuous functions on the separable metric space `U` are determined by values on a countable dense subset, giving cardinality at most `|R|^{\aleph_0}=2^{\aleph_0}`, hence the stated upper dimension bound.

**Failure of supported lifting under a soft kernel.** Let `Q=GF/F`. Define a Godement section `b\in GF(X)` by the germ of `1/x` at every `x\ne0`, with zero germ at the origin. Its image `q\in Q(X)` vanishes on `U` but has nonzero stalk at zero, hence `supp(q)=Z`. If `q` had a lift `b'` in `GF(X)` supported in `Z`, then `b-b'` would be the Godement image of a **globally continuous** function agreeing with `1/x` on `U`, impossible. Thus the supported-surjectivity assertion of Theorem 10.56.2 would also fail without enlargement, although its ordinary non-supported analogue and the flabby-kernel version of Theorem 10.56.1 remain valid.

**Disposition / affected dependents:** No change to the theorem or the Godement construction is proposed. An optional sharpness example following Theorem 10.56.2 would prevent using soft-sheaf compact/support acyclicity for an arbitrary closed-point support family; this matters to the later compact-support comparison, local/cohomology-with-support arguments and duality applications. It does **not** invalidate the later compact-support results, because compact supports are enlargable in their locally compact hypotheses.

## Finding POME-KUMMER-INFINITE-SEMIPOSITIVE-001

**Status:** verified conditional deduction, **low** severity. **Not** a false statement or missing proof. It quantitatively strengthens the printed nonrigidity example.

**Precise source:** Proposition 10.27.2, source label `non-kahler-pluripotential-theory-FEDF8525`, permanent tag `6055AD1EB4F6`, and preceding Lemma 10.27.1, source `non-kahler-pluripotential-theory-FDC8007C`, tag `22EA1C593ACD`. Integrated `docs/sections/bott-chern-classes-and-singular-loci--nonrigid-classes-on-a-quotient-resolution/index.html`, blob `9ad1ad9323c3c53e9c1faec36877f911ac5f8b76`, lines **7–49** (resolution, geometric setup, admissibility) and **54–75** (proposition and proof).

**Claim.** In this fixed Kummer-surface example, the single irrational nef Bott–Chern boundary class `alpha` with `alpha^2=0` contains, for **each integer N>=1**, an injective affine image of an open `N`-dimensional real ball of smooth closed semipositive representatives. Every representative in these balls vanishes on a neighborhood of the sixteen exceptional curves and has pointwise square zero. This is more than just two distinct positive currents.

**Proof.** The printed construction fixes the irrational real parameter `a`, and associates to any even smooth circle function `h>=0`, of integral one and vanishing on a neighborhood of `(1/2)Z/Z`, the smooth semipositive form `T_h`. Its proof shows that all these forms represent the same `alpha`; if `k=h_1-h_2`, the even periodic solution of `f''=4 pi k` has derivative zero near the exceptional centers and descends to a global potential `G` satisfying `dd^cG=T_{h_1}-T_{h_2}`.

Choose an admissible `h_0` strictly positive on a pair of symmetric arcs away from `(1/2)Z/Z`. In the vector space of even smooth functions supported in those arcs and of mean zero, choose linearly independent `k_1,...,k_N`. This space is infinite-dimensional: select independently supported smooth bumps and take their even symmetrizations and independent integral-zero combinations. Shrink the coefficient ball around zero until
[
 h_{mathbf t}=h_0+sum_{j=1}^Nt_jk_jge0
]
for every coefficient vector in the ball; its evenness, integral one and vanishing near the exceptional points persist. By the cited proposition each `T_{h_t}` is smooth, closed, semipositive and in `alpha`; it has rank at most one on the smooth quotient locus and is zero near each exceptional divisor, so its wedge square is zero everywhere. If `T_{h_t}=T_{h_s}`, their lifts to the regular torus locus imply `h_t(y_1)=h_s(y_1)`, and linear independence forces `t=s`. Affine dependence on `h` is exact. Thus an open affine `N`-ball occurs for every `N`.

**Disposition / affected dependents:** Optional corollary after Proposition 10.27.2; no source, canonicalization or permanent-tag edit. This distinction matters when using nonrigidity of boundary classes and testing assertions of finite-dimensionality/uniqueness for smooth semipositive representatives. The irrationality and nefness conclusions retain exactly the printed hypotheses and their original proofs.

## Other actual proof checks and non-new historical item

- **§10.54**, integrated `docs/sections/spectral-sequences-support-and-cup-products--filtered-complexes-and-spectral-sequences/index.html`, blob `2d26dcf0ea764f1d8823bae057dc951063053a50`: checked representatives in Theorem 10.54.2 (source `demailly-complex-geometry-311B37F9`, permanent `E83B7568FE4B`, line 33), finite-filtration stabilization of Theorem 10.54.3 (source `demailly-complex-geometry-56791F90`, permanent `21231040599F`, line 72), and five-term edge reasoning in Theorem 10.54.7 (source `demailly-complex-geometry-B32921E0`, permanent `BD1FDFF09B89`, line 142). No new confirmed error; no unrestricted convergence inference.
- **§10.55**, integrated `docs/sections/spectral-sequences-support-and-cup-products--hypercohomology-and-direct-image-spectral-sequences/index.html`, blob `83ea6c60c0691a7e3559214e363361863f3ea2a2`: selected checks of Godement horizontal/vertical signs, two finite diagonal spectral sequences in Theorem 10.55.2 (source `demailly-complex-geometry-F6A52A0C`, tag `D461C5DFED48`, line 39), the augmentation normalization of Equation 10.55.4, and flabby direct-image/Leray comparison in Theorem 10.55.6 (source `demailly-complex-geometry-8B97C424`, tag `2CFDCB1083B2`, line 104). Exactness and cohomological identification were checked only as selected proof steps, not full certification of arbitrary direct-image applications.
- **§10.56**, the support-family definitions, Godement/flabby lifting in 10.56.1, the soft-support enlargement in 10.56.2, supported dimension shifting 10.56.3, locally compact neighborhoods 10.56.5, extension-by-zero 10.56.6, and selected compact-supported cochain steps 10.56.7/.9 were directly read. These latter results retain their distinct hypotheses; not all their derived-functor comparison and refinement details were certified. No outside topological cohomology theorem is imported as proof of the new example.
- **§10.26**, integrated `docs/sections/bott-chern-classes-and-singular-loci--rigid-boundary-classes-on-a-torus/index.html`, blob `0cd2a46d5f5aaceb809c5ef13b9a717c422a7212`, Theorem 10.26.1 tag `9A07C571BD3F` (source label `DA9C52EB`, line 14) and Examples 10.26.2/.3 tags `5B00F62ACA6B` and `87A3AA3B13FD` (lines 66,91), were reread. An initially considered Gromov–Hausdorff strengthening **was already logged** as `POME-TOR-FLAT-GH-001` on 20 October 2026, with the sharp rational example `POME-TOR-RATIONAL-DIAM-001`. Neither is reissued or represented as new progress; their prior statuses remain unchanged. No new §10.26 mathematical finding is registered.

**Coverage accounting:** §§10.27, 10.54–10.56 are first selected proof reviews in the 747-section matrix; §10.26 is a version-pinned recheck of a previously audited result, not a previously untouched section. Neither the entire cohomology/duality chain nor the Kummer construction's external topology is formally verified. Only audit Markdown is proposed for `review/mathematical-audit`; no edit to `main`, source, published reader, registry, tags, PRs, CI, tests, or website.
