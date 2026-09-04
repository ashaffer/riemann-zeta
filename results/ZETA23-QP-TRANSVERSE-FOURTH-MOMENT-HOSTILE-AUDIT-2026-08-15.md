# QP transverse fourth moment: hostile audit and moment frontier

**Date:** 2026-08-15  
**Verdict:** **PASS**, with an explicit logarithmic sharpening.  For fixed
`w`, `1<A<2`, `B=Y^A`, and all sufficiently large half-integer `Y`, the
complete actual prime-power node set satisfies

```text
s_v >>_w [M_Y(1+Y^2/B)]^(-1/2)
    >>_w sqrt(log Y)Y^(-(3-A)/2),                   (0.1)
r_+(H_Y;S_Y)>>_w sqrt(log Y)Y^(-(3-A)/2).           (0.2)
```

The first bound is uniform for every

```text
v=a(t_0)+Dq_0,       0<=t_0<=B,       0<D<=1,       (0.3)
```

and every signed adaptive dual vector on all prime-power coordinates.  It
therefore applies to a residual calibrated by a long negative prime event,
but does not use that calibration.  At `A=50/33`, (0.1) is

```text
s_v >>_w sqrt(log Y)Y^(-49/66).                    (0.4)
```

This is an asymptotic lower bound, not a strip-scale return.  It proves no
QP upper bound, `LTRAD_full`, QP-to-strip implication, or uniform strip.

---

## 1. Exact quantifier audit

The relevant body and support function are

```text
P_Y=conv{a(t):t in H_Y},
h_Y(y)=sup_(t in H_Y)y dot a(t),
s_v=sup{s>=0:-s v in P_Y}.                          (1.1)
```

The proof must control every real `y`, including vectors supported wholly
outside the selected prime interval, on proper prime powers, or on a close
cross-side reflection pair.  The fourth-moment proof retains all of these
coordinates.  It proves, uniformly when `y dot v<0`,

```text
h_Y(y)>>_w[M_Y(1+Y^2/B)]^(-1/2)[-y dot v].         (1.2)
```

It also proves `h_Y(y)>=0` for every `y`.  Thus for a sufficiently small
constant `c_w`, every dual satisfies

```text
y dot{-c_w[M_Y(1+Y^2/B)]^(-1/2)v}<=h_Y(y).         (1.3)
```

Compact support-function separation gives membership in `P_Y`.  This
direct argument proves feasibility; it does not invoke a ray-infimum
formula before feasibility has been established.

---

## 2. The bounded prime-power product multiplicity

The original proof used the general divisor estimate `d(k)=Y^o(1)`.  The
actual node set gives a stronger elementary fact.

### Lemma 2.1

For

```text
S_Y={p^j:Y exp(-w)<p^j<Y exp(w)},
r_2(k)=#{(n,m) in S_Y^2:nm=k},
```

one has

```text
sup_k r_2(k)<=C_w.                                  (2.1)
```

If `k` has two distinct prime bases, a representation by two prime powers
forces one factor to carry each base, leaving only the two orders.  If
`k=p^L`, write the factors as `p^j,p^(L-j)`.  The shell condition confines
`j` to an interval of length `2w/log p<=2w/log 2`, hence permits only
`O_w(1)` integers.  Products with more prime bases have no representation.

Consequently a product interval containing `O(1+Y^2/B)` integers contains
only `O_w(1+Y^2/B)` ordered shell pairs.  This simultaneously sharpens:

```text
number of unresolved reflection blocks <<_w1+Y^2/B, (2.2)
fourth-moment product Gram row sum    <<_w1+Y^2/B.   (2.3)
```

For (2.3), if `k,l asyp_wY^2`, Schwartz decay gives

```text
sum_l r_2(l)|hat psi(B log(k/l))|
 <<_w sum_(h in Z)(1+c_wB|h|/Y^2)^(-L)
 <<_w1+Y^2/B.                                      (2.4)
```

No short-interval prime theorem is used.

---

## 3. Close-reflection audit

Pair every cross-side absolute-log pair with gap at most `kappa/B`.  Such
pairs are disjoint because each side is `c_w/Y`-separated and `B>>Y`.
Equation (2.2) bounds their number by `R<<_w1+Y^2/B`.

The entire two-coordinate block, not merely its sum coordinate, is placed
in `J`.  In the normalized block variables

```text
p=y_1+y_2,
q=B|u_1-u_2|(y_1-y_2),                              (3.1)
```

the clustered frame gives

```text
||J||_infinity<<sqrt(R)E_J^(1/2),
int J^2rho_B<<E_J.                                  (3.2)
```

Therefore

```text
int J^4rho_B<<R E_J^2
              <<_w(1+Y^2/B)E_J^2.                 (3.3)
```

This is valid even when the raw difference coefficient is arbitrarily
large.  Off those complete blocks, the clustered energy controls the
ordinary coefficient square-sum.  Writing the remaining cosine sum as

```text
G(t)=Re[Y^(-it)sum_n y_n n^(it)]                   (3.4)
```

and applying (2.4) to its square gives

```text
int G^4rho_B<<_w(1+Y^2/B)E_G^2.                    (3.5)
```

Equations (3.3)--(3.5) prove, for the complete signed dual,

```text
int F_y^4rho_B<<_w(1+Y^2/B)(int F_y^2rho_B)^2.      (3.6)
```

---

## 4. One-sided range and the explicit logarithm

After subtracting the rapidly decaying smooth mean, `L^1-L^2-L^4`
interpolation gives

```text
sup_(t in H_Y)F_y(t)
 >>_w(1+Y^2/B)^(-1/2)(int F_y^2rho_B)^(1/2).       (4.1)
```

The clustered point-evaluation inequality, valid at both `0` and every
`0<=t_0<=B`, gives

```text
|y dot v|<<_w sqrt(M_Y)(int F_y^2rho_B)^(1/2).     (4.2)
```

Combining (4.1)--(4.2) proves the first bound in (0.1).  Chebyshev's prime
bound and the elementary count of proper prime powers give

```text
M_Y<<_wY/log Y.                                     (4.3)
```

Since `1<A<2`, substituting `B=Y^A` into (0.1) proves the explicit
`sqrt(log Y)` strengthening.  This logarithm was hidden when both product
multiplicity and shell cardinality were written as `Y^o(1)`.

---

## 5. The standard even-moment frontier

The same product argument can be run at every fixed even moment `2k`,
`k>=2`.  A product of `k` shell prime powers has only `O_(w,k)(1)` ordered
representations.  Indeed, assign its at most `k` prime bases to the `k`
slots and note that every exponent lies in a fixed-length interval.  The
good-coordinate product packet and the unresolved-block contribution give

```text
int |F_y|^(2k)rho_B
 <<_(w,k)Y^(k-A)(int F_y^2rho_B)^k.                 (5.1)
```

For the bad blocks the factor is
`R^(k-1)=Y^((2-A)(k-1))`, which is no larger than `Y^(k-A)` because

```text
(k-A)-(2-A)(k-1)=(A-1)(k-2)>=0.                    (5.2)
```

Interpolating `L^1`, `L^2`, and `L^(2k)` costs the
`1/[2(k-1)]` power of the packet factor.  After point evaluation the
resulting transverse exponent is

```text
theta_k=1/2+(k-A)/[2(k-1)]
       =1-(A-1)/[2(k-1)].                           (5.3)
```

For `1<A<2`, `theta_k` is strictly increasing in `k`.  Hence

```text
min_(fixed k>=2)theta_k=theta_2=(3-A)/2.            (5.4)
```

The fourth moment is therefore optimal within this standard fixed
even-moment/product-Schur/interpolation family.  This is a method barrier,
not an upper bound on the true `s_v`.  Mixed moments, cancellation inside
product packets, a coefficient-sensitive short-product theorem, or a use
of the calibrated long event remain possible sources of further gain.

---

## 6. Disposition

```text
all-signed-dual quantifiers retained:               VERIFIED;
unresolved pair treatment in divided differences:  VERIFIED;
prime-power pair-product multiplicity O_w(1):       PROVED;
explicit kurtosis K<<_w1+Y^(2-A):                  PROVED;
s_v,r_+ >>sqrt(log Y)Y^(-(3-A)/2):                 PROVED;
A=50/33 exponent 49/66 plus sqrt(log Y):           PROVED;
higher fixed even moments improve 49/66:            FALSE BY THIS METHOD;
strip-scale transverse return or LTRAD_full:        NOT PROVED;
QP, QP-to-strip, or a uniform strip:                NOT PROVED.
```

Executable replay:

- `src/qp_transverse_fourth_moment_gate.py`;
- `src/test_qp_transverse_fourth_moment_gate.py`;
- `results/verify_zeta23_qp_transverse_fourth_moment_gain.py`.
