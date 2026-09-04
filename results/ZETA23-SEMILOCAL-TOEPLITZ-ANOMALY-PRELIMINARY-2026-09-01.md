# Preliminary semilocal Toeplitz-anomaly reconstruction

Date: 2026-09-01

## Verdict

The anomaly-preserving Cayley normalization is now explicit and passes a
smooth-symbol control, but the actual semilocal Hardy-block sums do **not**
converge under the tested hard Laurent cutoffs.  This is an indeterminate
finite reconstruction, not a counterexample to the continuum trace formula.

It does rule out claiming suppression from the present finite data.  On the
`M=40,q=1,delta=.32` moment-null Ward extremizer, every fixed,
sampling-stable truncation tested has an order-one `-b^*b` trace comparable
with the `c^*c` and cross terms.  The desired value can only arise after
large signed cancellations.  Because the block sums have not converged, this
is evidence against a `c`-only estimate rather than a continuum block
attribution.

## Conventions and exact checks

Use

\[
 z=\frac{t-i}{t+i}=e^{i\theta},\qquad
 t=-\cot(\theta/2),\qquad
 \frac{dt}{d\theta}=\frac{1+t^2}{2}.
\]

The line kernel `-i/(2 pi(s-t))` transfers to the lower Hardy projection

\[
 P e_n=e_n\quad(n\leq0).
\]

For `U=e^{i Theta}` this convention gives the analytic diagonal
`diag(P-U^*PU)=Theta'`, not its negative.  Thus

\[
 \tau_g(D_U)=\frac1{2\pi}\int_0^{2\pi}g(\theta)\Theta'(\theta)d\theta
 =\frac1{2\pi}\int_{\mathbb R}g(t)m_F(t)dt.
\]

Laurent matrices use `(M_f)_(ij)=f_hat_(i-j)`.  A smooth control with
`U=exp(.7 i sin(theta))` and `g=cos(theta)` reconstructs the exact value
`.7/2=.35` to floating error using 16 central modes and 128 padding modes.
The unit shift `U=z` reconstructs its rank-one anomaly exactly.

## Actual relative Ward vector

The code independently rebuilds the top two-moment relative Ward extremizer:

- Ward ratio and direct pole-free pairing: `1.0960282678752`;
- old relative Ritz floor: `2.6352182043e-5`;
- moment residual: `3.47e-15`;
- algebraic pairing identity error: `2.64e-13`;
- parity: even.

The Cayley/Jacobian quadrature converges independently to the x-space value.
At `2^18` midpoint samples it gives `1.09600741244` (absolute error
`2.09e-5`); at `2^20` it gives `1.09602987454` (error `1.61e-6`).

## Hardy decomposition and failure of hard-cutoff convergence

With `H_+=ran(P)` and `H_-=ran(1-P)`, the infinite algebraic blocks are

\[
 D_U=\begin{pmatrix}c^*c&-a^*b\\-b^*a&-b^*b\end{pmatrix}.
\]

The padded diagnostic restricts only the final trace diagonal to `N` modes
per side.  The intermediate index in `M_gD` and the half-line leakage sum are
both extended to `L` modes.  Inserting the central projection between `M_g`
and `D` was separately tested and rejected.

Two sampling-stable examples (`2^16` versus `2^18` changes the total by about
`5--6e-4`) are:

| `N` | `L` | `++` | `+-` | `-+` | `--=-b^*b` | total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 32 | 1.1933 | .4971 | .4201 | -1.0585 | 1.0520 |
| 8 | 64 | 1.6789 | .1432 | .0835 | -1.4297 | .4759 |

The corresponding squared Frobenius masses `(c,b)` are approximately
`(.341,1.815)` and `(.430,2.435)`.  These are truncation diagnostics, not
operator norms, but they decisively do not show reverse-channel suppression.

Padding does not stabilize the actual trace.  For `N=4`, increasing `L` over
`32,64,128,256,512` gives totals

```text
1.0520, 1.0049, 1.0832, 1.1911, 1.2575.
```

For `N=8`, `L=64,128,256,512,1024` gives

```text
.4759, .5974, .7146, .7632, .7775.
```

Neither sequence licenses a limit or a comparison with `1.096028...`.
A square Toeplitz section retaining `I-a_L^*a_L` was also tested.  It has an
outer-boundary bias even for a smooth zero-winding phase, so it is a control,
not the continuum regularization.

## Interpretation

The Cayley endpoint `z=1` is an infinitely oscillatory singularity of the
semilocal phase.  Ordinary midpoint FFT coefficients converge nonmonotonically,
and the noncompact `b` channel makes the separate Hardy traces conditional.
Hard rectangular cutoffs therefore do not yet implement the regularized
trace, even though the direct analytic diagonal is stable.

The next mathematically licensed reconstruction would use either the
point-split kernel with its analytic diagonal, or a proved Abel/heat
regularization of all four Hardy blocks with a common removal order.  Any such
regularization must retain `-b^*b`; the present computation gives no evidence
that the relative harmonic lift annihilates it.

The relative signed-cancellation theorem, `HRW`, propagation, a uniform strip,
and RH remain open.

## Artifact and replay

- implementation: `src/semilocal_toeplitz_anomaly_probe.py`
- fast controls: `src/test_semilocal_toeplitz_anomaly_probe.py`

```bash
PYTHONPATH=src python3 -m pytest -q src/test_semilocal_toeplitz_anomaly_probe.py
PYTHONPATH=src python3 src/semilocal_toeplitz_anomaly_probe.py \
  --sample-power 18 --central-modes 4,8,16 --padding-factors 2,4,8
```
