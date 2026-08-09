# R150 translated-carrier and functional-equation gate

## Status

R149 left two possible analytic escapes from the absolute outer-divisor
ledger of the exterior quotient.  The first was to multiply a target-pole
detector by a translated copy of its positive, head-deleted Euler tail.  The
copy equals one at the target and is exponentially small at the observation
point, so at first sight it appears to preserve the pole while improving the
high-jet upper bound.  The second was to use the exact degree-zero functional
equation instead of an absolute Cauchy estimate.

Both escapes are closed in their natural forms.

1.  A normalized positive Dirichlet tail is a Laplace transform.  When it
    multiplies `1/w`, its order-`k` jet is not the isolated pole jet times a
    small harmless factor.  It is exactly that jet times a Poisson lower-tail
    probability.  In the head-deletion regime this probability is
    exponentially small.  The carrier's regular Taylor terms cancel the
    pole jet it was intended to retain.
2.  On any circle containing the target, the same carrier grows at the left
    point by `X^(R-d)`.  This growth is strictly larger than the entire
    Cauchy localization gain `(R/d)^k`, for every admissible radius.
3.  Making the carrier reflection-symmetric cannot help:
    `H(d)H(-d)>=1`.  The reflected factor pays back the one-sided decay.
4.  The exterior quotient's functional equation pairs every numerator zero
    with a numerator zero and every denominator pole with a denominator
    pole.  An antisymmetric kernel that cancels every unknown auxiliary pair
    also cancels the selected zeta pair.
5.  Classical `3-4-1` prime positivity makes the obstruction more explicit.
    Every standard-factor zero is a pole of the positive logarithmic
    derivative and contributes with the adverse positive sign at all three
    evaluation points.  Reflection reinforces rather than centers it.
6.  Conditional on the common zeta pole and a deleted Euler head, every
    field's remote regular part is forced to cancel the pole jet to
    exponential relative accuracy.  Convex averaging preserves that common
    mode; signed centering needs exponential condition number.
7.  Among all differential filters of order at most `k`, the pure highest
    derivative is already optimal for an absolute outer-divisor estimate.

Thus neither translated positive carriers, reflection-symmetric absolute
contours, nor `3-4-1` positivity lower the `O(log D)` remote-divisor bill.
Only pointwise correlation with the auxiliary divisor precisely where the
carrier is large could evade the theorem; that is the still-open signed
joint-divisor problem, not a consequence of the functional equation.

```text
translated carrier preserves target value                 TRUE
translated carrier preserves isolated high pole jet       FALSE
exact carried-pole jet                                     POISSON LOWER TAIL
absolute circular-contour gain                             IMPOSSIBLE
reflection-symmetric carrier gain                          IMPOSSIBLE
functional equation cancels auxiliary pairs only          FALSE
3-4-1 centers denominator poles                            FALSE
convex family centering removes common regular mode        FALSE
bounded-condition signed centering removes common mode     FALSE
mixed derivative orders improve absolute localization     FALSE
target-conditioned signed boundary cancellation           OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md`](R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md),
[`R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md`](R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md),
and
[`R149-DEGREE-ZERO-L-DATA-AND-DISTINCT-DIVISOR-GATE.md`](R149-DEGREE-ZERO-L-DATA-AND-DISTINCT-DIVISOR-GATE.md).

## 1. Positive tails are Laplace transforms

Let

```text
A_X(s)=sum_(n>X) a_n n^(-s),       a_n>=0,                 (1.1)
```

be nonzero and absolutely convergent for `Re(s)>1`.  Fix a real
`sigma_0>1` and normalize the translated carrier by

```text
H(w)=A_X(sigma_0+w)/A_X(sigma_0).                          (1.2)
```

Put `L=log X`.  The discrete measure

```text
mu({log n})=a_n n^(-sigma_0)/A_X(sigma_0)                  (1.3)
```

is a probability measure supported on `[L,infinity)`, and

```text
H(w)=integral_[L,infinity) exp(-tw) dmu(t).                (1.4)
```

In particular,

```text
H(0)=1,
0<H(d)<=X^(-d)                    for d>0.                 (1.5)
```

These are the two features which motivated the construction: a detector
with a pole at `w=0` retains the same residue after multiplication by `H`,
while its value at an observation point `w=d` is exponentially damped.
Equation (1.4), however, also fixes every Taylor coefficient of the carrier.

## 2. Exact Poisson cancellation of the pole jet

For every integer `k>=0`, direct differentiation gives

```text
(-1)^k/k! [d^k/dw^k (exp(-tw)/w)]_(w=d)
 =d^(-k-1) exp(-td) sum_(j=0)^k (td)^j/j!.                (2.1)
```

Integrating (2.1) against `mu` proves the exact identity

```text
(-1)^k/k! [d^k/dw^k (H(w)/w)]_(w=d)
 =d^(-k-1) integral P(Poisson(td)<=k) dmu(t).              (2.2)
```

The normalized order-`k` jet of the isolated pole `1/w` is `d^(-k-1)`.
Consequently its exact survival ratio after multiplication by `H` is

```text
E_mu[P(Poisson(td)<=k)].                                  (2.3)
```

This is not an approximation and does not depend on a choice of contour.

### Theorem 2.1 -- translated-carrier pole-jet suppression

Use the high-jet scaling

```text
X=exp(lambda k/r),        lambda>1,        d>r>0,           (2.4)
```

and put `a=lambda d/r>1`.  Then

```text
0<=
 {(-1)^k/k! (H/w)^(k)(d)}/{d^(-k-1)}
 <=exp[-k(a-1-log a)].                                    (2.5)
```

Indeed, every `t` in the support satisfies `td>=ak`, and the standard
Poisson Chernoff bound gives

```text
P(Poisson(zk)<=k)<=exp[-k(z-1-log z)],       z>1.          (2.6)
```

The exponent in (2.6) increases with `z`.

Thus a meromorphic detector

```text
B(w)=c/w+G(w),                                             (2.7)
```

does retain residue `c` at zero after multiplication by `H`, but its
purported leading pole contribution at `d` is exponentially canceled by
the derivatives of the carrier.  Treating `H` as the constant `H(0)=1`
inside a high derivative is invalid.  To see the target at isolated-pole
strength one needs at least

```text
k>=d log X,                                                (2.8)
```

whereas head-tail damping requires `log X>k/r`; these inequalities are
incompatible because `d>r`.

## 3. The circular-contour form of the same obstruction

Center a Cauchy circle at the observation point `w=d` and give it radius
`R>d`.  Write

```text
u=R-d>0.                                                   (3.1)
```

If `sigma_0-u>1`, the leftmost boundary point is within the half-plane of
absolute convergence and (1.4) gives

```text
H(-u)=integral exp(tu)dmu(t)>=X^u=X^(R-d).                 (3.2)
```

To make an absolute Cauchy boundary estimate smaller than the target pole
jet, this growth would have to fit inside the localization reserve:

```text
X^(R-d)=o((R/d)^k).                                        (3.3)
```

Under (2.4), the exponent required by (3.3) is

```text
lambda(R-d)/r < log(R/d).                                  (3.4)
```

But for every `R>d`,

```text
log(R/d)<(R-d)/d<lambda(R-d)/r.                            (3.5)
```

The first inequality is `log x<x-1`; the second is `lambda d>r`.
No radius works, including the limit `R` down to `d`.

For the actual exterior logarithmic derivative, `A_X` has the retained pole
at `s=1`.  If `sigma_0-u<=1`, the translated pole at
`w=1-sigma_0` lies on or inside the circle because

```text
R>=d+sigma_0-1.                                            (3.6)
```

Thus leaving the absolute-convergence half-plane does not open an omitted
range of radii: it puts a new carrier singularity inside the localization
contour.

Theorem 2.1 and (3.5) are two views of the same conservation law.  The
first shows exact cancellation in the Taylor jet; the second locates the
corresponding boundary growth.

## 4. Reflection pays back one-sided decay

Whenever both sides are finite, Cauchy--Schwarz applied to (1.4) gives

```text
H(d)H(-d)
 =E_mu exp(-td) E_mu exp(td)>=1.                            (4.1)
```

Therefore the reflection-symmetric product `H(w)H(-w)` cannot be small at
the observation point.  A symmetric sum is dominated by its growing branch.
This rules out repairing the one-sided carrier merely by multiplying or
adding its functional-equation reflection.

Notice the scope of the theorem.  A signed factor correlated with the
auxiliary quotient could in principle cancel the boundary precisely where
`H` is large.  Equations (2.2) and (3.5) rule out bounds obtained from the
absolute carrier size; they do not assume the desired signed correlation is
impossible.

## 5. What the degree-zero functional equation actually supplies

For the self-dual exterior Artin quotient, signed degree, finite conductor,
and Gamma factors cancel.  Up to its root number it satisfies

```text
F(s)=W overline(F(1-overline(s))),       |W|=1.             (5.1)
```

The divisor involution is

```text
j(theta)=1-overline(theta),
ord_(j(theta))F=ord_theta F.                                (5.2)
```

For `A=-F'/F`, (5.1) yields

```text
A(s)=-overline(A(1-overline(s))),                           (5.3)
A^(q)(s)=(-1)^(q+1)overline(A^(q)(1-overline(s))).          (5.4)
```

Hence reflected high-jet evaluations are algebraically dependent; they are
not a second independent estimate.

More generally, a linear divisor kernel contributes

```text
sum_theta ord_theta(F)[K(theta)+K(j(theta))]                (5.5)
```

pair by pair.  Choosing `K(j(theta))=-K(theta)` annihilates every unknown
standard-factor pair, but it annihilates the selected zeta pair as well.
If the kernel retains the zeta pair, it also retains auxiliary pairs.

A location-only countermodel makes the logical point transparent.  For
real `a,b`, put

```text
U_M(s)=
 {[(s-a)(s-(1-a))]/[(s-b)(s-(1-b))]}^M.                    (5.6)
```

For nonreal points include the two conjugate factors in numerator and
denominator.  Then `U_M(1-s)=U_M(s)`, it has degree zero at infinity, and
an auxiliary pole pair just outside a selected disk can have arbitrary
multiplicity `M`.  Functional symmetry alone supplies no upper bound for
its boundary effect.  This rational example is not claimed to be an Euler
product; it separates the functional equation and location data from the
extra signed arithmetic theorem that would be needed.

## 6. The `3-4-1` inequality has the wrong pole sign

In `Re(s)>1`, write

```text
A(s)=sum_n b_n n^(-s),                 b_n>=0.              (6.1)
```

For real `sigma>1` and `tau`, coefficient positivity gives

```text
0<=3A(sigma)+4 Re A(sigma+i tau)+Re A(sigma+2i tau)
  =sum_n b_n n^(-sigma)
     2[1+cos(tau log n)]^2.                                 (6.2)
```

A zero of `F` contributes with negative residue to `A`, which is the useful
sign for excluding a selected numerator zero.  A pole `alpha` of `F` of
order `m` contributes

```text
m[3 Re 1/(sigma-alpha)
  +4 Re 1/(sigma+i tau-alpha)
  +  Re 1/(sigma+2i tau-alpha)].                            (6.3)
```

Every term in (6.3) is positive when `sigma>Re(alpha)`.  The standard-factor
zeros are exactly such poles of the exterior quotient.  They therefore
offset the selected zeta zero, and their functional-equation partners add
the same sign.  Bounding (6.3) absolutely recovers the

```text
O(log D+log(|tau|+3))                                      (6.4)
```

completed-divisor ledger from R147.  Allowing negative trigonometric weights
can center this cloud only by introducing a signed zero sum, which is the
unproved target-conditioned joint-divisor estimate in different notation.

## 7. The centered family has a deterministic common mode

The preceding gates explain why an absolute estimate fails.  There is also
a sharp obstruction to ordinary centering.  Let

```text
rho=1-delta+i gamma,
z_*=1+r+i gamma,
d=r+delta,                                                   (7.1)
```

and suppose `rho` is a zeta zero of order `e`.  For a head-deleted cubic
quotient whose standard denominator is nonzero at `rho`, define

```text
J_k(A_K)=(-1)^k A_K^(k)(z_*)/k!,
T_k=-e d^(-k-1).                                             (7.2)
```

Here `T_k` is the exact common zeta-pole contribution.  Write

```text
J_k(A_K)=T_k+R_(K,k),                                        (7.3)
```

where `R_(K,k)` contains the complete regular and remote-divisor part.
The head-tail estimate of R147 says, for
`X=exp(lambda k/r)` and `I(lambda)>log(d/r)`, that

```text
|J_k(A_K)|
 <=exp[-ck+o(k)] |T_k|,
c=I(lambda)-log(d/r)>0.                                     (7.4)
```

Consequently, field by field,

```text
R_(K,k)=-T_k+O(exp[-ck+o(k)]|T_k|).                          (7.5)
```

This identity is an important reality check.  Conditional on the common
target and the deleted Euler head, the remote part is not mean-zero noise.
It is forced to cancel the target to exponential relative accuracy.

For any convex weights `w_K>=0`, `sum_K w_K=1`, equation (7.5) gives

```text
sum_K w_K R_(K,k)
 =-T_k+O(exp[-ck+o(k)]|T_k|).                               (7.6)
```

For signed weights with `sum_K w_K=1`, forcing

```text
|sum_K w_K R_(K,k)|<=epsilon |T_k|                          (7.7)
```

requires

```text
sum_K |w_K| >=(1-epsilon)exp[ck-o(k)].                       (7.8)
```

Indeed, subtract `-T_k sum w_K=-T_k` in (7.5) and use the triangle
inequality.  Thus a signed centering scheme needs exponential condition
number and amplifies its Euler-tail, counting, and zero-density errors by
the same factor it was meant to gain.

### 7.1 The exact cubic first moment

The local Shintani mass makes the common mode visible before analytic
continuation.  At an unrestricted odd prime in the odd-squarefree cubic
family,

```text
P(p inert | p unramified)=p/[3(p+1)].                       (7.9)
```

Since the cubic exterior coefficient is three on inert powers not divisible
by three, the first main-term mean after conditioning away inert primes
through `X` is

```text
B_X(s)=sum_(p>X) [p/(p+1)]
             sum_(3 does not divide v) (log p)p^(-vs).      (7.10)
```

Writing `D_zeta=-zeta'/zeta`, one has in `Re(s)>1`

```text
B_X(s)=D_zeta(s)-D_zeta(3s)-H_X(s)-E_X(s),                  (7.11)

H_X(s)=sum_(p<=X) sum_(3 does not divide v)
                         (log p)p^(-vs),

E_X(s)=sum_(p>X) [1/(p+1)] sum_(3 does not divide v)
                         (log p)p^(-vs).                    (7.12)
```

The last series is absolutely convergent for `Re(s)>0`.  At every zeta zero
with `Re(rho)>1/2`, all terms in (7.11) except `D_zeta(s)` are regular.
Thus `B_X` has exactly the common zeta-pole residue.

It follows that:

- centering `A_K-B_X` removes the target pole exactly;
- partial centering multiplies both target and deterministic background by
  the same factor;
- centering only the auxiliary factor restores the full zeta prime head;
  and
- subtracting a principal-part-removed `B_X` preserves the target only by
  explicitly adding the bare pole jet `e d^(-k-1)`.

Variance estimates apply to `A_K-B_X`, precisely the component from which
the common pole has disappeared.  They do not justify a square-root saving
for (7.3).

## 8. Pure highest derivative is the optimal absolute filter

Nor can a finite linear combination of derivative orders improve the
remote-divisor exponent.  Let

```text
L(A)=sum_(j=0)^k b_j J_j(A),
Q(v)=sum_(j=0)^k b_j v^(j+1).                               (8.1)
```

A simple pole at `a` has response `Q((z_*-a)^(-1))`.  Normalize the target
response by

```text
Q(1/d)=1.                                                   (8.2)
```

An absolute coefficientwise estimate for divisors outside
`|a-z_*|>=R` has norm

```text
S_R=sum_(j=0)^k |b_j|R^(-j-1).                              (8.3)
```

The triangle inequality gives the sharp minimax bound

```text
1=|Q(1/d)|
 <=(R/d)^(k+1)S_R,
S_R>=(d/R)^(k+1).                                           (8.4)
```

Equality is attained by the pure highest derivative.  Hence no differential
filter of orders at most `k` improves the absolute localization condition

```text
log D=o((R/d)^k).                                           (8.5)
```

An improvement must use the actual signed auxiliary-zero locations.  It
cannot come from functional calculus alone.

## 9. Sharp remaining escape

The translated carrier does not fail because of a loose Chernoff estimate:
equation (2.2) is exact.  The functional-equation route does not fail because
the wrong reflection was chosen: equation (5.5) is pairwise.  The combined
gate is therefore

```text
positive head-tail decay
 + absolute or pairwise functional-equation control
 <= exact Poisson/Cauchy localization threshold.           (9.1)
```

There are only two ways outside (9.1) on the exterior-quotient branch:

1. prove a pointwise signed correlation between the standard-factor divisor
   and the carrier on the part of the boundary where the carrier grows; or
2. construct an exceptional head-deleting quotient whose complete absolute
   divisor complexity is already `o(X^kappa)`, `kappa<1/2`.

The first is not furnished by the functional equation, positivity, or
`3-4-1`; the second is the exceptional least-Frobenius/subentropy problem
isolated in R147--R149.  This report proves neither a fixed zeta zero-free
strip nor the existence of zeta zeros approaching one.

Successor:
[`R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md`](R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md).
