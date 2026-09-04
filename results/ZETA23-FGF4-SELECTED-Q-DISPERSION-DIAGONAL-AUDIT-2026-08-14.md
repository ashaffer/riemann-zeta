# FGF4: selected-`q` dispersion, Buchstab bilinearization, and endpoint audit

**Date:** 2026-08-14
**Status:** exact selected-frequency, centered-moment, and one-step Buchstab
identities are proved.  They do not yield the required power saving.  The
failure statement below is a method barrier, not a no-go theorem for the
actual cousin-prime coefficient.

## Verdict

Let

```text
P_I={p in I:p and p+4 are prime},       N_I=#P_I,
q=3 (mod 4),                            a=(q+1)/4,
S_4(I;q)=sum_(p in P_I) chi_4(p)e(p/(4q)).            (0.1)
```

The direct attack has a binary outcome.

1. The selected coefficient has exact fixed-`q` dispersion identities.  If
   `A(r)=#{p in P_I:p=r (mod q)}`, then

   ```text
   S_4(I;q)=-i sum_(r mod q) A(r)e_q(ar).             (0.2)
   ```

   No modulus, frequency, or shift is averaged in (0.2).

2. Centering deletes the additive zero mode exactly.  The resulting `L2`
   identity has an unavoidable literal cousin-pair diagonal.  When the
   integer diameter of `I` is strictly below `q` (in particular, for a
   half-open block of length `H<=q`),

   ```text
   sum_(b=1)^(q-1)|sum_r A(r)e_q(br)|^2
      =q(N_I-N_I^2/q).                               (0.3)
   ```

   Consequently the all-frequency Cauchy step, even with the twin-sieve
   bound `N_I<<H(log Y)^(-2)Y^o(1)`, gives only `H(log Y)^(-1)Y^o(1)` at
   `H=q`.  It gives no fixed power of `q`.

3. The centered fourth moment is not killed by its diagonal.  It gives the
   exact remaining possible route

   ```text
   E_4(I;q):=sum_(s mod q)(R_A(s)-N_I^2/q)^2
      <<H^4 q^(-1-4delta)Y^o(1),                     (0.4)
   R_A(s)=sum_r A(r)A(r+s).
   ```

   Estimate (0.4) would imply `|S_4|<<Hq^(-delta)Y^o(1)`.  At `H=q` its
   right side is `q^(3-4delta)`, while the literal zero-shift floor is only
   about `N_I^2`.  Thus there is no algebraic `L4` no-go.  Proving (0.4),
   however, is a centered four-cousin correlation theorem at one selected
   modulus; a positive upper-bound sieve does not estimate its subtraction.

4. One exact Buchstab step does expose a bilinear phase `e(rm/(4q))`.
   It does **not** separate the arithmetic coefficient: the same term still
   contains `rm-4` prime.  The first Cauchy step has a phase-free
   `m_1=m_2` mode, while every off-diagonal contains the simultaneous shifted
   primality conditions `rm_1-4` and `rm_2-4`.  Iterating Vaughan or
   Heath--Brown identities preserves a fixed product-difference constraint.
   No `q^(-1/8)`, much less `q^(-1/8-eta)`, is exposed by this identity.

For the repository's conservative rationalized bill
`kappa_bar=.01974048259`, the required exponent is

```text
delta_req=kappa_bar/.1537=.128435150228...,
eta_req=delta_req-1/8=.003435150228....               (0.5)
```

Using the raw optimized value
`kappa_max=.0197404825829421...` instead gives
`kappa_max/.1537=.128435150181...`.  The rationalized value is a harmless
strictly stronger target, but it should not be confused with the raw exact
quotient.

Thus even an imported `q^(-1/8)` estimate would miss by
`q^(-.003435150228...)`, or by the `Y` exponent
`.00052798259...` at the lower denominator endpoint.

No published theorem located has the fixed shift, fixed selected modulus,
short block, and centered correlation quantifiers required by (0.4).  No
published no-go theorem located rules out the actual coefficient (0.1).
No zero-free strip is claimed.

---

## 1. Exact selected-frequency normalization

Every `p in P_I`, apart from the irrelevant bounded pair at the origin, is
odd.  For odd `p`,

```text
e(p/4)=i chi_4(p).
```

Since `4a=q+1`, this gives

```text
chi_4(p)e(p/(4q))=-i e(p/4)e(p/(4q))
                 =-i e_q(ap),                       (1.1)
```

which proves (0.2).  Notice that `(a,q)=1` automatically.

Put

```text
B(r)=A(r)-N_I/q,          Ahat(b)=sum_r A(r)e_q(br).
```

Because `sum_r e_q(ar)=0`, the selected coefficient is unchanged by
centering:

```text
Ahat(a)=sum_r B(r)e_q(ar).                            (1.2)
```

There is also a selected, rather than averaged, difference identity.  If

```text
C_I(h)=#{(p,p') in P_I^2:p-p'=h},
```

then

```text
|S_4(I;q)|^2=sum_h C_I(h)e_q(ah).                    (1.3)
```

The `h=0` term in (1.3) is exactly `N_I`.  It is numerically harmless at the
desired scale; the fatal amplification appears only if the selected
frequency is bounded by a nonnegative all-frequency moment.

---

## 2. Exact centered `L2` identity and the `H=q` endpoint

Finite Fourier orthogonality gives

```text
sum_(b=1)^(q-1)|Ahat(b)|^2=q V_I(q),
V_I(q)=sum_r(A(r)-N_I/q)^2.                          (2.1)
```

Expanding the residue collisions before applying any inequality gives

```text
V_I(q)=N_I-N_I^2/q+2 sum_(k>=1) C_I^+(kq),           (2.2)
```

where `C_I^+(h)=#{p<p' in P_I:p'-p=h}`.  Every term after the first two is
nonnegative.  If the integer diameter of `I` is strictly below `q`, distinct
lower endpoints cannot differ by a positive multiple of `q`, so (2.2) becomes

```text
V_I(q)=N_I-N_I^2/q.                                  (2.3)
```

This audits the diagonal before Cauchy.  Bounding the selected term by the
whole left side of (2.1) gives

```text
|S_4(I;q)|<=sqrt(q V_I(q)).                          (2.4)
```

At `H=q`, estimate (2.4) meets `Hq^(-delta)` only if

```text
N_I(1-N_I/q)<=q^(1-2delta).                          (2.5)
```

In the sparse regime `N_I=o(q)`, this asks for

```text
N_I<=q^(.743129699545...+o(1))                       (2.6)
```

at `delta=delta_req`.  The unconditional upper-bound sieve supplies only
`N_I<<q(log Y)^(-2)Y^o(1)`, and the Hardy--Littlewood prediction has that
same logarithmic rather than power sparsity.  Neither closes (2.5).

More generally, even granting the optimistic diagonal-scale estimate
`V_I(q)<<N_IY^o(1)` and `N_I<<H Y^o(1)`, (2.4) is

```text
|S_4(I;q)|<<sqrt(qH)Y^o(1).                          (2.7)
```

For `H=Y^h`, `q=Y^b`, (2.7) can reach `Hq^(-delta)` only when

```text
h>=(1+2delta)b.
```

At the required delta this ratio is

```text
1+2delta_req=1.256870300455....                      (2.8)
```

For the top block exponent `h=33/133`, the largest denominator exponent
compatible with (2.8) is only

```text
b=.197411221080...,
```

whereas the retained range includes `b=h=.24812030075...`.  In particular,
the endpoint `H=q` is decisively outside the all-frequency `L2` route.

This is not a lower bound for the selected Fourier coefficient.  The other
frequencies may carry all of (2.1), and the selected coefficient itself may
cancel.  Equations (2.3)--(2.8) close only the proof class that replaces one
selected frequency by the complete nonnegative second moment.

---

## 3. The centered fourth moment: still a genuine open route

Define the cyclic residue correlation

```text
R_A(s)=sum_(r mod q) A(r)A(r+s).
```

The zero frequency contributes `Ahat(0)=N_I`.  It must be removed before a
fourth-moment inequality.  Orthogonality gives the exact centered identity

```text
sum_(b=1)^(q-1)|Ahat(b)|^4
   =q sum_(s mod q)(R_A(s)-N_I^2/q)^2.               (3.1)
```

Thus (0.4) is a clean sufficient theorem.  With
`delta=delta_req` and `H=q`, its allowed energy is

```text
q^(3-4delta)=q^(2.486259399089...).                  (3.2)
```

At zero shift,

```text
R_A(0)-N_I^2/q=V_I(q).
```

If `N_I` has its conjectural scale `q/(log q)^2`, the square of this term is
`q^2/(log q)^4`, below (3.2).  The diagonal therefore does not refute (0.4).

What blocks the standard sieve step is the centering.  For nonzero `s`,
`R_A(s)` counts two cousin-pair lower endpoints in prescribed residue
difference classes.  Away from overlaps this is a four-prime pattern.
An upper-bound sieve estimates the positive count `R_A(s)` but does not prove
that it lies near the unknown baseline `N_I^2/q`; discarding the subtraction
returns only logarithmic savings.  So (3.1) identifies a live, substantially
stronger theorem rather than proving it.

---

## 4. Exact Buchstab bilinearization

Let `P^-(m)` be the least prime factor of `m`, with `P^-(1)=infinity`, and
take `3<=z<sqrt(Y)`.  For every integer `M` near `Y`, the least-prime-factor
partition gives the pointwise identity

```text
1_(M prime)
 =1_(P^-(M)>=z)
  -sum_(z<=r<=sqrt(M), r prime, r|M)
       1_(P^-(M/r)>=r).                              (4.1)
```

Indeed, a composite surviving the first term has a unique least prime
factor `r>=z`, and is removed exactly once.

Apply (4.1) to `M=p+4`, while retaining `p` prime.  With

```text
S_z(I;q)=sum_(p prime in I, P^-(p+4)>=z)
             chi_4(p)e(p/(4q)),
```

we obtain

```text
S_4(I;q)=S_z(I;q)
 -e(-1/q) sum_(r,m)
    chi_4(r)chi_4(m)e(rm/(4q))                       (4.2)
```

where the second sum has the exact conditions

```text
r prime, z<=r<=sqrt(p+4), m>=r,
rm-4 in I and prime, P^-(m)>=r.                      (4.3)
```

The phase transformation in (4.2) is exact because `r,m` are odd and

```text
chi_4(rm-4)=chi_4(rm)=chi_4(r)chi_4(m),
e((rm-4)/(4q))=e(-1/q)e(rm/(4q)).                   (4.4)
```

This is the strongest clean bilinear identity found in the direct attack.
It also displays the parity boundary: `S_z` and the subtraction are
individually much larger sieve objects whose exact difference reconstructs
the second prime indicator.

### The first Cauchy zero mode

In a dyadic prime-factor sector write

```text
Gamma_r(m)=1_(rm-4 in I and prime) 1_(P^-(m)>=r),
T_R=sum_(r asyp R) chi_4(r)
       sum_m chi_4(m)Gamma_r(m)e(rm/(4q)).           (4.5)
```

Cauchy in `r`, followed by an exact expansion, gives

```text
|T_R|^2
 <=#R sum_(r asyp R) |sum_m chi_4(m)Gamma_r(m)e(rm/(4q))|^2

 =#R sum_(m_1,m_2) chi_4(m_1m_2)
      sum_(r asyp R) Gamma_r(m_1)Gamma_r(m_2)
        e(r(m_1-m_2)/(4q)).                          (4.6)
```

The literal zero mode is

```text
#R sum_(r,m) Gamma_r(m),                             (4.7)
```

with no `q`-oscillation.  Every off-diagonal in (4.6) contains two coupled
shifted primes `rm_1-4`, `rm_2-4`.  Replacing `Gamma_r(m)` by separated
coefficients would be a new arithmetic theorem, not a consequence of
Buchstab's identity.

The same issue appears under an exact Vaughan decomposition.  For `x>U`,

```text
Lambda(x)
 =(mu_<=V * log)(x)
  -(mu_<=V * 1 * Lambda_<=U)(x)
  +(mu_>V * 1 * Lambda_>U)(x).                       (4.8)
```

Applying (4.8) to both `Lambda(n)` and `Lambda(n+4)` creates multilinear
forms whose reconstructed products differ by exactly `4`.  A Cauchy
diagonal removes the bilinear phase, and an off-diagonal retains a shifted
prime correlation.  Heath--Brown's longer identity changes the number and
ranges of factors but not that product-difference constraint.

Therefore the answer to the requested fail-fast test is:

```text
exact Buchstab/Heath--Brown bilinear phase exposed:  YES
separated coefficient to which q^(-1/8) applies:     NO
unconditional q^(-1/8-eta_req) from this route:      NO
actual selected coefficient disproved:               NO
```

---

## 5. What `H=q` means arithmetically

For a cousin pair above `3`, reduction modulo `3` forces

```text
p=1 (mod 3).
```

Since `p` is odd, only two classes remain:

```text
chi_4(p)=+1  iff p=1 (mod 12),
chi_4(p)=-1  iff p=7 (mod 12).                       (5.1)
```

Across an interval of length `H`, the slow phase `e(p/(4q))` traverses an
arc of angular width at most

```text
pi H/(2q).                                           (5.2)
```

Thus at `H=q` the selected theorem is, up to a quarter-turn modulation, a
power-saving discrepancy between cousin pairs in the two classes in (5.1).
This is much stronger than a twin-sieve upper bound.

The exact prefix statement is useful for scope.  Put

```text
D(t)=sum_(p in P_I, p<=t) chi_4(p).
```

Partial summation gives

```text
|S_4(I;q)|
 <=(1+pi H/(2q)) sup_(t in I)|D(t)|.                (5.3)
```

Conversely, a uniform bound for every twisted prefix gives the same estimate
for `D` with the same factor.  Hence a prefix-uniform mod-`12` discrepancy
theorem would solve the endpoint.

A single full-block value of `S_4`, however, does not control the unweighted
imbalance `D(sup I)`: freezing the slow phase costs `O(N_I)` at `H=q`, much
larger than the desired power-saving target.  This distinction prevents an
overstatement of the reduction.

There is a rigorous coefficient-blind countermodel, but not an arithmetic
one.  On an interval of length `q`, retain all integers `n=1 (mod 12)`.
Then `n,n+4` avoid the local primes `2,3`, all signs in (5.1) are positive,
and their slow phases lie in an arc shorter than `pi/2`; consequently the
selected sum has magnitude at least `N/sqrt(2)`.  This proves that local
admissibility, total mass, and the `L2` diagonal alone do not force
cancellation.  It is **not** a counterexample satisfying a complete
prime-producing Type-I/Type-II axiom system, and it says nothing against the
actual primes.

---

## 6. Why prefix estimates do not localize for free

A global estimate for a prefix of length `Y`, even if it had a factor
`q^(-delta)`, gives after differencing two endpoints an error of size
`Yq^(-delta)`, not `Hq^(-delta)`.  Here `H<=Y^(33/133)`, so the lost factor
`Y/H` is a power.  Smooth localization has the same issue unless one already
has a short-interval theorem uniform in the translated cutoff.

This is visible in the primary short-interval literature.  Kawada's 1993
Theorem 2 treats prime `k`-tuples in arithmetic progressions, but:

```text
it sums q<=Q, maximizes the residue, and averages the shift vector b;
it assumes y>x^(2/3)(log x)^C;
it has Q<=y x^(-1/2)(log x)^(-B).                    (6.1)
```

At `y=H=Y^.24812...`, the last range is empty at power scale, and the fixed
shift `4` is one member of the averaged shift family.  Kawada therefore does
not localize to this gate.

---

## 7. Primary-literature quantifier audit

The following sources were checked at theorem level.

1. Kawada,
   [*The prime k-tuplets in arithmetic progressions*](https://tsukuba.repo.nii.ac.jp/records/15690),
   Theorems 1--2, proves a Bombieri--Vinogradov-type average over moduli and
   tuple shifts.  Its short interval begins above `x^(2/3)` and satisfies
   (6.1).  It permits the selected shift and modulus here to be exceptional.

2. Mikawa,
   [*On prime twins in arithmetic progressions*](https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf),
   proves a strong dispersion theorem after averaging the modulus and the
   prime-pair shift.  It does not retain shift `4` and one height-selected
   `q`.

3. Green--Tao,
   [*Restriction theory of the Selberg sieve, with applications*](https://arxiv.org/abs/math/0405581),
   controls an `L^p` frequency norm for prime-tuple exponential sums.  It
   allows exceptional individual frequencies; Bernstein localization of the
   norm returns only logarithmic saving.

4. Matomäki--Radziwiłł--Tao,
   [*Correlations of the von Mangoldt and higher divisor functions I*](https://arxiv.org/abs/1707.01315),
   obtains the expected correlation for almost all shifts in long shift
   ranges.  The single shift `4` may be exceptional and there is no selected
   additive twist.

5. Akeno,
   [*On the level of distribution of Goldbach primes and its applications*](https://arxiv.org/abs/2606.29559),
   is a relevant 2026 advance.  Theorem 2.1 averages `d asyp D` and every
   additive residue `b (mod d)` on a full scale `X`; Theorem 1.1 holds for all
   but an exceptional set of Goldbach totals `N`.  The diagonal slice
   `p_2-p_1=4`, one short interval, and one selected `q` are not consequences.

6. Matomäki,
   [*A Bombieri--Vinogradov type exponential sum result with applications*](https://doi.org/10.1016/j.jnt.2009.01.010),
   supplies a power-saving rational-phase theorem for well-factorable sieve
   surrogates on a full dyadic scale.  It neither localizes to `H` nor replaces
   the surrogate by the signed exact shifted-prime indicator.

7. Murty--Vatwani,
   [*Twin primes and the parity problem*](https://mast.queensu.ca/~murty/TwinPrimes-Parity.pdf),
   makes the missing shifted-prime/Möbius equidistribution an additional
   conjecture.  It is not an unconditional input.

8. Ford--Maynard,
   [*On the theory of prime producing sieves*](https://arxiv.org/abs/2407.14368),
   gives genuine counterexamples for general nonnegative sequences satisfying
   specified Type-I/Type-II information.  It rules out inferring parity-
   sensitive conclusions from unspecified sieve axioms.  It does not state a
   no-go theorem for the actual signed short-block coefficient (0.1), nor was
   a specialization preserving this selected mod-`12` Fourier statistic
   located.

The exact literature verdict is therefore:

```text
fixed shift 4:                         required, not averaged
one selected q and numerator:          required, not averaged
one H=Y^.248... curvature block:       required, not a full prefix
centered four-cousin energy (0.4):      not found
published theorem ruling out (0.1):    not found
```

---

## 8. Reproduction and truth boundary

Run

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_fgf4_selected_q_dispersion.py
PYTHONPATH=src python3 \
  results/verify_zeta23_fgf4_selected_q_dispersion.py
```

The verifier checks:

- (0.2), (1.3), (2.1)--(2.3), and (3.1) on actual cousin primes;
- an exact `H<q` endpoint with no hidden same-residue off-diagonal;
- the pointwise Buchstab identity (4.1) and transformed bilinear phase (4.2);
- the expanded Cauchy energy and its literal zero mode;
- the exponent ledger (0.5), (2.6), (2.8), and (3.2);
- the explicitly scoped local-admissibility countermodel.

```text
near-quarter normalization (0.2):                    EXACT
selected difference identity (1.3):                  EXACT
centered L2 and q-shift ledger:                       EXACT
all-frequency L2 closes H=q target:                   NO
centered L4 identity and sufficient threshold:        EXACT
L4 diagonal proves impossibility:                     NO
one-step Buchstab bilinearization:                    EXACT
first-Cauchy zero/coupled modes:                      EXACT
q^(-1/8-eta_req) obtained:                            NO
coefficient-blind/local-admissibility countermodel:   PROVED
full sieve-axiom countermodel for actual coefficient: NOT CLAIMED
published fixed-shift selected-q theorem:             NOT FOUND
published no-go theorem for actual coefficient:       NOT FOUND
FGF4 selected cousin-prime sector:                    OPEN
whole q-first signed transition:                      OPEN
zero-free strip:                                      NOT CLAIMED
```
