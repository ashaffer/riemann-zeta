# R158 conditioned mixed-point family and skeleton gate

## Status

The quadratic quotient

```text
F_chi(s)=zeta(s)/L(s,chi)                                  (0.1)
```

is the smallest arithmetic family in which the remaining R156 signed
mixed-point problem can be tested.  Requiring

```text
chi(p)=1,                         p<=H,                    (0.2)
```

deletes the complete Euler head.  At the certified conductor scale
`X=exp(BH+o(H))`, `B>2`, this still leaves `X^(1-o(1))` positive
fundamental discriminants, and ordinary real-character zero density removes
the denominator-zero exceptions with a fixed power saving.

This report finds a sharp distinction between two questions.

1. On the full connected localization bridge containing a hypothetical
   zeta zero and a right cap, a mixed-point exceptional estimate is
   conditionally false.  R155 implies that every denominator-zero-free
   member has a zero of `zeta-2L_chi`; real-character zero density therefore
   makes such mixed zeros density one in the conditioned family.
2. On a compact target-local domain strictly inside `1/2<Re(s)<1`, that
   theorem does not locate the forced point.  All mixed points could escape
   the compact set through the transition collar near `Re(s)=1`.  This
   location problem remains open.

There is an exact deterministic reduction.  Put

```text
P_H=product_(p<=H)(1-p^(-s)),
E_H=zeta P_H,
R_(chi,H)=L(s,chi)P_H.                                    (0.3)
```

Then

```text
zeta-2L(s,chi)=[E_H-2R_(chi,H)]/P_H.                       (0.4)
```

Thus conditioned family moments do not see a generic small-value event.
They perturb the deterministic `2`-point divisor of the truncated-zeta
skeleton `E_H`.  A Rouché criterion below makes this exact.

Unconditioned power-saving bounds for the mixed-point family are false:
quadratic character-aspect universality gives a positive-density family
with a mixed zero in any prescribed nonempty target domain.  Direct use of
an approximate functional equation and the quadratic large sieve also
cannot resolve the diagonal conditioned family: the moment order needed to
beat the head entropy tends to infinity, while the conductor-length
approximate functional equation leaves the large-sieve range at fixed
moment order.

```text
conditioned quadratic family size                          X^(1-o(1))
denominator-zero exceptional set                           POWER SAVING
full-bridge mixed-point-free selection under source zero   IMPOSSIBLE
full-bridge mixed-point bad proportion                     1-o(1)
unconditioned mixed-point power-saving upper bound         FALSE
exact truncated-zeta skeleton factorization                THEOREM
deterministic skeleton Rouché criterion                    THEOREM
direct AFE plus ordinary quadratic large sieve             ENTROPY FAILURE
pointwise small-ball plus discretization                    DIMENSION FAILURE
target-local transition-collar escape                      OPEN
diagonal conditioned functional tail theorem               NOT KNOWN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md`](R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md),
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
and
[`R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md).

## 1. The diagonal head-conditioned family

For definiteness, let `D(X,H)` be the positive fundamental discriminants
`d` in `[X,2X]` such that

```text
d=1 mod 8,
chi_d(p)=1                    for every odd p<=H.           (1.1)
```

In particular none of these small primes divides `d`.  Set

```text
M_H=8 product_(3<=p<=H)p.                                  (1.2)
```

The prime number theorem gives

```text
log M_H=H+o(H),
pi(H)=H/log H+o(H/log H).                                  (1.3)
```

For every fixed `B>2`, take `X` in the diagonal range

```text
log X=B H+o(H).                                             (1.4)
```

Squarefree counting in the compatible residue classes modulo `M_H`, as in
R155 Section 3, gives

```text
#D(X,H)
 >>_B X/[2^pi(H) log H]

 =X exp[-(log 2+o(1))H/log H]
 =X^(1-o(1)).                                               (1.5)
```

The harmless `log H` records the local squarefree factors.  Only the final
`X^(1-o(1))` scale is needed below.

Let `Omega` be a fixed bounded set contained in

```text
Re(s)>=sigma_0>1/2,
|Im(s)|<=T.                                                 (1.6)
```

The real-character zero-density estimates imported in R139 give

```text
#{d in D(X,H):L(s,chi_d) has a zero in Omega}
 <=X^[a_*(sigma_0)+epsilon],                               (1.7)
```

where one may take

```text
a_*(sigma)
 =min{3(1-sigma)/(2-sigma), 8(1-sigma)/3}<1.               (1.8)
```

The left side of (1.7) is bounded by the corresponding sum over all real
primitive characters, so no conditioned large sieve is needed here.  From
(1.5),

```text
X^[a_*(sigma_0)+epsilon]=o(#D(X,H))                         (1.9)
```

when `epsilon>0` is sufficiently small.  Thus denominator selection is
compatible with the growing head throughout the right half of the critical
strip.

## 2. Density-one mixed points on the full bridge

The exact normal-family obstruction has a strong family consequence.

Let `Omega_tilde` be a fixed bounded simply connected domain such that

* `closure(Omega_tilde)` lies in `Re(s)>sigma_0>1/2`;
* `1` is not in `closure(Omega_tilde)`, so zeta is holomorphic there;
* `Omega_tilde` contains a nonempty open set `V` in `Re(s)>1`; and
* `Omega_tilde` contains a zeta zero `rho`.

The third and fourth conditions describe the connected localization bridge.
They are compatible when the ordinate of `rho` is nonzero.

### Theorem 2.1 -- conditional density-one mixed-point theorem

Fix `B>2`, choose

```text
0<epsilon<1-a_*(sigma_0),                                  (2.0)
```

and let `H -> infinity`, `log X=BH+o(H)`.  Under the four hypotheses
above,

```text
#{d in D(X,H):zeta(s)-2L(s,chi_d) has a zero in Omega_tilde}

 >=#D(X,H)-X^[a_*(sigma_0)+epsilon].                       (2.1)
```

In particular the proportion on the left tends to one.

#### Proof

For `d in D(X,H)`, the Euler products give, uniformly on compact subsets of
`Re(s)>1`,

```text
F_(chi_d)(s)=zeta(s)/L(s,chi_d)=1+O_V(H^(-epsilon_V)).      (2.2)
```

Suppose that `L(s,chi_d)` has no zero in `Omega_tilde`.  Then `F_(chi_d)`
is holomorphic there.  Its zero divisor is contained in the fixed zeta zero
divisor, so the number of its distinct zeros is bounded independently of
`d` and `H`.  It retains `F_(chi_d)(rho)=0`.

R155 Theorem 2.1, applied to (2.2), says that such a function cannot omit
the value `2` for all sufficiently large `H`.  Hence

```text
F_(chi_d)(s)=2
```

somewhere in `Omega_tilde`, which is equivalent to

```text
zeta(s)-2L(s,chi_d)=0.                                    (2.3)
```

The only possible exceptions are therefore the characters whose
denominator has a zero in `Omega_tilde`.  Equation (1.7) bounds those
exceptions and proves (2.1).  QED.

### Consequence 2.2 -- the full-bridge exceptional estimate is conditionally false

Under the retained-zero hypothesis, neither

```text
#{d in D(X,H):zeta-2L_(chi_d) has a zero in Omega_tilde}
 =o(#D(X,H))                                                (2.4)
```

nor any fixed-proportion upper bound below `#D(X,H)` can hold.  Proving
such a bound would exclude `rho`; it is not a routine family lemma waiting
to be imported.

There is also a deterministic special case.  The function

```text
E_H(s)=zeta(s) product_(p<=H)(1-p^(-s))                    (2.5)
```

is holomorphic in `Omega_tilde`, has the fixed zeta zero divisor, and tends
to `1` on `V`.  R155 therefore gives

```text
E_H(s)=2                                                    (2.6)
```

at some point of `Omega_tilde` for every sufficiently large `H`.

## 3. Why a target-local domain is different

Let now

```text
Omega compactly contained in {1/2<Re(s)<1}.                (3.1)
```

Even if `Omega` contains the source zero, Theorem 2.1 does not imply that
the forced mixed point lies in `Omega`.  Its proof uses connected analytic
continuation from the source zero to an open right cap.  Once the compact
target is cut away from that cap, the omitted-value family can discharge
its nonnormality in the complement.

For every fixed `epsilon>0`, (2.2) shows that `F_chi=2` is impossible on
fixed compact subsets of

```text
Re(s)>=1+epsilon                                           (3.2)
```

when `H` is large.  This still allows every forced point to approach the
line `Re(s)=1`, from either side, through a shrinking transition collar.
No result in R155--R157 rules this out.

Thus the following two assertions must not be conflated.

```text
mixed-point-free on the full connected bridge              IMPOSSIBLE

mixed-point-free on one fixed compact Omega left of one    OPEN.          (3.3)
```

Moreover, target-local avoidance by itself is sufficient for R153 only if
`Omega` contains every mixed divisor capable of entering the selected
power-sum radius.  A point in the transition collar can be closer to the
right-hand differentiation center than the source zero and cannot simply be
discarded.

## 4. Exact truncated-zeta skeleton factorization

Define the three functions in (0.3).  Since (1.1) holds, their Euler
products in `Re(s)>1` satisfy

```text
R_(chi,H)(s)
 =product_(p>H)(1-chi(p)p^(-s))^(-1),                      (4.1)
```

with the usual omission of primes dividing the conductor.  Algebraically,
throughout every domain of holomorphy,

```text
zeta(s)=E_H(s)/P_H(s),
L(s,chi)=R_(chi,H)(s)/P_H(s),                              (4.2)

zeta(s)-2L(s,chi)
 =[E_H(s)-2R_(chi,H)(s)]/P_H(s).                           (4.3)
```

The finite Euler product `P_H` has no zero in `Re(s)>0`.
Consequently the mixed-point divisor is exactly the zero divisor of

```text
E_H-2R_(chi,H).                                             (4.4)
```

This factorization reverses the naive small-ball interpretation.  Once the
head is conditioned, the varying function is a tail perturbation of the
deterministic skeleton `E_H`; it is not an unstructured sample of
`L(s,chi)` near the fixed value `zeta(s)/2`.

### Theorem 4.1 -- deterministic skeleton Rouché criterion

Let `Omega` be a Jordan domain compactly contained in `Re(s)>1/2`.  Assume
that neither `E_H-2` nor `E_H-2R_(chi,H)` vanishes on `partial Omega`, and
put

```text
m_H(Omega)=min_(s in partial Omega)|E_H(s)-2|.              (4.5)
```

If

```text
sup_(s in partial Omega)|R_(chi,H)(s)-1|<m_H(Omega)/2,      (4.6)
```

then, with multiplicity,

```text
N_Omega[zeta-2L_(chi)]
 =N_Omega[E_H-2].                                          (4.7)
```

#### Proof

On `partial Omega`, (4.6) is precisely

```text
|[E_H-2R_(chi,H)]-[E_H-2]|
 =2|R_(chi,H)-1|<|E_H-2|.                                  (4.8)
```

Rouché's theorem and (4.3) prove (4.7).  QED.

The criterion has two opposite consequences.

* If `N_Omega(E_H-2)=0` and the boundary gap in (4.5) is larger than an
  attainable tail error, (4.6) supplies a mixed-point-free character.
* If `N_Omega(E_H-2)>0` robustly, ordinary tail concentration makes mixed
  points more common, not less common.

Thus a useful family theorem must be calibrated against both the winding
and the condition number of the deterministic function `E_H-2`.

## 5. What the random tail predicts, and what is not proved

In the independent quadratic Euler model, the logarithm of (4.1) has mean
and variance on a line `Re(s)=sigma>1/2` of sizes

```text
mean log R_(chi,H)=O(H^(1-2sigma)/log H),

Var log R_(chi,H)
 asymp sum_(p>H)p^(-2sigma)
 asymp H^(1-2sigma)/log H.                                 (5.1)
```

The natural pointwise fluctuation scale is therefore

```text
v_H(sigma)=H^(1/2-sigma)(log H)^(-1/2).                    (5.2)
```

This calculation is exact for the independent sign model and is consistent
with the known random-Euler-product descriptions of quadratic values.  It
is not, by itself, a theorem uniform in the diagonal arithmetic family
`D(X,H)` on a compact set in the critical strip.

The missing functional statement would have the following form.

### Target 5.1 -- conditioned functional tail theorem

For every compact `K` in `Re(s)>sigma_0>1/2`, after removing the
power-saving denominator-zero exceptional set, prove a quantitative bound
such as

```text
#{d in D(X,H):
  sup_(s in K)|R_(chi_d,H)(s)-1|>lambda_H}
 =o(#D(X,H)),                                               (5.3)
```

where `lambda_H ->0` is explicit and ideally has the scale
`H^(1/2-sigma_0+o(1))`.

Existing quadratic universality theorems first fix all local conditions and
then send the conductor to infinity.  Their constants and convergence rates
are not uniform when the conditioned prime set grows with
`H asymp log X`.  Existing point-value distributions are also insufficient
for the supremum event in (5.3).

Even Target 5.1 would not by itself select avoidance.  It must be combined
with

```text
N_Omega(E_H-2)=0,
m_H(Omega)>2 lambda_H.                                     (5.4)
```

On the full bridge, (2.6) proves that the first condition in (5.4) is
eventually false.

## 6. An unconditioned power-saving bound is false

There is a separate literature-level obstruction to treating the mixed
point as an ordinary rare value.

### Theorem 6.1 -- positive-density unconditioned mixed points

Let `Omega` be any nonempty open subset of

```text
1/2<Re(s)<1.                                                (6.1)
```

Then there is a compact disc `K` contained in `Omega` and a positive
constant `c_K` such that a positive lower proportion of positive
fundamental discriminants `d` satisfy

```text
zeta(s)-2L(s,chi_d)=0
```

at some point of `K`.

#### Proof

Choose a nonreal point `s_0 in Omega` which is not a zeta zero and a small
closed disc `K` about it.  Include the reflected disc when applying the
real-character universality theorem.  The two discs have connected
complement and no real slice.

For sufficiently small nonzero `c`, define on the upper disc

```text
h(s)=zeta(s)/2+c(s-s_0),                                   (6.2)
```

and define it by conjugate reflection on the lower disc.  Shrinking `K`
if necessary makes `h` holomorphic and nonvanishing.  It is therefore an
admissible target in the quadratic character-aspect universality theorem of
Mishou and Nagoshi.  A positive lower proportion of discriminants obey

```text
sup_(s in K)|L(s,chi_d)-h(s)|<epsilon                       (6.3)
```

for every sufficiently small fixed `epsilon`.

But

```text
zeta(s)-2h(s)=-2c(s-s_0)                                  (6.4)
```

has one simple zero.  Rouché's theorem transfers it to
`zeta-2L_(chi_d)` for every discriminant in (6.3).  QED.

Consequently, for no fixed `delta>0` can one have the unconditioned bound

```text
#{d<=X:zeta-2L_(chi_d) has a zero in Omega}
 <<X^(1-delta).                                             (6.5)
```

The prime-discriminant universality theorem gives the analogous statement
inside a fixed arithmetic progression.  Hence any fixed finite collection
of compatible Legendre-symbol conditions can be imposed before taking the
conductor limit.  The dependence on that fixed modulus is not uniform and
does not permit the diagonal substitution `H asymp log X`.

This is the precise quantifier boundary:

```text
H fixed, then X -> infinity       mixed zeros have positive density;

H -> infinity with log X asymp H  no imported theorem decides the
                                  target-local event.       (6.6)
```

## 7. Approximate-functional-equation and large-sieve ledger

The ordinary quadratic large sieve cannot simply be restricted to the thin
family.  A nonnegative unconditioned moment bound loses the reciprocal
density

```text
2^pi(H)=exp[(log 2+o(1))H/log H]                            (7.1)
```

after division by (1.5).  This exceeds every fixed negative power of `H`.

The obstruction persists at high moments.  Suppose optimistically that a
tail polynomial at a fixed point has variance

```text
V_H=H^[-(2sigma-1)+o(1)]                                  (7.2)
```

and even suppress the unfavorable factorial factor `k^k` in its
Gaussian-size moments.  To make Markov's inequality beat (7.1) at a fixed
nonzero threshold would still require

```text
k
 >[log 2/(2sigma-1)+o(1)] H/(log H)^2.                     (7.3)
```

On the other hand, an approximate functional equation for a conductor-`X`
quadratic `L`-function has length `X^(1/2+o(1))`.  Raising it to the `k`th
power produces a Dirichlet polynomial of length

```text
X^(k/2+o(k)).                                               (7.4)
```

Restoring the actual Gaussian factor `(CkV_H)^k` only worsens this necessary
condition and, for much of the strip, prevents such a moment from being
small at all.  Independently, the quadratic large sieve has the schematic
cost `X+N` for polynomial
length `N`.  Equations (7.3)--(7.4) leave that range already at fixed
`k>2`, long before the required growing moment.

This does not prove that a conditioned moment theorem is false.  It proves
that it must use the CRT structure of (1.1), a much shorter logarithmic
Euler approximation, or a new conditioned large sieve.  The direct
conductor-length AFE plus the ordinary quadratic large sieve fails before
the mixed-point geometry is reached.

## 8. Pointwise small balls do not discretize a zero event

There is a second method-independent dimension check.  Let

```text
G_chi(s)=zeta(s)-2L(s,chi)                                 (8.1)
```

and suppose on a fixed two-dimensional compact set that

```text
sup |G_chi'|<=M_X.                                         (8.2)
```

If `G_chi` has a zero, a mesh of spacing `epsilon/M_X`
contains a point where `|G_chi|<=epsilon`.  Such a mesh has

```text
asymp M_X^2/epsilon^2                                      (8.3)
```

points.  Even an ideal bounded planar density gives a fixed-point small-ball
probability only of order `epsilon^2`.  The union bound leaves the factor
`M_X^2`; decreasing `epsilon` supplies no saving.

This is the expected codimension match: a complex zero imposes two real
conditions but can move in two real dimensions.  A useful theorem must
control the analytic path, winding, or Jensen characteristic, not merely
the value distribution at predetermined samples.

The same issue appears in Jensen's formula.  Quadratic large-sieve moments
control the positive part of `log |G_chi|`.  Counting characters with a zero
requires a lower-tail or inverse-moment bound for `G_chi`, and the additive
combination (8.1) has no Euler product from which to build the standard
zero-detecting mollifier.  No existing quadratic zero-density theorem
applies to (8.1).

## 9. Exact surviving alternatives

For a target-local compact `Omega`, a mixed-point-free denominator can be
selected as soon as one proves

```text
#{d in D(X,H):
  L_(chi_d) has a zero in Omega
  or zeta-2L_(chi_d) has a zero in Omega}
 <#D(X,H).                                                  (9.1)
```

The first exceptional set is already `o(#D(X,H))` by (1.7).  The second
cannot be replaced by an unconditioned power-saving estimate, and on the
full bridge it has conditional density one by Theorem 2.1.

The remaining target-local options are therefore exact.

1. Find cutoffs `H` for which the deterministic skeleton satisfies (5.4),
   and prove enough of Target 5.1 to apply Theorem 4.1.
2. Construct an atypical tail prime pattern which approximates a
   nonvanishing target `g_H` for which `E_H-2g_H` is zero-free on `Omega`,
   with conductor and entropy uniform in `H`.
3. Keep the forced mixed points and prove the signed joint reciprocal-power
   estimate requested in R155--R156.

The first two alternatives can only be target-local.  Extending either
approximation across the full connected bridge would contradict Theorem
2.1 under the source-zero hypothesis.  This report neither proves nor
disproves a fixed zero-free strip.

## Primary sources

* D. R. Heath-Brown,
  [*A mean value estimate for real character
  sums*](https://ora.ox.ac.uk/objects/uuid:b188b365-d8d1-4267-8548-49f01e6cb6a7),
  Acta Arith. 72 (1995), especially the quadratic large sieve and Theorem 3.
* C. C. Corrigan,
  [*A note on the zeros of L-functions associated to fixed-order Dirichlet
  characters*](https://arxiv.org/abs/2310.16518),
  Bull. Aust. Math. Soc. 110 (2024), especially Theorem 2.1.
* H. Mishou and H. Nagoshi,
  [*Functional distribution of `L(s,chi_d)` with real characters and
  denseness of quadratic class numbers*](https://doi.org/10.1090/S0002-9947-06-03825-6),
  Trans. Amer. Math. Soc. 358 (2006), 4343--4366.
* H. Mishou and H. Nagoshi,
  [*The universality of quadratic L-series for prime
  discriminants*](https://doi.org/10.4064/aa123-2-3),
  Acta Arith. 123 (2006), 143--161.
* H. Mishou and H. Nagoshi,
  [*Equivalents of the Riemann
  hypothesis*](https://doi.org/10.1007/s00013-005-1375-1),
  Arch. Math. 86 (2006), 419--424.
* Y. Lamzouri,
  [*On the distribution of extreme values of zeta and `L`-functions in the
  strip `1/2<sigma<1`*](https://arxiv.org/abs/1005.4640),
  Int. Math. Res. Not. 2011, for the random-Euler-product value model.

Successor:
[`R159-QUADRATIC-FUNCTIONAL-EQUATION-MIXED-POINT-GATE.md`](R159-QUADRATIC-FUNCTIONAL-EQUATION-MIXED-POINT-GATE.md).
