# R97 nonlinear Euler and prime-zeta rigidity gate

Status: prime-level cancellation really can move a Dirichlet coefficient
`H^2` threshold left, even arbitrarily far left after higher local
renormalization.  The gain occurs exactly when the prime-zeta singularity
cancels the simple reciprocal-zeta zero at `s=1` and all reciprocal-zeta
poles in the corresponding half-plane.  Zero-preserving holomorphic scalar
transforms retain squarefree fixed-almost-prime coefficients and therefore
cannot move the `H^2` threshold below `1/2`.  A separate Euler-logarithmic
theorem shows that sparse or signed residual primes cannot evade this
conclusion when the zero is carried by the infinite prime logarithm.
Reinserting the zero with a normally convergent Dirichlet multiplier creates
recurrent artificial zeros; reinserting it with an Archimedean factor loses
vertical recurrence.  No fixed zero-free strip, and no failure of every
fixed strip, is proved.

Date: 2026-08-07.

## 1. Verdict

Let

```text
F(s)=1/zeta(s),

mathcal P(s)=sum_p p^(-s)                             (1.1)
```

in their initial half-plane of absolute convergence.  The proposed family
is

```text
G_c(s)=F(s)exp(c mathcal P(s)).                       (1.2)
```

There is a genuine phase transition.

```text
c!=1:  the prime coefficient is c-1,
        so the coefficient-Hilbert threshold is 1/2;

c=1:   every prime coefficient vanishes,
        and the threshold drops to 1/4.               (1.3)
```

At the exceptional value `c=1`, however,

```text
G_1(s)=product_p (1-p^(-s))exp(p^(-s))               (1.4)
```

is holomorphic and nonzero in `Re(s)>1/2`, including at `s=1`.  It has
cancelled the target zero rather than made it easier to recur.

This report proves the following rigidity results.

1. Near `s=1`,

   ```text
   G_c(s) asymp nonzero_factor*(s-1)^(1-c).           (1.5)
   ```

   A single-valued holomorphic `G_c` has a simple zero there only for
   `c=0`, the original reciprocal zeta.  That case has threshold `1/2`.
2. Cancelling the first `r-1` local prime-power layers produces a nonzero
   Euler product with coefficient-Hilbert threshold `1/(2r)`.  For every
   `r>=2`, it is nonzero at `1` and has removed the reciprocal-zeta
   singularities which carried the target information.
3. Let `Phi` be any holomorphic scalar transform with

   ```text
   Phi(0)=0, Phi'(0)!=0, Phi(z)!=0 for z!=0.           (1.6)
   ```

   Then `Phi(F)` retains the unique simple zero of `F`.  If its prime
   coefficient is cancelled to order `r` at `F=1`, every squarefree product
   of exactly `r` primes has the same nonzero coefficient.  Their square
   mass diverges on every line `Re(s)<=1/2`.  Infinite-order cancellation is
   impossible for a nonconstant holomorphic `Phi`.
4. In an Euler-local correction whose zero is carried by residual prime
   coefficients `r_p`, a simple zero at `1` forces their logarithmic prime
   mass to diverge.  If they were square summable on any line left of
   `1/2`, Cauchy--Schwarz would make the prime logarithm holomorphic at `1`,
   contradicting the zero.  This includes sparse residual sets and
   arbitrary signs.  A finite Euler factor which itself vanishes at `1` is
   excluded here and falls under the recurrent artificial-zero theorem.
5. More generally, every nonzero Dirichlet series with coefficient-Hilbert
   threshold strictly below `1/2` and a zero at `1` has high zeros recurring
   to `Re(s)=1`.  It therefore cannot preserve the unique zero set of
   `1/zeta`.  An Archimedean factor such as `s-1` avoids those zeros, but its
   translates do not recur or even remain locally bounded without a
   normalization that erases the anchored zero.

Thus nonlinear Euler renormalization faces an exact trilemma:

```text
retain the reciprocal zero  -> Hilbert threshold >=1/2;
lower the threshold         -> cancel the reciprocal zero;
reinsert a Dirichlet zero   -> create recurrent artificial zeros.       (1.7)
```

## 2. The exact prime-zeta calculation

For `Re(s)>1`, Euler's identity gives

```text
log zeta(s)=sum_(m>=1) mathcal P(ms)/m.               (2.1)
```

Put

```text
Q_2(s)=sum_(m>=2)mathcal P(ms)/m.                    (2.2)
```

The series in (2.2) is normally convergent in `Re(s)>1/2`.  Hence, with a
consistent logarithm initially chosen on `Re(s)>1`,

```text
G_c(s)=zeta(s)^(c-1)exp[-c Q_2(s)].                  (2.3)
```

This identity makes all singularity bookkeeping explicit.  At `s=1`,

```text
zeta(s)^(c-1) approximately (s-1)^(1-c),             (2.4)
```

while the second factor in (2.3) is holomorphic and nonzero.

**Theorem 2.1 (the exceptional cancellation parameter).**

1. `G_c` has a single-valued holomorphic continuation across `s=1` with a
   simple zero there only when `c=0`.
2. At `c=1`, `G_1=exp(-Q_2)` is holomorphic and nonzero throughout
   `Re(s)>1/2`.
3. If `c` is not an integer, the local power `(s-1)^(1-c)` is branched.  If
   `c` is an integer, its zero or pole order at `1` is `1-c`.

### Proof

All assertions follow directly from (2.3)--(2.4).  QED.

In particular, at a zeta zero `rho` with `Re(rho)>1/2`, the prime-zeta
logarithm has exactly the logarithmic singularity needed for `G_1` to cancel
the pole of `F`.  The apparent new continuation is not evidence against
`rho`; it has divided out its signal.

## 3. Dirichlet coefficients and the real threshold gain

The Euler-local coefficient at one prime is

```text
(1-z)exp(cz)=sum_(k>=0)a_c(k)z^k,                   (3.1)

a_c(0)=1,
a_c(k)=c^(k-1)(c-k)/k!                 (k>=1).       (3.2)
```

Thus

```text
a_c(1)=c-1.                                          (3.3)
```

Let `g_c(n)` be the resulting multiplicative Dirichlet coefficients and
define their Hilbert abscissa

```text
sigma_2(G_c)=inf{alpha:
 sum_n abs(g_c(n))^2 n^(-2alpha)<infinity}.          (3.4)
```

**Theorem 3.1 (exact Hilbert thresholds for `G_c`).**

```text
sigma_2(G_c)=1/2                   if c!=1,

sigma_2(G_1)=1/4.                                    (3.5)
```

### Proof

The coefficient-square series has Euler product

```text
product_p [sum_(k>=0)abs(a_c(k))^2p^(-2k alpha)].    (3.6)
```

If `c!=1`, its first nonconstant local term is

```text
abs(c-1)^2p^(-2alpha),                               (3.7)
```

so convergence is equivalent at the prime level to
`sum_p p^(-2alpha)<infinity`, namely `alpha>1/2`.

For `c=1`,

```text
a_1(1)=0,
a_1(2)=-1/2,                                         (3.8)
```

and the first local square term is `(1/4)p^(-4alpha)`.  The factorial decay
in (3.2) controls all higher powers.  Convergence is therefore equivalent to
`4alpha>1`.  QED.

This is a genuine improvement in coefficient geometry.  It simply belongs
to a function which no longer has the target zero.

## 4. Arbitrarily deep local cancellation has the same defect

For an integer `r>=2`, define

```text
E_r(s)
 =F(s)exp[sum_(m=1)^(r-1)mathcal P(ms)/m]

 =product_p (1-p^(-s))
   exp[sum_(m=1)^(r-1)p^(-ms)/m]

 =product_p exp[-sum_(m>=r)p^(-ms)/m].               (4.1)
```

Its local factor is

```text
e_r(z)=1-z^r/r+O(z^(r+1)).                           (4.2)
```

**Theorem 4.1 (higher local renormalization).**

1. `E_r` is holomorphic and nonzero in `Re(s)>1/r`.
2. Its ordinary absolute Dirichlet-series threshold is `1/r`.
3. Its coefficient-Hilbert threshold is

   ```text
   sigma_2(E_r)=1/(2r).                               (4.3)
   ```

4. `E_r(1)!=0`; the simple zero of `F` and every reciprocal-zeta pole in
   `Re(s)>1/r` have been cancelled by the prime-zeta layers.

### Proof

The logarithm in the last product of (4.1) begins with
`-sum_p p^(-rs)/r` and converges normally exactly for `r Re(s)>1`.
Exponentiating an absolutely convergent logarithmic Euler series gives an
absolutely convergent Dirichlet series there.  Conversely, the coefficient
of `p^r` is `-1/r`, so absolute convergence is impossible when
`sum_p p^(-r sigma)` diverges.  This proves the exact ordinary threshold and
nonvanishing.  The same two-sided argument applied to coefficient squares,
whose first local term is `p^(-2r alpha)/r^2`, proves (4.3).  Since `1>1/r`,
the product is normally convergent and nonzero at `s=1`.  QED.

Taking `r` large can push the formal Hilbert threshold arbitrarily close to
zero.  The limiting operation cancels every Euler-log layer and leaves the
constant function one.  Threshold improvement and loss of the zeta signal
are quantitatively identical.

## 5. Rigidity of zero-preserving holomorphic scalar transforms

Perhaps an Euler-local exponential is too destructive.  A different idea is
to apply a holomorphic map directly to `F`, chosen to have no zero except at
the origin.

Let `Phi` be holomorphic on a connected neighborhood containing `0` and `1`,
and suppose

```text
Phi(0)=0,
Phi'(0)!=0,
Phi(1)!=0.                                            (5.1)
```

The stronger zero-preserving condition `Phi(z)!=0` for `z!=0` implies
(5.1).  Write

```text
F(s)=1+U(s),
U(s)=sum_(n>=2)mu(n)n^(-s),                           (5.2)

Phi(1+u)=sum_(j>=0)b_j u^j.                          (5.3)
```

Because `Phi` is nonconstant, there is a finite integer

```text
r=min{j>=1:b_j!=0}.                                  (5.4)
```

**Theorem 5.1 (squarefree residual rigidity).**  Let

```text
Phi(F(s))=sum_(n>=1)A_Phi(n)n^(-s)                  (5.5)
```

in a far-right half-plane.  For every squarefree

```text
n=p_1...p_r
```

with exactly `r` distinct prime factors,

```text
A_Phi(n)=b_r(-1)^r r! !=0.                           (5.6)
```

Consequently

```text
sum_n abs(A_Phi(n))^2n^(-2alpha)=infinity

for every alpha<=1/2.                                (5.7)
```

Thus no nonconstant holomorphic zero-preserving scalar transform of `F` can
move its coefficient-Hilbert threshold strictly left of `1/2`.

### Proof

The series `U` has no constant coefficient.  To produce a squarefree integer
with exactly `r` primes from `U^r`, every convolution factor must receive
one prime.  There are `r!` ordered assignments and each contributes
`(-1)^r`.  Terms `U^j` with `j<r` have zero Taylor coefficient by (5.4),
while terms with `j>r` cannot factor `n` into more than `r` nontrivial
integers.  This proves (5.6).

The subseries in (5.7) contains a fixed positive multiple of

```text
sum_(p_1<...<p_r)(p_1...p_r)^(-2alpha).              (5.8)
```

It diverges whenever `sum_p p^(-2alpha)` diverges, in particular for
`alpha<=1/2`.  QED.

The example

```text
Phi(z)=z exp(1-z)                                    (5.9)
```

is instructive.  It has only the zero `z=0` and

```text
Phi(1+u)=(1+u)exp(-u)=1-u^2/2+u^3/3-... .           (5.10)
```

Every prime coefficient vanishes, but every squarefree semiprime `pq` has
coefficient `-1`.  Thus cancelling the prime layer has not moved the lower
barrier `1/2`; no upper-bound claim for the complete coefficient series is
needed here.

Trying to cancel all fixed-almost-prime layers would require every derivative
of `Phi` at `1` to vanish.  Analyticity would make `Phi` constant on the
connected domain, contradicting the simple zero at `0`.  This is the scalar
holomorphic rigidity behind (5.7).

## 6. Sparse and signed residual primes cannot evade the threshold

The preceding theorem treats transforms depending only on the scalar value
`F(s)`.  Prime-dependent corrections can cancel different primes by
different amounts, so a separate statement is needed.

Consider a normalized Euler-local product, initially for `Re(s)>1`,

```text
G(s)=product_p g_p(p^(-s)),                           (6.1)

log g_p(z)=-r_p z+O(C_p abs(z)^2),                   (6.2)
```

with coherent logarithm branches there.  Require explicitly that the
summed remainder has a regular continuation through `s=1`: for real
`sigma>1`,

```text
log G(sigma)=-sum_p r_p p^(-sigma)+R(sigma),         (6.3)
```

where `R` extends holomorphically to a neighborhood of `1`.  Equivalently,
the quadratic Euler remainder is normally summable there and no finite
Euler factor or separate analytic prefactor supplies the zero.  The
coefficient of `p^(-s)` in `G` is `-r_p`.

**Theorem 6.1 (residual-prime Hilbert rigidity).**  Under the explicit
logarithmic-remainder hypothesis above, suppose `G` extends holomorphically
to `s=1` and has a simple zero there.  Then, for every `alpha<1/2`,

```text
sum_p abs(r_p)^2p^(-2alpha)=infinity.                (6.4)
```

In particular the coefficient-Hilbert abscissa of `G` is at least `1/2`,
regardless of sparsity or signs in the residual primes whose infinite
logarithm carries the zero.

### Proof

Along the real axis `sigma->1+`, a simple zero gives

```text
log abs(G(sigma))=log(sigma-1)+O(1).                 (6.5)
```

The remainder `R` in (6.3) remains bounded, so

```text
Re sum_p r_p p^(-sigma)
 =log[1/(sigma-1)]+O(1).                             (6.6)
```

Assume (6.4) fails for some `alpha<1/2`.  Cauchy--Schwarz gives

```text
sum_p abs(r_p)p^(-sigma)

 <=[sum_p abs(r_p)^2p^(-2alpha)]^(1/2)
   [sum_p p^(-2(sigma-alpha))]^(1/2).                (6.7)
```

The second factor is finite whenever

```text
sigma>alpha+1/2.                                     (6.8)
```

This is a half-plane containing `s=1`.  Hence the prime logarithm would be
absolutely convergent and bounded at `1`, contradicting (6.6).  QED.

For a correction

```text
F(s)exp(sum_p c_p p^(-s)+higher_prime_powers),       (6.9)
```

one has `r_p=1-c_p`.  Cancelling all but a sparse set means `r_p` is
supported on that set.  If its prime harmonic mass is finite, the zero at
`1` disappears.  If it is large enough to retain a simple zero, (6.3)
forces the same `1/2` Hilbert barrier.  Signed choices cannot help because
the simple-zero asymptotic fixes the divergent real part in (6.6), while
Cauchy--Schwarz sees their absolute square mass.

The nonvanishing-log hypothesis is essential.  The one-factor example

```text
1-2^(1-s)                                             (6.10)
```

has a simple zero at `1` and only finite prime support, but its logarithm is
singular at `1`; the zero is supplied by that finite factor rather than by
the infinite residual-prime tail.  It has zeros on the entire lattice
`1+2 pi i k/log 2`, so it is precisely the recurrent artificial-zero case
handled in Section 7, not a counterexample to the qualified theorem.

## 7. Reinserting the zero creates the missing obstruction elsewhere

The low-threshold products `E_r` are nonzero at `1`.  There are two obvious
ways to put a simple zero back.

First record a general consequence of the recurrence theorem already proved
in R91.

**Theorem 7.1 (universal low-Hilbert recurrent-zero obstruction).**  Let

```text
T(s)=sum_(n>=1)t_n n^(-s)                              (7.1)
```

be nonzero, and suppose its coefficient-Hilbert abscissa satisfies

```text
sigma_2(T)<1/2.                                       (7.2)
```

If `T(1)=0`, then `T` has zeros `s_j` such that

```text
abs(Im(s_j))->infinity,             Re(s_j)->1.       (7.3)
```

Consequently no such `T` can have exactly the zero set of `1/zeta` in a
fixed neighborhood of the line `Re(s)=1`.

### Proof

Choose

```text
sigma_2(T)<alpha<1/2
```

so that `sum_n abs(t_n)^2 n^(-2 alpha)<infinity`, and then choose

```text
0<eta_0<1/2-alpha.                                   (7.4)
```

Cauchy--Schwarz gives

```text
sum_n abs(t_n)n^(-1+eta_0)
 <=[sum_n abs(t_n)^2n^(-2alpha)]^(1/2)
   [sum_n n^(-2(1-eta_0-alpha))]^(1/2)<infinity.     (7.5)
```

Thus the Dirichlet series is normally convergent in a fixed half-plane
strictly left of `1`.  Theorem 6.2 of
`R91-ETA-POSITIVE-INTERVAL-NONVANISHING-GATE.md` now gives (7.3).
The meromorphic function `1/zeta` has only one zero, at `s=1`, because that
is the only pole of zeta.  Hence a zero-set-preserving carrier cannot have
the high zeros in (7.3).  QED.

This theorem shows that the obstruction is not specifically Eulerian.  Any
Dirichlet-series transform which achieves the desired sub-half threshold
and retains the anchored zero necessarily manufactures other zeros.

### 7.2 A Dirichlet multiplier creates recurrent artificial zeros

Let

```text
T(s)=B(s)E_r(s),                                     (7.6)
```

where `B` is a nonzero Dirichlet series, normally convergent in a fixed
neighborhood to the left of `Re(s)=1`, and `B(1)=0`.  Theorem 6.2 of
`R91-ETA-POSITIVE-INTERVAL-NONVANISHING-GATE.md` gives zeros `s_j` of `B`
with

```text
abs(Im(s_j))->infinity,
Re(s_j)->1.                                          (7.7)
```

Since `E_r` is nonzero, these are zeros of `T`.  They are zeros of the
inserted multiplier, not poles or zeros of zeta.  Thus `T` no longer has the
translate-zero-free property required by the reciprocal recurrence
argument.

The elementary choice

```text
B(s)=1-2^(1-s)                                       (7.8)
```

makes the problem visible immediately: it has an entire vertical lattice of
zeros on `Re(s)=1`.

### 7.3 An Archimedean zero destroys vertical recurrence

The function

```text
T_r(s)=(s-1)E_r(s)                                   (7.9)
```

has a simple zero at `1` and no other zero in `Re(s)>1/r`.  It is not a
Dirichlet almost-periodic carrier.  On any line `Re(s)=sigma>1`, the normally
convergent Euler product `E_r(s)` is bounded above and bounded away from zero
uniformly in height, whereas

```text
abs(s+i tau-1) asymp abs(tau).                       (7.10)
```

Hence its vertical translates are not locally bounded, much less recurrent
to `T_r`.  Dividing by `i tau` restores boundedness but makes

```text
(s+i tau-1)/(i tau)->1,                              (7.11)
```

so the limiting function has lost the zero at `s=1`.  The Archimedean factor
anchors the zero precisely by breaking the recurrence intended to copy it.

## 8. Consequence for Dirichlet `H^2` recurrence

The R96 Mobius--Besicovitch audit showed that coefficient `H^2` recurrence
requires a half-unit horizontal shift before point evaluation becomes
bounded.  A successful threshold below `1/2` could therefore have opened a
disc around `s=1`.

The results above show why the promising calculation does not do so.

```text
transform                         sigma_2       zero at 1

F=1/zeta                          1/2           simple
G_1=F exp(mathcal P)              1/4           absent
E_r                               1/(2r)        absent
Phi(F), Phi zero-preserving       >=1/2         simple
B E_r, B(1)=0                     possibly low  recurrent artificial zeros
(s-1)E_r                          not a fixed
                                  Dirichlet H2   simple, no recurrence.     (8.1)
```

For scalar zero-preserving transforms, the half-unit point-evaluation tax
therefore still places generic compact recurrence strictly to the right of
`Re(s)=1`.  For Euler-renormalized transforms, the coefficient space is
better but there is no target zero to recur.

A height-dependent parameter `c=c(t)` does not interpolate between the two
outcomes.  For every fixed nonzero residual `c-1`, the prime square mass has
threshold `1/2`; at the exact value `c=1`, the zero disappears.  Allowing the
transform itself to vary with height destroys the fixed holomorphic family
needed by Rouché or Hurwitz, and its degenerating constants merely encode
the same singular limit.

## 9. Disposition

This report proves the following reusable conclusions.

1. Prime-zeta cancellation at `c=1` genuinely lowers the Hilbert threshold
   to `1/4`, but exactly cancels the reciprocal-zeta zero and poles.
2. Cancelling `r-1` Euler-log layers lowers the threshold to `1/(2r)` while
   producing a nonzero product at `s=1`.
3. Every nonconstant holomorphic zero-preserving scalar transform retains a
   nonzero layer of squarefree fixed-almost-prime coefficients, forcing
   threshold at least `1/2`.
4. Sparse and signed prime-dependent corrections obey the same barrier if
   their infinite prime logarithm retains the simple zero at `1`; finite
   vanishing factors instead create recurrent artificial zeros.
5. Universally, any Dirichlet series with Hilbert threshold below `1/2`
   and a zero at `1` has recurrent high zeros; it cannot preserve the
   reciprocal-zeta zero set.
6. An Archimedean factor restores the zero only by destroying vertical
   recurrence.

No loophole remains in the tested nonlinear Euler/prime-zeta class.  A new
route would have to leave the low-threshold Dirichlet-carrier framework
entirely: Theorem 7.1 shows that even a non-Eulerian carrier with the desired
coefficient threshold and anchored zero necessarily has recurrent high
zeros.  Avoiding that theorem means giving up the normality which was meant
to turn coefficient recurrence into pointwise control.
