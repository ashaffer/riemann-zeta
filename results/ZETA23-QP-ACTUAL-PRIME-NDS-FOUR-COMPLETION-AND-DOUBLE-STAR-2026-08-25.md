# QP actual-prime NDS: four completions, determinant cells, and a prime double star

**Date:** 2026-08-25  
**Verdict:** the residual edge-degree product `(RDP)` is stronger than the
Schur closure actually needed.  For the residual transition graph it is
enough to prove the neighbourhood-degree sum

```text
W(gamma)=sum_(p~gamma) deg(p) << D q^o(1).                 (NDS)
```

On the actual prime-power shell, `W(gamma)` has an exact four-completion
form and injects into an `O(D) x O(D)` determinant grid.  The inequality
`D^2<q` makes the row carrier unique inside each error cell, but it does not
reduce the number of occupied cells from `D^2` to `D`.  The missing result is
therefore a sharp, mask-sensitive occupied-cell theorem.  It is not proved
here, so the sharp four-cycle theorem remains open.

## 1. Exact four-completion formulation

Let `P_q` be the actual prime-power shell and let `F_u(v)` denote the unique
`w in P_q`, when it exists, for which

```text
|8*u*v*w-q^3|<=qD.                                      (1.1)
```

The missing-coordinate interval has length `O(D/q)<1`, so `F_u(v)` is a
partial function.  Fix `gamma=(c,C)`.  Every two-step residual chain

```text
gamma -- p=(b,B) -- gamma'=(d,E)                         (1.2)
```

is equivalent, without multiplicity, to a pair `(a,x) in P_q^2` passing
the four tests

```text
b=F_a(c),       B=F_a(C),
d=F_x(b),       E=F_x(B).                               (1.3)
```

Consequently `W(gamma)` is exactly the number of surviving `(a,x)` in
(1.3), after the tangent edges are removed.  This is a selected
four-prime-power-completion sieve, not an unweighted determinant count.

The random-scale prediction is extremely sparse: four independent
apertures of width `D/q` over `q^2` row pairs give

```text
q^2*(D/q)^4 = D^4/q^2 = q^(-2/33).                      (1.4)
```

The uniform theorem cannot use that heuristic directly because affine
major arcs attain order `D`.

## 2. Determinant-cell injection

For a chain (1.2), put

```text
delta=b*c-B*C,             ell=C*d-c*E.                 (2.1)
```

Subtracting two hard-window residuals with a common row gives
`|delta|,|ell|<<D`.  The labels are injective.  Indeed, if two centre pairs
have the same `delta`, then

```text
c*(b-b')=C*(B-B').                                      (2.2)
```

Distinct actual nodes in the ratio-`e^.4<2` shell have distinct prime bases,
so `(c,C)=1`.  Hence

```text
(b-b',B-B')=t*(C,c).                                    (2.3)
```

The shell diameter is smaller than `min(c,C)`, forcing `t=0`.  The same
argument makes `ell` determine `(d,E)`.  Pair uniqueness in (1.1) then
recovers `a` and `x`.  Thus

```text
chain -> (delta,ell) in [-O(D),O(D)]^2                  (2.4)
```

is injective.  This proves `W(gamma)<<D^2`, while `(NDS)` is precisely the
stronger assertion that only `Dq^o(1)` physical cells in (2.4) are occupied.

Equivalently, let `p_delta=(b_delta,B_delta)` be the (at most one) shell
solution of

```text
b_delta*c-B_delta*C=delta,                              (2.5)
```

and let `gamma_ell=(d_ell,E_ell)` be the (at most one) shell solution of
`C*d_ell-c*E_ell=ell`.  Define `A_gamma(delta)` to say that an actual row
`a` completes both coordinates of `(p_delta,gamma)`, and define
`X_gamma(delta,ell)` to say that an actual row `x` completes both
coordinates of `(p_delta,gamma_ell)`.  Then the exact selected-sieve formula
is

```text
W(gamma)=sum_(|delta|,|ell|<<D)
           A_gamma(delta) X_gamma(delta,ell).            (2.6)
```

The first mask in (2.6) is one reciprocal aperture on a primitive lattice
orbit; the second is a coupled aperture in both determinant variables.
Dropping the coupled aperture structure leaves the ambient `O(D^2)` ceiling
and loses the target power.

## 3. What `D^2<q` proves, exactly

Relative to one base row write

```text
r=x*d-a*c,                 s=x*E-a*C.                   (3.1)
```

The exact approximate-gcd identity is

```text
C*r-c*s=x*(C*d-c*E)=x*ell.                             (3.2)
```

The hard windows give `|r|,|s|,|ell|<<D`.  In a box of diameter smaller
than `min(c,C)`, the map

```text
(r,s) -> C*r-c*s                                         (3.3)
```

is injective by the same primitive-step argument as (2.2)--(2.3).
Moreover a nonzero value in (3.3), of size `O(qD)`, has at most one divisor
`x` in the actual shell: two distinct such prime powers are coprime and
their product is `asymp q^2>qD`.

This is genuine rigidity, but it leaves `O(D^2)` possible error pairs.
The hoped-for `D` bound does not follow from divisibility or from
`D^2<q`; the other two completion masks in (1.3) must supply the missing
square-root aggregation.

## 4. Actual prime powers do contain residual major arcs

The degree-one prime-power scans are not structural.  Let

```text
m=2,934,091,          q=2m=5,868,182,          D=1,912.
```

All seven numbers

```text
m-24,m-18,m-12,m,m+6,m+12,m+18                       (4.1)
```

are prime and lie in the project shell.  The following three edges satisfy
the literal hard window; their displayed determinants are nonzero:

| row | centre pair | colour pair | determinant |
|---:|---:|---:|---:|
| `m-18` | `(m,m+6)` | `(m+18,m+12)` | `-72` |
| `m-12` | `(m,m+6)` | `(m+12,m+6)` | `-36` |
| `m-24` | `(m+6,m+12)` | `(m+18,m+12)` | `-36` |

The largest of the six absolute residuals is `10,985,257,440`, below

```text
qD=11,219,963,984.                                      (4.2)
```

The three displayed edges already give a double star.  Enumerating the
complete residual transition support induced by the seven primes in (4.1)
is stronger: the central edge has endpoint degrees `4` and `4`, and the
central colour has

```text
W=14.                                                     (4.3)
```

These are rigorous lower bounds for the full actual shell, since adding
the other shell nodes cannot delete an edge.  Across either displayed arm,
the two semiprime factor
pairs are disjoint, so this is not an exact-product or swapped-factor
artifact.  It does not challenge `(NDS)` (`14<<D`); it proves that an NDS
proof must retain and charge actual-prime affine major arcs rather than
declare every actual residual component a matching.

The all-integer affine bicliques already constructed in the companion
tangent/Pluecker audit have side length `L` and `D=512L^2`.  For a vertex in
such a block, `W` is of order `L^2`, hence of order `D`.  They demonstrate
that `(NDS)` has the correct scale.

## 5. Finite audit and remaining theorem

Exact full-integer critical-window scans give:

| `q` | `D` | `max W(gamma)` | ratio |
|---:|---:|---:|---:|
| 400 | 18 | 9 | .500 |
| 900 | 27 | 9 | .333 |
| 1,400 | 34 | 14 | .412 |
| 2,200 | 42 | 21 | .500 |
| 3,500 | 52 | 29 | .558 |
| 6,000 | 68 | 41 | .603 |
| 10,000 | 87 | 56 | .644 |
| 20,000 | 121 | 75 | .620 |

These data support `W<<D`; they do not prove it.  Algebraic determinant
labels alone also do not prove it: an arbitrary `D x D` partial Latin
support can have `D^2` cells, and the known scattered secant models retain
the same local Pluecker identities.  What remains is the following exact
physical theorem:

> For every primitive actual endpoint `gamma`, the four-completion system
> (1.3) occupies at most `Dq^o(1)` determinant cells `(delta,ell)`.

There is a useful but limited inverse consequence.  Dyadically group the
base neighbours by `t<=deg(p)<2t`.  Since there are `O(log D)` groups, an
NDS excess `W` produces one group `P_t` with

```text
|P_t|*t >> W/log D.                                    (5.1)
```

Thus a polynomial violation forces a genuinely two-sided high-fan block;
one of `|P_t|` and `t` exceeds `sqrt(W/log D)`.  This is the correct place
to invoke a physical packet-or-dispersion theorem.

It is not, by itself, an affine-packet theorem.  A bipartite forest on
`O(D)` row and column labels can have nearly `2D` occupied cells and no
`2 x 2` rectangle at all.  Even a small polynomial excess above `D` need
not cross the general `D^(3/2)` four-cycle threshold.  Therefore neither
label injectivity nor a purely extremal-graph argument can classify every
NDS excess as a ruling.  The classification must use all four completion
masks in (1.3).  No legal all-integer hard-window fixture with `W>D` was
found in the scans above, but this finite failure to find one is not an
integer-shell theorem.

Equivalently, one needs a packet-or-dispersion theorem: affine/rank-one
major arcs have total area `O(Dq^o(1))`, while the complement satisfies a
two-inverse large sieve with the same total.  Current Kloosterman bilinear
theorems average coefficients or moduli and do not supply this fixed,
four-mask occupied-cell estimate.

## 6. Verification

Executable artifacts:

```text
src/qp_actual_prime_nds.py
src/test_qp_actual_prime_nds.py
lean/weilcert/QPActualPrimeNDS.lean
```

The tests replay the literal prime fixture, the four-completion count, the
determinant labels, and (3.2).  Lean certifies (3.2), both difference
identities, the two-large-coprime-divisors contradiction, primality of all
seven fixture nodes, all six hard-window inequalities, and the three
displayed determinants.  It does not
certify the open asymptotic occupied-cell theorem.
