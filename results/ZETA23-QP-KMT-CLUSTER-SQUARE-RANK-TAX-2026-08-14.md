# KMT cluster repair: local positivity and the macroscopic-square rank tax

**Date:** 2026-08-14
**Verdict:** Corollary 4.3 does **not** extend to all Guth--Maynard packets by
cluster merging plus scalar KMT.  The attempted deduction has an exact
block-size dichotomy.  This is a no-go for that black-box proof package, not
a no-go for the unknown actual-prime covariance theorem.

Let

```text
epsilon=Y^(-.019),             eta=(log Y)^(-3/10+o(1)),
R<=epsilon^(-2+o(1))=Y^(.038+o(1)).                 (0.1)
```

For the natural smooth von Mangoldt shell, KMT controls every fixed high
twist by `eta`.  For one packet this makes the cosine variance
`1/2+o(1)`, so the positive tilt in Corollary 4.3 works.  For `R` packets,
however, a positive square contains an adaptive quadratic tail.  The exact
conclusions are:

1. `cos(delta u)>=1/2` on the shell only for a fixed-size neighborhood of a
   packet.  Merging therefore saves a constant factor, not a power of `Y`.
2. A stably normalized mixture of squares which supplies normalized linear
   lift `asymp epsilon` at `R` surviving packet representatives must contain
   a square involving `asymp R` of them.
3. On such a square, termwise scalar KMT pays the adaptive covariance tax
   `eta R`, whereas the required remainder is `O(epsilon)`.

Thus the two apparent escapes are mutually exclusive: small square blocks
pay a PSD normalization/rank tax, while macroscopic blocks require a new
coefficient-sensitive actual-prime cross-Gram estimate.  The logarithmic KMT
floor cannot provide it.

---

## 1. Exact local covariance and what cluster merging buys

Let `mu_Y` be the normalized positive smooth von Mangoldt measure on the
fixed log shell `|u|<=w`, with `w=1/5`, and write

```text
Phi(v)=integral exp(ivu)dmu_Y(u),
X_t(u)=cos(tu).                                      (1.1)
```

The exact real covariance is

```text
Cov(X_s,X_t)
 =1/2 Re[Phi(t-s)+Phi(t+s)]
   -Re Phi(s) Re Phi(t).                             (1.2)
```

For `|t-s|<=r_0`, where

```text
r_0=arccos(1/2)/w=5pi/3,                            (1.3)
```

the shell support gives `cos((t-s)u)>=1/2` pointwise.  KMT controls the
high sum `t+s` and the two means by `eta`, so (uniformly once the packet
heights are high)

```text
Cov(X_s,X_t)>=1/4-o(1)>=1/5                         (1.4)
```

for all sufficiently large `Y`.  Since KMT also gives
`|E X_t|<=eta`, the positive multiplier `1+6eta X_s` lifts every negative
moment in this fixed-radius neighborhood above zero (with room after slightly
enlarging the constant), while its normalization is `1+O(eta^2)`.  Thus one
local tilt really can repair a fixed-radius cluster.

The Guth--Maynard packet centers are taken one-separated.  An interval of
diameter `2r_0` therefore contains at most

```text
floor(2r_0)+1=11                                    (1.5)
```

centers.  Partitioning a long consecutive bad run into such windows leaves
at least `R/11` representatives.  Transitive merging does not change this:
a chain of `R` unit-spaced packets can have diameter `R-1`, and (1.4) only
controls a fixed local neighborhood.  Consequently low-difference
positivity does not lower the critical exponent `R=Y^(.038+o(1))`.

This is the favorable part of the proposal.  The obstruction occurs when
one asks for one positive multiplier to retain all these lifts.

---

## 2. Every positive square mixture is a PSD block matrix

Consider the general mixture used to avoid cross-cluster interactions:

```text
h(u)=sum_alpha |x_alpha
             +sum_(i in S_alpha)y_(alpha,i)e^(-it_i u)|^2,
|S_alpha|<=L.                                       (2.1)
```

Nonnegative mixture weights have been absorbed into `x_alpha,y_alpha`.
Put

```text
s=sum_alpha |x_alpha|^2,
d=sum_(alpha,i)|y_(alpha,i)|^2,
D=s+d,
b_i=sum_alpha conjugate(x_alpha)y_(alpha,i).         (2.2)
```

Here `b_i` is the baseline--packet Fourier coefficient which reproduces the
one-packet linear tilt.  The complete coefficient matrix is PSD because it
is a sum of rank-one Gram matrices.

### Theorem 2.1 (block-Cauchy rank tax)

For (2.1),

```text
sum_i |b_i| <=sqrt(Lsd)<=sqrt(L)D/2.                (2.3)
```

#### Proof

For each row, Cauchy gives

```text
sum_(i in S_alpha)|x_alpha y_(alpha,i)|
 <=sqrt(L)|x_alpha| ||y_alpha||_2.
```

Sum in `alpha` and apply Cauchy once more.  The arithmetic--geometric mean
inequality gives the second bound.  QED

Let

```text
Z=integral h dmu_Y.                                  (2.4)
```

Suppose the normalization is stable in the weak direction

```text
D<=K Z                                               (2.5)
```

for a fixed or subpolynomial `K`.  Suppose also that a fixed fraction `q>0`
of each required `epsilon` lift is supplied by the baseline--packet channel:

```text
|b_i|>=q epsilon Z          (i=1,...,R).             (2.6)
```

Equations (2.3)--(2.6) imply the exact support lower bound

```text
L >= [2qR epsilon/K]^2.                              (2.7)
```

At the critical packet count `R=epsilon^(-2)`, (2.7) is

```text
L >=(4q^2/K^2)R.                                    (2.8)
```

Thus singleton squares, fixed-size cluster squares, and every
`L=R^(1-o(1))` block decomposition fail under stable normalization.  To
retain all critical lifts, at least one square must be macroscopic.

The hypothesis (2.6) is intentionally explicit.  The theorem classifies the
proposed extension of the one-packet tilt, in which the linear covariance
does the lifting and the quadratic tail is controlled as an error.  A proof
whose nonlinear tail itself supplies the lifts is not excluded; that would
already be a new signed adaptive covariance theorem.

---

## 3. The exact KMT tax on a macroscopic square

Take one tail

```text
D_a(u)=sum_(i in S)a_i e^(-it_i u),       |S|<=L.   (3.1)
```

At target `t_k`, its contribution to the reweighting covariance is

```text
C_k(a)=sum_(i,j in S)a_i conjugate(a_j)
 [Phi(t_k-t_i+t_j)-Phi(t_k)Phi(-t_i+t_j)].           (3.2)
```

The `i=j` terms cancel exactly.  Put the packet centers in one multiplicative
bin

```text
T<=t_i,t_k<=(1+rho)T,             0<rho<1.           (3.3)
```

Then every translated frequency in the first `Phi` in (3.2) lies between
`(1-rho)T` and `(1+2rho)T`.  The top is below `3B`, which is still within
KMT's superpolynomial height aperture; subdividing the last bin removes the
irrelevant endpoint constant.  Once `(1-rho)T` is in the high range, scalar
KMT and `|Phi|<=1` give, for `i!=j`,

```text
|Phi(t_k-t_i+t_j)-Phi(t_k)Phi(-t_i+t_j)|<=2eta.     (3.4)
```

Therefore its termwise black-box estimate is exactly

```text
|C_k(a)|
 <=2eta sum_(i!=j)|a_i a_j|
 <=2eta(L-1)||a||_2^2.                              (3.5)
```

For the whole mixture, the same formula sums over rows.  Moreover the first
Cauchy inequality in Theorem 2.1 also gives

```text
d/Z >=(qR epsilon)^2/(LK).                           (3.6)
```

Hence any attempt to make the *termwise KMT certificate* for the nonlinear
remainder at most `epsilon` must reconcile (2.7), (3.5), and (3.6).  At
`R=epsilon^(-2)` and fixed `q,K`, (2.7) forces `L asymp R`, (3.6) forces
`d/Z gg 1`, and the numerical right side supplied by (3.5) is at least on
the scale

```text
eta R =Y^(.038+o(1))/(log Y)^(3/10),                 (3.7)
```

not `epsilon=Y^(-.019)`.

This last statement is about the size of the available absolute-value
certificate, not a lower bound on the actual `C_k(a)`.  Actual cancellations
could make (3.2) small.  Proving those cancellations uniformly for the
coefficients selected from the bad packets is precisely the missing
coefficient-sensitive cross-Gram theorem.

### Why more bins do not help

Dividing the band into `O(log Y)` multiplicative bins ensures the translated
frequencies in (3.2) stay high.  A positive mixture removes quadratic cross
terms between bins, but Theorem 2.1 then charges the number and sizes of its
blocks.  Since fixed-radius merging leaves `Y^(.038+o(1))` representatives,
one bin can still contain the critical number; the hypotheses provide no
distribution theorem forcing otherwise.  If the representatives are spread
among many bins, summing their block-Cauchy inequalities gives the same PSD
budget up to `Y^o(1)`.

---

## 4. KMT-informed sharpness model for the missing quantifier

The scalar-to-adaptive gap is not merely Gershgorin bookkeeping.  Let `s` be
even, `R=s^2`, and take the uniform probability on sign vectors

```text
x in {-1,1}^R,              sum_i x_i=-2s.           (4.1)
```

Then, for `i!=j`,

```text
E x_i=-2/s=-2epsilon,
E x_i^2=1,
E x_i x_j=3/(R-1)=O(epsilon^2),
epsilon=R^(-1/2).                                   (4.2)
```

Every coordinate has variance `1-4/R=1-o(1)`, so every individual packet is
locally repairable.  All pair moments are `O(epsilon^2)`, much smaller than
the KMT floor `eta`.  Nevertheless (4.1) holds pointwise, so under **every**
positive reweighting

```text
sum_i E_h x_i=-2s.                                  (4.3)
```

At least one coordinate therefore remains at most `-2epsilon`; simultaneous
lifting of all coordinates to `-epsilon` is impossible.  Equivalently, the
centered covariance annihilates the distinguished all-ones source direction.

This is an abstract bounded-entry moment model, not a scalar prime-log curve.
Its exact scope is nevertheless stronger than a generic half-grid example:
even excellent one-packet variance and pairwise scalar correlations far below
KMT do not imply the adaptive source statement.  The missing theorem must use
the actual joint prime-log curve, not just the KMT values of its first two
scalar moments.

---

## 5. Binary disposition

```text
one natural-prime packet locally repairable:             PROVED (prior);
fixed-radius cluster locally repairable:                  PROVED;
cluster merging changes R=Y^.038 exponent:                NO;
small-block positive square mixture at stable norm:       CLOSED BY (2.7);
macroscopic square controlled by termwise scalar KMT:     CLOSED BY (3.5)-(3.7);
KMT scalar data imply adaptive source covariance:         FALSE ABSTRACTLY;
actual-prime adaptive cross-Gram cancellation:            OPEN;
positive simultaneous antenna / actual Delsarte value:   OPEN;
QP-KILL, QP-PROMOTE, or zero-free strip:                  NOT PROVED.
```

The surviving lemma is now fully explicit.  For the actual smooth prime
measure and coefficients chosen from every Guth--Maynard bad-packet family,
prove directly that the signed quantities (3.2), together with their
off-packet analogues, have operator size `O(Y^(-.019+o(1)))` after the exact
normalization.  That is a vector-valued prime covariance theorem; it is not
contained in scalar KMT.

Executable replay:

- `src/qp_kmt_cluster_square_gate.py`;
- `src/test_qp_kmt_cluster_square_gate.py`;
- `results/verify_zeta23_qp_kmt_cluster_square_gate.py`.
