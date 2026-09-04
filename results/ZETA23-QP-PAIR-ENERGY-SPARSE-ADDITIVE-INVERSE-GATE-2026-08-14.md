# QP pair-energy sparse/additive inverse gate

**Date:** 2026-08-14

**Verdict:** the exact pair-energy identity gives a valid actual-prime
relational concentration theorem, but it does **not** improve the existing
one-point packet-compression gate and it does **not** yield the proposed
``sparse or rank-one additive`` inverse theorem.  For a signed carrier
representation of total variation `C`, an oriented fraction

```text
delta >=1/(2C^2-1)                                      (0.1)
```

of all polar pairs has a sum or difference in an actual-prime large-value
set covered by

```text
R<=C^4*Y^o(1)                                           (0.2)
```

unit packets.  After unit-cell discretization the sharp generic conclusions
are only

```text
||w||_2^2 >=delta/R >>C^-6*Y^-o(1),
weighted additive energy >=delta^2/R >>C^-8*Y^-o(1).    (0.3)
```

The already-proved one-point identity puts mass `>>C^-1` in only
`C^2Y^o(1)` packets and therefore gives

```text
||w||_2^2 >>C^-4*Y^-o(1).                               (0.4)
```

Thus pair energy starts two powers of `C` behind the current frontier.

This loss is real.  A diagonal regular-Hadamard simplex obeys the exact
coordinate interpolation and positive-antipode identities with all pair
energy diagonal.  A second model with `C^2` mutually incommensurate AP
islands of `C^4` points each simultaneously saturates (0.1)--(0.3): additive
combinatorics can isolate a small island or a generalized progression, but
not an exact rank-one carrier representation of the whole measure.  The
translated-AP dilation-shadow theorem applies only when the **whole carrier**
has an exact AP representation.  It cannot be applied to an extracted
component of polar mass `C^-2`, and unit-scale additive structure cannot be
upgraded to an exact AP because bounded irrational jitter survives every
packet statement.

These are logical countermodels, not actual-prime cosine nullers.  A theorem
for actual prime-log nodes can still rule them out, but it must use a new
augmented directional minor/simplex-exclusion estimate for the one-parameter
cosine curve.  Pair energy, BSG/Freiman theory, positivity, aperture, and the
present large-value packet counts do not supply that estimate.

No cheap QP construction, power lower bound, promotion, or zero-free strip
is proved here.

---

## 1. Exact setup and polarity

Retain the actual distinct absolute prime-power log nodes

```text
V_Y={|log(n/Y)|: n=p^a in [Y*exp(-w),Y*exp(w)]},
M=#V_Y=Y^(1-o(1)),
a(t)=(cos(t*v))_(v in V_Y),
q_0=(1,...,1),
S_Y(t)=<q_0,a(t)>=sum_(v in V_Y)cos(t*v).                (1.1)
```

The remote QP interpolation problem asks for a signed real measure `mu` on
the legal high-frequency interval such that

```text
integral a(t)dmu(t)=q_0,       ||mu||_TV=C.              (1.2)
```

Write its polar decomposition as

```text
dmu=C*epsilon*dnu,       nu=|mu|/C,       |epsilon|=1.   (1.3)
```

The cosine Gram kernel is exactly

```text
K(s,t)=<a(s),a(t)>
      =1/2[S_Y(t-s)+S_Y(t+s)].                           (1.4)
```

Define the oriented normalized kernel

```text
G(s,t)=epsilon(s)epsilon(t)K(s,t)/M.                     (1.5)
```

Every entry of `a(t)` has absolute value at most one, so `G<=1`.  Notice that
the signs in (1.5) cannot be discarded: replacing `G` by `|K|/M` before
using (1.2) loses the exact barycentric identity.

### Theorem 1.1 (exact oriented pair identity)

Every representation (1.2) satisfies

```text
E_(s,t~nu) G(s,t)=1/C^2.                                 (1.6)
```

#### Proof

By (1.2)--(1.3),

```text
integral epsilon(t)a(t)dnu(t)=q_0/C.
```

Taking its squared Euclidean norm and using `||q_0||^2=M` gives

```text
integral integral epsilon(s)epsilon(t)<a(s),a(t)>
                 dnu(s)dnu(t)=M/C^2,
```

which is (1.6).  QED

---

## 2. The strongest unconditional weighted concentration statements

The following elementary bound is useful because it uses no unjustified
positivity of the kernel.

### Lemma 2.1 (one-sided expectation threshold)

If `X<=1` and `E X=m`, then for every `theta<m`,

```text
P{X>=theta}>=(m-theta)/(1-theta).                        (2.1)
```

#### Proof

If the event has probability `p`, then
`E X<=p+(1-p)theta`.  Rearrangement gives (2.1).  The bound is sharp as an
infimum by a two-point distribution with its lower value tending to
`theta` from below.  QED

### Theorem 2.2 (actual-prime pair concentration)

For the polar probability in (1.3),

```text
(nu x nu){G>=1/(2C^2)}>=1/(2C^2-1).                     (2.2)
```

Every pair in this event obeys at least one of

```text
|S_Y(t-s)|>=M/(2C^2),
|S_Y(t+s)|>=M/(2C^2).                                   (2.3)
```

The set

```text
L_C={u in [-2B,2B]: |S_Y(u)|>=M/(2C^2)}                 (2.4)
```

is covered by at most

```text
C^4*Y^o(1)                                              (2.5)
```

intervals of fixed radius, uniformly for
`C<=Y^(kappa_promote+o(1))`.

#### Proof

Apply Lemma 2.1 to (1.6) with `theta=1/(2C^2)` to obtain
(2.2).  On that event, `|K(s,t)|>=M/(2C^2)`.  Formula (1.4) implies (2.3),
since otherwise the absolute value of their half-sum would be smaller than
`M/(2C^2)`.

For (2.5), apply the actual-integer Dirichlet-polynomial large-values theorem
used in the singular atomic packet gate with its cost parameter `D=C^2`.
On an interval of length `O(B)`, its three terms are

```text
D^2,       Y^(-2/5)D^4,       Y^(50/33-8/5)D^4,
```

hence here

```text
C^4,       Y^(-2/5)C^8,       Y^(50/33-8/5)C^8.         (2.6)
```

At `kappa_promote=.0180303234`, their fixed-power exponents are

```text
.0721212936,
-.2557574128,
.0593941023515.                                         (2.7)
```

The third is below the first by `.0127271912485`, so (2.5) follows.  This
argument works equally on negative lags and across zero because translating
the time interval only modulates the bounded Dirichlet coefficients.  QED

### Theorem 2.3 (carrier roots have relational halos)

Put

```text
X(t)=epsilon(t)S_Y(t)/M.                                 (2.8)
```

Then

```text
nu{X>=1/(2C)}>=1/(2C-1).                                (2.9)
```

For every `t` in that carrier-aligned set,

```text
nu{s:G(t,s)>=1/(4C^2)}>=1/(4C^2-1).                    (2.10)
```

Every neighbor in (2.10) has `t-s` or `t+s` in a set covered by
`O(C^4Y^o(1))` unit packets.

#### Proof

Taking the scalar product of (1.2) with `q_0` gives

```text
E_nu X=1/C.
```

Lemma 2.1 with threshold `1/(2C)` proves (2.9).  For fixed `t`, (1.2) also
gives the exact conditional identity

```text
E_(s~nu)G(t,s)=X(t)/C.                                  (2.11)
```

On the set in (2.9) this is at least `1/(2C^2)`.  Apply Lemma 2.1 at
threshold `1/(4C^2)` to obtain (2.10).  The kernel decomposition (1.4) now
forces one of `|S_Y(t-s)|,|S_Y(t+s)|` to be at least `M/(4C^2)`.
The same large-values calculation as (2.6), now with `D=2C^2`, changes only
absolute constants.  QED

The rooted statement is genuine new information about where the relation is
seen.  It still permits `C^2` unrelated roots, each with a halo of polar mass
`C^-2`, which is exactly the many-island obstruction below.

---

## 3. Unit-cell discretization: the pair route is quantitatively weaker

Let `w=(w_j)` be the probability weights obtained by placing `nu` into unit
cells.  Up to an absolute enlargement of every lag packet, (2.2)--(2.5)
give a set `Lambda` of

```text
R<<C^4Y^o(1)                                             (3.1)
```

allowed discrete sums and differences carrying pair mass

```text
delta>>C^-2.                                             (3.2)
```

### Lemma 3.1 (sharp convolution consequences)

For a probability weight on a discrete abelian group, put

```text
r(d)=sum_x w(x)w(x+d).
```

If `sum_(d in Lambda)r(d)>=delta` and `#Lambda=R`, then

```text
sum_x w(x)^2>=delta/R,                                   (3.3)
sum_d r(d)^2>=delta^2/R.                                 (3.4)
```

The identical statements hold for restricted sums.

#### Proof

Cauchy--Schwarz gives `r(d)<=||w||_2^2` for each `d`; summing over `Lambda`
proves (3.3).  A second Cauchy--Schwarz inequality gives

```text
sum_(d in Lambda)r(d)^2
 >=R^-1[sum_(d in Lambda)r(d)]^2,
```

which proves (3.4).  QED

Substituting (3.1)--(3.2) yields exactly (0.3).  In exponent notation at the
promotion frontier,

```text
pair packet count       4*kappa = .0721212936,
pair mass exponent     -2*kappa =-.0360606468,
pair L2 exponent       -6*kappa =-.1081819404,
pair energy exponent   -8*kappa =-.1442425872.           (3.5)
```

Now compare the positive-polarity carrier event (2.9).  Its mass is
`>>C^-1`, and `|S_Y(t)|>=M/(2C)` there.  The established actual-prime packet
theorem covers this set with `C^2Y^o(1)` unit packets.  Cauchy--Schwarz gives

```text
||w||_2^2 >> (C^-1)^2/C^2=C^-4Y^-o(1).                  (3.6)
```

Thus the pair relation does not pass the existing packet-compression gate:
its best generic effective-support estimate is worse by `C^2`.

---

## 4. Why BSG and Freiman do not repair the loss

Balog--Szemeredi--Gowers converts large additive energy into a **large
subset** of small doubling; it does not say the original weighted carrier
measure lies on one rank-one progression.  The sharp result of
[Reiher--Schoen](https://arxiv.org/abs/2308.10245) obtains, for
`E(A)>=|A|^3/K`, a subset of order `K^-1/2|A|` with difference set bounded by
`O_epsilon(K^4|A'|)`, and explains that the subset size is essentially best
possible.  Weighted input first requires atom splitting or dyadic
regularization, which cannot improve these powers.

Even after small doubling is obtained, the general conclusion is a
generalized/coset arithmetic progression, not a one-dimensional AP; see the
primary Green--Ruzsa theorem,
[Freiman's theorem in an arbitrary abelian group](https://arxiv.org/abs/math/0505198).
Neither theorem preserves the signed carrier equation after throwing away
the complement.

Three separate gaps therefore remain:

1. **mass:** an extracted additive island can have polar mass only `C^-2`;
2. **direction:** its complement can carry the orthogonal coordinates needed
   for the exact interpolation of `q_0`;
3. **exactness:** a unit-packet approximate progression can have arbitrary
   irrational jitter and need not lie on any exact affine lattice.

The remote AP dilation-shadow theorem assumes an identity of the form

```text
q_0=sum_(k in K)c_k a(s+k*tau)                           (4.1)
```

for the full carrier, with `sum|c_k|<=C`.  BSG supplies none of (4.1), an
exact common `tau`, or a TV bound for the extracted subset after the
remainder is residualized.  Applying the AP theorem at that point would be
a non sequitur.

---

## 5. Countermodel I: exact bounded-coordinate diagonal simplex

The diagonal branch is not an artifact of a weak estimate.

### Proposition 5.1 (regular-Hadamard positive antipode)

Let `C=2^m` and `L=C^2`.  There exist `L` vectors

```text
b_1,...,b_L in {+1,-1}^L                              (5.1)
```

such that

```text
<b_i,b_j>/L=1_(i=j),
(1/L)sum_(i<=L)b_i=q_0/C.                               (5.2)
```

Consequently the atoms `a_i=-b_i` obey

```text
(1/L)sum_i a_i=-q_0/C,                                  (5.3)
```

so `-q_0/C` is an exact positive convex antipode.  Equivalently,

```text
q_0=sum_i(-1/C)a_i,       sum_i|-1/C|=C.                (5.4)
```

For the polar measure in (5.4), every atom is exactly carrier-aligned,

```text
epsilon_i<q_0,a_i>/L=1/C,
```

while the oriented normalized pair kernel is

```text
G(i,j)=1_(i=j).                                         (5.5)
```

Thus the entire mean `E G=C^-2` is diagonal and there is no off-diagonal
additive information.

#### Proof

Put `H_4=J_4-2I_4`.  It is a sign matrix satisfying

```text
H_4 H_4^T=4I_4,
H_4 1=2*1,
H_4^T 1=2*1.
```

Take the `m`-fold Kronecker power.  The resulting regular Hadamard matrix
has order `4^m=C^2`, orthogonal rows, and every row and column sum `2^m=C`.
Its rows are the `b_i`.  Equations (5.2)--(5.5) follow directly.  QED

For every positive integer `C`, not only powers of two, the complete block
design consisting of all sign columns with coordinate sum `C` gives the
same identities with more coordinates.  The regular-Hadamard family shows
that the countermodel already fits in the minimal dimension `M=C^2`, far
below the actual QP dimension `M=Y^(1-o(1))` at `C=Y^.018...`.

This model preserves bounded coordinates, exact TV polarity, and the exact
positive antipode.  It does **not** preserve the special one-parameter form
`a(t)=(cos(t v_j))`; exclusion of (5.5) for actual prime-log cosine rows is
precisely an arithmetic augmented-simplex theorem that is presently absent.

### What the diagonal branch really gives

For an atomic polar probability with masses `p_i`, diagonal pair mass is

```text
D=sum_i p_i^2.                                          (5.6)
```

If `D>>C^-2`, its effective participation ratio is `D^-1<<C^2`.  This does
not imply that the heavy atoms themselves represent `q_0`: a diffuse
complement can carry essential transverse cancellation.  Even for a TV
minimizer on an exposed Elfving face, the correct target is the residualized
augmented Cramer ratio, not support cardinality.

For a square support matrix `A=[a(t_1)|...|a(t_M)]`, the exact TV is

```text
sum_i |det A_i(q_0)|/|det A|,                            (5.7)
```

where `A_i(q_0)` replaces column `i` by `q_0`.  A useful sparse theorem must
lower-bound these **directional replacement minors after eliminating the
complement**.  Unaugmented volume, collision mass, or an effective-support
bound does not control (5.7).

---

## 6. Countermodel II: many mutually incompatible AP islands

The off-diagonal/additive branch has a separate sharp obstruction.

### Proposition 6.1 (island saturation)

Let `L=C^2` and `m=C^4`, initially with integer `C`.  Choose a common step
`h>4L+4` and bases `r_1,...,r_L` in one period such that

```text
dist(r_i-r_j,h*Z)>1            for i!=j,                 (6.1)
```

and such that all ratios `(r_i-r_j)/h` are irrational.  This is possible by
choosing bounded, rationally independent perturbations of `4i`.  Put

```text
A_i={r_i+jh:0<=j<m},       A=union_(i<=L)A_i,            (6.2)
```

and give all `Lm=C^6` points equal probability.  Let the allowed lag packets
be the radius-one neighborhoods of

```text
Lambda={dh:-(m-1)<=d<=m-1}.                              (6.3)
```

Then:

```text
#Lambda=2m-1 asymp C^4,
P{x-y lies in Lambda+[-1,1]}=1/L=C^-2,
||w||_2^2=1/(Lm)=C^-6.                                  (6.4)
```

Moreover the restricted additive energy is

```text
[m^2+2*sum_(k<m)k^2]/(L^2m^4) asymp C^-8.              (6.5)
```

No exact affine lattice contains two complete islands.

#### Proof

Within one island all differences lie in (6.3).  Condition (6.1) excludes
every cross-island difference.  The probability that two independent
points choose the same island is `L*(1/L)^2=1/L`, proving the second formula
in (6.4); the other two are immediate.  For lag `dh`, the convolution mass
is `(m-|d|)/(Lm^2)`.  Squaring and summing proves (6.5).

If an affine lattice contains two complete islands, its step divides `h` in
the integer sense, while it also divides their base difference.  Their
ratio must therefore be rational, contrary to the choice of bases.  QED

The executable finite fixture makes only one base perturbation irrational.
That weaker choice already certifies the conclusion that no single exact
affine lattice contains the whole union; it is not a numerical replay of the
stronger pairwise-irrational choice in Proposition 6.1.

This construction has diameter `O(Lm)=O(C^6)` after harmless rescaling of
the fixed separation constants.  At the promotion frontier its exponent is

```text
6*kappa_promote=.1081819404<50/33,                       (6.6)
```

so the legal aperture does not exclude the geometry.  One may translate all
islands beyond `cY/log Y`; no shallow atom is needed.

The construction also survives unit-scale jitter.  More simply, points

```text
j+eta_j,       |eta_j|<.1                               (6.7)
```

have every difference in one of `O(N)` unit packets centered at the integer
lags, while a single irrational ratio among the first three differences
prevents containment in any exact affine lattice.  Hence even a maximally
successful packet-level Freiman conclusion cannot be inserted into the
exact AP dilation-shadow theorem.

Again, Proposition 6.1 is not an actual-prime nuller.  It proves that the
pair-mass/packet-count data, including the full legal aperture, cannot rule
out a union of unrelated additive islands.  Actual coordinate interpolation
would have to couple the islands through new directional information.

---

## 7. Exact disposition of the proposed inverse theorem

The proposed statement

```text
every cheap remote actual-prime nuller is either sparse
or has a carrier-scale rank-one additive support                      (7.1)
```

has the following audited status.

| component | strongest justified result | status |
|---|---|---|
| pair identity | `E G=C^-2` with correct TV signs | **proved** |
| high oriented pairs | mass at least `1/(2C^2-1)` | **proved** |
| actual-prime lag/sum cover | `C^4Y^o(1)` packets | **proved** |
| rooted relational halo | (2.9)--(2.10) | **proved** |
| discrete concentration | `||w||_2^2>>C^-6` | **proved; sharp in scale** |
| additive energy | `>>C^-8` | **proved; sharp in scale** |
| improvement over one-point gate | one-point gives `>>C^-4` | **false** |
| diagonal mass implies sparse carrier representation | simplex/complement obstruction | **false from current inputs** |
| BSG yields full rank-one carrier | islands, remainder, jitter | **false from current inputs** |
| actual-prime cosine curve excludes both models | needs augmented minor theorem | **open** |
| QP-PROMOTE / uniform strip | | **not proved** |

Thus the sparse-versus-additive strategy has failed fast in its generic
form.  It should not consume another iteration unless a new estimate sees
the actual augmented direction.  The clean next theorem is:

> **Actual-prime augmented-simplex exclusion.**  Uniformly for remote
> support points whose polar masses and pair graph satisfy the saturation
> scales above, prove that the actual prime-log cosine rows cannot form a
> `C^2`-vertex near-orthogonal simplex with barycenter `-q_0/C`, or else
> lower-bound the residualized replacement-minor sum (5.7) by
> `Y^(kappa_promote+eta)`.

Anything weaker than a directional estimate remains compatible with both
countermodels.

---

## 8. Reproducibility

The executable gate is

```text
src/qp_pair_inverse_gate.py
```

and checks:

* the exact expectation-threshold constants;
* the cosine product kernel identity;
* the regular-Hadamard and complete-design positive antipodes;
* the multi-island `C^-6` and `C^-8` saturation scales;
* the Guth--Maynard exponent ledger.

Run

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_pair_inverse_gate.py
PYTHONPATH=src python3 src/qp_pair_inverse_gate.py --cost 3 --island-size 40
python3 results/verify_zeta23_qp_pair_inverse_gate.py
```

The current replay result is `5 passed`, and the verifier prints `PASS`.
