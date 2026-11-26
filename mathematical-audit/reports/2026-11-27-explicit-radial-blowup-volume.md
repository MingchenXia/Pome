# 2026-11-27 — Explicit radial solutions in the one-blowup order model

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Direct reading of the integrated HTML, not source numbering. Audit only; no source or production change. All designated Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain deferred-by-user, not resolved. None is reopened here.

## Coverage and anchors

- Entire mathematical content of §12.22, physical lines 7–108, docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--comparison-under-an-arbitrary-modification/index.html, blob 2752af2181f07f54695112f0007173b9e4dad128. Lemmas 12.22.1 (0A017BFF9468, source 9F4393DE), 12.22.3 (51797AE0DE1F, source AAF8E58D), Proposition 12.22.5 (8AB4DFD2719F, source 249AEE03). Historical selected review of 12.22.3 (POME-GAUD-MODIF-TEST-DDC-CLOSEDNESS-SHARP-001) is retained, not counted anew.
- Entire mathematical content of §12.23, physical lines 7–96, docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--strict-changes-under-one-blowup/index.html, blob 44644097cffbe33a98a2984623353827b8298fcd. Proposition 12.23.1 (1E30136A67F6, source F3889ABB), equations (12.23.2) 48EE58E16325 / D2C0DDD8, (12.23.3) 61B56EB11C84 / 9D859AFD, (12.23.4) F24A79D3D80E / 546D2583, (12.23.6) 85080CF9B131 / 836D3D8F.
- Selected §§12.2.1–3, physical lines 7–80, docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html, blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e; Theorem 12.2.3 tag 2DB664A6EFDF. Only the quotient, pointwise AM–GM, and smooth Stokes are needed in the new proof.
- Chapter 12 actual section list compared with the existing matrix. Historic first visits are not asserted. No full transitive proof chain certified.

## POME-GAUD-BLOWUP-RADIAL-EXPLICIT-SOLUTION-001

Severity low; status **verified conditional shorter proof** (not a false printed theorem). Proposition 12.23.1, Step 2, lines 32–77, invokes the general smooth Hermitian Monge–Ampère existence theorem 14.2.1 to produce a Kähler solution on the base. That invocation is legitimate but avoidable in this radial model. The following explicit solution also removes the need for general conformal Gauduchon existence from this calculation, since the minimizing test is explicitly balanced.

Retain exactly the hypotheses and normalization of 12.23.1: m>=2, p,k>=1, b>0, epsilon>0, H normalized by int H^m=1, and the radial smooth q of lines 24–30 (equal to s^k near 0, constant positive for large s). Set s=|z|^2 and t=log s. On the downstairs P^m let x=b+epsilon, y=0 and nu=H^m. Upstairs on the point blowup set x=b+epsilon, y=epsilon and nu=(H+L)^m/(2^m-1). In each case let A=xH+yL (omit L downstairs), g=q+epsilon, M=(x+y)^m-y^m, J=int g^{-p} nu, and J(s)=int_{|z|^2<s} g^{-p} nu, interpreted on the blowup by inverse image. All these numbers are positive for s>0, J finite, and the smooth probability nu has no mass on the boundary divisors.

Define the radial derivative
\[
 h(s)=\left(y^m+M\,J(s)/J\right)^{1/m}.
\]
For t real choose F with F'(t)=h(e^t). Define
\[
 u=F(t)-x\log(1+e^t)-yt.
\]
On the dense punctured affine chart, h>0 and dh/ds>0, so alpha=dd^c F(t) is positive: its tangential eigenvalue is proportional to h/s and radial eigenvalue to dh/ds. The normalized radial Monge–Ampère flux formula in §12.23 lines 45–51 gives the cumulative mass h(s)^m-y^m=M J(s)/J. Differentiation identifies the smooth radial densities (both are U(m)-invariant and disintegrate into the same uniform angular probabilities). Thus alpha^m=(M/J)g^{-p}nu on the chart.

**Smoothness and strict positivity at the two ends, not just equality on a dense open set.** Write the densities from (12.23.2) explicitly. Downstairs Xi=(s/(1+s))^m, so Xi'=m s^{m-1}(1+s)^{-m-1}; upstairs Xi'=m(1+s/(1+s))^{m-1}(1+s)^{-2}/(2^m-1). Since g is positive smooth in s including 0, downstairs J(s)=s^m a(s) with a smooth a(0)>0, and upstairs J(s)=s a(s) with a smooth a(0)>0 (integration after substituting the integration variable s v proves smoothness). Consequently h(s)=s A_0(s), A_0(0)>0 downstairs, and h(s)=y+s A_0(s), A_0(0)>0 upstairs. In both cases A_0 is smooth: downstairs take the positive m-th root of a positive smooth factor, upstairs expand the smooth m-th root at y^m>0. Hence F(t)-yt has a smooth extension as a function of s, with derivative A_0(0)>0 at 0. Downstairs this gives a smooth strictly positive Hessian at the origin. Upstairs in a blowup chart s=|w|^2(1+|v|^2); after removing y log|w|^2, a local potential is y log(1+|v|^2)+smooth function of s, so along w=0 the tangential form is positive (y>0), and the normal coefficient is A_0(0)(1+|v|^2)>0, with no cross term at w=0. The reference potential has the same y log|w|^2 singular term, so u itself extends smoothly.

At infinity let r=1/s. From the same explicit densities and q constant for large s, J-J(1/r)=r a_infty(r), smooth a_infty(0)>0 in both cases (differentiate Xi(1/r) at 0). Thus h(1/r)=x+y-r A_infty(r), A_infty smooth and positive at 0. Integrating dF/dt shows F(t)-(x+y)t extends smoothly as a function of r with positive derivative A_infty(0). Near the hyperplane at infinity use projective coordinates w=Z_0/Z_j and v=(Z_i/Z_j) for i!=0,j, so r=|w|^2/(1+|v|^2). Removing -(x+y)log|w|^2 gives a local potential (x+y)log(1+|v|^2)+smooth function of r, strictly positive along w=0 by the same tangential/normal argument. The reference potential has the identical logarithmic term. This proves smooth global u and strict positivity of A+dd^c u, including the exceptional divisor and hyperplane at infinity. Equality of the smooth top forms extends globally.

On the product with P^p take Omega=alpha+g omega, and gamma=g^{-p/(n-1)}Omega, n=m+p. Direct wedge expansion is exactly (12.23.3), so d(gamma^{n-1})=0: one coefficient multiplies a base top form, and the other term is closed. Also
\[
 \Omega^n=\binom{n}{m}(M/J)\,\nu\wedge\omega^p.
\]
For every Gauduchon test G, smooth Stokes replaces the numerator pairing with the perturbed background by the pairing with Omega. Pointwise AM–GM yields quotient >= [binom(n,m)M/J]^{1/n}, with equality for the explicitly balanced gamma. Therefore the variational volume is binom(n,m)M/J, as in (12.23.4). No existence of a general Hermitian MA solution or conformal Gauduchon representative is needed in this model; the radial flux, explicit Kähler forms and elementary quotient calculation suffice. This is a proposed alternative for Step 2, not a change of statement, of normalization or of attribution.

The positive-coefficient assumption epsilon>0 is essential in the above smooth positivity argument; the limit epsilon=0 is not claimed to be a smooth solution. No regularization is used.

## Remaining direct checks

§12.22: the vertical kernel of the pulled-back metric in a smooth-center blowup is the projective fiber tangent space; the curvature of O(-E) is positive there. The compactness argument gives a uniform metric after scaling, and iteration retains an effective exceptional divisor. In Lemma 12.22.3 the correction pairing vanishes because the rank on each exceptional component is at most n-2, and Stokes/Poincaré–Lelong is applied to a smooth dd^c-closed test. The degree-one change of variables is used only with top forms. In Proposition 12.22.5, the positive cofactor matrix has unique positive (n-1)-st root, its determinant to the power 1/n is continuous on the semidefinite cone, the limit denominator is strictly positive, and the infimum is taken only after obtaining the bound for each test. Dividing by negative log epsilon reverses the order. The allowed Hironaka elimination input at line 10 and Gauduchon existence in Step 2 remain explicit dependencies; no proof of them asserted. The rescaling of epsilon by K is harmless: the root volume is monotone in epsilon and bounded between epsilon times the positive root volume of h_X and a fixed finite upper bound for 0<epsilon<=1, by 12.2.1–2, so the logarithmic ratios are bounded and log(K epsilon)/log epsilon tends to 1.

§12.23: checked the two cumulative mass densities and total mass M, the binomial coefficient and balanced wedge expansion, and the three regimes of (12.23.6). For kp>d the rescaling has integrable limiting density v^{d-1}(1+v^k)^{-p}; for kp=d substitution t=s^k gives the coefficient a/k of log(1/epsilon), and for kp<d the limiting density is integrable. Example m=k=2,p=1 uses B(1/2,1/2)=pi, coefficient pi/3 upstairs, coefficient 1 downstairs; m=2,k=p=1 has coefficient 2/3 upstairs. The printed orders and arbitrary positive integer increases follow. No new false theorem or proof gap identified in these two sections.

Affected dependents: the exact volume identities (12.23.4), subsequent orders and examples of Proposition 12.23.1, and comparisons with Proposition 12.22.5. This is a local alternative proof, not certification of the general existence theorem or a revision of any other chapter.

## Summary

Two whole direct conditional mathematical sections, one selected dependency, one verified conditional shorter proof, zero newly confirmed errors or demonstrated gaps, zero complete transitive certifications. No builds, tests, CI, permanent-tag, source, registry, main or website edits.
