# Positive spectral prime nulling: the compact-factorization theorem and the square-root gate

Status: focused exact reduction and construction audit, 2026-08-12.  A
positive atomic moment solution is proved to descend to a genuine compact
scalar two-lobe packet while retaining its central-atom carrier.  A
fixed-power `Y^(-1)` exact construction is also proved.  A subpower lower
bound for the optimized central atom is **not** proved; the present finite
LP data are compatible with the generic square-root scale.  No zero-free
strip is claimed.

## 1. Verdict

Let

```text
u_j=log(n_j/Y_c)                                      (1.1)
```

be the active prime-power offsets in a fixed logarithmic window, and put

```text
v(xi)=(cos(xi*u_1),...,cos(xi*u_M)).                  (1.2)
```

The positive spectral proposal is exactly the following convex problem:

```text
mu=w_0*delta_0+(1-w_0)*nu,
supp(nu) subset {xi:Y<=abs(xi)<=T},
integral cos(xi*u_j)dmu(xi)=0       for every j.      (1.3)
```

Here `nu` is an even probability measure.  Write

```text
r=w_0/(1-w_0).                                       (1.4)
```

Then (1.3) is equivalent to

```text
-r*1 belongs to conv{v(xi):Y<=xi<=T}.                (1.5)
```

There are two distinct conclusions.

1. **The analytic-factorization step works.**  If (1.3) has a solution,
   multiplying its characteristic function by a fixed smooth compact
   positive-definite autocorrelation preserves every zero and compact
   support.  Krein's continuous Fejer--Riesz factorization then gives a
   compact scalar lobe.  Since every noncentral atom has frequency at least
   `Y`, its off-axis Laplace carrier is

   ```text
   w_0*(fixed carrier)+O_A(Y^(-A)).                  (1.6)
   ```

   Thus a proved lower bound `w_0>=Y^(-o(1))` would genuinely solve the
   cross-prime nulling/carrier gate.  The two-lobe sine factor does not
   introduce another power loss.

2. **That lower bound is presently missing.**  The exploratory optima

   ```text
   Y       30       100       300       1000
   w_0   .202      .163      .121      .0738          (1.7)
   ```

   are compatible with `w_0 asymp M^(-1/2)`, equivalently
   `sqrt(log Y/Y)`.  They do not validate a `c/log Y` law.  The square-root
   interpretation would be a fixed half-power loss, not a subpower carrier.
   These four finite computations neither prove that square-root decay is
   asymptotic nor rule out a better actual-prime construction.

The new exact advance is therefore (1.6): **positive atomic prime nulling
is not merely a formal LP surrogate; it has a lossless compact two-lobe
realization at the scale of `w_0`.**  The remaining problem is the
one-dimensional convex inradius (1.5).

## 2. Exact primal and dual

Let

```text
K=conv{v(xi):Y<=xi<=T} subset R^M.                   (2.1)
```

Since an even measure on the two-sided band has the same cosine moments as
a measure on `[Y,T]`, (1.3) gives

```text
0=w_0*1+(1-w_0)*integral v(xi)dnu(xi).               (2.2)
```

This proves (1.5), and the converse follows by representing a point of `K`
by a probability measure.  In finite dimension, Caratheodory reduces that
measure to at most `M+1` noncentral frequencies.  Thus there is no
compactness or infinite-dimensional qualification hidden in (1.5).

For `a in R^M`, define

```text
A(a)=sum_j a_j,
h(a)=sup_(Y<=xi<=T) sum_j a_j*cos(xi*u_j).            (2.3)
```

The exact separation dual is

```text
-r*1 in K
iff
h(a)+r*A(a)>=0                    for every a.        (2.4)
```

In particular, for arbitrary nonnegative `lambda_j`, take
`a_j=-lambda_j`.  Every feasible `r` obeys

```text
r <= - min_(Y<=xi<=T)
          sum_j lambda_j*cos(xi*u_j)
        / sum_j lambda_j.                            (2.5)
```

Equation (2.5) is the exact positive-quadrature obstruction.  Conversely,
proving (2.4) for `r=Y^(-o(1))` is exactly the required inradius theorem;
a dimension surplus by itself does not prove it.

One elementary bound is worth recording.  At any one zero,

```text
w_0
 =abs(integral cos(xi*u_j)d(mu-w_0*delta_0)(xi))
 <=1-w_0,
```

and hence

```text
w_0<=1/2.                                            (2.6)
```

This bound is sharp for a single node and says nothing useful about the
many-node decay.

### 2.1 What the audited prime quadrature proves

Choose nonnegative smooth weights `lambda_j` from a compact
positive-definite logarithmic window, so that the corresponding continuum
cosine transform is nonnegative.  The audited von-Mangoldt/KMT quadrature
gives, uniformly on the present frequency band,

```text
min_xi sum_j lambda_j*cos(xi*u_j)
 >=-C*(log Y)^(-3/10)*sum_j lambda_j.                (2.7)
```

Equations (2.5) and (2.7) imply

```text
r<< (log Y)^(-3/10),
w_0<< (log Y)^(-3/10).                              (2.8)
```

This is an upper bound only.  It is compatible with the desired
`Y^(-o(1))` lower bound and also with a square-root-power optimum.  A
square-root upper bound for the actual prime-log curve would require a
much sharper uniform lower bound for the negative excursions in (2.5).
No such actual-prime theorem is currently available in the audited input.

## 3. Compact positive-definite transfer

We now prove that the atomic LP is the right problem rather than a
nonfactorable relaxation.

### Theorem 3.1 (atomic-to-compact carrier transfer)

Let `mu` satisfy (1.3), and let

```text
phi(u)=integral exp(i*xi*u)dmu(xi)
      =w_0+(1-w_0)*integral cos(xi*u)dnu(xi).         (3.1)
```

Let `R_0` be a real even `C_c^infinity` positive-definite function,
supported in `[-a,a]`, and suppose

```text
C_0(alpha)=integral R_0(u)*exp(alpha*u)du>0           (3.2)
```

for the fixed depth `alpha`.  Define

```text
R(u)=R_0(u)*phi(u).                                  (3.3)
```

Then:

1. `R` is real, even, smooth, compactly supported, and positive definite;
2. `R(u_j)=0` for every active offset;
3. there is a compactly supported scalar `q` with

   ```text
   R=q*tilde(q),       tilde(q)(x)=conj(q(-x));       (3.4)
   ```

4. for every fixed `A`, uniformly for `alpha` in a fixed compact set,

   ```text
   C_R(alpha):=integral R(u)*exp(alpha*u)du
    =w_0*C_0(alpha)+O_(A,R_0)(Y^(-A)).               (3.5)
   ```

If the standard smooth spectral factor is selected, `q` may be taken
smooth and supported in an interval whose difference set is contained in
`[-a,a]`.

#### Proof

The characteristic function `phi` is positive definite by Bochner's
theorem.  Products of positive-definite functions are positive definite,
so (3.3) has all the properties in part 1.  Part 2 is immediate from
`phi(u_j)=0`.

Let `W` be the Fourier transform of `R`.  It is a nonnegative integrable
entire function of finite exponential type.  Krein's continuous
Fejer--Riesz theorem factors it as

```text
W(z)=Q(z)*conj(Q(conj(z))),                          (3.6)
```

where `Q` has half the exponential type and belongs to the appropriate
Paley--Wiener space.  The inverse Fourier transform `q` is compactly
supported and (3.4) follows.  The rapid decay inherited from smooth `R_0`
gives the smooth version.

Finally put

```text
C_0(alpha+i*xi)=integral R_0(u)
                         *exp(alpha*u+i*xi*u)du.      (3.7)
```

Repeated integration by parts gives

```text
abs C_0(alpha+i*xi)<=C_(A,R_0)*(1+abs(xi))^(-A).     (3.8)
```

Every noncentral frequency of `mu` has absolute value at least `Y` and
total mass `1-w_0`.  Substitution of (3.1) in (3.3), followed by (3.8),
proves (3.5).  QED

The spectral-gap hypothesis in the last paragraph is essential.  An
arbitrary positive-definite product which has low nonzero spectral atoms
may still have those atoms contribute at full size to (3.5).

The theorem is an exact compact-support statement, not by itself a uniform
finite-Gabor truncation theorem at the upper spectral endpoint.  Such a
transfer also needs the noncentral support to stay inside the available
relative-frequency aperture by a growing margin.  The strict `d<2/3`
constructions below have that margin; the bare allowance `abs(xi)<=T` in
(1.3) does not supply it at `abs(xi)=T`.

## 4. The exact two-lobe sine factor

Translate the factor in (3.4) by a separation `D` and set, in a target-
aligned modulation gauge,

```text
p_D(x)=q(x)-q(x-D).                                  (4.1)
```

Its autocorrelation is exactly

```text
R_p(u)=2R(u)-R(u-D)-R(u+D),                          (4.2)
```

and on the real spectral line

```text
abs(p_hat(xi))^2
 =4*sin^2(xi*D/2)*abs(q_hat(xi))^2.                 (4.3)
```

For the bilateral Laplace response,

```text
C_p(alpha)
 =[2-exp(alpha*D)-exp(-alpha*D)]*C_R(alpha)
 =-4*sinh^2(alpha*D/2)*C_R(alpha).                  (4.4)
```

Thus (3.5) gives the negative selected carrier

```text
C_p(alpha)
 =-4*sinh^2(alpha*D/2)
    *[w_0*C_0(alpha)+O_A(Y^(-A))].                  (4.5)
```

There is no additional square-root or sine loss at the aligned off-axis
point.

If `D` is larger than the support radius plus the active logarithmic
window, then at a cross-prime point `D+u_j`,

```text
R_p(D+u_j)=-R(u_j)=0.                               (4.6)
```

Equations (4.2) and (4.6) use the **full** autocorrelation.  In particular,
all coherent cross terms between the internal spectral bands produced by
the factorization are already present; none has been discarded by a
diagonal-intensity approximation.

The same-lobe prime rows, pole and archimedean rows, endpoint conditions,
and any prime powers omitted from the chosen node list remain separate
ledger entries.  For an exact zeta application, `U` must include every
active prime power, not just the primes used in the exploratory LP.

## 5. An unconditional exact construction with a fixed-power loss

There is a simple benchmark which nulls even all nearby integer-log nodes.
Choose

```text
Y_c=N+1/2.                                           (5.1)
```

For every integer `n!=Y_c` in a fixed multiplicative window,

```text
abs(log(n/Y_c))>=c/Y_c.                              (5.2)
```

Let `psi in C_c^infinity((-1/2,1/2))` be `L^2`-normalized with
`integral psi !=0`, and set

```text
q_Y(x)=a^(-1/2)*psi(x/a),       a<c/(2Y_c).          (5.3)
```

Its autocorrelation is supported in `[-a,a]`, so (5.2) makes every active
integer, hence every prime power, an exact cross zero.  On the other hand,
scaling gives

```text
integral R_(q_Y)(u)*exp(alpha*u)du
 =a*[c_psi+O_psi(alpha*a)]
 asymp 1/Y.                                          (5.4)
```

Here `c_psi=abs(integral psi)^2>0`.

After the phase flip (4.4), the selected carrier is therefore

```text
-Theta(Y^(-1))*exp(alpha*D)                          (5.5)
```

relative to the fixed-width carrier normalization.  Its natural spectral
scale is `a^(-1) asymp Y`; when `Y=T^d` with `d<2/3` this lies comfortably
inside the available `T` scale, and smoothness makes leakage beyond `T`
superpolynomially small.  Thus the elementary construction pays no type
overflow, but it does pay a full fixed power in carrier.

There is likewise no bare type obstruction to finite positive-definite
interpolation.  The product

```text
Phi(u)=product_j cos^2(pi*u/(2*u_j))                 (5.6)
```

is positive definite and vanishes at every `u_j`.  Its representing
measure has support radius at most

```text
B=pi*sum_j 1/abs(u_j)=O(Y*log Y)                     (5.7)
```

for the half-integer centering (5.1), using comparison with the harmonic
sum over all nearby integers.  Hence `B<T` throughout the strict
`d<2/3` regime.  But (5.6) generally has low noncentral atoms and an
exponentially small obvious central atom.  It proves type feasibility, not
subpower carrier retention, and cannot be substituted into (3.5) without
checking the spectral gap.

## 6. What the numerical LP says

For the reported experiment, the constraints were imposed at

```text
u_p=log(p/(Y+1/2)),       p in [Y/e,eY],              (6.1)
```

with noncentral frequencies in `[Y,Y^(3/2)]`.  The scale comparison is

```text
Y       M       w_0       1/log Y   sqrt(log Y/Y)   w_0*sqrt(M)
30      17      .202       .294          .337            .833
100     47      .163       .217          .215           1.117
300    112      .121       .175          .138           1.281
1000   323      .0738      .145          .0831          1.326.   (6.2)
```

For comparison, `w_0*log Y` has values `.687,.751,.690,.510`.  Four points
do not discriminate reliably between these slowly varying normalizations.
They are compatible with the square-root heuristic

```text
w_0 approximately c/sqrt(M)
    approximately c*sqrt(log Y/Y),                  (6.3)
```

but do not establish it or exclude `c/log Y`.  This is evidence, not an
asymptotic theorem.  The finite frequency mesh, solver residual, and the
omitted higher prime powers must
also be retained in any numerical claim.

The square-root behavior is the generic convex-hull expectation for a
polynomial-sized collection of high-frequency phase vectors in dimension
`M`.  Turning that expectation into an upper bound for the actual curve
`xi -> v(xi)` is precisely an actual-prime exponential-sum/discrepancy
theorem.  The current KMT input gives only (2.8), while abstract
time-bandwidth geometry does not give a universal square-root upper bound.

## 7. Exact frontier

The route can now be stated without a hidden analytic gap:

```text
prove -Y^(-o(1))*1 belongs to
      conv{(cos(xi*u_j))_j:Y<=xi<=T},
including every active prime power;                  (7.1)

then Theorem 3.1 produces a compact lobe q;
then (4.4)--(4.6) give exact cross-prime nulling and a
negative carrier of size Y^(-o(1))*exp(alpha*D).      (7.2)
```

What has been falsified is the claim that the four LP values already show
`1/log Y` retention.  What has **not** been falsified is the existence of a
different positive quadrature with subpower central mass.  At present:

```text
compact-factor transfer:                    PROVED;
exact fixed-power Y^(-1) construction:       PROVED;
subcritical modulation/type availability:    PROVED;
KMT logarithmic upper on w_0:                 PROVED;
actual-prime w_0>=Y^(-o(1)):                  OPEN;
actual-prime w_0<<sqrt(log Y/Y):              OPEN;
finite LP evidence:                           SQUARE-ROOT, NOT SUBPOWER. (7.3)
```

So this mechanism is a genuine live arithmetic lead, but it has not yet
produced a uniform zero-free strip.
