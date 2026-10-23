# Mathematical audit: classical complete-intersection pole mass and sharp CLN collar loss

**Checkpoint:** 2026-10-23, Asia/Shanghai. **Verified current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Initial audit branch:** `e54b793736c6e9e926e1e2acdfc5c2580ffa5ba2`, preserved without reset. Freshly fetched main `AGENTS.md` (blob `eda69505b93b4782290d9cfac07c8651dedd17c5`), `documentation/proof-expansions.md` (`8b37e218c74d5a93637e0f092cf5f29cc338a94d`), `docs/chapters/index.html` (`c0c07abf4d8f7575b54cff2ec694fcf987f51cf8`), and review-branch `README.md` (`7967ffabeccea69fd80a5ec5d364e0a8e6bca137`) and `mathematical-audit/LATEST.md` (`cd2352c7a3226f4f8fd841a6da39efff6cd35282`), plus cumulative matrix/ledger. The current **25 chapters / 747 sections** are an inventory, NOT a count of verified sections.

## Integrated proof anchors actually checked

* **7.28:** `docs/sections/classical-products-with-controlled-unbounded-loci/index.html`, blob `21dc39a9b02a4c1820f081a0c3a82e9f8ffca727`, Theorem **7.28.1**, stable source `demailly-complex-geometry:F96C3380`, permanent tag `1BBBF8109419`, statement physical HTML lines **6–10**, integrability/construction steps **13–22**. For every nonempty subfamily \(I\) of cardinality \(m\), it assumes \(\mathcal H^{2p-2m+1}(\bigcap_{j\in I}L(u_j)\cap\operatorname{Supp}T)=0\).
* **7.30:** `docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-under-hausdorff-intersection-conditions/index.html`, blob `9cde5bfdeb2e3c0457216278945df46eb230e42b`, Proposition **7.30.3**, source `demailly-complex-geometry:A5207F44`, tag `1AC7DC75B159`, its hypothesis Eq. **7.30.4**, source `demailly-complex-geometry:3115851B`, tag `E561BB270A1B`, physical line **32**, with selected bounds/cylinder proof lines **34–89**.
* **7.32:** `docs/sections/quantitative-chern-levine-nirenberg-bounds/index.html`, blob `efb37e29f386268fefb8c17bfd31ab2ef123dc4d`, Corollary **7.32.2**, source `demailly-complex-geometry:07A49BA9`, tag `EAB247B80433`, claim physical lines **8–16**, selected proof at **21 onward**. The factor is \(C/\delta\), \(C=4\delta_0+8\|\psi\|_\infty\).

No whole-section verification is claimed. The full continuity induction of 7.28 and cutoff geometry of 7.30 were **not** independently certified.

## POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001

**Status:** `verified conditional deduction`; **severity:** low; the printed theorem is **not** false. **Sources:** 7.28.1 and 7.30.3/7.30.4 above.

**Normal crossings.** Take \(p\ge2\), \(2\le q\le p\), \(X=\Delta^p\), \(T=1\) (closed positive of bidimension \((p,p)\)), and \(u_j=\log|z_j|^2\) for \(j=1,\dots,q\). For each \(m\)-element subfamily \(I\), the common unbounded locus is a coordinate subspace of complex codimension \(m\), real dimension \(2(p-m)\). Its \(\mathcal H^{2p-2m+1}\) measure vanishes, so **all** the assumptions hold. With the current convention \(dd^c=(i/(2\pi))\partial\bar\partial\), Poincaré–Lelong and recursive coefficient integrability yield

\[
\boxed{dd^c u_1\wedge\cdots\wedge dd^c u_q=[z_1=\cdots=z_q=0].}
\tag{1}
\]

To justify the recursion rather than merely quoting it: after the first \(m\) steps the integration current is that of the smooth coordinate subspace \(z_1=\dots=z_m=0\). Restricting the next logarithm \(\log|z_{m+1}|^2\) to this subspace gives an integrable one-variable logarithm. Its distributional \(dd^c\) is its unit coordinate divisor. Induction yields (1) with coefficient one. For \(q=p\) this is \(\delta_0\).

Yet the **non-pluripolar** product is zero: on the strict truncation locus \(O_k=\bigcap_j\{u_j>-k\}\) every \(u_j\) is pluriharmonic and all their Hessians vanish. The non-pluripolar definition restricts the bounded truncation product to \(O_k\), discarding all contact-boundary mass; every restricted product and its limit vanish. The classical and non-pluripolar products have **different and correctly specified domains of definition**, not contradictory assertions.

**Repeated divisor.** Now take \(q=2\), \(u_1=u_2=\log|z_1|^2\) on the same \(\Delta^p\). Each *individual* pole divisor is \(\mathcal H^{2p-1}\)-null. Their common intersection is again the entire real-\((2p-2)\)-dimensional smooth divisor \(D=\{z_1=0\}\), whose \(\mathcal H^{2p-3}\) measure is infinite on any nonempty local patch. More fundamentally the would-be weighted coefficient \((\log|z_1|^2)[D]\) is not integrable: the logarithm is \(-\infty\) at all points of the current's support, of positive trace measure. Thus testing only singleton pole loci cannot guarantee the existence of the recursive classical product. This does **not** say the Hausdorff condition is necessary for all imaginable special inputs; it proves omitting subfamily checks is unsound.

**Proposed use:** optional paired example following Theorem 7.28.1; do not modify its statement/tags. Relevant to 7.30's geometric assumptions, weighted products in 7.29–7.31 and proper-intersection cycle formula 20.5.10 (which retains separate hypotheses). No original theorem refuted.

## POME-CLN-COLLAR-INVDELTA-OPT-001

**Status:** `verified conditional deduction`, **severity:** low; exponent-sharpness consequence of correct Corollary 7.32.2, not a claim that its numerical constant is optimal. Source/tag/anchors above.

Let \(\Omega=\Delta\subset\mathbb C\), \(\psi=|z|^2-1\), \(\omega=dd^c\psi=dA/\pi\), \(T=1\) (bidimension \((1,1)\)), and \(u=\log|z|^2\). Fix \(0<\delta_0<1\). For any \(0<\delta\le\delta_0\), the unique unbounded point \(0\) belongs to \(\Omega_\delta=\{\psi<-\delta\}\). The exact collar supremum and current masses are

\[
M_\delta=\sup_{\sqrt{1-\delta}\le|z|\le1}|u(z)|=-\log(1-\delta),\qquad
\|T\|_{\overline\Omega,\omega}=1,
\]
\[
\|uT\|_{\overline\Omega,\omega}
=\frac1\pi\int_{|z|<1}-\log|z|^2\,dA
=\int_0^1-\log t\,dt=1.
\]

Consequently the exact ratio to the **unscaled** factor in the printed estimate is

\[
\boxed{\frac{\|uT\|}{(M_\delta/\delta)\|T\|}
       =\frac{\delta}{-\log(1-\delta)}\longrightarrow1.}\tag{2}
\]

This limit follows without asymptotic machinery from
\(\delta\le-\log(1-\delta)=\int_0^\delta(1-t)^{-1}dt\le\delta/(1-\delta)\), implying \(1-\delta\le\delta/[-\log(1-\delta)]\le1\).

If the \(\delta^{-1}\) factor were replaced by \(\delta^{-\gamma}\), \(\gamma<1\), with a constant depending only on the fixed geometric data, the right side for this model would be \(O(\delta^{1-\gamma})\to0\) while the left side stays one, contradiction. Thus **the exponent 1 is optimal**, though the printed coefficient \(C=4\delta_0+8\|\psi\|_\infty\) is not claimed sharp.

**Proposed use:** optional sharpness remark at 7.32.2, preserving tags and historical attribution; constrains claims of collar-depth exponent improvement in its dependent CLN estimates.

## Verification and exclusions

A small exact rational script `checks/check_bt_subfamilies_collar.py` checks **352 finite codimension identities** and **500,500 finite rational inequalities**; the two proofs above are mathematical and do not rest on the finite tests. Only selected passages of §§7.28,7.30,7.32 were read, with §7.31 as a **dependency boundary**. No full project build/test, CI, browser, site publication, formal proof certification, main/source/registry edit, branch reset, or PR manipulation was performed.

**Strict user deferral:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion remain **`deferred-by-user`**, neither solved nor certified. The general smoothing construction in §7.31.1 was not reaudited. All previous statuses and reports are preserved.
