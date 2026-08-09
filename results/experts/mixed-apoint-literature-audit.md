# Mixed `a`-point literature audit

## Question

For the cubic exterior quotient

```text
F_K(s)=N_K(s)/D_K(s)
      =zeta(s)L(s,chi_D)/L(s,Std_K),
```

the nonlinear support amplifier introduces the factors

```text
G_(K,c)(s)=N_K(s)-cD_K(s),
c=1+omega,  omega^q=1,  omega!=-1.
```

Can an existing conductor-aspect theorem select, from the cubic fields with
no inert prime through `H`, a field for which every one of these finitely many
functions is zero-free in a prescribed fixed disc contained in
`Re(s)>sigma_0>51/56`?

The answer from the present literature is **no**.  Genuine Artin/Hecke
zero-density estimates have enough quantitative strength, but their zero
detectors use the Euler product and do not apply to `N-cD`.  The results that
do apply to additive combinations are in the height aspect, with constants
depending on the individual field, and do not control a prescribed bounded
height window while the conductor varies.

Post-audit update: R155 proves that the proposed simultaneous zero-free
selection is actually impossible if a fixed zeta zero is retained and the
auxiliary quotient is holomorphic.  Two omitted mixed values give a normal
family; even one omitted value is impossible when the quotient has a bounded
local zero divisor.  The literature gap below therefore remains relevant
only for a **signed estimate including the forced mixed points**, not as a
plausible zero-free selection lemma.

## 1. Exact entropy threshold

Let `Y` be the cubic discriminant scale.  The head-conditioned family in R148
has size

```text
M(Y,H) asymp Y A_H,
A_H=(2/3)^(pi(H)) (log H)^(1/2+o(1)).
```

At the certified scale `log Y=(2+eta)H`,

```text
M(Y,H)
=Y exp[-{log(3/2)/(2+eta)+o(1)} log Y/log log Y]
=Y^(1-o(1)).
```

Consequently any unconditioned exceptional-set estimate

```text
#bad(Y) << Y^theta,                 theta<1,
```

would survive the head conditioning, and a fixed union over the `q-1` mixed
factors would cost nothing in the exponent.  By contrast, a qualitative
`o(Y)` result, an unspecified density-one theorem, or a positive-proportion
universality theorem can miss the entire conditioned subfamily.  A bound of
the form

```text
Y exp[-delta log Y/log log Y]
```

would suffice only if its explicit `delta` exceeded
`log(3/2)/(2+eta)` (before accounting for any additional local costs).

This is the quantitative target against which the literature must be tested.

## 2. What genuine automorphic zero density supplies

Brumley--Thorner--Zaman, Theorem 1.2, applied to the standard `GL_2` Artin
factor, gives at fixed height

```text
sum_K N_StdK(sigma,T)
 << (YT)^((56/5)(1-sigma)+o(1)).
```

Thus it removes the standard denominators throughout a fixed rectangle once
`sigma>51/56`; this is a power-saving exceptional set and is fully compatible
with `M(Y,H)=Y^(1-o(1))`.  The newer automorphic-family density results and
the Hecke density theorems have the same structural scope: they count zeros of
`L(s,pi)` or `L(s,pi x pi_0)`, not zeros of an additive combination of two
different `L`-functions.

There is no automorphic representation whose standard `L`-function is
`N_K-cD_K`.  Its coefficients are not multiplicative.  Therefore the
pseudo-character, Rankin--Selberg, and automorphic large-sieve zero detectors
in these papers cannot simply be quoted for `G_(K,c)`.

## 3. The strongest theorem that really applies to `N-cD`

Righetti's Theorem 3 applies exactly to each fixed cubic field.  In the normal
closure the functions

```text
zeta(s),  L(s,chi_D),  L(s,Std_K)
```

come from the three distinct irreducible characters `1`, `sgn`, and `Std` of
`S_3`, hence are pairwise orthogonal in Righetti's sense.  The polynomial

```text
P(X_1,X_sgn,X_Std)=X_1 X_sgn-c X_Std
```

is not a monomial.  It follows unconditionally that `G_(K,c)` has infinitely
many zeros in `Re(s)>1`.  More precisely, for that fixed tuple there is an
`eta_K,c>0` such that, whenever

```text
1<sigma_1<sigma_2<=1+eta_K,c,
```

the number of its zeros in

```text
sigma_1<Re(s)<sigma_2,  A<Im(s)<A+T
```

is `>>_(K,c) T`, uniformly in `A`, once `T` is sufficiently large depending
on the tuple.

This is an important reality check: a global zero-free theorem for the mixed
factors is false, already to the right of one.  It does **not**, however, kill
the nonlinear argument.  Neither `eta_K,c`, the first admissible `T`, nor the
implied density constant is uniform in the conductor.  The theorem gives no
zero in a prescribed fixed disc at the fixed height of the hypothetical zeta
zero.

Booker--Thorne proves the corresponding outside-the-critical-strip phenomenon
for automorphic combinations; universality results of Bauer and later authors
give analogous height-aspect abundance.  They have the same quantifier
mismatch.

## 4. Conductor-aspect universality is not the missing estimate

Cho--Kim prove a genuine conductor-aspect universality theorem for the
standard Artin functions of `S_3`, `S_4`, and `S_5` fields.  For a compact set
in `1/2<Re(s)<1`, their Theorem 1.8 gives a positive proportion of fields for
which `L(s,Std_K)` approximates a prescribed nonvanishing holomorphic
function.  In the critical strip this assumes their Conjecture 1.7, a large
sieve for the thin field family; Section 7 replaces it by GRH.  The theorem is
unconditional only for the point-value statements at `s=1` and `s=1+it`.

There are three independent mismatches here.

1. The theorem concerns the standard factor alone, not the correlated pair
   `(L(s,chi_D),L(s,Std_K))` and hence not their ratio.
2. Its positive lower density is relative to the full field family.  It has no
   convergence rate capable of being intersected with a subfamily of density
   `A_H=Y^{-o(1)}`.
3. The local conditions used to build the approximant are fixed before
   `Y -> infinity`.  No statement is uniform when all primes through
   `H asymp log Y` have already been constrained.

The authors' own local-counting discussion makes the last point explicit:
their counting error permits primes only up to a constant times `log Y`, and
their universality theorem does not provide a diagonal estimate as that local
set grows.

Mine proves unconditional conductor-aspect value distribution for cubic
standard Artin functions (using an auxiliary zero-density theorem), including
quantitative complex moments and point-value distribution for real
`sigma>7/8`.  This is a one-point, one-factor, unconditioned result.  It is not
a functional small-ball or zero-count theorem for `N-cD`, and it is not
uniform after the growing no-inert head.  Its error
`Y exp(-delta log Y/log log Y)` comes with no assertion that the relevant
`delta` beats the head entropy constant above.

Kowalski's Bagchi theorem for modular families and the other conductor/level
universality results have the same limitation: they are not a quantitative
mixed-`a`-point density theorem for this thin, increasingly conditioned cubic
family.

## 5. Other zero and value-distribution results

- Lamzouri--Lee count zeros of fixed linear combinations near the critical
  line as the height tends to infinity.  The functions are fixed; the result
  is neither conductor-aspect nor target-local.
- Gonek--Lee and Lee prove precise height-aspect zero counts for Epstein zeta
  functions, which are linear combinations of class-group Hecke functions.
  The quadratic form and its discriminant are fixed while `T -> infinity`, so
  these theorems likewise give no conductor-uniform fixed-window selection.
- Bauer's joint universality for Artin functions and joint universality in the
  Selberg class are vertical-shift theorems for a fixed tuple.  They explain
  abundance of mixed zeros but do not select an auxiliary field at a fixed
  height.
- Selberg-class `a`-point theorems concern `L(s)=a` for one Euler-product
  function in the height aspect.  Here the relevant object is the ratio
  `N/D`, equivalently the non-Euler function `N-cD`.
- One-level density, nonvanishing at the central point, and low-lying-zero
  theorems do not control a fixed off-central disc.

No primary source located through August 2026 states a conductor-uniform
upper bound for

```text
#{K: G_(K,c) has a zero in a prescribed fixed disc},
```

even without the growing head conditions.

## 6. Former selection lemma and surviving signed target

For a fixed even `q` and target disc `Omega`, the R153 formal implication
would have been closed by

```text
#{K in C(Y,H):
    product_(omega^q=1, omega!=-1)
    [N_K-(1+omega)D_K]
    has a zero in Omega}
=o(M(Y,H)),
```

uniformly for `log Y=(2+eta)H`.  A cruder unconditioned bound
`O_q(Y^(1-delta))`, with any fixed `delta>0`, would already imply this.

R155 shows that this display cannot hold along a sequence which retains the
source zero and removes the auxiliary divisor: right-cap convergence and
mixed-value omission contradict Montel normality.  An alternative would have
been a head-conditioned functional limit theorem giving
a uniformly positive probability that all these finitely many factors omit
zero on `Omega`.  Existing point-value distributions are not enough: disc
nonvanishing is a path event, and a zero need not force a small value at any
single predetermined sample point.

The literature does not supply that functional theorem, and R155 now proves
the zero-free version impossible.  Since the mixed factors are also globally
zero-rich, the only plausible continuation is genuinely local in height,
uniform in conductor and in the growing head, and signed strongly enough to
prevent the forced mixed reciprocal-power packet from cancelling the target.

## Primary sources

- F. Brumley, J. Thorner, and A. Zaman,
  [*Zeros of Rankin--Selberg L-functions at the edge of the critical strip*](https://arxiv.org/abs/1804.06402),
  especially Theorem 1.2.
- M. Righetti,
  [*Zeros of combinations of Euler products for `sigma>1`*](https://arxiv.org/abs/1412.6331),
  Theorem 3 and Corollary 2.
- A. R. Booker and F. Thorne,
  [*Zeros of L-functions outside the critical strip*](https://arxiv.org/abs/1306.6362).
- P. J. Cho and H. H. Kim,
  [*Universality of Artin L-functions in conductor aspect*](https://www.math.utoronto.ca/henrykim/JMAA-reprint.pdf),
  Theorem 1.8, Conjecture 1.7, and Proposition 6.6.
- M. Mine,
  [*The value-distribution of Artin L-functions associated with cubic fields in conductor aspect*](https://arxiv.org/abs/1905.11851),
  Theorems 2.2--2.5.
- Y. Lamzouri and Y. Lee,
  [*The number of zeros of linear combinations of L-functions near the critical line*](https://arxiv.org/abs/2010.10490).
- S. Gonek and Y. Lee,
  [*Zero-density estimates for Epstein zeta functions*](https://arxiv.org/abs/1511.06824).
- E. Kowalski,
  [*Bagchi's theorem for families of automorphic forms*](https://arxiv.org/abs/1702.05610).
- H. Bauer,
  [*The value distribution of Artin L-series and zeros of zeta-functions*](https://doi.org/10.1016/S0022-314X(02)00048-3).

Date: 2026-08-08.
