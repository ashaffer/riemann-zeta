# Quantitative Nyman--Beurling collar-rate and principal-mode gate

Status: focused fixed-strip attack, 2026-08-12.

Binary verdict: **no unconditional fixed strip is proved**.  The attack does,
however, give an exact power threshold for the natural Baez--Duarte collar and
a sharper localization of the missing estimate.

```text
target half-plane                         Re(s) >= 1-delta
exact L1 collar-rate sufficient condition ||E_n||_1=o(n^(-delta/(1-delta)))
delta=0.01 threshold                      n^(-1/99)
unconditional result for this collar      ||E_n||_1=o(1)
generic weight suppression                no free gain in the dual bound
critical coefficient window               n <= m <= n^(1/(1-delta))
delta=0.01 window                          n <= m <= n^(100/99)
missing gain in natural weighted norm      n^delta down to n^o(1)
uniform zero-free strip                    NOT PROVED
```

The new exact statement is this.  If a zero
`rho_0=beta+i gamma` exists, the natural compact collar cannot have `L1` mass
smaller than a fixed multiple of

```text
n^(-(1-beta)/beta).                                           (0.1)
```

In the proof direction, an upper bound `o(n^-a)` for the same mass excludes every zero
with real part at least `1/(1+a)`.  Thus the zero-conditioned lower exponent
and this particular strip-producing upper exponent meet with no loss.  This is
not an equivalence between a zero-free region and that quantitative rate.

## 1. Exact normalization

Write

```text
{u}=u-floor(u),                 chi=1_(0,1],
g(n)=sum_(k<=n) mu(k)/k,

B_n(x)=sum_(k<=n) mu(k){1/(kx)}-n g(n){1/(nx)},
E_n(x)=chi(x)+B_n(x).                                      (1.1)
```

The coefficient constraint is exact:

```text
sum_(k<=n) mu(k)/k - n g(n)/n = 0,                         (1.2)
```

so `B_n` belongs to the constrained Nyman space.  Mobius inversion gives

```text
B_n=-1 on (1/n,1],
B_n=0 on (1,infinity),
E_n=0 on (1/n,infinity).                                  (1.3)
```

At the single endpoint `x=1/n`, one instead has
`B_n(1/n)=n g(n)-1` and `E_n(1/n)=n g(n)`.  Thus the essential
support of `E_n` is contained in `(0,1/n)` (and its ordinary support is
contained in `(0,1/n]`).  All norm and Mellin identities below are
Lebesgue-integral statements, so this endpoint correction has no effect on
them.

The prime number theorem gives `g(n)->0`.  Consequently, for all sufficiently
large `n`,

```text
||E_n||_infinity
 <=1+sum_(k<=n)|mu(k)|+n|g(n)| <= 3n.                      (1.4)
```

Put

```text
A_n(s)=sum_(k<=n)mu(k)k^(-s)-n^(1-s)g(n).                  (1.5)
```

The standard constrained Mellin identity, valid for `Re(s)>0` (with the
value at `s=1` understood by removable continuation), is

```text
integral_0^1 E_n(x)x^(s-1) dx
       =[1-zeta(s)A_n(s)]/s.                               (1.6)
```

In particular, at every nontrivial zero `rho_0=beta+i gamma`,

```text
integral_0^1 E_n(x)x^(rho_0-1) dx = 1/rho_0.               (1.7)
```

This fixed scalar is the principal mode.  It is independent of `n` and of how
well the collar approximates zero pointwise.

## 2. The exact collar-rate theorem

### Theorem 2.1 (a zero forces a sharp L1 floor)

Let `rho_0=beta+i gamma` be a zero of `zeta`, with `0<beta<1`, and set
`epsilon_n=||E_n||_1`.  Then, for all sufficiently large `n`,

```text
epsilon_n >= (beta/|rho_0|)^(1/beta)
             (3n)^(-(1-beta)/beta).                        (2.1)
```

#### Proof

The decreasing-weight bathtub inequality says that if `0<=h<=H`,
`supp(h) subset (0,L)`, and `integral h=m`, then, whenever `m/H<=L`,

```text
integral_0^L h(x)x^(beta-1) dx
 <= H integral_0^(m/H) x^(beta-1) dx
 = H^(1-beta)m^beta/beta.                                  (2.2)
```

Indeed, among all densities of height at most `H` and mass `m`, the decreasing
weight is maximized by placing height `H` on the initial interval `(0,m/H)`.

Apply this with `h=|E_n|`, `H=3n`, `L=1/n`, and `m=epsilon_n`; support is
understood essentially.  The capacity
condition follows from (1.3)--(1.4).  Equations (1.7) and (2.2) give

```text
1/|rho_0|
 <= integral_0^(1/n)|E_n(x)|x^(beta-1) dx
 <= (3n)^(1-beta)epsilon_n^beta/beta,                       (2.3)
```

which is (2.1).  QED

### Corollary 2.2 (exact fixed-strip rate)

If, for some `a>0`,

```text
||E_n||_1=o(n^-a),                                         (2.4)
```

then `zeta` has no zero in the closed half-plane

```text
Re(s)>=1/(1+a).                                             (2.5)
```

Indeed, a zero with `beta>=1/(1+a)` has
`(1-beta)/beta<=a`, contradicting (2.1).  Equivalently, elementary
interpolation gives

```text
||E_n||_(1+a)^(1+a)
 <=(3n)^a||E_n||_1=o(1),                                   (2.6)
```

and the Nyman--Beurling theorem excludes zeros in the corresponding open
half-plane; (2.1) additionally handles its boundary.

For a desired line `1-delta`, the exact exponent is therefore

```text
a_delta=delta/(1-delta),       p_delta=1+a_delta=1/(1-delta).
                                                                    (2.7)
```

At `delta=0.01`, this is

```text
p_delta=100/99,             a_delta=1/99=0.010101....       (2.8)
```

Thus `||E_n||_1=o(n^(-1/99))` would prove the requested `0.99` strip.
The unconditional theorem `||E_n||_1->0` does not supply any fixed positive
value of `a`.

The interpolation used here is deliberately one-way.  More generally,
`||E_n||_p^p <= (3n)^(p-1)||E_n||_1`, so an `L1` rate
`o(n^(-(p-1)))` is sufficient for `L^p` convergence.  Conversely, shrinking
support gives only

```text
||E_n||_1 <= n^(-(1-1/p))||E_n||_p.                       (2.9)
```

Thus `||E_n||_p=o(1)` implies an `L1` rate with exponent `1-1/p`, not
`p-1`.  No converse equivalence of quantitative rates is claimed; the collar
threshold above is the sharp output of the stated support/height argument.

### Hostile sharpness check

The exponent in (2.1) cannot be improved using only support, height, and mass.
The bathtub extremizer has height `H` on an interval of length

```text
L_asymp H^(-1/beta),
```

so its mass is `H^(-(1-beta)/beta)` while its beta-Mellin moment is constant.
A complex phase `x^(-i gamma)` saturates the triangle step as well.  Real
oscillatory functions such as a suitably phased
`cos(gamma log x)` on the same interval have the same exponent, and reciprocal
step functions approximate them.  Therefore a stronger lower exponent must
use the actual Mobius coefficients, not merely the collar geometry.  This is
not a construction inside the Nyman span and is not claimed to prove optimality
there.

## 3. A candidate zero forces polynomial Lp growth

There is a useful non-endpoint form of the same obstruction.  Let `1<p<infinity`,
`1/p+1/q=1`, and suppose `beta>1/p`.  From (1.3), (1.7), and Holder,

```text
1/|rho_0|
 <=||E_n||_p
   (integral_0^(1/n)x^(q(beta-1))dx)^(1/q)
 =C_(p,beta)||E_n||_p n^(-(beta-1/p)).                     (3.1)
```

Hence

```text
||E_n||_p >= c_(rho_0,p)n^(beta-1/p).                      (3.2)
```

Thus a zero strictly to the right of the detected line does not merely prevent
convergence: it makes this moving-support natural approximation grow by a
fixed power.  Combining (3.2) with (2.6) and letting `p` decrease to `1/beta`
recovers the endpoint exponent (2.1).

## 4. The weighted sequence model is exactly the same collar

Put `t=1/x`.  On every interval `m<t<m+1`, define

```text
F_n(m)=1-sum_(k<=n)mu(k)floor(m/k)
          +n g(n)floor(m/n).                               (4.1)
```

Then

```text
E_n(1/t)=F_n(m),
F_n(m)=0 for m<n,
|F_n(m)|<=3n eventually,                                   (4.2)

||E_n||_p^p=sum_(m>=n)|F_n(m)|^p/[m(m+1)].                 (4.3)
```

Thus the `F_n` used in the modern weighted Dirichlet-space formulation is not
an analogy to the compact Baez--Duarte collar: it is its exact coefficient
sequence.

For completeness, define

```text
a_m(s)=integral_(1/(m+1))^(1/m)x^(s-1)dx
      =[m^(-s)-(m+1)^(-s)]/s.                              (4.4)
```

Equations (1.7) and (4.2) give the exact discrete principal mode

```text
sum_(m>=n)F_n(m)a_m(rho_0)=1/rho_0.                        (4.5)
```

For `1<p<infinity`, let

```text
||F||_(p,alpha)^p=sum_m |F(m)|^p(m+1)^alpha,
b=-(alpha+1)/p.                                            (4.6)
```

Since `|a_m(rho_0)| asymp_(rho_0)m^(-beta-1)`, weighted
Holder applied to (4.5) proves the quantitative dual bound

```text
||F_n||_(p,alpha) >= c_(rho_0,p,alpha)n^(beta-b),
                                  beta>b.                  (4.7)
```

Indeed, the dual tail is

```text
(sum_(m>=n)|a_m(rho_0)|^q(m+1)^(-alpha*q/p))^(1/q)
 asymp n^(-(beta-b)).                                      (4.8)
```

This both recovers and quantifies the boundary
`beta>-(alpha+1)/p` in the weighted approximation theorem.
For `p=1`, the same conclusion follows with the dual sum replaced by the
corresponding supremum; equations (4.7)--(4.8) should then be read in that
endpoint sense.

For the target `b=1-delta`, every choice on the line

```text
alpha=-1-p(1-delta)                                        (4.9)
```

has the same trivial natural-error scale:

```text
||F_n||_(p,alpha)^p
 <<n^p sum_(m>=n)m^alpha << n^(p delta),
||F_n||_(p,alpha)<<n^delta.                                (4.10)
```

Changing `p` or `alpha` does not reduce the missing exponent.  One must improve
the `p`-th moment by a relative factor `n^(-p delta+o(1))`, or the norm by
`n^(-delta+o(1))`.  The endpoint result in the weighted-space literature,
boundedness at `alpha=-p-1` and convergence for `alpha<-p-1`, detects only the
already known line `Re(s)=1`; moving to (4.9) asks for exactly this new power.

## 5. General weights: the exact dual tradeoff

Let `1<p<infinity`, let `w_n(x)>0`, and use the norm

```text
||f||_(p,w_n)^p=integral_0^1 |f(x)|^p w_n(x)dx.             (5.1)
```

At a zero, weighted Holder gives the exact necessary product

```text
1/|rho_0|
 <=||E_n||_(p,w_n)
   (integral_0^(1/n)x^(q(beta-1))w_n(x)^(-q/p)dx)^(1/q).   (5.2)
```

Pointwise suppression of the origin collar enlarges the displayed dual
evaluation norm in the second factor.  For a power weight
`w(x)=x^(alpha p)`, that factor is finite exactly when

```text
beta>alpha+1/p.                                            (5.3)
```

Thus a power `x^alpha` gained on the collar moves the detected boundary right
by exactly `alpha`.  At the level of this geometric/trivial scaling,
logarithmic or subpower weights do not move the boundary and cannot pay the
fixed factor `n^(p-1)` in (2.6).  A modulation
`x^(i tau)` has modulus one and changes no norm.  A Mellin multiplier which is
small at large heights makes the principal value `1/rho_0` small by the same
multiplier and loses uniform detectability.  These identities show that a
generic geometric reweighting supplies no free power gain.  They do **not**
prove that every coefficient-adapted weight is useless: such a weight could
still succeed only by exploiting additional cancellation or distributional
information about the actual `E_n`.

## 6. The obstruction localizes to one mesoscopic range

The bathtub calculation identifies where a hypothetical zero can store its
principal mode.  With height `H asymp n`, constant beta-Mellin mass is achieved
at

```text
x asymp n^(-1/beta),       equivalently m=1/x asymp n^(1/beta).
                                                                    (6.1)
```

Fix a proposed boundary `b=1-delta` and suppose a candidate zero has
`beta>b`.  The trivial amplitude bound makes the part of (4.5) beyond
`R=n^(1/b)` negligible:

```text
sum_(m>R)|F_n(m)a_m(rho_0)|
 << n sum_(m>R)m^(-beta-1)
 << n^(1-beta/b)=o(1).                                     (6.2)
```

Therefore a zero strictly to the right of `b` must place a nonvanishing part
of (4.5) in the finite window

```text
n<=m<=n^(1/b).                                              (6.3)
```

For `b=0.99`, this is precisely `n<=m<=n^(100/99)`.

This yields a sharper sufficient target.  For any fixed `1<=p<=2`, put

```text
Q_(p,b)(n)=
 (sum_(n<=m<=n^(1/b))|F_n(m)|^p m^(-1-pb))^(1/p).          (6.4)
```

If along an unbounded sequence of `n`

```text
Q_(p,b)(n)<=n^o(1),                                        (6.5)
```

then (4.5), Holder, and (6.2) exclude every zero with `beta>b`.
The trivial bound is `Q_(p,b)(n)<<n^(1-b)=n^delta`; hence (6.5) still asks for
the exact fixed gain `n^(-delta+o(1))`, but only on the critical window.

This localized criterion is strictly an **open-half-plane** statement.  At
`beta=b`, the tail in (6.2) is only `O(1)`, and the window dual norm loses its
decaying power.  To include the boundary one must instead use the little-`o`
collar rate of Corollary 2.2, or enlarge the cutoff to
`n^(1/b)L(n)` with `L(n)->infinity` and prove a genuine endpoint decay (for
`p=1`, `Q=o(1)`; for `p>1`, enough decay to absorb the resulting logarithmic
dual factor).  Thus (6.5) alone does not prove zero-freeness on `Re(s)=b`.

This explains, rather than merely resembles, the range
`m<n<m^(1/sigma)` (with `m` there denoting the approximation length) isolated
in the recent weighted Dirichlet-space work.
It is the capacity transition forced by the Mellin principal mode.

The first collar remains a hostile fail-fast test.  For `n<=m<2n`,

```text
F_n(m)=M(m)+n gamma(n),                                    (6.6)
```

where `gamma(n)=sum_(k<n)M(k)/[k(k+1)]` and
`g(n)=M(n)/n+gamma(n)`.  Thus (6.5) already demands, for example when `p=1`,

```text
sum_(n<=m<2n)|M(m)+n gamma(n)| <= n^(1+b+o(1)).             (6.7)
```

This is a centered dyadic Mertens power estimate.  No unconditional theorem
audited here supplies it at any fixed `b<1`.

## 7. Comparison with available approximation rates

### 7.1 The exact natural collar

Baez--Duarte proved `||E_n||_1->0` from the prime number theorem and proved
that convergence in one fixed `Lp`, `p>1`, is equivalent in existence to a
nontrivial zero-free half-plane.  Theorem 2.1 quantifies the transition: for
the `0.99` line the missing endpoint gain is exactly `n^(-1/99)`.

The Vinogradov--Korobov-shaped bound

```text
M(x)<<x exp(-c(log x)^(3/5)(log log x)^(-1/5))              (7.1)
```

is still `x^(1-o(1))`.  When inserted into any fixed `p>1` Mertens-moment
majorant, the positive term `(p-1)log x` eventually dominates the sublinear
exponent in (7.1).  Such an input gives no fixed `p>1` integrability and no
fixed power in (2.4).  This says the available majorant fails; it does not
assert that the desired moment diverges.

### 7.2 Optimized Hilbert-space Dirichlet polynomials

With

```text
d_N^2=inf_(A_N) (1/(2pi)) integral_R
 |1-zeta(1/2+it)A_N(1/2+it)|^2 dt/(1/4+t^2),               (7.2)
```

Burnol's unconditional lower bound is

```text
liminf_(N->infinity)d_N^2 log N
 >=sum_(Re(rho)=1/2)m(rho)^2/|rho|^2.                      (7.3)
```

There is no unconditional upper bound `d_N->0`; that would prove RH.  Under
RH, Balazard--de Roton proved only the logarithmic-scale upper bound

```text
d_N^2 << (log log N)^(5/2+epsilon)/(log N)^(1/2).           (7.4)
```

Bettin--Conrey--Farmer obtain the conjectural `1/log N` scale only under RH
and an additional moment hypothesis on `1/zeta'(rho)`.  These Hilbert results
therefore provide no unconditional power that can be imported into (2.4).

### 7.3 The residual cannot be uniformly mollified across a zero

For every Dirichlet polynomial `A`,

```text
1-zeta(rho_0)A(rho_0)=1.                                   (7.5)
```

For the balanced natural polynomial (1.5), (7.5) is exactly (1.7) and (4.5).
Mean-square mollifier estimates can tolerate an exceptional point or a thin
set of heights; a uniform strip cannot.  A pointwise or local analytic norm
strong enough to control (7.5) is precisely the missing principal-mode
estimate.  Optimizing coefficients does not alter its value.

## 8. Truth boundary and best next target

What is proved here:

1. the unconditional zero-conditioned lower bound (2.1);
2. the exact sufficient rate (2.4)--(2.7), including the closed boundary;
3. polynomial `Lp` and weighted-norm growth forced by a candidate zero;
4. the literal identity between the compact collar and the modern weighted
   coefficient model;
5. the exact general weighted duality tradeoff (5.2), with the scope just
   stated;
6. the critical-window reduction (6.2)--(6.5).

What is not proved:

1. `||E_n||_1=o(n^-a)` for any fixed `a>0`;
2. `Q_(p,0.99)(n)=n^o(1)` for any fixed `p`;
3. a new Mertens moment estimate;
4. any uniform zero-free strip.

The most focused remaining Nyman target is not another norm or weight.  It is
the arithmetic estimate

```text
Q_(p,0.99)(n)
= (sum_(n<=m<=n^(100/99))
      |F_n(m)|^p m^(-1-0.99p))^(1/p)
 <= n^o(1)                                                   (8.1)
```

along an unbounded sequence of `n`, with (6.6) as the first-collar test.
This formulation prunes the infinite tail, permits any `1<=p<=2`, and retains
exactly the coefficient-specific cancellation that generic weights discard.
It would exclude zeros with `Re(s)>0.99`; the boundary caveat immediately
after (6.5) remains in force.  It remains a fixed-power Mobius problem, not an
unconditional consequence of present mollifier, PNT, or zero-density
technology.

## Primary literature checked

* L. Baez--Duarte,
  [*On Beurling's real variable reformulation of the Riemann hypothesis*](https://doi.org/10.1006/aima.1993.1038),
  Adv. Math. 101 (1993), 10--30.
* L. Baez--Duarte,
  [*Arithmetical aspects of Beurling's real variable reformulation of the Riemann hypothesis*](https://arxiv.org/abs/math/0011254),
  and the published
  [*New versions of the Nyman--Beurling criterion*](https://doi.org/10.1155/S0161171202013248).
* E. A. Gallardo-Gutierrez and D. Seco,
  [*Zero-free regions of the Riemann zeta function and approximation in weighted Dirichlet spaces*](https://doi.org/10.1007/s11785-025-01661-2),
  Complex Anal. Oper. Theory 19 (2025), article 38.
* J.-F. Burnol,
  [*A lower bound in an approximation problem involving the zeros of the Riemann zeta function*](https://doi.org/10.1006/aima.2001.2066),
  Adv. Math. 170 (2002), 56--70.
* M. Balazard and A. de Roton,
  [*Sur un critere de Baez--Duarte pour l'hypothese de Riemann*](https://arxiv.org/abs/0812.1689).
* S. Bettin, J. B. Conrey, and D. W. Farmer,
  [*An optimal choice of Dirichlet polynomials for the Nyman--Beurling criterion*](https://doi.org/10.1134/S0081543813030036),
  Proc. Steklov Inst. Math. 280 (2013), S30--S36.
* D. Allison,
  [*On obtaining zero-free regions for the zeta-function from estimates of M(x)*](https://doi.org/10.1017/S030500410004562X),
  Proc. Cambridge Philos. Soc. 67 (1970), 333--337.
