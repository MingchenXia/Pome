# Correcting the finite concave-envelope left tail; weak closure versus total variation for polar curves

**Audit date:** 2026-10-29, Asia/Shanghai. **Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Initial audit branch:** <code>7770ae7966b315e6fb6bc8c9164bbfa356a1e997</code>. This report is a new selected direct proof audit, **not** a whole-section or whole-project mathematical certificate. No production, source, canonicalization, registry, tag, or site changes were made.

## Fresh integrated sources and precise scope

1. <code>docs/sections/non-archimedean-pluripotential-theory/index.html</code>, main blob <code>8448d710690ebe1cc28040f9611d05c9d008a961</code>. Definition **22.1.86**, source label <code>C4D2D319</code>, permanent tag <code>54C62141C0D9</code>, physical lines **1289–1313**; Remark **22.1.88**, source label <code>B104EEAF</code>, tag <code>9911A537C86C</code>, physical lines **1317–1338**, specifically **1326–1332**; Lemma **22.1.89**, source label <code>D532D7DB</code>, tag <code>6784060E951F</code>, lines **1343–1364**. Convex-function Proposition **21.11.12**, tag <code>B99B20CD6166</code>, <code>docs/sections/convex-functions-and-convex-bodies/index.html</code>, blob <code>2a123a863642a5a75caa173f0f73aff439a02ea4</code>, around line **102**, is a background comparison, **not certified**.
2. <code>docs/sections/volumes-under-bounded-mass--model-potentials-on-curves/index.html</code>, main blob <code>4ec0e8d5c90ad5df4e84f17bbc03a2298415e29f</code>, §**13.28.1** source label <code>3D44FEE1</code>, tag <code>2422DD1AB3AB</code>, lines **20–58**; §**13.28.4** label <code>647BF17A</code>, tag <code>74646DD62F50</code>, lines **64–85**; §**13.28.7**, tag <code>FB89848D2500</code>, lines **91–110**.
3. <code>docs/sections/volumes-under-bounded-mass--a-complete-space-over-varying-curve-backgrounds/index.html</code>, main blob <code>506708195b4fbeb7c1c0ac6ebea922983a764a6b</code>, Theorem **13.30.3**, source label <code>D0548646</code>, tag <code>C5551396F93B</code>, physical lines **43–90**, especially **58–76**. Proposition **13.29.1**, source label <code>405CAA19</code>, tag <code>C9C98321BEFC</code>, in <code>docs/sections/volumes-under-bounded-mass--background-changes-on-curves/index.html</code>, blob <code>94ff265434461fd6baee6532decdff369da3e177</code>, lines **14–36**, was used as an **internal, unrecertified classification input**.

This work explicitly excludes every Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion task. No such premise is expanded here.

## POME-NA-CONCAVE-TAIL-REPAIR-001

**Severity:** medium for the existing faulty printed recipe; **status: verified repair of the finite concave-envelope recipe only**. This extends, **but does not close**, the previously confirmed source error **POME-NA-CONCAVE-TAIL-001**. The original Remark 22.1.88 at main remains false as printed. Lemma 22.1.89 and its non-Archimedean valuation/cocycle inputs are **not** independently certified by the present repair.

### Error and exact correction

For finite nodes $\tau_0>\tau_1>\cdots>\tau_N$, Definition 22.1.86 interpolates the $\theta$-psh functions $A_i$ on adjacent node intervals and is constant $A_N$ on the entire left ray $\tau<\tau_N$. The correct inductive construction on the finite intervals is already displayed in Remark 22.1.88 (lines 1326–1329). But its separate left-ray assignment at **line 1332**

$$
 A'_\tau=A_{\tau_N}\qquad(\tau<\tau_N)
$$

must instead be

$$
 \boxed{A'_\tau=A'_{\tau_N}\qquad(\tau<\tau_N).}
$$

This single-symbol correction is **necessary**. With scalar data $(\tau_0,\tau_1)=(1,0)$ and $(A_0,A_1)=(0,-1)$, the printed rule yields $A'_\tau=0$ on $[0,1]$ but $A'_\tau=-1$ for $\tau<0$, violating concavity. The correct least concave majorant is identically zero on $(-\infty,1]$. Constants are $\theta$-psh for a Kähler background, so this is an admissible geometric test; see the older finding for the original counterexample.

### Complete finite real-data argument for the corrected rule

It suffices initially to take finite real node values $a_i$, since every finite family of $\theta$-psh potentials is finite outside a common pluripolar subset. Put $c_0=a_0$ and recursively define

$$
 r_j=\max\left\{0,\ \max_{i=j+1,\ldots,N}
       \frac{a_i-c_j}{\tau_j-\tau_i}\right\},
 \qquad
 c_{j+1}=c_j+(\tau_j-\tau_{j+1})r_j
 \quad (0\le j<N).
$$

The printed **finite-interval** maximum formula is *exactly*

$$
 F(\tau)=c_j+(\tau_j-\tau)r_j
 \quad(\tau\in[\tau_{j+1},\tau_j]),
 \qquad
 F(\tau)=c_N \quad(\tau\le\tau_N).
$$

For all $i>j$ one has

$$
 a_i\le c_j+(\tau_j-\tau_i)r_j.
$$

Consequently $c_{j+1}\ge a_{j+1}$, and, for all $i>j+1$,

$$
 \frac{a_i-c_{j+1}}{\tau_{j+1}-\tau_i}\le r_j,
 \qquad\text{so }0\le r_{j+1}\le r_j.
$$

The slopes of $F$ on the intervals, read from left to right, are $0,-r_{N-1},\ldots,-r_0$, a nonincreasing sequence. Thus $F$ is concave and nonincreasing. It majorizes the original affine interpolants because it majorizes them at both endpoints of each interval, and majorizes the original constant left tail because $c_N\ge a_N$.

For **minimality**, let $G$ be any real-valued concave majorant of the original curve on $(-\infty,\tau_0]$. Since $G(\tau)\ge a_N$ on the entire negative ray, concavity forces $G$ to be nonincreasing: a positive secant slope somewhere would force $G(\tau)\to-\infty$ as $\tau\to-\infty$, contradicting that lower bound. Starting at $\tau_0$, inductively suppose $G(\tau_j)\ge c_j$. For $\tau\in[\tau_{j+1},\tau_j]$ and any $i>j$, concavity and the majorant condition give

$$
 G(\tau)\ge
 \frac{\tau_j-\tau}{\tau_j-\tau_i}\,a_i+
 \frac{\tau-\tau_i}{\tau_j-\tau_i}\,c_j,
 \qquad G(\tau)\ge G(\tau_j)\ge c_j.
$$

Taking their maximum proves $G(\tau)\ge F(\tau)$ and the next-node induction. On $\tau<\tau_N$, monotonicity gives $G(\tau)\ge G(\tau_N)\ge c_N=F(\tau)$. Hence **the corrected formula gives the least concave majorant for all finite real node data**, not merely the original two-node counterexample.

For actual $\theta$-psh node functions, the corrected recursion uses only finite maxima and positive affine combinations of $\theta$-psh functions; hence every $A'_\tau$ is $\theta$-psh. Outside the common pluripolar pole set the scalar proof gives concavity, domination and minimality. Inequalities between quasi-psh representatives that hold outside a pluripolar set extend to their canonical upper-semicontinuous representatives. Thus the corrected finite construction is the least $\theta$-psh-valued concave majorant; polar-point ambiguities cannot be resolved by assigning arbitrary scalar values instead of the canonical psh representatives. The left ray is now automatically consistent with the value at the last node.

This verifies the **finite concave-envelope construction**. It does **not** verify the subsequently asserted non-Archimedean $\mathcal I$-projection/cocycle properties, nor any valuation-theoretic functoriality of Lemma 22.1.89. The source/error ledger must remain **confirmed error, unresolved until a separately reviewable source/reading patch**. A future patch should change only the left-tail token after checking all dependent statements **22.1.89** and **22.1.107** by their permanent tags.

### Reproducible small check

The new standalone text check <code>mathematical-audit/checks/concave_tail_finite_data.py</code> checks the two-node counterexample and 10,000 seeded random finite input arrays for node domination and the necessary nonincreasing $r_j$ slope condition. The check passed for that finite numerical assertion; it is **not** a substitute for the proof above, a project build, or formal verification.

**Affected dependents:** Remark 22.1.88, Lemma 22.1.89, Lemma 22.1.107, and any finite-data test-curve analytification that invokes the stated recipe. No blanket assertion that these downstream theorems are false, or repaired, follows from the correction to the isolated construction.

## POME-CURVE-POLAR-WEAK-CLOSURE-001

**Severity:** low; **status: verified conditional deduction** from the current curve classification and TV metric in Lemma 13.28.1, Theorem 13.28.4 and Theorem 13.30.3. The printed statements are correct; their full supporting theorem chains are not certified. **Conclusion:** finite-rational-atomic analytic models can converge **weakly as polar measures** to a **nonideal** ordinary model of the *same strictly positive mass*, despite remaining at a fixed positive TV distance from it.

### Explicit polar Cantor support

Work in the affine chart of $Y=\mathbb P^1$ with Fubini–Study form $\theta$ normalized by $\int_Y\theta=1$. Set

$$
 s_k=2^{-(k+1)!},\qquad
 E=\left\{\sum_{k=1}^\infty \varepsilon_k s_k:
                 \varepsilon_k\in\{0,1\}\right\}\subset ( -1,1),
 \qquad
 r_n=\sum_{k>n}s_k<2\,2^{-(n+2)!}.
$$

The $2^n$ level-$n$ cylinder sets are disjoint and each has diameter at most $r_n$. Every probability measure $\rho$ supported on $E$ has logarithmic energy

$$
 \begin{aligned}
 I(\rho)&=\iint_{E^2}\log\frac1{|x-y|}\,d\rho(x)\,d\rho(y)\\
 &\ge \log(1/r_n)\sum_{\varepsilon\in\{0,1\}^n}
      \rho(E_\varepsilon)^2
 \ \ge\ 2^{-n}\log(1/r_n)\ \longrightarrow+\infty .
 \end{aligned}
$$

Here the logarithmic kernel is nonnegative on $E^2$ because $\operatorname{diam}E<1$. The last divergence follows from $(n+2)!/2^n\to\infty$. The standard logarithmic-energy criterion therefore gives $\operatorname{cap}(E)=0$, so $E$ is polar on $Y$. Let $\nu$ be the Bernoulli measure obtained from independent fair digits $\varepsilon_k$; each $n$-cylinder has mass $2^{-n}$, so $\nu$ has **no atoms**.

Define finite-rational-atomic measures

$$
 \nu_n=2^{-n}\sum_{\varepsilon\in\{0,1\}^n}
        \delta_{\sum_{k=1}^n\varepsilon_k s_k},
 \qquad
 \mu_n=\tfrac12\nu_n,\qquad
 \mu=\tfrac12\nu .
$$

For every continuous test function $\varphi$,

$$
 \left|\int\varphi\,d\nu_n-\int\varphi\,d\nu\right|
 \le \omega_\varphi(r_n)\longrightarrow0,
$$

so $\mu_n\stackrel{w^*}{\longrightarrow}\mu$. But $\mu_n$ is carried by finitely many points whereas $\mu$ is nonatomic. Therefore they are mutually singular and

$$
 \boxed{\|\mu_n-\mu\|_{\rm TV}
       =\mu_n(Y)+\mu(Y)=1\quad\text{for every }n.}
$$

Let $p_n=p_{\mu_n}$ and $p=p_\mu$ be the **ordinary models** supplied by Lemma 13.28.1. Every $p_n$ is an **analytic ideal model** (finite rational polar atoms), while $p$ is **not ideal** because its polar measure is nonatomic. Nevertheless

$$
 U_\theta(p_n)=U_\theta(p)=1-\tfrac12=\tfrac12>0,\qquad
 d_\theta(p_n,p)=1.
$$

On the fixed-background fiber of the joint space, Theorem 13.30.3 gives the same distance $D((\theta,p_n),(\theta,p))=1$, and the exact distance of $p$ to the ideal subspace is $\mu^{\rm na}(Y)=1/2$.

### Interpretation and limitations

The result exhibits an **explicit fixed-positive-volume failure of weak-* closedness of the ideal/analytic polar-measure class**. It does **not** contradict the printed *total-variation* closedness of the ideal subspace or the density of analytic models **within that subspace**. A weak-* limit of polar measures is insufficient for any inference of $d_\theta$ or $D$ convergence. No claim is made here that the potentials $p_n$ converge pointwise, in capacity or in $L^1$ to $p$; weak convergence of polar curvatures is a strictly different premise.

**Affected dependents:** interpretation of §§13.28.4/.7, 13.29.1 and 13.30.3; topology of ideal projection, positive-volume model limits, and any proposed replacement of TV by weak-* measure convergence. Optional warning/example only; **no correction to a printed theorem** is proposed.

## Coverage, status and change boundary

This pass revisited *previously selected* §22.1.86–89 at proof level to **verify a complete repair of the known finite-recursion defect**, and directly checked the previously sampled §13.28.1/.4/.7 and §13.30.3 at a **new topology/weak-closure test**. §21.11.12 and §13.29.1 were read as conditional internal dependencies. The actual matrix remains **25 chapters / 747 numbered ToC sections / zero whole-section or whole-chapter certifications**. No other old finding was changed to resolved.

The excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains exactly **deferred-by-user**, neither fixed nor certified. No CI, builds, source edits, website publication, formalization, or original theorem-body modifications were carried out.
