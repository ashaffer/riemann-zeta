# R92 mod-6 eta-vector matrix gate

Status: exact six-state boundary ledger, exact Fourier/reflection
diagonalization, an exact natural moment-matrix calculation, and fail-fast
tests for matrix Herglotz, total positivity, Schur complements, transfer
matrices, and uniform singular-value bounds.  After the exact endpoint mode
is separated, the nonconstant reflection-even sector is `zeta` times
explicit local factors; the reflection-odd sector is the single spectator
`L(s,chi_(-3))` times explicit local factors.  Matrices which retain the odd
sector can stay invertible at a zeta zero and therefore do not detect it.
Matrices which isolate the eta-bearing even sector return `zeta` as a common
scalar factor.  No fixed zero-free strip, and no theorem excluding such a
strip, is proved here.

Date: 2026-08-07.

## 1. Verdict

Keeping all six joint remainder states is useful because it makes the exact
algebra visible.  It does not create a second zeta-bearing analytic degree of
freedom.

Let

```text
f_2(s)=1-2^(1-s),        f_3(s)=1-3^(1-s),
E_2(s)=f_2(s)zeta(s),    E_3(s)=f_3(s)zeta(s).          (1.1)
```

The period-six Dirichlet transforms split, after the discrete Fourier
transform and reflection `r -> -r`, into

```text
reflection-even sector:
  zeta, f_2 zeta, f_3 zeta, f_2 f_3 zeta;

reflection-odd sector:
  L(s,chi_(-3)), (1+2^(1-s))L(s,chi_(-3)).             (1.2)
```

For the interval-difference transforms, the constant Fourier mode `zeta` in
(1.2) is replaced by the exact endpoint `1`.  Thus their complete list is

```text
1; f_2 zeta, f_3 zeta, f_2 f_3 zeta;
L(s,chi_(-3)), (1+2^(1-s))L(s,chi_(-3)).               (1.2a)
```

This gives a sharp matrix dichotomy.

* If the odd sector is retained, it can keep a determinant or a Schur
  complement nonzero when `E_2=E_3=0`.  Such invertibility is compatible with
  a zeta zero and proves nothing about the desired strip.
* If the odd sector and the known endpoint are projected out, every
  remaining entry is `zeta(s)` times a known local factor.  A determinant or
  smallest-singular-value lower bound is then a zeta lower bound in another
  basis.  If the endpoint instead keeps the matrix invertible after the eta
  column vanishes, that invertibility is again irrelevant.

The natural `2 x 2` positive-density moment matrix realizes the first case
exactly.  At a zeta zero `rho` it is, generically,

```text
[[0, -h_2(rho)L(rho)/2],
 [-h_2(rho)L(rho)/2, -L(rho)]],

h_2(s)=1+2^(1-s),       L(s)=L(s,chi_(-3)),            (1.3)
```

whose determinant is `-h_2(rho)^2 L(rho)^2/4`, not zero.  Thus a proof that
this matrix is invertible would not exclude `zeta(rho)=0`.

The strongest elementary determinant which really does detect the common
eta zero is

```text
det [[E_2(s),1],
     [E_3(s),1]]
 = E_2(s)-E_3(s)
 = (3^(1-s)-2^(1-s))zeta(s).                           (1.4)
```

For `Re(s)<1` its explicit prefactor is nonzero, so nonvanishing of (1.4) in
`1-eta<Re(s)<1` is exactly the fixed-strip problem.  But the pointwise mod-6
density determinant changes sign, so total positivity does not prove (1.4).
The prefactor also has a zero lattice on `Re(s)=1`, preventing a uniform
half-plane singular-value bound even though that boundary is already known
to be zeta-zero-free.

No independent matrix order theorem survives these checks.  The honest
remaining target is a signed theorem for (1.4), or an equivalent
reflection-even projection.  That target is not weaker than the requested
fixed strip.

## 2. The six interval states and the boundary term

On a unit interval `[n,n+1)`, put

```text
v_n=(n mod 2,n mod 3)^T.
```

The six states are

```text
r=n mod 6:      0       1       2       3       4       5
v_r:          (0,0)   (1,1)   (0,2)   (1,0)   (0,1)   (1,2).   (2.1)
```

For `Re(s)>0`, define the absolutely convergent interval transforms

```text
D_r(s)=sum_(n>=1, n=r mod 6) [n^(-s)-(n+1)^(-s)].      (2.2)
```

Then the positive Mellin representations from R91 give

```text
E_2=D_1+D_3+D_5,
E_3=D_1+2D_2+D_4+2D_5.                                (2.3)
```

It is important not to replace (2.2) by a cyclic difference without its
endpoint.  In `Re(s)>1`, let

```text
Z_r(s)=sum_(n>=1, n=r mod 6)n^(-s).
```

Directly shifting `n+1` gives

```text
D_0=Z_0-Z_1+1,
D_r=Z_r-Z_(r+1),                 1<=r<=4,
D_5=Z_5-Z_0.                                           (2.4)
```

The `+1` records that `Z_1` contains `n=1`, which is not reached from a
positive multiple of six.  In particular,

```text
sum_(r=0)^5 D_r=1.                                    (2.5)
```

This boundary mode is retained in every calculation below.

## 3. Exact Fourier diagonalization

Let

```text
omega=exp(2 pi i/6),
L_k(s)=sum_(n>=1) omega^(kn)n^(-s),       0<=k<=5.     (3.1)
```

Initially (3.1) is read in `Re(s)>1`; the displayed combinations below
continue to their usual larger domains.  Taking the six-point Fourier
transform of (2.4) gives the exact formula

```text
D_hat_k(s)=sum_r omega^(kr)D_r(s)
          =1+(1-omega^(-k))L_k(s).                    (3.2)
```

For `k=0`, this is precisely `D_hat_0=1`, so (3.2) retains the endpoint in
(2.4).  The two eta coordinates are

```text
E_2=-L_3,
E_3=-(L_2+L_4).                                      (3.3)
```

Now let `chi=chi_(-3)` be the real primitive character modulo three, with
`chi(1)=1` and `chi(2)=-1`, and put `L(s)=L(s,chi)`.  Elementary coefficient
comparison gives

```text
L_0                         = zeta,
L_3                         = -f_2 zeta,
L_2+L_4                     = -f_3 zeta,
L_1+L_5                     = f_2 f_3 zeta,
L_2-L_4                     = i sqrt(3) L,
L_1-L_5                     = i sqrt(3) h_2 L,        (3.4)

h_2(s)=1+2^(1-s).
```

For completeness, (3.4) can be checked without any analytic input.  The
following six coefficient vectors, listed on residues `0,...,5`, form a
basis of all period-six sequences:

```text
sequence                    residue vector                    Dirichlet series

1                    ( 1, 1, 1, 1, 1, 1)                     zeta
1-2 1_(2|n)          (-1, 1,-1, 1,-1, 1)                     f_2 zeta
1-3 1_(3|n)          (-2, 1, 1,-2, 1, 1)                     f_3 zeta
c_6(n)               ( 2, 1,-1,-2,-1, 1)                     f_2 f_3 zeta
chi(n)                ( 0, 1,-1, 0, 1,-1)                     L
(-1)^(n+1)chi(n)      ( 0, 1, 1, 0,-1,-1)                     h_2 L.   (3.5)
```

The first four vectors are invariant under residue reflection and the last
two are anti-invariant.  Thus (1.2) is not a heuristic representation-theory
analogy: it is the complete exact diagonalization of the six states.

In particular, `E_2` and `E_3` both lie in the even sector and their whole
common-zero information is the one scalar `zeta(s)`.  The extra mod-6
coordinates add only the odd `L(s,chi_(-3))` sector and the endpoint mode.

## 4. The natural positive-density matrix is not a zeta detector

The most direct matrix lift keeps the pointwise positive semidefinite
rank-one matrices `v_r v_r^T`:

```text
K(s)=s integral_1^infinity
          v_floor(x) v_floor(x)^T x^(-s-1) dx
    =sum_(r=0)^5 v_r v_r^T D_r(s).                    (4.1)
```

It is holomorphic for `Re(s)>0`.  A finite calculation using (2.1), or the
basis (3.5), gives

```text
K_11 = E_2,
K_12 = E_2+E_3/2-h_2 L/2,
K_22 = 2E_3-L.                                        (4.2)
```

Here the transpose symmetry is literal; at nonreal `s` this is not a
Hermitian matrix.

The sign ledger behind (4.2) is short enough to retain.  For any period-six
scalar state weight `b_r` with `b_0` used at the endpoint, (2.4) gives

```text
sum_r b_r D_r
 =b_0
  +sum_(n>=1)(b_(n mod 6)-b_((n-1) mod 6))n^(-s).     (4.2a)
```

For the off-diagonal state weight `A_2 A_3`, the state and difference
vectors are

```text
b=(0,1,0,0,0,2),
Delta b=(-2,1,-1,0,0,2)
       =(1-2 1_(2|n))
        +(1/2)(1-3 1_(3|n))
        -(1/2)(-1)^(n+1)chi(n).                       (4.2b)
```

For the lower-right weight `A_3^2`, they are

```text
b=(0,1,4,0,1,4),
Delta b=(-4,1,3,-4,1,3)
       =2(1-3 1_(3|n))-chi(n).                        (4.2c)
```

Equations (4.2b)--(4.2c), together with (3.5), prove the last two entries of
(4.2) and make the odd-sector signs explicit.

Suppose `rho` is a zeta zero with `0<Re(rho)<1`.  Then `E_2(rho)=E_3(rho)=0`
and (4.2) becomes (1.3).  Moreover `h_2(rho)` cannot vanish, because

```text
abs(2^(1-rho))=2^(1-Re(rho))>1.                       (4.3)
```

Consequently, whenever `L(rho)!=0`,

```text
det K(rho)=-h_2(rho)^2 L(rho)^2/4 !=0.                (4.4)
```

The natural matrix can therefore be perfectly invertible at a zeta zero.
Its lower bound is not merely insufficient quantitatively; it has the wrong
logical zero set.

The same issue survives the obvious Schur complement.  If `L(rho)!=0`, then

```text
K_11-K_12^2/K_22 = h_2(rho)^2 L(rho)/4.               (4.5)
```

It is again nonzero at the putative zeta zero.  Centering by the first moment
does not help: at `E_2=E_3=0` the centered second-moment matrix is still
(1.3).  Augmenting by the constant coordinate gives the analytic moment
matrix

```text
[[1,E_2,E_3],
 [E_2,K_11,K_12],
 [E_3,K_12,K_22]],                                    (4.6)
```

whose lower-right determinant at a zeta zero is still (4.4).

This is the exact reason that “use the covariance of the two positive
coordinates” does not close the common-zero problem.  The covariance sees
new odd residue information, and that information can support the matrix
after the even zeta-bearing coordinates vanish.

## 5. Matrix positive-real and total-positivity checks

Dividing (4.1) by `s` gives the causal matrix Laplace transform

```text
F(s)=K(s)/s
    =integral_0^infinity C(u)e^(-su)du,

C(u)=v_floor(exp(u))v_floor(exp(u))^T.                 (5.1)
```

The density is pointwise positive semidefinite, but this alone does not make
`F` a matrix Herglotz or positive-real function.  There are two exact early
obstructions.

First, at every artificial eta zero

```text
s_k=1+2 pi i k/log 2,       k!=0,                     (5.2)
```

one has

```text
e_1^* F(s_k)e_1=E_2(s_k)/s_k=0.                       (5.3)
```

Thus the Hermitian part of `F` cannot be strictly positive definite
throughout `Re(s)>0`, and no positive-real lower bound can be uniformly
coercive there.

Second, the matrix density is neither Loewner-increasing nor
Loewner-decreasing.  At the first transition from state `v_1=(1,1)` to
`v_2=(0,2)`, its jump is

```text
v_2 v_2^T-v_1 v_1^T
 = [[-1,-1],
    [-1, 3]],               determinant=-4.           (5.4)
```

It has one positive and one negative eigenvalue.  Every fixed invertible
congruence preserves this inertia.  In the one-hot six-state lift, every
transition has the same obstruction:

```text
e_(r+1)e_(r+1)^T-e_r e_r^T                            (5.5)
```

has one positive and one negative direction.  Hence no fixed change of
state basis turns the six-cycle density into a monotone matrix density to
which the matrix version of R91 Theorem 3.1 applies.

Total positivity fails just as early.  Projection onto the first coordinate
of `v_r` recovers the scalar binary density `B_2`; R91 exhibits an exact
negative order-two Toeplitz minor for that density.  Any matrix total-
positivity theorem which implies total positivity of scalar principal
projections is therefore unavailable.  More specifically, the pointwise
density behind the detecting determinant (1.4) is

```text
det [[A_2(x),1],
     [A_3(x),1]]
 = A_2(x)-A_3(x),                                    (5.6)
```

whose values on residues `0,...,5` are

```text
0, 0, -2, 1, -1, -1.                                 (5.7)
```

They change sign.  Reversing the rows only reverses every sign and does not
make the kernel sign-regular.

For reference, a direct numerical diagnostic also shows that even
semidefinite positive-real behavior is not present for the natural matrix.
At `s=0.55+2i`, the Hermitian part of `F(s)` is approximately

```text
[[ 0.2716170669,  0.3229122577],
 [ 0.3229122577, -0.0221837081]],                     (5.8)
```

with eigenvalues approximately `-0.2300396454` and `0.4794730042`.  The
exact obstructions (5.3)--(5.7), rather than this floating-point witness, are
the proof-level conclusions.

## 6. Transfer matrices and continued fractions diagonalize back to (3.4)

Let `P` be the six-cycle permutation, `P e_r=e_(r+1)`, with indices modulo
six.  For `0<q<1`, the state generating function is exactly

```text
b(q)=sum_(n>=1)q^n e_(n mod 6)
    =qP(I-qP)^(-1)e_0.                                (6.1)
```

The six-point Fourier transform diagonalizes `P`; its eigenvalues are the
sixth roots of unity.  Therefore every finite transfer-matrix elimination,
block Schur complement, or continued-fraction representation of (6.1) is a
repackaging of the six scalar resolvents

```text
q omega^k/(1-q omega^k).                              (6.2)
```

Mellinizing with `q=e^(-t)` gives

```text
Z_r(s)=1/Gamma(s) integral_0^infinity
       t^(s-1) [b(e^(-t))]_r dt,                      (6.3)
```

initially for `Re(s)>1`.  Thus diagonalizing before (6.3) produces exactly
the additive twists `L_k(s)` in (3.1), and reflection produces exactly the
two sectors in (3.4).  A finite continued fraction cannot introduce an
additional analytic coordinate which was absent from this spectrum.

The same conclusion holds for stationary cross-residue covariance.  Any
positive cyclic filter has the form

```text
Q(P)^*Q(P),                                           (6.4)
```

or a limit of such forms, and in Fourier coordinates its eigenvalues are
the nonnegative weights `abs(Q(omega^k))^2`.  It can attenuate or amplify an
eta mode, but it cannot couple that mode to a new common-zero constraint.
If the complementary modes are removed, the retained eta energy is still

```text
abs(zeta(s))^2 times an explicit nonnegative weight.  (6.5)
```

If complementary modes are retained, their energy can stay nonzero when
`zeta(s)=0`, just as in (4.4).

This also identifies where Perron--Frobenius intuition ceases to help.  The
real-`q` resolvent in (6.1) is entrywise positive, but its Perron mode is the
constant residue mode.  Removing that mode to reach the eta coordinates is
a signed Fourier projection.  The resulting non-Perron eigenmodes are
precisely (3.3), so entrywise transfer positivity supplies no strict lower
bound for them.

## 7. Determinants and smallest singular values

Let

```text
e(s)=(E_2(s),E_3(s))^T=zeta(s)f(s),
f(s)=(f_2(s),f_3(s))^T.                               (7.1)
```

The honest Hermitian Gram matrix of the transform vector is

```text
e(s)e(s)^*
 =abs(zeta(s))^2 f(s)f(s)^*.                          (7.2)
```

It has rank at most one.  Every nonzero singular value or quadratic form
obtained from (7.2) is `abs(zeta(s))^2` times a known explicit factor.
Consequently, strict positivity of such a form in a fixed left half-strip is
the desired zeta nonvanishing statement, not an independent consequence of
Gram positivity.

Adjoining one or more eta columns to columns independent of `e` creates the
following fail-fast dichotomy.

1. If the augmented matrix remains invertible after setting `e=0`, its
   invertibility is compatible with a zeta zero and is irrelevant.  The
   natural moment matrix (4.2) is an exact example.
2. If the augmented matrix is structurally singular when `e=0`, multilinear
   expansion in those eta columns has a positive power of `zeta` as a
   factor.  A lower bound for that determinant is then a lower bound for
   `zeta`, up to the explicit remaining factor.

The minimal version of the second case is (1.4).  It is worth recording its
exact scope.  If `Re(s)<1`, then

```text
abs(3^(1-s))=3^(1-Re(s))
           >2^(1-Re(s))=abs(2^(1-s)),                 (7.3)
```

so the prefactor in (1.4) cannot vanish.  Hence

```text
det [[E_2,1],[E_3,1]] !=0 throughout 1-eta<Re(s)<1

if and only if

zeta(s)!=0 throughout 1-eta<Re(s)<1.                  (7.4)
```

This is a clean signed matrix formulation, but (5.7) explains why the
positive interval geometry does not prove it.

There is also no uniform conditioning from the explicit eta vector.  Let
`p_j/q_j` be continued-fraction convergents to

```text
alpha=log(3)/log(2),
```

and set

```text
t_j=2 pi q_j/log(2).                                  (7.5)
```

Then

```text
f_2(1+it_j)=0,
abs(f_3(1+it_j))
 <=2 pi abs(q_j alpha-p_j)
 < 2 pi/q_j.                                         (7.6)
```

Therefore

```text
inf_(abs(t)>T) norm(f(1+it))=0                        (7.7)
```

for every `T`.  With the standard boundary estimate
`abs(zeta(1+it))<<log(2+abs(t))`, (7.6) also gives

```text
norm(e(1+it_j)) << log(t_j)/t_j ->0.                  (7.8)
```

Thus an absolute smallest-singular-value lower bound for a detector using
the eta column is false even on the known zero-free line `Re(s)=1`.
Pointwise division between the two coordinates remains possible, but its
condition number is unbounded along (7.5).

The determinant in (1.4) has the same boundary reality check.  Its explicit
factor vanishes at

```text
s=1+2 pi i k/log(3/2),       k!=0,                    (7.9)
```

although these are not zeta zeros.  One may restrict (7.4) to `Re(s)<1` and
handle the boundary by the classical theorem, but no uniform half-plane
matrix lower bound survives (7.9).

## 8. What remains

The mod-6 vector experiment produces one useful exact reduction and closes
the proposed automatic matrix mechanisms.

The useful reduction is the signed determinant (1.4): it combines two
positive interval transforms, has no artificial factor zeros strictly left
of `Re(s)=1`, and is exactly equivalent there to zeta nonvanishing.

What has been ruled out is obtaining its nonvanishing merely from:

```text
pointwise PSD of the state moments,
Loewner monotonicity after a fixed basis change,
matrix positive-realness of the natural Laplace transform,
order-two total positivity,
a finite six-cycle transfer matrix or continued fraction,
ordinary cross-residue Gram positivity,
or a uniform explicit eta-vector condition number.                  (8.1)
```

The remaining theorem would have to be a genuinely signed, height-uniform
order statement for

```text
E_2(s)-E_3(s)
 =s integral_1^infinity [A_2(x)-A_3(x)]x^(-s-1)dx,    (8.2)
```

or an equivalent reflection-even matrix projection.  Because the density in
(8.2) has the sign pattern (5.7), such a theorem must exploit arithmetic
oscillation beyond finite-state positivity.  By (7.4), proving it in any
fixed strip would already prove the desired fixed zero-free strip.

The six-state lift therefore sharpens the frontier but does not cross it:
the only independent extra analytic sector is `L(s,chi_(-3))`, and it is
either a spectator which makes the matrix blind to zeta zeros or it is
removed, returning the original zeta factor.
