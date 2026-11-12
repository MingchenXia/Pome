# Exact cutoff normalization and large-time recovery for ideal-envelope test curves

**Audit date:** 2026-11-13.
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Stable finding ID:** \`POME-ENVSYS-CUTOFF-LEGENDRE-RECOVERY-001\`.
**Severity / status:** **low / verified conditional deduction**. The printed Definition 16.29.2 and Proposition 16.29.3 are **not** false. This is a new consequence of their hypotheses, conditional only on the stated internal normalization/upper-envelope facts, and **not** a certification of the full section or of its multiplier-ideal dependency chain.

## Precisely reviewed integrated source

- \`docs/sections/envelope-systems-over-hermitian-perturbations/index.html\`, main blob \`856e240bbc5c86058ff861873f11e87db021e1bd\`; section permanent tag \`4AD4DDD929EE\`, original label \`non-kahler-pluripotential-theory:D633A6C5\`.
- **Definition 16.29.2**, original \`non-kahler-pluripotential-theory:DC46E61D\`, permanent \`F0A985779829\`, physical HTML lines **24–47** (left constancy, pointwise concavity/decrease, cutoff and fixedness).
- **Proposition 16.29.3**, original \`non-kahler-pluripotential-theory:C6135113\`, permanent \`160B15BF08FE\`, physical lines **51–66** (regularized Legendre transform and bounds).
- Independent scope crosscheck: \`docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html\`, main blob \`f1979b73c857f4874dd4a5cb10b93bcc047ebbdc\`, **Theorem 18.4.2**, original \`non-kahler-pluripotential-theory:3A211D73\`, permanent \`7F20FD198864\`, physical lines **22–29** and normalization argument **45–46**.
- We use the standard local upper-envelope fact that a locally bounded-above supremum of PSH functions equals its usc regularization outside a pluripolar set. The rest is elementary and needs no projective regularization.

## Claim (stronger than the printed inequalities)

Let \(X\) be compact, let \(\theta\) be a smooth real \((1,1)\)-form, let \(a<c\), and let \(\Gamma\in\mathscr T_{a,c}(\theta)\) be as in Definition 16.29.2. Assume the printed normalization \(\sup_X\Gamma_\tau=0\) for every \(\tau<c\). Put \(\varphi=\Gamma_a\), \(\Gamma_c=\lim_{\tau\uparrow c}\Gamma_\tau\), and
\[
 U_t=\left(\sup_{\tau<c}(\Gamma_\tau+t\tau)\right)^*,\qquad t>0.
\]
Then:

1. The **common zero set** is nonempty and is exactly the zero set of the cutoff:
   \[
       \varnothing\ne Z:=\bigcap_{\tau<c}\{x:\Gamma_\tau(x)=0\}
          =\{x:\Gamma_c(x)=0\}.
   \]
   In particular \(\sup_X\Gamma_c=0\), a strengthening of the printed assertion that \(\Gamma_c\not\equiv-\infty\).
2. **The global upper slope is attained at every point of \(Z\), for all \(t>0\)**:
   \[
       U_t(x)=ct\quad (x\in Z),\qquad \boxed{\sup_X U_t=ct}.
   \]
   No optimizer \(\tau<c\) for the Legendre supremum is asserted; indeed in the constant curve \(\Gamma_\tau=\varphi\), the supremum \(ct\) at \(Z\) is **not attained by any \(\tau<c\)**.
3. The full cutoff potential is recovered, not merely its normalization:
   \[
           \boxed{U_t-ct\ \downarrow\ \Gamma_c\quad
              \text{pointwise on }X\ \text{as }t\to+\infty.}
   \]
   The limit is a limit of **decreasing** \(\theta\)-PSH functions; no sequential compactness of an arbitrary net or interchange of upper semicontinuous regularization and an increasing limit is assumed.

## Proof

**Common zero set.** Every \(\Gamma_\tau\) is upper semicontinuous and \(\Gamma_\tau\le0\) with \(\sup_X\Gamma_\tau=0\). Compactness makes its zero set \(Z_\tau\) nonempty and compact. If \(s<t<c\), monotonicity gives \(\Gamma_s\ge\Gamma_t\), so \(Z_t\subset Z_s\). Thus the family \(Z_\tau\) has the finite-intersection property and its intersection \(Z\) is nonempty. At \(x\in Z\), \(\Gamma_c(x)=\inf_{\tau<c}\Gamma_\tau(x)=0\). Conversely, \(\Gamma_c(x)=0\) and \(\Gamma_\tau(x)\ge\Gamma_c(x)\) together with \(\Gamma_\tau(x)\le0\) imply \(x\in Z\).

**Exact maximal slope.** The printed upper bound \(U_t\le\varphi+ct\) and \(\varphi\le0\) give \(U_t\le ct\). At \(x\in Z\), the unregularized expression is
\[
 \sup_{\tau<c}(\Gamma_\tau(x)+t\tau)
    =\sup_{\tau<c}t\tau=ct.
\]
Regularization can only increase the supremum, while the printed upper bound still applies, so \(U_t(x)=ct\). The constant-family example demonstrates why \(\sup\) must not be replaced by \(\max\) at the excluded endpoint.

**Recovery before regularization.** Write
\[
 S_t(x)=\sup_{\tau<c}\{\Gamma_\tau(x)-t(c-\tau)\},
 \qquad U_t-ct=S_t^*.
\]
For each \(x\), \(S_t(x)\ge\Gamma_c(x)\) by taking \(\tau\uparrow c\), while \(S_t\) decreases in \(t\). If \(\varphi(x)=-\infty\), all these expressions and \(\Gamma_c(x)\) are \(-\infty\). Otherwise \(\varphi(x)\) is finite and \(\Gamma_\tau(x)\le\varphi(x)\).

Suppose first \(\Gamma_c(x)>-\infty\). For \(t_j\to\infty\), select an approximate maximizing \(\tau_j<c\) with
\[
 S_{t_j}(x)\le \Gamma_{\tau_j}(x)-t_j(c-\tau_j)+1/j.
\]
Since \(S_{t_j}(x)\ge\Gamma_c(x)\), we get
\[
 0<c-\tau_j\le
  \frac{\varphi(x)-\Gamma_c(x)+1/j}{t_j}\longrightarrow0.
\]
Hence \(\Gamma_{\tau_j}(x)\to\Gamma_c(x)\), giving \(S_{t_j}(x)\to\Gamma_c(x)\). If \(\Gamma_c(x)=-\infty\) but \(S_{t_j}(x)\) were bounded below along an unbounded sequence of \(t_j\), the same approximate-maximizer argument would again force \(\tau_j\uparrow c\) while keeping \(\Gamma_{\tau_j}(x)\) bounded below, a contradiction. Thus in all cases
\[
 S_t(x)\downarrow\Gamma_c(x).
\]

**Passing through usc regularization without a false pointwise interchange.** Fix the integers \(t=j\ge1\). The family \(\{\Gamma_\tau+j(\tau-c):\tau<c\}\) is locally uniformly bounded above by \(\varphi\le0\); hence its supremum \(S_j\) and regularization \(S_j^*=U_j-cj\) agree off a pluripolar set \(P_j\). Their countable exceptional union \(P=\bigcup_jP_j\) is pluripolar. Therefore, off \(P\),
\[
      U_j-cj=S_j\longrightarrow\Gamma_c.
\]
The functions \(U_j-cj\) form a decreasing family of \(\theta\)-PSH functions, bounded below by the \(\theta\)-PSH function \(\Gamma_c\). Their limit is \(\theta\)-PSH (not identically \(-\infty\) because it is zero on \(Z\)), and agrees with \(\Gamma_c\) off a pluripolar set. Canonical PSH representatives are equal when they agree almost everywhere, so the limit equals \(\Gamma_c\) **at every point**. Since \(t\mapsto U_t-ct\) is decreasing, squeezing between consecutive integers gives the claimed full continuous-parameter limit.

## Implications, boundaries, and nonduplication

These identities sharpen the **maximum-value and cutoff-limit** information implicit in §16.29.2–3. They do not identify the maximal locus of \(U_t\) beyond the inclusion \(Z\subset\{U_t=ct\}\), and do not say any finite parameter maximizes the raw Legendre expression. They distinguish an actual **pointwise decreasing limit** from a naive exchange of supremum and usc regularization. The earlier §16.29 audit of projection and mass recovery is not repeated; this proof instead audits the left-normalization/cutoff mechanics of the original definition, including the previously unverified **Definition 16.29.2** and cutoff-limit step.

**Remaining conditional internal dependencies:** normalization of fixed ideal envelopes (Theorem 18.4.2), existence/PSH regularization of \(U_t\) (Theorem 17.17.5), the local PSH upper-envelope discrepancy theorem, and the fact that a decreasing nontrivial PSH limit is PSH. This is not a full proof of those results. Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remain **deferred-by-user**, unexamined and uncertified. No mathematical source, published section, registry, permanent tags, main branch, CI, or website edits are proposed or performed.
