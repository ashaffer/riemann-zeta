# Centered one-square machine/SOS discovery card

**Date:** 2026-08-13

**Verdict:** **no candidate-conditioned SOS identity was found.  The positive
finite scans do not support a prime-separable or finite-head symbolic proof.
Two exact obstructions explain why: independent-prime SOS loses the common
height phase, and a prescribed candidate zero imposes no algebraic condition
on any finite von Mangoldt head unless a nonlocal tail/completion term is
retained.  No arithmetic lower edge or strip is proved.**

This card uses the exact centered formula and matrix implementation in
`centered_even_cosine_gate.py` and `high_height_carrier_slice.py`.  The new
probe is `centered_one_square_sos_overfit_probe.py`.

## 1. What the symbolic search actually sees

For the unprojected sinh-tent carrier, the prime part is exactly

```text
sum_(p^k<=X) (log p)/sqrt(p^k) C(log(p^k))
                    cos(k*gamma*log p),                    (1.1)
```

and the finite Hahn-projected carrier has the same form with an explicitly
computed autocorrelation coefficient in place of `C`.  Thus, with
`theta_p=gamma log p`, the prime contribution is

```text
sum_(p<=X) P_p(theta_p),                                  (1.2)
```

where every `P_p` is a one-variable real trigonometric polynomial.  This is
the only genuinely sparse decomposition supplied by prime-power support.

If the prime phases are treated independently, then exactly

```text
min_((theta_p)_p in torus) sum_p P_p(theta_p)
   =sum_p min_theta P_p(theta).                            (1.3)
```

Each one-variable lower bound in (1.3) has a Fejer--Riesz/SOS certificate.
Therefore (1.3) is the strongest possible certificate in the proof class
which uses prime-local SOS blocks but does not retain the common-height
relation `theta_p=gamma log p` or another cross-prime constraint.

There is also an exact global-height interpretation.  The numbers `log p`
for distinct primes are linearly independent over the rationals, so
Kronecker's theorem makes the orbit

```text
gamma -> (gamma*log p mod 2*pi)_(p<=X)                    (1.4)
```

dense in the finite prime torus.  Hence the infimum over all real `gamma` of
the **prime part alone** equals the right side of (1.3).  This does not say
that a bounded dyadic height interval explores the torus, and it does not
include the `gamma`-dependent archimedean background.  It confirms that the
separable envelope is not an artificial global prime-only obstruction.

The machine stress test used the actual von Mangoldt coefficients, centered
odd carrier, aperture `.2`, even jet order `2`, depth `.49`, and
`gamma=1.5X`.  It included the exact archimedean/pole background and the
`2*pi/log X` completion:

| `X` | dimension | actual shifted square | independent-phase lower envelope |
|---:|---:|---:|---:|
| 32 | 7 | 2.4375 | 1.7632 |
| 48 | 11 | 1.7753 | 1.2913 |
| 64 | 17 | 2.1450 | .9552 |
| 96 | 27 | 2.1109 | .5267 |
| 128 | 39 | 1.9284 | .1792 |
| 256 | 91 | 2.2474 | **-.6205** |
| 512 | 203 | 2.0363 | **-1.5577** |

These are floating diagnostics.  The negative margins use sampled phase
values, so the exact torus minima can only be smaller; an interval replay of
the coefficients would certify the two displayed failures if needed.  The
conclusion is already structural: the observed positivity uses coherent
cross-prime phases.  Prime-by-prime diagonal dominance, convolution squares,
or separate Fejer factors cannot explain it.

## 2. The sparse matrix identity is Loewner, not positive

There is an exact rank-two displacement identity, but it supplies no sign.
Put

```text
E_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+it)
       -integral_1^X v^(-1/2+it)dv,
A(t)=Im E_X(t),       R(t)=Re E_X(t),       L=log X.       (2.1)
```

Let `L_A` be the confluent Loewner matrix on nodes `tau_i`:

```text
(L_A)_(ij)=(A(tau_i)-A(tau_j))/(tau_i-tau_j),  i!=j,
(L_A)_(ii)=A'(tau_i).                                  (2.2)
```

Direct differentiation of (2.1), or inspection of the exact implementation,
gives the centered arithmetic matrix

```text
H_E=2*L_A-2*L*diag(R(tau_i)).                            (2.3)
```

Consequently, for `D=diag(tau_i)`,

```text
[D,H_E]=2*(A*1^T-1*A^T),       rank([D,H_E])<=2.          (2.4)
```

This is a real symbolic compression: the dense matrix has displacement rank
two.  It does **not** move the lower edge.  Loewner positivity would require
an operator-monotone/Pick property of the oscillatory actual function `A`,
while the diagonal correction in (2.3) changes sign with `R`.  The rigorous
negative evenized-multiplier example already rules out the corresponding
pointwise Herglotz shortcut.  A Cholesky or generic PSD fit to the scanned
matrices hides the nonlocal cross-prime cancellation rather than identifying
an arithmetic SOS.

## 3. Finite-head nonidentifiability of the candidate relation

The candidate equation cannot be inserted into a finite von Mangoldt
regression as one extra scalar feature.  The following elementary theorem
gives the obstruction.

### Proposition 3.1 (a candidate quartet can be placed beyond any head)

Fix `X`, a point `rho=beta+i*gamma`, and a prime `q>X`.  Define

```text
F_(rho,q)(s)=(1-q^(rho-s))*(1-q^(conj(rho)-s)).             (3.1)
```

Then:

1. `F_(rho,q)` has real Dirichlet-polynomial coefficients and vanishes at
   `rho` and `conj(rho)`;
2. on a right half-plane, `F'/F` has a Dirichlet expansion supported only on
   `q^k`, `k>=1`; hence multiplying a Dirichlet object by `F` changes no
   logarithmic-derivative coefficient indexed by `2<=n<=X`;
3. `F(s)F(1-s)` is real-symmetric and invariant under `s -> 1-s`, and inserts
   the full quartet `rho,conj(rho),1-rho,1-conj(rho)` (with the evident
   coincidences/multiplicities, and together with the harmless vertical
   aliases of this exponential-polynomial model) while retaining that same
   finite right-hand von Mangoldt head.

For completeness, put `ell=log q`.  On `Re(s)>beta`,

```text
F'(s)/F(s)=ell*sum_(k>=1)
 [q^(k*rho)+q^(k*conj(rho))]q^(-k*s).                  (3.2)
```

For the symmetric product `G(s)=F(s)F(1-s)`, factor

```text
F(1-s)=q^(2*s+rho+conj(rho)-2)
       (1-q^(1-rho-s))(1-q^(1-conj(rho)-s)).             (3.3)
```

Hence, on `Re(s)>max(beta,1-beta)`,

```text
G'(s)/G(s)=2*ell+ell*sum_(k>=1)
 [q^(k*rho)+q^(k*conj(rho))
  +q^(k*(1-rho))+q^(k*(1-conj(rho)))]q^(-k*s).           (3.4)
```

All nonconstant Dirichlet terms are supported on `q^k>X`, and the constant
`2*ell` is an exponential/completion term rather than a coefficient indexed
by `n>=2`.  This proves the claimed head preservation and also displays why
the reflected factor belongs to the nonlocal completion.

Therefore the data

```text
{Lambda(n):n<=X} + formal convolution identities among that head
```

do not acquire any new algebraic relation merely from the assertion that a
completed object has a zero at `rho`.  Any valid candidate-conditioned proof
must also retain a global Euler/functional-equation remainder which detects
the factor in Proposition 3.1.  Once that remainder is retained, the problem
is no longer a sparse finite-head SOS fit; it is the original explicit-formula
gate.

This proposition is a structural countermodel, not an Euler-product
counterexample to zeta.  It scopes the machine search: zeta-specific success
must use its exact nonlocal completion, not only its actual finite head and a
zero label.

## 4. Why the positive scans cannot train the missing implication

The matrix fixtures explicitly record

```text
candidate_is_asserted_zero = False.                              (4.1)
```

Their positivity is valuable falsification data, but none is a sample from
the conditional population `zeta(rho)=0` with `Re rho>1/2`.  There are no
known positive or negative training examples in that population.  Spectral
feature regression can consequently learn the large smooth archimedean
background, finite-height phase cancellation, or matrix dimension; it cannot
identify how the hypothetical-zero relation changes the lower edge.

The existing scan corpus varies `X`, aperture, jet order, and depth, but it
contains no candidate-zero labels on which to train a conditional
decomposition.  In the present exact-feature search the only
low-complexity identities were the two-abscissa scalar already known, the
prime-local split (1.2), and the Loewner displacement (2.3)--(2.4).  The
first is the open gate; the second loses cross-prime coherence; the third
has no sign.

## 5. Decision

```text
actual prime-power one-variable decomposition       EXACT;
prime-separable Fejer/SOS lower edge                 FAILS finite stress test;
centered Loewner/displacement-rank identity          EXACT, SIGNLESS;
candidate relation from finite Lambda head alone     IMPOSSIBLE structurally;
nonlocal candidate-conditioned arithmetic identity  NOT FOUND;
uniform centered one-square lower edge               NOT PROVED;
uniform zero-free strip                              NOT PROVED.          (5.1)
```

The right next search, if this branch is ever reopened, is not a larger PSD
regression.  It is a proof-carrying symbolic ansatz that includes an exact
approximate-functional-equation remainder coupling composite monomials
across primes.  Without that nonlocal term, finite positivity is overfitting.
