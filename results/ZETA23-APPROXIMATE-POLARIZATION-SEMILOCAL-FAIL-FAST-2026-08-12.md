# Approximate polarization: exact spectral floor and semilocal fail-fast

Status: exact finite-dimensional lower bounds, a zero-independent semilocal
metric experiment, and an inventory of the missing generator, 2026-08-12.
The exact results show what an approximate polarization would prove and why a
post-hoc Lyapunov metric is only a detector.  The semilocal quadrature is a
reproducible diagnostic, not interval-certified.  No zero-free strip or RH is
proved.

## 1. Verdict

The approximate-polarization target is mathematically valid but the smallest
actual all-place candidate is not yet present in the repository.

For a finite generator `A` and a positive Hermitian metric `G`, define

```text
epsilon_G(A)
 =norm(G^(-1/2)*(A^*G+GA-G)*G^(-1/2))_op.             (1.1)
```

The sharp spectral floor is

```text
epsilon_G(A)>=max_(lambda in spec(A)) abs(2 Re(lambda)-1).  (1.2)
```

For every diagonalizable `A`, equality is attained by a metric constructed
from its eigenvectors.  Thus optimizing `G` after seeing `A` recovers exactly
the horizontal spectral width; it does not prove a smaller width.

Three consequences settle the finite sanity checks.

1. For the off-line functional-equation block

   ```text
   A_alpha=diag(1/2+alpha,1/2-alpha), alpha in R,     (1.3)
   ```

   every `G>0` obeys `epsilon_G(A_alpha)>=2 abs(alpha)`, and every
   positive diagonal metric attains equality.
2. For a realization retaining the ungraded pole/Tate pair as invariant
   eigenvalues,

   ```text
   A_pole=diag(1,0),                                  (1.4)
   ```

   every positive metric has defect at least one.  This remains true after
   arbitrary positive metric coupling to other sectors, provided those
   invariant eigenvalues remain zero and one.  Such a realization must isolate
   the pole/Tate pair in a grading before placing a strict positive
   quasi-polarization on the middle sector.  The argument does not cover a
   different generator which accounts for pole terms without eigenvalues
   zero and one.
3. The repository's natural semilocal Euler metric is not monotone under the
   identity realization when a
   prime is adjoined.  Its exact Radon--Nikodym multiplier crosses one, and
   the existing moment compressions have both positive and negative update
   eigenvalues.  Hence prime-by-prime Loewner propagation cannot supply the
   desired metric.

There is a useful zero-independent positive control.  The semilocal cyclic
measure fixes a moment Gram matrix `G_p` from gamma and one Euler factor.
Compressing the scaling multiplier `1/2+i s` in that same metric gives a
Galerkin generator with `epsilon=0` algebraically.  This is not spectral
fitting, but it is also not a zeta generator: its Ritz spectrum lies on the
critical line by construction, it omits the pole sector, and no determinant
or resolvent identification with the nontrivial zeta zeros is proved.

Freezing the archimedean scaling generator in the fixed monomial coefficient
realization and changing only to the one-prime metric gives defects larger
than one already for `p=2` in dimension three and for `p=3` in dimension five.
These numerical failures rule out that identity-coefficient comparison.  The
exact semilocal Euler-multiplier isomorphism is a different comparison and
transports the multiplication generator with defect zero; it still has no
zeta-divisor spectral identification.

The honest state is therefore

```text
sharp approximate-polarization theorem                 PROVED;
post-hoc optimal metric                                 SPECTRAL DETECTOR;
ungraded invariant-(0,1) pole/Tate epsilon<1           IMPOSSIBLE;
natural semilocal metric monotonicity                   FALSE;
native semilocal scaling polarization                  EXACT CONTROL, NO ZETA SPECTRAL ID;
zero-independent coupled middle zeta generator         NOT CONSTRUCTED;
uniform independent epsilon<1 on that generator         OPEN.             (1.5)
```

## 2. Exact spectral lower bound

### Theorem 2.1 (every positive metric sees every horizontal eigenvalue)

Let `A` be a finite complex matrix and `G>0`.  Then

```text
epsilon_G(A)>=abs(2 Re(lambda)-1)                     (2.1)
```

for every eigenvalue `lambda` of `A`.

#### Proof

Let `Av=lambda v`, `v!=0`, and put

```text
D=A^*G+GA-G.                                          (2.2)
```

Then exactly

```text
v^*Dv=(2 Re(lambda)-1)*v^*Gv.                         (2.3)
```

The relative Rayleigh quotient of `D` at `v` therefore has absolute value
`abs(2 Re(lambda)-1)`.  Its absolute value is at most the operator norm in
(1.1), proving (2.1).  QED

Equivalently, a two-sided Loewner inequality

```text
-epsilon G<=A^*G+GA-G<=epsilon G                      (2.4)
```

confines the entire spectrum to

```text
abs(Re(lambda)-1/2)<=epsilon/2.                       (2.5)
```

This implication is independent of normality.

### Theorem 2.2 (a fitted metric attains the spectral floor)

Suppose `A` is diagonalizable:

```text
A=S Lambda S^(-1).                                    (2.6)
```

Set

```text
G_fit=(S^(-1))^* S^(-1)>0.                            (2.7)
```

Then

```text
epsilon_(G_fit)(A)
 =max_j abs(2 Re(lambda_j)-1).                         (2.8)
```

#### Proof

One has `S^*G_fit S=I`.  Congruencing the defect by `S` gives

```text
S^*(A^*G_fit+G_fit A-G_fit)S
 =Lambda^*+Lambda-I.                                  (2.9)
```

The generalized defect eigenvalues relative to `G_fit` are therefore the
real scalars `2 Re(lambda_j)-1`.  Equation (2.8) follows.  QED

This theorem is the precise circularity audit for a Lyapunov LMI.  Once the
eigenvectors have been used in (2.7), the optimized defect is exactly the
spectral conclusion one hoped to derive.  An approximate-polarization proof
must instead define `G` from arithmetic or geometry before inspecting the
zero spectrum and prove (2.4) independently.

There is also a conditioning debt.  In the Euclidean operator norm,

```text
cond_2(G_fit)=cond_2(S)^2.                              (2.10)
```

A badly conditioned eigenbasis produces a badly conditioned fitted metric.
Even a sequence of finite post-hoc metrics with small defects supplies no
uniform categorical polarization unless its conditioning and comparison maps
are controlled independently.

## 3. Exact off-line and pole/Tate gates

### 3.1 Off-line block

For (1.3), with `alpha` real, Theorem 2.1 gives

```text
epsilon_G(A_alpha)>=2 abs(alpha)                     (3.1)
```

for every `G>0`.  If `G=diag(g_1,g_2)` with `g_1,g_2>0`, then

```text
A_alpha^*G+G A_alpha-G
 =diag(2 alpha g_1,-2 alpha g_2),                     (3.2)
```

so the relative defect eigenvalues are exactly `2 alpha,-2 alpha`.  Hence

```text
inf_(G>0) epsilon_G(A_alpha)=2 abs(alpha).             (3.3)
```

No categorical metric can make a fixed off-line pair appear closer to the
line than it is.  A uniform defect `epsilon<1` is precisely a uniform margin

```text
Re(rho) <= 1/2+epsilon/2 <1.                          (3.4)
```

The strict inequality is the substantive uniform statement; for any one
known finite block inside the open critical strip a fitted defect below one
is automatic.

### 3.2 Pole/Tate block

The eigenvalues of (1.4) give

```text
epsilon_G(A_pole)>=1                                  (3.5)
```

for every positive `G`.  The identity metric attains equality.

More generally, suppose an all-place generator has invariant eigenvectors
with eigenvalues zero and one representing the pole/Tate pair.  Theorem 2.1
still gives (3.5), even if `G` has arbitrary positive off-diagonal couplings
between those eigenvectors and the middle sector.  Therefore no positive
metric on the **ungraded total object** can have defect strictly below one.

This does not kill a cohomological construction.  It specifies the required
shape for constructions which represent the pole/Tate terms by invariant
spectral parameters zero and one: that pair must contribute through grading,
supertrace, or an isolated degree, while (2.4) is imposed on a positive
middle object.  Treating the total supertrace as a positive trace would be the
already-audited trace/polarization error.  A different all-place generator
which reproduces pole terms without containing those two eigenvalues is not
excluded by this lemma.

## 4. What zero-independent generator data actually exist

The repository contains three different finite artifacts which must not be
conflated.

### 4.1 Connected all-place trace fixture

`src/two_prime_global_trace_gate.py` contains the exact connected Euler jet
for `{infinity,3,5}`, the first two rational gamma modes, and the alternating
functional-equation pairing.  The surrounding all-place audit records the
pole/prime normalization ledger.  The script proves exact trace identities
and absence of the mixed `15` coefficient.

It does **not** define one coupled generator `A_(infinity,3,5)`, a positive
metric on its middle sector, or a determinant whose zeros are the zeta zeros.
The invariant finite place-torus model instead forces a block-diagonal metric
and was already eliminated as a cross-place engine.

### 4.2 Semilocal cyclic measure

The one-prime semilocal model gives the zero-independent positive density

```text
d mu_p(s)
 =abs(Gamma(1/4+i s/2))^2
  /[1+p^(-1)-2 p^(-1/2) cos(s log p)] ds.             (4.1)
```

This genuinely couples the archimedean gamma weight and one Euler factor in
one Hilbert metric.  It also has a natural scaling multiplier.  Section 5
uses it for the smallest reconstructible positive control.

It does not include the pole/Tate pair in the positive middle metric, and
the finite moment compression is not identified with the completed zeta
divisor.

### 4.3 Abstract spectral controls

`A_alpha`, the on-line rotation block, and `A_pole` are exact sanity controls.
They are not derived prime+gamma+pole generators.  Inserting an off-line
`alpha` from a hypothetical zeta zero would destroy the required
zero-independence.

Consequently there is currently no matrix on which one can both:

1. verify the exact connected prime+gamma+pole trace fixture;
2. use a positive metric constructed independently of zeros; and
3. identify its spectrum, determinant, or resolvent with the nontrivial zeta
   divisor.

This absence is a construction gap, not a numerical failure and not a proof
that such a generator cannot exist.

## 5. Natural semilocal metric and scaling control

### 5.1 Arithmetic metric

Use the monomial basis

```text
b(s)=(1,s,...,s^(d-1)).                                (5.1)
```

Define the zero-independent moment matrices

```text
(G_p)_(ij)=integral s^(i+j) d mu_p(s),
(H_p)_(ij)=integral s^(i+j+1) d mu_p(s).              (5.2)
```

The positive density makes `G_p>0`.  Both gamma and Euler data are fixed
before any spectrum is computed.

Let

```text
M_p=G_p^(-1) H_p,
A_p=(1/2)I+i M_p.                                     (5.3)
```

Since `H_p=H_p^T`,

```text
M_p^T G_p=G_p M_p=H_p,                                (5.4)
```

and therefore

```text
A_p^*G_p+G_p A_p-G_p=0.                               (5.5)
```

This is an exact algebraic identity once the moments are fixed.  The tiny
nonzero values printed by the script are floating-point roundoff.

### 5.2 Why the exact control is not a zeta result

Equation (5.5) is a useful normalization check, not evidence for a strip.
The Galerkin multiplier was defined from the same metric so that (5.4) holds.
Its eigenvalues are

```text
1/2+i*t_j,                                             (5.6)
```

where the `t_j` are real Ritz nodes of multiplication by `s`.  They lie on
the critical line by construction.  No theorem identifies these nodes with
zeta zeros or the determinant of `A_p` with a completed zeta function.

This is categorically different from the fitted metric (2.7): here the
metric has independent arithmetic provenance, but the generator lacks the
required spectral provenance.  A successful construction needs both in the
same object.

### 5.3 Exact semilocal transport control

Let

```text
phi_p(s)=1-p^(-1/2-i s),
d mu_p=abs(phi_p)^(-2) d mu_infinity.                 (5.7)
```

Multiplication by `phi_p` defines an isometry

```text
U_p:L^2(mu_infinity)->L^2(mu_p),
(U_p f)(s)=phi_p(s)f(s),                              (5.8)
```

on its natural semilocal domain, because the two factors cancel pointwise in
the norm.  The scaling generator `A f(s)=(1/2+i s)f(s)` commutes with `U_p`.
Consequently the exact positive adjoint relation is transported with defect
zero.

This is the strongest independent quasi-polarization fixture actually
instantiated by the current semilocal data.  It couples the gamma density and
one Euler place and is not fitted to zeros.  It nevertheless fails three
admission gates for the proposed strip proof:

1. its multiplication spectrum lies on the line by definition;
2. the pole/Tate pair is not part of its positive middle spectrum; and
3. no conservative determinant or resolvent theorem identifies this scaling
   spectrum with the nontrivial zeta zeros.

The exact isomorphism also explains why nonmonotonicity of the metric update
does not contradict semilocal stability: the spaces are isomorphic, not
nested by an ordered identity inclusion.

### 5.4 Fixed-coefficient cross-stage diagnostic

Let `G_infinity,A_infinity` denote (5.2)--(5.3) without the Euler factor.
The finite test freezes one part of the data and changes the other:

```text
epsilon_(infinity->p)=epsilon_(G_p)(A_infinity),
epsilon_(p->infinity)=epsilon_(G_infinity)(A_p).       (5.9)
```

Representative output is:

| prime | full monomial dimension | `infinity -> p` | `p -> infinity` |
|---:|---:|---:|---:|
| 2 | 3 | `2.086626` | `1.279021` |
| 2 | 5 | `2.802382` | `3.842572` |
| 3 | 3 | `0.809236` | `0.683696` |
| 3 | 5 | `1.843137` | `2.186872` |
| 5 | 3 | `0.152102` | `0.165646` |
| 5 | 5 | `0.698524` | `0.625012` |
| 7 | 3 | `0.276834` | `0.309905` |
| 7 | 5 | `0.359701` | `0.336239` |

These use the identity map on the fixed monomial coefficient space, not the
Euler-multiplier isomorphism (5.8).  They are ordinary double-precision
quadratures, not interval enclosures.
They establish no theorem for `p=5,7` and no asymptotic trend.  They do
falsify the numerical hope that the most obvious frozen-generator update is
uniformly small in every first finite section: it already exceeds one for
small primes at modest dimension.

Rebuilding `A_p` together with `G_p`, or using the exact infinite-dimensional
transport (5.8), restores zero defect.  Passing to zeta still requires a
carrier-conservative determinant/spectral identification; (5.5) and (5.8)
supply neither.

## 6. The Euler metric is not a monotone update

Writing `q=p^(-1/2)`, the metric multiplier is

```text
w_p(theta)=1/(1+q^2-2q cos(theta)).                   (6.1)
```

Exactly,

```text
w_p(0)=1/(1-q)^2>1,
w_p(pi)=1/(1+q)^2<1.                                  (6.2)
```

Thus `G_p-G_infinity` has both signs on the full multiplication space by
localizing functions near the two phase arcs.  Lean checks (6.2) in
`RHBridge.SemilocalPrimeWeight.localWeight_crosses_one`.

The repository's even-monomial compression gives the following numerical
diagnostics:

| prime | even-monomial dimension | minimum update | maximum update |
|---:|---:|---:|---:|
| 2 | 2 | `-0.2046` | `6.9512` |
| 3 | 3 | `-0.3584` | `2.9977` |
| 5 | 3 | `-0.2099` | `1.3863` |
| 7 | 3 | `-0.05436` | `0.9268` |

The exact pointwise crossing, not the floating-point table, proves that no
global Loewner ordering exists.  Hence adjoining a prime cannot be justified
as adding a positive metric block.  Any successful naturality law must
include signed cross-place corrections and prove their completed sign.

## 7. Pole-inclusive reconstruction fails sharply

The smallest positive-control augmentation is

```text
A_all=A_p direct_sum diag(1,0),
G_all=G_p direct_sum I_2.                              (7.1)
```

Equations (5.5) and (3.5) give exactly

```text
epsilon_(G_all)(A_all)=1.                              (7.2)
```

More importantly, Theorem 2.1 proves

```text
inf_(G>0) epsilon_G(A_all)>=1                          (7.3)
```

even if `G` is allowed arbitrary off-diagonal coupling between the semilocal
and pole sectors.  The obstruction comes from the invariant eigenvalues zero
and one, not from the direct-sum choice in (7.1).

This is an exact fail-fast for any proposed all-place approximate
polarization which retains the pole/Tate spectral parameters as invariant
eigenvalues zero and one: before testing `epsilon<1`, that construction must
exhibit the middle-sector projection or grading which removes them from the
positive adjoint inequality.  A new coupled differential could realize such
an isolation, and a generator encoding the pole terms in another way lies
outside this no-go.  No prime+gamma+pole complex with the required trace and
spectral limit is presently constructed here.

## 8. Independent metric versus post-hoc detector

The provenance ledger is as important as the numerical defect.

| construction | metric provenance | generator provenance | conclusion |
|---|---|---|---|
| `G_fit` in (2.7) | zeta/eigenvector-dependent | arbitrary known `A` | exact detector of spectral width; circular as proof |
| `G_p,A_p` in (5.2)--(5.3) | gamma + Euler measure | scaling compression from the same measure | exact positive control; no zeta spectral identification |
| `G_p,A_infinity` in (5.9) | gamma + Euler measure | independently frozen archimedean scaling in fixed coefficients | honest finite mismatch diagnostic; fails `<1` for small primes/dimensions |
| `G_all,A_all` in (7.1) | semilocal metric + pole identity | direct-sum control | exact defect one; pole must be graded away |
| desired middle object | arithmetic/geometry before zeros | exact completed zeta trace and conservative spectral limit | not constructed |

Solving a semidefinite Lyapunov inequality for the desired `A` is useful as a
consistency test.  By Theorem 2.2 it cannot count as independent evidence for
a strip when its metric is selected from the same eigenvectors or optimized
against the target band.

## 9. Reproducibility

The lightweight diagnostic is

```text
python3 src/approximate_polarization_gate.py \
  --primes 2 3 5 7 --dimensions 2 3 4 5
```

It prints:

1. the exact analytic lower bounds and identity-metric values for
   `A_alpha` and the pole/Tate block;
2. native semilocal defects, which should be roundoff-size;
3. both frozen cross-stage defects in (5.9);
4. generalized eigenvalues of `G_p-G_infinity`;
5. the pole-augmented defect; and
6. the moment-metric condition number.

The floating regression tests for the exact algebraic formulas are

```text
python3 src/test_approximate_polarization_gate.py
```

They check the sharp off-line value, a non-diagonal metric lower bound, the
pole/Tate value one, the direct-sum fail-fast, a positive metric with explicit
cross-sector entries, and the native semilocal adjoint identity for a fixed
positive moment pair.  These NumPy tests are not exact-arithmetic
certificates.  The semilocal integrals use SciPy adaptive
quadrature truncated at `|s|=60`; the gamma tail is tiny, but no
outward-rounded interval claim is made.

## 10. Next theorem card

Further metric optimization should stop until a candidate supplies the
missing generator.  The minimal admissible next object must provide:

1. a degree-isolated positive middle space for `{infinity,p}` or
   `{infinity,p,q}`;
2. one zero-independent generator on that space, rather than a newly rebuilt
   generator at every metric stage;
3. the exact connected prime and gamma trace, with the pole/Tate pair accounted
   for in the other degrees;
4. a metric defined from arithmetic or geometry before the spectrum;
5. an exact or interval proof of `epsilon<1` for that fixed pair `(A,G)`; and
6. a conservative determinant/resolvent limit identifying its spectrum with
   the nontrivial zeta divisor.

If items 1--4 are constructed, (1.1) is the correct finite computation and an
interval `LDL^*` certificate would be worthwhile.  Before then, an optimized
small defect either tests a semilocal scaling control or reads back a chosen
finite spectrum.

## 11. Cross-links

- `ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`;
- `GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`;
- `SEMILOCAL-PRIME-UPDATE-AUDIT.md`;
- `CROSS-DISCIPLINARY-FALSIFICATION-2026-08.md`;
- `ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`;
- `RHBridge.FinitePolarizationNoGo`;
- `RHBridge.SemilocalPrimeWeight`.
