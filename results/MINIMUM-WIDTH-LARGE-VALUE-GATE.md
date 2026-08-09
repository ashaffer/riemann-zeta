# Minimum-width large-value gate

Status: exact Bernstein and Paley--Wiener lemmas, finite-height Sobolev
calibration, current large-values barrier, and fail-fast specification;
2026-08-06.  A completed exceptional-set theorem remains open.  This note
does **not** prove a new zero-free region or the Riemann Hypothesis.

## 1. Verdict

R75 leaves one credible global strategy: make one hypothetical off-line zero
force a resolvable set of large values, then prove that the complete finite
arithmetic field has too small an exceptional set to contain such a peak.
There are two materially different analytic objects.

1. The R73 polynomial

   ```text
   A_I(t)=sum_(n in N_I)c_n n^(-it)                     (1.1)
   ```

   is bounded and almost periodic.  Bernstein's inequality uses its
   **global** supremum, not its supremum on the height window being studied.
   An arbitrary value of off-line size `exp(delta R)` is guaranteed to
   persist only for width

   ```text
   exp(-(1/2-delta)R-o(R))/(H_I+2ell),                  (1.2)
   ```

   under the unconditional coefficient bound.  A width `1/R`, or the
   demodulated width `1/H_I`, is justified only at a value comparable with
   the global supremum.  No zero-to-global-maximum statement is known.
2. The correct completed object is the compactly windowed transform

   ```text
   F_I(t)=Fourier[chi_I G_I](t),                         (1.3)
   ```

   where `G_I` contains the grouped tail and the entire rank-two or exact
   Type-I center before localization.  It is a Paley--Wiener function of
   type `H_I/2`.  Spectral concentration plus an off-line `L2` carrier forces
   an exceptional set of measure `gg 1/H_I`, without assuming that a local
   high value is near the global maximum.
3. A finite Sobolev hierarchy places a fixed positive proportion of the
   energy in a finite height window.  At derivative order `q`, an off-line
   displacement `d` produces height

   ```text
   T_R=exp(((1/2-d)/q+o(1))R)                            (1.4)
   ```

   and completed values of size

   ```text
   exp((d-(1/2-d)/(2q)-o(1))R).                         (1.5)
   ```

   A growing order with `k^2=o(R)` formally improves these to
   `T_R=exp(o(R))` and `exp((d-o(1))R)`, subject to the open R71 blockwise
   converse and the growing-order Sobolev estimate (5.3).  The underlying
   Euler-trace uniformity is now imported.
4. Generic large-value and finite-moment estimates do not reach the required
   exceptional measure.  Their length term remains exponentially large at
   every normalized threshold `N^alpha` with `alpha<1/2`.  Current deep
   large-value technology controls the number of many separated peaks; this
   gate must exclude even one interval of length comparable with `1/H_I`.
5. The surviving theorem is therefore a cutoff-complete exceptional-measure
   bound for (1.3), uniform on **every** regular block and retaining the
   center.  A theorem for the raw polynomial, separate Vaughan sectors, or a
   density-one family of blocks does not pass the gate.

The large-value formulation changes the shape of the open estimate, but not
its logical strength.  No upper bound of the required kind is proved here.

## 2. The two exact finite objects

Freeze the Vaughan cutoffs on a regular logarithmic block `I=[a,b]` of
length

```text
H_I=b-a.                                                 (2.1)
```

Let `mathcal V` be the normalized compact R71 coboundary profile of support
width `2ell`, and put

```text
c_n=a_(U,V)(n)/sqrt(n),
B_I(R)=sum_n c_n mathcal V(R-log n).                     (2.2)
```

Only the finite set

```text
N_I={n: (log n+supp(mathcal V)) intersects I}            (2.3)
```

can contribute.  The safe Mellin polynomial is (1.1).  The completed field
is

```text
G_I(R)=B_I(R)-z_I(R),                                   (2.4)

z_I(R)=exp(R/2)(alpha_I+beta_I R)/norm(W_(h,k))_2.       (2.5)
```

The constants `alpha_I,beta_I` are the exact R73 finite-cutoff quantities.
Alternatively retain the unevaluated Type-I head; then

```text
G_I^ex=C_full                                            (2.6)
```

is exactly cutoff-independent.  The explicit-center version is

```text
G_I=C_full+mathcal E_I,                                  (2.7)
```

where `mathcal E_I` is the Euler-evaluation defect.  This notation is kept
distinct from the block energy `E_I` introduced in (4.4).

Choose a real smooth cutoff `chi_I` supported in `I`, and take the R73
energy weight to be `psi_I=chi_I^2`.  Define

```text
g_I=chi_I G_I,
F_I(t)=integral_R g_I(R)exp(-itR)dR.                     (2.8)
```

This is still a completely finite arithmetic object.  Exactly,

```text
F_I(t)=sum_n c_n integral chi_I(R)mathcal V(R-log n)
                         exp(-itR)dR
       -[alpha_I J_chi(1/2-it)+beta_I J_chi'(1/2-it)]
          /norm(W_(h,k))_2,                              (2.9)

J_chi(s)=integral chi_I(R)exp(sR)dR.                    (2.10)
```

Formula (2.9) records two restrictions which cannot be discarded.

* Multiplication by `chi_I` makes the atom integral depend on `n` near the
  block boundary.  It is not globally equal to `mathcal Vhat(t)A_I(t)`.
* The center is part of `F_I`.  Dividing it by `mathcal Vhat`, bounding it
  separately, or subtracting it after a large-value estimate destroys the
  completion.  Tail and center can each have size `exp(R/2+o(R))` while
  their difference has only off-line size `exp(delta R)`.

## 3. What Bernstein really says for the raw polynomial

### Lemma 3.1 (sharp global-supremum persistence)

Let

```text
P(t)=sum_j d_j exp(-i lambda_j t),
Omega=max_j lambda_j-min_j lambda_j>0,
M=sup_(t in R)|P(t)|.                                    (3.1)
```

If `abs(P(t_0))=V`, then

```text
abs(P(t))>=V/2
whenever abs(t-t_0)<=V/(Omega M).                        (3.2)
```

Hence the real half-height set contains an interval of length

```text
2V/(Omega M).                                            (3.3)
```

#### Proof

Put `lambda_c=(lambda_max+lambda_min)/2` and

```text
Q(t)=exp(i lambda_c t)P(t).
```

Then `Q` is bounded on the real axis and has exponential type `Omega/2`.
The sharp Bernstein inequality gives

```text
sup_R abs(Q')<=(Omega/2)M.                               (3.4)
```

Since `abs(Q)=abs(P)`, integrating (3.4) proves (3.2).

For (1.1), the active frequencies satisfy

```text
Omega_I<=H_I+2ell.                                      (3.5)
```

The elementary divisor estimate gives, with `R=b`,

```text
M_I<=sum_(n in N_I)|c_n|
 <<sum_(n<=exp(R+ell)) tau_3(n)log(n)/sqrt(n)
 <<exp(R/2+o(R)).                                       (3.6)
```

Thus a value `V>=exp((delta-o(1))R)` gives only (1.2).

If `V=M_I`, (3.3) has size `2/Omega_I`.  This does **not** justify applying
that width to an arbitrary value in a bounded height window.  The supremum
in (3.1) is global.  It may only be approached at very large recurrence
times, and its size can be exponentially larger than the local value.

The dependence in (3.2) cannot be improved from the stated data.  For

```text
P(t)=V+iM[exp(i Omega(t-t_0))-1],                         (3.7)
```

one has `P(t_0)=V` and `P'(t_0)=-M Omega`, so a change of order `V` occurs
on the scale `V/(M Omega)`.  Fixed-band superoscillatory polynomials provide
the complementary warning that a local supremum cannot replace the global
one.

This kills the naive raw-polynomial claim.  Demodulation improves a global
type `R` to the true diameter `H_I+2ell`; it does not delete the ratio
`V/M_I`.

## 4. The compact completed width lemmas

Because `g_I` is supported in an interval of length `H_I`, multiplication
of `F_I` by a unimodular exponential makes it an entire function of type
`H_I/2`.  It is continuous, tends to zero at real infinity, and attains its
global maximum.

### Lemma 4.1 (completed global maximum)

If

```text
M_F=sup_R abs(F_I),                                      (4.1)
```

then

```text
measure{t:abs(F_I(t))>=M_F/2}>=2/H_I.                   (4.2)
```

This is Lemma 3.1 with `Omega=H_I` at a maximizing point.  Consequently a
**global** estimate

```text
measure{t:abs(F_I(t))>=lambda}<2/H_I                    (4.3)
```

implies `M_F<2lambda`.  The same conclusion holds in a finite height window
only if a global maximizing interval of radius `1/H_I` is known to lie in
that window.  Bernstein gives no corresponding statement from a merely
local maximum.

The off-line energy carrier does not by itself locate the global maximum in
a prescribed height window.  The following `L2` lemma is the robust
replacement.

### Lemma 4.2 (energy forces completed exceptional measure)

Let

```text
E_I=norm(g_I)_2^2.                                      (4.4)
```

Suppose, for `0<eta<=1`, that

```text
integral_(-T)^T abs(F_I(t))^2dt>=2pi eta E_I.            (4.5)
```

Set

```text
lambda^2=pi eta E_I/(2T).                               (4.6)
```

Then

```text
measure{abs(t)<=T:abs(F_I(t))>=lambda}
 >=pi eta/H_I.                                          (4.7)
```

#### Proof

Cauchy--Schwarz gives the completed, rather than sectorwise, bound

```text
norm(F_I)_infinity^2<=norm(g_I)_1^2<=H_I E_I.            (4.8)
```

If the set in (4.7) has measure `m`, its complement contributes at most
`2T lambda^2=pi eta E_I` to (4.5), while the set contributes at most
`H_I E_I m`.  This proves (4.7).

More generally, if the left side of (4.5) is at least `2pi eta E_I` and

```text
measure{abs(t)<=T:abs(F_I(t))>=lambda}<=c/H_I,           (4.9)
```

then

```text
(2pi eta-c)E_I<=2T lambda^2.                            (4.10)
```

For any fixed `c<2pi eta`, an exceptional-measure theorem at the
`1/H_I` scale therefore gives an energy upper bound.  It is not literally
equivalent to a local pointwise bound, but it is quantitatively almost as
strong after spectral concentration.  Conversely, (4.7) shows that a large
energy cannot hide in a set smaller than this scale.

## 5. A finite height window from Sobolev control

For every positive integer `q` for which the weak derivative exists,
Plancherel gives

```text
integral_(abs(t)>T) abs(F_I(t))^2dt
 <=2pi T^(-2q) norm(g_I^(q))_2^2.                        (5.1)
```

For a window centered at a fixed ordinate `gamma`, replace `g_I^(q)` by
`(d/dR-i gamma)^q g_I`.  A fixed `gamma` changes only the constants below.
If the ordinate is allowed to grow with `R`, its contribution must be kept
explicit.

For fixed smoothing order `k>q+1`, Leibniz's rule, the compact B-spline
derivative norms, (3.6), and the exact rank-two center give

```text
norm(g_I^(q))_2
 <=C_(q,k,ell,chi) exp(R/2)R^C.                          (5.2)
```

For a growing fixed-step order the safe target is

```text
norm(g_I^(q))_2
 <=exp(R/2+O_h(k^2+k log(k+2))+o(R)),                    (5.3)
```

where the `k^2` allowance covers the imported Euler-trace uniformity.  A
Gevrey block partition can keep its derivative constants
inside `exp(O(k log k))`.  Formula (5.3), and the corresponding growing-order
blockwise carrier, are proof obligations rather than inputs silently
available from the fixed-order theorem.

Suppose a regular block satisfies

```text
E_I>=exp((2d-o(1))R),       d>0.                         (5.4)
```

For fixed `q`, take

```text
T_R=exp((vartheta+o(1))R),
vartheta>(1/2-d)/q.                                      (5.5)
```

Equations (5.1)--(5.2) put `1-o(1)` of the energy in `[-T_R,T_R]`.
Lemma 4.2 then forces

```text
measure{abs(t)<=T_R:
 abs(F_I(t))>=exp((d-vartheta/2-o(1))R)}
 >>1/H_I.                                                (5.6)
```

The limiting fixed-`q` exponent is

```text
alpha_q(d)=d-(1/2-d)/(2q).                              (5.7)
```

It is positive exactly when

```text
d>1/(4q+2).                                              (5.8)
```

Thus a hypothetical fixed displacement can first be fixed, after which one
may choose a sufficiently large but still fixed smoothing order.  This
avoids claiming uniform growing-order estimates which have not been proved.

If `q` grows comparably with `k`, `k^2=o(R)`, and both (5.3) and the R71
blockwise converse hold uniformly, the formal limit is

```text
T_R=exp(o(R)),
threshold=exp((d-o(1))R),
exceptional measure >>1/H_I.                             (5.9)
```

## 6. What one off-line zero actually supplies

Let

```text
rho=1/2+delta+i gamma,       delta>0                     (6.1)
```

be one fixed zeta zero.  The R71 compact coboundary multiplier does not
vanish at `rho-1/2`.  The proved fixed-window scale-energy law therefore
has abscissa at least `delta`.  For every fixed `0<d<delta`, its cumulative
energy exceeds `exp(2dR)` along a sequence.

A standard block extraction is legitimate but must be stated.  Remove an
earlier proportional interval using the unconditional width `Delta<=1/2`,
partition the remaining logarithmic shell into a subexponential number of
regular frozen-cutoff blocks, and use a bounded-overlap square partition
`sum chi_I^2=1`.  At least one block satisfies (5.4).  With the exact Type-I
head this is a finite completed field identity.  With the explicit R71
center one must also prove

```text
norm(chi_I mathcal E_I)_2=o(exp(dR)).                    (6.2)
```

For fixed order below the Euler endpoint this is the usual fixed-order
transfer.  For the fixed-step growing-order schedule the uniform Euler lemma
in `FULL-FIELD-VK-SUBPOWER-BOUND.md` proves (6.2), in fact with an
`exp(-kappa R)` defect.  Only the blockwise converse remains open here.

The resulting quantifiers are:

1. fix one off-line zero and then fix `d<delta`;
2. choose `q,k` after `d` is fixed;
3. obtain infinitely many regular blocks, not necessarily a positive-density
   family;
4. use the height window required by (5.5), including the fixed ordinate
   `gamma` in its constants;
5. apply an arithmetic exceptional-set theorem which holds on **every**
   sufficiently large admissible block.

An estimate holding only for almost all blocks can miss the carrier
subsequence.  An estimate on a fixed or polynomial height range does not
automatically cover (5.5).  A growing zero ordinate cannot be absorbed into
a fixed implied constant.

There is also a decisive circular shortcut.  For `Re(s)>1`, the untruncated
tail factors as

```text
(1-zeta(s)M_Y(s))[-zeta'(s)/zeta(s)-L_Y(s)].             (6.3)
```

Its analytic continuation has the R74 principal part at `rho`.  The finite
polynomial `A_I(t)` is entire.  Evaluating (6.3) at `rho`, or claiming from
its pole that `A_I(gamma)` is large, requires a truncation remainder smaller
than the proposed peak.  That is the large-value/zero-isolation theorem
being sought.  The valid unconditional route is the scale-energy carrier
followed by Lemmas 4.2 and 5.1; it need not put the peak at exactly `gamma`.

## 7. Why current generic large-values estimates stop early

The versioned literature cards and R71 pass/fail matrix are maintained in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).

Write `N=exp(R)`.  On a dyadic subblock, compare the normalized polynomial
(1.1) with an ordinary length-`N` polynomial

```text
P(t)=sum_(n~N)b_n n^(-it),       abs(b_n)<=N^o(1),       (7.1)
```

through `P=N^(1/2+o(1))A_I`; on the faithful growing-order schedule the
whole active block has the same relation, while at fixed order one first
uses a bounded or subexponential dyadic partition.  A completed threshold

```text
abs(A_I)>=N^alpha,       alpha<1/2,                      (7.2)
```

corresponds to an ordinary threshold `V=N^(1/2+alpha+o(1))`.

The classical comparison large-values estimate for a one-separated set has
the form

```text
R_large<=T^o(1)[N^2 V^(-2)
 +T min(N V^(-2),N^4 V^(-6))].                          (7.3)
```

Its first term becomes

```text
N^(1-2alpha+o(1)).                                      (7.4)
```

It is exponentially larger than `1/H_I` for every `alpha<1/2`.

Guth and Maynard prove major improvements in the critical large-value range,
especially around `V=N^(3/4)`, and obtain important zero-density and
short-interval consequences.  See the official
[Annals of Mathematics article](https://annals.math.princeton.edu/2026/203-2/p06)
and [arXiv:2405.20552](https://arxiv.org/abs/2405.20552).  Those theorems do
not assert that a single arbitrary completed Mobius--Vaughan peak is absent.
They count separated large values of a generic coefficient-bounded
polynomial.  Precisely, their Theorem 1.1 gives

```text
R_large<=T^o(1)[N^2 V^(-2)+N^(18/5)V^(-4)
                         +T N^(12/5)V^(-4)].             (7.5)
```

At the normalization `V=N^(1/2+alpha+o(1))`, the three exponents are

```text
1-2alpha,       8/5-4alpha,       tau+2/5-4alpha,
T=N^tau.                                                   (7.6)
```

The first is positive for every `alpha<1/2`, independently of `T`.  The
present gate needs an upper bound smaller than one Bernstein-scale interval,
with the center and coefficient cancellation retained.  At the benchmark
`V=N^(3/4)`, the classical comparison is roughly
`N^(1/2)+T N^(-1/2)` and the new bound is roughly
`N^(3/5)+T N^(-3/5)` in the range highlighted by the authors.  The improved
balance has major applications, but both first terms still allow a positive
power of `N` exceptional points rather than excluding one.

Matomäki and Teräväinen show in the converse direction that zero-density
information itself implies substantial large-value estimates for Dirichlet
polynomials; see
[arXiv:2403.13157](https://arxiv.org/abs/2403.13157).  This reinforces the
quantifier warning: density technology can control how many exceptional
heights occur while one off-line zero is already fatal here.  Feeding a
zero-density consequence back into this gate cannot exclude that one zero
unless the resulting estimate reaches the strict minimum-width threshold.

### 7.1 The finite-moment hierarchy has the same barrier

For a positive integer `m`, Markov's inequality gives

```text
measure{abs(t)<=T:abs(A_I(t))>=lambda}
 <=lambda^(-2m) integral_(-T)^T abs(A_I(t))^(2m)dt.       (7.7)
```

Applying the mean-value theorem to the `m`-fold product, with only divisor
losses suppressed, gives the generic scale

```text
integral_(-T)^T abs(A_I(t))^(2m)dt
 <<(T+N^m)N^o(m).                                       (7.8)
```

At `lambda=N^alpha`, this yields

```text
measure(exceptional)
 <<T N^(-2m alpha)+N^(m(1-2alpha)+o(m)).                 (7.9)
```

For every `alpha<1/2`, the length term grows exponentially for every fixed
`m`, and increasing `m` makes that obstruction worse.  Letting `m` grow
also makes the suppressed divisor and smoothing constants load-bearing.

Expanding moments of the completed `F_I` rather than `A_I` is legitimate,
but then every unequal product and every center term must remain inside the
`2m`-fold form.  Bounding those pieces separately returns the
`exp(R/2)` raw scale.  A completed moment theorem strong enough to make

```text
integral abs(F_I)^(2m)=o(lambda^(2m)/H_I)               (7.10)
```

would be a genuine new arithmetic result; it is not supplied by the generic
moment hierarchy.  At `m=1`, its cancellation content is already the R71/R73
energy problem.

There is a useful fixed-strip calibration.  A raw value `N^d` together
with the unconditional `N^(1/2+o(1))` global bound persists on the scale
`N^(-1/2+d-o(1))`.  Its forced contribution to the `2m`-th moment therefore
has exponent

```text
(2m+1)d-1/2.                                            (7.11)
```

If an independent coefficient-specific completed moment theorem had upper
exponent `theta_m`, it would exclude that displacement whenever

```text
theta_m<(2m+1)d-1/2.                                    (7.12)
```

The dream calibration `theta_m=0` starts at
`d>1/(4m+2)` (`1/6,1/10,1/14,...`).  This is a graduated way to ask for a
new zero-free strip, not a shortcut: expanding the moment gives a complete
`2m`-shift Mobius-and-center correlation, and `m=1` already contains the
R71 energy obstruction.

For the compact transform itself, let `U_p=integral abs(F_I)^p` and let
`M` be its global maximum.  Combining Lemma 4.1 at level `theta M` with
Markov and optimizing `theta^p(1-theta)` gives

```text
theta=p/(p+1),
p log(M)-log(U_p)
 >log(H_I(p+1)/4)+p log(1+1/p).                         (7.13)
```

Here the half-width is `H_I/2`; equivalently the right side is
`log(B(p+1)/2)+p log(1+1/p)`.  Centering therefore saves a logarithmic
factor compared with the spurious raw type near `R`, but it does not create
the needed moment estimate.  For `p=2`, Plancherel returns the R71 energy;
higher completed moments expand into still larger shift correlations.

## 8. The exact surviving theorem target

Fix `d>0` and an integer `q` for which `alpha_q(d)>0`.  Put

```text
vartheta>(1/2-d)/q,
alpha<d-vartheta/2.                                     (8.1)
```

The minimum-width large-value theorem needed to exclude a zero of
displacement greater than `d` is:

> For every admissible regular frozen-cutoff block `I` with right endpoint
> `R`, for its exact completed transform `F_I` in (2.8), and for
> `T_R=exp((vartheta+o(1))R)`, one has
>
> ```text
> measure{abs(t)<=T_R:abs(F_I(t))>=exp(alpha R)}
>   =o(1/H_I),                                           (8.2)
> ```
>
> uniformly in the allowed cutoffs and block weights.

The `o(1/H_I)` may be replaced by `c/H_I` with a constant strictly below
the lower constant furnished by Lemma 4.2.  Formula (4.10) then turns (8.2)
directly into the required energy upper bound.

For an RH endpoint via a growing order, the corresponding target is:

```text
for every epsilon>0,
measure{abs(t)<=exp(o(R)):
        abs(F_I(t))>=exp(epsilon R)}=o(1/H_I),            (8.3)
```

with all `o(R)` terms uniform on the locally constant schedule.  Before
(8.3) can be called RH-equivalent, the R71 growing-order blockwise converse
and the growing-order Sobolev/carrier bounds must be completed.  The Euler
trace itself is already an imported lemma.

Any proposed proof must pass these fail-fast gates.

1. Work with `F_I`, or prove a coefficient-for-coefficient transfer from a
   raw-polynomial theorem including every boundary and center term.
2. State whether a supremum is global or restricted to a height window.
   Bernstein never accepts the latter in place of the former for free.
3. Track the height range `T_R`, the block length `H_I`, the derivative
   order, and all dependence on a zero ordinate.
4. Retain the full center before taking absolute values or moments.
5. Prove the estimate on every regular block; a density-one assertion is
   insufficient.
6. Do not evaluate the analytically continued infinite tail at a zero as if
   it were the finite polynomial.
7. Beat the actual `1/H_I` lower measure.  A power-sized count of separated
   points, a zero-density estimate, or a bound which merely says the
   exceptional set is sparse does not do so.

## 9. Research consequence and reproducibility

The cleanest remaining experiment is a coefficient-specific short-orbit
restriction estimate.  For `m=2` or `m=3`, compare the completed local
moment on the required `t` window with its long-time multiplicative-energy
or Bohr-torus analogue, without separating the center.  Such a transfer is
false for generic coefficients because the frequencies `log(n)` can be
spaced at scale `exp(-R)`.  Any gain must therefore use the actual grouped
Mobius coefficients.  The first worthwhile milestone is not RH: it is one
fixed `theta_m` satisfying (7.12), which would produce an explicit new
zero-free strip and validate the mechanism.

The finite D-rated diagnostic is
[`src/r71_large_value_width_probe.py`](../src/r71_large_value_width_probe.py),
with focused tests in
[`src/test_r71_large_value_width_probe.py`](../src/test_r71_large_value_width_probe.py).
It includes every boundary-intersecting atom, the normalized rank-two
center, raw and centered transforms, the six analytic gates above, and
quadrature refinement.  Run

```text
python3 src/r71_large_value_width_probe.py --frequency-bound 200 \
  --frequency-points 16001
python3 -m pytest -q src/test_r71_large_value_width_probe.py
```

The computation tests constants and finite geometry only.  Sampled peak
widths and moments are not asymptotic bounds and are not evidence for RH.

## 10. Final disposition

The naive minimum-width argument is closed: a raw off-line-sized value does
not automatically occupy width `1/R` or `1/H_I`.  The sharp bound contains
the exponentially small ratio between that value and the global raw
supremum.

The completed energy formulation does yield a real improvement.  Once a
finite height window contains a fixed fraction of the off-line energy, an
exceptional set of measure comparable with `1/H_I` is forced at an explicit
exponential threshold.  This is the correct lower gate for a future
Mobius-specific large-value theorem.

No existing generic large-values or moment estimate supplies the matching
upper bound, and no such bound is proved here.  The remaining task is the
complete theorem (8.2), not another local cutoff, graph, sign, or generic
coefficient argument.

The follow-up
[`FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md`](FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md)
derives the exact fourth-moment implication
`U_4<=exp((2-kappa+o(1))R) => Re(rho)<=1-qkappa/(4q+1)`,
expands the complete four-shift form, and audits the phase/Haar and
center-annihilator shortcuts.  No fixed `kappa>0` is proved there.
