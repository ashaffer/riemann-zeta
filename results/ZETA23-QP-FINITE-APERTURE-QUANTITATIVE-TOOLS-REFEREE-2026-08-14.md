# QP finite-aperture quantitative-tools referee

**Date:** 2026-08-14  
**Verdict:** no surveyed quantitative recurrence, discrepancy, Littlewood,
mean-value, or generic convex-geometric theorem decides the actual-prime QP
extremal.  There is, however, a sharp logical split and a rigorous metric
benchmark:

1. nonreturn of one harmonic AP kills only that AP construction, not QP;
2. a full QP kill requires a one-sided actual-node dual antenna;
3. quantitative Kronecker and linear-forms estimates are superpolynomial in
   the growing dimension `M=Y^(1-o(1))`;
4. in an independent-node model, every polynomial aperture misses every
   depth-`Y^(-kappa)` positive antipode with probability

   ```text
   1-O((B/r) exp(-c r^2 M)),                            (0.1)
   ```

   which tends to one faster than any power at the QP exponent.

Thus generic geometry predicts **KILL**, very strongly.  Turning that metric
statement into an actual-prime theorem is exactly the unproved arithmetic
step.  Neither (0.1) nor any literature result below proves QP-KILL,
QP-PROMOTE, or a zeta strip.

---

## 1. The three statements that must not be conflated

For actual absolute prime-log nodes `u_1,...,u_M`, put

```text
a(t)=(cos(t u_j))_(j<=M),       q_0=(1,...,1).          (1.1)
```

### 1.1 Full positive QP

On a legal high band `H`, define

```text
C_+(H)=inf {mu(H): mu>=0, integral_H a(t)dmu(t)=-q_0},
r_+(H)=1/C_+(H).                                       (1.2)
```

The promotion target is

```text
r_+(H)>=Y^(-kappa_promote+eta),
kappa_promote=.0180303234...,                           (1.3)
```

for some fixed `eta>0`, together with the already audited compact-state
adapter required by the surrounding construction.

Continuous linear-programming duality gives the exact identity

```text
C_+(H)=sup {q_0 dot y:
            y dot a(t)>=-1 for every t in H}.           (1.4)
```

Consequently the weakest normalized full positive-KILL certificate is

```text
q_0 dot y=1,
inf_(t in H) y dot a(t)>=-Y^(-c+o(1)),
c>kappa_promote.                                       (1.5)
```

Indeed, pairing (1.5) with a depth-`r` antipode gives
`-r>=-Y^(-c+o(1))`.

For the original signed low/high QP extremal, (1.5) alone is not enough.
One needs a hybrid antenna which also approximates the low carrier.  In the
normalization of the existing reports, a uniform exponent
`c>kappa_max=.0187463697...` closes that architecture-wide dual route.
Here `kappa_max` and the convenient auxiliary target `c=.019` are calibrated
only at the active fixed value `d=33/50` (so `B=Y^(50/33)`).  They are not a
uniform certificate over a varying `d`-family; changing `d` requires
recomputing both the carrier maximum and every deletion margin.

### 1.2 Harmonic-AP promotion

For an `M`-set of integer harmonics `K`, an AP certificate has atoms

```text
{k tau:k in K}.                                        (1.6)
```

The sparse positive-cosine theorem constructs open phase chambers for every
`K` and every subunit depth.  Entry of

```text
tau ->(tau u_1,...,tau u_M) mod 2pi                    (1.7)
```

into one such chamber before the support reaches the upper aperture is a
sufficient QP promotion.

### 1.3 AP nonreturn is not full QP-KILL

An extreme solution of (1.2) uses at most `M` atoms, but those atoms are
arbitrary real frequencies.  They need not be integer multiples of one
common step.  Therefore

```text
one AP enters a chamber:             sufficient PROMOTE;
every AP misses its chamber:         AP subroute killed;
dual certificate (1.5):              full positive QP killed.   (1.8)
```

The reverse implication in the middle line is false without a new
commensurability theorem.  This is the first required scope correction.

### 1.4 Spectral-null atom equivalence

There is an exact and useful reformulation.  Symmetrize a probability
measure `nu` on `H` to an even probability on `+/-H`.  Then

```text
integral cos(tu_j)dnu(t)=-r       for every j          (1.9)
```

if and only if

```text
sigma=[r delta_0+nu]/(1+r)                            (1.10)
```

is an even probability on `{0} union +/-H` satisfying

```text
hat sigma(u_j)=0                         for every j,
sigma({0})=r/(1+r).                                    (1.11)
```

Conversely, remove an atom of mass `alpha` at zero from a spectral-null
probability and renormalize the remainder.  Its common cosine moment is

```text
-alpha/(1-alpha).                                     (1.12)
```

Thus positive QP asks how large an atom at zero can be hidden inside a
positive measure having the prescribed prime-log spectral nulls.

A literal zero node would of course kill the positive problem immediately:
if the shell centre equalled one active prime power, that coordinate of
every `a(t)` would be `1`.  This is not a free recentering in the current
candidate architecture.  The centre is fixed as `Y=X^d` by the selected
candidate/saddle and compact carrier construction.  Moving it to a nearby
prime using the unconditional `O(Y^(21/40))` prime-gap scale changes a log
node by as much as `Y^(-19/40)`; at the top aperture the resulting phase
change is

```text
B Y^(-19/40)=Y^(50/33-19/40)=Y^(1373/1320),           (1.12a)
```

so it is emphatically not a uniform perturbation of the QP curve.  The prior
signed-height-filter audit explicitly leaves absorption of even a chosen
centre perturbation into the deterministic divisor/compact-state
construction unproved.  Hence a prime-centred zero coordinate kills a
different recentered model, not the candidate-tuned QP extremal audited
here.

Because zero is isolated from `+/-H`, the corresponding measure LP has the
following exact Delsarte dual.  The maximum central mass is the infimum of
`c` over real `z_1,...,z_M` such that

```text
F(t)=c+sum_j z_j cos(tu_j),
F(0)>=1,
F(t)>=0                    for every t in +/-H.         (1.13)
```

This is ordinary strong duality for a compact moment problem: integrate
(1.13) against `sigma` for weak duality, and separate the compact moment
cone for equality.

The normalized antenna (1.5) is exactly a Delsarte certificate.  If
`sum_j lambda_j=1` and

```text
P_lambda(t)=sum_j lambda_j cos(tu_j)>=-epsilon
                                                   on H, (1.14)
```

then

```text
F(t)=[epsilon+P_lambda(t)]/(1+epsilon)                 (1.15)
```

is admissible in (1.13), so

```text
alpha<=epsilon/(1+epsilon),       r<=epsilon.          (1.16)
```

The coefficients `lambda_j` may be signed in the exact LP.  Requiring them
to be nonnegative is a useful stronger hypothesis: `P_lambda` is then a
normalized positive-definite cosine transform of a probability on the
spectral nodes.  The metric tent theorem below constructs a certificate in
this stronger class.

---

## 2. Quantitative Kronecker: definitive scale mismatch

Qualitative Kronecker--Weyl recurrence applies when the nodes are rationally
independent.  It has no uniform first-return content.

The current sharp localized quantitative results have the following form.
Maksimova's transference theorem uses

```text
gamma=2^(M-2)/[M(M!)^2],
T_*=1/(gamma delta),                                   (2.1)
```

provided every nonzero bounded integer combination of the frequencies is at
least `delta`; the coefficient box itself has side comparable with
`1/(gamma epsilon)`.  Thus the displayed constant is already factorial in
`M`, before estimating `delta`.

For logarithms of algebraic numbers, Matveev's lower bound is exponential
in the number of logarithms and contains the product of their logarithmic
heights.  With `M=Y^(1-o(1))` primes of height `asymp log Y`, inserting this
bound into a localized Kronecker theorem is far beyond every fixed power of
`Y`.  It cannot reach

```text
tau<=B/M=Y^(17/33+o(1)).                               (2.2)
```

The direction also matters.  Quantitative Kronecker theorems give a time
large enough to guarantee a hit.  They do not prove that a specified chamber
is avoided before a shorter time.

There is a general obstruction to extracting a bound from rational
independence alone.  Fix a target open set `U` and a rational frequency
vector whose periodic orbit avoids the closure of `U`.  For every prescribed
finite `T`, all sufficiently close frequency vectors also avoid `U` through
time `T`; rationally independent vectors are dense among them.  Hence no
finite first-hit bound can depend only on dimension, chamber radius, and
rational independence.

Primary comparisons:

- [Gonek--Montgomery, *Kronecker's Approximation Theorem*](https://doi.org/10.1016/j.indag.2016.02.002);
- [Maksimova, *A Note on Kronecker's Approximation Theorem*](https://arxiv.org/abs/2405.07051), especially Theorem 1 and (2.1);
- [Korolev--Rezvyakova, simultaneous approximation to logarithms of primes](https://www.mathnet.ru/eng/cheb1257);
- [Matveev, explicit logarithmic-form lower bounds](https://www.mathnet.ru/eng/im314).

None has polynomial dependence in the present growing dimension.

---

## 3. Discrepancy has the same denominator

Applying Erdos--Turan--Koksma to (1.7) produces terms

```text
min(1,1/[T |h dot u|])                                 (3.1)
```

for integer vectors `h` in a growing coefficient box.  For prime logarithms,
`h dot u` is a logarithm of a ratio of large prime products, with an
additional `log Y` term when absolute values cross the shell center.
Unique factorization proves nonvanishing in the appropriate generic shell;
it does not give a polynomial lower bound.  Matveev returns the same
dimension loss as Section 2.

Low discrepancy would in any case have to beat the Haar volume of a positive
chamber.  A phase box of coordinate radius `rho` has volume `asymp rho^M`.
Even for inverse-polynomial `rho`, this is

```text
exp[-Theta(M log M)],                                  (3.2)
```

whereas the legal orbit length is polynomial in `Y`.  Discrepancy is useful
only if the union of favorable chambers has much larger structured measure;
no surveyed theorem proves such a statement for the positive determinant
signs.

Metric discrepancy and almost-everywhere results cannot settle a pointwise
actual-prime problem.  A single exceptional hit suffices for promotion.

---

## 4. Rigorous metric finite-aperture no-hit theorems

The random-polytope prior can be made theorem-grade without assuming
independent orbit samples.  In fact, a data-dependent positive dual antenna
gives the full statement on the entire band.

### Theorem 4.1 (independent-node full-band tent antenna)

Let `U_1,...,U_M` be independent and uniform on `[-w,w]`.  Put

```text
g(u)=1-|u|/w,
y_j=g(U_j)/sum_l g(U_l),
P_M(t)=sum_j y_j cos(tU_j).                             (4.1)
```

For `0<epsilon<=1/8` and `B>=1`,

```text
P{inf_(0<=t<=B) P_M(t)<-(8/3)epsilon}
 <=2(2+4wB/epsilon) exp(-M epsilon^2/8).                (4.2)
```

On the complementary event, `y dot q_0=1` and

```text
inf_(0<=t<=B)y dot a(t)>=-(8/3)epsilon.                (4.3)
```

Thus (4.3) is the exact full positive-QP dual certificate (1.5), valid
simultaneously for every atom in the continuum.  Every positive antipode in
`[0,B]` has depth at most `(8/3)epsilon`.

#### Proof

Set

```text
A_M(t)=M^(-1)sum_j g(U_j)cos(tU_j),
A(t)=E[g(U)cos(tU)].                                   (4.4)
```

The normalized population transform is exactly

```text
A(t)/A(0)=2[1-cos(wt)]/(w^2t^2)
          =[sin(wt/2)/(wt/2)]^2>=0.                   (4.5)
```

Both `A_M` and `A` are `w`-Lipschitz.  Take a grid of mesh at most
`epsilon/(4w)`, including both endpoints.  At each grid point Hoeffding's
inequality gives

```text
P{|A_M-A|>epsilon/2}<=2 exp(-M epsilon^2/8).
```

There are at most `2+4wB/epsilon` grid points.  The Lipschitz estimate and a
union bound therefore give

```text
sup_(0<=t<=B)|A_M(t)-A(t)|<=epsilon                    (4.6)
```

outside the set displayed in (4.2).  Since the grid includes zero, the same
event gives `A_M(0)>=A(0)-epsilon>=3/8`.  Since `A(t)>=0`,

```text
P_M(t)=A_M(t)/A_M(0)>=-(8/3)epsilon.                   (4.7)
```

uniformly on the band.  This proves (4.2)--(4.3).  Pairing (4.3) with a
positive antipode proves the depth assertion.  QED

The same proof works for independent nodes with a density bounded above and
below on the shell: importance-weight by the reciprocal density times the
tent.  Uniformity is used only to display the exact nonnegative transform
(4.5).

Taking `epsilon` a sufficiently small constant multiple of
`r=Y^(-kappa+eta)`, with the scales in (4.13) below, makes the exceptional
probability

```text
exp[-Y^(1-2kappa+2eta-o(1))].                          (4.8)
```

This is a full-band and fully adaptive metric KILL theorem.  The dual
weights depend on the sampled nodes, just as an actual-node antenna is
allowed to do.

### Theorem 4.2 (general characteristic-function benchmark)

Let `U_1,...,U_M` be independent, identically distributed random variables
supported in `[0,w]` and
put

```text
S(t)=sum_(j<=M) cos(t U_j).                             (4.9)
```

Let `H=[T_0,B]`, `0<r<1`, and suppose

```text
sup_(t in H)|E cos(t U_1)|<=r/4.                       (4.10)
```

Then, for an absolute `c>0`,

```text
P{there is a probability nu on H with
   integral a(t)dnu(t)=-r' q_0 for some r'>=r}
 <=(2+8wB/r) exp(-c r^2 M).                            (4.11)
```

The measure in (4.11) is arbitrary: it may be continuous, atomic,
incommensurable, or adaptively chosen after seeing the nodes.  Thus (4.11) is
a full positive-QP statement for the indicated random-node band, not merely
an AP statement.

#### Proof

Any antipode of depth `r'>=r` satisfies

```text
integral_H S(t)dnu(t)=-r'M,
```

so some `t in H` has `S(t)<=-rM`.

The deterministic derivative bound is

```text
|S'(t)|<=wM.                                           (4.12)
```

Use a grid of mesh `r/(4w)`.  If the preceding negative peak exists, a grid
point `s` has `S(s)<=-3rM/4`.  By (4.10),

```text
E S(s)>=-rM/4.
```

Hoeffding's inequality for the independent variables
`cos(sU_j) in [-1,1]` gives

```text
P{S(s)<=-3rM/4}<=exp(-c r^2M).
```

There are at most `2+8wB/r` grid points after harmless endpoint rounding.
The union bound proves (4.11).  QED

For uniform nodes on `[0,w]`,

```text
|E cos(tU)|=|sin(wt)/(wt)|<=1/(wt),
```

so (4.10) holds once `T_0>=4/(wr)`.  In particular it holds on the all-remote
AP band `t>=M` whenever `rM -> infinity`.

At the audited QP scales

```text
M=Y^(1-o(1)),       B=Y^(50/33+o(1)),
r=Y^(-kappa+eta),   kappa=.0180303234...,              (4.13)
```

the exponent in (4.11) is

```text
r^2M=Y^(1-2kappa+2eta-o(1)).                           (4.14)
```

while the prefactor has only logarithmic size on the log scale.  Hence the
failure probability is `exp[-Y^(.9639...+o(1))]` at `eta=0`.

This proves that a polynomial first hit is fantastically nongeneric.  It
does **not** permit replacing actual prime logs by independent nodes.  The
actual theorem must therefore detect a deterministic arithmetic coherence
which the model omits, or prove that no such coherence occurs.

### 4.3 The sharp deterministic hypothesis suggested by the model

For a deterministic node vector define, for probability weights
`lambda=(lambda_j)`,

```text
P_lambda(t)=sum_j lambda_j cos(tu_j).                  (4.15)
```

The precise positive-coefficient replacement for Theorem 4.1 is

```text
lambda_j>=0,                 sum_j lambda_j=1,
inf_(t in H)P_lambda(t)>=-Y^(-c+o(1)),
c>kappa_promote.                                      (DPA_c)
```

By (1.14)--(1.16), `(DPA_c)` rules out every positive antipode at the
promotion depth.  It is uniform over arbitrary continuous or atomic
cancellation measures and therefore is a full positive-QP KILL, not an AP
nonreturn statement.

An easier but stronger deterministic target mirrors the proof exactly.  Let

```text
Phi_w(t)=[sin(wt/2)/(wt/2)]^2>=0.                     (4.16)
```

It suffices to construct positive actual-node quadrature weights satisfying

```text
sup_(t in H)|P_lambda(t)-Phi_w(t)|<=Y^(-c+o(1)).       (4.17)
```

The current diffuse prime quadrature proves the required low-band
approximation and a fourth-moment exceptional-set estimate on the high band.
It does not prove either the one-sided pointwise statement `(DPA_c)` or the
two-sided statement (4.17).  The exceptional high-denominator peaks are the
entire deterministic gap between the metric theorem and actual primes.

The exact signed Delsarte LP permits signed `lambda_j`; positivity in
`(DPA_c)` is an additional convenience, not a logical necessity.  For the
full signed low/high QP extremal one must additionally approximate the low
carrier, as recorded after (1.5).

---

## 5. Littlewood, Riesz products, and off-diagonal moments

Qualitative Sidon/Kronecker interpolation takes place on the full compact
dual group.  It places no bound on the real character parameter `t`.
The distinction is explicit in the definitions used by
[Hare--Ramsey](https://arxiv.org/abs/1506.07389): an epsilon-Kronecker set
permits an arbitrary character of the compact group, not a character from a
fixed polynomial segment of one real orbit.

The natural prime Riesz product gives the desired common negative first
moment on the unrestricted torus.  Its useful Fourier degree is of order

```text
r^2M.                                                   (5.1)
```

At (4.13), this is a fixed power close to `Y^.964`, not a bounded degree.
Transferring it to a finite real orbit requires control of prime-product
near-relations at those degrees.

Ordinary Dirichlet-polynomial moments stop at the conductor transition.  If

```text
S_Y(t)=sum_(p in shell) exp(it log(p/Y)),
```

then the `2q`-th moment sees products of `q` shell primes and conductor
`Y^q`.  Montgomery--Vaughan mean values plus the derivative conversion give
normalized exponent

```text
[max(50/33,q)-q]/(2q+1)>=0.                            (5.2)
```

for every `q`.  Growing `q` worsens the factorial and logarithmic factors.
The relevant primary inputs are
[Montgomery--Vaughan's Hilbert inequality](https://doi.org/10.1112/jlms/s2-8.1.73)
and the modern actual-prime large-value theorem of
[Guth--Maynard](https://arxiv.org/abs/2405.20552).

Guth--Maynard compresses the values with
`|S_Y(t)|>=rM` into `r^(-2)Y^o(1)` packets.  This is a count, not emptiness;
it loses the negative sign and allows a positive measure to concentrate on
all exceptional packets.  Pair-energy and weighted BSG can extract a small
approximate-group component, but do not preserve the carrier identity or
return the whole measure.  Exact countermodels in the existing pair-energy
audit saturate those losses.

Resonance methods and large-value theorems prove that selected Dirichlet
polynomials can have large values.  They do not simultaneously prescribe
the `M=Y^(1-o(1))` shell-prime phases inside a height `Y^O(1)` and do not
produce the directional positive determinant signs.

### 5.1 Turan and Delsarte have the wrong supplied datum

The tent in Theorem 4.1 is not accidental.  It is the interval
autocorrelation

```text
g=1_[-w/2,w/2]*1_[-w/2,w/2]/w,                        (5.3)
```

and its Fourier transform is the nonnegative Fejer/sinc-squared kernel.
Classical Turan theory identifies this continuous positive-definite
extremizer for an interval.  See
[Kolountzakis--Revesz](https://arxiv.org/abs/math/0204086) and their
[LCA-group formulation](https://arxiv.org/abs/math/0312218).

That theorem supplies the **continuous spectral density** `g(u)du`.  QP
needs a positive quadrature for it supported on the prescribed discrete
prime-log nodes and uniformly accurate through `B`.  No Turan theorem in
the cited framework provides that discretization.

The standard Delsarte extremal problem similarly optimizes a
positive-definite function under a spatial support condition and a global
sign restriction.  Our exact dual (1.13) instead pins the spectrum to the
actual finite prime-log set and asks for one-sided nonnegativity only on the
remote band.  Calling (1.13) a Delsarte LP is useful—the duality and central
atom interpretation are exact—but it does not import an extremal value from
the classical support problem.

The closest probability-Fourier extremal result I found is
[Luo--Zhang](https://www.numdam.org/articles/10.1016/j.crma.2005.07.021/),
which constrains a characteristic function to vanish at **one fixed point**.
That is not a many-zero theorem on a prescribed, growing prime-log set, and
it has neither our off-central support restriction nor our central-atom
objective.  Likewise, the spectral-gap theory of
[Poltoratski](https://arxiv.org/abs/0908.2079) starts with a measure whose
Fourier transform vanishes on an interval and asks how support density
permits such a gap.  Our datum is only finitely many prescribed zeros while
the measure support is restricted to `{0} union (+/-H)`; neither direction
of that spectral-gap theorem supplies the missing positive quadrature.

Turan--Nazarov is also insufficient.  For an `n`-term exponential
polynomial it propagates a modulus bound from a measurable subset `E` to an
interval `I` with a factor of the form

```text
(A |I|/|E|)^(n-1).                                    (5.4)
```

Here `n=M=Y^(1-o(1))`, so even a fixed-ratio propagation costs
`exp(Theta(M))`.  More importantly, it propagates absolute magnitude, not a
lower sign bound.  It cannot turn the proved small exceptional-set estimate
into `(DPA_c)`.  The primary local estimate is
[Nazarov](https://www.mathnet.ru/eng/aa397).

### 5.2 Nonharmonic Fourier inequalities stop at `L2`

Ingham--Beurling and Montgomery--Vaughan inequalities control

```text
integral_I |sum_j c_j exp(iu_jt)|^2dt                 (5.5)
```

from coefficient `l2` norms, under separation or Beurling-density
hypotheses.  They do not construct probability coefficients with the
one-sided pointwise property `(DPA_c)`.  Even an ideal frame estimate leaves
isolated negative spikes, exactly the quantifier that QP cannot tolerate.

The basic uniform-gap hypothesis also fails at the audited aperture for the
absolute prime-log nodes.  Nodes on the same side of the shell have gaps
`gg1/Y`, but an opposite-side pair has separation

```text
||log(p/Y)|-|log(q/Y)||=|log(pq/Y^2)|.                 (5.6)
```

For integral `Y`, the elementary worst-case scale is only `gg Y^-2`; for a
general real shell center it can be arbitrarily smaller.  A uniform-gap
Ingham lower frame bound then asks for an observation interval of order
`Y^2`, while

```text
B=Y^(50/33+o(1))=o(Y^2).                               (5.7)
```

Quotienting near-collisions can improve conditioning because the target
moments agree, but it still returns an `L2` frame statement rather than
(4.15).  The already-proved fourth-moment packet theorem is stronger for
the present polarity and still allows exceptional atoms.

Primary nonharmonic comparisons are
[Seip's survey](https://emis.de/journals/DMJDMV/xvol-icm/08/Seip.MAN.html)
and the explicit
[Ingham--Beurling estimates](https://arxiv.org/abs/0808.2255).  Neither
contains prescribed positive quadrature, a pointwise lower sign, or
actual-prime high-denominator control.

---

## 6. Convex geometry: what is complete and what is not

The finite geometry is complete:

- at most `M` atoms suffice at an extremal boundary point;
- generically exactly `M` are necessary and the optimum is unique;
- every prescribed harmonic `M`-support has open positive chambers;
- the continuous problem has the exact one-sided dual (1.4).

None supplies a finite-height theorem.  Caratheodory and Elfving reduce the
number of atoms after feasibility is known; they do not locate those atoms.
Generic full spark rules out support compression; it does not bound Cramer
signs or the first legal aperture.

The metric Theorem 4.1 is consistent with the usual random-polytope scale

```text
r_random about sqrt(log N/M)                           (6.1)
```

for `N` polynomially many effective orbit samples.  The desired
`r=Y^(-.018...)` is enormously larger than (6.1).  This is a prior and a
metric theorem, not an actual-prime substitution.

---

## 7. Weakest honest closure lemmas

There are four distinct binary targets.

### AP-PROMOTE

Exhibit one `K`, one legal `tau<=B/max K`, and strict weights with

```text
sum_(k in K)w_k a(k tau)=-r q_0,
r>=Y^(-kappa_promote+eta).                             (7.1)
```

An interval-certified Cramer-sign certificate at every sufficiently large
`Y` would suffice.

### AP-KILL

Prove that every legal harmonic support misses the positive Cramer chambers.
This closes only the commensurable construction.

### Full positive-QP KILL

Prove (1.5) with `c>kappa_promote`.  A uniform negative-peak estimate for
the unweighted prime sum is one sufficient choice `y=q_0/M`, but a uniform
power estimate of that type is already adjacent to fixed-strip prime-sum
technology.  An adaptive actual-node antenna could be weaker and remains
the highest-probability honest route.

### Full signed-QP KILL

Construct the same antenna while approximating the low carrier, with an
exponent exceeding the audited architecture-wide maximum.  This is the
actual theorem needed to close the whole low/high QP branch.

No primary theorem surveyed supplies any of these four statements for the
actual growing prime-log system.

---

## 8. Final disposition

```text
qualitative eventual AP recurrence:                  PROVED;
polynomial quantitative recurrence from Q-independence: IMPOSSIBLE;
published quantitative prime-log Kronecker at M~Y:   FAR TOO LARGE;
ordinary discrepancy/linear forms:                   SAME LOSS;
fixed-order Littlewood/mean-value transfer:           CONDUCTOR-CRITICAL;
generic polynomial-aperture positive QP at target r:  KILLED METRICALLY;
actual-prime AP first hit/nonreturn:                   OPEN;
actual-prime full positive-QP dual antenna:            OPEN;
actual-prime full signed low/high antenna:             OPEN;
QP-PROMOTE / QP-KILL / zeta strip:                    NOT PROVED.
```

The fail-fast conclusion is strong: another generic Kronecker, discrepancy,
Riesz-product, random-polytope, or Caratheodory argument cannot close the
gate.  A successful proof must be an actual-prime, finite-height directional
theorem—most plausibly an adaptive one-sided antenna on the exceptional
large-value packets—or an explicit certified promoter.

---

## 9. Replay

The finite checker independently replays the sinc-squared tent transform,
the exact continuum probability constant, the metric exponent, the
spectral-null atom conversion, and the rational `.019` auxiliary margins:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_finite_aperture_referee.py
PYTHONPATH=src python3 src/qp_finite_aperture_referee.py
```

These checks verify the algebraic and probability identities in the report;
they do not assert the missing deterministic actual-prime antenna.
