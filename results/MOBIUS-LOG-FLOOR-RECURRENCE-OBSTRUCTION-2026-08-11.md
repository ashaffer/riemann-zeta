# Mobius--log / Mertens floor-recurrence obstruction

Status: focused coefficient audit, 2026-08-11.  No fixed zero-free strip is
proved.  The new statements below are elementary exact theorems within the
project audit; no literature-priority claim is made.

## 1. Verdict

The recompleted coefficient and the reciprocal Mertens recurrence do not
give two independent opportunities for a fixed power saving.  They are
joined by an exact triangular identity.

Put

```text
C=mu*Lambda=-mu log,
S_C(N)=sum_(n<=N) C(n),
R(N)=psi(N)-N.
```

Then

```text
S_C(N)-1
 =sum_(k<=N)mu(k)R(floor(N/k)).                       (1.1)
```

Thus the centered ordinary-dual coefficient is the inverse Mobius floor
transform of the prime-number-theorem error.  This is an identity, not an
estimate.  It retains every zeta-zero pole.

There are three sharp consequences.

1. `S_C` and the Mertens function have the same power-growth exponent; the
   passage from `mu` to `-mu log` changes only one logarithm.
2. The inverse operator in (1.1), and even its off-identity part, has no
   `L1(nu) -> weak-Lq(nu)` bound for any `q>1`, even on reciprocal-mean-zero
   inputs.  Hence no bootstrap based only on such an operator bound,
   reciprocal centering, and a size or tail norm for `R` can be obtained by
   applying the inverse floor transform.
3. Conversely, any weak-`Lq`, `q>1`, estimate for the actual `S_C` already
   implies a pointwise fixed power saving and hence a fixed zero-free
   half-plane.  The logarithmic increments of `S_C` spread a large spike far
   enough for the R136 argument to apply.

The best unconditional input remains Vinogradov--Korobov sized.  A fixed
power in (1.1), in the smooth Mobius--log polynomial, or in the complete
ordinary dual would be the desired strip theorem itself.

## 2. The exact floor-transform algebra

For an arithmetic function `a` and a function `f` on the nonnegative
integers with `f(0)=0`, define

```text
(T_a f)(N)=sum_(k<=N)a(k)f(floor(N/k)).               (2.1)
```

### Theorem 2.1 (floor-transform semigroup)

For finitely supported inputs, and pointwise whenever the displayed sums
are finite,

```text
T_a T_b=T_(a*b).                                     (2.2)
```

If `F_b(N)=sum_(n<=N)b(n)`, then

```text
T_a F_b(N)=sum_(m<=N)(a*b)(m).                       (2.3)
```

#### Proof

The elementary floor identity

```text
floor(floor(N/k)/ell)=floor(N/(k ell))
```

groups the double sum by `m=k ell` and proves (2.2).  Also

```text
sum_(k<=N)a(k)sum_(n<=N/k)b(n)
 =sum_(kn<=N)a(k)b(n),
```

which is (2.3).  QED.

Let `1` denote the constant arithmetic function and `epsilon` the Dirichlet
identity.  Since

```text
C*1=Lambda,       mu*1=epsilon,                      (2.4)
```

(2.3) gives the first exact recurrence

```text
T_1 S_C=psi.                                         (2.5)
```

The cumulative function of `epsilon` is the constant function one on the
positive integers, and `T_1 1=N`.  Define

```text
E_C(0)=0,
E_C(N)=S_C(N)-1       (N>=1).                        (2.6)
```

Then one has

```text
T_1 E_C=R.                                           (2.7)
```

Applying `T_mu` and using (2.2) proves the promised inverse recurrence

```text
E_C=T_mu R,
S_C(N)-1=sum_(k<=N)mu(k)
                  [psi(floor(N/k))-floor(N/k)].      (2.8)
```

Equivalently, at coefficient level,

```text
C-epsilon=mu*(Lambda-1).                             (2.9)
```

This is the exact meeting point of the R128 ordinary-dual route and the R136
floor-recurrence route.

## 3. Centering does not remove the zero carrier

Put `A(s)=1/zeta(s)`.  In `Re(s)>1`, and then meromorphically,

```text
sum_n (C(n)-epsilon(n))n^(-s)
 =A'(s)-1
 =A(s)[-zeta'(s)/zeta(s)-zeta(s)].                   (3.1)
```

If `rho` is a zeta zero of multiplicity `j`, then locally

```text
A(s)=(s-rho)^(-j)h(s),       h(rho)!=0,
```

so `A'(s)-1` has a pole of order `j+1`.  The subtraction makes the already
holomorphic `A'` vanish at `s=1`, equivalently removing its reciprocal mean;
it does not weaken a nontrivial-zero pole.

There is nevertheless exact reciprocal centering.  With

```text
nu({N})=1/[N(N+1)],
```

Vinogradov--Korobov decay justifies passage to the limit in the finite
summation-by-parts identity and gives

```text
sum_(N>=1) E_C(N)/[N(N+1)]
 =sum_(n>=1)(C(n)-epsilon(n))/n
 =A'(1)-1=0.                                         (3.2)
```

Here `A(s)=(s-1)+O((s-1)^2)`, so `A'(1)=1`.  Thus (2.8)
already lies in the globally centered reciprocal framework; the missing
input is not another rank-one centering.

## 4. Passing from `mu` to `-mu log` preserves the power exponent

Let

```text
M(x)=sum_(n<=x)mu(n).
```

Stieltjes summation gives, exactly for real `x>=2`,

```text
S_C(x)=-M(x)log x+integral_1^x M(t)dt/t,             (4.1)

M(x)=1-S_C(x)/log x
       -integral_2^x S_C(t)dt/[t(log t)^2].          (4.2)
```

The second formula is just partial summation after dividing the coefficient
`mu(n)log n` by `log n`; the lower boundary is zero because the `n=1`
logarithmic coefficient vanishes.

Consequently, for every fixed `theta>0`,

```text
M(x)<<x^theta(log x)^B
       => S_C(x)<<x^theta(log x)^(B+1),              (4.3)

S_C(x)<<x^theta(log x)^B
       => M(x)<<1+x^theta(log x)^(B-1).              (4.4)
```

In particular,

```text
limsup_(x->infinity) log(2+abs M(x))/log x
 =limsup_(x->infinity) log(2+abs S_C(x))/log x.       (4.5)
```

The same identities hold after any fixed Mellin modulation.  Namely, put

```text
M_tau(x)=sum_(n<=x)mu(n)n^(i tau),
S_(C,tau)(x)=sum_(n<=x)C(n)n^(i tau),
```

and replace `M,S_C` by `M_tau,S_(C,tau)` in (4.1)--(4.2).
Thus differentiating the reciprocal-zeta coefficients does not create a
power gain in the low Mellin modes used by R120/R128.

## 5. The inverse Mobius floor operator has no higher-tail gain

The coefficient `mu(k)` in (2.8) might appear to improve the centered
operator obstruction of R136.  It does not do so at the level of an operator
estimate.

### Theorem 5.1 (weak-type obstruction)

For every `q>1`, neither

```text
T_mu
```

nor its off-contact part

```text
T_mu-I=sum_(k>=2)mu(k)D_k                            (5.1)
```

maps mean-zero `L1(nu)` to weak-`Lq(nu)`.  The failure occurs on finitely
supported integer-valued inputs of `L1(nu)` norm one.  It is unchanged by
subtracting any rank-one output proportional to the reciprocal mean.

#### Proof

For `N>=4`, set

```text
f_N(1)=-1,
f_N(N)=N(N+1)/2,
f_N(m)=0 otherwise.                                  (5.2)
```

Then

```text
integral f_N dnu=0,       norm(f_N)_L1(nu)=1.         (5.3)
```

At the output point `N`, only `k=1` reaches the input point `N`, while
`floor(N/k)=1` for `N/2<k<=N`.  Hence

```text
(T_mu f_N)(N)
 =N(N+1)/2-sum_(N/2<k<=N)mu(k),
abs(T_mu f_N(N))>>N^2.                               (5.4)
```

This conclusion uses only `abs(mu(k))<=1`, not cancellation in a Mertens
sum.

The identity contact can also be removed.  At the output point `2N`, the
only `k>=2` with `floor(2N/k)=N` is `k=2`, and
`floor(2N/k)=1` exactly when `N<k<=2N`.  Since `mu(2)=-1`,

```text
((T_mu-I)f_N)(2N)
 =-N(N+1)/2-sum_(N<k<=2N)mu(k),
abs((T_mu-I)f_N(2N))>>N^2.                           (5.5)
```

Take `U` to be a sufficiently small fixed multiple of `N^2`.  The one
output atom in (5.4), or in (5.5), gives

```text
U^q nu(abs(T f_N)>U)>>N^(2q-2),                      (5.6)
```

which diverges for every `q>1`.  The inputs in (5.2) have zero reciprocal
mean, so a rank-one mean correction vanishes on them.  QED.

Theorem 5.1 does not show that the particular input `R` in (2.8) has a large
tail.  It proves the precise no-go statement: a proof cannot combine only a
norm or tail estimate for `R`, reciprocal centering, and boundedness of the
inverse floor kernel.  It must exploit cancellation in the actual joint
sequence

```text
mu(k)R(floor(N/k)).                                  (5.7)
```

That joint cancellation is already a Mobius/prime-error theorem.

## 6. Weak tails for the actual Mobius--log sum are strip-strength

There is also no cheaper weak-tail endpoint on the output side.

### Theorem 6.1 (logarithmic spike spreading)

Suppose that, for some `q>0` and all `U>0`,

```text
nu(abs(S_C)>U)<=K U^(-q).                            (6.1)
```

Then

```text
abs S_C(N)<<_q (1+K)^(1/(q+1))
                    [N^2 log(2N)]^(1/(q+1)).         (6.2)
```

In particular, every `q>1` in (6.1) gives a pointwise bound

```text
S_C(N)<<N^theta(log N)^(1/(q+1)),
theta=2/(q+1)<1,                                     (6.3)
```

and therefore a fixed zero-free half-plane for zeta.

#### Proof

Let `H=abs S_C(N)`.  Since

```text
abs[S_C(n)-S_C(n-1)]=abs C(n)<=log n,                (6.4)
```

a backward interval of length comparable to `H/log(2N)` has
`abs S_C(n)>H/2`.  The trivial bound `H<=N log N` keeps this interval inside
`[1,N]`; bounded `H/log(2N)` is absorbed in the constant.  Telescoping the
reciprocal weights on that interval gives

```text
nu(abs(S_C)>H/2)>>H/[N^2 log(2N)].                   (6.5)
```

Combining (6.5) with (6.1) proves (6.2).

If `q>1`, summation by parts makes

```text
sum_n C(n)n^(-s)=A'(s)
```

holomorphic in `Re(s)>theta`.  But a zeta zero there would give the pole of
Section 3.  Hence no such zero exists.  QED.

This is the exact Mobius--log analogue of R136's unit-increment theorem.
The logarithm in (6.4) costs only the displayed logarithmic factor, not a
power.

## 7. Recompletion is exactly the prime field

For every finitely supported test function `f`, (2.4) also gives

```text
sum_q C(q)sum_m f(qm)
 =sum_n f(n)sum_(q|n)C(q)
 =sum_n Lambda(n)f(n).                               (7.1)
```

Thus the scalar inside R128's completed square is exactly the prime field:

```text
sum_q C(q)sum_m f_R(qm)=sum_n Lambda(n)f_R(n).        (7.2)
```

After the recorded center subtraction and detector normalization, the
complete ordinary dual is the original prime-discrepancy energy.  Unfolding
`C` as `mu*Lambda`, or refolding it by (7.1), cannot by itself supply an
upper bound.

For a fixed smooth dyadic weight,

```text
B_(X,w)(tau)
 =sum_n C(n)n^(-1/2+i tau)w(n/X),                    (7.3)
```

the Vinogradov--Korobov/explicit Mertens bound gives, uniformly on fixed
`tau` intervals,

```text
B_(X,w)(tau)
 <<X^(1/2)exp{-c(log X)^(3/5)(loglog X)^(-1/5)}.      (7.4)
```

The corresponding complete energy is only `X^(1-o(1))`.  See
Lee--Leong, *New explicit bounds for the Mertens function*, Theorem 1.2,
<https://arxiv.org/abs/2208.06141>, and Bellotti's current PNT transfer,
<https://arxiv.org/abs/2508.02041>.

Finally, for a compactly supported smooth `w`, define

```text
what_w(s)=integral_0^infinity w(x)x^(s-1)dx.
```

The Mellin-transform identity, initially in `Re(s)>1`, is

```text
integral_0^infinity [sum_n C(n)w(n/Y)]
       Y^(-s)dY/Y
 =what_w(s)A'(s).                                    (7.5)
```

A fixed-power estimate for a finite bank whose Mellin transforms have no
common zero continues `A'` locally throughout a fixed half-plane: at each
point choose a bank member whose transform is nonzero, and patch the local
quotients.  It therefore excludes all zeta zeros there.  This is why a
fixed-power version of (7.4), or

```text
O_full(X)<<X^(1-delta),       delta>0,                (7.6)
```

cannot be imported as an auxiliary bilinear estimate: it is already the
fixed-strip theorem.

## 8. Surviving target

The two candidate coefficient routes now have one common endpoint:

```text
prime error R
  -- exact inverse T_mu --> centered Mobius--log sum E_C
  -- smooth Mellin bank --> complete ordinary-dual energy.
```

The generic operator step has no higher-tail gain (Theorem 5.1), and a
higher tail for the actual output is already strip-strength (Theorem 6.1).
The only surviving arithmetic possibility is a new, sign-sensitive estimate
for (5.7), uniform through the complete modulation/dilation bank and strong
enough to give a fixed power.  No such estimate is proved here or in the
checked primary literature.
