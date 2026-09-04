# QP LTRAD B3: sparse-separator theorem and two-cluster closure

**Date:** 2026-08-30

**Subsequent correction.**  Sections 5.4 and 6 are superseded by
`ZETA23-UNIFORM-STRIP-DECISION-TREE-CONSOLIDATION-AND-MAXIMUM-INFORMATION-GAIN-2026-08-30.md`.
The `.000655647...` short-carrier gap was an artifact of using the global
fourth-moment range loss on a localized carrier; the corrected localized
range already clears `8/33`, and calibrated phase selection gives the
stronger threshold `(1+c)/3`.  The proposed localization-or-progression
dichotomy also requires a third, dispersed growing-rank branch.  The
effective-participation theorem and finite fixtures in this report remain
valid.

## Verdict

The corrected, separator-qualified B3 problem has not been solved, and this
report proves neither `LTRAD_full`, a uniform zero-free strip, nor RH.  It does
remove the entire fixed-cluster branch from the decision tree.

Let `E=sum_b r_b^2` be the clustered frame energy of a dual cosine
polynomial, let `S_1=sum_b r_b`, and define its effective block participation
by

```text
P_eff=S_1^2/E.                                       (0.1)
```

For every source-normalized dual `y dot v=-1`, the existing smooth
cluster-frame estimates imply the new bound

```text
h_Y(y)>=c_w/P_eff.                                   (0.2)
```

Consequently, a separator at the adapter target

```text
h_Y(y)<=epsilon_Y,       epsilon_Y=Y^(-.0179+o(1)), (0.3)
```

must satisfy

```text
P_eff >>Y^(.0179-o(1)),
number of active frame blocks >>Y^(.0179-o(1)).      (0.4)
```

This is stronger than merely excluding one or two reflected pairs: every
bounded number of active blocks, and every family with at most
`Y^(.0179-delta)` active blocks for fixed `delta>0`, is impossible.
The proof needs the smooth high-band mean estimate.  An `L2/L-infinity`
argument without mean absorption would not establish the one-sided support
bound.

For comparison, a direct hard-window calculation gives the explicit uniform
constant

```text
h_Y(y)>9e-4                                           (0.5)
```

for a dual supported on two `B^-1`-close reflected pairs whose scaled centers
are sufficiently separated.  A hostile numerical search over more than one
thousand same-cloud-calibrated two-pair configurations found no target-scale
candidate.  An exact synthetic two-pair fixture has transverse depth
rigorously bracketed by

```text
.5000000625000065 < s_v < .5000002500001042.         (0.6)
```

The rigorous surviving requirement is polynomial effective participation.
A growing, delocalized autocorrelation profile is the sharp candidate class,
not a proved classification of every counterexample.  Frame inequalities
alone cannot exclude that class.  Besides the usual Fejer kernel, an exact
rank-two generalized-progression construction below attains the `1/P_eff`
scale.  This falsifies the overly narrow idea that every near-extremizer must
be a literal one-dimensional triangular Fejer profile.

The numerical constants and exponent ledger are replayed by

```bash
python3 results/verify_zeta23_qp_ltrad_b3_sparse_separator.py
```

## 1. Setup

Use the actual absolute-log nodes and the project aperture

```text
u_n=|log(n/Y)|,
F_y(t)=sum_n y_n cos(tu_n),
B=Y^(50/33),
H_Y=[Y^.01,B],
h_Y(y)=sup_(t in H_Y)F_y(t).                         (1.1)
```

The low source height satisfies `0<=t_0<=Y`.  For `0<=D<=1`, put

```text
v=a(t_0)+Dq_0,
y dot v=F_y(t_0)+D F_y(0)=-1.                       (1.2)
```

Partition the signed frequencies into the singleton/two-point blocks of the
smooth cluster-frame lemma in
`ZETA23-QP-TRANSVERSE-RETURN-CLUSTER-FRAME-GATE-2026-08-15.md`.
For a singleton, `r_b` is the coefficient magnitude.  For a two-point block
with coefficients `c_1,c_2`, scaled gap `z=B|xi_1-xi_2|`, and coordinates

```text
p=c_1+c_2,
q=min(1,z)(c_1-c_2),
r_b=(|p|^2+|q|^2)^(1/2).                             (1.3)
```

Let `L` be the number of nonzero blocks and set

```text
E=sum_b r_b^2,       S_1=sum_b r_b,
P_eff=S_1^2/E.                                       (1.4)
```

Source normalization forces `E>0`.  Cauchy--Schwarz gives

```text
1<=P_eff<=L<=M_Y.                                   (1.5)
```

## 2. Effective-participation theorem

### Theorem 2.1

For all sufficiently large `Y`, every real dual satisfying `(1.2)` obeys

```text
h_Y(y)>=c_w/P_eff,                                  (2.1)
```

where `c_w>0` is independent of `y,Y,t_0,D`.  Hence `(0.3)` implies
`P_eff,L>>epsilon_Y^-1`.

### Proof

Let `rho_B` be the smooth probability supported in the middle of the high
band supplied by the cluster-frame lemma.  That lemma gives

```text
Q:=int F_y(t)^2 rho_B(t)dt >=c_w E,                 (2.2)
|int F_y(t)rho_B(t)dt|
 <=C_(w,R)sqrt(M_Y)(Y/B)^R sqrt(E).                 (2.3)
```

There is also the coefficient-sensitive pointwise estimate

```text
U:=sup_(0<=t<=B)|F_y(t)|<=C_w S_1.                  (2.4)
```

For a singleton this is immediate.  In a pair with `z<=1`, the difference
mode contains

```text
sin((xi_1-xi_2)t/2)=O(z t/B),                       (2.5)
```

which cancels the `z` in `(1.3)`; for `z>=1`, `(1.3)` retains the full
difference coefficient.  Summing the block bounds proves `(2.4)`.

Since `F_y^2<=U|F_y|`, equations `(2.2)` and `(2.4)` imply

```text
int |F_y|rho_B >=c_w E/S_1.                         (2.6)
```

The sign of the mean matters.  Put `mu=int F_y rho_B`.  Relative to the
right side of `(2.6)`, equation `(2.3)` has size at most

```text
|mu|/(E/S_1)
 <=C_(w,R)sqrt(M_Y P_eff)(Y/B)^R
 <=C_(w,R)M_Y(Y/B)^R.                               (2.7)
```

Here `P_eff<=M_Y` and `M_Y=O_w(Y)`.  Taking the fixed smoothing order `R=2`
at `B=Y^(50/33)` gives

```text
M_Y(Y/B)^2
 <<Y^(1+2(1-50/33))=Y^(-1/33)=o(1).                (2.8)
```

Thus the mean is absorbed in `(2.6)`, and

```text
int (F_y)_+ rho_B
 =.5[int |F_y|rho_B+mu]
 >=c_w E/S_1.                                       (2.9)
```

Because `rho_B` is a probability supported in `H_Y`, its left side is at
most `h_Y(y)`.  Finally, the same blockwise bound at `t=t_0` and `t=0` gives

```text
1=|F_y(t_0)+D F_y(0)|<=C_w S_1.                    (2.10)
```

Using `E/S_1=S_1/P_eff` in `(2.9)` proves `(2.1)`.  QED

### Corollary 2.2

If at most `K` frame blocks are active, then

```text
h_Y(y)>=c_w/K.                                      (2.11)
```

In particular, no fixed-`K` family can challenge a target tending to zero.
This closes the one-cluster and two-cluster branches independently of the
corrector-energy allowance.

## 3. Direct two-reflected-pair constant

The following calculation is redundant for asymptotic closure after
Theorem 2.1, but it independently tests the delicate reflected-pair
coordinates and supplies an explicit constant.

Scale `t=Bs`.  For two Fourier-close pairs write

```text
omega_(j,+/-)=Omega_j+/-z_j/2,       0<=z_j<=1,
F(s)=sum_(j=1)^2 [
 p_j cos(z_js/2)cos(Omega_js)
 +q_j sin(z_js/2)/z_j sin(Omega_js)],               (3.1)
```

with the continuous value `s/2` when `z_j=0`.  Let
`x=(p_1,q_1,p_2,q_2)` and normalize averages on `J=[1/2,1]` by
`Avg_J g=2 int_(1/2)^1 g(s)ds`.

Assume

```text
Omega_min>=1000,
|Omega_1-Omega_2|>=144pi.                            (3.2)
```

For `C^1` weights, integration by parts gives

```text
|Avg_J[w(s)e^(i lambda s)]|
 <=2[|w(1/2)|+|w(1)|+int_J|w'|]/|lambda|.           (3.3)
```

On `J`, if `a_j=cos(z_js/2)` and
`b_j=sin(z_js/2)/z_j`, then

```text
cos(1/2)<=a_j<=1,       sin(1/4)<=b_j<=1/2,
|a_j'|<=1/4,            0<=b_j'<=1/2.               (3.4)
```

Expanding the two diagonal squares and applying `(3.3)` at frequency
`2Omega_j` gives

```text
Avg_J f_j^2
 >=[.5 sin^2(1/4)-2.04/Omega_j]||x_j||_2^2.         (3.5)
```

For the cross term, product-to-sum and `(3.3)` at frequencies
`Omega_1+/-Omega_2` give

```text
|2 Avg_J f_1f_2|
 <=(1/Delta+1/Sigma)
   (|x_1|^T [[4.5,2.125],[2.125,1.125]] |x_2|),    (3.6)
```

where `Delta=|Omega_1-Omega_2|` and `Sigma=Omega_1+Omega_2`.
The matrix has operator norm below its Frobenius norm
`sqrt(30.546875)<5.53`.  Therefore `(3.2)` yields

```text
Avg_J F^2
 >=[.5 sin^2(1/4)-2.04/1000
    -2.765(1/(144pi)+1/2000)]||x||_2^2
 >.02||x||_2^2.                                     (3.7)
```

The elementary pointwise and mean bounds are

```text
sup_J|F|<=sqrt(2.5)||x||_2,
|Avg_J F|<=sqrt(48.5)Omega_min^-1||x||_2.           (3.8)
```

Indeed, the pointwise coefficient majorant is `(1,1/2,1,1/2)`;
one further use of `(3.3)` bounds each pair's mean coefficients by
`(4.5,2)/Omega_j`.

Since `F^2<=sup|F| |F|`, equations `(3.7)--(3.8)` imply

```text
sup_J F
 >=.5[.02/sqrt(2.5)-sqrt(48.5)/1000]||x||_2
 =.002842458251... ||x||_2.                         (3.9)
```

At a scaled source `tau=t_0/B<=1`, the coefficients of the source functional
`F(tau)+D F(0)` have Euclidean norm at most

```text
sqrt[2(2^2+(1/2)^2)]=sqrt(8.5).                     (3.10)
```

Thus source normalization gives `||x||_2>=1/sqrt(8.5)`, and

```text
h_Y(y)>=sup_JF>.0009749551367...>9e-4.              (3.11)
```

No restriction on the source phases or corrector energy was used.  Actual
distinct frame blocks eventually satisfy `(3.2)`, and `J` lies in the scaled
high band.  Equation `(3.11)` directly excludes the two-Fourier-close-pair
case.

## 4. Hostile numerical search and an exact control

The corresponding inner convex program was searched over more than one
thousand outer configurations at `tau=.002`.  The tests varied

```text
center gap:        144pi through 12000,
pair gaps z_j:     .01 through 1,
calibrated event:  one-node, one-pair, and larger subsets,
D:                 at least .5.                     (4.1)
```

The smallest finite-grid objectives were about `.5000`; guarded candidates
were `.505--.507`.  The best configurations had `D>.988`.  Their scaled
corrector norms were below `.52`, while the mapped B3 budget was about
`15.01`, so the energy constraint was inactive.  In the sampled
configurations, removing that constraint did not reveal a smaller value.
These are diagnostics, not an exhaustive outer certificate, and the outer
search is not replayed by the certificate script.

There is also an exact synthetic control.  Take

```text
tau=1/500,       z_1=z_2=1,
Omega_1=5pi/tau,       Omega_2=6pi/tau,             (4.2)
```

and calibrate on both nodes of the first pair.  Then

```text
D=cos(tau/2),
v_(1,+/-)=0,
v_(2,+/-)=2cos(tau/2).                              (4.3)
```

Put `a=tau/4`, `s_1=tau/2`, `s_2=3tau/2`, and

```text
w_1=sin(3a)/(sin(a)+sin(3a)),
w_2=sin(a)/(sin(a)+sin(3a)).                        (4.4)
```

At the finite scale mapped from `tau=.002`, both points lie in the scaled
high band.  Both weights are positive and sum to one.  The first-pair
coordinates of
`w_1a(s_1)+w_2a(s_2)` cancel, while both second-pair coordinates equal

```text
-C,       C=w_1cos(a)+w_2cos(3a).                   (4.5)
```

Hence this positive two-atom measure equals `-rv`, where

```text
r=C/[2cos(2a)]
 =.5000000625000065104... .                         (4.6)
```

Every dual with `y dot v=-1` therefore has `sup F_y>=r`.  Conversely, the
dual

```text
y_(1,+/-)=0,
y_(2,+/-)=-1/[4cos(tau/2)]                          (4.7)
```

has zero difference energy, is source-normalized, and satisfies

```text
sup F_y<=1/[2cos(tau/2)]
 =.5000002500001041667... .                         (4.8)
```

This proves `(0.6)`.  It is a synthetic fixture, not an actual-prime
contiguous source event, and its fixed finite `tau` is preasymptotic for the
project target.  It is also not the universal sharp two-pair constant.

Indeed, if `D=1` is supplied by disjoint source-event nodes, take the
`z_j->0` limit with

```text
Omega_1=2pi/tau,       Omega_2=4pi/tau,
p_1=-1/3,              p_2=-1/6,
q_1=q_2=0.                                         (4.9)
```

The disjoint source nodes are synthetic, and `tau` is taken small enough for
the center-separation hypotheses in `(3.2)`.

After a `1+O(tau^2)` normalization, `y dot v=-1`, while, on writing
`x=cos(2pi s/tau)`,

```text
F(s)=1/6-x/3-x^2/3,
sup F=1/4.                                         (4.10)
```

For `z_1=z_2=z` with `0<z<=1`, the extra common factor
`cos(zs/2)` does not increase this positive maximum, apart from the same
source-normalization error.  Thus a
universal `1/2` lower bound is false; the rigorous `9e-4` bound is deliberately
nonsharp.  This distinction does not affect fixed-cluster closure.

## 5. What the surviving obstruction must look like

The abstract Fejer model in the cluster-frame report has

```text
S_1 asymp1,       E asymp1/K,       P_eff asympK,
h_Y(y) asymp1/K.                                     (5.1)
```

It shows that `(2.1)` is sharp for support/spacing/frame information.  Thus a
separator at `(0.3)` must use at least `Y^(.0179-o(1))` effective blocks;
autocorrelation near-extremizers remain a sharp possible mechanism.  Another
fixed-dimensional minimax search has essentially zero information value.

Existing actual-prime rigidity narrows this further but does not close it.

* The short-carrier theorem excludes a complete, ordinary-prime,
  carrier-one antenna lying in one physical interval of diameter
  `Y^(.2417685-epsilon_0)` at the project exponents.  Its hypotheses do not
  automatically apply to an arbitrary transverse dual or to correction
  tails.
* The literal one-sided harmonic Fejer transfer of length
  `L=Y^(.0179+o(1))` must have physical diameter at least
  `Y^(.5179-o(1))`.  This still fits inside a fixed shell.
* Weighted log-AP rigidity closes only a worst-case Lipschitz transfer beyond
  `L>>Y^(2-50/33)=Y^(16/33)`; since `.0179<16/33`, it does not touch the
  minimum participation required here.

### 5.1 Rank-two autocorrelation falsifier

There is a broader exact sharpness family.  Let `n>=2`, `m=n^2`, choose an
integer `Q>2(n-1)`, and put

```text
A={i+Qj:0<=i,j<n}.                                   (5.3)
```

The condition on `Q` makes every signed difference
`r+Qs`, `|r|,|s|<n`, unique.  With a frequency spacing `h>0`, define

```text
K_A(t)=m^-1 |sum_(a in A)e^(iaht)|^2 >=0,
F_A(t)=[1-K_A(t)]/[2(m-1)].                          (5.4)
```

If `nu(d)` counts ordered representations `a-b=d`, then

```text
K_A(t)=1+(2/m)sum_(d>0)nu(d)cos(dht),
y_d=-nu(d)/[m(m-1)].                                 (5.5)
```

Thus

```text
F_A(0)=-1/2,
sup_(t in R)F_A(t)=1/[2(m-1)].                       (5.6)
```

The equality follows by taking `ht=2pi/n`, where the first geometric sum in
`(5.4)` vanishes.

At the common source height `t_0=2pi/h`, all hard phases are `+1`.  Taking
`D=1` gives

```text
y dot[a(t_0)+q_0]=F_A(t_0)+F_A(0)=-1.               (5.7)
```

There are exactly

```text
L=2n(n-1)                                           (5.8)
```

positive difference frequencies.  Their coefficient `l1` mass is `S_1=1/2`.
Writing

```text
T_n=sum_(r=-(n-1))^(n-1)(n-|r|)^2=(2n^3+n)/3,      (5.9)
```

their singleton energy and participation are

```text
E=[T_n^2-m^2]/[2m^2(m-1)^2],
P_eff=m^2(m-1)^2/[2(T_n^2-m^2)]
     =(9/8+o(1))m.                                  (5.10)
```

Consequently

```text
(sup F_A)P_eff =9/16+o(1).                          (5.11)
```

This saturates Theorem 2.1 up to constants while using a rank-two difference
pattern rather than consecutive triangular Fejer weights.

The example can also be delocalized.  Take `h=2pi/Y` and `Q` of order
`Y/n`, with the constant chosen so all `dh` remain in the fixed shell.  If
`m=o(Y)`, then `Q>>n`, `t_0=Y`, the number of active nodes remains `asymp m`,
and the carrier spans a fixed log-frequency diameter.  A disjoint half-mesh
supplies as many exact `-1` source nodes as the abstract model requires.  This
is not an actual-prime construction; it proves that source calibration,
frame geometry, participation, and delocalization still do not suffice
without arithmetic information about the mask.

The structural invariant exposed by `(5.3)--(5.11)` is not a literal AP.  It
is a high-multiplicity difference set, equivalently large weighted additive
energy.  On actual logarithmic nodes, its approximate additive quadruples
become approximate multiplicative relations among the underlying prime
powers.  That is the point at which an inverse theorem could feed into the
project's four-cycle/product-rigidity machinery.

### 5.2 Exact resonance is absent on the ordinary-prime mask

There is an elementary but useful complementary fact.  Assume the narrow
shell used in the actual-Fejer rigidity theorem,

```text
Y=N+1/2=A/2,       A=2N+1,
0<w<(log 2)/2.                                        (5.12)
```

Then the numbers

```text
u_p=|log(p/Y)|                                       (5.13)
```

for distinct ordinary shell primes are linearly independent over the
rationals.

To see this, write `u_p=sigma_p(log p-log Y)`, with `sigma_p` equal to the
side of the center.  An integer relation gives

```text
product_p p^(k_p sigma_p)=(A/2)^K,
K=sum_p k_p sigma_p.                                (5.14)
```

No shell prime divides `2A`: if `p|A`, then the odd integer `A/p` can be
neither `1` (which puts `p=A=2Y` above the shell) nor at least `3` (which puts
`p<=A/3=2Y/3` below it).  Comparing the `p`-adic valuations in `(5.14)`
therefore gives every `k_p=0`.

Kronecker's theorem now yields, for every real coefficient vector on these
ordinary primes,

```text
sup_(t in R) sum_p y_p cos(tu_p)=sum_p |y_p|.        (5.15)
```

Indeed, the one-parameter phase orbit is dense in the full torus, so it can
approach phase `0` on positive coefficients and phase `pi` on negative ones.

Thus the rank-two model cannot be copied *exactly* onto the ordinary-prime
mask.  Any actual separator is necessarily a finite-aperture phenomenon: its
coefficient signs cannot align accurately during `H_Y`, even though such
alignments occur at arbitrarily large times.  A generic quantitative
Kronecker theorem is exponentially bad in the number of active frequencies
and is useless when that number is `Y^.0179`.  The missing result must exploit
weights, source alignment, and prime-product spacing to turn failure of a
return before `B` into a low-complexity approximate relation.  Exact product
spacing is only `asymp Y^-2`, finer than `B^-1=Y^(-50/33)`; at the aperture
resolution there remains an integer-defect slack of size
`Y^2/B=Y^(16/33)`.  Rational independence alone therefore cannot control the
needed approximate relations.

### 5.3 Applying the existing PHR2 Hankel serialization theorem

The actual mask gives a stronger pointwise obstruction than rational
independence.  The following statement is exactly the project theorem PHR2
from `ZETA23-PRIME-SHADOW-HANKEL-RIGIDITY-2026-08-29.md`, rewritten in the
present log coordinates.  Its application to rows of the rank-two model is
the new information here; the theorem itself is not new in this report.

**Theorem 5.1.**  Let `A_ap>3/2`, `B=Y^A_ap`, and let
`p_0,...,p_(L-1)` be distinct ordinary primes in the fixed shell, all on the
same side of `Y`.  Suppose that, for real `u_0,h` and fixed `C`,

```text
|u_(p_j)-(u_0+jh)|<=C/B                 (0<=j<L).   (5.16)
```

Then `L=O_(w,C,A_ap)(log Y)`.  At `A_ap=50/33`, the determinant margin in
the proof is `Y^-1/33`.

The PHR2 proof converts `(5.16)` on either side of the center into

```text
p_j=Xr^j+O_(w,C)(delta),       delta=Y/B,            (5.17)
```

where `Xr^j asymp_w Y`.  Form the `3 x (L-2)` integer Hankel matrix and all
of its cubic minors,

```text
H=(p_(i+j))_(0<=i<=2,0<=j<=L-3).                    (5.18)
```

The ideal geometric matrix in `(5.17)` has rank one.  In the multilinear
determinant expansion, the terms with zero or one error column vanish, so

```text
|det H_minor|<<Y delta^2+delta^3
       <<Y^3/B^2=Y^(3-2A_ap)=o(1).                  (5.19)
```

Thus every cubic minor vanishes exactly for large `Y`.  Put

```text
D_j=p_jp_(j+2)-p_(j+1)^2.                           (5.20)
```

Unique factorization and distinctness give `D_j!=0`, while `(5.17)` gives

```text
|D_j|<<Y delta+delta^2<<Y^2/B.                      (5.21)
```

The nonzero adjacent minors force `rank(H)=2`, hence one common rational
recurrence

```text
p_(j+2)=s p_(j+1)+t p_j.                            (5.22)
```

Its Cassini identity is `D_(j+1)=-tD_j`.  If `t` is a nonunit rational,
integrality and boundedness of the `D_j` give `L=O(log Y)` immediately.
For `t=+/-1`, clearing denominators shows that `s` is an integer from a fixed
finite set.  PHR2 then treats every hyperbolic pair by its characteristic
roots and the rational-root theorem, again obtaining `O(log Y)`.  The
nonhyperbolic pairs cause repetitions or negative terms except for

```text
(s,t)=(2,-1),       p_(j+2)=2p_(j+1)-p_j.           (5.23)
```

This last sequence is an exact arithmetic progression.  Every prime `ell<L`
must divide its common difference; otherwise `ell` consecutive terms contain
a term divisible by `ell`, and that term is much larger than `ell`,
contradicting primality.  The primorial lower bound and the `O(Y)` shell span
give `L=O(log Y)`.  This is the full PHR2 unit-recurrence classification; a
bare assertion that unit Cassini ratios imply an AP would be insufficient.

For the rank-two model, each fixed second coordinate produces a consecutive
row of length `asymp n`.  Theorem 5.1 excludes an actual embedding of a row
of length `n=Y^(.00895+o(1))` if that row stays on one side.  It does not
exclude arbitrary interlacing of lower and upper nodes: a two-coloring can
avoid monochromatic progressions of length comparable to `log Y`.  Nor does
it follow merely from a weighted-average approximation; `(5.16)` is a
pointwise hypothesis.  The concrete remaining structural target is therefore
either

```text
near extremality => one same-side B^-1-log-AP run of length >>log Y,       (5.24)
```

or a genuinely two-color Hankel-serialization theorem that handles the
interlaced lower/upper pattern directly.

### 5.4 Localized prime energy is abundant, not forbidden

A second fast falsifier changes how a four-cycle theorem could be used.  Put

```text
theta_quad=(2-A_ap)/2=8/33=.24242424... .           (5.25)
```

Partition the two one-sided halves of a fixed prime shell into physical
intervals of width `W=Y^theta`.  The prime number theorem for the whole shell
and pigeonholing give at least one one-sided interval containing

```text
M>>W/log Y                                            (5.26)
```

ordinary primes.  Their additive energy obeys

```text
E_+(P)=#{p_1+p_2=p_3+p_4}
      >=M^4/O(W)>>M^3/log Y.                         (5.27)
```

For all four primes in that interval, an equal-sum quadruple satisfies

```text
|p_1p_2-p_3p_4|=O(W^2),
|log(p_1p_2/(p_3p_4))|=O(W^2/Y^2).                  (5.28)
```

Hence every quadruple in `(5.27)` is a `B^-1`-scale approximate
multiplicative/logarithmic four-cycle whenever

```text
B W^2/Y^2=o(1),       theta<8/33.                   (5.29)
```

Thus an inverse theorem whose arithmetic conclusion is merely “large
approximate additive energy” cannot finish the proof: the actual primes
already contain such clouds at nearly maximal normalized energy.  The
location of that energy is the extra datum.  These examples are confined to
one short physical interval, precisely the geometry addressed by the
short-carrier no-go.

The two thresholds almost coincide.  The hard-core exclusion threshold

```text
theta_H(c)=(3A_ap-2+6c)/11                          (5.30)
```

gives

```text
theta_H(.019)=.241768595...,
8/33-theta_H(.019)=.000655647...;                   (5.31)

theta_H(.0179)=.241168595...,
8/33-theta_H(.0179)=.001255647... .                 (5.32)
```

Exact equality `theta_H(c)=8/33` occurs at `c=2/99=.02020202...`.
Consequently the localized-energy branch is not closed, but its exponent
gap is genuinely tiny.  A useful inverse theorem must preserve enough of the
source normalization to feed such a localized component into the hard-core
theorem; generic energy extraction does not do that.

Within the ordinary-prime, complete-carrier hypotheses covered by the
rigidity results above, the sharp candidate would have to be simultaneously

```text
polynomially participatory,
spatially delocalized,
compatible with the actual prime mask and source event,
and globally one-sided after carrier/corrector cancellation.             (5.2)
```

## 6. Maximum-information next step

The next branch should test the highest-information surviving structural
class.  There are two mutually decisive outcomes.

1. **Source-preserving inverse/stability dichotomy.**  Prove that near
   equality in `(2.1)` produces either (a) a source-carrying high-energy
   component localized below physical diameter `Y^(8/33-o(1))`, or (b) a
   pointwise `B^-1`-accurate same-side log progression longer than
   `C log Y`.  Improve the short-carrier threshold across the `.00066`
   exponent gap in branch (a); PHR2 kills branch (b).  The rank-two family
   shows that the conclusion cannot simply demand one consecutive AP.

2. **Scalable dispersed construction.**  Build an actual-prime, growing-`K`
   coefficient profile satisfying the true source normalization and
   high-band one-sided bound.  Such a family would refute the proposed B3
   route and prevent further time being spent on it.

The first falsifier for the narrow AP version is already `(5.3)--(5.11)`, and
`(5.25)--(5.29)` falsifies the claim that high approximate energy itself is
rare on primes.  Moreover, the project's pair-energy/weighted-BSG hostile
audit already shows that generic BSG extraction can lose the carrier
identity, coefficient signs, and all but a small island of the mass.  The
next theorem must therefore be **source preserving**: the extracted component
must itself carry a fixed fraction of `y dot v=-1`.  If neither branch in
item 1 can be forced, the right fallback is an explicit dispersed,
lower/upper-interlaced actual-prime countermodel.  This is the genuine
remaining case.  Generic moment conversion and generic BSG remain too lossy.

## 7. Status

```text
mean-absorbed effective-participation bound h>>1/P_eff: PROVED;
separator needs P_eff,L>>Y^.0179:                       PROVED;
all bounded-active-block separators:                    EXCLUDED;
two Fourier-close pairs, explicit h>9e-4:               PROVED;
exact synthetic two-pair depth near 1/2:                PROVED;
rank-two autocorrelation saturation of h~1/P_eff:       PROVED;
unique rank-one triangular-Fejer inverse description:    FALSE;
hostile two-pair outer search:                           DIAGNOSTIC ONLY;
growing actual-prime autocorrelation separator:          OPEN;
source-sensitive carrier/corrector theorem (7.5):        OPEN;
LTRAD_full, a uniform zero-free strip, or RH:             NOT PROVED.
```
