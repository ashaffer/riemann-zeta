# R122 zero-replication density gate

Status: a quantitative Rouche replication lemma is proved and matched to
the imported zero-density exponent.  Positive-density self-recurrence on a
disc containing an off-line zero would contradict zero density, but this is
Bagchi's strong-recurrence criterion and is RH-equivalent.  Ordinary,
hybrid, and effective universality exclude precisely the vanishing target
needed for that step.  Finite Euler products have the wrong winding number.
Every fixed R120 smooth-Mobius detector bank is genuinely Bohr recurrent,
but finite-bank recurrence reproduces detector values rather than zeta
divisors; the zero-detecting implication needs an unbounded separating bank,
whose recurrence density is not uniform.  A punctured-contour construction
reduces a possible workaround to one explicit joint universality/derivative
density inequality, not presently available.  No fixed strip, and no
failure of every fixed strip, is proved.

Date: 2026-08-07.

Predecessors:

* [`R98-QUASI-RH-BOOTSTRAP-GATE.md`](R98-QUASI-RH-BOOTSTRAP-GATE.md)
  for the individual-zero versus aggregate-density obstruction;
* [`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md)
  for the faithful `Q_h` zero multiplier;
* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md)
  for the primitive smooth-Mobius reduction; and
* [`R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md`](R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md)
  for the exact signed Mellin kernel and separating-bank qualification.

## 1. Verdict

There is a rigorous zero-replication mechanism.  Let

```text
rho_0=beta+i gamma_0
```

be an off-line zero and let `D=D(rho_0,r)` be a closed disc lying in
`1/2<Re(s)<1`, with no zero on its boundary.  Put

```text
m_D=min_(s in boundary D)|zeta(s)|>0.                 (1.1)
```

Every shift `tau` for which

```text
sup_(s in boundary D)|zeta(s+i tau)-zeta(s)|<m_D      (1.2)
```

holds creates, by Rouche's theorem, a translated off-line zero.  Moreover,
the measure of such shifts is at most a constant times the corresponding
zero count.  Thus a recurrence set of size `T^(kappa+o(1))` contradicts a
zero-density bound of exponent strictly below `kappa`.

This clean implication does not supply recurrence.  The known theorems
divide exactly at (1.2):

```text
ordinary/hybrid universality        nonvanishing target only;
Bagchi strong self-recurrence       permits (1.2), but is RH-equivalent;
finite Euler-product recurrence     positive density, wrong winding;
finite R120 detector recurrence     positive density, no inverse zero map;
Turan power recurrence              repeats one carrier, not its divisor.
                                                               (1.3)
```

The closest noncircular workaround found here is to apply unconditional
self-universality on a boundary circle with a small arc deleted.  A
derivative bound fills the missing arc and restores Rouche.  If the deleted
arc has length `ell`, the needed derivative threshold is of order `1/ell`.
The off-line-zero hypothesis then forces the density of those punctured
recurrences to be `O(ell^2)` by the classical second moment of `zeta'`.
Empty-interior universality gives only an unspecified positive density,
with no lower bound that beats `ell^2`.  This is an exact quantitative gate,
not a proof.

## 2. Quantitative Rouche replication

Let `rho_0` be a zero of multiplicity `j>=1`.  Choose

```text
0<r<min(beta-1/2,1-beta)                              (2.1)
```

so that `zeta` has no zero on `boundary D`, where
`D={s:abs(s-rho_0)<=r}`, and shrink it further so that `rho_0` is its only
zero.  For `0<epsilon<m_D`, define

```text
A_D(T,epsilon)
 ={tau in [T,2T]:
   sup_(s in boundary D)|zeta(s+i tau)-zeta(s)|<epsilon}.
                                                               (2.2)
```

### Theorem 2.1 -- recurrence measure is bounded by zero count

With multiplicities counted,

```text
j meas A_D(T,epsilon)
 <=2r N(beta-r;
        T+gamma_0-r,2T+gamma_0+r).                   (2.3)
```

Here the last expression counts zeros with real part at least `beta-r`
and ordinate in the displayed interval.

**Proof.**  For each `tau` in (2.2), Rouche gives exactly `j` zeros of
`zeta(s+i tau)` inside `D`, hence exactly `j` zeros of `zeta` inside
`D+i tau`.  Therefore

```text
j 1_(A_D)(tau)
 <=sum_rho 1_(abs[rho-(rho_0+i tau)]<r),              (2.4)
```

where the sum includes multiplicity.  Integrate over `[T,2T]` and
interchange the nonnegative sum and integral.  A fixed zero can lie in
`D+i tau` for a set of `tau` of length at most `2r`.  Every such zero has
`Re(rho)>=beta-r` and lies in the stated ordinate interval.  This proves
(2.3).  QED.

The imported Guth--Maynard corollary in R98 is

```text
N(sigma,T)<=T^[d(sigma)+o(1)],
d(sigma)=30(1-sigma)/13.                              (2.5)
```

Consequently Theorem 2.1 gives

```text
meas A_D(T,epsilon)
 <=T^[d(beta-r)+o(1)].                                (2.6)
```

In particular, a theorem

```text
meas A_D(T,epsilon)>=T^(kappa-o(1))                   (2.7)
```

would exclude the zero whenever

```text
kappa>d(beta-r).                                      (2.8)
```

Equivalently, such recurrence would force the explicit line

```text
beta<=1-13kappa/30+r.                                 (2.9)
```

For positive-density recurrence, `kappa=1`, (2.5) already contradicts an
off-line zero with `beta-r>17/30`.  The classical Bohr--Landau density
theorem `N(sigma,T)=o(T)` for each fixed `sigma>1/2` strengthens this:
positive-density recurrence around every such disc excludes every zero to
the right of `1/2`.

This last statement is not a new RH argument.  It is the converse half of
Bagchi's theorem: RH is equivalent to positive-lower-density
self-approximation of `zeta` on every compact subset of
`1/2<Re(s)<1` with connected complement.  A convenient primary statement
is Theorem A of Nakamura--Pankowski,
[Self-approximation for the Riemann zeta
function](https://doi.org/10.1017/S0004972712000846).  Bagchi's original
source is [A joint universality theorem for Dirichlet
L-functions](https://doi.org/10.1007/BF01161980).

Theorem 2.1 is useful nonetheless: any proposed weaker recurrence theorem
can now be graded by the single exponent inequality (2.8).

## 3. Why ordinary and hybrid universality stop exactly short

Voronin universality supplies positive lower density for

```text
sup_(s in K)|zeta(s+i tau)-f(s)|<epsilon              (3.1)
```

when `f` is continuous on `K`, holomorphic inside, and **nonvanishing** on
`K`.  The effective theorem of Lamzouri--Lester--Radziwill retains the same
hypothesis; see [An effective universality theorem for the Riemann
zeta-function](https://arxiv.org/abs/1611.10325), Theorem 1.1.  Hybrid
universality adds finitely many prime-phase constraints but does not remove
the target's nonvanishing condition; the zero-free and strong variants
remain distinct in [Discrete universality, continuous universality and
hybrid universality are equivalent](https://arxiv.org/abs/2310.03619).

For `f=zeta` on the disc in Section 2, that condition fails.  It cannot be
repaired by a small perturbation.  If

```text
sup_(s in boundary D)|f(s)-zeta(s)|<m_D,              (3.2)
```

then Rouche says that `f` has the same `j` zeros in `D`.  Thus every
nonvanishing admissible target obeys the topological lower bound

```text
sup_(s in boundary D)|f(s)-zeta(s)|>=m_D.             (3.3)
```

The approximation precision required for zero replication and the
nonvanishing target class are disjoint.

This also disposes of two tempting perturbations.

1. For small constants `a`, `zeta+a` still has `j` zeros in `D`; it is not
   an admissible target.
2. An exponential target `exp(g)` is nonvanishing, but (3.3) prevents it
   from approximating the zero-containing boundary inside the Rouche
   threshold.

The dynamical formulation says the same thing.  The limiting random Euler
product lives on nonvanishing holomorphic functions.  A translate
containing an off-line zero is an exceptional state outside that support.
Ergodic recurrence applies to typical supported states, not to this
prescribed zero-containing state.  Proving its recurrence is exactly the
strong-recurrence/RH step.

## 4. Finite Euler products: recurrence with the wrong winding

For fixed `y`, put

```text
E_y(s)=product_(p<=y)(1-p^(-s))^(-1).                 (4.1)
```

It is uniformly almost periodic in the vertical variable on compact
subsets of `Re(s)>0`.  The numbers `log p/(2pi)` are rationally independent,
so Kronecker--Weyl gives a positive-density set of shifts which return all
of its prime phases close to their starting values.

But `E_y` is nonzero and holomorphic on the disc `D` of Section 2.  Hence
(3.3) gives, for every finite cutoff `y`,

```text
sup_(s in boundary D)|E_y(s)-zeta(s)|>=m_D.           (4.2)
```

No choice of cutoff crosses the Rouche threshold.  In logarithmic form the
obstruction is the exact winding ledger

```text
1/(2pi i) integral_(boundary D) zeta'(s)/zeta(s) ds=j,

1/(2pi i) integral_(boundary D) E_y'(s)/E_y(s) ds=0. (4.3)
```

Approximations to `log zeta` by short Euler products therefore delete
neighborhoods of zeros before choosing a branch.  The known exceptional
set is not a technical nuisance here: the prescribed base shift containing
`rho_0` necessarily belongs to it.

A general finite Dirichlet polynomial may have zeros and may approximate
`zeta` at one fixed height.  That does not help either.  To transfer its
Bohr recurrence to `zeta(s+i tau)` at large `tau`, one also needs a uniform
approximation of the shifted zeta function.  An approximate functional
equation has a length growing as a positive power of the shifted height,
and its dual/gamma term is not returned by merely recurring finitely many
prime phases.  This is the analytic-continuation error hidden by a naive
finite-sum argument.

## 5. What really recurs in the R120 detector

R120's recompleted coefficient is

```text
C(n)=(mu*Lambda)(n)=-mu(n)log n.                      (5.1)
```

One basic smooth Mellin polynomial is

```text
B_(X,w)(t)
 =sum_n C(n)n^(-1/2)w(n/X)n^(it).                    (5.2)
```

The actual primitive `g=1` term retains `1_((c,n)=1)`.  Its exact
diagonalization therefore has the sector form

```text
P_X(0)=1/(2pi)int lambda_P(tau)
          sum_d mu(d)|B_(d,X)(tau)|^2 d tau,          (5.3)

B_(d,X)(tau)
 =sum_a C(da)(da)^(-1/2)w(da/X)a^(i tau),             (5.4)
```

with the ratio profile depending on the gcd sector in the full R81
decomposition.  The multiplier `lambda_P` is real but signed.  Accordingly
one scalar `P_X` is not a positive zero detector.  The valid zero response
belongs to the complete separating Hermitian bank/full reconstructed
energy.

For that bank, a zero `rho=beta+i gamma` contributes at scale `X`
schematically as

```text
X^(beta-1/2) q_h(rho-1/2),

q_h(rho-1/2)
 =[exp(h(rho-1/2))-exp(h/2)]^2 !=0.                  (5.5)
```

The bank has no common Mellin zero, so a uniform positive-energy bound at
all large `X` detects the divisor and yields the exponent implication in
R120.  The words **all large `X`**, **separating bank**, and **positive
energy** cannot be dropped.

### 5.1 Every fixed cutoff really is recurrent

Fix `X`, a finite profile bank, and let `N` contain every active integer.
For `0<delta<1/2`, define

```text
R_N(delta)
 ={tau: norm[tau log p/(2pi)]<delta for every p<=N}. (5.6)
```

Unique factorization proves rational independence of the `log p`.
Kronecker--Weyl therefore gives the exact limiting density

```text
lim_(T->infinity)meas[R_N(delta) intersect [0,T]]/T
 =(2delta)^pi(N)>0.                                   (5.7)
```

For every `n<=N`,

```text
abs(n^(i tau)-1)
 <<delta Omega(n)<<delta log N.                       (5.8)
```

Thus all finite polynomials (5.2)--(5.4), and every finite R120 bank made
from them, return uniformly close to their starting values on a
positive-density set.  This fact is unconditional and completely
rigorous.

It does **not** replicate a zeta zero.  At fixed `X`, (5.2) is just an
entire trigonometric polynomial in `t`.  A large value is a consequence of
a nearby zero in the forward explicit-formula argument, but it is not a
converse divisor certificate.  If fixed-bank value recurrence implied a
zero, (5.7) would already prove positive-density zero replication and hence
RH by Theorem 2.1.  The missing inverse is exactly the passage from a
finite projection to the unbounded Mellin family.

### 5.2 The density is not uniform through the zero-detecting limit

The elementary phase ledger makes the loss visible.  On a dyadic block,

```text
sum_(n asymp X)|C(n)|n^(-1/2)<<sqrt(X)log X.          (5.9)
```

Equations (5.8)--(5.9) give a recurrence error

```text
<<delta sqrt(X)log^2 X.                               (5.10)
```

To preserve a carrier of order `X^(beta-1/2)` by this worst-case phase
return, one needs

```text
delta<<X^(beta-1)/log^2 X.                            (5.11)
```

Substitution in (5.7), using `pi(X)~X/log X`, gives for fixed `beta<1`

```text
log density R_X(delta)
 <=-[1-beta+o(1)]X.                                   (5.12)
```

For every fixed `X` the density is still positive.  As the bank is enlarged
through the scales needed to identify a pole, it collapses exponentially
and no positive lower density survives.  Recurrence sets for successive
`X` are also different; one cannot infer that a fixed translated point
shadows the complete unbounded detector.

This is the exact finite-versus-complete split:

```text
finite bank:       Bohr recurrence PROVED, no valid zero converse;
unbounded bank:    divisor separating, uniform recurrence ABSENT;
uniform power:     fixed-strip theorem itself.                       (5.13)
```

The signed multiplier in (5.3) makes one more shortcut invalid: recurrence
of a single scalar primitive form can reproduce a cancellation between
positive and negative Mellin sectors.  Only the separating Hermitian bank
has the R120 zero implication.

## 6. Turan and scale recurrence do not create new ordinates

A zero carrier in a smooth explicit formula has the form

```text
X^(beta-a) M(rho) exp(i gamma log X),                 (6.1)
```

with a detector-dependent normalization `a` and nonzero Mellin response
`M(rho)`.  Turan power sums guarantee that finitely many such carriers
cannot cancel at every member of a controlled scale block.  Bohr recurrence
of the phase in `log X` gives many further scales at which the **same**
carrier has a similar phase.

Neither operation changes `gamma`.  One pole of a Mellin transform is
supposed to generate an oscillation on infinitely many physical scales.
Counting those oscillations as distinct zeros would count the same residue
infinitely often.  Zero-density estimates count distinct vertical
ordinates, not large prime/Mobius remainders as `X` varies.

This also explains why combining Turan with R98's conditional PNT does not
contract the edge.  The lower carrier has exponent `beta`; the permitted
arithmetic envelope has exponent `Theta`.  Repeating the phase changes
neither exponent and gives a contradiction only for `beta>Theta`, exactly
as recorded in R98.

### 6.1 Replication across imprimitive families is only relabeling

There is a different literal way to manufacture many copies of one zeta
zero.  For every modulus `q`, the principal-character function is

```text
L(s,chi_(0,q))
 =zeta(s) product_(p|q)(1-p^(-s)).                    (6.2)
```

Every nontrivial zeta zero is therefore a zero of all these imprimitive
functions, apart from no possible cancellation because the finite Euler
factors are nonzero in `Re(s)>0`.  Likewise, every Dedekind zeta function
whose factorization contains `zeta(s)` inherits the zero.

This does not challenge a family zero-density theorem.  All principal
characters in (6.2) are induced from the single primitive character of
conductor one.  Primitive-family counts record that divisor once.  If one
instead counts every imprimitive label, the family cardinality/diagonal in
the upper bound grows by the same multiplicity.  Dedekind products have the
same explicit common-factor issue.  Removing the common zeta factor removes
the replicated zero.

Thus algebraic copies in other functions are not new vertical ordinates of
`zeta` and cannot be inserted into the left side of Theorem 2.1.  A useful
replication theorem must create distinct zeros of the same primitive zeta
function, not aliases carrying a visible common factor.

## 7. A genuine workaround: puncture the contour

There is an unconditional self-universality theorem on compact sets with
empty interior.  Andersson proves that if `K` has connected complement and
no interior points, every continuous target on `K` is approximated by zeta
shifts on a set of positive lower density; see [Lavrentiev's approximation
theorem with nonvanishing polynomials and universality of
zeta-functions](https://arxiv.org/abs/1010.0386), Theorem 2 and Corollary 2.
For the boundary arc below, `zeta` is already nonzero, so ordinary Voronin
universality would suffice.  The real gain is removing the interior of the
disc and opening its separating boundary, not invoking a vanishing target
on the arc.

Apply this to almost all of the Rouche contour.  Let `Gamma=boundary D` and
delete an open arc `J_ell` of arclength `ell`; its complement

```text
K_ell=Gamma\J_ell                                    (7.1)
```

is a compact arc with connected complement and empty interior.  For each
fixed `ell>0` and `epsilon>0`, Andersson gives

```text
liminf_(T->infinity) meas U_(ell,epsilon;T)/T
 =c_(ell,epsilon)>0,                                  (7.2)

U_(ell,epsilon;T)
 ={tau in [0,T]:
   sup_(s in K_ell)|zeta(s+i tau)-zeta(s)|<epsilon}.
```

This gets around the nonvanishing-target restriction on the observed arc.
It does not yet control the missing arc.

### Proposition 7.1 -- derivative completion gate

Put

```text
H_tau(s)=zeta(s+i tau)-zeta(s).                       (7.3)
```

If `tau` lies in `U_(ell,epsilon;T)` and

```text
sup_(s in J_ell)|H_tau'(s)|<=M,                       (7.4)
```

then

```text
sup_(s in Gamma)|H_tau(s)|<=epsilon+M ell.            (7.5)
```

Indeed, integrate `H_tau'` along the omitted arc from its nearest endpoint.
Thus

```text
epsilon+M ell<m_D                                    (7.6)
```

restores (1.2) and replicates the zero.

The derivative has the uniform second-moment bound

```text
integral_0^T sup_(s in J_ell)
 |zeta'(s+i tau)|^2 d tau<<_D T.                     (7.7)
```

To see this, enclose `Gamma` in a fixed compact neighborhood still lying
in `Re(s)>1/2`, apply Cauchy's estimate/subharmonicity on finitely many
small discs, integrate in `tau`, and use the classical uniform second
moment of `zeta` on every closed substrip to the right of `1/2`.  The fixed
term `zeta'(s)` is harmless.  Chebyshev therefore gives

```text
meas{tau in [0,T]:sup_(J_ell)|H_tau'|>M}
 <<_D T/M^2.                                          (7.8)
```

Choose, for example,

```text
epsilon=m_D/4,
M=m_D/(2ell).                                         (7.9)
```

Then every shift in `U_(ell,epsilon;T)` outside an exceptional set of
measure

```text
<<_D T ell^2/m_D^2                                   (7.10)
```

replicates the zero.  By the `[0,T]` version of the same proof as Theorem
2.1 and `N(beta-r,T)=o(T)`, an off-line zero consequently forces the
quantitative upper constraint

```text
c_(ell,m_D/4)<<_D ell^2/m_D^2.                        (7.11)
```

Equation (7.11) is the sharp new gate exposed by this audit.  A lower bound

```text
c_(ell,m_D/4)>>_D ell^alpha,
alpha<2,                                              (7.12)
```

along arbitrarily small `ell`, or any joint universality theorem which
puts a positive fraction of (7.2) inside the moderate-derivative event,
would contradict the assumed off-line zero.  With the power-density
version of Theorem 2.1 one can similarly grade sublinear joint sets.

No available theorem supplies (7.12).  Empty-interior universality states
only that `c_(ell,epsilon)` is positive for each **fixed** arc.  Its proof
first approximates the target on `K_ell` by a nonvanishing polynomial and
then applies ordinary universality.  As the gap closes, that polynomial
must unwind the zero through the shrinking gap; its complexity and the
resulting universality constant are uncontrolled.  Choosing `ell` after
learning `c_(ell,epsilon)` is circular because changing `ell` changes the
recurrence set and its density.  Effective universality for a fixed
nonvanishing target does not give the missing uniform lower bound through
this degenerating family.

Thus the punctured contour is a real workaround to the qualitative target
restriction, but derivative completion restores the same quantitative
content as strong recurrence.  It is a useful narrowly stated research
target, not an RH proof.

## 8. Exponent and failure ledger

```text
hypothetical zero rho_0                         one prescribed divisor;
full-disc self-recurrence                       would replicate divisor;
recurrence measure T^kappa                      needs kappa>d(beta-r);
positive-density full recurrence                Bagchi/RH-equivalent;
ordinary/hybrid universality                    target must be nonzero;
finite Euler product                            zero winding exactly;
fixed R120 detector bank                        Bohr recurrent exactly;
fixed detector value -> nearby zero             no converse;
unbounded separating R120 bank                  fixed-strip strength;
Turan/scale recurrence                          repeats same residue;
punctured-contour universality                   positive density proved;
moderate derivative on missing arc              required jointly;
needed punctured density lower rate              OPEN.                 (8.1)
```

The proposed global escape therefore does not currently yield a strict
bound on `beta`.  It does identify two precise statements which would:

1. a local self-recurrence estimate (2.7) with
   `kappa>d(beta-r)` for every putative near-one zero disc; or
2. the punctured-contour joint estimate (7.12), or an equivalent positive
   lower density after imposing the derivative cap (7.4).

The first is a quantitative fragment of Bagchi strong recurrence.  The
second avoids asking for full-disc recurrence at the outset, but its
missing density comparison is forced by the winding number and is of the
same individual-zero strength.

No result in this report shows that a fixed zero-free strip exists.  It
also gives no evidence that such a strip is impossible.  It rules out the
claim that Bohr recurrence of a finite smooth detector, universality with a
nonvanishing target, or repeated Turan peaks already replicate a zeta zero.
