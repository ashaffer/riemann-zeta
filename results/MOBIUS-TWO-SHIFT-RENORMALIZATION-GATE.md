# Mobius-specific two-shift renormalization gate

Status: exact bilinear expansion, analytic exponent audit, cutoff/Riccati
renormalization no-go, and complete finite diagnostics; 2026-08-06.  The
local Mobius recursion is closed as a source of contraction.  The genuinely
global joint-dispersion theorem remains open.  This note does **not** prove a
new zero-free region or the Riemann Hypothesis.

## 1. Verdict

R73 left one possible mechanism: use the exact Mobius coefficient, rather
than a generic coefficient norm or Ward sign, to prove a cutoff-complete
two-shift estimate.  We tested its strongest concrete forms.

1. Expanding the grouped coefficient produces one exact four-variable
   Mobius--prime dispersion form with a rank-two center.  Cauchy--Schwarz,
   the multiplicative large sieve, zero density, almost-all short-interval
   cancellation, and separate dyadic rectangles give no fixed exponent
   saving.
2. Uniformly estimating all central plateau subrectangles independently is
   circular.  A saving `x^(-eta)` for a sufficiently rich sliding family
   forces a power-saving Mertens estimate and hence a fixed zero-free strip
   stronger than the strip sought from the full aggregate.
3. Fixed-step smoothing and the unconditional Vinogradov--Korobov region
   give a stronger subpower calibration for the cutoff-independent
   exact-head field.  With order `k`, its optimized energy saving is

```text
S(R,k)
 asymp R^(3/5) k^(2/5) [log(R/k)]^(-1/5).                (1.1)
```

   Taking `k=R^(1/2)/L(R)` with `L(R)->infinity` subpolynomial gives at best
   `S=R^(4/5-o(1))`.  Since `S/R` still tends to zero, this is not one fixed
   `eta`.  The follow-up `FULL-FIELD-VK-SUBPOWER-BOUND.md` proves the concrete
   bound `S=R^(4/5)(log R)^(-3/5)` for the full field and, by the uniform
   periodic-Euler lemma, for the frozen explicit-center field as well.
4. The exact Vaughan cutoff flow is a gauge transformation.  At every zeta
   zero its tail series has the same principal part for every finite cutoff;
   the zero carrier is an eigenvalue-one direction of every shell update.
5. The nonlinear Selberg--Volterra/Riccati recursion is critical, not
   contractive.  Its quadratic core has a double-pole-null direction at an
   arbitrary complex location; the remaining linear pole field leaves only
   a simple pole.  Cole--Hopf linearization returns to division by `zeta`.
6. Complete finite models reject cutoff-energy monotonicity, normalized
   monotonicity, coefficientwise contraction, and a channel-independent
   ordering.  With the exact unevaluated Type-I head the completed field is,
   correctly, cutoff-independent; with the explicit R71 center its Euler
   defect makes finite shell steps move in both directions.

Thus the **local** last method is killed.  What remains is not a recursion
but the global theorem itself:

```text
X_(I,U,V) <= x^(1-2eta+o(1)),       0<eta<1/2,            (1.2)
```

where `X_(I,U,V)` contains all unequal total products, all cofactors, and
both center terms after the equal-product diagonal is removed.  This theorem
is essentially equivalent to the fixed zero-free strip
`Re(rho)<=1-eta`.  No independent contraction was found.

## 2. Exact Mobius-specific dispersion form

Put

```text
beta_V(r)=sum_(b|r, b>V)Lambda(b).                        (2.1)
```

For a frozen cutoff block, the complete Vaughan tail is exactly

```text
T(R)=sum_(d>U,r>V)
 mu(d)beta_V(r)/(dr)^(1/2) V_k(R-log(dr)).                (2.2)
```

Here `V_k` is the normalized fixed-step coboundary window.  For an
admissible block weight `psi`, define

```text
K_I(u,v)=integral psi(R)V_k(R-u)V_k(R-v)dR,
L_I(u)=integral psi(R)V_k(R-u)z(R)dR.                     (2.3)
```

Then the completed energy is

```text
E_I=
 sum_(d_1,d_2>U; r_1,r_2>V)
 [mu(d_1)mu(d_2)beta_V(r_1)beta_V(r_2)
  /sqrt(d_1 d_2 r_1 r_2)]
 K_I(log(d_1 r_1),log(d_2 r_2))

 -2 sum_(d>U,r>V)
 [mu(d)beta_V(r)/sqrt(dr)]L_I(log(dr))

 +integral psi(R)abs(z(R))^2dR.                           (2.4)
```

Equal values of `d r` must be grouped before declaring the atomic diagonal.
Doing so returns the R73 coefficient

```text
a_(U,V)(n)=sum_(dr=n,d>U)mu(d)beta_V(r).                  (2.5)
```

Expanding `r=bm` gives the equivalent cofactor form

```text
T(R)=sum_(m>=1)1/sqrt(m)
 sum_(d>U,b>V) mu(d)Lambda(b)/sqrt(db)
 V_k(R-log(dbm)).                                        (2.6)
```

If the cutoff is frozen at the left endpoint `R_0` of a block of length `H`,
then on the faithful schedule

```text
m<=exp(2cR_0/k+H+O_h(k))=x^o(1),                         (2.7)
```

because `H=O(R_0/k)` and `k=o(R_0)`.  Thus Cauchy in `m` costs only
`x^o(1)`.  It does not solve the problem:
assigning the center or estimating the resulting cofactor blocks separately
deletes the cross-cofactor terms that restore the simple zeta pole.

## 3. Where present analytic tools stop

The current primary-source statements, versions, and exact R71 normalization
are consolidated in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).

On dyadic blocks define

```text
M_D(t)=sum_(d~D,d>U)mu(d)d^(-1/2-it),
B_Q(t)=sum_(r~Q,r>V)beta_V(r)r^(-1/2-it).                 (3.1)
```

The finite Mellin polynomial is the complete sum of
`M_D(t)B_Q(t)` over `D Q=x^(1+o(1))`.  The relevant `t` range is
`x^o(1)`, while `D,Q=x^(1/2+o(1))`.  The mean-value theorem therefore gives

```text
integral_(-T)^T abs(M_D(t))^2dt
 <<(D+T)sum_(d~D)1/d
 <<x^(1/2+o(1)),                                         (3.2)
```

and analogously for `B_Q`, up to logarithms.  Cauchy, a fourth moment, or an
ambient operator norm returns

```text
abs(T-z)<<x^(1/2+o(1)),
E_I<<x^(1+o(1)).                                         (3.3)
```

This is exactly `eta=0`.

Bombieri--Vinogradov does not directly enter: `dbm~x` is a moving product
condition, not an average of `Lambda` over residue classes.  Divisor
switching returns either the original centered product sum or weighted
correlations of the form

```text
sum_(d~D)mu(d)mu(d+h)W_(h,D)(d),                          (3.4)
```

and multiplicative-ratio analogues, uniformly over a large family of
shifts.  Available logarithmically averaged or almost-all cancellation does
not provide the required uniform fixed power.  The relevant comparison is
the short-interval work of
<https://doi.org/10.4007/annals.2016.183.3.6> and the higher-uniformity
theorem <https://doi.org/10.4007/annals.2023.197.2.3>.

The newest large-value technology substantially improves zero-density
estimates, but it still controls how many exceptions occur.  One off-line
zero already creates positive exponential R71 energy, so density cannot
replace exclusion.  See Guth--Maynard,
<https://doi.org/10.4007/annals.2026.203.2.6>.

### 3.1 Uniform separate-rectangle control is stronger than the target

On a central plateau rectangle with cofactor `m=1`, the kernel is rank one:

```text
T_rect=
 [sum_(d~D)mu(d)/sqrt(d)]
 [sum_(p~Q)log(p)/sqrt(p)],
D,Q=x^(1/2+o(1)).                                        (3.5)
```

The prime factor is `x^(1/4+o(1))`.  Hence an estimate uniform over all
sliding plateau subrectangles, or over a sufficiently rich smooth-weight
family,

```text
abs(T_rect)<<x^(1/2-eta+o(1))                            (3.6)
```

forces corresponding bounds for every partial weighted Mobius sum and hence

```text
sum_(d~D)mu(d)/sqrt(d)<<D^(1/2-2eta+o(1)),
M(D)<<D^(1-2eta+o(1)).                                   (3.7)
```

The last estimate follows by partial summation and continues `1/zeta(s)` to
`Re(s)>1-2eta`.  A bound for one isolated rectangle would not suffice for
this inference; the load-bearing point is the uniform independent family
needed by a blockwise triangle or Cauchy strategy.  Such a strategy assumes
a zero-free strip stronger than the `Re(s)>1-eta` conclusion sought from the
joint energy.  The full cross-block completion is not optional.

## 4. Fixed-step/Vinogradov--Korobov calibration

Let a zero have ordinate `gamma=exp(y)`.  From the exact fixed-step
multiplier,

```text
abs(G_(h,k)(rho-1/2))
 <<_h exp(O_h(k))exp(-(k+1)y).                            (4.1)
```

The Vinogradov--Korobov region gives

```text
1-Re(rho)
 >>y^(-2/3)(log y)^(-1/3).                               (4.2)
```

An explicit modern version is
<https://doi.org/10.1007/s40993-023-00498-y>.  Combining the horizontal
zero gap with (4.1), Riemann--von Mangoldt counting consumes the extra
`exp(-y)` factor and leaves `exp(-k y)` up to powers of `y`.  The resulting
formal optimization is

```text
R/[y^(2/3)(log y)^(1/3)]+k y.                            (4.3)
```

The optimizer and saving are

```text
y asymp (R/k)^(3/5)[log(R/k)]^(-1/5),
S(R,k) asymp
 R^(3/5)k^(2/5)[log(R/k)]^(-1/5).                        (4.4)
```

For the complete von Mangoldt coboundary this leads to the spectral
calibration

```text
E_I^full
 <<exp(R-c_h S(R,k)+o(R)).                               (4.5)
```

Here `R` denotes the right endpoint of the block.  The follow-up
[`FULL-FIELD-VK-SUBPOWER-BOUND.md`](FULL-FIELD-VK-SUBPOWER-BOUND.md) supplies
the shellwise zero summation, complete residue inventory, uniform window
normalization, and block bookkeeping, proving (4.5) for the full field.
Transferring it to the frozen-cutoff energy
`E_I^(U,V)` additionally uses

```text
sqrt(E_I^(U,V))
 <=sqrt(E_I^full)+norm(Delta epsilon_(U,V))_(L2(I)).       (4.6)
```

The inequality is exact.  Arbitrary-order periodic Euler summation now gives

```text
norm(Delta epsilon_(U,V))_(L2(I))
 <=exp[-(2c-1/2+o(1))R+O_h(k^2+klog k)]                 (4.6a)
```

for `U=V=exp[(1/2-c/k)R_0]`, `c>1/4`, provided
`hk^2<=(2c-o(1))R_0`.  This is the classical-synthesis lemma
`PROJ-EUL1/2` in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).
In the faithful range take

```text
k=R^(1/2)/L(R),
L(R)->infinity,       log L(R)=o(log R).                  (4.7)
```

The proved full-field and frozen-center calibrations then become

```text
E_I^full+E_I^(U,V)<<exp(R-R^(4/5-o(1))).                 (4.8)
```

This genuinely improves the subpower saving from a fixed smoothing order
for the exact-head field, but its
effective exponent

```text
eta(R) asymp S(R,k)/R
 ->0.                                                     (4.9)
```

It proves no fixed strip.  The calculation resolves the exponent-level R71
subpower calibration, including the frozen evaluated center:
spectral cooling can improve the subpower remainder, but it cannot turn a
zero-free region that narrows with height into a fixed gap.

## 5. Exact cutoff renormalization preserves the zero carrier

For `Re(s)>1`, put

```text
K(s)=-zeta'(s)/zeta(s),
A_Y(s)=[1-zeta(s)M_Y(s)][K(s)-L_Y(s)].                    (5.1)
```

For two finite cutoffs write `Delta M=M_(Y')-M_Y` and
`Delta L=L_(Y')-L_Y`.  Direct expansion gives the shell recursion

```text
A_(Y')=A_Y
 -(1-zeta M_Y)Delta L
 -zeta Delta M(K-L_Y)
 +zeta Delta M Delta L.                                  (5.2)
```

If `rho` is a zero of multiplicity `m_rho`, then

```text
principal_part_rho A_Y
 =-m_rho/(s-rho)                                         (5.3)
```

for **every** finite `Y`.  Every term in `A_(Y')-A_Y` is analytic at `rho`.
Thus the exceptional carrier has Laurent multiplier exactly one under every
finite cutoff update.

This gives a decisive audit for an exact shell transport, or for a
nonsingular cutoff RG which preserves the completed common mode:

1. multiplier one means no contraction of the mode that must be excluded;
2. a multiplier below one obtained only after `Y->infinity` requires the
   nonuniform normalization `M_Y~1/zeta`;
3. a recursive argument that does not otherwise exclude the common
   principal part cannot prove a fixed exponent saving.

On each fixed total-product fiber, a positive reversible factor-assignment
chain has the same obstruction.  It can contract parity and assignment
differences, but it preserves the constant fiber vector.  After assignment
summation that vector is precisely the grouped coefficient `a_Y(n)`.
Mixing different products with a uniform completed gap is (1.2), not a local
lemma.

There is also a scale mismatch.  The decisive semiprime fibers have depth
two, while the cofactor has logarithmic size `O(R/k)`.  Even at maximal
cofactor depth, a fixed gain per cofactor prime accumulates only
`exp(-O(R/k))=exp(-o(R))` on the faithful schedule.  Shallow cofactors gain
less.  A fixed saving must come from global mixing among total products.

## 6. The Riccati quadratic core has no double-pole coercivity

There is a stronger nonlinear identity.  In logarithmic measure notation let

```text
lambda=sum_n Lambda(n) delta_(log n),
p(u)du=exp(u)du,
eta=lambda-p,
beta=u lambda+lambda*lambda-2u p.                        (6.1)
```

Since `p*p=u p`, the Selberg identity gives the centered Volterra law

```text
beta=u eta+2p*eta+eta*eta.                               (6.2)
```

Taking the Mellin/Laplace transform in the classical unshifted `s` variable,
put

```text
Q(s)=-zeta'(s)/zeta(s)-1/(s-1).                          (6.3)
```

Equation (6.2) is the exact Riccati identity

```text
-Q'(s)+2Q(s)/(s-1)+Q(s)^2
 =zeta''(s)/zeta(s)-2/(s-1)^2.                           (6.4)
```

Its homogeneous quadratic core is critical.  For every complex `a`,

```text
q_a(s)=-1/(s-a),
-q_a'(s)+q_a(s)^2=0.                                     (6.5)
```

Equivalently in scale coordinates, `eta_a(u)=-exp(a u)` satisfies

```text
u eta_a+eta_a*eta_a=0.                                   (6.6)
```

Equations (6.5)--(6.6) solve only the quadratic core, not the full centered
homogeneous operator.  Indeed

```text
-q_a'+2q_a/(s-1)+q_a^2
 =-2/[(s-1)(s-a)].                                       (6.7)
```

Thus an off-axis pole is a double-pole-null direction, while the linear pole
field leaves a simple pole.  The double poles cancel rather than create a
coercive square.  Cole--Hopf linearization recovers the underlying zeta
equation; selecting its zero-free solution requires the missing inverse-zeta
control.

The model convolution is exponent-marginal as well.  For a density `f`, or
for a signed measure dominated in weighted total variation by
`exp(alpha u)du`,

```text
abs(f*f(R))<=R exp(alpha R).                              (6.8)
```

This model inequality preserves `alpha`; it does not improve it.  The actual
arithmetic `eta` is an atomic signed measure plus a density, so applying
(6.8) requires the stated variation control after smoothing.  In
particular, the classical Selberg forcing supplies no automatic induction
from the critical normalized scale `exp(R/2)` to
`exp((1/2-eta)R)`.

## 7. Complete finite cutoff gate

The diagnostic
[`src/mobius_cutoff_recursion_probe.py`](../src/mobius_cutoff_recursion_probe.py)
verifies the exact simultaneous shell update.  For `q=Y+1`,

```text
a_q-a_Y
 =-mu(q)delta_q*Lambda_(>Y)*1
  -Lambda(q)mu_(>Y)*delta_q*1
  +mu(q)Lambda(q)delta_(q^2)*1.                           (7.1)
```

The last term restores the row/column intersection.

The sharp complete example is

```text
X=25, h=0.04, j=m=1, Y:2->3.                             (7.2)
```

The active products stay `(24,25)`, while

```text
a_2(24)=-log 2,       a_3(24)=+log 2,
a_2(25)=a_3(25).                                         (7.3)
```

Therefore the raw atomic diagonal is identical, but the explicit-center
energy changes as follows:

```text
D_raw       0.0408071746286 -> 0.0408071746286,
E_raw       0.00825209992517 -> 0.0223489892653,
E ratio     2.70827904,
covariance ratio 7.06683075,
zero-mode ratio  0.802869125.                             (7.4)
```

The exact-head covariance ratio is exactly one, as Vaughan cutoff invariance
requires.  The opposite motions of covariance and zero mode rule out a
channel-independent ordering for the explicit-center recursion.  At the
coefficient level, `a_2(30)=0` but `a_3(30)=log 5`, so absolute-coefficient
contraction also fails.

Larger and higher-order examples amplify instead of repair the issue:

```text
X=101, Y:6->7, h=0.04: normalized energy ratio >28,
X=50,  Y:4->5, h=0.04, j=m=2: ratio >14.                 (7.5)
```

At fixed cutoff, adjacent scale steps occur in both directions as well.
These are D-rated finite diagnostics, not asymptotic counterexamples.  Their
role is to reject local monotonicity and Pythagorean shell arguments.  They
do not refute (1.2) or a recursion whose additive source is already as large
as the new completed shell energy.

Focused tests are in
[`src/test_mobius_cutoff_recursion_probe.py`](../src/test_mobius_cutoff_recursion_probe.py).

## 8. Final disposition

The experiment distinguishes the statement from the method.

* **Closed:** local cutoff martingales, cutoff/scale monotonicity, a Riccati
  double-pole coercivity argument, factor-fiber spectral gaps, uniform
  independent rectangle estimates that discard their cross terms, and any
  exact finite cutoff transport claimed to damp zeta residues.
* **Proved full-field and frozen-center calibration:** (4.5)--(4.8),
  concretely
  `exp[R-c_hR^(4/5)(log R)^(-3/5)]`, with effective `eta(R)->0`.
  The varying-test converse remains open.
* **Still open:** the one global joint-dispersion estimate (1.2), retaining
  all total products, cofactors, and center terms simultaneously.

Calling (1.2) “Mobius-specific cancellation” does not make it an independent
engine: after the gates above, it is the fixed-zero-free-strip problem in
arithmetic coordinates.  A future **recursive** proposal must act
nontrivially on the common Laurent mode without inserting `1/zeta` or zero
locations.  A direct arithmetic proof could instead show that this common
carrier is absent, but then it must establish the global joint estimate
(1.2) rather than infer it from local transport.

The follow-up
[`HYPOCOERCIVE-THOMSON-TRANSPORT-GATE.md`](HYPOCOERCIVE-THOMSON-TRANSPORT-GATE.md)
tests two deliberately nonlocal-looking escapes.  Exact cutoff
hypocoercivity retains the same common carrier in its bracket kernel, while
the natural positive signed-flow network forgets Mobius orientations and
collapses to independent total-product fibers.  Neither changes the final
disposition above.
