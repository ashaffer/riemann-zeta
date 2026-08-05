# Cross-disciplinary RH falsification tournament

Status: fail-fast audit completed 2026-08-04.  This report contains no RH
claim.  It distinguishes structural counterexamples from numerical scouts and
from conditional theorem schemas.

## 1. Executive verdict

The following proposed mechanisms are now pruned as independent routes:

1. ordinary, equivariant, mod-2/mod-4, or Krein collision indices for the
   de Bruijn--Newman flow;
2. finite S-matrix/EFT coefficient positivity;
3. finite Ihara zetas, standard expanders, compact quantum graphs, and
   prime-cycle graphs;
4. standard cryptographic indistinguishability or direct-product
   amplification of a Möbius bias;
5. plain categorical duality, positivity of a stable supertrace, a dagger
   without a C*-positive metric, and the abstract GNS construction;
6. energy-preserving primon supersymmetry and an unconstrained BRST
   differential;
7. factorwise passive Euler colligations and independent-prime Lee--Yang
   gases, already pruned in the earlier repository audits.

The broad interacting Lee--Yang proposal is not contradicted, but it is not
yet a research mechanism: at its present level it says only to approximate
the Riemann theta measure by objects already known to have the desired zero
property.  A necessary GHS inequality passes a lightweight numerical scan.

After the pruning, all serious survivors share one load-bearing target:

> Construct, independently of zeta's zeros and of the Weil form's sign, one
> completed global arithmetic object with an exact trace/determinant and a
> degree-isolated positive polarization.

Physics calls this a positive spectral representation, category theory calls
it a polarized dagger realization, and the Weil criterion calls it positivity
of the completed form.  These are not three independent bets.  Only an
independent geometric construction of the polarization would add information.

## 2. Heat-flow topology and Krein signature are killed

Let `H_t` satisfy

`partial_t H_t(z) = -partial_z^2 H_t(z)`

and suppose there is a generic real collision at `(t_0,x_0)`, so

`H=H_z=0`, `H_zz != 0`.

Writing `tau=t-t_0` and `w=z-x_0`, the heat equation gives the local expansion

`H_(t_0+tau)(x_0+w)`

` = (H_zz/2)(w^2-2 tau)+O(w^3,tau w,tau^2)`.

Hence the two local zeros are

`w_+(tau),w_-(tau) = +/-sqrt(2 tau)+O(tau)` for `tau>0`,

and

`w_+(tau),w_-(tau) = +/-i sqrt(-2 tau)+O(|tau|)` for `tau<0`.

This is exactly the generic real-to-complex bifurcation.  Reality and
conjugation preserve it; evenness merely duplicates it at `-x_0` to form the
usual quartet.

### 2.1 Exact symmetry-preserving countermodel

For `a>0`, put

`P_t(z)=exp(-t partial_z^2)(z^2-a^2)^2`

`      =(z^2-a^2)^2-12t z^2+4a^2 t+12t^2`.

It is an exact even real backward-heat solution.  For sufficiently small
`t>0` it has four real zeros; for sufficiently small `t<0` its zeros form an
off-axis quartet.  Therefore no homotopy invariant of real, even heat
solutions can forbid the transition.

Even positivity of the Fourier measure does not repair this.  For `c>0`,

`F_t(z)=exp(t) cos z+c exp(4t) cos(2z)`

is the heat deformation of the positive measure `delta_1+c delta_2`.  With
`r=c exp(3t)` and `y=cos z`, its zeros obey

`2r y^2+y-r=0`.

Both roots correspond to real `z` exactly when `r>=1`, so its Newman
threshold is

`t_*=-(1/3)log c`.

The threshold can be placed anywhere while preserving the heat equation,
evenness, conjugation symmetry, and a positive Fourier measure.

### 2.2 Why the candidate indices fail

- The argument-principle degree of the local quadratic remains two.
- The two real roots have opposite one-dimensional local degrees, so their
  signed total is zero before the collision and zero after it.
- Two roots disappear from the real axis, leaving mod-2 count unchanged.
- Parity duplicates the event, leaving a mod-4 count unchanged.
- The upper-half-plane count jumps only because the count is undefined at the
  double root; it is not a protected invariant through the collision.

Krein theory also permits exactly this event.  Define

`A_tau=[[0,1],[2tau,0]]`, `J=[[0,1],[1,0]]`.

Then `A_tau^* J=J A_tau`.  For `tau>0` its eigenvalues are
`+/-sqrt(2tau)`, and the corresponding `J`-norms have opposite signs.  They
collide at a neutral Jordan point and become a complex-conjugate pair for
`tau<0`.  Thus Krein signature predicts, rather than prevents, the dangerous
collision.

There is a second global obstruction: if nonreal zeros approaching the
Newman threshold do not have a bounded subsequence ending at a multiple real
zero, they can escape to infinite height.  A finite collision index therefore
also requires a no-escape/compactness theorem.

**Verdict:** kill the topological/Krein route.  Definite Krein type plus a
no-escape theorem would work, but definite type is already a positive metric
and therefore imports the Hilbert--Polya/Weil burden.

Primary anchors: Rodgers--Tao, arXiv:1801.05914; Dobner,
arXiv:2005.05142; Chernyavsky--Pelinovsky, arXiv:1706.05756.  This strengthens
the earlier `PARABOLIC-MASLOV-DEGREE-AUDIT.md` by closing equivariant and Krein
variants too.

## 3. Finite S-matrix positivity is killed

Remmen's exact zeta amplitude is

`A(s)=-d/ds log Xi(sqrt(s))`,

whose poles are the squared zero ordinates.  If all poles are physical real
masses, RH follows.  The proposed weaker scout was to derive the result from
forward-amplitude Taylor/EFT positivity.

The following countermodel kills that scout.  Fix `R>2` and
`theta notin pi Z`, and set

`A_(R,theta)(s)`

` =1/(1-s)+1/(R exp(i theta)-s)+1/(R exp(-i theta)-s)`.

Its crossing-symmetric forward amplitude is

`M(s)=A_(R,theta)(s)+A_(R,theta)(-s)`.

For `|s|<1`, the coefficient of `s^(2k)` is

`c_(2k)=2+4 R^(-(2k+1)) cos((2k+1)theta)`.

Consequently

`c_(2k)>=2-4/R>0`

for every `k>=0`, even though the amplitude has a nonreal conjugate pair of
poles.  Thus every scalar forward even-derivative positivity bound can hold
while the analogue of RH fails.

More generally, any finite collection of strict coefficient or Hankel
inequalities is stable under inserting a sufficiently remote complex pole
quartet: its first `N` Taylor coefficients are `O(R^-1),...,O(R^-N)`.  This is
the S-matrix form of the exceptional-zero obstruction.

A full Stieltjes/Herglotz spectral representation, with the required growth
and no hidden pole cancellation, would force all poles onto the physical
axis.  But constructing that representation for the exact zeta amplitude is
the global positive-state problem again.  The spectrum is already inserted
in the definition of the amplitude.

**Verdict:** prune finite dispersion/EFT positivity and low-energy bootstrap
as RH mechanisms.  Retain the amplitude only as a useful physical dictionary
for a future independently constructed theory.

Primary anchor: Remmen, arXiv:2108.07820.

## 4. The broad Lee--Yang proposal passes one scout but adds no mechanism yet

The Riemann theta representation already gives a positive even measure
`nu_R` such that

`M_R(h)=xi(1/2+h)/xi(1/2)=integral exp(h u) d nu_R(u)`.

Saying that `nu_R` is a Lee--Yang measure is equivalent to saying that its
Fourier transform has only real zeros, hence to RH.  Treating `nu_R` as one
generalized spin therefore changes the language but supplies no independent
ferromagnetic theorem.

The independent-prime gas has already failed: the arithmetic factor
`p^(-1/2)` moves the natural local zero/singularity away from the Lee--Yang
circle, and the gamma completion is not a harmless boundary field.  See
`ORTHOGONAL-SPRINT1-GATES.md`.

A standard pairwise ferromagnetic realization would impose the GHS necessary
condition

`d^3/dh^3 log M_R(h) <= 0` for `h>=0`.

The reproducible lightweight scan

`python3 src/xi_lee_yang_ghs_scan.py --linear-samples 61 --log-samples 61`

found no violation on `0.01<=h<=100`.  At 60 decimal digits its sampled range
was approximately

`-1.805e-3 <= d^3 log M_R/dh^3 <= -4.461e-6`.

This is a numerical falsifier only.  It is neither an interval proof nor
evidence for RH, and GHS is much weaker than Lee--Yang zero location.

**Verdict:** the naive model is killed; the unrestricted interacting model is
parked, not promoted.  It re-enters only after an explicit prime-and-gamma
Hamiltonian is defined independently.  Inverse-fitting unspecified couplings
to xi is nonfalsifiable and can hide the entire theorem.

**2026-08-04 final inverse-cone update:** Arb certifies the model-free
Newman--Stieltjes cumulant localizers through dimension 20, so that finite RH
shadow survives.  The stricter independent weighted-Rademacher/product-spin
cone fails rigorously at dimension 16.  The earlier proposal to combine
strongly-Rayleigh and ferromagnetic GKS inequalities was invalid because the
two classes have opposite dependence signs.  See
`results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`.

Primary anchors: Lee--Yang, Phys. Rev. 87 (1952); Dimitrov,
arXiv:1311.0596; Simon--Griffiths, Phys. Rev. Lett. 30 (1973).

## 5. Standard Ihara, expander, and quantum-graph routes are killed

For a finite `(q+1)`-regular graph, Bass's identity is

`Z_G(u)^(-1)=(1-u^2)^(r-1) det(I-Au+q u^2)`.

Its graph RH is exactly the Ramanujan adjacency bound.  This does not connect
to classical zeta without a separate exact determinant or trace identity.
The standard constructions fail several independent gates.

1. Under `u=q^(-s)`, a fixed-`q` graph zeta is imaginary-periodic.  A normal
   fixed-`q` limit remains periodic, unlike completed xi.  Shrinking periods
   require a singular, non-normal limiting procedure.
2. A finite metric graph has orbit lengths in the integer span of finitely
   many edge lengths, whereas the set `{log p}` is rationally independent.
3. Connecting one cycle for each prime creates mixed primitive words absent
   from Euler's product.  Keeping the cycles disjoint destroys the expander
   mechanism.
4. Circles of lengths `log p` have infinite total length and first nonzero
   Laplace eigenvalues tending to zero, so their union has no compact
   resolvent.
5. Compact quantum graphs obey a linear Weyl law, while the zero count has a
   `T log T` leading term.
6. A unitary orbit amplitude produces powers `a^m`; it cannot give the same
   negative coefficient `-p^(-m/2)` for every repetition.  A graded
   supertrace can supply a minus sign, but then positivity is missing.
7. The rational Ihara topological factor does not produce the gamma factor or
   the exact Riemann--von Mangoldt smooth term.

Weighted nuclear transfer operators evade some graph obstructions but are
normally nonselfadjoint; their resonances may be complex.  Requiring a
self-adjoint generator, exact completed trace formula, compact resolvent, and
positive polarization is the terminal Hilbert--Polya target, not an expander
lemma.

**Verdict:** kill every standard finite-graph/expander route.  The only
nonterminal compatibility milestone worth admitting is a single
zero-independent infinite graded system which simultaneously reproduces the
`T log T` density, every bounded-support prime-power trace coefficient, and a
cutoff-uniform compactness estimate.  Existing models reproduce subsets of
these requirements, not all three.

Primary anchors: Bass/Kotani--Sunada; Kuipers--Hummel--Richter,
arXiv:1307.6055; Endres--Steiner, arXiv:0912.3183.

## 6. Cryptographic amplification is killed

For smooth compactly supported `W`,

`S_(t,W)(X)=sum_n mu(n)n^(-it)W(n/X)`

has Mellin transform `W_hat(s)/zeta(s+it)`.  A zero
`rho=beta+i gamma` gives an `X^beta` obstruction after choosing `t=gamma`.
This is an exact phase detector, but the corresponding square-root bound is
the standard smoothed `1/zeta` form of RH.

At cryptographic input length `lambda=log_2 X`, the normalized bias is

`delta_X about X^(beta-1)=2^(-(1-beta)lambda)`.

For every fixed `beta<1`, this is negligible in `lambda`.  Polynomially many
hybrids cannot expose it; classical estimation needs order `delta_X^-2`
samples and quantum amplitude estimation order `delta_X^-1`, both exponential
in `lambda`.  XOR/direct-product lemmas normally shrink rather than amplify
correlation.  A false zero may also give only a nonuniform adversary with
`gamma` hard-coded.

**Verdict:** the Mellin-distinguisher language accurately explains why
averaging loses an exceptional zero, but standard cryptographic
pseudorandomness can coexist with false RH.  Any strong enough uniform
amplifier either reads exponentially many Möbius values or assumes the
square-root discrepancy to be proved.

## 7. Categorical no-go results

### 7.1 Duality does not imply purity

For arbitrary complex `a`, let

`Theta=diag(a,1-a)`, `B=[[0,1],[1,0]]`.

Then

`Theta^T B+B Theta=B`.

Thus a perfect pairing, semisimplicity, a Tate twist, and the functional
equation permit arbitrary off-line eigenvalues `a,1-a`.  Four dimensions add
conjugation symmetry without changing the conclusion.

If `B` is replaced by a positive Hermitian metric `G` and

`Theta^*G+G Theta=G`,

then `Theta-1/2` is skew-adjoint in that metric and the spectrum lies on the
critical line.  Fitting `G` after seeing `Theta` is therefore essentially
equivalent to the desired spectral conclusion.

### 7.2 Stable trace and dagger are not positive

Additivity of trace in a stable category gives

`tr(id_(Sigma X))=-tr(id_X)`.

No nonzero total stable Euler trace can consequently be nonnegative on every
identity.  Positivity must be imposed only after isolating the middle/physical
degree; `THH/TP` supertrace itself cannot be the Weil norm.

A dagger alone is also insufficient.  On `C^2` with
`J=diag(1,-1)` and `f^dagger=J f^* J`, taking `f=e_12` gives

`tr(f^dagger f)=-1`.

A genuine C*-positive realization or Hodge polarization is additional data,
not a consequence of involution.

### 7.3 Global GNS and unconstrained BRST are circular

For the completed Weil form, existence of a global factorization

`Q_W(f,g)=tau(pi(g)^*pi(f))`

with positive `tau` is equivalent to Weil positivity by GNS, hence equivalent
to RH.  Regularized traces and supertraces do not preserve positivity.

For a finite `Z/2` complex with superdimension `M(X)`, every differential
satisfies

`dim H >= |M(X)|`.

Conversely, an abstract differential can pair all possible even and odd basis
vectors and attain equality.  Mere existence of a BRST differential with
`O(X^(1/2+epsilon))` homology is therefore equivalent to the desired Mertens
bound.

The primon Hamiltonian has distinct energies `log n`.  Any odd supercharge
commuting with it must vanish on the one-dimensional parity-pure eigenspaces.
If a supercharge mixes different integers, it fails to commute with the sharp
cutoff `P_X`; the entire problem moves to the boundary commutator.  A
fixed-prime toggle leaves a positive-density strip `X/p<n<=X`, so its leakage
is linear rather than square-root.

This last obstruction is exact.  On squarefree basis states let `Q_p` toggle
the occupation of a fixed prime `p`; then `Q_p^2=1`, so `G_p=Q_p/2` satisfies

`Q_p G_p+G_p Q_p=1`.

The boundary pairs are precisely

`m <= X < p m`, with `m` squarefree and `p` not dividing `m`.

On each such two-state block, `[P_X,Q_p]G_p` has trace norm one.  Their number
is asymptotic to

`(6/pi^2) ((p-1)/(p+1)) X`.

Thus the most elementary natural BRST parametrix fails even the `o(X)` PNT
gate by a fixed positive proportion.  Its supertrace can be smaller only by
the original Möbius parity cancellation, which a trace-norm estimate discards.

**Verdict:** kill plain duality, total stable-trace positivity, abstract GNS,
and energy-preserving primon supersymmetry.  The only categorical survivor is
a degree-isolated polarization constructed before the spectrum is known.

Primary anchors: Hesselholt, arXiv:1602.01980; Deninger,
arXiv:math/0204110; Groth--Ponto--Shulman, arXiv:1212.3277; Connes--Consani,
arXiv:1211.4239.

## 8. Investigation of the survivors

### 8.1 The surviving categorical unit test

Before building an infinite zeta cohomology, a candidate geometry should pass
the following strictly weaker test using no nontrivial zero data:

1. combine the finite-place Frobenius/Verschiebung data for at least `p=2,3`
   with an independently defined archimedean object;
2. reproduce the two local Euler traces and the gamma determinant with exact
   normalizations;
3. isolate the pole/Tate hyperbolic pair rather than declaring its total
   supertrace positive;
4. on the remaining middle object, define the positive metric before
   computing any spectrum and prove the normalized adjoint relation;
5. prove coherence between the two finite places and infinity.

Failure would show that the proposed dagger cannot reconcile even two primes
with the real place.  Success would not prove RH, but would locate a genuine
source of positivity rather than a fitted Gram matrix.  The naive `THR(Z)`
candidate already fails the gamma-spectrum part; see
`CYCLOTOMIC-CONNECTIVITY-AUDIT.md`.

### 8.2 The surviving BRST unit test

For an independently constructed supercharge and parametrix

`QG+GQ=1-Pi`,

supercyclicity gives the exact cutoff identity

`M(X)=Str(P_X Pi)+Str([P_X,Q]G)`.

The first admissible target is only PNT scale:

`|Str(P_X Pi)|+||[P_X,Q]G||_1=o(X)`.

This is much weaker than RH and tests whether the construction creates any
real cross-integer cancellation.  The fixed-prime toggle fails with order
`X` boundary leakage.  A candidate that cannot beat this before using known
Möbius cancellation should be discarded.

### 8.3 The actual remaining long-horizon target

The repository already has exact prime cancellation `mu*log=Lambda`, the
archimedean incidence term, and isolation of the pole sector.  Their natural
combination is a signed mixed pairing/supertrace, not a norm.  Higher
differentials which leave the primary incidence map fixed cannot change its
degree-zero energy.

Therefore the genuinely surviving theorem is not another categorical trace:

> Construct a new completed primary arithmetic object, or a geometric Hodge
> star on the existing relative object, whose independently positive middle
> pairing reproduces the full Weil form and whose determinant/trace is xi.

This is recognizable as the missing characteristic-zero analogue of the
polarization/Hodge-index step in the function-field proof.  It survives
because no structural counterexample rules out such geometry.  It remains a
very hard construction, and merely postulating the positive pairing is RH.

## 9. Revised allocation

1. Close collision topology, finite S-matrix positivity, standard graphs,
   crypto amplification, and plain category theory as independent routes.
2. Do not spend more time on Lee--Yang models until a zero-independent
   Hamiltonian with fixed couplings is specified.
3. Use the BRST PNT-scale boundary test only as a cheap admission gate.
4. Concentrate serious conceptual work on the two-prime-plus-infinity
   degree-isolated dagger/polarization test.
5. Reject any construction whose positivity is obtained by GNS/Cholesky from
   the Weil form, whose determinant is defined from xi's zeros, or whose
   infinite limit lacks a no-escape theorem.

The tournament therefore makes a substantial negative Bayesian update for
the newly proposed physics/crypto shortcuts, but a useful positive update in
clarity: the remaining search space is no longer a collection of spectral
metaphors.  It is the much narrower search for an independently polarized,
completion-native arithmetic geometry.
