# Complete filtrations with finite-page degeneration: bounded boundary loss

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit only; no production edits.

## POME-SPECTRAL-COMPLETE-FILTRATION-BOUNDED-LOSS-001

Severity low; status **verified conditional deduction**, not a false printed theorem. Theorem 10.54.3 correctly requires degreewise finite filtrations for its stated automatic convergence. The following gives a different sufficient condition, with a sharp quantitative primitive estimate. No claim that completeness alone gives finite degeneration.

Integrated anchor: `docs/sections/spectral-sequences-support-and-cup-products--filtered-complexes-and-spectral-sequences/index.html` (blob 2d26dcf0ea764f1d8823bae057dc951063053a50), physical lines 7–112; page construction Theorem 10.54.2 (source tag 311B37F9, permanent E83B7568FE4B), graded cycle/boundary quotient and isomorphism lines 62–68, convergence Theorem 10.54.3 (source tag 56791F90, permanent 21231040599F), equation 10.54.4 (B14FBC5EE8B8). The tail counterexample at line 112 is valid, but its direct-sum filtration is not complete.

### Statement

Let \(K^\bullet\) be a cochain complex of modules with an integer-indexed decreasing filtration by subcomplexes, exhaustive, separated and complete in each degree, meaning \(K^n \simeq \varprojlim_{p\to+\infty} K^n/F^pK^n\) canonically. Suppose for some integer \(R\ge1\) every page differential \(d_r\), \(r\ge R\), vanishes in all bidegrees. Use exactly the page convention of 10.54.2. Then:

1. Every element of \(Z_R^{p,n}\) has a genuine closed representative with the same image in \(F^pK^n/F^{p+1}K^n\).
2. For every boundary \(y\in F^pK^n\cap dK^{n-1}\) there is a primitive \(v\in F^{p-R+1}K^{n-1}\). Equivalently
   \[
   F^pK^n\cap dK^{n-1}=F^pK^n\cap d(F^{p-R+1}K^{n-1}).
   \]
   The loss \(R-1\) is optimal uniformly over such complexes.
3. The induced filtration on \(H^n(K)\) is exhaustive, separated and complete, and the canonical associated graded is \(E_R^{p,n-p}\).
4. A filtered cochain map between two complexes satisfying these hypotheses that induces an isomorphism on a page at or before a common finite collapse page induces a filtered isomorphism on cohomology. It need not give a splitting of the filtration.

### Proof

Write \(\overline Z_r^{p,n}\) and \(\overline B_r^{p,n}\) exactly as at line 62: they are images in the graded module of \(Z_r^{p,n}\) and \(F^pK^n\cap dF^{p-r+1}K^{n-1}\), respectively. In particular \(\overline B_r\subset\overline Z_{r+1}\) since the boundary has an actual closed representative. The isomorphism in lines 65–68 identifies the graded cycle drop with the graded boundary increase. Under \(d_r=0\) both stabilize: indeed, for \(x\in Z_r^{p,n}\), the vanishing of its page differential means \(dx\) has its leading graded term in \(\overline B_r^{p+r,n+1}\); the image of all such derivatives is \(\overline B_{r+1}^{p+r,n+1}/\overline B_r^{p+r,n+1}\) by the displayed isomorphism. Thus for all \(r\ge R\) the two graded subgroups are equal to those at \(R\).

**Closed lifts.** Start with \(x_R=x\in Z_R^{p,n}\). Given \(x_r\in Z_r^{p,n}\), \(dx_r\) has leading graded term in \(\overline B_{r+1}^{p+r,n+1}=\overline B_R^{p+r,n+1}\). Choose \(b_r\in F^{p+r-R+1}K^n\) with \(db_r\in F^{p+r}K^{n+1}\) and \(dx_r-db_r\in F^{p+r+1}K^{n+1}\). Set \(x_{r+1}=x_r-b_r\). Each correction lies in \(F^{p+1}\), and its filtration tends to infinity. Completeness gives \(x_\infty=x-\sum_{r\ge R}b_r\) (partial sums are eventually constant modulo each \(F^a\)). Since the differential preserves the filtration, \(dx_\infty\in\bigcap_a F^aK^{n+1}=0\). The leading graded term is unchanged. This uses an actual convergent correction series, not an unjustified interchange of page limits.

**Bounded primitive loss.** Choose any primitive \(v\) of \(y\), lying in some \(F^a\) by exhaustiveness. If \(a<p-R+1\), then \(p\ge a+R\), so \(v\in Z_R^{a,n-1}\). Subtract its actual closed lift with the same leading graded term, leaving a primitive in \(F^{a+1}\). Repeat only finitely many times until filtration \(p-R+1\) is reached. The reverse inclusion is tautological. For sharpness over a field take \(K^0=ke,K^1=kf,de=f\), with \(e\) of filtration weight 0 and \(f\) of weight \(R-1\) (a vector of weight \(w\) belongs to \(F^p\) exactly for \(p\le w\)). This finite filtration has its only nonzero page differential at \(r=R-1\) (including \(d_0\) when \(R=1\)), so \(E_R=0\). The boundary \(f\in F^{R-1}\) has no primitive in \(F^1K^0\).

**Associated graded.** Actual cycles surject onto \(\overline Z_R\) by the first step. An actual cycle whose leading term belongs to \(\overline B_R\) differs from a boundary by an actual cycle in \(F^{p+1}\), hence defines zero in \(\operatorname{gr}_F^pH^n\). Conversely if a cycle in \(F^p\) has cohomology class represented by a cycle in \(F^{p+1}\), their difference is a boundary in \(F^p\). By the bounded-loss estimate its leading term is in \(\overline B_R\). This proves the canonical identification using 10.54.4, with no choice of a section of the graded quotient.

**Separatedness.** In degree \(n\), the image of \(d\) is closed in the filtration topology: if \(z\) is in its closure, for integers \(j\ge0\) choose boundaries \(y_j\) with \(z-y_j\in F^jK^n\). Then \(y_{j+1}-y_j\in F^jK^n\) is a boundary. Lift it to \(v_j\in F^{j-R+1}K^{n-1}\) by the estimate. Choose any primitive \(v_*\) of \(y_0\). Completeness supplies \(v=v_*+\sum_{j\ge0}v_j\). By filtration continuity and separatedness \(dv=z\). Now a class represented by a cycle \(z\) in every induced \(F^jH^n\) has \(z\) in the closure of the boundaries: subtract a cycle in \(F^j\) representing that class. Thus its class is zero.

**Completeness.** Given compatible classes in \(H^n/F^jH^n\), \(j\ge0\), choose representatives \(h_j\in H^n\); then \(h_{j+1}-h_j\in F^jH^n\), with actual closed representatives \(c_j\in F^jK^n\). Choose a cycle \(c_*\) for \(h_0\). The convergent sum \(c_*+\sum c_j\) is a cycle realizing all compatible residues, since each \(F^j\) is closed (it is an open subgroup in the filtration topology). Separatedness gives uniqueness. Exhaustiveness follows from that on \(K\).

**Comparison.** Naturality of 10.54.2 propagates the page isomorphism to a common collapse page, hence to the associated graded of the complete separated exhaustive cohomology filtrations. Such a filtered map is a filtered isomorphism: for any target in \(F^p\), lift its leading term from the source \(F^p\), and lift successive errors from \(F^{p+1},F^{p+2},\ldots\). Completeness and separatedness give a preimage in \(F^p\). For injectivity, a kernel element starts in some \(F^p\), and graded injectivity forces it into every higher filtration term. This also proves the inverse preserves the filtration.

All arguments are purely algebraic in the printed page convention. The adjacent finite-filtration proof remains correct. The example at line 112 completes to a product of coefficient spaces, where the triangular difference map \(de_i=f_i-f_{i+1}\) is invertible by finite partial sums at each coordinate, consistent with the new result. No derived inverse-limit theorem is invoked.

**Proposed correction/addition:** optional proposition following the warning at line 112, keeping the finite-filtration theorem and warning unchanged. Affected dependents 10.54.6–7 and 10.55.2, 10.55.6 use genuinely finite diagonal filtrations and need no repair. The new statement could be used in a later completed-complex construction only after its completeness, exhaustiveness and global finite-page collapse are independently checked.

## Additional direct coverage (conditional on existing internal inputs)

All mathematical paragraphs in the following three current integrated sections were read. Historical first visits are not asserted, since older records are not fully reconciled.

- **10.54**, path/blob above, physical lines 7–168. Checked page denominators and incoming boundary indices; finite stabilization uses degrees \(n-1,n,n+1\); exactness of the five-term sequence and distinct top/bottom edge page ranges; Frölicher convergence uses finite bidegrees and asserts no degeneration. The earlier November 8 late-transgression example is distinct and not counted again.
- **10.55**, `docs/sections/spectral-sequences-support-and-cup-products--hypercohomology-and-direct-image-spectral-sequences/index.html`, blob 83ea6c60c0691a7e3559214e363361863f3ea2a2, lines 7–170. Checked 10.55.1 (486AE7A0/C081C1E12790) shift conjugation by \((-1)^{sp}\); 10.55.2 (F6A52A0C/D461C5DFED48) finite diagonals for bounded below complexes and row sign; 10.55.3 (6F97C2F4/D8E20B32F22B) augmentation comparisons; (10.55.4) (9AECA85DAE24) zigzag sign \((-1)^{n(n+1)/2}\); 10.55.6 (8B97C424/2CFDCB1083B2) stalk colimits, flabby direct-image resolution, naturality and the adjunction counit edge identification. No fiber-cohomology identification is asserted. Conditional on 10.43.3/.5/.7/.8 and the exactness of inverse image; not a new transitive proof certificate.
- **10.56**, `docs/sections/spectral-sequences-support-and-cup-products--sheaf-cohomology-with-prescribed-supports/index.html`, blob 69cfb501098d00134ef6fe08d485e946af87fc76, lines 7–198. Checked 10.56.1 (008F9010/391CCB0E8947) coordinate lifts and exact-support flabby lift by maximal extension; 10.56.2 (3F06E0BE/DE3B76CEB62B) soft lift with enlarged support; 10.56.3 (0AC2892D/7C0750CA5296) positive connecting convention; 10.56.5 (8018B539/899BD7174FB8) compact-neighborhood and annular refinement; 10.56.6 (D06C7345/984908A81943) open extension/closed restriction and Mayer–Vietoris signs; 10.56.7 (D932D1CC/2E236442C324) compact closure and directed union; 10.56.9 (20E574B0/C9EFB9BEE0D7) finite support under locally finite refinement, partition contraction, coefficient lift after refinement and dimension shifting. Conditional on 10.43.14–16 and 10.44.4/.7/.9/.11/.12; these upstream proofs were not freshly certified here. In particular no assertion that open subspaces of arbitrary paracompact spaces are paracompact is needed.

## Coverage and exclusions

Three whole direct conditional sections, one new conditional theorem, zero newly confirmed printed errors, zero demonstrated proof gaps, zero complete transitive certificates. Current actual contents and existing matrix have the same 747 section identifiers with no duplicates. Excluded Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain deferred-by-user, not resolved. The historical cohomology source attribution is unchanged. No software tests, builds, CI, publication or production/registry/tag edits.
