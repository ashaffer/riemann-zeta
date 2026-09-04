# FGF4 twisted-cousin route: hostile literature and no-go referee audit

**Date:** 2026-08-14
**Scope:** the selected near-quarter gap-four sector only
**Status:** exact reduction and fail-fast moment thresholds checked; no
published unconditional theorem located with the required four simultaneous
quantifiers; no theorem located that rules out the coefficient-specific target.

## 1. Referee verdict

The proposed gap-four target is normalized correctly.  For

```text
kappa=.0197404825829...,
H=Y^h,
q=Y^b,
.1537<=b<=min(h,.24812030075...),
q=3 (mod 4),
a=(q+1)/4,
```

the exact gap-four part of the selected transition is

```text
2i(1+e(1/q))
 sum_(p,p+4 prime in I) chi_4(p)e(p/(4q))
 +O(H/q+1).                                           (1.1)
```

The multiplier in (1.1) has modulus

```text
4|cos(pi/q)|,
```

so it neither supplies nor costs a power.  The puncture error is harmless
because `b>kappa` and `h>kappa`.  A uniform theorem of the form

```text
|sum_(p,p+4 prime in I) chi_4(p)e(p/(4q))|
   <<H q^(-delta)Y^o(1)                               (1.2)
```

closes this sector provided

```text
delta>kappa/.1537=.1284351501815....                  (1.3)
```

Thus `q^(-1/8)` misses the uniform lower-denominator endpoint by

```text
kappa-.1537/8=.0005279825829...                       (1.4)
```

in the `Y` exponent.

The literature boundary is unfavorable but precise:

1. no checked result treats **one fixed shift `4`**, **one individual
   height-selected modulus `q`**, **every physical block of length
   `Y^.248...` through `Y^.58...`**, and the **preserved character/additive
   twist**;
2. existing prime-pair dispersion theorems average the shift, modulus, or
   both, and allow the required pair `(4,q)` to be exceptional;
3. Kloosterman and spectral theorems with power errors apply after a
   divisor/factorable expansion, not to the exact second-prime indicator;
4. a positive sieve majorant cannot be transferred through this complex
   Fourier coefficient;
5. Ford--Maynard and the classical parity examples rule out deductions from
   specified generic sieve axioms, not the actual signed coefficient (1.2).

There is therefore **no genuine no-go theorem for (1.2)**.  There is a
definitive scoped obstruction to the obvious black-box routes.  At the hard
endpoint `q asyp H`, nonzero-frequency `L2` dispersion has an unavoidable
literal diagonal and cannot close from the natural cousin-pair mass.  A
centered `L4` dispersion target is not killed by that diagonal and remains a
legitimate, but genuinely new, research problem.

Even a proof of (1.2) settles only the FGF4 sector.  It does not prove the
whole signed transition or a strip.

---

## 2. Independent reconstruction of the coefficient

Write `e(x)=exp(2*pi*i*x)` and `e_q(x)=e(x/q)`.  Since

```text
a/q=1/4+1/(4q),
```

for every odd prime `p`,

```text
e_q(ap)=e(p/4)e(p/(4q))
       =i chi_4(p)e(p/(4q)).                          (2.1)
```

If

```text
P_I={p in I:p and p+4 are prime},
A_I(r)=#{p in P_I:p=r (mod q)},
Ahat_I(b)=sum_(r mod q)A_I(r)e_q(br),
```

then the twisted cousin sum is exactly

```text
T_I(q):=sum_(p in P_I)chi_4(p)e(p/(4q))
       =-i Ahat_I(a).                                 (2.2)
```

The edge calculation in the source audit gives

```text
R_(I,4)(a/q)=2i(1+e(1/q))T_I(q)+O(H/q+1).             (2.3)
```

Every pair in `P_I` with `p>3` is automatically consecutive: among
`p,p+2,p+4`, primality of the endpoints forces `3|(p+2)`.  No growing-order
inclusion--exclusion is hidden in (2.3).

The exact local bill is `H Y^(-kappa)`.  At a particular exponent `b`, a
`q`-power theorem only needs `delta>kappa/b`.  In particular, at the physical
endpoint

```text
b=h=33/133=.24812030075...,
```

the exact endpoint requirement is

```text
delta_end>kappa/h=.0795601267741....                  (2.4)
```

The stronger value (1.3) is required only if one insists on a single
`q^(-delta)` theorem that also covers `b=.1537`.  This distinction matters
when judging endpoint moment thresholds.

---

## 3. What the endpoint `q asyp H` really asks for

For `p,p+4>3` prime, one has `p=1 (mod 3)`.  Hence

```text
p=1 or 7 (mod 12),
chi_4(p)=+1 or -1, respectively.                      (3.1)
```

Across a block of length `H`, the slow factor `e(p/(4q))` turns through angle

```text
2*pi*H/(4q)=pi*H/(2q)=O(1)                            (3.2)
```

when `q asyp H`.  It is not a long oscillation.  Define the unmodulated
prefix race

```text
B_I(t)=sum_(p in P_I,p<=t)chi_4(p)
      =# {p<=t:p in P_I,p=1 mod 12}
       -# {p<=t:p in P_I,p=7 mod 12}.                 (3.3)
```

Abel summation gives exactly

```text
T_I(q)=B_I(v)e(v/(4q))
       -(2*pi*i/(4q))int_u^v B_I(t)e(t/(4q))dt        (3.4)
```

for `I=(u,v]`, with the evident endpoint convention.  Consequently

```text
|T_I(q)|
 <=(1+pi*H/(2q)) sup_(u<t<=v)|B_I(t)|.                (3.5)
```

Thus a power-saving cousin-pair race on every block and every prefix would
transfer directly at the endpoint.  No such theorem was located.  Ordinary
equidistribution of single primes modulo `4` is not a substitute for (3.3),
which conditions simultaneously on `p+4` being prime.

The Hardy--Littlewood local model predicts equal main terms for the two
classes.  As a useful sanity check, if `q` is prime, summing the additive
character over the admissible residue classes `r !=0,-4 (mod q)` gives

```text
sum_(r mod q,r(r+4)!=0)e_q(ar)=-1-e_q(-4a)=O(1).      (3.6)
```

Among `asymp q` allowed classes this is a `q^(-1)` local Fourier factor, so
the conjectural local main term is harmless.  Formula (3.6) is not an error
theorem; the missing input is pointwise control of the discrepancy for the
actual fixed-shift support.

---

## 4. Exact selected-`q` dispersion identities

Put `N=|P_I|` and retain the notation `A_I(r)`.  For

```text
V_I(q)=sum_(r mod q)(A_I(r)-N/q)^2,                   (4.1)
```

nonzero-frequency Parseval gives

```text
sum_(b=1)^(q-1)|Ahat_I(b)|^2=q V_I(q).                (4.2)
```

If `C_I(d)` counts unordered pairs `p<p'` in `P_I` with `p'-p=d`, then

```text
V_I(q)=N-N^2/q+2 sum_(k>=1)C_I(kq).                  (4.3)
```

When the block diameter is strictly below `q`, the last sum vanishes and

```text
V_I(q)=N-N^2/q.                                      (4.4)
```

An `L2` proof of (1.2) would require

```text
V_I(q)<<H^2 q^(-1-2delta)Y^o(1).                     (4.5)
```

At `H=q` and the conjectural/natural mass `N=q/log^(2+o(1))q`, the left side
of (4.5) is `q/log^(2+o(1))q`, whereas its right side is
`q^(1-2delta+o(1))`.  With the uniform exponent (1.3), an `L2` closure would
instead need roughly

```text
N<=q^(1-2delta+o(1))=q^(.7431296996...+o(1)).         (4.6)
```

Equivalently, at general `H=Y^h,q=Y^b`, natural mass is compatible with this
uniform `L2` route only if

```text
h>=b(1+2delta).                                       (4.7)
```

At `h=33/133` this restricts `b` to

```text
b<=.19741122108....                                   (4.8)
```

For the exact `Y^(-kappa)` bill rather than the stronger uniform theorem,
the analogous feasibility condition is `b+2kappa<=h`.  Either formulation
fails at `b=h`.  This is a no-go for a natural-mass, all-nonzero-frequency
`L2` proof, not a theorem that the selected coefficient is large: the pair
set could be unusually sparse, or one selected Fourier mode could cancel.

There is a materially different fourth-moment identity.  Define

```text
R_I(s)=sum_(r mod q)A_I(r)A_I(r+s),
E4_I(q)=sum_(s mod q)(R_I(s)-N^2/q)^2.                (4.9)
```

Then exactly

```text
sum_(b=1)^(q-1)|Ahat_I(b)|^4=q E4_I(q).              (4.10)
```

Therefore the sufficient centered fourth-order dispersion theorem is

```text
E4_I(q)<<H^4 q^(-1-4delta)Y^o(1).                    (4.11)
```

At `H=q` and the uniform exponent (1.3), (4.11) allows

```text
E4_I(q)<<q^(3-4delta+o(1))
        =q^(2.4862593993...+o(1)).                    (4.12)
```

The literal zero-shift term in (4.9) is
`(N-N^2/q)^2`, of natural size `q^2/log^(4+o(1))q`, so it fits inside
(4.12).  Even the stronger uniform theorem is therefore **not diagonally
ruled out at `L4`**.  If one asks only for the exact endpoint exponent
(2.4), the allowance is the still larger `q^(2.6817594929...+o(1))`.

This is the cleanest surviving dispersion opportunity.  It is also a new
fourth-order additive-energy theorem for the exact cousin-prime support;
none of the literature below proves it.  An average over shifts or moduli
does not control (4.11) for the selected pair `(4,q)`.

---

## 5. Exact Buchstab bilinearization and where it stops

Let `P^-(n)` be the least prime factor of `n`, with `P^-(1)=infinity`, and
let `z>=3`.  One-step Buchstab decomposition gives the exact identity

```text
1_(n prime)
 =1_(P^-(n)>=z)
  -sum_(z<=r<=sqrt(n), r prime, r|n)
       1_(P^-(n/r)>=r).                               (5.1)
```

Apply (5.1) to `n=p+4=rm`.  Since `r,m` are odd,

```text
chi_4(rm-4)=chi_4(rm)=chi_4(r)chi_4(m).               (5.2)
```

Thus (2.2) becomes exactly

```text
T_I(q)=T_(I,rough)(q)
 -e(-1/q)
  sum_(r,m:rm-4 prime, P^-(m)>=r)
    chi_4(r)chi_4(m)e(rm/(4q)),                       (5.3)
```

with the evident ranges imposed by `rm-4 in I` and `r>=z`.

Equation (5.3) is a real transfer opportunity: Matomaki-type
well-factorable exponential estimates can control suitable linear-sieve
models for `T_(I,rough)`, and the product phase is native to bilinear or
Kloosterman analysis.  It does not finish the exact problem.  Cauchy in `r`
expands terms with simultaneous conditions

```text
rm_1-4 prime,          rm_2-4 prime,                  (5.4)
```

plus the two roughness constraints.  The coefficient in (5.4) is coupled,
not a product of two arbitrary one-variable sequences.  Its diagonal
`m_1=m_2` is explicit; the off-diagonal is another fixed-shift prime
correlation.  No checked spectral or Kloosterman lemma accepts (5.4) and
returns the needed selected `q` power.  In particular, (5.3) exposes no
automatic `q^(-1/8)` saving.

---

## 6. Primary-literature quantifier audit

The following table records what was checked and the first fatal mismatch.
An entry marked “average” cannot be assigned to a modulus or shift chosen by
the height rule.

| Primary result | Native statement relevant here | Why it does not transfer |
|---|---|---|
| [Mikawa, *On prime twins in arithmetic progressions* (1992)](https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf) | `sum_(q<=x^(1/2)log^-B x) max_a sum_(0<2k<=x)|E(x;q,a,2k)| << x^2 log^-A x` | It averages both the modulus and the even shift.  Shift `4` and the selected `q` may be exceptional; it is also a long-prefix result without the preserved twist. |
| [Kawada, *The prime k-tuplets in arithmetic progressions* (1993)](https://tsukuba.repo.nii.ac.jp/record/15690/files/3.pdf), Theorems 1--2 | Averages moduli and tuple translations.  The short-interval theorem assumes `y>=x^(2/3)` up to logs and `Q<=y x^(-1/2)` up to logs. | It may discard the fixed translation `(0,4)`.  Our `h<=.58<2/3`; even ignoring that, its modulus range is at most exponent `h-1/2`, below `b>=.1537`. |
| [Laporta, *A short intervals result for 2n-twin primes in arithmetic progressions* (1999)](https://hdl.handle.net/11588/492652) | The variable `2n` is the prime difference in `2n=p_1-p_2`; the theorems average that difference and progression moduli. | “Short interval” does not mean a pointwise theorem for the fixed difference `4` on each physical `p`-block. |
| [Matomaki--Radziwill--Tao, *Correlations of the von Mangoldt and higher divisor functions I*](https://arxiv.org/abs/1707.01315), Theorem 1.3 | The expected `Lambda(n)Lambda(n+h)` asymptotic for almost all shifts in a window of length at least `X^(8/33+epsilon)`, on a long dyadic `n` range, with logarithmic error saving. | The paper explicitly notes that no asymptotic is known for a single fixed even `h`.  It may discard `h=4`, and contains neither our short physical block nor selected additive twist. |
| [Lichtman, *Averages of the Mobius function on shifted primes*](https://arxiv.org/abs/2009.08969) | Cancellation of `mu(p+h)` for shifts on average when `log H/loglog X -> infinity`. | The paper states the fixed-shift assertion as a folklore conjecture.  It diagnoses, rather than supplies, the parity-sensitive large-divisor input left by exact divisor decompositions. |
| [Green--Tao, *Restriction theory of the Selberg sieve*](https://arxiv.org/abs/math/0405581) | Natural-scale `L^p` control in frequency for functions dominated by prime-tuple sieve majorants. | It controls how many frequencies are large, not the height-selected one.  Sampling/localizing a degree-`H` polynomial restores the `H^(1/p)` loss and no fixed power at one frequency. |
| [Matomaki, *A Bombieri--Vinogradov type exponential sum result with applications*](https://doi.org/10.1016/j.jnt.2009.01.010), Theorem 1 | A full-dyadic exponential estimate for `Lambda(n)` with a well-factorable divisor weight.  At this phase its displayed terms give a global model saving `min(b/4,1/20)`, at least `.038425`. | The theorem is not block-local at `H=Y^.248...-.58...`; the divisor weight is a linear/Chen-sieve model for `n+4`, not `1_(n+4 prime)`. |
| [Grimmelt--Teravainen, *The exceptional set in Goldbach's problem with almost twin primes*](https://arxiv.org/abs/2207.08805), Proposition 6.5 | Pointwise Fourier transference for specified nonnegative sieve-model functions. | The exact shifted-prime indicator is not in the model class, and the order step used by the convolution architecture is unavailable against our signed/complex test. |
| [Drappeau, *Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method*](https://arxiv.org/abs/1504.05549) | Quintilinear Kloosterman bounds; power errors for the Titchmarsh divisor problem under GRH for Dirichlet `L`-functions, and divisor-correlation applications. | The arithmetic coefficient is divisor/factorable.  The theorem does not replace it by `Lambda(n)Lambda(n+4)` or accept the coupled prime constraints (5.4). |
| [Cowan, *A twisted additive divisor problem*](https://arxiv.org/abs/2304.12572) | Spectral asymptotics for shifted convolutions of twisted generalized divisor functions `sigma(n,chi)sigma(n+k,psi)`. | Eisenstein/divisor coefficients possess the required automorphic spectral expansion; the two von Mangoldt factors do not inherit it. |
| [Matomaki--Merikoski, *Siegel zeros, twin primes, Goldbach's conjecture, and primes in short intervals*](https://arxiv.org/abs/2112.11412) | Under the extraordinary assumption of a real exceptional zero, an asymptotic for `sum Lambda(n)Lambda(+-n+h)`, uniform in large `h`. | It is conditional on a Siegel-zero regime, is a long-prefix result, and has no selected phase.  It is evidence that Kloosterman machinery needs additional parity-breaking structure, not an unconditional transfer. |
| [Matomaki--Radziwill--Tao, *Fourier uniformity of bounded multiplicative functions in short intervals on average*](https://arxiv.org/abs/1812.01224) | Local Fourier cancellation averaged over interval starts for nonpretentious multiplicative functions, with applications averaged over prime shifts. | `chi_4` is a bounded-conductor pretentious character, and the exact prime-pair condition is not a multiplicative coefficient.  The fixed shift remains outside the theorem. |
| [Akeno, *On the level of distribution of Goldbach primes and its applications* (2026)](https://arxiv.org/abs/2606.29559), Theorems 1.1 and 2.1 | Level `1/6` for Goldbach-prime sets for all but `O(X log^-A X)` even `N`; the exponential input is mean-square over `d` and additive residues on a full `X` range. | A cousin pair would be the central representation of the varying integer `N=2p+4`.  “Almost all `N`” neither selects that representation nor fixes shift `4`; the new exponential estimate averages the wrong frequency family. |
| [Bazin, *A Bombieri--Vinogradov theorem for exponential sums over products of k primes* (2026)](https://arxiv.org/abs/2607.15137) | Full-prefix, denominator-averaged estimates for the unshifted sequence `1_(Omega(n)=k)`. | `Omega(n(n+4))=2` on cousin pairs does not linearize the thin quadratic support `m=n(n+4)`, and the phase is linear in `n`, not `m`. |

The character-weighted endpoint is not hidden in any of these statements.
Writing one von Mangoldt factor as `chi_4 Lambda` merely translates its
ordinary prime Fourier spectrum by `1/4`; it does not create an independent
small spectrum.  Major-major local terms cancel as in (3.6), but the
residual-residual correlation is still the fixed-shift binary problem.

---

## 7. What the parity and prime-producing-sieve no-go theorems say

Murty--Vatwani's
[*Twin primes and the parity problem*](https://mast.queensu.ca/~murty/TwinPrimes-Parity.pdf)
formulates a shifted-Mobius Elliott--Halberstam conjecture.  Together with
ordinary Elliott--Halberstam it implies fixed-even-shift prime pairs.  This
is a precise description of additional parity-sensitive information; it is
not a proved input and not an impossibility theorem.

The latest checked version of Ford--Maynard,
[*On the theory of prime-producing sieves*](https://arxiv.org/html/2407.14368)
(dated 2026-08-11), is equally important to scope correctly:

- its ambient sequence `a_n` is arbitrary, bounded/nonnegative, and is
  compared with another sequence through specified Type-I and Type-II
  axioms;
- Theorem 2.1 constructs, for every `gamma<1` and sufficiently narrow Type-II
  range, sequences satisfying those axioms but with zero weight on every
  prime;
- Theorem 2.2 gives an exact criterion for when those axioms force an
  asymptotic and constructs alternative sequences when the criterion fails.

Therefore Ford--Maynard genuinely rules out a proof that uses only the
corresponding generic Type-I/Type-II information.  It does **not** assert
that the actual cousin-prime sequence behaves like a counterexample, and it
does not cover the signed/complex coefficient (1.2).  Splitting (1.2) into
its positive and negative residue classes does not change this logical
scope: the theorem shows that the axioms do not determine prime mass, not
that the actual two masses cannot cancel.

The classical Selberg example `a_n=1+lambda(n)` has the same status.  It is a
nonnegative sequence with no mass on primes and excellent Type-I behavior,
showing that Type I alone cannot detect primes.  It is a method countermodel,
not a counterexample to an actual-prime statement.

There is also an elementary order obstruction.  If `0<=f<=nu` and `|u_n|=1`,
then in general

```text
|sum u_n f_n|<=|sum u_n nu_n|                         (7.1)
```

is false.  For `u=(1,-1)`, `f=(1,0)`, and `nu=(1,1)`, the two sides of
(7.1) are `1` and `0`.  Thus no positive Selberg/Chen majorant can be
substituted into (1.2) without separately proving that its excess has a
power-small selected Fourier coefficient.  That separate assertion is
already the missing parity-sensitive input.

---

## 8. Exact transfer opportunities that remain

The audit leaves four honest interfaces.

### 8.1 Endpoint race theorem

Prove, for every endpoint block,

```text
sup_(t in I)|B_I(t)|<<H Y^(-kappa-epsilon).           (8.1)
```

Equation (3.5) transfers (8.1) to the slow phase whenever `q asyp H`.  This
is a fixed-power, fixed-shift cousin-prime race theorem; no checked source
supplies it.

### 8.2 Centered fourth-order dispersion

Prove (4.11), at least for the individual height-selected modulus and the
near-quarter frequency.  The literal diagonal fits with a strict power
margin, unlike `L2`.  This is the only moment route in this audit that
survives the endpoint fail-fast test.  A theorem averaged over `q`, over the
shift, or over block starts must include an additional selector-stability
argument before it can be used.

### 8.3 Coefficient-specific Buchstab Type II

Use (5.3), but prove a Type-II estimate for its **actual coupled** coefficient
and for the physical block.  Once such an estimate has converted the
second-prime condition into factorable data with power-small selected
Fourier error, Matomaki/Drappeau-style phase and Kloosterman lemmas become
usable.  They do not perform that conversion themselves.

### 8.4 A power-accurate signed sieve model

Construct a factorable signed approximation `w(n+4)` satisfying directly

```text
|sum_(n in I) Lambda(n)chi_4(n)e(n/(4q))
  (1_(n+4 prime)-w(n+4))|
   <<H Y^(-kappa-epsilon).                            (8.2)
```

Matomaki's global model exponent shows that the rational phase is then
affordable.  But (8.2), not the existing well-factorable theorem, is the new
parity-sensitive content.

---

## 9. Truth boundary

```text
near-quarter coefficient and factor 4:                  EXACT
uniform q-saving threshold delta>.12843515018:           EXACT
endpoint-only threshold delta>.07956012677:              EXACT
gap-four pairs automatically consecutive:                EXACT
endpoint reduction to 1-vs-7 mod 12 race with slow phase: EXACT
nonzero-frequency L2 diagonal obstruction at q~H:         EXACT, METHOD-SCOPED
centered L4 literal diagonal rules the route out:          NO
centered L4 theorem (4.11):                               OPEN
exact Buchstab bilinearization (5.3):                     EXACT
published spectral lemma closes its coupled off-diagonal: NO THEOREM FOUND
positive sieve majorant transfers through the twist:      FALSE IN GENERAL
Mikawa/Kawada/Laporta fix both shift 4 and selected q:     NO
Ford--Maynard eliminates the actual signed coefficient:    NO
Ford--Maynard eliminates inadequate generic I/II axioms:   YES
published unconditional theorem for (1.2):                NOT FOUND
published no-go theorem making (1.2) impossible:           NOT FOUND
FGF4 sector closed:                                       NO
whole transition or strip proved:                         NO
```

The exact finite identities and exponent ledger are replayed by
[`verify_zeta23_fgf4_selected_q_dispersion.py`](verify_zeta23_fgf4_selected_q_dispersion.py)
and the companion module/tests.  They certify algebra and finite examples,
not an asymptotic prime theorem.
