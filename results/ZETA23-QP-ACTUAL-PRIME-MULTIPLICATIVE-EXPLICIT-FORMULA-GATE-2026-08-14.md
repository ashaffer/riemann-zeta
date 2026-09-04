# QP actual-prime multiplicative gate: exact rank tax and strip boundary

**Date:** 2026-08-14
**Verdict:** the actual-prime Delsarte value remains **open**.  The natural
multiplicative-function route does not presently prove the needed fixed-power
one-sided antenna.  Its exact failure can now be stated more sharply than
“KMT gives only a logarithm.”

There are three definitive conclusions.

1. Klurman--Mangerel--Teravainen has more than enough height: its primary
   statement uses

   ```text
   X=x^((log x)^(1/25)),                              (0.1)
   ```

   and therefore covers `2Y^(50/33)`.  But its normalized scalar saving is
   only `delta_KMT=(log Y)^(-.3+o(1))`.

2. At the Guth--Maynard packet count `R=Y^(2c+o(1))`, scalar prime-twist
   bounds plus even an **ideal** unprojected Gram estimate control the carrier
   only through

   ```text
   h_T <= R delta_KMT^2/gamma.                        (0.2)
   ```

   The sharp threshold is `delta<<R^(-1/2)=Y^(-c)`.  For `c=.019`,

   ```text
   delta_KMT sqrt(R)
      =Y^.019/(log Y)^.3 -> infinity.                 (0.3)
   ```

   Thus KMT scalar estimates cannot be combined with a Gram lower bound to
   prove the adaptive carrier-source gap.  This threshold is not an artifact:
   an exact sign model has `H=I`, all means `-R^(-1/2)`, and carrier leverage
   one.

3. A hypothetical fixed-power **modulus** upgrade for the natural sharp prime
   twist throughout the QP band would already prove a fixed zero-free strip by
   Turan localization.  A conservative top-aperture specialization says that
   if

   ```text
   |sum_(N1<=p<=N2) p^(-it)| << N^(1-c)               (0.4)
   ```

   uniformly for `N<=N1<N2<=2N` already on the high sub-band
   `N^.5<=|t|<=N^(50/33)`, then at all sufficiently large heights

   ```text
   zeta(s)!=0 when
   Re(s)>1-(33c/50)^2.                                (0.5)
   ```

   At `c=.019`, the width is exactly

   ```text
   (33*.019/50)^2=.0001572516.                        (0.6)
   ```

This is a fail-fast boundary, not a solution.  Formula (0.5) is an explicit
consequence, not the optimization over every placement of Turan's prime
lengths in the full band.  It concerns the natural modulus theorem (0.4), not
the adaptive signed Delsarte coefficients.
The exact Delsarte theorem may be weaker and is not proved equivalent to a
strip here.

---

## 1. The actual surviving QP statement

Let the prescribed nonzero prime-power nodes be

```text
u_j=|log(n_j/Y)|<=1/5,
a(t)=(cos(tu_j))_(j<=M),
H_Y=[Y^.01,Y^(50/33)].                                (1.1)
```

The exact one-sided Delsarte value is

```text
A_H=sup {Q(0):
 Q(t)=1+sum_j lambda_j cos(tu_j)>=0 for all t in H_Y}.(1.2)
```

The already-proved compact moment duality says

```text
r_+(H_Y)=1/(A_H-1).                                   (1.3)
```

On the fixed `d=33/50` slice, a convenient kill target is

```text
A_H>=1+Y^.019,                                        (1.4)
```

equivalently a normalized dual whose positive error is at most `Y^-.019`.
The coefficients in (1.2) may be signed and may depend on the complete actual
node set.  This quantifier is why the strip reductions below are deliberately
restricted to the natural-weight subroute.

---

## 2. What KMT actually supplies

Klurman--Mangerel--Teravainen,
[*Multiplicative functions in short arithmetic progressions*](https://arxiv.org/abs/1909.12280),
Lemma `pls_hyb` (printed Lemma 7.9), states for a fixed smooth cutoff `h`, a
character of conductor at most `x^epsilon`, and `|t|<=X` with (0.1),

```text
|sum_n Lambda(n)chi(n)n^(-it)h(n/x)|
 <<_h epsilon log^3(1/epsilon)x
      +x/(log x)^.3+x/(t^2+1).                       (2.1)
```

The immediately following remark permits a sharp cutoff if the final term is
replaced by `x/(|t|+1)`.  The outer exponent on `x` in (0.1) is present in the
arXiv TeX.  Consequently

```text
2Y^(50/33)<Y^((log Y)^(1/25))                         (2.2)
```

for all sufficiently large `Y`.  Height is not the obstruction.

After choosing `epsilon` at its permitted logarithmic scale and normalizing by
the prime mass, (2.1) gives schematically

```text
|Phi_Y(t)|<<delta_KMT,
delta_KMT=(log Y)^(-.3+o(1)),                         (2.3)
```

through the QP band for the natural smooth von-Mangoldt measure.  This is
enough for the already-recorded one-packet variance repair.  It is not an
inverse-polynomial antenna.

### Important scope

The KMT theorem is scalar and coefficient-specific.  It estimates one
von-Mangoldt/character twist.  An adaptive packet field

```text
F_c(u)=sum_(i<=R)c_i exp(i t_i u)                     (2.4)
```

is a linear combination of multiplicative twists, not one multiplicative
function.  In general

```text
F_c(log(mn/Y)) != F_c(log(m/Y))F_c(log(n/Y)).         (2.5)
```

Likewise `|F_c|^2` is not multiplicative.  The pretentious distance introduced
by [Granville--Soundararajan](https://arxiv.org/abs/math/0608407) therefore
does not accept the adaptive weight as a scalar multiplicative input.  Applying
KMT to its individual twists is legal, but pays the coefficient norms computed
below.

No claim is made that a future vector-valued or coefficient-specific theorem
is impossible.  The claim is that the checked scalar primary theorem does not
contain the adaptive quantifier.

---

## 3. Exact carrier-source threshold

Let `mu` be any probability on the actual nodes and let

```text
b_i(u)=cos(t_i u),
m_i=E_mu b_i,
H_ij=E_mu b_i b_j.                                   (3.1)
```

The carrier leverage of the span is

```text
h=m^T H^(-1)m                                         (3.2)
```

when `H` is invertible.  This is the weighted version of the projection
quantity `h_T` in the companion projected-Gram report.

### Proposition 3.1 (scalar-to-source rank tax)

If

```text
|m_i|<=delta              for every i,
H>=gamma I_R,             gamma>0,                   (3.3)
```

then

```text
h<=R delta^2/gamma.                                  (3.4)
```

#### Proof

The Gram hypothesis gives `H^(-1)<=gamma^(-1)I`, while
`||m||_2^2<=Rdelta^2`.  Insert these two inequalities into (3.2).  QED

Even under the optimistic constant conditioning `gamma~1`, a constant carrier
gap follows from this information only at

```text
delta<=sqrt((1-eta)/R).                               (3.5)
```

The large-value packet count at threshold `Y^-c` is

```text
R<=Y^(2c+o(1)).                                      (3.6)
```

Thus (3.5) asks for

```text
delta<=Y^(-c+o(1)).                                  (3.7)
```

For `c=.019`, KMT instead gives (0.3).  The formal upper bound (3.4) becomes
larger than one and says nothing.

### Proposition 3.2 (the threshold is sharp from these data)

Let `s` be even, `R=s^2`, and let `mu` be uniform on all sign vectors

```text
x in {-1,1}^R,             sum_i x_i=-s.             (3.8)
```

Then

```text
E x_i=-1/s=-R^(-1/2),
E x_i x_j=delta_ij,
1=-(1/s)sum_i x_i             pointwise.             (3.9)
```

Hence `H=I_R`, while the constant carrier lies in the packet span and

```text
h=1.                                                 (3.10)
```

The off-diagonal identity in (3.9) follows from exchangeability and

```text
0=E[(sum_i x_i)^2]-s^2
 =R+R(R-1)E[x_1x_2]-R.                               (3.11)
```

This is an abstract bounded-entry model, not an actual-prime model.  Its exact
logical content is that **scalar means plus an ideal unprojected Gram cannot
beat the `R^-1/2` threshold**.  Additional actual-prime source correlation is
mandatory.

---

## 4. Adaptive covariance and positive square reweighting

Let `mu` be a base probability with characteristic function

```text
Phi(v)=integral exp(ivu)dmu(u).                       (4.1)
```

Take

```text
C(u)=sum_(r<=S)c_r exp(i s_r u),
h(u)=|C(u)|^2>=0.                                    (4.2)
```

The reweighted characteristic function is exactly

```text
Phi_h(t)=
 [sum_(r,q)c_r conjugate(c_q)Phi(t+s_r-s_q)]
 /[sum_(r,q)c_r conjugate(c_q)Phi(s_r-s_q)].         (4.3)
```

This is the difference-kernel identity from the positive-weight audit.  It
also gives an exact black-box cost for KMT.

Define the effective rank

```text
K(c)=||c||_1^2/||c||_2^2,             1<=K(c)<=S.    (4.4)
```

### Proposition 4.1 (termwise scalar-estimate tax)

Optimistically suppose every nonzero frequency occurring in (4.3) satisfies

```text
|Phi(v)|<=delta.                                      (4.5)
```

If `delta[K(c)-1]<1`, then termwise estimation gives

```text
|Phi_h(t)|
 <=delta K(c)/{1-delta[K(c)-1]}.                     (4.6)
```

#### Proof

The diagonal of the denominator is `||c||_2^2`.  Its off-diagonal part has
absolute value at most

```text
delta[||c||_1^2-||c||_2^2].                          (4.7)
```

The numerator is at most `delta||c||_1^2`.  Divide the two estimates.  QED

Actual KMT is weaker than the optimistic hypothesis (4.5): close differences
`s_r-s_q` may lie below the high band, and translated frequencies can require
`2B`.  The latter is within (0.1), but the former carries the nondecaying
`1/(1+v^2)` term.  Even after granting (4.5), (4.6) has two consequences:

```text
normalization controlled by scalar KMT only if
 K(c)=o((log Y)^.3);                                  (4.8)

a Y^-c off-packet bound cannot follow from the
termwise KMT bound even at K(c)=1, since
(log Y)^-.3 >> Y^-c.                                 (4.9)
```

Thus a positive square tilt can still work only by using the **signed actual
covariances** in (4.3), not by inserting KMT absolute values.  Those adaptive
covariances are precisely the unproved source/off-packet theorem.

For the ordinary packet Gram, the same entrywise logic is even more expensive.
If every covariance entry has error at most `delta`, its operator error can be
`Rdelta`.  Preserving a constant spectral gap by Gershgorin would require

```text
delta=o(1/R)=Y^(-2c+o(1)),                            (4.10)
```

and actual close packet differences do not satisfy the premise.  This does
not rule out Toeplitz structure or a directional source theorem.  It rules out
the proposed scalar-entrywise black-box deduction.

---

## 5. One-sided global natural twists are strip-strength

There is also a polarity-correct explicit-formula boundary.  It needs a real
one-sided Tauberian argument; naive Abel continuation would be invalid because
a lower bound alone does not make the positive part of a summatory function
integrable below `Re(s)=1`.

For fixed `t>0`, put

```text
A_t(x)=sum_(n<=x)Lambda(n)cos(t log n).               (5.1)
```

### Theorem 5.1 (one-sided Landau obstruction at a matching ordinate)

If for some `theta<1`, `C>0`, and `x_0`,

```text
A_t(x)>=-C x^theta             for every x>=x_0,     (5.2)
```

then zeta has no zero `rho=beta+it` with `beta>theta`.

#### Proof

For `Re(s)>1`, partial summation gives

```text
F_t(s)=sum_n Lambda(n)cos(t log n)n^(-s)
 =-1/2[zeta'/zeta(s-it)+zeta'/zeta(s+it)].           (5.3)
```

Assume a zero `beta+it` with `beta>theta` exists.  Among the zeros at ordinate
`t` with real part at least `beta`, let `beta_*` be the largest real part.
This is a finite set in the compact horizontal segment `[beta,1]+it`, so the
maximum exists.  The conjugate zero occurs at ordinate `-t`.  If the total
multiplicity at `beta_*+it` is `m`, then (5.3) has at the real point
`s=beta_*` residue

```text
Res F_t(s)=-m.                                        (5.4)
```

There is no cancellation in (5.4): the two conjugate logarithmic derivatives
each contribute `-m/2`.  The shifted pole of zeta is nonreal because `t>0`,
and the other terms are analytic at this rightmost real point.

Now set `G(x)=A_t(x)+Cx^theta>=0` for `x>=x_0` and consider its Mellin
transform

```text
M(s)=integral_(x_0)^infinity G(x)x^(-s-1)dx.         (5.5)
```

For `Re(s)>1`, (5.3) and partial summation give

```text
M(s)=F_t(s)/s+C x_0^(theta-s)/(s-theta)+E(s),        (5.6)
```

where `E` is entire.  In particular, the meromorphic continuation of `M` has
at `beta_*` the negative residue

```text
-m/beta_*<0.                                         (5.7)
```

We use the elementary Landau lemma for Mellin transforms: if `G>=0` and its
Mellin transform has finite real abscissa of convergence `sigma_c`, then
`sigma_c` is a singularity.  For completeness, if the transform were analytic
across `sigma_c`, expand it about `sigma_0>sigma_c`.  Its derivatives are the
nonnegative moments

```text
(-1)^k M^(k)(sigma_0)
 =integral G(x)(log x)^k x^(-sigma_0-1)dx.           (5.8)
```

Tonelli then identifies the Taylor series at a point left of `sigma_c` with
the supposedly divergent Mellin integral, a contradiction.

Here `G(x)=O(x log x)`, so `sigma_c<=1`.  If `sigma_c=-infinity`, the
nonnegative integral (5.5) converges absolutely on every vertical line and
defines an entire function, immediately contradicting (5.7).  Otherwise
`sigma_c` is finite and the Landau lemma applies.  If `sigma_c>beta_*`, (5.6)
is analytic at `sigma_c`, contradicting the Landau
lemma.  If `sigma_c<beta_*`, the integral defines an analytic function through
`beta_*`, contradicting (5.7).  Hence `sigma_c=beta_*`.  But for real
`sigma>beta_*`, (5.5) is nonnegative, whereas (5.6)--(5.7) tends to `-infinity`
as `sigma` decreases to `beta_*`.  This final contradiction proves the
theorem.  QED

### Scope of Theorem 5.1

The theorem is global in the summation scale `x` at one fixed ordinate `t`.
The QP antenna is a centered fixed shell and is required only while

```text
Y^.01<=t<=Y^(50/33).                                  (5.9)
```

For fixed `t`, (5.9) permits only a finite range of `Y`.  Therefore Theorem
5.1 does **not** prove that the finite-aperture adaptive Delsarte problem is
equivalent to a strip.  It proves exactly that a global one-sided natural
von-Mangoldt replacement is not a cheap lemma.

---

## 6. Finite polynomial aperture: an explicit Turan exponent

The modulus version admits a finite-height statement with the precise QP
aperture.  Weber's primary paper
[*Local Suprema of Dirichlet Polynomials and Zerofree Regions of the Riemann Zeta-Function*](https://arxiv.org/abs/1005.3932)
reproduces the needed Turan localization criterion.

In its notation, fix for example `E=1/2`.  If for

```text
T-T^E<=tau<=T+T^E,                  0<E<=9/10,
T^(D(1-beta^(1/6)))<=N<=N1<N2<=2N
                    <=T^(D(1+beta^(1/6)))            (6.1)
```

one has

```text
|sum_(N1<=p<=N2)p^(-i tau)|
 <=c_Tur N log^10(N)/tau^beta,                        (6.2)
```

where `c_Tur` is the fixed numerical constant required by the criterion, then

```text
zeta(s)!=0 for Re(s)>1-beta^2,
T-T^E<=Im(s)<=T+T^E.                                 (6.3)
```

### Theorem 6.1 (QP-band modulus estimate implies a strip)

Put

```text
A=50/33.                                                (6.4)
```

Assume that for some fixed `0<c<=.019`, all sufficiently large `N`, every
`N<=N1<N2<=2N`, and every `tau` with

```text
N^(1/2)<=|tau|<=N^A,                                  (6.5)
```

the fixed-power natural prime estimate (0.4) holds.  Then zeta has no zeros,
at all sufficiently large heights, in the fixed open strip

```text
Re(s)>1-(c/A)^2.                                      (6.6)
```

#### Proof

Fix any

```text
0<beta<c/A,
r=beta^(1/6).                                         (6.7)
```

Choose a small `eta>0` and set

```text
D=(1+eta)/[A(1-r)].                                   (6.8)
```

For every length in (6.1), the shortest length has top QP height

```text
[T^(D(1-r))]^A=T^(1+eta),                            (6.9)
```

which contains `T+T^E` for large `T`.  At the longest length the lower edge
of the chosen half-power sub-band has exponent

```text
(1/2)D(1+r)
 ={(1+eta)(1+r)}/{2A(1-r)}<1.                        (6.10)
```

For every `beta<c/A` at the fixed-slice value this inequality has a uniform
margin; with the displayed replay slack its limiting value is below `.946`.
Thus (6.1) lies
inside the high QP sub-band (6.5).

At the shortest permitted length, hypothesis (0.4) gives the relative saving

```text
N^-c<=T^[-cD(1-r)]
     =T^[-c(1+eta)/A].                               (6.11)
```

Since `beta<c/A`, choose `eta` small and then `T` large.  The spare power in
(6.11) absorbs the implied constant in (0.4) relative to the fixed numerical
`c_Tur` (the `log^10 N` factor only enlarges the permitted right side).  Turan's
criterion proves (6.3).  Letting `beta` increase to `c/A` proves the open strip
(6.6).  QED

At the QP value `c=.019`,

```text
c/A=.019*(33/50)=.01254,
(c/A)^2=.0001572516.                                 (6.12)
```

This is a finite-aperture no-shortcut theorem for the natural **modulus**
route, with an exact exponent for the displayed top-aperture specialization.
It is deliberately not optimized over the lower part of the band.  The
half-power edge avoids the elementary continuous pole term that makes a sharp
modulus target near `N^.01` unlike the one-sided QP target.  The theorem does
not apply to a one-sided centered shell bound or arbitrary adaptive Delsarte
coefficients.

---

## 7. Selberg and Beurling positive weights

### Small-divisor Selberg squares are constant on the active primes

Consider the standard nonnegative divisor square

```text
w_D(n)=|sum_(d|n,d<=D)lambda_d|^2.                    (7.1)
```

If

```text
D<Y exp(-1/5),                                        (7.2)
```

then every prime `p` in the active shell has no divisor `d<=D` except one.
Therefore

```text
w_D(p)=|lambda_1|^2                                  (7.3)
```

for every active prime.  Such a Selberg square cannot adapt the prime-node
weights at all.  Variation on prime powers does not change this statement on
the dominant prime subcollection.  To distinguish active primes by the same
divisibility mechanism one must take `D` to prime scale, where the ordinary
small-divisor sieve evaluation no longer supplies a free estimate.

This is narrowly scoped: a positive weight using the numerical value of `p`,
an external oscillatory factor, or a full-level optimization is not a
small-divisor square and is not ruled out.

### Beurling--Selberg extremals choose a continuum spectrum

The classical Beurling--Selberg problem, and for example the primary Gaussian
subordination theorems of
[Carneiro--Littmann--Vaaler](https://arxiv.org/abs/1008.4969), construct entire
majorants/minorants of prescribed exponential type and compactly supported
Fourier transforms.  They do not assert that the Fourier spectrum can be
moved onto the prescribed finite set

```text
{log(p^k/Y): p^k in the actual shell}.                (7.4)
```

Moving a continuum extremizer to (7.4) while retaining pointwise positivity
through `Y^(50/33)` is the missing actual-prime quadrature/Delsarte theorem.
If positivity is preserved instead by a square multiplier, the exact formula
is (4.3), and the scalar KMT rank tax returns.

Accordingly, no checked Selberg or Beurling theorem supplies the adaptive
fixed-power source covariance.

---

## 8. Binary disposition

```text
KMT height through B=Y^(50/33):                     YES;
KMT scalar fixed-power saving:                       NO;
KMT input multiplicative after adaptive packet sum: NO;
scalar KMT + even ideal Gram gives carrier gap:      NO, sharp rank tax;
one natural-base packet repair:                     YES (prior report);
R=Y^.038 simultaneous adaptive source control:       OPEN;
square reweight via termwise KMT:                    CLOSED;
global one-sided sharp Lambda bound at power theta:  STRIP-STRENGTH;
finite QP-band natural modulus bound at power c:     STRIP-STRENGTH;
small-divisor Selberg square adapts active primes:    NO;
continuum Beurling extremal transfers to prime logs: NOT PROVIDED;
actual-prime Delsarte value A_H:                     OPEN;
QP-KILL, QP-PROMOTE, or a zero-free strip:           NOT PROVED.        (8.1)
```

The exact survivor is not another scalar prime exponential sum.  It is a
coefficient-sensitive theorem for the actual adaptive source:

```text
no sparse packet combination can approximate the carrier on all
actual shell primes, and its completed residual remains one-sided
on every off-packet query.                            (8.2)
```

KMT controls each original twist but loses the packet dimension; Turan shows
that simply replacing it by a uniform natural fixed-power modulus estimate
would already prove a strip.  Any successful route must therefore exploit the
direction of the actual adaptive source, not just improve a scalar absolute
value estimate mechanically.

Executable replay:

- `src/qp_actual_multiplicative_gate.py`;
- `src/test_qp_actual_multiplicative_gate.py`;
- `results/verify_zeta23_qp_actual_multiplicative_gate.py`.
