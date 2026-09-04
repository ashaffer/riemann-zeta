# LTRAD conditional prime-only reformulation and reflected-difference leverage suppression

**Date:** 2026-08-28  
**Verdict:** neither residual sector is eliminated from `LTRAD_full` as it is
currently stated.  Two narrower facts are rigorous.

1. **Conditional prime-only replacement.**  If a separate upper theorem
   proves the stronger ordinary-prime-supported statement `DPA_P`, then a
   prime-only radialization statement gives the identical Turan
   contradiction.  This does not follow from full-node DPA.  In the forward
   direction, a zero-free strip does produce a prime-only positive antenna,
   because deleting proper powers costs only `Y^(-1/2+o(1))` after
   normalization.
2. At the smaller Turan aperture `A'=1`, which is legal for directional
   exponent `d_dir=.001`, the antisymmetric coordinates of all Fourier-close
   reflected prime pairs contribute `o(epsilon_tr)` to the calibrated
   leverage of any putative transverse separator at the target scale
   `epsilon_tr=Y^{-(c_rad-d_dir)+o(1)}`.  A reflected-difference vector which
   carries a fixed share of the leverage has support function
   `>>Y^(1/33-o(1))`.

Even under the additional prime-only hypothesis, the unresolved object may
contain a Fourier-close, zero-carrier reflected corrector.  The estimate
below suppresses that corrector's **low-band calibration leverage** only; it
does not stop the corrector from cancelling the carrier at high-band
heights.  Nothing here proves `LTRAD`, DPA, QP, or a zero-free strip.

---

## 1. A separately proved prime-only DPA would be sufficient

Let

```text
P_Y={p prime:Y exp(-w)<p<Y exp(w)},
a_P(t)=(cos(t|log(p/Y)|))_(p in P_Y),
P_Y^mom=conv{a_P(t):t in H_Y},
r_P(H_Y)=sup{r>=0:-r q_P in P_Y^mom}.               (1.1)
```

Define `DPA_P(c_0)` by the existence, at every sufficiently large legal
center, of real coefficients supported only on `P_Y` such that

```text
sum_p y_p=1,
inf_(t in H_Y) sum_p y_p cos(t|log(p/Y)|)>=-Y^(-c_0).
                                                               (1.2)
```

Moment duality gives

```text
DPA_P(c_0) ==> r_P(H_Y)<=Y^(-c_0).                 (1.3)
```

For the same mass-normalized prime event used in the existing bridge, define

```text
LTRAD_P(c_rad,d_dir):
 e(I,Y,t_0)>=N^(-d_dir) ==> r_P(H_Y)>=N^(-c_rad).   (1.4)
```

### Proposition 1.1 (prime-only conditional strip chain)

If `DPA_P(c_0)` and `LTRAD_P(c_rad,d_dir)` hold with

```text
c_0>c_rad>0,                                       (1.5)
```

then the phase-localization and Turan arguments in the existing reverse
bridge give the same high-height strip of width

```text
(d_dir/A')^2,                                      (1.6)
```

provided the audited half-power coverage inequality holds.

#### Proof

Equations (1.3)--(1.5) exclude the premise of (1.4) for every sufficiently
large center.  Hence every mass-normalized negative prime event is smaller
than `N^(-d_dir)`.  The proved phase-localization comparison bounds the
natural Turan prime modulus by a fixed multiple of this quantity.  The
audited local Turan theorem then gives (1.6).  No proper-power coordinate
occurs in this chain.  QED

### Proposition 1.2 (a strip gives a prime-only positive antenna)

Fix `w>0`, fixed exponents `0<a<A<infinity`, and

```text
h in C_c^infinity((exp(-w),exp(w))),   h>=0,
c_h:=integral h(x)dx>0.                              (1.7)
```

For the ordinary primes in the shell define

```text
W_P(Y):=sum_p (log p)h(p/Y),
lambda_p:=(log p)h(p/Y)/W_P(Y).                      (1.8)
```

If zeta has a zero-free strip of width `0<delta<=1/2`, then `W_P(Y)>0`
for all sufficiently large `Y`, and for every `0<c<delta`,

```text
sum_p lambda_p cos(t|log(p/Y)|)>=-Y^(-c)
                   uniformly for Y^a<=t<=Y^A.       (1.9)
```

The fixed positive lower exponent `a` is part of the statement; no estimate
at heights tending to zero is asserted.

#### Proof

Let

```text
S_Y(t):=sum_n Lambda(n)h(n/Y)n^(-it),
R_Y(t):=sum_(k>=2,p) (log p)h(p^k/Y)(p^k)^(-it).
```

The established strip-to-QP contour argument gives, for every fixed
`eta in (0,delta)`,

```text
|S_Y(t)|<<Y^(1-delta+eta)       (Y^a<=t<=Y^A).      (1.10)
```

This is where `a>0` is used: Mellin decay makes the pole term negligible on
that aperture.  Independently of `t`, elementary counting gives

```text
|R_Y(t)|<<_h Y^(1/2)(log Y)^2.                      (1.11)
```

The normalization is checked separately at `t=0`, where (1.10) is not being
used.  The same contour argument with its pole term retained gives

```text
sum_n Lambda(n)h(n/Y)
 =c_hY+O(Y^(1-delta+eta)).                          (1.12)
```

Subtracting `R_Y(0)` and using (1.11) gives

```text
W_P(Y)=c_hY+O(Y^(1-delta+eta)+Y^(1/2)(log Y)^2)
      ~c_hY>0.                                      (1.13)
```

For `Y^a<=t<=Y^A`, the prime transform in (1.14) is the quotient of
`Y^(it)[S_Y(t)-R_Y(t)]` by `W_P(Y)`.  The factor `Y^(it)` has modulus one,
and therefore

```text
|sum_p lambda_p exp(-it log(p/Y))|
 <<Y^(-delta+eta)+Y^(-1/2)(log Y)^2.                (1.14)
```

Given `c<delta<=1/2`, choose `eta>0` with `delta-eta>c`; both terms in
(1.14) are then `o(Y^-c)`.  Taking real parts, and using the evenness of
cosine to replace `log(p/Y)` by its absolute value, proves (1.9).  QED

### Scope of the reduction

A general signed full-node DPA certificate need not project to a prime-only
certificate: deleting unbounded proper-power coefficients can destroy both
the carrier and its floor.  Thus (1.4) is the correct adapter only after a
separate proof of the stronger prime-supported upper theorem (1.2).
Proposition 1.2 shows that this formulation is compatible with the known
strip-to-QP direction; it does **not** supply `DPA_P` in the reverse
direction and does not remove proper powers from `LTRAD_full` itself.

---

## 2. A lower Turan aperture is legal at the benchmark directional exponent

The existing half-power coverage condition is

```text
r_d=(d/A')^(1/6),
(1+r_d)/[2A'(1-r_d)]<1.                             (2.1)
```

Take

```text
d_dir=.001,                  A'=1.                  (2.2)
```

Then `r_d=1/sqrt(10)` and the left side of (2.1) is

```text
(1+1/sqrt(10))/[2(1-1/sqrt(10))]
 =.9624752955...<1.                                  (2.3)
```

Thus the Turan event may be restricted to

```text
N^(1/2)<=t_0<=N,                                    (2.4)
```

while the QP radial measure still uses the full band with top

```text
B=Y^A,                 A=50/33.                     (2.5)
```

The resulting conditional strip width is `10^(-6)`.  For example, the
strict exponent choice

```text
c_0=.019,            c_rad=.0189                   (2.6)
```

is compatible with (1.5).

---

## 3. Fourier-close reflected pairs

Consider the ordinary-prime coordinates on the two sides of `Y`.  Join a
lower node `u_i` and an upper node `u_i'` only when

```text
B|u_i-u_i'|<=kappa                                  (3.1)
```

for one fixed `0<kappa<=1`.  These pairs are disjoint for large `Y`.  The exact
integer-product count from the covariance audit gives

```text
Delta:=1+Y^2/B=Y^(2-A+o(1)),
K:=#pairs <<Delta Y^o(1).                           (3.2)
```

On one such pair put `z_i=B|u_i-u_i'|` and write the coefficients in the
standard symmetric and scaled-antisymmetric coordinates

```text
p_i=y_i+y_i',
q_i=min(1,z_i)(y_i-y_i').                          (3.3)
```

The clustered energy contains `|p_i|^2+|q_i|^2`, up to the fixed norm
equivalence in the frame theorem.  On the pairs selected by (3.1),
`min(1,z_i)=z_i`; this identity, rather than an untruncated definition of the
energy coordinate, is used below.  Let `y^-` denote the pure antisymmetric
component on all selected pairs: its entries on pair `i` are
`((y_i-y_i')/2,-(y_i-y_i')/2)`, and hence its carrier is zero.  For
`t_0<=Y^(A'+o(1))`, the cosine Lipschitz estimate gives

```text
|F_(y^-)(t_0)|
 <<(t_0/B) sum_i |q_i|
 <<(t_0/B)sqrt(K) E_Y(y^-)^(1/2).                  (3.4)
```

This is the calibration gain: a close reflected difference is fully visible
near the top `B`, but is smaller by `t_0/B` in the Turan band.

Only pairs satisfying (3.1) are covered.  Cross-side pairs with
`B|u_i-u_i'|>kappa`, as well as unpaired coordinates, remain in the ordinary
carrier sector and are not suppressed by this argument.

The proved actual-log fourth-moment range theorem gives, for every complete
signed vector `y`,

```text
h_Y(y):=sup_(t in H_Y)F_y(t)
 >>Delta^(-1/2)E_Y(y)^(1/2).                       (3.5)
```

For the transverse mixing scheme, assume the useful exponent regime
`c_rad>d_dir>0`.  The required scale is not the final radial scale.  If the
directional event has depth `D>=Y^(-d_dir+o(1))`, then
`r_Y>=Ds_v/(1+s_v)` shows that the target
`r_Y>=Y^(-c_rad+o(1))` asks for

```text
epsilon_tr(Y):=Y^(-(c_rad-d_dir)+o(1))              (3.5a)
```

as the lower bound for the transverse return `s_v`.  A putative obstruction
is therefore a vector normalized by `y dot v=-1` with
`h_Y(y)<epsilon_tr(Y)`.

### Proposition 3.1 (difference leverage is nonextremal)

Let `v=a(t_0)+Dq_0`, and normalize a dual by `y dot v=-1`.  If the pure
close-reflection difference component supplies a fixed amount `eta>0` of
this leverage, namely

```text
|F_(y^-)(t_0)|>=eta,                                (3.6)
```

then

```text
h_Y(y)>>eta Y^(2A-A'-2-o(1)).                       (3.7)
```

#### Proof

The pair sum/difference blocks are orthogonal in `E_Y`, up to fixed norm
equivalence, so `E_Y(y)>=cE_Y(y^-)`.  Equations (3.2), (3.4), and (3.6)
give the following; the premise (3.6) makes `K>=1`, so the displayed
division is legitimate:

```text
E_Y(y)^(1/2)>>eta B/[t_0 sqrt(K)].                  (3.8)
```

Insert (3.8) into (3.5), use `sqrt(K)sqrt(Delta)
<=Y^(2-A+o(1))`, and use `t_0<=Y^(A'+o(1))`.  This is (3.7).  QED

At (2.2)--(2.5),

```text
2A-A'-2=2(50/33)-1-2=1/33.                         (3.9)
```

Therefore any reflected-difference component carrying fixed calibrated
leverage forces `h_Y(y)>>Y^(1/33-o(1))`; it cannot occur in a separator with
support function at the transverse target (3.5a).

There is a useful quantitative contrapositive.  If

```text
h_Y(y)<=epsilon,                                    (3.10)
```

then (3.5) bounds `E_Y(y)^(1/2)<<epsilon
Delta^(1/2)`.  Equations (3.2) and (3.4) yield

```text
|F_(y^-)(t_0)|
 <<epsilon Y^(A'+2-2A+o(1)).                       (3.11)
```

At `A'=1`, this is

```text
|F_(y^-)(t_0)|<<epsilon Y^(-1/33+o(1)).            (3.12)
```

Hence the close reflected differences contribute not merely `o(1)`, but
`o(epsilon)`, to the calibrated normalization of every putative extremal
separator.

At the benchmark `(c_rad,d_dir)=(.0189,.001)`, take

```text
epsilon=epsilon_tr=Y^(-.0179+o(1)).                 (3.13)
```

Then (3.12) reads

```text
|F_(y^-)(t_0)|<<Y^(-(.0179+1/33)+o(1))
                    =Y^(-.04820303...+o(1)).        (3.14)
```

This is a statement about low-band leverage, not deletion of `y^-`.

---

## 4. What remains under the additional prime-only formulation

Assume, in addition to the presently known results, that the separately
required `DPA_P` upper theorem in Proposition 1.1 has been proved.  Only in
that stronger formulation may the reverse bridge be run without
proper-power coordinates.  Split every Fourier-close cross-side pair as in
(3.3).  Proposition 3.1 shows that the calibrated leverage of a transverse
separator with `h_Y(y)<=epsilon_tr` lies, up to `o(epsilon_tr)`, in

```text
* unpaired ordinary-prime coordinates; and
* symmetric pair sums p_i.                          (4.1)
```

These are both ordinary-prime carrier coordinates.  The cluster hard-core
no-go in the companion report further shows that such a carrier cannot be
supported in a physical interval of diameter `Y^(.2417-epsilon_0)` at the
project DPA exponent, when the complete support and carrier-one hypotheses of
that theorem apply.  It does not by itself impose that localization statement
on an arbitrary transverse separator.

The remaining cancellation problem can therefore be stated as follows,
conditional on whatever carrier decomposition supplies those hypotheses:

> Prove that a delocalized ordinary-prime symmetric carrier with calibrated
> leverage `-1+o(1)` cannot have its positive high-band excursions hidden by
> a zero-carrier reflected corrector satisfying
> `E_Y(y^-)^(1/2)
> <<Y^(-(c_rad-d_dir)+(2-A)/2+o(1))`.

Indeed, this energy budget is exactly (3.5) with
`h_Y(y)<=epsilon_tr`:

```text
E_Y(y^-)^(1/2)<<E_Y(y)^(1/2)
 <<epsilon_tr Delta^(1/2)
 =Y^(-(c_rad-d_dir)+(2-A)/2+o(1)).                  (4.2)
```

At `A=50/33` and `(c_rad,d_dir)=(.0189,.001)`, the exponent on the right is

```text
-.0179+8/33=.22452424... .                          (4.3)
```

Thus (4.2) is a power-growth allowance, not an absolute bounded-energy or
small-energy conclusion.

Equation (3.12) proves that the corrector cannot create the leverage.  It
does not prove that the corrector cannot cancel the carrier at selected
high-band heights: the generic pointwise conversion from clustered energy
still costs a square root of the number of pairs.  This is the surviving
calibration-sensitive cancellation theorem.  No claim beyond that reduction
is made.
