# An irrational holomorphic curve has a full-dimensional closure but a two-dimensional image

**Finding:** `POME-CSPACE-DENSE-IMAGE-CLOSURE-RANK-001`  
**Date:** 2026-11-08  
**Severity / status:** low / **verified conditional deduction (sharpness countermodel)**. The printed Lemmas 9.3.14–15 and Theorem 9.7.2 are **not refuted**. This is an independent, completely specified model showing why the analyticity-of-image qualification in 9.3.15(3), and the properness qualification in 9.7.2, may not be silently removed.

## Direct integrated reading and stable provenance

- Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Actual reading-edition file: `docs/sections/complex-spaces-and-modifications--analytic-sets-and-their-local-branches/index.html`, blob `85516d6b7ac0226ea121a16ee98d673e2cbb43d5`.
- Lemma **9.3.14** (holomorphic constant-rank normal form): source `foundations-of-pluripotential-theory:C501FEA1`, permanent tag `F802E1301C0F`; physical statement lines **361–366**, proof lines **369–373**.
- Lemma **9.3.15** (Hausdorff-measure bounds for holomorphic images and dimension of *analytic* images): source `foundations-of-pluripotential-theory:A2E7BB66`, permanent tag `A814C831E915`; statement lines **377–387**, proof lines **393–405**. In particular, part (3) **assumes** that `F(A)` is analytic; its conclusion is only an upper bound on that analytic image's complex dimension.
- Supporting rank-stratum and compact-cube facts in Corollary **9.3.13** (physical lines **322–353**) were checked for the dimension convention, and the proof's reliance on countable coverings (9.3.15(1), lines 395–400) was distinguished from unjustified sequential compactness.
- Adjacent contextual statement: `docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html`, blob `b44fe157b8c01363da7799990b8ef6ed82525553`, Theorem **9.7.2** (Remmert): source `foundations-of-pluripotential-theory:7AC95C77`, permanent `0FC675348681`, physical lines **15–22**. Only its *properness hypothesis and conclusion* are used for comparison; its lengthy inductive proof was **not certified**.

## Precisely delimited new model

Let
\[
\Lambda=\mathbb Z+i\mathbb Z,\qquad
E=\mathbb C/\Lambda,\qquad
X=E\times E,
\]
and fix a real irrational number \(\alpha\). Define the holomorphic map
\[
F:\mathbb C\longrightarrow X,\qquad
F(z)=([z],[\alpha z]).
\tag{1}
\]
The domain \(N=\mathbb C\) is a connected, second-countable complex manifold and an analytic subset of itself, of complex dimension one.

**Claims.** The differential of \(F\) has constant complex rank one; the image \(F(\mathbb C)\) has Hausdorff dimension **exactly two** in the flat product metric, yet
\[
\boxed{\ \overline{F(\mathbb C)}=E\times E,\qquad
\dim_{\mathbb C}\overline{F(\mathbb C)}=2>1.\ }
\tag{2}
\]
In particular \(F(\mathbb C)\) is not analytic in \(X\), and \(F\) is not proper. An attempt to replace an analytic image in 9.3.15(3) by the **closure of an arbitrary holomorphic image** is false even for an immersion into a compact smooth Kähler surface.

## Full independent proof

**1. Holomorphic immersion.** The covering quotient \(\mathbb C^2\to X\) is a local biholomorphism, and the lift of \(F\) is \(z\mapsto (z,\alpha z)\), whose derivative is the nonzero complex vector \((1,\alpha)\) everywhere. Thus \(\operatorname{rank}_{\mathbb C}\mathrm dF=1\). On a sufficiently small disk, the first coordinate \([z]\) is injective, so \(F\) restricts to an embedded holomorphic disk. This disk has positive two-dimensional Hausdorff measure in the flat metric: the projection to the first elliptic factor is 1-Lipschitz and its image contains an open disk; consequently \(\dim_H F(\mathbb C)\ge2\).

**2. Exact image dimension.** In the standard flat quotient metric on \(X\), the quotient map \(\mathbb C^2\to X\) is 1-Lipschitz. On \(\mathbb C\) the lift \(z\mapsto(z,\alpha z)\) is globally \(\sqrt{1+\alpha^2}\)-Lipschitz. Cover \(\mathbb C\) by the integer squares \(Q_R=[-R,R]+i[-R,R]\), \(R=1,2,\ldots\). Each square has \(\mathcal H^s(Q_R)=0\) for all \(s>2\): partitioning it into \(O(\varepsilon^{-2})\) squares of diameter \(O(\varepsilon)\) gives a total \(s\)-content \(O(\varepsilon^{s-2})\). Lipschitz images preserve \(\mathcal H^s\)-nullity, and countable unions preserve nullity. Therefore \(\mathcal H^s(F(\mathbb C))=0\) for every \(s>2\). Together with Step 1,
\[
\boxed{\dim_H F(\mathbb C)=2.}
\tag{3}
\]
This independently checks the **sharpness of the exponent** \(2k\) in the printed 9.3.15(1) for \(k=1\) (after using target coordinate charts); it does **not** independently reprove that lemma for arbitrary maps.

**3. Density.** Fix arbitrary \(([u],[v])\in E^2\), choosing complex representatives \(u,v\). For any integers \(m,n\), take \(z_{m,n}=u+m+in\). Then
\[
F(z_{m,n})=([u],[\alpha u+\alpha m+i\alpha n]).
\tag{4}
\]
For irrational real \(\alpha\), the fractional parts of \(\alpha\mathbb Z\) are dense in \(\mathbb R/\mathbb Z\). Here is an elementary justification: by pigeonholing \(N+1\) fractional parts \(\{0\},\{\alpha\},\ldots,\{N\alpha\}\) into \(N\) equal intervals, for arbitrarily large \(N\) one obtains a nonzero integer \(q\) with the fractional part of \(q\alpha\), up to sign, in \((0,1/N)\). Integer multiples of this small irrational rotation give a \(1/N\)-net on the circle. The same argument applies independently to \(m\) and \(n\). Consequently, the second coordinates in (4) are dense in \(E\), while their first coordinate is exactly \([u]\). Since \([u]\) was arbitrary, \(F(\mathbb C)\) is dense in all of \(E^2\), proving (2).

**4. Image is neither analytic nor proper.** A complex analytic subset is closed by definition. If \(F(\mathbb C)\) were analytic in \(E^2\), its density would imply equality with \(E^2\). But (3) gives \(\mathcal H^4(F(\mathbb C))=0\), whereas a nonempty open piece of \(E^2\) has positive \(\mathcal H^4\). Therefore the image is proper dense and nonanalytic. Also \(F^{-1}(X)=\mathbb C\) is not compact, although \(X=E^2\) is compact; thus \(F\) is nonproper.

## Correct interpretation and downstream boundary

1. The printed 9.3.15(1) remains correct: its \(\mathcal H^s\)-nullity assertion concerns the **image**, not its closure, and in the model the bound is sharp. Applying the same statement in target charts (or the direct Lipschitz proof) does **not** imply an estimate on the closure.
2. The printed 9.3.15(3) remains correct: it *explicitly assumes* \(F(A)\) is an analytic subset and concludes \(\dim F(A)\le\dim A\). The example fails that assumption. The statement with \(\overline{F(A)}\) substituted for \(F(A)\) is **false** without another restriction, e.g. properness.
3. The printed Remmert Theorem 9.7.2 requires properness. This map lacks it and so is no counterexample; the example does show why it is unsafe to extrapolate analytic-image conclusions to all holomorphic maps from noncompact sources. The proper-image proof and all global complex-space dependencies stay **uncertified**.
4. **Proposed optional editorial addition:** place a short model remark after Lemma 9.3.15 or in the comparison with 9.7.2, keeping original statements, attribution, source/permanent tags and both valid versions unchanged. No main/source edit was made.
5. **Actual coverage:** first recorded selected mathematical proof-level reading of §9.3.14–15 and Corollary 9.3.13(2)–(3), with §9.7.2 a hypothesis-only crosscheck; **not** an entire §9.3 or §9.7 audit. ToC remains **25 chapters / 747 numbered sections**, **zero completely certified mathematical sections**.
6. **Exclusions:** Demailly approximation/regularization and the dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, not resolved or reopened. No private material, paid service, tests, build, Actions CI, formal verification or website publication is involved.
