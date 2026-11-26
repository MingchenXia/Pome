# Smooth threshold tests and the essential lower envelope (2026-11-27)

Production main b6933b772f41b45918f7e25ed1afbbb1fd892272; audit head at start 024ef672db40a61a6c5e9fce8c4e378951b1299e.

## POME-THRESHOLD-SMOOTH-ESSENTIAL-LOWER-ENVELOPE-001

Low / verified conditional deduction, not a printed error. Theorem 15.28.9 (source 6B50E67D, permanent 4AC87EC7D266, lines 155–216) gives a special gap between smooth and measurable comparison tests. The exact general formula is as follows, conditional on the existing threshold characterization and dual formula.

Use the chapter convention of smooth positive probability dV, connected compact X, n>=1, Hermitian h. For a probability density f in L^1 with f>=m>0 almost everywhere, define the essential lower envelope
\[
 f_*(x)=\sup_{U\ni x}\operatorname*{ess\,inf}_U f
\]
over open neighborhoods. Then
\[
 \boxed{C_h^{\rm sm}(f)=b_h(f_*)}.
\]
Here f_* need not be a probability density; it may be infinite on a null set.

Proof. The superlevel sets {f_*>t} are open. For rational t, each is a union of members U of a countable base with ess inf_U f>t; thus f>t almost everywhere on it. Taking the union of exceptional null sets over rational t proves f_*<=f a.e., hence f_* is integrable as an equivalence class. Also f_*>=m. For continuous g, g<=f a.e. iff g<=f_* everywhere: if g(x)>f_*(x), choose a strict intermediate number t and a neighborhood where g>t; the a.e. inequality forces ess inf there >=t, a contradiction. The converse uses f_*<=f a.e.

For a smooth positive probability test g, R=||g/f||_infty is finite and positive. The smooth density q=g/R satisfies q<=f a.e. and c_h(q)=R c_h(g) by 15.27.1. Conversely any smooth strictly positive q<=f can be normalized to g=q/Z, Z=int q dV, and then R c_h(g)=||q/f||_infty c_h(q)<=c_h(q). Thus the printed infimum equals inf{c_h(q): q smooth, 0<q<=f_*}. Every such q has c_h(q)=b_h(q)>=b_h(f_*) by 15.28.4 and 15.28.7.

For the reverse bound construct smooth positive minorants. Fix a Riemannian distance d. For integers j>m let
\[
 v_j(x)=\inf_y\{\min(f_*(y),j)+j d(x,y)\}.
\]
These are finite j-Lipschitz functions, >=m, <=f_* and increase to f_* pointwise: otherwise bounded almost-minimizing values along j→infty imply d(x,y_j)→0, the truncation at j is inactive for large j, and lower semicontinuity gives a contradiction. Approximate v_j uniformly within epsilon_j (0<epsilon_j<m/4, epsilon_j→0) by smooth functions using a finite smooth partition of unity on neighborhoods of oscillation <epsilon_j; subtract epsilon_j. The resulting q_j satisfy m/2<=q_j<=v_j<=f_* and converge pointwise to f_*; they need not increase. For each fixed Gauduchon gamma, dominated convergence using the bounded coefficient a_gamma and integrable f_*^(1/n) gives L_gamma(q_j^(1/n))→L_gamma(f_*^(1/n)). Hence 15.29.1 and 15.28.7 imply
\[
 \sup_j c_h(q_j)^{-1/n}\ge \sup_\gamma L_{h,\gamma}(f_*^{1/n})
 = b_h(f_*)^{-1/n}.
\]
The reverse bound follows from q_j<=f_* a.e. Taking reciprocal powers proves the formula, including b_h(f_*)=0. No limit-supremum interchange is needed.

Consequences: the smooth tests depend only on f_* and compute b_h(f) whenever f=f_* a.e. In particular this holds for continuous f. If h is Kähler, V=int h^n, then C_h^sm(f)=V/int f_* dV while b_h(f)=V. A strict numerical gap can therefore occur even with positive lower mass. Choose a closed nowhere dense set K of measure a in (0,1) (remove a dense open set of sufficiently small volume from a small closed coordinate ball). For f=(1+1_K)/(1+a), every open set meets the open complement of K, so f_*=1/(1+a) and C=(1+a)V>V. Theorem 15.28.9's special strict gap in positivity is unaffected, and its proof is the special case of a constant f_*. Proposed addition after that theorem; retain its conclusion and hypotheses. No assertion of exact threshold solutions.

## POME-THRESHOLD-ZERO-RESIDUAL-PROBABILITY-CONE-001

Low / verified conditional deduction, not a printed error. Strengthens the discontinuity statement after Theorem 15.32.1 (permanent D988D47D5E0E), lines 11–33. Assume v_-(h)=0 and fix 0<=m<1. In the L^1-complete metric space
\[
 \mathscr P_m=\{ f\in L^1(dV): f\ge m\text{ a.e.},\ \int f\,dV=1\},
\]
zero-threshold densities are a dense G_delta; positive-threshold densities are dense and meagre.

Proof. Theorem 15.28.9 supplies a probability density g with b_h(g)=0. By 15.28.4, b is order-reversing and b_h(tg)=b_h(g)/t for t>0, including zero. Thus g_m=m+(1-m)g belongs to P_m and has zero threshold. For any f in P_m, mixtures (1-t)f+t g_m, 0<t<1, stay in P_m, dominate t(1-m)g and have zero threshold; they tend to f in L^1. Each {b_h<1/k} is relatively open by 15.32.1 (or the infimum of continuous positive quotients in 15.29.3). These sets are dense by the mixtures and their intersection is exactly {b_h=0}. Its complement is a countable union of closed nowhere dense sets. On the other hand bounded probability densities q_j=min(f,j)+1-int min(f,j)dV, j>=1, remain >=m, converge to f in L^1, and have positive threshold by 15.28.7. This proves both density statements. At m=1 the space is a singleton of positive threshold. Suggested addition after the printed discontinuity paragraph. No convergence of potentials or exact equation claims.

## Actual coverage and checks

- docs/sections/equations-with-prescribed-singularities--subsolutions-for-an-individual-density/index.html, blob 9262e6b9fd8929cbdd3f75bacbe2a532839d1dbe: all mathematical lines 7–220. Checked (15.28.1–2), 15.28.3 (source 0BA4348E/permanent 8298FD96E154), 15.28.4 (76378BFC/CC13A9B1D927), 15.28.6 (AF83D4C4/D42D2088B421), 15.28.7 (58DB2491/69BB1D568698), 15.28.9 (6B50E67D/4AC87EC7D266). Tail infima in 15.28.3 are bounded by their a.e. limit g, validating both dominated convergence passages; finite maximum locality precedes the damped limit; division by the positive weight is away from poles. The greatest normalized subsolution proof has a fixed integrable lower function. The diagonal nowhere-dense construction's tail bound is summable; g=1 is a probability test by the chapter convention.
- docs/sections/equations-with-prescribed-singularities--gauduchon-tests-for-integrable-densities/index.html, blob 8cd9c2d08a4f60ed96d0f5197f4f7ae4df276998: all mathematical lines 7–126. 15.29.1 (0DF693AB/346B39C3F0B6), 15.29.5 (74689D40/429BB0FF98A9); checked normalization cancellation, dual exponent 2n/(2n-1), bounded-density approximation, interchange of two suprema, reciprocal powers in metric comparison, exact-ddc Stokes, reference-volume change.
- Context only: §15.27 lines 7–71, blob fc7d4f24f72d9b6ec898eedc961b789e65ef3e25 (scalar comparison and L^p continuity); §15.1 line 7, blob a638ee4e9afd9b284c28aef989076a4874b028aa (probability); §15.32 lines 7–33, blob 903ae0ce7173604063a833295dd94e971b18fd72 (upper semicontinuity and discontinuity). Not new whole coverage.
- Also reread §§21.5–6 mathematical lines 7–157 and 7–46, blobs 7089aa41ae2422b1bd6b5094e46668cbc8ed37be and b3b4e34fff767a717df812a381f905589b257fb3, already whole direct in the matrix. Checked slope measurability, vague/narrow distinction, polarization and compact envelope lower semicontinuity; no new finding logged.
- Uncertified dependencies: 13.14.6, 13.15.9, 5.29.19, 5.25.2, 15.27.1–2, 12.2.3, 12.15.4, 14.19.19, 15.35.3 and their upstream analytic existence, comparison and continuity. Any excluded regularization inputs remain deferred-by-user; no excluded proof reopened.
- Actual main docs/index.html TOC had 747 distinct section IDs and the matrix had 747 rows with no missing IDs. Structural check only. Two whole direct conditional sections, two new conditional deductions, zero confirmed errors, zero demonstrated new gaps, zero complete upstream certifications; historical first visits unreconciled. No tests/build/CI/publication or production source, registry or tag changes.
