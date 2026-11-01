# Background positivity in the Di Nezza–Trapani contact identity: missing step and conditional repair

**Audit date:** 2026-11-01. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-NPP-DNT-CONTACT-BACKGROUND-001` — **medium / confirmed proof gap, verified conditional repair proposed (not applied)**.
The stated theorem has **not** been disproved. This report checks a single nonexcluded logical bridge, not the full result or its analytic prerequisites.

## Exact source and integrated anchors

- Reading edition: `docs/sections/non-pluripolar-products--properties-of-non-pluripolar-products/index.html`, production blob `4ace6181d3767e6d5ac3a681c36e392e33b717a2`.
- Theorem **13.13.57**, source `sgpt:CDA82187`, permanent tag `6245F87DD88E`, statement at **line 1167**; mixed contact Eq. **13.13.58**, permanent `F5A7BEAB8003`; same-background reduction Step 2.2 **lines 1285–1293**; general-barrier Step 3 **lines 1295–1315**, specifically the use of Step 2 at **lines 1308–1312**.
- Lemma **13.13.51**, source `sgpt:2ED2C8D7`, permanent `9453F71CEE8F`, lines **1054–1073** (contact second-order equality). Proposition **13.13.50**, source `sgpt:5B387752`, permanent `4BEA034735FD`, lines **1049–1054** (rooftop $C^{1,\bar1}$ regularity). Theorem **13.13.49**, source `sgpt:03EBC438`, permanent `FE0721C3DE01`, lines **1037–1047**, is an *external PDE regularity input* due to Tosatti and Chu–Zhou, not merely historical attribution. Its proof is not provided or verified here.
- Corollary **13.13.61**, permanent tag `77CAD5891555`, lines **1321–1342**, depends on Theorem 13.13.57.

## Precise gap, not a counterexample to the theorem

Step 2 proves the contact identity for $\varphi\le g$ **under the additional hypothesis** that the barrier $g$ itself belongs to $\mathrm{PSH}(X,\theta)$. In Step 3, the proof sets
\[
q=P_{\theta+\omega}(f),\qquad \varphi\le q\le f,
\]
with $\omega>0$ chosen so that $\theta+\omega>0$; then it applies Step 2 to the pair $\varphi,q$ **under background $\theta$**. The available conclusion is only $q\in\mathrm{PSH}(X,\theta+\omega)$, **not** $q\in\mathrm{PSH}(X,\theta)$. Footnote 8 at **line 1318** explicitly acknowledges that $q$ need not be $\theta$-psh, but does not supply the missing bridge. Hence “However, Step 2 implies” is not justified as printed.

There is a concrete failure of this *premise*. Take $X=\mathbb P^1$, $\theta=0$, $\varphi=0$, and let $\omega$ be Fubini–Study. Choose a nonzero smooth nonnegative bump $b$ supported in a proper coordinate disk, and fix $\varepsilon>0$ small enough that $\omega+dd^c(\varepsilon b)\ge \frac12\omega$. For $f=\varepsilon b$, one has
\[
q=P_\omega(f)=f,\qquad q\notin \mathrm{PSH}(X,0),
\]
since a nonconstant smooth subharmonic function cannot exist on the compact connected $\mathbb P^1$. Nonetheless $\{\varphi=q\}$ contains the nonempty open set $X\setminus\operatorname{supp}b$. This is **not a counterexample** to the contact identity; it demonstrates precisely why the printed application of Step 2 is invalid.

## Verified conditional replacement for Step 3

Retain $q=P_{\theta+\omega}(f)$ and put $C=\{\varphi=q\}$. By the already cited envelope $C^{1,\bar1}$ regularity (Proposition 13.13.50, which is conditional here on the external Theorem 13.13.49), the bounded-coefficient top exterior power $(\theta+dd^cq)^n$ is defined **as a signed measure** even without $\theta$-positivity of $q$.

For every $t\ge1$ put $\theta_t=\theta+t\omega$. This is Kähler, and
\[
\begin{aligned}
\theta_t+dd^c\varphi
&=(\theta+dd^c\varphi)+t\omega\ge0,\\
\theta_t+dd^cq
&=(\theta+\omega+dd^cq)+(t-1)\omega\ge0.
\end{aligned}
\]
Moreover $\varphi\le q$. **All assumptions of Step 2 now hold** for $\varphi,q$ in the background $\theta_t$, so its conclusion gives equality of measures on the **same fixed Borel contact set** $C$:
\[
{\bf1}_C\left\langle(\theta+dd^c\varphi+t\omega)^n\right\rangle
=
{\bf1}_C(\theta+dd^cq+t\omega)^n,
\qquad t\ge1. \tag{1}
\]
The left side is a polynomial in $t$ with measure coefficients, by multilinearity of non-pluripolar products with the fixed smooth positive factor $\omega$. The right side is a polynomial with signed measure coefficients, since $dd^cq$ has bounded coefficients. Pairing with any smooth test function gives two real polynomials of degree at most $n$ agreeing on an interval; hence they agree identically. **After this polynomial extension**, evaluation at $t=0$ yields
\[
\boxed{
{\bf1}_C\left\langle(\theta+dd^c\varphi)^n\right\rangle
={\bf1}_C(\theta+dd^cq)^n.} \tag{2}
\]
No assertion that $\theta+dd^cq\ge0$ or that the right side is a non-pluripolar positive measure is made or needed. Equation (2) is the precise intermediate identity missing from the original Step 3.

Since $\varphi\le q\le f$, the smaller contact set is
\[
\{\varphi=f\}=\{\varphi=q=f\}\subset C\cap\{q=f\}.
\]
On $\{q=f\}$, Lemma 13.13.51 applied to the regular envelope $P_{\theta+\omega}(f)$ gives equality almost everywhere of the second-order jets of $q$ and $f$. Their bounded-coefficient exterior powers therefore agree when restricted to this set, and restricting (2) gives the desired common-background scalar identity **13.13.59**. The original Step 1 then polarizes to the mixed identity **13.13.58**.

This is a **complete repair of the identified background-mismatch inference**, conditional on the printed Step 2, non-pluripolar multilinearity, and the stated envelope regularity. It is **not** a self-contained proof of Theorem 13.13.57 nor its external PDE input. The general theorem is not shown false.

## External dependencies, exclusions, dependents and coverage

Theorem 13.13.49 explicitly quotes Tosatti/Chu–Zhou $C^{1,1}$ envelope regularity, used downstream via Proposition 13.13.50 and Lemma 13.13.51; this is a **genuine unproved external input**. Preserve the historical attributions and exact permanent/source tags. Theorem 13.13.57 Step 2.1 (around **lines 1220–1230**) uses a decreasing smooth approximation of a psh potential. **No part of that approximation is examined or completed**; the entire Demailly approximation/regularization and dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remains **deferred-by-user**, not certified or resolved. No attempt to use the repair above to reopen that programme is made.

**Affected dependents:** Theorem 13.13.57 (tag `6245F87DD88E`), Eq. 13.13.58 (tag `F5A7BEAB8003`), Corollary 13.13.61 (tag `77CAD5891555`), and further uses of their contact-set measure formula. Proposed production change: replace Step 3's unsupported Step 2 invocation at lines **1308–1312** by (1)–(2). This is **only a proposed separately reviewable patch**: do not edit production body, source, canonicalization, tags, registry, website, or `main`.

**Actual review coverage:** first targeted proof review of **13.13.57 Step 3** within previously **partially reviewed** §13.13; Step 2.2 and 13.13.49–51 were checked only for dependency applicability. No full theorem/section/transitive proof certificate is claimed. The current collection inventory remains **25 chapters / 747 numbered sections / zero completely mathematically certified sections**. No tests, project build, CI, formal verification, or website publication were run.
