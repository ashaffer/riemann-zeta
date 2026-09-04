# ZETA23 QP/Turán source-fiber bifurcation

Date: 2026-09-03.

## Outcome

The precommitted bifurcation has been run.  It did **not** produce a proved
actual-prime invariant.  Instead, the smooth density-matched real-node model
already recorded in the PWCT audit simultaneously defeats

1. the direct abstract radial lower bound at exponent `.0189`; and
2. the source-fiber lower bound at exponent `.0179` used by the recorded
   transverse mixing argument.

It does so while retaining the legal contiguous source event, the full height
band, prime-scale node density and maximum gaps, positivity, diffuseness,
unpaired antenna support, and (after an arbitrarily small generic
perturbation) rational independence and absence of prescribed finite additive
relations.  What it deliberately does not retain is the literal deterministic
mask

\[
 u_p=|\log(p/Y)|,\qquad p\text{ an ordinary prime}.
\]

Thus the density/spacing/convexity/moment/equicontinuity proof class is closed.
Actual-prime `LTRAD_P(.0189,.001)` remains open: a real-node countermodel is
not a counterexample on primes.  `DPA_P(.019)`, the uniform zero-free strip,
the sharp four-cycle bound, and RH also remain open.

Under the recorded stop rule, QP/Turán is now parked.  Reopening it requires a
separately stated and proved quantitative consequence of deterministic prime
placement at the full finite-aperture resolution, not another soft density or
moment hypothesis.  The next bounded maximum-information experiment is the
cheap direct-RH exterior-factorization falsifier for
`C_{a,b}=T_{a,b}A_a` on the dense core.

The finite identities below are **PROJECT_SYNTHESIS**.  The smooth
pseudonode construction is imported from the August 30 PWCT audit.  No claim
of literature-level novelty is made.

## 1. Exact passport and the scope correction

At an allowed half-integer center `Y` comparable with `N`, put

\[
 \begin{aligned}
 P_Y&=\{p:\ p\text{ prime},\ Ye^{-1/5}<p<Ye^{1/5}\},\\
 u_p&=|\log(p/Y)|,\\
 H_Y&=[Y^{.01},Y^{50/33}],\\
 a_Y(t)&=(\cos(tu_p))_{p\in P_Y},\qquad q=(1)_p.
 \end{aligned}
\]

A legal source event consists of a physically contiguous prime interval `I`
and `t_0 in [N^(1/2),N]`.  With

\[
 M=\#I,\qquad
 \lambda=M^{-1}\mathbf1_I,\qquad
 D=-\lambda\cdot a_Y(t_0),\qquad
 e=(M/N)D\ge N^{-.001+o(1)},
\]

define

\[
 v=a_Y(t_0)+Dq.
\]

Then `lambda.q=1` and the exact source-null identity is

\[
 \boxed{\lambda\cdot v=0.}                         \tag{1.1}
\]

There are two different lower targets.  They must not be conflated.

The direct radial quantity is

\[
 r_P(Y)=\sup\{r\ge0:-rq\in\operatorname{conv}a_Y(H_Y)\}.
\]

`LTRAD_P(.0189,.001)` asks that the existence of a legal event force

\[
 r_P(Y)\ge Y^{-.0189+o(1)}.                         \tag{1.2}
\]

The selected source-fiber mechanism instead asks for

\[
 s_v=\inf_{y:y\cdot v=-1}\sup_{t\in H_Y}y\cdot a_Y(t)
     \ge Y^{-.0179+o(1)}.                           \tag{1.3}
\]

The exact one-atom mixing lemma gives

\[
 r_P(Y)\ge\frac{D s_v}{1+s_v}.                      \tag{1.4}
\]

Hence `(1.3)` is a sufficient route to `(1.2)` because
`.001+.0179=.0189`.  It is not equivalent to `(1.2)`: a convex body can have
a long `-q` ray and a short event-dependent `-v` ray.  Failure of `(1.3)`
alone therefore does not refute direct LTRAD.

The quantifiers in `(1.3)` are also exact:

```text
for every legal event E,
  for every signed y chosen after E with y.v_E=-1,
    there exists t in the full H_Y chosen after y.
```

No sign, sparsity, entropy, source-overlap, pair-symmetry, or shared-contact
condition on `y` follows from this passport.

## 2. The two exact antenna witnesses

Let `alpha` be any probability vector on the node set and write

\[
 \Phi_\alpha(t)=\alpha\cdot a_Y(t),\qquad
 \delta=-\inf_{t\in H_Y}\Phi_\alpha(t).
\]

### 2.1 Direct radial dual

Set `z=-alpha`.  Then `z.q=-1` and

\[
 \sup_{t\in H_Y}z\cdot a_Y(t)=\delta.               \tag{2.1}
\]

If `-rq` belongs to the convex hull of the atoms, pairing its convex
representation with `z` gives `r<=delta`.  Thus

\[
 \boxed{r_P(Y)\le\delta.}                           \tag{2.2}
\]

This is the direct LTRAD obstruction.

### 2.2 Projective source-fiber dual

Put

\[
 A_E(\alpha)=D+\Phi_\alpha(t_0).
\]

Whenever `A_E(alpha)>0`, define

\[
 y=-\frac{\alpha}{A_E(\alpha)}.
\]

The probability normalization gives the exact identities

\[
 \boxed{y\cdot v=-1},\qquad
 \boxed{\sup_{t\in H_Y}y\cdot a_Y(t)
       =\frac{\delta}{A_E(\alpha)}}.                \tag{2.3}
\]

This is the distinct source-fiber obstruction.  It belongs to the optional
nonpositive-separator/PWCT subclass, which makes it a particularly strong
soft falsifier but does not make that subclass target-forced.

## 3. Filled diffuse real-node model

The construction is the one proved probabilistically in §5.2 of
`ZETA23-PWCT-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`.

On a fixed antenna interval take the triangular profile

\[
 g(u)=(1-u/L)_+,
 \qquad
 G(t)=\frac{2(1-\cos Lt)}{L^2t^2}\ge0.              \tag{3.1}
\]

Stratified sampling at background density comparable with `exp(u)`, with
importance weights proportional to `g(u)/exp(u)`, supplies a deterministic
realization with `M_A` comparable with `Y/log Y` and

\[
 \sup_{t\in H_Y}|\Phi_\alpha(t)-G(t)|
      \le Y^{-1/2+o(1)}.                            \tag{3.2}
\]

In a disjoint interval take `M_I` comparable with `Y/log Y` quantiles of

\[
 e^u[1-\kappa_Y\cos(t_0u)],
 \qquad t_0=Y^{1/2},\qquad
 \kappa_Y=C(\log Y)Y^{-.001}.                       \tag{3.3}
\]

Integration by parts and quantile error give

\[
 D=\kappa_Y/2+o(\kappa_Y),
 \qquad e=(M_I/N)D>Y^{-.001}                       \tag{3.4}
\]

after choosing the fixed constants.  The source nodes form one contiguous
block.  Zero-weight filler fills the entire shell at prime-scale density and
physical maximum gap `O(log^2 Y)`.

Deleting antenna vertices incident to opposite-side `B^{-1}`-close pairs,
where `B=Y^{50/33}`, changes the transform by only

\[
 Y^{-17/33+o(1)}=o(Y^{-1/2+o(1)}).                 \tag{3.5}
\]

The resulting antenna is positive, diffuse, disjoint from the source, and
unpaired.  A perturbation much smaller than `B^{-1}` can avoid any prescribed
finite collection of rational or additive coincidences without changing the
displayed estimates.

By `(3.1)--(3.2)`, its worst negative dip obeys

\[
 \delta_Y\le Y^{-1/2+o(1)}.                        \tag{3.6}
\]

Equations `(2.2)` and `(3.6)` now give

\[
 r_{\rm pseudo}(Y)\le Y^{-1/2+o(1)}
                    \ll Y^{-.0189},                \tag{3.7}
\]

so direct abstract LTRAD fails in this filled soft model.  Moreover
`A_E(alpha)>=D-delta_Y>0`, and `(2.3)` gives

\[
 s_{v,\rm pseudo}
 \le\frac{Y^{-1/2+o(1)}}{D-Y^{-1/2+o(1)}}
 =Y^{-.499+o(1)}\ll Y^{-.0179}.                    \tag{3.8}
\]

The exact exponent ledger is

\[
 .001+.0179=.0189,\qquad
 .5-.001=.499,
\]

and the source-fiber countermodel has exponent margin
`.499-.0179=.4811`.

An independent exact Fejér realization gives the same conclusion with a
finite triangular probability.  It is useful as an executable algebra
fixture; the smooth construction shows that lattice relations are not the
cause.

## 4. Hostile passport audit

| Field | Forced by the target? | Model status |
|---|---:|---|
| literal ordinary-prime logarithms | yes | intentionally absent |
| contiguous mass-normalized source | yes | retained |
| legal source scale and exact `D` | yes | retained |
| full continuum `H_Y` | yes | retained uniformly |
| event–dual–height quantifier order | yes | defeated by one legal event and its adaptive witnesses |
| signed adaptive direct dual | yes | retained; `z=-alpha` is allowed |
| source-normalized transverse dual | only for mechanism `(1.3)` | retained; `y.v=-1` exactly |
| prime-scale density and maximum gaps | derived/coarse | retained |
| opposite-pair count/matching scale | proof decomposition | retained after deletion |
| positivity, diffuseness, unpaired support | optional stronger subclass | retained |
| rational independence/no finite relations | optional genericity | may be imposed by perturbation |
| source overlap, sparsity, low entropy | not forced | deliberately absent |

The first unmatched datum is therefore deterministic prime placement at
frequency resolution `B^{-1}`—physical resolution `Y/B=Y^{-17/33}<1`—and
the multiplicative/consecutive-prime correlations bundled into that mask.
Saying merely “prime anti-quadrature” is not progress: unless it is stated
with the `.0189` or `.0179` rate and independently proved, it is just LTRAD
or the source-fiber target renamed.

Known same-side progression rigidity, pair counting, localized-carrier
exclusion, tensor/SR2PF restrictions, and generic rational independence do
not exclude this diffuse morphology.  Accordingly, the bifurcation's
promotion branch has no certified candidate.

## 5. Verification and formal scope

The executable replay is

```bash
PYTHONPATH=src pytest -q src/test_qp_source_fiber_bifurcation.py
python3 src/qp_source_fiber_bifurcation.py --order 101 --depth .2
```

It passes eight tests, checks the finite source and projective identities,
matches the Fejér square formula, and checks the rational exponent ledger.

The Lean files

- `lean/rhbridge/RHBridge/QPSourceFiberBifurcation.lean`, and
- `lean/rhbridge/RHBridge/QPSourceFiberBifurcationAudit.lean`

kernel-check `(1.1)`, the two normalizations, the finite convex dual upper
bound, and the exponent comparisons.  Their axiom audit reports only
`propext`, `Classical.choice`, and `Quot.sound`.  Lean does not formalize the
probabilistic real-node construction or any actual-prime asymptotic theorem.

## 6. Decision

```text
direct abstract LTRAD in the filled real-node model:  FALSE
source-fiber lower bound in that model:                FALSE
all catalogued mask-coarser restrictions sufficient:  FALSE
separate quantitative actual-prime invariant found:   NO
actual-prime LTRAD_P(.0189,.001):                      OPEN
DPA_P(.019):                                           OPEN
QP/Turan branch under the stop rule:                   PARKED
uniform zero-free strip:                               NOT PROVED
sharp four-cycle bound:                                OPEN
RH:                                                     NOT PROVED
```

The useful result is a clean boundary: any future QP/Turán proof must use an
actual-prime theorem strong enough to distinguish deterministic prime
placement from an equidistributed, diffuse, prime-density quadrature at the
full aperture.  Everything weaker has now been stress-tested away.

## Sources

- `results/ZETA23-PWCT-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`
- `results/ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md`
- `results/ZETA23-QP-RADIALIZATION-MASS-NORMALIZATION-GATE-2026-08-15.md`
- `results/ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`
- `results/ZETA23-COEFFICIENT-SENSITIVE-RADIALIZATION-LITERATURE-PASSPORT-2026-08-31.md`
