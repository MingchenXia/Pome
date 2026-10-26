# 2026-10-26: A PSH-representative proof bridge and compact scalar Hermitian rigidity

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Starting audit head:** ae3e637b72cd32c394b906f6677b88a152b9b36e.
All findings refer to the actual public integrated reading edition at the pinned main revision. No source, canonical entry, or permanent tag is changed.

## Exact source anchors and scope

| Locator | Permanent tag | Integrated path, main blob, precise physical lines |
| --- | --- | --- |
| Theorem 5.9.1 (real distribution and canonical PSH representative) | 2A4F77263F48 | docs/sections/plurisubharmonic-functions--positive-hessians-and-holomorphic-maps/index.html ; 6f73e47e8a1f91a54fc37761c07627b4724306ce ; 10–26 |
| Definition 5.22.1, Proposition 5.22.2 | 9CBA378B705D; 887F604607E9 | docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html ; bf6e5ca74ac04a3d79565bb58bda8d968a68be68 ; 13–46, external citation at line 44 |
| Proposition 5.22.3, Lemma 5.22.4 | F62C0F30E87C; 0DED015E67EF | same §5.22 blob ; 60–102, smooth scalar-factor identity at lines 78–101 |
| Propositions 5.23.1–2 | 237930AECE45; B16999654254 | docs/sections/plurisubharmonic-functions-and-singularities--changes-of-background/index.html ; 57c9cc9f1a10adf7925ef159c1095ca270150962 ; 10–53 |
| Lemmas 5.24.1–9 | 729BA86BCC7C; 0CFD6850F9F8; D1DAB1D38637; 05BCBF7FAC9C; E6AC64216A47; 16E53426F2DB; F3A890BB2575; 64CFA1B8522B; 98E72E23E884 | docs/sections/plurisubharmonic-functions-and-singularities--maxima-and-the-maximum-principle/index.html ; af8c44279c1e18f00174d613473b1d175beaa44a ; 10–160 |

The listed sections received **selected integrated theorem and proof reading**, not a certificate for entire dependency closures. §5.9.1 itself was read, while its earlier subharmonic §3.4.12 and line-restriction §5.4.4 dependencies were not independently reaudited.

## POME-QPSH-DISTRIBUTIONAL-INTERNAL-BRIDGE-001

**Severity:** low. **Status:** verified repair of an **avoidable external mathematical dependency**, **not** a false printed theorem.

At Proposition 5.22.2 line 44, the proof appeals to DemCADG Chapter I, Theorem 5.8 for the distributional characterization of PSH functions. The exact required local result, **including uniqueness of the PSH representative for a real distribution** with positive complex Hessian, was proved earlier in the integrated §5.9.1 (tag 2A4F77263F48, lines 10–26). This is a mathematical statement-and-hypothesis match, not a replacement based merely on an external locator.

Complete internal substitution: on a relatively compact holomorphic coordinate ball choose A so that
\[
\theta\leq A\,dd^c|z|^2.
\]
If \(\theta+dd^cT\geq0\) distributionally, then \(dd^c(T+A|z|^2)\geq0\). §5.9.1 gives a unique PSH representative \(p\) of that distribution. The difference \(p-A|z|^2\) is a quasi-PSH representative of T with the claimed curvature bound. On overlapping balls, add a **common** local smooth correction to the two representatives. They become PSH functions agreeing almost everywhere; the uniqueness in §5.9.1 makes them equal pointwise. They therefore glue. The reverse direction of Proposition 5.22.2 (finite local charts and a common C on compact X, lines 45–46) needs no external theorem.

**Proposed correction only:** replace the mathematical proof dependency at line 44 by the internal tag 2A4F77263F48, while **retaining DemCADG historical attribution** in the subject-based project history or clearly as attribution, not a required external proof. Preserve the local flat-distribution and global relative-background statements as distinct valid versions. **Affected:** §5.22.2 itself and §5.23/§5.24 when invoking its canonical representative; no altered conclusion.

## POME-HERM-SCALAR-COMPACT-RIGIDITY-001

**Severity:** low. **Status:** verified conditional deduction from Lemma 5.22.4 (not full independent certification of its elliptic regularity inputs).

**Statement.** Let X be a **compact connected** complex manifold of dimension n≥2, \(\gamma>0\) any smooth Hermitian real (1,1)-form, and \(\theta\) any smooth real (1,1)-form, not necessarily closed. Suppose for i=0,1 the real \(L^1_{\mathrm{loc}}\) functions \(u_i,a_i\) satisfy
\[
\theta+dd^c u_i=a_i\gamma
\]
as currents. Then \(a_1=a_0\) everywhere, and \(u_1-u_0\) is constant. No positivity assumption on \(a_i\) is necessary.

**Proof.** Lemma 5.22.4 (tag 0DED015E67EF, lines 78–102) makes all these unknowns smooth. Set \(w=u_1-u_0\), \(b=a_1-a_0\). Subtracting and differentiating gives
\[
dd^cw=b\gamma,\qquad db\wedge\gamma+b\,d\gamma=0.
\]
Wedge the second identity with \(\gamma^{n-2}\). Since \(n\ge2\), the map \(\xi\mapsto\xi\wedge\gamma^{n-1}\) is an isomorphism from real one-forms to real (2n−1)-forms. Hence for a fixed smooth one-form \(C_\gamma\) determined by
\[
C_\gamma\wedge\gamma^{n-1}=d\gamma\wedge\gamma^{n-2}
\]
we have \(db=-bC_\gamma\). Along any piecewise smooth path \(\sigma\), this is a scalar linear ODE
\[
\frac{d}{dt}b(\sigma(t))=-C_\gamma(\dot\sigma(t))b(\sigma(t)).
\]
Thus by connectedness either b is identically zero or b never vanishes and has a constant strict sign. At a maximum point of the smooth real w, its complex Hessian is nonpositive, so b≤0 there; at a minimum point b≥0. These extrema exist by compactness and exclude the constant-strict-sign case. Therefore b=0; w is smooth pluriharmonic on compact connected X and must be constant.

**Sharpness:** If n=1, take \(X=\mathbb P^1\), \(\theta=\gamma=\omega_{\mathrm{FS}}\), a nonconstant smooth real h, \(u_0=0,a_0=1\), and \(u_1=\varepsilon h,\ a_1=1+\varepsilon\,dd^ch/\gamma\). In dimension one every real (1,1)-form is a scalar multiple of \(\gamma\), and for sufficiently small nonzero \(\varepsilon\) both a-functions are strictly positive; uniqueness fails. If X is noncompact, in dimension n≥2 take \(X=\mathbb C^n\), \(\theta=\gamma=dd^c|z|^2\), with \(u_0=0,a_0=1\) and \(u_1=|z|^2,a_1=2\). So neither dimension nor compactness may be omitted.

**Proposed correction only:** add an optional global compact rigidity corollary immediately after Lemma 5.22.4. **Affected:** uniqueness interpretation of scalar Hermitian curvature/trace ansätze; do **not** extend the claim to matrix-valued Monge–Ampère equations or noncompact spaces.

## Other checked non-excluded steps

- §5.24.1 lines 16–23: freezing the smooth nonclosed background to \(\theta'\) with error ±εκ and choosing \(dd^cr=\theta'+\varepsilon\kappa\) indeed gives \(\theta+2\varepsilon\kappa+dd^c\max(u,v)\geq0\). Both error signs checked.
- §5.24.5 lines 75–86: for Euclidean \(\sigma=(\Delta f)dA\), the circular mean has derivative \(\sigma(B(0,r))/(2\pi r)\); its integrated factor \(1/(2\pi)\) is correct.
- §5.24.6–8 lines 97–149: the real-period supremum becomes a convex function of the imaginary coordinate with only logarithmic upper growth; the polar-hole extension uses an increasing family as t↓0; the isolated-point upper bound requires two independent complex coordinates, correctly indicating n≥2.
- §5.23.1 lines 10–30: smooth background changes preserve the current even noncompactly, but the claim that the shift is **bounded** requires the standing compactness of X.

No additional confirmed mathematical error is asserted. Historical findings and their statuses are unchanged. **Excluded:** the entire user-deferred Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. No source/body/registry/permanent-tag/main edits, project tests, build, CI, formal proof, or website publication.
