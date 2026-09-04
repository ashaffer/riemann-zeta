# Bellman reward sampling for the uniform-strip search

**Date:** 2026-08-30  
**Status:** twenty sampled research rollouts, hostile Bellman backup, two
diagnostic rounds, and the COSE and PWCT proof-or-counterexample audits
completed.  Actual-prime COSE and PWCT remain open; their tested soft
relaxations are refuted.  No uniform zero-free strip and no proof of RH.

## 0. Outcome

Bellman backup changed the research policy in three steps.

1. The raw rollout sampler favored a source-conditioned KKT experiment
   followed by entropy diagnostics and only then an arithmetic transport.
2. Hostile backup assigned zero continuation value to two attractive paths:
   a paired `q/v` saddle has an exact abstract convex countermodel, and the
   four-index `E` associator is a tautology.
3. The selected KKT precondition experiment found full-dimensional contacts
   reaching almost to `B`, but increasingly ill-conditioned signed
   `B^-1`-shift response and no low-entropy trend.  This lowers the value of
   immediate source-to-projective transport.

The first Bellman revision proposed **SCPSI**, an exact carrier-positive
sampling inequality with a semi-infinite SDP.  A second audit showed that its
lower bound is equivalent, relative to the proved energy upper bound, to the
nonexistence of the putative separator.  SCPSI is therefore a certificate
reformulation of exponent-level LTRAD, not an intermediate lemma.  The honest
next split is carrier-only source excitation followed, only in the overshoot
branch, by a many-peak corrector-cancellation theorem.  An event-conditioned
or universal prime-only DPA upper certificate also remains independently
necessary.  The subsequent COSE audit found an exact mass-legal synthetic
Fejer countermodel to the tested abstract source/carrier relaxation.  It did not
transfer to ordinary-prime logarithms.  On shells without close reflected
pairs, actual-prime COSE is exactly LTRAD, so it is not a uniform reduction
unless a legal event is first shown to force such pairs.

## 1. Bellman proof-search rule

A state is the complete typed theorem DAG, not merely the latest conjecture.
An action is a theorem attempt, reduction, countermodel search, or certified
experiment.  Each transition retains

```text
quantifiers; exponents; source normalization; ordinary-prime mask;
global floor/cap; B^-1 precision; dependencies; hostile controls.
```

Proof reward and information reward are kept separate:

```text
Q_proof(s,a)=r_proof(s,a)
             +gamma min_(omega in hostile outcomes) V_proof(T(s,a,omega)),

Q_info(s,a)=r_info(s,a)-cost(a)
             +gamma CVaR_.20 V_info(T(s,a,omega)).                 (1.1)
```

The minimum in the first line reflects the fact that a proof must survive
every admissible case.  The lower-tail backup in the second prevents a
high-upside but usually ambiguous experiment from dominating.  At a logical
AND gate, proof value is the bottleneck value of its children; at an OR gate,
it is their maximum.  Downstream rewards are set to zero until every required
adapter is present.

The hard-veto rules are:

- an exact countermodel satisfies the advertised hypotheses;
- the proposed lemma is the target with renamed notation;
- an escape clause assumes the desired transverse return;
- a source, mask, floor, precision, or exponent is lost;
- an undefined normalization can change the claimed invariant; or
- a downstream theorem is rewarded before its transport/adapter exists.

The numerical rewards used to sample actions are policy heuristics, not
mathematical probabilities.  Exact deductions and countermodels remain the
only logical evidence.

The hostile outcome set contains abstract convex hulls, diffuse coisometries,
Sidon--Fejer states, normalized `GL_2` kernels, local composite shells,
finite actual-prime shells, and the unresolved asymptotic actual-prime case.

## 2. Rollout sampling and adversarial backup

Twenty depth-three-to-six rollouts were sampled.  Before hostile backup, the
five leading policies were:

| policy | first actions | hostile-floor score |
|---|---|---:|
| R15 | certified KKT -> actual-prime/hostile comparison -> participation -> transport test | 22.27 |
| R14 | paired saddle -> participation -> event-conditioned upper certificate | 20.36 |
| R9 | certified KKT -> paired-saddle falsifier -> APDIE invariant | 19.59 |
| R10 | certified KKT -> paired saddle -> event-conditioned upper certificate | 18.56 |
| R11 | participation -> sparsification test -> transport -> arithmetic rigidity | 18.29 |

Three backups materially changed this order.

### 2.1 Paired-saddle veto

Let `q,v` be linearly independent and choose any `alpha,beta,D>0`.  An
abstract convex atom hull can have `-alpha q` and `-beta v` as separately
exposed vertices while containing the source atom

```text
a_0=v-Dq.
```

Its two radial KKT measures are disjoint point masses and the two radial
values can be chosen independently.  In particular one may arrange

```text
r(q)>Y^(-.019),                 r(v)<Y^(-.0179).
```

Thus the relation `v=a_0+Dq` plus two KKT identities supplies no generic
contact overlap or cross-covariance law.  A prime-specific coupling theorem
could still exist, but that theorem is the missing action; jointly solving
the two LPs does not earn its reward.  Policies R14, R9, and R10 are removed
in their present form.

### 2.2 Associator zero reward

For normalized two-vectors `u_i v_i=1`, the system `s_ki=u_k v_i` has

```text
s_ki-s_kj s_ji=det(u_k,u_j)det(v_i,v_j),
```

while its four-index associator is an identity for arbitrary edge labels.
Arbitrary `GL_2` chains therefore support arbitrarily varying projective
coordinates.  Projective rigidity earns no reward from the associator; only
the actual-prime, small-height, parity, gcd, and modular data remain live.
Moreover this entire arithmetic branch is dependency-discounted until a
faithful signed source-to-shadow transport exists.

### 2.3 APDIE typing veto

The provisional APDIE card did not freeze its query set, corrector
coordinates, whitening, cancellation norm, choice among nonunique KKT
measures, or exponent quantifier.  Stable rank changes with the whitening,
and the phrase “unless a transverse return already occurs” built the target
into an escape clause.  APDIE is therefore retired rather than rewarded as a
theorem.  Section 4 gives its typed replacement.

After these backups, R15's initial action remained the robust choice:
measure the exact source-conditioned saddle and its transport preconditions
before attempting the downstream arithmetic theorem.

## 3. Executed precondition audit

`src/qp_source_saddle_probe.py` was extended to record

- weighted contact-frame numerical rank and condition number;
- separator `l1` and `l2` norms;
- the elementary response bound for independent `B^-1` log shifts; and
- the singular spectrum of the exact linearized `B^-1` shift Jacobian on
  active contacts.

The sampled finite-prime run used 8,001 source times and 6,001 contact times:

| `Y` | primes / contacts | effective contacts | stable rank | max contact / `B` | contact condition | shift-Jacobian condition | `l1` shift bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100.5 | 8 / 8 | 5.17 | 2.58 | .688 | 1.37e3 | 2.07e3 | .791 |
| 200.5 | 15 / 15 | 8.40 | 3.10 | .930 | 1.95e2 | 2.08e3 | 1.390 |
| 400.5 | 27 / 27 | 17.48 | 6.49 | .944 | 1.67e2 | 2.43e3 | 1.288 |
| 800.5 | 46 / 46 | 24.84 | 6.85 | .979 | 4.34e2 | 1.35e4 | 1.284 |
| 1600.5 | 83 / 83 | 48.55 | 11.91 | .999 | 3.63e2 | 1.41e5 | 1.280 |

Primal--dual gaps were below `6.5e-14`.  At `Y=1600.5`, the smallest
singular value of the scaled shift Jacobian was `1.95e-6`.

These data have a narrow interpretation.

- Contact reach does not kill superresolution: the finite optima reach a
  fixed fraction of `B`, approaching the band endpoint in this sample.
- Bounded contact and low-dimensional saturation are not visible: support
  equals the prime dimension and effective size/stable rank grow.
- The signed `B^-1` response is fragile.  The shift-Jacobian condition number
  worsens by almost two orders of magnitude, while the naive `l1` Lipschitz
  bound remains order one.  Thus independent Lipschitz transport cannot
  supply a vanishing error, let alone the PQR weighted error, without a new
  cancellation-sensitive inequality.

This is floating sampled evidence, not an asymptotic result.  In particular,
these finite sources do not satisfy the project's asymptotic `.001` event
threshold.  The trends update research value only; they prove no strip
claim.

Replay with

```bash
PYTHONPATH=src python3 src/qp_source_saddle_probe.py \
  100.5 200.5 400.5 800.5 1600.5 \
  --source-points 8001 --contact-points 6001
```

## 4. Proposed typed replacement: SCPSI, then collapse

Put

```text
tau=.0179,                  B=Y^(50/33),
Delta=1+Y^2/B=Y^(16/33+o(1)),
epsilon=Y^(-(tau+eta)),     0<eta<10^-4 fixed.       (4.1)
```

Assume a legal actual-prime source event and a putative separator

```text
y.v=-1,                     h_Y(y)<=epsilon.         (4.2)
```

Use the proved ordinary-prime matching of opposite-side nodes satisfying
`B|u_i-u_i'|<=kappa`.  With

```text
delta_i=u_i-u_i',           m_i=(u_i+u_i')/2,
z_i=B|delta_i|,
```

orient the antisymmetric coefficient as `Q_i` and define

```text
Psi_i(t)=(t/B)sinc(delta_i t/2)sin(m_i t).           (4.3)
```

Then the reflected corrector is exactly

```text
F_corr(t)=sum_i Q_i Psi_i(t),                        (4.4)
```

up to the frozen global sign convention.  The existing clustered-energy
bound gives

```text
||Q||_2 <<epsilon sqrt(Delta)Y^o(1).                (4.5)
```

The carrier contains every unpaired coordinate, every non-close cross-side
coordinate, and the symmetric half of each selected pair.  Put

```text
g_y(t)=(F_car(t)-epsilon)_+                          (4.6)
```

and define the carrier-positive sampling functional

```text
Xi(y)^2=
 sup { integral g_y(t)^2 dmu(t):
       mu is a finite positive Borel measure on H_Y,
       integral Psi(t)Psi(t)^T dmu(t) <= I }.        (4.7)
```

The matrix inequality is in the real PSD order.  Since `(4.2)` implies
`g_y(t)<=|F_corr(t)|`, equations `(4.4)` and `(4.7)` give the exact upper
bound

```text
Xi(y)<=||Q||_2.                                     (4.8)
```

The new conjectural lemma is:

> **Source-conditioned carrier-positive sampling inequality (SCPSI).**
> Uniformly over the actual-prime objects in `(4.1)--(4.7)`,
> ```text
> Xi(y) >>epsilon sqrt(Delta)Y^(eta/2).              (4.9)
> ```

Equations `(4.5)`, `(4.8)`, and `(4.9)` contradict one another for fixed
`eta`; hence SCPSI excludes `(4.2)`.  Taking arbitrarily small fixed `eta`
gives the exponent-level transverse bound needed for LTRAD, while
`eta<10^-4` preserves the strict gap to `DPA_P(.019)`.

Under the standard finite-dimensional Slater condition, the measure SDP has
the dual

```text
Xi(y)^2=
 inf {tr Z: Z>=0,
      Psi(t)^T Z Psi(t)>=g_y(t)^2 for every t in H_Y}.   (4.10)
```

### 4.1 Equivalence collapse

Every assumed separator already gives the feasible rank-one dual matrix

```text
Z=Q Q^T.                                             (4.11)
```

Indeed `(4.8)` is pointwise exactly the dual feasibility inequality, and
`tr(Z)=||Q||_2^2`.  Consequently the proposed lower bound `(4.9)` is not an
independent prediction about the SDP.  Together with `(4.5)`, it says that
no `y` satisfying `(4.2)` exists.

Conversely, if the exponent-level LTRAD bound holds, the class quantified by
SCPSI is empty and `(4.9)` holds vacuously.  Under the project's attainment
and facial-reduction hypotheses,

```text
SCPSI_eta <==> no separator with h_Y(y)<=Y^(-(.0179+eta))
           <==> exponent-level LTRAD_eta.            (4.12)
```

There is also a visible zero-excess branch.  Source normalization gives only
`y_car dot v=-1+o(epsilon)`; it does not force `F_car>epsilon`.  If
`F_car<=epsilon` throughout the band, then `g=0`, `Xi=0`, and the
renormalized carrier is itself a carrier-only LTRAD obstruction.  If there
are no close reflected pairs, this dichotomy is literal: `Psi` is
zero-dimensional and `Xi` is zero when `g=0` (infinite if `g>0` somewhere).

Thus SCPSI is retired as an intermediate theorem.  Its SDP remains a useful
diagnostic only after a separate theorem has forced quantitative carrier
overshoot.

### 4.2 Finite diagnostic

On sampled actual-prime shells the exact carrier/corrector identity held to
`1.7e-13`.  At the unit-constant finite plug-in
`epsilon=Y^(-(.0179+.00005))`, `g` vanished in every tested shell because
`epsilon` was about `.87--.91`, above the finite saddle caps.  Hence `Xi=0`.
The asymptotic statement has unspecified constants and an `o(1)` term, so
this is not a canonical finite threshold.  These sources are not
asymptotically legal.

Retuning `epsilon` to the sampled cap made the SDP nontrivial.  Its
primal/dual values essentially saturated the generic upper bound
`Xi<=||Q||_2`; the normalized ratio `Xi/(epsilon sqrt(Delta))` fell from
`.0799` at `Y=254.5` to `.00623` at `Y=3000.5`.  This floating experiment is
not an asymptotic counterexample, but it supplies no evidence for the
conjectured `sqrt(Delta)` surplus.

The hostile controls are exact at the level relevant to the conjecture:
one-mode and discrete coisometric correctors attain `Xi=||Q||`, while scaling
`Q` realizes arbitrarily smaller normalized ratios.  A diffuse rotating
two-dimensional frame numerically attained the same equality to `2.4e-6`.
Thus cap-plus-energy geometry alone cannot create the proposed surplus; any
such theorem would have to contain a new actual-prime/source hypothesis.

## 5. Revised long-horizon policy

The Bellman policy after the equivalence and COSE collapses is:

1. compare the carrier-constrained transverse radius with the unrestricted
   radius on source-conditioned prime saddles;
2. retain only **actual-prime COSE**, explicitly using contiguity of the
   source prime interval and the ordinary-prime logarithmic mask;
3. only if COSE forces quantitative overshoot, use the `Xi` SDP to seek the
   separate many-peak theorem needed to defeat corrector cancellation;
4. pursue an event-conditioned prime-only DPA certificate independently;
5. dependency-discount source-to-projective transport and RSDR until a
   signed superresolution inequality exists; and
6. keep RH outside the reward horizon until the fixed strip itself is proved.

```text
paired q/v saddle from convex geometry alone:       REFUTED
associator as projective rigidity:                   INFORMATION-NEUTRAL
provisional APDIE statement:                         RETIRED / ILL-TYPED
finite B-scale contact reach:                        OBSERVED
naive l1 B^-1 transport stability:                   NOT OBSERVED
SCPSI as an intermediate lemma:                      RETIRED / LTRAD-EQUIVALENT
abstract source/carrier relaxation of COSE:          REFUTED
COSE (actual-prime statement):                       OPEN / LTRAD-EQUIVALENT IF NO PAIRS
many-peak corrector cancellation:                    OPEN
event-conditioned or universal DPA_P(.019):          OPEN
LTRAD_P(.0189,.001):                                 OPEN
uniform zero-free strip:                             NOT PROVED
RH:                                                  NOT PROVED
```

## 6. PWCT follow-up backup

The next action after COSE was the positive-weight carrier theorem `PWCT`.
Its hostile audit proved the exact probability normalization, semi-infinite
dual, unpaired-event inheritance, and source-time/participation closures.
It did not prove the actual-prime theorem.  A diffuse real-node construction
with prime-scale density, gaps, a contiguous legal source, and unpaired
positive support has

```text
rho_+(v)<=Y^(-.499+o(1)),
```

so every tested non-arithmetic proof mechanism fails by a large margin.
Finite actual-prime exchange runs showed no stable arithmetic surplus and
often assigned little or no mass to the source interval.

There is also a dependency correction.  PWCT excludes only nonpositive
separators and cannot be paired with the recorded signed `DPA_P(.019)`.
It needs a separately open positive upper antenna.  For a probability antenna
with maximum atom `Y^(-1+o(1))`, averaging each close reflected pair changes
the band transform by only `Y^(-17/33+o(1))`; hence diffuse positive
`PDPA_+(.019)` automatically carrierizes.

Diffuse positive `PDPA_+(.019)` is only a sufficient adapter, and it is a
strict strengthening of the positive-antenna program already audited in the
actual-node Delsarte reports.  Its refutation would not kill non-diffuse
positive carrier antennas: participation permits atoms on the
`Y^(-.019+o(1))` scale, far above the diffuse cap.  There is no known
diffusification lemma.

The corrected maximum-information action was a source-free comparison of the
exact `delta_+^C(Y)` with the unrestricted positive antenna and a frozen
diffuse-capped carrier antenna, including the dual contact measure.  It has
now been run through `Y=8000.5`.  The cap was active, but its sampled relative
penalty shrank from `3.5%` to `1.1%`; capped effective support and dual contact
count grew with the prime dimension.  The carrier itself was almost vacuous
because three of five shells had no close pair.  Thus diffuseness survives as
a sufficient adapter, but no low-complexity template or arithmetic carrier
surplus appeared.  PWCT is retained as a conditional/falsification branch,
not the leading standalone theorem target.  Full details are in
`ZETA23-PWCT-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`.

```text
PWCT source-time and low-participation branches:     CLOSED
PWCT tested soft relaxations:                        REFUTED
PWCT (actual-prime statement):                       OPEN
diffuse positive PDPA_+(.019):                       OPEN / OLD STRONGER PROGRAM
event-free delta_+^C cap comparison:                 RUN / DIFFUSE HIGH-RANK
```
