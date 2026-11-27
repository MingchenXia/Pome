# Universal slope-stability chamber for the Hirzebruch extensions

Date: 2026-11-27. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Finding: **POME-HIRZEBRUCH-UNIVERSAL-EXTENSION-STABILITY-CHAMBER-001** — low / verified conditional deduction (sharp strengthening, not a printed theorem error).

## Anchors and actual coverage

All three current integrated sections were directly read (mathematical paragraphs only; HTML physical line numbers).

- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--ample-comparison-quotients-on-hirzebruch-surfaces/index.html`, blob 6d836a2ed19f76c26311025602fb44a56713e390, lines 7–195. Lemma 11.13.1 (9A9AA541 / 8FE2AABC7334), Proposition 11.13.2 (3E4548CE / 6EA287558571), Lemma 11.13.3 (5616608C / 7055476D483C), Proposition 11.13.4 (32431F4A / B6B9C2094631).
- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--stable-extensions-approaching-the-split-comparison-bundle/index.html`, blob 03559e82ef17c97d04258775312d994ec217e376, lines 7–143. Proposition 11.14.1 (D386B065 / A195B6162A49), statement 26–34, proof 39–87, especially 58–86; Proposition 11.14.2 (A0E26851 / FD54983C4E79), 92–107; Proposition 11.14.3 (E4134CA1 / 7215288BDF53), 112–139.
- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--deforming-to-stable-ample-bundles/index.html`, blob 08ac54c401030e52cf3001d6ddc146fc35956d54, lines 7–142. Lemmas 11.15.1–4 (CC879AEF / 0EEC7E1B2FB0; 943EC9EA / 927EFEB9D586; E3916599 / EBF7EB73EABE; CAE7FA8C / 319641577F72), Theorem 11.15.5 (88F5B6CB / E769519C862E), Corollary 11.15.6 (792988FB / A2CE95B32341). Walter input at line 117; Finsler implication at line 141.

Source label precedes permanent tag above. All three matrix rows previously had bare LEGACY-UNRECONCILED status; historic first visits not asserted.

## Exact uniform chamber

Keep the line convention and notation of §§11.13–14: X=F_e, e>=0, S²=-e, S·f=1, f²=0, L1=O(5S-f), L2=O(-S+(12e+5)f). Let Q=aS+bf be an ample real numerical polarization, so a>0 and b>ea. For algebraic openness below use an integral ample Q (rational classes may be rescaled). For each nonzero extension class xi in H¹(X,O(6S-(12e+6)f)), let V_xi be the corresponding nonsplit extension of L2 by L1.

**Claim.** Every nonsplit extension is mu_Q-stable if and only if
```
(3e+2/3)a < b < (3e+1)a.
```
Every nonsplit extension is mu_Q-semistable if and only if the same two inequalities are non-strict. These are statements quantified over *all* nonzero extension classes; outside the chamber no claim is made that every individual extension is unstable.

Proof. Write delta=mu_Q(V)-deg_Q(L1)=deg_Q(L2)-mu_Q(V)=(9e+3)a-3b. The direct-image calculation of Lemma 11.13.1 gives the effective cone and the identification
```
H¹(X,O(6S-Bf)) = direct sum_{i=0}^6 H¹(P¹,O(-B-ie)), B=12e+6.
```
This uses the vanishing R¹ pi_* and the Leray identification, as in Proposition 11.14.1.

First, multiplication by any nonzero section of O(mS), m>=0, induces an injection
```
H¹(X,O(6S-Bf)) -> H¹(X,O((6+m)S-Bf)).
```
For e>0 the only effective divisor in |mS| is mS: the direct image of O(mS) is O plus strictly negative-degree summands, so its sole section up to scale is the m-th power of the section of S. In the split symmetric-power decomposition this section is the monomial in the O summand (its vanishing locus is S, the lines in O(e)). Multiplication by its m-th power embeds the seven original direct summands identically into the corresponding seven summands in degree 6+m, and hence is injective on H¹. For e=0, the product description identifies the map with multiplication of nonzero homogeneous polynomials in the first P¹ factor tensored with the identity on H¹(P¹,O(-B)); it is injective as in the printed proof. The case m=0 is scalar multiplication.

As in lines 58–60 of Proposition 11.14.1, test rank-one line-bundle subsheaves after taking double duals and extending into the locally free target. A line M mapping into L1 has degree <= deg_Q L1. Otherwise M maps nontrivially to L2, so M=L2(-D) with effective D; D=0 would split the extension. Writing D=mS+nf, m,n>=0, the lift exists exactly when multiplication by the defining section of D kills xi in H¹(X,O(6S-Bf+D)). This is the connecting map in Hom(M,-), or equivalently the pulled-back extension class. The injection above excludes n=0 for every nonzero xi. Hence every lifted D satisfies n>=1 and
```
Q·D=m(b-ea)+na >= a.
```
It follows that all subsheaves have slopes bounded above by the maximum of deg_Q(L1) and deg_Q(L2)-a. This proves the strict assertion if 0<delta<a and the non-strict one if 0<=delta<=a.

For sharpness, L1 itself is a subbundle: delta<=0 obstructs stability, and delta<0 obstructs semistability. For the other wall, fix any fiber F_p and its defining section s in H⁰(O(f)). The multiplication map
```
H¹(X,O(6S-Bf)) -> H¹(X,O(6S-(B-1)f))
```
is a direct sum of seven maps H¹(O(-B-ie)) -> H¹(O(1-B-ie)) on P¹, each having a one-dimensional kernel. Indeed the short exact sequence obtained by multiplication by the base section with a simple zero at p has a one-dimensional skyscraper quotient, while both line bundles have no global sections (B>=6), and the skyscraper has no H¹. Thus the full kernel has dimension seven. Take any nonzero xi in it. Then the map L2(-F_p) -> L2 lifts to V_xi and is injective as a map of sheaves, so its slope is deg_Q(L2)-a. This excludes universal stability when delta>=a and universal semistability when delta>a. At delta=a all extensions are semistable, and these chosen extensions are strictly semistable; at delta=0 all are strictly semistable. Solving for b gives the claimed interval. The original P=4S+(12e+3)f has delta=3 and a=4, strictly within the interval for all e, including e=0. No printed statement is refuted.

## Downstream and proof review

For each fixed integral ample Q in this open chamber, Theorem 11.15.5 and Corollary 11.15.6 admit the same conditional argument with Q instead of P: the proof of Lemma 11.15.3 works with a general positive pair of intersection weights Q·S, Q·f, using upper bounds from kQ-M effective and lower bounds from the slope constraint. The stable prioritary locus is nonempty by the chamber result and Proposition 11.14.2, and the ample prioritary locus is unchanged. Walter's smooth irreducible stack theorem and the original Finsler obstruction remain inputs. This does not assert a common ample bundle stable for every real polarization in the chamber at once.

Direct proof checks:
- §11.13: checked line-projectivization sign, relative canonical class, direct image and very-ampleness argument; c2=65e+26=13H². Rank-drop codimension three exceeds surface dimension. The projective subdivisor incidence has dimension at most three (finite fibers over P³); four independent cubic restrictions on an integral support curve give codimension >=4, so no common curves for general b. Checked the prioritary vanishing via Serre duality and H¹ of the base summands; A1,A2 have the stated intersections -1.
- §11.14: verified the extension dimension 105e+35 and slopes 40e+11,14,17; Hartogs double-dual extension and pullback criterion; fiber splitting and prioritary Hom vanishing; triangular Dolbeault integrability and C^m convergence.
- §11.15: checked flatness/Nakayama, proper support arguments for openness of ampleness, finiteness of potentially destabilizing numerical line classes, density in smooth atlas via openness of the smooth map, smooth parallel transport and dual perturbation -A^T. No implication that the split comparison bundle itself is ample or stable.

Conditional inputs not independently certified here: projective bundle direct-image/base-change and Leray/Künneth, Serre duality/vanishing, proper quasi-finite implies finite, finite pullback of ample is ample, coherent semicontinuity/base change, Walter's prioritary-stack theorem (explicit external input), Corollary 11.12.7. The latter is not reopened as an upstream proof programme. Proposed documentation-only strengthening of 11.14.1 and fixed-polarization variants of 11.15.5–6; no source change. None of these deductions uses the excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme; earlier excluded notes remain deferred-by-user.

Coverage: three whole direct conditional sections, zero new confirmed printed errors, zero demonstrated proof gaps, one new conditional deduction, zero full upstream proof-chain certificates. Current Chapter 11 TOC has 49 sections; existing 747-row matrix retained. No builds, tests, CI, website publication or production edits.
