# Divisible-degree saturation of flat-twisted adjoint envelopes; direct complex Hessian comparison review

**Date:** 2026-11-21. **Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch before this report:** `71f2161cd4f702ae2e3e93c598425bab7dbb358d`.

**Scope:** Complete current integrated mathematical prose, statements and proof in `docs/sections/flat-twists-of-adjoint-section-envelopes/index.html`, physical lines **7–61**, main blob `f106e8f79d1a1341045f1e3c41cdeb531b5f699b`; and `docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html`, physical lines **7–365**, main blob `580d3bc2b10ebd01d880b2a31fc6930436570aac`. The latter is an entire direct section, **not** a complete proof of its previously cited §8.2/8.9/8.11/8.12 dependencies. §8.1 was selectively checked (line 7, `2<=m<n`); it is **not** counted as an entire direct review. No source/body/registry edits, CI or publication.

## New finding: POME-FLAT-TWIST-DIVISIBLE-DEGREES-ENVELOPE-001

**Severity/status:** Low / **verified conditional deduction**; no false printed theorem alleged. The relevant source statement is Theorem **19.11.1**, source `flat-twists-of-adjoint-section-envelopes:24E1B42B` (integrated source element `non-kahler-pluripotential-theory-24E1B42B` if the source namespace is inferred from the page; the permanent tag, independently verified from the reading HTML, is **`1D4EB7891AC1`**). In case source namespace differs from the inferred namespace, use the unambiguous source `data-tag=24E1B42B` and the permanent tag as authoritative. Anchors: integrated lines **9–13** (assertion), **19–42** (Nadel construction and normalization), **44–58** (divisibility, uniform norms and $L^1$ limit).

Let $Z,F,h_F,A,m_0,D$ satisfy **all** hypotheses of Theorem 19.11.1: $Z$ smooth projective, $(F,h_F)$ semipositive with trivial multiplier ideal, $K_Z+F$ pseudoeffective, $A$ ample, $m_0\ge1$, $D=K_Z+F+A/m_0$. Fix any $\rho_0\in\operatorname{Pic}^0(Z)$ and integer $r\ge1$. On a local frame of $D$, define $B_{\rho_0}^{[r]}$ by exactly the same normalized section supremum as the theorem but restrict its section degrees to positive multiples $k\in r\mathbb N$ for which the rational bundle $kD$ is integral. Then

\[
 \boxed{\left(\log B_{\rho_0}^{[r]}\right)^*
 =\left(\log B_{\rho_0}\right)^*
 =\left(\sup_{\rho\in\operatorname{Pic}^0(Z)}\log B_\rho\right)^*.}
\]

In particular **one may discard every section degree outside any fixed divisible progression**, without changing the regularized envelope. This is stronger than invariance under the flat twist for the unrestricted degree set. It neither proves pointwise equality of the unregularized suprema nor claims a uniform rate of convergence.

### Justification

Let $s\ne0$ be any normalized seed in $H^0(Z,k_0D+\rho)$, of any admissible degree $k_0$. Choose a sequence of integers $\ell_j\to\infty$ each divisible by $r$, so $k_j=\ell_jk_0$ is divisible by $r$ and is a permitted target degree. The construction in lines 23–42, using the positive metric on $B_{k_j}=(k_j-1)D+F+A/m_0+\rho_0$, Nadel vanishing and flat-twist invariance of the Euler characteristic, produces $u_{k_j}\in H^0(Z,k_jD+\rho_0)$ with a normalized root integral at most $1$ after multiplying by one **fixed** scalar. The divisibility calculation at lines 44–50 gives

\[
u_{k_j}=s^{\ell_j-1}v_{k_j},\qquad
v_{k_j}\in H^0\bigl(Z,k_0D+\rho_0-(\ell_j-1)\rho\bigr).
\]

All the $v_{k_j}$ have weighted $L^2$ norm one against the single fixed multiplier-ideal weight
$|s|^{-2(k_0-1)/k_0}h_F(h_A')^{1/m_0}$. The buffered-chart submean and closed-graph estimates in line 50 bound their smooth suprema from both sides independently of $j$; their varying flat factors have unitary transition maps. The quasi-psh compactness argument in lines 52–55 therefore yields

\[
\frac{1}{k_j}\log|u_{k_j}|^2
=\frac{\ell_j-1}{k_j}\log|s|^2
 +\frac{1}{k_j}\log|v_{k_j}|^2+O(k_j^{-1})
\longrightarrow\frac1{k_0}\log|s|^2
\quad\text{in }L^1_{\mathrm{loc}}.
\]

The $O(k_j^{-1})$ is the harmless fixed normalization factor. For every $j$, the left side lies below the upper-semicontinuously regularized **restricted-degree** target envelope. The $L^1$ limit and equality of canonical psh representatives almost everywhere imply that this envelope dominates $(1/k_0)\log|s|^2$ everywhere. Taking the supremum over all starting degrees $k_0$, sections and flat twists gives $\left(\log B_{\rho_0}^{[r]}\right)^*\ge(\sup_\rho\log B_\rho)^*$. The reverse inequality is immediate by inclusion of eligible sections. This proves the displayed equality. No commutation of two unspecified limits is used: first fix the seed, then let $\ell_j\to\infty$ along the selected progression, and only afterward take the supremum of seeds.

**Correction proposed:** Optional corollary following Theorem 19.11.1, with explicit insistence on **USC regularization**, and with admissible divisibility of $kD$ retained. No statement/proof correction is necessary. **Dependents:** constructions of the extremal adjoint singular metric from sparse graded series or fixed flat twists. **Remaining input:** Nadel vanishing in **10.102.1**, flat-twist Euler-characteristic invariance in **10.103.1**, and normality/closed-graph/quasi-psh compactness used at lines 44–55 were *not* independently proven in this run. In particular, no excluded regularization/Bergman/L²/Ohsawa–Takegoshi completion programme was reopened.

**Prior results kept separate:** The 2026-11-10 `POME-ADJOINT-FLAT-DIVISIBILITY-SCOPE-001` computes a local divisor/multiplier-ideal threshold and nonnormality limitation. It is **not** re-counted here. The present finding is about global arithmetic thinning of permitted section degrees.

## Entire §8.13 direct check (no newly confirmed printed error)

Scope and anchors: Lemma 8.13.1 `69692CE9985B` lines **10–38**, Proposition 8.13.3 `CCDE5B297235` lines **42–62**, Theorem 8.13.4 `53F870DE5980` lines **65–121**, Example 8.13.5 `0DB9D80DE230` lines **125–150**, Lemma 8.13.7 `0F8C3F6B0122` lines **153–221**, Theorem 8.13.8 `B83D4B8CE619` lines **225–274**, Theorem 8.13.10 `A532C77D7D0C` lines **281–302**, Corollary 8.13.11 `6BFB2EB67A74` lines **305–323**, Proposition 8.13.12 `FBE7E9A6BE5E` lines **330–352**, Corollary 8.13.13 `5460C4009B01` lines **355–363**.

* **Mass identity:** The subset expansion in 8.13.1 has $\binom mq$ contributions when all slots coincide; the empty subset is exactly $\int\omega^n$. Each nonempty term is paired with $dd^c\omega^{n-|I|}$, with canonical bounded multiplication asserted by the earlier recursion. No missing top-degree normalization was found in this direct reading.
* **Characterization of constant Hessian mass:** In 8.13.4, polynomial expansion for $tf$ and polarization determine all $dd^c\omega^{n-q}$, $1\le q\le m$. The converse global comparison is indeed the maximum inequality plus constant total masses; taking a large constant shift of one potential recovers constancy of mass from comparison. This is a valid conditional deduction from its cited product calculus.
* **Explicit sign check in 8.13.5:** For the torus with $b=2+\cos(2\pi x_1)$, $dd^c(t\cos(2\pi x_1))=-\pi^2t\cos(2\pi x_1)\beta_1$, and since $(dd^cu_t)^2=0$, the mass is $n!B_n(2-m\pi^2t/(2n))$. For $t<0$ it exceeds the mass at $t=0$, so a sufficiently large constant shift yields the advertised failure of unmodified comparison.
* **Torsion and weighted convergence:** Lemma 8.13.7 explicitly keeps the top-degree metric-derivative contributions. Its step from smooth to bounded potentials uses joint decreasing convergence for the *unrestricted* positive mixed measures, and a continuous weight for the signed torsion term before restricting to the Borel set $E$; there is no claimed weak convergence after multiplying by $1_E$. This reduces the delicate step to 8.11.12 and 8.12.4, which remain **uncertified inputs**. The rescaled recurrence in 8.13.8 uses $B_k=\eta^{m-k}a_k$ and $\delta=C_3s\eta^{-3}$, so the published smallness condition makes the sum of lower-degree masses bounded by $2m\eta^{-m}a_m$ without dividing by $a_m$.
* **Domination and stability:** Theorem 8.13.10 correctly requires $E_s$ to have *positive volume*, not necessarily interior, and cites the canonical a.e.-order property 8.2.10; Proposition 8.13.12 applies domination to $(v+s,u)$ with $c=e^{K-\kappa s}<1$ in the right order. The endpoint uniqueness statements then follow conditionally.

**Unresolved verification boundaries (not new findings):** the complete canonical product/weighted convergence proof chain in §§8.9–8.12, positive-volume/canonical-order input 8.2.10, and smooth solvability 8.6.1/8.8.3. Checking the *use* of these results does not certify them. No theorem from §8.13 was shown false in this run; no old finding is repeated as new.

**Coverage delta:** +2 current direct whole sections (**19.11** and **8.13**); +1 selected scope/convention section (**8.1**, line 7); +0 complete upstream proof-chain certifications; no historical first-visit claim. The user's excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**. No software tests, build, CI, or publication were run.
