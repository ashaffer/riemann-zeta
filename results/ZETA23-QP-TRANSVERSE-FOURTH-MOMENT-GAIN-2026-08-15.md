# QP transverse return: a fourth-moment fixed-power gain

**Date:** 2026-08-15  
**Verdict:** the actual integer nature of the prime-power nodes improves the
previous transverse floor.  Let

```text
H_Y=[Y^a,Y^A],              1<A<2,
B=Y^A,
S_Y={n=p^k:Y exp(-w)<n<Y exp(w)},
a(t)=(cos(t log(n/Y)))_(n in S_Y),
M_Y=|S_Y|.
```

For every `0<=t_0<=B`, `0<D<=1`, and

```text
v=a(t_0)+D(1,...,1),
s_v=sup{s>=0:-s v in conv{a(t):t in H_Y}},
```

one has

```text
s_v >>_w sqrt(log Y) Y^(-(3-A)/2).                  (0.1)
```

The same proof, with the normalization `F_y(0)=-1`, also gives the full-band
positive-antipode floor

```text
r_+(H_Y;S_Y)>>_w sqrt(log Y) Y^(-(3-A)/2).          (0.1a)
```

At the project aperture `A=50/33`, this is

```text
s_v >>_w sqrt(log Y) Y^(-49/66).                    (0.2)
```

Thus the exponent improves from `1` to `49/66`; equivalently the gain over
the dimension floor is `17/66`.  The proof is uniform in the signed dual
coefficients and therefore applies to the specially calibrated residual
coming from a long negative prime interval.  It actually uses only the form
`a(t_0)+D q_0`, not the calibration identity.

This is a genuine fixed-power transverse theorem, but it is still far from
the needed scale `s_v>=Y^{-(c-d)+o(1)}` with `c-d` near zero.  It proves
neither `LTRAD_full`, QP, a QP-to-strip implication, nor a uniform strip.

---

## 1. The clustered quadratic form

Use the smooth probability `rho_B(t)=B^-1 psi(t/B)` from the clustered-frame
theorem, with support in the upper part of `H_Y`.  For

```text
F_y(t)=sum_(n in S_Y)y_n cos(t log(n/Y)),
Q_y=int F_y(t)^2 rho_B(t)dt,
```

that theorem constructs a positive block energy `E_Y(y)` satisfying

```text
Q_y asyp_w E_Y(y),                                  (1.1)
|F_y(t)| <<_w sqrt(M_Y) E_Y(y)^(1/2)  (0<=t<=B),   (1.2)
|int F_y rho_B| <<_(w,L) sqrt(M_Y)(Y/B)^L
                              E_Y(y)^(1/2).          (1.3)
```

The only nonstandard blocks are cross-side pairs `n<Y<m`.  If their
absolute frequencies have gap `delta`, their energy coordinates are

```text
p=y_n+y_m,
q=min(1,B delta)(y_n-y_m).                          (1.4)
```

All other blocks have energy uniformly equivalent to ordinary coefficient
square-sum.

The purpose of this note is to replace the general fourth-moment bound
`int F^4<=M Q^2` by an arithmetic bound of size `Y^(2-A+o(1))Q^2`.

---

## 2. Remove only the unresolved reflections

Fix a sufficiently large constant `kappa`.  Call a cross-side pair bad if

```text
|log(Y/n)-log(m/Y)|<=kappa/B.                       (2.1)
```

Exactly as in the near-reflection audit, (2.1) implies

```text
|nm-Y^2|<<_kappa Y^2/B.                            (2.2)
```

There are `O(1+Y^2/B)` possible integer products `nm`.  Each has only
`O_w(1)` ordered representations by two members of `S_Y`.  If it has two
prime bases, the factors are forced up to order.  If it is `p^L`, both
exponents must lie in an interval of length `2w/log p`, leaving at most
`1+2w/log 2` choices.  Hence the number `R_Y` of bad pairs and endpoints
obeys the sharper bound

```text
R_Y<<_w1+Y^2/B<<Y^(2-A).                            (2.3)
```

For large `Y`, a node belongs to at most one such pair: nodes on either
fixed side have frequency spacing `>>_w1/Y`, whereas `B^-1=o(Y^-1)`.

Write

```text
F_y=G_y+J_y,       E_Y=E_G+E_J,                    (2.4)
```

where `J_y` contains the endpoints of bad pairs.  The normalized pair
formula behind (1.4) gives, for `0<=t<=B`,

```text
|J_y(t)|<<_w sqrt(R_Y) E_J^(1/2).                  (2.5)
```

The clustered frame also gives `int J_y^2 rho_B<<E_J`.  Consequently

```text
int J_y^4 rho_B<=||J_y||_infty^2 int J_y^2 rho_B
                    <<R_Y E_J^2
                    <<_w(1+Y^2/B)E_J^2.            (2.6)
```

This is where the close cross-side collisions are paid for.  No coefficient
square-sum is asserted on an unresolved pair.

---

## 3. Integer-product fourth moment off the bad pairs

Once the endpoints in Section 2 are removed, the block energy is ordinary:

```text
sum_(n good)y_n^2<<_w E_G.                          (3.1)
```

Indeed same-side gaps are `>>1/Y`, and every remaining cross-side absolute
gap is `>kappa/B`; taking `kappa` fixed and large gives a uniform lower
two-point Gram eigenvalue.  This also follows directly from (1.4), since
every retained divided-difference factor is bounded below by a constant.

Put

```text
P_y(t)=sum_(n good)y_n exp(it log(n/Y)).             (3.2)
```

Then `G_y=Re P_y`, and the harmless factor `Y^(-it)` gives

```text
|P_y(t)|=|sum_(n good)y_n n^(it)|.                  (3.3)
```

On squaring, write

```text
(sum_n y_n n^(it))^2=sum_k b_k k^(it),
b_k=sum_(nm=k)y_n y_m.                              (3.4)
```

All active `k` lie in a fixed interval of size `asymp_wY^2`.  Expanding the
smooth mean square in (3.4), Schwartz decay gives the Fourier-kernel row
sum

```text
<<_(w,L) sum_(h in Z)(1+c_wB|h|/Y^2)^(-L)
<<_w1+Y^2/B.                                        (3.5)
```

Thus

```text
int |P_y|^4 rho_B
 <<_w(1+Y^2/B)sum_k|b_k|^2.                        (3.6)
```

Let `r_S(k)` count the ordered representations `k=nm` with `n,m in S_Y`.
The prime-power observation in Section 2 gives `r_S(k)<<_w1`, and
Cauchy--Schwarz gives

```text
|b_k|^2<=r_S(k)sum_(nm=k)y_n^2 y_m^2.              (3.7)
```

Summation of (3.7) yields, with no divisor-function loss,

```text
sum_k|b_k|^2<<_w(sum_n y_n^2)^2.                    (3.8)
```

Since `|G_y|<=|P_y|`, (3.1), (3.6), and (3.8) prove

```text
int G_y^4 rho_B<<_w(1+Y^2/B)E_G^2.                 (3.9)
```

The argument is uniform in the real, adaptive coefficients `y_n`.  Prime
distribution in short intervals is not used; bounded prime-power product
multiplicity is enough.

Combining (2.6), (3.9), and
`|G+J|^4<=8(|G|^4+|J|^4)` gives the kurtosis estimate

```text
int F_y^4 rho_B<=K_Y Q_y^2,
K_Y<<_w1+Y^2/B<<Y^(2-A).                            (3.10)
```

---

## 4. Fourth moment forces a positive excursion

We record the elementary one-sided moment step.  If a real random variable
`Z` has mean zero, variance `V`, and fourth moment `W`, interpolation between
`L^1`, `L^2`, and `L^4` gives

```text
E|Z|>=V^(3/2)/W^(1/2).                              (4.1)
```

Since `E Z_+=E|Z|/2`,

```text
sup Z>=V^(3/2)/(2W^(1/2)).                          (4.2)
```

Apply this with `Z=F_y-int F_y rho_B`.  Choose the fixed integer `L` in
(1.3) so large that

```text
sqrt(M_Y)(Y/B)^L=o(K_Y^(-1/2)).                     (4.3)
```

This is possible for every fixed `A>1`.  Equations (1.1), (1.3), and (3.10)
then give

```text
sup_(t in H_Y)F_y(t)>>Q_y^(1/2)/sqrt(K_Y).          (4.4)
```

This is the coefficient-sensitive gain absent from the second-moment proof.

---

## 5. The transverse depth

Normalize a dual vector by

```text
y dot v=F_y(t_0)+D F_y(0)=-1.                       (5.1)
```

Because `0<=t_0<=B` and `0<D<=1`, the leverage bound (1.2) implies

```text
1<<sqrt(M_Y)E_Y(y)^(1/2),
Q_y^(1/2)>>M_Y^(-1/2).                              (5.2)
```

Substitution in (4.4) proves, uniformly for every normalized dual,

```text
h_Y(y):=sup_(t in H_Y)y dot a(t)
 >>_w1/sqrt(M_Y K_Y).                               (5.3)
```

The shell count `M_Y<<_wY/log Y` and (3.10) give

```text
h_Y(y)>>_w sqrt(log Y)Y^(-(3-A)/2).                 (5.4)
```

Equation (4.4) makes `h_Y(y)>0` for every nonzero `y`.  Take
`s=c_w/sqrt(M_YK_Y)` with `c_w` small enough.  By homogeneity, (5.3) gives

```text
y dot(-s v)<=h_Y(y)                 for every y.     (5.5)
```

For `y dot v<0`, this is (5.3) after normalization.  For `y dot v>=0`,
the left side is nonpositive and `h_Y(y)>=0`.  Compact support-function
separation places `-s v` in the moment body, proving (0.1) without
presupposing that the transverse ray is feasible.

For completeness, the radial dual formula is

```text
r_+(H_Y;S_Y)=inf_(y:F_y(0)=-1)h_Y(y).               (5.5a)
```

Under this normalization, (1.2) at `t=0` gives (5.2) directly.  Therefore
the identical argument proves (0.1a).  This is a lower bound on the radius;
QP/DPA KILL asks for an upper bound and does not follow from it.

For `A=50/33`,

```text
2-A=16/33,
(3-A)/2=49/66,
1-(3-A)/2=(A-1)/2=17/66.                            (5.6)
```

---

## 6. Exact scope

The result shows that exact Sidonicity is not the useful finite-band
invariant: at resolution `B^-1`, pair products necessarily occupy packets
of average size about `Y^2/B`.  The useful statement is instead the uniform
weighted multiplicative-convolution estimate (3.6)--(3.8).  It is a local
one-sided Littlewood input of fourth order, and it yields precisely the
power in (0.1).

To improve (0.1) by the same route one would need a stronger, uniformly
weighted prime-log Littlewood theorem that reduces either the
`Y^2/B` fourth-moment packet factor or the leverage cost in (5.2).  Ordinary
spacing, exact additive energy, or qualitative Sidon interpolation does not
do so.

```text
unresolved-reflection count <<_w 1+Y^(2-A):        PROVED;
adaptive actual-node fourth moment K<<_wY^(2-A):   PROVED;
one-sided transverse floor sqrt(log Y)Y^(-(3-A)/2): PROVED;
full-band radial floor sqrt(log Y)Y^(-(3-A)/2):    PROVED;
A=50/33 exponent 49/66 plus sqrt(log Y):           PROVED;
strip-scale LTRAD_full(c,d):                        NOT PROVED;
QP, QP-to-strip, or a uniform strip:                NOT PROVED.
```

Executable algebra checks:

- `src/qp_transverse_fourth_moment_gate.py`;
- `src/test_qp_transverse_fourth_moment_gate.py`.
