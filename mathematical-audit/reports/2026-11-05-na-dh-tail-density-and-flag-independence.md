# Non-Archimedean Duistermaat–Heckman distributions: exact tails, flag independence, density, and the terminal atom

**Date:** 2026-11-05. **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (not changed).

**Stable finding IDs:** \`POME-NA-DH-TAIL-FLAG-INDEPENDENCE-001\` (medium / **verified repair**: a shorter alternative proof of one valid theorem clause, not a false theorem); \`POME-NA-DH-DENSITY-ENDPOINT-ATOM-001\` (low / **verified conditional deduction**).

**Exact integrated reading edition:** \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, main blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`, physical lines 902–997 (Definition 22.1.55 at 907–912; Theorem 22.1.56 and moments 915–933; original long approximation-based flag-independence proof 933–997). Source/permanent labels: Definition 22.1.55 \`sgpt:115B0C00\` / \`9ADEFD2FF381\`; Theorem 22.1.56 \`sgpt:420C36E9\` / \`0AD7F80A793D\`; Eq. 22.1.57 \`sgpt:097E0D17\` / \`A51020D58E6F\`; Eq. 22.1.58 \`sgpt:7D143167\` / \`51031202809C\`. The relevant reading-edition heading is §22.1.54 (permanent \`3C0D12E80020\`).

## The claim and its precise scope

Let \`X\` be a connected compact Kähler manifold of dimension \`n>=1\`, \`theta\` a smooth closed real \`(1,1)\`-form representing a **big** class, and
\[
\Gamma\in\mathrm{PSH}^{\mathrm{NA}}(X,\theta)_{>0}.
\]
Set \(a=\Gamma_{\max}\), \(V=\operatorname{vol}\Gamma>0\), and, for \(t<a\), set
\[
M(t):=\operatorname{vol}(\theta+dd^c\Gamma_t).
\]
Here \(\operatorname{vol}\) denotes **the non-pluripolar mass in the convention of Pome**, not Euclidean lattice volume; the latter has a factor \(1/n!\). Suppose first that \(X\) admits a smooth admissible flag \(Y_\bullet\), as in Definition 22.1.55, and write \(\mu_Y=\operatorname{DH}_Y(\Gamma)\).

**Exact tail identity, with no finite-energy or moment assumption:**
\[
\boxed{\quad \mu_Y([t,\infty))=M(t)\quad \text{for every }t<a.\quad} \tag{A}
\]
In particular \(M(t)\) and \(V=\lim_{t\to-\infty}M(t)\) uniquely determine the full finite Borel measure \(\mu_Y\), independently of the flag. Thus (A) supplies a direct **replacement for the flag-independence step of Theorem 22.1.56**. It does not invoke that theorem, its moment method, the bounded-support reduction, or its \(\epsilon\)-approximating test curves.

**Additional distributional structure:**
\[
\boxed{\quad
\mu_Y=(-M'(t))\,\mathbf 1_{(-\infty,a)}(t)\,dt
       +M(a-)\,\delta_a,\qquad
M(a-)=\lim_{t\uparrow a}M(t).\quad} \tag{B}
\]
The derivative is the almost-everywhere derivative of a locally Lipschitz function. In particular, the measure is absolutely continuous below its maximal spectral value, has **no atom at any \(t<a\)**, and has **no singular-continuous component**. A possibly nonzero atom can occur only at the **top endpoint \(a\)**. Moreover \(M^{1/n}\), and therefore \(\log M\), is concave on \((-\infty,a)\); the a.e. hazard ratio \(-M'/M\) is nondecreasing.

These conclusions remain conditional only on the specific internal Okounkov-body construction and mass dictionary listed below. In the no-smooth-flag case, the same description carries over to Definition 22.1.59 **provided** the birational definition and its independence are established; no new assertion about resolving flags is made here.

## Proof, including the exact factor \(n!\)

Fix an admissible smooth flag. Put
\[
\Delta=\Delta_{Y_\bullet}(\theta,\Gamma_{-\infty}),
\qquad B_t=\Delta_{Y_\bullet}(\theta,\Gamma_t)\quad(t<a).
\]
Theorem 19.6.24 identifies \(B_\bullet\) as an Okounkov test curve on \(\Delta\). Theorem 19.5.26(1), applied at **each fixed level**, gives
\[
n!\operatorname{vol}_{\mathbf R^n}(B_t)=M(t),
\qquad
n!\operatorname{vol}_{\mathbf R^n}(\Delta)=V. \tag{1}
\]
These are precisely the internal analytic inputs; their full upstream proofs are **not independently certified by this report**. Under the definitions, \(B_t\) is a compact convex body, \(B_s\supseteq B_t\) for \(s<t<a\), and
\[
B_{(1-\lambda)s+\lambda t}
\supseteq (1-\lambda)B_s+\lambda B_t
\qquad(0\leq\lambda\leq1). \tag{2}
\]

Let \(G:\Delta\to[-\infty,a]\) be the Legendre test function of Definition 19.6.7. By the *inverse* Legendre relation (19.6.8 and Theorem 19.6.13),
\[
B_t=\{x\in\Delta:G(x)\geq t\},\qquad t<a. \tag{3}
\]
To see the endpoint convention directly: if \(G(x)>-\infty\), the supremum of those \(s\) with \(x\in B_s\) is attained for \(s<a\), by the left-continuity of the compact convex levels; if \(G(x)=a\), then \(x\) belongs to **all** levels \(t<a\). A point with \(G(x)=-\infty\) belongs to none. No equality at the *endpoint level* \(a\) is required for (3).

By Definition 19.6.18 and Definition 22.1.55,
\[
\mu_Y=n!\,G_*(\mathbf 1_\Delta\,d\lambda).
\]
The pushforward is a measure on \(\mathbf R\), since the convex test function \(G\) is finite on the interior of the full-dimensional body \(\Delta\), whose boundary has Lebesgue measure zero. Consequently, (3) and (1) give
\[
\mu_Y([t,\infty))=n!\lambda(\{G\ge t\})
=n!\lambda(B_t)=M(t),
\]
which proves (A) without computing a single moment. The measures obtained from *any two flags* have identical tails for every \(t<a\), are both supported on \((-\infty,a]\), and have the same finite total mass \(V\); the tails determine their values on all half-open intervals, hence on all Borel sets. This proves flag independence without using the original approximation argument.

To prove (B), take \(s<t<a\). Brunn–Minkowski applied to (2) gives
\[
M((1-\lambda)s+\lambda t)^{1/n}
\ge(1-\lambda)M(s)^{1/n}+\lambda M(t)^{1/n}. \tag{4}
\]
Proposition 19.6.4 also guarantees that \(M(t)>0\) and that the levels, hence \(M\), vary continuously for \(t<a\). Alternatively (4) gives local continuity and local Lipschitz regularity immediately, since a finite concave function on an open interval is locally Lipschitz. Raising to the \(n\)-th power preserves local Lipschitz regularity because \(M^{1/n}\) is locally bounded. Thus \(\mu_Y(\{t\})=0\) for every \(t<a\): by (A),
\[
\mu_Y(\{t\})=M(t)-\lim_{s\downarrow t}M(s)=0.
\]
For each bounded interval \((s,t]\subset(-\infty,a)\), (A) now yields
\[
\mu_Y((s,t])=M(s)-M(t)=\int_s^t -M'(u)\,du. \tag{5}
\]
Uniqueness on intervals proves the absolute-continuity assertion on \((-\infty,a)\), including the exclusion of a singular-continuous part. The measure has no mass above \(a\). Continuity from above for the finite measure gives
\[
\mu_Y(\{a\})=\lim_{t\uparrow a}\mu_Y([t,\infty))
=\lim_{t\uparrow a}M(t)=M(a-).
\]
Finally \(M(t)\uparrow V\) as \(t\to-\infty\) by the defining Hausdorff exhaustion \(B_t\to\Delta\) and continuity of convex-body volume. Hence the continuous density plus the one endpoint atom exhaust the total mass \(V\). This proves (B).

Since \(M^{1/n}\) is positive and concave by (4), \(\log M=n\log(M^{1/n})\) is concave on \((-\infty,a)\). Its derivative is nonincreasing wherever it exists; thus \(-M'/M\) is nondecreasing almost everywhere. This is a statement about the tail hazard, **not** a claim that the density itself is log-concave.

## Explicit test-curve calibration; atom at the correct endpoint only

The following is an **abstract convex Okounkov test curve**, not an assertion that every such test curve has already been realized by a geometric non-Archimedean \(\Gamma\). Take \(\Delta=[0,1]^n\), any \(a\in\mathbf R\), \(b>0\), \(c\in(0,1)\), and the concave continuous test function
\[
G(x)=a-b(x_1-c)_+.
\]
Its levels \(B_t=\{G\ge t\}\) satisfy Definition 19.6.1 and, for \(t<a\),
\[
n!\operatorname{vol}B_t
=n!\min\{1,c+(a-t)/b\}.
\]
Direct Fubini integration gives, **including the exact mass at the upper endpoint**,
\[
n!\,G_*\lambda
=\frac{n!}{b}\,\mathbf1_{(a-b(1-c),\,a)}(t)\,dt
+n!c\,\delta_a.
\]
The absolutely continuous part has mass \(n!(1-c)\), the endpoint atom has mass \(n!c\), and total mass is \(n!\operatorname{vol}\Delta=n!\). The case \(G\equiv a\) gives the allowable pure endpoint atom \(n!\delta_a\). This checks normalization, interval orientation, and the fact that no interior atom appears despite a positive-volume plateau of \(G\).

## Impact and precise limitations

* **Verified proof-step replacement**: Theorem 22.1.56's **flag independence** follows from the exact tails and internal Theorems 19.5.26(1), 19.6.13, 19.6.24, without the proof's bounded-support moment determinacy, \(\epsilon\)-approximation from 17.13.21, or the \(d_S\)/Hausdorff continuity steps 16.9.14 and 19.6.22. This identifies a shorter dependency path, not an error in the printed proof. Keep the Boucksom–Jonsson and Ross–Witt Nyström historical attributions intact.
* **Verified conditional deduction**: (B), including the unique possible top atom, is genuinely stronger than integer moment identities 22.1.57–58; it requires **no finite moments**, so it covers cases where those identities have extended values. It does not by itself prove the general comparison theorem, continuity Proposition 22.1.60, or any unverified upstream mixed-mass theorem.
* **Dependencies still open**: geometric existence/continuity of partial Okounkov bodies (19.5.26), model test-curve correspondence (19.6.24), and the internal Brunn–Minkowski argument have been used with exact hypotheses, not certified end-to-end. Extension to manifolds without smooth flags in Eq. 22.1.59 uses the separate birational independence input 19.5.26(5); this remains open here. No sequential compactness, exchange of unrelated limits, or regularization theorem is asserted.
* **Proposed integration, audit only**: place (A) and its short proof after Definition 22.1.55 or within Theorem 22.1.56, and add the locally absolutely continuous/endpoint-atom refinement as a remark after the theorem. Preserve the theorem statement, provenance, permanent tags, and existing longer proof until a separately reviewable source/body patch is accepted.

**Exact cross-section anchors (dependency inspection, not full audit):**
* \`docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html\`, blob \`20ff3089e62dd1c8349e8bcc077ec64605a9788b\`: Definition 19.6.1 \`sgpt:26A94CBB\` / \`ACD722F45231\` lines 16–52; Proposition 19.6.4 \`sgpt:5FBEF833\` / \`29A7DDA38CA2\` lines 55–85; Legendre Definition 19.6.7 \`sgpt:2E276BD3\` / \`7B20D9977149\` lines 112–134; Definition 19.6.18 \`sgpt:09132002\` / \`51940EF88F4F\` lines 328–334; Theorem 19.6.24 \`sgpt:43914315\` / \`74133E3920A2\` lines 447–453. (All locations are physical integrated HTML line numbers.)
* \`docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html\`, blob \`a53c6b2f80c3775e9d646f57808425823ec4a4ac\`: Theorem 19.5.26(1), source \`sgpt:9B46A73A\` / permanent \`944BC14A8246\`, lines 310–318; its scope is positive-volume currents, satisfied by the levels in Theorem 19.6.24.

**Coverage:** actual new selected subsection §22.1.54–59 distribution/flag-independence mathematics, plus only the specifically cited §§19.5–19.6 convex/Legendre/mass hypotheses; **not** mathematical certification of all of §22.1 or any full chapter. As checked against the current published ToC, the collection still has **25 chapters, 747 numbered sections, and zero wholly mathematically certified sections**. All earlier confirmed errors, gaps, candidates, external dependencies, duplications, and repairs remain separately classified. Demailly approximation/regularization and its dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remain **deferred-by-user**: neither reopened nor marked resolved.

This is an audit-only proposal; no production main, source document, registry, tag, CI, build, formal verification, or website publication is involved.
