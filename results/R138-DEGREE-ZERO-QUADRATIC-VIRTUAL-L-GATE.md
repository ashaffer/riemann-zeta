# R138 degree-zero quadratic virtual `L`-function gate

## Status

This report records a new exact cancellation mechanism.  Let `chi` and
`psi` be primitive even real quadratic characters of coprime positive
fundamental discriminants.  Then

```text
F_(chi,psi)(s)=zeta(s)L(s,chi psi)/[L(s,chi)L(s,psi)]       (0.1)
```

has all three properties which the earlier logarithmic-derivative routes
could not obtain simultaneously:

```text
-F'/F has nonnegative prime-power coefficients;
the complete Gamma degree is zero;
the complete conductor is one.                              (0.2)
```

In fact

```text
-F'/F
 =D_zeta+D_(chi psi)-D_chi-D_psi
 =sum_(p,v>=1) (log p)(1-chi(p)^v)(1-psi(p)^v)p^(-vs),       (0.3)
```

where `D_chi=-L'/L`.  The coefficient in (0.3) is nonnegative.
This is a genuine degree-zero positive Euler detector, not merely a
cancellation of leading asymptotics.

The mechanism extends to every nonnegative Boolean class function satisfying
explicit identity and inertia vanishing conditions.  It includes a sparse
`m+2`-function construction

```text
(m-1)D_zeta-sum_j D_(chi_j)+D_(product_j chi_j),              (0.4)
```

whose prime coefficient is always nonnegative and whose Gamma and conductor
terms cancel exactly.

The fail-fast audit does not turn (0.1) into a fixed strip.  A hypothetical
zeta zero is a negative pole of (0.3), but zeros of the denominator
`L`-functions are positive poles and can pay for it.  Killing the high-jet
prime saddle would force those auxiliary poles into a target disc unless the
weighted conductor complexity is at least the Cauchy localization budget.
All currently controlled ways of selecting quadratic characters -- direct
CRT prescription, independent-character averaging, Haar large deviations,
and the explicit complement interpolant below -- spend that budget too
quickly.  Two exceptional possibilities remain:

1. a very low-conductor quadratic character pattern which is anomalously
   principal-like on precisely the high-jet primes; or
2. a finite-height off-diagonal correlation which makes the signed auxiliary
   zero remainder much smaller than its absolute conductor bound.

Neither is ruled out here.  Consequently this report proves neither a fixed
zero-free strip nor zeros approaching one.

```text
biquadratic positive logarithmic derivative                 EXACT
Gamma-degree cancellation                                   EXACT
conductor cancellation                                      EXACT
general Boolean virtual-character theorem                   EXACT
sparse m+2-function positive detector                        EXACT
conditional high-jet contradiction criterion                EXACT
direct CRT realization                                       TOO EXPENSIVE
Haar/family large-deviation selection                        TOO LATE
exceptional low-conductor Frobenius pattern                  OPEN
signed auxiliary-zero correlation                            OPEN
fixed zero-free strip                                        NOT PROVED
nonexistence of a fixed strip                                NOT PROVED
```

Date: 2026-08-08.

## 1. The biquadratic identity

Choose coprime positive odd fundamental discriminants `d_1,d_2`, and put

```text
chi=chi_(d_1),       psi=chi_(d_2).                           (1.1)
```

Then `chi`, `psi`, and `chi psi=chi_(d_1d_2)` are primitive and even.  Their
completed functions are

```text
Lambda_d(s)=(d/pi)^(s/2) Gamma(s/2)L(s,chi_d),
Lambda_d(s)=Lambda_d(1-s).                                   (1.2)
```

Together with the completed zeta function, (1.2) gives the exact identity

```text
[pi^(-s/2)Gamma(s/2)zeta(s)] Lambda_(d_1d_2)(s)
---------------------------------------------------
             Lambda_(d_1)(s)Lambda_(d_2)(s)

       =zeta(s)L(s,chi psi)/[L(s,chi)L(s,psi)].                (1.3)
```

Both powers of `pi`, both Gamma factors, and both discriminants cancel.
Thus `F_(chi,psi)(s)=F_(chi,psi)(1-s)` as a meromorphic identity.

For `Re(s)>1`, logarithmic differentiation gives (0.3).  Since every value
of a real character belongs to `{-1,0,1}`,

```text
(1-chi(p)^v)(1-psi(p)^v)>=0.                                  (1.4)
```

At an unramified prime the coefficient is `4` exactly when both characters
are `-1` and `v` is odd; otherwise it is zero.  Correspondingly the local
Euler factor is

```text
1,                                      not both values -1;
[(1+p^(-s))/(1-p^(-s))]^2,              both values -1.       (1.5)
```

Ramified values also satisfy (1.4).  The zeta pole at one is retained, since
all three nonprincipal quadratic `L`-functions are nonzero at one.

This is the first construction in the present sequence which has positive
prime coefficients and cancels both the vertical `log T` term and the
conductor constant without a sigma difference.

## 2. Boolean virtual-character theorem

The pair identity is one member of a larger exact cone.  Let

```text
d_1,...,d_m
```

be pairwise coprime positive odd fundamental discriminants.  Write `chi_j`
for their characters and, for `S subset {1,...,m}`,

```text
chi_S=product_(j in S)chi_j,       d_S=product_(j in S)d_j,
chi_empty=1,                       L(s,chi_empty)=zeta(s).      (2.1)
```

Every `chi_S` is primitive and even.  Let

```text
phi(x_1,...,x_m)=sum_S a_S product_(j in S)x_j                (2.2)
```

be the multilinear Fourier expansion of a real function on
`{+-1}^m`.  Put `e=(1,...,1)` and let `v_j` be the vertex with its `j`th
coordinate `-1` and all other coordinates `1`.

### Theorem 2.1 -- degree-zero positive virtual characters

Assume

```text
phi>=0 on {+-1}^m,
phi(e)=0,
phi(v_j)=0 for 1<=j<=m.                                      (2.3)
```

Then

```text
A_phi(s)=sum_S a_S D_(chi_S)(s)                              (2.4)
```

has the following properties.

1. In `Re(s)>1`,

   ```text
   A_phi(s)=sum_(p,v>=1)(log p)phi(chi_1(p)^v,...,chi_m(p)^v)
                                      p^(-vs),                (2.5)
   ```

   and every coefficient is nonnegative.
2. All Gamma, `pi`, and conductor terms in the completed logarithmic
   derivative cancel exactly.
3. `A_phi(s)=-A_phi(1-s)` away from its poles.
4. The coefficient of `D_zeta` is

   ```text
   a_empty=2^(-m)sum_(x in {+-1}^m)phi(x).                    (2.6)
   ```

   It is positive for every nonzero `phi` satisfying (2.3).

#### Proof

A multilinear polynomial at a point of `[-1,1]^m` is a convex combination
of its values at the vertices.  Hence nonnegativity on the Boolean cube also
holds when some coordinates are zero.  Formula (2.5) follows by expanding
the Dirichlet series for every logarithmic derivative.

The common Gamma coefficient is

```text
sum_S a_S=phi(e)=0.                                           (2.7)
```

For the conductor, Fourier inversion gives

```text
sum_(S containing j)a_S=[phi(e)-phi(v_j)]/2=0.                (2.8)
```

Since `log d_S=sum_(j in S)log d_j`, (2.8) cancels every
`log d_j` separately.  Apply the functional equation (1.2) term by term to
obtain the antisymmetry.  Equation (2.6) is the constant Fourier
coefficient.  QED.

Conditions (2.3) have an Artin-conductor interpretation: the virtual class
function vanishes at the identity and at every generator of inertia.  This
explains why degree and conductor can both vanish without making the prime
class function zero.

## 3. Two exact subfamilies

### 3.1 The product detector

For

```text
phi_prod(x)=product_(j=1)^m(1-x_j),                            (3.1)
```

Theorem 2.1 gives

```text
A_prod(s)=sum_S(-1)^|S|D_(chi_S)(s).                           (3.2)
```

At an unramified odd prime power it is supported only on the Frobenius class
`(-1,...,-1)`, where its value is `2^m`.  Its Fourier `l1` mass is `2^m`.
If the characters have an odd multiplicative dependency, the all-minus
class is absent, but then (3.1) is identically zero on the actual Galois
group and the corresponding `L`-combination cancels algebraically.  Thus a
global structural cover of every prime also deletes the zeta detector.

### 3.2 A sparse `m+2`-function detector

For every `m>=2`, define

```text
phi_star(x)
 =1-[1/(m-1)]sum_j x_j+[1/(m-1)]product_j x_j.                 (3.3)
```

If exactly `w` coordinates of a Boolean vertex are negative, then

```text
phi_star(x)=[2w-1+(-1)^w]/(m-1)
            =2 floor(w/2)/(m-1)>=0.                            (3.4)
```

It vanishes at `w=0,1`, so Theorem 2.1 applies.  Clearing denominators gives
the integer-exponent virtual quotient

```text
calF_m(s)=zeta(s)^(m-1)L(s,product_j chi_j)
                         /product_j L(s,chi_j),                (3.5)

-calF_m'/calF_m
 =(m-1)D_zeta-sum_jD_(chi_j)+D_(product_jchi_j).               (3.6)
```

The prime coefficient in (3.6) is `(m-1)phi_star>=0`.  Its Gamma and
conductor terms cancel exactly.  Unlike (3.2), it uses only `m+2` functions,
and

```text
sum_S |a_S|=2m/(m-1),
sum_S |a_S||S|=2m/(m-1).                                      (3.7)
```

The second identity is the relevant conductor-weighted Fourier cost.
The head vanishes if, for every active prime, at most one of the `chi_j(p)`
is negative.  Producing that unusually disjoint family of nonresidue sets is
the arithmetic difficulty; the analytic virtual quotient itself is cheap.

## 4. A conditional high-jet contradiction theorem

The exact value of the construction is best stated as a sufficient theorem.
Let

```text
J_(phi,k)(s)=(-1)^k A_phi^(k)(s)/k!.                           (4.1)
```

Suppose a zeta zero creates a nearest zeta-pole distance `d` from

```text
z_*=1+r+i gamma,       r>0,                                   (4.2)
```

and choose `R>d`.  Assume the closed disc `B(z_*,R)` contains no zero of
any nontrivial `L(s,chi_S)` for which `a_S!=0`.  The only singularities of
`A_phi` in that disc are then zeta zeros.  The nearest-pole power-sum lemma
from R133 supplies a bounded-gap sequence of orders for which

```text
|J_(phi,k)(z_*)|>=c d^(-k-1)
 -O(C_phi R^(-k-1)),                                         (4.3)

C_phi=sum_S |a_S|[1+log d_S+log(|gamma|+3)].                  (4.4)
```

The standard unit-interval zero count for Dirichlet `L`-functions gives
(4.3): outside the zero-free disc, sum the reciprocal powers over unit
height annuli.  Polynomial factors in `k` can be absorbed into the constant
or into `R^(o(k))`.

Now suppose all discriminants are coprime to the primes `p<=X` and

```text
phi(chi_1(p),...,chi_m(p))=0,             p<=X.                (4.5)
```

Even prime powers vanish because `phi(e)=0`; hence (2.5) and Chebyshev's
bound give, for `X=exp(lambda k/r)` and fixed `lambda>1`,

```text
|J_(phi,k)(z_*)|
 <=||phi||_infinity r^(-k+o(k))
       exp[-k(lambda-1-log lambda)].                            (4.6)
```

Consequently (4.3)--(4.6) contradict the source zero if, along the useful
orders,

```text
lambda-1-log lambda>log(d/r),
||phi||_infinity=exp(o(k)),
C_phi=o((R/d)^k),                                              (4.7)
```

and all auxiliary functions are zero-free in `B(z_*,R)`.

This is a genuine fixed-strip reduction.  It asks for a quadratic
Frobenius mask with sub-localization conductor complexity plus an auxiliary
zero-avoidance statement.  Neither requirement mentions RH for zeta.

## 5. Why the direct CRT construction misses (4.7)

There is an elementary way to make (4.5) hold for the pair detector.  Put

```text
P_X=8 product_(p<=X)p,                                        (5.1)
```

and choose distinct primes `q_1,q_2` congruent to `1 mod P_X`.  Quadratic
reciprocity gives

```text
chi_(q_j)(p)=1,                 p<=X.                          (5.2)
```

Linnik's theorem supplies such primes with

```text
log(q_1q_2)<<log P_X<<X.                                      (5.3)
```

For `X=exp(lambda k/r)`, the logarithm of the weighted conductor therefore
has exponential rate `lambda/r` in `k`.  But localization into
`Re(s)>1-eta`, with `R<r+eta`, has rate

```text
L=log(R/d),
rL<eta.                                                       (5.4)
```

For every nontrivial strip `eta<1` and every `lambda>1`, the explicit CRT
rate is larger than (5.4).  Thus (5.3) cannot satisfy (4.7).

This is a failure of the construction, not a lower bound for every possible
quadratic character.  Burgess's least-nonresidue theorem gives only a
polynomial relation between a modulus and a long initial residue run.  It
does not prove the exponential-in-`X` conductor lower bound that would close
the exceptional possibility in (4.7).  The simultaneous two-character
cover is weaker still than asking each character to equal `+1` on the whole
head.

## 6. Adaptive Boolean interpolation and its square-root wall

Theorem 2.1 permits a mask chosen after the finite Frobenius vectors are
known.  Let `H` contain

```text
e, v_1,...,v_m,
and every vector (chi_1(p),...,chi_m(p)) for p<=X,              (6.1)
```

and suppose the head primes are unramified.  If `N=2^m` and `h=|H|<N`, set

```text
phi_H(x)=N/(N-h) 1_(x notin H).                                (6.2)
```

Then `phi_H` satisfies Theorem 2.1, has mean one, and kills the complete
prime head.  Its Fourier coefficients obey the exact Parseval identities

```text
a_empty=1,
sum_(S nonempty)|a_S|^2=h/(N-h),                               (6.3)

sum_S |a_S||S|
 <=1/2 sqrt[hN(m^2+m)/(N-h)].                                 (6.4)
```

Thus, when `N>>h`, the auxiliary Fourier mass has a square-root rather than
linear dependence on the number of distinct head vectors.

For an unstructured head, however, `h` is of order

```text
pi(X)=exp[(lambda/r+o(1))k].                                  (6.5)
```

Even (6.4) then has exponential rate `lambda/(2r)`.  In the only relevant
range `eta<1/2`, (5.4) gives

```text
L<1/(2r)<lambda/(2r).                                         (6.6)
```

So the explicit complement interpolant still misses (4.7).  This is the
quadratic-character analogue of R137's variance/Cauchy gate.

Equation (6.4) is not a universal lower bound.  A specially structured set
of Frobenius vectors can be annihilated by a much smaller Fourier polynomial;
`phi_star` is an exact example.  The live arithmetic question is whether the
actual prime vectors admit such exceptional low-conductor interpolation at
the high-jet saddle.

## 7. Family averaging reconstructs the classical zeta obstruction

On the formal independent quadratic sign torus,

```text
E chi(n)=1_(n is a square).                                   (7.1)
```

For the pair detector,

```text
E[(1-chi(n))(1-psi(n))]
 =[1-1_(n is a square)]^2.                                   (7.2)
```

Consequently an unconditioned family average of (0.3) is just `D_zeta`
with the square-prime-power series removed.  That removed series is
absolutely convergent in `Re(s)>1/2`.  The average therefore reconstructs
the classical zeta logarithmic derivative, including its near-one target
and its bulk zero ledger; it does not create a new sign.

Conditioning the family so that the high jet is much smaller than this mean
is a large-deviation event.  Applying the entropy theorem of R137 to the
independent quadratic sign blocks gives the same lower rate

```text
G=min{2 log((r+1/2)/d), log((r+1)/d)}.                         (7.3)
```

For `eta<1/2`, `G>log(R/d)`.  Hence every selection theorem whose main term
is Haar/diagonal quadratic-character averaging needs a family larger than
the conductor size allowed by (4.7).  As in R137, this is not a deterministic
statement that the actual finite family never hits the exceptional set.
An off-diagonal arithmetic hit remains open.

## 8. Auxiliary zero density is not, by itself, the fatal step

Jutila's classical estimate, in the notation summing over primitive
characters of conductor at most `Q`, is

```text
N(alpha,Q,T)<<_(epsilon)(QT)^[4(1-alpha)+epsilon],
alpha>=4/5.                                                   (8.1)
```

For fixed target height and `1-alpha<1/4`, (8.1) says that only `o(Q)` of a
linear-size family can have a zero in a fixed near-one rectangle.  Prescribing
finitely many Legendre symbols still leaves a positive-density family once
the conductor range tends to infinity.  Qualitatively, one can therefore
avoid the auxiliary zeros after fixing `k` and its finite head.

The quantitative problem is that the density of a prescribed head pattern
is exponentially small in the number of independent prime conditions.  The
conductor range needed to find a good member then makes `C_phi` in (4.4)
larger than `(R/d)^k`.  Differentiation removes the conductor constant from
the explicit formula, but the conductor reappears in the number of remote
auxiliary zeros which can cancel the zeta target.  This is the precise
repayment mechanism.

## 9. What would actually close the route

Any one of the following would be enough to reopen (and potentially finish)
the proof.

1. **Exceptional two-character cover.**  For infinitely many useful orders,
   find coprime positive fundamental discriminants with

   ```text
   no p<=exp(lambda k/r) has chi(p)=psi(p)=-1,
   log(d_1d_2)=o((R/d)^k),                                    (9.1)
   ```

   and with `L(s,chi)`, `L(s,psi)`, and `L(s,chi psi)` zero-free
   in `B(z_*,R)`.
2. **Low-conductor Boolean interpolant.**  Prove (4.5) with the weighted
   Fourier conductor norm (4.4) below `(R/d)^k`, improving decisively on
   (6.4).
3. **Signed remote-zero theorem.**  Keep a larger conductor, but prove that
   the alternating auxiliary zero sum has cancellation beyond its absolute
   `C_phi R^(-k)` bound.

The first two are exceptional Frobenius-pattern statements; the third is a
target-conditioned joint zero correlation.  Standard character large sieve,
ordinary zero density, and Haar moments supply none of them.

## 10. Literature boundary

The analytic ingredients imported here are classical rather than new:

* D. R. Heath-Brown, *The density of zeros of Dirichlet's L-functions*,
  Canadian Journal of Mathematics 31 (1979), for family zero-density
  estimates and their conductor dependence;
* M. Jutila, *Zero-density estimates for L-functions*, Acta Arithmetica 32
  (1977), especially the estimate quoted in (8.1);
* D. A. Burgess, *The distribution of quadratic residues and non-residues*,
  Mathematika 4 (1957), for the least-nonresidue limitation discussed after
  (5.4); and
* the Heilbronn/Brauer virtual-character literature for the general use of
  character combinations in quotients of Artin `L`-functions.

No source found in the audit treats the positive degree-zero class function
`(1-chi)(1-psi)` as a fixed-strip detector, nor supplies any of the three
estimates in Section 9.  Those are new reductions, not imported theorems.

## 11. Verdict

The main gain is real: positivity no longer forces a `log T` Gamma debt, and
conductor cancellation no longer forces a signed prime side.  The exact
biquadratic identity (0.3) passes both tests.

The remaining obstruction is also now exact.  A near-one zeta zero can be
paid for by zeros of the denominator `L`-functions.  Making the prime side
too small forces that payment to be local only when the weighted conductor
complexity lies below `(R/d)^k`.  Every currently controlled character
selection spends more than this localization budget.  Exceptional arithmetic
selection or a signed auxiliary-zero theorem remains logically possible.

Therefore this mechanism has not proved a fixed strip, and its failure has
not proved that no fixed strip exists.
