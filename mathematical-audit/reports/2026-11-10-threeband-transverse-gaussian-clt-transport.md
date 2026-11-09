# Three-band kernel measures: transverse Gaussian CLT and sharp transport rate

Date: 2026-11-10. Finding: **POME-THREEBAND-TRANSVERSE-CLT-W1-001**. **Severity:** low. **Status:** verified conditional deduction (new quantitative consequence, not a correction of a false printed theorem).

## Exact reviewed source and scope

Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.

Reading-edition path: **docs/sections/partial-kernels-and-quotient-equilibrium--three-monomial-bands-from-a-multiplier-ideal-selection/index.html**; main blob **dec0c9cf53e927c039d6cf85c52c4da5d65c39cb**.

- Section 18.47, permanent tag **435C250083A1**, source label **non-kahler-pluripotential-theory:FCCA87E3**: physical lines 5–38, model and norms.
- Proposition 18.47.4, permanent tag **AD8335312F45**, source label **non-kahler-pluripotential-theory:79F7C192**: physical lines 155–200, especially the three-band index set (158), orthogonality (168), squared monomial norm (174–178), and Gaussian integral and estimates (170–191).
- Equation 18.47.5, permanent tag **CA62D9FD1FF2**, source label **non-kahler-pluripotential-theory:2B37019C**: physical lines 176–178.
- Equation 18.47.6, permanent tag **8DAD90BE35BE**, source label **non-kahler-pluripotential-theory:748138C6**: physical lines 181–191.
- Theorem 18.47.7, permanent tag **A0E408FAE124**, source label **non-kahler-pluripotential-theory:D3DDF8B8**: physical lines 205–220, especially the two normalized measure limits (212–220); proof's explicit Gaussian-measure identification and three Riemann sums at line 277.

This is the first selected proof-level audit of §18.47 in the coverage matrix (previously inventory-only). The present proof checks the finite-dimensional Gaussian/monomial component only. It does **not** undertake the owner-excluded Demailly regularization, dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion programme. The terminology "kernel measure" refers only to the **explicitly printed finite monomial model**.

## Claim

Work in the printed logarithmic coordinates $x_j=\log |z_j|^2$ on $K=[-1,2]^2\times(S^1)^2$, with Haar probability measures $\mathrm d\tau_1,\mathrm d\tau_2$ on the angles. For $m\ge1$, let

\[
\mathcal A_m=\{(a,b)\in\{0,\ldots,m\}^2:|a-b|\le1\},\qquad N_m=3m+1,
\]
\[
q_{m,t}(\mathrm dx)=
\frac{\mathbf1_{[-1,2]}(x)e^{-m(x-t)^2/2}}{J_m(t)}\,\mathrm dx,\qquad
J_m(t)=\int_{-1}^2e^{-m(x-t)^2/2}\,\mathrm dx.
\]

Let $\Pi_m=N_m^{-1}B_m\nu$ be exactly the probability measure of Theorem 18.47.7. Let $\Pi$ be the diagonal-shell probability obtained by taking $t$ uniformly in $[0,1]$, setting $x_1=x_2=t$, and independently taking both angles Haar, i.e. the printed $\mu$.

**(A) Exact decomposition and transverse CLT.** One has

\[
\Pi_m=\frac1{3m+1}\sum_{(a,b)\in\mathcal A_m}
q_{m,a/m}\otimes q_{m,b/m}\otimes\mathrm{Haar}\otimes\mathrm{Haar}.
\tag{1}
\]

The pushforward of $\Pi_m$ under $T_m=\sqrt m(x_1-x_2)$ converges weakly to $N(0,2)$. For every real 1-Lipschitz bounded test function $F$ on $\mathbb R$,

\[
\left|\int F(T_m)\,\mathrm d\Pi_m-\int F\,\mathrm dN(0,2)\right|
\le m^{-1/2}+C\|F\|_\infty m^{-1/2}e^{-m/2}.
\tag{2}
\]

Moreover, the first absolute transverse moment has the **exact leading constant**

\[
\int|x_1-x_2|\,\mathrm d\Pi_m
=\frac2{\sqrt{\pi m}}+O(m^{-1}).
\tag{3}
\]

**(B) Sharp quantitative weak convergence.** Give $K$ the product metric whose logarithmic-coordinate factor is the standard Euclidean metric and whose angle factors are their usual circle metrics. For the associated Wasserstein-1 distance,

\[
\sqrt{\frac2{\pi m}}-O(m^{-1})
\ \le\ W_1(\Pi_m,\Pi)\ \le\ C m^{-1/2}.
\tag{4}
\]

Thus the qualitative limit $\Pi_m\rightharpoonup\Pi$ in the printed theorem has the optimal **order** $m^{-1/2}$ in this natural metric. In particular, for every Lipschitz test $f$ on $K$, the convergence error is at most $C\,\mathrm{Lip}(f)m^{-1/2}$, with the order unimprovable uniformly over 1-Lipschitz tests. This does **not** assert that all fixed smooth tests have a matching lower bound.

## Proof

**1. Recompute the exact probability law from the displayed squared norms.** The printed monomial with indices $(a,b)$ has squared norm $A_m(a,b)=I_m(a/m)I_m(b/m)/9$ (Equation 18.47.5), where $I_m(t)=e^{mt^2/2}J_m(t)$ (lines 168–178). On the torus, dividing the weighted squared monomial by this exact norm cancels the factor $1/9$ in $\nu$, while completing the square in each logarithmic coordinate gives $q_{m,a/m}$ and $q_{m,b/m}$. The angles remain independent Haar because the squared modulus is radial. Orthogonality follows by integrating the distinct angular characters. The three index bands contain $m+1,m,m$ elements, respectively, proving (1) without an asymptotic approximation. This checks the normalization $\int\Pi_m=1$ and the printed factor $N_m=3m+1$.

**2. Control of truncation uniformly over the moving centers.** For $0\le t\le1$, the interval $[-1,2]$ contains $[t-1,t+1]$. If $G_{m,t}$ denotes the full normal distribution $N(t,1/m)$, a Gaussian tail bound gives

\[
G_{m,t}(\mathbb R\setminus[-1,2])
\le \frac{2e^{-m/2}}{\sqrt{2\pi m}}.
\]

Since $q_{m,t}$ is exactly $G_{m,t}$ conditioned to the interval, its total-variation distance from $G_{m,t}$ is at most that tail probability (using $\sup_A|\mu(A)-\nu(A)|$). The product of two such conditioned laws differs from the product of their full Gaussians in total variation by at most the sum of the two tail probabilities. All bounds are independent of $a,b,m$.

**3. Transverse CLT with rate.** Under the untruncated product law for $(a,b)$, let $Z_1,Z_2$ be independent $N(0,1)$ variables. Then

\[
\sqrt m(x_1-x_2)=Z_1-Z_2+\frac{a-b}{\sqrt m}.
\]

Here $Z_1-Z_2\sim N(0,2)$ and $|a-b|\le1$. The translation bound for 1-Lipschitz $F$ is $m^{-1/2}\mathrm{Lip}(F)$; Step 2 bounds the effect of truncation for bounded tests by $C\|F\|_\infty m^{-1/2}e^{-m/2}$. Averaging across all bands gives (2), hence the CLT, without interchanging uncontrolled limits.

For the first moment, $\mathbb E|Z_1-Z_2|=2/\sqrt\pi$. The reverse triangle inequality gives
\[
\left|\mathbb E\left|Z_1-Z_2+\frac{a-b}{\sqrt m}\right|-\frac2{\sqrt\pi}\right|
\le m^{-1/2}.
\]
To transfer this *unbounded* test from the full to the conditioned law one must not merely invoke total variation. Instead, with $A$ the event that both Gaussian variables lie in $[-1,2]$, apply Cauchy–Schwarz to $|x_1-x_2|\mathbf1_{A^c}$ and use
$\mathbb E|x_1-x_2|^2=2/m+(a-b)^2/m^2\le3/m$ and the exponential tail bound. The conditional expectation changes by $o(m^{-1})$ uniformly for these centers. After dividing by $\sqrt m$, this gives (3), with a uniform $O(m^{-1})$ remainder and no missing boundary contribution.

**4. Wasserstein upper bound.** Let $Q_m$ be the discrete measure obtained from (1) by replacing each Gaussian factor by its central Dirac mass $\delta_{a/m}\otimes\delta_{b/m}$ and retaining both Haar angles. The printed lower estimate $J_m(t)\ge c/\sqrt m$, $c=\int_{-1}^1e^{-y^2/2}\,\mathrm dy$, gives

\[
\mathbb E_{q_{m,t}}|x-t|
\le \frac{2/m}{c/\sqrt m}=\frac2{c\sqrt m}.
\]

Couple each factor to its center and the angles identically; therefore $W_1(\Pi_m,Q_m)\le4/(c\sqrt m)$.

The pushforward of $Q_m$ onto logarithmic coordinates is the sum of diagonal points $(j/m,j/m)$ for $0\le j\le m$ and off-diagonal points $((j+1)/m,j/m)$ and $(j/m,(j+1)/m)$ for $0\le j<m$, all with weight $1/(3m+1)$. Replacing the off-diagonal points by $(j/m,j/m)$ costs $O(1/m)$, and the resulting diagonal empirical measure differs from uniform diagonal $t\in[0,1]$ in $W_1$ by $O(1/m)$ via the usual equal-interval coupling, with the extra endpoint point having weight $1/(3m+1)$. Thus $W_1(Q_m,\Pi)\le C'/m$. The triangle inequality gives the upper bound in (4).

**5. Matching lower bound.** The function
\[
f(x_1,x_2,\tau_1,\tau_2)=\frac{|x_1-x_2|}{\sqrt2}
\]
is 1-Lipschitz in the stated product metric and satisfies $f=0$ $\Pi$-almost everywhere. By Kantorovich duality and (3),
\[
W_1(\Pi_m,\Pi)\ge\int f\,\mathrm d\Pi_m
=\sqrt{\frac2{\pi m}}+O(m^{-1}).
\]
This is a sharp-order lower bound; no exact leading constant for $W_1$ itself is asserted.

## Mathematical judgement, status, and affected dependencies

**No false printed theorem is established.** The checked normalization and finite-dimensional concentration steps of Proposition 18.47.4 and Theorem 18.47.7 are correct. This is an **additive quantitative deduction**, not a proof repair. The only inherited analytic input is the printed selection by multiplier ideals in Lemma 18.47.1 and the identification of the sections: their full upstream proof chains have **not** been certified. In particular, the present computation does not independently prove the global envelope, non-pluripolar product, or geometric-current statements in §18.47.

Affected dependents are the interpretation of the **normalized measure limit** in Theorem 18.47.7 and comparisons of finite-level kernels with its shell probability. The rate does not automatically transfer to unnormalized measures, arbitrary weighted kernel families, or unrelated choices of a background metric.

**Proposed source change (not applied):** Add an optional remark after the measure-convergence proof in Theorem 18.47.7 stating the transverse $N(0,2)$ CLT, moment constant $2/\sqrt\pi$, and sharp $W_1\asymp m^{-1/2}$ for the logarithmic-coordinate metric. Retain the printed theorem, permanent labels, original historical attribution and all earlier distinct variants.

**Coverage:** first selected mathematical proof inspection of §18.47 (1 newly visited numbered section, 0 entirely certified sections); §18.30 only definition-context, not newly verified. Actual existing inventory: 25 chapters and 747 numbered sections. Owner-deferred regularization/Bergman/L2/OT/multiscale/positivity-loss findings remain **deferred-by-user**, neither resolved nor certified. This report records no project tests, build, CI, formal verification or publication.
