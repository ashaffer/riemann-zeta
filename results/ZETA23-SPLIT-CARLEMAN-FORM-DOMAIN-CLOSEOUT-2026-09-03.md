# ZETA23 split-Carleman and form-domain closeout

Date: 2026-09-03  
Registry: R186  
Status: the two technical debts are closed in the correct weak/L2 topology;
the proposed pointwise-jet topology is unavailable; KNC, a uniform strip, and
RH remain open

Preflight:
[`zeta23_split_carleman_form_domain_closeout_preflight_v1.json`](context/zeta23_split_carleman_form_domain_closeout_preflight_v1.json)

## 0. Verdict

The split finite-part old operator can be serialized exactly.  Genuine
Friedrichs-domain contacts can also be carried into a canonical weak old
equation, an `L2` exterior readout on every finite collar, and a continuous
integrated potential.  Thus neither item is a remaining technical gap.

The closeout does **not** prove old-to-collar propagation.  Once the two
adapters are installed, the desired statement is still exactly

\[
 n\in\ker A_a\quad\Longrightarrow\quad
 (W*\widetilde n)|_{I_b\setminus I_a}=0.                 \tag{0.1}
\]

This is KNC.  Serialization only writes the premise and conclusion in one
state space; it supplies no implication between them.

There is also a genuine negative conclusion.  Point values, endpoint traces,
and all boundary jets of the split source are not continuous on the generic
form domain.  They cannot be recovered by density.  Any future use of the
R185 jet tower must first prove zeta-specific regularity of homogeneous
solutions.  The domain-safe state is instead

```text
(density n, analytic Cauchy transform off J,
 weak old equation, L2 finite-collar source, continuous integrated potential).
```

Both preregistered fast falsifiers were executed.  They rule out propagation
from local Plemelj data or from the coefficient-free combination of split
orientation, reflection, positivity, and bilateral dilation.  They do not
refute the completed-zeta identity because the second model is synthetic and
the first density is not in `L2`.

## 1. Exact finite-part serialization

Put

\[
 \ell(t)=e^{-t/2}\Phi(e^{-2t},1,1/4),\qquad
 K(t)=\frac{e^{3t/2}}{e^{2t}-1}.
\]

Termwise differentiation of the convergent Lerch series gives

\[
 \ell'(t)=-2K(t).                                      \tag{1.1}
\]

For smooth `n` on `I_a=(-a,a)`, the archimedean old channel is

\[
 (L_an)(x)=\lim_{\epsilon\downarrow0}\left\{
 \int_{\substack{-a<y<a\\|x-y|>\epsilon}}
 K(|x-y|)n(y)\,dy-\ell(\epsilon)n(x)\right\}.          \tag{1.2}
\]

Subtracting `n(x)` inside the integral and using (1.1) removes the finite
part completely:

\[
\boxed{
 (L_an)(x)=\int_{-a}^{a}K(|x-y|)[n(y)-n(x)]\,dy
 -\frac{\ell(a+x)+\ell(a-x)}2n(x).}                   \tag{1.3}
\]

The integral in (1.3) is ordinary for smooth `n`.  In the form-domain
closure, (1.2)--(1.3) are interpreted through the closed form/distributional
pairing, not as pointwise formulas.

Now set

\[
 X=e^{x/2},\quad Y=e^{y/2},\quad
 J=(\alpha,\beta)=(e^{-a/2},e^{a/2}),\quad
 f(Y)=n(2\log Y).
\]

The two rational identities

\[
 \frac12\sum_{\zeta^4=1}\frac1{X-\zeta Y}
 =\frac{2X^3}{X^4-Y^4},\qquad
 \frac12\sum_{\zeta^4=1}\frac{\zeta^{-1}}{Y-\zeta X}
 =\frac{2XY^2}{Y^4-X^4}                               \tag{1.4}
\]

and `dy=2 dY/Y` give the exact cutoff serialization

\[
\begin{aligned}
 (L_af)(X)=\lim_{\epsilon\downarrow0}\bigg[&
 \frac12\sum_{\zeta^4=1}
 \int_\alpha^{Xe^{-\epsilon/2}}\frac{f(Y)}{X-\zeta Y}\,dY\\
 &+\frac12\sum_{\zeta^4=1}\zeta^{-1}
 \int_{Xe^{\epsilon/2}}^\beta\frac{f(Y)}{Y-\zeta X}\,dY
 -\ell(\epsilon)f(X)\bigg].                           \tag{1.5}
\end{aligned}
\]

There is an even smaller convergent four-Cauchy state.  Define

\[
\begin{aligned}
 H_+f(X)&=\frac12\int_\alpha^X\frac{f(Y)-f(X)}{X-Y}\,dY
       +\frac12\int_X^\beta\frac{f(Y)-f(X)}{Y-X}\,dY
       +h_a(X)f(X),\\
 H_-f(X)&=\frac12\int_\alpha^X\frac{f(Y)}{Y+X}\,dY
       -\frac12\int_X^\beta\frac{f(Y)}{Y+X}\,dY,       \tag{1.6}\\
 h_a(X)&=\frac12\log\frac{(X-\alpha)(\beta-X)}{X^2}
          -\log2-\frac\pi2.
\end{aligned}
\]

For

\[
 C_f(z)=\frac1{2\pi i}\int_\alpha^\beta
             \frac{f(Y)}{Y-z}\,dY,
\]

the exact identity is

\[
\boxed{L_af=H_+f+H_-f+\pi\{C_f(iX)-C_f(-iX)\}.}        \tag{1.7}
\]

The constant in `h_a` follows from

\[
 \ell(\epsilon)=-\log\epsilon+2\log2+\pi/2+o(1),       \tag{1.8}
\]

itself equivalent to `psi(1/4)=-gamma-pi/2-3 log 2`.
Consequently the combined local coefficient in
`B_a=R_a+c_Gamma-P_a-L_a` is

\[
 c_\Gamma-h_a(X)=-\gamma-\log(4\pi)
 -\frac12\log\frac{(X-\alpha)(\beta-X)}{X^2}.          \tag{1.9}
\]

Equations (1.5) and (1.7) close the R185 serialization debt.  Stacking this
old row with the exterior rows is bookkeeping; its compatibility condition
remains `E|ker(B_a)=0`.

## 2. The correct form-domain adapter

Let `q_a` be Suzuki's closed localized Weil form, and let `A_a` be its
Friedrichs operator at a nonnegative contact.  Extend `n` by zero to
`\widetilde n` on the line.  Suzuki's smooth distribution identity and the
form-core closure give the domain-safe equivalence

\[
\boxed{
 n\in\ker A_a
 \quad\Longleftrightarrow\quad
 (W*\widetilde n)|_{I_a}=0
 \text{ in }\mathcal D'(I_a).}                         \tag{2.1}
\]

Here is the proof with the topology exposed.

1. For every core test `z`, the smooth identity represents the polarized
   form by the convolution distribution.
2. `C_c^infinity(I_a)` is a form core.  Form convergence implies `L2`
   convergence, while pairing the convolution with a fixed test is an `L2`-
   continuous functional.  The identity therefore passes to `D(q_a)`.
3. By the first representation theorem, `A_an=0` is equivalent to
   `q_a(n,z)=0` for every `z in D(q_a)`, hence for every core test.  The
   converse follows by core density.

The equivalent integrated-potential version, already established in the
project's `ZETA23-SCREW-COLLAR-POTENTIAL-AND-CONTACT-AUDIT-2026-09-01.md`, is

\[
 H_n(x)=i\int_{-a}^a g'(x-y)n(y)\,dy.                  \tag{2.2}
\]

Because `g' in L2_loc`, translations are continuous in `L2` and hence `H_n`
is continuous.  With `W=-g''`, (2.1) is equivalent to `H_n` being constant
on `I_a`.  For `a<b`, KNC is precisely extension of that plateau to `I_b`.

### 2.1 Finite-collar exterior state

For every fixed `a<b`, the smooth exterior formula extends uniquely to a
bounded map

\[
 E_{a,b}:L^2(I_a)\longrightarrow L^2(I_b\setminus I_a). \tag{2.3}
\]

Indeed, at an adjacent edge the singular Lerch channel has kernel comparable
to `1/(r+s)` for inward/outward distances `r,s>0`; the classical Carleman
inequality gives `L2` boundedness.  The other three root channels have
bounded kernels, the pole terms are finite rank, and only finitely many
prime-power translations can meet a fixed collar.  Each such restricted
translation is an `L2` contraction.  Density identifies (2.3) with
`(W*\widetilde n)|_{I_b\setminus I_a}` distributionally.

Thus a genuine contact has all of the weak/L2/Cauchy state required to state
R185 compatibility.  No trace theorem is needed.

## 3. Why endpoint jets must be retired

Suzuki explicitly warns that generic vectors in `D(A_a)` need not have
point values.  This is also visible directly from his Fourier form formula.
For a fixed smooth compactly supported bump
`u_epsilon(x)=phi(x/epsilon)` with `phi(0)=1`, scaling that formula gives

\[
 \|u_\epsilon\|_{q_a,\mathrm{shifted}}^2
 =O(\epsilon\log(1/\epsilon))\longrightarrow0,          \tag{3.1}
\]

while `u_epsilon(0)=1`.  Point evaluation is therefore unbounded; derivative
traces are no better.  Form-core density cannot pass the boundary derivatives
written in R185.

This does not invalidate the smooth-core jet identities.  It changes their
status to a conditional diagnostic: they apply to a contact only after an
independent homogeneous-equation regularity theorem places that contact in a
trace class.  They are not part of the canonical adapter.

## 4. Executed fast falsifiers

### 4.1 Arcsine finite-Hilbert falsifier

For `rho(t)=(1-t^2)^(-1/2)` on `(-1,1)`, take the branch
`sqrt(z^2-1)~z` at infinity.  Then

\[
 C(z)=\frac1{2\pi i}\int_{-1}^1\frac{\rho(t)}{t-z}\,dt
     =\frac{i}{2\sqrt{z^2-1}}.                         \tag{4.1}
\]

On the cut, `C_++C_-=0`, but

\[
 C(2)=\frac{i}{2\sqrt3}\ne0.                           \tag{4.2}
\]

Interior Plemelj-average zero therefore does not imply exterior zero.  This
is only a local mechanism falsifier: `rho` is not in `L2`, and the oriented
finite Hilbert transform is not the positive split-Carleman old channel.

### 4.2 Exact split-Cauchy/dilation contact

Take the ambient interval `J=(1/3,3)`, collocation nodes
`(1/2,1,2)`, weights `(1,2,4)`, and `v=(1,0,-1)`.  With the exact pole,
split-root, and bilateral one-step dilation matrices used by the replay, at
`q=3/7` and `c=2039/255` the old matrix is

\[
 B=\begin{pmatrix}
 4079/255&781/105&4079/255\\
 781/105&4079/255&781/105\\
 4079/255&781/105&4079/255
 \end{pmatrix}.                                       \tag{4.3}
\]

It is positive semidefinite of rank two and

\[
 Bv=0,
 \qquad E_R(v)=\frac{201161}{8190}\ne0,
 \qquad E_L(v)=-E_R(v).                                \tag{4.4}
\]

This is part of a rational reciprocal-node family, so it is not an accidental
floating-point example.  It proves that split orientation, reflection, old
positivity, and bilateral dilation do not force propagation without using
the completed-zeta coefficients.  It is not a discretization theorem and is
not a counterexample to zeta KNC.

## 5. Final decision-space update

The two requested technical branches are now closed, and both fast
falsifiers are discharged.  The equilibrium statement is:

```text
old serialization       CLOSED exactly on the smooth core, weakly by closure
form-domain adapter      CLOSED for distributions/L2/continuous potential
endpoint/all-jet adapter FALSE generically; needs new solution regularity
global compatibility     OPEN and exactly KNC
coefficient-free route   REFUTED by exact synthetic contact
completed-zeta route     OPEN; must exploit zeta-specific coefficients
uniform zero-free strip  OPEN
RH                       OPEN
```

For the direct KNC lane, the only honest next theorem is a zeta-specific
unique-continuation/spectral-synthesis statement for the plateau in (2.2), or
an equivalent proof that the exact total exterior readout (2.3) annihilates
`ker A_a`.  No further serialization or generic trace work stands between us
and that theorem.  For the uniform-strip goal, the independent R71
source-preserving fixed-window estimate remains the primary route.

## 6. Provenance and novelty

The closed-form/Friedrichs and generic-domain facts are imported from
Suzuki's [current v2 preprint](https://arxiv.org/html/2606.09096v2), especially
its distributional formulas (2.9)--(2.11), form-core argument, and explicit
point-value warning.  Adjacent finite-Hilbert `L2` boundedness is also treated
in the primary literature, for example
[Katsevich--Tovbis](https://arxiv.org/abs/1511.01967); the elementary Carleman
bound used here is sufficient.  The
exact root decomposition, state-space synthesis, and rational hostile model
are project calculations.  This report establishes a rigorous closeout and
route classification, not a claimed literature-level new analytic theorem.

Machine scope is narrower than the human theorem: Lean checks the rational
root identities, finite algebra, and abstract kernel/radical logic.  Python
replays the exact rational hostile witness.  Neither machine layer formalizes
Suzuki's analytic form-core theorem, Carleman's inequality, KNC, a zero-free
strip, or RH.
