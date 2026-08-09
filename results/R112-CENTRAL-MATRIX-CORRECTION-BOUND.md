# R112 central-matrix correction bound

Status: exact classification and universal-profile bound for the
`g=plusminus I` correction which is outside R110--R111.  In the critical
no-alias box, every unramified central configuration is either a paired
double axis or a modular hyperbola.  The actual Blomer--Pascadi completion
profiles satisfy the required point-evaluation bound at their effective
Fourier scale, including every fixed `Q_h` cross-correlation and fixed seam
translate.  The formal BP cutoff is a `c^epsilon` enlargement of that scale;
this is an epsilon loss, not an exact identification of the two lengths.
The still-unproved interface is the representation of the complete
outer-prime-dependent R71 packet by these BP profiles at controlled
projective cost.

Date: 2026-08-07.

## 1. Exact finite-field classification

Put

```text
A(x)=[[x,-1],[1,0]]
```

and, over `F_r`, write

```text
g=A(x_1)A(x_2)A(x_3)A(x_4).                         (1.1)
```

Direct multiplication gives

```text
g_11=x_1x_2x_3x_4-x_3x_4-x_1x_4-x_1x_2+1,
g_12=x_1+x_3-x_1x_2x_3,
g_21=x_2x_3x_4-x_4-x_2,
g_22=1-x_2x_3.                                      (1.2)
```

**Theorem 1.1 (central words).**  For every odd prime `r`,

```text
g= I  iff x_3=-x_1, x_4=-x_2, x_1x_2=0,
g=-I  iff x_3= x_1, x_4= x_2, x_1x_2=2.             (1.3)
```

Indeed, if `g=epsilon I`, `epsilon in {plusminus1}`, the bottom-right and
two off-diagonal equations in (1.2) give

```text
x_2x_3=1-epsilon,
x_3=-epsilon x_1,
x_4=-epsilon x_2.                                   (1.4)
```

Thus `x_1x_2=1-epsilon`.  Conversely these equations give the required
matrix (or use determinant one to recover its remaining diagonal entry).

Apply this with

```text
x_1=lambda h_1, x_2=h_2, x_3=lambda h_3, x_4=h_4,  (1.5)
```

where `lambda` is an integer.  If `r` does not divide `lambda`, then

```text
g=I:
 h_3=-h_1, h_4=-h_2, and h_1h_2=0       (mod r),

g=-I:
 h_3= h_1, h_4= h_2, and lambda h_1h_2=2 (mod r).   (1.6)
```

Thus `g=I` is the union of two paired double axes.  The `g=-I` locus is
one modular hyperbola, not another axis.

## 2. Exact weighted correction

Let `z_i` be complex weights on an integer box.  Aggregate aliases by

```text
Z_i(a)=sum_(h congruent a mod r) z_i(h),   a in F_r. (2.1)
```

When `r` does not divide `lambda`, the two central coefficients are

```text
C_r^+
 =Z_1(0)Z_3(0) sum_y Z_2(y)Z_4(-y)
  +Z_2(0)Z_4(0) sum_x Z_1(x)Z_3(-x)
  -product_i Z_i(0),                                  (2.2)

C_r^-
 =sum_(lambda x y=2 mod r)
    Z_1(x)Z_3(x)Z_2(y)Z_4(y).                        (2.3)
```

The subtraction in (2.2) removes the twice-counted origin.  Since the
ordinary Legendre trace function is zero at trace `plusminus2`, while the
special `SL_2(F_r)` character has value `r` at both central matrices, its
correction at this raw trace-character layer is exactly

```text
r(C_r^+ + C_r^-).                                    (2.4)
```

This normalization is exactly equation (3.11) of Blomer--Pascadi,
[*Bilinear forms with Kloosterman sums via quadratic
characters*](https://arxiv.org/abs/2607.24311); it is not inferred merely
from the trace polynomial.

Equations (2.2)--(2.4) hold with arbitrary complex weights; no positivity
or conjugation convention is being assumed.

Suppose now that every `z_i` is supported on `[-H,H]` and `2H<r`.  There
are no coordinate aliases, so (2.2) becomes

```text
C_r^+
 =z_1(0)z_3(0) sum_h z_2(h)z_4(-h)
  +z_2(0)z_4(0) sum_h z_1(h)z_3(-h)
  -product_i z_i(0).                                (2.5)
```

The product congruence in (2.3) may still wrap modulo `r`; no assumption
`abs(lambda)H^2<r` is needed below.

## 3. Universal-profile bound

The precise property of a fixed scaled Fourier profile which is needed is

```text
norm(z_i)_infinity
 <=K_i H^(-1/2) norm(z_i)_2.                         (3.1)
```

Put `Z=product_i norm(z_i)_2`.  Cauchy's inequality in (2.5) gives

```text
abs(C_r^+)
 <=[K_1K_3+K_2K_4]H^(-1)Z
    +product_i K_i H^(-2)Z.                         (3.2)
```

For (2.3), the map `x -> 2/(lambda x)` is a bijection on nonzero
residues.  In the no-coordinate-alias box it restricts to a partial
matching between the two integer supports.  Hence

```text
abs(C_r^-)
 <=norm(z_1z_3)_2 norm(z_2z_4)_2
 <<_(K_i) H^(-1)Z.                                  (3.3)
```

This is uniform in the amount of product wrap and in the unramified value
of `lambda modulo r`.

For fixed `lambda` there is a sharper, though unnecessary, check.  Every
point of (2.3) obeys

```text
lambda h_1h_2=2+k r,
abs(k)<<1+abs(lambda)H^2/r.                          (3.4)
```

Divisor counting therefore gives

```text
#support(C_r^-)
 <<_(C,epsilon)H^epsilon[1+abs(lambda)H^2/r]         (3.5)
```

when `abs(lambda)<=H^C`.  At `r asymp H^2` and fixed (or subpower)
`lambda`, (3.1) and (3.5) improve (3.3) to

```text
abs(C_r^-)<<H^(-2+epsilon)Z.                         (3.6)
```

The paired `g=I` axes, not the modular hyperbola, are consequently the
larger universal central stratum.

Condition (3.1) is automatic for a genuine fixed scaled profile.  For
example, if

```text
z_(i,H)(h)=alpha_i Phi_i(h/H)+O(abs(alpha_i)/H),     (3.7)
```

with fixed bounded compactly supported nonzero `Phi_i`, then
`norm(z_i)_2 asymp abs(alpha_i)sqrt(H)` and (3.1) follows.  The same is true
for the autocorrelation of a fixed scaled B-spline:

```text
z_H(h)=c/H sum_u w_H(u)conjugate(w_H(u-h)),
w_H(u)=beta W(u/H),                                  (3.8)
```

because (3.8) is a Riemann sum for a fixed autocorrelation profile.  Section
6 proves the stronger band-limited version needed for the actual BP
profiles and the finite `Q_h` family.  It also records the distinction
between the effective profile scale and BP's larger formal cutoff.

## 4. Comparison with R111

Take `R=H^2`, primes `r in [R,2R]`, and assume the rows under consideration
are unramified.  For one separated component, put

```text
Q_cent=sum_r omega(r) r(C_r^+ + C_r^-).              (4.1)
```

If the constants in (3.1) are `H^o(1)`, (3.2)--(3.3) give

```text
abs(Q_cent)
 <<H^(1+o(1)) Z norm(omega)_1
 <<H^(2+o(1)) Z norm(omega)_2.                       (4.2)
```

At `lambda=1`, R111 bounds the nonparabolic part of the same separated raw
trace-character sum by

```text
H^(11/4+epsilon) Z norm(omega)_2.                    (4.3)
```

Thus the special central correction for fixed scaled profiles is smaller
than the R110--R111 off-axis bound by

```text
H^(-3/4+o(1))=R^(-3/8+o(1)).                         (4.4)
```

This is the abstract R111 critical normalization with one fixed integer
`lambda=1` across the outer primes.  It is not, by itself, the generic BP
normalization: BP uses `lambda=bar(a) modulo r`, which can vary with `r`
and whose least integer representative can have size comparable to `r`.
The exact BP central formula is uniform in that residue, but R111's
`lambda=1` off-axis line cannot be imported for generic `a` without a
separate coefficient/varying-prime reduction.

For unit-size flat outer weights, (4.2) is `H^(3+o(1))Z`, whereas (4.3)
is `H^(15/4+epsilon)Z`.  If the four scaled packets themselves have
`norm(z_i)_2 asymp sqrt(H)`, then these are respectively `H^5` and
`H^(23/4)` in the raw unit-amplitude ledger.

At this raw moment layer the comparison is scale invariant: multiplying
any packet by a scalar multiplies both sides through `Z`.  What matters
here is the profile flatness (3.1).  Section 7 separately records the loss
when this raw comparison is subsequently passed through BP's fourth root.

There is no coefficient-uniform substitute for (3.1).  For example, take

```text
z_1=z_3=delta_0,
z_2=z_4=1_[-H,H].                                    (4.5)
```

Then the first paired axis in (2.5) has size `asymp H`, while
`Z asymp H`; there is no `H^(-1)` gain.  With flat unit outer weights its
raw central contribution is of order `H^5`, whereas the formal R111
off-axis bound for the same norms is only `H^(19/4+epsilon)`.  Thus R110's
arbitrary-weight theorem cannot simply absorb the special central value.
The universal-profile or an equivalent point-evaluation estimate is a
genuine additional hypothesis.

## 5. Ramification and alias warnings

If `r` divides `lambda`, then `x_1=x_3=0` for every input.  The exact
classification changes to

```text
g=I  iff h_4=-h_2 (mod r), with h_1,h_3 arbitrary,
g=-I never.                                          (5.1)
```

In a no-alias box its weighted coefficient is

```text
[sum_h z_1(h)][sum_h z_3(h)]
 sum_t z_2(t)z_4(-t).                                (5.2)
```

Even under (3.1), (5.2) can have size `H Z`, and after multiplication by
`r asymp H^2` a single ramified row can have size `H^3 Z`.  It is not
uniformly power-small relative to (4.3) when the outer weight is
concentrated on that row.  For fixed `lambda`, no prime `r asymp H^2`
ramifies once `H` is large.  For a growing coefficient one must either
remove the finitely many divisors `r|lambda`, prove that their outer weights
are harmless, or use an exact packet identity such as a vanishing full
sum in (5.2).

If `2H>=r`, formulas (2.2)--(2.3) remain exact after residue aggregation,
but flatness of the original integer profile does not by itself imply
flatness of the aliased vectors `Z_i`.  Coherent aliases can increase both
point evaluations and `l^2` norms.  The critical regime `H asymp sqrt(r)`
has no coordinate aliases for large `r`; only the harmless product wrap in
(3.4) remains.

For BP Proposition 3.1 this ramified case does not occur: its odd exponent
is `lambda=bar(a) modulo c`, and `a` is a unit modulo `c`.  The warning is
needed only when the R71 lift replaces that unit by a different integer
coefficient.

## 6. Flatness for the actual BP completion profiles

The weights in BP Proposition 3.1 are more structured than the proposition's
stated bound `z_i(h)<<1`.  Corollary 4.11 of Pascadi,
[*Non-abelian amplification and bilinear forms with Kloosterman
sums*](https://arxiv.org/abs/2511.08445), constructs, before the
Schwartz-tail truncation,

```text
u_(L,s)(n)=Phihat(n/L)e(-sn/c),
L_1=c/M,                    L_2=c/N,                 (6.1)
```

where `Phi` is a fixed smooth function of compact support.  BP takes

```text
B_1=H_1=2c^epsilon L_1,
B_2=H_2=2c^epsilon L_2                              (6.2)
```

and, for `i congruent j (mod 2)`, equation (3.7) of BP is

```text
z_i(t)=4/B_j sum_(|n|,|n-t|<=B_j/2)
                    u_(L_j,s_j)(n)
                    conjugate[u_(L_j,s_j)(n-t)].     (6.3)
```

Thus `B_j` is the formal support radius of `z_i`, while `L_j` is its
effective variation length.  They must not be denoted by the same symbol
when epsilon powers are being audited.

**Theorem 6.1 (BP packet flatness).**  The bare profiles (6.1)--(6.3)
satisfy (6.9).  Any fixed finite sum of their scaled translates,
modulations, and comparable fixed-scale variants satisfies (6.8), uniformly
in the endpoint phases.  This includes the fixed `Q_h` and fixed-seam
families of R102, modulo the arbitrary-power truncation error in (6.10).

For the proof, use for a sequence `u` the Fourier series

```text
U(alpha)=sum_n u(n)e(-n alpha),       alpha in R/Z.  (6.4)
```

Poisson summation applied to (6.1) gives, up to an irrelevant sign in the
argument,

```text
U_(L,s)(alpha)
 =L sum_(k in Z)Phi(L[k-alpha-s/c]).                 (6.5)
```

If the support of `Phi` has length `A`, the support of (6.5) on the
frequency circle has measure at most `A/L`.  The endpoint `s` only
translates this support.  If

```text
R_(u,v)(t)=sum_n u(n)conjugate[v(n-t)],              (6.6)
```

then the Fourier series of `R_(u,v)` is a product of `U` and `conjugate(V)`.
It is therefore supported on a set `E` of measure `O(1/L)` when the two
scales are comparable to `L`.  Fourier inversion, Cauchy, and Parseval give

```text
norm(R_(u,v))_infinity
 <=integral_E abs(Rhat(alpha))dalpha
 <=meas(E)^(1/2)norm(Rhat)_2
 <<L^(-1/2)norm(R_(u,v))_2.                          (6.7)
```

This argument is homogeneous and remains true if the cross-correlation is
zero.  It requires neither positivity nor a lower bound at `t=0`.

More generally, let `u` and `v` each be a sum of at most `J` fixed scaled
profiles, index translates, and linear phase modulations, with all profile
scales comparable to `L` and all underlying compact supports of bounded
scaled length.  Their Fourier supports are unions of at most `J` arcs of
length `O(1/L)`.  The same proof yields

```text
norm(R_(u,v))_infinity
 <<J^(1/2)L^(-1/2)norm(R_(u,v))_2.                   (6.8)
```

The constant is independent of the endpoint phases and of where the arcs
meet.  Consequently:

1. the two bare BP autocorrelations satisfy

```text
norm(z_i)_infinity<<L_j^(-1/2)norm(z_i)_2;           (6.9)
```

2. the three translated packets made by the fixed `Q_h` operator have
   `J<=3`, and their full autocorrelation, or any of the at most nine
   cross-correlations, satisfies (6.8);

3. fixed B-spline endpoints and seams only change the bounded number,
   locations, and lengths of these arcs.  The estimate is uniform provided
   the number of seam pieces and their scaled support diameters remain
   bounded, exactly the fixed-`h`, fixed-seam regime stated in R102.  If a
   later partition uses `J=H^o(1)` pieces or scaled support diameter
   `H^o(1)`, (6.8) retains the corresponding square-root subpower factor;
   a power-growing seam bank would have to be charged explicitly.

The sharp restrictions in (6.3) do not invalidate this argument.  Since
`Phihat` is Schwartz and `B_j/(2L_j)=c^epsilon`, for every `D>0`

```text
norm(u-u 1_(abs(n)<=B_j/2))_1<<_(D,epsilon,Phi)c^(-D). (6.10)
```

after choosing a sufficiently high Schwartz seminorm.  The convolution
inequality transfers (6.10) to every fixed autocorrelation and
cross-correlation in both `l^2` and `l^infinity`.  For a bare BP
autocorrelation, its `l^2` norm is `asymp L_j^(3/2)` before the factor
`4/B_j`, so the error is absorbed and (6.9) holds for the truncated weight
itself.  For a finite cross-term which vanishes identically before
truncation, its truncated remnant is part of the same arbitrary-power BP
tail error; it must be put there rather than assigned a relative flatness
constant.

In terms of the formal cutoff, (6.9) is

```text
norm(z_i)_infinity
 <<c^(epsilon/2)B_j^(-1/2)norm(z_i)_2.               (6.11)
```

Thus (3.1) holds with `K_i<<c^(epsilon/2)`, not with an epsilon-independent
constant when `H` means BP's formal cutoff.  Because the completion margin
may be chosen with an arbitrarily small positive epsilon, this is an
ordinary epsilon loss and can be made smaller than any prescribed fixed
power.  It is not legitimate to set `K_i=O(1)` at fixed epsilon.

For unequal side lengths, (3.2)--(3.3) consequently sharpen to the
effective-scale statement

```text
abs(C_r^+)+abs(C_r^-)
 <<[L_1^(-1)+L_2^(-1)+(L_1L_2)^(-1/2)]Z             (6.12)
```

up to the arbitrary-power tail.  In the balanced critical box
`M,N asymp sqrt(c)`, both `L_j asymp sqrt(c)`, so (6.12) is
`O(c^(-1/2)Z)`.

For completeness, the formal cutoff does not hide a loss in the
central/off-axis comparison in the special fixed-coefficient case.  In a
varying-prime row with `r asymp R=L^2`, formal support
`B=R^eta L`, and `lambda=1`, R111 with the honest trace interval
`N<<B^4` gives

```text
off-axis <<B^(11/4+o(1))Z norm(omega)_2,
central  <<R^(1+o(1))Z norm(omega)_2.                (6.12a)
```

Thus the raw ratio is at most

```text
R/B^(11/4)=R^(-3/8-11eta/4),                        (6.12b)
```

and in the arbitrarily-small-margin convention it is
`R^(-3/8+o(1))`.  This calculation does not remove the generic
`bar(a)` issue just noted.

What (6.7)--(6.12) do **not** prove is that the actual completed R71
coefficient is a fixed union of these arcs.  R102 proves only that `Q_h`
preserves a separation which already exists; R104 records that the
Vaughan-to-fixed-`r` BP lift is still absent.  An outer-prime mask or
arithmetic coefficient inserted inside `u(n)` can spread `U(alpha)` around
the entire frequency circle and destroy (6.7).  The exact remaining
interface is therefore

```text
actual R71 packet
   = finite/projectively controlled sum of BP band-limited packets
     + an error controlled before the fourth moment.                 (6.13)
```

No such identity is presently proved in the repository.

## 7. BP normalization audit

There are three distinct normalization layers.  They should not be mixed.

First, for `k=2`, BP equation (3.8) is exactly

```text
Tr((Fhat Fhat*)^2)=(B_1B_2)^(-2) S,                 (7.1)
```

where `S` is the raw four-variable character sum and each `z_i` already
contains its factor `4/B_j` from (6.3).  Therefore the central correction
inside this same raw `S` is exactly

```text
c(C_c^+ + C_c^-).                                   (7.2)
```

There is one factor `c`, supplied by BP equation (3.11), and no second
factor from (7.1).  Equations (2.2)--(2.4) and R111's Legendre sum are thus
like-for-like only at this raw `S` layer.

Second, the Schatten fourth-root step gives

```text
norm(Fhat)
 <=(B_1B_2)^(-1/2) S^(1/4).                         (7.3)
```

BP Proposition 3.1 then gives

```text
abs(bilinear form)
 <=norm(alpha)_2 norm(beta)_2 {
    c^(1+2epsilon)(B_1B_2)^(-1/2)S^(1/4)
    +O(c^(-100))}.                                  (7.4)
```

Hence a relative saving `delta` between two positive upper bounds at the
raw moment layer becomes only `delta^(1/4)` after the BP fourth root.  In
particular, the formal raw ratio `c^(-3/8+o(1))` corresponding to (4.4)
would become `c^(-3/32+o(1))`, not `c^(-3/8)`, in a fixed-modulus bilinear
operator estimate.  R111 itself is an outer-prime signed sum rather than
that fixed-modulus operator norm, so this sentence is a normalization
translation, not a theorem identifying the two problems.

Third, BP Proposition 3.4 is an amplified triangle-inequality bound.  For
prime `c`, its `d=c` term carries a factor `c` and imposes
`g congruent plusminus I (mod c)`; this represents the same central factor
as (7.2).  It is not an additional multiplier, nor is Proposition 3.4 an
exact decomposition into an off-axis Legendre sum and a central sum.  For
the exact prime-modulus split one must use equation (3.11) before that
triangle inequality.

Finally, BP has

```text
a_1=a_3=bar(a),       a_2=a_4=1,                    (7.5)
```

and the word in equation (3.8) has the prefactor `(-1)^k=1` for `k=2`.
Thus the matrix classification in Section 1 applies with
`lambda=bar(a) modulo c` and with no missing sign.  Since `a` is a unit,
the BP central word is automatically in the unramified case.

This also identifies the exact limit of the claimed like-for-like
comparison.  For each fixed prime modulus, equation (3.11) splits the same
raw BP moment into its ordinary Legendre part and (7.2), with identical
weights and the identical prefactor in (7.1).  That comparison is exact.
Identifying the Legendre part with R111 additionally requires all of the
following:

```text
same four z_i packets,
same integer trace lift and trace interval,
same outer-prime coefficient bar(a),
same projective separation before the outer Cauchy step.              (7.6)
```

Only the first item is proved for the bare BP profile.  In particular,
unless `a=1` (or another reduction supplies a fixed small inverse), R111's
displayed `lambda=1` exponent is not yet a bound for BP's generic off-axis
piece.  The normalization factors are now reconciled; the arithmetic
identification in (7.6) remains open.

## 8. Disposition

The flatness concern is closed for the profiles BP actually constructs:

```text
bare BP autocorrelations                         PROVED
fixed Q_h finite cross-correlations              PROVED BEFORE TRUNCATION
literal degenerate truncated cross-terms         ABSORBED AS BP TAIL
fixed endpoint phases and fixed seam translates PROVED
Schwartz cutoff tails                            NEGLIGIBLE AS IN BP
all BP factors through the fourth root           AUDITED.             (8.1)
```

The central correction is therefore not the obstruction in a genuine BP
critical box.  The unresolved statement is (6.13), together with the
outer projective-cost and recombination requirements already isolated in
R102, R104, and R111.  Until that lift is proved, this report supplies a
conditional central ledger, not a zero-free strip.
