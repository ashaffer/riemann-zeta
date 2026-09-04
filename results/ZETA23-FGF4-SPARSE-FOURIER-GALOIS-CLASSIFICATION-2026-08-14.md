# FGF4 sparse Fourier and cyclotomic classification

**Date:** 2026-08-14  
**Status:** unconditional finite classification theorem, with sharp equality
cases, stability, an exact verifier, and a scoped no-go consequence.  This
does not estimate the actual cousin-prime coefficient and does not prove a
zero-free strip.

## Verdict

Let `q` be odd, let `a` be a unit modulo `q`, and let `A` be an `N`-subset
of `Z/qZ`.  Write

```text
Ahat(b)=sum_(r in A) e_q(br),
R_A(s)=#{(r,r') in A^2:r'-r=s},
C(A)=sum_(s mod q)(R_A(s)-N^2/q)^2.                 (0.1)
```

At the FGF4 endpoint, `a=(q+1)/4` and therefore `a^(-1)=4 (mod q)`.
The following exact theorem settles what sparsity and finite cyclic
classification can do by themselves.

1. **Sharp support-only extremum.**  For every `0<=N<=q`,

   ```text
   |Ahat(a)| <= D_q(N):=sin(pi N/q)/sin(pi/q).       (0.2)
   ```

   For `0<N<q`, equality holds exactly when `aA` is a cyclic interval of
   `N` consecutive residues.  Thus the extremizers in the original residue
   coordinate are modular arithmetic progressions of step `a^(-1)`.  In the
   FGF4 case their step is exactly `4`.

2. **Inverse race and stability.**  If

   ```text
   Delta_a(A)=max_J |#{r in A:ar in J}-N|J|/q|,     (0.3)
   ```

   where `J` ranges over cyclic intervals, then

   ```text
   |Ahat(a)| <= 4 Delta_a(A).                        (0.4)
   ```

   Hence a selected coefficient larger than `T` forces a discrepancy larger
   than `T/4` on a modular step-four progression interval.  If
   `theta=arg Ahat(a)`, then for every `0<rho<=pi`,

   ```text
   #{r in A:dist(2pi ar/q,theta)>=rho}
      <= (N-|Ahat(a)|)/(1-cos rho).                 (0.5)
   ```

   This gives a quantitative phase-arc classification of near extremizers.

3. **Exact centered-energy rigidity.**  Put

   ```text
   lambda=N(N-1)/(q-1),
   mu=N(q-N)/(q-1),
   C0=N^2(q-N)^2/[q(q-1)].                          (0.6)
   ```

   Then

   ```text
   C(A)-C0
    =sum_(s!=0)(R_A(s)-lambda)^2
    =(1/q)sum_(b!=0)(|Ahat(b)|^2-mu)^2.             (0.7)
   ```

   If `N(N-1)=(q-1)ell+t`, `0<=t<q-1`, then

   ```text
   C(A) >= C0+t(q-1-t)/(q-1),                       (0.8)
   C(A)-C0-t(q-1-t)/(q-1) in 2 Z_(>=0).             (0.9)
   ```

   Equality in (0.8) holds exactly when every nonzero difference occurs
   either `ell` or `ell+1` times, with exactly `t` occurrences of the latter.
   These are precisely the balanced cyclic almost-difference sets.  When
   `t=0`, equality means a cyclic difference set.  Equation (0.9) gives a
   literal stability gap: a non-extremizer pays at least `2` more energy.

4. **Prime-modulus Galois classification.**  Now suppose `q` is prime and
   `0<N<q`.  For a selected `b!=0`, put

   ```text
   E_b=|Ahat(b)|^2,
   H_b={k in (Z/qZ)^*:E_(kb)=E_b},
   h=|H_b|,                 d=(q-1)/h.              (0.10)
   ```

   Then

   ```text
   H_b={k:R_A(ks)=R_A(s) for every s},
   -1 in H_b,
   d=[Q(E_b):Q] and d divides (q-1)/2.              (0.11)
   ```

   The `d` Galois-conjugate nonzero Fourier energies occur on the
   multiplicative cosets of `H_b`, each with multiplicity `h`.  Moreover,

   ```text
   h | N(N-1),
   Tr_(Q(E_b)/Q)(E_b)=N(q-N)/h=d mu in Z,
   0<E_b<=d mu.                                     (0.12)
   ```

   The last inequality is strict for `d>1`.  In particular,

   ```text
   d >= (q-1)/gcd(q-1,N(N-1)).                      (0.13)
   ```

   If the gcd in (0.13) is `2`, then `H_b={+-1}`, `d=(q-1)/2`, and

   ```text
   E_b=E_c  iff  c=+-b.                             (0.14)
   ```

   Thus every nonzero Fourier energy is spectrally simple after the forced
   conjugation.  At the FGF4 primes `q=3 (mod 4)`, every possible `d` is odd.
   Finally, `d=1` if and only if `A` is a cyclic difference set; equivalently,
   one rational nonzero Fourier energy forces the whole nonzero spectrum to
   be flat.

5. **Degree-sensitive selected-energy penalty.**  For `d>1`, (0.7) and the
   multiplicity `h=(q-1)/d` give

   ```text
   C(A) >= C0+(q-1)/[q(d-1)] (E_b-mu)^2.            (0.15)
   ```

   Consequently a large selected coefficient is not merely one exceptional
   Fourier atom: it forces an entire cyclotomic orbit and a quantified
   autocorrelation-energy excess.

This is an exact and useful classification theorem built mostly from
classical ingredients.  It rules out low-cyclotomic-degree configurations as
possible obstructions, but it does not prove that the actual cousin-prime
spectrum has low degree.  Its definitive negative consequence is narrower:
support sparsity and local admissibility alone do not force the needed power
cancellation.  Any remaining counterconfiguration must have a large
step-four residue race, and at prime `q` it must typically have very high
cyclotomic degree.

---

## 1. Proof of the sharp sparse extremum

Let `zeta=e(1/q)` and rotate the selected sum into the positive real
direction.  If `theta=arg Ahat(a)`, then

```text
|Ahat(a)|=sum_(x in aA) cos(2pi x/q-theta).         (1.1)
```

Among the `q` sampled cosines, the `N` largest are attached to `N`
consecutive roots closest to `theta`.  The sum of any such consecutive block
is a geometric progression of modulus

```text
|1+zeta+...+zeta^(N-1)|=sin(pi N/q)/sin(pi/q).      (1.2)
```

Its projection in the direction `theta` is no larger than its modulus.  This
proves (0.2).  Equality in both selections forces `aA` to be the consecutive
block and `theta` to be its resultant direction.  Conversely every such
block attains (1.2).

For the stability statement, set
`psi_r=2pi ar/q-theta`, reduced to `[-pi,pi]`.  The exact identity

```text
N-|Ahat(a)|=sum_(r in A)(1-cos psi_r)               (1.3)
```

and Markov's inequality prove (0.5).

For (0.4), reorder the centered indicator by `j=ar`:

```text
f(j)=1_(j in aA)-N/q,             sum_j f(j)=0.
```

Let `F(u)=sum_(0<=j<=u)f(j)`.  Every `|F(u)|` is bounded by
`Delta_a(A)`.  Abel summation of (1.1) gives a weighted sum of the `F(u)`
against consecutive differences of one sampled cosine.  The total cyclic
variation of a cosine is at most `4`, proving (0.4).  Notice that this is a
selected-frequency inverse theorem: no average over `b` is introduced.

---

## 2. Proof of the exact energy classification

The zero shift is fixed:

```text
R_A(0)=N,                   sum_(s!=0)R_A(s)=N(N-1). (2.1)
```

The mean of the nonzero rows is therefore `lambda`.  Expanding the squares
around that mean, with the cross term deleted by (2.1), gives

```text
C(A)=C0+sum_(s!=0)(R_A(s)-lambda)^2.                (2.2)
```

Fourier orthogonality gives

```text
C(A)=(1/q)sum_(b!=0)|Ahat(b)|^4,
sum_(b!=0)|Ahat(b)|^2=N(q-N)=(q-1)mu.               (2.3)
```

Subtracting the square of the mean in (2.3) proves the spectral half of
(0.7).

For the integer refinement, distribute `N(N-1)` indistinguishable ordered
differences among `q-1` integer rows.  The sum of their squares is minimized
exactly when the rows differ by at most one, proving (0.8) and its equality
classification.  More explicitly,

```text
C(A)-C0-t(q-1-t)/(q-1)
 =sum_(s!=0)R_A(s)^2
  -[(q-1-t)ell^2+t(ell+1)^2].                      (2.4)
```

The right side is a nonnegative integer.  It is even because `x^2=x (mod 2)`
and both row vectors have the same sum.  This proves (0.9).

---

## 3. Proof of the cyclotomic orbit theorem

Let `zeta=e(1/q)`.  The energy is the cyclotomic integer

```text
E_b=sum_(s mod q)R_A(s)zeta^(bs).                  (3.1)
```

For `k in (Z/qZ)^*`, the Galois automorphism `sigma_k(zeta)=zeta^k`
sends `E_b` to `E_(kb)`.  If `E_(kb)=E_b`, reindexing (3.1) gives a rational
linear relation among all `q` powers of `zeta`.  Their only rational relation
is a constant multiple of
`1+zeta+...+zeta^(q-1)=0`.  The coefficient at shift zero is already zero,
so every coefficient is zero.  Hence

```text
E_(kb)=E_b  iff  R_A(ks)=R_A(s) for every s.        (3.2)
```

This proves the stabilizer description.  Since `R_A(-s)=R_A(s)`, it also
proves `-1 in H_b`.  The orbit--stabilizer theorem in the Galois extension
`Q(zeta)/Q` now gives

```text
[Q(E_b):Q]=[(Z/qZ)^*:H_b]=d.                       (3.3)
```

Every nonzero `H_b`-orbit has size `h`, and `R_A` is constant on it.  Summing
the nonzero correlations proves `h|N(N-1)`.  Alternatively, summing all
nonzero Fourier energies and grouping equal conjugates gives

```text
h Tr(E_b)=sum_(c!=0)E_c=N(q-N),                    (3.4)
```

which proves the trace formula and `h|N(q-N)`.

Every `E_c` is positive.  Indeed, if `Ahat(c)=0`, the `0/1` polynomial
`sum_(r in A)X^r` would be divisible by the prime cyclotomic polynomial
`1+X+...+X^(q-1)`, forcing `A` to be empty or all of `Z/qZ`.  Positivity and
(3.4) give the trace bound in (0.12), strict when another conjugate exists.

The divisibility `h|q-1` and `h|N(N-1)` proves (0.13).  Since `-1 in H_b`,
`h>=2`; therefore gcd `2` forces `H_b={+-1}` and proves (0.14).

When `d=1`, (3.2) makes `R_A` constant away from zero, exactly the difference
set condition.  Conversely a difference set has flat nonprincipal character
magnitudes.  Finally, the selected value `E_b` occurs `h=(q-1)/d` times.  If
`x_c=E_c-mu`, the other `q-1-h` deviations sum to `-h x_b`.  Cauchy's
inequality yields

```text
sum_(c!=0)x_c^2
 >=h x_b^2+h^2 x_b^2/(q-1-h)
 =(q-1)x_b^2/(d-1).                                (3.5)
```

Combining (3.5) with (0.7) proves (0.15).

---

## 4. Exact FGF4 consequences

### 4.1 What a failed selected bound would force

At the endpoint `H=q`, suppose

```text
|Ahat(a)|>q^(1-delta),              delta=.128435150228... .
```

Since `mu<=N`, the trace bound (0.12) forces

```text
d > q^(2-2delta)/N.                                (4.1)
```

At the cousin-pair model scale `N asymp q/(log q)^2`, (4.1) becomes

```text
d >> q^(.743129699545...)(log q)^2.                (4.2)
```

Thus a bad coefficient cannot come from a rational, quadratic, bounded-degree,
or even moderately growing cyclotomic spectrum.  It must occupy a very
high-degree Galois orbit.  This is a genuine classification, not a proof that
such an orbit cannot occur.

### 4.2 Why support sparsity still cannot close FGF4

For `N<=q/2`, (0.2) also gives the attained lower estimate

```text
D_q(N)>=N(1-pi^2 N^2/(6q^2)).                      (4.3)
```

Hence `D_q(N)=(1+o(1))N` whenever `N=o(q)`.  At
`N asymp q/(log q)^2`, this is much larger than `q^(1-delta)`:

```text
N/q^(1-delta) asymp q^delta/(log q)^2 -> infinity. (4.4)
```

There is also an exact sparse counterconfiguration respecting the elementary
cousin-pair local constraints.  Let `q=3 (mod 4)`, `3` not divide `q`, put
`a=(q+1)/4`, and take

```text
A_N={n_0+12j:0<=j<N},       n_0=1 (mod 12),
12(N-1)<q.                                           (4.5)
```

Every `n in A_N` and `n+4` avoids the local prime obstructions `2` and `3`,
and distinct lower endpoints never differ by `4`.  Yet `12a=3(q+1)`, so

```text
|Ahat(a)|=|sum_(j<N)e_q(3j)|
          =|sin(3pi N/q)/sin(3pi/q)|.              (4.6)
```

For `N=o(q)`, (4.6) is `(1+o(1))N`.  Taking
`N=floor(q/(log q)^2)` satisfies (4.5) for large `q` and violates the desired
power bound asymptotically.

This is **not** a counterexample made of actual cousin primes.  It proves the
sharply scoped no-go statement:

```text
sparsity + distinct residues + local admissibility at 2 and 3
+ exclusion of adjacent gap-four lower endpoints
does not force selected-frequency power cancellation.              (4.7)
```

The arithmetic theorem still missing is distribution of the actual
cousin-prime set across the step-four progression intervals (0.3), or an
upper bound for the centered correlation energy beyond these finite
classifications.

---

## 5. Literature and priority audit

The theorem above deliberately does not claim that its standard ingredients
are new.

1. Mönius, [*The algebraic degree of spectra of circulant graphs*](https://doi.org/10.1016/j.jnt.2019.08.002),
   determines algebraic degrees for prime-order circulant graphs, and the
   later [splitting-field paper](https://doi.org/10.1016/j.jalgebra.2021.11.036)
   gives the general stabilizer/fixed-field framework.  The Galois orbit in
   (0.10)--(0.14) is a direct specialization to the integer autocorrelation
   circulant.  It should not be advertised as a new Galois principle.

2. Jedwab--Li,
   [*Group rings and character sums: tricks of the trade*](https://arxiv.org/abs/2211.11986),
   gives the standard character-sum criterion for difference sets: flat
   nonprincipal character magnitude is equivalent to uniform nonzero
   differences.  This is the equality case `d=1` above.

3. Arasu--Ding--Helleseth--Kumar--Martinsen,
   [*Almost difference sets and their sequences with optimal autocorrelation*](https://doi.org/10.1109/18.959271),
   develops the almost-difference-set/three-level-autocorrelation theory.
   Thus the equality objects in the integer refinement (0.8) belong to an
   established literature.  The exact variance decomposition and parity-two
   stability gap here are elementary optimizations of that framework.

4. Tao,
   [*An uncertainty principle for cyclic groups of prime order*](https://arxiv.org/abs/math/0308286),
   proves the sharp support uncertainty theorem
   `|supp f|+|supp fhat|>=q+1`.  That result concerns support versus Fourier
   support; it does not bound one selected Fourier magnitude.  In particular,
   it does not contradict the coherent sparse extremizers (0.2).

5. The consecutive-root bound (0.2), the bounded-variation inverse (0.4),
   the trace identity (0.12), and the variance inequality (0.15) all have
   short self-contained proofs above.  No literature-priority claim is made
   for these elementary facts or for their packaging.  The contribution to
   this project is the exact FGF4 specialization: step `4`, the degree and gcd
   ledger, the equality/stability classification, and the locally admissible
   sparse no-go model.

No cited paper states a no-go theorem for the actual signed cousin-prime
coefficient.  Nothing here supplies one.

---

## 6. Reproduction and truth boundary

Run

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_fgf4_sparse_fourier_classification.py
PYTHONPATH=src python3 \
  results/verify_zeta23_fgf4_sparse_fourier_classification.py
```

The eight unit tests and independent verifier check:

- (0.2) and all equality cases exhaustively for small odd prime moduli;
- (0.4), (0.5), and the FGF4 inverse step `a^(-1)=4`;
- (0.7)--(0.9), including exact rational energy and the parity-two gap;
- the `(7,3,1)` Paley difference-set equality case;
- the Galois stabilizer, degree, trace, gcd, and spectral simplicity for a
  generic three-subset modulo `11`;
- the degree-sensitive energy penalty (0.15);
- the exact local model (4.5)--(4.6);
- the endpoint degree exponent `.743129699545...`.

```text
sharp support extremum and equality classification: PROVED
large selected coefficient => step-four residue race: PROVED
centered energy rigidity and integer stability gap:  PROVED
prime-q Galois degree/trace/gcd classification:       PROVED
low-degree bad selected coefficient possible:         NO
high-degree bad selected coefficient ruled out:       NO
sparsity/local admissibility alone closes FGF4:        NO
actual cousin-prime selected coefficient estimated:   NO
FGF4 centered-L4 arithmetic gate:                      OPEN
zero-free strip:                                      NOT CLAIMED
```
