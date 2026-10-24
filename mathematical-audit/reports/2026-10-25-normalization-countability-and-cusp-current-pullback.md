# Normalization countability proof-step defect and current pullbacks on the cusp

Audit date: 2026-10-25 (Asia/Shanghai). Reviewed immutable Pome main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Starting review branch: **640c02dd3371f29da4a372fac6fc0cec2a15d0fd**.

## Scope and pinning

The following **integrated reading-edition sources**, not merely their parent manuscripts, were read. The physical line numbers refer to the pinned main HTML blobs:

| Section | Exact main file and blob | Selected physical HTML lines and stable entries |
| --- | --- | --- |
| 9.4 | docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html; **06439f43d1ce8e83d2529682c9a630bffa3d9c22** | Definition of reduced complex space, line 10; Proposition 9.4.3, source foundations-of-pluripotential-theory-AC231B8D, permanent **36422A732754**, lines 56–79; Lemma 9.4.4, source foundations-of-pluripotential-theory-E60680A7, permanent **D73CC9F08C05**, lines 87–108; Theorem 9.4.6, source foundations-of-pluripotential-theory-7042BB57, permanent **12A47DB401E2**, lines 142–157. |
| 9.5 | docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html; **2c725646172203283ac4564bddd46213d9a75cbe** | Proposition 9.5.1, source foundations-of-pluripotential-theory-7EBE91CF, permanent **A3A9384DC317**, lines 11–35; Lemma 9.5.5, source foundations-of-pluripotential-theory-CB1EA559, permanent **776A532CD79E**, lines 84 onward, dependency context only. |
| 5.5 | docs/sections/complex-differential-forms-and-positive-currents--holomorphic-zeros-and-the-poincare-lelong-formula/index.html; **4231a246a84f17c3808a6f3164644f931aa0c654** | Weierstrass and slicing, lines 11–108; Theorem 5.5.6, source foundations-of-pluripotential-theory-09CD57CC, permanent **8D4BA339507E**, lines 162–184. |
| 5.6 | docs/sections/complex-differential-forms-and-positive-currents--maps-of-currents-and-local-mass/index.html; **1d9d81f147a96878236944fcae54aeb8f6f58098** | Pushforward and submersion pullback, lines 11–105; Proposition 5.6.5, source foundations-of-pluripotential-theory-D64C5493, permanent **6DAA1675792B**, lines 111–125; Example 5.6.6, source foundations-of-pluripotential-theory-7125710A, permanent **5A6B397A8B30**, line 131. |
| 5.2 | docs/sections/complex-differential-forms-and-positive-currents--complex-manifolds-and-differential-forms/index.html; **886a687d5029616950683fe55defce1fe6854b12** | Definition 5.2.3 (paracompact Hausdorff manifolds), permanent **42A02A1A5EFE**, line 49; uncountably disconnected manifolds expressly allowed, lines 83–86. Contextual hypothesis check, not an audit of Section 5.2. |

These pages were checked against main AGENTS.md and documentation/proof-expansions.md and the existing review README, LATEST, ledger, and 747-row coverage matrix. The earlier cusp-conductor and monodromy audit findings are **not re-entered**. The Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme is **deferred-by-user** and was not opened.

## POME-NORM-COUNTABLE-COVER-001

**Severity:** medium. **Status:** confirmed error **in a proof step**; *not a counterexample to Theorem 9.4.6*. **Source:** Theorem 9.4.6, permanent 12A47DB401E2, section 9.4 HTML **line 157**; compare the section's own definition at **line 10**, and Definition 5.2.3 plus its explicit warning at **5.2 lines 49 and 83–86**.

The gluing step says, in substance, that because the reduced complex space X has a countable basis, one may choose a countable cover of local normalization charts and hence conclude that the glued normalization has a countable basis and is paracompact. **The premise is false under the actual stated definitions.** Section 9.4 defines a reduced complex space as Hausdorff and locally isomorphic to an analytic subset of a domain. It imposes no global second-countability condition. Section 5.2 explicitly allows complex manifolds with uncountably many components and says a countable basis is to be assumed explicitly when needed.

### Exact counterexample to the proof assertion

Let I be any uncountable set and put

\[
X=\coprod_{i\in I}\Delta_i,\qquad \Delta_i=\{z\in\mathbb C:|z|<1\}.
\]

This is a reduced complex space by the definition of Section 9.4. It is even a paracompact complex manifold under Definition 5.2.3: each disc is paracompact and topological disjoint unions of paracompact spaces are paracompact. It is **not second countable**, because the pairwise disjoint nonempty open sets \(\Delta_i\) are uncountable, whereas every family of pairwise disjoint nonempty open subsets of a second-countable space is countable (injectively choose a distinct basis element inside each).

Every connected local normalization chart built around a point stays in one of the clopen components \(\Delta_i\). No countable family of such local charts covers X. Nevertheless the normalization exists and is simply the identity \(X\to X\), a finite bimeromorphic map. Hence **the theorem survives**, but the printed countability inference is demonstrably unjustified.

### Proposed complete local repair

After the uniqueness and cocycle gluing, keep the existing Hausdorffness argument: two preimages of the same base point lie in a common local normalization and can be separated there, while points with distinct base images can be separated by inverse images of disjoint base neighborhoods. The glued space inherits an atlas of analytic subsets from **all** local normalizations; this is exactly what the Section 9.4 definition of a reduced complex space requires. Finiteness, normality, and bimeromorphy are local on the target and are already established in the preceding steps. **Delete** the sentences inferring that X has a countable basis, taking a countable subcover, and deducing paracompactness from a countable basis. They are unnecessary under the chapter's stated complex-space convention. If a stronger global convention is intended, state its hypothesis explicitly and prove any ensuing paracompactness separately rather than inferring global countability.

**Affected dependents:** the normalization theorem and citations that use it (especially proper finite maps, analytic curves, trace/restriction on normal models). No issue found with uniqueness on overlaps or the finite-branch local construction. Source text, theorem tags, and canonicalization are to remain unchanged until a separately reviewed patch.

## POME-PL-CUSP-RESTRICTION-001

**Severity:** low. **Status:** verified conditional deduction / concrete source-consistency check; **no false printed theorem**. **Source:** Theorem 5.5.6 (permanent 8D4BA339507E), Proposition 5.6.5 (permanent 6DAA1675792B), Example 5.6.6 (permanent 5A6B397A8B30), and normalization/curve parametrization Theorem 9.4.6 and Proposition 9.5.1 (permanents 12A47DB401E2 and A3A9384DC317). Their section blobs and exact anchors are in the table above.

Let the reduced irreducible cusp germ in \(\mathbb C^2_{x,y}\) be

\[
C=\{y^2=x^3\},\qquad \nu:\Delta\longrightarrow C,\quad \nu(t)=(t^2,t^3).
\]

The map is finite, bijective and bimeromorphic, and the source is normal; thus it represents the local normalization. The normalized holomorphic parameter t is **weakly holomorphic on C but not holomorphic in its singular structure sheaf**: the latter is \(\mathbb C\{t^2,t^3\}\), in which no germ has a nonzero linear term in t. (The earlier generalized cusp-conductor result is separate and is not repeated as a new finding.)

On the smooth ambient surface, set

\[
T_x=\mathrm{dd}^{\mathrm c}\log|x|^2=[x=0],
\qquad
T_y=\mathrm{dd}^{\mathrm c}\log|y|^2=[y=0].
\]

The compositions of both local potentials with \(\nu\) are not identically minus infinity on the disc, so Proposition 5.6.5 applies. Using the exact normalization \(\mathrm{dd}^{\mathrm c}\log|t|^2=[0]\) from Theorem 5.5.6 gives

\[
\boxed{\nu^*T_x=2[0],\qquad \nu^*T_y=3[0].}
\]

More generally, if an ambient holomorphic germ h does not vanish identically on C, the Taylor expansion yields

\[
h(t^2,t^3)=\sum_{a,b\ge0}c_{ab}t^{2a+3b}.
\]

After possible cancellation among terms of equal degree, every nonzero exponent still belongs to \(\langle 2,3\rangle=\{0,2,3,4,\ldots\}\). Thus the order of the pullback divisor belongs to this semigroup; in particular **no ambient holomorphic hypersurface germ pulls back to a simple zero at 0**, although the weakly holomorphic normalization parameter t has a simple zero on the disc. Each nonnegative exponent in the semigroup occurs for a monomial \(x^ay^b\), so this is exact, not just a bound.

Finally, the ambient function \(g(x,y)=y^2-x^3\) satisfies \(g\circ\nu\equiv0\); its current \([\{g=0\}]\) therefore **does not** admit a pullback along \(\nu\) by Proposition 5.6.5, precisely because \(\log|g|^2\circ\nu\equiv-\infty\). Hence the nonidentically-minus-infinity hypothesis is essential even on a finite normalization. This simultaneously checks Poincaré–Lelong multiplicities, the nonsubmersion pullback convention and the distinction between ambient-holomorphic and weakly holomorphic functions.

**Dependents:** divisor intersection multiplicities after normalization and uses of pullbacks of positive (1,1)-currents along analytic curves. This is a conditional compatibility computation, not an assertion that arbitrary currents admit pullbacks or a replacement for a singular-space intersection theory.

## Coverage and residual qualifications

This run newly checked selected complete argument passages in previously inventory-only **Sections 5.5 and 5.6** (one-variable distribution factors, zero-set exceptional loci, positive trace coefficients, proper-support pushforward signs, product-measure submersion pullback, and local-potential compatibility). It also revisited only the newly relevant countability/gluing step of **Section 9.4** and the disc parametrization of **Section 9.5**; both had prior selected proof coverage and remain **partially checked**, not recertified. Section 5.2 is strictly a definition crosscheck. The unreviewed portions of these sections, global upstream resolution, singular-current products and nonexcluded chapters elsewhere remain open.

The one confirmed error is an **invalid global proof inference**, not a false normalization theorem. The current-pullback result is a **verified conditional deduction**, not a repair to a nonexistent defect. No entire theorem chain or section is certified. No full build, CI, automated publication, formalization, or numerical test is claimed. No private documents are included. All source/registry/tag/main edits remain proposals only.
