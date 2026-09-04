# QP carrier-preserving inverse gate: exact defect rays and the major-arc pullback

**Date:** 2026-08-24  
**Binary verdict:** a genuinely mask-preserving coherent-ray extraction is
proved, but the requested inverse theorem is not.

For the exactly bi-centered carrier--colour operator, any spectral excess
above `sqrt(D)` forces a power correlation on one fixed **actual physical**
defect ray

```text
h=a*c-a'*c'=(rho-rho')/(8*b),              |h|<<D.       (0.1)
```

No box completion, translation of the product window, or loss of the common
carrier occurs.  Quantitatively, a singular value

```text
sigma>=sqrt(D)*D^epsilon                                (0.2)
```

forces one ray quadratic of size `D^(2epsilon-o(1))`, after the already
controlled diagonal and permutation sector is removed.

The first unproved step is now exact: a large fixed-`h` ray is a selected
shifted-semiprime/reciprocal graph.  Current affine/Hankel theorems control
three or more incidences on one short physical line, but a fixed ray can
spread over `q/sqrt(D)>>D` carrier cells.  No theorem converts its small
power numerical-radius excess into a rich affine packet.

The circle-method proposal does not evade this step.  The determinant phase
is Fourier self-dual on `M_2(Z/rZ)`, so a rational major arc pulls back to a
Ramanujan-weighted combination of the same physical defect rays.  Although
its denominator `r<=sqrt(D)=q^(8/33)` is below the numerical
Bombieri--Vinogradov level, the remaining prime variable is sampled in
moving reciprocal intervals of length `D/q<1`, with arbitrary colour
weights and a common carrier.  BV/Vaughan therefore lands on the existing
selected-shell two-inverse/BDH problem rather than a long prime progression.

No faithful asymptotic prime-power countermodel with a `D^epsilon` excess was
found.  Thus the carrier-preserving inverse theorem and the sharp four-cycle
bound remain open.

---

## 1. Exact centered physical operator

Put

```text
Q=q^3,       rho(a,b,c)=8*a*b*c-Q,       |rho|<=H,
H<<q*D.                                                   (1.1)
```

Let `E` be any retained family of actual prime-power triples in this window,
with weights `kappa_e`, `|kappa_e|<=1`.  The physical truncation is
pair-unique, so

```text
T_(b,c)=sum_a kappa(a,b,c)                               (1.2)
```

has at most one summand in every cell.  Let `P_B,P_C` be orthogonal
projections off the constant vectors on the carrier and colour shells, and
define the exact bi-centered operator

```text
T_0=P_B*T*P_C.                                           (1.3)
```

This is stronger and cleaner than subtracting one approximate scalar
multiple of the all-ones matrix.  A right singular vector of `T_0` may be
taken with

```text
P_C z=z,             ||z||_2=1.                          (1.4)
```

For such `z`, orthogonal projection gives

```text
||T_0 z||_2^2
 =||Tz||_2^2-|B|^(-1)*|<1,Tz>|^2
 <=||Tz||_2^2.                                           (1.5)
```

Thus opening the last norm retains only actual edges; centering introduces
one negative rank-one term and cannot create a false positive incidence.

There is one bookkeeping qualification.  The existing rich-cell tangent
peel assigns **pair incidences**, not necessarily original `T` edges.  Its
regular remainder is consequently a masked Gram kernel and need not factor
as `T_reg^* T_reg`.  The identities below remain valid after inserting any
symmetric pair-incidence mask, but one must not silently replace that mask
by deletion of an arbitrary edge set.

## 2. Exact defect-ray decomposition

For an ordered pair of distinct actual edges sharing `b`, write

```text
e =(a ,b,c ),          e'=(a',b,c'),
h(e,e')=a*c-a'*c'.                                      (2.1)
```

The residuals satisfy the exact carrier-preserving identity

```text
rho(e)-rho(e')=8*b*h(e,e').                            (2.2)
```

In particular,

```text
|h|<=H/(4*b_min)<<D.                                   (2.3)
```

For a colour vector `z`, define the oriented ray quadratic

```text
K_h[z]
 =sum_(e,e' share b; e!=e'; h(e,e')=h)
    kappa_e*conjugate(kappa_e')
    *z_c*conjugate(z_c').                              (2.4)
```

Then

```text
K_(-h)[z]=conjugate(K_h[z]).                           (2.5)
```

If

```text
d_c=sum_(e has colour c)|kappa_e|^2,                  (2.6)
```

direct expansion proves the exact Gram identity

```text
||Tz||_2^2
 =sum_c d_c*|z_c|^2+sum_h K_h[z].                     (2.7)
```

This is the desired mask-sensitive replacement for coefficient-blind BSG.
Every term in (2.4) has one common actual carrier and both original product
windows.  Fixed `(c,c',h)` determines `(a,a')` up to `O(1)`: all solutions
of `ca-c'a'=h` differ by `(c',c)`, which cannot fit twice inside the project
shell.  The first product window then determines `b`.  Hence every fixed ray
is a genuine `0/1` selected shifted-factorization graph, not a completed
box.

The `h=0` ray is precisely the equality/permutation branch.  In the
all-five-distinct sector multiplicative Sidonicity eliminates it; in the
full form it belongs to the already controlled repeated/permutation sector.

## 3. Quantitative excess-to-ray theorem

### Theorem 3.1 (physical coherent defect ray)

Let

```text
Delta=max_c d_c,       Z_0=|K_0[z]|,
H_*=floor(H/(4*b_min)).                               (3.1)
```

For every `z` satisfying (1.4), if

```text
||T_0z||_2^2=sigma^2,                                (3.2)
```

then some integer `1<=h<=H_*` obeys

```text
2*Re K_h[z]
 >=(sigma^2-Delta-Z_0)/H_*.                          (3.3)
```

The right side is interpreted as zero when its numerator is negative.

**Proof.**  Equations (1.5) and (2.7) give

```text
sum_(h>0) 2*Re K_h[z]
 >=sigma^2-sum_c d_c|z_c|^2-K_0[z]
 >=sigma^2-Delta-Z_0.                                (3.4)
```

There are at most `H_*` positive defect values by (2.3).  Pigeonholing
(3.4) proves (3.3).  `square`

At the balanced scale, `Delta+Z_0<<Dq^o(1)` after the certified elementary
sectors are removed and `H_*<<D`.  Therefore a genuine squared-norm excess

```text
sigma^2>=D^(1+2epsilon)                              (3.5)
```

forces

```text
2*Re K_h[z]>=D^(2epsilon-o(1)).                      (3.6)
```

Conversely, the uniform regular-ray estimate

```text
sup_(||z||=1)|K_h[z]|<<q^o(1)                       (FR_h)
```

for every nonzero `|h|<<D` would imply

```text
||T_0||_(2->2)^2<<Dq^o(1),                          (3.7)
```

and hence the sharp `sqrt(D)` selected-shell bound.  Thus `(FR_h)` is an
exact, carrier-preserving sufficient theorem.  It is substantially stronger
than fixed-tuple uniqueness.

## 4. Why the fixed ray is not yet an affine/Hankel packet

Writing (2.4) without operator notation exposes the remaining arithmetic:

```text
a*c-a'*c'=h,
|8*a*b*c-Q|<=H,
|8*a'*b*c'-Q|<=H,                                   (4.1)
```

with all five variables in the actual prime-power shell.  For fixed
`(c,c',h)` there is at most one wedge, but for fixed `c,h` the possible
shifted semiprimes `a*c-h=a'*c'` form a moving reciprocal graph.  The common
carrier is then the isolated rounded value near `Q/(8ac)`.

The current local theorem says that three common incidences for one ordered
row pair inside a carrier interval of length `O(sqrt(D))` lie on an exact
simultaneous affine/tangent packet.  After those cells are peeled, it leaves
at most two incidences per such cell.  This does not bound `(FR_h)` because

```text
# carrier cells ~q/sqrt(D)=D^(25/16+o(1))>>D.          (4.2)
```

A fixed ray can therefore place every one of its allowed incidences in a
different cell.  Large numerical radius at the very small threshold
`D^(2epsilon)` does not, by graph theory alone, force three incidences in one
cell: high-girth regular components and fresh-label stars are the exact
abstract obstruction.  Promoting (3.6) to a physical packet requires a new
cross-cell theorem for (4.1).

There is a useful literal finite warning.  At `q=50021`, the all-eight-
distinct prime rectangle

```text
(a1,a2)=(21277,22741),       (b1,b2)=(28277,28793),

        [26003 25537]
(cij)= [24329 23893]                                    (4.3)
```

has all four residuals inside a fixed `O(qD)` product window.  Opening it by
common carrier gives the two nonzero defect magnitudes

```text
a1*c11-a2*c21=42,          a1*c12-a2*c22=36.          (4.4)
```

Every carrier line has only two retained edges, so the three-point packet
test is empty.  On this four-edge subfamily the mean-zero vector
`(1,-1,1,-1)/2` has centered energy `2`, diagonal energy `1`, and the extra
unit is split equally between the `36` and `42` ray pairs.  This is a
faithful actual-mask constant-factor example showing that “any excess at
all implies one tangent packet” is false.  It is not a `D^epsilon`
asymptotic countermodel and does not isolate the same subfamily from all
other edges of the global operator.

## 5. Circle major arcs pull back to the same determinant rays

Let `r>=2` and `(s,r)=1`.  The finite Fourier transform on `M_2(Z/rZ)` is
exactly

```text
sum_(x,y,x',y' mod r)
 e_r(s*(x*y-x'*y')+u*x+v*y+u'*x'+v'*y')

 =r^2*e_r(s_bar*(u'*v'-u*v)).                       (5.1)
```

This is just the complete bilinear Gauss identity applied twice.  It says
that the determinant phase is Fourier self-dual.  Consequently a rational
circle mode

```text
e_r(s*Delta)                                         (5.2)
```

does not become a one-variable progression after inverse Poisson.  It
becomes another determinant mode, with inverse numerator, on the physical
fan variables.  After summing primitive numerators, it weights the physical
defects by

```text
c_r(h)=sum_(s mod r)^* e_r(s*h).                     (5.3)
```

Thus the entire denominator-`r` major contribution is a signed combination

```text
sum_(|h|<<D)c_r(h)*K_h[z],                           (5.4)
```

up to the already audited fan units and smooth scalar weights.  Formula
(5.4) retains the common carrier, but it does not select a positive affine
packet.

This also explains the finite-rank audit.  Taking all reduced rationals with
`r<=sqrt(D)` supplies `asymp D` determinant modes, enough effective rank to
span a length-`D` shift window.  Such a data-dependent major-arc/Eisenstein
continuum is not refuted.  Subtracting it is useful only if its physical
pullback (5.4) can itself be bounded.

## 6. Exact failure of the naive BV/Vaughan closure

The denominator range looks favorable numerically:

```text
r<=sqrt(D)=q^(8/33)<q^(1/2).                         (6.1)
```

Nevertheless ordinary Bombieri--Vinogradov does not estimate (5.4).

1. **The modulus couples two products.**  The physical condition is
   `a*c-a'*c' (mod r)`, not one prime in a fixed residue class.  Its
   coefficient also contains arbitrary `z_c conjugate(z_c')`.
2. **The product window leaves no long prime interval.**  Once `(b,c)` is
   fixed, the allowed interval for `a` has length

   ```text
   H/(b*c)<<D/q<1.                                    (6.2)
   ```

   Reordering the variables replaces it by isolated reciprocal samples
   `round(Q/(8bc))`; it does not create a length-`q` progression to which
   BV applies.
3. **Summing the carrier recreates the selected-modulus problem.**  Vaughan
   decomposition of the prime indicator on the samples in (6.2) produces
   the two coupled inverse phases already isolated in the BDH report.
   The common `b` fibre prevents scalar large-sieve diagonalization.
4. **The coefficients are adversarial.**  BV controls the unweighted prime
   discrepancy averaged over moduli.  Uniformity for every colour vector
   asks for an `ell^2` operator theorem; Cauchy and the ordinary large sieve
   return the existing `D^(1/8)` loss.
5. **Moving fan factors are secondary, not a cure.**  Character--Mellin
   diagonalization can remove their scalar dependence without a power loss,
   but it leaves (5.4) and the subunit sampling (6.2) intact.  Combining the
   circle denominator naively with the top DFI modulus can instead create a
   joint conductor as large as `q`.

Hence a BV/Vaughan proof would need a new theorem for primes along the
moving reciprocal samples with the determinant weight (5.3).  That theorem
is another formulation of `(FR_h)`/selected-shell BDH, not a consequence of
classical BV.

The corresponding minor-arc claim

```text
integral_minor |sum_(u,v)p_u q_v e(theta*u*v)|^4 dtheta
 <<D^o(1)*||p||_2^4*||q||_2^4                         (6.3)
```

after deleting every rational arc of denominator at most `sqrt(D)` is
plausible and has the correct normalization, but no coefficient-uniform
proof of (6.3) is present in the project.  Even granting (6.3), the full
major term (5.4) is the unresolved part.

## 7. The `M_2` pretrace interpretation

Identity (5.1) confirms that an `M_2` theta/pretrace or Motohashi
regularization is more natural than forcing `Delta` into one short Hecke
polynomial.  Rank-zero and rank-one matrix orbits are the circle/polar
channels, while invertible matrices form the regular spectrum.

This is a reformulation, not yet a bound.  The QP coefficient is not an
invariant Schwartz function on `M_2`: it contains four separate actual-prime
shell masks, the selected product window, arbitrary colour weights, and the
external common-carrier fibre.  A pretrace theorem strong enough to preserve
those data and bound the regular orbit at tensor scale is precisely the
mask-sensitive two-index square function isolated in the companion report.

## 8. Status

```text
exact bi-centered physical operator:                 DEFINED;
common-carrier defect identity (2.2):                PROVED;
exact Gram decomposition into K_h:                   PROVED;
D^epsilon spectral excess => D^(2epsilon) ray:       PROVED;
fixed-(c,c',h) wedge uniqueness:                     PROVED;
uniform regular fixed-ray bound (FR_h):               OPEN;
large fixed ray => actual affine/Hankel packet:       OPEN;
constant-factor actual broad warning (4.3):          EXPLICIT;
faithful asymptotic D^epsilon prime countermodel:     NOT FOUND;
determinant Fourier self-duality:                     PROVED;
major arcs pull back to Ramanujan-weighted K_h:       PROVED IN FINITE CORE;
ordinary BV controls that pullback:                  NO;
coefficient-uniform minor-arc tensor bound (6.3):     OPEN;
M_2 pretrace supplies mask-sensitive norm:            OPEN;
sharp uniform four-cycle theorem:                    NOT PROVED.
```

Exact finite replay is in

```text
src/qp_carrier_defect_ray_inverse.py
src/test_qp_carrier_defect_ray_inverse.py
```

The tests verify the literal all-prime product window, pair uniqueness,
the `36/42` physical rays, exact centered Gram reconstruction, determinant
Fourier self-duality, and Ramanujan grouping of the same rays.
