# QP balanced cross-side tensor: the `q^2` character barrier

**Date:** 2026-08-15  
**Verdict:** the best coefficient-uniform bound proved for the balanced
cross-side cubic tensor remains the raw Schur scale

```text
R^(1/2)=q^((2-A)/2).
```

At `A=50/33` this is `q^(8/33)`, so this route does **not** lower the
full-shell transverse exponent `49/66`.

The obstruction is stronger than a failure of Burgess.  Character
Parseval modulo `q^2` forces some nonprincipal residual coefficient to have
size at least

```text
sqrt(qR)=q^(1/2)sqrt(R)
```

for every prime `q`.  Thus even an ideal square-root character estimate,
or a density-one large-sieve theorem attaining it, is a factor `q^(1/2)`
too large for the coefficient-uniform tensor problem.  Fibre and pair
codegrees still give `sqrt(R)`, and their restricted-set interpolation is
sharp at the level of those inputs.

This is a method barrier.  It is not an actual-node example proving that
the tensor norm is `>>sqrt(R)`.

---

## 1. The balanced relation and the rigorous baseline

Let

```text
q be an odd prime,             Y=q/2,
B=Y^A,                         3/2<A<2,
R=q^2/B=q^(h+o(1)),            h=2-A<1/2,
D=qR=q^3/B=q^(1+h+o(1)).                         (1.1)
```

The cross-side term left after the two pure one-sided cubics is supported
on

```text
|8abc-q^3|<=C_wD,              a,b,c asyp_w q,     (1.2)
```

with `a,b,c` actual prime powers.  For a fixed pair `(a,b)`, the interval
for `c` has length

```text
O(D/q^2)=O(R/q)=o(1),                            (1.3)
```

so at most one integer `c` occurs.  For fixed `c`, the product `ab` lies
in an interval of length `O(D/q)=O(R)`.  A fixed integer has `O_w(1)`
ordered representations by two shell prime powers.  Hence every `c` has
degree `O_w(R)`.

For arbitrary coefficient vectors, Cauchy--Schwarz first over edges and
then over the fixed-`c` fibres gives

```text
|T(x,y,z)|<<_w sqrt(R)||x||_2||y||_2||z||_2.     (1.4)
```

This proves tensor exponent `h/2`.  At the active aperture,

```text
h=16/33,             h/2=8/33,
1/2+h/2=49/66.                                  (1.5)
```

---

## 2. What reduction modulo `q^2` retains and loses

Let `I_D` be the unit residue classes modulo `q^2` represented by integers
`r` with `0<|r|<=C_wD`.  Since `D=o(q^2)`, these representatives are
distinct.  Every solution of (1.2) satisfies

```text
8abc mod q^2 in I_D.                              (2.1)
```

The converse need not hold: reduction modulo `q^2` forgets which lift by a
multiple of `q^2` is the target lift near `q^3`.  Thus the character count
below is a majorant, not an identity.  The exact identity is obtained
modulo `q^3`; see
`ZETA23-QP-BALANCED-ALL-PLUS-CHARACTER-METHOD-BARRIER-2026-08-15.md`.

For sets `A_0,B_0,C_0` of nodes, write their cardinalities as `X,Y,Z`.
Multiplicative-character orthogonality modulo `q^2`, after dropping only
the target-lift condition, gives

```text
E_D(A_0,B_0,C_0)
 <= (D/phi(q^2))XYZ+N_D
 << (R/q)XYZ+N_D.                                 (2.2)
```

All shell nodes are less than `q` for the project width.  Therefore a
congruence between two products of two nodes modulo `q^2` is an equality.
Bounded prime-power product multiplicity gives

```text
(1/phi(q^2)) sum_chi |Ahat(chi)|^4 <<_w X^2,       (2.3)
```

and analogously for `B_0`; Parseval gives the second moment for `C_0`.
Consequently the standard `(L^4,L^4,L^2)` closure is

```text
|N_D|<<_w S_D sqrt(XYZ),                          (2.4)
S_D=max_(chi nonprincipal)|sum_(r in I_D)chi(r)|.
```

Thus the normalized nonprincipal cost is `S_D`, independently of the set
sizes.

---

## 3. Parseval is already too large

Put `Phi=phi(q^2)` and `L=|I_D|asymp D`.  Character Parseval gives

```text
sum_chi |sum_(r in I_D)chi(r)|^2=Phi L.            (3.1)
```

After removing the principal coefficient of size `L`,

```text
S_D^2 >=(Phi L-L^2)/(Phi-1)asymp D,               (3.2)
S_D>>sqrt(D)=sqrt(qR)=q^(1/2)sqrt(R).              (3.3)
```

This holds for every `q`, not merely for an exceptional sequence.  Hence:

1. Burgess cannot repair (2.4); its upper bound is weaker than the
   square-root scale relevant here.
2. A density-one multiplicative large sieve cannot repair it either.  Even
   a hypothetical optimal upper bound `S_D<=D^(1/2)q^o(1)` would remain a
   factor `q^(1/2)` above (1.4).
3. Replacing the maximum by a standard Hölder norm does not help.  On the
   probability character space every `L^p` norm with `p>=2` is at least the
   `L^2` norm `asymp sqrt(D)`.

Coefficient adaptivity is essential here: the dual vector is chosen after
the center, so an average over characters cannot simply discard the large
character modes.  A useful theorem must instead control their **joint**
correlation with all three restricted prime-power transforms.

---

## 4. Exact fibre/codegree optimization

Sort the set sizes as

```text
X<=Y<=Z.                                           (4.1)
```

Besides (2.2), the integer geometry gives

```text
E_D<<_w RX,                 E_D<<XY.               (4.2)
```

The first is the fixed-smallest-coordinate fibre bound; the second says
that a pair determines at most one third coordinate.  After division by
`sqrt(XYZ)`, their minimum is

```text
sqrt(X/Z) min(R/sqrt(Y),sqrt(Y))<=sqrt(R).         (4.3)
```

Equality in this numerical interpolation occurs at `X=Y=Z=R`.  Thus the
fibre/pair package alone has no power below Schur.  As in the exact
`q^3` audit, a multiplicative Latin-square hypergraph of order `R`
realizes this abstract equality.  It is not asserted that the actual
prime-power hypergraph does so.

It is informative to delete the nonprincipal term formally.  The three
remaining normalized bounds are

```text
p=(R/q)sqrt(XYZ),
f=R sqrt(X/(YZ)),
g=sqrt(XY/Z).                                      (4.4)
```

For `X<=sqrt(q)`, `min(p,f)<=sqrt(pf)<=R/q^(1/4)`.
For `X>=sqrt(q)`, `f<=R/sqrt(Z)<=R/q^(1/4)`.  Hence

```text
min(p,f,g)<=R/q^(1/4),                             (4.5)
```

and equality is attained at `X=Y=Z=sqrt(q)` because `h<1/2`.
Therefore a genuinely joint theorem which removed the discrepancy could,
at best within this interpolation, expose tensor exponent

```text
h-1/4.                                             (4.6)
```

At `h=16/33`, this hypothetical ledger is

```text
h-1/4=31/132,
1/2+h-1/4=97/132,                                  (4.7)
```

only `1/132` below `49/66=98/132`.  Equation (4.7) is **not proved** for
the tensor; it measures the value of the missing joint discrepancy input.

---

## 5. Binary conclusion

```text
balanced cross-side tensor <<sqrt(R):               PROVED;
active tensor exponent 8/33:                         PROVED;
q^2 character/fibre/codegree fixed-power gain:       NO;
density-one max-character gain:                      IMPOSSIBLE IN THIS SCHEME;
hypothetical principal-only transverse 97/132:       NOT PROVED;
actual tensor saturation at sqrt(R):                 NOT PROVED;
full-shell exponent below 49/66:                     NOT PROVED;
QP or strip consequence:                             NOT PROVED.
```

The next viable target is a quotient-localized joint character theorem, or
a curvature/incidence estimate for `abc=q^3/8` which excludes dense actual
prime-power Latin subsquares.  Separate character sums, exact product
multiplicity, fixed-fibre bounds, and large-sieve exceptional sets do not
supply it.

Executable ledger checks:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_balanced_cross_tensor_barrier.py
```
