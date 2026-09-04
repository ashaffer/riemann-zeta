# QP-to-zeta reverse bridge: phase localization is solved, radialization is not

**Date:** 2026-08-15

**Verdict:** the exact zero contrapositive can be pushed one substantive step
further.  A large canonical prime **modulus** in the Turan range always
produces, with only a constant loss, a genuinely **negative** centered cosine
sum on an actual prime-power shell at an allowed half-integer center, with
the same `N^(-1)` mass normalization as Turan's modulus.
Therefore a hypothetical zero close to one does force a polarity-correct
canonical negative QP-band event at a polynomially related scale.

This does not yet contradict fixed-power QP KILL.  QP KILL bounds the radial
positive-antipode depth, whereas the zero event is one canonical coefficient
direction.  The remaining statement is an actual-prime radialization
inequality comparing that directional depth with the antipode radius.  It is
exactly the coefficient adapter, not a phase, scale, or centering problem.

No radialization inequality, QP-to-strip implication, QP theorem, or strip
is proved here.

---

## 1. Canonical modulus and mass-normalized negative depth

Fix `w=1/5`, put `C_w=2 exp(w)`, and initially choose any

```text
1/2<A'<A=50/33.                                      (1.1)
```

Sections 1--3 only use `A'<2`.  The zero-free consequence in Sections 4--5
also requires the explicit Turan coverage condition recorded in (4.2)
below; it holds for `A'` sufficiently close to `50/33` at every
`0<d<=.019`.

Let

```text
L_N(A')=sup N^(-1)|sum_(N_1<=p<=N_2)p^(-i tau)|,     (1.2)
```

where the supremum is over

```text
N<=N_1<N_2<=2N,
N^(1/2)<=tau<=N^(A').                                (1.3)
```

Define `E_N^-(A')` as the largest number of the form

```text
-N^(-1)sum_(p in I)cos[tau log(p/Y)],                (1.4)
```

where

- `Y` is an allowed half-integer with `N<=Y<=C_w N`;
- `I` is a nonempty prime interval contained in
  `[Y exp(-w),Y exp(w)]`;
- `tau` obeys (1.3) and lies in the QP band of `Y`.

If `M=#(I intersect primes)`, then weights `1/M` on these primes and zero on
every other shell prime power are a legal positive actual-node coefficient
vector, and (1.4) is `M/N` times its negative centered value.  The factor
`M/N` is essential: it is exactly the mass normalization in (1.2).

The superficially stronger probability-normalized definition

```text
sup -M^(-1)sum_(p in I)cos[tau log(p/Y)]              (1.5)
```

is identically `1` for all large `N`.  Indeed, take a singleton prime
`I={p}` in a shell.  Since a half-integer center cannot equal `p`, its node
`u=|log(p/Y)|` is nonzero; an odd multiple of `pi/u` lies in
`[N^(1/2),N^(A')]` for `A'>1`, and the cosine is `-1`.  Therefore (1.5)
cannot be used in a radialization theorem.  This is why every statement
below uses `E_N^-`, not probability-normalized depth.

This is an actual-prime refutation of the discarded radialization law, not
just an atomic warning.  The unconditional Vinogradov--Korobov tent theorem
gives, uniformly for all the present centers and every fixed polynomial
aperture,

```text
R_N^QP<=exp[-c (log N/log log N)^(1/3)]=o(1).         (1.6)
```

Together with (1.5)=`1`, this disproves
`(probability depth)<=C(R_N^QP)^lambda` for every fixed `C` and
`lambda>0`.  The mass-normalized replacement (1.4) is therefore mandatory.

---

## 2. Half-integer logarithmic phases cover every fixed arc

The discrete center condition is not an obstruction.

### Lemma 2.1 (uniform half-integer phase coverage)

Let `I_N` be any interval of half-integer centers contained in `[N,CN]` and
of length at least `cN`, where `c,C>0` are fixed.  Uniformly for

```text
N^(1/2)<=tau<=N^(A'),             A'<2,              (2.1)
```

the phases

```text
tau log(m+1/2) modulo 2 pi,       m+1/2 in I_N,      (2.2)
```

have discrepancy `o(1)`.  In particular, every fixed arc contains one of
these phases for all sufficiently large `N`.

#### Proof

Apply Erdos--Turan with truncation `H=N^eta`, where

```text
0<eta<2-A'.                                          (2.3)
```

For `1<=h<=H`, the phase

```text
f_h(x)=h tau log(x+1/2)                              (2.4)
```

has second derivative of constant sign and size

```text
|f_h''(x)|asymp h tau/N^2                            (2.5)
```

throughout `I_N`.  The standard second-derivative estimate gives

```text
|sum_(m+1/2 in I_N) exp[i f_h(m)]|
 <<sqrt(h tau)+N/sqrt(h tau).                        (2.6)
```

After division by `#I_N asyp N` and summation with the Erdos--Turan weights
`1/h`, the discrepancy is

```text
<<N^-eta+N^[(A'+eta)/2-1]+N^-1/4=o(1).              (2.7)
```

All three exponents are negative by (2.3).  QED

---

## 3. Modulus-to-negative phase alignment

### Theorem 3.1 (canonical modulus implies a negative actual-shell value)

For fixed `w` and `A'<A`,

```text
L_N(A') <=(4/3) J_w E_N^-(A')           (N large),    (3.1)
J_w=ceil[2 log(2)/w].                                 (3.2)
```

At the project width `w=1/5`, `J_w=7`.

#### Proof

Take an interval and height in (1.2)--(1.3), and write its complex prime sum
as `S`.  Partition `[N_1,N_2]` into at most `J_w` logarithmic intervals of
ratio at most `exp(w/2)`.  One piece `[a,b]` has sum `S_0` satisfying

```text
|S_0|>=|S|/J_w.                                      (3.3)
```

Every center in

```text
[b exp(-w),a exp(w)]                                 (3.4)
```

places `[a,b]` inside its shell.  Because `b/a<=exp(w/2)`, the interval in
(3.4), after intersecting with `[N,C_wN]`, has length `gg_w N`.

Lemma 2.1 supplies an allowed half-integer `Y` for which

```text
Re[Y^(i tau)S_0]<=-3|S_0|/4.                         (3.5)
```

Since `Y>=N`, the upper bound `tau<=N^(A')` lies below `Y^A`; since
`Y<<N` and `tau>=N^(1/2)`, the lower QP bound `Y^.01` also holds for large
`N`.  Therefore

```text
-N^(-1)Re[Y^(i tau)S_0]>=3|S|/(4J_wN).               (3.6)
```

Taking suprema proves (3.1).  QED

This theorem resolves three possible loopholes simultaneously: the complex
phase of Turan's prime sum, the half-integer center restriction, and the
need to place the selected prime interval inside one fixed-width shell.

---

## 4. Exact contrapositive consequence of a near-one zero

The audited Turan theorem says that a uniform estimate

```text
L_N(A')<<N^-d                                        (4.1)
```

implies a high-height zero-free strip of width `(d/A')^2`, provided the
half-power lower edge covers every length in the local Turan window.  A
sufficient explicit condition, uniform up to the limiting strip width, is

```text
0<d<=.019,
r_d=(d/A')^(1/6),
(1+r_d)/[2A'(1-r_d)]<1.                              (4.2)
```

At `d=.019` and `A'=50/33`, the last quantity is
`.9441382387...`; hence (4.2) persists for `A'<50/33` sufficiently close to
`50/33`.  This condition is indispensable for the particular natural-prime
Turan theorem being invoked: merely assuming `A'>1/2` does not make its
longest prime interval satisfy `tau>=N^(1/2)`.

Under (4.2), the local contrapositive of the audited Turan criterion,
combined with Theorem 3.1, says:

> A sufficiently high zeta zero in `Re(s)>1-(d/A')^2` forces, at one of the
> polynomially related Turan scales, a legal canonical shell prime interval
> whose mass-normalized centered cosine sum is at most `-N^(-d)` at a height
> in the QP band.

Here is the local quantifier check.  For a zero `rho=sigma+iT`, choose

```text
sqrt(1-sigma)<beta<d/A',       r=beta^(1/6),          (4.3)
```

and then choose `eta>0` small enough that the strict half-power coverage in
(4.2) persists.  In the notation of the audited local criterion, take

```text
D=(1+eta)/[A'(1-r)].                                (4.4)
```

Because the zero lies in the local `T` window and to the right of
`1-beta^2`, contraposition produces an interval sum at some

```text
T^[D(1-r)]<=N<=T^[D(1+r)],       tau=T+O(T^(1/2)),   (4.5)
```

whose relative modulus is larger than a fixed constant times
`(log N)^10 tau^(-beta)`.  But

```text
N^-d<=T^[-dD(1-r)]
     =T^[-d(1+eta)/A']=o(T^-beta).                   (4.6)
```

Thus the fixed Turan constant, the logarithm, and the factor `4J_w/3` in
Theorem 3.1 are all absorbed for sufficiently large `T`, yielding the
displayed depth `N^-d`.  This is a genuinely local contrapositive tied to
the given zero; the bare logical contrapositive of an eventual global strip
statement would only give an unlocalized sequence of failures.

Thus the zero really does force the negative polarity relevant to the
one-sided problem.  No fixed-ordinate limit is being taken: the center and
scale move polynomially with the zero height, exactly as permitted by QP.

---

## 5. The sole surviving adapter is radialization

Put

```text
K_N=[N^(1/2),N^(A')],                                (5.1)
R_N^K=sup {r_+(K_N;S_Y):N<=Y<=C_wN, Y allowed},
R_N^QP=sup {r_+(H_Y;S_Y):N<=Y<=C_wN, Y allowed}.     (5.2)
```

The first radius uses the common Turan subband; the second is the full QP
radius actually controlled by DPA.  Since `K_N subset H_Y`,
`R_N^K<=R_N^QP`.  Pair a `K_N` antipode with
the uniform probability on all primes in the fixed-width shell.  The prime
number theorem gives `M>>_w N/log N`, so

```text
E_N^-(A')>>_w R_N^K/log N.                           (5.3)
```

Indeed, the pairing locates a prime average at most `-r`; multiplication by
`M/N` gives (5.3).  This is still the wrong direction for a reverse theorem.
The missing zeta-specific statement is

```text
MRAD_QP(lambda): E_N^-(A')<=C (R_N^QP)^lambda
                 for some fixed lambda>0.            (5.4)
```

The power law (5.4) is stronger than the reverse argument actually needs.
For fixed exponents `d,c>0`, the weakest threshold form is

```text
LTRAD(d,c):
E_N^-(A')>=N^-d  ==>  R_N^QP>=N^-c                 (5.4a)
for every sufficiently large N.                     
```

If DPA holds at an exponent `c_0>c`, then (5.5) contradicts the conclusion
of `LTRAD(d,c)`, so `E_N^-<N^-d`; Theorem 3.1 then supplies the natural
prime saving needed by Turan.  Thus `LTRAD(d,c)` alone gives strip width
`(d/A')^2` under (4.2).  Taking `d=lambda*c` and allowing exponent slack
recovers the consequence of (5.4), without assuming a global Holder law.

There is no atomic-floor issue at this threshold.  If an interval `I` with
`M` primes realizes `E_N^->=N^-d`, then

```text
M>=-sum_(p in I)cos[tau log(p/Y)]>=N^(1-d).          (5.4b)
```

Hence it is enough to prove `LTRAD(d,c)` for intervals containing at least
`N^(1-d)` primes.  Singletons contribute only `1/N` and are irrelevant for
the project values `d<=.019`.

Finally, `E_N^-` is already a localized natural-prime modulus in disguise.
For the same interval and height,

```text
-Re[Y^(i tau)sum_(p in I)p^(-i tau)]
 <=abs(sum_(p in I)p^(-i tau)),                      (5.4c)
```

so `E_N^-` is bounded above by the corresponding `N^(-1)` shell-modulus
supremum.  Conversely Theorem 3.1 bounds the original Turan modulus by a
fixed multiple of `E_N^-`.  All shell scales differ from `N` by fixed
factors only.  Formally the reverse comparison is with
`sup_(N' asymp N)L_(N')`, not with the single `L_N` whose intervals are
restricted to `[N,2N]`.  Thus (5.4) or (5.4a) is, up to phase alignment and
comparable scales, precisely the coefficient-sensitive natural-modulus-to-radial
comparison isolated earlier as `COMP`; it is not furnished by a generic
convex theorem.

It is a pure directional-to-radial comparison for the complete actual-prime
curve.  The target deliberately uses the **full** QP radius, because that is
the weakest radius sufficient for contradiction with DPA.  The common-band
radius is needed only in the automatic wrong-way estimate (5.3): pairing a
full-band antipode with a canonical vector would locate a negative value
somewhere in `[Y^.01,Y^A]`, not necessarily above `N^(1/2)`.

For `Y` in the range in (5.2), `K_N` is contained in `H_Y` for all large
`N`.  Monotonicity under restriction of the ordinate set and DPA therefore
give

```text
r_+(K_N;S_Y)<=r_+(H_Y;S_Y)<=Y^-c<=N^-c.             (5.5)
```

Consequently, if `d=lambda*c<=.019`, (4.2) holds with `d=lambda*c`, and
`MRAD_QP(lambda)` holds, fixed-power DPA/QP KILL gives

```text
R_N^QP<=N^-c
 ==>E_N^-<<N^(-lambda c)
 ==>L_N<<N^(-lambda c),                              (5.6)
```

where the last arrow is Theorem 3.1.  Turan then yields the high-height strip

```text
Re(s)<=1-(lambda c/A')^2.                            (5.7)
```

Letting `A'` increase to `A=50/33` recovers the conditional width
`(lambda c/A)^2`; bounded heights leave a possibly smaller positive global
width.

The Fejer and finite-factor countermodels in the existing bridge report show
that (5.4) is not a support-only convex-geometric fact.  For zeta's actual
prime shells it remains open.  Theorem 3.1 proves that no additional
modulus-to-sign, moving-band, half-integer-center, or shell-placement adapter
is needed.

---

## 6. Binary disposition

```text
zero localization -> canonical prime modulus:          PROVED (TURAN);
canonical modulus -> negative actual-shell mass:       PROVED HERE;
phase/centering/moving-band loss:                       REMOVED;
negative canonical mass -> full QP radius:             OPEN (LTRAD/MRAD_QP);
fixed-power QP KILL -> uniform zeta strip:              CONDITIONAL ONLY;
QP, QP <=> strip, or a uniform strip:                   NOT PROVED.
```

Executable replay:

- `src/qp_zeta_reverse_phase_gate.py`;
- `src/test_qp_zeta_reverse_phase_gate.py`.
