# Hostile falsification of the center-density route

Date: 2026-08-31

Preflight:
[zeta23_center_density_falsification_preflight_v1.json](context/zeta23_center_density_falsification_preflight_v1.json)

Finite pseudo-node replay:
[center_density_falsifier.py](../src/center_density_falsifier.py)

Actual-prime scout:
[ZETA23-CENTER-DENSITY-ACTUAL-PRIME-PROBE-2026-08-31.json](ZETA23-CENTER-DENSITY-ACTUAL-PRIME-PROBE-2026-08-31.json)

## Verdict

The deterministic center-set intersection adapter survives, after two
precision repairs. The broader hoped-for mechanism does not.

A single global prime-density real-node model can have all of the following
simultaneously:

1. one fixed contiguous source interval and one common ordinate;
2. legal negative source events on a positive density of half-integer
   centers;
3. prime-scale density and gaps, positivity, exact barycentric edge moments,
   and distinct nontrivial pair sums;
4. an averaged retained-hat fourth moment much smaller than the proposed
   target;
5. failure of density radialization on a linear-density subset of those same
   source-aligned centers.

The mechanism is inverse-density compensation. The unweighted counting
measure detects an oscillatory density wave, while the adjacent-gap
hat/Voronoi weights multiply each point by approximately the reciprocal local
density and erase that wave.

A complementary same-passport Bragg model makes the averaged fourth moment
fail catastrophically. Therefore common source coherence and center density
do not couple the upper and lower gates. The retained soft passport permits
either gate to fail.

These are real-node countermodels, not actual-prime counterexamples. The
actual-prime averaged moment and density-radialization statements remain
open. But the falsifier removes the main reason for expecting the
center-density reformulation itself to bridge the arithmetic gap. Any
surviving proof must use a quantitative multiplicative property of the
actual prime logarithms that fails in both models.

The bounded actual-prime probe found no adverse center/source co-resonance,
but its source event is far from asymptotically legal and hence changes no
theorem status.

---

## 1. What survived the logical audit

For a fixed Turan interval sum \(S_I\) and common ordinate \(\tau\), the
eligible half-integer centers obey

\[
 \#\mathcal W_N
 =
 \left(\frac{\arccos\kappa}{\pi}
 +O(N^{-\delta(A')})\right)\#\mathcal J_N,
 \qquad
 \delta(A')=\min\left(\frac{2-A'}3,\frac14\right).   \tag{1.1}
\]

The Erdos--Turan and van der Corput derivation, the \(N\)-versus-\(Y\)
conversion, and the height-band inclusion all survive re-derivation.

Two details required correction.

First, \(\arccos(3/4)/\pi=0.230053\ldots\) is the fraction of the eligible
center interval, not a coefficient multiplying \(N\) without qualification.
If \([a,b]\subset[N,2N]\), \(b/a\le e^{w/2}\), and

\[
 \mathcal J_N=[be^{-w},ae^w]\cap[N,2e^wN],
\]

then

\[
 \#\mathcal J_N\ge(e^w-1)N-O(1).                    \tag{1.2}
\]

At \(w=1/5\), \(\kappa=3/4\), this gives the uniform absolute lower bound

\[
 \#\mathcal W_N\ge(0.0509344697\ldots+o(1))N.       \tag{1.3}
\]

Second, the fixed-hat adapter licenses every exponent \(c_0<.019\), not the
endpoint itself. Freeze

\[
 c_0=.01895=\frac{379}{20000}.
\]

Then the averaged-moment exceptional-set saving is

\[
 \begin{aligned}
 m
 &=\frac{1187}{13000}-\frac92c_0\\
 &=\frac{3137}{520000}
 =.0060326923\ldots.                                 \tag{1.4}
 \end{aligned}
\]

Thus an averaged GCG4 estimate would leave at most

\[
 N^{1-m+o(1)}=N^{.9939673\ldots+o(1)}               \tag{1.5}
\]

bad upper centers. A lower-return success set of size \(N^{.995}\) still
forces an intersection, because \(c_0=.01895>.0189\). All exponent
orientations and uniformity requirements then type-check.

Accordingly:

\[
 \text{phase count + set intersection}
 \quad\text{is a valid conditional adapter}.         \tag{1.6}
\]

It supplies no reason that the lower success set must exist.

---

## 2. Compensated random-mesh world

This countermodel targets the proposed density-radialization premise while
allowing the averaged upper theorem to hold.

### 2.1 One global node set and one common source

Let

\[
 \tau=N^{1/2},\qquad
 h=\frac{\log N}{N},\qquad
 \kappa_N=C(\log N)N^{-.001}.                        \tag{2.1}
\]

Choose a fixed log interval \(I\) contained in every shell of a
fixed-factor eligible center block. Partition the surrounding global log
block into equal-mass cells for the density

\[
 \rho_N(x)=\frac{e^x}{\log N}
 \left(1-\kappa_N1_I(x)\cos(\tau x)\right),          \tag{2.2}
\]

and select one independent uniform point \(X_j\) from each cell. The
pseudo-primes are \(e^{X_j}\). This is one global set used for every center,
not a new set chosen after \(Y\).

The cell widths are \(O(h)\), so the physical gaps are \(O(\log N)\). Hence
all edges pass the cutoff \(Y^{161/1000}\). The modulation tends to zero,
and the system retains prime-scale density. Continuous jitter makes every
nontrivial equality

\[
 X_i+X_j=X_k+X_l
\]

absent almost surely. The literal barycentric tilted-tent weights are
positive, have total mass one, and reproduce mass and first moment exactly
on each edge.

For the one fixed source interval,

\[
 M\asymp\frac{N}{\log N},\qquad
 S_I:=\sum_{X_j\in I}e^{i\tau X_j}
 =-\left(\frac{\kappa_N}{2}+o(\kappa_N)\right)M      \tag{2.3}
\]

with overwhelming probability. On the phase-aligned centers,

\[
 \Re(e^{-i\tau\log Y}S_I)\le-\frac34|S_I|,
\]

one has

\[
 D_Y\ge\frac38\kappa_N,\qquad
 \frac{M}{N}D_Y\ge N^{-.001}                        \tag{2.4}
\]

after choosing the fixed constant \(C\). Thus the common source is legal at
the required exponent on a linear-density center set.

### 2.2 The exact hats compensate the source wave

Let \(F_Y\) be the exact barycentric retained-hat polynomial. Its nodal
weights have size \(O(h)\). Each centered summand depends on only three
neighboring random cell points, so splitting the indices modulo three and
using the fourth-moment inequality gives

\[
 \mathbb E|F_Y(t)-\mathbb EF_Y(t)|^4\ll h^2.         \tag{2.5}
\]

If \(\ell_j\) are the deterministic quantile-cell lengths, then

\[
 \sum_j|\ell_{j+1}-\ell_j|
 \ll h(1+\kappa_N\tau).                              \tag{2.6}
\]

For a constant profile on equal cells, the local cell weight is

\[
 \lambda_j=\frac{X_{j+1}-X_{j-1}}2.
\]

Conditional expectation turns this exactly into cellwise Lebesgue
integration. The fixed smooth tilted tent and the varying cells add the
total-variation error in (2.6), uniformly in \(t\):

\[
 |\mathbb EF_Y(t)-\widehat\phi(t)|
 \ll h(1+\kappa_N\tau)
 =N^{-.501+o(1)}.                                    \tag{2.7}
\]

Equation (2.7) is an expectation-level stratified-sampling identity, not a
pathwise high-frequency quadrature estimate. Pathwise interpolation costs
\(O(t^2h^2)\), which is used only below \(L\). In (2.9), the uniform
pointwise expectation bounds are integrated by Fubini; no supremum over the
high band is taken.

This identity exhibits the mechanism:

\[
 \text{counting density }\rho_N(X_j),
 \qquad
 \lambda_{j,Y}\approx
 \frac{\phi(X_j-\log Y)}{\rho_N(X_j)}.               \tag{2.8}
\]

The reciprocal local-density factor cancels the modulation that generated
the unweighted source sum.

### 2.3 Averaged GCG4 holds, radialization fails

Put

\[
 L=N^{839/1000},\qquad B=N^{50/33}.
\]

Since \(|\widehat\phi(t)|\ll t^{-2}\), equations
(2.5)--(2.7) give

\[
 \begin{aligned}
 \mathbb E I_Y
 &\ll Bh^2+L^{-7}
   +B\{h(1+\kappa_N\tau)\}^4\\
 &\ll N^{-16/33+o(1)}.                              \tag{2.9}
 \end{aligned}
\]

This is far stronger than the proposed
\(N^{-1187/13000+o(1)}\) averaged bound. Fubini, Markov, and the source
concentration give a single global realization satisfying both (2.3) and
the center-averaged form of (2.9).

Take

\[
 c_*=\frac{39}{2000}=.0195.
\]

Below \(L\), the continuum negative part is \(O(t^{-2})\), while the
finite-element interpolation error is \(O(t^2h^2)\). Above \(L\), moment
persistence and (2.9) leave at most

\[
 N^{1-d+o(1)},\qquad
 d=\frac{16}{33}-\frac92c_*
 =\frac{52417}{132000}=.397098\ldots                \tag{2.10}
\]

centers at which this positive antenna can have a deeper negative value.
Consequently a linear-density subset of the common phase-aligned source
centers satisfies

\[
 r_P(H_Y)\le N^{-.0195+o(1)}.                       \tag{2.11}
\]

This contradicts the proposed synthetic lower conclusion
\(r_P(H_Y)\ge N^{-.0189+o(1)}\). Therefore the synthetic
density-radialization analogue is false on a single global prime-density
real-node system even when the averaged fourth moment is true with a large
reserve. This does not refute the literal actual-prime statement.

At the source ordinate, the same compensation gives the additional
diagnostic

\[
 |F_Y(\tau)|
 \ll\tau^{-2}+\tau^2h^2=N^{-1+o(1)}=o(D_Y),         \tag{2.12}
\]

This says that the canonical retained-hat antenna screens the source wave.
It is not, by itself, a PWCT counterexample: that statement has an additional
reflected-pair carrier constraint and a source-leverage normalization.  No
PWCT status is changed here.

A \(4000\)-node deterministic smoke test illustrates the cancellation:
the normalized counting coefficient is \(-0.09999991\), the Voronoi-weighted
coefficient is \(-1.75\cdot10^{-5}\), and an imposed fine-grid Bragg
coefficient has modulus \(1\). These floating values illustrate the two
mechanisms; the asymptotic claims above rest on the analytic estimates, not
on this fixture.

---

## 3. Complementary Bragg world

The upper averaged theorem is independently false under the same soft
geometric data.

Take a global log lattice of spacing \(h=\log N/N\) on the union of all
eligible shells. Reserve a contiguous source block of log length

\[
 \ell=C N^{-.001}\log N,                             \tag{3.1}
\]

where \(C\) is a sufficiently large fixed constant. In that block replace
the lattice points by quantiles of a density comparable to
\(h^{-1}(1-\beta\cos(\tau x))\), with \(\tau=N^{1/2}\) and \(0<\beta<1\).
Then

\[
 M=(C+o(1))N^{.999},\qquad
 M^{-1}\sum_{p\in I}\cos(\tau\log p)
 =-\frac\beta2+o(1).                                 \tag{3.2}
\]

Choosing \(C>2/(\kappa\beta)\) makes the aligned source event legal even
with coefficient-one normalization. The block has only
\(O(\ell+h)=o(1)\) of every fixed-width hat's total mass.

Outside it, at the resonances

\[
 t_k=\frac{2\pi k}{h},
\]

all endpoint phases coincide. Now perturb every node generically by at most
\(\varepsilon_N/B_{\max}\), where \(\varepsilon_N\to0\) and \(B_{\max}\) is
the largest conductor in the center block. The perturbation is \(o(h)\), so
it preserves order, prime-scale gaps, the source event, and every resonant
peak, while avoiding the finite union of all nontrivial pair-sum
hyperplanes. All physical gaps remain \(O(\log N)\), hence all edges are
retained and the exact barycentric shares still partition the profile
integral.

For every moving center, use resonances in the common interval below the
smallest conductor \(B_{\min}\). Positivity of the weights and the \(o(1)\)
source mass give

\[
 |F_Y(t_k)|=1-o(1).
\]

Since \(|F_Y'|\le w\), these yield disjoint peaks of fixed width. Their number
is

\[
 B_{\min}h=N^{17/33+o(1)}.
\]

Consequently, uniformly in the center,

\[
 I_Y\gg N^{17/33-o(1)}.                              \tag{3.3}
\]

This catastrophically violates averaged GCG4 while retaining comparable
prime density, small gaps, positivity, exact edge moments, one common legal
source, and pair-sum uniqueness. It is a soft real-node countermodel, not a
counterexample to the literal actual-prime mask.

The two pseudo worlds prove that no theorem based only on those fields can
force either open gate.

---

## 4. Bounded actual-prime falsifier

The finite scout used:

- all \(1001\) half-integer centers \(Y=8000.5,\ldots,9000.5\);
- the fixed actual-prime interval \([8200,9060]\), containing \(98\) primes;
- the exact adjacent-gap cutoff with \(\theta=.161\);
- two independent \(4096\)-point top-band samples;
- \(2048\) common ordinates in \([\sqrt{8000},8000]\);
- circular-shift controls that repeat the hostile ordinate scan.

The retained floating hat weights agreed with the independent Arb
construction to less than \(1.8\cdot10^{-13}\) in \(\ell^1\).

The median phase-aligned fraction was \(0.230769\), close to the predicted
\(0.230053\) fraction of the sampled eligible block. For the
source-coherence ordinate, the aligned-to-unaligned diagonal-normalized
fourth-moment ratio was \(0.99924\), with circular-shift
\(p=0.615\). The hostile scan found a maximum ratio \(1.00489\), but its
scan-adjusted circular-shift value was \(p=0.568\). Thus the simplest finite
actual-prime co-resonance falsifier failed.

This is weak evidence. The source interval has

\[
 \frac{M}{N}=.01225,
\]

while the asymptotic premise at this scale demands
\(N^{-.001}=.99105\). No legal event can occur in the fixture. The probe
does not approximate the radial radius and cannot prove or refute either
asymptotic theorem.

---

## 5. Decision-tree consequence

The hostile result is sharper than “actual primes are still special.”

The compensated pseudo world models the precise first-order phenomenon one
expects from an oscillatory prime-density wave: unweighted counts detect the
wave, while cell-length weights flatten it. Thus the common-zero coherence
is not naturally allied with the canonical upper antenna; it is naturally
screened by it.

The center-density adapter remains available if an independently motivated
actual-prime theorem supplies one of the missing gates. It should not,
however, be treated as evidence that such a theorem exists or as a
standalone high-priority route. The phrase “prove a multiplicative feature
that defeats compensation” is not a new intermediate lemma: without a
concrete property and a complete adapter, it is density radialization
renamed.

The rational disposition is:

| Claim | Hostile-audit status |
|---|---|
| Quantitative phase replication | **SURVIVES, with corrected absolute count** |
| Center-set intersection implication | **SURVIVES at licensed \(c_0=.01895\)** |
| Soft-data implication to averaged GCG4 | **REFUTED** |
| Soft-data implication to density radialization | **REFUTED** |
| Abstract coupling of the two gates by common source coherence | **REFUTED** |
| Actual-prime averaged GCG4 | **OPEN** |
| Actual-prime density radialization | **OPEN, prior reduced** |
| Uniform zero-free strip | **OPEN** |
| RH | **OPEN** |
