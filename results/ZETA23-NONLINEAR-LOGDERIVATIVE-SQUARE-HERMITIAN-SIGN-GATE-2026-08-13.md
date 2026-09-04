# Log-derivative square: local residue and global Hermitian sign gate

**Date:** 2026-08-13

**Verdict:** multiplying `(zeta'/zeta)^2` by a holomorphic test `H` with
`H(rho)=0` does isolate the clean local residue

```text
m_rho^2 H'(rho).                                      (0.1)
```

It does not give a globally signed completed explicit formula.  At every
other zero the residue contains the regular Laurent germ `a_rho`, and after
completion those germs are pairwise interactions with all other zeros.
Reflection symmetrization has an exact parity dichotomy:

* a symmetric/Hermitian test, the one compatible with a real boundary
  weight, cancels the reflected residue pair, including the desired signal;
* an antisymmetric test retains the selected derivative signal but also
  retains `4m a_rho H(rho)` at every unselected pair and has no positive
  Hermitian boundary weight.

The identity

```text
L^2=zeta''/zeta-L'                                    (0.2)
```

makes the collapse explicit.  At a selected simple zero, `H(rho)=0` kills
the `zeta''/zeta` residue, and the entire residue (0.1) comes from the
linear derivative term `-H L'`, or after contour integration by parts from
`H' L`.  Other zeros retain the signed quotient-germ debt.

The boundary-positive completion does not repair this.  On the critical
line, for `X=xi'/xi`, one has `|X|^2=-X^2`.  Its local integral has a
positive contact `pi m^2 h(gamma)/sigma`; a nonnegative `h` which kills the
contact at `gamma` necessarily has `h'(gamma)=0`, so it cannot extract the
holomorphic derivative residue.  Subtracting the contact or polarizing to
extract an oriented first derivative loses positivity and restores the
regular-germ/cross-term debt.  Positive polarizations may retain the contact
and detect pole blowup, but that is not the finite `H'(rho)` detector and
bounding it across a strip is already the zero-free problem.

Thus the positive `Lambda*Lambda` semiprime coefficients are only one
uncompleted piece.  Gamma--prime cross terms and pairwise zero terms have
both signs.  No completed Hermitian sign theorem results.

No zero-free strip is claimed.

---

## 1. Exact Laurent residue

Write near a zero `rho` of multiplicity `m`

```text
L(s)=zeta'(s)/zeta(s)
    =m/(s-rho)+a_rho+O(s-rho).                        (1.1)
```

Then

```text
L(s)^2=m^2/(s-rho)^2+2m a_rho/(s-rho)+O(1),          (1.2)
```

and hence

```text
Res_(s=rho) H(s)L(s)^2
 =m^2 H'(rho)+2m a_rho H(rho).                        (1.3)
```

The proposed local cancellation is correct: if `H(rho)=0`, (1.3) reduces
to `m^2H'(rho)`.  A global contour sums (1.3) over every enclosed zero; it
does not impose `H=0` at the other zeros.

---

## 2. Completion exposes the reflected pair debt

Put

```text
X(s)=xi'(s)/xi(s).                                    (2.1)
```

The functional equation gives

```text
X(1-s)=-X(s).                                         (2.2)
```

If

```text
X(s)=m/(s-rho)+a_rho+O(s-rho),                        (2.3)
```

then at the reflected zero `rho*=1-rho`,

```text
a_(rho*)=-a_rho.                                      (2.4)
```

The sum of the two residues is therefore exactly

```text
m^2[H'(rho)+H'(1-rho)]
 +2m a_rho[H(rho)-H(1-rho)].                         (2.5)
```

If `H(1-s)=H(s)`, then

```text
H'(1-rho)=-H'(rho),
H(1-rho)=H(rho),                                      (2.6)
```

so (2.5) is zero.  The Hermitian-even completion cancels both the debt and
the selected derivative signal.

If `H(1-s)=-H(s)`, then

```text
H'(1-rho)=H'(rho),
H(1-rho)=-H(rho),                                     (2.7)
```

and (2.5) becomes

```text
2m^2H'(rho)+4m a_rho H(rho).                          (2.8)
```

At the selected reflected pair, imposing `H=0` leaves a clean doubled
signal.  Every other pair retains the second term in (2.8).

This term is genuinely pairwise.  In a symmetrically regularized Hadamard
expansion, `a_rho` contains

```text
sum_(nu!=rho) m_nu/(rho-nu)                           (2.9)
```

plus fixed completion constants.  Summing the corresponding terms over
zeros and pairing `(rho,nu)` produces divided differences of the form

```text
[H(rho)-H(nu)]/(rho-nu).                              (2.10)
```

For complex zero quartets these have no fixed sign.  Reality after quartet
completion is not positivity.

---

## 3. The square collapses to a linear derivative plus quotient debt

For either `L=zeta'/zeta` or `X=xi'/xi`,

```text
L^2=zeta''/zeta-L',
X^2=xi''/xi-X'.                                      (3.1)
```

At a simple zero,

```text
zeta''(s)/zeta(s)=2a_rho/(s-rho)+O(1),
L'(s)=-1/(s-rho)^2+O(1).                             (3.2)
```

If `H(rho)=0`, the first expression in (3.2) becomes regular after
multiplication by `H`, while

```text
Res_(rho)[-H L']=H'(rho).                             (3.3)
```

On a closed contour, integration by parts gives

```text
integral H L^2
 =integral H(zeta''/zeta)+integral H' L.             (3.4)
```

Thus the selected simple-zero detector is linear after one integration by
parts.  At unselected zeros the first term in (3.4) contributes
`2a_rho H(rho)` and the second contributes `H'(rho)`, reproducing (1.3).

For multiplicity `m`, `zeta''/zeta` has double coefficient `m(m-1)` and
simple coefficient `2ma_rho`; together with `-L'` it reconstructs
`m^2H'(rho)+2ma_rho H(rho)`.  The nonlinear notation removes no global
term.

On the Dirichlet side,

```text
[-zeta'/zeta(s)]^2
 =sum_n (Lambda*Lambda)(n)n^(-s),                    (3.5)
```

with nonnegative convolution coefficients.  But completion writes
`X=A_infinity-zeta'/zeta`, so `X^2` also contains a signed prime--gamma
cross term and an archimedean square.  Identity (3.1) is the same
cancellation in analytic coordinates.  Keeping only (3.5) is not a
completed explicit formula.

---

## 4. Positive Hermitian energy retains contact, not the derivative

On `Re(s)=1/2`, equations (2.1)--(2.2) and conjugation imply that `X` is
purely imaginary, hence

```text
|X(1/2+it)|^2=-X(1/2+it)^2.                           (4.1)
```

Near a zero at height `gamma`, put `x=t-gamma` and evaluate on a horizontal
offset `sigma>0`:

```text
X=m/(sigma+i x)+a+O(sigma+i x).                       (4.2)
```

Then

```text
|X|^2
 =m^2/(sigma^2+x^2)
  +2m[sigma Re(a)-x Im(a)]/(sigma^2+x^2)+O(1).        (4.3)
```

For a smooth real weight `h`, the first term gives

```text
integral h(gamma+x)m^2/(sigma^2+x^2)dx
 =pi m^2 h(gamma)/sigma+finite_part.                  (4.4)
```

This contact is positive.  If `h>=0` and `h(gamma)=0`, differentiability at
the local minimum forces

```text
h'(gamma)=0.                                          (4.5)
```

So a positive Hermitian weight cannot both kill (4.4) and retain the
first-order datum corresponding to `H'(rho)`.

Subtracting the contact in (4.4) is an indefinite renormalization.  Its
finite part contains the two regular-germ terms in (4.3), including a
Hilbert-transform term from `x/(sigma^2+x^2)`, and has no fixed sign.

More generally, shifted polarizations form the positive-semidefinite
matrix

```text
K_(j,k)=integral h(t)X(sigma_j+it)
                         conjugate[X(sigma_k+it)]dt. (4.6)
```

Every positive combination of (4.6) is a squared modulus.  It either keeps
the pole contact, or cancels a whole repeated component and loses the
oriented first derivative.  Extracting an off-diagonal real/imaginary part,
a shift derivative, or a contact-subtracted finite part uses a difference
of positive squares and is indefinite.  Positive difference-square
variants can cancel a regular constant locally, but they still retain pole
contacts and do not realize the finite holomorphic residue (0.1).

Therefore polarization offers a valid positive **pole-blowup** detector,
not a positive finite-residue detector.  Proving it uniformly bounded in a
fixed open strip would already assert that the poles are absent there.

---

## 5. Decision

```text
selected local residue m^2 H'(rho):                         EXACT;
other-zero residue omits the regular Laurent germ:          FALSE;
completed symmetric test retains selected reflected signal: FALSE;
completed antisymmetric test removes other-zero debt:       FALSE;
L^2 supplies a genuinely nonlinear selected simple-zero term: FALSE;
Lambda*Lambda positivity survives full completion alone:    FALSE;
positive Hermitian energy has a pole contact:                EXACT;
nonnegative h kills contact but keeps h'(gamma)!=0:          FALSE;
centered/polarized finite residue stays positive:            FALSE;
nonlinear square yields a global signed exclusion theorem:   NOT PROVED;
uniform zeta zero-free strip:                                NOT PROVED.
```

The only clean nonlinear object is the positive contact itself.  Keeping it
does not isolate a finite selected residue; removing it destroys the sign.
The proposed `H(rho)=0` square therefore recreates the same pairwise signed
debt as the linear explicit formula.
