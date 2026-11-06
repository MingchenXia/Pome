# Chapter 19 mathematical audit: full-sequence convex slices and arbitrarily slow endpoint modulus (2026-11-07)

**Finding ID:** POME-OKO-SLICE-ENDPOINT-MODULUS-001  
**Classification:** low / **verified repair** of a proof presentation, with an independently proved sharpness example. **No false printed theorem.**  
**Production main actually reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **no production edits**.

## Integrated anchors and source identity

- Actual main reading edition: docs/sections/almost-semigroups/index.html, Git blob **33898b2963ad0f8b7e30bf414276642f60925b74**, physical lines **96–134** (Lemma **19.7.9**, original source label **sgpt:68EC4013**, permanent tag **806DFD35CCE5**).
- The convergence criterion to which its proof appeals is Theorem **19.7.6**, source **sgpt:3312EB21**, permanent **AFBD46E7C0A4**, physical lines **45–59**.
- The immediately relevant downstream proof is Theorem **19.7.14** (multiplicative Brunn–Minkowski), source **sgpt:7B965039**, permanent **72547EEEBFE4**, physical lines **198–208**; it requires positivity and continuity of interior slice volumes. Theorem **19.7.5**, source **sgpt:D4B8C3D6**, permanent **66339C0E3C21**, lines **38–42**, supplies volume continuity.
- The source attribution and original statement labels are historical provenance and should be retained.

## Exact statement and the logical point

Let $K\subset\mathbb R^n$ be nonempty compact convex with $n>0$, and set $a=\min_K x_1$, $b=\max_K x_1$. Every section
\[
K_t=\{y\in\mathbb R^{n-1}:(t,y)\in K\},\qquad a\le t\le b,
\]
is a nonempty compact convex set, and $t\mapsto K_t$ is Hausdorff continuous, including at $a,b$.

The integrated proof of Lemma 19.7.9, physical lines 119–130, describes the lower Kuratowski condition by finding approximating points **after replacing the parameter sequence by a subsequence**. The cited Theorem 19.7.6, lines 46–52, asks for approximating points along the **entire prescribed sequence**. This is a presentation-level omitted passage, not a counterexample: using the every-subsequence-has-a-subsubsequence criterion would also fix it, but the direct argument below avoids that additional topological conversion altogether.

## Complete elementary repair, including every endpoint and the whole sequence

If $a=b$, the parameter domain is a singleton and there is nothing to prove. Suppose $a<b$, fix $t_j\to t$ with $t_j\in[a,b]$, and choose $p^-=(a,v^-)\in K$, $p^+=(b,v^+)\in K$.

For **each fixed** $y\in K_t$, construct a point $(t_j,y_j)\in K$ for **every sufficiently large $j$** as follows:
\[
y_j=
\begin{cases}
\bigl(1-\frac{t_j-t}{b-t}\bigr)y+
  \frac{t_j-t}{b-t}v^+,&t_j>t\quad(t<b),\\[2mm]
y,&t_j=t,\\[2mm]
\bigl(1-\frac{t-t_j}{t-a}\bigr)y+
  \frac{t-t_j}{t-a}v^-,&t_j<t\quad(t>a).
\end{cases}
\]
The impossible sign is omitted when $t=a$ or $t=b$. Convexity gives $(t_j,y_j)\in K$ and the coefficients of $v^\pm$ tend to zero; hence $y_j\to y$ along the **full** sequence, even if $t_j-t$ changes sign infinitely often. This verifies Theorem 19.7.6(1) literally, not merely on a favorable subsequence. For its condition (2), if $t_{j_k}\to t$ and $y_{j_k}\in K_{t_{j_k}}$ converge to $y$, then $(t,y)\in K$ by closedness. The compactness of $K$ gives boundedness of the sections, and Theorem 19.7.6 now applies. Equivalently, a direct contradiction argument for either Hausdorff excess gives the same result. No regularization or compactness of an inverse limit is involved.

There is also an explicit **interior Lipschitz estimate** (not present in the printed statement). Put $D=\operatorname{diam}(K)$ and fix $t\in(a,b)$. Applying the same convex interpolation first from a point of $K_t$ toward the opposite extreme section, then from $K_s$ toward the other extreme, yields for **all** $s\in[a,b]$
\[
\boxed{d_{\mathrm{Haus}}(K_t,K_s)\le
\frac{D}{\min\{t-a,b-t\}}\,|s-t|.}
\]
For example, if $s>t$, the directed distance $K_t\to K_s$ is bounded by $D(s-t)/(b-t)$, and $K_s\to K_t$ by $D(s-t)/(s-a)\le D(s-t)/(t-a)$. The case $s<t$ is symmetric. This confirms the interior continuity invoked in the proof of Theorem 19.7.14; it does **not** yield a bound uniform as $t$ approaches $a$ or $b$.

## Sharp failure of *every* positive Hölder endpoint modulus

Already in $\mathbb R^2$, define for $0<x\le1$
\[
f(x)=\frac{1}{3-\log x},\qquad f(0)=0.
\]
Then
\[
f'(x)=\frac{1}{x(3-\log x)^2}>0,\qquad
f''(x)=\frac{2-(3-\log x)}{x^2(3-\log x)^3}<0.
\]
Thus $f$ is continuous, increasing and concave on $[0,1]$. The set
\[
K=\{(t,y):0\le t\le1,\quad |y|\le f(1-t)\}
\]
is a compact convex body with strictly positive area: convexity follows because $t\mapsto f(1-t)$ is concave, so both $y\le f(1-t)$ and $-y\le f(1-t)$ define convex constraints. Its terminal slice is $K_1=\{0\}$ and $K_{1-\delta}=[-f(\delta),f(\delta)]$. Consequently
\[
\boxed{d_{\mathrm{Haus}}(K_{1-\delta},K_1)
=\frac{1}{3+\log(1/\delta)}.}
\]
It tends to zero, as the printed lemma asserts. However, **for every** $\beta>0$,
\[
\lim_{\delta\downarrow0}
\frac{d_{\mathrm{Haus}}(K_{1-\delta},K_1)}{\delta^\beta}
=\lim_{\delta\downarrow0}
\frac{\delta^{-\beta}}{3+\log(1/\delta)}
=+\infty.
\]
In particular, Hausdorff continuity of convex slices does not imply *any* positive-power Hölder estimate at the endpoints, even for one fixed full-dimensional planar convex body. This is stronger than the square-root endpoint behavior of a round disk. The proof uses only direct differentiation, elementary convexity and intervals, with no external analytic input.

## Audit conclusion, proposal, and affected dependents

- **Status:** POME-OKO-SLICE-ENDPOINT-MODULUS-001 = low / verified repair; Lemma 19.7.9 is **correct**, not false. The only identified defect is that the displayed proof does not spell out passage from a favorable subsequence to the full sequence required by the cited Hausdorff criterion; the formula above closes this passage.
- **Proposed production patch (not applied):** insert the full-sequence two-sign convex interpolation, or explicitly justify the subsequence criterion. Keep the existing statement, source labels, permanent tags, numbering and historical attribution unchanged. Do **not** insert an unqualified endpoint Hölder estimate.
- **Affected dependent:** the expanded proof of Brunn–Minkowski (19.7.14) invokes slice continuity only in interior projection intervals; the repaired lemma provides this, in fact locally Lipschitz in the slice parameter. Neither Theorem 19.7.14 nor volume continuity (19.7.5) has been independently re-proved in this audit.
- **Coverage boundary:** this audit inspected only the selected integrated proof and adjacent statements at the pinned anchors. No whole-section certificate or general almost-semigroup counting/volume theorem verification follows. Project inventory baseline: **25 chapters, 747 numbered sections, zero fully certified mathematical sections**. Earlier confirmed errors/proof gaps/external dependencies remain untouched.
- **Explicitly deferred:** Demailly approximation/regularization and its dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof programme remain **deferred-by-user**, not resolved or reexamined.

This is a direct mathematical proof check, not a build, a software test, a formalization, or CI.
