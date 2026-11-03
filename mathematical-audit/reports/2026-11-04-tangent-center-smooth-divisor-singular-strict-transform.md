# Smooth divisors can acquire an A1 singularity under a smooth-center ambient blowup

**Date:** 2026-11-04 (Asia/Shanghai). **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Finding:** \`POME-MOD-TANGENT-CENTER-STRICT-A1-001\`, **low / verified conditional deduction**. The printed propositions are correct: this is a precisely delimited **counterexample to a stronger unprinted smoothness assertion**, with an explicit local repair on a further blowup, and not a claim of certification of the entire §9.8.

## Exact integrated passages and provenance

- Main reading edition \`docs/sections/complex-spaces-and-modifications--connected-fibers-and-resolution-models/index.html\`; blob \`6ad8bec31c3089b7eab91f199f5a1eb355a12c40\`.
- Proposition **9.8.3**, source label \`foundations-of-pluripotential-theory:FCB2677B\`, permanent tag \`2312A839D109\`: **line 37** statement, **lines 43–61** proof, especially **lines 59–61** irreducible strict-transform claim.
- Definition **9.8.4**, source \`foundations-of-pluripotential-theory:E9F7D8E8\`, permanent tag \`0C92F63F8A00\`, **line 85** (divisor representatives).
- Lemma **9.8.5(2)**, source \`foundations-of-pluripotential-theory:7C25C2FE\`, permanent tag \`5488C1DAFED2\`, **lines 90–114**, especially **lines 96–100 and 114** (an extra principalization to obtain a smooth representative).
- Blowup-chart prerequisites are in \`docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html\`, blob \`f452f4b1abe5cdfe348ae11fcd934febcfdd570b\`, Proposition **9.6.3**, source \`foundations-of-pluripotential-theory:2959F02B\`, permanent tag \`865FE5EC97E6\`, and Eq. **9.6.4**, source \`foundations-of-pluripotential-theory:5649DBB5\`, permanent tag \`E62F169B3F9F\`, physical lines **49–69**. Only elementary charts are used; no regularization programme is implicated.

## Complete projective countermodel

Let \([X:Y:Z:W]\) be homogeneous coordinates on \(\mathbf P^3\), and set
\[
L=\{X=Y=0\},\qquad D=\{XW-Z^2+Y^2=0\}.
\]
The center \(L\cong\mathbf P^1\) is a smooth codimension-two submanifold. The surface \(D\) is a **smooth irreducible quadric**, since its four partial derivatives are \(W,2Y,-2Z,X\), which cannot vanish simultaneously at a projective point. The restriction of its defining polynomial to \(L\) is \(-Z^2\). Thus \(D\cap L\) consists set-theoretically of the single point \(p=[0:0:0:1]\), with scheme-theoretic intersection of length two.

Let \(\pi:\widetilde{\mathbf P^3}=\operatorname{Bl}_L\mathbf P^3\to\mathbf P^3\). The ambient blowup is smooth because the center is smooth. On \(W=1\), use \(x=X/W,y=Y/W,z=Z/W\). The equation of \(D\) is \(x-z^2+y^2=0\). In the **\(y\)-pivot blowup chart**, put \(x=yt\). The inverse image of \(D\), which is its strict transform in this chart, is
\[
F(y,z,t)=y(t+y)-z^2=0.
\]
There is **no exceptional factor** to divide out: \(D\) does not contain \(L\); indeed the equation above is irreducible and the locus \(y\ne0\) is dense in its zero set. More concretely, every point with \(y=z=0\) and finite \(t=t_0\) is a limit of solutions with \(y\ne0\), by solving \(z^2=y(t_0+y)\).

The gradient is
\[
(\partial_yF,\partial_zF,\partial_tF)=(t+2y,-2z,y).
\]
All three derivatives vanish precisely at \(q=(y,z,t)=(0,0,0)\). The analytic change of coordinate \(T=t+y\) transforms the local equation into
\[
yT-z^2=0.
\]
Its quadratic Hessian in coordinates \((y,z,T)\) is nonsingular (determinant \(2\)), so \(q\) is an **ordinary double point**, equivalently a surface \(A_1\) singularity. In the \(x\)-pivot chart \(y=xu\), the transformed equation \(x-z^2+x^2u^2=0\) has \(\partial_x=1\) over \(p\); no additional singularity arises there.

Thus **a smooth irreducible hypersurface can have a singular irreducible strict transform, even when the ambient modification is the blowup of a smooth center between smooth compact projective manifolds**. Proposition 9.8.3 makes only the correct irreducibility and generic-isomorphism claims; it does **not** assert smoothness. The example supplies a concrete reason for Lemma 9.8.5(2) to request another modification.

## Elementary one-blowup repair of this particular model

Blow up the singular point \(q\) in the ambient smooth threefold. In coordinates \((y,T,z)\) with \(yT=z^2\), the three pivot charts for the strict transform read:

- \(y\)-pivot: \(T=yT_1,\ z=yz_1\) gives \(T_1=z_1^2\);
- \(T\)-pivot: \(y=Ty_1,\ z=Tz_1\) gives \(y_1=z_1^2\);
- \(z\)-pivot: \(y=zy_1,\ T=zT_1\) gives \(y_1T_1=1\).

Each is smooth. This is an explicit **local repair** of the *model*, not a replacement proof of Hironaka principalization or of the general Lemma 9.8.5(2). On the projective ambient blowup the same one extra point blowup resolves the only singularity of this strict transform.

## Arbitrarily high tangency variant (local)

For any integer \(m\ge2\), take the smooth germ \(D_m=\{x=z^m-y^2\}\subset\mathbf C^3\) and the same smooth line \(\{x=y=0\}\). The \(y\)-pivot strict transform has equation \(y(t+y)=z^m\), hence in \(T=t+y\) coordinates \(yT=z^m\). It is a surface singularity of type \(A_{m-1}\) at the origin. Thus no uniform smoothness assertion follows from smoothness of the original divisor and of the ambient center; the contact order controls the resulting singularity type. For \(m>2\) the **single extra point blowup above is not asserted to resolve the germ**.

## Classification and dependencies

**Status:** verified conditional deduction (unprinted stronger assertion refuted; both printed statements are correct). **Severity:** low, explanatory; no mandatory source correction. **Suggested optional patch:** after Proposition 9.8.3, note that strict transforms need not be smooth and refer to Lemma 9.8.5 for a smooth representation. Retain all existing source labels, permanent tags, valid differing versions, and historical attribution.

**Affected mathematical users:** Definition 9.8.4 and Lemma 9.8.5 prime-divisor representatives; §9.6 smooth-center blowups; Chapters 20 (b-divisors and trace) and 22 (divisorial valuations), where replacing an irreducible strict transform by a smooth one requires a further justified model. This report does not assert any downstream false theorem or gap.

**Actually reviewed:** Proposition 9.8.3 **statement and strict-transform Step 3**, Lemma 9.8.5(2)'s **precise smoothness claim**, and the local blowup chart formula. The connected-fiber theorem, all proper-image/normalization prerequisites, general principalization, and full §§9.6/9.8 are **not re-certified**. Local symbolic differentiation, the Hessian determinant and three point-blowup charts were independently checked. No project tests/build/CI/formalization/site publication occurred. All owner-excluded Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**.
