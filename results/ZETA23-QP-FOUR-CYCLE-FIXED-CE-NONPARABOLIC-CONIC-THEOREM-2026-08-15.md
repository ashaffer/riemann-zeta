# QP four-cycle: fixed `(C,E)` nonparabolic conic theorem

**Date:** 2026-08-15  
**Verdict:** a nonzero fixed pair-completion difference cannot carry a
large tangent family.  More precisely, at the active QP scale, for every
fixed oriented color matrix `C` and every fixed nonzero realized product
difference `E`, the number of ordered completion pairs realizing `(C,E)`
is `q^o(1)`.

The point is an exact invariant.  The possible first product matrices form
an affine integral conic.  Its two points at infinity have discriminant
`-k det(E)`, where `k=det(C)`.  Both factors are nonzero in the generic
actual-shell sector, so the conic is never parabolic.  Its full degeneracy
parameter is `L^2+k det(E)`, which is also nonzero at the active scale.
An elementary divisor/Pell count then gives the asserted subpolynomial
multiplicity.

This proves the previously open **generic realized-`(C,E)` multiplicity
theorem**.  It does not by itself prove the global weighted pair-energy
bound: one must still sum the distinct realized secants `E`, especially in
the rational tangent-plane branch.

---

## 1. Two rank-one equations become one plane

Write

```text
K=( c11 -c12; -c21 c22),       k=det K=det C,       (1.1)
```

and use the coefficient pairing

```text
<K,M>=sum_ij Kij Mij.                                 (1.2)
```

Fix a color matrix `C`, its pinned integral level `L`, and two distinct
completions.  Their product matrices satisfy

```text
M=a b^T,                 M'=a' b'^T,
E=M-M',                  Delta=det E !=0,
<K,M>=<K,M'>=L.                                      (1.3)
```

The nonvanishing of `Delta` is the already proved actual-shell Sidon
lemma for two distinct completions.  Since `det M=0`, the second rank-one
condition expands exactly as

```text
det(M-E)=det M-<adj(E)^T,M>+det E=0,
<adj(E)^T,M>=Delta.                                  (1.4)
```

Thus, for fixed `(C,E,L)`, all possible `M` lie on `det M=0` inside two
fixed integral affine planes, (1.3) and (1.4).  This is an affine conic,
not a four-variable product box.

---

## 2. Canonical idempotent coordinates

Put

```text
R=E^(-1) M.                                          (2.1)
```

Then

```text
det R=0,                 det(R-I)=0,
tr R=1,                  R^2=R.                     (2.2)
```

The last identity follows from the characteristic polynomial.  Define

```text
A=K^T E.                                              (2.3)
```

The common-level equation for `E` gives

```text
tr A=<K,E>=0,                 det A=k Delta.          (2.4)
```

Write

```text
A=( alpha beta; gamma -alpha),
R=( x y; z 1-x).                                     (2.5)
```

After putting `X=2x-1`, equations (2.2) and (1.3) become

```text
X^2+4 y z=1,
alpha X+gamma y+beta z=L.                            (2.6)
```

This already displays the exact geometry.  The quadratic part after
eliminating one coordinate has discriminant

```text
16(alpha^2+beta gamma)=-16 k Delta !=0,              (2.7)
```

because

```text
alpha^2+beta gamma=-det A=-k Delta.                  (2.8)
```

Equivalently, the two points at infinity are governed invariantly by

```text
det(K-lambda adj(E)^T)=k+Delta lambda^2.             (2.9)
```

Here the absent linear coefficient is exactly `<K,E>=0`.  Since both
`k` and `Delta` are nonzero, (2.9) has two distinct geometric roots.  In
particular the fixed-`E` conic has no parabolic tangent-at-infinity branch.

For integrality, no rational denominator needs to be ignored.  Set

```text
T=adj(E) M,
X0=T11-T22,                 Y0=T12,       Z0=T21.    (2.10)
```

All three variables are integers, and multiplying (2.6) by `Delta^2`
gives

```text
X0^2+4 Y0 Z0=Delta^2,
alpha X0+gamma Y0+beta Z0=L Delta.                  (2.11)
```

The map `M -> T -> (X0,Y0,Z0)` is injective because `E` is invertible.

---

## 3. The full conic is nondegenerate

Assume first `beta!=0` and eliminate `Z0` from (2.11).  One obtains

```text
beta X0^2-4 alpha X0 Y0-4 gamma Y0^2
       +4 L Delta Y0-beta Delta^2=0.                (3.1)
```

The determinant of the homogenized ternary quadratic matrix is a nonzero
constant times

```text
N=L^2+k Delta.                                       (3.2)
```

The same invariant results after swapping `Y0,Z0` if `beta=0,gamma!=0`.
If both vanish, then `alpha!=0`, the second equation in (2.11) fixes `X0`,
and the first is directly a nonzero divisor equation in `Y0 Z0`.

For completeness, (3.2) is also the cross-level invariant.  If

```text
A0=det(a,a'),               B0=det(b,b'),
Xc=a^T K b',                Yc=a'^T K b,             (3.3)
```

then

```text
Delta=-A0 B0,
L^2-Xc Yc=k A0 B0,
Xc Yc=L^2+k Delta=N.                                 (3.4)
```

At the active scale, residual pinning gives

```text
|L| asymp |k| q,                                     (3.5)
```

whereas the short pair determinants give

```text
|Delta|<<D^2,                   1<=|k|<<D.            (3.6)
```

Consequently

```text
|k Delta|<<D^3=o(q^2)<=o(L^2),                       (3.7)
```

because `D=q^(16/33+o(1))`.  Hence `N!=0` for all sufficiently large `q`.
The affine conic is therefore nondegenerate as well as nonparabolic.

---

## 4. Uniform integral-point count

We record the elementary counting input in the precise form needed here.

### Lemma 4.1 (nonparabolic integral conic)

Let

```text
F(U,V)=a U^2+b U V+c V^2+d U+e V+f                 (4.1)
```

have integer coefficients of size at most `q^O(1)`.  Suppose its quadratic
discriminant and its full projective determinant are both nonzero.  Then
the number of integral zeros with `|U|+|V|<=q^O(1)` is `q^o(1)`.

**Proof.**  After an integral interchange or shear, assume `a!=0`.  Put

```text
delta=b^2-4ac,
U1=2aU+bV+d,
l=2bd-4ae,                 n=d^2-4af.               (4.2)
```

On `F=0`, direct completion of squares gives

```text
V1^2-4 delta U1^2=R,
V1=2 delta V+l,            R=l^2-4 delta n.          (4.3)
```

The two nondegeneracy assumptions say `delta R!=0`.  Remove the square
part of `4 delta`.  If the remaining quadratic discriminant is a square,
(4.3) factors and the number of solutions is bounded by a divisor function
of `R`.  Otherwise (4.3) is a norm equation in a quadratic order.  The
ideal generated by a solution divides `(R)`; there are
`tau(|R delta|)^O(1)=q^o(1)` possible ideal divisors.  Solutions generating
one ideal differ by a unit.  Imaginary quadratic orders have finitely many
units, while in the real case only `O(log q)` unit powers have polynomial
height.  This proves the lemma.  The linear changes in (4.2) are injective,
so dropping their congruence conditions only enlarges the count.  QED

Apply Lemma 4.1 to (3.1).  Its quadratic discriminant is (2.7), and its
full determinant is nonzero by (3.2)--(3.7).  Every coefficient, every
coordinate in (2.11), and the resulting norm right side have size
`q^O(1)`.  Therefore

```text
#{M: det M=det(M-E)=0, <K,M>=L, M in the product box}
       <<q^o(1).                                     (4.4)
```

---

## 5. Returning from product matrices to carriers

An actual product matrix `M=a b^T` has only `O(1)` oriented shell
factorizations.  Indeed, `M11=a1*b1`; multiplicative Sidonicity of the
narrow prime-power shell determines the unordered pair `{a1,b1}`.  Once
its orientation is chosen,

```text
b2=M12/a1,                    a2=M21/b1              (5.1)
```

are forced.  Thus `M` has at most two carrier factorizations, and the same
holds for `M-E`.  Combining this with (4.4) proves:

### Theorem 5.1 (fixed `(C,E)` multiplicity)

For every all-distinct actual-shell color matrix `C` at the active scale
and every nonzero realized pair difference `E`,

```text
nu(C,E)
=#{(completion,completion'): M-M'=E}
<<q^o(1).                                             (5.2)
```

This theorem is sharp at the qualitative level: the full-integer finite
ledger has a fixed `(C,E)` collision of multiplicity four.  What it rules
out is polynomial growth, including a hidden `sqrt(D)` family at one fixed
nonzero secant.

---

## 6. Exact consequence and remaining gate

For a fixed `C`, let `mathcal E(C)` be the nonzero realized difference
matrices.  Theorem 5.1 gives

```text
m(C)(m(C)-1)
 =sum_(E in mathcal E(C)) nu(C,E)
 <<q^o(1) #mathcal E(C).                            (6.1)
```

Thus the generic successive-minima branch, where the short common-level
lattice has only `O(D)` vectors, satisfies

```text
m(C)<<D^(1/2) q^o(1).                               (6.2)
```

More importantly, the earlier generic-branch gap is now removed: counting
short `E` values really does count completion pairs up to `q^o(1)`.

What remains for the full four-cycle theorem is a **weighted global count
of the distinct realized secants**.  The bare pointwise `O(D)` in (6.1)
cannot be multiplied by the already proved `O(D)` weighted color mass.
The exceptional rational-plane branch likewise needs its tangent patches
grouped with bounded weighted color reuse.

```text
fixed-(C,E) nonparabolic conic:                    PROVED;
fixed-(C,E) multiplicity q^o(1):                   PROVED;
generic E-value count O(D):                        PREVIOUSLY PROVED;
generic fixed-C multiplicity sqrt(D) q^o(1):       PROVED COMBINED;
weighted distinct-secant sum O(D):                 OPEN;
full weighted pair-energy / FC:                    OPEN.
```
