# QP self-orbit total kernel: reciprocal large-sieve audit

**Date:** 2026-08-26  
**Verdict:** summing the whole symmetric self-orbit kernel is a genuine
simplification: it removes the rooted selector and would imply NDS
immediately.  After one radial window is majorized, its constant Fourier
mode is only

```text
D^3/q = D^(15/16+o(1)),
```

so it lies below the desired `D` scale.  The remaining term is exactly a
diagonal-strength large sieve for reciprocal products of two copies of the
same short modular orbit.  Proving that large sieve would prove the total
edge theorem and hence NDS.

The displayed diagonal large sieve is only a sufficient target, not a
uniformly true theorem: a coherent adjacent integer orbit has a macroscopic
low-frequency mode and violates it by a fixed power even though its radial
edge count is `O(D)`.  Thus a viable version must first subtract/charge the
coherent major arcs and retain the signed Fourier reconstruction on them.

This is not a scalar Blomer--Pascadi application.  The exact phase splits,
by additive reciprocity, into **two moving inverse phases**.  Alternatively,
reducing the radial residual modulo the row erases both orbit variables;
the radial interval contains `Theta(D)` quotient lifts in that one residue
class.  Thus the old joint Paley obstruction has disappeared, but the
archimedean quotient/two-inverse obstruction remains.  No total-edge or
four-cycle proof is obtained here.

## 1. Why total edges would be enough

For the fixed anchor orbit, write

```text
p_t=(b_t,B_t),
X(t,j)=1
```

when one actual row `x` satisfies

```text
|8*x*b_t*B_j-q^3|<=qD,
|8*x*B_t*b_j-q^3|<=qD.                              (1.1)
```

The kernel is symmetric.  If `deg(t)=sum_j X(t,j)`, then the rooted
quantity is

```text
W_gamma=sum_t X(0,t)deg(t).
```

Consequently, for the ordered total edge mass

```text
E_gamma=sum_t deg(t)=sum_(t,j)X(t,j),
```

one has simply

```text
W_gamma<=E_gamma.                                   (1.2)
```

Thus

```text
E_gamma << D*q^o(1)                                 (TE)
```

is a strictly stronger sufficient theorem for NDS.  It has no zero-tag or
root-neighbour selector: the two outer masks are the separated orbit masks
in `t` and `j`.

## 2. One radial window gives a reciprocal-product discrepancy

There are `N<<D` physical orbit points.  Dropping the second inequality in
(1.1), and even enlarging the actual row set to all shell integers, can only
increase `E_gamma`.  For a surviving triple put

```text
Q=q^3,                 y_(t,j)=Q/(8*b_t*B_j).
```

All shell coordinates are `asymp q`, and the first hard window implies

```text
dist(y_(t,j),Z) << D/q.                              (2.1)
```

Conversely the possible integer row is unique, since the interval for `x`
in (2.1) has length `O(D/q)<1`.  Row-shell membership is irrelevant for the
upper bound.

Let `delta=C*D/q`, and choose a Selberg majorant `P_H` for
`1_(||y||<=delta)` of degree

```text
H asymp delta^(-1) asymp q/D.
```

It can be chosen with

```text
P_H(y)=sum_(|h|<=H)c_h e(hy),
c_0<<D/q,                 |c_h|<<D/q.                (2.2)
```

Define the exact reciprocal-product sums

```text
S_gamma(h)=sum_(t,j) alpha_t alpha_j
             e(h*Q/(8*b_t*B_j)),                    (2.3)
```

where `alpha` is the actual orbit indicator.  (The row mask may be enlarged
for this upper bound; enlarging the vertex mask creates the coherent
obstruction in Section 4.)  Equations (2.1)--(2.3) give

```text
E_gamma
 << (D/q)N^2
    +(D/q)sum_(1<=|h|<=H)|S_gamma(h)|.               (2.4)
```

The constant mode is therefore

```text
(D/q)N^2 << D^3/q.                                  (2.5)
```

At the project scale `D=q^(16/33+o(1))`, this is

```text
D^3/q=D^(15/16+o(1)),                               (2.6)
```

with a genuine `D^(1/16)` margin below the target.

## 3. The exact smaller theorem which would close the argument

Cauchy in (2.4) shows that the following diagonal-strength estimate is
sufficient:

```text
sum_(1<=h<=q/D) |S_gamma(h)|^2
  << q*D*q^o(1).                                    (RPLS)
```

Indeed,

```text
(D/q)*sqrt(q/D)*sqrt(qD)=D.                         (3.1)
```

The right side of `(RPLS)` is exactly its random/diagonal scale: the sum
in (2.3) has `N^2` terms, so the formal diagonal contribution over `H=q/D`
frequencies is

```text
H*N^2 asymp (q/D)*D^2=qD.                           (3.2)
```

Thus a sufficient missing assertion is not another pointwise degree
estimate.  It is
a reciprocal-product large sieve for a short modular orbit, with essentially
complete off-diagonal cancellation at its natural scale.  A signed weighted
version of (2.4) would suffice.  The next section shows why `(RPLS)` itself
must be restricted to the packet-free/minor-arc sector.

There is also an exact finite Fourier form.  Choose `M` larger than twice
the range of every relevant product residual and put
`I=[-qD,qD]`.  For one window,

```text
T=M^(-1) sum_(h mod M) Ihat(h)e_M(-hQ)
       sum_(x,t,j) e_M(8h*x*b_t*B_j),                (3.3)
```

where `Ihat(h)=sum_(r in I)e_M(-hr)`.  Taking `M asymp q^3`, the `h=0`
term in (3.3) is again (2.5).  Its nonzero part is a modulus-`q^3`
trilinear product sum.  Formula (2.4) is the more economical Poisson/Selberg
version after the row has been summed.

## 4. A coherent major arc refutes the uniform diagonal large sieve

The full physical orbit already contains a rigorous obstruction to applying
Cauchy in (2.4) globally.  Put `q=2M`, take the primitive anchor

```text
gamma=(M,M+1),
```

and use the Bezout solution `u=v=-1`.  The consecutive token lane is

```text
p_t=(M+1-t,M-t).
```

Writing `a=t-1`, `b=j`, its one-window phase is

```text
Q/(8*b_t*B_j)=M^3/((M-a)(M-b)).                     (4.1)
```

There is the exact identity

```text
M^3/((M-a)(M-b))-(M+a+b)
 =[M(a^2+a*b+b^2)-a*b*(a+b)]/((M-a)(M-b)).          (4.2)
```

For `|a|,|b|<=cD` and `D^2=o(q)`, the right side is `O(D^2/q)`.  Hence on
an `N asymp D` full-integer suborbit, uniformly for
`1<=h<=c_0*q/D^2` with a sufficiently small fixed `c_0`,

```text
|S_gamma(h)| >> N^2.                                (4.3)
```

The left side of `(RPLS)` is then at least

```text
(q/D^2)*D^4=qD^2,                                   (4.4)
```

which exceeds its claimed `qD` right side by the exact factor `D`.  A single
frequency already gives the smaller violation
`D^3/q=D^(15/16+o(1))`; the whole coherent major arc supplies the remaining
`D^(1/16)`.

Nevertheless the positive-definite quadratic remainder in (4.2) leaves
only `O(D)` radial cells; this is the already known coherent ellipse
mechanism.  The failure is caused by taking absolute values/Cauchy across
the Fourier modes, not by a large edge set.  In fact the coherent band has
length `q/D^2`, so its direct contribution to (2.4) has the correct size

```text
(D/q)*(q/D^2)*D^2=D.                                (4.5)
```

Replacing that `ell^1` calculation by global Cauchy costs exactly
`sqrt(D)`, explaining the old `D^(3/2)` ceiling.

This full-integer lane is not an actual-prime counterexample.  It proves
that one cannot enlarge the orbit mask and invoke a coefficient-uniform
diagonal large sieve.  A legal analytic theorem has to charge such coherent
low-frequency packets separately and prove a centered/minor-arc analogue
of `(RPLS)` on the remaining actual mask.

## 5. Why scalar Blomer--Pascadi still does not apply

On the coprime odd actual sector (the unique possible power-of-two shell
coordinate may be split off), `gcd(8b_t,B_j)=1`.  Additive reciprocity gives
the exact factorization

```text
e(hQ/(8*b_t*B_j))
 =e_(B_j)(hQ*inverse(8*b_t))
  e_(8*b_t)(hQ*inverse(B_j)).                        (5.1)
```

Thus (2.3) contains two coupled inverse phases with both moduli moving.
Blomer--Pascadi instead estimates two scalar interval sequences against one
complete Kloosterman sum with one fixed modulus.  Completing either factor
in (5.1) leaves the other as a joint `(t,j)` coefficient; it is not absorbed
by that theorem.

Fixing a row does not manufacture the missing kernel.  If

```text
r=8*x*b_t*B_j-Q,
```

then exactly

```text
r == -Q (mod 8*x),                                  (5.2)
```

which contains neither `b_t` nor `B_j`.  Since `x asymp q`, the allowed
interval `|r|<=qD` contains `Theta(D)` representatives of the single class
(5.2).  Retaining a representative is the exact quotient condition

```text
(Q+r)/(8*x)=b_t*B_j;                                (5.3)
```

discarding it makes the radial test vacuous.  Hence a fixed-residue
inversion graph is not a legal encoding of this one-window total count.

The `Theta(D)` quotient vector also explains the familiar square-root loss:
plain Parseval controls its `ell^2` norm, while the positive count needs its
`ell^1` norm.  Cauchy costs `sqrt(D)`, sharply for a flat quotient vector,
and returns the `D^(3/2)`-type ceiling rather than (TE).  A new theorem must
retain the quotient lift, or prove a packet-subtracted version of (RPLS).

## 6. A short-cycle identity, and why it does not yet give high girth

There is one exact cycle consequence of the same small window.  On an
oriented `m`-cycle `i -> i+1`, let its row be `x_i` and put

```text
e_i=8*x_i*b_i*B_(i+1)-Q,
f_i=8*x_i*B_i*b_(i+1)-Q,
kappa_i=b_i*B_(i+1)-B_i*b_(i+1).                    (6.1)
```

The physical factors telescope, so

```text
product_i(Q+e_i)=product_i(Q+f_i).                  (6.2)
```

Expanding (6.2) and using `|e_i|,|f_i|<=qD` gives

```text
|sum_i e_i-sum_i f_i| << m^2*D^2/q                  (6.3)
```

for `mD/q^2` bounded away from one.  The left side is an integer.  Hence,
whenever the right side is below one,

```text
sum_i x_i*kappa_i=0.                                (6.4)
```

This is an exact additive holonomy law for every sufficiently short cycle.
It does not say that the cycle is coherent or tangent.  At precisely this
scale, (6.4) is the integral rounding of the telescoping real reciprocal
law; noncoherent zero-holonomy configurations have not been excluded.  A
high-girth proof would therefore still require an inverse theorem charging
every short zero-holonomy cycle to a bounded-capacity packet.  The identity
alone does not permit deleting those cycles.

The quantitative high-girth implication is otherwise sufficient.  Take
`k=floor(c log D)`.  Then `k^2D^2/q=o(1)`, so every cycle of length at most
`2k` satisfies (6.4).  If an inverse theorem let one remove
`O(Dq^o(1))` packet edges and left no such zero-holonomy cycle, the remaining
graph would have girth greater than `2k`.  The elementary Moore bound then
gives, for its average degree `d`,

```text
(d-1)^k << D,
```

and hence `d=O(1)` and `E=O(D)`.  Thus the exact missing high-girth statement
is the classification/charging of (6.4), not a stronger extremal graph
theorem.

## 7. Status

```text
total self-orbit edge theorem implies NDS:              PROVED;
root/joint selector disappears in the total sum:        PROVED;
one-window constant mode is D^3/q=D^(15/16):            PROVED;
RPLS at qD would close the total-edge theorem:            PROVED;
uniform RPLS on the enlarged physical orbit:              FALSE;
coherent adjacent lane violates RPLS by factor D:          PROVED;
coherent adjacent lane violates the D edge bound:         NO;
reciprocal phase is a coupled two-inverse phase:         PROVED;
fixed-row residual has Theta(D) quotient lifts:          PROVED;
scalar Blomer--Pascadi controls those lifts:             NO;
plain quotient Parseval removes the sqrt(D) loss:        NO;
short cycles satisfy additive holonomy:                  PROVED;
zero holonomy forces coherent/tangent packet structure:  OPEN;
total-edge bound (TE):                                   OPEN;
sharp four-cycle bound:                                  NOT PROVED.
```

The finite implication (1.2), the permutation cross-product identity, and
the exact residual product identity (6.2) are machine-checked in

```text
lean/weilcert/QPSelfOrbitTotalKernel.lean
```

with `lake env lean QPSelfOrbitTotalKernel.lean`.
