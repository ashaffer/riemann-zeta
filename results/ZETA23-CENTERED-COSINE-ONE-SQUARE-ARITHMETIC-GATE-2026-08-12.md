# The centered cosine one-square: a sinh-tent scalar and two rigorous no-go reductions

Status: exact centered-carrier and two-abscissa reduction, rigorous Arb
counterexample to pointwise evenized Herglotz positivity, exact zero-density
obstruction to local positive height averaging, and expanded actual-coefficient
fail-fast, 2026-08-12.  The one-square sign itself is not proved or falsified.
No zero-free strip or new zeta-zero bound is claimed.

## 1. Verdict

Centered even parity removes the geometric anchor loss, but it does not
remove the arithmetic difficulty.  This audit produces four precise results.

1. For even endpoint order the full carrier is exactly the endpoint
   projection of

   ```text
   y_k=k/(k^2+q^2),                 q=alpha*L/(2*pi),
   ```

   and is independent of the center height `gamma`.  The selected positive
   row is even, so its constraint is automatic on this odd state.

2. On the two-sided full sharp lattice, before endpoint projection, the
   state has a closed physical model: up to a nonzero scalar its synthesis is
   the Fourier transform of

   ```text
   f_(L,alpha)(x)=sinh(alpha*x)*1_(|x|<=L/2).         (1.1)
   ```

   Its prime correlation collapses exactly to one linear combination of the
   truncated logarithmic-derivative polynomial and its `sigma` derivative at
   the two abscissae `1/2+/-alpha+i*gamma`.  Thus the remaining arithmetic
   input is a named, one-dimensional **centered sinh-tent restricted Weil
   inequality**, not an unspecified matrix law.

3. The tempting pointwise Herglotz proof is false for actual von Mangoldt
   coefficients.  A rigorous Arb computation gives

   ```text
   T=4096, gamma=6144, s=-1105.1008,

   1+[nu_T(gamma+s)+nu_T(gamma-s)]/2
    =[-0.52354227980134224484188384418155744655911009695
       +/- 8.5e-50].                                  (1.2)
   ```

   The internal replay at 80 digits has radius below `9e-75`; (1.2) is
   deliberately rounded outward.  Parity therefore does **not** turn the
   shifted completed multiplier into a pointwise nonnegative one.

4. Positive height averaging confined to a carrier-local window cannot null
   the prime phases.  If an averaging probability is supported in `[-H,H]`,
   its characteristic function has at most

   ```text
   4*H*R/(pi*log 2)                                  (1.3)
   ```

   zeros in `|z|<=R`.  Nulling all `log p`, `p<=T`, forces
   `H >> T/(log T)^2`; in particular `H=O(1)` is impossible.  Allowing remote
   mass while keeping an aligned atom reduces exactly to the positive
   prime-log central-atom moment problem already isolated elsewhere.

No actual negative one-square was found.  A new gamma-resolved scan tested
286,276 centered full-carrier configurations and found every **unshifted**
value positive.  A separate 5,552-configuration scan found the entire
endpoint-constrained odd compression positive in every tested case.  These
are diagnostics, not interpolation or asymptotic theorems.

## 2. The finite centered carrier is independent of height

Put

```text
tau_k=gamma+h*k,        h=2*pi/L,        -J<=k<=J,
q=alpha/h.
```

After the sharp-grid sign conjugation, the selected reflected-pair row is a
positive common scalar times

```text
x_k+i*y_k=q/(k^2+q^2)+i*k/(k^2+q^2).                (2.1)
```

Let `W_m` be the kernel of the first `m` coordinate moments.  Reflection
preserves `W_m`.  If `m` is even, then `P_(W_m)y` is odd and `P_(W_m)x` is
even.  Hence

```text
<P_(W_m)y,x>=0,
P_(W_m intersect ker x)y=P_(W_m)y.                 (2.2)
```

Consequently the unit full-carrier state is exactly

```text
a_(J,m,q)=P_(W_m)y/||P_(W_m)y||.                    (2.3)
```

It depends on `(J,m,q)` and not on `gamma`.  Height enters only through the
arithmetic multiplier, specifically through the phases
`cos(gamma*log n)`.  This explains why a gamma scan must resolve the natural
`1/log T` oscillation scale; sampling only a few fixed fractions of `T` can
miss narrow arithmetic troughs.

For any real odd companion `w`, every real combination of `a` and `w` is
odd.  Complex combinations remain odd as coefficient sequences and still
have even squared synthesis.  Thus parity supplies many geometry-only
companions, but no choice among them obtains an arithmetic sign for free.

## 3. Exact infinite-lattice synthesis theorem

The unprojected full-lattice carrier can be summed in closed form.

### Theorem 3.1 (centered Cauchy tail equals an odd sinh packet)

Let `q>0`.  For real `r`,

```text
sum_(k in Z) [k/(k^2+q^2)]/(r-k)
 =pi*[r*cot(pi*r)-q*coth(pi*q)]/(r^2+q^2).          (3.1)
```

Therefore the sharp synthesis is

```text
Phi_(q,h)(r)
 =(2*pi/h)*[r*cos(pi*r)-q*coth(pi*q)*sin(pi*r)]
             /(r^2+q^2).                           (3.2)
```

If `r=(t-gamma)/h`, `q=alpha/h`, then, up to a fixed nonzero scalar and the
harmless modulation by `gamma`, (3.2) is the Fourier transform of
`f_(L,alpha)` in (1.1).

#### Proof

Use

```text
k/(k^2+q^2)=(1/2)*[1/(k-iq)+1/(k+iq)]
```

and the Mittag--Leffler identity

```text
sum_k 1/[(k-a)(r-k)]
 =pi*[cot(pi*r)-cot(pi*a)]/(r-a).
```

Adding the cases `a=+/-iq` proves (3.1), and multiplication by
`2*sin(pi*r)/h` proves (3.2).  Finally

```text
integral_(-pi)^pi [sinh(q*u)/sinh(pi*q)]*exp(-i*r*u)du
 =2*i*[r*cos(pi*r)-q*coth(pi*q)*sin(pi*r)]/(r^2+q^2),
```

which proves the physical-space assertion after `u=h*x`.  QED

This theorem identifies the canonical unprojected parity carrier with a
very concrete endpoint-growing packet.  Finite aperture removes its Cauchy
tails.  Endpoint projection replaces it by its corresponding Hahn tail; no
claim is made that those operations leave the following unprojected formula
unchanged.

## 4. The sinh-tent autocorrelation and the two-abscissa collapse

For `0<=u<=L`, direct integration gives

```text
C_(L,alpha)(u)
 :=integral_(-L/2)^(L/2-u)
       sinh(alpha*x)*sinh(alpha*(x+u))dx

  =sinh(alpha*(L-u))/(2*alpha)
    -(L-u)*cosh(alpha*u)/2.                         (4.1)
```

Extend `C` evenly and set it to zero outside `[-L,L]`.  Notice that `C` is
positive at zero but negative near `u=L`.  Thus even the autocorrelation of
the odd carrier is not a nonnegative prime weight.

Let

```text
P_T(s)=sum_(n<=T) Lambda(n)n^(-s),
D_T(s)=L*P_T(s)+P_T'(s)
      =sum_(n<=T) Lambda(n)log(T/n)n^(-s),
L=log T,
s_+=1/2+alpha+i*gamma,
s_-=1/2-alpha+i*gamma.                              (4.2)
```

Expanding (4.1) into exponentials gives the exact identity

```text
sum_(n<=T) Lambda(n)/sqrt(n)
  *C_(L,alpha)(log n)*cos(gamma*log n)

 =1/4*Re{
      (T^alpha/alpha)*P_T(s_+)
     -(T^(-alpha)/alpha)*P_T(s_-)
     -D_T(s_+)-D_T(s_-)
   }.                                               (4.3)
```

The same identity holds with `P_T,D_T` replaced by their continuum
integrals.  Hence the centered prime-minus-continuum part is exactly (4.3)
with each polynomial replaced by its discrepancy from that integral.

Equation (4.3) is the sharpest scalar formulation found in this audit.  It
couples two complementary abscissae and one first `sigma` derivative; it is
not a maximum norm, a whole Pick matrix, or a generic prime polynomial.  A
uniform proof of the unprojected one-square would follow from the following
scalar statement, together with the explicit gamma/rational background.

> **Centered sinh-tent restricted Weil inequality.**  Uniformly for the
> admissible `T,gamma,alpha`, the shifted positive gamma/rational square
> dominates the real two-abscissa discrepancy in (4.3).

For the actual endpoint construction, replace `C_(L,alpha)` by the
autocorrelation of the finite-aperture Hahn-projected packet.  The theorem
has the same one-dimensional form, but (4.3) is then replaced by the
corresponding explicitly computable cosine weights.  Thus (4.3) is a core
model and exact limiting baseline, not a silent deletion of endpoint jets.

This is a restricted Weil-positivity problem.  A rigorous negative value of
the complete square would be an actual RH countercertificate, so a floating
negative scout would require interval replay before any mathematical claim.

## 5. Pointwise evenized Herglotz positivity is rigorously false

Write the exact completed multiplier in the normalization of the
conditional-Pick report as

```text
nu_T(t)
 =[Re psi(1/4+i*t/2)-log pi]/(2*pi)
  +1/[2*pi*(1/4+t^2)]
  -(1/pi)*Re E_T(t),                                (5.1)

E_T(t)=sum_(n<=T) Lambda(n)n^(-1/2+i*t)
       -integral_1^T v^(-1/2+i*t)dv.
```

If `W(s)=|Phi(gamma+s)|^2` is even, then the shifted square can be written
using the evenized multiplier

```text
nu_even,+1(gamma,s)
 =1+[nu_T(gamma+s)+nu_T(gamma-s)]/2.                (5.2)
```

Pointwise nonnegativity of (5.2) would prove every centered odd square at
once.  It fails.

### Proposition 5.1 (actual-coefficient Arb countercertificate)

At

```text
T=4096,
gamma=6144,
s=-1105.1008,
t_1=5038.8992,
t_2=7249.1008,
```

an 80-decimal Arb/Acb evaluation retaining every prime power `n<=4096`, the
matching continuum, complex digamma, and rational term gives

```text
nu_T(t_1)
 =[-1.63576277268361562158437681016836929759634674347
    +/- 5.1e-50],

nu_T(t_2)
 =[-1.41132178691906886809939087819474559552187345044
    +/- 5.6e-50],

nu_even,+1(gamma,s)
 =[-0.52354227980134224484188384418155744655911009695
    +/- 8.5e-50].                                  (5.3)
```

The source evaluator actually returns radii below `9e-75`; (5.3) is rounded
outward to avoid advertising irrelevant digits.

This refutes only the pointwise Herglotz sufficient condition.  The negative
set can be narrow, while an admissible `W` is bandlimited and constrained.
It is **not** a negative compressed square and does not falsify RH.

Ordinary Fejer smoothing does not restore a free theorem.  A local positive
height average multiplies the prime coefficient at `log n` by the
characteristic function of the averaging measure.  Fixed-width Fejer
averaging leaves the small-prime frequencies at constant size; a width
tending to infinity leaves the target-local regime.  The exact obstruction
to trying to null every prime phase is quantified next.

## 6. Positive local height averaging has too few zeros

### Theorem 6.1 (carrier-local averaging zero bound)

Let `eta` be a probability measure supported in `[-H,H]` and

```text
phi(z)=integral exp(i*t*z)deta(t).
```

Counting multiplicity, the number `N_phi(R)` of zeros in `|z|<=R` obeys

```text
N_phi(R)<=4*H*R/(pi*log 2).                          (6.1)
```

#### Proof

One has `phi(0)=1` and

```text
|phi(z)|<=exp(H*|Im z|).
```

Apply Jensen's formula on the circle `|z|=2R`.  Its averaged logarithmic
upper bound is

```text
(1/(2*pi))*integral_0^(2*pi)2*H*R*|sin theta|dtheta
 =4*H*R/pi.
```

Every zero in `|z|<=R` contributes at least `log 2`, proving (6.1).  QED

If positive height averaging is required to annihilate every prime phase,
then `phi(log p)=0` for all `p<=T`.  Take `R=log T`.  Since
`pi(T)>>T/log T`, (6.1) forces

```text
H >> T/(log T)^2.                                  (6.2)
```

Thus an average all of whose centers remain in an `O(1)` target-aligned
window cannot perform prime-log nulling.  This conclusion uses only the
prime nodes; prime powers make the interpolation request larger.

There is one escape from the strict-support statement: keep positive mass
near the aligned center and put the remaining mass at remote shifts.  Write

```text
eta=w_0*delta_0+(1-w_0)*eta_far.
```

Then exact prime nulling is precisely the convex moment problem

```text
-[w_0/(1-w_0)]*1
 in conv{(cos(xi*log p))_p: xi in supp(eta_far)}.    (6.3)
```

Only the aligned mass and any genuinely bounded-frequency cluster retain
the target without decay.  Hence this escape is not a new averaging proof;
it is exactly the positive spectral central-atom gate.  Existing finite LP
data suggest a square-root-power aligned mass, but no actual-prime
asymptotic upper or subpower lower bound is known.

Varying the cutoff scale without height averaging changes the weights and
active nodes in (4.3), but it does not alter the phase
`cos(gamma*log n)`.  It therefore does not evade the two-abscissa scalar by
itself.  Joint scale/height averaging returns to (6.3).

## 7. What spectral factorization does and does not supply here

Positive prime-log moment data can be multiplied by a compact positive-
definite autocorrelation and continuously factorized.  This correctly
produces a compact scalar packet whose **total autocorrelation** vanishes at
the chosen prime-log nodes.

For the centered parity route there is an additional adapter: the full
carrier is a prescribed real odd state.  A Krein spectral factor of an even
positive spectral density need not itself be real odd.  Splitting a general
factor into its even and odd parts does not preserve the nodewise zeros,
because the vanishing total autocorrelation can use cancellation between the
two parity pieces.  Therefore compact factorization alone proves neither

```text
an odd prime-null factor,
nor a subpower overlap with the prescribed Hahn carrier.       (7.1)
```

There are two valid ways forward:

1. prove an odd-factor/carrier-overlap theorem for the actual moment
   solution; or
2. use the factorized packet in the separate two-lobe program, where exact
   centered parity is not the geometric engine.

This is an adapter requirement, not a refutation of the positive spectral
construction.

## 8. Actual-coefficient fail-fast

The carrier simplification (2.3) permits a denser gamma scan than the earlier
boundary--confluent companion scan.

### 8.1 Full centered carrier

The new scan used

```text
T in {48,64,96,128},
aperture fraction in {.12,.20,.30,.40},
m in {0,2,4,6,8,10,12} when dimension permitted,
alpha in {.05,.20,.40,.49},
absolute gamma step .06 throughout the admissible centered band.
```

It evaluated 286,276 valid unit-carrier states.  Results:

```text
negative unshifted squares: 0,
negative shifted squares:   0,

smallest unshifted value:
  0.01763128462600095
  at T=48, gamma/T=1.4485000000000123,
     aperture=.12, m=0, alpha=.05, grid dimension=7.       (8.1)
```

The gamma step is finer than the natural `1/log T` oscillation scale on this
range.  It is not an interval cover.

### 8.2 Whole odd compression

Independently, the complete arithmetic matrix was compressed to the odd
coefficient subspace after the odd endpoint moments were imposed.  Across
5,552 configurations with

```text
T in {6,7,8,9,10,12,16,24,32,48,64,96,128,192,256,384,512},
m even, 0<=m<=20,
multiple centered apertures and center fractions,
```

no negative unshifted odd eigenvalue was found.  The smallest was

```text
0.003585625676413192
at T=96, gamma/T=1.55, aperture=.4, m=0.            (8.2)
```

This stronger-looking finite fact is consistent with verified critical-line
behavior at accessible heights.  It is not evidence for a uniform theorem:
the arithmetic matrix is a Weil form, and a rigorous negative certificate
would have consequences far beyond a numerical gate diagnostic.

## 9. Exact remaining theorem and research decision

The centered-even arithmetic gate has not been proved or falsified.  It has
been reduced to the following alternatives.

1. **Direct scalar route.**  Prove the centered sinh-tent restricted Weil
   inequality (4.3), then transfer it with controlled loss to the finite
   aperture and Hahn-projected autocorrelation.  This is now the cleanest
   formulation of the actual one-square problem.
2. **Moment-null route.**  Prove a subpower aligned mass in (6.3) together
   with an odd-factor/carrier-overlap adapter.  Dimension counting and compact
   factorization do not prove either estimate.
3. **Falsification route.**  Find a negative complete square and replay it
   with Arb.  The 286,276-point carrier scan and the 5,552 odd-compression
   scan found none; pointwise negativity (5.3) is insufficient.

The following proposed engines should be pruned in their bare forms:

```text
pointwise positivity of the parity-evenized shifted multiplier;
fixed-width Fejer/Herglotz averaging;
exact prime-log nulling by a carrier-local positive height average;
scale averaging without phase averaging;
generic spectral factorization without an odd carrier adapter.            (9.1)
```

The executable identities and interval certificate are in
[`centered_even_cosine_gate.py`](../src/centered_even_cosine_gate.py), with
tests in
[`test_centered_even_cosine_gate.py`](../src/test_centered_even_cosine_gate.py).
The focused suite returns

```text
4 passed.
```

