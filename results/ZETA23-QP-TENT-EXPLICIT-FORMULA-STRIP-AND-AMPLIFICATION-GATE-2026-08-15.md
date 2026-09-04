# QP tent/explicit-formula theorem and amplification gate

**Date:** 2026-08-15  
**Verdict:** there is a new unconditional actual-prime Delsarte bound, but it
is subpower and does **not** close QP.  A fixed zero-free strip of width
`delta` gives the missing fixed-power certificate at every exponent
`c<delta`.  On the audited `d=33/50` slice, a strip wider than

```text
kappa_max=.018746369714728765...                       (0.1)
```

would therefore kill positive QP; width `.019` itself gives every exponent
strictly below `.019`, while any width greater than `.019` gives the cached
convenient `.019` certificate.

Unconditionally, the Vinogradov--Korobov zero-free region and one explicit
positive tent on the **actual prime-power nodes** give

```text
P_Y(t)>=-exp[-c_A (log Y/log log Y)^(1/3)]
          for every |t|<=Y^A,                         (0.2)

A_H>=exp[c_A (log Y/log log Y)^(1/3)],
r_+(H)<=exp[-c_A (log Y/log log Y)^(1/3)].            (0.3)
```

Here `A>0` is fixed and `c_A>0`; constants may change between occurrences.
Thus (0.2) covers the complete QP aperture `A=50/33`, improves the natural
KMT logarithmic antenna, and is a genuine all-height actual-node theorem.
It remains `Y^(-o(1))`, whereas QP needs `Y^(-c)` for a fixed
`c>kappa_max`.

The obvious amplification mechanisms have exact obstructions:

1. convex mixing of disjoint subshells **averages** their errors;
2. products and nonlinear powers would multiply gains, but leave the finite
   actual-node cosine span by generating sum/difference log frequencies;
3. every nonnegative real positive-definite shell kernel gives a resonant
   zero at least its full normalized mass, so kernel convolution, products,
   or multiscale smoothing cannot turn the VK zero exponent into a fixed
   exponent term by term;
4. sequential positive reweighting is exactly one final point of the same
   node simplex.

Consequently the surviving unconditional route is not positivity or scale
iteration.  It is a genuinely coefficient-sensitive cancellation theorem for
the adaptive actual-prime cross-error (equivalently the original one-sided
Delsarte/convex-hull gate).  No such theorem is proved here.  No uniform
zero-free strip is proved.

---

## 1. Actual-node setup and polarity

Fix `w=1/5` and a half-integer center `Y=N+1/2`.  For every prime power in
the shell, put

```text
u(n)=log(n/Y),                 |u(n)|<w.              (1.1)
```

After identifying equal absolute values, these give the distinct nonzero QP
coordinates `u_j=|u(n)|`.  A normalized positive actual-node antenna is

```text
P_lambda(t)=sum_j lambda_j cos(t u_j),
lambda_j>=0,                  sum_j lambda_j=1.       (1.2)
```

If `P_lambda(t)>=-epsilon` on the complete high band `H`, then

```text
Q(t)=1+P_lambda(t)/epsilon>=0,
Q(0)=1+1/epsilon.                                    (1.3)
```

Therefore

```text
A_H>=1+1/epsilon,             r_+(H)<=epsilon.        (1.4)
```

This is a sufficient positive-coefficient certificate for the exact signed
Delsarte value.  All exponent polarities below follow from (1.4).

---

## 2. The tent has a nonnegative pole transform

Take the fixed tent

```text
g_w(u)=(1-|u|/w)_+.                                  (2.1)
```

Its bilateral Laplace transform is entire and equals

```text
F_w(z)=int_R g_w(u)e^(zu)du
      =2[cosh(wz)-1]/(w z^2),       F_w(0)=w.         (2.2)
```

On the imaginary axis,

```text
F_w(-it)=w [sin(wt/2)/(wt/2)]^2>=0.                  (2.3)
```

Thus the pole/main term has the required sign at every height, not only on
average.  This is the continuous Turan/Fejer fact, but the next theorem
transfers it to the prescribed arithmetic nodes rather than replacing those
nodes by a continuum.

Define the finite actual-prime sum

```text
S_Y(t)=sum_n Lambda(n)/n * g_w(log(n/Y))
                       * exp[-it log(n/Y)].           (2.4)
```

The sum is automatically over prime powers in the shell.  Its mass is
`W_Y=S_Y(0)>0` for large `Y`.  Aggregate the positive weights

```text
omega_n=Lambda(n)g_w(log(n/Y))/n                     (2.5)
```

at equal absolute nodes and divide by `W_Y`.  Then the resulting legal
antenna satisfies

```text
P_Y(t)=Re S_Y(t)/W_Y.                                (2.6)
```

---

## 3. Exact explicit formula for the tent antenna

### Theorem 3.1 (uniform shell explicit formula)

Uniformly for real `t`,

```text
S_Y(t)=F_w(-it)
       -sum_rho Y^(rho-1) F_w(rho-1-it)
       +O_w(Y^(-3/2) log(2+|t|)),                    (3.1)
```

where the sum counts every nontrivial zeta zero with multiplicity and is
absolutely convergent.

#### Proof

For any `a>0`, bilateral Mellin inversion and the absolutely convergent
Dirichlet series for `-zeta'/zeta` give

```text
S_Y(t)=1/(2 pi i) int_(Re s=a)
       F_w(s-it)Y^s[-zeta'/zeta(1+s)]ds.             (3.2)
```

Shift to `Re s=-3/2`, along a standard sequence of horizontal edges avoiding
zero ordinates.  The pole of zeta at `1` makes `-zeta'/zeta(1+s)` have
residue `+1` at `s=0`, giving `F_w(-it)`.  A nontrivial zero `rho` gives a
pole of residue `-m_rho` at `s=rho-1`, giving the zero sum in (3.1).  The
first trivial-zero pole is at `s=-3`, so none is crossed.

For `-3/2<=sigma<=0`, (2.2) gives

```text
|F_w(sigma+i v)|<=C_w/(1+v^2).                       (3.3)
```

On `Re(1+s)=-1/2`, the functional equation and the absolutely convergent
series at the reflected line `3/2` give

```text
|zeta'/zeta(-1/2+i v)|<<log(2+|v|).                  (3.4)
```

Equations (3.3)--(3.4) bound the new vertical integral by the remainder in
(3.1) and make the horizontal integrals vanish.  Finally, the local
Riemann--von Mangoldt estimate

```text
N(T+1)-N(T)<<log(2+T)                                (3.5)
```

and (3.3) show

```text
sum_rho (1+|gamma-t|)^(-2)<<log(2+|t|),              (3.6)
```

so the zero sum is absolutely convergent.  QED

This proof retains the full oscillatory height `t`: unlike partial summation
from a PNT error, it loses no factor `|t|`.
The contour template was cross-checked against the general smoothed explicit
formula in Helfgott,
[*The ternary Goldbach problem*](https://arxiv.org/abs/1501.05438),
Lemma 9.1.1; (3.1) is the simpler compact log-shell specialization with the
line stopped before the first trivial zero.

---

## 4. A fixed strip gives a fixed-power actual-node certificate

### Theorem 4.1 (strip-to-Delsarte transfer)

Assume, for some fixed `0<delta<=1/2`,

```text
zeta(s)!=0                   when Re s>1-delta.       (4.1)
```

For every fixed `A>0`, the weights (2.5) satisfy

```text
P_Y(t)>=-C_(A,w,delta) Y^(-delta)log Y
                  for every |t|<=Y^A.                (4.2)
```

Consequently, for every `c<delta` and all sufficiently large `Y`,

```text
P_Y(t)>=-Y^(-c),
A_H>=1+Y^c,
r_+(H)<=Y^(-c).                                      (4.3)
```

#### Proof

Every zero in (3.1) has `beta<=1-delta`.  By (3.3) and (3.6),

```text
|sum_rho Y^(rho-1)F_w(rho-1-it)|
 <=C_w Y^(-delta)log(2+|t|).                         (4.4)
```

At `t=0`, (3.1) therefore gives

```text
W_Y=w+O(Y^(-delta)),                                 (4.5)
```

so `W_Y>=w/2` for large `Y`.  The main term (2.3) is real and nonnegative.
Taking real parts in (3.1), dividing by (4.5), and using
`log(2+|t|)<<_A log Y` proves (4.2).  If `c<delta`, the logarithm and fixed
constant are eventually smaller than `Y^(delta-c)`, proving (4.3) via
(1.3)--(1.4).  QED

### Exact QP threshold

On the fixed `d=33/50` slice, the audited bill is

```text
kappa_min=.018030323424358778...,
kappa_max=.018746369714728765....                    (4.6)
```

Theorem 4.1 kills this slice if

```text
delta>kappa_max.                                     (4.7)
```

For the cached convenient choice `c=.019`, the theorem requires the strict
inequality `delta>.019`.  A strip of width exactly `.019` supplies every
`c<.019`, which is already enough for (4.7), but not the literal endpoint
`c=.019` after the logarithmic loss.

This is conditional.  It does not construct (4.1), and using (4.1) as an
input to prove a strip would be circular.

---

## 5. Unconditional VK actual-node theorem

The explicit Vinogradov--Korobov region has the shape

```text
beta<=1-c_0/[(log(2+|gamma|))^(2/3)
             (log log(3+|gamma|))^(1/3)].            (5.1)
```

A checked explicit primary version is Bellotti,
[*Explicit bounds for the Riemann zeta function and a new zero-free region*](https://arxiv.org/abs/2306.10680),
which proves this shape for every `|gamma|>=3`.  The later classical region
of Bellotti--Trudgian--Yang,
[*Zero-free regions inspired by work of Heath-Brown*](https://arxiv.org/abs/2603.21490),
improves the finite-height `1/log t` constant but does not replace the wider
VK shape asymptotically.

### Theorem 5.1 (unconditional subpower Delsarte certificate)

For every fixed `A>0`, there is `c_A>0` such that the actual weights (2.5)
obey (0.2)--(0.3) for all sufficiently large `Y`.

#### Proof

Choose fixed `D>A+2` and split the zero sum in (3.1) at `|gamma|=Y^D`.
For `3<=|gamma|<=Y^D`, (5.1) gives

```text
Y^(beta-1)
 <=exp[-c_D (log Y)^(1/3)(log log Y)^(-1/3)].        (5.2)
```

The finitely many lower zeros have a fixed positive distance from `Re s=1`
and contribute a power-smaller term.  Equation (3.6) controls the remaining
kernel sum by `O(log Y)`.  For `|gamma|>Y^D` and `|t|<=Y^A`, (3.3) and the
zero count give

```text
sum_(|gamma|>Y^D)|F_w(rho-1-it)|
 <<Y^(-D)log Y.                                      (5.3)
```

Absorb the logarithm in a smaller `c_A`, use the nonnegative main term, and
normalize as in (4.5).  Equations (1.3)--(1.4) give (0.3).  QED

The exponent in (0.2) is `o(log Y)`.  Therefore (0.2) is smaller than every
fixed inverse logarithm but larger than `Y^(-c)` for every fixed `c>0` once
`Y` is sufficiently large.  It is a substantive QP bound, not QP closure.

---

## 6. Exact failure of positivity/scale amplification

### Proposition 6.1 (convex subshells only average)

Suppose positive antennas on any collection of disjoint or overlapping
actual-node subsets satisfy

```text
P_k(t)>=-epsilon_k,          P_k(0)=1.                (6.1)
```

For `theta_k>=0`, `sum theta_k=1`, their mixture has only the black-box bound

```text
sum_k theta_k P_k(t)>=-sum_k theta_k epsilon_k.       (6.2)
```

The weighted error in (6.2) is at least `min_k epsilon_k`, so mixing cannot
improve on the best constituent.  Equivalently,
convexly combining the normalized Delsarte polynomials averages their values
at zero and cannot exceed the best constituent.  Disjoint subshells do not
multiply the gain.

### Proposition 6.2 (the actual-node cosine span is not an algebra)

Let `U` be any finite nonempty set of positive frequencies and

```text
V_U=span_R{1,cos(ut):u in U}.                         (6.3)
```

If `u_* = max U`, then

```text
cos^2(u_*t)=[1+cos(2u_*t)]/2 notin V_U.              (6.4)
```

Indeed `2u_*>u_*`, and distinct real exponential frequencies are linearly
independent.  More generally, if a polynomial antenna has nonzero top
frequency `u_*`, every genuine degree-`k>=2` pointwise polynomial in it has
the nonzero harmonic `k u_*`.

Thus the tempting amplifier

```text
Q(t)>=0  --->  Q(t)^k>=0,       Q(0)^k              (6.5)
```

is illegal even before accounting for the normalization of the new constant
coefficient: its spectrum contains sums and differences of prime-log nodes,
not the prescribed prime-power log nodes.  For bulk primes these are
semiprime/ratio frequencies.  If one uses several disjoint seed factors to
keep the product's constant coefficient equal to one, its value at zero can
indeed multiply, but the same convolution creates all the illegal mixed
frequencies.

For the tent factors this support spill cannot cancel inside a positive
mixture.  Each factor has a nonnegative spectral measure

```text
delta_0+sum_u a_u(delta_u+delta_(-u))/2,      a_u>=0. (6.6)
```

Multiplication convolves these positive measures.  Every generated
sum/difference frequency therefore has nonnegative mass; averaging such
products cannot cancel it.  Projecting the product back onto `V_U` while
preserving positivity is precisely another signed actual-node interpolation
theorem, not a free tensor step.

Shrinking each seed to frequencies `|u|<=w/k` keeps the *generated interval*
inside `[-w,w]`, but it does not put the generated sums on the discrete
prime-power node set.  Replacing those sums by nearby actual nodes uniformly
through height `B` costs `B` times the log-frequency displacement.  Recovering
the product without that loss is exactly the unresolved high-denominator
prime-log coherence/interpolation theorem.

The primal version has the same support defect.  Convolution multiplies
Fourier moments, but Minkowski-adds the time supports: it exceeds the top
aperture and, after two-sided symmetrization, can fill the forbidden central
gap.

### Proposition 6.3 (positive-definite kernels cannot damp a resonant zero)

Let `g>=0` be supported on `[-w,w]`, with mass `G>0`, and set

```text
F_g(z)=int g(u)e^(zu)du.                              (6.7)
```

For `0<=a<=1`,

```text
e^(-aw)<=F_g(-a)/G<=e^(aw).                          (6.8)
```

If `g` is even, then more sharply

```text
F_g(-a)/G=E_g cosh(aU)>=1.                           (6.9)
```

Every real positive-definite kernel is even.  Hence the nonnegative
positive-definite kernels used to keep the pole transform nonnegative cannot
attenuate, at `t=gamma`, the Mellin factor of a zero
`rho=1-a+i gamma`; they retain at least its normalized mass.  Convolution,
pointwise products, and multiscale autocorrelation of such kernels remain in
the same class and still obey (6.9).

This proves a precise theorem-class boundary: applying a zero-free region
term by term with positive-definite shell kernels cannot improve the exponent
`Y^(beta-1)`.  It does **not** rule out cancellation among different zeros or
an adaptive signed actual-prime construction.

### Proposition 6.4 (positive iteration adds no feasible points)

Starting from strictly positive node weights `lambda_j`, any sequence of
positive multipliers `h_1(u_j),...,h_k(u_j)` and renormalizations ends at

```text
lambda'_j=
 lambda_j product_l h_l(u_j)
/sum_m lambda_m product_l h_l(u_m).                 (6.10)
```

This is one point of the original simplex.  Conversely every target simplex
point supported where `lambda_j>0` is obtained in one step.  Iterated
boosting, Riesz reweighting, and positive scale cooling do not enlarge the
positive feasible set.  Their success still requires the original
actual-node convex-hull statement.

### Proposition 6.5 (the VK-to-target bootstrap is the original game)

Define the best positive full-band margin

```text
v(U,H)=sup_(lambda in simplex) inf_(t in H)
       sum_j lambda_j cos(tu_j).                     (6.11)
```

Compact minimax gives the exact dual form

```text
v(U,H)=inf_(nu probability on H) max_j
       int_H cos(tu_j)dnu(t).                        (6.12)
```

The VK tent proves only `v(U,H)>=-eta_Y`, with
`eta_Y=exp[-c(log Y/log log Y)^(1/3)]`.  For a target
`epsilon_Y=Y^(-c)<<eta_Y`, failure of the target is witnessed by a `nu` for
which every coordinate in (6.12) is below `-epsilon_Y`.  Integrating the VK
base antenna against this `nu` merely puts its weighted average in the
nonempty interval `[-eta_Y,-epsilon_Y)`; there is no contradiction.

Thus neither minimax nor generic positivity bootstraps the subpower bound.
Excluding the witness in (6.12) is exactly the actual-prime positive-antipode
/ Delsarte theorem already being sought.  Guth--Maynard can sparsify the
large-value packets on which such a witness concentrates, but packet count
does not exclude the witness or control its carrier-specific cross-Gram.

---

## 7. Finite LP/SDP certification is exact but not asymptotic

For a positive antenna (1.2),

```text
|P_lambda'(t)|
 <=sum_j lambda_j|u_j|<=w.                           (7.1)
```

If a grid contains the endpoints of `H` and has maximal gap `Delta`, then

```text
inf_(t in H)P_lambda(t)
 >=min_(t in grid)P_lambda(t)-w Delta/2.             (7.2)
```

Thus a finite linear program plus rigorous interval evaluation can certify
the whole continuum at any fixed `Y`.  To spend half of
`epsilon=Y^(-c)` on interpolation, it is enough to take

```text
Delta<=epsilon/w,
#constraints=O(Y^(50/33+c)).                         (7.3)
```

At `c=.019`, the constraint exponent is

```text
50/33+.019=1.534151515151515....                     (7.4)
```

This is a valid finite algorithm, not an asymptotic proof.  A list of finite
extremizers supplies no uniform law as both the nodes and the aperture vary.
Weak convergence of the prime-log measures is also insufficient because the
test frequencies grow like `Y^(50/33)` and are not an equicontinuous class;
the previously audited half-period grids have excellent weak/mesh data while
their top-frequency cosine value is `-1` at every node.

For the full signed Delsarte LP, (7.1) becomes

```text
|Q'(t)|<=w sum_j |lambda_j|.                          (7.5)
```

No a priori variation bound is available.  A discretized signed SDP/LP is
therefore a continuum certificate only after it also certifies the coefficient
variation or uses interval positivity directly.

Christoffel/leverage bounds control two-sided `L2` evaluation in a chosen
feature span.  They do not imply the one-sided source residual needed here;
the exact critical saturation and projected-residual countermodels in the
companion Gram report remain applicable.

---

## 8. Primary quadrature/sampling scope check

The checked quadrature literature does not supply the missing asymptotic
step.

- Peherstorfer,
  [*Positive trigonometric Quadrature Formulas and quadrature on the unit circle*](https://arxiv.org/abs/1001.2451),
  characterizes formulas exact through a prescribed trigonometric degree via
  orthogonal/para-orthogonal node polynomials.  Its nodes satisfy that
  generated polynomial relation; the theorem does not place them at an
  arbitrary preassigned prime-log set.
- Kunis,
  [*Positive quadrature and mobile sampling of multivariate trigonometric polynomials*](https://arxiv.org/abs/2608.11915),
  treats exactness for full finite-dimensional trigonometric polynomial
  spaces and derives covering-radius necessities.  The QP condition is a
  one-sided approximate inequality for a sparse incommensurate frequency
  set, so the theorem is neither a closure nor a no-go for QP.
- Exact degree-`n` positive trigonometric quadrature needs at least `n+1`
  nodes by the Toeplitz moment-rank argument.  Here the actual shell has
  `Y^(1+o(1))` nodes while the aperture degree is `Y^(50/33)`.  Exact full
  quadrature is therefore impossible, but approximate one-sided quadrature
  remains the live problem.
- Deterministic sparse Fourier sampling can preserve a known antenna or norm
  on a finite space.  It does not improve the sign of the VK base antenna;
  sampling an antenna with floor `-eta` preserves that floor up to sampling
  error.  An adaptive selector that improves it is again the convex-hull
  problem.

These statements respect the source quantifiers.  None of the cited theorems
claims prescribed actual-prime nodes, every real height through
`Y^(50/33)`, and a fixed-power one-sided error simultaneously.

---

## 9. Hostile self-audit of Theorems 3.1 and 5.1

The nonsmooth tent and the height-uniform quantifiers were checked separately.

1. **Mellin inversion is absolute.**  The tent is continuous, compactly
   supported, vanishes at its endpoints, and is piecewise `C^1`.  Its exact
   transform (2.2) is entire and is `O((1+|v|)^(-2))` on every fixed vertical
   strip.  Hence the inverse integral is absolutely convergent.  On the
   initial line `Re s=a>0`, `sum Lambda(n)n^(-1-a)` is absolutely convergent,
   so exchanging sum and integral in (3.2) is legal.
2. **The contour does not hide a smoothness loss.**  Take horizontal edges
   along a standard good-height sequence, separated from zero ordinates,
   where `zeta'/zeta` is at most polynomial (the standard partial-fraction
   bound gives `O(log^2 V)` in the fixed rectangle).  The tent's `V^(-2)`
   decay makes those edges vanish.  Smooth compact support is unnecessary.
3. **All crossed poles are accounted for.**  Between `Re s=a` and
   `Re s=-3/2` lie `s=0` and the nontrivial poles `s=rho-1`.  Since
   `zeta(0)=-1/2`, there is no pole at `s=-1`; the first trivial-zero pole is
   `s=-3`, outside the contour.
4. **The zero series is genuinely absolute.**  Uniformly for
   `-1<=beta-1<=0`, (3.3) gives the summand majorant
   `C_w(1+|gamma-t|)^(-2)`.  Unit-interval zero counts give (3.6), including
   multiplicities.
5. **The polynomial aperture is uniform.**  The new-line integral is a
   convolution of `(1+|v-t|)^(-2)` with `log(2+|v|)`, hence is
   `O(log(2+|t|))`.  The VK zero tail beyond `Y^D`, with fixed `D>A+2`, is
   `O(Y^(-D)log Y)` because `|gamma-t|` is comparable to `|gamma|` there.
6. **Normalization has the right scale and sign.**  At `t=0` the same
   absolutely convergent formula gives `W_Y=w+o(1)>0`.  Dividing by `W_Y`
   therefore loses only a fixed factor, and aggregation at equal absolute
   nodes preserves positivity and every cosine moment.

An independent multiplicative-side hostile pass recomputed the transform
shift, residues, first trivial-zero location, new-line error, VK tail, and
normalization and found no defect.  The replay scripts check only the exact
finite algebra and exponent polarity; they do not purport to numerically
verify a zero-free region.

---

## 10. Final disposition

```text
actual positive tent on prescribed prime-power nodes:       CONSTRUCTED;
exact all-height explicit formula for that antenna:         PROVED;
unconditional VK subpower full-band Delsarte bound:         PROVED;
fixed strip delta -> every Delsarte power c<delta:           PROVED;
strip width >kappa_max kills fixed d=33/50 slice:            PROVED, CONDITIONAL;
convex/disjoint-subshell multiplicative amplification:       FALSE;
nonlinear/tensor amplification inside actual frequency pool: FALSE;
positive-definite kernel improvement of the VK exponent:     FALSE TERM BY TERM;
finite positive LP continuum certification:                  PROVED PER Y;
asymptotic fixed-power actual-node certificate:               OPEN;
QP-PROMOTE or unconditional QP-KILL:                          NOT PROVED;
uniform zeta zero-free strip:                                 NOT PROVED.
```

The surviving theorem must exploit cancellation that all absolute-value and
positive-kernel arguments discard: an adaptive actual-prime cross-Gram/zero
correlation bound strong enough to improve `Y^(-o(1))` to `Y^(-c)` while
retaining one-sided positivity on **every** height.  That is the original
Delsarte gate in its narrowest current form.

Replay:

```bash
python3 src/test_qp_tent_explicit_formula_gate.py
python3 results/verify_zeta23_qp_tent_explicit_formula_gate.py
```
