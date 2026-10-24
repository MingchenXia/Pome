# 2026-10-24: holomorphic-retract Green rigidity and sharp density-order stability

**Freshly reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (25 chapters, 747 numbered sections). **Preserved audit branch:** review/mathematical-audit, starting at 020dd1227f1dfd2d093fe3fe676398554edadce3. This is an audit of **selected integrated proofs**, not certification of those sections or of upstream analytic results.

**Scope:** first selected nonexcluded proof-level reading of §§7.22, 7.26–7.27, and 15.13–15.15. The independent comparison and density estimates here do not inspect Demailly approximation/regularization, Bergman kernels, L² extension, Ohsawa–Takegoshi, multiscale atlases or positivity-loss proof completion. Those historical items remain **deferred-by-user, neither resolved nor certified**. §15.16's regularization-based construction is **not** audited by this report.

## Finding POME-GREEN-HOLO-RETRACT-001

**Status:** verified conditional deduction (low severity); **not** a false printed theorem or new external input. **Suggested change:** optional separately reviewable corollary of Proposition 7.27.2, with the existing example and all permanent tags preserved.

**Pinned source:** main docs/sections/symmetric-green-envelopes-on-unbounded-domains/index.html, blob 76c965efd42eb17ffa9c34c8b7b0408d56a9e2ce, Proposition **7.27.2** source klimek-pluripotential-theory-DC0D60AB, permanent 28AAE4E86F18, physical lines **28–55**; Example **7.27.3** source klimek-pluripotential-theory-E575F65F, permanent 7F276A63690B, lines **56–77**. Proposition **7.27.1**, source klimek-pluripotential-theory-71A15571, permanent A2711B944A6D, lines **10–27**, was also inspected. The earlier definition of the symmetric Green envelope is in §7.19.3 and is used only with the explicit extended-slice convention stated in §7.27.

### Exact claim and proof

Let D be a proper (possibly unbounded) domain in complex Euclidean space, let p:D→Δ be holomorphic, and assume there is a holomorphic section i:Δ→D with p∘i=id. Let g_D be the extended pluricomplex Green function and W_D the jointly subharmonic, separately plurisubharmonic symmetric Green envelope defined in §§7.19/7.27. For any s,t∈Δ,

\[
\boxed{\quad
W_D(i(t),i(s))=g_D(i(t),i(s))
 =\log\left|\frac{t-s}{1-\overline{s}t}\right|.
\quad}
\]

The value on the diagonal is minus infinity. No isolated-pole or total Monge–Ampère mass assertion follows.

**Proof, lower bound.** Define
\[
K_p(z,w)=\log\left|
\frac{p(z)-p(w)}{1-\overline{p(w)}p(z)}
\right|.
\]
It is nonpositive, symmetric and jointly upper semicontinuous (with minus infinity on the appropriate level-set diagonal). For fixed w, the numerator is holomorphic in z and the denominator is holomorphic and nonvanishing in z; hence K_p(·,w) is PSH, with the symmetric assertion in w. Jointly, the log absolute value of the numerator is subharmonic on D×D. The log absolute value of the denominator is harmonic in z separately and in w separately, so its joint **real Laplacian**, the sum of those partial Laplacians, is zero. Thus K_p is jointly subharmonic.

Write d(z)=dist(z,∂D). Schwarz's lemma on the complex lines of B(z,d(z)) gives the ball Schwarz bound
\[
\left|\frac{p(z)-p(w)}{1-\overline{p(w)}p(z)}\right|
\leq \frac{\|z-w\|}{d(w)}
\]
when \(\|z-w\|<d(w)\); when outside that ball the bound is automatic because the left side is at most one. Interchanging z,w and combining yields
\[
K_p(z,w)\leq
\log\|z-w\|-\log\max\{d(z),d(w)\}.
\]
This is precisely the required distance/pole constraint, including the diagonal upper bound, so K_p belongs to the defining admissible family for W_D. In particular \(W_D(i(t),i(s))\geq K_p(i(t),i(s))\), which equals the displayed disc Green kernel.

**Proof, upper bound.** Any negative PSH Green competitor U(·) on D with a logarithmic pole at i(s) pulls back to a negative subharmonic function U∘i on Δ. Holomorphicity of i gives \(\|i(t)-i(s)\|\leq C|t-s|\) locally, so the pulled-back pole satisfies the correct upper logarithmic bound at s. The ordinary disc Green extremal principle gives
\[
U(i(t))\leq\log\left|\frac{t-s}{1-\overline{s}t}\right|.
\]
Taking the supremum of all U gives the same upper bound for g_D on the retract. Proposition 7.27.2 gives W_D≤g_D; combine the two bounds. This proof works even when other Green slices collapse, and does not assume symmetry of the whole g_D.

**Concrete §7.27.3 consequence.** For
\[
D=\{(z,w)\in\mathbb C^2:\ |w|^2(1+|z|^2)<1\},
\quad p(z,w)=w,\quad i(t)=(0,t),
\]
the full identity holds for **every pair** on the vertical disc:
\[
W_D((0,t),(0,s))=g_D((0,t),(0,s))
=\log\left|\frac{t-s}{1-\overline{s}t}\right|.
\]
This strengthens the source's lower bound at the special pole (0,0), while remaining compatible with the source's proof that that Green slice is minus infinity along the entire horizontal line \(\{w=0\}\). Another explicit admissible Green competitor at (0,0) is
\[
H(z,w)=\log|w|+\tfrac12\log(1+|z|^2)
      =\log\bigl(|w|\sqrt{1+|z|^2}\bigr),
\]
which is negative PSH on D and satisfies the required logarithmic upper pole bound. Hence \(g_D((z,w),(0,0))\geq H(z,w)\), a strictly stronger lower bound than \(\log|w|\) for z≠0, w≠0. **No equality off the retract** is asserted.

**Dependents:** holomorphic retracts in unbounded Green domains, interpretations of the symmetric envelope W_D and its singular line, and any proposed transfer of bounded-domain isolated-pole mass statements. Retraction rigidity says nothing about positivity or finiteness of such masses.

## Finding POME-EXP-MA-DENSITY-RATIO-001

**Status:** verified conditional deduction (low severity); the source's comparison theorem is **not** false. **Suggested change:** optional standalone order-and-sharp-log-Lipschitz corollary after §15.13.3, with unchanged source statements and tags.

**Pinned source:** main docs/sections/equations-with-prescribed-singularities--comparison-above-a-strict-singular-barrier/index.html, blob db560c935a7d651803427b6243957ea1f957b468. Lemma **15.13.1**, source non-kahler-pluripotential-theory-F564C83F, permanent E6E5D71344DD, physical lines **13–44**; Theorem **15.13.2**, source non-kahler-pluripotential-theory-241F3E4D, permanent F71978C42841, **45–99**; Corollary **15.13.3**, source non-kahler-pluripotential-theory-3262185F, permanent 24CD508AEB8D, **100–127**.

### Exact claim and proof

Fix the smooth big real background θ and strict analytic barrier ρ of §15.13, and λ>0. Suppose u_f,u_g are θ-PSH solutions of
\[
\mathrm{MA}_\theta(u_f)=e^{\lambda u_f}f\,dV,\qquad
\mathrm{MA}_\theta(u_g)=e^{\lambda u_g}g\,dV,
\]
in the **same ordinary singularity type**, each bounded below by ρ minus a constant, with nonnegative nonzero densities f,g. If for some ε≥0
\[
f\leq e^\varepsilon g,\qquad g\leq e^\varepsilon f
\quad\text{a.e.},
\]
then, for the canonical representatives on all of X,
\[
\boxed{\quad
\sup_X|u_f-u_g|\leq \varepsilon/\lambda .
\quad}
\]

Indeed fix t>ε/λ. On the open comparison set \(\{u_f<u_g-t\}\) (restricted to Ω if necessary), nonnegative measure domination gives
\[
\mathrm{MA}_\theta(u_f)
=e^{\lambda u_f}f\,dV
\leq e^{\varepsilon-\lambda t}\,
   e^{\lambda u_g}g\,dV
=e^{\varepsilon-\lambda t}\,
   \mathrm{MA}_\theta(u_g-t).
\]
The coefficient is strictly less than one. Theorem 15.13.2 applies to the pair (u_f,u_g−t): their common ordinary type supplies the finite upper difference constant; each obeys the required lower barrier bound. It gives \(u_f\geq u_g-t\). Let t decrease to ε/λ. Interchanging f and g gives the reverse estimate. Theorem 15.13.2 / Lemma 5.24.3 already handle extension across the barrier pole set. There is **no appeal to a new existence theorem or to a regularization scheme** in this conditional statement.

The one-sided order assertion is also useful: if merely \(f\leq g\) a.e. for two solutions as above, then \(u_f\geq u_g\). Apply the same proof with arbitrary t>0 and ε=0 in the single indicated direction. Thus the exponential solution map reverses the pointwise order of densities in a fixed type.

**Sharpness without an existence assertion.** Starting with any one solution u_f, scale the data by \(g=e^\varepsilon f\), and put \(u_g=u_f-\varepsilon/\lambda\). Since \(\mathrm{MA}_\theta\) is unchanged by addition of constants,
\[
\mathrm{MA}_\theta(u_g)
=\mathrm{MA}_\theta(u_f)
=e^{\lambda(u_f-\varepsilon/\lambda)}
 e^\varepsilon f\,dV.
\]
By §15.13.3 it is the unique solution in that type for data g. Therefore the difference attains ε/λ everywhere: the constant \(1/\lambda\) cannot be reduced.

**Dependents:** stability of normalized or fixed-type exponential equations under multiplicative density errors, uniqueness, comparison of positive numerical approximations. This statement does not imply L^p-to-uniform continuity under merely additive density perturbations; no such estimate is claimed.

## Additional actual source checks, without new defect certificates

- **§7.22.1**, docs/sections/a-smooth-strictly-pseudoconvex-domain-with-asymmetric-green-function/index.html, blob 578eae14c12814126a1b4cb2bd3c3e2ce96cef28, source klimek-pluripotential-theory-98AA2433, permanent 8B924AA3ED4A, lines **7–48**. Inspected the proper two-sheeted map and uniqueness of the fiber over (0,0), the gluing-circle bound \(|w|^2\gtrsim\varepsilon\), the strict \(\sqrt{\log(1/\varepsilon)}\) separation, and the monotone polynomial sublevel exhaustion. No new error certified; the final asymmetric-envelope mass criterion is conditional on §7.21.
- **§7.26.1/.2/.3**, docs/sections/generalized-products-and-their-associated-bounded-products/index.html, blob ccdb1ff3375fa102c90f78bd97dd4c6a26ae6ed9, sources klimek-pluripotential-theory-2D7D9C7C / 8C5E7ECD / 77522B43, permanent EFE2F92EE4F9 / 8DF858D7EC52 / 5C50A7C32E5B, lines **31–145**. Checked the quantifier ordering for Colombeau moderateness/negligibility, the moment cancellation of smooth embeddings, the translation of capacity tests inside a buffered pair of balls, and the signed-kernel decomposition into two positive normalized kernels. Passage to Bedford–Taylor products uses the bounded capacity-continuity theorem conditionally. Generalized association was **not** confused with equality of Colombeau classes or with existence of a positive classical unbounded product.
- **§15.14.1/.2**, docs/sections/equations-with-prescribed-singularities--subsolutions-and-the-gauduchon-trace/index.html, blob c7c809b0cbd96e0deeece05d4aa2309527796536, sources non-kahler-pluripotential-theory-7537970B / FDEEE883, permanent 869D3138741D / 0A5580561320, physical lines **10–105**. Directly checked \(1\leq t\leq2-\rho\), convex recomposition coefficients \(1-t^{-2}\), \(t^{-2}\), \(2t^{-3}\), the pointwise determinant/trace normalization and Gauduchon Stokes sign. The bounded Hermitian equation Lemma 15.3.1 is a conditional internal dependency, **not** an independently certified external gap.
- **§15.15.1/.3**, docs/sections/equations-with-prescribed-singularities--stability-above-a-strict-barrier/index.html, blob 2a884ceafcc821213e77ad5d9e70d69fe35475bb, sources non-kahler-pluripotential-theory-D2956B4A / 31E24C9E, permanent 668D07ADFF44 / 131F17206F6A, lines **10–100**. Checked \(t=(2m_\delta/b)^{1/n}\), positivity of the mixed expansion on the strict comparison set, and the Hölder/Chebyshev balance
\[
\gamma_q=\frac{p-q}{npq+p-q}\longrightarrow
\frac{p-1}{np+p-1}\quad(q\downarrow1).
\]
Read the compactness argument using local bounded products on Ω and weak L^p subsequences, without certifying the complete upstream PDE chain.

### Coverage and audit limits

These six sections had previously been **inventory-only** in the 747-row current-ToC matrix; this report upgrades only the cited entry ranges to **selected proof coverage**. §7.19.3, §7.21, §5.24, §15.3 and §15.8 were *prerequisites/context only*. No whole section, deep compactness theorem, external analytic existence theorem or collection-wide result is certified. No new false theorem, genuine duplication or complete proof repair was established in this pass. The two findings above are sharpenings with complete deductions **conditional on precisely identified printed theorems**.

**Write boundary:** audit Markdown on review/mathematical-audit only. No source, mathematical body, canonicalization, permanent tag, main, PR, CI, build, formalization, or website publication changes. The entire dedicated user-excluded Demailly/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**.
