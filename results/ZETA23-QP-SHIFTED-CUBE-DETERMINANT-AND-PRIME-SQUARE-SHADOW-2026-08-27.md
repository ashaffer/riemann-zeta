# Shifted-cube determinant rigidity and the prime-square shadow (2026-08-27)

## 0. Binary verdict

This report treats the primitive top-coefficient slice.  The desired estimate

```text
#{(A,B,u,Delta): gcd(A,B)=1, A*u^3-B*P^3=Delta}
   << P^(9/16+o(1))
```

is **not proved** here.  The provisional `P^(5/8+o(1))` Huxley-IV floor is
not improved; its applicability to the integral cubic still requires the
source check recorded in the companion gcd/Huxley audit.

The literal raw count without `gcd(A,B)=1` is a different, stronger
quantifier: coefficient content creates all reduced scales
`P^(1/8)\ll Q\ll T`.  Nothing below proves its `P^(9/16+o(1))` bound either.

What is proved is an exact structural closeout of three tempting routes.

1. For one fixed input `u`, all solutions lie on one scalar ray
   `(A,B,Delta)=t*(a,b,d)`.  In the primitive slice `gcd(A,B)=1`, there is
   at most one solution for each `u`.
2. The determinant of two solutions at distinct inputs is strictly ordered
   and has size

   ```text
   A_1*B_2-A_2*B_1 asymp P^(1/8)*(u_2-u_1).
   ```

   Thus a genuinely bounded determinant is absent.  The determinants at
   the Huxley scale are not bounded.
3. The cross determinant of two same-`A` solutions satisfies another
   shifted-cube equation with exactly the original coefficient, input, and
   residual scales.  Its generic `abc` quality is one.  Iterating this
   determinant therefore reproduces the obstruction instead of descending.

For a prime base `P=p`, even the necessary congruence modulo `p^2` is an
exact incidence problem for Fermat quotients.  A square-root estimate for a
specific constrained Fermat-quotient sum would prove the prime-base
transition, but no such estimate is supplied by the standard Weil or
short-sum technology.

## 1. Uniform shell

Fix positive constants

```text
alpha <= beta,       lambda <= Lambda,       eta > 0,
```

and let `P` tend to infinity.  Put

```text
T=P^(9/16),                 H=P^(7/16),
T*H=P.                                                     (1.1)
```

A transition point is an integer quadruple satisfying

```text
alpha*T <= A,B <= beta*T,
lambda*P <= u <= Lambda*P,
0 < |Delta| <= eta*H,
A*u^3-B*P^3=Delta.                                        (1.2)
```

Changing the fixed shell constants affects only constants below.  The
primitive transition additionally has `gcd(A,B)=1`.

## 2. GCD normalization

Let

```text
g=gcd(u,P),             u=g*x,             P=g*y.
```

Then `gcd(x,y)=1` and (1.2) becomes

```text
g^3*(A*x^3-B*y^3)=Delta.                                  (2.1)
```

Consequently

```text
g^3 | Delta,            g <= (eta*H)^(1/3),
y >= eta^(-1/3)*P/H^(1/3) asymp P^(41/48).                (2.2)
```

In particular `y^3 >> P^(41/16) >> T`.  Thus nonzero
transition points are never hidden low-denominator exact cube rays.

The finite example

```text
61*788^3-82*714^3=-16
```

has `g=2` and reduces exactly to

```text
61*394^3-82*357^3=-2,
gcd(394,357)=gcd(61,82)=1.                                (2.3)
```

It therefore rules out any assertion that the primitive nonzero stratum is
empty merely by gcd normalization.

One immediate consequence of `y^3 >> T` is that, for fixed `(u,Delta)`,
there is at most one coefficient pair `(A,B)` in a fixed shell of diameter
`O(T)`: subtracting two such equations makes `y^3` divide the difference of
the two `A` values.

## 3. Same-input scalar-ray theorem

Suppose two transition points have the same input `u`:

```text
A_i*u^3-B_i*P^3=Delta_i,                i=1,2.             (3.1)
```

Eliminating `u^3` gives the exact identity

```text
P^3*(A_1*B_2-A_2*B_1)=A_2*Delta_1-A_1*Delta_2.            (3.2)
```

The right side has absolute value at most

```text
2*beta*eta*T*H=2*beta*eta*P=o(P^3).                       (3.3)
```

For all sufficiently large `P`, (3.2) therefore forces

```text
A_1*B_2=A_2*B_1,              A_2*Delta_1=A_1*Delta_2.    (3.4)
```

It follows that every transition point with this fixed `u` has the form

```text
(A,B,Delta)=t*(a,b,d)                                        (3.5)
```

for one primitive integer triple `(a,b,d)` and a positive integer `t`.

**Primitive-ray corollary.**  If `gcd(A,B)=1`, (3.4) forces two coefficient
pairs in the same positive shell to be identical.  Hence the primitive
transition contains at most one point for each fixed `u`.

This is a real rigidity statement, but it does not prove the target.  A
one-point-per-input configuration still has `P` available inputs, and the
abstract Huxley-floor occupancy pattern is already primitive and vertically
simple.

## 4. Ordered determinant theorem

Take two not necessarily equal-`A` transition points and assume `u_2>u_1`.
Set

```text
k=u_2-u_1,             D=A_1*B_2-A_2*B_1.
```

Substitution from (1.2) gives

```text
P^3*D
 =A_1*A_2*(u_2^3-u_1^3)+A_2*Delta_1-A_1*Delta_2
 =A_1*A_2*k*(u_1^2+u_1*u_2+u_2^2)
      +A_2*Delta_1-A_1*Delta_2.                            (4.1)
```

The shell assumptions imply the explicit bounds

```text
D >=3*alpha^2*lambda^2*T^2*k/P-2*beta*eta/P^2,
D <=3*beta^2*Lambda^2*T^2*k/P+2*beta*eta/P^2.              (4.2)
```

Therefore, for sufficiently large `P`,

```text
D>0,                    D asymp T^2*k/P=P^(1/8)*k.         (4.3)
```

In particular any two distinct inputs have

```text
|D| >> P^(1/8).                                            (4.4)
```

Thus a fixed `O(1)` determinant stratum is a singleton, but this does not
touch the critical range: for an input gap `k`, the relevant determinant is
of size `P^(1/8) k`, not `O(1)`.

There is also no hidden gain from summing this order relation.  If the
points are ordered by input and `k_i=u_(i+1)-u_i`, then (4.3) gives

```text
sum_i D_i asymp (T^2/P)*sum_i k_i <<T^2.                  (4.5)
```

This is exactly the ambient area scale of the coefficient box.  Combining
`D_i>>P^(1/8)` with (4.5) yields only `#points<<P`, the already trivial
one-per-input bound.  Thus strict determinant order is present, but its
first-moment packing inequality is scale-sharp and cannot supply the
missing `P^(7/16)` saving by itself.

## 5. Why the cross determinant does not descend

Suppose two points have the same `A`:

```text
A*u_i^3-B_i*P^3=Delta_i,                  i=1,2.
```

Eliminating `A` gives

```text
P^3*J=Delta_2*u_1^3-Delta_1*u_2^3,
J=B_1*u_2^3-B_2*u_1^3.                                  (5.1)
```

Hence

```text
|J| <=2*eta*Lambda^3*H.                                  (5.2)
```

The new equation

```text
B_1*u_2^3-B_2*u_1^3=J                                   (5.3)
```

has coefficients `B_i asymp T`, inputs `u_i asymp P`, and residual
`|J|<<H`: it is the same shifted-cube box again.  The generic radical and
term-height ledgers agree exactly:

```text
term height:       T*P^3=P^(57/16),
generic radical:  T^2*P^2*H=P^(57/16).                   (5.4)
```

Thus (5.3) is quality one.  The case `J=0` is a proportional cubic ray;
the case `J!=0` is not a lower-height problem.  This is the precise failure
of determinant iteration.

The same phenomenon occurs if two points share `u`: before applying the
strong rigidity of Section 3, direct subtraction produces

```text
(A_1-A_2)*u^3-(B_1-B_2)*P^3=Delta_1-Delta_2,              (5.5)
```

whose a priori coefficient and residual ranges are again `T` and `H`.
Equation (3.2), rather than (5.5), is the useful same-input elimination.

## 6. Exact prime-square/Fermat-quotient shadow

Let `P=p` be an odd prime.  Assume `A,|Delta|<p`.  A transition point cannot
have `p|u`, since its defining equation would then force `p^3|Delta`.
Consequently write

```text
u=s+j*p,                    1<=s<=p-1,                    (6.1)
```

where `j` ranges over a fixed finite set determined by the input shell.
For `p` not dividing `n`, write

```text
q_p(n)=(n^(p-1)-1)/p  (mod p).                            (6.2)
```

The same definition is used for signed `n`; for odd `p`,
`q_p(-n)=q_p(n)`.

For two units `x,y`, the pair of data

```text
x (mod p),                 q_p(x) (mod p)
```

determines `x` modulo `p^2`.  Indeed, if
`x/y=1+p*t (mod p^2)`, then

```text
q_p(x)-q_p(y)=-t (mod p).                                (6.3)
```

Also, direct binomial expansion gives

```text
q_p(s+j*p)=q_p(s)-j/s (mod p).                           (6.4)
```

It follows that the necessary prime-square congruence

```text
A*(s+j*p)^3=Delta (mod p^2)                              (6.5)
```

is equivalent to the two congruences

```text
A*s^3=Delta (mod p),
q_p(A)+3*q_p(s)-3*j/s=q_p(Delta) (mod p).                 (6.6)
```

This equivalence is exact.  The original transition congruence modulo
`p^3` implies (6.5), so the number of transition points is at most the
number of points in (6.6): `(s,j)` determines `u`, and then the exact
transition equation determines `B`.

For coefficient and signed-residual sets `mathcal A,mathcal D`, let `C_j`
denote the count in (6.6).  Additive orthogonality gives the exact spectral
identity

```text
C_j=(1/p)*sum_(h mod p)
 sum_(A in mathcal A, Delta in mathcal D, s in F_p^*)
  1_(A*s^3=Delta mod p)
  e_p(h*(q_p(A)+3*q_p(s)-3*j/s-q_p(Delta))).              (6.7)
```

The `h=0` contribution is at most

```text
3*|mathcal A|*|mathcal D|/p <<T*H/p<<1,                  (6.8)
```

because a nonzero cubic congruence has at most three roots.  A uniform
square-root estimate `O(p^(1/2+o(1)))` for each nonzero inner sum in (6.7)
would give

```text
C_j<<p^(1/2+o(1))<<T,                                    (6.9)
```

and hence prove the prime-base transition.

The phase in (6.7) contains Fermat quotients (equivalently, a carry from
modulo `p` to modulo `p^2`), not a bounded-degree rational function over
`F_p`; ordinary Weil bounds therefore do not apply.  For context, the
individual short-sum technology surveyed in
[Shparlinski, *Fermat quotients: Exponential sums, value set and primitive
roots*](https://arxiv.org/abs/1104.3909) becomes nontrivial only beyond the
`p^(1/2+epsilon)` threshold, while the best cited complete Heilbronn-sum
bound in [Shkredov, *On Heilbronn's exponential
sum*](https://arxiv.org/abs/1208.6124) is `p^(59/68)` up to logarithms.
Neither statement is the constrained trilinear estimate (6.7); they locate
why (6.9) is new input rather than an off-the-shelf Weil estimate.

## 7. Simultaneous linear-resonance dichotomy

There is a separate exact reduction before the shifted-cube transition.
Let `F>=1`, `C>0`, `h` be real, and suppose positive integers
`1<=a,b<=F` and integers `r,s` obey

```text
|h*F^3/(a^2*b)-r| <= C/F,
|h*F^3/(a*b^2)-s| <= C/F.                               (7.1)
```

Put

```text
d=a*r-b*s.                                                (7.2)
```

Since

```text
a*h*F^3/(a^2*b)=b*h*F^3/(a*b^2)=h*F^3/(a*b),             (7.3)
```

equations (7.1)--(7.3) give

```text
|d| <=C*(a+b)/F<=2*C,              gcd(a,b)|d.            (7.4)
```

Thus, on the `d!=0` branch, `gcd(a,b)<=2C`.

On the `d=0` branch, write

```text
a=g*A_0,       b=g*B_0,       gcd(A_0,B_0)=1.
```

Then `A_0*r=B_0*s`, so for an integer `t`,

```text
r=B_0*t,                       s=A_0*t.                   (7.5)
```

Dividing the first inequality in (7.1) by `B_0` and the
second by `A_0` yields

```text
||h*F^3/(g^3*A_0^2*B_0^2)||
 <= C/(F*max(A_0,B_0)).                                  (7.6)
```

This proves the clean dichotomy: the nonzero determinant branch has bounded
gcd, while the zero determinant branch is a one-dimensional reciprocal-cube
resonance.  In the already audited dyadic/Farey change of variables, the
diagonal condition (7.6) is the branch that clears to

```text
A*u^3-B*F^3=Delta,
A,B asymp F^(9/16),          0<|Delta|<=F^(7/16).         (7.7)
```

The algebra above isolates (7.7); it does not estimate its nonzero
solutions.

## 8. What remains genuinely open

The proved statements remove vertical multiplicity, exact proportional
aliases, and bounded coefficient determinants.  They do not remove a
primitive one-point-per-input set with nonzero cross determinants.  Such a
set is compatible with every statement above and with the abstract
`P^(5/8)` Huxley-floor incidence pattern.

The missing input is exposed in two forms.  The second is only a sufficient
prime-base shadow, not an equivalent formulation for composite `P`:

1. an arithmetic aggregation estimate for the primitive nonzero solutions
   of (1.2), saving `P^(1/16)` over Huxley; or
2. for prime bases, a new constrained Fermat-quotient incidence estimate
   strong enough to bound (6.7) by `P^(9/16+o(1))`.

Neither estimate is proved here.  Consequently this audit supplies a
sharper boundary and two exact reductions, not the sharp four-cycle bound.
