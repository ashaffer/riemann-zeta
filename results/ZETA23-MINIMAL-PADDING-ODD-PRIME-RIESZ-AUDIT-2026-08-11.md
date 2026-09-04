# Minimal-padding odd-prime Riesz theorem stops at the Laplace target

Status: exact raw-grid theorem, full-aperture atomic square-root floor, and
exact transfer failure, 2026-08-11.  At
minimal padding, the odd-prime translate atoms have a uniform lower Riesz
margin `1-2/e+o(1)`.  The proposed half-integer augmentation has the same
margin.  This does not give a lower bound for the actual Fourier--Laplace
carrier, nor does it survive lobe and endpoint-jet projection by dimension
alone.  No zero-free strip is proved.

## 1. Verdict

Put

```text
L=log X=log(T/(2*pi))+2*log 2-1+eta,
X/T=(2/(pi*e))*exp(eta),
d=T*L/(2*pi)+O(1).                                   (1.1)
```

For an odd integer `n<=X`, define the normalized critical-grid atom

```text
theta_n=log(n)/L,
v_n(k)=d^(-1/2)*exp(2*pi*i*k*theta_n),   0<=k<d.     (1.2)
```

At minimal padding `eta=o(1)`, every finite family of distinct odd-integer
atoms satisfies

```text
||sum_n c_n*v_n||_2^2
 >=(1-2/e+o(1))*sum_n abs(c_n)^2,                    (1.3)

1-2/e=0.2642411176....                               (1.4)
```

This includes all odd primes and, if desired, all odd prime powers.  A
half-integer atom at the proposed carrier shift can be adjoined without
changing (1.3).

The first failure is not a constant or a prime-power term.  The augmented
atom is a point translate.  The selected-zero carrier is a
Fourier--Laplace row, equivalently a weighted integral of translate atoms.
A lower quotient norm for every one point atom does not give a lower
quotient norm for that integral.  The existing von-Mangoldt/KMT quadrature
in fact gives a logarithmic **upper** approximation to the genuine Laplace
target, fully consistent with (1.3).

There is a second independent failure.  If `P_E` imposes physical-lobe and
endpoint-jet admissibility, the projected Gram matrix subtracts a positive
operator.  Its rank or trace is not enough to protect the target Schur
complement.  Thus the raw theorem is genuine, but it does not close the
prime-translate gate.

## 2. Exact circular spacing

Let `3<=n<n'<=X` be odd integers.  Their ordinary logarithmic gap obeys

```text
(log n'-log n)/L
 >=log(1+2/X)/L.                                     (2.1)
```

The gap across the circular seam is larger:

```text
1-(log n'-log n)/L
 =log(X*n/n')/L>=log 3/L.                            (2.2)
```

Consequently the circular separation of the nodes in (1.2) is

```text
delta_X=log(1+2/X)/L.                                (2.3)
```

Subtracting a common carrier center `log Y` only applies the same diagonal
unitary to every column.  Using the half-integer critical modes
`k+1/2` only multiplies each column by a scalar phase.  Neither operation
changes the Gram spectrum.

## 3. The exact Montgomery--Vaughan margin

The Montgomery--Vaughan cosecant inequality applied to the Dirichlet Gram
matrix gives, for `delta_X`-separated circular nodes,

```text
sum_(k=0)^(d-1) abs(sum_n a_n*exp(2*pi*i*k*theta_n))^2
 >=(d-delta_X^(-1))*sum_n abs(a_n)^2.                (3.1)
```

There is no extra factor two in (3.1).  After the normalization (1.2),

```text
G>= [1-1/(d*delta_X)]*I.                             (3.2)
```

From (1.1) and (2.3),

```text
1/(d*delta_X)
 =2*pi/[T*log(1+2/X)]+o(1)
 =pi*X/T+o(1)
 =2*exp(eta-1)+o(1).                                (3.3)
```

Equations (3.2)--(3.3) prove (1.3).  More generally, the raw margin is
positive throughout

```text
eta<1-log 2-o(1).                                    (3.4)
```

The source for the cosecant inequality is Montgomery--Vaughan,
[*Hilbert's inequality*](https://doi.org/10.1112/jlms/s2-8.1.73),
Theorem 1, equation (1.2).  The exact lower constant produced by that
inequality is `d-delta_X^(-1)`, as in (3.1).  There is no additional `-1`;
the familiar `d-1+delta_X^(-1)` is the sharp **upper** large-sieve
constant and is a different statement.

## 4. The half-integer target really can be adjoined

In the symmetric two-lobe notation, active cross nodes satisfy

```text
X^(1-2*a)<=n<=X,              Y=X^(1-a).             (4.1)
```

Choose

```text
n_*=floor(Y)+1/2.                                    (4.2)
```

For every integer `n`, the closest possible separation obeys

```text
abs(log n-log n_*)
 >=log(1+1/(2*n_*)).                                 (4.3)
```

For every fixed `a>0`, eventually `n_*<=X/4`, so the right side of (4.3)
is at least `log(1+2/X)`.  The augmented family consisting of `v_(n_*)`
and all desired odd-prime or odd-prime-power atoms therefore still
satisfies (1.3).  In particular,

```text
dist(v_(n_*),span{v_p:p odd active prime})^2
 >=1-2/e+o(1).                                       (4.4)
```

Equation (4.4) is a correct theorem.  Its target is the wrong object for
the completed carrier.

## 5. Prime powers do not spoil the power ledger

Every odd prime power is an odd integer, so it can be included among the
columns in (1.3).  Alternatively, null only the odd primes and estimate all
higher powers absolutely:

```text
sum_(p^j<=X,j>=2) log(p)/p^(j/2)=O(L).               (5.1)
```

Indeed, `j=2` contributes

```text
sum_(p<=sqrt X) log(p)/p=O(log X),                   (5.2)
```

and the sum over `j>=3` converges absolutely after extending it to all
primes.  The first power of `p=2` and all powers of two cost only `O(1)`.
With a coefficient-normalized autocorrelation `abs(C(y))<=L`, (5.1)
contributes only `O(1)` after the completed form's `L^(-2)` normalization.
It is negligible beside every fixed positive carrier power.

Including powers of two in the raw Riesz family is not useful: arbitrary
integers have only `log(1+1/X)/L` spacing, changing the formal limiting
margin to `1-4/e<0`.  Absolute treatment is sufficient.

## 6. First failure: a translate atom is not the Laplace row

Let `V` have the active odd-prime translate atoms as columns, and let `Q`
be the quotient map modulo their span.  Equation (4.4) says

```text
||Q*v_(n_*)||>=sqrt(1-2/e)+o(1).                     (6.1)
```

The selected off-line zero does not produce `v_(n_*)`.  Its target is the
projected Fourier--Laplace row `a_alpha`.  In translate coordinates it has
the form

```text
a_alpha=integral_I W_alpha(u)*v(u)du,                (6.2)
```

for the physical cross-lobe window and its exponential depth weight.
Linearity gives

```text
Q*a_alpha=integral_I W_alpha(u)*Q*v(u)du.            (6.3)
```

A pointwise lower bound on `||Q*v(u)||` does not lower-bound the norm of
the signed vector integral (6.3).  The quotient vectors can rotate and
cancel.  Therefore (6.1) supplies neither

```text
dist(a_alpha,span V)>=X^(-o(1))*||a_alpha||          (6.4)
```

nor the Wiener-atomic lower bound required by the polarized two-lobe
problem.

This is not merely an abstract warning.  The exact duality in
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md)
identifies the genuine target with a continuous Laplace moment sequence.
Von-Mangoldt quadrature and KMT give the upper approximation

```text
dist_in_l-infinity(a_alpha,span{prime-log atoms})
 <<(log Y)^(-3/10).                                  (6.5)
```

The constant point-atom margin (6.1) and the vanishing Laplace-target
upper bound (6.5) coexist because their targets differ.  Identifying them
is the exact first failure in the proposed argument.

There is also an exact normalization loss for a flat seed.  Let its `d`
relative-mode coefficients satisfy `abs(r_k)=d^(-1/2)`, let
`||ell||_2=1`, and let the genuine cross carrier have Fourier coefficients

```text
b_k=integral W(u)*exp(2*pi*i*k*u/L)du.               (6.6)
```

Then Cauchy--Schwarz and Parseval give

```text
abs(sum_k b_k*conj(ell_k)*r_k)
 <=d^(-1/2)*(sum_k abs(b_k)^2)^(1/2)
 <=sqrt(L/d)*||W||_2
 =O(T^(-1/2))*||W||_2.                              (6.7)
```

Thus using the raw flat atom as one lobe loses a square-root power in the
normalized Laplace carrier even before lobe or jet projection.  Rescaling
the atom does not repair a Rayleigh quotient, because the coefficient norm
rescales with it.

## 7. Lobe and endpoint-jet projection are a second gate

Let `P_E` be the orthogonal projection onto the permitted lobe space after
endpoint jets.  If `V` denotes the raw column matrix, then exactly

```text
G_E=V^*P_E*V=V^*V-V^*(I-P_E)*V.                     (7.1)
```

For an augmented target `v_*`,

```text
dist(P_E*v_*,span(P_E*V))
 =dist(v_*,span(V)+E^perp).                          (7.2)
```

The subtractive operator in (7.1) is positive.  Prolate dimension and
individual-column concentration do not bound its operator norm on the
entire augmented span.  If the endpoint-jet codimension is `m`, the
subtractive term has rank at most `m`, so at most `m` Gram eigenvalues are
spoiled; the target Schur complement may be one of them.  Even a rank-one
projection can annihilate the raw target residual.

The exact missing theorem is consequently a **target-conditioned projected
Riesz bound**, with the Laplace row rather than a translate atom:

```text
dist(P_(E_- intersect W_m)*a_alpha,
     span{P_(E_- intersect W_m)*T_(log p)*r})
 >=X^(-o(1))*||a_alpha||.                            (7.3)
```

The raw theorem proves only the unprojected point-atom analogue of (7.3).

## 8. Asymmetric length `Y=T^(3/4+o(1))` does not clear the arithmetic gate

For asymmetric lobe fractions

```text
a>1/2,       b->0,       d_(a,b)=1-(a+b)/2,          (8.1)
```

the selected cross center is

```text
Y=X^d_(a,b),
Y=T^(3/4+o(1)),        gamma=T^(1+o(1))=Y^(4/3+o(1)) (8.2)
```

as `a` decreases to `1/2` and `b` to zero.  The exact same-lobe and carrier
powers are

```text
same-lobe: X^(a/2+o(1)),
carrier:   X^(alpha*d_(a,b)-o(1)),
alpha>a/(2-a-b).                                     (8.3)
```

Thus the limiting conditional threshold is `alpha>1/3`, or right edge
`5/6`.

The actual centered prime shell is

```text
S_(Y,w)(gamma)
 =sum_n Lambda(n)/sqrt(n)*omega_w(log(n/Y))*n^(-i*gamma)
  -matching continuum.                              (8.4)
```

KMT applies throughout every fixed power band `Y=T^d`, including `d=3/4`.
After bounded-variation partial summation it gives

```text
S_(Y,w)(gamma)
 <<_w Y^(1/2)/(log Y)^(3/10).                        (8.5)
```

This is larger than `Y^alpha` by

```text
Y^(1/2-alpha)/(log Y)^(3/10)                         (8.6)
```

for every fixed `alpha<1/2`.  At the limiting `alpha=1/3` target, the
missing improvement is a fixed `Y^(1/6)` power.  Equivalently, before the
`n^(-1/2)` normalization one would need a centered von-Mangoldt estimate
of size `Y^(5/6+o(1))`, rather than KMT's `Y/(log Y)^(3/10)`.

Ordinary exponent-pair estimates handle the Type-I pieces, but the balanced
Vaughan Type-II twist is multiplicatively separable:

```text
(m*n)^(-i*gamma)=m^(-i*gamma)*n^(-i*gamma).          (8.7)
```

Generic bilinear bounds absorb both phases into the coefficient sequences
and recover no fixed power.  The currently completed Type-II estimates
therefore remain at `Y^(1/2-o(1))` after normalization.  No unconditional
fixed-power estimate below (8.5) is present in the audited inputs.

This arithmetic conclusion is independent of the promising asymmetric
zero-side mirror geometry.  A bound

```text
S_(Y,w)(gamma)=o(Y^(1/3+epsilon))                    (8.8)
```

uniformly at the selected height would be the new arithmetic statement
needed for the conditional `5/6+epsilon` edge; it is not supplied by the
raw odd-prime Riesz theorem, KMT, exponent pairs applied separately, or the
current completed Type-II route.

## 9. A genuine square-root floor for the full-aperture atomic target

The asymmetric aperture does yield one new unconditional statement about
the genuine smooth target.  Its direction is important: it is a **lower**
bound for the unrestricted Wiener extremal, not an upper bound and hence not
a proof that the actual-prime distance has a power loss.

Let the fixed cross window be supported in a bounded interval, put

```text
b(xi)=integral W(u)*exp(i*xi*u)du,
b(0)=b_0>0,                                          (9.1)
```

and assume the uniform bounded-variation estimate

```text
abs(b(xi))<=C_W/(1+abs(xi)).                         (9.2)
```

The exact triangular target satisfies the stronger `O_W(abs(xi)^(-2))`
bound.  The binomial approximants used in the endpoint packet satisfy
(9.2) uniformly by their audited variation bound.

Let `n_1,...,n_M` be the active odd primes, or the active odd prime powers,
in a fixed multiplicative window

```text
c_1*Y<=n_j<=c_2*Y,
u_j=log(n_j/Y).                                      (9.3)
```

For raw primes the prime number theorem gives

```text
M asymp_W Y/log Y;                                   (9.4)
```

adding the higher odd prime powers changes this by only `O(sqrt(Y))`.
Let `J` contain a low relative critical mode `xi_low=O(1/L)` and, because
the full aperture is `T=Y^(4/3+o(1))`, a consecutive high block `H` with

```text
abs(H) asymp C*Y*L,
c*Y<=abs(xi_k)<=C'*Y,              k in H.           (9.5)
```

Define the exact finite atomic extremal

```text
E_Y=inf_lambda max_(k in J)
 abs(b(xi_k)-sum_(j=1)^M lambda_j*exp(i*xi_k*u_j)).  (9.6)
```

### Theorem 9.1 (square-root floor)

For a sufficiently long fixed-constant block in (9.5),

```text
E_Y>=c_W/sqrt(M)
   >=c_W*sqrt(log Y/Y).                              (9.7)
```

#### Proof

The normalized high-block nodes are `u_j/L`.  Distinct odd integers in
(9.3) have circular separation

```text
delta_Y>=log(1+2/(c_2*Y))/L>=c/(Y*L).               (9.8)
```

Taking the constant in `abs(H) asymp YL` large enough makes the exact
Montgomery--Vaughan lower bound

```text
sum_(k in H) abs(sum_j lambda_j*exp(i*xi_k*u_j))^2
 >=kappa*abs(H)*sum_j abs(lambda_j)^2                (9.9)
```

hold with fixed `kappa>0`.  A common initial frequency in the high block
only multiplies the columns by phases and does not affect (9.9).

Suppose the residual in (9.6) is at most `epsilon`.  Equations (9.2) and
(9.5), followed by (9.9), give

```text
||lambda||_2<=C*(epsilon+Y^(-1)).                   (9.10)
```

At the low mode, `b(xi_low)=b_0+o(1)`.  Cauchy--Schwarz therefore gives

```text
b_0/2-epsilon
 <=abs(sum_j lambda_j*exp(i*xi_low*u_j))
 <=sqrt(M)*||lambda||_2.                            (9.11)
```

If `epsilon>=b_0/4`, (9.7) is immediate.  Otherwise combine
(9.10)--(9.11).  Since `sqrt(M)/Y=o(1)`, this yields
`epsilon>=c_W/sqrt(M)` for all sufficiently large `Y`.  Taking the infimum
over `lambda` proves (9.7).  QED

In the asymmetric geometry `Y=X^(d+o(1))`, `d->3/4`, the guaranteed floor
is only

```text
E_Y>=X^(-3/8+o(1)).                                 (9.12)
```

Consequently this argument alone guarantees only a carrier of scale
`Y^(alpha-1/2+o(1))`, which does not grow for any zeta depth
`alpha<1/2`.  It does **not** say that `E_Y` is at most this size.  The
actual prime-log extremal may be larger.  The coherent-spike model in the
atomic-gate report attains the square-root scale with the same lower-frame
and count information, so no better conclusion follows from those two
inputs alone; obtaining `E_Y>=Y^(-o(1))` requires arithmetic information
beyond them.

There is a separate power obstruction for the particular flat seed which
realizes the raw atoms (1.2).  Equation (6.7), with
`d asymp T*L`, gives for every opposite unit lobe

```text
normalized smooth-target overlap
 <=C_W*T^(-1/2)
 =Y^(-2/3+o(1)).                                    (9.13)
```

Thus that concrete full-grid/Montgomery--Vaughan implementation has carrier
at most `Y^(alpha-2/3+o(1))`, a genuine fixed-power failure for every
`alpha<1/2`.  The upper bound persists when the **opposite** unit lobe is
restricted further, since that only shrinks the vectors over which (6.7) is
optimized.  Projecting and then renormalizing the seed itself generally
produces a nonflat seed and exits this raw-grid calculation.  The bound does
not apply to an arbitrary nonflat seed; for such a seed the raw unweighted
Gram matrix (3.1) is no longer its translate Gram matrix.

Finally, Theorem 9.1 is proved for the unrestricted finite Wiener ball.  An
endpoint-lobe or endpoint-jet restriction makes the feasible correlation
set smaller, and the converse Wiener factorization need not land in the
restricted spaces.  Therefore the lower bound (9.7) does not automatically
descend through those projections.  A projected factorization theorem, in
addition to the arithmetic improvement from `M^(-1/2)` to `Y^(-o(1))`, is
still required.
