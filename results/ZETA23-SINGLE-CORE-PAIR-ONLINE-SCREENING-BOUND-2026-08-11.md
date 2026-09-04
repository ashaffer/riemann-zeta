# A single core pair with only on-line competitors cannot be power-screened

Status: exact sharp-kernel theorem before and after endpoint-jet compression,
and a moment-compatible artificial configuration, 2026-08-11.
This note makes no claim about the existence or location of an actual zeta
zero and does not prove a zero-free strip.

## 1. Verdict

Consider one simple reflected pair at fixed depth `alpha>0`, with ordinate in
the core of a symmetric sharp modulation band, and suppose every other local
atom is simple and on the critical line.  In the exact isolated-zero
normalization `1/L^2`, the on-line matrix satisfies

```text
||B_on|| <= pi*M*L+4*pi*M/L,                          (1.1)
```

where `M` is the largest number of on-line ordinates in a unit interval.  In
contrast, the pair has a negative direction orthogonal to its positive mate,
of size

```text
kappa_(alpha,L,W)
 >= sinh(alpha*L)/(alpha*L)-1
      - C*exp(alpha*L)/(L*W).                         (1.2)
```

Here `W` is the distance from the pair ordinate to the nearer edge of the
coordinate band.  Therefore

```text
K=-lambda_min(B_on+B_pair)
 >= kappa_(alpha,L,W)-pi*M*L-4*pi*M/L.                (1.3)
```

For a core pair, `W asymp T`; for the classical unit count, `M=O(log T)`;
and for `X=exp(L)` with `L=log T+o(log T)`, (1.3) becomes

```text
K >= (1+o(1))*sinh(alpha*L)/(alpha*L)
   = X^(alpha+o(1))/(2*alpha*L).                      (1.4)
```

Thus **simple on-line atoms cannot screen a single core pair by any fixed
power** in the unprojected sharp coordinate space.  The associated
rank-one Birman--Schwinger leverage tends to infinity, rather than merely
exceeding one.

This conclusion is compatible with the Zeta23 moment ledger.  There are
simple on-line configurations satisfying Riemann--von Mangoldt discrepancy
and the unit count for which, after adding the one pair,

```text
tr H=N+o(N),              tr(H^2)=(4/3)*N+o(N).       (1.5)
```

The pair changes the two quantities by only `o(N)` when `alpha<1/2`.
Consequently the first two moments neither force screening nor obstruct the
large negative edge in (1.4).

For the endpoint-jet space `V_m`, center an even sharp half-grid at the pair
ordinate and let `P_m` be the orthogonal projection.  Put

```text
kappa_jet
 = (2/L^2)*dist(P_m*y,span(P_m*x))^2.                 (1.6)
```

The exact compressed reduction is

```text
K_jet >= kappa_jet-pi*M*L-4*pi*M/L,                  (1.7)

b_jet >= kappa_jet/(pi*M*L+4*pi*M/L).                (1.8)
```

In the pair-centered symmetric placement, `P_m*x` and `P_m*y` have opposite
parity, so `kappa_jet=2*||P_m*y||^2/L^2`.  An explicit binomial-tail
trigonometric polynomial constructed in Section 7 proves

```text
kappa_jet
 >= c_alpha*L^(-2)
      *exp(alpha*L-C*alpha*sqrt(m*L/T)).               (1.9)
```

Consequently, in the endpoint budget `m/T=O(eta)`, `eta=o(L)`,

```text
kappa_jet>=X^(alpha-o(1))/L,
K_jet>=X^(alpha-o(1))/L.                             (1.10)
```

Thus the no-power-screening conclusion survives the endpoint jets for a
single pair on the centered core grid.  This is a genuine carrier lemma for
the **one-pair/all-other-atoms-on-line** model.  It does not cover additional
off-line pairs: their positive `x` rows occur at exponential scale and are
exactly what the legal sublattice constructions use for power screening.

## 2. Sharp rows and exact normalization

Put

```text
h=2*pi/L,
Phi_L(z)=integral_(-L/2)^(L/2) exp(i*z*t)dt
        =2*sin(L*z/2)/z.
```

Center a symmetric finite coordinate set at the distinguished ordinate
`gamma`:

```text
tau_k=gamma+k*h,             k in K_W,
K_W=-K_W,
|k*h|<=W+O(h).
```

Integer or half-integer symmetric indices may be used.  For a real ordinate
`r` and the lower member `z=gamma-i*alpha` of the reflected pair, write

```text
e_r=(Phi_L(r-tau_k))_(k in K_W),
v=(Phi_L(z-tau_k))_(k in K_W)=x+i*y.
```

All coefficient vectors are real.  With simple atoms, the exact normalized
matrices are

```text
B_on   =(1/L^2)*sum_(r in Lambda) e_r*e_r^T,
B_pair =(2/L^2)*(x*x^T-y*y^T),
H      =B_on+B_pair.                                  (2.1)
```

The factor `2` in `B_pair` accounts for the two reflected members.  No row
is duplicated and no factor of `L` is absorbed into the coefficient norm.

Reflection of the symmetric coordinate set gives

```text
v_(-k)=conj(v_k).
```

Therefore `x` is even, `y` is odd, and

```text
<x,y>=0.                                              (2.2)
```

This is the finite-band version of the exact bilinear Parseval identity for
the full sharp lattice.

## 3. The on-line Bessel bound

### Lemma 3.1 (unit-count sampling bound)

Let `Lambda` be any finite multiset of real ordinates such that

```text
M=sup_(j in Z) #(Lambda intersect [j,j+1))<infinity.
```

Then the normalized on-line matrix in (2.1) satisfies (1.1).

#### Proof

For a real coefficient vector `c`, set

```text
f_c(t)=1_[-L/2,L/2](t)*sum_k c_k*exp(-i*tau_k*t),
F_c(s)=integral f_c(t)*exp(i*s*t)dt=e_s^T*c.
```

The coordinate spacing is `2*pi/L`, so exact orthogonality gives

```text
||f_c||_2^2=L*||c||_2^2.                              (3.1)
```

For every unit interval `I` and every `s in I`, the fundamental theorem of
calculus, Cauchy--Schwarz, and averaging the comparison point over `I` give

```text
|F_c(s)|^2
 <=2*integral_I |F_c(u)|^2 du
   +2*integral_I |F_c'(u)|^2 du.                     (3.2)
```

There are at most `M` samples in `I`.  Summing (3.2) over the unit intervals
and using Plancherel gives

```text
sum_(r in Lambda)|F_c(r)|^2
 <=2*M*(||F_c||_2^2+||F_c'||_2^2)
 <=4*pi*M*L*(1+L^2/4)*||c||_2^2.                    (3.3)
```

Indeed, `F_c'` is the Fourier transform of `i*t*f_c` and
`|t|<=L/2`.  Dividing (3.3) by `L^2` proves

```text
c^T*B_on*c
 <=(pi*M*L+4*pi*M/L)*||c||_2^2.
```

QED

The deliberately elementary Sobolev estimate is more than sufficient here.
A local Bernstein sampling theorem improves the right side by a power of
`L`, but no such improvement is needed: under `M=O(L)`, (1.1) is already
only `O(L^2)=X^o(1)`.

## 4. Exact pair edge in a core band

On the two-sided infinite coordinate lattice, Parseval and bilinear
Parseval give

```text
||v||_2^2=L*integral_(-L/2)^(L/2) exp(2*alpha*t)dt
          =L*sinh(alpha*L)/alpha,

v^T*v=L^2.                                           (4.1)
```

Hence the infinite-lattice real and imaginary parts are orthogonal and

```text
(2/L^2)*||y||_2^2
 =sinh(alpha*L)/(alpha*L)-1
 =:kappa_infinity.                                   (4.2)
```

For the centered integer lattice one also has explicitly

```text
|v_k|^2
 =4*sinh(alpha*L/2)^2/((k*h)^2+alpha^2).             (4.3)
```

The analogous half-integer formula has `cosh` in place of `sinh` and obeys
the same upper estimate.  Since

```text
sum_(|k*h|>W) 1/(k*h)^2 <= C/(h*W)=C*L/W,            (4.4)
```

removing the coordinates outside the finite symmetric band loses at most

```text
(2/L^2)*sum_(|k*h|>W)y_k^2
 <=C*exp(alpha*L)/(L*W).                             (4.5)
```

Equations (2.2), (4.2), and (4.5) prove (1.2).  In particular, if
`W>=c*T` and `alpha>0` is fixed, the relative loss in (4.5) is `O_alpha(1/T)`.

### Theorem 4.1 (no power screening by on-line atoms)

Under the hypotheses above, (1.3) holds.

#### Proof

If `y` is nonzero, use the unit vector `c=y/||y||`.  By (2.2), the positive
mate contributes zero, the negative mate contributes
`-2*||y||^2/L^2`, and Lemma 3.1 bounds the on-line contribution from above.
This is (1.3).  QED

For the Zeta23 unit count, `M=O(log T)=O(L)`.  Thus, for every fixed
`alpha>0`, the on-line error is negligible relative to (4.2).  Notice that
this conclusion is uniform over arbitrary clustering of the simple on-line
atoms; no zero-separation hypothesis is used.

## 5. Birman--Schwinger leverage

Put

```text
p=sqrt(2)*x/L,
u=sqrt(2)*y/L,
A=B_on+p*p^T,
beta=pi*M*L+4*pi*M/L.                                (5.1)
```

Then `H=A-u*u^T`, `u` is orthogonal to `p`, and

```text
A<=beta*I+p*p^T.                                     (5.2)
```

If `u` is not in `range(A)`, the rank-one criterion gives a negative
direction immediately and its leverage may be recorded as infinity.  If
`u in range(A)`, the variational formula for the Moore--Penrose inverse and
(5.2) give

```text
b(A,u)=u^T*A^dagger*u
 >=u^T*(beta*I+p*p^T)^(-1)*u
 =||u||^2/beta
 =kappa_(alpha,L,W)/beta.                            (5.3)
```

Under the core and unit-count hypotheses, the last ratio is

```text
X^(alpha+o(1))/L^3 -> infinity.                      (5.4)
```

Thus the selected negative atom is not close to the screening threshold
`b=1`.  This is stronger than an inertia statement: it identifies the
scale on which the positive on-line population fails to dominate the pair.

## 6. Compatibility with the first two Zeta23 moments

The preceding theorem is not invalidated by requiring the normalized first
two moments to have their Zeta23 sizes.  The following construction makes
this explicit.

### Proposition 6.1 (simple on-line background with the `1,4/3` moments)

Let `N asymp T*L` and suppose the sharp coordinate density `L/(2*pi)` is
slightly larger than the target Riemann--von Mangoldt density on the dyadic
core.  There is an artificial configuration consisting of one simple
depth-`alpha` reflected core pair and `N-2` distinct simple on-line atoms
such that

```text
#(C intersect I)=integral_I log(t/(2*pi))/(2*pi)dt+O(1)
```

for intervals `I` in that dyadic core, every unit interval contains `O(L)`
points, and
the normalized sharp matrix satisfies (1.5).

#### Construction and proof

First choose a balanced subset of the real sharp grid in the dyadic core.
Cumulative rounding of the target density selects grid points with interval
discrepancy `O(1)`; this is possible because the target mass of each grid
cell is less than one.  The padding fraction is `o(1)`, so all but `o(N)`
selected points lie in long runs of adjacent grid cells.  A collar, if one
is included in a separate carrier theorem, contains only `o(N)` points in
the endpoint budget and may be filled by a separate quantile sequence; no
moment assertion about those rows is needed for the leading relations below.

In disjoint blocks of six selected adjacent grid points, use one block of
rows of the form

```text
e_k, e_(k+epsilon), e_(k+2), e_(k+3), e_(k+4), e_(k+5),               (6.1)
```

where the notation denotes ordinates near the corresponding sharp-grid
points and `epsilon>0` tends to zero so fast that

```text
epsilon*L*sqrt(N)->0.                                 (6.2)
```

Thus the second atom has been moved from the `(k+1)`st grid point to a
distinct point next to the `k`th.  The movement intervals are disjoint and
have length `O(h)`, so interval discrepancy changes by at most an absolute
constant.  The atoms remain simple and the unit count remains `O(L)`.

At `epsilon=0`, normalized sharp-grid rows are coordinate vectors.  Each
six-atom block then has one doubled coordinate, one hole, and four singleton
coordinates.  Its positive Gram matrix has

```text
trace=6,                trace(square)=2^2+4=8.        (6.3)
```

The exact sharp reproducing-kernel identity

```text
<e_r/L,e_s/L>=sin(L*(r-s)/2)/(L*(r-s)/2)             (6.4)
```

and (6.2) show that the distinct perturbed rows change the aggregate
moments by `o(N)`.  Using one such doubled pair per six atoms gives

```text
tr B_on=N-2+o(N),
tr(B_on^2)=(4/3)*(N-2)+o(N),
||B_on||=2+o(1).                                     (6.5)
```

Replace two nearby on-line atoms by the two members of the distinguished
reflected pair.  This changes interval discrepancy only by `O(1)`.
The pair eigenvalues on the full sharp lattice are

```text
kappa_infinity+2,             -kappa_infinity.       (6.6)
```

For fixed `alpha<1/2`,

```text
kappa_infinity^2
 =X^(2*alpha+o(1))/L^2=o(N).                         (6.7)
```

Its trace is `2`, its squared Frobenius norm is `o(N)`, and its cross term
with (6.5) is at most

```text
O(||B_on||*kappa_infinity)=o(N).                     (6.8)
```

Equations (6.5)--(6.8) prove (1.5).  QED

This construction is only a consistency model.  It is not asserted to be a
zero set of any `L`-function and it does not satisfy the zeta explicit
formula.  Its purpose is narrower: the count, simplicity, and the two bulk
moments are fully compatible with the unscreened single-pair edge.

## 7. Endpoint-jet compression and an explicit retained packet

Let `P` be any real orthogonal projection, in particular the projection
onto the endpoint-jet space `V_m`.  Set

```text
x_P=P*x,
y_P=P*y,
y_perp=y_P-proj_(span(x_P))(y_P),
kappa_P=2*||y_perp||^2/L^2.                          (7.1)
```

Compression does not increase the on-line norm, so Lemma 3.1 still gives
`||P*B_on*P||<=beta`.  Testing the compressed form on
`y_perp/||y_perp||` proves

```text
-lambda_min(P*H*P)>=kappa_P-beta.                    (7.2)
```

The same variational Moore--Penrose argument as in Section 5, now using the
component of `P*y` orthogonal to `P*x`, gives

```text
b_P>=kappa_P/beta                                    (7.3)
```

whenever the leverage is finite.  These are (1.7)--(1.8).

For a pair-centered symmetric coordinate set, the endpoint-jet subspace is
reflection invariant.  Its projection preserves parity, so

```text
<P*x,P*y>=0,
kappa_P=2*||P*y||^2/L^2.                             (7.4)
```

The bulk moment model also survives this compression at leading order.  In
the construction of Section 6, `||B_on||=O(1)`.  If `codim(P)=m=o(N)`, then

```text
tr(P*B_on*P)=tr(B_on)+O(m),
tr((P*B_on*P)^2)=tr(B_on^2)+O(m).                    (7.5)
```

The compressed pair has rank at most two and Hilbert--Schmidt norm no larger
than the uncompressed pair, so (6.7)--(6.8) remain `o(N)`.  Thus the
trace/Frobenius ledger places no additional obstruction on (7.2).

It remains to lower-bound this projection norm.  The following construction
does so without an interpolation determinant.

### Lemma 7.1 (a flat binomial-tail endpoint-jet packet)

Use an even symmetric coordinate subset with relative frequencies

```text
omega_q=q*h,
q in {-(J-1/2),...,-1/2,1/2,...,J-1/2},
h=2*pi/L.                                            (7.6)
```

Dropping at most one coordinate makes this possible for either parity of the
original coordinate count.  Put

```text
theta=2*pi*t/L,
R=J-1,
r=ceil(m/2),
u(t)=cos(theta/2)^2,

W_(R,r)(u)=sum_(j=r)^R binom(R,j)*u^j*(1-u)^(R-j),

p(t)=i*sin(theta/2)*W_(R,r)(u(t)).                    (7.7)
```

Assume `r<=R/4`.  Then `p` has a Fourier expansion in the modes (7.6) with
real coefficients `c_q`, belongs to `V_m`, and satisfies

```text
sum_q c_q^2<=1.                                      (7.8)
```

If

```text
s_0=(L/pi)*arcsin(sqrt(2*r/R)),                       (7.9)
```

then, for every fixed `alpha>0` and all sufficiently large parameters,

```text
abs(Im integral_(-L/2)^(L/2) p(t)*exp(alpha*t)dt)
 >=c_alpha*exp(alpha*L/2-alpha*s_0).                 (7.10)
```

#### Proof

The function `W_(R,r)` is the upper-tail probability

```text
P(Binomial(R,u)>=r).
```

It lies in `[0,1]`.  Since every term contains `u^r`, (7.7) has a zero of
order at least `2r>=m` at each endpoint.  As a polynomial of degree `R` in
`u=(1+cos(theta))/2`, `W` has only integer Fourier modes of order at most
`R`; multiplication by `i*sin(theta/2)` produces precisely real
coefficients on half-integer modes of order at most `R+1/2=J-1/2`.  Thus the
coefficient vector is real, uses (7.6), and is in `V_m`.

Exact Fourier orthogonality and `|p(t)|<=1` give

```text
L*sum_q c_q^2=integral |p(t)|^2dt<=L,
```

which is (7.8).

If `R*u>=2r`, the Chernoff lower-tail inequality gives

```text
W_(R,r)(u)
 >=1-exp(-R*u/8)
 >=1-exp(-r/4)>=1/2                                  (7.11)
```

eventually.  Write `t=L/2-s`.  By (7.9), condition (7.11) holds throughout
`s in [s_0,s_0+1]`.  Also

```text
sin(pi*t/L)=cos(pi*s/L)>=1/2
```

there for large parameters.  The function in (7.7) is purely imaginary and
odd.  Hence

```text
abs(Im integral p(t)*exp(alpha*t)dt)
 =2*integral_0^(L/2)
      sin(pi*t/L)*W_(R,r)(u(t))*sinh(alpha*t)dt.
```

Restricting this positive integral to the unit interval just displayed
proves (7.10).  QED

### Theorem 7.2 (core jet retention)

Suppose the pair ordinate is the center of the even grid (7.6), the
coordinate width satisfies `J asymp T*L`, and `m=o(T*L)`.  Then

```text
kappa_P
 >=c_alpha*L^(-2)
      *exp(alpha*L-C*alpha*sqrt(m*L/T)).              (7.12)
```

#### Proof

For the coefficient vector in Lemma 7.1, the lower-pair evaluation is

```text
F_c(gamma-i*alpha)=integral p(t)*exp(alpha*t)dt.
```

It is purely imaginary.  Since `c in V_m` and `||c||_2<=1`, (7.10) gives
a lower bound for the norm of the imaginary evaluation row projected onto
`V_m`.  Equation (7.4) then gives (7.12), because

```text
s_0
 <=C*L*sqrt(r/R)
 <=C*sqrt(m*L/T).                                    (7.13)
```

QED

In the carrier budget `m/T=O(eta)` and `eta=o(L)`, the loss in (7.12) is
`exp(-o(L))`.  Powers of `L` are also `X^o(1)`, so

```text
kappa_P>=X^(alpha-o(1))/L.                           (7.14)
```

Combining (7.14), (7.2), and the unit count `M=O(L)` proves (1.10).

The centered grid is a legal carrier choice for a selected core ordinate:
one translates the modulation grid so that the pair is at its midpoint, or,
in a strip contradiction indexed by the pair ordinate, chooses the dyadic
base height so that the ordinate is the midpoint.  This changes the two
band endpoints by at most one grid spacing.  The statement here is a
zero-side carrier theorem; a prime-side use must, as always, keep its
estimates uniform under that harmless common grid translation.

## 8. Consequence for the carrier search

The legal core sublattice construction uses many off-line pairs.  Their
positive `x` rows live at the same exponential scale as the selected
negative `y` row and can therefore produce genuine power screening.  Simple
on-line atoms are categorically different: their entire positive Gram
operator is at most polylogarithmic under the unit count.

Hence the single-deepest-pair carrier no longer needs a grouped interpolation
determinant: Lemma 7.1 directly controls the sharp projection quantity

```text
dist(P_m*y_(gamma-i*alpha),span(P_m*x_(gamma-i*alpha))).               (8.1)
```

at full power up to `X^o(1)`.  The unresolved hostile carrier case must
therefore use at least one additional off-line pair (or abandon the centered
core placement).  The simple-line density theorem limits how many such
exponential-scale positive mates are available, but controlling their joint
screening remains the signed grouped problem identified in the periodic-mask
audit.
