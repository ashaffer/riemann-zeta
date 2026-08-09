# Difference-moment quadrature, the initial prime-log gap, and the arithmetic-alias gate

Status: R99 proves that positive quadrature on prime-power logarithms cannot
force pole dominance through arbitrarily high polynomial degree.  The reason
is simpler and stronger than the circular Farkas formulation in R90: every
prime-power logarithm is at least `log 2`, while the pole-minus-target
difference measure has support down to zero.  A truncated localizing matrix
detects this support mismatch at an explicit degree.  More strongly, for
every fixed pair `delta,e>0` and every requested reserve `0<theta<1`, there
is a finite derivative polynomial `W`, with `W(0)=0` and `W>=0` on the whole
interval `[log 2,infinity)`, such that

```text
0 < H_W(delta) < theta H_W(delta+e).                         (1.1)
```

Thus the first, pole-versus-target line of R90 Theorem 10.1 is algebraically
solvable with an arbitrary fixed reserve.  It is not the remaining obstacle.
No estimate of the complete signed zero remainder follows from this
construction.

The infinite-order stress test

```text
A(x)=cos(2 pi exp(x))-1                                      (1.2)
```

vanishes at every integer logarithm, hence at every prime-power logarithm,
and also satisfies `A(0)=0`.  Nevertheless its continuous Laplace transform
is nonzero.  Stationary phase gives only

```text
H_A(u+iv) asyp |v|^(-u-1/2)                                 (1.3)
```

on the relevant vertical rays.  It therefore does not define a free
infinite differentiated operator: either its spectral sum is not absolutely
available, or a correctly regularized explicit formula makes its entire pole
signal cancel as a spectral null identity.

```text
positive prime-log quadrature for all degrees              IMPOSSIBLE
support-floor obstruction                                  EXACT
explicit growing-degree bound                              EXACT
W(0)=0 derivative constraint                               PRESERVED
positive target plus fixed pole reserve                    EXISTS
coefficient/norm control uniform as e -> 0                 FAILS
bounded infinite-order arithmetic alias                    SPECTRAL NULL
complete signed remainder estimate                         OPEN
fixed zero-free strip                                      NOT PROVED.    (1.4)
```

## 2. The exact difference measure

Put

```text
a=log 2,
S={log(p^k): p prime, k>=1},
nu_(delta,e)(dx)=exp(-delta x)(1-exp(-e x))dx.               (2.1)
```

Then `S` is contained in `[a,infinity)`, and for every polynomial `W`,

```text
H_W(delta)-H_W(delta+e)
 =integral_0^infinity W(x)nu_(delta,e)(dx).                  (2.2)
```

The moments are explicit:

```text
mu_k
 :=integral x^k nu_(delta,e)(dx)
 =k![delta^(-k-1)-(delta+e)^(-k-1)].                         (2.3)
```

More generally, after imposing a zero of order `r` at the origin, define

```text
nu_r(dx)=x^r nu_(delta,e)(dx),

mu_k^(r)
 =(r+k)![delta^(-r-k-1)-(delta+e)^(-r-k-1)].                 (2.4)
```

This is the derivative-weighted version of the same moment problem.

Suppose positive atoms `omega_j` on nodes `s_j in S` represented the first
`M` moments:

```text
mu_k=sum_j omega_j s_j^k,             0<=k<=M.               (2.5)
```

Then every degree-`M` polynomial nonnegative on the chosen nodes would obey

```text
integral W dnu=sum_j omega_jW(s_j)>=0.                       (2.6)
```

R90 observed that asking for (2.5) in general is Farkas-dual to asking for
a separator and is therefore circular.  Here the missing support interval
`(0,a)` supplies an explicit localizing separator and makes the argument
noncircular.

## 3. Degree one is completely decidable

The normalized first moment of `nu=nu_0` is

```text
mu_1/mu_0=1/delta+1/(delta+e).                               (3.1)
```

### Proposition 3.1 (exact first-moment criterion)

Positive atoms on `S` represent `mu_0,mu_1` if and only if

```text
1/delta+1/(delta+e)>=log 2.                                  (3.2)
```

#### Proof

Necessity follows because every node is at least `a`.  Conversely, the
convex hull of `S` is `[a,infinity)`: `a=log 2` is in `S`, `S` is unbounded,
and any point between two nodes is a convex combination of those nodes.
Multiply a two-node probability representation of the mean by `mu_0`.

For the R90 example `delta=60,e=1`, the mean is

```text
1/60+1/61=0.0330601... < log 2.                              (3.3)
```

Thus positive prime-log quadrature already fails at degree one there.  This
explains why a low-degree counterexample is available in that regime without
invoking the fine prime mesh.

For `nu_r`, the corresponding mean is

```text
(r+1)/delta
 *[1-(delta/(delta+e))^(r+2)]
  /[1-(delta/(delta+e))^(r+1)].                              (3.4)
```

It moves away from zero as `r` grows, which is why a growing derivative
order delays detection of the missing interval.

## 4. The localizing eigenvalue

For integers `r,n>=0`, define

```text
lambda_(n,r)
 :=inf_(0!=q, deg q<=n)
       [integral x q(x)^2 nu_r(dx)]
       /[integral q(x)^2 nu_r(dx)].                          (4.1)
```

This is the smallest generalized eigenvalue of the two Hankel matrices

```text
G_n=(mu_(i+j)^(r))_(0<=i,j<=n),
X_n=(mu_(i+j+1)^(r))_(0<=i,j<=n).                            (4.2)
```

Equivalently, it is the smallest zero of the degree-`n+1` orthogonal
polynomial for `nu_r`.  The infimum is attained because `G_n` is positive
definite.

### Theorem 4.1 (explicit support-floor detection)

Let

```text
c_0=1-exp(-1),
B_(n,r)=(r+2)(r+3)/[delta(n+r+3)].                            (4.3)
```

If `e B_(n,r)<1`, then

```text
lambda_(n,r)
 <=B_(n,r)/[c_0(1-e B_(n,r))].                               (4.4)
```

In particular, `lambda_(n,r)<a` once the right side of (4.4) is below
`log 2`.  A convenient sufficient condition is

```text
n+r+3
 >[(r+2)(r+3)/delta]
   max(2e, 2/[c_0 log 2]).                                   (4.5)
```

Hence, for every fixed `r,delta,e`,

```text
lambda_(n,r)=O_(r,delta,e)(1/n) ->0.                         (4.6)
```

#### Proof

Compare `nu_r` with the gamma measure

```text
gamma_r(dx)=e x^(r+1)exp(-delta x)dx.                         (4.7)
```

Their density ratio is

```text
h(x)=(1-exp(-e x))/(e x),

0<h(x)<=1,
h(x)>=c_0                  for 0<=x<=1/e.                    (4.8)
```

The minimum multiplication-by-`x` quotient over degree `n` for `gamma_r`
is the smallest zero, divided by `delta`, of

```text
L_(n+1)^(r+1).                                                (4.9)
```

The classical Laguerre extreme-zero bound

```text
x_min(L_(n+1)^alpha)
 <(alpha+1)(alpha+2)/(n+alpha+2)                             (4.10)
```

therefore gives a gamma quotient `R<=B_(n,r)`.  Formula (4.10)
is recorded explicitly in K. Driver and K. Jordaan,
[*Bounds for extreme zeros of some classical orthogonal polynomials*](https://arxiv.org/abs/1111.1218),
equation (5).

Let `q` be the gamma minimizer and let `D=integral q^2 dgamma_r`.
Markov's inequality in its elementary integral form gives

```text
integral_(1/e)^infinity q^2 dgamma_r
 <=e integral xq^2 dgamma_r
 =eRD.                                                       (4.11)
```

Using (4.8),

```text
integral q^2 dnu_r>=c_0(1-eR)D,
integral xq^2 dnu_r<=RD.                                    (4.12)
```

Consequently

```text
lambda_(n,r)<=R/[c_0(1-eR)]
             <=B_(n,r)/[c_0(1-eB_(n,r))],                   (4.13)
```

which is (4.4).  Condition (4.5) makes `eB<1/2` and
`2B/c_0<log 2`.

### Corollary 4.2 (explicit polynomial separator)

If `lambda_(n,r)<a`, choose a minimizing `q` and put

```text
W_(n,r)(x)=x^r(x-a)q(x)^2.                                  (4.14)
```

Then

```text
W_(n,r)(x)>=0                  for every x>=a,
deg W_(n,r)<=r+2n+1,

H_W(delta)-H_W(delta+e)
 =integral (x-a)q(x)^2 nu_r(dx)<0.                           (4.15)
```

For `r>=1`, this separator also has the required derivative normalization
`W(0)=0`.  Therefore no positive atomic measure on `S` can represent the
moments through degree `r+2n+1`.

For `delta=e=1,r=1`, direct high-precision diagonalization gives

```text
n       lambda_(n,1)
0       2.33333333333
4       0.830017201464
5       0.722396454736
6       0.640467595501 < log 2.                              (4.16)
```

Thus a degree-`14` separator already detects the support gap.  The explicit
comparison bound (4.4) is deliberately conservative; it certifies the same
conclusion without relying on the numerical eigenvalue.

## 5. Why the first separator is not yet useful

The localizing separator (4.14) is negative throughout `(0,a)`.  In the
examples tested, this makes both transforms negative:

```text
delta=e=1, r=1, n=6:

H_W(1)=-0.6426697188,
H_W(2)=-0.5899901337.                                       (5.1)
```

It reverses the order but does not give the positive target response
`A=H_W(delta+e)>0` required by R90 Theorem 10.1.  Positive quadrature failure
alone therefore does not solve the pole gate.

The sign problem can, however, be repaired exactly at the existence level.

## 6. A universal finite-polynomial pole reversal

### Theorem 6.1 (arbitrary fixed reserve below the first prime log)

Fix `delta,e>0`, `a>0`, and `0<theta<1`.  There is a real polynomial `W`
such that

```text
W(0)=0,
W(x)>=0                         for every x>=a,
0<H_W(delta)<theta H_W(delta+e).                             (6.1)
```

For `a=log 2`, this is an admissible finite differentiated prime weight and
is nonnegative at every prime power.

#### Proof

Choose

```text
0<x_0<b<x_1<a,
f(x)=x(x-b)(x-a).                                            (6.2)
```

Then `f(x_0)=F_0>0`, `f(x_1)=-F_1<0`, and `f>=0` on
`[a,infinity)`.  Let `0<q_0<theta`, and set

```text
kappa
 =F_0[exp(e x_0)-q_0]
  /{F_1[exp(e x_1)-q_0]}.                                   (6.3)
```

Consider first the ideal target-weighted two-point mass having masses `1`
at `x_0` and `kappa` at `x_1`.  Its target and pole responses after
multiplication by `f` are

```text
A_*=F_0-kappa F_1>0,

P_*=F_0exp(e x_0)-kappa F_1exp(e x_1)
    =q_0 A_*>0.                                              (6.4)
```

The positivity of `A_*` follows from `x_0<x_1` and `q_0<1`.

Replace the two atoms by sufficiently narrow, disjoint compact bumps of a
nonnegative density `g(x)^2 exp(-(delta+e)x)dx`.  By continuity, their
responses still satisfy

```text
A_g>0,             0<P_g<theta A_g.                          (6.5)
```

Polynomials are dense in

```text
L^2(|f(x)|exp(-delta x)dx).                                  (6.6)
```

For completeness, if a function were orthogonal to all polynomials in this
space, its exponentially tilted transform would be analytic near zero and
would have every derivative zero there.  Analytic continuation to the
imaginary axis and uniqueness of the Fourier transform force the function
to vanish.  Thus choose polynomials `p_m` converging to `g` in (6.6).

Since

```text
integral |f||p_m^2-g^2|exp(-delta x)dx ->0,                  (6.7)
```

both the pole and target responses converge.  For all sufficiently large
`m`,

```text
W_m(x)=f(x)p_m(x)^2                                          (6.8)
```

satisfies (6.1).  It is a finite polynomial, has zero constant term, and is
nonnegative on `[a,infinity)`.

### Consequence 6.2

For every prescribed `theta<1`, the first inequality in R90 (10.3),

```text
H_W(delta)<=theta H_W(delta+e),                              (6.9)
```

can be met by a finite derivative polynomial with a positive target
response.  This is not just the isolated cubic of R90 Section 3.  The
initial gap `(0,log 2)` makes the pole half of the criterion universally
feasible.

The proof is existential and gives no useful degree or coefficient norm.
That omission is substantive, especially as `e` tends to zero.

## 7. The unavoidable low-gap condition number

The universal construction becomes singular when the pole and target
measures become close.

### Proposition 7.1 (fixed reserve costs `1/e` target variation)

Suppose `W>=0` on `[a,infinity)`,

```text
A=H_W(delta+e)>0,
0<=H_W(delta)<=theta A,              0<=theta<1.             (7.1)
```

Let

```text
N=integral W_-(x)exp(-(delta+e)x)dx.                          (7.2)
```

Then

```text
N/A >=(1-theta)/(exp(ea)-1).                                 (7.3)
```

#### Proof

The negative support lies in `(0,a)`.  Hence

```text
A-H_W(delta)
 =-integral W(x)exp(-(delta+e)x)(exp(ex)-1)dx

 <=[exp(ea)-1]N.                                             (7.4)
```

The left side is at least `(1-theta)A`.

Thus a fixed reserve normalized by `A=1` has negative target mass at least

```text
(1-theta)/(ea)(1+O(ea))                                     (7.5)
```

as `e->0`.  The total-variation condition number is at least
`1+2N/A`.  The two-bump proof realizes the same qualitative blow-up: its
positive and negative target masses nearly cancel when `e` is small.

This cost is only logarithmic at the classical scale `e asyp 1/log T`, not
the power cost of a high prime-log gap.  But a low-gap kernel has no native
`1/log T` vertical resolution.  If its weighted first moment is controlled,

```text
|H_W(u+i(v+h))-H_W(u+iv)|
 <=|h| integral x|W(x)|exp(-ux)dx.                           (7.6)
```

It therefore sees the entire local zero cloud almost identically.  Making
the polynomial tail at `x asyp log T` do the resolving returns to the
prime-mesh/superoscillation gate of R90.

## 8. What a growing derivative order does

The explicit bound (4.3) is

```text
B_(n,r) asyp r^2/[delta(n+r)]                                (8.1)
```

when `r` grows.  For fixed `r`, degree eventually detects the interval
`(0,a)` at the sharp qualitative rate `O(1/n)`.  The sufficient uniform
regime is

```text
n >> r^2/(delta a).                                          (8.2)
```

If the baseline derivative order is comparable to the available polynomial
modulation degree, this localizing proof no longer forces a separator.  That
does not establish positive quadrature; it records the honest limit of the
support-floor argument.  A growing gamma/derivative weight shifts most mass
away from zero, and detecting its tiny hard-edge component needs a degree
quadratic in the derivative order.

This agrees with, rather than evades, the R89 pole-resolution tradeoff.
Using large derivative order to localize vertically attenuates the target
relative to the pole; using still larger modulation degree to recover the
missing interval creates the same coefficient and remainder problem.

## 9. The bounded infinite-order alias

Define

```text
A(x)=cos(2 pi exp(x))-1.                                     (9.1)
```

For every integer `m>=1`,

```text
A(log m)=cos(2 pi m)-1=0,                                   (9.2)
```

and `A(0)=0`.  Therefore its sampled prime Dirichlet series is identically
zero:

```text
sum_(n>=2)Lambda(n)A(log n)n^(-s)=0,        Re s>1.           (9.3)
```

On the other hand, its Laplace transform is not zero.  Substitution
`u=exp(x)` gives, for `Re z>0`,

```text
H_A(z)
 =integral_1^infinity u^(-z-1)[cos(2 pi u)-1]du

 ={E_(z+1)(-2 pi i)+E_(z+1)(2 pi i)}/2-1/z,                 (9.4)
```

where `E_p` is the generalized exponential integral.  Since

```text
A(x)=-2 pi^2 x^2+O(x^3)              as x->0,                (9.5)
```

Watson's lemma gives

```text
H_A(z)=-4 pi^2/z^3+O(z^-4)            on the positive ray.   (9.6)
```

Thus continuous Laplace response is not determined by the arithmetic
samples once infinite-order functions are admitted.

### Proposition 9.1 (stationary-phase tail)

For fixed `u>0` and `v->+infinity`,

```text
H_A(u+iv)
 =1/2 (v/(2 pi))^(-u-1/2)
   exp{i[v-v log(v/(2 pi))+pi/4]}

  +O_u(v^(-u-3/2)+v^-3).                                   (9.7)
```

#### Proof sketch

In the positive-frequency half of the cosine, the phase is

```text
phi(x)=2 pi exp(x)-vx.                                      (9.8)
```

It has the unique stationary point

```text
x_0=log(v/(2 pi)),       phi''(x_0)=v.                       (9.9)
```

The amplitude there is `exp(-u x_0)`, and the Gaussian stationary-phase
factor is `sqrt(2 pi/v)`.  Including the cosine factor `1/2` yields (9.7).
The negative-frequency branch has no stationary point.  The subtraction of
`1` cancels the endpoint terms through first order because `A(0)=A'(0)=0`,
leaving an `O(v^-3)` endpoint contribution.

The numerical probe at `v=100` gives

```text
u       |H_A(u+100i)|       stationary envelope       ratio
0.25    0.0627480792        0.0627487250              0.999990
2       0.0004967931        0.0004947886              1.00405. (9.10)
```

### Consequence 9.2 (no free functional calculus)

For spectral arguments whose smallest horizontal real part is `u<=1/2`,
the absolute zero sum suggested by (9.7) diverges against zero density
`asyp log |v|`.  Even where an explicit formula can be justified by
conditional summation or by moving farther right, (9.3) forces its complete
spectral side to be exactly a null relation: the pole response in (9.4) is
canceled by the zeros, trivial zeros, and any archimedean/boundary terms.

Adding a multiple of `A` to a continuous interpolant changes its Laplace
pole and target responses without changing a single prime coefficient.  It
cannot therefore improve R90 Theorem 10.1 unless the corresponding complete
spectral null vector is retained.  Taylor truncation does not repair this:
`A` has infinite order, and its truncations do not converge with a common
majorant on all integer logarithms or in the spectral sum.

This is the precise analytic-continuation anomaly requested in the R99
stress test.  It is not evidence for a strip; it is a diagnostic showing
that prime-sample interpolation and continuous Laplace functional calculus
cease to be faithful at infinite order.

## 10. Reproducible probes

The implementation is in

```text
src/r99_difference_moment_probe.py
src/test_r99_difference_moment_probe.py
```

It provides:

1. exact moments (2.3)--(2.4);
2. high-precision Cholesky solution of the localizing eigenproblem (4.2);
3. the explicit Laguerre comparison bound (4.4);
4. construction of the derivative-safe separator (4.14);
5. exact polynomial Laplace transforms;
6. the generalized-exponential-integral formula (9.4); and
7. a numerical stationary-phase audit.

The focused test run is

```text
PYTHONPATH=src python3 -m unittest \
  src.test_r99_difference_moment_probe -v

Ran 9 tests
OK                                                              (10.1)
```

The tests also preserve the sign reality check (5.1) and reproduce the R90
cubic with positive target response.

## 11. Decision

The positive-quadrature proposal is decisively resolved.

1. A positive difference-moment quadrature on prime logs cannot survive to
   all degrees.  The initial support gap kills it by an explicit localizing
   polynomial; no Farkas assumption or prime-gap estimate is needed.
2. Requiring `W(0)=0` does not save quadrature.  Multiplying the localizer by
   `x^r` gives a finite differentiated separator with an explicit degree
   threshold.
3. The raw localizer has a negative target response, but this is not a real
   obstruction.  A two-bump construction proves that finite polynomials can
   achieve an arbitrary fixed positive pole reserve for every `delta,e>0`.
4. Therefore the pole half of R90 Theorem 10.1 is no longer an open
   existential question.  The only unresolved inequality is the signed
   estimate for `E_0+E_1` after the weight has been normalized.
5. As `e->0`, every low-gap fixed-reserve construction has target variation
   at least of order `1/e`.  It also lacks vertical resolution unless it
   activates a high, prime-mesh-controlled tail.
6. The off-wall bounded alias is an exact arithmetic null function, not a
   cancellation gift.  Its slow stationary-phase tail or its complete
   spectral null relation returns every apparent Laplace gain.

The honest survivor is consequently narrower than in R90:

```text
finite W with prime positivity and fixed pole reserve        EXISTS

plus a target-conditioned estimate
|E_0(W)+E_1(W;T,rho_0)| <= r H_W(delta+e),
theta+r<1,
uniform despite the low-gap 1/e condition number
and any high-scale resolving tail                            OPEN.          (11.1)
```

R99 proves neither that a fixed zero-free strip exists nor that none exists.
It does prove that positive quadrature cannot close the argument, while the
desired pole cancellation itself is genuinely achievable by the allowed
finite coefficient-specific weights.  Any next step must attack the full
signed spectral remainder rather than revisit pole dominance.
