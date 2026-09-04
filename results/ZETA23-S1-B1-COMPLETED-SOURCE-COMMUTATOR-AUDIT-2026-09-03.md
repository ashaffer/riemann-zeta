# ZETA23 S1-B1 completed-source commutator audit

Date: 2026-09-03.

## Outcome

S1-B1 fails the strict-adapter admission test.  The literal arithmetic
commutator is either zero after an interior prefix compression, exactly the
original prime source on a narrow shell, or accompanied by an uncontrolled
divisor-boundary tail.  Its completion-sensitive repair is an exact and
off-critical-faithful reflection formula, but it is only a scalar/reflected
coordinate of the original completed source.  Finite iteration inside the
multiplier/reflection crossed product creates no third source channel.

This is a negative routing result, not a zero-free estimate.  It proves no
uniform zero-free strip and no statement of RH.  The elementary identities
below are **PROJECT_SYNTHESIS**; no literature-level novelty is claimed.

The precommitted S1 sprint has now tested its two concrete candidates:

- S1-A0, the naked `C*1=Lambda` re-expansion, was tautological; and
- S1-B1, the completed-source commutator, is not a strict adapter.

This closes only the finite window/reflection commutator class tested here.
It does not prove that every possible coefficient--completion law or every
complete two-scale inequality is impossible.  Under the September decision
rule, the next bounded experiment is the single QP/Turan source-fiber
bifurcation.

## 1. Theorem passport

The target remains the complete fixed-window R71/R128 energy

\[
 O_{\rm full}=E_I^Q
 \le X^{1-\kappa+o(1)},\qquad 0<\kappa\le1,
\]

on every block of one fixed regular partition.  R180 shows that this is
uniform-strip strength.  The source coefficient is

\[
 C(n)=(\mu*\Lambda)(n)=-\mu(n)\log n,
 \qquad C*\mathbf 1=\Lambda.
\]

The R71 product weight is

\[
 f_R(n)=n^{-1/2}V_Q(R-\log n),
\]

and the complete field is

\[
 D_{V_Q}(R)=\sum_q C(q)\sum_m f_R(qm).
\]

Thus a valid S1 adapter must preserve the product weight, the output-block
localizer, every cofactor/gcd/conductor/profile/orientation class, and all
quadratic cross terms.  It must also produce a genuinely smaller controlled
term rather than rename `O_full`.

There is no route-native operator called `W_R`.  Below, `W=M_w` means
arithmetic multiplication by an explicitly declared sequence `w`; it must
not be confused with the detector window or with the external block
localizer in `R`.

## 2. Literal arithmetic commutator

Define Dirichlet convolution by `C` as

\[
 (T_Ca)(n)=\sum_{d\mid n}C(d)a(n/d)
\]

and use the convention `[W,T_C]=WT_C-T_CW`.  Then, pointwise,

\[
 \boxed{
 ([W,T_C]\mathbf1)(n)
 =\sum_{d\mid n}C(d)\bigl(w(n)-w(n/d)\bigr).}
 \tag{2.1}
\]

Since `T_C 1=Lambda`, one also has

\[
 \boxed{W\Lambda=[W,T_C]\mathbf1+T_Cw.}
 \tag{2.2}
\]

Equation (2.2) is only `C*1=Lambda` distributed across a window.  Moreover,
`T_Cw` puts the window on the inner factor `m`, whereas R128 requires the
product weight at `dm`.  Without an outer cutoff it also has an unbounded
cofactor tail.

### 2.1 Prefixes and narrow shells

For the prefix `w=1_{n\le X}`, (2.1) vanishes for `n\le X`.  Compression back
to the prefix therefore kills the commutator exactly; all nonzero terms are
boundary leakage outside it.

For a hard shell `I=[A,B]`, let `W=M_{1_I}` and let `P_B` restrict the output
to `n\le B`.  If `B<2A`, then

\[
 P_BT_C1_I=0.
\]

Indeed, `m in I`, `m|n`, and `n\le B<2A` force `n/m=1`, while `C(1)=0`.
Consequently

\[
 \boxed{P_B[W,T_C]\mathbf1=1_I\Lambda.}
 \tag{2.3}
\]

The projected commutator is nonzero precisely because it is the original
source.  Globally,

\[
 (I-P_B)[W,T_C]\mathbf1=-(I-P_B)T_C1_I,
\]

and the exterior leakage is real: if `r in I` and `p>B` are primes, then
`(T_C1_I)(pr)=C(p)=log p`.  Wider or smooth windows replace this by a family
of translated divisor collars.  Since the full `C` has arbitrarily large
support, those collars are not uniformly thin.

At quadratic level, writing the two terms in (2.2) as `A+B` requires

\[
 |A+B|^2=|A|^2+2\Re(A\overline B)+|B|^2.
\]

Discarding the mixed or exterior terms destroys the all-class R128
reconstruction.  Absolute values or early Cauchy--Schwarz likewise remove
the only available Mobius cancellation.

The exact finite replay at `N=64,128,256`, with
`A=floor(N/3)`, `B=N/2`, found zero compressed residual, equality of the
projected commutator and source norms, and positive exterior leakage in every
case.  The values were respectively

| `N` | source = projected-commutator norm | exterior norm below `N` |
|---:|---:|---:|
| 64 | 6.102455708487214 | 2.640527433644839 |
| 128 | 9.084387464203376 | 3.712191846035012 |
| 256 | 13.503145955977460 | 4.727248837665882 |

These computations replay the exact support proof; they are not asymptotic
evidence.

## 3. Strongest completion-sensitive repair

Put

\[
 K(s)=-\frac{\zeta'}{\zeta}(s),\qquad
 U(s)=K(s)-\frac1{s-1},
\]

and let `R` denote reflection, `(RF)(s)=F(1-s)`, with
`P_-=(I-R)/2`.  Write

\[
 \mathfrak a(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
 + \frac12\frac{\Gamma'}{\Gamma}(s/2),
\]

so the functional equation gives

\[
 K(s)+K(1-s)=\mathfrak a(s)+\mathfrak a(1-s).
\]

Also define the actual coefficient series in its convergent half-plane,

\[
 B_C(s)=\sum_n C(n)n^{-s}=-\frac{\zeta'(s)}{\zeta(s)^2},
 \qquad K(s)=\zeta(s)B_C(s).
\]

The Dirichlet series here is licensed only for `Re s>1`.  Formula (3.2) in
the critical strip uses the meromorphic continuation
`B_C=-zeta'/zeta^2`; it is not a finite, pre-analytic-continuation coefficient
adapter.  This is already a separate failure of S1's finite/pre-analytic-
continuation requirement, distinct from ordinary cutoff completeness.

For `z=s-1/2` and `h>0`, the R102 multiplier is

\[
 H(s)=\widehat V_Q(z)=q_h(z)\widehat V(z),
 \qquad q_h(z)=(e^{hz}-e^{h/2})^2.
\]

Exact reflection algebra yields

\[
 \boxed{
 [P_-,M_H]U(s)
 =\frac{H(s)-H(1-s)}2\,U(1-s).}
 \tag{3.1}
\]

For an even base window,

\[
 H(s)-H(1-s)
 =4\widehat V(z)\sinh(hz)
   \bigl(\cosh(hz)-e^{h/2}\bigr).
\]

Substitution of the completion and the actual `C` series gives the most
faithful repaired candidate:

\[
 \boxed{
 \begin{aligned}
 [P_-,M_H]U(s)
 ={}&2\widehat V(z)\sinh(hz)
       \bigl(\cosh(hz)-e^{h/2}\bigr)\\
 &\times\left[
 \mathfrak a(s)+\mathfrak a(1-s)-\zeta(s)B_C(s)+\frac1s
 \right].
 \end{aligned}}
 \tag{3.2}
\]

This formula does not misuse `K(1-s)` as a second convergent Euler series.
For the R71 B-spline window, its explicit `Vhat` has zeros only on
`Re z=0`.  The other two factors in (3.2) are also nonzero when
`0<|Re z|<1/2`:

- `sinh(hz)=0` forces `Re z=0`;
- if `cosh(hz)=e^{h/2}`, the imaginary part first forces
  `Im(hz)` to be an integral multiple of `pi`; the positive real case then
  requires `cosh(h|Re z|)=e^{h/2}`.  Since
  `cosh(h/2)<e^{h/2}`, this requires `|Re z|>1/2`.

Thus (3.2) is off-critical zero-faithful.  That is not coercivity.  Equation
(3.1) is exactly a multiplier times a reflected copy of the original source.
Its multiplier has critical-line zeros and is not bounded below there, so no
uniform inverse-energy bound or smaller arithmetic norm follows.  Once the
external output block is
localized, multiplication by that block becomes Mellin convolution; the
corresponding physical-space commutator is the already-known R102 boundary
collar at the unknown raw scale.

## 4. Finite algebra closes on two channels

Let

\[
 \mathcal C_H=[P_-,M_H]
 =\frac12M_{H-H^{\mathcal R}}\mathcal R.
\]

For any two multipliers `G,H`, exact algebra gives

\[
 \boxed{
 \mathcal C_G\mathcal C_H
 =-\frac14M_{(G-G^{\mathcal R})(H-H^{\mathcal R})}.}
 \tag{4.1}
\]

More generally, every finite word generated by multiplication operators and
one involutive reflection has normal form

\[
 M_a+M_b\mathcal R.
\]

Therefore adding multiplier windows or nesting reflection commutators inside
this operator algebra does not create a new independent source.  It merely
changes the two scalar coefficients of the original and reflected channels.
This is the precise scope of the closure result.  In particular, it does not
classify nested arithmetic commutators involving `T_C`, nor operators outside
this finite crossed product.

## 5. Hostile audit

| Required test | Result | Reason |
|---|---|---|
| R71 typing and strict adapter | **FAIL** | The literal seed omits scalarization/cutoff; after repair it either equals the endpoint or adds a raw boundary tail. |
| Fejer/half-period | **FAIL to discriminate** | The convolution algebra lifts to a free commutative pseudo-prime monoid with arbitrary additive pseudo-logs. |
| Density-matched pseudo-primes | **FAIL to discriminate** | The same lift preserves `C*1=Lambda`; density and soft covariance do not supply the missing arithmetic law. |
| R178 positive Euler surgery | **FAIL to discriminate** | For coefficients `a`, inverse `b`, and `C_b=-Db`, the differential convolution identity `C_b*a=Lambda_a` survives.  Exact zeta completion is not converted into an inequality. |
| R179 planted quartet | **FAIL to discriminate** | Reflection-commutator algebra is universal, and exact functional symmetry can coexist with a planted off-line quartet.  Combining actual zeta coefficients with completion identifies the zeta source but gives no bound. |
| R121 CRT/Hilbert | **Not triggered at seed** | Any later character/profile Cauchy step pays the sharp square-root profile cost. |
| Early Cauchy/absolute values | **FAIL if used** | It separates two raw endpoint-scale terms and erases the outer signed cancellation. |
| All packet retention | **FAIL as a reduction** | Retaining all inner/exterior/mixed terms restores `O_full`; dropping them loses the exact R128 adapter. |

No listed test supplies the missing strict inequality.  The conjunction of
actual coefficients and exact completion is zeta-specific, but specificity
is not a saving theorem.

## 6. Decision and next experiment

S1-B1 is rejected.  Do not attempt to rescue it by changing commutator sign,
adding multiplier windows within the reflection crossed product, nesting
reflection commutators, truncating `C`, or discarding exterior/mixed terms:
the identities above show exactly where each of those moves collapses or
loses the endpoint.  Arbitrary nested arithmetic commutators have not been
classified.

The complete-family source-law branch is parked under its two-candidate stop
rule.  Reopening it requires an operator outside the finite
multiplier/reflection algebra and an explicit finite coefficient--completion
inequality with a strict norm advantage.

The next maximum-information experiment is one QP/Turan source-fiber
bifurcation:

1. derive every exact restriction imposed by one legal event on the source,
   adaptive coefficient vector, and actual-prime orbit, preserving quantifier
   order;
2. try to realize all restrictions in a filled density-matched pseudonode
   model;
3. if a bad-radius realization exists, close that soft proof class;
4. if realization fails for a proved reason, promote only the first violated
   condition as a candidate actual-prime invariant; and
5. continue only if that invariant has an exact theorem statement and an
   exponent ledger reaching `0.0179` or `0.019`.

Otherwise QP/Turan is parked too.  The uniform strip, its complete R71
fixed-power bound, the later strip-to-RH amplifier, the sharp four-cycle
bound, and RH all remain open.

## 7. Formal and executable synchronization

The abstract finite identities, including endpoint equality whenever the
inner-weight residual is zero, are formalized in
[`S1B1CompletedSourceCommutator.lean`](../lean/rhbridge/RHBridge/S1B1CompletedSourceCommutator.lean)
and axiom-audited in
[`S1B1CompletedSourceCommutatorAudit.lean`](../lean/rhbridge/RHBridge/S1B1CompletedSourceCommutatorAudit.lean).
The divisor-shell support implication, analytic completion identities, and
nonvanishing argument are recorded here and replayed where applicable in
Python; they are not claimed as Lean theorems.

The exact finite replay is implemented in
[`s1_b1_completed_source_commutator.py`](../src/s1_b1_completed_source_commutator.py)
with regression tests in
[`test_s1_b1_completed_source_commutator.py`](../src/test_s1_b1_completed_source_commutator.py).

Verification commands:

```text
PYTHONPATH=src pytest -q src/test_s1_b1_completed_source_commutator.py
cd lean/rhbridge
lake build RHBridge.S1B1CompletedSourceCommutator
lake env lean RHBridge/S1B1CompletedSourceCommutatorAudit.lean
```

Observed on 2026-09-03: `8` Python tests passed; the Lean build and audit
passed, and the printed axioms were limited to `propext`, `Classical.choice`,
and `Quot.sound` where used.
