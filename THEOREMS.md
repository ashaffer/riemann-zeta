# Theorems

Proved statements extracted from this program's measurements. House standard:
every constant explicit, every proof complete or explicitly labeled
computer-assisted with its trust base; novelty claims carry the same diligence
caveats as everything else in this repository ("new as stated, pending
literature check" — the frontier corpus is Connes–Consani(–Moscovici), Suzuki,
Groskin; see `PROGRAM.md` §7).

Throughout, for L > 0 put a = L/4 and let H_L be the real Hilbert space
L²([−a, a]), extended by zero to ℝ. For φ ∈ H_L set

  φ̂(r) = ∫ φ(x) e^{−irx} dx,     ψ_φ(u) = ∫ φ(x) φ(x+u) dx,

  P(φ)  = 2 (∫ φ(x) e^{x/2} dx)(∫ φ(x) e^{−x/2} dx)                 (pole)
  A(φ)  = (1/2π) ∫_ℝ |φ̂(r)|² ( Re ψ(1/4 + ir/2) − log π ) dr        (archimedean)
  Π(φ)  = 2 Σ_{n ≥ 2 prime power} Λ(n) n^{−1/2} ψ_φ(log n)          (primes)

  Q_L(φ) = P(φ) + A(φ) − Π(φ),        λ(L) = inf { Q_L(φ) : ‖φ‖₂ = 1 }.

Since ψ_φ(u) = 0 for |u| ≥ 2a = L/2, the prime sum is the finite sum over
n < e^{L/2}: Q_L is precisely the truncated Weil form of the certified ledger
(`PROGRAM.md` §6), and Weil's criterion says: RH ⟺ λ(L) ≥ 0 for all L.
All measurements of λ(L) in `results/RESULTS.md` are Galerkin upper bounds for
these quantities. ψ denotes the digamma function; ψ(1/4) = −γ − π/2 − 3 log 2.

---

## Lemma A (archimedean kernel bounds)

For all real r:

 (i) Re ψ(1/4 + ir/2) − ψ(1/4)
     = ∫₀^∞ e^{−t/4} (1 − cos(rt/2)) / (1 − e^{−t}) dt ≥ 0;

 (ii) Re ψ(1/4 + ir/2) ≥ ψ(1/4) + ½ log(1 + 4r²);

 (iii) | r · d/dr Re ψ(1/4 + ir/2) | ≤ 2 + π/2 < 4;

 (iv) Re ψ(1/4 + ir/2) ≤ ψ(1/4) + ½ log(1 + 4r²) + 8.

**Proof.** (i) Gauss's formula ψ(z) = ∫₀^∞ [e^{−t}/t − e^{−zt}/(1−e^{−t})] dt
(Re z > 0; Whittaker–Watson §12.3). Subtracting the values at z = 1/4 + ir/2
and z = 1/4, the e^{−t}/t terms cancel, and Re e^{−(1/4+ir/2)t} =
e^{−t/4} cos(rt/2); the integrand of the difference is
e^{−t/4}(1 − cos(rt/2))/(1−e^{−t}) ≥ 0, and the integral converges absolutely
(integrand ≤ min(Ct r², 2/(1−e^{−t}) ) near 0 and ∞ respectively).

(ii) For t > 0, e^t ≥ 1 + t gives 1 − e^{−t} ≤ t, so (1−e^{−t})^{−1} ≥ 1/t.
Hence the integral in (i) is at least ∫₀^∞ e^{−t/4}(1−cos(rt/2)) dt/t
= ½ log(1 + (r/2)²/(1/4)²) = ½ log(1+4r²), by the classical evaluation
∫₀^∞ e^{−at}(1−cos bt) dt/t = ½ log(1 + b²/a²) (differentiate in b:
∫₀^∞ e^{−at} sin(bt) dt = b/(a²+b²); integrate from 0 to b).

(iii) d/dr Re ψ(1/4+ir/2) = Re[(i/2) ψ′(1/4+ir/2)] and ψ′(z) = Σ_{n≥0}(z+n)^{−2},
so with z = 1/4 + ir/2:
|ψ′(z)| ≤ Σ_{n≥0} ((n+1/4)² + r²/4)^{−1}
        ≤ (1/16 + r²/4)^{−1} + ∫₀^∞ ((t+1/4)² + r²/4)^{−1} dt
        = 16/(1+4r²) + (2/|r|) arctan(2|r|)
(the sum over n ≥ 1 is compared with the integral of the decreasing integrand).
Multiplying by |r|/2: |r| · 8/(1+4r²) ≤ 2 (maximum at |r| = 1/2), and
(|r|/2)(2/|r|) arctan(2|r|) = arctan(2|r|) < π/2. Total < 2 + π/2.
(Measured maximum over a wide grid: 2.078 — the bound is comfortable.)

(iv) For t > 0, e^t − 1 ≥ t gives (1−e^{−t})^{−1} = 1 + (e^t−1)^{−1} ≤ 1 + 1/t,
so the integral in (i) is at most ½log(1+4r²) + ∫₀^∞ e^{−t/4}·2 dt
= ½log(1+4r²) + 8. (Measured supremum of the slack: 2.8412.) ∎

*Remark.* (ii) and (iv) sandwich the archimedean weight between
½log(1+4r²) + ψ(1/4) and the same plus 8 — the entire theorem below runs on
this two-sided log-control, which is elementary and self-contained.

---

## Lemma B (a priori bounds on near-minimizers)

Fix 0 < ℓ₀ ≤ L ≤ ℓ₁ and ‖φ‖₂ = 1, φ ∈ H_L. Write κ₀ = ψ(1/4) − log π
(κ₀ > −5.38) and define the log-weighted energy

  W₊(φ) = (1/2π) ∫ |φ̂(r)|² · ½ log(1+4r²) dr ≥ 0.

Then, with C_P = 4 sinh(ℓ₁/4) and C_Π = 2 ℓ₁ e^{ℓ₁/4}:

 (i) |P(φ)| ≤ C_P and |Π(φ)| ≤ C_Π;
 (ii) A(φ) ≥ κ₀ + W₊(φ);
 (iii) λ(L) ≤ C_λ(ℓ₀), an explicit constant depending only on ℓ₀ (below);
 (iv) if Q_L(φ) ≤ λ(L) + 1 then W₊(φ) ≤ C_B, where
      C_B := C_λ(ℓ₀) + 1 + C_P + C_Π + 5.38;
 (v) for R ≥ 1: (1/2π) ∫_{|r|>R} |φ̂|² dr ≤ C_B / (½ log(1+4R²)) ≤ 2C_B/ log(2R).

**Proof.** (i) By Cauchy–Schwarz |∫φ e^{±x/2}| ≤ (∫_{−a}^{a} e^{±x} dx)^{1/2}
= (2 sinh a)^{1/2}, so |P| ≤ 2·2 sinh a ≤ C_P. For the primes, |ψ_φ(u)| ≤ 1
(Cauchy–Schwarz again) and Λ(n) ≤ log n ≤ L/2 for the participating n, so
|Π| ≤ 2·(ℓ₁/2)·Σ_{n ≤ e^{ℓ₁/2}} n^{−1/2} ≤ ℓ₁ · 2 e^{ℓ₁/4} = C_Π,
using Σ_{n≤N} n^{−1/2} ≤ 2√N.

(ii) Lemma A(ii) plus Plancherel ((1/2π)∫|φ̂|² = ‖φ‖² = 1).

(iii) Monotonicity (Theorem 1, step 1 — proved without this clause) gives
λ(L) ≤ λ(ℓ₀), so it suffices to exhibit one unit test function at ℓ₀. Take
φ₀ = (2a₀)^{−1/2} 1_{[−a₀,a₀]}, a₀ = ℓ₀/4, whose transform satisfies
|φ̂₀(r)|² = 2 sin²(a₀ r)/(a₀ r²). Using sin² ≤ min(a₀²r², 1) and Lemma A(iv):

  W₊(φ₀) ≤ (1/2π)[ ∫_{|r|≤1/a₀} (2a₀/2π-free) … ]  — explicitly,
  W₊(φ₀) ≤ (a₀/π) ∫₀^{1/a₀} log(1+4r²) dr + (1/π a₀) ∫_{1/a₀}^∞ log(1+4r²) r^{−2} dr
        ≤ (1/π) log(1 + 4/a₀²) + (1/π)[ log(1+4/a₀²) + 4 a₀ arctan-term ]
        ≤ (2/π) log(1 + 4/a₀²) + 2,

  where the second integral was integrated by parts:
  ∫_{1/a₀}^∞ log(1+4r²) r^{−2} dr = a₀ log(1+4/a₀²) + 8∫_{1/a₀}^∞ (1+4r²)^{−1} dr
  ≤ a₀ log(1+4/a₀²) + 2π a₀.
  Hence A(φ₀) ≤ κ₀ + 8 + W₊(φ₀), and
  C_λ(ℓ₀) := 4 sinh(ℓ₀/4) + κ₀ + 8 + (2/π) log(1+64/ℓ₀²) + 2 + 2ℓ₀ e^{ℓ₀/4}
  bounds Q_{ℓ₀}(φ₀) (the prime term bounded as in (i) at ℓ₀).

(iv) W₊ ≤ A − κ₀ = Q_L − P + Π − κ₀ ≤ (λ(L)+1) + C_P + C_Π + |κ₀|.

(v) On |r| > R the weight ½log(1+4r²) exceeds ½log(1+4R²) ≥ log(2R) − c with
½log(1+4R²) ≥ ½log(4R²) = log(2R); Chebyshev. ∎

---

## Lemma C (no concentration on short intervals)

Let ‖φ‖ = 1 with W₊(φ) ≤ C_B, and let J ⊂ ℝ be an interval of length ε ≤ 1.
Then

  ∫_J φ² ≤ 2√ε + 4 C_B / log(1/ε)   ( ≤ C_C / log(1/ε) with C_C = 2 + 4C_B,
                                       for all 0 < ε ≤ 1, since √ε·log(1/ε) ≤ 2/e < 1 ).

**Proof.** Split φ = φ_R + φ^R at frequency R: φ_R = (2π)^{−1}∫_{|r|≤R} φ̂ e^{irx} dr.
Then ‖φ_R‖_∞ ≤ (2π)^{−1} ∫_{|r|≤R}|φ̂| ≤ (2π)^{−1}(2R)^{1/2}(∫|φ̂|²)^{1/2}
= (R/π)^{1/2}, and ‖φ^R‖² ≤ 2C_B/log(2R) by Lemma B(v). Hence
∫_J φ² ≤ 2 ∫_J φ_R² + 2‖φ^R‖² ≤ 2εR/π + 4C_B/log(2R). Choose R = ε^{−1/2}:
2√ε/π + 4C_B/log(2ε^{−1/2}) ≤ 2√ε + 4C_B/log(1/ε). ∎

## Lemma D (translation modulus of the autocorrelation)

Under the hypotheses of Lemma C, for all u, u′ with |u − u′| ≤ 1:

  |ψ_φ(u) − ψ_φ(u′)| ≤ √|u−u′| + 4 C_B / log(1/|u−u′|) ≤ C_C / log(1/|u−u′|).

**Proof.** ψ_φ(u) = (2π)^{−1}∫ |φ̂(r)|² e^{iru} dr (Wiener–Khinchin; both sides
continuous, φ ∈ L¹∩L²), so with Δ = |u−u′|,
|ψ_φ(u) − ψ_φ(u′)| ≤ (2π)^{−1}∫ |φ̂|² min(2, |r|Δ) dr
≤ Δ·R·(2π)^{−1}∫_{|r| ≤ R}|φ̂|² + 2·(2π)^{−1}∫_{|r|>R}|φ̂|²
≤ ΔR + 4C_B/log(2R); take R = Δ^{−1/2} as in Lemma C. ∎

## Lemma E (edge bound: the entering prime is weakly coupled)

Under the hypotheses of Lemma C, if supp φ ⊂ [−a, a] and 0 ≤ 2a − u = ε ≤ 1:

  |ψ_φ(u)| ≤ ( C_C / log(1/ε) )^{1/2}.

**Proof.** ψ_φ(u) = ∫_{−a}^{a−u} φ(x)φ(x+u) dx; the integration variable ranges
over an interval of length ε. By Cauchy–Schwarz,
|ψ_φ(u)| ≤ (∫_{−a}^{−a+ε} φ²)^{1/2} · ‖φ‖ and Lemma C applies to the sliver. ∎

---

## Theorem 1 (monotonicity and the glide: λ is continuous through prime-power thresholds)

Let 0 < ℓ₀ ≤ L ≤ L′ ≤ ℓ₁ with h := L′ − L ≤ min(1/2, ℓ₀/2, 1/e). Then:

 (1) **Monotonicity.**  λ(L′) ≤ λ(L).

 (2) **Modulus.**  λ(L) − λ(L′) ≤ C_glide(ℓ₀, ℓ₁) · ( log(1/h) )^{−1/2},

with the explicit constant

  C_glide = 16/ℓ₀ + C_P′ + C_Π C_C + (1 + e^{ℓ₁/2} ) ℓ₁ √C_C,
  C_P′    = 4 e^{ℓ₁/4} (2 + ℓ₁/4) √(ℓ₁) ,

C_B, C_C as in Lemmas B–C (all depending only on ℓ₀, ℓ₁). In particular λ is
continuous on (0, ∞) — including at every prime-power threshold L = 2 log n —
and lim_{L′ ↓ 2 log n} λ(L′) = λ(2 log n): **the entry of a new prime produces
no jump in the margin.**

**Proof.**

*Step 1 (monotonicity).* Let φ be a unit near-minimizer at L: Q_L(φ) ≤ λ(L)+η.
Extend φ by zero to H_{L′}. The pole and archimedean terms do not involve L.
Every prime power n that participates at level L′ but not at L has
log n ≥ L/2 = 2a, hence ψ_φ(log n) = 0 by support. Therefore
Q_{L′}(φ) = Q_L(φ) ≤ λ(L) + η, so λ(L′) ≤ λ(L) + η for all η > 0.

*Step 2 (contraction of a near-minimizer at L′).* Let φ′ be a unit
near-minimizer at L′: Q_{L′}(φ′) ≤ λ(L′) + η. Note λ(L′) ≤ λ(ℓ₀) ≤ C_λ(ℓ₀)
(Step 1 and Lemma B(iii)), so Lemma B(iv) applies to φ′ (for η ≤ 1):
W₊(φ′) ≤ C_B. Set s = L′/L ∈ (1, 1 + h/ℓ₀] and
φ_s(x) = s^{1/2} φ′(sx), a unit vector of H_L. We compare Q_L(φ_s) with
Q_{L′}(φ′) term by term; note ψ_{φ_s}(u) = ψ_{φ′}(su) and
φ̂_s(r) = s^{−1/2} φ̂′(r/s).

*(2a: archimedean.)* A(φ_s) − A(φ′) = (1/2π)∫|φ̂′(ρ)|² [W(sρ) − W(ρ)] dρ where
W(r) = Re ψ(1/4+ir/2) − log π. By Lemma A(iii), |W(sρ) − W(ρ)| =
|∫_{log ρ}^{log ρ + log s} (d W/d log r) d log r| ≤ 4 log s ≤ 4h/L ≤ 4h/ℓ₀.
Hence |A(φ_s) − A(φ′)| ≤ 4h/ℓ₀. (This also shows W₊(φ_s) ≤ C_B + 4 log s + …;
we only use W₊(φ′) ≤ C_B below, applied to ψ_{φ′}.)

*(2b: pole.)* ∫φ_s e^{±x/2} dx = s^{−1/2} ∫ φ′(y) e^{±y/(2s)} dy. For
y ∈ [−a′, a′], |e^{±y/(2s)} − e^{±y/2}| ≤ e^{a′/2}·(a′/2)(1 − 1/s) ≤
e^{ℓ₁/8}(ℓ₁/8)(h/L), and |s^{−1/2} − 1| ≤ h/(2L). Combining with
Cauchy–Schwarz (each factor ≤ (2 sinh a′)^{1/2} ≤ e^{ℓ₁/8}√(ℓ₁/2) in absolute
value, and each error term ≤ √(2a′)·e^{ℓ₁/8}(ℓ₁/8)(h/ℓ₀) + (h/2ℓ₀)·(2 sinh a′)^{1/2}):
|P(φ_s) − P(φ′)| ≤ C_P′ · h / ℓ₀ with C_P′ as displayed (a generous but
explicit collection of the four cross terms).

*(2c: incumbent primes.)* For prime powers n with log n < 2a (participating at
both levels), the coefficients differ by
|ψ_{φ_s}(log n) − ψ_{φ′}(log n)| = |ψ_{φ′}(s log n) − ψ_{φ′}(log n)|,
and (s−1) log n ≤ (h/L)(L/2) = h/2 < 1, so by Lemma D each differs by at most
C_C / log(2/h). Summing against 2ΣΛ(n)n^{−1/2} ≤ C_Π (Lemma B(i)):
total incumbent error ≤ C_Π C_C / log(2/h).

*(2d: departing primes.)* Prime powers with 2a ≤ log n < 2a′ participate at L′
but not at L (for φ_s their coefficient vanishes by support). Each satisfies
2a′ − log n ≤ 2a′ − 2a = h/2 =: ε-range, so by Lemma E,
|ψ_{φ′}(log n)| ≤ (C_C / log(2/h))^{1/2}. The number of prime powers in
[e^{L/2}, e^{L′/2}) is at most e^{ℓ₁/2} h/2 + 1 ≤ e^{ℓ₁/2} + 1 (h ≤ 1/2 — 
crudely, an interval of length e^{L'/2}−e^{L/2} ≤ e^{ℓ₁/2}h/2 contains at most
that many integers plus one), and each carries weight 2Λ(n)n^{−1/2} ≤ ℓ₁.
Total: ≤ (1 + e^{ℓ₁/2}) ℓ₁ (C_C)^{1/2} (log(2/h))^{−1/2}.

*Step 3 (assembly).* λ(L) ≤ Q_L(φ_s) ≤ Q_{L′}(φ′) + [2a] + [2b] + [2c] + [2d]
≤ λ(L′) + η + C_glide (log(1/h))^{−1/2}, since (log(2/h))^{−1} ≤ (log(1/h))^{−1}
and h-linear terms are absorbed: h ≤ (log(1/h))^{−1/2} for h ≤ 1/e. Let η → 0.
With Step 1, 0 ≤ λ(L) − λ(L′) ≤ C_glide (log(1/h))^{−1/2}. ∎

**Corollary (the glide).** At every prime-power threshold L₀ = 2 log n₀ the
margin is continuous from both sides, and the newly entering prime's influence
switches on with coefficient O((log(1/(L−L₀)))^{−1/2}). There is no local
knife-edge in λ at thresholds: any d^κ-type collapse observed in a fixed
finite basis is a property of the basis, not of the form. (Measured
counterpart: `results/RESULTS.md`, threshold glide table; the measured
crossing ratio 0.973 vs. the envelope law's 0.968.)

**Honesty note.** The modulus (log 1/h)^{−1/2} is enormously weaker than the
measured smoothness (the envelope law is C^∞-like in L). The theorem's content
is the *absence of a jump* with an explicit modulus — it does not prove the
envelope law. All constants are explicit but generous; no attempt was made to
optimize.

**Novelty status.** We have not found a continuity-in-support statement for
the truncated Weil form's margin in the frontier corpus; experts may regard it
as folklore-provable. The proof technique (log-weight from Lemma A(ii) as a
substitute for compactness) is elementary. Claimed as: new as stated, pending
literature check.

---

## Theorem 2 (a machine-checked window of Weil positivity)

Let mRat ∈ ℚ^{12×12} be the explicit rational matrix of `lean/weilcert/`
(entries a_{ij}/10^{24} with the integers a_{ij} listed in the Lean source),
and δ = 10^{−20}. Then — **verified by the Lean 4 kernel, axioms
`[propext, Classical.choice, Quot.sound]` only, no `native_decide`, no floats:**

  for every M ∈ ℚ^{12×12} with |M_{ij} − mRat_{ij}| ≤ δ entrywise and every
  0 ≠ x ∈ ℚ^{12}:   xᵀ M x > 0.

(`WeilCert.weil_window_positive`; the certificate is an integer congruence
c² B = Wᵀ diag(g) W with B = 10^{24}·mRat − 120000·I, Winv·W = f·I, g > 0,
all verified by kernel computation; positivity propagates to M through an
exact ℚ Cauchy–Schwarz perturbation bound. By continuity of quadratic forms
the same conclusion holds for every real symmetric M in the same entrywise
ball.)

## Bridge Proposition (computer-assisted, trust base stated)

Let Q ∈ ℝ^{12×12} be the matrix of the truncated Weil form Q_{L} at
L = 497/200 in the basis b_k(x) = P_k(4x/L) (unnormalized Legendre
polynomials, k = 0..11) of test functions supported in [−L/4, L/4] — the
support window in which the prime powers 2 and 3 participate. Then

  |Q_{kj} − mRat_{kj}| ≤ 10^{−20}   for all k, j.

**Proof (computer-assisted).** The entries reduce exactly (`src/certified_spectral.py`,
derivation in `PROGRAM.md` §2.14–2.16) to
  ψ(1/4)·G + [exact rationals: the 1/(2u)-part of the kernel integral against
  the universal polynomials F_kj] + [Bernoulli-series part with remainder
  |g_r| ≤ 250/π^{r+1}, summed against exact rational moments] + [geometric
  tail of ∫_U^∞ e^{−u/2}(1−e^{−2u})^{−1}] + [pole: 2a·i_k(a/2) by the
  positive-term modified-spherical-Bessel series with geometric tail] −
  [primes: 2 Λ(n) n^{−1/2} · a F_kj(log n / a) over the prime powers
  n < e^{L/2} = e^{1.2425} ≈ 3.465, i.e. n ∈ {2, 3}] + [conductor −log π · G],
with every series remainder enclosed by the stated rigorous geometric bounds
and all arithmetic performed in 220-bit outward-rounded interval arithmetic
(mpmath.iv). Measured enclosure widths: ≤ 5·10^{−60} per entry; rounding to
the 10^{−24} grid contributes ≤ 5·10^{−25}. Trust base: the mpmath.iv
enclosures of exp, log, π, γ and directed rounding. Artifacts: the generating
script and the emitted integer data are in the repository; independent
cross-checks include exact agreement of the F_kj polynomials with a separately
implemented Gauss–Legendre overlap engine, the hp hat-basis pipeline, the
zero-side explicit-formula inequality, and the interval Rayleigh bound.  ∎

**Corollary (interpretation).** The truncated Weil form of ζ at support
L = 497/200 is strictly positive on the explicit 12-dimensional space
span{P_k(4x/L)}_{k≤11} ⊂ H_L: a finite, formally verified piece of the
RH-equivalent positivity criterion, in a window where the archimedean-plus-pole
part alone is *not* positive (deficit −0.41 at the window top; the rescue
requires both primes 2 and 3). The remaining gap between Theorem 2 and a fully
formal statement about ζ itself is exactly the Bridge Proposition; its
formalization requires interval-verified special functions in mathlib
(Bernoulli generating series — present; Gauss's digamma integral and directed-
rounded evaluation — absent), and is, to our knowledge, the concrete shortest
path to the first end-to-end formal window of Weil positivity.

**Novelty status.** Finite positivity computations for truncated Weil forms
exist in the literature (Connes–Consani; Groskin, arXiv:2605.20224,
arXiv:2607.02828, at far greater numerical depth). What we believe is new here
is the *kernel-checked* certificate: a formally verified positivity window
with an explicitly stated, independently reproducible bridge. Pending
literature check, as always.

---

## Provenance

Theorem 1 was found by proving what the July 25 "threshold glide" measurement
demanded (`PROGRAM.md` §2.17); Lemma A(ii) crystallized from the x-space
kernel identity of §2.14. Theorem 2 executes the first rung of Track A's
Curry–Howard ladder (§4, Track A) at the p = 3 window. The Lean development
(~750 lines including data) compiles in ~10 s against mathlib (Lean 4.32.1);
`#print axioms` output is reproduced in `lean/README-verify.md`.
