# QP balanced band-pass: partial-permutation spectral inverse

**Date:** 2026-08-15  
**Verdict:** the coherence-length decomposition does not yet prove a power
saving, but the signed balanced tensor admits an exact spectral reduction
which is sharper than the earlier unsigned `TT*` reduction.  After a
Schwartz truncation, the tensor is a color combination of
partial-permutation matrices with disjoint Hilbert--Schmidt supports.

Two positive structural statements follow.

1. Near saturation of the `sqrt(R)` Schur bound forces the **same** dual
   vectors to generate a Frobenius-near rank-one, weighted partial-Latin
   core.
2. The proposed `R^(1/4+o(1))` bound follows from one explicit signed
   nondegenerate four-cycle estimate of size `R q^o(1)`.

The four-cycle estimate itself is not proved here.  Thus this is an exact
inverse/reduction theorem, not a balanced tensor saving, QP, or a strip.

---

## 1. Truncated band-pass matrices

Let

```text
q be an odd prime,             Y=q/2,
B=Y^A,                         3/2<A<2,
R=q^2/B=q^(2-A+o(1)),
K(a,b,c)=W(B log(abc/Y^3)),                         (1.1)
```

where `W` is a fixed Schwartz function.  Fix a small `delta>0` and truncate
to

```text
|B log(abc/Y^3)|<=U,             U=q^delta.         (1.2)
```

For `delta<A-1`, varying one integer coordinate while fixing the other two
changes the argument in (1.1) by `asymp B/q>>U`.  Consequently every two
coordinates determine at most one third coordinate in (1.2).

For each `c`, define the matrix

```text
(P_c)_(a,b)=K(a,b,c) 1_(1.2).                      (1.3)
```

It is a weighted partial permutation: every row and every column has at
most one nonzero entry.  Moreover the supports of distinct `P_c` are
disjoint as subsets of the `(a,b)` matrix entries.  For fixed `c`, the
integer product `ab` lies in an interval of length `O_w(UR)`.  Bounded
prime-power product multiplicity therefore gives

```text
d_c:=||P_c||_F^2<<_w UR=:D.                        (1.4)
```

Normalize `||W||_infinity<=1`; a fixed constant otherwise propagates
harmlessly.  For `z=(z_c)` put

```text
A_z=sum_c z_c P_c.                                 (1.5)
```

The truncated trilinear form is naturally `x^T A_z y`.  Replacing `x` by
its complex conjugate writes it as `x^*A_z y` without changing any
independent-slot norm; on the real diagonal cubic the two forms coincide.

The discarded Schwartz tail is smaller in the pair-to-node Schur norm.
Indeed, outside (1.2), the one-node fibre has mass `O_N(U^-N)`, while the
fixed-node pair fibre has mass `O_(w,N)(R U^(1-N))`.  Hence

```text
||K_tail||_(2->2)
 <<_(w,N) sqrt(R) U^((1-2N)/2).                    (1.6)
```

For any desired final `q^epsilon` loss, first choose `delta` sufficiently
small and then fixed `N` sufficiently large.  It is therefore enough for
power-exponent purposes to prove the core estimate uniformly in (1.2).

---

## 2. Exact Hilbert--Schmidt and spectral identities

Disjoint entry supports give

```text
<P_c,P_d>_HS=0                         (c!=d),
||A_z||_F^2=sum_c |z_c|^2 d_c<=D||z||_2^2.         (2.1)
```

This is an equality before the last inequality, not a Schur estimate.
For unit `x,y,z`, write

```text
t=|x^*A_z y|,                  s=||A_z||_op.       (2.2)
```

Then the following defect decomposition is exact:

```text
D-t^2
 =(D-||A_z||_F^2)
  +(||A_z||_F^2-s^2)
  +(s^2-t^2).                                      (2.3)
```

Every term on the right is nonnegative.  After multiplying `A_z` by a
unit scalar so that `x^*A_z y=t`, there is also the exact endpoint identity

```text
||A_z-t x y^*||_F^2=||A_z||_F^2-t^2.              (2.4)
```

Equations (2.1)--(2.4) retain the signed color combination which was lost
in the unsigned near-product-energy argument.

### Near-saturation inverse theorem

If

```text
t>=(1-epsilon)sqrt(D),                             (2.5)
```

then, with `delta_e=2epsilon-epsilon^2`,

```text
D-||A_z||_F^2<=delta_e D,
||A_z-t x y^*||_F^2<=delta_e D.                   (2.6)
```

Let `E` be the projection of the truncated triples to their `(a,b)`
pairs.  Since `A_z` vanishes off `E`, (2.4) also yields

```text
sum_((a,b) notin E)|x_a|^2|y_b|^2
 <=delta_e/(1-epsilon)^2.                          (2.7)
```

Thus near saturation forces the actual pair projection to capture almost
all of the product probability `|x|^2 tensor |y|^2`, and on that projection

```text
z_(c(a,b)) K(a,b,c(a,b))
```

is Frobenius-close to the rank-one matrix `t x_a conjugate(y_b)`.
This is a precise weighted coherent partial-Latin core.

The partial-Latin property in all three coordinate pairs gives one further
necessary condition.  Holding `a` fixed, the incident `(b,c)` relation is a
matching, so its bilinear form has norm at most one.  Hence

```text
t<=min(||x||_1,||y||_1,||z||_1),                  (2.8)
```

and (2.5) forces every coefficient vector to have support at least
`(1-epsilon)^2D`.  At coherence length `L=sqrt(R)`, such a core must occupy
at least `sqrt(R)` integer blocks in every coordinate.

This theorem does not promote weighted density to a literal unweighted
complete Latin subsquare; that additional promotion would require a new
arithmetic input.

---

## 3. The exact fourth-trace target

The operator norm obeys

```text
||A_z||_op^4<=tr((A_z^*A_z)^2).                   (3.1)
```

Expanding the trace gives the signed ordered rectangle identity

```text
tr((A_z^*A_z)^2)
 =sum_(a1,a2,b1,b2)
   conjugate(A_(a1,b1)) A_(a1,b2)
   conjugate(A_(a2,b2)) A_(a2,b1).                (3.2)
```

For unit `z`, every row and every column of `A_z` has squared `ell^2` norm
at most one: a fixed `(a,c)` or `(b,c)` pair occurs at most once.  Therefore
the part of (3.2) with `a1=a2` has mass at most `D`, and the part with
`b1=b2` has mass at most `D`.  If `Q_nd(z)` denotes the remaining signed
sum with both inequalities strict, then

```text
tr((A_z^*A_z)^2)<=2D+|Q_nd(z)|.                   (3.3)
```

It follows immediately that the single estimate

```text
|Q_nd(z)|<<_(w,epsilon)D q^epsilon
for every ||z||_2=1                               (FC)
```

implies

```text
||A_z||_op<<_(w,epsilon)D^(1/4)q^(epsilon/4)
          =R^(1/4)q^O(epsilon).                   (3.4)
```

Together with (1.6), this is the desired
`R^(1/4+o(1))` coefficient-uniform balanced tensor estimate.

The arithmetic content of `(FC)` is explicit.  The four incident triples
in a nondegenerate rectangle satisfy

```text
|log(c11 c22/(c12 c21))|<=4U/B,
|c11 c22-c12 c21|<<_w U q^2/B=UR=D.               (3.5)
```

Thus `(FC)` is a signed, arbitrary-weight near-determinant theorem on the
actual prime-power colors, with the two `a,b` completion coordinates still
present.  It is strictly more structured than the unsigned near-product
energy already known to be large.

An abstract Latin square shows that `(FC)` is not formal.  On a group of
order `D`, take `c=-a-b` and `z_c=D^(-1/2)`.  Then `A_z` is the constant
matrix `D^(-1/2)`, so

```text
||A_z||_F^2=D,
tr((A_z^*A_z)^2)=D^2,
||A_z||_op=sqrt(D).                                (3.6)
```

Actual prime-power arithmetic must rule out precisely this coherent
four-cycle accumulation.

---

## 4. What the coherence-length calculation does and does not give

Put

```text
L=Y/sqrt(B)=sqrt(R) q^o(1).                        (4.1)
```

On an integer block `n=n_0+u`, `|u|<=L`, Taylor's theorem gives

```text
B log((n_0+u)/n_0)
 =B u/n_0-B u^2/(2n_0^2)+O_w(B L^3/Y^3),          (4.2)
B L^2/Y^2=1,                  B L^3/Y^3=B^(-1/2). (4.3)
```

So the quadratic phase is genuinely order one and the cubic error tends to
zero.  This validates the proposed wave-packet scale.

It does not by itself give almost orthogonality for arbitrary coefficients.
For a fixed residual Fourier variable `tau`, the complete phase is exactly

```text
exp(i tau B log(abc/Y^3))
 =const_tau exp(i tau B log a)
             exp(i tau B log b)
             exp(i tau B log c).                  (4.4)
```

All linear, quadratic, and higher Taylor terms in that Fourier slice are
single-coordinate phases and can be absorbed by diagonal unitary changes
of the three coefficient vectors.  The only possible uniform gain is
therefore cancellation between Fourier slices together with the actual
prime-power incidence mask.  Identity (3.2) packages exactly that surviving
interaction.

Here "band-pass" records the motivating high-time window.  The reduction
itself uses Schwartz localization and partial-permutation geometry; it does
not use or claim cancellation of a zero principal Fourier mode.

No bound for `Q_nd` beyond the old Schur scale is asserted here.

---

## 5. Binary status

```text
exact disjoint-support Frobenius identity:          PROVED;
near-Schur coherent-core inverse theorem:           PROVED;
exact signed nondegenerate four-cycle reduction:    PROVED;
coherence length L=sqrt(R) with cubic error o(1):   PROVED;
automatic block almost-orthogonality:               NO;
uniform bound (FC):                                 NOT PROVED;
balanced tensor norm R^(1/4+o(1)):                  NOT PROVED;
QP or a uniform strip:                              NOT PROVED.
```

Executable checks:

```bash
python3 -m pytest -q \
  src/test_qp_bandpass_partial_permutation_inverse.py
```
