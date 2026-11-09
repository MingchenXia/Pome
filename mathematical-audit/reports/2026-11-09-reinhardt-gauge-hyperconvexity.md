# Complete Reinhardt gauge and hyperconvexity: source-anchored mathematical audit

- **Finding:** `POME-REINHARDT-HYPERCONVEX-GAUGE-001`
- **Date:** 2026-11-09.
- **Severity / status:** **low / verified conditional deduction** (new independent geometric consequence; **not** an error in the published statements, and **not** a complete upstream proof-chain certification).
- **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading edition:** `docs/sections/reinhardt-domains-and-logarithmic-convexity/index.html`, blob `51d14c9874a7f3ec3a4886644749db8ddb82d923`.
- **Precise anchors:** Proposition 9.62.2 at physical lines 17–34, source `demailly-complex-geometry:D34443BE`, permanent `B7A5F2850576`; Lemma 9.62.3 at lines 38–82, source `demailly-complex-geometry:C667FC59`, permanent `9179B3F88EE7`; Theorem 9.62.6 at lines 86–108, source `demailly-complex-geometry:463F81C1`, permanent `2A0C2847FC1E`. In particular the union-of-polydiscs/coordinate-contraction assertion is proved at lines 54–57.
- **Printed results:** Correct as inspected. This report does not change their hypotheses, their historical attribution, source labels, permanent tags, or canonicalization.

## Statement proved in this audit

Let (D\subset\mathbb R^n) be nonempty, open, convex and **downward closed** in each coordinate, and let
\[
\Omega=\widetilde\Omega_D
=\{z\in\mathbb C^n:\ |z_j|\le e^{x_j}\ (1\le j\le n)
\text{ for some }x\in D\}.
\]
Put (M_j=\sup_{x\in D}x_j\in\mathbb R\cup\{+\infty\}). Then the following conditions are equivalent:

1. Every (M_j) is finite.
2. (\Omega) is bounded.
3. (\Omega) admits a **bounded, continuous, negative plurisubharmonic exhaustion** (in particular, it is hyperconvex).
4. (\Omega) contains no nonconstant entire holomorphic curve.
5. (\Omega) is Kobayashi hyperbolic (equivalently in this family, Carathéodory hyperbolic).

When these conditions hold, set for (x\in\mathbb R^n)
\[
\gamma_D(x)=\inf\{t\in\mathbb R:x-t\mathbf1\in D\},
\qquad
p_D(z)=\exp\gamma_D(\log|z_1|,\ldots,\log|z_n|)
\quad(z\in(\mathbb C^*)^n).
\]
Then (p_D) has a **unique continuous nonnegative PSH extension to all of** (\mathbb C^n), is homogeneous in the exact sense (p_D(az)=|a|p_D(z)), and
\[
\boxed{\Omega=\{p_D<1\},\qquad p_D^{-1}(0)=\{0\}.}
\]
In particular, (p_D-1\in\mathrm{PSH}(\Omega)\cap C^0(\Omega)), (-1\le p_D-1<0), and each ({p_D\le r}), (0\le r<1), is a compact subset of (\Omega). More precisely,
\[
\{p_D<r\}=r\Omega\qquad (r>0).
\]

If some (M_j=+\infty), then the **whole complex coordinate line** (\mathbb C e_j\) lies in (\Omega), so conditions (3)–(5) fail. This dichotomy is specific to complete Reinhardt domains; it is not inferred for arbitrary pseudoconvex Reinhardt domains with coordinate-axis holes.

## Complete argument

**(A) Geometry of the logarithmic domain.**
The union of polydiscs on the printed line 55 is open and invariant under separate coordinate contractions. It contains (0), is connected (every point joins (0) by a radial segment), and is balanced. If every (M_j<+\infty), then (\Omega\subset\prod_j\{|z_j|\le e^{M_j}\}), hence bounded. Conversely, if (M_j=+\infty), then for each (R>0) there is (x\in D) with (e^{x_j}>R); setting the other coordinates to zero in the defining union of polydiscs gives (Re_j\in\Omega). Rotation and arbitrariness of (R) yield (\mathbb C e_j\subset\Omega). Thus (1) and (2) are equivalent.

**(B) The exact convex logarithmic gauge.**
Assume all (M_j) are finite. Fix (x^0\in D). If (t\ge\max_j(x_j-x_j^0)), then (x-t\mathbf1\le x^0\), so (x-t\mathbf1\in D). Thus (\gamma_D(x)<+\infty). Conversely (x-t\mathbf1\in D) implies (t>x_j-M_j) for every (j); hence (\gamma_D(x)>-\infty). The set of admissible pairs ((x,t)) is convex because (D) is convex, and is upward closed in (t), because (D) is downward closed. It is the open strict epigraph of (\gamma_D), so (\gamma_D) is a finite convex function, hence continuous. Downward closure also gives coordinatewise monotonicity
(x'\le x\Longrightarrow\gamma_D(x')\le\gamma_D(x)).
Direct substitution yields
\[
\gamma_D(x+s\mathbf1)=\gamma_D(x)+s.
\]
Moreover
\[
\boxed{ x\in D\iff\gamma_D(x)<0.}
\]
For the forward direction openness permits increasing (x) by a small common positive amount, giving an admissible negative (t); for the reverse direction a negative admissible (t) and downward closure imply (x\in D).

**(C) Continuity and PSH extension across the coordinate axes.**
The map (\chi(x)=e^{\gamma_D(x)}) is finite, positive, continuous, convex and coordinatewise nondecreasing on all (\mathbb R^n). Apply the **actual** Lemma 9.62.3 with its auxiliary logarithmic domain equal to (\mathbb R^n), not with the original (D): it gives a unique continuous PSH extension of (\chi(\log|z|)) to all of (\mathbb C^n). For completeness, on any stratum with nonzero-coordinate set (J), its value is
\[
p_D(z)=\lim_{T\to\infty}
e^{\gamma_D(\log|z_J|,-T\mathbf1_{J^c})}.
\]
The limits decrease, are bounded below by zero, and are finite convex functions in the remaining logarithmic variables; their continuity and locally uniform convergence follow from the elementary finite-convex-function argument on the printed lines 59–67. The PSH claim also follows directly by applying convex Jensen and coordinatewise monotonicity to
(\tfrac12\log(|z_j|^2+\varepsilon^2)), then taking a decreasing limit, exactly as in lines 69–81. This proof does **not** require Demailly regularization, Bergman estimates, weighted (L^2), Ohsawa–Takegoshi, or multiscale patching.

**(D) Domain identity, including all coordinate strata.**
For (z\in(\mathbb C^*)^n), the equivalence (x\in D\iff\gamma_D(x)<0) proves (z\in\Omega\iff p_D(z)<1). If (z\in\Omega) has zero coordinates, openness provides (a>1) close to one with (az\in\Omega). Approximate (az) inside (\Omega) by points with all coordinates nonzero; continuity gives (p_D(az)\le1). Homogeneity (first verified off the axes from the translation identity and then extended by continuity) gives (p_D(z)\le a^{-1}<1). Conversely if (p_D(z)<1), choose (w\in(\mathbb C^*)^n) arbitrarily close to (z) and satisfying (|w_j|>|z_j|) in every coordinate. Continuity permits (p_D(w)<1), so (w\in\Omega). Coordinate contraction yields (z\in\Omega). Thus (\Omega=\{p_D<1\}) everywhere, not merely on the punctured torus. Homogeneity also gives (p_D(0)=0). If (z\ne0) and (p_D(z)=0), then (p_D(Rz)=0) for all (R>0), so the bounded (\Omega) would contain the whole ray (Rz), a contradiction. This proves the asserted zero locus and ({p_D<r}=r\Omega).

**(E) Hyperconvexity and intrinsic hyperbolicity.**
The function (p_D-1) is continuous, PSH and strictly negative on (\Omega). For (0\le r<1), its sublevel closure (\{p_D\le r\}) is compact (closed by continuity, bounded since it lies in the bounded (\Omega), and still lies in (\Omega)). Hence (2) implies (3). It also implies (4) by applying Liouville separately to the bounded coordinate functions of any entire map (\mathbb C\to\Omega).

To verify (5) without a global metric theorem, choose (R_j>e^{M_j}). Each (z\mapsto z_j/R_j\) maps (\Omega) holomorphically into the unit disc. For (z\ne w), choose a different coordinate (j); Schwarz–Pick yields
\[
c_\Omega(z,w)\ge
\rho_{\mathbb D}(z_j/R_j,w_j/R_j)>0,
\qquad k_\Omega(z,w)\ge c_\Omega(z,w),
\]
so both intrinsic pseudodistances separate points. Conversely if some (M_j=+\infty), the whole coordinate line is included. The Kobayashi pseudodistance vanishes between any two of its points because (k_{\mathbb C}=0), and every bounded holomorphic function on (\Omega) is constant along that line by Liouville, so the Carathéodory pseudodistance vanishes there. Also any negative PSH exhaustion would restrict to a bounded-above subharmonic function on that line, hence a constant (or (-\infty)); an appropriate negative sublevel would contain the entire line and could not be relatively compact. Therefore (3)–(5) all fail. This proves the equivalences.

## Exact model checks and limits of the claim

- (D=(-\infty,0)^n): (\Omega=\mathbb D^n), (\gamma_D(x)=\max_jx_j), (p_D(z)=\max_j|z_j|), giving the explicit bounded negative PSH exhaustion (\max_j|z_j|-1).
- (D=\{(x_1,x_2):x_1+x_2<0\}): (\Omega=\{|z_1z_2|<1\}), (\gamma_D(x)=(x_1+x_2)/2), and (p_D(z)=\sqrt{|z_1z_2|}\). Both coordinate axes lie in (\Omega) as entire complex lines; it is pseudoconvex by printed Theorem 9.62.6 but is not hyperconvex in the compact-sublevel sense above. The gauge has a nontrivial zero locus, showing why the boundedness hypothesis cannot be discarded.
- An arbitrary downward-closed (D) is already unbounded in negative logarithmic directions. **The relevant criterion is boundedness above in each coordinate, not boundedness of (D) itself.**

## Classification, suggested placement and dependencies

**Verified conditional deduction, low severity**. The printed Proposition 9.62.2, Lemma 9.62.3 and Theorem 9.62.6 are not contradicted. This is a new, exact geometric sharpening of their **bounded complete Reinhardt** case, suggested as a separate remark/corollary after Theorem 9.62.6, preserving the existing historical attribution. The continuous PSH extension is derived in detail from the internal Lemma 9.62.3 (with its printed convex-composition proof); the usual one-variable Schwarz–Pick and Liouville principles enter only the intrinsic-metric corollary. No dependency on the owner-excluded approximation/regularization programme is introduced. Potential downstream uses: deciding when the convex-logarithmic models in §9.62 have bounded negative PSH exhaustions and distinguishing pseudoconvexity from hyperconvexity in noncompact Reinhardt examples. No downstream Pome theorem is claimed to contain a newly confirmed error. No proof of the entire §9.62 or its upstream convexity/PSH chain is certified.
