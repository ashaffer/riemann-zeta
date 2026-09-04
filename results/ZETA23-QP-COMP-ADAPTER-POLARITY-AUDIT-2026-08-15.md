# QP `COMP(lambda)` adapter: polarity and quantitative-resonance audit

**Date:** 2026-08-15  
**Binary verdict:** **NOT PROVED.**  Neither `COMP(lambda)` for any fixed
`lambda>0` nor a different implication from the present fixed-power DPA/QP
statement to a zeta zero-free strip is obtained here.

There is an exact reason that the obvious minimax, averaging, convolution,
and zero-contrapositive arguments do not supply the adapter.  A QP antipode
controls every coefficient vector in the direction opposite to the one
needed by `COMP`: it forces the canonical transform to have a value of
modulus at least the antipode depth.  It gives no upper bound for that
transform.  Multiplicative convolution merely iterates the same
wrong-polarity eigenvalue.

A perturbed Fejer family below also shows that rational independence, exact
Sidon/unique-factorization consequences, node separation, and an arbitrarily
long but finite polynomial aperture cannot repair the polarity.  A proof for
the complete actual-prime shell would need a new *quantitative*
anti-resonance theorem at resolution `1/B`, together with a comparison of the
worst adaptive signed direction with the canonical prime direction.  That is
precisely substantive strip-strength input, not a consequence presently
available from QP.

Nothing below disproves the literal arithmetic statement `COMP(lambda)` for
the actual complete prime shells.  The conclusion is deliberately binary:
the requested adapter remains open.

---

## 1. The exact antipode operator points the other way

Let `u_1,...,u_M` be any nonzero nodes, let `H` be compact, and suppose a
depth-`r` positive antipode is represented by a probability `nu` on `H`:

```text
integral_H cos(s u_j) dnu(s)=-r,             1<=j<=M.       (1.1)
```

For arbitrary complex coefficients `a_j`, put

```text
F_a(t)=sum_j a_j exp(i t u_j),
P_a(t)=sum_j a_j cos(t u_j).                          (1.2)
```

Then the following identities are exact:

```text
integral_H P_a(s)dnu(s)=-r sum_j a_j,                 (1.3)

integral_H [F_a(t+s)+F_a(t-s)]/2 dnu(s)=-r F_a(t).    (1.4)
```

Indeed, (1.3) is (1.1) paired with `a`; (1.4) follows from

```text
[exp(i(t+s)u)+exp(i(t-s)u)]/2
   =exp(i t u)cos(su).                                (1.5)
```

In particular, for every probability vector `a_j>=0`, `sum a_j=1`,

```text
min_(s in H) P_a(s)<=-r,
sup_(s in H)|F_a(s)|>=r.                              (1.6)
```

Thus the canonical unweighted or von-Mangoldt probability is forced to have
**at least** depth `r` somewhere.  The proposed comparison needs the reverse
kind of statement,

```text
sup |F_canonical| <= C r^lambda.                      (1.7)
```

No rearrangement of (1.3) yields (1.7).

Define the translation-average operator

```text
(T_nu F)(t)=integral_H [F(t+s)+F(t-s)]/2 dnu(s).      (1.8)
```

Equation (1.4) says `T_nu F_a=-r F_a`, hence

```text
T_nu^k F_a=(-r)^k F_a.                               (1.9)
```

Because `T_nu` is a contraction in the supremum norm, iteration gives only
the tautology `r^k||F_a||_infinity<=||F_a||_infinity`.  This closes the
direct averaging, random-walk, and convolution versions of the proposed
adapter.

The signed DPA dual has the same gap.  It supplies one adaptive vector `y`
with `sum y_j=1` and a one-sided bound for `P_y`.  The canonical prime vector
is a different direction.  Passing from one to the other requires a bound on
the relevant coefficient-change operator (or its projected Gram inverse);
QP itself contains no such bound.

---

## 2. Quantitative Fejer stress test

The obstruction persists after exact rational relations are removed.

Fix `w>0`, an integer `M>=2`, and set

```text
u_j=jw/M,                         1<=j<=M,
lambda_j=2(M+1-j)/[M(M+1)].                         (2.1)
```

The Fejer identity gives, on the whole real line,

```text
P(t)=sum_(j=1)^M lambda_j cos(tu_j)>=-1/M.            (2.2)
```

Let `H subset [-B,B]` contain `t_*=2 pi M/w`, with `B>=t_*`, and
perturb to

```text
u'_j=u_j+epsilon_j,
max_j |epsilon_j|<=delta<=1/(MB).                    (2.3)
```

Since cosine is one-Lipschitz,

```text
sum_j lambda_j cos(tu'_j)>=-1/M-B delta>=-2/M
                                      for |t|<=B.    (2.4)
```

Consequently the Delsarte/antipode duality gives

```text
r_+(H)<=2/M.                                          (2.5)
```

On the other hand, for the *uniform* node measure,

```text
F_unif(t)=M^(-1)sum_j exp(i t u'_j),
|F_unif(t_*)|>=1-t_* delta>=1-1/M.                   (2.6)
```

The perturbations in (2.3) may be chosen arbitrarily small and
`Q`-linearly independent: the complement is only a countable union of
proper rational hyperplanes.  Such a set also has the exact additive-Sidon
consequences normally obtained from unique factorization of independent
prime logarithms.

For any fixed `C` and `lambda>0`, (2.5)--(2.6) violate

```text
sup |F_unif|<=C r_+^lambda                            (2.7)
```

as `M` tends to infinity.  Therefore rational independence, full spark,
exact absence of multiplicative relations, and a finite aperture by
themselves cannot prove `COMP(lambda)`.  What distinguishes the complete
actual-prime shell, if (1.7) is true there, must be quantitative exclusion of
the near-grid resonance in (2.3) at the scale

```text
max_j |epsilon_j| << 1/B.                            (2.8)
```

Qualitative unique factorization says nothing at resolution (2.8).

---

## 3. Why a zero contrapositive does not close the gap

A zero `rho=beta+iT` can be localized, by the explicit formula or Turan's
power-sum method, into a large canonical von-Mangoldt/prime Dirichlet
polynomial near ordinate `T`.  This is one scalar statement in the
canonical coefficient direction.

To contradict DPA one must instead prove that **every** adaptive vector `y`
with `sum y=1` has a positive excursion exceeding its alleged DPA margin.
Pairing a zero-produced canonical large value with such a `y` requires one
of the following equivalent new inputs:

```text
* a coefficient-change bound from y to the canonical prime vector;
* a source-sensitive projected-Gram inverse bound;
* a lower bound correlating every DPA separator with Lambda;
* the comparison COMP(lambda) itself.                (3.1)
```

The explicit formula supplies none of these: its coefficients are fixed as
`Lambda(n)`, while DPA permits unrelated signed coefficients at every shell.
Using a natural fixed-power prime-twist estimate at (3.1) would be circular,
since the audited Turan localization already turns that estimate into the
desired strip.

The moving-band quantifier is not the principal obstruction for a
contrapositive at a zero of height `T`: one can choose `Y` polynomially
related to `T`.  The coefficient-direction mismatch remains even after that
choice and is exact.

---

## 4. Binary disposition

```text
QP antipode => canonical lower excursion of depth r:       PROVED;
translation/convolution reverses that polarity:            NO;
rational independence / exact Sidon repairs COMP:          FALSE;
zero localization supplies canonical large prime twist:    YES;
canonical zero witness tests every adaptive DPA vector:     NO;
COMP(lambda) for any fixed lambda>0:                        OPEN;
present DPA/QP => uniform zeta strip:                       OPEN.       (4.1)
```

Accordingly this audit supplies a definitive blocker for the proposed
minimax/multiplicative shortcut, not one of the three requested headline
theorems.  It must not be cited as a proof of QP, a strip, or their
equivalence.
