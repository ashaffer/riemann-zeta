# QP signed-kernel capacity gate

**Date:** 2026-08-15  
**Verdict:** no fixed-power QP certificate is obtained.  There is an exact
capacity obstruction for the whole natural class of compact shell kernels
whose pole transform is nonnegative on the entire real line.  This class
contains autocorrelation kernels and the squared derivative/Chebyshev
filters tested below.

Let

```text
F(z)=integral_(-w)^w g(u)e^(zu)du,        F(0)>0,       (0.1)
```

where `g` is real and `C^2`, and suppose

```text
F(it)>=0                  for every real t.             (0.2)
```

Then, for every real `a` and every `eta>0`,

```text
sup_v (eta^2+v^2)|F(-a+iv)|
   >=(2 eta/w)F(0).                                  (0.3)
```

For the QP shell width `w=1/5`, the normalized floor in (0.3) is `10`
when `eta=1`.  Thus no such signed kernel can obey a vertically uniform
zero-side estimate

```text
|F(-a+iv)|<=epsilon_Y F(0)/(1+v^2)                  (0.4)
```

with `epsilon_Y=o(1)`, let alone `epsilon_Y=Y^(-c)`.  Making the resonant
value `F(-a)` tiny only moves the same normalized transform capacity to
nonzero ordinate offset.

This is exactly fatal to an argument which combines the
Vinogradov--Korobov zero-free region, local zero counting, and termwise
absolute values in the explicit formula.  It is **not** a no-go for signed
cancellation among the actual zeta zeros, and it is not a no-go for kernels
whose Fourier transform is constrained only on the finite moving QP band.
No QP statement and no zero-free strip is proved here.

---

## 1. General signed-shell explicit formula

For a real compact shell kernel put

```text
S_(g,Y)(t)=sum_n Lambda(n)/n * g(log(n/Y))
                              *exp[-it log(n/Y)].     (1.1)
```

The same contour calculation as for the tent gives

```text
S_(g,Y)(t)=F(-it)
 -sum_rho Y^(rho-1)F(rho-1-it)
 +R_(g,Y)(t).                                        (1.2)
```

For a fixed `C^2` kernel, the remainder has the usual power-small bound;
for a varying kernel `g=g_Y`, its constant depends on the vertical decay
and smoothness seminorms of `g_Y`.  Those constants must not be suppressed.

If (0.2) holds, the pole term has the correct sign.  A triangle-inequality
certificate must control, with `a=1-beta` and `v=gamma-t`,

```text
Y^(-a)|F(-a+iv)|.                                   (1.3)
```

The positive tent controls (1.3) by the VK factor times a fixed
`(1+v^2)^(-1)` envelope.  A signed filter would have to add a fixed power
of `Y` to that envelope.  The next theorem proves that this cannot happen
in the all-line pole-positive class.

## 2. Turan--Paley--Wiener capacity theorem

### Theorem 2.1 (vertical capacity conservation)

Let `g in C_c^2([-w,w])` be real, let `F` be (0.1), and assume (0.2).
Then

```text
F(0)<=w*g(0),                                         (2.1)

integral_R |F(-a+iv)|dv >= 2*pi*F(0)/w               (2.2)
```

for every real `a`.  Consequently (0.3) holds.

#### Proof

Condition (0.2) says that `g` is positive definite.  Periodize `g` with
period `w`:

```text
G(x)=sum_(k in Z)g(x+kw).                             (2.3)
```

Because `g` is continuous and supported on `[-w,w]`, its endpoint values
vanish and `G(0)=g(0)`.  The Fourier coefficients of `G` are

```text
c_n=F(2*pi*i*n/w)/w>=0.                              (2.4)
```

The `C^2` hypothesis makes the Fourier series absolutely convergent.
Therefore

```text
g(0)=G(0)=sum_n c_n>=c_0=F(0)/w,                    (2.5)
```

which is (2.1).  This interval Turan constant is sharp: the triangular
kernel has `F(0)=w*g(0)`.

For fixed real `a`, the function `v -> F(-a+iv)` is the Fourier transform
of `u -> e^(-au)g(u)`.  Fourier inversion at `u=0` gives

```text
2*pi*g(0)=integral_R F(-a+iv)dv.                    (2.6)
```

Taking absolute values and using (2.1) proves (2.2).  Finally, if the
left side of (0.3) is `M`, then

```text
integral_R |F(-a+iv)|dv
 <=M*integral_R dv/(eta^2+v^2)=pi*M/eta.             (2.7)
```

Combine (2.2) and (2.7).  QED

### Exact scope

The theorem does not say that the zero sum in (1.2) is large.  It says that
the transform cannot be made uniformly small on any whole vertical line.
Hence a proof which treats every zero term by absolute value and uses only
a uniform vertical envelope cannot improve the VK exponent.  A theorem
using the locations, phases, or cancellation of the actual zeros lies
outside this obstruction.

The all-real condition (0.2) is stronger than merely requiring the pole
term to be nonnegative for `t in [Y^.01,Y^(50/33)]`.  The latter larger
class remains open.  This distinction is essential.

## 3. Exact squared-Chebyshev test

The most favorable elementary derivative filter can indeed suppress all
resonant displacements in an interval.  Its failure is off resonance, not
at the interpolation step.

Fix `0<a_0<a_1` and put

```text
Delta=a_1^2-a_0^2,
xi=(a_1^2+a_0^2)/Delta,
chi(z)=[2z^2-(a_0^2+a_1^2)]/Delta,

C_m(z)=T_m(chi(z))/T_m(-xi),
P_m(z)=C_m(z)^2.                                    (3.1)
```

Then

```text
P_m(0)=1,
P_m(it)>=0                         (t real),
0<=P_m(-a)<=sech^2(m theta)        (a_0<=a<=a_1),   (3.2)

theta=arcosh(xi)=log[(a_1+a_0)/(a_1-a_0)].          (3.3)
```

The first inequality is exact Chebyshev minimax in the variable `z^2`
before squaring.  In particular, obtaining an error `exp(-kappa L)` in
this squared-polynomial family needs

```text
m >= arcosh(exp[(kappa L+O(1))/2])/theta
  =(kappa*a_1/(4a_0)+o(1))*L                        (3.4)
```

when `a_0/a_1 ->0`.

To realize the multiplier by an honest `C^2` compact kernel, set

```text
K=4m+4,
B_K(z)=[sinh(wz/K)/(wz/K)]^K.                       (3.5)
```

This is the bilateral transform of the `K`-fold convolution of the uniform
probability density on `[-w/K,w/K]`.  Its support is exactly `[-w,w]` and
its spline has `K-2=4m+2` continuous derivatives.  Applying the even
differential operator `P_m` leaves a real `C^2` signed kernel `g_m` with

```text
F_m(z)=P_m(z)B_K(z),
F_m(0)=1,
F_m(it)>=0                         for every t.      (3.6)
```

Moreover, since `B_K(-a)<=exp(wa)`,

```text
|F_m(-a)|<=exp(w a_1)sech^2(m theta)                (3.7)
```

throughout the desired displacement interval.  Thus the resonant filter
works exactly.

## 4. The forced off-resonant spike

Put

```text
t_m=pi*K/(2w),
eta_m=[2t_m^2+a_1^2+a_0^2]/Delta.                   (4.1)
```

Direct substitution, with no asymptotic estimate, gives

```text
F_m(i t_m)
 =[T_m(eta_m)/T_m(xi)]^2*(2/pi)^K.                  (4.2)
```

For fixed `a_1,w`, with `a_0/a_1` bounded away from `1` (in particular in
the VK regime `a_0/a_1 ->0`), and `m -> infinity`,

```text
log F_m(i t_m)=4m log m+O_(a_1,w)(m).               (4.3)
```

Thus the filter replaces the resonant error by a superexponentially large
off-resonant transform value.  In particular,

```text
||g_m||_1>=F_m(i t_m).                              (4.4)
```

For a VK displacement

```text
a_0 asymp L^(-2/3)(log L)^(-1/3)                    (4.5)
```

and fixed `a_1,kappa>0`, (3.4) requires

```text
m=Omega(L^(5/3)(log L)^(1/3)),                      (4.6)
```

while (4.3) is

```text
log F_m(i t_m)
 =Omega(L^(5/3)(log L)^(4/3)) >> kappa*L.           (4.7)
```

The order `t_m` is only polylogarithmic in `Y`, so this is not a spike
hidden beyond the polynomial QP aperture.  Higher-order B-splines repair
absolute convergence of (1.2), but do not repair its constants.  Making
the base still smoother redistributes the same capacity; Theorem 2.1 is
independent of this particular realization.

## 5. Actual prime-power coefficients and normalization

The filtered kernel does produce legal finite signed coefficients:

```text
c_n=Lambda(n)/n*g_m(log(n/Y))                       (5.1)
```

on the prescribed prime powers in the shell.  After grouping equal
absolute nodes,

```text
Re S_(g_m,Y)(t)=sum_j lambda_j cos(tu_j)             (5.2)
```

is in the exact signed Delsarte span.  There is no support or reality defect.

What is missing is the necessary lower bound.  If one had, uniformly on the
whole QP band,

```text
Re S_(g_m,Y)(t)>=-E_Y,
S_(g_m,Y)(0)>=c_0>0,
E_Y<=Y^(-kappa),                                    (5.3)
```

then

```text
Q(t)=1+Re S_(g_m,Y)(t)/E_Y                          (5.4)
```

would be a legal fixed-power Delsarte certificate.  Equations (0.3) and
(4.2) show that the VK-plus-absolute-values proof does not establish (5.3).
No cancellation theorem for the actual zero sum is supplied here.

## 6. Disposition

```text
signed compact actual-prime coefficients:                    LEGAL;
resonant Chebyshev suppression on every VK depth:             CONSTRUCTED;
nonnegative pole transform on the complete real line:         PROVED;
uniform vertical fixed-power suppression:                     IMPOSSIBLE IN CLASS;
VK + local zero count + termwise absolute values:             SUBPOWER ONLY;
finite-band-only pole positivity:                             NOT RULED OUT;
signed cancellation among actual zeta zeros:                  NOT RULED OUT;
QP KILL, QP PROMOTE, or a uniform zeta strip:                  NOT PROVED.
```

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_signed_kernel_capacity_gate.py
python3 results/verify_zeta23_qp_signed_kernel_capacity_gate.py
```
