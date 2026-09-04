# Ten orthogonal long-tail hypotheses

**Date:** 2026-08-13

**Truth boundary:** none of the hypotheses below has proved a uniform
zero-free strip.  They are deliberately speculative, but each is conditioned
on the project's audited conservation laws and has a precise kill or promotion
test.  The quoted probabilities are subjective research priors, not
mathematical confidence intervals.

## 1. Sampling rule

The portfolio excludes ideas already known to fail for one of the following
reasons:

```text
wrong carrier normalization;
separate states for carrier and sign;
loss of the principal Mertens mode;
tensor length beyond the conductor;
finite-head nonidentifiability;
an estimate which tolerates one exceptional zero;
or a common determinant/main term estimated before cancellation.
```

The ten hypotheses use different mathematical mechanisms.  Some are
**promotion hypotheses**, which could imply a strip.  Others are **kill
hypotheses**, whose proof would decisively remove a surviving route and
concentrate effort elsewhere.

## H1. Actual prime logs obey a power-law antenna theorem

**Mechanism:** harmonic analysis of prime exponential sums.

Let `E_Y` be the actual-node Wiener/Schur extremal in the audited aperture.
The precise kill hypothesis is that there are coefficients on the actual
prime-power nodes and a constant `c>0.0180303234` such that

```text
sup_(0<=xi<=Y^(50/33+o(1)))
 |b(xi)-sum_n lambda_n cos(xi*log(n/Y))|
   <=Y^(-c+o(1)).                                       (H1)
```

A dual antenna of this form proves `E_Y<=Y^(-c+o(1))` and would kill the
current positive-prime-null route.  It does **not** prove an asymptotic
equality for `E_Y`; the four computed scales are not evidence for a stable
power exponent.

The low/mid portion is no longer hypothetical.  Actual-node Voronoi or
piecewise-linear quadrature plus the unconditional prime-gap mesh
`h_Y<<Y^(-19/40+o(1))` gives a fixed-power certificate through
`|xi|<=Y^(19/40-epsilon)`.  The exact survivor is the high tail from that
scale to `Y^(50/33)`.  The tempting `Y^(-1/4)` second-derivative heuristic in
this tail applies to smooth all-integer coefficients, not to prime/gap
weights.  With `Lambda/log` weights the audited pointwise theorem is still
only logarithmic.

**Prior:** 55% that some full-aperture power upper bound beyond the threshold
is true as a random-frame phenomenon; below 5% that present prime
exponential-sum methods prove it.  These are structural priors, not an
extrapolation of the four floating values.

## H2. The modular theta kernel has third-tail rigidity

**Mechanism:** modular Poisson summation and variation diminution.

For the actual theta kernel, hypothesize that every

```text
B_P(w)=1/4 integral (|d|-P)_+^2
       Phi((w+d)/2)Phi((w-d)/2) dd                       (H2)
```

is positive definite.

This hypothesis survived the actual-theta numerical scan through height
`1000`, while an exact positive-definite Laguerre--Polya atomic model violates
it.  Therefore any proof must use the complete modular orbit; generic
real-rootedness is unavailable.

An attempted smaller statement has now been eliminated.  Arb certifies at
`T=152.7` that `S_2(P,T)` has signs `+,-,+` at three ordered values of `P`.
Thus the one-crossing/Pontryagin-index-one shortcut is **false for the actual
theta kernel**.  This does not decide `S_3>=0`, because `S_3` is the integrated
tail of `S_2`, not its pointwise sign.

**Prior after this falsification:** 8% that full `B_P` positivity is true;
below 1% that it can presently be completed to the required endpoint theorem.

## H3. An outer zero forces reverse Husimi localization

**Mechanism:** microlocal/phase-space uncertainty with a zero constraint.

Husimi positivity proves the forward smoothed comparison

```text
exp(s^2*A^2) G_s*U_A >= exp(s^2*B^2) G_s*U_B.
```

Hypothesize that if the outer line contains a zero at height `T_0`, the exact
theta coefficients, functional equation, and local Taylor jet force, for
some scale `s`,

```text
(G_s*U_A)(T_0)
  < exp(-4*s^2*alpha*eta) (G_s*U_B)(T_0).                (H3)
```

The two inequalities would contradict each other.  Separate maximum-modulus
bounds cannot prove (H3); it must be a relative outer/inner-line estimate on
the same Gaussian window.

The local candidate equation is now known not to supply it.  For the exact
model `F(z)=C(z-z_0)^m`, Gaussian moments give

```text
M_s(A,T_0)/M_s(B,T_0)>=exp(-8*m*eta^2*s^2).             (H3a)
```

Thus the reverse target is impossible whenever `2*m*eta<=alpha`.  The strict
survivor must use global variation of the nonzero theta/zeta cofactor; in a
bounded-cofactor model with ratio `K`, it must pay

```text
log K>2*eta*(alpha-2*m*eta)*s^2.                        (H3b)
```

**Prior after the local-zero no-go:** 2% true, below 0.5% accessible.

## H4. The completed AFE Loewner matrix has an integrable signed factorization

**Mechanism:** displacement-rank operators and integrable kernels.

The centered finite matrix satisfies

```text
H_E=2*L_A-2*(log X)*diag(Re E),
rank([D,H_E])<=2.
```

Hypothesize that after adjoining an exact approximate-functional-equation
tail, the full candidate-conditioned matrix has a factorization

```text
H_full=V^* J V + R_gamma,                                (H4)
```

where the negative index of `J` records off-strip residues and the explicit
candidate state isolates one negative direction with a carrier-sized gap.
Precisely, for a normalized candidate state `x_gamma`, the factorization
must exhibit numbers `g_gamma>0` and `epsilon>0`, uniform in the target
regime, such that

```text
x_gamma^* V^* J V x_gamma <=-g_gamma,
|x_gamma^* R_gamma x_gamma| <=(1-epsilon)g_gamma,         (H4a)
```

with `g_gamma` carrier-sized.  This would turn the signless low-rank
commutator into a nonlocal certificate.  A decomposition with unrestricted
`R_gamma` is tautological and has no sign content.

The kill test is remote-factor invariance: if the proposed factors use only a
finite coefficient head, the construction is invalid.  Every valid version
must display the AFE tail and its norm before claiming a sign.

**Prior:** 4% that a useful factorization exists, below 1% that its remainder
can be controlled with current technology.

## H5. An adelic capacity inequality controls directional leverage

**Mechanism:** product formula and non-Archimedean potential theory.

The DPP determinant itself cancels.  For a legal high-band design `rho`, let
`G_rho` be its actual-node Gramian and `q` the low-carrier phase vector.  The
exact directional design cost is

```text
R_H(q)^2=inf_(rho in Prob(H)) q^*G_rho^dagger q.          (H5a)
```

Here the infimum is restricted to designs with `q` in `range(G_rho)`;
equivalently the displayed cost is `+infinity` when that range condition
fails.  This condition is part of the exact pseudoinverse identity.

Hypothesize that an explicit legal `rho_Y` admits a genuinely directional
adelic factorization whose finite-place factors have an independently proved
`Y^(-o(1))` lower bound and which yields

```text
q^*G_(rho_Y)^dagger q <=Y^(o(1)),                        (H5)
```

with `q` in `range(G_(rho_Y))` and actual-node approximation error below the
carrier margin.  This would promote the prime atomic route even though
uniform/Lebesgue designs have leverage of order `M`.

This is not the already-failed common-determinant strategy: the local factors
must be directional resultants involving the carrier row.  A product upper
bound without a lower bound for the finite-place product is vacuous, and a
rational-node toy has no automatic transfer to the phases `p^(i*xi)`.

**Prior:** 3% that an exact identity exists, 0.5% that it has the favorable
direction.  The first test is a finite rational-node model in which every
local capacity and the Schur complement can be computed exactly.

## H6. Riemann zeta admits a genuinely non-lattice transfer operator

**Mechanism:** thermodynamic formalism and Dolgopyat cancellation.

Hypothesize an exact factorization in a fixed right half-strip

```text
xi(s)=E(s) det(I-L_s),                                  (H6)
```

on an anisotropic Banach space, with an analytic Fredholm determinant and
with `E` holomorphic and zero-free in the target half-strip, where the roof
lengths encode the coupled prime-power completion and satisfy a uniform
non-integrability estimate.  A Dolgopyat spectral gap for `L_s` would then
give a fixed strip.  Without the zero-free condition on `E`, the displayed
factorization and a gap for `L_s` do not exclude zeros of `xi`.

The kill test is severe: an operator built from independent Euler factors has
an almost-lattice principal channel and merely rewrites the Mertens mode.
The representation must couple primes before taking the determinant and must
recover the functional equation, not only the Euler product for `sigma>1`.

**Prior:** 2% that such an exact useful representation exists, below 0.5%
that the required non-integrability is provable.

## H7. One zero triggers deterministic vertical replication

**Mechanism:** arithmetic renormalization dynamics.

Zero-density estimates fail because they permit one offender.  Hypothesize a
candidate-relative renormalization theorem: a zero with
`beta>1-delta` forces at least `T^c` distinct companion zeros in a controlled
higher-height interval, with `c` exceeding the zero-density exponent for
that same box.  A version stated first in terms of near-zeros is admissible
only if it includes a multiplicity-aware, bounded-overlap Rouche or
argument-principle conversion to that many actual zeros in the same box;
near-zero values alone are not counted by a zero-density theorem.

Unlike ordinary universality, the replicas must preserve winding and the
missing constant jet.  The new ingredient would be a multiplicative scale
cocycle tying the principal value `zeta(rho+i*tau)` to derivative recurrence,
rather than discarding it.

**Prior:** 2% true in a quantitatively useful form, below 1% accessible.  A
two-scale exact recurrence or a counterexample in a symmetric Euler-product
model is the immediate test.

## H8. Off-strip zeros are tropically visible in tau--Li coefficients

**Mechanism:** asymptotic coefficient geometry/Newton polygons.

For `tau<2`, an off-strip zero is exactly an exterior pole under
`q_tau(rho)=rho/(rho-tau)`.  Hypothesize that actual prime-Laguerre
coefficients satisfy a cancellation restriction strong enough that an
exterior pole forces negativity on every sufficiently large degree in a
syndetic set `S`, while the completed prime formula forces, for every cutoff
`M`, nonnegativity at some degree `m in S` with `m>=M`.  The two assertions
refer to the same `S`; with that quantifier made explicit they exclude the
pole without proving every coefficient positive by a termwise bound.

The statement must exploit arithmetic relations between degrees; absolute
Laguerre majorants diverge and endpoint positivity at `tau=2` does not
transport below `2`.

**Prior:** 3% that a syndetic domination theorem exists, below 1% that a
matching arithmetic sign law exists.

## H9. A quantitative Speiser tree amplifies horizontal depth

**Mechanism:** complex critical-point geometry.

Hypothesize that a zeta zero at horizontal depth `epsilon` off the critical
line creates, through repeated critical points of `xi,xi',xi'',...`, a
branching tree with one of the following two quantitative terminal outcomes:

```text
(i) more distinct derivative zeros in one controlled box than an explicit
    proved upper bound permits; or
(ii) after an explicitly bounded number of generations, a descendant in a
     proved zero-free region for the corresponding derivative.            (H9)
```

Merely producing one descendant of depth `c*epsilon` is not a terminal
contradiction unless an iterated estimate proves (ii).  Gauss--Lucas alone
is inadequate: the exact symmetric-quartet polynomial has all critical
points on the central line.  The hypothesis therefore needs the Euler/gamma
logarithmic derivative at every generation.

**Prior:** 2% true, below 0.5% accessible.  The first kill test is a completed
Euler-product model with one inserted quartet and controlled logarithmic
derivatives.

## H10. The full AFE has nonlocal circular-domain stability

**Mechanism:** stable polynomials and holographic transformations.

The natural local version is now ruled out.  In the exact two-prime AFE
cylinder

```text
F=(1+x_2)(1+x_3)+g(1+y_2)(1+y_3)+r,
```

the Rayleigh minor is

```text
Delta_(x_2,x_3)=-g(1+y_2)(1+y_3)-r.                    (H10a)
```

It takes both signs.  The same obstruction survives general nonzero AFE
weights, so no fixed coordinatewise real `GL_2`/Mobius holographic transform
can make the additive primal/dual lift stable on a product of half-planes.

The strict surviving hypothesis is different and falsifiable.  For each
polarized full AFE degree, there is an explicit invertible cross-channel map
`T` mixing primal, dual, and remainder variables, and an explicit proper
non-product cone `C`, such that

```text
P_AFE(T*z)!=0 whenever Im(z) is in interior(C),          (H10)
```

uniformly in the degree, while the physical diagonal for `sigma>.99` maps
inside that tube.  A uniform diagonal-preserving `C`-stability theorem would
exclude the target zeros; the ordinary product-domain Grace--Walsh theorem is
no longer enough.

Prime-separable Fejer/SOS positivity is already false, so the interactions
must couple the common height across primes.  Finite-head remote-prime
nonidentifiability forces an exact tail variable; omitting it invalidates the
model.  Merely renaming a nonlocal transform does not count: its domain and
physical diagonal must be written explicitly.

**Prior after the exact two-prime kill:** 0.3% that such nonlocal stability
holds, below 0.1% accessible.

## 2. Portfolio disposition

```text
ACTIVE NOW:
  H1  actual-node hybrid dual / square-root kill theorem;
  H2  complete modular Poisson attack (one-crossing shortcut is dead).

NEXT EXACT KILL TESTS:
  H4  remote-factor-complete Loewner factorization;
  H5  finite adelic directional-capacity model.

WATCH ONLY UNTIL A NEW LEMMA APPEARS:
  H3 global-cofactor reverse localization;
  H6, H7, H8, H9;
  H10 explicit non-product domain or cross-channel transform (the local
      product-half-plane version is closed).
```

The portfolio is intentionally asymmetric.  H1 is likely to close a route;
H2 and H3 are low-probability proof routes; H4--H10 are long-tail bets whose
first task is falsification.  This prevents speculative breadth from erasing
the project's central lesson: only a theorem changing the completed
debt/carrier ratio on one state moves the zero-free boundary.

## 3. Hostile survival audit against the existing evidence

This section is part of the hypotheses, not a disclaimer.  A path is retained
only in the strict form that has not already been closed.

| Hypothesis | Evidence which closes the naive form | Exact surviving form |
|---|---|---|
| H1 | generic Gram/Riesz transfers stop at square-root scale; low-band prime-mesh quadrature does not cross its Nyquist scale; KMT gives only logarithmic high-band control | a uniform **actual-prime, carrier-aware** dual estimate over the full legal aperture |
| H2 | `S_2>=0`, fractional tails, generic LP/HB positivity, and now the one-crossing law are false | positive definiteness of the complete actual-theta `B_P`, or a different modular identity controlling its integrated signed tail |
| H3 | Wigner positivity, positive Husimi banks, correlated Gaussian squeezing, signed anti-Wick recovery, and forcing from the local zero/multiplicity jet are closed | global cofactor-specific **relative** localization beating (H3b) on the same Gaussian tube |
| H4 | displacement rank two, finite Loewner data, separate determinants, and finite-head SOS have explicit countermodels | a full AFE-completed relative factorization whose candidate remainder is uniformly smaller than its signed carrier gap as in (H4a) |
| H5 | linear adelic/character ancillas compress back to the scalar extremal; common determinant products cancel | a range-feasible, directional, multiplicatively coupled local-capacity law for the carrier Schur complement itself |
| H6 | compact observability, ordinary FUP, and generic cusp control miss the constant parabolic channel | a zero-free-prefactor arithmetic transfer gap acting directly on that principal channel and recovering the completed scattering scalar |
| H7 | ordinary universality loses winding; derivative recurrence loses its constant polynomial jet | a quantitative recurrence which transports winding and the missing principal value and yields enough actual zeros in the density box |
| H8 | endpoint transport from `tau=2`, termwise Laguerre bounds, and degree-uniform absolute majorants fail | an actual-coefficient relation **between degrees** which contradicts exterior-pole domination on the same syndetic set |
| H9 | Gauss--Lucas, quartet symmetry, Speiser's global equivalence, and derivative-zero density all tolerate one offender | a depth-sensitive, height-local per-zero map or branching theorem with one of the terminal contradictions in (H9) |
| H10 | prime-separable Fejer/SOS, every finite-head candidate label, and every fixed coordinatewise real product-half-plane holographic transform are closed | explicit uniform cross-channel `T` and non-product cone `C` satisfying the tube-stability statement (H10) |

Consequently none of the ten retained strict statements is contradicted by a
proved result in the project.  Several are deliberately much narrower than
their familiar names.  In particular, “Loewner,” “adelic,” “transfer
operator,” “universality,” and “Lee--Yang” without the surviving qualifier in
the last column are already closed and must not be restarted.
