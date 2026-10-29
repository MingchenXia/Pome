# Pome mathematical audit — 2026-10-29: Hölder-density sublevels and an exceptional-flag Okounkov semigroup

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.  
**Starting audit-branch HEAD:** <code>0be5f11398544839d3127da1ef5c4945ff80805f</code>.  
**Classification:** two low-severity **verified conditional deductions**, both with complete elementary model/topological calculations; the general printed theorems and their transitive inputs are **not** certified. No previously logged gap, error, or external dependency is declared resolved. No Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof work was reopened.

## POME-DEGEN-HOLDER-SUBLEVEL-001

**Severity/status:** low / **verified conditional deduction**; not a false printed theorem, not a proof repair.  
**Reading-edition file:** <code>docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html</code>; main blob <code>044f55457f10b2f640052854a7f5f14b8403be82</code>.  
**Exact anchors:** Theorem 14.21.3, permanent tag <code>6EB399397505</code>, source <code>non-kahler-pluripotential-theory:61B8DD0F</code>, physical lines 28–50 and 133–170; Theorem 14.21.13, permanent tag <code>61851D05B072</code>, source <code>non-kahler-pluripotential-theory:A7BC9EDB</code>, lines 177–222; its quadratic zero estimate (14.21.15), permanent tag <code>BB22D6F8FAF9</code>, source <code>non-kahler-pluripotential-theory:55D866EB</code>, lines 199–209.

**Precise extension.** Fix $0<\alpha<1$. Let $X$ be connected and compact, let $\omega$ be a smooth Hermitian form and $\mathrm dV$ a smooth positive volume, and let $u,v\in C^{1,1}(X)$ have almost-everywhere semipositive $A=\omega+\mathrm{dd}^{\mathrm c}u$ and $B=\omega+\mathrm{dd}^{\mathrm c}v$, with
\[
 A^n=B^n=f\,\mathrm dV,\qquad f\in C^{1,\alpha}(X),\quad f\ge0.
\]
If
\[
 \liminf_{t\downarrow0}\frac{\operatorname{Vol}_{\mathrm dV}\{f\le t\}}{t^{1/(1+\alpha)}}=0,
\]
then $\{f>0\}$ is connected and $u-v$ is constant. The same conclusion follows if $f^{-1/(1+\alpha)}\in L^1(\mathrm dV)$ (with the reciprocal infinite on zeros). At $\alpha=1$ this recovers the square-root argument of the printed Theorem 14.21.13; for $0<\alpha<1$ it extends the density regularity range. Using Theorem 14.21.3 makes $C^{1,1}$ potentials sufficient, as already allowed in that theorem. **Theorem 14.21.3's comparison/maximum-principle proof remains a conditional internal input**, not recertified here.

**Proof of the topological statement, without PDE regularization.** At any zero $z$ of the nonnegative differentiable $f$, $\nabla f(z)=0$. On a fixed relatively compact convex coordinate chart, write $K=[\nabla f]_{C^{0,\alpha}}$. Integrating $\nabla f$ along the segment from $z$ to $x$ gives
\[
 0\le f(x)\le \frac{K}{1+\alpha}|x-z|^{1+\alpha}.
\]
If the complement of the zero set disconnects a sufficiently small coordinate ball, choose two compact transverse disks in distinct components and join corresponding points by parallel segments within that ball, as in the nonexcluded geometric argument at printed lines 197–214. Each segment meets the zero set, and its zero stays uniformly away from the endpoint disks. For all sufficiently small $t$, the segment then contains an interval of length at least
\[
 2\left(\frac{(1+\alpha)t}{K}\right)^{1/(1+\alpha)}
\]
inside $\{f\le t\}$ (if $K=0$, local $f\equiv0$, contradicting the assumed vanishing sublevel ratio). Fubini and uniform upper/lower comparison of the smooth density with Euclidean volume give
\[
 \operatorname{Vol}_{\mathrm dV}\{f\le t\}\ge c\, t^{1/(1+\alpha)}
\]
for all small $t$, contradicting the liminf assumption. The same assumption excludes positive-volume zero sets. Hence sufficiently small coordinate balls have nonempty connected intersection with $\{f>0\}$. Overlapping balls share a point in $\{f>0\}$ (because the zero set is null), so connectedness of $X$ propagates a single connected component globally. Finally,
\[
 \frac{\operatorname{Vol}\{f\le t\}}{t^{1/(1+\alpha)}}
 \le \int_{\{f\le t\}} f^{-1/(1+\alpha)}\,\mathrm dV\longrightarrow0
\]
by absolute continuity of the Lebesgue integral whenever the displayed negative power is integrable. Theorem 14.21.3 then gives $u-v$ constant.

**Sharpness of the topological exponent (not a PDE nonuniqueness assertion).** On the unit-volume flat complex torus $(\mathbb C/(\mathbb Z+i\mathbb Z))^n$, put
\[
 f(z)=|\sin(2\pi\operatorname{Re}z_1)|^{1+\alpha}.
\]
This nonnegative function is $C^{1,\alpha}$, its positive set has exactly two connected components, and elementary one-variable change of scale near its two simple zeros gives
\[
 \lim_{t\downarrow0}\frac{\operatorname{Vol}\{f\le t\}}{t^{1/(1+\alpha)}}=\frac2\pi>0.
\]
Thus the power $1/(1+\alpha)$ is optimal for this *sublevel-topology mechanism* among nonnegative $C^{1,\alpha}$ functions. No claim is made that this particular density admits two distinct solutions of a global Monge–Ampère equation.

**Proposed correction/action and dependents:** optional corollary after Theorem 14.21.13, keeping the original $C^{1,1}$-density statement, its attribution, and its permanent tags untouched. This tests the connectivity input in §14.21 and the downstream uniqueness criteria §§14.22–14.25; it neither removes the need for Theorem 14.21.3 nor certifies those downstream PDE arguments.

## POME-BLOWUP-EXCEPTIONAL-FLAG-OKO-001

**Severity/status:** low / **verified conditional deduction**; a new exact flag-valuation calculation, **not** a new registration of the previously verified $\operatorname{Vol}(H+bE)$ section-count identity.  
**Reading-edition file:** <code>docs/sections/flags-convex-bodies-and-section-growth/index.html</code>; main blob <code>83557f0e15275253661fe679c75407e6636d497c</code>.  
**Exact anchors:** flag/valuation definition §19.9.1, permanent tag <code>954DDD998705</code>, source <code>non-kahler-pluripotential-theory:5E5BBF30</code>, physical lines 12–32; Lemma 19.9.2, tag <code>2B103C3B777A</code>, source <code>non-kahler-pluripotential-theory:EAA5A841</code>, lines 36–49; §19.9.5 body definition, tag <code>E9A3FA804369</code>, source <code>non-kahler-pluripotential-theory:B9A34270</code>, lines 105–131; Proposition 19.9.6 tag <code>E6B4502ECB3B</code>, source <code>non-kahler-pluripotential-theory:A4601CA4</code>, lines 135–151; Corollary 19.9.7 tag <code>071721B08FC2</code>, source <code>non-kahler-pluripotential-theory:8930F62C</code>, lines 160–169.

**Model and full value semigroup.** Let $\pi:X=\operatorname{Bl}_p\mathbb P^2\to\mathbb P^2$ blow up $p=[1:0:0]$, let $H=\pi^*\mathcal O_{\mathbb P^2}(1)$, and let $E\simeq\mathbb P^1$ be the exceptional divisor. Fix **integers $a\ge1$, $b\ge1$** and $L=\mathcal O_X(aH+bE)$. Choose the admissible complete flag $X\supset E\supset\{q\}$ with $q$ corresponding to the tangent direction $X_1=0$. Then for every $m\ge1$, the set of actual valuation vectors is **exactly**
\[
 \{\nu(s):0\neq s\in H^0(X,L^m)\}
 =\{(mb+k,j):0\le k\le ma,\ 0\le j\le k,\ k,j\in\mathbb Z\}.
\]
Indeed, for $r\ge1$ the restriction $\mathcal O_E(maH+rE)\simeq\mathcal O_{\mathbb P^1}(-r)$ has no nonzero global sections. The divisor restriction sequences therefore identify
\[
 H^0(X,\mathcal O_X(maH+mbE))
   =\sigma_E^{mb}\,\pi^*H^0(\mathbb P^2,\mathcal O(ma)).
\]
For a nonzero homogeneous polynomial $P$ of degree $ma$, let $k=\operatorname{mult}_p P$. Its first valuation is $mb+k$. On $E$ the first nonzero homogeneous Taylor piece of $P$ has degree $k$, so the second valuation, its vanishing at $q$, lies in $[0,k]\cap\mathbb Z$. Conversely the explicit polynomial $X_0^{ma-k}X_1^jX_2^{k-j}$ realizes every pair $(k,j)$ in this range. The argument uses only restriction sequences and local blowup charts; no external convex or analytic theorem.

Consequently the precise Okounkov body is the **translated triangle**
\[
 \Delta(L)=\{(x,y)\in\mathbb R^2:b\le x\le a+b,\ 0\le y\le x-b\},
\]
with vertices $(b,0),(a+b,0),(a+b,a)$ and area $a^2/2$. For every $m$, the exact section count is
\[
 h^0(X,L^m)=\sum_{k=0}^{ma}(k+1)=\frac{(ma+1)(ma+2)}2.
\]
The valuation semigroup is generated **in degree one**: distribute any $k\le ma$ into $m$ integers $0\le k_i\le a$, then distribute $j\le k$ into $0\le j_i\le k_i$. Moreover it is saturated in its full lattice cone because its inequalities are precisely $bm\le x\le(a+b)m$, $0\le y\le x-bm$ for integral $(x,y,m)$; the three degree-one points $(b,0,1)$, $(b+1,0,1)$ and $(b+1,1,1)$ generate $\mathbb Z^3$ as a group. Hence in this model the lattice/volume normalization in Corollary 19.9.7 is verified **directly**:
\[
 \lim_{m\to\infty}m^{-2}h^0(X,L^m)=a^2/2=\operatorname{Area}\Delta(L).
\]
The fixed exceptional component changes the first valuation coordinate by $b$ but **does not** change the body area. When $a=1,b=2$, the self-intersection $L^2=-3$ contrasts with volume $1$, as previously recorded under <code>POME-AC-VOLUME-EXCEPTIONAL-NEGATIVE-001</code>; that earlier volume calculation is *not* counted as a new finding. The new content is the exact full semigroup, saturated degree-one generation, and translated-flag body.

**Proposed correction/action and dependents:** optional explicit flag example after §19.9.5–7, retaining the valuation convention and all permanent tags. Useful for checking semigroup canonicalization (§§19.3–19.4), volume-to-body normalization (§19.9), and non-nef b-divisor examples (§20). The original printed results are correct. General Kaveh–Khovanskii and compact-manifold growth arguments are **not** independently certified by this example.

## Coverage, unchanged findings, and excluded work

- **New proof-level mathematical calculations:** $C^{1,\alpha}$ density extension and sharp topological model around already selected §14.21.13; entire degree-by-degree exceptional-flag valuations and semigroup for already selected §19.9.1/.2/.5–7. These are *incremental targeted checks*, **not first visits** to either section and **not complete-section certifications**.
- **Contextual only:** §14.20.1 polarization, §19.7.20 semigroup theorem, and the previously recorded big-class volume example. They are not represented as newly checked.
- **Coverage inventory:** the current project still has **25 chapters and 747 distinct numbered ToC sections; zero entire sections or chapters mathematically certified**. Prior unresolved, confirmed-error, verified-repair and external-input ledger entries remain unchanged.
- **User exclusion:** Demailly approximation/regularization and the dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme remains **deferred-by-user, not resolved or verified**. This review neither entered those proofs nor tried to repair their prerequisites.
- **No production edits:** no source, mathematical body, registry, canonicalization, permanent tag, website, PR, CI, build, or formalization change. A small independent enumeration of integer pairs for $(a,b)=(1,2),(2,3)$ and $m=1,2,3$ agreed with the closed formula; this is not a repository test suite or formal proof.
