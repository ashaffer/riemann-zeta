# Breadth synthesis: edge-defect no-go and the center-density adapter

Date: 2026-08-31

Preflights:
[`zeta23_edge_defect_synthesis_preflight_v1.json`](context/zeta23_edge_defect_synthesis_preflight_v1.json),
[`zeta23_center_density_adapter_preflight_v1.json`](context/zeta23_center_density_adapter_preflight_v1.json)

Exact ledger:
[`center_density_adapter.py`](../src/center_density_adapter.py)

Hostile-audit addendum:
[`ZETA23-CENTER-DENSITY-HOSTILE-FALSIFICATION-2026-08-31.md`](ZETA23-CENTER-DENSITY-HOSTILE-FALSIFICATION-2026-08-31.md)

The addendum supersedes the route-priority assessment below.  It preserves
the conditional set-intersection adapter, with two quantitative repairs, but
gives a prime-density pseudo-node countermodel to the hoped-for soft coupling
between source coherence and radialization.  Neither actual-prime open input
is thereby refuted.

## Verdict

The broad synthesis changed the decision tree, but it did not prove either
open strip input.

The proposed edge-defect breakthrough is false at the advertised level of
generality.  Harmonic analysis, probability, additive combinatorics, and the
closest analytic-number-theory estimates all locate the same obstruction:
two local vanishing moments are low-frequency information, whereas even a
twin-prime log gap has phase diameter

\[
 Y^{50/33}\frac{2}{Y}=2Y^{17/33}
\]

at the top of the band.  A wavelet or Peano argument therefore spends back
its derivatives, and a hostile half-grid retains a unit high-frequency peak.
Actual cancellation among unequal products remains indispensable.

The positive result comes from changing the quantifiers.  A hypothetical
zero does not supply one unrelated bad center: Turan localization supplies
one fixed interval sum at one fixed ordinate, and that same sum is negatively
aligned at a positive density of eligible half-integer centers.  Therefore
uniform-in-center DPA is stronger than the contradiction needs.

More precisely, the current averaged fourth-moment exponent permits an upper
exceptional set of size

\[
 N^{1-3137/520000+o(1)}.
\]

It is enough for source-conditioned radialization to succeed on more than
that many phase-aligned centers.  This gives a new coupled center-density
adapter and replaces two uniform center quantifiers by a strict comparison of
two exceptional-set exponents.

The averaged fourth moment and the density radialization theorem are both
open.  Consequently the uniform strip and RH remain open.

---

## 1. Quantitative replication of one Turan witness

Let \(\mathcal J_N\) be the half-integers in an interval of length
\(\gg N\) contained in \([N,CN]\).  Let

\[
 N^{1/2}\le \tau\le N^{A'},\qquad A'<2.
\]

For \(1\le h\le H=N^\eta\), van der Corput's second-derivative estimate
applied to \(h\tau\log(m+1/2)\) gives

\[
 \left|\sum_{m+1/2\in\mathcal J_N}
 e^{ih\tau\log(m+1/2)}\right|
 \ll \sqrt{h\tau}+\frac{N}{\sqrt{h\tau}}.             \tag{1.1}
\]

Erdos--Turan therefore gives the normalized phase discrepancy

\[
 D_N\ll N^{-\eta}
       +N^{(A'+\eta)/2-1}
       +N^{-1/4}.                                     \tag{1.2}
\]

Balancing the first two exponents at

\[
 \eta=\frac{2-A'}{3}
\]

proves

\[
 D_N\ll N^{-\delta(A')},\qquad
 \delta(A')=\min\left(\frac{2-A'}3,\frac14\right).  \tag{1.3}
\]

Thus \(\delta(1)=1/4\) for the benchmark Turan aperture used by the
width-\(10^{-6}\) chain, while
\(\delta(50/33)=16/99\) even at the full project aperture.

Now fix the interval sum

\[
 S_I=\sum_{p\in I}p^{-i\tau}.
\]

The centers that place \(I\) inside their logarithmic shell contain such an
interval \(\mathcal J_N\).  For every fixed \(0<\kappa<1\), (1.3) implies

\[
 \begin{aligned}
 &\#\left\{Y\in\mathcal J_N:
 \Re(Y^{i\tau}S_I)\le-\kappa|S_I|\right\}\\
 &\quad=\left(\frac{\arccos\kappa}{\pi}
       +O(N^{-\delta(A')})\right)\#\mathcal J_N.     \tag{1.4}
 \end{aligned}
\]

At \(\kappa=3/4\), the limiting fraction is

\[
 \frac{\arccos(3/4)}{\pi}=0.2300534561\ldots.        \tag{1.5}
\]

This is the fraction of the eligible center interval, not of every center in
a length-\(N\) block.  If the partitioned Turan interval is
\([a,b]\subset[N,2N]\) with \(b/a\le e^{w/2}\), then its eligible interval
satisfies

\[
 \#\mathcal J_N\ge(e^w-1)N-O(1).                    \tag{1.5a}
\]

Consequently at \(w=1/5\) and \(\kappa=3/4\), the uniform absolute lower
density is \(0.0509344697\ldots+o(1)\) relative to \(N\).

This strengthens the previously recorded existence form of half-integer
phase coverage to a quantitative count.  It is an elementary
project-proved lemma, not a claim of literature-level novelty.

Because

\[
 \sum_{p\in I}\cos(\tau\log(p/Y))
 =\Re(Y^{i\tau}S_I),                                 \tag{1.6}
\]

one Turan witness produces \(\gg_w N\) legal negative source events with the
same interval and ordinate.  Constants such as \(3/4\) are absorbed by the
strict power margins in the existing Turan adapter.

---

## 2. Averaged fourth moment gives a center-count upper bound

For a half-integer center \(Y\), let \(F_Y\) be the normalized retained-hat
prime polynomial from the frozen GCG4 branch, and put

\[
 I_Y=\int_{Y^{839/1000}}^{2Y^{50/33}}|F_Y(t)|^4\,dt. \tag{2.1}
\]

The already-audited persistence argument says that a pointwise upper-antenna
failure of depth \(Y^{-c_0}\) costs

\[
 I_Y\gg Y^{-(9/2)c_0}.                               \tag{2.2}
\]

Suppose only the center average, not the pointwise GCG4 theorem, were known:

\[
 \frac1{\#\mathcal Y_N}\sum_{Y\in\mathcal Y_N}I_Y
 \ll N^{-\gamma+o(1)},                              \tag{2.3}
\]

where \(\mathcal Y_N\) is a fixed-factor block of half-integer centers.
Markov's inequality and (2.2) give

\[
 \#\mathcal E_N(c_0)
 \ll N^{1-\gamma+(9/2)c_0+o(1)},                    \tag{2.4}
\]

where \(\mathcal E_N(c_0)\) is the set on which the fixed-hat DPA upper
certificate fails.

Use the safely licensed fixed-hat exponent strictly below the open endpoint:

\[
 \gamma=\frac{1187}{13000},\qquad
 c_0=\frac{379}{20000}=.01895<.019.
\]

the center saving is exactly

\[
 m=\gamma-\frac92c_0
  =\frac{3137}{520000}=0.0060326923\ldots.           \tag{2.5}
\]

Hence averaged GCG4 would prove fixed-hat DPA outside at most

\[
 N^{1-m+o(1)}=N^{0.9939673\ldots+o(1)}              \tag{2.6}
\]

centers.  This is stronger than merely saying "density one" and exposes the
amount of lower-return replication actually needed.

---

## 3. The center-density intersection theorem

Let \(\mathcal W_N\) be the phase-aligned witness centers in (1.4).  Suppose
the following two presently open inputs hold along every Turan witness:

1. the averaged fourth moment (2.3) with exponent \(\gamma\);
2. source-conditioned prime radialization succeeds on a set
   \(\mathcal R_N\subseteq\mathcal W_N\) satisfying

\[
 \#\mathcal R_N\gg N^{1-\rho-o(1)},                 \tag{3.1}
\]

and gives \(r_P(H_Y)\ge N^{-c_{\rm rad}+o(1)}\) there.

If

\[
 c_0>c_{\rm rad},\qquad
 \rho<\gamma-\frac92c_0,                            \tag{3.2}
\]

then \(\mathcal R_N\) cannot be contained in the exceptional set (2.4).
For some common center \(Y\), radialization gives

\[
 r_P(H_Y)\ge N^{-c_{\rm rad}+o(1)},                 \tag{3.3}
\]

while the retained-hat antenna gives

\[
 r_P(H_Y)\le N^{-c_0+o(1)}.                         \tag{3.4}
\]

The strict first inequality in (3.2) makes (3.3)--(3.4) incompatible for
large \(N\).  The audited Turan contrapositive then excludes the
hypothetical zero.

At the project values

\[
 c_0=.01895,\qquad c_{\rm rad}=.0189,\qquad
 \rho<\frac{3137}{520000},                          \tag{3.5}
\]

is sufficient.  Uniform centerwise LTRAD corresponds to \(\rho=0\), but is
far stronger than necessary: it is enough to obtain the lower return on, for
example, \(N^{.995}\) of the \(\gg N\) phase-aligned centers.

The exact nonasymptotic pigeonhole condition behind (3.2) is simply

\[
 \#\mathcal R_N
 > C N^{(9/2)c_0}\sum_{Y\in\mathcal Y_N}I_Y.        \tag{3.6}
\]

This is the cleanest statement of the new architecture: it couples the two
old locks by comparing their bad-center budgets.  A scale-global LTRAD
theorem that produces one unspecified large-radius center does not suffice;
that center could lie in \(\mathcal E_N(c_0)\).

---

## 4. Why center averaging is not a free conductor gain

The quantifier weakening is real, but the analytic theorem does not follow
formally from averaging.

Write \(y=\log Y\), \(x_j=\log p_j\),
\(d_j=x_{j+1}-x_j\), and \(g_j=p_{j+1}-p_j\).  An edge is retained precisely
when

\[
 y\in J_j=
 \left[\max\left(x_{j+1}-w,\frac{\log g_j}{\theta}\right),
 x_j+w\right].                                      \tag{4.1}
\]

Let \(c_j(y)\) be the exact sum of the two retained barycentric edge shares
incident to \(p_j\), and \(A(y)=\sum_jc_j(y)\).  Then exactly

\[
 F_y(t)=e^{-ity}A(y)^{-1}\sum_jc_j(y)e^{itx_j}.      \tag{4.2}
\]

The global center phase disappears from \(|F_y(t)|^4\).  Integrating in
\(y\) therefore gives nonnegative overlap coefficients

\[
 C_{prqs}=\int W(y)A(y)^{-4}c_p(y)c_r(y)c_q(y)c_s(y)\,dy              \tag{4.3}
\]

multiplying the same kernel in \(\log(pr/qs)\).  No new oscillatory
variable appears.

Even if the top window is scaled with \(Y\), the kernel has phase
\(e^{(50/33)y}\log(pr/qs)\).  On the critical determinant tube
\(|pr-qs|\asymp Y^{16/33}\), both that phase and its \(y\)-derivative are
of order one.  Integration by parts in the center therefore gives no power
of \(Y\).  A scale-covariant half-grid also defeats the averaged statement
if one uses only density, gaps, positivity, and the two edge moments.

Thus the averaged theorem is strictly weaker in quantifiers, but still needs
actual multiplicative arithmetic.  Averaging does not manufacture the
missing \(3/8\) conductor saving.

### 4.1 Positive mixtures do not bypass radialization

A tempting stronger shortcut is to mix the canonical antennas over the
phase-aligned centers and hope to reconstruct the uniform prime measure on
the Turan interval.  The exact partition-of-unity calculation rules this
out.

If the center mixture is weighted by raw retained mass, then averaging with
respect to \(dy=d\log Y\) assigns a prime a weight proportional, in the
unretained benchmark, to the sum of its adjacent log gaps.  Averaging with
respect to \(dY\) assigns physical-gap/Voronoi weights.  Neither average is
counting measure.  Retention adds the next-prime gap indicator rather than
flattening it.

There is also unavoidable leakage.  The Turan interval has logarithmic
length at most \(w/2\), whereas every eligible antenna occupies a shell of
width \(2w\).  Each component has positive mass outside the source interval,
so a positive mixture cannot reproduce a measure supported on that interval.
Even a hypothetical domination

\[
 \overline\nu\ge c_wN^{-1}\sum_{p\in I}\delta_p     \tag{4.4}
\]

would not preserve the sign: the positive remainder has total mass of order
one and can contribute positively at the source ordinate, overwhelming a
negative event of depth only \(N^{-.001}\).  Finally, each centered antenna
uses its own phase \(e^{-i\tau y}\), so arbitrary positive mixing does not
preserve a common linear functional.

Thus partition of unity gives a mass comparison, not the sign-sensitive
directional-to-radial return.  It cannot eliminate the lower gate.

---

## 5. What the three external mathematical languages actually say

### 5.1 Harmonic analysis: exact Peano saturation

For an edge \(e=[a,b]\), \(d=b-a\), define its exact defect

\[
 D_e=\alpha_e\delta_a+\beta_e\delta_b
       -\phi(u)1_{[a,b]}(u)\,du.
\]

There is a nonnegative compactly supported Peano kernel \(G_e\) with

\[
 D_e=G_e'',\qquad
 \widehat D_e(t)=-t^2\widehat G_e(t),\qquad
 |\widehat D_e(t)|
 \le m_e\min\left(2,\frac{(td)^2}{8}\right).        \tag{5.1}
\]

For constant \(\phi\), the exact multiplier is proportional to

\[
 \cos(td/2)-\operatorname{sinc}(td/2),              \tag{5.2}
\]

which saturates rather than decays when \(td\gg1\).

The edge interiors are disjoint, so

\[
 \int_{\mathbb R}
 \frac{|\sum_e\widehat D_e(t)|^2}{t^4}\,dt
 =2\pi\sum_e\|G_e\|_2^2.                           \tag{5.3}
\]

With the recorded gap moments, the resulting band-\(L^2\) exponent at
\(t=Y^a\) is

\[
 4(a-(1-\theta))-s.                                 \tag{5.4}
\]

It saves at the transition \(a=1-\theta\) but becomes
\(2.685\ldots\) at \(a=50/33\).  Hausdorff--Young is worse.  Moreover,

\[
 |\widehat{\sum D_e}(t)|^4
 =t^8|\widehat{G*G}(t)|^2,                          \tag{5.5}
\]

so almost orthogonality of the edge convolutions is exactly separation of
edge-sum locations at \(1/t\) resolution: the original balanced-semiprime
near-collision problem has merely reappeared.

### 5.2 Probability and additive combinatorics: degeneracy is insufficient

Barycentrically round a continuum point \(U\) in its edge to an endpoint
\(X\), so \(\mathbb E[X\mid U]=U\).  For
\(K_J(x)=\int_J e^{itx}\,dt\), the fourth moment has the exact form

\[
 I_J=\mathbb E[\Delta_1\Delta_2\Delta_3\Delta_4
 K_J(U_1+U_2-U_3-U_4)].                             \tag{5.6}
\]

Each difference annihilates affine functions, but four Peano steps give only
\(I_J\ll T^9D_2^4\).  At the top project scale this has exponent
\(6.8477\ldots\), so the derivative cost overwhelms the cancellation.

Worse, a perturbed odd half-grid can simultaneously have prime-scale mesh,
the exact zero and first moments, \(S_2=Y^{-1+o(1)}\), and distinct unordered
pair sums, while retaining \(|\widehat D(B)|=1-o(1)\).  Therefore local
moments plus even exact Sidon uniqueness do not imply any fixed conductor
gain.  Quantitative clustering of unequal products is the relevant datum.

### 5.3 Analytic number theory: the selector, not the modulus, is the wall

At the natural delta-method modulus \(Q=B^{1/2}=Y^{25/33}\), a nonzero mode
already varies across a twin-prime edge by \(\gg Y^{8/33}\).  The local
moments therefore cancel only the zero/affine modes, which belong to sectors
already controlled by the one-prime mean-value theorem.

The closest trilinear Kloosterman estimate,
[Bettin--Chandee](https://arxiv.org/abs/1502.00769), would give only a formal
\(Y^{-27/220}\) saving in a friendlier coefficient class, short of
\(Y^{-3/8}\) by \(111/440\).  More importantly, it accepts only two arbitrary
coefficient slots; the remaining factors must be smooth.  The exact
next-prime selector couples all four slots and cannot be replaced at top-band
phase accuracy.  The numerical comparison is therefore a benchmark, not an
imported proof.

### 5.4 Almost-all and variational theorems: the averaging variable is wrong

The closest current almost-all input is Theorem 1.8 of
[*Higher Uniformity of Arithmetic Functions in Short Intervals II*](https://arxiv.org/abs/2411.05770).
With \(M=Y^2\), our determinant window has length
\(H=M^{8/33}\), and the desired conductor gain is
\(M^{-3/16}\).  That theorem instead treats a modelled divisor discrepancy,
with an exceptional set measured among all \(M\) additive interval starts.
It does not accept the factor-level predecessor/successor weights in

\[
 a_{m,Y}=\sum_{pq=m}\lambda_{p,Y}\lambda_{q,Y}.       \tag{5.7}
\]

Even after a fictitious coefficient transfer, its stated power saving is at
most \(M^{-1/300000+o(1)}\), far short of \(M^{-3/16}\).  Its exceptional set
may also contain every sampled square \(M=Y^2\), since there are only
\(M^{1/2}\) shell centers.

Variational prime averages such as
[Mirek--Trojan--Zorin-Kranich](https://arxiv.org/abs/1410.3255) control changes
in a cutoff for natural prime convolution operators; they give boundedness,
not fixed-power smallness, and they do not recompute adjacent-gap weights as
the center moves.  The
[Lewko--Lewko variational large sieve](https://arxiv.org/abs/1111.6190)
accepts arbitrary coefficients and consequently retains the generic
conductor term.  The current literature therefore supplies no theorem in the
required shell-center variable.

---

## 6. Corrected decision tree

```text
hypothetical near-one zero
        |
        v
one Turan interval I and one common ordinate tau
        |
        v
positive-density phase-aligned center set W_N                 PROVED
        |
        +-- averaged retained-hat GCG4
        |       -> upper failure set size <= N^(1-m+o(1))     OPEN
        |
        `-- event-conditioned radialization on
                >= N^(1-rho-o(1)) centers, rho<m              OPEN
                         |
                         v
               the two center sets intersect
                         |
                         v
               fixed near-one zero-free strip                 CONDITIONAL

strip-to-critical-line amplifier                              NOT AVAILABLE
RH                                                             OPEN
```

The real synthesis is not a new disguise for GCG4 or LTRAD.  It identifies
the information discarded by the old formulation: a zero reuses one
ordinate and one prime interval coherently across many scales.  The correct
remaining object is therefore a coupled center-count inequality such as
(3.6), not two unrelated uniform theorems.

## Status ledger

| Statement | Status |
|---|---|
| Quantitative half-integer phase count (1.4) | **PROJECT-PROVED** |
| Center exceptional-count implication (2.4) | **PROJECT-PROVED, conditional on the displayed averaged moment** |
| Center-density intersection theorem (3.2) | **PROJECT-PROVED CONDITIONAL ADAPTER** |
| Two-moment edge-defect route alone | **REFUTED WITH SCOPE** |
| Positive center-mixture reconstruction of the source | **REFUTED WITH SCOPE** |
| Averaged retained-hat GCG4 | **OPEN** |
| Event-conditioned density radialization | **OPEN** |
| Uniform zero-free strip | **OPEN** |
| RH | **OPEN** |
