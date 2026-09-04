# Prime-log early returns: the exact dual sum and the mean-value critical line

Status: focused follow-up to the prime Riesz-product torus theorem,
2026-08-12.  The exact finite-band implication is reduced to a pointwise
prime exponential sum.  The direct Montgomery-mean-value/derivative
conversion is proved to stop at a critical equality and give no fixed power;
the accompanying Vaughan discussion audits only coefficient-blind
fixed-order `L^2` recompletions.  This is a scoped no-go for those
mechanisms, not a proof that the finite-band positive moment vector is
impossible.  No zero-free strip is claimed.

## 1. Verdict

Let `P_Y` be the primes in a fixed nonempty multiplicative shell about
`Y_c`, put

```text
u_p=log(p/Y_c),
M=abs(P_Y)=Y_c^(1+o(1)),
S_Y(xi)=sum_(p in P_Y) exp(i*xi*u_p),                (1.1)
```

and let the permitted spectral band be

```text
I=[Y_c,T],                 T=Y_c^(1/d),              (1.2)
```

with fixed `0<d<2/3`.  If a probability measure on `I` has the common
negative moments

```text
integral cos(xi*u_p)dnu(xi)=-r
                         for every p in P_Y,         (1.3)
```

then necessarily

```text
r <= sup_(xi in I) abs(S_Y(xi))/M.                  (1.4)
```

The same statement holds with arbitrary nonnegative prime-power weights.
Thus a uniform fixed-power upper bound for this one exponential sum would
falsify the desired `r=Y_c^(-o(1))` construction outright.

The available audited pointwise arithmetic input gives only

```text
sup_(xi in I) abs(S_Y(xi))/M
 <<(log Y_c)^(-3/10)                                (1.5)
```

after the standard smooth-shell partial summation.  This is a subpower
upper bound and is compatible with both the desired subpower lower and the
square-root-power LP behavior.

The new exact calculation is that the direct ordinary-high-moment plus
Lipschitz conversion cannot improve (1.5) to a power.  For every fixed
integer `q>=1`, Montgomery's mean-value theorem and the Lipschitz bound for
`S_Y` imply

```text
[sup_I abs(S_Y)/M]^(2*q+1)
 <<_q (T+Y_c^q)/M^q.                                (1.6)
```

Since `M=Y_c^(1+o(1))` and `T=Y_c^(1/d)`, the exponent on the right is

```text
max(1/d,q)-q >=0.                                   (1.7)
```

It is positive for `q<1/d` and zero for `q>=1/d`.  No fixed `q` makes it
negative.  The uniform-in-`q` version in (3.7) below also shows that allowing
`q` to grow does not rescue this direct estimate.  The audited high-moment
route therefore cannot even
prove

```text
sup_I abs(S_Y)/M <=Y_c^(-delta)                     (1.8)
```

for one fixed `delta>0`.  This is the same conductor equality that made the
finite-band Riesz product lose control of its high-degree Fourier mass.

## 2. The exact uniform-prime dual

Sum (1.3) over the primes.  Positivity of `nu` gives

```text
r*M
 =abs integral Re(S_Y(xi))dnu(xi)
 <=integral abs(S_Y(xi))dnu(xi)
 <=sup_(xi in I) abs(S_Y(xi)).                      (2.1)
```

This proves (1.4).  More generally, for nonnegative `lambda_n` on any
collection of active prime powers,

```text
r <= sup_(xi in I)
        abs sum_n lambda_n*exp(i*xi*u_n)
       /sum_n lambda_n.                             (2.2)
```

Equation (2.2) is only a necessary condition.  Smallness of one weighted
sum can disprove a proposed `r`; largeness does not prove the full convex
inclusion, which requires every separating functional.

The von-Mangoldt choice used in the existing atomic dual is stronger than
the uniform-prime choice for available estimates.  The imported sharp-prefix
KMT bound is uniform for
`abs(xi)<=Y_c^((log Y_c)^(1/25))`, hence throughout (1.2) for fixed `d` and
large `Y_c`.  On a fixed shell, the audited estimate is

```text
sum_n Lambda(n)/sqrt(n)*W(log(n/Y_c))
       *exp(i*xi*log(n/Y_c))
 <<sqrt(Y_c)/(log Y_c)^(3/10)                       (2.3)
```

If one imports the centered version of this estimate, its matching
continuum is `O(sqrt(Y_c)/abs(xi))=O(Y_c^(-1/2))` on `I`, so (2.3) follows
with no change of scale.  Bounded-variation partial summation applied to the
factor `sqrt(p)/log p` then gives

```text
abs(S_Y(xi)) << Y_c/(log Y_c)^(13/10).               (2.4)
```

Since `M asymp Y_c/log Y_c`, this is (1.5).  The total contribution of
higher prime powers to (2.3) is `O(1)` on a fixed shell and is negligible at
this normalization.  See
`../publication/IMPORTED-ANALYTIC-BASELINE.md`, LIT-PT1,
`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`, Section 6,
and `ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`,
Section 7, for the precise imported range and normalization.

## 3. The Montgomery criticality theorem

We prove (1.6).  A fixed smooth shell changes no exponent, so write the
sharp shell for simplicity.  Expanding the `q`-th power gives a Dirichlet
polynomial

```text
S_Y(xi)^q
 =sum_n a_q(n)*exp(i*xi*log(n/Y_c^q)),              (3.1)
```

where `a_q(n)` counts ordered representations of `n` as a product of `q`
shell primes.  If the shell lies in `[c*Y_c,C*Y_c]`, its support lies below
`(C*Y_c)^q`.  Unique factorization gives

```text
sum_n abs(a_q(n))^2 <=q!*M^q.                       (3.2)
```

Indeed, two ordered `q`-tuples have the same product only when their prime
multisets agree, and each multiset has at most `q!` reorderings.

The mean-value theorem for Dirichlet polynomials, on any interval of length
at most `T`, now yields the uniform form

```text
integral_I abs(S_Y(xi))^(2*q) dxi
 <=C_0*(T+(C*Y_c)^q)*q!*M^q,                       (3.3)
```

with an absolute mean-value constant `C_0`; smooth prime weights of modulus
at most one give the same inequality.  For fixed `q`, (3.3) has the simpler
`<<_q (T+Y_c^q)M^q` form used in (1.6).

Put

```text
B=sup_(xi in I) abs(S_Y(xi)).                       (3.4)
```

Since every `u_p` lies in a fixed compact interval,

```text
sup_I abs(S_Y'(xi))<<M.                             (3.5)
```

At a point where `abs(S_Y)=B`, the value remains at least `B/2` on a
one-sided interval of length `gg B/M`.  Here `B<=M` and `T->infinity`, so
the endpoint causes no loss.  Consequently, with a shell-dependent constant
`C_1`,

```text
integral_I abs(S_Y(xi))^(2*q) dxi
 >=C_1^(-1)*4^(-q)*B^(2*q+1)/M.                    (3.6)
```

Combining (3.3) and (3.6), then dividing by `M^(2*q+1)`, gives

```text
[B/M]^(2*q+1)
 <=C_2*4^q*q!*(T+(C*Y_c)^q)/M^q.                  (3.7)
```

For fixed `q`, this proves (1.6).

### Theorem 3.1 (mean-value critical line)

Let `T=Y_c^A`, `A>1`, and let `M=Y_c^(1+o(1))`.  The direct pointwise bound
for the shell-prime sum obtained by:

1. applying the ordinary Dirichlet-polynomial mean-value theorem to
   `S_Y^q`, and
2. converting the resulting `2q`-moment to a supremum through the derivative
   bound (3.5),

has normalized power exponent

```text
[max(A,q)-q]/(2*q+1)>=0.                            (3.8)
```

Thus this mechanism supplies no fixed-power saving, at any moment order.
For `q<A`, the observation interval is too long relative to the available
moment normalization.  For `q>A`, the product conductor `Y_c^q` is longer
than the interval.  The formal threshold is `q=A` (the adjacent integers
straddle it when `A` is not integral).

Allowing `q=q(Y_c)` to grow does not rescue this particular bound.  There
are only finitely many integers `q<=A`; once `q>A`, (3.7) contains

```text
((C*Y_c)/M)^q=(Theta(log Y_c))^q,                  (3.9)
```

up to fixed shell constants, while `4^q q!` only worsens the right side.
This conclusion uses the explicit uniform inequality (3.7), not the
fixed-`q` implied constant in (1.6).

## 4. Why Vaughan and exponent pairs do not remove the equality

For an unrestricted integer sum, exponent pairs exploit the curvature of
`xi*log n`.  A Vaughan decomposition of the prime sum contains balanced
Type-II pieces.  On a rectangular piece their oscillation is

```text
(m*n)^(i*xi)=m^(i*xi)*n^(i*xi).                     (4.1)
```

Both one-variable phases can therefore be absorbed into the two coefficient
sequences.  An argument that subsequently treats those sequences only by
their moduli or `L^2` norms has no phase curvature left to exploit.  The
generic bilinear Cauchy/large-sieve estimate in that coefficient-blind class
returns the same `T+MN` conductor term as (3.3); separate exponent-pair
bounds for Type-I pieces do not by themselves control the balanced piece.
The fixed-order Vaughan recompletions audited in this project consequently
return a `Y_c^(1-o(1))` unweighted prime sum, in the same power class as
(1.5), rather than a fixed power.  This paragraph is not a no-go for every
coefficient-specific treatment of the balanced Type-II sums.

A transition-range estimate for this one sharp shell is not, by itself, a
formal zero-free-strip theorem: the normal-convergence argument for
`-zeta'/zeta` needs a centered smooth family on all tail shells, including
the low-frequency range.  However, a fixed-power version uniform for that
full smooth von-Mangoldt family would imply a strip by the exact dyadic
argument in `ZETA23-WIENER-ATOMIC-PRIME-GATE-TRICHOTOMY-2026-08-11.md`,
Proposition 8.1.  Thus one must distinguish:

```text
transition-only unweighted power bound: new and presently unproved;
full smooth centered power quadrature:  already strip-strength.          (4.2)
```

No classical exponent-pair or ordinary mean-value theorem in the audited
inputs supplies the first statement.

## 5. Consequence for Riesz products and sparse torus quadrature

The unrestricted torus construction with common moment `-r` has squared
`L^2` condition number

```text
exp(Theta(r^2*M)).                                  (5.1)
```

Its squared Fourier mass is concentrated at prime-factor degree
`Theta(r^2*M)`.  If `r=Y_c^(-o(1))`, that degree is `Y_c^(1-o(1))`, while
Theorem 3.1 reaches only the fixed conductor threshold `q about 1/d` before
the `Y_c^q` term dominates.  Hence:

1. the audited quantitative-Kronecker descent of the natural torus density
   cannot be completed by a bounded-degree truncation into `[Y_c,T]`;
2. the direct Montgomery bounds above do not control the high-degree
   near-relations which carry almost all of its `L^2` mass;
3. a sparse empirical torus quadrature with a polynomially conditioned Gram
   correction remains confined to the local scale

   ```text
   r<=M^(-1/2)*Y_c^o(1)=Y_c^(-1/2+o(1)).            (5.2)
   ```

The last line is a barrier for the stable Gram/Riesz implementation, not a
universal upper bound on all positive measures in the band.  An arbitrarily
ill-conditioned positive atomic solution could evade it through coherent
cancellation among degrees far beyond `1/d`; none of the present tools
controls or rules out that possibility.

## 6. Exact frontier

The early-return branch now has a sharp outcome:

```text
unbounded scalar orbit, r>=c/log Y_c:               PROVED;
finite band, stable Riesz/Gram mechanisms:           SQUARE-ROOT BARRIER;
finite band, direct Montgomery/derivative moments:   CRITICAL, NO POWER;
finite band, KMT weighted dual:                      LOG UPPER ONLY;
finite band, r=Y_c^(-o(1)):                          OPEN;
finite band, universal fixed-power upper:            OPEN.               (6.1)
```

An escape inside the audited Riesz/mean-value framework would have to use
the signs of actual high-degree prime near-relations before absolute values
or Cauchy--Schwarz.  That is a coefficient-specific arithmetic statement,
not quantitative Kronecker, ordinary discrepancy, a generic large sieve, or
a standard Riesz product.  A different direct convex or arithmetic argument
for the finite-band moment problem is not excluded.

No zeta bound is changed by this addendum.
