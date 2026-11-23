# Audit: Newton bodies under toric maximum/rooftop; a divisor denominator prerequisite

Date: 2026-11-23. Reviewed Pome main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Audit branch: review/mathematical-audit.

## Scope and source anchors

- Complete *nonexcluded* direct reading of the current §19.4.1–56 algebraic partial Okounkov body statements and their integrated proofs. Relevant file: **docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html**, blob **c661e264cab0995a2a344453039940028feff8e0**. Special attention to Proposition 19.4.7 (source sgpt-32BC1D4A, permanent tag 632B1323B741, lines 58–122), twisted Proposition 19.4.12 (sgpt-ADB3B184, tag 1ED4AF0D9A23, lines 174–198), and Lemma 19.4.43 (sgpt-10EC43BE, tag FD338F03BE48, lines 632–678). Analytic approximation inputs are **not** reexamined.
- Selected previously incompletely reviewed §21.12, emphasizing Theorem 21.12.13 and Propositions 21.12.21, 21.12.23, 21.12.24. File: **docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html**, blob **56a1a55dfc8185aee0e6d495a6a93d8a2313d76b**. Anchors: source sgpt-E09727EF / tag 8B5B73657BF7 (line 238 onward), sgpt-E2F47062 / tag 419A1D9F18A9 (lines 390–413), sgpt-A47B98F5 / tag 73034E124A9A (lines 443–465), sgpt-D3D075B2 / tag 725063C1ED05 (lines 466–520). Convex Legendre duality from §21.11 is used only as an already stated input, **not** recertified.
- §19.3 Remark 19.3.3 (source sgpt-00F064E7, permanent tag 5AA6A085DBB0) was consulted solely to interpret the valuation-on-a-modification step in Proposition 19.4.7. Its previously logged flag-model external-input/Step 1 issue is **not** a new finding here.

## POME-OKOUNKOV-ANALYTIC-RESIDUE-DIVISIBILITY-001

**Severity: low. Status: proof gap, local and repairable; not a counterexample to the lemma.**

In the analytic-singularities proof of Lemma 19.4.43, lines 646–661, a rational effective divisor D and a positive rational ε are fixed. The text chooses a positive integer N so that **ND is integral and Nε is an integer**. The upper comparison at line 659, however, invokes Proposition 19.4.12 for the divisor class

\[
NL-N(1-\epsilon)D.
\]

The quoted twisted Proposition 19.4.12 is stated for an actual line bundle, so using it literally requires **N(1−ε)D integral** too, or a separately established Q-divisor variant with appropriately handled ceilings. The printed two conditions do not imply this third integrality requirement. For example, if D=E/2, ε=1/2, N=2, then ND=E and Nε=1, yet N(1−ε)D=E/2.

**Precise local correction.** Choose N divisible by the denominators of both D and (1−ε)D (and of ε, if the printed integer condition is retained). This is possible for rational ε and Q-divisor D and ensures that both NL−ND and NL−N(1−ε)D are genuine integral Cartier line bundles on the smooth model. The residue-class comparisons then have integral line-bundle inputs and one can invoke Proposition 19.4.12 exactly as stated. The division by N at the limit is unchanged.

**Affected dependents:** the particular upper sandwich in Lemma 19.4.43, and therefore its use by Theorem 19.4.41. This is a missing divisibility clause in the written proof, not evidence that Hausdorff convergence is false. The higher-level approximation input is not certified here; the proposed fix is complete *only for this integrality point*. No reading-edition/source patch was applied.

## POME-TORIC-NEWTON-MAX-ROOF-CONVEX-LATTICE-001

**Severity: low. Status: verified conditional deduction from the presently stated toric Legendre correspondence and toric non-pluripolar mass formula; not a printed error.**

Let (X,ω) be the smooth polarized compact toric variety of §21.12, associated with the full-dimensional lattice polytope P. For toric ω-psh potentials u,v, write G_u,G_v for their closed proper Legendre conjugates, whose effective domains lie inside P. Define

\[
K(u)=\overline{\operatorname{dom}G_u}\subseteq P,\qquad
K(v)=\overline{\operatorname{dom}G_v}\subseteq P.
\]

We use the fact that n! times ordinary lattice-normalized Euclidean volume of K(u) is the non-pluripolar mass of ω+dd^c u (§21.12.24).

**(A) Maximum.** For w=max(u,v),

\[
\boxed{K(w)=\operatorname{conv}\bigl(K(u)\cup K(v)\bigr)},\qquad
\boxed{\operatorname{Mass}(w)=n!\operatorname{vol}\operatorname{conv}\bigl(K(u)\cup K(v)\bigr)}.
\]

**Proof.** Each closed proper G_i has compact effective-domain closure K_i and is bounded below on P. Its conjugate F_i(tξ) satisfies

\[
\lim_{t\to+\infty}t^{-1}F_i(t\xi)=h_{K_i}(\xi)
\]

for every ξ: the upper bound follows from the lower bound of G_i, and the lower bound follows by fixing a finite point of G_i arbitrarily close to the support supremum. The toric correspondence gives F_w=max(F_u,F_v) (§21.12.23). Thus its recession support function equals max(h_K(u),h_K(v)), which is the support function of conv(K(u)∪K(v)). Uniqueness of compact convex sets from support functions proves the first boxed identity. The toric mass formula proves the second.

**(B) Rooftop.** The ω-psh rooftop r=u∧v is not identically −∞ **if and only if** the actual effective domains (not merely their closures) meet:

\[
\boxed{r\not\equiv-\infty\iff\operatorname{dom}G_u\cap\operatorname{dom}G_v\ne\varnothing}.
\]

When it exists,

\[
\boxed{K(r)=\overline{\operatorname{dom}G_u\cap\operatorname{dom}G_v}},\qquad
\boxed{\operatorname{Mass}(r)=n!\operatorname{vol}(K(u)\cap K(v))}.
\]

**Proof.** A toric potential below both u,v corresponds to a proper closed convex G dominating both G_u,G_v. The pointwise maximum of these two G's is proper precisely when their effective domains intersect; if it is proper it is closed convex, and its conjugate produces the maximal common lower bound. This is exactly the content of §21.12.21. Its finite domain is the actual intersection. For the mass identity, if K(u)∩K(v) has zero n-dimensional volume, so does K(r). If its volume is positive, both K's are full-dimensional and int K_i lies in dom G_i (a convex set contains the interior of its closure). Hence the closure of the actual-domain intersection and K(u)∩K(v) differ only on a Lebesgue-null convex boundary. Applying §21.12.24 proves the final formula. This does **not** assert equality of the two closed sets, which can fail at a shared boundary point.

**(C) Explicit P¹ model showing the domain-versus-closure distinction.** Fix 0<a<b<1, P=[0,1], and define G_u as the convex indicator of [0,a], and G_v as the convex indicator of [b,1]: each is zero on its interval and +∞ outside it. Their conjugates on the tropical real coordinate s=log|z|² are

\[
F_u(s)=\max(0,as),\qquad F_v(s)=\max(bs,s).
\]

Taking the Fubini–Study reference F_0(s)=log(1+e^s), the toric ω-psh potentials are u=F_u−F_0 and v=F_v−F_0 on C*. Their Newton bodies are [0,a] and [b,1], of masses a and 1−b. The rooftop is identically −∞ because these *actual* effective domains are disjoint. Independently, u has Lelong number 1−a at infinity, and v has Lelong number b at zero; any common ω-psh minorant would have Lelong mass at least (1−a)+b>1, contradicting the total cohomological mass one. Nevertheless,

\[
F_{\max(u,v)}(s)=\max(0,s),\qquad K(\max(u,v))=[0,1],
\]

so max(u,v) is bounded on P¹ and has **full non-pluripolar mass 1**, although the two starting masses were strictly below one. This is a model phenomenon, **not** a counterexample to any printed theorem.

An auxiliary caution: replacing the rooftop criterion by K(u)∩K(v)≠∅ is invalid. To see the difference with *touching* Newton bodies, take G_1(m)=−log(1/2−m) on [0,1/2), and G_2(m)=−log(m−1/2) on (1/2,1], both +∞ elsewhere. They are proper closed convex on P, their domain closures meet at 1/2, but the effective domains do not; the rooftop is still −∞. Thus positivity of the *intersection volume*, not mere contact of the closures, is the reliable mass statement.

## Audit limits and status

The toric identities are conditional on the precise already-integrated §21.12 toric correspondence and mass formula. Their complete transitive proofs (especially the general complex Monge–Ampère/convex approximation arguments) were **not** independently certified. No Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was resumed. Those remain **deferred-by-user**, not resolved. This run did not audit the entire §21.12, nor did it claim first-ever historical visits. No tests, builds, CI, production registry/body/label edits, branch merges, or publication were performed.
