# Singular atomic exceptional-span gate

**Date:** 2026-08-13

**Verdict:** a cheap singular cancellation measure is forced into a small,
explicit collection of extreme-correlation packets, but packet counting and
Taylor rank do not by themselves exclude it.  For total variation `C`, at
least one half unit of variation must lie where

```text
|sum_(n in N_Y) cos(t*log(n/Y))| >=M/(2C),                (0.1)
```

and an actual-integer Dirichlet-polynomial large-values theorem covers this
exceptional set by at most

```text
Y^o(1)*C^2                                                 (0.2)
```

fixed-width intervals.  Subdivision gives a refined cover by `C^3Y^o(1)`
intervals of width `O_w(1/C)`.  At
`C=Y^kappa`, `kappa=.0180303234`, and `B=Y^(50/33)`, the
packet-count exponent is

```text
2*kappa=.0360606468...<1.                                 (0.3)
```

Each fixed-width packet has `Y^o(1)` effective Taylor rank at any prescribed
fixed-power accuracy; the shrinking refinement has constant rank.  This is
a genuine actual-prime theorem and is stronger in the `L^1` direction than
the earlier broad-profile concentration result.

The missing implication is also exact: a low-dimensional collection of
packet jets can still contain the **one distinguished vector** `q_0`; rank
smaller than `M` excludes generic vectors, not this carrier.  The exact
exterior-power identity shows that a determinant lower bound for the jet
matrix alone is irrelevant: one must lower-bound the *augmented* determinant
obtained by adjoining `q_0`, equivalently its directional Schur complement.
The currently available prime-twist coherence is only polylogarithmic,
whereas a Gershgorin or block restricted-invertibility closure at
`C^2Y^o(1)` columns needs a fixed-power saving.  Therefore Turan--Nazarov,
zero counting, cluster packing, or restricted invertibility using only rank
or unaugmented volume does not finish the actual-prime problem.

The old uniform-log-lattice alias is **not** used as evidence against this
actual-prime transversality statement.  It fails the integer
Dirichlet-polynomial hypothesis behind (0.2).  All conclusions below that
concern packet count or arithmetic rigidity are proved for the actual
prime-power nodes.

For the actual prime nodes, a new exact rigidity lemma rules out a one-atom
alias, and a second lemma rules out coarse commensurable/harmonic grids.
Neither gives a power TV lower bound for arbitrary incommensurable atoms.

No subpower design, prime power upper bound, zeta bound, or zero-free strip
is proved.

---

## 1. Exact `L^1` interpolation form

Use the self-contained `QP` continuation packet.  Thus

```text
N_Y={p^k:Y*exp(-w)<=p^k<=Y*exp(w)},
u_n=log(n/Y),
a(t)=(cos(t*u_n))_(n in N_Y),
M=#N_Y=Y^(1-o(1)),
H=[Y^.751,Y^(50/33)],       B=Y^(50/33).                 (1.1)
```

The lower endpoint `.751` is the current frontier after the
mean-square-gap Voronoi antenna; replacing it by any smaller positive power
does not change the arguments below.

Let

```text
q_0=a(0)=(1,...,1),
S_Y(t)=<q_0,a(t)>=sum_(n in N_Y)cos(t*u_n).                (1.2)
```

A singular promotion of the principal carrier requires a signed real
measure `mu` on `H` such that

```text
integral_H a(t)dmu(t)=q_0,
||mu||_TV=C.                                               (1.3)
```

This is the interpolation statement

```text
F_mu(u_n)=1 for every n in N_Y,
F_mu(u)=integral_H cos(t*u)dmu(t),
||mu||_TV=C.                                               (1.4)
```

The exact global atomic cost is the infimum of `C` in (1.3).  For a fixed
probability design `rho`, by contrast,
`q_0^T G_rho^dagger q_0` is a least-`L^2(rho)` cost.  The two are linked only
after polarizing an `L^1` measure:

```text
rho=|mu|/C,       dmu=C*epsilon*d rho,      |epsilon|=1,
q_0^T G_rho^dagger q_0<=C^2.                              (1.5)
```

Conversely, a fixed design of leverage `L` supplies an `L^2` density of
norm `sqrt(L)` and hence an `L^1` representation of cost at most
`sqrt(L)`.  A lower bound for one broad base design is not automatically a
lower bound for all `L^1` measures; the induced polar design in (1.5) is the
correct object here.

Writing `C_*(q_0;H)` for the least TV cost in (1.3), taking the two infima
gives the exact directional Christoffel identity, with no normalization
loss:

```text
C_*(q_0;H)^2
 =inf_(rho probability on H, q_0 in Ran G_rho)
     q_0^T G_rho^dagger q_0.                              (1.6)
```

For the converse direction explicitly, the canonical density
`h(t)=a(t)^T G_rho^dagger q_0` represents `q_0` and has squared
`L^2(rho)` norm `q_0^T G_rho^dagger q_0`; Cauchy--Schwarz then bounds its
TV norm by the square root.  Thus throughout this packet `C` is the actual
`L^1` carrier cost and `C^2` is directional leverage.

---

## 2. Half-unit localization on an actual prime-phase peak set

### Theorem 2.1 (`L^1` exceptional localization)

If (1.3) holds, define

```text
E_C={t in H: |S_Y(t)|>=M/(2C)}.                           (2.1)
```

Then

```text
|mu|(E_C)>=1/2.                                           (2.2)
```

In particular there is a support atom (or a support limit point) with

```text
|S_Y(t)|>=M/C.                                            (2.3)
```

#### Proof

Summing all coordinates of (1.3) gives the exact scalar identity

```text
M=integral_H S_Y(t)dmu(t).                                (2.4)
```

The complement of `E_C` contributes at most
`[M/(2C)]||mu||=M/2`, while the part on `E_C` contributes at most
`M|mu|(E_C)`.  This proves (2.2).  Applying (2.4) directly without splitting
gives `M<=C sup_H|S_Y|`, which is (2.3).  QED.

The distinction from an arbitrary low-leverage design is useful.  For the
polar probability in (1.5), (2.2) says

```text
rho(E_C)>=1/(2C),                                         (2.5)
```

rather than merely the `C^(-2)` mass obtained from a second-moment leverage
argument.

The same localization exponent holds for every fixed phase carrier
`q_s=a(s)`.  Put

```text
S_(Y,s)(t)=<a(s),a(t)>,       N_s=||a(s)||^2.             (2.6)
```

Uniformly for `s` in a fixed compact set, the prime number theorem gives
`N_s>=c_(w,s)M`.  If `mu` represents `a(s)` at TV cost `C`, then
`N_s=integral S_(Y,s)dmu`, while `|S_(Y,s)|<=M`.  Hence a fixed positive
amount of variation lies where `|S_(Y,s)|>=N_s/(2C)`, and one support point
satisfies `|S_(Y,s)|>=N_s/C`.  The moment, derivative, and large-values
arguments in Section 3 are unchanged up to fixed constants: after expanding
the product of cosines, the relevant Dirichlet-polynomial coefficients are
still bounded.  Thus the packet exponent (0.3) also covers the observed
fixed carrier near `s=6--8`.

### Corollary 2.2 (pointwise arithmetic gate comes first)

Any bound

```text
sup_(t in H)|S_Y(t)|<=M*Y^(-delta+o(1))                  (2.7)
```

implies `C>=Y^(delta-o(1))`.  Thus a promotion at
`C<=Y^(kappa-epsilon)` first requires an actual frequency with

```text
|S_Y(t)|>=M*Y^(-kappa+epsilon).                           (2.8)
```

Span or conditioning questions occur only after this scalar prime
Dirichlet-polynomial event exists.  The proof packet's current
`(log Y)^(-3/10)` pointwise estimate gives only a polylogarithmic lower cost,
not (2.7) with fixed `delta`.

---

## 3. Multiplicative fourth moment and exact cluster packing

The actual-node logarithmic packing theorem first gives the full-band mean
square

```text
(1/|H|)*integral_H |S_Y(t)|^2 dt <=C_w M.                 (3.1)
```

This follows either from the sinc-profile Gram bound or by applying the
Montgomery--Vaughan mean-value inequality separately to the two monotone
branches `n<Y` and `n>Y`.  Almost-reflected nodes do not create an extra
factor.

Actual multiplicative structure gives a much stronger estimate for the
extreme values needed here.  Put

```text
D_Y(t)=sum_(n in N_Y)n^(it).
```

Since `S_Y(t)=Re[Y^(-it)D_Y(t)]`, `|S_Y(t)|<=|D_Y(t)|`.

### Lemma 3.1 (fourth moment below the fourth-moment aperture)

Uniformly for every interval `I` of length at most `B<Y^2`,

```text
integral_I |S_Y(t)|^4 dt <=Y^(2+o(1))*M^2.                (3.2)
```

#### Proof

Write

```text
D_Y(t)^2=sum_m r_2(m)m^(it),
r_2(m)=#{(n_1,n_2) in N_Y^2:n_1*n_2=m}.                  (3.3)
```

The mean-value theorem for a Dirichlet polynomial of length `O_w(Y^2)`
gives

```text
integral_I |D_Y(t)|^4 dt
 <=O_w(B+Y^2)*sum_m r_2(m)^2.                             (3.4)
```

Every `m` here is `O_w(Y^2)`.  The divisor bound gives
`r_2(m)<=d(m)=Y^o(1)`, while `sum_m r_2(m)=M^2`.  Hence

```text
sum_m r_2(m)^2<=Y^o(1)*M^2.                              (3.5)
```

Since `B<Y^2` and `|S_Y|<=|D_Y|`, (3.2) follows.  QED.

The identical argument with coefficients `u_n`, which are bounded by `w`,
also gives

```text
integral_I |S_Y'(t)|^4 dt <=Y^(2+o(1))*M^2.              (3.6)
```

This does not contradict the proof packet's fourth-moment conductor warning.
The conductor term is indeed `Y^2`, rather than `B`.  At the exceptionally
large threshold `M/C`, division by the fourth power of that threshold leaves
only `(Y/M)^2*C^4=C^4*Y^o(1)`.  The fourth moment locates near-maximal peaks
even though it does not have random-size normalization.

The fourth moment already implies that the slightly enlarged set
`{|S_Y|>=M/(4C)}` has length at most `C^4Y^o(1)`.  Together with (3.6) and
one-dimensional Sobolev, it gives a valid cover by `C^4Y^o(1)` fixed-width
packets.  That estimate is useful as a self-contained check, but is not the
sharp packet count.

### Lemma 3.2 (large values for an integer Dirichlet polynomial)

Let

```text
A(t)=sum_(N<n<=2N) b_n*n^(it),       |b_n|<=1,
```

and let `t_1,...,t_R` be `1`-separated in an interval of length `T`, with
`|A(t_r)|>=V`.  The large-values theorem of
[Guth--Maynard, Theorem 1.1](https://arxiv.org/abs/2405.20552) gives

```text
R<=T^o(1)*[N^2/V^2+N^(18/5)/V^4+T*N^(12/5)/V^4].         (3.7)
```

The classical Montgomery--Halasz--Huxley estimate would also suffice in
this near-maximal-value range.  The crucial point is that (3.7) is a theorem
for coefficients bounded by one; no density or primality assumption on the
support is needed.

### Theorem 3.3 (actual fixed and shrinking packet covers)

Suppose `C<=Y^(kappa+o(1))`.  There are centers
`sigma_1,...,sigma_R` such that

```text
E_C subset union_(j<=R)[sigma_j-1,sigma_j+1],
R<=C^2*Y^o(1).                                           (3.8)
```

There are also centers `tau_1,...,tau_K` giving a shrinking refinement

```text
E_C subset union_(j<=K)
 [tau_j-1/(4wC),tau_j+1/(4wC)],
K<=C^3*Y^o(1).                                           (3.9)
```

#### Proof

Choose a maximal `1`-separated subset of `E_C`.  At each selected point,

```text
|D_Y(t)|>=|S_Y(t)|>=M/(2C).                              (3.10)
```

Partition the fixed multiplicative window containing `N_Y` into
`O_w(1)` dyadic intervals.  For each selected point at least one dyadic
piece of `D_Y` has size `V>>_w M/C`; partition the selected points according
to such a piece.  Translating `H` to an interval starting at zero merely
multiplies its coefficients by unimodular constants.  Lemma 3.2 therefore
applies with

```text
N asymp_w Y,       T<=B=Y^(50/33),       V>>_w M/C.
```

Since `M=Y^(1-o(1))`, its three terms are respectively

```text
C^2*Y^o(1),
Y^(-2/5)*C^4*Y^o(1),
Y^(50/33-8/5)*C^4*Y^o(1).                               (3.11)
```

At `C=Y^(kappa+o(1))`, the last two fixed-power exponents are

```text
-2/5+4*kappa             =-.3278787064...,
50/33-8/5+4*kappa        =-.0127271912....               (3.12)
```

Thus the first term dominates and proves (3.8); maximality supplies the
cover.  Finally, subdivide each fixed-width packet into `O(C)` intervals of
width `O(1/C)` to obtain (3.9).  Notice that `C>=1`, directly from any one
coordinate of (1.3).  QED.

At the target cost the two covers now give

```text
R<=Y^(2*kappa+o(1))=Y^(.0360606468...+o(1)),
K<=Y^(3*kappa+o(1))=Y^(.0540909702...+o(1)).               (3.13)
```

This strictly supersedes the fourth-moment `C^4` fixed cover and derivative
`C^5` shrinking cover.  By Theorem 2.1, at least half a unit of the
representing variation lies in these packets.

---

## 4. Packet jets have low approximate rank

For a packet center `tau`, Taylor's theorem gives, coordinatewise,

```text
a(t)=sum_(m<d) (t-tau)^m/m! * a^(m)(tau)+r_d(t),
||r_d(t)||_2<=sqrt(M)*(w*|t-tau|)^d/d!.                   (4.1)
```

On a shrinking packet in Theorem 3.3,

```text
||r_d(t)||_2<=sqrt(M)/(d!*(4C)^d).                        (4.2)
```

Consequently the contribution of `mu` restricted to `E_C` is within

```text
sqrt(M)/(d!*4^d*C^(d-1))                                 (4.3)
```

of a subspace of dimension at most `K*d`.

For `C=Y^(kappa+o(1))`, any prescribed relative error `Y^(-A)` is obtained
with a fixed

```text
d>1+A/kappa.                                              (4.4)
```

Thus the significant atomic contribution has dimension at most
`Y^(.054091+o(1))` at every fixed-power accuracy.

The constant-width cover is sharper overall.  On a fixed packet,
(4.1) has error at most

```text
sqrt(M)*w^d/d!.                                          (4.5)
```

After integration against variation at most `C`, choosing

```text
d=O_(A,w)(log Y/loglog Y)                                (4.6)
```

makes the relative error at most `Y^(-A)`.  Since this rank is `Y^o(1)` per
packet and `R<=C^2Y^o(1)`, the significant contribution is within any fixed
power error of a subspace of dimension

```text
C^2*Y^o(1)=Y^(.0360606468...+o(1))                       (4.7)
```

at the target cost.  Thus (4.7), rather than the shrinking-cover exponent,
is the strongest approximate-rank conclusion.

This does **not** prove it misses `q_0`.  A subspace of dimension one can
contain one distinguished vector.  Nor is the complement of `E_C` small in
vector norm: Theorem 2.1 controls its scalar carrier projection, while its
orthogonal component may be large and may cancel the packet-jet residual.
Replacing that missing distance estimate by generic dimension counting is
the precise invalid step in the proposed restricted-invertibility closure.

The additional theorem actually needed is, for every admissible collection
of actual-prime large-value centers and packet jets,

```text
dist(q_0, span{a^(m)(sigma_j):j<=R,m<d})
 >=Y^(-O(1))*||q_0||,                                    (4.8)
```

in a form stable under the lower-correlation remainder.  No such theorem
for the actual prime-log nodes is presently known.  Proving (4.8) is an
arithmetic exceptional-span theorem, not a consequence of rank.  Even
(4.8) must ultimately be strengthened to remain directional after adding
the contribution from `H\E_C`: scalar localization does not bound that
contribution in Euclidean norm.

---

## 5. Exact actual-prime one-atom rigidity

The simplest possible alias can at least be removed arithmetically.

### Lemma 5.1 (five-prime one-atom no-go)

Assume the window contains five distinct primes.  There do not exist
`t!=0` and a real `c` such that

```text
c*a(t)=q_0.                                               (5.1)
```

#### Proof

Equation (5.1) says that `cos(t log(p/Y))=r=1/c` for every prime coordinate.
Choose `theta in [0,pi]` with `cos(theta)=r`.  For each prime `p`,

```text
t*log(p/Y)=2*pi*k_p+epsilon_p*theta,
epsilon_p in {+1,-1}.                                    (5.2)
```

Among five primes, three, say `p,q,r`, have the same `epsilon`.  Subtracting
the `q` equation gives

```text
t*log(p/q)=2*pi*(k_p-k_q),
t*log(r/q)=2*pi*(k_r-k_q).                               (5.3)
```

Neither integer difference is zero, since the primes are distinct and
`t!=0`.  Hence `log(p/q)/log(r/q)` is rational.  Clearing denominators and
exponentiating gives a multiplicative relation among the three distinct
primes, contradicting unique factorization.  QED.

This proof uses actual prime identities rather than node spacing.  It does
not extend automatically from one atom to two: a two-frequency exponential
polynomial can have many level-one crossings.

### Lemma 5.2 (quantitative one-atom Diophantine bill is too weak)

Choose the five primes in five fixed, pairwise separated subwindows of the
carrier window; the prime number theorem permits this for large `Y`.  If
`t in H` (hence `Y^.751<=t<=B`) and

```text
max_(i<=5)|c*cos(t*log(p_i/Y))-1|<=epsilon<1/4,            (5.4)
```

then the same branch-pigeonhole argument produces three primes `p,q,r` and
nonzero integers `k,l`, of size `O_w(B)`, for which

```text
0!=Lambda=l*log(p/q)-k*log(r/q),
|Lambda|<<_w sqrt(epsilon).                              (5.5)
```

Unique factorization makes `Lambda` nonzero.  Elementary rational
separation gives only

```text
|Lambda|>=exp[-O_w(B*log Y)],
epsilon>=exp[-O_w(B*log Y)].                             (5.6)
```

#### Proof

Equation (5.4) implies `|c|>=1-epsilon`.  Let `cos(theta)` be the projection
of `1/c` onto `[-1,1]`; then each cosine in (5.4) differs from `cos(theta)`
by `O(epsilon)`.  Uniformly, this puts its phase within
`O(sqrt(epsilon))` of one of the two level-set branches
`2*pi*m+-theta`.  Three of the five primes use the same branch.  Subtracting
the equation for `q` gives

```text
t*log(p/q)=2*pi*k+O(sqrt(epsilon)),
t*log(r/q)=2*pi*l+O(sqrt(epsilon)).                       (5.7)
```

The fixed separation of the subwindows and `t in H` make `k,l` nonzero and
of size comparable to `t`, up to constants depending on `w`.  Cross
multiplication in (5.7) proves the upper bound in (5.5).  On the other hand,
`Lambda` is the logarithm of a nonunit positive rational whose numerator
and denominator are at most `exp[O_w(B log Y)]`.  Distinct positive integers
of that size have logarithmic ratio at least `exp[-O_w(B log Y)]`, proving
(5.6).  QED.

Thus exact unique-factorization nonvanishing does not automatically provide
the polynomial augmented-minor bound (7.4).  Standard linear-forms-in-
logarithms technology improves (5.6), but with prime heights of size `Y` it
still does not directly give a uniform `Y^(-O(1))` bound at arbitrary real
frequencies.  The multi-atom determinant is harder still.

---

## 6. Coarse harmonic-grid rigidity

A second exact result removes one natural FFT-style atomic family.

### Theorem 6.1 (commensurable frequency order bill)

Let the support frequencies be `t_j=m_j*tau`, where `tau!=0` and the `m_j`
are nonzero integers with `|m_j|<=D`.  If a signed atomic measure on those
frequencies represents `q_0`, then, for `M_p` prime coordinates in the
window,

```text
D>=M_p/4.                                                 (6.1)
```

Consequently a legal harmonic grid with `|t_j|<=B` must have

```text
|tau|<=4B/M_p=Y^(17/33+o(1)).                             (6.2)
```

#### Proof

Put `z_p=exp(i*tau*log(p/Y))`.  The interpolation equations say

```text
sum_j c_j*(z_p^(m_j)+z_p^(-m_j))/2=1.                    (6.3)
```

After multiplication by `z^D`, the left side minus one is a nonzero
polynomial of degree at most `2D`.  It is nonzero because its Laurent
polynomial before multiplication has no zero-frequency term but is being
compared with the constant one.

Every value of `z_p` occurs for at most two distinct primes.  Indeed, three
colliding primes would give two equations
`tau log(p/q),tau log(r/q) in 2*pi*Z`, and the same unique-factorization
argument as Lemma 5.1 gives a contradiction.  Thus (6.3) supplies at least
`M_p/2` distinct roots.  A nonzero degree-`2D` polynomial has at most `2D`
roots, proving (6.1).  Since `D|tau|<=B`, (6.2) follows.  QED.

This is a conductor/order obstruction, not a TV bound.  Fine harmonic grids
with spacing below `B/M` remain legal, and arbitrary incommensurable atoms
are outside the theorem.

---

## 7. Exact actual-prime exterior and dual audit

This section keeps the actual prime-power rows throughout.  Let `V` be the
`M` by `dR` matrix whose columns are the chosen packet jets
`a^(m)(tau_j)`, after deleting any dependent columns, and put

```text
G=V^*V,       b=V^*q_0,
G_tilde=[q_0 V]^*[q_0 V]=[[M,b^*],[b,G]].                 (7.1)
```

### Proposition 7.1 (directional exterior identity)

Exactly,

```text
dist(q_0,Ran(V))^2=M-b^*G^(-1)b
                   =det(G_tilde)/det(G).                 (7.2)
```

Moreover Cauchy--Binet writes the numerator as

```text
det(G_tilde)=sum_(|I|=dR+1)|det([q_0 V]_I)|^2,            (7.3)
```

where `I` ranges over subsets of the **actual prime-power coordinates**.

#### Proof

The first equality is the orthogonal-projection formula.  The second is the
block determinant/Schur-complement identity, and (7.3) is Cauchy--Binet.
If the original jet list is dependent, first pass to any basis of its
range.  QED.

This identifies precisely what an exterior-power proof has to show.  A
large unaugmented `det(G)` says that the jets span a well-conditioned
subspace, but says nothing about whether that subspace contains `q_0`.
The required actual-prime statement is an *augmented* minor estimate such
as

```text
det(G_tilde)>=Y^(-O(1))*M*det(G),                         (7.4)
```

uniformly for the admissible large-value centers.  Merely proving one
minor nonzero is also insufficient for the desired power cost; (7.4) is a
quantitative resultant bound for arbitrary real centers up to `B`.

### Proposition 7.2 (coherence route is power-short)

Even granting the current polylogarithmic prime-twist estimate to every
weighted jet correlation, ordinary Gershgorin or block restricted
invertibility cannot prove (7.4).

Indeed products of jet columns reduce to fixed linear combinations of

```text
Q_r(x)=sum_(n in N_Y)u_n^r*exp(i*x*u_n)                  (7.5)
```

at `x=tau_j-tau_k` and `x=tau_j+tau_k`.  After normalizing and
orthogonalizing within each packet, a scalar coherence bound `eta` gives
only

```text
lambda_min(G_normalized)>=1-(dR-1)*eta.                  (7.6)
```

Since `dR=C^2Y^o(1)`, this route requires

```text
eta<<C^(-2)*Y^(-o(1))=Y^(-.0360606468...-o(1)).           (7.7)
```

The available `(log Y)^(-3/10)` scale is asymptotically much larger.  The
block version has the same issue: it needs off-block norm `o(1/R)`.  This is
not a defect in constants.

There is a second, directional saturation.  Write normalized jet columns
as `v_alpha` and `v_0=q_0/sqrt(M)`.  Peak columns can have
`|<v_0,v_alpha>|` of order `1/C`; with `R` of order `C^2`, the Bessel sum

```text
sum_alpha |<v_0,v_alpha>|^2
```

is already of order one.  Thus even ideal mutual orthogonality is exactly
at the scale where `v_0` may lie in their span.  A proof needs a
carrier-specific saving in the augmented family, not only conditioning of
the jet family.

### Proposition 7.3 (difference-set energy still permits one null direction)

There is a stronger actual-integer average input than pairwise coherence,
but it remains nondirectional.  For a `1`-separated center set
`T={tau_1,...,tau_R}`, put

```text
x(t)=(n^(it))_(n in N_Y),       K(s)=<x(0),x(s)>.
```

Heath--Brown's difference-set theorem (in the normalization quoted as
[Guth--Maynard, Theorem 1.6](https://arxiv.org/abs/2405.20552)) gives

```text
sum_(j,k<=R)|K(tau_j-tau_k)|^2
 <=Y^o(1)*[R^2*Y+R*Y^2+R^(5/4)*B^(1/2)*Y].               (7.8)
```

For `R<=C^2Y^o(1)` at the target cost, the middle term dominates: relative
to `R*Y^2`, the first and third terms have fixed-power factors at most

```text
R/Y<=Y^(-.9639...),
R^(1/4)*B^(1/2)/Y
 <=Y^(kappa/2+25/33-1)=Y^(-.2334...).                    (7.9)
```

Thus, for the complex exponential-column Gram matrix `G_X`,

```text
tr(G_X^2)<=R*M^2*Y^o(1),       tr(G_X)=R*M.              (7.10)
```

The participation ratio `(tr G_X)^2/tr(G_X^2)` is consequently
`R*Y^(-o(1))`.  This validates power-scale rank and average conditioning on
the actual rows, and it also applies after adjoining the zero-frequency
carrier column.  But (7.10) is fully compatible with that augmented matrix
having one zero eigenvalue: deleting one direction changes neither trace
estimate at this scale.  Hence difference-set energy/restricted
invertibility still does not establish the directional Schur complement
(7.2).  Weighted fixed-order jets obey the same exponent ledger after
rescaling their bounded coefficients.

### Proposition 7.4 (exact directional dual)

Let `C_*(Y,H)` be the least TV norm of a measure representing `q_0`.  Then

```text
C_*(Y,H)=sup_(z!=0) <z,q_0>/sup_(t in H)|<z,a(t)>|.       (7.11)
```

This is the finite-dimensional Hahn--Banach dual of the atomic norm.  It
also shows what must supplement (7.4): a vector separating `q_0` from the
peak jets must still have controlled correlation with **every** low-peak
column.  The choice `z=q_0` recovers the scalar route (2.7).  A genuinely
new transversality route must construct an actual-prime `z` with

```text
<z,q_0> >=Y^(kappa-o(1))*sup_(t in H)|<z,a(t)>|.          (7.12)
```

No such vector is supplied by rank, Cauchy--Binet, or the present
polylogarithmic coherence estimate.

This audit deliberately does not promote a uniform-log-lattice
counterexample into an actual-prime obstruction.  Such a lattice fails the
integer Dirichlet-polynomial hypothesis used in Lemma 3.2.  It remains only
a warning that packing-only theorems are false; (7.4) and (7.12) are posed
and must be proved on the actual rows.

---

## 8. Decision and next admissible theorem

What is now proved:

```text
cheap L1 representation => one extreme actual prime-phase value     EXACT;
at least half-unit TV localized on that extreme set                  EXACT;
fourth moment localizes peaks to absolute length C^4*Y^o              EXACT;
large values cover significant set by <=C^2*Y^o fixed packets        EXACT;
shrinking cover has <=C^3*Y^o packets                                EXACT;
packet contribution has Y^.036061 approximate dimension at target    EXACT;
directional augmented-determinant and atomic dual identities          EXACT;
actual difference-set Gram energy has power-scale effective rank      EXACT;
one actual-prime high atom cannot represent the carrier               EXACT;
elementary quantitative one-atom angle is only exp[-O(B log Y)]       EXACT;
coarse commensurable harmonic grids pay order >=M/4                  EXACT;
unaugmented determinant/coherence closure                            CLOSED. (8.1)
```

What remains open:

```text
pointwise |S_Y(t)|<=M*Y^(-delta), delta>kappa             NOT PROVED;
exceptional packet jets uniformly transverse to q_0      NOT PROVED;
arbitrary incommensurable atomic TV lower bound           NOT PROVED;
explicit subpower atomic design                           NOT FOUND;
full carrier-aware C(L,H) dichotomy                       NOT DECIDED;
uniform zero-free strip                                   NOT PROVED. (8.2)
```

The next admissible result must use the actual prime phases in one of two
ways:

1. prove the scalar pointwise bound (2.7), which immediately gives the
   desired atomic cost lower bound; or
2. conditional on the rare large values in (2.8), prove a quantitative
   augmented-minor/transversality bound of the form (7.4), together with
   control of the low-correlation remainder as in the dual condition (7.12).

Restricted invertibility after replacing the actual packet jets by generic
vectors, or another Lebesgue measure estimate for the exceptional set, does
not meet this requirement.

---

## 9. Reproduction

Run

```bash
python3 results/verify_singular_atomic_span_gate.py
```

to replay the exponent ledger, actual multiplicative-energy check, and
directional Schur-complement identity in floating arithmetic.  The analytic
proofs above do not depend on the floating check.
