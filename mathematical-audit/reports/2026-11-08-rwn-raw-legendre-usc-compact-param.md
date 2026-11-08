# Raw Legendre transforms: a direct compact-parameter upper-semicontinuity proof

**Finding ID:** POME-RWN-RAW-LEGENDRE-USC-COMPACT-001. **Severity:** low. **Classification:** verified repair **proposed only** (an optional, shorter internal proof of an existing correct result; not a confirmed false statement or proof gap). The alternative is completely justified from the cited current internal hypotheses, without the original pluripolar exceptional-set/Kiselman/biconjugacy circuit.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated proof under review:** `docs/sections/test-curves--ross-witt-nystrom-correspondence/index.html` (blob `bdfe4175ffeeb4d1b3decf4dbaace0738c4c2b09`), **Lemma 17.13.7**, source `sgpt:27709055`, permanent tag `BC74B8EA334F`, physical lines **60–117**, especially the original proof lines **66–115**. The forward-transform definition **17.13.1 / 17.13.2**, source `sgpt:236F4C37` / `sgpt:236BD41E`, permanent tags `2105331E66C7` / `22C9794122C8`, is at lines **13–24**. Context `docs/sections/test-curves--the-notion-of-test-curves/index.html` (blob `6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7`): **Definition 17.12.1**, source `sgpt:ECCF19D5`, permanent `C8399F09D86D`, lines **10–36**; cutoff **Remark 17.12.3**, source `sgpt:FCDC9660`, permanent `3D73AB2E32CB`, lines **42–48**; left-continuity identity **(17.12.5)**, source `sgpt:07C41068`, permanent `5EFADBE6069E`, lines **71–78**. Chapter-17 TOC section tag for 17.13: `C9D15D724069`.

## Exact statement and conditional prerequisites

Let (X) be compact Kähler, (	heta) a smooth closed real ((1,1))-form in a big class, and (Gammainmathrm{TC}(X,	heta;phi)) a test curve as in 17.12.1. Write (c=Gamma_{max}inmathbb R). For (	au<c), (Gamma_	auinmathrm{PSH}(X,	heta)), (Gamma_	aule0), and (Gamma_	au) decreases in (	au). The **pointwise** left-order continuity in (17.12.5) and the cutoff convention in 17.12.3 say
[
Gamma_{	au_0}(x)=inf_{sigma<	au_0}Gamma_sigma(x)quad(	au_0<c),
qquad
Gamma_c(x)=inf_{sigma<c}Gamma_sigma(x).
	ag{1}
]
Do not silently replace either equality by almost-everywhere agreement; (1) is precisely the stated internal result under use. Define for (t>0)
[
F(x,t)=sup_{	au<c}{Gamma_	au(x)+t	au}
       =sup_{	aule c}{Gamma_	au(x)+t	au}.
	ag{2}
]
The equality follows by (1), including the possibility of a value (-infty). **Claim:** (F) is jointly upper semicontinuous on (X	imes(0,infty)). Consequently (F(x,operatorname{Re}z)) is (pi_X^*	heta)-psh on the right half-plane product, and every slice (F(cdot,t)) is (	heta)-psh. The latter is exactly Lemma 17.13.7.

## Proof: joint upper semicontinuity of the indexed family

Extend the family at (	au=c) by (1). Consider ((x_j,	au_j)	o(x_0,	au_0)), with (	au_j,	au_0le c). For each fixed (sigma<	au_0), eventually (	au_j>sigma), so monotonicity gives
[
Gamma_{	au_j}(x_j)le Gamma_sigma(x_j).
]
Upper semicontinuity of the fixed (	heta)-psh potential (Gamma_sigma) yields
[
limsup_jGamma_{	au_j}(x_j)leGamma_sigma(x_0).
]
Taking the infimum over (sigma<	au_0) and applying (1) proves
[
limsup_jGamma_{	au_j}(x_j)leGamma_{	au_0}(x_0).
	ag{3}
]
This works even when the right side is (-infty), at the cutoff, and at points in the common pluripolar locus. In particular ((x,	au)mapsto Gamma_	au(x)+t	au) is jointly upper semicontinuous for (	aule c), locally uniformly for (t) varying in compact subsets of ((0,infty)).

## Proof: compact truncation and uniformly negative tails

Fix ((x_0,t_0)) and a neighborhood where (0<arepsilonle tle T). Choose (M) large enough that (-M<c), and put
[
 F_M(x,t)=sup_{-Mle	aule c}{Gamma_	au(x)+t	au}.
]
The parameter interval is **compact** and the summands are jointly upper semicontinuous by (3). Therefore (F_M) is upper semicontinuous: for a convergent sequence of ((x,t)), choose maximizing (or asymptotically maximizing) parameters in this compact interval and extract a convergent subsequence; if all values are (-infty), the claim is immediate. No sequential compactness is asserted of any infinite-dimensional function space, only of this real compact interval.

For the omitted tail, (Gamma_	aule0) and (tgearepsilon) give uniformly
[
 sup_{	au<-M}(Gamma_	au(x)+t	au)le-arepsilon M.
]
Hence throughout the fixed neighborhood
[
 F_M(x,t)le F(x,t)lemax{F_M(x,t),-arepsilon M}.
]
For any ((x_j,t_j)	o(x_0,t_0)), usc of (F_M) gives
[
 limsup_jF(x_j,t_j)
 le max{F_M(x_0,t_0),-arepsilon M}
 le max{F(x_0,t_0),-arepsilon M}.
]
Let (M	oinfty) to obtain (limsup_jF(x_j,t_j)le F(x_0,t_0)), **including the case (F(x_0,t_0)=-infty)**. This proves the joint usc assertion without interchanging limits. It is stronger than merely concluding usc almost everywhere or for each fixed (t).

## Plurisubharmonicity, and exact dependency reduction

On (X	imesmathbb H), (mathbb H={z:operatorname{Re}z>0}), each
[
 (x,z)longmapstoGamma_	au(x)+	auoperatorname{Re}z
]
is (pi_X^*	heta)-psh: the second summand is pluriharmonic. The family is locally uniformly bounded **above** because (Gamma_	aule0), (	au<c), and (operatorname{Re}z) lies in a compact positive interval. The upper envelope of a locally upper-bounded family of quasi-psh functions is quasi-psh **after** usc regularization; here the raw upper envelope already is usc, by the proof above. Thus (F(x,operatorname{Re}z)) is (pi_X^*	heta)-psh (not identically (-infty), since a test-curve member is not identically (-infty)). Restriction to (X	imes{t}) proves (Gamma_t^*=F(cdot,t)inmathrm{PSH}(X,	heta)).

The only substantive internal analytic dependencies are the psh status/usc of members, their normalization (Gamma_	aule0), and the **pointwise** left-continuity (17.12.5); the customary elementary locally bounded psh upper-envelope theorem is also invoked. In contrast to the printed proof, the argument does **not** invoke exceptional-set pluripolarity 5.14.5, Kiselman's minimum principle 5.14.15, a Fubini exceptional-set argument, uniqueness by almost-everywhere psh equality 5.14.6, or the final conjugacy 21.11.26 **for this lemma**. It does not remove those inputs where other theorems need them.

## Disposition, context, and unreviewed dependencies

**Proposed optional edit** (never applied here): replace only the proof of Lemma 17.13.7 with (3) and compact-tail estimates, retaining theorem text, source attribution, tags, and other versions. The printed lemma is correct; this is **not** evidence of a false statement or an unjustified original limit. The general upper-envelope principle and the full proof chain of 17.12.5 were consulted as internal input, **not transitively certified**. Immediate mathematical dependents include **Corollary 17.13.9** (its proof invokes 17.13.7, lines 119–141) and the subsequent Ross–Witt Nyström correspondence; those dependents are not fully verified by this replacement. The earlier independent `POME-RWN-POLE-QUANTIFIER-001` proof-gap finding in the wider §17.13 chain is **unchanged**.

**Actual coverage:** direct statement and all proof lines 60–117 of 17.13.7; forward transform and cutoff conventions 17.13.1–2, 17.12.1/.3 and (17.12.5); statement and immediate invocation in 17.13.9. §17.13 had previous selected visits, so **0 newly first-visited sections / 0 complete mathematical-section certifications**. TOC baseline remains **25 chapters / 747 numbered sections / 0 complete sections**. The excluded Demailly approximation/regularization, dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme remains **deferred-by-user**, not resolved. No tests/build/CI/formal verification or website release in this mathematical derivation.
