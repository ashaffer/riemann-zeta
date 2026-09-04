# QP four-cycle: the mod-`q^3` multiplicative-character conductor audit

**Date:** 2026-08-22  
**Verdict:** the conductor filtration is useful, but it does not prove the
four-cycle bound or improve the existing `D^(21/16+o(1))` exponent.  The
principal character is negligible, the complete `q`-blocks cancel for every
nonprincipal conductor-`q` character and their possible endpoint block is
negligible, and the complete block of characters factoring through `q^2` has
Schatten-fourth mass `o(1)`.  The surviving primitive
conductor-`q^3` block requires a matrix-valued multiplicative restriction
estimate which is equivalent in strength to the original four-cycle problem.

Individual Pólya--Vinogradov or Burgess estimates do not supply that
restriction.  Character orthogonality and unique factorization give only a
primitive operator-norm bound of order `sqrt(qD)`; combined with the known
Hilbert--Schmidt bound, this is worse than the elementary `D^2` fourth-trace
bound.  Burgess is weaker still at the active length.  Thus this route alone
does not even recover the `D^(21/16)` result.

The first irreducible loss is precise: restriction of the primitive
`q^3` Fourier multiplier to the `q`-by-`q` multiplication table of the actual
prime-power shell.  Bounding scalar interval coefficients does not estimate
its zero-modulation box norm.

---

## 1. Exact character expansion

Let

```text
M=q^3,                 L=qD,
R={r:0<|r|<=L, q does not divide r}.                (1.1)
```

The fixed shell is narrow enough that `0<8abc<2q^3`.  Since every shell
node is a unit modulo `q`, the hard carry condition is exactly

```text
8abc (mod q^3) in R.                                (1.2)
```

For a character modulo `q^3`, put

```text
Rhat(chi)=sum_(r in R) conjugate(chi(r)),
Z_z(chi)=sum_(c in S) z_c chi(c),
u_chi(a)=chi(a).                                    (1.3)
```

Character orthogonality gives the exact matrix identity

```text
A_z
 =1/phi(q^3) sum_(chi mod q^3)
    Rhat(chi) Z_z(chi) chi(8) u_chi u_chi^T.        (1.4)
```

No approximation, completion, or tail occurs in (1.4).

The character counts by exact conductor are

```text
1:       1,
q:       q-2,
q^2:     (q-1)^2,
q^3:     q(q-1)^2.                                  (1.5)
```

Symmetry also kills every odd character, since `R=-R`.  This saves a
constant, not a power.

## 2. Conductors `1` and `q`

Write the integer endpoint as

```text
floor(L)=J*q+s,                 0<=s<q.             (2.1)
```

The `J` complete positive `q`-blocks and `J` complete negative `q`-blocks
cancel for every nonprincipal character induced modulo `q`.  If `s=0`, its
coefficient vanishes exactly.  In general only the two boundary intervals of
length `s` remain.  Recombining all characters modulo `q`, that boundary is
a matrix of the form

```text
q^-2 sum_c z_c beta(8abc mod q),        0<=beta<=2. (2.2)
```

There are `O(q^2)` cells and `O(q)` colors.  Cauchy--Schwarz therefore gives

```text
||A_(q,boundary)||_HS^2 <<q^-1||z||_2^2,
||A_(q,boundary)||_S4^4 <<q^-2||z||_2^4.            (2.3)
```

Thus the endpoint remainder is harmless.  The often convenient aligned
choice `L=q*floor(D)` makes it literally zero, but alignment is not needed.

The principal term is the constant rank-one matrix

```text
A_1(a,b)=|R|/phi(q^3) * sum_c z_c.                  (2.4)
```

Writing `N=#S<<q`, its only singular value is at most

```text
O(D*N^(3/2)/q^2) * ||z||_2.                         (2.5)
```

Consequently

```text
||A_1||_S4^4 <<D^4/q^2 ||z||_2^4
              =q^(-2/33+o(1))||z||_2^4.            (2.6)
```

Thus the first two conductor levels are harmless.

## 3. Recombine every character through `q^2`

It is better not to estimate conductor-`q^2` coefficients separately.
Let `A_<=2` be the sum in (1.4) over all characters factoring modulo
`q^2`.  Orthogonality at modulus `q^2` gives

```text
A_<=2(a,b)
 =1/q sum_c z_c rho_2(8abc),                        (3.1)

rho_2(x)=#{r in R:r==x (mod q^2)}.                 (3.2)
```

Because `2L<q^2`, the function `rho_2` is zero-one.  Define

```text
h_2(x)=sum_c z_c rho_2(xc).                         (3.3)
```

The products `ab`, with `a,b` in the actual shell, are below `q^2` and
are multiplicatively Sidon.  Hence each residue `ab mod q^2` has at most
two ordered shell representations, and

```text
||A_<=2||_HS^2
 <=2/q^2 sum_(x mod q^2)|h_2(x)|^2.                (3.4)
```

The energy on the right counts

```text
r*c' - r'*c = t*q^2,        |t|<<D.                (3.5)
```

For distinct actual colors `c,c'`, coprimality makes the solutions in
`(r,r')` one arithmetic progression with step `(c,c')`; the box
`|r|,|r'|<=L` contains `O(D)` points for each fixed `(c,c',t)`.  There are
`O(D)` possible `t`.  Cauchy--Schwarz gives

```text
sum_(c,c') |z_c z_c'| <=N||z||_2^2<<q||z||_2^2.   (3.6)
```

When `c=c'`, condition `2L<q^2` forces `t=0,r=r'`.  It follows that

```text
sum_x |h_2(x)|^2 <<qD^2 ||z||_2^2,                (3.7)

||A_<=2||_HS^2 <<D^2/q ||z||_2^2
                =q^(-1/33+o(1))||z||_2^2.         (3.8)
```

In particular,

```text
||A_<=2||_S4^4 <<D^4/q^2 ||z||_2^4=o(1)||z||_2^4. (3.9)
```

Since the principal and conductor-`q` blocks already satisfy (2.3) and
(2.6), the exact
conductor-`q^2` block

```text
A_2=A_<=2-A_<=1,          A_<=1=A_1+A_q,           (3.10)
```

is harmless as well.  This conclusion
uses the whole conductor block and elementary determinant spacing; no
individual character-sum theorem is needed.

## 4. The primitive restriction operator

Let `X_3*` denote the primitive characters of conductor `q^3` and put

```text
T_z=1/phi(q^3) sum_(chi in X_3*)
       Rhat(chi)Z_z(chi)chi(8)u_chi u_chi^T.        (4.1)
```

Then

```text
A_z=T_z+A_<=2.                                      (4.2)
```

A sufficient new theorem is the Schatten restriction estimate

```text
||T_z||_S4^4 <<D q^o(1)||z||_2^4.                  (4.3)
```

Indeed, (3.9), (4.2), and the triangle inequality in `S_4` would give the
same bound for the full hard core and hence for its nondegenerate part.

The exact nondegenerate form of the required restriction can also be
written explicitly.  For a character `eta`, let

```text
S(eta)=sum_(a in S)eta(a),
B(eta,nu)=S(eta)S(nu)-S(eta*nu).                    (4.4)
```

The subtraction in `B` removes equal row or column indices.  Put

```text
lambda_chi=Rhat(chi)Z_z(chi)chi(8).                 (4.5)
```

Then the primitive nondegenerate box form is exactly

```text
1/phi(q^3)^4 sum_(chi1,...,chi4 in X_3*)
 lambda_1 conjugate(lambda_2) lambda_3 conjugate(lambda_4)

 *B(chi1*conjugate(chi4), chi3*conjugate(chi2))
 *B(chi1*conjugate(chi2), chi3*conjugate(chi4)).    (4.6)
```

Bounding (4.6) by `D q^o(1)||z||_2^4`, together with compatible mixed
low-conductor terms, is the exact restriction problem.  Estimate (4.3) is
a clean sufficient version which handles those mixed terms automatically.

## 5. What character orthogonality actually gives

For arbitrary unit vectors `x,y` on the shell, define

```text
X(chi)=sum_a conjugate(x_a)chi(a),
Y(chi)=sum_b y_b chi(b).                            (5.1)
```

The actual prime-power shell has unique factorization of every product of
three shell nodes.  Character orthogonality therefore gives

```text
sum_chi |X(chi)|^6 <<phi(q^3)||x||_2^6,            (5.2)
```

and the same bound for `Y` and `Z_z`.  Parseval gives

```text
sum_chi |Rhat(chi)|^2=phi(q^3)|R|,
|R| asymp qD.                                       (5.3)
```

Hölder with exponents `(2,6,6,6)` in the bilinear form associated with
(4.1) yields only

```text
||T_z||_(2->2) <<sqrt(qD)||z||_2.                  (5.4)
```

The known pair-uniqueness/color-degree bound and (3.8) give

```text
||T_z||_HS^2 <<D q^o(1)||z||_2^2.                 (5.5)
```

Combining (5.4)--(5.5) produces `qD^2`, worse than the elementary
Hilbert--Schmidt fourth bound

```text
||T_z||_S4^4 <=||T_z||_HS^4
              <<D^2 q^o(1)||z||_2^4.              (5.6)
```

Thus plain character orthogonality stops at `D^2`.

## 6. Individual conductor bounds do not repair the loss

For conductor `q^2`, Pólya--Vinogradov gives at best `q log q`, but the
block estimate (3.9) is already much stronger than anything obtained by
inserting that pointwise bound into (1.4).

For a primitive character modulo `q^3`, Burgess with `r=2` gives

```text
|Rhat(chi)|
 <<L^(1/2)*(q^3)^(3/16+o(1))
 =sqrt(L)*q^(9/16+o(1)).                            (6.1)
```

At `D=q^(16/33)` the exponent in `q` is

```text
689/528 =1.3049... ,                               (6.2)
```

whereas the normalized `L^2` size used in (5.3) is only

```text
sqrt(L)=q^(49/66)=q^(0.7424...).                   (6.3)
```

Consequently Burgess is worse than the moment input already used in (5.4).
Pólya--Vinogradov is larger still.  Even hypothetical pointwise
square-root cancellation for every primitive coefficient would merely
match (5.3); it would not provide the matrix restriction saving in (4.3).

The issue is not the scalar length of `R`.  It is the correlation of the
four primitive characters after restriction to the shell multiplication
table, precisely the two `B` factors in (4.6).

## 7. Exponent verdict

At the project scale,

```text
target D:                         q^(16/33),
existing D^(21/16):               q^(21/33)=q^(7/11),
character/HS endpoint D^2:        q^(32/33),
principal and <=q^2 fourth mass:  q^(-2/33).        (7.1)
```

Therefore the conductor attack cleanly removes every imprimitive mode but
does not improve the global exponent.  Its binary ledger is

```text
mod-q^3 character expansion:                       EXACT;
principal block:                                   HARMLESS;
nonprincipal conductor-q complete blocks:          ZERO;
conductor-q endpoint block:                        S4^4<<q^-2;
all conductors through q^2:                        S4^4=o(1), PROVED;
primitive conductor-q^3 scalar Burgess bound:      INSUFFICIENT;
primitive matrix restriction (4.3)/(4.6):          OPEN;
new four-cycle exponent from this method:           NONE;
four-cycle bound:                                   NOT PROVED.
```

Executable conductor counts and exponent arithmetic are in

```text
src/qp_q3_character_conductor_audit.py
src/test_qp_q3_character_conductor_audit.py
```
