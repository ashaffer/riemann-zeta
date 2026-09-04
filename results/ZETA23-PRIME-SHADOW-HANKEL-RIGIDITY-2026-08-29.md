# Finite prime-shadow Hankel rigidity above the cubic threshold

**Date:** 2026-08-29

**Status:** project analytic theorem; targeted prior-art search completed; independent
publication review and formalization remain.

**Evidence class:** the proof below is elementary once finite Hankel
rank--recurrence equivalence is granted.  The literature attribution is to
Elkies for that algebraic interface.  No claim of priority is made.

**Trust base:** unique factorization in `Z`, the rational-root theorem,
Chebyshev's lower bound for the prime theta function, and the finite
Hankel-rank interface cited in Section 5.  The overlap argument in Section 1
also proves the needed order-two instance directly.  No numerical
computation is used.

## 0. Claim of record

### Theorem PHR2 -- finite near-geometric prime-block rigidity

Fix constants

```text
0<c<C,                 K>0,                 A>3/2.
```

There are constants `B=B(c,C,K,A)` and `Y_0=Y_0(c,C,K,A)` such that the
following holds.  Let `Y>=Y_0`, let `r>0`, and let

```text
L>=1 be an integer,
p_0,p_1,...,p_(L-1)
```

be pairwise-distinct primes satisfying, for every `0<=j<L`,

```text
cY <= p_j <= CY,
|p_j-Yr^j| <= K Y^(1-A).                              (0.1)
```

Then

```text
L <= B log(2Y).                                       (0.2)
```

### Exact scope

The hypothesis is a **pointwise** shadow of one rank-one geometric sequence.
It is not an averaged error estimate.  The terms must be pairwise-distinct
ordinary primes in one fixed multiplicative shell.  The exponent threshold
`A>3/2` is strict.

### Nonclaims

PHR2 does not prove:

- the sharp four-cycle bound;
- `LTRAD`, `LTRAD_P`, `DPA_P`, or a zero-free strip;
- that a small one-sided trigonometric floor creates the pointwise shadow
  `(0.1)`;
- an order-`m` prime-rigidity theorem for `m>=3`; or
- that `A>3/2` is necessary for the conclusion.  It is the critical threshold
  delivered by this cubic determinant bound, not a proved sharp threshold
  for the theorem itself.

## 1. Cubic integer collapse

The assertion is immediate after increasing `B` when `L<=4`, so assume
`L>=5`.  Put

```text
g_j=Yr^j,                   e_j=p_j-g_j,
E=K Y^(1-A).
```

Form the `3 x (L-2)` Hankel matrix

```text
H=(p_(i+j))_(0<=i<=2, 0<=j<=L-3).                    (1.1)
```

The reference column

```text
(g_j,g_(j+1),g_(j+2))^T = Yr^j(1,r,r^2)^T            (1.2)
```

is proportional to every other reference column.  In the multilinear
expansion of any `3 x 3` minor of `H`, the term with no error columns and all
terms with only one error column vanish: at least two untouched reference
columns remain proportional.  Since the shell bounds make every reference
entry `O(Y)`, every minor is

```text
O(YE^2+E^3)
 =O(Y^(3-2A)+Y^(3-3A))
 =o(1).                                                (1.3)
```

Each minor is an integer, so all of them vanish for sufficiently large `Y`.
Consequently

```text
rank(H)<=2.                                            (1.4)
```

For every available `j`, the adjacent Cassini minor

```text
C_j=p_j p_(j+2)-p_(j+1)^2                             (1.5)
```

is nonzero.  Indeed, equality would say that a product of two distinct
primes is the square of a third; unique factorization would force all three
primes to coincide.  Thus `rank(H)=2`.  Finite Hankel rank gives one common
rational recurrence

```text
p_(j+2)=s p_(j+1)+t p_j                 (0<=j<L-2)    (1.6)
```

with `s,t in Q`.

This last step is the classical finite rank--recurrence interface.  It can
also be proved locally: each consecutive cubic minor gives a unique
order-two recurrence because `C_j!=0`; two adjacent blocks share two
equations whose determinant is `C_(j+1)`, so their coefficients agree.

## 2. A rational order-two recurrence cannot carry many shell primes

The Cassini minors obey the exact identity

```text
C_(j+1)=-t C_j.                                       (2.1)
```

Write `t=a/b` in lowest terms with `b>0`.  The bounds

```text
1<=|C_j|<=2C^2Y^2                                    (2.2)
```

and `(2.1)` have three consequences.

1. `t=0` is impossible because it would give `C_(j+1)=0`.
2. If `b>=2`, integrality of `C_j=(-a/b)^j C_0` gives
   `b^j | C_0`, hence `2^j<=2C^2Y^2`.
3. If `b=1` and `|a|>=2`, then
   `2^j<=|C_j|<=2C^2Y^2`.

In either nonunit case `L=O_(C)(log Y)`, which already proves the desired
conclusion.  It remains only to consider

```text
t in {1,-1}.                                          (2.3)
```

Write `s=u/v` in lowest terms.  Multiplying `(1.6)` by `v` shows that `v`
divides every interior prime.  Two distinct interior primes force `v=1`.
Thus `s` is an integer; moreover

```text
|s|<=2C/c.                                            (2.4)
```

Only finitely many recurrence pairs `(s,t)` remain.

For every hyperbolic pair, let `lambda,mu` be the characteristic roots,
ordered so that `|lambda|>1>|mu|`.  Then

```text
U=(p_1-mu p_0)/(lambda-mu),
V=(lambda p_0-p_1)/(lambda-mu),
p_j=U lambda^j+V mu^j.                                (2.5)
```

The integer

```text
Q=p_1^2-s p_0p_1-t p_0^2
  =(p_1-lambda p_0)(p_1-mu p_0)                       (2.6)
```

is nonzero: otherwise the rational number `p_1/p_0` would be a hyperbolic
rational root of a monic polynomial with constant term `+1` or `-1`, which
the rational-root theorem excludes.  Hence `|Q|>=1`.  One factor in `(2.6)`
is `O(Y)`, so `(2.5)` gives

```text
|U| >>_(c,C,s,t) Y^(-1),             |V| <<_(c,C,s,t)Y.
```

Since every `p_j=O(Y)` and `|mu|^j<=1`, the triangle inequality now gives

```text
|lambda|^j << Y^2,
```

and again `j=O(log Y)`.

For completeness, the nonhyperbolic cases are explicit.  If `t=1,s=0`,
then `p_(j+2)=p_j`, contradicting pairwise distinctness.  If `t=-1`, then
`s=-2,-1,0` make `p_2` negative; `s=1` gives
`p_2=p_1-p_0` and `p_3=-p_0`; and `s=2` is the single surviving,
potentially long parabolic recurrence

```text
(s,t)=(2,-1),             p_(j+2)-p_(j+1)
                           =p_(j+1)-p_j.              (2.7)
```

Thus the only possibly long case is an arithmetic progression of primes.

## 3. A shell arithmetic progression of primes is logarithmically short

Write the remaining sequence as

```text
p_j=p_0+jd,                  d!=0.                    (3.1)
```

Let

```text
K_0=min(L,floor(cY/2)).                                (3.2)
```

For each prime `ell<=K_0`, if `ell` does not divide `d`, then the first
`ell` terms in `(3.1)` run through every residue modulo `ell`.  One is
divisible by `ell`; but it is a prime larger than `ell`, a contradiction.
Therefore

```text
prod_(ell prime, ell<=K_0) ell  divides |d|.           (3.3)
```

The shell also gives

```text
(K_0-1)|d| <= (C-c)Y.                                 (3.4)
```

Taking logarithms and using Chebyshev's bound
`theta(x)=sum_(ell<=x)log ell >> x` first rules out
`K_0=floor(cY/2)` for large `Y`, and then gives

```text
K_0=L=O_(c,C)(log Y).                                 (3.5)
```

This completes the proof of PHR2.

## 4. The literal Fejer-transfer corollary

Suppose a future inverse step produces a contiguous block of pairwise-
distinct primes in fixed shells `cY<=p_j<=CY`, for which, with an implied
constant fixed uniformly in `j` and `Y`,

```text
log(p_j/Y)=jh+delta_j,      |delta_j|<<mathcal_B^(-1), (4.1)
mathcal_B=Y^A,              A=50/33.
```

With `r=exp(h)`, exponentiation inside a fixed shell gives

```text
p_j=Yr^j+O(Y/mathcal_B)=Yr^j+O(Y^(-17/33)).            (4.2)
```

Since `50/33>3/2`, PHR2 forces the block length to be `O(log Y)`.  Thus a
superlogarithmic pointwise near-AP block in logarithmic prime coordinates is
impossible at the project resolution.

This is useful as a **branch terminator**.  It does not supply the missing
inverse step from an aggregate one-sided Fourier floor to `(4.1)`.  In
particular, Bloom--Green gives an AP-rich subset only after integer
quantization and equal-weight control; it does not provide the whole-support
pointwise shadow needed here.

## 5. Prior art and novelty boundary

The 2026-08-29 search covered finite Hankel rank and recurrence, small
integer Hankel determinants, approximate/rounded geometric sequences, Pisot
recurrences, and prime-valued linear recurrences, including searches for the
statement and its contrapositive.  The closest located sources are recorded
below.

The finite algebraic step is classical.  Elkies defines a degree-`m` finite
recursion and identifies it with rank at most `m` of the corresponding
finite Hankel matrix; the corollary after Proposition 1 identifies minimal
recursion degree with Hankel rank under the half-length condition:

- N. D. Elkies, [*On Finite Sequences Satisfying Linear
  Recursions*](https://nyjm.albany.edu/nyjm/j/2002/8-5.pdf), New York J.
  Math. 8 (2002), 85--97; see equations (1)--(2), Proposition 1, and the
  following corollary.

Infinite Kronecker-style Hankel theorems are related but are not the finite
interface used here:

- A. Bakan and C. Berg, [*Solvability of the Hankel determinant problem for
  real sequences*](https://arxiv.org/abs/1605.01196), Theorems A and C.

Rounded near-geometric integer sequences do not automatically satisfy a
linear recurrence.  Boyd gives explicit Pisot sequences with no linear
recurrence, and later computational work records apparent recurrences that
fail only after thousands of terms:

- D. W. Boyd, [*Pisot sequences which satisfy no linear
  recurrence*](https://doi.org/10.4064/aa-32-1-89-98), Acta Arith. 32
  (1977), Theorem 4.
- Ekhad--Sloane--Zeilberger, [*Automated Proofs (or Disproofs) of Linear
  Recurrences Satisfied by Pisot
  Sequences*](https://arxiv.org/abs/1609.05570), especially Sections 2 and
  5 for delayed failures and Section 7 for higher-order Hankel analogues.

The targeted search found no exact predecessor for the quantitative finite
prime specialization in Sections 2--3 or for its combination with the
rank-one shadow in Section 1.  Publication-safe wording is therefore:

> The determinant-to-recurrence mechanism is classical.  The quantitative
> finite prime-block rigidity lemma and its combination with a rank-one
> shadow appear to be unrecorded in the targeted search.

That is not a priority claim.

## 6. Sharpness and next formalization target

- **Pointwise error:** determinant integrality uses every shadow error.
  An `L^1` or weighted aggregate error needs a separate extraction lemma.
- **Cubic threshold:** a rank-one `3 x 3` determinant needs two error
  columns, giving `YE^2`.  At `A=3/2` this is only `O(1)`, not `<1`.
- **Primality:** without primes, an arithmetic progression supplies
  arbitrarily long exact rank-two shell blocks.
- **Distinctness:** a constant prime sequence is an exact rank-one shadow.

The clean formalization package is:

1. determinant expansion for a rank-one matrix plus bounded error;
2. integer absolute value `<1` implies zero;
3. finite Hankel rank two implies one rational recurrence;
4. Cassini propagation and denominator collapse;
5. the hyperbolic/unit-root classification; and
6. the arithmetic-progression primorial obstruction.

All analytic literature theorems in the wider program remain external to
this finite algebraic package.

**Reproduction:** Sections 1--3 are the complete conventional proof; there
is no generated certificate or hidden data dependency.
