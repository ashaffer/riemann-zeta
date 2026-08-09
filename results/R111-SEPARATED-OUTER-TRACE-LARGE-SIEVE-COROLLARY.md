# R111 separated-outer trace-large-sieve corollary

Status: rigorous corollary of R100 Theorem 5.1 and the weighted R110 trace
energy.  For a finite projective separation of the outer-prime dependence,
it gives an explicit fixed power at the critical scale, conditional only on
the stated separation cost.  It does not assert that the actual completed
R71 coefficients admit such a separation at acceptable cost.

Date: 2026-08-07.

## 1. Setup

Let

```text
P_R={r prime: R<=r<=2R},
f_r(T)=Legendre_r(T^2-4),                             (1.1)
```

and let `F_lambda(h)` be the trace in R110 (1.1).  Suppose an
outer-prime-dependent coefficient has a finite separated representation

```text
C_r(h_1,h_2,h_3,h_4)
 =sum_(j=1)^J omega_j(r) product_(i=1)^4 z_(i,j)(h_i),  (1.2)
```

where every `z_(i,j)` is supported on `[-H,H]`.  Put

```text
Z_j=product_(i=1)^4 norm(z_(i,j))_2,

P_2(D)=sum_j norm(omega_j)_(l^2(P_R)) Z_j,
P_1(D)=sum_j norm(omega_j)_(l^1(P_R)) Z_j,            (1.3)

P_0(D)=sum_j abs(sum_(r in P_R) omega_j(r)/r) Z_j.   (1.4)
```

Here `D` denotes the chosen decomposition (1.2).  The infimum of `P_2(D)`
over all finite representations is the relevant outer/inner projective
tensor cost.  Keeping a chosen representation visible is useful because
the zero Fourier mode has the sharper exact cost (1.4).

Consider only the nonparabolic Legendre-trace sum

```text
Q_np(C)
 =sum_(r in P_R) sum_(h: F_lambda(h)!=plusminus2)
       C_r(h) f_r(F_lambda(h)).                       (1.5)
```

For each `j`, define

```text
A_(j,T)=sum_(F_lambda(h)=T) product_i z_(i,j)(h_i),
             T!=plusminus2.                          (1.6)
```

Assume that every sequence `(A_(j,T))_T` is supported in an interval of
length at most `N`.

## 2. Corollary with the exact zero mode

R100 Theorem 5.1 states

```text
sum_(r in P_R) abs(sum_T A_T f_r(T))^2
 <<(R^2+N)sum_T abs(A_T)^2
   +R^(-1)abs(sum_T A_T)^2.                           (2.1)
```

The last term is not an error estimate.  It is the exact complete zero
Fourier mode

```text
fhat_r(0)=-1,
S_(r,0)(A)=-r^(-1)sum_T A_T.                         (2.2)
```

Combining the nonzero modes in (2.1) with R110 Theorem 1.1 and applying
Cauchy--Schwarz in `r` term by term in (1.2) proves:

**Theorem 2.1 (finite-projective outer trace bound).**  Fix `C>0` and
suppose `1<=abs(lambda)<=H^C`.  For every finite representation `D` in
(1.2),

```text
abs(Q_np(C))
 <<_(C,epsilon) H^epsilon (R^2+N)^(1/2)
       [H+H^(3/2)/sqrt(abs(lambda))]^(1/2) P_2(D)
    +H^2 P_0(D).                                     (2.3)
```

Indeed, R110 gives

```text
sum_(T!=plusminus2) abs(A_(j,T))^2
 <<H^epsilon [H+H^(3/2)/sqrt(abs(lambda))] Z_j^2.    (2.4)
```

For the zero mode,

```text
abs(sum_T A_(j,T))
 <=product_i norm(z_(i,j))_1
 <<H^2 Z_j.                                          (2.5)
```

Equations (2.2) and (2.5) give exactly the second term of (2.3).  Also,

```text
P_0(D)
 <=(sum_(r in P_R)r^(-2))^(1/2) P_2(D)
 <<R^(-1/2)P_2(D),                                   (2.6)
```

so a convenient one-cost version is

```text
abs(Q_np(C))
 <<H^epsilon {
      (R^2+N)^(1/2)
       [H+H^(3/2)/sqrt(abs(lambda))]^(1/2)
      +H^2R^(-1/2)} P_2(D).                          (2.7)
```

The theorem holds for arbitrary finite rank `J`; rank enters only through
the projective cost.

## 3. Critical-scale power saving

Now take

```text
R=H^2,             N<<H^4=R^2.                       (3.1)
```

Then (2.7) becomes

```text
abs(Q_np(C))
 <<H^epsilon [H^(5/2)
               +H^(11/4)/abs(lambda)^(1/4)] P_2(D). (3.2)
```

The zero mode contributes only `O(H P_2(D))` here and is absorbed in
(3.2).

For one separated packet with unit-size outer weights,

```text
norm(omega)_2<<R^(1/2)=H,
P_2(D)<<H Z,                                         (3.3)
```

where `Z=product_i norm(z_i)_2`.  Thus

```text
abs(Q_np)
 <<H^epsilon [H^(7/2)
               +H^(15/4)/abs(lambda)^(1/4)] Z.       (3.4)
```

At `lambda=1`, the second term dominates and (3.4) is

```text
abs(Q_np)<<H^(15/4+epsilon)Z.                        (3.5)
```

The direct coefficient-uniform scale is `H^4Z`.  Hence (3.5) has the exact
relative power

```text
H^(-1/4)=R^(-1/8).                                   (3.6)
```

The coefficient dependence improves this factor.  Relative to `H^4Z`,
(3.4) saves

```text
H^(-1/2)+(H abs(lambda))^(-1/4).                     (3.7)
```

In the power ledger, the dominant saving is `(H abs(lambda))^(-1/4)` for
`1<=abs(lambda)<=H`, and it saturates at `H^(-1/2)` for
`abs(lambda)>=H`.

The support hypothesis `N<<H^4` in (3.1) must be retained.  If one instead
uses the unrestricted natural trace range for growing `lambda`, then
`N` can be as large as `abs(lambda)^2H^4+O(abs(lambda)H^2)` and its
large-sieve cost must be restored.  Formula (2.3), not (3.2), is the
correct statement in that regime.

## 4. Quantitative projective-cost conditions

There are two equivalent useful ways to state when the saving survives.

First, fix a reference packet scale `Z_*` and normalize the projective
overhead by

```text
K_2(D)=P_2(D)/(H Z_*).                                (4.1)
```

At the critical scale, (3.2) gives

```text
abs(Q_np(C))/(H^4 Z_*)
 <<H^epsilon K_2(D)
       [H^(-1/2)+(H abs(lambda))^(-1/4)].             (4.2)
```

Therefore a relative saving `H^(-eta)` survives whenever

```text
K_2(D)[H^(-1/2)+(H abs(lambda))^(-1/4)]
 <=H^(-eta).                                         (4.3)
```

In particular, at `lambda=1` it is enough that

```text
K_2(D)<=H^(1/4-eta).                                 (4.4)
```

If (1.2) has `J` components, each with
`norm(omega_j)_2<<H` and `Z_j<<Z_*`, then `K_2(D)<<J`.  Thus the explicit
rank condition

```text
J<=H^(1/4-eta)                                       (4.5)
```

is sufficient at `lambda=1`.  This is only a convenient sufficient
condition; the projective norm, not raw rank, is the invariant statement.

Second, the direct estimate for the same decomposition is

```text
abs(Q_np(C))<<H^2 P_1(D).                            (4.6)
```

Hence (3.2) improves (4.6) by `H^(-eta)` whenever

```text
P_2(D)/P_1(D)
 <=H^(2-eta)/[H^(5/2)+H^(11/4)/abs(lambda)^(1/4)].   (4.7)
```

At `lambda=1`, this reads

```text
P_2(D)/P_1(D)<=H^(-3/4-eta).                         (4.8)
```

A flat outer vector has `norm(omega)_2/norm(omega)_1=H^(-1+o(1))`, so it
retains the full `eta<1/4` saving.

## 5. Integral-coefficient rescaling

For an ordinary nonzero integral `lambda`, the trace values occupy one
congruence class modulo `lambda`.  This should be used before paying the
additive-large-sieve support length.  Write

```text
P=h_1h_2h_3h_4,
Q=(h_1+h_3)(h_2+h_4),

U=(F_lambda(h)-2)/lambda=lambda P-Q.                 (5.1)
```

Thus `T=lambda U+2`, and for every prime `r` not dividing `2lambda`,

```text
Legendre_r(T^2-4)
 =Legendre_r(lambda U(lambda U+4)).                   (5.2)
```

The map `U |-> lambda U+2` is a bijection modulo `r`.  Consequently the
complete zero mode of the function in (5.2) is still exactly `-1`, its
Parseval mass is still `r(r-2)`, and the proof of R100 Theorem 5.1 applies
word for word with additive frequencies in `U`.  Primes dividing `lambda`
give zero for the ordinary Legendre term and may be discarded.  Hence,
if

```text
B_U=A_(lambda U+2),                                   (5.3)
```

then

```text
sum_(r in P_R) abs(sum_U B_U
          Legendre_r(lambda U(lambda U+4)))^2
 <<(R^2+N_U)sum_U abs(B_U)^2
   +R^(-1)abs(sum_U B_U)^2.                           (5.4)
```

The R110 energy is unchanged because (5.3) is injective.  The natural
support length, however, improves to

```text
N_U<<abs(lambda)H^4+H^2,                             (5.5)
```

instead of the `abs(lambda)^2H^4` length of the unscaled `T` variable.
Thus Theorem 2.1 remains true with `N=N_U` and with the same trace-energy
factor.

At `R=H^2`, using the full natural support (5.5), the nonzero-mode factor
in (2.7) is

```text
<<H^2(1+abs(lambda))^(1/2)
     [H+H^(3/2)/sqrt(abs(lambda))]^(1/2).             (5.6)
```

For one flat outer packet this gives, in the power ledger,

```text
abs(Q_np)
 <<H^epsilon *
   { H^(15/4)abs(lambda)^(1/4) Z,   1<=abs(lambda)<=H;
     H^(7/2)abs(lambda)^(1/2) Z,    abs(lambda)>=H. } (5.7)
```

In particular, for `1<=abs(lambda)<=H` the relative factor against `H^4Z`
is

```text
(abs(lambda)/H)^(1/4).                               (5.8)
```

Thus the rescaled natural-support argument retains a saving `H^(-eta)`
whenever `abs(lambda)<=H^(1-4eta)`.  It reaches the endpoint at
`abs(lambda)asymp H`.  This is the corrected growing-coefficient ledger;
the improving `lambda` dependence in Section 3 applies only when an
independent localization keeps `N<<H^4`.

The excluded parabolic values become `U=0` and, only when it is integral,
`U=-4/lambda`.  Their ordinary Legendre value is zero; the special central
character remains a separate issue.

## 6. Reciprocal coefficients and the normalized integer trace

Suppose now that the finite-field trace coefficient is

```text
lambda congruent k^(-1) (mod r),       (k,r)=1,       (6.1)
```

where `k` is an ordinary nonzero integer.  Multiplying the finite-field
trace by the square `k^2` gives the exact integer polynomial

```text
U_k(h)=P-kQ+2k^2.                                     (6.2)
```

Since `k^4` is a square modulo `r`,

```text
Legendre_r(F_(k^(-1))(h)^2-4)
 =Legendre_r(U_k(h)^2-4k^4).                          (6.3)
```

For fixed `k` independent of `r`, the trace function

```text
g_(r,k)(U)=Legendre_r(U^2-4k^4)                       (6.4)
```

again has complete zero mode `-1` and Parseval mass `r(r-2)` for
`r` not dividing `2k`.  Therefore the same additive large sieve applies in
the integer variable `U`.  Its natural support length is only

```text
N_k<<H^4+abs(k)H^2;                                  (6.5)
```

the constant translation `2k^2` does not enlarge the interval.

The inner arithmetic theorem now required is not literally R110, because
the product and bilinear coefficients in (6.2) are `1` and `k`, rather
than `lambda^2` and `lambda`.  The same balanced/unbalanced mechanism does,
however, prove the following normalized version.

**Theorem 6.1 (reciprocal-normalized trace energy).**  Fix `C>0`, suppose
`1<=abs(k)<=H^C`, and define

```text
C_U=sum_(U_k(h)=U) product_(i=1)^4 z_i(h_i).
```

Then, for every `0<kappa<=1`,

```text
sum_(U!=plusminus2k^2) abs(C_U)^2
 <<_(C,epsilon) H^epsilon
 [H^(2-kappa)+H+abs(k)H^(1+kappa)]
 product_i norm(z_i)_2^2.                            (6.6)
```

Consequently,

```text
sum_(U!=plusminus2k^2) abs(C_U)^2
 <<H^epsilon min{H^2,
                  H+H^(3/2)sqrt(abs(k))}
   product_i norm(z_i)_2^2.                          (6.7)
```

For completeness, here is the proof structure.  In the balanced sector,
share `x=h_1` between two copies and put `n=bcd`, `Q=b+d`.  Equal traces
give

```text
x A=B,
A=(n-n')-k(Q-Q'),
B=k(cQ-c'Q').                                        (6.8)
```

If `A!=0`, the shared coordinate is unique and the two triple products lie
in a band of width

```text
<<abs(k)(H^2/L+H),       L=H^(1-kappa).               (6.9)
```

The product-fiber `l^2` argument of R110 gives the third term of (6.6).
If `A=B=0`, the exact invariant is

```text
(b,c,d) |-> (cbd-k(b+d), c(b+d)),                    (6.10)
```

whose fibers have divisor multiplicity; summing the shared `x` gives the
term `H`.

For the unbalanced sector, the fixed-pair identities are

```text
(u h_2-kx)(u h_4-kx)
 =uU+k^2(h_1^2+h_3^2),                               (6.11)

(q h_3-kh_1)(q h_4-kh_2)
 =kq^2+qU+k^3,

u=h_1h_3, x=h_1+h_3, q=h_1h_2-k.                    (6.12)
```

Nonzero right sides are divisor-bounded.  A zero right side has at most
two rational slope or `q` classes.  Outside `U=2k^2`, a zero opposite-pair
factor forces the scale parameter of `(h_1,h_3)` to divide a fixed nonzero
integer; hence all such zero-factor tuples contribute only
`H^(1+epsilon)`.  The cell `q=0` has divisor-many pairs `h_1h_2=k` and a
nontrivial linear equation in `(h_3,h_4)`, also giving
`H^(1+epsilon)`.  The axes are identical.  Selecting the two smallest
coordinates now proves the restricted-fiber term `H^(2-kappa+epsilon)`.
The value `U=-2k^2` may also be handled this way, but is excluded in (6.6)
because its ordinary character vanishes.  Optimizing `kappa` when
`abs(k)<=H`, and using the general `H^(2+epsilon)` fiber endpoint when
`abs(k)>=H`, proves (6.7).

Combining (6.4)--(6.7) with Theorem 2.1 gives, when `k` is fixed across the
outer-prime family and `1<=abs(k)<=H`,

```text
abs(Q_np,k)
 <<H^(15/4+epsilon)abs(k)^(1/4) Z                    (6.13)
```

for one flat outer packet at `R=H^2`; here (6.5) is still `O(H^4)`.
Relative to `H^4Z`, the surviving factor is `(abs(k)/H)^(1/4)`.

This normalization does not by itself provide the actual R71 lift.  If
`k` varies with `r`, the integer fibers `C_U` in (6.6) also vary with the
outer row, so the common-coefficient hypothesis of the additive large
sieve is lost.  One still needs a finite projective separation in `k` and
`r` satisfying Section 4's cost condition.  In addition, the exact central
levels `U=plusminus2k^2` have zero ordinary Legendre value but can carry the
special `SL_2` central-character correction; that correction remains
outside Theorem 6.1 and R111.

## 7. Scope

Theorem 2.1 applies to the Legendre trace function `f_r(T)` and to the
nonparabolic trace levels.  The special `SL_2(F_r)` character used in the
R71 reduction differs from `f_r(T)` on central matrices.  Its special
central-character correction is not bounded by this corollary and remains
outside (2.3).

Likewise, no assertion is made here that the actual outer-prime-dependent
B-spline weights, common-factor masks, reducible faces, seams, or completed
rectangular limit possess a finite separation with (4.3), (4.4), or (4.7).
R111 proves the exact implication from such a separation; it does not
supply that remaining analytic interface.
