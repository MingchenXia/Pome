# 2026-10-29 — Conformal Kähler Hessian comparison and an irreducible nodal cubic

**Production main inspected:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read afresh). **Audit branch before this checkpoint:** `4e3f1681dbbb663d45aab76baf08770b65dab477`. This review uses only public integrated reading-edition HTML. No dedicated Demailly regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof work was reopened.

## POME-HESS-CONFORMAL-KAHLER-MASS-001

**Classification:** low / **verified conditional deduction**; original Theorem 8.13.4 and Example 8.13.5 are correct. This is a new compact-manifold family and a precise within-conformal-class characterization, not a new incorrect theorem.

**Pinned integrated references:** `docs/sections/complex-hessian-equations/index.html` line 7 (global standing restriction `2 <= m < n`); `docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html`, blob `580d3bc2b10ebd01d880b2a31fc6930436570aac`, Theorem **8.13.4**, permanent tag `53F870DE5980`, physical lines **70–121** (especially mass polynomial 100–118 and comparison 120); Example **8.13.5**, tag `0DB9D80DE230`, lines **129–150**. Section tag `B908310EE8A2`. The relevant source variant is `non-kahler-pluripotential-theory`.

**Claim (in the actual intermediate-Hessian domain).** Let `(X,beta)` be any connected compact Kähler manifold of complex dimension `n >= 3` and `omega=e^phi beta` for smooth real `phi`. For every `2 <= m < n`, the ordinary unmodified bounded-admissible `m`-Hessian comparison principle for `omega` holds **if and only if** `phi` is constant. If `phi` is nonconstant, there is a **single smooth strictly admissible potential** `u`, independent of `m`, and a constant `C>sup_X u` for which, for all intermediate `m`,
$$
\{u<C\}=X,\qquad \int_X H_m(C)=\int_X\omega^n>\int_XH_m(u).
$$
Thus comparison fails even on the underlying Kähler manifold: the **chosen nonclosed Hermitian background**, not the complex manifold, is decisive.

**Self-contained proof of the obstruction.** Set `f=e^{(n-1)phi}`. Since `beta` is closed,
$$
\omega^{n-1}=f\,\beta^{n-1}.
$$
For every `m` in the stated range, consider the smooth mass polynomial
$$
P_m(t)=\int_X(\omega+t\,dd^cf)^m\wedge\omega^{n-m}.
$$
Its first variation at zero is
$$
\begin{aligned}
P_m'(0)
&=m\int_X dd^cf\wedge\omega^{n-1}\\
&=m\int_X f\,dd^cf\wedge\beta^{n-1}\\
&=-m\int_X df\wedge d^cf\wedge\beta^{n-1}<0.
\end{aligned}
$$
The last equality is Stokes on compact `X`, and the last strict inequality holds exactly when `f` is nonconstant, because `df wedge d^c f` is a semipositive real `(1,1)`-form with strictly positive `beta`-trace where `df != 0`. This is consistent with the project's `dd^c=(i/2pi)partial barpartial` convention. Since `omega` is positive, `omega+t dd^c f` stays positive for sufficiently small `t>0`, hence `u=tf` is smooth and strictly admissible for **every** intermediate `m`. There are finitely many such `m`, so choose one `t>0` for which `P_m(t)<P_m(0)` for all of them. Choose `C>sup_X tf`. Then `u<C` everywhere and `H_m(C)=omega^n`, so ordinary comparison would require `P_m(0)<=P_m(t)`, a contradiction. When `phi` is constant, `omega` is Kähler and all `dd^c(omega^{n-q})` vanish, so the sufficient direction follows from the precisely stated Theorem 8.13.4. No theorem beyond the stated internal comparison characterization is independently certified.

**Why distinct from old findings.** The printed Example 8.13.5 uses a special torus metric with one oscillating coefficient. This result works for **every** compact Kähler `X`, any nonconstant conformal factor, every allowed `m` simultaneously, and displays a canonical strict first variation. The earlier §14.12 surface Gauduchon-adjoint example concerns `n=2` and a different operator, so is not being repeated.

**Suggested action and dependents:** optional new example/remark under §8.13.4; no change to the mathematical statement. Relevant to §8.13.3–.4's comparison-versus-mass characterizations and §8.13.8's modified comparison (which is **not** contradicted). The general bounded Hessian-current convergence and comparison inputs are not recertified.

## POME-NORM-IRREDUCIBLE-NODAL-CUBIC-001

**Classification:** low / **verified conditional deduction**; printed normalization and unibranch statements are correct.

**Pinned integrated references:** `docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html`, blob `06439f43d1ce8e83d2529682c9a630bffa3d9c22`; Theorem **9.4.6** tag `12A47DB401E2` lines **142–163** (unique finite bimeromorphic normalization and branch fibers), Corollary **9.4.9** tag `EE1633042D3D` lines **185–192**, and Example **9.4.10** tag `60A14C7A1845` lines **197–200** (reducible node and unibranch cusp). Section tag `C16A2F5D9879`. Source variant `foundations-of-pluripotential-theory`.

**Claim.** The projective cubic
$$
C=\{[X:Y:Z]\in\mathbf P^2:Y^2Z=X^2(X+Z)\}.
$$
is **globally irreducible**, but its germ at `P=[0:0:1]` has **two analytic branches**. Its normalization is the finite birational map
$$
\nu:\mathbf P^1\longrightarrow C,\qquad
[S:T]\longmapsto [S(T^2-S^2):T(T^2-S^2):S^3].
$$
The fiber over `P` consists of `[1:1]` and `[1:-1]`; at the node `delta_P=dim_C(widetilde{mathcal O}_{C,P}/mathcal O_{C,P})=1`, and the conductor inside the local normalization is precisely the pairs of germs vanishing at their respective origins. Therefore *global irreducibility does not imply the local unibranch condition*. In particular, this normalization is not a homeomorphism, without contradicting Corollary 9.4.9.

**Explicit proof.** All three coordinate forms above have degree three and no common projective zero (at `S=0`, `Y=T^3!=0`; for `S!=0`, `Z=S^3!=0`). They satisfy the cubic identity by direct substitution: `Y^2 Z = S^3 T^2(T^2-S^2)^2 = X^2(X+Z)`. On `S!=0`, write `t=T/S`; then `x=X/Z=t^2-1`, `y=Y/Z=t(t^2-1)`. When `x!=0`, `t=y/x` is the inverse rational function. Thus `nu` is birational and its image is the whole cubic, which is irreducible as a continuous algebraic image of `P^1`. As a nonconstant morphism of projective curves, `nu` is proper with finite fibers, hence finite. Its source is smooth, so Theorem 9.4.6 identifies it as the normalization. The preimages of `P` solve `t^2=1`, giving exactly two points.

On the affine chart `Z=1` near `P`, the equation is `y^2=x^2(1+x)`. Choose the holomorphic square root `h(x)=sqrt(1+x)` with `h(0)=1`, and put `w=y/h(x)`. The completed/local analytic equation becomes `(w-x)(w+x)=0`, displaying the two smooth transverse branches. The normal local algebra is `B=C\{x\}oplus C\{x\}`; the local curve algebra identifies with
$$
A=\{(g_+,g_-)\in B:g_+(0)=g_-(0)\}.
$$
Indeed restriction of a germ `F(x,w)` to `w=+x` and `w=-x` has equal constants, and for any such pair the formula
$$
F(x,w)=\frac{g_+(x)+g_-(x)}2+
\frac{g_+(x)-g_-(x)}{2x}\,w.
$$
is holomorphic and realizes it. Thus `B/A ~= C` (difference of constants), and the conductor `{b in B : bB subset A}` consists exactly of the pairs with both constants zero. This direct local computation proves `delta_P=1`.

**Suggested action and dependents:** optional example after §9.4.10 contrasting a *globally irreducible* nodal cubic with the reducible coordinate cross and the unibranch cusp; reinforces exact hypotheses of Theorem 9.4.6 and Corollary 9.4.9. No source theorem or proof is identified as false. The earlier coprime monomial-cusp conductor example `POME-NORM-MONOM-CONDUCTOR-001` is **not** repeated.

## Coverage and limitations

**New direct proof/statement inspection:** standing scope §8.1 (line 7), selected Theorem §8.13.4 and Example §8.13.5; Theorem §9.4.6, Corollary §9.4.9 and Example §9.4.10. **Context only, not certified:** adjacent §8.13.3 and §8.13.8–.12; §8.9–.12 Hessian-current convergence and torsion/capacity steps (sampled to check scope, not fully proved); §9.3.1 and §9.5.1. This is not a complete section/chapter audit. The existing actual ToC inventory is **25 chapters / 747 numbered sections / 0 fully certified sections**. Prior confirmed errors, proof gaps, deferred dependencies, and historical labels are untouched.

All Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, **not** resolved or certified. These deductions are independent of that excluded programme.

Only audit Markdown is proposed for `review/mathematical-audit`; no edits to `main`, mathematical body, source, registry, permanent tags, site, GitHub Actions, or formalization. No software build, browser test, CI, or formal proof was performed.
