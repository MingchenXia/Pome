# Actual quotient topology in completed Tor and reduced cohomology

Date: 2026-11-27. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit parent: `632197e22edfa77439ca679a3434cf0449afbd2f`.

## POME-TOR-HAUSDORFF-INDEPENDENCE-001

Severity: low. Status: verified conditional deduction (not a refutation). Theorem 9.44.3 (source 7B796A7C, permanent C8C2118EE2C8), physical lines 40–69, and Theorem 9.45.1 (source B74DAFC0, permanent ED1150490F04), lines 7–61. Their actual-image convention and the separate Hausdorff requirement in transversality are essential even when every positive Tor group vanishes.

Let S=O(C), with its nuclear Fréchet compact-open topology (2.13.4). In Taylor coordinates at zero use equivalent seminorms p_R(x)=sum_{j>=0}|x_j| R^j for R>=1 (Cauchy estimates on a larger disk prove continuity; the supremum on the disk is at most p_R). Let lambda_j=exp(-j^2), and D multiply the jth coefficient by lambda_j. D is continuous and injective; its range contains every polynomial and so is dense. It is not onto: y_j=exp(-j^2/2) defines an entire function, but its only possible preimage has coefficients exp(j^2/2) and is not entire.

Take A=O(C), with coordinate t, and define the module E=S by (a.x)_j=a(lambda_j)x_j. This is a unital associative jointly continuous action, since p_R(a.x)<=sup_{|t|<=1}|a(t)| p_R(x). Take F=C with action a(0). The strict free resolution 0 -> A --t--> A -> F -> 0 is exact: division by t is entire for functions vanishing at 0, the kernel is closed, and open mapping applies. By the actual free-factor identity and resolution comparison in 9.44.2–3, its balanced tensor with E is the two-term complex E --D--> E. Thus Tor_q^A(E,F)=0 for every q>=1, whereas Tor_0=E/D(E) is nonzero with the indiscrete quotient topology (every nonempty saturated open subset contains every coset because D(E) is dense). The two modules are not transverse. Replacing the relation image by its closure would instead give the zero space and would erase the entire algebraic tensor quotient. This example uses only nuclear Fréchet modules, not Banach modules outside the printed hypotheses.

A separate all-degree example uses A_2=C[e]/(e^2), F=C with e acting by zero, and E=S direct sum S, with e acting as N(x,y)=(0,Dx). The action is jointly continuous, and N^2=0. The periodic strict free resolution of F uses multiplication by e in every positive degree; exactness follows from ker(e)=im(e)=Ce. After balanced tensor its maps are N. Consequently Tor_0 is S direct sum (S/D(S)), with the product quotient topology; every Tor_q for q>=1 is ker(N)/im(N)=S/D(S), with its nonzero indiscrete topology. In particular reduced Tor vanishes in every positive degree while ordinary Tor does not. This is not the earlier 2026-11-13 finite-dimensional residue/residue calculation POME-TOR-TRUNCATED-POLYNOMIAL-INFINITE-TAIL-001: the new point is actual nonclosed relation and boundary images and independent necessity of the two transversality conditions.

Suggested addition: insert the first example after the definition at §9.45 line 7 and the second after §9.44.3 line 52. Do not alter the theorem or replace any actual image by a closure. Affected downstream scope: §9.45.1 base-change and exactness arguments require Hausdorffness independently of higher Tor vanishing; §9.45.4 proves both conditions for its analytic restriction, so neither example contradicts that proposition. No claim of an error in these results.

## POME-NUCLEAR-REDUCED-TENSOR-001

Severity: low. Status: verified conditional deduction. Proposition 9.41.6 (source D01CAEC4, permanent 574665EBC99C), lines 110–121, assumes closed boundaries for its ordinary cohomology formula. Without that assumption there is a canonical topological formula for reduced cohomology in each degree:
```tex
\overline H^q(H\widehat\otimes C^\bullet)
\simeq H\widehat\otimes \overline H^q(C^\bullet),
\qquad
\overline H^q(C^\bullet)=\ker d^q/\overline{\operatorname{im} d^{q-1}}.
```
Here H is nuclear Fréchet and the complex has Fréchet terms and continuous differentials; no boundedness assumption on the degree range is needed for a single degree. Proof: let Z=ker d^q and B=im d^{q-1}, and let K be the closure of B in C^q (equivalently in Z). The kernel assertion of 9.41.1 identifies tensor cycles topologically with H completed tensor Z. The image of the tensored previous differential lies in the closed subspace H completed tensor K, by factoring d^{q-1} through K and strict exactness for the inclusion K -> C^q. Conversely this image contains every elementary tensor h tensor b with b in B. For every k in K the latter tensors approximate h tensor k by continuity; finite sums and then completion give density in H completed tensor K. Thus the closure of the actual tensor boundary image equals H completed tensor K, without asserting equality of actual images. Strict ordinary tensor exactness for 0 -> K -> Z -> Z/K -> 0 gives the displayed topological quotient formula. On elementary classes it is the canonical map. All approximation assertions are topological density assertions, not a choice of simultaneous limit or a sequential compactness claim.

This supplies a reduced alternative to the one-factor proposition; it does not assert an unrestricted two-complex reduced Künneth theorem. In particular the finite-dimensional (ordinary) hypothesis of 9.41.10 has not been replaced. Suggested addition after Proposition 9.41.6; downstream use must specify which cohomology is intended.

## Coverage and dependencies

Paths below are on the reviewed main, not the audit branch. All mathematical paragraphs of the following integrated sections were directly read (including proof bodies; physical line ranges exclude navigation).

| Section | Exact path | Blob | Lines | Review |
|---|---|---|---|---|
| 9.41 | docs/sections/analytic-tensor-products-and-proper-direct-images--completed-tensors-gluing-and-cohomology/index.html | c3c927f7b2b5b9adb40857b3fd11ef8680c5888e | 7–200 | Whole direct conditional: contractions, product seminorms, gluing, both Künneth arguments and connecting-map topology. Finite diagonals and closedness checked; no infinite totalization inferred. |
| 9.43 | docs/sections/analytic-tensor-products-and-proper-direct-images--coherent-products-and-nuclear-analytic-modules/index.html | 057ae61b984be97c533852e3be4f7964799be4e0 | 7–58 | Whole direct conditional: nonreduced product ideals, right exactness of presentations, filtered stalk colimits, joint action and Banach-link factorization. Coherent vanishing and local presentation theorems not independently proved here. |
| 9.44 | docs/sections/analytic-tensor-products-and-proper-direct-images--balanced-tensors-and-the-standard-resolution/index.html | 33c9658f92156b3f0676ea53e77715ef7fd06f49 | 7–69 | Whole direct conditional: unit-insertion relation image equals kernel, bar contraction, reversal exponent q(q+1)/2, strict tensor sequences, actual quotient homology comparison. |
| 9.45 | docs/sections/analytic-tensor-products-and-proper-direct-images--transversality-and-analytic-restriction/index.html | eb6d9e770e09bcc75557965a42a8d155ef780f7e | 7–79 | Whole direct conditional: actual-image balanced associativity, bounded-above backward induction, cone signs, fixed compact set in the coherent free-resolution construction. |

Checked statements of 2.12.5 (cohomological openness, including non-Hausdorff quotient) and 2.13.4–5 (nuclear holomorphic function spaces and strict completed tensor exactness). Dependencies on 9.42, 9.51, 10.43.15 and the upstream Oka/coherent vanishing arguments remain conditional; no new full proof-chain certification. The finite-diagonal comparison, free-factor formulas and continuity of connecting maps are consistent with these inputs. The historical first-visit status is unreconciled; earlier selected visits and periodic-Tor work are preserved. No new confirmed printed error or demonstrated proof gap.

The live chapter 9 TOC was read on main; the existing matrix has 747 numbered rows, of which chapter 9 has 77. The four sections above change only their current direct coverage status; the remaining rows retain their prior status. Other chapters were not exhaustively re-read this run.

Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain deferred-by-user, not resolved or certified. No tests, build, CI, publication, main, source, registry or tag edits.
