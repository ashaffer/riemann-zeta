# QP pair cells: discriminant divisor bound and the unresolved carrier-sum projection

**Date:** 2026-08-24  
**Verdict:** fixing the completion sum, error sum, **and** carrier sum gives a
divisor-scale pair cell by an exact discriminant factorization.  Forgetting
the carrier sum is not harmless: none of the factorization identities bounds
the number of possible carrier sums by `q^o(1)`.  This remains open even after
restricting all four coordinates to actual shell prime powers.

Consequently no `mu_2=q^o(1)` theorem, packet-free reciprocal-energy theorem,
or sharp four-cycle theorem is proved here.

## 1. Exact pair-cell algebra

Let

```text
e=a*v-N_0,                 f=b*w-N_0,
S=a+b,                     eta=e+f,
P=2*N_0+eta=a*v+b*w,
U=v+w,
x=a-b,                     y=v-w,
X=a*v-b*w=e-f,
Delta=a*w-b*v.
```

Direct expansion gives

```text
S*U+x*y=2*P,                                      (1.1)
S*y+x*U=2*X.                                      (1.2)
```

Several useful discriminant forms are therefore exact:

```text
S*X+P*(b-a)=2*a*b*(v-w),                          (1.3)
2*a*b*U-P*S=(b-a)*X,                              (1.4)
U*X+P*(w-v)=2*v*w*(a-b),                          (1.5)

(S*U-P-Delta)*(S*U-P+Delta)=P^2-X^2.              (1.6)
```

Equation (1.6) is also the identity

```text
(2*b*v)*(2*a*w)=(P-X)*(P+X).
```

It is a genuine factorization, but its two sides still contain the free
product difference `X`.

## 2. The theorem that the discriminant does prove

Fix `(S,eta,U)`, and hence fix `P=2*N_0+eta`.  From (1.1),

```text
x*y=2*P-S*U.                                      (2.1)
```

If the right side is nonzero, every ordered pair gives a signed divisor `x`
of that fixed integer, after which

```text
a=(S+x)/2, b=(S-x)/2, v=(U+y)/2, w=(U-y)/2
```

are forced.  Thus

```text
B(S,eta,U)<=2*tau(|2*P-S*U|)=q^o(1).              (2.2)
```

Parity and shell restrictions only reduce this count.  If `2*P-S*U=0`, then
`x*y=0`.  In the physical regime `q>2D`, each fixed `a` has at most one
admissible `v`, and each fixed `v` has at most one admissible `a`.  Hence the
zero case is just the diagonal pair and has multiplicity at most one.

This proves a three-label codegree theorem.  It does **not** prove the desired
two-label codegree

```text
mu_2=max_(S,eta) sum_U B(S,eta,U).                 (2.3)
```

## 3. Why summing the carrier sum remains open

For fixed `X`, the individual products are

```text
a*v=(P+X)/2,               b*w=(P-X)/2.            (3.1)
```

Divisor counting therefore gives `q^o(1)` possibilities for each fixed `X`.
But `|X|<<D`, so summing this statement gives only

```text
mu_2<<D*q^o(1).                                    (3.2)
```

The same loss appears if one first fixes `U` and applies (2.2).  Equations
(1.3)--(1.6) change the parametrization of the free label; they do not remove
it.

For actual shell prime powers, unique factorization improves the multiplicity
at a fixed `X`, but it does not bound the number of different `X`'s (or `U`'s)
that can occur.  Such a bound would be a uniform short-interval correlation
statement for two complementary products of shell prime powers, together
with the fixed factor-sum condition `a+b=S`.  No such theorem is supplied by
the divisor bound, and none is proved in this audit.

## 4. What the Jing--Wu surface theorem gives

The lifted point set

```text
mathcal X={(a,v,e):e=a*v-N_0}
```

lies on the irreducible quadratic surface `e=a*v-N_0`.  Its affine ruling
lines fix either `a` or `v`; the physical fibre uniqueness above makes the
line-concentration parameter equal to one.  The theorem of
[Jing--Wu, *Near diagonal additive energy bound for points on algebraic
surfaces*](https://arxiv.org/abs/2608.14467) consequently gives

```text
sum_(S,U,eta) B(S,eta,U)^2 << H^(2+epsilon).        (4.1)
```

The tagged energy needed by the error-labelled argument is instead

```text
E_tag=sum_(S,eta) (sum_U B(S,eta,U))^2.             (4.2)
```

Passing from (4.1) to (4.2) costs the number of carrier sums in a fixed
`(S,eta)` cell.  Proving that number is `q^o(1)` is exactly the unresolved
projection statement, not a consequence of the surface theorem.

## 5. Why square-root error blocks do not automatically close

Partition the `O(D)` possible error sums into `J=O(sqrt(D))` intervals `I` of
length `L=O(sqrt(D))`, and put

```text
B_I(S)=sum_(eta in I) B(S,eta).
```

Then

```text
E_a<=J*sum_(S,I) B_I(S)^2
   <=J*(max_(S,I) B_I(S))*H^2.                     (5.1)
```

Thus blocking would close at the desired square-root scale if every blocked
cell had multiplicity `q^o(1)`.  Exact pair-cell codegree does not imply this:
the trivial sum over the `L` exact errors restores the full factor `D`.

There is also a shell-faithful calibration.  Let `N_0=Q^2` and

```text
(a_h,v_h,e_h)=(Q+h,Q-h,-h^2),       |h|<=sqrt(D).  (5.2)
```

For completion sum `S=2Q`, the ordered pair is `(h,-h)` and

```text
eta=-2*h^2.
```

Every exact `(S,eta)` cell has multiplicity at most two.  Nevertheless the
single block `-sqrt(D)<=eta<=0` contains `asymp D^(1/4)` ordered pairs.
Hence a block-codegree `q^o(1)` statement is false before exploiting the
broad cut or the packet peel.

For two such representations indexed by `h,k`, the associated direction
product is

```text
|(k-h)(-k-h)|=|k^2-h^2|<=sqrt(D)/2.                (5.3)
```

So this particular obstruction is entirely narrow (`sqrt(D)<<q`) and is an
affine tangent packet.  It does not refute a **broad, post-peeling** block
norm theorem.  It does show that such a theorem needs to use broadness inside
the block norm; ordinary Cauchy--Schwarz on blocked cell sizes is insufficient.

## 6. Computational audit

Exact exhaustive scans of all integer points in `[q,2q]^2` for sampled
centres produced the following largest projected cells:

```text
(q,D)       maximum observed mu_2
(500,20)             6
(1000,28)            6
(2000,40)            9
(5000,62)            7
(10000,87)           9
```

The largest examples were divisor resonances, often with both individual
errors equal.  No power-sized counterexample to `mu_2=q^o(1)` was found.  This
is evidence only: the scan does not replace the missing uniform bound on the
number of carrier sums.

The exact identities, the refined divisor majorant, the small shell scan, and
the tangent-block calibration are replayed in
`src/qp_pair_cell_discriminant.py` and
`src/test_qp_pair_cell_discriminant.py`.

## 7. Binary status

```text
pair-cell identities (1.1)--(1.6):                 PROVED;
fixed-(S,eta,U) divisor codegree q^o(1):            PROVED;
Jing--Wu full-vector surface energy:                APPLICABLE;
Jing--Wu controls the projected tagged energy:      NO;
number of U values in fixed (S,eta):                OPEN;
mu_2=q^o(1), unrestricted shell:                    OPEN;
mu_2=q^o(1), actual shell prime powers:             OPEN;
sqrt(D)-block codegree q^o(1) before broad peel:     FALSE;
broad post-peeling sqrt(D)-block norm theorem:       OPEN;
sharp four-cycle bound:                             NOT PROVED.
```
