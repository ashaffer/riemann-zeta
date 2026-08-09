# R116 Vieta-product energy attack

Status: exact multiplicative-Fourier diagonalization and a substantial
fail-fast reduction of R115 Target 8.1.  At the critical scale
`r asymp H^2`, all honest integer collisions, the `Q=0` slice, the singular
genus-one locus `Q^2=16P`, the two principal-character axes, and the unique
homogeneous character line have the ideal collision size `H^(4+epsilon)`.
The only spectral estimate not supplied here is a fourth moment of genuinely
two-nonprincipal, nonhomogeneous incomplete Jacobi sums.  Exact enumeration
finds no `H^5` structured counterexample, but this is evidence and not a
proof.

Consequently this report neither proves a fixed zero-free strip nor proves
that one cannot exist.  It replaces the undifferentiated genus-one endpoint
in R115 by one precise fourth-moment theorem and proves that all evident
degeneracies are harmless for the native flat profiles.

Date: 2026-08-07.

Predecessors and companions:

* [`R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md`](R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md),
  especially Target 8.1;
* [`R112-CENTRAL-MATRIX-CORRECTION-BOUND.md`](R112-CENTRAL-MATRIX-CORRECTION-BOUND.md),
  for native-profile flatness; and
* [`R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md`](R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md),
  for the additional endpoint phase which must ultimately be retained.

## 1. Verdict and the exact remaining theorem

Let `r` be prime, let `r asymp H^2`, and assume the integer intervals under
consideration have length `O(H)` and inject into `F_r`.  Write

```text
(a,b,c,d)=(h_1,h_2,h_3,h_4),
P=abcd,
Q=(a+c)(b+d).                                      (1.1)
```

After the coordinate axes `P=0` are separated as in R115, define

```text
J_13(chi,psi)
 =sum_(a,c: ac(a+c)!=0)
     w_1(a)w_3(c) chi(ac)psi(a+c),                 (1.2)

J_24(chi,psi)
 =sum_(b,d: bd(b+d)!=0)
     w_2(b)w_4(d) chi(bd)psi(b+d),                 (1.3)
```

where the `w_i` are bounded by one and supported on `O(1)` intervals of
total length `O(H)`.  The exact coefficient energy is

```text
E_(P,Q)^(P Q!=0)
 =1/(r-1)^2 sum_(chi,psi)
      |J_13(chi,psi)J_24(chi,psi)|^2.              (1.4)
```

The forced spectral sets

```text
chi=1,             psi=1,             psi=chi^(-2) (1.5)
```

contribute only `H^(4+epsilon)` to (1.4).  Thus the clean sufficient target
left by this attack is

```text
sum_(chi,psi generic)
 |J_13(chi,psi)|^2 |J_24(chi,psi)|^2
 << r^2 H^(5-delta+epsilon)                         (1.6)
```

for some fixed `delta>0`, where “generic” means the complement of (1.5).
The conjecturally natural right side is `r^2 H^(4+epsilon)`.

Equation (1.6) is a large-values/fourth-moment problem.  It is not the
pointwise nonlinear Burgess estimate rejected in R115.  A pointwise route
combined with the exact second moment would need roughly

```text
|J_ij(chi,psi)| << H^(3/2-delta)                    (1.7)
```

throughout the generic set.  Available double-character estimates do not
give (1.7) at `H=sqrt(r)`, and pointwise control is stronger than the moment
actually needed.

## 2. Flat native profiles reduce the problem to collision counting

For a coefficient set `Omega subset F_r^2`, put

```text
C_z(P,Q)=sum_(h: (P(h),Q(h))=(P,Q)) product_i z_i(h_i),
E_Omega(z)=sum_((P,Q) in Omega)|C_z(P,Q)|^2.         (2.1)
```

Let `N_Omega` be the same energy with all four weights replaced by indicator
functions of their supports.  On expanding the square and taking absolute
values,

```text
E_Omega(z)<=N_Omega product_i ||z_i||_infinity^2.   (2.2)
```

R112 proves for the actual Blomer--Pascadi profiles

```text
||z_i||_infinity
 <<H^(-1/2+o(1))||z_i||_2.                          (2.3)
```

It follows that

```text
N_Omega<<H^(4+epsilon)
  implies E_Omega(z_actual)
          <<H^epsilon product_i||z_i||_2^2,         (2.4)

N_Omega<<H^(5-delta+epsilon)
  implies E_Omega(z_actual)
          <<H^(1-delta+epsilon)product_i||z_i||_2^2.(2.5)
```

Thus `H^4` is the ideal collision scale and `H^5` is exactly the endpoint
which R115 must beat.

## 3. Exact Vieta convolution and incomplete Jacobi transform

On `G=(F_r^*)^2`, define the two opposite-pair distributions

```text
A_13(u,x)=sum_(ac=u, a+c=x)w_1(a)w_3(c),
A_24(v,y)=sum_(bd=v, b+d=y)w_2(b)w_4(d).            (3.1)
```

The sums in (3.1) have `u,x,v,y!=0`.  Coordinatewise multiplication in
`G` gives the following exact identity.

**Theorem 3.1 (Vieta-product Plancherel identity).**  If

```text
C(P,Q)=sum_(uv=P,xy=Q)A_13(u,x)A_24(v,y),           (3.2)
```

then

```text
C=A_13 *_times A_24,

sum_(P,Q in F_r^*)|C(P,Q)|^2
 =1/(r-1)^2 sum_(chi,psi)
    |J_13(chi,psi)J_24(chi,psi)|^2.                (3.3)
```

If the two opposite-pair profiles agree, the right side is

```text
1/(r-1)^2 sum_(chi,psi)|J(chi,psi)|^4.              (3.4)
```

**Proof.**  Since `(P,Q)=(uv,xy)`, (3.2) is precisely group convolution.
The multiplicative Fourier transform of `A_13` is

```text
sum_(u,x)A_13(u,x)chi(u)psi(x)=J_13(chi,psi),       (3.5)
```

and similarly for `A_24`.  Fourier transform converts convolution to a
product, and Plancherel on the group of order `(r-1)^2` gives (3.3).
QED.

There is a useful automorphism behind (3.3).  For `x!=0`, put

```text
kappa=u/x^2.                                        (3.6)
```

The map `(u,x)|->(kappa,x)` is an automorphism of `G`, and for a Vieta pair

```text
kappa(a,c)=ac/(a+c)^2.                              (3.7)
```

It is invariant under common scaling and under `a<->c`.  This explains both
the Vieta involution and the exceptional character line `psi=chi^(-2)`.

### 3.1. Full-field cancellation is supported on one line

If the short intervals in (1.2) are replaced by all of `F_r`, set
`x=a+c` and `t=a/x`.  Then

```text
a=xt,              c=x(1-t),

J_full(chi,psi)
 =[sum_(x!=0)(chi^2 psi)(x)]
   [sum_(t!=0,1)chi(t(1-t))].                       (3.8)
```

Consequently

```text
J_full(chi,psi)=0 unless psi=chi^(-2).              (3.9)
```

The generic incomplete sums are therefore entirely a failure of scaling
completion at the boundary of the square-root box.  This is a useful
structural fact, but completing each interval separately loses too much to
prove (1.6).

## 4. Imported interval-product lemma

The only external estimate used in the positive results below is the
fourth-moment theorem of Ayyad--Cochrane--Zheng for multiplicative
characters on intervals.

**Lemma 4.1 (weighted ACZ consequence).**  Let `I` be an interval, or a
union of `O(1)` intervals, of total length `O(H)`, and let `|rho(n)|<=1`.
Then

```text
sum_(chi mod r)|sum_(n in I)rho(n)chi(n)|^4
 <<(H^4+rH^2)r^epsilon.                             (4.1)
```

At `r asymp H^2`, the right side is `H^(4+epsilon)`.  If `I,J` are two such
interval sets, then

```text
# {(a,a',c,c') in I^2 times J^2:
       ac'=a'c mod r}
 <<H^(2+epsilon).                                   (4.2)
```

**Proof.**  For unit weights, (4.1) is character orthogonality combined
with the ACZ count for `n_1n_2=n_3n_4 mod r`.  For bounded complex weights,
expand the fourth power after summing over characters and bound the weight
of every surviving congruence by one.  A union of a bounded number of
intervals follows from the fourth-power triangle inequality.  Formula
(4.2) follows from character orthogonality and Cauchy--Schwarz applied to
two instances of (4.1).  QED.

Reference: A. Ayyad, T. Cochrane, and Z. Zheng,
[*The congruence x1x2 congruent to x3x4 (mod p), the equation x1x2 = x3x4,
and mean values of character sums*](https://doi.org/10.1006/jnth.1996.0105),
J. Number Theory 59 (1996), 398--413.

## 5. Honest collisions are already ideal

The first theorem locates exactly where a modular counterexample would have
to live.

**Theorem 5.1 (exact-product collisions).**  Suppose all variables are
nonzero integers of size `O(H)`.  Count pairs of quadruples for which

```text
abcd=a'b'c'd'                         over Z,
(a+c)(b+d)=(a'+c')(b'+d')             over Z,       (5.1)
```

and the common second quantity is nonzero.  Their number is
`O(H^(4+epsilon))`.  The same conclusion holds if the second equality in
(5.1) is only modulo `r`, provided its common residue is nonzero.

**Proof.**  Fix the first quadruple and write

```text
x=a+c,       y=b+d,       u=ac,       v=bd.         (5.2)
```

For the second quadruple, `x'y'` is fixed.  In the modular version it has
only `O(1)` possible integer values because `|x'y'|=O(H^2)` and
`r asymp H^2`.  The divisor bound gives `H^epsilon` choices for `(x',y')`.
Likewise the exact product identity says

```text
u'v'=uv,                                             (5.3)
```

so there are `H^epsilon` choices for `(u',v')`.  For each choice, the roots
of

```text
T^2-x'T+u'=0,
T^2-y'T+v'=0                                        (5.4)
```

determine `(a',c')` and `(b',d')`, with at most two orderings each.  There
are `O(H^4)` first quadruples.  Absorb both divisor factors into
`H^epsilon`.  QED.

Thus any collision excess beyond `H^(4+epsilon)` with `P,Q!=0` must contain
a genuine product alias

```text
abcd-a'b'c'd'=n r,                 n!=0,             (5.5)
```

where `|n|=O(H^2)`.  Aliasing in `Q` alone is harmless.

## 6. The two geometric exceptional strata are ideal

### 6.1. The `Q=0`, `P!=0` slice

Because `2H<r`, the congruence `Q=0` means

```text
a+c=0                  or                  b+d=0.    (6.1)
```

**Theorem 6.1.**  The collision count on `Q=0,P!=0` is

```text
N_(Q=0,P!=0)<<H^(4+epsilon).                         (6.2)
```

**Proof.**  On `a+c=0`, one has `P=-a^2bd`.  By multiplicative-character
orthogonality, the collision count for this slice is

```text
1/(r-1) sum_chi
 |sum_a chi^2(a)|^2
 |sum_b chi(b)|^2
 |sum_d chi(d)|^2.                                  (6.3)
```

The first factor is at most `H^2`.  Hölder and Lemma 4.1 bound the product
of the remaining fourth moments by `H^(4+epsilon)`.  Division by
`r-1 asymp H^2` proves (6.2) for this slice.  The other slice is identical.
Their intersection has `P=a^2b^2`; Lemma 4.1, allowing the two signs after
taking square roots, gives `O(H^(2+epsilon))` collisions.  Finally use the
square triangle inequality for the union in (6.1).  The same proof works
with bounded weights.  QED.

This removes a piece which R115's nonzero-`P` endpoint bound still included.

### 6.2. The singular elliptic parameter

For fixed nonzero `x=a+c` and `y=b+d`, the bidegree `(2,2)` curve

```text
a(x-a)b(y-b)=P                                      (6.4)
```

is singular only when `16P=x^2y^2`, equivalently `Q^2=16P`.

**Theorem 6.2.**  On `P Q!=0` and `Q^2=16P`,

```text
total number of tuples              <<H^3,
maximum size of one (P,Q)-fiber     <<H^(1+epsilon),
collision count                     <<H^(4+epsilon). (6.5)
```

**Proof.**  Fix `a,b,c`.  Since `a+c!=0`, the singular equation is a
nonzero quadratic in `d`, hence has at most two residue roots and at most
two representatives in its interval.  This proves the first assertion.

For a fixed `(P,Q)`, the integer product `xy` has only `O(1)` lifts of the
residue `Q` in its natural `O(H^2)` range.  Each nonzero lift has
`H^epsilon` factorizations `(x,y)`.  For a fixed factorization and a fixed
`a`, the equation

```text
16a(x-a)b(y-b)=x^2y^2                               (6.6)
```

is a nonzero quadratic in `b`, hence has at most two roots.  This proves
the maximum-fiber bound.  Summing the square of each fiber is at most the
maximum fiber times the total mass, giving the last assertion.  QED.

By (2.4), both Theorems 6.1 and 6.2 contribute only
`H^epsilon product_i||z_i||_2^2` for the actual profiles.

These are physical coefficient-space estimates.  They should not be
confused with deleting character lines in (3.3): Fourier transform does
not preserve the singular coefficient subset.

## 7. All forced spectral lines are ideal

In this section `|w_i|<=1`.  Boundary exclusions such as `a+c=0` are kept,
rather than silently absorbed.

### 7.1. The line `psi=1`

Put

```text
A_i(chi)=sum_h w_i(h)chi(h).                         (7.1)
```

The exact formula is

```text
J_13(chi,1)=A_1(chi)A_3(chi)-D_13(chi),
D_13(chi)=sum_a w_1(a)w_3(-a)chi(-a^2).             (7.2)
```

Lemma 4.1 and `|A_i|<=H` give

```text
sum_chi |A_1(chi)A_3(chi)|^4
 <<rH^(6+epsilon).                                  (7.3)
```

The map `chi|->chi^2` has multiplicity at most two, so Lemma 4.1 also
controls the fourth moment of `D_13`; it is smaller than (7.3).  Therefore

```text
sum_chi |J_13(chi,1)|^4<<rH^(6+epsilon).             (7.4)
```

The same holds for `J_24`, and Cauchy--Schwarz gives

```text
1/(r-1)^2 sum_chi
 |J_13(chi,1)J_24(chi,1)|^2
 <<H^(4+epsilon).                                   (7.5)
```

### 7.2. The line `chi=1`

Let

```text
R_13(x)=sum_(a+c=x)w_1(a)w_3(c).                    (7.6)
```

It is supported on `O(1)` intervals of total length `O(H)` and satisfies
`|R_13(x)|<=H`.  Applying Lemma 4.1 to `R_13/H` gives

```text
sum_psi |J_13(1,psi)|^4<<rH^(6+epsilon).             (7.7)
```

The `24` pair and Cauchy--Schwarz again give a normalized contribution
`O(H^(4+epsilon))`.

### 7.3. The homogeneous line `psi=chi^(-2)`

This is the only character line invariant under the common scaling
`(a,c)|->(ta,tc)`, since the summand scales by `(chi^2 psi)(t)`.
On this line,

```text
J_13(chi,chi^(-2))
 =sum_(a,c)w_1(a)w_3(c)
    chi(ac/(a+c)^2).                                (7.8)
```

Put

```text
R(t)=sum_(a/c=t)w_1(a)w_3(c),
F(t)=t/(1+t)^2,
W(s)=sum_(F(t)=s)R(t).                              (7.9)
```

Lemma 4.1 gives

```text
||R||_2^2<<H^(2+epsilon).                           (7.10)
```

Every fiber of `F` has size at most two, so

```text
||W||_2^2<<H^(2+epsilon),          ||W||_1<=H^2.    (7.11)
```

Now `J_13(chi,chi^(-2))=sum_s W(s)chi(s)`.  Orthogonality and Young's
convolution inequality give

```text
sum_chi |J_13(chi,chi^(-2))|^4
 =(r-1)||W *_times W||_2^2
 <=(r-1)||W||_1^2||W||_2^2
 <<rH^(6+epsilon).                                  (7.12)
```

Cauchy--Schwarz between the two opposite pairs shows that this line also
contributes only `H^(4+epsilon)` to (3.3).

Combining (7.5), (7.7), and (7.12) proves the spectral assertion in
Section 1.  In particular, neither principal characters nor the Vieta
scaling symmetry explains the endpoint `H` loss.

## 8. What standard tools do and do not give

The generic part of (1.6) has both characters nonprincipal and
`chi^2 psi!=1`.

### 8.1. Gauss expansion: exact formula and exact loss

There is a natural attempt to combine additive and multiplicative
Parseval.  For nonprincipal `psi`, set

```text
A_chi(t)=sum_a w_1(a)chi(a)e_r(ta),
C_chi(t)=sum_c w_3(c)chi(c)e_r(tc),
B_chi(t)=A_chi(t)C_chi(t).                          (8.1)
```

Gauss inversion gives, up to a scalar of absolute value one,

```text
J_13(chi,psi)
 =r^(-1/2)sum_(t!=0)bar(psi)(t)B_chi(t).            (8.2)
```

This identity is exact.  If

```text
E_times(B)=sum_(t_1t_2=t_3t_4)
 B(t_1)B(t_2)bar(B(t_3)B(t_4)),                     (8.3)
```

then multiplicative Parseval gives the equally exact formula

```text
sum_(psi!=1)|J_13(chi,psi)|^4
 ={(r-1)E_times(B_chi)-|sum_t B_chi(t)|^4}/r^2.    (8.4)
```

Thus the principal Mellin coefficient has to be subtracted before any
inequality is applied.

A tempting mixed-norm bound is

```text
E_times(B_chi)
 <=||B_chi||_1^2||B_chi||_2^2
 <=r||B_chi||_2^4.                                 (8.5)
```

Equations (8.4)--(8.5) reduce the fourth moment to

```text
sum_chi (sum_t|A_chi(t)C_chi(t)|^2)^2.             (8.6)
```

This reduction cannot reach (1.6).  In the most favorable symmetric case
`C_chi=A_chi`, additive Parseval and Cauchy's inequality give, for every
`chi`,

```text
sum_t|A_chi(t)|^2=r||w_1||_2^2,

sum_t|A_chi(t)|^4
 >=r^(-1)(sum_t|A_chi(t)|^2)^2
 =r||w_1||_2^4.                                    (8.7)
```

For a flat interval profile `||w_1||_2^2 asymp H`, the expression in (8.6)
is therefore at least

```text
r^3 H^4                                              (8.8)
```

after summing over `chi`.  The ideal total fourth moment is `r^2H^4`, and
even the fixed-power target is `r^2H^(5-delta)`.  At `r=H^2`, (8.8) is
larger than the latter by `H^(1+delta)`.  In particular, any proposed
normalization of (8.6) which would require its unnormalized form to be
`O(rH^(4+epsilon))` contradicts (8.7).

This does **not** give a lower bound of that size for the true Jacobi fourth
moment.  It proves that (8.5) has discarded the decisive subtraction in
(8.4).  The failure is in the mixed-norm inequality, not in the desired
theorem.

The recombination can be audited without estimates.  For nonzero `x_i`,

```text
sum_(t_1t_2=t_3t_4)
 e_r(t_1x_1+t_2x_2-t_3x_3-t_4x_4)

 =r^2 1_(x_1x_2=x_3x_4)-(r+1).                    (8.9)
```

To prove (8.9), insert a multiplicative character for the product
constraint.  Every nonprincipal character contributes four Gauss sums,
whose product is `r^2`; character orthogonality gives the displayed two
values.  The principal character contributes one.

After summing over `chi`, the other orthogonality condition is exactly
`u_1u_2=u_3u_4`.  Hence (8.9) reconstructs the original joint Vieta
collision, minus a uniform product-only baseline.  Applying ACZ before this
recombination controls the baseline but leaves the variance in (8.4), which
is precisely the unresolved joint energy.  Applying absolute values first
loses the required power.  Thus additive/multiplicative Parseval is an exact
reformulation, not by itself a new estimate.

### 8.2. Other imported estimates

Three further tempting substitutions fail for distinct reasons.

1. **Fiberwise genus-one counting.**  Fixing `x,y` and three root variables
   gives at most two choices for the fourth.  Together with the
   `H^(2+epsilon)` possible product collisions `x_1x_2=x_3x_4`, this is
   `H^(5+epsilon)`, exactly R115's endpoint.

2. **Pointwise double-character cancellation.**  The results of
   Shkredov--Shparlinski control important sums with one multiplicative
   character of an additive expression, using incidence estimates.  Their
   theorem applies to (1.2), after absorbing `chi(a)` and `chi(c)` into the
   two bounded weights.  With their moment parameter `nu=4` and
   `H=r^(1/2+o(1))`, it gives

   ```text
   |J_13(chi,psi)|
    <<H^(2-1/32+o(1))                               (8.10)
   ```

   for nonprincipal `psi`.  Exact second-moment orthogonality gives

   ```text
   sum_(chi,psi)|J_13(chi,psi)|^2<<r^2H^2.          (8.11)
   ```

   Therefore maximum times second moment yields only

   ```text
   sum_(chi,psi)|J_13(chi,psi)|^4
    <<r^2H^(6-1/16+o(1)),                           (8.12)
   ```

   almost one full power of `H` short of (1.6).  The pointwise route would
   need the much stronger scale (1.7).

3. **Polynomial-value or conic point bounds.**  Bounds for points of a
   fixed finite-field curve in a square-root box recover an `O(H)`-type
   fixed-fiber estimate here.  The needed gain is an average over the full
   correlated family of product aliases, not an improvement for one
   generic curve in isolation.

Relevant primary references are I. Shkredov and I. Shparlinski,
[*Double Character Sums with Intervals and Arbitrary Sets in Finite
Fields*](https://arxiv.org/abs/1803.08699), and I. Shparlinski,
[*Polynomial Values in Small Subgroups of Finite
Fields*](https://arxiv.org/abs/1401.0964).  Neither paper can be imported as
(1.6) without a new argument.

The right kind of theorem is therefore a large-values estimate for the
generic incomplete Jacobi transform, or equivalently an incidence theorem
which averages the genus-one fibers over the nonzero aliases in (5.5).

## 9. Structured-counterexample search

As a falsification probe, take

```text
w_i=1_[1,H]
```

and enumerate all `H^4` tuples exactly, accumulating their residues
`(P,Q)` for a prime `r` close to `4H^2`.  The following table reports the
exact energy and largest coefficient fiber.

| `H` | `r` | `E_(P,Q)` | `E/H^4` | maximum fiber |
|---:|---:|---:|---:|---:|
| 8  | 257  | 31,776     | 7.758 | 16 |
| 12 | 577  | 181,392    | 8.748 | 24 |
| 20 | 1601 | 1,495,120  | 9.345 | 32 |
| 30 | 3607 | 8,022,614  | 9.904 | 56 |
| 44 | 7753 | 37,594,224 | 10.03 | 64 |

Symmetric intervals, with `P=0` removed, show the same qualitative
behavior.  A two-dimensional finite-group Fourier computation reproduces
the direct energies and shows the three lines in Section 7 are only
`H^4`-scale pieces.

This rules out the most obvious small-height coherent fiber and is
consistent with `H^4` times logarithms.  It does **not** prove a uniform
estimate, does not test adversarial smooth phases, and cannot exclude a
sparse sequence of primes and intervals with larger energy.

## 10. Implication for the fixed-strip program

This attack produces a strict narrowing, not the requested fixed strip.
For the untwisted R115 coefficient energy, a proof of (1.6) with any fixed
`delta>0` would give Target 8.1 after native flatness.  Conversely, a
counterexample must now exhibit at least one of the following:

```text
nonzero product aliases abcd-a'b'c'd'=nr;
two simultaneously nonprincipal characters;
failure away from the scaling line chi^2 psi=1;
energy of size H^(5-o(1)) or larger.                 (10.1)
```

Axes, exact coincidences, the singular elliptic curve, principal
characters, and Vieta scaling cannot supply such a counterexample.

There is a separate interface warning.  The real BP packet contains the
phase `e_r(-s_1k(a+c))`.  The companion actual-profile report proves that
retaining `x=a+c` in the coefficient frame costs an additional endpoint
factor.  Therefore even an ideal proof of the untwisted moment (1.6) would
still have to be inserted into a joint endpoint/vector estimate; it would
not alone prove a zero-free strip.

The next mathematically honest target is exactly (1.6), preferably in the
strong form

```text
sum_(chi,psi generic)|J(chi,psi)|^4
 <<r^2H^(4+epsilon).                                (10.2)
```

A useful proof strategy must average the nonzero aliases in (5.5).  More
fixed-fiber Weil bounds, ordinary Burgess substitution, or separate
absolute values in `x` reproduce `H^5` and should be treated as fail-fast
endpoints rather than prospective fixed-power gains.
