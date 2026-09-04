# Blaschke density isolation: the one-product theorem and compact-transfer gate

Status: exact Hardy-space extremal, corrected Riemann--von Mangoldt
potential ledger, exact finite-interval Gram reduction, and scoped no-go for
the one-branch target-positive construction, 2026-08-12.  This note proves a real
positive exponent in an *ideal phase-cell-compressed half-line model*.  It
does not prove actual-zeta collateral isolation or a zero-free strip.

## 1. Verdict

There is a genuine `d>1/2` mechanism, but it does not yet close the current
program.

* If one endpoint component is constrained by the collateral zeros and the
  opposite endpoint is left unconstrained, the selected pair pays one
  Blaschke product.  After the Riemann--von Mangoldt main density, both
  ordinate signs, the Bellotti--Wong endpoint discrepancy, and one effective
  condition per phase cell are all included, a strictly positive exponent
  survives for every fixed `d>1/2`.
* If every collateral zero is put on one endpoint branch and the same state
  is required to satisfy the selected positive-row equation

  ```text
  F(alpha)+F(-alpha)=0,
  ```

  then that branch's Blaschke product is squared.  This **does not** force
  the square of the full product: the subsequent bipartite theorem splits
  conditions between the two legs, balances their Hardy potentials, and
  restores the one-product exponent on the same selected-positive state.
* The causal Hardy extremizer is supported on a half-line, not in the
  required finite packet interval.  For finite support the exact answer is
  a truncated-Cauchy Gram determinant.  No uniform theorem comparing that
  determinant with the Hardy product for `Theta(L)` moving nodes is presently
  proved.
* The known coherent microcluster theorem supplies phase-cell compression
  only on one bounded `L`-rescaled rectangle.  A simultaneous compression
  across `Theta(L)` cells, including the slowly growing near-depth collar,
  remains open.

Thus the new direction is mathematically real: prove a compact
phase-cell-compressed, balanced two-leg **one-product** transporter.  No
unequal-target-endpoint relaxation is now required algebraically, but the
growing compact realization and arithmetic admission theorem remain open.

## 2. Exact half-plane extremal

Let `z_j` be distinct effective condition nodes (with a factor repeated only
when the corresponding derivative condition is also imposed), and write

```text
z_j=beta_j-i*delta_j,       beta_j>0,
B(s)=product_j (s-z_j)/(s+conj(z_j)).                (2.1)
```

In the right-half-plane Hardy space, the closed subspace of functions
vanishing at every `z_j` is `B H^2`.  Since multiplication by `B` is
isometric on the boundary, the reproducing-kernel calculation gives

```text
sup { |G(alpha)| : ||G||_(H^2)<=1, G(z_j)=0 }
 =|B(alpha)|/sqrt(2*alpha),                          (2.2)

|B(alpha)|
 =product_j sqrt(
    ((alpha-beta_j)^2+delta_j^2)
   /((alpha+beta_j)^2+delta_j^2)).                  (2.3)
```

Equality is attained in `H^2` by a normalized multiple of

```text
B(s)/(s+alpha).                                     (2.4)
```

For a packet `q` supported in `[-D/2,D/2]`, put

```text
F(s)=integral q(t)exp(s*t)dt,
G(s)=exp(-s*D/2)F(s).                               (2.5)
```

Then (2.2) implies

```text
|F(alpha)|
 <=exp(alpha*D/2)|B(alpha)| ||q||_2/sqrt(2*alpha). (2.6)
```

This is a necessary bound for compact packets.  Equality in (2.2) is an
equality in the unrestricted causal space `L^2(0,infinity)`, not an
attainment statement in `L^2(0,D)`.

## 3. The three factor-twos

For a near-tie node `beta_j=alpha-o(1)`, define its amplitude potential

```text
V_alpha(delta)
 =(1/2)*log(1+(2*alpha/delta)^2).                   (3.1)
```

The elementary integral is

```text
integral_R V_alpha(delta)d delta=2*pi*alpha.        (3.2)
```

There are three distinct factor-twos.

1. Riemann--von Mangoldt counts both horizontal members of an off-line
   reflected pair.  Hence pair centers have main full-line density

   ```text
   p*L,       p=1/(4*pi),                            (3.3)
   ```

   half the all-zero density.
2. Collaterals can occur on both ordinate sides of the selected zero.  The
   full-line integral (3.2), rather than its one-sided half, is required.
3. A selected reflected-pair value is quadratic in the endpoint
   evaluations.  If every root is put on one branch, selected-row balancing
   reduces both endpoints to that branch's constrained size and squares
   its product.  If roots are split between two legs with potentials
   `S_R,S_L`, the loss is instead `2*max(S_R,S_L)`; greedy balance makes
   this one full product up to the largest individual weight.

Consequently the uniform main-density cost is

```text
one-product cost:       p*integral_R V=alpha/2,
positive-row/square cost:                 alpha.    (3.4)
```

The first line leaves `alpha*(d-1/2)` from a carrier of exponent
`alpha*d`.  The second leaves only `alpha*(d-1)`, but it is only the
one-branch assignment.  Balanced bipartite splitting attains the first
line while retaining the selected positive-row equality; see the report
cited at the end.

## 4. Bellotti--Wong plus phase-cell compression

The endpoint discrepancy must be added to, not substituted for, the
Riemann--von Mangoldt main term.  For every fixed `h` and a center
`gamma asymp T`, Bellotti--Wong gives

```text
N(gamma+h)-N(gamma-h)
 <=[h/pi+0.20152+o(1)]*L.                           (4.1)
```

After horizontal pairing, the number `M(h)` of off-line pair centers obeys

```text
M(h)/L<=h/(2*pi)+a+o(1),       a=0.10076.           (4.2)
```

Now make the following explicit **compression hypothesis**:

> Across the whole carrier-relevant list, every occupied ordinate phase cell
> of width `2*pi/D` costs at most one effective Blaschke condition, and all
> further members are made nonpositive with one **total** `X^o(1)` loss.  This
> is a global loss bound, not a separate `X^o(1)` factor that may be multiplied
> over `Theta(L)` cells.

The coherent microcluster theorem proves this on any one fixed bounded
`L`-rescaled depth/ordinate rectangle.  It does not yet prove the global
hypothesis above.

Write `mu_L=L^(-1)*sum_j delta_(delta_j)` for the chosen cell
representatives and pass to a weak local limit `mu`.  Under the hypothesis,
that effective-condition measure satisfies

```text
mu([-h,h])<=a+2*p*h,
mu(I)<=q*|I|,                q=d/(2*pi),             (4.3)
```

up to vanishing endpoint errors.  The cell cap exceeds the main pair
density exactly when `d>1/2`.

Here the target is chosen with maximal depth in the finite carrier-relevant
band, so `0<beta_j<=alpha`.  The potential for such a node is bounded above
by `V_alpha`; a deeper node would have to be promoted to the target before
this ledger is applied.

Because `V_alpha` is even and decreasing in `|delta|`, layer-cake
rearrangement shows that the largest potential allowed by (4.3) has density
`q` on `[-h_0,h_0]` and density `p` outside, where

```text
h_0=a/[2*(q-p)]=2*pi*a/(2*d-1).                     (4.4)
```

Put

```text
y=h_0/(2*alpha)=pi*a/[alpha*(2*d-1)],
R(y)=[y*log(1+y^(-2))+2*atan(y)]/pi.                (4.5)
```

Then `0<R(y)<1` for every finite `y`, and direct integration gives the
sharp one-product upper bill

```text
integral V_alpha d mu
 <=alpha/2+alpha*(d-1/2)*R(y).                     (4.6)
```

Therefore the retained half-line exponent is at least

```text
E_1(alpha,d,a)
 =alpha*(d-1/2)*(1-R(y))>0                         (4.7)
```

for every fixed `alpha>0`, finite `a`, and `d>1/2`.

At the current endpoint values,

```text
E_1(1/2,2/3,0.10076)=0.0133834321...,
E_1(0.49,2/3,0.10076)=0.0128736062....              (4.8)
```

This is much smaller than the calculation which uses only the `0.10076 L`
discrepancy conditions: (4.6) also charges the full Riemann--von Mangoldt
main density.  It nevertheless remains strictly positive.

The cell cap is doing essential work here.  A root-per-row ledger may
superpose the full main-density background and all `aL` discrepancy roots
in the most dangerous cells.  That is the negative combined ledger in the
coherent-microcluster report, equal to `-0.0960289999...` at
`(alpha,d)=(1/2,2/3)`.  Under (4.3), by contrast, the discrepancy conditions
**displace** background conditions once a cell is occupied: overlaying the
old background and discrepancy densities would exceed the cap `q` there.
Thus (4.7) is a conditional gain from global phase-cell compression, not a
consequence of zero counting alone.

If all effective conditions are put on one branch, (4.6) is doubled.
Balanced two-leg splitting divides the potential between the branches and
returns the one-product bill, provided both grouped cascades admit the same
compact transfer.

## 5. Why Huxley does not complete the hypothesis

For every fixed line `sigma<1`, the Ingham--Guth--Maynard--Huxley envelope
has a positive power exponent.  Near one, Huxley gives

```text
N(sigma,T)
 <=T^[3*(1-sigma)/(3*sigma-1)+o(1)].                (5.1)
```

An exceptional target-centered cluster of `O(L)` zeros at any fixed depth
strictly below one is far smaller than (5.1).  Thus global horizontal
density does not improve (4.2) uniformly at the selected height and does
not prove the phase-cell compression hypothesis.  Bellotti's `O(1)` result
near the moving Vinogradov--Korobov boundary does not apply at a fixed
depth.

Conversely, the known density theorems are consistent with one near-depth
node in each of `Theta(L)` consecutive phase cells around a sparse target
height.  This is exactly the configuration for which a simultaneous compact
transporter is needed.

## 6. Exact finite-support endpoint gate

The endpoint issue has a finite-dimensional exact form.  In `L^2(0,D)` let

```text
k_z(u)=exp(-conj(z)*u),
K_D(z,w)=<k_w,k_z>
        =[1-exp(-(z+conj(w))*D)]/[z+conj(w)].        (6.1)
```

For the constraint space

```text
E_D={f:<f,k_(z_j)>=0 for every j},                  (6.2)
```

the exact retained evaluation is

```text
sup_(f in E_D, ||f||=1)|<f,k_alpha>|
 =dist(k_alpha,span{k_(z_j)}).                     (6.3)
```

If `Gamma_D=(K_D(z_i,z_j))` and
`v_D=(K_D(z_i,alpha))`, its square is

```text
K_D(alpha,alpha)-v_D^* Gamma_D^dagger v_D.          (6.4)
```

For `D=infinity`, the Cauchy determinant evaluates (6.4) as

```text
(1/(2*alpha))*|B(alpha)|^2.                         (6.5)
```

For finite `D`, (6.4) is at most (6.5).  It tends to (6.5) for a fixed
finite list as `D->infinity`, but that convergence is not uniform when the
number of nodes is `Theta(L)` and `D=dL`.  Equation (6.4), rather than the
half-line product alone, is the exact compact PW/Gabor endpoint gate.

A useful sufficient tail estimate illustrates the missing constant.  If
`a_0<=Re z_j`, `0<eta<min(a_0,alpha)`, and `g` is the inverse Laplace
transform of `B(s)/(s+alpha)`, then

```text
||1_(t>W)g||_2^2
 <=exp(-2*eta*W)
   *product_j ((Re z_j+eta)/(Re z_j-eta))^2
   /[2*(alpha-eta)].                                (6.6)
```

The logarithmic derivative of the right side of (6.6) at `eta=0` is
`-2W+4*sum_j 1/(Re z_j)+1/alpha`.  Thus an exact infinitesimal decrease asks
for `W>2*sum_j 1/(Re z_j)+1/(2*alpha)`.  When `W` and `M` are of order `L`,
the leading exponential margin is therefore

```text
W>2*sum_j 1/(Re z_j),                               (6.7)
```

and the cruder consequence is `W>2M/a_0`.  With only the discrepancy count
`M<=0.10076 L`, near-depth nodes have `a_0 approximately alpha`, and the
optimistic choice `W=dL`, this asks

```text
alpha*d>0.20152.                                    (6.8)
```

At `d=2/3` it reaches only `alpha>0.30228...`; it is not uniform in the
strip depth.  More importantly, truncation destroys the exact zeros, and
correcting `Theta(L)` residual conditions returns to the Gram conditioning
problem (6.4).  The physically available `W` must also be audited against
the actual lobe/endpoint layout; it cannot simply be declared equal to
`D`.

## 7. Same-state correction: bipartite splitting removes the wall

Write

```text
A=F(alpha),       C=F(-alpha).                      (7.1)
```

The selected reflected-pair form is proportional to

```text
2*Re(A*conj(C))
 =(1/2)*(|A+C|^2-|A-C|^2).                         (7.2)
```

Suppose first that every collateral zero is imposed on the right endpoint.
The Hardy extremal permits `|A|` of size `B_alpha` times its unconstrained
endpoint scale, while `|C|` may retain the full opposite-endpoint scale.
Choosing opposite phases makes (7.2) negative at one-product size before
the selected row is imposed.

The current target-only feasible space imposes `A+C=0`.  It follows
identically that

```text
|A|=|C|,
2*Re(A*conj(C))=-2*|A|^2.                           (7.3)
```

For that one-branch assignment the smaller constrained endpoint bounds both
sides, so (7.3) has size `B_alpha^2`.  The word "one-branch" is essential.

Color each collateral pair red or blue and annihilate its right evaluation
on the red leg or its left evaluation on the blue leg.  If the corresponding
Hardy potentials are `S_R,S_L`, selected-row balancing gives the harmonic
mean

```text
|A|^2 asymp exp(alpha*D)
 *[exp(2*S_R)+exp(2*S_L)]^(-1),                    (7.4)
```

whose exponent loss is `2*max(S_R,S_L)`.  Greedy two-bin balancing gives

```text
2*max(S_R,S_L)
 =S_R+S_L+O(max_j w_j).                            (7.5)
```

For `max_j w_j=o(L)`, this is exactly one full product.  Thus the selected
positive-row equality does **not** intrinsically square the global bill.

The continuation problem is now quantitative rather than algebraic:

1. prove global phase-cell compression across the growing list;
2. balance the resulting grouped conditions between the two legs;
3. compactly realize both causal filters with the exponent in (4.7); and
4. establish the arithmetic admission sign on that same state.

## 8. Truth table

| assertion | verdict |
|---|---|
| Hardy extremal equals a Blaschke product | **proved**, on the half-line |
| the RvM main pair density is `L/(4*pi)` | **proved** |
| both ordinate signs leave one-product threshold `d>1/2` | **proved** |
| Bellotti--Wong discrepancy destroys that threshold after ideal cell compression | **no**; (4.7) remains positive |
| Huxley supplies the required uniform local compression | **no** |
| the Hardy extremizer is automatically compactly supported | **false** |
| finite-support optimum is the Gram quantity (6.4) | **proved** |
| one-branch selected-positive construction pays a square | **proved** |
| balanced two-leg selected-positive construction pays one product | **proved in the causal model** |
| actual-zeta collateral isolation on the current same state | **open** |

Related local theorem:
[`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`](ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md).

Same-state correction:
[`ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`](ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md).

Primary counting inputs:
[Bellotti--Wong, *Improved estimates for the argument and zero-counting of
the Riemann zeta-function*](https://arxiv.org/abs/2412.15470) and
[Huxley, *On the difference between consecutive
primes*](https://doi.org/10.1007/BF01418933).
