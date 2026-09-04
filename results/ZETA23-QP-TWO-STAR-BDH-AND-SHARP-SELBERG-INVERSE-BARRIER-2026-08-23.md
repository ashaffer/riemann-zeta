# QP broad tail: two-star BDH target and the sharp-Selberg inverse barrier

**Date:** 2026-08-23  
**Verdict:** the physical two-star count has an exact selected-modulus
variance formulation.  The natural tangent-safe estimate

```text
sum_b d_b^2 << M*D+(D^2/q)*M^2 q^o(1)                         (0.1)
```

would close the balanced broad tail with room to spare.  Unique
factorization reduces every wedge to one short determinant parameter, but
the remaining sum over that parameter is precisely a cross-interval
dispersion problem.  The fixed-`q^3` character expansion diagonalizes to an
exact rank-`#S` projection; the principal and equal-character terms are
safe, while the distinct-character correlation is not controlled by the
ordinary large sieve.

A standard bilinear large-spectrum or Balog--Szemeredi--Gowers inverse of
the sharp Selberg `L^1` target does not repair this.  An arbitrarily small
power failure is only a tiny **centered** perturbation of the uniform phase
background, below the density threshold at which positive-energy BSG gives
a macroscopic packet.  Moreover `|S_l|` is invariant under translating all
reciprocal phases, so an inverse packet need not carry any mass in the
actual product window.  A cyclic Latin block gives an exact abstract
separable saturation with all three pair projections injective and no
locally rich tangent cell.  The actual product equations exclude the
complete block, but promoting general spectral excess to the linked cycles
needed for that exclusion is a new mask-sensitive inverse theorem.

Thus neither the two-star bound nor the sharp four-cycle theorem is proved
here.  The precise surviving input is a selected-shell BDH/restriction
estimate, or an equivalent centered and mask-sensitive bilinear inverse
theorem.

---

## 1. Exact physical wedge reduction

Let `S` be the actual prime-power project shell, let `A subset S` have
cardinality `M`, and put

```text
T_(b,c)=1
```

when some `a in S` satisfies

```text
|8*a*b*c-q^3|<=C*q*D.                                      (1.1)
```

The admissible interval for `a`, after `(b,c)` is fixed, has length
`O(D/q)<1`; hence `a` is unique.  Write

```text
d_b=sum_(c in A)T_(b,c),
E2(A)=sum_b d_b(d_b-1).                                    (1.2)
```

For one ordered wedge choose its two row lifts `a,a'` and residuals

```text
r =8*a *b*c -q^3,
r'=8*a'*b*c'-q^3.                                         (1.3)
```

Then

```text
h=a*c-a'*c',             0<|h|<<D,
r-r'=8*b*h.                                                (1.4)
```

In the all-five-distinct sector the shell nodes have distinct prime bases,
so

```text
gcd(q^3+r,q^3+r')=8*b.                                    (1.5)
```

Fix `(c,c',h)`.  Any two integral solutions of

```text
c*a-c'*a'=h                                                (1.6)
```

differ by an integral multiple of `(c',c)`.  The project shell has diameter
smaller than either coordinate, so at most one shell solution exists.
Once `(a,c)` is fixed, the interval for `b` in (1.1) again has length
`O(D/q)<1`.  Consequently

```text
(c,c',h) determines the whole ordered wedge up to O(1).    (1.7)
```

This proves only `E2(A)<<M^2 D q^o(1)`.  Removing the `h`-sum is the exact
remaining issue; fixed-tuple uniqueness is not the desired aggregation.

Equivalently, let `R_A` be the oriented residual multiset in (1.3).  Its
multiplicity is `O(1)` by unique factorization, and

```text
d_b=#{r in R_A:r==-q^3 (mod 8*b)}.                           (1.8)
```

Thus the two-star problem is a variance problem for one selected residue
class over the shell moduli `b~q`.

## 2. The tangent-safe BDH theorem that would close the tail

The expected degree is

```text
mu~M*D/q.                                                   (2.1)
```

The diagonal-strength selected-modulus statement is

```text
sum_(b in S)|d_b-mu|^2<<M*D q^o(1).                         (BDH)
```

It implies

```text
sum_b d_b^2
 <<M*D+(D^2/q)*M^2 q^o(1),                                (2.2)
```

which is (0.1).  At the balanced broad face

```text
M=D^(15/8),                 q=D^(33/16+o(1)),              (2.3)
```

both terms in (2.2) are smaller than `M^2`:

```text
M*D/M^2=D^(-7/8),
D^2/q=D^(-1/16).                                           (2.4)
```

Hence `(BDH)` proves `E2(A)<<M^2q^o(1)` and closes this broad face.
The first term is necessary in a uniform theorem: the explicit full-integer
tangent packet in the companion two-star report has `E2~M*D` in its own
parameter range.  It is therefore wrong to ask for the random main term
alone.

## 3. Exact fixed-modulus projection identity

Assume for this paragraph that `q` is odd and restrict to the unit sector
modulo

```text
Q=q^3,                     Phi=phi(Q).                     (3.1)
```

Let `R_chi`, `P_chi`, and `A_chi` be the multiplicative-character sums of
the residual interval, the shell, and `A`, respectively.  Character
orthogonality in

```text
r==8*a*b*c (mod Q)                                          (3.2)
```

gives, with an immaterial unit phase absorbed into `F_chi`,

```text
d_b=Phi^(-1) sum_chi F_chi conjugate(chi(b)),
F_chi=R_chi conjugate(P_chi*A_chi*chi(8)).                  (3.3)
```

Define

```text
V_(b,chi)=Phi^(-1/2) conjugate(chi(b)),       b in S.       (3.4)
```

Distinct shell nodes are distinct units modulo `Q`, so full character
orthogonality gives the exact identity

```text
V*V^*=I_S,
sum_(b in S)d_b^2=Phi^(-1)||V F||_2^2.                      (3.5)
```

Equivalently, if

```text
K(eta)=sum_(b in S)eta(b),                                  (3.6)
```

then

```text
sum_b d_b^2
 =Phi^(-2) sum_(chi,psi) F_chi conjugate(F_psi)
                         K(conjugate(chi)*psi).             (3.7)
```

The principal term has size `(D^2/q)M^2`.  The
`chi=psi!=1` diagonal is below `M^2` by the proved fourth/sixth-moment and
Burgess ledger.  The unresolved term is exactly `chi!=psi`.

Identity (3.5) is also a no-go for a coefficient-blind fixed-modulus large
sieve: `V` already has orthonormal rows.  Its operator norm is exactly one,
and the corresponding convolution kernel in (3.7) is the rank-`#S`
projection onto the selected shell.  Any gain must use the special product
structure of `F`, not another application of character orthogonality.

In physical coordinates, Poisson completion of the common-carrier window
produces phases

```text
e(l*q^3/(8*a*c)),                 |l|<=q/D.                  (3.8)
```

After the second copy is inserted, additive reciprocity has two coupled
varying inverses.  This is the same reciprocal/Farey-fan HSM kernel isolated
in `(2E.F3)--(2E.F7)` of the weighted-secant report.  Current one-inverse
large-sieve or local fan estimates do not control its cross-fan sum.

## 4. Why ordinary large-spectrum/BSG is below threshold

The sharp local Selberg target is

```text
sum_(1<=|l|<=H)|S_l(A,C)|<<q q^o(1),
H=q/D, 
S_l(A,C)=sum_(a in A,c in C)e(l*q^3/(8*a*c)),               (4.1)
```

for two relevant slope-block projections with

```text
|A|,|C|<=D.                                                  (4.2)
```

At the maximal local sizes put

```text
N=|A|*|C|=D^2,                 H=D^(17/16+o(1)).             (4.3)
```

Suppose (4.1) fails by an arbitrarily small power:

```text
sum_l|S_l|>=q*D^epsilon.                                    (4.4)
```

The average large coefficient is only

```text
q*D^epsilon/H=D^(1+epsilon),
|S_l|/N~D^(-1+epsilon).                                    (4.5)
```

Thus a Chang large-spectrum bound at the forced normalized threshold
`rho=D^(-1+epsilon)` has dimension allowance

```text
rho^(-2) log H=D^(2-2epsilon+o(1)),                         (4.6)
```

which gives no useful low-dimensional structure.

Cauchy--Schwarz gives the exact second-moment consequence

```text
sum_l|S_l|^2>=q*D^(1+2epsilon)
              =H*N*D^(2epsilon).                            (4.7)
```

Discretize the reciprocal phases into `H` equal cells and let `n_j` be the
occupancies.  Parseval identifies the nonzero Fourier energy with the
centered variance, up to harmless smoothing:

```text
sum_j(n_j-N/H)^2 >= N*D^(2epsilon).                         (4.8)
```

But the uniform background has squared mass

```text
H*(N/H)^2=N^2/H=D^(47/16+o(1)).                             (4.9)
```

The relative perturbation in (4.8) is only

```text
D^(-15/16+2epsilon).                                       (4.10)
```

For every `epsilon<15/32` this tends to zero.  Positive-energy BSG sees the
background, not the centered perturbation.  Since a `q^o(1)` theorem must
exclude every fixed `epsilon>0`, ordinary BSG cannot supply the needed
inverse at the relevant threshold.

## 5. Mask loss and an exact abstract inverse obstruction

There is a second, independent logical obstruction.  Replacing every phase
`x_(a,c)` by `x_(a,c)+theta` multiplies `S_l` by `e(l theta)` and leaves

```text
|S_l|                                                     (5.1)
```

unchanged.  It can move the recovered packet completely away from the
zero-centered product window.  Therefore an inverse theorem whose input is
only the magnitudes in (4.1) cannot conclude that its packet contains any
actual edges.  This is exactly the mass-retention gap created by the
positive Selberg completion: a resonance among added or off-window pairs
cannot be charged to the existing tangent/Hankel merger.

The gap has a finite separable model.  Take a cyclic group of order `L` and
triples

```text
(a_i,b_s,c_(i+s)),                  i,s in Z/LZ.             (5.2)
```

Every two displayed coordinates determine the third, so all three
two-coordinate projections are injective.  Assign the `L` carriers to `L`
different short carrier intervals.  Then every fixed ordered row pair has
at most one common carrier in any short interval: the local tangent test is
empty.

Abstractly assign reciprocal phase zero to every `(a_i,c_j)` pair.  With
flat separable weights,

```text
S_l=L^2                  for every l,
sum_(l<=H)|S_l|=H*L^2.                                  (5.3)
```

Choosing

```text
L=D^((1+epsilon)/2)<=D                                  (5.4)
```

makes (5.3) equal `qD^epsilon`.  Hence an arbitrarily small power excess is
compatible with separability, pair uniqueness, and complete local tangent
sparsity in the abstract incidence category.

This is not an actual QP configuration.  The exact product equations rule
out the complete cyclic block: a four-shift determinant cancellation gives

```text
|c_j*c_(j+2)-c_(j+1)^2|<<D,                              (5.5)
```

and the cyclic ratio chain forces all integral colors to coincide because
`D^2/q=o(1)`.  The point is that deriving enough coherently indexed cycles
like (5.5) from a small centered spectral excess is itself the missing
cross-interval inverse theorem.  Local BSG, tangent peeling, and pair
uniqueness do not provide that indexing.

## 6. Binary status

```text
fixed-(c,c',h) wedge uniqueness:                     PROVED;
residual selected-modulus/BDH formulation:            PROVED;
(BDH) => sharp balanced broad tail:                   PROVED;
principal and equal-character diagonal:               SAFE;
distinct-character/off-diagonal restriction:          OPEN;
ordinary fixed-modulus large sieve closes it:          NO (PROJECTION IDENTITY);
ordinary positive-energy BSG reaches q^o threshold:    NO (CENTERED DENSITY AUDIT);
Selberg-|S_l| inverse retains actual mask:             NO;
abstract separable Latin saturation:                   EXPLICIT;
actual-prime-power two-star or sharp Selberg theorem:  OPEN;
sharp uniform four-cycle theorem from this route:      NOT PROVED.
```
