# QP versus a uniform strip: the exact bridge and the missing reverse adapter

**Date:** 2026-08-15

**Verdict:** one implication is rigorous and coefficient-canonical:

```text
uniform zero-free strip of width delta
    ==> positive actual-prime QP-KILL at every power c<delta.       (0.1)
```

The proof uses the smooth von Mangoldt weights themselves, not an abstract
existence argument.  It is uniform on every fixed polynomial aperture,
including

```text
H_Y=[Y^.01,Y^(50/33)].                                 (0.2)
```

Consequently, on the fixed `d=33/50` slice, any strip width

```text
delta>.018746369714728765...                           (0.3)
```

implies a QP kill strong enough to clear the audited carrier bill.

The reverse implication does **not** follow from the Delsarte value as a
support-only statement, even after a node-only selector is allowed to inspect
the complete family of scales.  Finite Dirichlet factors insert arbitrarily
high zeros on any prescribed line `Re(s)=beta`, `0<beta<1`, while preserving
every prime-power frequency location.  One such factor even preserves
strict positivity of every ordinary Dirichlet coefficient.  Every actual-node
Delsarte value and every node-measurable cross-scale selection is therefore
unchanged.  This is a rigorous nonimplication for support-only arguments.  It
does not disprove a coefficient-sensitive theorem special to zeta.

There is a second, independent quantifier no-go.  An explicit nonzero-node
Fejer family has positive probability weights and cosine floor `-1/M` on the
**whole real line**, while its fixed-ordinate cosine transform tends to a
strictly positive sinc square.  Alternating two widths gives incompatible
scale limits.  Thus moving-band QP feasibility, even with positive and
coherent certificates of the right dimension and much better power, cannot
by compactness alone produce the fixed-ordinate input of an explicit-formula
or Landau argument.

For reference, the classical coefficient-sensitive diagnostic is:

```text
zeta has no zero with Re rho>theta
 <==>
for every alpha>theta and every t>0, the continuum-centered
von Mangoldt cosine discrepancy is O_(alpha,t)(x^alpha);             (0.4)
```

and only the **lower** bound in (0.4) is needed for the reverse arrow.  This is
not a QP equivalence.  A non-tautological QP-to-strip reduction is isolated
below: a power comparison between positive-antipode depth and the natural
prime modulus would turn QP power `c` into the high-height strip width
`(lambda*c/A)^2`.  The comparison is false for general node systems and open
for the actual primes.

Nothing in this report proves a strip or an unconditional fixed-power
actual-prime QP bound.

---

## 1. Exact statements

Fix a shell width `w>0`, lower aperture exponent `a>0`, and upper aperture
exponent `A<infinity`.  The project values are

```text
w=1/5,                 a=.01,                A=50/33. (1.1)
```

Take shell centers `Y` to be half-integers, so no integer prime power equals
`Y`.  Let

```text
S_Y={n=p^k: Y exp(-w)<n<Y exp(w)},
u_n=|log(n/Y)|,
H_Y=[Y^a,Y^A].                                         (1.2)
```

Repeated absolute nodes, if any, are merged by adding their coefficients.

### Definition 1.1 (uniform strip)

For `0<delta<=1/2`, write `ZF(delta)` for

```text
zeta(rho)=0, 0<Re(rho)<1  ==>  Re(rho)<=1-delta.       (1.3)
```

### Definition 1.2 (positive actual-node QP kill)

Write `PQP(c)` if, for every sufficiently large allowed `Y`, there is a
positive probability vector `(lambda_n)_(n in S_Y)` such that

```text
P_Y(t)=sum_(n in S_Y)lambda_n cos(tu_n)
      >=-Y^(-c)                       for every t in H_Y. (1.4)
```

This is stronger than the signed Delsarte formulation.  Indeed

```text
Q_Y(t)=1+Y^c P_Y(t)                                   (1.5)
```

is nonnegative on `H_Y` and

```text
Q_Y(0)=1+Y^c.                                         (1.6)
```

Therefore

```text
A_H>=1+Y^c,                 r_+(H_Y)<=Y^(-c).         (1.7)
```

The exact reciprocal relation in (1.7) is the already-proved Delsarte moment
duality.

### Definition 1.3 (exact signed Delsarte kill)

The project QP-KILL statement does not require positive coefficient weights.
Write `DPA(c)` if, for every sufficiently large allowed `Y`, there are real
coefficients `(y_n)` with

```text
sum_(n in S_Y)y_n=1,
inf_(t in H_Y) sum_(n in S_Y)y_n cos(tu_n)>=-Y^(-c).  (1.8)
```

Then

```text
PQP(c) ==> DPA(c) ==> A_H>=1+Y^c ==> r_+(H_Y)<=Y^(-c). (1.9)
```

The first arrow is strict at the level of definitions.  The strip theorem
below proves the stronger `PQP(c)`.  Every reverse no-go below therefore
applies a fortiori to the exact signed statement.

---

## 2. A strip gives canonical positive QP weights

Choose once and for all

```text
h in C_c^infinity((exp(-w),exp(w))),
h>=0,                    integral h(x)dx>0.           (2.1)
```

Put

```text
W_Y=sum_n Lambda(n)h(n/Y),
lambda_n=Lambda(n)h(n/Y)/W_Y.                         (2.2)
```

The vector `(lambda_n)` is supported on actual prime powers in the shell, all
weights are nonnegative, and the weights are independent of the packet set.
Because a function in `C_c^infinity((exp(-w),exp(w)))` vanishes near the two
shell endpoints, this construction need not put positive mass on every node
of `S_Y`; zero coefficients are allowed in Definition 1.2 and in the
Delsarte polynomial.

### Theorem 2.1 (uniform strip implies positive actual-node QP kill)

For every fixed `w,a,A` as above,

```text
ZF(delta)  ==>  PQP(c)             for every 0<c<delta. (2.3)
```

More quantitatively, for each `eta in (0,delta)`, uniformly on `H_Y`,

```text
|sum_n lambda_n exp(-it log(n/Y))|
 <<_(h,delta,eta,a,A) Y^(-delta+eta).                 (2.4)
```

#### Proof

Let

```text
S_Y(t)=sum_n Lambda(n)h(n/Y)n^(-it),
h_tilde(s)=integral_0^infinity h(x)x^(s-1)dx.         (2.5)
```

Mellin inversion gives

```text
S_Y(t)=-(1/(2 pi i)) integral_(Re s=2)
       [zeta'/zeta(s+it)] h_tilde(s)Y^s ds.           (2.6)
```

Fix `eta in (0,delta)` and shift to

```text
sigma_0=1-delta+eta/2.                                (2.7)
```

The strip hypothesis leaves no zero pole to the right of this line.  The
shift crosses only the pole of zeta at `s=1-it`, giving

```text
S_Y(t)=Y^(1-it)h_tilde(1-it)
       -(1/(2 pi i)) integral_(Re s=sigma_0)
        [zeta'/zeta(s+it)]h_tilde(s)Y^s ds.           (2.8)
```

We record the standard log-derivative bound needed here.  On any line a fixed
distance to the right of all zeros,

```text
|zeta'/zeta(sigma_0+iv)|<<_(delta,eta) log(|v|+3).    (2.9)
```

For completeness, the partial-fraction expansion of the completed zeta
function writes the log derivative as the sum of `1/(s-rho)` over zeros with
`|Im(rho)-v|<=1`, plus `O(log(|v|+3))`.  There are
`O(log(|v|+3))` such zeros, and (1.3)--(2.7) put every denominator at horizontal
distance at least `eta/2`.  The pole and bounded-height region are a compact
remainder.  This proves (2.9).

Because `h` is smooth and compactly supported, for every `K`

```text
|h_tilde(sigma+iv)|<<_(h,K)(1+|v|)^(-K)              (2.10)
```

uniformly on bounded horizontal strips.  Hence, for `t<=Y^A`, the line
integral in (2.8) is

```text
<<Y^(1-delta+eta/2) log Y.                            (2.11)
```

At the lower aperture `t>=Y^a`, the pole term satisfies

```text
Y|h_tilde(1-it)|<<_(h,K)Y t^(-K)<=Y^(1-aK).          (2.12)
```

Choose

```text
K>=ceil((delta-eta)/a).                               (2.13)
```

Equations (2.11)--(2.13), with the logarithm absorbed by the spare `eta/2`,
give

```text
|S_Y(t)|<<Y^(1-delta+eta).                            (2.14)
```

The same contour at `t=0` yields

```text
W_Y=Y h_tilde(1)+O(Y^(1-delta+eta))
   asymp_h Y.                                         (2.15)
```

Finally,

```text
sum_n lambda_n exp(-it log(n/Y))
 =Y^(it)S_Y(t)/W_Y,                                  (2.16)
```

so (2.4) follows.  Its real part is the cosine sum in (1.4), because cosine is
even and `u_n=|log(n/Y)|`.

Given `c<delta`, take `eta=(delta-c)/2`.  Then
`delta-eta=(delta+c)/2>c`, so the implied constant in (2.4) is at most the
spare power `Y^(delta-eta-c)` for large `Y`.  This proves (1.4).  QED

### Corollary 2.2 (fixed-slice implication)

The audited fixed-`d=.66` carrier threshold is

```text
kappa_max=.018746369714728765... .                    (2.17)
```

If `ZF(delta)` holds with `delta>kappa_max`, choose

```text
kappa_max<c<delta.                                    (2.18)
```

Then Theorem 2.1 gives `A_H>=1+Y^c`, which is a positive-route QP kill beyond
the complete fixed-slice carrier bill.

This corollary is conditional.  It does not establish `ZF(delta)`.

---

## 3. Why support-only QP cannot imply a strip

The exact Delsarte value

```text
A_H=sup {Q(0):
 Q(t)=1+sum_j lambda_j cos(tu_j)>=0 on H_Y}           (3.1)
```

depends on the node locations `u_j` and on nothing else.  In particular, it
does not see the von Mangoldt coefficients attached to those nodes.

That loss is logically real, not just a missing estimate.

### Theorem 3.1 (support-preserving finite-Euler-factor countermodel)

Fix a prime `p`, `0<beta<1`, and choose `tau>0` outside the countable set

```text
1-2p^(k beta)cos(k tau log p)=0,       k=1,2,... .    (3.2a)
```

Define

```text
E_(beta,tau,p)(s)
 =(1-p^(beta+i tau-s))(1-p^(beta-i tau-s)),
F_(beta,tau,p)(s)=zeta(s)E_(beta,tau,p)(s).           (3.2)
```

Then:

1. `F` has real Dirichlet coefficients and satisfies conjugate symmetry;
2. `F(beta+i tau)=F(beta-i tau)=0`;
3. in the half-plane of absolute convergence, `-F'/F` is supported on exactly
   the same prime powers as `-zeta'/zeta`;
4. only the coefficients at `p^k` change, by

   ```text
   -2 log(p) p^(k beta) cos(k tau log p);              (3.3)
   ```

5. every prime-power node set (1.2), and therefore every value `A_H`, is
   exactly the same for `F` and for zeta.

#### Proof

The two factors in (3.2) are conjugates on the real axis, proving real
coefficients and conjugate symmetry.  Substitution proves the two stated
zeros.  For `Re(s)>1`, expand

```text
-d/ds log(1-p^(beta+i tau-s))
 =-log(p)sum_(k>=1)p^(k(beta+i tau))p^(-ks).          (3.4)
```

Adding the conjugate expansion gives (3.3), supported only at `p^k`.  At
`p^k`, the full coefficient becomes

```text
log(p)[1-2p^(k beta)cos(k tau log p)],                (3.4a)
```

which is nonzero by (3.2a).  Every other prime-power coefficient is unchanged.
Thus multiplication by the finite factor neither deletes nor adds a
prime-power frequency location.  Since (3.1) sees only those locations, its
value is unchanged.  QED

Choose `beta>1-delta`; the exceptional ordinates in (3.2a) are countable, so
an admissible `tau` exists in every open height interval.  Then `F` violates
the width-`delta` strip while having identical QP/Delsarte data.  Therefore

```text
support-only A_H bound  ==>  zero-free strip          (3.5)
```

is false in the natural class of Dirichlet series obtained by finite Euler
modification.

The coefficient scope can be made sharper than Theorem 3.1.

### Theorem 3.2 (the countermodel may have positive Dirichlet coefficients)

Fix a prime `p` and `0<beta<1`, and put

```text
E^+_(beta,p)(s)=1+p^(beta-s),
F^+_(beta,p)(s)=zeta(s)E^+_(beta,p)(s).                (3.6)
```

Then:

1. every ordinary Dirichlet coefficient of `F^+` is strictly positive;
2. `F^+` has zeros

   ```text
   beta +/- i(2k+1)pi/log(p),             k=0,1,...; (3.7)
   ```

3. `-F^{+prime}/F^+` is supported at exactly the same prime powers as
   `-zeta'/zeta`;
4. hence the complete family of actual-node QP instances is identical for
   `F^+` and zeta.

#### Proof

Multiplying the Dirichlet series of zeta by `1+p^beta p^(-s)` gives

```text
a_n(F^+)=1+p^beta 1_(p divides n)>0.                  (3.8)
```

Equation (3.7) follows by setting `p^(beta-s)=-1`.  In `Re(s)>1`,

```text
-F^{+prime}/F^+
 =-zeta'/zeta
   +log(p)sum_(j>=1)(-1)^(j-1)p^(j beta)p^(-js).      (3.9)
```

Thus the full coefficient at `p^j` is

```text
log(p)[1+(-1)^(j-1)p^(j beta)],                      (3.10)
```

which never vanishes because `beta>0`; every other prime-power coefficient is
unchanged.  This proves all four claims.  QED

### Corollary 3.3 (all-scale node selectors still cannot see the zeros)

Let a rule inspect the **entire** family of prime-power node sets, all shell
centres, all apertures, and all resulting values `A_H`, and from that data
select any family of Delsarte coefficients.  The rule has exactly the same
input, and hence exactly the same output, for zeta and `F^+`.  Nevertheless
`F^+` has the arbitrarily high zeros (3.7).  Therefore no node-measurable
cross-scale canonicalization, by itself, can imply a strip in any function
class containing both examples.

This corollary closes the proposed repair by **scale coherence alone**.  It
does not close a repair which injects the numerical von Mangoldt coefficients,
the exact local Euler factors, or zeta's functional equation.

### Scope

Neither countermodel is zeta: its local factor at `p` differs, and neither is
asserted to satisfy zeta's functional equation.  Theorem 3.2 shows that mere
positivity of ordinary Dirichlet coefficients does not repair this.  Thus the
examples do not falsify the literal material implication between two
statements about the one fixed zeta function.  They prove the precise theorem
actually claimed here: coefficient input beyond the complete node family is
indispensable.  No manipulation of `A_H`, including a multiscale selection,
can by itself recover a strip.

---

## 4. The polarity-correct strip equivalence

The exact coefficient-sensitive replacement for QP is a centered von
Mangoldt discrepancy.

For `t>0`, define

```text
C_t(x)=Re[x^(1-it)/(1-it)],
D_t(x)=sum_(n<=x)Lambda(n)cos(t log n)-C_t(x).        (4.1)
```

The centering is forced:

```text
C_t'(x)=cos(t log x).                                 (4.2)
```

Without `C_t`, the shifted pole of zeta produces oscillations of order `x/t`,
so a global inverse-power one-sided bound would be impossible even under RH.

### Theorem 4.1 (uniform strip iff centered twist bounds)

Fix `1/2<=theta<1`.  The following are equivalent:

1. every nontrivial zeta zero satisfies `Re(rho)<=theta`;
2. for every `alpha>theta` and every fixed `t>0`,

   ```text
   D_t(x)=O_(alpha,t)(x^alpha);                        (4.3)
   ```

3. for every `alpha>theta` and every fixed `t>0`, there are constants
   `C_(alpha,t),x_(alpha,t)` such that

   ```text
   D_t(x)>=-C_(alpha,t)x^alpha
                       for every x>=x_(alpha,t).      (4.4)
   ```

Thus a one-sided lower estimate suffices for the difficult reverse arrow.

#### Proof that 1 implies 2

The truncated explicit formula for the von Mangoldt sum is

```text
psi(x)=x-sum_(|Im rho|<=T)x^rho/rho
       +O(x log^2(xT)/T+log^2(xT)),                  (4.5a)
```

with the standard half-weight convention at a jump (changing that convention
costs only `O(log x)`).  Also

```text
sum_(|Im rho|<=T)1/(|rho|+1)<<log^2(T+3),             (4.5b)
```

by the Riemann--von Mangoldt local count.  Under statement 1, choose for
example `T=x^2`.  Then, for every `alpha>theta`, the logarithms in
`x^theta log^2 x` are absorbed by the spare power and

```text
psi(x)=sum_(n<=x)Lambda(n)=x+O_alpha(x^alpha).         (4.5)
```

Write `psi(x)=x+E(x)` in partial summation:

```text
sum_(n<=x)Lambda(n)n^(-it)
 =x^(-it)psi(x)+it integral_1^x psi(u)u^(-it-1)du.   (4.6)
```

The contribution of `psi(u)=u` is

```text
x^(1-it)/(1-it)+O_t(1),                              (4.7)
```

and (4.5) makes the contribution of `E` `O_(alpha,t)(x^alpha)`.
Taking real parts proves (4.3).

#### Proof that 2 implies 3

Immediate.

#### Proof that 3 implies 1

Suppose instead that `rho=beta+it` is a zero with `beta>theta`.  Choose

```text
theta<alpha<beta.                                    (4.8)
```

Among zeros at ordinate `t` with real part at least `beta`, choose one with
largest real part `beta_*`; the relevant horizontal segment is compact and
contains finitely many zeros.  Put

```text
F_t(s)=sum_n Lambda(n)cos(t log n)n^(-s)
 =-1/2[zeta'/zeta(s-it)+zeta'/zeta(s+it)].           (4.9)
```

If the zero at `beta_*+it` has multiplicity `m`, then `F_t` has at the real
point `beta_*` residue `-m`: the two conjugate logarithmic derivatives each
contribute `-m/2`.

The Mellin transform of the continuum term is

```text
J_t(s)=1/[2(1+it)(s-1-it)]
      +1/[2(1-it)(s-1+it)].                          (4.10)
```

At `s=1+it` and `s=1-it`, the residues of `F_t(s)/s` are respectively

```text
1/[2(1+it)],               1/[2(1-it)],              (4.11)
```

so (4.10) cancels the pole carrier exactly.

By (4.4),

```text
G(x)=D_t(x)+C_(alpha,t)x^alpha>=0                    (4.12)
```

eventually.  Its Mellin transform is, initially for `Re(s)>1`,

```text
M(s)=F_t(s)/s-J_t(s)
    +C_(alpha,t)x_0^(alpha-s)/(s-alpha)+E_0(s),      (4.13)
```

where `E_0` is entire.  The nonreal pole carriers cancel by (4.10)--(4.11),
while at `s=beta_*`, (4.13) has the negative residue

```text
-m/beta_*<0.                                         (4.14)
```

Apply the elementary Landau lemma for a nonnegative Mellin transform.  Its
real abscissa of convergence is a singularity; this follows by expanding at a
point to the right and using Tonelli on the nonnegative logarithmic moments.
If the abscissa is `-infinity`, the transform is entire, contradicting (4.14).
If it is greater than `beta_*`, (4.13) is analytic at the abscissa, also a
contradiction.  If it is smaller than `beta_*`, the defining integral is
analytic through the pole.  Hence it would have to equal `beta_*`.  But the
integral is nonnegative immediately to the right, whereas the negative pole
in (4.14) tends to `-infinity`.  This is the final contradiction.  QED

---

## 5. Exact logical map

The two proved arrows and the failed support-only arrow are

```text
                         Theorem 2.1
uniform strip --------------------------------> natural positive QP
     |                                                |
     | Theorem 4.1                                    | forget coefficients,
     v                                                | fixed ordinates, and
centered von Mangoldt discrepancy                     | cross-scale coherence
     ^                                                v
     +----------------------------------------- arbitrary Delsarte A_H
             reverse adapter NOT PROVIDED             (5.1)
```

The exact QP statement loses four things needed by Theorem 4.1:

1. **coefficients:** QP chooses arbitrary signed Delsarte coefficients,
   whereas (4.1) uses the fixed von Mangoldt coefficients;
2. **scale coherence:** QP may choose unrelated coefficients at every `Y`;
3. **ordinate quantifier:** `t>=Y^.01` means a fixed `t` eventually leaves the
   QP band, while Theorem 4.1 needs every fixed ordinate through `x->infinity`;
4. **pole centering:** QP has no requirement matching the exact continuum
   term `C_t(x)`.

The finite-factor theorem proves that item 1 cannot be recovered from node
support, even if all scales are supplied simultaneously.  The following
exact family separates the moving-band and fixed-ordinate quantifiers without
using an `L`-function.

### Theorem 5.1 (finite Fejer moving-band countermodel)

Fix `w>0` and an integer `m>=2`.  On the `M=m-1` distinct nonzero nodes

```text
u_j=jw/(m-1),                         1<=j<=m-1,      (5.2)
```

put the positive probability weights

```text
lambda_j=2(m-j)/[m(m-1)].                            (5.3)
```

Then, for every real `t`,

```text
P_m(t)=sum_(j=1)^(m-1)lambda_j cos(tu_j)
      =[m F_m(wt/(m-1))-1]/(m-1)>=-1/(m-1),          (5.4)

F_m(x)=m^(-2)|sum_(r=0)^(m-1)exp(irx)|^2>=0.         (5.5)
```

The floor is attained whenever `wt/(m-1)=2 pi l/m` with `m` not dividing
`l`.  On the other hand, at every fixed `t`,

```text
lim_(m->infinity)P_m(t)
  =[sin(wt/2)/(wt/2)]^2.                             (5.6)
```

#### Proof

The weights in (5.3) are positive and sum to one.  Expanding the square in
(5.5) gives

```text
F_m(x)=1/m+sum_(j=1)^(m-1)2(m-j)m^(-2)cos(jx),       (5.7)
```

which is exactly (5.4).  The geometric sum in (5.5) vanishes at the stated
phases, proving sharpness.  Finally, with `x=wt/(m-1)`, the normalized
geometric sum is a Riemann sum for `integral_0^1 exp(iwtr)dr`; taking its
squared modulus proves (5.6).  QED

Take `m(Y)-1 asymp Y/log Y`, the same cardinality order as a prime shell.  For
every fixed `c<1`, (5.4) gives the analogue of `PQP(c)` for this node family on
`[Y^.01,Y^(50/33)]` for all large `Y`--indeed on the whole real line.  Yet at
`t=1` and `w=1/5`, (5.6) is greater than `.99`, not zero.  The certificates
already converge weakly to one fixed triangular law, so adding subsequential
compactness or a coherent choice does not fix the ordinate mismatch.
Alternating two values of `w` gives two distinct fixed-ordinate subsequential
limits while retaining the same global floor.

The family also separates an arbitrary QP certificate from designated
"natural" weights.  Put the designated probability at any one node.  Its
Fourier modulus is identically one, while (5.4) gives
`r_+<=1/(m-1)`.  Hence no universal comparison

```text
natural modulus <= C r_+^lambda,        lambda>0,     (5.8)
```

can follow from finite-dimensional Delsarte geometry, positivity, aperture,
cardinality, or scale coherence.  An actual-prime version of (5.8), if true,
must be genuinely arithmetic.

Items 2--4 in the list above are therefore not removable by an abstract
compactness argument.

Accordingly, the strongest valid conclusion is

```text
uniform strip ==> actual-node QP-KILL;                PROVED;
actual-node A_H ==> uniform strip, support-only;      FALSE;
actual zeta QP + new coefficient/scale adapter
                          ==> uniform strip;          CONDITIONAL / OPEN;
centered canonical discrepancy <=> uniform strip;    PROVED.           (5.9)
```

There is no audited `QP <=> strip` theorem without the new adapter.

---

## 6. Strongest non-tautological conditional QP equivalence

The missing adapter can be stated as one concrete extremal comparison.  Put

```text
L_N=sup N^(-1)|sum_(N1<=p<=N2)p^(-it)|,              (6.1)
```

where the supremum is over

```text
N<=N1<N2<=2N,              N^(1/2)<=|t|<=N^A,        (6.2)
```

and put

```text
R_N=sup {r_+(H_Y): N/3<=Y<=3N, Y an allowed centre}.(6.3)
```

For `lambda>0`, call the following the canonical comparison:

```text
COMP(lambda):       L_N<=C R_N^lambda
                    for every sufficiently large N. (6.4)
```

This is coefficient-sensitive: the left side uses the actual primes with
their canonical unit coefficients, while the right side is the node-only QP
extremal.  It is not a restatement of the centered discrepancy theorem.

### Theorem 6.1 (conditional fixed-power equivalence)

Assume `COMP(lambda)` for some fixed `lambda>0`.

1. `ZF(delta)` implies `DPA(c)` for every `0<c<delta`.
2. If `DPA(c)` holds and `lambda*c<=.019`, then zeta has no zeros at all
   sufficiently large heights in

   ```text
   Re(s)>1-(lambda*c/A)^2,             A=50/33.       (6.5)
   ```

3. Consequently, under `COMP(lambda)`, existence of **some** fixed-power
   actual-node Delsarte kill is equivalent to existence of **some** global
   fixed zero-free strip.  To retain the exact width in (6.5) globally, one
   additionally checks the bounded-height region at that width.

#### Proof

Part 1 is Theorem 2.1 and `PQP(c)=>DPA(c)`.  Under `DPA(c)`, moment duality
gives `r_+(H_Y)<=Y^(-c)`, so (6.3)--(6.4) give

```text
L_N<<N^(-lambda*c).                                  (6.6)
```

The audited Turan localization theorem for the aperture (6.2) turns the
natural prime saving `lambda*c` into the high-height strip (6.5).  This proves
Part 2.  For Part 3, the forward implication is Part 1.  The reverse gives a
high-height fixed strip; the zero-free line `Re(s)=1` and discreteness leave a
positive (possibly smaller) width on the remaining compact height range.
QED

With no comparison loss, `lambda=1`, and the project value `c=.019`, (6.5)
has width

```text
(.019/(50/33))^2=.0001572516.                         (6.7)
```

Theorem 5.1 proves that `COMP(lambda)` is false as a general selection lemma.
Theorems 3.1--3.2 prove that no rule based only on the complete actual node
family can establish it across a natural finite-factor class.  For zeta
itself, (6.4) is an exact, sharply scoped open arithmetic bridge.  Proving it
would be substantive enough to turn QP into a strip.  QP alone does not
verify (6.4), so this reduction cannot be invoked from QP alone.

---

## 7. Replay

Executable artifacts:

- `src/qp_strip_bridge.py`;
- `src/test_qp_strip_bridge.py`;
- `results/verify_zeta23_qp_strip_bridge.py`.

They verify the fixed-slice exponent placement, lower-aperture Mellin decay,
exact continuum derivative and pole cancellation, hostile zero residue, both
support-preserving finite factors, the exact nonzero Fejer floor and its
fixed-ordinate limit, and the conditional Turan exponent.
