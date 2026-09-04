# Uniform-strip decision tree: consolidation and maximum-information run

**Date:** 2026-08-30  
**Status:** theorem/countermodel audit; no zero-free strip and no proof of RH

## 0. Verdict

This run materially changes the local decision tree, but it does not complete
the prime-QP route.

**Subsequent SR2PF update.**  The broad one-flattening matrix conjecture in
Section 8.4 remains open, but the tensor-labelled version actually produced by
the digit construction has now been proved.  All compatible flattenings place
the cleaned tensor on the second Segre secant variety; both its tangent and
honest-secant branches satisfy

```text
r<<log(Y)/log log(Y),
```

contradicting the required
`r=(.0179+o(1))log(Y)/log log log(Y)`.  See
`ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`.  Accordingly, the finite
tensor gate is closed; what remains upstream is the analytic actual-prime
transport into that tensor alternative.

1. The apparent `0.000655647...` gap between the old short-carrier theorem
   and the localized four-cycle scale `8/33` was artificial.  The old proof
   paid a global fourth-moment range loss after the carrier had already been
   confined to `M<=Y^theta` blocks.  Using the localized frame range raises
   the exclusion threshold from

   ```text
   theta >=.241768595...                              (old)
   ```

   to `.293857142...`.  A calibrated common antipode raises it further to

   ```text
   theta >=(1+c)/3=.339666666...       at c=.019.    (0.1)
   ```

   Therefore the entire complete-support localized-carrier branch at
   `theta=8/33` is closed with room to spare.

2. The proposed next dichotomy, “a separator either localizes or contains a
   long pointwise progression,” is false before actual-prime arithmetic is
   used.  A tensor-Fejer construction below is exactly source-normalized,
   has

   ```text
   h_Y=Y^(-.0179+o(1)),       P_eff=Y^(.0179+o(1)), (0.2)
   ```

   is physically dispersed, and has no `B^-1`-accurate log progression
   longer than `O(log log Y)`.  It is synthetic: its physical nodes are real
   numbers, not primes or even integers.

3. The corrected structural split has three branches:

   ```text
   hereditary localized carrier
        / low-rank pointwise packet
        / dispersed growing-rank autocorrelation.   (0.3)
   ```

   The first branch is killed if it can actually be extracted with its own
   carrier normalization and one-sided floor.  PHR2 kills the second branch
   if a superlogarithmic same-side pointwise log progression is extracted.
   The third branch is genuine in the abstract frame/source class.

4. The highest-information surviving test is now an actual-prime transport
   problem for the tensor construction.  A successful transport would
   produce, after elementary cleaning, a super-polylogarithmic matrix of
   distinct fixed-shell primes having rational rank at most two and lying
   within `O(Y/B)` of a positive rank-one matrix.  A polylogarithmic bound for
   this structured prime matrix kills the explicit high-rank obstruction; a
   construction keeps that obstruction alive.

The exact arithmetic checks in this report are replayed by

```bash
python3 results/verify_zeta23_uniform_strip_decision_tree.py
```

## 1. The authoritative logical tree

The root goal and the presently selected milestone must not be conflated.
A fixed zero-free strip is strictly weaker than RH, and the project does not
currently have a proved fixed-strip-to-RH amplification.  Per the present
research choice, this report studies the fixed-strip milestone.

For the prime-only QP route, the proved conditional chain is

```text
prime-supported DPA_P(.019)
        +
source-conditioned LTRAD_P(.0189,.001)
        |
        v
no directional event of depth Y^-.001
        |
        v
Turan/phase localization
        |
        v
fixed zero-free width 10^-6.                         (1.1)
```

Both displayed inputs remain open.  They are logically independent in the
current formulation:

```text
DPA_P(.019):
  exists y on ordinary primes, sum y=1,
  inf_(t in H_Y) F_y(t)>=-Y^-.019;

LTRAD_P(.0189,.001):
  a long negative source event implies
  r_P(H_Y)>=Y^(-.0189+o(1)).                         (1.2)
```

For a source event, with

```text
v=a_P(t_0)+Dq_P,              D>=Y^(-.001+o(1)),
```

the exact transverse target is

```text
inf_(y:y dot v=-1) sup_(t in H_Y)F_y(t)
       >=Y^(-.0179+o(1)).                            (1.3)
```

The product of `(1.3)` with `D` gives the radial exponent `.0189`.

There is a potentially weaker, not-yet-developed route which should remain
visible in the tree: replace the two universal assertions in `(1.1)` by an
**event-conditioned upper/lower pair** for `r_P`.  It is enough to prove the
DPA-type upper estimate only at centers carrying a bad source event.  The
current universal split may therefore be a genuine over-strengthening, not a
canonical decomposition of the strip problem.

## 2. Where the decision tree went wrong

The errors occurred at different depths.  Ordered from the root downward:

### 2.1 A fixed strip was treated rhetorically as if it finished RH

It does not.  A fixed strip is a substantial milestone and can be pursued on
its own, but another mechanism would still be required to reach the critical
line.

### 2.2 The sharp four-cycle problem was selected too early

The generic moment conversion is far too lossy.  Even the desired weighted
sharp four-cycle endpoint, passed through the existing smooth transverse
argument, gives only

```text
s_v >>Y^(-41/66-o(1)),
```

where `(1.3)` needs `Y^(-.0179+o(1))`.  The four-cycle theorem is important
for the QP upper problem, but it is not a direct dependency of the present
adapter proof.  It can re-enter only through a source-preserving inverse
theorem.

### 2.3 The universal DPA/LTRAD split may be stronger than necessary

The current chain asks for a DPA certificate at every center and an LTRAD
lower bound at every bad event.  A source-conditioned antenna, or a direct
event-exclusion theorem, could use information discarded by that split.

### 2.4 Early B3 formulations omitted the separator hypothesis

Source normalization and a corrector-energy allowance alone do not force a
positive high-band return.  The relevant object must also satisfy the global
separator cap `h_Y(y)<=Y^(-.0179+o(1))`.  This quantifier was corrected in the
preceding B3 audits.

### 2.5 A global range loss was paid on a localized carrier

This is the concrete error responsible for the alleged `.000655647` gap.
Once the vector is supported on `M<=W` blocks, the pointwise frame bound costs
`sqrt(M)`, not the ambient fourth-moment cost `sqrt(Delta)=Y^(8/33)`.
Section 3 repairs this and closes the `8/33` branch.

### 2.6 A lower bound on participation was mistaken for stability

The proved estimate

```text
h_Y(y)>>1/P_eff                                      (2.1)
```

and a separator upper bound give only
`P_eff>>Y^.0179`.  They do not imply constant-factor near equality in
`(2.1)`.  The tensor example below shows that even exponent-level near
equality does not force a one-dimensional Fejer profile.

### 2.7 The localization-or-progression dichotomy omitted growing rank

Rank-two and higher digit-box autocorrelations can be delocalized and
progression-free while saturating `(2.1)` up to `Y^o(1)`.  This is not a
minor exceptional case; it is the sharp abstract obstruction class.

### 2.8 Generic BSG was asked to preserve data it does not preserve

The existing pair-energy/BSG hostile audits show that a generic extraction
can lose coefficient signs, the source vector, the carrier identity, and all
but a small island of the mass.  Merely finding high additive or approximate
multiplicative energy does not feed the localized hard-core theorem.
Moreover, actual primes already have nearly cubic localized additive energy
at the `8/33` scale.

### 2.9 One-dimensional Hankel rigidity was overextended

PHR2 is a branch terminator only after a pointwise same-side near-geometric
sequence is produced.  Arbitrary lower/upper interlacing does not preserve
one global Hankel rank, and finite multivariate rank statements have boundary
and completion issues.  Section 7 records the rigorous partial serialization
that survives.

## 3. The corrected localized-carrier theorem

Fix `1<A<2`, `0<a<1`,

```text
B=Y^A,             H_Y=[Y^a,B],             Y=N+1/2.
```

Let `P` be a collection of distinct **integer** nodes in a fixed
multiplicative shell around `Y`, all contained in one physical interval of
diameter at most

```text
W=Y^theta,                  theta<1/2.
```

Put `M=#P`, `u_n=|log(n/Y)|`, and

```text
F(t)=sum_(n in P)y_n cos(tu_n),       sum_(n in P)y_n=1. (3.1)
```

### Theorem 3.1 -- calibrated localized-carrier exclusion

For arbitrary real signed coefficients in `(3.1)`, if

```text
inf_(t in H_Y)F(t)>=-Y^-c,                         (3.2)
```

then

```text
theta >=(1+c)/3-o(1).                              (3.3)
```

The theorem applies in particular to ordinary primes and to distinct prime
powers.  No parity property of primes is used.

### 3.1 Localized signed range

Restrict the established smooth cluster frame to the blocks meeting `P`.
Let `E` be its block energy and let `rho_B` be the smooth probability in the
interior of `H_Y`.  The frame proof gives

```text
Q:=int F^2 rho_B asyp E,
sup_(0<=t<=B)|F(t)|<<sqrt(M)E^(1/2),
|int F rho_B|<<_K sqrt(M)(Y/B)^K E^(1/2).           (3.4)
```

Choose fixed `K` so that `M(Y/B)^K=o(1)`.  Applying the elementary
positive-range inequality to `-F`, with the mean in `(3.4)` absorbed, gives

```text
-inf_(t in H_Y)F(t)>>E^(1/2)/sqrt(M).               (3.5)
```

This step is unconditional, coefficient-sensitive, and uses neither DPA nor
LTRAD.  The old proof instead used
`Delta^-1/2 E^(1/2)`, where `Delta=Y^(2-A+o(1))`; that was the unnecessary
global loss.

### 3.2 A calibrated common antipode

There is a legal `t_* asyp_w Y` for which, with

```text
delta_n=1+cos(t_*u_n),
```

the restricted block-dual norm satisfies

```text
||delta||_(E*,P)<<sqrt(M) W^2/Y.                   (3.6)
```

There are three cases.

1. If the packet meets both sides of `Y`, or lies within `O(W)` of `Y`, use
   `t_*=2piY`.  Every half-distance `h=|n-Y|` is a half-integer, so `2pi h`
   is an odd multiple of `pi`; the phase error is `O(h^2/Y)` and the cosine
   defect is `O(W^4/Y^2)<<W^2/Y`.

2. For a same-side packet at distance at most `sqrt(Y)`, choose one node
   `n_0`, put `h_0=|n_0-Y|`, `u_0=|log(n_0/Y)|`, and take

   ```text
   t_*=2pi h_0/u_0.                                  (3.7)
   ```

   This makes `n_0` exactly antipodal.  The function
   `|log((Y+/-h)/Y)|/h` has derivative `O_w(Y^-2)`, so every other packet
   node has phase error `O(W/sqrt(Y))` and cosine defect `O(W^2/Y)`.

3. For a same-side packet farther than `sqrt(Y)`, choose the odd integer `m`
   nearest `2n_0u_0` and take

   ```text
   t_*=m pi/u_0.                                     (3.8)
   ```

   Then `t_*u_0` is an odd multiple of `pi`, while for `n=n_0+d`,
   expansion about `n_0` gives, modulo `2pi`, error

   ```text
   O(W/H+W^2/Y)<<W/sqrt(Y).                          (3.9)
   ```

   The baseline is `2pi d`, so only integrality of `d` is used.

For a close reflected block wholly retained by a central packet, the two
half-distances are equal: their difference is an integer but the frame-close
condition makes it `o(1)`.  The reflected defect difference is
`O(h^5/Y^3)`; division by
`min(1,B|u_--u_+|)` remains `O(W^2/Y)`.  A one-side packet meets at most one
endpoint of any reflected pair.  Thus `(3.6)` includes all divided-difference
coordinates.

The three heights above lie between `Y^a` and `B` for large `Y`, including at
the fixed shell endpoints.

### 3.3 Completion of the proof

At the common antipode,

```text
F(t_*)=-1+y dot delta.
```

Assumption `(3.2)` implies `y dot delta>=1-o(1)`.  Dual Cauchy--Schwarz and
`(3.6)` give

```text
E^(1/2)>>Y/[sqrt(M)W^2].                            (3.10)
```

Insert `(3.10)` into `(3.5)` and use `M<=W+1`:

```text
-inf F>>Y/(MW^2)>>Y^(1-3theta-o(1)).                (3.11)
```

Comparison with `(3.2)` proves `(3.3)`.

### 3.4 Exact diagnosis of the old exponent gap

The four available combinations are

| Antipode | Range conversion | Excursion exponent | Forced `theta` |
|---|---|---:|---:|
| old | global fourth moment | `A/2-1/3-11theta/6` | `(3A-2+6c)/11` |
| old | localized frame | `(2-7theta)/3` | `(2+3c)/7` |
| calibrated | global fourth moment | `A/2-5theta/2` | `(A+2c)/5` |
| calibrated | localized frame | `1-3theta` | `(1+c)/3` |

At `A=50/33,c=.019`, the thresholds are respectively

```text
.241768595...,  .293857142...,  .310630303...,
.339666666... .                                      (3.12)
```

The localized four-cycle scale is

```text
theta_quad=(2-A)/2=8/33=.242424242... .             (3.13)
```

At `(3.13)`, the calibrated/localized lower excursion in `(3.11)` is
`Y^(3/11-o(1))`, not a marginal negative power.  Even the old antipode plus
localized range gives `Y^(10/99-o(1))`.  The previous gap was therefore a
bookkeeping/optimization artifact, not a new prime threshold.

### 3.5 Scope boundary

The theorem requires the **complete carrier** to lie in one interval, to
have sum one, and to retain its own one-sided floor.  If an arbitrary global
separator is decomposed into a local part and a correcting tail, none of
these properties automatically passes to the local part.  Closing the
localized carrier is not the same as proving that every separator contains
such a hereditary carrier.

## 4. What source normalization alone really localizes

There is a useful weak statement which fixes the boundary in Section 3.5.
Decompose a separator into frame blocks and write

```text
c_b=<y_b,v_b>,             a_b=(-c_b)_+,
A=sum_b a_b.                                         (4.1)
```

Since `sum c_b=y dot v=-1`, one has `A>=1`.  The source block has uniformly
bounded dual norm, so

```text
|c_b|<<r_b.                                          (4.2)
```

Partition physical space into `W`-cells.  Put

```text
mu_I=A^-1 sum_(b in I)a_b.
```

For every fixed `eta>0`, either

```text
mu_I>=eta for some cell I,
```

in which case Cauchy--Schwarz proves

```text
E_I>>eta^2 A^2/n_I,                                 (4.3)
```

where `n_I` is the number of blocks in the cell, or

```text
sum_I mu_I^2<eta,                                   (4.4)
```

so the source has cell participation greater than `eta^-1`.

This is a genuine localization/dispersion dichotomy, but `(4.3)` does not
give the cell a carrier normalization or a hereditary floor.  It therefore
cannot by itself invoke Theorem 3.1.  This is the exact point at which the
earlier proposed source-preserving inverse theorem asked for too much.

## 5. The dispersed tensor-Fejer countermodel

Fix

```text
c=.0179,
n=2 floor((log log Y)/2),
r=ceil(c log Y/log n),
m=n^r,                       Q=10n.                 (5.1)
```

Let

```text
mathcal A={sum_(j<r)a_jQ^j:0<=a_j<n},
R=(n-1)(Q^r-1)/(Q-1).                               (5.2)
```

Then `m=Y^(c+o(1))` and `R=Y^(c+o(1))`.  Choose

```text
ell=floor(wY/(8pi R)),       omega=2pi ell/Y,
t_0=2pi/omega=Y/ell.                                  (5.3)
```

For each positive `d in mathcal A-mathcal A`, let

```text
nu(d)=#{(a,b) in mathcal A^2:a-b=d},
u_d=omega d,
y_d=-nu(d)/[m(m-1)].                                 (5.4)
```

All frequencies lie in one side of a fixed shell.  Define

```text
K(t)=m^-1 |sum_(a in mathcal A)exp(i omega a t)|^2.
```

Exact expansion gives

```text
F_y(t)=[1-K(t)]/[2(m-1)].                            (5.5)
```

Consequently

```text
F_y(t)<=1/[2(m-1)]             for every real t,
F_y(0)=F_y(t_0)=-1/2.                                (5.6)
```

Taking `D=1` gives the exact source normalization

```text
y dot[a(t_0)+q_0]=-1.                               (5.7)
```

At `t_*=t_0/n`, the first digit geometric sum is zero, so `K(t_*)=0`.
Because `t_*=Y^(c+o(1))` lies in `[Y^.01,B]`, `(5.6)` is attained there:

```text
h_Y(y)=1/[2(m-1)]=Y^(-c+o(1)).                     (5.8)
```

A long synthetic negative source event can be padded on zero-coefficient
half-mesh nodes.  Thus cardinality and a calibrated negative event do not
remove this example.

### 5.1 Exact participation

The base `Q=10n` prevents carries.  With

```text
T_n=sum_(s=-(n-1))^(n-1)(n-|s|)^2=(2n^3+n)/3,
```

one has

```text
S_1=1/2,
E=[T_n^r-m^2]/[2m^2(m-1)^2],
P_eff=m^2(m-1)^2/[2(T_n^r-m^2)]
     =(1/2+o(1))m(3/2)^r
     =Y^(c+o(1)).                                    (5.9)
```

In particular,

```text
h_Y P_eff=(3/2)^r/4+o(1)=Y^o(1).                   (5.10)
```

The example is exponent-near equality in the participation theorem.  It is
not being hidden in an enormous irrelevant coefficient norm.

### 5.2 No localization

Associate the synthetic physical positions

```text
p_d=Y exp(u_d).
```

Adjacent positions are separated by at least

```text
asyp Y omega asyp Y/R=Y^(1-c-o(1)).                 (5.11)
```

Thus every physical interval of width `Y^(8/33-o(1))` contains at most one
active node.  The largest single-node source fraction and energy fraction
are both `Y^(-c+o(1))`.  No fixed fraction of the source or energy localizes.

### 5.3 No long progression

Every `d in mathcal A-mathcal A` has a unique balanced base-`Q` expansion
with digits in `[-(n-1),n-1]`.  If distinct `d_0,...,d_(k-1)` form an
arithmetic progression, base dominance forces every digit sequence to be an
integer arithmetic progression.  At least one digit is nonconstant, hence

```text
k<=2n-1=O(log log Y).                               (5.12)
```

If the `u_d` are within `C/B` of a log progression, second differences are
within `4C/B`.  Since `omega>>B^-1`, the corresponding integer second
difference vanishes, so `(5.12)` also holds for `B^-1`-accurate
progressions.

Finally, perturb each frequency generically by at most `B^-1m^-3` and
rescale the coefficients by `1+o(1)`.  The frequencies can be made
`Q`-linearly independent, while for `t<=B` the polynomial changes by
`o(h_Y)`.  Therefore rational independence of ordinary-prime logs is not the
missing theorem either.

### 5.4 What the example does and does not refute

It satisfies the harmonic frame, source, sign, participation,
delocalization, and progression-free requirements.  It refutes every inverse
statement based only on those data.

It is **not** an actual-prime counterexample.  The `p_d` are real synthetic
positions.  Naive rounding controls their log frequencies only at scale
`O(Y^-1)`, much coarser than `B^-1=Y^(-50/33)`; there is no mechanism making
all rounding errors exceptionally smaller.  Actual-prime finite-aperture
arithmetic is the remaining information.

## 6. Corrected trichotomy

An honest inverse theorem must allow all three outcomes.

### A. Hereditary localized carrier

A component supported in one short physical interval must retain:

- a nontrivial fraction of the source;
- carrier normalization comparable to that source;
- its own one-sided floor, or a uniform theorem preventing cancellation by
  the complement; and
- the actual integer/prime mask.

Theorem 3.1 then kills it below `theta=(1+c)/3`.  None of these hereditary
properties follows from generic BSG.

### B. Source-preserving low-rank packet

If the inverse output contains a pointwise `B^-1`-accurate, same-side log
progression of length greater than `C log Y`, project theorem PHR2 kills it by
integer Hankel collapse, rational recurrence classification, and the
primorial obstruction.

### C. Dispersed growing-rank autocorrelation

The digit-box construction proves this branch exists abstractly at precisely
the target exponent.  Any proof must now use actual-prime placement, not only
energy, participation, rational independence, or one-dimensional APs.

Branches A and B are conditional terminators, not an exhaustive extraction
theorem.  Branch C is the missing third output.

## 7. Two-color Hankel fallback

The full lower/upper-interlaced version of PHR2 remains open.  A rigorous
partial serialization is available.

Suppose distinct shell primes satisfy

```text
||log(p_j/Y)|-(u_0+jh)|<=C/B,             A>3/2,   (7.1)
```

with arbitrary side colors.  Whenever a set of offsets has one repeated
monochromatic color pattern, the matrix of the corresponding primes over the
repeated starts has rational rank at most two.  Indeed the same-side
reference matrix has rank one, and every integer `3 x 3` minor is

```text
O(Y(Y/B)^2)=O(Y^(3-2A))=o(1),                       (7.2)
```

so it vanishes.

Using the two-color van der Waerden number `W(2,3)=9` on disjoint blocks and
pigeonholing the color/offset type gives `>>L` prime triples satisfying one
common primitive relation

```text
a_0p_(t+r)+a_1p_(t+r+d)+a_2p_(t+r+2d)=0,
0<max |a_i|<<Y^2/B=Y^(16/33).                       (7.3)
```

A repeated color word of length `asyp log L`, combined with
Bombieri--Vaaler, supplies many independent common relations of small height
and with exact zeroth and first moments.  At the project exponents one may
take height `Y^.0175`, with at most 27 large-height exceptions.  This is
small-height serialization, not a contradiction with primality.

Two falsifiers prevent a stronger claim.

1. Arbitrary interlacing does not give one global Hankel rank; an exact
   composite six-term two-color model has a nonzero cubic Hankel determinant.
2. Exact rank two and primality are compatible.  For example the matrix

   ```text
   199   409   619
   829  1039  1249
   1459 1669  1879                                  (7.4)
   ```

   has nine distinct prime entries and rank exactly two.

Thus the two-color result is a fallback when a one-dimensional pointwise
packet is extracted.  The clean digital flattening in the next section is
stronger for branch C.

## 8. Maximum-information gate actually selected

> **Historical selection notice.**  Sections 8--9 record the decision made at
> this stage.  The faithful all-cut tensor `SR2PF` gate was subsequently proved
> in its scoped manuscript, so “resolve SR2PF” is no longer a current priority.
> The updated decision tree is
> `ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`.

### 8.1 Weighted actual-prime digit-box transport

Retain the digit parameters in Section 5.  The direct falsifier asks for
same-side ordinary primes `p_s` and digit frequencies `omega_j` such that

```text
sum_s |y_s| |u_(p_s)-sum_j s_j omega_j|
       <=kappa/(mB),                                (8.1)
```

with `kappa` a sufficiently small fixed constant and with the source phase
congruences preserved to the corresponding weighted accuracy.

Equation `(8.1)` is the correct scale: for every `t<=B`,

```text
|Delta F(t)|<=B sum_s |y_s||Delta u_s|<=kappa/m,   (8.2)
```

which is comparable with, and for small `kappa` preserves, the floor in
`(5.8)`.  A successful transport plus a legal long source event would give an
actual-prime countermodel to this B3 mechanism.

### 8.2 Weighted cleaning

Weighted `L1` is not an obvious escape.  Mark nodes with frequency error
larger than `C_0/B` as bad.  Markov applied to `(8.1)` gives bad coefficient
mass `O(1/m)`.  Under the product triangular difference law, choose a random
five-term interval in the central half of each digit coordinate.  Every
vertex marginal is bounded by `C^r` times that law, so a union bound over the
`5^r` vertices has cost

```text
(5C)^r/m=exp[r(log(5C)-log n)]=o(1).                (8.3)
```

After fixing a leading positive digit, there is therefore an all-good,
same-side `5^r` subcube.

### 8.3 Exact tensor flattening

On the clean subcube, exponentiation gives

```text
p_s=Y exp(sum_j s_j omega_j)+O(Y/B).                (8.4)
```

Split the `r` digit coordinates into two nearly equal sets and flatten the
tensor.  The reference matrix in `(8.4)` has rank one.  In every `3 x 3`
determinant, the zero-error term and all one-error terms vanish.  Hence

```text
det=O(Y(Y/B)^2+(Y/B)^3)=O(Y^3/B^2)
   =O(Y^(-1/33)).                                    (8.5)
```

The determinant is an integer and is therefore zero for large `Y`.  The
prime matrix has rational rank at most two.  Both dimensions are

```text
k=5^(r/2)
 =exp[(c log 5/2+o(1)) log Y/log log log Y],         (8.6)
```

which is larger than every fixed power of `log Y` but is `Y^o(1)`.

### 8.4 Structured rank-two prime flattening (`SR2PF`)

The concrete next theorem/falsifier is:

> Let `P=(p_ij)` be a matrix of pairwise-distinct primes in `[c_0Y,C_0Y]`.
> Suppose there are positive real vectors `x_i,z_j` such that
> `|p_ij-x_i z_j|<<Y/B`, and suppose `rank_Q(P)<=2`.  Must
> `min(#rows,#columns)<=(log Y)^C` for some fixed `C`?

The near-rank-one hypothesis is retained because it is present in `(8.4)`;
discarding it makes the problem less faithful and probably much harder.

The outcomes have high information value.

- A polylogarithmic `SR2PF` theorem kills the explicit digit-box realization
  of branch C.
- A super-polylogarithmic construction satisfying the full tensor and
  weighting constraints keeps an actual-prime B3 countermodel credible.
- If exact finite rank does not globalize because of boundary effects, that
  identifies the required completion hypothesis before more inverse theory
  is attempted.

### 8.5 Literature boundary

Multivariate finite-rank Hankel/Prony theory does supply the relevant
annihilating ideals, shift-invariant spaces, and polynomial-exponential
representations once the necessary global or completion hypotheses are in
place; see Tomas Sauer,
[*Hankel and Toeplitz operators of finite rank and Prony's problem in several
variables*](https://arxiv.org/abs/1805.08494), and the general-domain work of
Andersson and Carlsson,
[*On the Structure of Positive Semi-Definite Finite Rank General Domain
Hankel and Toeplitz Operators in Several Variables*](https://link.springer.com/article/10.1007/s11785-016-0596-6).
The latter discussion also emphasizes that a finite low-rank Hankel matrix
need not, without extra hypotheses, have the naive finite exponential-sum
representation.  Consequently an infinite Kronecker theorem cannot simply
be quoted at `(8.5)`.

Rank-two prime matrices are not locally impossible.  Elsholtz constructs
large sets `A,B` of primes for which every `(a+b)/2` is prime, producing
additive rank-two prime grids at logarithmic scales (without asserting all
of the distinctness and tensor conditions in `SR2PF`); see
[*Triples of primes in arithmetic progressions*](https://academic.oup.com/qjmath/article-abstract/53/4/393/1537641).
The fixture `(7.4)` is the smallest warning of the same kind.  The targeted
search found no theorem resolving the super-polylogarithmic, distinct,
near-multiplicative matrix in `(8.4)--(8.6)`.

## 9. Research ordering and stop rules

### Priority 1: resolve `SR2PF` with its tensor labels

The proof program is:

1. formalize the weighted cleaning lemma in Section 8.2;
2. determine the exact finite completion needed to turn all compatible
   flattening minors into commuting two-dimensional shifts;
3. classify the resulting rank-two rational representation while retaining
   the positive near-rank-one geometry;
4. apply projective residue avoidance or a larger-sieve argument to the two
   families of row/column slopes; and
5. stop immediately if an additive or recurrence construction scales beyond
   every polylogarithm while meeting the near-rank-one tolerance.

This is the maximum-information branch because either sign of the result
changes the structural program.

### Priority 2: test the coupled strip gate

In parallel conceptually, replace universal `DPA_P+LTRAD_P` by the weakest
event-conditioned upper/lower contradiction.  If the source event cannot
help construct the upper certificate, the universal split is justified; if
it can, one open theorem is removed from `(1.1)`.

### Priority 3: retain two-color serialization as fallback

If a one-dimensional approximate packet appears but clean same-side runs do
not, use `(7.2)--(7.3)` and the small-height common relations.  Do not treat a
ternary relation or rank two alone as a prime contradiction.

### Routes not to reopen without a new interface

- generic fourth-moment conversion to `(1.3)`;
- generic BSG without source and floor inheritance;
- the claim that localized approximate energy is rare on primes;
- a literal one-dimensional Fejer classification of all near-extremizers;
- fixed-`K` separator searches; or
- the sharp four-cycle theorem as a direct strip dependency.

## 10. Status ledger

```text
fixed zero-free strip:                                      NOT PROVED
RH:                                                         NOT PROVED
fixed strip => RH in the current project:                   NOT AVAILABLE
DPA_P(.019):                                                OPEN
LTRAD_P(.0189,.001):                                        OPEN
mean-absorbed participation h>>1/P_eff:                     PROVED
complete localized integer carrier below (1+c)/3:          EXCLUDED
old .000655647 localized exponent gap:                      ARTIFACT/CLOSED
local source-cell energy/dispersion lemma:                  PROVED
localization-or-long-AP dichotomy from abstract data:       REFUTED
dispersed tensor-Fejer target-scale countermodel:           CONSTRUCTED
actual-prime realization of that countermodel:              OPEN
same-side pointwise superlog packet via PHR2:                EXCLUDED
full two-color PHR2:                                        OPEN
two-color repeated-pattern rank-two serialization:          PROVED
broad one-flattening matrix SR2PF conjecture:                OPEN
faithful all-cut tensor SR2PF gate:                          PROVED/CLOSED
sharp four-cycle bound:                                     OPEN/NOT A DIRECT GATE
```

## 11. Dependencies

This report supersedes the exponent-gap and two-branch recommendation in

- `ZETA23-QP-LTRAD-B3-SPARSE-SEPARATOR-AND-TWO-CLUSTER-CLOSURE-2026-08-30.md`,
- `ZETA23-QP-LTRAD-ACTUAL-PRIME-CLUSTER-HARD-CORE-NOGO-2026-08-28.md`.

It retains the exact logical reductions and PHR2 theorem from

- `ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md`,
- `ZETA23-QP-LTRAD-PRIME-ONLY-AND-REFLECTED-DIFFERENCE-REDUCTION-2026-08-28.md`,
- `ZETA23-PRIME-SHADOW-HANKEL-RIGIDITY-2026-08-29.md`, and
- `ZETA23-FRONTIER-LITERATURE-IMPORT-AND-JOINT-RESEARCH-PROGRAM-2026-08-29.md`.

The report narrows the next task.  It does not convert any conditional arrow
in `(1.1)` into a proof of a strip.

The subsequent finite-gate resolution is recorded in
`ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`.
