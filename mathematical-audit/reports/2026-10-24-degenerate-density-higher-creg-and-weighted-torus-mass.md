# 2026-10-24 mathematical audit: higher-regularity degenerate densities and weighted torus mass

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit branch initial head:** `aed8f3f3d33d96a52ddebee74c84ac18d0f76923`.
**Scope:** Fresh direct inspection of the integrated proofs of §§7.24, 7.25, 7.33, and 9.12, together with the local convex/toric normalization of §21.12.24. These are selected theorem/proof checks, **not** whole-section or upstream certification. Demailly approximation/regularization and its dedicated Bergman/L²/OT/atlas/positivity-loss programme were deliberately not examined; historical findings remain **deferred-by-user**, not certified.

## POME-DEGEN-CREG-SCALE-001 — higher-order smooth right sides with non-\(C^{1,1}\) solutions

**Status:** verified conditional deduction; **severity:** low (optional strengthening, no false original theorem).
**Exact integrated anchor:** Proposition 7.24.1, permanent tag `D0960BD969B2`, source label `klimek-pluripotential-theory-5F0EDAF7`; `docs/sections/degenerate-densities-and-interior-second-derivatives/index.html`, blob `fafeab3a344243fe04f24265022bd921f3a4d375`, physical lines 11–35 (statement, source ansatz and density regularity), 37–67 (radial comparison/free-boundary sequence), 69–100 (scaling and contradiction).

**Precise strengthening.** Fix an integer \(n\ge3\) and an integer
\[
 3\le r\le 2n-3.
\]
There exists a nonnegative \(f\in C^r(\mathbb C^n)\) whose unique continuous psh solution of
\[
 (dd^c u)^n=f\,dV_{2n}\quad\text{on } B(0,1),
 \qquad u|_{\partial B}=0,
 \qquad dd^c=\frac{i}{2\pi}\partial\bar\partial,
\]
is **not \(C^{1,1}\) on any neighborhood of the origin**. In particular, \(n=3,r=3\) is possible, whereas the printed construction specifies only \(C^2\) for all \(n\ge3\).

**Parameter construction.** Put \(N=2(n-1)\). Since \(r<N\), choose
\[
 \alpha>\frac{N}{N-r},\qquad
 r\alpha<\beta<N(\alpha-1).
\]
For example one can set \(\alpha=2N/(N-r)\) and
\(\beta=[r\alpha+N(\alpha-1)]/2\). Write \(z=(z',w)\in\mathbb C^{n-1}\times\mathbb C\) and define
\[
 \eta(t)=\begin{cases}\exp[-1/(1-t^2)]&0\le t<1,\\0&t\ge1,\end{cases}
 \quad
 f(z',w)=\begin{cases}|z'|^\beta\eta(|w|/|z'|^\alpha)&z'\ne0,\\0&z'=0.\end{cases}
\]
Here \(\eta(|w|/a)\) is smooth at \(w=0\), as its nonzero part is a smooth function of \(|w|^2/a^2\).

**Regularity proof.** On \(\operatorname{supp} f\), \(|w|\le|z'|^\alpha\). For every real multi-index \(|\gamma|=j\le r\), differentiation costs at most \(|z'|^{-\alpha}\) per order (because \(\alpha>1\)); the fixed smooth cutoff and its derivatives are bounded. Thus
\[
 |D^\gamma f(z',w)|\le C_j |z'|^{\beta-j\alpha}.
\]
Since \(\beta>r\alpha\), each of these derivatives tends uniformly to zero along \(\{z'=0\}\). Inductively, the zero extensions are the successive derivatives at the hyperplane as well: the difference quotients of the \(j\)-th extensions tend to zero because \(\beta-j\alpha>1\) for \(j<r\). The conclusion is \(f\in C^r\) globally. The strict inequality is important; the endpoint is not claimed.

**Why the printed PDE argument remains valid for these parameters.** The proof of Proposition 7.24.1 uses only (a) \(\alpha>1\), (b) the positivity of \(f\) when \(0<|z'|\) and \(|w|<|z'|^\alpha\), and (c) the homogeneity of its anisotropic support and amplitude. Its comparison argument (physical lines 37–67) gives, independently of the original numerical \(\alpha,\beta\), a sequence \(\varepsilon_k\downarrow0\) with
\[
 s(\varepsilon_k)=U(\varepsilon_k^{1/\alpha},\varepsilon_k),
 \quad s(t):=u(0,t),\quad u(z',w)=U(|z'|,|w|),
\]
and, for \(\lambda=\varepsilon^{1/\alpha}\),
\[
 u(0)\le u(z',w)\le s(\varepsilon)
 \quad (|z'|\le\lambda,\ |w|\le\varepsilon).
\]
For clarity, the comparison begins with \(h(x)=s(e^x)\), convex by radial subharmonicity. Where the radial boundary value \(b(t)=U(\min(t^{1/\alpha},\sqrt{1-t^2}),t)\) exceeds \(s(t)\), maximality of \(u\) in the open zero-density region \(|z'|^\alpha<|w|\) forces \(h\) to be locally affine. If \(s\) had an initial constant interval, positivity of the density in the intervening product would give \(b>s\) at its final radius, forcing continued constancy, a contradiction. Thus \(s(t)>s(0)\) for all \(t>0\); if \(b>s\) near zero, local affineness and the finite left-end limit would make \(s\) constant there. Hence the stated contact sequence exists. No differentiation of the unknown solution is assumed here.

Rescale by
\[
 d=(\varepsilon\lambda^{n-1})^{2/n},\qquad
 v(\zeta',\zeta_n)
   =\frac{u(\lambda\zeta',\varepsilon\zeta_n)-s(\varepsilon)}{d}.
\]
Then \(v(0)\le v\le0\), and complex determinant covariance gives the *exact*
\[
 (dd^c v)^n=f(\lambda\zeta',\varepsilon\zeta_n)dV_{2n},
 \qquad d^n=(\varepsilon\lambda^{n-1})^2.
\]
On the fixed set \(1/8<|\zeta'|<1/4\), \(|\zeta_n|<8^{-\alpha}/2\), the cutoff is bounded below by a positive constant, so the right side has mass \(\ge c_{n,\alpha,\beta}\lambda^\beta\). The bounded Chern–Levine–Nirenberg estimate on the half-ball yields
\[
 c\lambda^\beta\le\int_{B(0,1/2)}(dd^c v)^n
 \le C_n(-v(0))^n.
\]
Consequently
\[
 s(\varepsilon_k)-s(0)\ge
 c\,\varepsilon_k^{\,\gamma},
 \quad \gamma=\frac{2\alpha+2(n-1)+\beta}{n\alpha}
 =2-\frac{N(\alpha-1)-\beta}{n\alpha}<2.
\]
If \(u\) were \(C^{1,1}\) near zero, rotation invariance in \(w\) would imply \(\nabla_wu(0)=0\) and \(s(t)-s(0)=O(t^2)\), contradiction.

**Explicit check:** In complex dimension \(n=3\), take \(r=3,\alpha=8,\beta=26\). Then \(\beta-r\alpha=2>0\), \(\beta<4(\alpha-1)=28\), and
\(\gamma=(16+4+26)/(3\cdot8)=23/12<2\). The construction therefore has a \(C^3\) right side and lacks an interior \(C^{1,1}\) solution.

**Sharpness for this method, not the general equation:** the two strict parameter inequalities require \(r<2(n-1)\). They cannot produce \(C^{2n-2}\) densities with this exact anisotropic rescaling; **no claim** is made that such densities always yield \(C^{1,1}\) solutions.

**Dependencies and limitations:** The existence/uniqueness theorem for continuous-density complex MA Dirichlet, bounded Bedford–Taylor maximality/comparison, and the CLN bound are used **conditionally** from the existing integrated text. We checked the scaling determinant, regularity powers, and barrier argument but did not globally recertify these results. This is distinct from earlier `POME-KLIM-PLIS-PARAM-001`, which checked \(\alpha,\beta\) for \(C^2\) only.

**Proposed source change:** optional corollary/remark immediately after §7.24.1 giving \(3\le r\le2n-3\), with the strict inequalities and no endpoint assertion. Keep original attribution, theorem and permanent tag. Affected dependent discussion: Dirichlet regularity limits in §7.24 and later §15 smooth/degenerate equations; this does *not* replace their precise \(f^{1/n}\) hypotheses.

## POME-SEPMAX-WEIGHTED-TORUS-001 — exact polytorus mass, no multinomial

**Status:** verified conditional deduction; **severity:** low; not a false §7.33.3 statement.
**Exact anchors:** §7.33.3, permanent tag `F8604F30C7C6`, source `isolated-plurisubharmonic-singularities-DE8582D3`, `docs/sections/separated-maximum-monge-ampere-products/index.html`, blob `a859ac5637379266fa191831656f214c51676ca1`, lines 39–79; convex Alexandrov measure §21.5.1 `409656CC47D4`, and local toric Jacobian normalization §21.12.24 `725063C1ED05`, `docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html` blob `56a1a55dfc8185aee0e6d495a6a93d8a2313d76b`, lines 466–529 (only local toric change of variables is used, not any multiplier-ideal result).

Fix positive weights \(\lambda_i\) and radii \(R_i\) in \(\mathbb C^p\), and write
\[
 f(z)=\max(0,\lambda_1\log(|z_1|^2/R_1^2),\dots,
                 \lambda_p\log(|z_p|^2/R_p^2)).
\]
This is locally bounded nonnegative psh. Let \(m_R\) denote normalized Haar probability on \(\{|z_i|=R_i\}_{i=1}^p\). Then
\[
 \boxed{(dd^c f)^p=\Bigl(\prod_{i=1}^p\lambda_i\Bigr)m_R.}
\]
Indeed \(f=F(\log|z_1|^2,\dots,\log|z_p|^2)\) with piecewise-linear convex \(F\). Its subgradient has full dimension only at \(x_R=(\log R_i^2)_i\), and
\[
 \partial F(x_R)=\operatorname{conv}(0,\lambda_1 e_1,\dots,\lambda_p e_p).
\]
The Alexandrov measure with the book's \(p!\) convention is
\(p!\operatorname{vol}(\partial F(x_R))\delta_{x_R}
  =(\prod_i\lambda_i)\delta_{x_R}\).
The local toric Jacobian formula and monotone bounded Bedford–Taylor convergence give the displayed complex mass on \((\mathbb C^*)^p\); compact-torus invariance makes its conditional angular measure Haar. Near each coordinate hyperplane the corresponding logarithm is inactive and \(f\) is independent of that coordinate, so the top product has no additional mass there. The resulting measure is supported on \(\{f=0\}\), satisfying the printed theorem's nonpositive-locus assumption.

For analogous \(g(w)\) with \(q\) weights \(\mu_j\) and radii \(S_j\), put \(h(z,w)=\max(f(z),g(w))\). The exact §7.33.3 identity now gives
\[
 \boxed{(dd^c h)^{p+q}
   =\Bigl(\prod_i\lambda_i\prod_j\mu_j\Bigr)
      m_R\otimes m_S.}
\]
There is **no** binomial/multinomial coefficient. As an independent normalization check, the convex function for \(h\) is the maximum of \(0\) and all \(p+q\) coordinate affine forms; its gradient simplex has volume \((\prod\lambda_i\prod\mu_j)/(p+q)!\), canceling the Alexandrov factorial. This is a concrete weighted model **distinct** from previously logged `POME-BT-SEPMAX-MULTIBLOCK-001` (the abstract induction to many blocks).

**Proposed change:** optional explicit example after §7.33.3, documenting angular Haar measure and the factorial convention. Keep both original permanent tags. Affects cross-checks in §§7.33,21.5,21.12 and avoids normalization mistakes in separated maximum constructions. Conditional on the established real Alexandrov/BT monotone theory; no whole-chapter certification.

## Other genuinely inspected proof steps; no new IDs

- **§7.25:** `docs/sections/boundary-zero-green-functions-and-hyperconvexity/index.html`, blob `4680003b95a90211015a03b44bd634eb331fb426`, §7.25.1 tag `B63D9FDC459B` lines 8–33 and §7.25.2 tag `033C98D473B9` lines 37–58. Checked use of compact-ball normalization \(q=-1\) on \(K\), the sign of the pasting inequalities \(q>-\varepsilon/2\ge H_t-\varepsilon\), and the lower-semicontinuity conclusion; reviewed Green boundary-limit implication. No defect established, and global Green continuity inputs are not newly certified.
- **§9.12:** `docs/sections/separate-holomorphy/index.html`, blob `2eafedb77d4a45f0133a5d92e27ad16b0be44ffd`, Theorem 9.12.1 tag `362351A63FB6`, source `klimek-pluripotential-theory-120C7FB1`, lines 8–51. Checked the Baire closed-set cover, holomorphy in the lower-variable block by induction, and coefficient subharmonic Hartogs control. No theorem error found; the Hartogs lemma itself remains a pre-existing upstream input.
- **§7.33:** explicitly crosschecked that differentiating \((h-f)C^k=(h-f)B^k\) produces \(C^{k+1}-AC^k=CB^k-AB^k\) without a missing coefficient, and that only two \(C\)-terms survive in total degree \(p+q\). No new erroneous proof step.

## Reproducible finite arithmetic check

The accompanying `checks/check_deg_density_creg_parameters.py` uses exact rational arithmetic for all integers \(3\le n\le12\), \(3\le r\le2n-3\). It verifies the strict derivative, gap and exponent inequalities in **100** cases, including the \((3,3,8,26,23/12)\) example. It cannot verify regularity, the PDE comparison argument or the Alexandrov measure theorem. This session did **not** run project builds, CI, published-site updates or formal proof verification.

**Audit classifications:** both numbered findings are `verified conditional deduction`, not `confirmed error`, `proof gap` or `verified repair`. Previously outstanding and user-deferred records stay unchanged.