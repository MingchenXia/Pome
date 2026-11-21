# Analytic density tails, degenerate Monge–Ampère uniqueness and radial ODEs — 21 November 2026

## Immutable review target and scope

- **Main revision:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Direct full-section readings:** \`docs/sections/uniqueness-for-degenerate-equations--comparison-and-invariant-mass/index.html\` (reader §14.25, mathematical physical lines **7–115**, blob \`7683a63656f9b4311a77d1db8e260a1bdc65f0b0\`); \`docs/sections/uniqueness-for-degenerate-equations--nonuniqueness-with-a-zero-set-of-empty-interior/index.html\` (§14.27, mathematical physical lines **7–198**, blob \`3cd83bbb6ab246cda0adae1789d7374d815529a6\`); \`docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html\` (§14.29, mathematical physical lines **7–210**, blob \`2f00a81edc49855971bb3a6d774603ee5bbf40db\`).
- **Selected prerequisites, not full additional section reviews:** §14.26.2–14.26.11, especially (14.26.3)–(14.26.6), (14.26.11), mathematical lines 21–63, 154–161 (blob \`7240d97e9192c70acf09f755ec90a5420bc11ef7\`); §14.28.3–14.28.6, mathematical lines 66–133 (blob \`7a70517262563acf523940c261daa8ec11a8cb55\`); §14.21.13–14.21.15, mathematical lines 177–223 (blob \`044f55457f10b2f640052854a7f5f14b8403be82\`). §14.28 previously had a separate whole-section review; it is **not** counted again as new whole-section coverage.
- The selected current chapter TOC is \`docs/chapters/monge-ampere-equations/index.html\` (29 sections). The existing 747-section register is retained, with unknown earlier visits left unreconciled.
- User-excluded Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programmes are **deferred-by-user**, not resolved, repaired or certified. None is revisited here.

## Finding POME-P3-ANALYTIC-DENSITY-EXACT-TAIL-001

**Status:** verified conditional deduction. **Severity:** low. **No false printed theorem, no complete transitive certification.**

**Primary anchors:** §14.29 Theorem **14.29.1**, permanent tag **DD001DBBE659**, mathematical lines 11–20; formula **(14.29.2)** source label **B358F4101DED**, lines 15–18; §14.29 **(14.29.16)** source label **C72BCF7334A2**, lines 199–206. Secondary affected result: §14.21 Theorem **14.21.13**, source tag **61851D05B072**, lines 186–223, for which the original square-root threshold is sharp.

**Claim and normalization.** Let the homogeneous blocks \(A,B\in\mathbb C^2\), \(t=|A|^2/(|A|^2+|B|^2)\), \(a=(1+\mathrm e)^{-1}\), \(b=\mathrm e(1+\mathrm e)^{-1}\) and \(f_*(t)=(t-a)^2(t-b)^2\) be *exactly* as in §14.29.1. Write \(V=\int_{\mathbb P^3}\omega_X^3\), \(c=ab=\mathrm e/(1+\mathrm e)^2\), and \(\Delta=b-a=(\mathrm e-1)/(1+\mathrm e)=\sqrt{1-4c}>0\). Then

\[
 \frac{1}{V}\int_{\mathbb P^3}\Phi(t)\,\omega_X^3
   =\int_0^1 6t(1-t)\Phi(t)\,dt
\]
for any bounded Borel function \(\Phi\). With \(q=t(1-t)\), \(0<q<1/4\), the pushforward density is **exactly**
\[
 \frac{12q}{\sqrt{1-4q}}\,dq,
 \qquad f_*=(q-c)^2.
\]
Consequently, for
\[
 0<s<s_0:=\min\{c^2,(1/4-c)^2\},
\]
the normalized sublevel distribution equals
\[
 \boxed{\frac{\operatorname{Vol}\{f_*\le s\}}{V}
 =\int_{c-\sqrt{s}}^{c+\sqrt{s}}\frac{12q}{\sqrt{1-4q}}\,dq
 =\mathcal A(c+\sqrt{s})-\mathcal A(c-\sqrt{s}),}
 \qquad
 \mathcal A(q)=-\tfrac32\sqrt{1-4q}+\tfrac12(1-4q)^{3/2}.
\]
In particular, unlike the comparability \(\asymp\sqrt{s}\) printed in (14.29.16), the **exact leading constant and next term** are
\[
 \boxed{\frac{\operatorname{Vol}\{f_*\le s\}}{V}
  =\frac{24c}{\Delta}\sqrt{s}
   +\frac{16(1-c)}{\Delta^5}s^{3/2}
   +O(s^{5/2}).}
\]
The leading coefficient is \(24\mathrm e/(\mathrm e^2-1)\). At the sharp integrability exponent,
\[
 \lim_{\varepsilon\downarrow0}
 \frac{1}{V\log(1/\varepsilon)}
 \int_{\{f_*\ge\varepsilon\}}f_*^{-1/2}\,\omega_X^3
   =\frac{12c}{\Delta},
\]
and, as \(\alpha\uparrow1/2\),
\[
 \boxed{\lim_{\alpha\uparrow1/2}(1-2\alpha)
    \frac{1}{V}\int_{\mathbb P^3} f_*^{-\alpha}\,\omega_X^3
       =\frac{24c}{\Delta}.}
\]
The same **normalized** distribution and constants hold for the higher-dimensional product examples \(\mathbb P^3\times\mathbb P^{n-3}\) of §14.29, with volume \(\Omega_n^n\) and pulled-back \(f_*\).

**Proof.** A standard isotropic complex Gaussian vector in \(\mathbb C^4=\mathbb C^2\oplus\mathbb C^2\) projects to normalized Fubini–Study volume on \(\mathbb P^3\): the pushforward is \(U(4)\)-invariant and therefore equals the unique invariant probability measure \(\omega_X^3/V\). The squared block norms \(S=|A|^2\), \(T=|B|^2\) are independent gamma random variables of shape two with density \(xe^{-x}\,dx\). The change of variables \(w=S/(S+T)\), \(z=S+T\), with Jacobian \(z\), yields the joint density \(w(1-w)z^3e^{-z}\,dw\,dz\); integrating \(z\) gives \(6w(1-w)\,dw\). Thus the first formula holds without assuming any regularity of \(\Phi\). Since \(a+b=1\) and \(ab=c\), \((t-a)(t-b)=t^2-t+c=c-q\). For each \(0<q<1/4\), its two inverse images \(t=(1\pm\sqrt{1-4q})/2\) have Jacobian \(|dt/dq|=(1-4q)^{-1/2}\), and \(6t(1-t)=6q\), giving the indicated \(12q/\sqrt{1-4q}\).

For the specified small \(s\) the interval \([c-\sqrt{s},c+\sqrt{s}]\) lies strictly in \((0,1/4)\). Direct differentiation shows \(\mathcal A'(q)=12q/\sqrt{1-4q}\), proving the exact formula. With \(g(q)=12q(1-4q)^{-1/2}\), \(g(c)=12c/\Delta\) and \(g''(c)=48(1-c)/\Delta^5\), symmetric Taylor integration over \([c-\sqrt{s},c+\sqrt{s}]\) gives \(2g(c)\sqrt{s}+\tfrac13g''(c)s^{3/2}+O(s^{5/2})\). Smoothness near \(c\) justifies the remainder.

At \(\alpha=1/2\), write \(u=q-c\) and integrate \(g(c+u)/|u|\) on \(|u|\ge\sqrt{\varepsilon}\) in a fixed neighborhood of zero: the divergence is \(g(c)\log(1/\varepsilon)+O(1)\); the complement contributes \(O(1)\). Similarly, for \(\alpha<1/2\), the local integral \(g(c+u)|u|^{-2\alpha}\) has leading singularity \(2g(c)/(1-2\alpha)\) as \(\alpha\uparrow1/2\); the smooth remainder and the complement have vanishing contribution after multiplication by \(1-2\alpha\). In the product case \(\Omega_n^n=\binom n3\pi_1^*\omega_X^3\wedge\pi_2^*\theta^{n-3}\), so the normalized \(t\)-distribution is unchanged.

**Dependencies and correction:** The probability/pushforward and tail calculations are direct and independent of the *existence* of the nonunique solution forms. Their application to the nonuniqueness phenomenon is **conditional on** Theorem 14.29.1's explicit construction, which was inspected but whose full transitive upstream chain is not certified. Add the above formula as an optional supplementary corollary after (14.29.16), without changing the valid \(\asymp\sqrt{s}\) assertion or permanent tags. The \(\alpha=1/2\) threshold of §14.21.13 is quantitatively sharp for these examples. No original statement is false.

## Direct review: §14.25

- Equations (14.25.1) and (14.25.4), Theorem 14.25.3 (tag **FE27B72E2DB5**) lines 10–65: verified the max-potential decomposition and the direction of the contact-measure order. The converse uses the ability to shift one smooth potential by a constant, then the internally cited total-mass characterization; it does **not** prove the latter anew.
- Theorem 14.25.2 (tag **27DED19DBC11**), lines 69–111: checked \(G=2F{\bf1}_S+b_0\) with \(\int G\,\omega^n=V\), the mixed Minkowski factor \(A_\delta=((1-\delta)+\delta2^{1/n})^n>1\), the correct comparison orientation on \(E_\delta=\{v<q_\delta\}\), and the use of the bounded domination principle to conclude \(u-v\) is constant. There is no division by \(F\) on its zero set. Note that existence, mixed inequality and domination remain **separate unverified ancestors**: §§14.19.2, 5.28.9, 14.19.10 and mass invariance §§11.1.3/11.1.7.
- No new confirmed printed error. The equivalence here holds under the **Guan–Li background condition**, not for the general nonclosed metric of §§14.27–14.29.

## Direct review: §14.27

- Theorem 14.27.1 (tag **E16A6F31A061**), lines 11–47, uses the smooth flat bump \(p=C\exp[-1/(1-r^2)]\), compactly supported on \((-1,1)\), and \(k_s=(x+sp)(y-sp)(z+sp')\). The determinant is positive away from the two zero levels, while the limiting form has rank one there.
- Lemma 14.27.3 (tag **C96C68E6BB33**), lines 51–120: checked the left backward lower barrier \(c_Lp\), the right forward lower barrier \(-tp\), the strict signs in (14.27.5) and (14.27.6), and extension of the initial-value solution throughout \((-1,1)\) using compact trapping on compact subintervals.
- Lemma 14.27.7 (tag **31CA87ECD1DF**), lines 125–171: checked the endpoint ratios \(\xi=h/p\), rational ODE (14.27.8), polynomial derivative growth, and that multiplication by the flat bump gives infinite-order vanishing. On lines 176–198, the positive coefficient identity \(z+h'=k_s/[(x+h)(y-h)]\) and distinct initial slopes verify the claimed semipositivity and uncountability, conditional on the §14.26 rank-one forms.
- The theorem is **not** a counterexample to §14.25: the constructed Hermitian form need not satisfy the Guan–Li condition. No new confirmed printed error.

## Direct review: §14.29

- Theorem 14.29.1 (tag **DD001DBBE659**) and (14.29.3)–(14.29.10), lines 11–105: checked \(\sigma'=\sigma(1-\sigma)\), \(\omega_X^3=6(\sigma')^2P\wedge Q\wedge R\), \(d_*=(1-r^2)^2H_*^2\), positivity of both triples and the crucial equality \(qD_*=z_bE_*\). The determinant \((D_*+E_*)(z_b-q)=(D_*-E_*)(z_b+q)=d_*\) has consistent normalization.
- Lines 107–165: checked that the cutoff interpolation occurs away from the zero levels; \(z=d_*/(xy)\) retains the product, matching \(z_b\) on the overlap. The exact perturbation \(dd^c(\varepsilon(r^2-1)\eta)\) restores positive background coefficients without changing either solution form. The nonclosure calculation \((z_b(0)+1/2)\,dr\wedge(Q-P)\neq0\) has the claimed sign.
- Lines 167–210: checked regularity of \(t\), the two connected zero hypersurfaces, rank of the two degenerate forms, binomial coefficient \(\binom n3\) in the higher-dimensional product, and the \(1/2\) integrability threshold. The new density-law calculation above refines (14.29.16), not repairs it.
- No newly confirmed printed error; full upstream proof chains **not** re-certified. §14.26's rank-one decomposition and all external topology/regularity inputs remain selectively checked only.

## Audit status and limitations

- Newly directly reviewed in full: **3 current reader sections (§14.25, §14.27, §14.29)**; selected prerequisites: **3 additional sections (§14.21, §14.26, §14.28)**. First-ever visits **not** claimed and preexisting §14.28 whole-section audit preserved.
- Findings: **one genuinely new, mathematically proved conditional deduction**, **zero newly confirmed printed errors**, **zero complete transitive proof-chain certificates**.
- No code/build/browser test/CI or site publication was performed. No main, sources, registry, canonicalization or permanent tags changed.
- Open issues: fully audit the §14.19 continuous existence/domination inputs and §5.28 mixed inequality independently; separately review Guan–Li mass invariance (§11.1) and the §14.26 global rank-one extension. Do **not** reopen user-excluded regularization proof-completion topics.
