# R126 punctured-contour all-moment and keyhole gate

Status: the all-moment derivative estimate is inserted into the R122
punctured-contour argument, and the resulting conditional upper bound for
punctured self-recurrence is proved.  A sharp circular-arc calculation shows
that hiding one unit of winding in an angular gap of size `theta` costs
polynomial degree `Theta(theta^(-2))`.  An explicit nonvanishing target with
that degree is constructed, and a matching lower bound is proved.  Known
effective-universality lower bounds deteriorate much faster than the
all-moment exceptional set, so the two estimates do not overlap.  A
near-one keyhole does not repair this: its transition connectors carry the
same missing winding, while absolute Euler-product control costs
`exp(exp(C/h))` on the density scale.  No fixed zero-free strip, and no
failure of such a strip, is proved.

Date: 2026-08-08.

Predecessor:

* [`R122-ZERO-REPLICATION-DENSITY-GATE.md`](R122-ZERO-REPLICATION-DENSITY-GATE.md).

## 1. Verdict

Let `rho_0=beta+i gamma_0`, `beta>1/2`, be a zero of multiplicity `j`, and
let `D=D(rho_0,r)` contain no other zero and have zero-free boundary
`Gamma`.  Write

```text
m=min_(s in Gamma)|zeta(s)|>0.                         (1.1)
```

Delete an arc of arclength `ell` from `Gamma`, and let
`c_D(ell,m/4)` be the lower density of shifts which approximate `zeta` to
accuracy `m/4` on the remaining arc.  R122 obtained the conditional bound
`c_D(ell,m/4)<<ell^2` from a second moment.  The all-moment replacement is:

```text
c_D(ell,m/4)
 <<_D exp{-c_D L^A (log L)^B},                         (1.2)

L=log(c_D'/ell),
A=1/(1-sigma_*),
B=sigma_*/(1-sigma_*)=A-1,                            (1.3)
```

for every fixed `sigma_*<beta-r`, once `ell` is small enough.  This follows
from the derivative large-deviation proposition of
Lamzouri--Lester--Radziwill (LLR), with its proof localized to the fixed
disc.  Equation (1.2) is forced by the existence of the off-line zero.  It
is not an unconditional lower bound.

Thus a lower-density theorem of the form

```text
c_D(ell,m/4) >= exp{-C_D L^Q},       Q<A,              (1.4)
```

would exclude `rho_0`.  In particular, a uniform fixed `Q` in (1.4) would
give a fixed zero-free strip.  This is much weaker than the power lower
bound in `ell` requested in R122, but it is still far stronger than known
constructive universality bounds.

The obstruction is quantitative and can now be measured exactly.  On a
circle with an angular gap `2 theta`, a zero-free exponential target which
shadows the function `z` on the remaining arc requires degree

```text
n asymp_epsilon 1/[-log cos(theta/2)]
  asymp_epsilon 8/theta^2.                            (1.5)
```

There is an explicit construction attaining this order.  Its logarithm
has norm `exp(O(theta^(-2)))` on a fixed buffer.  In Garunkstis's published
tiny-disc geometry, his explicit phase construction then guarantees only
a density on the scale

```text
exp{-exp(C/(nu theta^2))},                             (1.6)
```

where `nu` must be smaller than the distance of the universality domain
from the line `Re(s)=1`.  This is vastly smaller than the exceptional-set
upper bound (1.2).  Even the optimistic, false-to-current-proof assumption
that the buffered target norm were only `theta^(-q)` would give a guarantee

```text
exp{-theta^(-q/nu+o(1))},                              (1.7)
```

which is still smaller than (1.2) as `theta->0`.  For a general zero-disc,
even this lower bound is not presently published; below it is explicitly
labelled as the optimistic scale of an extension of Garunkstis's proof.

The conclusion is a fail-fast result about the method, not about RH:

```text
all-moment derivative tail                 proved;
sharp winding-unwinder degree              proved;
effective lower bound > derivative tail    fails with known estimates;
fixed zero-free strip                       not proved.                (1.8)
```

## 2. The fixed-compact derivative tail

LLR prove the following for a disc centered at `3/4`; see Proposition 2.1
and Section 4 of [An effective universality theorem for the Riemann
zeta-function](https://doi.org/10.4171/CMH/448).  If `0<R<1/4` and
`sigma(R)=3/4-R`, then

```text
P_T{max_(|z|<=R)|zeta'(3/4+it+z)|>e^V}
 << exp{-b_1 V^[1/(1-sigma(R))]
                (log V)^[sigma(R)/(1-sigma(R))]}      (2.1)
```

uniformly in

```text
b_2<V<=b_3 (log T)^[1-sigma(R)]/log log T.             (2.2)
```

Here `P_T` is normalized Lebesgue measure on `[T,2T]`.  The constants
depend on the fixed disc.

LLR do **not** state the following general-center lemma verbatim.  We derive
the special case needed here by making the parameter replacements in their
proof.  A weaker fallback requiring no such replacement is recorded after
the proof.

### Lemma 2.1 -- general-center derivative tail derived from the LLR proof

Let `K` be a fixed compact set contained in
`1/2<Re(s)<1`, and choose

```text
1/2<sigma_*<min_(s in K) Re(s).                        (2.3)
```

There are positive constants `b_i=b_i(K,sigma_*)` such that

```text
P_T{max_(s in K)|zeta'(s+it)|>e^V}
 <<_(K,sigma_*) exp{-b_1 V^A(log V)^B},                (2.4)

A=1/(1-sigma_*),    B=sigma_*/(1-sigma_*),            (2.5)
```

in the analogue of (2.2).

**Proof.** It is enough to treat one disc `|z-c|<=R`, with
`1/2<c-R<c+R<1`; a finite cover then proves the statement.  In Section 4
of LLR, replace `3/4` by `c` and their quantity `1/4-r` by
`c-R-1/2`.  Their zero-free rectangle still runs from
`1/2+delta_0` to `1`, where one may take any fixed
`0<delta_0<(c-R-1/2)/2`.  Granville--Soundararajan's short-Euler-product
lemma therefore gives the same uniform approximation on the enlarged
disc, with an exceptional set `O(T^(1-delta_1)polylog(T))` for a fixed
`delta_1>0`.  LLR's moment Lemma 4.3 is already stated for an arbitrary
real part `1/2<sigma<1`, so its use on the left edge is unchanged.

In the Cauchy step, take the auxiliary radius `exp(-V/2)` and increase the
lower threshold for `V` so the twice-enlarged disc stays in the strip.
The real part in the moment bound is then
`c-R-2exp(-V/2)`.  For fixed `c,R`, this differs from `c-R` by precisely
the negligible amount handled in LLR's optimization.  The optimized
moment is

```text
k asymp V^[1/(1-sigma_*)]
          (log V)^[sigma_*/(1-sigma_*)].               (2.6)
```

Taking the finite union of the exceptional sets proves (2.4).  This is a
derivation from LLR's proof, not a theorem quoted from their paper.  QED.

There is also a completely verbatim fallback for the zero disc.  After
removing its fixed imaginary center, `D(beta,r)` is contained in the LLR
disc centered at `3/4` of radius

```text
R_0=|beta-3/4|+r<1/4.                                 (2.7)
```

LLR Proposition 2.1 directly gives (2.4) with any left edge slightly below
`3/4-R_0`.  The general-center derivation improves this to any fixed edge
slightly below `beta-r`; the existence of an all-moment tail does not rely
on that improvement.

For a fixed `V`, condition (2.2) is automatic as `T->infinity`.  If the gap
is allowed to shrink with `T`, (2.2) must be retained; it cannot be silently
dropped.

## 3. All-moment completion of the R122 gate

Let `J_ell` be the omitted arc and `K_ell=Gamma\J_ell`.  Put

```text
H_tau(s)=zeta(s+i tau)-zeta(s).                        (3.1)
```

As in R122, if

```text
max_(K_ell)|H_tau|<m/4,
max_(J_ell)|H_tau'|<=m/(2ell),                         (3.2)
```

then

```text
max_Gamma |H_tau|<3m/4<m,                             (3.3)
```

and Rouche replicates the `j` zeros inside `D`.

Let

```text
C_D=max_(s in Gamma)|zeta'(s)|.                        (3.4)
```

For `ell<m/(8C_D)`, failure of the derivative condition in (3.2) implies

```text
max_(s in J_ell)|zeta'(s+i tau)|>m/(4ell).             (3.5)
```

Apply Lemma 2.1 to a fixed neighborhood of `Gamma`, with any
`sigma_*<beta-r`.  With

```text
L=log(m/(4ell)),                                       (3.6)
```

the upper density of (3.5) is at most

```text
<<_D exp{-c_D L^A(log L)^B}.                          (3.7)
```

On the other hand, every shift satisfying both conditions in (3.2)
produces a zero with real part at least `beta-r`.  The Bohr--Landau
zero-density theorem says that the measure of all such shifts is `o(T)`;
the integrated zero-counting argument is Theorem 2.1 of R122.  Therefore:

### Theorem 3.1 -- all-moment punctured-recurrence gate

If the off-line zero `rho_0` exists, then Lemma 2.1 as derived above gives,
for every fixed `1/2<sigma_*<beta-r`,

```text
liminf_(T->infinity) meas U_ell(T)/T
 <<_D exp{-c_D L^A(log L)^B},                          (3.8)
```

where

```text
U_ell(T)
 ={tau in [T,2T]:max_(s in K_ell)
       |zeta(s+i tau)-zeta(s)|<m/4},                  (3.9)
```

and `L,A,B` are given by (3.6)--(2.5).

Without the general-center derivation, the verbatim LLR proposition still
proves the same statement for every
`sigma_*<3/4-(|beta-3/4|+r)`.  All later comparisons remain fail-fast in
that weaker form; only the sharper near-one value of `A` is lost.

This proves (1.2).  In particular, all fixed power lower bounds in `ell`
would now suffice, because

```text
exp{-c L^A(log L)^B}=o(ell^q)                         (3.10)
```

for every fixed `q` whenever `A>1`.

## 4. Exact circular-arc winding cost

The function-theoretic part can be solved sharply.  Normalize the zero
disc to the unit disc and put

```text
K_theta={z=e^(it): theta<=t<=2pi-theta},              (4.1)
```

so the missing angular gap has length `2theta`.  Rotate by `w=-z`.  Then
`K_theta` becomes

```text
Gamma_alpha={e^(it):-alpha<=t<=alpha},
alpha=pi-theta.                                       (4.2)
```

Its logarithmic capacity is

```text
c_alpha=Cap(Gamma_alpha)=sin(alpha/2)=cos(theta/2).   (4.3)
```

This classical capacity formula and the corresponding modern
residual-polynomial framework also appear in
Christiansen--Eichinger--Rubin--Zinchenko,
[Weighted residual polynomials on a circular
arc](https://arxiv.org/abs/2602.05428).

### 4.1 An explicit extremal-scale residual polynomial

Define

```text
Phi_+ + Phi_- = w-1,
Phi_+ Phi_-   =-c_alpha^2 w,                           (4.4)

Q_n(w)=Phi_+(w)^n+Phi_-(w)^n.                         (4.5)
```

Equivalently,

```text
Q_0=2,
Q_1=w-1,
Q_n=(w-1)Q_(n-1)+c_alpha^2 w Q_(n-2).                (4.6)
```

Thus `Q_n` is a polynomial of degree `n`.  At `w=0`, its two characteristic
roots are `0` and `-1`, so

```text
Q_n(0)=(-1)^n.                                        (4.7)
```

On `Gamma_alpha`, both roots in (4.4) have modulus `c_alpha`; this is the
standard two-sheeted conformal map of the circular-arc complement.
Consequently

```text
max_(Gamma_alpha)|Q_n|<=2c_alpha^n.                   (4.8)
```

After rotating back, set

```text
q_n(z)=(-1)^n Q_n(-z).                                (4.9)
```

Then

```text
q_n(0)=1,
max_(K_theta)|q_n|<=2cos(theta/2)^n.                 (4.10)
```

The lower bound at the same exponential scale is immediate from
Bernstein--Walsh.  The Green function of the complement with pole at
infinity satisfies

```text
g_(K_theta)(0,infinity)
 =-log cos(theta/2).                                  (4.11)
```

Hence every polynomial `q` of degree `n` with `q(0)=1` obeys

```text
max_(K_theta)|q|>=cos(theta/2)^n.                    (4.12)
```

Thus (4.10) is within a factor two of the exact residual norm, uniformly
in `n`.

### 4.2 Explicit nonvanishing approximation to one unit of winding

Because `q_n(0)=1`,

```text
p_n(z)=(1-q_n(z))/z                                   (4.13)
```

is a polynomial.  On `K_theta`,

```text
|p_n(z)-1/z|<=2cos(theta/2)^n.                        (4.14)
```

Let `Log_theta z=it` for `z=e^(it)`,
`theta<=t<=2pi-theta`.  Fix one endpoint `z_0` and define the polynomial

```text
P_n(z)=Log_theta(z_0)+integral_(z_0)^z p_n(w)dw.      (4.15)
```

Comparing the integral along the arc gives

```text
max_(K_theta)|P_n-Log_theta z|
 <=4pi cos(theta/2)^n.                                (4.16)
```

Therefore

```text
max_(K_theta)|exp(P_n(z))-z|
 <=exp(4pi cos(theta/2)^n)-1.                         (4.17)
```

For any fixed desired error `0<epsilon<1`, it is enough that

```text
n >= log(4pi/log(1+epsilon))
       /[-log cos(theta/2)].                          (4.18)
```

Since

```text
-log cos(theta/2)=theta^2/8+O(theta^4),               (4.19)
```

this is the upper half of (1.5).

### 4.3 Matching lower bound for every exponential polynomial

Suppose `P` is a polynomial of degree `n` and

```text
max_(K_theta)|exp(P(z))-z|<=epsilon_0                 (4.20)
```

for a sufficiently small absolute `epsilon_0`.  The ratio `exp(P)/z`
lies in a fixed disc about `1`, so it has its principal logarithm there.
On the connected arc,

```text
P(z)-Log_theta z-Log(exp(P(z))/z)                     (4.21)
```

is a constant multiple of `2pi i`.  Subtracting that constant from `P`
does not change `exp(P)` and gives

```text
max_(K_theta)|P|<=2pi+O(epsilon_0).                   (4.22)
```

Choose once and for all an integer `m_0` so that the degree-`m_0` Taylor
polynomial `S_(m_0)(w)` for `exp(-w)` has error at most `1/8` on the disc
in (4.22).  Then

```text
p(z)=S_(m_0)(P(z))                                    (4.23)
```

has degree at most `m_0 n` and, after reducing `epsilon_0` if necessary,

```text
max_(K_theta)|p(z)-1/z|<1/4.                          (4.24)
```

The polynomial

```text
q(z)=1-zp(z)                                          (4.25)
```

has `q(0)=1`, degree at most `m_0 n+1`, and norm less than `1/4` on the
arc.  Applying (4.12),

```text
1<=1/4 exp{(m_0 n+1)[-log cos(theta/2)]}.             (4.26)
```

Consequently

```text
n >= [log 4/(-log cos(theta/2))-1]/m_0
  >> theta^(-2).                                      (4.27)
```

Together, (4.18) and (4.27) prove the sharp degree law (1.5).  The
quadratic inverse-gap loss is a potential-theoretic capacity cost forced
by the winding singularity, not an artifact of an inefficient Mergelyan
approximation.

## 5. The explicit zero-free target on the zeta disc

Factor inside a slightly larger zero-isolating disc as

```text
zeta(s)=(s-rho_0)^j H(s),                             (5.1)
```

where `H` is holomorphic and nonzero.  With

```text
z=(s-rho_0)/r,                                        (5.2)
```

define

```text
F_theta(s)=r^j H(s) exp(jP_n(z)).                     (5.3)
```

This target is holomorphic and nonzero on the full disc.  On the punctured
boundary it approximates `zeta(s)` as closely as desired by (4.17).  It is
therefore a completely explicit version of the nonvanishing target hidden
inside the Andersson/Voronin argument.

There is, however, a buffer cost.  Let the larger disc have radius `R>r`
and put `Lambda=R/r>1`.  Recurrence (4.6) gives, for a constant depending
only on `Lambda`,

```text
max_(|z|<=Lambda)|q_n(z)|<=C_Lambda(Lambda+2)^n.       (5.4)
```

The same bound, up to another fixed factor, holds for `P_n`.  Hence a
branch of `log F_theta` on the larger disc has norm

```text
M_theta<=exp{C_(D,Lambda) theta^(-2)}.                (5.5)
```

The notation in (5.5) records an upper bound for the logarithm's norm;
the target `F_theta` itself can be one exponential larger.  A buffer whose
relative width shrinks with `theta` might improve (5.5), but no effective
universality theorem used here is uniform in that simultaneous shrinking
limit.

## 6. Comparison with known effective universality

Garunkstis gives an explicit lower-density construction for log-zeta
universality in [The effective universality theorem for the Riemann zeta
function](https://klevas.mif.vu.lt/~garunkstis/preprintai/effective.pdf).
His Theorem 1 uses an outer analytic radius `R`, an auxiliary exponent
`nu` satisfying

```text
nu+R<1/4                                                (6.1)
```

for a disc centered at `3/4`, and a prime cutoff `rho` constrained by

```text
M<<rho^nu/log rho.                                     (6.2)
```

The explicit phase-box factor in the density is `(2V)^(-pi(rho))`, with
`50<=V<=rho`; the approximation error makes one choose `V` as a positive
power of `rho`.  For fixed target accuracy this yields the schematic, but
literal, consequence

```text
d_G(M)>=exp{-M^[1/nu+o(1)]}.                           (6.3)
```

For example, Garunkstis's Corollary 2, in its stated tiny-disc and
unit-norm regime, gives

```text
d(epsilon)>=exp(-epsilon^(-13)).                       (6.4)
```

The published theorem is centered at `3/4` and has restrictive radii.
Translating its proof to a disc centered at `sigma_c` would replace (6.1)
by the structurally necessary constraint

```text
nu+R<1-sigma_c.                                       (6.5)
```

We use (6.5) only as an optimistic ledger for a possible extension, not as
a quoted published theorem.

Within Garunkstis's published admissible geometry, substituting (5.5) into
(6.3) gives the constructive scale below.  For an arbitrary center, it is
only the optimistic scale predicted by the extension (6.5):

```text
d_G(theta)
 >=exp{-exp(C/(nu theta^2))}.                          (6.6)
```

By contrast, Theorem 3.1 makes the derivative exceptional set at most

```text
b(theta)
 <<exp{-c L^A(log L)^B},
L=log(1/theta).                                       (6.7)
```

The lower guarantee (6.6) is much smaller than the upper bound (6.7), so
the subtraction

```text
meas(recurrence)-meas(derivative exceptional)         (6.8)
```

has the wrong sign at the level of known estimates.

This failure is not caused only by the fixed-buffer exponential in (5.5).
Suppose optimistically that one had `M_theta<<theta^(-q)`.  Then (6.3)
would give only

```text
d_G(theta)>=exp{-exp[(q/nu+o(1))L]}.                  (6.9)
```

For (6.9) to exceed (6.7), one would need

```text
(q/nu)L < A log L+B log log L+O(1),                   (6.10)
```

which fails as `L->infinity`.

Near a hypothetical line `beta=1-delta`, both `A` and `1/nu` are of order
`1/delta`; that common factor does not change the comparison.  Equation
(6.10) still compares `L` on the constructive side with `log L` on the
derivative side.  Thus the presently explicit effective-universality
machinery does not produce a fixed strip when combined with the LLR tail.

This does **not** show that the true recurrence density is as small as
(6.6).  In the published geometry it shows that the explicit lower bound
is too small to exploit the derivative upper bound.  For a general
zero-disc, no directly applicable explicit lower bound is currently
available, and the optimistic extension is already too small.

## 7. An off-wall rational unwinder, and why it does not change the cost

There is a simple rational map which makes the missing winding visible.
For `a=1-eta`, define

```text
G_a(z)=-z(1-az)/(z-a).                                (7.1)
```

On the unit circle,

```text
|G_a(z)|=1,                                           (7.2)
```

and

```text
G_a(z)/z-1=(a-1)(1+z)/(z-a).                         (7.3)
```

Consequently, off a gap of half-width `theta` centered at `1`,

```text
max |G_a(z)-z|<<eta/theta.                            (7.4)
```

Choosing `eta<<epsilon theta` gives a fixed-quality approximation to `z`.
The zero at `0` and pole at `a` have net winding zero inside the circle;
the pole localizes the unwinding in the omitted gap.

This is a useful geometric model, but not a quantitative escape.  Any
branch of `log G_a` on the major arc still has a nonremovable logarithmic
singularity at `z=0`.  The Green distance of that point is exactly
`-log cos(theta/2)`, so polynomial approximation of the logarithm retains
the `theta^(-2)` cost proved in Section 4.  The rational pole moves the
phase defect; it does not erase the capacity barrier.

## 8. The near-one keyhole

We now test a contour which encloses `rho_0=1-delta+i gamma_0` but spends
most of its boundary in `Re(s)>1`.  Take a thin finger around `rho_0`, join
it to a right-hand body, and split the boundary into

```text
C_left(h)   contained in Re(s)<=1-h,
C_right(h)  contained in Re(s)>=1+h,
J_h         two connectors across 1-h<Re(s)<1+h.      (8.1)
```

The total connector length is `asymp h`.  Hybrid universality can be
asked to control `C_left(h)` while imposing finitely many prime phases;
absolute Euler convergence controls `C_right(h)`.  The connectors must be
filled by a derivative estimate at threshold `asymp1/h`.

### 8.1 Cost of deterministic Euler control on the right

For `sigma>=1+h`, the logarithmic tail after primes up to `Y` is bounded by

```text
sum_(p>Y) p^(-1-h)
 << integral_Y^infinity dx/(x^(1+h)log x)
 =E_1(h log Y).                                       (8.2)
```

For `x=h log Y>=1`, `E_1(x)<<e^(-x)/x`.  Thus fixed accuracy requires

```text
h log Y>=C_epsilon,
Y>=exp(C_epsilon/h).                                  (8.3)
```

Aligning the phases of all `p<=Y` in a box of width `eta_phase` has exact
Kronecker--Weyl density

```text
(2eta_phase)^pi(Y).                                   (8.4)
```

The phase sensitivity of the truncated logarithm contributes at most a
factor `log log Y`, so one may take
`eta_phase` a fixed inverse power of `log log Y`.  Equations (8.3)--(8.4)
then give the constructive scale

```text
-log d_right(h)=exp(C_epsilon/h+o(1)).                (8.5)
```

Hybrid universality supplies positivity after the left-hand condition is
added, but no explicit lower bound which improves (8.5).

### 8.2 The connectors retain the full winding defect

Let `F` be any holomorphic nonvanishing model inside the keyhole.  Suppose
it shadows `zeta` within `m/4` off `J_h`.  Since

```text
wind_C(zeta)=j,
wind_C(F)=0,                                          (8.6)
```

the missing change of argument must occur on `J_h`.  More concretely,
either `|F|` drops from at least `3m/4` at a connector endpoint below
`m/2`, or it stays above `m/2` and its argument supplies a discrepancy of
`2pi j+O(1)`, where the fixed approximation error makes the `O(1)` term
strictly smaller than the full winding discrepancy.  In the first case
the mean-value theorem gives

```text
max_(J_h)|F'|>>m/h;                                   (8.7)
```

in the second case the same conclusion follows from integrating `F'/F`.
Thus a derivative of reciprocal connector length is not merely a
sufficient completion device.  It is forced by winding.

Lemma 2.1 applies to fixed compact subsets strictly inside
`1/2<Re(s)<1`; it does not, as stated, control the part of `J_h` to the
right of `1`.  On the complete pair of connectors the standard
fixed-compact second moment and Cauchy estimate do give

```text
d_bad(h)<<h^2.                                         (8.8)
```

The all-moment bound sharpens (8.8) on every subarc kept in a fixed compact
subset of the universality strip, but no cited theorem supplies that
sharpening uniformly across the full connector.  The available
constructive density scale (8.5) is much smaller even than the rigorous
bound (8.8), so the union-bound intersection again fails.

### 8.3 Why one cannot insert the formal exponent `A=1/h`

It is tempting to seek an across-line extension of (2.4), insert a left
edge `sigma_*=1-O(h)`, and claim an exponent of order `1/h`.  Even before
the across-line issue, LLR's constants are not uniform in that limit, and
their admissible lower threshold `b_2` cannot be ignored.

The loss is already visible in their moment lemma.  It has the form

```text
||log zeta(s,X)||_(2k)
 <<C(sigma) k^(1-sigma)/(log k)^sigma.                (8.9)
```

Put `q=1-sigma` and choose `k` of order `exp(1/q)`.  The left side is at
least its nonzero `L^2` norm, uniformly as `sigma->1`, while

```text
k^q/(log k)^sigma asymp q.                            (8.10)
```

Therefore

```text
C(sigma)>>1/q.                                        (8.11)
```

The large-deviation regime based on (8.9) starts only above a threshold
of at least this scale.  For a keyhole connector,

```text
V=log(derivative threshold)=log(1/h),
q asymp h,
qV=h log(1/h)->0.                                     (8.12)
```

It is below, not above, the uniform high-deviation regime.  The formal
use of the exponent `A=1/h` at this threshold is therefore invalid.  A
Cauchy estimate
shows the same tradeoff: keeping the real-part loss `O(h)` leaves only a
constant bound for the zeta value after multiplying the derivative
threshold `1/h` by a Cauchy radius `O(h)`.

No primary theorem found supplies a uniform near-one, across-line
derivative tail at the connector threshold strong enough to beat (8.5).
The second-moment estimate (8.8) is the valid full-connector estimate used
here.

## 9. Meromorphic winding ledger

The nontrivial zero has `|gamma_0|>0`, so a sufficiently small local
keyhole around height `gamma_0` does not contain the pole at `s=1`.
For large positive shifts, the pole of `zeta(s+i tau)` is at
`1-i tau`, also outside.  On such a contour the argument principle counts
zeros only, exactly as required in R122.

If a contour is instead deformed so that it contains `s=1`, the ledger is

```text
1/(2pi i) integral_C zeta'(s)/zeta(s) ds
 =N_C(zeta)-P_C(zeta).                                (9.1)
```

A simple enclosed zero and the simple pole contribute `1-1=0`.  A
zero-free Euler model also has winding zero, so for a simple zero Rouche no
longer forces a replicated zero.  A zero of multiplicity `j>=2` leaves
winding `j-1` and can at most force those remaining `j-1` zeros; this does
not exclude the simple zeros needed for a fixed-strip theorem.  For
shifted zeta the pole moves to `1-i tau`; comparing
meromorphic functions without tracking the two different pole divisors is
invalid.  The natural pole-regularized function
`Z(s)=(s-1)zeta(s)` does retain vertical-translation structure, since its
translate is `(s+i tau-1)zeta(s+i tau)`.  What fails is transfer of a
self-recurrence estimate for `zeta`: the two multipliers on the base and
shifted functions are very different.  Cancelling only the base pole turns
the target into `(s-1)zeta(s)`, which still contains the prescribed zero
and reinstates the original nonvanishing-target obstruction.

Thus the zeta pole is not an unwinder which can be borrowed for free.  If
it is outside, it is irrelevant; if it is inside, it cancels the winding
certificate of one simple zero.

## 10. Exact remaining theorem

The all-moment improvement changes the clean research target.  A theorem

```text
liminf_(T->infinity) meas U_ell(T)/T
 >=exp{-C_D [log(1/ell)]^Q}                           (10.1)
```

with a fixed exponent `Q`, for the punctured zeta self-target, would combine
with Theorem 3.1.  It would exclude every zero for which one can choose

```text
1/(1-sigma_*)>Q.                                     (10.2)
```

This is a direct fixed-strip criterion.

Known approaches instead give the following hierarchy:

```text
needed recurrence cost        -log c_ell << L^A;
finite-dimensional optimistic -log c_ell ~exp(C L/nu);
fixed-buffer construction     -log c_ell ~exp(C e^(2L)/nu);
LLR derivative exceptional    -log b_ell ~L^A(log L)^(A-1).
                                                                  (10.3)
```

The desired new mechanism must therefore be a collective small-ball or
conditional large-deviation estimate.  It cannot be obtained by aligning
every prime in the cutoff, and it cannot pay independently for all
`Theta(ell^(-2))` coefficients of the arc unwinder.  Equivalently, one
would need to show that the rare winding transition is generated at
stretched-logarithmic entropy cost, then prove that the transition is
jointly compatible with approximation on the major arc.

That joint estimate is exactly where the present path stops.  Proving it
with exponent `Q` would give a fixed zero-free strip through (10.2).
Proving that its true cost is necessarily larger would kill this
zero-replication route, but would not prove that a zero-free strip itself
does not exist.

## 11. Source ledger

Primary sources used here:

* Y. Lamzouri, S. Lester, and M. Radziwill,
  [An effective universality theorem for the Riemann zeta
  function](https://doi.org/10.4171/CMH/448), especially Proposition 2.1
  and its large-moment proof.
* R. Garunkstis,
  [The effective universality theorem for the Riemann zeta
  function](https://klevas.mif.vu.lt/~garunkstis/preprintai/effective.pdf),
  Theorem 1 and Corollary 2.
* J. S. Christiansen, B. Eichinger, O. Rubin, and M. Zinchenko,
  [Weighted residual polynomials on a circular
  arc](https://arxiv.org/abs/2602.05428), for modern context on the
  circular-arc residual-polynomial framework.  The particular polynomial
  construction and estimates in Section 4 are proved directly here.
* J. Andersson,
  [Lavrentiev's approximation theorem with nonvanishing polynomials and
  universality of zeta-functions](https://arxiv.org/abs/1010.0386), for
  empty-interior universality underlying the punctured-contour setup.
