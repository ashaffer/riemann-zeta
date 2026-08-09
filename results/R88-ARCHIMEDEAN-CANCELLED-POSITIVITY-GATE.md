# Archimedean-cancelled positivity and the wrong-sign zero ledger

Status: R88 exact prime-side positivity identity, exact conductor-cancellation
condition, finite- and growing-degree wrong-sign-mass theorem, and PSD/Gram
no-go.  This route does **not** prove a fixed zero-free strip.  It isolates a
new signed correlation estimate which would be sufficient, but which is not
provided by zero density.

The proposed off-axis mechanism was to combine logarithmic derivatives at
the harmonics of a putative zero ordinate so that

```text
prime side >= 0,
the (1/2) log T conductor terms cancel,
the zero beta+iT retains a negative pole.                         (1.1)
```

The first two requirements are compatible.  For example,

```text
P(theta)=2+cos(theta)-cos(2 theta)
        =(1+cos(theta))(3-2 cos(theta)) >= 0                      (1.2)
```

has positive target coefficient and zero sum of its nonconstant cosine
coefficients.  Thus this is not killed by a superficial coefficient-sign
argument.

It is nevertheless killed as a *termwise positivity/zero-density proof* by
an exact ledger identity.  Cancelling the conductor forces negative harmonic
coefficients.  At every negative harmonic, the wrong-sign contribution of
the actual zeta zeros is asymptotic to one half of the coefficient times
`log T`.  More strongly, this has a uniform lower bound which survives an
arbitrary finite degree depending on `T`.  The mass is present even if all
collateral zeros are put on the critical line.  A marginal zero-density
estimate near `Re(s)=1` therefore cannot remove it.

The only live escape is a **signed joint correlation across the dilated
ordinates** `T,2T,...`, conditioned on there being a near-one zero at `T`.
That would be genuinely new information; ordinary zero density is not such a
correlation theorem.

```text
finite trigonometric/Gram positivity             EXACT
archimedean log cancellation                     POSSIBLE
target harmonic retained                         POSSIBLE
pointwise zero-side positivity after cancellation IMPOSSIBLE
wrong-sign collateral mass                       >= (a_1/2) log T-O(1)
control by near-one zero density                  IMPOSSIBLE
signed cross-dilate correlation                   OPEN
fixed zero-free strip                             NOT PROVED.          (1.3)
```

## 2. Exact prime and zero identities

Put

```text
D(s)=-zeta'(s)/zeta(s),                sigma>1.                    (2.1)
```

For real coefficients let

```text
P(theta)=a_0+sum_(1<=k<=m) a_k cos(k theta).                       (2.2)
```

Absolute convergence of the von Mangoldt series gives the exact identity

```text
F_P(sigma,T)
 :=a_0D(sigma)+sum_(1<=k<=m)a_k Re D(sigma+i kT)
  =sum_(n>=2) Lambda(n)n^(-sigma)P(T log n).                       (2.3)
```

Hence

```text
P(theta)>=0 for every theta  ==>  F_P(sigma,T)>=0.                (2.4)
```

This already includes every finite scalar Fejer--Riesz or matrix-Gram
construction: a sum of squared trigonometric polynomials is just another
nonnegative `P`.

For a nontrivial zero `rho=beta+i gamma`, define

```text
L_(sigma,rho)(u)
 =(sigma-beta)/[(sigma-beta)^2+(u-gamma)^2],

Z_sigma(u)=sum_rho L_(sigma,rho)(u).                              (2.5)
```

The sum in (2.5) is absolutely convergent.  Let

```text
E_sigma(u)=Re[1/(sigma+iu)+1/(sigma-1+iu)],
G_sigma(u)=-1/2 log(pi)+1/2 Re psi((sigma+iu)/2).                  (2.6)
```

Hadamard factorization of `xi` supplies a real convention constant
`C_xi`, independent of `sigma,u`, for which

```text
Re D(sigma+iu)
 =E_sigma(u)+G_sigma(u)-C_xi-Z_sigma(u).                          (2.7)
```

One may instead choose the standard paired Hadamard normalization and absorb
`C_xi` into that normalization.  Keeping it visible makes all estimates
independent of a product convention.

For fixed `sigma>1`,

```text
G_sigma(u)=1/2 log(|u|/(2 pi))+O_sigma(u^(-2)),
E_sigma(u)=O_sigma(u^(-2)),
|D(sigma+iu)|<=D(sigma).                                         (2.8)
```

Consequently

```text
Z_sigma(u)=1/2 log(|u|/(2 pi))+O_sigma(1)                         (2.9)
```

uniformly for `|u|>=2`.  There is also a one-sided version, needed below:
for an effective constant `C_sigma`,

```text
Z_sigma(u)>=1/2 log |u|-C_sigma,                 |u|>=2.           (2.10)
```

This is not a density heuristic.  It follows directly from (2.7), the
digamma bound, and the absolutely convergent prime-series bound in (2.8).

## 3. The exact conductor-cancellation condition

At the high harmonics, (2.8) gives

```text
sum_(k>=1)a_k G_sigma(kT)
 =A/2 log T+1/2 sum_(k>=1)a_k log(k/(2 pi))+o_(P,sigma)(1),

A=sum_(k>=1)a_k.                                      (3.1)
```

Thus the high-ordinate conductor cancels if and only if

```text
A=0.                                                               (3.2)
```

If `rho_0=beta+iT`, its contribution to the weighted zero sum is

```text
sum_(k>=1)a_k L_(sigma,rho_0)(kT)
 =a_1/(sigma-beta)+O_P((sigma-beta)/T^2).                           (3.3)
```

So `a_1>0` retains exactly the desired target pole.  Formula (1.2) proves
that (2.4), (3.2), and `a_1>0` can all hold at once.

There are, however, two unavoidable coefficient facts.  Write

```text
B_+=sum_(a_k>0,k>=1)a_k,
B_-=sum_(a_k<0,k>=1)|a_k|.                                        (3.4)
```

Then (3.2) and `a_1>0` imply

```text
B_+=B_->=a_1.                                                      (3.5)
```

Also, nonnegativity gives

```text
a_0=(1/(2 pi)) integral_(-pi)^pi P(theta)dtheta>0,
|a_1|<=2a_0                                                        (3.6)
```

for every nonzero `P`.  Thus the zero-frequency term, and therefore the
pole-sized quantity `a_0D(sigma)~a_0/(sigma-1)`, cannot be removed inside
the positive cone.

### Why `P(0)=0` and higher vanishing do not help

Since

```text
P(0)=a_0+A,                                                        (3.7)
```

conductor cancellation gives `P(0)=a_0>0`.  Imposing `P(0)=0` as well forces
`a_0=0`; a nonnegative trigonometric polynomial of mean zero is identically
zero.  Higher-order vanishing at zero is therefore also incompatible with a
nontrivial conductor-cancelled member of this cone.

If one imposes `P(0)=0` without (3.2), then `A=-a_0`, so the high-ordinate
term is `-(a_0/2)log T`: it has not been cancelled.  It must be restored by
wrong-sign zero mass.  The simplest example `1-cos(theta)` displays exactly
this transfer.

## 4. Fail-fast theorem: the deleted conductor reappears in zeros

### Theorem 4.1 (uniform wrong-sign zero ledger)

Fix `sigma>1`.  For each `T` let `P_T` be any finite nonnegative
trigonometric polynomial of the form (2.2); its degree and coefficients may
depend on `T`.  Assume

```text
sum_(k>=1)a_k(T)=0,                 a_1(T)>0.                       (4.1)
```

Define the zero contribution carried by the negative harmonics by

```text
W_-(sigma,T)
 =sum_(a_k(T)<0)|a_k(T)| Z_sigma(kT).                              (4.2)
```

Then there is an effective `T_sigma` such that, for `T>=T_sigma`,

```text
W_-(sigma,T)
 >=B_-(T)[1/2 log T-C_sigma]
 >=a_1(T)[1/2 log T-C_sigma].                                     (4.3)
```

In particular, after normalizing `a_1(T)=1`, every such
conductor-cancelled construction has a wrong-sign collateral-zero term at
least `(1/2)log T-O_sigma(1)`.

#### Proof

For every negative harmonic, `kT>=T`, so (2.10) gives

```text
Z_sigma(kT)>=1/2 log T-C_sigma.                                   (4.4)
```

Sum (4.4) with weights `|a_k(T)|` and apply (3.5).  No restriction on the
degree is used.  Take `T_sigma` large enough that the bracket in (4.3) is
nonnegative before applying the second inequality.

The lower bound counts all nontrivial zeros.  Restricting a zero-density
theorem to `beta>1-eta` cannot reduce it: the ordinary bulk of zeros supplies
(2.9).  In particular, moving every collateral zero to `beta=1/2` does not
remove the logarithmic term.  Removing the target quartet itself changes
(4.2) by at most `O_sigma(B_-(T)/T^2)`, since every negative harmonic has
`k>=2`; hence the same conclusion holds for genuinely collateral zeros.

### Corollary 4.2 (no pointwise zero-side sign)

Let `ell_a(x)=a/(a^2+x^2)`, where `a>0`, and put

```text
K_(P,T)(y)=sum_(k>=1)a_k ell_a(y-kT).                              (4.5)
```

Under (4.1),

```text
integral_R K_(P,T)(y)dy=pi sum_(k>=1)a_k=0.                        (4.6)
```

Distinct translates of `ell_a` are linearly independent.  Hence a
nontrivial `K_(P,T)` takes both signs.  There is no way to cancel the
conductor and then discard every collateral zero by a pointwise nonnegative
zero kernel.  This remains true under RH, where `a=sigma-1/2` is common to
all zero kernels.

### Concrete two-harmonic counterexample

For (1.2), (2.3) says

```text
2D(sigma)+Re D(sigma+iT)-Re D(sigma+2iT)>=0.                       (4.7)
```

The two high gamma factors contribute only

```text
-1/2 log 2+o(1),                                                   (4.8)
```

and the zero at `beta+iT` has coefficient `+1/(sigma-beta)`.  But
the minus sign at `2T` produces on the other side

```text
Z_sigma(2T)=1/2 log T+O_sigma(1).                                 (4.9)
```

Thus an absolute value or a marginal density bound recreates the exact
logarithmic loss which (4.8) appeared to remove.

## 5. The cone is not too small: shifted Fejer kernels approach the sharp
target/pole ratio

The obstruction is genuinely the joint zero term, not an inability to put
enough coefficient on the target.  Let

```text
F_N(theta)=1+2 sum_(1<=k<=N)(1-k/(N+1))cos(k theta)                (5.1)
```

be the Fejer kernel.  Choose `theta_N` between zero and its first zero so
that `F_N(theta_N)=1`, and set

```text
P_N(theta)=[F_N(theta-theta_N)+F_N(theta+theta_N)]/2.              (5.2)
```

Then

```text
P_N>=0,       a_0=1,       P_N(0)=1,       sum_(k>=1)a_k=0,
a_1=2N/(N+1) cos(theta_N) -> 2.                                  (5.3)
```

Thus the universal bound `a_1<=2a_0` in (3.6) is asymptotically sharp even
inside the conductor-cancelled slice.  Fejer--Riesz/PSD freedom cannot improve
the target-to-pole ratio beyond two, but it can get arbitrarily close.  The
reason the method stops is Theorem 4.1, not a weak target coefficient.

## 6. General PSD combinations do not create a hidden translated version

For real frequencies `tau_j` and complex coefficients `c_j`, absolute
convergence gives the Hermitian Gram identity

```text
sum_(j,l)c_j conjugate(c_l)
 D[sigma+i(tau_j-tau_l)]

=sum_(n>=2)Lambda(n)n^(-sigma)
 |sum_j c_j n^(-i tau_j)|^2 >=0.                                  (6.1)
```

Two facts follow.

1. Only **differences** `tau_j-tau_l` survive.  Translating every `tau_j` by
   a large central ordinate cancels out of (6.1); it does not move all sample
   points to high ordinate.

2. The diagonal difference zero has coefficient

```text
sum_j |c_j|^2>0                                                     (6.2)
```

   unless the construction is zero.  This is the Gram version of `a_0>0`
   and leaves the zeta-pole cost at `D(sigma)~1/(sigma-1)`.

Sums of Gram squares have the same properties.  Therefore matrix PSD,
multiple squares, and Fejer--Riesz factorization do not evade Sections 3--4.
They merely give different parameterizations of the same positive cone.

### Cauchy averaging is an exact radial PSD lift, but it dilutes the target

There is one natural scale-dependent variant worth checking explicitly.
Average (2.3) in `T` against the Cauchy probability density

```text
w_H(x)=H/[pi(H^2+x^2)],                   H>0.                    (6.3)
```

Since the integrand is nonnegative, its average is nonnegative.  The Fourier
transform of `w_H` gives the exact identity

```text
bar F_(P,H)(sigma,T)
 =a_0D(sigma)+sum_(k>=1)a_k Re D(sigma+kH+i kT)>=0.                (6.4)
```

On the prime side, the bracket is

```text
a_0+sum_(k>=1)a_k r^k cos(k theta),
r=n^(-H), theta=T log n,                                         (6.5)
```

which is the Poisson extension of `P` and is therefore nonnegative.  Thus
(6.4) is a genuine PSD operation, not an inequality loss.

It still does not change the ledger.  Every high gamma factor has leading
term `(1/2)log T`, so its cancellation condition remains `sum a_k=0`, and
every fixed negative harmonic still carries `(1/2)log T+O(1)` zero mass.
Meanwhile the target pole is weakened exactly from

```text
a_1/(delta+epsilon)  to  a_1/(delta+epsilon+H).                   (6.6)
```

This follows either from (6.4) or from the convolution law for two Cauchy
kernels.  Taking `H` large enough to damp the low prime frequencies therefore
dilutes the target on the same horizontal scale.  Cauchy averaging may be
useful inside a future target-conditioned correlation theorem, but by itself
it does not evade Theorem 4.1.

## 7. What a real escape theorem would have to say

Before conditioning on a target zero, even a signed joint estimate of the
right scale is false.  The obstruction is vertical almost periodicity.

### Proposition 7.1 (unconditioned signed bounds are too large)

Fix a nonconstant conductor-cancelled `P` and let

```text
M_P=max_theta P(theta)>a_0.                                       (7.1)
```

For each fixed `delta>0`, Kronecker approximation and absolute convergence
give a sequence `T_nu -> infinity` on which, for any chosen `theta_*`,

```text
F_P(1+delta,T_nu)
 ->sum_p sum_(r>=1)(log p)p^(-r(1+delta))P(r theta_*).             (7.2)
```

Indeed, the numbers `log p` are rationally independent over every finite
set of primes, and the tail of (2.3) is absolutely small.  Choose
`P(theta_*)=M_P`.  Since the terms `r>=2` stay bounded as `delta -> 0+`,

```text
F_P(1+delta,T_nu)=M_P/delta+O_P(1),
a_0D(1+delta)=a_0/delta+O_P(1).                                  (7.3)
```

It follows from (2.7) and conductor cancellation that the full signed zero
fluctuation has, along these sequences,

```text
sum_rho sum_(k>=1)a_k L_(1+delta,rho)(kT_nu)
 =-(M_P-a_0)/delta+O_P(1).                                       (7.4)
```

Thus no estimate uniform in all `T` can replace the logarithmic term by a
small harmless constant.  Any successful lower bound must use the special
conditional information that `T` itself is the ordinate of a zero very near
one.  This is substantially stronger than merely keeping the harmonics
joint.

Put `delta=sigma-1`, let a hypothetical zero be

```text
rho_0=1-epsilon+iT,                                                (7.5)
```

and remove its functional-equation quartet from the zero sum.  For a fixed
conductor-cancelled `P`, define the signed collateral term

```text
J_P^off(delta,T)
 =sum_(rho not in quartet(rho_0)) sum_(k>=1)
   a_k (1+delta-beta)/[(1+delta-beta)^2+(kT-gamma)^2].             (7.6)
```

Equations (2.3), (2.7), and (3.2) reduce the desired contradiction to a
lower bound on (7.6).  Up to fixed `P,delta` constants and `o(1)`, the ledger
has the form

```text
0<=F_P
 =a_0D(1+delta)+C_P
  -a_1/(delta+epsilon)-J_P^off(delta,T),

C_P=1/2 sum_(k>=1)a_k log(k/(2 pi)).                              (7.7)
```

The reflected zero at `epsilon+iT` adds another same-sign bounded term; it
has been omitted in (7.7), making the displayed requirement weaker.

Hence a sufficient new input would be a target-conditioned estimate

```text
J_P^off(delta,T)>=-R_P(delta)                                     (7.8)
```

with a constant small enough that

```text
a_1/(delta+epsilon)
 >a_0D(1+delta)+C_P+R_P(delta).                                   (7.9)
```

For the family (5.2), `a_1/a_0` can approach two, so (7.9) has genuine
coefficient reserve when `delta` is a fixed multiple greater than one of
`epsilon`.  But Theorem 4.1 shows that (7.8) cannot come from bounding the
negative harmonics separately.  It must cancel logarithmic masses between
different dilates before absolute values.

Using (2.7), the centered signed collateral fluctuation is equivalent, up
to explicit gamma and target terms, to the prime almost-periodic sum

```text
sum_(k>=1)a_k Re D(1+delta+i kT)
 =sum_(n>=2)Lambda(n)n^(-1-delta)
   sum_(k>=1)a_k cos(kT log n).                                  (7.10)
```

Thus (7.8) is not a repackaged one-point zero-density estimate.  It is a
correlation/repulsion theorem coupling the zero process near all of
`T,2T,...` to the exceptional event that a zero near `Re(s)=1` occurs at
`T`.  No such theorem has been established in this repository.

## 8. Decision

The archimedean-cancellation idea passes its first algebraic test and fails
its proposed easy analytic closure:

* nonnegative/PSD prime weights can cancel the high conductor and retain a
  positive target coefficient;
* cancellation necessarily creates at least the same amount of negative
  harmonic coefficient;
* the zeta explicit formula forces those harmonics to carry wrong-sign zero
  mass `>= (a_1/2)log T-O(1)`;
* `P(0)=0`, higher vanishing, Fejer--Riesz, and matrix Gram lifts do not
  remove this ledger;
* ordinary zero density near one cannot control a mass supplied by the full
  critical-strip bulk.

The route should therefore not be pursued through another polynomial search
or a sharper marginal density constant.  Its only noncircular continuation
is the signed, target-conditioned cross-dilate estimate (7.8), or a mechanism
which proves the same cancellation before the zero sum is separated.
