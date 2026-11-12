# A zero-volume obstruction to extending the almost-semigroup Okounkov body map

**Finding ID:** POME-OKO-ZEROVOLUME-NONEXTENSION-001  
**2026-11-12 | Severity:** low | **Status:** verified conditional deduction (direct counterexample to an *unprinted extension*, not a source error).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated file:** docs/sections/almost-semigroups/index.html  
**Integrated blob SHA:** 33898b2963ad0f8b7e30bf414276642f60925b74  
**Related section:** 19.7 (with the semigroup/volume terminology used in 19.2).

## Precise source anchors

- Equation 19.7.17, source sgpt:A996EEF7, permanent tag 642E2D6850DF, physical lines 215–230: the normalized-level symmetric-difference pseudometric.
- Theorem 19.7.20, source sgpt:282DA4DD, permanent tag 85641516C8CA, physical lines 299–319: normalized counting and the full-lattice group caveat.
- Definition 19.7.26, source sgpt:56C14254, permanent tag 0270FA2C03BD, physical lines 393–398: the cone-slice Okounkov body.
- Definition 19.7.31, source sgpt:7DD4FA88, permanent tag B0C65454CC85, physical lines 528–532: the strictly positive volume domain.
- Theorem 19.7.32, source sgpt:ED83BFDD, permanent tag 1551B679B8B7, physical lines 535–546 and proof 548–658: the *continuous* extension on strictly positive-volume almost semigroups.

The proposed stronger claim, namely continuity across the zero-volume boundary of the pseudometric closure, is **not** asserted by Theorem 19.7.32.

## Exact one-dimensional construction

Set \(n=1\) and fix once and for all the pointed rational cone
\[
 C=\{(x,k)\in\mathbb R\times\mathbb R_{\geq0}:0\leq x\leq k\}.
\]
It satisfies the ambient conditions in subsection 19.7.15. Let \(E=\{(0,0)\}\subset C\cap\mathbb Z^2\) be the zero semigroup. For every integer \(j\geq3\), let
\[
 \begin{split}
 C_j^-&=\{(x,k):k\geq0,\ 0\leq x\leq k/j\},&
 S_j&=C_j^-\cap\mathbb Z^2,\\
 C_j^+&=\{(x,k):k\geq0,\ (1-1/j)k\leq x\leq k\},&
 T_j&=C_j^+\cap\mathbb Z^2.
 \end{split}
\]
Every \(S_j,T_j\) is a *saturated* (cone-intersection) subsemigroup in the same ambient \(C\). Both generate the full abelian lattice \(\mathbb Z^2\): the members \((0,1),(1,j)\in S_j\) have determinant \(-1\), while \((1,1),(j-1,j)\in T_j\) have determinant \(1\). Thus \(S_j,T_j\in\mathcal S'(C)\), including the full-group hypothesis needed for the standard volume identification.

At every positive degree \(k\),
\[
 (S_j)_k=\{0,1,\dots,\lfloor k/j\rfloor\},\qquad
 (T_j)_k=\{\lceil k(1-1/j)\rceil,\dots,k\}.
\]
The latter two sets each have exactly \(\lfloor k/j\rfloor+1\) elements. Since \(j\geq3\), the corresponding real intervals are disjoint, so \((S_j\cap T_j)_k=\varnothing\) for \(k>0\). Also \(E_k=\varnothing\) for every \(k>0\). Hence **directly from equation 19.7.17**, without using any limiting or counting theorem,
\[
 \begin{split}
 d_{\rm sg}(S_j,E)
 &=\lim_{k\to\infty}\frac{\lfloor k/j\rfloor+1}{k}
 =\frac1j,\\
 d_{\rm sg}(T_j,E)&=\frac1j,\qquad
 d_{\rm sg}(S_j,T_j)=\frac2j.
 \end{split}
\]
Both sequences therefore converge to the *same* zero-volume semigroup \(E\) in the pseudometric closure. The definition of volume or its 1-Lipschitz extension gives \(\operatorname{vol}(E)=0\), while \(\operatorname{vol}(S_j)=\operatorname{vol}(T_j)=1/j>0\).

On the other hand, the cone-slice definition 19.7.26 gives exactly
\[
 \Delta(S_j)=[0,1/j],\qquad
 \Delta(T_j)=[1-1/j,1].
\]
Both are nonempty compact convex bodies (lower-dimensional limits are explicitly permitted in section 19.7). Their Hausdorff limits are
\[
 \Delta(S_j)\longrightarrow\{0\},\qquad
 \Delta(T_j)\longrightarrow\{1\},
\]
and
\[
 d_{\rm Haus}\bigl(\Delta(S_j),\Delta(T_j)\bigr)
 =1-\frac1j\longrightarrow1.
\]

## Consequences and exact logical scope

**(1) Positive volume is essential for the claimed domain.** There is no continuous map from the *entire* pseudometric closure \(\overline{\mathcal S'(C)}\) to \(\mathcal K_1\) that agrees with \(\Delta\) on \(\mathcal S'(C)\). Such a map would send the common limit \(E\) to both \(\{0\}\) and \(\{1\}\), contrary to Hausdorff uniqueness. This is an obstruction even though \(\mathcal K_1\) already contains both singleton convex bodies; it is not a missing-target-space issue.

**(2) No uniform continuity on the strictly positive domain.** The pairs \(S_j,T_j\) stay *inside* \(\mathcal S'(C)\), have \(d_{\rm sg}(S_j,T_j)\to0\), but their Okounkov bodies remain a definite Hausdorff distance apart. Thus the map in Theorem 19.7.32 is continuous pointwise as printed, but is not uniformly continuous on all \(\mathcal S'(C)\) (nor on its positive-volume closure). This does not contradict continuity at any fixed positive-volume semigroup: all moving examples approach the excluded boundary \(E\).

**(3) The lattice and regularity hypotheses are not loopholes.** Both families are saturated semigroups, generate the full \(\mathbb Z^2\), and live in the same fixed rational pointed cone. In particular, the phenomenon survives all the common restrictions used to state the semigroup volume theorem.

The finding is a sharp **scope test**, not a counterexample to Theorem 19.7.32. Its proof needs only the printed definitions and elementary floor arithmetic; it makes no use of the user-deferred Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme.

## Proposed editorial qualification and affected dependents

No production theorem or proof edit is required. If a global continuity assertion is later used in the Okounkov/graded-series arguments (especially sections 19.1–19.7) or in comparing limiting flags, it must remain **at a positive-volume limit**; positive volume of each moving input separately is not enough. A short remark after Theorem 19.7.32 could state that the positive-volume restriction is sharp and that uniform continuity fails near that boundary. This is a proposed addition only, not an authorized modification of the published text or tags.

## Actual coverage and verification boundary

New direct proof-level check: the **zero-volume boundary of Definition 19.7.31 / Theorem 19.7.32**, using the pseudometric of 19.7.17 and cone body 19.7.26. The established printed extension proof, the general Kaveh–Khovanskii theorem, and every upstream group-theoretic dependency are **not** fully certified by this elementary model. Section 19.7 was already partly sampled in the audit; **+0** first-visited numbered sections, **+0** entirely certified sections. The production table of contents remains **25 chapters / 747 numbered sections**. No build, tests, formal verification, CI, main/source/registry/tag changes or website publication were performed.
