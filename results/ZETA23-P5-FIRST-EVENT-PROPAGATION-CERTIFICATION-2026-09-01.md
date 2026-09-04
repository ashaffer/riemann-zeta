# First $p=5$ event propagation certificate

**Date:** 2026-09-01  
**Verdict:** **PASS for one explicit microscopic event crossing; uniform/cofinal propagation remains open.**

## Statement

Use project support $L=4a$, and let

\[
\lambda(L)=\inf_{\lVert f\rVert_2=1}Q_L(f)
\]

on the logarithmic Weil-form domain. Put

\[
L_5=2\log5,\qquad a_5=\frac{\log5}{2}
 =0.8047189562170501873\ldots .
\]

The new interval certificate proves

\[
\boxed{\lambda(L_5)\ge 5\times10^{-18}}.                 \tag{1}
\]

Moreover, the explicit support-continuity estimate in `THEOREMS.md`, instantiated with $\ell_0=L_5$ and $\ell_1=4$, gives

\[
C_{\rm glide}=12661.069087634894\ldots<12662.
\]

Consequently, for every

\[
0<h\le e^{-10^{22}},
\]

\[
\boxed{\lambda(L_5+h)>3.733\times10^{-18}>0}.            \tag{2}
\]

The physical half-window in (2) is $a_5+h/4$, and

\[
\log5<\frac{L_5+h}{2},
\]

so $p=5$ is genuinely active. This is therefore an actual crossing of the first prime event, not merely positivity up to its boundary.

Independently of the project's effective modulus, [Suzuki's Theorem 1.3](https://arxiv.org/abs/2606.09096v2) proves unconditional continuity of the actual localized ground value. Thus (1) alone already implies positivity on some unspecified nonempty interval past $L_5$. Support monotonicity, also recorded in [Connes–Consani–Moscovici, Corollary 3.7](https://arxiv.org/abs/2511.22755), covers the whole interval from Chuk's $L=3.2$ window through $L_5$.

## Endpoint certificate

At $L_5$, the $p=5$ shift equals the autocorrelation support diameter. Its endpoint autocorrelation is zero, and the strict $\log n<L/2$ convention retains exactly the source terms $2,3,4$. The successful bounded minorant uses

```text
T = 250
alpha = 73/100
Legendre degrees = 0,...,299 (150 per parity)
Gauss--Legendre order = 80 on each of 250 unit panels
working precision = 640 bits
```

The exterior and analytic-quadrature checks give

```text
beta_*(250)                         = 0.73761032622928049... > 0.73
|Omega-alpha| on [0,250]            < 15.6692 < 16
|Omega-alpha| on Bernstein ellipses < 19.9049 < 21
entry error                         < 1.537e-29
parity-block operator error         < 2.305e-27
```

An approximate eigensolver supplies only an untrusted change-of-basis proposal. Arb recomputes the interval congruence and Cholesky. After subtracting the exact $6\times10^{-18}$ head shift:

```text
even smallest shifted pivot > 9.8374879910e-19
odd  smallest shifted pivot > 5.2722765766e-15
```

The infinite Legendre complement is retained. The final head/tail ledger is

```text
rho_tail                   < 8.234e-26
head/tail coupling         < 4.592e-12
complement diagonal        = 0.73 - O(1e-24)
shifted Schur determinant  > 7.2997892175e-19
```

This proves (1) on the full real form domain; parity and real/imaginary splitting give the complex statement. Nine independent `acb.integral` entries, sharing neither the common Gauss nodes nor its Bernstein remainder, all overlap the certified matrix. Seven regression tests pass.

An independent higher-order replay with 310 degrees, Gauss order 88, and 704-bit arithmetic also passes. It reproduces the same head pivots while reducing the quadrature operator error to $1.079\times10^{-30}$ and the tail leakage to $1.835\times10^{-35}$.

## Effective propagation calculation

The Glide theorem states, for $h=L'-L$,

\[
0\le\lambda(L)-\lambda(L')
 \le \frac{C_{\rm glide}}{\log(1/h)}.
\]

For $h\le e^{-10^{22}}$, (1) therefore gives

\[
\lambda(L_5+h)
 \ge 5\times10^{-18}-\frac{12662}{10^{22}}
 =3.7338\times10^{-18}>0.
\]

All side conditions $h\le\min(1/2,L_5/2,1/e)$ and $L_5+h\le4$ are immediate.

## What failed and what this teaches

The original $T=200,\alpha=1/2$ Chuk minorant does not reach the event. At $a=0.8047$, an explicit odd Legendre polynomial has the rigorous Rayleigh enclosure

\[
[-2.9360061942792\times10^{-15}\ \pm\ 8.92\times10^{-29}].
\]

Increasing to $T=250,\alpha=0.73$ repairs that certificate loss.

A coarse Schur perturbation is hopeless. The entering reflection has norm

\[
\kappa_5=\frac{\log5}{\sqrt5}=0.7197625155\ldots,
\]

about $8\times10^{16}$ times the old $8.9\times10^{-18}$ floor. The useful quantity is instead the boundary-compressed resolvent

\[
P_{\partial,\varepsilon}A^{-1}P_{\partial,\varepsilon},
\]

which vanishes as the boundary slivers shrink because $A^{-1}$ is compact. The logarithmic Glide bound is a very crude effective realization of this localization.

## Scope and trust boundary

This establishes one explicit $p=5$ crossing. It does **not** establish a reusable event theorem, a uniform step size, a non-Zeno/cofinal iteration, global Weil positivity, a uniform zero-free strip, or RH. Repeating microscopic steps without a lower bound on their accumulated support can converge at a finite scale.

The endpoint is certified at the analytic-plus-Arb level. The named analytic inputs are the exterior digamma envelope, endpoint autocorrelation identity, Parseval/parity reduction, Legendre/Bessel and pole tails, Bernstein quadrature bound, and logarithmic form-domain closure. The explicit interval (2) additionally relies on the hand-proved effective Glide theorem in `THEOREMS.md`; only parts of that analytic chain have Lean counterparts. This is not yet an end-to-end kernel proof.

## Replay

```bash
PYTHONPATH=src python3 src/chuk_p5_threshold_arb_certificate.py --quiet --cross-check
PYTHONPATH=src python3 -m pytest -q \
  src/test_chuk_l08_arb_certificate.py \
  src/test_chuk_p5_threshold_arb_certificate.py
```

Machine-readable ledger: `results/chuk_p5_threshold_T250_M300_arb_certificate_2026_09_01.json`.
