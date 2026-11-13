# Sharp transport convergence of cube-averaged Bedford--Taylor dominated measures

- **Stable finding ID:** \`POME-BT-CUBE-HISTOGRAM-TRANSPORT-001\`.
- **Date:** 2026-11-14.
- **Classification:** **low / verified conditional deduction**; **no false theorem and no proof defect confirmed**. This is an additional quantitative consequence of the hypotheses of Proposition 7.11.5, not a complete certification of that proposition's upstream analytic inputs.
- **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Integrated reading-edition file:** \`docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html\`; Git blob \`e619f7aa95f80ce11aa676193b054db3180e59d4\`.
- **Original statement:** Proposition **7.11.5**, source \`foundations-of-pluripotential-theory:3263E506\`, permanent tag \`1151DF7B32E4\`, physical HTML **lines 98--131**, especially the cube construction at **99--103**. The corresponding proof is at **133--177**, especially compact support **136**, weak convergence **138--144**, local psh bound **146--152**, dominated energy **154--168**, and global $L^1$ compactness **170--176**.
- **Related original inputs (hypotheses only):** Theorem **7.11.2**, source \`foundations-of-pluripotential-theory:C2BB479D\`, permanent tag \`05F71889C324\`, **lines 25--91**; local inequality (7.11.6), source \`foundations-of-pluripotential-theory:C88407F2\` / permanent \`CC0546ABBCE7\`, **lines 109--117**, and the energy control (7.11.7), source \`foundations-of-pluripotential-theory:364DF017\` / permanent \`00E17178E4CB\`, **lines 119--124**.
- **Scope:** Bedford--Taylor/local Monge--Ampère measures and elementary optimal transport. No Demailly regularization, Bergman, weighted L2, Ohsawa--Takegoshi, multiscale atlas, or positivity-loss work.

## Statements and precise quantifiers

Let $B\subset\mathbb C^n$, $d=2n$, and let $\mu$ be a finite measure supported on a compact set $K\Subset B$, with mass $m>0$. For each *arbitrarily translated*, axis-aligned half-open cubic partition $\mathcal Q_j$ of $\mathbb R^d$ of side $h_j\downarrow0$, form the histogram measure from Proposition 7.11.5:
\[
\mu_j=\sum_{Q\in\mathcal Q_j}\frac{\mu(Q)}{h_j^d}\mathbf1_Q\,dx.
\]
For $j$ large enough, both measures are compactly supported inside $B$. Write $P=\mu/m$, $P_j=\mu_j/m$. Then
\[
\boxed{W_2(P,P_j)^2\le \frac{d}{3}h_j^2
=\frac{2n}{3}h_j^2,\qquad
W_\infty(P,P_j)\le\sqrt d\,h_j.}
\]
Consequently $W_q(P,P_j)\le\sqrt d\,h_j$ for every finite $q\ge1$, in particular convergence holds in each $W_q$ rather than merely weakly. The **universal coefficient $\sqrt{d/3}$ for $W_2/h_j$ is optimal** over the allowed class when the dominating bounded psh function may vary with $\mu$.

If in addition $\mu=f\,dx$ with nonnegative $f\in W^{1,1}_c(\mathbb R^d)$, then
\[
\boxed{ W_1(P,P_j)\le
 \frac{\sqrt d\,h_j^2}{m}
 \sum_{i=1}^d\|\partial_i f\|_{L^1(\mathbb R^d)}.}
\]
The order $h_j^2$ cannot be improved for all fixed *smooth, nonnegative compactly supported densities*, even if $\mu\le(dd^cw)^n$ for a smooth bounded psh $w$ on $B$. Neither the stronger Sobolev assumption nor this rate is asserted for an arbitrary Bedford--Taylor-dominated measure.

## Direct coupling and sharp $W_2$ constant

For each cube $Q$ let $U_Q$ denote normalized Lebesgue measure on $Q$. Set
\[
\pi_j(dx\,dy)=\frac1m\sum_{Q\in\mathcal Q_j}
  \mathbf1_Q(x)\,\mu(dx)\,U_Q(dy).
\]
This is a coupling of $P$ and $P_j$, with no need for nested grids or any convergence of partitions. Let $c_Q$ be the center of $Q$. A uniform point $Y$ in $Q$ satisfies
\[
\mathbb E(|Y-x|^2)=|x-c_Q|^2+\frac{d h_j^2}{12}
\le\frac{d h_j^2}{4}+\frac{d h_j^2}{12}
=\frac{d h_j^2}{3}\quad(x\in Q).
\]
Integrate over the coupling to prove the displayed $W_2$ bound. The support of $\pi_j$ is contained in $\{|x-y|\le\sqrt d\,h_j\}$, proving the $W_\infty$ and all $W_q$ assertions.

For optimality fix one cube $Q\Subset B$ and one of its vertices $v$. Choose nonnegative smooth unit-mass densities $f_\epsilon$ supported in smaller and smaller balls *inside $Q$* converging to $v$. Each $\mu_\epsilon=f_\epsilon dx$ is a case of the original proposition: choosing a sufficiently large constant $C_\epsilon$ gives $\mu_\epsilon\le(dd^c(C_\epsilon|z|^2))^n$, and the potential is smooth bounded psh on the fixed ball $B$. Its histogram on this grid is exactly $U_Q$. Hence
\[
W_2(\mu_\epsilon,U_Q)\longrightarrow
W_2(\delta_v,U_Q)
=\left(\int_Q |y-v|^2\,U_Q(dy)\right)^{1/2}
=h_j\sqrt{d/3}.
\]
This establishes sharpness **uniformly over the allowed class**, not for a fixed bounded oscillation of $w$ nor for a single fixed measure as $h_j\to0$.

## An independent smooth-density improvement, with sharp order

The dual formula for probability-measure $W_1$ tests against real 1-Lipschitz $g$. On each cube, both $f-\bar f_Q$ and $g-\bar g_Q$ have zero mean, and
\[
\int_Q g(f-\bar f_Q)
=\int_Q(g-\bar g_Q)(f-\bar f_Q).
\]
Since $\sup_Q|g-\bar g_Q|\le\sqrt d\,h_j$ and the coordinatewise $L^1$ Poincare estimate obtained by successively averaging one variable at a time reads
\[
\int_Q|f-\bar f_Q|\,dx
\le h_j\sum_{i=1}^{d}\int_Q|\partial_i f|\,dx,
\]
we obtain, on summing over the partition,
\[
\left|\int_{\mathbb R^d}g\,d(P-P_j)\right|
\le\frac{\sqrt d\,h_j^2}{m}
\sum_{i=1}^d\|\partial_i f\|_1.
\]
Approximation gives the same formula for Sobolev, not only $C^1$, densities.

To see that the exponent two is sharp even for *one fixed smooth measure*, take $h_j=1/j$ and a nonnegative $f_1\in C_c^\infty(\mathbb R)$ equal to $a+x$ on a fixed interval $I$ (choose $a$ so it stays strictly positive there). Let $f(x)=f_1(x_1)\prod_{i=2}^d f_i(x_i)$ with nonnegative nonzero compactly supported smooth $f_i$. Choose $B$ large enough to contain the support. Under projection to the first coordinate (a 1-Lipschitz map), the histogram is exactly the one-dimensional histogram of the $f_1$ marginal. On each grid interval $[b,b+h_j]\subset I$, the cumulative signed mass difference equals
\[
\int_b^{b+t}\bigl[(a+x)-(a+b+h_j/2)\bigr]\,dx
=\tfrac12(t^2-h_jt),\qquad 0\le t\le h_j.
\]
Its absolute integral is $h_j^3/12$. Since the cumulative difference vanishes at every grid boundary, the one-dimensional $W_1$ is the sum of these nonnegative cell contributions. At least $c/h_j$ cells lie in $I$, so the normalized $W_1$ is bounded below by $c' h_j^2$ as $j\to\infty$. Projection makes this a lower bound in dimension $d$ as well. The smooth density is bounded, so a single sufficiently large $C$ makes $\mu=f\,dx\le(dd^c(C|z|^2))^n$ on $B$, with $C$ **fixed** for this example. This also checks the original proposition's compact-support and bounded-psh domination requirements.

## Logical audit and dependent steps

The printed proof's cube geometry, uniform-continuity weak limit, local psh estimate, transfer of energy, and $L^1$ compactness arguments were inspected at the precise lines above. No error was found in these passages. The new coupling is entirely independent of the analytic estimate in Theorem 7.11.2 and does **not** certify the cited Błocki inequality (Proposition 7.4.5), the Dirichlet existence Theorem 7.10.2, or the full subsequent Theorem 7.11.30. In particular, **ordinary $W_q$ convergence of the measures must not be substituted for capacity convergence of their solutions**; that requires independent nonlinear estimates. This is a quantitative supplement, not a proof of the complete dependency chain.

**Proposed correction:** optional nonintrusive note after Proposition 7.11.5(1), stating the normalized Wasserstein bounds with explicit $m>0$ and the Sobolev-density improvement as an extra hypothesis. Any production-text amendment must go through a separate reviewable PR. There is no change to canonicalization, provenance, numbering, or tags. Historical attribution to Cegrell and the named analytic inputs is retained.
