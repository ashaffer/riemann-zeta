# R102 center-annihilated off-axis gate

Status: exact pre-localization center annihilation, exact continuum-marginal
nullity, zero-carrier faithfulness, diagonal and Type-I ledgers, and a
constant-rank R89--R100 packet transfer are proved.  This removes the
separate `P_1/P_2` contact from the transformed detector.  The required
off-axis trace-energy saving is still open, so no new fixed zero-free strip
is proved.

Date: 2026-08-07.

R104 successor: the zero marginal also makes the original nonprimitive
cofactor expansion exactly finite on each fixed-ratio block.  After direct
rational aggregation, `theta=0`, `j=0`, the punctured axes, and the raw
`m=1/n=1` faces are polylogarithmic.  See
[`R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md`](R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md).

## 1. Verdict

There is a clean way to put the full R71 detector into a genuinely
center-free coordinate before the first Cauchy--Schwarz or fourth-trace
step.  Fix `h>0`, put

```text
c=exp(h/2),
(tau_h F)(R)=F(R+h),
Q_h=(tau_h-c)^2.                                      (1.1)
```

If the exact completed field is

```text
D_V(R)=integral V(R-log t)t^(-1/2)
        [sum_n Lambda(n)delta_n(dt)-dt],               (1.2)
```

then

```text
Q_h D_V=D_(V_Q),

V_Q(x)=V(x+2h)-2c V(x+h)+c^2 V(x).                    (1.3)
```

The transformed window has two vanishing continuum moments.  In particular,
for every nonnegative block localizer `psi`, the positive R71 kernel made
from `V_Q` has

```text
G_(1,Q)=0,       G_(2,Q)=0,       C_Q=0.               (1.4)
```

Consequently the exact R87 one-axis quantities satisfy

```text
P_(1,Q)=P_(2,Q)=0.                                    (1.5)
```

This is not merely a cancellation after summing a fourth moment.  It holds
pointwise in the scale variable and therefore occurs before any Cauchy or
trace conversion.

The transformation is faithful:

```text
Q_h exp[(rho-1/2)R]
 =[exp(h(rho-1/2))-exp(h/2)]^2 exp[(rho-1/2)R],        (1.6)
```

and the multiplier is nonzero at every nontrivial zeta zero.  It is also
bounded above and below on the real Fourier axis.  Thus the transformed
field has the same horizontal zero exponent as the original P4/R71 field.
Its elementary atomic diagonal remains subexponential.

The useful change to the R89--R100 ledger is therefore real:

```text
original detector:       H_off - P_1-P_2 + subpower,
Q_h detector:            H_off,Q         + subpower.  (1.7)
```

The old parity objection that an even fourth trace cannot generate a
standalone `+P_1+P_2` no longer applies to the transformed detector.  What
remains is an actual off-axis estimate.  R100 currently reaches only its
natural endpoint.  In particular, the stronger nonparabolic trace-fiber
bound which would yield R100 (5.29) with `delta=1/2` is not proved here.

```text
Q_h before localization                         REQUIRED
rank-two evaluated center                       KILLED EXACTLY
full continuum marginals                        ZERO EXACTLY
nontrivial zero residues                         ALL RETAINED
atomic diagonal                                  SUBEXPONENTIAL
Type-I evaluation error                          SAME SUBPOWER CLASS
B-spline seams                                   RETAINED / CONSTANT COST
outer-prime packet separation                    CONSTANT-RANK TRANSFER
R89/R100 standalone contact requirement          REMOVED
R100 fixed-power trace energy                    OPEN
fixed zeta zero-free strip                       NOT PROVED.            (1.8)
```

## 2. Exact transformed window

Let

```text
dP(t)=t^(-1/2)[sum_n Lambda(n)delta_n(dt)-dt].          (2.1)
```

All integrals below are finite because `V` is compactly supported on the
active logarithmic block.  Translation in `R` acts on the window by

```text
D_V(R+jh)=D_(V(.+jh))(R),                              (2.2)
```

where the right side means the window `x |-> V(x+jh)`.  Expanding (1.1)
therefore proves (1.3) term by term.  No explicit formula, limiting process,
or arithmetic estimate is used.

Define the two continuum moments

```text
J_0(V)=integral_R V(x)exp(-x/2)dx,
J_1(V)=integral_R x V(x)exp(-x/2)dx.                   (2.3)
```

For `j=0,1,2`, direct substitution gives

```text
J_0[V(.+jh)]=exp(jh/2)J_0(V),                          (2.4)

J_1[V(.+jh)]
 =exp(jh/2)[J_1(V)-jh J_0(V)].                        (2.5)
```

Using `c=exp(h/2)` in (1.3), both the `J_1(V)` and `J_0(V)` coefficients
cancel:

```text
J_0(V_Q)=0,                 J_1(V_Q)=0.                (2.6)
```

The first identity kills the exact pole continuum in (1.2).  The pair of
identities is the window-side form of

```text
Q_h exp(R/2)=0,
Q_h[R exp(R/2)]=0,                                    (2.7)
```

so it also kills the evaluated rank-two Vaughan center.

In particular,

```text
integral_0^infinity t^(-1/2)V_Q(R-log t)dt
 =exp(R/2)J_0(V_Q)=0                                  (2.8)
```

for every real `R`.  Hence the transformed completed field has the purely
atomic expression

```text
D_(V_Q)(R)
 =sum_n Lambda(n)n^(-1/2)V_Q(R-log n).                 (2.9)
```

Equation (2.9) does not mean that the prime-minus-continuum information has
been discarded: Section 4 shows that every zero residue is still present.
It means that the continuum is orthogonal to this particular window.

## 3. Both kernel marginals vanish before localization

For an arbitrary nonnegative compact block weight `psi`, put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),                            (3.1)

L_Q(t,u)=integral_R psi(R)f_R(t)conjugate(f_R(u))dR.   (3.2)
```

This is the positive R71 Gram kernel in the convention which absorbs the
exact `t^(-1/2)` weights.  Define

```text
G_(1,Q)(t)=integral_0^infinity L_Q(t,u)du,
G_(2,Q)(u)=integral_0^infinity L_Q(t,u)dt,
C_Q=double_integral L_Q(t,u)dtdu.                      (3.3)
```

Fubini and (2.8) give, pointwise in `t`,

```text
G_(1,Q)(t)
 =integral psi(R)f_R(t)
    conjugate[integral f_R(u)du]dR
 =0.                                                   (3.4)
```

The same calculation in the other coordinate gives `G_(2,Q)=0`, and then
`C_Q=0`.  This proves (1.4).

R87 defines

```text
P_1=<sum Lambda(n)delta_n-dt,G_1>,
P_2=<sum Lambda(n)delta_n-dt,G_2>.                     (3.5)
```

Thus (3.4) proves (1.5) exactly.  Equivalently, in ordinary additive
Fourier coordinates,

```text
Lhat_Q(xi,0)=0,              Lhat_Q(0,eta)=0            (3.6)
```

for every real `xi,eta`.  The punctured axes inserted by completing a
cofactor lattice therefore have zero weight for the full transformed
kernel.

One old normalization must not be reused.  R87's positive-mass response
scale was

```text
M_L=J_0(V)^2 integral psi(R)exp(R)dR.                  (3.7)
```

It is identically zero for `V_Q`.  Ratios such as `J_1/J_0` and the
monotone-positive B-spline response estimate are therefore inapplicable to
the transformed kernel.  Positivity of the Gram kernel survives, but its
size must be normalized by its diagonal or real-frequency `L^2` mass.

The order is important.  The argument allows an arbitrary `psi` because
`Q_h` was applied to the field first and the bracket in (3.4) vanishes for
each `R`.  It does not justify applying `Q_h` after multiplying the field by
a block cutoff; Section 6 records that commutator.

## 4. The transformed detector is faithful to every zeta zero

On an exponential mode `exp(sR)`, (1.1) has multiplier

```text
q_h(s)=[exp(hs)-exp(h/2)]^2.                           (4.1)
```

At a nontrivial zero `rho`, the completed explicit formula has exponent
`s=rho-1/2`.  If its transformed coefficient vanished, then

```text
exp[h(rho-1)]=1,                                      (4.2)
```

which forces `Re(rho)=1`.  The classical zero-free line excludes this.
Thus

```text
q_h(rho-1/2)!=0                                       (4.3)
```

for every nontrivial zero, including multiple zeros.

There is also a norm-level check.  For real `t`,

```text
[exp(h/2)-1]^2
 <=abs(q_h(it))
 <=[exp(h/2)+1]^2.                                    (4.4)
```

Consequently `Q_h` is boundedly invertible in whole-line `L^2`, with

```text
Q_h^(-1)
 =exp(-h)sum_(j>=0)(j+1)exp(-jh/2)tau_h^j.             (4.5)
```

The series converges in operator norm.  It transfers any uniform all-block
power saving for `Q_hD_V` back to `D_V`; alternatively (4.3) lets the usual
one-sided pole argument be repeated directly.  Subject to the same
fixed-window or regular-block hypotheses used by the R71 energy theorem,
the transformed detector therefore has the same exponent `Delta`.

This is why annihilating the continuum center does not itself prove a
saving.  It is an elliptic coordinate change on the real-frequency field,
not a contracting filter.

## 5. The elementary diagonal remains subexponential

After (2.9), the atomic diagonal on one block is

```text
D_(Q,I)
 =sum_n Lambda(n)^2/n
    integral psi(R)abs[V_Q(R-log n)]^2dR.              (5.1)
```

Translations are isometries in `L^2`, so

```text
norm(V_Q)_2
 <=(1+2c+c^2)norm(V)_2
 =(1+c)^2norm(V)_2.                                   (5.2)
```

The factor is fixed once `h` is fixed.  On any R71 active product range,
the elementary inequalities

```text
Lambda(n)<=log n,
sum_(A<n<=B)1/n<=log(B/A)+O(1/A)                      (5.3)
```

show that (5.1) is `exp(o(R))` after the existing window normalization.
This remains true on the proportional bank: the logarithmic support length
is at most `O(R)`, while every window and seam loss in (5.2) is fixed or
subexponential.

Thus the transformed off-diagonal problem is still exponent-equivalent to
the transformed positive energy.  No large new diagonal was created by
center annihilation.

## 6. Type-I, localization, and seam ledger

On a frozen regular block the exact-head comparison has the form

```text
D_I^full=G_I+e_I,
G_I=B_I-z_I,                                           (6.1)
```

where

```text
z_I(R)=exp(R/2)(alpha_I+beta_I R)                      (6.2)
```

up to the already recorded window normalization.  Equations (2.7) give

```text
Q_h z_I=0,
Q_h D_I^full=Q_h B_I+Q_h e_I.                         (6.3)
```

Moreover,

```text
norm(Q_h e_I)
 <=(1+2c+c^2)max_(j=0,1,2)norm[tau_(jh)e_I].           (6.4)
```

Therefore the imported periodic-Euler estimate leaves `Q_he_I` in exactly
the same negligible or `exp(o(R))` class as `e_I`.  The bounded primitive
constant mentioned in R76 is not killed by `Q_h`, but remains bounded and
cannot affect any positive exponential saving.

The exact unevaluated Type-I head is not separately annihilated.  Formula
(6.3), not deletion of that head, is the legitimate transfer: retain its
evaluated rank-two part and the proved Euler defect.

Localization must follow the difference.  For a cutoff `chi`, direct
expansion gives

```text
Q_h(chi G)-chi Q_hG
 =[chi(R+2h)-chi(R)]G(R+2h)
  -2c[chi(R+h)-chi(R)]G(R+h).                         (6.5)
```

The right side lives on boundary collars at the unknown raw scale.  Use an
enlarged frozen block with a `2h` safety margin, form `Q_hG` there, and only
then localize.  Estimating (6.5) absolutely would restore the original
problem.

Finally, `V_Q` is a three-translate linear combination of the original
compact B-spline.  It introduces no new distributional seam: it has at most
three translated copies of each old knot, with seminorms multiplied by a
fixed function of `h`.  All R87 seam and variation estimates therefore
remain in their previous subexponential class.

## 7. Constant-rank transfer to the R89--R100 packets

Write

```text
b_0=c^2,             b_1=-2c,             b_2=1,
V_Q=sum_(j=0)^2 b_j V(.+jh).                              (7.1)
```

The kernel is the exact nine-packet sum

```text
L_Q=sum_(j,k=0)^2 b_j conjugate(b_k)L_(j,k),           (7.2)

L_(j,k)(t,u)
 =1/sqrt(tu) integral psi(R)
    V(R+jh-log t)conjugate[V(R+kh-log u)]dR.           (7.3)
```

Every coefficient `b_j` depends only on the fixed `h`; no outer prime,
cofactor, determinant, or shift variable has entered it.

The R89 fourth-trace packet `z` is an autocorrelation of the underlying
localized weight.  Replacing that weight by the three-packet sum (7.1)
replaces `z` by at most nine separated cross-correlations.  A product of
four such packets expands into at most `9^4` terms.  This is a fixed number,
not a power of the arithmetic scale.

More invariantly, if an outer-prime family before the transformation has a
separation

```text
w_r=sum_(ell<=L)omega_ell(r)v_ell,                    (7.4)
```

then `Q_hw_r` has separation rank at most `3L`, and its autocorrelation has
rank at most `9L^2`.  Thus `Q_h` preserves every already proved low-rank or
Mellin separation in the outer prime up to a fixed factor.  It does not
prove that the actual R71 `r`-dependent weights possess the separation
still requested by R100.

The expansion (7.2) is a separation identity, not permission to estimate
its nine terms independently before centering.  The three translates in
(7.1) generally have nonzero continuum moments; only their signed sum has
moment zero.  Form the full `V_Q` marginal cancellation first.  The fixed
packet expansion may then be used on the remaining nonzero modes.

There is one recombination rule.  A dyadic partition of `f_R(t)` has pieces
whose individual continuum integrals need not vanish:

```text
integral chi_s(t)f_R(t)dt need not equal 0,
sum_s integral chi_s(t)f_R(t)dt=0.                    (7.5)
```

Hence shell axes must be summed to zero before the first absolute value or
Cauchy step.  Equivalently, derive the full identities (3.4)--(3.6), remove
the zero axes there, and only then decompose the remaining nonzero packets.
Applying Cauchy separately to the partial shell axes discards (7.5) and
recreates a boundary contact ledger.

More exactly, if `sum_s chi_s(t)=1` and

```text
f_(R,s)(t)=chi_s(t)f_R(t),       m_s(R)=integral f_(R,s)(t)dt,
```

then generally `m_s!=0` although `sum_s m_s=0`.  The marginal-null kernel
is the **full double sum**

```text
sum_(s,t) integral psi(R)
  f_(R,s) tensor conjugate(f_(R,t))dR.                (7.5a)
```

Keeping only shell diagonals, or triangle-bounding the `(s,t)` blocks,
loses the cross-shell cancellation.  In contrast, a partition of the
output localizer `psi=sum_j psi_j` is safe: each kernel formed with one
`psi_j` is separately marginal-null by (3.4).  This is the exact
localization test which a future R100 lift must pass.

With this ordering, the R89/R100 parity theorem becomes compatible rather
than obstructive: the transformed detector asks only for its off-axis
fourth trace.  Paired-axis and central/parabolic pieces must still be kept
in the exact trace formula, but no standalone linear `+P_1+P_2` coefficient
is required.

In particular, continuum mean zero does **not** say that every fourth-trace
zero-shift coefficient vanishes.  For an autocorrelation packet,

```text
z(0)=constant * sum_u abs(w(u))^2>0                   (7.6)
```

unless the packet itself is zero.  The paired-axis square locus and the
special `g=plusminus I` parabolic correction can therefore remain.  What
has vanished is the linear one-axis R87 contact, not these even-moment
diagonals.

## 8. Relation to literal Hoeffding projection

The alternative proposal was to center an arbitrary positive finite-shell
kernel directly.  On a fixed-ratio shell `Omega_X=[aX,bX]`, use the
unweighted-kernel convention

```text
m_X(t)=1_(Omega_X)t^(-1/2),
M=<m_X,m_X>=log(b/a),
P_m f=m_X<m_X,f>/M,
K_c=(I-P_m)K(I-P_m).                                  (8.1)
```

If `h=Km_X` and `C=<m_X,Km_X>`, then exactly

```text
K_c
 =K-[h tensor m_X+m_X tensor h*]/M
   +(C/M^2)m_X tensor m_X.                            (8.2)
```

For the shell discrepancy `dP_X`, put

```text
A_X=<m_X,dP_X>
 =sum_(aX<n<=bX)Lambda(n)/n-log(b/a),

P_X=<dP_X,Km_X>.                                      (8.3)
```

Then

```text
(I-P_m)dP_X=dP_X-(A_X/M)m_Xdt,                        (8.4)

E_(K_c)(dP_X)
 =E_K(dP_X)-2 Re[conjugate(A_X)P_X]/M
   +(C/M^2)abs(A_X)^2.                                (8.5)
```

Thus literal Hoeffding projection is also a faithful new detector, but it
replaces the known continuum coefficient by the data-dependent harmonic
prime mass `A_X/M`.  It does not make the carrier disappear from the exact
finite-shell energy.

Indeed a zero `rho` contributes the projected shell density

```text
-t^(-1/2){t^(rho-1)-X^(rho-1)c_rho}dt,

c_rho
 =[b^(rho-1)-a^(rho-1)]
   /[(rho-1)log(b/a)].                                 (8.6)
```

For `rho!=1` the bracket is not identically zero.  Under the R71 feature
map its response is `X^(rho-1/2)` times a nonzero scale-free profile.
Hence this projection also kills only the pole mode and preserves every
nontrivial zero exponent.

The finite-shell Fourier correction in (8.2) occurs at every rational
off-axis mode, not only on the literal axes.  At frequency `xi=theta/X`,
the shell transform of `m_X` has its full natural size.  Therefore the
rank-two terms in (8.2) relocate the contact into near-axis nonzero packets.
The pre-localization `Q_h` construction is preferable here: it gives the
same desired marginal nullity using an R71-native three-translate window
and preserves the packet class transparently.

There is a normalization warning.  Passing from `K` to
`L=K/sqrt(tu)` is a congruence, not a unitary conjugation on ordinary
`L^2(dt)`.  Projecting onto `t^(-1/2)` in the `K` convention is therefore
not literally the same operation as projecting onto the constant function
in the `L` convention.  Both versions are faithful, but their finite-shell
contact scalars are different.  Any future use must declare its Hilbert
metric.

## 9. The remaining R100 trace-energy theorem

R100 groups the four-step trace by

```text
T
 =a^2 h_1h_2h_3h_4-a(h_1+h_3)(h_2+h_4)+2.            (9.1)
```

For separated packets put

```text
A_T=sum_(h:trace_a(h)=T)product_(i=1)^4 z_i(h_i).      (9.2)
```

The proved uniform nonparabolic fiber bound is

```text
# {h:trace_a(h)=T} <<H^(2+o(1)),       T!=plusminus2,  (9.3)
```

which gives only the natural endpoint

```text
sum_T abs(A_T)^2
 <<H^(2+o(1))product_i norm(z_i)_2^2.                 (9.4)
```

Center annihilation does not improve (9.3).  It removes the separate
one-axis theorem which R100 previously needed in addition to an off-axis
bound.

There is a precise conditional upgrade.  If one proved the stronger
uniform arithmetic theorem

```text
# {h:trace_a(h)=T} <<H^(1+o(1)),       T!=plusminus2,  (9.5)
```

then fiberwise Cauchy and disjointness of the fibers would give

```text
sum_(T!=plusminus2)abs(A_T)^2
 <<H^(1+o(1))product_i norm(z_i)_2^2.                 (9.6)
```

This is exactly R100 (5.29) with `delta=1/2`.  It would yield a relative
`H^(-1/2+o(1))` trace saving before the remaining outer-rank and completion
ledgers.

At the R100 scale `R=H^2`, the trace large sieve would then have mean-square
size `H^(5+o(1)) product_i norm(z_i)_2^2`; the final outer Cauchy factor
gives `H^(7/2+o(1)) product_i norm(z_i)_2`, versus the natural `H^4`
scale.  This is the same relative `H^(-1/2)=R^(-1/4)` gain.

Equation (9.5) is consistent with small finite counts but is not established
by the divisor factorization used in R100, which gives (9.3).  This report
does not promote that numerical pattern to a theorem.

Even after a proof of (9.5), a strip deduction would still require:

1. the exact central/parabolic `T=plusminus2` terms for the transformed
   packets;
2. a low-rank separation, or a direct theorem, for the actual
   outer-prime-dependent B-spline weights;
3. all common-`g` primitive masks and reducible faces;
4. the signed shell recombination (7.5), every seam, and the original
   rectangular limiting order; and
5. the already controlled Type-I defect (6.4).

Only the last item is currently discharged in full.  The first four are
arithmetical/off-axis interfaces, not a restored continuum contact.

## 10. Disposition

The new center-free coordinate is valid and worth retaining:

```text
full completed R71 field
  -- apply Q_h on a 2h-safe block --> exact V_Q field
  -- continuum integration --------> G_1=G_2=C=0
  -- R87 recompletion --------------> off-axis + subpower
  -- R89/R100 trace conversion -----> weighted trace-energy gate. (10.1)
```

This genuinely removes one previously separate obstruction.  It does not
give a bound for the surviving off-axis form.  The next fail-fast theorem is
therefore no longer a signed reconstruction of `+P_1+P_2`; it is the
center-free, coefficient-specific version of R100 (5.29), with the
parabolic, outer-prime, common-factor, seam, and rectangular ledgers kept
jointly.

In particular, proving (9.5) together with those interfaces would be a new
route to a fixed-power R71 estimate.  At present the correct status is:

```text
separate canonical contact                 REMOVED BY EXACT COORDINATE
complete center-free off-axis fixed power  OPEN
fixed zero-free strip                      OPEN.        (10.2)
```
