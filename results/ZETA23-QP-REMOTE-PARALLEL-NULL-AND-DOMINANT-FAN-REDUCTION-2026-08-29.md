# QP remote parallel-null and dominant-fan reduction

**Date:** 2026-08-29

**Status:** a coefficient-large physical parallel-null theorem is proved
below.  It leaves one explicit small-coefficient simultaneous-divisor
lemma.  The stronger dominant-fan inverse is false for determinant-strip
shell geometry alone, and a per-line physical theorem would not imply it.
The sharp four-cycle bound is not proved.

## 1. Physical null-line coordinates

Fix the residual edge witnessed by

```text
(a,b,c), (a,B,C)
```

and two projected affine arms

```text
u(t)=(d_t,D_t)=u_0+t*(p_1,p_2),
v(s)=(e_s,E_s)=v_0+s*(p_2,p_1).
```

The second direction is the primitive null-dual of the first, after a sign
orientation.  Put

```text
k=bc-BC !=0,
lambda=b*p_1-B*p_2,          mu=c*p_2-C*p_1,
gamma=p_2*d_t-p_1*D_t,       eta=p_1*e_s-p_2*E_s.   (1.1)
```

The last two quantities are constant on their respective lines.  The
direction coefficients satisfy the exact Cramer identities

```text
k*p_1=c*lambda+B*mu,
k*p_2=C*lambda+b*mu.                                  (1.2)
```

If `x_t,y_s` are the physical witnesses, define the exact centred product
errors

```text
alpha_t=x_t*d_t-a*c,       Alpha_t=x_t*D_t-a*C,
beta_s =y_s*e_s-a*b,       Beta_s =y_s*E_s-a*B.       (1.3)
```

All four have size `O(D q^o(1))`, by subtracting hard-window residuals
with a common fixed coordinate.  The homogeneous product lifts become

```text
p_2*alpha_t-p_1*Alpha_t=gamma*x_t-a*mu,
p_1*beta_s -p_2*Beta_s =eta*y_s-a*lambda.             (1.4)
```

These are exact, not asymptotic.

## 2. Coefficient-large parallel-null theorem

Let `K=C D q^o(1)` dominate all product-error and determinant-strip
constants, and let `H_U,H_V` be the two sparse parameter spans.  Then

```text
max(1,|lambda|,|mu|,|gamma|,|eta|)*H_U <<K,
max(1,|lambda|,|mu|,|gamma|,|eta|)*H_V <<K.           (2.1)
```

Indeed:

* `bd_t-BD_t` has slope `lambda`, while `Cd_t-cD_t` has
  slope `-mu`; both quantities are `O(K)` by the two left hard windows.
* `ce_s-CE_s` has slope `mu`, while `Be_s-bE_s` has
  slope `-lambda`; both are `O(K)` by the two right hard windows.
* the full Cartesian determinant is

  ```text
  F(u(t),v(s))=A+eta*t+gamma*s,                       (2.2)
  ```

  so endpoint subtraction gives `|eta|H_U,|gamma|H_V<<K`.
* the two omitted symmetric bounds follow directly from the product lift.
  At the extrema of `U`, for example,

  ```text
  x_0*x_1*gamma*H_U
   =(ac+alpha_0)(aC+Alpha_1)
    -(ac+alpha_1)(aC+Alpha_0).                       (2.3)
  ```

  Its right side is `O(q^2 K)` and `x_0x_1 asymp q^2`, so
  `|gamma|H_U<<K`.  The proof of `|eta|H_V<<K` is identical.

Consequently, with

```text
R=max(1,|lambda|,|mu|,|gamma|,|eta|),
```

one has

```text
|U||V| <<(1+K/R)^2.                                  (2.4)
```

In particular every physical parallel-null line pair with

```text
R >=sqrt(K)                                           (2.5)
```

satisfies the sharp local bound `|U||V|<<K`.  If `gamma=0`, actual-shell
coprimality writes `(d,D)=z(p_1,p_2)` and forces `z=1`, so `U` has at most
one point; `eta=0` is symmetric.  Also `lambda=mu=0` is impossible by
`(1.2)` and `k!=0`.

Thus the only local null block not closed by existing arguments has

```text
0<max(|lambda|,|mu|,|gamma|,|eta|)<sqrt(K),           (2.6)
```

and at least one non-affine remote witness graph.  For each failed graph
the earlier interpolation audit adds

```text
p_i^2*H^3 >>q.                                        (2.7)
```

## 3. Exact irreducible selected-divisor lemma

Equations `(1.3)--(1.4)` show exactly what remains.  The left population is
the number of actual prime powers `x` and error pairs in a `K`-box such
that

```text
p_2*alpha-p_1*Alpha=gamma*x-a*mu,
x | ac+alpha,             x | aC+Alpha,              (3.1)
```

and both quotients are distinct actual prime powers.  The right population
is the symmetric count

```text
p_1*beta-p_2*Beta=eta*y-a*lambda,
y | ab+beta,              y | aB+Beta.               (3.2)
```

For a fixed error pair the shell divisor is unique up to `q^o(1)`: it
divides `C*alpha-c*Alpha`, whose size is `O(qK)=o(q^2)`, and two distinct
shell prime powers are coprime.  This still leaves a two-dimensional error
box.  The exact missing local statement is

```text
N_U(p,gamma,mu)*N_V(p,eta,lambda) <<K q^o(1)          (3.3)
```

under `(1.2),(2.6),(2.7)`.  Ordinary divisor bounds give only one choice
per occupied error cell, not the required bound on the number of occupied
cells.

There is no hidden missing-cross-edge condition to exploit: after the
central edge is fixed, a valid left neighbor and a valid right neighbor are
independently selectable.  Their six hard windows already hold, and the
cross determinant identity follows algebraically.  Thus any proof of
`(3.3)` must use the shared central arithmetic in `(1.2),(3.1),(3.2)`, not
an assumed physical witness at the absent cross corner.

## 4. Determinant geometry does not prove dominant-fan inverse

The proposed estimate

```text
|U||V| <<q^o(1)*(K+M_null),                           (4.1)
```

where `M_null` is the largest occupancy product of a null-dual affine-line
pair, is false for shell-scale determinant strips without the physical
mask.  Here is an exact family.

Fix `L=10h` and let

```text
S={(L+i,L+j):0<=i,j<h},
A_N=((N,N-1),(N+1,N)),
B_N=((N,N+1),(N-1,N)),
U=A_N*S,                    V=B_N*S.                  (4.2)
```

For `J=diag(1,-1)`, direct multiplication gives

```text
A_N^T*J*B_N=J.                                        (4.3)
```

Therefore `F(A_N u,B_N v)=F(u,v)`, and for `u,v in S`,

```text
|F(u,v)| <=21h^2=:K.                                  (4.4)
```

Taking `N>>h^3` puts every coordinate in one fixed proportional shell and
makes `K^2=o(q)`.  Both populations are `h^2`, so their product is `h^4`.
An invertible linear map preserves collinearity, and an `h by h` grid has
at most `h` points on a line.  Hence `M_null<=h^2=O(K)`, while

```text
|U||V|=h^4 >>K+M_null.                                (4.5)
```

This family is not an actual-prime-power or hard-product-window family.  It
proves precisely that shell geometry, `K^2<q`, curvature-free line
extraction, and the Cartesian determinant strip cannot establish `(4.1)`.

## 5. What line spread plus local fibres actually gives

There is a rigorous weaker dominant-line inequality.  Let `R_U,R_V` be the
maximum affine-line occupancies and retain the notation `M_null`.  A line
of `R_U` points has integral parameter span at least `R_U-1`.  Endpoint
subtraction covers `V` by `O(K/R_U)` affine fibres in its null direction.
Each such fibre has occupancy at most `M_null/R_U`; hence

```text
|V| <<M_null*(1/R_U+K/R_U^2),
|U| <<M_null*(1/R_V+K/R_V^2).                         (5.1)
```

In the physical shell each whole arm has `O(K)` points by its injective
nonzero determinant label, so `R_U,R_V=O(K)`.  Thus `(5.1)` simplifies,
up to the same shell constants, to the displayed `K*M/R^2` bounds.

The Cartesian line-spread theorem gives

```text
|U||V| <<K*R_U*R_V.                                   (5.2)
```

Combining `(5.1)--(5.2)` yields

```text
|U||V| <<K^(4/3)*M_null^(2/3).                        (5.3)
```

Even a sharp per-null-line theorem `M_null<<Kq^o(1)` therefore returns only
the ambient `K^2q^o(1)` product.  To replace the global affine Carleson
gate, one still needs a mask-sensitive weighted statement: after a disjoint
line/fan allocation, the sum of all transverse blocks and all nondominant
null blocks must be `O(Kq^o(1))`.  Pointwise `O(K)` control of each block
does not supply this summation.

## 6. Verdict

The physical remote null theorem is proved outside the explicit core
`(2.6)--(3.3)`.  Neither unique witnesses, ordinary divisor counting,
`D^2<q`, nor the mixed-error identity eliminates that core.  The strengthened
dominant-fan inverse additionally requires a weighted line-cover theorem;
it does not follow from a local null-line estimate.  These are the two
smallest surviving implications.
