# QP four-cycle: uniform `307/256` trace theorem from Burgess

**Date:** 2026-08-23  
**Verdict:** replacing the nonprincipal fourth-moment estimate in the
determinant-band character argument by the classical `r=2` Burgess bound
gives the uniform theorem

```text
||A_z||_(S_4)^4, |Q_nd(z)|
  <<D^(307/256) q^o(1) ||z||_2^4.                 (0.1)
```

Consequently

```text
||A_z||_op <<D^(307/1024) q^o(1)||z||_2.          (0.2)
```

This improves the previous trace exponent `5/4=320/256` by `13/256`.
It is **not** the sharp trace exponent `1`; the remaining gap is `51/256`.

The key point is that the parabolic `5/4` endpoint is a singleton-line
term, not the curvature term.  The occupied-line theorem bounds its
pointwise multiplier by `D^(5/16)`, so the same Burgess determinant mass
that improves the broad sector also improves this parabolic endpoint.  The
parabolic curvature term was already `D^(37/32)=D^(296/256)`.

---

## 1. Burgess determinant-band mass

Let `A` be a set of `M` actual prime-power colors in the fixed project
shell.  Put

```text
N_D(A)=#{(a,b,c,d) in A^4:0<|a*d-b*c|<<D q^o(1)}. (1.1)
```

Fix `a in A`.  Distinct shell prime powers have distinct prime bases, so
every element of `A\{a}` is a unit modulo the prime power `a`, and these
elements occupy distinct residues modulo `a`.  Once `(a,b,c)` is fixed,
the determinant window has length `O(D/a)<1` in `d`.  Dropping `d in A`
and using character orthogonality on `(Z/aZ)^*` gives the principal term

```text
O(M^2*D/q)                                           (1.2)
```

and the nonprincipal remainder

```text
1/phi(a) sum_(chi != chi_0) |B_a(chi)|^2 |H_a(chi)|,

B_a(chi)=sum_(b in A\{a}) chi(b),
H_a(chi)=sum_(0<|h|<<D) chi(h).                    (1.3)
```

The `r=2` Burgess estimate gives, uniformly in every nonprincipal
character,

```text
|H_a(chi)|
 <<D^(1/2) a^(3/16) q^o(1)
 <<D^(1/2) q^(3/16) q^o(1).                       (1.4)
```

The two signs in `H_a` cost only a constant.  Restricting the short
interval to units is automatic because Dirichlet characters vanish on
nonunits.

The prime-power modulus causes no loss.  If `a=p^j` and `chi` is
imprimitive, its primitive inducer has conductor `p^s<=p^j`; the two
characters agree on units and vanish on multiples of `p`.  Apply Burgess
at conductor `p^s` and enlarge it to `a`.  The `r=2` form has no cube-free
hypothesis.  This is also covered directly by Burgess's prime-power
analysis.

Parseval and residue injectivity give

```text
1/phi(a) sum_chi |B_a(chi)|^2=M+O(1).             (1.5)
```

Thus (1.3) is at most

```text
M*D^(1/2)*q^(3/16+o(1)).                          (1.6)
```

Sum over `a`, divide by the flat quartic normalization `M^2`, and use
`q=D^(33/16+o(1))`.  This proves

```text
N_D(A)/M^2
 <<q^o(1)[M*D/q+D^(1/2)q^(3/16)]
 =q^o(1)[M*D/q+D^(227/256)].                      (1.7)
```

For a factor-two coefficient-height bin `z_B`, with support `M` and
`s=||z_B||_2`, the same comparison by absolute values gives

```text
sum_(0<|det C|<<D q^o) w_(z_B)(C)
 <<[M*D/q+D^(227/256)]q^o(1)*s^4.                 (1.8)
```

The classical input is the Burgess character-sum estimate

```text
sum_(x<n<=x+N) chi(n)
 <<N^(1-1/r) conductor(chi)^((r+1)/(4r^2)+o(1)).  (1.9)
```

At `r=2`, (1.9) is exactly (1.4).  See Burgess,
[*Estimation of Character Sums Modulo a Power of a Prime*](https://doi.org/10.1112/plms/s3-52.2.215),
and the prime-modulus formulation in Kerr--Shparlinski--Yau,
[*A refinement of the Burgess bound for character sums*](https://arxiv.org/abs/1711.10582).

## 2. Small support bins

Put

```text
M<=D^(461/256).                                    (2.1)
```

The principal term in (1.8), after multiplication by the broad completion
cap `D^(5/16)`, has exponent

```text
461/256+1-33/16+5/16=269/256.                     (2.2)
```

The nonprincipal term has exponent

```text
227/256+5/16=307/256.                             (2.3)
```

### Broad slices

Every nondegenerate or identically-zero broad color satisfies

```text
m(C)<<D^(5/16)q^o(1).                             (2.4)
```

Equations (1.8), (2.2), and (2.3) therefore give

```text
Q_broad(z_B)<<D^(307/256+o(1))*s^4.               (2.5)
```

### Parabolic slices

The occupied-line theorem gives, color by color,

```text
m_par(C)
 <<K_C+sqrt(D*K_C/h(C)),
K_C<<D^(5/16)q^o(1).                              (2.6)
```

The first term in (2.6) is the singleton or first-occupied-point term.  It
is positive and bounded by `D^(5/16)` times the full determinant-band mass
in (1.8), so it obeys (2.3).  The second term is the curvature contribution;
the determinant-content/gap-token theorem already proves, uniformly in the
coefficients,

```text
Q_(par,curv)(z_B)<<D^(37/32+o(1))*s^4
                         =D^(296/256+o(1))*s^4.   (2.7)
```

Consequently

```text
Q_par(z_B)<<D^(307/256+o(1))*s^4.                 (2.8)
```

This is the bridge that a generic pointwise parabolic cap would miss:
using only `m(C)<<D^(1/2)` in (1.8) would be weaker than the old theorem.
The split (2.6) is essential.

Repeated-node, permutation, opposite-color, and square-edge sectors remain
`O(Dq^o(1)s^4)`.  Thus every bin satisfying (2.1) has fourth trace at most
`D^(307/256+o(1))s^4`.

## 3. Large support bins

For a factor-two bin, the proved diffuse participation theorem gives

```text
|Q_nd(z_B)|
 <<[D+D^3/M]q^o(1)*s^4.                           (3.1)
```

If

```text
M>=D^(461/256),                                    (3.2)
```

then

```text
3-461/256=307/256.                                (3.3)
```

Hence (3.1), together with the closed repeated sectors, proves the same
`307/256` fourth-trace estimate for every large bin.  The small- and
large-support arguments overlap exactly at (2.1)--(3.2).

## 4. Recombination

After discarding a negligible `q^-100` coefficient tail by the established
Hilbert--Schmidt estimate, decompose `z` into `O(log q)` factor-two height
bins.  The carry matrix is linear:

```text
A_z=sum_B A_(z_B)+A_tail.                          (4.1)
```

Take fourth roots of the bin estimates and use the Schatten-`4` triangle
inequality.  Since

```text
sum_B ||z_B||_2<<sqrt(log q)||z||_2,               (4.2)
```

the logarithmic factor is `q^o(1)`.  This proves (0.1) for the complete
fourth trace.  The exact rectangle expansion and the already bounded
repeated-row/column contribution then give the same exponent for
`Q_nd(z)`.

The operator and transverse exponents are

```text
operator:    (307/256)/4=307/1024,
transverse:  1/2+4*(307/256)/33=1363/2112.        (4.3)
```

## 5. Audit ledger

```text
Burgess r=2 short detector D^(227/256):             PROVED;
prime-power and imprimitive characters:             INCLUDED;
flat-bin determinant mass (1.8):                    PROVED;
broad singleton synthesis:                         PROVED;
parabolic singleton K_C<=D^(5/16):                 PROVED BY OCCUPIED-LINE THEOREM;
parabolic curvature D^(37/32):                     PREVIOUSLY PROVED;
diffuse crossover M=D^(461/256):                   EXACT;
Schatten height-bin recombination:                  PROVED;
uniform trace exponent 307/256:                    PROVED;
uniform operator exponent 307/1024:                PROVED;
sharp trace exponent 1:                            NOT PROVED.
```

The exact exponent replay is
`src/qp_burgess_307_256_synthesis.py`, with tests in
`src/test_qp_burgess_307_256_synthesis.py`.
