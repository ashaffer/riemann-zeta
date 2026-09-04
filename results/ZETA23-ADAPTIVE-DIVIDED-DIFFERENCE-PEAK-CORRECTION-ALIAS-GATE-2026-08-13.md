# Adaptive divided-difference peak correction: exact alias gate

**Date:** 2026-08-13

**Verdict:** high-order moment annihilation gives genuine low-band leverage,
and its coefficient size is irrelevant after normalization.  For `K+1`
nodes the moment-annihilating direction is unique, however, and its response
at the high center is a divided difference.  The exact normalized
corrector is

```text
C_(U,t0)(s)
 =(s/t0)^K Phi_U(s)/Phi_U(t0),                         (0.1)
```

where `Phi_U` is the characteristic function of a compact B-spline
probability law determined by the nodes.  The advertised factorial cancels
between numerator and denominator.  Thus the construction needs two facts
not supplied by moment cancellation:

```text
Phi_U(t0) is not too small,                            (0.2)

sup_(t in H)|D_U(t)/D_U(t0)| is controlled.           (0.3)
```

On a uniform mesh of step `h`,

```text
D_U(t)=exp(i t u_0)[exp(i t h)-1]^K/(K! h^K).         (0.4)
```

Every alias `t=2 pi m/h` makes (0.4) exactly zero, so no normalized
moment-annihilating correction exists.  Away from an alias the low leakage
is excellent,

```text
asyp [T h/|exp(i t0 h)-1|]^K,                         (0.5)
```

but a remote comb lobe is amplified by

```text
[2/|exp(i t0 h)-1|]^K.                                (0.6)
```

Hence the same filter which suppresses the low band can create much larger
far-tail peaks.

This is not only an exact-lattice pathology.  An arbitrarily small generic
perturbation of the uniform mesh removes every common exact alias and may
be chosen rationally independent, while making all finitely many adaptive
block responses at the old alias arbitrarily small.  Its maximal gap and
sum of squared gaps remain stronger than the available prime-gap inputs.
Because (0.1) is scale invariant, allowing unbounded coefficients does not
repair this near-alias obstruction.

High order can tolerate a very small *quantified* nonalias factor; a
polynomial lower bound is not logically necessary.  It cannot work from
qualitative nonvanishing alone, and it supplies no far-sidelobe control.
For actual prime logs, proving the needed adaptive nonalias and sidelobe
bounds is another form of the unresolved high-tail Chebyshev/quotient
theorem.

No zero-free strip is claimed.

---

## 1. The unique moment-annihilating direction

Let

```text
U={u_0<...<u_K}                                       (1.1)
```

be `K+1` adjacent prime-log nodes.  Define the barycentric weights

```text
omega_j=1/product_(ell!=j)(u_j-u_ell).                (1.2)
```

### Lemma 1.1 (moment identities)

One has

```text
sum_(j=0)^K omega_j u_j^m=0        (0<=m<K),
sum_(j=0)^K omega_j u_j^K=1.                         (1.3)
```

Moreover every vector annihilating the first `K` moments is a scalar
multiple of `omega`.

#### Proof

The first two identities are the leading-coefficient formula for the
Lagrange interpolant of `x^m`.  The `K` by `K+1` Vandermonde moment matrix
has rank `K`, so its nullspace has dimension one.  QED

Put

```text
D_U(t)=sum_(j=0)^K omega_j exp(i t u_j).               (1.4)
```

A correction which annihilates moments `0,...,K-1` and has value `A` at a
center `t_0` exists if and only if `D_U(t_0)!=0`; when it exists it is
unique and has transform

```text
A D_U(t)/D_U(t_0).                                    (1.5)
```

This already removes coefficient norm from the discussion.  Scaling the
weights changes numerator and denominator equally.  The only relevant
quantities are response ratios.

---

## 2. Hermite--Genocchi gives the exact nonalias factor

Let `(S_0,...,S_K)` be uniform on the probability simplex

```text
S_j>=0,             sum_j S_j=1,                     (2.1)
```

and put

```text
X_U=sum_j S_j u_j,
Phi_U(t)=E exp(i t X_U).                              (2.2)
```

The Hermite--Genocchi formula for divided differences gives

```text
D_U(t)=(i t)^K Phi_U(t)/K!.                           (2.3)
```

Consequently (1.5), normalized to `A=1`, is exactly

```text
C_(U,t0)(s)
 =(s/t0)^K Phi_U(s)/Phi_U(t0).                        (2.4)
```

The `K!` in the low Taylor remainder is also present in the high response
and cancels.  What high order buys is the ratio `(T/|t_0|)^K`; what it pays
is the reciprocal characteristic function `1/Phi_U(t_0)`.

If the block diameter is

```text
H_U=u_K-u_0                                           (2.5)
```

and `|s|H_U<=1/2`, then, after removing the harmless phase `exp(i s u_0)`,

```text
1-|s|H_U<=|Phi_U(s)|<=1.                              (2.6)
```

Thus the low response is not secretly zero.  In particular,

```text
|C_(U,t0)(T)|
 >=(1-T H_U)(T/|t_0|)^K/|Phi_U(t_0)|,                 (2.7)
```

while the matching upper bound drops the factor `1-T H_U`.

For `N` peak corrections with amplitudes `A_j`, the direct low-leakage
ledger is therefore

```text
sup_(|s|<=T)|sum_j A_j C_(U_j,t_j)(s)|
 <=sum_j |A_j|(T/|t_j|)^(K_j)/|Phi_(U_j)(t_j)|.       (2.8)
```

Cancellation can improve (2.8), but proving it would be a joint
interpolation theorem rather than a consequence of the moment identities.

High order means that a polynomial lower bound in (0.2) is not necessary.
For example, at `|t_j|>=Y^.751` and `T=Y^.01`, the numerator in (2.8) is at
most

```text
Y^(-.741 K_j).                                        (2.9)
```

It can absorb a superpolynomially small nonalias factor if `K_j` grows.
But (2.4) still needs an explicit lower bound on that factor; mere
nonvanishing gives no asymptotic rate.

---

## 3. Uniform mesh: factorial cancellation and exact aliases

Take

```text
u_j=u_0+jh.                                           (3.1)
```

Then

```text
omega_j=(-1)^(K-j)/[j!(K-j)!h^K],                    (3.2)
```

so the binomial theorem gives

```text
D_U(t)
 =exp(i t u_0)[exp(i t h)-1]^K/(K!h^K).              (3.3)
```

Equivalently,

```text
Phi_U(t)
 ={[exp(i t h)-1]/(i t h)}^K exp(i theta_U(t)),       (3.4)
```

where the last factor is a phase.

At

```text
t_m=2 pi m/h,                                         (3.5)
```

equation (3.3) vanishes for every `K>=1`.  Since the moment-zero condition
already includes `sum omega_j=0`, this has a simpler interpretation: all
high phases are equal, so every admissible correction has response zero.
Coefficient size is irrelevant.

For a nonalias center put

```text
q(t_0)=|exp(i t_0 h)-1|.                              (3.6)
```

If `Th=o(1)`, equations (1.5) and (3.3) give

```text
|C_(U,t0)(T)|=(1+o(1))[Th/q(t_0)]^K.                 (3.7)
```

This is the correct version of the proposed factorial gain.  The factorial
does not remain after high normalization.

The full target aperture contains points with

```text
|exp(i t h)-1|=2                                     (3.8)
```

whenever `h=Y^(-1+o(1))`.  Therefore

```text
sup_(t in H)|C_(U,t0)(t)|
 >=[2/q(t_0)]^K.                                     (3.9)
```

Unless the correction center lies at a maximal lobe, the divided
difference is a comb amplifier elsewhere in the high band.  At an alias it
cannot correct at all.  Iteratively chasing these new lobes is not a
contraction supplied by high-order moments.

---

## 4. A generic near-uniform countermodel

The exact alias does not disappear as an obstruction merely by declaring
the nodes nonlattice.  Fix `Y`, a uniform mesh of `M` nodes with

```text
h asyp log Y/Y,              t_*=2 pi/h.              (4.1)
```

Perturb it to

```text
u_j^(epsilon)=u_0+jh+epsilon_j,
max_j |epsilon_j|<=epsilon h.                         (4.2)
```

For every fixed consecutive block and every fixed order `K>=1`, its
barycentric weights and divided difference depend continuously on the
nodes.  At `epsilon=0`,

```text
D_U(t_*)=0,
D_U(T)!=0                         when Th is small.    (4.3)
```

There are only finitely many consecutive blocks and orders `1<=K<M` for a
fixed `Y`.  Hence:

### Proposition 4.1 (adaptive near-alias obstruction)

For every prescribed `L>0`, the perturbations in (4.2) may be chosen
nonzero and generic so that, simultaneously for every legal adaptive block
and order for which the low response is tested,

```text
|D_U(T)/D_U(t_*)|>L                                  (4.4)
```

whenever the denominator is nonzero.  They may also be chosen so that no
nonzero height gives a common phase on all nodes.

#### Proof

Continuity and (4.3) give (4.4) for each member of the finite family after
a sufficiently small perturbation.  Intersect the resulting open
neighborhoods.  The exceptional perturbations producing an exact zero or a
rational relation lie in a finite or countable union of proper analytic
hypersurfaces, so a generic point remains.  QED

The perturbed gaps satisfy

```text
max Delta_j=Y^(-1+o(1)),
sum_j Delta_j^2=Y^(-1+o(1)),                          (4.5)
```

strictly stronger than the imported actual-prime gap bounds.  Thus maximal
gaps, mean-square gaps, path locality, and qualitative nonlattice structure
do not prove the adaptive denominator bound in (0.2).  An actual-prime
argument must use a quantitative nonalias property absent from those data.

---

## 5. Packet correction also needs a far-sidelobe theorem

Let a packet center be `t_j` and let its required correction amplitude be
`A_j`.  The normalized moment corrector is

```text
R_j(t)=-A_j D_(U_j)(t)/D_(U_j)(t_j).                  (5.1)
```

Moment annihilation controls (5.1) only for `|t|H_(U_j)<<1`.  Over the high
tail its exact amplification is

```text
M_j=sup_(t in H)|D_(U_j)(t)|/|D_(U_j)(t_j)|.          (5.2)
```

No estimate for `M_j` follows from the first `K_j` vanishing moments.
Equation (3.9) makes it powerfully false on the lattice model.  The
near-lattice construction makes it arbitrarily large without an exact
common alias.

One can solve for many correctors jointly so that their remote lobes cancel.
But then the unknown is the complete evaluation matrix on the continuum
high band.  That is the original unconstrained quotient/Chebyshev problem;
it is not a consequence of divided-difference order, and no coefficient
norm obstruction is being invoked here.

The fourth-moment packet count helps only after (0.2)--(0.3).  If all
`N<=Y^.0855` centers had quantified factors `chi_j=|Phi_(U_j)(t_j)|`, then
(2.8) would give an explicit choice of the orders `K_j`.  It supplies no
lower bound for `chi_j` and no control of `M_j`, so it cannot make the
iteration self-closing.

---

## 6. Decision

```text
K moment conditions leave one divided-difference direction:       EXACT;
normalized low response formula (0.1):                            EXACT;
factorial survives normalization as an extra gain:                FALSE;
uniform mesh has exact high aliases for every K:                   EXACT;
away from aliases high order gives low leakage (0.5):             EXACT;
away from aliases it is automatically high-tail localized:        FALSE;
qualitative nonlattice removes the need for a denominator bound:   FALSE;
current prime-gap inputs imply adaptive nonalias:                  FALSE;
fourth-moment packet count controls remote comb lobes:             FALSE;
adaptive divided differences close the high tail:                  NOT PROVED;
uniform zeta zero-free strip:                                     NOT PROVED.
```

The construction is not vacuous.  If one proves an adaptive lower bound for
`Phi_U(t_j)` strong enough relative to `(T/t_j)^K` **and** a simultaneous
far-sidelobe bound for the same blocks, then high order makes the low leakage
negligible even for all exceptional packets.  Those two estimates are the
precise surviving arithmetic target.  Neither follows from moment
annihilation or from allowing arbitrarily large coefficients.
