# Two-wave orthogonal fail-fast reset

Status: two research waves completed, 2026-08-04.  Ten mechanisms were given
explicit carriers and kill gates.  No proof of RH is claimed.

## Executive result

The exercise produced one exact new repository reduction, several finite or
structural no-go results, and a sharper search law.  It did not produce a new
lemma known to block RH.

The common failure is no longer best described as “not enough positivity.”
It is an information mismatch:

> A hypothetical off-line zero is a globally coherent complex phase defect.
> Most tractable structures retain only real positivity, magnitude, density,
> finite moments, or averaged mass.  They erase the defect before their strong
> theorem is applied.

The few constructions that retain the phase exactly are trace identities,
equivalent criteria, or meromorphic continuations.  They detect the defect but
do not supply an independent order that excludes it.

## 1. Admission protocol used in both waves

Each proposal was required to state:

1. the exact object changed by one arbitrarily high off-line quartet;
2. the topology in which that change does not vanish;
3. how primes, gamma, poles, and the functional equation enter before any sign
   claim;
4. an independent amplifier or exclusion theorem;
5. a global closure/no-escape statement; and
6. a finite countermodel or scale comparison capable of killing the route.

A detector without an exclusion engine was not counted as progress.

## 1.1 Pre-wave gate: cyclotomic connectivity

The requested cyclotomic two-prime calculation was completed first.  Local
finite-field determinant traces are genuine, but their direct sum merely
recovers the Euler product.  A finite commuting model cannot use one linear
trace to keep all pure moments while killing all raw mixed moments.  But
tensor/Fock gluing followed by connected extraction is compatible with a
separate positive polarization, so the broad architecture is not ruled out.
Current constructions lack a canonically integrated all-prime archimedean
realization and compatible pairing.  The narrow gate is closed; the general
path remains a long-horizon open program.  See
`CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md`.

## 2. Wave one: five phase-erasing structures

### 2.1 Bost--Connes Gibbs partition trace -- killed

The Bost--Connes Hamiltonian has

```text
H e_n = log(n)e_n,       Tr(exp(-sH))=zeta(s), Re(s)>1.
```

This trace formula does not continue as a positive trace-class Gibbs partition
function into the critical strip: `zeta(sigma)<0` for every real
`0<sigma<1`.  This does not deny the existence of Bost--Connes KMS states in
that range; it kills this particular Gibbs-trace realization.  Moreover, the
finite positive partition function `1+2 exp(-s)` has complex-temperature zeros on
`Re(s)=log 2`; positive coefficients can put that line at an arbitrary real
location, not specifically `1/2`.  Positivity at real temperature has no
critical-line force after complexification.  The naive Gibbs partition-trace
mechanism is definitively pruned, not every possible use of the Bost--Connes
system.  Primary anchor:
[Bost--Connes](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38.pdf).

### 2.2 O-minimal tameness -- killed as a global engine

An o-minimal definable subset of a line cannot be an infinite discrete set, so
the full critical-line zero set cannot be made tame in the needed sense.
Height-truncated sets with complexity growing with height are harmless but
give no global bound.  If one fixed o-minimal definable family had fibers
equal to all the height-truncated zero sets, uniform finiteness would bound
their component counts and contradict the growth of `N(T)`.  Recent work
describes optimal bounded domains of definability rather than a global
imaginary-unbounded one
([Padgett--Speissegger](https://arxiv.org/abs/2506.15119)).

The `Pi_1` presentation of RH remains useful for proof-theoretic bookkeeping;
it is not an analytic exclusion mechanism.

### 2.3 Tropical/amoeba geometry -- phase-blind version killed

The reciprocal polynomials

```text
P(z)=z^4+z^3+z^2+z+1,
Q(z)=z^4+z^3-z^2+z+1
```

have the same support and ordinary coefficient valuations.  Both have the
same reciprocal functional symmetry.  All roots of `P` are on the unit
circle, while `Q` has a reciprocal real pair off it.  Ordinary tropicalization
therefore cannot distinguish an RH configuration from an off-line one.

Exact Ronkin/amoeba data can distinguish them, but then contains the radial
zero distribution being sought.  Only a new arithmetic coamoeba phase law
could revive the path.

### 2.4 `W_1` and integrated transport discrepancy -- insufficient

For

```text
nu_X = psi(X)^(-1) sum_(n<=X) Lambda(n) delta_(n/X),
```

one has exactly

```text
W_1(nu_X,dt)
 = 1/(X psi(X)) integral_0^X
     |E(u)-uE(X)/X| du,       E(u)=psi(u)-u.
```

Monotonicity forces a discrepancy spike of height `H` to contribute at least
on the scale `H^2/X^2` to `W_1` (up to endpoint and atomic-weight caveats).
Thus an RH-scale `W_1` upper bound yields only a pointwise bound near
`X^(3/4)`, not the square-root scale.  `W_infinity` retains the required
supremum discrepancy, but
its square-root bound is essentially the RH prime-number-theorem error term.
Generic `W_1` arguments, and arguments using only the same integrated
discrepancy, are pruned.  This calculation alone does not rule out every
`W_2` or entropy construction; any such revival must state how it prevents
localized spikes without importing pointwise prime control.

### 2.5 Fractal-string inverse spectra -- exact but equivalent

The spectral operator is multiplication by `zeta(c+it)`.  Uniform bounded
invertibility is false for `1/2<c<1`: universality makes its modulus
arbitrarily small even on a zero-free line.  Truncated quasi-invertibility is
the zero-free-line assertion itself.  The fractal-string formulation remains
an elegant equivalence but supplies no simpler coercive theorem.  Primary
anchors: [Lapidus--Maier](https://doi.org/10.1112/jlms/52.1.15) and
[Voronin](https://www.mathnet.ru/eng/im2037).

## 3. First regrouping

The five mechanisms use thermodynamics, logic, tropical geometry, transport,
and spectral geometry, yet fail at one common interface:

```text
completed complex phase
        -> magnitude / average / real order
        -> strong theorem
```

The first arrow is irreversible.  Functional-equation symmetry does not
restore the discarded phase.  This led to a second wave using carriers that
retain exact cancellation.

## 4. Wave two: five cancellation-preserving structures

### 4.1 Plain finite-field ultraproduct transfer -- insufficient

Every reduction of `P^1_Z` modulo `p` has

```text
Z(P^1_Fp,t)=1/((1-t)(1-pt))
```

and satisfies finite-field RH, whereas

```text
zeta(P^1_Z,s)=zeta(s)zeta(s-1).
```

This is a hardness calibration: a theorem transferring the expected global
zero lines would already prove ordinary RH.  Bare field-language Los transfer
does not automatically form an Euler product over its indices, retain a
rescaled square-root Frobenius fluctuation through `p -> infinity`, or create a
real gamma place.  Prismatic cohomology genuinely compares realizations after
one prime is fixed, not all primes and infinity simultaneously
([Bhatt--Scholze](https://arxiv.org/abs/1905.08229)).

Plain first-order ultraproduct transfer from local purity is therefore
insufficient.  Enriched difference, nonstandard counting, or Loeb structures
are not ruled out; they must visibly add the missing cross-prime and
archimedean information.  A global absolute geometry is a different,
long-horizon proposal, not a formal consequence of finite-field purity.

### 4.2 Natural fixed-partner automorphic replication -- killed

For irreducibles,

```text
Hom(1, pi tensor pi') = Hom(dual(pi),pi').
```

The trivial constituent, and hence a formal zeta factor, occurs only on the
diagonal `pi'=dual(pi)`.  Turning a hypothetical zeta zero into an actual zero
of the convolution also requires that the remaining adjoint quotient be
holomorphic there; this is a noncancellation hypothesis in general (or one may
restrict to ranks where the needed adjoint holomorphy is known).  Even under
that hypothesis, a fixed-partner Rankin--Selberg family contains at most one
such isomorphism class.  Moving along the diagonal copies the same imprimitive
factor but leaves the hypotheses of the cited fixed-partner large-sieve
theorem; this does not rule out every diagonal-family estimate.  Any raw
diagonal zero-density theorem must accommodate the common zeta factor, while
dividing it out removes the proposed replicated zero.  Compare the
fixed-partner setup in
[Humphries--Thorner](https://arxiv.org/abs/2103.05634).

### 4.3 Conditioned Bagchi recurrence -- subtraction shortcut killed

Sup-norm recurrence of zeta on compact subsets of `1/2<Re(s)<1` has exactly
the right topology: Rouche turns one zero into recurrent replicas.  The
fail-fast obstruction is quantitative conditioning.  For

```text
A_y(eta)={tau: |p^(-i tau)-1|<eta for every p<=y},
```

For each fixed `y`, after taking the long-time limit, Kronecker recurrence
gives density on the scale

```text
exp(-c_eta y/log y),
```

whereas an *unconditional* Euler-tail `L2` bad-set bound is only polynomial in
`y`.  Subtracting that bad-set measure from the exponentially smaller cylinder
cannot prove their intersection is nonempty.

This kills only the unconditional-measure subtraction shortcut.  Finite
small- and large-prime phase blocks are Haar-independent under Kronecker
equidistribution in that fixed-`y` limit, so a relative conditional `L2`
estimate can carry the cylinder-density factor.  The real unresolved gate is
extending that control to the analytically continued zeta tail in sup norm on
a compact that may contain a zero.  Flexible Helson Euler products remain a
required countermodel audit, not a proved obstruction.  Bagchi's recurrence
equivalence is the primary anchor
([DOI](https://doi.org/10.1007/BF01903937)).

**Subsequent audit:** the relative conditional route is now pruned at fixed
`y`.  After removing the conditioned factors, its exact limiting tail is a
zero-free random Euler product.  A deterministic continued tail carrying an
off-line zero has a Rouche neighborhood disjoint from that support, so the
desired conditional frequency is zero.  Prescribed-zero Helson zetas retain
their divisor even after any finite initial prime phases are reset exactly.
See `BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`.

### 4.4 Squarefree fugacity polynomial -- one exact kill, one weak survivor

The polynomial

```text
P_N(z)=sum_(n<=N) mu(n)^2 z^omega(n)
```

satisfies `P_N(-1)=M(N)`.  Already at `N=114`, exact arithmetic gives
`P_N(z)=1+30z+32z^2+9z^3` with discriminant `-28139`.  This kills the
real-rooted/independent-spin route.

Hurwitz stability passes the finite exact gates tested, but half-plane
location yields only `|M(N)|<P_N(1)=O(N)`.  RH requires a quantitative product
of root displacements.  See
`SQUAREFREE-FUGACITY-STABILITY-GATE-2026-08.md`.

### 4.5 Mobius boundary exchange -- exact reduction, no current leverage

The exact identity

```text
M(N)=sum_(N/2<m<=N, m odd,squarefree) mu(m)
```

is Björner's homology collar.  Replacing one prime factor by two flips the
sign; the separate requirement that both endpoints lie in this collar keeps a
valid graph edge at the chosen scale.  An explicit pairing with only
`O_epsilon(N^(1/2+epsilon))` exceptions would prove RH.

Maximum matching experiments saturate the smaller parity class, but then the
unmatched count is exactly `|M(N)|` by cardinality.  The exchange endpoints
are incomparable faces, so the pairing is not a discrete-Morse cancellation.
The graph is a language for the desired cancellation, not its cause.  See
`MOBIUS-BOUNDARY-EXCHANGE-GATE-2026-08.md`.

## 5. Second regrouping: the minimal obstruction basis

The repository's many failures now factor through four mechanisms.

1. **Topology mismatch.**  A zero is nonvanishing as a pole, phase, or index,
   but tends to zero in density, normalized means, finite moments, or `L2`.
2. **Completion failure.**  Prime, gamma, pole, and theta pieces are not
   separately ordered; the global cross terms carry the useful cancellation.
3. **Identity without order.**  Duality, traces, supertraces, and functional
   equations detect the forbidden configuration but do not exclude it.
4. **Closure carries RH.**  Finite windows and finite models work; uniform
   tail control, boundary control, or identification with completed xi is the
   theorem, not cleanup.

“Coherence without mass” is the shared adversary.  For a hypothetical zero
with `beta>1/2`, prime amplitudes `p^(-beta)` are square-summable.  Quadratic
localization regards the tail as harmless even though coherent analytic
accumulation creates a pole.

### Remote-defect continuity lemma

There is a small abstract lemma behind many of the finite no-gos.  Let `D` be
a critical-line divisor, let `D_T` be obtained by inserting a symmetric
off-line quartet at height `T`, and let `Phi` be a carrier map into a
topological space such that

```text
Phi(D_T) -> Phi(D) as T -> infinity.
```

If finitely many continuous tests `F_j` have strict positive margins at
`Phi(D)`, then those same tests remain positive on `Phi(D_T)` for all large
`T`.  On any admissible class containing these synthetic perturbations, they
therefore cannot imply critical-line containment.  This is just continuity,
but it simultaneously explains the failures of finite moments, finite Taylor
cones, bounded-resolution transport, density statistics, and fixed finite
certificates.

Every successful finite-looking criterion must evade at least one hypothesis:
use a topology in which the remote quartet has nonvanishing size, an infinite
family whose margins collapse at exactly the needed rate, or a discontinuous
quantized invariant.  A zeta-specific arithmetic theorem could instead
exclude the synthetic `D_T` before applying the criterion; that would be the
missing independent engine, not a consequence of the continuous tests.  The
last two choices expose why “uniform closure” and
“integer-valued phase defect” keep reappearing in the surviving portfolio.

## 6. Revised portfolio after two waves

| Rank | Target | Why it remains | Immediate kill gate |
|---:|---|---|---|
| 1 | deterministic `p <-> qr` boundary pairing | exact Mobius endpoint; finite, combinatorial, phase-preserving | exhibit a positive-density unmatched family for every rule in a defined bounded-complexity class |
| 2 | conditioned Bagchi tail control | correct sup topology and genuine zero replication | derive relative conditional sup-norm control for the analytically continued tail; unconditional measure subtraction is inconclusive |
| 3 | quantitative fugacity root displacement | exact finite polynomial with `P_N(-1)=M(N)` | find a right-half-plane root or show qualitative stability has no recurrence capable of the required logarithmic displacement |
| 4 | global trace plus separate polarization | function-field mechanism respects the identity/order split | two-prime trace, no-mixed-term, gamma, and positivity unit tests must all pass before abstraction |
| 5 | quantized completed phase invariant | a single remote quartet cannot fade in an integer-valued topology | construct it arithmetically without using zeros and defeat flexible Euler-product countermodels |

The first three are fail-fast.  The last two have higher conceptual upside but
should receive little computation until their finite unit tests pass.

## 7. Self-prompts for the next iteration

These prompts are intentionally written to prevent the usual circularity.

### Prompt A -- canonical Mobius exchange

> Define a deterministic sign-reversing involution on odd squarefree
> `m in (N/2,N]` using only a bounded number of ordered prime factors and the
> local ratios of candidate `p <-> qr` exchanges.  Do not inspect `M(N)`, the
> two global parity counts, or a maximum matching.  Either prove its exception
> set is `O_epsilon(N^(1/2+epsilon))`, or construct an explicit positive-density
> exceptional family.  Generalize the counterexample to every rule in the
> smallest natural bounded-complexity class before proposing another rule.

### Prompt B -- conditioned recurrence

> Fix a disk `K` in `1/2<Re(s)<1` and the finite-prime phase cylinder
> `A_y(eta)`.  Use finite-block Haar independence to formulate a relative
> conditional estimate, then determine whether it closes for the analytically
> continued infinite tail in sup norm on `K`.  Track the limit before invoking
> Rouche.  Test the same closure statement against precisely specified Helson
> Euler products; do not assume in advance that they fail it.

### Prompt C -- fugacity displacement

> For `P_N(z)=sum mu(n)^2 z^omega(n)`, first search exactly for the least
> right-half-plane zero.  If none appears, derive coefficient recurrences for
> the Hurwitz determinants under `N -> N+1`.  Determine whether those
> recurrences can force
> `sum log|(1+rho)/(1-rho)| <= -(1/2-epsilon)log N`.  Kill the route if a
> stable positive-coefficient counterfamily satisfies every derived local
> inequality but has only `o(log N)` accumulated displacement.

### Prompt D -- trace/polarization separation

> Construct the smallest all-place cohomological toy object in which the
> connected signed trace gives the `p,p^2,q,q^2` von Mangoldt terms with no
> mixed primitives, while a distinct cup/star pairing is positive and obeys
> the functional-equation adjoint law.  Include the first two archimedean gamma
> modes.  If the construction splits as a direct sum, uses a plethystic
> cumulant as a positive trace, or inserts the metric after seeing the
> spectrum, stop and record the no-go.

### Prompt E -- quantized phase detector

> Find an integer-valued Fredholm, winding, or intersection invariant of the
> completed prime--gamma object that changes under insertion of one off-line
> quartet but is computable from arithmetic data without a zero count.  State
> its topology and global closure theorem first.  Reject any construction
> whose Fredholmness, trace-class renormalization, or positivity is equivalent
> to Weil's criterion.

## 8. Honest Bayesian conclusion

The probability that the current repository already contains a route that
closes RH has gone down, not up.  The probability that its negative results
can support a useful methodological paper has gone up: the two-wave audit
turns a large collection of failed ideas into a small obstruction basis with
explicit countermodels.

The boundary and fugacity constructions are useful new repository-level
reformulations, but neither is presently simpler than the Mertens criterion.
The next genuine Bayesian checkpoint is not another successful finite scan.
It is either

- a nontrivial theorem bounding exceptions for one predetermined boundary
  pairing rule, or
- a proof that zeta's conditioned Euler tail beats the exponential phase
  cylinder scale.

Absent one of those, further numerical extension should not update belief in
an RH proof.

## 9. Subsequent checkpoint update

Both alternatives above have now received their intended fail-fast audit.

- Fixed-cutoff conditioned recurrence is excluded by the zero-free support of
  the exact conditional limit.  The diagonal growing-cutoff version remains
  logically open but requires a new zero-bearing shrinking-target theorem and
  has no independent engine.
- Fixed/local boundary rules have positive-density obstruction families.  For
  the adaptive value-ordered survivor, the exact identity
  `R_g=|M(N)|+2D_g` separates the shallow allocation defect from the majority
  imbalance.  Explicit length-three paths remove all `D_g` at the retained
  checkpoints and leave `|M(N)|` exactly.
- The collar matching polynomial satisfies
  `Q_N=(1+z)A_N+U_N`, with `U_N(-1)=M(N)`.  Together with the initial
  factor-`2` cancellation, this shows that Prompts A and C are two views of
  the same squarefree-fugacity singular endpoint rather than independent
  routes.

Accordingly Prompts A--C are parked absent a new arithmetic invariant.  The
next genuinely orthogonal portfolio starts with the finite unit tests in
Prompt D (global trace versus separate polarization), followed by the quartet
cancellation gate in Prompt E.  See
`results/MOBIUS-GREEDY-DEPENDENCY-VERDICT-2026-08.md` and
`results/BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`.

## 10. Prompt D finite-gate resolution

Prompt D's genuinely new part is now complete.  The pure two-prime connected
trace and absence of mixed primitives were already available from the
semilocal trace formula and from the Euler logarithm.  In a finite
torus-equivariant Hilbert complex, an invariant positive metric makes distinct
place weights orthogonal, so an honest pure-axis connected character splits
as a local direct sum.  Virtual mixed-weight cancellation in a supertrace does
not inherit positivity.

The exact adjoint gate is even sharper: a finite generator admits `G>0` with
`A*G+GA=G` if and only if it is diagonalizable with spectrum on the critical
line.  Lean checks the minimal countermodel in which an off-line pair obeys
the alternating functional-equation duality but admits no positive adjoint
metric, together with the on-line positive control.

Thus the finite Prompt D architecture is parked.  Its infinite survivor needs
a concrete, spectrum-independent polarization on the coupled semilocal space
that is natural as primes are added; absent such a candidate, this is not a
fail-fast branch.  Prompt E's quartet-cancellation test is now the next active
orthogonal target.  See
`results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`.

## 11. Prompt E quantized-phase resolution

The zero-side carrier passes but the natural arithmetic realization fails.
For a real polynomial `P`, the whole-line winding of

```text
P(x-ia)/P(x+ia)
```

counts roots in `|Im z|<a`.  A simple functional-equation quartet therefore
changes the winding by four when `a` crosses its displacement.  This is a
genuine integer detector, but computing it for completed `xi` by a contour is
the argument-principle zero count.

The zero-independent finite-prime construction has no matching topology.  In
the relevant range `0<a<1/2`, every literal local shifted quotient and every
right-shift unit Euler phase is null-homotopic.  The literal infinite quotient
is unbounded even in Bohr `B^2`.  The normalized unit phases do converge in
`B^2`, but fail uniform convergence for `a<=1/2`; a `B^2` equivalence class has
no continuous-symbol winding or `K_1` and erases isolated/zero-density phase
defects.  Uniform Euler convergence returns only for `a>1/2`, i.e. in the
ordinary zero-free half-plane `Re(s)>1`.

The localized completed Weil operator supplies an unconditional finite Morse
index, but that index is exactly completed Weil-form inertia, not an
independently computed phase invariant.  Burnol's global scattering phase
also detects bad zeros only because its Blaschke factor is explicitly built
from them.

Accordingly Prompt E's natural Euler-loop architecture is parked.  A revival
requires a concrete completion-native equivariant or semifinite relative
index whose summability is proved without zeros or Weil positivity and whose
topology sees one remote quartet.  This is an admission criterion, not a
current construction.  Prompts A--E are now exhausted in their stated forms;
the next action should be a portfolio regroup, not another phase convention.
See `results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`.
