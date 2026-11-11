# Nef perturbation volumes: effective logarithmic slope and its variance (2026-11-11)

**Stable finding:** `POME-GAUD-NEF-LOGSLOPE-VARIANCE-001`.  
**Severity/status:** low / **verified conditional deduction**; no printed theorem is false, no repair is certified or required.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Primary integrated edition:** `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html`, blob `a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0`. Section tag `3567ADAA7365`; Proposition 12.20.2, source `non-kahler-pluripotential-theory:03644B93`, permanent tag `883742E77C19`, physical lines **78–101**; Proposition 12.20.1, source `:895EF015`, permanent tag `EBFCF76A5A51`, lines **19–70**; comparison and closed-nef discussion lines **7–16, 75–76**.  
**Crosschecked dependency:** `docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html`, blob `086d12a65c46cfb68c7d6fe952266515ca04623b`, Theorem 12.11.1, source `non-kahler-pluripotential-theory:F03E2CAC`, permanent tag `9ECB2B21B601`, lines **10–38** (especially closed-nef formula lines 32–38). The general smooth-equation/existence and Gauduchon quotient inputs are **not independently certified** here.

## The exact new statement

Let `X` be a connected compact Kähler manifold of complex dimension `n>=2`. Let `theta` be a *smooth closed real (1,1)* representative of a nef cohomology class (the representative need not be semipositive), and let `h` be a Kähler form. Let `mu` be any smooth strictly positive probability volume form. For `epsilon>0` put
\[
 L(\epsilon)=\lambda_\mu(\theta+\epsilon h),\qquad
 P(\epsilon)=\int_X(\theta+\epsilon h)^n.
\]
By the **printed, conditional** closed-nef identity, `L(epsilon)=P(epsilon)^(1/n)>0`. Set
\[
 c_j=\binom nj\int_X\theta^{n-j}\wedge h^j\geq0
 \quad(0\leq j\leq n),\qquad
 c_n=\int_Xh^n>0.
\]
All coefficients are nonnegative by nefness, as justified in Proposition 12.20.2. Define the normalized weights
\[
 w_j(\epsilon)=\frac{c_j\epsilon^j}{P(\epsilon)},\qquad
 \sum_{j=0}^n w_j(\epsilon)=1.
\]

The **effective logarithmic slope** of the *normalization root* is
\[
 q(\epsilon):=\frac{d\log L(\epsilon)}{d\log\epsilon}
 =\frac1n\sum_{j=0}^n j\,w_j(\epsilon).
 \tag{1}
\]
Its derivative is exactly a variance:
\[
 \boxed{\quad
 \frac{dq}{d\log\epsilon}
 =\frac1n\left(\sum_j j^2w_j-
 \left(\sum_j jw_j\right)^2\right)
 =\frac{\operatorname{Var}_{w(\epsilon)}(j)}n\geq0.
 \quad}\tag{2}
\]
It is **strictly** positive for every positive epsilon precisely when at least two `c_j` are nonzero; if only one coefficient is nonzero, `q` is constant. Hence the local effective exponent is monotone **throughout the full positive perturbation ray**, not merely asymptotic as epsilon tends to zero.

Put
\[
 r=\max\{k:\int_X\theta^k\wedge h^{n-k}>0\}
 \in\{0,\ldots,n\},
\]
the numerical dimension from the printed Proposition 12.20.2. The least nonzero `j` is `j_0=n-r`. Therefore
\[
 \frac{n-r}{n}\leq q(\epsilon)\leq1,\qquad
 \lim_{\epsilon\downarrow0}q(\epsilon)=\frac{n-r}{n},
 \qquad\lim_{\epsilon\to\infty}q(\epsilon)=1.
 \tag{3}
\]
For `0<epsilon<eta`, integrating (3) gives the **global two-sided distortion**
\[
 \boxed{\quad
 \frac\epsilon\eta
 \leq\frac{L(\epsilon)}{L(\eta)}
 \leq\left(\frac\epsilon\eta\right)^{(n-r)/n}.
 \quad}\tag{4}
\]
These inequalities also apply when `r=n` (with the right side equal to 1), or `r=0` (both bounds equal).

If `r<n`, then, writing `C_r=c_{n-r}^{1/n}>0`,
\[
 L(\epsilon)
 = C_r\epsilon^{(n-r)/n}(1+O(\epsilon)),\quad
 L'(\epsilon)
 =\frac{n-r}{n}C_r\epsilon^{-r/n}(1+O(\epsilon)).
 \tag{5}
\]
For `1<=r<n`, the optimal local Hölder exponent of `L` at zero is **exactly** `(n-r)/n`, and the right derivative blows up. In contrast `r=0` yields exact linearity, and `r=n` yields a positive endpoint value and a locally Lipschitz root.

For **every** such fixed nef class, `L` is Hölder-`1/n` on `[0,1]`:
\[
 |L(\epsilon)-L(\eta)|
 \leq\left(\sum_{j=1}^n j c_j\right)^{1/n}
 |\epsilon-\eta|^{1/n},\quad
 \epsilon,\eta\in[0,1].
 \tag{6}
\]
The dimension-only exponent `1/n` cannot be increased uniformly across all closed nef classes with positive numerical dimension.

## Proof, with no excluded regularization step

The printed closed-nef formula gives the polynomial `P(epsilon)=sum c_j epsilon^j`. Differentiating with `t=log epsilon` yields `d log P/dt=sum j w_j`; dividing by `n` gives (1). Direct differentiation of the rational weights yields
\[
 \frac{dw_j}{dt}=w_j\left(j-\sum_k k w_k\right).
\]
Substitution into (1) gives (2), including the equality case: with positive epsilon, `w_j>0` iff `c_j>0`; the variance vanishes iff all positive indices coincide. Since `c_n>0`, the highest possible index is `n`, and by numerical dimension the lowest is `n-r`. Concentration of weights at the extreme index proves the limits (3); the support bound gives the middle inequalities at every epsilon. Integrating `q(t)` on `[log epsilon,log eta]` and exponentiating (taking care that `epsilon/eta<1`) proves (4).

For `r<n`, factor
\[
 P(\epsilon)=c_{n-r}\epsilon^{n-r}
 \left(1+\sum_{j>n-r}\frac{c_j}{c_{n-r}}
 \epsilon^{j-(n-r)}\right).
\]
Taking the positive `n`th root and differentiating establishes both asymptotics in (5); a positive leading coefficient makes all remainders uniform near zero. Thus no Hölder exponent greater than `(n-r)/n` is possible for that fixed class, and `L'` diverges when `r>0`. At `r=0` the polynomial is exactly `c_n epsilon^n`; at `r=n` it has strictly positive constant term and its root is smooth near zero.

For (6), all `c_j` are nonnegative, and for `0<=epsilon<=eta<=1`,
\[
 0\leq P(\eta)-P(\epsilon)
 =\sum_{j=1}^nc_j(\eta^j-\epsilon^j)
 \leq(\eta-\epsilon)\sum_{j=1}^njc_j
\]
Hence the Lipschitz constant of `P` on `[0,1]` is `sum j c_j`. Using the elementary inequality `a^(1/n)-b^(1/n) <= (a-b)^(1/n)` for `a>=b>=0` proves (6) with the displayed constant. 
## Exact sharp family

For `1<=r<n`, choose `X=P^r x P^{n-r}` and let
`alpha=pr_1^*omega_FS`, `beta=pr_2^*omega_FS`, `theta=alpha`, `h=alpha+beta`. Their forms are closed, `theta` is semipositive nef of numerical dimension `r`, and `h` is Kähler. Put `C=int_X alpha^r beta^{n-r}>0`. A degree count in the exterior algebra gives exactly
\[
 P(\epsilon)=\binom nr C(1+\epsilon)^r\epsilon^{n-r},
\quad
 L(\epsilon)=(\binom nr C)^{1/n}
 (1+\epsilon)^{r/n}\epsilon^{(n-r)/n}.
\]
Consequently
\[
 q(\epsilon)=\frac{n-r}{n}
 +\frac rn\frac\epsilon{1+\epsilon},\qquad
 \frac{dq}{d\log\epsilon}
 =\frac rn\frac\epsilon{(1+\epsilon)^2}>0.
\]
For `r=n-1` this proves the universal `1/n` boundary Hölder exponent in (6) is sharp. The model also distinguishes the *volume* order `n-r` already printed in §12.20 from the **root normalization** order `(n-r)/n` and its monotone moving exponent.

## Audit classification, dependencies and precise coverage

- **Verified conditional deduction / low:** the variance identity (2), global slope bounds (4), derivative and Hölder statements (5)–(6), with explicit sharp models, are newly checked corollaries. The **printed** Propositions 12.20.1/.2 and Theorem 12.11.1 are **not refuted**. This is not an independent proof of Gauduchon quotient duality or Monge–Ampère smooth existence.
- **Do not mistake this for the previously printed polynomial order:** §12.20.2 already proves `P(epsilon) ~ epsilon^(n-r)`. The new material is the **full-ray variance monotonicity for the effective exponent**, sharp two-parameter root distortion, and explicit optimal Hölder and derivative bounds. No old degeneration order is relabeled as a fresh discovery.
- **Proposed correction/placement:** add an *optional new remark* following Proposition 12.20.2 stating (1)–(4) and (6) with the `j` factor. There is **no necessary correction** to the printed result, and no direct source or production edit. Preserve historical attribution and original/permanent labels.
- **Affected dependents:** `12.11.1` (closed-nef formula), `12.20.1–2` (order and perturbation invariance); optional quantitative interpretation in the Gauduchon boundary discussions of §§12.21–12.25. Their independent proof chains remain conditional.
- **Coverage:** new proof-level calculation within previously partially audited §12.20; selected §12.11.1 statement and closed-nef step as prerequisite only. **0 first-visited numbered sections; 0 entire sections certified.** Actual current ToC: **25 chapters, 747 sections**.
- **Explicit exclusion:** no Demailly approximation/regularization, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale atlas/positivity-loss programme. All earlier such notes stay **deferred-by-user**, not resolved or certified. No builds, tests, CI, formalization, site deployment, source or main changes claimed.
