# QP calibrated signed cubic: carrier-projection no-go

**Date:** 2026-08-15  
**Verdict:** calibration and carrier projection, by themselves, do not give
a power saving over the `49/66` transverse exponent.  There is an exact
formal moment model which simultaneously has

```text
lambda dot v=0,
v=a_*+(1/2)q,             a_* in {+1,-1}^M,
||v||_2 asyp sqrt(M),
|mu_3(y)|<=sqrt(Delta)||y||_2^3,                    (0.1)
```

yet for one signed, rank-one-tested direction

```text
J_v(y):={[-y dot v]/sqrt(V_y)}
        {1+max(0,-mu_3(y)/V_y^(3/2))}
 >=(9/32)sqrt(M Delta).                             (0.2)
```

Here `Delta=1+Y^2/B`.  With `M=Y^(1+o(1))` and `B=Y^A`, (0.2) has exponent

```text
1/2+(2-A)/2=(3-A)/2,                               (0.3)
```

which is `49/66` at `A=50/33`.

The obstruction preserves the sign of the cubic moment and its rank-one
form `T(y,y,y)`; it does not pass through unsigned Schur estimates.  Its
mechanism is a direct sum: the carrier direction supplies full leverage,
while an orthogonal calibrated-null direction supplies the negative skew.

This is **not** an actual-prime-log counterexample and does not prove the
true actual-node exponent optimal.  It rigorously rules out a saving based
only on:

1. the calibration identity;
2. the separate carrier leverage bound;
3. the separate signed cubic tensor bound; and
4. an orthogonal carrier/null decomposition.

An actual saving must prove a coupling which forbids this direct-sum
geometry for the prime-log feature curve.

---

## 1. The calibrated phase vector

Let `M` be divisible by four.  Take a phase vector `a_*` with `M/4` entries
equal to `+1` and `3M/4` entries equal to `-1`, and put

```text
D=1/2,
v=a_*+Dq.                                            (1.1)
```

Thus `v` has `M/4` entries `3/2` and `3M/4` entries `-1/2`.  For the uniform
probability

```text
lambda=M^(-1)q                                      (1.2)
```

one has exactly

```text
lambda dot a_*=-1/2=-D,
lambda dot v=0.                                     (1.3)
```

This is the algebraic calibration produced by a negative canonical event.
Moreover

```text
||v||_2^2=3M/4.                                     (1.4)
```

Define the orthonormal carrier and calibrated-null directions

```text
r=v/||v||_2,
z=q/sqrt(M).                                        (1.5)
```

Equation (1.3) gives `r dot z=0`.  Notice that the calibration probability
is parallel to `z`, not to the carrier `r`.

---

## 2. An exact signed rank-one cubic model

Fix `1<=Delta=o(M)` and write `S=sqrt(Delta)`.  Let `R` be a symmetric
Rademacher variable.  Independently, let `Z` be the standardized mean-zero
two-point variable with

```text
E Z=0,       E Z^2=1,       E Z^3=-S.               (2.1)
```

For completeness, take

```text
p={1+S/sqrt(S^2+4)}/2,
Z= sqrt((1-p)/p)             with probability p,
Z=-sqrt(p/(1-p))             with probability 1-p. (2.2)
```

Now use the random feature vector

```text
A=Rr+Zz.                                             (2.3)
```

For a coefficient vector `y=cr+sz`, put `F_y=y dot A`.  Independence and
(2.1) give the exact centered moments

```text
V_y=E F_y^2=c^2+s^2,
mu_3(y)=E F_y^3=-sqrt(Delta)s^3.                    (2.4)
```

Thus the cubic tensor is not replaced by its absolute majorant: it is the
signed rank-one tensor

```text
T=-sqrt(Delta) z tensor z tensor z.                 (2.5)
```

Its operator norm is exactly `sqrt(Delta)`.

The model can also be kept coordinate-bounded in the active two-dimensional
span.  The carrier coordinates are `O(M^-1/2)`, and the larger atom of `Z`
has size `O(sqrt(Delta))`; hence every coordinate of (2.3) is `o(1)` when
`Delta=o(M)`.  The obstruction is therefore not caused by an unbounded
single coordinate.

---

## 3. Exact saturation after carrier projection

Choose

```text
y=-(1/2)r+(sqrt(3)/2)z.                             (3.1)
```

Then `V_y=1`, and because `z dot v=0`,

```text
-y dot v=(1/2)||v||_2=sqrt(3M)/4.                  (3.2)
```

The negative standardized skewness is

```text
Gamma_-(y)=-mu_3(y)
 =(3sqrt(3)/8)sqrt(Delta).                          (3.3)
```

Consequently

```text
J_v(y)
 =sqrt(3M)/4 {1+(3sqrt(3)/8)sqrt(Delta)}
 >=(9/32)sqrt(M Delta).                             (3.4)
```

This uses a fixed nonzero component in each orthogonal summand.  Making the
carrier polynomial itself symmetric or proving small carrier skewness does
not help: the calibrated-null component retains a fixed share of the
variance and carries the entire negative cubic moment.

---

## 4. What an actual theorem must add

For the actual prime-log curve, define as before

```text
L_v(y)=[-y dot v]_+/V_y^(1/2),
Gamma_-(y)=max(0,-mu_3(y)/V_y^(3/2)).               (4.1)
```

The desired fixed saving is a genuinely joint assertion

```text
L_v(y)[1+Gamma_-(y)]
 <=Y^(49/66-eta+o(1))             for every y.      (4.2)
```

Equations (1.1)--(3.4) show that (4.2) does not follow formally from

```text
lambda dot v=0,
L_v(y)<<sqrt(M),
Gamma_-(y)<<sqrt(Delta).                            (4.3)
```

Nor does projection onto the Riesz carrier suffice unless one proves that
the orthogonal complement cannot contain a high-negative-skew direction.
The missing actual-node input can be stated precisely as either:

```text
Gamma_-(y_perp)<=Y^((2-A)/2-eta)
```

uniformly on the carrier-null space, or a tradeoff which forces
`L_v(y)` below `sqrt(M)` whenever `Gamma_-(y)` is large.  Either statement
must use the arithmetic relation between the actual prime-log packets and
the calibrated long event; covariance geometry alone cannot prove it.

---

## 5. Scope

```text
exact calibration lambda dot v=0:                   RETAINED;
bounded phase vector v=a_*+(1/2)q:                  RETAINED;
signed cubic, evaluated as T(y,y,y):                RETAINED;
carrier/null orthogonality:                         RETAINED;
formal J_v >=(9/32)sqrt(M Delta):                   PROVED;
power saving from the four listed separate axioms:  FALSE;
actual-prime rank-one/calibrated coupling saving:   OPEN;
actual exponent below 49/66:                        NOT PROVED;
LTRAD_full, QP, QP-to-strip, or a uniform strip:    NOT PROVED.
```

Executable exact checks:

```bash
python3 -m pytest -q src/test_qp_calibrated_cubic_projection_nogo.py
```
