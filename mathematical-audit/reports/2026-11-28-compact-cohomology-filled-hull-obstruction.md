# Compact restriction in degree n-1: exact filled-hull obstruction

Date: 2026-11-28. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit branch only; no changes to the reading edition or source registries.

## Scope and anchors

- `docs/sections/spectral-sequences-support-and-cup-products--orientation-classes-and-cap-duality/index.html`, blob 88ed77871455097c456cafaba2cca34986f3a3fb, all mathematical lines 7–160. Lemma 10.71.1 (source 4F144FDE, permanent 603753CCA942), Lemma 10.71.2 (7313C33C / 3C7389B6FCBC), cap formulas 10.71.3–4 (2EEBE145 / 5E4EEAACF262 and 90E0D055 / 6F3FE0A6CE1E), Theorems 10.71.5–7 (87D6C3E7 / 9EC6A8A9270A; 63D3EBF4 / 61D073B63D13; 726E10E1 / 211197321C0C).
- `docs/sections/spectral-sequences-support-and-cup-products--the-dualizing-complex-and-cohomological-duality/index.html`, blob 6b6c9fc091feb1d437ae0e3858f32feb11cba68a, all mathematical lines 7–143. Propositions 10.72.1–2 (11705A2E / 9E818639205F; AA116797 / 13DBDC23AA55), Theorem 10.72.3 (14A61A97 / 3968AEF4C8FE), Corollary 10.72.4 (3F7B3578 / 9C9125F4F2EE), Proposition 10.72.5 (5FB0B8F3 / B7AF8FB473E5).
- `docs/sections/general-complex-cohomology-and-modifications/index.html`, blob 09afe450589f7169d2f2296d0606882b11efec60, entire introductory convention at lines 6–8; not a review of §§10.84–87.
- Selected dependency: `docs/sections/convex-neighborhoods-and-coherent-vanishing--convexity-and-cohomology-in-the-top-degrees/index.html`, blob e43441b6bf9c098ee7222415cb30c06331efc8ee, lines 63–77, Lemma 9.52.5 (5D86F0BB / 4A19B00897C5).
- Selected dependency: `docs/sections/spectral-sequences-support-and-cup-products--injective-modules-and-extension-modules/index.html`, blob a26517e086ac8ed8c5d590cad04b203a2f602f99, lines 126–151 (Theorem 10.68.6 statement and beginning of the two-row calculation, 9119DC26 / 04CB406A4809). Its full proof chain is not re-certified.
- §10.71.7 supplies the bounded soft resolution and the inverse sequence argument; references to 10.60.1, 10.61.7–8, 10.62.2 and 10.70 remain prerequisites rather than new independent certifications.

## POME-COMPACT-CAP-DUALITY-FILLED-HULL-OBSTRUCTION-001

Severity low; status **verified conditional deduction**, not a false theorem or a demonstrated proof gap. Proposed optional corollary after 10.71.7. Conditional on the internal compact cap duality, its restriction naturality, the filled exhaustion lemma and the soft resolution inputs explicitly used in 10.71.7.

Let X be a connected noncompact paracompact real n-manifold without boundary (so n>=1), A any local R-module system in the conventions of §10.71, and K any compact subset. Write B = tau_X tensor A. Let F(K) be the set of relatively compact connected components G of X minus K, and H = K union all such G. By Lemma 9.52.5, H is compact and every component of X minus H has noncompact closure.

There is an exact sequence, natural in A,

    H^{n-1}(X,A) -> H^{n-1}(K,A|K)
       -> direct sum_{G in F(K)} H_0(G,B|G) -> 0.

Here the middle arrow is compact cap duality D_K followed by the relative boundary to H_0(X minus K,X minus H;B), then the canonical component decomposition. Fix the sign convention of D_K from 10.71.6. No finiteness of the set F(K), stalks, or homology groups is required. The direct sum, not product, is essential.

### Proof

1. Apply the countability argument and filled compact exhaustion in 10.71.7 to obtain E_j exhausting X, with H contained in the interior of E_1, E_j contained in the interior of E_{j+1}, and all complementary components of each E_j having noncompact closure. Put E_0=H. For every j>=0, each component of X minus E_j meets X minus E_{j+1}: otherwise it is contained in the compact E_{j+1} and has compact closure. Since the complements are open manifolds, their components are path connected. With any local coefficients B, transport along such a path represents the same H_0 class; hence H_0(X minus E_j,X minus E_{j+1};B)=0. This is the transport argument at lines 151–157 of 10.71.7, including j=0.

2. The long exact triple sequence for X minus E_{j+1} contained in X minus E_j contained in X now shows that H_1(X,X minus E_{j+1};B) -> H_1(X,X minus E_j;B) is surjective. By 10.71.6, the restrictions H^{n-1}(E_{j+1},A) -> H^{n-1}(E_j,A) are surjective. Restriction of A to each compact set is understood.

3. The surjections just proved permit recursively lifting any class on E_0 to a compatible sequence of classes on all E_j. Let L^bullet be the soft resolution used in 10.71.7, and C_j = Gamma(E_j,L^bullet|E_j). Its restrictions are surjective in every degree, by softness, and compute cohomology on each compact set. Its limit is Gamma(X,L^bullet) by gluing over the interiors. Consequently there is a short exact sequence of complexes

       0 -> Gamma(X,L^bullet) -> product_j C_j
         --(1-s)--> product_j C_j -> 0,

   where s is restriction from the next index. Surjectivity degreewise follows by recursive lifting, not by an arbitrary inverse limit exactness assertion. Products of module sequences are exact. The long exact sequence in cohomology therefore maps H^{n-1}(X,A) onto the kernel of 1-s on product_j H^{n-1}(E_j,A). The chosen compatible sequence is in that kernel. Thus restriction H^{n-1}(X,A) -> H^{n-1}(H,A|H) is surjective. This establishes the image assertion even for non-finitely-generated modules; it is not a sequential compactness argument.

4. Put P=X minus K and Q=X minus H. The triple sequence of Q contained in P contained in X contains

       H_1(X,Q;B) -> H_1(X,P;B) -> H_0(P,Q;B) -> H_0(X,Q;B).

   The last group is zero because X is connected, Q is nonempty (H is compact and X noncompact), and local coefficients can be transported from every point to Q. Thus the preceding boundary is onto, with kernel exactly the image from H_1(X,Q;B). By compact cap duality and its restriction naturality, the first arrow corresponds to restriction from H to K. Step 3 identifies its image with the image of restriction from X to K.

5. P is the disjoint union of its open connected components. Q is exactly the union of those not in F(K). Every singular simplex lies in one component; the singular chain complex with local coefficients is the direct sum of component complexes, and the relative quotient deletes precisely the summands in Q. Hence H_0(P,Q;B) is canonically the stated direct sum. This proves the exact sequence.

### Consequences and endpoints

Each H_0(G,B|G) is the coinvariant module of the transported fiber, by the path and loop calculation in Corollary 10.72.4, lines 106–108. In particular, if X is oriented and A is constant with nonzero fiber L, each hole contributes one copy of L. For arbitrary X one can instead take A=tau_X tensor the constant nonzero module L; the double orientation twist is trivial and again every hole contributes L. Thus absence of relatively compact complementary components is equivalent to surjectivity for every local coefficient system. For a fixed nontrivial local system, the coinvariants can vanish even when holes exist; the exact sequence is the correct criterion, not an unconditional converse for each fixed A. For K empty both the middle and obstruction terms vanish. For n=1 this says that locally constant values on K extend precisely when the transported differences across bounded complementary intervals vanish; e.g. X=R, K={0,1}, L constant, the cokernel of diagonal L -> L^2 is L.

No smoothness, local contractibility or singular cohomology comparison of K is required. For infinitely many holes the obstruction is still a direct sum, because a relative singular chain is finite. The result does not assert surjectivity in other degrees, nor a canonical splitting. No changes to 10.71.7 or its hypotheses are needed; this is an optional consequence and may be useful wherever compact restrictions or top-degree vanishing are used. No directly affected theorem requiring a correction has been identified.

## Direct checks and limitations

In §10.71, checked the radial comparison of convex compact pairs, finite-union relative Mayer–Vietoris uniqueness and existence, determinant orientation and reflection sign, cap boundary identity with sign (-1)^p, front/back evaluation, the open-union connecting sign (-1)^{p+1}, the compact-union connecting sign (-1)^q in the stated conventions, neighborhood direct limits and the degreewise surjective product-complex argument. The passage to compact K uses sheaf cohomology, not an unjustified singular comparison on K.

In §10.72, checked that the compact-section extension-by-zero sequence uses actual germs on the closed complement and compact support, injectivity gives flabby Hom sheaves, the two-row differential has opposite mixed signs, the Ext term in degree zero vanishes by the degree bound, the orientation and contravariant coefficient transports, and the role of the Ext hypothesis in comparing the ordinary Hom complex with the two-row derived complex. The degree-q pairing sign epsilon_q=(-1)^{q(q+1)/2} satisfies epsilon_{q+1}=(-1)^{q+1}epsilon_q and (-1)^{q+1}epsilon_{q+1}=epsilon_q as used in lines 126–140. The compact-first cap convention remains distinct from the raw dualizing-complex edge convention. The noncanonical splitting is conditional on 10.68.6. No new confirmed printed error or demonstrated gap in these selected arguments.

Coverage: two whole direct conditional mathematical sections, one whole introductory conventions section, two selected internal prerequisites. Legacy history unreconciled; no historical first-visit assertion. Zero newly certified complete transitive proof chains. No Demailly approximation, dedicated Bergman/L2/OT, multiscale or positivity-loss work; these remain deferred-by-user. No build, test, CI, publication or production edit performed.
