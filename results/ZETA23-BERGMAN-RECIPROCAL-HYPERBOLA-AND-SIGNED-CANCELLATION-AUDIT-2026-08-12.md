# Bergman reciprocal hyperbola and signed-cancellation audit

Status: exact recompletion and obstruction theorem, 2026-08-12.  This note
attacks the sole open term in
`ZETA23-BERGMAN-SUPERCONDUCTOR-MOLLIFIER-AND-RECIPROCAL-JET-GATE-2026-08-12.md`.
It does not prove a zero-free strip.

The main advance is that the apparent `n asymp X^2` obstruction is not the
primitive one.  The part of the *unweighted* factor above the analytic
conductor can be completed by Euler--Maclaurin with a power saving, even
after multiplication by the full sharp Mobius polynomial.  What remains is
an exact reciprocal hyperbola.  Its coefficient sequence has a solid block
equal to `-1`; consequently its diagonal grows, and the desired theorem
requires a negative offdiagonal main term of the same size.  Poisson or
Voronoi summation does not turn that main term into an error: its complete
set of reciprocal modes reconstructs `zeta`, while its zero-frequency
component is a logarithmic Mertens tail.

```text
high--high product range n asymp X^2                 PRUNED
exact remaining form                                 reciprocal hyperbola
coefficient on T<n<=2T                               identically -1
diagonal of recompleted form                         >=T^0.022/log T
required signed offdiagonal                          same size, negative
Perron dual                                           zeta(s)/zeta(s+w)
physical dual                                         signed Mertens tail
fixed power saving                                    OPEN
uniform zero-free strip                               NOT PROVED
```

## 1. Notation

Retain the parameters of the Bergman report:

```text
sigma_-=0.989,       sigma_+=1.001,
Omega_T=[sigma_-,sigma_+] x [T-r,2T+r],
theta=1.03,          X=floor(T^theta),

D_Z(s)=sum_(m<=Z)m^(-s),
M_X(s)=sum_(d<=X)mu(d)d^(-s),
F_X(s)=D_X(s)M_X(s)-1.                                (1.1)
```

The preceding report proves

```text
norm_(L2(Omega_T))((zeta-D_X)M_X)=o(1),              (1.2)
```

and reduces its proposed strip proof to

```text
norm_(L2(Omega_T))(F_X)=o(1).                         (1.3)
```

We now recomplete `D_X` down to the conductor.

## 2. The unweighted super-conductor tail is harmless

Put `Y=floor(T)`.  Uniformly for `s=sigma+it` in `Omega_T`,

```text
D_X(s)-D_Y(s)
 =[X^(1-s)-Y^(1-s)]/(1-s)+O(T^(-sigma) log^C T).     (2.1)
```

The logarithm is inessential and can be removed with a more careful
endpoint convention.  Here is a direct uniform proof.  Apply
Euler--Maclaurin to `u^(-s)` between `Y` and `X`, retaining `2K` derivatives
with `K=C_0 log T`.  On this box,

```text
(|t|+2K)/(2*pi*Y) <=1/pi+o(1)<1.                     (2.2)
```

The Bernoulli estimate

```text
|B_(2K)|/(2K)! <=2*zeta(2K)/(2*pi)^(2K)              (2.3)
```

makes the remainder at most

```text
T^(1-sigma) [(|t|+2K)/(2*pi*Y)]^(2K),                (2.4)
```

which is smaller than any prescribed power after increasing `C_0`.
Every retained lower endpoint term is

```text
O(T^(-sigma)(|t|/(2*pi*T))^j),                       (2.5)
```

and these form a convergent geometric sum.  The upper endpoint is easier
because `|t|/X=T^(-0.03+o(1))`.  This proves (2.1), including all endpoint
and Bernoulli terms.  Equivalently, Poisson summation has no stationary
nonzero frequency on `m>=T`, since `|t|/(2*pi*m)<=1/pi+o(1)`.

The trivial bound needed here is only

```text
|M_X(s)| <<X^(1-sigma_-)*log X=T^(0.01133+o(1)).     (2.6)
```

The integral term in (2.1), after multiplication by `M_X`, is therefore

```text
O(T^[-1+2*theta*(1-sigma_-)+o(1)])
 =O(T^(-0.97734+o(1))),                              (2.7)
```

and the endpoint error is `O(T^(-0.97767+o(1)))`.
Squaring and integrating over a box of ordinate length `T` gives

```text
norm_(L2(Omega_T))^2((D_X-D_Y)M_X)
 <<T^[-1+4*theta*(1-sigma_-)+o(1)]
 =T^(-0.95468+o(1))=o(1).                            (2.8)
```

Thus we have proved the following exact reduction.

**Theorem 2.1 (conductor recompletion).**  With

```text
G_(T,X)(s)=D_Y(s)M_X(s)-1,                           (2.9)
```

one has

```text
norm_(L2(Omega_T))(F_X-G_(T,X))=o(1).                (2.10)
```

This also holds at the level of squared norms, with an additive `o(1)`.
Indeed, the coefficient-blind mean-value bound gives

```text
norm(F_X) <<T^(0.02266+o(1)),
norm(G_(T,X)) <<T^(0.02233+o(1)),                    (2.11)
```

whereas (2.8) gives `norm(F_X-G_(T,X))<<T^(-0.47734+o(1))`.
Cauchy--Schwarz therefore yields

```text
norm(F_X)^2=norm(G_(T,X))^2+o(1).                   (2.12)
```

In particular, (1.3) holds if and only if

```text
norm_(L2(Omega_T))(G_(T,X))=o(1).                    (2.13)
```

This removes the original same-sign semiprimes with both primes near `X`
as a *primitive* obstruction.  Their large absolute kernel mass cancels
inside the nonstationary Euler--Maclaurin completion.  The obstruction
reappears at the conductor boundary, as the next sections make exact.

## 3. Exact reciprocal-hyperbola form

Write

```text
G_(T,X)(s)=sum_(n>Y)b_(T,X)(n)n^(-s).                (3.1)
```

Since `mu*1=delta`, its coefficients are exactly

```text
b_(T,X)(n)
 =sum_(d|n; d<=X; n/d<=Y)mu(d),                     (3.2)
```

for `n>1`, and they vanish for `n<=Y`.  Equivalently,

```text
G_(T,X)(s)
 =sum_(m<=Y)m^(-s) sum_(Y/m<d<=X)mu(d)d^(-s).       (3.3)
```

Equation (3.3) is the promised reciprocal hyperbola.  It retains the full
sign of every Mobius coefficient; no absolute value has been taken.

For `Y<n<=X`, complete divisor cancellation also gives

```text
b_(T,X)(n)=-sum_(d|n; d<n/Y)mu(d).                  (3.4)
```

For `X<n<=XY`, the two missing sides of the divisor hyperbola give

```text
b_(T,X)(n)
 =-sum_(d|n; d<n/Y)mu(d)-sum_(d|n; d>X)mu(d).       (3.5)
```

The two sums in (3.5) have disjoint ranges.  These identities show exactly
where a hyperbola or divisor-switching proof must use Mobius cancellation.

## 4. A solid `-1` block and a growing diagonal

For all sufficiently large `T`, `X>2Y`.  If

```text
Y<n<=2Y,                                             (4.1)
```

then the condition `n/d<=Y` excludes only the divisor `d=1` from the
complete divisor sum.  Hence

```text
b_(T,X)(n)=-1                 (Y<n<=2Y).             (4.2)
```

This is stronger than a sparse same-sign example: the recompleted
coefficient sequence is identically negative on a full conductor-length
interval.

Let `Delta_G` denote the diagonal in the exact area norm of `G_(T,X)`.
From (4.2),

```text
Delta_G
 >=(T+O(1)) sum_(Y<n<=2Y)
      [n^(-2sigma_-)-n^(-2sigma_+)]/(2log n)
 >>T^(2-2sigma_-)/log T
 =T^0.022/log T.                                    (4.3)
```

It follows that a proof of (2.13) must establish

```text
OffDiag_G=-Delta_G+o(1),                             (4.4)
```

and in particular must produce a negative offdiagonal contribution of
size at least `T^0.022/log T`.  An offdiagonal theorem stated merely as an
error smaller than the diagonal cannot work.  The original form `F_X` had
an `o(1)` diagonal because its coefficient deletion continued through
`X`; conductor recompletion moves that deletion into the signed
offdiagonal cancellation (4.4).

This also explains why completing the high product range is not itself a
proof: it converts a large absolute wall into an explicit large signed
main-term identity.

## 5. The absolute wall survives at the reciprocal boundary

There is an exact mixed-semiprime version of the earlier obstruction.  Let

```text
p in [X/2,X],       q in [Y/2,Y]                     (5.1)
```

be primes.  Since `p>Y`, the only admissible representation of `pq` in
(3.2) is `d=p,m=q`, and therefore

```text
b_(T,X)(pq)=-1.                                      (5.2)
```

There are `>>XY/(log X log Y)` distinct such products.  Partition their
range into `O(T)` intervals of length `XY/(100T) asymp X`.  The same
Cauchy--Schwarz and positive-kernel argument as in the original report
produces an absolute same-sign contribution

```text
>>(XY)^[2(1-sigma_-)]/log^5 T
 =T^[2*(theta+1)*(1-sigma_-)+o(1)]
 =T^(0.04466+o(1)).                                  (5.3)
```

Again, (5.3) is not a lower bound for the full signed norm.  It proves that
the cancellation required by (4.4) must also cancel a fixed-power family
of mixed near-products.  Rowwise estimates, coefficient squares, and
absolute shifted-convolution estimates are excluded.

## 6. What Poisson and shifted convolution actually return

In a smooth version of the area norm, the ordinate integral gives a kernel

```text
T*hat(w)(T log(d_1*m_1/(d_2*m_2))).                  (6.1)
```

Thus its physical shifted-convolution range is

```text
|d_1*m_1-d_2*m_2| << d_1*m_1/T.                     (6.2)
```

On the discarded range `m>T`, Poisson has no stationary nonzero frequency;
this is precisely Theorem 2.1.  On `m<=T`, the stationary points

```text
m=t/(2*pi*k),       k>=1,                            (6.3)
```

are present.  Keeping all of them reconstructs the usual reciprocal
transform, hence the zeta functional equation.  Dropping them is false;
taking their absolute values restores the power in (5.3).

The continuous dual term can be read without asymptotics.  Replacing an
unweighted `m`-sum by its integral and putting `u=dm` changes

```text
mu(d)d^(-s)m^(-s)dm
```

into

```text
mu(d)/d * u^(-s)du.                                  (6.4)
```

Consequently every zero-frequency hyperbola term contains signed sums of
the form

```text
sum_(aX<d<bX)mu(d)/d                                 (6.5)
```

or their endpoint-weighted variants.  The identity `1/zeta(1)=0` predicts
their cancellation, but a fixed-power rate for (6.5) is a fixed-power
Mertens estimate.  The nonzero reciprocal modes do not remove this
primitive: together with (6.5), they recomplete the original reciprocal
zeta factor.

The same obstruction is visible if one starts with the shifted equation
instead of Poisson summation.  In the mixed range `d asymp X`, `m asymp T`,
(6.2) has additive width `X`.  For a fixed `m`, this restricts `d` to an
interval of length

```text
X/T=T^0.03=X^(0.029126...).                           (6.6)
```

A delta-method or character decomposition controls the nonprincipal
characters by its large-sieve part, but its principal character is the
signed Mobius sum on precisely these intervals.  Deleting that character
deletes the cancellation needed in (4.4); retaining it leaves an
unproved fixed-power short-interval Mertens estimate.  Voronoi summation
on the unweighted `m` variable has the same outcome: the Kloosterman modes
are transformed, while the principal Mobius mode remains.

Real-part averaging supplies the positive weight

```text
[(n_1*n_2)^(-sigma_-)-(n_1*n_2)^(-sigma_+)]
 /log(n_1*n_2).                                      (6.7)
```

It gives the logarithm in (4.3), but it gives no oscillatory sign and no
power saving.  In particular, sigma averaging cannot pay either exponent
`0.022` or `0.04466`.

## 7. Exact Perron and Mertens duals

The analytic primitive can be stated with no heuristic.  Put

```text
X_*=X+1/2,
```

so that the Perron cutoff does not pass through an integer.  Initially for
`Re(s)>1` and a Perron line to the right of every singularity,

```text
M_X(s)
 =1/(2*pi*i) integral_((c)) X_*^w/[w*zeta(s+w)] dw.  (7.1)
```

Therefore

```text
zeta(s)M_X(s)-1
 =1/(2*pi*i) integral_((c))
      X_*^w/w * zeta(s)/zeta(s+w) dw -1.             (7.2)
```

When `zeta(s)!=0`, the pole at `w=0` has residue one and cancels the final
term.  At a zeta zero, this point collides with the denominator-zero
singularity described below, so that cancellation cannot be invoked
uniformly across the putative zero.  For `zeta(s)!=0`, moving the contour a
fixed distance to the left encounters poles

```text
w=rho-s                                                (7.3)
```

from zeros `rho` of zeta.  Thus a residue-free fixed-power contour shift is
literally a fixed zero-free strip.  Indenting around (7.3) retains the
single-zero contribution detected by the Bergman disc; it does not create
a smaller error.

The same primitive in physical space is obtained by partial summation.  If

```text
M(u)=sum_(n<=u)mu(n),                                  (7.4)
```

then, initially in `Re(s)>1`,

```text
zeta(s)M_X(s)-1
 =zeta(s) [M(X)X^(-s)
            -s integral_X^infinity M(u)u^(-s-1)du].  (7.5)
```

Equation (7.5) must be kept signed: the boundary term and integral can
cancel.  Continuing it with a fixed power into `Re(s)<1`, or bounding its
complete signed value at the scale required by (2.13), is a
Mertens/reciprocal-zeta theorem of strip strength.  Classical
subexponential PNT cancellation and logarithmic almost-all short-interval
estimates do not pay the fixed powers in (4.3) and (5.3).

Finally, (1.2) and Theorem 2.1 give

```text
G_(T,X)(s)=zeta(s)M_X(s)-1+o_(L2(Omega_T))(1).        (7.6)
```

Thus the hyperbola form (3.3), the reciprocal ratio (7.2), and the Mertens
tail (7.5) are three exact coordinates on the same remaining signed mode.

## 8. Verdict

The conductor recompletion is a genuine pruning result: no further effort
should be spent trying to control the `n asymp X^2` semiprimes separately.
Their absolute mass cancels inside a rigorously small nonstationary tail.

The surviving theorem is sharper than the phrase "bound the
offdiagonal" suggests.  In the reciprocal-hyperbola coordinates it asks
for a negative offdiagonal main term which cancels a growing diagonal,
including the full block `b(n)=-1` on `(T,2T]` and the mixed-semiprime wall
(5.3).  Hyperbola switching, Euler--Maclaurin, Poisson, reciprocity, and
sigma averaging have all been exhausted up to the exact primitive:

```text
sum_(m<=T)m^(-s) sum_(T/m<d<=X)mu(d)d^(-s),          (8.1)
```

or equivalently the complete signed Mertens tail (7.5).  No known
coefficient-blind or absolute-value estimate supplies its required fixed
saving.  Proving that saving would prove the requested strip; it has not
been proved in this audit.
