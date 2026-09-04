# Prime-Voronoi localized boosting: the exact Schur-margin gate

**Date:** 2026-08-13

**Verdict:** translated Voronoi kernels really do give accurate local
correctors: after modulation, the quadrature error depends on `t-t_j`, not
on the absolute height `t`.  This permits a correction around one bad
component over relative distances below `Y^.751...`.  It does **not** yield
a global boosting theorem.  Preserving even the single low anchor while
correcting one high value costs the inverse square root of

```text
1-|k_Y(t_j)|^2,                                      (0.1)
```

and correcting many components costs the inverse of a conditional Schur
Gram matrix.  The entries outside the local relative aperture are exactly
the unresolved high-tail aliases.  A fourth-moment bound on the number of
bad components supplies neither the one-point margin (0.1) nor a lower
eigenvalue for this matrix.

The antenna coefficients themselves have no imposed norm bound.  Therefore
a tiny but nonzero Schur margin is not an impossibility theorem: it permits
an enormous correction.  It is an exact obstruction to the proposed
`l2`-controlled iterative contraction and to every leakage estimate that
uses coefficient size.  Only a zero pivot is outright infeasibility.

Even granting the proposed count

```text
N_bad<=Y^.0855                                       (0.2)
```

at threshold `epsilon=Y^(-.0180303234)`, the raw translated corrections can
leak

```text
N_bad epsilon^2=Y^.0494393532...                     (0.3)
```

back into the low anchor.  Local Gershgorin control would require
`N_bad epsilon<1`, whereas that product is `Y^.0674696766...`.  The ordinary
coefficient `l2` norm can remain small, but the full aperture multiplies its
mean-square ledger by `Y^(50/33)` and gives a positive exponent even under
optimistic orthogonality.

Thus localized boosting is not closed, but it has been reduced exactly to
the same carrier-relative Christoffel/Schur margin as H1.  Component count,
local quadrature, and coefficient `l2` size do not prove that margin.

No zero-free strip is claimed.

---

## 1. The translated local kernel is legitimate

Normalize the positive Voronoi weights from
`ZETA23-PRIME-GAP-VORONOI-ANTENNA-AND-HIGH-TAIL-STRIP-GATE-2026-08-13.md`
so that

```text
q_p>0,                 sum_p q_p=1,                  (1.1)

k_Y(s)=sum_p q_p exp(i s v_p),
v_p=log(p/Y).                                          (1.2)
```

Let

```text
kappa(s)=
 [integral_(-w)^w phi(u)exp(i s u)du]
 /[integral_(-w)^w phi(u)du].                         (1.3)
```

The mean-square-gap Voronoi theorem gives, for every fixed auxiliary
`eta>0`,

```text
|k_Y(s)-kappa(s)|<<_eta |s|Y^(-77/100+eta),           (1.4)

|kappa(s)|<< (1+s^2)^(-1).                            (1.5)
```

For a center `t_j`, modulating the coefficients by
`exp(-i t_j v_p)` produces exactly

```text
sum_p q_p exp(-i t_j v_p)exp(i t v_p)=k_Y(t-t_j).
                                                               (1.6)
```

So the local error in (1.4) genuinely depends on `t-t_j`.  In particular,
if `c=.0180303234`, then throughout the relative annulus

```text
Y^(c/2)<=|t-t_j|<=Y^(77/100-c-2eta),                  (1.7)
```

equations (1.4)--(1.5) give

```text
|k_Y(t-t_j)|<<Y^(-c+o(1)).                            (1.8)
```

This is the useful content of localization.  It controls no pair whose
relative displacement is larger than about `Y^.751969...`, and in
particular gives no estimate for leakage from a high center back to zero
once the center is beyond that relative aperture.

---

## 2. Raw boosting and its low leakage

Suppose a current residual has value `y_j` at `t_j`.  Since `k_Y(0)=1`,
the raw correction

```text
R_j(t)=-y_j k_Y(t-t_j)                                (2.1)
```

kills that value exactly.  Its value at the low anchor is

```text
R_j(0)=-y_j k_Y(-t_j).                                (2.2)
```

If the current residual is the kernel itself, so that
`y_j=k_Y(t_j)`, then

```text
|R_j(0)|=|k_Y(t_j)|^2.                                (2.3)
```

Thus a threshold-sized bad value is squared at the anchor, which looks
helpful for one correction.  But for `N` unconstrained centers the triangle
ledger is

```text
sum_j |R_j(0)|<=sum_j |y_j||k_Y(t_j)|.                (2.4)
```

If both factors are only known to be of threshold size `epsilon`, (2.4)
allows `N epsilon^2`.  With the numbers in (0.2),

```text
.0855-2(.0180303234)=.0494393532>0.                   (2.5)
```

Hence the squared one-center leakage is not perturbative after the allowed
number of corrections.  Values larger than threshold only worsen this
unconditional ledger.

One can subtract an additional low kernel to force (2.2) to vanish.  The
cost of doing so is not free; it is exactly the Schur margin in the next
section.

---

## 3. Exact one-center and many-center Schur formulas

Give coefficient vectors the weighted Hilbert norm

```text
||c||_(q^-1)^2=sum_p |c_p|^2/q_p.                     (3.1)
```

The evaluation functional

```text
E_t(c)=sum_p c_p exp(i t v_p)                         (3.2)
```

has representer

```text
h_t=(q_p exp(-i t v_p))_p,                            (3.3)

<h_s,h_t>_(q^-1)=k_Y(t-s).                            (3.4)
```

### Lemma 3.1 (one-anchor localized correction)

The least possible norm of a correction satisfying

```text
E_0(c)=0,             E_t(c)=1                        (3.5)
```

is

```text
inf ||c||_(q^-1)^2=1/[1-|k_Y(t)|^2],                 (3.6)
```

provided the denominator is positive.  If its denominator is zero, (3.5)
is infeasible.

#### Proof

Project `h_t` orthogonally off `h_0`.  Since both have norm one, the squared
norm of the residual representer is

```text
||h_t-<h_t,h_0>h_0||^2=1-|k_Y(t)|^2.                 (3.7)
```

The minimum-norm vector representing value one on this residual functional
has squared norm equal to the reciprocal of (3.7).  QED

The formula extends without loss to arbitrary low samples and bad centers.
Let

```text
S={s_1,...,s_m},        T={t_1,...,t_N},              (3.8)

G_S=(k_Y(s_j-s_i))_(i,j),
K_TS=(k_Y(s_j-t_i))_(i,j),
K_TT=(k_Y(t_j-t_i))_(i,j).                            (3.9)
```

After imposing `E_s(c)=0` for `s in S`, the Gram matrix of the projected
bad-center evaluations is the Schur complement

```text
M_(T|S)=K_TT-K_TS G_S^dagger K_ST.                   (3.10)
```

For a target vector `y` in its range, exact least-norm interpolation gives

```text
inf {||c||_(q^-1)^2:
     E_s(c)=0 (s in S), E_ti(c)=y_i}
 =y^* M_(T|S)^dagger y.                              (3.11)
```

Equations (3.10)--(3.11) are the carrier-relative Christoffel formula for
localized boosting.  A count of rows bounds neither
`lambda_min(M_(T|S))` nor the directional pseudoinverse in (3.11).
Since the dual coefficient norm is unconstrained, largeness of (3.11) alone
does not exclude a coefficient vector.  It says exactly why the proposed
norm-controlled correction cannot be certified and why uniform
between-sample leakage remains unbounded by this method.

### Lemma 3.2 (the exact iterative pivot)

The Schur obstruction is not removed by correcting the peaks one at a time.
Suppose `S_r` is the set of samples whose values an iteration already
preserves, `P_r` is orthogonal projection onto

```text
span{h_s:s in S_r},                                   (3.12)
```

and a new center is `t`.  Define its conditional pivot by

```text
pi_r(t)=||(1-P_r)h_t||_(q^-1)^2
       =1-K_(t,S_r) G_(S_r)^dagger K_(S_r,t).          (3.13)
```

If the new correction must vanish on `S_r` and have value `y` at `t`, its
least possible squared norm is exactly

```text
|y|^2/pi_r(t).                                        (3.14)
```

For the minimum-norm sequential interpolant these increments are
orthogonal.  Consequently its squared norm after `r` corrections is

```text
sum_(j<=r) |y_j^(res)|^2/pi_(j-1)(t_j),               (3.15)
```

where `y_j^(res)` is the value still to be removed when `t_j` is selected.
If the ordered Gram matrices are nonsingular and the ordering starts from
the empty set, Schur determinant factorization also gives

```text
det G_(S_r)=product_(j<=r) pi_(j-1)(t_j).             (3.16)
```

With a nonempty initial protected set, the right side is multiplied by its
initial Gram determinant.

Thus iteration merely exposes the conditional margins one pivot at a time.
A small far-alias pivot makes the norm jump; revisiting old centers without
preserving them instead gives the usual Gram-system iteration, whose
convergence is controlled by the same smallest eigenvalue.  Neither version
has a rate from the number of peak components alone.

There is an additional exactness warning.  Requiring a finite exponential
polynomial to vanish on the entire low interval forces it to vanish
identically.  Equivalently, `M` suitably chosen distinct low samples give a
full Vandermonde matrix on the `M` distinct nodes.  A real construction may
only keep its low leakage small, not impose continuum zero leakage.  A
finite sampled Schur formula is therefore a necessary diagnostic, not an
automatic continuum solution.

There is a useful quantitative sampling ledger for the continuum warning.
Since `sum q_p=1`, Cauchy--Schwarz gives

```text
sum_p |c_p|<=||c||_(q^-1),
sup_t |(E_t c)'|<=w||c||_(q^-1).                      (3.17)
```

If a correction is forced to vanish on a grid of spacing `d` in a low
interval of length `T`, then

```text
sup_low |E_t c|<=w||c||_(q^-1)d.                     (3.18)
```

Keeping this below `epsilon` therefore uses on the order of

```text
m_low >= T w||c||_(q^-1)/epsilon                     (3.19)
```

low samples.  Even in the optimistic regime in which all Schur pivots are
constant-sized and the fourth-moment peak ledger gives
`sum |y_j|^2<<epsilon^(-5/2+o(1))`, one has

```text
||c||_(q^-1)<<epsilon^(-5/4+o(1)),
m_low=Y^[tau+(9/4)c+o(1)].                            (3.20)
```

For `tau=.01` and `c=.0180303234`, the last exponent is
`.05056822765...`.  This is dimensionally affordable, but every added low
sample decreases the conditional matrix in positive-semidefinite order.
No lower bound for the resulting pivots follows from affordability.

---

## 4. Why local accuracy does not control the Schur matrix

For pairs of centers whose difference lies in (1.7), equation (1.8) gives
an off-diagonal entry of size `O(epsilon)`.  If one uses only Gershgorin,
then a group of `N` centers requires

```text
N epsilon<1.                                          (4.1)
```

Under (0.2), however,

```text
.0855-.0180303234=.0674696766>0.                      (4.2)
```

so (4.1) fails by a fixed power.

One could demand local quadrature error at most `1/N`.  From (1.4), this
restricts the controlled relative diameter to

```text
|t_i-t_j|<=Y^(77/100-.0855-o(1))=Y^.6845-o(1).        (4.3)
```

The full aperture has exponent `50/33=1.51515...`; it contains
polynomially many such slabs.  Entries between distinct slabs are outside
the proven relative aperture.  A correction in a later slab can therefore
recreate an order-one alias in every earlier slab or in the low band.
Because the kernel is Hermitian, ordering the slabs does not produce a
one-sided or triangular escape.

This is not merely an artifact of Gershgorin.  Any improvement requires a
lower eigenvalue or a directional inverse bound for (3.10), which is the
original all-coefficient high-tail problem in matrix form.

### 4.1 Spectral support is preserved, but a hard local cutoff is unavailable

Translation in `t` only modulates the prime coefficients, so (1.6) retains
exactly the original logarithmic-frequency nodes `v_p`.  There is no loss of
spectral support in forming a translated corrector.

That fact also limits attempts to erase its far aliases.  Multiplying
`k_Y(t-t_j)` by a time cutoff convolves its logarithmic-frequency measure
with the Fourier transform of the cutoff.  A compactly supported time cutoff
has noncompact Fourier support and is not representable on the same finite
prime shell.  If one reserves an interior spectral margin `rho` and uses a
cutoff bandlimited to `[-rho,rho]`, the product remains inside the
*continuous* shell, but it is no longer supported on the finite prime-node
set and must be discretized again.  No nonzero such cutoff is compactly
supported in time.  Its continuous tails can be made rapidly decreasing;
the discrete quadrature remainder still
obeys only

```text
O(|t-t_j|Y^(-77/100+eta)),                            (4.4)
```

which loses every saving at relative displacement `Y^(77/100+o(1))`.
Smoother continuous tapers therefore improve `kappa`, not the unresolved
prime-log alias.  The support-margin maneuver does not supply the missing
far entries of (3.10).

---

## 5. Fourth moments count components but do not create margin

Let `F` have derivative bounded by a fixed `L`, and let

```text
E_4=integral_I |F(t)|^4dt.                            (5.1)
```

Every component of `{|F|>epsilon}` which contains a point of height at
least `2epsilon` contains an interval of length `gg epsilon/L` on which
`|F|>=epsilon`.  Therefore

```text
N_bad<<L E_4 epsilon^(-5).                            (5.2)
```

This is the legitimate fourth-moment component count behind localized
boosting.  It says nothing about:

```text
1-|k_Y(t_j)|^2,
lambda_min M_(T|S),
or k_Y(t_i-t_j) for far-separated centers.            (5.3)
```

An equal-grid countermodel makes the logical gap exact.  For nodes
`u_j=-w+jh` with equal positive weights,

```text
|k(2 pi/h)|=1.                                        (5.4)
```

There may be only one bad alias in a chosen high interval, but Lemma 3.1
has zero margin there: no correction can kill the alias while preserving
the anchor.  Thus even `N_bad=1` does not imply a usable localized
corrector.  Actual prime logs are not an equal grid, but ruling out their
approximate aliases is precisely the missing arithmetic theorem.

---

## 6. Small coefficient `l2` does not give a boosting contraction

For raw corrections (2.1), the combined coefficient vector is

```text
c_p=-q_p sum_j y_j exp(-i t_j v_p).                   (6.1)
```

The Voronoi quadratic norm obeys

```text
sum_p q_p^2<<Y^(-77/100+o(1)).                        (6.2)
```

If `N=Y^kappa` values all have threshold scale `epsilon=Y^(-c)`, triangle
inequality gives

```text
sum_p |c_p|^2
 <=Y^[-77/100+2kappa-2c+o(1)].                        (6.3)
```

At `kappa=.0855` and `c=.0180303234`, the exponent in (6.3) is

```text
-.77+.171-.0360606468=-.6350606468.                   (6.4)
```

This looks small.  But the Montgomery--Vaughan mean value over the full
aperture `B=Y^(50/33)` gives the ledger

```text
integral_0^B |sum_p c_p exp(i t v_p)|^2dt
 <<(B+Y)sum_p |c_p|^2,                                (6.5)
```

whose exponent is

```text
50/33-.6350606468=.8800908683...>0.                  (6.6)
```

Even optimistically replacing `N^2` in (6.3) by `N`, as if all modulated
coefficient vectors were orthogonal, gives

```text
50/33-.77+.0855-.0360606468
 =.7945908683...>0.                                  (6.7)
```

Thus coefficient `l2` remains far too weak to show that one boosting round
has less high-band energy than the peaks it removes.  Converting (6.5) to a
supremum incurs the already-audited derivative loss.

---

## 7. Decision

```text
modulated Voronoi kernel has local t-t_j accuracy:       PROVED;
one-anchor minimum correction cost:                      EXACT (3.6);
many-center conditional Schur formula:                   EXACT (3.10)-(3.11);
fourth moment bounds number of robust bad components:    YES;
component count implies Schur margin:                    FALSE;
N_bad epsilon^2 low leakage is perturbative:             FALSE;
local Gershgorin closes at proposed exponents:            FALSE;
small coefficient l2 gives full-band contraction:        FALSE;
far-alias/nonlattice prime-log bound:                     OPEN;
localized boosting closes H1:                            NOT PROVED;
uniform zeta zero-free strip:                            NOT PROVED.       (7.1)
```

Localized boosting remains a viable *organization* only if supplemented by
one genuinely new estimate:

```text
lambda_min M_(T|S)>=Y^(-o(1))                         (7.2)
```

for every legal bad-center set, or the corresponding directional bound in
(3.11), while the sampled low set controls the continuum low band.  That is
not a consequence of fourth moments or local quadrature; it is a precise
restatement of the unresolved conditional Christoffel gate.
