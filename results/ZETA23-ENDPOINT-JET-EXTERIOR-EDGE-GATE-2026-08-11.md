# Endpoint jets and exterior powers at the Zeta23 spectral edge

Status: exact paper-level lemmas and a revised gate, 2026-08-11.  The
endpoint-jet construction below is a genuine improvement of the sharp-window
carrier: qualitative interpolation and a small remote tail can coexist.  No
prime-side lower-edge estimate is proved, so this note does not prove a
zero-free strip.

Later carrier-rate correction: the fixed-parameter qualitative interpolation
statements below remain valid.  Quantitatively, a distinguished collar pair
can be jet-suppressed at the endpoint-tail scale, while a configuration
compatible with all current zero-count and density inputs, using a core
`k=7` pair sublattice, has
`K<=X^(6*alpha/7+o(1))/L`.  See
[`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md)
and
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md).
Compatibility of that artificial configuration with the separately
evaluated trace, Frobenius, and pair-correlation data is not claimed.

## 1. Verdict

The principal audited conclusions are as follows.

1. Inside the sharp Gabor span one may impose many endpoint-jet conditions.
   The resulting Fourier transforms still have a Cauchy--Vandermonde
   interpolation theorem, while their remote-zero leakage is exponentially
   small in the number of imposed jets.  Thus the earlier sharp
   interpolation/smooth-tail dichotomy is not absolute.  Collision merging
   also gives a fixed-parameter signed carrier edge, but not an effective
   asymptotic rate.
2. A full-lattice off-line pair at depth `alpha` has explicitly computable
   eigenvalues.  For fixed multiplicity, in the isolated-zero normalization
   its negative eigenvalue has magnitude comparable with
   `exp(alpha*L)/L` for the fixed-width taper.
3. Even with this amplified edge, the exact first two Zeta23 moments and a
   long initial segment of the exterior-power signs admit one hyperbolic
   pair.  At the strict additive edge the first exterior coefficient whose
   **sign** is forced to be informative can have degree as large as

   ```text
   T^(1-alpha) * (log T)^2.
   ```

The endpoint construction does not supply an effective asymptotic signed-
carrier margin.  Ordinary Cauchy--Vandermonde singular values retain
arbitrarily small cluster factors, although collision merging gives a
strictly positive but ineffective fixed-parameter negative edge.  The Zeta23
counting input supplies no rate for that edge.  At the same time, the exact
prime matrix has no proved lower edge at the resulting carrier scale.
Its individual complex exponential prime constituents have a phase-twisted
full-rank Toeplitz representation.  For the sharp window their exact sum has
a different, common Loewner displacement of rank at most two, and the same
rank bound survives endpoint-jet compression.  This is displacement rank,
not matrix rank: arbitrary diagonal/confluent data remain, and no sign or
lower edge follows.  The exterior coefficients still contain prime products
up to their full degree.

The revised route is therefore conditional but sharper:

```text
endpoint jets       give full spark and an exponentially small tail;
effective carrier   still needs a quantitative grouped/collision bound;
prime lower edge    must be o(the actual carrier margin), and is still an
                    arithmetically distinct but scale-coupled missing input.
```

## 2. Endpoint-jet sharp span

Let

```text
h       = 2*pi/L,
tau_k   = tau_0+k*h,                 0 <= k < d,
phi     = 1_[-L/2,L/2],
f_c(t)  = phi(t) sum_k c_k exp(-i*tau_k*t),
F_c(z)  = integral f_c(t) exp(i*z*t) dt.
```

Choose a real center `tau_c` and put `omega_k=tau_k-tau_c`.  For an integer
`0<=m<d`, define the endpoint-jet subspace

```text
V_m = {c : sum_k (-1)^k c_k omega_k^j = 0,
             0 <= j < m}.                              (2.1)
```

The centered and uncentered moment conditions are equivalent by the binomial
theorem.

For the explicit-formula application take `m>=3`.  Then every zero-extended
`f_c` in this subspace is at least `C^2`, although the individual sharp basis
vectors are not.

### Theorem 2.1 (simultaneous sharp interpolation and high-order leakage)

The following statements hold.

**(a) Dimension and endpoint jets.**  The conditions in (2.1) are independent,
so

```text
dim V_m = d-m.                                         (2.2)
```

For `c in V_m`, the trigonometric polynomial

```text
p_c(t)=sum_k c_k exp(-i*omega_k*t)
```

and its first `m-1` derivatives vanish at both endpoints `+-L/2`.

**(b) Cauchy--Vandermonde form.**  Put

```text
Q(z)=product_(0<=k<d) (z-tau_k).
```

There is a polynomial `P_c`, depending linearly on `c`, such that

```text
F_c(z)
 = 2 sin(L*(z-tau_0)/2) sum_k (-1)^k c_k/(z-tau_k)
 = 2 sin(L*(z-tau_0)/2) P_c(z)/Q(z),                  (2.3)

deg P_c <= d-m-1.                                     (2.4)
```

Moreover, `c -> P_c` maps `V_m` bijectively onto the polynomials of degree at
most `d-m-1`.

Consequently, if `z_1,...,z_q` are distinct nodes, `q<=d-m`, and no node is
an unused zero of the sine factor, then

```text
c in V_m |-> (F_c(z_1),...,F_c(z_q))                  (2.5)
```

is surjective.  A node equal to one of the used grid points `tau_k` is
handled by the removable limit in (2.3).  Unused grid degeneracies can be
removed by a generic grid offset.  Any alternative enlargement of the
coordinate grid has to be included explicitly in the dimension and collar
budget.

For a conjugation-invariant node set, conjugation-compatible target values
can be interpolated by real coefficients.  Hence, when all local distinct
zero locations fit in `d-m` coordinates, the local zero form retains one
negative direction per off-line pair as a qualitative inertia statement.
Its Rayleigh margin can be arbitrarily small and is not controlled here.

**(c) Uniform exterior leakage.**  Assume `m>=3` and let

```text
W=max_k |omega_k|.
```

For `|Im z|<1/2` and `z!=tau_c`,

```text
|F_c(z)|
 <= L * exp(L/4) * (W/|z-tau_c|)^m * ||c||_2.         (2.6)
```

For the Zeta23 placement of the modulation interval in `[T,2T]`, suppose
`1<=D<=T` and the carrier contains every zero ordinate within distance `D` of
that interval.  Use the classical unit-window bound

```text
N(t+1)-N(t) <= A_0 log(t+3).
```

Then the remote-zero form restricted to `V_m` obeys, up to an absolute
constant and harmless endpoint adjustments,

```text
||E_remote|V_m||
 <= A_0 * L^2 * X^(1/2) * log(4T)
      * (1+(W+D)/m) * (W/(W+D))^(2m),                 (2.7)
```

where `X=exp(L)`.  For the sharp window `a=1`; in the general isolated-zero
normalization `G/(aL^2)`, division cancels the factor `L^2` and leaves the
corresponding factor `1/a`.  This is a coefficient-norm operator bound.
Interpolating prescribed local values can multiply it by the norm of an
interpolation right inverse, so (2.7) alone is not a carrier margin.

#### Proof

At `t=+L/2`, every exponential in `p_c^(j)` has the common factor
`exp(-i*(tau_0-tau_c)*L/2)` times `(-1)^k`; at `t=-L/2` the analogous common
factor is its inverse.  Thus (2.1) is exactly the simultaneous vanishing of
the first `m` endpoint jets.  The moment matrix is a signed Vandermonde matrix
in the distinct numbers `omega_k`, which proves (2.2).

For the sharp window,

```text
2 sin(L*(z-tau_k)/2)/(z-tau_k)
 = 2 (-1)^k sin(L*(z-tau_0)/2)/(z-tau_k).
```

Putting the partial fractions over `Q` proves (2.3).  Expansion at infinity
gives

```text
sum_k (-1)^k c_k/(z-tau_k)
 = sum_(j>=0) z^(-j-1) sum_k (-1)^k c_k tau_k^j.
```

The first `m` coefficients vanish exactly when the numerator degree drops
from at most `d-1` to at most `d-m-1`.  Since ordinary partial fractions give
a bijection before imposing the conditions, they give the asserted
bijection afterwards.  Polynomial interpolation now proves (2.5).  For
conjugation-compatible data on `q` conjugation-invariant nodes, take the
unique interpolant of degree strictly less than `q` (viewed inside the
degree-`d-m-1` space); uniqueness and conjugation show that it has real
coefficients.

For (2.6), modulate by `tau_c` and integrate by parts `m` times.  All boundary
terms vanish by part (a).  Exact orthogonality at spacing `2*pi/L` gives

```text
||p_c^(m)||_2^2
 = L sum_k |c_k|^2 |omega_k|^(2m)
 <= L W^(2m) ||c||_2^2.
```

Therefore `||p_c^(m)||_1<=L W^m||c||_2`; the factor `exp(L/4)` accounts for
`|Im z|<1/2`.  This proves (2.6).  For the shell estimate, first take
`tau_c` to be the midpoint of the grid and write
`W_0=max_k|tau_k-tau_c|`.  This loses no freedom: changing `tau_c` performs a
triangular change of the moment conditions, so the subspace `V_m` is
center-independent.  Squaring the bound, grouping remote zeros in unit
ordinate shells, and using

```text
sum_(j>=0) (W_0/(W_0+D+j))^(2m)
 <= (1+(W_0+D)/(2m-1)) (W_0/(W_0+D))^(2m)
```

proves (2.7) with `W_0`.  The zero-count factor is not literally constant in
the far shells; with `D<=T`, its growth is absorbed by the same right side
using `log(4T+j)<=log(4T)+j/T` and `m>=3`.  For any other displayed center,
`W_0<=W`, and the right side is monotone in `W`, which gives the stated form.
This argument keeps every remote zero; there is no sharp-tail deletion or
cancellation assumption.  QED

### 2.2 Available jet budget

Write more generally

```text
L=ell_1+eta(T).
```

The raw Zeta23 prime estimates remain asymptotic in the mesoscopic range

```text
eta*T >> sqrt(T)*l,
eta=o(l),
exp(eta)*log(l)/l -> 0,                                (2.8)
```

because their decisive off-diagonal ratio is `X/(T*L)` (with the displayed
proof's extra `log l`), not the fixed-parameter shorthand
`T^(lambda-1) log l`.  Thus `eta=theta log l`, fixed `theta<1`, is admissible
at paper level.  The dimension surplus is of order `eta*T`.

Remark 7.1(iii) of the Zeta23 paper explicitly states that the sharp-cutoff
matrix still has the Section 5 prime estimates (`g(y)=(L-|y|)_+`); what fails
there is the original remote-tail proposition.  Condition (2.8) is the raw
varying-parameter extension of that same estimate.  It validates the support
length, cutoff, dimension, and error regime, but it does **not** transfer a
lower-edge estimate to the new compression: restricting to `V_m` changes the
matrix observables.  A formal port would also need a varying-parameter
wrapper.

If the endpoint conditions and a collar of width `D` are both paid from this
surplus, the budget has the schematic form

```text
m + O(D*l) <= c*eta*T.                                 (2.9)
```

Balancing the two terms makes the exponential in (2.7) of size

```text
m*D/T  asymp  eta^2*T/l.                              (2.10)
```

For `eta=theta log l`, this is `T*(log l)^2/l`.  Hence the endpoint-jet tail
can be far smaller than the polynomial smooth-taper tail.

This does not by itself yield an effective carrier margin.  In polynomial
coordinates an ordinary, ungrouped interpolation minor contains

```text
product_(i<j) (z_j-z_i),                               (2.11)
```

times nonzero row and basis factors.  As two allowed distinct nodes coalesce,
the least row singular value tends to zero.  Equivalently, the two-row
variational estimate is

```text
sigma_min(E_m)
 <= ||R_m(z+epsilon)-R_m(z)||_2/sqrt(2)
 = O_(T,L,m,z)(|epsilon|).                             (2.12)
```

This least-singular-value collapse is **not** an exact obstruction to the
signed carrier: when same-orientation atoms coalesce, their multiplicities
add.  Compactifying all collision strata and using Cauchy--Vandermonde
surjectivity gives, at every fixed `T,L,m` and fixed depth `delta>0`, a
strictly positive separation-free lower bound for the magnitude of *some*
negative eigenvalue whenever the total local point count is at most
`dim V_m`; see
[`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md).
The compactness bound is ineffective as the parameters vary.  No grouped
Paley--Wiener/divided-difference estimate in the audited inputs proves

```text
log(1/kappa_comp)=o(eta^2*T/log T),                   (2.13)
```

which is what would compare it with (2.7).  High-order jets therefore repair
the tail/full-spark conflict and clustering is not a qualitative no-go, but
the effective signed-carrier gate remains open.

## 3. Exact size of one full-lattice hyperbolic block

Let `phi` now be any nonzero real even `L2` function supported in
`[-L/2,L/2]`, put

```text
a=(1/L) integral phi(t)^2 dt,
K_alpha(r)=integral phi(t) exp(alpha*t) exp(i*r*t) dt,
v_k=K_alpha(gamma-T-k*h),              k in Z,
h=2*pi/L.
```

Write `v=x+i*y` with real `x,y`.

### Theorem 3.1 (exact pair eigenvalues)

For `alpha>0`,

```text
A_alpha := ||v||_2^2
         = L integral phi(t)^2 exp(2*alpha*t) dt,

v^T v   = a*L^2.                                      (3.1)
```

Consequently `x` and `y` are orthogonal and

```text
||x||^2=(A_alpha+aL^2)/2,
||y||^2=(A_alpha-aL^2)/2.                             (3.2)
```

A reflected pair of multiplicity `M` contributes, in the isolated-zero
normalization,

```text
B_alpha = (2M/(aL^2)) (x*x^T-y*y^T),                 (3.3)
```

whose two nonzero eigenvalues are exactly

```text
lambda_+ = M (A_alpha/(aL^2)+1),
lambda_- = -M (A_alpha/(aL^2)-1).                    (3.4)
```

In particular `lambda_+-|lambda_-|=2M`.  For the fixed-width Zeta23 taper,
fixed `alpha>0`, fixed multiplicity `M`, and large `L`,

```text
kappa_alpha:=|lambda_-| asymp_(alpha,M) exp(alpha*L)/L. (3.5)
```

#### Proof

The values `v_k/L` are the Fourier-series coefficients on an interval of
length `L` of

```text
g(t)=phi(t) exp(alpha*t) exp(i*(gamma-T)*t).
```

Parseval proves the first identity in (3.1).  Its bilinear version gives

```text
sum_k (v_k/L)^2=(1/L) integral g(t)g(-t)dt.
```

Evenness of `phi` cancels the displacement and phase, proving the second
identity.  Equations (3.2)--(3.4) follow immediately.  Strict negativity
holds because the even integral of `exp(2*alpha*t)` is the integral of
`cosh(2*alpha*t)`, strictly larger than its value at `alpha=0`.

For a taper with `0<=phi<=1` equal to one on
`[-L/2+w,L/2-w]`,

```text
(w/L) exp(alpha*L-4*alpha*w)
 <= (integral phi^2 exp(2*alpha*t))/(integral phi^2)
 <= exp(alpha*L)/(2*alpha*(L-2w)).                    (3.6)
```

Taking fixed `w` proves (3.5).  QED

At `L=log(T/(2*pi))+O(log log T)`, (3.5) is

```text
kappa_alpha=T^(alpha+o(1))/log T.                     (3.7)
```

For every fixed `0<alpha<1/2`, since
`N(T,2T) asymp T log T`, one has

```text
kappa_alpha^2=o(N(T,2T)).                             (3.8)
```

Thus even the optimistic unscreened pair edge is below the square-root bulk
scale measured by the second moment.

## 4. A sharp exterior-power obstruction matching the Zeta23 moments

For a Hermitian matrix `H`, write `e_r(H)` for the degree-`r` elementary
symmetric polynomial of its eigenvalues, equivalently
`tr(exteriorPower_r H)`.

### Lemma 4.1 (delay of the first negative exterior coefficient)

Suppose `H` has one eigenvalue `-kappa` and its other `N-1` eigenvalues are at
least `a_0>0`.  Then

```text
e_r(H)>=0 whenever r <= a_0*N/(a_0+kappa).            (4.1)
```

The bound is sharp when all positive eigenvalues equal `a_0`.

#### Proof

Let `E_r` be the elementary symmetric polynomial of the positive
eigenvalues.  Then

```text
e_r(H)=E_r-kappa*E_(r-1).                             (4.2)
```

Double-counting extensions of `(r-1)`-subsets gives

```text
r*E_r
 = sum_(|S|=r-1) product_(i in S)lambda_i
       sum_(j notin S)lambda_j
 >= a_0*(N-r)*E_(r-1).                               (4.3)
```

Equations (4.2)--(4.3) prove (4.1).  Equality holds throughout for a constant
positive spectrum.  QED

The next theorem strengthens the two-moment countermodel by retaining the
positive mate required by an actual simple hyperbolic block.

### Theorem 4.2 (exact Zeta23 moments, one amplified pair, long positive exterior prefix)

Let

```text
K_N -> 4/3,
kappa_N>0,
kappa_N^2/N -> 0.
```

For every sufficiently large `N` there is an `N` by `N` Hermitian matrix
`H_N` with

```text
tr H_N       = N,
tr(H_N^2)    = K_N*N,                                 (4.4)

spec(H_N) contains -kappa_N and kappa_N+2,
all remaining eigenvalues are positive,
min(spec(H_N)\{-kappa_N}) >= 1/3.                    (4.5)
```

It has exactly one negative eigenvalue, yet

```text
e_r(H_N)>=0 for every r <= N/(1+3*kappa_N).           (4.6)
```

Extra zero eigenvalues may be appended without changing (4.4) or any
`e_r` through the active rank.

#### Proof

Put `n=N-2`, `p=floor(n/2)`, `q=n-p`, and

```text
v_N=(K_N*N-kappa_N^2-(kappa_N+2)^2)/n-1,
A_N=1+sqrt(v_N*q/p),
B_N=1-sqrt(v_N*p/q).                                  (4.7)
```

Take the spectrum

```text
-kappa_N, kappa_N+2,
p copies of A_N, q copies of B_N.                     (4.8)
```

The two deviations from one have weighted sum zero and weighted square sum
`n*v_N`; direct summation proves (4.4).  The hypotheses imply

```text
v_N -> 1/3,
B_N -> 1-1/sqrt(3)>1/3,
```

so (4.5) holds eventually.  Lemma 4.1 with `a_0=1/3` proves (4.6).  QED

For the actual ideal Zeta23 normalization at the additive edge,

```text
K_N = 1/u+u/3+o(1),       u=L/ell_1 -> 1,             (4.9)
```

so Theorem 4.2 applies.  Combining (3.7) and (4.6), the first exterior degree
which a coefficient-sign argument can force to be informative for a simple
full-lattice pair (`M=1`, `kappa_N=kappa_alpha`) is only after

```text
N/(1+3*kappa_alpha)
 = T^(1-alpha+o(1))*(log T)^2.                        (4.10)
```

For the strict padding `L=ell_1+c/l`, this is
`asymp_alpha T^(1-alpha)*(log T)^2`.  For mesoscopic `eta`, it acquires the
explicit additional factor `exp(-alpha*eta)`.

The full determinant detects an odd negative index, but it has degree of
order `N`; if the padded local matrix has null directions, its determinant is
zero and the relevant object is a high pseudo-determinant coefficient.

## 5. Exact prime-side exterior formula

The exterior hierarchy does have an exact prime-side representation, but the
matrix must be matched to an admissible test space.  In particular, for the
sharp window the individual coordinate functions are not `C_c^2`; only their
endpoint-jet combinations are admissible in the explicit formula.

Let `U` be a real `d` by `n` matrix with orthonormal columns `u_a`, and put

```text
f_a(x)=phi(x) sum_(0<=k<d) U_(k,a) exp(-i*tau_k*x),
g_a(t)=f_a_hat(t),
K_U(t,s)=sum_(0<=a<n) g_a(t)g_a(s),

H_U(a,b)=integral_R g_a(t)g_b(t) nu_X(t)dt,
nu_X=mu+Pi_X+P_X.
```

Assume that every `f_a` is in `C_c^2`.  This includes the original smooth
Zeta23 taper with `U=I_d`, and it includes the sharp endpoint construction
when `m>=3`, `n=d-m`, and the columns of `U` are an orthonormal real basis of
`V_m`.  In the latter case `H_U` is the relevant compressed matrix; the full
sharp coordinate matrix is not being inserted into the zero-side explicit
formula.

### Theorem 5.1 (continuous Cauchy--Binet formula)

For `0<=r<=n`,

```text
e_r(H_U/(aL^2))
 = 1/(r!*(aL^2)^r)
   integral_(R^r) det[K_U(t_i,t_j)]_(i,j<=r)
                  product_(i=1)^r nu_X(t_i) dt_i.     (5.1)
```

All integrals are absolutely convergent in both cases just listed.

#### Proof

The explicit formula applied to the admissible functions `f_a` gives the
displayed entries of `H_U`.  Expand `e_r` as the sum of the `r` by `r`
principal minors.  Andreief's identity for the signed density `nu_X` writes
each minor as the integral of the square of its real evaluation determinant
divided by `r!`.  Summing those squares and applying finite Cauchy--Binet
gives `det[K_U(t_i,t_j)]`.  The transforms have at least quadratic decay,
while `nu_X(t)=O_X(log(2+|t|))`, which justifies the signed Andreief identity,
all finite expansions, and the Fubini interchanges.  QED

The kernel determinant in (5.1) is nonnegative, but `nu_X` is signed.
Expanding

```text
P_X(t)=-(1/pi) sum_(n<=X) Lambda(n)/sqrt(n) cos(t log n)               (5.2)
```

shows that the degree-`r` coefficient contains exact `q`-fold prime-power
sums for every `0<=q<=r`.  Thus (5.1) retains the pole, gamma, every exact
prime term, and through the explicit formula every remote zero; it supplies
no unconditional sign by itself and makes no smooth/sharp matrix
identification.

## 6. Toeplitz constituents and the sharp Loewner structure

One prime frequency has a useful time-domain Toeplitz factorization.  For
`0<y<L`, set

```text
q_y(u)=phi(u)phi(u+y),
c_j(y)=2*pi integral q_y(u) exp(-i*j*h*u)du,
C_y(k,l)=c_(k-l)(y),
D_y(l,l)=exp(i*tau_l*y).
```

### Lemma 6.1 (phase-twisted full-rank complex constituent)

The complex exponential constituent is

```text
B_y(k,l)
 := integral phiHat(t-tau_k)phiHat(t-tau_l)exp(i*t*y)dt
  = (C_y D_y)(k,l).                                   (6.1)
```

If `q_y` is positive on a set of positive measure, then `C_y` is positive
definite and `B_y` has full rank `d`.  Its cosine part is

```text
A_y=Re B_y,                                           (6.2)
```

and, away from the finite-section boundary,

```text
A_y(k+2,l+2)-2*cos(h*y)A_y(k+1,l+1)+A_y(k,l)=0.       (6.3)
```

#### Proof

Fourier inversion with the constraint `s=-y-u` gives (6.1).  For every
vector `z`,

```text
z^* C_y z
 =2*pi integral q_y(u)|sum_k z_k exp(-i*k*h*u)|^2 du.
```

This is strictly positive for nonzero `z`, because a nonzero trigonometric
polynomial cannot vanish on a set of positive measure.  The diagonal `D_y`
is invertible.  Finally

```text
B_y(k+1,l+1)=exp(i*h*y)B_y(k,l),
```

and taking real parts proves (6.3).  QED

Although `A_y` can be singular at exceptional phases, it is generically full
rank: `det Re(exp(i*theta)B_y)` is a nonzero Laurent polynomial in
`exp(i*theta)`, whose highest Laurent coefficient is a nonzero multiple of
`det B_y`.  This full matrix rank is compatible with low *displacement* rank;
the two notions must not be conflated.

For the prime sum,

```text
G_prime=-(1/pi)sum_(n<=X) Lambda(n)/sqrt(n) A_(log n).                (6.4)
```

The prime-dependent twists in Lemma 6.1 do **not** imply that the sum lacks a
common low-displacement structure.  For the sharp window, the common sine
factor gives exactly such a structure.

### Theorem 6.2 (sharp Loewner identity and its jet compression)

Take `phi=1_[-L/2,L/2]` and put

```text
S(t)=sin(L*(t-tau_0)/2),
epsilon=diag((-1)^k),
Delta=diag(tau_0,...,tau_(d-1)),

Gsharp_(k,l)=integral phiHat(t-tau_k)phiHat(t-tau_l)nu_X(t)dt,
H=epsilon*Gsharp*epsilon.
```

Then

```text
H_(k,l)=4 integral S(t)^2 nu_X(t)
                    /((t-tau_k)*(t-tau_l)) dt.         (6.5)
```

Fixing `tau_0` as a subtraction point, define the absolutely convergent
quantities

```text
j_k=4 integral S(t)^2 nu_X(t)
       *(1/(t-tau_k)-1/(t-tau_0)) dt.                 (6.6)
```

With `1` denoting the all-ones vector,

```text
[Delta,H]=j*1^T-1*j^T,       rank([Delta,H])<=2.       (6.7)
```

For the endpoint-jet compression with `m>=1`, let `U` be the orthonormal real
basis of `V_m` used in Section 5, put `Utilde=epsilon*U`,
`P=Utilde*Utilde^T`, and set

```text
A_m=Utilde^T*Delta*Utilde,
H_m=Utilde^T*H*Utilde=U^T*Gsharp*U.
```

Then

```text
rank([A_m,H_m])<=2.                                   (6.8)
```

#### Proof

The sharp transform is

```text
phiHat(t-tau_k)=2*(-1)^k*S(t)/(t-tau_k),
```

which proves (6.5).  Its integrals are absolutely convergent.  The subtraction
in (6.6) makes the integrand `O_X(log(2+|t|)/t^2)` at infinity, while the
zeros of `S` remove the apparent grid-point singularities.  For `k!=l`,

```text
(tau_k-tau_l)*H_(k,l)=j_k-j_l;
```

the diagonal of the commutator is zero, proving (6.7).

After the sign conjugation,

```text
epsilon*V_m
 ={b: sum_k b_k*omega_k^r=0, 0<=r<m}=:W_m.
```

Thus `P*1=0`.  Multiplication by `Delta` raises the moment degree by one, so
`Delta*W_m` is contained in `W_(m-1)`.  Since `W_m` has codimension one in
`W_(m-1)`, the matrix

```text
R=(I-P)*Delta*Utilde
```

has rank at most one.  Compressing the commutator (6.7), whose two generators
are killed by `P*1=0`, gives

```text
[A_m,H_m]=-R^T*H*Utilde+Utilde^T*H*R.
```

This is a sum of two rank-one matrices and proves (6.8).  QED

The identity applies separately to the prime, archimedean, and pole weights,
and to their exact sum.  It corrects the tempting but false inference from
the varying twists in (6.1) that no common bounded displacement exists.
However, rank-two displacement is not rank two of the matrix.  The diagonal
(equivalently, confluent Loewner) data remain unrestricted by (6.7), the
weight `nu_X` is signed, and neither (6.7) nor (6.8) gives a determinant sign
or a lower spectral edge.  They expose a genuine structured route that still
requires new arithmetic input.

For the prime density this structure has the exact scalar form

```text
H_P=-2*diag(D_X)+(2/h)*(diag(A_X)*K_d-K_d*diag(A_X)),
||K_d||_op<=pi,
```

where `A_X,D_X` are the two transition-length Dirichlet polynomials in
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
The resulting scalar norm estimate is a sufficient lower-edge reduction,
not a structural sign theorem: the arbitrary confluent diagonal remains.

## 7. Higher moments and the support-depth barrier

The exact pair size also quantifies the least new arithmetic that could
detect a fixed depth by a Schatten moment.  With

```text
L=lambda*log T+o(log T),
kappa_alpha=T^(alpha*lambda+o(1)),
N(T,2T)=T^(1+o(1)),
```

an even moment ceiling

```text
tr(Ghat^p) <<_p N(T,2T)*T^o(1)                       (7.1)
```

can contradict a surviving pair edge only when

```text
alpha*lambda*p>1.                                    (7.2)
```

The unconditional diagonal/Rudnick--Sarnak range quoted in the Zeta23 paper
is

```text
lambda*p<2.                                          (7.3)
```

The paper separately evaluates the boundary case `p=2, lambda=1` (and the
raw additive-edge variant above); for fixed `alpha<1/2` it still fails
(7.2).

Since every off-line depth satisfies `alpha<1/2`, (7.2) and (7.3) never
overlap for this single support-`L` compression.  A union of several shorter
modulation grids would require a separate analysis of the mixed moments,
normalization, and retained pair edge; (7.2)--(7.3) alone do not prove the
same barrier for that construction.  Odd moments are weaker for the actual
full-lattice pair `(-kappa,kappa+2)`, because their leading `kappa^p` terms
cancel.

Therefore a moment route needs at least one of the following genuinely new
inputs:

1. an even prime-side moment beyond `lambda*p=2`, with
   `lambda*p>1/alpha`;
2. a sub-leading asymptotic whose error is `o(kappa_alpha^p)`, rather than a
   bulk `o(N)` evaluation; or
3. a direct negative-part or lower-edge estimate not mediated by finitely
   many bulk moments.

At the additive edge `lambda=1+o(1)`, the first option means an even order
`p>1/alpha`, and its prime expansion lies outside the currently proved
Montgomery--Vaughan package.

## 8. Almost-all-height loophole

A zero of ordinate `gamma` belongs to `[T,2T]` for every
`T in [gamma/2,gamma]`.  Thus a genuine lower-edge theorem outside an
`o(T)` exceptional set would logically suffice.  Present mean estimates do
not give such a theorem: the bad eigenvector is adaptive in `T`, and first
two trace moments permit one negative edge for every `T` by Theorem 4.2.

Varying `T` also does not automatically provide the missing *effective*
carrier rate.  For a fixed local zero cluster, the ordinary ungrouped
Vandermonde factor (2.11) is independent of `T` and can remain tiny throughout
the whole membership interval.  Collision compactification still gives a
strict signed edge at each fixed parameter set, but no audited input controls
that compactness constant on average in `T`.  An almost-all argument is
therefore a valid conditional formulation, not a consequence of the existing
mean-value estimates.

## 9. Revised go/no-go card

The endpoint-jet branch should remain open only in the following precise
form.

```text
PROVED HERE:
  sharp Cauchy--Vandermonde interpolation after m endpoint jets;
  a separation-free fixed-parameter carrier margin after collision merging
    (qualitative/compactness, with no asymptotic rate);
  exponentially small remote tail on that constrained subspace;
  exact full-lattice isolated-pair edge size;
  exact exterior-coefficient prime integral;
  long exterior-sign countermodel matching the two Zeta23 moments;
  exact Loewner displacement identity of rank at most two before and after
    jet compression;
  no sign or lower edge from displacement rank alone.

STILL REQUIRED:
  an effective grouped-interpolation/carrier bound satisfying
    log(1/kappa)=o(eta^2*T/log T), or an argument avoiding such a bound;
  an unconditional prime-side lower edge on the same constrained space whose
    normalized negative error is o(kappa).

SUFFICIENT NEW ARITHMETIC OPTIONS:
  a direct shifted-determinant/negative-part inequality;
  or an even moment beyond lambda*p=2 with lambda*p>1/alpha;
  or high exterior-coefficient control beginning near N/kappa_alpha.
```

The first missing line is not presently implied by zero counting, and the
second is not implied by Toeplitz Gram structure, trace, Frobenius norm, or
the endpoint conditions.  The tail-rate condition on `kappa` need not retain
a fixed or power-scale fraction of the full-pair edge, so it does not
automatically combine with a scalar prime estimate stated only as
`o(X^alpha)`.  The two matched gates are reduced more sharply in
[`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
and
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
No claim of a zero-free strip or of publication-level novelty is made.

Primary sources used: the Zeta23 paper, especially Sections 2, 4, 5, and
7.5; its exact explicit-formula matrix and raw Montgomery--Vaughan estimates;
and the additive-edge and single-block gate reports in this repository.
