# R100 varying-prime discriminant, conductor, and contact-parity gate

Status: exact outer-prime trace-square theorem, exact one-axis central-value
classification, Heath--Brown quadratic-large-sieve reduction with the actual
square-kernel norm, trace-variable additive-large-sieve theorem, exact
nonparabolic trace-fiber and adjacent-continuant factorizations,
almost-injective affine-line parametrization, sharp `Omega(H)` weighted
energy examples, critical conductor ledger,
Poisson/Burgess threshold audit, row-dependent-weight obstruction, and a
signed-contact parity theorem.
Quadratic reciprocity in the outer prime has no nonzero principal diagonal;
the exceptional central value on a single axis requires a second zero and is
therefore a paired-axis term.  In the square-root box, the integer
discriminant has natural full height `R^4`, putting an outer interval of length
`R` exactly at the fourth-root conductor threshold.  The standard quadratic
large sieve gives no saving even under favorable coefficient separation,
and its square-kernel diagonal is an `L^2` pairing rather than the missing
`+P_1+P_2` contact.  No fixed zeta zero-free strip, and no theorem excluding
all fixed strips, is proved here.

Date: 2026-08-07.

## 1. Verdict

R89 left the signed varying-prime fourth trace

```text
Q_off
 =sum_(r prime) omega_r
   sum_h c_r(h) Legendre_r(Delta_a(h)),                 (1.1)

c_r(h)=product_(i=1)^4 z_(i,r)(h_i),

Delta_a(h)
 =[a^2 h_1h_2h_3h_4-a(h_1+h_3)(h_2+h_4)+2]^2-4.       (1.2)
```

The weights in (1.1) are placeholders only for notation: throughout the
actual application they must retain `omega_r`, the common-cofactor mask,
the four completed autocorrelations, the B-spline amplitude, and the
rectangular limiting order.

There are four new exact conclusions.

1. Write `T` for the trace in brackets in (1.2).  An integer of the form
   `T^2-4` is never a nonzero square.  Consequently the outer quadratic
   character has no nonzero principal square-kernel class.  Its only
   square case is `Delta=0`, where the ordinary Legendre symbol is zero.

2. On the single axis `h_1=0`, put

   ```text
   X=a h_3(h_2+h_4).
   ```

   Then

   ```text
   T=2-X,              Delta=X(X-4).                   (1.3)
   ```

   The special `SL_2(F_r)` character value `r` occurs at `g=I` only when

   ```text
   h_3=0,              h_2+h_4=0       (mod r),        (1.4)
   ```

   and `g=-I` is impossible on this slice.  Thus even the exceptional
   central term needs a second zero and a paired opposite frequency.  It
   cannot supply a single-axis B-spline marginal.

3. If one makes the most favorable separability assumption
   `c_r(h)=omega_r c(h)`, Heath--Brown's quadratic large sieve gives the
   honest bound

   ```text
   abs(Q_off)
    <<(RD)^epsilon norm(omega)_2 (R+D)^(1/2)
      [sum_d (sum_m abs(A_(d m^2)))^2]^(1/2),          (1.5)

   A_n=sum_(h: Delta_a(h)=n)c(h),
   D=max_h abs(Delta_a(h)).                            (1.6)
   ```

   At the critical fixed-modulus scale `h_i~H=R^(1/2)` and even in the
   best case `a~1`, one has `D~H^8=R^4`.  With unit, collision-free
   coefficients, (1.5) has scale `H^7`, while direct summation has scale
   `H^6`.  The imported theorem is worse by `H=R^(1/2)` at this gate.

4. The absence of a first-moment principal diagonal and the failure of
   (1.5) are separate from the contact problem.  Applying an outer
   quadratic large sieve squares (1.1).  Its diagonal pairs equal
   squarefree kernels.  Every axis contribution is therefore paired with a
   second coefficient: either another axis coefficient or an off-axis
   coefficient with the same kernel.  The imported inequality does not
   evaluate such a cross term as the standalone signed coefficient `+1`
   multiplying `P_1` or `P_2`.  Summing over `r` does not change the
   fixed-`r` parity theorem from R89.

5. Grouping by the integer trace `T`, rather than by the squarefree kernel
   of `T^2-4`, avoids the `R^4` conductor charge.  Additive Fourier
   expansion and the classical additive large sieve give

   ```text
   sum_(r~R) abs(sum_T A_T Legendre_r(T^2-4))^2
    <<(R^2+N)sum_T abs(A_T)^2
      +R^(-1)abs(sum_T A_T)^2,                         (1.6a)
   ```

   for `A_T` supported in an interval of length `N`.  An exact divisor
   factorization bounds every nonparabolic trace fiber by `H^(2+o(1))`.
   At `N=H^4=R^2`, this improves the `H^7` Heath--Brown ledger to `H^6`,
   exactly the direct-summation scale.  A power saving is equivalent to a
   strictly stronger weighted trace-collision estimate, isolated below.

This gives a sharp method-level no-go:

```text
signed first outer moment:   no nonzero principal Delta class;
outer quadratic L2 moment:   paired squarefree kernels only;
special central character:   paired axis only;
critical conductor:          R^4 against an interval of length R;
actual r-dependent weights:  outside the coefficient-uniform theorem. (1.7)
```

Quadratic reciprocity remains a legitimate way to reorganize the off-axis
sum.  But the standard real-character large sieve and Poisson/completion do
not give a fixed-power estimate at the R71 scale, and none of these
operations generates the missing one-axis contact.

## 2. Trace factorization and the missing principal character

Put

```text
F=a^2h_1h_2h_3h_4-a(h_1+h_3)(h_2+h_4),
T=F+2.                                                   (2.1)
```

Then the discriminant has the useful exact factorization

```text
Delta=T^2-4=F(F+4).                                     (2.2)
```

This factorization has an arithmetic consequence which is different from
the *polynomial-square four-tuple locus* in R89.  Here we ask when the one
integer value `Delta` has trivial squarefree kernel as the outer prime
varies.

**Theorem 2.1 (no nonzero square trace discriminant).**  If `T,y` are
integers and

```text
T^2-4=y^2,                                              (2.3)
```

then `T=plusminus2` and `y=0`.

### Proof

Equation (2.3) gives

```text
(T-y)(T+y)=4.                                           (2.4)
```

The two factors have the same parity.  The only same-parity factor pairs of
`4` are `(2,2)` and `(-2,-2)`.  Hence `T=2` or `T=-2` and `y=0`.  QED.

Thus, away from `Delta=0`, the real character

```text
r |-> Legendre_r(Delta)                                 (2.5)
```

is never the principal character for the tautological reason that `Delta`
is a square.  The `Delta=0` value of the ordinary Legendre symbol is zero,
not one.

There are only two negative discriminant values.  Since `T` is an integer,

```text
Delta<0       if and only if       T in {-1,0,1},

Delta in {-3,-4}.                                       (2.6)
```

They give the fixed characters of squarefree kernels `-3` and `-1`.
These are nonprincipal over the full odd-prime family.  Restricting outer
primes to a specially selected residue class can make one of them constant,
but that would be an imposed outer coefficient correlation and still
supports only the thin trace levels in (2.6), not the full axis marginal.

For a fixed positive squarefree kernel `d>1`, equal-kernel collisions obey
the Pell-type equation

```text
T^2-dy^2=4.                                             (2.7)
```

This is the exact source of the square-kernel pairing in the quadratic
large sieve.  It is not a linear main term.

## 3. The one-axis exceptional character is actually paired

Set `h_1=0`.  Then (2.1) becomes

```text
X=a h_3(h_2+h_4),
T=2-X,
Delta=X(X-4).                                          (3.1)
```

The principal square cases from Theorem 2.1 are

```text
X=0 or X=4,          Delta=0.                          (3.2)
```

The two fixed negative kernels are

```text
X=1 or 3:            Delta=-3,
X=2:                 Delta=-4.                        (3.3)
```

All other nondegenerate integral values have a varying positive nonsquare
kernel.

The special character used by Blomer--Pascadi is not determined by trace
alone at `Delta=0`: it has value `r` at `g=plusminus I`, while a noncentral
unipotent trace-`plusminus2` element is not given that value.  The matrix
calculation settles the distinction.

With

```text
T(x)=[[1,x],[0,1]],           S=[[0,-1],[1,0]],         (3.4)
```

the four-step product on `h_1=0` is

```text
g=
 [[1-a h_3h_4,                 a h_3],
  [-h_2+h_4(a h_2h_3-1),       1-a h_2h_3]].           (3.5)
```

Let `r` be an odd prime and let `a` be a unit modulo `r`.

**Theorem 3.1 (central one-axis classification).**  On `h_1=0`,

```text
g=I       if and only if       h_3=0 and h_2+h_4=0 (mod r),
g=-I      never occurs.                                      (3.6)
```

### Proof

The upper-right entry of (3.5) forces `h_3=0` for either central value.
Both diagonal entries then equal `1`, so `g=-I` is impossible.  The
lower-left entry becomes `-(h_2+h_4)`, giving (3.6).  QED.

The large exceptional value therefore contains:

```text
one declared zero h_1=0
 + a second zero h_3=0
 + the paired relation h_2=-h_4.                       (3.7)
```

It is exactly an even/paired-axis configuration.  Its weight is built from
`z_1(0)z_3(0)z_2(h)z_4(-h)`, an autocorrelation energy.  It is not the R71
contact

```text
P_1+P_2=2 Re<Lambda(n)delta_n-dt,G_1>,                 (3.8)
```

which has one zero Fourier coordinate and is linear in the one-axis
B-spline marginal.

Thus neither the ordinary principal Legendre value nor the exceptional
`SL_2` central value supplies the missing coefficient.

## 4. Exact Heath--Brown reduction for separated outer weights

To give quadratic reciprocity every possible advantage, first assume that
after dyadic localization and Mellin separation the coefficient has the
form

```text
c_r(h)=omega_r c(h).                                   (4.1)
```

Define

```text
A_n=sum_(h:Delta_a(h)=n)c(h).                          (4.2)
```

Then, with ramified values retained automatically,

```text
Q=sum_(r~R, r prime)omega_r sum_(abs(n)<=D)A_n(n/r).   (4.3)
```

Split the sign and the bounded 2-adic classes of `n`; this costs only a
fixed number of sums.  Cauchy's inequality in `r`, followed by the real
quadratic large sieve, gives

```text
abs(Q)^2
 <<(RD)^epsilon norm(omega)_2^2 (R+D)
   sum_(n_1 n_2=square)abs(A_(n_1)A_(n_2)).            (4.4)
```

Writing each nonzero integer as `d m^2` with signed squarefree `d`, the
last factor is

```text
S_square(A)
 =sum_d [sum_m abs(A_(d m^2))]^2.                     (4.5)
```

This is the exact general-coefficient norm.  Replacing it by
`sum_n abs(A_n)^2` is valid only when the support is squarefree, or after a
separate square-multiple argument.  Grouping signed coefficients as

```text
A_d^signed=sum_m A_(d m^2)                             (4.6)
```

can be smaller, but proving that cancellation is itself a new theorem
inside each Pell fiber; it is not supplied by the quadratic large sieve.

There is also a ramification detail.  If `n=d m^2`, then

```text
(n/r)=(d/r)1_(r not dividing m).                       (4.7)
```

Dropping the mask in (4.7) is not exact.  Formula (4.4), applied before
squarefree reduction, is the clean way to retain primes dividing the
square part.

The imported baseline is Heath--Brown,
[*A mean value estimate for real character sums*](https://doi.org/10.4064/aa-72-3-235-275),
Theorem 1 and Corollary 2.  The modern explicit form, with the same
`R+D` and square-pair structure, is Zihao Liu,
[*Explicit quadratic large sieve inequality*](https://arxiv.org/abs/2505.09637),
equations (10), (36), and (37).  Restricting the outer squarefree moduli to
primes only makes the left side smaller.

## 5. The critical conductor budget fails before coefficient losses

Let

```text
abs(h_i)<=H,
abs(a) asymp 1.                                         (5.1)
```

Then

```text
abs(T)<<H^4,
abs(Delta)<<H^8.                                       (5.2)
```

The exponent is attained on a full box.  For example, when `a=1` and all
`h_i` lie in `[H/2,H]`, the quartic term in (2.1) dominates the quadratic
term once `H` is large, so

```text
abs(T)asymp H^4,        abs(Delta)asymp H^8.           (5.3)
```

At the Blomer--Pascadi critical range, the completed differences satisfy

```text
H asymp R^(1/2).                                       (5.4)
```

Even in this best fixed-`a` model,

```text
D asymp H^8=R^4.                                      (5.5)
```

If the representative `a` also varies with `r` and has size larger than a
constant, (5.5) only gets worse unless a separate congruence normalization
is proved.

Here is the optimistic coefficient ledger.  There are

```text
K=H^4                                                     (5.6)
```

four-tuples.  Pretend that their nonzero discriminants are collision-free
and their coefficients have unit size, so

```text
S_square(A)=K=H^4.                                     (5.7)
```

This is more favorable than the actual square-kernel collision norm.  Take
unit outer weights.  Formula (4.4) gives

```text
quadratic-large-sieve scale
  R^(1/2) D^(1/2) K^(1/2)
  =H * H^4 * H^2
  =H^7.                                                (5.8)
```

Direct summation gives

```text
R K=H^2 H^4=H^6.                                      (5.9)
```

Thus the standard varying-modulus quadratic large sieve is worse than the
trivial estimate by `H=R^(1/2)` in the most optimistic collision ledger.
Squarefree-kernel collisions only increase (4.5).

The same ratio holds for the natural outer weight `log(r)/r`: both sides
lose the same outer `R` normalization.

This is not a defect in Heath--Brown's theorem.  It is a geometry mismatch.
The theorem charges the **height of the character conductor**, not the
cardinality `K` of the sparse polynomial image.  A hypothetical sparse
polynomial large sieve with `R+K` in place of `R+D` would give

```text
R^(1/2) K^(1/2) K^(1/2)=H^5,                          (5.10)
```

a factor `H` saving over (5.9).  No such theorem for the actual
four-variable discriminant and its `r`-dependent weights is being imported.

Equivalently, merely to make (4.4) non-worse in this unit model one would
need effective conductor height

```text
D<<H^6=R^3,                                            (5.11)
```

whereas the full coefficient-uniform height is `H^8=R^4`.  A fixed-power gain needs a
fixed-power improvement beyond (5.11), not just removal of logarithms.

### 5.1 Trace-variable Fourier expansion removes the height, but only to the natural scale

The squarefree-kernel reindexing is not the only way to use the special
form of the discriminant.  Define, for an odd prime `r`,

```text
f_r(T)=Legendre_r(T^2-4).                              (5.12)
```

This is an `r`-periodic trace function of bounded algebraic complexity.  Its
complete zero mode is exact:

```text
sum_(T mod r)f_r(T)=-1.                                (5.13)
```

Indeed the standard quadratic-polynomial character identity gives `-1`
because `T^2-4` has nonzero discriminant.  Parseval also gives

```text
sum_(k mod r)abs(fhat_r(k))^2
 =r sum_(T mod r)abs(f_r(T))^2
 =r(r-2),                                             (5.14)

fhat_r(k)=sum_(T mod r)f_r(T)e_r(-kT).                 (5.15)
```

Let `(A_T)` be supported in an interval of `N` consecutive integers and put

```text
S_r(A)=sum_T A_T f_r(T).                               (5.16)
```

Fourier inversion gives

```text
S_r(A)
 =r^(-1)sum_(k mod r)fhat_r(k)
       sum_T A_T e_r(kT).                              (5.17)
```

For `k!=0`, Cauchy's inequality and (5.14) show

```text
abs(S_r^*(A))^2
 <=sum_(k=1)^(r-1)abs(sum_T A_T e_r(kT))^2.            (5.18)
```

As `r` ranges over primes in `[R,2R]`, all fractions `k/r`,
`1<=k<r`, are reduced and distinct.  The additive large sieve therefore
proves:

**Theorem 5.1 (varying-prime trace large sieve).**  One has

```text
sum_(R<=r<=2R, r prime)abs(S_r(A))^2
 <<(R^2+N)sum_T abs(A_T)^2
   +R^(-1)abs(sum_T A_T)^2.                            (5.19)
```

The last term is the contribution of `k=0`, since (5.13) makes it
`-r^(-1)sum_T A_T` for each prime.  Logarithmic improvements from counting
only primes are immaterial here.

The special `SL_2` character differs from (5.12) on central matrices.  Its
correction is kept separately; Theorem 3.1 has already shown that on a
single axis this correction is a paired-axis configuration.

It remains to bound the trace coefficients produced by the four `h`
variables.  Put

```text
A_T=sum_(h: trace_a(h)=T)
       z_1(h_1)z_2(h_2)z_3(h_3)z_4(h_4),
T!=plusminus2.                                         (5.20)
```

There is an exact factorization of every fiber.  Fix `(h_1,h_3)` and write

```text
u=h_1h_3,             x=h_1+h_3,             F=T-2.   (5.21)
```

Then the trace equation is equivalent to

```text
(a u h_2-x)(a u h_4-x)=uF+x^2.                        (5.22)
```

**Theorem 5.2 (nonparabolic trace-fiber bound).**  Suppose
`abs(h_i)<=H`, `a!=0`, and `abs(a)<=H^C` for a fixed `C`.  For every
`T!=plusminus2`,

```text
#{h:trace_a(h)=T}<<H^(2+o(1)).                         (5.23)
```

### Proof

For `u!=0`, the right side of (5.22) cannot vanish.  Indeed

```text
uF+x^2=h_1^2+T h_1h_3+h_3^2.                          (5.24)
```

If this were zero with `h_1h_3!=0`, the rational number `h_1/h_3` would be
a root of `X^2+TX+1`, forcing `T^2-4` to be a rational square.  For integer
`T`, Theorem 2.1 then forces `T=plusminus2`.  Thus (5.22) has at most
`H^o(1)` factor pairs for each of the `O(H^2)` choices of `(h_1,h_3)`.

If `u=0` but not both `h_1,h_3` vanish, the trace equation fixes
`h_2+h_4`, giving `O(H)` pairs for each of `O(H)` axis choices.  If both
vanish, then `T=2`, which was excluded.  This proves (5.23).  QED.

Cauchy within each fiber now gives the coefficient-uniform energy bound

```text
sum_(T!=plusminus2) abs(A_T)^2
 <<H^(2+o(1)) product_(i=1)^4 norm(z_i)_2^2.           (5.25)
```

At the critical scale

```text
R=H^2,                 N=H^4=R^2,                     (5.26)
```

Theorem 5.1, (5.25), and Cauchy in the outer prime give, for unit-size
outer weights in the power ledger,

```text
abs(sum_r omega_r S_r(A))
 <<H^(4+o(1)) product_i norm(z_i)_2.                  (5.27)
```

The direct coefficient-uniform bound is exactly the same:

```text
sum_r sum_h abs(product_i z_i(h_i))
 <=R H^2 product_i norm(z_i)_2
 =H^4 product_i norm(z_i)_2.                          (5.28)
```

Thus trace grouping is a real improvement over (5.8): it removes the extra
factor `H`.  But the exact general bound lands at equality, not at a fixed
power.

The new off-axis target is now extremely concrete.  If for the actual
separated B-spline packets one could prove, for some `delta>0`,

```text
sum_(T!=plusminus2) abs(A_T)^2
 <<H^(2-2delta+o(1)) product_i norm(z_i)_2^2,           (5.29)
```

then (5.27) would gain `H^(-delta)=R^(-delta/2)`.  This
is a weighted multiplicative/incidence estimate for the trace fibers, not a
zero-free theorem by itself.  The max-fiber divisor argument proves only
the endpoint `delta=0`.

### 5.2 The adjacent continuant identity does not supply the missing power

There is a second exact factorization, now based on an adjacent pair.  Put

```text
p=a h_1h_2-1,                 T=trace_a(h_1,h_2,h_3,h_4).
```

Direct expansion gives

```text
(p a h_3-a h_1)(p h_4-h_2)=p^2+Tp+1.                (5.30)
```

For `a=1`, this is precisely a length-two instance of the reciprocal
quadratic continuant equation studied structurally by Badziahin in
[*Continuant Diophantine equations*](https://arxiv.org/abs/1607.07212).
The cited paper relates such equations to factorizations of polynomial
values; it does not state the uniform bounded-box fiber estimate needed
here.

Equation (5.30) gives another proof of the endpoint (5.23).  If
`p!=0` and `T!=plusminus2`, then `p^2+Tp+1!=0`: otherwise the integer
quadratic `X^2+TX+1` would have the rational root `p`, forcing
`T^2-4` to be a square and hence `T=plusminus2`.  For each fixed
`(h_1,h_2)`, the two left factors in (5.30) therefore have only
`H^o(1)` possibilities, after which `h_3,h_4` are fixed.  The case
`p=0` contains only finitely many adjacent pairs and contributes `O(H)`.

The important fail-fast point is that (5.30) does **not** prove an
`H^(1+o(1))` maximum fiber.  It leaves the outer adjacent product `p`.
That parameter has genuinely near-quadratic range, not merely an artifact
of a loose interval bound.  Already for `a=1`, take

```text
h_1=q prime in (H/2,H],       1<=h_2<=H/2.             (5.31)
```

All products `q h_2`, and hence all resulting `p`, are distinct: if
`q m=q' n` with `q,q'>H/2` prime and `m,n<=H/2`, then `q=q'` and
`m=n`.  The prime number theorem therefore gives

```text
#{p in (5.31)} >> H^2/log H=H^(2-o(1)).               (5.32)
```

Thus any proof which applies a divisor bound separately for every `p` and
then sums absolutely is locked at `H^(2+o(1))`.  Reaching
`H^(1+o(1))` requires a new theorem correlating the factorizations of
the varying reciprocal quadratics `p^2+Tp+1`; it does not follow from the
continuant identity itself.  This is a concrete method obstruction, not a
counterexample to an `H^(1+o(1))` fiber theorem.

The same identity does, however, isolate the precise part of the *energy*
which is still missing.  For clarity take `a=1` and write

```text
U=p h_3-h_1,        V=p h_4-h_2,        N_p(T)=p^2+pT+1.  (5.32a)
```

On the diagonal with the same nonzero `p` in both copies of the squared
energy, there are divisor-many adjacent pairs because
`h_1h_2=p+1`, and divisor-many representations `UV=N_p(T)`.  Cauchy
therefore bounds the complete `p=q!=0` diagonal by

```text
H^o(1) product_i norm(z_i)_2^2.                       (5.32b)
```

The degenerate cell `p=0` is different but elementary.  Its only signed
nonzero adjacent pairs are `(h_1,h_2)=(1,1),(-1,-1)`, and their traces are

```text
T=1-h_3-h_4,              T=1+h_3+h_4.               (5.32c)
```

Young's convolution inequality gives exactly an `O(H)` energy bound for
this cell.  It is the source of the sharp examples in Section 5.4.

For two distinct nonzero cells `p,q`, equality of their traces is
equivalent to the exact shifted determinant equation

```text
qUV-pU'V'=(p-q)(pq-1).                                (5.32d)
```

Indeed multiply `UV=N_p(T)` by `q`, multiply
`U'V'=N_q(T)` by `p`, and subtract.  Thus the candidate (5.40) has been
reduced further: its only non-elementary part is an off-diagonal weighted
shifted-divisor large sieve for (5.32d), averaged over the near-quadratic
multiplication-table set of `p,q`.  The continuant factorization proves
the diagonal bound but supplies no cancellation in this off-diagonal sum.

### 5.3 Almost-injective affine lines isolate the remaining incidence

The trace is affine in its fourth coordinate:

```text
T=C h_4+D,
C=a^2h_1h_2h_3-a(h_1+h_3),
D=2-a(h_1+h_3)h_2.                                  (5.33)
```

On nonzero coordinates, the map `(h_1,h_2,h_3)->(C,D)` has
`H^o(1)` multiplicity.  Indeed put `x=h_1+h_3` and `u=h_1h_3`.
If `K=2-D!=0`, then

```text
K=a x h_2,             C=a^2u h_2-a x.               (5.34)
```

There are only divisor-many choices for `(x,h_2)`, then `u` is fixed,
and `h_1,h_3` are the at most two roots of `X^2-xX+u`.  If `D=2`,
then `x=0` and

```text
C=-a^2h_1^2h_2,                                      (5.35)
```

which again has divisor-type multiplicity.

This removes a possible hidden `H`-fold collision among identical affine
lines.  It still does not bound the energy of their evaluations
`C h_4+D`: different lines can meet at different integer arguments.  The
unresolved theorem can equivalently be stated as a weighted incidence
bound for this explicit almost-injective family of lines.

There is also an exact two-dimensional dot-product form:

```text
T-2=a (a h_1h_3,-h_1-h_3) dot (h_2h_4,h_2+h_4).       (5.36)
```

Each pair invariant has multiplicity at most two.  Generic incidence
estimates at this point recover the `H^2` endpoint; an `H`-scale operator
bound would have to exploit the two discriminant-square lattices in
(5.36), not merely their cardinalities.

### 5.4 The strongest possible trace-energy power is now sharp

The candidate improvement in (5.29) cannot have `delta>1/2`.  Take
`a=1`,

```text
z_1=z_2=delta_1,       z_3=z_4=1_[1,H].               (5.37)
```

Then `T=1-h_3-h_4`, and after deleting `T=plusminus2` one obtains exactly

```text
sum_(T!=plusminus2)|A_T|^2=(2H^3+H)/3-4,
product_i norm(z_i)_2^2=H^2.                         (5.38)
```

Hence the energy-to-norm ratio is `(2/3+o(1))H`.

This lower scale persists for genuine zero-axis autocorrelations.  Take the
first two packets to be the punctured autocorrelation of `(1,1)`, and the
last two to be the punctured autocorrelation of the flat packet of length
`H+1`.  Restricting to `h_1=h_2=1` and
`ceil(H/4)<=h_3,h_4<=floor(H/2)` gives only nonparabolic traces and proves

```text
trace energy / product_i norm(z_i)_2^2 >= H/24576.    (5.39)
```

Thus the best conceivable coefficient-uniform result is

```text
sum_T |A_T|^2 << H^(1+o(1)) product_i norm(z_i)_2^2,  (5.40)
```

equivalently the endpoint `delta=1/2` in (5.29).  The examples do not
disprove (5.40); they prove that it must be sharp and that no further
power can be reserved for later losses.

## 6. Poisson and Burgess meet the same fourth-root wall

Quadratic reciprocity turns a fixed squarefree kernel `d` into a real
Dirichlet character in the outer variable `r`, of conductor comparable to
`abs(d)` up to the standard factor `4`.  The integer height which must be
allowed uniformly is

```text
abs(Delta)asymp R^4.                                   (6.1)
```

If the squarefree kernel has full scale
`abs(d)asymp abs(Delta)`, its primitive conductor is therefore `R^4`.
R100 does not assume this for every tuple: concentration of the actual
B-spline mass on unusually squarefull discriminants is one possible escape.
Without such a theorem, a coefficient-uniform reciprocity argument must
allow full-scale kernels.  In that full-scale case, the following
completion ledger applies.

Completing an `r`-sum of length `R` modulo `d` produces a dual length

```text
abs(d)/R asymp R^3                                    (6.2)
```

and square-root completion costs `sqrt(abs(d))asymp R^2`, both worse than
the original length `R`.

The same relation is the Burgess endpoint:

```text
R=abs(d)^(1/4).                                        (6.3)
```

Classical Burgess cancellation starts uniformly only beyond the
fourth-root threshold (with an epsilon margin).  At (6.3) it supplies no
fixed power, and a von-Mangoldt/prime-weighted outer sum is not easier than
the underlying integer character sum.

This explains why the off-the-wall reciprocity idea lands on a familiar
barrier despite beginning with a four-variable `SL_2` trace: degree four in
the trace becomes degree eight in the discriminant, while the completed
differences have square-root length.

A route through (6.3) would need one of the following genuinely new facts:

```text
most actual B-spline weight lies on abs(sf(Delta))<<R^(3-delta);
a sparse-polynomial quadratic large sieve depending on image size;
or cancellation inside the Pell fibers before applying the large sieve. (6.4)
```

None follows from quadratic reciprocity alone.

## 7. Height versus coefficient separability

The common real-character coefficient in (4.2) must be independent of the
outer modulus.  This is essential, not technical.

**Lemma 7.1 (row-dependent weights have no character saving).**  For any
finite family of nonzero Legendre symbols, arbitrary coefficients
`b_(r,d)` can be chosen as

```text
b_(r,d)=conjugate((d/r)) abs(b_(r,d)).                 (7.1)
```

Then

```text
sum_(r,d)b_(r,d)(d/r)=sum_(r,d)abs(b_(r,d))            (7.2)
```

over the nonramified pairs.  Hence no coefficient-uniform large sieve can
save for a different sequence on every row `r`.

The actual R71 coefficient is not literally adversarial, but it is
`r`-dependent:

```text
omega_r,
z_(i,r)(h),
residue aggregation modulo r,
common-g masks,
B-spline scales and seams,
rectangular endpoints.                                 (7.3)
```

Smooth dependence might be separated by Mellin expansion at subpower rank,
as in earlier low-beat tensor work.  Residue aggregation and primitive
masks still need an exact interface theorem.  Granting such a theorem leads
back to the unfavorable conductor ledger (5.8).

There is a particularly clean dichotomy.  If one retains the integer
polynomial `Delta_a(h)` independent of `r`, its height is `R^4`.  If one
replaces it by a least residue modulo `r` to force height `O(R)`, the new
integer label depends on `r`, so the common coefficients `A_n` in (4.2) no
longer exist.  Thus:

```text
common squarefree kernel across r       => conductor-height barrier;
small representative for each r         => row-dependent-weight barrier. (7.4)
```

Quadratic reciprocity cannot take both advantages simultaneously.

## 8. Why the outer average still cannot create `+P_1+P_2`

The all-sector conservation law requires

```text
H_nonW=-P_1-P_2+Y^o(1),

H_off must contribute +P_1+P_2 at fixed-power accuracy. (8.1)
```

There are three possible places to look for such a contribution, and the
preceding calculations close each automatic version.

### 8.1 Signed first moment

A signed average over `r` before absolute values can have a stable
quadratic-character diagonal only when the outer character is principal.
Theorem 2.1 shows that there is no nonzero principal discriminant.  On the
single axis, the only trace-square values have `Delta=0`, for which the
ordinary symbol vanishes.

The special character value at `g=I` does survive, but Theorem 3.1 makes it
a double-zero paired-axis term.  Its coefficient is an autocorrelation
energy, not `+P_1`.

An accidental correlation between the actual `r`-dependent weights and a
nonprincipal character is logically possible.  Proving it with exactly the
coefficient `+1` would be a new coefficient-specific first-moment theorem;
it is not a diagonal furnished by reciprocity.

### 8.2 Outer quadratic large sieve

Squaring (4.3) gives

```text
sum_r abs(sum_d A_d(d/r))^2.                            (8.2)
```

Its diagonal is `d_1=d_2` (more precisely, `n_1n_2` a square).  An axis
packet can occur only paired with another packet of the same squarefree
kernel.  The resulting terms have the form

```text
abs(A_d^axis)^2
or
2 Re[A_d^axis conjugate(A_d^off)].                    (8.3)
```

They are `L^2` energies/correlations.  There is no coefficient multiplying
one copy of the full axis marginal alone.  This is the outer-prime analogue
of R89 Corollary 4.2, not a repair of it.

### 8.3 The fixed-modulus fourth trace

The discriminant (1.2) appears only after the Cauchy--Schwarz and fourth
trace steps of the Blomer--Pascadi argument.  Those steps produce a positive
moment majorant for the original signed bilinear form.  A bound for that
majorant can prove an off-axis upper bound, but it cannot certify a signed
main term cancelling an axis which was separated before Cauchy.

If the axes are inserted into the moment before taking the fourth power,
the polynomial-square parity from R89 pairs every zero input.  If they are
kept outside, the discriminant theorem never sees their sign.  Therefore:

**Theorem 8.1 (Cauchy/contact incompatibility).**  Within the standard
Blomer--Pascadi discriminant conversion followed by the Heath--Brown
quadratic-large-sieve diagonal, an axis is either paired locally as in R89
or paired with a second equal-kernel coefficient as in (8.3).  The imported
diagonal supplies no standalone one-axis term with the fixed coefficient
`+1` required by (8.1).  Obtaining that coefficient from an axis/off-axis
cross term would require a new signed evaluation of the cross term, not the
large-sieve upper bound.

This theorem does not say that the original signed off-axis block cannot
cancel the contact.  It says that the even-moment quadratic-character
mechanism cannot prove that cancellation as a main-locus identity.

## 9. Relation to the fixed-modulus theorem

Blomer--Pascadi prove a relative `r^(-1/32)` saving in their native
critical fixed-modulus bilinear form; see
[*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311),
Theorem 1.1.  R89 already records the remaining interface differences with
R71.

R100 does not weaken that theorem and does not attempt to re-prove it.  It
answers a different question: whether retaining the sign and summing over
the varying outer prime repairs the contact or creates an additional
large-sieve saving.  The answer for the imported quadratic-large-sieve,
Poisson, and diagonal mechanisms is no:

```text
fixed r:       genuine off-axis saving, paired-axis square locus;
varying r:     conductor R^4, fourth-root outer range, paired-kernel L2;
contact:       still a separate signed first-axis theorem.          (9.1)
```

Summing valid fixed-`r` upper bounds by triangle inequality may preserve a
fixed-`r` saving after all interface hypotheses are checked.  It discards
the signed outer recombination and supplies no `+P_1+P_2` coefficient.

## 10. What theorem would actually move the frontier

There are now three distinct possible successors.

The most concrete off-axis successor is the weighted trace restriction
estimate (5.29).  It would upgrade the exact additive trace large sieve
from the natural endpoint to a fixed-power saving while retaining the
special form `T^2-4`.  It still requires a low-rank separation of the actual
`r`-dependent B-spline packets.

The second is an off-axis-only sparse square-kernel theorem:

```text
sum_(r~R) omega_r sum_h c_r(h)(Delta_a(h)/r)
 <<R^(-delta) times its natural scale,                 (10.1)
```

where the bound depends on the number/geometry of polynomial values rather
than their height `R^4`, and where the actual `r`-dependent B-spline weights
are retained.  Even a proof of (10.1) would still leave the contact.

The theorem which could close R87 must still be centered before the first
absolute-value step:

```text
sum_r omega_r
 [B_(r,off)+B_(r,axis 1)+B_(r,axis 2)-B_(r,origin)]
 =small,                                               (10.2)
```

with the bracket retaining the exact Kloosterman values (R89 (5.2)) and
with its two axis pieces identified with `P_1,P_2` under the original
cofactor/B-spline synthesis.  This is a signed bilinear/trace formula, not a
quadratic large-sieve consequence.  It must be proved before Cauchy erases
the contact sign.

The prime-point and complete-shift obstructions in R86 show that (10.2)
cannot be coefficient-uniform in the native square-root block.  Any proof
must use the complete R71 cofactor weights and its specific B-spline kernel.

## 11. Probe ledger

The exact companion files are

```text
src/varying_prime_discriminant_gate.py
src/test_varying_prime_discriminant_gate.py.            (11.1)
```

They check:

1. `Delta=F(F+4)` for the four-step trace;
2. the absence of nonzero square values `T^2-4` over a large exact integer
   panel;
3. the complete negative-discriminant list `{-3,-4}`;
4. the axis table `X=0,1,2,3,4,5` and its signed squarefree kernels;
5. the matrix classification (3.6) over every residue tuple modulo `11`;
6. both trace-fiber factorizations (5.22) and (5.30);
7. the dot-product and affine-line trace parametrizations;
8. the complete trace-character zero mode (5.13) for seven odd primes;
9. exact squarefree reduction with the ramification mask;
10. the `H^7` versus `H^6` quadratic-large-sieve budget;
11. the trace-large-sieve endpoint `H^6=H^6`;
12. the paired square-kernel norm (4.5);
13. an exact adversarial row-dependent coefficient alignment; and
14. both the exact `Omega(H)` energy example (5.38) and the genuine
    punctured-autocorrelation lower bound (5.39).

These are algebra and exponent-budget tests, not numerical evidence about
zeta zeros.

## 12. Disposition

```text
outer quadratic reciprocity                         EXACT;
nonzero principal trace discriminant                ABSENT;
single-axis special central value                   PAIRED AXIS ONLY;
squarefree-kernel grouping                          EXACT WITH RAMIFICATION;
Heath--Brown varying-r bound                        IMPORTED / NO GAIN AT R71 SCALE;
trace-variable additive large sieve                 EXACT;
nonparabolic trace fiber                             <<H^(2+o(1));
adjacent continuant reduction                        EXACT / SAME ENDPOINT;
number of adjacent-product cells                     H^(2-o(1));
affine-line parametrization multiplicity             H^o(1);
coefficient-uniform trace bound                      NATURAL SCALE / NO POWER;
candidate sharp trace-energy scale                   H^(1+o(1));
lower obstruction to any better scale                Omega(H);
weighted trace-energy improvement (5.40)             OPEN;
Poisson completion in r                             CONDUCTOR TOO LONG;
Burgess in r                                         EXACT FOURTH-ROOT ENDPOINT;
arbitrary r-dependent coefficients                  NO UNIFORM SAVING;
outer L2 diagonal                                    PAIRED KERNEL ENERGY;
coefficient of linear P_1+P_2                       ZERO / NOT GENERATED;
new fixed-power off-axis theorem                    OPEN;
centered signed all-axis theorem                    OPEN / STRIP-STRENGTH;
fixed zeta zero-free strip                          NOT PROVED;
nonexistence of every fixed strip                   NOT PROVED.          (12.1)
```

The varying-prime discriminant was a real survivor: unlike the finite
mod-6 and positive-renewal routes, it exposes a new family of real
characters.  The exact audit shows why the family does not close the proof.
Its first moment has no principal off-axis diagonal, its standard mean
square lives at the `R^4` conductor barrier, and every diagonal created by
squaring is paired.  The missing object remains a genuinely signed
single-axis recombination before Cauchy, with the actual prime/cofactor
B-spline coefficients intact.
