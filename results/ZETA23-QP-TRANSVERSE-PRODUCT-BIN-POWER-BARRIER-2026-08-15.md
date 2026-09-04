# QP transverse return: product-bin power barrier

**Date:** 2026-08-15  
**Verdict:** the factor

```text
Delta=Y^2/B=Y^(2-A)                                (0.1)
```

in the actual-node fourth-moment theorem cannot be replaced uniformly by
`Delta^(1-eta)` for any fixed `eta>0`.  This remains false after all proper
prime powers are removed, after restricting to one side of the center, and
after retaining the rank-one form of the product coefficients.  In fact a
real coefficient vector on a fixed one-sided prime cell satisfies

```text
(int F_y^4 rho_B)/(int F_y^2 rho_B)^2
 >>_w Delta/(log Y)^2.                              (0.2)
```

Thus a local semiprime sieve, an absolute product-bin Schur estimate,
signed Gram cancellation used only to improve the coefficient-uniform
fourth moment, or a large-value truncation cannot yield a fixed power gain
over the `49/66` transverse exponent.

This is a **method barrier**, not an upper bound on the true transverse
depth.  The vector below is not proved to be an extremal separator for a
strip-threshold calibrated residual.  A joint inequality exploiting both
`y dot v<0` and the long-event identity `lambda dot v=0` could still improve
`s_v`.  No such improvement, `LTRAD_full`, QP, or strip is proved here.

---

## 1. Prime product bins already have full power

Choose a fixed one-sided interval

```text
J_Y=[Y exp(eta_1),Y exp(eta_2)],
0<eta_1<eta_2<w,                                   (1.1)
```

and let `P_Y` be its primes.  The prime number theorem gives

```text
M=#P_Y asyp_w Y/log Y.                              (1.2)
```

The ordered products `pq`, `(p,q) in P_Y^2`, have logarithms in a fixed
interval.  Partition that interval into bins of width `epsilon/B`, with
fixed sufficiently small `epsilon>0`.  There are `O_w(B)` bins and `M^2`
ordered pairs.  Hence one bin contains at least

```text
M^2/O_w(B)>>_w Y^(2-A)/(log Y)^2
             =Delta/(log Y)^2                     (1.3)
```

pairs.

This has two immediate consequences.

First, no uniform local-semiprime estimate of the form

```text
every 1/B log-product bin contains O(Delta^(1-eta))
```

can hold.  Indeed `Delta/(log Y)^2` exceeds `Delta^(1-eta)` for every fixed
`eta>0` and all sufficiently large `Y`.

Second, the absolute Gram row sums used by Schur cannot have a power
saving.  Within the bin,

```text
|B log(pq/rs)|<=epsilon.                            (1.4)
```

Continuity and `hat psi(0)=1` make the absolute Fourier-kernel entry at
least a fixed positive constant when `epsilon` is small.  Thus the largest
absolute row sum is at least the right side of (1.3).  Rough-number or
upper-bound sieving may improve logarithms, but cannot change its power of
`Y`.

This argument is prime-only.  Splitting off proper powers does not affect
the obstruction.

---

## 2. Real rank-one analytic saturation

The bin count alone concerns an absolute pair-incidence matrix.  The next
argument shows that the exact positive fourth moment also has the same
power, for a real rank-one coefficient vector.

Let

```text
u_p=log(p/Y),
rho_B(t)=B^(-1)psi(t/B),                            (2.1)
```

where `psi` is the fixed smooth nonnegative probability used in the frame
theorem.  Choose a closed interval `I` strictly inside a region on which
`psi` is bounded below.  Averaging over `t_c in BI` gives, uniformly for
`p in P_Y`,

```text
(1/|BI|)int_(BI)cos^2(t_c u_p)dt_c
 =1/2+O_w(B^-1),                                   (2.2)
```

because `u_p` is bounded above and below by positive constants.  Therefore
some `t_c in BI` satisfies

```text
sum_(p in P_Y)cos^2(t_c u_p)>=M/3.                 (2.3)
```

Use the real coefficients

```text
y_p=-cos(t_c u_p),
F_y(t)=sum_(p in P_Y)y_p cos(tu_p),                 (2.4)
```

and set all other prime-power coefficients to zero.  Then

```text
F_y(t_c)=-sum_p cos^2(t_cu_p)<=-M/3.               (2.5)
```

The frequencies lie in a fixed compact interval.  Hence for a fixed
`delta_w>0`, the Lipschitz inequality preserves

```text
|F_y(t)|>=M/6             when |t-t_c|<=delta_w.   (2.6)
```

The interval in (2.6) remains in the region where `rho_B>>_wB^-1`, so

```text
int F_y(t)^4rho_B(t)dt>>_w M^4/B.                  (2.7)
```

All nodes are on one side and are `c_w/Y`-separated.  The smooth frame
upper bound and `sum y_p^2<=M` give

```text
int F_y(t)^2rho_B(t)dt<<_wM.                       (2.8)
```

Dividing (2.7) by the square of (2.8), and using (1.2), proves (0.2).

The coefficient vector in (2.4) is not an arbitrary vector on product
pairs: its squared-Dirichlet coefficients are exactly the rank-one tensor
`y_p y_q`.  The negative spike also shows why discarding a small set of
large values cannot improve the uniform one-sided moment input: the spike
has fixed time width and contributes the full lower bound (2.7).

---

## 3. What the barrier does and does not exclude

The fourth-moment proof of positive return has two independent costs:

```text
range cost:       Delta^(1/2),
endpoint cost:    M^(1/2).                          (3.1)
```

Sections 1--2 prove that the first cost cannot be reduced by any estimate
whose only new assertion is a coefficient-uniform improvement of the
product-bin fourth moment.  The following proposed refinements therefore
cannot give a fixed power improvement in that form:

```text
remove all proper powers;                           blocked by primes alone;
use local rough/semiprime density;                  at most logarithmic;
replace divisor Schur by rank-one product weights;  rank-one spike remains;
use exact signed Gram cancellation uniformly;       exact Q4 is saturated;
truncate exceptional large values uniformly;        fixed-width spike remains.
```

There is an important remaining logical opening.  The separator relevant
to transverse return is restricted by

```text
y dot v<0,
v=a(t_0)+Dq_0,
lambda dot v=0.                                    (3.2)
```

The construction in Section 2 proves no simultaneous extremality for the
ratio `h_Y(y)/[-y dot v]` when `(t_0,D,lambda)` comes from a long event of
strip-threshold depth.  A leverage--skewness tradeoff, a signed mixed
moment containing the endpoint functional, or new arithmetic forced by
the long prime event could evade this barrier.  Such a theorem would have
to use (3.2) essentially; it cannot follow from a smaller uniform
kurtosis constant.

---

## 4. Disposition

```text
prime-only bin occupancy >>Delta/log^2 Y:           PROVED;
uniform local-semiprime Delta^(1-eta) bound:         FALSE;
real rank-one kurtosis >>Delta/log^2 Y:              PROVED;
proper-power removal gives a power gain:             FALSE BY THIS METHOD;
uniform signed-Gram/L4 power gain:                   FALSE;
calibration-sensitive transverse power gain:         OPEN;
strip-scale transverse return, LTRAD_full, or QP:     NOT PROVED.
```

Executable replay:

- `src/qp_transverse_product_bin_barrier.py`;
- `src/test_qp_transverse_product_bin_barrier.py`.
