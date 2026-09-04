# QP exceptional translated-AP promotion hostile audit

**Date:** 2026-08-14

**Verdict:** the singular-denominator idea is closed, but a uniform
determinant-sign exclusion of exceptional AP steps is false as a proof class.

For the first-`M` harmonic AP with distinct cosine nodes, a zero of the
constant Chebyshev coefficient `r_0` makes the interpolation system
inconsistent.  Approaching such a zero at fixed `M` sends the directional TV
to infinity and a positive-antipode depth to zero.  A singular `r_0` on this
distinct-node locus is therefore an obstruction, not a source of cheap
promotion.  Exact cosine-node collisions are a separate rank-deficient locus
and are not subsumed by that statement.

In the opposite direction, positive coefficient signs are fully compatible
with `M` prescribed real roots.  More strongly, for **every** set of `M`
positive harmonic indices `K`, including the genuinely all-remote translated
block

```text
K={M,M+1,...,2M-1},
```

there is an open phase chamber on which those harmonics realize a positive
antipode of fixed depth.  If the actual absolute prime-log nodes are linearly
independent over `Q`, the Kronecker flow visits that chamber infinitely often,
and in fact with positive limiting time density.  The resulting steps are
arbitrarily remote.

For the width used in the QP packet, the actual prime-power nodes are
`Q`-independent for every `Y` outside an explicit countable exceptional set.
Thus Chebyshev systems, total positivity, determinant sign variation,
trigonometric moment-curve geometry, and coefficient positivity cannot prove
that exceptional positive AP steps never occur.

This does **not** promote QP.  Kronecker recurrence gives no uniform bound for
the first visit as `M` grows.  The QP step aperture is only

```text
B/M=Y^(17/33+o(1)),
```

whereas published quantitative Kronecker theorems are upper hitting-time
theorems on exponentially or worse growing-dimensional scales.  They are not
lower nonreturn theorems.  Turan--Nazarov has exponential-polynomial order at
least `2^M` for the relevant determinant coefficient, and actual-prime large
value theorems count exceptional packets without proving that a deterministic
AP misses them.

The sole surviving AP question is consequently precise:

```text
does the actual prime-log flow enter a positive determinant chamber
before the polynomial QP aperture?
```

No surveyed primary theorem answers this.  No QP promotion, QP kill, zeta
bound, or zero-free strip is proved here.

---

## 1. Exact AP polarity

Let the distinct absolute feature nodes be

```text
u_1,...,u_M>0,       a(t)=(cos(t u_j))_(j<=M),
q_0=(1,...,1).                                          (1.1)
```

For the first-`M` AP put

```text
x_j=cos(tau u_j),
R_tau(x)=product_(j<=M)(x-x_j)=sum_(k=0)^M r_k T_k(x).  (1.2)
```

Throughout the `r_0` statements in Sections 1--2, assume that the `x_j` are
distinct.  If cosine rows collide, the repeated interpolation equations must
first be quotiented; a repeated-root nodal product does not encode their
multiplicity and the divisibility proof below does not apply.

The exact square representation

```text
q_0=sum_(k=1)^M c_k a(k tau)                            (1.3)
```

exists if and only if `r_0!=0`, in which case

```text
c_k=-r_k/r_0,
C_AP=sum_(k>=1)|r_k|/|r_0|.                            (1.4)
```

The same support realizes a positive antipode

```text
sum_(k=1)^M w_k a(k tau)=-r q_0,
w_k>=0, sum w_k=1, r>0                                 (1.5)
```

if and only if every `c_k<=0`.  Since the nodal product is monic,

```text
r_M=2^(1-M)>0.                                         (1.6)
```

Hence positivity forces

```text
r_0>0, r_k>=0 for every k>=1,
w_k=r_k/[R_tau(1)-r_0],
r=r_0/[R_tau(1)-r_0].                                  (1.7)
```

These signs and the depth are directional.  An ordinary Vandermonde
determinant or Gram determinant does not replace them.

For an arbitrary harmonic index set

```text
K={k_1<...<k_M},                                       (1.8)
```

the positive equations are the square augmented system

```text
sum_(k in K)w_k cos(k theta_j)+r=0,   j<=M,
sum_(k in K)w_k=1.                                    (1.9)
```

The relevant determinant is that of

```text
[ (cos(k theta_j))_(j,k)    1 ]
[              1^T          0 ].                      (1.10)
```

The next two sections audit both possible determinant strategies.

## 2. Singular `r_0` is an exact no-go

### Theorem 2.1 (distinct-node singular inconsistency and fixed-degree blowup)

For (1.2):

1. if `r_0=0`, (1.3) is inconsistent;
2. if `r_0!=0`,

   ```text
   C_AP>=2^(1-M)/|r_0|;                                (2.1)
   ```

3. along a positive chamber,

   ```text
   r<=2^(M-1) r_0.                                     (2.2)
   ```

Consequently, at fixed `M`, approaching `r_0=0` makes the signed cost diverge
and every positive depth tend to zero.

#### Proof

At `r_0=0`, the nodal product is a nonzero polynomial in
`span{T_1,...,T_M}` vanishing at every `x_j`; hence the no-constant evaluation
matrix is singular.  If a polynomial `P` in the same span took value one at
all the roots, then `P-1=lambda R_tau`.  Its constant Chebyshev coefficient is
`-1` on the left and zero on the right, a contradiction.

Equation (2.1) follows from the fixed leading coefficient (1.6).  In a
positive chamber all coefficients in (1.7) are nonnegative, so

```text
r=r_0/sum_(k>=1)r_k<=r_0/r_M,
```

which is (2.2).  QED

The fixed-degree qualification matters.  Since `r_M=2^(1-M)`, this does not
give a useful uniform asymptotic bound merely from the statement that an
unscaled `r_0` is small.

There is a transparent degree-two model.  Put `a=1/sqrt(2)` and take roots

```text
a-delta, -a,       delta>0.
```

Then exactly

```text
r_0=a delta,       r_1=delta,       r_2=1/2,           (2.3)
C_AP=(delta+1/2)/(a delta),
r=(a delta)/(delta+1/2).                               (2.4)
```

All three coefficients are positive, but the cost tends to infinity and the
depth to zero.  At `delta=0`, the no-constant matrix has rank one while the
matrix augmented by `q_0` has rank two.  The verifier replays this exact
limit.

## 3. Positive determinant chambers exist for every harmonic block

The singular no-go does not extend to a sign no-go away from the singular
locus.

### Theorem 3.1 (universal interior positive harmonic template)

Let `K` be any set of `M` distinct positive integers and let `0<d<1`.  There
exist distinct phases

```text
theta_1,...,theta_M in (0,pi),
```

strictly positive weights `w_k`, and a depth `r>0` such that (1.9) holds.
The augmented determinant (1.10) is nonzero.  The phases may be chosen so
that `r` is arbitrarily close to `d`.

Therefore the same strict positivity and a fixed positive depth persist on
an open neighborhood of the phase vector.

#### Proof

Write `D=max K`.  The cosine polynomial

```text
F_0(theta)=d+cos(D theta)                               (3.1)
```

has exactly `D` simple roots in `(0,pi)`.  On those roots evaluate the `M`
functions

```text
1,   cos(k theta),       k in K without {D}.            (3.2)
```

Their evaluation matrix has column rank `M`: otherwise a nonzero cosine
polynomial of degree at most `D-1`, equivalently an algebraic polynomial in
`cos(theta)` of degree at most `D-1`, would vanish at `D` distinct points.
Select `M` roots on which an `M` by `M` minor is nonzero.

For small `epsilon>0`, put

```text
F_epsilon(theta)
 =d+cos(D theta)+epsilon*sum_(k in K, k<D)cos(k theta). (3.3)
```

The selected simple roots continue to distinct roots of (3.3).  Normalize
the nonconstant coefficients by

```text
W=1+(M-1)epsilon.
```

Then (1.9) holds with

```text
w_D=1/W,
w_k=epsilon/W for k<D,
r=d/W.                                                 (3.4)
```

At `epsilon=0`, a homogeneous vector in the kernel of (1.10), after using
the last row to eliminate its `D`th coefficient, would give a linear
dependence among (3.2) on the selected roots.  Thus (1.10) is nonsingular at
the base point and remains so for small `epsilon`.  Equations (3.4) are then
the unique solution and are strictly positive.  Letting `epsilon` tend to
zero makes `r` tend to `d`.  QED

This applies directly to

```text
K={1,...,M}                         first-M AP,
K={M,...,2M-1}                      all-remote translated harmonic block.
                                                               (3.5)
```

For the all-remote block the certificate can be written in the original
signed-representation polarity with no matrix inversion.  Set `D=2M-1` and

```text
F_epsilon(theta)
 =1/2+epsilon*sum_(k=M)^(D-1)cos(k theta)+cos(D theta). (3.6)
```

Let `Delta=(sqrt(2)-1)/2`, fix `0<c<Delta`, and take
`epsilon=c/M`.  Bracket every root of `F_0` at phase distance
`pi/(12D)`.  The base endpoint magnitude is at least `Delta`, while the
whole perturbation is smaller than `(M-1)epsilon<c`; hence all `D` simple
roots persist uniformly.

The continued `D` roots give a root-by-`K` matrix of rank `M`.  Indeed, a
supported cosine polynomial of degree at most `D` vanishing at all `D` roots
would be proportional to `F_epsilon`; its missing zero-frequency coefficient
makes that impossible.  Select an invertible `M`-row minor.  At every
selected root,

```text
1=-2 epsilon*sum_(k=M)^(D-1)cos(k theta)-2cos(D theta). (3.7)
```

Thus the exact carrier coefficients are

```text
c_M=...=c_(D-1)=-2 epsilon,       c_D=-2,
C_AP=2[1+(M-1)epsilon],
r=1/C_AP=(1/2)/[1+(M-1)epsilon].                 (3.8)
```

Every coefficient has the correct strict sign, and the selected evaluation
minor plus `sum c_k<0` makes the augmented system nonsingular.  With the
uniform choice `epsilon=c/M`,

```text
r=(1/2)/[1+c(M-1)/M] >=1/[2(1+c)],                    (3.8a)
```

while every support atom lies between `M tau` and `(2M-1)tau`.  Thus the
all-remote positive chamber has both a uniform fixed depth and a rigorously
uniform inverse-degree perturbation.

For the first family there is also a completely explicit template.  Put

```text
Delta=(sqrt(2)-1)/2,
epsilon_M=Delta/(4M)=(sqrt(2)-1)/(8M),
F_M(theta)=1/2+epsilon_M*sum_(k<M)cos(k theta)+cos(M theta).
                                                               (3.9)
```

Around each root of `1/2+cos(M theta)`, take a bracket of radius
`pi/(12M)`.  The unperturbed endpoint magnitude is at least `Delta`, while
the entire perturbation has magnitude less than `Delta/4`.  Every bracket
therefore retains a sign change.  Since a degree-`M` cosine polynomial has at
most `M` roots in `(0,pi)`, (3.9) has exactly `M` simple roots there.  Its
normalized antipode depth is

```text
r_M^template
 =1/[2(1+(M-1)epsilon_M)] >.47.                       (3.10)
```

This is already much deeper than the requested `Y^(-.0180303234...)` scale.
It is a phase-space construction, not yet a legal finite-height actual-node
construction.

Theorem 3.1 is also consistent with the primary literature.  Dubickas gives
recursive families of cosine polynomials with every coefficient positive,
all roots on the unit circle after symmetrization, and asymptotically
uniformly distributed root arguments.  Thus neither coefficient positivity
nor coarse root equidistribution can distinguish a forbidden chamber.

## 4. Kronecker transfers the chambers to generic actual nodes

### Theorem 4.1 (eventual positive AP recurrence)

Suppose `u_1,...,u_M` are linearly independent over `Q`.  Fix any harmonic
set `K` as in Theorem 3.1.  Then there is a positive-depth chamber `U` and a
set of steps `tau` of positive limiting density such that

```text
(tau u_1,...,tau u_M) mod 2pi belongs to U             (4.1)
```

and the support `{k tau:k in K}` realizes a positive antipode.  In
particular, such steps occur arbitrarily far out.

#### Proof

Theorem 3.1 and nonsingularity make the strict positive solution an open
condition in the phase torus.  The continuous Kronecker flow

```text
tau ->(tau u_j mod 2pi)_(j<=M)                         (4.2)
```

is dense and uniquely ergodic when no nonzero integer vector annihilates
`u`.  Choose a small box with boundary of Haar measure zero inside the
positive chamber.  Its visit frequency equals its positive Haar measure.
QED

For the actual prime-power shell this independence is generic in an explicit
sense.  Write

```text
n_j=p_j^(a_j),
u_j=|log(n_j/Y)|.                                      (4.3)
```

When the multiplicative half-width is `w=.2`, two different powers of the
same prime cannot both occur: their ratio is at least two, whereas
`exp(2w)<2`.  Thus the prime bases in (4.3) are distinct.  If
`sum m_j u_j=0`, put `epsilon_j=sign(log(n_j/Y))`; then

```text
sum_j m_j epsilon_j a_j log p_j
 =(sum_j m_j epsilon_j)log Y.                          (4.4)
```

If the coefficient of `log Y` is zero, unique factorization forces every
`m_j=0`.  Otherwise (4.4) forces

```text
Y^q in Q for some nonzero integer q.                   (4.5)
```

Hence the actual absolute nodes are `Q`-independent whenever no nonzero
integral power of `Y` is rational.  The excluded `Y` form a countable set.
This statement also excludes absolute-node collisions and zero nodes.

The conclusion is deliberately asymptotic in `tau` for each fixed node
system.  It does not say that a visit occurs before `B/M` when `M` and `B`
grow with `Y`.  That quantifier distinction is exactly the surviving gate.

The theorem covers harmonic translated blocks `k tau`, including (3.5).  It
does not claim the same result here for an additive shift `s+k tau` with `s`
fixed independently of `tau`; that family has row-dependent sine terms and
requires a separate augmented determinant analysis.

## 5. The finite-aperture problem begins with a negative prime peak

Put

```text
S_Y(t)=<q_0,a(t)>=sum_(j<=M)cos(t u_j).                 (5.1)
```

If a positive AP design of depth `r` exists, pairing it with `q_0` gives

```text
sum_(k in K)w_k S_Y(k tau)=-rM.                        (5.2)
```

Therefore necessarily

```text
min_(k in K) S_Y(k tau)<=-rM.                          (5.3)
```

There is also a weighted localization statement.  At least

```text
r/(2-r)                                                (5.4)
```

of the AP probability lies on harmonics satisfying

```text
S_Y(k tau)<=-rM/2.                                     (5.5)
```

Indeed, on the complement of (5.5) the normalized sum is greater than
`-r/2`, while it is at least `-1` everywhere; solving the resulting two-point
extremal inequality gives (5.4).

At the promotion depth `r=Y^(-kappa+eta)`, (5.3) is a sign-resolved
near-maximal actual-prime Dirichlet-polynomial event.  Guth--Maynard covers
the corresponding absolute-value set by `Y^(2kappa+o(1))` fixed-width
packets, and the existing dilation-shadow theorem proves that almost every AP
step misses them.  It does not prove that a deterministically selected step
misses them, nor does it retain the negative sign in the absolute-value
packet count.

Thus either of the following would settle the positive AP subroute:

```text
uniform negative-peak exclusion:
  S_Y(k tau)>-M Y^(-kappa+eta)
  for every legal tau and k in K;                      (5.6)

or exceptional-chamber exclusion:
  every legal (tau,k) hitting the negative packets
  fails the augmented determinant signs.               (5.7)
```

No theorem surveyed proves (5.6) or (5.7).

## 6. Why the named classical tools stop here

### Chebyshev systems, total positivity, and `c`-optimal design

The functions `1,T_1,...,T_M` form a Chebyshev system on `(-1,1)`.  This
gives the uniqueness in (1.4) and controls the sign of the full ordered
Vandermonde.  It does not control the signs of all replacement ratios
`r_k/r_0`.  Theorem 3.1 supplies an open family on which every required sign
is favorable.

Elfving's theorem identifies directional optimal design with a boundary
point of a symmetric convex hull.  Dette--Melas solve fixed-order Fourier
`c`-optimal problems on fixed arcs.  Neither theorem controls when the
growing actual prime-log orbit reaches the relevant exposed face.

The symmetric trigonometric moment curve has rich locally neighborly faces,
as Barvinok--Lee--Novik prove.  That geometry confirms that high-dimensional
trigonometric convex hulls can have many structured faces; it is not a
finite-height hitting theorem for (4.2).

### Positive-coefficient and Littlewood theory

Dubickas proves the existence of positive-coefficient self-reciprocal
polynomials whose roots are all unimodular, with uniformly distributed root
arguments.  Gilbert--Smyth construct positive-coefficient zero-mean cosine
polynomials that stay negative on long terminal arcs.  These results run in
the opposite direction from a coefficient-sign no-go: positive Fourier
coefficients permit both a full real-root pattern and long negative regions.

They do not construct a legal actual-prime step, because they prescribe the
phase configuration rather than its first Kronecker hitting time.

### Turan--Nazarov

Turan--Nazarov propagates the magnitude of an exponential polynomial from a
measurable subset to an interval with an algebraic exponent equal to its
number of exponential terms minus one.  It neither fixes a sign nor rules
out isolated recurrent chambers.

For generic `Q`-independent nodes, `tau -> r_0(tau)` already contains the full
product

```text
product_(j<=M)cos(tau u_j),                            (6.1)
```

whose signed-subset expansion has `2^M` distinct exponential frequencies.
The Turan--Nazarov exponent is therefore at least `2^M-1` before the other
elementary-symmetric terms are counted.  The metric-span refinement of
Friedland--Yomdin allows discrete norming sets but retains degree/frequency
dependence and does not reverse Theorem 4.1 into a polynomial first-return
lower bound.

### Quantitative Kronecker and linear forms in logarithms

Gonek--Montgomery give strong localized quantitative Kronecker theorems;
Maksimova improves their quantitative version; Korolev--Rezvyakova give an
explicit specialization to logarithms of primes.  These theorems bound an
interval length that is sufficient to **find** every target phase box.  They
do not prove that a specified box is avoided before that length.  Their
published general and prime-log bounds do not furnish a polynomial-in-`Y`
hitting time when the dimension is `M=Y^(1-o(1))`, much less the lower
nonreturn estimate needed here.

Matveev's explicit lower bound applies to integer linear forms in logarithms
of algebraic numbers and has a constant exponential in the number of
logarithms, multiplied by their logarithmic heights.  Eliminating the
continuous `tau` by a direct logarithmic-form argument inherits this severe
growing-dimensional deterioration.  The published estimate therefore does
not yield a fixed-power-in-`Y` separation for this `M`-coordinate phase box
and does not prove (5.6) or (5.7).

### Prime Dirichlet-polynomial large values

Guth--Maynard is the right actual-arithmetic input for counting separated
near-maximal values.  The already-proved packet and dilation-shadow bounds
are a sharp use of that theorem at the required threshold.  A count of
`Y^(2kappa+o(1))` packets is not emptiness, is not a sign theorem, and does not
exclude a one-parameter AP chosen as a function of those packets.

## 7. Primary literature boundary

* G. Elfving,
  [*Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442),
  for the directional convex-hull characterization.
* H. Dette and V. Melas,
  [*Optimal Designs for Estimating Individual Coefficients in Fourier Regression Models*](https://doi.org/10.1214/aos/1065705122),
  for fixed Fourier-regression `c`-optimal designs.
* A. Dubickas,
  [*Some Polynomials with Unimodular Roots*](https://doi.org/10.4134/BKMS.b210728),
  especially Theorems 1.1 and 2.2, for positive coefficients, a full
  unimodular root set, and root-argument equidistribution.
* A. Gilbert and C. Smyth,
  [*Zero-Mean Cosine Polynomials which are Non-Negative for as Long as Possible*](https://doi.org/10.1112/S0024610700001216),
  for positive-coefficient cosine polynomials with extremal long sign arcs.
* A. Barvinok, S. Lee, and I. Novik,
  [*Neighborliness of the Symmetric Moment Curve*](https://arxiv.org/abs/1104.5168),
  for local neighborliness of trigonometric orbitopes.
* F. Nazarov,
  [*Local Estimates for Exponential Polynomials and Their Applications to Inequalities of the Uncertainty Principle Type*](https://www.mathnet.ru/eng/aa397),
  for the measurable Turan--Nazarov inequality.
* O. Friedland and Y. Yomdin,
  [*An Observation on the Turan--Nazarov Inequality*](https://arxiv.org/abs/1107.0039),
  for its metric-span/discrete-set refinement.
* S. Gonek and H. Montgomery,
  [*Kronecker's Approximation Theorem*](https://doi.org/10.1016/j.indag.2016.02.002),
  for localized quantitative hitting theorems.
* D. Maksimova,
  [*A Note on Kronecker's Approximation Theorem*](https://doi.org/10.1016/j.indag.2024.08.002),
  for the later quantitative improvement; it remains an upper hitting-time
  theorem.
* M. Korolev and I. Rezvyakova,
  [*On Simultaneous Approximations to the Logarithms of Primes*](https://doi.org/10.22405/2226-8383-2022-23-5-87-100),
  for an explicit prime-log local Kronecker theorem.
* E. Matveev,
  [*An Explicit Lower Bound for a Homogeneous Rational Linear Form in Logarithms of Algebraic Numbers*](https://www.mathnet.ru/eng/im190),
  for the dimension-dependent logarithmic-form bound.
* L. Guth and J. Maynard,
  [*New Large Value Estimates for Dirichlet Polynomials*](https://arxiv.org/abs/2405.20552),
  for the actual-prime exceptional-packet count.

No result in this list proves a growing-dimensional lower bound for the first
entry of the actual prime-log flow into a prescribed open determinant chamber.

## 8. Exact disposition and next attack

```text
distinct-node first-M r_0=0 interpolation:           INCONSISTENT;
fixed-M near-r_0 singular promotion:                 KILLED;
exact cosine-node collision locus:                   SEPARATE / NOT KILLED HERE;
positive root configurations for every harmonic K:  PROVED;
open positive determinant chambers:                  PROVED;
generic actual-node eventual recurrence:             PROVED;
generic recurrent steps arbitrarily remote:          PROVED;
recurrence before B/M=Y^(17/33+o(1)):                OPEN;
fixed independent additive shift s+k tau:            NOT COVERED HERE;
uniform negative prime-peak exclusion:                OPEN;
determinant signs inside actual negative packets:     OPEN;
QP-PROMOTE:                                           OPEN;
uniform zero-free strip:                              NOT PROVED.
```

The concrete next attack is not another determinant identity.  It is a
sign-sensitive finite-height arithmetic theorem for the actual exceptional
packets:

1. prove (5.6) uniformly on the legal AP dilation shadow; or
2. retain the packets, but prove the augmented determinant has a wrong sign
   throughout every one of their AP preimages; or
3. find one actual preimage and certify its positive augmented solution by
   interval arithmetic, which would promote this AP subroute rather than the
   whole QP theorem.

Average-in-`tau`, almost-everywhere, ordinary Vandermonde, root-distribution,
and recurrence-at-unbounded-height arguments cannot decide this target.

## 9. Replay

```bash
python3 src/test_qp_exceptional_translated_ap_audit.py
python3 results/verify_zeta23_qp_exceptional_translated_ap_audit.py
python3 src/qp_exceptional_translated_ap_audit.py
```
