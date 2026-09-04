# A depth-sensitive microscopic zero count

Status: exact explicit-formula lemma and application to the `0.99` carrier
ledger, 2026-08-12.  This sharpens the depth-blind local count used in the
current Pick analysis.  It does not prove a global Pick theorem, a zero-free
strip, or RH.

## 1. Statement

Let

```text
L=log |t|,        h=C/L,
```

where `C>0` is fixed.  For every fixed `1/2<sigma_0<1`, the number of
nontrivial zeta zeros, counted with multiplicity, satisfying

```text
Re rho>=sigma_0,       |Im rho-t|<=h
```

obeys

```text
N_cell(sigma_0,t;C)
 <=[(1-sigma_0)/2]*L+O_(sigma_0,C)(sqrt(L)).        (1.1)
```

The estimate is uniform in the location of the microscopic ordinate cell.
For off-line reflected pairs, the number of right-half pair centers is at
most the left side of (1.1), so the same bound applies without an additional
factor of two.

At the first fixed-strip target

```text
alpha_0=0.49,       d_0=0.66,
```

the selected zero has real part at least `0.99`, while the
carrier-relevant depth threshold is

```text
sigma_min=1/2+alpha_0*d_0=0.8234.                  (1.2)
```

Consequently one microscopic cell contains at most

```text
beta>=0.99:       (0.005+o(1))*L zeros,
beta>=0.8234:     (0.0883+o(1))*L zeros.            (1.3)
```

These constants are materially smaller than the depth-blind total ceiling,
but they still allow a growing near-confluent cluster.

## 2. Completed logarithmic derivative

Put

```text
Xi(s)=(1/2)*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s).
```

The Hadamard product and the standard normalization of `Xi` give, for
`s=sigma+i*t` with `1<sigma<=2` and `|t|>=3`,

```text
sum_rho (sigma-Re rho)
        /[(sigma-Re rho)^2+(t-Im rho)^2]

 = (1/2)*log(|t|/(2*pi))
   +Re[zeta'(s)/zeta(s)]+O(1).                     (2.1)
```

The sum is over all nontrivial zeros with multiplicity.  It is absolutely
convergent in this positive real-part form.  The rational factors in `Xi`
and the error in the digamma asymptotic are absorbed by the `O(1)` term;
that error is uniform for `1<=sigma<=2` and `|t|>=3`.

For `sigma>1`, absolute convergence of the von Mangoldt series gives

```text
abs(zeta'(sigma+i*t)/zeta(sigma+i*t))
 <=-zeta'(sigma)/zeta(sigma)
 <=1/(sigma-1)+O(1).                               (2.2)
```

Every term on the left of (2.1) is positive.  Therefore

```text
sum_rho (sigma-Re rho)
        /[(sigma-Re rho)^2+(t-Im rho)^2]
 <=(1/2)*L+1/(sigma-1)+O(1).                       (2.3)
```

## 3. Proof of the microscopic count

Choose

```text
u=L^(-1/2),       sigma=1+u,
A=1+u-sigma_0.                                      (3.1)
```

At this choice, (2.1)--(2.2) give the stronger two-sided equilibrium

```text
sum_rho (1+u-Re rho)
        /[(1+u-Re rho)^2+(t-Im rho)^2]
 =(1/2)*L+O(sqrt(L)),                               (3.1a)
```

uniformly in `t`.  The upper half of (3.1a) is what is needed for the
count; the lower half records that the leading Poisson budget is
asymptotically filled rather than merely bounded.

For every zero counted by `N_cell`, put

```text
a=sigma-Re rho,       v=t-Im rho.
```

Then

```text
u<=a<=A,       |v|<=h<=u                           (3.2)
```

for all sufficiently large `t`.  Here the lower bound uses the standard
fact that every nontrivial zeta zero has real part strictly below one.  On
this rectangle the Poisson kernel

```text
a/(a^2+v^2)
```

is minimized at `a=A`, `|v|=h`.  Hence each counted zero contributes at
least

```text
A/(A^2+h^2).                                       (3.3)
```

Combining (2.3) and (3.3) yields the explicit finite-height inequality

```text
N_cell(sigma_0,t;C)
 <=[(A^2+h^2)/A]*[(1/2)*L+sqrt(L)+O(1)].           (3.4)
```

Since `sigma_0` and `C` are fixed,

```text
(A^2+h^2)/A=1-sigma_0+L^(-1/2)+O(L^(-2)),          (3.5)
```

and (1.1) follows.

## 4. What this changes in the Pick search

The old local ledger allowed an `O(L)` cluster with a depth-independent
coefficient.  Equation (1.1) instead supplies the cumulative depth cap

```text
#{rho in one cell: Re rho>=1/2+b}
 <=(1/4-b/2+o(1))*L.                               (4.1)
```

For a maximal target of depth `alpha`, the Blaschke cost of a collateral
row increases with `b`.  Thus (4.1), rather than the total zero count, is
the correct constraint in any depth-integrated Pick extremal.

This does not by itself close the global quantifier.  In particular,
`(0.005+o(1))L` is still a genuinely linear allowance.  More generally the
cumulative cap permits `Theta(L)` distinct zeros, spread through
`Theta(L)` microscopic depth cells, inside one ordinate phase cell.  For
example, at the `0.99` target one may put one effective depth representative
at each gap

```text
alpha-b=k/L,       1<=k<=0.01*L,                   (4.2)
```

without violating (4.1): at a depth gap `x` the number `xL` is at most
`(0.01+x)L/2` for `0<=x<=0.01`.  This is an allowed abstract allocation,
not a claim about the actual zeta divisor.

Thus (1.1) does not imply one effective condition per ordinate phase cell.
The coherent microcluster theorem collapses arbitrary cardinality only in
one bounded `L`-rescaled depth--ordinate rectangle; it does not collapse the
growing depth fan (4.2).  A growing confluent Pick construction can still
turn such a fan into a fixed-power carrier loss.  Deciding that competition
requires a uniform high-jet interpolation theorem, a global half-disk Pick
theorem, or a new actual-zeta anti-confluence input.

### 4.1 The Poisson budget couples background and discrepancy

There is nevertheless a structural improvement over treating the
Riemann--von Mangoldt background and endpoint discrepancy as independent
adversarial measures.  Write an off-line reflected pair at ordinate `tau`
as

```text
1/2+b+i*tau,       1/2-b+i*tau,       0<b<1/2.
```

Its combined contribution to (2.3), at `sigma=1+u`, is

```text
P_(u,b)(x)
 =(1/2+u-b)/[(1/2+u-b)^2+x^2]
  +(1/2+u+b)/[(1/2+u+b)^2+x^2],

x=t-tau.                                            (4.3)
```

Exactly

```text
integral_R P_(u,b)(x)dx=2*pi,                       (4.4)
```

independently of `b` and `u`.  Hence a uniform off-line pair-center
background of density `L/(4*pi)` contributes `L/2`, exactly the leading
value in (3.1a).  The analogous statement for critical-line zeros uses
one Poisson kernel of integral `pi` and density `L/(2*pi)`, with the same
total.  Thus a local endpoint cluster must displace background mass in this
Poisson-smoothed ledger; it cannot simply be superposed without charge.

This coupling is rigorous, but its smoothing scale is too coarse to settle
the Pick problem.  The Fourier transforms make the lost information exact.
For `q=|xi|>0`,

```text
Fourier[P_(u,b)](xi)
 =2*pi*exp(-(1/2+u)*q)*cosh(b*q).                   (4.5)
```

The target Pick potential at depth `alpha>=b`,

```text
V_(alpha,b)(x)
 =(1/2)*log{
   [(alpha+b)^2+x^2]/[(alpha-b)^2+x^2]},            (4.6)
```

has, away from the zero frequency,

```text
Fourier[V_(alpha,b)](xi)
 =2*pi*exp(-alpha*q)*sinh(b*q)/q.                   (4.7)
```

The exact deconvolution multiplier from (4.5) to (4.7) is therefore

```text
exp[(1/2+u-alpha)*q]*tanh(b*q)/q.                   (4.8)
```

For a `0.99` target, `1/2-alpha=0.01`; at microscopic frequencies
`q asymp D=dL`, (4.8) has the fixed-power size

```text
exp[(0.01+o(1))*D]=Y^(0.01+o(1)),
Y=exp D.                                            (4.9)
```

Thus transferring the positive logarithmic-derivative bound from the Euler
half-plane to the cell-scale Pick potential is an inward analytic
continuation with exactly the small fixed-power loss which the raw
`alpha=0.49` carrier cannot afford.  Equations (4.3)--(4.9) do not prove
that every nonlinear or sign-only Pick transfer pays this loss.  They do
show why the depth-sensitive count, by itself or through a translation-
invariant linear deconvolution, is not the missing global Pick theorem.

### 4.2 Fixed-width reflected-pair cap

The same positive budget gives a stronger count than (1.1) for a list
which spans a fixed ordinate interval.  Let `I` have fixed length `H`, and
suppose `N_pair` horizontal reflected pairs have ordinates in `I` and
right-half depths

```text
1/2+b_j,       0<b_0<=b_j<=b_1<1/2.
```

Put

```text
a_R=1/2-b_0,       a_L=1/2+b_1.
```

Then, for every fixed padding `s>0`,

```text
N_pair/L
 <=(H+2*s)
   /{2*sum_(a in {a_R,a_L})
       [atan((H+s)/a)+atan(s/a)]}
   +o(1).                                          (4.10)
```

Indeed, integrate (2.3) over the interval obtained by padding `I` by `s`
on both sides.  Its total positive budget is

```text
(H+2*s)*L/2+o(L).                                  (4.11)
```

For a zero of horizontal distance at most `a` whose ordinate lies in `I`,
the integrated kernel is minimized at an endpoint of `I` and is at least

```text
atan((H+s)/a)+atan(s/a)+o(1).                      (4.12)
```

Both horizontal members of every pair occur in the Poisson sum.  Their
distances are bounded above by `a_R` and `a_L`, respectively, so summing
(4.12) and comparing with (4.11) proves (4.10).

For the interlaced binomial Pick screen in
`ZETA23-GLOBAL-HALFDISK-PICK-BINOMIAL-AND-POISSON-AUDIT-2026-08-12.md`,

```text
H=c*pi/d,       N_pair/L=2*c+o(1),
b_0=b_1=.49-o(1),       d=.66.
```

Taking `s=.003` in (4.10) gives

```text
c<=0.00465416454... .                              (4.13)
```

The corresponding forced Schur attenuation is at most

```text
c*log[.49*.66/(2*pi*c)]
 <=0.01118512309... .                              (4.14)
```

This is below the old conditional reserve `0.0119000134...`.  Applying the
microscopic cap `(0.005+o(1))L` to the whole fixed-width screen would be
incorrect: that screen occupies `Theta(L)` microscopic phase cells.  The
integrated estimate (4.10), not the one-cell estimate, is the relevant
restriction.

There is also a clean long-interval density corollary.  For an arbitrary
off-line pair, the two limiting horizontal distances add to one and each is
at most one.  Take `s=sqrt(H)` in the preceding proof and then let `H` tend
to infinity.  Uniformly in the interval location,

```text
N_pair(I)
 <=[H/(4*pi)+O(sqrt(H))]*L+o(L).                   (4.15)
```

Consequently the off-line pair-center measure has long-interval upper
Beurling density at most `L/(4*pi)+o(L)`, without adding a Bellotti--Wong
endpoint discrepancy as an independent mass.  The `O(sqrt(H))*L` boundary
allowance in (4.15) is essential: (4.15) does **not** give a strict uniform
density margin in every fixed short interval, and therefore does not by
itself settle finite-section Pick conditioning.

## 5. Truth boundary

Proved here:

1. the explicit finite-height bound (3.4);
2. the asymptotic microscopic count (1.1);
3. the numerical depth caps (1.3);
4. the fixed-width reflected-pair cap (4.10);
5. the long-interval pair-density bound (4.15).

Not proved here:

1. that actual zeta realizes, or avoids, the extremal clusters allowed by
   (1.1);
2. that local Pick losses multiply across cells;
3. the global compact Pick transfer;
4. any arithmetic lower edge or zero-free strip.
