# Warped prime lattice: multiscale FFT and Wiener conservation

**Date:** 2026-08-13

**Binary verdict:** **the separated dyadic/FFT/wavelet compilation does not
beat the square-root certificate; no improved nuller or strip is proved.**

On a fixed multiplicative shell, `u_n=log(n/Y)` is indeed a smoothly warped
integer lattice.  Local Taylor linearization makes additive FFT characters
available, and the full aperture `B=Y^(50/33)` contains their central
stationary-frequency band.  This does **not** by itself give an exact finite
Fourier realization: truncating a smooth warped atom leaves small but nonzero
node errors, whose controlled exact correction is a separate interpolation
problem.  The hoped-for gain is lost in the independently charged
phase-space ledger: shortening an integer block narrows its `u`-support by
`H/Y` but widens its Fourier packets by `Y/H`, while an individual edge
character has curvature cost `max(1,H/sqrt(Y))`.  A blockwise
Parseval/Wiener upper certificate charges `sqrt(M_j)` for `M_j` prime-power
nodes, so every separated partition is assigned the cost

```text
sum_j sqrt(M_j) >= sqrt(sum_j M_j)=sqrt(M).                (1.1)
```

The one-block certificate already has this scale.  Beating it requires
coherent cancellation among the lifted characters (within or between cells)
or a large additive-character bias after all sieve characters are charged.
Either is the original global Wiener extremal, not a consequence of local
lattice geometry.

## 1. The exact local warp

Let an integer cell have center `N asymp Y` and length `H<=cY`.  Put

```text
u_0=log(N/Y),       delta=H/N,
```

and fix a nonzero smooth window `chi` supported in a fixed bounded
`v`-interval.  The lift of the additive character `r mod H` is

```text
Psi_(N,H,r)(u)
 =chi((u-u_0)/delta)
  exp(2*pi*i*r*(Y*exp(u)-N)/H).                           (1.2)
```

At every integer node `Y*exp(u)=n`, the **phase factor** in (1.2) is exactly
the ordinary character `exp(2*pi*i*r*(n-N)/H)`; the full value also contains
the window multiplier `chi((u_n-u_0)/delta)`.  Thus there is no Taylor error
in the phase.  Exact mask values still require the window-compatible assembly
spelled out in Section 3.

After `u=u_0+delta*v`, remove the harmless linear modulation
`exp(2*pi*i*r*v)`.  The remaining phase is

```text
Phi(v)=2*pi*r*N/H *[exp(delta*v)-1-delta*v],
Phi''(v)=2*pi*r*H/N *exp(delta*v).                         (1.3)
```

Continuous Fourier Wiener norm is invariant under translation, modulation,
and dilation.  Standard one-dimensional stationary phase, together with
the trivial lower bound `||f_hat||_1>=2*pi*||f||_infinity`, therefore gives
the following exact scale.

### Lemma 1.1 (local curvature cost)

For `1<=|r|<=C_0*H` and the fixed shell/window above (allowing the usual
integer aliases of a residue class),

```text
||Fourier[Psi_(N,H,r)]||_1
 asymp_chi max(1,sqrt(|r|*H/Y)).                            (1.4)
```

The constants are uniform in `N,H,r,Y` for one fixed
`C_c^infinity` window family with bounded seminorms.  For `|r|*H/Y>>1`, the
Fourier transform is concentrated on a spectral interval of length
`O(|r|*H/Y)`.  Cauchy--Schwarz and Plancherel give the
`O(sqrt(|r|*H/Y))` central upper bound, and repeated nonstationary integration
by parts gives the same-scale tail bound.  For the lower bound, van der
Corput gives
`||f_hat||_infinity<=C_chi*(|r|*H/Y)^(-1/2)`; Plancherel and
`||f_hat||_2^2<=||f_hat||_1||f_hat||_infinity` give the reverse square-root
bound.  This avoids the stronger, generally unjustified assertion that the
stationary-phase amplitude is bounded below pointwise across the entire
stationary interval.  When `|r|*H/Y<=1`, smooth compact norm bounds and
`||f_hat||_1>=2*pi||f||_infinity` give the constant scale.  The uniformity
does not cover windows whose transition widths shrink with `H`.

The edge characters and first nontrivial aliases have `|r| asymp H`, hence
cost

```text
max(1,H/sqrt(Y)).                                          (1.5)
```

This is the curvature bill which a linearized FFT suppresses on paper.

## 2. Edge-character Taylor partition versus curvature

If (1.2) is replaced by its linear phase, the discarded phase on one cell
is, for `r asymp H`,

```text
sup |Phi(v)| asymp H^2/Y.                                 (2.1)
```

Thus first-order linearization has uniformly small error only for
`H=o(sqrt(Y))`, which requires `J asymp Y/H >> sqrt(Y)` cells.  If
`H>=sqrt(Y)`, retaining the exact warp costs `H/sqrt(Y)` per edge character
by (1.5), and

```text
(Y/H)*max(1,H/sqrt(Y)) >= sqrt(Y).                         (2.2)
```

Equation (2.2) is the partition--curvature ledger for compilers which insist
on an edge character (or first nontrivial alias) in every cell, as in the
local exact all-integer factor.  It is **not** a lower bound for an arbitrary
FFT mask: a mask with negligible high-residue coefficients need not pay one
edge-character cost per cell.  That possibility is the additive-bias branch
audited in Section 4.  Higher Taylor order changes the discarded remainder
but not the ordinary Fourier Wiener norm of each exact warped atom in (1.4).
Treating polynomial chirps as unit-cost wavelet atoms hides that per-atom
cost; it still does not rule out cancellation after several atoms are
combined.

## 3. Local FFT masks and the blockwise square root

Let `S_j` be the `M_j` active prime powers in an integer block of length
`H_j`.  On `Z/H_j Z`, let `g_j` be their indicator and use normalized DFT

```text
g_hat_j(r)=1/H_j * sum_(x mod H_j)
 g_j(x)exp(-2*pi*i*r*x/H_j).                              (3.1)
```

For a single residue block, Fourier inversion gives exact data and Parseval
gives

```text
sum_r |g_hat_j(r)|^2=M_j/H_j.                             (3.2)
```

Multiplication by the outer window in (1.2), however, gives
`chi(v_n)g_j(n)` at a node, not `g_j(n)`.  Exact global assembly therefore
requires either a plateau window equal to one on every assigned node or a
bounded-overlap partition with bounded local data `d_j(n)` chosen so that
`sum_j chi_j(v_n)d_j(n)=1` on active nodes.  In that rigorous frame
formulation, Parseval gives the upper estimate (summed over bounded overlap)

```text
(H_j/Y)*sum_r |d_hat_j(r)|^2 <= C*M_j/Y.                 (3.3)
```

The local `u`-window has width `H_j/Y`, while its `H_j` FFT modes have
spacing `Y/H_j` and fill a log-frequency band of length `asymp Y`,
independently of `H_j`.  Cauchy--Schwarz on the central band, together with
a Sobolev/nonstationary-phase estimate for its tails, gives the canonical
block upper certificate

```text
||local lifted mask||_A <= C*sqrt(Y)*sqrt(M_j/Y)
                         =C*sqrt(M_j).                    (3.4)
```

The tail step uses the bounded-seminorm window/frame hypothesis from Lemma
1.1.  Discrete Parseval alone does not prove (3.4) for an arbitrary
`H_j`-dependent cutoff, nor does it give a lower bound for the local Wiener
norm.

Now assemble disjoint or bounded-overlap dyadic cells and estimate them by
the FFT/Parseval certificate followed by the triangle inequality.  Its
charged cost is

```text
C_FFT(P)=sum_(j in partition P) sqrt(M_j).                 (3.5)
```

Since all `M_j` are nonnegative, (1.1) proves:

### Theorem 3.1 (blockwise FFT certificate conservation)

Among all separated dyadic partitions, the proof strategy that bounds each
block by (3.4) and then applies the triangle inequality cannot improve the
one-block `sqrt(M)` **charged exponent**.  Refining a block strictly
increases the numerical ledger (3.5) whenever at least two children contain
active nodes.  Bounded-overlap wavelets change only the fixed frame constant.
Charging individual curvature weights from Lemma 1.1 cannot improve this
particular triangle-inequality ledger.

This is only a theorem about the value output by that prescribed upper-bound
bookkeeping.  It is not a lower bound on an individual block norm, on the
combined Wiener norm, or on the true extremal `E_Y`.  Parseval does not
forbid cancellation within a block after warped characters are combined,
and the triangle inequality discards all cross-block cancellation.  Proving
either kind of cancellation is precisely a global all-coefficient theorem
absent from local Taylor geometry.

## 4. Exact additive-bias dichotomy

The same boundary can be stated without a randomness heuristic.  Remove
the DC coefficient from (3.1) and put

```text
E_j=sum_(r!=0)|g_hat_j(r)|^2
   =M_j/H_j-(M_j/H_j)^2,
eta_j=max_(r!=0)|g_hat_j(r)|.                             (4.1)
```

Then the elementary `l2^2/l-infinity` inequality gives exactly

```text
sum_(r!=0)|g_hat_j(r)| >= E_j/eta_j.                       (4.2)
```

In particular, if the centered local prime mask is Fourier-flat in the
quantitative sense

```text
eta_j<=A*sqrt(M_j)/H_j,                                   (4.3)
```

then, for `M_j=o(H_j)`,

```text
sum_(r!=0)|g_hat_j(r)| >= (1-o(1))*sqrt(M_j)/A.            (4.4)
```

Thus a power improvement over the square-root ledger forces one of two
specific phenomena within this compilation:

1. large additive-character biases in a positive share of the cells; or
2. cancellation after the warped characters are combined, either within a
   cell or between different cells.

Notice that (4.4) is a lower bound for the **DFT coefficient** `l1` norm.
It is not a lower bound for the ordinary Fourier Wiener norm of the lifted
sum, because the warped character transforms overlap.  Promoting (4.4) to
such a lower bound would require a reverse frame/unconditionality theorem
which is not proved here.

Actual primes do have elementary large biases, beginning with parity and
small-prime residue classes.  Charging those biases through the literal
exact sieve does not help.  On the primorial group,

```text
||product_(p<=R)(1-1_(p|.))||_A
 =product_(p<=R) 2*(1-1/p),                                (4.5)
```

which is exponential in `pi(R)`.  Formula (4.5) is not a lower bound for a
cleverly recombined log-coordinate filter; it shows only that the natural
Boolean/sieve compilation spends much more than the desired square root.
Any useful bias-based escape must exhibit a new coherent recombination, not
merely invoke the existence of residue structure.

## 5. Aperture and exactness audit

The central frequencies in (1.2) are

```text
2*pi*r*N/H=O(Y),
```

and the curvature spread is `O(r)<=O(H)`.  Hence all substantial mass lies
at frequency `O(Y)`, far inside

```text
B=Y^(50/33).                                               (5.1)
```

For a fixed bounded-seminorm smooth window, Fourier mass outside the central
band has rapidly decaying tails, so the full aperture gives a very accurate
finite-band approximation.  It does **not** automatically give exact node
values.  Correcting the residual errors on a disjoint high-frequency block
requires a right inverse for the actual prime-log evaluation matrix with a
controlled Wiener norm.  The mere ratio `B/Y=Y^(17/33)` does not provide
such a right inverse; that is the original condition-number/extremal gate.
Thus aperture is not the source of the square-root bookkeeping loss, but
exact finite realization remains unproved.

Conversely, if one discards curvature and asks the correction block to repair
the Taylor error, (2.1) shows that first-order cells larger than `sqrt(Y)`
start with order-one errors.  Exact interpolation of those errors is then
the original prime-log condition-number problem, not a perturbative cleanup.

## 6. Decision

```text
warped-integer local phase identity              EXACT;
local curvature Wiener scale                     PROVED for fixed uniform windows;
edge-character partition--curvature ledger       PROVED in its scoped class;
blockwise FFT/wavelet charged upper ledger        >= sqrt(M), no improvement;
exact finite-band correction                     NOT PROVED;
literal sieve/Boolean compilation                exponentially costly;
coherent within/cross-cell Fourier cancellation  OPEN, equals global E_Y gate;
new lower bound for E_Y                           NOT PROVED;
uniform zeta zero-free strip                      NOT PROVED.
```

The practical conclusion is to prune independent dyadic FFT or wavelet
notches.  A viable continuation must directly exploit a coherent global
additive bias of the actual prime set and prove that it survives the
logarithmic Fourier map with small ordinary Wiener norm.  That would be a
new solution of the adversarial-design extremal, not a gain supplied by
local Taylor linearization itself.
