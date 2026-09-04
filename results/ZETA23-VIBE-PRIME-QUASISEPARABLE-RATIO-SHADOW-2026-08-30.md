# Prime quasiseparable ratio shadows: the non-tensor Fejer branch

**Date:** 2026-08-30  
**Status:** proved reduction and arithmetic invariant; proposed rigidity
theorem remains open; no zero-free strip and no proof of RH

**Subsequent curvature refinement.**  The odd triangle-charge theorem in
`ZETA23-VIBE-PQR-ODD-CURVATURE-CHARGE-ADDENDUM-2026-08-30.md` supersedes the
conditional `.6961` calibration below: parity forces every transported seed
to satisfy `diam(A)>>m t_0/sqrt(Y)` and physical width `>>m sqrt(Y)`.  Thus a
near-minimal Sidon ruler already fails for `t_0>Y^(.5179+o(1))` at the project
value `m=Y^(.0179+o(1))`.

**Subsequent cold-round update.**  The shared-index same-side branch has a
stronger elementary constraint than the localized bound recorded in Section
6: the half-integer triangle identity proves

```text
W >>M sqrt(Y).
```

Consequently `W=o(m sqrt(Y))` is impossible after weighted cleaning, and a
near-minimal Sidon ruler is excluded for `t_0>Y^(.5179+o(1))`.  This
supersedes the `.696133` boundary below within that branch.  The proof,
single-cut countermodel, and exact prime sanity check are in
`ZETA23-VIBE-PQR-HALF-INTEGER-TRIANGLE-COLLAPSE-2026-08-30.md`.

## 0. Verdict

The critical-inverse-large-sieve proposal cannot send every saturation state
straight to a digit tensor.  There is a much larger exact synthetic class.
For every finite integer seed `A`, not just a generalized progression, its
off-diagonal autocorrelation has one-sided cap of order `1/#A`.  Sidon and
perfect-difference seeds need not have useful tensor peeling.

If such a Sidon state is transported to distinct same-side prime-log nodes at
the required aggregate accuracy, elementary cleaning produces a linear-size
complete prime graph.  Across every ordered cut its prime matrix has exact
rank two, not merely approximate rank two.  Equivalently it is a symmetric
rank-two quasiseparable prime kernel.  Its exact arithmetic data are nested
nonzero Pluecker minors of height

```text
H=Y^2/B=Y^(16/33).
```

This reduction is proved below.  What is not proved is the new arithmetic
terminator:

```text
prime quasiseparable ratio-shadow rigidity (PQR):
    m << (log Y)^C,
```

or the stronger expected scale `m<<log Y/log log Y`.  Broad one-flattening
SR2PF gives only `m<<Y^(4/33+o(1))` and therefore does not settle PQR.
The all-cut tensor SR2PF theorem settles only the product/digit subbranch.

For reflected prime pairs there is a second exact label

```text
G_ij=4p^-_ij p^+_ij-(2Y)^2,       0<|G_ij|<<Y^2/B.
```

The gap labels alone recover only `m<<Y^(8/33+o(1))`.  A successful theorem
must couple them to the nested Pluecker system, as in a source-sensitive
vector sieve.

## 1. Arbitrary-seed Fejer states

Let

```text
A={a_1<...<a_m} subset Z,        omega=2pi/t_0,
```

and put

```text
K_A(t)=m^-1 |sum_i exp(i omega a_i t)|^2,
F_A(t)=[1-K_A(t)]/[2(m-1)].                         (1.1)
```

If `nu(d)` counts pairs `i>j` with `a_i-a_j=d`, then

```text
F_A(t)=-sum_(d>0) nu(d)/[m(m-1)] cos(omega d t).    (1.2)
```

Consequently, for every real `t`,

```text
F_A(t)<=1/[2(m-1)],
F_A(0)=F_A(t_0)=-1/2.                               (1.3)
```

Taking source depth `D=1`, equation `(1.3)` gives the exact normalization

```text
F_A(t_0)+D F_A(0)=-1.                               (1.4)
```

No additive structure of `A` was used.  In particular a Sidon/Golomb-ruler
seed, for which every positive difference is distinct, is an exact
one-sided saturation model with `m(m-1)/2` singleton frequencies and no
forced product coordinates.  This is a rigorous abstract falsifier for any
near-saturation lemma whose structured output is always a digit tensor.

Perfect-difference constructions also occur as exact extremizers in Turan
power-sum problems; see Johan Andersson,
[*Explicit solutions to certain inf max problems from Turan power sum
theory*](https://arxiv.org/abs/math/0607238).  They support the same warning,
although the continuous-time state `(1.1)` is established directly and does
not require that paper.

## 2. The faithful same-side transport hypothesis

Freeze

```text
B=Y^(50/33),          delta=Y/B,          H=Y^2/B.
```

Assume `Y=N+1/2`, `Y^.5<=t_0<=Y`, and that `A` is Sidon.  For every edge
`i>j`, suppose an ordinary shell prime `p_ij`, all on the same side of `Y`,
is assigned to the frequency `omega(a_i-a_j)`.  Write

```text
e_ij=||log(p_ij/Y)|-omega(a_i-a_j)|.                 (2.1)
```

The aggregate accuracy which preserves the Fejer cap is

```text
sum_(i>j) e_ij/[m(m-1)] <= kappa/(mB).               (2.2)
```

Indeed, for every `t<=B`, changing the frequencies changes `(1.2)` by at
most `B` times the left side of `(2.2)`, namely `O(kappa/m)`.

### Proposition 2.1 -- linear-size pointwise cleaning

For every fixed `C>0`, `(2.2)` supplies a subset `V subset {1,...,m}` with

```text
#V >= m/(1+2kappa/C)-O(1)                            (2.3)
```

such that

```text
e_ij<=C/B                 for all i,j in V, i>j.     (2.4)
```

For large `Y`, all the retained primes are automatically distinct even if
distinctness was not assumed separately.

#### Proof

Multiplying `(2.2)` by `m(m-1)` gives

```text
sum_(i>j)e_ij <=kappa(m-1)/B.                        (2.5)
```

Thus the graph of edges violating `(2.4)` has at most `kappa(m-1)/C`
edges.  Turan's elementary independence bound
`alpha(G)>=m^2/(m+2e(G))` gives `(2.3)`.

If two retained edges had the same prime, their distinct Sidon differences
would give

```text
omega<=2C/B.
```

But `omega=2pi/t_0>=2pi/Y`, whereas `B/Y=Y^(17/33)->infinity`.  This is
impossible for large `Y`.  QED

The same argument works whenever a weighted autocorrelation contains a
linear-size Sidon subgraph on which the individual weights are comparable to
`m^-2`.  Producing such a subgraph from an arbitrary separator is part of the
unproved analytic extraction, not part of Proposition 2.1.

## 3. Determinant collapse and the quasiseparable invariant

Relabel the cleaned set as `1<...<M`.  If the primes lie above `Y`, set

```text
X_ij=Y exp[omega(a_i-a_j)]       (i>j);              (3.1)
```

for lower-side primes replace `omega` by `-omega`.  On every ordered
rectangle (all row indices larger than all column indices), `(X_ij)` has
rank one.  Equation `(2.4)` gives

```text
p_ij=X_ij+O(delta).                                  (3.2)
```

### Proposition 3.1 -- exact ordered-cut rank two

Every `3 x 3` integer minor in an ordered rectangle vanishes.  Every `2 x 2`
minor whose four edge labels are distinct is a nonzero integer of magnitude
`O(H)`.  Hence every ordered block with at least two rows and columns has
rational rank exactly two.

#### Proof

In the determinant of `X+E`, the zero-error term vanishes because `X` has
rank one.  Every one-error term also vanishes because the other two reference
columns are proportional.  Therefore

```text
|det(p_ij)| <<Y delta^2+delta^3
             <<Y^3/B^2=Y^(-1/33)=o(1).              (3.3)
```

The determinant is an integer, so it is zero.  For a `2 x 2` minor the same
expansion gives `O(Y delta+delta^2)=O(H)`.  Equality to zero would equate two
products of four globally distinct primes, contrary to unique
factorization.  QED

Complete the edge array symmetrically by `P_ij=P_ji=p_ij` off the diagonal.
Proposition 3.1 says that for every cut `k`,

```text
rank_Q P[{k+1,...,M},{1,...,k}] <=2.                 (3.4)
```

Thus `P` is a symmetric rank-two **quasiseparable** kernel.  This is weaker
than global matrix rank two and stronger than one isolated SR2PF
flattening.

There is an explicit nested rational generator.  Fix anchor columns
`c_1<c_2`.  For every later column `j` and all rows `i>j`,

```text
p_ij=alpha_j p_(i,c_1)+beta_j p_(i,c_2).             (3.5)
```

Choose any two rows beyond `j`; their anchor `2 x 2` minor is nonzero, so
`alpha_j,beta_j` are uniquely determined.  Every further row satisfies
`(3.5)` by the corresponding vanishing cubic minor.  Cramer's rule and the
minor bound show that their numerators and denominators before reduction are
nonzero integers of size `O(H)`.  Moving the cut gives a nested family of
such generators.  Its nonzero bounded minors and their exact Pluecker
relations are the arithmetic invariant which a PQR proof must exploit.

## 4. The proposed arithmetic theorem card

> **PQR -- prime quasiseparable ratio-shadow rigidity.**  Under the
> hypotheses of Section 2, or equivalently under `(3.2)--(3.4)` together
> with the common ordered exponential reference and global distinctness,
> prove
>
> ```text
> M <<(log Y)^C.                                     (4.1)
> ```
>
> The stronger expected target is
>
> ```text
> M <<log Y/log log Y.                               (4.2)
> ```

This is a conjectural theorem card.  No proof of `(4.1)` is presently in the
project or in the checked literature.

The already proved broad projective-sieve estimate applies to any one
ordered rectangle and gives only

```text
M <<H^(1/4)=Y^(4/33+o(1)),                           (4.3)
```

which is vacuous for the required seed size `M=Y^(.0179+o(1))`.  The faithful
tensor SR2PF theorem applies if the seed has enough compatible product
coordinates; a general Sidon seed supplies only the nested cut structure
`(3.4)`.  Therefore determinant collapse identifies PQR but does not by
itself terminate it.

A plausible proof route is an entropy sieve on the nested projective
generators in `(3.5)`: modulo each small prime, primality excludes one polar
class for every earlier vertex; either the available projective entropy
contracts at a fixed rate, or repeated generator ratios create a product
subcube already excluded by tensor SR2PF.  The required source signs and the
nested, rather than single-cut, compatibility must be retained.  This route
is a proposal, not a deduction from the ordinary larger sieve.

## 5. Reflected-pair enhancement and its exact limit

Suppose a frequency is represented by a Fourier-close reflected pair

```text
p^-<Y<p^+,
|log(Y/p^-)-log(p^+/Y)|<=C/B.                        (5.1)
```

Put `Q=2Y=2N+1` and

```text
G=4p^-p^+-Q^2.                                      (5.2)
```

Then

```text
G in Z,             0<|G|<<Y^2/B=Y^(16/33).         (5.3)
```

The size follows by exponentiating `(5.1)`.  Nonvanishing follows already
modulo four: `4p^-p^+` is divisible by four whereas `Q^2` is odd.  If two
pairs have the same `G`, they have the same prime product and hence the same
unordered pair by unique factorization.  Therefore the gap labels are
injective, and counting gives only

```text
#pairs <<Y^(16/33),
M <<Y^(8/33)                                         (5.4)
```

when pairs label the edges of a complete graph.  This is far above the
target.

The strengthened reflected theorem card is consequently:

> **PQR+G.**  Prove `(4.1)` for two coupled rank-two quasiseparable prime
> kernels `P^-` and `P^+`, using both their nested bounded Pluecker minors
> and the entrywise small-gap equations `(5.2)--(5.3)`.

This is the exact setting for the proposed semiprime-gap vector sieve.  The
scalar gap count `(5.4)` and determinant collapse considered separately do
not prove it.

## 6. Source-height geometry

Let

```text
m=Y^(tau+o(1)),             tau=.0179,
t_0=Y^(alpha+o(1)),
diam(A)=Y^(rho+o(1)).                                (6.1)
```

The physical diameter of the same-side shadow is, while it remains in a
small logarithmic arc,

```text
W asyp Y omega diam(A)=Y^(1+rho-alpha+o(1)).         (6.2)
```

The calibrated localized-carrier theorem at upper exponent `c=.019`
excludes a complete carrier when

```text
1+rho-alpha < theta_H,
theta_H=(1+c)/3=.339666666... .                      (6.3)
```

A Sidon set of `m` integers has

```text
diam(A)>=m(m-1)/2=Y^(2tau-o(1)).                     (6.4)
```

For a near-minimal Sidon ruler, `rho=2tau=.0358`, equations `(6.2)--(6.3)`
show that the localized theorem already kills the state whenever

```text
alpha>1+2tau-theta_H
      =.696133333... .                               (6.5)
```

This is the source of the `.6961` boundary.  It is conditional on
near-minimal diameter.  A more widely spaced Sidon ruler has larger `rho`
and is not eliminated by `(6.5)`.  The full surviving region is exactly

```text
rho>=alpha-1+theta_H.                                (6.6)
```

The later half-integer triangle theorem strengthens this phase diagram.  For
a cleaned same-side complete graph it gives `W>>M sqrt(Y)`, hence excludes

```text
alpha>1/2+rho-.0179.
```

For a near-minimal ruler this is `alpha>.5179`, leaving only
`.5<=alpha<=.5179` at minimal diameter.  PQR is therefore needed for low
source ordinates and sparse, large-diameter/wide-span rulers.  Section 6's
localized calculation remains correct but is no longer the best bound in the
shared-index same-side setting.

## 7. Consequence for the proof search

The corrected saturation fork is

```text
critical carrier/corrector saturation
       |
       +-- low-doubling/product seed
       |       -> all-cut tensor transport -> tensor SR2PF -> CLOSED
       |
       +-- Sidon/diffuse seed
               -> prime quasiseparable ratio shadow -> PQR or PQR+G -> OPEN.
```

Accordingly, a critical inverse large-sieve theorem must output a general
prime-labelled autocorrelation graph, not always a peelable tensor.  The
highest-information arithmetic falsifier is now a finite search for large
same-side prime quasiseparable shadows with all ordered cubic minors zero and
all quadratic minors in `[-H,H]`; for the reflected branch it should record
the coupled `G` labels as well.

One literature boundary is relevant.  Krein spectral factorization gives a
factor for a globally nonnegative entire function of exponential type, but
the factor need not retain a finite or uniformly almost-periodic spectrum
without additional hypotheses; see Wayne Lawton,
[*Note on Spectral Factorization Results of Krein and Levin*](https://arxiv.org/abs/2104.08917).
The project has only interval positivity before extraction.  Hence no
published spectral-factor theorem currently supplies the missing analytic
map from an arbitrary actual-prime separator to the PQR shadow.

```text
arbitrary-seed Fejer saturation:                         PROVED
Sidon weighted cleaning to a linear good clique:          PROVED
ordered cubic determinant collapse:                       PROVED
nested rank-two quasiseparable representation:            PROVED
semiprime gap invariant and scalar bound:                  PROVED
near-minimal source-height boundary alpha=.696133...:      PROVED
shared-index half-integer boundary alpha=.5179:             PROVED LATER
analytic separator -> autocorrelation graph extraction:   OPEN
PQR / PQR+G arithmetic rigidity:                           OPEN
uniform zero-free strip:                                  NOT PROVED
RH:                                                       NOT PROVED
```
