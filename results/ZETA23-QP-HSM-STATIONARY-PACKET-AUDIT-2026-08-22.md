# HSM stationary packet and completion audit

**Date:** 2026-08-22  
**Verdict:** the physical zero quotient is removable and the exact stationary
center is proportional, hence diagonal on primitive support.  A rectangular
completion nevertheless has a `q^(3/11)` **absolute stationary-packet
barrier** and an exact nonprincipal modular alias.  The barrier is not a
lower bound for the signed HSM quadratic form.  Three natural attempts to
average the aliases are now sharply audited: positive `SL_2` orbit summation
is false at the target scale, the published scalar BBLR/Watt theorem is not
stable under the four fan weights, and exact ruling sparsity does not imply
the required approximate-energy estimate.  A signed, mask-sensitive packet
theorem remains open.

## 1. Balanced ledger

Throughout,

```text
D=q^(16/33),             P=Q=sqrt(D)=q^(8/33),
R=S=q/sqrt(D)=q^(25/33), L=q/D=q^(17/33),
J=K=q^2/D^(3/2)=q^(42/33),
X=J*K=q^(84/33),         B0=L*R*S/q=q^(34/33).
```

Thus

```text
B0=L^2,             S=L*P,             B0/S=L/P=q^(9/33).
```

For the separated stationary main, the pair coefficient mass is

```text
||u||_2^2 ||v||_2^2 ~ D*X=q^(100/33),
```

and the unscaled HSM target is

```text
L ||u||_2^2 ||v||_2^2=q^(117/33).                 (1.1)
```

## 2. The physical zero quotient is sparse before completion

Write a quotient-chart point as

```text
x=m*(R,S)+r*(U,V),             R*V-S*U=1.          (2.1)
```

The literal zero quotient is `r=0`, so

```text
x=m*(R,S),       gcd(x_1,x_2)=|m|*gcd(R,S)=|m|.   (2.2)
```

An actual primitive vertex therefore has `|m|=1`.  On the positive shell
there is at most the single point `(R,S)`.  In the balanced shell the
required multiplier has size

```text
m~q/R=P=q^(8/33),                               (2.3)
```

so the zero quotient is absent for large `q`.  It may be split off before
filling a quotient interval; splitting the positive and negative quotient
intervals costs only a constant.  This conclusion is about the original
primitive support.  Filling an interval across zero would recreate a new
integer point and is not licensed by (2.2).

The helper `zero_quotient_content` in
`src/qp_four_cycle_weighted_secant_lab.py` replays (2.2) exactly.

## 3. Exact stationary center

On the product fibre `j*k=j'*k'`, put

```text
j=u*j',                 k'=u*k.                    (3.1)
```

For nonzero physical fan indices `r,r',s,s'`, the translation part of the
stationary phase is

```text
Phi=-(U/R)*j'*(r*u-r')-(V/S)*k*(s-s'*u).           (3.2)
```

Its exact interior stationary equations are

```text
r*u=r',       s=s'*u,       (U*r/R)*j'=(V*s'/S)*k. (3.3)
```

In particular,

```text
u=r'/r=s/s',                    r*s=r'*s'.          (3.4)
```

The same relation is forced throughout the normalized stationary tube.  Its
first two inequalities have the form

```text
L*|r*u-r'|<<q^epsilon,       L*|s-s'*u|<<q^epsilon.
```

The exact identity

```text
r*s-r'*s'=r*(s-s'*u)+s'*(r*u-r')                  (3.5)
```

bounds the integral left side by `q^epsilon*P/L=q^(-9/33+epsilon)`.
For fixed sufficiently small `epsilon`, it is less than one and hence
vanishes.  This is an integrality gain at the fan level, not yet a covering
of the whole tube by primal charts.

The inverse stationary map is

```text
a(j,k)=C_a*j^(-2/3)*k^(1/3),
c(j,k)=C_c*k^(-2/3)*j^(1/3).                       (3.6)
```

Equations (3.1) give

```text
a'/a=u=r'/r,                 c'/c=u^(-1)=s'/s.     (3.7)
```

Writing the primal coordinates as

```text
a=R*m+U*r,       a'=R*m'+U*r',
```

one has the exact cancellation

```text
r*a'-r'*a=R*(r*m'-r'*m).                           (3.8)
```

Thus the first equality in (3.7) forces `(m',r')` to be proportional to
`(m,r)`; the color identity is identical.  Positive primitive proportional
integer pairs coincide.  Therefore the exact stationary center on the
actual primitive support is the product diagonal.  The functions
`stationary_fan_cross_identity` and `quotient_proportionality_identity`
replay (3.5) and (3.8) with exact rational/integer arithmetic.

## 4. What rectangular completion still creates

For `x,y~X`, the exact HSM kernel is

```text
K_L(x,y)=sum_ell omega(ell/L)
 e(3*(T/(R*S))^(1/3)*ell^(1/3)*(x^(1/3)-y^(1/3))). (4.1)
```

Writing `h=x-y`, Taylor expansion on the short-shift scale gives

```text
K_L(X+h,X)/L
 ~ integral omega(t)e(kappa*t^(1/3)*h/B0)dt,       (4.2)
```

where `kappa` stays bounded above and below on the dyadic block.  Formula
(4.2) is a signed, generally complex Fourier kernel when `h/B0~1`; it is
not a Fejer kernel and it is not nonnegative on the full short-shift range.

The completed aligned tangent contains `B0/S=L/P=q^(9/33)` packet positions
on that range.  Taking absolute values packet by packet therefore permits

```text
(B0/S)*L*||u||_2^2*||v||_2^2
 =q^(126/33),                                      (4.3)
```

which exceeds (1.1) by `q^(9/33)=q^(3/11)`.  This is the certified
**completed tangent absolute-sum barrier**: a proof that discards the signs
in (4.1) cannot close the target from the present packet bounds.

It is essential not to reverse this statement.  Replacing `K_L/L` by one
in (4.3) is illegal.  A very small `h` subwindow can be chosen so that the
real part of (4.2) is positive, but a positive submoment does not lower-bound
the full off-diagonal quadratic form; the complementary shifts and fan
quartets may cancel it.  Consequently (4.3) is **not** a discrete HSM lower
bound, not a counterexample to `(*)`, and not a four-cycle obstruction.

## 5. Exact nonprincipal alias

The fully nonconstant `SL_2` orbit has stabilizer increment

```text
-d*A*(s*r-s'*r')/(g^2*S).                          (5.1)
```

There is an exact balanced-scale alias.  Choose an integer model with

```text
d=L,        A=Q,        S=L*Q,        g=1,
r=r'=1,    s'=s-1.
```

Then `Delta=s*r-s'*r'=1` is nonprincipal, but

```text
-d*A*Delta/(g^2*S)=-L*Q/(L*Q)=-1.                 (5.2)
```

Its exponential is one.  Thus extracting only the principal relation
`Delta=0` does not control all completion-created tangent modes.  This is
an exact modular identity, not a scale heuristic.  It is replayed by
`nonprincipal_stabilizer_increment`.

## 6. The remaining promotion gate

The certified parabolic/Hankel theory gives

```text
Q_par(z)<<D^(5/4) q^o(1) ||z||_2^4,               (6.1)
```

and rich fixed-direction stationary families factor into rational affine
Hankel charts.  What is not proved is the mask-sensitive passage from the
HSM tube to those charts.  A sufficient promotion lemma must simultaneously:

1. split off the physical zero quotient before any positive completion;
2. cover every actual stationary packet, including one- and two-point and
   varying-direction packets, by `q^o(1)` certified charts or a target-sized
   transverse remainder;
3. preserve enough of the original prime-power mask in every charged packet;
4. complete the transverse complement without introducing new stationary
   triples such as (5.2).

The existing positivity inequality only enlarges the support and proves no
mass-retention statement in the reverse direction.  Hence the current
status is

```text
physical zero-quotient excision:                 PROVED;
stationary fan determinant relation:             PROVED;
primitive exact center is diagonal:              PROVED;
completed tangent absolute q^(3/11) barrier:      PROVED;
that barrier is an HSM lower bound:               FALSE / NOT CLAIMED;
exact nonprincipal d=L alias:                     PROVED;
parabolic/Hankel D^(5/4) chart bound:             PROVED;
mask-sensitive stationary packet covering:       OPEN;
weighted HSM, slope-block theorem, four-cycle:    OPEN.
```

The exact exponent and status assertions are regression-tested by
`src/test_qp_four_cycle_weighted_secant_lab.py`.

## 7. The exact `SL_2` orbit and why positive averaging fails

Write one determinant fibre as

```text
x=d*u,       y=d*v,       (u,v)=1,       h=d*n,
a=alpha*n+v*t,             b=beta*n+u*t,
u*alpha-v*beta=1.                                  (7.1)
```

For row modes `r,r'`, set

```text
A=r*v-r'*u,                 B=r*alpha-r'*beta.     (7.2)
```

The two Poisson windows are

```text
||A/R|| << 1/d,             ||B/R|| << d/H.        (7.3)
```

The matrix

```text
M=(v -u; alpha -beta) in SL_2(Z)                   (7.4)
```

maps `(r,r')` to `(A,B)`.  If `(r,r')=g*(p,p')`, all matrices in one
stabilizer orbit are `M_0*T_k`, and the color phase changes by

```text
-d*A*(s*r-s'*r')/(g^2*S).                          (7.5)
```

Thus `s*r=s'*r'` is the principal zero frequency, but it is not the only
modular zero.  The alias in Section 5 satisfies (7.3) and makes (7.5) an
integer with `s*r-s'*r'=1`.

A tempting sufficient positive estimate would be

```text
sum_(d,u,v,r,r') W_d(A,B)
  |F_Q(d*u/S) F_Q(d*v/S)|
 <<P*Q*N^2/H*q^o,                                  (7.6)

W_d(A,B)=(1+d*||A/R||)^(-C)
         *(1+(H/d)*||B/R||)^(-C).
```

This statement is false uniformly in the fan coefficients.  Already at
`d=1`, the zero residue in the second window has normalized mass `1/R`, not
`1/H`.  For fixed `r,r'<<P`, there are `gg N^2/R` coprime pairs
`alpha,beta~N` with

```text
r*alpha-r'*beta=0 (mod R).                         (7.7)
```

Choose the reduced Bezout solution `u_0*alpha-v_0*beta=1` and translate it
to

```text
u=u_0+2*beta,                 v=v_0+2*alpha.       (7.8)
```

Then `u,v~N`, `(u,v)=1`, and `B=0 (mod R)`.  Hence the uncolored positive
mass is at least

```text
P^2*N^2/R=q^(75/33),                               (7.9)
```

whereas the right side of (7.6) is `q^(66/33)`.  This is the same
`q^(9/33)=q^(3/11)` positive alias floor as in Section 4.  For arbitrary
flat phases `|beta_s|=1`, Steinhaus averaging and Khintchine give a choice
with an additional factor `Q`, namely

```text
Q*P^2*N^2/R=q^(83/33).                             (7.10)
```

Thus Cauchy/Parseval is sharp for a coefficient-uniform positive theorem.
Any successful orbit estimate must retain signed cancellation and must
project away the moving modular zero before absolute values.

## 8. Scalar BBLR/Watt has insufficient weighted headroom

For the centered quadratic-divisor problem, specialize Proposition 3.1 of
[Bettin--Bui--Li--Radziwill](https://arxiv.org/abs/1609.02539) to

```text
A=B=1,              M_1=M_2=N_1=N_2=N.             (8.1)
```

The unrestricted-shift error is

```text
E_0 << N^(3/2)*H+H^2=q^(97/33+o(1)).               (8.2)
```

The fixed-short-shift HSM target is

```text
D*N^2=q^(100/33).                                  (8.3)
```

So the scalar theorem has only `q^(3/33)=q^(1/11)` headroom.  A perfect
Hilbert lift paying the natural `P*Q=D` costs `q^(113/33)`; even a
`sqrt(D)` lift costs `q^(105/33)` and misses (8.3) by `q^(5/33)`.

This is not only an exponent mismatch.  The theorem permits arbitrary
coefficients in only two slots, while the other factor weights must be
slow.  A fan kernel has normalized derivative scale `N*P/R=q^(25/33)`.
Moreover the stronger Watt branch assumes `H<<(A*B)^(1/2+epsilon)`, which
is unavailable when `A=B=1` and `H=q^(34/33)`.  Finally the zero harmonic
moves with the primitive direction: for `d~H`, `u,v~P=Q`, the nonzero fan
quadruple

```text
(r,r',s,s')=(v,u,u,v)                              (8.4)
```

kills both the row phase and the lift frequency and satisfies
`r*s=r'*s'`.  Centering the individual fans therefore does not delete the
principal tangent main.

The weakest useful replacement is a new tangent-projected, fan-aware vector
Watt theorem.  It is not a tensorized consequence of the cited proposition.

## 9. Exact incidence energy is not stable at the HSM tolerance

There is a valid exact-energy theorem behind the decoupling idea.  For a
finite set on a paraboloid, Theorem 16 of
[Rudnev](https://arxiv.org/abs/1806.03534) gives an `n^(5/2)` energy term
plus the contribution of rich isotropic lines.  After the complex linear
identification of `v*w` with a two-square paraboloid, and after dropping the
independent `u`-sum condition, this yields schematically

```text
E_exact(A) << n^(5/2)+k_0*n^2                     (9.1)
```

for `A` on `(u,v,w,v*w)`, provided the `(v,w)` projection is injective.

The required statement is instead approximate at

```text
rho=delta^2=N^(-1).                                (9.2)
```

Exact ruling sparsity does not control it.  Let `M~D`, `M^2<=N`, and put

```text
v_ij=rho*(i+j/(10*M)),
w_ij=rho*(j+i/(10*M)),
A={(0,v_ij,w_ij,v_ij*w_ij):1<=i,j<=M}.             (9.3)
```

Then `n=|A|=M^2~D^2`, the points are `c*rho` separated, all `v_ij` and
`w_ij` are distinct, and each exact ruling contains at most one point.
Even every `rho`-tube around a contained ruling plane contains only
`O(M)=O(sqrt(n))` points.  Nevertheless the additive relations in the
`i,j` indices produce

```text
E_rho(A) >> M^6=n^3,                               (9.4)
```

because the product-coordinate error is `O(M^2*rho^2)<=O(rho)`.  Thus an
estimate `E_rho(A)<<n^(5/2)+mu_rho(A)*n^2` fails by `sqrt(n)` on (9.3).
This rational construction is not an actual-prime counterexample, but it
obeys the currently proved separation and exact-ruling constraints.

The favorable conditional ledger remains informative.  If a genuinely
multiscale actual-mask theorem supplied (9.1) at tolerance `rho`, then

```text
n=D^2=q^(32/33),          mu_rho<=q^(24/33)
```

would give squared loss

```text
max(n^(1/4),mu_rho^(1/2))=q^(12/33)<D,             (9.5)
```

with `q^(4/33)` room.  But the present HSM is a signed Dirichlet-kernel
pair correlation, not the positive energy in (9.1), and rectangular
completion erases the prime-power mask.  Both a multiscale tangent-patch
bound and a mask-preserving reduction would be new inputs.

## 10. Final uniform status

The audits above prove more than a generic statement that the problem is
hard: they identify and populate the precise aliases that defeat each
positive shortcut.  They do not disprove the signed HSM or the four-cycle
bound.  The uniform implication still requires one of:

1. a signed tangent-projected four-fan Watt/HSM estimate at (8.3); or
2. a mask-sensitive stationary-packet decomposition which charges every
   tangent tube to the proved parabolic/Hankel theorem and completes only
   the transverse complement.

Accordingly the uniform four-cycle bound remains open.
