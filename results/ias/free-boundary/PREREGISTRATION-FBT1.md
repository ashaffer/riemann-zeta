# FB-T1 pre-registration — boundary trace and structured tails of the Galerkin argmin

Seat: free-boundary / potential theory. Timestamp: 2026-07-26 21:34:55 UTC.
Committed BEFORE any curve or trace was computed. One worker, budget ≤ 30 CPU-min.

## Configuration

ζ, L = 7/4 (a = 0.4375), spectral Legendre basis (`src/spectral_margins.py`,
`spectral_form` / `spectral_lam_min`), m ∈ {32, 48, 64}, dps 35 assembly / 28
solve (regression tolerance loosened accordingly). Bottom eigenvector c → float;
φ_m(x) = Σ c_k ν_k P_k(x/a), ν_k = √((2k+1)/2a).

Quantities:
- λ_m (regression: λ_48 must reproduce RESULTS.md 3.14389e−5 to ≤ 1e−3 relative,
  λ_64 ≈ 3.14160e−5 per FULLINF §8; else STOP, pipeline broken).
- trace t_m = φ_m(a), t'_m = φ_m(−a); derivative traces φ'_m(±a).
- transform φ̂(r) = Σ c_k ν_k · 2a(−i)^k j_k(ra) on period-averaged windows
  centered at r = 500, 1000, 2000, 3000 (content edge m/a ≤ 146 ≪ 500).
- trace-law ratio h_φ(r) = ⟨r²|φ̂|²⟩_window / (φ_m(a)² + φ_m(−a)²).
- corner-corrected remainder ψ = φ − (c₀ + c₁x)·1_[−a,a] with c₀, c₁ matching
  both endpoint values (ψ(±a) = 0); ψ̂ explicit;
  h_ψ(r) = ⟨r⁴|ψ̂|²⟩_window / (ψ'(a)² + ψ'(−a)²).
- tail mass τ_φ(R) = (1/2π)∫_{|r|>R}|φ̂|² at R = 287 (FULLINF's quoted point)
  and R = 1000; same for ψ.

## Pre-registered predictions

P1 (the trace exists and is small-but-nonzero): |t_m| ∈ [0.005, 0.05] for all
three m. Basis: FULLINF §8 measured τ(287) ≈ 4e−7 for Legendre argmins at this
window; the boundary-trace law τ(R) ≈ (2/π)φ(a)²/R inverts to |φ(a)| ≈ 0.013.
The minimizer is expected in the even block: |t'_m − t_m|/|t_m| ≤ 0.05.

P2 (the far tail is the trace's tail, nothing else): h_φ(r) ∈ [0.7, 1.3] on all
four windows at every m, and the log-log slope of ⟨|φ̂|²⟩ across the windows is
−2 ± 0.2. Consequently τ_φ(287) ∈ [1.5e−7, 1.2e−6] (i.e. FULLINF's 4e−7 is the
trace, quantitatively).

P3 (one explicit corner atom buys two powers of r): h_ψ(r) ∈ [0.5, 2] on the
windows r ≥ 1000, log-log slope of ⟨|ψ̂|²⟩ = −4 ± 0.3, and
τ_ψ(287)/τ_φ(287) ≤ 3e−4 (predicted ratio ~ (ψ'(a)/t·R)² ~ 1e−4–1e−5 modulo
the unknown ψ'(a); the ≤ 3e−4 gate is the falsifiable claim).

P4 (m-drift of the trace — the FB-3 discriminator, reported not gated):
q₁ = t_48/t_32, q₂ = t_64/t_48. H_const predicts q ≈ 1 ± 0.05;
H_log (boundary layer at Legendre endpoint resolution a/m², t ~ c/ln(m²))
predicts q₁ ≈ 0.90, q₂ ≈ 0.93. Prior 60/40 toward H_log (from the logarithmic-
Laplacian boundary-theory analogy, literature detail UNVERIFIED). The three-m
range cannot settle this; the numbers are recorded for the next rung.

Kill consequences: P2 or P3 failing kills the FB-3 corner-layer template as
formulated (the tail would not be trace-dominated / not atom-correctable);
P1 failing with t_m ≈ 0 (< 0.001) would mean the argmin tails are NOT boundary
driven and FULLINF's τ measurement has another source — FB-3 dies, F5's wall
stands unstructured.
