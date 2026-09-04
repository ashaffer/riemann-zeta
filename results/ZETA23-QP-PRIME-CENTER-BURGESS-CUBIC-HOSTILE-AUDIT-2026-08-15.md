# Prime-center Burgess cubic theorem: independent hostile audit

**Date:** 2026-08-15  
**Binary verdict:** **PASS** for the all-prime, one-sided, prime-half-center
theorem and its exponent `755/1056`.  This is a theorem only for the
coordinate-projected one-sided game at centers `Y=q/2`, with `q` an odd
prime and fixed `w<log 2`.  It does not lower the exponent for a balanced
full shell.

There is one minor presentation gap in the authoring proof: the hard
incidence estimate is valid only while the residual window is `o(q)`, so
the far Schwartz tail cannot literally be handled by applying that estimate
at every dyadic scale.  Section 5 below supplies the missing truncation and
shows that the tail is negligible.  No exponent changes.

The density-one refinement is not needed for the main verdict.  Its phrase
about enlarging a character interval before taking absolute values is not
valid if read as a comparison of two character sums.  The claim is repaired
without a maximal theorem: on each modulus block, enlarge the **positive
incidence set** `E_R` to `E_D` for one deterministic `D>=sup R(q)`, then run
the large sieve on that fixed interval.  Section 7 records the check.

---

## 1. Restricted incidence estimate

Let `q` be an odd prime, `Y=q/2`, `3/2<A<2`, `B=Y^A`, and

```text
R=Y^2/B=q^(2-A+o(1)).
```

Let the three node sets be subsets of one fixed side of the shell.  The
upper side is contained in `(q/2,q)` because `w<log 2`; the lower side is
also contained in `(0,q)`.  Thus distinct integer nodes give distinct
nonzero residues modulo `q`.

For

```text
E(A0,B0,C0)
 =#{(a,b,c) in A0 x B0 x C0: |2ab-qc|<=C R},
```

multiplicative-character orthogonality, after dropping the condition on
`c`, gives

```text
E <= C_w {(R/q)|A0||B0|+S_R sqrt(|A0||B0|)},       (1.1)
```

where `S_R` is the maximum nonprincipal character sum on the union of the
two residual intervals.  The principal term in (1.1) is essential and has
not been discarded.

Assume `|A0|<=|B0|`.  Two independent elementary bounds are

```text
E <= C_w R|C0|,                                    (1.2)
E <= C_w |A0||C0|.                                 (1.3)
```

For (1.2), fixing `c` leaves `O(R)` possible product integers `ab`.
Each has `O_w(1)` ordered representations by two shell prime powers.  If
the product has two prime bases, the factors are forced up to order; if it
is a power of one prime, the fixed logarithmic shell permits only `O_w(1)`
exponent splits.  For (1.3), fixing `(a,c)` confines `b` to an interval of
length `O(R/q)=o(1)`.

Put

```text
P=(R/q)|A0||B0|,  N=S_R sqrt(|A0||B0|),
F=R|C0|,          D=|A0||C0|.
```

The scalar inequality

```text
min(P+N,F,D) <= min(P,F)+min(N,D)                  (1.4)
```

is valid in all four order cases.  Geometric interpolation then gives

```text
min(P,F)/sqrt(|A0||B0||C0|) <= R/sqrt(q),          (1.5)

min(N,D)/sqrt(|A0||B0||C0|)
 <=sqrt(S_R)(|A0|/|B0|)^(1/4) <=sqrt(S_R).         (1.6)
```

Consequently

```text
E(A0,B0,C0)
 <=C_w (R/sqrt(q)+sqrt(S_R))
       sqrt(|A0||B0||C0|).                         (1.7)
```

This verifies the potentially dangerous principal-character interpolation.

## 2. Arbitrary coefficients

For nonnegative coordinate magnitudes, layer cake converts (1.7) into

```text
|T_R(x,y,z)| <=C_w K_R L(x)L(y)L(z),
K_R=R/sqrt(q)+sqrt(S_R),                           (2.1)
L(x)=int_0^infinity sqrt(#{i:|x_i|>s}) ds.
```

If a vector has at most `M` coordinates, decreasing rearrangement and
Cauchy--Schwarz give the finite-dimensional endpoint inequality

```text
L(x)<=C sqrt(log(2M))||x||_2.                      (2.2)
```

Equivalently, one may use rank blocks of sizes `1,2,4,...`; this avoids any
assumption on the smallest nonzero coefficient.  Since `M<=q`,

```text
|T_R(x,y,z)|
 <=C_w (log q)^(3/2)(R/sqrt(q)+sqrt(S_R))
          ||x||_2||y||_2||z||_2.                  (2.3)
```

Thus the restricted-to-strong step is valid for arbitrary signed or complex
coefficients.  It is not merely an indicator-vector estimate.

## 3. Burgess ledger

For a nonprincipal character modulo the prime `q`, Burgess with parameter
`r=2` gives, uniformly for an interval of length `O(R)`,

```text
S_R <=C_epsilon R^(1/2)q^(3/16+epsilon).           (3.1)
```

The symmetric residual set is a union of two intervals.  Hence (2.3) is

```text
<<q^epsilon(log q)^(3/2)
  {R/sqrt(q)+R^(1/4)q^(3/32)} product ||.||_2.     (3.2)
```

At `A=50/33`, `R=q^(16/33+o(1))`.  The nonprincipal standardized-skew
exponent is

```text
(16/33)/4+3/32=4/33+3/32=227/1056.                (3.3)
```

The principal term has exponent `16/33-1/2=-1/66` and is negligible.
Point evaluation costs at most `sqrt(M)=q^(1/2+o(1))`; therefore the
transverse exponent is

```text
1/2+227/1056=755/1056.                             (3.4)
```

The previous full-shell exponent is `49/66=784/1056`, so the numerical
saving in this restricted game is exactly `29/1056`.

## 4. Mean, variance, and the unmixed cubic

On either one-sided shell, positive analytic frequencies are separated by
`c_w/q`, and the smallest frequency is also at least `c_w/q`.  Since
`B/q=q^(A-1+o(1))` tends to infinity, Schwartz decay and an absolute Gram
row estimate give, uniformly in the coefficient vector,

```text
mean(F)=q^(-K)||y||_2,
Var(F)=(1/2+o(1))||y||_2^2                         (4.1)
```

after choosing the fixed Fourier-decay order as large as required.  More
explicitly, the mean first costs `sqrt(M)`, while every off-diagonal row is
bounded by

```text
sum_(d>=1)(1+c_w(B/q)d)^(-K)=O((B/q)^(-K)).        (4.2)
```

For the upper side, the analytic frequencies in `P^3` are all positive;
for the lower side the analogous positive-frequency parametrization has
the same property.  Their sum is at least `c_w/q`, so `P^3` and its
conjugate are Schwartz-negligible even after the `M^(3/2)` coefficient
cost.  The only nonnegligible cubic is `P^2 conjugate(P)`, whose frequency
condition is precisely

```text
|2ab-qc|<<q^2/B asymp R.                           (4.3)
```

Mean-centering changes the third moment only by negligible terms from
(4.1).

## 5. Smooth-kernel tail repair

On the fixed shell,

```text
|hat psi(B log(2ab/(qc)))|
 <=C_L(1+|2ab-qc|/R)^(-L).                         (5.1)
```

For dyadic residual radii `2^jR<=q/4`, apply (2.3), Burgess, and the factor
`2^(-jL)`.  The sum preserves (3.2) as soon as `L>1`.

For the remaining tail `|2ab-qc|>=q/4`, do not reuse the small-residual
incidence lemma.  Instead use

```text
sum |x_a y_b z_c|
 <=M^(3/2)||x||_2||y||_2||z||_2
```

and (5.1).  Its norm is at most

```text
q^(3/2)(R/q)^L=q^(3/2-L(A-1)+o(1)),                (5.2)
```

which is smaller than every required fixed power when `L` is chosen large.
This closes the authoring proof's only omitted range.

## 6. Exact conclusion and scope

The centered cubic endpoint inequality now gives

```text
sup F_y >=q^(-227/1056-o(1))||y||_2.               (6.1)
```

The trivial calibrated leverage bound is

```text
[-y dot v]_+ <=C sqrt(M)||y||_2,                   (6.2)
```

uniformly in the legal base point and depth.  Support-function separation
therefore proves

```text
s_v >=q^(-755/1056-o(1))                           (6.3)
```

for the one-sided prime-power coordinate system at `Y=q/2`.

Audit ledger:

```text
restricted cubic tensor (2.3):                     VERIFIED;
prime-power fixed-fibre multiplicity:               VERIFIED;
principal-character interpolation:                  VERIFIED;
Burgess r=2 exponent 755/1056:                      VERIFIED;
smooth tail after explicit truncation:              VERIFIED;
one-sided mean/variance and P^3 separation:          VERIFIED;
balanced full-shell exponent below 49/66:            NOT PROVED;
QP, QP equivalence, or a uniform strip:              NOT PROVED.
```

## 7. Density-one refinement (separate re-audit)

Put `h=2-A<1/2` and restrict prime moduli to `q in [Q,2Q]`.  Choose the
deterministic length

```text
D_0=ceil(sup_(Q<=q<=2Q) R(q)) asymp Q^h.
```

Positivity gives `E_(R(q))<=E_(D_0)`.  This is the legitimate enlargement;
no comparison between the absolute values of two character sums is used.
For each fixed `D_j=2^jD_0<=Q^(1/2)`, the multiplicative large sieve applied
to the fourth power of `sum_(r<=D_j)chi(r)` gives

```text
sum_(Q<=q<=2Q) sum_(chi primitive mod q)
 |sum_(r<=D_j)chi(r)|^8 <=Q^(2+o(1))D_j^4.         (7.1)
```

Thus the number of prime moduli having any character larger than
`D_j^(1/2)Q^(1/8+2 epsilon)` is
`O(Q^(1-16 epsilon+o(1)))`.  A union over the `O(log Q)` fixed dyadic
windows is harmless.  Positive dyadic majorants for the smooth kernel then
give

```text
sqrt(S)<=D_0^(1/4)Q^(1/16+o(1)).                  (7.2)
```

The windows beyond `Q^(1/2)` are negligible by Schwartz decay and a raw
norm because `h<1/2`.  Hence the density-one transverse exponent is indeed

```text
1/2+h/4+1/16=361/528                               (7.3)
```

when `h=16/33`.  This remains a density-one, one-sided prime-center result,
not a uniform full-shell theorem.
