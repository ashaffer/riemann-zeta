# Logical strength of the Pick, prime-hull, Schur-angle, and sinh-tent gates

Status: quantified implication audit and fixed-depth theorem card,
2026-08-12.  No zero-free strip, RH statement, or new bound on a zeta zero
is proved here.

## 1. Verdict

The four current gates live at three different logical levels and should not
be described as if they were interchangeable.

1. The global half-disk Pick theorem is a **geometric state-construction
   lemma**.  Even with compact transfer it controls the loss caused by
   collateral zero rows; it says nothing about the completed prime form.
2. The twisted prime-hull inradius and the aggregate Schur angle are
   **arithmetic-admission lemmas**.  The inradius enforces all chosen
   cross-prime equalities, whereas the Schur angle preserves the carrier
   after one cross-leg aggregate equality.  Neither statement controls the
   same-leg arithmetic terms.  Neither one alone is a zero-free theorem.
3. Uniform completed one-square positivity is on the **RH side** of the
   hierarchy.  RH implies it for every autocorrelation test.  A fixed strip
   does not imply it in the class of real symmetric order-one completed
   functions: the matched-quartet polynomial gives a fixed-strip function
   with a negative centered sinh-tent square.  The converse for the raw
   two-parameter sinh-tent family has not been proved, so it must not be
   called an RH equivalence.

The closing arithmetic statement is smaller than positivity.  Once a
deterministic candidate-conditioned state has an independently certified
negative geometric carrier `K_rho`, a convenient sufficient scalar lower
edge is

```text
Q_ar(q_rho) >= -o(K_rho).                            (1.1)
```

This is not literally the weakest numerical edge.  If the remote and
transfer error is `err_rho=o(K_rho)`, the exact requirement is

```text
Q_ar(q_rho)+K_rho > err_rho;                         (1.2)
```

for all sufficiently high candidates.  In particular,
`Q_ar(q_rho)>=-(1-epsilon)K_rho` for one fixed `epsilon>0` is enough.
The `-o(K_rho)` version is a stronger, cleaner power-saving theorem card.

For one fixed depth band this is fixed-strip scale, not RH scale.  Requiring
the analogous closure for every positive depth is RH scale.

## 2. Quantifier normalization

For a nontrivial zero `rho=beta+i*gamma`, write

```text
alpha(rho)=beta-1/2.
```

For `0<alpha_0<1/2`, let

```text
ZF(alpha_0): no zeta zero has beta>=1/2+alpha_0.     (2.1)
```

After the finite low-height range is handled, `ZF(alpha_0)` is a uniform
zero-free strip.  RH is the collection of statements `ZF(alpha_0)` for
every `alpha_0>0`.  Thus the quantifier distinction is exact:

```text
one fixed alpha_0<1/2       fixed-strip scale;
every alpha_0>0             RH scale.               (2.2)
```

A theorem only for `alpha in [0.49,1/2]` would already exclude
`beta>=0.99`.  There is no reason to demand control as `alpha` tends to zero
in a first strip attack.

Candidate-conditioned assertions require care.  Under `ZF(alpha_0)` there
is no candidate in the band, so the reverse implication from the strip to
such an assertion is merely vacuous.  It supplies no estimate for the Pick
problem, the prime hull, or a Schur angle.  Consequently these implications
should always be read in the contradiction direction: assume one candidate
exists, construct its state without inspecting the arithmetic sign, prove
(1.1), and contradict the explicit formula.

## 3. A fixed-depth carrier budget

Under ideal phase-cell compression and balanced two-leg splitting, the
proved potential calculation gives

```text
E_1(alpha,d,a)
 =alpha*(d-1/2)*(1-R(y)),

y=pi*a/[alpha*(2*d-1)],
R(y)=[y*log(1+y^(-2))+2*atan(y)]/pi.                (3.1)
```

This is the carrier exponent after the one-product divisor bill, before the
still-open compact and arithmetic transfers.  It is increasing in `alpha`.
Indeed

```text
R'(y)=log(1+y^(-2))/pi,

d/dalpha [alpha*(1-R(C/alpha))]
 =1-R(y)+y*R'(y)
 =1-2*atan(y)/pi>0.                                 (3.2)
```

The packet and prime-aperture constructions require the strict inequality
`d<2/3`; the endpoint `d=2/3` is only a limiting ledger and cannot be used
as a theorem parameter.  Take, for example, the fixed interior value

```text
d_0=0.66,       a=0.10076,       alpha_0=0.49,

E_0:=min_(0.49<=alpha<1/2)E_1(alpha,d_0,a)
    =E_1(0.49,0.66,0.10076)
    =0.0119000134....                                (3.3)
```

The inadmissible limiting value as `d` increases to `2/3` is
`0.0128736062...`; it is useful for optimization diagnostics but not as the
reserve in a theorem card.

Therefore a complete implementation may spend a fixed loss

```text
X^(-kappa+o(1)),       any kappa<E_0,               (3.4)
```

and still leave a power-sized contradiction.  A subpower loss is sufficient
but is not necessary.

For the prime-moment notation `Y=T^(d_0)=X^(d_0+o(1))`, an aligned mass

```text
w_0>=Y^(-kappa_Y+o(1))                              (3.5)
```

costs `X^(-d_0*kappa_Y+o(1))`.  At (3.3), the actual threshold is

```text
kappa_Y<E_0/d_0=0.0180303234....                     (3.6)
```

Thus the requested `Y^(-o(1))` inradius is quantitatively stronger than the
first strip attack needs.  The observed generic square-root scale
`Y^(-1/2+o(1))` and the proved support-separation scale `Y^(-1)` are still
far outside the budget.

The same bookkeeping applies to one Schur projection.  If
`sin^2(angle)>=X^(-kappa+o(1))`, the left capacity squared and hence the
harmonic-mean carrier lose at most that factor.  Any `kappa<E_0` is enough,
provided the same-leg terms and compact transfer are separately closed.

## 4. Gate-by-gate implication audit

### 4.1 Global half-disk Pick compression

Let `G_HD(alpha_0)` denote the proposed theorem which, for every
carrier-relevant actual list attached to a maximal-depth candidate with
`alpha>=alpha_0`, obtains the half-product potential up to `X^o(1)` and
survives the finite-support transfer.

Its output is a state with a large selected negative zero carrier and
controlled collateral zero rows.  It has no prime, pole, or gamma sign in
its conclusion.  Thus the present explicit-formula chain establishes only

```text
G_HD(alpha_0) + arithmetic lower edge
                           implies ZF(alpha_0);      (4.1)
G_HD(alpha_0) alone       [no closing implication proved].
```

There are two quantifier versions which must not be conflated.  The
actual-list assertion above is candidate-conditioned, so `ZF(alpha_0)`
implies it vacuously.  The unrestricted half-disk problem over arbitrary
node lists is instead a coefficient-free interpolation statement; a
zero-free theorem supplies no nonvacuous estimate for those arbitrary
lists.  Conversely, an abstract interpolation theorem would still leave
the actual completed arithmetic form untouched.  No formal independence
claim is intended here, and neither the growing actual-list theorem nor the
unrestricted global half-product theorem has been proved or falsified.

The exact alternating lattice and the exact five-point jet fixture reinforce
this classification.  They prove nontrivial facts about the Pick optimum in
opposite local regimes without deciding any zero location; in particular,
the local jet loss has not been proved to multiply across a growing list.

### 4.2 Twisted prime-moment transverse inradius

For the actual balanced twist `U`, the inradius condition is a sufficient
way to solve

```text
-r*Psi(0) in conv{Psi(eta):Y<=abs(eta)<=T}.          (4.2)
```

With a quantitative central mass and a compact two-cascade transfer, it
annihilates every listed **cross-leg** prime row while retaining a known
fraction of the causal carrier.  It does not control:

```text
the same-leg prime terms;
the completed pole/gamma ledger;
the collateral zero rows;
the compact realization of the growing inner cascades.       (4.3)
```

Accordingly no standalone closing implication has been established from
the inradius statement as currently formulated.  Its arithmetic
difficulty can nevertheless exceed that of a strip: it asks for a
well-conditioned simultaneous return of a growing prime-log orbit.  Logical
weakness and proof difficulty are different notions here.

A universal theorem over arbitrary growing twists is also the wrong target.
Boundary ray solutions are destroyed by arbitrarily small transverse phase
rotations, and a growing all-pass cascade can mimic a delay on a finite
band.  The only defensible version is for the single balanced twist selected
beforehand from the actual candidate geometry, or for a family with an
independently proved transverse margin.

### 4.3 Aggregate Schur angle

For fixed right leg `f`, the exact identity is

```text
sigma_agg(f)^2
 =||a||^2
  -|<a,P_E P_ar f>|^2/||P_E P_ar f||^2.             (4.4)
```

As in the source theorem, the quotient is defined to be zero when
`P_E P_ar f=0`; in that case the aggregate constraint is vacuous.

Thus a quantitative angle controls exactly the carrier lost when one
complex aggregate equality is imposed; the real sign/equality version costs
only one real direction.  It is strictly more targeted than pointwise
nulling of every prime row.

But (4.4) is not an arithmetic sign theorem.  It removes one cross-leg
aggregate and leaves the same-leg terms.  Generic Hilbert geometry cannot
prove it: in an abstract model one may set `P_E P_ar f` parallel to `a`.
The desired statement must therefore use the actual von Mangoldt operator
and the predetermined candidate state.  Even then it is one component of
(1.1), not a replacement for (1.1).

### 4.4 Centered sinh-tent completed square

Let `W_sinh` be nonnegativity of the complete unprojected centered
sinh-tent square for all its admissible parameters.  RH implies `W_sinh`:
on RH every zero spectral parameter is real and

```text
K(t)=|F(t)|^2>=0.                                   (4.5)
```

The reverse implication is not presently proved because this restricted
two-parameter autocorrelation family has not been shown to separate every
possible off-line zero multiset.  Calling `W_sinh` equivalent to RH would
therefore overstate the result.

On the other hand, a fixed strip does not imply `W_sinh` from functional
equation, reality, and order.  Let `Xi_0` be a real symmetric order-one
completed function with critical-line zeros and put

```text
Xi_N(s)=Xi_0(s)*H_(alpha,gamma)(s)^N,                (4.6)
```

where `H_(alpha,gamma)` is the matched-quartet polynomial from the
functional-equation no-go theorem.  All zeros of `Xi_N` lie in the fixed
strip

```text
1/2-alpha<=Re(s)<=1/2+alpha<1,                      (4.7)
```

but the quartet changes the centered square by

```text
N*[-2*A_(L,alpha)^2+2*Re K(2*gamma+i*alpha)]<0      (4.8)
```

once `gamma` is above the explicit threshold.  Taking `N` large overwhelms
the background.  This is a relative countermodel in the structural class,
not an Euler-product counterexample to zeta.  It proves that uniform
sinh-tent positivity asks for Euler-coefficient information stronger than a
bare fixed strip.

The projected candidate-conditioned version is different.  It only needs
the lower edge (1.1) for one state and one fixed depth band.  That is the
appropriate first-strip target.

## 5. The exact closing package

Fix `alpha_0=0.49` and the admissible interior separation `d_0=0.66`.
Suppose that for every sufficiently high hypothetical
zeta zero with `alpha in [alpha_0,1/2]`, a deterministic construction,
chosen before inspecting the completed arithmetic value, produces a compact
state `q_rho` such that

```text
zero-side target plus collaterals <=-K_rho,
K_rho>=X^(E_0-o(1)),
remote zero tail=o(K_rho).                          (5.1)
```

Suppose also that the exact completed arithmetic form on that same state
satisfies either the fractional lower edge

```text
Q_ar(q_rho)>=-(1-epsilon)*K_rho                     (5.2)
```

for one fixed `epsilon>0`, uniformly in the candidate geometry, or the
stronger power-saving edge

```text
Q_ar(q_rho)>=-X^(E_0-sigma).                        (5.3)
```

Here `sigma>0` is fixed.  The explicit formula identifies the two sides.
Equation (5.1), together with either (5.2) or (5.3), gives a contradiction
for large height, proving `ZF(0.49)` and hence a fixed zero-free strip
`Re(s)<0.99` after the finite range is checked.

This implication is the honest sense in which the package is
"strip-strength."  The pieces separately are not.  Repeating the theorem
for every fixed `alpha_0>0` would prove RH; no such all-depth quantifier is
needed now.

If an arithmetic admission step spends `X^(-kappa+o(1))`, replace `E_0` in
(5.1) and (5.3) by `E_0-kappa`.  The power-ledger closure condition is
`kappa<E_0` plus a positive residual saving.

There is an important logical caveat.  Once (5.1) is independently proved,
the universally quantified candidate-relative lower edge (5.2) or (5.3) is
classically equivalent in truth value to `ZF(0.49)`: the forward direction
is the contradiction above, and the reverse direction is vacuous because
there is then no candidate.  Calling (5.2) the *minimal arithmetic closure*
describes the amount and shape of analytic information requested, not a
formal logical weakening of the strip.  Its noncircular content can only be
in a proof that does not import the strip or an equivalent positivity
criterion.

## 6. Weakest noncircular theorem card

The recommended arithmetic target is:

> **Candidate-relative completed one-square lower edge.**  Fix
> `alpha_0=0.49`, `d_0=0.66`, the deterministic balanced half-disk optimizer,
> and a geometry-only tie-breaker.  Conditional only on
> `zeta(1/2+alpha+i*gamma)=0` with
> `alpha in [alpha_0,1/2]`, prove the finite-aperture, Hahn-projected
> completed form on the resulting state is at least
> `-(1-epsilon)K_rho` for some fixed `epsilon>0`.  The cleaner but stronger
> power-saving target is `-X^(E_0-sigma)` for some fixed `sigma>0`.

This asks for strictly less completed-form information than the first three
statements below and avoids the much larger system of constraints in the
last two:

```text
pointwise positivity of the completed multiplier;
positivity of the complete Pick/Loewner matrix;
a whole-matrix KMT lower edge;
nulling every prime-power row;
uniform sinh-tent positivity for every depth.        (6.1)
```

The current cross-leg nulling hypothesis and (1.1) are not formally ordered
until the same-leg completion is added: cross-leg nulling alone need not
imply (1.1).  The point is that (1.1) is the exact final scalar needed, while
row-by-row nulling is an overconstrained construction route to part of it.

It is noncircular only if all of these safeguards are enforced:

1. the depth band and `sigma` are fixed in advance;
2. the state is selected from zero geometry before its arithmetic value is
   evaluated;
3. `K_rho` is certified from the divisor/Pick construction, not defined as
   the observed negative eigenvalue of the completed form;
4. no metric, branch coloring, companion, or Schur direction is refitted
   after seeing the von Mangoldt operator; and
5. the proof may use the candidate equation `zeta(rho)=0`, but not a
   zero-free hypothesis in the band being excluded.

## 7. Research decision

The logical ordering of the live attacks is now:

```text
global half-disk plus compact transfer
          -> geometric carrier K_rho;

twisted inradius
          -> expensive sufficient cross-prime nulling;

aggregate Schur angle
          -> cheaper cross-leg admission;

candidate-relative completed one-square lower edge
          -> exact minimal arithmetic closure;

geometric carrier plus minimal arithmetic closure
          -> one fixed strip.                       (7.1)
```

The direct one-square lower edge should receive priority.  The inradius
program should continue only if the actual optimized loss is below the
explicit threshold (3.6), and the aggregate-angle program only if the full
same-leg completion is tracked in the same computation.  A proof of raw
uniform sinh-tent positivity would be spectacular, but it is an
unnecessarily RH-sided target for the first strip.

Primary dependencies:

- `ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`;
- `ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md`;
- `ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`;
- `ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`;
- `ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`.
