# R173 matrix arithmetic lift and causal-cofactor gate

## Status

The `GL_2` identity of R171 can be coupled to the two-layer determinant
amplifier without losing any of the three formal properties which made the
amplifier useful:

```text
entrywise head deletion,
exact retention of the common zeta divisor,
signed H -> H^2 support amplification through a positive majorant. (0.1)
```

There is a clean arithmetic normal form.  Let `G` and `F=GR` be two
head-deleted scalar channels with coefficientwise positive majorants, let
`t>0`, and put

```text
T=F-G=G(R-1),                 c=(G^2-G)/t.              (0.2)

     [ G    T ]                    [ G^2   -T ]
X_0= [        ],             X_1= [          ].          (0.3)
     [ c   G^2]                    [ -c     G ]
```

Every entry of `X_j-I` is a Dirichlet tail supported beyond `H`; the
off-diagonal entries are scalar multiples of differences of scalar
channels.  At every
common zero of `G` and `F`, both matrices vanish.  Direct multiplication
gives

```text
I-(X_1-I)(X_0-I)=G C I_2,
C=1+G(G-1){(R-1)/t-1}.                                  (0.4)
```

Consequently the complete cofactor is zero-free whenever

```text
sup_(partial Omega)|G(G-1)| |(R-1)/t-1|<1.              (0.5)
```

This is a conditional arithmetic lift theorem, not a construction of the
required `R`.  It reduces the matrix completion problem to one explicit
small-constant interpolation problem for an optional Euler ratio:

```text
R-1=t(1+e),             sup |G(G-1)e|<1.                (0.6)
```

on the full localization contour, together with a coefficientwise
majorant for `F-G` proportional to `t`.

The last two requirements are incompatible if "lift" means uniform
approximation of the literal R171 block matrices.  Let

```text
s_*=1+r+i gamma,
T(s)=sum_(n>H)a(n)n^(-s).                               (0.6a)
```

If `T(s_*)=t[1+o(1)]`, as approximation of the upper entry `tG` requires,
then its positive majorant satisfies

```text
T_hat(1+r/2)>=H^(r/2)|T(s_*)|
                 =t H^(r/2+o(1)).                      (0.6b)
```

For the standard head-deleted Euler channel,
`(G^2-G)/t` has majorant
`t^(-1)H^(-r/2+o(1))`.  Their positive closed two-cycle is therefore
`H^(o(1))`, not `H^(-r+o(1))`; after differentiation it is not even
power-small.  The scale `t` cancels.  Thus the literal `GL_2` block
approximation has formal `H^2` support but loses the analytic suppression
which the high-jet argument needs.  This is a decisive causal obstruction
to that lift, independent of prime rounding and of the transition hull.

One can weaken the goal and require only the scalar output (0.4) to stay
safe.  Then `T` need not imitate `tG` on the right cap, because the error is
multiplied by `G-1` there.  The majorant no-go no longer applies directly,
but this tapered construction is exactly a new global cofactor/image-control
problem; the matrix identity has not solved it.

The two known perturbative choices now form a sharp dichotomy.  If the
normalized late tail `D/t` has a tame coefficient majorant, it tends to zero
on the right `q`-disk; asking it to tend to one on the left outside arc so
that `C->1` returns R168's filled-hull obstruction.  If `D/t` is instead
made constant-like through the filled domain, Theorem 3.4 says its necessary
coefficient growth erases the `H^2` majorant gain.  Any remaining matrix
escape must therefore be nonperturbative and phase-sensitive: it must prove
the cofactor zero-free without either uniform relative interpolation to the
`GI_2` template or an absolute positive-majorant estimate.

The reduction passes the formal support test even for complex or signed
coefficients.  A carrier-affine matrix channel

```text
X_j=sum_alpha C_(j,alpha)F_alpha,       sum_alpha C_(j,alpha)=I,
F_alpha=Z A_alpha=1+U_alpha             (0.7)
```

satisfies

```text
det[I-(X_1-I)(X_0-I)]
 =Z^2 det[M_0+M_1-ZM_1M_0].                            (0.8)
```

The logarithmic derivative is supported beyond `H^2`; its coefficient
moduli are dominated term by term by the nonnegative closed-walk series
formed from the absolute coefficient majorants.  The same statement gives
`H^q` for `q` cyclic layers.

The existing actual-prime theorem does not yet supply (0.5).  If

```text
t=H^(-A),                  sup |G(G-1)|<=H^(Lambda),     (0.9)
```

then it is enough to approximate the small constant in the logarithm of
`R` with absolute error

```text
sup |Log R-log(1+t)|=o(H^(-A-Lambda)).                 (0.10)
```

This is a statement about `Log R`; the equivalent entrywise statement is
`R-1-t=o(H^(-A-Lambda))` while `t` is small.

R163's actual-prime discretization can do this only inside the explicit
window

```text
A+Lambda < c_prime,             c_prime<sigma_0-7/12,   (0.11)
```

after also paying the coefficient norm of the continuum construction.
No report proves that this window is nonempty on a completed localization
contour.  If only the much weaker raw bound

```text
sup |G|<=exp(H^(lambda+o(1)))                            (0.12)
```

is available, (0.5) asks for `exp(-H^lambda)` relative accuracy.  The
known delayed approximation then needs horizon `asymp H^lambda`, hence an
outer prime cutoff `H exp(O(H^lambda))`; the standard left-boundary Euler
majorant grows to `exp(O(H^lambda))` in its *logarithm*.  This is a
precision--growth feedback loop.  It proves that the presently available
worst-case bounds do not close, but not that a specially cancelled optional
Euler ratio cannot close.

There is no dependence on `min_(partial Omega)|G|` in the sharp test.
The common factor `G` is exact and is divided out before Rouche is applied;
only the maximum in (0.5) amplifies the ratio error.  A direct perturbation
of the unfactored `2 x 2` determinant obscures this and incorrectly demands
accuracy proportional to the smallest boundary value of `G`.

The full-contour polynomial hull is also not, by itself, a no-go for this
particular interpolation.  A tiny constant is globally holomorphic on the
filled contour.  Delayed polynomials can approximate it with coefficient
cost `exp(CM)`, and choosing `t<=exp(-CM)` pays that cost.  R168's hull
obstruction applies to a nonzero-left/zero-right limiting profile; after
the present scaling the unnormalised target tends to zero everywhere.
But Theorem 3.4 shows that the coefficient cost cannot be ignored: for
literal block approximation it destroys the positive-majorant power gain
before actual-prime rounding is reached.  Tapering the target on the right
avoids that lower bound only by returning to R168's transition geometry and
the global cofactor problem.

Finally, the exact causal replacement can be scalarized.  Writing

```text
T=t(G-1)+D
```

turns (0.4) into

```text
C=1+(G-1)(D/t-1).                                      (0.13)
```

The noncausal choice `D=t` gives `C=1`; the causal choice `D=0` gives the
old fixed-value factor `2-G`.  Choosing

```text
D/t=1+[exp(1-G)-1]/(G-1)                               (0.14)
```

gives `C=exp(1-G)` and output `G exp(1-G)I_2`, exactly
R153's `q=2` unique-zero transform.  It fails the stronger entrywise carrier
condition because the upper off-diagonal entry does not vanish at `G=0`.
The endpoint-normalized choice

```text
Phi(G)=exp(G-G^2),
D/t=1+[Phi(G)-1]/(G-1)                                 (0.15)
```

does make every entry causal and every matrix entry vanish at `G=0`; its
output is `G Phi(G)I_2`.  Thus an exact analytic lift exists, but it pays
the same essential-singularity and value-plane boundary bill as the scalar
unique-zero transform.

Genuine noncommutativity cannot remove that bill in a global entire
functional calculus.  If all layer matrices equal `I+O((G-1))` at the
head, a `q`-layer determinant is `1+O((G-1)^q)`.  If it has only the
retained `G`-zero and an entire zero-free cofactor, its scalar determinant
is necessarily

```text
G^m exp h(G),
h(G)=-m log G+O((G-1)^q)       near G=1.                (0.16)
```

In particular `h` is nonconstant.  This is R153's truncated-log
conservation law at determinant level, independent of whether the matrices
commute.  Noncommutativity can still help on a bounded `G`-image, where a
polynomial determinant cofactor may place its zeros outside the image; that
is precisely the remaining global image-control problem, not a global
entire escape.

```text
carrier-affine exact divisor factorization                 THEOREM
complex/signed positive-majorant H -> H^2 support          THEOREM
q-layer positive-majorant H -> H^q support                 THEOREM
explicit optional-ratio GL_2 cofactor formula              THEOREM
Rouche test independent of min |G|                         THEOREM
full-contour delayed approximation of a tiny constant      THEOREM
exact endpoint-normalized causal entire matrix lift         THEOREM
global noncommutative entire-transform escape              CLOSED
literal full-contour R171 block lift with positive majorant IMPOSSIBLE
fixed-power tapered-output precision window                 CONDITIONAL
optional-Euler tapered coefficient majorant                 OPEN
full-contour determinant-only realization                   OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching Re(s)=1                                  NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md),
[`R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md`](R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md),
[`R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md`](R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md),
and
[`R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md`](R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md).

## 1. Carrier-affine matrix channels

Work first with formal Dirichlet series in a right half-plane.  Let

```text
F_alpha=Z A_alpha=1+U_alpha,
supp U_alpha subset {n:n>H}.                             (1.1)
```

The coefficients of the tails may be nonnegative, as for the head-deleted
Euler channels, although the first algebraic statement does not require
this.  Let `C_(j,alpha)` be constant `d x d` complex matrices satisfying

```text
sum_alpha C_(j,alpha)=I_d                               (1.2)
```

and define

```text
X_j=sum_alpha C_(j,alpha)F_alpha,
M_j=sum_alpha C_(j,alpha)A_alpha.                       (1.3)
```

Then

```text
X_j-I=sum_alpha C_(j,alpha)U_alpha,
X_j=Z M_j.                                               (1.4)
```

Thus every entry of `X_j-I` is head-deleted, while every entry of `X_j`
vanishes at every retained zero of `Z`.  An off-diagonal entry has total
scalar weight zero and is therefore a finite sum of differences of scalar
channels.  A diagonal entry is one base channel plus such differences.

### Theorem 1.1 -- exact two-layer divisor

Put

```text
K=I-(X_1-I)(X_0-I),                   P=det K.           (1.5)
```

Then

```text
K=Z[M_0+M_1-ZM_1M_0],
P=Z^d det[M_0+M_1-ZM_1M_0].                            (1.6)
```

#### Proof

Expanding the product in (1.5) gives

```text
K=X_0+X_1-X_1X_0.                                      (1.7)
```

Substitution of (1.4) proves (1.6).  QED.

For `d=2`, the target multiplicity is twice the multiplicity of `Z` if the
last determinant in (1.6) is nonzero there.  More usefully, if a boundary
comparison proves that `P` and an exact target with divisor `Z^2` have the
same total zero count, (1.6) shows at once that the cofactor has no extra
zero anywhere inside.  No separate pointwise transversality calculation is
then needed.

## 2. Signed closed walks and the positive majorant

Make the `2d x 2d` bipartite adjacency matrix

```text
       [ 0    X_1-I ]
A=     [              ].                                (2.1)
       [ X_0-I   0   ]
```

The block determinant identity gives

```text
det(I-A)=det[I-(X_1-I)(X_0-I)]=P.                       (2.2)
```

For each scalar entry of `A`, replace every Dirichlet coefficient by its
absolute value and call the resulting nonnegative matrix series `A_hat`.

### Theorem 2.1 -- signed majorant

Where the majorant converges absolutely and has spectral radius less than
one,

```text
P'/P=sum_(k>=0)tr[A^k(-A')]                             (2.3)
```

has no coefficient below or at `H^2`, and every coefficient modulus is at
most the corresponding coefficient of

```text
sum_(k>=0)tr[A_hat^k(-A_hat')].                         (2.4)
```

For a cyclic `q`-layer graph the same assertions hold with `H^2` replaced
by `H^q`.

#### Proof

Jacobi's formula and the geometric matrix series prove (2.3).  Every trace
monomial is a closed directed walk.  Bipartiteness forces its length to be
at least two, and a cyclic `q`-layer graph forces length at least `q`.
Every edge coefficient has integer support strictly beyond `H`, so the
convolution index of a length-`ell` walk is strictly beyond `H^ell`.

Taking absolute values term by term replaces every edge coefficient by its
majorant and every differentiated coefficient by the same absolute
coefficient times `log n`.  This is exactly a term in (2.4).  Absolute
convergence justifies the rearrangement.  QED.

This theorem is stronger than a support statement: signs and complex phases
do not invalidate the right-circle estimate provided the positive
majorant, rather than the signed function, has the required size.

Suppose, for example, that every ordinary edge satisfies on the right
circle

```text
U_hat+(-U_hat')<=H^(-r/2+o(1)).                         (2.5)
```

If constant matrix coefficients have size at most `H^omega`, the crude
two-layer bound is

```text
|P'/P|<=H^(-r+2omega+o(1)).                             (2.6)
```

The scaling in the explicit construction below is better treated
cyclewise.  An edge of majorant size `t H^(-r/2)` paired with its reciprocal
scaled edge `t^(-1)H^(-r/2)` still costs only `H^(-r)` around the closed
walk.  If only the crude bound `H^(-r/2)` is known for the first edge, the
same cycle loses the factor `t^(-1)`.  This is why proportional
coefficientwise control of an optional-channel difference is a genuine
condition, not cosmetic bookkeeping.

## 3. The exact `GL_2` arithmetic normal form

Let

```text
G=1+U,
F=GR=1+V                                                    (3.1)
```

be two scalar head-deleted channels and let `t` be a nonzero scalar.  Set

```text
T=F-G=G(R-1),                 c=(G^2-G)/t                (3.2)
```

and define the matrices in (0.3).

### Theorem 3.1 -- scalar cofactor formula

The entries of `X_j-I` are tails supported beyond `H`.  If `G` and `F`
vanish at a retained point, every entry of both `X_j` vanishes there.
Moreover,

```text
I-(X_1-I)(X_0-I)=G C I_2,                               (3.3)

C=1+G-G^2+(G-1)T/t
 =1+G(G-1){(R-1)/t-1}.                                  (3.4)
```

Consequently

```text
P=det[I-(X_1-I)(X_0-I)]=G^2 C^2.                        (3.5)
```

#### Proof

The diagonal tails are `G-1` and

```text
G^2-1=2U+U^2.                                           (3.6)
```

The lower off-diagonal tail is `GU/t`, a scalar multiple of the difference
`G^2-G`, and the upper one is the difference of the two head-one channels
in (3.1).  At a common zero, (3.2) gives
`T=c=0`, proving the entrywise divisor assertion.

Write `a=G-1`.  Multiplication of the two matrices `X_j-I` makes both
off-diagonal entries cancel.  Each diagonal entry of the product is

```text
a(G^2-1)-Tc.                                             (3.7)
```

Subtracting from one and using `c=Ga/t` gives (3.3)--(3.4).
Equation (3.5) follows.  QED.

### Corollary 3.2 -- conditional arithmetic lift

Let `Omega` be a bounded localization domain on whose boundary `G` is
nonzero, and assume `C` is holomorphic on a neighborhood of
`closure(Omega)`.  If

```text
eta:=sup_(partial Omega)
       |G(G-1)| |(R-1)/t-1|<1,                          (3.8)
```

then `C` has no zero in `Omega`, and `P` has exactly twice the divisor of
`G` there.

Indeed, (3.4) gives `|C-1|<1` on the boundary, so Rouche compares `C` with
one.  Formula (3.5) supplies the exact divisor.

Notice what is absent from (3.8): no lower bound for `|G|` is required.
The exact common carrier is removed before the comparison.  If

```text
M_G=sup_(partial Omega)|G(G-1)|,                         (3.9)
```

the precise approximation demand is simply

```text
sup_(partial Omega)|R-1-t|<t/M_G.                       (3.10)
```

### Corollary 3.3 -- right-circle majorant

Assume `G-1` has the standard positive right-circle bound (2.5), and that
the coefficientwise majorant of the channel difference satisfies

```text
T_hat+(-T_hat')<=t H^(-r/2+o(1)).                       (3.11)
```

Then the majorant in Theorem 2.1 gives

```text
|P'/P|<=H^(-r+o(1))                                    (3.12)
```

on that circle.  The factors `t` and `t^(-1)` cancel on every off-diagonal
two-cycle.  Without (3.11), the crude majorant loses `t^(-1)`.

The condition (3.11) looks natural but cannot hold when `T` uniformly
approximates the literal R171 entry `tG` on a filled localization domain.

### Theorem 3.4 -- a causal constant edge erases the power gain

Let

```text
s_*=1+r+i gamma,                    r>0,                 (3.13)
T(s)=sum_(n>H)a(n)n^(-s)                                  (3.14)
```

converge absolutely in `Re(s)>=1+r/2`, and define

```text
T_hat(sigma)=sum_(n>H)|a(n)|n^(-sigma).                 (3.15)
```

If

```text
|T(s_*)|>=c_0 t                                         (3.16)
```

for fixed `c_0>0`, then

```text
T_hat(1+r/2)>=c_0 t H^(r/2).                            (3.17)
```

Suppose in addition that `G=1+U` has nonnegative coefficients and the
nontrivial first-tail mass

```text
U(1+r/2)>=H^(-r/2-o(1)),                                (3.18)
```

as does the standard head-deleted Euler channel `G=E_H`, and put

```text
c=(G^2-G)/t.                                             (3.19)
```

Then

```text
c(1+r/2)>=H^(-r/2-o(1))/t,                              (3.20)

T_hat(1+r/2)c(1+r/2)>=H^(-o(1)).                        (3.21)
```

The positive closed-walk majorant for the two-cycle containing `T` and
`c` is consequently not bounded by any fixed negative power of `H` after
logarithmic differentiation.

#### Proof

For every `n>H`,

```text
n^(-1-r/2)>=H^(r/2)n^(-1-r).                            (3.22)
```

Therefore

```text
T_hat(1+r/2)
 >=H^(r/2)sum_(n>H)|a(n)|n^(-1-r)
 >=H^(r/2)|T(1+r+i gamma)|,                             (3.23)
```

which proves (3.17).

Write `G=1+U`.  Positivity gives

```text
c=(U+U^2)/t>=U/t                                        (3.24)
```

on the real axis.  Assumption (3.18) now gives (3.20)--(3.21).  For the
standard channel the required assumption follows from the prime terms of
`E_H-1` and the prime number theorem:

```text
U(1+r/2)>=sum_(p>H)p^(-1-r/2)
          =H^(-r/2-o(1)).                               (3.25)
```

(more precisely there is a factor comparable to `1/log H`).

The length-two term of the positive closed-walk series contains the
derivative of the product `T_hat c`.  Every convolution index in that
product exceeds `H^2`, so its negative derivative is at least
`2 log H` times its value.  It is therefore `H^(-o(1))`, and cannot satisfy
the `H^(-r+o(1))` estimate required of a genuine two-step amplifier.  QED.

If the actual block matrices approximate the R171 templates uniformly on
the boundary of a filled domain containing `s_*`, the maximum principle
gives (3.16), since `G(s_*)=1+o(1)`.  The theorem is unchanged if `t` is
made arbitrarily small: its factor in (3.17) is canceled by `t^(-1)` in
(3.19).  A shared sparse rounding of the two scalar channels cannot evade
the deterministic `ell^1` inequality (3.23).

The theorem does **not** follow merely from the output condition (3.8).
On the right cap, `G-1` is small, so (3.8) permits `T` to be much smaller
than `tG`.  Such a tapered edge gives up literal block approximation and
returns to the global cofactor problem.

The theorem allows `G^2` as a scalar channel.  It is again a positive
head-deleted Dirichlet series, though its retained zeta multiplicity is
two rather than one.  The matrix factorization, not the individual entry,
determines the final multiplicity in (3.5).

## 4. Exact causality versus contour approximation

The original R171 identity uses the noncausal upper entry `tG`, whose
Dirichlet constant is `t`.  Keep all other entries fixed and replace it by
an arbitrary tail `T`.  Write

```text
T=t(G-1)+D.                                              (4.1)
```

Then (3.4) becomes the exact identity

```text
C=1+(G-1)(D/t-1).                                      (4.2)
```

This exposes all of the elementary choices:

```text
D=t        gives C=1,        but D has a forbidden head;
D=0        gives C=2-G,      the old fixed-value divisor;
D/t=1+e   gives C=1+(G-1)e.                             (4.3)
```

Thus replacing the constant by a causal tail is not a free perturbation.
It is exactly a scalar product-hypersurface problem, and the error is
amplified by `G-1`.

There is also an exact formal obstruction.  Suppose the unperturbed R171
blocks were realized literally and every entry of `X_j-I` were supported
beyond `H`.  Their two off-diagonal entries have product

```text
(Gt)[G(G-1)/t]=G^2(G-1).                                (4.4)
```

The left side would be supported beyond `H^2`.  Since `G^2` has constant
one and no support at or below `H`, comparison of coefficients up to
`H^2` would force

```text
supp(G-1) subset {n:n>H^2}.                             (4.5)
```

For the standard cutoff channel the first prime after `H` is below `2H`
for large `H`, so (4.5) is false.  Exact realization would therefore assume
the desired two-step deletion in advance.  Approximation on a bounded
contour is essential; literal equality cannot provide a new causal gain.

## 5. Why the transition hull does not kill a tiny constant

The preceding contour problem asks a tail to imitate the *small* constant
`t`, not to tend to a nonzero function on the left while tending to zero
on the right.  The distinction can be made quantitative in the `q`-plane.

### Theorem 5.1 -- delayed approximation of a tiny constant

Let `K` be the closure of a bounded analytic Jordan domain in `C`, assume

```text
0 notin K,                    C\K connected,             (5.1)
```

and fix finitely many interpolation points and jet orders in `K`.  There
are constants `c,C>0` and an integer `d>=1` such that, for every sufficiently
large integer `M`, a polynomial

```text
P_M(q)=sum_(n=M)^((1+d)M)b_(n,M)q^n                    (5.2)
```

satisfies

```text
sup_K|P_M-1|<=exp(-cM),
sum_n|b_(n,M)|<=exp(CM),                                (5.3)
```

and `P_M-1` has all the prescribed zero jets.

Consequently, if

```text
|t_M|<=exp[-(C+epsilon)M],                              (5.4)
```

then `D_M=t_MP_M` has strictly slack coefficients, is a delayed polynomial,
and approximates `t_M` with relative error `exp(-cM)` on the *whole filled
domain* `K`.

#### Proof

The function `q^(-M)` is holomorphic on a fixed neighborhood of `K`.
Bernstein--Walsh approximation on that neighborhood gives a polynomial
`Q_M` of degree at most `dM` such that

```text
sup_K|q^(-M)-Q_M|
 <=exp(-c_1M) max_K|q|^(-M)                             (5.5)
```

after increasing the fixed `d`.  Put `P_M=q^M Q_M`.  This proves the first
part of (5.3).  Polynomial norm equivalence on the fixed nonpolar compactum,
together with degree `O(M)`, bounds the monomial coefficient norm by
`exp(CM)`.

Approximate first on a slightly larger fixed neighborhood.  Cauchy's
inequality makes the errors of the finitely many prescribed derivatives
exponentially small.  Subtract a fixed Hermite interpolation polynomial
with those errors as its data before multiplying by `q^M`.  This imposes
the jets, changes neither the degree scale nor the exponential estimates,
and retains the factor `q^M`.  Scaling by (5.4) proves the last assertion.
QED.

Take `K` to be the image of the filled localization domain under

```text
q=exp[h(1-s)]                                             (5.6)
```

with `h` small enough to make the map injective.  Then (5.1) holds.  The
theorem shows that full-contour approximation of a globally compatible
small constant has no polynomial-hull obstruction.  After division by
`t_M`, the coefficients grow like `exp(CM)` and the normalized polynomials
need not tend to zero on the unit disk.  Without division by `t_M`, both the
target and the polynomial tend to zero everywhere.  Neither sequence has
the incompatible limiting boundary data used in R168.

The theorem is analytic, not yet arithmetic.  Turning (5.2) into actual
prime logarithms invokes the density normalization and rounding errors of
R163.  Those errors are absolute, while (3.10) is relative to `t`.
Moreover, the coefficient norm `exp(CM)` is not harmless for the amplifier:
Theorem 3.4 shows that, when the polynomial is used to approximate the
literal constant edge on the full filled domain, exactly this causal
coefficient growth erases the positive-majorant power gain.

### Corollary 5.2 -- hull-or-majorant dichotomy

Return to (4.2) and put

```text
Q_H=D_H/t_H,
C_H=1+(G_H-1)(Q_H-1).                                  (5.7)
```

Suppose a perturbative construction tries to make `C_H->1` on a completed
localization contour.  There are two cases covered by the present methods.

1. If the normalized late coefficients are tame enough that

   ```text
   Q_H->0
   ```

   on a nonempty open right `q`-disk, while `G_H-1` stays bounded away from
   zero on a left outside arc, then `C_H->1` forces `Q_H->1` on that arc.
   R168's polynomial-hull theorem forbids these two boundary limits on the
   completed contour.

2. If `Q_H->1` through the filled domain instead, then the corresponding
   causal upper edge is constant-like at the right center.  Theorem 3.4
   forces its absolute coefficient majorant to pay `H^(r/2)`, and the
   reciprocal lower edge cancels the scale `t_H`.  The closed two-cycle is
   not power-small.

Thus neither tame cutoff interpolation nor uniform constant interpolation
turns the R171 identity into a positive-majorant amplifier.  The statement
does not exclude a cofactor which stays zero-free by winding or signed phase
cancellation while remaining far from one.  Such an argument would no
longer be a perturbation of the exact `GI_2` template.

## 6. The fixed-power precision window

Suppose

```text
t=H^(-A),
M_G<=H^(Lambda+o(1)).                                   (6.1)
```

If a logarithmic optional-prime control gives

```text
L=Log R=log(1+t)+O(H^(-c))                              (6.2)
```

uniformly on the completed contour, then, for small `t`,

```text
(R-1)/t-1=O(H^(A-c)).                                   (6.3)
```

Condition (3.8) follows whenever

```text
c>A+Lambda.                                             (6.4)
```

R163's actual-prime block lift supplies only

```text
c<sigma_0-7/12                                          (6.5)
```

on a compact set with left edge `sigma_0`.  In addition, Theorem 5.1 and
the exact logarithmic-density normalization impose a lower bound

```text
A>A_geom                                                (6.6)
```

to pay the coefficient norm and the decay forced by the rightmost part of
the contour.  The present tools can therefore close the matrix perturbation
only if the explicit window

```text
A_geom+Lambda < sigma_0-7/12                            (6.7)
```

is nonempty.  No existing report establishes (6.7) for a full localization
domain.  It is a useful fail-fast target: improving approximation without
writing down all three exponents does not advance the matrix lift.

There is a second coefficient condition.  If `F` and `G` are constructed
by two independently rounded optional-prime patterns, pointwise closeness
of `F-G` to `tG` does not imply the proportional majorant (3.11).  A crude
absolute majorant by `F+G` loses `H^A` in (3.12).  More decisively,
Theorem 3.4 proves that **no** coupling, sparse or otherwise, can give
(3.11) while approximating the literal constant-like edge throughout the
filled domain.  Its deterministic `ell^1` inequality already applies
before prime discretization.

The precision window (6.7) is therefore relevant only to a tapered-output
construction in which `T` is allowed to be much smaller than `tG` on the
right cap.  Such a construction must verify (3.8) directly and establish a
new cyclewise majorant; it is not an arithmetic lift of the R171 block
template.

### The log-polynomial feedback

If instead only

```text
M_G<=exp(H^(lambda+o(1)))                               (6.8)
```

is known, (3.10) requires accuracy

```text
t exp[-H^(lambda+o(1))].                                (6.9)
```

An exponential-accuracy delayed approximation uses degree and time horizon
`N` of order `H^lambda`.  The corresponding prime cutoff is

```text
Y=H exp(O(H^lambda)).                                   (6.10)
```

At a fixed left penetration `a>0`, the standard absolute Euler estimate is

```text
sum_(p<=Y)p^(-(1-a))=Y^(a+o(1))
 =exp[O(aH^lambda)].                                    (6.11)
```

This quantity bounds the *logarithm* of the new Euler multiplier.  Feeding
it back into (6.9) demands a still smaller, essentially double-exponential
accuracy.  Thus the available worst-case majorants do not form a closed
bootstrap.

This is not an impossibility theorem.  Equation (6.11) is an absolute
majorant and may be vastly larger than a deliberately cancelled signed
channel on the localization boundary.  What is proved is narrower and
decisive for the present method: log-polynomial outer control plus generic
delayed approximation cannot certify the matrix Rouche step.  One needs raw
fixed-power conditioning as in (6.1), or a new signed estimate replacing
(6.11).

## 7. Exact causal scalarizations

Formula (4.2) can be solved exactly.  Let `Phi` be a zero-free entire
function with `Phi(1)=1` and put

```text
d_Phi(G)=1+[Phi(G)-1]/(G-1),
D=t d_Phi(G),
T=t[(G-1)+d_Phi(G)].                                    (7.1)
```

The apparent quotient is removable at `G=1`, and (4.2) gives

```text
C=Phi(G).                                                (7.2)
```

The constant term of `D`, equivalently of `T`, vanishes exactly when

```text
d_Phi(1)=1+Phi'(1)=0.                                   (7.3)
```

The upper entry `T` vanishes at every `G=0` point exactly when

```text
-1+d_Phi(0)=0,
equivalently Phi(0)=1.                                  (7.4)
```

### 7.1 The R153 transform

Take

```text
Phi(G)=exp(1-G).                                        (7.5)
```

Then (7.3) holds and

```text
G C=G exp(1-G),
(GC)'/(GC)=(1-G)G'/G.                                  (7.6)
```

The logarithmic derivative begins at the two-tail level.  This is precisely
R153's `q=2` unique-zero transform.  But `Phi(0)=e`, so (7.4) fails: the
upper off-diagonal entry does not vanish at the retained zero.  The output
divisor is correct, but the stronger edgewise carrier condition is lost.

### 7.2 Endpoint-normalized carrier transform

Take instead

```text
Phi(G)=exp(G-G^2).                                      (7.7)
```

Then

```text
Phi(0)=Phi(1)=1,             Phi'(1)=-1.                (7.8)
```

Equations (7.3)--(7.4) show that every entry of `X_j-I` is a tail and every
entry of `X_j` vanishes when `G=0`.  The exact output is

```text
I-(X_1-I)(X_0-I)=G exp(G-G^2) I_2.                     (7.9)
```

Moreover

```text
d/ds log[G exp(G-G^2)]
 =[1/G+1-2G]G'
 =[-3(G-1)+O((G-1)^2)]G',                              (7.10)
```

so its formal Dirichlet support is strictly beyond `H^2`.  Expanding the
entire functions in the positive tail `U=G-1` also gives a coefficientwise
absolute majorant on every right half-plane of absolute convergence.

This is an exact analytic and formal causal lift.  It is not an actual
finite Euler/prime lift.  The composition `exp(G-G^2)` turns poles or large
boundary values of `G` into the same essential-singularity and
`exp(O(|G|^2))` boundary bill already identified in R153.  Splitting its
signed Taylor coefficients into positive and negative pieces makes formal
positive Dirichlet channels, but does not turn them into finite optional
Euler products with a controlled completed divisor ledger.

## 8. Why noncommutativity cannot erase the global entire bill

The preceding scalarization might appear to be an artifact of the symmetric
`2 x 2` ansatz.  At determinant level it is forced.

### Theorem 8.1 -- determinant truncated-log conservation

Let `q` be even and let `X_0(z),...,X_(q-1)(z)` be entire `d x d` matrix
functions satisfying

```text
X_j(0)=0,                    X_j(1)=I_d.                 (8.1)
```

Put

```text
K(z)=I-product_(j=q-1)^0[X_j(z)-I],
P(z)=det K(z).                                             (8.2)
```

Assume that the zero at `z=0` has multiplicity `m>=1` and that `P` has no
other zero in the plane.  Then

```text
P(z)=z^m exp h(z)                                        (8.3)
```

for an entire function `h`, and near `z=1`,

```text
h(z)=-m Log z+O((z-1)^q).                               (8.4)
```

In particular `h` is nonconstant.  For `q=2`,

```text
h'(1)=-m.                                                (8.5)
```

#### Proof

Since every `X_j-I=O(z-1)` at `z=1`, the product in (8.2) is
`O((z-1)^q)`.  Hence

```text
P(z)=1+O((z-1)^q).                                      (8.6)
```

The zero hypothesis and the Weierstrass logarithm on the simply connected
plane give (8.3).  Taking a local logarithm of (8.3) at `z=1` and using
(8.6) yields

```text
m Log z+h(z)=O((z-1)^q),                                (8.7)
```

which is (8.4).  Since `m>0`, its first derivative gives (8.5), so `h`
cannot be constant.  QED.

The first `q-1` Taylor coefficients in (8.4) are exactly the truncated-log
counterterms in R153.  The theorem used only the scalar determinant and the
head contact; the matrices need not commute.  Thus a globally entire,
zero-free matrix cofactor cannot retain the support gap with constant
determinant or with no value-plane growth.  Noncommutativity changes the
factorization of the cofactor, not its scalar determinant bill.

On a bounded localization image, the cofactor determinant need only be
zero-free on that image.  A polynomial determinant may put all its zeros
outside it, and `GL_d` flexibility can help arrange the matrix entries.
Theorem 8.1 does not close that possibility.  It says that extending such a
construction to a global entire identity merely returns the R153
truncated-log transform.

## 9. Decision

The matrix escape is neither dead nor a proof of a strip.

It survives the exact arithmetic bookkeeping in a stronger form than was
known in R171: carrier-affine blocks retain the zeta divisor automatically,
signed coefficients retain `H^2` or `H^q` support through a positive
closed-walk majorant, and the explicit optional-ratio form (3.1)--(3.5)
turns the full matrix completion into one scalar relative approximation.

It also has four sharp limitations.

1. Exact use of the noncausal constant assumes the `H^2` support gain in
   advance.
2. Literal causal approximation of that constant edge forces an absolute
   coefficient majorant which erases the `H^2` right-circle saving.  Shared
   sparse rounding cannot alter this deterministic inequality.
3. Tapering the edge on the right avoids that particular lower bound, but
   then the construction is no longer an approximation of the R171 blocks.
   Perturbative tapering faces the hull-or-majorant dichotomy of
   Corollary 5.2 and the unverified precision window (6.7).
4. A global entire exact solution is just the scalar truncated-log
   unique-zero transform at determinant level and inherits its boundary
   bill.

The most concrete next theorem is therefore:

> Construct a carrier-affine matrix template with no constant-like
> zero-length edge, and prove its collective determinant cofactor zero-free
> on the completed localization domain by a phase-sensitive signed estimate
> which does not replace every edge by its absolute coefficient majorant.

The literal R171 missing-constant route is closed under the positive-
majorant high-jet strategy.  Arbitrary noncommutative templates and signed
cofactor estimates are not closed.  Consequently neither existence nor
nonexistence of a fixed zeta zero-free strip follows.
