# R96 one-sided von Mangoldt ramp gate

Status: exact sign and transform audit of the R95 ramp, exact lcm and
complementary-sum forms, removal of higher prime powers at square-root cost,
a Landau-hypothesis verification, bounded-filter and variable-scale
barriers, and an exact Selberg/Riccati obstruction.  No one-sided fixed-power
bound is proved.  The target remains sufficient for a fixed strip, but
Chebyshev positivity, convexity, scale averaging, and the standard Selberg
identity do not supply it without a new prime-specific correlation estimate.

Date: 2026-08-07.

## 1. Verdict

Put

```text
R(x)
 =sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1),       x>=1.       (1.1)
```

R95 proved that either one-sided estimate

```text
R(x)>=-C x^a                                               (1.2)
```

or

```text
R(x)<= C x^a,                    a<1,                      (1.3)
```

would prove that `zeta(s)` is zero-free in `Re(s)>a`.  This report checks
that reduction carefully and attacks (1.2)--(1.3) from four arithmetic
directions.

The conclusions are:

1. All signs in the Landau reduction are correct.  The ramp transform is

   ```text
   [(s-1)/(s+1)](1/s)
   [-zeta'(s)/zeta(s)-1/(s-1)],                           (1.4)
   ```

   which is analytic at every positive real point and has a pole at every
   nontrivial zeta zero.  The ramp is locally integrable and of finite
   exponential order, so Landau's theorem applies exactly as stated.

2. Higher prime powers contribute only

   ```text
   O(sqrt(x)log x).                                       (1.5)
   ```

   Therefore any proposed strip with right boundary strictly above `1/2`
   may work with primes only.  The hard term is already

   ```text
   sum_(p<=x)log(p)(2p/x-1).                              (1.6)
   ```

3. At an integer `N`, the ramp is exactly a complementary upper/lower-half
   imbalance and exactly an lcm barycenter derivative:

   ```text
   sum_(n<=N)Lambda(n)(2n/N-1)
    =Lambda(N)
     +sum_(1<=m<N/2)(1-2m/N)[Lambda(N-m)-Lambda(m)],       (1.7)

   N R(N)
    =log { L_N^N / product_(m=1)^(N-1)L_m^2 }-N+1,
   L_m=lcm(1,...,m).                                      (1.8)
   ```

   Neither form has a hidden sign.  In (1.7), a termwise positive matching
   asks for complementary prime information of Goldbach/sieve-parity type.
   In (1.8), the displayed ratio is generally a rational number with large
   prime valuations of both signs.

4. Monotonicity of `psi`, convexity of its integral, Chebyshev bounds, and
   a standard PNT remainder all stop at their input exponent.  A positive
   atomic integer-supported countermodel has the exact linear main term and
   off-line Mellin poles, so positivity, atomicity, and the one-sign-change
   kernel alone cannot prove (1.2) or (1.3).

5. Making the signed kernel increasingly one-sided creates an apparent
   trivial power bound, but suppresses a putative zero mode by exactly the
   corresponding power.  This closes a dangerous variable-filter false
   proof.

6. Selberg's positive coefficient identity becomes, after exact centering,

   ```text
   F(s)^2-F'(s)+2F(s)/(s-1),                              (1.9)
   F=-zeta'/zeta-1/(s-1).                                 (1.10)
   ```

   The physical quadratic term is an indefinite centered convolution.
   Inverting the Riccati equation contains `1/zeta(s)^2`.  Applying the ramp
   does not give that quadratic term a sign.

Thus no fixed strip follows.  The remaining theorem is sharply
coefficient-specific: control one side of a weighted imbalance between
actual von Mangoldt mass below and above `x/2`, without estimating the two
positive halves separately.

## 2. Exact ramp identities and signs

Let

```text
psi(x)=sum_(n<=x)Lambda(n),
A(x)=sum_(n<=x)n Lambda(n),
Psi_1(x)=integral_1^x psi(y)dy.                            (2.1)
```

Stieltjes summation gives

```text
Psi_1(x)=sum_(n<=x)Lambda(n)(x-n),                        (2.2)

A(x)=x psi(x)-Psi_1(x).                                  (2.3)
```

Consequently the prime part of the ramp has the equivalent forms

```text
S(x):=R(x)+1-x^(-1)
 =2A(x)/x-psi(x)
 =psi(x)-2Psi_1(x)/x.                                    (2.4)
```

Let

```text
D(x)=psi(x)-(x-1).                                        (2.5)
```

The continuum term cancels exactly:

```text
R(x)=D(x)-(2/x)integral_1^x D(y)dy.                       (2.6)
```

Thus no main term has been hidden in (1.1).

There is a useful differential form.  Away from prime-power jumps,

```text
d/dx [Psi_1(x)/x^2]
 =S(x)/x^2.                                               (2.7)
```

Since `psi` is nondecreasing, `Psi_1` is convex.  But convexity of
`Psi_1` does not determine the sign of the derivative in (2.7) after the
quadratic normalization.

Between consecutive prime powers, `A(x)` and `psi(x)` are constant and

```text
R'(x)=-2A(x)/x^2-x^(-2)<0.                                (2.8)
```

At a prime power `q`, the jump is

```text
R(q+)-R(q-)=Lambda(q).                                    (2.9)
```

The ramp is therefore a downward drift with positive arithmetic jumps.  A
prime-gap theorem bounds the drop during one empty gap, but not the baseline
accumulated over all earlier gaps.  That baseline is the global queue.

## 3. Full Landau audit

This section verifies that the one-sided implication does not conceal an
endpoint or convergence assumption.

On logarithmic scale put

```text
mathcal R(U)=R(exp(U)).                                    (3.1)
```

For `Re(s)>1`, R95 gives

```text
integral_0^infinity mathcal R(U)exp(-sU)dU
 =[(s-1)/(s(s+1))]
  [-zeta'(s)/zeta(s)-1/(s-1)].                            (3.2)
```

The identity can also be checked directly from (2.6).  The Volterra
high-pass has multiplier `(s-1)/(s+1)`, and integration of a cumulative
measure contributes `1/s`.

For a termwise sign check,

```text
integral_(log n)^infinity exp(-sU)(2n exp(-U)-1)dU
 =[(s-1)/(s(s+1))]n^(-s),                                (3.2a)

integral_0^infinity exp(-sU)(-1+exp(-U))dU
 =-1/[s(s+1)].                                            (3.2b)
```

Together these are exactly (3.2).

### 3.1 Analyticity on the positive real axis

For `0<s<1`, the alternating eta representation gives

```text
zeta(s)=eta(s)/(1-2^(1-s))<0.                             (3.3)
```

In particular zeta has no real zero there.  At `s=1`,

```text
-zeta'(s)/zeta(s)-1/(s-1)                                (3.4)
```

has a removable singularity.  The rational prefactor in (3.2) introduces
no positive real pole.  Hence the meromorphic continuation of (3.2) is
analytic at every real `s>0`.

At a nontrivial zero `rho`, however,

```text
(rho-1)/(rho(rho+1))!=0,                                  (3.5)
```

so (3.2) has a pole with the zeta multiplicity.

### 3.2 Exponential order

The elementary bound `Lambda(n)<=log n` gives

```text
psi(x)<=x log x,
A(x)<=x psi(x),
abs(R(x))=O(x log x).                                     (3.6)
```

Thus `mathcal R` is locally integrable and of finite exponential order.
Every Laplace abscissa below is finite.

### 3.3 One-sided implication

Assume, for example,

```text
mathcal R(U)>=-C exp(aU),       0<a<1,                    (3.7)
```

eventually.  After changing a compact initial segment,

```text
g(U)=mathcal R(U)+C exp(aU)>=0.                           (3.8)
```

Its Laplace transform is (3.2) plus `C/(s-a)` and an entire function.  If a
zero `rho=beta+i gamma` had `beta>a`, the Laplace abscissa of `g` would be at
least `beta`; otherwise the defining integral would be holomorphic at
`rho`.  Landau's theorem for an eventually nonnegative function forces a
singularity at the *real* convergence abscissa.  But the continued transform
is analytic at every real point larger than `a`, by Section 3.1.  This is a
contradiction.

For an upper bound, apply the same argument to

```text
C exp(aU)-mathcal R(U).                                   (3.9)
```

All hypotheses are now explicit:

```text
eventual nonnegativity       supplied by the one-sided bound
finite exponential order     (3.6)
real-axis analyticity         (3.3)--(3.4)
target pole retention         (3.5)
compact initial correction    entire in Laplace space.    (3.10)
```

The R95 Landau reduction is therefore sound.

## 4. Higher prime powers are not the obstruction

Because the ramp coefficient has modulus at most one,

```text
sum_(p^k<=x, k>=2) log p abs(2p^k/x-1)
 <=sum_(k>=2) theta(x^(1/k)).                             (4.1)
```

Chebyshev's elementary upper bound `theta(y)<<y` gives

```text
sum_(k>=2)theta(x^(1/k))<<sqrt(x)log x.                   (4.2)
```

Hence

```text
R(x)
 =sum_(p<=x)log p(2p/x-1)-1+x^(-1)
  +O(sqrt(x)log x).                                       (4.3)
```

For every proposed exponent `a>1/2`, the error in (4.3) is harmless after
an endpoint epsilon.  The fixed-strip problem in this formulation is
already a signed first moment of the actual primes; prime powers and their
multiplicities are not the bottleneck.

## 5. Complementary halves and the parity wall

At an integer `N`, pair an upper integer `n=N-m` with the lower integer
`m`.  The weights are opposite:

```text
2(N-m)/N-1=1-2m/N.                                       (5.1)
```

The middle weight is zero when `N` is even.  Therefore

**Theorem 5.1 (complementary identity).**

```text
S(N)
 =Lambda(N)
  +sum_(1<=m<N/2)(1-2m/N)[Lambda(N-m)-Lambda(m)].          (5.2)
```

This is exact, including the endpoint `m=0` through `Lambda(N)`.

A termwise sign-reversing injection would have to send lower prime powers
`m` to complementary upper prime powers `N-m`, or combine many such terms
with controlled load.  That is not supplied by the existence of a nearby
prime.  It asks for lower bounds on primes in a prescribed complementary
set, where ordinary lower-bound sieve arguments meet the parity problem.

Estimating the two nonnegative quantities

```text
P_-(N)=sum_(m<N/2)Lambda(m)(1-2m/N),
P_+(N)=Lambda(N)+sum_(m<N/2)Lambda(N-m)(1-2m/N)            (5.3)
```

separately gives `O(N)` and discards the required cancellation.  The target
is precisely one side of

```text
S(N)=P_+(N)-P_-(N).                                       (5.4)
```

Bombieri--Vinogradov or a prime-gap theorem controls different averages;
neither gives a pointwise fixed-power imbalance in (5.4).  Such an
imbalance would already imply the zero-free strip by Section 3.

## 6. The lcm barycenter has no divisibility sign

Let

```text
L_m=lcm(1,2,...,m),             log L_m=psi(m).            (6.1)
```

At an integer `N`, discrete summation gives

```text
A(N)=N psi(N)-sum_(m=1)^(N-1)psi(m).                      (6.2)
```

Combining (2.4) and (6.2) proves

**Theorem 6.1 (lcm ratio identity).**

```text
N R(N)
 =log Q_N-N+1,                                            (6.3)

Q_N=L_N^N / product_(m=1)^(N-1)L_m^2.                    (6.4)
```

This looks like an integrality opportunity, but `Q_N` is generally only a
rational number.  Its exact prime valuation is

```text
v_p(Q_N)=sum_(p^k<=N)(2p^k-N).                            (6.5)
```

### Proof of (6.5)

The exponent of `p` in `L_N^N` is

```text
N #{k:p^k<=N}.                                            (6.6)
```

For a fixed `p^k<=N`, the factor `p` occurs in `L_m` for exactly
`N-p^k` values `1<=m<N`.  Subtracting twice that count gives the summand in
(6.5).  QED.

For every prime `N/2<p<=N`, (6.5) contains the positive valuation

```text
2p-N>0.                                                    (6.7)
```

For a fixed small prime, the number of powers is asymptotic to
`log N/log p`, while their geometric sum is `O(N)`, so

```text
v_p(Q_N)=-N log N/log p+O(N)                              (6.8)
```

along generic large `N`.  Large positive and negative valuations coexist.
Neither `Q_N` nor its reciprocal is forced to be an integer, and a
divisibility lower bound cannot place `log Q_N` within `O(N^(a+1))` of the
specific main value `N-1` required by (6.3).

The convex form (2.7) has the same obstruction in analytic language.
Chebyshev bounds constrain `Psi_1(x)/x^2` to a compact interval, and the PNT
makes it tend to `1/2`; neither statement gives a fixed-power pointwise
bound for its derivative.  Positive monotone countermodels in Section 9
make that failure explicit.

## 7. Scale averaging and the variable-filter false proof

The family from R95 is

```text
w_lambda(y)
 =[lambda y^(lambda-1)-1]/(lambda-1),       0<y<=1,        (7.1)
```

with

```text
integral_0^1 w_lambda(y)dy=0,
-1/(lambda-1)<=w_lambda(y)<=1.                            (7.2)
```

For fixed `lambda`, the Mellin response of a zero mode is

```text
rho integral_0^1 w_lambda(y)y^(rho-1)dy
 =(rho-1)/(rho+lambda-1).                                 (7.3)
```

It is nonzero and Section 3 applies.

There is a tempting but false variable-scale argument.  Let
`lambda=x^kappa`.  Positivity and the lower bound in (7.2) give, using
Chebyshev,

```text
sum_(n<=x)Lambda(n)w_lambda(n/x)
 >=-psi(x)/(lambda-1)
 >=-C x^(1-kappa).                                        (7.4)
```

This appears to be a one-sided fixed power.  But (7.3) simultaneously
suppresses a fixed zero mode by

```text
abs((rho-1)/(rho+lambda-1)) asymp_rho lambda^(-1).         (7.5)
```

Thus a mode `x^rho` becomes `x^(rho-kappa)`.  Comparing its real exponent
with the bound in (7.4) asks for

```text
Re(rho)-kappa>1-kappa,                                    (7.6)
```

which is again only `Re(rho)>1`.  Moreover a filter varying with `x` is not
the Laplace multiplier of one fixed function, so the Landau proof cannot be
applied to it.

The same conservation holds for a broad bounded class.

**Lemma 7.1 (small-negative-part ledger).**  Suppose

```text
-epsilon<=w(y)<=1,
integral_0^1 w(y)dy=0,
0<epsilon<=1.                                             (7.7)
```

Then, for `0<beta<1`,

```text
abs(integral_0^1 w(y)y^(beta+i gamma-1)dy)
 <=2 epsilon^beta/beta.                                   (7.8)
```

### Proof

The positive and negative masses of `w` are equal and at most `epsilon`.
Among functions bounded by one with mass at most `epsilon`, the decreasing
weight `y^(beta-1)` is maximized by the indicator of `(0,epsilon)`, giving
`epsilon^beta/beta`.  The negative part is bounded by
`epsilon integral_0^1 y^(beta-1)dy=epsilon/beta`, which is no larger than
`epsilon^beta/beta`.  Adding the two bounds proves (7.8).  QED.

Shrinking the negative coefficient enough for a trivial power bound also
shrinks every off-line Mellin response.  Unbounded positive
superoscillatory weights fall outside Lemma 7.1, but then their conditioning
must be paid; that branch is the R91--R92 superoscillation gate, not a free
one-sided estimate for (1.1).

A fixed positive average of scales has the opposite issue.  It multiplies
(3.2) by a fixed zero-free smoothing factor and retains every pole, so a
one-sided power bound for the average is still a strip theorem.  Standard
scale averaging gives an upper mean estimate, not the pointwise signed
orientation required by Landau.

## 8. Selberg positivity becomes an indefinite centered Riccati equation

Let

```text
A(s)=-zeta'(s)/zeta(s)=sum_n Lambda(n)n^(-s),              (8.1)

F(s)=A(s)-1/(s-1).                                        (8.2)
```

Selberg's positive coefficients are

```text
b(n)=Lambda(n)log n+(Lambda*Lambda)(n)>=0,                 (8.3)

sum_n b(n)n^(-s)=A(s)^2-A'(s).                            (8.4)
```

Substituting (8.2) gives the exact centered identity

```text
A(s)^2-A'(s)-2/(s-1)^2
 =F(s)^2-F'(s)+2F(s)/(s-1).                               (8.5)
```

On the logarithmic measure side, if

```text
nu=M-P,                                                    (8.6)
```

then (8.5) is the transform of

```text
u nu+2(P*nu)+nu*nu.                                       (8.7)
```

The uncentered coefficients in (8.3) are positive, but the last term in
(8.7) is a signed convolution.  Applying the one-sign-change ramp to (8.7)
does not make it positive.  For example, with

```text
nu=delta_a-delta_b,        a<b,                            (8.8)
```

one has

```text
nu*nu=delta_(2a)-2delta_(a+b)+delta_(2b).                 (8.9)
```

A translated ramp or compact test centered near `a+b` sees the negative
cross atom; changing the relative sign in (8.8) makes it positive.  Finite
moment corrections do not change this two-block signature.

The transform inversion is equally explicit.  Put

```text
Y(s)=(s-1)zeta(s),
F(s)=-Y'(s)/Y(s).                                         (8.10)
```

Then (8.5) is a Riccati equation.  Linearizing its right side at `F` sends a
perturbation `h` to

```text
-h'(s)+2A(s)h(s).                                         (8.11)
```

Solving for `h` uses the integrating factor `zeta(s)^2`:

```text
h(s)
 =zeta(s)^(-2)
  integral_s^infinity zeta(u)^2 q(u)du,                   (8.12)
```

up to the sign convention for the forcing `q` and with the decaying
boundary condition on a rightward horizontal ray.  The condition operator
contains `1/zeta^2`.  Consequently the standard Selberg remainder does not
invert to a one-sided bound for `F`, and hence not for `R`, without already
controlling the zeros.

The R95 positive oscillatory countermodel also passes the generic size of
(8.7): the mixed pole term is `O(exp(U))`, while the pure discrepancy terms
are `O((1+U)exp(beta U))` for every `beta<1`.  Thus the usual
`O((1+U)exp(U))` Selberg scale cannot orient the ramp.

## 9. Positive atomic countermodels

It is useful to separate actual-prime structure from generic positivity and
atomicity.  Fix

```text
0<beta<1,
gamma!=0,
0<epsilon<1.                                              (9.1)
```

Define nonnegative integer weights

```text
a_n=1+epsilon n^(beta-1)cos(gamma log n)>0.                (9.2)
```

Their Dirichlet series is exactly

```text
sum_(n>=1)a_n n^(-s)
 =zeta(s)
  +(epsilon/2)zeta(s+1-beta-i gamma)
  +(epsilon/2)zeta(s+1-beta+i gamma).                     (9.3)
```

It has the ordinary main pole at `s=1` and additional poles at

```text
s=beta+i gamma,
s=beta-i gamma.                                           (9.4)
```

The cumulative mass is

```text
sum_(n<=x)a_n
 =x+Re(c_(beta,gamma) x^(beta+i gamma))+O(1+x^(beta-1)),  (9.5)
```

with a nonzero constant `c_(beta,gamma)`.  Applying the ramp multiplies the
two off-line residues by the nonzero factor `(s-1)/(s+1)`, so its ramp has
positive and negative excursions of order `x^beta`.

This model is:

```text
positive                         yes
atomic on the integers           yes
linear cumulative main term      yes
monotone cumulative function     yes
convex integrated cumulative     yes
flat scale identities            yes
one-sided fixed power < beta     no.                      (9.6)
```

It is not the von Mangoldt sequence and does not satisfy the exact Selberg
coefficient identity (8.3).  That is precisely the point: any successful
argument must use more than positivity, atomic support, convexity, and scale
algebra.  Section 8 shows why importing only the usual size consequence of
Selberg's identity still does not suffice.

There is also a continuous version with

```text
psi_model(x)=x+epsilon x^beta cos(gamma log x)             (9.7)
```

after a compact cutoff.  Its derivative is positive for sufficiently small
`epsilon`, while its ramp again has size `x^beta` on both sides.  This
directly falsifies any convexity or monotonicity theorem claimed to prove a
fixed power.

## 10. What remains

No estimate in this audit improves the imported Vinogradov--Korobov shape

```text
R(x)<<x exp(-c(log x)^(3/5)(log log x)^(-1/5))             (10.1)
```

to a fixed power.  The report instead narrows the missing arithmetic input.

For any fixed `a` with `1/2<a<1`, it is enough to prove one of

```text
sum_(p<=x)log p(2p/x-1)>=-C_a x^a,                        (10.2)
```

or

```text
sum_(p<=x)log p(2p/x-1)<= C_a x^a,                        (10.3)
```

because (4.3) restores prime powers and Section 3 invokes Landau.  This is a
one-sided signed comparison between the prime mass and barycenter in the
two halves of `[1,x]`.

The following approaches are now sharply separated:

```text
Chebyshev/convexity only          positive atomic countermodel defeats
termwise complementary pairing  Goldbach/parity-strength lower problem
lcm divisibility                 ratio has valuations of both signs
fixed scale smoothing            preserves every target pole
variable one-sided smoothing     suppresses target by the same power
Selberg coefficient positivity   centered convolution is indefinite
Selberg inversion                contains 1/zeta^2.                         (10.4)
```

A survivor must prove a new *joint* inequality for the actual primes in the
upper and lower halves before absolute values.  Equivalently, it must orient
one side of the prime barycenter error.  No fixed zero-free strip and no
sequence of zeros approaching one is proved here.
