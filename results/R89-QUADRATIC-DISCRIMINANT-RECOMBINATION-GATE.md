# Quadratic-discriminant recombination at the R87 contact

Status: R89 exact fixed-prime axis decomposition, exact fourth-moment
square-locus coefficient, B-spline contact comparison, and varying-modulus
applicability audit.  The Blomer--Pascadi mechanism remains a possible
off-axis input, but its square locus does not reproduce the R87 contact.
No fixed zero-free strip is proved, and no no-strip theorem is proved.

## 1. Verdict

The quadratic-character conversion of Blomer--Pascadi can be performed
algebraically **one prime modulus at a time** after completing the reciprocal
variable.  It cannot presently be performed as one signed theorem over the
outer varying prime modulus, and retaining the two zero arguments does not
repair this.

There is a sharper fail-fast obstruction than the fixed-modulus mismatch.
In the fourth moment used by Blomer--Pascadi, the large quadratic-character
main locus consists exactly of four dual frequencies whose residue multiset
has even multiplicities.  Thus:

```text
one zero argument + three off-axis arguments     not in square locus;
two zero arguments + one paired off-axis value   in square locus;
four zero arguments                              in square locus.          (1.1)
```

R87's `P_1` and `P_2` are one-axis terms: one coordinate of `Lhat` is zero
and the other is the canonical prime-minus-continuum frequency.  Their
coefficient in the Blomer--Pascadi square locus is therefore **exactly
zero**, whereas the coefficient needed to cancel `-P_1-P_2` is `+1` for
each orientation.

The paired-axis terms that do occur have a different weight.  They are
quartic functionals of an additive autocorrelation `z`; in particular their
zero-frequency input is an `L^2` mass.  The R87 contact is linear in the
one-axis marginal

```text
G_1(t)=integral L(t,u)du,       G_2(u)=integral L(t,u)dt.              (1.2)
```

For the actual R71 B-spline kernel this distinction can be written exactly,
not just at the level of homogeneity.  Consequently the square-discriminant
diagonal cannot be relabelled as the canonical contact.

One genuinely signed object survives the conversion: a varying-prime sum
of Legendre symbols of the four-step `SL_2` discriminant.  It is displayed
in Section 8.  It is a proper off-axis research target, but it contains no
one-axis main term and hence cannot by itself close the R87 conservation
law.

## 2. The exact term which has to be reproduced

Use R87's finite primitive gauge on the active support and put

```text
nu=sum_n lambda_N(n)delta_n-dt,        lambda_N(n)=Lambda(n),
E_L(nu)=double_integral L(t,u)dnu(t)conjugate(dnu(u)).                (2.1)
```

Let

```text
G_1(t)=integral L(t,u)du,       G_2(u)=integral L(t,u)dt,
A_1=sum_n lambda_N(n)G_1(n),
A_2=sum_n conjugate(lambda_N(n))G_2(n),
C=double_integral L(t,u)dtdu,
P_1=A_1-C,                     P_2=A_2-C.                           (2.2)
```

The exact all-sector identity is

```text
H_off+H_(theta=0)+H_(j=0)+H_axes=E_L(nu),                         (2.3)

H_axes=-A_1-A_2+C.                                                  (2.4)
```

After the elementary diagonal, ordinary-lattice, and Ramanujan fluctuation
are recompleted, the non-Wright sector is

```text
H_nonW=-P_1-P_2+Y^o(1).                                             (2.5)
```

Thus a proposed off-axis main term must have the signed coefficient

```text
+P_1+P_2.                                                           (2.6)
```

It is not enough to obtain a positive diagonal of the right order of
magnitude.

The frequency-side form makes the one-axis nature explicit.  A `b=0`
puncture contributes

```text
-Lhat(-theta/(gmn),0),                                              (2.7)
```

and the reversed `a=0` puncture contributes

```text
-Lhat(0,-theta/(gmn)).                                              (2.8)
```

After the canonical beat synthesis, (2.7)--(2.8) are exactly
`-P_1-P_2`, with the nonzero integer aliases retained as in R87.  Any
candidate main locus must therefore contain terms with precisely one zero
Fourier coordinate.

## 3. What the Blomer--Pascadi conversion actually does

For a fixed modulus `c`, Blomer--Pascadi start with the operator

```text
K_c(m,n)=S(am,n;c)                                                   (3.1)
```

on two intervals.  Two applications of Cauchy--Schwarz and a fourth-power
trace bound replace the original signed bilinear form by a nonnegative
four-step trace.  Fourier completion produces bounded autocorrelation
weights of the form

```text
z(h)=(4/H) sum_(u-v=h) w(u)conjugate(w(v))                           (3.2)
```

up to the harmless orientation convention.  This is their equation (3.7).
For a prime `r`, the special `SL_2(F_r)` character is

```text
chi_r^circ(g)=Legendre_r(Tr(g)^2-4)                                  (3.3)
```

away from `g=plusminus I`, where the character has the exceptional value
`r`.  For

```text
g=T^(a h_1) S T^(h_2) S T^(a h_3) S T^(h_4) S,
```

one has

```text
Tr(g)
 =a^2 h_1 h_2 h_3 h_4-a(h_1+h_3)(h_2+h_4)+2.                       (3.4)
```

This gives the signed discriminant sum

```text
sum_(h_1,...,h_4) z_1(h_1)...z_4(h_4)
 Legendre_r({Tr(g)^2-4}).                                            (3.5)
```

The saving is not obtained by identifying a signed main term in (3.5).
After a further Holder step, the last variable is put into

```text
C_(2,r)
 =sum_(x,y mod r)
   abs{sum_h z(h) Legendre_r((xh+y)^2-4)}^4.                         (3.6)
```

The large part of (3.6) is the locus on which the product of four quadratic
polynomials is a square.  Proposition 4.5 of the paper bounds this locus as
the diagonal term in its equation (4.8).  The next section computes its
coefficient exactly.

The source is Blomer--Pascadi,
[*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311),
v1, 2026-07-27, especially Propositions 3.1, 3.4, 3.6, and 4.5.

## 4. Exact square-locus coefficient

Here "square locus" has the character-sum meaning used in Proposition 4.5:
after expanding the absolute fourth power, the *product polynomial* in the
complete variable is a square.  It does not mean merely that one numerical
value `Tr(g)^2-4` is a quadratic residue; residues and nonresidues are the
two signs whose cancellation the character sum is meant to detect.

Let `r` be an odd prime.  Aggregate all integer aliases of the last Holder
weight into

```text
Z_a=sum_(h congruent a mod r)z(h),       a in F_r.                  (4.1)
```

Define

```text
S_2=sum_a abs(Z_a)^2,
T_2=sum_a Z_a^2,
S_4=sum_a abs(Z_a)^4.                                             (4.2)
```

### Theorem 4.1 (exact polynomial-square contribution)

In the expansion of (3.6), the contribution from tuples
`(a_1,a_2,a_3,a_4)` for which

```text
product_(i=1)^4 (X+a_i)                                            (4.3)
```

is a square in `F_r[X]` is exactly

```text
D_square(r;Z)
 =(r-2)^2[2S_2^2+abs(T_2)^2-2S_4]+2(r-2)S_4.                       (4.4)
```

Equivalently, its leading `r^2` coefficient is

```text
2S_2^2+abs(T_2)^2-2S_4.                                           (4.5)
```

The square condition in (4.3) says exactly that the residue multiset can be
partitioned into two equal pairs.

Here the coefficient of a four-tuple in the expansion of the absolute
fourth power is

```text
Z_(a_1)conjugate(Z_(a_2))Z_(a_3)conjugate(Z_(a_4)).                 (4.5a)
```

#### Proof

For a fixed four-tuple put

```text
f(X)=product_i(X+a_i),       A_u=Legendre_r(f(u)).                  (4.6)
```

The change of variables used in Blomer--Pascadi (4.11) is exact.  The
`x!=0` pairs are in bijection with `(u,v)` with `u!=v`, while `x=0`
contributes `r-2`.  If `d` is the number of distinct roots of `f`, then

```text
E_r(a_1,a_2,a_3,a_4)
 :=sum_(x,y mod r) product_i Legendre_r((xa_i+y)^2-4)
 =sum_(u!=v)A_u A_v+(r-2)
 =[sum_u A_u]^2+d-2.                                                (4.7)
```

If the four-tuple consists of two distinct pairs, then `d=2`,
`sum_u A_u=r-2`, and

```text
E_r=(r-2)^2.                                                        (4.8)
```

If all four residues agree, then `d=1`, `sum_u A_u=r-1`, and

```text
E_r=r(r-2).                                                        (4.9)
```

The three pair partitions contribute

```text
2S_2^2+abs(T_2)^2.                                                  (4.10)
```

An all-equal tuple occurs in all three partitions, so subtracting two
copies gives the union coefficient

```text
2S_2^2+abs(T_2)^2-2S_4.                                            (4.11)
```

Give this union the two-distinct value `(r-2)^2`, then correct every
all-equal tuple by

```text
r(r-2)-(r-2)^2=2(r-2).                                             (4.12)
```

This proves (4.4).

### Corollary 4.2 (the one-axis coefficient is zero)

A polynomial-square tuple contains the residue `0` with even multiplicity.
Consequently the square locus has:

```text
coefficient of one Z_0 axis copy       0;
coefficient of three Z_0 axis copies   0.                               (4.13)
```

The first axis terms occur through quantities such as

```text
abs(Z_0)^2 sum_(a!=0)abs(Z_a)^2,
Re[Z_0^2 conjugate(sum_(a!=0)Z_a^2)],
abs(Z_0)^4.                                                        (4.14)
```

They are paired-axis energies, not one-axis contacts.

This is independent of how favorable the eventual estimate for the
nonsquare tuples may be.

## 5. Exact fixed-prime axes before taking the fourth power

The failure in Corollary 4.2 is not caused by forgetting that Kloosterman
sums have zero arguments.  They can be retained exactly before Cauchy.
For a prime `r`,

```text
S(0,0;r)=r-1,
S(0,k;r)=-1                 for k!=0,
S(h,0;r)=-1                 for h!=0.                              (5.1)
```

Hence for arbitrary full residue vectors `alpha,beta`,

```text
B_r^full=sum_(h,k mod r)alpha_h beta_k S(h,k;r)

 =sum_(h,k!=0)alpha_h beta_k S(h,k;r)
  -alpha_0 sum_(k!=0)beta_k
  -beta_0 sum_(h!=0)alpha_h
  +(r-1)alpha_0 beta_0.                                            (5.2)
```

This has the same inclusion--exclusion *shape* as the two punctured axes
and their common origin.  At this signed bilinear level the axes have not
been lost.

However, the Blomer--Pascadi fourth-power step replaces (5.2) by a spectral
norm/positive moment.  Corollary 4.2 then forces each zero argument in its
large square locus to be paired.  The two linear middle terms in (5.2) do
not reappear with their signed coefficients.

There is an exact operator explanation.  For the full `r` by `r`
Kloosterman matrix,

```text
sum_h S(h,m;r)conjugate(S(h,n;r))=r c_r(m-n),
K_r K_r^*=r(rI-J),
K_r 1=0.                                                           (5.3)
```

Thus full completion removes the constant vector and has norm exactly `r`
on its orthogonal complement.  This is the fixed-prime analogue of R87's
automatic singular-series-background cancellation.  It is not a
contraction of the coefficient-specific `Lambda-1` direction.

Blomer--Pascadi also remove the cases `h_1h_2h_3=0` or `h_1+h_3=0` by an
absolute error in their equation (3.19) before the final Holder step.  One
may keep those cases via (5.1)--(5.2), but doing so restores explicit axis
terms rather than a new quadratic-character cancellation.

For example, the one-axis slice `h_1=0` in (3.4) has

```text
Tr(g)=2-a h_3(h_2+h_4),
Tr(g)^2-4
 =a h_3(h_2+h_4)[a h_3(h_2+h_4)-4].                              (5.4)
```

The last polynomial is not identically a square.  Thus a single retained
axis is a remaining signed quadratic-character sum, not an `r`-sized
diagonal.  Universal exceptional configurations arise only after further
degeneracy; in the fourth-moment bookkeeping those are paired-axis or
all-axis terms.  Estimating the nonsquare one-axis slice with its original
cofactor weight would be a new coefficient-specific theorem, not the
published square-locus bound.

## 6. The B-spline weight is the wrong functional

For the actual R71 kernel, write

```text
f_R(t)=t^(-1/2)V_(h,k)(R-log t),
L(t,u)=integral psi(R)f_R(t)f_R(u)dR,                              (6.1)
```

with real `V` and nonnegative `psi`.  Put

```text
J_0=integral V_(h,k)(x)e^(-x/2)dx.                                (6.2)
```

Direct substitution gives

```text
integral f_R(u)du=e^(R/2)J_0,                                     (6.3)

G_1(t)
 =J_0 integral psi(R)e^(R/2)t^(-1/2)
       V_(h,k)(R-log t)dR,                                        (6.4)

C=J_0^2 integral psi(R)e^R dR.                                    (6.5)
```

Therefore the exact Hermitian contact is

```text
P_1+P_2
 =2 Re<nu,G_1>

 =2J_0 Re integral psi(R)e^(R/2)
    [sum_n Lambda(n)n^(-1/2)V_(h,k)(R-log n)
      -J_0 e^(R/2)]dR.                                             (6.6)
```

This is linear in the prime discrepancy and uses the one-axis `L^1`
marginal of `L`.

By contrast, the zero input to the Blomer--Pascadi square locus is, in the
no-alias range,

```text
Z_0=z(0)=(4/H)sum_u abs(w(u))^2.                                  (6.7)
```

Equations (4.4) and (4.14) then use `abs(Z_0)^2` or `abs(Z_0)^4`.
Even when `w` is built from the completed R71 amplitude, (6.7) is an
additive autocorrelation energy.  It is not (6.4), and it has no term with
the coefficient in (6.6).

The frequency-side comparison is just as direct:

```text
R87 one-axis weight:       Lhat(-theta/(gmn),0)
                           or Lhat(0,-theta/(gmn));

BP square-axis weight:     products of two or four Z_0/Z_a
                           autocorrelations.                         (6.8)
```

Thus the exact comparison requested at the fail-fast gate is

```text
needed coefficient of P_1+P_2              +1,+1;
square-locus coefficient of P_1+P_2          0, 0;
first square-locus axis weight                paired L^2 autocorrelation;
R71 contact weight                            one-axis B-spline marginal. (6.9)
```

No choice of normalization in the fourth root changes (6.9).

## 7. Why the varying outer prime does not fix the coefficient

The R71 square-root phase is

```text
e_r(-k inverse(p)),        k=j theta,                                (7.1)
```

with the outer prime `r` varying.  For each fixed `r`, completion in `p`
is exact:

```text
e_r(-k inverse(p))1_((p,r)=1)
 =r^(-1)sum_(h mod r)S(h,-k;r)e_r(-hp).                             (7.2)
```

The `h=0` term is `c_r(k)` and the `k=0` term is `c_r(h)`, so (7.2)
retains the two axes if they are not discarded.  This proves that the
fixed-prime quadratic-character conversion is an available algebraic
reindexing after sufficient coefficient separation.

It does **not** put the R71 sum in the hypotheses of the published theorem:

1. each `r` gives a different Kloosterman operator and a different finite
   field;
2. the completed additive frequency and `k=j theta` are not the native two
   balanced interval variables of Theorem 1.1;
3. the amplitude still couples `g,p,r,theta,j` and the B-spline seams;
4. summing the fixed-`r` bounds by triangle inequality removes precisely
   the signed outer recombination under investigation; and
5. taking the fourth power before the `r`-sum creates mixed moduli
   `r_1,r_2,r_3,r_4`, for which the single-`SL_2(F_r)` trace identity
   (3.3)--(3.4) no longer applies.

One can instead form the direct sum of all fixed-`r` operators.  Its fourth
trace is the sum of the nonnegative fixed-`r` fourth traces, so its square
locus is

```text
sum_r D_square(r;Z_r).                                               (7.3)
```

Every summand still has zero one-axis coefficient.  Varying the modulus
therefore cannot change the local parity statement (4.13).

The published fixed-modulus saving `r^(-1/32)` in its critical native range
is consequently not a bound for the all-sector R71 energy.

## 8. The genuinely surviving signed sum

Before the final Holder/absolute-value step, the prime-modulus conversion
does expose a concrete signed object.  In the simplest `g=1` orientation it
has the form

```text
Q_off
 =sum_(r in P) omega_r
   sum_(h_1,...,h_4)^off
     z_(1,r)(h_1)z_(2,r)(h_2)z_(3,r)(h_3)z_(4,r)(h_4)
     Legendre_r(Delta_a(h_1,h_2,h_3,h_4)),                           (8.1)

Delta_a(h_1,h_2,h_3,h_4)
 =[a^2 h_1h_2h_3h_4-a(h_1+h_3)(h_2+h_4)+2]^2-4.                    (8.2)
```

Here `omega_r` and the four `z_(i,r)` would have to retain the actual
cofactor coefficients, common-`g` mask, B-spline amplitude, and rectangular
limit.  The superscript `off` removes the explicit zero-argument and
`g=plusminus I` cases only after they have been recorded through (5.2).

Quadratic reciprocity makes (8.1) an interesting possible large-sieve
target in the varying prime `r`: away from primes dividing `2Delta_a`, the
Legendre symbol can be regarded as a real character in `r` whose conductor
is controlled by the squarefree kernel of `Delta_a`.  This observation is
not a bound; repeated or square `Delta_a` values are exactly the diagonal
which must be retained.

Most importantly, (8.1) is a signed **off-axis fourth-trace sum**.  Its
square-polynomial main locus is (4.4), and its one-axis main coefficient is
zero.  Even a fixed-power theorem for (8.1) would therefore improve the
proper off-axis estimate only.  To close R87 it would need an additional,
separately proved signed first-axis term equal to `+P_1+P_2`; supplying that
term is the original fixed-strip gate.

## 9. Disposition

```text
fixed-r reciprocal completion                         EXACT;
fixed-r Kloosterman axes                              EXACT;
four-step discriminant conversion                     EXACT off axis;
square-polynomial locus coefficient                   EXACT, (4.4);
coefficient of a one-axis contact in that locus       ZERO;
B-spline weight match to P_1+P_2                      FALSE;
outer varying-r signed theorem                        NOT IMPORTED;
varying-r quadratic-character sum (8.1)               GENUINE / OPEN;
all-sector fixed-power estimate                       OPEN;
fixed zero-free strip                                 NOT PROVED;
nonexistence of a fixed strip                         NOT PROVED.          (9.1)
```

The Blomer--Pascadi architecture is valuable as a potential new off-axis
lemma, especially if quadratic reciprocity can exploit the outer prime
average.  It does not supply the missing recombination: its large main
locus pairs the axis, while the R87 conservation law needs a signed single
axis.
