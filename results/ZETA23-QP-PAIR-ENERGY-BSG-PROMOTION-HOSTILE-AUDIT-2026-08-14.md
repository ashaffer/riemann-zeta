# QP pair-energy / weighted-BSG promotion hostile audit

**Date:** 2026-08-14

**Verdict:** the proposed first pair-energy lemma is correct, including its
`C^4 Y^o(1)` packet count.  The proposed promotion from that lemma to a
rank-one arithmetic-progression shadow is not valid.  The strongest generic
conclusion is only

```text
unit-cell L2 concentration       >= C^-6 Y^-o(1),
weighted additive energy         >= C^-8 Y^-o(1).
```

A weighted Balog--Szemeredi--Gowers theorem may then extract a translate of
a `C^O(1)` approximate group carrying `C^-O(1)` of the normalized variation.
It does not extract the whole representing measure, preserve the vector
identity, preserve the coefficient signs, produce a positive antipode, or
reduce a multidimensional generalized progression to the one translated AP
handled by the existing shadow theorem.

This is not merely a gap in constants.  Two exact countermodels saturate the
entire ledger.

1. A **Bessel-saturated positive antipode** supported on `C^2` mutually
   orthogonal feature packets has all good-pair probability on the diagonal,
   exactly `C^-2`, and no off-diagonal additive structure.
2. A union of `C^2` unrelated AP islands, each of mass `C^-2` and length
   `asymp C^4`, has a common allowed within-island difference set of size
   `asymp C^4`, total support `asymp C^6`, and weighted energy `asymp C^-8`.
   BSG can extract one island, but that island carries only `C^-2` mass and
   need not carry any fraction of the carrier identity.

The second countermodel is an exact finite subset of a torsion-free abelian
group and embeds additively in the real line.  The first is an exact Hilbert
feature model satisfying the **positive antipode** and Gram identities.  It
does not assert realizability by the actual prime-log cosine orbit; rather,
it proves that any successful continuation must use an additional
orbit-specific theorem absent from pair energy, BSG, Freiman theory, and
positivity alone.

The pair-energy route is also strictly weaker in concentration than the
already-proved one-point exceptional-packet theorem.  The latter places
normalized mass `gg C^-1` in only `C^2 Y^o(1)` packets; the pair route places
pair probability `gg C^-2` in `C^4 Y^o(1)` allowed relative packets and only
forces one cell of mass `gg C^-6`.

No QP promotion, QP kill, zeta bound, or zero-free strip is proved here.

---

## 1. Exact starting identity

Let

```text
a(t)=(cos(t u_n))_(n<=M),
q_0=(1,...,1),
S(x)=<q_0,a(x)>,
K(s,t)=<a(s),a(t)>
      =[S(t-s)+S(t+s)]/2.                              (1.1)
```

Suppose that a real signed measure `mu` satisfies

```text
integral a(t) dmu(t)=q_0,       ||mu||_TV=C.            (1.2)
```

Then

```text
M=||q_0||^2=double_integral K(s,t)dmu(s)dmu(t).         (1.3)
```

Since `|K|<=M`, put

```text
E={|K(s,t)|>=M/(2C^2)}.                                (1.4)
```

Writing `m=(|mu| x |mu|)(E)`, absolute values in (1.3) give

```text
M <= M m +[M/(2C^2)](C^2-m),
m >= C^2/(2C^2-1)>1/2.                                (1.5)
```

Thus for `nu=|mu|/C`,

```text
(nu x nu)(E)>=1/(2C^2-1).                              (1.6)
```

This proves the proposed pair lemma, with a slightly sharper constant.

From (1.1), membership in `E` forces at least one of

```text
|S(t-s)|>=M/(2C^2),       |S(t+s)|>=M/(2C^2).          (1.7)
```

Consequently one of the difference and sum branches has normalized pair
mass at least

```text
eta_C=1/[2(2C^2-1)] >=1/(4C^2).                        (1.8)
```

At the threshold in (1.7), the Guth--Maynard actual-integer large-values
theorem gives a cover by

```text
R<=C^4 Y^o(1)                                          (1.9)
```

fixed-width packets.  Up to harmless absolute factors, this part of the
proposed chain is sound.

## 2. Strongest unconditional cell and energy consequences

Partition the high-time interval into unit cells and write

```text
p_j=nu([j,j+1)),       sum_j p_j=1.                    (2.1)
```

A radius-one difference packet meets at most five cell offsets.  The same
is true after reflecting one copy for a sum packet.  If `D` is the resulting
set of at most `5R` offsets, then the branch in (1.8) gives

```text
eta_C <=sum_(d in D) sum_j p_j p_(j+d).                 (2.2)
```

Every shifted correlation is at most `sum_j p_j^2` by Cauchy--Schwarz.
Therefore

```text
sum_j p_j^2 >=eta_C/(5R)
             >=1/(20 R C^2)
             =C^-6 Y^-o(1).                            (2.3)
```

In particular some unit cell has normalized mass at least the right side
of (2.3).  This is an effective-sparsity statement, not a low-doubling
statement and not a carrier representation.

There is a valid weighted-energy consequence.  Put

```text
c_d=sum_j p_j p_(j+d).
```

Cauchy over `D` yields

```text
sum_d c_d^2 >=eta_C^2/(5R)
             >=1/(80 R C^4)
             =C^-8 Y^-o(1).                            (2.4)
```

For the sum branch, reflect one copy; equivalently use that the `L2` norms
of `p*p` and `p*tilde(p)` agree.  Thus sum versus difference changes no
exponent in (2.4), but it does change the **geometry of the extracted
subsets**, as Section 7 records.

At the promotion cost `C=Y^kappa`, `kappa=.0180303234`, these scales are

```text
C^2 =Y^.0360606468,
C^4 =Y^.0721212936,
C^6 =Y^.1081819404,
C^8 =Y^.1442425872.                                    (2.5)
```

None is `Y^o(1)`.

## 3. The one-point theorem dominates the concentration ledger

Pairing (1.2) directly with `q_0` gives

```text
M=integral S(t)dmu(t).                                  (3.1)
```

For

```text
F={|S(t)|>=M/(2C)},                                     (3.2)
```

the same split gives the exact lower bound

```text
|mu|(F)>=C/(2C-1),
nu(F)>=1/(2C-1) asymp C^-1.                             (3.3)
```

The actual large-values theorem covers `F` by only

```text
R_1<=C^2 Y^o(1)                                        (3.4)
```

unit packets.  Hence one unit cell carries normalized mass

```text
gg C^-3 Y^-o(1),                                       (3.5)
```

versus only `C^-6 Y^-o(1)` in (2.3).  For a positive antipode

```text
integral a dnu=-q_0/C,                                 (3.6)
```

one may retain orientation: probability `gg C^-1` lies where

```text
S(t)<=-M/(2C).                                         (3.7)
```

Thus pair energy does not improve the known localization theorem.  Its only
possible added value would be relational structure between exceptional
packets.  The countermodels below show that no such useful structure follows
generically.

## 4. What weighted BSG actually supplies

There is no literature gap at the level of existence of a weighted theorem.
The `L2`-flattening form of weighted BSG says, schematically, that if a
probability measure fails to flatten under convolution by a factor `K`,
then a translate of a `K^O(1)` approximate group carries `K^-O(1)` mass.

Equation (2.4) makes such a theorem applicable after discretization and
symmetrization.  Since

```text
||p*tilde(p)||_2 >= C^-4 Y^-o(1),       ||p||_2<=1,     (4.1)
```

one may take `K=C^4Y^o(1)` in a coarse application.  The resulting valid
conclusion has the form

```text
there exist H,x with
H a C^O(1)-approximate group,
nu(x+H)>=C^-O(1).                                      (4.2)
```

This does **not** imply any of the following statements needed by the AP
shadow route:

```text
the whole support lies in x+H;                          false in general;
the discarded measure has zero carrier contribution;   unavailable;
the restriction to x+H still represents q_0;            unavailable;
H has rank one;                                         false in general;
the support is an exact AP rather than unit-close to H; unavailable;
the signed coefficients have one antipodal sign;        lost on |mu|.
```

This boundary is explicit in the primary literature.

* [Tao, *Product set estimates for non-commutative groups*](https://arxiv.org/abs/math/0601431)
  develops discrete, continuous, and metric-entropy BSG.  Its conclusion is
  large intersection with translates of an approximate group, not a
  carrier-preserving decomposition.
* [Reiher--Schoen, *Note on the Theorem of Balog, Szemeredi, and Gowers*](https://arxiv.org/abs/2308.10245)
  proves essentially optimal bounds for the size of a structured subset and
  gives examples showing that BSG cannot in general return most of the
  original set.
* [Green, *The asymmetric Balog--Szemeredi--Gowers theorem*](https://people.maths.ox.ac.uk/greenbj/papers/asym-BSG.pdf)
  gives a union-of-translates conclusion in its strong asymmetric regime,
  again not one translate carrying the original linear identity.

No weighted version can evade the examples in Sections 5--6, because those
examples already satisfy the weighted conclusions sharply.

## 5. Exact positive-antipode Bessel saturation

Fix an integer `C>=1` and put `J=C^2`.  Let

```text
x_1,...,x_J
```

be orthonormal unit vectors and define

```text
e=-(1/C)sum_(j<=J)x_j.                                  (5.1)
```

Since `J=C^2`, `e` is a unit vector and

```text
<e,x_j>=-1/C,
(1/J)sum_j x_j=-e/C.                                   (5.2)
```

After scaling `e,x_j` by `sqrt(M)`, let `q_0=sqrt(M)e` and let `nu` be the
uniform probability on the scaled `x_j`.  Then

```text
integral a dnu=-q_0/C.                                 (5.3)
```

Thus (5.3) is a genuine positive antipode of depth `1/C`; equivalently
`mu=-C nu` represents `q_0` with TV cost `C`.  Yet

```text
K(i,j)/M=1_(i=j).                                      (5.4)
```

At the pair threshold `M/(2C^2)`, the good graph is exactly the diagonal:

```text
(nu x nu)(E)=1/J=1/C^2,
(|mu| x |mu|)(E)=1.                                    (5.5)
```

There is no off-diagonal additive relation to feed to BSG.  At the same
time every atom saturates the one-point scale:

```text
<q_0,a_j>=-M/C.                                        (5.6)
```

This is the exact `C^2`-packet Bessel boundary already visible in the
augmented-span audit.  It proves that **positivity of the antipode does not
repair the pair-energy chain**.  To exclude (5.1)--(5.6) for QP one needs a
new theorem about the actual one-parameter cosine orbit, not a generic Gram,
convexity, or additive-energy theorem.

## 6. Exact AP-island nontransfer model

Let `C>=2`, `J=C^2`, and

```text
L=floor((C^4+1)/2).                                    (6.1)
```

In the free abelian group on `e_0,e_1,...,e_J`, put

```text
A_j={k e_0+e_j:0<=k<L},       A=union_(j<=J)A_j.        (6.2)
```

For the uniform probability on `A`,

```text
|A|=JL asymp C^6/2,
mass(A_j)=1/J=C^-2.                                    (6.3)
```

Pairs in a common island have differences in

```text
D={h e_0:|h|<L},       |D|=2L-1<=C^4,                 (6.4)
```

and their total probability is exactly

```text
sum_j mass(A_j)^2=1/J=C^-2.                            (6.5)
```

Thus (6.2) simultaneously saturates pair density `C^-2`, allowed packet
count `C^4`, and effective support `C^6`.

The exact interval energy is

```text
E_L=sum_(|h|<L)(L-|h|)^2=(2L^3+L)/3.                   (6.6)
```

Pooling the within-island differences and keeping all ordered transverse
differences gives

```text
E(A)=J(2J-1)E_L,
E(A)/|A|^4 asymp C^-8.                                 (6.7)
```

Hence the model also saturates the weighted energy (2.4).  BSG can validly
extract one AP island.  It carries only `C^-2` of the measure, and pair
energy supplies no statement that its signed vector contribution is a
nonzero multiple of `q_0`.

Moreover the difference subgroup of `A` contains

```text
e_0, e_2-e_1,...,e_J-e_1
```

and has rank `J`.  Therefore `A` is not contained in any rank-one AP.  The
group embeds in `R` by mapping its basis to Q-linearly independent reals,
so this is not a torsion artifact.  For example one may use scaled square
roots of distinct primes for the island translates.

This directly refutes the missing transfer

```text
one BSG-structured component
   --false--> full representing measure lies in one AP shadow.            (6.8)
```

## 7. Four further scope failures

### 7.1 Freiman gives a generalized AP, not an AP

Even maximal energy does not force rank one.  For Q-linearly independent
`alpha,beta`, the real set

```text
G_n={i alpha+j beta:0<=i,j<n}                           (7.1)
```

has

```text
|G_n|=n^2,
|G_n+G_n|=(2n-1)^2,
E(G_n)=[(2n^3+n)/3]^2 asymp(4/9)|G_n|^3,               (7.2)
```

but cannot lie in a rank-one AP: otherwise both `alpha` and `beta` would be
integer multiples of one step, contradicting their irrational ratio.

[Green--Ruzsa, *Freiman's theorem in an arbitrary abelian group*](https://arxiv.org/abs/math/0505198)
and [Chang, *A polynomial bound in Freiman's theorem*](https://doi.org/10.1215/S0012-7094-02-11331-3)
conclude containment in a **multidimensional** progression.  Neither theorem
collapses (7.1) to the rank-one AP family controlled by the current shadow
theorem.  Here the doubling parameters are powers of `C`, not fixed
constants, so even the resulting rank is not uniformly bounded.

### 7.2 The sum branch can be a bipartite matching

In a free abelian group take

```text
A={e_i:i<=N},       B={g-e_i:i<=N},                    (7.3)
```

and retain the `N` matching edges.  Their restricted sumset is the singleton
`{g}`, but the edge density is only `1/N`; every connected component is one
edge.  At `N=C^2` this exactly matches the pair density.  Reflecting `B`
turns this into a difference relation, but BSG can extract only singleton
scale structure.  It does not create a same-side AP carrying the measure.

Thus the identity

```text
K=[S(t-s)+S(t+s)]/2                                    (7.4)
```

must not be treated as a same-set difference-energy theorem without an
explicit bipartite audit.

### 7.3 Signed pair geometry does not orient an antipode

In one coordinate let `a=1/2` and `mu=2 delta_a`.  Then

```text
integral a dmu=1,       C=2,
double_integral K dmu dmu=1,
K=1/4>M/(2C^2)=1/8.                                   (7.5)
```

But `conv{1/2}` contains no negative multiple of the carrier `1`.  The value
`1/2` is an actual cosine value, and can occur at arbitrarily high times by
adding periods.  Hence a cheap signed representation plus maximal pair
concentration does not imply the positive-antipode condition.

For QP the proof tree already records this distinction: the signed target
requires a separately proved positivity/compact-state adapter.  BSG does not
supply that adapter because it is applied to `|mu|`.

### 7.4 Complex measures add no useful escape

Because every `a(t)` and `q_0` is real, if a complex measure represents
`q_0`, then its real part also represents `q_0` and

```text
||Re(mu)||_TV<=||mu||_TV.                               (7.6)
```

Thus complex measures cannot lower the optimum.  If one nevertheless runs
the pair identity complex-bilinearly, passing to total variation erases all
phases before BSG.  Null imaginary or signed components can dominate the
extracted geometry while contributing nothing to the carrier.  A phase
reconstruction theorem would be an additional hypothesis, not a consequence
of weighted additive energy.

## 8. Fourier and large-spectrum literature boundary

The closest Fourier inverse theorems do not repair the transfer.

* [Lee, *Covering the large spectrum and generalized Riesz products*](https://arxiv.org/abs/1508.07109)
  treats large spectra of probability distributions on finite abelian groups
  and obtains containment in a low-dimensional span.  A span is not one AP,
  and the finite-group character setting is not the continuous log-prime
  frequency problem here.
* [Ramare, *Rudin Inequality, Chang Theorem, primes and squares*](https://arxiv.org/abs/2501.05056)
  proves additive structure for large values of trigonometric polynomials
  supported on **integer primes**, subject to quantitative dissociation and
  rational-separation conditions.  QP uses frequencies `log p` and a
  continuous time variable.  The theorem does not transfer, and even its
  conclusion is multi-generator/projection structure rather than rank one.
* Wiener's Fourier--Stieltjes theorem identifies atomic mass from a full
  long Cesaro average of squared Fourier coefficients.  The QP input is a
  finite selected collection of prime-log samples and exceptional time
  packets, not such an average.  It gives no atom, periodicity, or AP
  decomposition here.

No primary source found in this audit proves a carrier-preserving weighted
BSG theorem, a rank-one inverse theorem for the present continuous
prime-log orbit, or a theorem upgrading a structured `C^-O(1)` restriction
to a positive antipode for the whole measure.

## 9. Exact disposition

```text
pair Gram identity:                                      PROVED;
good-pair absolute mass >=1/2:                          PROVED;
sum/difference packet cover R<=C^4 Y^o:                 PROVED;
unit-cell L2 concentration >=C^-6 Y^-o:                 PROVED;
weighted additive energy >=C^-8 Y^-o:                   PROVED;
weighted/metric BSG applicability:                       VALID;
BSG output preserves the carrier identity:              FALSE GENERICALLY;
Freiman output has rank one:                             FALSE;
signed representation implies positive antipode:        FALSE;
positive antipode removes diagonal/island saturation:    FALSE ABSTRACTLY;
pair route improves one-point packet localization:       FALSE;
actual prime-log orbit excludes the countermodels:       OPEN;
QP-PROMOTE:                                              OPEN;
zero-free strip:                                         NOT PROVED.
```

The only admissible revival is an actual-orbit theorem of roughly the
following form:

```text
Every positive measure on the high prime-log cosine orbit with
integral a dnu=-q_0/C has one structured component which itself carries
a quantitatively nonnegligible negative q_0 component, and that component
lies in a rank-one family covered by the AP shadow theorem.               (9.1)
```

Pair energy, positivity, BSG, Freiman theory, and existing large-spectrum
theorems do not imply (9.1).  Proving it would require new deterministic
transversality of the actual prime-log orbit.

## 10. Replay

```bash
python3 src/test_qp_pair_energy_bsg_audit.py
python3 results/verify_zeta23_qp_pair_energy_bsg_audit.py
python3 src/qp_pair_energy_bsg_audit.py
```
