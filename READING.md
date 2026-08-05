# Reading order

A route into the mathematics this repository instruments, ordered so that each stage's
measurements (in `PROGRAM.md` §2) serve as your experimental companion.

## Stage 0 — understand the artifact before the literature

- [`publication/MATHEMATICAL-OVERVIEW.md`](publication/MATHEMATICAL-OVERVIEW.md):
  the local arithmetic Weil theorem, its proof architecture, and the exact
  all-support/zero-side gap.
- [`publication/LEAN-ANALYTIC-INFRASTRUCTURE.md`](publication/LEAN-ANALYTIC-INFRASTRUCTURE.md):
  the reusable analytic theorem arcs and their formal dependency boundaries.
- [`publication/CERTIFICATE-GUIDE.md`](publication/CERTIFICATE-GUIDE.md): why
  exact witnesses certify the last finite step without replacing the
  mathematical explanation.
- [`publication/NO-GO-THEOREM-GUIDE.md`](publication/NO-GO-THEOREM-GUIDE.md):
  the obstruction results grouped by their common mathematical mechanisms.

## Stage 1 — the problem and the explicit formula
- **Bombieri, "The Riemann Hypothesis"** (the official Clay problem description):
  the cleanest short statement of the problem, Weil's positivity criterion, and why
  the function-field case matters. Companion measurements: §2.5 (the two-sided
  identity to 29 digits) and `src/oracle.py`.
- **Edwards, *Riemann's Zeta Function*** and **Titchmarsh, *The Theory of the Riemann
  Zeta-Function***: the classical foundations; Riemann–Siegel, the argument function
  S(t), zero counting. Companion: `src/spectral_instruments.py` (census, Lehmer).
- **Iwaniec–Kowalski, *Analytic Number Theory***, ch. 5: the explicit formula in the
  exact shape used here (our §6 normalization ledger is that formula, certified).

## Stage 2 — the evidence and its limits
- **Farmer, "Currently there are no reasons to doubt the Riemann Hypothesis"**
  (arXiv:2211.11671): the strongest published defense of the consensus; read against
  the bias audit in the conversation record and §2's pre-asymptotic measurements.
- **Ivić, "On some reasons for doubting the Riemann hypothesis"**: the skeptical
  counterpart. Companion: the Mertens measurement (§2.3) — 0.472 observed vs a
  proven lim sup above 1.8.
- **Rodgers–Tao** (de Bruijn–Newman constant, Λ ≥ 0): the zero-slack theorem the
  margins keep rediscovering locally (§2.7, §2.12).

## Stage 3 — the positivity program (the door)
- **Connes–Consani, "Weil positivity and the trace formula, the archimedean place"**
  (Selecta 2021; arXiv:2006.13771): the conceptual root — positivity as a compressed
  trace, prolate spheroidal machinery.
- **Connes–Consani, "Spectral triples and ζ-cycles"** (arXiv:2106.01715): the
  archimedean failure past log 2, the prime-2 rescue, the 10⁻³ rigidity — the
  phenomena our margin meter reproduces and extends (§2.6–2.11).
- **Connes–Consani–Moscovici, "Zeta zeros and prolate wave operators"**
  (arXiv:2310.18423): the finite criterion P(n) — Euler factors below n, all n,
  equivalent to RH — the ladder Track A certifies.
- **Suzuki, "Weil's quadratic form via the screw function"** (arXiv:2606.09096):
  a parallel continuous-variable formulation.
- **arXiv:2607.02828** (finite Guinand–Weil dictionary): what finite numerics can
  and cannot certify about the truncated form — the theoretical frame for every
  caveat in this repository.
- **Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time"**
  (arXiv:2602.04022): the 2026 survey of the whole landscape.

## Stage 4 — context for the July 2026 recalibration
- **Alon–Bloom–Gowers–Litt–Sawin–Shankar–Tsimerman–Wang–Wood, "Remarks on the
  disproof of the unit distance conjecture"** (arXiv:2605.20695): the template for
  model-in-the-loop mathematics done right — sharp question, broad exploration,
  human-and-oracle audit.
- **Tao's blog, "A digestion of the Jacobian conjecture counterexample"** (July
  2026): the other template, and the reminder that expert consensus is a weaker
  signal than it feels.

## Stage 5 — the tools of the six tracks
- Interval arithmetic: **Johansson's ARB** documentation (Track A).
- Sums of squares / Positivstellensatz: **Parrilo's lecture notes** on SOS
  optimization; **Marcus–Spielman–Srivastava** interlacing families (Tracks B, C).
- Proof assistants: the **Lean/mathlib** analytic number theory development and the
  PrimeNumberTheoremAnd project (Track F).
- Random matrices: **Keating–Snaith**; **Conrey–Keating–Rubinstein–Snaith** on
  central values (the symplectic 3/2 law our §2.10 confirms empirically).

Throughout: whenever a paper states a phenomenon, check whether §2 of `PROGRAM.md`
measured it, then rerun the measurement yourself. The instruments were built so the
literature can be *experienced*, not only read.
