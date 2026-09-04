# QP diagonal calibration: quartic reduction and positive-carry gate

**Date:** 2026-08-15  
**Verdict:** repeating one real coefficient vector in all three cubic slots
and retaining the separator sign does not, by itself, lower the proved cubic
scale.  After covariance whitening, the hard joint factor is exactly the
positive part of the even quartic

```text
Q_a(x)=(a dot x) T(x,x,x).                            (0.1)
```

Its four-linear tensor is merely the symmetrized rank-one product
`a sym_tensor T`; it contains no new four-node carry equation.  Calibration
places one known vector in `a^perp`, but creates no contraction between the
new linear slot and the three arithmetic cubic slots.

There is also an actual-support signed barrier.  For an exactly calibrated
singleton residual with `D=1`, every separator coordinate is nonnegative.
On every entrywise-nonnegative symmetric carry core on the actual prime-power
nodes, changing a nonnegative vector `x` to `-x` makes it a legal separating
vector and changes the cubic to the required negative sign.  The legal
negative diagonal norm is therefore exactly the unrestricted diagonal norm.
Polarization makes that norm equivalent, within the absolute factor `9/2`,
to the three-independent-vector norm.

Thus a stronger theorem must exploit cancellation between the positive carry
core and the signed remainder, or prove an actual arithmetic alignment bound
for (0.1).  Symmetry, diagonalization, the half-space sign, and scalar
calibration alone do not supply a power gain.  No exponent below `49/66`, no
QP result, and no strip result is proved here.

---

## 1. Exact diagonal form of the calibrated problem

Work on the nondegenerate covariance range.  Let `Sigma` be the covariance
of the actual centered prime-log features, choose a whitening map `W` with

```text
W^T Sigma W=I,
y=Wx,
a=W^T v,                                               (1.1)
```

and let the actual centered cubic become the real symmetric form

```text
P(x)=Ttilde(x,x,x),          ||x||_2=1.               (1.2)
```

On the active branch of the cubic endpoint argument,

```text
L=-a dot x>0,                 g=-P(x)>0,
L Gamma_-=L g=(a dot x)P(x).                           (1.3)
```

Since both linear and cubic forms are odd, their product is even.  Therefore

```text
sup_(||x||=1,a dot x<0,P(x)<0) (-a dot x)(-P(x))
 =max_(||x||=1) [(a dot x)P(x)]_+.                     (1.4)
```

Here and below the left-hand supremum is defined to be `0` if the active
set is empty.  Equivalently, one may use the closed inequalities and take
the positive part of the displayed product.  This convention is the one
relevant to the endpoint bound, where an absent negative-skew branch costs
nothing.

Indeed, whenever the product on the right is positive, the two factors have
the same sign.  If both are positive, replace `x` by `-x`; both then become
negative without changing their product.  Equation (1.4) keeps the diagonal
coefficient constraint and both one-sided signs exactly.

The symmetric four-linear form associated with (1.4) is

```text
S_a(x1,x2,x3,x4)
 =1/4 sum_(r=1)^4 (a dot xr)
      Ttilde(x1,...,omit xr,...,x4),                    (1.5)
```

so `S_a(x,x,x,x)=Q_a(x)`.  In coefficient indices,

```text
(S_a)_(i,j,k,l)
 =1/4[a_i T_(j,k,l)+a_j T_(i,k,l)
      +a_k T_(i,j,l)+a_l T_(i,j,k)].                   (1.6)
```

This is the exact reason a proposed four-node carry estimate does not appear
automatically: the fourth index is separable.  All arithmetic incidence is
still confined to the original three indices of `Ttilde`.

If `lambda dot v=0`, then in whitened coordinates the corresponding vector
`b=W^(-1)lambda` obeys

```text
b dot a=lambda dot v=0.                                (1.7)
```

Thus calibration identifies one vector in the equator of the linear factor.
It does not make (1.5) vanish, and it supplies no bound on the restriction of
`Ttilde` to that equator or on the positive quartic (1.4).

The exact target for an improved calibrated theorem is consequently

```text
max_(||x||=1)[Q_a(x)]_+
 <<sqrt(M) Delta^(1/4+o(1)),                           (1.8)
```

or a stronger bound, with `a` and `Ttilde` coming from the same actual
prime-power frame.  Separate estimates
`||a||<<sqrt(M)` and `||Ttilde||<<sqrt(Delta)` return only
`sqrt(M Delta)`.

---

## 2. Symmetric diagonal and independent norms have the same power scale

Let `T` be any real symmetric trilinear form on a Hilbert space, and put

```text
C_diag=sup_(||x||=1)|T(x,x,x)|,
C_tri =sup_(||x_i||=1)|T(x_1,x_2,x_3)|.             (2.1)
```

The real polarization identity is

```text
T(x_1,x_2,x_3)
 =1/48 sum_(eps_i in {+1,-1})
   eps_1 eps_2 eps_3
   P(eps_1 x_1+eps_2 x_2+eps_3 x_3).               (2.2)
```

For unit vectors, (2.2) and the triangle inequality give

```text
C_diag<=C_tri<=(9/2)C_diag.                          (2.3)
```

The upper constant follows from
`8*3^3/48=9/2`.  More generally one may first rescale the three inputs and
minimize `(alpha+beta+gamma)^3/(6 alpha beta gamma)`; the minimum is again
`9/2`.

Thus the use of one repeated coefficient vector cannot by itself improve a
power exponent in a coefficient-uniform cubic estimate.  It can change only
an absolute constant.  A power gain must use the sign in (1.4), the special
arithmetic entries of `T`, or both.

---

## 3. The positive actual carry core survives the separator

The compact high-time law used in the clustered moment argument has cosine
transform

```text
C_B(omega)=cos(B omega/2)sinc(B omega/(6q_0))^q_0. (3.1)
```

Fix `0<c_0<pi`.  For every signed triple frequency with
`|B omega|<=c_0`, its contribution in (3.1) is nonnegative.  Keeping only
these contributions and symmetrizing the three coefficient indices defines
an entrywise-nonnegative symmetric **carry-core tensor** `T_core` on the
same actual prime-power node set.  It includes, in particular, the balanced
relation

```text
|8abc-q^3|<<q^3/B                                  (3.2)
```

inside a smaller fixed core window.  This truncation is used only for the
following method audit; the signed remainder is not discarded from the
actual cubic theorem.

Choose an actual node `p` and a legal odd resonance

```text
t_0=(2k+1)pi/|log(p/Y)|,            D=1,
lambda=delta_p.                                          (3.3)
```

Then the actual residual

```text
v_n=1+cos(t_0 log(n/Y))>=0,
lambda dot v=v_p=0.                                    (3.4)
```

Assume `v` is nonzero, as it is for any nontrivial selected residual.  For
`P_core(x)=T_core(x,x,x)`, define

```text
C_core=sup_(||x||=1)|P_core(x)|,
C_core^-(v)=sup_(||y||=1,y dot v<0)[-P_core(y)]_+.  (3.5)
```

### Proposition 3.1

For (3.4),

```text
C_core^-(v)=C_core.                                    (3.6)
```

#### Proof

Entrywise nonnegativity gives

```text
|P_core(x)|<=P_core(|x|),                              (3.7)
```

so the unrestricted diagonal supremum is approached by nonnegative vectors.
For such an `x`, put `y=-x`.  Then

```text
P_core(y)=-P_core(x),              y dot v<=0.          (3.8)
```

If `x dot v>0`, the separator is strict.  If `x dot v=0`, add an arbitrarily
small nonnegative component on any coordinate where `v_n>0`, renormalize,
and pass to the limit.  This proves `C_core^-(v)>=C_core`; the reverse
inequality is immediate.  QED

Together with (2.3), Proposition 3.1 says that, on this actual calibrated
residual, the legal signed diagonal norm of the positive carry core is
equivalent within `9/2` to its three-vector norm.  This statement does **not**
assert that the actual core norm is `>>sqrt(R)`.  It proves exactly that
diagonalization and separator orientation cannot be used to improve whatever
arithmetic norm the positive core has.

The full centered cubic also contains the complementary frequency windows,
other sign patterns, and negligible mean corrections.  They may cancel the
core for a given vector.  Proposition 3.1 therefore blocks only proofs which
majorize the core and remainder separately; it does not rule out the desired
signed cancellation theorem.

---

## 4. What remains genuinely stronger

The diagonal/calibrated escape is now reduced to one of two actual-node
statements:

1. a direct positive-quartic estimate for `Q_a` in (1.4), using the common
   origin of `a` and `Ttilde`; or
2. cancellation between `T_core` and the signed cubic remainder strong
   enough to beat the positive-core norm on every legal separator.

Neither follows from a four-node incidence count, because (1.6) factorizes.
Neither follows from symmetry, by (2.3).  Scalar calibration gives only
(1.7), and the exact signed formal model in the earlier carrier-projection
report shows that this orthogonality plus the separate norm bounds can
saturate `sqrt(M Delta)`.

At the active aperture,

```text
M=Y^(1+o(1)),              Delta=Y^(16/33+o(1)),
separate quartic scale     sqrt(M Delta)=Y^(49/66+o(1)),
desired quarter scale      sqrt(M)Delta^(1/4)=Y^(41/66+o(1)). (4.1)
```

No estimate lowering the first line to the second has been proved for the
full actual tensor.

---

## 5. Binary disposition

```text
exact one-sided quartic identity (1.4):              PROVED;
four-linear factorization a sym_tensor T:            PROVED;
new four-node carry relation from calibration:       NO;
diagonal/trilinear equivalence within 9/2:            PROVED;
actual singleton calibration with v>=0:              PROVED;
legal negative core norm equals full core norm:       PROVED;
actual carry-core saturation at sqrt(R):              NOT PROVED;
core/remainder signed cancellation saving:            OPEN;
calibrated positive-quartic bound at quarter scale:    OPEN;
full-shell exponent below 49/66:                       NOT PROVED;
QP or uniform strip:                                   NOT PROVED.
```

Executable checks:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_diagonal_calibration_quartic_gate.py
```

The tests replay the quartic sign orientation, the symmetric
four-linear factorization, the polarization identity and `9/2` constant,
and the positive-core singleton barrier.
