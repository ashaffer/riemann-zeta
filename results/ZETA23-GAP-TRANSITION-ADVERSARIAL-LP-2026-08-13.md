# Consecutive-gap transition adversarial LP and q-stage frontier

**Date:** 2026-08-13

## Verdict

A new falsification/lemma-design tool now optimizes the selected symmetrized
gap DFT over nonnegative residue-transition measures while independently
switching on:

```text
block count and gap mass;
exact unweighted row/column marginals;
b=a+g (mod q);
fixed-wheel endpoint admissibility;
exact consecutive survivors of a finite wheel;
Gafni--Tao tail caps;
second/third gap moments;
one-height rational-cell selectors;
local stage count/second-moment constraints.
```

The decisive modeling point is that a variable is normalized **event count**
`x_(a,b,g)`, while the Voronoi mass and objective use `g*x_(a,b,g)`.
Equidistribution of unweighted prime counts therefore does not silently
become equidistribution of successor-gap-weighted counts.

The result is a clean negative/positive boundary.

1. Positivity, exact unweighted marginals, physical congruence, fixed-wheel
   admissibility, the known Gafni--Tao tail, known gap moments, block mass,
   and common-height incidence still admit explicit coherent extremizers.
   The finite certificate is rational and all of its linear constraints are
   replayed exactly.
2. Even after granting the proposed local q-stage count

   ```text
   N_q/Y <<Y^(-b+o(1)),
   ```

   the optimal consequence of the **known** positive tail/moment package at
   `b=beta=.1598` is only

   ```text
   Y^(-c_stage+o(1)),       c_stage=.010827272727...,
   ```

   below both the shallow carrier budget `.017522268449...` and the uniform
   band maximum `.019740482583...`.
3. The proposed new rough-stage second moment

   ```text
   sum_(one q-stage) G_j^2 <<Y^(1+o(1))
   ```

   would combine with the local count by Cauchy to give

   ```text
   Y^(-b/2+o(1))=Y^(-.0799+o(1))                     (0.1)
   ```

   at the bottom denominator.  This decisively beats the carrier.  But it is
   not a consequence of endpoint wheel admissibility, and a bound for each
   stage separately does not by itself bound the signed sum of all deletion
   stages.
4. For the terminal symmetrized DFT, the exact missing object is simpler to
   state: gap-weighted endpoint marginals.  Their selected Fourier
   discrepancy controls the objective directly.  Exact weighted uniformity
   leaves only the Ramanujan principal mode `O(1/q)`.

Thus the existing constraint package fails fast.  Two genuinely new tools
remain live: a **local rough-stage S2 theorem plus signed stage aggregation**,
or a direct **gap-weighted endpoint-marginal theorem**.  Neither is supplied
by the current literature inputs or by the LP.

No actual-prime counterexample and no zero-free strip are claimed.

---

## 1. Exact finite LP

For a block `I`, selected reduced `r/q`, units `a,b mod q`, physical gap `g`,
and optionally wheel residues `u,v`, let

```text
x_(I,a,b,g,u,v)>=0
```

be event count divided by shell length.  The normalization is

```text
sum x = n_I,                  sum g*x=m_I.            (1.1)
```

The selected frozen symmetrized DFT is

```text
A_I(r/q)=sum x*g*{e_q(ra)+e_q(rb)}/2.                (1.2)
```

Physical transitions obey

```text
b=a+g (mod q).                                      (1.3)
```

For a wheel `W`, endpoint admissibility retains only atoms with

```text
(u,W)=(u+g,W)=1.                                    (1.4)
```

The stronger deletion-stage option additionally requires that there be no
unit of `W` strictly between `u` and `u+g`; it models consecutive survivors
of that finite wheel, not merely two admissible endpoints.

The unweighted marginal constraints are

```text
sum_(b,g,u,v)x_(a,b,g,u,v)=n_I/phi(q),
sum_(a,g,u,v)x_(a,b,g,u,v)=n_I/phi(q).               (1.5)
```

There are analogous optional wheel marginals.  Gafni--Tao tails and moments
are linear because of the count normalization:

```text
sum_(g>=H) g*x <= B_H,
sum g^2*x<=B_2,                 sum g^3*x<=B_3.      (1.6)
```

The complex modulus is the maximum of directional real LPs.  The tool can
sweep those directions and supplies a Lipschitz upper bracket.  Every
individual directional optimum is a certified feasible lower bound.  SciPy
HiGHS is used for large instances; a dependency-free exact vertex enumerator
handles small instances.

The implementation is
[`src/gap_transition_adversarial_lp.py`](../src/gap_transition_adversarial_lp.py).

---

## 2. Progressive finite falsification

The deterministic diagnostic uses `q=7`, wheel `W=30`, total mass `1`,
event count `1/12`, even gaps through `42`, a tail cap on `g>=14`, and
rational second/third-moment caps.  These constants are a finite analogue,
not fitted asymptotic prime data.

| last constraint added | maximum real projection | attained modulus |
|---|---:|---:|
| normalization | `.6234898019` | `1.0000000000` |
| exact unweighted q-marginals | `.4917970571` | `.4917970571` |
| physical gap congruence | `.4229259651` | `.4995648601` |
| endpoint wheel + exact wheel marginals | `.4031140519` | `.4032025091` |
| GT-shaped tail cap | `.1373256832` | `.1373954362` |
| second and third moments | `.0823758432` | `.0823758432` |

The final optimizer has 27 nonzero atoms.  Rounding the HiGHS vertex back to
fractions of denominator at most `866880` gives an **exact** feasible
certificate: every equality and inequality is then checked with rational
arithmetic.  Interval evaluation of the seventh-root trigonometric
coefficients gives

```text
Re A_7(1)>.0823758432247>.08.                        (2.1)
```

Thus the full listed finite constraint set does not algebraically force
cancellation.  This is a theorem about the transition-measure relaxation,
not a realization by primes.

### Common height

The selector module treats an affine block frequency

```text
alpha_I(t)=s_I*t+o_I
```

and enumerates exact intersections with lifted rational cells.  In the test,
one common height in

```text
[99/700,101/700]
```

simultaneously selects `1/7` on one block and `2/7` on a second.  With total
normalization shared between the two blocks, all constraints above still
admit

```text
Re(A_I0+A_I1)=.0948226488786....                     (2.2)
```

This proves only that common-height incidence, as a selector constraint, is
not cancellation.  It does not model every nonlinear curvature relation of
the zeta application.

---

## 3. Exact known-input q-stage frontier

Now grant the proposed global count for a selected q-stage,

```text
q=Y^(b+o(1)),             N_q<=Y^(1-b+o(1)).         (3.1)
```

For fail-fast purposes this section also grants that the terminal
Gafni--Tao tail and terminal gap moments apply directly to the local stage
spans.  That inheritance is not currently proved for the intermediate
deletion geometry.  The failure below therefore persists under a deliberately
favorable extra assumption.

At a gap threshold `Y^h`, short gaps contribute at most

```text
N_q*Y^h/Y <=Y^(-(b-h)+o(1)).                         (3.2)
```

The audited Gafni--Tao branch gives the long-gap mass bound

```text
Y^(-s(h)+o(1)),       s(h)=(9/13)(h-2/15).           (3.3)
```

Consequently the best positive bound obtainable from (3.1)--(3.3) is found
at `b-h=s(h)`:

```text
h_*=(13b+6/5)/22,
c_stage=b-h_*=(9/22)(b-2/15).                        (3.4)
```

At `b=beta=799/5000`, exactly

```text
h_*=16387/110000=.148972727272...,
c_stage=1191/110000=.010827272727....                (3.5)
```

This is not merely a weak derivation.  A one-scale positive allocation with

```text
Y^(1-beta) events,          each gap Y^(h_*),
```

saturates (3.2)--(3.3) in exponent.  It also has

```text
gap-square exponent =1-beta+2h_*=1.1381454545...<1.23,
gap-third exponent  =1-beta+3h_*=1.2871181818...
                    <1.2999692307...,                (3.6)
```

where the last number is the current truncated-third-moment budget
`1+2theta-s(theta)` at `theta=.1588`.  It lies below the retained cutoff
because `h_*<theta`.  Thus the known S2 and truncated M3 cannot remove this
extremal allocation.

The deficits are

```text
kappa(.47,.665)-c_stage       =.006694995722...,
kappa(.5,.665)-c_stage        =.008913209856....      (3.7)
```

Count plus GT begins to beat the shallow and band-max thresholds only for

```text
b>2/15+(22/9)kappa
  =.1761655451...  (shallow),
b> .1815878463...  (band maximum),                  (3.8)
```

well above the bottom `b=.1598`.

This allocation is a scoped exponent-ledger adversary.  The finite rational
LP separately verifies compatibility of phase coherence with positivity,
physical residue transitions, exact unweighted marginals, and a wheel.  The
two checks do not constitute an asymptotic sequence of actual primes.

---

## 4. The rough-stage S2 proposal

There is no issue on a complete periodic cell if the proposed exact identity

```text
M_q^(multiple)=m/q                                    (4.0)
```

is available: at `q=Y^(b+o(1))`, its positive mass already saves `b`, far
more than either carrier threshold.  The LP can impose (4.0) exactly through
a congruence-class mass constraint; its regression test uses mass `1/7` on
the `0 mod 7` gap class.  The unresolved step is **localization** to the
physical curvature blocks, which generally do not contain a complete period.
The local count/S2 proposal is one possible replacement for the unavailable
full-period averaging.

Let one deletion stage have at most `N_q` charges, and let `G_j` dominate the
absolute local span appearing in each charge.  Since the exact deletion
formula gives `|D_j|<=G_j`, Cauchy yields

```text
1/Y*|sum_j D_j|
 <=sqrt{(N_q/Y)*(sum_j G_j^2/Y)}.                    (4.1)
```

More generally, write the stage second moment as

```text
sum_j G_j^2 <<Y^(1+rho+o(1)).                       (4.2)
```

Then (4.1) saves exactly `(b-rho)/2`.  A strict carrier saving `kappa`
therefore requires the sharp exponent inequality

```text
rho < b-2*kappa.                                     (4.3)
```

At `b=beta=.1598`, the two current thresholds are

```text
rho <.124755463100513...   for kappa(.47,.665),
rho <.120319034834116...   for kappa(.5,.665).       (4.4)
```

This quantifies the actual theorem needed.  `rho=0` has ample room; the
known terminal value `rho=.23` has none.

Three moment levels must be kept distinct.

### 4.1 Known global prime-gap S2

Even optimistically granting the terminal bound

```text
sum G_j^2 <<Y^(1.23+epsilon)
```

to a deletion stage, (4.1) has saving

```text
(b-.23)/2=-.0351                                    (4.5)
```

at `b=.1598`: it is power-vacuous.  In the actual deletion identity, local
stage spans are intermediate rough-neighbor gaps and multiplicities must be
audited before even this optimistic inheritance is legal.

### 4.2 Proposed new rough-stage S2

If instead one proves

```text
sum_(one stage) G_j^2 <<Y^(1+o(1)),                 (4.6)
```

then (4.1) gives `b/2=.0799`, proving (0.1).  This is a real potential new
tool, not a rearrangement of the current moments.

### 4.3 Why wheel admissibility does not prove (4.6)

Endpoint sieving constrains only congruence classes.  It permits a tiny
amount of mass on arbitrarily long CRT-compatible gaps.  The LP makes this
failure quantitative while preserving exact q- and wheel-count marginals:

```text
allowed largest gap             max sum g^2*x
42                              31.9733333333...
84                              61.6000000000...
```

The maximum grows with the permitted gap.  Thus (4.6) cannot be inferred
from endpoint wheel admissibility.

The code also implements the stronger finite condition that the endpoints
be **consecutive units of the wheel**.  For `W=30` this correctly leaves only
gaps `2,4,6`.  It is a useful finite-stage laboratory, but a local uniform
bound for a growing roughness cutoff is still an analytic theorem: a full
primorial period is vastly longer than the physical block in the relevant
range.

### 4.4 Stage aggregation remains separate

The deletion identity is

```text
T_prime-T_integer=sum_p D_p.                         (4.7)
```

A per-stage estimate does not automatically estimate the signed pointwise
sum.  If there are `P` active stages, triangle inequality loses `P`, while
Cauchy across stages loses `sqrt(P)`.  An absolute square-function estimate
closes only if its exponent includes that aggregation loss, or if a new
martingale/orthogonality mechanism removes it.  Therefore (4.6) is
high-value but not by itself a proof of the terminal antenna bound.

The exact deletion identity and its scope are in
[`ZETA23-ERATOSTHENES-DELETION-CURVATURE-CHARGE-TOOL-2026-08-13.md`](ZETA23-ERATOSTHENES-DELETION-CURVATURE-CHARGE-TOOL-2026-08-13.md).

---

## 5. Exact weighted-marginal conditional lemma

For constant block amplitude define the gap-weighted endpoint marginals

```text
mu_L(a)=sum_(b,g)g*x_(a,b,g),
mu_R(b)=sum_(a,g)g*x_(a,b,g),
sum mu_L=sum mu_R=m.                                 (5.1)
```

Then (1.2) is exactly

```text
A_q(r)=1/2{sum_a mu_L(a)e_q(ra)
            +sum_b mu_R(b)e_q(rb)}.                 (5.2)
```

Let `u(a)=m/phi(q)` on the units and put

```text
delta_q=1/2{||mu_L-u||_1+||mu_R-u||_1}.              (5.3)
```

Triangle inequality and the Ramanujan sum give the exact bound

```text
|A_q(r)|<=delta_q+m*|c_q(r)|/phi(q).                 (5.4)
```

For prime `q=Y^(b+o(1))` the second term is
`m*Y^(-b+o(1))`.  Hence the following theorem would close the terminal
symmetrized DFT on each normalized block:

```text
delta_q <<m*Y^(-kappa-eta).                         (5.5)
```

Exact gap-weighted uniformity is the special case `delta_q=0`, leaving only
`m/(q-1)`.  The LP includes both exact weighted uniformity and the relaxed
L1 budget (5.3).  Ordinary prime-in-progressions input controls unweighted
counts in (1.5), not (5.3).

For a selected pole sub-sector or for the signed sum of deletion stages,
joint transition information can still be necessary.  Lemma (5.4) is scoped
to the full terminal symmetrized endpoint statistic (5.2); it does not erase
those distinctions.

---

## 6. Reproduction and truth boundary

Run

```bash
PYTHONPATH=src python3 -m unittest -v src/test_gap_transition_adversarial_lp.py
python3 results/verify_zeta23_gap_transition_adversarial_lp.py
python3 src/gap_transition_adversarial_lp.py
```

The verifier checks:

1. all exponent identities in (3.4)--(3.8) with exact fractions;
2. compatibility of the extremal scale with the known S2/M3 ledgers;
3. an exact rational finite LP certificate;
4. a rigorous interval lower bound for its selected DFT;
5. failure of endpoint wheel admissibility to bound the second moment;
6. exact common-height cell intersection and a surviving two-block LP;
7. SciPy and dependency-free exact-solver paths.

Proved here are finite relaxation nonimplications and the conditional lemmas
(4.1)--(4.4) and (5.4).  Not proved are the rough-stage S2 (4.6), signed
aggregation in (4.7), realization of an LP extremizer by primes, the full antenna, or a
zero-free strip.
