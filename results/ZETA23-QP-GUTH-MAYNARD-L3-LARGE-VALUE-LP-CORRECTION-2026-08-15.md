# QP Guth--Maynard `L3` large-value LP correction

**Date:** 2026-08-15  
**Verdict:** Guth--Maynard's large-value theorem, combined with the
classical Montgomery--Halász--Huxley estimate and `L2` Markov, does **not**
prove the critical arbitrary-coefficient `L3` estimate on supports
`M>=q^(8/11)`.  The proposed `8/11` conclusion discarded the nonnegative
remainder terms in two sum bounds.  With those terms retained, this package
closes no support range beyond the elementary one-block range
`M<=q^(8/33)`.

This corrects only that proposed application.  It does not contradict the
Guth--Maynard theorem.

---

## 1. Inputs and normalization

Write

```text
T=B=q^A,        A=50/33,
D=q^h,          h=2-A=16/33,
M=q^m,          V=q^v,       0<=v<=m/2.             (1.1)
```

On a normalized dyadic coefficient block, `||x||_2=1` and
`|x_n|<<M^(-1/2)`.  Set

```text
b_n=sqrt(M) x_n,             |b_n|<<1,
W=V sqrt(M).                                         (1.2)
```

Let `R(V)` be the number of one-separated ordinates in an interval of
length `T` at which the normalized polynomial has magnitude at least `V`.
Theorem 1.1 of Guth--Maynard,
[*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
gives

```text
R <<T^o(1) [q^2/W^2+q^(18/5)/W^4+T q^(12/5)/W^4]. (1.3)
```

The classical comparison bound printed as equation (1.1) in that paper is

```text
R <<T^o(1) [q^2/W^2
             +T min(q/W^2,q^4/W^6)].               (1.4)
```

The normalized `L2` bound gives

```text
R/T <<q^o(1) V^(-2).                               (1.5)
```

The shell is covered by `O(1)` ordinary Dirichlet-polynomial ranges.  The
usual local Sobolev sampling changes the continuous level-set measure into
`R(V)/T` at only a `q^o(1)` cost.

---

## 2. The exact exponent LP

After dividing by `T`, define the affine exponents

```text
l = -2v,                                           (2.1)
a = h-m-2v,                                        (2.2)
b = min(1-m-2v, 4-3m-6v),                         (2.3)
g = 12/5-2m-4v.                                   (2.4)
```

The `q^(18/5)/W^4` term in (1.3), after division by `T`, has constant part
`18/5-A=344/165<12/5`; hence (2.4) is the larger Guth--Maynard remainder
throughout the range.

Crucially, (1.3) and (1.4) are **sum bounds**.  Their exponent forms are
`max(a,g)` and `max(a,b)`, not `min(a,g)` and `min(a,b)`.  Combining the
three independent bounds gives

```text
r(v,m)=min(l, max(a,b), max(a,g))
      =min(l, max(a,min(b,g))).                    (2.5)
```

Layer cake contributes `V^3 R(V)/T` on a logarithmic level, so the correct
third-moment exponent is

```text
F(v,m)=3v+r(v,m).                                  (2.6)
```

The desired estimate requires

```text
sup_(0<=v<=m/2) F(v,m) <= h/4=4/33.                (2.7)
```

---

## 3. Exact failure at the proposed threshold

Take

```text
m=8/11,            v=m/2=4/11.                    (3.1)
```

Then

```text
a=-32/33,
b=-5/11,
g=-28/55,
l=-8/11.                                           (3.2)
```

Therefore (2.5) gives `r=-8/11`, and

```text
F=3*(4/11)-8/11=4/11.                             (3.3)
```

This is three times larger in the exponent than the target `4/33`.  The
incorrect value

```text
h-m/2=4/33                                         (3.4)
```

comes from using only the common first summand `q^2/W^2`, whose exponent is
`a`, while deleting the larger remainder summands.  An upper bound
`R<=A+B` does not imply `R<=A`.

---

## 4. No second support range follows from these inputs

The failure is not confined to the endpoint `8/11`.

If

```text
h/2 < m <=4/5,                                     (4.1)
```

take `v=m/2`.  At this point both large-value sum bounds are no stronger
than `L2`, so `r=-m` and

```text
F=m/2>h/4.                                         (4.2)
```

If

```text
4/5<=m<=1,                                         (4.3)
```

take `v=1/5`.  Direct substitution in (2.1)--(2.4) gives `r=-2/5`, hence

```text
F=1/5>4/33.                                        (4.4)
```

Thus this collection of upper bounds cannot establish (2.7) for any
`m>h/2=8/33`.  For `m<=8/33`, the elementary estimate

```text
average |X|^3 <=||X||_infinity average |X|^2
               <<sqrt(M)                          (4.5)
```

already gives exponent `m/2<=4/33`.  Guth--Maynard adds no new certified
support interval for this particular target.

```text
one-block range m<=8/33:                            PROVED;
claimed second range m>=8/11 from GM:               RETRACTED;
correct GM/classical/L2 layer LP:                   (2.5)--(2.6);
new support range from these inputs:                NONE;
global arbitrary-coefficient L3 target:             OPEN;
four-cycle / QP / strip:                            NOT PROVED.
```
