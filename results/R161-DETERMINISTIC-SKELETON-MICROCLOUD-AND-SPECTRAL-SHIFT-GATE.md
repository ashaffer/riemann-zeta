# R161 deterministic skeleton microcloud and spectral-shift gate

## Status

R158 reduced one possible continuation of the quadratic-family argument to
the deterministic function

```text
P_H(s)=product_(p<=H)(1-p^(-s)),
E_H(s)=zeta(s)P_H(s).                                      (0.1)
```

The hoped-for input was a sequence of cutoffs on which `E_H-2` has no zero
in a fixed target neighborhood.  That input is false in the strongest local
sense relevant here.  Every sufficiently large cutoff has a polynomially
large, uniformly conditioned cloud of `E_H=2` points in an
`O(1/log H)` microdisc inside every fixed open subset of the strip.  The
same statement holds in an `O(1/log H)` neighborhood of any hypothetical
off-line zeta zero.

The cloud has a computable leading signed reciprocal-power law.  In
particular, a same-height cloud does not cancel itself at proportional
orders `k asymp log H`.  Clouds farther to the right are smaller in number
but closer to the right-hand differentiation point, and can exponentially
dominate the target cloud.  Thus a local packet near a retained zeta zero is
not a closed signed system.

There is an exact way to subtract the universal cutoff lattice.  Its signed
divisor is a spectral shift between `zeta P_H-2` and `cP_H-2`.  In the
large-`P_H` phase this shift tends to `zeta'/zeta-c'/c`; in the small-`P_H`
phase it tends to zero.  Hence zeta-zero multiplicity is indeed a missing-
sheet defect transported across the cutoff Stokes curves.  The subtraction,
however, gives residue `-1` to every background point, loses the positive
divisor, and cannot share the right-cap head normalization unless `c=zeta`,
which makes the defect identically zero.  Standard PNT accuracy is also far
coarser than one sheet, so it cannot evaluate the residual global signed
moment after subtracting two clouds of polynomial size.

```text
uniform prime-sum phase asymptotic                         THEOREM
E_H=2 microcloud in every fixed open strip set             THEOREM
microcloud within C/log H of a hypothetical zeta zero      THEOREM
simple points and disjoint conditioned boundary circles    THEOREM
proportional-order signed microcloud moment law             THEOREM
internal cancellation of a same-height cloud               FALSE
neglect of rightward corridor clouds                        FALSE
exact background spectral-shift divisor identity           THEOREM
zeta multiplicity as a large-P_H missing-sheet defect       THEOREM
fixed scalar background preserving the right head          ONLY c=zeta
PNT-level computation of the sheetwise global residual     INSUFFICIENT
fixed uniform zeta zero-free strip                          NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md),
and
[`R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md`](R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md).

## 1. Exact logarithmic phase

Put

```text
L=log H,
S_H(s)=sum_(p<=H) p^(-s),
Q_H(s)=sum_(p<=H) sum_(nu>=2) p^(-nu s)/nu.                (1.1)
```

For `Re(s)>0`, every factor in `P_H` is nonzero and the absolutely
convergent logarithm of each finite Euler factor gives

```text
P_H(s)=exp[-S_H(s)-Q_H(s)].                                (1.2)
```

On a simply connected set on which `zeta` is finite and nonzero, choose a
branch

```text
g(s)=Log(zeta(s)/2),
T_H(s)=S_H(s)+Q_H(s)-g(s).                                 (1.3)
```

Then

```text
E_H(s)/2=exp[-T_H(s)],
E_H(s)=2  iff  T_H(s) in 2 pi i Z.                         (1.4)
```

Thus `E_H=2` is not an unstructured value-distribution question.  It is the
inverse image of a fixed vertical lattice under an explicit prime-sum
phase.

For every `sigma_*>1/2`, the series defining `Q_H` and each fixed derivative
is uniformly bounded on compact subsets of `Re(s)>=sigma_*`.  This follows
from

```text
sum_p sum_(nu>=2) (log p)^j p^(-nu sigma_*) < infinity.    (1.5)
```

### Lemma 1.1 -- uniform endpoint PNT

Let `K` be a compact subset of

```text
0<Re(s)<1.                                                 (1.6)
```

Uniformly for `s in K`,

```text
S_H(s)=A_H(s)(1+O_K(1/L))+O_K(1),
A_H(s)=H^(1-s)/((1-s)L).                                  (1.7)
```

The same estimate is uniform on a fixed complex neighborhood of `K`.

#### Proof

Partial summation and the classical PNT with a de la Vallee Poussin error
give

```text
S_H(s)=integral_2^H t^(-s)/log(t) dt
       +O_K(H^(1-Re(s)) exp[-c sqrt(L)])+O_K(1).           (1.8)
```

One endpoint integration by parts, uniformly because `1-s` stays away from
zero on `K`, gives

```text
integral_2^H t^(-s)/log(t) dt
 =H^(1-s)/((1-s)L)(1+O_K(1/L))+O_K(1).                    (1.9)
```

Equations (1.8)--(1.9) prove the result.  Applying them on a slightly larger
compact set also supplies derivative estimates by Cauchy's formula.  QED.

The decisive feature is

```text
|A_H(s)| asymp_K H^(1-Re(s))/L -> infinity.                (1.10)
```

## 2. Phase-centered microdiscs

Fix

```text
s_0=sigma_0+i t_0,
1/2<sigma_0<1,                                             (2.1)
```

and suppose first that `zeta(s_0)` is finite and nonzero.  Let `r>0` be
small and fixed.  For every sufficiently large `H`, one can choose a real
number `u_H` in a fixed bounded interval of length greater than `2 pi` such
that

```text
s_H=s_0+i u_H/L,
A_H(s_H)=iY_H,
Y_H asymp_(s_0) H^(1-sigma_0)/L.                          (2.2)
```

Indeed, as `u` traverses such an interval, the argument of
`A_H(s_0+iu/L)` changes by `-u+O(1/L)` and therefore crosses the desired
phase modulo `2 pi`.

Use the scaled coordinate

```text
s=s_H+xi/L.                                                (2.3)
```

Uniformly for `|xi|<=r`, Lemma 1.1 gives

```text
A_H(s_H+xi/L)/A_H(s_H)
 =exp(-xi)(1+O_(s_0,r)(1/L)),                              (2.4)

T_H(s_H+xi/L)/A_H(s_H)=exp(-xi)+O_(s_0,r)(1/L).            (2.5)
```

The bounded terms `Q_H-g` are `o(Y_H)`.  Uniformity on a slightly larger
`xi`-disc and Cauchy's formula give the differentiated version of (2.5).

Choose once and for all a compact interval

```text
I=[a,b] subset (exp(-r/4),exp(r/4)).                       (2.6)
```

For every integer `n` satisfying

```text
v_(n,H)=2 pi n/Y_H in I,                                  (2.7)
```

Rouche's theorem applied near `xi=-log v_(n,H)` gives one
solution `xi_(n,H)` of

```text
T_H(s_H+xi/L)=2 pi i n.                                   (2.8)
```

More precisely,

```text
xi_(n,H)=-log v_(n,H)+O_(s_0,r,I)(1/L),                   (2.9)
```

uniformly in `n`.  First take a fixed circle about `-log v` contained in
`|xi|<r/2`; compactness gives a uniform positive boundary lower bound and
therefore a root in a fixed interior neighborhood.  On the smaller circle
`|xi+log v|=C/L`, Taylor's theorem gives
`|exp(-xi)-v| >= c_I C/L`.  Choosing the fixed constant `C` larger than the
implicit constant in (2.5) and applying Rouche again proves (2.9).  This is
the required shrinking-radius slack.  The derivative version of (2.5)
then shows that every selected solution is simple.

The number of admissible lattice values is

```text
#{n:v_(n,H) in I}=(b-a)Y_H/(2 pi)+O(1).                   (2.10)
```

### Theorem 2.1 -- ubiquitous deterministic microcloud

Let `Omega` be a nonempty open set with compact closure in

```text
1/2<Re(s)<1.                                               (2.11)
```

Choose any `s_0 in Omega` at which `zeta` is finite and nonzero.  There are
constants `r,c,C>0` such that, for every sufficiently large `H`, a center
`s_H` with

```text
|s_H-s_0|<=C/log H                                        (2.12)
```

satisfies

```text
N(|s-s_H|<r/log H; E_H(s)=2)
 >=c H^(1-Re(s_0))/log H.                                 (2.13)
```

All the counted points may be taken simple, and the microdisc is contained
in `Omega`.

In particular, there is no sequence `H_j -> infinity` for which `E_(H_j)-2`
is zero-free on any fixed open target set in the strip.

## 3. A microcloud next to a hypothetical zeta zero

Let

```text
rho=beta+i gamma,
1/2<beta<1,                                                (3.1)
```

be a zero of `zeta` of multiplicity `m`.  Write

```text
zeta(s)=(s-rho)^m h(s),
h(rho)!=0.                                                 (3.2)
```

Fix constants `x>2r>0`.  Choose `u_H` in a fixed bounded interval so that

```text
s_H=rho+(x+i u_H)/L,
A_H(s_H)=iY_H,
Y_H asymp_rho H^(1-beta)/L.                               (3.3)
```

The scaled disc `s=s_H+xi/L`, `|xi|<=r`, does not contain `rho`.  On it one
may choose the branch

```text
g(s)=m[Log(x+i u_H+xi)-log L]+Log(h(s)/2).                 (3.4)
```

Consequently

```text
g(s)=O_(rho,x,r)(log L),                                  (3.5)
```

which is still `o(Y_H)`, and (2.5)--(2.10) remain valid.

### Theorem 3.1 -- near-zero skeleton abundance

If `rho` as in (3.1) exists, then there are constants `C,c>0`, depending on
`rho`, such that for every sufficiently large `H`,

```text
N(|s-rho|<C/log H; E_H(s)=2)
 >=c H^(1-beta)/log H.                                    (3.6)
```

The counted points may all be taken simple.

This is important logically.  A retained zeta zero does not create a hole
in the deterministic mixed-point skeleton.  It sits next to an abundant
mixed packet.

## 4. Uniform conditioning

At any selected point `a_(n,H)=s_H+xi_(n,H)/L`, differentiated (2.5) gives

```text
|T_H'(a_(n,H))| asymp L Y_H asymp H^(1-sigma_0),
|T_H''(s)| << L^2 Y_H                                    (4.1)
```

throughout a slightly smaller microdisc.  Moreover, the bound on the first
derivative of the normalized phase implies

```text
|xi_(n,H)-xi_(n',H)| >= c_I |n-n'|/Y_H.                   (4.2)
```

Choose a sufficiently small fixed `eta>0`.  The circles

```text
|s-a_(n,H)|=eta/(L Y_H)                                   (4.3)
```

are then pairwise disjoint.  Taylor's theorem, (4.1), and
`E_H/2=exp(-T_H)` show on each circle that

```text
|E_H(s)-2|>=c_0>0,                                        (4.4)
```

where `c_0` is independent of `H` and `n`.  Equivalently, the physical
circle radius is

```text
1/(L Y_H) asymp H^(-(1-sigma_0)).                         (4.5)
```

Thus these are not nearly multiple, boundary-ill-conditioned zeros.  A
tail approximation with a fixed sufficiently small boundary error would
transfer each selected point separately by Rouche.

## 5. Proportional-order signed moment law

The same asymptotic determines the leading signed reciprocal powers of one
microcloud.  This is stronger than an unsigned count.

Keep the notation of Section 2, let `z_*` be fixed with

```text
D=z_*-s_0 !=0,                                             (5.1)
```

and let `k_H` be integers with

```text
k_H/L -> kappa,  0<=kappa<infinity.                        (5.2)
```

After passage to a subsequence, the bounded numbers `i u_H` converge to a
number `eta`.  Uniformly for the points indexed by (2.7),

```text
(z_*-a_(n,H))^(-k_H-1)
 =D^(-k_H-1)
   exp[kappa(eta-log v_(n,H))/D](1+o(1)).                 (5.3)
```

The lattice spacing in the `v` variable is `2 pi/Y_H`.  Hence the Riemann
sum gives the following exact leading law.

### Theorem 5.1 -- signed microcloud transform

Along every subsequence on which `i u_H -> eta`,

```text
D^(k_H+1)/Y_H
 sum_(v_(n,H) in I) (z_*-a_(n,H))^(-k_H-1)

 -> exp(kappa eta/D)/(2 pi)
    integral_a^b v^(-kappa/D) dv.                         (5.4)
```

For the near-zero cloud, pass to a subsequence on which
`x+i u_H -> eta_rho`; the statement remains valid after replacing `eta` by
`eta_rho` and `s_0` by `rho`.

If `z_*` and `s_0` have the same imaginary part and `z_*` lies to the right,
then `D>0` is real.  The integral in (5.4) is positive and
`|exp(kappa i u_H/D)|=1`.  Therefore

```text
|sum_(v_(n,H) in I) (z_*-a_(n,H))^(-k_H-1)|
 asymp_(I,kappa,D) Y_H D^(-k_H-1).                        (5.5)
```

There is no internal signed cancellation of a same-height microcloud at
any finite proportional order.

### Corridor warning

Take

```text
z_*=1+r+i gamma,
rho=beta+i gamma,
s_sigma=sigma+i gamma,
beta<sigma<1,                                              (5.6)
```

and write

```text
D_beta=1+r-beta,
D_sigma=1+r-sigma.                                        (5.7)
```

The near-`rho` cloud has size `asymp H^(1-beta)/L`; the corridor cloud at
`s_sigma` has size `asymp H^(1-sigma)/L`, but `D_sigma<D_beta`.  Section 2
constructs it when `zeta(s_sigma)!=0`, and Section 3 supplies the same
conclusion if `s_sigma` is itself a zeta zero.  At
`k_H/L -> kappa`, (5.5) makes the ratio of their leading magnitudes

```text
exp{L[-(sigma-beta)
       +kappa log(D_beta/D_sigma)]+o(L)}.                  (5.8)
```

Consequently the corridor packet is exponentially larger whenever

```text
kappa>(sigma-beta)/log(D_beta/D_sigma).                    (5.9)
```

This is a rigorous obstruction to treating the near-target cloud as the
whole mixed divisor.  Global cancellation must couple many Stokes packets.

## 6. Exact positive two-value response

There is an independent exact check on that conclusion.  In `Re(s)>1`,
write

```text
E_H(s)=1+U_H(s).                                           (6.1)
```

The tail `U_H` has nonnegative Dirichlet coefficients and support beyond
`H`.  The two-value logarithmic derivative is

```text
A_(2,H)(s)
 =E_H'(s)/E_H(s)+E_H'(s)/(E_H(s)-2)
 =-2U_H'(s)U_H(s)/[(1+U_H(s))(1-U_H(s))].                 (6.2)
```

In a sufficiently far right half-plane, and in particular in a fixed
right-hand neighborhood once `H` is large, `|U_H|<1`.  Expanding
`(1-U_H^2)^(-1)` there shows that (6.2) has nonnegative Dirichlet
coefficients supported beyond `H^2`.

Its divisor ledger is equally exact:

* a zero of `E_H` of multiplicity `m` has residue `+m`;
* an `E_H=2` point of multiplicity `m` has residue `+m`;
* a pole of `E_H` of order `m` has residue `-2m`.

In particular a hypothetical zeta zero and the nearby selected
`E_H=2` cloud enter with the same sign.  The Euler-small right-hand jets of
(6.2) can only result from nonlocal cancellation involving the corridor
clouds and the negative pole ledger.  It cannot be explained by cancellation
inside the target microcloud.

## 7. Exact spectral-shift subtraction

The natural universal background phase is

```text
T_(0,H)=S_H+Q_H.                                           (7.1)
```

Its lattice `T_(0,H) in 2 pi i Z` is the zero set of `2P_H-2`.  More
generally let `c` be holomorphic and nonvanishing on a domain `D` in the
strip and define

```text
Delta_(c,H)(s)
 =d/ds log[(zeta(s)P_H(s)-2)/(c(s)P_H(s)-2)]

 =(zeta P_H)'/(zeta P_H-2)-(cP_H)'/(cP_H-2).              (7.2)
```

### Theorem 7.1 -- exact signed divisor identity

Let `Gamma` be a positively oriented contour in `D` avoiding the zeros of
both factors, and let `phi` be holomorphic inside `Gamma`.  Then

```text
1/(2 pi i) integral_Gamma phi(s)Delta_(c,H)(s) ds

 =sum_(zeta P_H=2 inside Gamma) mult(a)phi(a)
  -sum_(cP_H=2 inside Gamma) mult(b)phi(b).                (7.3)
```

This is the argument principle applied to the quotient in (7.2).  It is an
exact renormalized `a`-point divisor, not a density heuristic.

There are two sharply different phase limits.  On a compact set on which
`P_H` is exponentially large and `zeta,c` stay bounded away from zero,

```text
Delta_(c,H)=zeta'/zeta-c'/c+o(1).                         (7.4)
```

On a compact set on which `P_H` is exponentially small,

```text
Delta_(c,H)=o(1).                                         (7.5)
```

The derivative claims follow because `P_H'/P_H` grows only polynomially in
`H` on a fixed strip compact, whereas the phase margins in (7.4)--(7.5) are
exponential in `H^(1-sigma)/L`.

For the universal choice `c=2`, equation (7.4) is `zeta'/zeta+o(1)`.  Thus a
zeta zero of multiplicity `m` is an excess of `m` actual sheets relative to
the universal background in the large-`P_H` phase.  In the small-`P_H`
phase the defect disappears.  It must therefore be transported through the
rapidly oscillating transition curves on which `|P_H|` is of order one.

## 8. The defect at a hypothetical zero is real but has the wrong sign

At `rho=beta+i gamma`, Lemma 1.1 gives

```text
log|P_H(rho)|=-Re A_H(rho)+O(|A_H(rho)|/L)+O(1),
|A_H(rho)| asymp H^(1-beta)/L.                            (8.1)
```

The argument of `A_H(rho)` is

```text
-gamma log H-arg(1-rho).                                  (8.2)
```

It winds indefinitely.  There are therefore arbitrarily large cutoff
subsequences on which `|P_H(rho)|` is exponentially large, and others on
which it is exponentially small.

Consider a large-phase subsequence and put `M_H=|P_H(rho)|`.  On the circle

```text
|s-rho|=M_H^(-1/(2m)),                                    (8.3)
```

one has `P_H(s)/P_H(rho)=1+o(1)`, because

```text
|(log P_H)'|<<H^(1-beta)                                  (8.4)
```

there and the radius in (8.3) is exponentially small.  From (3.2),

```text
|zeta(s)P_H(s)| asymp M_H^(1/2) >>2.                      (8.5)
```

Rouche's theorem gives exactly `m` zeros of `zeta P_H-2` inside (8.3).  If
`c` is nonvanishing there, `cP_H-2` has no zero.  More precisely, the actual
points are simple and satisfy

```text
s-rho=omega_j[2/(h(rho)P_H(rho))]^(1/m)(1+o(1)),
omega_j^m=1.                                               (8.6)
```

Thus the local spectral defect is `+m`, not `-m`.  It reinforces the zeta
zero in the positive two-value response.  On a small-phase subsequence, the
same stability argument gives a shrinking neighborhood with no
`E_H=2` point; the defect has moved out to the Stokes corridor.

## 9. Why scalar renormalization does not close the strip argument

There are three exact bills.

### 9.1 The background divisor is negative

Every background point in (7.3) has residue `-1`.  Subtracting the
polynomially large universal cloud therefore destroys the same-sign divisor
which made the two-value response (6.2) useful.  Taking absolute values
restores the full polynomial cloud cost.

### 9.2 Right-cap normalization forces the trivial background

On every open right cap in `Re(s)>1`,

```text
P_H(s) ->1/zeta(s),
zeta(s)P_H(s) ->1.                                        (9.1)
```

If a fixed scalar background `cP_H` is required to have the same limiting
head germ, then `c/zeta=1` on that open cap.  The identity theorem forces

```text
c=zeta,                                                    (9.2)
```

and (7.2) is identically zero.  The universal background `c=2` retains the
cutoff lattice but does not retain the right-cap head normalization.

There is also no free normal-family version of an `H`-dependent workaround.
If nonvanishing `c_H` are normal on the connected bridge and converge to
`zeta` on a right cap, every convergent subsequence has limit `zeta`
throughout.  Hurwitz then contradicts a retained zeta zero.  Such a
background must lose nonvanishing, normality, or the right-cap
approximation, each of which restores a divisor or outer-growth bill.

### 9.3 PNT is much coarser than one sheet

Lemma 1.1 controls the phase only to

```text
T_H(s)=A_H(s)+O(|A_H(s)|/L)+O(log L).                     (9.3)
```

The error `|A_H|/L` tends to infinity throughout every fixed substrip, while
adjacent lattice sheets differ by exactly `2 pi i`.  It is enough for the
bulk count, conditioning, and the Riemann-sum law (5.4), because those are
relative-scale statements.  It is not enough to identify the `O(1)`
residual after subtracting two `asymp |A_H|` sheet families.  A successful
spectral-shift continuation would need a genuinely prime-specific estimate
which controls paired Stokes endpoints or the exact signed transform; a
standard PNT refinement by finitely many endpoint terms does not do this.

Formally, if `g=Log(zeta/c)` and an actual sheet is paired with a background
sheet, its displacement is

```text
delta s =g(s)/T_(c,H)'(s)+lower-order terms.               (9.4)
```

The corresponding signed sheet density is the derivative of this shift and
records the monodromy of `g`, hence the multiplicity `m`.  Turning (9.4)
into a global reciprocal-power estimate requires uniform control through
the Stokes endpoints.  Equations (7.2)--(7.5) are the rigorous version of
the topology; (9.4) alone is not an arithmetic error estimate.

## 10. Consequence for the fixed-strip program

The deterministic alternative left in R158 is now decided:

```text
find a cutoff subsequence with E_H-2 zero-free
on a fixed target neighborhood                                  FALSE. (10.1)
```

The result does **not** prove that zeta has zeros in every fixed right
substrip.  The points constructed here solve `E_H=2`, not `zeta=0`.
Accordingly, it proves neither existence nor nonexistence of a fixed
zero-free strip for zeta.

What remains from this branch is narrower and more concrete.  One must
estimate a global signed spectral shift coupling all cutoff Stokes packets,
or prove a coefficient-specific correlation between the quadratic tail and
the robust circles (4.3).  Local zero avoidance, local positivity, and the
leading PNT phase cannot do it: the microcloud theorem and the corridor law
give explicit countergeometry to each of those simplifications.
