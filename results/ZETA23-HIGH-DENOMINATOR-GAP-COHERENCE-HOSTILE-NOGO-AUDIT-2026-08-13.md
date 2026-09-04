# High-denominator consecutive-gap coherence: hostile no-go audit

**Date:** 2026-08-13

**Verdict:** the available gap-size, localization, large-value, sieve-upper,
and qualitative-nonlattice inputs do not by themselves prove the required
minor-arc cancellation.  This statement has three different levels, which
must not be conflated.

1. There is a rigorous **abstract positive-node countermodel** satisfying far
   stronger maximal-gap and gap-square estimates than the primes, the same
   low-denominator excision, a prime-density-shaped local counting upper
   bound, and even rational independence after an arbitrarily small
   perturbation.  Its retained high-denominator antenna is nevertheless
   `1-o(1)`.
2. Guth--Maynard and even the conjecturally optimal Montgomery large-value
   bound count exceptional packets; they permit one packet.  Phase modulation
   on the actual prime support shows rigorously that no argument which sees
   only coefficient magnitudes and the support can remove that last packet.
3. Neither counterexample is a positive antenna on the actual primes.  Thus
   they do **not** rule out a proof using the joint structure

   ```text
   actual primes + positivity + consecutive-gap/Voronoi coefficients.
   ```

No literature theorem found in this audit eliminates that joint route.  In
particular, the sieve parity literature is often quoted more broadly than its
proved scope warrants.

---

## 1. Exact target under audit

Put

```text
A=50/33,             B=Y^A,
theta=797/5000,      beta=1537/10000,    Q=Y^beta,
omega_t(x)=t/(2*pi*x),
eta_t=sqrt(t)/Y.
```

Let `C_p` be the logarithmic Voronoi cell of an actual prime in the fixed
multiplicative shell and

```text
lambda_p=integral_(C_p) phi(log(x/Y)) dx/x >=0.
```

Let `B_t(Q)` be the union of every cell meeting

```text
M_t(Q)={x: |omega_t(x)-a/q|<=eta_t/q
             for some (a,q)=1, 1<=q<=Q}.
```

Let `L_Y` be the union of the two logarithmic half-cells belonging to each
physical prime gap larger than `C_w Y^theta`.  If `v(u)=log(p/Y)` on the
Voronoi cell of `p`, the exact super-`Y` retained target is

```text
sup_(Y<=t<=B)
 |integral_([-w,w] minus (B_t(Q) union L_Y))
    phi(u)[exp(i*t*v(u))-exp(i*t*u)]du|
 <=Y^(-c)                                                (1.1)
```

for one fixed `.0180303234<c<1173/65000`.  Equivalently, one may use the
positive retained node weights and restore the retained continuum term: its
difference from the full, rapidly decaying continuum transform is bounded by
the already deleted mass.  A separate transition estimate is still needed
on `[Y^.751,Y]`.

---

## 2. A countermodel satisfying the geometric packages exactly

The following construction explains why removing ordinary rational aliases
does not remove high-denominator coherence.

### Theorem 2.1 (retained log-lattice alias)

For every sufficiently large `Y` there is a set of positive real nodes

```text
X_Y={x_j} subset [Y*exp(-w),Y*exp(w)]
```

with logarithmic Voronoi coefficients `lambda_j` such that

```text
#X_Y asyp Y/log Y,
max_j (x_(j+1)-x_j) <<log Y,
sum_j (x_(j+1)-x_j)^2 <<Y log Y,                       (2.1)

#(X_Y intersect J) <<1+|J|/log Y                       (2.2)
```

for every physical interval `J`, but at `t=B`

```text
sum_(C_j disjoint from M_B(Q))
 lambda_j exp(i*B*log(x_j/Y))
 =integral_(-w)^w phi(u)du-o(1).                       (2.3)
```

There are no `L_Y` half-cells in this model for large `Y`, since all its
physical gaps are `O(log Y)`.  Its exact retained error in (1.1) also equals
the right side of (2.3) up to `o(1)`.  After normalizing the total coefficient
mass, both quantities are `1-o(1)`.

#### Proof

Take the fine logarithmic lattice

```text
u=2*pi*k/B
```

and retain every `L`-th point in `[-w,w]`, where

```text
L asyp B log(Y)/Y.
```

Set `x_j=Y exp(u_j)`.  Then

```text
Delta u_j asyp log(Y)/Y,
x_(j+1)-x_j asyp log Y,
```

which proves (2.1), (2.2), and the asserted cardinality.  These estimates are
much stronger than the Baker--Harman--Pintz maximal-gap scale and Stadlmann's
`Y^(1.23+epsilon)` gap-square scale.

The elementary major-arc geometry used in the rational-alias localization
card gives

```text
|M_B(Q)|<<Q sqrt(B),
number of components R_B(Q)<<(B/Y)Q^2.                 (2.4)
```

Every physical Voronoi cell in the present model has length `O(log Y)`.
Enlarging `M_B(Q)` to all meeting cells therefore deletes coefficient mass at
most

```text
Q sqrt(B)/Y + (B/Y)Q^2 log(Y)/Y
 <<Y^(-29279/330000)
   +Y^(-29279/165000)log Y=o(1).                       (2.5)
```

For every retained node,

```text
exp(i*B*u_j)=1,                                        (2.6)
```

because `B*u_j` is an integral multiple of `2*pi`.  The full continuum
transform is `O(B^-2)`, while the continuum integral over deleted cells is
at most their mass in (2.5).  Equations (2.5)--(2.6) prove (2.3) and the
retained-error assertion.  QED

### Corollary 2.2 (qualitative nonlattice does not repair the model)

For every fixed `K`, the nodes in Theorem 2.1 can be perturbed by

```text
|u'_j-u_j|<=B^(-1)Y^(-K)                               (2.7)
```

so that the centered frequencies are rationally independent, while (2.1),
(2.2), (2.5) remain valid and the normalized modulus in (2.3) remains
`1-o(1)`.

Indeed, the complement of rationally independent configurations is a
countable union of proper rational hyperplanes, hence has empty interior.
Choose a perturbation outside that union.  At height `B`, its phase error is
at most `Y^(-K)`, and the mesh estimates are stable.

This corollary models the **qualitative consequence** of unique
factorization used in nonrecurrence arguments.  It does not turn the real
nodes into integers or actual primes.

### Scope

Theorem 2.1 is a joint countermodel to the following abstract data:

```text
node count;
maximal gap;
sum of squared gaps;
positive Voronoi coefficients;
low-denominator curvature-scale excision;
local prime-density-shaped upper counts.
```

Corollary 2.2 adds qualitative rational independence.  Neither result is an
actual-prime counterexample, and neither satisfies the hypotheses of a
Dirichlet-polynomial theorem whose frequencies must be logarithms of
integers.  Those limitations are load-bearing.

---

## 3. What Guth--Maynard does and does not eliminate

Guth--Maynard Theorem 1.1 states that if `|b_n|<=1` and a length-`N`
Dirichlet polynomial has magnitude at least `V` at `R` one-separated points
in `[0,T]`, then

```text
R<=T^o(1)[N^2 V^-2+N^(18/5)V^-4+T N^(12/5)V^-4].      (3.1)
```

In the present exceptional-packet normalization, its first term is the
cached `C^2` bound.  At

```text
C=Y^.0180303234
```

this permits `Y^(.0360606468+o(1))` packets.  It certainly permits one.
The conjecturally optimal Montgomery bound has the same `N^2V^-2` scale.
Guth and Maynard also give explicit arbitrary-coefficient examples with
`gg N^(2-2sigma)` separated large values.  Thus the `C^2` term is structural,
not merely an avoidable loss in their proof.

There is an exact coefficient-blind obstruction on the actual prime support.
For any positive magnitudes `lambda_p` and any legal `t_0`, put

```text
b_p=lambda_p exp(-i*t_0*log(p/Y)).
```

Then

```text
sum_p b_p exp(i*t_0*log(p/Y))=sum_p lambda_p.          (3.2)
```

The support, coefficient magnitudes, prime gaps, sieve properties, and
unique-factorization properties are unchanged.  After a harmless common
rescaling, (3.2) is within Guth--Maynard's coefficient hypotheses.
Consequently no combination of those inputs which is invariant under
coefficient phase can prove pointwise cancellation.

Equation (3.2) is **not** a counterexample to (1.1): the target coefficients
are positive, while `b_p` are modulated.  It proves that the surviving proof
must use positivity and the actual relationship between `lambda_p` and the
neighboring prime gaps, rather than use Guth--Maynard as a black box.

Heath-Brown's difference-set estimate, quoted as Theorem 1.6 by
Guth--Maynard, has the same logical limitation: a singleton exceptional set
has no rich difference set to contradict.

---

## 4. Sieve limitations: exact and non-exact statements

### 4.1 What is rigorous

Ford--Maynard's framework fixes precise Type-I and Type-II axioms for a
nonnegative sequence `(a_n)`.  Their Theorem 2.1 proves that, for every
`gamma<1`, some positive amount of Type-II range is necessary: when `nu` is
sufficiently small, there are bounded nonnegative sequences satisfying the
stated Type-I and Type-II estimates but vanishing on every prime.  Their
Theorem 2.2 gives complementary optimality statements within the same
axiomatic framework.

This rigorously rules out the assertion

```text
strong Type-I information plus an arbitrarily short Type-II range
automatically detects prime mass.                      (4.1)
```

It does not discuss consecutive-gap Voronoi coefficients or prove that
(1.1) is impossible.

There is also an exact obstruction to importing their full Type-II axiom by
curvature alone.  A logarithmic Fourier mode factorizes:

```text
(mn)^(it)=m^(it)n^(it).                                (4.2)
```

The allowed Type-II test coefficients can conjugate both factors.  Hence a
coefficient-uniform Type-II saving for this mode is false.  A successful
sieve argument must retain some coefficient-specific arithmetic restriction;
it cannot simply feed the bare logarithmic chirp into an arbitrary-coefficient
Type-II black box.

### 4.2 What is not a theorem here

Section 8 of the Polymath8 paper says explicitly that its parity-barrier
discussion is “somewhat informal and heuristic in nature.”  Its stated
conclusion concerns improving `H_1<=6` by purely sieve-theoretic methods,
even under GEH.  It is not a rigorous no-go theorem for a signed Fourier
estimate involving consecutive gaps.

Likewise, ordinary Brun/Selberg upper bounds control nonnegative counts and
congruence occupancy.  The real-node model in Section 2 satisfies the
resulting local counting envelope, but not literal congruence hypotheses.
Therefore this audit proves:

```text
count-envelope-only sieve input is insufficient;       PROVED abstractly;
all possible sieve uses on the actual primes fail;      NOT PROVED.
```

---

## 5. Unique factorization and logarithmic forms

Unique factorization gives exact multiplicative collision identities,
fixed-moment bounds, and the five-prime exclusion of a literal one-atom
alias.  It does not give a polynomial-scale separation from an approximate
multi-atom recurrence.

Matveev's explicit logarithmic-form theorem is quantitative, but its lower
bound has exponential dependence on the number `n` of logarithms and a
product of their heights.  Here

```text
n asyp Y/log Y,             height(log p) asyp log Y.
```

Substitution yields a separation vastly smaller than every negative power
of `Y`; it cannot certify the required polynomial-aperture Schur margin.
This is a failure of the currently available bound at growing dimension,
not a theorem that a sharper actual-prime estimate is impossible.

Corollary 2.2 gives the correct logical no-go: qualitative independence
alone cannot imply a power margin.  The literal actual-prime quantitative
problem remains open.

---

## 6. A useful large-gap reduction, with exact scope

Gafni--Tao define `mu(theta)` by the Lebesgue measure of the exceptional set
for the PNT in intervals of length `x^theta`.  Their General Bound (Theorem
1.2), combined with the piecewise zero-density bounds in their Table 1, gives
the following exact consequence:

```text
mu(theta) <= 1-(9/13)(theta-2/15)
for 2/15 <= theta <= 353/1445.                         (6.1)
```

Equation (6.1) is not printed in this range in the paper.  The paper only
prints the same formula for sufficiently small positive `theta-2/15`.
However, (6.1) follows by checking the finitely many rational branches in
their displayed table: throughout this interval the maximum in Theorem 1.2
is attained at

```text
sigma=7/10,                 Abar(sigma)=30/13.
```

At the upper endpoint it ties the threshold point on the
`11/(48 sigma-36)` branch:

```text
theta=353/1445,             mu bound=1334/1445.
```

Immediately above that endpoint this threshold point is larger, so this is
the exact range of this linear envelope obtained from the current table.
The optimized live specialization, followed by two historical checkpoints,
is

```text
mu(797/5000)<=63827/65000=1-1173/65000,
mu(1/6)  <=127/130,
mu(4/25) <=319/325=1-6/325.                            (6.2)
```

These exceptional-**measure** estimates control total large-gap mass more
strongly than the displayed gap-**count** corollary in the paper.  Fix
`C>2^theta`.  For a gap `g=p_(n+1)-p_n>C Y^theta` inside `[Y,2Y]`, the set of
`x` in that gap for which

```text
(x,x+x^theta] contains no prime
```

has measure at least

```text
g-(2Y)^theta >=(1-2^theta/C)g.                         (6.3)
```

These sets are disjoint for distinct gaps.  The von Mangoldt sum on such an
interval receives only prime-power terms, whose total is `O(log(Y)^2)` and
hence `o(Y^theta)`.  Thus (6.3) lies in, say, the `delta=1/2` exceptional set
for all sufficiently large `Y`.  The `O(1)` shell-boundary gaps are absorbed
by the available maximal-gap estimate.  It follows that

```text
sum_(Y<=p_n<=2Y, g_n>C Y^theta) g_n
   <<Y^(mu(theta)+o(1)).                                (6.4)
```

The same estimate, divided by `Y`, bounds the logarithmic Voronoi mass of all
cells touching one of these gaps.  The optimized live cutoff gives

```text
theta=797/5000:
  discarded mass <<Y^(-1173/65000+o(1)).              (6.5)
```

The saving is

```text
1173/65000=.018046153846... > .0180303234
```

with margin `.000015830446...`.  This is enough for the cached target, but
the margin is extremely narrow.  The `theta=1/6` and `theta=4/25` estimates
remain useful simpler checkpoints, not the current retained definition.
The continuous strict frontier is

```text
theta> .1593771338,
beta < .153720513824242...,
inf(theta-beta)=.005656619975757... .
```

The chosen rational pair `.1594,.1537` lies just inside it and leaves corridor
width `.0057`.

This also improves the rational-alias geometry, but one must split cells into
their two gap half-cells before combining it with the rational excision.  Let
`L_Y` be the union of all half-cells belonging to gaps larger than
`C Y^(797/5000)`.  On the complement of `L_Y`, every half-cell has
logarithmic mass `O(Y^(797/5000)/Y)`.  Take

```text
Q=Y^(1537/10000).
```

At `t=B`, the geometric part of the marked mass is

```text
Q sqrt(B)/Y=Y^(-29279/330000).                        (6.6)
```

The number of raw rational components, and hence of union boundary points,
is

```text
R_t(Q)<< (t/Y)Q^2.
```

Form the original cell cover of `M_t(Q)` before subtracting `L_Y`; otherwise
the long-gap deletion could artificially fragment the set and inflate its
component count.  Subtracting `L_Y` afterward creates no new collars.
Covering by the remaining small half-cells therefore adds at most

```text
R_t(Q) Y^(797/5000)/Y <<Y^(-1489/82500)               (6.7)
```

at the top aperture.  Factors for two endpoints, two cells, or two
half-cells are constants.  Overlap only lowers the union component count,
and clipping at the fixed shell endpoints adds only `O(1)` half-cells.
Both exponents in (6.6)--(6.7) beat the target; the tail exponent
`1173/65000` in (6.5) is the bottleneck, narrowly below the collar saving
`1489/82500`.

It would be incorrect to put `Q=Y^(797/5000)` into this actual-prime boundary
argument.  Although its geometric length remains small, the small-gap collar
would then save only

```text
2-50/33-3(797/5000)=1097/165000=.00664848...,
```

which is below the target.  The much stronger regular-cell collar in (2.5)
does not transfer to actual primes.  The historical simple pair
`theta=4/25`, `beta=3/20` is valid but leaves a wider `.01` corridor.  The
older gap-square truncation at `Q=Y^.249` is beyond the Dirichlet cover
threshold `Y^(8/33)`: at that scale every local velocity has such an
approximation, so the proposed minor arcs can be empty.

The exact conclusion of (6.5) is only about **literal step aliases**.  For a
reduced rational `a/q`,

```text
exp(2*pi*i*a*g/q)=1  iff  q divides g.
```

After (6.5), every retained gap is at most `C Y^(797/5000)`, so such a
literal alias has `q<=C Y^(797/5000)`.  The enlarged rational excision removes
`q<=Y^(1537/10000)`, leaving only the optimized literal one-gap exponent
window

```text
Y^(1537/10000)<q<=C Y^(797/5000).                     (6.8)
```

This does not bound the denominator at which a whole residue-class sum can
cohere: many nonzero phases can have a large aggregate without any individual
`q|g`.  It also does not control approximate aliases spanning several gaps or
the errors in linearizing the logarithmic phase.

### 6.1 Exact rational DFT identity

For clarity, put

```text
g_k=p_(k+1)-p_k,
G_r(X;q)=sum_(p_(k+1)<=X, p_k=r mod q) g_k.
```

Then, with `e(z)=exp(2*pi*i*z)`, one has the exact finite identity

```text
sum_(p_(k+1)<=X) g_k e(a p_k/q)
   =sum_(r mod q) e(ar/q) G_r(X;q).                    (6.9)
```

Thus the additive forward-gap antenna at a rational frequency is precisely
the discrete Fourier transform of Jaeyoon Kim's prime-running residue masses,
apart from the one terminal partial-gap convention in Kim's `Phi(X;q,r)`.
A dyadic shell introduces at most two analogous endpoint terms.  Smooth
weights follow by Stieltjes partial summation.  Identity (6.9) is not exact
for the logarithmic phase `t log(p/Y)` or for symmetric Voronoi weights until
the relevant Taylor/symmetrization errors are supplied.

Kim conjectures fixed-`q` equidistribution of these masses, but his paper
does not prove the needed fixed-`q` main term beyond the trivial `q=2` case,
much less a result uniform for `q` growing like a power of `Y`.  Moreover, a
uniform main term over reduced residues transforms to the Ramanujan sum

```text
sum_((r,q)=1) e(ar/q)=c_q(a)=mu_Mobius(q)              (6.10)
```

when `(a,q)=1`, rather than to zero.  Its normalized contribution is
`O(1/phi(q))`, which is harmless at large `q`; the missing ingredient is a
uniform Fourier error.  The absence of such a theorem is a literature gap,
not a no-go theorem for the route.

---

## 7. Literature scope audit

1. Julia Stadlmann,
   [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867),
   proves the gap-square exponent `1.23`.  The theorem contains no phase or
   signed correlation conclusion.
2. Larry Guth and James Maynard,
   [*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
   prove (3.1), exhibit the `N^(2-2sigma)` scale for arbitrary coefficients,
   and formulate Montgomery's matching conjectural count.  None is a
   zero-exception theorem.
3. Kevin Ford and James Maynard,
   [*On the theory of prime-producing sieves*](https://arxiv.org/abs/2407.14368),
   give rigorous optimality and countersequence theorems for their exact
   Type-I/Type-II axioms.  Those axioms are not hypotheses currently proved
   for the gap antenna.
4. D. H. J. Polymath,
   [*Variants of the Selberg sieve, and bounded intervals containing many
   primes*](https://arxiv.org/abs/1407.4897), Section 8, discusses the parity
   obstruction but labels that discussion informal and heuristic.  It must
   not be cited as eliminating (1.1).
5. E. M. Matveev,
   [*An explicit lower bound for a homogeneous rational linear form in
   logarithms of algebraic numbers*](https://doi.org/10.1070/im1998v062n04ABEH000190),
   supplies a genuine quantitative theorem, but its growing-dimensional
   constants are far outside the required polynomial scale.
6. Ayla Gafni and Terence Tao,
   [*On the number of exceptional intervals to the prime number theorem in
   short intervals*](https://arxiv.org/abs/2505.24017), Theorem 1.2 and Table
   1, imply (6.1)--(6.5).  Their printed prime-gap corollary counts gaps;
   estimate (6.4) instead uses the defining exceptional-set measure.
7. Jaeyoon Kim,
   [*Prime Running Functions*](https://arxiv.org/abs/2006.13355), studies the
   residue masses in (6.9) and records their biases empirically and in random
   models.  Those observations are not a uniform cancellation theorem.

No primary source located in this survey proves Fourier cancellation for
consecutive-prime-gap or logarithmic Voronoi weights after high-denominator
minor-arc restriction.

---

## 8. Precise survivor

The following is not eliminated:

### AP-GAP-COH

For the **actual primes**, split each positive logarithmic Voronoi weight into
its two gap half-cell weights.  Delete the halves belonging to gaps larger
than `C_w Y^(797/5000)`.  For every `Y<=t<=Y^(50/33)`, let `B_t` be the union
of the original Voronoi cells meeting `M_t(Y^(1537/10000))`, formed before
the long half-cells are removed.  With `v(u)=log(p/Y)` on the cell of `p`,
prove

```text
|integral_([-w,w] minus (B_t union L_Y))
   phi(u)[exp(i*t*v(u))-exp(i*t*u)]du|
 <=Y^(-c+o(1))                                         (8.1)
```

for some `.0180303234<c<1173/65000`.

Any proof of (8.1) must use information absent from every countermodel above.
The minimal recognizable possibilities are:

1. a sign-sensitive correlation between consecutive actual prime gaps and
   the local logarithmic phase;
2. a coefficient-specific Type-II/dispersion theorem which cannot be
   neutralized by (4.2);
3. an actual-prime directional Schur/leverage estimate excluding the final
   exceptional packet.

The package audit is therefore:

```text
max gap + sum gaps^2 + excision:             insufficient (abstract theorem);
local sieve count envelopes:                 insufficient (abstract theorem);
qualitative unique factorization/nonlattice: insufficient (abstract theorem);
GM/MHH packet count as a black box:           cannot remove last packet;
coefficient-phase-blind actual-prime methods: insufficient (exact modulation);
all actual-prime positive gap-weight methods: NOT eliminated;
AP-GAP-COH:                                  OPEN.
```
