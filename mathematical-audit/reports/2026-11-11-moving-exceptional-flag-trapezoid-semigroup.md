# Mathematical audit — 2026-11-11: moving exceptional-flag graded semigroup

**Finding:** POME-OKO-BLOWUP-MOVING-FLAG-NORMAL-SEMIGROUP-001. **Severity/status:** low / **verified conditional deduction** (an explicit algebraic model, not a correction to the printed theorem and not a general proof-chain certification).

**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/flags-convex-bodies-and-section-growth/index.html (blob 83557f0e15275253661fe679c75407e6636d497c).

**Source and permanent anchors:**
- §19.9.1, non-kahler-pluripotential-theory:5E5BBF30, permanent 954DDD998705, physical lines 12–32.
- Lemma 19.9.2, non-kahler-pluripotential-theory:EAA5A841, permanent 2B103C3B777A, physical lines 35–54.
- Theorem 19.9.9, non-kahler-pluripotential-theory:4EE23942, permanent CC2BF9294FA3, physical lines 193–244; Proposition 19.9.10, non-kahler-pluripotential-theory:41E2532A, permanent E32D710594E0, physical lines 246–272.
- Lemma 19.9.15, non-kahler-pluripotential-theory:41985179, permanent 744C8C462232, physical lines 321–346; Theorem 19.9.16, non-kahler-pluripotential-theory:6F0F3D7F, permanent 1EBEF54DB76D, physical lines 348–371.

## New model and exact statements

Let $\pi:X=\operatorname{Bl}_p\mathbb P^2\to\mathbb P^2$, $p=[0:0:1]$, with $H=\pi^*\mathcal O_{\mathbb P^2}(1)$ and exceptional curve $E$. Take integers $a\ge b\ge0$ with $a\ge1$, and the moving linear system $L=\mathcal O_X(aH-bE)$; write $c=a-b$. Choose the complete flag $X\supset E\supset\{q\}$, where $q=[0:1]$ on $E=\mathbb P(T_p\mathbb P^2)$.

For every integer $k\ge0$, **the entire valuation set** of nonzero sections of $L^k$ is
\[
\Gamma_k=\{(j,\ell)\in\mathbb Z^2:0\le j\le ck,\quad 0\le\ell\le bk+j\}.
\]
Each valuation is represented by exactly one distinguished degree-$ak$ monomial. The full semigroup $\Gamma=\{(k,j,\ell): (j,\ell)\in\Gamma_k\}$ is **generated in degree one and saturated** in its difference lattice; the entire section ring is the semigroup algebra $\mathbb C[\Gamma]$ and is **integrally closed**. Every multiplication map from tensor powers of $H^0(X,L)$ onto $H^0(X,L^k)$ is surjective. This does not claim that $L$ embeds $X$ when $b=0$: in that case $E$ is contracted.

The *all-degree* Hilbert function and Hilbert series are
\[
\boxed{h^0(X,L^k)= (ck+1)(bk+1)+\frac{ck(ck+1)}2
=\frac{a^2-b^2}{2}k^2+\frac{3a-b}{2}k+1,}
\]
\[
\boxed{\sum_{k\ge0}h^0(X,L^k)t^k
=\frac{1+(A+B-2)t+(A-B+1)t^2}{(1-t)^3},\quad
A=\frac{a^2-b^2}{2},\ B=\frac{3a-b}{2}.}
\]
When $a>b$, the Okounkov body is the **trapezoid**
\[
\Delta(L)=\{(x,y):0\le x\le c,\ 0\le y\le b+x\},
\quad \operatorname{Area}\Delta(L)=bc+\frac{c^2}{2}=\frac{a^2-b^2}{2}.
\]
When $a=b>0$, the body is a one-dimensional segment with degree-$k$ count $ak+1$, so the *intrinsic* dimension is one and the ambient two-dimensional area vanishes.

The exact probability distribution of the first exceptional valuation among the one-dimensional valuation leaves (equivalently the natural monomial basis) is
\[
\mu_k=\frac1{h^0(X,L^k)}\sum_{j=0}^{ck}(bk+j+1)\delta_{j/k}.
\]
For fixed $a>b$, it converges with **$O_{a,b}(k^{-1})$ error against 1-Lipschitz tests** to
\[
\mu_\infty(dx)=\frac{b+x}{bc+c^2/2}\mathbf1_{[0,c]}(x)\,dx.
\]
Its mean is $c(3b+2c)/[3(2b+c)]$. These are counting measures of flag valuations, **not** a distribution of randomly sampled sections under an unmentioned probability law.

## Direct proof

Choose homogeneous coordinates $[X:Y:Z]$ and let $x=X/Z,y=Y/Z$ near $p$. A section of $L^k$ corresponds to a homogeneous polynomial $F(X,Y,Z)$ of degree $ak$ whose dehomogenization $f(x,y)=F(x,y,1)$ has $\operatorname{ord}_p f\ge bk$. Indeed, on the point blowup chart $(x,y)=(u,uv)$, divisibility by $u^{bk}$ is necessary and sufficient to extend a section after twisting by $-bkE$; the other chart agrees. Conversely any such polynomial gives a regular section. The Hartogs passage used in Lemma 19.9.15 ensures no extra sections arise from the exceptional locus.

Write $f=\sum_{d\ge bk}f_d(x,y)$ with homogeneous pieces, and let $d$ be its least nonzero degree. Dividing the pullback section by its prescribed twist gives first flag valuation $j=d-bk$; the residual restriction to $E$ is exactly the homogeneous form $f_d$ of degree $bk+j$. Its vanishing at $q=[0:1]$ is $\ell\in[0,bk+j]$. Conversely, **every** allowed pair $(j,\ell)$ is realized by
\[
F_{k,j,\ell}=X^\ell Y^{bk+j-\ell}Z^{ck-j}.
\]
These monomials form a basis of $H^0(kL)$, and their valuations are all distinct. Consequently no spurious multiplicities occur in the semigroup-to-dimension identification. Multiplication of these monomials corresponds exactly to addition in $\Gamma$.

To prove degree-one generation constructively, given $0\le j\le ck$ choose integers $j_1,\ldots,j_k\in[0,c]$ summing to $j$. Since $\sum_i(b+j_i)=bk+j$, any $0\le\ell\le bk+j$ can be distributed into integers $0\le\ell_i\le b+j_i$ with sum $\ell$. Then $(k,j,\ell)=\sum_i(1,j_i,\ell_i)$ and the associated degree-one monomials multiply to $F_{k,j,\ell}$.

The semigroup is the set of integral points in the rational polyhedral cone defined by the nonnegative integer forms $k$, $j$, $ck-j$, $\ell$, $bk+j-\ell$. It is therefore saturated in its group. When $c>0$ this group is the entire $\mathbb Z^3$ (the degree-one differences yield the independent $j$- and $\ell$-directions); for $c=0$ it is the rank-two lattice $j=0$. One can independently verify **normality of its ring** without assuming a toric geometry theorem: inside the fraction field of the Laurent group algebra, $\mathbb C[\Gamma]$ is the intersection of the Laurent polynomial ring and the five monomial valuation rings defined by those linear forms. Membership of a Laurent polynomial in a monomial valuation ring means that every term has nonnegative weight (distinct monomials do not cancel in the associated graded ring). The Laurent polynomial ring and each valuation ring are integrally closed; hence so is their intersection.

For each $j$, exactly $bk+j+1$ monomials occur. Summing over $0\le j\le ck$ proves the Hilbert function and its rational generating series by the identities for $\sum k t^k$ and $\sum k^2t^k$. Scaling the semigroup gives the stated trapezoid; its area agrees exactly with the leading Hilbert coefficient and with $L^2/2$ in the big case. For the probability law, divide the weighted Riemann sum
$\sum_{j=0}^{ck}(bk+j+1)\phi(j/k)$ by $Ak^2+Bk+1$. After subtracting $\phi(0)$, a 1-Lipschitz $\phi$ is uniformly bounded by $c$ on the support, and the one-dimensional Riemann-sum error is $O_{a,b}(k)$; division gives the claimed $O(k^{-1})$ rate. The finite-degree mean is
\[
\frac{(bk+1)ck(ck+1)/2+ck(ck+1)(2ck+1)/6}
{k[(ck+1)(bk+1)+ck(ck+1)/2]},
\]
whose limit equals $c(3b+2c)/[3(2b+c)]$.

## Boundary, nonduplication and dependency ledger

This is **not a repeat** of POME-BLOWUP-EXCEPTIONAL-FLAG-OKO-001 (2026-10-29): that earlier proof concerns $aH+bE$ with a fixed exceptional component and a translated **triangle**, giving the same polynomial count as $aH$; the new moving $aH-bE$ imposes a vanishing-order constraint, produces a **trapezoid**, varies the Hilbert polynomial in $b$, and has a nonuniform first-coordinate limit. No earlier finding is resolved, superseded or reclassified.

Exact finite enumerations for $(a,b)=(2,1),(3,1),(5,2),(4,4),(3,0)$ and $k=1,\dots,4$ checked the claimed monomial counts against the closed polynomial and direct binomial formula. For $k\le3$ they also exhaustively checked degree-one Minkowski sums. These are elementary auxiliary checks, **not** project tests or formal verification.

**Classification:** low / verified conditional deduction, with fully explicit model proof. Lemma 19.9.15 and Theorems 19.9.9/16 are not refuted, but their general semigroup and analytic inputs are not independently certified. **Proposed action:** optional source-anchored worked example near §19.9.14–16, on a separate reviewable patch only. Potential dependents/checks: §19.9 intrinsic-lattice growth, §19.7 graded semigroups and §20 birational divisors; none is asserted verified by this example. Existing confirmed errors, proof gaps, external inputs and user-deferred entries are preserved. No Demailly approximation/regularization or its dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale or positivity-loss proof-completion work was entered.
