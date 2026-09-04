# Fixed periodic masks force a signed carrier edge

Status: exact fixed-period theorem in the sharp coefficient model,
2026-08-11.  This closes the signed-isolation step for the pure `k=7`
periodic mask, and more generally for every nontrivial mask of fixed minimal
period at least three.  It does not treat growing periods or aperiodic zero
ordinates, and it does not prove a zero-free strip.

## 1. Verdict

Use the coefficient `ell^2` norm and the exact `1/L^2` zero-form
normalization.  Put

```text
h=2*pi/L,       P=L/7,       X=exp(L).
```

For the pure `k=7` pair lattice of common depth `alpha`, let `H_(7,J)` be
the form of the pairs retained in the finite carrier `J_D`, and let `P_on`
be any positive on-line evaluation form whose total point multiplicity is
at most `C*d`, for a fixed `C`.  Assume the endpoint-jet and collar regime
of the core-sublattice report, so in particular

```text
m/d=o(1),                 ||H_out|V_m||=o(1).
```

If `alpha>=delta>0`, then, uniformly in the lattice offset and in the
locations of the on-line atoms,

```text
lambda_min((H_(7,J)+P_on)|V_m)
 <= -(2*cos(pi/7)/49+o(1))*X^(6*alpha/7).             (1.1)
```

The `o(1)` in the coefficient in (1.1) is uniform for
`delta<=alpha<1/2`.  In particular, for all sufficiently large `T`,

```text
K=-lambda_min((H_(7,J)+P_on)|V_m)
 >= c_7*X^(6*alpha/7),                                (1.2)
```

where any fixed `c_7<2*cos(pi/7)/49` is valid.  Together with the previously
proved norm upper bound,

```text
K <= (26/7+o(1))*X^(6*alpha/7),                       (1.3)
```

this determines the exact carrier **power** of the pure `k=7` model.
Since (1.2) is in the exact `1/L^2` normalization, it is stronger than the
weakened display `K>=X^(6*alpha/7-o(1))/L`.

The mechanism is elementary.  Coefficient indices in one residue class
modulo seven diagonalize all thirteen Poisson aliases simultaneously.  One
of the seven residue classes makes the top alias `q=6` negative.  The first
`m=o(d)` endpoint jets cannot remove that whole class, and a count-bounded
positive filler has only `O(d)` trace, whereas screening this negative
subspace would cost order `d*X^(6*alpha/7)` trace.

## 2. Exact normalized Poisson form

Index the sharp coordinates by `0<=k<d`, with

```text
tau_k=tau_0+k*h,       omega_k=tau_k-tau_c,
p_c(t)=sum_k c_k*exp(-i*omega_k*t).
```

For one occupied residue `b modulo 7`, the infinite pair lattice is

```text
gamma_j=tau_c+beta+(b+7*j)*h,       j in Z.
```

Its exact normalized signed form is

```text
Q_7(c)
 = (2/(7*L))*Re sum_(q=-6)^6
       exp(2*pi*i*b*q/7)
       *exp((alpha+i*beta)*q*P)*I_q(c),               (2.1)

I_q(c)=integral p_c(t)*p_c(q*P-t)dt.                  (2.2)
```

The integral in (2.2) is over

```text
J_q=[-L/2,L/2] intersection [q*P-L/2,q*P+L/2],
```

which has center `q*P/2` and length

```text
ell_q=L-|q|*P=(7-|q|)*L/7.                            (2.3)
```

The prefactor in (2.1) is exactly

```text
(2/L^2)*(L/7)=2/(7*L):
```

`2/L^2` is the contribution of one reflected pair and `L/7` is the
Poisson covolume.  Thus no hidden factor of `L` is discarded below.

## 3. Simultaneous alias diagonalization

For `r in {0,...,6}`, let

```text
U_r={c: c_k=0 unless k=r (mod 7)}.                    (3.1)
```

Here and below an empty initial residue is represented by its first index
in `[0,d)`.  If `k,l` belong to the same residue class and `k-l=7*n`, then

```text
integral_(J_q) exp(-i*(omega_k-omega_l)*t)dt
 = phase * 2*sin(pi*n*(7-|q|))/(omega_k-omega_l)
 = 0                                                   (3.2)
```

for `n!=0`.  On the diagonal the integral is `ell_q`.  Moreover,

```text
exp(-i*omega_(r+7*n)*q*P)=exp(-i*omega_r*q*P).         (3.3)
```

Expanding (2.2) and using (3.2)--(3.3) proves the exact identity

```text
I_q(c)=ell_q*exp(-i*omega_r*q*P)*||c||_2^2,
                  c in U_r.                           (3.4)
```

Thus the full infinite-lattice form is scalar on each `U_r`:

```text
Q_7(c)=lambda_r*||c||_2^2,                            (3.5)

lambda_r=(2/7)*Re sum_(q=-6)^6
  (1-|q|/7)*exp(alpha*q*P)
  *exp(i*q*((beta-omega_r)*P+2*pi*b/7)).              (3.6)
```

This is the missing signed calculation: the other aliases cannot cancel in
an uncontrolled way on `U_r`; they are explicit scalars there.

## 4. The top alias has a negative residue class

The `q=6` part of (3.6) is

```text
(2/49)*X^(6*alpha/7)*cos(theta_r),                    (4.1)
```

where, as `r` runs through the seven residue classes, `theta_r` runs through
seven angles separated by `2*pi/7`.  One of them is within `pi/7` of `pi`.
Choose that residue, denoted `r_*`.  Then

```text
cos(theta_(r_*)) <= -cos(pi/7).                       (4.2)
```

All remaining positive aliases have `q<=5`, while the negative aliases
have exponentially decaying hyperbolic weights.  Uniformly for
`alpha>=delta`,

```text
lambda_(r_*)
 <= -(2*cos(pi/7)/49)*X^(6*alpha/7)
       +O_delta(X^(5*alpha/7))
 = -(2*cos(pi/7)/49+o(1))*X^(6*alpha/7).              (4.3)
```

In particular, the entire space `U_(r_*)`, not just one specially tuned
vector, is a top-scale negative subspace for the complete alias sum.

## 5. Endpoint jets and positive fillers do not screen the edge

Let

```text
W=U_(r_*) intersection V_m.
```

Since `V_m` has codimension `m` in the `d`-dimensional coefficient space,

```text
dim W >= dim U_(r_*)-m
      >= floor(d/7)-m
       = (1/7-o(1))*d.                                (5.1)
```

This is the quantitative endpoint-jet accessibility statement.  Combining
(4.3) with the finite-carrier tail estimate gives, for every `c in W`,

```text
c^T*H_(7,J)*c
 <= -(2*cos(pi/7)/49+o(1))*X^(6*alpha/7)*||c||_2^2.  (5.2)
```

It remains to audit the on-line positive form.  For a real ordinate
`gamma`, let `e_gamma(c)=F_c(gamma)`.  The full cardinal-sine identity gives

```text
||e_gamma||_2^2/L^2
 <= sum_(k in Z) sinc((gamma-tau_0)*L/(2*pi)-k)^2
 = 1.                                                 (5.3)
```

Therefore an on-line atom of multiplicity `M_gamma`, whose exact normalized
matrix is

```text
(M_gamma/L^2)*e_gamma^T*e_gamma,
```

has trace at most `M_gamma`.  If the total on-line multiplicity is at most
`C*d`, then

```text
Tr(P_on)<=C*d.                                        (5.4)
```

Let `Pi_W` be the orthogonal projection onto `W`.  Positivity and (5.4)
give

```text
Tr(Pi_W*P_on*Pi_W)<=C*d.
```

Consequently some unit vector `c_* in W` satisfies

```text
c_*^T*P_on*c_* <= C*d/dim W=7*C+o(1).                (5.5)
```

Equations (5.2) and (5.5) prove (1.1).  Notice that neither separation of
the on-line ordinates nor a lower interpolation singular value is used.
Only their actual point-multiplicity budget enters.

In fact the trace argument gives more than one Rayleigh vector.  Let
`a_7<2*cos(pi/7)/49` be fixed.  The number of eigenvalues of
`Pi_W*P_on*Pi_W` exceeding `(a_7/2)*X^(6*alpha/7)` is at most

```text
(2*C*d/a_7)*X^(-6*alpha/7)=o(d).                     (5.6)
```

On the orthogonal complement of those filler directions, (5.2) makes the
total form at most `-(a_7/2)*X^(6*alpha/7)`.  Thus a
`(1/7-o(1))*d`-dimensional top-scale negative subspace survives.  Screening
the periodic edge would require polynomially more positive trace than the
zero-count budget permits.

## 6. An explicit endpoint-jet packet at the reflected fixed point

The dimension argument in Section 5 is sufficient, but the accessibility
can also be seen directly.  Let `k_0` be the first index in the selected
residue class and suppose `k_0+7*m<d`.  Define real coefficients

```text
c_(k_0+7*j)=binom(m,j)/sqrt(binom(2*m,m)),   0<=j<=m,
c_k=0 otherwise.                                      (6.1)
```

Then `||c||_2=1` and

```text
p_c(t)=exp(-i*omega_(k_0)*t)
       *(1+exp(-i*7*h*t))^m/sqrt(binom(2*m,m)).        (6.2)
```

At both endpoints `t=+-L/2`, the factor in parentheses vanishes to order
`m`, so `c in V_m`.  Its modulus is periodic with period `P=L/7` and, in
the cell centered at `j*P`, obeys

```text
|p_c(j*P+u)|^2
 = 4^m*cos(7*pi*u/L)^(2*m)/binom(2*m,m),
                  |u|<=P/2.                           (6.3)
```

Thus it is a Gaussian-scale packet train of width `P/sqrt(m)`.  The `q=6`
overlap is the single cell

```text
J_6=[5*L/14,L/2],
```

whose reflection fixed point is `3*L/7=3*P`; (6.3) has a packet centered
exactly there.  Formula (3.4) shows that its reflected product has the phase
selected in (4.2), while every lower alias is already included in (4.3).
This gives an explicit packet realization of the negative top alias.  The
high-dimensional trace argument, rather than this one packet alone, makes
the conclusion robust against an adversarial on-line filler.

## 7. General fixed periodic masks

The same calculation closes the fixed-period version of the missing
implication.  Let `B` be a nonempty proper mask of fixed minimal period
`M>=3`, put

```text
A_q=sum_(b in B) exp(2*pi*i*b*q/M),
q_*=max{1<=q<=M-1: A_q!=0},
N_*=M/gcd(M,q_*).
```

On the coefficient residue space `U_r={k=r (mod M)}`, the exact analogue of
(3.4) is

```text
I_q(c)=L*(1-|q|/M)*exp(-i*omega_r*q*L/M)*||c||_2^2.  (7.1)
```

The `q_*` phases sampled by the `M` residue classes form a regular
`N_*`-gon.  Minimality of `M>=3` implies `N_*>=3`.  Indeed, `N_*=2` would
force `q_*=M/2`; maximality and conjugation would then make every Fourier
coefficient of `1_B` vanish except those at `0` and `M/2`, so `1_B` would
depend only on parity and the mask would have period at most two.

Hence some residue class has top-alias cosine at most
`-cos(pi/N_*)`.  All higher aliases vanish by definition and all lower ones
lose at least the fixed power `X^(-alpha/M)`.  Repeating Sections 4--5 gives

```text
-lambda_min((H_(B,J)+P_on)|V_m)
 >= c(B,M,delta)*X^(alpha*q_*/M),                     (7.2)
```

for a positive constant `c(B,M,delta)` and every count-bounded on-line
filler.  The Newton power-sum lemma gives

```text
q_*>=M-#B,                                            (7.3)
```

so (7.2) proves, for every fixed periodic mask of minimal period at least
three, the candidate exponent

```text
alpha*q_*/M >= alpha*(1-#B/M).                        (7.4)
```

Thus the high-alias statement really does imply a signed lower edge in the
fixed-period setting.  The unresolved cases are not fixed periodic masks:
they are growing periods, aperiodic ordinates, depth variation, and the
transfer of any resulting reduced carrier scale through the prime side.
No zero-free-strip conclusion follows from this theorem alone.
