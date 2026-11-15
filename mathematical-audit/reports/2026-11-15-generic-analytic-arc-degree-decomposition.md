# Generic-direction finite-cover decomposition of analytic arcs — 2026-11-15

**Finding:** `POME-ARC-GENERIC-DIRECTION-DEGREE-DECOMPOSITION-001`  
**Classification:** low / **verified conditional deduction**. The printed Proposition 9.5.2 and Corollary 9.5.3 remain correct; this is not a false theorem or a repaired error.  
**Scope:** selected integrated proof of Proposition 9.5.2 and both clauses of Corollary 9.5.3, with Proposition 9.5.1 and the finite-projection statement as explicitly conditional inputs. No complete-section certification.

## Pinned reading-edition anchors

- Reviewed **main**: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Physical file: `docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html`, Git blob `2c725646172203283ac4564bddd46213d9a75cbe`; section 9.5 permanent tag `2BDD13613B99`.
- **Proposition 9.5.2**: source label `foundations-of-pluripotential-theory:EFA18446`, permanent tag `1497A0492453`, statement physical line 41; original proof lines 46–50, especially the nonzero norm and discriminant product in lines 47–49.
- **Corollary 9.5.3**: source `foundations-of-pluripotential-theory:EE2F6014`, permanent tag `F7B8B4ADF874`, statement line 55 and proof lines 60–64.
- **Proposition 9.5.1**, used for its punctured-disc covering parametrization: source `foundations-of-pluripotential-theory:7EBE91CF`, permanent `A3A9384DC317`, statement line 11, proof lines 16–35. This statement was audited previously; its historical status is unchanged.
- Local finite-parametrization input: Theorem 9.3.4, permanent `833B11F874F9`; bounded holomorphic extension of the norm: Lemma 9.2.9, permanent `AA4164301998`. These are **internal upstream inputs**, not newly and transitively certified here.

## New precise strengthening

Let ((X,x)) be an **irreducible reduced** analytic germ of dimension (d\ge1); let (B\subsetneq (X,x)) be a proper analytic subgerm. Select the finite local parametrization used in the printed proof,
[
 \pi:(X,x)\longrightarrow (\mathbb C^d,0),
 \quad \pi^{-1}(0)=\{x\},
]
whose restriction above the complement of a holomorphic discriminant (δ) is an unramified covering of **degree (q\ge1)**.

There exists a **nonzero homogeneous polynomial (G_m\)** on (ℂ^d) such that, for **every** projective direction ([v]\in\mathbb P^{d-1}\setminus\{G_m=0\}), after shrinking the line disc (Δ_v), the punctured inverse image
[
 \pi^{-1}(\{tv:0<|t|<\rho_v\})
]
is a disjoint union of (ℓ_v) connected finite unramified coverings of the punctured disc, of positive degrees (e_1,\ldots,e_{ℓ_v}) satisfying the **exact identity**
[
 \sum_{i=1}^{\ell_v}e_i=q.
]
Each component has a holomorphic normalization parameter (γ_i:(\Delta,0)\to(X,x)), with
[
 \pi\circ\gamma_i(s)=v s^{e_i},\qquad
 \gamma_i(s)\in X_{\rm reg}\setminus B\quad(s\ne0),
]
after a harmless scaling of the parameter disc. Distinct components give distinct punctured images, and each point of a sufficiently small nonzero target line fiber is represented exactly once among the (γ_i) parameterizations. This is stronger than the existence of **one** avoiding arc in Proposition 9.5.2; it records all generic projected sheets and their ramification degrees.

This conclusion **does not** say that every direction works or that each (e_i=1). In particular, the projective direction exception is generally unavoidable.

## Proof (complete relative to the identified finite-projection inputs)

**1. Norm and a common exceptional polynomial.** The irreducibility and reducedness assumptions imply that the analytic germ (B\cup X_{\mathrm{sing}}) is proper. Choose a holomorphic germ (f) vanishing on it but not identically on (X). As in the integrated proof, on the (q)-sheeted unbranched projection locus define
[
 N_f(z)=\prod_{y\in\pi^{-1}(z)} f(y).
]
Local sheet permutations make (N_f) holomorphic off (δ=0); boundedness on a sufficiently small finite-projection representative and the codimension-one removable extension in Lemma 9.2.9 extend it holomorphically to the base. It is not identically zero: otherwise one sheet function would vanish on an open set, hence on the connected regular covering locus and by density on the irreducible germ. Thus (g=δ N_f) is a nonzero holomorphic germ, and its first nonzero homogeneous Taylor term (G_m) is a nonzero polynomial.

**2. Uniform exclusion along each chosen line.** If (G_m(v)\ne0), then
[
  g(tv)=t^m(G_m(v)+O(t))
]
and the factor in parentheses is nonzero for (0<|t|<\rho_v). Hence the inverse-image line over the puncture stays outside the ramification locus (δ=0) and outside ({f=0}\supset B\cup X_{\rm sing}). Since ({G_m=0}) is a proper homogeneous algebraic set, the admissible directions form a nonempty Zariski-open subset of projective space (the sole direction in (d=1) is admissible).

**3. Exact finite-cover partition.** The finite projection restricted to this line is a proper unramified covering with (q) points in every nonzero fiber. It has finitely many connected components (Y_i^*); the restriction on each is a connected covering of degree (e_i\ge1). A single fiber is partitioned into its component fibers, proving (Σ_i e_i=q). No sequential compactness, limit interchange or generic-flatness assertion is used.

**4. Holomorphic normalization and the center.** For a connected (e)-sheeted covering of a punctured disc, its monodromy permutation of the fiber is a **single (e)-cycle**: connectedness makes the cyclic monodromy action transitive. Lifting the exponential map from a left half-plane and dividing by the (2\pi i e)-period yields a holomorphic biholomorphism from a punctured parameter disc to the covering, with projected map (s\mapsto s^e v). This is precisely the elementary covering argument written in Proposition 9.5.1, physical lines 19–33, applied to **each component** rather than only to one curve branch. The coordinates of the lifts are bounded by the chosen bounded representative. The one-variable removable-singularity theorem extends each lift to (s=0); the only point in the central fiber is (x), so every (γ_i(0)=x). Over the puncture all images lie in (X_{\rm reg}\setminus B). Distinct component images are disjoint, and the normalizing maps enumerate the (q) points exactly.

This completes the conditional strengthening.

## Sharp examples and limits

- **Ramification may be total.** The irreducible plane germ (z^q=x^{q+1}), (q\ge2), with projection (π(x,z)=x), is normalized by (s\mapsto(s^q,s^{q+1})). Its generic projected degree is (q), but the punctured inverse image is connected and its **single** arc has exponent (e_1=q).
- **All generic sheets may be separate arcs.** The irreducible hypersurface germ (z^q=x^{q-1}y\subset\mathbb C^3), (q\ge2), with projection (π(x,y,z)=(x,y)), has degree (q). On a line ((x,y)=(a t,b t)) with (ab\ne0), its (q) branches are (z=ζ(a^{q-1}b)^{1/q}t) for the (q)th roots of unity (ζ); thus (ℓ=q) and all (e_i=1). The germ is irreducible because (z^q-x^{q-1}y) is primitive and linear in (y).
- **Not every direction avoids the specified subgerm.** In smooth (X=\mathbb C^2), let (B={x=0}) and take identity projection. The line direction (v=(0,1)) lies entirely in (B); no avoiding arc projects to this line. The generic-direction qualification is essential.

## Independent original-proof checks

1. Proposition 9.5.2 lines 47–49: its use of the **nonzero norm** and a line avoiding (g=0) is justified only because the germ is irreducible and (f\not\equiv0) on its connected covering locus. Both hypotheses are present; nothing is inferred from a mere generic degree number.
2. Corollary 9.5.3 lines 60–63: the first assertion applies arc selection **separately to each irreducible branch**, as required. For the second, the nonisolated locus (K_+) is closed in compact (K); a positive-dimensional branch near a point of (K_+) remains in (K_+), so the maximum of (|z|^2) over (K_+) is legitimately tested on the analytic arc. With (Δ|\gamma|^2=4\sum|\gamma_j'|^2), the maximum principle forces constant (γ). No missing assumption or incorrect sign was found in these inspected steps.
3. The proof of finite-projection/covering normalization upstream (9.3.4 and 9.5.1) is **not** re-certified in full in this run. Previously logged concerns elsewhere in the project remain unchanged.

## Status, impact, and proposed edit

**Status:** verified conditional deduction / low. **No confirmed error** or new source proof gap in 9.5.2–3; proof above is complete relative to the named finite-projection and normalization inputs. The result can optionally be added as a clearly labeled corollary immediately after Proposition 9.5.2, without touching the original proposition or its historical attribution. Affected uses: analytic curve selection avoiding singular loci, testing local maximum principles on branches, and local finite-map degree bookkeeping. It does **not** establish flatness, a global degree theorem for arbitrary maps, or a generalized current pushforward formula.

**Audit boundary:** no Demailly approximation, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work was read or advanced. All prior notes on those programmes remain **deferred-by-user**, not resolved.
