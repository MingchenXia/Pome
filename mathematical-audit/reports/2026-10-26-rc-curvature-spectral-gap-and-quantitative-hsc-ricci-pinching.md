# 26 October 2026 — exact RC-curvature spectral margin and a quantitative Ricci/HSC pinching inequality

## Audit checkpoint and scope

- **Reviewed current `main` SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Audit starting branch:** `review/mathematical-audit` at `62d2b5e0bb67c2f50fe96d46407d3e434820e474` (never reset).
- Freshly read: `AGENTS.md`, `documentation/proof-expansions.md` on current `main`; `README.md`, `mathematical-audit/LATEST.md` and the existing coverage/ledger on the audit branch.
- **First selected theorem/proof-level inspection:** §11.27, especially Lemmas 11.27.1–2 and Theorem 11.27.4; §11.28, especially Lemma 11.28.2, Proposition 11.28.3, Corollary 11.28.5 and Proposition 11.28.7. §11.26.2 and §11.26.3 were consulted only for the interpretation of RC-positivity. No whole section or transitive chain certified.
- This report has no connection to Demailly approximation/regularization, Bergman, `L²`, Ohsawa–Takegoshi, multiscale atlases or positivity-loss proof completion. All prior related records remain **deferred-by-user**, not resolved.

## POME-RC-CURVATURE-SPECTRAL-GAP-001

**Status:** verified conditional deduction. **Severity:** low; printed Lemma 11.27.1 is not false and needs no correction.

**Exact integrated source:** `docs/sections/gauduchon-metrics-and-linear-mass--ricci-flat-kahler-surfaces/index.html`, main blob `119ac604fd60b412ecb7d51910cfcecc04b3b7cf`. The standing compact Ricci-flat Kähler surface convention is at physical lines 10–34; Lemma **11.27.1**, permanent tag **`00DBBF153DBA`**, source `non-kahler-pluripotential-theory-E530CFDA`, is at lines **37–60**, especially the curvature formula at **44–47** and the anti-self-dual projection and norm at **52–60**. Related RC-positivity criterion: `docs/sections/gauduchon-metrics-and-linear-mass--conformal-changes-and-directional-curvature-positivity/index.html`, main blob `d54016b202422bde3bc5e2c6e493e4618918a7d7`, Lemma 11.26.2, tag `23EB10AE428C`, lines 23–29.

**Claim and exact normalization.** At a point `x`, let `A_x:\Lambda^-_x\to\Lambda^-_x` be the real self-adjoint trace-free curvature operator of the Ricci-flat Kähler metric `g`. For every nonzero tangent-bundle fiber vector `v`, let `\alpha_{h,v}` be its directional Chern-curvature real `(1,1)`-form, and let `\lambda_{\max}^g(\alpha)` be the largest eigenvalue relative to `\omega_g`. Then

\[
\boxed{\inf_{v\ne0}\frac{\lambda_{\max}^g(\alpha_{h,v})}{|v|_h^2}
       =\frac12\sigma_{\min}(A_x)
       =\frac12\min_{\lambda\in\operatorname{Spec}(A_x)}|\lambda|.}
\]

Here all form norms are the *real* Hilbert–Schmidt norms from §11.27, **not** a Chern-normalized `dd^c` rescaling. In particular, this margin is positive exactly on the open invertibility locus of Lemma 11.27.1, and its precise dependence on the smallest absolute curvature eigenvalue is explicit.

**Proof.** At `x`, write `v=(V-iJV)/2` for a real tangent vector `V`. The integrated proof gives

\[
 |v|_h^2=\frac{|V|_g^2}{2},\qquad
 \Pi(V)=V\wedge JV-\frac{|V|_g^2}{2}\omega_g,\qquad
 |\Pi(V)|_g=\frac{|V|_g^2}{\sqrt2},\qquad
 \alpha_{h,v}=\frac12(A_x\Pi(V))^\flat .
\]

The last form is real primitive `(1,1)`: `A_x\Pi(V)\in\Lambda^-`. In a unitary real frame any such form has eigenvalues `s,-s` relative to `\omega_g`, with real form norm `\sqrt2\,|s|`. Consequently

\[
 \lambda_{\max}^g(\alpha_{h,v})
   =\frac{|\alpha_{h,v}|_g}{\sqrt2}
   =\frac{|A_x\Pi(V)|_g}{2\sqrt2}.
\]

Put `w=\sqrt2\Pi(V)/|V|_g^2`. Then `|w|=1` and

\[
 \frac{\lambda_{\max}^g(\alpha_{h,v})}{|v|_h^2}
 =\frac{|A_x\Pi(V)|}{\sqrt2|V|_g^2}
 =\frac{|A_xw|}{2}.
\]

Lemma 11.27.1 proves not just nonvanishing but *surjectivity* of `V\mapsto\Pi(V)` onto the nonzero elements of `\Lambda^-` (lines 57–58), so `w` ranges over the entire unit sphere of `\Lambda^-`. Taking its infimum gives `\frac12\sigma_{\min}(A_x)`. For a diagonal check, `V=e_1` and `A\Pi(V)=\lambda\Pi(V)` yield `\alpha=(\lambda/4)(e_1\wedge Je_1-e_2\wedge Je_2)`, whose normalized positive eigenvalue is `|\lambda|/2`.

**Dependencies and proposal.** The new equality assumes the curvature identification, Hodge conventions, and Ricci-flat Kähler setting already stated in Lemma 11.27.1. No independent reproof of the lengthy eigenframe/Bochner identity in Lemma 11.27.2 is claimed; in particular, Theorem 11.27.4's existence argument is only selectively checked. An optional quantitative corollary after Lemma 11.27.1 would clarify the exact pointwise RC margin. It does **not** mean “uniformly RC-positive” in the stronger, fixed-direction-for-all-fibers sense of Definition 11.26.1. Affected use: the open RC-positive locus and conformal perturbation margin in §§11.26–11.27.

## POME-HSC-RICCI-QUANT-PINCH-001

**Status:** verified conditional deduction. **Severity:** low; Lemma 11.28.2 and Proposition 11.28.3 remain correct, and their integrated arguments supply the only non-elementary inputs.

**Exact integrated source:** `docs/sections/gauduchon-metrics-and-linear-mass--holomorphic-sectional-curvature/index.html`, main blob `06c98914b1a3e3d43b546a52213b043ec03b4d24`: the curvature contractions are at physical lines **10–35**; Lemma **11.28.2**, source `non-kahler-pluripotential-theory-4B4CC53A`, permanent tag **`8D640C26806F`**, at **38–55**; Proposition **11.28.3**, source `non-kahler-pluripotential-theory-6FA99DEC`, tag **`37B317ABBC08`**, at **72–121**, and its integrated Equation **11.28.4**, tag **`7659E6D4E603`**, at **74–76**. The existing zero-lower-Ricci consequence is Corollary 11.28.5, tag `550E97762605`, **127–136**; torus rigidity Proposition 11.28.7, tag `19F2C00A6056`, **148–176**.

**Claim.** Let `X` be a compact complex manifold of complex dimension `n\ge2`, with Kähler metric `g` and smooth Hermitian tangent metric `h`. Suppose, for constants `\Lambda\ge0,\kappa\ge0`,

\[
 \operatorname{Ric}(g)\ge-\Lambda\omega_g,\qquad
 H_h(x,[v])\le-\kappa\quad\text{for all }(x,[v]).
\]

Set `u=\operatorname{tr}_g h>0`, `q=\operatorname{tr}((g^{-1}h)^2)`, and let `S` be the symmetric part of the difference between the two Chern connections as in §11.28. Then

\[
\boxed{\quad
 \int_X|S|_{g,h}^2\,dV_g+
 \frac{\kappa}{2}\int_X(u^2+q)\,dV_g
 \ \le\ \Lambda\int_Xu\,dV_g .
 \quad} \tag{A}
\]

If additionally `h\ge c g` pointwise for a constant `c>0`, then

\[
\boxed{\kappa c\le\frac{2\Lambda}{n+1}.} \tag{B}
\]

The latter is invariant under constant rescaling of `h` (which sends `c\mapsto tc` and `\kappa\mapsto\kappa/t`). For **strict equality** in (B) with `\kappa c>0`, one necessarily has

\[
 h=cg,\qquad \operatorname{Ric}(g)=-\Lambda\omega_g,\qquad
 H_g\equiv-\kappa c
\]

(the Kähler reference metric has constant negative holomorphic sectional curvature). Conversely, for any compact complex space form having constant holomorphic sectional curvature `-\kappa c`, its metrics `g`, `h=cg`, and `\Lambda=(n+1)\kappa c/2` attain equality. This is an **equality model**, not an independently established existence theorem for space-form quotients.

**Proof.** The integrated Gaussian fourth-moment argument, Lemma 11.28.2, yields `\mathcal R_g(h)\le-\frac\kappa2(u^2+q)` pointwise. Since the Ricci endomorphism of `g` is bounded below by `-\Lambda I` and `h` is positive definite, `I_g(h)=\operatorname{tr}(g^{-1}\operatorname{Ric}(g)g^{-1}h)\ge-\Lambda u`. Integrating Proposition 11.28.3 gives `0=\int(|S|^2+I_g(h)-\mathcal R_g(h))`. Combining the two pointwise lower bounds proves (A) without any approximation, integration limit or assumption about `h` being Kähler.

For (B), write `\lambda_1,\dots,\lambda_n\ge c` for the eigenvalues of `g^{-1}h`. Then

\[
  (u^2+q)-(n+1)cu
  =u(u-nc)+\sum_j\lambda_j(\lambda_j-c)\ \ge0.
\]

Thus (A) implies `\frac{\kappa}{2}(n+1)c\int u\le\Lambda\int u`; because `\int u>0`, (B) follows. When `\kappa c>0` and equality holds, all discarded nonnegative terms vanish. In particular `(u^2+q)-(n+1)cu=0` pointwise, forcing each `\lambda_j=c`, so `h=cg`. Equality in the Ricci bound gives `\operatorname{Ric}(g)=-\Lambda\omega_g`, since the positive matrix `h` has zero trace against the nonnegative endomorphism `\operatorname{Ric}(g)+\Lambda g`. Equality in Gaussian averaging gives `H_h\equiv-\kappa`: a continuous nonnegative quartic form with zero Gaussian integral vanishes in every direction. Therefore `H_g\equiv-\kappa c`. For the converse algebraic equality check, a Kähler complex space form with `H_g=-\kappa c` has `R_{i\bar j k\bar l}=-(\kappa c/2)(g_{i\bar j}g_{k\bar l}+g_{i\bar l}g_{k\bar j})`, whence `\operatorname{Ric}(g)=-(n+1)\kappa c\,g/2` and both inequalities saturate.

**Distinctness and boundary.** This is a **quantitative, scale-invariant curvature pinching and equality-rigidity** statement, not a repetition of Corollary 11.28.5 (`\Lambda=0` qualitative obstruction). It is also distinct from the previously logged flat-torus integral-curvature equality `POME-HERM-TORUS-AVG-001`: no torus, flatness or equality of integral averaged curvature is assumed. Lemma 11.28.2's Gaussian normalization and Proposition 11.28.3's global torsion/Chern identity were directly checked, but **not formally verified**; the new corollary is conditional on their correctness, and the curvature-torsion identity was not independently reconstructed from scratch. Proposed optional quantitative corollary after Corollary 11.28.5; affected dependents: curvature comparisons, rigidity, and §11.27's Ricci-flat setting.

## Outcome and audit limits

Both findings concern **correct original statements with additional deductions**, not false theorems, missing proofs or resolved upstream dependencies. Other direct checks in the sampled integrated text: §11.27's ASD projection/Hodge norm and the role of a nonzero open `det A` locus, §11.28's Gaussian fourth-moment factor `1/2`, the global Stokes cancellation in the integrated torsion identity, and the compact flat-torus integration-by-parts implication. The latter is an earlier ledger finding and is **not** newly re-counted. No original code or source/registry/permanent-tag edits, no `main` changes, no builds, tests, CI, formalization or website publishing. The 25-chapter/747-section current ToC remains an **inventory**, with two newly sampled nonexcluded sections and no whole-section certification.
