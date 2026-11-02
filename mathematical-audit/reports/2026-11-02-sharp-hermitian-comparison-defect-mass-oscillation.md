# Exact additive Hermitian Monge–Ampère comparison defect

**Finding ID:** POME-HERM-COMPDEF-MASS-OSC-001  
**Date:** 2026-11-02  
**Severity / classification:** low / **verified conditional deduction** (a sharp new consequence of the printed locality/contact steps; **not a false printed theorem, not a completed repair**).  
**Production `main` reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Scope:** nonexcluded Bedford–Taylor products and Hermitian comparison; no regularization, Bergman, weighted L², Ohsawa–Takegoshi, or positivity-loss proof checked.

## Exact source anchors

- `docs/sections/uniqueness-for-degenerate-equations--comparison-and-invariant-mass/index.html`, main blob `7683a63656f9b4311a77d1db8e260a1bdc65f0b0`, **physical lines 33–64**: Theorem **14.25.3**, source label `non-kahler-pluripotential-theory:27525A10`, permanent tag `FE27B72E2DB5`; Equation **14.25.4**, source `non-kahler-pluripotential-theory:F7BB1056`, permanent tag `A25B3D75AF64`. The original proof uses ordered contact and plurifine locality before invoking invariant total mass.
- `docs/sections/plurisubharmonic-functions-and-singularities--products-with-smooth-backgrounds/index.html`, main blob `e2ba89b51376ba0296846221109c664a0c29b2c3`, **physical lines 48–68**: Lemma **5.28.3**, source `non-kahler-pluripotential-theory:A262AD55`, permanent tag `5087175B2C39` (ordered contact).
- `docs/sections/torsion-and-the-variation-of-mass/index.html`, main blob `9abec9685e33a1b40f9c0765381408eb52b325d3`, **physical lines 69–89, 185–195, 208–240**: Theorem **11.1.5**, source `non-kahler-pluripotential-theory:D4902E5B`, permanent tag `2B3316345A4A`; Corollary **11.1.10** permanent tag `2C05FFD39C6D`; Example **11.1.12**, source `non-kahler-pluripotential-theory:028A9E19`, permanent tag `F336FEED9D87`. The example is already printed: it is **not** presented here as a newly discovered counterexample.

## Statement (optimal additive defect)

Let \(X\) be a compact complex \(n\)-fold and \(\omega>0\) a smooth Hermitian form. Put
\[
\mathcal P_\omega=\operatorname{PSH}(X,\omega)\cap L^\infty(X),
\qquad \mu_u=(\omega+dd^c u)^n,\qquad M(u)=\mu_u(X).
\]
Products are the bounded Bedford–Taylor products used in the integrated text. There is **no** Guan–Li or mass-invariance assumption. For \(a,b\in\mathcal P_\omega\), let \(q=\max(a,b)\) and set
\[
d(a,b)=\mu_b(\{a<b\})-\mu_a(\{a<b\}).
\]
Then
\[
\boxed{d(a,b)\le M(q)-M(a).}\tag{A}
\]
The **exact optimal uniform additive comparison constant**, possibly \(+\infty\), is
\[
\boxed{\sup_{a,b\in\mathcal P_\omega}d(a,b)
=\sup_{u,v\in\mathcal P_\omega}\bigl(M(v)-M(u)\bigr)
=\sup_{\mathcal P_\omega}M-\inf_{\mathcal P_\omega}M.}\tag{B}
\]
The last expression is understood as an extended nonnegative value; the difference is unambiguous because \(0\le\inf M\le M(0)<\infty\). In particular, finite optimal additive comparison defect is equivalent to a uniform upper bound on the total masses \(M(u)\) of **all** bounded \(\omega\)-psh potentials. Zero defect is equivalent to mass invariance and ordinary comparison. There is no claim that a finite nonzero defect yields uniqueness of the degenerate equation.

### Proof of (A)

By plurifine locality for bounded products, \(\mathbf1_{\{a<b\}}\mu_q=\mathbf1_{\{a<b\}}\mu_b\). The ordered contact lemma applies to \(a\le q\) and gives
\(\mathbf1_{\{a=q\}}\mu_a\le\mathbf1_{\{a=q\}}\mu_q\).
The Borel set \(\{a\ge b\}\) equals \(\{a=q\}\). Hence
\[
\begin{aligned}
\mu_b(\{a<b\})
&=M(q)-\mu_q(\{a\ge b\})\\
&\le M(q)-\mu_a(\{a\ge b\})\\
&=\mu_a(\{a<b\})+M(q)-M(a).
\end{aligned}
\]
The total masses in this argument are finite, and no limit interchange, net compactness, external regularization theorem, or background \(dd^c\)-closedness is used. This is exactly the portion of the printed proof of Theorem 14.25.3 that precedes its substitution of a common mass \(V\).

### Proof of sharpness and of (B)

From (A), \(d(a,b)\le M(q)-M(a)\le\sup_{u,v}(M(v)-M(u))\).

Conversely fix arbitrary \(u,v\in\mathcal P_\omega\). Choose a constant \(C>\sup_X(u-v)\), possible because both potentials are bounded. Then \(u<v+C\) everywhere and \(dd^c(v+C)=dd^c v\), so
\[
d(u,v+C)=M(v+C)-M(u)=M(v)-M(u).
\]
Taking the supremum proves (B), including the case where it is infinite. This argument also proves **optimality**: a smaller additive constant fails for a pair shifted to have the strict comparison set equal to all of \(X\). The equality with the oscillation of \(M\) is elementary; the infimum is finite because \(M(u)\ge0\) and the zero potential is admissible.

## Explicit noninvariant metric and positive defect (crosscheck, not new example)

Use the **existing** Example 11.1.12 on the complex two-torus, with
\(\omega=\beta_1+(2+\cos 2\pi x_1)\beta_2\),
\(u_t=t\cos(2\pi x_1)\), \(B=\int_X\beta_1\wedge\beta_2>0\).
For \(0<t<\pi^{-2}\), the printed exact mass computation is
\[
M(u_t)=(4-\pi^2t)B,\qquad M(0)=4B.
\]
Choose \(a=u_t\), \(b=C\) constant with \(C>t\). Both are smooth strictly \(\omega\)-psh; \(\{a<b\}=X\), and
\[
d(a,b)=M(0)-M(u_t)=\pi^2tB>0.
\]
Thus (A) can attain equality and ordinary comparison can fail without Guan–Li. The novelty of this report is **the global optimal-defect identity (B)**, not the already integrated torus mass example or the already proved qualitative equivalence in Theorem 14.25.3.

## Dependency and status boundaries

- **Verified conditional deduction:** equations (A)–(B) follow from the printed bounded-product plurifine locality and ordered contact inequality (§5.28.3); these dependencies were read in the actual integrated edition but their complete analytic construction was **not** independently re-certified.
- **Printed results are not contradicted:** Theorem 14.25.3 explicitly assumes Guan–Li for zero-defect comparison and already proves the qualitative equivalence. Its proof remains correct in the checked passages. Theorem 14.25.2's auxiliary density, existence, mixed inequality and domination steps were inspected for hypothesis alignment only, **not** certified.
- **External / excluded:** Theorem 11.1.7's bounded-potential approximation route invokes regularization (§5.32.1); it is **deferred-by-user**, not used or audited here. Historical Chiose attribution in Theorem 11.1.7 is retained. No new non-Hironaka external mathematical input is introduced by (A)–(B).
- **Proposed nonproduction addition:** A short corollary after (14.25.4), explicitly scoped to *unrestricted bounded potentials* (no normalization \(\sup u=0\)), recording the sharp constant (B). A body change is not made in this audit branch. Dependent discussions of Hermitian comparison (14.25.2–3) and mass variation (11.1.5, 11.1.10) may cite it; it does not repair or establish their unverified upstream PDE steps.

## Coverage and reproducibility

Actual new work: direct proof-level audit of the **pre-invariance** locality/contact part of Theorem 14.25.3 and extraction of a sharp all-pairs quantitative statement; selected independent crosscheck of Lemma 5.28.3 and the already published torus mass computation 11.1.12. No other §14.25 or §11.1 claims are promoted to complete theorem-chain status. Current ToC remains **25 chapters / 747 numbered sections / zero entire sections mathematically certified**. No project build, tests, CI, formalization, publication, source edits, registry edits, or change to permanent tags.

Manual check of the displayed torus calculation: for \(0<t<\pi^{-2}\), \(\pi^2tB>0\), \(\mu_{u_t}\ge0\), and choosing \(C>t=\sup u_t\) makes the strict sublevel set exactly \(X\). This is a symbolic calculation, **not** a software test.
