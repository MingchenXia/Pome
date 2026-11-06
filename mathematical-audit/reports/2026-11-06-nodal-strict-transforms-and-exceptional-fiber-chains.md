# 2026-11-06 — nodal strict transforms and reducible connected exceptional fibers

## Provenance and review boundary

- Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (verified from live `main`).
- Main reading file: `docs/sections/complex-spaces-and-modifications--connected-fibers-and-resolution-models/index.html`; Git blob `6ad8bec31c3089b7eab91f199f5a1eb355a12c40`; physical lines **10–18** (Theorem 9.8.1), **22–32** (Corollary 9.8.2), **36–62** (Proposition 9.8.3), **84–85** (Definition 9.8.4), **105–115** (strict-transform composition), and **120–171** (Theorem 9.8.6, contextual only).
- Principal labels: Theorem 9.8.1 `foundations-of-pluripotential-theory:11F7A347` / permanent `176C7A4C3D95`; Corollary 9.8.2 `foundations-of-pluripotential-theory:9CE118B1` / `6EB72DC4EC68`; Proposition 9.8.3 `foundations-of-pluripotential-theory:FCB2677B` / `2312A839D109`; Definition 9.8.4 `foundations-of-pluripotential-theory:E9F7D8E8` / `0C92F63F8A00`.
- Cross-check: `docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html`, blob `06439f43d1ce8e83d2529682c9a630bffa3d9c22`, physical lines **141–157**, Theorem 9.4.6 `foundations-of-pluripotential-theory:7042BB57` / permanent `12A47DB401E2`.
- This is **new explicit local blowup and fiber geometry** within previously sampled §9.8, particularly its previously unexamined strict-transform Proposition 9.8.3 and Definition 9.8.4. It does **not** recertify §9.8.1, §9.8.2, §9.4.6 or all of §9.8, and does not revisit any owner-deferred regularization program.

## POME-AN-NODAL-BLOWUP-STRICT-TRANSFORM-001

**Severity:** low. **Status:** verified conditional deduction; the original statements remain correct.

**Precisely tested claims.** Theorem 9.8.1 assumes an *irreducible local germ* at the target point, not merely a globally irreducible target. Proposition 9.8.3 asserts that the strict transform of a globally irreducible hypersurface remains irreducible, not that its intersection with the exceptional set is irreducible or connected.

Consider the reduced affine curve
\[
 C=\{(x,y)\in\mathbb C^2:y^2=x^2(1+x)\},\quad o=(0,0).
\]
It is algebraically irreducible: a factorization of the monic quadratic in \(y\) over \(\mathbb C[x]\) would require \(x^2(1+x)\) to be a polynomial square, which it is not. Yet near \(o\), with the holomorphic square root \(h(x)=\sqrt{1+x}\),
\[
 y^2-x^2(1+x)=(y-xh(x))(y+xh(x)),
\]
so the germ \((C,o)\) consists of two distinct smooth branches with tangent directions \(y=\pm x\).

Let \(\pi:\mathrm{Bl}_o\mathbb C^2\to\mathbb C^2\). In the blowup chart \(y=xt\), the total transform has equation
\[
 x^2(t^2-1-x)=0,
\]
and the **strict** transform is
\[
 C'=\{x=t^2-1,\ y=t(t^2-1)\}\simeq\mathbb C_t.
\]
Both tangent directions lie in this chart; no further points of \(C'\) lie above \(o\) in the other chart. The exceptional divisor is \(x=0\), and
\[
 C'\cap\pi^{-1}(o)=\{(x,t)=(0,1),(0,-1)\}.
\]
Thus \(C'\) is *smooth and irreducible*, while the fiber of the induced proper bimeromorphic map \(\pi|_{C'}:C'\to C\) has **two disconnected points**. This does **not** contradict Theorem 9.8.1: the target germ at \(o\) is reducible. Indeed \(\pi|_{C'}\) is finite and is exactly the normalization: \(t\) satisfies the monic equation \(t^2=1+x\); off \(o\), \(t=y/x\), and \(\mathbb C[t]\) is finite over \(\mathbb C[x,y]/(y^2-x^2(1+x))\).

The same example checks two further logical guards: (i) dropping **normality of the target** from the finite-bimeromorphic-isomorphism clause of Corollary 9.8.2 would be false; and (ii) dropping the condition that \(\phi^{-1}(X_{\rm sing})\) is nowhere dense from its *unique* normalization-lift clause would be false: for the normal one-point space \(S=\{*\}\) mapping constantly to \(o\), there are two different lifts, selecting \(t=1\) and \(t=-1\). All *printed* qualifications are satisfied in their original scope.

**Proposed correction:** None to theorems. Optional explanatory sentence after Theorem 9.8.1: global irreducibility alone does not imply connected fibers; the strict transform of a nodal curve under the blowup of its node is irreducible but meets the exceptional divisor in two points.

**Dependents checked, not recertified:** §9.4.6 normalization fiber/branch correspondence, §9.8.3 strict-transform irreducibility, §9.8.2 finite normal-target isomorphism and lifting uniqueness. No circular inference was used to establish the explicit chart calculation.

## POME-AN-ITERATED-EXCEPTIONAL-FIBER-CHAIN-001

**Severity:** low. **Status:** verified conditional deduction; no false theorem.

**Precisely tested claim.** The connected-fiber assertion of Theorem 9.8.1 does not imply irreducibility, even when *both source and target are smooth*; Definition 9.8.4 also permits multiple distinct exceptional prime divisors over one smooth target point.

On \(X=\mathbb C^2\), successively blow up the origin and then, at each further stage, a **smooth point on the newest exceptional curve away from intersections with earlier components**. Write
\[
 f_r:X_r\longrightarrow X,\qquad E_1,\ldots,E_r\subset X_r
\]
for the final strict transforms of the exceptional curves (\(r\ge1\)). Each \(X_r\) is smooth and \(f_r\) is proper bimeromorphic. The reduced fiber is exactly the chain \(E_1\cup\cdots\cup E_r\) of \(r\) copies of \(\mathbb P^1\), each adjacent pair meeting transversely at exactly one point; nonadjacent pairs do not meet.

For \(r=2\), take the first blowup chart \(y=xt\) and blow up \(x=t=0\). In a chart of the second blowup \(x=uv,t=v\), the map is
\[
 (x,y)=(uv,uv^2),\qquad
 f_2^{-1}(o)_{\rm red}=\{u v=0\};
\]
here \(E_1=\{u=0\}\) and \(E_2=\{v=0\}\) meet transversely. These are different **exceptional prime divisors** on the same model, both lying over the origin, and remain distinct under the equivalence of Definition 9.8.4.

The exceptional curve of a point blowup has normal bundle \(\mathcal O_{\mathbb P^1}(-1)\): in the incidence description of the blowup the normal direction is the tautological line in \(\mathbb C^2\) over the direction \([x:y]\). Thus its self-intersection is \(-1\). Blowing up a smooth point on a compact curve reduces the normal bundle degree by one; this follows directly by comparing the local defining coordinate with its factor by the exceptional parameter in a blowup chart. Consequently the final intersection matrix \(Q_r=(E_i\cdot E_j)\) has diagonal
\[
 (-2,-2,\ldots,-2,-1)
\]
and off-diagonal entries \(1\) exactly for \(|i-j|=1\). For every real vector \(a=(a_1,\ldots,a_r)\),
\[
 -a^\mathsf T Q_r a=a_1^2+\sum_{i=1}^{r-1}(a_i-a_{i+1})^2>0
 \quad\text{if }a\ne0.
\]
In particular \(Q_r\) is negative definite and \(\det Q_r=(-1)^r\), since the displayed quadratic form is the square of a triangular integer matrix of determinant \(\pm1\). The fiber has arbitrarily many components while remaining connected. This is consistent with Theorem 9.8.1 and does **not** make the finite-map isomorphism clause of Corollary 9.8.2 applicable, since the blowup map is not finite at the origin.

**Proposed correction:** None. Optional cross-reference from Theorem 9.8.1/Definition 9.8.4 to the two-blowup chart as a concrete illustration distinguishing connected fibers, irreducible strict transforms and individual exceptional prime divisors.

**Dependents and limits:** Compatible with Proposition 9.8.3 (codimension-two exceptional image), Definition 9.8.4, and the divisorial model discussion in §§20.1–20.3. This elementary smooth surface chain does not prove the arbitrary compact-complex-space extraction theorem 9.8.6, whose general smooth-center principalization depends on the permitted Hironaka input.

## Classification and actual coverage

The two IDs are **new, source-pinned conditional deductions**, not confirmed errors, missing-proof repairs, global statements about every modification, or full mathematical certifications. Only elementary explicit blowup charts, local analytic branch factorization, a monic integral equation and normal-line transition were proved here. There is no claim that all relevant reference chains, Hironaka, or the full 747-section collection were verified.

Owner-deferred Demailly approximation/regularization and dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programs remain **deferred-by-user**, not certified or reopened. No source/body/permanent-tag changes, tests, builds, CI or website publication were performed.
