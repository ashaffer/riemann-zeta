# QP transverse return: mixed cubic incidence and the unsigned-energy barrier

**Date:** 2026-08-15  
**Verdict:** a nonstandard cubic endpoint argument can be made completely
uniform on the actual prime-power nodes, including unresolved reflected
pairs.  Its arithmetic input is a pair-to-node incidence operator of norm

```text
<<(1+Y^2/B)^(1/2).                                  (0.1)
```

It recovers the proved fourth-moment floor

```text
s_v >>_w [M_Y(1+Y^2/B)]^(-1/2),                    (0.2)
```

but does not improve its power.  At `B=Y^(50/33)`, this is the exponent
`49/66`, with the already proved factor `sqrt(log Y)`.

There is a rigorous obstruction to improving the power by unsigned
additive/multiplicative energy.  For the uniform coefficient vector on the
actual shell, the absolute `B^-1`-local pair-product energy is at least

```text
>>_w M_Y^2/B >>_w Y^(2-A)/(log Y)^2.                (0.3)
```

Thus no absolute-value packet-energy estimate can replace the exponent
`2-A` by `2-A-epsilon`.  A further fixed-power gain requires one of:

1. cancellation inside the short product packets;
2. a power-saving **rank-one** norm for the actual prime-log
   pair-to-node incidence tensors; or
3. a joint estimate showing that a dual with large calibrated leverage
   cannot also have large negative skewness.

These are genuinely new coefficient-sensitive prime-log Littlewood inputs.
No such input, no exponent below `49/66`, and no strip-scale return is proved
here.

---

## 1. Setup

Fix a half-integer `Y`, a fixed shell width `w`, and

```text
S_Y={n=p^j:Y exp(-w)<n<Y exp(w)},
F_y(t)=sum_(n in S_Y)y_n cos(t log(n/Y)),
B=Y^A,                         1<A<2.               (1.1)
```

Let `rho_B(t)=B^-1 psi(t/B)` be the smooth probability from the clustered
frame theorem.  Put

```text
m_y=int F_y rho_B,
Z_y=F_y-m_y,
V_y=int Z_y^2rho_B,
mu_3(y)=int Z_y^3rho_B.                             (1.2)
```

The clustered energy `E_Y(y)` satisfies

```text
V_y asyp_w E_Y(y),                                  (1.3)
|m_y|<<_(w,L)sqrt(M_Y)(Y/B)^L E_Y(y)^(1/2),        (1.4)
|F_y(t)|<<_w sqrt(M_Y)E_Y(y)^(1/2)  (0<=t<=B).     (1.5)
```

The mean in (1.4) is smaller than every fixed power required below after
choosing the fixed integer `L` sufficiently large.

---

## 2. A sharp one-sided cubic endpoint lemma

### Lemma 2.1

Let `Z` be a real random variable with

```text
E Z=0,        E Z^2=V>0,        E Z^3=mu_3,
H=ess sup Z.
```

Then, with `gamma=mu_3/V^(3/2)`,

```text
H/sqrt(V)>=(gamma+sqrt(gamma^2+4))/2.               (2.1)
```

In particular, if `gamma>=-S`, `S>=0`, then

```text
H>=sqrt(V)/(S+1).                                   (2.2)
```

#### Proof

For every real `a`, `(H-Z)(Z+a)^2>=0`.  Taking expectations and setting
`a=V/H` gives

```text
H V-mu_3-V^2/H>=0.                                  (2.3)
```

After division by `V^(3/2)`, (2.3) is

```text
x^2-gamma x-1>=0,             x=H/sqrt(V)>0.        (2.4)
```

This proves (2.1).  The right side of (2.1) is increasing in `gamma`, and

```text
(sqrt(S^2+4)-S)/2>=1/(S+1),                         (2.5)
```

which proves (2.2).  Two-point laws attain equality in (2.1), so no stronger
conclusion follows from the first three moments alone.  QED

This lemma uses the sign of the third moment.  It is not merely
`L^1-L^2-L^4` interpolation.

---

## 3. The actual pair-to-node incidence operators

First remove the complete two-coordinate blocks whose opposite-side
absolute-log gap is at most `kappa/B`.  As in the fourth-moment theorem,
there are

```text
R_Y<<_w1+Y^2/B                                      (3.1)
```

such blocks, their divided-difference part has cubic moment
`<<sqrt(R_Y)E_J^(3/2)`, and all mixed terms with the remaining coordinates
obey the same scale by Cauchy--Schwarz and the proved second and fourth
moment estimates.

It remains to audit the ordinary-coefficient part.  Write

```text
P_y(t)=Y^(-it)sum_(n good)y_n n^(it),
G_y(t)=Re P_y(t).                                    (3.2)
```

The expansion of `G_y^3` contains `P_y^3`, `P_y^2 conjugate(P_y)`, and
their conjugates.  The two relevant absolute kernel matrices are

```text
K_+((n_1,n_2),n_3)
 =|hat psi(B log(n_1n_2n_3/Y^3))|,

K_-((n_1,n_2),n_3)
 =|hat psi(B log(n_1n_2/(Y n_3)))|.                 (3.3)
```

For a fixed ordered pair `(n_1,n_2)`, varying the integer `n_3` changes the
logarithm by `asymp_w1/Y`; Schwartz decay and `B/Y->infinity` give

```text
sup_(n_1,n_2)sum_(n_3)K_+ + K_- <<_w1.             (3.4)
```

For fixed `n_3`, a nonnegligible entry confines the integer product
`k=n_1n_2` to an interval of length

```text
Delta_Y=1+Y^2/B.                                    (3.5)
```

A product of two shell prime powers has `O_w(1)` ordered representations:
two distinct prime bases determine the two factors up to order, while one
base permits only `O_w(1)` exponent splits inside the fixed shell.  Hence

```text
sup_(n_3)sum_(n_1,n_2)K_+ + K_- <<_w Delta_Y.       (3.6)
```

Schur's test applied from ordered pairs to nodes gives

```text
||K_+||_(2->2)+||K_-||_(2->2)<<_w sqrt(Delta_Y).   (3.7)
```

Since `||y tensor y||_2=||y||_2^2`, (3.7), the divided-difference split,
and (1.3) prove the uniform skewness estimate

```text
|mu_3(y)|<<_w sqrt(Delta_Y)V_y^(3/2).               (3.8)
```

The same conclusion follows less sharply in structure from
`|int Z^3|<=(int Z^2)^(1/2)(int Z^4)^(1/2)`.  Equations (3.3)--(3.7)
identify the exact mixed-moment arithmetic whose improvement would matter.

---

## 4. Why the cubic route stops at `49/66`

Lemma 2.1 and (3.8), with the negligible mean restored, give

```text
sup_(t in H_Y)F_y(t)
 >>_w Delta_Y^(-1/2)V_y^(1/2).                     (4.1)
```

For `v=a(t_0)+Dq_0`, `0<=t_0<=B`, `0<D<=1`, (1.5) gives

```text
[-y dot v]_+<<_w sqrt(M_Y)V_y^(1/2).               (4.2)
```

Therefore

```text
sup_(t in H_Y)F_y(t)
 >>_w[M_Y Delta_Y]^(-1/2)[-y dot v]_+.             (4.3)
```

Support-function separation proves (0.2).  The mixed cubic theorem thus
lands exactly at the fourth-moment exponent.

There is a useful exact joint formulation.  Define

```text
L_v(y)=[-y dot v]_+/V_y^(1/2),
Gamma_-(y)=max(0,-mu_3(y)/V_y^(3/2)).               (4.4)
```

The endpoint lemma gives, up to the negligible smooth mean,

```text
h_Y(y)/[-y dot v]_+
 >>1/{L_v(y)[1+Gamma_-(y)]}.                        (4.5)
```

The present separate estimates are

```text
L_v(y)<<sqrt(M_Y),
Gamma_-(y)<<sqrt(Delta_Y).                          (4.6)
```

Consequently a power improvement by mixed moments is reduced to the
coefficient-sensitive joint theorem

```text
sup_(y:y dot v<0)L_v(y)[1+Gamma_-(y)]
 <=Y^((3-A)/2-epsilon).                             (4.7)
```

Calibration supplies `lambda dot v=0`, but no currently proved estimate
uses it to establish (4.7).  Even the ideal bound `Gamma_-=O(1)` leaves the
generic leverage floor `M_Y^(-1/2)`; reaching a transverse exponent below
`1/2` necessarily requires calibrated leverage information as well.

---

## 5. Unsigned local energy cannot give a power saving

This obstruction is exact and uses the actual node count.  There are
`M_Y^2` ordered products `nm`, counted with multiplicity.  Their log
frequencies

```text
log(nm/Y^2)
```

all lie in an interval of length `4w`.  Partition that interval into
`O_w(B)` bins of width at most `1/B`, and let `N_b` be the number of ordered
products in bin `b`.  Then

```text
sum_b N_b=M_Y^2,
sum_b N_b^2>>_w M_Y^4/B.                            (5.1)
```

The second inequality is Cauchy--Schwarz.  For the uniform normalized
coefficient vector `y_n=M_Y^(-1/2)`, the absolute local pair-product energy
is therefore

```text
sum_b sum_(alpha,beta in b)
 |y_(alpha_1)y_(alpha_2)y_(beta_1)y_(beta_2)|
 =M_Y^(-2)sum_bN_b^2
 >>_w M_Y^2/B.                                      (5.2)
```

The prime number theorem in the fixed shell gives `M_Y asyp_wY/log Y`, so

```text
M_Y^2/B asyp_wY^(2-A)/(log Y)^2.                    (5.3)
```

Thus the exponent `2-A` in an **absolute-value** local energy estimate is
unimprovable, even on the actual prime-power set.  This does not show that
the signed smooth fourth moment, the negative cubic moment, or the true
transverse depth has that size: phases may cancel, and the calibrated
residual may exclude the worst coefficients.  It proves precisely that a
power gain cannot come from a smaller unsigned additive-energy count.

---

## 6. Frontier

```text
sharp cubic endpoint inequality:                    PROVED;
actual pair-to-node incidence norm <<sqrt(1+Y^2/B): PROVED;
mixed cubic recovery of the 49/66 floor:             PROVED;
unsigned local energy >=Y^(2-A)/log^2 Y:             PROVED;
uniform power improvement of absolute packet energy: FALSE;
power-saving signed/rank-one incidence theorem:      OPEN;
calibrated leverage--negative-skew joint bound:       OPEN;
actual exponent below 49/66:                         NOT PROVED;
LTRAD_full, QP, QP-to-strip, or a uniform strip:      NOT PROVED.
```

Executable exact checks:

- `src/qp_transverse_mixed_moment_barrier.py`;
- `src/test_qp_transverse_mixed_moment_barrier.py`.

Replay from the repository root:

```bash
python3 -m pytest -q src/test_qp_transverse_mixed_moment_barrier.py \
  src/test_qp_transverse_fourth_moment_gate.py \
  src/test_qp_transverse_sharpness_lab.py
```
