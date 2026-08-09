# R139 quadratic universality and pair-replication gate

## Status

The character-aspect continuation of R138 separates into a strong theorem
and a sharp obstruction.

For the degree-zero quotient

```text
F_(d,e)(s)=zeta(s)L(s,chi_(de))
                    /[L(s,chi_d)L(s,chi_e)],                    (0.1)
```

control on only the upper half of a conjugation-symmetric contour is enough
to force the complete divisor identity

```text
N_D(L_(chi_d))+N_D(L_(chi_e))
 =N_D(zeta)+N_D(L_(chi_(de))).                                  (0.2)
```

Consequently every successful pair must supply at least as many denominator
zeros as the zeta function has in `D`.  Quadratic-family zero density then
shows that the proportion of successful pairs is at most

```text
Q^[-Delta(sigma_D)+epsilon],       Delta(sigma_D)>0              (0.3)
```

for every fixed domain whose left edge `sigma_D` is greater than `1/2`.
Thus even a polynomially decaying pair-replication theorem would prove the
desired zero-free region.  The counting stage reaches the whole right half
of the critical strip; the older `4/5` or `3/4` thresholds are not the
bottleneck.

Standard quadratic universality cannot supply the forcing event.  Its target
functions must extend holomorphically and without zeros to a simply connected
conjugation-symmetric region.  A region of that kind which contains the upper
half-contour also contains the full contour and its interior.  The target
ratio therefore retains the enclosed zeta zero, so it cannot be uniformly
close to a nonzero constant on the upper half-contour.  This is not a weak
effective constant: the required admissible target does not exist.

Mishou and Nagoshi's 2006 theorem already identifies the corresponding
single-character approximation statement as an equivalent of RH.  The
present pair formulation lowers the density needed from positive to a
specific negative power of the conductor, but it does not remove the target
topology.

```text
upper-half reflection--Rouche criterion                 EXACT
full divisor identity for the R138 quotient             EXACT
quadratic pair-counting threshold for every sigma>1/2   EXACT
ordinary quadratic universality closure                 IMPOSSIBLE
published correlated chi-aspect universality closure    IMPOSSIBLE
slit/keyhole closure                                     DERIVATIVE DEBT
fixed zero-free strip                                    NOT PROVED
zeros approaching one                                    NOT PROVED
```

Date: 2026-08-08.

Predecessors:

* [`R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md`](R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md);
* [`R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md).

## 1. One-sided control is already a closed-contour theorem

Let `D` be a conjugation-symmetric Jordan domain compactly contained in

```text
1/2<Re(s)<1,                                                   (1.1)
```

write `Gamma=partial D`, and put

```text
Gamma_+=Gamma intersection {Im(s)>=0}.                         (1.2)
```

The domain may be very tall: when a proposed zero has ordinate `gamma`, it
can enclose both that zero and its conjugate.  Its height is fixed while the
character conductor tends to infinity.

### Lemma 1.1 -- reflection--Rouche

Suppose that `f` is meromorphic near the closure of `D`, has no zero or pole
on `Gamma`, and

```text
f(conjugate(s))=conjugate(f(s)).                                (1.3)
```

If `c` is a nonzero real number and

```text
sup_(s in Gamma_+) |f(s)-c|<|c|,                               (1.4)
```

then

```text
Z_D(f)-P_D(f)=0.                                               (1.5)
```

#### Proof

Reflection and the reality of `c` extend (1.4) to all of `Gamma`.  The
image `f(Gamma)` lies in the open disc of centre `c` and radius `|c|`, which
does not contain zero.  It has winding zero around zero.  The meromorphic
argument principle gives (1.5).  QED.

This lemma is useful because the analytic approximation is needed on only
half of a contour.  It is also dangerous: real-character symmetry supplies
the other half for free, so there is no way to hide the missing winding
there.

## 2. Exact application to the biquadratic detector

Take distinct positive prime fundamental discriminants `d,e`, or more
generally coprime positive odd fundamental discriminants.  All characters in
(0.1) are real and even, so (1.3) holds.  Inside a domain satisfying (1.1)
none of the four functions has a pole.  The divisor of (0.1) is

```text
div(F_(d,e))
 =div(zeta)+div(L_(chi_(de)))
  -div(L_(chi_d))-div(L_(chi_e)).                               (2.1)
```

Lemma 1.1 therefore gives (0.2), with multiplicity.  Common zeros require no
special convention: (2.1) is an identity of divisors, so all cancellations
are already included.

If `D` contains a zeta zero, every pair satisfying (1.4) obeys

```text
N_D(L_(chi_d))+N_D(L_(chi_e))>=N_D(zeta)>=1.                    (2.2)
```

A zero of the product character does not offer an escape.  It occurs on the
right side of (0.2) and forces still more denominator multiplicity.

The same statement applies to the non-coprime shared-twist quotient

```text
zeta(s)L(s,chi_e)/[L(s,chi_d)L(s,chi_(ed))].                    (2.3)
```

Exact conductor cancellation is irrelevant to this contour-counting lemma.
It matters only to attempts to prove the approximation event analytically.

## 3. Quadratic-family zero density makes counting cheap

For primitive real characters define

```text
calN(sigma,R,T)
 =sum_(cond(chi)<=R) N(sigma,T,chi).                             (3.1)
```

Heath-Brown's real-character estimate gives, for fixed `epsilon>0`,

```text
calN(sigma,R,T)
 <<_(epsilon) (RT)^epsilon
       R^[a_H(sigma)] T^[(3-2sigma)/(2-sigma)],

a_H(sigma)=3(1-sigma)/(2-sigma).                               (3.2)
```

Corrigan's 2024 fixed-order estimate improves the conductor exponent near
one.  At fixed `T` one may use

```text
a_*(sigma)
 =min{3(1-sigma)/(2-sigma), 8(1-sigma)/3}.                      (3.3)
```

The second branch is better for `sigma>7/8`.  The decisive fact is

```text
a_*(sigma)<1 if and only if sigma>1/2.                          (3.4)
```

Let `P_Q` be the primes `q` in `[Q,2Q]` with `q=1 mod 4`.  Then

```text
#P_Q asymp Q/log Q.                                             (3.5)
```

Fix `D` and put

```text
sigma_D=min_(s in closure(D)) Re(s)>1/2,
T_D=1+max_(s in closure(D)) |Im(s)|.                            (3.6)
```

Call `q` bad when `L(s,chi_q)` has a zero in `D`.  Equations
(3.1)--(3.4) give

```text
# {q in P_Q:q bad} <<Q^[a_*(sigma_D)+epsilon].                  (3.7)
```

Every successful ordered pair from Section 2 contains a bad coordinate.
Hence

```text
# successful pairs
 <<(#P_Q) Q^[a_*(sigma_D)+epsilon],

# successful pairs/(#P_Q)^2
 <<Q^[-Delta(sigma_D)+epsilon] log Q,                           (3.8)

Delta(sigma)=1-a_*(sigma)>0.                                   (3.9)
```

Explicitly,

```text
Delta(sigma)=(2sigma-1)/(2-sigma),       1/2<sigma<=7/8,
Delta(sigma)=(8sigma-5)/3,               7/8<=sigma<1.          (3.10)
```

Thus a forcing theorem with density

```text
delta_Q >>Q^[-Delta(sigma_D)+2epsilon]                          (3.11)
```

would contradict (3.8).  Positive density is far more than is needed.

If a construction instead counts the product character as an alternative,
the map `(d,e)->de` has multiplicity at most

```text
tau(de)=Q^o(1),                                                (3.12)
```

and its conductor is at most order `Q^2`.  Its zero-density contribution is
`Q^[2a_*(sigma_D)+o(1)]=o(Q^2)`.  For prime discriminants the product
multiplicity is exactly two.  For the exact divisor identity (0.2), however,
this extra estimate is unnecessary.

### Consequence

The counting side is not merely a fixed-strip theorem.  If the one-sided
forcing event could be proved at the density (3.11) for every fixed `D` in
the right half-strip, the same argument would exclude every zeta zero with
real part greater than `1/2`.

## 4. The known universality theorem is already an RH equivalent

Mishou and Nagoshi proved quadratic character-aspect universality for
`L(s,chi_d)` as `d` ranges over fundamental discriminants, and a
prime-discriminant version in arithmetic progressions.  The admissible
target is holomorphic and nonvanishing in the universality region and is
positive on its real slice.

In their separate paper *Equivalents of the Riemann hypothesis* they prove,
in particular, that RH is equivalent to the positive-lower-density statement

```text
max_(s in K)|L(s,chi_d)+zeta(s)|<epsilon                         (4.1)
```

for every compact `K` in `1/2<Re(s)<1` and every positive `epsilon`.
Under RH the target `-zeta` is admissible: it is nonvanishing in the strip
and is positive on the real interval.  Conversely, if `K` encloses an
off-line zero, Rouche and real-character zero density turn (4.1) into a
contradiction.

This is exactly the logical boundary encountered here.  Universality for a
zero-bearing target is not an unimported routine strengthening; in this
setting it is the result to be proved.

The primary sources are:

* H. Mishou and H. Nagoshi,
  [*Functional distribution of `L(s,chi_d)` with real characters and
  denseness of quadratic class numbers*](https://doi.org/10.1090/S0002-9947-06-03825-6),
  Trans. Amer. Math. Soc. 358 (2006), 4343--4366;
* H. Mishou and H. Nagoshi,
  [*The universality of quadratic L-series for prime
  discriminants*](https://doi.org/10.4064/aa123-2-3),
  Acta Arith. 123 (2006), 143--161; and
* H. Mishou and H. Nagoshi,
  [*Equivalents of the Riemann
  hypothesis*](https://doi.org/10.1007/s00013-005-1375-1),
  Arch. Math. 86 (2006), 419--424.

## 5. Why the upper arc does not evade the target restriction

At first sight `Gamma_+` looks ideal for universality: as a compact arc it
has connected complement.  The obstruction comes from the support of a
real-character family, not from the arc by itself.

Suppose that targets `h_d,h_e,h_(de)` are nonvanishing and holomorphic in a
simply connected conjugation-symmetric region `Omega` containing
`Gamma_+`.  Symmetry gives

```text
Gamma subset Omega.                                             (5.1)
```

An open simply connected set containing a Jordan curve contains its
interior; otherwise the curve would have nonzero winding about a point of
the complement.  Hence

```text
closure(D) subset Omega.                                        (5.2)
```

The target ratio

```text
H(s)=zeta(s)h_(de)(s)/[h_d(s)h_e(s)]                            (5.3)
```

retains every zeta zero in `D`.  Lemma 1.1 now gives, for every nonzero real
`c`,

```text
sup_(Gamma_+)|H(s)-c|>=|c|.                                    (5.4)
```

Thus targets which would make (0.1) close to a constant are not members of
the admissible support.  The target fails before any effective-density
estimate is considered.

## 6. Correlated joint universality does not change the topology

The published 2017 character-aspect theorem of Mishou and Nagoshi treats
simultaneous shared twists

```text
L(s,chi lambda_1),...,L(s,chi lambda_r)                          (6.1)
```

by fixed distinct Dirichlet characters.  Its targets are again nonvanishing
analytic functions.  It can force zeros of linear combinations, but those
are not zeros of an individual quadratic `L`-function and are not counted by
(3.1).

A 2014 Mathematical Society of Japan abstract announced joint
`d`-universality for

```text
L(s,chi_(d_1d)),...,L(s,chi_(d_rd)).                             (6.2)
```

A later grant report says that a manuscript was submitted, but no published
paper or proof was found in the authors' current publication records.  It
cannot be imported as a lemma.  Even the announced statement retains the
same symmetric, nonvanishing target restriction and therefore does not
evade Section 5.

The published shared-twist source is H. Mishou and H. Nagoshi,
[*Joint universality for Dirichlet L-functions and zeros of their linear
combinations in the character
aspect*](https://doi.org/10.1007/s00605-016-0996-8),
Monatsh. Math. 181 (2016/2017), 399--416.

## 7. A slit returns exactly the derivative debt

One can make the target admissible by deleting arcs which prevent the
universality region from surrounding `D`.  The missing winding must then be
spent on those arcs.

### Lemma 7.1 -- slit derivative cost

Let `J` be a union of omitted boundary arcs of total arclength `ell`.  If

```text
sup_(Gamma\J)|f-c|<=epsilon<|c|,
Z_D(f)-P_D(f)!=0,                                              (7.1)
```

then

```text
sup_J |f'| >=(|c|-epsilon)/ell.                                 (7.2)
```

#### Proof

If the right side of (7.2) were a strict upper bound, integrate `f'` from a
controlled endpoint across every omitted component.  The change of `f`
would be less than `|c|-epsilon`, extending `|f-c|<|c|` to all of `Gamma`.
Lemma 1.1 would then contradict (7.1).  QED.

This is the reciprocal-gap loss in R122 and R126.  Character aspect changes
the zero-density exponent on the final counting side; it does not remove the
analytic transition required to restore the contour.

## 8. Degree zero supplies no local normal-family bound

The exact conductor-one functional equation of R138 does not control the
derivative in (7.2).  A finite model makes this explicit.  For root orbits

```text
Q_a(s)=product_(u in {a,conjugate(a),1-a,1-conjugate(a)})(s-u)  (8.1)
```

choose two orbits outside `D` and put

```text
R_M(s)=[Q_a(s)/Q_b(s)]^M.                                      (8.2)
```

Then

```text
R_M(1-s)=R_M(s),
R_M(conjugate(s))=conjugate(R_M(s)),
R_M(s)->1 as |s|->infinity,                                    (8.3)
```

and `R_M` is zero- and pole-free on `D`.  Nevertheless

```text
R_M'/R_M=M[Q_a'/Q_a-Q_b'/Q_b]                                  (8.4)
```

grows linearly with `M`.  Signed cancellation of degree and conductor does
not bound the total auxiliary divisor complexity or the derivative on a
slit.

## 9. Literature boundary for the counting estimate

The zero-density inputs used in Section 3 are:

* D. R. Heath-Brown,
  [*A mean value estimate for real character
  sums*](https://ora.ox.ac.uk/objects/uuid:b188b365-d8d1-4267-8548-49f01e6cb6a7),
  Acta Arith. 72 (1995), especially Theorem 3; and
* C. C. Corrigan,
  [*A note on the zeros of L-functions associated to fixed-order Dirichlet
  characters*](https://arxiv.org/abs/2310.16518),
  Bull. Aust. Math. Soc. 110 (2024), 252--261, especially Theorem 2.1.

At fixed height, Heath-Brown supplies the first exponent in (3.3) and
Corrigan the second.  These bounds are substantially stronger for this task
than a generic all-character density theorem because the family contains
only primitive real characters.

## 10. Verdict and surviving target

The R138 pair-replication strategy no longer has an uncertain counting
stage.  A theorem producing the upper-half event

```text
sup_(Gamma_+)|F_(d,e)-c|<|c|                                   (10.1)
```

for more than

```text
Q^[-Delta(sigma_D)+o(1)]                                      (10.2)
```

of the conductor-`Q` pairs would exclude every zeta zero in `D`.

Ordinary, hybrid, prime-discriminant, and published correlated
character-aspect universality cannot prove (10.1).  Their nonvanishing
target class is topologically disjoint from it whenever `D` contains a zeta
zero.  Opening the contour makes the target admissible but returns the
quantitative derivative gate already isolated in R126.

The live theorem must therefore be genuinely different: a meromorphic or
zero-bearing pair-support theorem, a coefficient-specific signed divisor
estimate, or an exceptional Frobenius construction.  Any of these must be
strong enough to cross (10.2); restating standard universality on another
fixed compact is not sufficient.

This report proves neither a fixed zero-free strip nor the nonexistence of
one.
