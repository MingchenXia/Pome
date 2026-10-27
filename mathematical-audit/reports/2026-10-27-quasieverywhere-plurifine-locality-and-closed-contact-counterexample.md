# Quasi-everywhere equality, plurifine locality, and a closed-contact counterexample

**Date:** 2026-10-27. **Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Branch:** review/mathematical-audit (audit records only). **Scope:** first selected proof-level review of §§5.9 and 5.47; fresh cross-check of already-reviewed §13.2. Demailly approximation/regularization, its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme, and their prerequisites are expressly excluded by the user. Previously recorded items in that programme remain deferred-by-user, not resolved.

## Finding POME-PLURIFINE-QE-EQUALITY-LOCALITY-001

**Status:** verified conditional deduction (proposed strengthening of correct printed locality results; no false theorem found). **Severity:** low.

### Exact sources and dependent propositions

1. Main docs/sections/pluripolar-sets-and-the-plurifine-topology/index.html, blob **1bfa1fc213c9d9cf3db6ec015a10aeb21617aa2c**:
   - Definition 5.47.14 (permanent tag **09A00D4B8096**, lines 275–279): the plurifine topology makes plurisubharmonic functions continuous with extended-real values.
   - Proposition 5.47.16 (tag **DD1F66C6842A**, lines 337–346): the complement of each pluripolar subset is plurifinely dense.
   - Theorem 5.47.20 (tag **17D9EEFA42DF**, lines 382–419): quasi-Lindelöf Borel representatives of plurifine-open sets up to pluripolar sets.
   - Theorem 5.47.22 (tag **C1A6B45ED829**, lines 450–480): plurifine locality of Bedford–Taylor products of locally bounded psh potentials; the proof uses polarization and a countable basic-set selection, not a presumption that plurifine opens are Borel.
   - Proposition 5.47.23 (tag **983478512954**, lines 487–510): compatibility of truncations on joint superlevel sets and monotone positive trace measures.
2. Main docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob **81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c**:
   - Lemma 13.2.2 (tag **D59675D9F6D8**, lines 35–58): the locally finite non-pluripolar current and completion-measurable plurifine restrictions.
   - Proposition 13.2.6 (tag **7F7123F92478**, lines 80–111, especially lines 90–94): plurifine locality of locally finite non-pluripolar products for *pointwise* equality on a plurifine-open set.
3. Main docs/sections/plurisubharmonic-functions--positive-hessians-and-holomorphic-maps/index.html, blob **6f73e47e8a1f91a54fc37761c07627b4724306ce**, Theorem 5.9.1 (tag **2A4F77263F48**, lines 11–35): uniqueness of the canonical psh representative of a distribution; checked for consistency, not needed as an extra input in the proof below.

### Strengthened statement

Let $U\subset\mathbb C^n$ be open, $W\subset U$ be **plurifine open**, and $u_1,\ldots,u_p,v_1,\ldots,v_p\in\mathrm{PSH}(U)$, $1\le p\le n$. Suppose that there is a (possibly non-Borel) pluripolar set $E\subset U$ such that
\[
  u_j(z)=v_j(z)\qquad(z\in W\setminus E,\ j=1,\ldots,p).
\]
Then **$u_j=v_j$ everywhere on $W$**, even at points where both sides equal $-\infty$.

Consequently:

(a) If all these psh functions are locally bounded, their Bedford–Taylor mixed products have identical restrictions to $W$.

(b) If the two mixed non-pluripolar products exist as **locally finite currents** in the sense of Definition 13.2.4, their restrictions to $W$ coincide as completed coefficient measures. Local finiteness of both products is an explicit premise; it is *not* inferred from equality restricted to $W$.

The claim applies to non-Borel $W$ and $E$. With different exceptional sets $E_j$ for the factors, one may replace them by their finite union.

### Complete argument

For every psh function $u$ on $U$, Definition 5.47.14 makes $u:U\to[-\infty,\infty)$ continuous for the plurifine topology, with the ordinary extended-real order topology on the target. That target is Hausdorff. Therefore, for any two psh functions $u,v$, the equalizer
\[
  Z(u,v)=\{z\in W:u(z)=v(z)\}
\]
is **closed in the relative plurifine topology on $W$**: it is the inverse image of the closed diagonal of $[-\infty,\infty)^2$ under the continuous map $(u,v)|_W$. This argument includes common poles, and never forms the undefined difference $-\infty-(-\infty)$.

By Proposition 5.47.16, $U\setminus E$ is plurifinely dense in $U$. Since $W$ is plurifine open, $W\setminus E$ is plurifinely dense **in $W$**: any nonempty relatively plurifine-open subset of $W$ is a nonempty plurifine-open subset of $U$, hence meets $U\setminus E$. Since $Z(u_j,v_j)$ is closed in $W$ and contains $W\setminus E$, it equals $W$. This proves pointwise equality for every factor.

For (a), Theorem 5.47.22 now applies directly to the pointwise equality just proved. It constructs the restrictions to possibly non-Borel $W$ via completions of the trace/coefficient measures, so no Borel hypothesis was inserted.

For (b), invoke the same pointwise equality and the established **conditional** locality statement of Proposition 13.2.6; the local-finiteness hypothesis ensures that the limiting coefficient measures and their restrictions exist, by Lemma 13.2.2. Equivalently, at every truncation level one may work on $W\cap\bigcap_j\{u_j>-k\}$, apply (a) there and pass through the increasing currents using Lemma 13.2.2. The excluded regularization programme plays no role.

### Necessity of plurifine openness (sharp boundary counterexample)

The openness hypothesis cannot be replaced by an arbitrary *closed* set, even if the potential equality holds **pointwise**, with no exceptional set. In one complex dimension put
\[
 u(z)=\max\{0,\log|z|^2\},\qquad v(z)=0,\qquad K=\{|z|\le1\}.
\]
Both $u,v$ are locally bounded psh functions on $\mathbb C$, and $u=v=0$ at every point of $K$. Nevertheless, in the Pome normalization $dd^c\log|z|^2=\delta_0$, the radial Stokes formula (or the jump in outward derivative of the radial potential at $r=1$) gives
\[
 dd^c u=\frac{d\theta}{2\pi}\ \text{on }\{|z|=1\},
 \qquad dd^c v=0.
\]
More explicitly, $\int_{\mathbb C}\chi\,dd^c u=(2\pi)^{-1}\int_0^{2\pi}\chi(e^{i\theta})\,d\theta$ for each compactly supported smooth test $\chi$; there is no atom at $0$ since $u$ vanishes on an open disk. All this mass lies in $K$, so
\[
  \mathbf1_K dd^c u\ne\mathbf1_K dd^c v.
\]
In particular $K$ cannot be plurifine open, consistently with Theorem 5.47.22. This is a **new use of an elementary already-known max-potential model**, not a new alleged error in a printed theorem or a duplicate filing of the earlier Fubini–Study circle-curvature calculation.

### Adjudication and proposed placement

The printed Theorem 5.47.22 and Proposition 13.2.6 are **correct under their stated hypotheses**; the new statement removes a *redundant pointwise equality assumption* when equality is known quasi-everywhere on a plurifine-open set. A short corollary after Theorem 5.47.22, with a cross-reference after Proposition 13.2.6, is sufficient; do not alter existing permanent tags or the canonical statements. The closed-disk example makes the topological condition essential rather than cosmetic. Affected uses include truncation restrictions for non-pluripolar products and potential representatives specified only quasi-everywhere on plurifine neighborhoods.

**Upstream limitations:** This verifies the equalizer/topological argument and its implication *conditional on* Proposition 5.47.16, Theorem 5.47.22, and Proposition 13.2.6. The prior proof dependencies (Choquet selection, Bedford–Taylor monotone continuity, coefficient domination, local mass criteria) were inspected at their cited steps but **not transitively certified**. Neither a complete §5.47 proof certification nor a project-wide verification is claimed.

## Precise fresh coverage and exclusion

- **New selected proof review, §5.47:** Definition 5.47.14, Propositions 5.47.15–16, Theorem 5.47.20, Lemma 5.47.21, Theorem 5.47.22, Proposition 5.47.23, and Propositions 5.47.25/Corollary 5.47.27, with contextual read of extremal-capacity results 5.47.6–8 and Josefson 5.47.10. These are selected statements and proofs, **not all entries** of the section.
- **New selected proof review, §5.9:** Theorem 5.9.1, Proposition 5.9.3, Lemma 5.9.4 and chart/locality discussion. No full proof chain certified.
- **Previously audited §13.2, new contextual cross-check only:** Lemmas 13.2.1–2, Definition 13.2.4, and Proposition 13.2.6 at its “Symmetry and locality” passage. Do **not** count §13.2 again as a newly entered section.
- No changes to body, source, proof registry, tags, website, main, PR state or CI. No builds/formal verification were performed. The Demailly regularization and dedicated Bergman/L²/OT programmes remain **deferred-by-user**.
