# R172 hull-compatible delayed truncation and prime lift

## Status

The transition-hull obstruction in R168 has one genuine analytic escape:
make the target itself holomorphic on the filled hull and exponentially
small on the inner disk, rather than prescribing incompatible data on
separate pieces.  In that setting a completely elementary operation works:
take a Bernstein--Walsh approximant and delete every monomial of degree less
than `M`.

There is an exact exponent condition.  Suppose

```text
{|q|<=r} subset E subset {|q|<=R},          r>1,        (0.1)
```

and a degree-`dM` polynomial approximates a hull-compatible target `G_M`
with error `exp(-beta M)`, while

```text
sup_(|q|<=r)|G_M(q)| <= exp(-A M).                       (0.2)
```

Then deletion of the degrees below `M` gives

```text
P_M(q)=sum_(n=M)^(floor(dM)) c_(n,M) q^n               (0.3)
```

with

```text
sup_E |G_M-P_M|
   << M exp(-[min(A,beta)-log(R/r)]M),                  (0.4)

sum_n |c_(n,M)|
   << exp(-[min(A,beta)+log r]M).                       (0.5)
```

Consequently this construction is power-effective exactly when

```text
min(A,beta)>log(R/r).                                   (0.6)
```

For a fixed Bernstein--Walsh neighborhood with approximation rate
`rho^D`, and targets satisfying

```text
sup_U |G_M| << exp(lambda M),                           (0.7)
```

one may take

```text
beta=d log(1/rho)-lambda.                               (0.8)
```

Thus increasing the fixed degree ratio `d` beats every fixed exponential
neighborhood-growth bill.

The neighborhood-growth hypothesis is necessary.  Holomorphy on a fixed
neighborhood and a bound on `E` alone do **not** imply a degree-`O(M)`
approximation.  On `E={|q|<=R}`, the entire functions

```text
G_M(q)=(q/R)^(M^2)                                     (0.9)
```

are bounded by one on `E` and are smaller than `exp(-AM)` on every smaller
disk for every fixed `A`, but their distance from all degree-`dM`
polynomials is at least one.  Therefore the theorem proposed with only
`sup_E|G_M|<=exp(lambda M)` is false; (0.7), or an equivalent quantitative
degree-complexity hypothesis, is indispensable.

Taking `M=B log H`, (0.5) supplies strict coefficient slack after the exact
logarithmic-density correction.  The actual-prime block lift and random-sign
rounding of R163 then apply without a new loss.  On a compact set with

```text
sigma_0=inf Re(s)>7/12,                                 (0.10)
```

the arithmetic remainder still permits every exponent

```text
c<sigma_0-7/12.                                         (0.11)
```

This **does** bypass the analytic transition-hull no-go for rapidly varying,
hull-compatible targets.  For example `(q/R)^M` is tiny on the inner disk
and has modulus one on the outer circle.  It does **not** recover the old
nonzero-left/zero-right cutoff: a target converging to a fixed nonzero
profile on the outside arc remains impossible.  Any successful zeta
application must therefore make the nonlinear collective cofactor accept an
`M`-dependent high-frequency phase.  No such divisor-preserving realization
is proved here.

There is a second, quantitatively different regime.  If the target norm on
the fixed Bernstein--Walsh neighborhood is `exp(H^chi)`, while its inner
value is only power-small in `H`, then the delay may remain `O(log H)` but
the uniform Bernstein--Walsh construction requires maximum degree
`Theta(H^chi)`, and this order is sharp for the full target class.  The
corresponding prime horizon is

```text
Y=H exp(Theta(H^chi)),                                  (0.12)
```

not `H^kappa`.  This loses the polynomial-horizon ledger used in the
earlier fixed-cutoff formulation.  It does not by itself lose local analytic
control: the actual-prime block error, sign-rounding error, exact
logarithmic-Euler lift, and the right-half-plane higher-power correction are
uniform in the upper cutoff.  A controlled globally compatible target can
therefore keep this superpolynomial-horizon route analytically alive.  What
must be re-audited is every later argument that genuinely uses a polynomial
upper cutoff, not the prime-discretization step itself.

The companion propagation theorem R174 explains why this regime occurs:
power-small cap normalization around a retained divisor forces a logarithm
of size at least `H^chi` somewhere on a fixed bridge, so the corresponding
multiplier can have size `exp(H^chi)`.  The superpolynomial degree conclusion
applies when that **multiplier** is approximated directly.  If arithmetic is
performed in logarithmic coordinates, the target norm may instead be only
`H^chi=exp(chi log H)`; then the one-scale theorem can still have degree
`O(log H)`, provided the logarithmic target has the required inner smallness
and coefficient slack.  R174's generic cap-peak construction does not by
itself prove that slack.

```text
weak bounded-on-E formulation                            FALSE
fixed-neighborhood exponential-growth formulation        THEOREM
delayed support M<=n<=dM                                 THEOREM
exponent margin min(A,beta)>log(R/r)                     EXACT FOR THIS PROOF
exponentially small coefficient ell^1 norm               THEOREM
exact logarithmic-density repair                         THEOREM
fractional actual-prime lift                             THEOREM
one sign per actual prime                                THEOREM
fixed-profile transition cutoff                          STILL IMPOSSIBLE
rapid-phase hull-compatible transition target            ANALYTICALLY FEASIBLE
target norm exp(H^chi)                                   DEGREE Theta(H^chi)
polynomial prime horizon for that target                  LOST IN GENERAL
prime lift / rounding uniform in the upper cutoff         SURVIVES
divisor-preserving collective-cofactor realization       OPEN
fixed uniform zeta zero-free strip                       NOT PROVED
zeros approaching Re(s)=1                                NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md),
[`R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md`](R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md),
and
[`R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md`](R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md).
See also the companion conditioning result
[`R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md`](R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md).

## 1. Quantitative hull hypothesis

Let `E` be a regular polynomially convex compact set in `C`, invariant under
conjugation, and assume (0.1).  Let `U` be a fixed conjugation-invariant
neighborhood of `E`.  We use the following quantitative form of
Bernstein--Walsh approximation: there are constants

```text
C_BW>=1,                     0<rho<1                   (1.1)
```

such that, for every `F` holomorphic on `U` and every integer `D>=0`, there
is a polynomial `Q_D` of degree at most `D` satisfying

```text
sup_E |F-Q_D| <= C_BW rho^D sup_U |F|.                  (1.2)
```

For a fixed Green-function level neighborhood compactly contained in `U`,
(1.2) is the standard Bernstein--Walsh estimate.  It is useful to state
(1.2) explicitly because mere extension to `U`, without a bound on that
extension, gives no uniform rate for a varying family.

Assume that `G_M` is holomorphic on `U`, respects conjugation, and obeys

```text
sup_U |G_M| <= C_G exp(lambda M),
sup_(|q|<=r)|G_M(q)| <= C_G exp(-A M),                  (1.3)
```

where `A>0` and `lambda>=0` are fixed.  Bounds with a negative `lambda` are
of course stronger and can be included without change.

Put

```text
ell=log(R/r),
beta=d log(1/rho)-lambda.                               (1.4)
```

The only substantive exponent hypothesis below is

```text
d>1,                 min(A,beta)>ell.                   (1.5)
```

## 2. Hull-compatible delayed truncation theorem

### Theorem 2.1

Under (1.1)--(1.5), there are real polynomials `P_M` of the form (0.3) and
a constant `C`, independent of `M`, such that

```text
sup_E |G_M-P_M|
 <= C M exp(-[min(A,beta)-ell]M),                       (2.1)

sum_(n=M)^(floor(dM)) |c_(n,M)|
 <= C exp(-[min(A,beta)+log r]M).                       (2.2)
```

In particular, for every

```text
0<eta<min(A,beta)-ell                                  (2.3)
```

the right side of (2.1) is `O(exp(-eta M))`.

### Proof

Let

```text
D=floor(dM).                                             (2.4)
```

By (1.2)--(1.3), there is a polynomial

```text
Q_M(q)=sum_(n=0)^D a_(n,M)q^n                           (2.5)
```

such that

```text
epsilon_M:=sup_E|G_M-Q_M|
 << rho^D exp(lambda M)
 << exp(-beta M).                                       (2.6)
```

Symmetrizing `Q_M` by

```text
[Q_M(q)+conjugate(Q_M(conjugate(q)))]/2                 (2.7)
```

makes all coefficients real without increasing the degree or error.

On the circle `|q|=r`, (1.3) and (2.6) give

```text
|Q_M(q)| << exp(-AM)+exp(-beta M).                      (2.8)
```

Cauchy's coefficient estimate therefore gives, for every `0<=n<=D`,

```text
|a_(n,M)|
 << [exp(-AM)+exp(-beta M)]r^(-n).                      (2.9)
```

Delete the low-degree part and set

```text
P_M(q)=sum_(n=M)^D a_(n,M)q^n.                          (2.10)
```

For `q in E`, `|q|<=R`, and hence

```text
|Q_M(q)-P_M(q)|
 <<[exp(-AM)+exp(-beta M)]
       sum_(n=0)^(M-1)(R/r)^n
 <<M exp(-[min(A,beta)-ell]M).                          (2.11)
```

Together with (2.6), this proves (2.1).  For the retained coefficients,
(2.9) gives

```text
sum_(n=M)^D |a_(n,M)|
 <<[exp(-AM)+exp(-beta M)]sum_(n=M)^infinity r^(-n)
 <<exp(-[min(A,beta)+log r]M),                          (2.12)
```

because `r>1`.  This proves (2.2).  QED.

### Remark 2.2 -- the direct approximation form

The neighborhood hypothesis can be replaced by exactly what the proof
uses.  If there are degree-`dM` polynomials `Q_M` with

```text
sup_E|G_M-Q_M| << exp(-beta M),                         (2.13)
```

then (2.1)--(2.2) hold whenever `min(A,beta)>ell`.  This is
the most general formulation.  Equations (1.2)--(1.3) are a convenient
checkable sufficient condition for (2.13).

### Remark 2.3 -- the margin is the actual truncation bill

The factor `exp(ell M)=(R/r)^M` in (2.11) is not an artifact of replacing a
geometric sum by a rough estimate.  Information about a low Taylor
coefficient obtained on `|q|=r` can amplify by exactly `(R/r)^n` at radius
`R`.  A better theorem would need more than the two sup-norm bounds used
here, for example phase cancellation among the deleted coefficients.

## 3. Why boundedness on the hull is insufficient

### Proposition 3.1

Fix `1<r<R`, a constant `d>0`, and put

```text
E={|q|<=R},                 G_M(q)=(q/R)^(M^2).          (3.1)
```

Then `G_M` is entire,

```text
sup_E|G_M|=1,                                             (3.2)
```

and for every fixed `A>0`, once `M` is sufficiently large,

```text
sup_(|q|<=r)|G_M(q)|<=exp(-AM).                          (3.3)
```

Nevertheless, for every polynomial `P` of degree at most `dM`,

```text
sup_E|G_M-P|>=1                                         (3.4)
```

when `M>d`.

### Proof

Equations (3.2)--(3.3) follow from

```text
(r/R)^(M^2)=exp[-M^2 log(R/r)].                         (3.5)
```

If `M^2>dM`, the coefficient of `q^(M^2)` in `G_M-P` is `R^(-M^2)`.
Cauchy's coefficient estimate on `|q|=R` says

```text
R^(-M^2)<=R^(-M^2) sup_(|q|<=R)|G_M-P|,                 (3.6)
```

which proves (3.4).  QED.

Thus the assumptions

```text
G_M holomorphic on one fixed neighborhood,
sup_E|G_M|<=1,
sup_(|q|<=r)|G_M|<=exp(-AM)                             (3.7)
```

do not control linear-in-`M` degree complexity.  In (3.1), the supremum on
any strictly larger disk grows like `exp(cM^2)`, exactly violating (1.3).

## 4. Causal Laplace realization

Let

```text
lambda=1-s,                 q=exp(h lambda),
kappa_h(lambda)=[exp(h lambda)-1]/lambda,               (4.1)
```

with the removable value `kappa_h(0)=h`.  Let `Lambda` be a fixed compact
set whose `q`-image is contained in `E`, and assume the desired target
descends to the `q`-plane.  For the polynomial (0.3), define the real step
function

```text
a_M(v)=c_(n,M),             nh<=v<(n+1)h.               (4.2)
```

Termwise integration gives the exact identity

```text
integral_0^infinity a_M(v)exp(lambda v)dv
       =kappa_h(lambda)P_M(exp(h lambda)).              (4.3)
```

The support and amplitude satisfy

```text
support(a_M) subset [Mh,(floor(dM)+1)h],
||a_M||_infinity
 <=sum_n|c_(n,M)|
 <<exp(-nu M),                                           (4.4)

nu=min(A,beta)+log r>0.                                 (4.5)
```

If `kappa_h G_M` is the desired Laplace target, then Theorem 2.1 gives,
for every `eta` as in (2.3),

```text
sup_(lambda in Lambda)
 |kappa_h(lambda)G_M(exp(h lambda))
   -integral_0^infinity a_M(v)exp(lambda v)dv|
 <<exp(-eta M).                                         (4.6)
```

The bounded factor `kappa_h` is absorbed in the implied constant.

## 5. Exact logarithmic density

Put

```text
T=log H,                       M=ceil(BT),               (5.1)
```

where `B>0` is fixed, and define

```text
b_H(v)=(T+v)a_M(v)/T.                                  (5.2)
```

Since `v<=h(dM+1)` on the support, (4.4) implies

```text
||b_H||_infinity
 <<_(B,d,h) exp(-nu M)<=1/2                             (5.3)
```

for all sufficiently large `H`.  Thus the control has fixed strict slack.
If

```text
Y=H exp[h(floor(dM)+1)]<=H^kappa,
kappa>1+hdB,                                             (5.4)
```

then the change of variables `x=H exp(v)` gives the exact identity

```text
integral_H^Y b_H(log(x/H))x^(-s)dx/log x
 =H^lambda/T integral_0^infinity
                  a_M(v)exp(lambda v)dv.                (5.5)
```

No approximation of `1/log x` by `1/log H` has been made.

For example, let `A_H(s)` be an analytic head and suppose

```text
G_M(exp(h lambda))
 =-T H^(-lambda)A_H(1-lambda)/kappa_h(lambda)           (5.6)
```

is single-valued and satisfies the hypotheses of Theorem 2.1.  If

```text
Lambda_+=max_(lambda in Lambda)Re(lambda),              (5.7)
```

then (4.6) and (5.5) give

```text
sup_(lambda in Lambda)
 |A_H(1-lambda)
   +integral_H^Y b_H(log(x/H))x^(lambda-1)dx/log x|
 <<H^(Lambda_+-eta B+o(1)).                             (5.8)
```

Hence every prescribed continuum exponent `C>0` follows by taking

```text
B>(C+Lambda_+)/eta,                                     (5.9)
```

provided the family in (5.6) continues to satisfy the uniform target
hypotheses for that fixed `B`.

## 6. Lift to actual primes and signs

Let `K=1-Lambda` and put

```text
sigma_0=inf_(s in K)Re(s).                              (6.1)
```

Choose

```text
7/12<theta<sigma_0.                                     (6.2)
```

Theorem 2.1 of R163 applies to the strictly slack control (5.2).  It gives
coefficients `u_p in [-1,1]`, supported on the actual primes `H<p<=Y`,
such that

```text
sup_(s in K)
 |sum_(H<p<=Y)u_p p^(-s)
   -integral_H^Y b_H(log(x/H))x^(-s)dx/log x|
 <<H^(theta-sigma_0)/log H.                             (6.3)
```

The proof normalizes by the exact number of primes in each short block, so
there is no additional PNT remainder.  The fact that `b_H` is supported
late in `[H,Y]` causes no change.

If `K` is compactly contained in a bounded domain in
`Re(s)>sigma_1>1/2`, Theorem 4.1 of R163 replaces the `u_p` by one sign
`epsilon_p in {+1,-1}` at each actual prime, at cost

```text
O(H^(1/2-sigma_1)/sqrt(log H)).                         (6.4)
```

After (5.9) makes the continuum error negligible, (6.3) is limiting.
Letting `theta` approach `7/12` gives every fixed exponent

```text
c<sigma_0-7/12.                                         (6.5)
```

The same block and rounding theorems apply to the exact logarithmic Euler
kernel.  The polynomial Laplace identity (4.3) directly shapes the linear
kernel.  If it is used as an approximation to the Euler logarithm, the
higher-power correction on this late support is bounded, for
`sigma_0>1/2`, by

```text
integral_(H exp(hM))^infinity x^(-2sigma_0)dx/log x
 <<[H exp(hM)]^(1-2sigma_0)/log H,                      (6.6)
```

and is therefore power-small as well.  Alternatively one may shape the
exact logarithmic-kernel continuum target before invoking R163's exact
logarithmic lift.

## 7. What this does and does not bypass

There are nontrivial hull-compatible examples.  For concentric disks,

```text
E={|q|<=R},               G_M(q)=(q/R)^M               (7.1)
```

is already a delayed polynomial.  It is exponentially small on
`|q|<=r`, but has modulus one on the whole outer circle.  Thus the identity
theorem does not forbid inner extinction together with outer magnitude;
the price is a phase oscillating `M` times around the boundary and
exponential growth on every fixed larger neighborhood.

This explains exactly why there is no contradiction with R168.  R168
rules out polynomials converging to zero on the disk and to one fixed
nonzero analytic profile on the outside arc.  The sequence in (7.1) has no
such nonzero uniform limit on any outer arc.  More generally, if a family
covered by Theorem 2.1 converged uniformly to a fixed nonzero profile on an
outside arc while tending to zero on the disk, the resulting `P_M` would
contradict Proposition 6.1 of R168.  Therefore at least one exponent or
complexity hypothesis of this theorem must fail for every stable cutoff
family.

The new option is narrower but real:

```text
fixed left profile + zero right profile                 impossible;
M-dependent rapid-phase carrier + tiny right magnitude  possible.   (7.2)
```

Rouche arguments depend on magnitudes and winding, so a rapid phase is not
automatically useless.  But it must be incorporated into the exact divisor
ledger.  In the current nonlinear program that means constructing optional
prime channels for which the collective cofactor is asymptotic to such a
hull-compatible high-degree carrier while retaining the prescribed zeta
divisor.  R164--R171 do not yet supply that realization.  The present result
therefore removes the polynomial-hull obstruction for the correct target
class; it does not prove that the zeta target belongs to that class.

## 8. Two-scale theorem and `exp(H^chi)` targets

The delay and the approximation degree need not be proportional.  Keeping
them separate is essential when a cap-normalized construction has very
large bridge growth.  R174 proves that this growth is unavoidable for the
logarithm of an exactly retained divisor with power-small cap error.  The
theorem below concerns direct approximation of the associated full
multiplier.  Approximation of the logarithm itself has the smaller target
norm `H^chi` and must be assessed separately.

### Theorem 8.1 -- arbitrary target scale

Retain the geometry and Bernstein--Walsh estimate (1.1)--(1.2), and write

```text
tau=log(1/rho),                  ell=log(R/r).           (8.1)
```

Let `N=N_H` and `D=D_H` be integers with `1<=N<=D`.  Suppose

```text
sup_U|G_H|                    <=C exp(L_H),
sup_(|q|<=r)|G_H(q)|          <=C exp(-a_H),             (8.2)
```

and put

```text
beta_H=tau D_H-L_H.                                    (8.3)
```

There is a polynomial

```text
P_H(q)=sum_(n=N_H)^(D_H)c_(n,H)q^n                     (8.4)
```

such that

```text
sup_E|G_H-P_H|
 <<exp(-beta_H)
   +N_H exp(N_H ell)[exp(-a_H)+exp(-beta_H)],           (8.5)

sum_n|c_(n,H)|
 <<[exp(-a_H)+exp(-beta_H)]r^(-N_H).                    (8.6)
```

Thus approximation tends to zero whenever

```text
min(a_H,beta_H)-N_H ell ->+infinity,                    (8.7)
```

and the coefficient norm tends to zero whenever

```text
min(a_H,beta_H)+N_H log r ->+infinity.                  (8.8)
```

#### Proof

Choose a degree-`D_H` Bernstein--Walsh approximant `Q_H`.  Its error is

```text
O[rho^(D_H)exp(L_H)]=O(exp(-beta_H)).                   (8.9)
```

On `|q|=r`, `Q_H` is bounded by the sum of the two exponentials in
(8.5).  Cauchy's estimate bounds its `n`-th coefficient by that sum times
`r^(-n)`.  Delete the coefficients with `n<N_H`.  Summing them on
`|q|<=R` proves (8.5), and summing the retained coefficients from `N_H` to
infinity proves (8.6).  QED.

### Corollary 8.2 -- bridge norm `exp(H^chi)`

Fix `chi>0`, `A>0`, and `B>0`, and suppose

```text
L_H=H^chi+O(1),                 a_H=A log H,
N_H=ceil(B log H).                                      (8.10)
```

Choose

```text
D_H=ceil([H^chi+A log H]/tau).                          (8.11)
```

Then `beta_H=A log H+O(1)`, and Theorem 8.1 gives

```text
sup_E|G_H-P_H| <=H^(-A+B ell+o(1)),                     (8.12)

sum_n|c_(n,H)| <=H^(-A-B log r+o(1)).                   (8.13)
```

In particular, hull approximation has a fixed power saving if

```text
A>B log(R/r).                                           (8.14)
```

The causal step function now extends to time

```text
v_max=hD_H=(h/tau+o(1))H^chi,                          (8.15)
```

so its exact prime horizon is

```text
Y=H exp[(h/tau+o(1))H^chi].                            (8.16)
```

The logarithmic-density multiplier in (5.2) has size at most

```text
1+v_max/log H=H^(chi+o(1)).                             (8.17)
```

Equations (8.13) and (8.17) therefore retain strict coefficient slack
provided

```text
A+B log r>chi.                                          (8.18)
```

If the final continuum target also incurs the factor `H^Lambda_+` from
(5.5), its available power exponent is

```text
A-B log(R/r)-Lambda_+.                                 (8.19)
```

Thus a positive final exponent requires the corresponding strict version
of (8.14).  Conditions (8.14) and (8.18) display the complete two-sided
choice of the delay `B`: increasing `B` improves coefficient slack through
`r^(-N)`, but worsens hull approximation through `(R/r)^N`.

The order in (8.11) is sharp for a uniform theorem.  To see this, take
concentric disks with

```text
1<r<R<S                                                     (8.19a)
```

and measure the neighborhood norm on `|q|<=S`.  Put

```text
n_H=ceil([H^chi+A log H]/log(S/r)),
G_H(q)=H^(-A)(q/r)^(n_H).                               (8.19b)
```

Then `G_H` is entire, its norm on `|q|<=r` is `H^(-A)`, and
its norm on `|q|<=S` is `exp(H^chi+O(log H))`.  If a polynomial has
degree less than `n_H`, Cauchy's estimate applied to the `q^(n_H)`
coefficient shows that its approximation error on `|q|<=R` is at least

```text
H^(-A)(R/r)^(n_H).                                     (8.19c)
```

In particular no degree `o(H^chi)` family gives a uniform small-error
theorem for all targets satisfying (8.10).  Special low-degree targets can
of course do better; R174's logarithmic polynomial is such additional
structure and should not be replaced unnecessarily by its full
exponential multiplier.

### Proposition 8.3 -- the arithmetic lift is cutoff-uniform

The restriction `Y<=H^kappa` in the convenient statement of R163 is not
needed for its error estimates.  If `Y>H` is any finite number and

```text
7/12<theta<sigma_0,                                    (8.20)
```

the same exact block normalization gives

```text
O(H^(theta-sigma_0)/log H)                              (8.21)
```

uniformly in `Y`.

Indeed, the sum of the block-variation errors is bounded by

```text
integral_H^Y x^(theta-sigma_0-1)dx/log x
 <=integral_H^infinity x^(theta-sigma_0-1)dx/log x
 <<H^(theta-sigma_0)/log H.                             (8.22)
```

The last incomplete block obeys the same bound because
`theta-sigma_0<0`.  The all-interval prime theorem used to verify coefficient
capacity is uniform once the left endpoint exceeds `H`.  Likewise the
random-sign variance is bounded by

```text
sum_(p>H)p^(-2sigma_1),                                 (8.23)
```

independently of `Y`.

For the exact Euler logarithm, block variation uses

```text
|d Log(1-x^(-s))/dx| <<x^(-sigma_0-1),                 (8.24)
```

again giving (8.22).  Random rounding uses
`|Log(1-p^(-s))|<<p^(-sigma_1)`, so (8.23) is unchanged.
Finally, the accumulated difference between the linear and logarithmic
kernels is bounded by (6.6), whose integral converges at infinity for
`sigma_0>1/2`.  Hence all three arithmetic passages are uniform even for
the superpolynomial horizon (8.16).

The verdict is therefore precise:

```text
hull compatibility             removes the topological obstruction;
norm exp(H^chi)                worst-case degree/time Theta(H^chi);
prime horizon                  becomes H exp(Theta(H^chi));
actual-prime/error estimates   remain cutoff-uniform;
local outer bound              survives if the target controls it;
polynomial-horizon hypotheses  require a new audit.                  (8.25)
```

This distinction matters for R166 and R170.  Their right-half-plane tail
majorants start at the lower support cutoff and may be summed to infinity,
so they do not automatically fail when `Y` is enlarged.  On the other
hand, any conductor, complexity, or global-growth estimate which explicitly
uses `Y=H^kappa` is no longer available from the old ledger.  The
superpolynomial horizon is therefore a serious new cost, but not by itself
an analytic contradiction.

### Remark 8.4 -- why multiplying by `q^N` is not enough here

On a fixed compact set bounded away from zero, one can approximate
`q^(-N)t_H(q)` by a polynomial `Q_H` and then put `P_H=q^NQ_H`.  Standard
finite-degree norm comparison costs at most `exp(CD)` in coefficient norm
on fixed nonpolar geometry.  Thus this older device works for a target
`t_H` small enough to pay an `exp(CN)` bill when `D=O(N)`.

It does not address a generic target with neighborhood norm
`exp(H^chi)` using `N=O(log H)`: Bernstein--Walsh still requires
`D=Omega(H^chi)` unless the target has additional special low-degree
structure.  Moreover, the connected hull used here contains `q=0`, so
`q^(-N)G_H` is generally singular.  Direct low-degree deletion in Theorem
8.1 is precisely the version which remains valid on the filled hull.

## 9. R174, the unique-zero transform, and the high-jet condition

The superpolynomial upper prime horizon is not the variable which decides
the later high-jet contradiction.  That argument compares three local
quantities: target-pole derivatives, the lower-support gain, and the outer
holomorphic remainder.  The upper end of the prime block does not occur.

To make this exact, use starred letters for the localization geometry in
R166.  Let the retained pole be at distance `d_*` from the right center,
let the tail estimate hold on a circle of radius `r_*`, and let the outer
Cauchy circle have radius `R_*`, with

```text
0<r_*<d_*<R_*,              2d_*/r_*>1.                (9.1)
```

Suppose a support-`H^q` logarithmic derivative obeys

```text
|B^(k)(s_*)|/k!
 <<H^(-q r_*/2+o(1))(2/r_*)^k,                         (9.2)
```

while near the retained zero

```text
B(s)=1/(s-rho)+G_H(s),
sup_(|s-s_*|=R_*)|G_H(s)|<=M_B(H).                     (9.3)
```

The pole dominates the outer Cauchy remainder only if

```text
k>log M_B(H)/log(R_*/d_*)+O(1),                        (9.4)
```

whereas the tail is smaller than the pole only if

```text
k<[q r_*/(2 log(2d_*/r_*))]log H-o(log H).             (9.5)
```

Consequently the exact asymptotic room condition for this high-jet method
is

```text
q>C_geom [log M_B(H)/log H]+o(1),

C_geom=2 log(2d_*/r_*)/[r_* log(R_*/d_*)].             (9.6)
```

For `M_B(H)=H^(lambda+o(1))`, (9.6) is precisely R166's fixed-`q`
condition.  For `M_B(H)=exp(H^(chi+o(1)))`, it instead asks for

```text
q>C_geom H^(chi+o(1))/log H.                           (9.7)
```

This derivation also shows why (8.16) is not alone fatal: the prime-lift,
rounding, Euler-log, and right-tail estimates are upper-cutoff uniform, and
the high-jet interval (9.4)--(9.5) depends on lower support and outer local
growth, not on `Y`.

Now compare with the unique-zero transform

```text
Phi(F)=F exp(1-F),
Phi'(F)F'/Phi(F)=(1-F)F'/F.                            (9.8)
```

It preserves exactly the zeros of `F` and, because

```text
Phi(1+u)=1-u^2/2+O(u^3),                               (9.9)
```

it deletes the prime layer and starts at the two-fold support scale.  This
is the cleanest scalar example of the unique-zero transform from R97 and
R153.

For an R174 exact-divisor family

```text
F=Z exp(h),                  sup|h|<=H^(chi+o(1))       (9.10)
```

on a fixed slightly enlarged localization domain, Cauchy's estimate gives
`h'=H^(chi+o(1))`, while

```text
|F|<=exp(H^(chi+o(1))).                                 (9.11)
```

The direct bound from (9.8) is therefore

```text
M_B(H)<=exp(H^(chi+o(1))).                              (9.12)
```

up to fixed factors from `Z'/Z` on the boundary.  This is an upper ledger,
not a matching lower bound: special phase cancellation in `(1-F)F'/F`
could make the actual remainder smaller.  But with only the information
proved in R174, the fixed quadratic arity `q=2` does not satisfy the
available high-jet criterion (9.6).

Increasing the order of the scalar unique-zero transform does not
automatically repair this.  R153's order-`q` truncated-log transform has

```text
G_q'(F)F'/G_q(F)=(-1)^(q-1)(F-1)^(q-1)F'/F.            (9.13)
```

The crude R174-scale outer bill then has

```text
log M_B(H)=O(q H^(chi+o(1))).                           (9.14)
```

The same `q` appears on both sides of (9.6), so the support gain does not
beat this scalar boundary estimate once `H^chi>>log H`.  This is the
quantitative form of R153's unique-zero growth trilemma in the present
geometry.

The exact remaining alternatives are therefore:

1. prove a much smaller, phase-sensitive bound for the actual remainder
   `M_B(H)` in (9.3); or
2. realize a mixed-product or transfer-matrix amplifier with arity `q`
   satisfying (9.6), while keeping its outer remainder from acquiring the
   scalar `qH^chi` bill in (9.14).

Neither alternative is disproved by the superpolynomial prime horizon, and
neither is proved by the present approximation theorem.  Thus this route is
not closed: its unresolved exponent gate is exactly (9.6), together with
the divisor-preserving arithmetic realization of the chosen amplifier.
