# QP actual-prime positive weights: half-period barrier and exact repair gates

**Date:** 2026-08-14
**Verdict:** the actual-prime one-sided Delsarte estimate is **not proved**.
The constructive survey does, however, eliminate three proposed shortcuts
exactly and strengthens the arithmetic diagnosis.

The strongest new no-go is polarity-correct.  There are prime-density log-node
sets with gaps `O(log Y)`, gap-square sum `O(Y log Y)`, the same low-denominator
deletion budget, and rational independence after an invisible perturbation, for
which at the legal top height

```text
cos(B u_j)=-1+o(1)                 for every node j.       (0.1)
```

Consequently **every** normalized positive weighting has value `-1+o(1)`
there.  Adaptive Voronoi weights, multiplicative weights, random subsets, and
positive packet repair all fail on this common countermodel.  This is stronger
than the previous `+1` log-lattice countermodel for the present one-sided
question.

This does not model the actual primes.  It proves that the missing theorem must
use actual multiplicative arithmetic beyond node count, maximal gaps, gap
moments, local upper density, low-denominator excision, and qualitative
nonlattice information.

Two further exact gates survived hostile checking:

1. positive quadrature exact through trigonometric degree `n` needs at least
   `n+1` nodes, whereas the prime shell has `M=Y^(1+o(1))` and the required
   degree is `asymp B=Y^(50/33)`;
2. projected-Gram invertibility licenses a signed affine packet correction,
   not a positive one.  Positive packet correction is exactly membership in a
   convex hull of actual coordinate phase vectors.  A Gram matrix can be
   strictly positive while the requested corrected value lies outside that
   hull.

Thus exact quadrature, finite packet algebra by itself, and support thinning do
not solve the actual-prime QP.  The remaining statement is still an actual-node
convex-hull/Delsarte theorem.

---

## 1. Target and polarity

Let the distinct nonzero actual prime-power log nodes be `u_j in (0,w]`, and
put

```text
P_lambda(t)=sum_j lambda_j cos(t u_j),
lambda_j>=0,                 sum_j lambda_j=1,
H=[Y^.01,Y^(50/33)].                                  (1.1)
```

At fixed `d=33/50`, a sufficient positive-QP kill is

```text
P_lambda(t)>=-Y^(-c+o(1))       for every t in H       (1.2)
```

with `c>kappa_promote`; `c=.019` is the already audited convenient target on
that fixed slice.  A positive peak is harmless.  A valid proof-class
countermodel therefore needs a coherent **negative** peak.  Section 2 supplies
one.

The coefficients in the exact Delsarte dual may be signed.  Restricting to
`lambda_j>=0` is a stronger constructive ansatz.  The no-go below defeats every
positive choice, but it does not defeat arbitrary unbounded signed coefficients
after perturbation and does not determine the actual-prime Delsarte value.

---

## 2. Universal positive-weight half-period countermodel

Write

```text
A=50/33,       B=Y^A,
beta=19/125=.152,       Q=Y^beta.                     (2.1)
```

### Theorem 2.1 (negative half-grid defeats every positive reweighting)

For every sufficiently large `Y`, there is a real node set in the fixed
multiplicative shell with the following properties:

```text
M asyp Y/log Y,
maximum physical gap       <<log Y,
sum of squared gaps        <<Y log Y,
#(nodes in J)              <<1+|J|/log Y              (2.2)
```

for every physical interval `J`.  After deleting all cells meeting the cached
low-denominator curvature arcs with `q<=Q`, a `1-o(1)` fraction of its Voronoi
mass remains.  Nevertheless, at `t=B`, every retained normalized positive
weight vector satisfies

```text
sum_j lambda_j cos(Bu_j)=-1.                          (2.3)
```

The same construction can be perturbed so that
`{2pi,u'_1,...,u'_M}` is linearly independent over `Q` and, for every fixed
`K`,

```text
sum_j lambda_j cos(Bu'_j)
 <=-cos(Y^(-K))=-1+O(Y^(-2K))                        (2.4)
```

simultaneously for **every** positive probability vector `lambda`.

#### Proof

Take one congruence class of the odd half-period grid

```text
u_j=(2k_j+1)pi/B,          k_(j+1)-k_j=L,
L=ceil[B log(Y)/(2pi Y)].                              (2.5)
```

Use all indices placing `u_j` in the signed shell and put `x_j=Y exp(u_j)`.
The log spacing is

```text
Delta u=2pi L/B=asymp log(Y)/Y.                       (2.6)
```

Since `x asyp Y`, (2.6) gives physical gaps `asymp log Y`, cardinality
`asymp Y/log Y`, the gap-square estimate, and the local counting upper bound
in (2.2).

The low-denominator arc geometry used in the preceding Voronoi audit deletes
mass at most

```text
Q sqrt(B)/Y +(B/Y)Q^2 log(Y)/Y.                       (2.7)
```

The two exact powers in (2.7) are

```text
beta+A/2-1 = -373/4125=-.09042424...,
A-2+2beta  = -746/4125=-.18084848....                 (2.8)
```

Both are negative (and both beat `.019`), so retained mass is `1-o(1)`.
There is no large-gap deletion because every gap is `O(log Y)`.

Equation (2.5) gives identically

```text
B u_j=(2k_j+1)pi,           cos(Bu_j)=-1.             (2.9)
```

Deleting nodes or changing their positive weights cannot change (2.9), which
proves (2.3).

Finally, the configurations for which `{2pi,u'_1,...,u'_M}` has a rational
linear dependence form a countable union of proper affine hyperplanes.
Perturb each node outside that union by at most `B^(-1)Y^(-K)`.  All mesh
statements persist, while the phase perturbation at `B` is at most
`Y^(-K)`.  Since
`cos((2m+1)pi+delta)=-cos(delta)`, (2.4) follows.  QED

### Scope

The theorem simultaneously defeats any proposed rule whose proof sees only

```text
positive/adaptive weights;
Voronoi or gap-local weights;
multiplicative formulas for those weights;
random thinning or subset sampling;
maximal-gap and finitely many gap-moment estimates;
prime-density local upper bounds;
low-q deletion;
qualitative rational independence.                   (2.10)
```

It is not a prime counterexample.  The half-grid physical nodes are real, not
integers or primes.  A theorem using unique factorization quantitatively,
consecutive-prime transition arithmetic, or an actual-prime inverse theorem is
not touched.

---

## 3. Random subset sampling cannot repair an unknown bad base antenna

### Proposition 3.1 (inheritance of a fixed negative peak)

Let `U_1,...,U_K` be sampled independently from any positive node rule
`lambda`.  If at a fixed height `t_0`

```text
P_lambda(t_0)<=-2 epsilon,
```

then

```text
Pr{K^(-1)sum_l cos(t_0 U_l)>=-epsilon}
 <=exp(-K epsilon^2/2).                               (3.1)
```

This is Hoeffding's inequality for variables in `[-1,1]`.  Thus subset
sampling concentrates around the base actual-prime antenna; it cannot prove
that the unknown base antenna has no negative peak.  On Theorem 2.1's
half-grid every subset has value exactly `-1`, so no probability estimate is
needed.

This does not say that a carefully selected deterministic actual-prime subset
cannot work.  It says random thinning alone does not manufacture the missing
arithmetic sign.

---

## 4. Square reweighting: exact difference-kernel and normalization ledger

The most promising adaptive proposal is to start from a diffuse positive rule
`mu_0` and multiply its weights by

```text
h(u)=|C(u)|^2,       C(u)=sum_(s in S)c_s exp(i s u).  (4.1)
```

This preserves positivity.  It does not, by itself, average away a bad packet.
The exact formula identifies the additional theorem it needs.

Write

```text
Phi(t)=integral exp(i t u)dmu_0(u),
E=sum_s |c_s|^2,
Z=integral h dmu_0.                                  (4.2)
```

### Theorem 4.1 (difference-kernel covariance identity)

The reweighted characteristic function is exactly

```text
Phi_h(t)
 =Z^(-1) sum_(s,r)c_s conjugate(c_r) Phi(t+s-r).      (4.3)
```

Separate the diagonal and off-diagonal pieces:

```text
Z=E+N,
N=sum_(s!=r)c_s conjugate(c_r)Phi(s-r),
R_t=sum_(s!=r)c_s conjugate(c_r)Phi(t+s-r).           (4.4)
```

Then

```text
Phi_h(t)-Phi(t)=[R_t-Phi(t)N]/Z,                     (4.5)

R_t-Phi(t)N
 =sum_(s!=r)c_s conjugate(c_r)
   [Phi(t+s-r)-Phi(t)Phi(s-r)].                       (4.6)
```

Thus only an off-diagonal **actual-node covariance** changes the old antenna.
The diagonal contribution is `E Phi(t)`, and the same diagonal energy `E`
normalizes the filter.  If the packet shifts are approximately orthogonal, so
that `|N|<=eta E`, then a change of at least `epsilon` at a bad packet requires

```text
|R_t-Phi(t)N|>=epsilon Z>=epsilon(1-eta)E.            (4.7)
```

Packet sparsity bounds the number of large values of `Phi`.  It does not bound
the covariance values in (4.6), their signs, or the `O(|S|^2)` difference
locations.  In particular, the hoped-for factor `1/|S|` is canceled by
normalization when off-diagonal normalization is small.

#### Proof

Expand

```text
|C(u)|^2=sum_(s,r)c_s conjugate(c_r)exp(i(s-r)u)
```

and integrate, first with and then without `exp(itu)`.  Subtracting
`Phi(t)Z` cancels every diagonal term and gives (4.5)--(4.6).  QED

### Normalization and diffuseness

Let

```text
K_eff=||c||_1^2/||c||_2^2<=|S|.                      (4.8)
```

If `|N|<=eta E`, then

```text
Z>=(1-eta)E,
max_j(lambda'_j/lambda_j)
 <=||c||_1^2/Z<=K_eff/(1-eta).                       (4.9)
```

For the natural packet ansatz

```text
C(u)=1+sum_(i<=R)a_i exp(i t_i u),
R<=epsilon^(-2+o(1)),       |a_i|=O(epsilon),         (4.10)
```

the diagonal energy is only

```text
E=1+sum_i|a_i|^2=O(Y^o(1)).                          (4.11)
```

So there is no automatic normalization catastrophe.  But (4.9) permits a
worst-case diffuseness loss of order

```text
R=epsilon^(-2+o(1))=Y^(.038+o(1))                   (4.12)
```

at the fixed-slice `epsilon=Y^(-.019)`, and even `Z asyp E` itself is an
actual-prime packet-Gram statement.  More importantly, (4.7) still requires a
signed covariance of the correct size at every repaired packet and controlled
covariance away from them.

### Proposition 4.2 (one-packet variance gate)

There is an exact one-packet version which makes the missing information
especially clear.  Put

```text
X(u)=cos(t_0u),       m=E_(mu_0)X,
h_delta(u)=1+delta X(u),       0<=delta<=1.            (4.13)
```

The multiplier is nonnegative and has a two-term Fejer--Riesz square.  Its
normalization and corrected packet value are

```text
Z_delta=1+delta m,
m_delta=[m+delta E(X^2)]/[1+delta m],
m_delta-m=delta Var(X)/[1+delta m].                   (4.14)
```

If `m=-a` and the target is `m_delta>=-epsilon`, this family succeeds for
some `delta<=1` if and only if

```text
Var(X)>=(a-epsilon)(1-a),                             (4.15)
```

apart from the trivial endpoint `a=1`, where zero variance makes repair
impossible.  A sparse large-value theorem gives no lower bound for this
within-packet variance.  Equivalently,

```text
Var(X)=[1+Re Phi(2t_0)]/2-[Re Phi(t_0)]^2,            (4.16)
```

so even the first nonlinear repair already asks for a correlated actual-prime
estimate at a doubled height.

### Corollary 4.3 (one natural-prime packet is locally repairable)

For the normalized smooth fixed-shell von Mangoldt rule, the
Klurman--Mangerel--Teravainen estimate quoted in Section 7 and partial
summation give, uniformly for `t in H`,

```text
Phi(t),Phi(2t)=O((log Y)^(-3/10))+o(1).               (4.17)
```

The source height range `Y^((log Y)^(1/25))` contains `2B`.  Hence, at any
one packet,

```text
m=o(1),             E(X^2)=1/2+o(1),
Var(X)=1/2+o(1).                                    (4.18)
```

If `m<0`, take

```text
delta=-m/E(X^2)=O((log Y)^(-3/10)).                  (4.19)
```

Then `0<delta<1`, the positive multiplier `1+delta X` makes the corrected
packet moment exactly zero, and

```text
Z_delta=1-O((log Y)^(-3/5)).                         (4.20)
```

Thus the one-packet variance obstruction is not the actual-prime blocker for
this natural base rule.  The unresolved step is simultaneous correction:
cross-packet differences, clustered/confluent conditioning, positivity over
the whole band, and off-packet propagation.  KMT controls a fixed natural
coefficient sequence; it does not control the adaptive covariance (4.6).

Theorem 2.1 is the sharp obstruction: there `X=-1+o(1)` on every coordinate,
so every positive multiplier `h`, square or otherwise, leaves the bad packet
at `-1+o(1)`.  Therefore sparse packets can be diluted by square reweighting
only after proving actual-prime covariance/inradius and off-packet leverage;
packet count alone is insufficient.

---

## 5. Positive packet correction is a convex-hull theorem

Fix packet centers `t_1,...,t_R` and define the coordinate feature vectors

```text
b_j=(cos(t_1u_j),...,cos(t_Ru_j)) in [-1,1]^R.        (5.1)
```

### Theorem 5.1 (simplex/packet equivalence)

The packet vectors attainable by positive normalized node weights are exactly

```text
{sum_j lambda_j b_j:lambda_j>=0, sum_j lambda_j=1}
   =conv{b_1,...,b_M}.                                (5.2)
```

Therefore a proposed positive correction from moment vector `m` to `m+d` is
feasible if and only if

```text
m+d in conv{b_j}.                                    (5.3)
```

Projected-Gram invertibility says only that the corresponding affine span has
the expected dimension.  It does not imply (5.3), nor provide a quantitative
inradius.

#### Sharp two-coordinate example

At one packet take coordinate values

```text
b_1=-1,        b_2=-1/2.                              (5.4)
```

After projecting away the constant vector, the Gram value is

```text
sum_j(b_j-mean(b))^2=1/8>0.                           (5.5)
```

Thus the signed affine correction system has full rank.  But the positive
range is exactly `[-1,-1/2]`; correcting the packet to zero is impossible.

The finite projected-Gram formula in the companion audit remains correct for
signed dual coefficients.  To turn it into a positive weight construction one
must additionally prove an actual-prime convex-hull inradius and control its
off-packet propagation.  Packet count and Gram rank supply neither.

---

## 6. Exact positive quadrature cannot span the aperture

### Theorem 6.1 (Toeplitz rank barrier)

Let

```text
mu=sum_(j=1)^M lambda_j delta_(x_j),
lambda_j>0,       sum_j lambda_j=1,                   (6.1)
```

be exact for normalized circle integration for every mode `|k|<=n`.  Then

```text
M>=n+1.                                               (6.2)
```

#### Proof

The moment matrix indexed by `0<=a,b<=n` is

```text
T_(a,b)=hat mu(a-b)=delta_(a,b),                      (6.3)
```

so `rank(T)=n+1`.  On the other hand

```text
T=V diag(lambda) V*,                                 (6.4)
```

where `V_(a,j)=exp(2pi i a x_j)`, and hence `rank(T)<=M`.  QED

After linearly rescaling the fixed log shell to a circle, exactness through all
Fourier heights `t<=B` would require `n=asymp B`.  The actual prime-power shell
has

```text
M=Y^(1+o(1)),              B=Y^(50/33),               (6.5)
```

so exact positive quadrature is dimensionally impossible by a factor
`Y^(17/33-o(1))`.

The new paper
[Kunis, *Positive quadrature and mobile sampling of multivariate
trigonometric polynomials*](https://arxiv.org/abs/2608.11915), Theorem 3.3 and
Remark 3.4, independently supplies the complementary covering-radius
necessity for positive exact quadratures.  In one dimension, exactness through
degree `2n-1` forces covering radius at most `1/(4n)`.  Prime-gap theorems only
give log-mesh control through a far smaller frequency scale than `B`.

This is a no-go only for **exact full trigonometric quadrature**.  The desired
one-sided inequality (1.2) is much weaker, and neither the rank proof nor
Kunis's theorem rules it out.

Tchakaloff's theorem does not alter this conclusion: it chooses quadrature
nodes (or compresses a discrete rule which is already valid).  It does not
move its nodes onto the prescribed prime-log set.  Likewise the standard
positive scattered-quadrature/Marcinkiewicz--Zygmund mechanism assumes
`mesh*bandwidth=O(1)`; with the unconditional prime mesh it reaches only the
already-audited low/mid scale near `Y^(19/40)`, not `B`.

---

## 7. Other constructive routes

### Tent/Voronoi weights

They remain the best natural actual-node candidate.  The continuum tent has a
nonnegative sinc-squared transform, and low/mid transfer is already proved.
The high band still requires sign-sensitive consecutive-gap cancellation.
Theorem 2.1 proves that mesh and gap moments cannot supply it by themselves.

### Multiplicative weights

Weights such as smooth powers of the node location only replace one positive
base distribution by another.  They cannot overcome Theorem 2.1 because all
coordinate phases there are the same at `B`.  On actual primes they remain a
possible ansatz, but their transform is again an actual prime Dirichlet
polynomial and no fixed-power all-height theorem was found.

### Spectral-null convolutions

The exact Bernoulli construction and grouping theorem in the companion report
already show that nodewise or polylogarithmically grouped positive convolution
factors have exponentially small retained central atom.  Reaching polynomial
depth forces a macroscopic group, which is the original growing-dimensional
actual-prime problem.

### Positive quadrature

Full exactness is excluded by Theorem 6.1.  Approximate one-sided quadrature is
not excluded, but proving it at `B` cannot be reduced to a mesh estimate; the
negative half-grid has excellent mesh and fails maximally.

### Existing prime-twist estimate

Klurman--Mangerel--Teravainen,
[Lemma 7.9 and Remark 7.2](https://doi.org/10.1112/plms.12546), gives only a
logarithmic saving, with the `log^(-3/10)` bottleneck in this application.  Its
upper height is `Y^((log Y)^(1/25))`, so it **does** cover the polynomial top
aperture `Y^(50/33)`.  The valid mismatch is the saving and the fixed,
nonadaptive coefficient sequence: it does not supply the fixed-power
actual-weight covariance or antenna required here.  It does suffice for the
single-packet variance calculation in Corollary 4.3.

---

## 8. Disposition

```text
actual-prime positive antenna at fixed power:          OPEN;
actual-prime Delsarte value A_H:                       OPEN;
geometry/gap-only positive-weight proof:               KILLED;
random thinning without a good base antenna:           KILLED;
Gram-only positive packet repair:                      KILLED;
exact positive quadrature through the full aperture:   KILLED;
square reweighting from packet count alone:            KILLED;
single natural-base packet repair:                     PROVED;
actual-prime convex-hull inradius / transition theorem: OPEN;
QP-KILL or QP-PROMOTE:                                 NOT PROVED;
zero-free strip:                                       NOT PROVED.       (8.1)
```

The clean remaining target is now:

> Prove, for the actual prime-power log nodes, either a positive probability
> vector satisfying (1.2) on the entire band, or a signed Delsarte polynomial
> with the corresponding value; equivalently, prove an actual-prime
> convex-hull separation/inradius theorem which excludes the half-period
> coherence permitted by every known geometric package.

Executable artifacts:

- `src/qp_actual_prime_weight_barrier.py`;
- `src/test_qp_actual_prime_weight_barrier.py`;
- `results/verify_zeta23_qp_actual_prime_weight_barrier.py`.
