# Xi Fourier-kernel strip audit

Status: no fixed zero-free strip is proved.  A sharp countermodel shows that
positivity, evenness, real analyticity, strict log-concavity, all-order boundary
jet cancellation, the centered functional equation, and even the exact leading
double-exponential Xi tail can all coexist with transform zeros arbitrarily
close to the boundary of the trivial strip.  Translation total positivity of
infinite order is inapplicable (and false for the Xi kernel), while finite-order
total positivity and fixed-degree Jensen tests point in the wrong geometric
direction.  The remaining Fourier route must use the discrete theta arithmetic
before it is compressed into qualitative kernel shape.

Date: 2026-08-12.

## 1. Centered Laplace normalization

Write

```text
X(s) = xi(1/2+s) = integral_R Phi(u) exp(su) du,        (1.1)
```

up to the harmless conventional scaling of `u`.  The theta kernel `Phi` is
positive and even, so `X` is real entire and even.  If

```text
s=a+it,
```

then a zero is equivalent to the two cancellations

```text
integral_0^infinity Phi(u) cosh(au) cos(tu) du = 0,
integral_0^infinity Phi(u) sinh(au) sin(tu) du = 0.    (1.2)
```

The desired fixed strip is the assertion that, for some `a<1/2`, all zeros of
`X` have `abs(Re(s))<=a`.

Positivity does not make either oscillatory integral in (1.2) positive.  The
question is whether adding the much stronger known shape of `Phi` repairs this.
The next theorem says that those qualitative shape hypotheses, even combined,
do not do so generically; it is not a statement about the actual `Phi`.

## 2. An Xi-tail, strictly log-concave countermodel

### Theorem 2.1

Fix any

```text
0 < a_* < a_0 < 1/2
```

and any `k>1`.  There is a sequence of positive even kernels `h_L`, with
`L -> 0+`, having all of the following properties.

1. `h_L` is real analytic and strictly log-concave on the whole real line.
2. Every odd derivative of `h_L` at zero vanishes.
3. Its bilateral Laplace transform

   ```text
   H_L(s)=integral_R h_L(u)exp(su)du
   ```

   is entire, real, and even, hence obeys the exact centered functional
   equation `H_L(s)=H_L(-s)`.
4. It has the Xi leading tail

   ```text
   log h_L(u) = -pi exp(4 abs(u)) + O_L(u^2)          (2.1)
   ```

   as `abs(u)->infinity`.
5. It has a quartet of zeros `+/-s_L,+/-conj(s_L)` with

   ```text
   Im(s_L) = pi/L + o(1),
   Re(s_L) -> a_0.                                    (2.2)
   ```

In particular, `Re(s_L)>a_*` for all sufficiently small `L`.  Since `a_*`
may be arbitrarily close to `1/2`, the listed kernel properties imply no
nontrivial uniform strip.

### Construction

Put `r=kL` and let

```text
G_r(u)=exp(-u^2/(2r^2)),

g_L(u)=G_r(u-L)+2 cosh(a_0 L)G_r(u)+G_r(u+L).         (2.3)
```

The Gaussian-mixture calculation in
`R93-COMPLEMENTARY-POSITIVE-CARRIER-FUNCTIONAL-EQUATION-GATE.md`, Theorem
5.1, proves that `g_L` is strictly log-concave whenever `r>L`.

Now define the fixed tail factor

```text
q(u)=exp{-2pi[cosh(4u)-1-8u^2]},
h_L(u)=g_L(u)q(u).                                    (2.4)
```

The elementary inequality `cosh(4u)>=1+8u^2` gives `0<q<=1`.  Moreover,

```text
(log q)'' = -32pi[cosh(4u)-1] <= 0.                  (2.5)
```

Thus `q` is log-concave, and the product with the strictly log-concave `g_L`
is strictly log-concave.  Both factors are positive, even, and real analytic.
Evenness gives all odd boundary jets and the functional equation.

Finally,

```text
-2pi cosh(4u) = -pi exp(4 abs(u))+o(1),
```

while the remaining terms in `log h_L` are at most quadratic.  This proves
(2.1), and the double-exponential decay makes `H_L` entire.

### Persistence of the off-axis zeros

The root calculation is quantitative.  Scale

```text
u=Lv,       w=Ls,

F_L(w)=L^(-1)H_L(w/L)
      =integral_R g_L(Lv)q(Lv)exp(wv)dv.              (2.6)
```

Without `q`, Gaussian integration gives exactly

```text
B_L(w)=2 C_k exp(k^2 w^2/2)
       [cosh(w)+cosh(a_0 L)],                         (2.7)
```

where `C_k>0` is independent of `w` and `L`.  Hence `B_L` has the simple
zeros

```text
w=+/-a_0 L+i(2m+1)pi.                                (2.8)
```

The subtraction of `1+8u^2` in (2.4) is important.  Taylor expansion gives

```text
cosh(4Lv)-1-8L^2v^2=(32/3)L^4v^4+O(L^6v^6),
q(Lv)=1+O(L^4v^4)                                    (2.9)
```

on bounded scaled sets.  Gaussian domination upgrades (2.9), uniformly for
`z` in compact subsets of the plane, to

```text
F_L(i pi+Lz)=B_L(i pi+Lz)+O(L^4).                    (2.10)
```

Here is an explicit domination for that step.  Taylor's theorem gives, for
real `x`,

```text
0 <= cosh(4x)-1-8x^2
   <= (32/3)x^4 cosh(4 abs(x)).                       (2.10a)
```

Since `0<=1-exp(-y)<=y` for `y>=0`,

```text
abs(q(Lv)-1)
 <=(64pi/3)L^4 v^4 cosh(4L abs(v)).                  (2.10b)
```

For `w=i pi+Lz` and `z` in a fixed compact set, every term of
`g_L(Lv)exp(wv)` is bounded in modulus by a shifted Gaussian in `v` times
`exp(C L abs(v))`.  Multiplying by the right side of (2.10b) and integrating
therefore gives `C_K L^4`, uniformly on that compact set.  This proves the
locally uniform error claimed in (2.10), rather than only pointwise
convergence.

But

```text
cosh(i pi+Lz)+cosh(a_0L)
  =cosh(a_0L)-cosh(Lz)
  =(L^2/2)(a_0^2-z^2)+O(L^4).                        (2.11)
```

After division by the common nonzero Gaussian factor and by `L^2`, (2.10)--
(2.11) converge locally uniformly to a nonzero multiple of `a_0^2-z^2`.
Rouche's theorem on small disjoint circles around `z=+/-a_0` therefore gives
roots `z_L -> +/-a_0`.  Returning to `s=w/L` proves (2.2).  Reality and
evenness supply the full quartet.  QED.

This is a scoped countermodel theorem.  The kernels `h_L` are not asserted to
be the Riemann theta kernel, and the theorem neither constructs an off-line zeta
zero nor disproves a zeta zero-free strip.

## 3. Consequences for the proposed kernel properties

Theorem 2.1 simultaneously closes the following generic implications:

```text
positive + even                                      -/-> fixed strip;
strictly decreasing on the positive half-line       -/-> fixed strip;
strict log-concavity (Toeplitz TP_2)                 -/-> fixed strip;
real analyticity and all odd boundary jets zero      -/-> fixed strip;
exact centered functional equation                   -/-> fixed strip;
Xi-rate double-exponential decay                     -/-> fixed strip;
all of the preceding properties together             -/-> fixed strip. (3.1)
```

This strengthens the earlier Gaussian countermodel: the possible escape through
the special theta tail is now removed at its leading exact scale.  It does not
imitate the integer theta series itself.  That discrete arithmetic is precisely
what a surviving theorem must retain.

## 4. Total positivity points in the wrong direction

There are two distinct notions which should not be conflated.

### 4.1 Translation total positivity

If `Phi(x-y)` were totally nonnegative of every order (a Polya-frequency
function), Schoenberg's bilateral-Laplace representation would make its transform
zero-free wherever the transform is finite.  The actual transform is Xi and has
known real-frequency zeros.  Therefore the actual Xi kernel is **not** a
translation `PF_infinity` function, independently of RH.

Order two is merely log-concavity and is covered by Theorem 2.1.  For a compactly
supported `PF_p` function of support length `rho`, Schoenberg's finite-order
theorem excludes transform zeros with

```text
abs(Im(s)) < p pi/rho.                                (4.1)
```

In the Xi convention this controls the *frequency/ordinate* coordinate, not
`Re(s)`, which is the horizontal displacement relevant to a zero-free strip.
The Xi kernel also has unbounded support.  Thus finite-order translation total
positivity supplies neither the required orientation nor the required scale.

### 4.2 Hankel total positivity

Hankel positivity concerns kernels of the form `Phi(x+y)` and is a different
moment problem.  It cannot be inferred from log-concavity of `Phi(x-y)`.  Any
proposal using it must state a new theta-specific determinant inequality and then
show how that inequality implies the Hermite--Biehler condition below.  No such
inequality is presently available.

## 5. Jensen-polynomial blindness at fixed degree

Fixed-degree Jensen or Laguerre inequalities cannot see a zero quartet whose
height tends to infinity.  Switch here to the Fourier-frequency variable
`z=-is`.  In its centered Hadamard expansion, an off-axis zero

```text
rho_z=T+ia,       theta=arg(rho_z)=a/T+O(T^-3)
```

contributes at logarithmic order `m` through

```text
Re(rho_z^(-2m))=abs(rho_z)^(-2m)cos(2m theta).        (5.1)
```

For every fixed `m`, the difference from an on-axis zero is only
`O(m^2a^2/T^2)`.  Resolving the displacement requires orders with

```text
m theta comparable to 1, hence m comparable to T/a. (5.2)
```

This explains why eventual hyperbolicity for each fixed Jensen degree, or any
finite list of Turan inequalities, has no uniform-strip content.  One needs a
joint theorem with degree growing at least on the height scale.  Such a theorem
would be a new global zero-localization result, not a consequence of the known
fixed-degree asymptotics.

## 6. The exact surviving Fourier criterion

For `a>0`, set

```text
E_a(z)=X(a-iz).
```

By evenness and reality, all zeros of `X` lie in `abs(Re(s))<=a` if and only if
`E_a` is a Hermite--Biehler function (with the usual harmless convention on
boundary zeros).  Equivalently, the shifted ratio

```text
Theta_a(z)=E_a#(z)/E_a(z)
```

is analytic and contractive in the upper half-plane.  On the real boundary its
phase derivative is

```text
-Im[E_a'(t)/E_a(t)] = Re[X'(a-it)/X(a-it)].           (6.1)
```

Thus an admissible Fourier breakthrough must establish the shifted
Hermite--Biehler/Schur condition at one explicit `a<1/2`.  Positivity and
log-concavity do not establish it: Theorem 2.1 gives counterexamples satisfying
all those shape hypotheses.

Strong universal factors do genuinely narrow zero strips, but using one here
requires an independently proved factorization of the **full** theta kernel into
a known real-rooted Fourier kernel times a certified strong universal factor.
The dominant-term/finite-theta decompositions do not qualify: their boundary
jets have algebraic Fourier tails, and the infinite modular cross terms cancel
those tails at all orders.  This is exactly the obstruction recorded in
`THETA-BOUNDARY-JET-CANCELLATION.md` and
`MODULAR-ORBIT-GRAM-AUDIT.md`.

## 7. Functional-equation polynomial factors do not help

In centered variables,

```text
s_original(s_original-1)=-(z^2+1/4).
```

The polynomial in the completed Xi function cancels the two boundary poles of
the uncompleted Mellin transform.  It is nonzero at every nontrivial zero in the
open critical strip and therefore neither moves nor narrows that zero set.
Treating its integration-by-parts action as a strip-decreasing differential
operator loses the pole-cancellation boundary terms and is invalid.  Any gain
must come from the theta/Euler arithmetic, not from the completion polynomial.

## 8. Verdict

No explicit `delta>0` was obtained.  The branch does, however, sharply prune the
search space:

1. generic positive-kernel, log-concavity, `PF_2`, tail, smoothness, and symmetry
   arguments are closed even in combination;
2. translation `PF_infinity` is impossible for the actual Xi kernel;
3. finite-order total positivity and fixed-degree Jensen theory have the wrong
   orientation or insufficient height resolution;
4. the only live Fourier target is a theta-arithmetic proof of one shifted
   Hermite--Biehler inequality, or an explicit full-theta strong-universal-factor
   decomposition whose stability is proved independently of Xi's zeros.

The second alternative would actually be stronger than a fixed strip if the base
transform is already real-rooted.  It should therefore be treated as an RH-scale
target, not as a soft consequence of kernel shape.

## Primary references

- P. Branden and M. Chasse, *Classification theorems for operators preserving
  zeros in a strip*, arXiv:1402.2795.
- A. Khare, *Multiply positive functions, critical exponent phenomena, and the
  Jain--Karlin--Schoenberg kernel*, arXiv:2008.05121, especially the finite-order
  Laplace zero theorem.
- I. J. Schoenberg, *On the zeros of the generating functions of multiply
  positive sequences and functions*, Annals of Mathematics 62 (1955).
