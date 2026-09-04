# QP finite carrier relative trace: exact Fourier model and induced-span gate

**Date:** 2026-08-24  
**Verdict:** no counterexample to the sharp centered carrier norm was found,
and the tested literal prime-power matrices are much smaller than
`sqrt(D)`.  There is, however, an exact warning for the proposed
regularization: after compression to the narrow prime-power shell, the
restrictions of finite induced characters span **every symmetric physical
matrix**.  Thus "subtract all induced channels" is vacuous unless the
inducing data come with a new norm and a proof that their physical pullback
is one of the already controlled tangent/chart terms.

This report does not prove the asymptotic sharp four-cycle theorem.

## 1. The literal carrier matrix

Let

```text
D=floor(q^(16/33)),
S(q)={prime powers in [(q/2)e^(-.2),(q/2)e^(.2)]}.
```

The finite matrix tested here is exactly

```text
T_q(b,c)=sum_(a in S(q)) 1_(|8abc-q^3|<=qD),       b,c in S(q),       (1.1)
mu_q=(sum_(b,c)T_q(b,c))/|S(q)|^2.
```

The product interval contains at most one integer `a` at these parameters.
The implementation nevertheless checks both adjacent integer candidates
and rejects a cell if it acquires two labels.  All window comparisons use
Python integers.  In particular, the code computes `D` from

```text
D^33 <= q^16 < (D+1)^33                              (1.2)
```

without a floating-point power.

The finite sharp norm statement is

```text
||T_q-mu_q J||_(2->2) << sqrt(D) q^o(1).             (1.3)
```

Using the empirical mean gives the best literal physical constant-mode
normalization.  Replacing it by the analytic main coefficient `kappa`
requires the separate, familiar degree-main-term estimate.

## 2. An exact carrier-preserving finite group

The actual matrix has an exact finite abelian-group realization; no
logarithmic binning or approximate product map is necessary.

The ratio of the shell endpoints is `e^.4<2`.  Therefore `S(q)` contains at
most one power of any base prime.  Write its nodes as

```text
s_i=p_i^(e_i),                  1<=i<=n.              (2.1)
```

Choose pairwise independent cyclic coordinates of orders `M_i`, with each
`M_i` a prime larger than `3 max(e_i)`, and put

```text
G=product_i Z/M_i Z,
iota(s_i)=e_i times the i-th coordinate vector.       (2.2)
```

There is no exponent wrap for a product of three shell nodes.  Let `Omega`
be the set of group vectors `iota(a)+iota(b)+iota(c)` for which the
corresponding integer product satisfies (1.1), and set

```text
f(x)=sum_(a in S(q)) 1_Omega(iota(a)+x),
H_f(x,y)=f(x+y).                                      (2.3)
```

If `R:ell^2(G)->ell^2(S(q))` is restriction to the embedded shell, then

```text
T_q=R H_f R*.                                         (2.4)
```

This is the exact finite carrier-preserving analogue of the proposed
two-index Poincare transform.

## 3. Exact singular and polar decomposition

For a character `chi` of `G`, use

```text
fhat(chi)=sum_(x in G) f(x) conjugate(chi(x)).
```

Finite Fourier inversion gives

```text
H_f(x,y)=1/|G| sum_chi fhat(chi) chi(x)chi(y),         (3.1)
singular values of H_f = {|fhat(chi)|}.               (3.2)
```

Moreover, if `A` is the shell indicator and `W=1_Omega`, then

```text
fhat(chi)
  =(sum_(a in S(q))chi(iota(a))) What(chi).           (3.3)
```

Thus the common carrier is retained, the complete induced decomposition is
explicit, and deletion of a character set `P` leaves the exact full-group
norm

```text
||H_f-H_(f,P)|| = max_(chi notin P)|fhat(chi)|.        (3.4)
```

Compression is contractive, so choosing every mode with
`|fhat(chi)|>sqrt(D)` does give a regular remainder of norm at most
`sqrt(D)`.  This part is tautological but exact.  The entire issue is the
physical pullback of the deleted modes.

## 4. The complete induced continuum is the whole physical space

Put

```text
v_chi=(chi(iota(s_1)),...,chi(iota(s_n))).             (4.1)
```

Because the base-prime coordinates in (2.2) are independent and
`gcd(e_i,M_i)=1`, the entries of `v_chi` range independently over roots of
unity.  After compression, a character term in (3.1) is a multiple of

```text
v_chi v_chi^T.                                        (4.2)
```

### Proposition 1 (exact induced-span theorem)

The tensors (4.2), as `chi` ranges over the characters of `G`, span
`Sym_n(C)`, the full space of complex symmetric `n x n` matrices.

**Proof.**  Regard the independent character values as variables
`z_1,...,z_n`.  The upper-triangular coordinates of (4.2) are the distinct
torus characters

```text
z_i z_j,                      1<=i<=j<=n.              (4.3)
```

They are mutually orthogonal on the finite character torus because every
coordinate order exceeds two.  Hence their evaluation matrix has rank
`n(n+1)/2`, which is the dimension of `Sym_n(C)`.  `square`

The executable enumeration checks this rank for small finite tori.

Consequences:

1. The phrase "all induced/Eisenstein channels" does not define a proper
   exceptional physical space.
2. The trivial full-group character is not by itself the physical constant
   mode after shell compression; nontrivial characters also project onto
   that mode.
3. A full arbitrary-inducing-data Eisenstein continuum can reproduce every
   physical symmetric operator.  Removing it without an inducing-data norm
   removes the problem rather than solves it.
4. The missing theorem must distinguish a norm-controlled polar synthesis
   from the complete induced span and must charge its pullback to the known
   tangent/chart estimates.

This is a finite, exact form of the regularized Motohashi gate.

## 5. Literal actual-prime data

The centered and doubly centered norms were computed for representative
prime moduli.  Double centering means

```text
(I-J/n) T_q (I-J/n),                                 (5.1)
```

which additionally removes the two degree-fluctuation cross channels and
is therefore a rank-at-most-two strengthening of constant subtraction.

| `q` | `D` | `n` | edges | max degree | `||T-mu J||/sqrt(D)` | double ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 1,013 | 28 | 35 | 12 | 4 | 0.4761 | 0.4175 |
| 7,817 | 77 | 193 | 72 | 8 | 0.4211 | 0.4065 |
| 25,013 | 135 | 535 | 78 | 4 | 0.2204 | 0.2189 |
| 100,003 | 265 | 1,875 | 792 | 6 | 0.1921 | 0.1920 |
| 200,003 | 371 | 3,496 | 1,515 | 6 | 0.1740 | 0.1740 |
| 500,009 | 579 | 8,097 | 4,218 | 6 | 0.1468 | 0.1466 |
| 1,000,003 | 811 | 15,374 | 10,851 | 8 | 0.1278 | 0.1278 |

No displayed matrix has even one singular mode above `sqrt(D)`; no polar
subtraction is numerically required.

This is not only an eigensolver observation.  If `Delta_q` and `dbar_q`
are the maximum and mean degrees, Schur's test gives

```text
||T_q-mu_q J|| <= Delta_q+dbar_q,                     (5.2)
||(I-J/n)T_q(I-J/n)|| <= Delta_q.                     (5.3)
```

The code checks the cleared integer inequalities

```text
(Delta_q*n+edges)^2 <= D*n^2,
Delta_q^2 <= D.                                      (5.4)
```

Thus whenever (5.4) holds, the literal finite `sqrt(D)` bound is certified
without floating point.

The search comprised:

* every one of the 2,594 prime moduli `1001<=q<=25000`;
* 31 geometrically spaced prime moduli through `q=1,000,003`; and
* 80 deterministic log-uniform prime moduli in `[25000,1,000,003]`, using
  random seed `240824`.

Every searched instance passed both exact inequalities (5.4).  In the
exhaustive range the largest observed spectral ratio was `0.47613`, at
`q=1013`.  The known literal non-tangent four-cycle at `q=200003` is present
with all four labels exactly replayed, but its whole carrier matrix still
passes (5.4) by a large margin.

These sizes are arithmetically faithful but asymptotically sparse.  The
experiment is therefore evidence against an easy actual-prime
counterexample, not evidence sufficient to extrapolate a theorem.

## 6. What a nonvacuous breakthrough must say

The finite calculation suggests the following exact inverse formulation.
For the actual physical centering, every singular mode above
`sqrt(D)q^epsilon` must be synthesized by a quantitatively bounded family of
the already classified tangent, parabolic, or prime-power chart packets;
after removing those synthesized packets, the residual norm must be at most
`sqrt(D)q^epsilon`.

It is essential that "synthesized" include all three assertions:

```text
(i)   the inducing-data norm is bounded by the physical source norm;
(ii)  its pullback is supported on a previously controlled packet class;
(iii) the packet charges have bounded overlap across moving moduli.       (6.1)
```

Without (i)--(iii), Proposition 1 shows that a complete induced continuum
can simply rename the entire matrix as polar.  With (i)--(iii), the Fourier
threshold decomposition (3.4) supplies the desired regular remainder and
the existing packet estimates control the polar part.  This is the precise
finite shadow of the mask-sensitive two-index Motohashi theorem.

## 7. Status

```text
exact carrier-preserving finite group:               CONSTRUCTED;
exact character singular decomposition:             PROVED;
regular remainder after threshold deletion:          EXACT/TAUTOLOGICAL;
restricted induced span equals all Sym_n:             PROVED;
"all induced channels" as a useful polar definition: REFUTED;
literal q=200003 non-tangent cycle replay:            PASS;
actual-prime counterexample through q=1,000,003:      NOT FOUND;
all searched exact Schur sqrt(D) certificates:        PASS;
asymptotic mask-sensitive polar synthesis (6.1):      OPEN;
sharp four-cycle theorem:                             NOT PROVED.
```

Executable certificates:

* `src/qp_finite_carrier_relative_trace.py`;
* `src/test_qp_finite_carrier_relative_trace.py`.

