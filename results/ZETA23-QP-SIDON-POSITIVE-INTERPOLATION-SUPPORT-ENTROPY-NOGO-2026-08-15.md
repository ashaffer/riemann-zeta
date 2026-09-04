# QP positive Sidon interpolation: exact support-entropy no-go

**Date:** 2026-08-15  
**Binary verdict:** the Florek/Fatou--Zygmund theorem does not produce a
fixed-power QP antipode on the polynomial band.  The actual centered
prime-power nodes (apart from at most one power of `2`) are rationally
independent and have a uniform *global* Sidon constant.  However, universal
positive interpolation on an interval of QP length has local interpolation
constant at least

```text
Y^(1/2-o(1)).
```

More sharply, retaining interpolation constant `C` forces support diameter

```text
exp[Omega(M/C^2)]/M,              M asymp Y/log Y.    (0.1)
```

Thus `C<=Y^.019` requires superpolynomial, indeed exponentially large,
support.  This kills the **universal positive-interpolation route** at the
target exponent.

It does **not** prove that the special all-negative target has the universal
interpolation cost.  The actual finite-band antipode and QP remain open.

The primary sources used are:

- J. Florek, [*Interpolation by the Fourier--Stieltjes transform of a
  positive compactly supported measure*](https://bibliotekanauki.pl/articles/722421.pdf),
  Colloq. Math. 54 (1987), 113--120,
  [DOI 10.4064/cm-54-1-113-120](https://doi.org/10.4064/cm-54-1-113-120);
- M. Dechamps--Gondim, [*Ensembles de Sidon topologiques*](https://www.numdam.org/article/AIF_1972__22_3_51_0.pdf),
  Ann. Inst. Fourier 22 (1972), 51--79,
  [DOI 10.5802/aif.424](https://doi.org/10.5802/aif.424).

Replay is in `src/qp_sidon_support_entropy.py`, with tests in
`src/test_qp_sidon_support_entropy.py`.

---

## 1. What Florek actually proves

Let `G` be an LCA group and `Lambda` a symmetric topological Sidon subset of
its dual, not containing the identity.  Florek's main theorem (pp. 113--114)
says that, given a compact set `K` associated with `Lambda`, a separation
neighborhood `U`, and `epsilon>0`, every bounded Hermitian function `Phi` on
`Lambda` is interpolated exactly by the Fourier--Stieltjes transform of a
positive measure `mu_Phi` satisfying

```text
supp(mu_Phi) subset 2K+K_1(C,U,epsilon),
||mu_Phi|| <= C_1(C)/epsilon.                         (1.1)
```

The support compact is independent of `Phi`.  The proof on pp. 117--118
first builds an approximate positive interpolant of norm

```text
16 C^4 ||Phi||_infinity / epsilon
```

and then sums a geometric correction sequence.  Its displayed estimates
give the explicit final bound

```text
||mu_Phi|| <= 32 C^4 ||Phi||_infinity / epsilon.     (1.2)
```

This is genuine positive interpolation, not merely a signed-measure result.
It is also genuinely compactly supported.

What the theorem does **not** give is a quantitative diameter for either the
associated compact `K` or the correction compact `K_1(C,U,epsilon)`.
Dechamps--Gondim proves that, for the connected time group `R`, every compact
interval with nonempty interior is associated with a topological Sidon set.
That theorem is existential: its interpolation constant can depend on the
interval and the frequency set.

This missing support/constant dependence is exactly where the QP aperture
enters.

---

## 2. The actual odd-base nodes are globally optimal Sidon frequencies

Fix the project width `w=.2`, an allowed center

```text
Y=a/2,                       a odd,
```

and prime powers `q=p^e` in `[Y exp(-w),Y exp(w)]`.  Since

```text
exp(2w)=exp(.4)<2,
```

there cannot be two different powers of the same prime base in one shell.
Delete the possible power of `2`; this removes at most one node.  All
remaining `q` are odd and have distinct prime bases.

### Lemma 2.1 (exact rational independence)

The centered frequencies

```text
v_q=log(q/Y)
```

and hence their absolute values `u_q=|v_q|` are linearly independent over
the rationals.

#### Proof

Suppose `sum_q k_q v_q=0` with integers `k_q`, and put `K=sum_q k_q`.
Exponentiating gives an identity of positive rationals

```text
2^K product_q q^(k_q)=a^K.                           (2.1)
```

Every `q` and `a` is odd.  The `2`-adic valuation of (2.1) gives `K=0`.
Unique factorization and the distinct prime bases of the `q` then give
`k_q=0` for every `q`.  Replacing `v_q` by `|v_q|` only changes the signs of
the integer coefficients.  QED

Let `m` be the number of retained nodes.  Kronecker density now gives

```text
t -> (exp(i t u_1),...,exp(i t u_m))
```

dense in the `m`-torus.  Therefore, for arbitrary complex coefficients,

```text
sup_(t in R) |sum_j c_j exp(i t u_j)|=sum_j |c_j|.   (2.2)
```

The asymmetric global Sidon constant is exactly `1`.  The symmetrized set
`{+/-u_j}` also has a universal Sidon constant: density reduces the problem
to independent `z_j` on the unit circle, and

```text
sup_z |sum_j (a_j z_j+b_j conjugate(z_j))|
 >=(1/2)sum_j(|a_j|+|b_j|).                          (2.3)
```

Indeed, choose a common direction, maximize each real part separately, and
average that direction; the circular mean of `|a+z b|` is at least
`max(|a|,|b|)>=(|a|+|b|)/2`.  Thus one may take global constant `2`.

So global Sidonicity is not the obstruction.  The obstruction is the first
compact interval on which this global phase freedom becomes available.

---

## 3. An exact local support-entropy theorem

For arbitrary real frequencies `|u_j|<=w` and an interval `I` of length
`L`, define the local Sidon constant

```text
C_I(u)=sup_(c != 0)
  [sum_j |c_j|] / [sup_(t in I)|sum_j c_j exp(i t u_j)|]. (3.1)
```

### Theorem 3.1 (random-sign local lower bound)

For every `m>=1`, `w>0`, and `L>=0`,

```text
C_I(u) >= m /
 [2 sqrt{m log(8(2+Lwm))}+1].                        (3.2)
```

#### Proof

Take independent Rademacher signs `epsilon_j`.  At a fixed height,
Hoeffding's inequality applied to real and imaginary parts gives

```text
P(|sum_j epsilon_j exp(i t u_j)|>=x)
 <=4 exp[-x^2/(4m)].                                 (3.3)
```

Put a grid on `I` of spacing at most `(wm)^(-1)`.  It has at most
`2+Lwm` points.  With

```text
x=2 sqrt{m log(8(2+Lwm))},
```

the union bound is strictly below `1`.  Hence one sign choice is bounded by
`x` on the grid.  Its trigonometric sum has derivative at most `wm`, so it
is bounded by `x+1` throughout `I`.  Substituting this coefficient vector
in (3.1) proves (3.2).  QED

The exact inversion is also useful.  If `C_I(u)<=C`, then

```text
L >= { exp[((m/C-1)_+)^2/(4m)]/8 - 2 }/(wm).         (3.4)
```

In particular, when `m>=2C`,

```text
L >= { exp[m/(16C^2)]/8 - 2 }/(wm).                 (3.5)
```

No spacing or arithmetic hypothesis appears in this theorem.

### Positive interpolation consequence

Suppose a fixed compact `J` contained in an interval of length `L` has the
following universal property: for every sign vector
`sigma in {+1,-1}^m`, a positive measure `mu_sigma` supported in `J`
satisfies

```text
hat(mu_sigma)(u_j)=sigma_j,       mu_sigma(J)<=P.     (3.6)
```

Use in (3.6) the sign vector equal to the random coefficient vector from
the proof.  Then

```text
m=|integral_J sum_j epsilon_j exp(-i t u_j)dmu| 
 <=P sup_(t in J)|sum_j epsilon_j exp(-i t u_j)|.
```

Consequently `P` obeys the same lower bound (3.2).  Thus (3.2)--(3.5)
apply directly to universal **positive** interpolation; no linear selection
operator and no converse theorem are being assumed.

---

## 4. Application to the QP band

The prime number theorem gives, after removing at most one node,

```text
m asymp_w Y/log Y.                                   (4.1)
```

The full QP band has length

```text
L_Y=Y^(50/33)-Y^.01=Y^(50/33)(1+o(1)).              (4.2)
```

Insert (4.1)--(4.2) and fixed `w` into (3.2):

```text
C_(H_Y) >= c_w sqrt{Y}/log Y =Y^(1/2-o(1)).          (4.3)
```

This is far above the target mass scale `Y^.019`.  Conversely, if one
insists on a universal interpolation constant

```text
C=Y^.019,
```

then (3.5) requires

```text
log L >= Omega(Y^.962/log Y),                        (4.4)
```

not `log L=O(log Y)`.

The location of the compact is not an extra loophole.  If a universal
support compact has diameter at most `|H_Y|`, translate it into `H_Y` and
ask Florek to interpolate the phase-precompensated Hermitian values.  The
translation then produces the desired values.  Diameter, not the fact that
the interval starts at `Y^.01`, is decisive.

Florek's explicit construction makes the loss still larger.  Interpolating
the constant value `-1` and normalizing its positive measure would guarantee
depth at least

```text
epsilon/(32 C^4).                                    (4.5)
```

To make (4.5) as large as `Y^(-.019)` would require
`C<=Y^(.019/4+o(1))`, while (4.3) forces
`C>=Y^(1/2-o(1))` on the polynomial band.  Even a hypothetical improvement
from quartic to linear dependence on the universal interpolation constant
would still miss the target by a wide power.

---

## 5. Exact statement about Florek's associated compact

There are two distinct conclusions, and they must not be conflated.

1. If an actual compact `K` of diameter `D` is associated with these `m`
   frequencies with interpolation norm `C_K`, then (3.2) gives a **necessary
   lower bound** on the tradeoff between `D` and `C_K`.  This follows by
   enclosing `K` in an interval of length `D`.  No converse is used.

2. Florek and Dechamps--Gondim do **not** give an upper bound on the diameter
   of a compact associated with a prescribed norm, nor an upper bound on
   `K_1(C,U,epsilon)`.  Our local lower bound cannot be inverted into such an
   upper bound.  Large diameter is necessary for small norm, not sufficient.

Applied directly to Florek's final common support

```text
J=2K+K_1(C,U,epsilon),
```

the mass estimate (1.2) and Theorem 3.1 force `diam(J)` to be exponential
whenever `C` and `epsilon` are fixed.  This is a lower bound on the final
support size, not a claim identifying whether `K` or `K_1` carries the
growth.

That is the precise support audit: the primary theorem is correct, but its
unquantified associated compact hides exactly the recurrence scale that QP
must control.

---

## 6. Scope: why the special antipode is still open

The entropy argument chooses a hostile sign pattern depending on the
frequency set and interval.  QP asks only for the single Hermitian target

```text
hat(nu)(+/-u_j)=-r               for every j,        (6.1)
```

or, equivalently, equal negative cosine moments.  Universal interpolation
may be exponentially harder than (6.1).  Neither Theorem 3.1 nor Florek's
quartic construction proves a lower bound for the minimum mass of this one
target.

Thus the valid conclusion is

```text
global odd-base-subset Sidon constant:             UNIFORMLY BOUNDED;
universal positive interpolation on H_Y:           COST >=Y^(1/2-o(1));
bounded-constant associated support:                EXPONENTIAL DIAMETER;
Florek theorem with polynomial support:             CANNOT REACH c=.019;
special all-negative full-band antipode:             OPEN;
fixed-power QP / uniform zeta strip:                 NOT PROVED.
```

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_sidon_support_entropy.py
PYTHONPATH=src python3 src/qp_sidon_support_entropy.py
```

The first command currently reports `5 passed`.
