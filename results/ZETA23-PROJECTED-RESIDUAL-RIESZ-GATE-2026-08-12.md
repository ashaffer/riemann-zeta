# A raw Riesz margin does not survive the target projection

Status: exact projection-loss identity, projected-Riesz exceptional-space
theorem, and sharp floor-preserving countermodel, 2026-08-12.  The
countermodel is structural: it does not use the actual von Mangoldt
coefficients or the Cauchy relation between the selected rows.  It rules out
a deduction from the raw `1-2/e` margin, codimension, and a spectral floor
alone.  No actual arithmetic counterexample and no zero-free strip is proved.

## 1. Binary verdict

Let `Q` be the endpoint-jet projection, let

```text
b=Q*x/||Q*x||,
P=Q-b*b^*,                 S=range(P),              (1.1)
```

and let `a in S` be the unit selected negative carrier.  For the uncompressed
completed matrix `K_0`, put

```text
<a,K_0*a>=-r<0,            K=P*K_0*P|S.             (1.2)
```

The quadratic Lanczos moment is

```text
m_2=||K*a||^2=||P*K_0*a||^2.                        (1.3)
```

There is an exact orthogonal loss ledger:

```text
m_2
 =||K_0*a||^2
  -||(I-Q)*K_0*a||^2
  -abs(<b,K_0*a>)^2.                                (1.4)
```

The only part which no admissibility projection can erase is the carrier
component itself:

```text
m_2=r^2+||P_(S intersect a^perp)*K_0*a||^2>=r^2.    (1.5)
```

This lower bound is sharp even if the uncompressed energy is arbitrarily
large, the raw atom family is orthonormal (hence has Riesz margin `1`), and
the spectral floor `K_0>=-M*I` is sharp.  In particular, for every
`0<r<M` there are nondegenerate examples with

```text
||K_0*a||^2 arbitrarily large,
m_2<r*M,
K>=-M*I,
max spectrum(K)<0.                                  (1.6)
```

Thus the lower large-sieve margin cannot prove `m_2>=r*M` unless one also
proves a **target-conditioned angle bound** excluding `K_0*a` from the
endpoint/selected defect space.  Codimension shows that only a few
coefficient directions can be lost; it gives no protection for this one
specified direction.

There is also an earlier mismatch.  The existing `1-2/e+o(1)` theorem is a
lower Riesz bound for separated point-translate columns (and an adjoined
half-integer point column).  The completed Fourier--Laplace carrier is a
weighted integral of such columns, and `K_0*a` includes background--prime
cancellation.  The point-column theorem is not, by itself, an uncompressed
lower bound for that completed residual.

## 2. Exact endpoint and selected-row loss

### Theorem 2.1 (target residual ledger)

Let `H` be a finite-dimensional Hilbert space, let `Q` be an orthogonal
projection, and let `b` be a unit vector in `range(Q)`.  Put

```text
P=Q-b*b^*.
```

Let `a` be a unit vector in `range(P)`, let `K_0=K_0^*`, and suppose
`<a,K_0*a>=-r` with `r>0`.  Then

```text
||P*K_0*a||^2
 =||K_0*a||^2-||(I-Q)*K_0*a||^2-abs(<b,K_0*a>)^2,  (2.1)

||P*K_0*a||^2
 =r^2+||P_(range(P) intersect a^perp)*K_0*a||^2.   (2.2)
```

Consequently, for any `M>=r`,

```text
||P*K_0*a||^2>=r*M

iff

||P_(range(P) intersect a^perp)*K_0*a||^2
   >=r*(M-r).                                       (2.3)
```

At carrier fraction `theta=8/9`, the two quadratic hypotheses in the
spectral-floor Lanczos lemma are together equivalent to

```text
||P_(range(P) intersect a^perp)*K_0*a||^2
   >=max{r*(M-r),8*r^2}.                             (2.4)
```

#### Proof

The ranges of `I-Q`, `b*b^*`, and `P` are mutually orthogonal and their
projections sum to the identity.  Pythagoras applied to `K_0*a` proves
(2.1).  Since `P*a=a`,

```text
<a,P*K_0*a>=<a,K_0*a>=-r.
```

Decomposing `P*K_0*a` along `C*a` and its orthogonal complement proves
(2.2).  Subtracting `r^2` proves (2.3), and the condition
`m_2>=9*r^2` similarly becomes a transverse lower bound of `8*r^2`, proving
(2.4).  QED

Equation (2.1) pins down the two losses requested by the actual construction:

```text
endpoint loss =||(I-Q)*K_0*a||^2,
selected loss =abs(<Q*x,K_0*a>)^2/||Q*x||^2.        (2.5)
```

Neither term is controlled by the fact that `a` itself lies in `S`.
Hermiticity only rewrites the selected loss as
`abs(<K_0*Q*x,a>)^2/||Q*x||^2`; it supplies no small factor.

## 3. What a projected Riesz theorem actually says

The rank loss can be described exactly after whitening the raw Gram matrix.

### Theorem 3.1 (projected-Riesz exceptional space)

Let `V:C^N -> H` satisfy

```text
G=V^*V>=gamma*I,             gamma>0,               (3.1)
```

and let `P` be an orthogonal projection whose complementary projection
`D=I-P` has rank at most `q`.  Define

```text
U=V*G^(-1/2),
Lambda=U^*D*U.                                      (3.2)
```

Then

```text
0<=Lambda<=I,
rank(Lambda)<=q,
trace(Lambda)<=q,                                   (3.3)
```

and, for every coefficient vector `c`, with `h=G^(1/2)c`,

```text
||P*V*c||^2=<h,(I-Lambda)h>,
||V*c||^2=||h||^2.                                  (3.4)
```

In particular, if

```text
ell_P(c)=<h,Lambda*h>/||h||^2                       (3.5)
```

for `c!=0`, then exactly

```text
||P*V*c||^2=(1-ell_P(c))*||V*c||^2
            >=gamma*(1-ell_P(c))*||c||^2.           (3.6)
```

There is a subspace of whitened coefficient dimension at least `N-q` on
which no energy is lost.  Nevertheless no positive lower bound for (3.6)
holds for a specified `c`: `ell_P(c)=1` is possible, already for an
orthonormal family.

#### Proof

Equation (3.1) makes `G` invertible, and `U^*U=I`.  Hence
`0<=U^*D*U<=I`.  Rank cannot increase under multiplication, and cyclicity of
trace gives

```text
trace(Lambda)=trace(D*U*U^*)<=trace(D)<=q,
```

because `U*U^*` is an orthogonal projection.  Since `V=U*G^(1/2)`, (3.4)
follows immediately.  Equations (3.5)--(3.6) follow by division.  Finally,
`dim ker(Lambda)>=N-q`.  Sharpness is obtained from `V=I` and a nonzero
vector in `range(D)`.  QED

For `m` endpoint jets plus the selected positive row, `q<=m+1`.  The theorem
therefore proves a useful but target-free statement: all loss is concentrated
in a whitened atomic coefficient subspace of dimension at most `m+1`.
The completed coefficient vector associated with `K_0*a` may have its whole
mass in precisely that exceptional subspace.  Trace, rank, and average
leverage do not bound its value in (3.5).

## 4. Sharp floor-preserving countermodel

### Theorem 4.1 (arbitrary raw energy, failed projected residual)

Fix real numbers

```text
0<r<M,
0<t^2<r*(M-r),
q>=0.                                               (4.1)
```

Let `a,w,b` be orthonormal, put `S=span{a,w}`, and let `P` be the orthogonal
projection onto `S`.  Define

```text
v=sqrt(M-r)*a
  +t/sqrt(M-r)*w
  +q/sqrt(M-r)*b,

K_0=-M*I+v*v^*.                                     (4.2)
```

Then

```text
K_0>=-M*I,
<a,K_0*a>=-r,
K_0*a=-r*a+t*w+q*b,                                 (4.3)

||K_0*a||^2=r^2+t^2+q^2,
||P*K_0*a||^2=r^2+t^2<r*M.                          (4.4)
```

Moreover the compressed operator `K=P*K_0*P|S` has eigenvalues

```text
-M,
-r+t^2/(M-r)<0.                                    (4.5)
```

Thus the first Lanczos plane is nondegenerate (`t!=0`) but contains no
nonnegative vector.  Sending `q` to infinity makes the raw energy arbitrarily
large without changing the projected moment.

#### Proof

The identity `K_0+M*I=v*v^*>=0` proves the floor.  Since
`<v,a>=sqrt(M-r)`, multiplication gives (4.3), hence (4.4).  On `S`,

```text
K=-M*I_S+v_S*v_S^*,
v_S=sqrt(M-r)*a+t/sqrt(M-r)*w.
```

This rank-one perturbation has eigenvalues `-M` and

```text
-M+||v_S||^2=-r+t^2/(M-r),
```

which is negative by (4.1).  QED

Take `Q=I` and choose the normalized selected positive row to be `b`.  Then
the entire `q*b` term in (4.3) is removed by the selected-row projection.
Alternatively, put `b` in the endpoint-defect space to realize the same
loss at the endpoint stage.  Taking the raw synthesis `V=I` gives Riesz
margin `1`, strictly stronger than `1-2/e`.  Hence even a perfect raw frame,
an arbitrarily large raw norm, codimension one, and a sharp spectral floor
do not force (2.3).

The strict inequality in (4.1) is also exact.  As
`t^2` increases to `r(M-r)`, the second eigenvalue in (4.5) increases to
zero and the projected moment increases to `r*M`.  Thus `r*M` is the sharp
boundary in this structural class.

## 5. Arithmetic scope and the remaining theorem

The countermodel proves an implication impossible:

```text
raw Riesz margin
+ small endpoint/selected codimension
+ spectral floor
+ large uncompressed ||K_0*a||

does NOT imply

||P*K_0*a||^2>=r*M.                                 (5.1)
```

It does **not** show that the actual completed zeta matrix realizes the
alignment in (4.2).  Its selected row is an abstract vector, not necessarily
the real part of the same Cauchy evaluation whose imaginary part produces
`a`; its rank-one update is not asserted to be a von-Mangoldt Loewner
matrix.  Therefore this is a fail-fast theorem about the proposed proof
inputs, not an actual-coefficient falsification.

For the actual matrix, the quadratic escape is now equivalent to the single
target-conditioned estimate

```text
||P_(S intersect a^perp)*K_0*a||^2>=r*(M-r),        (5.2)
```

or to the stronger eight-ninths version (2.4).  An atomic proof of (5.2)
must control the leverage (3.5) of the **specific completed coefficient
vector**, including prime--continuum cancellation, against the endpoint and
selected Cauchy rows.  This is an orientation/correlation theorem, not a
lower large-sieve theorem.

Accordingly, the quadratic reformulation remains exact and potentially
useful, but it is no easier from the presently proved raw Riesz margin.  A
new actual-coefficient input must couple the completed Loewner action
`K_0*a` to the target geometry; dimension and separated-node energy cannot
supply that coupling.
