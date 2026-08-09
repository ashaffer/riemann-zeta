# R127 near-one mixed-contour density gate

Status: the proposed contour can be constructed and its two control
mechanisms can be joined on every fixed punctured contour.  It does not
currently exclude a zero.  A Jordan contour going from the universality
strip to the half-plane of absolute Euler convergence must contain at least
two transition arcs.  If their horizontal margin is `eta`, derivative
completion loses only `O(eta^2)` in ambient density, but direct finite-Euler
recurrence has phase-cylinder density

```text
exp{-exp(u/eta+o(1/eta))},                            (0.1)
```

where `u>0` is fixed by the requested boundary accuracy.  Thus the explicit
recurrence set is much smaller than the available derivative exceptional
set.  Hybrid universality gives positive density for each fixed `eta`, but
no lower bound uniform as `eta->0`.  At `eta=0` the missing joint statement
is topologically impossible for the zero-free random Euler product: it
would approximate a boundary of nonzero winding and hence create a zero.
The pole at `s=1` is not involved; all crossings occur near height `gamma`,
and the shifted pole leaves every fixed contour as the shift grows.

No fixed zero-free strip, and no failure of all fixed strips, is proved.

Date: 2026-08-07.

Predecessors:

* [`R122-ZERO-REPLICATION-DENSITY-GATE.md`](R122-ZERO-REPLICATION-DENSITY-GATE.md)
  for the Rouche replication lemma and the one-gap derivative gate;
* [`BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`](BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md)
  for fixed-prime conditioning and the random-Euler support obstruction;
* [`ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`](ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md)
  for the correct phase convention in the hybrid limit.

## 1. Geometry of a mostly-right contour

Assume that

```text
rho=beta+i gamma,     beta=1-delta>1/2               (1.1)
```

is a zero.  Choose `x_L<beta`, `a>0`, and `h>0` so that the rectangle

```text
Omega={x+iy:x_L<x<1+a, abs(y-gamma)<h}               (1.2)
```

has no zero on its boundary `Gamma` and contains `rho`.  We may also arrange
`x_L>1/2` and `h<abs(gamma)/2`.  Put

```text
m=min_(s in Gamma)|zeta(s)|>0.                        (1.3)
```

For

```text
0<eta<min(a,1-x_L),                                  (1.4)
```

split the boundary into

```text
K_- =Gamma intersect {Re(s)<=1-eta},
K_+ =Gamma intersect {Re(s)>=1+eta},
J_+ union J_-=Gamma minus (K_- union K_+).            (1.5)
```

The two `J`'s are the horizontal intervals crossing `Re(s)=1`; each has
length `2 eta`.  The rectangle is geometrically optimal at this scale.

### Lemma 1.1 -- two-crossing lower bound

Let a Jordan curve have points in both `Re(s)<=1-eta` and
`Re(s)>=1+eta`.  After deleting those two closed regions, the curve has at
least two connecting components, each of arclength at least `2 eta`.
Consequently the total transition length is at least `4 eta`.

**Proof.**  A Jordan curve has two disjoint routes between any chosen left
and right points.  Along each route the real part changes by at least
`2 eta`, while total variation dominates absolute displacement.  QED.

One may send the right edge far to the right, making an arbitrarily large
fraction of the perimeter lie in `Re(s)>1`.  Lemma 1.1 is unchanged.  A
thin teardrop or cusp changes constants, not the two crossings or their
minimum displacement.  Rouche uses a boundary supremum, so perimeter
fractions carry no weight.

If the intended left excursion is genuinely near-one, say

```text
x_L=1-O(delta),   h=O(delta),                         (1.6)
```

then a nonempty separated left piece requires `eta=O(delta)`.  This is the
near-one scaling used in Section 5.

## 2. The punctured mixed recurrence exists

On `K_-`, the target `zeta(s)` is continuous and nonzero.  The compact set
lies strictly in `1/2<Re(s)<1` and has connected complement.  Hybrid
universality therefore gives, simultaneously,

```text
sup_(s in K_-)|zeta(s+i tau)-zeta(s)|<epsilon,
norm(tau log p/(2 pi))<theta       for every p<=P,    (2.1)
```

on a set of positive lower density for every fixed
`eta,epsilon,theta,P`.  This is exactly the finite-prime case of
[Pankowski's hybrid joint universality
theorem](https://doi.org/10.4064/aa141-1-3), Theorem 1.1.  The phase sign in
(2.1) is correct because

```text
p^(-s-i tau)=p^(-s) exp(-i tau log p).                (2.2)
```

The same phase conditions control `K_+` by absolute convergence of the
Euler product.  Thus, for every fixed `eta>0`, there is a positive-lower-
density set `U_eta` on which

```text
sup_(s in K_- union K_+)
  |zeta(s+i tau)-zeta(s)|<epsilon.                    (2.3)
```

This is a genuine unconditional advance over asking for self-recurrence on
all of `Gamma`: the target has no zero on the observed compact and the
separating boundary has been opened twice.

What hybrid universality does **not** state is a lower bound for

```text
c_eta=liminf_(T->infinity) meas(U_eta intersect [T,2T])/T              (2.4)
```

uniform in the degenerating geometry.  The explicit 2025 theorem of Nakai
also exhibits a prime-coordinate cost exponential in the number of
controlled primes in its special fixed-disc setting; see [Effective hybrid
joint universality for Dirichlet L-functions](https://arxiv.org/abs/2512.02428),
Theorem 1.6 and Corollary 1.7.  It does not supply a shrinking-gap estimate
for the present contour.

## 3. Sharp cost of direct Euler control

This section records the cost rather than hiding it in almost periodicity.
For `s in K_+`, use the absolutely convergent logarithm and write

```text
D_tau(s)=log zeta(s+i tau)-log zeta(s)
 =sum_p sum_(k>=1) p^(-ks)(exp(-ik tau log p)-1)/k.   (3.1)
```

If the phase inequalities in (2.1) hold, then

```text
sup_(K_+)|D_tau|
 <=2 pi theta A(P,eta)+4 S(P,eta),                   (3.2)

A(P,eta)=sum_(p<=P) 1/(p^(1+eta)-1),
S(P,eta)=sum_(p>P) p^(-1-eta).                       (3.3)
```

Indeed, `|exp(-ik tau log p)-1|<=2 pi k theta` in the
head, and `-log(1-x)<=x/(1-x)` in the tail.

Let `lambda>0` be the logarithmic accuracy needed to make the right side of
(2.3) at most `epsilon`; for the fixed contour one can take

```text
lambda asymp min(1,epsilon/sup_(K_+)|zeta|).          (3.4)
```

The prime number theorem and partial summation give, with
`u=eta log P`,

```text
S(P,eta)=(1+o(1)) E_1(u),
E_1(u)=integral_u^infinity exp(-v) dv/v.              (3.5)
```

Choose the fixed `u=u(lambda)>0` so that `4E_1(u)<lambda/2`, and take

```text
P=exp((u+o(1))/eta).                                 (3.6)
```

This is the sharp prime-tail scale.  The cruder replacement of primes by
all integers inserts an unnecessary `log(1/eta)` in `log P`.

At (3.6), again by partial summation,

```text
A(P,eta)=log(1/eta)+O_lambda(1).                      (3.7)
```

It is enough to take

```text
theta=lambda/(8 pi A(P,eta))
      asymp_lambda 1/log(1/eta).                      (3.8)
```

Kronecker--Weyl gives the exact density of the full phase cylinder:

```text
d_eta=(2 theta)^pi(P).                                (3.9)
```

Since every set constructed by (2.1) lies inside that cylinder,

```text
c_eta<=d_eta,
-log d_eta=pi(P) log(1/(2 theta)),                    (3.10)
```

at every continuity value for the limiting density.  From (3.6)--(3.8),

```text
pi(P)=exp(u/eta+o(1/eta)),
d_eta=exp{-exp(u/eta+o(1/eta))}.                      (3.11)
```

In particular,

```text
d_eta=o(eta^A)       for every fixed A>0.             (3.12)
```

The conclusion is not that every possible right-half-plane recurrence must
pay (3.11).  It is that the proposed direct all-prime-phase implementation
does pay it.  A compressed small-ball theorem for the Euler values rather
than coordinatewise phase return is considered in Section 7.

## 4. Derivative completion and the exact comparison

Put

```text
H_tau(s)=zeta(s+i tau)-zeta(s).                       (4.1)
```

Suppose (2.3) holds with `epsilon=m/4`.  Every point of either transition
interval is within arclength `eta` of a controlled endpoint.  Hence

```text
sup_(J_+ union J_-)|H_tau|
 <=m/4+eta sup_(J_+ union J_-)|H_tau'|.               (4.2)
```

The fixed compact neighborhood of these intervals lies in
`Re(s)>1/2`.  Cauchy's estimate, a finite disc cover, and the classical
second moment to the right of `1/2` give, uniformly for small `eta`,

```text
integral_T^(2T) sup_(J_+ union J_-)|H_tau'(s)|^2 d tau
 <=C_Gamma T.                                        (4.3)
```

Consequently

```text
meas{tau: sup_J |H_tau'|>m/(2 eta)}
 <=4 C_Gamma T eta^2/m^2.                            (4.4)
```

Outside this exceptional set, (4.2) is `<m`, while (2.3) is already `<m`
on the rest of the boundary.  Rouche then replicates every zero of `zeta`
inside `Gamma` at height translated by `tau`.

Bohr--Landau zero density therefore yields the following necessary
condition under the assumed off-line zero:

```text
c_eta<=4 C_Gamma eta^2/m^2.                           (4.5)
```

Conversely, any estimate

```text
c_eta >>_(Gamma) eta^alpha,       alpha<2,            (4.6)
```

along a sequence `eta->0`, or any relative conditional derivative bound
leaving a fixed positive fraction of `U_eta`, would contradict the zero.
Equation (4.6) is the exact success criterion.

The direct Euler construction cannot meet it: (3.10)--(3.12) show that its
entire phase cylinder is already smaller than the ambient derivative
exceptional bound.  Subtracting the two measures gives no surviving shift.
This is where the proposed proof fails, not at the existence of hybrid
recurrences.

## 5. Why the near-one limit makes the comparison worse

For a contour whose left excursion has scale `delta=1-beta`, (1.6) forces

```text
eta<=C delta.                                         (5.1)
```

Taking the largest useful transition margin `eta=c delta` gives

```text
Euler phase cylinder       <=exp{-exp(C_1/delta)},
derivative exceptional set <<delta^2 T/m^2.           (5.2)
```

The first quantity loses to every fixed power of the second as
`delta->0`.  Taking a smaller margin makes the phase cutoff and density
worse.  Making most of the contour lie farther right does not change the
minimum right margin at the crossings and hence does not change (5.2).

There is also no uniform lower bound for `m` in (1.3) as the hypothetical
zero, its multiplicity, neighboring zeros, and the contour vary.  This does
not obstruct a qualitative argument about one fixed zero, but it is an
additional loss in any theorem intended to be uniform over a fixed strip.

Thus near-one geometry supplies no fixed `delta_0` exclusion through the
available estimates.  It also does not prove that zeros approach `Re(s)=1`;
the latter would itself disprove every fixed strip and remains unknown.

## 6. The `Re(s)=1` endpoint is a topological gate

It is tempting to remove the transition intervals by extending
universality to their two crossing points on `Re(s)=1` and using conditional
Euler tails there.  This is not a harmless endpoint strengthening.

Let

```text
Z(s,omega)=exp(sum_p omega(p)p^(-s)
                    +sum_p sum_(k>=2) omega(p)^k/(k p^(ks)))            (6.1)
```

be the limiting random Euler product.  Almost surely its logarithm is
analytic for `Re(s)>1/2`, so `Z` is zero-free there.  Since `zeta` has at
least one zero inside `Gamma`, Rouche gives the deterministic support
exclusion

```text
sup_(s in Gamma)|Z(s,omega)-zeta(s)|>=m               (6.2)
```

for every sample for which (6.1) is defined on the contour and its
interior.

Let `E_eta` be the closed random-model event that the error is at most a
fixed `epsilon<m` on `Gamma minus (J_+ union J_-)`, with nested gaps
shrinking to the two crossings.  Then

```text
E_eta decreases to the empty set,
P(E_eta)->0.                                          (6.3)
```

The last assertion is continuity of probability from above combined with
(6.2).  Thus density collapse as the gaps close is forced by winding, not
merely by an ineffective universality proof.  A theorem claiming joint
left universality and right conditional-tail return at Rouche accuracy all
the way to the endpoints would already exclude the zero.

This also identifies the false independence intuition.  High-prime phases
which realize the prescribed function on the left arc cannot simultaneously
be treated as an independent harmless tail on the right as the two pieces
close into a zero-winding contour.  Each marginal statement is valid; their
endpoint joint statement has zero random-Euler support.

## 7. Workarounds tested

### 7.1 Compress the right recurrence

Requiring every prime phase to return is far stronger than requiring a few
Euler values to return.  A potentially better object is the optimal mixed
small-ball probability

```text
p_eta(epsilon)=P{sup_(Gamma minus J_eta)
                    |Z(s,omega)-zeta(s)|<epsilon}.    (7.1)
```

The support argument proves only `p_eta->0`, not its rate.  A new lower
bound

```text
p_eta(m/4)>>eta^alpha,       alpha<2,                 (7.2)
```

together with a quantitative transfer from the random model to vertical
shifts would close the argument.  Coordinatewise finite-phase recurrence
cannot prove (7.2), by (3.12).  Establishing (7.2) is a genuinely sharper,
coefficient-sensitive target, but it has individual-zero/RH strength.

### 7.2 Condition the derivative relative to recurrence

The ambient Chebyshev bound is wasteful if derivatives on `U_eta` behave
typically.  It would be enough to prove

```text
meas{tau in U_eta: sup_J |H_tau'|<=m/(2eta)}
  >=kappa meas(U_eta)                                 (7.3)
```

for one fixed `kappa>0` and arbitrarily small `eta`.  Under an off-line zero,
the topology above forces (7.3) to fail eventually: almost every successful
punctured recurrence must spend the missing winding in a transition spike.
Thus (7.3) is an exact possible breakthrough statement, not an available
independence lemma.

### 7.3 Randomize or multiply the crossing corridors

Allowing the top and bottom crossing heights to be chosen after the shift
replaces a supremum derivative by a line integral through a thin rectangle.
Cauchy--Schwarz gives

```text
(integral_across |H_tau'|)^2
 <=2eta integral_across |H_tau'|^2.                  (7.4)
```

Averaging over a family of heights makes the mean area energy `O(eta)`,
while a winding-changing crossing requires energy `Omega(1/eta)`.  Markov
again gives the ratio `O(eta^2)`.  Using many disjoint corridors multiplies
both the expected energy and the required energy by the same number.  The
exponent in (4.5) is invariant; this geometric randomization does not beat
the gate.

### 7.4 Higher jets and harmonic measure

Controlling finitely many endpoint derivatives changes (4.4) to a higher
fixed power of `eta`, but (3.12) is smaller than every such power.  Letting
the jet order grow invokes factorial Cauchy constants and is a quantitative
analytic-continuation problem equivalent to controlling the missing
winding.

Harmonic-measure interpolation can move the Rouche contour away from the
gaps, but it also needs a global bound for the uncontrolled translate.
Since that bound grows with the shift height, the gap must then shrink with
`T`; fixed-compact hybrid universality supplies no such diagonal theorem.

## 8. Pole ledger

The original pole is at `1+0i`, whereas `Gamma` lies near ordinate `gamma`
and was chosen with `h<abs(gamma)/2`.  It is outside `Omega`.  The pole of
`zeta(s+i tau)` is at

```text
s=1-i tau,                                            (8.1)
```

which is also outside every fixed `Omega` for all sufficiently large
positive `tau`.  Hence Rouche compares holomorphic functions in the
relevant domain.  The line `Re(s)=1` matters only because it separates
conditional/universal control from absolute Euler convergence; the pole is
vertically irrelevant.

## 9. Verdict and next exact target

The mostly-right contour is valid, and for every fixed opening it produces
positive-density recurrence on the punctured boundary.  It does not produce
a fixed zero-free strip with known estimates.  In the natural near-one
scaling, the explicit Euler cylinder is double-exponentially smaller than
the polynomial derivative exceptional set.  Closing the gaps exactly runs
into the zero-free support/winding obstruction.

The only non-redundant successor exposed here is a **compressed mixed
small-ball/derivative theorem**, namely either (7.2) or the relative estimate
(7.3).  Both avoid the catastrophic all-coordinate cylinder.  Either one,
proved at the stated strength, would exclude the assumed zero; neither is a
known consequence of hybrid universality, Euler almost periodicity, or
unconditional moment bounds.

