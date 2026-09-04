# ZETA23 per-zero universality replication and principal-mode gate

Date: 2026-08-12.

## Status and verdict

Assume that one zero

\[
\rho _0=\beta+i\gamma _0,
\qquad \beta>1-\delta,
\tag{0.1}
\]

exists.  Full self-recurrence of `zeta` on a small circle about `rho_0`
would indeed replicate that zero.  Guth--Maynard then gives the sharp
power target for this strategy: more than

\[
T^{(30/13)\delta+o(1)}
\tag{0.2}
\]

recurring shifts would be enough.  In particular, to exclude
`beta>.99` it would be enough to produce more than

\[
T^{3/130+o(1)}=T^{0.0230769\ldots+o(1)}
\tag{0.3}
\]

replicas.

No known universality theorem produces that event.  The obstruction is
not merely an ineffective constant:

1. a connected-complement universality compact either omits part of the
   enclosing Jordan curve or contains its whole interior, including the
   prescribed zero;
2. a slit removes exactly the cycle whose winding would imply a zero;
3. closing a slit of length `ell` forces either a replicated zero or a
   derivative/logarithmic-derivative spike of order `1/ell`;
4. universality of `zeta^(k)` forgets exactly a polynomial of degree
   `k-1`.  For `k=1`, the missing scalar is

   \[
   C_\tau=\zeta(\rho _0+i\tau).
   \tag{0.4}
   \]

   Controlling this scalar together with derivative recurrence restores
   full self-recurrence and is therefore bounded by the same
   Guth--Maynard exponent.

This report proves the quantitative replication, topology, slit-debt, and
principal-jet statements precisely.  It audits ordinary, strong, hybrid,
derived, and truncated-Euler universality against them.  It does **not**
prove a fixed zero-free strip, nor does it prove that no fixed strip
exists.

The main new consolidation is the exact sequence

\[
0\longrightarrow {\cal P}_{k-1}
 \longrightarrow {\cal O}(D^\circ)
 \mathop{\longrightarrow}^{d^k/ds^k}{\cal O}(D^\circ)
 \longrightarrow 0.
\tag{0.5}
\]

Derived universality acts after the last arrow.  Zero divisors do not
descend through that quotient.  The lost `P_(k-1)` jet is the analytic
version of the winding lost when a Jordan contour is slit.

## 1. Exact normalization and the Guth--Maynard threshold

Choose `r>0` so that the closed disc

\[
D=\{s:|s-\rho _0|\leq r\}
\tag{1.1}
\]

lies in `1/2<Re(s)<1`, contains no zero other than `rho_0`, and has no zero
on its boundary `Gamma`.  Let `j` be the multiplicity of `rho_0`, and put

\[
m=\min_{s\in\Gamma}|\zeta(s)|>0.
\tag{1.2}
\]

For `0<epsilon<m`, define

\[
 A_D(T,\epsilon)=
 \left\{\tau\in[T,2T]:
 \max_{s\in\Gamma}|\zeta(s+i\tau)-\zeta(s)|<\epsilon\right\}.
\tag{1.3}
\]

### Theorem 1.1 -- per-zero replication count

Counting zeros with multiplicity,

\[
j\,\operatorname {meas}A_D(T,\epsilon)
 \leq 2r\,N\!\left(\beta-r;
 T+\gamma _0-r,2T+\gamma _0+r\right).
\tag{1.4}
\]

Moreover, `A_D(T,epsilon)` contains a `2r`-separated subset of cardinality
at least

\[
\frac{\operatorname {meas}A_D(T,\epsilon)}{4r}-1,
\tag{1.5}
\]

and the corresponding translated discs are disjoint.  Thus (1.5) is also
a lower bound, up to the displayed constant, for the number of distinct
replicated zeros, without multiplicity.

#### Proof

Rouche's theorem gives exactly `j` zeros of `zeta(s+i tau)` in `D`, hence
`j` zeros of `zeta` in `D+i tau`.  Therefore

\[
j1_{A_D}(\tau)
 \leq \sum_\rho 1_{\{|\rho-(\rho _0+i\tau)|<r\}}.
\tag{1.6}
\]

Integrating in `tau`, a fixed zero contributes on an interval of length at
most `2r`; every contributing zero has real part at least `beta-r` and
ordinate in the interval in (1.4).  This proves (1.4).  A maximal
`2r`-separated subset has `4r`-neighborhoods covering `A_D`, which proves
(1.5); its translated open discs are disjoint.  QED.

Guth and Maynard prove

\[
N(\sigma,T)\leq T^{30(1-\sigma)/13+o(1)}.
\tag{1.7}
\]

See [Guth--Maynard, *New large value estimates for Dirichlet
polynomials*](https://doi.org/10.4007/annals.2026.203.2.6).  Hence

\[
\operatorname {meas}A_D(T,\epsilon)
 \leq T^{d_r+o(1)},
\qquad
d_r=\frac {30}{13}(1-\beta+r).
\tag{1.8}
\]

Under (0.1), choose additionally

\[
0<r<\beta-(1-\delta).
\tag{1.9}
\]

Then `d_r<(30/13)delta`.  Consequently a lower bound

\[
\operatorname {meas}A_D(T,\epsilon)
 \geq T^{(30/13)\delta-o(1)}
\tag{1.10}
\]

would contradict (1.8).  The strict inequality in (1.9) absorbs both
`o(1)` terms.  This is the precise meaning of target (0.2).

For `delta=1/100`, the target exponent is exactly `3/130`.  Positive
density would be enormous overkill.  The difficulty is not the
zero-density side; it is constructing even the sparse event (1.10).

## 2. The topology audit: fill the zero or break the cycle

### Lemma 2.1 -- connected-complement Jordan dichotomy

Let `Gamma` be a Jordan curve with bounded interior `D`, and let `K` be a
compact subset of the plane containing `Gamma`.  If `C\K` is connected,
then

\[
\overline D\subseteq K.
\tag{2.1}
\]

#### Proof

If `z` belonged to `D\K`, connectedness of the open set `C\K` would give a
path in `C\K` from `z` to a sufficiently distant exterior point.  The
Jordan curve theorem says that this path crosses `Gamma`, contrary to
`Gamma subset K`.  QED.

Classical Voronin universality requires `K` to have connected complement
and its target to be nonvanishing on `K`.  Applied to a contour enclosing
`rho_0`, Lemma 2.1 gives an exact dichotomy:

```text
retain the whole Jordan cycle + connected complement -> include rho_0;
avoid the zero while staying admissible              -> break the cycle.
```

Filling the disc restores connected complement but makes the target
`zeta` vanish.  Keeping only the full boundary avoids the zero but its
complement has two components.  Deleting an open arc makes the complement
connected, but destroys the closed cycle needed by the argument principle.

This also audits annular and keyhole variants.  A planar slit annulus has
connected complement only because a crosscut joins its inner hole to the
outside.  Restoring the missing crosscut restores a nontrivial cycle and
the same winding obstruction.  Treating the two banks of a zero-width slit
as different points moves to a Riemann surface; it is no longer a compact
subset of the plane to which Voronin's theorem applies.

Andersson's empty-interior extension does not change this ledger.  It
allows arbitrary continuous targets on empty-interior compacta, but still
assumes connected complement.  Thus it applies to a proper closed arc,
not to the entire circle.  See [Andersson, *Lavrentiev's approximation
theorem with nonvanishing polynomials and universality of
zeta-functions*](https://arxiv.org/abs/1010.0386), Theorem 2.

### Lemma 2.2 -- zero-free support has a hard boundary gap

If `g` is holomorphic and zero-free in a neighborhood of `D`, then

\[
\max_{s\in\Gamma}|g(s)-\zeta(s)|\geq m.
\tag{2.2}
\]

Indeed, a strict reverse inequality would give `j` zeros of `g` in `D` by
Rouche.  Thus the open recurrence ball required in Theorem 1.1 is
disjoint from every zero-free Euler product, not merely assigned a small
probability by it.

## 3. What a slit really costs

Let `J_ell` be an open subarc of `Gamma` of arclength `ell`, and set

\[
K_\ell=\Gamma\setminus J_\ell,
\qquad
H_\tau(s)=\zeta(s+i\tau)-\zeta(s).
\tag{3.1}
\]

For `0<epsilon<m`, define the punctured recurrence event

\[
U_\ell(T,\epsilon)=
\{\tau\in[T,2T]:\max_{K_\ell}|H_\tau|<\epsilon\}.
\tag{3.2}
\]

For every **fixed** `ell>0`, ordinary universality gives this event positive
lower density: the target is nonzero on the compact arc `K_ell`.  The next
statement identifies where that density must go if `rho_0` exists.

### Theorem 3.1 -- replicated zero or slit derivative spike

Put

\[
M_\ell=\frac{m-\epsilon}{2\ell}.
\tag{3.3}
\]

Then

\[
U_\ell(T,\epsilon)
 \subseteq A_D\!\left(T,\frac{m+\epsilon}{2}\right)
 \cup
 \left\{\tau:\max_{s\in J_\ell}|H_\tau'(s)|>M_\ell\right\}.
\tag{3.4}
\]

Consequently, uniformly for arcs `J_ell subset Gamma`, including arcs
whose length depends on `T`,

\[
\operatorname {meas}U_\ell(T,\epsilon)
 \ll_D T^{d_r+o(1)}
   +\frac{T\ell^2}{(m-\epsilon)^2}.
\tag{3.5}
\]

#### Proof

If the second event in (3.4) fails, integrate `H_tau'` from an endpoint of
the missing arc.  On `J_ell`,

\[
|H_\tau(s)|<\epsilon+M_\ell\ell
 =\frac{m+\epsilon}{2}<m.
\tag{3.6}
\]

The same is already true on `K_ell`, so the first event holds.  This proves
(3.4).

A fixed compact neighborhood of `Gamma` lies in `Re(s)>1/2`.  Cauchy's
estimate on a finite disc cover and the classical second mean value there
give

\[
\int_T^{2T}\max_{s\in\Gamma}|H_\tau'(s)|^2d\tau\ll_D T.
\tag{3.7}
\]

Chebyshev, (1.8), and (3.3) prove (3.5).  QED.

For `beta>.99`, take `r` as in (1.9), so `d_r<3/130`.  To make the
unconditioned derivative exceptional set no larger than the
Guth--Maynard term, (3.5) requires

\[
\ell\leq T^{-(1-d_r)/2+o(1)}
 \leq T^{-127/260+o(1)}.
\tag{3.8}
\]

On a circular contour, hiding one unit of winding in a gap of angular size
`theta asymp ell` requires a polynomial unwinder of degree
`Theta(theta^(-2))`; the sharp capacity calculation is recorded in
[`R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md).
At the scale (3.8), that degree is at least

\[
T^{127/130-o(1)}.
\tag{3.9}
\]

Known effective-universality constructions operate with polylogarithmic
Dirichlet/Euler approximants, not an unwinder of almost linear power
complexity.  Classical universality has no uniform assertion at all when
`ell=ell(T)` shrinks.  This is why replacing positive density by the much
smaller Guth--Maynard target does not close the slit argument.

### Proposition 3.2 -- invariant winding debt

Let `f` and `g` be holomorphic on a neighborhood of `overline(D)` and
nonzero on `Gamma`, suppose `f` has `j` zeros and `g` has no zeros in `D`,
and assume

\[
|g-f|\leq\epsilon<m_f:=\min_\Gamma|f|
\quad\hbox{on }\Gamma\setminus J_\ell.
\tag{3.10}
\]

Then

\[
\int_{J_\ell}
 \left|\frac{g'}g-\frac{f'}f\right|\,|ds|
 \geq 2\pi j-2\arcsin(\epsilon/m_f).
\tag{3.11}
\]

#### Proof

On the retained arc, `q=g/f` lies in the disc
`|q-1|<=epsilon/m_f<1`.  Its argument at any two points differs by at most
`2 arcsin(epsilon/m_f)`.  The winding of `q` around the full curve is
`-j`.  The omitted arc must therefore carry the remaining argument change.
Integrating `q'/q=g'/g-f'/f` gives (3.11).  QED.

Thus any zero-free translate shadowing the long arc must pay the missing
topological degree on the short arc, either by a logarithmic-derivative
spike of order `j/ell` or by approaching zero there.  A teardrop, keyhole,
spiral, or annular slit can move this debt but cannot remove it.

## 4. Derived universality and the missing principal jet

Derivative universality looks initially more promising because targets
for `zeta'` may vanish.  It nevertheless lives in the quotient (0.5).

### Theorem 4.1 -- exact principal-jet gate

For an integer `k>=1`, let

\[
P_{\tau,k-1}(s)
 =\sum_{\nu=0}^{k-1}
   \frac{H_\tau^{(\nu)}(\rho _0)}{\nu!}(s-\rho _0)^\nu.
\tag{4.1}
\]

If

\[
\max_{s\in D}|H_\tau^{(k)}(s)|\leq\eta,
\tag{4.2}
\]

then

\[
\max_{s\in\Gamma}|H_\tau(s)-P_{\tau,k-1}(s)|
 \leq \frac{\eta r^k}{k!}.
\tag{4.3}
\]

Hence the joint event

\[
\max_D|H_\tau^{(k)}|\leq\eta,
\qquad
\max_\Gamma|P_{\tau,k-1}|+\frac{\eta r^k}{k!}<m
\tag{4.4}
\]

is contained in the strict Rouche event
`{tau:max_Gamma |H_tau|<m}` and has measure at most

\[
T^{d_r+o(1)}.
\tag{4.5}
\]

#### Proof

Taylor's formula with integral remainder along the radial segment from
`rho_0` to `s` gives (4.3).  Condition (4.4) gives
`max_Gamma |H_tau|<m`; apply Theorem 1.1.  QED.

For `k=1`, this becomes especially transparent:

\[
P_{\tau,0}=H_\tau(\rho _0)=\zeta(\rho _0+i\tau).
\tag{4.6}
\]

Uniform recurrence of `zeta'` on `D` plus a small value of
`zeta(rho_0+i tau)` replicates the zero.  Therefore

\[
\begin{split}
\operatorname {meas}\{\tau\in[T,2T]:&
 \max_D|\zeta'(s+i\tau)-\zeta'(s)|\leq\eta,\\
 &|\zeta(\rho _0+i\tau)|<m-\eta r\}
 \leq T^{d_r+o(1)}.
\end{split}
\tag{4.7}
\]

Equation (4.7) is the requested unavoidable **principal mode**.  It is one
complex scalar, but known derived universality does not control it.

### 4.2 Why strong universality of `zeta'` does not help

The derivative is strongly universal on discs in the usual strip.  This
can be seen directly from ordinary universality, without importing a
joint-value theorem.  Given a holomorphic target `g` on a slightly larger
disc, choose an antiderivative `G` and then a constant `C` so large that
`G+C` is nonvanishing.  Voronin approximates `G+C` by shifts of `zeta` on
the larger disc, and Cauchy's formula shows that the corresponding shifts
of `zeta'` approximate `g` on the smaller disc.  This is also within the
scope of [Meyrath, *On the universality of derived functions of the
Riemann zeta-function*](https://doi.org/10.1016/j.jat.2011.05.004).

For the recurrence target `g=zeta'`, take the primitive `G=zeta`; the
nonvanishing target used in ordinary universality is

\[
G+C=\zeta+C.
\tag{4.8}
\]

It produces positive-density derivative recurrence while simultaneously
forcing

\[
H_\tau(s)=C+o(1).
\tag{4.9}
\]

The construction lands deliberately in a large-`C` fiber, safely outside
the Rouche ball.  Asking in addition that `C_tau` in (4.6) be small is not
a routine strengthening: (4.7) shows that it is already the rare
zero-replication event.

Higher derivatives do not improve this.  They enlarge the forgotten
fiber from constants to all polynomials of degree at most `k-1`.
Controlling those jet coefficients reconstructs the original function and
returns to Theorem 1.1.

## 5. Audit of the named universality and recurrence mechanisms

### 5.1 Ordinary and Bagchi strong recurrence

Ordinary universality permits a nonvanishing target on a compact subset of
`1/2<Re(s)<1` with connected complement.  Lemmas 2.1 and 2.2 show why this
cannot approximate the required zero-bearing state on a full contour.

Bagchi's strong self-recurrence does permit the target `zeta` itself.
Precisely this distinction is RH-level: Theorem A in
[Nakamura--Pankowski, *Self-approximation for the Riemann zeta
function*](https://doi.org/10.1017/S0004972712000846) states that positive
lower density of

\[
\max_K|\zeta(s+i\tau)-\zeta(s)|<\epsilon
\tag{5.1}
\]

for every admissible compact `K` is equivalent to RH.  Theorem 1.1 asks
for less than positive density, but only locally around one candidate
zero; it is a quantitative fragment of that same strong-recurrence step.

The generalized self-approximation results in the same paper compare
`zeta(s+i tau)` with `zeta(s+i d tau)` for `d` different from `0` or `1`.
Both heights move.  They do not recur a fixed zero-bearing target, and a
single prescribed zero cannot be pinned to one member on a positive-measure
set of `tau`.  They therefore do not imply (1.10).

### 5.2 Hybrid universality

Hybrid universality adds finitely many prime-phase constraints, but retains
the nonvanishing target hypothesis.  This is explicit in
[Pankowski, *Hybrid joint universality theorem for Dirichlet
L-functions*](https://doi.org/10.4064/aa141-1-3).  Finite phase constraints
can control an Euler-product head or a point in `Re(s)>1`; they cannot
change Lemma 2.2.  A hybrid theorem imposing enough extra data to make
(4.4) hold would itself be a per-zero replication theorem and is bounded
by (4.5).

### 5.3 Finite and truncated Euler products

In (5.5)--(6.4), write `d=d_r` for the candidate-conditioned
Guth--Maynard exponent in (1.8).

For finite `y`, put

\[
E_y(s)=\prod_{p\leq y}(1-p^{-s})^{-1}.
\tag{5.2}
\]

It is zero-free in `D`, so Lemma 2.2 gives the exact obstruction

\[
\max_\Gamma|E_y-\zeta|\geq m
\tag{5.3}
\]

for **every** cutoff.  Kronecker recurrence of its prime phases returns
`E_y`, not the missing zeta divisor.  Letting `y` grow does not change its
winding; one also needs a continued tail which creates the zero.  No
growing-cutoff recurrence theorem supplies such an atypical tail at the
power frequency required by (1.10).

For fixed `y` and phase tolerance `theta`, coordinatewise recurrence through
`p<=y` has limiting density

\[
(2\theta)^{\pi(y)}.
\tag{5.4}
\]

Thus, in the iterated regime in which this fixed-dimensional limiting
density is first established, retaining more than `T^d` shifts has the
formal entropy requirement

\[
\pi(y)\log\frac1{2\theta}<(1-d+o(1))\log T.
\tag{5.5}
\]

Thus only `O(log T)` independent phase coordinates are affordable at fixed
accuracy in the equidistributed-cylinder model.  This is not, by itself, a
uniform theorem when `y=y(T)`: Kronecker--Weyl gives (5.4) for each fixed
dimension, and a diagonal use needs a quantitative discrepancy bound whose
dependence on the prime frequencies is not supplied here.  Approximate
functional equations at height `T` have power-length data, so the entropy
calculation strongly disfavors recurring all of those phases, but it is not
a rigorous growing-cutoff count without that additional uniformity.

### 5.4 Random Euler products and effective universality

Bagchi's limiting random Euler product is almost surely a nonvanishing
holomorphic function in the relevant domain.  By Lemma 2.2, the full
Rouche recurrence ball has random-model probability exactly zero.  This is
a support statement, not a small-ball estimate.

Effective universality does not reverse it.  Lamzouri--Lester--Radziwill
retain the nonvanishing target and obtain convergence with a saving that is
a small power of `log T`; see [*An effective universality theorem for the
Riemann zeta-function*](https://doi.org/10.4171/CMH/448).  Their theorem
does not apply to the zero-bearing target.  Even if its random-model
comparison were extended to that target, a zero main term plus a
logarithmic error would give at best an event of size `T/(log T)^c`.  The
normalized frequency needed to contradict (1.8) is

\[
T^{d_r-1+o(1)},
\tag{5.6}
\]

a negative power of `T`.  Effective weak convergence at logarithmic scale
cannot see that sparse exceptional orbit.

## 6. The near-one mixed-contour escape also misses the scale

One may try to place most of a contour in `Re(s)>1`, recur a truncated
Euler product there, and use universality only on a left excursion.  A
Jordan curve must cross the transition strip at least twice.  If the
horizontal margin is `eta`, those two omitted connectors have total length
at least `4eta`.

Direct right-half-plane control to fixed accuracy needs a prime cutoff

\[
y=\exp\{(u+o(1))/\eta\}
\tag{6.1}
\]

for a fixed `u>0`; coordinatewise phase recurrence then has density

\[
d_\eta=\exp\{-\exp(u/\eta+o(1/\eta))\}.
\tag{6.2}
\]

These estimates are proved in
[`R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md`](R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md).
If one formally diagonalizes the fixed-`eta` limiting density and asks that
`T d_eta` exceed `T^d`, the resulting necessary scale is

\[
\eta\geq\frac{u+o(1)}{\log\log T}.
\tag{6.3}
\]

On the other hand, second-moment completion down to the Guth--Maynard
count requires, by (3.8),

\[
\eta\leq T^{-(1-d)/2+o(1)}.
\tag{6.4}
\]

There is no overlap between these two formal diagonal scales.  What is
rigorous without exchanging limits is the fixed-gap statement from the
referenced report: the direct phase-cylinder limiting density is
`o(eta^A)` for every fixed `A`, whereas the ambient derivative-exceptional
fraction is only `O(eta^2)`.  Consequently subtraction of the available
estimates cannot produce a surviving shift.  Hybrid universality avoids
committing to the coordinatewise cylinder, but supplies no lower bound
uniform as `eta` shrinks and no independence from the forced connector
spike.  A quantitative diagonal theorem (or a compressed hybrid small-ball
theorem) remains a genuinely new requirement; (6.3)--(6.4) alone do not
rigorously rule one out.

The pole at `s=1` is not the issue.  The contour may cross `Re(s)=1` near
height `gamma_0`, away from the pole.  The obstruction is the transition
scale and the zero-bearing winding, not an accidental singularity at the
real point `1`.

## 7. Exact statements that would succeed

The audit leaves three equivalent-looking but separately testable
research targets.  Each is sufficient for the candidate zero in (0.1),
with `r` chosen as in (1.9).

1. **Full recurrence.**  Prove (1.10).

2. **Conditioned slit recurrence.**  For some `ell=ell(T)` and fixed
   `epsilon<m`, prove

   \[
   \operatorname {meas}\left\{\tau\in U_\ell(T,\epsilon):
   \max_{J_\ell}|H_\tau'|\leq\frac{m-\epsilon}{2\ell}\right\}
   \geq T^{(30/13)\delta-o(1)}.
   \tag{7.1}
   \]

3. **Principal-mode small ball.**  For some fixed `eta` with `eta r<m`,
   prove

   \[
   \begin{split}
   \operatorname {meas}\{\tau\in[T,2T]:&
   \max_D|\zeta'(s+i\tau)-\zeta'(s)|\leq\eta,\\
   &|\zeta(\rho _0+i\tau)|<m-\eta r\}
   \geq T^{(30/13)\delta-o(1)}.
   \end{split}
   \tag{7.2}
   \]

Rouche turns each event into more zeros than Guth--Maynard permits.  Under
the assumed zero, Theorems 1.1, 3.1, and 4.1 prove the matching upper bound
`T^(d_r+o(1))` for each.  Consequently none of (7.1)--(7.2) is supplied by
an existing unconditioned universality statement in disguise.

The most focused possible new direction is therefore not another form of
ordinary universality.  It is a quantitative **fiber theorem**: show that
enough derivative-recurrence shifts land in the small principal-mode
fiber, or that enough slit recurrences avoid paying their winding debt on
the gap.  Any valid theorem must work at a negative-power normalized
frequency, not just with an unspecified fixed-compact lower density.

## 8. Hostile counterchecks

1. **Multiplicity.**  The integrated inequality (1.4) counts
   multiplicity consistently.  The separated-disc argument (1.5) also
   gives genuinely distinct zeros if multiplicity is discarded.

2. **Disc-radius loss.**  The density exponent is
   `(30/13)(1-beta+r)`, not `(30/13)(1-beta)`.  The strict hypothesis
   `beta>1-delta` permits the choice (1.9), so the requested delta exponent
   remains valid.

3. **Boundary equality.**  All Rouche uses are strict.  Thresholds in
   (3.3) and (4.4) leave explicit slack.

4. **A slit is not compact when only one point is removed.**  One cannot
   apply universality to `Gamma\{p}` and then close by continuity; that set
   is not closed.  Every admissible compact arc omits a gap of positive
   length, and its universality constant may collapse as the gap closes.

5. **Derivative recurrence is not function recurrence.**  The integration
   constant in (4.6) is not known to be small.  The usual proof of derived
   universality makes it large on purpose.

6. **Prime phases do not encode the tail zero.**  Every finite Euler
   product has winding zero.  Returning its phases cannot change (5.3).

7. **Universality density and derivative tails are correlated.**  It is
   invalid to multiply their marginal densities.  Under the candidate
   zero, (3.4) says almost every non-replicating punctured recurrence must
   lie in the derivative-spike event.

8. **No assertion about zeros approaching one.**  The report gives a
   conditional upper bound for recurrence around one prescribed zero.  It
   neither constructs a uniform strip nor obstructs all possible methods
   of constructing one.

## 9. Binary conclusion

```text
per-zero Rouché replication threshold using Guth--Maynard    PROVED
target exponent for beta>.99: 3/130                          PROVED
Jordan connected-complement/topology dichotomy               PROVED
slit recurrence -> zero or 1/ell derivative debt             PROVED
invariant logarithmic winding debt                            PROVED
derived recurrence modulo a polynomial principal jet         PROVED
ordinary/hybrid/truncated-Euler theorem controlling that jet  ABSENT
explicit fixed zero-free strip                                NOT PROVED
```

The route does isolate a very small missing object: one complex principal
mode for first-derivative recurrence.  But controlling that mode at the
required frequency is already a quantitative per-zero strong-recurrence
theorem.  Current universality machinery controls the quotient and avoids
precisely this fiber.
