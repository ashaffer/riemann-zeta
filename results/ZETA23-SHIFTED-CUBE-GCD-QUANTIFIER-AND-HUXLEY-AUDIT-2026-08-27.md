# Shifted-cube gcd, quantifier, and Huxley audit

**Date:** 2026-08-27
**Verdict:** The displayed unreduced shifted-cube count is not the primitive
count to which Huxley's rational-point theorems apply.  For the literal raw
count, an exact content decomposition and a completely licensed application
of Huxley II give

```text
N(P) <<_epsilon P^(25/32+epsilon).                     (0.1)
```

The desired exponent is `9/16`, so (0.1) does not close the problem.  If the
original theorem of Huxley IV is first checked in its general determinant form
and is confirmed to admit the integral cubic at determinant order `d=2`, then
the same content decomposition improves (0.1) to the provisional bound

```text
N(P) <<_epsilon P^(49/64+epsilon).                     (0.2)
```

This conditional calculation does **not** give `P^(9/16)`.  The often-quoted
`P^(5/8)` is the bound for the **primitive top-denominator slice**, not for the
literal raw count.  The accessible Blomer--Schöbel proposition cannot by itself
license the cubic substitution because its printed hypothesis is
`alpha notin Z`.

## 1. Frozen literal statement

Let `P` be a sufficiently large positive integer and put

```text
T=P^(9/16),                  H=P^(7/16).                (1.1)
```

To remove every ambiguity in `asymp`, define

```text
N(P)=#{(A,B,u) in Z_(>0)^3:
        T<=A<2T, T<=B<2T, P<=u<2P,
        0<|A*u^3-B*P^3|<=H}.                            (1.2)
```

Changing any endpoint by an absolute multiplicative constant only changes
the constants below and the number of dyadic boxes by `O(1)`.  The exponent
statements are uniform in `P`.

The target under audit is

```text
N(P) <<_epsilon T*P^epsilon=P^(9/16+epsilon).           (1.3)
```

No coprimality condition occurs in (1.2).

## 2. Exact content decomposition

For a point counted by (1.2), write

```text
D=A*u^3-B*P^3,
g=gcd(A,B),              A=g*a, B=g*b, D=g*e.           (2.1)
```

Then

```text
gcd(a,b)=1,              0<|e|<=H/g.                    (2.2)
```

Since `e` is a nonzero integer, `g<=H`, and consequently

```text
a=A/g>=T/H=P^(1/8).                                  (2.3)
```

Let `Q` run through powers of two for which `[Q,2Q)` meets
`[T/H,2T)`.  If `Q<=a<2Q`, then the original dyadic restrictions imply

```text
T/(2Q)<g<2T/Q,          Q/2<b<4Q,
0<|e|<2H*Q/T.                                           (2.4)
```

Define the reduced count

```text
R(Q)=#{(a,b,u) in Z_(>0)^3:
        Q<=a<2Q, Q/2<b<4Q, P<=u<2P,
        gcd(a,b)=1,
        0<|a*u^3-b*P^3|<2H*Q/T}.                        (2.5)
```

Every raw solution maps to exactly one dyadic `Q` and one point counted by
`R(Q)`.  Conversely, a fixed reduced point in (2.5) has fewer than `2T/Q`
possible multipliers `g` that can land in (1.2).  Therefore

```text
N(P) <= 2*sum_(Q dyadic, T/(2H)<=Q<=2T) (T/Q)*R(Q).
                                                               (2.6)
```

This is the precise missing gcd ledger.  In particular, the uniform lemma

```text
R(Q) <<_epsilon Q*P^epsilon
for T/(2H)<=Q<=2T                              (SC)
```

would imply (1.3) immediately from (2.6).  It is a sufficient lemma, not an
equivalence: a weighted average version of (SC) would also suffice.

There is no harmless `P^epsilon` divisor multiplicity here.  The residual
`D` is allowed to vary.  A primitive point with residual `e` can support
`asymp T/Q` different multiples whenever `|e|<<HQ/T`; multiplying changes
`D` to `g e`.  At the bottom scale `Q=T/H`, this potential multiplicity is
`H=P^(7/16)`.

## 3. A fixed-u rigidity fact

Suppose `(A_i,B_i,u)`, `i=1,2`, are two raw solutions, with residuals `D_i`.
Eliminating `u^3` gives

```text
P^3*(A_1*B_2-A_2*B_1)=A_2*D_1-A_1*D_2.                (3.1)
```

The absolute value of the right side is less than `4TH=4P`, and hence

```text
|A_1*B_2-A_2*B_1|<4/P^2<1                             (3.2)
```

for large `P`.  Thus the determinant is zero.  All solutions over a fixed
`u` lie on a single primitive ray `(A,B)=g(a,b)`.  This verifies that (2.1)
is the genuine arithmetic multiplicity, rather than an artefact of the
argument.  It does not bound the number of admissible `u`.

## 4. An elementary cubic-root bound for R(Q)

We first record a standard prime-power fact.  For nonzero integer `c` and
positive integer `n`, let

```text
rho_3(c;n)=#{x mod n:x^3==c (mod n)}.
```

For every `epsilon>0`,

```text
rho_3(c;n) <<_epsilon n^epsilon*gcd(c,n)^(2/3).         (4.1)
```

Indeed, for `p^k || n`, if `v_p(c)=3j<k`, a solution has `x=p^j y`; the
unit cubic congruence has at most three roots and each such root has `p^(2j)`
lifts modulo `p^k`.  If `p^k|c`, there are
`p^(k-ceil(k/3))<=p^(2k/3)` roots.  The Chinese remainder theorem and
`3^omega(n)<<_epsilon n^epsilon` prove (4.1).

Fix `a` in (2.5), put

```text
h=gcd(a,P^3),             n=P^3/h.                     (4.2)
```

The congruence `a u^3==e (mod P^3)` requires `h|e`; after division it is

```text
u^3==(a/h)^(-1)*(e/h) (mod n).                          (4.3)
```

Here `gcd(a/h,n)=1`.  Moreover `a<4T` on all relevant boxes, so

```text
n>=P^3/(4T)>2P                                              (4.4)
```

for sufficiently large `P`.  Thus every root class modulo `n` contains at
most one integer `u` in `[P,2P)`.

For `X>=1`, (4.1) and divisor switching give

```text
sum_(1<=j<=X) gcd(j,n)^(2/3)
 <= X*sum_(d|n) d^(-1/3)
 <<_epsilon X*n^epsilon.                                (4.5)
```

Summing (4.3) over the nonzero `e` in (2.5), then over `a`, proves

```text
R(Q) <<_epsilon Q*(H*Q/T)*P^epsilon
     = H*Q^2*T^(-1)*P^epsilon.                          (4.6)
```

The factor `HQ/T` is at least an absolute constant on the range in (2.6),
so integer endpoint errors are absorbed in (4.6).  The restrictions on `b`
and `gcd(a,b)` can only decrease this upper bound, since `b` is uniquely
determined by `(a,u,e)`.

## 5. Fully licensed Huxley-II bound

For a point in (2.5),

```text
|(u/P)^3-b/a| < 2H/(T*P^3).                             (5.1)
```

Apply Theorem 2 of M. N. Huxley,
[*The rational points close to a curve II*](https://matwbn.icm.edu.pl/ksiazki/aa/aa93/aa9331.pdf),
to

```text
f(m)=(1+m/P)^3,             0<=m<P,                    (5.2)
```

with denominator cap `2Q`.  The derivative constants are absolute, and

```text
3*f''(m)^2-2*f'(m)*f'''(m)
 =72*(1+m/P)^2/P^4 asymp P^(-4),                        (5.3)
```

so every hypothesis of that theorem is met.  Its approximation parameter
may be taken as

```text
delta=8H*Q^2/(T*P^3).                                  (5.4)
```

For `Q<=2T`, both `delta<<P^(-2)` and `delta*P<<P^(-1)`.
Huxley's theorem consequently gives

```text
R(Q)
 <<_epsilon [P*delta^(1/4)+(P*Q^2*(delta*P+1))^(1/3)]P^epsilon
 <<_epsilon [P^(7/32)*Q^(1/2)+P^(1/3)*Q^(2/3)]P^epsilon
 <<_epsilon P^(1/3+epsilon)*Q^(2/3).                   (5.5)
```

The last term dominates the first throughout the relevant range.

Combining (4.6) and (5.5) in (2.6) yields

```text
N(P)
 <<_epsilon sum_Q min(H*Q,
                       T*P^(1/3)*Q^(-1/3))*P^epsilon.   (5.6)
```

The increasing and decreasing terms balance at

```text
Q_0=(T*P^(1/3)/H)^(3/4)=P^(11/32),                     (5.7)
```

which lies between `T/H=P^(1/8)` and `T=P^(9/16)`.
Dyadic summation is geometric on both sides of `Q_0`, and hence

```text
N(P) <<_epsilon H*Q_0*P^epsilon
     =P^(25/32+epsilon).                                (5.8)
```

This proves (0.1) for every integer `P`, with no primality or
squarefreeness assumption.

For comparison, if one inserts the missing condition `gcd(A,B)=1` into
(1.2), only the top denominator `Q asymp T` remains.  Formula (5.5) then
gives the fully licensed primitive bound

```text
N_prim(P) <<_epsilon P^(17/24+epsilon),                 (5.9)
```

not `P^(5/8+epsilon)`.

## 6. Precisely fenced Huxley-IV calculation

This section is conditional on the following source check:

> **IV-admissibility check.** Verify from Theorem 1 of Huxley,
> *The rational points close to a curve IV*, Bonner Math. Schriften 360
> (2003), that its determinant-order `d=2` statement applies to
> `f(m)=(1+m/P)^3` and gives the four terms encoded by `H_2`.

The commonly cited accessible formulation, Proposition 1 of
[Blomer--Schöbel, *Twins of powerful numbers*](https://doi.org/10.7169/facm/2013.49.2.12),
assumes explicitly that the exponent `alpha` is **not an integer**.  It is
therefore not, by itself, a valid citation for `alpha=3`.

There is good reason to expect the original determinant formulation to be
applicable.  In Huxley,
[*The rational points close to a curve III*](https://www.impan.pl/shop/publication/transaction/download/product/83110),
the relevant order-`d=2` determinants for the cubic are

```text
D_(3,s)(f)=(f'''/3!)^s=P^(-3s),       s=1,2,3,          (6.1)
```

because their matrices are triangular.  Thus the cubic is nondegenerate at
order two; the blanket `alpha notin Z` condition in the quoted corollary is
stronger than what (6.1) suggests is needed for this single value of `d`.
Nevertheless, expectation is not a substitute for checking the original
Theorem 1, so the rest of this section is not used in the unconditional
verdict.

Assuming the IV-admissibility check, substitute

```text
M=P,       mathcal T=Q^2,
Delta asymp H*Q^2/(T*P^3),       s=2.                  (6.2)
```

The four terms in `P H_2(P,Q^2,Delta)` are

```text
P^(2/5)*Q^(2/5),
P^(23/80)*Q^(3/5),
P^(3/8)*Q^(2/5),
P^(-31/144)*Q.                                         (6.3)
```

For `P^(1/8)<<Q<<P^(9/16)`, the first term dominates all the others.  Thus

```text
R(Q) <<_epsilon P^(2/5+epsilon)*Q^(2/5).               (6.4)
```

Combining (6.4), still conditionally, with the unconditional root bound
(4.6) gives

```text
N(P)
 <<_epsilon sum_Q min(H*Q,
                       T*P^(2/5)*Q^(-3/5))*P^epsilon.   (6.5)
```

The balance is

```text
Q_1=(T*P^(2/5)/H)^(5/8)=P^(21/64),                     (6.6)
```

and (0.2) follows because

```text
H*Q_1=P^(7/16+21/64)=P^(49/64).                        (6.7)
```

At the primitive top slice `Q=T`, (6.4) instead reads

```text
N_prim(P) <<_epsilon P^(2/5)*T^(2/5)*P^epsilon
          =P^(5/8+epsilon).                            (6.8)
```

This is the origin of the `1/16` gap

```text
5/8-9/16=1/16.                                         (6.9)
```

It is not an exponent for the unreduced count (1.2).  Even granting (6.4),
the raw exponent furnished by this decomposition is `49/64`, whose gap over
the desired `9/16` is `13/64`.

## 7. The explicit closing lemma

For the literal raw problem, the clean local statement that closes the
argument is (SC):

> For every dyadic `Q` with `T/(2H)<=Q<=2T`, the number of reduced triples
> in (2.5) is `O_epsilon(Q P^epsilon)`.

More generally, the weaker weighted form is enough:

```text
sum_Q R(Q)/Q <<_epsilon P^epsilon.                      (7.1)
```

The current licensed inputs give, at their worst transition
`Q=P^(11/32)`, only

```text
R(Q) <<P^(9/16+epsilon),
whereas (SC) asks for P^(11/32+epsilon).                 (7.2)
```

If Huxley IV is licensed, its combination with (4.6) moves the worst scale
to `Q=P^(21/64)` but still gives `R(Q)<<P^(17/32+epsilon)`, versus the
required `P^(21/64+epsilon)`.

For the primitive formulation `gcd(A,B)=1`, only (SC) at `Q asymp T` is
needed.  There the desired `R(T)<<T P^epsilon` is exactly the sharp
transition statement, and the provisionally licensed Huxley-IV count misses
it by the factor `P^(1/16)`.

No unconditional proof of (SC), and no arithmetic counterexample to it, was
found.  A square-sieve, determinant-method, or endpoint-energy argument would
have to save over the number of small-denominator cubic residue classes, not
merely reprove Farey spacing or the pointwise cube-root bound (4.6).

## 8. Logical status relative to the four-cycle problem

The local report currently uses language suggesting that (1.3) is a
necessary shifted-cube transition.  What is actually documented is weaker:

1. a positive diagonal incidence estimate is necessary for one proposed
   weighted-HSM route;
2. the shifted-cube box appears as a component of a Farey/Huxley upper-bound
   decomposition of that incidence;
3. no reverse map is given showing that a large raw count (1.2) creates a
   large original diagonal incidence with the required weights and constants;
4. no implication is proved from the shifted-cube estimate alone to sharp
   spacing, weighted HSM, or the four-cycle bound.

Accordingly, (1.3) should be labelled a **sufficient local gate in one proof
strategy**, not an equivalent or independently necessary consequence of the
four-cycle theorem, unless the missing reverse reduction is supplied.

The report must also decide which quantifier is intended:

```text
primitive transition: gcd(A,B)=1, top Q asymp T;
literal raw transition: no gcd condition, all T/H<<Q<<T with multipliers.
```

Conflating these two statements is exactly what turns the conditional
primitive exponent `5/8` into an unsupported assertion about the raw count.
