# R133 high-jet Euler-recurrence gate

## Status

This report tests an individual-zero replication mechanism which stays
entirely in `Re(s)>1`.  It therefore **does bypass the contour-winding
obstruction** in R122 and R126: no logarithm is continued around a zero and
no zero-bearing boundary function is approximated by a nonvanishing Euler
product.

The recurrence engines proved or modeled here do not produce a fixed
strip.  There is an exact mismatch between the double-exponential scale
at which the torus-volume pigeonhole argument **guarantees** returns and
the scale on which Cauchy can still localize a zero.  This is not a
deterministic lower bound for the first return of the actual prime-log
orbit; exceptionally early or overabundant arithmetic returns remain a
live conditional successor.

```text
large derivative at 1+r+i gamma from a nearby zero       YES
bounded-gap sequence of useful derivative orders         YES
finite-prime recurrence with an explicit return count    YES
Cauchy conversion of a copied jet into a nearby zero      YES
overlap for the guaranteed torus-volume return engine     NO
exceptional early prime-log return theorem                OPEN
fixed zero-free strip                                     NOT PROVED
zeros approaching one                                     NOT PROVED
```

For a derivative of order `k`, the positive Euler series has saddle

```text
log n asymp k/r.                                           (0.1)
```

Absolute control of the tail therefore requires a prime cutoff
`X=exp(lambda k/r)` with `lambda>1`.  Recurring the corresponding prime
phases first becomes guaranteed on the scale

```text
log log T >= (lambda/r+o(1))k.                             (0.2)
```

On the other hand, if the copied derivative is to force a zero in
`Re(s)>1-eta`, Cauchy's inequality permits only

```text
log log T <=
  [log((r+eta)/(r+delta_*))+o(1)]k,                        (0.3)
```

where `r+delta_*` is the distance from the source point to its nearest
singularity.  The sharp geometric inequality

```text
r log((r+eta)/(r+delta_*)) <= eta-delta_*                  (0.4)
```

shows that the **guaranteed scale** (0.2) and the localization scale (0.3)
cannot overlap whenever `eta-delta_*<1`, since `lambda>1`.  In particular
the pigeonhole/torus-volume engine has no overlap for any strip relevant
to the nontrivial zeros.  The inequality does not exclude a prime-log
orbit which enters the tiny return cylinder much earlier than its Haar
volume predicts.

Optimized partial-prime workarounds are also audited.  Instead of recurring
the whole jet, one can align only the cheapest left tail of its prime
saddle, or choose a sparse packet near the largest individual Euler
coefficients, and control the unaligned primes in mean square.  The first
optimization is governed by an exact Legendre-duality identity.  The
second has best possible coherent-packet entropy rate
`log((1+r)/d)`, which is still strictly larger than the Cauchy rate
`log(R/d)` whenever `R<r+1`.  Thus the failure is not an artifact of
demanding recurrence of too many harmless tail phases.

Date: 2026-08-08.

Predecessors:

* [`R89-DIFFERENTIATED-POSITIVITY-GATE.md`](R89-DIFFERENTIATED-POSITIVITY-GATE.md),
  for the differentiated explicit formula and the local Turan
  `1/log T` tradeoff;
* [`R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md`](R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md),
  for the distinction between compact-local convergence and
  height-uniform recurrence;
* [`R122-ZERO-REPLICATION-DENSITY-GATE.md`](R122-ZERO-REPLICATION-DENSITY-GATE.md),
  for the replication-versus-zero-density comparison; and
* [`R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md),
  for the contour-winding version of the replication obstruction.

## 1. The positive Euler jet and its zero expansion

Put

```text
D(s)=-zeta'(s)/zeta(s),
J_k(s)=(-1)^k D^(k)(s)/k!,                  k>=1.       (1.1)
```

In `Re(s)>1` this is the absolutely convergent positive-coefficient
Dirichlet series

```text
J_k(s)=sum_(n>=2) Lambda(n)(log n)^k/[k! n^s].         (1.2)
```

The differentiated Hadamard formula is

```text
J_k(s)=1/(s-1)^(k+1)
       -sum_rho 1/(s-rho)^(k+1)
       -sum_(j>=1)1/(s+2j)^(k+1).                     (1.3)
```

The sums in (1.3) are absolutely convergent.  Thus a zero is literally a
pole of `D`, and high Taylor coefficients at a point to the right of one
record the nearest pole without ever crossing the line `Re(s)=1`.

Let

```text
z_*=1+r+i gamma,                    r>0,              (1.4)
```

and suppose `rho_0=1-delta+i gamma` is a zeta zero.  Let `d` be the
distance from `z_*` to the nearest pole of `D`.  Once `z_*` is chosen so
that the pole at one is not nearer than `rho_0`, the nearest pole is a
zeta zero and

```text
r<=d<=r+delta.                                        (1.5)
```

It is convenient to write

```text
d=r+delta_*,                  0<=delta_*<=delta.       (1.6)
```

A nearest zero then has real part at least `1-delta_*`, since its
Euclidean distance from `1+r+i gamma` is `r+delta_*`.

### Lemma 1.1 -- a nearest pole leaves bounded-gap large jets

There are constants `M>=1`, `c_*>0`, and `K_0`, depending on the fixed
source point `z_*`, such that for every `K>=K_0` there is an integer

```text
k in {K,...,K+M-1}                                    (1.7)
```

for which

```text
abs(J_k(z_*))>=c_* d^(-k-1).                           (1.8)
```

#### Proof

There are finitely many poles of `D` on the nearest circle
`abs(s-z_*)=d`; call them `w_1,...,w_M`, combining coincident poles by
multiplicity.  Subtract their principal parts.  The remainder is
holomorphic on a strictly larger disc, so its `k`th normalized Taylor
coefficient is `O(d_1^(-k))` for some `d_1>d`.

After multiplication by `d^(k+1)`, the nearest-pole contribution is a
finite power sum

```text
S_k=sum_(j=1)^M m_j exp[-i(k+1)theta_j],               (1.9)
```

with positive integral multiplicities `m_j`.  No `M` consecutive values
of this power sum can vanish: the resulting linear system has a
Vandermonde matrix.  The closure of the phase orbit is compact, so the
maximum of every `M` consecutive absolute values has a positive uniform
lower bound.  The exponentially smaller remainder can be absorbed for
large `K`.  This proves (1.8).  QED.

This observation removes one apparent local-density problem.  The source
zero and its nearest-pole cluster are fixed while the copied height tends
to infinity, so their finite multiplicity only costs a bounded number of
adjacent derivative orders.  The obstruction below occurs later.

## 2. Cauchy localization at the copied height

The following standard local form is the only analytic-continuation input
needed.

### Lemma 2.1 -- zero-free disc jet bound

Fix `r,R_0>0` and `0<R<R_0`.  If the disc

```text
abs(s-(1+r+it))<=R_0                                  (2.1)
```

contains no zeta zero and is far from the pole at one, then

```text
abs(J_k(1+r+it))
   <<_(r,R,R_0) log(abs(t)+3) R^(-k).                 (2.2)
```

#### Proof

The local explicit formula and the unit-interval zero count give

```text
zeta'(s)/zeta(s)=sum_(abs(Im rho-t)<=C)1/(s-rho)
                  +O_(C)(log(abs(t)+3))               (2.3)
```

uniformly in a fixed bounded strip.  The enlarged zero-free disc keeps
the displayed denominators a fixed distance from the smaller circle
`abs(s-(1+r+it))=R`, and there are `O(log(|t|+3))` of them.  Hence `D` is
`O(log(|t|+3))` on that circle.  Cauchy's derivative inequality proves
(2.2).  QED.

Consequently, if for some fixed `d<R<R_0`

```text
abs(J_k(1+r+it))>=c d^(-k-1),                          (2.4)
```

then a zero must occur in the enlarged disc once

```text
log(abs(t)+3)<c' d^(-1)(R/d)^k.                       (2.5)
```

At the exponential-rate level this is

```text
log log abs(t) <=[log(R/d)+o(1)]k.                    (2.6)
```

To force the resulting zero into `Re(s)>1-eta`, one must take

```text
R_0<r+eta.                                             (2.7)
```

Letting `R` approach `R_0` gives the largest possible localization rate

```text
L(r,d,eta)=log((r+eta)/d).                             (2.8)
```

For `d=r+delta_*`, concavity of the logarithm gives the sharp elementary
bound

```text
r L(r,d,eta)
 =r log(1+(eta-delta_*)/(r+delta_*))
 <=r(eta-delta_*)/(r+delta_*)
 <=eta-delta_*.                                        (2.9)
```

This inequality is uniform in `r`; moving the observation line farther
right cannot improve the product of horizontal resolution and Euler
saddle width.

## 3. What it costs to recur the actual source jet

At the real point `1+r`, (1.3), or the prime number theorem applied to
(1.2), gives

```text
J_k(1+r)=r^(-k-1)exp(o(k)).                            (3.1)
```

For `lambda>1`, put

```text
X=exp(lambda k/r).                                     (3.2)
```

The absolute tail of (1.2) has the gamma-distribution estimate

```text
sum_(n>X) Lambda(n)(log n)^k/[k! n^(1+r)]
 <=r^(-k-1)exp[-k I(lambda)+o(k)],                     (3.3)

I(lambda)=lambda-1-log lambda.                         (3.4)
```

Thus, in order that this tail be `o(d^(-k-1))`, it is enough to choose

```text
I(lambda)>log(d/r).                                    (3.5)
```

In particular every admissible cutoff has `lambda>1`.  When `d/r` is
close to one, `lambda` may approach one, but it cannot cross it.

Let

```text
P_(k,X)(s)=sum_(n<=X) Lambda(n)(log n)^k/[k! n^s].     (3.6)
```

If every prime `p<=X` obeys

```text
norm(tau log p/(2pi))<=alpha,                          (3.7)
```

then unique factorization gives

```text
abs(n^(-i tau)-1)<<alpha log X,             n<=X.     (3.8)
```

It follows from (3.1) that the finite head at `z_*+i tau` differs from
the head at `z_*` by at most

```text
alpha log X r^(-k-1)exp(o(k)).                         (3.9)
```

Taking

```text
alpha<=exp[-k log(d/r)+o(k)]/log X                     (3.10)
```

makes (3.9) smaller than a fixed fraction of the useful value (1.8).

### Lemma 3.1 -- effective finite-torus return count

For arbitrary real frequencies `omega_1,...,omega_D` and
`0<alpha<1/4`, the number of nonzero integers `tau` with `abs(tau)<=T`
and

```text
norm(tau omega_j)<=2alpha,             1<=j<=D,        (3.11)
```

is at least

```text
c T (c alpha)^D-1.                                     (3.12)
```

#### Proof

Place the `T+1` points

```text
(n omega_1,...,n omega_D),             0<=n<=T,        (3.13)
```

in a partition of the `D`-torus into at most `(C/alpha)^D` boxes of
diameter `alpha` in each coordinate.  One box contains at least
`(T+1)(c alpha)^D` points.  Subtract its first point from all the others.
The resulting distinct integer differences satisfy (3.11).  QED.

This avoids any ineffective lower bound for a linear form in prime
logarithms.  Applied to the `D=pi(X)` prime phases in (3.7), the box lemma
guarantees a positive count of returns once

```text
log T >=D log(C/alpha).
```

Since

```text
D=exp[(lambda/r+o(1))k],                (3.14)
```

the sufficient pigeonhole recurrence scale is

```text
log log T >=(lambda/r+o(1))k.           (3.15)
```

The same returns recur every member of any fixed-length jet, since the
extra polynomial factors in `log n` do not alter (3.14).

It is essential not to reverse Lemma 3.1.  Equation (3.15) is a scale by
which the box argument guarantees returns in bulk; it is **not** a lower
bound for the first return, nor an upper bound for the number of returns
below that scale.  A one-parameter orbit can hit a small torus box much
earlier than its volume suggests if its frequencies have an exceptional
simultaneous approximation.  No deterministic Diophantine lower bound of
the strength needed here is proved for the vector `(log p/(2pi))_(p<=X)`.

## 4. The exact guaranteed-engine no-overlap theorem

### Theorem 4.1 -- pigeonhole-guaranteed high-jet gate

Let a fixed source zero produce the large jets in Lemma 1.1, let
`d=r+delta_*` be the nearest-pole distance, and attempt to copy those jets
by absolute-tail finite-prime recurrence.  If the copied jets are to force
zeros in

```text
Re(s)>1-eta,                                             (4.1)
```

then Lemma 3.1 certifies an asymptotic height window only if

```text
lambda/r<log((r+eta)/d)                                 (4.2)
```

for some `lambda` satisfying (3.5).  No such **certified** window exists
when

```text
eta-delta_*<1.                                          (4.3)
```

#### Proof

The sufficient recurrence scale furnished by Lemma 3.1 is (3.15), while
Cauchy localization has the upper threshold (2.6)--(2.8).  An overlap
between those two proved ranges requires (4.2).  But (2.9) and
`lambda>1` give

```text
r log((r+eta)/d)<=eta-delta_*<1<lambda,                 (4.4)
```

the reverse of (4.2).  QED.

There is a useful equivalent power ledger.  Localization first requires

```text
k log((r+eta)/(r+delta_*)) >=log log T.                 (4.5)
```

Together with (2.9), this forces

```text
k/r >=log log T/(eta-delta_*).                          (4.6)
```

The necessary Euler cutoff is consequently at least

```text
X=exp(lambda k/r)
 >=(log T)^[lambda/(eta-delta_*)+o(1)].                 (4.7)
```

Since `lambda/(eta-delta_*)>1`, even a constant-width cylinder for these
prime phases has Haar volume at most on the scale

```text
exp[-(log T)^(A+o(1))],                 A>1.            (4.8)
```

The Haar volume at this scale is smaller than the reciprocal of the
available interval, so Lemma 3.1 contains no guaranteed return below
height `T`.  The loss in this guaranteed engine is a power of `log T` in
the exponent, not a removable logarithmic factor.  This volume statement
does not rule out an exceptional arithmetic hit.

The certified-range comparison remains unfavorable if `r` is allowed to
vary with `k`.
When `k/r` tends to infinity, the pointwise inequality (4.4) remains in
force.  When `k/r` stays bounded, the Cauchy gain in (4.5) is bounded and
cannot dominate `log log T`.

## 5. The conditional zero-density theorem and exponent ledger

It is still useful to record exactly what would have happened had (4.2)
held.  Choose

```text
k=c log log T.                                         (5.1)
```

The recurrence box count (3.12) would give

```text
# returns up to T >=T exp[-(log T)^(c lambda/r+o(1))].  (5.2)
```

Thus

```text
c lambda/r<1                                           (5.3)
```

would give `T^(1-o(1))` separated copied jets.  Cauchy would force a zero
at each copied height provided

```text
c log((r+eta)/d)>1.                                    (5.4)
```

The simultaneous existence of `c` in (5.3)--(5.4) is precisely (4.2).
The fixed length of the source-order blocks in Lemma 1.1 changes only
`o(1)` terms.

Discs centered at distinct integer shifts have bounded overlap, so the
conclusion would be

```text
N(1-eta,T)>=T^(1-o(1)).                                (5.5)
```

The imported Guth--Maynard estimate

```text
N(sigma,T)<=T^[(30/13)(1-sigma)+o(1)]                  (5.6)
```

would contradict (5.5) for

```text
eta<13/30.                                             (5.7)
```

This is the exact conditional replication theorem requested by the
zero-density strategy.  The density comparison is more than strong
enough; it is the incompatible recurrence/localization window before it
which fails.  Bellotti's stronger `O(1)` density in a region adjacent to
the moving Korobov--Vinogradov boundary does not change (4.4), and hence
does not repair the mechanism.

## 6. Mean-square recurrence is on the wrong side of the target

Perhaps the full phase cylinder is wasteful: one could hope that a copied
large modulus occurs at typical shifts.  The Besicovitch mean square of
(1.2) is coefficient-diagonal:

```text
norm(J_k(1+r+i .))_(B^2)^2
 =sum_(n>=2) Lambda(n)^2(log n)^(2k)/[(k!)^2 n^(2+2r)]. (6.1)
```

The prime number theorem, followed by Stirling, gives

```text
norm(J_k(1+r+i .))_(B^2)^(1/k)
 =2/(1+2r)+o(1)
 =1/(r+1/2)+o(1).                                     (6.2)
```

Prime powers `p^a`, `a>=2`, have strictly smaller exponential base

```text
2a/[2a(1+r)-1]<2/(1+2r),                              (6.3)
```

so (6.2) is not hiding a proper-power contribution.

For the source signal with `d=r+delta`, define

```text
H=log((r+1/2)/(r+delta)),                              (6.4)
L=log((r+eta)/(r+delta)).                              (6.5)
```

Here `H` is the target-over-RMS exponential advantage and `L` is the
largest Cauchy localization exponent.  For every `eta<1/2`,

```text
H>L.                                                   (6.6)
```

Thus a jet large enough to detect a zero to the right of `1-eta` is
exponentially larger than the root-mean-square jet, by a factor whose
exponent already exceeds the available localization exponent.  A second
moment can upper-bound the frequency of such exceptional values; it gives
no lower bound with which to replicate one.  Ordinary mean-value
recurrence therefore cannot replace the phase cylinder.

This is the mean-square shadow of Theorem 4.1.  The next section tests a
more favorable rare-event construction rather than stopping at (6.6).

### 6.1 A random-prime-torus upper bound for every large-value event

The mean-square comparison can be upgraded from a warning to a sharp
large-deviation gate in the natural random Euler model.  Give each prime
an independent Haar phase `omega_p` and group all powers of that prime:

```text
X_(p,k)(omega_p)
 =sum_(a>=1) (log p)(a log p)^k
   omega_p^a/[k! p^(a(1+r))].                          (6.7)
```

These blocks are independent and have mean zero.  The saddle calculation
used below in (7.13)--(7.14), now allowing all powers of one prime, gives

```text
max_p norm(X_(p,k))_infinity
 <=[1/(1+r)+o(1)]^k.                                  (6.8)
```

Their total variance has square root (6.2).  Bernstein's inequality,
applied to real and imaginary parts, therefore gives, for
`V=d^(-k+o(k))`,

```text
Prob(abs(sum_p X_(p,k))>=V)
 <=4 exp{-c min(V^2/S_k^2,V/B_k)}
 <=exp{-exp[(G+o(1))k]},                              (6.9)

G=min{2 log((r+1/2)/d), log((1+r)/d)}.                (6.10)
```

If the desired disc has `R<r+eta` with `eta<1/2`, then its Cauchy rate

```text
L=log(R/d)                                             (6.11)
```

satisfies

```text
G>L.                                                   (6.12)
```

Indeed both entries in the minimum (6.10) exceed `L`: the first by
`R<r+1/2`, and the second by `R<r+1`.

At the Cauchy height ceiling, `log T<=exp[(L+o(1))k]`.  Even if the
vertical prime orbit sampled its growing torus perfectly at the natural
Haar scale, its expected large-value count would be bounded by

```text
T Prob(abs(J_k)>=V)
 <=exp{exp[(L+o(1))k]-exp[(G+o(1))k]}=o(1).            (6.13)
```

Thus ideal mean-value mixing is not merely unable to prove enough
replicas: its natural model predicts no useful large value before Cauchy
localization expires.  This does not rule out a specially structured
arithmetic subsequence of the one-parameter prime orbit, but such a
subsequence would have to beat the Haar large-deviation scale rather than
follow from ordinary moments or equidistribution.

There is a matching finite-height reason that the exceptional subsequence
cannot simply be discarded.  For a Dirichlet-polynomial truncation of
length `X`, the deterministic mean-value theorem gives only

```text
meas{t<=T:abs(J_k(1+r+it))>=d^(-k)}
 <<T exp[-2H k+o(k)]                                  (6.14)
```

when `T>>X`.  At `k asymp log log T` this is merely a power of `log T`,
not the double-exponential Haar bound (6.9).  To recover (6.9) by a
`2q`th moment one needs `q` on the scale `exp(Gk)`, while diagonal
finite-height control requires roughly

```text
q log X<=log T.                                        (6.15)
```

At the Cauchy ceiling the right side has exponential rate `L`, whereas
`q` has rate `G>L`.  Thus the moment needed to prove natural Haar rarity
is itself unavailable before localization expires.  This is why the
report leaves exceptional arithmetic returns open rather than promoting
the random-torus estimate to a deterministic no-go.

## 7. Optimized partial-prime alignment

The strongest simple workaround is to manufacture a large jet rather
than copy all phases of the source jet.  Fix `0<x<1`, set

```text
Y=exp(x k/r),                                           (7.1)
I(x)=x-1-log x,
q_x=exp[-I(x)]=x exp(1-x).                             (7.2)
```

The mass from prime bases `p<=Y` is the left large-deviation tail of the
same gamma saddle:

```text
sum_(p<=Y) (log p)^(k+1)/[k! p^(1+r)]
 =r^(-k-1)exp[-k I(x)+o(k)]
 =(r/q_x)^(-k+o(k)).                                   (7.3)
```

Write

```text
d_x=r/q_x.                                             (7.4)
```

Aligning just these prime phases in a fixed arc produces a head of size
`d_x^(-k+o(k))`.  Its phase cylinder has Haar density

```text
exp[-C pi(Y)]
 =exp{-exp[(x/r+o(1))k]}.                              (7.5)
```

The unaligned prime bases are independent coordinates in the limiting
prime torus.  When

```text
d_x<r+1/2,                                             (7.6)
```

(6.2) and Chebyshev show that a positive relative part of this cylinder
has complementary sum smaller than half the aligned head.  Thus, granting
quantitative sampling of the growing prime torus at its natural Haar
scale, (7.5) is the optimistic onset exponent for a genuine large value.
This is strictly more favorable than recurring the absolute right tail,
because `x<1<lambda`.

Such a large value could force a zero in a disc of radius `R>d_x` only in
the window

```text
x/r<log(R/d_x)=log(q_x R/r).                           (7.7)
```

Yet the following exact identity closes that window.

### Lemma 7.1 -- entropy/Cauchy Legendre duality

For `0<x<=1`,

```text
log q_x
 =min_(u>=0){x u-log(1+u)}.                            (7.8)
```

Consequently, for every `r>0` and `0<eta<=1`,

```text
log[q_x(1+eta/r)]<=x/r.                                (7.9)
```

#### Proof

The minimum in (7.8) occurs at `u=(1-x)/x` and equals

```text
1-x+log x=log[x exp(1-x)]=log q_x.                    (7.10)
```

Evaluate (7.8) at `u=1/r`, and use
`1+eta/r<=1+1/r`.  This gives (7.9).  QED.

Since a zero in the desired strip requires `R<r+eta`, (7.9) yields

```text
log(q_x R/r)<x/r,                     eta<=1,          (7.11)
```

which is the reverse of (7.7).  Therefore even the optimized monotone
prime-head cylinder, with the remaining primes granted ideal conditional
mean-square behavior and **natural-scale Haar equidistribution**, has no
usable certified height window for a nontrivial fixed strip.  This does
not preclude an exceptional overconcentration of the actual prime-log
orbit in that cylinder.

Lemma 7.1 formalizes the large-deviation content of `H>L` in Section 6.

### 7.2 Sparse packets near the largest individual coefficients

The monotone head is not literally the cheapest coherent packet in every
parameter range.  A sparser set of primes near the maximum of one
individual coefficient can sometimes have a smaller phase dimension.
That optimization also has an exact gate.

For a prime with

```text
log p=a k+o(k),                                        (7.12)
```

its coefficient in `J_k(1+r)` has exponential base

```text
[(log p)^(k+1)/(k! p^(1+r))]^(1/k)
 =B_r(a)+o(1),
B_r(a)=a exp[1-(1+r)a].                                (7.13)
```

The maximum over `a>0` occurs at `a=1/(1+r)` and is

```text
max_a B_r(a)=1/(1+r).                                  (7.14)
```

The same exponential maximum holds after all powers of one fixed prime
base are grouped together; the sum over powers contributes only a
subexponential factor.  Therefore a coefficient-positive coherent packet
with total size `d^(-k+o(k))`, where `d<1+r`, must involve at least

```text
exp{k log((1+r)/d)+o(k)}                               (7.15)
```

independent prime bases.  Aligning a fixed arc for those bases has no
better cylinder scale than

```text
exp{-exp[k log((1+r)/d)+o(k)]}.                        (7.16)
```

Equivalently, its inverse-Haar-volume exponent in `log log T` is

```text
E_sparse=log((1+r)/d).                                 (7.17)
```

But Cauchy localization into a disc of radius `R<r+eta` has rate
`log(R/d)`.  For every `eta<1`,

```text
log(R/d)<log((1+r)/d)<=E_sparse.                       (7.18)
```

Thus the coefficient-optimal sparse coherent packet also runs out of
height **under natural-scale torus sampling** before it can force a zero.
This argument covers the parameter range in which a central packet
improves on the monotone left tail.  It is not a deterministic lower bound
for when the prime-log orbit can first align that packet.

Neither (7.11) nor (7.18) is a theorem that every conceivable signed or
correlated large-value event has the same entropy.  Together they prove
that both natural coefficient-positive optimizations--a cumulative
left-saddle head and a coefficient-maximizing sparse packet--do not evade
the full-tail gate.  A successful continuation would need a structured,
signed large-value set whose recurrence entropy beats both rates, not
merely a better tail estimate or a higher moment.

## 8. Relation to the classical `1/log T` wall

This construction genuinely avoids the *topological* winding problem:
all recurrence takes place in an absolutely convergent half-plane and
Cauchy's theorem is used only after a scalar jet has been copied.

It has two possible quantitative endings.

1. If one preserves the individual source jet using the proved
   pigeonhole/torus-volume recurrence count, Theorem 4.1 gives the stronger
   double-exponential entropy/localization mismatch.  There is no
   fixed-strip window certified by that recurrence engine.  An
   exceptionally early and sufficiently numerous family of arithmetic
   prime-log returns is not excluded.
2. If one abandons recurrence and instead applies a conventional Turan
   power-sum detector at the high target height, a vertical window of
   width `r` can contain `asymp r log T` competing zeros.  Resolving them
   costs derivative order

   ```text
   k>=c r log T.                                       (8.1)
   ```

   A zero at gap `delta` is then attenuated relative to the pole-scale
   Euler mass by

   ```text
   [r/(r+delta)]^k
    <=exp[-c delta log T+o(1)].                         (8.2)
   ```

   Retaining a constant signal forces

   ```text
   delta log T=O(1),                                   (8.3)
   ```

   exactly the R89 moving-region barrier.

Thus the high-jet idea bypasses winding but not the underlying resolution
cost for the engines presently controlled.  Volume-guaranteed recurrence
runs out of height before Cauchy can localize; ordinary Turan localization
falls back to `1/log T`.  Exceptional prime-log recurrence remains outside
both conclusions.

## 9. Verdict and the remaining conditional target

No fixed zero-free strip, and no sequence of zeros approaching one, has
been proved here.  The result is a fail-fast theorem for the
pigeonhole/torus-volume engine and the natural Haar large-deviation
variants, not for every possible arithmetic recurrence of the high jet:

```text
source nearest-pole signal                 d^(-k)
Cauchy height ceiling                      loglog T<k log(R/d)
full Euler guaranteed-return scale         loglog T>lambda k/r, lambda>1
strip geometry                             r log(R/d)<=eta-delta_*<1
optimized head inverse-Haar-volume scale   loglog T>x k/r
optimized head localization ceiling         loglog T<k log(q_x R/r)
Legendre duality                            log(q_x R/r)<=x/r
sparse packet inverse-Haar-volume scale     loglog T>k log((1+r)/d)
sparse coherent-packet localization ceiling loglog T<k log(R/d)
random-torus large-value entropy rate        min(2H,log((1+r)/d))>L
known fixed-strip zero density              exponent (30/13)eta
```

The most concrete successor is an arithmetic exceptional-return theorem.
For infinitely many useful orders `k`, it would have to produce, below
the Cauchy ceiling

```text
T_k<=exp{c(R/d)^k},                                    (9.1)
```

enough distinct shifts returning the required prime phases (or directly
returning the large jet) to beat the zero-density count
`T_k^((30/13)eta+o(1))`.  Haar volume predicts far fewer than one such
shift in this range, but Lemma 3.1 gives no upper bound and therefore does
not rule this out.  Proving it would require special simultaneous
approximation structure in the prime logarithms, not merely Kronecker
density.

Equivalently, one could reopen the route with a theorem producing a set of
large high-Euler-jet values whose **actual vertical-orbit** recurrence
entropy is strictly below its Cauchy localization rate, thereby beating
both the Legendre left-tail and sparse-packet Haar rates.  Neither phase
cylinders, absolute tails, ordinary moments, natural-scale
equidistribution, nor the standard Turan power-sum method supplies that
theorem.

## References

* Larry Guth and James Maynard,
  [*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
  for (5.6).
* Chiara Bellotti,
  [*A new zero-density estimate for zeta and the error term in the Prime Number Theorem*](https://arxiv.org/abs/2508.02041),
  for the stronger density result adjacent to the moving
  Korobov--Vinogradov boundary.
* Chiara Bellotti, Tim Trudgian, and Andrew Yang,
  [*Zero-free regions inspired by work of Heath-Brown*](https://arxiv.org/abs/2603.21490),
  for the current explicit `1/log t`-scale zero-free-region comparison.
