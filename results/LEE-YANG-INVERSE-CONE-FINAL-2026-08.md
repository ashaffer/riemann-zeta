# Final finite Lee--Yang inverse-cone test

Status: completed fail-fast audit, 2026-08-04.  The model-free finite
Lee--Yang cone survives through order 40 / Hankel dimension 20.  A narrower
independent weighted-spin cone is rigorously falsified at Hankel dimension 16.
No RH claim is made.

## 1. The legitimate model-free cone

Normalize the centered xi function by

`M(h)=xi(1/2+h)/xi(1/2)`.

Newman's Hadamard factorization says that an even moment-generating function
of order at most two with purely imaginary zeros has the form

`M(h)=exp(b h^2) product_j (1+h^2/alpha_j^2)`,  `b>=0`.

Writing

`log M(h)=sum_(n>=1) (-1)^(n-1) a_n h^(2n)/n`,

gives, apart from the Gaussian contribution to `a_1`,

`a_n=sum_j alpha_j^(-2n)`.

Thus `a_n>=0`, and the two Stieltjes Hankel localizers

`H0_d=(a_(i+j+1))_(0<=i,j<d)`,

`H1_d=(a_(i+j+2))_(0<=i,j<d)`

must be positive semidefinite.  This is a canonical, well-defined model-free
inverse cone available from finitely many centered log coefficients.  A
certified failure for xi would refute its
purely-imaginary-zero property and hence RH.  A finite pass proves only
truncated Stieltjes consistency.

Primary sources are Newman's Proposition 2 and Theorems 3 and 6,
<https://fig.if.usp.br/~marchett/rg/inequalities-ising-models-field-theories-which-obey-lee-yang-theorem_newman.pdf>,
and Newman--Wu's modern closure/factorization treatment,
<https://arxiv.org/pdf/1708.08820>.

## 2. Certified result

The new driver `src/xi_lee_yang_inverse_cone.py` constructs the Taylor series
of `log M` directly from

`xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2`

using 8000-bit python-flint/Arb complex ball arithmetic.  It certifies

- `a_n>0` for every `1<=n<=40`;
- every leading principal determinant of `H0_d` and `H1_d` is positive for
  `1<=d<=20`; and consequently
- both order-20 localizers are strictly positive definite.

The final determinant enclosures are

`det H0_20 in [9.5255384169509393199e-1326 +/- 3.95e-1347]`,

`det H1_20 in [7.5644546008674159188e-1398 +/- 3.27e-1418]`.

An independent rerun at 6000 bits, 36 moments, and dimension 18 produced the
same signs.  This is a rigorous software-interval result relative to the
python-flint/FLINT-Arb implementation; it is not a Lean kernel certificate.

**Verdict for the general finite cone: survives.**  This does not raise the
probability of RH: low reciprocal power sums are dominated by the first known
critical-line zeros, and finite Taylor data cannot exclude a sufficiently
remote off-line quartet.

## 3. A genuinely stronger product-spin cone fails

There is a nontrivial stricter test.  If xi had an independent weighted
Rademacher-spin representation, including Gaussian limiting slack,

`M(h)=exp(b h^2) product_j cosh(w_j h)`,  `b>=0`,

then

`p_n=[h^(2n)] log M(h) / [h^(2n)] log cosh(h)`

would equal `sum_j w_j^(2n)` for `n>=2`, with the Gaussian term represented
at zero in the first localizer.  Hence the same two Stieltjes Hankel families
built from `p_n` must be positive semidefinite.

They are not.  Both families have positive leading determinants through
dimension 15 and become rigorously negative at dimension 16:

`det P0_16 in [-2.5548964371890279436e-723 +/- 3.71e-743]`,

`det P1_16 in [-1.6370497852121883227e-772 +/- 1.96e-792]`.

Equivalently, their sixteenth LDL pivots are enclosed by

`[-1.0740025096660227718e-94 +/- 1.53e-116]`,

`[-1.1294529798729454386e-96 +/- 1.20e-116]`.

**Verdict for independent weighted spins: pruned.**  This rules out an exact
product of real Rademacher spin factors, and any locally uniform limit whose
log derivatives converge to xi's.  It does not rule out interacting
ferromagnetic models.

## 4. The interacting-ferromagnet scout

For a standard pairwise ferromagnetic total magnetization, GHS requires

`d^3/dh^3 log M(h)<=0` for `h>=0`.

A 100-decimal-digit scan of 902 linear/logarithmic points on
`10^(-6)<=h<=1000` found

`minimum=-0.00180502752878489636971965`,

`maximum=-4.46071191423230467021139e-10`,

and no sampled violation.  This remains a non-interval grid scout and cannot
exclude a between-grid sign change.  GHS is model-specific: its failure would
prune pair-ferromagnetic realizations, not general Lee--Yang measures or RH.

## 5. Corrections to the proposed inverse problem

The earlier roadmap combined constraints that do not belong to one cone.

1. Strongly Rayleigh measures are negatively associated, while
   ferromagnetic GKS/FKG models are positively associated.  Imposing both
   mixed-correlation signs forces the product/degenerate boundary rather than
   testing a general interacting ferromagnet.  See Borcea--Branden--Liggett,
   <https://arxiv.org/pdf/0707.2340>.
2. A generic multiaffine stable lift is not a stronger gate.  Stable
   polarization exists if and only if the univariate polynomial is already
   stable (ibid., Corollary 4.7).  This merely repackages Jensen
   hyperbolicity.
3. One-variable Taylor data do not determine a nonsymmetric multivariate
   lift, its nonnegative pair couplings, or a projective marginalization rule.
   Ruelle's disk-stable Lee--Yang class is the relevant finite object, and his
   all-temperature theorem identifies the pair-interaction subclass, but a
   fixed diagonal specialization cannot recover those interactions:
   <https://arxiv.org/pdf/0811.1327>.
4. Exact projective consistency under eliminating one spin is not necessary
   for an ordinary thermodynamic limit: marginalization can create higher-body
   effective interactions.

Consequently there is no honest, universal finite SDP that can decide
pair-ferromagnetic realizability from xi's univariate cumulants alone.  A
fixed-`N`, fixed-topology nonlinear fit could only prune that selected ansatz.

## 6. Reproduction and research decision

Run

```text
python3 src/xi_lee_yang_inverse_cone.py

python3 src/xi_lee_yang_inverse_cone.py \
  --bits 6000 --moments 36 --hankel-dimension 18 --digits 16

python3 src/xi_lee_yang_ghs_scan.py \
  --h-min 0.000001 --h-max 1000 \
  --linear-samples 301 --log-samples 601 --dps 100
```

The finite test has now done all it can legitimately do:

- it prunes the natural independent/product-spin mechanism;
- it leaves the general Lee--Yang shadow consistent, as expected;
- it neither constructs nor falsifies an interacting arithmetic Hamiltonian;
  and
- stable polarization and a hybrid strongly-Rayleigh/GKS cone are not
  independent routes.

The Lee--Yang branch should therefore be parked until an explicit
prime-and-gamma Hamiltonian is supplied independently of xi's zeros and
Taylor coefficients.  The next fail-fast branch in the orthogonal portfolio
is the Mobius residue-to-density gate.
