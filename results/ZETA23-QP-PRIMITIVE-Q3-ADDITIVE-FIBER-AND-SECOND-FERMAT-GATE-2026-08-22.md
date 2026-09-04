# QP four-cycle: primitive `q^3` additive-fibre and second-Fermat gate

**Date:** 2026-08-22  
**Verdict:** the primitive conductor-`q^3` block has two exact additional
normal forms, but neither gives a new four-cycle exponent.  Primitive
multiplicative projection is exactly additive projection onto frequencies
not divisible by `q`.  For an aligned residual window, its additive
multiplier factors into two Dirichlet kernels and a band of
`asymp q^2/D` unit frequencies has essentially constant height `qD`.  This
band carries a fixed proportion of the entire residual `L^2` mass and a
constant normalized `L^1` mass.  Thus conductor `q^3` does not force high
Archimedean oscillation.

In wild-character coordinates the same block is a family of incomplete
quadratic Postnikov sums of length `D<sqrt(q)`, coupled to the second Fermat
quotient of the shell nodes.  After the legal integer-carrier enlargement
and Poisson summation, the resonant part is precisely the reciprocal outer-fan
sum with frequencies `ell<=q/D`.  The low range `ell<=q/D^2` has total
`L^1` mass `O(q)` trivially; one contiguous tangent-band pair also has the
required bound.  The surviving range is the already identified scattered
outer-fan aggregation problem.

Consequently, neither scalar `q^3` character bounds nor one-variable
`p`-adic stationary phase bypasses the open arithmetic step.  They transform
it into the same high reciprocal-frequency restriction.  No uniform
four-cycle, slope-block, or exponent improvement is claimed here.

---

## 1. Primitive multiplicative projection is an additive fibre difference

Put

```text
M=q^3,
R={r mod M: 0<|r|<=qJ, q does not divide r},       (1.1)
```

where first `J` is an integer with `J<q`; at the project scale `J` is
comparable with `D=q^(16/33)`.  Extend `1_R` by zero from the units to all
residues modulo `M`.

The kernel of reduction

```text
(Z/q^3 Z)^* -> (Z/q^2 Z)^*
```

is `{1+q^2t:t mod q}`.  For a unit `x`, its multiplicative orbit under this
kernel is

```text
x*(1+q^2t)=x+q^2*(x*t),                            (1.2)
```

and `x*t` runs through every residue modulo `q`.  Hence the multiplicative
conditional expectation onto characters factoring modulo `q^2` is exactly
the additive fibre average

```text
E_2 F(x)=q^-1 sum_(t mod q) F(x+t*q^2).            (1.3)
```

It follows that the conductor-`q^3` projection is

```text
P_3 F=(I-E_2)F.                                    (1.4)
```

Additive Fourier transformation modulo `M` diagonalizes (1.3): `E_2`
retains precisely the frequencies divisible by `q`.  Therefore

```text
P_3 1_R(x)
 =M^-1 sum_(h mod M, q does not divide h)
       Rhat(h) e_M(h*x),                           (1.5)

Rhat(h)=sum_(r in R)e_M(-h*r).                    (1.6)
```

This is the pointwise version of the Gauss-sum recombination in the earlier
joint-character audit.  It also proves directly that the primitive matrix is

```text
T_z(a,b)
 =M^-1 sum_(q does not divide h) Rhat(h)
       sum_c z_c e_M(8*h*a*b*c).                  (1.7)
```

Thus the primitive phase is the additive cubic product phase, not a new
reciprocal character phase.

## 2. Exact aligned-window factorisation and a flat primitive band

On the positive half of (1.1), write uniquely

```text
r=q*v+u,        0<=v<J,       1<=u<q.              (2.1)
```

The symmetric Fourier coefficient factors exactly as

```text
Rhat(h)=2 Re(U_h V_h),                             (2.2)

U_h=sum_(u=1)^(q-1)e_(q^3)(-h*u),
V_h=sum_(v=0)^(J-1)e_(q^2)(-h*v).                 (2.3)
```

This is stronger than a generic interval-Fourier upper bound.  Fix a small
absolute `c>0`.  For

```text
1<=h<=c*q^2/J,                                    (2.4)
```

every positive summand in (1.6) lies in an arc of angular length at most
`2*pi*c`.  Taking, for example, `c=1/100` gives

```text
|Rhat(h)| >=2*cos(2*pi/100)*J*(q-1) asymp qJ.      (2.5)
```

There are `asymp q^2/J` such frequencies not divisible by `q`.  Parseval
on the full additive group gives

```text
sum_(h mod q^3)|Rhat(h)|^2
 =q^3*|R| asymp q^4*J.                             (2.6)
```

The unit frequencies in (2.4) alone contribute

```text
(q^2/J)*(qJ)^2 asymp q^4*J,                       (2.7)
```

a fixed proportion of (2.6).  Their normalized `L^1` mass is likewise

```text
q^-3*(q^2/J)*(qJ) asymp 1.                        (2.8)
```

If

```text
K=q^2/J,                                          (2.9)
```

then the main primitive multiplier is therefore a genuinely flat block of
length `K` and coefficient size `1/K`.  It cannot be discarded as a small
high-conductor tail, and taking absolute values over it loses a constant,
not a negative power of `q`.

At `J=D=q^(16/33)`, the exact scale ledger is

```text
qJ:                         q^(49/33),
K=q^2/J:                    q^(50/33),
Rhat(h)/q^3 on the flat band:q^(-50/33),
K*D^3:                      q^(98/33)
                              =(q^3)^(98/99),
entropy deficit:            q^(1/33).              (2.10)
```

The final two lines reproduce the subcritical Fourier-box deficit from the
joint-character audit, now with an exact aligned hard-window lower bound for
the relevant multiplier.

An unaligned endpoint changes (2.2) by at most one incomplete `q`-block.
The exact conductor report already bounds that endpoint where needed.  It
does not alter any scale in (2.5)--(2.10).

## 3. Primitive characters are second-Fermat phases

Every unit modulo `q^3` has a unique Teichmueller decomposition

```text
n=omega(n)*<n>,
omega(n)^(q-1)=1,             <n> in 1+q Z/q^3 Z. (3.1)
```

The truncated logarithm

```text
ell(<n>)=log(<n>)/q mod q^2,
ell(1+q*x)=x-q*x^2/2 mod q^2                       (3.2)
```

is an additive coordinate on the wild unit group.  Thus every character can
be written

```text
chi_(alpha,beta)(n)
 =omega(n)^alpha e_(q^2)(beta*ell(<n>)),           (3.3)

alpha mod q-1,                  beta mod q^2.       (3.4)
```

It has exact conductor `q^3` if and only if `q` does not divide `beta`.

For a shell integer `n<q`, put

```text
Q_2(n)=(n^(q-1)-1)/q mod q^2.                     (3.5)
```

Taking the truncated logarithm of `n^(q-1)` gives the exact identity

```text
ell(<n>)
 =(q-1)^(-1)*(Q_2(n)-q*Q_2(n)^2/2) mod q^2.       (3.6)
```

Thus the wild part of a primitive shell transform samples the **second
Fermat quotient graph**, not merely an ordinary character on `F_q`.

There is also an exact Postnikov formula on each residual `q`-block.  For
`1<=u<q`, `0<=v<J`, and `ubar=u^(-1) mod q^2`,

```text
ell(<u+qv>)-ell(<u>)
 =v*ubar-q*v^2*ubar^2/2 mod q^2.                  (3.7)
```

Consequently the positive residual coefficient of (3.3) is

```text
sum_(u=1)^(q-1) chi(u)
 sum_(v=0)^(J-1)
   e_(q^2)(beta*v*ubar)
   e_q(-beta*v^2*ubar^2/2).                       (3.8)
```

The negative half adds the corresponding parity multiple.  Formula (3.8)
is a coupled family of incomplete quadratic sums of length

```text
J=q^(16/33)<sqrt(q).                               (3.9)
```

There is no uniform one-variable cancellation at this length: short
quadratic phases can be coherent when their least residue is small.  More
importantly, even a scalar bound for every (3.8) would not estimate the
signed matrix box form in the conductor report.  The shell transforms in
that box contain the correlated coordinates (3.6).

For comparison, the ordinary first-Fermat-quotient problem is already a
delicate short-sum problem; see Shparlinski,
[*Fermat quotients: exponential sums, value set and primitive roots*](https://arxiv.org/abs/1104.3909).
That paper does not supply the weighted second-quotient matrix restriction
needed here.

## 4. Poisson resonance gives the reciprocal outer-fan gate

The additive cubic block and the reciprocal Selberg block are two Fourier
views of the same carrier condition.  Let `W` be a smooth compactly
supported function and, temporarily, enlarge the carrier to all integers.
For fixed shell-scale `a,c`, Poisson summation gives exactly

```text
sum_(b in Z) W((8*a*c*b-q^3)/(qJ))
 =qJ/(8*a*c) sum_(ell in Z)
    What(ell*qJ/(8*a*c))
    e(-ell*q^3/(8*a*c)).                           (4.1)
```

Since `a*c asymp q^2`, the effective reciprocal frequency range is

```text
|ell| <=q/J.                                      (4.2)
```

For a hard interval, the Selberg polynomial gives the same finite range up
to harmless endpoint weights.  Summing (4.1) over the two slope-block
projections produces exactly the reciprocal phases

```text
S_ell(A,C)=sum_(a in A,c in C)
             e(ell*q^3/(8*a*c)).                  (4.3)
```

The connection to (1.7) is also visible by stationary frequency matching.
Summation in `b` makes an additive residual frequency `h` resonant only when

```text
8*h*a*c/q^3 is close to the integer ell,
h is close to ell*q^3/(8*a*c).                    (4.4)
```

The flat cutoff `h<=q^2/J` from Section 2 maps under (4.4) to
`ell<=q/J`, exactly (4.2).  Hence a one-variable `q`-adic stationary-phase
analysis of the primitive block lands on the reciprocal frequency family;
it does not remove it.

At the active scale, the initial reciprocal band is already harmless:

```text
sum_(1<=ell<=q/J^2)|S_ell|
 <=(q/J^2)*J^2=q.                                  (4.5)
```

This is exactly the `L^1` size required by the slope-block theorem.  The
remaining range is

```text
q/J^2 < ell <=q/J,
q^(1/33)<ell<=q^(17/33).                           (4.6)
```

On one contiguous tangent-band pair, two-dimensional stationary phase gives
`|S_ell|<<q^(1+o(1))/ell`, whose `L^1` sum is also admissible.  What is not
proved is lossless aggregation over the many separated affine/Farey bands
of two complete modular strips.  Taking absolute values band by band pays
the known fan multiplicity; an unclassified second moment is defeated by
the coherent modes in (4.5).

Thus the primitive-conductor problem, after its natural stationary-phase
step, is the existing scattered outer-fan problem rather than an independent
character-sum problem.

## 5. Exact conclusion

```text
primitive multiplicative projection = I-E_(mod q^2):  PROVED;
primitive block = additive unit-frequency block:       PROVED;
aligned residual Fourier factorisation:                PROVED;
flat unit band of length q^2/D and height qD:           PROVED;
flat band carries constant residual L2 and L1 mass:     PROVED;
wild coordinate = corrected second Fermat quotient:    PROVED;
q-block Postnikov quadratic formula:                   PROVED;
Poisson resonance -> reciprocal modes ell<=q/D:        PROVED;
low reciprocal modes ell<=q/D^2:                       O(q), PROVED;
one contiguous tangent-band pair:                      CLOSED PREVIOUSLY;
scattered high-frequency outer-fan aggregation:        OPEN;
primitive Schatten-four restriction:                   OPEN;
new four-cycle exponent:                               NONE;
uniform four-cycle bound:                              NOT PROVED.
```

Finite identities and exponent arithmetic are replayed by

```text
src/qp_primitive_q3_additive_fiber_gate.py
src/test_qp_primitive_q3_additive_fiber_gate.py
```

with

```bash
PYTHONPATH=src pytest -q \
  src/test_qp_primitive_q3_additive_fiber_gate.py
```
