# R110 weighted trace-collision power-saving theorem

Status: unconditional coefficient-uniform theorem for the full signed box.
The balanced top-trace obstruction left open in R108 is removed by a
shared-coordinate energy argument.  For arbitrary separated complex
weights, the nonparabolic trace energy has a fixed half-power improvement
over the previous `H^(2+o(1))` coefficient-uniform endpoint:

```text
E_nonparabolic <<_epsilon H^(3/2+epsilon)
                            product_i norm(z_i)_2^2.  (0.1)
```

More precisely, for trace coefficient `lambda`, the factor in (0.1) is

```text
H^epsilon [H+H^(3/2)/sqrt(abs(lambda))].              (0.2)
```

For unit weights this gives the full eight-variable collision bound

```text
N_8(H) <<_epsilon H^(11/2+epsilon).                  (0.3)
```

Date: 2026-08-07.

## 1. Statement

Let `H>=2`, let `lambda` be a nonzero integer, and put

```text
F_lambda(h_1,h_2,h_3,h_4)
 =lambda^2 h_1h_2h_3h_4
  -lambda(h_1+h_3)(h_2+h_4)+2.                       (1.1)
```

For complex functions `z_i` supported on `[-H,H] intersect Z`, define

```text
A_T=sum_(F_lambda(h)=T) product_(i=1)^4 z_i(h_i),

E_lambda^np(z_1,z_2,z_3,z_4)
 =sum_(T!=plusminus2) abs(A_T)^2.                    (1.2)
```

**Theorem 1.1 (weighted nonparabolic trace energy).**  Fix `C>0`.
Uniformly for

```text
1<=abs(lambda)<=H^C,                                 (1.3)
```

and for every `epsilon>0`,

```text
E_lambda^np(z_1,z_2,z_3,z_4)
 <<_(C,epsilon) H^epsilon
       [H+H^(3/2)/sqrt(abs(lambda))]
       product_(i=1)^4 norm(z_i)_2^2.                (1.4)
```

In particular,

```text
E_lambda^np(z_1,z_2,z_3,z_4)
 <<_(C,epsilon) H^(3/2+epsilon)
       product_(i=1)^4 norm(z_i)_2^2.                (1.5)
```

At `lambda=1`, (1.5) is R100 equation (5.29) with `delta=1/4`.
This is a coefficient-uniform weighted theorem; it is stronger than an
unweighted point count.

For unit weights, put

```text
r_(lambda,T)(H)=#{h in [-H,H]^4: F_lambda(h)=T},
N_(8,lambda)(H)=sum_T r_(lambda,T)(H)^2.              (1.6)
```

Then:

**Corollary 1.2 (full unweighted collision energy).**  Under (1.3),

```text
N_(8,lambda)(H)
 <<_(C,epsilon) H^(5+epsilon)
       +H^(11/2+epsilon)/sqrt(abs(lambda)).           (1.7)
```

In particular `N_(8,lambda)(H)<<H^(11/2+epsilon)` uniformly, and the
canonical coefficient `lambda=1` has a saving `delta=1/2` from the old
`H^(6+o(1))` unweighted endpoint.

The exclusion `T=plusminus2` in Theorem 1.1 is essential to the divisor
factorizations.  Those two fibers are harmless for Corollary 1.2, but
arbitrary weights on them require separate analytic treatment.

## 2. Uniform fixed-pair divisor lemmas

The proof begins by extending the two R108 factorizations to general
`lambda`.

### 2.1 Adjacent pair

Fix `h_1,h_2` and put

```text
p=lambda h_1h_2-1.
```

Direct expansion gives

```text
(p lambda h_3-lambda h_1)(p h_4-h_2)
 =p^2+pT+1                                           (2.1)
```

on the fiber `F_lambda(h)=T`.

If `p!=0` and `T!=plusminus2`, the right side is nonzero.  Indeed an
integral root `p` of `X^2+TX+1` must divide `1`, and the two possibilities
give exactly `T=plusminus2`.  Every factor pair on the right of (2.1)
determines at most one pair `(h_3,h_4)`.  Since a nonempty fiber under
(1.3) has all relevant integers of polynomial height in `H`, the divisor
bound gives `H^epsilon` completions.

If `p=0`, then `lambda h_1h_2=1`.  Thus `lambda,h_1,h_2` are units, so this
case occurs only for `abs(lambda)=1` and for finitely many adjacent pairs.
The trace equation reduces to a nontrivial linear equation in
`(h_3,h_4)`, with `O(H)` solutions at a fixed `T`.

### 2.2 Opposite pair

Fix `h_1,h_3`, and write

```text
u=h_1h_3,             x=h_1+h_3.
```

Then

```text
(lambda u h_2-x)(lambda u h_4-x)
 =x^2+u(T-2)
 =h_1^2+T h_1h_3+h_3^2.                             (2.2)
```

If `u!=0` and `T!=plusminus2`, the right side is nonzero.  Otherwise
`h_1/h_3` would be a rational root of `X^2+TX+1`, which again forces
`T=plusminus2`.  Thus every fixed nonzero opposite pair also has
`H^epsilon` completions.

If a coordinate is zero, for example `h_1=0`, a nonparabolic fiber obeys

```text
lambda h_3(h_2+h_4)=2-T.                             (2.3)
```

Divisor counting in `h_3`, followed by the `O(H)` representations of a
fixed sum, gives `H^(1+epsilon)` tuples on that axis.  The other axes and
their intersections are the same by symmetry.

All bounds in this section are uniform under (1.3).  The dependence on
`C` enters only when the standard divisor estimate is applied to
polynomial-height integers.

## 3. A generalized R108 unbalanced-fiber bound

For a tuple with no zero coordinate, let `mu(h)` be the product of its two
smallest coordinate magnitudes.  Declare every tuple with a zero
coordinate unbalanced.

**Lemma 3.1 (restricted nonparabolic fiber).**  For every `0<kappa<=1`,

```text
sup_(T!=plusminus2)
 #{h in [-H,H]^4: F_lambda(h)=T,
                     mu(h)<=H^(2-kappa)}
 <<_(C,epsilon) H^(2-kappa+epsilon).                 (3.1)
```

**Proof.**  For a nonzero tuple, select the positions of its two smallest
coordinates.  There are only six choices.  For each choice the number of
signed pairs `(v,w)` with

```text
0<abs(v),abs(w)<=H,       abs(vw)<=Z:=H^(2-kappa)     (3.2)
```

is

```text
<<H+Z log(2H)<<H^(2-kappa)log(2H).                   (3.3)
```

Every pair of positions is, by the dihedral symmetry of (1.1), either an
adjacent or an opposite pair.  Sections 2.1--2.2 give `H^epsilon`
completions for each fixed pair.  The exceptional adjacent pair and all
zero-coordinate strata contribute only `H^(1+epsilon)`, which is within
(3.1) because `kappa<=1`.  QED.

There is also a height-sensitive version.  Every tuple in a `T` fiber
satisfies

```text
abs(h_1h_2h_3h_4)
 <=[abs(T-2)+4abs(lambda)H^2]/abs(lambda)^2.          (3.4)
```

Repeating the R108 smallest-pair proof with the square root of the right
side gives the corresponding `lambda`-uniform small-trace improvement.
Only Lemma 3.1 is needed below.

## 4. The unbalanced weighted energy

Fix `0<kappa<=1` and put

```text
L=H^(1-kappa).                                       (4.1)
```

Split each `A_T` into its unbalanced part, where
`mu(h)<=H^(2-kappa)`, and its balanced part.  The inequality
`abs(X+Y)^2<=2abs(X)^2+2abs(Y)^2` reduces the proof to the two separate
energies.

By fiberwise Cauchy--Schwarz and Lemma 3.1,

```text
sum_(T!=plusminus2) abs(A_(T,unbal))^2
 <<H^(2-kappa+epsilon)
   sum_h product_i abs(z_i(h_i))^2

 =H^(2-kappa+epsilon) product_i norm(z_i)_2^2.       (4.2)
```

If a tuple is not unbalanced, order its coordinate magnitudes as
`v_1<=v_2<=v_3<=v_4`.  Since

```text
v_1v_2>H^(2-kappa),       v_2<=H,
```

every coordinate in the balanced part satisfies

```text
L<abs(h_i)<=H.                                       (4.3)
```

## 5. Cauchy reduction in the balanced sector

Write

```text
x=h_1,       b=h_2,       c=h_3,       d=h_4,
Q=b+d,       Q'=b'+d'.                                (5.1)
```

Let

```text
B_(x,T)=sum_(b,c,d balanced; F_lambda(x,b,c,d)=T)
                  z_2(b)z_3(c)z_4(d).                (5.2)
```

Then Cauchy--Schwarz in `x` gives

```text
sum_(T!=plusminus2)
 abs(sum_x z_1(x)B_(x,T))^2
 <=norm(z_1)_2^2 E_shared,                           (5.3)

E_shared=sum_(x,T) abs(B_(x,T))^2.                   (5.4)
```

The right side may be enlarged by allowing all `T` in (5.4).  It counts
weighted pairs `(b,c,d),(b',c',d')` with a shared `x` and equal trace.
After dividing the trace difference by the nonzero integer `lambda`, the
exact equation is

```text
x A=B,                                               (5.5)

A=lambda(bcd-b'c'd')-(Q-Q'),
B=cQ-c'Q'.                                           (5.6)
```

We treat `A!=0` and `A=B=0` separately.

## 6. The nondegenerate shared-coordinate energy

Suppose `A!=0`.  Equation (5.5) determines `x=B/A` uniquely.  Moreover,
by (4.3),

```text
abs(A)<=abs(B)/L<=4H^2/L.                            (6.1)
```

Put `n=bcd`, `n'=b'c'd'`.  Equations (5.6) and (6.1) imply

```text
abs(n-n')
 <=[4H^2/L+4H]/abs(lambda).                          (6.2)
```

Let

```text
D=1+[4H^2/L+4H]/abs(lambda)                          (6.3)
```

and define the nonnegative product-fiber sum

```text
g(n)=sum_(bcd=n; b,c,d balanced)
          abs(z_2(b)z_3(c)z_4(d)).                   (6.4)
```

Dropping the integrality and box restrictions on the unique quotient
`x=B/A`, the absolute value of the `A!=0` contribution to (5.4) is at
most

```text
sum_(abs(n-n')<=D) g(n)g(n')
 <<D norm(g)_2^2.                                    (6.5)
```

This is the elementary `l^2` norm of convolution with an interval.

Balanced triples are nonzero, so every product `n` in (6.4) is nonzero.
The number of its ordered signed three-factor representations is
`O_epsilon(H^epsilon)`.  Cauchy--Schwarz inside each product fiber gives

```text
norm(g)_2^2
 <<_(C,epsilon) H^epsilon
       product_(i=2)^4 norm(z_i)_2^2.                (6.6)
```

Consequently the nondegenerate part of `E_shared` is

```text
<<_(C,epsilon) H^epsilon
 [1+(H^(1+kappa)+H)/abs(lambda)]
 product_(i=2)^4 norm(z_i)_2^2.                      (6.7)
```

This step works for arbitrary complex weights because absolute values were
taken only after expanding the positive energy (5.4), and (6.5)--(6.6)
are valid for their moduli.

## 7. The degenerate shared-coordinate energy

The condition `A=B=0` has an exact low-multiplicity invariant.  For a
balanced triple put

```text
P=bd,       Q=b+d,

Psi_lambda(b,c,d)=(lambda cP-Q, cQ).                 (7.1)
```

Then (5.6) shows that

```text
A=B=0
 if and only if
Psi_lambda(b,c,d)=Psi_lambda(b',c',d').              (7.2)
```

Every fiber of `Psi_lambda` has `H^epsilon` points, uniformly under
(1.3).  To prove this, fix a value `(X,Y)`.

If `Y!=0`, then `c` is a signed divisor of `Y`, after which

```text
Q=Y/c,            P=(X+Q)/(lambda c).                (7.3)
```

There are at most two ordered pairs `(b,d)` with prescribed sum `Q` and
product `P`.  Thus the fiber has divisor multiplicity.

If `Y=0`, balancedness gives `c!=0`, hence `Q=0`, `d=-b`, and

```text
X=-lambda c b^2.                                     (7.4)
```

Here `X!=0`, and the number of square-divisor representations in (7.4)
is again `H^epsilon`.  This proves

```text
sup_(X,Y) #Psi_lambda^(-1)(X,Y)
 <<_(C,epsilon) H^epsilon.                           (7.5)
```

For arbitrary complex weights, fiberwise Cauchy--Schwarz now yields

```text
sum_(X,Y)
 abs(sum_(Psi_lambda(b,c,d)=(X,Y))
             z_2(b)z_3(c)z_4(d))^2
 <<H^epsilon product_(i=2)^4 norm(z_i)_2^2.          (7.6)
```

When (7.2) holds, the two traces agree for every shared `x`.  There are
`O(H)` possible balanced values of `x`.  Therefore the degenerate part of
`E_shared` is

```text
<<_(C,epsilon) H^(1+epsilon)
       product_(i=2)^4 norm(z_i)_2^2.                (7.7)
```

This invariant replaces the longer determinant case split in the first
version of the unweighted argument and makes the complex-weight estimate
transparent.

## 8. Completion and optimization

Combining (5.3), (6.7), and (7.7), the balanced energy is

```text
E_bal
 <<_(C,epsilon) H^epsilon
 [H+1+(H^(1+kappa)+H)/abs(lambda)]
 product_(i=1)^4 norm(z_i)_2^2.                      (8.1)
```

Together with (4.2), this proves, for every `0<kappa<=1`,

```text
E_lambda^np
 <<_(C,epsilon) H^epsilon
 [H^(2-kappa)+H+H^(1+kappa)/abs(lambda)]
 product_(i=1)^4 norm(z_i)_2^2.                      (8.2)
```

The suppressed `1+H/abs(lambda)` is dominated by `H`.

If `1<=abs(lambda)<=H`, choose

```text
kappa=(1+log_H(abs(lambda)))/2.                      (8.3)
```

The first and third terms in (8.2) are then both
`H^(3/2)/sqrt(abs(lambda))`.  If `abs(lambda)>=H`, choose `kappa=1`;
all three terms are `O(H)`.  This proves (1.4).  Taking `kappa=1/2`
without using coefficient size proves the uniform form (1.5).

## 9. The parabolic fibers and Corollary 1.2

It remains only to show that unit weights at `T=plusminus2` do not spoil
the collision count.  Uniformly under (1.3),

```text
r_(lambda,2)(H)+r_(lambda,-2)(H)
 <<_(C,epsilon) H^(2+epsilon).                       (9.1)
```

Use the opposite-pair identity (2.2).  At `T=2`, its right side is
`(h_1+h_3)^2`.  If `u!=0` and `h_1+h_3!=0`, divisor counting applies.  If
`u!=0` and `h_1+h_3=0`, one of `h_2,h_4` must vanish, giving `O(H^2)`
tuples.  On the axes the original equation is
`h_3(h_2+h_4)=0` or its symmetric counterpart, also giving `O(H^2)`.

At `T=-2`, the right side of (2.2) is `(h_1-h_3)^2`.  The only new zero
case has `h_1=h_3=t!=0`.  A factor can then vanish only if

```text
lambda t h_2=2       or       lambda t h_4=2,        (9.2)
```

which allows only divisor-many `t` and one free coordinate.  The axes
obey `lambda h_3(h_2+h_4)=4` or its symmetric counterpart and are smaller.
This proves (9.1).

For unit weights, each squared `l^2` norm in Theorem 1.1 is `O(H)`, so
(1.4) bounds the nonparabolic part of (1.6) by

```text
<<H^(5+epsilon)+H^(11/2+epsilon)/sqrt(abs(lambda)).  (9.3)
```

The two parabolic fibers contribute only `H^(4+epsilon)` by (9.1).
This proves Corollary 1.2.

## 10. Meaning and remaining analytic interfaces

Theorem 1.1 closes the coefficient-uniform weighted trace-energy theorem
isolated as open in R100 (5.29) and R102 Section 9, with the explicit
value

```text
delta=1/4.                                           (10.1)
```

The mechanism combines two coefficient-specific facts which generic
trilinear or incidence estimates do not use together:

```text
unbalanced tuple
  -> a small-pair divisor saving;

balanced shared-coordinate pair, A!=0
  -> a short band between the two triple products;

balanced shared-coordinate pair, A=B=0
  -> the divisor-multiplicity invariant Psi_lambda. (10.2)
```

This is a real fixed-power arithmetic input.  It is not, alone, a theorem
about zeros of the Riemann zeta function.  The R100/R102 analytic chain
must still verify the parabolic/central terms for the transformed packets,
the actual outer-prime-dependent B-spline weights, common-factor masks,
reducible faces, seams, signed shell recombination, and the original
rectangular limiting order.  The theorem proves neither that every fixed
zero-free strip fails nor that those remaining interfaces automatically
preserve the gain.
