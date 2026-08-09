# Fixed-strip fourth-moment proof attempt

Status: exact full-moment width theorem proved, completed pair-cell reduction
and high-order-filter no-go proved, finite pair partitions audited;
2026-08-06.  The requested fixed-power arithmetic estimate remains open.
This note does **not** prove a new zero-free strip or the Riemann Hypothesis.

## 1. Verdict

The requested theorem was

```text
U_4(I)=integral_R abs(F_I(t))^4dt
 <=X^(2-kappa+o(1))                                     (1.1)
```

for one fixed `kappa>0`, uniformly on every admissible completed R71 block.
We did not prove (1.1).

The decisive new result is that (1.1) is already exponent-equivalent to the
fixed strip it was intended to prove.  For a continuously translated fixed
localizer,

```text
limsup_(R->infinity) log(1+U_4(R))/R=4 Delta.            (1.2)
```

Consequently

```text
(1.1) <=> Delta<=1/2-kappa/4
      <=> Re(rho)<=1-kappa/4                            (1.3)
```

at exponential scale, subject to the fixed-order exact-head packaging.
The forward implication in (1.3) is exact and loses no Sobolev factor.  The
reverse implication follows from the standard fixed-window zero expansion
and Hausdorff--Young.

Thus proving (1.1) from present arithmetic input would prove the still-open
quasi-Riemann hypothesis `sup Re(rho)<1`.  Calling it a near-product,
fourth-moment, or variance theorem does not make it weaker.

The proof attempt nevertheless yielded three useful closures.

1. Exact, near, and dyadically merged product cells have signed interference;
   none supplies diagonal domination or a monotone positive energy.
2. A power-saving mesoscopic variance for the centered
   `Lambda*Lambda` coefficient is itself equivalent to the same fixed strip.
3. A high-order scale filter cannot create a fixed real-axis contraction
   while retaining all off-line carriers with sublinear scale support.

## 2. Exact local moment exponent

Let `G` be the fixed-order complete coboundary detector.  Its fixed-window
zero expansion has the form

```text
G(R)=sum_lambda c_lambda exp(lambda R)+r(R),             (2.1)
```

where the zero-carrier coefficients are absolutely summable, every
nontrivial zero contributes a nonzero carrier
`lambda=rho-1/2`, the correction `r` has no nontrivial-zero pole, and

```text
sup_lambda Re(lambda)=Delta.                            (2.2)
```

Fix a nonzero `chi` in `C_c^infinity` and define

```text
g_R(u)=chi(u)G(R+u),
F_R(t)=integral g_R(u)exp(-itu)du,
U_p(R)=integral abs(F_R(t))^pdt,       2<=p<infinity.   (2.3)
```

### Theorem 2.1

For every fixed `2<=p<infinity`,

```text
limsup_(R->infinity) log(1+U_p(R))/R=p Delta.            (2.4)
```

### Upper bound

For every `epsilon>0`, absolute convergence of (2.1) gives

```text
abs(G(R+u))<=C_(chi,epsilon)exp((Delta+epsilon)R)        (2.5)
```

on the support of `chi`.  Hausdorff--Young, with
`p'=p/(p-1)`, gives

```text
norm(F_R)_p<=C_p norm(g_R)_(p')
            <=C_(p,chi,epsilon)exp((Delta+epsilon)R).   (2.6)
```

Raising (2.6) to the `p`th power proves that the left side of (2.4) is at
most `p Delta`.

### Lower bound

Fix a carrier `lambda_0` with
`delta=Re(lambda_0)>0`.  Choose `phi` smooth, supported in an open set where
`chi` is nonzero, and satisfying

```text
Phi(lambda_0)=integral phi(u)exp(lambda_0 u)du !=0.      (2.7)
```

A sufficiently narrow nonzero bump has this property.  Put
`conjugate(h)=phi/chi`.  Fourier duality and Holder give

```text
abs(L_phi(R))
 :=abs(integral phi(u)G(R+u)du)
 <=norm(hat(h))_(p') U_p(R)^(1/p)/(2pi).                (2.8)
```

Suppose the limsup in (2.4) were less than `p delta`.  Formula (2.8) would
give `L_phi(R)=O(exp(aR))` for some `a<delta`.  Its one-sided Laplace
transform would therefore be holomorphic on `Re(s)>a`.  Termwise use of
(2.1), however, gives a genuine pole at `s=lambda_0` with residue

```text
c_(lambda_0) Phi(lambda_0) !=0.                          (2.9)
```

No pole or archimedean correction can cancel this nontrivial-zero pole.
This contradiction proves a lower exponent `p delta`.  Taking the supremum
over carriers proves (2.4); no rightmost zero is required.

### Regular-block transfer

An every-block estimate transfers to (2.4) when the regular block family

1. covers every sufficiently large translate;
2. contains a fixed-width core on which the block weight is bounded below;
3. anchors that core at `R_I-o(R_I)`; and
4. has only `exp(o(R_I))` support and derivative losses.

For the lower bound, place `phi` in the core.  The Fourier norm in (2.8) is
translation invariant.  For the upper bound, the expanding support costs
only `exp(o(R_I))` in (2.6).  The exact Type-I head equals the full completed
field; the fixed-order explicit-center Euler defect is `exp(o(R_I))` and is
harmless for every positive fixed exponent.

Taking `p=4` proves (1.2)--(1.3).  More generally,

```text
U_(2m)<=X^(m-kappa+o(1))
 <=> Re(rho)<=1-kappa/(2m)                              (2.10)
```

at exponent scale.  If a moment is known only on a finite growing frequency
window, the R76 Sobolev fallback is still needed and loses the factor
`q/(4q+1)`.

## 3. Exact completed pair ledger

Write the faithful completed transform as

```text
F(t)=sum_i F_i(t),                                      (3.1)
```

where the channels include every boundary-truncated grouped product and the
signed full center.  Then exactly

```text
F(t)^2=sum_(i<=j)m_(ij)F_i(t)F_j(t),
m_(ij)=1 if i=j and 2 otherwise.                        (3.2)
```

For any partition `C` of these pair channels,

```text
U_4=D_atom+I_within(C)+I_across(C).                     (3.3)
```

Here `D_atom` is the sum of individual pair-channel energies,
`I_within` is the interference inserted by grouping channels within a cell,
and `I_across` is the remaining cross-cell interference.  Merging two cells
`H_a,H_b` changes the cell diagonal by

```text
2 Re inner(H_a,H_b),                                    (3.4)
```

which has no fixed sign.

In physical space, with `g=sum_n p_n-z_c`,

```text
U_4=2pi norm(g*g)_2^2,
g*g=sum_(n,m)p_n*p_m-2sum_n p_n*z_c+z_c*z_c.            (3.5)
```

Thus every product partition is a bookkeeping choice inside one completed
atomic--continuous convolution.  It cannot discard the cross-cell term.

The D-rated finite audit at `X=127,Y=8,T=80` gives

```text
U_4/D_atom=1.6334823915,
U_4/D_exact_product=1.5947043586.                       (3.6)
```

Near-product cell domination fails at every one of eight sampled offsets
for widths through `2/T`.  Dyadic merging is nonmonotone:

```text
D_cell(0.005)=0.00537434537
 >D_cell(0.01)=0.00511570682.                           (3.7)
```

The center lowers `U_4` by about `2.54%` in this block but raises it by about
`6.7%` at `X=205,Y=7`; it has no stable sign.  Removing boundary atoms does
not remove the finite failure.  These calculations refute the proposed
finite inequalities, not an asymptotic theorem special to the actual
coefficient.

## 4. Mesoscopic cells are the same strip in variance coordinates

Let the pair-product scale be

```text
M=X^2,
T=X^tau,
H=M/T.                                                  (4.1)
```

Let `E_2(x,H)` be the interval error for `Lambda*Lambda` after subtracting
the complete `s=1` polynomial main term and retaining the continuous center.
A smoothed Gallagher/Plancherel reduction shows that a variance estimate

```text
integral_M^(2M) abs(E_2(x,H))^2dx
 <<H^2 M^(1-2sigma+o(1))                                (4.2)
```

would give

```text
U_4<<M^(1-2sigma+o(1))
    =X^(2-4sigma+o(1)).                                 (4.3)
```

Thus (4.2) would prove (1.1) with `kappa=4sigma`.

It is not an easier theorem.  Put `L=-zeta'/zeta`.  The Dirichlet series of
`Lambda*Lambda` is `L(s)^2`.  At a zero `rho` of multiplicity `m_rho`,

```text
L(s)^2=m_rho^2/(s-rho)^2+O(1/(s-rho)).                  (4.4)
```

The double-pole coefficient is never zero.  Perron inversion supplies a
term

```text
x^rho(C_rho log x+D_rho),       C_rho!=0.               (4.5)
```

Its increment over a cell of length `H=o(M)` has size
`H M^(beta-1)` times a nonzero logarithmic factor.  A smoothed frequency
localization, or equivalently the pole argument of Theorem 2.1, gives along
a subsequence

```text
integral_M^(2M) abs(E_2(x,H))^2dx
 >=H^2 M^(2beta-1-o(1)).                                (4.6)
```

Comparing (4.2) and (4.6) forces

```text
beta<=1-sigma=1-kappa/4.                                (4.7)
```

The fact that the cells are very long therefore does not create spare
exponent.  The Gallagher conversion and the zero contribution consume the
same factor.

## 5. The connected Selberg identity does not close the estimate

The exact identity

```text
Lambda*Lambda+Lambda log=mu*log^2,
L^2-L'=zeta''/zeta                                     (5.1)
```

cancels the double pole of `L^2` at a simple zero.  The resulting
`zeta''/zeta` generally has a simple pole, but that pole can be removable at
a simple zero satisfying `zeta''(rho)=0`; at a multiple zero it retains a
double pole.  This qualification prevents treating the connected term alone
as a complete zero detector.

More decisively, recovering `L^2` from (5.1) requires the derivative term
`L'`.  On the arithmetic side this is `Lambda log`, and a fixed-power bound
for its centered interval error is a power-saving prime number theorem,
again equivalent to a fixed zero-free strip.  In the norm square
`norm(L^2)^2`, the derivative enters with no favorable sign.  Bounding the
two pieces separately either assumes the target or loses their exact
cancellation.

## 6. High-order scale filters pay back their contraction

Consider any forward-shift filter

```text
P_R=sum_(j=0)^(n_R)a_(j,R)tau_(j h_R),
L_R=n_R h_R,
p_R(z)=sum_(j=0)^(n_R)a_(j,R)exp(jh_R z).               (6.1)
```

Bernstein--Walsh for the polynomial in `w=exp(h_R z)` gives, for `d>=0`,

```text
sup_t abs(p_R(d+it))
 <=exp(d L_R) sup_t abs(p_R(it)).                       (6.2)
```

Suppose the real-axis filter contracts by a fixed exponential amount,

```text
sup_t abs(p_R(it))<=exp(-aR+o(R)),       a>0.            (6.3)
```

For (6.2) even to permit nonexponential attenuation of every carrier on
`Re(z)=d_0`, it is necessary that

```text
L_R/R>=a/d_0-o(1).                                      (6.4)
```

Thus a sublinear-support filter has `a=0`.  Fixed center-annihilating factors
change neither exponent in (6.2).

For the repeated difference `((tau_h-1)/A)^m`, strict real-axis contraction
requires `A>2`.  At the resonant carrier phases `gamma h` in `2pi Z`, carrier
retention at displacement `d_0` requires

```text
exp(hd_0)-1>=A>2,
hd_0>log 3.                                             (6.5)
```

Taking `m` proportional to `R` therefore gives linear support.  If
`h=o(1)` is used to keep the support sublinear, the resonant carrier factor
is `O(h)^m` and becomes superexponentially small; normalizing it back makes
the real-axis norm explode.

There is also an arithmetic cost.  If `L_R=lambda R`, the filter samples
scales through `X^(1+lambda)`.  The elementary square-root scale becomes

```text
(1+lambda)/2-a
 >=1/2+lambda(1/2-d_0)>1/2.                             (6.6)
```

The support cost therefore exceeds the maximum retained contraction for
every `d_0<1/2`.  Absolutely continuous smoothing is no escape: its Fourier
multiplier tends to zero at large ordinates, and a proportional number of
iterations exponentially deletes some fixed zero carriers.

## 7. Where the proof attempt stops

The following methods reach `kappa=0` and no farther.

* Hyperbola dispersion followed by Cauchy loses the Mobius signs and returns
  the `X^2` pair-frame term.
* Circle/Mellin diagonalization moves the contour only until the same zero
  poles are met.
* Exact-product and near-product restriction omit signed cross-cell
  interference.
* Selberg connectedization trades the pair field for a derivative field of
  the same zero-free-strip strength.
* Proportional-order filtering requires proportional scale support, whose
  arithmetic cost restores the critical exponent.
* Current shifted-correlation and higher-uniformity estimates are
  almost-all or logarithmic; after the every-block conversion they give
  `kappa=0`.

The first genuinely missing statement is still (1.1), or equivalently the
variance (4.2).  Theorem 2.1 proves that either one is already the fixed
zero-free strip in a different norm.  No independent sign, contraction,
integrality, or averaging principle was found that proves it.

## 8. Reproducibility

The completed pair-cell ledger is implemented in
[`src/r71_pair_cell_probe.py`](../src/r71_pair_cell_probe.py), with focused
tests in
[`src/test_r71_pair_cell_probe.py`](../src/test_r71_pair_cell_probe.py).
It reconstructs `F^2` before partitioning, retains the signed center and all
boundary channels, and verifies (3.3) for every tested partition.

Run

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_r71_fixed_strip_moment_probe.py \
  src/test_r71_pair_cell_probe.py

PYTHONPATH=src python3 src/r71_pair_cell_probe.py \
  --scale 127 --cutoff 8 --height 80 --frequency-step 0.5 \
  --cell-widths 0.0025 0.005 0.00625 0.01 0.0125 0.025 \
  --offset-count 8 --gaussian-order 12
```

The computations are D-rated finite falsifications only.  Theorem 2.1 and
the filter tradeoff are analytic arguments independent of those runs.
