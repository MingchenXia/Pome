# Mathematical audit: root-integrable damping and high-moment concentration

**Checkpoint:** 2026-10-23 17:33 Asia/Shanghai. **Fresh main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Existing audit branch was f3435da74f5eb748d1d15529b04f3f600ceec4f8 before this write. Selected nonexcluded proof inspection only; no whole-section or full-project certification. Demailly regularization/approximation and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss completion programme remain **deferred-by-user**, neither examined nor resolved.

## Actual sources and review limits

- **13.15 Weighted Monge–Ampère measures:** docs/sections/weighted-monge-ampere-measures/index.html, main blob 37d9ae29e4861e1f280be6450b2c842b5ce452a3, source variant non-kahler-pluripotential-theory. Direct reading of Proposition 13.15.2, permanent tag 57A94BD59310 (statement line 33; bounded-range mixed-mass proof approximately 39–79); Lemma 13.15.3 tag 357B2DE7779E (approximately 86–101); Proposition 13.15.6 tag 8B51BF8706B7 (110–135); Theorem 13.15.7 tag 4394319FDE01 (139–156); Theorem 13.15.9 tag EE93EE2035F6 (168–211); Theorem 13.15.11 tag B72AF5B37CB7 (224–251); and selected finite-depth/tail proof steps of 13.15.13–15. Audited positivity directions, truncation restrictions, capacity normalization, and distinction between the thresholds q>n-2 and q>n. The proof of Proposition 13.15.2 cites a regularization step; **this excluded upstream step was only logged and was not investigated**. Its conclusion is used conditionally below.
- **13.14 Non-pluripolar Monge–Ampère measures:** docs/sections/non-pluripolar-monge-ampere-measures/index.html, main blob 5d0f652ffaaaef81cf74d1786082e429f71b3b89, same source variant. Direct reading of Theorem 13.14.18 tag AEE72111FEDA (280–336), Proposition 13.14.21 tag D889AEAF2866 (371–435), Corollary 13.14.22 tag 1D7A78F6BD02 (445–471), and Corollary 13.14.23 tag BED3510B9193 (475–514). §§13.14.2–8 were consulted for extended-measure locality only.
- **Narrow internal checks:** Lemma 5.26.2, tag 88C7A8DCE36E, docs/sections/plurisubharmonic-functions-and-singularities--uniform-exponential-integrability/index.html:18–55, blob d961c0412577bb6abdb8455efc44e2f35760c55c; bounded chain rule Eq. 5.27.9, tag B4EA93FC61EE, docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html:179ff, blob ddb2ac8d9de27a22152872e07e5e787d138a790e. Earlier global Bedford–Taylor theory remains conditional, not transitively certified.

## POME-NPP-WEIGHT-ROOTCAP-001

**Status:** verified conditional deduction; **severity:** low for existing printed results, useful improvement for rapidly decaying weights. **Not a false theorem or duplication.**

Let X be compact Hermitian of complex dimension n≥1, with form omega, and let w:[0,infinity)→(0,infinity) be C1 and nonincreasing. Assume

\[
 A=\int_0^\infty \left(\frac{w(s)}{w(0)}\right)^{1/n}ds<\infty.
\]

For every u∈PSH(X,omega) with u≤0, put

\[
 F(t)=\int_{-\infty}^t\left(\frac{w(-a)}{w(0)}\right)^{1/n}da,\quad t\le0,\qquad F(-\infty)=0.
\]

Then F(u) is bounded omega-psh, 0≤F(u)≤A, and there is an inequality of positive Borel measures

\[
 \boxed{w(-u)\,\mathrm{MA}^{\mathrm{ext}}_\omega(u)
 \le w(0)\,\mathrm{MA}_\omega(F(u)).} \tag{1}
\]

In particular, B=max{1,A} and r_n=max{n-2,0} give, for every Borel E,

\[
 \boxed{w(-u)\mu_u(E)\le w(0)B^n\operatorname{Cap}_\omega(E),\qquad
 (w(-u)\mu_u)(X)\le w(0)C_\omega(1+A)^{r_n}.} \tag{2}
\]

The mass bound invokes the existing Proposition 13.15.2 **conditionally**. The **linear capacity** bound follows independently of that range estimate from the capacity definition and bounded Bedford–Taylor products.

**Complete deduction.** Set g(t)=(w(-t)/w(0))^(1/n) on t≤0. Since w decreases, g increases, 0≤g≤1 and F'=g, F''=g'≥0. For bounded u, the chain rule yields

\[
 \omega+dd^cF(u)
 =g(u)(\omega+dd^cu)+(1-g(u))\omega+g'(u)\,du\wedge d^cu.
\]

Every summand is positive; taking the n-fold bounded product gives MA(F(u))≥g(u)^n MA(u), precisely (1). For unbounded u apply this on u_T=max(u,-T), restrict to {u>-T}, use plurifine locality of both products and let T→infinity. The extended measure and the bounded MA product give no mass to the pole set, so no assumption of finite mass of μ_u is required. Finally F(u)/B is an admissible capacity test, and

\[
 B(\omega+dd^c(F(u)/B))=(\omega+dd^cF(u))+(B-1)\omega\ge\omega+dd^cF(u),
\]

hence MA(F(u))≤B^n MA(F(u)/B), proving the first part of (2). The second follows from the stated range proposition.

**Strict improvement in a subrange.** If w(s)=(1+s)^(-q) and q>n, then

\[
 F(t)=\frac{n}{q-n}(1-t)^{1-q/n},\quad A=\frac{n}{q-n},
\]
\[
 \boxed{(1-u)^{-q}\mu_u(E)\le
 \max\{1,n/(q-n)\}^{n}\operatorname{Cap}_\omega(E).} \tag{3}
\]

For q>n, (3) is a **linear**, rather than the sublinear power-capacity estimate printed in Theorem 13.15.11. That theorem retains its broader validity for q>r_n; it is not redundant or false. Exponential w(s)=exp(-ps) yields A=n/p and recovers exactly Proposition 13.15.6/Theorem 13.15.7. No sharpness claim is made for the q>n threshold.

**Suggested patch:** independent bounded-convex-composition corollary after Proposition 13.15.6, with polynomial remark after Theorem 13.15.11. Retain historical attribution and all original tags. Potential dependents: weighted cutoff/continuity results §13.15, not newly certified.

## POME-HERM-EXP-LR-001

**Status:** verified conditional deduction; **severity:** low; quantitative enhancement, not a source-theorem error.

Under precisely the hypotheses of Corollary 13.14.23, let smooth omega-psh u_j satisfy sup_X u_j=0, let w_j=s_j u_j with 0<s_j<epsilon_j→0, and let their Monge–Ampère masses be *arbitrarily prescribed* b_j>∫omega^n. Choose alpha>0,C<infinity from Lemma 5.26.2, so ∫exp(-alpha u_j)dV≤C. For every fixed p>0 and finite real r≥1, eventually

\[
 \boxed{\|w_j\|_{L^r(dV)}
 \le\frac{r}{e\alpha}C^{1/r}\epsilon_j,\quad
 \|e^{-pw_j}-1\|_{L^r(dV)}
 \le\frac{2pr}{e\alpha}C^{1/r}\epsilon_j.} \tag{4}
\]

**Proof.** Put h_j=-u_j≥0. For x≥0, x^r≤(r/(e alpha))^r exp(alpha x). This proves the first bound. For large j, pr s_j≤alpha/2. Using (e^y-1)^r≤y^r e^(ry) for y≥0, and x^r e^((alpha/2)x)≤(2r/(e alpha))^r e^(alpha x), we obtain

\[
 (e^{p s_j h_j}-1)^r
 \le(p s_j)^r h_j^r e^{pr s_j h_j}
 \le(p s_j)^r(2r/(e\alpha))^r e^{\alpha h_j}.
\]

Integrate and take rth roots. Both estimates hold independently of b_j, even when prescribed b_j diverges arbitrarily fast.

The same argument for **the single unbounded** U of Theorem 13.14.18 (which has exponential moments of every order) gives ||exp(-p epsilon U)-1||_r=O_{p,r,U}(epsilon) and ||epsilon U||_r=O_{r,U}(epsilon). Nevertheless Corollary 13.14.22 still gives infinite extended MA mass and infinite pointwise determinant integral for every epsilon>0. This illustrates, without contradicting any Pome theorem, that strong Lr control of the potentials and their exponential weights does not control nonlinear MA masses.

**Suggested patch:** optional quantitative corollary near Corollary 13.14.23 and accompanying warning after 13.14.22. Preserve the distinction between smooth prescribed-mass and unbounded infinite-mass constructions.

## Validation and scope

The small exact SymPy helper checks/check_root_weight_damping.py evaluates 175 scalar derivative and normalization identities for polynomial/exponential weights, not current theory. This session did **not** run the Pome build, CI, website publication, formal verification, or source/registry/permanent-tag changes. Only selected mathematical passages of §§13.14–15 were reviewed; the cumulative 747-section index is a **catalog**, not certification. The dedicated Demailly regularization, Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains wholly **deferred-by-user**.