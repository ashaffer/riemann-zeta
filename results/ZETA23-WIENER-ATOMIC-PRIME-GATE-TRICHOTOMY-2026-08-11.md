# The Wiener atomic prime gate: a seed-coherence trichotomy

Status: focused polarity, seed-coherence, projection, and method audit,
2026-08-11.  A fixed-power upper bound is proved for every sufficiently
delocalized seed.  A short coherent seed shows that this upper bound cannot
be promoted to an arbitrary-seed no-go by same-lobe or pole bookkeeping.
No projected `Y^(-o(1))` lower bound, arbitrary-seed power upper bound, or
zero-free strip is proved.

## 1. Verdict

For the raw polarized problem, put

```text
E_raw(Y)
 =sup {abs(sum_k b_k*h_k): Vh=0, sum_k abs(h_k)<=1}. (1.1)
```

If both factors are required to lie in endpoint-jet/prolate lobe spaces,
let `E_ad(Y)` be the same supremum over the correlations which actually
factor as

```text
h_k=conj(ell_k)*r_k
```

with admissible unit factors.  The first polarity statement is exact:

```text
E_ad(Y)<=E_raw(Y).                                   (1.2)
```

Consequently:

```text
raw lower bound   does not descend through projection;
raw upper bound   does upper-bound the projected extremal.             (1.3)
```

Thus the Montgomery--Vaughan floor

```text
E_raw(Y)>=c/sqrt(M),       M asymp Y/log Y,           (1.4)
```

does not prove any admissible carrier.  The von-Mangoldt/KMT dual
quadrature does give

```text
E_ad(Y)<=E_raw(Y)<<_W(log Y)^(-3/10),                (1.5)
```

but (1.5) is only a subpower upper bound.  It is compatible with the desired
lower bound `E_ad(Y)>=Y^(-o(1))`.

There is one genuine fixed-power no-go.  Let `D` be the number of relative
modes, `D asymp T*L`, and suppose a normalized seed obeys

```text
max_k abs(r_k)<=mu/sqrt(D).                          (1.6)
```

Then its normalized smooth Laplace carrier against every opposite unit
lobe is at most

```text
C_W*mu*T^(-1/2).                                    (1.7)
```

This remains true after restricting the opposite lobe and after imposing
prime nulls.  Hence every seed with `mu=T^o(1)` loses a fixed half-power.
At `Y=T^d`, the loss in (1.7) is

```text
T^(-1/2+o(1))=Y^(-1/(2*d)+o(1)).                    (1.8)
```

In particular, multiplying by a depth carrier `Y^alpha` gives a decaying
quantity for every fixed `alpha<1/2` and every `d<=1`.  At the asymmetric
choice `d=3/4`, it is `Y^(alpha-2/3+o(1))`.

This no-go is not universal.  A smooth physical bump in a short lobe of
length `bL`, where

```text
b->0,              bL->infinity,                    (1.9)
```

has mode coherence about `sqrt(b)`, not `D^(-1/2)`, and an aligned opposite
bump has a constant normalized smooth carrier before prime nulling.  Its
same-lobe prime term is only

```text
X^(b/2+o(1))=X^o(1),                                (1.10)
```

and finite pole conditions do not create a fixed-power lower cost.  What is
not proved is that this coherent bump can use its small prolate tails to
null all `M` prime rows with subpower factor norm.  That weighted projection
condition number is exactly the original atomic gate.

The honest conclusion is therefore the trichotomy

```text
delocalized seed:
    unconditional fixed-power carrier upper;

coherent short-lobe seed before exact prime nulling:
    constant carrier and only subpower same-lobe absolute cost;

coherent short-lobe seed after exact prime nulling:
    unresolved Wiener/weighted-projection extremal.                  (1.11)
```

No audited Turan--Nazarov, Beurling--Malliavin, longer-aperture, prolate,
or endpoint-jet theorem closes the third line.

## 2. Exact raw/projected polarity

In the unrestricted relative Fourier basis,

```text
q_(ell,r)(u)=sum_k h_k*exp(i*xi_k*u),
h_k=conj(ell_k)*r_k,
sum_k abs(h_k)<=||ell||_2*||r||_2.                  (2.1)
```

Every admissible unit pair therefore produces a point in the raw Wiener
unit ball.  Imposing

```text
q_(ell,r)(log(n/Y))=0
```

for the active prime powers puts this point in `ker V`.  This proves (1.2)
without a dimension argument.

The converse raw factorization

```text
r_k=sqrt(abs(h_k)),
ell_k=conj(h_k)/sqrt(abs(h_k))                      (2.2)
```

does not preserve a lobe, endpoint jets, or physical leakage.  Therefore a
raw primal witness for (1.4) need not produce an admissible pair.  The exact
dual distance

```text
inf_lambda max_k
 abs(b_k-sum_n lambda_n*exp(i*xi_k*log(n/Y)))        (2.3)
```

is likewise the dual only of the convex raw problem.  The projected
factorization set is generally nonconvex and has no automatic copy of
(2.3).

A low-codimension projection cannot repair this.  It shrinks the feasible
correlation set, so it can only decrease the primal supremum.  Rank or
trace control does not protect its particular maximizing direction; a
rank-one projection can remove that direction exactly.

## 3. A coherence upper bound for the genuine smooth carrier

Let the relative grid have spacing `2*pi/L`, and put

```text
b_k=integral W(u)*exp(i*xi_k*u)du.                  (3.1)
```

The cross window lies strictly inside one period.  Discrete Parseval, or
Poisson summation with no overlapping translates, gives

```text
sum_k abs(b_k)^2<=C*L*||W||_2^2.                    (3.2)
```

The same bound holds on every finite permitted mode set and for the shifted
half-integer grid.

### Proposition 3.1 (delocalized-seed carrier upper)

If `||r||_2=1` and (1.6) holds, then for every `||ell||_2=1`,

```text
abs(sum_k b_k*conj(ell_k)*r_k)
 <=(sum_k abs(b_k)^2*abs(r_k)^2)^(1/2)
 <=C*mu*sqrt(L/D)*||W||_2
 <=C_W*mu*T^(-1/2).                                 (3.3)
```

This proves (1.7).  Prime nulling only restricts `ell`, so it cannot
invalidate the upper bound.  The same is true of endpoint and lobe
conditions on `ell`.

If a raw seed `r_0` is projected and renormalized, (3.3) survives precisely
when the normalized projected seed still satisfies (1.6) with
`mu=T^o(1)`.  Codimension alone gives no such `ell-infinity` statement.
Conversely, any successful fixed-strip construction in this seed class
must create mode coherence at least `T^(1/2-o(1))` relative to the flat
scale.  That is a necessary condition, not a construction.

## 4. Concentration does not force a same-lobe power cost

The coherence upper leaves open seeds concentrated in relative frequency.
That escape cannot be excluded from the current same-lobe ledger.

Choose a fixed smooth bump `phi` supported strictly inside `(-1/2,1/2)` and
put, in a physical lobe centered at `c`,

```text
p_(b,c)(t)=(bL)^(-1/2)*phi((t-c)/(bL)).              (4.1)
```

With the standard orthonormal critical-grid convention, its mode
coefficients have the form

```text
r_k=C_phi*sqrt(b)*exp(i*xi_k*c)*hat(phi)(bL*xi_k),   (4.2)
```

up to harmless Fourier-normalization constants.  Hence

```text
||r||_2=1+o(1),
max_k abs(r_k)<<_phi sqrt(b),
# effective adjacent modes asymp 1/b.               (4.3)
```

An oppositely located bump with the aligning phase has

```text
sum_k b_k*conj(ell_k)*r_k=b(0)+o(1),                (4.4)
```

for a normalized target with `b(0) !=0`.  Thus this seed evades (1.7).
Because its physical difference support has length `bL+O(1)`, Chebyshev
and partial summation give the complete absolute same-lobe bound (1.10).
For `b=o(1)` this is subpower and cannot dominate a fixed-power selected
carrier.

The bump is already zero in endpoint neighborhoods, so its physical
endpoint jets vanish.  The standard finite-aperture prolate approximation
transfers this pre-nulling example with arbitrarily high fixed-power
leakage accuracy.  This statement does not assert that the prime nulls
survive that transfer.

There is also no signed same-lobe lower bound in the current inputs.  In
relative modes its autocorrelation is

```text
C_r(u)=sum_k abs(r_k)^2*exp(i*xi_k*u),               (4.5)
```

so the same-lobe prime form is a convex combination of signed scalar prime
twists at the `xi_k`, not a positive energy.  Absolute estimates give
(1.10); they cannot be reversed.  The two pole rows are finite-dimensional
conditions, and the same-lobe archimedean term is subpower.  Therefore
neither of them yields the proposed concentration-versus-power-cost
principle.

## 5. Exact prime nulling reintroduces the atomic gate

The bump in Section 4 has only `s asymp1/b` effective consecutive modes,
whereas

```text
M asymp Y/log Y.                                    (5.1)
```

There is a rigorous finite-support warning.  On `s` consecutive modes the
prime evaluation matrix is an ordinary Vandermonde matrix in the distinct
points

```text
z_n=exp(i*(2*pi/L)*log(n/Y)).                        (5.2)
```

It has column rank `s` as soon as at least `s` distinct prime-power nodes
are used.  Thus a nonzero correlation supported on those `s<=M`
consecutive modes cannot vanish at every active node.

A finite-aperture prolate bump is not exactly supported on its effective
core: it has small coefficients over the remaining modes.  Exact nulling
can therefore try to use those tails.  In fixed-seed coordinates its norm
is the weighted Hilbert norm

```text
sum_k abs(h_k)^2/abs(r_k)^2,                         (5.3)
```

so using tiny seed coefficients can be arbitrarily expensive.  Proving
that the cost in (5.3) is only `Y^o(1)` while retaining (4.4) is precisely a
target-conditioned projected interpolation theorem.  Prolate dimension
`bTL>>M` proves only that algebraic solutions may exist; it does not bound
(5.3).

This also explains why the coherent seed does not establish (b) in the
concentration tradeoff: no admissible lower bound

```text
E_ad(Y)>=(log Y)^(-C)                                (5.4)
```

has been obtained from it.

## 6. A longer asymmetric aperture does not improve the MV floor

Suppose a high block `H` of rows has the Montgomery--Vaughan lower frame
bound

```text
sum_(k in H) abs(sum_j lambda_j*exp(i*xi_k*u_j))^2
 >=kappa*#H*sum_j abs(lambda_j)^2.                  (6.1)
```

If the dual residual is at most `epsilon` and `b(xi_k)<<Y^(-1)` on the
block, then

```text
||lambda||_2<<epsilon+Y^(-1).                       (6.2)
```

At a low row with `b(0)>0`,

```text
b(0)-epsilon<=sqrt(M)*||lambda||_2,                 (6.3)
```

which gives only

```text
epsilon>=c/sqrt(M).                                 (6.4)
```

If the aperture `T=Y^(1/d)` supplies many disjoint high blocks, summing
(6.1) multiplies both sides by the number of blocks and leaves (6.2)
unchanged.  A gain requires arithmetic control of the phase relation
between different blocks, not more copies of the same mean-square theorem.
The direction (6.4) is a lower bound for the raw extremal; it is not an
upper no-go and it does not survive projection by itself.

## 7. Turan--Nazarov and Beurling--Malliavin audit

For an exponential polynomial with `m` nonzero terms, the
Turan--Nazarov inequality propagates smallness from a subset `E` of an
interval `I` with a factor of the form

```text
(C*abs(I)/abs(E))^(m-1).                             (7.1)
```

The discrete metric-span refinement retains the same order exponent.
Here `m` is at least the effective interpolation order and can be `M` or
the full mode count `D`.  Reversing (7.1) from a high block to the carrier
therefore yields at best an exponentially tiny lower bound, far below
`Y^(-o(1))`.  Applying it after coefficient thresholding also loses the
uncontrolled discarded Wiener mass.  The polarity is not wrong; the
constant is unusable.

Beurling--Malliavin theory sees the prime-log nodes as strongly
underdense relative to bandwidth `Y`: their count on a fixed logarithmic
window is `Y/log Y`.  It consequently supports qualitative `L2`
incompleteness and the existence of bandlimited annihilators.  Its
completeness radius and multiplier conclusions do not bound the Fourier
`l1` norm of such an annihilator, the finite target quotient norm, or the
factorization cost (5.3).  Nor do they preserve two prescribed physical
lobes and endpoint jets.  Importing only its density conclusion repeats
the dimension argument already known to be insufficient.

## 8. Why a power improvement of the natural quadrature is strip-strength

This section concerns the natural von-Mangoldt dual weights, not the
optimized arbitrary coefficients in (2.3).

Let `w` be a smooth dyadic partition weight, normalized so that its
multiplicative dyadic translates sum to one away from a fixed initial
compact interval.  Fix `eta>0` and, for `-eta<=a<=delta`, define

```text
R_(Y,a)(t)
 =integral exp(a*u)*w(u)*exp(-i*t*u)du
  -sum_n Lambda(n)/n*exp(a*log(n/Y))*w(log(n/Y))
                   *exp(-i*t*log(n/Y)).              (8.1)
```

### Proposition 8.1 (natural power quadrature implies a zero-free strip)

Assume, locally uniformly in `a`, that for some fixed `delta,A,eta>0`,

```text
abs(R_(Y,a)(t))<<Y^(-delta)                          (8.2)
```

for every sufficiently large dyadic `Y`, every `-eta<=a<=delta`, and
`abs(t)<=Y^A`.  Then

```text
zeta(s)!=0                    when Re(s)>1-delta.     (8.3)
```

#### Proof

Initially take `1<Re(s)<1+eta`, write

```text
a=1-Re(s),            t=Im(s),
```

and decompose `-zeta'(s)/zeta(s)` and the main integral into dyadic shells.
For a shell at scale `Y`, the centered difference is exactly

```text
Y^(a-i*t)*[-R_(Y,a)(t)],                             (8.4)
```

up to the fixed finite initial shells.  By (8.2), its modulus is

```text
O(Y^(1-Re(s)-delta)).                                (8.5)
```

The same shell functions are analytic in `s`.  Equations (8.2)--(8.5),
now with `a=1-Re(s)` in `[-eta,delta]`, show normal convergence on every
compact subset of the strip

```text
1-delta<Re(s)<1+eta.                                (8.6)
```

On its nonempty overlap with `Re(s)>1`, the series equals the ordinary
Dirichlet series minus its main integral.  It therefore analytically
continues

```text
-zeta'(s)/zeta(s)-1/(s-1)                           (8.7)
```

through the strip, while its usual Dirichlet-series definition covers the
remaining half-plane to the right.  A zeta zero with `Re(s)>1-delta` would
give a pole of (8.7), proving (8.3).  For each fixed `t`, the condition
`abs(t)<=Y^A` holds on every sufficiently large tail shell.  QED

Thus improving the KMT natural residual from a logarithmic saving to a
uniform fixed power for the required smooth-weight family is already a
zero-free-strip theorem.  This does not prove that the optimized atomic
distance lacks a power upper bound: arbitrary dual coefficients need not
be von-Mangoldt weights.  It does show why a routine refinement of the
existing arithmetic quadrature should not be expected to settle the gate.

## 9. Audited conclusion

The requested projected lower

```text
E_ad(Y)>=Y^(-o(1))                                  (9.1)
```

remains open.  The requested arbitrary-seed actual-prime power upper also
remains open.  What is unconditional here is:

1. the exact projection polarity (1.2)--(1.5);
2. the fixed-power carrier upper (3.3) for every subpower-delocalized seed;
3. the coherent short-bump counterexample to any deduction of a
   fixed-power same-lobe cost from uncertainty and support alone;
4. the Vandermonde/tail-cost identification of where exact prime nulling
   reenters; and
5. the strip-strength implication for a fixed-power natural
   von-Mangoldt quadrature.

The arithmetic and projection gates therefore cannot be replaced by a
dimension count, repeated high blocks, a raw Riesz margin, or an
unquantified completeness theorem.  No zero-free strip is claimed.

## Primary sources used for the imported inputs

- H. L. Montgomery and R. C. Vaughan,
  [*Hilbert's inequality*](https://doi.org/10.1112/jlms/s2-8.1.73),
  especially the separated-node cosecant inequality.
- O. Klurman, A. Mangerel, and J. Teravainen,
  [*Multiplicative functions in short arithmetic progressions*](https://doi.org/10.1112/plms.12546),
  Lemma 7.9 and Remark 7.2 for the natural prime-twist upper bound.
- F. L. Nazarov,
  [*Local estimates of exponential polynomials and their applications to
  inequalities of uncertainty-principle type*](https://www.mathnet.ru/eng/aa397),
  for the Turan--Nazarov local estimate.
- O. Friedland and Y. Yomdin,
  [*An observation on the Turan--Nazarov inequality*](https://arxiv.org/abs/1107.0039),
  for the discrete metric-span refinement.
- A. Beurling and P. Malliavin,
  [*On Fourier transforms of measures with compact support*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5937-11511_2006_Article_BF02545792.pdf),
  Acta Mathematica 107 (1962), 291--309.
