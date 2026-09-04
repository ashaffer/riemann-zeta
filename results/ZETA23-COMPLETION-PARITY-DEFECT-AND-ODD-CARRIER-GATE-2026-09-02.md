# Completion parity, the functional-equation defect, and the odd-carrier gate

Date: 2026-09-02  
Status: exact reflection and pole-ledger theorems; the proposed direct
completion-defect bridge is closed; **no uniform zero-free strip and no
proof of RH**

Passport:
[completion-parity preflight](context/zeta23_completion_parity_bridge_preflight_v1.json)

## 0. Outcome

The proposed roadmap step

\[
 \text{completed functional-equation defect}
 \longrightarrow
 \text{one-sided R68/R95 saving}
 \tag{0.1}
\]

fails at its first algebraic gate.

The completed defect measures failure of a divisor to occur in
functional-equation pairs.  A genuine zeta zero already occurs in such a
pair, so its contribution to the defect is zero.  More precisely:

1. the functional equation fixes the reflection-even component of the
   logarithmic derivative;
2. all paired nontrivial-zero poles lie in the reflection-odd component;
3. for zeta the defect vanishes identically, while the odd residual is
   exactly the original R95 transform and retains every zero pole with its
   original residue;
4. the complete R68 Type-II series has the same decomposition, because its
   Type-I complement is holomorphic at every nontrivial zero; and
5. imposing a functional equation by symmetrization preserves arbitrary
   reflected zero pairs.  What it destroys is the ordinary right-half-plane
   Euler/Dirichlet structure.

Thus the sparse surgery was excluded for the right reason but the proposed
repair targeted the wrong symmetry channel.  Exact completion is useful only
when coupled nonlinearly to the actual coefficients in the odd channel.
Merely penalizing or setting the completion defect to zero cannot improve an
exponent.

## 1. Licensed completion and reflection

Let \(F\) be a nonzero meromorphic function, initially represented on a
right half-plane by

\[
 -\frac{F'}F(s)=\sum_{n\ge2}\frac{\Lambda_F(n)}{n^s}.
 \tag{1.1}
\]

Suppose \(F\) has a pole of order \(r\) at \(s=1\).  Fix a completion

\[
 \Xi_F(s)=C_F(s)F(s)                                      \tag{1.2}
\]

*independently* of the divisor one is trying to exclude.  For a meromorphic
function \(G\), write

\[
 G^\#(s)=\overline{G(\overline{s})},\qquad
 ({\cal J}G)(s)=G^\#(1-s).                               \tag{1.3}
\]

On a real/self-dual class, \({\cal J}\) is the reflection across the
critical line written holomorphically.  Put

\[
 L_F=\frac{\Xi_F'}{\Xi_F},\qquad
 \kappa_F=\frac{C_F'}{C_F}.                              \tag{1.4}
\]

The completion is licensed only if \(C_F\) is prescribed before inspecting
the zeros.  Otherwise one can force a functional equation tautologically by
inserting reflected copies of \(F\).

## 2. The exact defect and its divisor ledger

Define

\[
 {\cal D}_F(s)=
 \frac{\Xi_F(s)}{\varepsilon_F\Xi_F^\#(1-s)},\qquad
 {\cal E}_F(s)=\frac{{\cal D}_F'}{{\cal D}_F}(s)
              =L_F(s)+({\cal J}L_F)(s),                  \tag{2.1}
\]

where \(\varepsilon_F\ne0\) is constant.  Also define the odd channel

\[
 {\cal O}_F(s)=L_F(s)-({\cal J}L_F)(s).                  \tag{2.2}
\]

### Theorem 2.1: completion-defect parity

On every connected component on which the quotient is defined:

1. \({\cal E}_F=0\) if and only if
   \(\Xi_F(s)=\varepsilon_F\Xi_F^\#(1-s)\) up to a constant
   normalization;
2. \({\cal E}_F\) is reflection-even and \({\cal O}_F\) is
   reflection-odd; and
3. if

   \[
    \nu(a)=\operatorname{ord}_a\Xi_F,\qquad
    \nu^\#(1-a)=\operatorname{ord}_{1-a}\Xi_F^\#,
   \]

   then

   \[
    \operatorname*{Res}_{s=a}{\cal E}_F
       =\nu(a)-\nu^\#(1-a),\qquad
    \operatorname*{Res}_{s=a}{\cal O}_F
       =\nu(a)+\nu^\#(1-a).                              \tag{2.3}
   \]

#### Proof

The logarithmic derivative of the denominator in (2.1) acquires a minus
sign from \(1-s\), which gives the displayed plus sign in \({\cal E}_F\).
Therefore \({\cal E}_F=(\log {\cal D}_F)'\), proving the first assertion.
Applying \({\cal J}\) interchanges the two summands in (2.1) and negates the
difference in (2.2).

At \(s=a\), \(L_F\) has residue \(\nu(a)\).  If \(L_F^\#\) has residue
\(\nu^\#(1-a)\) at \(1-a\), composition with \(1-s\) changes that residue to
\(-\nu^\#(1-a)\).  Taking the sum and difference proves (2.3).

Equation (2.3) is the decisive ledger.  The defect sees the *difference*
between reflected multiplicities.  The odd channel sees their *sum*.
Every correctly paired off-line quartet is invisible to the defect.

## 3. Exact R95 decomposition

For \(x\ge1\), define the generalized centered ramp

\[
 R_F(x)=\sum_{n\le x}\Lambda_F(n)\left(\frac{2n}{x}-1\right)
        -r(1-x^{-1}),                                    \tag{3.1}
\]

and put

\[
 H(s)=\frac{s-1}{s(s+1)}.                                \tag{3.2}
\]

On the initial Euler half-plane,

\[
 {\cal M}R_F(s)
 =H(s)\left\{-\frac{F'}F(s)-\frac{r}{s-1}\right\}.       \tag{3.3}
\]

Since \(-F'/F=\kappa_F-L_F\) and
\(L_F=({\cal E}_F+{\cal O}_F)/2\), one obtains the exact identity

\[
 \boxed{
 {\cal M}R_F(s)
 =-\frac{H(s)}2{\cal E}_F(s)
  +H(s)\left\{-\frac12{\cal O}_F(s)
                    +\kappa_F(s)-\frac{r}{s-1}\right\}.}
 \tag{3.4}
\]

No estimate has been used.

### Corollary 3.1: the zeta residual is the original target

For

\[
 C_\zeta(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
 \Xi_\zeta=\xi,
 \]

the functional equation and conjugation give
\({\cal E}_\zeta=0\).  Hence (3.4) reduces identically to

\[
 {\cal M}R_\zeta(s)
 =H(s)\left\{-\frac{\zeta'}{\zeta}(s)-\frac1{s-1}\right\}.
 \tag{3.5}
\]

If \(\rho\) is a nontrivial zero of multiplicity \(m\), the residual in
(3.4) has residue

\[
 -mH(\rho).                                               \tag{3.6}
\]

Indeed, the paired zero at \(1-\overline{\rho}\) makes
\(({\cal J}L_\zeta)(s)\) singular at \(s=\rho\) with the reflected sign
required by (2.3).  The completion and pole-centering terms are regular at
\(\rho\).  Thus reflection reproduces the original carrier; it does not
weaken it.

Consequently either eventual one-sided bound

\[
 R_\zeta(x)\ge-Cx^q\quad\hbox{or}\quad R_\zeta(x)\le Cx^q,
 \qquad q<1,                                             \tag{3.7}
\]

remains the original Landau strip theorem.  The defect supplies no reserve.

## 4. The simpler zeta parity formula

It is useful to remove the conjugate notation when all coefficients are
real.  Set

\[
 A(s)=\frac{d}{ds}\log C_\zeta(s)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
   +\frac12\frac{\Gamma'}{\Gamma}(s/2),                  \tag{4.1}
\]

and \(K(s)=-\zeta'(s)/\zeta(s)\).  Differentiating
\(\xi(s)=\xi(1-s)\) gives

\[
 K(s)+K(1-s)=A(s)+A(1-s).                                \tag{4.2}
\]

With \(({\cal R}f)(s)=f(1-s)\), put

\[
 A_+=\frac{A+{\cal R}A}{2},\qquad
 K_-=\frac{K-{\cal R}K}{2}.                              \tag{4.3}
\]

Then

\[
 \boxed{K=A_++K_-,\qquad {\cal R}K_-=-K_-.}              \tag{4.4}
\]

The known archimedean data determine \(A_+\).  Every nontrivial-zero pole is
in \(K_-\).  At a zero \(\rho\) of multiplicity \(m\),

\[
 \operatorname*{Res}_{s=\rho}K_-=-m.                    \tag{4.5}
\]

Thus the exact functional equation fixes precisely the component which is
regular at the target divisor.

### Proposition 4.1: linear completion projection preserves the carrier

For an arbitrary meromorphic candidate \(K_F\), define its zeta-completion
defect and the associated linear projection by

\[
 E_F=K_F+{\cal R}K_F-A-{\cal R}A,\qquad
 \Pi_{\rm comp}K_F=K_F-\frac12E_F.                       \tag{4.6}
\]

Then

\[
 \Pi_{\rm comp}K_F=A_+
        +\frac12(K_F-{\cal R}K_F),                       \tag{4.7}
\]

so \(\Pi_{\rm comp}K_F\) satisfies (4.2) and preserves the entire odd
component of \(K_F\).  If \(K_F\) has a pole at \(\rho\) while
\({\cal R}K_F\) is regular there, the projected function still has a pole
there with half the residue and acquires its reflected partner.  If the pair
was already present with compatible residues, the full residue is retained.

Therefore a linear defect correction can enforce the logarithmic-derivative
functional equation without removing the planted carrier.

## 5. The R68 Type-II carrier has the same parity

For a hard cutoff \(Y\), use the exact R68 notation

\[
 \begin{aligned}
 K(s)&=-\zeta'(s)/\zeta(s),\\
 M_Y(s)&=\sum_{d\le Y}\mu(d)d^{-s},\\
 L_Y(s)&=\sum_{b\le Y}\Lambda(b)b^{-s},\\
 D_Y(s)&=(1-\zeta(s)M_Y(s))(K(s)-L_Y(s)).
 \end{aligned}                                           \tag{5.1}
\]

The exact Type-I complement is

\[
 I_Y(s)=K(s)-D_Y(s)
 =L_Y(s)-M_Y(s)\zeta'(s)-\zeta(s)M_Y(s)L_Y(s).           \tag{5.2}
\]

Because (5.2) contains no reciprocal zeta factor, \(I_Y\) is holomorphic at
every nontrivial zero.  Substituting (3.4), before the R95 multiplier, gives

\[
 D_Y(s)
 =-\frac12{\cal E}_\zeta(s)
  +\left\{-\frac12{\cal O}_\zeta(s)+A(s)-I_Y(s)\right\}.
 \tag{5.3}
\]

For zeta, the first term is identically zero.  The bracket is exactly
\(D_Y\), and at every zero \(\rho\) it has residue \(-m\).

Equivalently, define

\[
 D_Y^\pm(s)=\frac12\{D_Y(s)\pm D_Y(1-s)\}.               \tag{5.4}
\]

Functional-equation symmetry and the R68 pole ledger give

\[
 \operatorname*{Res}_{s=\rho}D_Y^+=0,\qquad
 \operatorname*{Res}_{s=\rho}D_Y^-=-m.                  \tag{5.5}
\]

The fixed R68 ramp multiplier is nonzero at every off-critical zero, so it
does not change (5.5).  The completion-even Type-II channel is
divisor-blind; the completion-odd channel is the full strip carrier.
Moving the Type-I complement or either mandatory centering changes only
terms regular at \(\rho\).

## 6. What the sparse surgery defect actually measures

Let

\[
 G(s)=Q_{K,P}(s+d+i\gamma)Q_{K,P}(s+d-i\gamma),\qquad
 L(s)=\zeta(s)G(s),                                      \tag{6.1}
\]

using the Chebotarev-sparse factor from R178.  Give \(L\) the *fixed zeta
completion* \(C_\zeta(s)L(s)=\xi(s)G(s)\).  Since \(G^\#=G\),

\[
 {\cal E}_L(s)=\frac{G'}G(s)+\frac{G'}G(1-s).            \tag{6.2}
\]

On its right half-plane of absolute convergence,

\[
 \frac{G'}G(s)
 =2q\sum_{\substack{p\in S\\p>P}}\sum_{k\ge1}
       (\log p)p^{-k(s+d)}\cos(k\gamma\log p).            \tag{6.3}
\]

Writing \(Q_{K,P}=B_{K,P}/\zeta_K\) supplies the meromorphic continuation

\[
 \frac{Q_{K,P}'}{Q_{K,P}}(w)
 =\frac{B_{K,P}'}{B_{K,P}}(w)
  -\frac{\zeta_K'}{\zeta_K}(w).                          \tag{6.4}
\]

Equations (6.2)--(6.4) show exactly why the defect rejects the original
surgery: a planted zero not accompanied by its critical-line reflection
contributes a nonzero residue to \({\cal E}_L\).

This can be certified inside the continuation domain.  If \(0<d<1/2\),
choose the prime degree \(q>1/(2d)\) and put
\(\alpha=1-d+i\gamma\).  At \(\alpha\), the two arguments of \(Q_{K,P}\)
are \(1+2i\gamma\) and \(1\), so \(G\) has the planted simple zero.  At the
reflected point \(1-\alpha=d-i\gamma\), those arguments are \(2d\) and
\(2d-2i\gamma\).  They lie in \(\Re w>1/q\) and neither is \(1\).
Because \(B_{K,P}\) is nonvanishing there and \(\zeta_K\) has no pole away
from \(1\), \(Q_{K,P}\) cannot have a zero at either argument.  It may have
a pole if a Dedekind-zeta zero intervenes, which only increases the signed
order discrepancy.  Hence

\[
 \operatorname{ord}_{\alpha}{\cal D}_L
 =\operatorname{ord}_{\alpha}G-\operatorname{ord}_{1-\alpha}G>0.
 \tag{6.4a}
\]

This is an admission test, not coercivity.  The two prime expansions in
(6.2) live in disjoint half-planes when \(0<d<1/2\):

\[
 \Re s>1-d,\qquad \Re s<d.                               \tag{6.5}
\]

Using both as convergent positive or signed Euler series in the critical
strip is invalid.  Analytically continuing the reflected series back across
the strip crosses precisely the planted and zeta-zero poles.

There is an even sharper falsifier.  Define

\[
 \widetilde\Xi(s)=\xi(s)G(s)G(1-s).                      \tag{6.6}
\]

Then

\[
 \widetilde\Xi(s)=\widetilde\Xi(1-s)                     \tag{6.7}
\]

identically, while every uncancelled zero of \(G\) and its reflection remain
in the divisor.  Thus exact completion by itself permits arbitrary paired
off-line zeros.  The price is that the underlying factor
\(\zeta(s)G(s)G(1-s)\) no longer has the ordinary positive
right-half-plane Euler expansion retained by the sparse model.

This proves the correct disjunction:

\[
 \boxed{\text{completion alone is insufficient, and Euler positivity alone
 is insufficient; only a theorem coupling them can advance the strip.}}
 \tag{6.8}
\]

It does not prove that every possible coupling must take one prescribed
form.

### Corollary 6.1: an exact symmetric-quartet falsifier

Fix \(1/2<\beta<1\) and \(\gamma\ne0\), and put

\[
 P_{\beta,\gamma}(s)=
 \prod_{\rho\in\{\beta\pm i\gamma,\,
                  1-\beta\pm i\gamma\}}(s-\rho).          \tag{6.9}
\]

Then

\[
 P_{\beta,\gamma}(1-s)=P_{\beta,\gamma}(s),              \tag{6.10}
\]

so its functional-equation defect vanishes identically.  Nevertheless its
R95 zero carrier is

\[
 -2\Re\left\{
 H(\beta+i\gamma)x^{\beta+i\gamma}
 +H(1-\beta+i\gamma)x^{1-\beta+i\gamma}\right\}.         \tag{6.11}
\]

Since \(H(\beta+i\gamma)\ne0\), the first term dominates the reflected term
by the factor \(x^{2\beta-1}\).  Along two interlacing phase sequences,
(6.11) therefore has opposite signs and magnitude comparable to
\(x^\beta\).  It is not bounded on either side by \(O(x^a)\) for any
\(a<\beta\).  The same pole ledger applies to every faithful fixed R68
multiplier.

Thus adding the mirror zero required by the functional equation does not
suppress a near-one zero; the mirror contributes only at exponent
\(1-\beta\).

## 7. The critical-line phase left uncontrolled

Away from zeros on the critical line, \(\xi(1/2+it)\) is real.  Put

\[
 \Theta(t)=\log|\xi(1/2+it)|.
\]

Then

\[
 \frac{\xi'}{\xi}(1/2+it)=-i\Theta'(t),\qquad
 K(1/2+it)=A(1/2+it)+i\Theta'(t).                        \tag{7.1}
\]

For the large-prime logarithmic tail \(C_Y=K-L_Y\),

\[
 C_Y(1/2+it)
 =A(1/2+it)-L_Y(1/2+it)+i\Theta'(t).                    \tag{7.2}
\]

Consequently the functional equation determines

\[
 \Re C_Y(1/2+it)
 =\Re\{A(1/2+it)-L_Y(1/2+it)\},                         \tag{7.3}
\]

but leaves the phase derivative \(\Theta'\) in the odd channel.  Near a
critical-line zero of multiplicity \(m\),

\[
 \Theta'(t)=\frac{m}{t-\gamma}+O(1).                    \tag{7.4}
\]

Off-line quartets appear through the corresponding meromorphic odd
projection.  Formula (7.2) is useful as a diagnostic, but not as an
\(L^2\) estimate: squaring it across zero ordinates without a prescribed
regularization is divergent.  The safe R68 object remains the finite
cutoff-complete polynomial and its exact center.

The missing information can therefore be described succinctly:
completion gives the real boundary trace, while the strip is carried by the
uncontrolled phase/odd trace.

## 8. The first nonlinear lift still has no sign

One might hope that Selberg's positive coefficients couple the even and odd
channels.  Define

\[
 {\cal S}(s)=K(s)^2-K'(s)
 =\sum_{n\ge1}\frac{(\Lambda*\Lambda)(n)+\Lambda(n)\log n}
                         {n^s},\qquad \Re s>1.           \tag{8.1}
\]

The coefficients in (8.1) are nonnegative.  Write

\[
 K=B+V,\qquad B=A_+,\qquad {\cal R}B=B,\quad {\cal R}V=-V.
 \tag{8.2}
\]

Direct algebra gives the exact parity projections

\[
 \frac{{\cal S}(s)+{\cal S}(1-s)}2
   =B(s)^2+V(s)^2-V'(s),                                \tag{8.3}
\]

\[
 \frac{{\cal S}(s)-{\cal S}(1-s)}2
   =2B(s)V(s)-B'(s).                                    \tag{8.4}
\]

These identities are nonlinear and do reach the odd carrier, but they do
not inherit coefficient positivity.  The Dirichlet series (8.1) converges
on the right; its reflected copy converges on the left.  Analytic
continuation of their average is not a positive measure.

On the critical line \(V(1/2+it)=iv(t)\) with \(v\) real, and

\[
 V^2-V'=-v(t)^2-v'(t),                                  \tag{8.5}
\]

which has no fixed sign.  Inverting the associated Riccati equation
reintroduces the reciprocal completed function, equivalently the zero
divisor.  This is the completion-parity form of the R96 Selberg obstruction.
No one-sided R95 or R68 estimate follows from (8.1)--(8.5).

### The weighted-Möbius reflection does not escape

The exact R95 sawtooth form uses

\[
 B_\mu(s)=\sum_{n\ge1}\frac{-\mu(n)\log n}{n^s}
         =-\frac{\zeta'(s)}{\zeta(s)^2}.                 \tag{8.6}
\]

Writing \(\zeta(s)=\chi(s)\zeta(1-s)\) gives

\[
 B_\mu(s)=\chi(s)^{-1}\left\{
 \frac{\zeta'(1-s)}{\zeta(1-s)^2}
 -\frac{\chi'}{\chi}(s)\frac1{\zeta(1-s)}\right\}.       \tag{8.7}
\]

The reflected side still contains \(1/\zeta\) and a signed gamma term.
Multiplication by the Mellin factor \(H(s)\zeta(s)\) of the positive
sawtooth recompletion simply restores

\[
 H(s)\left\{\frac{\zeta'}{\zeta}(1-s)
                  -\frac{\chi'}{\chi}(s)\right\}
 =-H(s)\frac{\zeta'}{\zeta}(s).                          \tag{8.8}
\]

Thus completion moves the weighted-Möbius carrier to the reflected side and
then moves it back; it does not turn it into a positive dual sum.

## 9. Corrected roadmap

The attempted direct bridge is closed:

\[
 {\cal E}_\zeta=0
 \quad\not\Longrightarrow\quad
 \text{a bound on the odd carrier}.                       \tag{9.1}
\]

The roadmap is now:

1. **Keep the endpoint fixed.**  Use either the R95 one-sided ramp or the
   complete centered R68 Type-II aggregate.  No additional detector is
   needed.
2. **Work in the odd channel.**  A candidate lemma must constrain
   \({\cal O}_\zeta\), \(K_-\), or its finite cutoff-complete arithmetic
   realization.  A theorem only about \({\cal E}_\zeta\) cannot see the
   target.
3. **Couple completion to coefficients before continuation.**  The estimate
   must use the actual all-prime coefficients in a finite identity and the
   zeta completion jointly.  Treating the reflected logarithmic derivative
   as a second convergent Euler series is forbidden.
4. **Preserve recompletion.**  In the R68 coordinate, retain every cofactor,
   both mandatory centers, unequal products, and the moving Type-I defect.
5. **Demand a fixed reserve.**  The concrete milestone remains, on every
   regular frozen-cutoff block,

   \[
    X_I\le \exp\{(1-2\eta+o(1))R\},\qquad 0<\eta\le\tfrac12
    \ \hbox{fixed},                                      \tag{9.2}
   \]

   with \(X_I\) the exact two-shift energy minus only its subexponential
   atomic diagonal.

Equation (9.2) is still open.  This pass does not produce a smaller proved
two-shift inequality.  It does identify a mandatory design test: any claimed
completion-sensitive proof must be false or inapplicable for the
symmetrized sparse factor (6.6), and its operative estimate must act on the
odd rather than the defect channel.

### A weaker scalar checkpoint

There is one exact weakening of the pointwise R95 endpoint.  For fixed
\(L>0\), define, when \(x\ge e^L\),

\[
 {\mathfrak B}_L(x)=\int_{xe^{-L}}^x R_\zeta(y)\frac{dy}{y},\qquad
 K_L(s)=\frac{1-e^{-Ls}}s.                               \tag{9.3}
\]

The nonzero zeros of \(K_L\) all lie on \(\Re s=0\).  Therefore the same
Landau argument proves:

> If, for fixed \(0\le a<1,L,C,X\), either
> \[
> {\mathfrak B}_L(x)\ge-Cx^a
> \quad\hbox{or}\quad
> {\mathfrak B}_L(x)\le Cx^a
> \]
> for every \(x\ge X\), then zeta has no zero with
> \(\Re\rho>a\).

On logarithmic scale this is causal convolution by the fixed box
\(\mathbf1_{[0,L]}\), so its Laplace multiplier is \(K_L\).  Compact
initial-segment corrections are entire.  A pointwise R95 bound implies the
box bound, while the converse fails for general locally integrable
functions; the box hypothesis is therefore strictly weaker at the
function-space level.

It also has a technical advantage.  With the harmless half-weight convention
at prime powers, contour shifting gives

\[
\begin{aligned}
 {\mathfrak B}_L(x)
={}&L(\log(2\pi)-1)\\
 &+(e^L-1)\left(1-2\frac{\zeta'(-1)}{\zeta(-1)}\right)x^{-1}\\
 &+\sum_{k\ge1}\frac{2k+1}{2k(2k-1)}
       \frac{e^{2kL}-1}{2k}x^{-2k}\\
 &+\sum_\rho
 \frac{1-\rho}{\rho(\rho+1)}K_L(\rho)x^\rho .
                                                               \tag{9.4}
\end{aligned}
\]

The zero sum is absolutely convergent: its coefficient is
\(O_L(|\rho|^{-2})\).  Nevertheless, an off-line quartet is still dominated
by its \(x^\beta\) member and takes both signs.  Current
Vinogradov--Korobov input gives only

\[
 {\mathfrak B}_L(x)\ll_L
 x\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\},            \tag{9.5}
\]

not a fixed power.  Thus (9.3) is a cleaner and weaker faithful detector,
but no arithmetic advantage for proving its one-sided bound is presently
known.

Hamburger's converse theorem explains why the full qualitative combination
is rigid: under its regularity hypotheses, a Dirichlet series satisfying
the zeta functional equation is a constant multiple of zeta.  That
uniqueness theorem identifies the function; it does not bound its zeros.
Invoking it therefore does not supply (9.2).

## 10. Provenance, novelty, and trust

- The differentiated functional equation and reflection projections are
  classical algebra.
- The defect/R95/R68 common pole ledger and its application to the R178
  sparse surgery are project synthesis, with strong local predecessors in
  R96, R131, R159, R176, and R178.
- Hamburger's converse theorem is classical; a modern survey is
  [Perelli](https://arxiv.org/abs/1605.02354), and the original first paper is
  [Hamburger 1921](https://eudml.org/doc/167643).
- No literature-level novelty is claimed.  The exact packaging is
  unrefereed and not Lean-formalized.

The terminal claim status is:

\[
\begin{array}{c|c}
\text{completion-defect direct bridge}&\text{CLOSED}\\
\text{odd-channel completion--coefficient inequality}&\text{OPEN}\\
\text{one-sided R95 fixed-power bound}&\text{OPEN}\\
\text{one-sided complete R68 bound}&\text{OPEN}\\
\text{uniform zero-free strip}&\text{OPEN}\\
\text{RH}&\text{OPEN}
\end{array}
\]

Finite reflection, residue, symmetrization, and Selberg-parity identities
are replayed in
\( \texttt{src/test\_completion\_parity\_bridge.py} \).  The bridge file has
eight passing tests; the combined R68/R95 regression suite has 84 passing
tests.
