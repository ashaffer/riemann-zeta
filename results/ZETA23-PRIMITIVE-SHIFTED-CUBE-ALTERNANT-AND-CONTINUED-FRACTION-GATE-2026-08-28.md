# Primitive shifted cubes: alternant rigidity and the continued-fraction gate

**Date:** 2026-08-28  
**Binary verdict:** the target primitive aggregation estimate is not proved.
There is, however, a new rigorous local result: the rational-quadratic
zero-determinant branch in the six-point equal-`A` alternant is impossible.
Consequently every six solutions with one common `A` have input span
`>>P^(39/80)`.  This strengthens the local rigidity but does not control
solutions whose coefficient labels recur only at long distances.

The global problem has an exact continued-fraction form.  Every transition
point creates a convergent to the rational cube `(u/g)^3/(P/g)^3` whose next
partial quotient is `>>P^2`.  Bounding the number of these giant-quotient
events by `P^(9/16+epsilon)` is a precise remaining fixed-denominator lemma.

## 1. Frozen statement

Fix positive shell constants and put

```text
T=P^(9/16),             H=P^(7/16),             T*H=P.
```

Let `mathcal S(P)` consist of integer quadruples satisfying

```text
A,B~T,                 u~P,
gcd(A,B)=1,
A*u^3-B*P^3=Delta,     0<|Delta|<=H.              (1.1)
```

The desired theorem is

```text
#mathcal S(P) <<_epsilon T*P^epsilon.               (PSC)
```

The shell constants only affect implied constants below.

For one fixed `u`, all coefficient pairs in (1.1) lie on one scalar ray;
primitivity therefore leaves at most one.  This one-point-per-input fact is
immediate on eliminating `u^3` from two points:

```text
P^3*(A_1*B_2-A_2*B_1)=A_2*Delta_1-A_1*Delta_2,
```

whose right side is `O(T*H)=O(P)=o(P^3)`.  The coefficient determinant is
therefore zero, and two positive primitive pairs on one ray coincide.  The
resulting one-point-per-input bound is only `P`.

## 2. Pair spacing with one common coefficient

Fix `A~T`, and let

```text
(u_i,B_i,Delta_i),              i=1,2,
```

be distinct solutions with this `A`, ordered so that `u_2>u_1`.  For large
`P`, monotonicity in (1.1) gives `B_2>B_1`.  Subtraction gives

```text
A*(u_2^3-u_1^3)-(B_2-B_1)*P^3=Delta_2-Delta_1.     (2.1)
```

Since `B_2-B_1>=1`, `u_i~P`, and the right side is `O(H)`, (2.1) implies

```text
u_2-u_1 >> P/A >> P^(7/16)=H.                      (2.2)
```

Write

```text
G=c*P/A
```

with a sufficiently small shell-dependent `c>0`.  Every pair of distinct
equal-`A` inputs is separated by at least `G`.

## 3. The six-point determinant

Take six equal-`A` solutions with

```text
u_1<...<u_6
```

and form the integer determinant

```text
D=det(1,u,u^2,B,u*B,u^2*B),                         (3.1)
```

where the six solutions are the rows.  Put

```text
v_j=(u_i^j)_(i=1)^6,       e_j=(Delta_i*u_i^j)_(i=1)^6,
V=det(v_0,...,v_5)=product_(i<j)(u_j-u_i)>0.         (3.2)
```

Scaling the last three columns in (3.1) by `P^3` and using
`P^3*B=A*u^3-Delta` gives the exact identity

```text
P^9*D
 =det(v_0,v_1,v_2,A*v_3-e_0,A*v_4-e_1,A*v_5-e_2)
 =A^3*V+E_1+E_2+E_3,                                (3.3)
```

where `E_j` is the sum of terms containing exactly `j` residual columns.

### 3.1 Relative error bounds

Expanding a one-residual determinant along that column leaves a five-row
generalized Vandermonde.  In the three possible cases, the residual power
of `u` and the Schur factor have total degree at most two.  Hence

```text
|E_1| <= C*A^2*H*P^2*V/G^5.                         (3.4)
```

For two residual columns, expand along two rows.  Their `2 by 2` minor
contains the corresponding row gap.  The complementary four-row
generalized Vandermonde, together with that minor, has at most a `P^2`
Schur factor.  The full Vandermonde has eight additional cross gaps, so

```text
|E_2| <= C*A*H^2*P^2*V/G^8.                         (3.5)
```

For all three residual columns, their three-row minor is

```text
product Delta_i * Vandermonde(three selected u_i),
```

and the complementary minor is the ordinary three-row Vandermonde.  There
are nine cross gaps.  Thus

```text
|E_3| <= C*H^3*V/G^9.                               (3.6)
```

All constants here are absolute after the shells are frozen.  These bounds
can also be checked directly by Laplace expansion.  For example, in a
one-error term the ratio of the five-row Vandermonde omitting row `r` to
`V` is exactly

```text
1/product_(s!=r)|u_r-u_s| <=G^(-5).
```

Divide (3.4)--(3.6) by the main term `A^3*V`, and use `G>>P/A`.  One obtains

```text
|E_1|/(A^3*V) << H*A^4/P^3  =P^(-5/16),
|E_2|/(A^3*V) << H^2*A^6/P^6=P^(-7/4),
|E_3|/(A^3*V) << H^3*A^6/P^9=P^(-69/16).            (3.7)
```

Therefore the combined error in (3.3) is smaller than `A^3*V/2` for all
sufficiently large `P`.  In particular,

```text
D!=0.                                                (3.8)
```

This removes the previously surviving rational-quadratic packet
alternative; it is not an assumption about generic points.

## 4. A proved six-point span

Let

```text
X=u_6-u_1.
```

The same Laplace expansions, now bounding every gap above by `X`, give

```text
|P^9*D|
 << A^3*X^15+A^2*H*P^2*X^10
       +A*H^2*P^2*X^7+H^3*X^6.                     (4.1)
```

Since `D` is a nonzero integer, the left side is at least `P^9`.  The first
term in (4.1) reaches that scale at

```text
X=(P^9/A^3)^(1/15)=P^(39/80).                       (4.2)
```

At this value the other three terms are smaller than `P^9` by fixed powers
of `P`.  It follows that

```text
u_6-u_1 >> P^(39/80).                               (4.3)
```

Thus every interval of this length contains at most five solutions with
one fixed `A`.  This is a genuine strengthening of the earlier alternative
"nonzero determinant or rational-quadratic packet."

It still does not imply `(PSC)`.  Equal-`A` labels may recur at gaps much
larger than `P^(39/80)`.  In particular, the critical Huxley-floor model in
which a label recurs only after distance `P^(15/16)` obeys (4.3) with ample
room.  Local equal-label alternants cannot see that global recurrence.

## 5. Why the obvious higher alternants do not iterate for free

For `m>=1`, put

```text
n=3*(m+1),           J=3*m*(m+1)/2,
```

and form the `n by n` evaluation determinant with columns

```text
u^i*B^j,             0<=i<=2, 0<=j<=m.             (5.1)
```

After multiplying the column `(i,j)` by `P^(3j)`, the residual-free term
has exponents

```text
i+3j=0,1,...,n-1.
```

Consequently there is the exact expansion

```text
P^(3J)*det(5.1)=A^J*V_n + terms containing Delta,   (5.2)
```

where `V_n` is the `n`-row Vandermonde.  If the main term alone governed
integrality, the nonzero-determinant span would be

```text
X_m=(P^3/A)^(m/(3m+2)),                              (5.3)
```

whose exponent tends to `13/16`.

The first residual term explains why this is not an automatic hierarchy.
Laplace expansion exactly as in Section 3 gives the relative estimate

```text
first-error/main
 << (H/A)*P^(n-4)/G^(n-1)
 << H*A^(n-2)/P^3.                                  (5.4)
```

For `n=6`, (5.4) is `P^(-5/16)` and proves (3.8).  Already for `n=9`, its
power is

```text
P^(22/16),                                           (5.5)
```

so pair spacing alone no longer prevents an error cancellation.  A higher
alternant proof would need new spacing for residual wedges, not merely more
columns.  Moreover, even a fixed-`A` span tending to `P^(13/16)` would not
by itself aggregate the different `A` labels at the target scale.

## 6. Exact continued-fraction reduction

Return to one solution of (1.1).  Set

```text
g=gcd(u,P),       u=g*x,       P=g*y,       gcd(x,y)=1.
```

Then

```text
g^3 | Delta,
delta=Delta/g^3!=0,
A*x^3-B*y^3=delta,
|delta|<=H/g^3.                                     (6.1)
```

In particular, `g<=H^(1/3)` and `y>=P/H^(1/3)=P^(41/48)`.
The rational approximation is

```text
|x^3/y^3-B/A|=|delta|/(A*y^3).                      (6.2)
```

Since

```text
2*A*|delta|/y^3 <= C*T*H/P^3 <<P^(-2),             (6.3)
```

Legendre's criterion shows that the reduced fraction `B/A` is a regular
continued-fraction convergent of the reduced rational cube `x^3/y^3`.

Let `q_next` be the denominator of the next convergent.  The standard
convergent inequalities and (6.2) give

```text
y^3/|delta|-A < q_next <= y^3/|delta|.              (6.4)
```

The cancellation of `g^3` is important:

```text
y^3/|delta|=P^3/|Delta| >=P^3/H=P^(41/16).          (6.5)
```

If `a_next` is the next partial quotient, then

```text
a_next >= q_next/A-1 >> P^3/(T*H)=P^2.             (6.6)
```

Thus every primitive shifted-cube transition produces a partial quotient
of size at least a constant times `P^2`, immediately after a convergent
whose numerator and denominator are both of order `T`.

There is also an exact continuant form.  If `B'/A'` is the preceding
convergent, then, with the appropriate common sign, there are integers
`R>0` and `S=|delta|` such that

```text
x^3=B*R+B'*S,
y^3=A*R+A'*S,
|A*B'-B*A'|=1,
R/S >>P^2.                                          (6.7)
```

Conversely, a packet (6.7) with the frozen shells and
`S<=H/g^3` gives (6.1).  The transition is therefore a cube-valued,
unimodular continuant packet with an exceptionally long next quotient.

## 7. Precise remaining aggregation lemma

The following fixed-denominator statement is sufficient for `(PSC)`.

> **Giant-quotient cube lemma `(GQC)`.**  Uniformly in `P`, sum over divisors
> `g|P` with `g<=H^(1/3)`, put `y=P/g`.  The number of integers `x~y`,
> `gcd(x,y)=1`, for which `x^3/y^3` has a convergent `B/A` with
> `A,B~T` and next partial quotient `a_next>>P^2` is
>
> ```text
> <<_epsilon T*P^epsilon.                            (GQC)
> ```

The divisor sum costs only `P^o(1)`.  By (6.1)--(6.6), `(GQC)` implies the
primitive shifted-cube target.  Up to fixed constants in the partial
quotient threshold, (6.4) also shows that `(GQC)` is the continued-fraction
form of the original residual restriction, rather than a generic
Diophantine-approximation reformulation.

Neither the classical fact that a large partial quotient is rare on
average nor the one-point-per-`u` theorem proves `(GQC)` for the sparse
fixed-denominator sequence of rational cubes.  The prime-denominator
specialization contains the previously isolated Fermat-quotient carry
condition modulo `P^2`; ordinary Weil bounds do not estimate that carry.

## 8. Pair-energy reorganization

Because the primitive slice contains at most one point over each `u`, its
ordered off-diagonal pair count is

```text
#mathcal S(P)*(#mathcal S(P)-1).                    (8.1)
```

Thus a bound `<<T^2*P^epsilon` for all transition pairs is, up to the
diagonal term, equivalent to `(PSC)` rather than a formally weaker route.
The determinant equation nevertheless identifies the exact arithmetic loss
in the most direct factorization attempt.

Take two points, order them by `u_2>u_1`, and put

```text
k=u_2-u_1,
Q=u_1^2+u_1*u_2+u_2^2=3*u_1^2+3*k*u_1+k^2,
D=A_1*B_2-A_2*B_1,
E=A_2*Delta_1-A_1*Delta_2.                           (8.2)
```

Then exactly

```text
P^3*D=A_1*A_2*k*Q+E,               |E|<<T*H=P.      (8.3)
```

Moreover `D>0` and, on `k~K`,

```text
D~T^2*K/P.                                           (8.4)
```

For fixed `(D,E)`, equation (8.3) has only `P^o(1)` candidate pairs.
Indeed, `A_1,A_2,k,Q` form a four-factor decomposition of `P^3D-E`;
after those factors are fixed, the identity

```text
12*Q-3*k^2=(6*u_1+3*k)^2                            (8.5)
```

determines `u_1`, and the two endpoint equations determine and check
`B_i,Delta_i`.  The divisor bound is uniform because all integers involved
have polynomial size in `P`.

But the box of possible invariants on this dyadic gap has size

```text
#D * #E <<(T^2*K/P)*P=T^2*K.                        (8.6)
```

This loses the full factor `K`.  The elementary one-point-per-input count
is `O(P*K)` on a dyadic `k`-block, which is smaller than (8.6) because
`T^2>P`; it is within the desired `T^2` only for

```text
K<=T^2/P=P^(1/8).                                   (8.7)
```

Consequently all gaps through `P^(1/8)` are harmless, but neither the
factorization nor the six-point equal-`A` alternant controls the aggregate
of the longer gaps.  A precise pair form of the missing theorem is

```text
#{(D,E) occupied by transition pairs with k~K}
   <<T^2*P^epsilon                                  (PE_K)
```

uniformly for `P^(1/8)<K<=P`.  By the fixed-`(D,E)` divisor statement and
dyadic summation, `(PE_K)` would prove the pair-energy target.  Compared
with (8.6), it asks for a factor-`K` saving from the endpoint condition

```text
E=A_2*Delta_1-A_1*Delta_2,                          (8.8)
```

not from further factorization of `P^3D-E`.  The equal-`A` alternant only
addresses a thin diagonal among these arbitrary-label pairs, so its new
zero-branch exclusion does not supply this saving.

## 9. Status

```text
one primitive point for each fixed u:                    PROVED;
equal-A pair gap >>P/A:                                  PROVED;
six-point rational-quadratic zero branch:                 IMPOSSIBLE;
six equal-A inputs span >>P^(39/80):                      PROVED;
naive higher-alternant iteration:                         BLOCKED BY (5.4);
continued-fraction giant quotient >>P^2:                 PROVED;
giant-quotient cube aggregation (GQC):                    OPEN;
fixed-(D,E) transition-pair multiplicity:                 P^o(1), PROVED;
pair gaps K<=P^(1/8):                                     WITHIN T^2;
long-gap occupied-invariant estimate (PE_K):              OPEN;
primitive shifted-cube count <<T*P^epsilon:              NOT PROVED;
sharp four-cycle bound:                                  NOT PROVED.
```
