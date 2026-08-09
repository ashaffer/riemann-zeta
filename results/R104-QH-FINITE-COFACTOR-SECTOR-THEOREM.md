# R104 finite-cofactor theorem after continuum annihilation

Status: exact finite nonprimitive cofactor expansion, exact reduced-rational
aggregation, and polylogarithmic `theta=0`, `j=0`, axis, and reducible-face
bounds are proved for fixed-ratio R71 blocks.  The complete all-box
Wright/Blomer--Pascadi range-and-kernel lift remains open.  No fixed
zero-free strip is proved.

Date: 2026-08-07.

R102 predecessor:
[`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md).

## 1. Verdict

Let

```text
c_h=exp(h/2),
Q_h=(tau_h-c_h)^2,
V_Q(x)=V(x+2h)-2c_h V(x+h)+c_h^2V(x).                (1.1)
```

R102 proves

```text
integral_0^infinity t^(-1/2)V_Q(R-log t)dt=0          (1.2)
```

for every `R`.  On a fixed-ratio physical block this has a stronger
arithmetic consequence than the earlier continuum-marginal statement:

```text
the canonical c(q)=-mu(q)log q expansion is finite;
its Poisson zero mode vanishes for every q;
no Mertens/cofactor tail is present;
the original nonprimitive basis has no primitive common-g mask.          (1.3)
```

After duplicate rationals are reduced, their coefficients satisfy

```text
abs(w_d(X))<<log^2(2X)/d.                              (1.4)
```

This is enough to prove directly that the equal-frequency `theta=0` sector
is `O(log^4 X)`, up to the fixed window seminorm.  The dual `j=0` sector is
the atomic diagonal minus its equal-frequency intersection and is
polylogarithmic as well.  Both punctured axes vanish identically.

Thus the transformed full field now has the exact ledger

```text
finite nonprimitive cofactors                    PROVED
conditional Mertens tail                         ABSENT
primitive common-g mask                          AVOIDED
punctured axes                                    ZERO EXACTLY
theta=0 equal-frequency sector                   POLYLOG
j=0 dual/physical-diagonal sector                POLYLOG
theta*j!=0 balanced reciprocal bulk              WRIGHT-COMPATIBLE LOCALLY
m=1 or n=1 reducible off-axis faces              POLYLOG
all ranges, high modes, and projective kernel sum OPEN
fixed-r Blomer--Pascadi lift                      NOT DERIVED
fixed zero-free strip                             NOT PROVED.       (1.5)
```

The remaining problem is smaller than R102 stated.  The nonzero-rational
faces `m=1` and `n=1` are not annihilated, but their **actual
kernel-weighted finite-window sums** can be bounded absolutely by the same
rational-frequency decay.  R87's reciprocal-zeta pole in the bare
coefficient marginal is therefore a warning against an unweighted tail
estimate, not an obstruction to the weighted bound proved below.

## 2. Fixed-ratio block and Fourier normalization

Let `psi>=0` be supported in a fixed-width output block about `R_0`, put
`X=exp(R_0)`, and assume the translated fixed window meets only

```text
aX<=t<=bX                                                (2.1)
```

for fixed `0<a<b<infinity`.  This includes every fixed-order R71 window;
the three translates in (1.1) merely change `a,b` by fixed factors.  Put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
fhat_R(xi)=integral_R f_R(t)e(-xi t)dt,
e(x)=exp(2pi i x),                                     (2.2)

L_Q(t,u)=integral psi(R)f_R(t)conjugate[f_R(u)]dR.     (2.3)
```

The extension of `f_R` to the real line is zero off the positive support.
Equation (1.2) says

```text
fhat_R(0)=0.                                           (2.4)
```

For an integer `B>=1`, define the dimensionless scale seminorm

```text
S_B(f_R;X)
 =max_(0<=j<=B) X^(j-1/2)norm(D^j f_R)_(TV).           (2.5)
```

Here the `TV` norm is the `L^1` norm when the derivative is a function and
the total variation when it is a finite measure.  Repeated integration by
parts gives

```text
abs[fhat_R(xi)]
 <<_B S_B(f_R;X)X^(1/2)(1+abs(xi)X)^(-B).             (2.6)
```

For a fixed R71 B-spline of order greater than `B`, direct differentiation
of (2.2) gives

```text
sup_(R in supp psi) S_B(f_R;X)<<_(V,h,B,a,b)1.         (2.7)
```

Indeed, every derivative has the form

```text
D_t^j f_R(t)
 =t^(-j-1/2)P_j(partial_x)V_Q(R-log t),                (2.8)
```

where `P_j` is a fixed polynomial of degree `j`.  Substitution
`t=exp(R-x)` proves (2.7), including the ordinary spline-knot jumps.  Set

```text
mathcal S_B^2
 =integral psi(R)S_B(f_R;X)^2dR.                       (2.9)
```

It is a fixed constant for the present fixed-window block.  Keeping it in
the displays makes every normalization explicit.

## 3. Exact finite nonprimitive cofactor theorem

Put

```text
c(q)=-mu(q)log q,
D_q[f]=sum_(m>=1)f(qm)-q^(-1)integral f(t)dt.          (3.1)
```

### Theorem 3.1

For every `R` in the block,

```text
D_q[f_R]=sum_(m>=1)f_R(qm),
D_q[f_R]=0                         if q>bX,            (3.2)
```

and the transformed completed field is exactly

```text
D_(V_Q)(R)
 =sum_(q<=bX)c(q)D_q[f_R]
 =sum_(q<=bX)c(q)sum_(m>=1)f_R(qm).                   (3.3)
```

Poisson summation gives, in the ordinary symmetric/Fejer sense and
absolutely once (2.6) is used with `B>1`,

```text
D_q[f_R]=q^(-1)sum_(a in Z-{0})fhat_R(a/q),           (3.4)

D_(V_Q)(R)
 =sum_(q<=bX)c(q)/q
    sum_(a in Z-{0})fhat_R(a/q).                       (3.5)
```

#### Proof

Equation (2.4) removes the integral in (3.1).  If `q>bX`, every positive
multiple of `q` lies outside (2.1), proving (3.2).  Since

```text
sum_(q|n)c(q)=Lambda(n),                               (3.6)
```

and only finitely many `n` meet (2.1), reversing the finite divisor sum
proves (3.3).  Extend `f_R` by zero.  Ordinary Poisson summation gives

```text
sum_(m in Z)f_R(qm)=q^(-1)sum_(a in Z)fhat_R(a/q).
```

The negative and zero physical samples vanish, while the Fourier term
`a=0` vanishes by (2.4).  This proves (3.4)--(3.5).  No use has been made of
the conditional identity `sum_q c(q)/q=1`.  QED.

The theorem also explains a possible bookkeeping trap.  When `q>bX`, the
nonzero aliases on the right of (3.4) sum to zero.  Estimating those aliases
separately would recreate an artificial cofactor tail.

## 4. Exact reduced-rational aggregation

Every nonzero rational in (3.5) has a unique presentation

```text
a/q=A/d,             A!=0,        (A,d)=1.             (4.1)
```

It occurs precisely when `q=kd` and `a=kA`.  Define

```text
w_d(X)=sum_(1<=k<=bX/d)c(kd)/(kd).                     (4.2)
```

Then (3.5) becomes exactly

```text
D_(V_Q)(R)
 =sum_(d<=bX)w_d(X)
    sum_(A!=0,(A,d)=1)fhat_R(A/d).                    (4.3)
```

The coefficient has the unconditional absolute bound

```text
abs[w_d(X)]
 <=d^(-1)sum_(k<=bX/d)log(kd)/k
 <<_b log^2(2X)/d.                                    (4.4)
```

This finite coefficient is not the old finite-Ramanujan Mertens gauge.  In
particular, no estimate for a logarithmically weighted Mobius tail is hidden
in (4.4).

## 5. The equal-frequency sector is polylogarithmic

Use the Fourier convention

```text
Lhat_Q(xi,eta)
 =double_integral L_Q(t,u)e(-xi t-eta u)dtdu.          (5.1)
```

The determinant `theta=0` is precisely equality of the two rational
frequencies.  After the unique reduction (4.1), its contribution is

```text
H_equal
 =sum_(d<=bX)abs[w_d(X)]^2
   sum_(A!=0,(A,d)=1)Lhat_Q(-A/d,A/d)

 =sum_(d<=bX)abs[w_d(X)]^2
   sum_(A!=0,(A,d)=1)
     integral psi(R)abs[fhat_R(-A/d)]^2dR.             (5.2)
```

Every summand is nonnegative because `L_Q` is a Gram kernel.

### Theorem 5.1

For every integer `B>=1`,

```text
0<=H_equal<<_(B,a,b) mathcal S_B^2 log^4(2X).          (5.3)
```

#### Proof

Drop the coprimality restriction.  Equations (2.6) and (4.4) give

```text
H_equal
 <<mathcal S_B^2 log^4(2X)
   sum_(d<=bX) X/d^2
      sum_(A!=0)(1+abs(A)X/d)^(-2B).                  (5.4)
```

For `d<=X`, the inner sum is `<<_B(d/X)^(2B)`.  Hence

```text
sum_(d<=X)X/d^2 (d/X)^(2B)
 =X^(1-2B)sum_(d<=X)d^(2B-2)<<_B1.                    (5.5)
```

For `X<d<=bX`, the inner sum is `O_(B,b)(1)` and
`sum X/d^2=O_b(1)`.  This proves (5.3).  QED.

The proof is scale invariant: the factor `X` from the Fourier mass is
exactly canceled by the `d^-2` coefficient and rational-frequency spacing.

## 6. The `j=0` and punctured-axis sectors

For completeness, define the reduced-rational correlation

```text
S_X(h)=sum_(d<=bX)abs[w_d(X)]^2 c_d(h),                (6.1)
```

where `c_d` is the Ramanujan sum.  Its value at zero obeys

```text
S_X(0)=sum_(d<=bX)phi(d)abs[w_d(X)]^2
 <<log^4(2X)sum_(d<=bX)phi(d)/d^2
 <<log^5(2X).                                         (6.2)
```

Let

```text
F(s)=integral L_Q(u+s,u)du,
D_atomic=sum_n Lambda(n)^2L_Q(n,n).                   (6.3)
```

The exact solution-line Poisson identity used in R81--R83 sends the dual
mode `j=0` to the physical diagonal.  With the `theta=0,j=0` intersection
subtracted once, it reads

```text
H_(j=0)=D_atomic-S_X(0)F(0).                           (6.4)
```

This identity is purely finite here: (4.3) is a finite reduced-rational
basis on the active physical support, so no limiting order is involved.
Moreover,

```text
F(0)=integral psi(R)norm(f_R)_2^2dR
    =norm(V_Q)_2^2 integral psi(R)dR,                  (6.5)

D_atomic
 =sum_n Lambda(n)^2/n
    integral psi(R)abs[V_Q(R-log n)]^2dR
 <<_(V_Q,psi,a,b)log^2(2X).                           (6.6)
```

Equations (6.2)--(6.6) prove

```text
abs[H_(j=0)]<<_(V_Q,psi,a,b)log^5(2X).                (6.7)
```

Finally, (1.2) gives, for every real `xi,eta`,

```text
Lhat_Q(xi,0)=0,               Lhat_Q(0,eta)=0.         (6.8)
```

Thus both punctured-axis corrections, and their intersection, vanish
before any triangle inequality.

Combining (5.3), (6.7), and (6.8), all non-Wright sectors isolated in R81
except the reducible off-axis faces are polylogarithmic on a fixed-window
block.

## 7. The reducible `m=1` and `n=1` faces are also polylogarithmic

It is important to bound these faces in the original nonprimitive basis.
That avoids using the reduced-rational aggregation to modify the generic
off-axis bulk, where it would reintroduce the primitive common-`g` mask.

Put

```text
h_q=c(q)/q,
U_q(R)=sum_(a in Z-{0})abs[fhat_R(a/q)].               (7.1)
```

For `B>1`, equation (2.6) and the convergent sum of `a^(-B)` give, uniformly
for `q<=bX`,

```text
U_q(R)
 <<_B S_B(f_R;X)X^(1/2)(q/X)^B.                       (7.2)
```

In the R81 factorization `q_1=gm`, `q_2=gn`, `(m,n)=1`, the face `m=1`
has

```text
q_1=g,                  q_2=gn.                        (7.3)
```

The case `n=1` in (7.3) is the equal-denominator sector already covered by
Section 5, so take `n>=2` here.  Before any fiber Poisson summation, the
absolute value of the whole raw face is bounded by

```text
abs(H_(m=1))
 <=integral psi(R)
    sum_(n>=2,g:gn<=bX)
      abs(h_g h_(gn))U_g(R)U_(gn)(R)dR.               (7.4)
```

This inequality retains every numerator and every integer alias.  Using
`abs(h_q)<<log(2X)/q` and (7.2), its right side is

```text
<<_B mathcal S_B^2 log^2(2X) X^(1-2B)
  sum_(n>=2)n^(B-1)
    sum_(g<=bX/n)g^(2B-2).                             (7.5)
```

Since `B>1`,

```text
sum_(g<=bX/n)g^(2B-2)<<_(B,b)(X/n)^(2B-1),
sum_(n>=2)n^(-B)<infinity.                             (7.6)
```

Therefore

```text
abs(H_(m=1))+abs(H_(n=1))
 <<_(B,b)mathcal S_B^2 log^2(2X).                      (7.7)
```

The `n=1` estimate follows by interchanging the two kernel coordinates.
This calculation includes the potentially dangerous range `g asymp X`:
the density of rational aliases uses up the two factors of `q^-1`, but only
to the constant scale in (7.7), not to a power of `X`.

There is no conflict with R87 Section 7.  Its Dirichlet series concerns the
bare coefficient marginal obtained after discarding the present
scale-dependent Fourier weights.  It explicitly did not prove that the
kernel-weighted face is large.  Equation (7.7) proves that, for a fixed
window with the normalization (2.5), it is polylogarithmic.

Combining Sections 5--7, every `theta=0`, `j=0`, punctured-axis, and
reducible face is now subpower.  What remains is the genuinely
two-denominator off-axis bulk

```text
theta*j!=0,             m>1,             n>1.          (7.8)
```

## 8. Exact Vaughan recombination and the missing fixed-modulus bridge

The exact gains above remove three earlier objections to an imported
off-axis estimate:

1. fixed nonprimitive cofactor sums no longer have a conditional tail;
2. one need not use the finite primitive basis and its common-`g` mask; and
3. the separate `+P_1+P_2` contact is absent.

There is an exact bridge from the finite cofactor identity to the balanced
Vaughan coordinate.  The coefficient convolution is

```text
c(q)=(mu*Lambda)(q)=-mu(q)log q.                      (8.1)
```

This is the coefficientwise derivative of `mu*1=epsilon`: the convolution
Leibniz rule and `D1=Lambda*1` give `Dmu=-mu*Lambda`, where
`Dmu(n)=mu(n)log n`.

Consequently (3.3) may be unfolded, still as a finite sum, as

```text
D_(V_Q)(R)
 =sum_(d,b,m>=1)mu(d)Lambda(b)f_R(dbm).                (8.2)
```

For cutoffs `U,V`, split the last sum into `d>U,b>V` and its complement.
Associativity, `Lambda*1=log`, and `mu*1=epsilon` show that the complement
is exactly the three standard Vaughan heads

```text
mu_(<=U)*log + Lambda_(<=V)
 -mu_(<=U)*Lambda_(<=V)*1.                            (8.3)
```

Thus the tail is exactly

```text
T_(U,V,Q)(R)
 =sum_(m>=1)sum_(d>U,b>V)
    mu(d)Lambda(b)f_R(mdb).                            (8.4)
```

This answers one structural question: the large cofactor boxes must be
recombined through (8.1)--(8.4), not estimated independently.  R102's
Type-I theorem evaluates (8.3) as a rank-two
`exp(R/2)(alpha+beta R)` center plus the periodic-Euler defect.  `Q_h`
kills that center exactly, while the defect remains in the same power-small
class.  Hence, under the already proved fixed-order support and Euler
hypotheses,

```text
D_(V_Q)(R)=T_(U,V,Q)(R)+e_Q(R),
norm(e_Q)_(block)=power-small.                         (8.5)
```

If `U=V=X^theta` with `theta` just below `1/2`, (8.4) has

```text
d,b in [X^theta,X^(1-theta+o(1))],
m<=bX/(UV)=X^(1-2theta+o(1)).                          (8.6)
```

It is therefore a genuinely balanced two-large-factor problem with a small
retained cofactor.

Independently, R84 Proposition 4.1 applies algebraically to every finite box
with `theta*j!=0`: after putting `k=j theta`, the mask-free box is a scalar
Wright trilinear reciprocal form.  On a balanced nonresonant box, its
nominal imported gain is `X^(-1/40+o(1))`, subject to the stated projective
kernel and range ledger.

There is still one exact analytic gap.  No existing reduction covers, in one
estimate, every unbalanced
`g,m,n`, every high determinant and shift product, and the total Mellin
projective norm of the actual kernel.  The seam-complete R87 response theorem
controls the primitive reciprocal response in its stated band; it is not a
summed all-range Wright estimate.

This is not merely the already removed cofactor tail.  In the direct
cofactor coordinate, boxes with `q_1,q_2 asymp X` have physical rational
spacing `1/X`; their reciprocal character has no automatic Fourier gap at
the window scale, and `abs(j theta)` can reach the full `MN` range.  The
local R84 identification is exact there, but no summed exponent ledger shows
that Wright's saving beats every mode and projective-norm cost.

There is a concrete fail-fast box.  Take `g asymp 1`, `M=N asymp X`, the
dominant bounded physical rational numerators, and the full kernel line
range.  Then

```text
Theta asymp X,          J asymp X,
K_0=abs(j theta)asymp X^2asymp MN,        Z asymp 1.   (8.7)
```

The R84 projective ledger gives, even favorably,

```text
norm(alpha)_2 norm(beta)_2<<X^(-1+o(1)),
integral norm(nu_t)_2dt<<X^(1+o(1)).                   (8.8)
```

Wright's native factor `(K_0MN)^(1/2)` is `X^2`, while the largest term in
its displayed bracket is `X^(-1/8+o(1))` on this box.  The resulting
`X^(15/8+o(1))` bound is worse than the direct absolute `X^(1+o(1))`
scale.  This does not disprove a sharper coefficient-specific estimate, but
it proves that the currently recorded R84 norm ledger cannot simply be
summed over all finite boxes.

The full dyadic audit reaches the same endpoint.  With

```text
K=J Theta,
Z=Theta X/(GMN),                                       (8.9)
```

the audited R84 kernel ledger followed by Wright gives the dyadic bound

```text
H(G,M,N,J,Theta)
 <<X^o K(1+K/(MN))^(1/4)(1+Z)^(1/2-B)W(M,N,K),        (8.10)

W=max{M^(-1/8),
      M^(1/8)N^(-1/4),
      N^(1/10)K^(-1/20)M^(-3/20),
      M^(3/20)K^(-3/20)N^(-1/5),
      M^(3/8)N^(-1/2)},                               (8.11)
```

with the better of this orientation and the one obtained by swapping
`M,N`.  Repeated integration by parts makes `K>MN X^delta` harmless through
`Z>>X^delta`, but it does not touch the boundary `K asymp MN`, `Z asymp 1`.

In the balanced specialization

```text
M=N=X^a,                 K=X^kappa,       kappa<=2a,
```

the exponent supplied by (8.10) is

```text
19kappa/20-a/20,       kappa<=3a/2,
kappa-a/8,             3a/2<=kappa<=2a.               (8.12)
```

At the endpoint `kappa=2a` it is `15a/8`.  It can beat the global `X`
scale only when `a<8/15`; the actual top cofactor box has `a=1`.  Thus no
orientation, large-`Z` cutoff, or already recorded dyadic decomposition
repairs (8.7)--(8.8).

The exact recombination (8.4)--(8.6) avoids those top cofactor boxes.
However, no identity presently derives the complete energy of (8.4), with
its product kernel and coefficients, as a Wright or
Blomer--Pascadi native reciprocal form.  The R81 reciprocal identity was
derived before the internal factorization (8.1).  Treating (8.4) as though
that derivation already existed would skip the main remaining bridge.

Blomer--Pascadi does not bypass these gaps.  Its theorem acts on

```text
sum_(m,n in intervals)alpha_m beta_n S(am,n;r)         (8.13)
```

for one fixed modulus `r`.  The R71/Vaughan field is a product-kernel
bilinear sum, while the R81 completion has a varying denominator, the
coupled `k=j theta` amplitude, and an all-box range ledger.  No identity in the
repository places the complete finite Vaughan tail, with its actual
coefficients and block kernel, into (8.13).  Applying the fixed-`r` theorem
after an unproved completion would assume the missing interface.

The transformed coordinate makes such a fixed-`r` lift logically
sufficient--triangle summation would no longer need to reconstruct a signed
one-axis contact--but it does not supply the lift.

## 9. Discrete zero-sum caution

For a finite sequence `w`, its autocorrelation

```text
z(h)=kappa sum_u w(u)conjugate[w(u-h)]                 (9.1)
```

satisfies

```text
sum_h z(h)=kappa abs(sum_u w(u))^2.                   (9.2)
```

After aggregating aliases modulo `r`,

```text
Z_a=sum_(h congruent a mod r)z(h),

sum_(a mod r)Z_a e_r(-ka)
 =kappa abs(sum_u w(u)e_r(-ku))^2.                    (9.3)
```

Thus an actual packet with `sum w=0` has an exactly missing zero residue
character.  Equation (1.2) alone does not assert this for every finite
packet: Poisson summation gives

```text
sum_n f(n)=sum_(ell!=0)fhat(ell)                       (9.4)
```

when only `fhat(0)=0`.  The nonzero aliases and all physical cross-shells
must be retained.  Even an exact discrete zero sum would remove only one
trace character; it would not by itself improve an `L^2` trace energy by a
fixed power.

## 10. Disposition

The center-annihilated coordinate has now discharged every finite-mode
obstruction which was genuinely a zero or equal-frequency sector.  The
next fail-fast target is narrower:

```text
prove a complete finite-window off-axis estimate for
theta*j!=0 and m,n>1, or derive an exact Vaughan-to-fixed-r reduction
which satisfies all imported theorem ranges and kernel norms.           (10.1)
```

Until one of those statements is proved, the correct conclusion remains:

```text
fixed non-Wright sectors                     SUBPOWER / PROVED
complete transformed off-axis fixed power    OPEN
fixed zeta zero-free strip                    OPEN.    (10.2)
```
