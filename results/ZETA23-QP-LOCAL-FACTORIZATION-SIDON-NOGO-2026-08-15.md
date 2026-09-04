# QP local-factorization gate: interval-positive Sidon antennas

**Date:** 2026-08-15  
**Verdict:** windowed local positivity does **not** force an approximate
additive progression, a repeated-difference clique, or a finite
Fejer--Riesz factor inside the active node set.  At the exact QP exponent
scale there are rigorous interval-positive antennas whose nonzero
coefficient support is `1/B`-Sidon.  Consequently a local PSD/factorization
argument cannot by itself turn a large Delsarte antenna into additive
structure that the prime-power logarithms could then contradict.

The first counterexample uses generic nodes in the same fixed logarithmic
shell.  A strengthened version puts every node on the exact logarithmic
lattice `log(n/Y)` with integral `n`.  Neither version restricts `n` to a
prime power, so they do **not** prove or disprove actual-node QP.  Their
precise conclusion is that the missing von Mangoldt-support input has to
enter a sign-sensitive Fourier estimate; it cannot be postponed until after
a support-only local factorization theorem.

---

## 1. The proposed inverse statement

At the active slice put

```text
T0=Y^.01,             B=Y^(50/33),
Q(t)=1+sum_(u in V) lambda_u cos(tu).                (1.1)
```

The hoped-for route was

```text
Q>=0 on [T0,B] and Q(0)>=Y^c
   => a large approximate AP/difference clique in supp(lambda),
   => contradiction from the arithmetic of u=log(n/Y).          (1.2)
```

Here `c=.019` is the convenient fixed-power target.  The first implication
in (1.2) is false even when every `lambda_u` is positive.

---

## 2. A fixed-power interval-positive Sidon theorem

Fix a compact interval `I` strictly inside `(w/2,w)` and a nonnegative
`C_c^infinity(I)` probability density `rho`.  Write

```text
A=50/33,       tau=.01,
H_Y=[Y^tau,Y^A].                                      (2.1)
```

### Theorem 2.1 (local-positive Sidon antenna)

Let `c>0` and choose an exponent `eta` satisfying

```text
2c<eta<A/4.                                           (2.2)
```

For every sufficiently large `Y` there are

```text
K=floor(Y^eta)
```

distinct nodes `u_1,...,u_K in I` and a number

```text
L_Y << sqrt(K log Y)                                  (2.3)
```

such that

```text
sup_(t in H_Y) |sum_(j<=K) cos(tu_j)| <= L_Y,          (2.4)
```

and the active set is `1/B`-Sidon:

```text
|u_i+u_j-u_k-u_l|<=1/B
       => {i,j}={k,l} as multisets.                   (2.5)
```

The nodes may additionally be chosen linearly independent over the
rationals; this has probability one under the same continuous sampling.

Therefore

```text
Q_Y(t)=1+L_Y^(-1) sum_(j<=K) cos(tu_j)                (2.6)
```

satisfies

```text
Q_Y(t)>=0                  for every t in H_Y,
Q_Y(0)=1+K/L_Y
      >=Y^(eta/2-o(1))>Y^c.                          (2.7)
```

In particular, its coefficient-carrying nodes contain no nontrivial
`1/B` approximate three-term AP and no repeated nonzero difference at that
resolution.  Since `I subset (w/2,w)`, no positive difference of two active
nodes is itself an active node either.

For the audited numbers one may take

```text
c=.019,       eta=.04,       A=50/33.                 (2.8)
```

Then `eta/2=.020>.019`, while

```text
K^4/B=Y^(.16-50/33)=o(1).                             (2.9)
```

Thus the example clears the required antenna power while being much more
additively sparse than any prospective AP obstruction.

### Proof

Sample the `u_j` independently with density `rho`, and put

```text
S_K(t)=sum_j cos(tu_j),
m(t)=integral rho(u)cos(tu)du.                        (2.10)
```

Repeated integration by parts gives, for every fixed integer `N`,

```text
|m(t)|<=C_N(1+|t|)^(-N).                             (2.11)
```

At a fixed `t`, Hoeffding's inequality bounds
`S_K(t)-K m(t)` by `O(sqrt(K log Y))` with polynomially small failure
probability.  Both the sampled sum and its mean have derivative at most
`wK`.  A grid of spacing `(4wK)^(-1)` therefore transfers the fixed-point
bound to all of `H_Y`; the grid has `O(BK)` points.  The union bound yields

```text
sup_(t in H_Y)|S_K(t)-K m(t)|
       <<sqrt(K log(BK)).                             (2.12)
```

Choose `N` so that

```text
eta-N tau<eta/2.                                     (2.13)
```

Equations (2.11)--(2.13) prove (2.3)--(2.4) with
probability tending to one.

For every nontrivial ordered quadruple `(i,j,k,l)`, the random variable
`u_i+u_j-u_k-u_l`, after canceling indices common to both sides, has a
bounded density near zero.  Hence

```text
Pr(|u_i+u_j-u_k-u_l|<=1/B)<<1/B.                     (2.14)
```

There are `O(K^4)` quadruples.  By (2.2), `K^4/B=o(1)`, so with probability
tending to one none of the nontrivial events (2.14) occurs.  The flatness
and Sidon events therefore occur simultaneously.  The countable union of
nontrivial rational hyperplanes has probability zero, which supplies the
optional rational independence.  Equations (2.6)--(2.7) finish the proof.
QED

The same proof permits a fixed multiple of `1/B`, or any resolution
`Y^o(1)/B` while `K^4Y^o(1)/B=o(1)`.

### Theorem 2.2 (the nodes can lie on the integral logarithmic lattice)

The conclusion of Theorem 2.1 remains true with

```text
u_j=log(n_j/Y),       n_j integral,                  (2.15)
```

provided `I subset (w/2,w)`,

```text
2c<eta<min(1/4,2-A),                                  (2.16)
```

and `B=Y^A` with `1<A<2`.  In particular, the active numerical choice
`c=.019`, `eta=.04`, `A=50/33` is legal.

#### Proof

Choose a nonnegative smooth weight `a` compactly supported in `exp(I)` and
sample each integer `n` with probability proportional to `a(n/Y)`.  If

```text
m_Y(t)=
 [sum_n a(n/Y)exp(it log(n/Y))]/[sum_n a(n/Y)],       (2.17)
```

then smooth Poisson summation, with no nonzero stationary mode for
`1<=t<=Y`, gives for every fixed `N`

```text
|m_Y(t)|<<_N t^(-N)+Y^(-N),          1<=t<=Y.         (2.18)
```

For `Y<=t<=Y^A`, the van der Corput second-derivative estimate applied to
`t log n` gives

```text
|m_Y(t)| << sqrt(t)/Y+1/sqrt(t).                      (2.19)
```

Indeed `|(t log x)''| asyp t/Y^2` throughout the shell, so the unnormalized
sum is `O(sqrt(t)+Y/sqrt(t))`; smooth partial summation preserves this
bound.  Equations (2.18)--(2.19) imply

```text
sup_(t in H_Y) K|m_Y(t)|=o(sqrt(K))                   (2.20)
```

after choosing `N` with `eta-N tau<eta/2`, because

```text
eta+A/2-1 < eta/2                                    (2.21)
```

is equivalent to the second upper bound in (2.16).  Hoeffding plus the same
derivative grid now proves (2.4).

The discrete sampling law has largest atom `O(1/Y)`.  Conditional on three
entries of a nontrivial additive quadruple of logarithms, the fourth integer
must lie in an interval of length

```text
O(Y/B)=o(1).                                          (2.22)
```

There are therefore `O(1)` possible fourth integers, and the conditional
probability is `O(1/Y)`.  The union bound is now

```text
O(K^4/Y)=O(Y^(4eta-1))=o(1),                          (2.23)
```

by (2.16).  Repeated sampled integers themselves have probability
`O(K^2/Y)=o(1)`.  Thus flatness, distinctness, and the `1/B`-Sidon property
again occur simultaneously.  QED

This integral version shows that neither the logarithmic change of
variables, shell width, integrality, nor elementary multiplicative
separation can supply the inverse implication (1.2).  The prime-power
support is the indispensable unresolved feature.

---

## 3. Why windowed Fejer--Riesz loses the discrete support

Let `chi>=0` be supported in `H_Y`.  Local positivity gives the PSD kernel

```text
K_chi(x,y)=integral chi(t)Q_Y(t)exp(i(x-y)t)dt.       (3.1)
```

Writing `h=sqrt(chi Q_Y)`, (3.1) is a Gram kernel, and on the Fourier side
`widehat(chi Q_Y)` is the autocorrelation of `hat h`.  This is the valid
local analogue of factorization.

It does not factor the finite polynomial with a factor supported on a
subset of the original nodes.  Time windowing convolves every spectral atom
with `hat chi`, while `hat h` has continuous, generally full support.  Thus
the differences in the Gram factor live in a continuum and need not be
differences of nodes in `supp(lambda)`.  Theorem 2.1 makes this loss
unavoidable rather than technical: the original active support has no
nontrivial approximate difference collision at the window resolution, yet
the local Gram factor exists and the antenna is polynomially large.

There is also an exact analytic obstruction to any finite exponential-
polynomial square on the interval.  Use the optional rationally independent
nodes in Theorem 2.1.  Kronecker's theorem gives ordinates at which every
`cos(tu_j)` is arbitrarily close to `-1`.  Since `K/L_Y` tends to infinity,
`Q_Y` is negative at some such ordinate.  If an identity

```text
Q_Y(t)=|R(t)|^2                                      (3.2)
```

with a finite exponential polynomial `R` held on any open interval, real
analytic continuation would make it hold on the whole line, contradicting
that negative value.  Thus local positivity does not merely fail to reveal
the correct discrete factor: in this example no finite discrete square
exists even locally as an identity.

Global positivity is different.  A globally nonnegative periodic
trigonometric polynomial has a discrete Fejer--Riesz square, and generalized
frequencies face strong Bohr-torus constraints.  Those theorems cannot be
applied after replacing positivity on `[T0,B]` by positivity on the whole
line.  The gap before `T0` is exactly what permits (2.6).

---

## 4. Many-island and coefficient stress tests

The construction is not a hidden perturbed Fejer progression.

1. **Positive coefficients.**  Every active coefficient in (2.6) is the
   same positive number.  Signed cancellation among coefficients is not
   being used.
2. **No approximate additive carrier.**  Equation (2.5) rules out even one
   nontrivial repeated difference at scale `1/B`, hence rules out every AP
   based on repeated active differences.  The choice `I subset (w/2,w)`
   also makes every positive active-node difference lie strictly below the
   active support, so there is no internal difference-closure clique.
3. **Uniform continuum, not a grid artifact.**  The derivative grid in the
   proof controls every real `t` in the complete band.
4. **Many-island mechanism.**  Flatness comes from the square-root empirical
   cancellation of `K` independent carriers over `O(BK)` effective sample
   points.  The large value at zero is the `ell^1/ell^2` gain
   `K/sqrt(K log Y)`, not a discrete square.
5. **Coefficient-sensitive inverse statements.**  Since all coefficients
   are equal and nonzero, weighting an alleged structural conclusion by
   coefficient mass does not repair (1.2).

A conclusion about some additive quadruple in the *ambient* node set, with
no coefficient mass on it, would not be contradicted.  It would also be
irrelevant to the dual polynomial: a dense shell has such quadruples by
pigeonhole regardless of `Q`.  The only useful inverse theorem would have
to see the active coefficient mass, and Theorem 2.1 rules out that form.

---

## 5. Exact scope for the actual prime-power problem

The theorems do not place their integral nodes at

```text
u=|log(p^k/Y)|.                                       (5.1)
```

Replacing the smooth all-integer expectation in (2.17) by a positive
measure supported only on (5.1) asks precisely for a uniform small lower
Fourier tail on the actual nodes.  That is the live QP estimate, not a
consequence of local factorization.  Nor does elementary multiplicative
separation help after Theorems 2.1--2.2: absence of additive relations is
compatible with, rather than hostile to, a large interval-positive antenna.

The surviving options are therefore narrower:

```text
windowed PSD => active approximate AP/difference clique:       FALSE;
local Fejer--Riesz preserving the prescribed node support:     FALSE;
fixed-power interval antenna on a 1/B-Sidon shell support:      EXISTS;
same with every node u=log(n/Y), n integral:                    EXISTS;
the same construction on actual prime-power nodes:             OPEN;
actual-prime coefficient-sensitive Fourier cancellation:       REQUIRED;
fixed-power QP, QP <=> strip, or a uniform strip:               NOT PROVED.
```

Executable exponent replay:

- `src/qp_local_factorization_sidon_nogo.py`;
- `src/test_qp_local_factorization_sidon_nogo.py`.
