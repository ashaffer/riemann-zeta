# QP transverse return: calibrated joint-invariant nonlinear laboratory

**Date:** 2026-08-15  
**Verdict:** finite actual-node evidence favors a calibrated joint bound at
the `sqrt(M)` to `sqrt(M) Delta^(1/4)` scale, rather than saturation of the
proved `sqrt(M Delta)` ledger.  This is evidence, not an asymptotic theorem.

For the explicit compact B-spline time laws tested here, the global
covariance-whitened cubic matricization norm is between `3.13` and `5.03` on
the full actual prime-power shells from `N=200` through `N=3000`.  Normalized
by `Delta^(1/4)`, it stays between `1.59` and `2.27`.  The optimized
calibrated candidates have still smaller negative skew, usually of order one,
and

```text
J_v/[sqrt(M) Delta^(1/4)]
```

decreases across the tested range for both singleton and broad calibrated
residuals.  Thus the finite data are consistent with a `41/66` transverse
exponent, and often look closer to `1/2`.  They do not prove either exponent.

One proposed extremizer can be ruled out rigorously.  If `Y=N+1/2`,
`B=Y^(50/33)`, and coefficients are supported on the short right window

```text
Y<n<=Y+Y/sqrt(B),
```

then half-integer parity forces every signed triple log frequency away from
zero.  Under every fixed-order B-spline law used here, the standardized third
moment of **every** vector on this packet tends to zero by a fixed power.  In
particular, uniform negative coefficients on the primes in this interval do
not produce `Delta^(1/4)` skew.

No uniform joint theorem on the whole shell, no exponent below `49/66`, no
new lower bound for `s_v`, no QP statement, and no uniform strip are proved in
this report.

---

## 1. The calibrated invariant

For actual shell nodes

```text
u_j=|log(n_j/Y)|,       n_j=p^a,
F_y(t)=sum_j y_j cos(tu_j),
```

let `rho_B` be a probability on `[B/3,2B/3]`, and put

```text
m_y=E F_y,
Z_y=F_y-m_y,
V_y=E Z_y^2,
mu_3(y)=E Z_y^3.
```

For a calibrated residual `v`, define

```text
L_v(y)=[-y.v]_+/sqrt(V_y),
Gamma_-(y)=max(0,-mu_3(y)/V_y^(3/2)),
J_v(y)=L_v(y)[1+Gamma_-(y)].                       (1.1)
```

The one-sided cubic endpoint lemma reduces a transverse return estimate to an
upper bound on `sup_(y:y.v<0) J_v(y)`.  The proved separate estimates

```text
L_v<<sqrt(M),             Gamma_-<<sqrt(Delta),
Delta=1+Y^2/B,                                      (1.2)
```

give `J_v<<sqrt(M Delta)` and the exponent `49/66` when
`B=Y^(50/33)`.  A bound `Gamma_-<<Delta^(1/4+o(1))` compatible with calibrated
leverage would instead give the exponent

```text
1/2+(2-50/33)/4=41/66.                              (1.3)
```

The purpose of the laboratory is to test the genuinely joint quantity (1.1),
not its two separate worst-case factors.

---

## 2. Exact-transform continuum moments

The order-`q` time law is explicit:

```text
T=B/2+U_1+...+U_q,
U_r uniform on [-B/(6q),B/(6q)].                   (2.1)
```

It is a probability supported exactly on `[B/3,2B/3]`.  Its characteristic
function and cosine transform are

```text
Phi_B(omega)=exp(iBomega/2)sinc(Bomega/(6q))^q,
C_B(omega)=cos(Bomega/2)sinc(Bomega/(6q))^q.        (2.2)
```

Consequently no time grid is used.  The floating arrays are evaluated from
the exact identities

```text
m_i=C_B(u_i),
R_ij=1/2[C_B(u_i-u_j)+C_B(u_i+u_j)],

Q_ijk=1/4 sum C_B(+-u_i+-u_j+-u_k),                (2.3)
```

where the last sum is the four cosine-product sign patterns.  The covariance
and centered third tensor are then

```text
Sigma_ij=R_ij-m_i m_j,
T_ijk=Q_ijk-m_iR_jk-m_jR_ik-m_kR_ij+2m_i m_j m_k. (2.4)
```

An independent continuum quadrature test for `q=1` checks every entry of
(2.3)--(2.4).  The formulas are continuum identities; their numerical
evaluation is ordinary double precision, not interval arithmetic.

---

## 3. A global floating cubic guard

Let `W` be covariance whitening on the retained range:

```text
W^T Sigma W=I,             y=Wx,       ||x||_2=1. (3.1)
```

Write

```text
a=W^T v,
Ttilde=T[W,W,W].                                    (3.2)
```

Then `L_v=-a.x` on the legal half-sphere, and the negative skew is
`max(0,-Ttilde[x,x,x])`.  Flattening the first mode of the tensor gives the
global inequality

```text
|Ttilde[x,x,x]|
 <=||Mat_1(Ttilde)||_(2->2) ||x||_2 ||x tensor x||_2
 = ||Mat_1(Ttilde)||_(2->2).                       (3.3)
```

Thus, for the computed floating moment arrays, every legal vector satisfies

```text
J_v(y)<=||a||_2[1+||Mat_1(Ttilde)||_(2->2)].       (3.4)
```

This is a global guard, unlike a local nonlinear optimum.  It remains a
floating finite-dimensional statement; no rounding enclosure or asymptotic
bound for the matrix norm is supplied.

The signed cubic itself is attacked independently by tensor-power-informed
multistart sphere ascent.  Its candidate is always below (3.3), as required.

---

## 4. Exact stationary identity for the joint optimizer

On the active branch put

```text
L=-a.x>0,               g=-Ttilde[x,x,x]>0.
```

Stationarity of `L(1+g)` on the unit sphere gives the exact identity

```text
-(1+g)a-3L Ttilde[x,x,.]=L(1+4g)x.                 (4.1)
```

If the skew branch is inactive, the identity is simply `-a=Lx`.  Equation
(4.1) is used as an a posteriori check; it is also a compact exact
characterization of any smooth extremizer.  Across the primary runs below,
the relative stationary residual is between about `10^-9` and `2.3*10^-4`.

Every reported joint candidate is explicitly checked to satisfy

```text
y.v=-L<0,             y^T Sigma y=1.               (4.2)
```

The residuals are actual calibrated ones:

* `singleton`: a legal odd prime resonance, with coordinate calibration and
  `D=1`;
* `broad`: a sampled/refined prime interval, with uniform interval
  calibration and `D` equal to its measured negative mean.

Both replay `lambda.v=0` to floating error.

---

## 5. Primary actual-node results

The main run uses `q=8`, shell width `w=0.2`, `B=Y^(50/33)`, and 16 starts.
Here `C_cand` is the unconstrained negative-cubic candidate and `C_up` is the
global matricization bound (3.3).

| `N` | `M` | `Delta^(1/4)` | `C_cand` | `C_up` | `C_up/Delta^(1/4)` |
|---:|---:|---:|---:|---:|---:|
| 200 | 17 | 1.937 | 2.158 | 3.130 | 1.616 |
| 600 | 40 | 2.196 | 4.250 | 4.975 | 2.266 |
| 1000 | 61 | 2.330 | 2.298 | 3.931 | 1.687 |
| 1800 | 99 | 2.497 | 1.845 | 3.973 | 1.591 |
| 3000 | 151 | 2.653 | 1.976 | 5.027 | 1.895 |

The joint candidates are:

| `N` | singleton `Gamma_-` | singleton `J/sqrt(M)` | singleton `J/[sqrt(M)Delta^(1/4)]` | broad `Gamma_-` | broad `J/sqrt(M)` | broad `J/[sqrt(M)Delta^(1/4)]` |
|---:|---:|---:|---:|---:|---:|---:|
| 200 | 1.643 | 4.450 | 2.298 | 1.411 | 2.995 | 1.547 |
| 600 | 2.382 | 5.552 | 2.529 | 1.361 | 2.529 | 1.152 |
| 1000 | 1.352 | 3.015 | 1.294 | 1.195 | 1.724 | 0.740 |
| 1800 | 1.064 | 2.875 | 1.152 | 0.911 | 1.638 | 0.656 |
| 3000 | 1.108 | 2.832 | 1.067 | 0.882 | 1.456 | 0.549 |

For comparison, applying the **global** bound (3.4) and normalizing by the
`41/66` proxy gives respectively

```text
singleton: 4.48, 7.96, 4.00, 3.73, 4.14,
broad:     3.26, 4.86, 2.14, 2.21, 2.23.          (5.1)
```

Thus even the global floating guard, which covers every coefficient vector
in each finite model, is compatible with `sqrt(M)Delta^(1/4)`.  The local
joint candidates are materially smaller and trend downward after the small
scales.  The range is much too short and noisy for an exponent fit to be a
theorem.

There is a conspicuous pre-asymptotic anomaly at `N=70`: the covariance
minimum eigenvalue is about `1.4*10^-4`, and `J/sqrt(M)` is roughly `39`--`45`.
It is excluded from the primary scaling table rather than hidden in a fit.

---

## 6. Packet structure and order robustness

The maximizing vectors do not have one stable geometry.

* Broad candidates are often diffuse: their coefficient effective support is
  about `42/61` at `N=1000` and `71/151` at `N=3000`.
* Singleton candidates can lock onto a reflected near-pair.  At `N=3000`,
  four coordinates carry 90% of the coefficient square mass and 91.4% lies
  on unresolved opposite-side reflection endpoints.
* This localization makes singleton values volatile, but it does not create
  `sqrt(Delta)` skew in the tested range.
* Crude signed-versus-absolute product-bin ratios are close to one.  These
  bins are not the centered smooth cubic tensor, so this observation is not a
  cancellation theorem.

The qualitative picture persists when the spline order is changed.  The
table gives the global cubic bound divided by `Delta^(1/4)`, followed by the
two joint `41/66` normalizations.

| `q` | `N` | `C_up/Delta^(1/4)` | singleton `J/41` | broad `J/41` |
|---:|---:|---:|---:|---:|
| 4 | 600 | 1.687 | 1.743 | 0.817 |
| 4 | 1000 | 1.456 | 1.120 | 0.666 |
| 4 | 1800 | 1.356 | 1.016 | 0.577 |
| 8 | 600 | 2.266 | 2.529 | 1.152 |
| 8 | 1000 | 1.687 | 1.294 | 0.740 |
| 8 | 1800 | 1.591 | 1.152 | 0.656 |
| 12 | 600 | 2.586 | 3.053 | 1.109 |
| 12 | 1000 | 1.830 | 1.452 | 0.805 |
| 12 | 1800 | 1.740 | 1.284 | 0.753 |

Finite constants depend on the smooth time law, especially for singleton
residuals.  The decreasing normalized trend and the order of the global
cubic guard are stable across these three choices.

---

## 7. The short right-window packet is anti-resonant

The suggested test vector was uniform negative mass on primes

```text
P={p prime:Y<p<=Y+Y/sqrt(B)},       Y=N+1/2.        (7.1)
```

It does not generate large negative skew for the laws (2.1).

### Proposition 7.1 (half-integer cubic suppression)

Let `q>=1` be fixed, `B>=6Y`, and let `S` be any set of integer nodes in the
interval in (7.1), not necessarily primes.  Put `K=|S|` and

```text
epsilon=min(1,(24qY/B)^q),
eta=1/2-K(epsilon+epsilon^2).                       (7.2)
```

If `eta>0`, then every real coefficient vector supported on `S` satisfies

```text
y^T Sigma y>=eta ||y||_2^2,
|mu_3(y)|/V_y^(3/2)
 <=(4epsilon+2epsilon^3)K^(3/2)/eta^(3/2).         (7.3)
```

#### Proof

Write `n=Y+h`.  Since `Y` is half-integral and `n` is integral, every `h` is
a half-integer.  For `0<h<=Y/sqrt(B)`,

```text
0<=h/Y-log(1+h/Y)<=h^2/(2Y^2)<=1/(2B).            (7.4)
```

Every signed sum of three `h`'s is a nonzero half-integer, so (7.4) gives

```text
|+-u_i+-u_j+-u_k|>=1/(2Y)-3/(2B)>=1/(4Y).         (7.5)
```

The same lower bound holds for every nonzero single or pair frequency that
occurs in the first and second moments.  By (2.2),

```text
|C_B(omega)|<=min(1,(6q/(B|omega|))^q)<=epsilon.  (7.6)
```

The covariance diagonal differs from `1/2` by at most
`epsilon/2+epsilon^2`, while an off-diagonal entry has absolute value at most
`epsilon+epsilon^2`.  Gershgorin therefore gives the first inequality in
(7.3).

Each raw third entry has absolute value at most `epsilon`.  Using (2.4) and
`|R_ij|<=1` gives

```text
|T_ijk|<=4epsilon+2epsilon^3.                       (7.7)
```

Finally, `||y||_1<=sqrt(K)||y||_2`, so (7.7) and the covariance lower bound
give the second inequality in (7.3).  QED

Since `K<=Y/sqrt(B)+1`, at `B=Y^(50/33)` the right side of (7.3) is

```text
O_q(Y^((12-17q)/33)).                              (7.8)
```

It decays already for `q=1`, and very rapidly for `q=8`.  The obstruction is
exactly the half-integer parity: three half-integers cannot sum with signs to
zero.  It is the opposite of a cubic revival.

Exact-transform floating evaluations of the uniform negative prime vector
illustrate the theorem:

| `N` | prime count `K` | `Delta^(1/4)` | measured `|Gamma|` | rigorous upper from (7.3) |
|---:|---:|---:|---:|---:|
| `10^8` | 6 | 9.326 | `4.72e-21` | `3.29e-13` |
| `10^10` | 11 | 16.298 | `5.72e-41` | `4.68e-21` |
| `10^12` | 30 | 28.480 | `2.04e-36` | `1.21e-28` |

The measured values are floating diagnostics; the analytic column follows
from Proposition 7.1.  This proposition rules out this short one-sided packet
as a quarter-power extremizer.  It does not rule out packets spanning both
sides of the shell, reflected divided-difference modes, or a different time
law.

---

## 8. What remains open

The data narrow the most plausible next theorem to a rank-one signed cubic
estimate on the **full** actual shell, after reflected pairs are handled:

```text
sup_(y!=0) |mu_3(y)|/V_y^(3/2)
 <<Delta^(1/4+o(1)),                                (8.1)
```

or, more economically, the calibrated joint version

```text
sup_(y:y.v<0) J_v(y)<<sqrt(M)Delta^(1/4+o(1)).     (8.2)
```

The finite matricization values support (8.1), but do not reveal the
arithmetic proof.  Proposition 7.1 says the hard vectors cannot live only in
the shortest one-sided integer packet.  The remaining likely sources are
cross-side reflected clusters and longer product-incidence packets.

The nonlinear candidates are lower bounds on the true finite supremum.  The
matricization guards are global upper bounds only for the evaluated floating
arrays.  Neither class of computation is an interval certificate or an
asymptotic estimate.

---

## 9. Reproduction

Implementation and tests:

```text
src/qp_transverse_joint_invariant_lab.py
src/test_qp_transverse_joint_invariant_lab.py
```

Representative commands:

```bash
PYTHONPATH=src python3 src/qp_transverse_joint_invariant_lab.py \
  --N 200 600 1000 1800 3000 --starts 16 --spline-order 8 --seed 0

PYTHONPATH=src python3 src/qp_transverse_joint_invariant_lab.py \
  --N 200 --starts 2 --short-window-N 100000000 10000000000 1000000000000

PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_transverse_joint_invariant_lab.py
```

Current test result: `7 passed`.  The tests include direct continuum
quadrature of all first, second, and third moment entries, covariance replay,
the global cubic inequality, the stationary identity, both actual
calibrations, scale-invariant packet diagnostics, and the half-integer bound.
