# Global phase-cell compression: Pick reduction and the critical lattice wall

Status: endpoint-leading two-leg-to-one-product reduction, exact causal
Schur/Pick formulation, exact uniform-lattice sign theorem, critical-density
calculation, and a scoped no-go for finite dummy-lattice completion,
2026-08-12.  The global
phase-cell compression theorem is not proved.  The first sharp obstruction
is now identified: present counts allow growing blocks at the critical
Paley--Wiener density, and the universal lattice compressor spends exactly
the whole carrier.  No zero-free strip is proved.

## 1. Verdict

Balanced bipartite splitting removes the earlier same-state factor-two
problem.  The remaining global collateral problem is a single scalar sign
interpolation problem.

Let `U_R,U_L` be the two causal endpoint transfer functions after reflecting
the left endpoint back to the right half-plane.  To leading carrier order,
a collateral pair at

```text
z_j=beta_j-i*delta_j
```

has sign governed by

```text
Re[exp(-i*D*delta_j)*U(z_j)],
U=U_R*U_L.                                          (1.1)
```

The color assigning an exact zero to the right or left leg changes the
factorization of `U`, but not the product in (1.1).  Once a useful inner
product `U` has been found, its scalar Blaschke factors can be greedily
balanced between the two legs.  The same selected-positive state then pays
one full product, up to the largest individual Hardy weight.

There is an explicit universal solution at the critical density of one
factor per complete phase cell:

```text
B_(a,D)(s)
 =cosh((D/2)*(s-a))/cosh((D/2)*(s+a)).              (1.2)
```

It signs **every** point with `0<=Re s<=a`, not just a prescribed finite
list.  But

```text
B_(a,D)(alpha)=exp(-alpha*D+O(1))       (alpha<=a), (1.3)
```

so its one-product bill consumes the entire `exp(alpha*D)` selected
carrier.  It is a boundary object, not an isolation theorem.

Truncating the dummy lattice to a finite ordinate band leaves a positive
formal potential exponent.  However, the omitted lattice tail also removes
exactly the phase delay needed to sign the whole band.  To first order in
the band edge `H`, restoring that phase by a compact delay costs precisely
the residual exponent.  Thus finite dummy-lattice completion plus ordinary
delay compensation cannot close the argument.

The surviving possibility is narrower and genuinely discrete: solve the
Pick sign problem only at the actual occupied clusters, at subcritical
*effective* density, and compactly realize a balanced factorization without
completing all missing cells.  Current Bellotti--Wong and Huxley inputs do
not provide the strict local density or spacing needed by standard stable
interpolation theorems.

## 2. Exact global grouping problem

After demodulation, the complete reflected-pair form is

```text
Q_j(q)
 =(2/L^2)*Re[F_q(z_j)*conj(F_q(-conj(z_j)))].       (2.1)
```

For two endpoint components, factor their dominant Laplace weights as

```text
F_R(z)=exp(z*D/2)*U_R(z)*R_0(z),
conj(F_L(-conj(z)))
      =exp(z*D/2)*U_L(z)*L_0(z),                   (2.2)
```

where the harmless base profiles have already been phase-normalized.  The
two exponentials in (2.2) produce `exp(beta_j*D-i*delta_j*D)`, so the
carrier-leading sign is (1.1).

This gives the leading endpoint analytic target.  Reverse-endpoint leakage
and base-profile errors must be restored in the compact transfer; they are
not part of the unrestricted Pick problem below.

### Global phase-cell compression problem

Given a maximal-depth target `alpha`, collateral nodes

```text
0<beta_j<=alpha,
```

and `D=dL`, construct right-half-plane Schur functions `U_R,U_L` such that

```text
Re[exp(-i*D*delta_j)*U_R(z_j)*U_L(z_j)]>=0          (2.3)
```

for every carrier-relevant collateral cluster, while

```text
-log|U_R(alpha)|-log|U_L(alpha)|
```

obeys the one-product potential bound and both inverse Laplace transforms
fit in the available compact endpoint layers with subcarrier error.

Exact row annihilation is the special case in which at least one factor in
(2.3) vanishes.  Coherent grouping is more general: all rows in one cluster
may satisfy the sign inequality without any of them being an exact zero.

## 3. Exact Nevanlinna--Pick formulation

First ignore compact support and factorization.  Put `U=U_R U_L`; it is a
Schur function.  For a proposed target amplitude `A in [0,1)`, introduce
interpolation values

```text
w_0=A,
w_j in C_j,
C_j={w: |w|<=1,
          Re[exp(-i*D*delta_j)*w]>=0}.              (3.1)
```

The half-line grouping problem is feasible if and only if values `w_j`
can be chosen so that the Pick matrix

```text
P_(r,s)
 =[1-w_r*conj(w_s)]/[z_r+conj(z_s)]                (3.2)
```

is positive semidefinite, where `z_0=alpha`.  Thus

```text
A_*=sup {A: there exist w_j in C_j with P>=0}       (3.3)
```

is the exact unrestricted causal phase-cell optimum.  Prescribing `w_j=0`
recovers the ordinary Blaschke product.  Allowing the half-disks `C_j` is
the precise mathematical meaning of sign grouping.

After an inner solution is found, factor its Blaschke zeros into
`U_R U_L`.  If their target potentials are `S_R,S_L`, the selected-row
harmonic mean has exponent loss

```text
2*max(S_R,S_L).                                    (3.4)
```

If `omega_k` denotes the nonnegative target potential of the `k`-th
Blaschke factor, greedy coloring makes (3.4) equal the total potential plus
`O(max_k omega_k)`.  Therefore the Pick problem and the bipartite balance
are separate: (3.3) decides global grouping; coloring restores the
same-state one-product bill.

For finite physical support, (3.2) is only a relaxation.  Exact zeros on a
leg instead have the truncated-Cauchy Gram kernel

```text
K_W(z,w)
 =[1-exp(-(z+conj(w))*W)]/[z+conj(w)],              (3.5)
```

and the retained endpoint evaluation is its Gram Schur complement.  A
compact sign analogue of (3.2) is the genuinely missing theorem.

## 4. Exact uniform-lattice compressor

Fix `a,D>0` and define (1.2).  Its zeros are

```text
a+i*(2*k+1)*pi/D,       k in Z.                    (4.1)
```

Thus there is exactly one zero per phase cell of width `2*pi/D`.  On the
imaginary axis the numerator and denominator of (1.2) are conjugates, so
`B_(a,D)` is inner.

### Theorem 4.1 (uniform-lattice continuum sign)

If

```text
0<=beta<=a,
tanh(a*D)>=1/2,                                    (4.2)
```

then for every real `delta`,

```text
Re[exp(-i*D*delta)*B_(a,D)(beta-i*delta)]>=0.       (4.3)
```

#### Proof

Put

```text
u=D*(a-beta)/2,       v=D*(a+beta)/2,
x=D*delta/2,          c=cos x, s=sin x.             (4.4)
```

After multiplying numerator and denominator by the conjugate denominator,
the numerator of the real part in (4.3) is exactly

```text
cosh(u)*cosh(v)*c^4
+sinh(u)*sinh(v)*s^4
+[2*sinh(a*D)-cosh(a*D)]*c^2*s^2.                 (4.5)
```

All three coefficients are nonnegative under (4.2), proving (4.3).
QED

This is stronger than one-representative annihilation: one fixed inner
function signs the entire depth/ordinate continuum below its zero line.
Choosing `a>alpha` gives a strict depth margin for every actual collateral
with `beta<=alpha`.

### Exact delay representation

Put `r=exp(-aD)`.  Direct algebra gives

```text
B_(a,D)(s)
 =[r+exp(-D*s)]/[1+r*exp(-D*s)].                   (4.6)
```

Hence it is exponentially close to a pure delay `exp(-D*s)` when
`aD` is large.  Its boundary group delay is

```text
tau_(a,D)(omega)
 =D*sinh(aD)/[cosh(aD)+cos(D*omega)]
 =D+O(D*exp(-aD)).                                 (4.7)
```

The sign theorem is therefore a precise all-pass version of the virtual
translation suggested by the fixed-microcluster construction.

At the target,

```text
B_(a,D)(alpha)
 =cosh(D*(a-alpha)/2)/cosh(D*(a+alpha)/2)
 =exp(-alpha*D+O(1))                               (4.8)
```

for fixed `a>=alpha`.  One full critical lattice costs the full selected
carrier exponent.

## 5. Bipartite lattice factorization

Split the zeros (4.1) into alternating sublattices.  Each sublattice has
spacing `4*pi/D`, hence its inner factor has asymptotic delay `D/2` and
target potential `alpha*D/2+O(1)`.  Call the factors `B_R,B_L`.  Then

```text
B_R*B_L=B_(a,D).                                    (5.1)
```

The collateral sign depends on the union product (5.1), while the selected
positive-row amplitude depends on the harmonic mean of the two endpoint
capacities.  The alternating split is balanced, so its loss is

```text
2*max(alpha*D/2+O(1),alpha*D/2+O(1))
 =alpha*D+O(1).                                    (5.2)
```

Thus bipartite splitting is algebraically optimal but cannot make the full
critical lattice profitable.  It does, however, show the exact compact
geometry one would want: two delays of `D/2` propagating inward from the
opposite endpoints.

The inverse Laplace transforms are not compact.  Formula (4.6) expands into
delays `D,2D,...` with geometrically decreasing coefficients; each
alternating factor similarly begins near delay `D/2` and has an infinite
tail.  Whether the available physical endpoint layers include a strict
margin beyond those two `D/2` delays is part of the compact-support gate.

## 6. Nonuniform representatives and the best effective density

For fixed real part `a`, a zero `a+i*eta` contributes boundary group delay

```text
2*a/[(omega-eta)^2+a^2],                            (6.1)
```

whose integral is `2*pi`.  If there is exactly one representative in every
cell of width `h=2*pi/D`, then elementary quadrature gives, uniformly in
`omega`,

```text
sum_k 2*a/[(omega-eta_k)^2+a^2]
 =D+O_a(1).                                         (6.2)
```

The error is exponentially small for the exact lattice and only bounded
for arbitrary within-cell jitter.  Hence one factor per cell is the correct
phase-winding density: it produces one delay `D`, and no generic all-pass
construction can use fewer degrees to track adversarial phases in every
occupied cell.

This density is also the Paley--Wiener critical density

```text
q_L=D/(2*pi)=d*L/(2*pi).                            (6.3)
```

The Riemann--von Mangoldt off-line-pair main density is

```text
p_L=L/(4*pi),                                       (6.4)
```

so the average utilization is `p_L/q_L=1/(2d)<1` when `d>1/2`.
But the Bellotti--Wong endpoint allowance does not force its additional
`0.10076 L` pair centers to remain in one shrinking cluster.  It may be
spread through a fixed-width band; combined with the main count, the
extremal allocation from Section 4 of the density report saturates `q_L` on
a constant-width, hence `Theta(L)`-cell, consecutive block.  Even ideal
within-cell grouping does not lower that abstract occupancy.  Huxley's
fixed-depth global bound permits such one-off `O(L)` blocks at the selected
height.

Therefore current inputs give no strict upper Beurling density below
`D/(2*pi)`.  Generic stable Paley--Wiener interpolation theorems require a
strict density margin; critical-density sequences can have arbitrarily bad
finite-section conditioning under allowed perturbations.  The best
uniform effective density justified by phase winding is exactly one
condition per occupied cell, and the current count can reach the endpoint
of that capacity.

### 6.1 Average group delay does not center the cell phase

There is a tempting but incomplete argument at the main pair density.  A
uniform representative lattice of density `L/(4*pi)` has delay

```text
tau=L/2<D.
```

The residual phase changes by less than `pi/2` across a half-cell when
`d>1/2`.  This controls phase **variation**, but it does not put the phase
in the favorable half-plane at the cell center.

The failure is already visible in the exact sparse lattice

```text
B_(a,tau)(s)
 =cosh((tau/2)*(s-a))/cosh((tau/2)*(s+a)),          (6.5)
```

whose roots on `Re s=a` are

```text
delta_k=(2*k+1)*pi/tau.                             (6.6)
```

For `a*tau` large, near such a root,

```text
exp(-i*D*delta)B_(a,tau)(a-i*delta)
 =-i*tau*exp(-a*tau-i*D*delta_k)
    *[1+O(exp(-2*a*tau))]*(delta-delta_k)
    +O((delta-delta_k)^2).                         (6.7)
```

If a collateral cluster has members on both sides of the representative,
nonnegativity requires the linear coefficient in (6.7) to be purely
imaginary, equivalently

```text
sin(D*delta_k)=O(exp(-a*tau)).                      (6.8)
```

That condition is not implied by `tau<D`.  Consecutive root orientations
rotate by

```text
D*(delta_(k+1)-delta_k)=2*pi*D/tau=4*pi*d.         (6.9)
```

For example, at `d=2/3` only one residue class of the sparse lattice has
the required tangency; the other roots cross the favorable boundary and
give opposite signs on their two sides.

Thus a Poisson/group-delay upper bound alone does **not** prove one-cell
grouping.  A successful tailored construction must also solve one absolute
phase/tangency condition per occupied cluster.  Those coupled conditions
are exactly what the Pick problem (3.1)--(3.3) retains and a density-only
argument forgets.

## 7. Why finite dummy-lattice completion spends its gain

Complete all phase cells with dummy factors only in `[-H,H]`, at density
`D/(2*pi)`, and put their zeros on the line `Re s=a>=alpha`.  The one-product
target potential per unit `L` is

```text
S_H/L
 =(d/(2*pi))*integral_(-H)^H
   (1/2)*log[
    ((alpha+a)^2+delta^2)
    /((alpha-a)^2+delta^2)] d delta.                (7.1)
```

The full-line integral is `2*pi*alpha`.  Consequently the formal exponent
left by the finite band is

```text
E_H
 =alpha*d-S_H/L
 =(d/(2*pi))*integral_(|delta|>H) V_(alpha,a)(delta)d delta
 =2*d*alpha*a/(pi*H)+O(H^(-3)).                    (7.2)
```

This looks positive for every fixed `H`.  The same omitted factors carry
the missing phase delay.  At the center of the completed band, the truncated
lattice supplies

```text
tau_H
 =D*(2/pi)*atan(H/a)+O(1),                          (7.3)
```

so the missing delay is

```text
Delta tau
 =D-tau_H
 =2*d*a*L/(pi*H)+O(L*H^(-3))+O(1).                 (7.4)
```

A compact pure delay restoring this phase has target attenuation
`exp(-alpha*Delta tau)`.  Equations (7.2)--(7.4) give the exact leading
identity

```text
alpha*Delta tau/L=E_H+O(H^(-3))+O(L^(-1)).         (7.5)
```

Thus ordinary delay compensation spends precisely the exponent apparently
saved by truncating the dummy lattice.  Without compensation, the residual
phase drifts through adversarial cells; current zero counts do not prevent
actual nodes from occupying the bad phases.

This is a scoped no-go:

```text
finite uniform dummy completion
+ uniform phase correction by translation
does not retain a fixed carrier exponent.           (7.6)
```

It does not rule out a discrete Pick interpolant tailored only to the
actual occupied cells.

## 8. Why the standard analytic tools stop here

### 8.1 Nevanlinna--Pick

Pick theory solves the unrestricted half-line value problem exactly through
(3.2).  Its extremal is rational inner and has reflected poles in the left
half-plane.  Its inverse Laplace transform has an infinite causal tail.
Pick positivity alone supplies no finite-support transfer for a growing
critical list.

### 8.2 Compact inner functions

An entire right-half-plane inner function of finite exponential type has no
finite Blaschke factors: their reflected poles would have to remain.  Up to
a unimodular constant, the compactly realizable scalar inner factors are
pure delays `exp(-tau*s)`.  Hence a nontrivial all-pass zero compressor
cannot be both exactly inner and exactly compact.  A successful packet must
accept an outer/norm defect and prove it is below the carrier margin.

### 8.3 Independent composition of microcluster filters

The fixed-cluster virtual translation uses a degree-`r` differential filter
and pays `L^r`.  Multiplying independent normalized filters over
`K=Theta(L)` cells pays

```text
L^(r*K)=exp(Theta(L*log L)),                         (8.1)
```

which is larger than every available carrier.  Therefore the proved local
microcluster theorem cannot be globalized by cellwise tensoring or
composition.  A single shared inner/Pick interpolant is essential.

### 8.4 Global density

Huxley bounds the total number of deep zeros by a positive power of `T`.
An `O(L)` critical block at one exceptional target height is much smaller
than that ceiling.  It therefore supplies neither a local density gap nor a
uniform Pick/Gram conditioning constant.

## 9. Exact next theorem

The remaining divisor-side theorem can now be stated without ambiguity.

> For every actual target-local collateral list obeying the zeta count,
> solve the half-disk Pick problem (3.1)--(3.3) with target loss bounded by
> the compressed one-product potential; factor the solution into two
> greedily balanced endpoint legs; and approximate both causal factors in
> the available finite PW/Gabor support with error
> `o(exp(E_1 L))`, where `E_1>0` is the compressed density margin.

The uniform lattice proves that phase-cell compression is analytically
possible at exactly one factor per cell.  The dummy-lattice calculation
proves that a universal continuum solution at that density is too expensive.
The unresolved content is therefore **discrete subcritical interpolation
through locally critical blocks**, together with its compact two-tail
realization.

## 10. Truth table

| assertion | verdict |
|---|---|
| two endpoint sign filters reduce to their product | **proved at leading endpoint-carrier order** |
| their zeros can be balanced back to one-product same-state loss | **proved** |
| half-line grouping has the Pick formulation (3.1)--(3.3) | **proved** |
| one exact lattice factor per phase cell signs all `beta<=a` | **proved** |
| the full lattice retains a positive carrier exponent | **false** |
| finite dummy completion plus ordinary delay repair retains its tail exponent | **false to leading order**, by (7.5) |
| one factor per cell is the critical phase/PW density | **proved** |
| current counts force a strict subcritical local density | **not implied by current inputs** |
| independent composition of the fixed-cluster filters is affordable | **false** |
| tailored discrete Pick grouping has a uniform compact realization | open |
| actual-zeta collateral isolation | open |

Companion reports:

- [`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`](ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md),
- [`ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`](ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md), and
- [`ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`](ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md).
