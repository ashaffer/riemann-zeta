# R99 lcm, factorial, and integrality ramp gate

Status: a new exact factorial/lcm divisibility certificate, a complete
integer Möbius inversion of factorial valuation profiles, and an exact
square-root-support certificate for the one-sided von Mangoldt ramp.  The
arithmetic support reduction succeeds: all prime-power layers above an
arbitrary cutoff `M` can be cancelled, leaving an integer of logarithmic
size `O(NM)`.  The signed factorial ratio which performs the cancellation,
however, is exactly the complementary high-prime ramp.  Bounding its size
on either side is equivalent, up to the small residual, to the original
fixed-power target.  R101 subsequently proves that the tempting exact
square-root sign conjecture for this ratio is false: its logarithm has
Littlewood-scale oscillations of both signs.  Positive factorial, binomial,
or Barnes-G multipliers cost `Theta(N^2)`; signed ratios span every profile
and therefore make finite valuation LPs tautological.  No fixed zero-free
strip and no failure of every fixed strip is proved.

Date: 2026-08-07.

## 1. Verdict

Recall from R96 that

```text
Q_N=L_N^N / product_(m=1)^(N-1)L_m^2,
L_m=lcm(1,...,m),                                      (1.1)

N R(N)=log Q_N-N+1,                                   (1.2)

v_p(Q_N)=sum_(p^k<=N)(2p^k-N).                        (1.3)
```

The integrality search found two exact constructions.

First,

```text
D_N
 =[(N!/L_N)^N]
  /product_(m=1)^(N-1)(m!/L_m)^2                     (1.4)
```

is always a positive integer.  This is a genuine divisibility law which is
not visible from (1.1).  If `N=a q+r`, `0<=r<q`, then the contribution of a
prime-power layer `q=p^k` to `v_p(D_N)` is

```text
d_N(q)=(a-1)(2q-r)>=0.                                (1.5)
```

It cancels every layer `q>N/2`.  Unfortunately

```text
log D_N=Theta(N^2),                                   (1.6)
```

so it gives only the exponent-one bound already available trivially.

Second, the factorial valuation transform admits an exact integer Möbius
inverse.  For every cutoff

```text
1<=M<N/2                                               (1.7)
```

there is an explicit signed factorial ratio `P_(N,M)` such that

```text
(Q_N P_(N,M))^(-1)
 =product_p p^[sum_(p^k<=M)(N-2p^k)]                  (1.8)
```

is an integer.  Its entire uncancelled profile is supported on prime powers
at most `M`, and

```text
0<=log (Q_N P_(N,M))^(-1)
  =sum_(q<=M)(N-2q)Lambda(q)
  <<N M.                                               (1.9)
```

Thus `M=floor(sqrt(N))` achieves exactly the requested
`O(N^(3/2))` residual, even without a polylogarithmic loss.

This does not yet bound `R(N)`.  The cancelling ratio satisfies the exact
identity

```text
log P_(N,M)
 =sum_(M<q<=N)(N-2q)Lambda(q),                         (1.10)

N R(N)
 =-log P_(N,M)
  -sum_(q<=M)(N-2q)Lambda(q)-N+1.                     (1.11)
```

The unknown in (1.11) is the original prime barycenter, restricted to the
complementary range.  The integer in (1.8) controls the second term but says
nothing about the size of the first.

The strongest tempting endpoint conjecture was

```text
P_(N,floor(sqrt(N)))<=1.                              (1.12)
```

If (1.12) held eventually, (1.9)--(1.11) would give

```text
R(N)>=-C sqrt(N),                                     (1.13)
```

and the R96 Landau theorem would prove zero-freeness in
`Re(s)>1/2`, hence RH by the functional equation.  The estimate at integers
extends to all real `x`: on `[N,N+1)` the atomic sums are fixed and
Chebyshev's bound gives `abs(R(x)-R(N))=O(1)`.  A finite scan through
`N=20,000,000` found no violation of (1.12).

[R101](R101-LITTLEWOOD-RAMP-SIGN-KILL.md) now proves rigorously that this
finite pattern cannot persist.  Unconditionally,

```text
R(N)=Omega_+ (sqrt(N) log log log N)
     and Omega_- (sqrt(N) log log log N),

log P_(N,floor(sqrt(N)))
 =Omega_+ (N^(3/2) log log log N)
  and Omega_- (N^(3/2) log log log N).                (1.14)
```

Thus (1.12) and its reverse each fail infinitely often.  The prime
valuations, factorial majorization tails, and Möbius coefficients of
`P_(N,M)` all have both signs, and the value itself now has proved
two-sided oscillation.  This kills the exact square-root endpoint only;
one-sided bounds with any fixed exponent `a>1/2` remain open.

## 2. The canonical factorial/lcm integer

Put

```text
F_m=m!/L_m.                                            (2.1)
```

Each `F_m` is an integer.  The non-obvious assertion in (1.4) is the
divisibility

```text
product_(m<N) F_m^2 divides F_N^N.                    (2.2)
```

**Theorem 2.1 (canonical factorial/lcm divisibility).**  For every integer
`N>=2`, `D_N` in (1.4) is an integer.  More precisely, its prime-power layer
is (1.5).

### Proof

Fix `q=p^k<=N`.  Its contribution to `v_p(F_m)` is

```text
max(floor(m/q)-1,0).                                  (2.3)
```

Write `N=a q+r`, `0<=r<q`.  The elementary floor sum is

```text
sum_(m=1)^(N-1)floor(m/q)
 =q a(a-1)/2+a r.                                     (2.4)
```

Therefore the contribution to (1.4) is

```text
N(a-1)
 -2 sum_(m=1)^(N-1)max(floor(m/q)-1,0)
 =(a-1)(2q-r).                                        (2.5)
```

It is nonnegative.  Summing (2.5) over the powers of each prime proves
(2.2).  QED.

When `q>N/2`, `a=1` and (2.5) vanishes.  The construction therefore performs
a real high-layer cancellation.  It does not leave a square-root-size
profile.  For `N/3<p<=N/2`, one has `a=2` and

```text
d_N(p)=4p-N>=N/3.                                     (2.6)
```

The prime number theorem, used here only as an imported classical lemma,
gives

```text
log D_N
 >=(N/3)[theta(N/2)-theta(N/3)]
 =Omega(N^2).                                         (2.7)
```

Chebyshev's upper bound gives the matching `O(N^2)`.  Thus (1.6) is exact
at the power scale.

## 3. Every unsigned integer multiplier has quadratic cost

The failure in Section 2 is not peculiar to `D_N`.

**Theorem 3.1 (quadratic unsigned-multiplier barrier).**  Let `A_N` be a
positive integer.

1. If `A_N Q_N` is an integer, then `log A_N=Omega(N^2)`.
2. If `A_N/Q_N` is an integer, then `log A_N=Omega(N^2)`.

### Proof

For `N/4<p<=N/3`, there is only one power of `p` below `N`, and

```text
v_p(Q_N)=2p-N<=-N/3.                                  (3.1)
```

Thus the first assertion requires `v_p(A_N)>=N/3` for every such prime, so

```text
log A_N
 >=(N/3)[theta(N/3)-theta(N/4)]
 =Omega(N^2).                                         (3.2)
```

For `3N/4<p<=N`,

```text
v_p(Q_N)=2p-N>=N/2.                                   (3.3)
```

The same argument proves the second assertion.  QED.

Factorials, binomial coefficients, and integer Barnes-G values are positive
integers.  Any product of them with nonnegative exponents falls under
Theorem 3.1.  No selection or LP optimization inside that cone can have
subquadratic logarithmic cost.

## 4. The exact factorial valuation transform

Signed ratios are much more flexible.  Let `h(1),...,h(N)` be arbitrary
integers.  Define

```text
C_h(d)=sum_(m<=N/d)mu(m)h(md),                        (4.1)

c_h(d)=C_h(d)-C_h(d+1),       C_h(N+1)=0,             (4.2)

P_h=product_(d=1)^N(d!)^[c_h(d)].                     (4.3)
```

Negative exponents are allowed in (4.3), so `P_h` is a positive rational
number.

**Theorem 4.1 (integer Möbius inversion of factorial layers).**  For every
`1<=q<=N`,

```text
sum_(d=1)^N c_h(d)floor(d/q)=h(q).                    (4.4)
```

Consequently

```text
v_p(P_h)=sum_(p^k<=N)h(p^k),                          (4.5)

log P_h=sum_(q<=N)h(q)Lambda(q).                      (4.6)
```

### Proof

The floor function is a sum of tail indicators.  Hence

```text
sum_d c_h(d)floor(d/q)
 =sum_(j<=N/q) sum_(d>=jq)c_h(d)
 =sum_(j<=N/q)C_h(jq).                                (4.7)
```

Insert (4.1), group by `ell=mj`, and use divisor Möbius inversion:

```text
sum_j sum_m mu(m)h(mjq)
 =sum_(ell<=N/q)h(ell q)sum_(m|ell)mu(m)
 =h(q).                                               (4.8)
```

Legendre's formula now gives (4.5), and summing valuations times `log p`
gives (4.6).  QED.

The finite matrix behind (4.4) is

```text
A_(q,d)=floor(d/q),            1<=q,d<=N.             (4.9)
```

It is upper triangular with diagonal one, so `det A=1` and its inverse is
integral.  Thus a finite exact solve will always find a signed factorial
ratio for every requested layer profile.  Such success is algebraic
universality, not evidence for a ramp inequality.

The matrix is not totally unimodular: it already contains entries equal to
two.  Replacing factorial layers by the `0-1` divisibility incidence matrix
does not repair this.  Rows `(2,3,5)` and columns `(6,10,15)` give

```text
[1 1 0]
[1 0 1]                                               (4.10)
[0 1 1]
```

with determinant `-2`.  LP relaxations can therefore produce fractional
vertices which have no integral divisibility meaning.  The full triangular
system is unimodular, but the sign-constrained subproblems are not protected
by total unimodularity.

## 5. Exact cancellation down to an arbitrary cutoff

Apply Theorem 4.1 with

```text
h_(N,M)(q)
 =(N-2q) 1_(q>M),                                     (5.1)

P_(N,M)=P_[h_(N,M)].                                  (5.2)
```

The layer of `Q_N` is `2q-N`.  Therefore

```text
layer_q(Q_N P_(N,M))
 =2q-N,        q<=M,
 =0,           q>M.                                  (5.3)
```

If `M<N/2`, every surviving layer in (5.3) is negative.  This proves (1.8)
exactly.  Moreover,

```text
E_(N,M)
 :=log (Q_N P_(N,M))^(-1)
 =sum_(q<=M)(N-2q)Lambda(q)                           (5.4)

0<=E_(N,M)<=N psi(M)<<N M.                           (5.5)
```

The last estimate uses only Chebyshev's bound.  The requested valuation
profile reduction therefore exists with a better-than-advertised error:

```text
M=floor(sqrt(N))  ->  E_(N,M)=O(N^(3/2)).             (5.6)
```

This is the strongest positive result of the route.

## 6. Why the square-root certificate is not a ramp bound

Equation (4.6) gives

```text
log P_(N,M)
 =sum_(M<q<=N)(N-2q)Lambda(q).                        (6.1)
```

Combining (5.4) with (1.2) gives (1.11).  Thus:

```text
upper bound for R  <-> lower bound for log P_(N,M),
lower bound for R  <-> upper bound for log P_(N,M),   (6.2)
```

up to the explicit error `O(NM)`.  For `M=N^theta`, any estimate at scale
`N^(1+a)` with `a>=theta` is the original fixed-power theorem with only a
short initial prime-power segment removed.

The integrality assertion in (1.8) says only

```text
log Q_N+log P_(N,M)=-E_(N,M)<=0.                     (6.3)
```

But (6.3) is the definition (5.4), whose sign is already termwise obvious.
It does not bound either summand separately.

The conditioning is necessarily quadratic.  Take `M<=N/4`.  For primes

```text
N/4<p<=N/3,
```

`P_(N,M)` has positive valuation `N-2p>=N/3`; for primes
`3N/4<p<=N`, it has negative valuation at most `-N/2`.  Hence the numerator
and denominator of this rational number both have logarithm `Omega(N^2)`.
The desired `O(NM)`-scale value is cancellation between two
quadratic-logarithmic integers.  Bounding numerator and denominator
separately loses exactly the needed power.

## 7. Möbius and majorization reality checks

The factorial exponents expose where that cancellation went.  Define

```text
M_0(x)=sum_(m<=x)mu(m),
M_1(x)=sum_(m<=x)m mu(m).                              (7.1)
```

For (5.1), formula (4.1) becomes

```text
C_(N,M)(d)
 =N[M_0(floor(N/d))-M_0(floor(M/d))]
 -2d[M_1(floor(N/d))-M_1(floor(M/d))].               (7.2)
```

Also, summation by parts in the factorial index gives the exact identity

```text
log P_(N,M)=sum_(d=2)^N C_(N,M)(d)log d.              (7.3)
```

Thus Stirling has not converted the prime cancellation into a smooth
archimedean remainder.  It has converted it into signed Mertens sums.
Equivalently, inserting

```text
Lambda(n)=sum_(d|n)mu(d)log(n/d)                      (7.4)
```

in (6.1) gives

```text
log P_(N,M)
 =sum_(d<=N)mu(d)
   sum_(M/d<m<=N/d)(N-2dm)log m.                     (7.5)
```

The continuous leading term of the inner sum contains `-N^2/(2d)`.
Obtaining a fixed power from (7.5) requires fixed-power cancellation in
weighted sums of `mu(d)/d`; this is another standard reciprocal-zeta form
of the zero-free-strip problem.

Simple factorial inequalities do not orient (7.3).  Since

```text
C_h(d)=sum_(e>=d)c_h(e),                              (7.6)
```

one would have `P_h<=1` immediately if all `C_h(d)<=0`, and the reverse
inequality if all were nonnegative.  But for `M<N/3`,

```text
N/3<d<=N/2  -> C_(N,M)(d)=h(d)-h(2d)=2d>0,

N/2<d<=N    -> C_(N,M)(d)=h(d)=N-2d<0.               (7.7)
```

So monotonicity fails deterministically.  Discrete convexity also fails as
a generic certificate.  At `N=100`, `M=10`, the double tails

```text
sum_(d>=j)C_(N,M)(d)
```

take the values `1104` at `j=11` and `-2550` at `j=51`.  The standard
majorization sufficient conditions therefore have both signs before any
asymptotics enter.

## 8. Factorial, binomial, and Barnes-G classes are exhausted

The three proposed integer families do not define independent signed
valuation lattices:

```text
binomial(a,b)=a!/[b!(a-b)!],                           (8.1)

G(n+1)=product_(d=1)^(n-1)d!,                         (8.2)

n!=G(n+2)/G(n+1).                                    (8.3)
```

Therefore:

1. With nonnegative exponents they are positive integers and fall under the
   quadratic barrier of Theorem 3.1.
2. With signed exponents, factorial and Barnes-G ratios generate the same
   lattice, while binomial ratios lie inside it.
3. That lattice already realizes every finite layer profile by Theorem 4.1.
   A valuation LP can always cancel the ramp exactly, even by choosing the
   tautological profile `h(q)=N-2q`, which gives `P_h=1/Q_N`.
4. The only missing datum is a one-sided numerical inequality for the
   resulting signed rational product.  Valuations alone cannot supply it.

This is a sharp class closure: adding more factorial or Barnes-G scales
cannot improve the valuation solvability, because it is already complete.
Adding only positive integer factors cannot improve the logarithmic cost,
because the prime intervals in Theorem 3.1 already force `Theta(N^2)`.

## 9. The square-root sign conjecture is false

For `M=floor(sqrt(N))`, the cleanest proposed extra statement was

```text
sum_(sqrt(N)<q<=N)(N-2q)Lambda(q)<=0,                 (9.1)
```

equivalently (1.12).  If eventually true, then (1.11) and Chebyshev give
(1.13), and R96 proves RH.  This explains both the strength of the
numerical pattern and the standard required for accepting it.

The exact probes found:

```text
N       floor(sqrt N)     log P_(N,M)       E_(N,M)

64             8          -487.619          361.601
100           10          -488.643          694.089
256           16         -3069.729         3222.195
1000          31        -31742.978        30779.293
5000          70       -337557.824       328030.589.       (9.2)
```

A separate sieve scan found no positive value in (9.1) for
`4<=N<=20,000,000`.  These floating computations are not used in any proof.
The exact finite tests instead certify (1.5), (4.4), (1.8), the mixed tail
signs, and the non-total-unimodularity minor.

[R101](R101-LITTLEWOOD-RAMP-SIGN-KILL.md) proves that (9.1) is false
infinitely often, not merely unsupported.  Its argument is an exhaustive
dichotomy.  If RH is false, the contrapositive of the R96 Landau theorem at
some `1/2<a<Re(rho)` gives both `R=Omega_+(x^a)` and
`R=Omega_-(x^a)`.  If RH is true, the exact
first-Riesz explicit formula gives

```text
integral_1^x D(t)dt=O(x^(3/2)),
R(x)=psi(x)-x+O(sqrt(x)),                             (9.3)
```

so the classical Hardy--Littlewood theorem transfers its two-sided
`sqrt(x)log log log x` oscillation from `psi(x)-x` to `R(x)`.  On a unit
interval, `R(x)-R(floor(x))=O(1)`, so the same result holds at integers.
Finally, (1.11) and `E_(N,floor(sqrt(N)))=O(N^(3/2))` give

```text
log P_(N,floor(sqrt(N)))
 =Omega_+ (N^(3/2)log log log N)
  and Omega_- (N^(3/2)log log log N).                (9.4)
```

Hence `P_(N,floor(sqrt(N)))>1` and `<1` each occur infinitely often.
The delayed first sign change is not bounded by this qualitative argument
and may lie far beyond the finite scan.

The structural obstructions remain useful explanations: `P_(N,M)` and its
reciprocal each have negative prime valuations on different macroscopic
prime intervals, so neither is an integer; the first majorization tails
have both signs uniformly and the second tails already have both signs in
the exact `N=100` audit; and its exponent formula is governed by Mertens
sums.

## 10. Disposition

The arithmetic-integrality route reaches a precise boundary.

```text
unsigned integer multiplier      necessarily exp(Theta(N^2))
canonical factorial certificate  exact, but quadratic
signed factorial/Barnes ratio    can cancel every chosen layer
sqrt-cutoff residual             exact O(N^(3/2)) integer
size of cancelling ratio         complementary ramp; both signs infinitely often
Möbius-inverted coefficients     signed Mertens sums
LP integrality shortcut          no total-unimodularity.                 (10.1)
```

The new reusable results are Theorems 2.1, 3.1, 4.1, and the exact
cutoff certificate (1.8).  They show that the requested small residual is
arithmetically possible, but not analytically sufficient.  R101 closes the
explicit square-root sign conjecture (9.1) negatively.  Continuing the
route now requires a genuinely weaker fixed-power one-sided estimate with
some exponent `a>1/2`; such an estimate is still a direct fixed-strip
criterion, not a consequence of factorial integrality alone.  R99 and R101
prove neither a fixed zero-free strip nor failure of every fixed strip.
