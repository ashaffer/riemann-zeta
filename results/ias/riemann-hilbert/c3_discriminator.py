#!/usr/bin/env python3
"""
Round-2 verification arithmetic for SEAT-riemann-hilbert.md R2.2 (C-2(I)(c)
dictionary check + C-3 discriminator scoring). All inputs previously published
(runs.csv; this seat's Round-1 §5; agent-deep-windows.md w_E2 table). The
decision rule was written in the seat file BEFORE this script ran.
"""
import math
LN10 = math.log(10)
PI = math.pi

# --- C-2(I)(c): Lambert point and chart dictionary --------------------------
# w_inf solves e^w (w-1) = 1  <=>  w = 1 + W(1/e)  <=>  w = 1 + e^{-w}
w = 1.2
for _ in range(60):
    w = 1 + math.exp(-w)
ew = math.exp(w)
print(f"w_inf = {w:.7f}; e^w_inf = {ew:.6f}; check e^w(w-1) = {ew*(w-1):.12f}")
print(f"identity e^w*w = 1 + e^w: {ew*w:.6f} vs {1+ew:.6f}")
den = 2 * PI * (1 + ew)
p, Ap, A = 4.85, 16.75, 11.5   # my fit; w_E2's own offset A = 11.5
print(f"2pi(1+e^w) = {den:.4f}; dictionary w(l) = w_inf - (p*l + A'-A) e^-l / {den:.3f}")
meas = {4.25: 1.2136, 4.50: 1.2192, 4.60: 1.2211, 4.75: 1.2243, 5.00: 1.2282}
for L, wm in meas.items():
    l = L / 2
    wpred = w - (p * l + Ap - A) * math.exp(-l) / den
    print(f"  L={L:4.2f}: w_pred = {wpred:.4f}  w_E2 = {wm:.4f}  diff = {wpred-wm:+.4f}")

# --- C-3: the L=5.50 triple, scored against the pre-registered rule ---------
x = [1.98537547115e-64, 1.4413990224e-67, 4.29586487391e-69]  # m=152/168/184
r_val = [x[1]/x[0], x[2]/x[1]]
d1, d2 = x[1]-x[0], x[2]-x[1]
aitken = x[2] - d2*d2/(d2-d1)
print(f"\nL=5.50 triple: value ratios {r_val[0]:.2e}, {r_val[1]:.4f} "
      f"(increase x{r_val[1]/r_val[0]:.0f} -> plunge; geometric model invalid)")
print(f"Aitken = {aitken:.4e} (log10 {math.log(aitken)/LN10:.2f}) -- invalid as limit")

# thresholds from published constants
def lg10(lnlam): return lnlam / LN10
for tag, pp, App in [("mine p=9/2 ", 4.5, 16.752), ("mine p=pi^2/2", PI*PI/2, 15.768),
                     ("Fuchs-literal", 4.5, 14.6757)]:
    l = 2.75
    print(f"  forecast {tag}: log10 lam(5.50) = {lg10(App - 4*PI*math.exp(l) + pp*l):8.2f}")
print("decision boundary log10 = -73.2 (6.3e-74); kill-mine: any RR rung < 1.0e-73;"
      " kill-both: < 1.5e-74")
print(f"last rung log10 = {math.log(x[2])/LN10:.2f}; gap to boundary = "
      f"{math.log(x[2])/LN10 + 73.2:.1f} decades -> NOT ADJUDICATED")
