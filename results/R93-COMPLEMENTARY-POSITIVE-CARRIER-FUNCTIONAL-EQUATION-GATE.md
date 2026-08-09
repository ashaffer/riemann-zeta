# R93 complementary-positive-carrier functional-equation gate

Status: an exact complementary-tilt reformulation is proved for the R92
Pareto carrier.  An off-critical zeta zero is equivalent to a common Fourier
zero of two explicit nonnegative exponential tilts of the same bounded
sawtooth density.  Positivity, monotone likelihood-ratio order, reflection
symmetry, smoothness, strict log-concavity, Hardy/Blaschke theory,
autocorrelation positivity, and elementary uncertainty do not by themselves
forbid this configuration; exact positive countermodels are given.  The only
surviving route must use the arithmetic placement and equal-height jumps of
the actual floor sawtooth before taking absolute values.  No fixed zero-free
strip, and no theorem excluding such a strip, is proved here.

Date: 2026-08-07.

## 1. Verdict

R92 found the bounded positive density

```text
A(x)=N(N+1-x)/x,                  N=floor(x),
C(u)=A(exp(u)),
```

whose transform is

```text
F(s)=integral_0^infinity C(u)exp(-su)du
    =[(s-1)/(s(s+1))]zeta(s),             Re(s)>0.     (1.1)
```

The rational multiplier has no zero in `Re(s)>0` except its required zero at
`s=1`, where it cancels the zeta pole.  Thus every zero of `F` in this
half-plane is a genuine zeta zero.  This makes the following use of the
functional equation free of the artificial eta zeros from R91.

Suppose

```text
rho=1/2+a+it,                0<a<1/2,
```

is a zeta zero.  Functional-equation symmetry and conjugation make
`1/2-a+it` a zero as well.  Adding and subtracting the two equations from
(1.1) gives

```text
integral_0^infinity
 C(u)e^(-u/2)cosh(au)e^(-itu)du =0,                   (1.2)

integral_0^infinity
 C(u)e^(-u/2)sinh(au)e^(-itu)du =0.                   (1.3)
```

Both densities in (1.2)--(1.3) are nonnegative.  After normalizing the first
one to a probability measure `nu_a`, these conditions are

```text
E_(nu_a)[e^(-itU)]=0,
E_(nu_a)[tanh(aU)e^(-itU)]=0.                          (1.4)
```

This is the cleanest positive joint form found in this branch: the same
unit-modulus phase is orthogonal both to `1` and to the strictly increasing
function `tanh(aU)`.

The order in (1.4) is real but is not enough.  Section 4 constructs, for
every `a` and every chosen scale, a positive three-atom measure whose two
complementary exponential tilts vanish at the same frequency.  Its natural
completion satisfies an exact `s -> 1-s` functional equation.  Section 5
smooths the completed countermodel to a strictly positive, even, analytic,
strictly log-concave Schwartz density without moving any zero.

Consequently the functional equation has converted the strip problem into a
useful two-density cancellation theorem, but generic positive-transform
technology does not prove that theorem.  Any successful inequality must see
the exact floor geometry of `C`, not merely positivity or reflection.

## 2. The carrier and its exact completion relation

Put

```text
P(s)=(s-1)/(s(s+1)),             F(s)=P(s)zeta(s).     (2.1)
```

The completed zeta function is related to `F` by

```text
xi(s)=Q(s)F(s),

Q(s)=(1/2)s^2(s+1)pi^(-s/2)Gamma(s/2).                (2.2)
```

The factor `Q` has no zero or pole in the open critical strip.  Thus the
positive one-sided sawtooth carrier and the usual completed theta carrier
have exactly the same zero set there.  Merely placing both positive
representations in a vector does not create a second analytic degree of
freedom: it gives `(F,QF)`.

Using the convention

```text
zeta(s)=chi(s)zeta(1-s),
```

one also has the exact functional equation

```text
F(s)=R(s)F(1-s),

R(s)=chi(s)(1-s)^2(2-s)/(s^2(s+1)).                   (2.3)
```

All displayed factors in `R` are nonzero at a nontrivial zero in the open
strip.  Hence (2.3), followed by conjugation, gives the mate at the same
positive height.

There is no hidden gain from differentiating (2.3).  At a simple zero,

```text
F'(rho)=-R(rho)F'(1-rho).                              (2.4)
```

On the other hand positivity supplies only upper moment bounds

```text
abs(F^(m)(sigma+it))
 <= integral_0^infinity u^m e^(-sigma u)du
 =m!/sigma^(m+1),                                     (2.5)
```

because `0<=C<=1`.  There is no positive lower bound for a derivative at a
zero.  Thus the gamma-factor size in (2.4) has nothing to contradict.

## 3. Exact complementary-tilt theorem

**Theorem 3.1 (off-line zeros are common zeros of two positive tilts).**
For `0<a<1/2` and real nonzero `t`, define

```text
K_a(t)=integral_0^infinity
 C(u)e^(-u/2)cosh(au)e^(-itu)du,

L_a(t)=integral_0^infinity
 C(u)e^(-u/2)sinh(au)e^(-itu)du.                      (3.1)
```

Then

```text
K_a(t)=L_a(t)=0
```

if and only if

```text
zeta(1/2+a+it)=zeta(1/2-a+it)=0.                      (3.2)
```

By the zeta functional equation, either zero in (3.2) already implies the
other.

### Proof

Absolute convergence follows from `C<=1` and `a<1/2`.  Directly from (1.1),

```text
F(1/2-a+it)=K_a(t)+L_a(t),
F(1/2+a+it)=K_a(t)-L_a(t).                             (3.3)
```

Thus the two transforms in (3.1) vanish if and only if both values of `F`
vanish.  The multiplier `P` is nonzero at both points, so this is equivalent
to (3.2).  QED.

The fixed-strip target is therefore exactly the following statement for some
fixed `0<eta<1/2`:

```text
K_a(t) and L_a(t) are not simultaneously zero

for 1/2-eta<a<1/2 and t!=0.                            (3.4)
```

This formulation is potentially useful because it exposes two positive
weights and the increasing likelihood ratio

```text
L-density / K-density = tanh(au).                      (3.5)
```

It is not already weaker than a strip theorem: by Theorem 3.1 it is exactly
one.

## 4. Exact positive countermodel to the two-tilt idea

The tempting claim that two likelihood-ordered positive tilts cannot share a
Fourier zero is false in the smallest useful finite model.

**Theorem 4.1 (three atoms realize any complementary pair).**  Fix
`0<a<1/2` and `L>0`, and set

```text
c=cosh(aL),

dmu(u)=delta_0+2c e^(L/2)delta_L+e^L delta_(2L).       (4.1)
```

Its one-sided Laplace transform is

```text
G(s)=1+2c e^(L/2)e^(-Ls)+e^L e^(-2Ls)
    =e^(-L(s-1/2)) H(s-1/2),                          (4.2)

H(z)=2[cosh(Lz)+cosh(aL)].                             (4.3)
```

Consequently

```text
G(1/2+a+i(2k+1)pi/L)=0,
G(1/2-a+i(2k+1)pi/L)=0                                (4.4)
```

for every integer `k`.  Moreover its completion obeys

```text
H(z)=H(-z),

G(s)=e^(-L(2s-1))G(1-s).                              (4.5)
```

### Proof

All masses in (4.1) are positive.  Equations (4.2)--(4.3) are a direct
expansion.  The solutions of

```text
cosh(Lz)=-cosh(aL)
```

are

```text
Lz=+/-aL+(2k+1)pi i,
```

which proves (4.4).  Evenness of `H` gives (4.5).  QED.

The cancellation is completely transparent.  At
`t=(2k+1)pi/L`, the phases on `0,L,2L` are `+1,-1,+1`.
For `sigma=1/2+a`, equality of the positive and negative phase masses is

```text
1+e^(-2aL)=2cosh(aL)e^(-aL),                          (4.6)
```

and for `sigma=1/2-a` it is the same identity with `a` replaced by `-a`.

Thus all of the following data are compatible with complementary off-axis
zeros:

```text
positive measure;
strict monotone-likelihood-ratio ordering of the tilts;
real-entire conjugation symmetry;
an exact centered functional equation;
arbitrarily large common zero height;
arbitrarily small distance of the right zero from Re(s)=1.              (4.7)
```

The model does not have the zeta gamma factor or the R92 floor geometry.
Therefore it does not refute an arithmetic theorem for `C`.  It does refute
every proposed proof whose hypotheses have forgotten those features.

Even the leading derivative-size asymmetry from Stirling is not a generic
escape.  From (4.5), the magnitudes of the derivatives at the two simple
mates have ratio `e^(-2aL)`.  Taking `L` of order `(1/2)log t` makes this
`t^(-a)`, the same leading scale as `abs(chi(1/2+a+it))`; the odd integer
`k` in (4.4) can be taken arbitrarily large.  An argument using only that
scale, without the exact gamma phase and arithmetic density, cannot close the
gate.

## 5. Smoothing and strict log-concavity do not repair the theorem

The atomic nature of Theorem 4.1 is inessential.

First, convolve `mu` with any nonzero nonnegative `C_c^infinity` causal
kernel `k`.  The resulting nonnegative smooth density has transform

```text
G(s)K(s),                                               (5.1)
```

so every zero in (4.4) remains.  Multiplying the density by a small positive
constant makes it bounded by one.  Thus regularity and the bound `0<=C<=1`
do not supply a general theorem.

There is a stronger reflection-symmetric version.

**Theorem 5.1 (strictly log-concave positive functional-equation
countermodel).**  Let

```text
dnu=delta_(-L)+2cosh(aL)delta_0+delta_L                (5.2)
```

and convolve it with the centered Gaussian of standard deviation `r>L`.
The resulting density `h_r` is even, strictly positive, real analytic,
Schwartz, and strictly log-concave on the whole real line.  Its bilateral
Laplace transform is, up to a positive constant,

```text
exp(r^2 z^2/2) 2[cosh(Lz)+cosh(aL)],                  (5.3)
```

so it still has every zero

```text
z=+/-a+i(2k+1)pi/L.                                   (5.4)
```

### Proof

Only log-concavity needs checking.  Ignoring a positive constant and writing

```text
A_0=exp(-L^2/(2r^2)),        c_0=L/r^2,
```

the density is

```text
h_r(u)=2exp(-u^2/(2r^2))
       [cosh(aL)+A_0 cosh(c_0u)].                     (5.5)
```

Its logarithmic second derivative is

```text
(log h_r)''
=-1/r^2+c_0^2
 [A_0 cosh(aL)cosh(c_0u)+A_0^2]
 /[cosh(aL)+A_0cosh(c_0u)]^2.                        (5.6)
```

The fraction is at most one, because the denominator squared minus its
numerator is

```text
cosh(aL)^2
+A_0 cosh(aL)cosh(c_0u)
+A_0^2 sinh(c_0u)^2 >=0.                              (5.7)
```

Hence

```text
(log h_r)'' <=-1/r^2+L^2/r^4<0.                       (5.8)
```

The transform formula follows from Gaussian convolution.  QED.

Because `h_r` is even and strictly log-concave, it is also strictly
decreasing on the positive half-line.  This does not contradict the R91
one-sided monotone-Laplace theorem: (5.3) is a *bilateral* transform, or a
positive-half-line `cosh` transform.  The negative half of the density is
essential.

Theorem 5.1 kills a broad theta-kernel shortcut.  Even positivity, radial
monotonicity, analytic smoothness, rapid decay, strict log-concavity, and the
exact symmetry `H(z)=H(-z)` do not force the zeros of a bilateral Laplace
transform onto the imaginary axis.  A theorem for the actual xi theta kernel
must use its modular arithmetic structure or a genuinely stronger class such
as a proved Pólya-frequency property; establishing the latter for xi would
already carry essentially the desired zero information.

## 6. Hardy and Blaschke theory impose no horizontal gap

For every fixed `epsilon>0`, (1.1) and `0<=C<=1` give

```text
abs(F(s))<=1/Re(s)<=1/epsilon,
                         Re(s)>=epsilon.               (6.1)
```

Thus `F` is a bounded analytic function on each shifted right half-plane.
Its zeros there satisfy the ordinary half-plane Blaschke condition

```text
sum_rho (Re(rho)-epsilon)/(1+abs(rho)^2)<infinity.     (6.2)
```

This condition has far too little horizontal resolution.  The standard
zero-counting bound `N(T)=O(T log T)` already implies convergence: on a
dyadic height block, the contribution is `O(k/2^k)`.  A zero with real part
tending to one contributes only `O(1/t^2)`.  Adding its reflected mate
changes only the bounded numerator and still satisfies (6.2).

Equivalently, the associated Blaschke factor is an inner factor and is
invisible to boundary modulus.  Pairing factors to respect conjugation and
`s -> 1-s` does not make them outer.  Hardy factorization can encode the bad
zeros exactly, but it supplies no mechanism forcing the corresponding inner
factor to be trivial.  This is the same logical boundary met by the shifted-xi
Schur and Nyman--Beurling audits elsewhere in the repository.

## 7. Autocorrelation, Gram positivity, and real log-convexity stop at zero

For real `sigma>0`, let

```text
b_sigma(u)=C(u)e^(-sigma u)1_(u>=0).
```

Then

```text
abs(F(sigma+it))^2
```

is the Fourier transform at `t` of the nonnegative autocorrelation

```text
R_sigma(v)=integral b_sigma(u+v)b_sigma(u)du           (7.1)
```

after even reflection.  This proves positive definiteness, not strict
positivity.  The Fourier transform of a triangular autocorrelation is a
`sinc^2` function and has infinitely many zeros.  The three-atom model makes
the same failure occur simultaneously for the complementary tilts.

Likewise, the `2 x 2` Gram matrix of the two Fourier transforms is positive
semidefinite, but at a common zero it is simply the zero matrix.  A Schur
complement cannot manufacture a lower bound after both coordinates have
vanished.

On the real axis, positive Laplace transforms are log-convex:

```text
F(sigma)F''(sigma)-F'(sigma)^2>=0.                    (7.2)
```

The proof is a variance identity.  At `sigma+it`, the phase turns the measure
complex and the sign is lost.  Theorems 4.1 and 5.1 show that neither real
log-convexity nor strict log-concavity of the density restores it.

The most natural signed `2 x 2` determinant also reduces to another
non-strict positive-transform statement.  Put

```text
F_-(t)=F(1/2-a+it),          F_+(t)=F(1/2+a+it)
```

and differentiate with respect to `t`.  Its Wronskian is

```text
W_a(t)=F_-(t)F_+'(t)-F_+(t)F_-'(t)

=i double_integral_(u,v>=0)
 C(u)C(v)e^(-(u+v)/2)
 (v-u)sinh(a(v-u))e^(-it(u+v))du dv.                 (7.3)
```

Indeed, expanding the determinant and averaging the integrand with its
`u,v` swap gives (7.3).  The factor

```text
(v-u)sinh(a(v-u))
```

is nonnegative.  Hence `W_a(t)/i` is the Fourier transform, in the sum
coordinate `u+v`, of an explicit positive push-forward measure.  At a common
zero of `F_-` and `F_+`, the Wronskian necessarily vanishes.  Positivity of
the push-forward therefore gives no contradiction; Theorem 4.1 supplies an
exact finite countermodel in which this vanishing occurs.  Higher moment or
Wronskian determinants have the same logical defect unless the exact
sawtooth geometry yields an additional strict sign before Fourier
transformation.

## 8. Phase and uncertainty bounds are vacuous at zeta height

If a positive measure is supported in an interval of length strictly less
than `pi/abs(t)`, its Fourier transform cannot vanish at `t`: after rotating
the interval midpoint to phase zero, every phase has positive real part.
This is the elementary positive-measure uncertainty bound.

It does not help here.  The actual sawtooth density has support
`[0,infinity)`.  The countermodel in Theorem 4.1 uses width exactly
`2pi/abs(t)` and realizes both complementary zeros.  Positive smoothing only
enlarges that width by an arbitrarily small amount.  As the zero height grows,
the necessary spatial scale shrinks like `1/abs(t)`, while the floor
sawtooth has structure on arbitrarily small logarithmic cells.

The equivalent convex-hull statement is equally weak.  A positive Fourier
transform can vanish only if its support phases are not contained in an open
semicircle.  For every nonzero `t`, the phases `e^(-itu)` generated by the
unbounded support of `C` wind around the circle infinitely often.  Both
exponential tilts have the same phase support, so reflection does not improve
this condition.

## 9. The exact sawtooth shows where positivity is spent

On a logarithmic cell,

```text
log(N)<=u<log(N+1),

C(u)=N(N+1)e^(-u)-N.                                  (9.1)
```

It decreases strictly from one to zero, then jumps upward by one at the next
integer.  In distribution form,

```text
dC(u)
=-sum_(N>=1) N(N+1)e^(-u)
  1_[log N,log(N+1))(u)du
 +sum_(n>=2) delta_(log n).                           (9.2)
```

Each open-cell density is as well behaved as one could reasonably ask: it is
positive and decreasing, and its logarithm is strictly concave.  All global
difficulty is in the exact cancellation between the negative in-cell drift
and the positive integer jump comb.

Integrating (9.2) by parts at a finite cutoff separates these two terms.  At
real exponent `sigma<1`, the positive jump variation up to `X` is

```text
sum_(n<=X)n^(-sigma) asymp X^(1-sigma)/(1-sigma),      (9.3)
```

and the absolute in-cell drift has the same leading order.  Their signed
combination is the bounded transform (1.1), but either piece separately
diverges as the cutoff tends to infinity.  At `sigma=1-eta`, an argument
which takes absolute values before recombining pays the fixed power `X^eta`.

This is the carrier-specific version of the main repository warning.  A
monotonicity decomposition, jump-by-jump triangle inequality, or positive
transfer bound destroys exactly the cross-cell cancellation needed for a
fixed strip.  The complementary mate at exponent `1/2-a` makes the loss more,
not less, visible when `a` is close to `1/2`.

The continuous Pareto filter itself has transfer multiplier

```text
(s-1)/(s+1),                                           (9.4)
```

a zero-free high-pass factor away from its pole-cancelling zero.  It removes
the eta recurrence problem, but a passive or state-space realization of this
known factor cannot remove zeros already present in its zeta input.

### 9.1 The adjacent-cell determinant has only a moving local sector

The exact floor geometry does give one nontrivial local sign, but it does not
globalize.  Let

```text
I_N=[log N,log(N+1)],        w(u)=C(u)e^(-u/2),

X_N^-(a,t)=integral_(I_N) w(u)e^(au)e^(-itu)du,
X_N^+(a,t)=integral_(I_N) w(u)e^(-au)e^(-itu)du.       (9.5)
```

For `N<M`, direct expansion gives the exact cell determinant

```text
D_(N,M)=X_N^- X_M^+ - X_N^+ X_M^-

=-2 double_integral_(u in I_N,v in I_M)
 w(u)w(v)sinh(a(v-u))e^(-it(u+v))du dv.               (9.6)
```

Before the oscillatory phase, the integrand in (9.6) has one strict sign.
Put

```text
q_0=(1/2)log[NM(N+1)(M+1)],
Omega_(N,M)=log[(N+1)(M+1)/(NM)].                      (9.7)
```

If

```text
abs(t) Omega_(N,M)<pi,                                 (9.8)
```

then

```text
Re[-e^(it q_0)D_(N,M)]>0.                             (9.9)
```

Indeed, `u+v-q_0` lies in an interval of radius
`Omega_(N,M)/2`, so the real part of the rotated phase is positive under
(9.8).  For adjacent cells, (9.8) reads

```text
abs(t)log(1+2/N)<pi,                                  (9.10)
```

and the simple sufficient range is `N>2abs(t)/pi`.

Thus adjacent high-index cells retain a complex version of strict total
positivity.  The obstruction is exact: the sector rotation `e^(itq_0)` moves
with `N,M`, and (9.8) fails throughout the head and resonant range
`N=O(abs(t))`.  Removing those rotations by absolute values pays the cell
variation from (9.3).  Consequently the local determinant does not rule out
a common zero of the two *global* sums.  It identifies a genuine piece of
structure, but also its cutoff: any successful global determinant theorem
must phase-lock the moving sectors across the resonant cells by arithmetic
means.

## 10. What remains genuinely open

The new exact target (3.4) is worth retaining.  It gives three stringent
admission tests for a successor idea.

1. It must distinguish the equal upward jumps at the exact locations
   `log(n)` from the three-atom and smoothed countermodels in Sections 4--5.
2. It must recombine the jump comb with the in-cell drift before absolute
   values; otherwise it pays (9.3).
3. It must use the two tilts jointly in a way stronger than a positive scalar
   sum, a Gram matrix, an autocorrelation, or a boundary Hardy norm.

A concrete sufficient theorem would be a carrier-specific signed determinant
or phase-separation estimate proving

```text
abs(K_a(t))^2+abs(L_a(t))^2>0                         (10.1)
```

for all `1/2-eta<a<1/2` and all real nonzero `t`, with the proof expanded at
the level of (9.1)--(9.2).  By Theorem 3.1, (10.1) is already the fixed-strip
theorem; its value is as a sharply falsifiable target, not as a reduction in
difficulty.

The adjacent-cell fail-fast experiment has been executed in (9.5)--(9.10).
It yields strict sectorial total positivity only beyond the moving threshold
`N` of order `abs(t)`, with a sector angle that changes from pair to pair.
The next admissible step would therefore have to phase-lock those exact local
determinants across `N=O(abs(t))`; repeating the determinant without such a
lock cannot help.

## 11. Exact disposition

This audit proves the following reusable statements.

1. An off-critical zeta zero is exactly a common Fourier zero of the two
   nonnegative sawtooth tilts (3.1).
2. Positive exponential tilts in strict likelihood-ratio order can share such
   a zero; a three-atom model realizes any prescribed horizontal displacement.
3. Exact reflection symmetry, smoothness, rapid decay, strict positivity,
   radial monotonicity, and strict log-concavity still do not force centered
   zeros onto the imaginary axis.
4. Hardy/Blaschke, autocorrelation/Gram, real log-convexity, and elementary
   uncertainty conditions are all compatible with zeros approaching
   `Re(s)=1` at unbounded height.
5. For the actual R92 density, separating its positive jumps from its negative
   drift costs `X^(1-sigma)` and therefore destroys a fixed-power argument.
6. Adjacent sawtooth cells have an exact sectorial determinant sign only in
   the narrow-cell range (9.8); its moving phase and resonant head prevent a
   global total-positivity conclusion.

This report does **not** prove that a fixed zero-free strip exists.  It also
does **not** prove that no fixed zero-free strip exists.  The continuous
carrier remains a genuine simplification because it has no artificial zeros;
the complementary functional equation turns its remaining problem into the
precise signed joint estimate (10.1).
