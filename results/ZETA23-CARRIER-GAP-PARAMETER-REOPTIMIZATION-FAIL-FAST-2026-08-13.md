# Carrier/gap parameter reoptimization: one depth slice closes, no uniform strip closes

**Date:** 2026-08-13

## Verdict

The coupled exponent ledger has two different quantifiers, and they must not
be interchanged.

1. If one insists on

   ```text
   .49<=alpha_0<.5,       1/2<d<2/3,
   ```

   no reoptimization within the current Gafni--Tao tail plus half-cell
   cover closes even the positive same-residue one-gap pole sector.  The
   best value occurs only at the inadmissible limiting point
   `alpha_0=.49, d->2/3`, and still has deficit

   ```text
   c_pole-kappa -> -.001034601762499405....          (0.1)
   ```

2. The lower bound `.49` is not a structural packet constraint.  It encoded
   the chosen target `Re rho>=.99`.  At the **single fixed depth** `.47`, an
   entirely interior rational calibration is

   ```text
   alpha=47/100=.47,          d=133/200=.665,
   theta=397/2500=.1588,      beta=799/5000=.1598.   (0.2)
   ```

   It satisfies every exponent and raw-carrier constraint audited below at
   `alpha=.47`.
   In particular `beta>theta`.  Once gaps above `Y^theta` are deleted, every
   reduced denominator of a literal one-gap recurrence is at most the gap
   and hence lies below `Y^beta`; the rational cover removes it.  The
   retained literal one-gap pole sector is therefore empty on that slice.

3. This does **not** close the full high tail `QP`, much less the
   candidate-centered route or a strip.  Multi-gap recurrences still have
   denominators up to `Y^(1-A/2)=Y^.2481203...`, far above the rational
   cutoff.  The nonpole retained minor-cell sum is also not bounded merely
   by deleting exact recurrences.  Moreover the global compact Pick gate
   `GP` and the same-state arithmetic reserve `GA` remain open.

4. More fundamentally, there is a quantifier reversal.  The lower-end value
   `kappa(alpha_0,d)` is the conservative budget for a **promotion** theorem.
   A dual antenna which claims to kill an architecture uniformly for
   `alpha in [alpha_0,1/2)` must instead beat the supremum
   `kappa(1/2,d)`.  At `d=.665` this is `.01974048258...`, larger than the
   tail, collar, and pole savings in (0.2) (the inverse-image row is slack).
   Even the continuously reoptimized top-depth pole frontier has margin
   `-.00312991348...`.  Thus (0.2) is a valid
   shallow-slice and literal-sector simplification, not an architecture-wide
   dual kill.  The earlier fixed-strip implication is explicitly retracted.

Thus reoptimization definitively removes the retained *literal one-gap
pole* only at the `.47` depth slice for the fixed cutoffs (0.2), and its
positive-mass errors clear only that slice's budget.  It does not remove the
pole uniformly over a band reaching `1/2`, and it does not turn the current
Gafni--Tao input into a full antenna theorem.

No zero-free strip is claimed.

---

## 1. Complete carrier and aperture ledger

Let

```text
Y=X^d,          1/2<d<2/3.
```

The available relative frequency interval has length `X`.  Consequently,
in `Y`-units its exponent is not an independent constant:

```text
B_max=X=Y^A,          A=1/d.                        (1.1)
```

This reproduces `A=50/33` only at the old `d=.66=33/50`.

The phase-cell-compressed one-product carrier exponent is

```text
E_1(alpha,d,a)
 =alpha*(d-1/2)*(1-R(y)),

y=pi*a/[alpha*(2d-1)],
R(y)={y log(1+y^-2)+2 atan(y)}/pi.                  (1.2)
```

For a target band `alpha in [alpha_0,1/2)`, the carrier exponent increases
with depth because

```text
d/dalpha {alpha*(1-R(C/alpha))}
 =1-2 atan(C/alpha)/pi>0.                           (1.3)
```

Consequently the band has two different extremal losses:

```text
kappa_min=kappa(alpha_0,d),
kappa_max=sup_(alpha_0<=alpha<1/2) kappa(alpha,d)
         =kappa(1/2,d).                             (1.4)
```

The first is the conservative uniform loss budget for a sufficient
**promotion** theorem: it is the smallest carrier supplied anywhere in the
band.  A dual **kill** valid for every possible candidate must instead have
an upper-bound saving larger than `kappa(alpha,d)` at every depth, so it must
beat `kappa_max`.  A saving strictly between the two kills the lower endpoint
without killing deeper candidates.  This promotion-minimum/kill-maximum
polarity is audited numerically in Section 5.3.

### The zero-count constant cannot be optimized away

The scalar

```text
a=.10076                                             (1.5)
```

is the coefficient in the global Bellotti--Wong endpoint discrepancy.  It
enters the cumulative full-window measure constraint used to derive (1.2).
The depth-sensitive microscopic count is a different constraint: it bounds
the number of zeros above a fixed horizontal line in one microscopic cell,
but still permits `Theta(log T)` rows there and does not replace the global
endpoint discrepancy by a smaller `a`.

Using `a>.10076` would be a valid but deliberately weaker count bound and
would artificially lower the guaranteed carrier.  Using `a<.10076` is not
licensed by the imported theorem.  The strongest currently proved version
of this ledger therefore keeps (1.5).  Bellotti--Wong's current primary
preprint states the same leading coefficient:
[arXiv:2412.15470](https://arxiv.org/abs/2412.15470).

### The Green--Poisson bill must also fit

The rounded positive-majorant certificate is, for general `d`,

```text
B_GP(d)<=.304/2+d*1.39/(2*pi)
        =.152+d*1.39/(2*pi).                        (1.6)
```

The old decimal `.298008745` is the specialization of (1.6) at `d=.66`;
it is not constant when `d` changes.  To retain the exponent (1.2), the
complete conditional geometry ledger requires

```text
alpha*d-B_GP(d) >= E_1(alpha,d,a)>0.                (1.7)
```

For (0.2),

```text
raw carrier alpha*d                         =.31255,
B_GP(.665)                                  =.299114871646993...,
Green reserve                               =.0134351283530065...,
E_1(.47,.665,.10076)                        =.0116523085190794...,
Green reserve-E_1                           =.00178281983392718.... (1.8)
```

Thus the Green bill is strictly nonbinding.  This is only an exponent
compatibility statement: the global representative reduction and compact
transfer assumed by both carrier ledgers remain unproved.

At the top of the putative band, the Green ledger has still more room:

```text
raw carrier at alpha=1/2                    =.3325,
Green reserve                               =.0333851283530066...,
E_1(.5,.665,.10076)                         =.0131274209176565...,
Green reserve-E_1                           =.0202577074353501.... (1.9)
```

Thus the uniform-kill failure is not caused by the raw Green--Poisson bill.
The carrier that must be contradicted grows with depth, while the present
gap/rational-cover savings do not keep pace.

The proof of the Green majorant uses `alpha<=A_0=.5`; its displayed lower
restriction `.49` was the selected target, not a hypothesis of the kernel
majorization.  The packet ledger also retains the strict `d<2/3` condition.
The older padding floor `alpha>3/8` is comfortably satisfied by `.47`.
The legacy compact-tail sufficient condition also has strict room:

```text
alpha*d^2-2a=.00632575>0.                           (1.10)
```

---

## 2. Coupled Gafni--Tao and rational-cover frontier

On the certified local branch of the Gafni--Tao envelope,

```text
s(theta)=(45 theta-6)/65
        =(9/13)(theta-2/15).                         (2.1)
```

For aperture exponent `A=1/d`, gap cutoff `Y^theta`, rational cutoff
`Y^beta`, and required saving `kappa`, the three positive-mass conditions
are

```text
s(theta)>kappa,                                     (tail)
2-A-2 beta-theta>kappa,                             (half-cell collar)
1-A/2-beta>kappa.                                   (inverse-image mass) (2.2)
```

The last condition is slack in the range used here.  The continuous strict
frontier is approached from inside at

```text
theta_0=2/15+(13/9)kappa,
beta_0 =14/15-1/(2d)-(11/9)kappa.                   (2.3)
```

The strongest unconditional positive same-residue pole bound at denominator
`Y^beta` is `s(beta)`.  Since `s(theta_0)=kappa`, its limiting margin has the
three equivalent forms

```text
s(beta_0)-kappa
 =(9/13)(beta_0-theta_0)
 =36/65-9/(26d)-(24/13)kappa
 =(24/13){kappa_crit(d)-kappa},                     (2.4)

kappa_crit(d)=3/10-3/(16d).                         (2.5)
```

Thus the pole closes exactly when the optimized rational cover overtakes
the gap cutoff:

```text
kappa<kappa_crit(d)  iff  beta_0>theta_0.            (2.6)
```

This equivalence is more informative than comparing two rounded decimal
savings: it says when there is no retained literal one-gap denominator at
all.

### Peano transition

The same tail gives

```text
sum_(g<=Y^theta) g^3 <<Y^(2 theta+1-s(theta)+epsilon).
```

After division by `Y^3`, the trapezoid Peano term at `t=Y^u` has saving

```text
2+s(theta)-2 theta-2u.                              (2.7)
```

It clears `kappa` through every fixed

```text
u < u_P(theta):={2+s(theta)-2theta-kappa}/2.         (2.8)
```

At the continuous tail boundary this tends to `1-theta_0`.

The primary exceptional-interval input for (2.1) is Gafni--Tao,
[*On the number of exceptional intervals to the prime number theorem in
short intervals*](https://arxiv.org/abs/2505.24017), Theorem 1.2 and its
zero-density table.

---

## 3. Slice optimization and the old `alpha>=.49` no-go

For fixed `d`, (1.3) shows that `kappa` increases with `alpha`; hence the
pole margin (2.4) decreases.  The best old-band value is at `alpha=.49`.

The remaining `d` optimization is also one-sided.  Put

```text
z=2d-1,       y=pi*a/(alpha*z),
f(y)=1-R(y),  ell(y)=log(1+y^-2).
```

Then

```text
kappa=alpha*z*f(y)/(z+1),

d kappa/dz
 =alpha{f/(z+1)^2+y ell/[pi(z+1)]}.                 (3.1)
```

For `alpha<=1/2`, `z<=1/3`, and `a=.10076`, one has
`y>=6*pi*a>sqrt(3)`.  Hence `f<1/3` and
`y*ell<1/y<1/sqrt(3)`.  Differentiating

```text
beta_0-theta_0=4/5-1/(z+1)-(8/3)kappa              (3.2)
```

and using `pi>3` gives

```text
(z+1)^2*d/dz(beta_0-theta_0)
 >1-(4/3){1/3+4/[9 sqrt(3)]}>0.                    (3.3)
```

Therefore the old-band pole margin increases with `d`, and its supremum is
the excluded endpoint `d=2/3`.  There,

```text
kappa                              =.019310409288020511...,
theta_0                            =.161226146749362960...,
beta_0                             =.159731721981308264...,
s(beta_0)                          =.018275807525521106...,
s(beta_0)-kappa                    =-.001034601762499405.... (3.4)
```

Every legal interior point is strictly worse.  This proves (0.1), rather
than merely observing it on a grid.

At the limiting `d=2/3`, the unique **single-depth slice** at which the
corridor just closes is the solution of

```text
kappa(alpha,2/3)=3/160,
```

namely

```text
alpha_*=.482559677686675026391908603751....         (3.5)
```

At the level of the tail/cover comparison, every fixed depth
`alpha<alpha_*` has a positive slice pole margin for sufficiently close
interior `d<2/3`.  Full slice legality additionally requires the Green and
packet conditions in Section 1; these exclude taking `alpha` arbitrarily
small.  The explicit `.47` certificate satisfies them.  This crossover says
nothing uniform about `[alpha,.5)`, because that band also contains depths
above `alpha_*`.  Indeed, every band reaching `1/2` contains top-depth slices
on the failing side of the crossover.  In particular, for `alpha>=.49` no
single slice closes the pole within this package.

---

## 4. Exact interior certificate at the `.47` slice

Use (0.2).  The resulting carrier and continuous frontiers are

```text
A=1/d=200/133                              =1.5037593984962406...,
E_1                                        =.011652308519079366...,
kappa=E_1/d                                =.017522268449743408...,
theta_0                                    =.158643276649629367...,
beta_0                                     =.160037528202193312.... (4.1)
```

The rational interior choices `theta=.1588`, `beta=.1598` give

| ledger item | saving | margin over `kappa` |
|---|---:|---:|
| Gafni--Tao long-gap tail `s(theta)` | `.017630769230769231` | `.000108500781025823` |
| short-half collar `2-A-2beta-theta` | `.017840601503759398` | `.000318333054015990` |
| main inverse-image length `1-A/2-beta` | `.088320300751879699` | `.070798032302136291` |
| same-residue tail `s(beta)` | `.018323076923076923` | `.000800808473333515` |

All inequalities are strict against `kappa(.47,.665)`.  More strongly,

```text
beta-theta=.001>0.                                  (4.2)
```

For every retained short gap `g<=Y^theta`, a literal endpoint recurrence
has reduced denominator `q|g`, so `q<=g<=Y^theta<Y^beta`.  It is already in
the rational cover.  Long gaps cost the first row of the table.  This proves
the asserted one-gap pole closure at exactly the `.47` depth slice; it is not
a statement uniform in `alpha>.47`.

The Peano endpoint from (2.8) is

```text
u_P=.841254250390512911....                          (4.3)
```

Thus the symmetric actual-prime transition estimate can be run through
every fixed `u<.84125425`, with the strict epsilon chosen below the smallest
table margin.

---

## 5. Hostile scope audit

### 5.1 What has actually been eliminated

The certificate eliminates only the positive mass carried by a **single
retained gap whose two rational endpoint phases coincide**.  It is stronger
than the prior estimate of that sector because no such retained gap exists
after the cover and cutoff at `alpha=.47`.  No uniform band elimination is
asserted.

### 5.2 Why full `QP` remains open

At the top aperture a curvature block has physical span and natural
denominator as large as

```text
Y/sqrt(t)=Y^(1-A/2)=Y^.2481203007518797....          (5.1)
```

This is far above `Y^beta=Y^.1598`.  A recurrence accumulated over several
consecutive gaps need not have a denominator dividing any individual gap.
Neither (4.2) nor the positive tail estimates control its selected signed
Fourier mode.

Also, absence of exact one-gap recurrence is not a quantitative minor-arc
bound for the entire retained Voronoi integral.  Near recurrences and
coherent sums of many individually nonresonant edges still require the
actual-prime consecutive-transition theorem isolated in the character and
dispersion audits.

Finally, (4.3) leaves the companion transition

```text
Y^.84125425 <= t <=Y
```

uncontrolled by this Peano estimate.

### 5.3 Promotion minimum versus dual-kill maximum

Changing `.49` to `.47` changes the desired candidate band from
`Re rho>=.99` to `Re rho>=.97`; the latter would be a stronger zero-free
statement.  But the present calculation is on the **dual/no-go** side of
`QP`, so lowering the depth weakens the carrier and makes that calculation
easier.  These directions must not be conflated.

For a sufficient promotion theorem one may deliberately retain only the
uniform lower-end carrier `E_1(alpha_0,d)`.  For a dual theorem claiming to
eliminate an architecture that may adapt to the actual candidate depth, the
comparison is instead

```text
c>sup_(alpha_0<=alpha<1/2) kappa(alpha,d)
  =kappa(1/2,d).                                    (5.2)
```

At `d=.665`,

```text
kappa(.47,.665)=.0175222684497434...,
kappa_crit(.665)=.0180451127819549...,
kappa(.5,.665) =.0197404825829421....               (5.3)
```

The fixed-cutoff savings have the following margins against the required
band maximum, not against the easier lower endpoint:

| fixed-cutoff component | saving minus `kappa(.5,.665)` |
|---|---:|
| long-gap tail | `-.002109713352172871` |
| short-half collar | `-.001899881079182704` |
| same-residue pole tail | `-.001417405659865179` |

Reoptimizing `theta,beta` does not repair the top slice.  Its continuous
frontier is

```text
theta_0(.5,.665)                 =.1618473637309164...,
beta_0(.5,.665)                  =.1573263775949505...,
s(beta_0)-kappa(.5,.665)         =-.0031299134787456.... (5.4)
```

Thus `beta_0<theta_0` at the depth that controls the uniform kill.  The
fixed-cutoff tail saving `.0176307692307692...` beats the first number in
(5.3) but not the last.  With the cutoffs (0.2), all positive-mass errors
beat candidate-specific `kappa(alpha,.665)` only for

```text
alpha<.47150559635909557... .                       (5.5)
```

Optimizing the pole frontier at this fixed `d` reaches only
`alpha<.47721728945766113...`; even the excluded limit `d=2/3` reaches only
the `alpha_*` in (3.5).  A deeper zero does not force a zero at one of these
shallower depths.

The Green ledger is not the obstruction.  At the two ends relevant to this
audit it gives

```text
[.47*d-B_GP(d)]-E_1(.47,d) =.00178281983392718...,
[.50*d-B_GP(d)]-E_1(.50,d) =.02025770743535005....  (5.6)
```

Both carrier slices fit after the raw Green--Poisson bill, with especially
large room at the top.  The failure in (5.4) is therefore a genuine
gap/rational-cover exponent deficit, not an artifact of violating the Green
reserve.  The lower-end `E_1` remains a legitimate promotion budget, but it
cannot be substituted for the top-depth loss in a uniform dual kill.

Consequently the literal short-gap pole is removed structurally by
`beta>theta`, but the accompanying dual error ledger is only a shallow-slice
certificate.  It neither kills the full `.47` band nor declares the old
`.49` route dead.

### 5.4 No arithmetic-reserve gain

The same-state gate remains

```text
Q_ar(q_rho)+K_rho >= epsilon*K_rho+o(K_rho).
```

Nothing in this optimization gives its sign.  The isolated completed block
still has zero reserve, and the positive Green--Poisson mass still has the
wrong polarity when solved for the candidate-relative reserve.  Therefore
even a hypothetical full `QP` disposition would not by itself prove a
strip.

---

## 6. Reproduction

Run

```bash
python3 results/verify_zeta23_carrier_gap_parameter_reoptimization.py
```

The checker replays the aperture conversion, old-slice limiting no-go,
critical slice depth, explicit rational slice certificate, both endpoint
Green reserves, all four positive-mass margins, the promotion-minimum versus
kill-maximum quantifier, the optimized top-depth failure, Peano endpoint,
and surviving multi-gap scale.  It does not reprove the two imported
analytic theorems.
