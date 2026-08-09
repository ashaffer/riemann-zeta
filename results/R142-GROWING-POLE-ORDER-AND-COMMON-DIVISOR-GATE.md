# R142 growing pole order and common-divisor gate

## Status

R141 left a deliberately nonlinear possibility: multiply many positive
degree-zero detectors so that a zeta zero shared by all factors has high pole
order, while an auxiliary zero belonging to one factor has low order.  The
product keeps nonnegative Dirichlet coefficients, and deleted prime heads
multiply their support thresholds.  At first sight this appears to improve
both the divisor and Euler sides simultaneously.

The improvement is illusory under every presently available absolute
estimate.  This report proves four exact statements.

1.  The multinomial which amplifies a common pole occurs identically in the
    product of the remote-zero ledgers.  It cancels from the comparison.
2.  The square-root Fourier cost is invariant under arbitrary tensor powers:
    distributing the Euler saddle among the factors gives exactly the old
    exponent `lambda/(2r)`.
3.  Lower Laurent coefficients can cancel the nominal high-order pole
    exponentially.  A sharp local model shows that reliable order-`m`
    amplification requires derivative order `k>>m^2`, leaving only a
    subexponential gain.
4.  There are exact positive common-divisor detectors obtained by
    differentiating products.  They remove an individual simple zero and
    retain a zero shared by all factors.  Scalarization necessarily creates
    derivative-critical or algebraic hypersurface zeros, and the surviving
    prime layer keeps the coefficient threshold at `1/2`; vector/corona
    formulations merely restate the missing joint lower bound.

Thus a growing pole-order tensor does not cross the R141 square-root wall.
The only escape is a target-conditioned signed theorem controlling the full
Laurent factor, not merely its highest-order coefficient.

```text
common-pole binomial amplification             EXACT
identical remote-ledger binomial                EXACT
tensor square-root exponent                     INVARIANT
regular-Laurent exponential cancellation        EXACT
positive derivative common-divisor detector     EXACT
scalar exact common-zero detector                IMPOSSIBLE
joint Laurent/L-function correlation             OPEN
fixed uniform zero-free strip                    NOT PROVED
zeros approaching one                            NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md`](R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md).

## 1. Product jets: the source and error have the same entropy

Let `A_1,...,A_m` be meromorphic Dirichlet series with nonnegative
coefficients, allowing repetitions, and put

```text
B(s)=product_(nu=1)^m A_nu(s).                                (1.1)
```

For

```text
J_k(H)=(-1)^k H^(k)/k!,                                      (1.2)
```

Leibniz gives the exact identity

```text
J_k(B)
 =sum_(k_1+...+k_m=k) product_nu J_(k_nu)(A_nu).              (1.3)
```

Suppose every factor has a simple pole at `rho`, with residue `c_nu`, and
write

```text
z_*-rho=d,                  K=k+m.                            (1.4)
```

The product has top Laurent term

```text
C(s-rho)^(-m),              C=product_nu c_nu.               (1.5)
```

Its contribution to (1.2) at `z_*` is

```text
binom(K-1,m-1) C d^(-K).                                    (1.6)
```

This binomial is the proposed source amplification.  It is not a surplus.
If the only factorwise remote estimate is

```text
|J_l(A_nu)(z_*)|<=M_nu R^(-l-1),                             (1.7)
```

then summing the same weak compositions in (1.3) gives

```text
|J_k(B)(z_*)|
 <=binom(K-1,m-1)[product_nu M_nu]R^(-K).                    (1.8)
```

The binomial in (1.6) and (1.8) cancels exactly.  Repeating a favorable
factor does not help: its remote constant is raised to the same power as its
source residue.

## 2. Tensoring preserves the square-root wall

Assume factor `A_j` is repeated `h_j` times and its positive coefficients
vanish below `X_j`.  The product support begins beyond

```text
product_j X_j^(h_j).                                         (2.1)
```

The order-`k` Euler saddle for a product with total pole order

```text
m=sum_j h_j,                  K=k+m                          (2.2)
```

is shifted beyond its maximum only when

```text
sum_j h_j log X_j=lambda K/r,             lambda>1.          (2.3)
```

For the R140 full-character interpolant, the absolute Fourier cost of one
factor is

```text
L_(X_j)=X_j^(1/2+o(1)).                                      (2.4)
```

The tensor cost is therefore

```text
product_j L_(X_j)^(h_j)
 =exp[(lambda/(2r)+o(1))K].                                  (2.5)
```

The largest Cauchy localization gain remains

```text
exp[K log(R/d)],
log(R/d)<1/(2r)<lambda/(2r).                                 (2.6)
```

Equations (2.5)--(2.6) are independent of how the saddle is divided among
the factors and of their multiplicities.  Tensoring preserves, rather than
beats, the square-root exponent.

## 3. A sharp local Laurent countermodel

The top Laurent coefficient is also badly conditioned when `m` grows.  Put

```text
w=s-rho,                 z_*=rho+d,
A_d(w)=c(1/w-1/d).                                           (3.1)
```

The function `A_d` has residue `c` at `rho`, but it vanishes at the
evaluation point.  Hence `A_d^m` has an order-`m` pole at `rho` and an
order-`m` zero at `z_*`.  Direct Taylor expansion gives

```text
J_k(A_d^m)(z_*)=0,                              k<m,          (3.2)

|J_k(A_d^m)(z_*)|
 =|c|^m binom(k-1,m-1)d^(-k-m),                 k>=m.         (3.3)
```

If only the top pole in (3.1) were retained, the advertised value would be

```text
|c|^m binom(k+m-1,m-1)d^(-k-m).                              (3.4)
```

The exact conditioning ratio is

```text
Q_(k,m)
 =product_(j=1)^(m-1)(k-j)/(k+j)
 <=exp[-m(m-1)/k].                                           (3.5)
```

Therefore a lower bound which treats all lower Laurent terms as a
perturbation needs at least

```text
k >> m^2.                                                     (3.6)
```

In this range

```text
log binom(k+m-1,m-1)=O(sqrt(k)log k)=o(k).                   (3.7)
```

The reliable divisor-order gain is subexponential and cannot repair the
strict exponential inequality (2.6).

The same phenomenon has an exact general form.  Write near `rho`

```text
B(w)=Cw^(-m)H_m(w),
H_m(w)=sum_(j>=0)q_jw^j,                  q_0=1.              (3.8)
```

The complete principal part at `z_*`, divided by the isolated contribution
(1.6), is

```text
sum_(j=0)^(m-1) q_j d^j (m-1)_j/(K-1)_j.                    (3.9)
```

Here `(a)_j` denotes the falling factorial.  If `m/K->theta`, expression
(3.9) samples `H_m(theta d)`, not `H_m(0)`.  For a product of simple-pole
detectors,

```text
H_m(w)=product_nu [w A_nu(rho+w)/c_nu].                      (3.10)
```

If `rho=1-epsilon+i gamma`, every fixed `theta>0` eventually evaluates
(3.10) in `Re(s)>1`, exactly where head deletion makes the Euler factors
small.  Keeping the sampling point on the other side of one forces

```text
theta<=epsilon/(r+epsilon)->0,                               (3.11)
```

which deletes the proposed positive-density pole-order entropy.

## 4. The zeta-tail sanity theorem

Any broad pole-order lower bound would prove a false statement even for a
finite truncation of the classical zeta logarithmic derivative.  Define

```text
A_X(s)
 =D_zeta(s)-sum_(n<=X)Lambda(n)n^(-s)
 =sum_(n>X)Lambda(n)n^(-s),               Re(s)>1.            (4.1)
```

It has nonnegative coefficients supported beyond `X` and retains the simple
pole of `D_zeta` at every zeta zero.  Thus `A_X^m` has nonnegative
coefficients supported beyond `X^m` and an order-`m` pole at every zeta zero.

Nevertheless, Cauchy's estimate on the circle of radius `r/2` around
`z_*=1+r+i gamma` gives

```text
|J_k(A_X^m)(z_*)|
 <=(2/r)^k [sum_(n>X)Lambda(n)n^(-1-r/2)]^m
 <<_r (2/r)^k X^(-mr/2).                                    (4.2)
```

For fixed `m,k`, this tends to zero with `X`.  Positivity, support, and pole
order alone therefore imply no useful lower bound.  The removed finite head
reappears as the regular Laurent terms which cancel the pole contribution.

## 5. What remains open

The only tensor escape is a theorem of the form

```text
abs[sum_(j=0)^(m-1)q_j d^j(m-1)_j/(K-1)_j]
 >=exp[-o(K)],                                                (5.1)
```

conditioned on the selected zeta zero, together with noncoincidence of that
zero with a positive proportion of the auxiliary divisors.  Positivity of
the Euler coefficients gives no control of (5.1); the sanity theorem shows
why.  Marginal zero density and formal distinctness of the `L`-functions do
not control exact local coincidences either.

The common-divisor constructions below sharpen the algebraic side, but do
not supply (5.1).

## 6. A positive common-zero derivative detector

There is an exact way to remove a *forced individual zero* without giving up
ordinary coefficient positivity.  Let

```text
P(s)=product_(j=1)^m F_j(s),                                  (6.1)
```

where every `F_j` has nonnegative ordinary Dirichlet coefficients.  Then,
for every integer `0<=q<m`,

```text
K_(m,q)(s)=(-1)^q P^(q)(s)                                   (6.2)
```

also has nonnegative coefficients.  If `rho` is a zero of every `F_j`, of
total order `M>=m`, then

```text
ord_rho K_(m,q)>=M-q.                                        (6.3)
```

In particular,

```text
K_(m,1)=-(product_j F_j)'                                    (6.4)
```

retains order at least `m-1` at a common simple zero.  For two factors,

```text
K_(2,1)=-F_1'F_2-F_1F_2'.                                   (6.5)
```

At a simple zero of `F_1` where `F_2` is finite and nonzero, (6.5) equals
`-F_1'F_2` and is nonzero.  Thus (6.5) exactly distinguishes a forced common
zero from a forced individual simple zero.

This does not remove the R138 obstruction.  The unfavorable auxiliary
divisors are zeros of denominator `L`-functions, hence poles of the positive
quotients `F_j`.  Differentiating `P` preserves or increases those poles.
Moreover, (6.2) inevitably has accidental derivative-critical zeros, and its
prime coefficient is

```text
[p]K_(m,q)=(log p)^q [p]P.                                   (6.6)
```

For every fixed nontrivial family, Chebotarev leaves (6.6) nonzero on a
positive-density prime set.  Its coefficient-square abscissa remains
`1/2`; common-zero multiplicity has not bought a smaller arithmetic
threshold.

## 7. Sum-of-squares scalarization and its unavoidable spurious divisor

For two factors another exact local gadget is

```text
S=(F_1F_2)^2+(F_1'F_2)^2+(F_1F_2')^2.                        (7.1)
```

Every summand has nonnegative ordinary Dirichlet coefficients, so the same
is true of `S`.  At a common simple zero of `F_1,F_2`, the function `S` has a
zero of order at least two.  At an individual simple zero, one derivative
term is nonzero.  At an individual pole, `S` has a pole; hence `1/S` is
analytic there and has a pole at the desired common zero.

The price is exact:

```text
S=(F_1F_2)^2[1+A_1^2+A_2^2],            A_j=-F_j'/F_j.       (7.2)
```

The hypersurface

```text
1+A_1^2+A_2^2=0                                             (7.3)
```

creates an uncontrolled extra zero divisor.  Passing to `1/S` or
`-S'/S` then turns it into uncontrolled poles and loses coefficient
positivity.

This is not a poor choice of polynomial.  Let `Phi` be a nonconstant scalar
holomorphic function of `N>=2` complex jet variables, with `Phi(0)=0`.
The zero germ of `Phi` has complex codimension one; it cannot consist only
of the common origin.  Equivalently, every scalar holomorphic
common-divisor test has nontrivial zero points arbitrarily close to the
origin.  A scalar sum of holomorphic squares is not a Hermitian norm over
`C`, and (7.3) is its minimal manifestation.

Wronskians make the same trade.  The determinant

```text
W=F_1F_2'-F_1'F_2                                          (7.4)
```

vanishes at a common simple zero and not at a forced individual simple zero,
but its Dirichlet coefficients are signed.  Normalizing gives
`W/(F_1F_2)=A_1-A_2`, which is just the signed difference of logarithmic
derivatives.

## 8. Why the vector version is only a corona restatement

A vector-valued holomorphic map can have an isolated common zero.  For
example,

```text
V=(F_1F_2, -F_1'F_2, -F_1F_2')                              (8.1)
```

has componentwise nonnegative Dirichlet coefficients, vanishes at a common
simple zero, and does not vanish at a forced individual simple zero.  This
avoids the scalar hypersurface theorem.

To use (8.1), however, one must prove a row lower bound

```text
sum_j |V_j(s)|^2 >=c(s)>0                                   (8.2)
```

or solve a Bezout/corona equation for the tuple in the target strip.
Equation (8.2) excludes exactly the common zeta divisor which the
construction was designed to detect.  Coefficientwise positivity gives no
lower bound on complex values, and scalarizing (8.1) holomorphically returns
the spurious hypersurface; scalarizing Hermitianly loses analyticity and the
Dirichlet-series divisor calculus.

Exterior powers, resultants, and Koszul determinants are equivalent choices:
they either remain vector-valued and require the same corona estimate, or
become scalar and acquire signed coefficients or a new divisor.

## 9. Verdict

Growing pole order and common-divisor algebra are both real, but neither
changes the quantitative problem.  Tensor products repay their source
binomial in the remote ledger and in their regular Laurent germs.
Differentiated products isolate common zeros only while leaving the
unfavorable poles and the prime `1/2` threshold.  Scalar exterior gadgets
add an uncontrolled divisor; vector gadgets ask directly for the missing
joint nonvanishing theorem.

The next branch should therefore test the remaining R141 permutation mask:
whether low-support Frobenius elements in a solvable/monomial transitive
group necessarily become completely split in a large intermediate field.
If so, the apparent approximate-splitting escape collapses back to the exact
root-discriminant gate.

**Successor update (R143--R144).**  This collapse is now proved for solvable
closures, with sharp orbit bound `2L`.  The nonsolvable primitive remainder
is natural `A_m/S_m`, where a new falling-support virtual character deletes
bounded-support Frobenii exactly.  The live obstruction has therefore moved
from tensor order and support fraction to cheap prescribed Frobenius plus
local noncancellation of a signed virtual Artin divisor.
