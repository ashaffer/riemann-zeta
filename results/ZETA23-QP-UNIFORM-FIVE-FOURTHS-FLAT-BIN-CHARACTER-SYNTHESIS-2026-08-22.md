# QP four-cycle: uniform five-fourths theorem from character-flat bins

**Date:** 2026-08-22  
**Verdict:** the multiplicative-character estimate for a flat color support
extends, without any change in its proof, from `M<=D` to every support size
in the project shell.  Combining it on coefficient-height bins with the
proved parabolic `D^(5/4)` theorem, the broad fixed-color
`D^(5/16)` theorem, and the diffuse participation estimate gives the
uniform bound

```text
||A_z||_(S_4)^4 << D^(5/4) q^o(1) ||z||_2^4.       (0.1)
```

The exact fourth-trace expansion and the already bounded repeated-row and
repeated-column terms then also give the uniform four-cycle estimate

```text
|Q_nd(z)| << D^(5/4) q^o(1) ||z||_2^4.             (0.1a)
```

Equivalently, the QP carry operator has norm

```text
||A_z||_op << D^(5/16) q^o(1) ||z||_2.             (0.2)
```

Under the already established smooth band transfer, this gives transverse
exponent

```text
1/2+(5/16)*(16/33)=43/66.                           (0.3)
```

This is a uniform improvement on `D^(21/16)` (operator exponent `21/64`),
not the literal four-cycle bound `D^(1+o(1))`.

## 1. Flat determinant-band estimate for every `M`

Let `A` be any set of `M` actual prime-power colors in the fixed narrow
project shell.  Put

```text
N_D(A)=#{(a,b,c,d) in A^4:0<|a*d-b*c|<=C*D*q^o(1)}.
```

The character proof in
`ZETA23-QP-DETERMINANT-BAND-FLAT-PRIME-OBSTRUCTION-AND-LOCAL-SQRT-THEOREM-2026-08-22.md`
actually proves, uniformly for every `M`,

```text
N_D(A)/M^2
 <<q^o(1)[M*D/q+M^(1/4)*D^(1/2)].                  (1.1)
```

Here is the quantifier audit.  Fix `a in A`.  The shell has ratio strictly
less than two, so distinct shell prime powers have distinct prime bases.
Consequently every member of `A\{a}` is a unit modulo the prime power `a`,
and the members have distinct residues modulo `a`.

For fixed `(a,b,c)`, the determinant interval has length less than one as
an interval for `d`.  Dropping `d in A`, character orthogonality on the
unit group modulo `a` leaves the principal term

```text
O(M^2*D/q)                                             (1.2)
```

and the nonprincipal expression

```text
1/phi(a) sum_chi |B_a(chi)|^2 |H_a(chi)|.             (1.3)
```

The short interval in `H_a` is restricted to units; omitting that
restriction only enlarges its fourth energy.  Holder with exponents
`2,4,4` gives

```text
(1.3)<=M^(1/2)*E_a(A)^(1/4)*E_a(I_D)^(1/4).           (1.4)
```

Three-variable determination gives `E_a(A)<=M^3`, for every `M`.  Also
`D^2*q^o(1)<a`, so the short-interval product congruence is an integer
equality and the divisor bound gives `E_a(I_D)<<D^(2+o(1))`.  Thus (1.4)
is at most

```text
M^(5/4)*D^(1/2)*q^o(1).                              (1.5)
```

Summing (1.2), (1.5) over the `M` choices of `a` and dividing by the flat
normalization `M^2` proves (1.1).  No step uses `M<=D`.  The argument uses
the full character group of the units and is valid for prime-power, not
only prime, moduli.

## 2. Transfer from flat supports to a height bin

Let `z_B` be supported on `A`, with `|A|=M`, and suppose

```text
t<|z_c|<=2t                 (c in A),
s=||z_B||_2.                                         (2.1)
```

Writing `w_z(C)=|z_a z_b z_c z_d|`, (1.1) gives

```text
sum_(0<|det C|<<D q^o) w_z(C)
 <<s^4 q^o(1)[M*D/q+M^(1/4)*D^(1/2)].              (2.2)
```

Indeed the left side is at most `(2t)^4 N_D(A)`, while
`M^2*t^4<=s^4`.  Thus arbitrary complex phases and a factor-two variation
inside a bin do not affect the flat character theorem.

If

```text
M<=D^(7/4),                                           (2.3)
```

then, using `q=D^(33/16+o(1))`,

```text
M*D/q<=D^(11/16+o(1)),
M^(1/4)*D^(1/2)<=D^(15/16),                         (2.4)
```

so the determinant-band mass in (2.2) is

```text
<<D^(15/16+o(1))*s^4.                               (2.5)
```

## 3. Every small bin has fourth trace `D^(5/4)`

The all-distinct retained cycles have the proved exhaustive slice
decomposition:

* every nonzero degenerate restriction belongs to the parabolic/tangent
  sector, whose complete contribution is

  ```text
  Q_par(z_B)<<D^(5/4+o(1))*s^4;                     (3.1)
  ```

* every nondegenerate or identically-zero restriction has fixed-color
  multiplicity

  ```text
  m(C)<<D^(5/16+o(1)).                              (3.2)
  ```

Consequently (2.5), (3.2) give

```text
|Q_broad(z_B)|
 <=D^(5/16+o(1))*sum_C w_z(C)
 <<D^(5/4+o(1))*s^4.                                (3.3)
```

Repeated-node, permutation, square-edge, and opposite-color-equality
sectors are already `O(D q^o(1)s^4)`.  Therefore every bin satisfying
(2.3) obeys

```text
||A_(z_B)||_(S_4)^4<<D^(5/4+o(1))*s^4.             (3.4)
```

The pointwise cap (3.2) is used only on its proper broad sector; (3.1)
covers its whole complement.

## 4. Every large bin has the same fourth-trace bound

For a factor-two bin, its normalized fourth-moment participation satisfies

```text
M_4(z_B)=s^4/sum_c |z_c|^4 >>M.                    (4.1)
```

The proved diffuse estimate, homogenized to mass `s`, is

```text
|Q_nd(z_B)|
 <<q^o(1)[D*s^4+D^3*sum_c|z_c|^4]
 <<q^o(1)[D+D^3/M]*s^4.                            (4.2)
```

Thus, if

```text
M>=D^(7/4),                                           (4.3)
```

the right side of (4.2) is at most `D^(5/4+o(1))s^4`.
Adding the already closed repeated sectors proves (3.4) for every large
bin as well.  At the crossover, the two active exponents are exactly

```text
5/16+(1/2+(7/4)/4)=5/4,
3-7/4=5/4.                                          (4.4)
```

## 5. Schatten recombination and the tiny tail

Normalize `||z||_2=1`.  The shell contains at most `q^O(1)` colors.  Put
all coefficients with `|z_c|<=q^(-100)` into `z_tail`, and partition the
rest into factor-two height bins.  There are `O(log q)` bins and

```text
sum_B ||z_B||_2<=O(sqrt(log q)).                    (5.1)
```

The carry matrix is linear in the color coefficients:

```text
A_z=sum_B A_(z_B)+A_(z_tail).                       (5.2)
```

Taking fourth roots in the bin theorem and applying the triangle inequality
in `S_4` gives

```text
||sum_B A_(z_B)||_(S_4)
 <<D^(5/16)q^o(1) sum_B||z_B||_2
 <<D^(5/16)q^o(1).                                 (5.3)
```

The exact pair-uniqueness Hilbert--Schmidt estimate gives

```text
||A_(z_tail)||_(S_4)
 <=||A_(z_tail)||_(HS)
 <<D^(1/2)||z_tail||_2=o(1).                       (5.4)
```

Thus (5.2)--(5.4), followed by the fourth power, prove (0.1).  This
recombination includes every mixed-height cycle automatically; no
coordinatewise expansion of cross-bin terms is needed.

Finally, the exact rectangle expansion writes `Q_nd(z)` as the fourth trace
minus the repeated-row/repeated-column contribution, whose absolute value
is `O(D q^o(1)||z||_2^4)`.  Equation (0.1) therefore implies (0.1a).

## 6. Audit ledger

```text
character flat-bin theorem for all M:              PROVED;
prime-power modulus and nonunit short residues:     INCLUDED;
D/q principal term below threshold:                PROVED;
small-bin broad/parabolic exhaustion:              PROVED BY EXISTING DICHOTOMY;
large-bin participation estimate:                  PROVED;
arbitrary complex phases in one bin:               HARMLESS BY ABSOLUTE VALUES;
mixed height bins:                                 CLOSED BY S_4 TRIANGLE;
arbitrarily small coefficient tail:                CLOSED BY HS;
uniform fourth trace D^(5/4+o):                    PROVED;
uniform four-cycle form D^(5/4+o):                 PROVED;
uniform operator exponent 5/16:                    PROVED;
literal four-cycle exponent 1:                     NOT PROVED.
```
