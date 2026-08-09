# R99 positive matrix-renewal and bosonic determinant gate

Status: exact operator-valued recurrence theorem, positive Fredholm
determinant/bosonic-Fock theorem, eta and two-carrier coefficient
obstructions, continuous-delay audit, noncommuting-cycle reality check, and
exterior-power/Schur-complement ledger.  A genuinely continuous renewal law
can remove the fake endpoint recurrences, but no positive finite-, infinite-,
or noncommuting operator kernel can then retain either eta carrier as its
characteristic determinant.  Its reciprocal would have to be a positive
Laplace transform, while the actual reciprocal has a negative atom at every
untouched prime.  No fixed zeta zero-free strip, and no theorem ruling out
all fixed strips, is proved here.

Date: 2026-08-07.

## 1. Verdict

The matrix-renewal proposal has two logically different jobs:

```text
(A) divide out the pole-killing endpoint factor;
(B) prove that the remaining eta/zeta-bearing numerator is nonzero.       (1.1)
```

Positive renewal can perform (A).  It does not perform (B).

For example, with `z=s-1` and `lambda>0`, the continuous exponential delay
law has transform and characteristic determinant

```text
Phi(z)=lambda/(lambda+z),
d(z)=1-Phi(z)=z/(lambda+z).                              (1.2)
```

The only zero of `d` is the required endpoint `z=0`; there are no recurrent
fake zeros near the imaginary axis.  Thus passing from discrete logarithmic
delays to a genuinely continuous nonlattice law really does repair the
denominator defect found in R91--R92.

The repair cannot be attached to the numerator while keeping positivity.
The central new theorem is the following.

**Positive determinant theorem.**  Let

```text
K(s)=integral_[0,infinity) exp(-su) dM(u)                 (1.3)
```

be the Laplace transform of a positive operator-valued measure on a Hilbert
space.  Suppose `K(sigma)` is trace class and

```text
0 <= K(sigma) < I.                                       (1.4)
```

Then

```text
D(sigma)=det(I-K(sigma)),
1/D(sigma)=sum_(m>=0) Tr_(Sym^m H)(K(sigma)^(tensor m))  (1.5)
```

and `1/D(sigma)` is the Laplace transform of a positive scalar measure.
This remains true when the positive increments of `M` do not commute.  It
also has the usual complex contraction consequence

```text
norm K(sigma+it) <= norm K(sigma).                       (1.6)
```

Now put

```text
E_q(s)=(1-q^(1-s))zeta(s).                               (1.7)
```

In `Re(s)>1`, its reciprocal has the absolutely convergent Dirichlet series

```text
1/E_q(s)
 = [sum_(j>=0) q^j (q^j)^(-s)]
   [sum_(n>=1) mu(n)n^(-s)].                             (1.8)
```

At every prime `p!=q`, the coefficient of `p^(-s)` in (1.8) is exactly

```text
mu(p)=-1.                                                (1.9)
```

Uniqueness of the Laplace transform says that (1.8) cannot also be the
transform of a positive measure.  Therefore neither `E_2` nor `E_3` can be
`det(I-K)` for any positive operator-valued renewal kernel satisfying the
contraction hypothesis, even only in the already-convergent half-plane
`Re(s)>1`.  This rules out finite matrices, trace-class infinite matrices,
continuous state spaces, and noncommuting Loewner-positive increments at
once.

The signed two-carrier detector from R92 has the same obstruction after its
natural normalization:

```text
-2^(s-1)[E_2(s)-E_3(s)]
  =[1-(3/2)^(1-s)]zeta(s).                              (1.10)
```

At every prime `p!=3`, the generalized Dirichlet coefficient of the
reciprocal at exponent `log p` is again `-1`.

There is a complementary discrete obstruction.  If an arithmetic
operator pencil

```text
K(s)=sum_(n>=2) A_n n^(-s)                              (1.11)
```

converges normally in trace norm across `Re(s)=1`, then every zero of
`det(I-K(s))` at `s=1` recurs at zeros

```text
s_j=1+i tau_j+o(1),             tau_j -> infinity.      (1.12)
```

Noncommutativity does not affect the proof.  Thus an arithmetic endpoint
Perron mode has the old recurrent fake-zero problem; a continuous endpoint
mode avoids that problem but fails the bosonic prime-atom test when one
tries to attach zeta.

This is a sharp fork, not a proof about the location of zeta zeros.  To
escape it, a proposed operator must either cease to be positive at the
measure level, place prime-specific atoms into the purported counterterm,
or use a signed Schur/exterior projection.  Those are precisely the three
places where the desired zeta information has been reintroduced rather
than proved nonzero.

## 2. Positive operator renewal gives complex contraction

Let `M` be a positive operator-valued Borel measure on `[0,infinity)`.  For
a real `sigma` at which the integral is bounded, weight the measure by
`exp(-sigma u)` and call the result `M_sigma`.  The operator Fourier
transform is

```text
K(sigma+it)=integral exp(-itu)dM_sigma(u).              (2.1)
```

Naimark dilation gives a Hilbert space `G`, a spectral measure `P`, and an
operator `V:H->G` such that

```text
M_sigma(B)=V^*P(B)V,
K(sigma)=V^*V,
K(sigma+it)=V^*U_tV,                                    (2.2)
```

where `U_t=integral exp(-itu)dP(u)` is unitary.  Consequently

```text
norm K(sigma+it)
 <= norm(V)^2
 = norm K(sigma).                                       (2.3)
```

The same estimate follows directly from Cauchy--Schwarz for positive
operator measures.  In particular,

**Theorem 2.1 (positive renewal contraction).**  If for some `a`

```text
norm K(sigma)<1                 for every sigma>a,       (2.4)
```

then

```text
I-K(s) is invertible             throughout Re(s)>a.     (2.5)
```

This is the hoped-for fixed-strip mechanism in its honest abstract form.
The issue is not the operator theorem.  The issue is realizing an
eta/zeta-bearing determinant under its hypotheses.

For entrywise nonnegative kernels on a Banach lattice, (2.3) has the
standard domination form

```text
abs(K(sigma+it)f) <= K(sigma)abs(f),                    (2.6)
```

so the same conclusion follows from the Perron radius.  Thus both the
Loewner-positive and the classical Perron--Frobenius meanings of
"positive kernel" are covered.

## 3. The bosonic reciprocal theorem

Assume now that `K(sigma)` is positive trace class with norm less than one.
If its eigenvalues are `(lambda_j)`, then

```text
1/det(I-K(sigma))
 =product_j (1-lambda_j)^(-1)
 =sum_(m>=0) Tr_(Sym^m H)(K(sigma)^(tensor m)).          (3.1)
```

This is the grand partition function on bosonic Fock space

```text
F_+(H)=direct_sum_(m>=0) Sym^m H.                       (3.2)
```

Substitute the operator-valued Laplace integral into the `m`-th summand:

```text
K(sigma)^(tensor m)
 =integral exp[-sigma(u_1+...+u_m)]
    dM(u_1) tensor ... tensor dM(u_m).                  (3.3)
```

Every tensor product in (3.3) is positive.  Compression to `Sym^m H` and
then taking the trace gives a positive scalar measure in the total delay
`u_1+...+u_m`.  The sum over `m` is finite after Laplace weighting because
of (3.1).  Hence:

**Theorem 3.1 (bosonic determinant positivity).**  Under (1.3)--(1.4),
there is a positive scalar measure `nu` such that

```text
1/det(I-K(sigma))
 =integral_[0,infinity) exp(-sigma u)dnu(u).            (3.4)
```

Equivalently, the reciprocal determinant is completely monotone on every
real interval on which the hypotheses hold.

No commutativity of the increments `dM(u)` was used.  They occur on
different tensor factors in (3.3), which is the reason the conclusion
survives genuinely noncommuting positive increments.

For entrywise nonnegative trace-class kernels, an alternative proof expands
the reciprocal determinant as the positive generating function of multisets
of directed cycles.  The bosonic proof is stronger because it also covers
Loewner positivity, where individual ordered cycle traces need not be
positive.

## 4. Exact eta and zeta coefficient obstruction

For `Re(s)>1`,

```text
1/zeta(s)=sum_(n>=1)mu(n)n^(-s),                        (4.1)

1/[1-q^(1-s)]
 =sum_(j>=0)q^j(q^j)^(-s).                              (4.2)
```

Multiplication proves (1.8).  If `p` is prime and `p!=q`, the only
factorization `p=q^j n` has `j=0,n=p`.  Therefore the coefficient is
`mu(p)=-1`.

Suppose (contrary to the claim) that

```text
E_q(s)=det(I-K(s))             for real s>1             (4.3)
```

with `K` satisfying Theorem 3.1.  Equation (3.4) gives a positive inverse
Laplace measure for `1/E_q`.  Equation (1.8) gives a signed atomic inverse
Laplace measure with mass `-1` at `log p`.

To invoke uniqueness without any distributional convention, fix
`sigma_1>1` and weight both measures by `exp(-sigma_1 u)`.  They become
finite measures whose Laplace transforms agree on a real interval.
Uniqueness for finite Laplace transforms makes the measures equal.  A
positive measure cannot have mass `-p^(-sigma_1)` at the singleton
`{log p}`.  This contradiction proves:

**Theorem 4.1 (eta is not a positive characteristic determinant).**  For
every integer `q>=2`, there is no positive operator-valued renewal kernel
with `0<=K(sigma)<I` and

```text
det(I-K(s))=E_q(s)                in Re(s)>1.            (4.4)
```

The conclusion already holds on the real axis and therefore cannot be
repaired by an analytic continuation to a left strip.

The direct determinant coefficient gives a shorter arithmetic version.
If

```text
K(s)=sum_(n>=2)A_n n^(-s),       A_n>=0,                (4.5)
```

then the coefficient of `p^(-s)` in `det(I-K(s))` is

```text
-Tr(A_p)<=0.                                             (4.6)
```

All exterior-power terms of degree at least two have multiplicative index
`n_1...n_r`, which cannot be prime.  But the coefficient of `p^(-s)` in
`E_q` is `+1` for `p!=q`.  This proves (4.4) in the arithmetic case without
forming the reciprocal.

The bosonic proof is what closes the more ambitious continuous-state and
noncommuting versions.

### 4.1 Positive scalarizations also fail

Normalize a positive combination of the two carriers by its limit at
infinity:

```text
D(s)=[c_2 E_2(s)+c_3 E_3(s)]/(c_2+c_3)
    =[1-alpha 2^(1-s)-beta 3^(1-s)]zeta(s),             (4.7)

alpha,beta>0,       alpha+beta=1.                       (4.8)
```

The reciprocal of the bracket in (4.7) has an absolutely convergent
geometric expansion supported on the multiplicative semigroup generated by
`2` and `3`.  At every prime `p>=5`, multiplication by `1/zeta` again leaves
the coefficient `-1`.  Hence no positive scalarization is a positive
characteristic determinant either.  This is independent of the recurrent
artificial zeros already proved in R91.

### 4.2 The signed two-carrier determinant also fails positivity

R92 found the exact zeta detector

```text
E_2-E_3=(3^(1-s)-2^(1-s))zeta(s).                       (4.9)
```

Normalize its high-real-part limit as in (1.10).  The inverse local factor
is the geometric series in `(3/2)^(1-s)`.  For a prime `p!=3`, an equality

```text
p=(3/2)^j n,              n an integer, j>=1            (4.10)
```

would force `3^j` to divide `p`.  Thus the only contribution at exponent
`log p` is once more `mu(p)=-1`.  The detecting determinant is necessarily
a signed projection; it cannot be the characteristic determinant of a
positive renewal kernel.

## 5. Why a smooth nonlattice counterterm cannot repair the atoms

The continuous exponential factor (1.2), translated back to `s`, is

```text
B_lambda(s)=(s-1)/(s+lambda-1).                         (5.1)
```

It has the clean reciprocal representation

```text
1/B_lambda(s)=1+lambda/(s-1)
 =Laplace[delta_0+lambda exp(u)du](s),        Re(s)>1.  (5.2)
```

This is positive and genuinely continuous away from the atom at zero.
However,

```text
1/[B_lambda(s)zeta(s)]
 =[1/B_lambda(s)] sum_n mu(n)n^(-s).                    (5.3)
```

Convolution of the continuous part of (5.2) with the Moebius atoms is
continuous and creates no singleton mass.  The `delta_0` term leaves mass
`-1` at every `log p`.  Thus (5.3) is not a positive Laplace transform and
`B_lambda zeta` is not a positive characteristic determinant.

More generally:

**Proposition 5.1 (non-atomic multipliers do not repair prime atoms).**
Let `B(s)^(-1)` be the Laplace transform of a measure with unit atom at zero
and no atoms at `log p` or at differences which can convolve an arithmetic
atom onto `log p`.  Then the inverse Laplace measure of

```text
1/[B(s)zeta(s)]                                          (5.4)
```

has mass `-1` at `log p`.

Consequently a multiplier capable of passing Theorem 3.1 must itself
insert compensating atomic mass at every prime.  A smooth continuum
renewal cannot do this.  A prime-specific counterterm can, but then the
kernel has imported the first Euler layer of `1/zeta`, which is the trace
anomaly isolated in R97 rather than an independent renewal theorem.

There is also a high-frequency version.  If `K(s)` is the transform of an
`L^1` trace-norm operator density, the Banach-valued Riemann--Lebesgue lemma
gives

```text
K(sigma+it)->0,
det(I-K(sigma+it))->1             as abs(t)->infinity.  (5.5)
```

In contrast, absolute Dirichlet convergence supplies unbounded arithmetic
recurrence times with

```text
zeta(sigma+i tau_j)->zeta(sigma)>1.                     (5.6)
```

A rational pole-killer tends to a fixed scalar at those heights.  Hence a
pure continuous-delay Fredholm determinant cannot equal the pole-killed
zeta transform even before the atom ledger is inspected.

## 6. Arithmetic operator recurrence survives noncommutativity

The continuous exponential law avoids recurrence.  An arithmetic operator
law does not.

**Theorem 6.1 (trace-norm operator recurrence).**  Suppose for some
`eta_0>0`

```text
K(s)=sum_(n>=1)A_n n^(-s),
sum_n norm(A_n)_(S_1) n^(-1+eta_0)<infinity.             (6.1)
```

Let

```text
D(s)=det(I-K(s))                                         (6.2)
```

and suppose `D` is not identically zero and `D(1)=0`.  Then there are zeros

```text
s_j=1+i tau_j+w_j,
tau_j->infinity,              w_j->0.                   (6.3)
```

### Proof

For each fixed finite set of integers, simultaneous Diophantine
approximation gives unbounded `tau_j` for which

```text
n^(-i tau_j)->1                                         (6.4)
```

on that set.  For every closed disc `abs(z)<=r<eta_0`, the tail in (6.1) is
uniformly small in trace norm.  Finite recurrence plus the tail estimate
therefore gives

```text
K(1+z+i tau_j)->K(1+z)                                  (6.5)
```

uniformly in trace norm on the disc.  Continuity of the Fredholm
determinant makes the same convergence true for `D`.

Choose a small circle centered at zero on which `D(1+z)` has no zero.
Rouche gives a zero of `D(1+z+i tau_j)` inside.  Repeat on circles with
radii tending to zero and diagonalize the recurrence sequence.  This gives
(6.3).  No products of the `A_n` were reordered, so commutativity plays no
role.  QED.

If Perron domination has already excluded zeros in `Re(s)>1`, the roots in
(6.3) lie on or to the left of that line.  If a strong nonlattice condition
also excludes nonzero boundary roots, they lie strictly to the left and
enter every fixed left half-strip.  Thus a normally convergent arithmetic
Perron determinant with an endpoint zero necessarily manufactures the fake
near-boundary zeros that continuous renewal was meant to remove.

The theorem is stable under finite sums, products, tensor powers, exterior
powers, and analytic Fredholm determinants: all preserve uniform vertical
recurrence on compact subsets.  Noncommuting transfer products therefore do
not evade it.

## 7. Noncommuting positive cycles: exact reality check

One tempting but false proof of Theorem 3.1 would claim that every ordered
trace in

```text
-log det(I-K)=sum_(m>=1)Tr(K^m)/m                       (7.1)
```

has a positive inverse Laplace measure.  This is false for noncommuting
Loewner-positive increments.

Take the three real vectors

```text
a=(1,0),       b=(1,1),       c=(-1,2)                 (7.2)
```

and the rank-one positive matrices

```text
A=aa^T,        B=bb^T,        C=cc^T.                  (7.3)
```

Then

```text
Tr(ABC)=(a.b)(b.c)(c.a)=-1.                            (7.4)
```

Every one of the six orderings with one copy of each has trace `-1`, so
their contribution to `Tr(K^3)/3` at the summed delay is `-2`.  Individual
cycle weights can therefore be negative.

The bosonic proof does not make this error.  At each particle number it
uses the positive tensor product

```text
dM(u_1) tensor ... tensor dM(u_m)                       (7.5)
```

and only then compresses to the symmetric subspace.  The extra permutation
terms in the symmetric trace restore positivity of the reciprocal
determinant even though the logarithm has signed ordered cycles.

This calculation also locates the only noncommutative escape hatch.  A raw
product of noncommuting positive matrices need not itself be positive.  If
one uses that fact to generate signed cycles, the product no longer has the
positive-measure domination (2.3), so Perron contraction at complex height
is lost.  If one repairs the product as `T^*T` or another positive dilation,
Theorem 3.1 applies again.

## 8. Exterior powers and Schur complements

The Fredholm determinant itself is the fermionic exterior-power sum

```text
det(I-K)=sum_(r>=0)(-1)^r Tr(exterior^r K).             (8.1)
```

At a primitive prime delay only the `r=1` term can contribute, giving the
negative sign (4.6).  Higher exterior powers begin at products of at least
two delays.  Thus exterior powers cannot flip the untouched-prime sign of
an eta carrier.  Treating the wedge sectors separately replaces (8.1) by a
positive energy, but then their alternating recombination is exactly the
signed projection one was trying to avoid.

Now partition an arithmetic positive kernel and form a principal Schur
complement:

```text
I-K = [[I-K_11, -K_12],
       [ -K_21, I-K_22]],

S=I-K_11-K_12(I-K_22)^(-1)K_21.                        (8.2)
```

The determinant identity is

```text
det(I-K)=det(I-K_22)det(S).                             (8.3)
```

At a prime index `p`, all cross terms in (8.2) have multiplicative degree
at least two.  Equivalently, compare the degree-one terms in the reciprocal
of (8.3).  The coefficient of `p^(-s)` in `1/det(S)` is

```text
Tr(A_(11,p))>=0.                                       (8.4)
```

It cannot equal the coefficient `-1` of `1/E_q` at an untouched prime.
Therefore a principal positive Schur complement does not realize an eta
carrier either.

One can force a different answer only by one of two moves:

* use a non-principal or signed elimination, in which case positivity is
  not inherited; or
* place prime atoms in the eliminated block so that a quotient can cancel
  them, in which case the spectator block already carries the full
  prime-specific anomaly.

This is the operator version of the R92 finite-sector dichotomy.  A
spectator either remains nonzero at a zeta zero and makes the matrix blind,
or its removal is a signed projection which returns the scalar zeta factor.

## 9. Probe ledger

The exact companion code is

```text
src/matrix_renewal_gate.py
src/test_matrix_renewal_gate.py.                        (9.1)
```

It checks:

1. the exact reciprocal-eta coefficient `-1` at untouched primes;
2. the opposite primitive-prime sign in a positive characteristic
   determinant;
3. the rank-one noncommuting PSD example (7.2)--(7.4), including all six
   cubic word traces;
4. the single endpoint zero of the exponential renewal characteristic;
5. positivity of elementary bosonic diagonal partition coefficients.

The tests are finite witnesses for the ledgers above, not evidence about
uncomputed zeta zeros.

## 10. Disposition and surviving route

This experiment closes the proposed automatic matrix mechanisms in a
strictly larger class than R92:

```text
finite positive transfer matrices,
trace-class infinite positive kernels,
positive operator-valued continuous-delay laws,
noncommuting Loewner-positive increments,
entrywise Perron-positive noncommuting kernels,
exterior-power characteristic determinants,
and principal positive Schur complements.               (10.1)
```

The obstruction is coefficient-specific, not generic pessimism.  A
positive characteristic determinant has a bosonically positive reciprocal;
an eta/zeta-bearing target has negative Moebius mass at every untouched
prime.

Three routes remain logically possible:

```text
1. a signed operator-valued measure with a new coercive complex estimate;
2. a prime-specific counterterm whose cancellation is proved rather than
   assumed;
3. a nonlinear/non-principal compression with a separate theorem replacing
   lost Perron domination.                               (10.2)
```

Route 1 returns to the signed von Mangoldt ramp of R95--R96.  Route 2 is the
first-prime trace anomaly of R97.  Route 3 returns to the signed determinant
`E_2-E_3` and its mod-6 sign pattern.  None is presently weaker than proving
a fixed-power prime cancellation estimate.

Accordingly R99 proves neither that a fixed zeta zero-free strip exists nor
that none exists.  It proves that continuous nonlattice renewal, even with
infinite state and noncommutativity, cannot supply such a strip while
honestly retaining the eta/zeta divisor through a positive characteristic
determinant.
