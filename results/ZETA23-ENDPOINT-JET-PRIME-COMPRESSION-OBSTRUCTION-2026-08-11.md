# Endpoint jets do not by themselves contract the prime lower edge

Status: exact finite-dimensional obstruction, 2026-08-11.  The statements
below apply to the complete sharp prime matrix, with every von Mangoldt
coefficient retained.  They do not prove a lower bound or a zero-free strip.

## 1. Verdict

Let `H_P` be the sign-conjugated sharp prime matrix on the critical grid and
let `W_m` be the endpoint-jet moment-null space.  Endpoint jets have two
important benefits: they cost exactly `m` dimensions and make the remote-zero
tail exponentially small.  They do **not**, merely through their difference
factor, create a small generalized prime eigenvalue.

There are two exact reasons.

1. `W_m` has codimension `m`.  Cauchy interlacing therefore permits the
   compression to discard at most the first `m` negative eigenvalues of an
   arbitrary Hermitian prime matrix.  In the mesoscopic construction
   `m/d=O(eta/log T)=o(1)`.
2. Most coordinate directions have small leverage against the discarded
   polynomial space.  If many confluent diagonal values `D_X(tau_k)` are
   large and positive, at least one corresponding negative diagonal
   Rayleigh quotient survives endpoint compression, up to an explicit
   `O(sqrt(epsilon)*L*B_X)` error.

Thus the formal factor `(1-z)^m` in a difference basis cannot be counted as
an arithmetic power saving.  A successful proof must still use cancellation
in the actual joint law of `A_X,D_X`, or prove the full constrained Pick
inequality at the carrier scale.

## 2. Setup

On the `d` critical nodes put

```text
W_m={x in C^d: sum_k x_k*tau_k^r=0, 0<=r<m},
P=orthogonal projection onto W_m,
Q=I-P.
```

The nodes are distinct, so the `m` moment rows are independent and

```text
dim W_m=d-m,       rank Q=trace Q=m.                  (2.1)
```

For the complete prime matrix, the exact Loewner calculation gives

```text
H_P(k,k)=-2*D_k,
H_P(k,l)=2*(A_k-A_l)/(tau_k-tau_l),       k!=l,       (2.2)

||H_P|| <= 2*max_k abs(D_k)+L*osc_k(A_k)=L*B_X.      (2.3)
```

No prime, prime power, Vaughan head, cofactor, or transition term is removed
in (2.2).

## 3. Exact interlacing obstruction

Write the eigenvalues of `H_P` increasingly as

```text
lambda_1<=...<=lambda_d
```

and those of its compression `P H_P P|W_m` as

```text
mu_1<=...<=mu_(d-m).
```

### Theorem 3.1

For `1<=j<=d-m`,

```text
lambda_j <= mu_j <= lambda_(j+m).                    (3.1)
```

In particular,

```text
mu_1<=lambda_(m+1).                                  (3.2)
```

#### Proof

This is the Poincare separation theorem, obtained directly from the
Courant--Fischer min--max characterization after restricting the admissible
subspaces to `W_m`.  Equation (3.2) says exactly that a codimension-`m`
restriction can pass over at most `m` eigenvalues at the lower edge.  QED

If `S_m` is the usual `m`th-difference matrix with `range(S_m)=W_m`, the
generalized Rayleigh quotient is

```text
b^* S_m^* H_P S_m b / (b^* S_m^* S_m b)
       = x^* H_P x/(x^*x),       x=S_m b.             (3.3)
```

Hence the binomial multiplier visible in both matrices is only a change of
coordinates.  Dropping the mass matrix `S_m^*S_m` would manufacture a false
contraction.

## 4. Coordinate-leverage survival theorem

For each coordinate vector `e_k`, define its discarded leverage

```text
ell_k=<e_k,Q e_k>=||Q e_k||^2.                       (4.1)
```

Then

```text
0<=ell_k<=1,              sum_k ell_k=m.             (4.2)
```

When `ell_k<1`, put

```text
u_k=P e_k/sqrt(1-ell_k) in W_m.                      (4.3)
```

### Theorem 4.1

The vector `u_k` has norm one and

```text
abs(u_k^* H_P u_k+2*D_k)
 <=2*||H_P||*sqrt(2-2*sqrt(1-ell_k))                 (4.4)
 <=2*L*B_X*sqrt(2-2*sqrt(1-ell_k)).                  (4.5)
```

Moreover, for every `0<epsilon<1`,

```text
#{k: ell_k>epsilon} < m/epsilon                      (4.6)
```

with `<=` in (4.6) if the threshold is `>=epsilon`.

#### Proof

Since `<e_k,P e_k>=||P e_k||^2=1-ell_k`, (4.3) is unit and

```text
<e_k,u_k>=sqrt(1-ell_k),
||u_k-e_k||^2=2-2*sqrt(1-ell_k).                     (4.7)
```

For unit vectors `u,e` and Hermitian `H`,

```text
abs(u^*Hu-e^*He)
 <=abs(u^*H(u-e))+abs((u-e)^*He)
 <=2*||H||*||u-e||.                                 (4.8)
```

Use (2.2), (2.3), and (4.7) to obtain (4.4)--(4.5).  Finally, (4.6) is
Markov's inequality applied to the nonnegative numbers in (4.2).  QED

### Corollary 4.2

Let `S` be a set of grid indices with `|S|>m/epsilon`.  Then some `k in S`
satisfies

```text
u_k^*H_Pu_k
 <=-2*D_k+2*L*B_X*sqrt(2-2*sqrt(1-epsilon)).         (4.9)
```

Thus a family of more than `m/epsilon` diagonals satisfying

```text
D_k>L*B_X*sqrt(2-2*sqrt(1-epsilon))                  (4.10)
```

forces a negative direction after endpoint compression.

This is a one-direction statement, not a count of negative eigenvalues.
Its role is fail-fast: endpoint moments alone cannot erase a sufficiently
large family of bad confluent diagonal values.

## 5. Scope and next gate

Theorems 3.1 and 4.1 are coefficient-exact but structurally one-sided.
They do not assert that the actual zeta values `D_k` satisfy (4.10), nor do
they preclude a favorable cancellation between the diagonal and Hilbert
commutator on a particular vector.  They therefore do not replace the
arithmetic task.

They do rule out the following shortcut:

```text
endpoint jets -> mth finite differences -> automatic prime power saving.
```

The remaining alternatives are exactly:

```text
SCALAR ROUTE:
  K=(X^alpha/L)r_T and B_X=o(X^alpha*r_T);

DIRECT PICK ROUTE:
  lambda_min(H_prime,norm|W_m)>=-o(K)
  at the same actual carrier margin K.                (5.1)
```

The unconditional logarithmic estimate
`B_X<<X^(1/2)/(log X)^(3/10)` does not change this conclusion.  It has no
fixed power saving, and (4.3)--(4.10) show why endpoint differencing cannot
simply be multiplied into that scalar estimate.
