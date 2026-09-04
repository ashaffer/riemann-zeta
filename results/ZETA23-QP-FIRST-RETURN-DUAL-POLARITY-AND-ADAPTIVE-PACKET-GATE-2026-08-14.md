# QP first return: full-depth dual polarity and adaptive-packet gate

**Date:** 2026-08-14

## 0. Verdict

The sparse theorem does **not** reduce the full QP problem to exceptional
arithmetic-progression steps.  A deepest positive design has at most `M`
atoms, but those atoms may be an arbitrary incommensurate `M`-tuple in the
legal interval.  The exact continuum dual is

```text
r_+(H)=inf_(y: 1^T y=-1) sup_(t in H) y^T a(t).       (0.1)
```

It covers AP and non-AP supports simultaneously.  The uniform-carrier choice
`y=-1/M` gives the useful sufficient kill

```text
r_+(H)<=-min_(t in H) S_Y(t)/M,
S_Y(t)=sum_j cos(t u_j),                               (0.2)
```

but no surveyed theorem proves the required one-sided actual-prime bound.

The exponent target in the previous shallow-slice notes was too weak even
for a full-depth disposition on the original fixed parameter slice.  At

```text
alpha_0=.49,       d=33/50=.66,       B=Y^(50/33),
```

the exact carrier ledger is

```text
kappa_min=.018030323424358778...,
kappa_max=.018746369714728765....                      (0.3)
```

Promotion is calibrated by `kappa_min`; a dual kill uniform over candidate
depth `alpha in [.49,.5)` **at fixed `d=33/50=.66`** must beat `kappa_max`.  The
earlier fixed
long-gap saving `1173/65000=.018046...` clears only the shallow endpoint.
It cannot certify a full-depth kill even on that fixed slice.

This is repairable at the exponent-ledger level on the fixed `d=33/50=.66` slice.
The rational choice

```text
beta=.152=19/125,
theta=.161=161/1000,
c=.019=19/1000                                        (0.4)
```

makes all three auxiliary deletion savings strictly larger than `.019`.
Consequently `Y^(-.019+o(1))` is a sufficient deterministic target on that
fixed slice.  Such a theorem would kill its positive QP route, including
every exceptional AP preimage and every incommensurate atomic design.  It is
not proved here.

A hostile comparison with the full parameter cache changes the global
scope.  At the cached reoptimized value `d=.665`, the top-depth bill is
`.0197404825829421...`; over `d<2/3` its supremum is
`.02007514816199...`.  Thus `.019` is **not** a full-cache or globally
architecture-wide kill exponent.  The recalibration below is a fixed-slice
ledger theorem, not a QP disposition.

There is a new exact adaptive-packet theorem.  Every finite list of bad
packet centers can be notched without changing the carrier by one projected
Gram solve.  The propagation cost away from those centers is an explicit
Schur leverage.  Guth--Maynard packet counting does not bound that leverage.
Thus sparse bad packets can be corrected **if and only if** one supplies a
new actual-node projected-span estimate; the correction algebra alone does
not close QP.

Finally, a sharp countermodel shows why generic geometry cannot provide that
estimate.  There are `M~Y/log Y` distinct, Q-independent nodes with mesh much
smaller than the best known prime-mesh bound, and an all-remote,
Q-independent frequency `M`-tuple inside the legal band, which supports a
strict fixed-depth positive antipode.  The construction is not made of prime
logs.  It proves that mesh, full spark, rational independence, remoteness,
and incommensurateness do not imply KILL; actual-prime arithmetic is
indispensable.

Therefore:

```text
fixed-d=33/50 full-depth exponent/cutoff calibration: PROVED;
full-cache .019 calibration:                          FALSE;
exact all-atom Delsarte/minimax interface:             PROVED;
finite adaptive packet correction formula:            PROVED;
off-packet Schur/leverage estimate for actual primes:  OPEN;
fixed-d=33/50 actual-prime Y^(-.019+o(1)) antenna:     OPEN;
QP promotion or architecture-wide kill:               NOT PROVED;
zero-free strip:                                      NOT PROVED.
```

---

## 1. Exact all-support polarity

Let

```text
u_1,...,u_M in (0,w],
a(t)=(cos(t u_j))_(j<=M),
q_0=(1,...,1),
H=[Y^.01,Y^(50/33)].                                  (1.1)
```

Define the maximum positive depth

```text
r_+(H)=sup{r>=0:-r q_0 in conv{a(t):t in H}}.          (1.2)
```

The interval and curve are compact, so the supremum is attained whenever it
is positive.

### Theorem 1.1 (continuum Delsarte/Elfving dual)

If a positive antipode exists, then

```text
r_+(H)=inf_(y:q_0^T y=-1) sup_(t in H)y^T a(t).        (1.3)
```

Moreover a deepest antipode has a representation on at most `M` frequencies.
On the generic full-spark locus it has exactly `M` frequencies, but they need
not be commensurate.

#### Proof

If

```text
-r q_0=integral_H a(t)dnu(t),       nu probability,
```

then every `y` with `q_0^T y=-1` satisfies

```text
r=integral_H y^T a(t)dnu(t)<=sup_H y^T a(t).          (1.4)
```

At the terminal point `-r_+q_0`, a supporting hyperplane of the compact
convex hull can be normalized by `q_0^T y=-1`; its support value is exactly
`r_+`.  This proves (1.3).  The terminal point lies in a proper supporting
face of an `M`-dimensional convex body, so facewise Caratheodory uses at most
`M` atoms.  The generic exact-`M` statement is the sparse/full-spark theorem
proved in the companion report.  QED

This theorem is the full QP interface.  An AP family tests only supports

```text
{tau,2 tau,...,M tau}
```

or their translated variants.  Excluding all of those supports does not
evaluate (1.3) on arbitrary `M`-tuples.

### Corollary 1.2 (one-sided actual-prime peak kill)

For any probability vector `lambda_j>=0`, taking `y=-lambda` in (1.3)
gives

```text
r_+(H)<=-min_(t in H) P_lambda(t),
P_lambda(t)=sum_j lambda_j cos(tu_j).                 (1.5)
```

The uniform specialization `lambda_j=1/M` is

```text
r_+(H)<=sup_H[-S_Y(t)/M]=-[min_H S_Y(t)]/M.            (1.6)
```

Thus

```text
S_Y(t)>=-M Y^(-c+o(1))       for every t in H         (1.7)
```

implies `r_+(H)<=Y^(-c+o(1))` for **every** positive
atomic measure, regardless of support arithmetic.  More generally, a
positive actual-prime Voronoi/tent rule with
`P_lambda(t)>=-Y^(-c+o(1))` gives the same all-support kill; equal weights
are not required.  This is the interface used by the retained-gap target
below.

There is also the exact localization used by the AP audit.  If a depth-`r`
antipode exists, at least

```text
r/(2-r)                                                  (1.8)
```

of its probability mass lies where

```text
S_Y(t)<=-rM/2.                                         (1.9)
```

Indeed the normalized scalar `S_Y/M` is at least `-1`; on the complement of
(1.9) it is greater than `-r/2`.  The two-point extremal inequality gives
(1.8).

Packet counting is therefore necessary information.  It is not a
separation certificate: an atomic optimizer may place its mass on the
packets which remain.

### Signed hybrid interface

For the stronger signed low/high cancellation problem, let

```text
P_y(t)=y^T a(t),
b(t)=integral phi(u)cos(tu)du.
```

If

```text
sup_L |b-P_y|<=epsilon,
sup_H |P_y|<=epsilon,                                 (1.10)
```

then the carrier-normalized signed cancellation cost is at least
`1/epsilon`.  Thus, at fixed `d=33/50=.66`, an absolute full-band antenna
with exponent `c>kappa_max` kills the signed sufficient prime-null
construction as well.
The one-sided condition (1.7) is enough only for the positive-antipode
subroute.

---

## 2. Correct min/max exponent target

With the licensed Bellotti--Wong coefficient `a=.10076`, put

```text
E_1(alpha,d)
 =alpha(d-1/2)[1-R(pi a/{alpha(2d-1)})],

R(y)=[y log(1+y^(-2))+2 atan(y)]/pi,
kappa(alpha,d)=E_1(alpha,d)/d.                        (2.1)
```

The derivative calculation in the polarity audit gives

```text
d/dalpha {alpha[1-R(C/alpha)]}
 =1-2 atan(C/alpha)/pi>0.                             (2.2)
```

Hence, at `d=.66`,

```text
kappa_min=kappa(.49,.66)
          =.018030323424358778...,

kappa_max=kappa(.5,.66)
          =.018746369714728765....                    (2.3)
```

The logical endpoints differ:

* a uniform promotion may retain only the smallest guaranteed carrier, so
  it must beat `kappa_min`;
* a dual kill must exclude a design adapted to every possible candidate
  depth, so it must beat `kappa_max`.

This is not cosmetic.  The previous long-gap deletion at
`theta=.1594` saved only

```text
1173/65000=.018046153846...<kappa_max.                (2.4)
```

Even a perfect proof for its retained consecutive-gap sum would not have
yielded a full-depth disposition on the fixed `d=33/50=.66` slice.

### Theorem 2.1 (rational `.019` fixed-`d` full-depth auxiliary calibration)

Let

```text
A=50/33,
beta=19/125=.152,
theta=161/1000=.161,
c=19/1000=.019.                                       (2.5)
```

On the certified Gafni--Tao branch, the three auxiliary savings are

```text
s_GT(theta)=(45 theta-6)/65 =249/13000,
2-A-2 beta-theta             =131/6600,
1-A/2-beta                   =373/4125.               (2.6)
```

Their exact margins over `c` are

```text
1/6500,       7/8250,       2357/33000,               (2.7)
```

respectively.  Also

```text
c-kappa_max=.0002536302852712349...>0.                (2.8)
```

Therefore, on the fixed `d=33/50=.66` slice, an estimate

```text
sup_(retained high tail)|R_Y(t)|<=Y^(-.019+o(1))      (2.9)
```

at the recalibrated cutoff would, together with the already proved low/mid
quadrature, give an effective exponent strictly between `kappa_max` and
`.019` after all `o(1)` losses.

#### Proof

Equations (2.6)--(2.8) are direct rational arithmetic.  The imported
Gafni--Tao exceptional-interval theorem supplies the first formula on this
interior branch; the rational inverse-image and short-collar estimates
supply the other two.  Lowering `beta` enlarges the retained denominator
set but improves both geometric deletion errors.  No oscillatory estimate
for that enlarged retained set is asserted.  QED

The recalibration repairs that fixed-slice polarity ledger, not the analytic
gap.  The
remaining theorem is slightly stronger than the old target because it must
cover denominators above `Y^.152`, rather than above `Y^.1537`, and save
`.019` rather than `.01803`.

### Full-cache scope audit

The aperture is `A=1/d`, so changing `d` changes both the carrier and the
auxiliary geometry.  The cached carrier formula gives

```text
fixed d=33/50:     kappa(.5,d)=.018746369714728765...;
cached d=.665:     kappa(.5,d)=.019740482582942102...;
sup_(d<2/3)        kappa(.5,d)=.020075148161991937.... (2.10)
```

The last value is the limit at `d=2/3`.  It is a supremum because the
factor `(d-1/2)/d` increases with `d`, while the argument of `R` decreases
and `R'(y)=log(1+y^(-2))/pi>0`.  Consequently `.019` misses the cached
`d=.665` bill by `.000740482582942102...` and the legal-`d` supremum by
`.001075148161991937...`.  Nothing in (2.5)--(2.9) may therefore be called a
global architecture-wide kill.

The companion transition is also part of the missing theorem.  Replaying
the cached truncated-third-moment proof at `theta=.161` gives tail saving
`249/13000` and controls the positive quadrature only through

```text
|t|<=Y^(1-theta)=Y^.839.                              (2.11)
```

Thus the unproved retained estimate on this fixed slice must cover the
complete remaining band `Y^.839<=|t|<=Y^(50/33)`, not just `|t|>=Y`.

---

## 3. Exact adaptive correction of exceptional packets

The Guth--Maynard theorem covers the large values of the initial actual
prime polynomial by few unit packets.  A natural proposal is to project
those packets away and iterate.  The following theorem identifies exactly
what this buys.

Let `t_1,...,t_R` be packet centers and set

```text
P_q=I-q_0 q_0^T/||q_0||^2,
v_i=P_q a(t_i),
V=[v_1 ... v_R],
G=V^T V.                                               (3.1)
```

### Theorem 3.1 (minimum-norm carrier-null packet correction)

Suppose `G` is invertible.  Let `y_0` be any dual, and prescribe center
values `z_i`.  Put

```text
d_i=z_i-y_0^T a(t_i),
delta=V G^(-1)d,
y_1=y_0+delta.                                        (3.2)
```

Then

```text
q_0^T delta=0,
y_1^T a(t_i)=z_i              for every i,
||delta||_2^2=d^T G^(-1)d.                            (3.3)
```

Among all carrier-null corrections attaining the center values, `delta` has
minimum Euclidean norm.  At an arbitrary query frequency `t`, put

```text
k(t)=V^T P_q a(t).
```

Then exactly

```text
delta^T a(t)=d^T G^(-1)k(t),                          (3.4)
```

and hence

```text
|delta^T a(t)|
 <=[d^T G^(-1)d]^(1/2)
   [k(t)^T G^(-1)k(t)]^(1/2).                         (3.5)
```

#### Proof

Since every column of `V` lies in `q_0^perp`, the first identity in (3.3)
is immediate.  Also

```text
V^T delta=G G^(-1)d=d,
```

which proves the interpolation identities.  Formula (3.3) follows by direct
multiplication.  The normal equations show minimum norm.  Equation (3.4) is
the definition, and (3.5) is Cauchy--Schwarz in the `G^(-1)` metric.  QED

The normalized off-packet leverage is

```text
L_T(t)=k(t)^T G^(-1)k(t)/||P_q a(t)||^2 in [0,1].     (3.6)
```

Thus packet correction needs two independent facts:

1. a lower spectral bound for `G`, controlling correction energy;
2. an off-packet bound for `L_T(t)`, preventing the correction from creating
   a new peak elsewhere.

Packet **count** controls neither.  The same formula applies to a block of
packet jets `P_q a^(m)(t_i)`, which can notch whole unit intervals to
factorial accuracy.  It still leaves the identical block-Schur leverage.

At the desired threshold `epsilon=Y^(-c)`, Guth--Maynard permits

```text
R<=Y^(2c+o(1)).                                       (3.7)
```

If the projected packet atoms were orthogonal at scale `M`, (3.3) would make
the correction energy approximately `R epsilon^2/M=M^(-1+o(1))`.
This explains why the proposal looks viable.  No actual-prime theorem gives
the required uniform Gram and off-packet leverage simultaneously.

There is an exact conservation law which prevents the algebra from proving
its own hypothesis.  If

```text
sum_k w_k a(t_k)=-r q_0,
```

then every normalized dual satisfies

```text
sum_k w_k y^T a(t_k)=r        when q_0^T y=-1.        (3.8)
```

Therefore some active atom always has `y^T a(t_k)>=r`.  An adaptive
correction can move the violating frequency, but cannot lower every
violation below `r` when an antipode exists.  Proving that the actual-prime
iteration terminates is exactly the missing arithmetic theorem, not a
consequence of sparse packet counting.

---

## 4. Atom at zero and the global Delsarte no-go

The finite-aperture qualification is essential.

### Theorem 4.1 (zero-node/global-dual equivalence)

For distinct nonnegative nodes `u_j`, the following are equivalent:

1. one node equals zero;
2. there is a finite dual `y` with

   ```text
   q_0^T y=-1,       y^T a(t)<=0 for every real t.     (4.1)
   ```

If these hold, no positive antipode of any depth exists.

#### Proof

If `u_j=0`, choose `y=-e_j`; then `y^Ta(t)=-1` for all `t`.  The same
coordinate of every convex combination of atoms is `+1`, so it cannot equal
`-r`.

Conversely, suppose every `u_j` is nonzero.  The finite almost-periodic
polynomial

```text
P(t)=sum_j y_j cos(tu_j)                              (4.2)
```

has Bohr mean zero, since it has no constant frequency.  If `P<=0` on the
real orbit, continuity gives `P<=0` on its compact Kronecker closure.  Haar
integration over that closure is zero, so `P` vanishes identically there.
In particular `P(0)=q_0^Ty=0`, contradicting (4.1).  QED

For generic QP scales no active prime-power node is exactly zero.  This
nonvanishing, not rational independence, is all Theorem 4.1 needs.  On a
shell-prime subcollection with pairwise distinct prime bases, the additional
hypothesis that no nonzero integral power of `Y` is rational does imply
Q-independence by unique factorization; one must not make that claim for a
list containing two powers of the same prime.  Exact global
nonpositive-polynomial certificates are therefore unavailable, and the
desired Delsarte dual is inherently a **finite-aperture approximate**
certificate.

This also explains why a Fejer-square shortcut does not automatically live
in the prime-log coordinate span.  Squaring a trigonometric polynomial
creates difference frequencies.  For generic `Y`, an identity among prime
log coordinates would give either a multiplicative relation among distinct
prime bases or a nonzero rational power of `Y`.  Neither is available.  A
positive polynomial on an artificial arithmetic frequency grid therefore
does not transfer to the actual coordinate set.

---

## 5. Generic geometry admits legal incommensurate promoters

The next theorem is a proof-class no-go.  It is **not** an actual-prime
construction.

### Theorem 5.1 (remote Q-independent fixed-depth countermodel)

Fix `0<r<1` and the actual rational shell width `w=1/5`.  Set

```text
tau_0=pi/w=5 pi.
```

For all sufficiently large `Y`, put

```text
M=floor(Y/log Y),
L=ceil(Y^.01/tau_0),
K={L+1,...,L+M}.                                      (5.1)
```

There exist `M` distinct nodes `u_j in (0,w)` and `M` positive frequencies
`t_k` such that:

1. the nodes are linearly independent over `Q`;
2. the frequencies are linearly independent over `Q`;
3. every frequency is legal and remote:

   ```text
   Y^.01<=min t_k<=max t_k=O(Y/log Y)<Y^(50/33);
   ```

4. the node mesh in the complete interval `[0,w]`, including its endpoints,
   is

   ```text
   O((L+2)/M)=O(Y^(-.99)(log Y));                     (5.2)
   ```

5. strictly positive weights satisfy

   ```text
   sum_k w_k a(t_k)=-r' q_0,       r'>=r/2.           (5.3)
   ```

The augmented system is nonsingular, so (5.3) persists on an open
neighborhood.

#### Proof

Use the prescribed-support theorem on `K`: choose positive weights with a
dominant top coefficient.  The polynomial

```text
r+sum_(k in K)w_k cos(k theta)                        (5.4)
```

has exactly one simple root in each of the `D=L+M` top-frequency cells, and
its `D by M` root table has rank `M`.  Select a nonsingular `M`-row minor.
Only `L` root cells are omitted.  Between two retained roots there are at
most `L` omitted roots; because every root lies in its own interval of
length `pi/D`, the largest interior phase gap is less than
`(L+2)pi/D`, while either endpoint gap is at most `(L+1)pi/D`.
Scale the selected phases by `u_j=theta_j/tau_0`.  Since
`pi/tau_0=w`, this covers the complete node interval and proves (5.2).

Strict positivity and the augmented determinant are open conditions.  In an
arbitrarily small node neighborhood choose

```text
u_j=c_j+delta sqrt(p_j),                              (5.5)
```

where the `c_j` and nonzero `delta` are rational and the `p_j` are distinct
primes.  The numbers `1,sqrt(p_1),...,sqrt(p_M)` are Q-linearly independent,
so the nodes are Q-independent.  The mesh and positivity survive.

Choose the node perturbations to be `o(1/M)`, so (5.2) is preserved.  Start
with physical frequencies `tau_0 k`.  Perturb them inside the same
strict chamber to

```text
t_k=tau_0 k+eta sqrt(q_k),                            (5.6)
```

with rational nonzero `eta` (chosen inside the open positivity radius) and
distinct new primes `q_k`.  In a rational relation among these frequencies,
the coefficient of `pi` and the remaining algebraic sum must vanish
separately because `pi` is transcendental.  Multiquadratic independence then
forces every rational coefficient to vanish.  Continuity preserves positive
weights, nonsingularity, and depth at least `r/2`.  Equations (5.1) give the
legal frequency bounds.  QED

The mesh in (5.2) is far smaller than the published maximal prime-log mesh
`O(Y^(-19/40))`.  Hence all of the following properties are compatible with
a fixed-depth legal promoter:

```text
correct dimension M~Y/logY;
excellent deterministic mesh;
Q-independent nodes;
Q-independent/incommensurate atoms;
strict positive weights;
all atoms remote;
open augmented-invertible chamber.
```

What the countermodel lacks is precisely the statement `u_j=|log(n_j/Y)|`
for actual prime powers.  Any successful KILL theorem must use that missing
arithmetic, not just the listed geometric properties.

---

## 6. Primary-literature boundary

* [Elfving, *Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442)
  gives the directional convex-hull/optimal-design dual underlying (1.3).
  It does not estimate the actual-prime support function.
* [Guth--Maynard, *New Large Value Estimates for Dirichlet Polynomials*](https://arxiv.org/abs/2405.20552)
  gives the packet count (3.7).  It is a count of large values, not an
  off-packet projected-Gram or Schur-leverage theorem.
* [Klurman--Mangerel--Teravainen, *Multiplicative Functions in Short
  Arithmetic Progressions*](https://doi.org/10.1112/plms.12546), Lemma 7.9
  and Remark 7.2, gives only a logarithmic pointwise saving for the natural
  principal prime twist throughout the polynomial height range.  Its exact
  range is `|t|<=x^((log x)^(1/25))`; the outer exponent is easy to lose in
  PDF text extraction.
* [Gafni--Tao, *On the Number of Exceptional Intervals to the Prime Number
  Theorem in Short Intervals*](https://arxiv.org/abs/2505.24017) supplies the
  exceptional-gap envelope used in (2.6).  It does not control the retained
  signed consecutive-gap Fourier mode.
* [Weber, *Local Suprema of Dirichlet Polynomials and Zerofree Regions of the
  Riemann Zeta-Function*](https://arxiv.org/abs/1005.3932) reproduces
  Turan's localization criterion.  A natural complex prime-interval power
  bound with its interval and local-height uniformity is already fixed-strip
  strength.  The present arbitrary-weight finite-aperture dual has fewer
  quantifiers, so no converse is claimed for it.
* [Gonek--Montgomery, *Kronecker's Approximation Theorem*](https://doi.org/10.1016/j.indag.2016.02.002)
  and [Maksimova, *A Note on Kronecker's Approximation Theorem*](https://doi.org/10.1016/j.indag.2024.08.002)
  give upper hitting-time theorems.  They do not prove avoidance of a
  specified growing-dimensional chamber before a polynomial aperture.

No primary result found in this audit proves either of the following
fixed-`d=33/50=.66` targets:

```text
inf_(t in H) S_Y(t)>=-M Y^(-.019+o(1))               (6.1)
```

or the stronger adaptive-weight full antenna, nor does one bound the Schur
leverage in Theorem 3.1 for every actual exceptional packet set.

---

## 7. Exact disposition

```text
AP generic/dilation-shadow obstruction:                 PROVED ELSEWHERE;
deterministically selected AP exceptional preimages:     OPEN;
arbitrary incommensurate positive atomic designs:        NOT COVERED BY AP;
full positive-depth minimax dual:                        PROVED;
q0 one-sided all-support kill criterion:                 PROVED;
fixed-d=33/50 promotion exponent kappa_min:               .018030323424...;
fixed-d=33/50 uniform-kill exponent kappa_max:            .018746369715...;
cached-d=.665 uniform-kill exponent:                     .019740482583...;
all-d<2/3 supremal uniform-kill exponent:                .020075148162...;
fixed-d=33/50 auxiliary target c=.019:                   PROVED FEASIBLE;
full-cache c=.019 target:                                INSUFFICIENT;
finite carrier-null bad-packet correction:               PROVED;
actual-prime off-packet leverage/Schur bound:             OPEN;
full deterministic tent/adaptive antenna:                OPEN;
positive QP promotion:                                   NOT PROVED;
fixed-d or architecture-wide QP kill:                    NOT PROVED;
uniform zero-free strip:                                 NOT PROVED.
```

The highest-value next theorem is now exact:

> For the actual prime-power nodes on the fixed `d=33/50=.66` slice and every
> Guth--Maynard bad-packet set at threshold `Y^(-.019+o(1))`, prove a
> projected-Gram lower bound and an
> off-packet leverage estimate strong enough to iterate Theorem 3.1; or prove
> the recalibrated retained Voronoi sum (2.9) directly.

Either statement must use actual multiplicative arithmetic.  Average packet
counts, generic full spark, mesh bounds, and rational independence cannot
substitute for it.

## 8. Replay

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_first_return_dual.py
PYTHONPATH=src python3 src/qp_first_return_dual.py
python3 results/verify_zeta23_qp_first_return_dual.py
```
