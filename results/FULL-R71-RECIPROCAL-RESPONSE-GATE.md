# Full R71 reciprocal-response and sector-conservation gate

Status: R87 exact CRT/fiber-Poisson response theorem, primitive-mask
zero-character classification, slow-axis identification, all-sector
conservation law, and Type-I completion audit.  The proposed *free*
all-sector cancellation mechanism is closed.  No fixed zero-free strip is
proved, and this report does not prove that such a strip fails to exist.

## 1. Verdict

R86 left one apparent loophole: although the square-root reciprocal block
does not cancel its canonical contact, perhaps the common-factor sectors,
the `theta=0` and `j=0` modes, the punctured axes, and the exact Type-I head
cancel it after the complete R71 pairing is restored.

There is an exact answer.

1. The CRT change of variables followed by Poisson summation along each
   solution line is invertible.  The common-`g` primitive mask translates
   the dual amplitude by fractions of `1/g`, but it does not change the
   reciprocal character in `j`.
2. On a reduced primitive sector, the reciprocal character has zero
   frequency only on the degenerate face `m=1` (or `n=1` after swapping the
   two sides).  The balanced sector `m,n>1` has no zero orbit.  In a
   nonreduced parametrization, every apparent extra zero orbit reduces to
   that same face.
3. The slow Fourier response of the canonical `-gamma` packet is exactly
   the centered punctured-axis sample `-P_1`; the reversed orientation gives
   `-P_2`.  The nonzero integer aliases are explicit and remain in the
   complete identity.
4. The complete sector sum is exactly

   ```text
   <sum_n Lambda(n)delta_n-dt,
       L(sum_n Lambda(n)delta_n-dt)>.                  (1.1)
   ```

   The off-axis and non-Wright sectors cancel one artificial
   singular-series background.  They do **not** cancel the completed
   prime-minus-continuum measure.
5. Restoring the exact Type-I head also reconstructs the same completed
   measure.  Replacing that head by the evaluated R71 center changes the
   field only by the already power-small Euler defect.

Thus sector recombination is a conservation law, not a new estimate:

```text
cofactor Poisson modes
  -- CRT and fiber Poisson (invertible) --> all R81 sectors
  -- exact recompletion ----------------> original dP energy.           (1.2)
```

This closes the alleged last *algebraic* all-sector cancellation route.  A
fixed-power upper bound for (1.1) would still prove a fixed zero-free strip,
but it would be a new estimate for the original R71/P4 energy itself.  The
identities below neither prove that estimate nor prove that no fixed strip
exists.

## 2. Fourier convention and the completed form

Put

```text
e(x)=exp(2 pi i x),
Lhat(xi,eta)=double_integral_R2
  L(t,u)e(-xi t-eta u)dtdu.                            (2.1)
```

It is enough initially to take `L` in `C_c^infinity((0,infinity)^2)` and
extend it smoothly by zero.  The same identities hold for Schwartz `L` and,
by the usual smoothing limit, for the R71 compact kernel.  These hypotheses
make every Poisson step below classical.  Cofactor sums are first kept
finite; an infinite cofactor expansion is taken only in its original
rectangular order.

Let

```text
nu=sum_(n>=1)Lambda(n)delta_n-dt.                      (2.2)
```

For the R71 kernel `L=K_(V,psi)/sqrt(tu)`, the completed local energy is

```text
E_L(nu)=double_integral L(t,u)dnu(t)conjugate(dnu(u)). (2.3)
```

With `c(q)=-mu(q)log q` and `h_q=c(q)/q`, the canonical cofactorwise Poisson
completion gives

```text
E_L(nu)
 =lim_(Q->infinity) sum_(q_1,q_2<=Q)h_(q_1)h_(q_2)
    sum_(a,b in Z; ab!=0)Lhat(-a/q_1,b/q_2).           (2.4)
```

The coefficients are real here.  For complex coefficients the second one
is conjugated.  Formula (2.4) includes the continuum center cofactor by
cofactor; the missing `a=0` and `b=0` modes must not subsequently be dropped.

All exact finite statements below may instead use R82's finite primitive
Ramanujan gauge.  That version avoids any conditional cofactor limit and
agrees with `Lambda` on the active integer support.

## 3. CRT fibers and exact reciprocal response

Write

```text
q_1=gm,       q_2=gn,       (m,n)=1,
theta=an-bm.                                             (3.1)
```

Choose `a_0` with

```text
a_0 n=theta (mod m),       b_0=(a_0 n-theta)/m.        (3.2)
```

Every integer solution of (3.1) is then uniquely

```text
a=a_0+m ell,             b=b_0+n ell,       ell in Z. (3.3)
```

Put `x_0=a_0/m` and

```text
H_(g,m,n,theta)(s)
 =Lhat(-s/g,[s-theta/(mn)]/g).                         (3.4)
```

Its one-dimensional Fourier transform, with the convention in (2.1), is

```text
Hcheck(y)=integral_R H(s)e(-ys)ds
 =g integral_R L(u+gy,u)e(theta u/(gmn))du
 =:A_(g,m,n,theta)(y).                                 (3.5)
```

Indeed, after inserting (2.1), integration in `s` gives
`delta((t-u)/g-y)=g delta(t-u-gy)`.  Poisson summation therefore gives the
exact fiber identity

```text
sum_(ell in Z)H(ell+x_0)
 =sum_(j in Z)e(jx_0)A(j)
 =sum_(j in Z)e(j theta inverse(n)/m)A(j).             (3.6)
```

This proves both the reciprocal phase and every factor of `g` in the R81
formula.  The maps

```text
(a,b) <-> (theta,ell),          ell-Fourier <-> j      (3.7)
```

are a bijective reindexing followed by Fourier inversion.  No estimate and
no loss of information has occurred.

Additive reciprocity gives

```text
e(j theta inverse(n)/m)
 =e(j theta/(mn))e(-j theta inverse(m)/n).             (3.8)
```

The first factor is the slow additive beat.  The second is precisely the
reciprocal rotation used in R84--R86.

## 4. Primitive common-factor masks do not create a zero orbit

In the finite reduced-rational basis, primitivity adds the periodic mask

```text
M_g(ell)
 =1_((a_0+m ell,g)=1)1_((b_0+n ell,g)=1).             (4.1)
```

Write its finite Fourier expansion as

```text
M_g(ell)=sum_(nu mod g)Mhat_g(nu)e(nu ell/g),
Mhat_g(nu)=g^(-1)sum_(r mod g)M_g(r)e(-nu r/g).        (4.2)
```

Applying Poisson summation term by term gives

```text
sum_ell M_g(ell)H(ell+x_0)
 =sum_(nu mod g)sum_(j in Z)
    Mhat_g(nu)e(-nu x_0/g)e(jx_0)A(j-nu/g).            (4.3)
```

Thus the mask changes the amplitude from the integral on the physical line
`t-u=gj` to those on `t-u=gj-nu`.  Its multiplier
`Mhat_g(nu)e(-nu x_0/g)` is independent of `j`.  In particular, it cannot
alter the `j`-character

```text
chi_(m,theta)(j)=e(j theta inverse(n)/m).              (4.4)
```

For primitive reduced frequencies, `(theta,mn)=1`.  Hence (4.4) has exact
order `m`, and

```text
chi_(m,theta)=1 identically       <=>       m=1.       (4.5)
```

After reversing the two coordinates the corresponding face is `n=1`.
Before rational reduction, (4.4) is trivial exactly when `m|theta`; then
`a_0=0 (mod m)`, so the first rational frequency is reducible.  Repeating
rational reduction moves the mode to `m=1`.  Consequently all apparent
cross-`g` zero characters are boundary copies of the same degenerate face.
Neither the common factor nor its fractional dual shifts repair the absent
zero orbit in a balanced `m,n>1` block.

There is a useful cohomological description.  The determinant map

```text
(a,b) |-> an-bm                                      (4.6)
```

has kernel `Z(m,n)`.  Choosing `(a_0,b_0)` is a choice of section; changing
the section changes `x_0` by an integer and leaves (4.4) unchanged.  The
primitive mask is a periodic coefficient on the kernel.  Its Fourier
expansion translates the dual kernel coordinate but cannot change the
section character.  The missing augmentation therefore lives on the
boundary `m=1`/`n=1`, not in a hidden choice of CRT gauge.

## 5. The slow response is the punctured axis

Define

```text
G_1(t)=integral_R L(t,u)du,
G_2(u)=integral_R L(t,u)dt.                            (5.1)
```

Then

```text
Ghat_1(xi)=Lhat(xi,0),       Ghat_2(eta)=Lhat(0,eta). (5.2)
```

The line completion (3.3) adds points with `a=0` or `b=0`.  Exact
inclusion--exclusion removes them by

```text
-1_(m|theta)Lhat(0,-theta/(gmn))
-1_(n|theta)Lhat(-theta/(gmn),0)
+1_(theta=0)Lhat(0,0).                                (5.3)
```

For example, if `b=0` then `theta=an`, so `n|theta` and
`-a/(gm)=-theta/(gmn)`.  The other sign follows similarly.  This proves
(5.3) directly, including both divisibility conditions and the restored
origin.

The exact Fourier response of the slow factor in (3.8) identifies its zero
alias with (5.3).  Namely, from (3.5) and

```text
g sum_(j in Z)delta(t-u-gj)
 =sum_(k in Z)e(k(t-u)/g),                             (5.4)
```

one obtains

```text
sum_(j in Z)e(j theta/(mn))A_(g,m,n,theta)(j)
 =sum_(k in Z)
    Lhat(-theta/(gmn)-k/g,k/g).                       (5.5)
```

The `k=0` response is exactly

```text
Lhat(-theta/(gmn),0)=Ghat_1(-theta/(gmn)),             (5.6)
```

with the opposite sign in the `b=0` puncture (5.3).  The reversed response
has zero alias `Lhat(0,-theta/(gmn))` and matches the `a=0` puncture.  The
terms `k!=0` in (5.5) are explicit two-dimensional lattice aliases; they
are retained in the all-sector identity and are not being identified with
the puncture.

This is the exact response-level meaning of R86's `-gamma` zero orbit.  To
match it to the centered one-point field, let a primitive beat frame of
modulus `M` synthesize

```text
v_n=Lambda(n)-1=sum_theta gamma_theta e(theta n/M)     (5.7)
```

on the active integer interval.  Ordinary Poisson summation gives

```text
P_1
 :=<sum_n Lambda(n)delta_n-dt,G_1>

 =sum_theta gamma_theta sum_(k in Z)
      Ghat_1(k-theta/M)
   +sum_(k!=0)Ghat_1(k).                               (5.8)
```

The last sum is the ordinary integer-comb Euler error.  Thus the canonical
slow packet is

```text
sum_theta gamma_theta Lhat(-theta/M,0),                (5.9)
```

and (5.3) contributes its negative.  Formula (5.8), rather than (5.9)
alone, is the exact `P_1`: all integer aliases remain displayed.  On a
smooth R71 shell the nonzero aliases are smaller than every fixed power by
repeated integration by parts, but no such estimate is needed for the
algebraic identification.  The second coordinate gives `P_2` in the same
way.

The raw punctured-axis sum is conventionally written `-A_1-A_2+C`.  The
`theta=0` origin and the ordinary-lattice baseline recenter it.  After that
bookkeeping its carrier is exactly `-P_1-P_2`, which is why the canonical
`-gamma` term in R86 and the R81 puncture are the same obstruction in two
coordinate systems.

## 6. Exact all-sector conservation

The preceding identification can be made without any asymptotic remainder.
Use the finite primitive R82 gauge on the active support and put

```text
lambda_N(n)=sum_(q<=N)htilde_q c_q(n)=Lambda(n),
S_N(h)=sum_(q<=N)|htilde_q|^2 c_q(h),
f(h)=integral_R L(u+h,u)du.                            (6.1)
```

Also define

```text
D_0=sum_n |lambda_N(n)|^2L(n,n),
T_off=sum_(t!=u)lambda_N(t)conjugate(lambda_N(u))L(t,u),

A_1=sum_n lambda_N(n)G_1(n),
A_2=sum_n conjugate(lambda_N(n))G_2(n),
C=double_integral L(t,u)dtdu.                          (6.2)
```

The determinant-zero, dual-zero, and punctured-axis sectors are exactly

```text
H_(theta=0)=sum_h S_N(h)f(h),
H_(j=0)=D_0-S_N(0)f(0),
H_axes=-A_1-A_2+C.                                    (6.3)
```

Therefore their sum is

```text
H_nonW
 =D_0-A_1-A_2+C+sum_(h!=0)S_N(h)f(h).                 (6.4)
```

On the other hand, expanding the original completed measure gives

```text
E_L(nu)=D_0+T_off-A_1-A_2+C.                          (6.5)
```

Since (3.7) is invertible, the remaining off-axis sector is not an
independent expression.  Subtracting (6.4) from (6.5) forces the exact
identity

```text
H_off
 =T_off-sum_(h!=0)S_N(h)f(h).                         (6.6)
```

Adding (6.4) and (6.6) proves the conservation law

```text
H_off+H_(theta=0)+H_(j=0)+H_axes
 =D_0+T_off-A_1-A_2+C
 =E_L(nu).                                             (6.7)
```

Thus the only automatic cross-sector cancellation is

```text
-sum_(h!=0)S_N(h)f(h)
 +sum_(h!=0)S_N(h)f(h)=0.                             (6.8)
```

This is the singular-series background introduced by the sector split.  It
is not `nu`, `P_1`, `P_2`, or the R71 energy.  Any additional cancellation
in (6.7) is exactly the arithmetic cancellation of the original completed
prime-minus-continuum form.

For comparison, write `S_N=1+R_N`,

```text
Q_L=sum_h f(h)-C,       P_i=A_i-C.                     (6.9)
```

Then the elementary diagonal, smooth lattice, and Ramanujan-fluctuation
terms in R83 reduce (6.4) to

```text
H_nonW=-P_1-P_2+Y^o(1)                               (6.10)
```

on normalized R71 shells.  Formula (6.6) says that the off-axis block must
contain the opposite full carrier if the complete energy is small.  Proving
that joint cancellation is the fixed-strip theorem; recompletion does not
supply it.

## 7. The degenerate zero-character face retains zeta poles

There is also a coefficient-level reality check on the only primitive zero
orbit.  For the original cofactor coefficient

```text
h_q=-mu(q)log(q)/q,                                    (7.1)
```

the `m=1`, `q_1=g`, `q_2=gn` face carries the absolutely convergent
coefficient

```text
b_n=sum_(g>=1)h_g h_(gn)

 =mu(n)/n sum_((g,n)=1)
    mu(g)^2 log(g)[log(g)+log(n)]/g^2.                 (7.2)
```

Both sides vanish when `n` is not squarefree.  Introduce

```text
F(x,y)=sum_((g,n)=1)mu(g)^2mu(n)g^(-x)n^(-y)
      =product_p(1+p^(-x)-p^(-y)).                    (7.3)
```

Initially for `Re(x),Re(y)>1`, differentiation term by term gives

```text
B(s):=sum_n b_n n^(-s)
 =[(partial_x^2+partial_x partial_y)F(x,y)]
      at x=2, y=s+1.                                  (7.4)
```

Factor

```text
F(x,y)=G(x,y)/zeta(y),
G(x,y)=product_p[1+p^(-x)/(1-p^(-y))].                (7.5)
```

Near `x=2`, `G` and the derivatives used below are holomorphic for
`Re(y)>0`.  Hence

```text
B(s)
 =[G_xx+G_xy]/zeta(y)-G_x zeta'(y)/zeta(y)^2,
 y=s+1.                                                (7.6)
```

Moreover `G_x(2,y)` never vanishes for `Re(y)>0`.  Indeed,

```text
G_x(2,y)/G(2,y)
 =-sum_p log(p)p^(-2)/[1-p^(-y)+p^(-2)],              (7.7)
```

and every summand before the minus sign has positive real part: if
`a=1+p^(-2)` and `z=p^(-y)`, then `|z|<1<a` and

```text
Re[1/(a-z)]=(a-Re z)/|a-z|^2>0.                       (7.8)
```

Thus a zero `rho` of `zeta` of multiplicity `r` produces an unavoidable
pole of order `r+1` in `B(s)` at `s=rho-1`.  In particular, a fixed-power
tail estimate

```text
B(0)-sum_(n<=N)b_n=O(N^(-eta))                         (7.9)
```

would continue (7.4) holomorphically to `Re(s)>-eta` and would exclude every
zeta zero with `Re(rho)>1-eta`.  The sole reciprocal zero-character face is
therefore not an elementary boundary error; even its scalar coefficient
marginal retains fixed-strip-strength zeta poles.

This does not show that the specifically weighted full R71 face cannot
cancel with the other sectors.  Equation (6.7) says precisely that such a
cancellation would be a new estimate for the completed field.

## 8. Type-I completion cannot be a separate repair

Let `D_I^full` be the normalized full von Mangoldt coboundary, `G_I` the
frozen Vaughan tail with the evaluated R71 rank-two center, and `e_I` the
signed Type-I evaluation defect.  The exact cutoff identity is

```text
D_I^full=G_I+e_I.                                     (8.1)
```

For every nonnegative block weight `psi`, the reverse triangle inequality
gives

```text
|norm(sqrt(psi)D_I^full)_2-norm(sqrt(psi)G_I)_2|
 <=norm(sqrt(psi)e_I)_2.                              (8.2)
```

At the R71 retreat

```text
U=V=exp[(1/2-c/k)R],       c>1/4,       k^2=o(R),     (8.3)
```

periodic Euler summation gives, up to polynomial normalization,

```text
norm(e_I)_infinity
 <=exp[-(2c-1/2)R+O_h(k^2+k log k)].                  (8.4)
```

Thus the exact head reconstructs `D_I^full`; the evaluated head changes it
only by a power-small field.  A Type-I cross term cannot supply a hidden
natural-scale cancellation which is absent from (6.7).  If the completed
energy has a fixed-power bound, then (8.2)--(8.4) transfer it between the two
coordinates; if it does not, changing coordinates does not create one.

## 9. Algebraic disposition

The proposed final shortcut now has a complete fail-fast verdict:

```text
balanced reciprocal zero orbit              absent;
common-g primitive-mask repair               absent;
theta=0, j=0, and punctured-axis sum          exact;
canonical slow sample                         centered punctured axis;
automatic off/non-Wright cancellation         singular-series background;
sum of every sector                           original dP energy;
exact versus evaluated Type-I head             power-small coordinate change;
new fixed-power estimate                       OPEN;
fixed zero-free strip                          NOT PROVED;
nonexistence of a fixed strip                  NOT PROVED.               (9.1)
```

The next valid theorem cannot be another rearrangement, gauge, or completion
of the same modes.  It must estimate (6.7) itself--equivalently the complete
R71/P4 energy--using new arithmetic information.  Conversely, failure of
this mechanism is not evidence that a fixed zero-free strip is false.

### Ledger-ready row

```text
R87 | P4 | full reciprocal response, primitive-mask zero-orbit
classification, slow-axis match, and all-sector conservation THEOREM;
free all-sector/Type-I cancellation CLOSED; completed fixed power OPEN |
CRT plus fiber Poisson is invertible.  The common-g mask only translates
dual amplitudes; the canonical -gamma slow response is the centered
punctured axis.  Off-axis and non-Wright sectors cancel only their inserted
singular-series background, and their complete sum is exactly the original
prime-minus-continuum R71 energy.  The m=1/n=1 zero-character face retains
explicit 1/zeta zero poles.  No strip or no-strip theorem follows. |
Any continuation must prove a genuinely new bound for the complete dP/R71
quadratic form; no further sector recompletion can lower the target.
```

## 10. Quantitative response of the actual B-spline kernel

The preceding conservation law is algebraic.  There is nevertheless a
useful quantitative fact about the particular R71 kernel: away from the
reducible faces, its reciprocal `j`-character sees a fixed-power Fourier
gap.  The B-spline knots do not fill that gap.

Write

```text
beta=theta/(gmn),
A_theta(j)=g integral L(u+gj,u)e(beta u)du,
R_theta(alpha)=sum_(j in Z)A_theta(j)e(j alpha).       (10.1)
```

The kernel is extended by zero outside the positive quadrant.  It is compact,
so the sum in (10.1) is finite.  With the convention (2.1), the line-comb
identity gives

```text
R_theta(alpha)
 =sum_(k in Z)
   Lhat(-(k+alpha)/g,[k+alpha-theta/(mn)]/g).          (10.2)
```

For a merely piecewise-smooth compact kernel, (10.2) is read as the symmetric
or Fejer Poisson limit.  It is classical pointwise after an arbitrarily small
smoothing, and its line-comb form before expanding the comb is an exact
distribution identity.  In particular, no absolute rearrangement of the
cofactor sum is being asserted.

Indeed,

```text
g sum_j delta(t-u-gj)=sum_k e(k(t-u)/g),               (10.3)
```

and on the line `t-u=gj` the phase in (10.1) is

```text
e(beta u+alpha(t-u)/g).
```

Inserting (10.3) proves (10.2).  Thus the slow phase

```text
alpha_0=theta/(mn)
```

has the exact response

```text
R_theta(alpha_0)
 =Lhat(-beta,0)
  +sum_(k!=0)Lhat(-(k+alpha_0)/g,k/g).                 (10.4)
```

The first term is the punctured axis identified in Section 5.  By contrast,
put

```text
alpha_R=theta inverse(n)/m  (mod 1).
```

Additive reciprocity says

```text
alpha_R-alpha_0=-theta inverse(m)/n  (mod 1).          (10.5)
```

Consequently, on a primitive sector `(theta,mn)=1`, every alias in (10.2)
satisfies

```text
abs(k+alpha_R)>=1/m,
abs(k+alpha_R-alpha_0)>=1/n.                           (10.6)
```

The reciprocal response is genuinely separated from both coordinate axes.
If primitivity is omitted, (10.6) fails precisely at the reducible resonances
already classified in Section 4.

### Theorem 10.1 (seam-complete variation bound)

Suppose `L` is compact and belongs to `W^(1,1)` in its first coordinate.
Then

```text
sum_j abs[A_theta(j+1)-A_theta(j)]
 <=g norm(partial_1 L)_1,                              (10.7)

abs R_theta(alpha)
 <=g norm(partial_1 L)_1/[2 abs(sin(pi alpha))]        (10.8)
```

for `alpha` not an integer.  Hence, on the primitive reciprocal character,

```text
abs R_theta(alpha_R)<<g m norm(partial_1 L)_1.         (10.9)
```

For (10.7), apply the fundamental theorem for `W^(1,1)` functions to
`L(u+g(j+1),u)-L(u+gj,u)`.  For each fixed `u`, the intervals
`[u+gj,u+g(j+1)]` partition the real line.  Summing therefore gives exactly
the right side of (10.7).  Discrete summation by parts gives (10.8), and
`abs(sin(pi alpha_R))>=sin(pi/m)` gives (10.9).  Notice that the additive
factor `e(beta u)` never gets differentiated.  The estimate is therefore
uniform in `theta`.

Now specialize to the actual R71 kernel.  Put

```text
f_R(t)=t^(-1/2)V_(h,k)(R-log t),
L(t,u)=integral psi(R)f_R(t)f_R(u)dR,                  (10.10)

ell=kh,
M_L=double_integral L(t,u)dtdu,
Y_psi=[integral psi(R)e^R dR]/[integral psi(R)dR].     (10.11)
```

Here `psi>=0`; harmless zero denominators are excluded.  If

```text
J_0=integral V(x)e^(-x/2)dx,
J_1=integral abs[V'(x)+V(x)/2]e^(x/2)dx,              (10.12)
```

then direct substitution `t=e^(R-x)` gives

```text
M_L=J_0^2 integral psi(R)e^R dR,
norm(partial_1 L)_1
 <=J_0 J_1 integral psi(R)dR.                         (10.13)
```

Every B-spline seam is already present in `J_1`.  There is no omitted
boundary distribution: the compact coboundary is continuous and absolutely
continuous on its support, while its derivative has only ordinary jumps at
the knots.

For `V=W_(h,k)/N_(h,k)`, evenness and monotonicity on `[0,ell]` give the
uniform sharp-enough estimate

```text
J_1/J_0<=1+2/ell.                                     (10.14)
```

To see this, `W(0)=1`, `W(ell)=0`, and `-W'>=0` almost
everywhere on `(0,ell)`.  Therefore

```text
integral abs(V')e^(x/2)dx
 =2 integral_0^ell [-V'(x)]cosh(x/2)dx
 <=2/N_(h,k)+J_0/2.                                  (10.15)
```

Adding `J_0/2` for the zeroth-order term in (10.12) gives
`J_1<=J_0+2/N_(h,k)`.  Finally, evenness and
`integral W=ell` imply

```text
N_(h,k)J_0=integral W(x)cosh(x/2)dx>=ell,             (10.16)
```

which proves (10.14).  This argument includes terminal order one and all
piecewise-polynomial knots; its constant does not grow with the number of
seams.

Combining (10.9), (10.13), and (10.14) yields the unconditional response
bound

```text
abs R_theta(alpha_R)/M_L
 <<[g m/Y_psi](1+2/ell).                              (10.17)
```

Thus at `g=Y^o(1)`, `m,n=Y^(1/2+o(1))`, and
`Y_psi=Y^(1+o(1))`, the reciprocal response is

```text
abs R_theta(alpha_R)/M_L<=Y^(-1/2+o(1)).              (10.18)
```

This is an unconditional kernel statement, not a Wright estimate and not an
estimate for the completed cofactor sum.

There is a matching axis approximation.  On the slow line the two phases in
(10.1) combine to `e(beta t)`.  The elementary rectangle-rule inequality

```text
abs{g sum_j F(u+gj)-integral F(t)dt}
 <=g integral abs(F'(t))dt                            (10.19)
```

gives

```text
abs[R_theta(alpha_0)-Lhat(-beta,0)]
 <=g{norm(partial_1 L)_1+2 pi abs(beta)M_L}.           (10.20)
```

At `theta=0`, this says that the slow zero response is
`M_L[1+O(g(1+2/ell)/Y_psi)]`.  For nonzero `theta`, (10.20)
reduces comparison with the reciprocal response to one explicit question:
the size of the true one-axis transform `Lhat(-beta,0)`.

### Proposition 10.2 (fixed-scaled proportional-order comparison)

The needed lower bound is rigorous in the fixed-scaled range already covered
by the whole-window Gamma theorem.  Let `R_0` tend to infinity, take

```text
k=lambda R_0+O(1),       0<lambda<1/h,
Y=exp(R_0),
```

and let `psi` be supported in a fixed translate of a compact `R-R_0`
interval.  Assume

```text
g=Y^o(1),        m,n=Y^(1/2+o(1)),
beta e^R
```

ranges in a fixed compact subinterval of one component of
`R-{0}` on the support of `psi`.  This is the fixed nonzero scaled-`theta`
regime.  Then

```text
abs Lhat(-beta,0)/M_L
  asymp B_(h,k)^(-1)=Y^(-a_h lambda+o(1)),             (10.21)

B_(h,k)
 =integral W_(h,k)(x)e^(-x/2)dx
 =4 sinh(kh/4)[sinh(h/4)/(h/4)]^k,

a_h=h/4+log[sinh(h/4)/(h/4)]<h/2.                    (10.22)
```

Indeed, if

```text
T_(h,k)(1/2,xi)
 =integral W_(h,k)(x)e^(-x/2)e(-xi e^(-x))dx,
```

then the factorization of (10.10) gives the exact ratio

```text
Lhat(-beta,0)/M_L
 =B_(h,k)^(-1)
   [integral psi(R)e^R
      T_(h,k)(1/2,-beta e^R)dR]
   /[integral psi(R)e^R dR].                          (10.23)
```

Uniformly on a fixed compact annulus, R81's whole-window theorem gives

```text
T_(h,k)(1/2,xi)
 ->Gamma(1/2)(2 pi abs(xi))^(-1/2)
   e[-sign(xi)/8].                                    (10.24)
```

All limiting values on one sign component have the same phase, so the
nonnegative `psi` average in (10.23) cannot cancel.  Formula (10.22) follows
from the exact B-spline Laplace multiplier.  Finally,
`sinh(x)/x<e^x` for `x>0`, which proves `a_h<h/2`.

The error in (10.20) is smaller than (10.21).  Consequently (10.18) and
(10.21) give

```text
abs R_theta(alpha_R)/abs R_theta(alpha_0)
 <=Y^(-[1/2-a_h lambda]+o(1)),                        (10.25)
```

and the exponent is positive throughout `0<lambda<1/h`.  In this precise
range the reciprocal gap cannot mix the canonical slow axis at fixed-power
size.  The actual B-spline seams strengthen neither side and create no
exception.

The fixed-annulus qualification can be relaxed, but only through an explicit
range tied to the B-spline order.

### Proposition 10.3 (uniform growing-frequency Gamma band)

Put

```text
b_h=(1-exp(-h/2))/(h/2),       c_h=-log(b_h)>0.        (10.26)
```

For every real `xi` with `abs(xi)>=1`, one has the uniform, seam-complete
estimate

```text
abs{T_(h,k)(1/2,xi)
 -Gamma(1/2)(2 pi abs(xi))^(-1/2)e[-sign(xi)/8]}
 <=C b_h^k,                                            (10.27)
```

where `C` is absolute.  More generally, for `abs(xi)>=xi_0>0` the right side
is `C_(xi_0)b_h^k`.

To prove this, let `S_k` be the sum of `k` independent uniforms on `[0,h]`.
The exact B-spline identity is

```text
W_(h,k)(x)=Prob(S_k>=abs(x)).                          (10.28)
```

After `y=exp(-x)`, write

```text
J_xi(A)=integral_(exp(-A))^(exp(A))
          y^(-1/2)e(-xi y)dy.
```

Fubini on the compact support gives

```text
T_(h,k)(1/2,xi)=E[J_xi(S_k)].                          (10.29)
```

The omitted lower tail is at most `2exp(-A/2)`.  One integration by parts
on the upper oscillatory tail gives

```text
abs integral_(exp(A))^infinity y^(-1/2)e(-xi y)dy
 <=[pi abs(xi)]^(-1)exp(-A/2).                        (10.30)
```

Thus `abs(J_xi(A)-G(xi))<=C exp(-A/2)` for
`abs(xi)>=1`, where `G` is the Gamma integral in (10.27).  Finally,

```text
E exp(-S_k/2)
 =[E exp(-U/2)]^k=b_h^k,                              (10.31)
```

which proves (10.27).  This proof integrates across all spline seams at
once; no derivative or knot count enters.

If `k=lambda log Y+O(1)`, (10.27) is a relative Gamma asymptotic uniformly
for

```text
1<=abs(xi)<=Y^tau,             tau<2c_h lambda.        (10.32)
```

Indeed, the smallest Gamma main term in this band has size
`Y^(-tau/2+o(1))`, whereas the error is
`Y^(-c_h lambda+o(1))`.  Therefore, on a central R71 shell where
`abs(beta)e^R` is comparable to `abs(theta)` and
`1<=abs(theta)<=Y^tau`, the slow-axis size is uniformly

```text
abs Lhat(-beta,0)/M_L
 >>Y^(-a_h lambda-tau/2+o(1)).                        (10.33)
```

The phase in (10.27) is still constant on each sign component, so a
nonnegative `psi` average cannot cancel.  Combining (10.17) and (10.33)
proves a fixed-power separation provided

```text
tau<min{2c_h lambda, 1-2a_h lambda}.                  (10.34)
```

The first inequality in (10.34) is the rigorous Gamma-window range; the
second is the response-separation range.  Both constants are explicit.

Since

```text
a_h+c_h=h/2,                  lambda h<1,
```

the Gamma-window condition `tau<2c_h lambda` is in fact the smaller of the
two bounds in (10.34).  It also implies

```text
3 tau/2+a_h lambda<1,
```

so the rectangle-rule error `g abs(beta)M_L` in (10.20) is smaller than the
axis lower bound (10.33).  Thus (10.34) compares the reciprocal response to
the full slow response, not merely to an axis term whose alias error was
left uncontrolled.

Neither (10.17), fixed-scaled (10.25), nor growing-band (10.34) proves a
bound for (6.7): one must still sum all cofactors and determinants with their
signed arithmetic coefficients and retain the degenerate faces.  What they
prove is narrower and decisive for the proposed mechanism.  Slow bulk
variation and the B-spline seams cannot up-convert the canonical axis into
the balanced reciprocal character at natural size throughout the band
(10.34).  Any surviving cancellation must come from the completed arithmetic
sum in (6.7), from reducible/axis sectors, or from determinants outside the
proved Gamma band--not from an unrecorded seam loss.

## 11. Final quantitative gate

The quantitative kernel audit strengthens, but does not alter, the algebraic
verdict:

```text
primitive reciprocal response / kernel mass       Y^(-1/2+o(1));
slow response in the proved growing band           explicitly nonzero;
reciprocal / slow response                          fixed-power small;
B-spline seam loss                                  uniformly bounded;
all-sector arithmetic recombination                 original dP energy;
completed fixed-power estimate                      OPEN;
fixed strip or no-strip conclusion                  NOT PROVED.       (11.1)
```

In particular, the R84--R86 conditional seam/variation ledger is now proved
for the actual R71 B-spline in the band (10.34).  The failure is no longer a
missing kernel regularity lemma.  It is the signed high-determinant,
reducible-face, and cross-cofactor arithmetic cancellation in (6.7).
