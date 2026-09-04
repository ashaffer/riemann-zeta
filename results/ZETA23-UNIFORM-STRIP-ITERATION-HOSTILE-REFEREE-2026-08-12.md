# Uniform-strip iteration: hostile referee audit

Status: **binary verdict -- NO STRIP PROVED**, 2026-08-12.

This audit checks the four reports produced in the post-sprint iteration:

1. `ZETA23-PRINCIPAL-BAND-MULTISCALE-AND-MOLLIFIER-AUDIT-2026-08-12.md`;
2. `ZETA23-BERGMAN-SUPERCONDUCTOR-MOLLIFIER-AND-RECIPROCAL-JET-GATE-2026-08-12.md`;
3. `ZETA23-SIGNED-HEIGHT-FILTER-LAPLACE-CARRIER-GATE-2026-08-12.md`;
4. `ZETA23-XI-FOURIER-KERNEL-STRIP-NOGO-2026-08-12.md`.

The displayed identities and exponent arithmetic used by their main theorems
check.  None supplies the fixed-power signed estimate at its final endpoint.
No combination of the four reports proves a fixed uniform zero-free strip or
improves the known unconditional zero-free region.

## 1. Principal-band and multiscale audit

For

```text
F_(r,a)(x)=M(x)-r^a M(x/r),
```

the Mellin calculation is exact:

```text
integral_1^infinity F_(r,a)(x)x^(-s-1)dx
 =[1-r^(a-s)]/[s zeta(s)].
```

An energy bound

```text
integral_X^(2X)|F_(r,a)(x)|^2dx << X^(1+2q)
```

on every sufficiently large dyadic block makes the integral locally uniformly
convergent in `Re(s)>q`.  It therefore excludes precisely those zeros not
cancelled by the finite multiplier.  For `a=0` the multiplier is zero-free in
`Re(s)>0`; for `a=1` its zeros lie on `Re(s)=1`, where the classical theorem
already excludes zeta zeros.  Thus

```text
integral_X^(2X)|M(x)-2M(x/2)|^2dx << X^2.98
```

really would exclude `Re(rho)>0.99`, but the report does not prove this bound.

The odd-block identities also check:

```text
M(x)=O(x)-O(x/2),
M(x)-2M(x/2)=O(x)-3O(x/2)+2O(x/4),
```

and their Mellin multiplier reduces to `1-2^(1-s)`.  The finite-prime
recompletion

```text
M=product_(p in P)(I-S_p)G_P
```

restores exactly the Euler factors removed from the `P`-free sum; it does not
produce a better reciprocal-zeta remainder.  The local-parity counterexample
has `X^3` energy with the stated signs, so its scoped no-go conclusion is
valid.

The independent principal-band target also has the stated exponent:

```text
H=X^(49/50), eta=1/49
   => X H^(2-eta)=X^2.94,
```

and the exact ANOVA endpoint bound then gives `M(X)<<X^0.99`.  This is a
strip-strength target, not a proof of it.

## 2. Bergman mollifier audit

The area detector is valid.  A zero with `beta>=0.99` in the ordinate window
places a radius-`0.001` disc inside the stated rectangle, and
`1-zeta(rho)M(rho)=1`.  Subharmonic mean value therefore forces area norm at
least `pi*10^(-6)` independently of the mollifier coefficients.

For `theta=1.03`, `X=T^theta`, and `sigma_-=0.989`, independent recalculation
gives the report's powers:

```text
first Euler--Maclaurin correction       T^(-0.95468+o(1));
endpoint correction                     T^(-1.01468+o(1));
k-th Bernoulli correction               T^(-0.95468-0.12k+o(1));
K=9 remainder                           T^(-0.03468+o(1));
polynomial diagonal                     T^(-0.00734+o(1));
generic offdiagonal wall                X^(0.044+o(1))
                                      = T^(0.04532+o(1)).
```

The finite product coefficients are also exact:

```text
c_X(n)=sum_(d|n, d<=X, n/d<=X)mu(d),
c_X(1)=1, c_X(n)=0 (2<=n<=X), |c_X(n)|<=tau(n).
```

For distinct primes `p,q in [X/2,X]`, only the central divisors `p,q`
contribute, so `c_X(pq)=-2`.  There are `gg X^2/log^2 X` such semiprimes.
Putting them into `O(T)` bins of length `X^2/(100T)` gives

```text
gg X^4/[T log^4 X]
```

close semiprime pairs.  On these pairs `Re B_(m,n) gg T` and integration over
the first `1/log X` of the sigma interval gives

```text
A_(m,n) gg X^(-4sigma_-)/log X.
```

Hence this one same-sign block has absolute kernel mass

```text
gg X^[4(1-sigma_-)]/log^5 X = X^0.044/log^5 X.
```

This verifies the absolute-value obstruction.  It is not a lower bound for
the complete signed offdiagonal, as the report correctly emphasizes.

The reciprocal-jet calculation also checks.  Stirling converts the ordinary
Dirichlet mean-value error with weight `n` into Taylor radius `a-1`, yielding
only `beta<=1`.  Replacing that weight by `n^(1-eta)` would enlarge the radius
to `a-1+eta/2` and prove `beta<=1-eta/2`; no such replacement is proved.

## 3. Signed height-filter audit

The separated-node theorem is correct.  On normalized Lebesgue measure over
`[H,3H]`, the exponential Gram matrix satisfies

```text
|G_(j,k)| <= 1/[H|u_j-u_k|],
sum_(k!=j)|G_(j,k)|
 <= 2[1+log(M+1)]/(H delta) <= 1/2.
```

Thus `spec(G)` lies in `[1/2,3/2]`; taking `c=G^(-1)e_0` gives the desired
interpolation values and `L2` norm at most `sqrt(2)`, hence total variation at
most `sqrt(2)`.  Distinct integer logarithms in a fixed multiplicative window
are separated by `gg1/Y`.  Choosing the cross centre to be the logarithm of a
nearby half-integer, before constructing the filter, also separates every
node from zero by `gg1/Y`.  Therefore `H=O(Y log Y)=o(X)` for `Y=X^d`, `d<1`.

This theorem normalizes only point evaluation `q(0)`.  It does not normalize
the selected carrier

```text
L_alpha(q)=sum_k h_k b(xi_k).
```

For a fixed-width `C_c^infinity` lobe, `b(xi)=O_A(|xi|^-A)`, so the constructed
high-frequency measure has superpolynomially small carrier.  With bounded
variation it still loses `O(1/H)`.  This is the decisive obstruction and is
correctly stated in the report.

The two-leg factorization cost also checks:

```text
inf_(h_k=conj(ell_k)r_k)||ell||_2||r||_2=sum_k|h_k|.
```

Consequently the carrier-normalized problem returns to the Wiener quotient
extremal `E_Y`.  The desired lower bound for `E_Y` is not supplied, and even
such a bound is an adapter inside the larger completed-form argument rather
than by itself a zero-free-strip theorem.

## 4. Xi-kernel countermodel audit

The countermodel is valid and correctly scoped away from the actual Riemann
theta kernel.  For `r=kL>L`, the three-shift Gaussian mixture is strictly
log-concave.  The tail factor

```text
q(u)=exp{-2pi[cosh(4u)-1-8u^2]}
```

is positive and log-concave because

```text
(log q)''=-32pi[cosh(4u)-1]<=0.
```

It also gives `log h_L(u)=-pi exp(4|u|)+O_L(u^2)`.  In scaled variables the
unperturbed transform is

```text
2C_k exp(k^2w^2/2)[cosh(w)+cosh(a_0L)]
```

with zeros `w=+-a_0L+i(2m+1)pi`.  The subtraction of the quadratic Taylor
term in `q` makes the transform perturbation `O(L^4)`, whereas around
`w=i*pi+Lz` the root term is

```text
(L^2/2)(a_0^2-z^2)+O(L^4).
```

Rouche therefore gives `z_L -> +-a_0` and zeros

```text
s_L=i*pi/L+z_L.
```

This proves only that positivity, evenness, strict log-concavity, the leading
Xi tail, and finite qualitative shape data do not imply a horizontal strip.
It neither models the exact theta arithmetic nor constructs a zeta zero.
The `PF_infinity` discussion is properly scoped: translation total positivity
of all orders would make the bilateral transform zero-free in its convergence
strip, and hence is already false for the actual Xi kernel, which has known
transform zeros.  `PF_2` is only log-concavity and is covered by the explicit
countermodel.

## 5. Narrowest sufficient open estimate

Of the endpoints in this iteration, the Bergman formulation is the narrowest
single sufficient estimate because all of its analytic completion and diagonal
terms are already power-saved.  With `X=floor(T^1.03)`, define

```text
O_T=sum_(m!=n)c_X(m)c_X(n)A_(m,n)B_(m,n).
```

The one remaining theorem is

```text
O_T=o(1)                                               (5.1)
```

uniformly on dyadic heights.  It is a signed assertion: the positive
semiprime subblock above is much larger than one and must cancel against the
other central-divisor layers.  Proving (5.1) would make the full Bergman norm
`o(1)`, contradict the fixed area cost of any zero with `beta>=0.99`, and
hence prove the requested fixed strip.  No estimate in the four audited
reports proves (5.1).

The cleanest alternative sufficient endpoint is

```text
integral_X^(2X)|M(x)-2M(x/2)|^2dx << X^2.98,
```

but it is another global fixed-power Mobius estimate.  The Xi report supplies
a search-space pruning theorem, and the signed-height report supplies an
interpolation theorem with the wrong normalization; neither combines with the
two sufficient endpoints to remove their signed arithmetic hypothesis.

## Final verdict

```text
explicit delta>0 proved                         NO
known zero-free region improved                 NO
new exact sufficient reductions                YES
new scoped no-go/countermodel theorems          YES
fatal circularity in a claimed strip proof      N/A -- no strip is claimed
remaining issue                                 signed fixed-power arithmetic
```

The mathematically correct iteration outcome is therefore a sharper frontier,
not a zero-free-strip theorem.
