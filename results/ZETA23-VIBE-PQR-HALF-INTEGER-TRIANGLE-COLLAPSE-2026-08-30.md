# PQR half-integer triangle collapse and the single-cut boundary

**Date:** 2026-08-30  
**Status:** new exact exclusion theorem for the small-span shared-index
branch; one-cut algebraic countermodel; no uniform zero-free strip and no
proof of RH

## 0. Verdict

The proposed additive-collapse observation is correct, and the full
shared-index graph contains a stronger obstruction.  If a cleaned same-side
prime shadow has `M` vertices and physical span

```text
W:=Y omega diam(A)=o(M sqrt(Y)),
```

then one of its local three-vertex chains forces an integer to lie `o(1)`
from the half-integer `Y=N+1/2`.  More precisely, every such shadow obeys the
spacing law `W>>M sqrt(Y)`.  Neither rank two nor primality is needed after
integrality and the reciprocal labels are retained.

For

```text
diam(A)=Y^(rho+o(1)),       t_0=Y^(alpha+o(1)),
omega=2pi/t_0,
```

this closes the region

```text
alpha>1/2+rho-tau,                                  (0.1)
```

For a near-minimal Sidon ruler at the project scale,
`rho=2(.0179)=.0358`, the new boundary is

```text
alpha>.5179.                                        (0.2)
```

This strictly extends the earlier localized-carrier boundary
`.696133...`.

There is an important scope boundary.  A single complete high-versus-low
bipartite cut has no three-edge chain whose middle vertex occurs in both
roles.  On one such cut the additive-collapse theorem merely gives an
additive prime grid and falls back to broad SR2PF/prime-sumset hardness.  An
explicit affine Sidon model below saturates the broad exponent
`Y^(4/33)` algebraically.  Thus the gain comes from **gluing nested cuts**,
not from one reciprocal factorization viewed in isolation.

## 1. Exact triangle identity

Let

```text
A={a_1<...<a_M} subset Z,
Y=N+1/2,
B=Y^(50/33),
delta=Y/B.
```

Fix one sign `sigma in {+1,-1}`.  Assume that for every ordered edge `i>j`
in a retained complete graph there is an integer `p_ij` satisfying

```text
p_ij=Y exp(sigma omega(a_i-a_j))+O(delta),           (1.1)
```

with one uniform implied constant.  `sigma=+1` is the upper same-side
shadow and `sigma=-1` the lower one.  The logarithmic cleaning estimate

```text
||log(p_ij/Y)|-omega(a_i-a_j)|<=C/B
```

implies `(1.1)` because all reference points lie in one fixed shell.

Take `k>i>j` and put

```text
x=sigma omega(a_k-a_i),
y=sigma omega(a_i-a_j).
```

The reference entries obey the exact identity

```text
Y exp(x)+Y exp(y)-Y exp(x+y)-Y
   =-Y[exp(x)-1][exp(y)-1].                          (1.2)
```

Therefore

```text
|p_ki+p_ij-p_kj-Y|
 <<Y omega^2(a_k-a_i)(a_i-a_j)+delta
 <<Y omega^2 diam(A)^2+delta
 = W^2/Y+Y/B.                                       (1.3)
```

The elementary bound in `(1.3)` is uniform for either sign whenever
`omega diam(A)=o(1)`; this holds throughout the asymptotic regime used below.

The quantity `p_ki+p_ij-p_kj` is an integer, whereas every integer has
distance exactly at least `1/2` from `Y=N+1/2`.  The right side of `(1.3)`
tends to zero because

```text
W^2/Y=o(1),              Y/B=Y^(-17/33)=o(1).
```

This is impossible for large `Y`.  Applying the same observation locally is
stronger.  Write the cleaned vertices as

```text
b_1<...<b_M,             g_r=b_(r+1)-b_r.
```

For every consecutive triple, `(1.2)` and the half-integer distance give,
once the `O(delta)` term is below `1/4`,

```text
g_r g_(r+1) >>1/(Y omega^2).                         (1.4)
```

Pair the gaps as `(g_1,g_2),(g_3,g_4),...`.  AM--GM and `(1.4)` yield

```text
diam(A)>=sum_r g_r >>M/(omega sqrt(Y)).              (1.5)
```

Multiplication by `Y omega` proves

```text
W >>M sqrt(Y).                                       (1.6)
```

Equivalently, if `W=o(M sqrt(Y))`, at least one consecutive triple has
reference curvature `o(1)` and contradicts the half-integer distance.

### Theorem 1.1 -- shared-index local-spacing exclusion

Under `(1.1)`, and uniformly while `omega diam(A)=o(1)`, every cleaned graph
with `M>=3` satisfies `(1.6)`.  In particular a growing family with
`W=o(M sqrt(Y))` is impossible.

This theorem uses:

- integrality of the three edge labels;
- one common upper/lower side;
- the reciprocal shared-index reference; and
- all three edges `ki,ij,kj`.

It does not use primality, Sidonicity, rational rank two, Pluecker minors, or
a sieve.  The weaker condition `W=o(sqrt(Y))` would already rule out one
triple, but using consecutive cleaned vertices gains the factor `M`.

## 2. Weighted-cleaning corollary

In the arbitrary-seed Fejer transport, weighted cleaning gives a retained
set `V` of size

```text
#V >=m/(1+2kappa/C)-O(1)                             (2.1)
```

on which every edge has logarithmic error at most `C/B`.  If the original
shadow is on one common side, Theorem 1.1 applies to the complete graph on
`V`.  Since `#V>>m`, no growing Sidon Fejer state survives when
`W=o(m sqrt(Y))`.

Put

```text
m=Y^(tau+o(1)),       tau=.0179,
t_0=Y^(alpha+o(1)),
diam(A)=Y^(rho+o(1)).                                (2.2)
```

Since

```text
W=Y omega diam(A)=Y^(1+rho-alpha+o(1)),              (2.3)
```

condition `W=o(m sqrt(Y))` follows from `(0.1)`.  A Sidon set has
`rho>=2tau-o(1)`.  Near minimal diameter, `rho=2tau=.0358`, proving `(0.2)`.

At equality `alpha=1/2+rho-tau`, no conclusion follows from the exponent
ledger without a sufficiently small constant.  The accurate asymptotic
condition is `W/(m sqrt(Y))->0`; Theorem 1.1 itself supplies a positive
constant lower bound.

## 3. Audit of additive `2 x 2` collapse

For rows `i,k` later than columns `j,l`, the reference additive mixed
difference is

```text
X_ij-X_il-X_kj+X_kl
 =Y[exp(sigma omega a_i)-exp(sigma omega a_k)]
    [exp(-sigma omega a_j)-exp(-sigma omega a_l)].   (3.1)
```

Thus its magnitude is `O(W^2/Y)`.  Equation `(1.1)` gives

```text
p_ij-p_il-p_kj+p_kl=O(W^2/Y+Y/B)=o(1).              (3.2)
```

The left side is an integer, hence is exactly zero.  On any one complete
ordered rectangle this glues to

```text
p_ij=r_i+c_j.                                        (3.3)
```

For a complete lower-triangular graph, the rectangular identities glue
globally: take `r_i=p_i1`, define `c_j=p_kj-p_k1` using any `k>j`, and use
`(3.2)` to see that this is independent of `k`; the last column is defined
from its sole later row.  Then `(3.3)` holds for every `i>j`.

The shared-index diagonal completion is

```text
r_i+c_i=p_ki+p_ij-p_kj                       (k>i>j), (3.4)
```

and `(1.2)` says it is `o(1)` from `Y`.  Thus the triangle proof is exactly
the half-integer obstruction hidden inside the additive gluing.

## 4. Why one high/low cut is different

Let `H` and `L` be disjoint, with every `a_i` in `H` larger than every `a_j`
in `L`.  A single matrix

```text
(p_ij)_(i in H,j in L)
```

has no observed edge joining two vertices of `H` or two vertices of `L`.
No vertex is both a row and a column, so `(3.4)` cannot be formed.  Additive
collapse gives only an injective prime sumset grid.  Existing broad SR2PF
technology does not bound its balanced side below `Y^(4/33+o(1))`.

The following exact algebraic model shows that this is not a bookkeeping
accident.

### Proposition 4.1 -- affine reciprocal Sidon shadow

Let `b_1<...<b_m` be an integer Sidon set of diameter `O(m^2)`.  Split it
after the midpoint.  Put

```text
a_i=4b_i+1       on the low half,
a_i=4b_i         on the high half.                  (4.1)
```

Then the `a_i` remain Sidon: equality of two ordered differences first
agrees modulo four and then reduces to equality of differences in `b`.
The order is unchanged, and every high-minus-low difference is odd.

Choose a fixed odd integer `L>=13`, and set

```text
lambda=L/2,              omega=lambda/Y,
q_ij=Y+lambda(a_i-a_j)       (i high, j low).        (4.2)
```

Because `2Y` and `L(a_i-a_j)` are both odd, every `q_ij` is an integer.
Sidonicity makes these integers distinct.  Moreover,

```text
Y exp[omega(a_i-a_j)]-q_ij
 =O(diam(A)^2/Y).                                    (4.3)
```

The matrix is exactly additive,

```text
q_ij=(Y+lambda a_i)-lambda a_j,                      (4.4)
```

so it has rational rank at most two and all its additive mixed differences
vanish.  Its nonzero multiplicative `2 x 2` minors have size
`O(diam(A)^2)`.

Take

```text
m<=c Y^(4/33),        diam(A)<<m^2<<c^2Y^(8/33).
```

For sufficiently small fixed `c`, `(4.3)` is `O(Y^-17/33)=O(Y/B)`, while
the minors have the full allowed height `O(Y^(16/33))`.  Thus the
reciprocal, shared-seed, Sidon, rank-two, distinct-integer structure
algebraically saturates the broad `Y^(4/33)` exponent.

The entries in `(4.2)` are not asserted to be prime.  Requiring all of them
to be prime is precisely a growing affine prime-difference-set problem, a
special case of the prime-sumset hardness already present in broad SR2PF.
Therefore no argument using only rank, minor height, reciprocity, Sidonicity,
and integrality can beat `4/33` on a single cut.  A proof must use primality
in a way stronger than unique factorization, or must restore the nested
three-edge gluing used in Theorem 1.1.

## 5. Exact finite prime sanity check for one cut

One cut is genuinely compatible with primes.  Take

```text
Y=10000006418.5,
A={1,5,16,24},
low={1,5},               high={16,24},
lambda=15/2,             omega=lambda/Y.
```

The set `A` is Sidon and its four cross differences are
`15,11,23,19`.  The affine entries `(4.2)` are the distinct primes

```text
10000006531   10000006501
10000006591   10000006561.                           (5.1)
```

All four are prime.  Their determinant is `1800`.  For the four entries,

```text
0<Y exp[omega(a_i-a_j)]-q_ij
 <=1.488e-6
 <Y^(-17/33)=7.055e-6.                              (5.2)
```

Also

```text
t_0=2pi/omega=(4pi/15)Y=0.837758...Y,
```

so the source height lies in the legal interval `[Y^.5,Y]`.  This fixed
fixture does not refute an asymptotic size bound, but it verifies every local
one-cut condition and illustrates why the missing shared-index triangle is
essential.

## 6. Updated PQR phase diagram

```text
clean same-side arbitrary-seed shadow with M asyp m
|
+-- W=o(m sqrt(Y)) and all ordered edges retained
|      -> local half-integer spacing contradiction: CLOSED
|
+-- W=o(sqrt(Y)) but only one disjoint high/low cut
|      -> additive prime grid
|      -> affine Sidon model saturates 4/33 algebraically
|      -> growing prime-sumset theorem: OPEN
|
`-- W not o(m sqrt(Y))
       -> quasiseparable PQR / PQR+G: OPEN.
```

The new mathematics is the first branch.  It closes the high-source,
small-span Sidon regime at `.5179`, rather than merely reclassifying it as an
additive grid.  It does not solve low-source PQR, the analytic extraction of
an arbitrary separator, DPA, a uniform zero-free strip, or RH.

The exponential identity, exponent arithmetic, primality of the finite
fixture, determinant, and high-precision transport errors replay with

```bash
python3 results/verify_zeta23_vibe_triangle.py
```
