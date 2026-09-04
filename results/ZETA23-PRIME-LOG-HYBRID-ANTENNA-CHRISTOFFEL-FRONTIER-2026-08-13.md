# Prime-log hybrid antenna and Christoffel frontier

**Date:** 2026-08-13

**Verdict:** the hybrid quadrature idea gives a genuine fixed-power theorem,
but only below the prime-mesh Nyquist scale.  An explicit, stable antenna on
the actual prime nodes has sidelobes `O(Y^(-.019))` from
`Y^.01` through `Y^.4655`.  This is already stronger than the required
`.0180303234` exponent on that truncated band and works against arbitrary
signed low measures.  It does **not** control the remaining legal band

```text
Y^.4655 <= xi <= Y^(50/33).
```

On the full band, the strongest imported pointwise theorem for the actual
prime twist gives only a `(log Y)^(-3/10)` relative saving.  The exact
Christoffel formula shows that Lebesgue large-values estimates and DPP volume
averages cannot upgrade this: the optimizing design is allowed to be atomic
and can sit on the exceptional frequencies.  Thus neither a subpower-cost
construction nor a power lower bound for the full cancellation cost is
proved here.  The prime-log square-root law survives as a hypothesis, with
its entire unresolved content now located in the high tail above
`Y^(19/40-o(1))`.

No zeta bound or zero-free strip is claimed.

---

## 1. Exact dual and directional Christoffel identities

Fix `0<w<1`.  Put

```text
N_Y={p^k : Y exp(-w) <= p^k <= Y exp(w)},
u_n=log(n/Y),
M_Y=#N_Y,
a(xi)=(cos(xi u_n))_(n in N_Y).                         (1.1)
```

The target in the current real-cosine model is

```text
b(xi)=2 Re[(cosh((alpha+i xi)w)-1)/(w(alpha+i xi)^2)]
     =integral_(-w)^w phi(u) cos(xi u)du,
phi(u)=(1-|u|/w) exp(alpha u).                           (1.2)
```

Split the legal frequency interval into `L` and `H`.  The carrier-aware
cancellation cost is

```text
C_(L,H)=inf {||nu||+||mu|| :
             supp(nu) subset L, supp(mu) subset H,
             integral a d(nu+mu)=0,
             integral b dnu=1}.                         (1.3)
```

For `lambda in R^M`, write

```text
P_lambda(xi)=<lambda,a(xi)>,
eta_L(lambda)=sup_(xi in L)|b(xi)-P_lambda(xi)|,
epsilon_H(lambda)=sup_(xi in H)|P_lambda(xi)|.          (1.4)
```

### Lemma 1.1 (hybrid dual certificate)

For every `lambda`,

```text
C_(L,H) >=1/max(eta_L(lambda),epsilon_H(lambda)).       (1.5)
```

#### Proof

If `(nu,mu)` is feasible, then

```text
1=|integral_L b dnu|
 <=eta_L(lambda)||nu||+|integral_L P_lambda dnu|
 = eta_L(lambda)||nu||+|integral_H P_lambda dmu|
 <=eta_L(lambda)||nu||+epsilon_H(lambda)||mu||.         (1.6)
```

This proves (1.5).  Notice that no positivity or one-low-atom assumption is
used.  This is the correct way to extend a low quadrature to arbitrary signed
low measures; testing only the kernel against one atom is weaker.

For the one-atom problem, let

```text
R_H(q)=inf{||mu|| : integral_H a dmu=q}.                 (1.7)
```

There is also an exact optimal-design identity.  For a probability measure
`rho` on `H`, set

```text
G_rho=integral_H a(xi)a(xi)^T d rho(xi).                (1.8)
```

Then, with the pseudoinverse and the usual range condition,

```text
R_H(q)^2
 =inf_(rho in Prob(H)) q^T G_rho^dagger q.              (1.9)
```

Indeed, a representation `q=integral a dmu` of cost `C` gives
`rho=|mu|/C` and an `L^2(rho)` density of norm `C`, so the right side is at
most `C^2`.  Conversely, the least-squares density
`a(xi)^T G_rho^dagger q` represents `q` and has `L^1(rho)` norm at most its
`L^2(rho)` norm.  Taking the two infima proves (1.9).

Equation (1.9) is the exact carrier-relative Christoffel/DPP formula.  It
also fixes the scope of any adelic or exterior-power proposal: a common
determinant is irrelevant after cancellation; only this directional ratio
can matter.

---

## 2. The actual prime kernel and the unconditional logarithmic theorem

Define the sharp prime-power twist

```text
Q_Y(t)=sum_(n in N_Y) exp(i t log(n/Y)).                  (2.1)
```

The one-atom kernel is exactly

```text
K(s,t)=<a(s),a(t)>
      =1/2 Re[Q_Y(t-s)+Q_Y(t+s)].                        (2.2)
```

Klurman--Mangerel--Teravainen's sharp pointwise estimate, in the principal
character specialization recorded in the imported analytic baseline, says

```text
sum_(n<=x) Lambda(n)n^(it)
 << x/(log x)^(3/10)+x/(1+|t|)                           (2.3)
```

through every fixed polynomial range in `t`.  Abel summation by `1/log n`
and subtraction at the two fixed multiplicative endpoints give

```text
sum_(n in N_Y) [Lambda(n)/log n] exp(i t log(n/Y))
 << Y/(log Y)^(13/10)+Y/[(1+|t|)log Y].                  (2.4)
```

The coefficient in (2.4) is `1/k` at `n=p^k`.  Replacing it by `1` costs
only the number of proper prime powers in the window, `O_w(sqrt(Y))`.
Since `M_Y asymp_w Y/log Y`, (2.1) therefore satisfies, uniformly for
`|t|<=Y^A` with fixed `A`,

```text
|Q_Y(t)|
 << M_Y[(log Y)^(-3/10)+(1+|t|)^(-1)
                         +(log Y)/sqrt(Y)].             (2.5)
```

This is a theorem about the exact hard window and the actual prime powers,
not a random-phase model.

Let `S` be a fixed compact low-frequency set.  The prime number theorem
gives, uniformly for `s in S`,

```text
||a(s)||^2 asymp_(S,w) M_Y.                              (2.6)
```

If `H=[T_Y,Y^A]`, where `T_Y` is a positive power of `Y`, then (2.2)--(2.6)
and the elementary directional test give

```text
R_H(a(s))
 >=||a(s)||^2/sup_(t in H)|K(s,t)|
 >>_(S,w) (log Y)^(3/10).                               (2.7)
```

Thus the observed one-low-atom architecture has a rigorous growing cost,
but only a logarithmic one.  Equation (2.7) is nowhere near
`Y^.0180303234`.

---

## 3. Actual-prime hat quadrature gives a fixed power below `Y^(19/40)`

The low-band part can be handled much more sharply by choosing the dual
coefficients, rather than taking the unweighted kernel direction.

Baker--Harman--Pintz prove that every sufficiently large interval
`[x-x^(21/40),x]` contains a prime.  Consequently the prime-log nodes in
`[-w,w]`, including their distances from the two endpoints, have maximal
mesh

```text
h_Y <<_w Y^(-19/40).                                    (3.1)
```

Write the prime nodes as `v_1<...<v_J`.  On `[v_1,v_J]`, let `ell_j` be the
ordinary continuous piecewise-linear hat function at `v_j`, and define

```text
lambda_j=integral_(v_1)^(v_J) phi(u)ell_j(u)du,
lambda_n=0 for the proper prime-power coordinates.       (3.2)
```

These are explicit nonnegative actual-node coefficients and

```text
sum_j lambda_j <=integral_(-w)^w phi(u)du=O_(w,alpha)(1).
                                                                    (3.3)
```

Let

```text
P_Y(t)=sum_j lambda_j cos(t v_j).                         (3.4)
```

Linear interpolation of `exp(i t u)` on an interval of length at most
`h_Y` has pointwise error at most `t^2 h_Y^2/8`.  The omitted endpoint
strips have `phi`-mass `O(h_Y^2)`, because `phi` vanishes linearly at both
endpoints.  Therefore

```text
|P_Y(t)-b(t)| <<_(w,alpha) (1+t^2)h_Y^2
                          <<(1+t^2)Y^(-19/20).          (3.5)
```

This bound is deterministic.  It uses only the actual prime nodes and the
published maximal-gap theorem.

The compact tent in (1.2) has a derivative of bounded variation and vanishes
at the endpoints, so two integrations by parts give

```text
|b(t)|<<_(w,alpha)(1+t^2)^(-1).                          (3.6)
```

### Theorem 3.1 (truncated hybrid power antenna)

Let

```text
L_Y=[0,Y^tau],
H_Y^0=[Y^tau,Y^sigma],
0<tau<sigma<19/40.                                      (3.7)
```

For the explicit coefficients (3.2),

```text
eta_(L_Y)(lambda)
 <<Y^[-2(19/40-tau)],

epsilon_(H_Y^0)(lambda)
 <<Y^(-2 tau)+Y^[-2(19/40-sigma)].                      (3.8)
```

Consequently

```text
C_(L_Y,H_Y^0)
 >>Y^d,
d=min{2 tau,2(19/40-sigma)}.                            (3.9)
```

#### Proof

The first line of (3.8) is (3.5) on `L_Y`.  On `H_Y^0`, combine (3.5) with
(3.6).  Lemma 1.1 then gives (3.9).

For example,

```text
tau=.01,       sigma=.4655
```

give

```text
d=min(.02,.019)=.019>.0180303234.                       (3.10)
```

This is a theorem-grade fixed-power kill of the carrier architecture on the
truncated aperture `[0,Y^.4655]`.  Because Lemma 1.1 was used, it includes
arbitrary signed low measures supported in `[0,Y^.01]`; it is not restricted
to the numerically observed one-low-atom design.

---

## 4. Why the proof stops, and exactly where it stops

The full legal aperture is

```text
B=Y^(50/33)=Y^(1.51515...).                              (4.1)
```

The interpolation remainder in (3.5) becomes order one when
`|t|h_Y` becomes order one.  Higher-order local interpolation changes
`(t h_Y)^2` to a higher power but does not cross the same barrier

```text
|t| about h_Y^(-1)=Y^(19/40).                           (4.2)
```

Thus the BHP mesh theorem settles the low/mid transition and leaves the
specific high-tail problem

```text
sup_(Y^(19/40-o(1))<=|t|<=Y^(50/33))
 |sum_(p~Y) lambda_(p,Y) exp(i t log(p/Y))|
 <=Y^(-delta),       delta>.0180303234,                 (4.3)
```

for coefficients which simultaneously retain the low carrier.

There are two tempting but invalid shortcuts.

### 4.1 The second-derivative heuristic is an all-integer estimate

For a smooth all-integer sum, `f(x)=t log x` has
`|f''(x)|asymp t/Y^2`, and van der Corput suggests the normalized scales
`Y^(-1/2)` near `t=Y` and `Y^(-1/4)` near `t=Y^(3/2)`.  The required sum in
(4.3), however, is supported on primes and has gap/quadrature coefficients.
Vaughan decomposition does not transfer the all-integer curvature bound:

```text
exp(i t log(mn))=m^(it)n^(it),                            (4.4)
```

so the height twist is absorbed into the two arbitrary coefficient
sequences of every Type-II block.  The mixed derivative of `t log(mn)` is
zero.  No classical coefficient-uniform Type-II estimate supplies the
claimed one-variable second-derivative gain for (4.3).

### 4.2 Corrected von-Mangoldt weights retain the zero-sensitive term

Replacing the hat weights by `Lambda(n)/log n` restores an exact
multiplicative coefficient, but the pointwise theorem then reverts to
(2.5), with its logarithmic term.  A fixed-power complex prime-interval
bound over the corresponding power-wide family is a Turan zero-localization
input; the scalar prime-polynomial audit records the precise criterion.  The
present real weighted antenna is not asserted to be logically equivalent to
a strip, but obtaining (4.3) from a standard von-Mangoldt twist would already
be zero-free-region strength, not a routine exponent-pair corollary.

The gap weights and the von-Mangoldt weights therefore fail for opposite
reasons:

```text
gap/hat weights:       stable low quadrature, no known high-t arithmetic;
Lambda/log weights:    exact arithmetic, only logarithmic pointwise saving.
                                                                    (4.5)
```

Bridging (4.5) is the surviving hybrid hypothesis.

---

## 5. Why large-values and DPP averaging do not bridge the high tail

For any probability design `rho`, Cauchy--Schwarz in (1.8) gives

```text
q^T G_rho^dagger q
 >=||q||^4/[q^T G_rho q]
 = ||q||^4/integral_H |<q,a(t)>|^2 d rho(t).            (5.1)
```

If `rho` were Lebesgue measure, a mean-value or large-values theorem would
control the denominator.  But (1.9) takes the infimum over **all** probability
measures.  An optimizing `rho` may be supported entirely on isolated large
values, exactly as the finite exchange computations are supported on
`M+1` atoms.  A bound on the Lebesgue measure or on the number of exceptional
frequencies therefore does not bound (5.1) without an additional theorem
about the span and Gramian of the exceptional atoms.

The diagonal large-values term is also at the geometry's natural threshold.
At a proposed cost `C`, the necessary kernel height is roughly `M/C`.
Second-moment large-values bounds permit `O(C^2)` separated peaks at that
height.  An orthogonal family of `C^2` such peaks can represent a unit
direction with `l^1` cost `C`; this is precisely the square-root/random-
polytope mechanism, not a contradiction to it.

Consequently:

```text
Lebesgue large values alone                         INSUFFICIENT;
common DPP determinant/fermionic volume             CANCELS;
directional exceptional-set span/Christoffel bound  REQUIRED.       (5.2)
```

This also scopes any proposed adelic capacity identity.  It must apply to a
specific legal design and bound the directional ratio in (1.9) itself.
An identity for `det G`, or an inequality whose local product has no
independent lower bound, is vacuous for this problem.

---

## 6. Decision: binary test of the prime-log square-root hypothesis

The attack produced three exact conclusions.

1. The actual one-atom kernel has the unconditional full-aperture lower cost
   `(log Y)^(3/10)`, by a published sharp prime-twist theorem.
2. A new explicit actual-prime hat antenna proves the desired fixed exponent
   against **all signed low measures** through `Y^.4655`.
3. Neither large-values counting nor the exterior-power/DPP ratio can extend
   this to the full aperture, because atomic designs may concentrate on the
   exceptional high frequencies.

The remaining binary hypothesis can now be stated without Remez scaling:

```text
H_square-root:
there exist actual-node coefficients lambda_Y with

sup_(0<=xi<=Y^(50/33))
 |b(xi)-sum_(n in N_Y)lambda_(n,Y)cos(xi log(n/Y))|
 <=Y^(-delta+o(1))

for some delta>.0180303234.                              (6.1)
```

Theorem 3.1 proves (6.1) up to `xi=Y^.4655`.  The interval from there to
`Y^(50/33)` is the whole unresolved content.  Proving (6.1) kills the current
positive-prime-null route.  Constructing a carrier cancellation of
subpower cost on that full interval promotes it.  Neither outcome is
obtained here.

```text
full-aperture power antenna                         OPEN;
full-aperture cost >=Y^.0180303234                  OPEN;
explicit full-aperture subpower-cost design         NOT FOUND;
uniform zero-free strip                             NOT PROVED.       (6.2)
```
