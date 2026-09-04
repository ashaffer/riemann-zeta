# Uniform zero-free strip goal: final direct attack and formal blocked audit

Date: 2026-08-13.

## 1. Objective and binary result

The objective was to prove, unconditionally and with an audited complete
argument, that there is a fixed `delta>0` such that

```text
zeta(s) != 0 whenever Re(s)>1-delta.                 (1.1)
```

The concrete calibration used in the last iterations was
`delta=10^(-6)`, but any explicit fixed positive value would have met the
goal.

Binary result:

```text
explicit fixed delta proved                          NO
known zero-free region improved                      NO
complete proof artifact                              NO
formal obstruction audited                           COMPLETE
strict disposition                                   BLOCKED
```

This report does not assert that (1.1) is false or impossible.  It records
that the requested theorem has not been proved and that the surviving step
is a genuinely new fixed-power arithmetic cancellation estimate, not an
unfinished normalization, finite computation, or routine use of a known
theorem.

## 2. Final direct attack A: generalized divisor/Voronoi remainder

The complete theta/Kontorovich--Lebedev detector was reduced exactly to

```text
P_T(r)=|xi((1+r+iT)/2)|^2,

Khat_(alpha,eta)(T)
  =1/16 [P_T(alpha+eta)-P_T(alpha-eta)].             (2.1)
```

Writing `u=(1+r)/2` gives

```text
P_T(2u-1)=C_T(u) Z_T(u),
Z_T(u)=zeta(u+iT/2)zeta(u-iT/2),
C_T(u)>0.                                            (2.2)
```

After the two Eisenstein residues, the remaining term is the Mellin moment
of the generalized-divisor remainder `Delta_T`.  Applying the exact
Voronoi formula to smooth truncations of this block gives a dual Bessel
kernel which is a real linear combination of

```text
J_(iT)(4pi sqrt(nx))-J_(-iT)(4pi sqrt(nx))
and K_(iT)(4pi sqrt(nx)).                            (2.3)
```

The kernel is signed.  At `T=0` its continuous limit contains
`-2pi Y_0+4K_0`; the `Y_0` term has infinitely many alternating lobes.
Consequently the exact Voronoi formula is a polarized signed remainder, not
a positive quadratic form.

More decisively, if a zero `rho=beta+i gamma` lies in the proposed strip,
set

```text
r_0=2beta-1,       T=2gamma,       eta=r_0-alpha.
```

Then `0<eta<0.000002`, `P_T(alpha+eta)=P_T(r_0)=0`, while
`P_T(alpha-eta)>=0`; hence the strict inequality in (2.1) fails.  Thus a
uniform relative estimate on the Voronoi remainder strong enough to sign
(2.1) already excludes precisely the zero in question.  Available absolute
divisor/hyperbola estimates, with their nonuniform `T` dependence, do not
give that relative estimate.

## 3. Final direct attack B: actual prime--Laguerre cancellation

For Freitas' generalized Li coefficients, put `tau=2(1-epsilon)` and

```text
f_n(x)=x^(-tau)L_n^(1)(tau log x).                   (3.1)
```

The continuous prime-density integral can be evaluated exactly and is the
coefficient of the completed pole term.  It cancels before the desired sign
is tested.  For every zero mode `x^rho`, the remaining Mellin integral is

```text
integral_1^infinity x^(rho-tau-1)
  L_n^(1)(tau log x) dx
 =1/tau [1-(rho/(rho-tau))^(n+1)].                  (3.2)
```

Hence the full saddle calculation is not merely similar to a zero test: its
remaining saddles are exactly the zero residues

```text
q_tau(rho)^(n+1),   q_tau(rho)=rho/(rho-tau),
|q_tau(rho)|>1 iff Re(rho)>tau/2.                   (3.3)
```

This does yield a finite effective theorem.  If zeros through height `H`
are known to satisfy `Re(rho)<=tau/2`, the paired tail controls a finite
range of degrees of order

```text
n <= c_tau H/[epsilon log H].                       (3.4)
```

Combining (3.4) with a classical shrinking zero-free region gives a very
large finite **effective range in principle** when `epsilon=10^(-6)`, after
inserting explicit zero-free constants and checking the compact low-height
range.  No numerical endpoint is certified in the direct report.  This
cannot give all degrees: a single unexcluded higher zero contributes an
exterior mode in (3.3).  All-degree prime--Laguerre positivity is the desired
strip criterion itself.

## 4. Final direct attack C: localized Nyman collar

The natural localized Nyman coefficient has the exact first-collar scalar

```text
L_n=n^2 g(n)+sum_(1<=j<n)(n-j)mu(n+j)
   =n sum_k mu(k) w(k/n),                            (4.1)

w(x)=1/x          for 0<x<=1,
     2-x          for 1<x<2,
     0            for x>=2.                         (4.2)
```

The full first-collar square splits as

```text
sum_(n<=m<2n)|M(m)+n gamma(n)|^2
 =|L_n|^2/n
  +(1/n)sum_(0<=u<v<n)|sum_(u<j<=v)mu(n+j)|^2.      (4.3)
```

Here `n gamma(n)=n g(n)-M(n)`, so the first-collar value can equivalently
be written `M(m)-M(n)+n g(n)`.  Replacing `n gamma(n)` by `n g(n)` would be
a normalization error and would destroy the exact ANOVA identity.

The bridge term is nonnegative, and the scalar in (4.1) is not removed by
centering.  Modern almost-all short-interval estimates give arbitrary fixed
logarithmic savings after averaging, but not the fixed power required at a
selected `n`.  Such logarithmic bounds do not imply a power-saving
subsequence: for example `exp(-sqrt(log n))` is smaller than every fixed
negative power of `log n` but is still `n^(-o(1))`.

More precisely, if `L(x)=x sum_k mu(k)w(k/x)`, then

```text
integral_0^infinity L(x)x^(-s-2)dx=W(s)/zeta(s),

W(s)=2[(s-1)2^s+1]/[s(s+1)(s-1)].                  (4.4)
```

The factor `W` is nonzero at every nontrivial zeta zero.  Consequently the
dyadic mean-square estimate

```text
sum_(X<=n<2X)|L_n|^2 << X^(3+2b)                   (4.5)
```

which is exactly the scale needed to select the scalar by Markov, already
excludes every zero with real part greater than `b`.  Moreover, an
offending zero `rho` with `Re(rho)>b` forces the complete localized Nyman
quantity to be at least a constant times `n^(Re(rho)-b)` for every
sufficiently large `n`.  Therefore the required `n^(o(1))` estimate on any
unbounded sequence would already prove the strip.  A favorable estimate for
the bridge alone is insufficient because `L_n` survives; even the complete
first collar on a sparse sequence does not control the higher harmonic
cofactors in the full localized quantity.

## 5. Why this is the same blocker, not three missing lemmas

The three final expressions retain the same **kind** of one-dimensional
principal arithmetic obstruction in different transforms; no literal
identity between the three coefficient sequences is asserted:

```text
Voronoi/KL       a signed generalized-divisor Mellin remainder;
tau--Li          an exterior zero residue q_tau(rho)^n;
Nyman            a weighted Mertens / reciprocal-zeta scalar.
```

A fixed-power estimate for any complete version excludes the offending
zero.  Transverse estimates do not suffice:

- positivity of the automorphic differential operator is lost in the
  signed inverse kernel;
- the continuous prime saddle cancels, leaving the zero residues exactly;
- the ANOVA bridge is positive but leaves the uncentered Mertens scalar;
- zero-density estimates can tolerate one zero at a fixed horizontal
  location;
- almost-all short-interval estimates can leave the one selected interval
  or principal mode.

Thus no combination of the audited bounds supplies an independent positive
margin from which (1.1) follows.

## 6. Formal blocked disposition

Parent goal state for goal `019fecce-02e4-7a60-a9a1-47fd6e30a25e` records
this as the third consecutive goal turn: the original user-triggered turn
and two automatic continuation turns.  Independently of that protocol
metadata, the hostile artifacts cited below verify the mathematical
recurrence of the same blocker.  In the final continuation we attacked
the surviving coefficient terms themselves, rather than adding another
equivalent criterion.  The direct transforms above return the offending zero
or weighted Mertens mode residue-for-residue.

The goal is therefore blocked under the goal protocol unless one supplies a
new theorem of at least one of the following forms:

1. a uniform relative signed bound for the complete generalized-divisor
   remainder at all heights;
2. all-degree cancellation in the actual von Mangoldt--Laguerre sum below
   `tau=2`;
3. a fixed-power bound for the **complete** localized Nyman quantity,
   including the selected weighted Mertens scalar, its first-collar bridge,
   and every remaining harmonic cofactor.

Each item is sufficient to move a fixed zero-free boundary and none is
proved in this workspace or by the audited current inputs.  Numerical
verification, finite-degree positivity, and finite-height zero verification
cannot establish the required all-height statement.

Final status after an independent hostile read and the scope patch above:

```text
requested theorem                                      NOT ACHIEVED
same blocking condition repeated for three goal turns  YES
meaningful safe in-scope next step without new input    NO
recommended goal-protocol status                        BLOCKED
```

## 7. Audit trail and strict final verdict

The three final direct artifacts are:

1. `results/ZETA23-GENERALIZED-DIVISOR-VORONOI-MONOTONICITY-GATE-2026-08-13.md`;
2. `results/ZETA23-ACTUAL-PRIME-LAGUERRE-PRINCIPAL-MODE-GATE-2026-08-13.md`;
3. `results/ZETA23-NYMAN-FIRST-COLLAR-SCALAR-MELLIN-EQUIVALENCE-2026-08-13.md`.

The recurrence is independently visible in
`results/ZETA23-UNIFORM-STRIP-GOAL-FINAL-HOSTILE-REFEREE-2026-08-12.md`,
`results/ZETA23-SECOND-UNIFORM-STRIP-ITERATION-HOSTILE-REFEREE-2026-08-12.md`, and
the iteration II--IV synthesis reports: every pass ends at a complete signed
principal Mobius, generalized-divisor, or prime-Laguerre mode requiring a
fixed-power coefficient-specific estimate.

No displayed implication in any of these artifacts supplies such an
estimate.  The Voronoi kernel is signed; the prime-Laguerre result is finite
in degree; and the Nyman estimates are conditional implications whose
premises remain unproved.  Therefore the strict requested disposition is

```text
PROVED                                                   NO
BLOCKED                                                  YES
```

This is a status verdict under the goal protocol, not a theorem that a
uniform strip is false or intrinsically unprovable.
