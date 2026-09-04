# Log curvature and the consecutive-gap antenna

## Truncated third moment, a longer proved transition, and an integer no-go

**Verdict.**  The exact symmetric gap rule does yield one further theorem for
the actual primes.  Combining the Gafni--Tao exceptional-gap envelope with
Stadlmann's gap input gives a truncated third moment strong enough to prove

```text
|P_short(t)-b(t)| << Y^(-1173/65000+epsilon)
                  for |t| <= Y^(4203/5000).          (0.1)
```

Here `P_short` is the positive logarithmic Voronoi rule after deleting both
half-cells of every physical gap larger than
`C_w Y^(797/5000)`, with the fixed shell constant `C_w`.  Since

```text
4203/5000=.8406,
1173/65000=.018046153846...>.0180303234,              (0.2)
```

this moves the end of the proved transition band from `Y^.751` to
`Y^.8406`.  For this fixed rational deletion threshold, the formal Peano
frontier is

```text
.840607915223...;                                    (0.3)
```

the conservative endpoint `.8406` makes the third-moment saving equal to the
already verified long-gap-mass saving.

If the deletion exponent is allowed to approach the continuous Gafni--Tao
tail boundary

```text
theta_*=2/15+(13/9)kappa=.1593771338,
```

the same argument reaches every fixed exponent strictly below

```text
1-theta_*=.8406228662.                                (0.4)
```

The displayed theorem keeps the already audited rational choice and its
strict theorem margin.

There is also a sharper, tightly scoped no-go.  One can construct **odd
integer** nodes, all with gaps comparable to `log Y`, whose exact logarithmic
phases at `t=Y^(50/33)` are coherent on all but `o(1)` of their Voronoi mass.
They survive the optimized low-denominator cell deletion.  Thus

```text
integrality + exact global log curvature + positivity + prime-shaped density
+ tiny gaps + low-q deletion
```

still do not imply cancellation for an arbitrary node set.  This is not a
prime counterexample.  It sharpens the diagnosis: a proof above `Y^.8406`
must use a property of actual primality correlated with consecutive gaps, not
merely the fact that the nodes are integers on a globally curved phase.

---

## 1. Inputs and notation

Put

```text
theta=797/5000=.1594,
mu=63827/65000=.981953846153...,
d=1-mu=1173/65000=.018046153846... .                 (1.1)
```

Keep the fixed shell constant explicit by writing

```text
G_gamma=C_w Y^gamma.                                 (1.2)
```

The Gafni--Tao envelope already audited in
`ZETA23-HIGH-DENOMINATOR-GAP-EXCEPTIONAL-TAIL-GATE-2026-08-13.md`
gives, uniformly for `2/15<=gamma<=theta`,

```text
sum_(p_j asyp Y, g_j>G_gamma) g_j
 <<_epsilon Y^[mu(gamma)+epsilon],

mu(gamma)=1-(9/13)(gamma-2/15).                       (1.3)
```

In particular `mu(theta)=mu`.  This is the exceptional-*measure* conclusion,
not just a count of exceptional gaps.  Stadlmann supplies

```text
sum_(p_j asyp Y) g_j^2 <<_epsilon Y^(1.23+epsilon),  (1.4)
```

although the new third-moment estimate below uses the full envelope (1.3),
not merely (1.4).

Write

```text
v_j=log(p_j/Y),             Delta_j=v_(j+1)-v_j,
F_t(u)=phi(u) exp(i t u).                            (1.5)
```

For every gap with `g_j<=G_theta`, retain its two logarithmic half-cells.
Delete both halves of every longer gap.  Let `P_short(t)` be the resulting
positive endpoint/Voronoi rule, and let `P_full(t)` be the original full
Voronoi antenna.  If `P_long=P_full-P_short`, positivity and (1.3) give

```text
P_full(t)=P_short(t)+P_long(t),
|P_long(t)|<=mass(P_long)
 <<Y^(mu-1+epsilon)=Y^(-d+epsilon).                   (1.6)
```

Thus every estimate below for `P_short-b`, after adding (1.6), gives the same
exponent estimate for the original antenna `P_full-b`.  The two rules are not
being identified.

Fixed shell constants, the single kink of `phi`, and the two support endpoints
are harmless below; they are suppressed from exponent notation.

---

## 2. The missing moment was the third, not the second

### Lemma 2.1 (truncated third moment)

For the retained physical gaps,

```text
sum_(g_j<=G_theta) g_j^3
 <<_epsilon Y^(2 theta+mu+epsilon)
 =Y^(84549/65000+epsilon).                            (2.1)
```

#### Proof

For `g<=G_(2/15)`, telescoping the gap lengths gives

```text
sum g^3 <=Y^(4/15) sum g <<Y^(1+4/15),               (2.2)
```

whose exponent `19/15=1.2666...` is smaller than the exponent in (2.1).

For a dyadic bin `G_gamma<g<=2G_gamma`, (1.3) gives

```text
sum_bin g^3
 <<Y^(2 gamma) sum_(g>G_gamma) g
 <<Y^[2 gamma+mu(gamma)+epsilon].                    (2.3)
```

On `[2/15,theta]`, the exponent in (2.3) has slope

```text
2-9/13=17/13>0.                                      (2.4)
```

Its maximum is therefore at `gamma=theta`, where it is `2 theta+mu`.
There are only `O(log Y)` bins, absorbed by `Y^epsilon`.  QED

Since `Delta_j<=C g_j/Y`, Lemma 2.1 immediately gives

```text
sum_(g_j<=G_theta) Delta_j^3
 <<Y^[-(3-2 theta-mu)+epsilon]
 =Y^(-110451/65000+epsilon).                          (2.5)
```

The saving before the two derivatives of the oscillatory function is

```text
110451/65000=1.699246153846... .                      (2.6)
```

---

## 3. Exact gap splitting and the trapezoid theorem

On a retained logarithmic gap `[v_j,v_(j+1)]`, let

```text
m_j=(v_j+v_(j+1))/2.
```

Its exact contribution to the Voronoi rule is

```text
Q_j(t)=exp(i t v_j) integral_(v_j)^m_j phi(u)du
      +exp(i t v_(j+1)) integral_m_j^(v_(j+1)) phi(u)du.  (3.1)
```

Introduce the ordinary endpoint trapezoid

```text
T_j(t)=Delta_j [F_t(v_j)+F_t(v_(j+1))]/2.             (3.2)
```

Because only the nonoscillatory amplitude is changed in passing from (3.1)
to (3.2),

```text
|Q_j-T_j| <=C_phi Delta_j^2.                          (3.3)
```

Summing (3.3) and using Stadlmann gives `O(Y^(-.77+epsilon))`.

Away from the single gap meeting the kink of `phi`, the Peano remainder for
the trapezoid rule gives

```text
|T_j-integral_(v_j)^(v_(j+1)) F_t(u)du|
 <=(Delta_j^3/12) sup_gap |F_t''|
 <=C_phi (1+t^2)Delta_j^3.                            (3.4)
```

The kink gap can be bounded directly by `O(Delta_j)` (already far smaller
than the target) or split at the kink.  The two support endpoint pieces gain
an extra power because `phi` vanishes linearly there.  Thus (1.6), (2.5),
(3.3), and (3.4) prove the following.

### Theorem 3.1 (actual-prime truncated-trapezoid transition)

Uniformly for real `t`,

```text
|P_short(t)-b(t)|
 <<_epsilon
 Y^(-d+epsilon)
 +Y^(-.77+epsilon)
 +(1+t^2)Y^(-110451/65000+epsilon).                  (3.5)
```

Moreover, (1.6) recovers the original antenna without changing an exponent:

```text
|P_full(t)-b(t)|
 <=|P_short(t)-b(t)|+|P_long(t)|,
```

so the right side of (3.5) also bounds `|P_full(t)-b(t)|`.

At

```text
|t|<=Y^(1-theta)=Y^(4203/5000),                      (3.6)
```

the saving in the last term is exactly

```text
110451/65000-2(4203/5000)
 =1173/65000=d.                                       (3.7)
```

This proves (0.1).  Since `d-kappa=1.5830446...*10^-5`, one first fixes the
epsilon losses below that strict margin.  More generally, the Peano term by
itself clears `kappa=.0180303234` through

```text
a <(110451/65000-kappa)/2
   =.8406079152230769... .                            (3.8)
```

The long-gap error remains capped by `d`, so (3.8) is the complete frontier
of this particular absolute truncated-third-moment argument.

There is a slightly larger continuous frontier if one reoptimizes the
deletion exponent for the transition instead of fixing `theta=.1594`.  For a
general `gamma` on the linear envelope (1.3), the tail saving is

```text
1-mu(gamma)=(9/13)(gamma-2/15).                       (3.9)
```

The smallest admissible exponent tends to

```text
gamma_*=2/15+(13/9)kappa=.1593771338.
```

At `a=1-gamma`, the Peano saving equals the tail saving, exactly as in
(3.7).  Hence every fixed

```text
a<1-gamma_*=.8406228662                              (3.10)
```

is reachable after choosing a fixed `gamma>gamma_*` sufficiently close to
`gamma_*`.  Equality is not claimed: at the boundary the strict margin over
`kappa` disappears.

### Consequence for the live strip route

The formerly open companion transition

```text
Y^.751 <=t<=Y
```

is reduced, with the audited rational parameters, rigorously to

```text
Y^.8406 <=t<=Y.                                      (3.11)
```

The super-`Y` retained high-denominator target is unchanged.

---

## 4. A single hostile model with integrality and exact curvature

The earlier audits deliberately used one integer frozen-additive model and
one real-node exact-log model.  The following construction combines their two
features.  Its purpose is to audit what a deterministic curvature proof can
possibly use.

### Theorem 4.1 (odd-integer exact-log coherence)

Fix a multiplicative shell `[cY,CY]`, with `0<c<C`, and put

```text
t=Y^(50/33),                 f(x)=t log(x/Y)/(2 pi).
```

For every sufficiently large `Y` there is a set `X_Y` of odd integers in the
shell such that

```text
#X_Y asyp Y/log Y,
log Y << x_(j+1)-x_j <<log Y,
sum_j (x_(j+1)-x_j)^2 <<Y log Y,                     (4.1)

#(X_Y intersect J)<<1+|J|/log Y                     (4.2)
```

for every interval `J`.  If `lambda_j` are its logarithmic Voronoi weights,
then, after deleting all cells meeting the optimized derivative-rational set
with `q<=Y^(1537/10000)`,

```text
|sum_retained lambda_j exp(i t log(x_j/Y))| >>1.      (4.3)
```

All gaps are `O(log Y)`, so its `C_w Y^(797/5000)` long-gap set is empty.  The
retained continuum transform is `o(1)`, and consequently the exact retained
Voronoi error is also bounded below by a positive constant.

The construction works, with the same proof, in any one fixed reduced residue
class modulo a fixed integer `W`; odd integers are the case `W=2`.

#### Proof: a local discrepancy lemma

Choose a small fixed arc

```text
I={z mod 1: ||z||<=epsilon_0},
```

say `epsilon_0=1/100`, and put `L=C_0 log Y`, where `C_0` is a sufficiently
large fixed constant.  Erdős--Turán's discrepancy inequality says that the
number of terms of a finite sequence in `I` differs from `2 epsilon_0` times
its length by at most

```text
C[N/H+sum_(1<=h<=H) |S_h|/h].                        (4.4)
```

Choose fixed constants `H` and then `D`, large in terms of `epsilon_0`.  Mark
the derivative-resonant set

```text
B={x in [cY,CY]: ||2h f'(x)||<D/L
                       for some 1<=h<=H}.             (4.5)
```

For an odd progression `n_0+2k` in a length-`L` interval outside a fixed
enlargement of `B`, linearization gives

```text
f(n_0+2k)=f(n_0)+2k f'(n_0)+O(t L^2/Y^2).             (4.6)
```

Here

```text
t L^2/Y^2=Y^(-16/33) log^2 Y=o(1).                   (4.7)
```

The geometric progression estimate and (4.5) give, for `h<=H`,

```text
|S_h| <<L/D+o(L).                                     (4.8)
```

Taking `H,D` successively large makes the discrepancy in (4.4) smaller than
`epsilon_0 L`.  Every such good interval therefore contains a positive
proportion of odd integers `n` satisfying

```text
||f(n)||<=epsilon_0.                                  (4.9)
```

These are the coherent candidates.

#### Proof: the resonant set has negligible length

Since

```text
f'(x)=t/(2 pi x),             |f''(x)| asyp t/Y^2,    (4.10)
```

the preimage for one pair `(h,a)` in (4.5) has length

```text
<<Y^2/(h t L).                                        (4.11)
```

For fixed `h`, only `O(h t/Y+1)` integers `a` occur.  Summing over the fixed
range `h<=H` gives

```text
|B|<<Y/L.                                             (4.12)
```

There are `O_H(t/Y+1)` components.  Enlarging them by `O(L)` changes their
total length by at most

```text
O((t/Y+1)L).
```

After division by `Y`, (4.12) and the enlargement cost are

```text
O(1/log Y+t log Y/Y^2)=o(1).                          (4.13)
```

#### Proof: select the nodes

On every good component, greedily thin the candidates (4.9) so consecutive
selected candidates are separated by comparable multiples of `L`.  The local
density statement following (4.8) guarantees an `O(L)` upper gap.  Fill the
enlarged bad components with arbitrary odd integers on an `asymp L` grid.
Elementary endpoint adjustments preserve both lower and upper `asymp L`
spacing.  This proves (4.1)--(4.2).

The Voronoi mass carried by filler nodes is bounded by the length in (4.13)
plus one `O(L)` collar per bad component, and hence is `o(1)` after logarithmic
normalization.  Every other node obeys (4.9), so

```text
Re exp(2 pi i f(x_j))>=cos(2 pi epsilon_0)>0.99.       (4.14)
```

It follows that the full normalized Voronoi sum has real part bounded below
by a positive constant.

Finally, the physical measure and component estimates for the optimized
low-denominator set are

```text
|M_t(Q)|<<Q sqrt(t),             #components<<(t/Y)Q^2,
Q=Y^(1537/10000).                                     (4.15)
```

Because every cell has length `O(log Y)`, the cell mass deleted in (4.15) is

```text
<<Q sqrt(t)/Y + t Q^2 log Y/Y^2=o(1),                (4.16)
```

the two exponent savings being `.088724...` and `.177448...`.  Equation
(4.3) follows.  The full continuum transform is `O(t^-2)`, and its restriction
to the deleted set is bounded by (4.16), so the retained continuum term is
`o(1)` as asserted.  QED

### Exact scope

Theorem 4.1 proves the nonimplication

```text
integer support (even a fixed wheel class)
+ exact t log x curvature
+ prime-density-shaped node count and local upper count
+ max gap O(log Y) and sum gap^2=O(Y log Y)
+ positive logarithmic Voronoi weights
+ optimized low-q deletion

does not imply a power-saving retained antenna for arbitrary node sets.    (4.17)
```

It does **not** give a set of primes, preserve von Mangoldt convolution, or
satisfy prime-tuple distribution statements.  It therefore does not rule out
the actual-prime target.  Its point is narrower and useful: a B-process,
transfer-matrix, or van der Corput proof that sees only integer locations,
smooth log curvature, and gap geometry cannot finish the route.

---

## 5. Summation by parts and B-process diagnosis

For constant amplitude on one log gap, the exact error remains

```text
Delta exp(i t m)[cos(t Delta/2)-sinc(t Delta/2)].     (5.1)
```

Writing the leading symmetric endpoint measure cumulatively reveals exactly
one extra local cancellation.  On a physical gap `[p,p+g]`, its discrepancy
from Lebesgue measure is the centered sawtooth

```text
D(x)=p+g/2-x.                                         (5.2)
```

It has zero integral on that gap.  A second summation by parts therefore
produces a Peano kernel of mass `asymp g^3`, which is precisely Lemma 2.1 and
Theorem 3.1.  The next primitive has nonzero mass of one sign.  Without a
correlation between different actual prime gaps, another deterministic
summation by parts merely accumulates `sum g^3`; it does not create a third
local cancellation.

Likewise, a B-process over the gap index has phase

```text
t(v_j+v_(j+1))/2,
```

whose first differences involve `(Delta_j+Delta_(j+1))/2` and whose second
differences involve unsmoothed consecutive-gap differences.  Neither
Stadlmann nor Gafni--Tao controls their sign variation.  Theorem 4.1 shows that
no universal curvature estimate can supply the missing variation: the support
itself may track the phase while retaining all the geometric packages.

---

## 6. Literature audit

1. Gafni--Tao,
   [*On the number of exceptional intervals to the prime number theorem in
   short intervals*](https://arxiv.org/abs/2505.24017), supplies the
   exceptional-measure envelope used in Lemma 2.1.  Published numbering is
   Theorem 1.4; arXiv v1 numbering is Theorem 1.2.  It is phase blind after the
   tail deletion.
2. Stadlmann,
   [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867),
   supplies the second-moment comparison error in (3.3).  It does not control
   consecutive-gap differences required by a B-process.
3. Colzani--Gigante--Travaglini,
   [*Trigonometric approximation and a general form of the Erdős--Turán
   inequality*](https://arxiv.org/abs/1001.0948), gives a primary modern
   treatment of the discrepancy tool used in Theorem 4.1.  Here that tool
   constructs a no-go model; it is not a theorem about primes.
4. Helfgott's
   [*The ternary Goldbach problem*](https://arxiv.org/abs/1501.05438),
   especially the explicit large-sieve/Type-II estimates in Chapter 5,
   illustrates the standard rational-frequency machinery for natural prime
   weights.  Those estimates use von Mangoldt structure and do not transfer
   to positive consecutive-gap Voronoi coefficients.
5. The search also returns Ferreira,
   [*Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725).
   Its abstract claims a prime number theorem in every interval `x^lambda`,
   `0<lambda<1`, and hence eventual Legendre-type conjectures.  As of the
   audited arXiv v4 page it is a preprint whose status says only "submitted to
   Annals of Mathematics"; no refereed publication is identified there.
   Those claims would resolve famous open problems, so they are not treated
   as established input.  Even the stated short-interval count is phase blind
   and does not state the consecutive-gap Fourier estimate needed here.

No primary source located in this sweep proves or disproves the actual-prime
retained estimate.  In particular, Theorem 4.1 is the no-go only for the
explicit abstract package (4.17), not for actual primes.

---

## 7. Updated survivor

The proved part is now

```text
actual-prime positive antenna through t=Y^.8406:       PROVED;
optimized long-gap and low-q mass deletion:            PROVED;
integer/global-curvature package alone:                 INSUFFICIENT;
actual-prime interval Y^.8406<=t<=Y:                    OPEN;
actual-prime retained super-Y high-denominator mode:    OPEN.           (7.1)
```

The best next target remains a sign-sensitive actual-prime theorem: a growing
modulus forward/reverse consecutive-gap dispersion estimate, or an equivalent
correlation estimate for the boundary values of the gap-renewal transform.

The rational exponent ledger and the countermodel deletion exponents are
checked by

```bash
python3 results/verify_zeta23_log_curvature_transition.py
```
