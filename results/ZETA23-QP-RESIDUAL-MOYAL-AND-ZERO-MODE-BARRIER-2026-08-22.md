# QP four-cycle: residual Moyal identity and the zero-mode barrier

**Date:** 2026-08-22  
**Verdict:** the near-dilation ratio and carry residual do form an exact
phase-space family, but its Moyal identity is an **averaged modulation**
statement.  The required positive fourth trace is the exceptional zero
modulation.  The actual carry mask localizes every affine-line atom to one
point, so the centered affine cancellation disappears.

There is one useful exact theorem.  If `H_h` is the row-pair/color-pair
incidence layer with

```text
h=a*c-a'*c',
```

then every `H_h` is a weighted partial matching.  Consequently

```text
integral_0^1 ||sum_h exp(2*pi*i*h*theta) H_h v||_2^2 dtheta
 =sum_h ||H_h v||_2^2
 <<D q^o(1) ||v||_2^2.                              (0.1)
```

For `v(c,c')=z_c conjugate(z_c')`, the right side is already the desired
`D q^o(1)||z||_2^4` scale.  But the original fourth trace is the left side
at the single point `theta=0`.  Point evaluation can cost one more full
factor `D`, and a cyclic matching example with a genuine tensor-square
input attains that loss.  Thus affine/Heisenberg Moyal alone gives no new
four-cycle exponent.

The missing statement is now especially clean: prove that the actual
prime-power carrier mask has a zero-mode restriction estimate on the
rank-one tensor cone.  This is equivalent in strength to excluding a
coherent Latin block in the actual `H` graph; it is not supplied by Fourier
orthogonality.

No FC or improved exponent is claimed here.

---

## 1. Direct multiplicative Hankel form

Let `S` be the actual prime-power shell, and let `tau(a,b,c)` be the retained
carry kernel.  Pair uniqueness permits the notation

```text
f_z(a*b)=z_c tau(a,b,c)
```

when the unique color `c` exists, and zero otherwise.  For ordered distinct
row and color pairs put

```text
rho=(a,a'),                 gamma=(c,c'),
H(rho,gamma)=sum_b tau(a,b,c) conjugate(tau(a',b,c')). (1.1)
```

The sum in (1.1) has at most one term: `(a,c)` already determines `b` in the
active product window.  With

```text
v_z(c,c')=z_c conjugate(z_c'),
```

direct expansion gives

```text
sum_(a!=a') |sum_b f_z(a*b) conjugate(f_z(a'*b))|^2
 =||H v_z||_2^2,                                    (1.2)
||v_z||_2<=||z||_2^2.                               (1.3)
```

Thus the proposed ratio/shift transform is most naturally a transform of
the existing `H` incidence operator.

For a supported entry define residuals

```text
r =8*a*b*c-q^3,            r'=8*a'*b*c'-q^3.
```

Then

```text
r-r'=8*b*h,                h=a*c-a'*c',
|h|<<D.                                                   (1.4)
```

The rational affine graph of this entry is

```text
a'=(c/c')*a-h/c'.                                   (1.5)
```

Hence `(c/c',h)` is exactly the near-dilation/translation coordinate
suggested by the multiplicative-Hankel picture.

## 2. Every residual layer is a partial matching

The shell ratio is strictly below two.  Distinct shell prime powers have
different prime bases and are therefore coprime.  Its diameter is also
strictly below its minimum.

Fix a row pair `(a,a')`.  Suppose two color pairs `(c,c')` and `(d,d')`
have the same residual shift.  Then

```text
a*(c-d)=a'*(c'-d').                                  (2.1)
```

Since `gcd(a,a')=1`, the integer `a'` divides `c-d`.  But

```text
|c-d|<diameter(S)<min(S)<=a',
```

so `c=d`, and then `c'=d'`.  Interchanging rows and colors proves the same
injectivity at a fixed color-pair vertex.  Pair uniqueness removes a
possible duplicate carrier.  Therefore:

> **Residual matching lemma.** For every integer `h`, the supported matrix
> `H_h=1_(shift=h) H` is a weighted partial permutation.

This is stronger than saying merely that there are `O(D)` possible shifts.
It shows that the residual is a proper edge coloring of the actual `H`
graph.

## 3. Exact residual-modulation Bessel identity

Define

```text
H(theta)=sum_h exp(2*pi*i*h*theta) H_h.             (3.1)
```

Fourier orthogonality and the matching lemma give, for every pair vector
`v`,

```text
integral_0^1 ||H(theta)v||_2^2 dtheta
 =sum_h ||H_h v||_2^2.                              (3.2)
```

Each `H_h* H_h` is diagonal.  Since all entries have modulus at most one and
the proved geometric color-pair degree is `D q^o(1)`, (3.2) implies

```text
integral_0^1 ||H(theta)v||_2^2 dtheta
 <<D q^o(1)||v||_2^2.                               (3.3)
```

Substitution of `v_z` and (1.3) gives exactly (0.1).  This is the genuine
Moyal/Bessel statement available from the residual coordinate.

Unfortunately (1.2) is

```text
||H(0)v_z||_2^2.                                    (3.4)
```

A trigonometric polynomial with `O(D)` frequencies obeys only

```text
||H(0)v||_2^2
 <<D integral_0^1 ||H(theta)v||_2^2 dtheta,          (3.5)
```

which restores the unwanted `D^2` bound.  Positivity makes `theta=0` the
most dangerous, rather than a generic, modulation.

## 4. The complete affine Moyal identity

The same issue is visible exactly over `F_q`.  Let `P_(s,t)` be the
permutation matrix of

```text
x -> s*x+t,                 s!=0.                    (4.1)
```

Two affine graphs with the same slope are either identical or disjoint;
graphs of distinct slope meet once.  Therefore

```text
<P_(s,t),P_(u,v)>_HS = q     if (s,t)=(u,v),
                       0     if s=u and t!=v,
                       1     if s!=u.                (4.2)
```

Writing `J/q` for the constant rank-one projection, (4.2) becomes

```text
<P_(s,t)-J/q,P_(u,v)-J/q>_HS
 =q*1_((s,t)=(u,v))-1_(s=u).                        (4.3)
```

Thus distinct slopes really are orthogonal after the constant mode is
removed.  Fourier transformation in the shift is even sharper.  For
`xi!=0`,

```text
W_(s,xi)=q^-1 sum_t exp(-2*pi*i*xi*t/q) P_(s,t)
        =|chi_(xi*s)><chi_xi|.                       (4.4)
```

The `W_(s,xi)` are orthonormal Fourier matrix units.  Equation (4.4) is the
literal affine Moyal identity sought in the phase-space proposal.

## 5. Why the actual mask destroys (4.4)

For fixed `(c,c',h)`, the matching lemma says that the actual carrier core
selects at most one point `(a,a')` of the complete line (1.5).  Its operator
atom is therefore

```text
E_(a,a')=D_a P_(s,t),                                (5.1)
```

where `D_a` is a one-point diagonal mask.  If several affine lines meet at
the same point, all their masked atoms (5.1) are the *same matrix unit*.
The cancellation in (4.3) used the other `q-1` points of each complete line;
those points are absent from the carry core.  Equivalently, a one-point mask
has flat Fourier spectrum along the line.

This persists after literal constant-mode subtraction.  If `Delta` marked
lines meet at one point and `M` is their point-line synthesis matrix, then,
with `Pi=I-J/q`,

```text
sqrt(Delta)*(1-1/q)
 <=||(Pi tensor Pi)M||<=sqrt(Delta).                 (5.2)
```

Indeed every one of the `Delta` columns becomes the same vectorized matrix
`(Pi e_a)(Pi e_a')*`, of norm `1-1/q`.  Thus centering a complete affine
permutation and centering its singleton compression are radically different
operations.

The precise failed factorization can also be displayed.  For fixed slope
`s`, let `R_s(x,y)` be the binary mask of marked points.  Fourier transform
in the intercept gives a kernel of the form

```text
q^-1/2 sum_(x,y) R_s(x,y) conjugate(f(x)) g(y)
                  exp(-2*pi*i*xi*(x-s*y)/q).         (5.3)
```

The two endpoint Fourier factors in (4.4) reappear only when `R_s` has
rank-one form `alpha_s(x) beta_s(y)`.  A singleton-marked partial
permutation has the opposite behavior: its binary rank is essentially its
number of edges.

This is not a small technical discrepancy.  The intersections of the
masked lines are exactly the common-neighbor/four-cycle terms one is trying
to estimate.  Completing the lines proves orthogonality for a different,
much denser operator.

There is also modular aliasing: distinct rational slopes `c/c'` can agree
modulo `q`.  That only weakens the finite-field orthogonality further; it is
not the main loss.

## 6. Sharp tensor-square zero-mode countermodel

The residual matching and tensor-square facts alone cannot control the zero
mode.  Take `n>=2` underlying colors and let

```text
m=n*(n-1)
```

index their ordered distinct pairs.  On two `m`-point vertex sets, decompose
`K_(m,m)` into its `m` cyclic perfect matchings `P_h`.  Thus every shift
layer is a matching and the maximum degree and number of shifts are both
`D=m`.

Take the normalized flat underlying color vector `z_c=n^-1/2`.  On every
ordered distinct pair,

```text
v_z(c,c')=1/n,
||v_z||_2^2=(n-1)/n.                                (6.1)
```

Exact calculation gives

```text
average_theta ||sum_h exp(2*pi*i*h*theta)P_h v_z||_2^2
 =(n-1)^2,                                          (6.2)

||sum_h P_h v_z||_2^2
 =n*(n-1)^3.                                        (6.3)
```

The zero-to-average ratio in (6.2)--(6.3) is exactly

```text
n*(n-1)=m=D,                                        (6.4)
```

and (6.3) exceeds the desired `D||z||_2^4` scale by `(n-1)^2`.
This is not an arithmetic carry counterexample.  It proves precisely that
proper residual edge coloring, bounded degree, and the tensor-square input
cone do not turn the averaged Moyal identity into a pointwise theorem.

## 7. Finite actual check and the remaining theorem

On the existing `q=25013`, cutoff-`12` actual fixture, the decomposition has

```text
H edges                         35,050
distinct residual shifts        2,015
residual range             [-2,620,2,620]
maximum left/right degree             4
violations of matching by h            0.             (7.1)
```

The large `h=0` layer has `3,998` edges but is itself a matching, as the
theorem requires.  These numbers merely replay the exact structure; they
are not asymptotic evidence.

An independent all-distinct-hyperedge audit gives the sharper point-mask
profile

| `q` | filtered pair terms | distinct affine lines | max marked-point multiplicity | centered point-line norm |
|---:|---:|---:|---:|---:|
| 25,013 | 31,052 | 31,052 | 4 | 1.99992017 |
| 50,021 | 97,424 | 97,424 | 4 | 1.99996007 |
| 100,003 | 261,248 | 261,248 | 4 | 1.99998002 |
| 200,003 | 755,012 | 755,012 | 5 | 2.23605680 |

The corresponding uncentered norms are exactly `2,2,2,sqrt(5)`.  Thus the
loss in (5.2) is numerically saturated to the displayed precision.  Across
fixed slopes, the sums of binary mask ranks divided by the filtered edge
counts are respectively

```text
0.99723, 0.99754, 0.99836, 0.99876.                  (7.2)
```

This rules out low-rank endpoint factorization as a description of these
fixtures.  The same conclusion survives the smooth carry weights: the
centered singleton-frame norm differs from the weighted marked-point norm
by at most the factor `1-1/q`.

The route would close FC if one proved the actual-mask restriction estimate

```text
||H(0)v_z||_2^2
 <<q^o(1) integral_0^1 ||H(theta)v_z||_2^2 dtheta   (7.3)
```

uniformly in `z`.  Together with (3.3), (7.3) gives the desired
`D q^o(1)||z||_2^4`.  But (7.3) says exactly that the actual prime-power
mask excludes coherent zero-mode Latin blocks.  It must use the joint
prime/reciprocal carrier constraint; neither affine Moyal nor an unmasked
determinant/Hecke completion supplies it.

Executable exact checks are in
`src/qp_four_cycle_residual_moyal.py` and
`src/test_qp_four_cycle_residual_moyal.py`.

```text
residual layers are partial matchings:              PROVED;
averaged residual Moyal/Bessel identity:             PROVED;
complete affine Fourier matrix-unit identity:        PROVED;
zero-mode loss can equal D on tensor-square inputs:  PROVED;
actual-mask zero-mode restriction (7.3):             OPEN;
new FC exponent from this transform alone:           NO.
```
