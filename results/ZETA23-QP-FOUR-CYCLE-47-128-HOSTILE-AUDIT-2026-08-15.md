# QP four-cycle `47/128` theorem: hostile audit

**Date:** 2026-08-15  
**Audited artifact:** `ZETA23-QP-FOUR-CYCLE-SHORT-RELATION-AVERAGING-AND-47-128-OPERATOR-THEOREM-2026-08-15.md`  
**Binary verdict:** **PASS**, conditional only on the earlier fixed-`(C,E)`
multiplicity and plane-conic inputs that the artifact explicitly lists.

The audit found no missing power, false fibre multiplicity, or normalization
error.  In particular, the theorem proves only

```text
Q_nd(z) << D^(47/32+o(1)) ||z||_2^4,
||A_z||_op << D^(47/128+o(1)) ||z||_2,
transverse exponent = 179/264.
```

It does not prove the full `D^(1+o(1))` four-cycle estimate.

---

## 1. Fixed invertible relation

Write the signed relation as

```text
e11*x-e12*y=e21*z-e22*w=H.
```

On one `H` fibre, the primitive directions are

```text
p=(e12/g1,e11/g1),  q=(e22/g2,e21/g2),
g1=gcd(e11,e12),     g2=gcd(e21,e22).
```

Thus

```text
k(s,t)=det((x,y),(z,w))=cst+as+bt+d,
c=det(p,q)=-det(e)/(g1*g2),
(cs+b)(ct+a)=ck+(ab-cd).
```

Here `c` is a nonzero integer.  The first completed factor is, up to the
nonzero scalar `g2`, `e21*x-e22*y`; the second is the analogous transverse
linear form.  A zero factor would give a rational equality between two
coprime, distinct shell prime powers.  After primitive reduction its
coefficients would have size at least the shell minimum, contradicting
`||e||_infinity<min(S)`.

Different `H` fibres partition both ordered-pair index sets, so their
incidence matrices are orthogonal blocks.  In each block the determinant
condition `|k|<<D` is a product band of width
`L<<|det(e)|D/(g1*g2)`.  The product-band Schur estimate therefore gives

```text
S_e(z) << sqrt(D)*sqrt(|det(e)|/(g1*g2))*q^o ||z||_2^4.
```

This part passes, including negative coefficients and nonprimitive rows.

## 2. Rank-one relation

After removing the harmless common scalar, write `e=r s^T`, with both
integer vectors primitive.  The relation implies, for one integer `h`,

```text
s1*x-s2*y=r2*h,       s1*z-s2*w=r1*h.
```

Choosing `s1*u0-s2*v0=1` gives

```text
(x,y)=r2*h*(u0,v0)+p*(s2,s1),
(z,w)=r1*h*(u0,v0)+q*(s2,s1),
det C=h*ell,           ell=r2*q-r1*p.
```

The matching point that was most important to check is valid.  For fixed
`(h,ell)`, the equation `r2*q-r1*p=ell` determines at most one `q` from
each `p` and at most one `p` from each `q`.  The same completion set is also
a matching under the two cross-pair projections, since `s1,s2,r1,r2` are
nonzero.  Hence both Cauchy bounds in the proof are genuine matching bounds,
not an illicit complete-bipartite estimate:

```text
T_(h,ell)<=sqrt(P_h Q_h),
T_(h,ell)<=sqrt(R_ell S_ell).
```

Their geometric mean and the `N=0` product-band norm yield
`S_e(z)<<sqrt(D)q^o||z||_2^4`.  If a component of `r` or `s` is zero, the
same coprimality/height argument makes the all-distinct color set empty.
This part passes.

## 3. Product-band lemma

For `|N|>2L`, on a dyadic block `|u|asymp U`, `|v|asymp V`, nonemptiness
forces `UVasymp|N|`.  The maximum degrees are

```text
1+L/U,    1+L/V,
```

whose Schur geometric mean is `O(sqrt(L))`.  For `|N|<=2L`, nonemptiness
forces `UV<<L`, and the trivial rectangular norm is `O(sqrt(UV))`.  Signs,
arithmetic-progression restrictions, and deletion of entries do not alter
the bound.  Dyadic summation costs only `q^o(1)`.  This part passes.

## 4. Relation count and successive minima

The short branch is a legitimate positive union bound.  A color with
`lambda1<R0` supplies a nonzero integer relation with sup norm below `R0`;
there are `O(R0^4)` such vectors.  Since
`sqrt(|det e|)<<R0`, the fixed-relation theorem gives

```text
sum_(short C) w_z(C) << R0^5 sqrt(D) q^o ||z||_2^4.
```

Multiplication by the already proved `m(C)<<sqrt(D)q^o` is therefore valid.
Multiple relations killing one color only overcount a positive sum.

For the long branch, assume `lambda1>=R0`.  If
`lambda1*lambda2>=R0*D`, expansion of
`product_i(1+D/lambda_i)` gives:

```text
linear terms    <= D/R0,
quadratic terms <= D/R0,
cubic term       asymp D^3/q = D/(q/D^2) << D/R0.
```

If `lambda1*lambda2<R0*D`, Minkowski gives
`lambda3 >> q/(R0D)`.  Choosing the fixed constant in
`R0=c0*q/D^2` small makes this exceed the entire realized difference box.
All differences then lie in one rational two-plane.  A reduced basis has
shortest length at least `R0`, so its two coordinates have size
`O(D/R0)`; the previously proved plane-conic theorem gives
`m(C)<<sqrt(D/R0)q^o`.  Both minima branches pass.

## 5. Exact exponent and transfer ledger

In powers of `D`,

```text
R0=q/D^2=D^(1/16),
Q_short <= D*R0^5       = D^(21/16),
Q_long  <= D^(3/2)/sqrt(R0) = D^(47/32).
```

The long branch dominates.  Taking a fourth root gives `47/128`.  The
existing carry-to-transverse transfer then gives

```text
1/2+(47/128)*(16/33)=179/264,
```

one `1/264` below `45/66=180/264`.  The arithmetic and normalization pass.

Exact replay tests are in
`src/test_qp_four_cycle_short_relation_hostile_audit.py`; together with the
underlying factorization and corrected large-value LP tests, all pass.

```text
fixed-relation theorem:          PASS;
rank-one matching step:          PASS;
O(R0^4) relation count:          PASS;
successive-minima split:         PASS;
47/128 operator exponent:        PASS;
179/264 transfer exponent:       PASS;
full four-cycle theorem:         NOT CLAIMED.
```
