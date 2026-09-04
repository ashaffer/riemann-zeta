# R176 maximum-information-gain audit

Status: falsification-first theorem and decision-tree audit, 2026-08-30.
This report proves no zero-free strip and does not prove RH.  It corrects the
quantifiers in the proposed R176 contour estimate, proves a new-to-this-project
fixed-contour obstruction from the prime number theorem, and closes the most
natural moving-contour escape by an exact harmonic-access law.

## 1. Binary outcome

The standard fixed-contour reading of R176 should be retired as an
intermediate lemma.  For the actual finite Euler head, the proposed
complementary-boundary upper bound is not merely hard: on every fixed regular
contour used by the argument its left side has the wrong asymptotic size.

For `q=1`, on every fixed admissible domain,

```text
I_C(1,H)/log H
  -> integral_C (1-Re(s))_+ domega_rho(s)
  >= 1-Re(rho)+a omega.                                  (1.1)
```

R176 (7.2) would require the limit superior to be at most `a omega-c`.
It therefore misses by at least `1-Re(rho)+c`.

For arbitrary integer `q=q(H)>=2`, every fixed smooth contour having a
transverse left subarc instead satisfies

```text
I_C(q,H) >> (q-1) H^epsilon/(log H)^2,                    (1.2)
```

which is much larger than `q log H`.  The extra nonlinear support is exactly
what amplifies the positive phases of the finite Euler head.

Thus a fixed regular domain cannot support the proposed estimate for any
sequence of integers `q` and unbounded `H`.  This closes the ordinary smooth
fixed-contour branch.  It does not disprove R176's intended implication: a
conditional estimate which fails at every candidate zero is simply another
certificate that no such zero exists.  The point is that the certificate has
not reduced the difficulty.  A singular fixed Jordan boundary not covered by
the transverse-arc proposition below remains a separate low-regularity
loophole rather than being silently ruled out.

The obvious remaining experiment was to let `D_H` follow the small finite-head
phases on the scale `1/log H`.  Proposition 7.1 below closes its bounded-
lemniscate form: any such corridor has right harmonic measure `O(1/log H)`.
Contours accepting the critical polynomial growth forced by harmonic measure
remain logically possible, but proving a strict deficit on them is precisely
the original zeta-specific estimate rather than a simpler geometric lemma.

## 2. The exact theorem card

Fix `0<eta_0<1/2`.  For every hypothetical zeta zero

```text
rho=beta+i gamma,       1-eta_0<beta<1,                   (2.1)
```

choose, before `H` tends to infinity, a bounded target-isolating Jordan domain
`D_rho` such that

* `rho` lies in `D_rho` and is the only zeta zero in its closure;
* `1` is not in the closure;
* the closure lies in `Re(s)>0`;
* `E_rho` is a nonempty boundary arc in `Re(s)>=1+a_rho`, where
  `a_rho>0`;
* `C_rho=partial D_rho\E_rho`; and
* `omega_rho=omega(rho,E_rho;D_rho)` lies strictly between zero and one.

Put

```text
P_H(s)=product_(p<=H)(1-p^(-s)),
F_H(s)=zeta(s)P_H(s),
B_(q,H)(s)=(1-F_H(s))^(q-1) F_H'(s)/F_H(s),              (2.2)

I_C(q,H)=integral_C log^+|(s-rho)B_(q,H)(s)|
                         domega_(rho,D_rho)(s).           (2.3)
```

The residue of `B_(q,H)` at a zero of multiplicity `m_rho` is `m_rho`.
The right Euler tail and harmonic measure give the precise lower bound

```text
I_C(q,H) >= q a_rho omega_rho log H
             -q omega_rho log C_(a_rho)
             -omega_rho log log H
             -omega_rho log R_(D_rho)
             +log|m_rho|.                                (2.4)
```

A minimal sufficient open hypothesis would be: for some `c_rho>0`, some
unbounded sequence `H_n`, and integers `q_n>=1`,

```text
I_C(q_n,H_n)
 <=q_n a_rho omega_rho log H_n-c_rho q_n log H_n.         (2.5)
```

Combining (2.4) and (2.5), then dividing by `q_n log H_n`, excludes `rho`.
Applying this separately to every zero in (2.1) proves the selected strip.

Three quantifier corrections are important.

1. `H_n -> infinity` must be stated.
2. The target-zero region must be stated.  Over `1/2<beta<1`, the estimate is
   RH-strength by functional-equation symmetry; over `1-eta_0<beta<1`, it is
   fixed-strip strength.
3. The constants and domain need not be uniform across distinct zeros.
   Positive `c_rho` and one fixed `D_rho` per target suffice.  Demanding a
   uniform zero-isolation radius imports an unnecessary and possibly harder
   assertion.

If `D=D_n` moves, the hidden error in (2.4) must instead be controlled
explicitly.  A convenient sufficient condition is

```text
q_n omega_n log C_(a_n)
 +omega_n log(R_(D_n) log H_n)=o(q_n log H_n).             (2.6)
```

Also, because `I_C>=0`, a nonvacuous version of (2.5) requires
`a_n omega_n>c_rho` eventually.  Quantifying over every admissible contour is
impossible: thin tubes can make `omega_n` arbitrarily small.

## 3. Logical strength after the quantifiers are frozen

Let `U(rho)` denote the existence of data satisfying (2.5).

| Target set for `rho` | Strength of `U(rho)` for every target zero |
|---|---|
| `1-eta_0<Re(rho)<1` | equivalent, as a zero-conditioned proposition, to that strip |
| `1/2<Re(rho)<1` | RH-equivalent by symmetry |
| a sequence with `Re(rho)->1` | equivalent to existence of some fixed strip |
| arbitrary points, rather than zeros | stronger and unsupported |

The converse implications in this table are vacuous when the target set has
no zeros.  The PNT obstruction below says more for fixed regular domains:
`U(rho)` is false at every candidate point, whether or not it is a zero.
Consequently the universally zero-conditioned assertion in that contour class
is literally a reformulation of zero absence, not yet an independently
motivated weaker theorem.

## 4. Generic analytic information is already saturated

The harmonic-measure lower bound is sharp.  In a conformal disk model, let
the controlled arc have harmonic mass `omega`, and prescribe the boundary
logarithm of an outer function `A_T` by

```text
log|A_T|=-T(1-omega) on E,
log|A_T|= T omega    on C.                                (4.1)
```

Its harmonic mean at the center is zero, so it can be normalized by
`A_T(rho)=1`.  Then `B_T=A_T/(s-rho)` has residue one.  Choosing

```text
T=q a log H/(1-omega)                                    (4.2)
```

makes the right size `H^(-qa)` and gives exactly

```text
integral_C log^+|(s-rho)B_T| domega=qa omega log H.       (4.3)
```

There is no generic `-c q log H` reserve.  R176 also gives a local inverse
which realizes every such residue-one meromorphic function in the nonlinear
form `(1-F)^(q-1)F'/F`.  Hence meromorphy, a retained residue, one-sided
smallness, and the nonlinear germ do not imply (2.5).

This agrees with the nearest primary literature.  Harmonic-majorant and
Poisson-balayage theory characterizes when logarithmic data have a majorant;
it does not create a reverse deficit.  Nevanlinna theory for Dirichlet series
uses global torus or vertical means, not harmonic measure conditioned at one
hypothetical zero.  Finite-Euler-product approximation to zeta is available
under RH and away from zeros, whereas R176 asks for control selected by a
hypothetical zero itself.

Relevant primary sources are:

* A. Hartmann, X. Massaneda, A. Nicolau, and P. Thomas,
  [*Interpolation in the Nevanlinna class and harmonic majorants*](https://arxiv.org/abs/math/0306093);
* K. Guo, J. Ni, and Q. Zhou,
  [*Nevanlinna class, Dirichlet series and Szegő's problem*](https://arxiv.org/abs/2201.01993);
* S. M. Gonek,
  [*Finite Euler products and the Riemann Hypothesis*](https://arxiv.org/abs/0704.3448).

## 5. The `q=1` fixed-contour theorem

### Proposition 5.1

Let `D,rho,E,C,a,omega` be fixed as in Section 2, with the boundary disjoint
from the zeta divisor and the pole.  Assume the boundary logarithms below are
harmonic-measure integrable.  Then

```text
lim_(H->infinity) I_C(1,H)/log H
 =integral_C (1-Re(s))_+ domega_rho(s).                   (5.1)
```

In particular,

```text
lim I_C(1,H)/log H >=1-beta+a omega.                      (5.2)
```

Therefore (2.5) is false for `q=1` on every fixed admissible domain.

### Proof

Logarithmic differentiation gives

```text
F_H'/F_H=zeta'/zeta
 +sum_(p<=H)sum_(k>=1)(log p)p^(-ks).                     (5.3)
```

On every compact subset of `0<Re(s)<1` avoiding the zeta divisor, the prime
number theorem and partial summation give

```text
F_H'(s)/F_H(s)=H^(1-s)/(1-s)(1+o(1)).                    (5.4)
```

The terms `k>=2` are lower order because `Re(s)>0`; `zeta'/zeta` is bounded
on the fixed boundary.  For fixed `s` on `Re(s)>1`, the logarithmic
derivative tends to zero, and on `Re(s)=1`, away from `s=1`, its positive
logarithm is `o(log H)`.  The elementary bound

```text
log^+|F_H'/F_H| <=(1-Re(s))_+ log H+O_D(log log H)         (5.5)
```

supplies domination.  The factor `s-rho` changes the logarithm by `O_D(1)`.
This proves (5.1).

Finally, harmonicity of `1-Re(s)` gives

```text
integral_C (1-Re(s))_+ domega
 >=integral_C (1-Re(s)) domega
 =1-beta-integral_E (1-Re(s)) domega
 >=1-beta+a omega.                                       (5.6)
```

This proves (5.2).

## 6. The nonlinear fixed-contour obstruction

### Proposition 6.1

Assume in addition that `C` contains a fixed `C^(1,alpha)` subarc `Gamma`
on which

```text
0<Re(s)<=1-epsilon,
|d Im(s(t))/dt|>=eta>0,                                  (6.1)
```

and harmonic measure has density bounded below with respect to arclength.
Then, uniformly for every integer-valued `q(H)>=2`,

```text
I_C(q(H),H) >> (q(H)-1)H^epsilon/(log H)^2.               (6.2)
```

Consequently (2.5) fails by an unbounded factor on every such fixed contour.

### Proof sketch with the only regularity input exposed

Uniformly on `Gamma`, PNT and partial summation give

```text
log P_H(s)
 =-H^(1-s)/((1-s)log H)(1+o(1)),                         (6.3)

F_H'/F_H=H^(1-s)/(1-s)(1+o(1)).                          (6.4)
```

As `Im(s)` moves along `Gamma`, the phase in (6.3) moves at speed comparable
to `log H`.  On a subarc of length comparable to `1/log H`, a fixed positive
fraction of one phase period satisfies

```text
Re log P_H(s) >> H^epsilon/log H.                         (6.5)
```

There `|F_H|` is exponentially large, since zeta is bounded above and below
on the fixed zero-free arc, and

```text
log|1-F_H| >> H^epsilon/log H.                            (6.6)
```

Equations (6.4)--(6.6), the lower harmonic-measure density, and integration
over a set of length `>>1/log H` prove (6.2).  Since
`H^epsilon/(log H)^3 -> infinity`, (6.2) dominates every `O(q log H)` target.

The stated smooth transverse-arc hypothesis is deliberate.  Proposition 5.1
does not need it.  Every globally `C^(1,alpha)` target domain has such an arc:
at a leftmost boundary point `Re(s)<beta<1`, regularity makes the tangent
vertical, and the Poisson kernel is locally positive and continuous.  A bare
Jordan boundary can instead be fractal and need not have a usable arclength
density.  That separate low-regularity loophole should not be hidden in the
theorem statement.

### Numerical sign check

As a check on signs rather than a proof, the exact prime product was sampled
on `s=0.30+it`, `10<=t<=11`.  The following are unweighted arc averages:

| `H` | mean `(Re log P_H)_+` | PNT main-term prediction | mean `log^+|B_(2,H)|` |
|---:|---:|---:|---:|
| 500 | 0.179 | 0.366 | 2.286 |
| 3,000 | 0.975 | 1.198 | 4.679 |
| 10,000 | 2.174 | 2.477 | 6.393 |
| 30,000 | 4.558 | 4.848 | 9.639 |

The finite range has a visible transient from the small primes, but the
positive head phase approaches the predicted main term and the nonlinear
logarithm grows in the asserted direction.

## 7. The moving-lemniscate escape also collapses

The natural phase-following object is the component of

```text
{s: |F_H(s)|<K},          K>1,                            (7.1)
```

which contains `rho`.  Initially this looked like the highest-information
survivor: its level boundary controls the nonlinear factor while a corridor
might connect the target to a right cap.  The two-constants theorem applied
to the nonlinear base itself gives an exact falsifier.

### Proposition 7.1 -- nonlinear harmonic-access law

Fix `H` and any target-isolating domain `D`, possibly depending on `H` or on a
later choice of `q`, for which the boundary logarithms are integrable.  If
`rho` is a target zero, then

```text
L_H:=integral_C log^+|1-F_H(s)| domega_rho(s)
    >=a omega log H-omega log C_a.                        (7.2)
```

This follows without the logarithmic derivative.  Put

```text
Y_H=1-F_H.                                                 (7.3)
```

At the retained zero, `Y_H(rho)=1`, while on `E` the Euler-tail estimate gives
`|Y_H|<=C_a H^(-a)`.  Subharmonicity and harmonic measure therefore give

```text
0=log|Y_H(rho)|
 <=integral_E log|Y_H| domega+integral_C log|Y_H| domega
 <=omega(log C_a-a log H)+L_H,                            (7.4)
```

which is (7.2).  Standard epsilon regularization handles boundary zeros of
`Y_H`.  Equivalently, under the stronger boundary integrability assumptions,
one can divide (2.4) by `q` and let `q` tend to infinity; the direct proof
shows that neither a common contour limit nor derivative control is needed.

If `|F_H|<=K` on `C`, then

```text
L_H <=(1-omega)log(1+K).                                  (7.5)
```

Combining (7.2) and (7.5) yields the explicit access bound

```text
omega
 <= log(1+K)/[a log H-log C_a+log(1+K)]
 =O_(a,K)(1/log H).                                       (7.6)
```

Here the displayed fraction is asserted once its denominator is positive,
which holds for all sufficiently large `H` when `a` and `K` are fixed.

Thus alternative C in the proposed lemniscate test is forced: every bounded
`F_H` corridor from a retained zero to a fixed right cap loses its harmonic
access.  Neither a derivative estimate nor a smooth-contour assumption is
needed for this conclusion.

More generally, if `|F_H|<=H^(lambda+o(1))` on `C`, (7.2) forces

```text
lambda+o(1) >=a omega/(1-omega)-O(1/log H).               (7.7)
```

This is exactly the harmonic-measure growth exponent already attained by
outer functions.  A moving contour may redistribute the bill, but it cannot
replace it by bounded or subcritical polynomial growth.

### Ground-truth numerical check

A coarse minimax grid around the first critical-line zero initially made the
sublevel escape look plausible.  On

```text
0.2<=Re(s)<=1.3,
|Im(s)-14.134725...|<=2,                                  (7.8)
```

the smallest grid barrier connecting the zero to `Re(s)=1.3` was close to
`K=1` for `H=30,100,300,1000,3000,30000`; at `H=10000` the minimizing path
left the finite vertical window.  A discrete harmonic-measure proxy at
`K=1.2` ranged from about `0.005` to `0.036` over these modest values.

This is not contrary evidence to (7.6).  The grid spacing was `0.025`, while
the prime phase scale is already about `1/log H` and the local lemniscate
neck can be exponentially thinner when `|P_H(rho)|` is large.  The experiment
therefore identified a numerical failure mode: fixed-resolution connectivity
substantially overestimates true harmonic access.  Proposition 7.1 supplies
the asymptotic conclusion without extrapolating the grid.

## 8. What remains after the access law

Any mildly moving family with a uniformly regular transverse subsequence
inherits Proposition 6.1.  Singular fixed boundaries and genuinely moving
families also satisfy the universal access law (7.2).  A remaining contour
would have to meet all of the following conditions.

1. **Critical rather than small head.**  It must accept complementary growth
   at least `H^[a omega/(1-omega)-o(1)]`; bounded lemniscates are closed.
2. **Strict arithmetic deficit.**  Despite that necessary growth, the joint
   quantity `(1-F_H)^(q-1)F_H'/F_H` must save `c q log H` in harmonic mean.
   Generic factorwise estimates lose the required correlation.
3. **Right access.**  It must retain `a_H omega_H>c>0`; otherwise the proposed
   upper bound has a negative right side.
4. **Target isolation.**  Its closure must contain the selected zero and no
   other zeta zero and must avoid the pole.
5. **Geometry accounting.**  The errors in (2.6), boundary integrability, and
   smoothing losses must remain subordinate to `q log H`.

Condition 2 is just the original coefficient-specific R176 estimate after
the geometric degrees of freedom have paid their unavoidable bill.  No
strictly weaker, independently testable moving-contour lemma remains in this
framework.

## 9. Updated decision tree

```text
R176 complementary log-mean
|
+-- exact quantifiers frozen
|   +-- per-zero fixed geometry is enough
|   +-- uniform zero separation was an unnecessary demand
|   `-- all off-line targets means RH-strength, not strip-strength
|
+-- generic complex analysis
|   `-- outer functions saturate harmonic measure: CLOSED
|
+-- fixed actual-zeta contour
|   +-- q=1: every admissible fixed boundary is CLOSED
|   `-- q>=2: every regular transverse fixed boundary is CLOSED
|
+-- bounded/subcritical phase-following contour
|   `-- omega=O(1/log H), by the two-constants access law: CLOSED
|
`-- critical-growth singular or moving contour
    `-- strict joint arithmetic deficit: ORIGINAL OPEN TARGET
```

The information gain is substantial even though no zero-free theorem was
proved.  Uniform zero separation was removed as a false prerequisite; smooth
fixed contours were closed by PNT; and the most natural moving-contour escape
was closed by (7.6).  What remains is no longer a geometric subproblem but the
original zeta-specific strict deficit, with logical strength equal to the
selected zero-exclusion conclusion.  R176 should therefore be deprioritized
unless an independent prime-phase theorem supplies that deficit.  Further
contour optimization by itself has essentially zero expected information
gain.
