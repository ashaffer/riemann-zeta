# Harmonic-center amplification of centered sinh-tent squares

Status: exact completed-form ledger, exact full-carrier retention for the
classical `3+4*cos+cos(2*)` amplifier, and a scoped no-go for positive
trigonometric-polynomial proofs, 2026-08-12.  No sign for the actual zeta
square, zero-free strip, or improved zero bound is proved.

## 1. Verdict

Positive harmonic amplification does **not** dilute the selected zero by
itself.  The classical polynomial

```text
P_*(theta)=3+4*cos(theta)+cos(2*theta)
          =2*(1+cos(theta))^2>=0                    (1.1)
```

gives a positive combination of the squares centered at `0`, `gamma`, and
`2*gamma`, and its response to a matched off-critical quartet is

```text
-8*C_alpha(0)^2+O(sinh(alpha*L)^2/gamma^2).         (1.2)
```

Thus this genuinely retains a full carrier.  The idea stops for two more
structural reasons.

1. In the exact Weil ledger the prime term is **subtracted**, and its weight
   is not merely `P(gamma*log n)`.  It is

   ```text
   C_a(log n)*P(gamma*log n),                       (1.3)
   ```

   where `C_a` is the autocorrelation of the odd sinh tent of width `L`.
   Uniformly in `a>0`,

   ```text
   C_a(u)>0  for 0<=u<=L/3,
   C_a(u)<0  for L/2<=u<L.                          (1.4)
   ```

   Hence a nonnegative phase polynomial leaves a sign-changing prime
   kernel.  Finitely many positive depth blocks have the same obstruction.

2. Every nonzero nonnegative trigonometric polynomial has a positive
   constant coefficient.  For the odd packet this zero-frequency square
   couples negatively to the zeta pole pair.  If the hypothetical zero has
   displacement `0<delta<1/2`, the aligned pole response is larger than the
   aligned target response by

   ```text
   exp((1/2-delta)*L)                               (1.5)
   ```

   up to an explicit fixed factor.  This remains true at every fixed packet
   depth.  Positive mixtures cannot cancel the aligned zero-mode pole
   because every odd sinh depth has the same pole sign.  Cancelling that
   term inside the pole ledger with nonzero-center pole tails requires
   `Omega(gamma^2)` coefficient mass and therefore loses the aligned carrier
   by `O(gamma^(-2))` after covariance normalization.  This does not
   preclude coefficient-specific cancellation against prime or
   archimedean terms.

Consequently the implication

```text
nonnegative trigonometric phase polynomial
 + positivity of the von Mangoldt coefficients
 + positive combinations of centered sinh-tent squares
 => a lower sign for the completed Weil square                  (1.6)
```

is false as a proof mechanism.  This is a scoped no-go, not a statement that
the actual coefficient-specific square is negative.  A proof using
cancellation between the two prime ranges in (1.4), a coherently pole-null
packet, or a finite actual-prime interpolation is not ruled out.

All exact formulas below concern the unprojected sharp-lattice sinh-tent
core.  Finite spectral aperture and Hahn endpoint projection change its
autocorrelation.  No sign-zone or pole-ratio transfer to that projected
packet is asserted without a separate estimate.

## 2. Exact packet normalization

Fix `L,a>0`, put `H=L/2`, and define

```text
f_a(x)=sinh(a*x)*1_(|x|<=H),
C_a(u)=integral_R f_a(x)f_a(x+u)dx,
F_a(z)=integral_R f_a(x)exp(i*z*x)dx,
K_a(z)=F_a(z)F_a(-z).                              (2.1)
```

Then `F_a` is odd, `K_a` is even, and

```text
K_a(t)=|F_a(t)|^2>=0                 (t real),
K_a(i*b)=-A_a(b)^2                   (b>0),          (2.2)

A_a(b)=2*integral_0^H sinh(a*x)sinh(b*x)dx
      =sinh((a+b)*H)/(a+b)-sinh((a-b)*H)/(a-b).     (2.3)
```

The second quotient in (2.3) is interpreted continuously when `a=b`.  In
particular,

```text
A_a(a)=sinh(a*L)/(2*a)-L/2=C_a(0).                 (2.4)
```

For `0<=u<=L`, direct integration gives

```text
C_a(u)=sinh(a*(L-u))/(2*a)
       -(L-u)*cosh(a*u)/2,                          (2.5)
```

extended evenly and by zero outside `[-L,L]`.

For a center `c`, take the sum of the cosine- and sine-modulated real
packets `f_a(x)cos(c*x)` and `f_a(x)sin(c*x)`.  This positive covariance has
autocorrelation

```text
C_a(u)*cos(c*u).                                    (2.6)
```

Its exact compact-support Weil ledger is

```text
Q_(a,c)=Pi_(a,c)+Arch_(a,c)
        -2*sum_(n<=exp L) Lambda(n)/sqrt(n)
             *C_a(log n)*cos(c*log n),              (2.7)

Pi_(a,c)=2*Re K_a(c+i/2).                           (2.8)
```

Here `Arch_(a,c)` is the correspondingly translated gamma-factor integral.
Equation (2.8) is exactly the rank-two pole term: at `c=0` it is

```text
Pi_(a,0)=2*K_a(i/2)=-2*A_a(1/2)^2.                 (2.9)
```

This agrees with the repository definition

```text
poleTerm(f)=2*<f,exp(x/2)>*<f,exp(-x/2)>.
```

For the odd packet the two inner products have opposite signs.  In the
continuum-centered multiplier convention of the conditional-Pick reports,
(2.9) is distributed between the rational and continuum terms; their sum
is still exactly (2.9).  The optional `+1` completion adds only the positive
energy term; it does not alter the pole/prime identities or the sign-zone
statements below.

## 3. Exact harmonic ledger

Let

```text
P(theta)=lambda_0+sum_(1<=j<=m)lambda_j*cos(j*theta),
lambda_j>=0,                                        (3.1)
```

and form the positive harmonic combination

```text
Q_(a,P)=sum_(0<=j<=m)lambda_j Q_(a,j*gamma).        (3.2)
```

Linearity in (2.7) gives, with no estimate,

```text
Q_(a,P)=Pi_(a,P)+Arch_(a,P)
        -2*sum_(n<=exp L) Lambda(n)/sqrt(n)
             *C_a(log n)*P(gamma*log n),            (3.3)

Pi_(a,P)=2*sum_(0<=j<=m)lambda_j
                    *Re K_a(j*gamma+i/2).           (3.4)
```

Now suppose `gamma>0` and a hypothetical zero quartet has ordinates
`+/-gamma` and displacements `+/-delta`.  The contribution of the quartet
to the square centered at `j*gamma` is exactly

```text
R_(a,j)(delta,gamma)
 =2*Re K_a((1-j)*gamma+i*delta)
  +2*Re K_a((1+j)*gamma+i*delta).                  (3.5)
```

Therefore

```text
R_(a,P)=sum_j lambda_j R_(a,j)
        =-2*lambda_1*A_a(delta)^2+E_target,         (3.6)
```

where `E_target` contains only real frequencies at least `gamma`.

For a completely explicit error bound, set

```text
q_(a,b)(x)=sinh(a*x)*exp(-b*x),
V_a(b)=|q_(a,b)(-H)|+|q_(a,b)(H)|
       +integral_(-H)^H |q_(a,b)'(x)|dx.            (3.7)
```

One integration by parts proves

```text
|K_a(x+i*b)|<=V_a(b)^2/x^2                  (x!=0). (3.8)
```

Hence

```text
|E_target|
 <=(2*V_a(delta)^2/gamma^2)
   *[2*lambda_0+lambda_1/4
     +sum_(j>=2)lambda_j
        *(1/(j-1)^2+1/(j+1)^2)].                   (3.9)
```

In particular every fixed amplifier with `lambda_1>0` retains the full
negative carrier as `gamma` grows.

## 4. The classical three-center amplifier really retains the carrier

For (1.1), `(lambda_0,lambda_1,lambda_2)=(3,4,1)`.  Formula (3.5) gives

```text
R_(a,P_*)
 =8*K_a(i*delta)
  +14*Re K_a(gamma+i*delta)
  + 8*Re K_a(2*gamma+i*delta)
  + 2*Re K_a(3*gamma+i*delta).                     (4.1)
```

At the matched depth `a=delta`, `K_a(i*a)=-C_a(0)^2`.  The monotonicity
calculation used in the centered-sinh report gives

```text
V_a(a)=2*sinh(a*L).                                 (4.2)
```

Thus

```text
R_(a,P_*)
 <=-8*C_a(0)^2
    +(584/9)*sinh(a*L)^2/gamma^2.                  (4.3)
```

It is strictly negative whenever

```text
gamma>(sqrt(73)/3)*sinh(a*L)/C_a(0).               (4.4)
```

The exact pole and prime ledgers of the same amplifier are

```text
Pi_(a,P_*)
 =6*K_a(i/2)+8*Re K_a(gamma+i/2)
                +2*Re K_a(2*gamma+i/2),            (4.5)

Prime_(a,P_*)
 =2*sum_(n<=exp L) Lambda(n)/sqrt(n)
       *C_a(log n)*P_*(gamma*log n).                (4.6)
```

Equations (4.3)--(4.6) are the useful positive result of the audit: harmonic
amplification and target retention are compatible at constant cost.  What
fails is the proposed arithmetic inference from `P_*>=0`.

## 5. Universal sign change of the sinh autocorrelation

### Theorem 5.1 (two deterministic sign zones)

For every `L,a>0`,

```text
C_a(u)>0  for 0<=u<=L/3,
C_a(u)<0  for L/2<=u<L.                             (5.1)
```

#### Proof

Write `t=u/L` and `x=a*L`.  Apart from the positive factor
`L*(1-t)/2`, the sign of (2.5) is the sign of

```text
sinh((1-t)*x)/((1-t)*x)-cosh(t*x).                 (5.2)
```

If `t>=1/2`, then `(1-t)*x<=t*x` and

```text
sinh(y)/y<cosh(y)<=cosh(t*x),
```

which proves the negative assertion.

If `0<=t<=1/3`, put `A=1-t` and `B=t`, so `A>=2*B`.  The case `B=0` is
immediate from the positive nonconstant coefficients of
`sinh(A*x)/(A*x)`.  If `B>0`, then in the power series for (5.2) the
constant terms agree and, for every `k>=1`,

```text
A^(2*k)>=(2*B)^(2*k)>(2*k+1)*B^(2*k).              (5.3)
```

The last inequality is `4^k>2*k+1`.  Termwise comparison of
`sinh(A*x)/(A*x)` and `cosh(B*x)` proves positivity.  QED

### Corollary 5.2 (positive depth blocks cannot make a one-sign kernel)

Let `a_1,...,a_R>0`, let every `P_r` be a nonzero nonnegative
trigonometric polynomial, and let

```text
W(u)=sum_(r<=R) C_(a_r)(u)*P_r(gamma*u).            (5.4)
```

Then `W>=0` on `[0,L/3]` and `W<=0` on `[L/2,L]`.  The first inequality is
strict away from the discrete common zero set of the `P_r`; the second is
strict on `[L/2,L)` away from that set, while every autocorrelation vanishes
at `u=L`.  Hence `W` changes sign and cannot be a nonzero globally positive
or globally negative prime weight.

At the actual nodes this says

```text
W(log n)>=0  for n<=exp(L/3),
W(log n)<=0  for n>=exp(L/2).                       (5.5)
```

Thus (3.3) subtracts the low-prime range and adds the high-prime range.  The
positivity of `Lambda(n)` alone compares neither range with the other.

This failure is logical, not just aesthetic.  Choose a point
`u_0 in (0,L/3)` outside the common zero set, so `W(u_0)>0`, and replace the
prime measure in (3.3) by the positive measure `M*delta_(u_0)`.  With pole
and archimedean data fixed, the resulting ledger tends to `-infinity` as
`M` tends to infinity.  It obeys coefficient positivity and every
phase-polynomial hypothesis used in this route.  Therefore those hypotheses
alone imply no lower bound.  This abstract positive measure is not asserted
to be the von Mangoldt measure; actual-prime cancellation remains additional
arithmetic information.

There is also a finite-degree obstruction to exact deletion of the adverse
range.  If a nonzero nonnegative degree-`m` polynomial is required to vanish
at `gamma*log p` for every prime `p<=N`, it must have

```text
m>=pi(N)/2.                                         (5.6)
```

Indeed a nonnegative degree-`m` trigonometric polynomial has at most `m`
distinct zeros modulo `2*pi`, since every zero has even multiplicity.  No
three distinct primes can have the same phase.  Otherwise, for distinct
`p_1,p_2,p_3`, there would be nonzero integers `k,l` with
`gamma*log(p_1/p_2)=2*pi*k` and
`gamma*log(p_1/p_3)=2*pi*l`.  Their ratio gives a nontrivial multiplicative
relation among the three primes, contrary to unique factorization.  Hence
the prime phases occupy at least `pi(N)/2` distinct points.

Bound (5.6) concerns exact nulling only.  Quantitative suppression without
exact zeros is a prime exponential-sum problem, not a consequence of
trigonometric positivity.

## 6. The unavoidable constant mode is a deeper negative carrier

For any real cosine polynomial `P>=0` which is not identically zero,

```text
lambda_0>0,                 |lambda_1|<=2*lambda_0. (6.1)
```

The first statement follows by integrating `P`; the second is the `2 x 2`
Toeplitz minor, or equivalently
`|widehat P(1)|<=widehat P(0)` with
`widehat P(1)=lambda_1/2`.

For the positive harmonic covariance (3.1) we additionally require every
`lambda_j>=0`.  If `lambda_1=0` there is no aligned target main term, so the
comparison below concerns `lambda_1>0`.

Using half-integer or finitely many incommensurable harmonics does not remove
the first conclusion.  A finite continuous almost-periodic sum with no zero
frequency has Bohr mean zero.  If it is everywhere nonnegative, its mean can
vanish only when the sum is identically zero.  Thus every nontrivial global
positive-phase amplifier, periodic or not, carries a positive zero-center
component.  Requiring positivity only at the finite prime phases is a
different interpolation problem.

From (3.4), (3.8), and (6.1), the pole ledger is

```text
Pi_(a,P)
 =-2*lambda_0*A_a(1/2)^2+E_pole,                  (6.2)

|E_pole|
 <=(2*V_a(1/2)^2/gamma^2)
       *sum_(j>=1)lambda_j/j^2.                    (6.3)
```

Compare its aligned term with the target term in (3.6).  For fixed
`a,b>0`, (2.3) gives

```text
A_a(b)
 =exp((a+b)*L/2)/(2*(a+b))*(1+o(1)).               (6.4)
```

Therefore, for `0<delta<1/2`,

```text
[lambda_0*A_a(1/2)^2]/[lambda_1*A_a(delta)^2]
 >=(1/2)*((a+delta)/(a+1/2))^2
      *exp((1/2-delta)*L)*(1+o(1)).                 (6.5)
```

The pole and target have the **same negative sign**, and the pole is deeper
by a fixed power.  For (1.1) the exact coefficient ratio in place of `1/2`
is `lambda_0/lambda_1=3/4`.

The common sign has a packet-level explanation.  For any real odd packet
`f`,

```text
K_f(i*b)=-[2*integral_0^H f(x)*sinh(b*x)dx]^2.      (6.6)
```

If additionally `f(x)>=0` for `x>0`, the magnitude inside brackets is
strictly increasing in `b`.  Thus every half-line-positive odd packet sees
the pole at displacement `1/2` with the same sign and at least the magnitude
with which it sees a target at `delta<1/2`.  The explicit sinh tent upgrades
this monotonic comparison to the fixed-power ratio (6.5).

The archimedean term does not hide another carrier of this size.  The exact
formula

```text
F_a(t)=2*i*[a*sin(t*H)*cosh(a*H)
            -t*cos(t*H)*sinh(a*H)]/(a^2+t^2)       (6.7)
```

and the logarithmic growth of the gamma multiplier imply, for fixed `a`,

```text
Arch_(a,j*gamma)
 =O_a(exp(a*L)*(1+log(2+j*gamma))).                 (6.8)
```

For a fixed amplifier and `log gamma=O(L)`, (6.8) and the optional `+1`
energy completion are smaller than the pole by `exp(-L/2)*L` and smaller
than the target by `exp(-delta*L)*L`.

Could many remote pole tails cancel (6.2) inside the pole ledger?  Even
cancelling half of the aligned pole in this way requires, by (6.3),

```text
sum_(j>=1)lambda_j/j^2
 >=lambda_0*A_a(1/2)^2*gamma^2/[2*V_a(1/2)^2].     (6.9)
```

For fixed `a`, the first exponential in (2.3) gives
`A_a(1/2)>=c(a)*exp((a+1/2)*H)`, while the endpoint and variation terms in
(3.7) give `V_a(1/2)<=C(a)*exp((a+1/2)*H)`.  Thus their ratio is bounded away
from zero as `L` grows.  Hence (6.9) needs
`Omega(lambda_0*gamma^2)` total coefficient
mass.  The trace of each center covariance in (2.6) is exactly `C_a(0)`, so
trace normalization divides all coefficients by `sum_j lambda_j`.  Since
`lambda_1<=2*lambda_0`, the normalized aligned coefficient, and therefore
the aligned target carrier, is `O(gamma^(-2))`.  Remote pole-tail
cancellation exchanges the pole wall for a quadratic carrier dilution.  It
does not rule out cancellation by the actual prime or archimedean ledgers.

## 7. Why finitely many depths do not repair the classical argument

Suppose each depth `a_r` carries its own nonnegative phase polynomial
`P_r`, with nonnegative cosine coefficients so that it also defines a
positive harmonic mixture as in (3.1).  Then Corollary 5.2 applies to the
total prime kernel.  Moreover, block by block,

```text
target main_r=-2*lambda_(r,1)*A_(a_r)(delta)^2,
pole main_r  =-2*lambda_(r,0)*A_(a_r)(1/2)^2,       (7.1)
```

with `lambda_(r,1)<=2*lambda_(r,0)`.  Every block has the same pole sign;
each block with `lambda_(r,1)>0` has the fixed-power ratio (6.5), while a
block with `lambda_(r,1)=0` adds pole mass and no aligned target.  Thus
positive depth mixing cannot cancel the aligned zero-mode pole.

One may instead arrange that only the coefficient sum

```text
sum_r P_r(theta)
```

is nonnegative while individual `P_r` change sign.  That fact has no
prime-side consequence: the actual coefficient of the `j`th phase is
`C_(a_r)(u)`, which depends on both `r` and `u`.  Nonnegativity after erasing
these amplitudes is not nonnegativity of the prime kernel.

A coherent signed linear combination of packet **vectors** is different.
It can impose

```text
integral f(x)*sinh(x/2)dx=0                         (7.2)
```

and thereby null the pole.  But its square contains cross-depth
autocorrelations and is not a positive mixture of the squares audited here.
Likewise a signed harmonic combination can remove the constant mode, but
then it is not a nonnegative covariance and loses the critical-line
positivity which motivated the construction.  These are legitimate new
problems, not exceptions to the theorem above.

## 8. Exact comparison with de la Vallee Poussin and Turan

The classical logarithmic-derivative ledger has the opposite useful sign.
For `sigma>1`,

```text
D(s)=-zeta'(s)/zeta(s)=sum_n Lambda(n)n^(-s),

sum_j lambda_j*Re D(sigma+i*j*gamma)
 =sum_n Lambda(n)n^(-sigma)*P(gamma*log n)>=0       (8.1)
```

whenever `P>=0`.  In the zero expansion of `D`, the pole at one supplies a
positive budget and a nearby zero subtracts from it.  Inequality (8.1)
therefore bounds how close the zero can approach the pole.  The elementary
constraint `lambda_1<=2*lambda_0` is part of that pole-versus-zero budget;
it is not a free amplifier.

For the centered Weil square the exact ledger is instead

```text
pole + archimedean - prime.                         (8.2)
```

The desired off-line carrier is negative, the odd packet's pole carrier is
also negative and deeper, and the prime amplitude `C_a` changes sign.  If
the prime weight in (8.2) were nonnegative, positivity of `Lambda` would
give an **upper** bound for the square, whereas the arithmetic gate needs a
lower bound.  In reality Theorem 5.1 prevents even that one-sign reduction.
Thus (8.1) cannot simply be transplanted into (8.2).

Turan power-sum arguments use signed high derivatives or powers to isolate
a logarithmic-derivative singularity.  Those signed operations can cancel a
constant mode, but they are not positive combinations of Weil squares.
Applying them to the two-abscissa sinh-tent scalar would require uniform
bounds for the resulting prime exponential sums over a range of harmonic
orders.  That is coefficient-specific arithmetic information; it is
exactly what trigonometric positivity was supposed to avoid.  The separate
target-conditioned harmonic-cascade audit shows that zero counting and
prime-side positivity alone also allow critical-line compensation.

## 9. Scope and remaining escape

This report proves neither that the centered arithmetic square is positive
nor that it is negative.  It rules out only the following bounded-cost
classical mechanism:

```text
positive incoherent mixtures of centered odd sinh-tent squares,
with globally nonnegative trigonometric phase polynomials,
using only positivity of Lambda(n) to infer the needed Weil lower sign.
```

Three materially different directions remain.

1. Prove actual cancellation between the low positive and high negative
   prime ranges in (5.5).  In the unamplified case this is precisely the
   centered two-abscissa prime-discrepancy gate.
2. Build one coherent odd, pole-null packet satisfying (7.2), and re-audit
   its cross-depth autocorrelation and target overlap.
3. Abandon global trigonometric positivity and solve a finite actual-prime
   phase interpolation problem.  This returns to the positive spectral
   prime-moment/central-atom gate and needs a quantitative aligned mass.

None of these follows from de la Vallee Poussin or Turan formalism alone.
