# QP balanced all-plus cubic: an exact character-method barrier

**Date:** 2026-08-15  
**Verdict:** no coefficient-uniform improvement over the existing
`sqrt(R)` bound is proved.  The natural multiplicative-character attack can
be made exact modulo `q^3`, but its unavoidable Parseval scale is
`sqrt(qR)`, a factor `q^(1/2)` *worse* than the raw Schur bound.  The local
pair-codegree and fibre-degree facts are separately sharp in an abstract
multiplicative Latin-square model.  Any gain for the actual nodes must use a
new joint correlation between residual characters and the restricted
prime-power transforms, or genuine curvature/incidence information.

This is a method barrier, not an example showing that the actual tensor has
norm `>>sqrt(R)`.

---

## 1. The remaining tensor

Let

```text
q be an odd prime,             Y=q/2,
B=Y^A,                         3/2<A<2,
R=q^2/B=q^(h+o(1)),            h=2-A<1/2,
H=qR=q^3/B=q^(1+h+o(1)),
S_Y={n=p^j:Y exp(-w)<n<Y exp(w)},   0<w<(log 2)/3.  (1.1)
```

The project width `w=.2` satisfies the displayed restriction.  For arbitrary
real or complex weights define

```text
T_+(x,y,z)
 =sum_(a,b,c in S_Y) x_a y_b z_c
   1_(|8abc-q^3|<=C_w H).                          (1.2)
```

This is the hard-kernel model for the all-plus Fourier term `P^3`.  It is
negligible on either pure one-sided shell but is the unresolved term for a
balanced two-sided vector.

For a fixed pair `(a,b)`, the admissible interval for `c` has length
`O(H/q^2)=O(R/q)=o(1)`.  For fixed `c`, the integer product `ab` lies in an
interval of length `O(H/q)=O(R)`; every integer has `O_w(1)` ordered
representations by two shell prime powers.  Schur's test therefore gives

```text
|T_+(x,y,z)|<<_w sqrt(R)||x||_2||y||_2||z||_2.    (1.3)
```

The question is whether the special center `q/2` yields a fixed power below
`sqrt(R)`.

---

## 2. Modulo `q^3` makes the residual identity exact

Put

```text
I_H={r mod q^3:0<|r|<=C_wH and (r,q)=1}.            (2.1)
```

Because every node is less than `exp(w)q/2`, the restriction
`3w<log 2` gives

```text
0<8abc<2q^3.                                       (2.2)
```

Also `H=o(q^3)`.  Thus, after harmlessly enlarging the constant in the hard
window and taking `q` large,

```text
|8abc-q^3|<=C_wH
 iff 8abc mod q^3 belongs to I_H.                  (2.3)
```

There is no spurious lift at `0` or `2q^3`.  Moreover the residual is
automatically a unit: `q` divides neither `a`, `b`, nor `c`, so
`8abc-q^3` is nonzero modulo `q`.

Writing `G=(Z/q^3Z)^*`, `Phi=|G|`, and

```text
D(chi)=sum_(r in I_H)chi(r),
X(chi)=sum_(a in S_Y)x_a chi(a),                   (2.4)
```

with analogous definitions for `Y(chi),Z(chi)`, character orthogonality
gives the exact identity

```text
T_+(x,y,z)
 =Phi^-1 sum_(chi on G)
   conjugate(D(chi)) chi(8)X(chi)Y(chi)Z(chi).     (2.5)
```

Modulo `q^2` gives the same necessary congruence but loses the quotient of
`q^2`; (2.5) shows that moving to `q^3` repairs that loss completely.

---

## 3. The actual prime-power transforms have exact low moments

For `k=2,3`, a product of `k` nodes is less than `q^3`.  Hence

```text
a_1...a_k congruent b_1...b_k (mod q^3)
 iff a_1...a_k=b_1...b_k.                          (3.1)
```

A fixed integer has `O_(w,k)(1)` ordered representations as a product of
`k` shell prime powers.  Distinct prime bases can only be assigned to the
`k` slots in finitely many ways.  If a base repeats, all admissible
exponents lie in an interval of length `2w/log 2`, so the number of exponent
splittings is also `O_(w,k)(1)`.

Weighted convolution and character orthogonality consequently give

```text
sum_chi |X(chi)|^4 <<_w Phi ||x||_2^4,
sum_chi |X(chi)|^6 <<_w Phi ||x||_2^6,             (3.2)
```

and the same estimates for the other two coefficient vectors.  Thus this
barrier is not caused by discarding the actual prime-power product
structure: its strongest exact moments up through the three-fold product
are retained.

---

## 4. Parseval defeats both standard character closures

The residues in `I_H` are distinct modulo `q^3`, and `|I_H|asymp H`.
Parseval on `G` says

```text
sum_chi |D(chi)|^2=Phi |I_H|.                      (4.1)
```

The principal contribution is `|I_H|^2=o(Phi|I_H|)`.  It follows that

```text
max_(chi nonprincipal)|D(chi)|
 >=sqrt((Phi|I_H|-|I_H|^2)/(Phi-1))
 >>sqrt(H)=q^(1/2)sqrt(R).                         (4.2)
```

This lower bound is fatal to the direct maximum-character scheme.  Indeed,
using `(L^4,L^4,L^2)` in (3.2) gives

```text
Phi^-1 sum_chi |X(chi)Y(chi)Z(chi)|
 <<_w||x||_2||y||_2||z||_2,                       (4.3)
```

so inserting `max |D(chi)|` can never certify a constant below the right
side of (4.2).

The all-moment Hölder closure is no better.  Put each of the three actual
node transforms in `L^6` using (3.2), and put `D` in `L^2`.  Equation (4.1)
then gives exactly

```text
|T_+(x,y,z)|<<_w sqrt(H)||x||_2||y||_2||z||_2.    (4.4)
```

Among the exact product moments supplied by (3.1), this is the endpoint
allocation: `3/6+1/2=1`.  It loses `q^(1/2)` against (1.3).  Moments beyond
sixth order no longer follow from (3.1), because products of four or more
nodes can wrap modulo `q^3`; controlling them would itself be a new
arithmetic input.

For completeness, the principal character in (2.5) is harmless.  Since
`M=|S_Y|<=q^(1+o(1))`, its coefficient-uniform contribution is

```text
(H/Phi)M^(3/2)
 <=q^(h-1/2+o(1)),                                 (4.5)
```

which decays for `h<1/2`.  The obstruction is entirely nonprincipal.

---

## 5. The local incidence data alone are also insufficient

The proof of (1.3) uses only:

1. every ordered pair lies in `O(1)` edges;
2. every vertex lies in `O(R)` edges.

Those facts cannot imply `o(sqrt(R))`.  Let `G_0` be any finite abelian
group of order `d` and take the multiplicative Latin-square hypergraph

```text
E_0={(a,b,c) in G_0^3:abc=1}.                      (5.1)
```

Every pair determines one third vertex and every vertex has degree `d`.
For the three constant unit vectors, normalized in `ell^2(G_0)`, the
trilinear form equals

```text
d^2/d^(3/2)=sqrt(d).                               (5.2)
```

Taking `d` comparable with `R` saturates the Schur scale.  This model is not
embedded into the actual prime-power nodes; it proves only that the current
codegree/fibre package, even with an abstract multiplicative law, has no
room for a power saving.

---

## 6. Exact conclusion

At the active aperture `A=50/33`,

```text
h=16/33,
raw all-plus tensor exponent       h/2=8/33,
character Parseval exponent        (1+h)/2=49/66,
principal exponent                 h-1/2=-1/66.    (6.1)
```

Therefore:

```text
coefficient-uniform all-plus saving below sqrt(R): NOT PROVED;
exact q^3 character decomposition:                 PROVED;
max-character/Hölder character route improves it:  NO;
pair-codegree plus fibre-degree route improves it: NO IN ABSTRACT;
actual prime-power tensor lower bound sqrt(R):      NOT PROVED;
balanced full-shell QP consequence:                 OPEN.
```

A successful next input must control the **joint** sum in (2.5), showing
that characters with large short-interval coefficient `D(chi)` cannot also
carry three large restricted prime-power transforms, or must exploit the
curvature of `abc=q^3/8` beyond degree and codegree.  Separate Burgess,
Parseval, product-multiplicity, and Schur estimates cannot do this.

Executable exact checks:

```bash
python3 -m pytest -q src/test_qp_balanced_all_plus_character_barrier.py
```

The checker verifies the rational exponent ledger, the exact nonprincipal
Parseval floor, the `q^3` residual equivalence on finite shells, and the
Latin-square `sqrt(d)` saturation.
