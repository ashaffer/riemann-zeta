# R170 high-girth transfer-determinant amplifier

## Status

The scalar mixed product is the one-state member of a larger positive
amplifier.  Let `A(s)` be a finite weighted directed adjacency matrix whose
nonzero entries are positive linear combinations of head-deleted tails

```text
U_e(s)=F_e(s)-1=sum_(n>H) u_e(n)n^(-s),       u_e(n)>=0. (0.1)
```

Put

```text
P(s)=det(I-A(s)),                 B(s)=P'(s)/P(s).       (0.2)
```

Then

```text
B=sum_(k>=0) tr[A^k(-A')].                              (0.3)
```

Every Dirichlet coefficient in (0.3) is nonnegative.  If the directed
girth is `q`, every contributing closed walk has at least `q` edges, so

```text
supp B subset {n:n>H^q}.                                (0.4)
```

A particularly useful graph has `q` cyclic layers, each containing `d`
states.  Its determinant reduces exactly to

```text
P=det(I-B_(q-1)...B_0),                                 (0.5)
```

where `B_j` is the transfer matrix from layer `j` to layer `j+1`.  The
case `d=1` is R166's scalar product.  For `d>=2`, the bad scalar equation
is replaced by matrix singularity.  Away from the prescribed divisor, the
safe target is `GL_d(C)`, not the complement of a finite set or one scalar
product hypersurface.

There is no target-jet obstruction.  Choose positive stochastic layer
matrices whose one-turn product is primitive.  At a common zero of all
`F_e`, the transfer matrices are their negative stochastic baselines.  For
even `q`, (0.5) then has a simple zero coming from the simple Perron root;
all transverse eigenvalues stay separated from one.  The scalar cofactor
at the target is a nonzero positive linear functional of the edge
multipliers unless those multipliers are deliberately phase-cancelled.

The local conditioning issue for the scalar product can also be solved
uniformly in growing `q`.  On every fixed `|z|<=R`, take

```text
F_1=z,             F_j=[eta/(q-1)]z,       2<=j<=q.     (0.6)
```

For every sufficiently small fixed `eta>0`, all channels have exactly the
zero of `z`, while

```text
1-product_j(F_j-1)=z C_q(z),
sup_(|z|<=R)|C_q(z)-1|
 <=(1+R)eta exp(R eta)<1.                               (0.7)
```

Thus the artificial local root at distance `O(1/q)` found for comparable
slopes is not forced.  One dominant target slope and `q-1` slopes of size
`asymp 1/q` keep the cofactor uniformly zero-free.  Moving those small
slopes back to head value one costs only `log q` in their unit logarithms,
consistent with R169's propagation ledger.

The matrix lift therefore survives both the coefficient/support test and
the local target-conditioning test.  It does **not** yet prove a strip.
Ambient Oka flexibility of `GL_d(C)` does not preserve the decisive edge
constraints

```text
1+A_e/w_e=Z M_e,             M_e a unit,                (0.8)
```

together with common cap normalization and fixed-power growth.  The next
theorem would have to be a quantitative, divisor-preserving matrix
completion/factorization theorem for (0.5).  Standard holomorphic
factorization into elementary matrices allows arbitrary holomorphic
entries and does not supply (0.8).

```text
matrix logarithmic-derivative positivity                 THEOREM
directed-girth H -> H^q support amplification             THEOREM
q-layer transfer determinant reduction                   THEOREM
simple common target through Perron root                  THEOREM
uniform growing-q local slope conditioning                THEOREM
scalar product recovered at d=1                          EXACT
ambient safe matrix locus GL_d(C)                        FLEXIBLE
divisor-preserving unit-edge matrix completion            OPEN
arithmetic realization with fixed-power control           OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching Re(s)=1                                 NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md`](R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md),
[`R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md`](R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md),
and
[`R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md`](R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md).

## 1. The graph determinant theorem

Let `G=(V,E)` be a finite directed multigraph.  Give every edge `e` a
positive weight `w_e`.  With the convention that an edge from `u` to `v`
contributes to entry `(v,u)`, define

```text
A_(v,u)(s)=sum_(e:u->v) w_e U_e(s).                     (1.1)
```

Assume (0.1) converges absolutely in a right half-plane.  Multiple edges
cause no difficulty.

### Theorem 1.1 -- positive closed-walk expansion

In every right half-plane in which the entries converge absolutely and
the spectral radius of their coefficientwise positive majorant is less
than one,

```text
P'/P=sum_(k=0)^infinity tr[A^k(-A')]                    (1.2)
```

is an absolutely convergent Dirichlet series with nonnegative
coefficients.  If `G` has directed girth `q`, its nonconstant support is
contained in `{n>H^q}`.

#### Proof

Jacobi's formula and the geometric matrix series give

```text
[log det(I-A)]'
 =tr[(I-A)^(-1)(-A')]
 =sum_(k>=0)tr[A^k(-A')].                               (1.3)
```

Expanding a trace in (1.3) produces closed directed walks of length
`k+1`, with one distinguished differentiated edge.  The coefficient of
that edge is multiplied by `log n` and remains nonnegative.  All other
edge coefficients and all graph weights are nonnegative as well.  A
closed walk has length at least the directed girth.  Since every edge
index is strictly larger than `H`, the integer index of its convolution
product is strictly larger than `H^(k+1)>=H^q`.  Absolute convergence
justifies all rearrangements.  QED.

The proof also gives a useful majorant version.  If complex edge
coefficients are dominated termwise by nonnegative tails satisfying the
same bounds, the coefficients of `P'/P` are dominated in modulus by the
corresponding positive closed-walk series.  Literal positivity is therefore
stronger than the right-circle estimate needed by the high-jet argument.

### Corollary 1.2 -- right-circle scale

Suppose the graph has fixed maximum weighted degree and, on a right
circle,

```text
max_e (|U_e|+|U_e'|)<=H^(-r/2+o(1)).                   (1.4)
```

For fixed graph size,

```text
|B(s)|<=H^(-qr/2+o(1)).                                 (1.5)
```

For a growing graph, the number of based closed walks supplies the explicit
combinatorial prefactor.  If the maximum weighted degree is `Delta`, it is
at most `|V| Delta^q` at the first possible length.  In particular,
`q=O(log H)` costs only a fixed power of `H` when `Delta` is fixed.  This
cost must be retained in any final exponent ledger.

## 2. Cyclic layers and the Perron target

Partition the vertices into `q` layers `V_0,...,V_(q-1)` of common size
`d`, and allow edges only from `V_j` to `V_(j+1 mod q)`.  Write the
corresponding weighted transfer blocks as `B_j(s)`.  Successive Schur
complements, or the eigenvector recurrence around the layers, give

```text
det(I-A)=det(I-B_(q-1)...B_0).                          (2.1)
```

Every directed closed walk has length divisible by `q`; hence the directed
girth is at least `q`, and it is exactly `q` as soon as one full positive
cycle exists.

Fix positive row-stochastic matrices `W_j` and put

```text
B_j(s)=W_j Hadamard U_j(s),                             (2.2)
```

where each allowed scalar edge tail equals `-1` at a common target zero.
At that point,

```text
B_j=-W_j,
B_(q-1)...B_0=(-1)^q T,
T=W_(q-1)...W_0.                                        (2.3)
```

Assume `q` is even and `T` is primitive.  Perron--Frobenius gives a simple
eigenvalue one of `T`, while every other eigenvalue has modulus strictly
less than one.  Equation (2.1) therefore has a simple spectral factor
available at the target.

To see transversality explicitly, let `Z` be a local coordinate for the
common divisor and write

```text
F_e=Z M_e,                 U_e=-1+Z M_e.                (2.4)
```

If all `M_e(rho)=m!=0`, then at first order

```text
B_j=(-1+Zm)W_j,
B_(q-1)...B_0=(-1+Zm)^q T.                              (2.5)
```

The Perron factor in (2.1) is

```text
1-(-1+Zm)^q=qmZ+O(Z^2).                                 (2.6)
```

All transverse factors are nonzero at `Z=0`, so `P` has the same simple
target zero.  For general edge values `M_e(rho)`, the derivative of the
Perron eigenvalue is a linear functional of those values.  Its
coefficients have one common sign after the alternating layer signs are
removed.  Thus nontransversality is a codimension-one phase cancellation,
not a forced matrix obstruction.

When `d=1`, (2.1) reads

```text
P=1-product_(j=0)^(q-1) B_j,                            (2.7)
```

which is precisely the mixed-product amplifier.  Positive dimension adds
parallel paths and mixing without shortening the causal cycle.

## 3. Uniform local conditioning for growing channel count

The comparable-slope warning in R169 is real but not universal.

### Theorem 3.1 -- one-dominant-slope template

Fix `R>0`.  Choose `eta>0` so that

```text
(1+R)eta exp(R eta)<1.                                  (3.1)
```

For every even `q>=2`, set `a_1=1` and

```text
a_j=eta/(q-1),                  2<=j<=q.                (3.2)
```

Then every `F_j(z)=a_jz` is `z` times a unit, and

```text
1-product_j(F_j-1)=z C_q(z)                             (3.3)
```

with `C_q` zero-free on `|z|<=R`, uniformly in `q`.

#### Proof

Since `q` is even,

```text
product_j(F_j-1)
 =(1-z) E(z),
E(z)=product_(j=2)^q(1-a_jz).                           (3.4)
```

Consequently

```text
C_q(z)-1=(1-z)[1-E(z)]/z,                               (3.5)
```

with the quotient filled removably at zero.  Put
`S=sum_(j=2)^q|a_j|=eta`.  Integrating the derivative of
`product_(j=2)^q(1-t a_jz)` for `0<=t<=1` gives

```text
|(1-E(z))/z|<=S exp(RS).                                (3.6)
```

Equations (3.1), (3.5), and (3.6) imply

```text
|C_q-1|<1                                                (3.7)
```

on the closed disc.  Hence `C_q` is zero-free there.  QED.

The target ratios between the small and dominant slopes are of order
`1/q`.  A unit interpolating from such a value at the target to one on the
cap needs a logarithmic excursion of order `log q`, exactly the scale left
open by R169.  The theorem therefore removes the proposed `O(1/q)` local
root as a fail-fast objection; it does not construct the global unit
interpolation.

## 4. The exact remaining matrix gate

Suppose the desired output divisor is represented by `Z`.  Every allowed
edge has the affine form

```text
A_e=w_e(F_e-1)=w_e(ZM_e-1),             M_e in O^x.     (4.1)
```

A successful construction must make

```text
det(I-A)=Z C,                         C in O^x,          (4.2)
```

while `ZM_e->1` on the fixed right cap and while the logarithms of the
`M_e` remain within the fixed-power outer ledger.  Equation (4.2), not
mere avoidance of `det(I-A)=0` away from the target, is the matrix analogue
of R169's cap-normalized two-unit equation.

The complement of the determinant hypersurface is `GL_d(C)`, a complex
Lie group and hence an Oka manifold.  Moreover, Ivarsson and
Kutzschebauch proved that null-homotopic holomorphic maps from finite
dimensional reduced Stein spaces into `SL_d(C)` factor into finitely many
holomorphic unipotent matrices:
[`Annals paper`](https://annals.math.princeton.edu/2012/175-1/p03).
That theorem confirms genuine ambient flexibility, but its elementary
matrix entries are unrestricted holomorphic functions.  It neither gives
the affine exact-divisor form (4.1) nor cap interpolation with a
fixed-power norm.  Applying it without proving those extra properties
would simply rename the open cofactor gate.

There are now two precise tests for this branch:

1. construct a relative matrix factorization satisfying (4.1)--(4.2) and
   quantify its cap-to-target norm; or
2. prove that every such factorization forces either a determinant zero
   beyond `Z` or outer growth exceeding the `H^q` support gain.

The local Perron and slope theorems show that either conclusion must be
global and quantitative.
