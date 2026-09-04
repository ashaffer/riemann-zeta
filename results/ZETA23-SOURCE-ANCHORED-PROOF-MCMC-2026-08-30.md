# Source-anchored proof MCMC for a uniform zero-free strip

**Date:** 2026-08-30  
**Status:** 58 named proof states, cold-posterior mutations, 20 Bellman
rollouts, and the COSE and PWCT proof-or-counterexample audits completed.
Their actual-prime statements remain open and their tested soft relaxations
are refuted.  No uniform zero-free strip and no proof of RH.

## 0. Outcome

The run did not converge to a proof.  It converged to a sharper and more
honest fork.

```text
hypothetical bad prime event
        |
        v
source-conditioned extremal separator + its exact KKT contact measure
        |
        +-- strict carrier/corrector deficit -> transverse return
        |
        +-- diffuse near-isometry
        |       +-- abstract carrier relaxation -> refuted by Fejer model
        |       +-- actual-prime carrier COSE -> open; equals LTRAD if no pairs
        |       `-- carrier overshoots -> many-peak corrector gate (open)
        |
        `-- low-entropy autocorrelation
                 +-- product/digit seed -> tensor SR2PF (closed)
                 `-- Sidon/diffuse seed
                          +-- span < m sqrt(Y) -> half-integer triangle (closed)
                          `-- wider span -> exact small E-defect charts
                                      -> global rank-two prime completion
                                      -> projective small-defect rigidity (open)
```

The important negative result is that the old fork

```text
near-Bessel saturation -> digit tensor -> tensor SR2PF
```

is false even in the abstract source/floor class.  Equality may be a diffuse
coisometry, and exact Fejer saturation may come from an arbitrary Sidon seed.
The faithful tensor SR2PF theorem remains useful, but it is only a terminator
for the low-entropy product subbranch.

The subsequent Bellman audit retired APDIE as ill-typed, proposed SCPSI, and
then found that SCPSI is equivalent to exponent-level LTRAD relative to the
proved energy upper bound.  An abstract relaxation of its next proposal,
**COSE**, has now been refuted by a mass-legal synthetic carrier-only Fejer
model.  Actual-prime COSE remains
open, but it is not uniformly a reduction: when there are no close reflected
pairs its carrier subspace is the full coefficient space and it is exactly
LTRAD.  A distinct many-peak corrector theorem is relevant only after an
actual-prime carrier overshoot has first been proved.  Only after a
source-to-shadow test returns a genuine arithmetic deficit should one invest
in a tensor extraction theorem.
A second, more concrete downstream target is **RSDR**, rigidity of the exact rank-one small
multiplicative-defect charts produced by a transported Sidon autocorrelation.
RSDR is a sharper interface to the former broad PQR target, not yet a
logically smaller hypothesis class.

## 1. What “proof MCMC” means here

A language model does not expose a literal coordinate chart on its hidden
activations.  The operational replacement used in this run was a stochastic
particle search over typed proof sketches.  Randomness generates proposals;
it never licenses an inference.

### 1.1 State type

A proof particle is a directed theorem graph.  Each edge stores

```text
claim; quantifiers; scale; height range; ordinary-prime mask;
source normalization; sign/floor; precision; exponent; inherited data.
```

The frozen target is the audited conditional chain

```text
DPA_P(.019) + LTRAD_P(.0189,.001)
       -> no directional event of depth Y^-.001
       -> a fixed zero-free width 10^-6.                 (1.1)
```

For a bad source event,

```text
v=a_P(t_0)+Dq_P,              D>=Y^(-.001+o(1)),
epsilon=Y^(-.0179+o(1)),      Delta=Y^(16/33),
```

and the exact transverse target is

```text
s_v=inf_(y:y.v=-1) sup_(t in H_Y)y.a_P(t) >=epsilon.   (1.2)
```

Multiplication by `D` gives the radial exponent `.0189`.

### 1.2 Proposal kernels

The hot sampler randomly applied the following mutations:

```text
Q  replace a universal theorem by an event-conditioned theorem;
D  dualize a separator into its positive contact measure;
S  replace a bound by stability/classification of its equality case;
T  tensorize a structured obstruction;
A  retain ordinary-prime labels through an arithmetic invariant;
M  add a second physical center or scale;
L  localize while demanding inherited source and floor data;
X  splice two independently incomplete chains.
```

Every proposal was paired with an antithetic hostile state: digit versus
Sidon, low rank versus diffuse coisometry, synthetic versus actual prime,
source resolution versus `B`-scale resolution, or local versus hereditary
floor.

### 1.3 Energy and acceptance

The energy was infinite if a state

- reversed an implication or lost a quantifier;
- discarded the ordinary-prime mask, source normalization, or global floor;
- used `Y^-1` source resolution where `B^-1=Y^(-50/33)` was required;
- paid a fixed exponent loss beyond `.0179`;
- was refuted by a state satisfying all advertised hypotheses; or
- renamed the strip, LTRAD, broad SR2PF, or another open theorem as a lemma.

Finite energy penalized independent open edges, exponent debt, inheritance
debt, and distance to a proved terminator, while rewarding a decisive fast
falsifier.  Low-energy diverse particles were resampled with the usual
formal weight `exp(-E/T)` and mutated as the temperature was lowered.  The
weights are research-search heuristics, not mathematical probabilities.

Finally, particles were canonicalized by their first unproved edge.  This
equivalence collapse is essential: twenty eloquent routes whose first edge
is LTRAD are one route, not twenty pieces of evidence.

## 2. Pool and annealing history

The run produced 58 named particles:

| round | particles | purpose |
|---|---:|---|
| hot | 37 | six broad clusters: tensor, corrector, upper antenna, direct zero, multiscale, orthogonal/exotic |
| splice | 6 | combine the best independently incomplete chains |
| hostile-conditioned | 15 | five quotient-graph, five full-KKT, and five event-certificate mutations |

The full cards, exponent ledgers, and fast falsifiers are in
`ZETA23-VIBE-MCMC-CANDIDATE-POOL-2026-08-30.md`.

### 2.1 First collapse

The following received zero continuation weight:

```text
generic fourth moments or the sharp four-cycle endpoint:
    best audited conversion misses .0179 by about .603312;

average zero density / almost-all cancellation:
    cannot exclude one zero;

moving-contour or harmonic-access optimization:
    returns the original zero-exclusion estimate;

ordinary Nyman L2 approximation:
    does not control one collar evaluation;

bounded contact/template reductions:
    contact supports can grow with prime dimension;

generic BSG/DRC/localization:
    source, sign, floor, or prime labels are not hereditary.
```

### 2.2 Second collapse: the critical-saturation mistake

The apparent exponent match

```text
||y_corr|| <=epsilon sqrt(Delta),
# orthogonal queries =Delta
```

does not imply tensor structure.  A coisometry `U` with carrier query vector
`c` admits `z=-U* c`, which cancels every query and exactly saturates the
budget while having stable rank `Delta`.  One source-null constraint removes
only one dimension.

There is also an exact nonlinear countermodel.  For every finite integer set
`A={a_1,...,a_m}` define

```text
K_A(t)=m^-1 |sum_j exp(i omega a_j t)|^2,
F_A(t)=[1-K_A(t)]/[2(m-1)].                          (2.1)
```

Then

```text
F_A(t)<=1/[2(m-1)]        for every real t,
F_A(0)=-1/2.                                             (2.2)
```

If `A` is Sidon, all positive differences are distinct and the support has
order `m^2`, with no forced tensor factors or long progression.  Thus
critical one-sided saturation does not imply a digit box.  Perfect-difference
sets appearing in exact Turan power-sum extremizers reinforce the warning,
but cyclic differences must not be mistaken for a consecutive real
difference interval.

### 2.3 Third collapse: KKT is a spine, not a bridge

Under the radial-feasibility/facial-reduction hypotheses used in the audited
QP formulation, compactness of `H_Y` and finite-dimensional convex duality
give

```text
s_v=max{r:-r v in conv{a_P(t):t in H_Y}}.            (2.3)
```

When the optimum is attained, there is a probability contact measure `nu`
with

```text
int a_P(t)dnu(t)=-s_v v,
supp(nu) subset {t:y.a_P(t)=s_v}.                    (2.4)
```

This is exact and source-preserving.  It does not, however, factor the signed
separator `y`.  The function `s_v-F_y` is nonnegative only on a finite
nonharmonic band, so global Fejer--Riesz factorization is unavailable.  The
KKT measure also does not force contacts near `B`, `B^-1` superresolution, or
a prime-valued quotient graph.  Its Bochner Gram has complex Fourier values
at `log(p/q)`; its entries are not primes and integer-minor arguments do not
apply.

Consequently the third-generation cards

```text
K1: KKT -> superresolved prime quotient graph,
G3: quotient cycles -> divisor contradiction
```

collapse respectively into an unproved superresolved signed-factor theorem
and the open PQR theorem.  They are useful theorem names, not deductions.

## 3. Exact gains from the run

These are exact within their stated scope and are not a strip proof.  They are
new to this project audit; no claim of literature-level novelty is made.

### 3.1 Canonical contact saddle

Equations `(2.3)--(2.4)` provide the right common coordinate system for every
future LTRAD proposal.  Complementary slackness retains the source, the
continuum cap, and positivity of the radial measure simultaneously.  It also
prevents a recurring mistake: positivity belongs to `nu`, not to the signed
prime coefficients `y`.

### 3.2 Arbitrary-seed Fejer obstruction

Equations `(2.1)--(2.2)` prove an exact family of diffuse, one-sided
saturators.  It enlarges the abstract obstruction class from digit products
to arbitrary difference sets.  Any valid inverse theorem must therefore
have at least three outputs: strict deficit, diffuse saturation, and
low-entropy/product saturation.

### 3.3 Conditional Sidon-to-PQR reduction

Suppose a Sidon state of size `m=Y^(.0179+o(1))` is transported to distinct
same-side prime logarithms with weighted error

```text
sum_(i>j) e_ij/[m(m-1)] <=kappa/(mB).                (3.1)
```

Markov plus Turan's independence bound removes only `O(m)` bad edges and
leaves a linear-size all-good vertex set.  On every ordered row/column cut,

```text
p_ij=Y exp[+/- omega(a_i-a_j)]+O(Y/B).               (3.2)
```

The reference block has rank one.  In every cubic determinant the zero-error
and one-error terms cancel, leaving

```text
det(p_ij)=O(Y^3/B^2)=O(Y^(-1/33)).                  (3.3)
```

The determinant is integral, hence zero.  Quadratic minors are nonzero by
unique factorization and have size

```text
H=Y^2/B=Y^(16/33).                                  (3.4)
```

Thus a transported Sidon state produces an exact rank-two **quasiseparable
prime ratio shadow**: every ordered cut has rank at most two, with a nested
system of bounded rational Pluecker generators.  This is strictly more
structured than one broad SR2PF matrix and strictly less structured than an
all-cut digit tensor.

There is a stronger elementary constraint which was found in the cold audit.
Write the cleaned vertices as `b_1<...<b_M`, put

```text
g_r=b_(r+1)-b_r,              omega=2pi/t_0,
W=Y omega(b_M-b_1).                                  (3.5)
```

For three consecutive vertices and either common side of `Y`, the reference
nodes obey the exact identity

```text
X_(r+2,r+1)+X_(r+1,r)-X_(r+2,r)-Y
  =-Y(e^(sigma omega g_(r+1))-1)
      (e^(sigma omega g_r)-1),       sigma in {+1,-1}. (3.6)
```

The corresponding combination of the three transported primes is an
integer, whereas `Y=N+1/2`.  Its distance from `Y` is therefore at least
`1/2`.  The `O(Y/B)=o(1)` transport error in `(3.2)` and `(3.6)` imply the
quantitative adjacent-gap law

```text
g_r g_(r+1) >>1/(Y omega^2).                          (3.7)
```

Pairing disjoint adjacent gaps and applying AM--GM gives the new exact
necessary condition

```text
b_M-b_1 >>M/(omega sqrt(Y)),
W >>M sqrt(Y).                                       (3.8)
```

Thus the entire same-side transported branch is already impossible when
`W=o(m sqrt(Y))`.  At the target `m=Y^(.0179+o(1))`, a surviving shadow must
span at least

```text
W>=Y^(.5179-o(1)).                                   (3.9)
```

This half-integer triangle theorem uses only integrality after the analytic
transport; it does not need rank-two classification or a sieve.

Its symbolic identity, exponent ledger, and exact prime one-cut sanity
fixture replay with

```bash
python3 results/verify_zeta23_vibe_triangle.py
```

The missing arithmetic theorem is

```text
PQR: every such prime quasiseparable ratio shadow has
     m <<(log Y)^C.                                  (3.10)
```

PQR is open.  The proved broad projective sieve gives only
`m<<Y^(4/33+o(1))`, far above `Y^.0179`.  For reflected pairs, the extra
integer

```text
G_ij=4p^-_ij p^+_ij-(2Y)^2,
0<|G_ij|<<Y^(16/33)                                 (3.11)
```

is injective, but by itself yields only `m<<Y^(8/33)`.  The proposed `PQR+G`
must couple `(3.11)` to the nested Pluecker relations.

For a near-minimal Sidon ruler, `diam(A)=Y^(.0358+o(1))`.  Combining its
physical span `W~Y diam(A)/t_0` with `(3.8)` closes this particular branch
when

```text
t_0>Y^(.5179+o(1)).                                  (3.12)
```

Only the narrow source-height window `Y^.5<=t_0<=Y^.5179` remains for a
near-minimal ruler.  More generally, if `diam(A)=Y^(rho+o(1))` and
`t_0=Y^(alpha+o(1))`, the half-integer theorem excludes
`alpha>1/2+rho-.0179`.  Widely spaced rulers remain open.  This supersedes
the weaker `.696133` boundary from the localized-carrier theorem within this
same-side transported branch.

### 3.4 Exact multiplicative-defect charts

The final mutation found a stronger invariant than the rank-two PQR cuts.
For each transported prime triangle put

```text
Q=2Y,                        d_ab=2p_ab-Q,
K_kji=d_ki-d_kj-d_ji,
E_kji=QK_kji-d_kj d_ji
     =2(Qp_ki-2p_kj p_ji).                           (3.13)
```

The decomposable exponential reference has `E*=0`.  Pointwise transport at
error `delta=Y/B` therefore gives

```text
0<|E_kji|<<Y delta=H=Y^(16/33),
E_kji=2 (mod 4).                                    (3.14)
```

The fixed shell also makes every participating prime coprime to `Q`, and
direct reduction of `(3.13)` gives the corresponding edge/Q gcd law.  More
importantly,

```text
E_kji=-d_kj d_ji (mod Q).                           (3.15)
```

For fixed `j`, `(3.15)` is a rank-one outer product modulo `Q`.  Every
quadratic minor of the integer matrix `(E_kji)_(k>j,i<j)` is consequently
divisible by `Q`, but its size is

```text
O(H^2)=O(Y^(32/33))=o(Q).
```

All these minors vanish exactly.  Since `(3.14)` excludes zero entries,
every nonempty fixed-middle `E` slice has rational rank one, with no extra
width restriction.  Primitive integral factors are modular rotations of the
incident residues `d_ab`.

Four vertices also obey the exact associator

```text
Q E_lki+2p_lk E_kji=Q E_lji+2p_ji E_lkj.            (3.16)
```

This identity is information-neutral: after division by `Q^3`, both sides
are identically `s_li-s_lk s_kj s_ji` for arbitrary edge labels.  It cannot
stabilize the rotations or generate height entropy.  The hostile audit also
gives an exact one-pivot composite family with positive
odd rank-one `K`, nonzero rank-one `E`, the required height, parity, gcd, and
transport error.  Thus no local divisor argument can work.

### 3.5 Global projective completion

There is nevertheless an exact global classification.  Set

```text
s_ki=2p_ki/Q,                 s_ii=1.
```

For every pivot `j`, form the southwest cut
`B_j=(s_ki)_(k>=j,i<=j)`.  Subtracting `s_kj` times pivot row `j` from each
lower row converts its lower block to `[E^(j)/Q^2 | 0]`; hence

```text
rank(B_j)=1+rank(E^(j))<=2.                          (3.17)
```

The terminal two-column minor is nonzero, since its vanishing would equate
two products of four distinct edge primes.  Columns one and two therefore
span every suffix cut.  It follows that there are two-dimensional row and
column vectors with

```text
s_ki=u_k v_i,                  u_i v_i=1             (3.18)
```

for all `k>=i`.  Conversely, `(3.18)` gives

```text
E_kji/Q^2=det(u_k,u_j)det(v_i,v_j).                 (3.19)
```

Thus all-pivot rank-one defects are exactly a global rank-two-completable
projective system in the nondegenerate prime branch.  This is a sharper
normal form, not a size bound: arbitrary `GL_2` projective chains can be
arbitrarily long.  The corrected **RSDR** target must obtain its gain from
prime values, the small nonzero quantized determinants `(3.19)`, gcd laws,
and modular rotations.  A structured output would still need a proved
adapter into PHR2 or tensor SR2PF.

The identities and exponent lift replay with

```bash
python3 results/verify_zeta23_vibe_e_defect.py
```

## 4. Preliminary source-saddle probe

The script `src/qp_source_saddle_probe.py` constructs a finite actual-prime
source direction and independently solves the sampled radial and separator
LPs.  It is a geometry probe, not an asymptotic event certificate.  In
particular, feasible scales do not meet the enormous prime-count threshold
of the `.001` source event.

With 8,001 sampled contact times it returned:

| center | prime coordinates | source depth | radius | contact atoms | effective atoms | weighted stable rank | max contact / band top |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100.5 | 8 | .253681 | .511683 | 8 | 4.94 | 2.58 | .688 |
| 200.5 | 15 | .362218 | .546312 | 15 | 8.86 | 3.09 | .930 |
| 400.5 | 27 | .257718 | .404742 | 27 | 17.91 | 6.46 | .944 |

Primal-dual gaps were below `1.2e-13`.  The contact support grew exactly with
the prime dimension in these instances, and the weighted stable rank grew as
well.  This refutes the bounded-contact heuristic at finite scale and makes
the diffuse branch operationally real.  The later Bellman audit extended
this probe to contact conditioning and signed `B^-1`-shift response; see its
companion report.  These runs do not decide asymptotic LTRAD because the
sources are not legal and the LP is floating point on a sampled band.  The
later rejection of SCPSI as an intermediate lemma is logical, not numerical.

Replay with

```bash
PYTHONPATH=src python3 src/qp_source_saddle_probe.py \
  --source-points 12001 --contact-points 8001
```

## 5. Cold posterior: three surviving research cards

### 5.1 COSE audit and the remaining actual-prime split

The Bellman audit found that APDIE's stable rank, whitening, cancellation
norm, and KKT-measure quantifier were undefined, while its escape clause
embedded the desired transverse return.  It therefore receives no proof
reward.

SCPSI temporarily replaced it with one invariant functional.  For the canonical
reflected-pair split write the exact corrector as `F_corr=Q dot Psi`, put
`g=(F_car-epsilon)_+`, and define

```text
Xi(y)^2=sup {int g^2 dmu:
             mu>=0, int Psi Psi^T dmu<=I}.
```

Separator cancellation and the proved energy bound give

```text
Xi(y)<=||Q||_2<<epsilon sqrt(Delta)Y^o(1).
```

SCPSI conjectured the incompatible actual-prime lower bound
`Xi(y)>>epsilon sqrt(Delta)Y^(eta/2)` when
`epsilon=Y^(-(.0179+eta))`.  But every assumed separator already supplies
the feasible SDP-dual certificate `Z=Q Q^T`, and the lower bound contradicts
the proved upper exactly when such a separator exists.  Conversely LTRAD
makes the quantified class empty.  SCPSI is therefore LTRAD-equivalent, not
an intermediate edge.

The proposed split was:

1. **COSE:** exclude source-conditioned separators lying in the canonical
   carrier subspace; and
2. after COSE forces quantitative carrier overshoot, prove that sufficiently
   many covariance-controlled peaks prevent the reflected corrector from
   cancelling them all.

The abstract relaxation of the first statement is false.  Take
`m=ceil(Y^(.0179+2eta))` active one-sided arithmetic-mesh frequencies and a
prime-scale population of zero-coefficient source nodes in negative-phase
arcs.  This satisfies the original mass-normalized event threshold, while a
scaled Fejer polynomial has source normalization `-1` and cap
`asymp 1/m<<Y^(-(.0179+eta))`.  Because every node is one-sided, the entire
separator lies in the carrier subspace.

This does not refute actual-prime COSE: the construction selects its node
mask and exact arithmetic mesh, whereas a legal event is a contiguous
interval of ordinary primes.  The projected frame argument gives only
`Y^(-1+o(1))`.  Moreover, if an actual-prime shell has no close reflected
pairs, carrier COSE is literally LTRAD.  Therefore the honest remaining split
is either a genuinely prime-sensitive proof/counterexample for COSE, or a
theorem that a legal event forces a quantitatively large reflected sector,
followed in its overshoot branch by many-peak cancellation.  The exact audit
is in `ZETA23-COSE-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`.

### 5.2 RSDR -- downstream arithmetic terminator

RSDR is the sharpened interface to PQR.  Its displayed axioms are
consequences of the same PQR approximation, so they do not yet define a
logically narrower input class.  It is nevertheless precise and finitely
falsifiable, but it only becomes relevant after a separate analytic theorem
transports a separator or autocorrelation to `B^-1`-accurate prime nodes.
Its usable normal form is the global rank-two completion `(3.18)`, equipped
with short nonzero signed determinant factors, prime gcd laws, and modular
rotations.  The associator `(3.16)` is tautological and has been removed from
the evidence.  Proving RSDR would close these arbitrary Sidon shadows; it
would not supply the analytic transport.  The
half-integer triangle law means it is needed only at physical span
`W>>m sqrt(Y)`.  Even constant modular rotations would still require a
proved adapter before PHR2 or tensor SR2PF could be invoked.

### 5.3 Event-conditioned upper certificate

The current universal split may still be too strong.  For the same bad event
one may seek either

```text
r(q_P)<=Y^(-.019+o(1)),
r(v)>=Y^(-.0179+o(1)),                              (5.1)
```

or a prime-specific common obstruction.  However, an exact abstract convex
countermodel gives the `q_P` and `v` systems arbitrary radial values and
disjoint KKT supports despite the source relation.  Merely pairing the two
LPs is therefore removed from the posterior.  A genuinely event-conditioned
prime-only upper certificate remains open and would replace the universal
`DPA_P` input.

## 6. COSE-X outcome

**COSE-X** compared unrestricted and carrier-constrained saddles on six
finite actual-prime surrogates.  The carrier restriction raised the sampled
radius by about `6.6%` in the smallest case and by an unresolved amount in
the two largest cases.  Every carrier radius remained below the
unit-constant finite plug-in `Y^(-.0179)`.

These observations are diagnostic only.  The asymptotic `o(1)` and constants
do not define a finite threshold, the sampled depths were only `.14--.49`
while `Y^(-.001)` is about `.992--.994` at these sizes, the exchange bounds
are floating, and there were only one to three close pairs.  In particular,
the runs neither test nor refute asymptotic COSE.  They do show that corrector
cancellation was not the first obstruction in these six surrogate problems.

The experiment used the following stop logic:

1. solve the unrestricted source-conditioned separator by exchange;
2. solve the same minimax problem with `y` restricted to the canonical
   carrier subspace;
3. compare the unrestricted and carrier-constrained transverse radii and
   certify their continuum caps with interval derivative guards;
4. only when the carrier radius clears the target while the unrestricted
   radius does not, form `g` and evaluate the `Xi` peak-packing SDP; and
5. repeat on actual primes and matched synthetic, Sidon, coisometric, and
   projective controls.

```text
carrier radius already below target         -> corrector cancellation is not
                                              the first obstruction;

carrier clears target, unrestricted fails   -> isolate the many-peak
                                              corrector theorem;

actual-prime-only spectral deficit          -> isolate and prove that
                                              arithmetic inequality;

low entropy/product factors                 -> only then invoke tensor SR2PF;

no asymptotic scaling law                    -> treat finite data as diagnostic,
                                              not evidence for a strip.
```

The Bellman backup now dependency-discounts **RSDR-X** until a faithful
signed source-to-projective transport has been proved.  The complete reward
ledger, transport-precondition run, SCPSI equivalence audit, and COSE
proof-or-counterexample audit are in the companion reports.

## 7. Final status

```text
named proof particles sampled:                         58
exact KKT contact identity:                            PROVED
arbitrary-seed Fejer diffuse obstruction:              PROVED
bounded-contact / tensor-only saturation hypothesis:   REFUTED
Sidon weighted cleaning and ordered determinant gate:  PROVED CONDITIONAL
same-side half-integer triangle spacing law:            PROVED CONDITIONAL
small E defect, parity/gcd, and exact slice rank one:    PROVED CONDITIONAL
E residue rotations:                                    PROVED CONDITIONAL
four-vertex E associator:                                PROVED / INFORMATION-NEUTRAL
global rank-two projective completion:                   PROVED CONDITIONAL
RSDR / PQR / PQR+G:                                    OPEN / DOWNSTREAM
APDIE:                                                 RETIRED / ILL-TYPED
SCPSI as an intermediate lemma:                        RETIRED / LTRAD-EQUIVALENT
abstract source/carrier relaxation of COSE:            REFUTED
COSE (actual-prime statement):                         OPEN / NOT A UNIFORM REDUCTION
many-peak corrector cancellation:                      OPEN
paired q/v saddle from convex geometry alone:          REFUTED
event-conditioned prime-only upper theorem:            OPEN
DPA_P(.019):                                           OPEN
LTRAD_P(.0189,.001):                                   OPEN
uniform zero-free strip:                               NOT PROVED
RH:                                                    NOT PROVED
```

## 8. Companion artifacts

- `ZETA23-BELLMAN-REWARD-SAMPLING-2026-08-30.md`
- `ZETA23-COSE-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`
- `ZETA23-VIBE-MCMC-CANDIDATE-POOL-2026-08-30.md`
- `ZETA23-VIBE-MCMC-ADVERSARIAL-FALSIFIER-2026-08-30.md`
- `ZETA23-VIBE-PRIME-QUASISEPARABLE-RATIO-SHADOW-2026-08-30.md`
- `ZETA23-VIBE-PQR-HALF-INTEGER-TRIANGLE-COLLAPSE-2026-08-30.md`
- `ZETA23-VIBE-PQR-ODD-CURVATURE-CHARGE-ADDENDUM-2026-08-30.md`
- `ZETA23-VIBE-PQR-E-DEFECT-ROTATION-AND-ASSOCIATOR-2026-08-30.md`
- `ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`
- `ZETA23-UNIFORM-STRIP-DECISION-TREE-CONSOLIDATION-AND-MAXIMUM-INFORMATION-GAIN-2026-08-30.md`
- `ZETA23-PWCT-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`

## 9. PWCT posterior update

The positive-weight carrier specialization closed the source-time and
low-participation branches but not the diffuse branch.  A smooth real-node
model retaining prime-scale density and gaps, a contiguous legal source,
positivity, and unpaired carrier support attains
`rho_+(v)<=Y^(-.499+o(1))`.  Thus any actual-prime proof needs a new
deterministic arithmetic discrepancy theorem; source geometry and moment
estimates are insufficient.

PWCT also lacks a terminal adapter to the signed `DPA_P(.019)` currently in
the strip chain.  The exact repair is diffuse positive `PDPA_+(.019)`:
averaging its close reflected pairs costs only `Y^(-17/33+o(1))`, producing
the needed positive-carrier upper antenna.  This sufficient repair is not a
new target: it strictly strengthens the already-audited positive-antenna
program, and its failure would leave non-diffuse carrier antennas open.  The
posterior therefore demotes PWCT as a standalone target and first compares
the exact event-free carrier value with unrestricted and diffuse-capped
positive values before reopening that program.  That comparison is now
complete through `Y=8000.5`: the diffuse cap has a small shrinking relative
penalty, while primal support and dual contact count grow with dimension and
the sparse carrier has negligible effect.  It leaves the old adaptive
actual-prime convex-hull/covariance theorem, not a new generic lemma.
