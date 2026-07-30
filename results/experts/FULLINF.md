# FULLINF — unrestricted lower bounds at three successive-regime endpoints

NT seat, round 3 assignment (coordinator: "certified full-infimum lower bound at
one window"). Audit status (2026-07-27): **the assignment is now met at three
endpoints under an explicit Arb-plus-analytic trust base. Theorems F8–F10 and
the three committed clipped-symbol drivers prove**

  inf_{0 ≠ φ ∈ D_{7/4}} Q_{7/4}(φ)/‖φ‖₂² > 2.2699×10⁻⁵.
  inf_{0 ≠ φ ∈ D_{497/200}} Q_{497/200}(φ)/‖φ‖₂² > 9.99×10⁻¹¹.
  inf_{0 ≠ φ ∈ D_{749/250}} Q_{749/250}(φ)/‖φ‖₂² > 9.9×10⁻¹⁶.

These are unrestricted, infinite-dimensional bounds, not Galerkin
extrapolations or frequency-tail-class statements. The third inequality and
support monotonicity establish positivity for every L≤749/250 (with the
stronger earlier bounds available on their nested ranges), but this still
does not prove RH, which requires the relevant positivity for every support.
The integration and Cholesky layer is software-certified with
python-flint/FLINT-Arb, not kernel-checked in Lean.

1. **(Positive, unrestricted)** F7 supplies sharp positive exterior floors
   for the exact Fourier symbols, and F8 is a general clipped finite-to-full
   transfer. At L=7/4, 600 Arb-enclosed independent matrix integrals prove the
   clipped V₄₈ block >2.27×10⁻⁵ and yield the first bound above. At L=497/200,
   both primes 2 and 3 participate; 1,640 independent matrix integrals prove
   the clipped V₈₀ block >10⁻¹⁰ and F9 yields the second bound. At L=749/250,
   prime powers
   2, 3 and 4 participate; 4,422 independent matrix integrals prove the
   clipped V₁₃₂ block >10⁻¹⁵ and F10 yields the third bound.
2. **(Positive, class-restricted cross-check)** Theorem F4 below upgrades any certified Legendre–Galerkin
   window value λ_m to a certified lower bound on the infimum of Q_L over an
   explicit, basis-independent frequency-tail class of full-domain test
   functions. The repaired inequality is instantiated by the committed
   `src/fullinf_class_certificate.py`: at L = 7/4, m = 48, R = 50 and
   τ̄ = 10⁻¹⁵ it proves Q_L > 1.1139×10⁻⁵ for every member of that class, under the
   stated `mpmath.iv` and analytic trust base (§8.2). F4 and this driver alone
   do not bound the unrestricted infimum; F8 does so separately. The same
   script certifies an explicit normalized degree-28 polynomial in the class,
   proving non-vacuity, but does not certify
   that a proposed zero-centered packet belongs. In fact the tail contraction
   puts the radius-2×10⁻⁸ unit-sphere cap around this witness in the class, so
   the same positive bound holds throughout that cap. The older m = 192 ledger
   remains **provisional**, because its T₂ integral used ordinary mpmath quadrature and
   its driver/artifact was not committed. No zero-exclusion corollary follows:
   the cited quantitative converse Weil lemma NT-4 is still a proposal, not a
   proved lemma.
3. **(Negative only for the older estimate)** The unrestricted full infimum is
   not reached by the particular direct-tail coercivity estimate tested in F5: the Weil form's coercivity in
   frequency is logarithmic (Lemma A(ii) of THEOREMS.md, sharp by A(iv)), and
   the direct split-at-R error budget tested in F5 bottoms out numerically near
   2.8 — five orders of magnitude above the margin. This does not prove that
   every subspace-plus-tail argument must fail; F5 records only the limitation
   of that explicit estimate.
4. **(Basis diagnostic; empirical)** Observation F6 records a second
   obstruction: polynomial (and hat) subspaces have Fourier content up to
   r ≈ m/a but capture competitors only below r ≈ 0.66·m/a; in the gap the
   coupling is O(1). This "capture-vs-content conflict" explains why the class
   in F4 sits at tail masses ~10⁻¹⁶ and suggests a prolate basis for future
   tightening (§7): band concentration directly targets the measured conflict.
   This is a basis-design heuristic, not a uniqueness theorem.

The analytic argument below is self-contained modulo THEOREMS.md and the
displayed standard digamma series; every constant is explicit. Section 7 gives
the unrestricted transfer and Arb certificate, §8.2 gives the class-restricted
cross-check, §9 preserves the older exploratory diagnostics, and §10 maps the
Lean gap. Notation: a = L/4, unit φ ∈ H_L = L²[−a,a] extended by
zero, φ̂(r) = ∫φe^{−irx}dx, V_m = polynomials of degree < m on [−a,a],
P_m = L²-orthogonal projection onto V_m, λ_m^cert = certified lower bound of
the Galerkin minimum over V_m (interval Cholesky, existing instruments).

---

## 1. Lemma F0 (the form is frequency-diagonal plus an explicit rank-two term)

For unit φ ∈ D_L,

  Q_L(φ) = (1/2π) ∫_ℝ |φ̂(r)|² Ω_L(r) dr + P(φ),

  Ω_L(r) := Re ψ(1/4 + ir/2) − log π − Σ_{n < e^{L/2}} 2Λ(n) n^{−1/2} cos(r log n),

with P(φ) = 2(∫φe^{x/2})(∫φe^{−x/2}) the pole term.

*Proof.* The archimedean term is definitionally the first two summands
(ledger, PROGRAM.md §6). For the primes: ψ_φ(u) = (1/2π)∫|φ̂|²e^{iru}dr
(Wiener–Khinchin; the same identity used in THEOREMS.md Lemma D, valid since
φ ∈ L¹∩L², both sides continuous), and ψ_φ is even, so
2Λ(n)n^{−1/2}ψ_φ(log n) = (1/2π)∫|φ̂|²·2Λ(n)n^{−1/2}cos(r log n)dr. The prime
sum is finite (n < e^{L/2}). ∎

## 2. Lemma F1 (envelope bounds on the symbol)

Let C_pr(L) := Σ_{n < e^{L/2}} 2Λ(n)n^{−1/2}, κ₀' := |ψ(1/4) − log π| = 5.3722…,
c₀ := κ₀' + 8 + C_pr(L), and Ω̄(r) := c₀ + ½log(1+4r²). Then for all real r:

 (i) |Ω_L(r)| ≤ Ω̄(r);
 (ii) Ω_L(r) ≥ −c₋, c₋ := κ₀' + C_pr(L);
 (iii) Ω_L(r) ≥ 0 for |r| ≥ r₊(L) := ½(e^{2c₋} − 1)^{1/2},
       and Ω_L(r) > 0 for |r| > r₊(L).

At L = 7/4: C_pr = 2 log2/√2 = 0.9803, c₀ = 14.352, c₋ = 6.352, r₊ = 286.9.
At L = 497/200: C_pr = 0.9803 + 2 log3/√3 = 2.2489, c₀ = 15.621, c₋ = 7.621,
r₊ = 1020.3.

*Proof.* THEOREMS.md Lemma A(ii),(iv) sandwich Re ψ(1/4+ir/2) − log π between
−κ₀' + ½log(1+4r²) and the same +8; the cosine sum is bounded by ±C_pr. (iii)
solves ½log(1+4r²) ≥ c₋, with strictness above the endpoint. ∎

## 3. Lemma F2 (capture: low frequencies are seen by V_m)

For all real r and m ≥ 1, with z = |r|a:

  ‖(I − P_m) e^{irx}‖²_{L²[−a,a]} = 2a · B_m(z),   B_m(z) := Σ_{k≥m} (2k+1) j_k(z)²,

and whenever q_m(z) := z²/((2m+1)(2m+3)) < 1:

  B_m(z) ≤ t_m(z)/(1−q_m(z)),   t_m(z) := (2m+1) z^{2m} / ((2m+1)!!)².

*Proof.* The orthonormal Legendre coefficients of e^{irx} on [−a,a] are
c_k = i^k √(2a(2k+1)) j_k(ra) (standard plane-wave expansion), and
Σ_{k≥0}(2k+1)j_k(z)² = 1 (spherical-Bessel addition theorem at θ = 0), which
also confirms ‖e^{irx}‖² = 2a. For the tail bound: the integral representation
j_k(z) = z^k/(2^{k+1}k!) ∫_{−1}^1 e^{izt}(1−t²)^k dt gives
|j_k(z)| ≤ z^k/(2k+1)!!; the summand ratio is z²/((2k+1)(2k+3)) ≤ q_m(z), so the
tail is dominated by the geometric series. ∎

For Z with q_m(Z) < 1, put

  B_m^*(Z) := t_m(Z)/(1−q_m(Z)).

Both t_m(z) and q_m(z) are increasing for 0 ≤ z ≤ Z, so the preceding
bound gives B_m(z) ≤ B_m^*(Z) uniformly on that interval. In particular, no
monotonicity of the exact Bessel tail B_m is assumed here.

Consequences (both used below; ε-terms superexponentially small once
aR ≤ 0.9·(2m/e)): for w = (I−P_m)φ, ‖φ‖ = 1,
 (a) sup_{|r|≤R} |ŵ(r)| ≤ ‖w‖·√(2a·B_m^*(aR));
 (b) ‖(I−P_m)φ_R‖ ≤ √(R/π)·√(2a·B_m^*(aR)) for the band-limited part φ_R.

## 4. Lemma F3 (content: what V_m carries at high frequency)

For unit u ∈ V_m and all r ≠ 0, with z = |r|a:

  |û(r)|² ≤ 2a · min( 1,  πm²/(2z),  (π/2)·c_L²·m²·z^{−5/3} ),  c_L = 0.7858.

*Proof.* |û(r)|² ≤ ‖u‖²‖e^{irx}‖² = 2a (Cauchy–Schwarz) gives the first
branch. For the others, |û(r)|² ≤ 2a·K_m(z), K_m(z) = Σ_{k<m}(2k+1)j_k(z)²
(Bessel's inequality in the plane-wave expansion), and
j_k(z)² = (π/2z)J_{k+1/2}(z)² with |J_ν| ≤ 1 (Bessel's bound) gives the
second; Landau's uniform bound |J_ν(z)| ≤ c_L z^{−1/3} (Landau, *Monotonicity
and bounds on Bessel functions*, 2000; c_L = 0.78574…) gives the third, using
Σ_{k<m}(2k+1) = m². ∎

Definition (the content functional): for R > 0,

  T₂(m, R) := sup_{unit u ∈ V_m} (1/2π)∫_{|r|>R} |û(r)|² Ω̄(r)² dr
            ≤ (1/π)∫_R^∞ 2a·min(1, πm²/(2ar), (π/2)c_L²m²(ar)^{−5/3})·Ω̄(r)² dr,

an explicit one-dimensional integral (evaluated in §8; e.g. √T₂ = 643 at
L = 7/4, m = 192, R = 284).

## 5. Theorem F4 (certified class-restricted full-infimum lower bound)

Fix L, m, and a cut R with aR ≤ 0.9·(2m+1)/e. Let λ_m^cert ≥ 0 be a certified
lower bound for the Galerkin minimum of Q_L over V_m. Define the class

  𝒞(R, τ̄) := { φ ∈ D_L : ‖φ‖₂ = 1, (1/2π)∫_{|r|>R} |φ̂(r)|² dr ≤ τ̄ }.

Then for every φ ∈ 𝒞(R, τ̄):

  Q_L(φ) ≥ λ_m^cert·(1 − ε²) − E,  where
  β := √(2a·B_m^*(aR)),  ε := √τ̄ + √(R/π)·β,
  E := 2[ √T₂(m,R)·ε + Ω̄(R)·√(R/π)·β·ε + √(2 sinh a)·δ_P·ε ]
       + (c₋ + δ_P²/2)·ε²,
  δ_P := ‖(I−P_m)e^{x/2}‖ + ‖(I−P_m)e^{−x/2}‖ (superexponentially small).

*Proof.* Write φ = u + w, u = P_mφ (support is preserved: V_m ⊂ H_L). Then
Q(φ) = Q(u) + 2B(u, w) + Q(w) with B the polarization of Q.

(1) Q(u) ≥ λ_m^cert‖u‖² = λ_m^cert(1 − ‖w‖²), and ‖w‖ ≤ ε by splitting
φ = φ_R + φ^R: the band-limited part is captured to Lemma F2(b), the tail has
mass ≤ τ̄ by the class hypothesis.

(2) By F0 and F1(ii), the multiplier part of Q(w) is at least −c₋ε².
Writing d_± = ‖(I−P_m)e^{±x/2}‖, orthogonality gives
|I_±(w)| ≤ d_±ε, hence |P(w)| ≤ 2d₊d₋ε² ≤ (δ_P²/2)ε².

(3) Cross term, B(u,w) = (1/2π)∫ û ŵ* Ω_L dr + [pole cross]. Pole cross:
|I_±(u)| ≤ √(2 sinh a) and |I_±(w)| ≤ d_±ε, so
|I_+(u)I_-(w)+I_-(u)I_+(w)| ≤ √(2 sinh a)·δ_P·ε.
Frequency integral, split at R: below R, |ŵ| ≤ ‖w‖·√(2a B_m^*(aR)) pointwise
(F2(a)), so the piece is ≤ Ω̄(R)·‖u‖·√(2R/2π)·√(2aB_m^*(aR))·‖w‖ ≤
Ω̄(R)√(R/π)·β·ε. Above R, Cauchy–Schwarz with the weight on u and
the normalized Plancherel bound
[(1/2π)∫_{|r|>R}|ŵ|²]^{1/2} ≤ ‖w‖₂ ≤ ε give directly
|(1/2π)∫_{>R} û ŵ Ω_L| ≤ √T₂(m,R)·ε. This is the term
missing from the original proof; no assumption R ≥ r₊(L) is needed.
Collecting (1)–(3) gives the display. ∎

Remarks. (i) The theorem is unconditional as a statement about Q_L (no RH
anywhere). (ii) The class is basis-independent and is NOT all of H_L; the
direct logarithmic-tail estimate in F5 does not extend this bound to all of
H_L. For the very small numerical τ̄ used below, a rigorous non-vacuity or
packet-membership certificate is a separate obligation not supplied by F4
itself. Section 8.2 discharges non-vacuity for its particular parameters; packet
membership remains open.
(iii) Sobolev corollary: if s > 0 and S_s(φ)² := (1/2π)∫|φ̂|²(1+r²)^s dr ≤ M², then
φ ∈ 𝒞(R, M²(1+R²)^{−s}); the tables below quote both forms.

## 6. Limitations and basis diagnostics

**Limitation F5 (the present coercivity estimate does not close).** The a-priori frequency control
the form gives its own near-minimizers is logarithmic: any unit φ with
Q_L(φ) ≤ λ_m has W₊(φ) := (1/2π)∫|φ̂|²·½log(1+4r²)dr ≤ C_B* :=
λ_m + κ₀' + C_P + C_Π (THEOREMS.md Lemma B(iv); C_B* ≈ 10.3 at L = 7/4), and
this is sharp up to the additive 8 (Lemma A(iv)). Consequently, substituting
the only available tail estimate
τ(R) ≤ C_B*/(½log(1+4R²)) into this direct split produces an error-budget
term of order Ω̄(R)·√(C_B*/log(2R)), whose displayed majorant grows rather
than decays as R → ∞. The numerical optimization of this particular budget
has minimum value ≈ 2.8 at the smallest useful cuts. Since every measured
window margin is ≤ 3.2×10⁻⁵, this particular estimate does not close for any
of the tested (m,R). This does **not** prove a lower bound on the error of every possible
subspace-plus-tail argument: additional regularity or cancellation information
could improve the estimate.

**Observation F6 (capture-vs-content conflict for polynomial subspaces).**
V_m captures competitors only below R ≈ 0.66·m/a (Lemma F2 needs
aR ≲ 2m/e), but carries its own Fourier content out to r ≈ m/a (Legendre
mode k peaks at r ≈ k/a), with O(1) mass in the gap [0.66 m/a, m/a] where
Ω̄ ≈ c₀ + log(2m/a). Hence the coupling constant √T₂(m,R) grows like
√(m·polylog) (measured: 406 → 643 → 777 for m = 96 → 192 → 256 at L = 7/4)
instead of decaying, and closure forces τ̄ ~ (λ_m/√T₂)² ~ 10⁻¹⁶. A basis of
band-concentrated functions (truncated prolates: content ≤ R by construction
up to the Landau–Widom leak e^{−plunge}) removes the conflict: the same F4
skeleton would close with τ̄ ~ (λ_m/Ω̄(R))² ~ 10⁻¹², four orders weaker a
hypothesis, i.e. a class containing packets to heights ~e^{L/2}-scale rather
than ~40. This is evidence that a prolate basis is the natural next choice,
not a no-go theorem for all polynomial-basis arguments.

## 7. Theorems F7–F10 (sharp clipping and unrestricted transfer)

**Lemma F7 (sharp exterior floor at L = 7/4).** Put

  D(r) := Re ψ(1/4+ir/2)−log π,  c₂ := √2 log 2.

Because log 2 < 7/8 < log 3, the exact symbol is
Ω(r)=D(r)−c₂cos(r log 2). The function D is even and strictly increasing for
r>0. Indeed, termwise differentiation of the absolutely locally convergent
trigamma series, with y=r/2, gives

  D′(r) = Σ_{n≥0} (n+1/4)y / ((n+1/4)²+y²)² > 0.

For S>0 set α_S=D(S)−c₂. Then Ω(r)≥α_S for |r|≥S. On |r|≤S, writing
κ=|D(0)| and c₋=κ+c₂,

  −(c₋+α_S) ≤ Ω(r)−α_S ≤ 2c₂,

so |Ω−α_S|≤M_S:=max(c₋+α_S,2c₂). At S=50, Arb encloses

  α = 1.09387112771667391235…,
  M = c₋+α = 7.4463126904108866863… .

The same argument works at every fixed L. With

  C_L := Σ_{n<e^{L/2}}2Λ(n)n^{-1/2},

set α_S=D(S)−C_L. Then Ω_L≥α_S outside the band and

  sup_{|r|≤S}|Ω_L(r)−α_S|
    ≤ max{D(S)−D(0), 2C_L}.

Since D(S)→∞, a positive exterior floor exists for every fixed L. Moreover,
the clipped symbols increase pointwise with S: if S₂>S₁, then on the newly
unclipped annulus Ω_L≥α_{S₁}, while α_{S₂}≥α_{S₁} outside. Thus the analytic
construction has no fixed-window barrier; later windows cost larger S and m
and have much smaller finite margins.

**Theorem F8 (band-clipped finite-to-full transfer).** Work first in the real
Hilbert space H=L²[−a,a], put

  ‖C_Sf‖² := (1/2π)∫_{|r|≤S}|f̂(r)|²dr,

and let V⊂H be finite dimensional with orthogonal projection P. Put
p_±(x)=e^{±x/2}, ρ=‖C_S|_{V⊥}‖², and
δ_±=‖(I−P)p_±‖. Suppose Ω≥α>0 off [−S,S], |Ω−α|≤M on the band, and the
clipped form

  A_S(f) := α‖f‖² +(1/2π)∫_{|r|≤S}(Ω(r)−α)|f̂(r)|²dr
            +2⟨f,p_+⟩⟨f,p_-⟩

satisfies A_S(u)≥β‖u‖² for u∈V. Define

  G := √(2sinh a),
  d := α−Mρ−2δ_+δ_-,
  c := M√ρ+G(δ_++δ_-).

Then, for f=u+w with u=Pf,

  Q_L(f) ≥ A_S(f)
         ≥ β‖u‖²+d‖w‖²−2c‖u‖‖w‖.

Consequently, if d>0 and βd>c²,

  Q_L(f) ≥ γ‖f‖²,
  γ := [β+d−√((β−d)²+4c²)]/2 > 0.

Equivalently, a proposed rational γ is certified by β>γ, d>γ, and
(β−γ)(d−γ)>c².

*Proof.* Outside the band,
Q_L−A_S=(2π)⁻¹∫(Ω−α)|f̂|²≥0. Orthogonality kills the α cross term. On V⊥,
the band block is at least −Mρ‖w‖² and its polarized u,w term has modulus at
most M√ρ‖u‖‖w‖. The pole w-block is at least
−2δ_+δ_-‖w‖²; its polarized cross term is at most
G(δ_++δ_-)‖u‖‖w‖. Combine these with the finite β inequality and diagonalize
the displayed two-by-two matrix. The Hermitian complex form follows by the
same absolute-value estimates (equivalently, by real and imaginary parts). ∎

**Certified Legendre instance.** For the orthonormal basis
b_k(x)=√((2k+1)/(2a))P_k(x/a) and V_m=span{b_0,…,b_{m−1}}, F2 gives

  ρ ≤ (2aS/π)B*,
  B* := t/(1−q),
  t := (2m+1)(aS)^{2m}/((2m+1)!!)²,
  q := (aS)²/((2m+1)(2m+3)).

The degree-(m−1) Taylor polynomial also gives

  δ_± ≤ √(2a)e^{a/2}(a/2)^m/m!.

At (a,S,m)=(7/16,50,48), q=0.0498298057898…, B*=5.81295077198×10⁻²³,
ρ<8.1×10⁻²², and δ_±<1.95×10⁻⁹³. The independent script
`src/fullinf_unrestricted_certificate.py` uses the entire 0F1 representation
near the removable Bessel singularity and Arb's Bessel functions on positive
unit panels. It encloses all 600 independent upper-triangular same-parity
clipped matrix integrals. At
128-bit precision, interval Cholesky proves

  A_50|_{V_48} > 2.27×10⁻⁵ I.

The transfer ledger then proves d>1.093, c<2.12×10⁻¹⁰ and, for the rational
γ=2.2699×10⁻⁵,

  (β−γ)(d−γ)−c² > 10⁻⁹.

Therefore

  **inf_{0≠φ∈D_{7/4}} Q_{7/4}(φ)/‖φ‖² > 2.2699×10⁻⁵.**

**Theorem F9 (second unrestricted instance, primes 2 and 3).** At
L=497/200, a=497/800 and log2,log3<L/2<log4. Thus

  Ω(r)=D(r)−√2log2 cos(rlog2)−(2log3/√3)cos(rlog3).

Take S=70 and m=80. The generalized F7 floor and the exact F2/Taylor bounds
give

  α=0.1617833272712522268…,
  M<7.783,
  q=0.072063508602294…,
  B*=3.09962261534312×10⁻²⁴,
  ρ<8.582×10⁻²³,
  δ_±<5.085×10⁻¹⁶⁰.

The separate driver `src/fullinf_unrestricted_p3_certificate.py` encloses all
1,640 independent upper-triangular same-parity entries of the clipped
80-dimensional matrix. Its hardened
128-bit Arb run took 399.34 seconds and interval Cholesky proved

  A_70|_{V_80} > 10⁻¹⁰ I.

The block ledger gives d>0.161, c<7.21×10⁻¹¹ and, for the rational
γ=9.99×10⁻¹¹,

  (β−γ)(d−γ)−c² > 1.6×10⁻¹⁴.

Hence

  **inf_{0≠φ∈D_{497/200}} Q_{497/200}(φ)/‖φ‖² > 9.99×10⁻¹¹.**

**Theorem F10 (third unrestricted instance, prime powers 2, 3 and 4).** At
L=749/250, a=749/1000 and log4<L/2<log5. Thus

  Ω(r)=D(r)−√2log2 cos(rlog2)−(2log3/√3)cos(rlog3)
       −log2 cos(2rlog2).

The crude absolute-cosine floor is not yet positive enough at the economical
cut S=110. Instead, 50,000 exact width-10⁻³ Arb panels prove
Ω(r)≥29/100 on [110,160]. At r=160 the crude floor is

  D(160)−(√2log2+2log3/√3+log2)
    =0.2953215959855678864… >29/100,

so trigamma monotonicity and |cos|≤1 continue the same floor to infinity;
evenness handles the negative half-line. On the band, | Ω−29/100 |<8.605.

Take m=132. The exact F2/Taylor bounds give

  q=67881121/707550000=0.095938…,
  B*=2.89051682601083×10⁻²²,
  ρ<1.52×10⁻²⁰,
  δ_±<8×10⁻²⁸¹.

`src/fullinf_unrestricted_n4_certificate.py` encloses all 4,422 independent
upper-triangular same-parity entries of the clipped matrix. It uses the entire
0F1 formula on the first panel, an exact sin/cos recurrence below the spherical
Bessel turning point, and Arb's Bessel J above it. A resumable 12-process run
took 1,040.12 seconds; interval Cholesky proved

  A_110|_{V_132} > 10⁻¹⁵ I.

The committed 4,422-entry checkpoint has SHA-256
`7591f662b1c1a79ed83cb6999881d8face43836dec1131ccff8d56d6bdf7354f`.
Its metadata includes a SHA-256 digest of the source functions defining the
cached integrand, so a numerical-kernel change invalidates the cache.
An independent audit found exactly the expected 2·(66·67/2) parity entries,
no duplicates or omissions, and six fresh Arb integrations contained by their
cached balls.

The block ledger gives d>0.289, c<1.06×10⁻⁹ and, for
γ=9.9×10⁻¹⁶,

  (β−γ)(d−γ)−c² > 1.77×10⁻¹⁸.

Hence

  **inf_{0≠φ∈D_{749/250}} Q_{749/250}(φ)/‖φ‖² > 9.9×10⁻¹⁶.**

The analytic inputs are F0, F2, the displayed trigamma monotonicity, the
elementary Bessel geometric majorant, and the Taylor remainder. The finite
integral and Cholesky enclosures use python-flint/FLINT-Arb
(`acb_calc_integrate`) and are software-certified, not Lean-formalized.
These are full-domain results, but they are not RH and assert nothing about
positivity beyond L=749/250.

## 8. Legacy exploratory instantiation ledger (§9 scratch scripts)

Configuration: cut R = 0.88·2m/(ea); class stated as tail mass at R;
Sobolev coverage at s = 10 (L = 7/4) and s = 12 (L = 497/200); "packet
coverage" = largest γ₀ such that a unit Gaussian wave packet at frequency γ₀
(width ~3) provably lies in the class (calibration-grade estimate
S_s ≈ 2(1+(γ₀+3)²)^{s/2}; to be hardened in the NT-4 writeup).

| L | m | R | class τ̄ at R | Sobolev form | provisional class bound | packet coverage |
|---|---|---|---|---|---|---|
| 7/4 | 96 | 142.1 | 3.7e−16 | S₁₀ ≤ 6.5e13 | ≥ 1.57e−5 | γ₀ ≤ 19.4 (zeros 1) |
| 7/4 | 128 | 189.4 | 2.5e−16 | S₁₀ ≤ 9.5e14 | ≥ 1.57e−5 | γ₀ ≤ 26.3 (zeros 1–2) |
| **7/4** | **192** | **284.2** | **1.5e−16** | **S₁₀ ≤ 4.2e16** | **≥ 1.56e−5** | **γ₀ ≤ 39.8 (zeros 1–6)** |
| 7/4 | 256 | 378.9 | 1.0e−16 | S₁₀ ≤ 6.1e17 | ≥ 1.56e−5 | γ₀ ≤ 53.0 |
| 497/200 | 192 | 200.1 | 1.7e−26 | S₁₂ ≤ 5.4e14 | ≥ 1.75e−10 | γ₀ ≤ 12.9 (none) |
| 497/200 | 256 | 266.8 | 1.2e−26 | S₁₂ ≤ 1.4e16 | ≥ 1.75e−10 | γ₀ ≤ 17.9 (zero 1) |

The m = 192 core now has an interval-Cholesky lower bound 3.13e−5 at L=7/4
(completed after the original report). Note the certified artifacts
are *mpmath.iv*; a Lean-integer version is NOT required for the claim (and at
m = 192 the CS-1/NA depth law prices the integer route as infeasible in the
current format — use NA Lemma 4(ii)'s inequality-form redesign if
formalizing).

### 8.1 Certification runs (completed; artifacts originally outside the repository)

Protocol: build the interval form `certified_spectral_form(7/4, m, N=400)`
once (mpmath.iv, rigorous series remainders as in the module header), then
interval-Cholesky of Q − βG down a β-ladder 3.13e−5 → 3.0e−5; the first PASS
certifies λ_m(V_m) > β outright (a PASS is a kernel-of-the-method proof that
every leading minor of the outward-rounded interval matrix is positive).
Drivers: `certrun.py` / `certrun2.py` (session scratchpad); logs flushed
line-by-line so runs survive session churn. Scratchpad root:
`/tmp/claude-1000/-home-ubuntu-Projects-Riemann-Zeta/b43eb949-595f-4ac3-ad58-82a3f3afb113/scratchpad`.

**Instrument finding (new, diligence-grade).** The first m = 96 attempt at
the module's default iv.prec = 220 bits FAILED all β down to 2.5e−5, each
Cholesky dying in < 1 s — an interval-width blowup, not a mathematical
failure (λ_96 is sandwiched in (3.12e−5, 3.1416e−5) by Rayleigh–Ritz
monotonicity and the operator limit). Cause, located: the prime-term Horner
evaluation of the exact F_kj polynomials at v₀ = log(2)/a = 1.584 > 1 with
coefficients of size ~4^{k+j} costs ~5.3·m bits of cancellation at L = 7/4;
220 bits is an implicit ceiling near m ≈ 48 on this window. All previously
published spectral certificates sat at v₀ ≤ 1.24 and m ≤ 48, so the ceiling
was never visible. **Program note: `certified_spectral.py` users must scale
iv.prec ≳ 5.3·m + 250 on small-a windows** (set from the caller; no src
change needed). Failed-run artifacts kept: `cert96.log`, `cert96.result`.

- **(a) m = 48, prec 512:** PASS at β = 3.13e−5 (53 s).
- **(b) m = 96, prec 768:** PASS at β = 3.13e−5 (1520 s).
- **(c) m = 192, prec 1344:** PASS at β = 3.13e−5 (47817 s).

These outputs were found in the original session scratch directory. They
certify the finite Galerkin core, but not the class-bound ledger by themselves.

Corrected headline assembly: with
β = certified Cholesky bound, the F4 chain at (m, R, τ̄) is
inf_{𝒞(R,τ̄)} Q_L ≥ β·(1−ε²) − 2[√T₂·ε + Ω̄(R)√(R/π)β_m-capture·ε + pole]
− (c₋+δ_P²/2)ε². The existing `ledger.py` used ordinary mpmath
quadrature for T₂ rather than a proved outward-rounded upper bound, so the
table's class bounds remain provisional until that one-dimensional integral is
certified and the corrected formula is rerun.

Verification safety: if certified β lands below 3.1e−5 the table's final
column degrades linearly, not catastrophically. Fallback needing NO new run:
none — the certified hat-basis value at L = 7/4 (3.77497970e−5, m = 41,
RESULTS.md) cannot be used directly, since F2/F3 are Legendre-specific.

### 8.2 Reproducible conservative class certificate (2026-07-27)

`src/fullinf_class_certificate.py` supplies the missing committed driver for a
smaller, deliberately conservative instance:

  L = 7/4,  m = 48,  R = 50,  τ̄ = 10⁻¹⁵,
  λ_m^cert = 3.13×10⁻⁵.

At 512-bit `mpmath.iv` precision it rebuilds the spectral matrix, proves
`Q_m - λ_m^cert I` positive definite by interval Cholesky, and bounds T₂
without quadrature. For r ≥ 1 it uses
`Ω̄(r) ≤ 15 + log r + (log 5)/2`, replaces Landau's constant by the weaker
safe value 1, splits the content majorant where its constant and r⁻⁵ᐟ³
branches cross, and evaluates both pieces by closed-form antiderivatives. The
July 27 hardened run returned

```
m=48 core lambda_m > 3.13e-5: True
rounded endpoint diagnostics:
  sqrt(T2): 318.473297256
  capture beta: 7.13185244203e-12
  epsilon: 3.16512285765e-8
  pole projection delta: 3.896136e-93
  class lower endpoint: 1.11398577391e-5
CERTIFIED: sqrt(T2)<318.474, beta<7.14e-12, eps<3.17e-8
SOFTWARE-CERTIFIED CLASS BOUND: inf_C Q_L > 1.1139e-5
rounded witness-tail endpoint: 1.49662537123e-17
CERTIFIED NONVACUITY: explicit degree-28 polynomial tail < 3e-17
```

The in-code interval comparison conservatively certifies the round statement

  inf_{φ ∈ 𝒞(50,10⁻¹⁵)} Q_{7/4}(φ) > 1.1139×10⁻⁵.

This closes the corrected F4 numerical ledger for this one row under its stated
software/analytic trust base. For completeness, write
`f(x)=Σ_{k=0,2,...,28} d_k P_k(x/a)` on `[−a,a]`, with the exact decimal-rational
coefficients committed in the script, and extend it by zero. The script
integrates the first 81 terms of

  sin(R(x−y))/(π(x−y)) = (R/π) Σ_{n≥0} (−1)ⁿ[R(x−y)]²ⁿ/(2n+1)!

against `f(x)f(y)` using exact rational moments. Since
`|R(x−y)|≤43.75` and `43.75²<164·165`, the alternating remainder is at most
the `z¹⁶²/163!` term. The uniform kernel error times
`‖f‖₁²≤2a‖f‖₂²` gives the normalized tail bound `<3×10⁻¹⁷`; the exact norm is
positive. The normalized zero extension belongs to D_L because it is compactly
supported and piecewise polynomial, hence its Fourier transform is `O(1/r)` by
integration by parts and the logarithmically weighted L² tail converges. Thus
`𝒞(50,10⁻¹⁵)` is nonempty. It also contains a genuine L² neighborhood on the
unit sphere: if φ₀ is this normalized witness and φ ∈ D_L is unit with
`‖φ−φ₀‖₂≤2×10⁻⁸`, the tail-projection contraction and Plancherel give tail
norm at most `√(3×10⁻¹⁷)+2×10⁻⁸<2.6×10⁻⁸`, hence tail mass below
`6.76×10⁻¹⁶`. In particular the class contains infinitely many independent
directions, although the certified neighborhood is very small.

This class calculation does not validate the older high-m table, certify
membership of a proposed zero packet, or invoke NT-4. The unrestricted bound
in §7 is logically separate.

## 9. Verification appendix

Scripts in the session scratchpad (`calib2.py`, `calib3.py`, `calib4.py`,
`ledger.py`); reproduce with python3 + mpmath + numpy + scipy, ≤ 10 min total,
2 processes max. Key outputs (quoted verbatim from the runs):

- Instrument regression: spectral λ(7/4, m=48) = 3.1438949e−5 (RESULTS.md:
  3.14389e−5 ✓); λ(7/4, m=64) = 3.1415961e−5 (new point, consistent with the
  ladder's descent toward 3.12–3.14e−5).
- Boundary-flatness is numerically cheap, but is not a class-non-vacuity
  certificate: minimizing Q over
  (1−(x/a)²)^q·V_{64−2q} gives 3.142012e−5 / 3.142184e−5 / 3.142145e−5 /
  3.142727e−5 for q = 1/2/3/5 — within 0.04% of the unrestricted m = 64
  value. The corresponding Fourier-tail inequality was not enclosed. (A
  naive windowed minimizer, by contrast, scores 7.7e−2, illustrating that the
  margin's cancellation is delicate.)
- Galerkin argmins carry wiggle tails τ(287) ≈ 4e−7 ≫ τ̄ = 1.5e−16 — the
  proposed class therefore does NOT contain those finite-m argmins. Whether a
  proposed smooth packet or mollified profile meets the quoted tail threshold
  has not been certified.
- Envelope constants: κ₀' = 5.3722, c₀(7/4) = 14.352, c₋ = 6.352,
  r₊ = 286.95; c₀(497/200) = 15.621, c₋ = 7.621, r₊ = 1020.3.
- Capture at (m, aR) = (192, 124.31): B_m^* = 6.96e−25, β = 7.8e−13 —
  all capture terms negligible against √T₂·√τ̄ ≈ 7.8e−6.
- Content: √T₂ = 406.2 / 491.6 / 642.7 / 777.0 at m = 96/128/192/256
  (L = 7/4) — the F6 growth, measured.
- Wall: min over R of the unconditional split error ≥ 2.78 (attained toward
  small R; increasing in R): 5 orders above every window margin.
- Ledger rows as tabled in §7 (script `ledger.py` output, verbatim).

## 10. Lean decomposition and mathlib gap map

The m-dimensional certified core is already kernel-checked technology
(Theorem 2, THEOREMS.md). The mathematics between the existing artifacts and
a formal unrestricted statement now decomposes as follows:

| Lemma | Content | mathlib status |
|---|---|---|
| F0 | Fubini/Wiener–Khinchin for compactly supported L² | `MeasureTheory.integral_integral_swap` + `Real.fourierIntegral` basics: FORMALIZABLE NOW (days) |
| F1 | Lemma A(ii),(iv) digamma sandwich | the known gap (Gauss digamma integral, directed rounding) — unchanged from THEOREMS.md's bridge list |
| F2 | plane-wave Legendre coefficients and factorial tail | `LegendreTail`, `LegendrePlaneWave`, and `LegendreRodrigues` kernel-check the exact weight integral, sharp double-factorial bound, infinite geometric tail, repeated integration by parts, Rodrigues, phase conversion, and `FI(P_n)=2(-i)^n sphericalJIntegralModel n z`, including z=0. `LegendreOrthogonality`, `LegendreCoefficientTail`, and `LegendreScaled` prove exact normalization, arbitrary-interval scaling, normalized coefficients, and complete scaled tails. `LegendreL2` and `LegendreScaledL2` prove density/completeness, Parseval, canonical finite projections, exact residual tails, and the real/imaginary coefficient bridge. `LegendrePlaneWaveL2` proves the pointwise F2 leakage inequality; `IntervalZeroExtension` and `FullInfFourierBridge` perform the exact Fourier/Plancherel band normalization and prove `ρ≤81/10^23` for the actual p=2 band operator |
| F3 (weak) | K_m ≤ 1 and the πm²/2z branch (drop Landau) | Cauchy–Schwarz + |J_ν| ≤ 1-equivalent via the same integral rep: moderate; the Landau branch (c_L z^{−1/3}) should be DROPPED in the formal version — the ledger still closes at m = 192 with weaker coverage (γ₀ ≤ ~33, still zeros 1–5; verified in-session) |
| F4 | pure inequality algebra over ℚ given F0–F3 + certified λ_m | kernel-ready in the existing `CertFramework` style |
| F7 | monotonicity of Re ψ(1/4+ir/2) and the exterior symbol floor | `Glide.DigammaMonotone` proves continuity/evenness, candidate-series summability, the `tsum`/real-part bridge, positive slope, and exterior comparison from the derivative identity. `Glide.DigammaSeries` derives the complex trigamma derivative and every F7 consequence from locally uniform Euler GammaSeq convergence; `Glide.GammaUniform` proves that convergence unconditionally. `Glide.P2Symbol` proves the actual p=2 exterior comparison, while `Glide.DigammaBounds` proves the directed floor and band-defect bounds `109387/100000` and `7447/1000` |
| F8 analytic transfer | Plancherel, orthogonal projection, and a scalar two-by-two determinant | `CertFramework`, `FullInfTransfer`, `IntervalZeroExtension`, `FullInfFourierBridge`, `PoleProjectionL2`, `BoundedSymbolMultiplier`, `FullInfOperatorLedger`, and `FullInfP2Endpoint` kernel-check the Hilbert/projection transfer, actual p=2 band operator, leakage ledger, pole residuals, complement/cross bounds, and specialized determinant composition. `LegendreParityCoordinates` supplies canonical parity coordinates and actual basis-entry matrices. `SymbolQuadraticComparison` proves the exact clipped-versus-original multiplier-integral comparison. `RHBridge.P2Parity` proves exact parity decoupling, while `RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment` closes the even/odd interval premise and `p2_canonical_clipped_endpoint` closes the clipped endpoint. The original-integral transfer still assumes weighted integrability; identification with the zeta form is not claimed |
| F8–F10 finite clipped blocks | 600 (m=48), 1,640 (m=80), and 4,422 (m=132) Arb-enclosed Bessel/digamma integrals, then interval Cholesky | `FullInfClipped48.clipped48IntervalLowerBound` checks the exact rational LDL data, and `FullInfClipped48Real.clipped48IntervalLowerBoundReal` proves the same strict bound for every real matrix in the stored L=7/4 radius-10^-12 parity-block intervals. Canonical p=2/m=48 analytic containment is now independently kernel-checked with bounded rational certificates; m=80 and m=132 remain software-only, and zeta-form identification remains external |
| Class membership of NT-4 packets | explicit Gaussian-tail integrals | elementary; needed only for the composition corollary |

The shortest formal route has narrowed to one local analytic obligation:
define the truncated zeta form with its precise domain and prove its weighted
Fourier integrability/multiplier-plus-pole representation. F7, directed p=2
scalar bounds, Fourier normalization and leakage, poles, operator algebra,
canonical coordinates, parity decoupling, finite real-matrix certification, the exact
original-versus-clipped integral comparison, and their p=2 composition no
longer belong to the gap.
Completing the remaining identification would make the corresponding
unrestricted local inequality kernel-checked.
A separate, proved quantitative converse such
as NT-4 would still be required before stating a zero-exclusion region.

## 11. Remaining limitations, said without decoration

The full infimum is positive through L=749/250, an interior point of the
third prime-power regime, but only under the documented FLINT-Arb plus analytic
trust base. It is not yet Lean-checked. It does not establish positivity
beyond L=749/250, let alone at every support
size, so it is not RH. It also does not supply the proposed NT-4 converse and
therefore makes no standalone claim excluding a named zeta zero.

F5 remains a valid warning about one direct tail estimate, not a limitation on
F8: clipping changes the operator first and controls the low/high block by the
band leakage of V⊥. Extending the method to later prime thresholds will require
new clipped finite blocks; the exterior-floor argument itself generalizes to
every fixed L, but the margins become dramatically smaller. The next n=5
regime's required dimensions and Arb integration cost have not been certified.
