# 2026-10-26 — density-ratio stability for maximal exponential subsolutions; ambient GH collapse for arbitrary nets

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Two low-severity **verified conditional deductions**, not claims of false theorems or completed verification of their upstream foundations. All author-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work was **skipped** and remains **deferred-by-user**.

## POME-EXP-GREATEST-LOGRATIO-001 — verified conditional deduction, low

**Primary source:** `docs/sections/equations-with-prescribed-singularities--exponential-equations-for-an-individual-density/index.html`, main blob `b4c15fdf7211401ad53bdef78a1831caf3c3dc65`. Equation 15.35.1: source `FB4936E0`, permanent tag `A708922257FB`, lines 7–14; Theorem 15.35.2: source `40C9E96E`, tag `9016C2906071`, statement lines 17–23, proof lines 25–47; Corollary 15.35.3: source `A854CD10`, tag `B2672237F244`, lines 52–95. Supporting selected check: Proposition 15.35.5, source `CD12A9FA`, tag `AC5E6031A12C`, root-functional inequalities and scalar bounds, lines 112–169.

**Result.** Let \(\lambda>0\) and let \(f,g\in L^1(dV)\) be nonzero nonnegative densities satisfying \(0<a f\leq g\leq b f\) almost everywhere for constants \(0<a\leq b<\infty\). If an exponential subsolution exists for \(f\), one also exists for \(g\), and their greatest solutions satisfy, **pointwise including at poles**,
\[
 \boxed{u_f-\lambda^{-1}\log b\leq u_g\leq u_f-\lambda^{-1}\log a.}\tag{1}
\]
Their pole sets and singularity types therefore coincide. Define \(M_f=\sup_Xu_f\), \(v_f=u_f-M_f\), \(c_f=e^{\lambda M_f}\). Taking suprema in (1) and subtracting gives
\[
 \frac1b\leq\frac{c_g}{c_f}\leq\frac1a,\qquad
 |v_g-v_f|\leq\lambda^{-1}\log(b/a)
\]
on the common finite locus; elsewhere use the equivalent pointwise extended-real inequalities instead of subtracting \(-\infty\). For each \(t>0\), the stronger **exact scaling law** holds:
\[
 \boxed{u_{tf}=u_f-\lambda^{-1}\log t,\quad
 M_{tf}=M_f-\lambda^{-1}\log t,\quad
 v_{tf}=v_f,\quad c_{tf}=c_f/t.}\tag{2}
\]
Consequently \(\mathrm{MA}_h^{\mathrm{ext}}(v_{tf})=\mathrm{MA}_h^{\mathrm{ext}}(v_f)\) exactly. When the threshold is defined as in §15.28 and Corollary 15.35.3, \(b_h(tf)=b_h(f)/t\). No \(L^p\) condition with \(p>1\) or strict positivity is needed.

**Complete proof.** Because \(\mathrm{MA}_h^{\mathrm{ext}}\) is invariant under additive constants,
\[
 \mathrm{MA}_h^{\mathrm{ext}}(s)\ge e^{\lambda s}f\,dV
 \quad\Longleftrightarrow\quad
 \mathrm{MA}_h^{\mathrm{ext}}(s-\lambda^{-1}\log t)
 \ge e^{\lambda(s-\lambda^{-1}\log t)}tf\,dV.
\]
This is an order-preserving bijection between *all* subsolutions for \(f\) and \(tf\); thus it maps the greatest elements to one another and proves (2), including equality of normalized measures. Also \(f\leq g\) implies every subsolution for \(g\) is one for \(f\), hence \(u_g\leq u_f\). The shifted greatest solution for \(bf\) is a subsolution for \(g\leq bf\), establishing existence for \(g\) from Theorem 15.35.2. Use \(af\leq g\leq bf\), monotonicity, and (2), to get (1). Taking suprema, subtracting finite bounds on the common finite locus, and scaling the admissible threshold scalar prove the remaining assertions. This checks all order/sign directions independently; it is a **strengthening of a correct theorem**, conditional on the printed greatest-solution existence/comparison input.

**Proposal and dependents.** Optionally append a log-density ratio stability corollary to 15.35.2/3; it is a normalization check for the scalar and greatest-solution constructions of §§15.35–15.36. It does not yield continuity for unbounded \(g/f\), solve an arbitrary zero-threshold equation, or independently prove the upstream non-pluripolar/smooth PDE theorems.

## POME-GH-AMBIENT-NET-COLLAPSE-001 — verified conditional deduction, low

**Primary source:** `docs/sections/equations-with-prescribed-singularities--degenerating-semipositive-backgrounds/index.html`, main blob `5ed2b285e8306f0a803df40712b93ed4054851a8`. Lemma 15.19.20, source `969D4BE0`, tag `022849340F28`, lines 400–424; Lemma 15.19.21, source `D5E70029`, tag `E3C9C96E314E`, lines 428–455; Proposition 15.19.22, source `738853ED`, tag `65049DB7855E`, statement lines 459–471, finite-excursion proof lines 476–522. The intrinsic sufficient bounds in Lemma 15.19.24 (tag `240B8EBF50C3`, lines 537–572) and Proposition 15.19.26 (tag `4A271B6E1DDB`, lines 622–650) were separately read; they remain valid.

**Statement.** Keep the setup of Proposition 15.19.22: a compact smooth \(X\), continuous surjection \(\pi:X\to Y\), finite contracted set \(S=\{s_a\}_{a=1}^N\subset Y\), a diffeomorphism on the regular complements, and the homeomorphism \(\iota:Y\to\widehat Y\) onto the compact completion of the regular intrinsic length metric \(d_0\). Let \((g_i)_{i\in I}\) be **any directed net** of smooth Riemannian metrics converging uniformly on each compact subset of \(X\setminus\pi^{-1}(S)\) to \(\pi^*g_0\), and let \(d_i\) be their **global length distances**. Suppose the nested neighborhood bases \(V_{a,r}\) satisfy
\[
 \lim_{r\downarrow0}\operatorname{diam}_{\widehat d_0}\iota(V_{a,r})=0,
 \qquad
 \lim_{r\downarrow0}\limsup_i
 \operatorname{diam}_{d_i}\bigl(\pi^{-1}(V_{a,r})\bigr)=0.\tag{3}
\]
The second diameter is **ambient**, not intrinsic within the open neighborhood, and is a strictly weaker hypothesis than the printed one. Then
\[
 \boxed{\sup_{x,x'\in X}|d_i(x,x')-\widehat d_0(\iota\pi x,\iota\pi x')|\longrightarrow0,}
\]
along the **full net**, and \(d_{\mathrm{GH}}((X,d_i),(\widehat Y,\widehat d_0))\to0\).

**Complete proof.** Fix \(\tau>0\). Because there are finitely many \(s_a\), choose disjoint \(V_a\), and smaller \(W_a\Subset V_a\), such that both diameters in (3) are \(<\tau\) for all sufficiently late indices (a common tail exists by directedness). The regular core \(K_X=\pi^{-1}(Y\setminus\bigcup_a W_a)\) is compact; on it metric tensor convergence gives two-sided path-length comparison factors \(A_i\ge1\) with \(A_i\to1\). Starting with a near-minimizing regular path between core points, delete the portion from first to last visit of each \(\overline W_a\), at most \(N\) portions, just as in the integrated proof at lines 490–494. Lift retained core portions. The lifted endpoints of any deleted portion lie in the **same** \(\pi^{-1}(V_a)\), and their *global* \(d_i\)-distance is \(<\tau\). The replacement curve need **not stay inside** this neighborhood, so the intrinsic-diameter hypothesis is unnecessary. Conversely, given a near-minimizing \(g_i\)-path, perform the same deletion in the corresponding preimages and project only its core portions. The projected endpoints of each removed portion are at \(\widehat d_0\)-distance \(<\tau\). Thus the two core inequalities remain
\[
 d_i\le A_i\widehat d_0\circ(G\times G)+N\tau,\quad
 \widehat d_0\circ(G\times G)\le A_i d_i+N\tau
\]
for \(G=\iota\pi\). Attach endpoints outside the core to chosen core representatives using only ambient \(d_i\) and \(\widehat d_0\) distances \(<\tau\). Exactly the same bookkeeping as integrated lines 503–515 gives the global two-sided inequalities with \(C_i=(N+2+2A_i)\tau\). If \(D=\operatorname{diam}\widehat Y\), the positive and negative distance errors are respectively at most
\[
 (A_i-1)D+C_i,\quad
 (A_i-1)(A_iD+C_i)+C_i.
\]
Their net limsups are bounded by \((N+4)\tau\). Since \(\tau>0\) is arbitrary, uniform full-net distance convergence follows. The graph of the surjective \(G\) is a correspondence; Lemma 15.19.20 bounds its GH distance by one half of its distortion, concluding the proof. This is a finite-cover, finite-excursion argument and does **not** infer sequential compactness from net convergence.

**Proposal and dependents.** State an optional ambient-neighborhood/net version after 15.19.22. The original theorem is correct and the intrinsic bound of 15.19.26 is still a convenient sufficient condition since ambient diameter never exceeds intrinsic diameter. The completion hypothesis, limiting-neighborhood smallness, and regular-core convergence remain essential assumptions in this proof. Relevant dependents: §15.19 metric degeneration and nodal resolution examples (§15.19.17, .22–.27). No main/source/registry/permanent-tag edits are proposed as already implemented.

## Actual coverage and excluded domains

First selected proof checks of §§15.19.20–22/.24/.26 and 15.35.2–3/.5. For §15.36, directly inspected the nonexcluded product reduction, radial flux (Lemma 15.36.2, source `D81523C8`, tag `91B8E02B5759`, lines 20–48) and normalized limit/capacity argument (Theorem 15.36.5, source `C917100A`, tag `AACA90B5B52B`, lines 62–113). No separate confirmed false result in these additional parts. Existing radial moment result `POME-RADIAL-MOMENT-SPECTRUM-001` and earlier density truncation rate `POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001` were checked for duplication and **not counted again**. Three formerly inventory-only current ToC rows receive *selected* coverage, **no entire section certified**. No project builds, software tests, CI, formal checks or publication.
