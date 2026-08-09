# R99 prime singular-trace boundary gate

Status: exact Schatten/Lorentz membership, prime-adapted spectral residue,
horizontal and vertical ideal-norm discontinuity, oscillatory residue collapse,
and relative-comparator ledger.  A prime-specific singular trace can see the
first Euler trace which `det_2` deletes, but precisely for that reason it is
not continuous, let alone holomorphic, on the family `diag_p(p^(-s))` across
`Re(s)=1`.  A relative trace can move left only as far as the power accuracy
of its prime comparator.  No fixed strip or no-strip theorem is proved.

Date: 2026-08-07.

## 1. Verdict

Let

```text
D_s=diag_(p prime)(p^(-s))
```

on `ell^2(P)`.  R97 showed that Hilbert--Schmidt regularization loses the
first prime trace carrying the divisor of `1/zeta`.  A natural reaction is
to replace the ordinary trace by a singular trace adapted to

```text
sum_(p<=x) 1/p = log log x + B_1+o(1).                 (1.1)
```

This report executes that idea.  The result is a useful but negative
topology theorem.

1. For `sigma>0`,

   ```text
   D_s in S_q  iff  q sigma>1.                          (1.2)
   ```

   At `s=1`, `D_1` is in ordinary weak trace class, but every standard
   logarithmically normalized Dixmier trace gives it value zero because

   ```text
   [sum_(n<=N)1/p_n]/log N ->0.                         (1.3)
   ```

2. The prime-adapted Marcinkiewicz scale

   ```text
   Psi(N)=log log(e^e+N)-1                              (1.4)
   ```

   does recover the missing trace:

   ```text
   [sum_(n<=N)1/p_n]/Psi(N) ->1.                        (1.5)
   ```

3. That recovery destroys analytic continuity.  For every real
   `epsilon>0` and every real `t!=0`,

   ```text
   ||D_(1+epsilon)-D_1||_(M_Psi) >=1,                   (1.6)

   ||D_(1+it)-D_1||_(M_Psi) >=4/pi.                    (1.7)
   ```

   The constants mean liminf lower bounds in the defining Ky Fan
   normalization and are independent of how small `epsilon` or `t` is.
   Thus `s -> D_s` is operator-norm continuous but has an order-one boundary
   layer in every prime-residue topology strong enough to see (1.5).

4. The corresponding complex spectral residue is concentrated at the unit
   character:

   ```text
   lim_(N->infinity)
     [sum_(n<=N)p_n^(-1-it)]/Psi(N)
       =1,  t=0,
       =0,  t!=0.                                      (1.8)
   ```

   It therefore cannot be the restriction of a holomorphic trace functional
   on this operator family.

5. Subtracting a smooth comparator `C_s=diag(q_n^(-s))` is honest, but its
   trace-class range is exactly controlled by weighted prime-quantile error:

   ```text
   D_a-C_a in S_1
    iff sum_n q_n^(-a)|(p_n-q_n)/q_n|<infinity          (1.9)
   ```

   when `p_n/q_n->1`.  A power PNT with exponent `theta` makes the relative
   trace class for `Re(s)>theta` (up to logarithms).  The known
   Vinogradov--Korobov error certifies no fixed line left of one.  Hence the
   relative construction consumes the same fixed-power input it was meant
   to create.

6. This is forced analytically.  Near any zeta zero `rho` with
   `Re(rho)>1/2`, the prime zeta function has the local logarithmic
   singularity

   ```text
   P(s)=sum_p p^(-s)=log zeta(s)-sum_(k>=2)P(ks)/k.     (1.10)
   ```

   The second term is holomorphic there.  A holomorphic regularized first
   trace in a fixed half-plane would therefore already exclude every zeta
   zero in that half-plane.

The proposed singular trace does see the lost arithmetic datum.  It sees it
as a discontinuous exceptional-character residue, not as a holomorphic
Fredholm trace.

```text
ordinary Dixmier trace                         TOO COARSE / VALUE ZERO
prime log-log singular residue                 RECOVERS FIRST TRACE
analytic continuity of D_s in that topology    FALSE, ORDER-ONE JUMP
vertical phase regularity                       FALSE, UNIT-CHARACTER ATOM
relative smooth comparator                      POWER-PNT LIMITED
fixed zero-free strip                           NOT PROVED.             (1.11)
```

## 2. Schatten and weak-ideal placement

Let `p_n` denote the `n`th prime.  The singular values of `D_s` are
`p_n^(-sigma)`, where `sigma=Re(s)`.  Euler's theorem on the prime harmonic
series, together with convergence of the prime zeta series to the right of
one, gives

```text
sum_n mu_n(D_s)^q=sum_p p^(-q sigma)<infinity
 iff q sigma>1.                                         (2.1)
```

This proves (1.2).  The prime number theorem gives

```text
p_n~n log n,                                            (2.2)

n mu_n(D_1)=n/p_n~1/log n.                              (2.3)
```

Thus `D_1` belongs both to the weak Schatten ideal defined by
`sup n mu_n` and to the larger logarithmic Ky Fan/Macaev ideal (the two
notations are sometimes both written `L_(1,infinity)` in the literature).
It is not trace class because `sum 1/p` diverges.

For the ordinary Dixmier normalization, Mertens' theorem for primes gives

```text
sum_(n<=N)mu_n(D_1)
 =log log p_N+B_1+o(1)
 =log log N+O(1),                                       (2.4)
```

and hence (1.3).  In particular `D_1` lies in the kernel, indeed the
separable part, seen by every ordinary logarithmic Dixmier residue.  Moving
from `S_2` to the standard weak trace ideal does not restore the missing
Euler trace.

General singular symmetric functionals on Marcinkiewicz ideals are standard;
the relevant background is Lord--Sedaev--Sukochev,
[*Dixmier Traces as Singular Symmetric Functionals and Applications to
Measurable Operators*](https://arxiv.org/abs/math/0501131).  The project only
uses the elementary spectral limits below, not a claimed new construction of
that theory.

## 3. The prime-adapted residue

Put

```text
Psi(x)=log log(e^e+x)-1.                                (3.1)
```

This is increasing, concave, vanishes at zero, and is asymptotic to
`log log x`.  On compact operators define the Marcinkiewicz gauge

```text
||T||_(M_Psi)
 =sup_(N>=1) Psi(N)^(-1)sum_(n<=N)mu_n(T),              (3.2)
```

with an immaterial bounded-range modification when `Psi(N)` is small.
Equations (2.2)--(2.4) show that `D_1 in M_Psi` and prove

```text
Res_P(D_1)
 :=lim_(N->infinity)
   Psi(N)^(-1)sum_(n<=N)mu_n(D_1)=1.                    (3.3)
```

Because the ordinary limit exists, every generalized-limit version of this
prime spectral residue has the same value.  This is exactly the coefficient
needed to recognize the logarithmic divergence of the first prime trace
near `s=1`.

The normalization is prime-specific.  That is allowed here: the proposal is
to save the zeta determinant by choosing a topology tailored to the prime
spectrum.  The next section shows the exact cost.

## 4. Horizontal discontinuity

There is first an ideal-independent obstruction.  Let `I` be any Banach
operator ideal containing `D_1` and every `D_(1+epsilon)`, and let
`tau:I->C` be bounded with

```text
tau(A)=0 for A in S_1,             tau(D_1)=c!=0.        (4.0)
```

Every singular trace which detects `D_1` has this form after normalization.
For every `epsilon>0`, `D_(1+epsilon) in S_1`, and hence

```text
||D_(1+epsilon)-D_1||_I
 >=abs(tau(D_(1+epsilon)-D_1))/||tau||
 =abs(c)/||tau||.                                      (4.0a)
```

Thus *any* Banach-ideal topology carrying a bounded singular functional
which restores the missing prime trace makes the Euler family discontinuous
at one.  The following calculation gives the sharp natural normalization in
`M_Psi`.

Fix `epsilon>0`.  In the common prime basis,

```text
|D_(1+epsilon)-D_1|
 =diag_p[p^(-1)(1-p^(-epsilon))].                       (4.1)
```

For any `N`, the sum of the largest `N` diagonal entries is at least the sum
over the first `N` primes.  Therefore

```text
||D_(1+epsilon)-D_1||_(M_Psi)
 >=limsup_(N->infinity) Psi(N)^(-1)
   sum_(n<=N)[1/p_n-1/p_n^(1+epsilon)].                 (4.2)
```

The second series converges and the first has normalized limit one.  This
proves (1.6).

For every fixed `sigma>1`, the same calculation gives the spectral residue

```text
Res_P(D_sigma)=0,              Res_P(D_1)=1.            (4.3)
```

Thus neither the operator family nor its prime residue is right-continuous
at one in `M_Psi`.  Notice the topology dependence: `D_s` is continuous in
operator norm.  The discontinuity appears exactly when the topology is
strengthened enough to retain the divergent first trace.

No Banach-ideal-valued holomorphic map can have this behavior, since
holomorphy implies norm continuity.  Consequently the prime-adapted singular
trace cannot be inserted into the analytic Fredholm determinant argument as
a holomorphic replacement for `Tr D_s`.

## 5. Vertical discontinuity and the exceptional character

Fix `t!=0`.  Entrywise,

```text
|p^(-1-it)-p^(-1)|
 =|1-exp(-it log p)|/p.                                  (5.1)
```

Let `f(v)=|1-exp(-iv)|=2|sin(v/2)|`.  Its period mean is

```text
f_bar=(1/(2pi))integral_0^(2pi)f(v)dv=4/pi.             (5.2)
```

Prime partial summation and the PNT give, for each fixed nonzero `t`,

```text
sum_(p<=x)f(t log p)/p
 =integral_(log 2)^(log x) f(tv)dv/v+o(log log x)
 =(4/pi)log log x+o(log log x).                         (5.3)
```

For completeness, the second equality follows by writing `f=f_bar+g`;
the primitive of the mean-zero periodic function `g` is bounded, so
Dirichlet integration makes `integral g(tv)dv/v=O_t(1)`.  The PNT error is
`o(log log x)` after Stieltjes partial summation.

As in Section 4, a Ky Fan sum is at least the sum over the first `N` prime
coordinates.  Equations (5.1)--(5.3) prove (1.7).  In particular there is no
`M_Psi`-norm vertical continuity at `t=0`.

The complex, rather than absolute, sum is even more revealing.  Partial
summation gives

```text
sum_(p<=x)p^(-1-it)
 =integral_(log 2)^(log x)exp(-itv)dv/v+o(log log x)
 =o(log log x),                 t!=0.                   (5.4)
```

The main integral converges conditionally at infinity; the displayed weaker
`o(log log x)` is all that is needed.  Dividing by `Psi(N)` proves (1.8).

Thus the residue which equals one at the unit prime character equals zero at
every fixed nontrivial vertical character.  This is the singular-trace
version of the exceptional Euler-order boundary layer in R96.  A generalized
limit cannot make the map holomorphic: the ordinary limits already exist and
have the discontinuity (1.8).

## 6. Relative comparison and its exact arithmetic cost

A possible repair is to subtract a smooth diagonal model.  Let `q_n>0`,
`q_n/p_n->1`, and put

```text
C_s=diag_n(q_n^(-s)),
epsilon_n=(p_n-q_n)/q_n.                                (6.1)
```

For a fixed real `a>0`, the mean value theorem, uniformly once
`p_n/q_n in [1/2,2]`, gives constants depending only on `a` such that

```text
|p_n^(-a)-q_n^(-a)| asyp_a q_n^(-a)|epsilon_n|.         (6.2)
```

Therefore

```text
D_a-C_a in S_1
 iff sum_n q_n^(-a)|epsilon_n|<infinity.                (6.3)
```

This proves (1.9).  It also prevents a semantic shortcut: subtracting the
prime divergence is easy at one, but extending the *relative* first trace a
fixed distance left requires power-weighted accuracy of the prime model.

Take the canonical smooth quantile `q_n=li^(-1)(n)`.  If a power PNT

```text
pi(x)-li(x)=O(x^theta log^B x),          theta<1,        (6.4)
```

is available, monotonic inversion gives, with harmless logarithmic losses,

```text
|p_n-q_n|/q_n
 <<q_n^(theta-1)log^(B+1)q_n.                           (6.5)
```

Since `q_n asyp n log n`, (6.2) is summable for every `a>theta`.  Hence a
fixed-power PNT constructs a relative trace in the corresponding half-plane.
This is a valid forward implication, but it is not a new proof of the input.

The Vinogradov--Korobov error is `x exp[-c(log x)^(3/5)(log log x)^(-1/5)]`.
Inserted into (6.2), its available majorant is not summable with
`q_n^(-a)` for any fixed `a<1`.  Thus current prime asymptotics certify the
relative construction only up to the abscissa-one boundary.  This statement
is about what the estimate proves; it is not a lower bound on the actual
quantile error.

One can set `q_n=p_n` and make the relative trace zero, but then the
comparator trace is the original prime zeta function.  All arithmetic has
merely moved into the model.

## 7. Holomorphic first trace is already the strip theorem

For `Re(s)>1`, the Euler logarithm gives

```text
log zeta(s)=sum_(k>=1)P(ks)/k,
P(s)=sum_p p^(-s).                                      (7.1)
```

For a recent direct treatment of the logarithmic expansion at one, see
Kawalec,
[*On the series expansion of the prime zeta function about s=1 and its
coefficients*](https://arxiv.org/abs/2603.21535).  Only the classical local
singularity, not any claimed new zero-free information, is used here.

Let `rho` be a nontrivial zeta zero with `Re(rho)>1/2` and choose a small
disc around it containing no other zero and no branch obstruction.  For
every `k>=2`, `Re(k rho)>1`, so `P(ks)` is holomorphic on a sufficiently
small disc.  Consequently

```text
P(s)=log zeta(s)-sum_(k>=2)P(ks)/k                     (7.2)
```

has the logarithmic singularity of `log zeta(s)` at `rho`.

It follows that any single-valued holomorphic regularized first trace which
agrees with `P(s)` to the right of one would exclude such a `rho` from its
domain.  Equivalently, constructing that trace throughout
`Re(s)>1-eta>1/2` is already a fixed zero-free-strip theorem.  A determinant
notation does not weaken the analytic task.

There is no contradiction between Sections 3 and 7.  The prime residue sees
the coefficient of the singularity at the real endpoint, while a
holomorphic trace must also control all finite parts and every vertical
character.  Equations (1.6)--(1.8) show exactly why the residue alone cannot
do that.

## 8. Disposition

The singular-trace idea reaches farther than the Hilbert--Schmidt determinant
in one precise sense: it recovers the first prime divergence rather than
regularizing it away.  It does not turn that divergence into an analytic
operator invariant.

```text
D_s Schatten placement                         EXACT
ordinary Dixmier value at s=1                  ZERO
prime-adapted log-log residue                   ONE
horizontal M_Psi continuity at s=1             FALSE
vertical M_Psi continuity at s=1               FALSE
residue away from unit character               ZERO
relative comparator criterion                  EXACT
fixed-power continuation from known PNT        UNAVAILABLE
fixed zero-free strip                           NOT PROVED
failure of every fixed strip                    NOT PROVED.             (8.1)
```

The only live operator continuation after R97 and R99 is therefore a
genuinely signed relative first trace whose topology is weak enough for
analytic motion in `s`, strong enough to retain the exceptional prime
character, and equipped with a comparator estimate not equivalent to a
fixed-power PNT.  The order-one boundary layer proves that no ordinary
unitarily invariant Marcinkiewicz-ideal continuity argument supplies all
three properties for free.

The finite probe
[`src/prime_singular_trace_probe.py`](../src/prime_singular_trace_probe.py)
reports the slow finite-cutoff approach to (1.5), (1.7), and (1.8).  It is a
normalization check, not evidence for a zero-free region.
