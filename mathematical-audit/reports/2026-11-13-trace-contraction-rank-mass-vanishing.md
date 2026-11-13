# Exact trace-mass vanishing orders on semiample contractions

**Date:** 2026-11-13. **Stable finding:** `POME-TRACE-CONTRACTION-RANK-MASS-ORDER-001`.  
**Severity / status:** low / **verified conditional deduction**. The printed Theorem 20.2.34 is **not** contradicted. Its general trace-convergence theorem is **not** certified here.

## Production anchors and precise scope

- Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading edition: `docs/sections/the-trace-operator/index.html`, exact main blob `1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a` (physical lines in this report refer to this HTML, not the source manuscript).
- Definition 20.2.10: source `sgpt:4261C2F9`, permanent `5239E9ADD0FF`, physical lines 254–264; the positive-mass condition is part of the definition of `Tr_Y^theta`.
- Example 20.2.15: `sgpt:050DD15F` / `917FA516701F`, lines 310–315; analytic/smooth singularities restrict in their ordinary type.
- Example 20.2.17: `sgpt:628E430C` / `2272C87A04CE`, lines 327–337; positive limiting trace mass ensures the normalized trace exists.
- §20.2.29 standing hypotheses (connected compact Kähler X and smooth connected Y, big alpha): source `sgpt:32BCCE77`, permanent `A437169E35B2`, lines 660–665.
- Extended restricted-volume definition (20.2.31): source `sgpt:BDB42FF6`, permanent `03AF8A775E35`, lines 678–685; its Collins–Tosatti attribution is retained, not an analytic premise of our polynomial computation.
- Proposition 20.2.32: source `sgpt:3CF28B36`, permanent `AFC4F39F65CF`, lines 688–744, with *stronger* hypothesis `Y not contained in nK(alpha)`.
- Theorem 20.2.34: source `sgpt:30FD148B`, permanent `7EFDFA26519B`, lines 746–823, especially the three-way formula (20.2.35), source `sgpt:0E153B6A`, permanent `3C4F71AC116E`, lines 748–752; diagonal inequalities (20.2.36–37), sources `sgpt:6906F73C`, `sgpt:879E21DE`, permanent `6EEF71F49B54`, `E74D68200A33`, lines 794–808 and closing monotonicity 810–817.

We audit the **nonexcluded numerical and normalization consequences** of these integrated statements. The quasi-equisingular construction of the trace, its regularization-based antecedents, and the dedicated Bergman/L²/Ohsawa–Takegoshi programme are **not** revisited or certified.

## A general rank formula

Let `f:X -> Z` be a surjective generically finite holomorphic map between smooth connected projective manifolds of the same complex dimension `n >= 2` (a projective modification is enough). Choose a Kähler form `kappa` on Z and any Kähler form `omega` on X, and write

\[
\theta=f^*\kappa,\qquad \alpha=\{\theta\}.
\]

Let `Y subset X` be a smooth connected positive-dimensional subvariety of dimension `m`, and put `r=dim f(Y)`, `0 <= r <= m`. Then:

1. `alpha` is **nef and big**. The minimal potentials in both backgrounds are exactly `V_theta=0` and `V_{theta+epsilon omega}=0` for every `epsilon>0`; `nn(alpha)` is empty and `nu(V_theta,Y)=0`.
2. The ordinary trace `Tr_Y(0)` has the ordinary/P type of zero. For each `epsilon>0`, its positive-mass model trace is defined and `Tr_Y^{theta+epsilon omega}(0)=0`.
3. The total trace mass, *without any normalization by m!*, is the **exact polynomial**
\[
\boxed{\;
M_Y(\varepsilon)
=\int_Y\bigl(\theta|_Y+\varepsilon\omega|_Y\bigr)^m
=\sum_{k=0}^{r}\binom mk\varepsilon^{m-k}
\int_Y\theta^k\wedge\omega^{m-k}.
\;}
\tag{1}
\]
For `r<m`, its first nonzero term is
\[
\boxed{\;
M_Y(\varepsilon)=
\binom mr\left(\int_Y\theta^r\wedge\omega^{m-r}\right)
\varepsilon^{m-r}+O(\varepsilon^{m-r+1}),
\quad
\int_Y\theta^r\wedge\omega^{m-r}>0 .
\;}
\tag{2}
\]
For `r=m`, the limit is positive, `M_Y(0)=int_Y theta^m>0`.
4. In this model the positive-mass normalized trace `Tr_Y^theta(0)` is **defined precisely when r=m**. When `r<m`, the ordinary trace `Tr_Y(0)` still exists, but its `theta|Y`-model has zero mass, so Definition 20.2.10 does **not** define `Tr_Y^theta(0)`. Theorem 20.2.34's stipulated zero value in (20.2.35) is therefore indispensable.

### Proof

Because `theta=f^*kappa` is a smooth semipositive closed form, `alpha` is nef: `theta+delta omega` is Kähler for each `delta>0`. Since `f` is generically finite, the change-of-variables identity gives
\[
\int_X\theta^n=\deg(f)\int_Z\kappa^n>0;
\]
hence `alpha` is big. The class admits a global smooth semipositive representative, so it has no positive minimal multiplicities and its non-nef locus is empty. The constant function 0 is an admissible `theta`-PSH competitor bounded above by 0, and so `V_theta=0`; the same argument works for the positive form `theta+epsilon omega`. Both Lelong numbers and singularity types are consequently trivial.

Example 20.2.15 identifies `Tr_Y(0)` with the zero singularity type. As `(theta+epsilon omega)|Y` is Kähler, `0` has strictly positive full Monge–Ampère mass and is the normalized P-envelope of its own type, proving claim 2.

On the smooth locus, `theta|Y=(f|Y)^*kappa` has generic Hermitian rank exactly `r=dim f(Y)`. Consequently every wedge power `theta^k|Y` with `k>r` vanishes identically; this holds at critical points by continuity. Expanding the *smooth forms* by the ordinary binomial theorem yields (1), without weak convergence or any exchange of singular product limits. On the nonempty open set on which `f|Y` has rank r, the semipositive form `theta^r wedge omega^{m-r}` is a strictly positive volume density. Since its integral is nonnegative everywhere and positive on that open set, the integral is strictly positive. This proves (2) and the positive limit for r=m.

If `r<m`, `int_Y theta^m=0`. Every positive non-pluripolar top mass in this smooth semipositive cohomology class is bounded above by its cohomological mass (the standard internal monotonicity/mass bound, used here only for this existence assertion), hence cannot be positive. In particular, the smooth representative of the trace type has zero mass and does not qualify for the `>0` clause of Definition 20.2.10. If `r=m`, `0` itself has positive mass, so the normalized trace is defined and equals 0. No general trace-continuity theorem is used in this computation.

## Explicit projective models and sharpness for every vanishing order

Fix `m>=1` and any integer `q` with `1<=q<=m`; put `r=m-q`. Consider
\[
X=\operatorname{Bl}_{p}\mathbf P^{q+1}\times\mathbf P^r,
\qquad
Z=\mathbf P^{q+1}\times\mathbf P^r,
\qquad f=\pi\times\operatorname{id},
\qquad
Y=E\times\mathbf P^r,
\]
where `E ~= P^q` is the exceptional divisor and `P^0` denotes a point. Then `dim X=m+1`, `dim Y=m`, and `dim f(Y)=r`. For `kappa=pr_1^*omega_FS+pr_2^*omega_FS`, `theta=f^*kappa` is a semipositive nef-and-big class, but its restriction to Y has rank exactly r. For any Kähler `omega` on X, (2) gives **exact vanishing order q**, with positive leading coefficient. Every integer order 1 through m occurs although `Y not subset nn(alpha)` and the ambient minimal potential is smooth.

At `r=0` the formula is even exact, not just asymptotic:
\[
X=\operatorname{Bl}_p\mathbf P^{m+1},\quad
Y=E\simeq\mathbf P^m,\qquad
\boxed{M_Y(\varepsilon)=\varepsilon^m\int_E\omega^m.}
\tag{3}
\]
Thus **zero generic Lelong number plus nefness of the ambient big class does not imply a positive-mass trace in the unperturbed restricted class**. This is the exact boundary between the stronger hypothesis of Proposition 20.2.32 and the zero-mass convention in Theorem 20.2.34. Theorem 20.2.34 remains correct in these models; the displayed limit equals zero when q>0.

## Independent check of the final limiting argument (conditional on its analytic inputs)

The displayed proof at lines 788–817 fixes a positive background shift, takes the `d_S` limit there, then chooses `epsilon_j<1/j` to obtain its diagonal value `A_j -> M` in (20.2.36). Equation (20.2.37) provides `M <= B_j <= A_j` for the varying-background mass `B_j`. The elementary squeeze yields `B_j -> M`; its printed monotonicity in the perturbation parameter then promotes convergence on that selected sequence to the full `epsilon downarrow 0` limit. No sequential compactness of the *net of all parameters* is being inferred. This algebraic implication is valid, **provided** the displayed fixed-background `d_S` mass continuity, mixed-product positivity/monotonicity, and trace comparison have been established. Their proofs are *not* verified in this run.

For the smooth models above, all these quantities are the same elementary polynomial `M_Y(epsilon)`. In particular, both the positive-limit and zero-limit branches are checked without invoking any excluded regularization result or the transitive general trace theory.

## Findings and proposed action

- **POME-TRACE-CONTRACTION-RANK-MASS-ORDER-001**, severity **low**, **verified conditional deduction**: exact order `dim Y - dim f(Y)` and sharp models for each positive order; original Theorem 20.2.34 is **not false**. No production patch is required. A useful *proposed-only* illustrative remark after (20.2.35) could state the smooth blowup example (3) to explain why the undefined-trace convention is necessary.
- **Unverified dependencies**: existence, well-definedness and full `d_S` continuity of general traces; comparison in arbitrary non-pluripolar classes; the original proof of Proposition 20.2.32 additionally cites Matsumura's restricted-volume continuity (physical line 733), which is a genuine external mathematical input and **not** supplied by this explicit model. Do not call these certified.
- **Not a genuine duplicate** of earlier blowup intersection or restricted-volume calculations: the newly checked assertion is the *full rank-indexed trace-mass vanishing-order law*, the `nn(alpha)` / positive trace distinction, and the exact zero-convention branch of (20.2.35). No previous finding is reclassified.
- **Deferred-by-user, unchanged**: all dedicated Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proofs, including any trace prerequisites that invoke that excluded programme. They have **not** been resolved.
- **Coverage**: §§20.2.29–20.2.35 and the numerical diagonal inequalities (20.2.36–37), plus the stated Definition 20.2.10, Examples 20.2.15 and 20.2.17 only; earlier §§20.2.21–22 not re-credited. **0 new first-visited numbered sections; 0 fully certified sections; actual main ToC 25 chapters / 747 numbered sections.** No builds/tests/CI, no publication or edits to main/source/registry/tags.
