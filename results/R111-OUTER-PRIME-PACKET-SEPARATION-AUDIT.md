# R111 outer-prime packet separation and native-interface audit

Status: equation-level audit of the R71--R89--R100 packet interface.  On a
genuine Blomer--Pascadi short-interval box, both the universal completion
profiles and the actual R81 B-spline line amplitude have an explicit
arbitrarily-small-power projective separation in a varying outer prime.
Autocorrelation, `Q_h`, a subpower common factor, and the full ordered shell
matrix preserve that separation.  This does **not** yet give a complete R71
estimate: the only exact full Vaughan-to-fixed-modulus formula in R105 has a
composite modulus and full-Fourier/modular-inverse coefficient supports, not
the two short intervals to which the trace construction applies.  In
addition, the trace coefficient is a modular inverse of the R81 shift
product; removing that row dependence requires the reciprocal-normalized
trace-energy lemma now stated as Theorem 6.1 of the companion
`R111-SEPARATED-OUTER-TRACE-LARGE-SIEVE-COROLLARY.md`, not literally R110 as
originally stated. The full R71-to-short-box lift remains absent.

Date: 2026-08-07.

## 1. Verdict

There are three distinct coefficients which were compressed into the
placeholder notation `z_(i,r)` in R89--R100.  They must not be conflated.

1. The actual center-annihilated R71 kernel is

   ```text
   f_R(t)=t^(-1/2)V_Q(R-log t),

   L_Q(t,u)=integral psi(R)f_R(t)conjugate[f_R(u)]dR.       (1.1)
   ```

   Its exact solution-line amplitude is

   ```text
   A_(g,p,r,theta)(j)
    =g integral L_Q(u+gj,u)e(theta u/(gpr))du.              (1.2)
   ```

   This is where the B-spline and all nine `Q_h` cross-translates live.

2. Once a scalar fixed-modulus bilinear Kloosterman box has actually been
   produced, the Blomer--Pascadi trace method introduces universal Fourier
   completion profiles `w_(1,r),w_(2,r)`.  Their autocorrelations are the
   four `z_i` in the length-four trace.  They do not contain the arbitrary
   input sequences; those sequences have already been replaced by their
   `l2` norms in the spectral-norm inequality.

3. A primitive reduced-rational parametrization may insert the periodic
   common-`g` mask of R87.  The transformed finite nonprimitive expansion of
   R104 avoids this mask altogether.

The first two families are smoothly/projectively separable across a dyadic
outer-prime interval as long as their scaled oscillation parameters are
subpower.  More precisely, a rank and projective cost

```text
L << Z+A log H                                             (1.3)
```

is available, where `Z` is the maximum phase variation when `R/r` moves in
`[1/2,1]`.  Autocorrelation squares this cost.  Thus `Z=H^o(1)` is enough;
a power-sized `Z=H^sigma` spends the power `H^sigma` before R110's gain is
used.

Two issues must be kept separate; the first now has a companion theorem,
while the second is the surviving native-interface obstruction.

* Up to reflecting one Kloosterman coordinate, the R81 reciprocal phase has
  Kloosterman multiplier `k=plusminus j theta`. The
  trace word contains `lambda=inverse(k) mod r`, which is not a smooth
  function of the outer prime.  There is an exact discriminant
  renormalization to a common polynomial. Its weighted energy is the
  reciprocal-normalized variant of R110 proved in the companion R111,
  subject to that theorem's final audit.
* R105's exact full-tail formula does not give the short-interval box whose
  universal weights are separated below.  It gives one full discrete
  Fourier transform and one modular-inverse image.  Low-rank separation of
  a hypothetical short-box weight cannot fill that missing bridge.

Consequently R110 and its reciprocal-normalized companion supply a real
arithmetic saving, but the fixed strip does not yet follow.

## 2. Backward trace to the actual R71 coefficient

After applying `Q_h` before localization, R102 gives

```text
integral_0^infinity f_R(t)dt=0.                         (2.1)
```

R104 then gives the exact finite nonprimitive cofactor expansion

```text
D_Q(R)
 =sum_(q<=bX)c(q)/q sum_(a!=0) fhat_R(a/q),
c(q)=-mu(q)log q,                                      (2.2)
```

and, for the recombined Vaughan tail,

```text
D_Q(R)=sum_q a_(U,V)(q)/q sum_(a!=0)fhat_R(a/q)+e_Q(R), (2.3)
```

where `e_Q` is already power-small on the admitted blocks.  Squaring (2.2)
or (2.3), writing

```text
q_1=gp,       q_2=gr,       (p,r)=1,
theta=ar-bp,                                             (2.4)
```

and applying Poisson summation on the solution line gives exactly (1.2).
Thus the only outer-`r` occurrence in the kernel amplitude is

```text
e([theta u/(gp)]/r).                                    (2.5)
```

This is the formula to separate.  It is stronger and cleaner than saying
only that “the B-spline is smooth”: no derivative of a spline seam is
needed for separation in `r`.

For the canonical cofactor coefficient, if `r` is prime and `(g,r)=1`,

```text
c(gr)/(gr)=mu(g)[log g+log r]/(gr).                    (2.6)
```

This has exact rank two in `r` and may in any case be absorbed into the
outer scalar weight.  For the Vaughan coefficient `a_(U,V)(gr)/(gr)` no
smoothness in `r` is asserted, but for fixed `g` it is still an outer scalar;
the trace large sieve permits arbitrary outer scalars.  The difficulty is
row dependence inside the four trace packets, not an arbitrary prefactor.

## 3. The exact Blomer--Pascadi/Pascadi profiles

The relevant source chain is:

* Blomer--Pascadi,
  [*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311),
  Proposition 3.1 and equations (3.7)--(3.8);
* Pascadi,
  [*Non-abelian amplification and bilinear forms with Kloosterman sums*](https://arxiv.org/abs/2511.08445),
  Corollary 4.11 and its proof.

Let the fixed modulus be the prime `r`, let

```text
I=[M]+s_1,          J=[N]+s_2,
K_(m,n)=S(a m,n;r),       (a,r)=1.                    (3.1)
```

Choose once and for all a smooth majorant `Phi`, supported in `[-1,2]`,
with `Phi>=1_[0,1]`.  Before truncating its rapidly decaying Fourier tails,
Pascadi's proof gives the profiles

```text
w_(1,r)(h)=Phihat(hM/r)e(-s_1 a h/r),
w_(2,r)(h)=Phihat(hN/r)e(-s_2 h/r).                   (3.2)
```

Up to the harmless scalar `MN/r^2`, the group-algebra packet is

```text
sum_(h_1,h_2 in Z)
 w_(1,r)(h_1)w_(2,r)(h_2)
 1_[T^(inverse(a)h_1) S T^h_2].                       (3.3)
```

The published proof truncates at

```text
abs(h_1)<=r^(1+epsilon)/M,
abs(h_2)<=r^(1+epsilon)/N                              (3.4)
```

and absorbs the tail into `O_epsilon(r^-100)`.  For an outer dyadic family
it is better to retain (3.2), choose one common truncation height for all
`r in [R,2R]`, and keep `MN/r^2` as an outer scalar.  This removes the
artificial row-dependent sharp boundary in (3.4).

For the fourth trace, Blomer--Pascadi define, with `j=1` for odd indices
and `j=2` for even indices,

```text
z_(i,r)(d)
 =(4/H_j)sum_(x-y=d)w_(j,r)(x)conjugate[w_(j,r)(y)].   (3.5)
```

The word is

```text
G=T^(inverse(a)h_1)S T^h_2 S
  T^(inverse(a)h_3)S T^h_4 S,                         (3.6)
```

and

```text
Tr(G)
 =lambda^2h_1h_2h_3h_4
  -lambda(h_1+h_3)(h_2+h_4)+2,
lambda=inverse(a) mod r.                              (3.7)
```

Equations (3.2) and (3.5), not an unspecified “B-spline packet”, are the
exact outer-prime-dependent autocorrelations in the published short-box
trace step.

There is also an important scope point.  The arbitrary input coefficients
`alpha_m,beta_n` in (3.1) do not occur in (3.2)--(3.5).  Proposition 3.1
first bounds the bilinear form by

```text
norm(alpha)_2 norm(beta)_2 times the spectral norm of K. (3.8)
```

The actual R71 B-spline amplitude must therefore be separated into scalar
input sequences **before** this trace construction is invoked.  It cannot
be recovered by changing `z_i` after the fact.

## 4. A rigorous projective separation theorem for (3.2)

The following elementary lemma gives the needed rank with explicit phase
dependence.

**Lemma 4.1 (dyadic reciprocal-parameter separation).**  Let
`r in [R,2R]`, `abs(h)<=K`, and put

```text
w_r(h)=Phihat(Mh/r)e(-s a h/r),
Z=[(3M+abs(sa))K]/R.                                  (4.1)
```

For every `A>=1` there are functions `omega_l(r)` and `v_l(h)`, with

```text
w_r(h)=sum_(0<=l<=L)omega_l(r)v_l(h)+E_r(h),

L<<_Phi Z+A log H,
sup_l,r abs(omega_l(r))<=1,
sum_(l<=L)sup_h abs(v_l(h))<<_Phi L,
sup_(r,h)abs(E_r(h))<=H^-A.                           (4.2)
```

Here one may take

```text
omega_l(r)=T_l(4R/r-3),                               (4.3)
```

where `T_l` is the Chebyshev polynomial.  Thus (4.2) is simultaneously a
rank bound and an `l1` projective-norm bound.

**Proof.**  With `e(x)=exp(2 pi i x)`, Fourier inversion in (3.2) gives

```text
w_r(h)=integral_(-1)^2 Phi(t)
          e(-[Mt+sa]h/r)dt.                           (4.4)
```

Put `x=R/r` and `y=4x-3`, so `y in [-1,1]`.  For fixed `(t,h)`, the
integrand in (4.4) is a constant phase times `exp(i gamma y)` with
`abs(gamma)<<Z`.  The standard Chebyshev/Bessel expansion of an exponential,
or the elementary Taylor remainder followed by conversion to the Chebyshev
basis, has uniform degree-`L` error `<=H^-A` once
`L>>Z+A log H`.  Integrating its coefficients against `Phi` proves the
expansion.  A Chebyshev coefficient of a function bounded by
`norm(Phi)_1` on `[-1,1]` has magnitude at most `2norm(Phi)_1`; summing the
`L+1` coefficients gives the projective bound.  QED.

The second profile in (3.2) is Lemma 4.1 with `M,s,a` replaced by `N,s_2,1`.
At the critical lengths

```text
M,N asymp sqrt(R),      K asymp sqrt(R) times a tail margin, (4.5)
```

the scaled bandwidths are

```text
Z_1<<tail_margin*[1+abs(a)s_1/M],
Z_2<<tail_margin*[1+abs(s_2)/N].                      (4.6)
```

Hence fixed-ratio interval endpoints and `abs(a)=H^o(1)` give subpower
rank.  A power-sized multiplier `a=H^sigma` costs rank `H^(sigma+o(1))`;
it is not free.

There are two legitimate tail choices.

1. With an arbitrary fixed `C_c^infinity` majorant, take a common height
   `K=(R/M)H^eta`.  Repeated Fourier decay makes the omitted tail `H^-A`
   after choosing enough fixed derivatives.  The rank is `H^(eta+o(1))`.
   Since `eta>0` is arbitrary, this is an arbitrarily-small-power loss.
2. Choose the permitted majorant `Phi` in a fixed Gevrey class of order
   `s>1`.  Then `Phihat(x)<<exp(-c abs(x)^(1/s))`; a common height
   `(R/M)(log H)^s` has power-small tail and gives literal `H^o(1)` rank.

No exact nontrivial finite-rank identity is asserted.  The dependence
`e(-sa h/r)` is a reciprocal-parameter Vandermonde-type family; the useful
statement is the uniform projective approximation (4.2).

### Corollary 4.2 (autocorrelation separation)

Use one common support `[-K,K]` and define

```text
z_r(d)=kappa sum_x w_r(x)conjugate[w_r(x-d)],
abs(kappa)<<1/K.                                       (4.7)
```

If (4.2) has rank `L`, then, up to an error `H^-A` after increasing `A`,

```text
z_r(d)=sum_(l,m<=L)
 omega_l(r)conjugate[omega_m(r)]Z_(l,m)(d),            (4.8)

Z_(l,m)(d)=kappa sum_x v_l(x)conjugate[v_m(x-d)].
```

Thus the rank is at most `(L+1)^2`.  Young's inequality and (4.2) give

```text
sum_(l,m<=L)norm(Z_(l,m))_2<<_Phi L^2 K^(1/2).        (4.9)
```

The natural `l2` scale of one bounded autocorrelation packet is `K^(1/2)`,
so the relative projective cost is `L^2`.  A product of four such packets
costs at most `L_1^4L_2^4`, still `H^o(1)` when both completion bandwidths
are subpower.

## 5. Direct separation of the actual B-spline line amplitude

The analogous result for (1.2) is even more direct.

**Lemma 5.1 (R71 kernel separation in the outer prime).**  Suppose one
fixed physical shell in (1.2) has `0<u<=U_*`, and define

```text
Z_A=abs(theta)U_*/(g abs(p)R).                        (5.1)
```

For every `A>=1`, uniformly in `r in [R,2R]`,

```text
A_(g,p,r,theta)(j)
 =sum_(l<=L_A)T_l(4R/r-3)A_l(g,p,theta,j)+Err_r,

L_A<<Z_A+A log H,
sum_l abs[A_l(g,p,theta,j)]
 <<L_A g integral abs[L_Q(u+gj,u)]du,

abs(Err_r)
 <<H^-A g integral abs[L_Q(u+gj,u)]du.                (5.2)
```

**Proof.**  Equation (1.2) is an integral mixture of exponentials in
`R/r`, now with frequency

```text
gamma(u)=theta u/(gpR),       abs(gamma(u))<=Z_A.      (5.3)
```

Apply the same Chebyshev approximation inside the absolutely convergent
integral.  QED.

This proof uses the full actual `L_Q`; every B-spline knot and all nine
cross-translates are already inside its `L1` mass.  Expanding

```text
V_Q=sum_(q=0)^2 b_q V(.+qh)                           (5.4)
```

first merely multiplies the number of kernel packets by nine.  It is not
needed for Lemma 5.1 and cannot create a power loss.

The low-band condition is now exact:

```text
abs(theta)U_* <=H^o(1) g abs(p)R.                    (5.5)
```

For power-sized `Z_A`, the rank in (5.2) is power-sized.  Integration by
parts in the physical variable may make some high-`Z_A` boxes small, but
that is a separate kernel-tail estimate; separation itself does not erase
them.

## 6. Common-`g` masks and shell recombination

### 6.1 The mask

The safest transformed coordinate is R104's finite **nonprimitive** basis:
there is no primitive common-`g` mask in (2.2), and the rational axes and
reducible faces are already polylogarithmic.

If a primitive reduced-rational basis is nevertheless used, R87 gives

```text
M_g(ell)
 =1_((a_0+p ell,g)=1)1_((b_0+r ell,g)=1)

 =sum_(nu mod g)Mhat_g(nu)e(nu ell/g).                (6.1)
```

This is an **exact** rank-`g` expansion in the solution-line variable. Its
coefficients may depend arithmetically on the outer prime: with the standard
section `a_0 r=theta (mod p)`, they are periodic only modulo `pg`, not merely
modulo `g`. This does not require a second Fourier expansion. For fixed
`nu`, the factor

```text
Mhat_(g,r)(nu)e(-nu x_0(r)/g)                         (6.2)
```

is independent of the line frequency `j`, so it is an admissible arbitrary
outer scalar in the projective trace theorem. Thus the mask has raw packet
rank at most

```text
g,                                                     (6.3)
```

and Parseval for the normalized finite Fourier transform gives
`sum_nu abs(Mhat_(g,r)(nu))<=sqrt(g)`. Hence its projective overhead is at
most `sqrt(g)`, before the reciprocal-parameter separation of Lemma 5.1.
This is harmless on `g=H^o(1)` sectors; a power-sized common factor still
spends a power. R104's nonprimitive expansion avoids even this charge and
should be the default in a strip proof.

### 6.2 Shells

Let `chi_s` be a physical partition and put

```text
f_(R,s)=chi_s f_R,       m_s(R)=integral f_(R,s)(t)dt.
```

Then

```text
sum_s m_s(R)=0,          m_s(R) need not equal 0.      (6.4)
```

The marginal-null kernel is the full ordered matrix

```text
L_Q=sum_(s,t)integral psi(R)
       f_(R,s) tensor conjugate[f_(R,t)]dR.            (6.5)
```

The correct order is:

1. form `Q_h` and (6.5);
2. use the full identity `Lhat_Q(xi,0)=Lhat_Q(0,eta)=0` to remove the two
   original Fourier axes;
3. retain all ordered `(s,t)` cross-shell packets;
4. sum every axis correction introduced by a later fixed-modulus
   completion, obtaining zero from (6.4);
5. only then apply Cauchy, the trace bound, or a triangle inequality to the
   genuinely off-axis packets.

A proportional B-spline has only `O(log X)` dyadic physical shells, so the
full ordered matrix costs `X^o(1)`.  Bounding shell axes separately is not
an `X^o(1)` approximation: it destroys the exact signed zero in (6.4) and
can recreate the original contact at natural size.

Output localization `psi=sum psi_j` is safe.  Each `psi_j` kernel is
separately marginal-null because (2.1) holds pointwise in `R`.

## 7. The modular-inverse trace coefficient

In the R81 application the reciprocal phase is

```text
e_r(-j theta inverse(p)).                              (7.1)
```

Using symmetry and simultaneous sign change of Kloosterman sums, one may
orient the completed box so that its multiplier in (3.1) is
`k=plusminus j theta`; reflecting the other interval switches the sign.
Fix one orientation and call that signed integer `k`. Although (3.2)
depends smoothly on this fixed integer, the trace
coefficient in (3.7) is

```text
lambda_r=inverse(k) mod r.                             (7.2)
```

This row dependence is not Mellin- or Chebyshev-separable.  R100's common
integer trace coefficients `A_T` therefore do not exist with (3.7) as
written.

There is an exact workaround at the character level.  Put

```text
P=h_1h_2h_3h_4,
Q=(h_1+h_3)(h_2+h_4),
U_k=P-kQ+2k^2.                                         (7.3)
```

For `(k,r)=1`,

```text
k^2 Tr_(lambda_r)(h)=U_k(h)                 (mod r),

( [Tr_(lambda_r)(h)^2-4]/r )
 =( [U_k(h)^2-4k^4]/r ).                              (7.4)
```

The multiplier `k^4` is a square, so (7.4) is exact.  Thus for each fixed
integer `k` the outer prime sees the common trace function

```text
f_(r,k)(U)=( [U^2-4k^4]/r ).                          (7.5)
```

If `r` does not divide `2k`, then exactly as in R100,

```text
sum_(U mod r)f_(r,k)(U)=-1,
sum_(xi mod r)abs(fhat_(r,k)(xi))^2=r(r-2).           (7.6)
```

Therefore the varying-prime additive trace large sieve remains available
after (7.4).  The finitely many outer primes dividing `2k` are elementary.

This energy theorem is not a word-for-word corollary of R110. Formally,

```text
U_k=k^2 F_(1/k),                                      (7.7)
```

but R110 is stated for an integral coefficient `lambda`, not the rational
coefficient `1/k`. The companion
`R111-SEPARATED-OUTER-TRACE-LARGE-SIEVE-COROLLARY.md`, Theorem 6.1, now
supplies the normalized estimate

```text
sum_U abs(sum_(U_k(h)=U) product_i z_i(h_i))^2
 <<H^epsilon[H+H^(3/2)sqrt(abs(k))]
      product_i norm(z_i)_2^2,                        (7.8)
```

at least for `abs(k)<=H^C`.  The expected outer-trace gain is then

```text
H^(-1/4+o(1))abs(k)^(1/4).                            (7.9)
```

Its proof must retain a point which a formal rescaling of R110 misses. For
example, the opposite-pair factorization becomes

```text
(h_1h_3h_2-k(h_1+h_3))
(h_1h_3h_4-k(h_1+h_3))

 =k^2(h_1+h_3)^2+h_1h_3[U-2k^2],                    (7.10)
```

whose right side can vanish at nonparabolic `U` when the associated
quadratic has a rational nonunit root.  Those zero strata satisfy the
additional divisor identity

```text
(h_1h_2-k)(h_2h_3-k)=k^2                             (7.11)
```

when the first factor in (7.10) vanishes. The companion proof handles these
zero strata separately. Thus (7.8) may now be imported after its final
audit; it is no longer the native-interface obstruction isolated here.

## 8. Parabolic and special central terms after `Q_h`

Center annihilation removes the linear R87 marginal.  It does **not** make
the autocorrelation value `z_i(0)` vanish.  For the prime-modulus special
character,

```text
chi_r^circ(G)=r                      if G=plusminus I,
              (Tr(G)^2-4 / r)       otherwise.        (8.1)
```

The ordinary Legendre contribution at every noncentral trace
`Tr(G)=plusminus2` is zero.  Only the two special central loci remain.

For the word (3.6), with `lambda` a unit modulo `r`, direct multiplication
gives

```text
G=I  iff
 [h_2=h_4=0, h_3=-h_1]
 or
 [h_1=h_3=0, h_4=-h_2],                              (8.2)

G=-I iff
 h_1=h_3,       h_2=h_4,       lambda h_2h_3=2       (mod r). (8.3)
```

On a common completion range of length `o(r)`, (8.2) has no aliases and
the central correction is exactly

```text
C_I(r)=r[
 z_2(0)z_4(0)sum_x z_1(x)z_3(-x)
 +z_1(0)z_3(0)sum_y z_2(y)z_4(-y)
 -product_i z_i(0)],                                  (8.4)

C_(-I)(r)=r sum_(lambda xy=2 mod r)
 z_1(x)z_3(x)z_2(y)z_4(y).                           (8.5)
```

Equations (8.4)--(8.5) prove the coefficient-uniform bound

```text
abs(C_I)+abs(C_(-I))
 <<r product_i norm(z_i)_2.                           (8.6)
```

For the actual BP autocorrelations one has the stronger pointwise fact

```text
abs(z_i(h))<<1,                                       (8.7)
```

and (8.2)--(8.3) contain only `O(H_1+H_2)` points.  Hence

```text
abs(C_I)+abs(C_(-I))
 <<r^(1+o(1))max(H_1,H_2).                            (8.8)
```

At `H_1,H_2 asymp sqrt(r)`, this is `r^(3/2+o(1))`, a full factor
`sqrt(r)` below the `r^2` four-variable trace scale.  It comfortably
preserves R110's quarter-power gain in a native BP short box. This is the
prime special case of the central term already isolated in the proof of
Blomer--Pascadi Proposition 3.6. The companion
`R112-CENTRAL-MATRIX-CORRECTION-BOUND.md` records the same classification
with aliases and the sharper scale-invariant flat-profile estimate.

Thus the parabolic verdict is precise:

```text
linear R87 axes after Q_h                  ZERO;
noncentral trace plusminus2 Legendre term   ZERO;
special G=plusminus I correction            NONZERO / PAIRED;
actual BP central size                      POWER-SMALL, (8.8). (8.9)
```

Using only arbitrary weighted `l2` packets loses the improvement from
(8.7), so a downstream proof must retain their autocorrelation origin for
the special center.  `Q_h` alone does not prove (8.8).

## 9. Why this is not yet an exact full-R71 bridge

R105 derives the exact optimistic fixed-modulus formula for the transformed
Vaughan tail.  With the first top cofactor product fixed as a modulus
`c asymp X`, and the second product unfolded as `q=db`, it is

```text
F_c(k)
 =sum_(d in I_d,b in I_b)alpha_d beta_b e_c(k inverse(db))

 =c^-1 sum_(h,n mod c)
    alphahat(h)betatilde(n)S(kh,n;c),                 (9.1)

betatilde(n)=beta_(inverse(n))
              1_(inverse(n) in I_b).                 (9.2)
```

This is an exact bilinear Kloosterman form, but:

```text
modulus c                  composite cofactor product, c~X;
first coefficient support full Fourier residue system;
second support             inverse image of a sqrt(c) interval;
BP hypothesis              two additive intervals of length sqrt(c). (9.3)
```

Partitioning the two residue systems into `sqrt(c)`-length intervals
introduces the block factor recorded in R105 (5.9).  It is nontrivial only
if the product of effective block counts is `<c^(1/16-o(1))`; no such
concentration is known for the rough `mu` Fourier transform and the inverse
image of the `Lambda` interval.

Most importantly for the present audit, the prime `r` in Sections 3--8 is
not supplied as the native fixed modulus of (9.1).  Passing from the
composite `c` to a prime divisor by CRT leaves the complementary factor in
the inverse-product phase.  It does not produce (3.1) with two short
intervals and a scalar outer weight.

Therefore Lemmas 4.1 and 5.1 prove the separation property of every
short-interval packet **once such a packet is present**.  They do not prove
that the complete R71/Vaughan field is a subpower projective sum of those
packets.  That is now the exact analytic bridge obstruction.

## 10. Concrete next lemma and exponent ledger

The shortest sufficient successor is the following single statement.

**Target lemma (completion-preserving varying-prime trace packet).**  On
each center-annihilated R71 block, after the original finite cofactor/Vaughan
recombination, write the entire nonparabolic off-axis contribution as

```text
sum_(g,k,box) sum_(r~R prime) omega_(g,k,box)(r)
  sum_(nu<=H^o(1)) Omega_nu(r)
  sum_h product_(i=1)^4 z_(i,nu)(h_i)
    ( [U_k(h)^2-4k^4]/r )                             (10.1)
```

plus a power-smaller error, with all of the following properties.

1. The total projective norm in `nu`, ordered shells, `Q_h` translates,
   and subpower common factors is `H^o(1)`.
2. The two original Fourier axes are canceled **before** the expansion;
   every shell cross term and its fixed-modulus axis correction is retained.
3. The special central term is kept in the paired form (8.4)--(8.5) and
   bounded using the actual autocorrelation estimate (8.7).
4. The `g,k,box` summation spends less than the available power.  For
   `k=H^o(1)`, the nominal R110/additive-large-sieve reserve is
   `H^(-1/4+o(1))`; more generally it is (7.9).
5. Formula (10.1) is derived from (2.2) or (2.3), not assumed by replacing
   the full-Fourier/inverse-image supports in (9.1) by intervals.

To use (10.1), import the reciprocal-normalized energy estimate (7.8) from
the companion R111 after its final audit. Then R100's additive trace large
sieve, with (7.6), gives the quarter-power gain on every separated packet.
Lemmas 4.1--5.1 and
Corollary 4.2 show that smooth outer-prime dependence, B-spline seams,
autocorrelation, and fixed `Q_h` rank do not consume that gain.

The remaining hard step is consequently not “show that a smooth B-spline
has low rank.”  That statement is now proved.  It is one of the following
equivalent native-interface advances:

* a vector/square-function Blomer--Pascadi theorem for the exact supports
  in (9.1), with an outer-prime trace decomposition of projective cost
  `H^o(1)`;
* a new CRT factorization of the composite Vaughan modulus which really
  yields (10.1) without separating the completion; or
* a direct weighted trace-large-sieve theorem for the full-Fourier and
  inverse-image coefficient pair, bypassing short intervals.

Until that native-interface lemma is proved, the correct conclusion is

```text
R110 weighted trace saving                         PROVED;
short-box outer-prime profile separation           PROVED HERE;
actual R81 B-spline outer-prime separation          PROVED HERE / LOW BAND;
Q_h rank cost                                       CONSTANT;
subpower common-g mask cost                         H^o(1), OR AVOIDED;
parabolic special center in native BP box           POWER-SMALL;
reciprocal-coefficient trace energy (7.8)            COMPANION R111 / AUDIT;
full R71-to-short-box trace packet (10.1)            OPEN;
fixed zero-free strip                                NOT YET PROVED. (10.2)
```
