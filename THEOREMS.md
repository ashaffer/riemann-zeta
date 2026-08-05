# Theorems

Proved statements extracted from this program's measurements. House standard:
every constant explicit, every proof complete or explicitly labeled
computer-assisted with its trust base; novelty claims carry the same diligence
caveats as everything else in this repository ("new as stated, pending
literature check" — the frontier corpus is Connes–Consani(–Moscovici), Suzuki,
Groskin; see `PROGRAM.md` §7).

Throughout, for L > 0 put a = L/4 and let H_L be the real Hilbert space
L²([−a, a]), extended by zero to ℝ. Define the dense form domain

  D_L = { φ ∈ H_L : ∫_ℝ |φ̂(r)|² log(1+r²) dr < ∞ }.

For φ ∈ D_L set

  φ̂(r) = ∫ φ(x) e^{−irx} dx,     ψ_φ(u) = ∫ φ(x) φ(x+u) dx,

  P(φ)  = 2 (∫ φ(x) e^{x/2} dx)(∫ φ(x) e^{−x/2} dx)                 (pole)
  A(φ)  = (1/2π) ∫_ℝ |φ̂(r)|² ( Re ψ(1/4 + ir/2) − log π ) dr        (archimedean)
  Π(φ)  = 2 Σ_{n ≥ 2 prime power} Λ(n) n^{−1/2} ψ_φ(log n)          (primes)

  Q_L(φ) = P(φ) + A(φ) − Π(φ),        λ(L) = inf { Q_L(φ) : φ ∈ D_L, ‖φ‖₂ = 1 }.

Since ψ_φ(u) = 0 for |u| ≥ 2a = L/2, the prime sum is the finite sum over
n < e^{L/2}: Q_L is precisely the truncated Weil form of the certified ledger
(`PROGRAM.md` §6), and Weil's criterion says: RH ⟺ λ(L) ≥ 0 for all L.
Unless explicitly labeled as a FULLINF full-space certificate, measurements
of λ(L) in `results/RESULTS.md` are Galerkin upper bounds for these quantities.
ψ denotes the digamma function; ψ(1/4) = −γ − π/2 − 3 log 2.

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

(iii) At r = 0 the claimed product is zero. For r ≠ 0,
d/dr Re ψ(1/4+ir/2) = Re[(i/2) ψ′(1/4+ir/2)] and
ψ′(z) = Σ_{n≥0}(z+n)^{−2}, so with z = 1/4 + ir/2:
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

## Proposition A′ (closed form, compact resolvent, and an attained margin)

For every L > 0, Q_L is a densely defined, closed, semibounded quadratic form
on H_L with form domain D_L. Its associated self-adjoint operator has compact
resolvent. Consequently λ(L) is finite and is attained by a unit vector in D_L.
The real test space C_c^∞((−a,a)) is a form core. Moreover, if
V₁ ⊂ V₂ ⊂ ⋯ ⊂ D_L and ⋃_m V_m is a form core, then

  inf { Q_L(φ) : φ ∈ V_m, ‖φ‖₂ = 1 } ↓ λ(L).

**Proof.** Put W(r) = Re ψ(1/4+ir/2) − log π. Lemma A(ii),(iv) show
that W is bounded below and that, after adding a fixed positive constant,
W(r) is comparable above and below to 1 + log(1+r²). Thus A is the
restriction to the closed support subspace H_L of the standard closed
Fourier-multiplier form with domain D_L. Smooth functions compactly supported
in (−a,a) lie in D_L and are dense in H_L, so the domain is dense.

They are also form-dense. Indeed, for φ ∈ D_L and s > 1, the compression
φ_s(x) = s^{1/2}φ(sx) has support in [−a/s,a/s] and converges to φ in the
weighted Fourier norm as s ↓ 1. This follows first for compactly supported
Fourier data and then in general by truncation, using
φ̂_s(r) = s^{−1/2}φ̂(r/s) and
1+log(1+s²r²) ≤ max(1,s²)[1+log(1+r²)]. For fixed s, convolve φ_s
with a smooth approximate identity whose support is smaller than a−a/s.
The result lies in C_c^∞((−a,a)) and converges in the same norm by dominated
convergence on the Fourier side. Thus C_c^∞((−a,a)) is a core for A, and
also for Q_L because the remaining forms are bounded.

The pole term is a bounded rank-two form: each functional
φ ↦ ∫φ(x)e^{±x/2}dx is bounded on H_L. The prime sum is finite, and
|ψ_φ(u)| ≤ ‖φ‖², so it too is a bounded form. A bounded symmetric
form perturbation preserves closedness and semiboundedness; hence Q_L has the
first two asserted properties.

It remains to prove compactness of the embedding D_L → H_L. Consider a set
bounded in the form norm. Its members have common compact support, bounded
L² norm, and a uniform bound

  (1/2π)∫ |φ̂(r)|² log(1+r²)dr ≤ C.

For translations τ_h, Plancherel gives

  ‖τ_hφ−φ‖² = (1/2π)∫ |φ̂(r)|² |e^{irh}−1|²dr.

After splitting at |r|=R, the high-frequency part is at most
4C/log(1+R²), uniformly in φ, while the low-frequency part is at most
R²h²‖φ‖². First choose R large and then h small. The
Fréchet–Kolmogorov compactness criterion now gives the compact embedding.
The representation theorem for closed semibounded forms produces the
self-adjoint operator, and compactness of the form-domain embedding gives
compact resolvent. Its spectral minimum is therefore an eigenvalue and is
attained. Finally, form-core density and the Rayleigh–Ritz principle give the
displayed monotone Galerkin convergence. ∎

**Scope note.** This proposition justifies the ground-state and operator
terminology used by the numerical program. It supplies no computable bound on
the gap between a finite Galerkin value and λ(L); finite-dimensional positivity
therefore remains evidence for, not a proof of, full operator positivity.

---

## Lemma B (a priori bounds on near-minimizers)

Fix 0 < ℓ₀ ≤ L ≤ ℓ₁ and ‖φ‖₂ = 1, φ ∈ D_L. Write κ₀ = ψ(1/4) − log π
(κ₀ > −5.38) and define the log-weighted energy

  W₊(φ) = (1/2π) ∫ |φ̂(r)|² · ½ log(1+4r²) dr ≥ 0.

Then, with C_P = 4 sinh(ℓ₁/4) and C_Π = 2 ℓ₁ e^{ℓ₁/4}:

 (i) |P(φ)| ≤ C_P and |Π(φ)| ≤ C_Π;
 (ii) A(φ) ≥ κ₀ + W₊(φ);
 (iii) λ(L) ≤ C_λ(ℓ₀), an explicit constant depending only on ℓ₀ (below);
 (iv) if Q_L(φ) ≤ λ(L) + 1 then W₊(φ) ≤ C_B, where
      C_B := C_λ(ℓ₀) + 1 + C_P + C_Π + 5.38;
 (v) if W₊(φ) ≤ C_B (in particular, under the hypothesis of (iv)), then for R ≥ 1:
      (1/2π) ∫_{|r|>R} |φ̂|² dr ≤ C_B / (½ log(1+4R²)) ≤ C_B/ log(2R).

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

  W₊(φ₀) ≤ (a₀/π) ∫₀^{1/a₀} log(1+4r²) dr
             + (1/π a₀) ∫_{1/a₀}^∞ log(1+4r²) r^{−2} dr
        ≤ (1/π) log(1 + 4/a₀²) + (1/π)[ log(1+4/a₀²) + 2 ]
        ≤ (2/π) log(1 + 4/a₀²) + 2,

  where the second integral was integrated by parts and
  8∫_{1/a₀}^∞(1+4r²)^{−1}dr = 4 arctan(a₀/2) ≤ 2a₀:
  ∫_{1/a₀}^∞ log(1+4r²) r^{−2} dr = a₀ log(1+4/a₀²) + 8∫_{1/a₀}^∞ (1+4r²)^{−1} dr
  ≤ a₀ log(1+4/a₀²) + 2a₀.
  Hence A(φ₀) ≤ κ₀ + 8 + W₊(φ₀), and
  C_λ(ℓ₀) := 4 sinh(ℓ₀/4) + κ₀ + 8 + (2/π) log(1+64/ℓ₀²) + 2 + 2ℓ₀ e^{ℓ₀/4}
  bounds Q_{ℓ₀}(φ₀) (the prime term bounded as in (i) at ℓ₀).

(iv) W₊ ≤ A − κ₀ = Q_L − P + Π − κ₀ ≤ (λ(L)+1) + C_P + C_Π + |κ₀|.

(v) On |r| > R the weight ½log(1+4r²) exceeds ½log(1+4R²), and
½log(1+4R²) ≥ ½log(4R²) = log(2R); Chebyshev. ∎

---

## Lemma C (no concentration on short intervals)

Let ‖φ‖ = 1 with W₊(φ) ≤ C_B, and let J ⊂ ℝ be an interval of length
0 < ε < 1.
Then

  ∫_J φ² ≤ 2√ε + 4 C_B / log(1/ε)   ( ≤ C_C / log(1/ε) with C_C = 2 + 4C_B,
                                       since √ε·log(1/ε) ≤ 2/e < 1 ).

**Proof.** Split φ = φ_R + φ^R at frequency R: φ_R = (2π)^{−1}∫_{|r|≤R} φ̂ e^{irx} dr.
Then ‖φ_R‖_∞ ≤ (2π)^{−1} ∫_{|r|≤R}|φ̂| ≤ (2π)^{−1}(2R)^{1/2}(∫|φ̂|²)^{1/2}
= (R/π)^{1/2}, and ‖φ^R‖² ≤ C_B/log(2R) by Lemma B(v). Hence
∫_J φ² ≤ 2 ∫_J φ_R² + 2‖φ^R‖² ≤ 2εR/π + 2C_B/log(2R). Choose R = ε^{−1/2}:
2√ε/π + 2C_B/log(2ε^{−1/2}) ≤ 2√ε + 4C_B/log(1/ε). ∎

## Lemma D (translation modulus of the autocorrelation)

Under the hypotheses of Lemma C, for all u, u′ with 0 < |u − u′| < 1:

  |ψ_φ(u) − ψ_φ(u′)| ≤ √|u−u′| + 4 C_B / log(1/|u−u′|) ≤ C_C / log(1/|u−u′|).

**Proof.** ψ_φ(u) = (2π)^{−1}∫ |φ̂(r)|² e^{iru} dr (Wiener–Khinchin; both sides
continuous, φ ∈ L¹∩L²), so with Δ = |u−u′|,
|ψ_φ(u) − ψ_φ(u′)| ≤ (2π)^{−1}∫ |φ̂|² min(2, |r|Δ) dr
≤ Δ·R·(2π)^{−1}∫_{|r| ≤ R}|φ̂|² + 2·(2π)^{−1}∫_{|r|>R}|φ̂|²
≤ ΔR + 2C_B/log(2R); take R = Δ^{−1/2} as in Lemma C. ∎

## Lemma E (two-edge bound: the entering prime is weakly coupled)

Under the hypotheses of Lemma C, if supp φ ⊂ [−a, a], 0 ≤ u < 2a, and
ε := 2a − u < 1, then:

  |ψ_φ(u)| ≤ C_C / log(1/ε).

**Proof.** ψ_φ(u) = ∫_{−a}^{a−u} φ(x)φ(x+u) dx; x ranges over the
left-edge interval [−a, −a+ε], while x+u ranges over the right-edge interval
[a−ε, a]. By Cauchy–Schwarz and Lemma C applied to both slivers,

  |ψ_φ(u)| ≤ (∫_{−a}^{−a+ε} φ²)^{1/2}
                  (∫_{a−ε}^{a} φ²)^{1/2}
              ≤ C_C / log(1/ε).  ∎

---

## Theorem 1 (monotonicity and the glide: λ is continuous through prime-power thresholds)

Let 0 < ℓ₀ ≤ L < L′ ≤ ℓ₁ with h := L′ − L ≤ min(1/2, ℓ₀/2, 1/e). Then:

 (1) **Monotonicity.**  λ(L′) ≤ λ(L).

 (2) **Modulus.**  λ(L) − λ(L′) ≤ C_glide(ℓ₀, ℓ₁) / log(1/h),

with the explicit constant

  C_glide = (16 + C_P′)/ℓ₀ + C_Π C_C + (1 + e^{ℓ₁/2} ) ℓ₁ C_C,
  C_P′    = e^{ℓ₁/4} (ℓ₁ + ℓ₁²/4) ,

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
W(r) = Re ψ(1/4+ir/2) − log π. Along the ray t ↦ tρ, Lemma A(iii)
gives |tρ W′(tρ)| ≤ 4, including when ρ < 0 without taking log ρ.
Thus |W(sρ) − W(ρ)| ≤ ∫₁ˢ 4 dt/t = 4 log s ≤ 4h/L ≤ 4h/ℓ₀.
Hence |A(φ_s) − A(φ′)| ≤ 4h/ℓ₀. We only use W₊(φ′) ≤ C_B below,
applied to ψ_{φ′}.

*(2b: pole.)* ∫φ_s e^{±x/2} dx = s^{−1/2} ∫ φ′(y) e^{±y/(2s)} dy. For
y ∈ [−a′, a′], |e^{±y/(2s)} − e^{±y/2}| ≤ e^{a′/2}·(a′/2)(1 − 1/s) ≤
e^{ℓ₁/8}(ℓ₁/8)(h/L), and |s^{−1/2} − 1| ≤ h/(2L). Combining with
Cauchy–Schwarz, each factor is at most
K := e^{ℓ₁/8}√(ℓ₁/2), while each factor changes by at most
(h/ℓ₀)K(1/2+ℓ₁/8). Therefore the product identity
|ab−cd| ≤ |a||b−d|+|d||a−c| gives
|P(φ_s) − P(φ′)| ≤ 4K²(1/2+ℓ₁/8)h/ℓ₀
= C_P′ h/ℓ₀ with C_P′ as displayed.

*(2c: incumbent primes.)* For prime powers n with log n < 2a (participating at
both levels), the coefficients differ by
|ψ_{φ_s}(log n) − ψ_{φ′}(log n)| = |ψ_{φ′}(s log n) − ψ_{φ′}(log n)|,
and (s−1) log n ≤ (h/L)(L/2) = h/2 < 1, so by Lemma D each differs by at most
C_C / log(2/h). Summing against 2ΣΛ(n)n^{−1/2} ≤ C_Π (Lemma B(i)):
total incumbent error ≤ C_Π C_C / log(2/h).

*(2d: departing primes.)* Prime powers with 2a ≤ log n < 2a′ participate at L′
but not at L (for φ_s their coefficient vanishes by support). Each satisfies
2a′ − log n ≤ 2a′ − 2a = h/2 =: ε-range, so by Lemma E,
|ψ_{φ′}(log n)| ≤ C_C / log(2/h). The number of prime powers in
[e^{L/2}, e^{L′/2}) is at most e^{ℓ₁/2} h/2 + 1 ≤ e^{ℓ₁/2} + 1 (h ≤ 1/2 — 
crudely, an interval of length e^{L'/2}−e^{L/2} ≤ e^{ℓ₁/2}h/2 contains at most
that many integers plus one), and each carries weight 2Λ(n)n^{−1/2} ≤ ℓ₁.
Total: ≤ (1 + e^{ℓ₁/2}) ℓ₁ C_C / log(2/h).

*Step 3 (assembly).* λ(L) ≤ Q_L(φ_s) ≤ Q_{L′}(φ′) + [2a] + [2b] + [2c] + [2d]
≤ λ(L′) + η + C_glide/log(1/h), since (log(2/h))^{−1} ≤
(log(1/h))^{−1} and the h-linear terms are absorbed by
h ≤ 1/log(1/h) for 0 < h ≤ 1/e. Let η → 0. With Step 1,
0 ≤ λ(L) − λ(L′) ≤ C_glide/log(1/h). ∎

**Corollary (the glide).** At every prime-power threshold L₀ = 2 log n₀ the
margin is continuous from both sides, and the newly entering prime's influence
switches on with coefficient O((log(1/(L−L₀)))^{−1}). Thus there is no jump
in λ at a threshold. Continuity alone does **not** exclude genuine power-law
vanishing at a threshold where λ(L₀) = 0; deciding whether that happens is still
RH-level operator information. The hat-basis collapse seen in this repository
is contradicted by the better-converged spectral data, not by continuity alone. (Measured
counterpart: `results/RESULTS.md`, threshold glide table; the measured
crossing ratio 0.973 vs. the envelope law's 0.968.)

**Honesty note.** The modulus (log 1/h)^{−1} is enormously weaker than the
measured smoothness (the envelope law is C^∞-like in L). The theorem's content
is the *absence of a jump* with an explicit modulus — it does not prove the
envelope law. All constants are explicit but generous; no attempt was made to
optimize.

**Novelty status (revised after the 2026-08-05 prior-art sweep).**
Attainment, compact-resolvent/Galerkin control, monotonicity, and qualitative
continuity are NOT new.  Bombieri established the variational ground-state
framework; Connes--Consani--Moscovici prove Galerkin convergence, discrete
lower-bounded spectrum, ground-state existence, and the monotonicity
explicitly in Proposition 3.4, Theorem 3.6, and Corollary 3.7 of
[*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755); and Suzuki proves
unrestricted qualitative continuity in Theorem 1.3 of
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096),
while recording Bombieri's earlier parity-restricted continuity assertions.
After matching conventions (`a=L/4` here and `lambda_CCM=exp(L/4)`), the
defensible additions in this section are (i) the explicit modulus
`C/log(1/h)` with displayed constants and (ii) the quantitative estimate for a
newly entering prime-power term in Lemma E.  Theorem 1 should therefore be
cited as an effective quantitative refinement of known glide results, not as
the source of attainment, monotonicity, or continuity.  The Frullani route to
Lemma A appears to be folklore-level; no priority claim is made for it.

**Formalization status.** Lemma A's sandwich — in its integral form, i.e.
½log(1+4r²) ≤ ∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t})dt ≤ ½log(1+4r²)+8 —
is now KERNEL-CHECKED: `GlideKernel.kernel_lower/kernel_upper` in
`lean/glide/Glide/Basic.lean` (with `laplace_sin` and `frullani_cos` as
formalized supporting lemmas), axioms [propext, Classical.choice, Quot.sound]
only. The identification with digamma awaits Gauss's formula in mathlib
(RH-LEMMA-MAP.md, Level 2).

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
exact ℚ Cauchy–Schwarz perturbation bound.) The direct scalar extension is
also kernel-checked: `CertInstance.real_window_positive_via_framework` proves
the same strict statement for arbitrary real matrices and nonzero real vectors.
This uses the exact congruence over ℝ; strictness is not inferred merely by
density, which would only yield nonnegativity.

## Bridge Proposition (computer-assisted, trust base stated)

Let Q ∈ ℝ^{12×12} be the matrix of the truncated Weil form Q_{L} at
L = 497/200 in the basis b_k(x) = P_k(4x/L) (unnormalized Legendre
polynomials, k = 0..11) of test functions supported in [−L/4, L/4] — the
support window in which the prime powers 2 and 3 participate. Then

  |Q_{kj} − mRat_{kj}| ≤ 10^{−20}   for all k, j.

**Correction notice (2026-07-26).** The originally emitted `mRat` integers were
computed with a dps-15 ambient conversion of the 220-bit interval endpoints,
carrying ~1.46e−17 error against the stated δ = 1e−20 — the kernel theorem
(about `mRat`) was never affected, but this Proposition was false as stated
for one day. Caught by the certificate-coherence oracle (nested m=12/m=24
certificates must agree on overlapping blocks), regenerated with exact 60-dps
conversion, re-verified, rebuilt, re-audited; coherence now passes at
5.00e−25 absolute. See results/RESULTS.md pathology log #5.

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

## Theorem 3 (a software-certified unrestricted window)

For the full logarithmically weighted form domain at L=7/4,

  Q_{7/4}(φ) > 2.2699×10⁻⁵ ‖φ‖₂²

for every nonzero φ. Consequently, by Theorem 1's support monotonicity, the
same lower bound holds for every 0<L≤7/4.

This is an infinite-dimensional conclusion. It is not the finite Galerkin
statement of Theorem 2 and is not restricted by a Fourier-tail hypothesis.
It is software-certified as a statement about the zeta form under the
remaining domain-identification trust base below; that identification is not yet checked by
the Lean kernel. Lean does now check the abstract Hilbert/projection transfer,
the complete F2 Legendre/Fourier/Plancherel leakage chain with its numerical
rational ledger, the pole residuals, directed p=2 scalar bounds, their
operator-level composition with the stored real finite certificate, and the
exact clipped-versus-original multiplier-integral comparison. The bounded
certificate now also checks containment for every canonical analytic matrix
entry and closes the clipped endpoint. It still does not check the zeta-form
domain/integrability identification.

**Proof.** At this window only n=2 occurs in the prime sum, so the multiplier
in Lemma F0 of `results/experts/FULLINF.md` is

  Ω(r)=Re ψ(1/4+ir/2)−log π−√2 log(2) cos(r log 2).

The trigamma partial-fraction series gives, for r>0 and y=r/2,

  d/dr Re ψ(1/4+ir/2)
    = Σ_{n≥0}(n+1/4)y/((n+1/4)²+y²)² > 0.

`Glide.DigammaMonotone` kernel-checks convergence and positivity of the series.
`Glide.DigammaSeries` reduces its identification with the derivative to local
uniform convergence of Euler's `Complex.GammaSeq`; `Glide.GammaUniform` proves
that convergence by a product-filter dominated-convergence argument. Thus the
derivative identity, strict monotonicity, and exterior comparison are
unconditional Lean theorems. `Glide.P2Symbol` additionally combines
monotonicity with `cos≤1` and proves the displayed p=2 symbol is at least its
clipped floor whenever `|r|≥50`.

Thus, at S=50, Ω(r) is bounded below outside the band by

  α=Re ψ(1/4+25i)−log π−√2log2
    =1.09387112771667… .

Replace Ω by α outside |r|≤50, leaving the rank-two pole term unchanged, and
call the resulting bounded form A. Then Q≥A. Let V be the first 48
orthonormal Legendre modes. The plane-wave Legendre identity and its geometric
Bessel-tail majorant give

  ‖1_{[-50,50]} ŵ‖²_{L²(dr/2π)} ≤ ρ‖w‖²,
  ρ<8.1×10⁻²²,  w∈V⊥.

`LegendreTail.norm_sphericalJIntegralModel_le` now kernel-checks the sharp
double-factorial bound for a directly defined oscillatory integral model, and
`LegendreTail.sphericalJIntegralModel_tsum_tail_le` kernel-checks the complete
infinite geometric summation. `LegendrePlaneWave` and `LegendreRodrigues`
kernel-check the all-degree endpoint vanishing and repeated integration by
parts, an all-degree Rodrigues theorem for a Legendre family transported from
mathlib's shifted definition, phase conversion, and the exact unnormalized
coefficient `FI(P_n)=2(-i)^n sphericalJIntegralModel n z`, including `z=0`.
`LegendreOrthogonality` now proves lower-degree and pairwise orthogonality,
the exact norm `integral P_n^2 = 2/(2n+1)`, and normalized Kronecker-delta
orthonormality. `LegendreCoefficientTail` and `LegendreScaled` prove the exact
normalized coefficients and complete tail on every symmetric interval.
`LegendreL2` and `LegendreScaledL2` prove polynomial density, construct the
complete Hilbert bases, establish Parseval and the canonical finite
projections, and identify real and imaginary plane-wave coefficients.
Finally, `LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal`
proves the explicit pointwise F2 leakage bound for every vector in the
orthogonal complement. `IntervalFourierL2` performs the band integration for
the genuine Bochner coefficient. `IntervalZeroExtension` constructs the
canonical zero extension, proves `L¹∩L²` compatibility with Mathlib's
Plancherel transform by a tempered-distribution argument, and proves the exact
band-norm identity including the `z/(2π)` change of variables.
`FullInfLegendreLedger` kernel-checks `ρ<81/10^23`, and
`FullInfFourierBridge.p2_angularFourierBandCLM_norm_sq_le` transfers it to the
actual band operator. No Fourier-normalization premise remains.

The degree-47 Taylor competitors for e^{±x/2} give pole projection residuals
δ_±<1.95×10⁻⁹³. `PoleProjectionL2` proves these residuals for the
canonical projection and proves both pole-vector norms are at most one.
`Glide.DigammaBounds` proves the directed scalar bounds
`109387/100000 ≤ α` and `|Ω−α|≤7447/1000` on the band, using an exact positive
rational digamma-difference series with explicit integral tails.

`src/fullinf_unrestricted_certificate.py` encloses all 600 independent
upper-triangular same-parity entries
of A|V by FLINT-Arb rigorous complex integration and proves by interval
Cholesky that A|V>βI with β=2.27×10⁻⁵. For φ=u+w, u∈V and w∈V⊥, the preceding
bounds give

`FullInfClipped48.clipped48IntervalLowerBound` now checks the corresponding
finite rational interval theorem in Lean, as two parity-reordered 24×24
blocks: every exact rational matrix in the stored radius-10⁻¹² intervals is
strictly above `(227/10^7)I`.
`FullInfClipped48Real.clipped48IntervalLowerBoundReal` directly casts the
integer congruence certificate and proves the same strict statement for every
real matrix in those intervals; it does not rely on density. The older
generator verifies externally that its Arb balls lie in those intervals.
Independently, the bounded rational certificate now proves in Lean that the
canonical analytic matrix entries lie in those intervals. This still does not
identify the resulting expression with the zeta form on its domain.
Nevertheless,
`FullInfClipped48Transfer.p2_projection_lower_bound_of_clipped48_intervals`
now composes this real interval theorem with the exact F8 projection ledger.
The later operator modules go further: `BoundedSymbolMultiplier` constructs a
Hermitian L² multiplier from an a.e.-real bounded symbol;
`FullInfOperatorLedger` derives the complement and cross inequalities from
Fourier leakage and pole residuals; and
`FullInfP2Endpoint.projection_lower_bound_of_fourier_clipped48_p2_symbol`
composes the actual band operator, poles, interval certificate, and determinant.
`LegendreParityCoordinates` supplies canonical even/odd coordinates, their
exact norm identity, and the actual basis-entry matrices, eliminating
coordinate isometry and matrix representation as independent assumptions.
`SymbolQuadraticComparison.interval_clipped_bandForm_le_original_integral`
proves the exact comparison with the original multiplier integral, including
Plancherel and the `2π` frequency scaling. In the cross-project composition,
`RHP2Bridge.p2ClippedForm_even_odd` proves parity decoupling from exact
Legendre reflection, Fourier real/imaginary parity, and pole reflection.
`RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`
discharges the even/odd interval premises after Lean verifies the analytic
error ledger and all 19,200 refinements. Its corollary
`p2_canonical_clipped_endpoint` proves the clipped lower bound from only
`f≠0`. `RHP2Bridge.p2_original_integral_lower_bound_of_matrix_containment_no_parity`
transfers
the same strict `22699/10^9` bound to the original unbounded weighted Fourier
integral plus the exact pole term, additionally assuming weighted integrability.
Neither theorem identifies that expression with the zeta Weil form.

  A(φ) ≥ β‖u‖²+d‖w‖²−2c‖u‖‖w‖,
  d>1.093,  c<2.12×10⁻¹⁰.

For the rational γ=2.2699×10⁻⁵, the same Arb run verifies

  β>γ,  d>γ,
  (β−γ)(d−γ)−c² > 10⁻⁹.

Hence the scalar two-by-two block is greater than γI, proving Q≥A>γI on the
full form domain. The Fourier, pole, scalar, operator, parity,
parity-coordinate, canonical matrix-containment, and clipped-to-original
comparison parts of this composition are kernel-checked. To turn it into a
Lean theorem about the zeta form, one must still identify the resulting
integral-plus-pole expression with that form on its domain and discharge the
required weighted integrability there.
Full derivations,
normalization factors, and reproduction
output are in `results/experts/FULLINF.md`, Theorems F7–F8. ∎

**Scope.** This proves local Weil positivity over one range of supports. RH
requires the corresponding positivity for every support size. No proposed
NT-4 converse is used or proved here, so no named-zero exclusion is asserted.

---

## Theorem 4 (a second unrestricted window)

For the full logarithmically weighted form domain at L=497/200,

  Q_{497/200}(φ) > 9.99×10⁻¹¹ ‖φ‖₂²

for every nonzero φ. Consequently, Theorem 1 gives positivity for every
0<L≤497/200. On 0<L≤7/4 the stronger constant in Theorem 3 still applies.

This is again a full-domain, software-certified statement under the stated
FLINT-Arb and analytic trust base, not a Lean-kernel theorem.

**Proof.** Here log 2,log 3<L/2<log 4, so the exact multiplier is

  Ω(r)=Re ψ(1/4+ir/2)−log π−√2 log(2)cos(r log 2)
       −(2log(3)/√3)cos(r log 3).

The trigamma argument in Theorem 3 applies unchanged. At S=70 it gives the
exterior floor α=0.1617833272712522268… and the band bound
|Ω−α|<7.783. For the first 80 orthonormal Legendre modes, the exact
Bessel-tail and Taylor estimates give

  ρ<8.582×10⁻²³,  δ_±<5.085×10⁻¹⁶⁰.

`src/fullinf_unrestricted_p3_certificate.py` encloses all 1,640 independent
upper-triangular same-parity entries of the clipped 80-dimensional block using FLINT-Arb and interval
Cholesky proves that block is greater than βI for β=10⁻¹⁰. The F8
transfer ledger gives d>0.161 and c<7.21×10⁻¹¹. For
γ=9.99×10⁻¹¹, the same run proves

  (β−γ)(d−γ)−c² > 1.6×10⁻¹⁴.

The two-by-two criterion of F8 (kernel-checked at projection level as
`FullInfTransfer.fullinf_p3_projection_lower_bound`) therefore proves
Q_{497/200}>γI on the complete form domain. Full definitions and output are in
`results/experts/FULLINF.md`, Theorem F9. ∎

**Scope.** Theorems 3–4 cover all nested supports only through L=497/200.
They do not establish positivity for arbitrary L and hence do not prove RH.

---

## Theorem 5 (a third unrestricted endpoint)

For the full logarithmically weighted form domain at L=749/250,

  Q_{749/250}(φ) > 9.9×10⁻¹⁶ ‖φ‖₂²

for every nonzero φ. Consequently, Theorem 1 gives positivity for every
0<L≤749/250, with the stronger constants of Theorems 3–4 on their nested
ranges. This remains a software-certified full-domain statement, not a
Lean-kernel theorem.

**Proof.** Here log4<L/2<log5, so the exact multiplier includes n=2,3,4:

  Ω(r)=Re ψ(1/4+ir/2)−log π−√2log(2)cos(rlog2)
       −(2log(3)/√3)cos(rlog3)−log(2)cos(2rlog2).

Write D(r)=Re ψ(1/4+ir/2)−log π. At S=110, 50,000 exact
width-10⁻³ Arb panels prove Ω(r)≥29/100
on [110,160]. The trigamma monotonicity used above and

  D(160)−(√2log2+2log3/√3+log2)
    =0.2953215959855678864… >29/100

continue that floor to infinity; evenness handles negative r. On the band,
|Ω−29/100|<8.605. For the first 132 orthonormal Legendre modes, the
exact Bessel-tail and Taylor estimates give

  ρ<1.52×10⁻²⁰,  δ_±<8×10⁻²⁸¹.

`src/fullinf_unrestricted_n4_certificate.py` rigorously encloses all 4,422
independent upper-triangular same-parity entries of the clipped block. Its
resumable 12-process FLINT-Arb run took 1,040.12 seconds, and interval
Cholesky proves that block is greater than βI for β=10⁻¹⁵. The F8
ledger gives d>0.289, c<1.06×10⁻⁹ and, for γ=9.9×10⁻¹⁶,

  (β−γ)(d−γ)−c² > 1.77×10⁻¹⁸.

The F8 criterion therefore proves Q_{749/250}>γI on the complete form
domain. Its rational projection-level instance is kernel-checked as
`FullInfTransfer.fullinf_n4_projection_lower_bound`; the analytic and Arb
premises remain external. Full details and output are in `results/experts/FULLINF.md`,
Theorem F10. ∎

**Scope.** Theorems 3–5 prove local Weil positivity only through L=749/250.
They do not establish positivity for arbitrary support and hence do not prove
RH or exclude any named zero without a separate quantitative converse.

---

## Provenance

Theorem 1 was found by proving what the July 25 "threshold glide" measurement
demanded (`PROGRAM.md` §2.17); Lemma A(ii) crystallized from the x-space
kernel identity of §2.14. Theorem 2 executes the first rung of Track A's
Curry–Howard ladder (§4, Track A) at the p = 3 window. The Lean development
(~750 lines including data) compiles in ~10 s against mathlib (Lean 4.32.1);
`#print axioms` output is reproduced in `lean/README-verify.md`.
Theorems 3–5 were obtained by clipping the exact Fourier multiplier at a frequency
where it has a sharp positive floor, then using the Legendre capture estimate
on the orthogonal complement and a rigorous finite block computation. It is
the first repository method to close the zeta finite-to-full gap at endpoints
in three successive prime-power regimes, and hence throughout the nested
range through L=749/250.
