# PLAN — Graph theory and spectral combinatorics

Independent consultant plan, prepared 2026-07-26, without reading other experts' files.
Repo numbers cited below match `results/RESULTS.md`; new numbers are from a light probe
(float hat pipeline, parameters stated inline, subject to the ~1e−8 error budget measured
in §2.14 of `PROGRAM.md` — adequate at the 1e−1 to 1e−7 scales quoted). Probe recipe: all
probe quantities are reproducible in ~30 s from `src/weil_core.py` alone (`build_form`,
`hat_overlap`, `lam_min_of`) plus a 20-line sparse power iteration; exact constructions are
specified where each number appears.

---

## 1. Reformulation

Throughout, the objects and normalizations of `THEOREMS.md` are used: H_L = L²[−a, a],
a = L/4, Q_L = P + A − Π, λ(L) = inf of Q_L on unit vectors, ψ_φ(u) = ∫φ(x)φ(x+u)dx,
w_n = 2Λ(n)n^{−1/2}.

**1.1 The prime term is the adjacency operator of a windowed divisibility graph.**
Π(φ) = Σ_n w_n ψ_φ(log n) = ⟨φ, (Σ_n w_n Sym T_{log n}) φ⟩, where T_u is translation by u
and Sym T_u = (T_u + T_u*)/2. The generators ±log n over prime powers n < e^{L/2} generate
the log-embedded multiplicative group ℚ₊^× ≅ ℤ^{(P)} (free abelian on the primes). So Π is
the weighted adjacency operator of a Cayley-type graph — vertices: the window [−a, a];
edges: x ~ x ± log n with weight Λ(n)n^{−1/2} — i.e., the **covering relation of the
divisibility lattice**, windowed. The orbit of a generic point is a set of log-rationals;
the orbit of 0 restricted to positive positions is {log m : m ≤ e^{L/2}}, the divisibility
graph on integers whose Redheffer matrix (det = Mertens M(n), verified in §2.3 of
`PROGRAM.md`) is the program's own combinatorial shadow. Weil positivity, RH-equivalently,
is the domination

  A(G_div) ⪯ (rank-2 pole term) + (archimedean log-potential),   for every window length,

which is exactly the *shape* of an expander mixing inequality (Alon–Chung, Discrete Math.
72 (1988) 15–19): adjacency ⪯ main term + small error. The catch, made precise in 1.3, is
that here the "error term" is the zero-side frame — the mixing inequality *is* the explicit
formula, term for term.

**1.2 Incidence-algebra normal form (the Redheffer connection made exact).** On the integer
sublattice define the symmetric N×N matrix

  M_N[i, j] = Λ(j/i)·(j/i)^{−1/2}  if j/i is a prime power (either direction),  0 else.

Then Π restricted to lattice fibers is the quadratic form of M_N (entries Λ(n)n^{−1/2} =
w_n/2 on both triangles — this is exactly `hat_overlap(Dm ± log n)`'s band structure in
`src/weil_core.py`). In the reduced incidence algebra of the divisor poset (≅ formal
Dirichlet series), the unweighted pattern is log Z, where Z[i,j] = 1 iff i|j is the poset
zeta matrix and (log Z)[i,j] = Λ(r)/log r at ratio r = j/i, because log ζ(s) =
Σ Λ(n)(log n)^{−1} n^{−s}. With Δ = diag(n^{1/2}), M_N = Sym(Δ^{-1} C Δ) where C ↔
−ζ'/ζ(s + 1/2): **the prime operator is the multiplicative Toeplitz matrix whose symbol is
the truncated critical-line logarithmic derivative of ζ.** Its Fourier analysis over the
characters n ↦ n^{−it} of ℚ₊^× returns −2 Re Σ_{n≤N} Λ(n) n^{−1/2−it} — the graph "hears"
ζ'/ζ on the critical line. This object class (multiplicative Toeplitz operators, Bohr lift
to H²(𝕋^∞)) is studied by Hilberdink (Acta Arith. 139 (2009) 331–344, and subsequent work)
and sits over the Hedenmalm–Lindqvist–Seip Dirichlet-series Hilbert space (Duke Math. J. 86
(1997) 1–37). The Redheffer spectral literature (Barrett–Forcade–Pollington, Linear Algebra
Appl. 107 (1988) 151–159; Vaughan, "On the eigenvalues of Redheffer's matrix" I, Lect.
Notes Pure Appl. Math. 147 (1993) 283–296; II, J. Austral. Math. Soc. A 60 (1996) 260–273)
is the unweighted, s = 0 cousin.

**1.3 Three tiers, and where the war is.** An exact identity organizes everything. Since
P(φ) = 2(∫φe^{x/2})(∫φe^{−x/2}) = 2∫_{−2a}^{2a} ψ_φ(u) e^{−u/2} du, and the PNT main term
of Π is Π_main(φ) := 2∫_0^{2a} ψ_φ(u) e^{u/2} du (from dψ(e^u) ≈ e^u du),

  P(φ) − Π_main(φ) = 2∫_0^{2a} ψ_φ(u) e^{−u/2} du,   |P − Π_main| ≤ 4‖φ‖².     (T1)

So the graph decomposes in three tiers:
- **Tier 1 (Perron / pole).** The divisibility graph's Perron growth is exponential — the
  flat direction has Π(𝟙/√(2a)) ≈ 4e^{L/4}/(L/4) — and is cancelled *identically, up to a
  bounded form*, by the pole term, by (T1). This is PNT-as-graph-fact. Probe check (hat
  m = 61, pencil (Π, G) vs (Π − pole, G) via `build_form` extras): λ_max(Π) =
  0.90 / 1.17 / 1.52 / 1.91 at L = 2.485 / 3.0 / 3.555 / 4.025, against ℓ¹ (degree) bounds
  5–12 — and the cosh(x/2) direction carries Π-Rayleigh 0.56…1.74 vs pole-Rayleigh
  2.54…4.33: the pole over-covers the Perron cone at small L.
- **Tier 2 (log-potential balance).** After the tier-1 twist, the graph's spectral radius
  is logarithmic, not exponential: Lemma G1 below proves λ_max(M_N) ≤ log N + 2.78
  *unconditionally* — an exponential improvement over the degree bound 4√N, by a two-line
  telescope. Meanwhile the archimedean weight at the Nyquist height T*(L) = 2πe^{L/2} is
  W(T*) = log(T*/2π) + O(1) = L/2 + O(1) = log N + O(1) (Lemma A of `THEOREMS.md`). **The
  leading balance of Weil positivity is the coincidence of the windowed divisibility
  graph's Perron value with the arch potential at Nyquist — both are log N + O(1).**
- **Tier 3 (envelope).** Everything below O(1) — the measured ln λ(L) ≈ 10.2 −
  1.755·e^{L/2}(L/2+4) — is cancellation the graph bounds cannot see (Section 5).

The unitary dictionary behind tier 1/2: counting measure on integers ≤ N is Lebesgue
measure e^x dx under x = log t, and the multiplication by e^{x/2} that flattens it
conjugates T_u to e^{u/2}T_u — i.e., **M_N is the pole-twisted window**, and the Chebyshev
identity Σ_{d|n} Λ(d) = log n implements tier-1 cancellation exactly on the lattice. The
two-sided continuum window contains untwisted directions, which is why raw λ_max(Π_L)
grows toward e^{L/4} and only the pole subtraction reveals tier 2 (measured: λ_max of the
pole-subtracted pencil = 1.42 / 1.62 at L = 3.555 / 4.025, close to L/2 − 0.56; see P2).

**1.4 Frame side.** λ(L) is the lower frame bound of the exponentials at zero ordinates
(§2.14(v)); the Gram matrix of that system is a sinc-kernel matrix *on the zeros* — the
graph-on-frequencies dual of the graph-on-the-window above. Landau–Widom asymptotics
(Landau–Widom, J. Math. Anal. Appl. 77 (1980) 469–481) govern its plunge; the measured
staircase/Poisson mechanism experiment (§2.17) says the plunge constant is a density
functional. My field's tools act on the prime side; the frame side belongs to harmonic
analysis (Interfaces).

**1.5 The function-field precedent, honestly located.** For a (q+1)-regular graph, the
Ihara zeta function satisfies RH iff the graph is Ramanujan (Ihara, J. Math. Soc. Japan 18
(1966) 219–235; Terras, *Zeta Functions of Graphs*, CUP 2010, Ch. 7) — discrete Weil
positivity. Lubotzky–Phillips–Sarnak (Combinatorica 8 (1988) 261–277) built such graphs
*from* Deligne; Marcus–Spielman–Srivastava built them from scratch by interlacing families
(Ann. of Math. 182 (2015) 307–325). The divisibility graph can never be an expander — it is
a Cayley graph of an abelian group, its symbol's sup over the dual 𝕋^∞ equals the degree
4e^{L/4}, and amenability forbids any gap on the free group ℤ^{(P)}. All spectral gain must
come from the window, the n^{−1/2} weights, and the pole. What the precedent transfers is
not expansion but **positivity technology that certifies spectral edges without
diagonalizing**: interlacing families, mixed characteristic polynomials, barrier arguments
(MSS), and two-sided spectral sparsification (Batson–Spielman–Srivastava, SIAM J. Comput.
41 (2012) 1704–1721). Those are the engines of Section 2.

---

## 2. Lemma candidates

### Lemma G1 (Perron balance of the windowed divisibility matrix)

**(a) Statement.** Let M_N be as in 1.2. Then, unconditionally, for all N ≥ 2:

  λ_max(M_N) ≤ log N + B₀,  with B₀ = 2.78 admissible
  (B₀ = 2 from Mertens' |Σ_{p≤x}(log p)/p − log x| ≤ 2, plus Σ_p log p/(p(p−1)) < 0.78);

and λ_max(M_N) ≥ log N − 3 for N ≥ 100. Moreover the Perron vector v satisfies
⟨v, u⟩ ≥ 1 − c/log N with u ∝ (n^{−1/2})_{n≤N} — the pole direction e^{−x/2} in log
coordinates. Conjectured sharp form: λ_max(M_N) = log N − γ + o(1).

**(b) Proof strategy.** Upper bound: Schur test with weights h_n = n^{−1/2}. Row i
splits into up-steps (multiples j = in): Σ_{n≤N/i} Λ(n)/n ≤ log(N/i) + B₀ (Mertens), and
down-steps (divisors j = i/n): Σ_{p^k | i} Λ(p^k) = log i **exactly** (Chebyshev's
identity). Total: log N + B₀, independent of i — the row sums telescope. Lower bound:
Rayleigh quotient of u = (n^{−1/2}): ⟨u, M_N u⟩/⟨u,u⟩ = (2/H_N)·Σ_{i≤N} i^{−1}
Σ_{n≤N/i}Λ(n)/n = log N + 2γ − 4 + o(1) with Mertens two-sidedly. Perron localization:
spectral gap from the down-step defect for vectors orthogonal to u. Sharp constant: the
Perron eigenvalue equation is a discrete Mellin/Wirsing-type equation; second-order
asymptotics via Hilberdink's multiplicative-Toeplitz machinery.

**(c) Hardest missing step.** Not the bound (that proof is complete as sketched) — the
**continuum port**. The two-sided window's fibers are *rationals*, and there the Schur
telescope fails: down-steps from position x cost Σ_{n ≤ e^{x+2a}} Λ(n) ≈ e^{x+2a}
(exponential), because denominators reintroduce the tier-1 growth. Only the rank-2 pole
subtraction removes it, and rank-2 cannot be absorbed in a diagonal Schur weight. The
continuum companion must therefore be stated *after* pole completion — which is Lemma G2.

**(d) Difficulty.** Upper/lower bounds with explicit constants: days (the proof is above).
Perron localization: weeks. Sharp constant −γ: months (and check against Hilberdink first
— possible prior art; the windowed Λ-weighted case at s = 1/2 is, to my knowledge, not in
his published norms, which treat symbol classes with convergent Dirichlet series).

**(e) Numerical stress-test (executed).** Sparse power iteration (edges (i, in),
weight Λ(n)/√n; bincount matvec):

  | N | λ_max | λ_max − log N | ⟨v, n^{−1/2}⟩ | λ₂ (by modulus) | edges |
  |---|---|---|---|---|---|
  | 10³ | 6.3577 | −0.5500 | 0.999874 | −5.677 | 2,877 |
  | 10⁴ | 8.6533 | −0.5571 | 0.999948 | −7.891 | 31,985 |
  | 10⁵ | 10.9518 | −0.5611 | 0.999973 | −10.134 | 343,614 |
  | 10⁶ | 13.2517 | −0.5638 | 0.999985 | — | 3,626,619 |

  The bracket holds, the deficit drifts toward −γ = −0.5772 (P1), and the Perron vector is
  the pole direction to 5 decimals. Bonus structure: the second-by-modulus eigenvalue is
  ≈ −λ_max + 0.7–0.8, a near-bipartite reflection — conjugation by the Liouville sign
  diag(λ(n)) negates every edge of odd prime-power order p^k, k odd, which is all but an
  O(1) total weight of the graph; the surviving asymmetry is the graph twin of the
  family's all-drain χ = −1 configuration. Repo follow-up:
  λ_max at N = 10⁷ (P1); and the continuum λ_max of the pole-subtracted pencil across
  L = 4…6 in the spectral basis (P2).

### Lemma G2 (pole completion: tier-1 domination with explicit PNT error)

**(a) Statement.** For every L > 0 and unit φ ∈ H_L, with E_L(φ) :=
2∫_0^{2a} ψ_φ(u) e^{−u/2} d(ψ(e^u) − e^u)  (Stieltjes; ψ(x) = Chebyshev's function):

  Q_L(φ) = A(φ) + 2∫_0^{2a} ψ_φ(u) e^{−u/2} du − E_L(φ),

hence, unconditionally,

  λ(L) ≥ ψ(1/4) − log π − 4 − ‖E_L‖,   and
  ‖E_L‖ ≤ C·exp(L/4 − c·(L/2)^{1/2})   with C, c explicit (from |ψ(x) − x| ≤
  C₁ x·exp(−c₁√(log x)), e.g. explicit de la Vallée Poussin constants; sharpened below the
  Platt–Trudgian verification height 3·10¹² to ‖E_L‖ ≤ C₂ e^{L/8}-type via |ψ(x) − x| ≪
  √x log²x there, i.e. for L/2 ≤ log(3·10¹²) ≈ 28.7).

**(b) Proof strategy.** The displayed identity is exact: P = 2∫_{−2a}^{2a}ψ_φ e^{−u/2}du
(substitute y = x + u in the double integral) plus Π = Π_main + E_L by definition of the
Stieltjes integral; (T1) of 1.3 assembles it. For ‖E_L‖: split [0, 2a] into unit blocks;
on each block Abel-sum against ψ(e^u) − e^u using |ψ_φ| ≤ 1 and the block variation of
ψ_φ(u)e^{u/2} controlled crudely (|ψ_φ| ≤ 1 suffices for the stated bound; Lemma D of
`THEOREMS.md` sharpens near-minimizer blocks by (log 1/Δ)^{−1} if wanted). Sum the block
errors: geometric-in-u weight e^{u/2} times PNT block error e^{u/2}exp(−c√u).

**(c) Hardest missing step.** None to the stated bound — this is bookkeeping plus explicit
PNT inputs (Rosser–Schoenfeld, Illinois J. Math. 6 (1962) 64–94; Platt–Trudgian, Bull.
LMS 53 (2021) 792–797; Büthe-type explicit ψ bounds). The hard and important step is the
**diligence check**: whether arXiv:2607.02828 (finite-cutoff theorems) already contains
this exact unconditional floor. If yes, G2 reduces to citation and its value here is the
graph reading: *elementary reasoning about the divisibility graph reaches
λ(L) ≥ −C e^{L/4 − c√(L/2)}, and every improvement of the exponent is a zero-free-region
statement* — the tier map of what combinatorics can and cannot see.

**(d) Difficulty.** Weeks (mechanical, given explicit PNT constants); the identity part,
days. Improving the error to e^{εL/4} for all L: equivalent to quasi-RH — not a target.

**(e) Numerical stress-test.** Cheap and decisive: compute Π_main by quadrature on the hp
minimizers at L = 1.75, 2.485, 3.0 and verify (i) P − Π_main = 2∫ψ_φe^{−u/2}du to machine
precision (identity check), (ii) |E_L(φ_min)| against Q_L(φ_min) − A(φ_min) −
2∫ψ_φe^{−u/2}du, (iii) the growth rate of sup over the Galerkin ball of |E_L| across
L = 2…6, fitted against e^{L/4−c√(L/2)}. Any violation of (i) is a bug (oracle
discipline); a measured |E_L| growth rate *above* e^{L/4} kills the lemma's constants.

### Lemma G3 (band leverage ledger: the entering prime against the coercive landscape)

**(a) Statement.** Let R_L := A + (1 − ψ(1/4) + log π)·I (coercive: R_L ⪰ I + W₊ by Lemma
A(ii) of `THEOREMS.md`), and for each prime power n < e^{L/2} let B_n = w_n Sym T_{log n}
and define the two-sided leverage τ_n(L) := sup_{φ≠0} |⟨φ, B_nφ⟩| / ⟨φ, R_Lφ⟩. Then:

  (i) [provable now] τ_n(L) ≤ w_n · min( 1, C₃·(log(1/δ_n))^{−1/2} ),
      δ_n := L/2 − log n ≤ 1,  with C₃ explicit via Lemmas C and E of `THEOREMS.md`
      applied with the *R-energy* in place of the near-minimizer bound C_B — i.e., an
      entering band is weakly coupled *relative to the log-potential*, uniformly in n and
      L, not only on near-minimizers.

  (ii) [conjecture-grade; this is UPT in transfer coordinates] There is a frequency-dyadic
      refinement: with R replaced by its Littlewood–Paley pieces R^{(j)} (arch weight
      localized to |r| ∈ [2^j, 2^{j+1})) and the bands decomposed accordingly, the
      interference Gram H[n,m] = tr(R^{−1}B_n R^{−1}B_m) is diagonally dominant after
      envelope normalization, uniformly in L. Diagonal dominance of H uniformly in L,
      plus (i), implies per-prime local certificates of bounded complexity — Track B's
      block hypothesis — and is the graph-side formulation of the renormalized transfer
      lemma of `PROGRAM.md` §3.

**(b) Proof strategy.** For (i): |ψ_φ(log n)| ≤ (∫_sliver φ²)^{1/2} (Cauchy–Schwarz on the
width-δ_n sliver, Lemma E), and sliver mass ≤ C/log(1/δ) in terms of W₊(φ) ≤ ⟨φ, R φ⟩
(Lemma C rerun with R-energy — no minimizer hypothesis needed since R is itself the
log-weight). For (ii): compute H, identify its dominant off-diagonal pattern (expected:
pairs n, m with nm or n/m a prime power ≤ e^{L/2} — the 4-cycles of the divisibility
graph), and attempt a Schur-complement/paving argument in the style of Kadison–Singer
discrepancy (Weaver, Discrete Math. 278 (2004) 227–239; MSS, Ann. of Math. 182 (2015)
327–350) on the band Gram rather than on vectors.

**(c) Hardest missing step.** The measured totals kill any *unnormalized* summed bound:
probe values (hat m = 41, R as defined, per-band generalized extreme eigenvalues) —
L = 3.0: τ₂,τ₃,τ₄ = 0.128, 0.120, 0.050, Σ = 0.298; L = 4.04: 0.179, 0.158, 0.075,
0.136, 0.077, Σ = 0.624. The sum doubles per window and scales like e^{L/4}; it crosses 1
near L ≈ 5.3 (P2-adjacent), so no triangle-inequality assembly survives. Everything rests
on the interference structure (ii) after envelope normalization — and the correct
normalization needs the Landau–Widom envelope from harmonic analysis (Interfaces). This is
where the plan is genuinely open: (ii) restated *is* the target lemma, not a lemma toward
it, unless the H-structure turns out to be forced by (i)-type local estimates.

**(d) Difficulty.** (i): weeks (proof path fully visible, constants explicit). (ii):
research-program; possibly the program's own M3 in different clothes.

**(e) Numerical stress-test.** (Partially executed, above.) Full test the repo should run
before proof attempts: assemble H[n,m] in the spectral basis at L = 3.0, 3.555, 4.025,
5.0; report (α) the diagonal-dominance ratio per row, (β) the top eigenvector of H (which
prime coalition threatens positivity), (γ) τ_n(δ) as δ_n → 0 at the p = 3 threshold
against the predicted (log 1/δ)^{−1/2} — the operator-level glide already measured (§2.17,
ratio 0.973 over ±0.001) says τ must vanish at entry; the *rate* tests (i). Kill signals:
top eigenvector of H spread over Ω(e^{L/4}) bands with coherent sign (per-prime blocking
structurally false), or τ_n(δ) flattening at a positive floor as δ → 0 in the spectral
basis (would contradict Lemma E's mechanism, and Theorem 1's proof route with it).

### Lemma G4 (signing rigidity: the arithmetic signing is the unique positive vertex)

**(a) Statement.** For σ ∈ {±1}^{K(L)} (one sign per prime-power band n < e^{L/2}), let
Q_L^σ = A + P − Σ_n σ_n B_n, so Q_L^{(+,…,+)} = Q_L. Two statements:

  (A) [finite, certifiable] At L = 497/200 on the 12-dimensional Legendre space of
      Theorem 2 (`THEOREMS.md`), λ_min(Q^σ) < 0 for every σ ≠ (+,+); i.e., the
      machine-checked positivity window is *sign-rigid*: the positivity cone of the
      signing polytope is the single arithmetic vertex.

  (B) [structural, open] The family {Q_L^σ}_σ, refined along any rank-one resolution of
      the bands, forms an interlacing family in the MSS sense (common interlacers /
      real-rooted mixed characteristic polynomials), and the arithmetic signing attains
      max_σ λ_min(Q_L^σ) for all L — with the pole term as the mechanism (the pole flip
      of §2.11 is what orients all-plus to the top; pole-free landscapes reverse it).

**(b) Proof strategy.** (A): interval Rayleigh upper bounds — one certified vector per
wrong signing — with the existing `src/certified_spectral.py` machinery; then optionally
the Lean route of Theorem 2 for a kernel-checked "uniqueness of the arithmetic signing"
companion theorem. (B): decompose each band into rank-ones B_n = Σ_k v_{n,k}v_{n,k}* −
Σ_k u_{n,k}u_{n,k}* (Sym T_u has explicit ±1-spectrum resolution on the window); the MSS
multivariate barrier controls expected characteristic polynomials under *independent*
signs; the obstacle is that our K signs are shared within bands (correlated rank-ones).
Attempt: treat bands as matrix-valued signs and use the finite free convolution calculus
(MSS, Probab. Theory Related Fields 178 (2020) 795–841) for the band ensemble; compare the
smallest root of the mixed characteristic polynomial with the measured λ_min(Q_L).

**(c) Hardest missing step.** For (B), real-rootedness/common interlacing for
*correlated* rank-one packets — outside every proved MSS setting; and even granted it,
interlacing families certify that *some* signing beats the mixed-char-poly root, while RH
needs the *arithmetic* signing; the identification "arithmetic = argmax" is exactly where
the arithmetic re-enters. If that identification requires knowing positivity, (B) is
circular for proving; it retains value as *structure detection* (see stress test).

**(d) Difficulty.** (A): days (compute), weeks (Lean companion). (B): likely-open;
months to settle whether the band ensemble's mixed characteristic polynomial is even
real-rooted at one window (a finite computation on 12×12 matrices can *refute* it).

**(e) Numerical stress-test (executed at float level).** Full signing sweep, hat m = 41,
ζ landscape (`build_form`; per-band matrices from `hat_overlap(Dm + log n, d)`):

  - L = 3.0 (bands 2, 3, 4; 8 free / 4 multiplicative signings): arithmetic all-plus
    λ_min = +7.87e−7 is the **unique positive signing** (1/8); best wrong signing
    (flip n = 4): −0.249; worst (all-minus): −1.687.
  - L = 4.04 (bands 2, 3, 4, 5, 7; 32 free / 16 multiplicative): all-plus +7.77e−7,
    again **unique positive of 32**; best wrong (flip n = 7): −0.424; worst: −2.670.

  Every single band is individually necessary — sign-flip rigidity in the same sense as
  Connes–Consani's 2 → 1.9999 weight rigidity (10⁻³), here with discrete flips at
  O(10⁻¹)–O(1) cost against a +8e−7 margin: a rigidity ratio of 10⁵–10⁶. Repo follow-ups
  before any proof attempt on (B): (α) rerun in the spectral basis at m ≥ 32 (float
  ranking is safe at these gaps); (β) L = 5.5 sweep (9 bands, 512 signings) — P3 predicts
  uniqueness persists; (γ) compute the mixed characteristic polynomial over uniform signs
  at L = 497/200 on the 12-dim space (32 determinants of 12×12 — exact rational) and
  test real-rootedness; a failure refutes the naive (B) immediately and cheaply.

---

## 3. Predictions

**P1 (lattice Perron constant).** λ_max(M_N) − log N converges to −γ = −0.5772…:
concretely, at N = 10⁷ the value is −0.566 ± 0.004 (i.e. λ_max = 15.552 ± 0.004), and the
N → ∞ limit lies within 0.010 of −γ. Basis: measured −0.5500 / −0.5571 / −0.5611 /
−0.5638 at N = 10³…10⁶ with per-decade decrements shrinking by ×0.65, plus the Rayleigh
identity ⟨u, M_N u⟩/⟨u,u⟩ = log N − (4 − 2γ) + o(1) for u = n^{−1/2} whose deficit is
recovered by Perron optimization. Falsified if the deficit drifts past −0.60 or stalls
above −0.545. (Also: Perron overlap with n^{−1/2} at N = 10⁷ exceeds 0.99999.)

**P2 (continuum tier split and crossover).** In the hat basis m = 61 (for comparability
with the probe anchors 0.90 / 1.17 / 1.52 / 1.91 at L = 2.485 / 3.0 / 3.555 / 4.025):
λ_max of the prime-only pencil crosses L/2 at L = 4.4 ± 0.2 (the flat-vector Rayleigh
quotient Π(𝟙/√(2a)) = 2Σ_n Λ(n)n^{−1/2}(1 − log n/(L/2)) reaches L/2 there), and at
L = 6 lands in [4.0, 6.0]
— while the pole-subtracted pencil stays at tier 2: λ_max(Π − pole) = L/2 − 0.56 ± 0.5
throughout L ∈ [4, 6] (measured 1.42, 1.62 at L = 3.555, 4.025 vs L/2 − 0.56 = 1.22,
1.45). The exponential/logarithmic split between the raw and pole-subtracted tops,
≥ 1.5 units by L = 6, is the tier-1 signature (T1); its absence falsifies the
pole-completion picture of G2.

**P3 (signing uniqueness persists).** In the spectral (Legendre) basis, m ≥ 32: at every
L ∈ [2.5, 5.5] the arithmetic all-plus signing remains the unique positive signing of the
free band-signing ensemble — in particular 1 of 512 at L = 5.5 — and the best wrong
signing at L = 4.04 has λ_min ≤ −0.35 (measured −0.424 in hats; spectral shifts these by
O(10%), cf. the 17% hat-vs-spectral bias of §2.16). A second positive signing anywhere in
the range kills Lemma G4(A)'s extension and the sign-rigidity reading; conversely
uniqueness at L = 5.5, where 9 bands interact, is strong evidence that the positivity cone
in signing space is exactly the arithmetic ray for all L (the graph twin of zero slack).

---

## 4. Interfaces

**What my lemmas NEED.**
- From **analytic number theory**: explicit Mertens/PNT constants (Rosser–Schoenfeld;
  Platt–Trudgian; explicit de la Vallée Poussin constants, e.g. Ford's) for G1's B₀ and
  G2's ‖E_L‖; the diligence read of arXiv:2607.02828 against G2; one-level density for
  the quadratic family (Özlük–Snyder, Acta Arith. 91 (1999) 209–228; Katz–Sarnak, Bull.
  AMS 36 (1999) 1–26; Soundararajan, Ann. of Math. 152 (2000) 447–488) to calibrate what
  ensemble-averaged positivity is already a theorem, so G4's ensemble language doesn't
  reprove or under-claim it.
- From **harmonic analysis**: the Landau–Widom/prolate normalization of the envelope —
  G3(ii) cannot even be *stated* sharply without the envelope functional env(L) that the
  smooth-staircase experiment (§2.17) shows is density-determined; also Littlewood–Paley
  splitting of the arch weight for the dyadic reference R^{(j)}.
- From **convex optimization (Track B)**: SOS certificates reported *band-resolved* —
  the sparsity pattern of machine certificates over prime blocks is the dual witness of
  G3(ii)'s diagonal dominance; and the multivariate barrier method (which is convex
  analysis) for G4(B).
- From **numerical analysis / formal methods**: certified sparse extremal-eigenvalue
  enclosures at N = 10⁷ for P1; interval Rayleigh certificates for the 31 wrong signings
  (G4(A)) and a Lean companion via the Theorem-2 pipeline; deep spectral-basis runs for
  P2/P3.

**What my field OFFERS.**
- The incidence-algebra / multiplicative-Toeplitz normal form (1.2): a shared exact
  language for Tracks B and C; the Redheffer corpus imported with it.
- The Schur–Chebyshev telescope (G1): an elementary lemma engine for domination proofs —
  candidate substitute for compactness in glide-type arguments, exportable to the family
  (conductor-shifted telescopes).
- The tier decomposition with the exact identity (T1): organizes every future
  unconditional bound; G2's floor λ(L) ≥ −C e^{L/4 − c√(L/2)} tells the certified ladder
  exactly what is and is not worth certifying at large L.
- The leverage/effective-resistance formalism (G3): UPT restated in per-band measurable
  inequalities; plus BSS-style band thinning (Batson–Spielman–Srivastava; Spielman–
  Srivastava, SIAM J. Comput. 40 (2011) 1913–1926) with Lemma D/E-certified truncation
  error for the M2 breadth ladder (p ≤ 50: certify with O(m/ε²) effective bands instead
  of all prime powers).
- The signing polytope (G4): the cleanest ensemble-vs-individual laboratory the program
  has; 32-point ground truth for any proposed transfer inequality (a candidate inequality
  that also "proves" positivity for a wrong signing is refuted instantly).
- Moment translation: closed walks of the divisibility graph = the Diophantine sums of
  pair-correlation heuristics; tr(Π^k) computations as cross-checks for Track E.

**Composition map (lemma × discipline).**
- G2 ∘ explicit PNT (number theory) → the unconditional floor, with constants — finishable
  jointly in weeks.
- G1 ∘ Wirsing/Hilberdink asymptotics (number theory) → the −γ constant; G1 ∘ certified
  sparse eigensolvers (numerical analysis) → a *certified* Perron-balance theorem at 10⁷.
- G3(i) ∘ Lemma C/E machinery (already in-house) → provable now; G3(ii) ∘ Landau–Widom
  (harmonic analysis) ∘ SOS block reports (convex optimization) → the renormalized
  transfer target; this triple is my best guess at where M3 actually lives.
- G4(A) ∘ interval certification/Lean (formal methods) → a machine-checked arithmetic-
  rigidity theorem within days of effort; G4(B) ∘ MSS barrier (convex optimization) →
  settle real-rootedness at one window by exact computation before anyone invests in
  proof.
- **Algebraic geometry**: no composition claimed. The honest content of the function-field
  precedent here is constraint, not construction: any candidate "curve-side" object
  (Track E) must, on discretization, reproduce the tier structure of 1.3 — Perron pair
  cancelled by a rank-2 term, log-scale balance, and a density-functional envelope. I do
  not have a lemma that touches the Frobenius side.

---

## 5. Honest assessment

The strongest objection: **every tool my field owns is magnitude-driven, and this problem
is cancellation-driven below the log scale.** My provable statements (G1, G2) bound the
divisibility graph at tier 1 and tier 2 — an exponential improvement over degree bounds,
achieved by exactly the two classical identities (Mertens, Chebyshev) that encode PNT —
and they terminate at an unconditional floor of order −e^{L/4 − c√(L/2)}. The target sits
at +e^{−1.755·e^{L/2}(L/2+4)}. The distance between those two numbers is not a technical
gap; it is the Riemann Hypothesis, and no Schur weight, interlacing family, sparsifier, or
mixing inequality known to me closes a super-exponential cancellation gap. Where a graph
method appears to reach further (the expander-mixing framing of 1.1), inspection shows the
"error term" it would need to bound *is* the zero-side frame: the mixing inequality for
the divisibility graph, with its true error term, is the explicit formula restated. Per
the coordinator's instruction, I flag this plainly: the "expander mixing as positivity
transfer" angle from my own brief did **not** survive crystallization into a lemma — G2 is
its only honest residue.

Three more specific self-objections. (1) *The mechanism experiment cuts against me*: §2.17
shows the envelope is a functional of the counting function alone — smooth staircase
reproduces the true margins, and even Poisson only costs the offset. Whatever my field's
discrete structures (signings, cycles, divisibility combinatorics) govern, it is confined
to the offset and below — precisely the part of the problem below the program's current
resolution. (2) *Amenability*: the divisibility graph is a Cayley graph of ℤ^{(P)}; no
expansion exists to be found, and the Ramanujan analogy is inspiration, not mechanism. The
measured signing sweep sharpens this into a warning about all ensemble methods: the
arithmetic signing is the unique positive point among 32 — positivity is a measure-zero
conspiracy in sign space, so no averaging, concentration, or "most signings" argument can
see it; MSS's exists-quantifier coincides with the arithmetic point only because that
point happens to be the maximum, and proving *that identification* looks as hard as
positivity itself (G4(c)). (3) *Base rate*: the Redheffer spectral program —
Barrett–Forcade–Pollington through Vaughan — produced clean theorems and no Mertens
progress in nearly four decades; my G1 is recognizably a member of that genre, one
diagonal twist away, and should be priced accordingly.

What survives the objections: the reformulation (1.2–1.3) is exact and shared; G1 and G2
are real, finishable theorems that fix the tier map and the unconditional floor; G3(i) is
provable and G3's stress tests are cheap and decisive about where the transfer structure
lives; G4(A) is a certifiable rigidity theorem that extends the program's flagship Lean
artifact; and the three predictions are numerical, dated, and killable. If the
harmonization round finds that harmonic analysis can supply env(L) as a theorem (Landau–
Widom with Riemann–von Mangoldt density), then G3(ii) — the leverage ledger normalized by
that envelope — is the single place where my field's technology could touch the actual
open lemma. If it cannot, my honest expectation is that this plan's lasting contributions
are the floor (G2), the rigidity certificates (G4A), and the toy theorem (G1) — supporting
instrumentation, not the door.
