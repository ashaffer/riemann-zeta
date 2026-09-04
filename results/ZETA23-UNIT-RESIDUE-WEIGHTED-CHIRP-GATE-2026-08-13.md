# Unit-residue extensions pay a square-root termwise chirp bill

**Date:** 2026-08-13

**Verdict:** parity, Ramanujan, principal-character, and finite Selberg/
divisibility aliases cannot produce a cheap prime-log design when their
additive harmonics are lifted separately to logarithmic chirps.  Every
periodic extension which is one on all reduced residues and has no constant
mode pays at least

```text
sqrt(Y/2)
```

in the natural stationary-phase weighted coefficient bill.  The bound is
sharp when the modulus is even: the parity alias attains it.

This is **not** a lower bound for the Wiener norm of the combined Mellin
transform after cancellation among overlapping stationary branches.  Such a
cancellation theorem would be a new full-aperture prime-log extremal, not a
consequence of the result below.  No subpower design, zeta bound, or
zero-free strip is proved.

## 1. The weighted extension problem

Write `e_q(x)=exp(2*pi*i*x/q)`.  Let

```text
g(x)=sum_(a mod q) d_a e_q(a*x),
g(r)=1                         ((r,q)=1).
```

For each nonzero residue `a mod q`, let `a_tilde` be its least signed lift,
chosen in `(-q/2,q/2]`, and put

```text
r_a=abs(a_tilde)=min(a_0,q-a_0),
L_a=Y*r_a/q.
```

Here `a_0 in {1,...,q-1}` is the canonical positive representative.  Thus
`r_a` is attached unambiguously to the residue class, not to an arbitrary
integer representative.  The lift `a_tilde` is the cheapest additive chirp
which has the prescribed values at integer arguments.

After a fixed smooth localization in `u`, lift this residue by `a_tilde`.
The additive harmonic
`exp(2*pi*i*a_tilde*Y*exp(u)/q)` has logarithmic Wiener norm comparable with
`sqrt(L_a)` when `L_a>=1`, by uniform one-dimensional stationary phase.
The absolute, termwise DFT-to-chirp bill is therefore

```text
W_Y(g)=sum_(a!=0)|d_a|*sqrt(Y*r_a/q).                 (1.1)
```

The constant coefficient `d_0` is the zero-frequency carrier.  For a pure
high-frequency representation it is zero.

## 2. Exact Ramanujan-dual theorem

### Theorem 2.1 (weighted unit-extension lower bound)

For every integer `q>=2` and every complex trigonometric polynomial above,

```text
W_Y(g) >=sqrt(Y/2)*abs(1-d_0).                        (2.1)
```

In particular, if `d_0=0`, then `W_Y(g)>=sqrt(Y/2)` independently of `q`.
If `q` is even, the constant is sharp.

### Proof

Sum the interpolation equations over the reduced residue system `U_q`.
With the Ramanujan sum

```text
c_q(a)=sum_(r in U_q)e_q(a*r),
```

one obtains

```text
phi(q)*(1-d_0)=sum_(a!=0)d_a*c_q(a).                  (2.2)
```

Put `m=q/gcd(a,q)`.  Holder's formula says

```text
c_q(a)=mu(m)*phi(q)/phi(m).                           (2.3)
```

Thus the term vanishes unless `m` is squarefree.  Using the canonical
positive representative `a_0` and writing
`a_0=gcd(a_0,q)*k`, with `(k,m)=1`, also gives

```text
r_a/q=min(k,m-k)/m >=1/m.                             (2.4)
```

For squarefree `m>=2`,

```text
sqrt(m)/phi(m)<=sqrt(2).                              (2.5)
```

Indeed, `p-1>=sqrt(p)` for every odd prime `p`, while the prime `2`
contributes exactly the extra factor `sqrt(2)`.  Equations (2.3)--(2.5)
give

```text
abs(c_q(a))
 <=sqrt(2)*phi(q)*sqrt(r_a/q).                        (2.6)
```

Apply the triangle inequality to (2.2) and multiply by `sqrt(Y)`.  This is
(2.1).

When `2|q`, all units are odd, so

```text
g(r)=-e_q((q/2)*r)
```

equals one on `U_q`, has `d_0=0`, and has
`W_Y(g)=sqrt(Y/2)`.  Hence equality is attained.  QED

## 3. Consequences for the proposed aliases

1. Taking `q=Y^(.9639...)` does not reduce the termwise bill to
   `Y^(.018...)`.  Although the first additive harmonic has stationary
   scale `Y/q`, the unit equations force weighted mass at remote residue
   frequencies.  Their aggregate bill is at least `Y^(1/2)/sqrt(2)`.

2. The centered principal-character extension is not special.  Theorem 2.1
   optimizes over **all** choices of the values on nonunits and all Fourier
   coefficients.  Primorial preprocessing therefore cannot improve this
   termwise power.

3. A finite Selberg/divisibility construction is periodic modulo the lcm of
   its moduli and is constant on the units of that lcm.  After removing its
   constant mode, the same theorem applies.  The optimized absolute lift is
   again parity at square-root scale.

4. The theorem imposes interpolation only at integers coprime to `q`.
   Active prime powers whose base divides `q` are outside its conclusion.
   No bound for the cost of correcting those exceptional coordinates is
   asserted here.

The apparent aperture transition near `B=Y` has a separate explanation.
For an exact correction block of length `L`, integer-log separation gives
an off-diagonal Gram row sum `O(Y log M/L)`.  Stable correction begins at
`L>>Y log M`; this is a frame/Nyquist transition, not an early scalar return
of the prime-log orbit.

## 4. Exact-cosine realization and the surviving loophole

A one-sided congruence alias is not even in `u`.  It can nevertheless be
made into an exact real-even alias in the pure high-frequency case `d_0=0`.
Starting from the residue coefficients `d_a`, choose the canonical positive
lifts `a_0 in {1,...,q-1}` and set

```text
g_+(x)=sum_(a!=0)d_a*exp(2*pi*i*a_0*x/q).
```

This chosen continuous extension agrees with the discrete extension at
every integer.  Its absolute termwise chirp bill is

```text
sum_(a!=0)|d_a|*sqrt(Y*a_0/q) >=W_Y(g),               (4.0)
```

because `a_0>=r_a`.  Thus using all-positive lifts to control the product
phase cannot evade Theorem 2.1.  Put

```text
A(u)=g_+(Y*exp(u)),
B(u)=conj(g_+(Y*exp(-u))),
F(u)=Re[A(u)+B(u)-A(u)B(u)].                           (4.1)
```

Then `F(-u)=F(u)`.  At an active node `u_n=log(n/Y)`, one has
`A(u_n)=g_+(n)=g(n)=1`; at its reflected point,
`B(-u_n)=conj(g_+(n))=1`.
Consequently `F(u_n)=F(-u_n)=1` whenever `n` is coprime to `q`.  Product
phases have the form

```text
(2*pi*Y/q)*(a*exp(u)-b*exp(-u)),
```

whose first derivative is positive.  Thus the standard opposite-orientation
completion does not create a zero-frequency stationary branch.

Theorem 2.1 still kills the construction when (4.1) is synthesized by
lifting its additive harmonics separately.  It does **not** exclude a
purpose-built choice of the `d_a` for which the overlapping Mellin
stationary contributions cancel before the Wiener norm is taken.  In
symbols,

```text
sum_a ||individual lifted harmonic||_A
```

is controlled here, whereas the true extremal contains

```text
||sum_a individual lifted harmonic||_A.               (4.2)
```

Passing from the first line to the second is exactly the unresolved
cross-harmonic/full-aperture cancellation problem.  Nor does the theorem
cover an atomic design that is tailored only to the actual prime residues
rather than to every member of `U_q`.

Consequently the result closes the explicit parity/Ramanujan/principal-
character/Selberg family under its natural absolute lift, but not arbitrary
nonlinear supports or the actual-prime atomic extremal `C_(T,B)`.

## 5. Relation to prior Fourier-algebra results

The classical Littlewood theorem of McGehee--Pigno--Smith and Konyagin gives
logarithmic lower bounds for unweighted `L^1` norms of exponential sums.
Green--Konyagin and Sanders prove polylogarithmic finite-cyclic Fourier-
algebra lower bounds for dense sets.  Cohen--Host idempotent theorems are
qualitative coset-ring classifications.  None of those results includes the
stationary chirp weight in (1.1).  Theorem 2.1 is instead an elementary,
directional Ramanujan-sum dual tailored to this weight.

Primary references:

- O. C. McGehee, L. Pigno, B. Smith, *Hardy's inequality and the
  `L^1`-norm of exponential sums*, Annals of Mathematics 113 (1981);
- B. Green, S. Konyagin, *On the Littlewood problem modulo a prime*,
  arXiv:math/0601565;
- T. Sanders, *The Littlewood--Gowers problem*, arXiv:math/0605522.

## 6. Replay

```bash
python3 results/unit_residue_weighted_chirp_audit.py --q-max 5000
```

The script verifies Holder's formula directly, searches the sharp ratio in
(2.6), identifies `m=2` as the extremizer, and checks the parity equality.
