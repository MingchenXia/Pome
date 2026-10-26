# Magnetic Riesz means: exact Landau midpoint defect and uniform Dirichlet rate; nuclear Banach rigidity

**Audit date:** 2026-10-27 (Asia/Shanghai).  
**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Review-branch head consulted before the update:** `1e130a81f5b539996317119059f22ff7839815c6`.  
**Scope:** first selected proof-level review of the current integrated §§2.24 and 2.13.1–3, *not* complete section or upstream-source certification. No Demailly approximation/regularization or its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme was opened. Although the reading-edition source identifier contains “demailly-complex-geometry”, these two independent functional-analytic/spectral sections contain no use of the excluded approximation programme in the arguments audited.

## Sources actually read

1. `docs/sections/magnetic-models-and-spectral-localization/index.html`, `main` blob `ee89de7d23cc96a8546c736ac7d068546b126f3a`: §2.24.1 initial convention (lines 5–8); Lemma **2.24.2** permanent tag `3E8E852DB903` (lines 10–27); measure **(2.24.4)** source label `demailly-complex-geometry-4EE24E32`, permanent tag `6919A4A3FD8F` (lines 31–35); counting and Riesz means **(2.24.5)** label `demailly-complex-geometry-E2C26C03`, tag `72E6618A3A3C` (lines 38–45); Lemma **2.24.6**, source label `demailly-complex-geometry-2FD17158`, tag `0F14CB3D46F3` (lines 49–71), especially uniform mass bounds **(2.24.7)** tag `DD3B970F19C7`, lines 50–54; Proposition **2.24.8**, source label `demailly-complex-geometry-7DBC83A8`, tag `C554004EA447`, lines 75–110; exact localization inequality **(2.24.10)** source label `demailly-complex-geometry-E619A2C2`, tag `B6FBF3F18EA3`, lines 94–109.
2. `docs/sections/open-maps-nuclear-spaces-and-inverse-limits--nuclear-spaces-and-completed-tensor-products/index.html`, `main` blob `ecbf01a4ed81461ba32f1e0c88c6a550ebaa8135`: Lemma **2.13.1**, source label `demailly-complex-geometry-A13EE630`, tag `67761F6CDA64`, lines 17–47; definition of nuclear Fréchet space (line 73); Theorem **2.13.3**, source label `demailly-complex-geometry-054FCEA1`, tag `A46D09531259`, lines 77–104. Supporting tensor Proposition 2.13.2 (lines 52–69) was read for consistency but not independently certified. Theorem 2.13.4 and its Bergman-space calculation are **outside the selected review**.

All source labels refer to the integrated reading edition, not an assertion that the underlying source itself has been fully reviewed.

## POME-LANDAU-RIESZ-MIDPOINT-001

**Severity:** low. **Status:** verified conditional deduction. **Printed theorem:** not false.  
**Claim:** for a *single magnetic pair* (complex dimension one) and any (b>0), (E\ge0), set
[
x=\frac E{2b},\qquad N=\max\{0,\lceil x-\tfrac12\rceil\}.
]
Then the exact, strict-threshold spectral counting convention of (2.24.5) gives
[
\nu_b(E)=\frac{bN}{2\pi},\qquad
r_b(E)=\frac b{2\pi}(NE-bN^2).
]
The zero-field measures in (2.24.4) give (\nu_0(E)=E/(4\pi)), (r_0(E)=E^2/(8\pi)), and therefore the **exact identity**
[
\boxed{r_0(E)-r_b(E)=\frac{b^2}{2\pi}\left(N-\frac E{2b}\right)^2}.
]
In particular
[
0\le r_0(E)-r_b(E)\le\frac{b^2}{8\pi},
\qquad
|\nu_b(E)-\nu_0(E)|\le\frac b{4\pi}.
]
Both error constants are optimal at every odd Landau threshold (E=(2m+1)b) ((m\ge0)). For (E\le0) the two Riesz means vanish, and the same bound holds. Thus the Riesz mean has an *every-energy uniform* (O(b^2)) zero-field error in one magnetic pair; counting is only (O(b)) and may jump at thresholds. This is stronger than the qualitative joint continuity of (r_b(E)) established in Lemma 2.24.6.

**Complete deduction.** The allowed Landau levels ((2p+1)b<E) are precisely (p=0,\dots,N-1). The odd-integer sum (\sum_{p=0}^{N-1}(2p+1)=N^2) yields the first two displayed expressions. The measures at (b=0) integrate directly. Writing (E=2bx),
[
\frac{E^2}{8\pi}-\frac b{2\pi}(NE-bN^2)
=\frac{b^2}{2\pi}(x-N)^2.
]
By the tie-down nearest-integer rule, (|N-x|\le1/2). Equality holds exactly at half-integers (x=m+1/2), where the strict counting convention chooses (N=m). The count difference is (b(N-x)/(2\pi)). No interchanging of any infinite limits is used; at each fixed (E>0) only finitely many Landau levels occur.

**Dependencies:** the spectral measure normalization of Lemma 2.24.6 and the displayed definitions (2.24.4–5), directly inspected but not independently reconstructed from operator domains. **Proposed change:** optional exact-error corollary after Lemma 2.24.6, preserving the strict threshold, zero-field normalization and source attribution. **Affected dependents:** quantitative small-field Riesz-mean estimates; no change to any existing theorem conclusion.

**Small independent arithmetic check actually executed:** 3,540 finite ((b,E)) choices, with (b\in\{0.001,0.1,0.3,1,2,10\}), each 590 energies (580 values (E=ib/29), (0\le i<580), plus ten odd-threshold energies), confirmed the exact upper bound within floating-point tolerance. This is not a substitute for the algebraic proof; no project test suite was run.

## POME-MAGNETIC-DIRICHLET-RATE-001

**Severity:** low. **Status:** verified conditional deduction / quantitative proof strengthening. **Printed theorem:** not false.  
**Claim:** under the hypotheses of Proposition 2.24.8, with the parallelepiped shape and inverse shape uniformly controlled, for every fixed upper energy (E_*\ge0) and sufficiently large (R),
[
\boxed{0\le r_b(E)-\frac{R_{H_{b,RU}}(E)}{\operatorname{Vol}(RU)}
\le \frac{C_{U,n}(E_*^n+E_*^{n+1})}{R}}
\quad(E\le E_*,\ b_j\ge0).
]
Here (C_{U,n}) is uniform within any specified shape-bounded family (an absolute additive numerical constant may be absorbed). The result also covers all (E\le0) because the magnetic form is nonnegative and both sides are zero. Unlike the printed (o(1)), the error is explicitly (O(R^{-1})), uniformly as some field magnitudes tend to zero or become arbitrarily large.

**Proof.** The upper bound is *already* established in lines 85–92. For the lower bound use the exact inequality (2.24.10), valid for every real (\eta\in C_c^\infty(RU)) with (0\le\eta\le1). Replace the printed layer of width (R^{1/2}) at line 109 by a layer of **fixed physical width**, say (1\)–(2), independent of (R,b,E): write (RU=A_R([0,1]^{2n})), choose a smooth one-variable function (\chi\) equal to zero at coordinate-distance (\le c/R) from each face, equal to one beyond (2c/R), and put (\eta(x)=\prod_{i=1}^{2n}\chi((A_R^{-1}x)_i)), with matching cutoffs at both ends. The shape and inverse-shape bounds imply, uniformly,
[
\int_{RU}\eta^2\ge\operatorname{Vol}(RU)(1-C/R),
\qquad \int_{RU}|d\eta|^2\le C\operatorname{Vol}(RU)/R.
]
Indeed the boundary-layer fraction is (O(R^{-1})), while the physical derivatives are (O(1)); the factor (R^{-1}) in the inverse coordinate Jacobian cancels the (O(R)) slope of the one-variable boundary cutoff. Substituting in (2.24.10) gives
[
\frac{R_{H_{b,RU}}(E)}{\operatorname{Vol}(RU)}
\ge r_b(E)-\frac C R\bigl(r_b(E)+\nu_b(E)\bigr).
]
Apply (2.24.7) to bound these two coefficients by (C_n(E_*^{n+1}+E_*^n)). This gives the claimed rate. An elementary fixed-width cutoff therefore improves the proof without any additional spectral input, and no eigenvalue-counting estimate at the discontinuous thresholds is required.

**Dependencies:** the bounded-domain variational argument in Lemma 2.24.2, the full-space spectral-model diagonal calculation in Lemma 2.24.6, and the trace lower inequality (2.24.10); these are inspected at the cited anchors but not independently globally certified. **Proposed change:** optional replacement of the last cutoff paragraph at §2.24.8, *through a separately reviewable patch only*. No changes to the theorem statement are required, except optionally recording the quantitative bound. **Affected dependents:** finite-volume uniform Riesz mean asymptotics used in spectral localization and related Morse calculations; the latter were not re-audited.

## POME-NUCLEAR-BANACH-FINITE-DIM-001

**Severity:** low. **Status:** verified conditional deduction. **Printed statements:** not false.  
**Claim:** with the nuclearity definition at physical line 73 of §2.13, **a Banach space is a nuclear Fréchet space if and only if it is finite-dimensional**.

**Proof.** A finite-dimensional Banach space has a defining norm whose canonical identity map is finite rank and nuclear. Conversely let (B) be Banach and nuclear as a Fréchet space. Choose an increasing defining sequence of seminorms (p_j) with nuclear links (B_{p_{j+1}}\to B_{p_j}). Since this sequence defines the Banach norm topology, some (p_J) dominates the Banach norm up to a positive scalar: the norm-unit neighborhood contains a neighborhood (\{p_J<\epsilon\}), and homogeneity yields (\|x\|\le C p_J(x)). Continuity gives the reverse inequality (p_J(x)\le C'\|x\|), and the same holds for (p_{J+1}). Consequently (B_{p_J}) and (B_{p_{J+1}}) both identify topologically with (B), and their canonical link is the identity on (B) up to Banach isomorphisms. By Lemma 2.13.1, that nuclear link is compact. Hence the identity on (B) is compact and the closed unit ball is compact.

For completeness, if an infinite-dimensional normed space had compact unit ball, choose inductively a unit vector (x_{m+1}) of distance (>1/2) from the finite-dimensional span of the preceding vectors. Such vectors exist: any proper closed subspace (V) and any (y\notin V), writing (d=\operatorname{dist}(y,V)>0), admit (v\in V) with (\|y-v\|<2d); the unit vector ((y-v)/\|y-v\|) has distance (>1/2) from (V). The resulting sequence is pairwise (>1/2)-separated, contradicting compactness. Thus (B) is finite-dimensional.

The Hilbertian equivalence and permanence results of Theorem 2.13.3 were checked for consistency with this consequence; they are not invoked as an independent complete proof. **Dependencies:** definition in §2.13 at line 73 and compactness of Banach nuclear maps in Lemma 2.13.1. **Proposed change:** optional clarifying corollary after Theorem 2.13.3; especially useful when applying nuclear Fréchet permanence to infinite-dimensional function spaces without mistaking nuclearity for a property of their Banach completions. **Affected dependents:** tensor-product and functional-analytic arguments that distinguish Fréchet inverse limits from their Banach steps.

## Coverage and disposition

- **New from inventory-only:** §2.24, direct selected proof reading of Lemma 2.24.2, Lemma 2.24.6 and Proposition 2.24.8, including precise normalizations, mode-counting, variational bound and cutoff choice.
- **New from inventory-only:** §2.13, direct selected reading of Lemma 2.13.1, Proposition 2.13.2 and Theorem 2.13.3 (definitions, compactness, Hilbert factorization, permanence and tensor topologies). No examination of the §2.13.4 holomorphic-function/Bergman-space calculation.
- **Not inspected:** the rest of chapter 2, the prerequisites such as §10.46.1, general magnetic Morse inequalities, and the underlying source manuscripts beyond the integrated rendered proof.
- Three new **conditional deductions**, no confirmed false theorem, no external-dependency closure, no claim that an entire section or entire chapter has been certified. Existing confirmed errors, proof gaps, resolved statuses and all user-deferred matters are preserved.
- **No** publication, full build, CI, formalization, main/source/registry/canonicalization/tag changes. This report and its tracking rows are review-branch-only audit Markdown.
