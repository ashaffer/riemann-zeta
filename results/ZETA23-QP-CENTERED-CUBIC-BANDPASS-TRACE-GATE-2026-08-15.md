# QP centered cubic: band-pass and trace gate

**Date:** 2026-08-15  
**Verdict:** centering the actual prime-log cosine features does not delete
the signed cubic carry block.  If

```text
F_y(t)=sum_n y_n cos(t u_n),       u_n=|log(n/Y)|,
m_y=E F_y,                         V_y=Var(F_y),
```

then the exact scalar identity is

```text
E(F_y-m_y)^3=E F_y^3-3m_y V_y-m_y^3.               (0.1)
```

The clustered-frame mean estimate makes the last two terms smaller than
every fixed power of `Y`, uniformly after variance normalization.  A
hypothetical exact zero of every node mean makes the centered cubic equal to
the raw cubic exactly; it does not remove any triple carry.

The raw diagonal cubic has the exact decomposition

```text
E F_y^3=(1/4) C_+++(y)+(3/4) C_++-(y).             (0.2)
```

The three choices of the minus sign give the same diagonal form and hence
add rather than cancel.  On the explicit compact B-spline laws, every actual
triple satisfying `|u_i+u_j-u_k|<=c/B` has a positive centered tensor entry
bounded away from zero for large `Y`.

There is an exact trace fact, but it is not a norm saving.  A hard
one-minus slice is trace-free and is a partial permutation on each pair of
node sides.  Symmetrizing the cubic reintroduces the doubling correlation

```text
sum_j C_B(2u_j-u_i),                               (0.3)
```

and centering forces neither coefficient-index row sums nor the full tensor
trace to vanish.  Even exact zero trace and exact zero all-ones contractions
do not bound a symmetric cubic below `sqrt(R)` as a matter of linear
algebra.

Thus the remaining actual-node target is a signed, coefficient-uniform norm
estimate for the one-minus carry form, or equivalently a bound on the
cross-correlations of the actual partial-permutation slices.
Scalar means, slice traces, and row sums test only degenerate contractions
and cannot supply that estimate.  No actual `sqrt(R)` saturation, no exponent
below `49/66`, no QP result, and no strip result is proved here.

---

## 1. Exact centered and raw identities

Let `Y=N+1/2`, let `S_Y` be the actual prime-power shell, merge repeated
absolute frequencies, and put

```text
u_n=|log(n/Y)|>0,                 M=|S_Y|,
B=Y^A,                            A>1.             (1.1)
```

Let `rho_B` be any probability for which the following moments exist, and
write

```text
C_B(omega)=E cos(t omega),
c_n(t)=cos(tu_n),                 m_n=C_B(u_n).     (1.2)
```

For `F_y=sum_n y_n c_n`, direct expansion gives

```text
kappa_3(y):=E(F_y-m_y)^3
 =E F_y^3-3m_y E F_y^2+2m_y^3
 =E F_y^3-3m_y V_y-m_y^3.                         (1.3)
```

Consequently, with `r_y=|m_y|/sqrt(V_y)`,

```text
|kappa_3(y)-E F_y^3|/V_y^(3/2)<=3r_y+r_y^3.       (1.4)
```

This is the whole effect of scalar centering on the diagonal cubic.

For the legal smooth full-band law used in the clustered frame, uniformly
in every real coefficient vector,

```text
|m_y|<<_(w,K) sqrt(M)(Y/B)^K E_Y(y)^(1/2),
V_y asyp_w E_Y(y).                                 (1.5)
```

The second comparison follows from the proved second-moment comparison and
(1.5), for large `Y`.  Since `M<<_wY` and `A>1`, for every fixed `N_0` one
may choose the fixed integration-by-parts order `K` so that

```text
sup_(y nonzero) r_y=O_(w,N_0)(Y^(-N_0)).           (1.6)
```

Equations (1.4)--(1.6) prove that centering cannot itself supply a
power-scale reduction in standardized skew.  This statement includes the
unresolved reflected-pair directions because (1.5) is stated in the
clustered energy.

There is an even sharper exact observation.  If a proposed filter satisfies

```text
C_B(u_n)=0                 for every actual node,  (1.7)
```

then `m_y=0` for every `y`, so

```text
kappa_3(y)=E F_y^3                                  (1.8)
```

exactly.  Thus a zero **linear** node-frequency block removes only the
centering correction; it does not remove the cubic carry block.

An exact open Fourier gap is also unavailable for the legal compact-time
probability itself.  Its cosine transform is entire and has `C_B(0)=1`.
If it vanished on a real open interval, the identity theorem would make it
zero everywhere, a contradiction.  Hard frequency windows used below are
therefore decompositions or majorants, not exact transforms of a nonzero
compact-time probability.

---

## 2. The three signed carries add on a diagonal coefficient vector

The cosine product formula gives the raw tensor

```text
Q_ijk=1/4[
 C_B(u_i+u_j+u_k)
 +C_B(u_i+u_j-u_k)
 +C_B(u_i-u_j+u_k)
 +C_B(-u_i+u_j+u_k)].                              (2.1)
```

Define

```text
C_+++(y)=sum_(i,j,k)y_i y_j y_k C_B(u_i+u_j+u_k),
C_++-(y)=sum_(i,j,k)y_i y_j y_k C_B(u_i+u_j-u_k). (2.2)
```

Because the same vector `y` occurs in all three slots, relabeling the
indices shows that all three one-minus sums are equal.  Therefore

```text
E F_y^3=(1/4)C_+++(y)+(3/4)C_++-(y).               (2.3)
```

There is no cancellation among the three orientations.  They are three
copies of the same scalar.

The all-plus term is uniformly rapidly decreasing in the clustered norm.
Indeed the smallest absolute node spacing is `>>Y^-2`, so the definition of
the two-point energy gives the crude but sufficient comparison

```text
||y||_2<<_w(1+Y^2/B)E_Y(y)^(1/2).                  (2.3a)
```

Every all-plus frequency is `>>Y^-1`.  Schwartz decay, (2.3a), and
`||y||_1<=sqrt(M)||y||_2` therefore give, for every fixed `K`,

```text
|C_+++(y)|
 <<_(w,K) M^(3/2)(1+Y^2/B)^3(Y/B)^K E_Y(y)^(3/2). (2.3b)
```

For fixed `A>1`, choosing `K` makes (2.3b) smaller than any prescribed
power.  This deliberately crude estimate only removes the nonresonant
all-plus block without discarding a reflected-pair direction.

For the explicit order-`q_0` B-spline probability,

```text
C_B(omega)=cos(Bomega/2)
           sinc(Bomega/(6q_0))^q_0.                (2.4)
```

Fix `0<c_0<pi`.  Suppose an actual triple obeys

```text
|u_i+u_j-u_k|<=c_0/B.                              (2.5)
```

The half-integer spacing gives `min_n u_n>>_w1/Y`.  The other three
frequencies in (2.1) are therefore all `>>_w1/Y` for large `Y`.  Hence

```text
T_ijk=(1/4)C_B(u_i+u_j-u_k)+O_(w,q_0)((Y/B)^q_0), (2.6)
```

where `T` is the centered third tensor.  The error includes the other three
raw sign patterns and all mean corrections.  Moreover

```text
C_B(u_i+u_j-u_k)
 >=cos(c_0/2)sinc(c_0/(6q_0))^q_0=:c_(0,q_0)>0.   (2.7)
```

Thus every actual hard-carry entry satisfies

```text
T_ijk>=c_(0,q_0)/8                                 (2.8)
```

once `Y` is sufficiently large, with the threshold depending on the fixed
parameters.  Equation (2.8) is conditional only on the actual triple being
present; it makes no lower-bound claim about how many such triples exist.
It proves that centering does not cancel an individual actual carry.

For a general `C^infinity` compact-time law, (2.3) remains exact and the
noncarry transforms are rapidly decreasing.  The B-spline law is used in
(2.6)--(2.8) only to make the positive core completely explicit.

---

## 3. What the slice trace does and does not say

Let `chi` be supported on `[-c_0,c_0]`, and isolate the hard one-minus core

```text
K_ijk=chi(B(u_i+u_j-u_k)).                          (3.1)
```

For fixed `i`, view `K_i=(K_ijk)_(j,k)` as an operator from the `j` slot to
the `k` slot.  Its diagonal is

```text
(K_i)_(j,j)=chi(Bu_i).                              (3.2)
```

Since `Bu_i>>B/Y->infinity`, for all large `Y`

```text
tr(K_i)=0.                                          (3.3)
```

On each fixed choice of the two node sides, the frequencies are
`>>_w1/Y` separated.  The core window has width `O(1/B)=o(1/Y)`.  Hence
every side-to-side block of `K_i` has at most one nonzero entry in every
row and every column: it is a weighted partial permutation.  Keeping both
sides makes the slice a sum of only the corresponding finitely many partial
permutations.  This statement retains the actual prime-power support and
does not replace it by a grid.

For the full smooth kernel instead of the hard core,

```text
tr(K_i)=M C_B(u_i)<<_(w,K)M(Y/B)^K.                 (3.4)
```

Thus the proposed trace is indeed zero for the hard block and negligible
for the smooth block.  It still does not control the singular norm of the
slice family.

More importantly, the actual cubic tensor is symmetric.  Put

```text
S_ijk=1/3[
 C_B(u_i+u_j-u_k)+C_B(u_i-u_j+u_k)
 +C_B(-u_i+u_j+u_k)].                              (3.5)
```

Then an exact contraction gives

```text
sum_j S_(i,j,j)
 =1/3[2M C_B(u_i)+sum_j C_B(2u_j-u_i)].            (3.6)
```

The first term is the negligible slice trace.  The second is the actual
doubling-carry correlation and is not forced to vanish.  If the node means
are exactly zero as in (1.7), the first term disappears but the second
remains.

For completeness, if

```text
X_i(t)=cos(tu_i)-m_i,
T_ijk=E X_i X_j X_k,                               (3.7)
```

then the exact coefficient-index contractions are

```text
sum_k T_ijk=E[X_i X_j sum_k X_k],                  (3.8)
sum_i T_iik=E[(sum_i X_i^2)X_k].                   (3.9)
```

Centering says only `E X_i=0`.  Equation (3.8) vanishes precisely when the
all-ones feature sum is orthogonal to every product `X_iX_j`; (3.9)
vanishes precisely when the feature radius-squared is orthogonal to every
coordinate.  Those are new third-order correlation assertions, not
consequences of centering.

After covariance whitening, (3.9) becomes

```text
E[||Z(t)||_2^2 Z(t)].                              (3.10)
```

Unit covariance does not make `||Z(t)||_2` constant and does not force
(3.10) to be zero.

---

## 4. Trace and row sums are identity-only data

Even granting stronger identities than the actual tensor is known to have
would not imply the desired norm estimate.  Let `e_1,e_2` be orthonormal
vectors perpendicular to the all-ones vector in any real coefficient space
of dimension at least three, and define the symmetric cubic

```text
P_R(x)=sqrt(R)[(e_1 dot x)^3
               -3(e_1 dot x)(e_2 dot x)^2].       (4.1)
```

Its tensor satisfies

```text
sum_i T_iik=0                    for every k,
T(q_0,x,z)=0                    for every x,z,     (4.2)
sup_(||x||=1)|P_R(x)|=sqrt(R).                     (4.3)
```

The first identity is harmonicity; the second gives zero all-ones row sums
in every mode; the last follows from the triple-angle identity.  This is an
algebraic identity barrier, not an actual-prime tensor and not a claim that
the actual carry norm saturates `sqrt(R)`.

There is an analogous operator barrier.  On a cyclic space of dimension
`4R`, let `U` be the cyclic shift and put

```text
A_R=R^(-1/2)sum_(r=1)^R(U^r-U^(r+R)).              (4.4)
```

Every summand is a difference of two permutation maps, while

```text
tr(A_R)=0,             A_R q_0=A_R^T q_0=0,
||A_R||_(2->2)>>sqrt(R).                            (4.5)
```

The last assertion follows by evaluating the Fourier mode of angle `pi/R`.
Again (4.4) is only a finite linear-algebra counterexample to an
identity-only inference.  It is not substituted for the actual support.

Equations (4.1)--(4.5) explain why a trace estimate, even supplemented by
row- and column-sum cancellation, cannot lower a coefficient-uniform
operator norm.  Such identities test a few prescribed vectors.  The norm
allows an arbitrary adaptive singular vector.

---

## 5. The exact actual correlation target

Put

```text
R=1+Y^2/B.                                          (5.1)
```

Up to the rapidly decreasing all-plus and centering terms isolated above,
the full cubic question is the one-minus form

```text
C_++-(y)=sum_(i,j,k)y_i y_j y_k
                    C_B(u_i+u_j-u_k).              (5.2)
```

The current coefficient-uniform theorem is at the `sqrt(R)` scale.  A
genuine fixed-power improvement is therefore the actual-node assertion

```text
|C_++-(y)|
 <<R^(1/2-delta)E_Y(y)^(3/2)                      (5.3)
```

for some fixed `delta>0` and every real `y`, with the two-point divided-
difference blocks retained.  At the active aperture, reaching the proposed
quarter scale would mean `delta=1/4-o(1)`.

In slice language, set

```text
(A_i)_(j,k)=C_B(u_i+u_j-u_k).                      (5.4)
```

Then (5.2) is `sum_i y_i <A_i y,y>`.  A strong sufficient `TT*` target is
obtained after passing to orthonormal clustered covariance coordinates and
denoting the resulting slices by `Atilde_r`:

```text
||sum_(r,r') x_r x_r' Atilde_r^*Atilde_r'||
 <<R^(1-2delta)||x||_2^2.                          (5.5)
```

The slice trace sees only the diagonal entries of each `A_i`.  Row sums test
only the all-ones vector.  Equation (5.5) instead requires control of all
off-diagonal compositions `A_i^*A_i'` on every adaptive vector.  Taking
absolute values in those compositions returns the already saturated local
product energy, so a successful proof must preserve the signed kernel or a
new rank-one correlation.

This is the exact point at which the band-pass/trace route stops.  It has
reduced the question to a genuine actual-prime weighted correlation, but it
has not estimated that correlation.

---

## 6. Binary disposition

```text
exact scalar centering identity (0.1):             PROVED;
centering correction superpolynomially small:      PROVED;
zero node means imply centered equals raw:          PROVED;
three one-minus diagonal forms add:                 PROVED;
individual B-spline carry survives centering:       PROVED;
hard actual-support slice trace zero:               PROVED;
hard-core side blocks are partial permutations:     PROVED;
full symmetric tensor trace zero:                   NOT FORCED;
coefficient-index row sums forced zero:              NOT FORCED;
trace/row-sum data imply norm below sqrt(R):         FALSE;
actual carry tensor saturates sqrt(R):               NOT PROVED;
actual fixed-power saving in (5.3):                  OPEN;
full-shell exponent below 49/66:                     NOT PROVED;
QP or a uniform strip:                               NOT PROVED.
```

Executable finite-algebra checks:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_centered_cubic_bandpass_trace_gate.py
```

They replay (0.1)--(0.2), the exact symmetrized trace formula, the actual
half-integer hard-slice trace and side partial-permutation property, and the
two identity-only norm barriers.
