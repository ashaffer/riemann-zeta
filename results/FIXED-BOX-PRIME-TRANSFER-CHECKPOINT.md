# Fixed-box prime-only and transfer checkpoint

Status: analytic checkpoint from standard prime-number-theorem and explicit-
formula inputs, 2026-08-06.  This note does **not** prove RH.

The actual-prime reflection, rough-Euler, and balanced Type-II continuation
is recorded in
[`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`](ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md).

## 1. Verdict

The fixed-box route admits one useful simplification and four sharp
boundaries.

1. Prime powers are not part of the hard term.  For every fixed box length,
   the R65 width theorem remains true after replacing the von Mangoldt sum by
   a sum over actual primes only.
2. The natural coboundary representation exists exactly, but its
   transfer function has the same horizontal-width exponent as the original
   discrepancy.  Its boundedness is itself RH-equivalent.
3. Refining one triangle into smaller triangles is an averaging operator of
   norm one, with infinitely many nonconstant unit modes.  It has no
   scale-uniform contraction.
4. The weakest positive-form route is already only `2 x 2`: positivity on the
   two coherent separated-box directions is equivalent to the missing bound.
   Arbitrarily strong diagonal packet margins do not control that cross term.
5. The centered Selberg/Hankel term is a reflection form: reflection-even
   energy minus reflection-odd energy.  Its positive and negative indices are
   unbounded across the growing support family, and no uniformly finite
   collection of moment, pole, or diagonal constraints can force its sign.

Within the transfer/Selberg route investigated here, the surviving target is
a completed relation coupling **distinct actual primes** across geometric
scales.  The most precise current form is a
power-bounded actual-prime transfer operator for centered geometric Birkhoff
sums, or an arithmetic mixed-prime reflection identity whose zeta-specific
completion supplies the cancellation absent from a generic Hankel square.

## 2. Definitions

Fix `ell>0` and put

```text
w_ell(u) = (1-abs(u)/ell)_+,
M_ell^2 = 16 sinh^2(ell/4)/ell.
```

R65 studies

```text
D_ell(R)
 = sum_n Lambda(n)n^(-1/2) w_ell(log n-R)
   - M_ell^2 exp(R/2).                                      (2.1)
```

Its proved width law is

```text
limsup_(R->infinity) log(1+abs(D_ell(R)))/R = Delta,
Delta = sup_rho abs(Re(rho)-1/2).                            (2.2)
```

Define the actual-prime discrepancy

```text
P_ell(R)
 = sum_p (log p)p^(-1/2) w_ell(log p-R)
   - M_ell^2 exp(R/2).                                      (2.3)
```

## 3. The actual-prime width theorem

### Theorem 3.1

For every fixed `ell>0`,

```text
D_ell(R) = P_ell(R) + ell/2 + o_ell(1).                      (3.1)
```

More precisely, if

```text
Q_(k,ell)(R)
 = sum_p (log p)p^(-k/2) w_ell(k log p-R),
```

then

```text
Q_(2,ell)(R) = ell/2+o_ell(1),
sum_(k>=3) Q_(k,ell)(R)
  = O_ell((1+R)exp(-R/6)).                                  (3.2)
```

The classical quantitative prime number theorem sharpens the first estimate
to

```text
Q_(2,ell)(R)-ell/2 = O_ell(exp(-c sqrt(R)))                  (3.2a)
```

for some absolute `c>0` (after decreasing `c` to absorb the fixed window).
This summable error, rather than the qualitative `o(1)`, is needed below.

In particular, `D_ell-P_ell=O_ell(1)` unconditionally.

### Proof

Only exponents

```text
k <= (R+ell)/log 2
```

can occur.  On the support of the `k`th summand,

```text
exp((R-ell)/k) < p < exp((R+ell)/k).
```

Chebyshev's bound `theta(x)<=C x` therefore gives

```text
Q_(k,ell)(R)
 <= exp(-(R-ell)/2) theta(exp((R+ell)/k))
 <= C exp(-R(1/2-1/k)+ell(1/2+1/k)).                         (3.3)
```

For `k>=3`, summing (3.3) over the `O(R+ell)` possible exponents proves the
second line of (3.2).  The same estimate at `k=2` gives the unconditional
uniform bound `Q_(2,ell)=O_ell(1)`.

For its limit, write the square contribution as a Stieltjes integral against
`theta`:

```text
Q_(2,ell)(R)
 = integral w_ell(2 log t-R) d theta(t)/t.                   (3.4)
```

The prime number theorem and partial summation say that, on every fixed
multiplicative interval, `d theta(t)/t` converges after the change
`v=2 log t-R` to `dv/2`.  Hence

```text
Q_(2,ell)(R)
 -> (1/2) integral_(-ell)^ell w_ell(v)dv
  = ell/2.                                                   (3.5)
```

Equations (3.2)--(3.5) prove (3.1).  QED.

For (3.2a), use the classical zero-free-region form
`theta(x)=x+O(x exp(-c_0 sqrt(log x)))` in (3.4) and partial summation.
Throughout the fixed multiplicative interval in (3.4), `log t=R/2+O_ell(1)`,
which gives the displayed error.

### Corollary 3.2

For every fixed `ell>0`,

```text
limsup_(R->infinity) log(1+abs(P_ell(R)))/R = Delta.          (3.6)
```

Consequently

```text
RH
 <=> P_ell(R)=O_ell(1)
 <=> P_ell(R)=O_(ell,epsilon)(exp(epsilon R))
     for every epsilon>0.                                   (3.7)
```

Indeed, a bounded additive correction cannot change a positive exponential
growth exponent, and under `Delta=0` R65 makes both discrepancies bounded.
This removes Euler prime-power renewal from the hard part of the problem.

## 4. The exact natural coboundary

Put

```text
S(R) = sum_(log n<=R) Lambda(n)n^(-1/2),
A(R) = S(R)-2 exp(R/2),
C_ell(R) = (1/ell) integral_(R-ell)^R A(u)du.                 (4.1)
```

The prime-side spelling is

```text
C_ell(R)
 = sum_(n<=exp(R-ell)) Lambda(n)n^(-1/2)
   +(1/ell) sum_(exp(R-ell)<n<=exp R)
       Lambda(n)n^(-1/2)(R-log n)
   -[4(1-exp(-ell/2))/ell]exp(R/2).                           (4.2)
```

### Proposition 4.1

At every continuity point, and distributionally everywhere,

```text
D_ell(R)=C_ell(R+ell)-C_ell(R).                              (4.3)
```

This follows either by inserting (4.1), or from the elementary ramp identity

```text
w_ell(x)=Phi_ell(x+ell)-Phi_ell(x),
Phi_ell(x)=min(1,max(0,x/ell)).                               (4.4)
```

Thus the desired coboundary was not missing.  The question is whether its
transfer function can be bounded independently.

### Proposition 4.2

For `R>ell`, define

```text
K_ell(s)=(1-exp(-ell s))/(ell s^2).                           (4.5)
```

With the usual symmetric Perron convention,

```text
C_ell(R)
 = -zeta'/zeta(1/2)
   -sum_rho m_rho K_ell(rho-1/2)exp((rho-1/2)R)
   -sum_(m>=1) K_ell(-2m-1/2)exp(-(2m+1/2)R).                 (4.6)
```

The zero series is absolutely convergent because `K_ell(s)=O_ell(abs(s)^-2)`
in the critical strip.  Moreover,

```text
K_ell(s)=0
 <=> s=2 pi i k/ell for a nonzero integer k.                  (4.7)
```

Every zero of this multiplier lies on the imaginary axis, so it cancels no
off-critical zeta zero.  The same one-sided Laplace-pole argument as R65 gives

```text
limsup_(R->infinity) log(1+abs(C_ell(R)))/R = Delta.          (4.8)
```

Hence

```text
RH <=> C_ell=O(1) <=> C_ell is subexponential.                (4.9)
```

This agrees with Suzuki's screw-function criteria: (4.2) is, up to the
explicit archimedean correction, a finite difference of the prime ramp in
the zeta screw function.  The coboundary is therefore a useful normalization,
but not an independent engine.

Every continuous solution of

```text
B(R+ell)-B(R)=D_ell(R)                                       (4.10)
```

differs from `C_ell` by an `ell`-periodic continuous function.  Such a
correction is bounded and cannot remove off-line exponential growth.

## 5. The geometric Birkhoff-sum gate

Iterating (4.3) gives the prime-side identity

```text
sum_(j=0)^(N-1) D_ell(r+j ell)
 = C_ell(r+N ell)-C_ell(r).                                  (5.1)
```

To state the same gate using actual primes, center their discrepancy by

```text
Ptilde_ell(R)=P_ell(R)+ell/2.
```

Then `D_ell=Ptilde_ell+r_ell`, and (3.2a) plus the higher-prime-power bound
give, for every sufficiently large `R_0`,

```text
sum_(j>=0) sup_(r in [R_0,R_0+ell))
  abs(r_ell(r+j ell)) < infinity.                            (5.1a)
```

Thus uniformly bounded Birkhoff sums of `D_ell` are equivalent to uniformly
bounded Birkhoff sums of the **centered actual-prime** discrepancy
`Ptilde_ell`.  Without this centering, the sums of `P_ell` have the linear
drift `-N ell/2+o(N)` even under RH.

Since `C_ell` is bounded on each fixed compact interval, (4.9) is equivalent
to

```text
sup_(r in [R_0,R_0+ell), N>=1)
  abs(sum_(j=0)^(N-1)D_ell(r+j ell)) < infinity.              (5.2)
```

This is the sharp surviving coboundary target.  It asks for uniformly bounded
geometric-scale Birkhoff sums from an actual-prime law.  A proposed
transfer operator should be tested on Mellin modes first: an off-line zero
creates the eigenvalue

```text
exp(ell(rho-1/2)),                                           (5.3)
```

whose modulus is greater than one on the right of the critical line.
Power-boundedness derived without using the zero-side formula would
exclude exactly those modes.

## 6. Why scale refinement is not that transfer operator

Put `h=ell/2`.  The normalized triangular B-splines satisfy the exact
two-scale identity

```text
D_(2h)(R)/(2h)
 = (1/4)D_h(R-h)/h
   +(1/2)D_h(R)/h
   +(1/4)D_h(R+h)/h.                                        (6.1)
```

On a generalized Fourier mode `exp(i xi R)`, the refinement multiplier is

```text
m_h(xi)=cos^2(xi h/2).                                      (6.2)
```

Its norm is one, and

```text
m_h(2 pi k/h)=1                                             (6.3)
```

for every integer `k`.  Finite mixtures of scales still have no uniform gap:
simultaneous Diophantine approximation produces nonconstant frequencies at
which all their multipliers approach one.

For a false-RH mode `exp((delta+i gamma)R)`, the analytic continuation of the
multiplier is

```text
cosh^2((delta+i gamma)h/2).                                  (6.4)
```

At resonant ordinates it has modulus greater than one.  Triangle refinement
is therefore averaging, not a contraction capable of proving (5.2).

The other immediate Euler renewal is equally lossy.  In logarithmic critical
normalization, `Lambda*1=log` becomes

```text
mathcalA * mathcalU = mathcalL.                              (6.5)
```

Solving by the naive Neumann rearrangement uses the kernel
`mathcalU-delta_0`.  On the Laplace line `Re(s)=sigma>1/2`, its
total-variation norm is

```text
norm(mathcalU-delta_0)_sigma
 = sum_(n>=2)n^(-sigma-1/2)
 = zeta(sigma+1/2)-1.                                       (6.6)
```

It is infinite for `sigma<=1/2` and is less than one only far to the right,
after the
unique solution of `zeta(sigma+1/2)=2` (numerically
`sigma=1.228647...`).  Stable inversion farther left is division by
`zeta(s+1/2)` and already requires the zero-free statement being sought.

## 7. The exact `2 x 2` positivity boundary

Let

```text
u_R=T_(-R/2)g_ell,
v_R=T_( R/2)g_ell,
q_ell=Q_W(g_ell,g_ell),
B_ell(R)=Q_W(u_R,v_R).
```

For `R>ell`, `u_R` and `v_R` are orthogonal in the reference `L^2` norm.  For
the real-even Weil distribution, the prime-side formula shows that
`B_ell(R)` is real.  (For a general Hermitian form the lower off-diagonal
entry below would be `conj(B_ell(R))`.)  For
`Q_c=Q_W+c<.,.>_(L^2)`, its matrix on their span is

```text
M_c(R) = [[q_ell+c, B_ell(R)],
          [B_ell(R), q_ell+c]].                              (7.1)
```

Therefore

```text
M_c(R)>=0 for every R>ell
 <=> abs(B_ell(R))<=q_ell+c for every R>ell.                  (7.2)
```

R65 immediately gives

```text
RH
 <=> there is a finite c>=0 for which (7.2) holds.            (7.3)
```

Under RH one may take `c=0`, since the zero-side coefficients
`H_ell(gamma)` are nonnegative and the even extension
`B_ell(-R)=B_ell(R)` is positive definite.  Thus full
Weil positivity is unnecessary for this carrier, but the weakest two-box
positivity is already exactly RH-strength.

More generally, suppose `P` is a Hermitian positive-semidefinite form on all
box translates,

```text
sup_s P(T_s g_ell,T_s g_ell)<=C,
```

and `Q_W+P` is positive on every separated two-box span.  Cauchy--Schwarz for
the two positive forms gives

```text
abs(B_ell(R))<=abs(q_ell)+2C.                                (7.4)
```

Any bounded-diagonal positive completion of this kind already proves RH; it
is not preliminary scaffolding.

### Arbitrarily large cross terms survive diagonal margins

The continuous shifted-atom model in
[`TRIANGULAR-PACKET-CONE-NOGO.md`](TRIANGULAR-PACKET-CONE-NOGO.md) gives a
sharp separation.  Fix `0<=mu<1` and any `A>0`.  Choose

```text
L=1,
d=1-epsilon,
c=(1-mu)/(2 epsilon)>A.                                     (7.5)
```

For sufficiently small positive `epsilon`, every modulated interval packet
obeys

```text
Q(f_(I,tau))>=mu norm(f_(I,tau))_2^2,                        (7.6)
```

while two normalized endpoint boxes have diagonal one and cross term `c>A`.
Under the unitary rescaling `x=epsilon y`, these become boxes of fixed width
one and separation `(1-epsilon)/epsilon`, with the same margin and cross
coefficient.  Thus there is no universal separated-box bound depending only
on a diagonal-packet margin below one, however close that margin is to one.

The zeta pole block does not fix this generically.  Its cross term grows on
the `exp(R/2)` scale and has signature `(1,1)`.  Turning its negative parity
into a positive square also makes the translate diagonals grow on that scale,
so Cauchy--Schwarz merely recovers the uncancelled pole size.  The required
boundedness is precisely the signed prime--pole cancellation in `D_ell`.

## 8. A positivity/PNT/Selberg countermodel

Even a positive prime-like measure with a PNT error `O(x^beta)` for some
`1/2<beta<1` does not control the fixed triangle.  On the logarithmic
half-line `t>=0`, let

```text
d Psi(t)=[exp(t)+epsilon exp(beta t)cos(gamma t)]dt,
1/2<beta<1, 0<epsilon<=1,
```

with `epsilon` small enough that the density is positive.  Its cumulative
mass is `exp(R)+O(exp(beta R))`, a power-saving PNT.  After critical
normalization by `exp(-t/2)`, convolution with `w_ell` retains a nonzero mode
of size

```text
exp((beta-1/2)R).                                            (8.1)
```

The kernel multiplier cannot vanish because `beta-1/2+i gamma` has positive
real part, whereas its nonzero zeros are purely imaginary.  Therefore
positivity plus a PNT error of this size cannot prove the R65 bound.  This
transfer program therefore needs a relation special to the actual primes and
strong enough to couple their phases; the example does not exclude a
different prime-specific global argument.

The same model also passes the generic Selberg-symmetry test.  Write

```text
dP(t)=exp(t)dt,
d nu(t)=epsilon exp(beta t)cos(gamma t)dt,
d Psi=P+nu.
```

Its centered Selberg distribution is exactly

```text
Sigma_epsilon=t nu+2(P*nu)+nu*nu.                            (8.2)
```

Here `P*nu=O(exp(t))`, while `t nu` and `nu*nu` are
`O((1+t)exp(beta t))`.  Consequently

```text
Sigma_epsilon([0,T])=O(exp(T)),                              (8.3)
```

the same remainder scale as the standard Selberg symmetry formula.  Thus
positivity, a power-saving PNT, and the standard Selberg remainder still do
not bound one fixed critical triangle.

## 9. Exact centered Selberg reflection audit

The preceding countermodel reflects an exact identity rather than a weakness
of one estimate.  On the additive logarithmic half-line, let

```text
M = sum_(n>=2) Lambda(n) delta_(log n),
P = exp(t)dt,
N = M-P,
E = exp(-t/2)N,
P_c = exp(t/2)dt.                                           (9.1)
```

Multiplication of a measure by `t` is denoted by `tM`, and `*` is additive
convolution.  Define the centered Selberg distribution

```text
Sigma=tM+M*M-2t exp(t)dt.                                   (9.2)
```

Since `tP+P*P=2t exp(t)dt`, expansion of `M=P+N` and critical
normalization give the exact Riccati identity

```text
Sigma_c:=exp(-t/2)Sigma
 = tE+2(P_c*E)+E*E.                                         (9.3)
```

The standard Selberg symmetry formula is precisely the cumulative estimate

```text
Sigma([0,T])=O(exp(T)).                                     (9.4)
```

Its conventional main term differs from the integral of
`2t exp(t)dt` only by `O(exp(T))`.

For `R>ell`, pair (9.3) with the translated triangle.  Since

```text
D_ell(R)=integral w_ell(t-R)dE(t),
```

one obtains the exact smoothed identity

```text
S_ell(R)
 := integral w_ell(t-R)d Sigma_c(t)
  = integral t w_ell(t-R)dE(t)
    +2 integral w_ell(t-R)d(P_c*E)(t)
    +H_(ell,R)(E),                                          (9.5)

H_(ell,R)(E)
 := integral integral w_ell(u+v-R)dE(u)dE(v).               (9.6)
```

Writing

```text
D^c_ell(x)=integral_[0,infinity) w_ell(t-x)dE(t),
J_ell(R)=integral (t-R)w_ell(t-R)dE(t),
```

gives `D^c_ell(x)=D_ell(x)` for `x>ell` and `D^c_ell(x)=0` for
`x < -ell`.  Expanding the convolution makes (9.5) the concrete
Riccati--Volterra equation

```text
R D_ell(R)+J_ell(R)
 +2 integral_0^infinity exp(u/2)D^c_ell(R-u)du
 +H_(ell,R)(E)
 =S_ell(R).                                                 (9.5a)
```

It is not closed on `D_ell`: it introduces both the first-moment companion
`J_ell` and the indefinite quadratic reflection term `H_(ell,R)`.

Partial summation of only (9.4) gives

```text
S_ell(R)=O_ell(exp(R/2)).                                   (9.7)
```

This is the precise source of the uncancelled critical-scale forcing.
Testing instead with `w_ell(t-R)/t` puts `D_ell(R)` itself in front.  For
large `R` (say `R>=2ell`), it only improves the right side to
`O_ell(exp(R/2)/R)`.  The corresponding weighted two-atom Hankel matrix has
eigenvalues `+1/R` and `-1/R`; division by `t` removes neither the forcing
scale nor the reflection indefiniteness.

There is an equally exact transform audit.  For `Re(s)>1/2`, put

```text
A(s)=integral exp(-st)dE(t)
    =-zeta'/zeta(s+1/2)-1/(s-1/2).                          (9.8)
```

Taking Laplace transforms in (9.3) yields

```text
R_Sigma(s):=integral exp(-st)d Sigma_c(t)
 =-A'(s)+2A(s)/(s-1/2)+A(s)^2
 = zeta''/zeta(s+1/2)-2/(s-1/2)^2.                          (9.9)
```

If `Y(s)=(s-1/2)zeta(s+1/2)`, then `A=-Y'/Y`.  Thus inversion
of this Riccati relation reconstructs a function whose zeros are the shifted
zeta zeros; obtaining zero-free power-bounded inversion is not a free renewal
estimate.

The failure remains visible after filtering to one triangle.  Put

```text
W_ell(s)=integral_(-ell)^ell w_ell(v)exp(sv)dv
        =4sinh^2(ell s/2)/(ell s^2),
Y_ell(s)=W_ell(s)A(s).
```

Then (9.9) becomes

```text
W_ell R_Sigma
 =-Y_ell'
  +(W_ell'/W_ell+2/(s-1/2))Y_ell
  +Y_ell^2/W_ell.                                          (9.9a)
```

Naive deconvolution from only the triangular observable divides by `W_ell`,
which vanishes at every nonzero `2 pi i k/ell`.  For genuine data the
corresponding zeros of `Y_ell` cancel, but this inverse is not bounded on the
boundary `L^2` transform space: `1/W_ell(i xi)` is an unbounded multiplier.
The same issue occurs in standard Hardy or supremum spaces reaching
`Re(s)=0`.  The exact Selberg recurrence therefore does not itself provide a
closed power-bounded scalar transfer.

At the unsmoothed arithmetic level, if

```text
b(n)=Lambda(n)log n+(Lambda*Lambda)(n),
```

then `b*1=log^2` exactly.  Reconstructing `b` is Möbius inversion, with
Dirichlet multiplier `1/zeta`.  More explicitly, for the raw transform
`A_0=-zeta'/zeta`, linearizing `A_0^2-A_0'` sends a perturbation `h` to
`f=2A_0h-h'`.  With the decaying boundary condition in `Re(z)>1`,

```text
h(z)=zeta(z)^(-2) integral_z^infinity zeta(u)^2 f(u)du.      (9.9b)
```

Here the integral is along the horizontal ray `z+[0,infinity)`.

Thus the literal divisor recurrence has a condition operator containing
`1/zeta^2`; it reintroduces the zero-free problem rather than bypassing it.

### The mixed term is a reflection signature

Let

```text
g_ell=ell^(-1/2) 1_[-ell/2,ell/2]
```

and restrict the real locally finite signed measure `E`, supported in
`[0,infinity)`, to `[0,R+ell]`; this does not change (9.6) and makes
`F=g_ell*E` an `L^2` function.  Let `J_R F(x)=F(R-x)`.  The box
autocorrelation identity gives

```text
H_(ell,R)(E)
 = integral F(x)F(R-x)dx
 = norm(F_+)^2-norm(F_-)^2,                                 (9.10)

F_+=(F+J_R F)/2,  F_-=(F-J_R F)/2.                          (9.11)
```

So the mixed-prime term is a reflection signature, not a square.  A sign
would require a new arithmetic imbalance between multiplicatively
complementary logarithmic locations `u` and `R-u`.

### Finite completion cannot create the sign

The first fail-fast test for a fixed-triangle Selberg square is already
negative.  For any signed logarithmic measure `E`, define the centered Hankel
quadratic form

```text
H_(ell,R)(E)
 = integral integral w_ell(u+v-R) dE(u)dE(v).               (9.12)
```

Choose `E=delta_a-delta_b`, `abs(a-b)>=ell`, and `R=a+b`.  Its two diagonal
terms vanish and its two cross terms equal `-1`, so

```text
H_(ell,a+b)(delta_a-delta_b)=-2.                            (9.13)
```

Changing the relative sign of the atoms gives `+2`.  Thus positivity already
fails on zero-mass two-atom data, while the unrestricted two-atom form is
indefinite.  Raw positivity of Selberg's coefficients cannot turn it into a
coercive centered variance.

The obstruction survives exact moment centering and deletion of all diagonal
atom pairs.  For `d>=ell`, take

```text
E=delta_0-2delta_d+delta_(2d).                              (9.14)
```

It has zero mass and zero first moment.  If `H^ne` denotes (9.12) with
the atom-diagonal terms removed, direct evaluation gives

```text
H^ne_(ell,d)(E)=-4,
H^ne_(ell,2d)(E)=2.                                        (9.15)
```

More generally, impose any `m` homogeneous real linear constraints on `E`.
Choose `N>m` points `0<=a_i<=A` separated by more than `ell`, take
`R>2A+ell`, and put `b_i=R-a_i`.  On these `2N` atoms the off-diagonal Hankel
matrix is exactly

```text
[[0,I_N],[I_N,0]].                                          (9.16)
```

Its positive and negative eigenspaces both have dimension `N`, so each meets
the codimension-at-most-`m` constraint space nontrivially.  The same argument
defeats a finite-rank quadratic completion that factors through finitely many
linear functionals: choose the witness in their common kernel.  Fixed affine
terms can be included as one more constraint or dominated by scaling.

For a positive-measure version, first translate the configuration into the
interior of `[0,infinity)` and replace its atoms by sufficiently narrow
disjoint bump bases.  Their Hankel matrix retains inertia `(N,N)`; choosing
coefficients in the exact finite constraint kernel retains the required
moments.  Adding a sufficiently small multiple of this signed bump density to
`exp(t)dt` then preserves positivity and changes the cumulative main term by
only `O(1)`.

This closes generic uniformly finite-rank/moment completed-Hankel positivity,
including diagonal square-prime deletion.  It does not address an
infinite-rank completion or a relation using the exact weights
`(log p)p^(-1/2)`, unique factorization, or correlations specific to the
actual primes.

### Prime-power stripping is linear but not bilinearly harmless

Let

```text
Pi_c = sum_p (log p)p^(-1/2)delta_(log p),
M_c  = exp(-t/2)M,
E_p  = Pi_c-P_c+(1/2)dt,
eta  = (M_c-Pi_c)-(1/2)dt,                                  (9.16a)
```

where `dt` is Lebesgue measure on `[0,infinity)`.  Define the causal
actual-prime extension

```text
Ptilde^c_ell(x)=integral w_ell(t-x)dE_p(t).
```

Then

```text
E=E_p+eta,
Ptilde^c_ell(R)=Ptilde_ell(R) for R>ell.                    (9.16b)
```

Section 3 proves that the local triangle pairings
`r^c_ell(x)=integral w_ell(t-x)d eta(t)` are summable along
`R_0+j ell` and equal `D_ell-Ptilde_ell` for `x>ell`.  But substituting
(9.16b) in the quadratic equation (9.3)
also creates

```text
t eta+2(P_c*eta)+2(E_p*eta)+eta*eta.                        (9.16c)
```

The main convolution already satisfies the exact identity

```text
integral w_ell(t-R)d(P_c*eta)(t)
 = exp(R/2) integral_(-infinity)^R exp(-s/2)r^c_ell(s)ds.    (9.16d)
```

The limiting pole coefficient of this **single** `P_c*eta` term is

```text
M_ell^2 [sum_p log(p)/(p(p-1))-1],                          (9.16e)
```

where the bracket is a convergent explicit constant (numerically
`-0.244633389...`); the full correction (9.16c) contains twice this term.  It
may be moved into an explicit completion counterterm, but it shows why a
locally summable prime-power correction can regenerate an `exp(R/2)` term
after Selberg convolution.  Linear actual-prime elimination does not, by
itself, close the bilinear transfer.

In Dirichlet variables this stripping changes no off-critical spectrum.  If

```text
Prime(z)=sum_p log(p)p^(-z),
A_0(z)=-zeta'/zeta(z),
```

then, initially for `Re(z)>1`,

```text
A_0(z)=sum_(k>=1)Prime(kz),
Prime(z)=sum_(k>=1)mu(k)A_0(kz).                            (9.16f)
```

The `k>=2` tail extends analytically to `Re(z)>1/2`, and the second identity
therefore defines the meromorphic continuation of `Prime(z)` in that
half-plane.  Prime-power stripping subtracts an analytic lower-order function
there; the poles from off-critical zeta zeros remain in the actual-prime
`k=1` component.

The standard Selberg symmetry estimate

```text
sum_(n<=x) [Lambda(n)log n+(Lambda*Lambda)(n)]
 = 2x log x+O(x)                                            (9.17)
```

also does not by itself have the needed critical-scale remainder.  Direct
partial summation of only the `O(x)` information in (9.17) permits an
`O(sqrt(x))=O(exp(R/2))` error after critical normalization.  This observation
does **not** rule out extra cancellation in an exactly smoothed identity, nor
a larger forcing term that is itself a bounded coboundary.

### Surviving checkpoint

The most immediate archimedean completion is exact but does not supply a
sign.  Write `xi=G zeta`, `F=-zeta'/zeta`, and `g=G'/G`.  Then

```text
xi''/xi=F^2-F'-2gF+g'+g^2,
xi''/xi(s)=xi''/xi(1-s).                                   (9.18)
```

The second identity is the functional equation.  It identifies the required
prime--archimedean reflection term, but `xi''/xi` can have poles at the zeta
zeros (some may be removable), while `xi'/xi` necessarily has their
logarithmic poles.  Contour transfer therefore has no divisor-free sign law
for free.  Reflection symmetry alone is not a positive invariant metric.

Within this Selberg/transfer branch, any surviving **completed**
fixed-triangle identity or reflection law would need to:

1. act on the centered actual-prime discrepancy `Ptilde_ell`, without
   obtaining its conclusion by reintroducing zeta zeros;
2. retain mixed terms between distinct primes rather than taking absolute
   values or diagonal variances;
3. be power-bounded on the critical logarithmic normalization; and
4. have either a uniformly summable forcing term or an independently bounded
   coboundary forcing term.

The exact triangular smoothing is now (9.5).  The next calculation is to
use the explicit stripping (9.16a)--(9.16f) and ask whether unique factorization
supplies either:

1. a support-uniform bound on the reflection-odd excess in (9.10); or
2. a transfer identity whose forcing is summable or an independently bounded
   coboundary.

The exact recurrence, its ordinary completion, every fixed finite-codimension
moment completion, and every fixed uniformly bounded-rank quadratic
completion are now closed as independent proof engines.  The remaining gate
within this branch is a genuinely new arithmetic invariant metric or
bounded-coboundary law for the completed reflection transfer, obtained
without division by `zeta` or `W_ell`.

## 10. Evidence and nonclaim

The actual-prime limit uses Chebyshev's bound and the prime number theorem;
summability in (5.1a) uses its classical quantitative zero-free-region form.
The width conclusion additionally imports R65 and hence Guinand--Weil.
Proposition 4.2 is an analytic Perron contour argument for
`R>ell`; its symmetric convention, contour limit, residue bookkeeping, and
trivial-zero series have not been formalized in Lean and require specialist
audit.  The two-by-two statements and shifted-atom separation are elementary
algebra.  The Lean file checks only the scalar equivalence
`q+b>=0 and q-b>=0 <=> abs(b)<=q` and its common-diagonal shift.  It does not
formalize reality of the Weil cross term, box orthogonality, matrix
positivity, the completion estimate, the countermodels, or an RH implication.
Section 8 is an exact elementary continuous-measure countermodel, not a Lean
theorem; it separates the generic hypotheses “positive measure plus an
`O(x^beta)` PNT error plus the standard Selberg `O(x)` remainder” from the
required triangle bound and makes no claim about actual primes.  The
Riccati--Volterra identity, reflection factorization, finite-codimension
no-go, and actual-prime splitting in Section 9 are analytic calculations, not
Lean theorems.  The decimal in (9.16e) is a numerical evaluation of an
explicit convergent constant and is not used as a proof certificate.  None
of these results supplies the bound in (3.7) or (5.2).

The relation to screw functions is consistent with Masatoshi Suzuki,
[*Aspects of the screw function corresponding to the Riemann zeta
function*](https://arxiv.org/abs/2206.03682), which gives several
screw-function equivalents of RH.  No novelty claim is made for the Perron or
screw-function reformulations without a dedicated prior-art review.  The
prime-power elimination, transfer audit, and sharp diagonal/cross separation
are recorded here as a project checkpoint requiring specialist review.
