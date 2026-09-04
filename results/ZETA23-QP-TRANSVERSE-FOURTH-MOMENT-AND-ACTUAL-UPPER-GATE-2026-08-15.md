# QP transverse return: actual-log fourth moment and a singleton upper gate

**Date:** 2026-08-15  
**Verdict:** the earlier `1/M_Y` transverse floor is not sharp once the
integer-log source of the actual nodes is used.  A robust fourth-moment
bound, including the unresolved cross-side pairs, proves

```text
s_v,r_+(H_Y;S_Y)>>_w sqrt(log Y)Y^[-(3-A)/2].       (0.1)
```

At the project aperture `A=50/33`, the exponent is

```text
(3-A)/2=49/66=.7424242424... .                      (0.2)
```

This is an unconditional asymptotic actual-node theorem.  It improves the
dimension-only exponent one, but it remains far below the return
`Y^(-(c-d))` required by `LTRAD_full`.

There is also a rigorous actual-node upper certificate for a calibrated
singleton event.  The unconditional Vinogradov--Korobov tent antenna gives

```text
s_v<=exp[-c_A(log Y/log log Y)^(1/3)]                (0.3)
```

for a legal singleton residual at every sufficiently large scale.  Thus the
actual singleton depth is bracketed between (0.1) and (0.3).  No matching
power upper bound is proved, and (0.3) does not apply to a strip-threshold
long interval whose probability depth is smaller than the VK error.

No fixed-power QP upper bound, strip-scale `LTRAD_full`, QP-to-strip
implication, or zero-free strip is proved here.

---

## 1. Setup and the divided-difference energy

Fix a half-integer `Y`, a fixed shell width `w`, and

```text
S_Y={n=p^k:Y exp(-w)<n<Y exp(w)},
u_n=|log(n/Y)|,
F_y(t)=sum_(n in S_Y)y_n cos(tu_n),
B=Y^A,                         1<A<2.               (1.1)
```

Let `rho_B(t)=B^-1 psi(t/B)`, where `psi` is a fixed nonnegative smooth
probability supported in `(1/3,2/3)`.  Its support lies in the full legal
band for large `Y`.

The clustered-frame theorem in the transverse-return report gives a
quadratic energy `E_Y(y)` with

```text
Q_2:=int F_y(t)^2rho_B(t)dt asyp E_Y(y),             (1.2)
|F_y(t)|<<sqrt(M_Y)Q_2^(1/2)       (0<=t<=B),        (1.3)
|int F_y rho_B|<<_K sqrt(M_Y)(Y/B)^K Q_2^(1/2).     (1.4)
```

For completeness, the energy treats a cross-side pair with positive
frequencies `u,u+delta` as

```text
|p|^2+min(1,B delta)^2|d|^2,
p=c_1+c_2,             d=c_1-c_2.                   (1.5)
```

Same-side frequencies are `>>1/Y` apart.  Hence only cross-side pairs can
have `B delta<1`, and every unresolved cluster has size two.

The new input is a fourth moment in terms of the same energy, rather than
the raw coefficient norm.

---

## 2. Robust perturbed-log fourth moment

### Lemma 2.1 (one-sign perturbed Dirichlet fourth moment)

Let `T` be any set of integers in `[cY,CY]`, let `sigma` be `+1` or `-1`,
and let real perturbations obey `|epsilon_n|<=C_0/B`.  Then

```text
int |sum_(n in T)b_n
          exp{it[sigma log(n/Y)+epsilon_n]}|^4 rho_B(t)dt
 <<Y^(2-A+o(1))(sum_n |b_n|^2)^2.                  (2.1)
```

If `T` consists of prime powers in the fixed shell, the sharper form is

```text
int |sum_(n in T)b_n
          exp{it[sigma log(n/Y)+epsilon_n]}|^4 rho_B(t)dt
 <<_w(1+Y^2/B)(sum_n |b_n|^2)^2.                  (2.1a)
```

The `o(1)` is uniform in `T`, the coefficients, and the perturbations.

#### Proof

Square the exponential sum.  Ordered pairs `alpha=(n_1,n_2)` carry
coefficient `b_(n_1)b_(n_2)` and frequency

```text
lambda_alpha=
 sigma log(n_1n_2/Y^2)+epsilon_(n_1)+epsilon_(n_2). (2.2)
```

The smooth `L^2(rho_B)` Gram entry of two pair frequencies is

```text
hat psi[B(lambda_alpha-lambda_beta)].                (2.3)
```

Write `k=n_1n_2`, `l=m_1m_2`; both are `asymp Y^2`.  Rapid decay gives,
for every fixed `K`,

```text
|(2.3)|<<_K
 [1+max(0,B|log(k/l)|-4C_0)]^(-K).                  (2.4)
```

Partition the possible `l` into integer intervals of length

```text
Delta=1+Y^2/B=Y^(2-A+o(1)).                         (2.5)
```

At distance `r Delta` from `k`, the right side of (2.4) is
`O_K((1+r)^(-K))`.  Each integer `l` has at most `d(l)=Y^o(1)` ordered
factorizations with both factors in `[cY,CY]`.  Therefore every absolute
Gram row has sum

```text
<<Y^o(1)Delta sum_(r>=0)(1+r)^(-K)
 <<Y^(2-A+o(1)).                                    (2.6)
```

Schur's test and

```text
sum_(n_1,n_2)|b_(n_1)b_(n_2)|^2=(sum_n|b_n|^2)^2  (2.7)
```

prove (2.1).

For (2.1a), observe that every integer `l` has only `O_w(1)` ordered
representations as a product of two shell prime powers.  With two prime
bases the factors are forced up to order.  For `l=p^L`, each factor
exponent lies in an interval of length `2w/log p`, so there are at most
`1+2w/log 2` possibilities.  Replacing the divisor bound in (2.6) by this
constant and summing the Schwartz tail directly gives `O_w(1+Y^2/B)`.
QED

This proof is stable at the exact resolution `1/B`; it does not assume
that the perturbed pair frequencies remain separated.

---

## 3. Fourth moment after quotienting reflected pairs

### Proposition 3.1 (clustered actual-log fourth moment)

For every signed coefficient vector on the complete actual node set,

```text
Q_4:=int F_y(t)^4rho_B(t)dt
 <<_w(1+Y^2/B)E_Y(y)^2
 <<_w(1+Y^2/B)Q_2^2.                                (3.1)
```

#### Proof

Fix a sufficiently large constant `kappa` and call a cross-side pair bad if

```text
|log(Y/n)-log(m/Y)|<=kappa/B.                       (3.2)
```

Such a pair obeys

```text
|nm-Y^2|<<_(w,kappa)Y^2/B.                          (3.3)
```

There are `O(1+Y^2/B)` possible integer products in (3.3), and the
prime-power product multiplicity from (2.1a) is `O_w(1)`.  Thus the number
`R_Y` of bad pairs and their endpoints satisfies

```text
R_Y<<_w1+Y^2/B.                                     (3.4)
```

No endpoint belongs to two bad pairs for large `Y`: the nodes on either
fixed side are `>>1/Y` apart, whereas `B^-1=o(Y^-1)`.

Write `F_y=G_y+J_y`, where `J_y` contains the complete two-coordinate
blocks of the bad pairs.  The divided-difference pointwise bound and the
clustered `L^2` frame give

```text
|J_y(t)|<<sqrt(R_Y)E_J^(1/2)       (0<=t<=B),
int J_y(t)^2rho_B(t)dt<<E_J.                        (3.5)
```

Consequently

```text
int J_y(t)^4rho_B(t)dt
 <=||J_y||_infinity^2 int J_y^2rho_B
 <<_w(1+Y^2/B)E_J^2.                               (3.6)
```

On the remaining nodes every two-point divided-difference factor is bounded
below by a fixed constant once `kappa` is chosen large.  Therefore

```text
sum_(n good)y_n^2<<E_G.                             (3.7)
```

The evenness of cosine now gives the exact original Dirichlet polynomial

```text
G_y(t)=Re P_y(t),
P_y(t)=Y^(-it)sum_(n good)y_n n^(it).                (3.8)
```

Apply the strengthened form (2.1a) with zero perturbation and (3.7):

```text
int G_y(t)^4rho_B(t)dt
 <=int |P_y(t)|^4rho_B(t)dt
 <<_w(1+Y^2/B)E_G^2.                               (3.9)
```

Finally, `|G+J|^4<=8(|G|^4+|J|^4)` proves the first inequality in (3.1),
and (1.2) proves the second.  QED

This is where actual integer-log structure first improves the dimension
bound.  The unresolved reflections themselves occupy only
`O_w(1+Y^2/B)` blocks, and after removing them the original symmetric cosine
sum is the real part of one ordinary Dirichlet polynomial.  A generic
harmonic Fejer model has neither property.

---

## 4. Fourth moment forces a larger positive return

Put

```text
R_1=int |F_y(t)|rho_B(t)dt,
m=int F_y(t)rho_B(t)dt,
h_0=sup_(t in supp rho_B)F_y(t).                     (4.1)
```

Interpolation between `L^1`, `L^2`, and `L^4` gives

```text
Q_2^(1/2)<=R_1^(1/3)Q_4^(1/6),
R_1>=Q_2^(3/2)/Q_4^(1/2)
    >>_w(1+Y^2/B)^(-1/2)Q_2^(1/2).                 (4.2)
```

Choose `K` in (1.4) so large that

```text
sqrt(M_Y)(Y/B)^K(1+Y^2/B)^(1/2)=o(1).              (4.3)
```

This is possible for every fixed `A>1`.  Equations (1.4) and (4.2) then
give `|m|=o(R_1)`.  The positive part satisfies

```text
int (F_y)_+ rho_B=(R_1+m)/2>=R_1/3.                 (4.4)
```

for all large `Y`.  In particular `h_0>0`, and because `rho_B` is a
probability,

```text
sup_(t in H_Y)F_y(t)>=h_0
 >>_w(1+Y^2/B)^(-1/2)Q_2^(1/2).                    (4.5)
```

Unlike the second-moment range inequality, (4.5) pays the fourth-moment
kurtosis rather than `sqrt(M_Y)` for the one-sided return.

---

## 5. Improved actual transverse and radial floors

Fix `0<=t_0<=B`, `0<D<=1`, and

```text
v=a(t_0)+Dq_0.                                      (5.1)
```

### Theorem 5.1 (actual-log transverse fourth-moment floor)

Uniformly in `t_0` and `D`, for all sufficiently large `Y`,

```text
s_v>>_w[M_Y(1+Y^2/B)]^(-1/2)
   >>_w sqrt(log Y)Y^[-(3-A)/2].                   (5.2)
```

#### Proof

For every signed dual `y`, point evaluation (1.3) gives

```text
|y dot v|=|F_y(t_0)+D F_y(0)|
 <<sqrt(M_Y)Q_2^(1/2).                              (5.3)
```

Combining (4.5), (5.3), and `M_Y<<_wY/log Y` shows, whenever
`y dot v<0`,

```text
sup_(t in H_Y)y dot a(t)
 >>_w[M_Y(1+Y^2/B)]^(-1/2)[-y dot v].              (5.4)
```

For `y dot v>=0`, (4.5) makes the support function nonnegative.  The
support-function characterization of `conv a(H_Y)` therefore puts
`-c_w[M_Y(1+Y^2/B)]^(-1/2)v` in that convex hull.  This direct inequality
also establishes feasibility rather than presupposing it.  QED

The same proof with the single evaluation `F_y(0)` gives:

### Corollary 5.2 (actual-log radial fourth-moment floor)

```text
r_+(H_Y;S_Y)>>_w sqrt(log Y)Y^[-(3-A)/2].           (5.5)
```

At `A=50/33`, (5.2)--(5.5) have exponent `49/66` and the displayed
`sqrt(log Y)` gain.  Exact transverse mixing
with a threshold event of probability depth `D>=Y^(-d+o(1))` gives only

```text
r_Y>=Y^[-(49/66+d)-o(1)],                           (5.6)
```

while the unconditional radial floor (5.5) is stronger.  Thus the theorem
does not close `LTRAD_full`.

---

## 6. A rigorous actual singleton upper certificate

The following general observation converts any positive QP-kill antenna
into a transverse upper bound.

### Lemma 6.1 (positive-antenna transverse upper bound)

Suppose `omega_j>=0`, `sum omega_j=1`, and

```text
P_omega(t)=sum_j omega_j cos(tu_j)>=-epsilon
                                      for t in H_Y. (6.1)
```

For a calibrated residual `v=a(t_0)+Dq_0`, if
`D+P_omega(t_0)>0`, then

```text
s_v<=epsilon/[D+P_omega(t_0)].                      (6.2)
```

#### Proof

Take

```text
y=-omega/[D+P_omega(t_0)].                          (6.3)
```

Then `y dot v=-1`, while

```text
sup_(t in H_Y)y dot a(t)
=-inf_(t in H_Y)P_omega(t)/[D+P_omega(t_0)]
<=epsilon/[D+P_omega(t_0)].                         (6.4)
```

The transverse dual bound proves (6.2).  QED

For every large half-integer `Y`, choose a shell prime with
`u_p` in a fixed subinterval of `(0,w)`; the prime number theorem supplies
one.  An odd multiple

```text
t_0=(2k+1)pi/u_p                                    (6.5)
```

lies in any prescribed polynomial Turan band with upper exponent greater
than one.  The singleton probability on `p` has `D=1`.

The unconditional actual-node VK tent theorem supplies positive weights
with

```text
epsilon_Y=exp[-c_A(log Y/log log Y)^(1/3)]           (6.6)
```

in (6.1).  Since `P_omega(t_0)>=-epsilon_Y`, Lemma 6.1 gives

```text
s_v<=epsilon_Y/(1-epsilon_Y)<<epsilon_Y.            (6.7)
```

This proves (0.3).  More generally, (6.2) is useful whenever the calibrated
depth exceeds the antenna error.  At a strip-threshold event
`D=Y^(-d+o(1))`, the VK error is asymptotically larger than `D`, so (6.2)
does not provide a long-interval upper bound.

---

## 7. Finite actual-node diagnostics

The exchange lab solves the finite-pool primal

```text
maximize s,
sum_t mu_t a(t)=-s v,       sum_t mu_t=1, mu_t>=0, (7.1)
```

and its dual `inf_(y dot v=-1)max_t y dot a(t)`.  A validation grid is
upgraded to a continuum upper guard using

```text
|F_y'|<=sum_j|y_j|u_j,
|F_y''|<=sum_j|y_j|u_j^2.                            (7.2)
```

The computations use floating-point HiGHS and cosine values.  Thus the
following are guarded floating brackets, not interval-arithmetic theorems.

Two residuals were tested at each base center `Y=N+1/2`:

1. an exact singleton resonance with `D=1`;
2. the broad prime interval maximizing the sampled mass-normalized negative
   direction in the Turan band.

The full return band was `[Y^.01,Y^(50/33)]`.

| `N` | `M_Y` | `1/M_Y` | singleton `s_v` | broad probability `D` | broad `s_v` |
|---:|---:|---:|---:|---:|---:|
| 70 | 9 | .111111 | [.450815,.451227] | .678416 | [.566355,.567366] |
| 200 | 17 | .0588235 | [.270727,.271059] | .576428 | [.470637,.471118] |
| 600 | 40 | .0250000 | [.243697,.244198] | .420918 | [.392253,.392917] |
| 1000 | 61 | .0163934 | [.202107,.202370] | .433871 | [.356662,.357417] |
| 1800 | 99 | .0101010 | [.162988,.163285] | .307446 | [.286906,.287286] |

Every final primal used exactly `M_Y` positive support heights.  The maximum
reported primal equality residual was below `3.4*10^-13`; the continuum
guards exceeded the refined dual maxima by the derivative allowance in
(7.2).  A temporary coefficient box used to prevent an unbounded first
coarse-grid dual was inactive in every final solution by more than five
orders of magnitude.

For the singleton midpoints,

```text
s_v sqrt(M_Y)=1.35, 1.12, 1.54, 1.58, 1.62,         (7.3)
```

whereas `s_v/Y^(-49/66)` grows from about `10.6` to `42.6` over the table.
These tiny scales therefore look closer to `M_Y^-1/2` than to either the
dimension floor `M_Y^-1` or the proved worst-case fourth-moment floor.
There is no monotone asymptotic range here, and the calculation does not
prove an exponent.  In particular, the broad events are far stronger in
probability depth than the strip-threshold events available asymptotically.

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_transverse_fourth_moment_gate.py \
  src/test_qp_transverse_sharpness_lab.py
PYTHONPATH=src python3 src/qp_transverse_sharpness_lab.py \
  --N 70 200 600 1000 1800 --phase-step .08 --iterations 8
```

---

## 8. Corrected frontier

```text
dimension-only actual transverse floor 1/M:          PROVED BUT NOT SHARP;
robust perturbed-log fourth moment:                   PROVED;
actual s_v floor Y^(-49/66-o(1)):                    PROVED;
actual radial floor Y^(-49/66-o(1)):                 PROVED;
actual singleton upper s_v<=VK subpower:             PROVED;
finite actual singleton/broad transverse brackets:   FLOATING DIAGNOSTICS;
matching actual power upper near Y^(-49/66):         OPEN;
long threshold-event upper or lower at c-d:          OPEN;
strip-scale LTRAD_full, QP upper, or uniform strip:  NOT PROVED.
```

Floating finite-scale diagnostics, clearly separated from these analytic
theorems, are implemented in `src/qp_transverse_sharpness_lab.py`.
