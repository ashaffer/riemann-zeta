# Varying the sharp cutoff and grid offset: exact reconstruction and the Turan obstruction

Status: rigorous theorem card, 2026-08-11.  This note determines exactly what
is gained by varying the cutoff in the two scalar prime polynomials and by
oversampling their critical lattice.  It proves no zero-free strip, prime
Pick lower edge, or carrier margin.

## 1. Verdict

Write `u=log X`, `y_n=log n`, and

```text
Z_u(t)=sum_(y_n<=u) Lambda(n)n^(-1/2)*exp(i*t*y_n),
A_u(t)=Im Z_u(t),
D_u(t)=sum_n Lambda(n)n^(-1/2)*(u-y_n)_+*cos(t*y_n).  (1.1)
```

There is a useful exact upgrade if the cutoff is known on a continuum.  If

```text
J_u(t)=integral_0^u A_v(t)dv,                          (1.2)
```

then, for `0<Delta<u`,

```text
[D_(u+Delta)-2D_u+D_(u-Delta)
 +i*(J_(u+Delta)-2J_u+J_(u-Delta))]/Delta

 =sum_n Lambda(n)n^(-1/2)
      *(1-abs(log n-u)/Delta)_+*exp(i*t*log n).        (1.3)
```

Thus varying `(A,D)` really does recover a **complex** triangular log-shell,
with every von Mangoldt coefficient and sharp endpoint convention retained.
It does not recover a sharp complex prefix from value bounds with comparable
norm: the real prefix is the cutoff derivative of `D`, and that derivative
is ill-conditioned at integer resolution.

Varying the lattice offset can close the discrete-versus-continuous gap at a
fixed cutoff.  Indeed, the union of all offsets of a lattice of step
`2*pi/u` is the whole real line.  It cannot enlarge the range of cutoffs or
by itself improve a logarithmic arithmetic saving into a fixed power saving.

These two facts do not supply Turan's localization hypothesis.  The current
transition family

```text
T*(log T)^(-C) <= X <= T*(log T)^C                   (1.4)
```

has a log-cutoff aperture `2C*loglog T`.  For fixed `D>0` and fixed
`0<beta<1`, Turan requires prime intervals throughout a log-cutoff aperture,
centered at `D*log T`, of width

```text
2*D*beta^(1/6)*log T+O(1).                            (1.5)
```

It also requires a `T^(-beta)` saving.  The KMT estimate gives only a
logarithmic saving, even if it is granted at every power length `T^D`.
Finite differences with subpower condition number preserve this mismatch.

The exact outcome is therefore:

```text
all offsets       -> continuous t-data at the same cutoff;
continuous cutoff -> complex triangular shells inside the same aperture;
current aperture  -> only X=T^(1+o(1)), not a power-wide family;
KMT               -> T^(-o(1)), not the fixed T^(-beta) Turan saving.
                                                               (1.6)
```

No fixed strip follows.

## 2. Exact cutoff calculus

The following identities hold for an arbitrary finite coefficient sequence;
in particular they hold coefficientwise for (1.1).  The notation in (1.1)
includes `y_n=u` in `Z_u`; the ramp in `D_u` is zero there.

### Theorem 2.1 (prefix, Cesaro, and shell identities)

For every fixed real `t`, `D_u(t)` is continuous and piecewise linear in
`u`, and

```text
partial_u^+ D_u(t)=Re Z_u(t),
partial_u^- D_u(t)=Re Z_(u-)(t).                      (2.1)
```

Here `Z_(u-)` omits a possible term with `log n=u`.  Equivalently, in the
sense of distributions,

```text
partial_u^2 D_u(t)
 =sum_n Lambda(n)n^(-1/2)*cos(t*log n)*delta_(log n). (2.2)
```

For every `Delta>0`,

```text
D_(u+Delta)(t)-D_u(t)
 =Delta*Re Z_u(t)
  +sum_(u<log n<=u+Delta) Lambda(n)n^(-1/2)
       *(u+Delta-log n)*cos(t*log n).                 (2.3)
```

Moreover,

```text
J_u(t)=sum_n Lambda(n)n^(-1/2)*(u-log n)_+*sin(t*log n),
                                                               (2.4)
```

and (1.3) holds.  Finally, for `a<b`,

```text
[partial_u^+D_b(t)-partial_u^+D_a(t)]
       +i*[A_b(t)-A_a(t)]
 =sum_(a<log n<=b) Lambda(n)n^(-1/2)*exp(i*t*log n).  (2.5)
```

#### Proof

For one frequency `y`, the cutoff kernels are `1_(y<=u)` and
`(u-y)_+`.  The right and left derivatives of the latter give (2.1), and
one more distributional derivative gives (2.2).  Subtracting its values at
`u+Delta` and `u` gives (2.3), including the zero-weight upper endpoint.
Integrating `1_(y<=v)` from `0` to `u` gives `(u-y)_+`, which proves
(2.4).  The central second difference of `(u-y)_+` is

```text
(Delta-abs(y-u))_+.
```

Applying this to the cosine and sine parts proves (1.3).  Subtracting the
two right derivatives in (2.1), and separately the two imaginary prefixes,
proves (2.5).  QED

The identity

```text
D_u(t)=Re integral_0^u Z_v(t)dv                     (2.6)
```

is the same statement in integral form.  It is also the log-variable form
of the exact identity `D_X=Re integral_1^X Z_Y dY/Y` in the scalar audit.

## 3. What value estimates transfer to

Exact reconstruction and stable reconstruction are different.  Put, for a
fixed `t` and `I=[u-Delta,u+Delta]`,

```text
H_A(I,t)=sup_(v in I) abs A_v(t),
H_D(I,t)=sup_(v in I) abs D_v(t)/v.                   (3.1)
```

### Proposition 3.1 (exact condition number for the tent transfer)

If `0<Delta<u`, the complex tent in (1.3), denoted by
`Q_(u,Delta)(t)`, satisfies

```text
abs Q_(u,Delta)(t)
 <=2*H_A(I,t)+(4*u/Delta)*H_D(I,t).                   (3.2)
```

Indeed,

```text
abs[J_(u+Delta)-2J_u+J_(u-Delta)]
 <=2*Delta*H_A(I,t),

abs[D_(u+Delta)-2D_u+D_(u-Delta)]
 <=[(u+Delta)+2u+(u-Delta)]*H_D(I,t)
 =4u*H_D(I,t).                                        (3.3)
```

This preserves the special extra logarithm in the `D` estimate.  In the
transition range, the scalar audit proves

```text
H_A << sqrt(exp u)/u^(3/10),
H_D << sqrt(exp u)/u^(13/10).                         (3.4)
```

For fixed `Delta>0`, with all cutoffs in `I` still in the transition range,
(3.2) therefore gives

```text
abs Q_(u,Delta)(t)<<_Delta sqrt(exp u)/u^(3/10).      (3.5)
```

So cutoff variation converts the two real observables into a complex
**smooth dyadic shell without losing the KMT logarithmic exponent**.  It
does not create a fixed power saving.

For a sharp shell, (2.5) shows the asymmetry precisely:

```text
abs[A_b(t)-A_a(t)]<=2*sup_(a<=v<=b) abs A_v(t),       (3.6)
```

whereas its real part requires one cutoff derivative at each endpoint.  If
`(u,u+epsilon]` contains no log-integer, then

```text
partial_u^+D_u(t)=[D_(u+epsilon)(t)-D_u(t)]/epsilon. (3.7)
```

A bound for `D_v/v` transfers through (3.7) with coefficient of order
`u/epsilon`.  A coefficient-blind choice that is guaranteed not to cross
any possible sharp endpoint near `N` takes `epsilon` of order at most

```text
log(n+1)-log n asymp 1/N,                             (3.8)
```

and its direct triangle-inequality bound costs order `N*log N`.  For the
fixed von Mangoldt sequence one can use the actual next prime-power gap;
(3.8) is not asserted to be a lower bound for every arithmetic endpoint.
It is the uniform resolution of the elementary exact-differentiation route.

This instability is not an artefact of the estimate.  Consider the
one-atom version of (1.1), with mass `c>0` at `y_0`, and choose
`t_0*y_0 in 2*pi*Z`.  At `t=t_0`, on
`y_0<=u<=y_0+epsilon`,

```text
A_u(t_0)=0,
D_u(t_0)=c*(u-y_0),
sup abs(D_u(t_0))/u <=c*epsilon/y_0,
partial_u^+D_u(t_0)=c.                               (3.9)
```

Thus no pointwise inequality can bound the real prefix derivative by the
two value norms with a constant `o(y_0/epsilon)`.  This is a conditioning
counterexample for the cutoff transform; it is not asserted to replace the
von Mangoldt coefficients by an adversarial sequence in an arithmetic
theorem.

The tent formula avoids integer resolution, but it supplies a triangular
weight, not the arbitrary sharp intervals in Turan's stated criterion.  A
new smoothed localization criterion could change that interface; none is
proved or used here.

## 4. Critical grids and varying offsets

Fix `u>0` and put

```text
h_u=2*pi/u,
t_(r,k)=t_0+r+k*h_u,       0<=r<h_u.                  (4.1)
```

Then

```text
union_(0<=r<h_u) {t_(r,k): k in Z}=R.                 (4.2)
```

Consequently, a bound assumed for **every** offset, with the maximum taken
over every grid point lying in an interval, is exactly a continuous bound
on that interval.  More precisely, for any function `F`,

```text
sup_(0<=r<h_u) max_(k: t_(r,k) in I_t) abs F(t_(r,k))
 =sup_(t in I_t) abs F(t).                            (4.2a)
```

There is no interpolation loss in this all-offset statement.  An average,
an almost-everywhere assertion, or a choice of one favorable offset does
not give the left side of (4.2a); the exceptional offset may depend on the
cutoff and on the target ordinate.

For the arithmetic polynomial, an oscillation bound can also be anchored
uniformly in the offset.  With `d=floor(T/h_u)`, the scalar audit proves

```text
abs[d^(-1)*sum_(k<d) Z_u(t_(r,k))]
 << exp(u/4)/T+exp(u/2)*u^2/T+u*exp(-u/2).            (4.3)
```

The right side is `o(1)` for `exp u=T*(log T)^O(1)`, uniformly in `r`,
because the offset contributes only a unit-modulus phase.  Hence on every
such grid

```text
max_k abs A_u(t_(r,k))<=osc_k A_u(t_(r,k))+o(1).      (4.4)
```

There is genuine blindness on one critical grid before this arithmetic
endpoint estimate is used.  A formal band-edge term

```text
F(t)=c*exp(i*u*t)                                     (4.5)
```

is constant on the grid in (4.1), so its imaginary part has zero
oscillation, while its `D` multiplier `u-y` is zero.  Sweeping `r` changes
the constant phase and detects it.  In (1.1) a possible exact endpoint has
size at most `u*exp(-u/2)`, which is why (4.3), rather than a generic
sampling assertion, disposes of this mode at the transition scale.

If `q` equally spaced offsets are used, their union has mesh

```text
h_u/q=2*pi/(q*u).                                     (4.6)
```

Since the real function `A_u` has frequencies in `[-u,u]`, one offset is
below the Nyquist density, two offsets are at the endpoint density, and
`q>=3` is strict oversampling.  At two offsets an exact frequency `u` still
has the usual Nyquist endpoint ambiguity.  For the sharp arithmetic
polynomial, the distance between `u` and the largest actual frequency can
be only `O(exp(-u))`, so there is no fixed strict-bandwidth margin on which
to base a uniform interpolation claim.  Moreover, samples restricted to a
finite `t`-window do not by themselves supply a global bandlimited
`L^infinity` interpolation theorem.  All offsets avoid those issues by
(4.2), but they only make the same fixed-cutoff data continuous.

In particular, offset variation cannot:

1. directly produce values at a cutoff not already present, without a
   separate inversion in `t`;
2. turn the Cesaro value bound into a stably bounded cutoff derivative; or
3. improve the exponent by a coefficient-free norm transfer from the same
   values.

## 5. Exact cutoff-aperture blindness

Let all available cutoffs lie in `I=[u_-,u_+]`.  At a fixed `t`, cutoff
operations act on a log-frequency `y` through the two kernels

```text
1_(y<=u),                 (u-y)_+,       u in I.      (5.1)
```

Every linear combination, finite difference, or finite signed integral in
`u` of these kernels has the following exact restrictions:

```text
y>u_+ : both responses are zero;
y<u_- : the prefix response is constant in y and the ramp response is
        affine in y.                                  (5.2)
```

Central second differences cancel both the constant and affine pieces, and
therefore have support inside the cutoff aperture; (1.3) is the elementary
example.  No linear cutoff manipulation of the class just described can
manufacture the indicator of a shell lying above `u_+`, or a localized
shell below `u_-`, without additional inversion in the `t` variable.

There is an exact information-theoretic counterexample above the aperture.
Two coefficient measures that agree on `y<=u_+` give identical `A_u,D_u`
for every `u in I`, every real `t`, and every grid offset, while their
complex interval sums on `y>u_+` can differ arbitrarily.  The added measure
can even be nonnegative.  This establishes blindness of the transform class;
it does not claim that the fixed von Mangoldt sequence is adversarial.

For the transition family (1.4),

```text
u_+-u_-=2C*loglog T,
u=log T+O(loglog T),
exp u=T^(1+O(loglog T/log T))=T^(1+o(1)).             (5.3)
```

Thus varying every allowed transition cutoff gives a multiplicative
polylogarithmic family, not a fixed-power family.

## 6. Quantitative comparison with Turan localization

The criterion reproduced at the start of Michel Weber, *Local Suprema of
Dirichlet Polynomials and Zerofree Regions of the Riemann Zeta-Function*,
has the following exact quantifiers.  Fix `D>0`, `0<E<=9/10`, and
`0<beta<1`.  It assumes, for every

```text
T-T^E <=tau<=T+T^E,                                   (6.1)
```

and every

```text
T^[D*(1-beta^(1/6))] <=N<=N_1<N_2<=2N
                    <=T^[D*(1+beta^(1/6))],           (6.2)
```

that

```text
abs sum_(N_1<=p<=N_2) p^(-i*tau)
 <=c*N*(log N)^10/tau^beta.                           (6.3)
```

It concludes that `zeta(s)` is zero-free in

```text
Re(s)>1-beta^2,
T-T^E<=Im(s)<=T+T^E.                                  (6.4)
```

Primary technical reference:
[Weber, arXiv:1005.3932](https://arxiv.org/abs/1005.3932).

The sign in (1.1) is the conjugate of the sign in (6.3), so it makes no
difference to any absolute-value estimate.

The printed logical order is: choose `D>0` and `0<E<=9/10`, then suppose
there exist `T,beta`.  Thus `D,E` precede `T,beta` in that statement.  A
one-height application could nevertheless choose the parameters afresh.
The direct-aperture obstruction below does not depend on this distinction:
it remains valid even if a positive `D=D(T,beta)` is allowed to vary.

Put `b=beta^(1/6)`.  The prime endpoints occurring in (6.2) range, up to
the harmless strict inequalities and factors `2`, from

```text
T^[D*(1-b)] to T^[D*(1+b)].                           (6.5)
```

Their logarithms therefore have center `D*log T` and width

```text
2*D*b*log T+O(1).                                     (6.6)
```

Put

```text
epsilon_T=[C*loglog T+O(1)]/log T.                    (6.7)
```

For the whole endpoint family (6.5) to be reconstructed directly from
cutoffs in (1.4), allowing a fixed `O(1)` log-width for local tent weights,
it is necessary that

```text
D*(1-b)>=1-epsilon_T,
D*(1+b)<=1+epsilon_T.                                 (6.8)
```

Hence

```text
(1-epsilon_T)/(1-b)<=D<=(1+epsilon_T)/(1+b).          (6.9)
```

The interval in (6.9) is nonempty only if

```text
(1-epsilon_T)*(1+b)<=(1+epsilon_T)*(1-b),
b<=epsilon_T.                                        (6.10)
```

This conclusion is independent of whether `D` was fixed in advance.  It
also gives `D=1+O(epsilon_T)`.  Since `b=beta^(1/6)`, it forces

```text
beta<=epsilon_T^6,
beta^2<=epsilon_T^12
       <<_C (loglog T/log T)^12=o(1).                 (6.11)
```

Thus this direct cutoff transfer can reach only a shrinking region, not a
fixed strip.  For fixed `D,b>0`, the simpler width comparison (6.6) already
fails.

All offsets can provide the continuous `tau` quantifier in (6.1), at least
for a local window contained in the sampled height interval, but only under
the supremum-over-offsets quantifier in (4.2a).  They do nothing to (6.6).

## 7. The KMT rate still misses the Turan rate

The obstruction persists even if the KMT theorem is used directly at every
power length, rather than only through the Zeta23 transition cutoff.  Its
sharp principal-character specialization is

```text
Psi(x,t):=sum_(n<=x) Lambda(n)n^(-i*t),

abs Psi(x,t)
 <<x/(log x)^(3/10)+x/(1+abs t),                      (7.1)
```

provided `abs t<=x^[(log x)^(1/25)]`.  Whenever fixed
`0<d_-<d_+` are given, this condition holds uniformly for
`T^d_-<=x<=T^d_+` and `abs t asymp T`, once `T` is large.  In particular it
holds throughout the power band (6.2), for fixed `D,b`.

Primary technical reference:
[Klurman--Mangerel--Teravainen, Lemma 7.9 and Remark 7.2](https://doi.org/10.1112/plms.12546).

Abel summation with `1/log x`, uniformly for
`N<=N_1<N_2<=2N` in any such fixed power band, gives (with the exact
choice of endpoint changing the display by at most one prime-power term)

```text
abs sum_(N_1<=n<=N_2) [Lambda(n)/log n]*n^(-i*t)
 <<_(D,b) N/(log N)^(13/10)+N/[T*log N].              (7.2)
```

Since

```text
sum_n [Lambda(n)/log n]*n^(-i*t)
 =sum_(p^k) (1/k)*p^(-i*k*t),                         (7.3)
```

the prime powers with `k>=2` contribute `O(sqrt N)` absolutely.  Therefore

```text
abs sum_(N_1<=p<=N_2) p^(-i*t)
 <<_(D,b) N/(log N)^(13/10)+N/[T*log N]+sqrt N.       (7.4)
```

The main term in (7.4) implies the required main term in (6.3) only if

```text
T^beta <<(log N)^(10+13/10)=(log N)^(113/10),         (7.5)
```

which is false for every fixed `beta>0`.  This is the rate obstruction in
the unweighted prime normalization used by Turan.

The tent transfer (3.2), fixed finite differences, integration in `u`, and
any other triangle-inequality transfer whose coefficient norm is
`T^o(1)` can change logarithms but cannot change the saving

```text
T^(-o(1)) into T^(-beta) with fixed beta>0.            (7.6)
```

Taking the coefficient-blind cutoff quotient at the exact integer
resolution in (3.8) instead has a power-sized condition number, so that
elementary transfer worsens rather than repairs the exponent.

### Scope of the no-go statement

Sections 3--7 rule out the stated route: coefficient-free reconstruction
from value bounds for `(A_u,D_u)` on the transition cutoffs, using cutoff
integration/differences and grid-offset completion, together with the
currently available KMT estimate.  They do **not** prove that the actual
prime sums in (6.3) are large, or that every multiscale method is impossible.
In particular, the following would be genuinely new inputs rather than
contradictions of this report:

1. a coefficient-specific theorem using inversion in the `t` variable;
2. a Turan localization theorem whose hypotheses are complex smooth tents
   and whose quantitative saving is actually proved;
3. a new fixed-power prime estimate across the whole family (6.2); or
4. a direct constrained Pick-pencil argument exploiting matrix cancellation.

## 8. Final theorem card

The exact disposition is:

```text
PROVED RECONSTRUCTION:
  Continuum cutoff values of A_u and D_u give the complex triangular shell
  (1.3).  The bound transfers with the exact loss
  2*H_A+(4u/Delta)*H_D.  For fixed Delta the two KMT logarithms match and
  yield sqrt(exp u)/u^(3/10), still no fixed power.

PROVED OFFSET EFFECT:
  Every offset turns critical samples into continuous t-data at the same
  cutoff.  A finite number of offsets only changes sampling density and
  leaves the cutoff support unchanged; a direct norm transfer from those
  values supplies no new arithmetic exponent.

PROVED BLINDNESS:
  Cutoff data in [u_-,u_+] vanish identically on frequencies above u_+;
  their cutoff kernels are only constant/affine below u_-.  The real sharp
  prefix is a cutoff derivative; the coefficient-blind exact quotient at
  integer resolution costs N*log N, and the one-atom model proves the
  derivative map is unbounded in the value norm.  Two measures agreeing
  below u_+ are indistinguishable by all cutoffs and offsets but may differ
  arbitrarily above it.

TURAN GATES STILL OPEN:
  (i) complex sharp intervals for every N_1,N_2 in (6.2);
  (ii) a cutoff aperture of fixed width 2D*beta^(1/6)*log T;
  (iii) a fixed T^(-beta) saving, rather than KMT's logarithmic saving.

ZETA23 PICK ROUTE STILL OPEN:
  If one returns to the Loewner matrix rather than Turan localization, the
  scalar prime error must still be o(K) at the actual signed carrier scale.
  Writing K=(X^alpha/L)*r_T, the matched condition remains
  B_X=o(X^alpha*r_T), unless a direct Pick-pencil lower bound proves an
  o(K) error without separating A_X and D_X.
```

Accordingly, varying the current sharp cutoff and lattice origin is a valid
complex-smoothing device, but it neither proves a uniform fixed zero-free
strip nor closes the carrier and prime gates.  This is a no-go theorem for
that transfer mechanism, not for all possible multiscale arithmetic routes.
