# Divisor zero splitting: arbitrary-net continuity and sharp transport obstruction

**2026-11-16.** **Stable finding:** `POME-DIVISOR-ZERO-SPLITTING-W1-NET-001` — **low / verified conditional deduction**, not a confirmed false theorem or proof gap. **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Integrated statement and exact provenance
- `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` at main blob `dae567406b2030e550664ca57b1fe77911d956d4`; §20.5 permanent tag `1564EBAEA948`.
- Lemma 20.5.2: source `demailly-complex-geometry:72B4BF94`, permanent tag `551A781E3A1C`, physical lines 10–21 (holomorphic-logarithm local L¹ convergence).
- Theorem 20.5.5: source `demailly-complex-geometry:D58680EB`, permanent tag `F1C928146DBC`, lines 63–75 (integer intersections, coefficient L¹ convergence) and proof lines 80–127; (20.5.7) source `demailly-complex-geometry:85805B88`, permanent tag `85DED4E0947F`, lines 70–74.
- Example 20.5.11: source `demailly-complex-geometry:1764A64B`, permanent tag `FF4839E28893`, lines 154–155 (cusp \(y^2=x^3\) with normalization \((t^2,t^3)\)).
- Lemma 20.5.3 lines 27–60 and Theorem 20.5.10 lines 133–149 were *contextual* dependency reads; no complete re-verification is claimed.

The convention is \(dd^c=i\partial\bar\partial/(2\pi)\), so \(dd^c\log|z|^2=\delta_0\). All \(W_1\) distances below are for equal-mass finite measures using Euclidean distance; the total-variation norm is the sum of the mutually singular masses.

## Arbitrary directed nets, without sequential-subnet assumptions

**Claim.** If a net \(f_\lambda\) of holomorphic functions on a fixed neighborhood of a reduced pure-dimensional analytic cycle \(A\) converges **compact-open** to \(f\), and \(f\) is not identically zero on any irreducible component of \(A\), then
\[
\log|f_\lambda|^2\longrightarrow\log|f|^2
\quad\text{in local coefficient }L^1([A]),
\]
and \(dd^c(\log|f_\lambda|^2[A])\rightharpoonup dd^c(\log|f|^2[A])\) on compactly supported tests **as a net**.

**Proof.** On each coordinate ball \(V\), the compact-open topology of \(\mathcal O(V)\) is metrizable by a compact exhaustion and its sup seminorms. At a nonzero \(g\), the neighborhood \(\{h:h(b)\ne0\}\) is open for any fixed \(b\) with \(g(b)\ne0\). Lemma 20.5.2 proves sequential continuity of \(h\mapsto\log|h|^2\) from that neighborhood into the metrizable space \(L^1_{\rm loc}(V)\). Between **metric spaces**, sequential continuity implies genuine topological continuity; consequently *every* directed net converging to \(g\) has convergent local logarithms. This argument does not extract a sequence or sequential subnet from the original net.

For each irreducible component, take the proper smooth resolution \(\pi:M\to A\) used in the integrated theorem (the permitted Hironaka input). Composition preserves compact-open convergence, so \(f_\lambda\circ\pi\to f\circ\pi\), and the latter is not identically zero on any component. Finitely many coordinate balls cover a compact neighborhood \(L\supset\pi^{-1}(K)\), giving smooth-volume \(L^1(L)\) convergence. Apply exactly the compact pullback coefficient bound of §20.5.5 proof lines 121–125:
\[
\int_{K\cap A}|\log|f_\lambda|^2-\log|f|^2|\,[A]\wedge\beta^p
\le C_K\int_L|\log|f_\lambda\circ\pi|^2-\log|f\circ\pi|^2|\,dV_M\to0.
\]
For an effective cycle, local finiteness reduces to finitely many components per compact. Passing to \(dd^c\) against fixed smooth compact test forms proves weak convergence of currents. \(\square\)

This upgrades the **quantifier** of the printed sequential result; it does not identify an error in the sequential proof. In particular it does *not* use an unproved assertion that a convergent net admits a convergent sequential subnet.

## Smooth curve: exact best weak rate and failed norm convergence

For \(m\ge1\), on \(\Delta\subset\mathbb C\), put \(f_a(z)=z^m-a\) and \(f_0(z)=z^m\), with \(0<|a|<1\). Then \(\|f_a-f_0\|_\infty=|a|\) exactly, and the Poincaré–Lelong identity gives
\[
\mu_a=dd^c\log|f_a|^2=\sum_{z^m=a}\delta_z,\qquad \mu_0=m\delta_0.
\]
Every source point must be transported to zero; all \(m\) distinct roots have modulus \(|a|^{1/m}\). Hence
\[
W_1(\mu_a,\mu_0)=m|a|^{1/m},\qquad
\|\mu_a-\mu_0\|_{\mathrm{TV}}=2m\quad(a\ne0).
\]
The test function \(\varphi(z)=|z|\) realizes the exact bounded-Lipschitz dual distance on \(\Delta\). For this family no estimate \(W_1\le C\|f_a-f_0\|_\infty^\alpha\) with \(\alpha>1/m\) can hold uniformly as \(a\to0\). Since \(m\) is arbitrary, the qualitative hypotheses cannot imply **any multiplicity-independent positive Hölder exponent**, much less total-variation continuity. This is not a claim of a general \(1/m\)-Hölder theorem.

## Singular cusp: two sharp exponents affected by the embedding

Let \(A=\{y^2=x^3\}\subset\mathbb C^2\) and \(\gamma(t)=(t^2,t^3)\). All formulas below hold in a fixed small neighborhood for \(0<|a|\ll1\).

For \(f_a=x^m-a\), one has \(f_a\circ\gamma=t^{2m}-a\). All \(2m\) roots give distinct smooth cusp points, and
\[
\mu^x_a=\sum_{t^{2m}=a}\delta_{(t^2,t^3)},\quad
\mu^x_0=2m\delta_{(0,0)}.
\]
Each point lies at Euclidean distance \(|a|^{1/m}\sqrt{1+|a|^{1/m}}\) from zero. Thus, **exactly**,
\[
W_1(\mu^x_a,\mu^x_0)
=2m|a|^{1/m}\sqrt{1+|a|^{1/m}},
\qquad \|\mu^x_a-\mu^x_0\|_{\mathrm{TV}}=4m.
\]

For \(h_a=y^m-a\), the normalization has \(h_a\circ\gamma=t^{3m}-a\). There are \(3m\) distinct smooth cusp zeros and
\[
\mu^y_a=\sum_{t^{3m}=a}\delta_{(t^2,t^3)},\quad
\mu^y_0=3m\delta_{(0,0)},
\]
\[
W_1(\mu^y_a,\mu^y_0)
=3m|a|^{2/(3m)}\sqrt{1+|a|^{2/(3m)}},
\qquad \|\mu^y_a-\mu^y_0\|_{\mathrm{TV}}=6m.
\]
In both families the *function* supnorm perturbation is exactly \(|a|\). The normalized orders \(2m,3m\) count intersection multiplicities but do **not by themselves** determine the ambient Euclidean \(W_1\) exponents \(1/m,2/(3m)\): the cusp parametrization enters. The formulas crosscheck the coefficient \(2\) in the original Example 20.5.11. They also exhibit a sharp weak/TV distinction for singular cycles.

## Classification, proposed correction, and affected dependencies

**No printed assertion is refuted.** Lemma 20.5.2, Theorem 20.5.5 including (20.5.7), and Example 20.5.11 remain consistent with this new exact test. Status is **verified conditional deduction** (the arbitrary-net extension uses the printed coefficient bound; the elementary smooth/cusp examples use the normalized Poincaré–Lelong identity). Theorem 20.5.10 and the general proper pushforward statement were not fully certified.

**Optional proposed patch (not applied):** add a remark after 20.5.5 explaining its local topological continuity extends to nets and that weak currents need not converge in total variation or with a multiplicity-free rate. Preserve attribution, source labels, equation numbering and permanent tags.

**Potential dependents:** any generalization in §20.8 or complex-cycle arguments that strengthens weak convergence to norm convergence, or assumes a universal rate without a zero-multiplicity bound. These dependents are *review candidates*, not asserted errors.

**Recorded inputs:** internal local holomorphic-log compactness, the normalized Poincaré–Lelong formula, coefficient-current pullback; the permitted Hironaka resolution in the arbitrary-cycle argument. The user-excluded Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**, not resolved or reopened.

**Coverage:** §20.5 was previously partially reviewed: first visits **+0**, complete transitive section certificates **+0**. Physical lines directly read 10–21, 63–75, 80–127, 154–155; lines 27–60 and 133–149 context only. Current main unchanged, existing index 25 chapters/747 sections (not independently recounted). A small standalone numerical check was executed for \(m=1,2,3,5\) and \(a=10^{-3},10^{-6}\); it is a consistency check, not proof. No project build, test suite, GitHub Actions CI or publication.
