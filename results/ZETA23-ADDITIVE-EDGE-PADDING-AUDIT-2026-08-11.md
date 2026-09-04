# Zeta23 additive-edge padding audit

Status: paper-level extension and revised gate, 2026-08-11.  The later
endpoint-jet construction cited below repairs the raw sharp-tail/full-spark
dichotomy but not the effective signed-carrier or prime-edge gaps.  This note
does not prove a zero-free strip and does not assert literature novelty.

## 1. Question and verdict

Put

```text
l    = log(T/(2*pi)),
c0   = 2 log 2 - 1,
ell1 = l + c0,
L    = ell1 + c/l                    (c > 0 fixed),
X    = exp(L),
h    = 2*pi/L,
d    = floor(T/h).
```

This is the smallest useful kind of modification of the Zeta23 endpoint:
`lambda_T=L/l` is slightly larger than one, but the prime cutoff remains a
fixed fraction of `T`.

The audit has one positive conclusion and one negative conclusion.

1. **The additive padding is analytically admissible.**  The raw first- and
   second-moment arguments of Zeta23 extend uniformly to this `L`; the smooth
   remote-zero tail remains small; and the padded dimension is eventually
   larger than the entire multiplicity count in the enlarged carrier window
   `I'=(T-sqrt(T),2T+sqrt(T)]`.
2. **This does not yet isolate an off-line pair with a uniform margin.**  On
   the unrestricted sharp space the remote tail is uncontrolled, while the
   original smooth window has no stable interpolation bound.  A subsequent
   endpoint-jet restriction of the sharp span gives both exact
   Cauchy--Vandermonde interpolation and an exponentially small tail.  Its
   ordinary interpolation margin can still collapse.  Collision merging
   nevertheless gives a positive signed carrier edge at each fixed parameter
   set, but no effective asymptotic rate for that edge is known.  Independently,
   the presently evaluated prime-side observables (trace and Frobenius norm)
   admit a fixed negative eigenvalue exactly.

Thus the earlier phrase “the `lambda<=1` dimension barrier” was too coarse.
The dimension barrier can be crossed by an additive edge while keeping
`X<T`.  Endpoint jets subsequently cross the qualitative
tail/interpolation tradeoff as well.  The surviving carrier obstruction is a
**quantitative signed-carrier rate** strong enough to beat the tail; the
independent arithmetic obstruction is the **prime lower spectral edge**.

## 2. Exact edge asymptotics

Since `exp(c0)=4/e`,

```text
X/T = exp(c0+c/l)/(2*pi)
    = (2/(pi*e)) exp(c/l)
    = 0.234199... * (1+O_c(1/l)).                         (2.1)
```

In particular `X<T` for all sufficiently large `T`, and more strongly
`X <= kappa_c T` for some fixed `kappa_c<1`.  Also

```text
lambda_T = L/l = 1 + c0/l + c/l^2,
L/ell1   = 1 + c/(l*ell1).                               (2.2)
```

The Riemann--von Mangoldt formula and the floor error give

```text
N(T,2T) = T*ell1/(2*pi) + O(l),
d       = T*(ell1+c/l)/(2*pi) + O(1),

d-N(T,2T) = c*T/(2*pi*l) + O(l).                         (2.3)
```

Zeta23 uses `D0=sqrt(T)` and

```text
I' = (T-D0,2T+D0].
```

Its local zero count gives `N(I'\I)=O(sqrt(T) l)`.  Hence

```text
d-N(I') = c*T/(2*pi*l) + O(sqrt(T) l) > 0                (2.4)
```

eventually, because `sqrt(T)/l^2 -> infinity`.  If `q(I')` is the number of
distinct locations, then

```text
q(I') <= N(I') <= d.                                    (2.5)
```

This includes the collar; it is stronger than merely repairing the central
main-term deficit.

Any fixed `c>0` works.  At `c=0`, the asymptotic `O(l)` remainder has unknown
sign and does not certify `d>=N`.  More generally, a padding `eta(T)` in
`L=ell1+eta(T)` handles the standard collar whenever

```text
eta(T)*T >> sqrt(T)*l.
```

The choice `eta(T)=c/l` has far more room than this minimum.

### 2.1 Mesoscopic padding range

The same calculation gives a larger paper-level extension which is useful
for future spectral-edge work.  Let

```text
L = ell1+eta(T),
eta(T)*T >> sqrt(T)*l,
exp(eta(T))*log(l)/l -> 0.                               (2.6)
```

Then `eta(T)=o(l)`, and

```text
X/T = (2/(pi*e))*exp(eta(T)),
d-N(I') = eta(T)*T/(2*pi)+O(sqrt(T)*l) > 0.             (2.7)
```

The second condition in (2.6) is exactly what is needed by the dominant raw
prime-side error in (3.5).  All conclusions of Sections 3--4 below continue
to hold, with errors tending to zero.  In particular, for every fixed
`0<theta<1` one may take

```text
eta(T)=theta*log(l),
X=(2/(pi*e))*T*l^theta,
d-N(I') ~ theta*T*log(l)/(2*pi).                         (2.8)
```

Thus keeping `X<T` is convenient but not the true analytic endpoint.  The
raw argument remains asymptotic throughout the wider regime
`X=o(T*l/log(l))`.  What it does not change is the phase-space ratio:
`L/ell1=1+o(1)`, so the compression is still asymptotically critical rather
than wider by a fixed factor.

## 3. Additive-edge extension of the prime-side estimates

### Theorem card 3.1 (raw Zeta23 estimates at the additive edge)

Fix `c>0`, a fixed `C^3` Zeta23 taper profile, and fixed ramp width `w=1`.
With the parameters above, the Zeta23 matrix `Gtilde=G/L` satisfies

```text
tr Gtilde
  = a*L*N(T,2T) + O(L*sqrt(X)),                          (3.1)

tr(Gtilde^2)
  = T*L/(2*pi) * (ell1^2 + L^2/3)
      * (1 + O_c(log(l)/l)),                             (3.2)

(tr Gtilde)^2 / tr(Gtilde^2)
  = F(L/ell1)*N(T,2T) * (1 + O_c(log(l)/l)),             (3.3)

F(u) = u/(1+u^2/3).
```

The constants may depend on the fixed taper and on `c`, but not on `T`.
In particular

```text
F(L/ell1) = 3/4 + 3c/(8*l*ell1) + O_c(l^-4).             (3.4)
```

This is a paper-level consequence of the displayed Zeta23 proof, not yet a
Lean theorem in the external API: `Params.Valid` fixes a `T`-independent
`lambda<=1`, so formalizing (3.1)--(3.3) requires a varying-parameter wrapper.

### Proof audit

The useful error quantity must be kept in its raw form:

```text
Eraw = w/L
     + (l^2+X)*log(l)/(T*l)
     + sqrt(X)/T.                                       (3.5)
```

Equations (2.1)--(2.2) give

```text
Eraw = O_c(log(l)/l).                                   (3.6)
```

More generally, under (2.6),

```text
Eraw = O(1/l)
     + O(l*log(l)/T)
     + O(exp(eta(T))*log(l)/l)
     + O(T^(-1/2)*exp(eta(T)/2))
     = o(1).                                             (3.7)
```

One must **not** substitute `lambda_T>1` into the paper's coarser shorthand
`T^(lambda-1) log l`; that shorthand was obtained after splitting into fixed
`lambda<1` and `lambda=1` cases and loses the decisive factor `1/l` here.

The proof components extend as follows.

- The explicit formula and Poisson identity are exact for every positive
  support length `L`.
- Proposition 5.3 has the raw error `O(L sqrt(X))`; (2.1) makes it negligible
  relative to `L*T*l`.
- The end-effect proof uses only `L<=2l`, `B^2<<l^2+X`, and the taper decay.
  The external Lean source already exposes this as the window-generic
  `LocalHypsCoreW` / `lem_ends_nu_W` interface, explicitly intended for
  `lambda in (1,2]`.
- The `mu-mu` estimate does not use the upper cap on `lambda`.
- Montgomery--Vaughan gives the prime-prime off-diagonal error
  `O(L^2 X)`.  At (2.1) this is `O(T l^2)`, whereas its diagonal main term is
  of order `T l^3`.
- The four cross terms remain bounded respectively by

  ```text
  O(l sqrt(X)), O(l L sqrt(X)), O(L X), O(L X/T),
  ```

  all negligible on the `T l^3` second-moment scale.
- The Chebyshev--Mertens sandwich is uniform in `X` and gives the same
  `L^3/6+O(L^2)` main term.

These are precisely the unsimplified estimates in Sections 5.2--5.5.  Their
constants and thresholds are uniform for `lambda_T` in a compact subinterval
of `(0,2)`: wherever the formal source records a `lambda`-dependent threshold,
it occurs through quantities such as `1/lambda` or
`exp(C/lambda)`, bounded uniformly here.

This extension is consistent with the paper's own limitation: the
Montgomery--Vaughan error becomes competitive only when `X` approaches or
exceeds `T L`, not when `L` exceeds `l` by a bounded additive amount.

## 4. The smooth tail also extends

For the standard `C^3` taper and `D0=sqrt(T)`, Proposition 4.2 gives directly

```text
||Etilde||
 <= 4*A0*C1^2 * sqrt(X)*log(4T)/D0^2
 = O_c(l/sqrt(T)),                                      (4.1)
```

where `C1=||phi''||_1` is fixed when `w=1`.  In the isolated-zero
normalization `Ehat=E/(aL^2)`,

```text
||Ehat||_1 <= 2||Etilde||/L = O_c(T^-1/2).               (4.2)
```

Therefore neither the prime cutoff nor the smooth remote tail prevents the
additive padding.

## 5. Why the sharp branch still fails

For the sharp interval window, the evaluation matrix is Cauchy after nonzero
row and column scalings.  Equations (2.4)--(2.5) remove its previous row-count
obstruction: qualitative surjectivity would preserve every carrier
hyperbolic block.

But the sharp Fourier transform has only `1/|r|` off-axis decay.  Zeta23
Remark 4.3 gives, in the corresponding tail calculation, a quantity of size

```text
sqrt(X) * l * log(T/D0),                                 (5.1)
```

which is not a small perturbation.  With `X asymp T` and `D0=sqrt(T)`, it
grows rather than tends to zero.  Enlarging `D0` enough to suppress the
logarithm consumes order `T l` additional zero locations, while the padding
surplus in (2.3) is only order `T/l`.  Thus the currently proved sharp-tail
estimate and the padded dimension cannot be satisfied simultaneously.

This is a failure of the available bound, not a theorem that the actual
sharp tail can never cancel arithmetically.

### 5.1 Subsequent endpoint-jet repair

The unrestricted-space failure above is not the end of the sharp branch.
Inside the same sharp Gabor span, impose `m` vanishing endpoint moments on
the coefficients.  The resulting transform has the exact form

```text
2 sin(L*(z-tau_0)/2) P(z)/Q(z),
deg P <= d-m-1,
```

so it still interpolates every `q<=d-m` local node, while `m` integrations by
parts give an exponentially small remote-zero operator once the collar and
the jet conditions are paid from the mesoscopic surplus.  The complete proof
is
[`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md).

The ordinary interpolation determinant keeps the Vandermonde factor and can
be arbitrarily small under clustering.  This is not an exact obstruction to
the signed local form: coincident same-orientation atoms merge by adding
multiplicities, and compactness gives a positive carrier edge for each fixed
parameter set.  What remains unknown is an effective grouped/collision bound
whose decay can be compared with the endpoint tail; see
[`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md).

### 5.2 The standard spline repairs do not retain universal full spark

A natural attempted escape is to convolve the sharp interval with one or
more short intervals.  This makes the window continuous or `C^1` and changes
the transform into a product of sinc factors.  Two exact tests reject the
usual claim that this preserves the sharp window's every-node Cauchy
interpolation.

First, even a literal Hadamard square of a Cauchy matrix is not universally
full spark.  With column poles `0,1` and distinct real row nodes `2,2/3`,

```text
[ 1/(2-0)^2       1/(2-1)^2     ]   [ 1/4  1 ]
[ 1/(2/3-0)^2     1/(2/3-1)^2   ] = [ 9/4  9 ]
```

has determinant zero.  This is the elementary two-by-two instance of the
Borchardt phenomenon: the determinant of a squared Cauchy matrix contains a
permanent factor, which can vanish when the denominators have mixed signs or
are complex.  The simple Cauchy determinant's universal nonvanishing does
not pass to powers.

Second, the actual compact spline at the critical lattice has an exact
residue-class defect.  Let

```text
phi_m = 1_[-L/(2m),L/(2m)] convolved with itself m times.
```

It is supported in `[-L/2,L/2]`, is `C^(m-2)`, and

```text
K_m(z) = phi_m_hat(z)
       = (2 sin(L*z/(2m))/z)^m                            (5.2)
```

up to a nonzero normalization.  Thus `m=3` is already a compact `C^1`
candidate with `1/|r|^3` decay.  At the critical spacing `h=2*pi/L`, take a
real node

```text
z_r = T + m*r*h
```

with `m*r` outside the coordinate range `0,...,d-1`.  For every column
`k` divisible by `m`, the numerator in

```text
K_m(z_r-T-k*h)
```

vanishes, while the denominator is nonzero.  Hence all such evaluation rows
annihilate the same `ceil(d/m)` coordinate columns.  Choosing

```text
q = d-ceil(d/m)+1 <= d
```

distinct admissible integers `r` gives a `q` by `d` evaluation matrix of
rank at most `d-ceil(d/m)<q`.  All nodes are distinct and real, hence lie in
`|Im z|<1/2`.  The triangular (`m=2`) and `C^1` cubic (`m=3`) cardinal
B-splines therefore fail every-node full row rank exactly.

The commensurate exponential B-splines have the same defect on translated
horizontal lines.  A factor `exp(alpha*t) 1_[0,L/m](t)` contributes

```text
(exp((alpha+i*z)L/m)-1)/(alpha+i*z),
```

whose zeros are `z=2*pi*n*m/L+i*alpha`.  If `|alpha|<1/2`, the preceding
residue-class construction lies inside the required strip.  Pairing
`alpha,-alpha` to make a real centered spline does not remove those zero
progressions.  Thus the standard exponential variant also supplies no
every-node theorem in the relevant strip.

The same residue mechanism appears for the flat-top convolution

```text
1_[interval of length L-w] * 1_[interval of length w],
```

whose transform is proportional to

```text
sin((L-w)z/2) sin(wz/2) / z^2.
```

When `w/L` is rational, one sinc factor annihilates a fixed residue class of
critical-lattice columns at an infinite arithmetic progression of real
nodes.  Irrational ratios remove this particular exact progression, but do
not provide a determinant theorem or a quantitative lower bound.

For a *fixed* finite node configuration, convolving by a sufficiently short
interval can preserve some nonzero sharp Cauchy minor by continuity.  This is
not uniform in the configuration: the required convolution width is governed
by that minor, equivalently by a least singular value.  At the same time the
standard tapered tail constant deteriorates like `w^-2` as the ramp width
`w` tends to zero.  Thus one needs a lower determinant bound before one can
choose a width that is simultaneously close enough to sharp interpolation
and wide enough for the remote-tail estimate.  The count inequality (2.5)
does not provide such a bound, and Theorem 6.1 below gives an exact reason it
cannot do so.

There is also an exponential-type reason that a pure higher-power Cauchy
repair is incompatible with the original critical support.  If an entire
transform of type at most `L/2` satisfied, after row and column scalings,

```text
K(z-k*h) = A(z) B_k/(z-k*h)^m,       m >= 2,             (5.3)
```

then `Q(z)=z^m K(z)` would be quasi-periodic with period `h` and would have
zeros of multiplicity at least `m` at every point of `h*Z`.  The standard
Jensen/Cartwright zero-density bound forces exponential type at least
`m*pi/h=mL/2`, contradicting type `L/2` for `m>=2` unless `K=0`.  The sharp
window (`m=1`) is exactly the saturated simple-zero case.  Cardinal splines
avoid the contradiction by spacing their multiplicity-`m` zeros by `m*h`,
which is precisely what creates the residue split above.

The rank-deficient spline configurations just constructed need not resemble
the actual zeta nodes in `I'`; they refute an **every-node** theorem for the
named candidate windows.  More importantly for the application, even a
different window that happened to be qualitatively full rank would still
face the quantitative clustering obstruction in the next section.

## 6. Exact stability obstruction for the smooth branch

The following calculation strengthens the qualitative “no spacing input”
warning.  It applies even after (2.5) has made the matrix wide enough.

### Theorem 6.1 (clustered rows force a small interpolation singular value)

Let `phi` be real, supported in `[-L/2,L/2]`, and let

```text
K_alpha(r) = integral phi(t) exp(alpha*t) exp(i*r*t) dt,
h          = 2*pi/L.
```

For a real ordinate `gamma`, define the full evaluation row

```text
R_alpha(gamma)_k = K_alpha(gamma-T-k*h),   k in Z.
```

Then Parseval gives the exact identities

```text
||R_alpha(gamma)||_2^2
  = L * integral phi(t)^2 exp(2*alpha*t) dt,             (6.1)

||R_alpha'(gamma)||_2^2
  = L * integral t^2 phi(t)^2 exp(2*alpha*t) dt
  <= (L^2/4) ||R_alpha(gamma)||_2^2.                     (6.2)
```

Let `E` be any finite evaluation matrix containing rows at two distinct
nodes of the same depth, `gamma` and `gamma+epsilon`.  Projection to the
finite coordinate set can only decrease norms, so the smallest row singular
value obeys

```text
sigma_min(E)
 <= ||R_alpha(gamma+epsilon)-R_alpha(gamma)||_2/sqrt(2)
 <= |epsilon|*L*||R_alpha(gamma)||_2/(2*sqrt(2)).         (6.3)
```

After division by the common full-lattice row norm in (6.1) this is

```text
sigma_min(E_normalized) <= |epsilon|*L/(2*sqrt(2)).      (6.4)
```

#### Proof

The entries divided by `L` are Fourier-series coefficients of
`phi(t)exp(alpha*t)exp(i(gamma-T)t)` on an interval of length `L`, which
proves (6.1).  Differentiate under the integral and apply the same Parseval
identity to `i*t*phi(t)exp(alpha*t)` to obtain (6.2).  In the variational
definition of the least row singular value, use the unit vector with
coefficients `1/sqrt(2),-1/sqrt(2)` on the two rows, then use the Hilbert-space
fundamental theorem of calculus.  This proves (6.3)--(6.4).

The Zeta23 local count and Riemann--von Mangoldt inputs impose no lower bound
on `|epsilon|`.  They therefore permit full-row-rank matrices whose normalized
least singular value is arbitrarily small.  Padding proves `q<=d`; it does
not prove stable interpolation.  Any carrier argument that isolates
arbitrary independent row values through a right inverse needs additional
information.  A grouped signed-carrier argument can survive collisions, but
the present inputs give no effective asymptotic rate for its negative edge.

Landau's density theorem supplies useful context for why an asymptotically
critical interpolation problem is delicate, but it is not used in this
proof.  The elementary bound (6.4) is decisive against a uniformly bounded
ungrouped interpolation inverse, not against every signed carrier.

## 7. Exact obstruction from the evaluated prime-side data

Even granting a stable carrier and a small tail, the existing prime-side
calculation supplies only the first two spectral moments.  The following
finite-dimensional construction shows exactly what those moments cannot
exclude.

### Theorem 7.1 (one fixed negative eigenvalue matches both moments)

Fix `kappa>0` and `K` with `1<K<2`.  For every sufficiently large integer
`N`, there is an `N` by `N` Hermitian matrix `H_N` such that

```text
tr(H_N)       = N,
||H_N||_F^2   = K*N,
lambda_min(H_N) = -kappa,                               (7.1)
```

and all other eigenvalues are positive.

Indeed, put `n=N-1`, `p=floor(n/2)`, `q=n-p`, and

```text
m   = (N+kappa)/n,
v   = (K*N-kappa^2)/n - m^2,
a   = m + sqrt(v*q/p),
b   = m - sqrt(v*p/q).
```

For large `N`, `v>0` and `b>0`, because `m->1`, `v->K-1<1`, and `p/q->1`.
Take one eigenvalue `-kappa`, `p` eigenvalues `a`, and `q` eigenvalues `b`.
The two deviations from `m` have weighted sum zero and weighted square sum
`n*v`, so direct summation proves (7.1).  Extra zero eigenvalues may be
appended when the compression dimension is larger than `N`.

At the additive or mesoscopic edge, the Zeta23 isolated-zero normalization
has

```text
K = 1/(L/ell1) + (L/ell1)/3 = 4/3+o(1).                 (7.2)
```

which lies in `(1,2)`.  Hence a fixed negative edge is compatible not merely
with the asymptotic trace/Frobenius formulas but with exact versions of both
numbers.  No rank--trace, Cauchy--Schwarz, or two-moment refinement can rule
out one exceptional pair.

This theorem does not assert that the actual prime-side Gabor matrix has such
a spectrum.  It proves that excluding it requires a new prime-side
lower-spectral-edge estimate using information absent from the Zeta23 moment
package.  By the explicit formula, such an estimate is already a restricted
Weil-positivity statement and is therefore the strip-strength step, not a
consequence of padding.

## 8. Revised theorem card and stop/go decision

The additive-edge route now has the following accurate status.

```text
DONE (paper level):
  L = ell1+c/l keeps X<T and extends the raw prime moments;
  d >= N(I') >= q(I') eventually;
  the smooth remote tail tends to zero.

SHARP FULL SPACE FAILS:
  qualitative Cauchy interpolation is available;
  the unrestricted proved remote-tail estimate is not small.

ENDPOINT-JET SHARP SUBSPACE SURVIVES CONDITIONALLY:
  Cauchy--Vandermonde interpolation and an exponentially small tail hold;
  collision merging gives a fixed-parameter signed carrier margin;
  no effective asymptotic rate is known for that margin.

SMOOTH WINDOW FAILS:
  remote tail is small;
  every-node full rank is unproved;
  stable interpolation is impossible from count data alone by (6.4).

INDEPENDENT FINAL GAP:
  the prime-side trace and Frobenius data permit one fixed negative
  eigenvalue by Theorem 7.1;
  a genuine lower-edge theorem is still required.
```

Accordingly, additive padding and endpoint jets should be retained as
corrected positive lemmas, but they do not prove a strip.  The branch now
requires both of the following genuinely new inputs:

1. an effective grouped-interpolation/signed-carrier bound for the
   tail-controlled endpoint-jet space, strong enough to beat its remote tail;
   and
2. a prime-side lower spectral-edge estimate in the same normalization whose
   negative error is smaller than that **actual** carrier margin.

The first is not supplied by zero counting alone.  In particular, merely
beating the remote tail need not preserve a fixed or power-scale fraction of
the full-pair edge.  The second must therefore be matched to the carrier
scale; it is not supplied by the first two moments and is already essentially
the desired zero-exclusion mechanism.  Higher exterior coefficients and moments are
quantified in the endpoint-jet follow-up and require prime correlations far
beyond those currently evaluated; the sharp Loewner displacement recorded
there is a separate structured possibility, but supplies no sign by itself.

## 9. Source and novelty boundary

Primary artifacts inspected:

- the Anthropic [full paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf),
  especially Propositions 4.2, 5.3, 5.6, 5.7, Theorem 5.8, Remark 4.3, and
  Section 7.5;
- the official [Zeta23 Lean source](https://github.com/anthropics/zeta-23-lean/tree/v1.0),
  especially `PrimeSideA`, `PrimeSideB`, `Tail`, and the window-generic
  `LocalHypsCoreW` / `lem_ends_nu_W` layer;
- Montgomery--Vaughan,
  [Hilbert's Inequality](https://doi.org/10.1112/jlms/s2-8.1.73), for the
  prime off-diagonal input; and
- Landau,
  [Necessary density conditions for sampling and interpolation of certain
  entire functions](https://doi.org/10.1007/BF02395039), as context only.

No novelty claim is made for the additive-edge observation.  In particular,
the external Lean artifact already contains a beyond-`lambda=1`
window-generic layer for a different family regime.  The new content of this
internal audit is the exact specialization (2.1)--(2.5), the explicit
varying-parameter proof audit (3.1)--(3.6), and the two fail-fast lemmas
(6.3)--(6.4) and (7.1); publication-level novelty would require a broader
primary-literature comparison and specialist review.
