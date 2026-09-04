import Mathlib

/-!
# Exact ledgers for the simultaneous-divisor RDP audit

These polynomial identities do not assert the open residual degree-product
theorem.  They certify the mixed-error expansion and its rectangular
cancellation, together with the numerical hard-window no-go fixture.
-/

namespace WeilCert.QPSimultaneousDivisorRDP

theorem mixedErrorLedger
    (a b B c C x d D y e E : ℤ) :
    x * y * (d * e - D * E) =
      a^2 * (b * c - B * C)
      + a * b * (x * d - a * c)
      - a * B * (x * D - a * C)
      + a * c * (y * e - a * b)
      - a * C * (y * E - a * B)
      + (x * d - a * c) * (y * e - a * b)
      - (x * D - a * C) * (y * E - a * B) := by
  ring

theorem rectangularMixedRemainder
    (K A₁ A₂ B₁ B₂ α₁ α₂ β₁ β₂ γ₁ γ₂ η₁ η₂ : ℤ) :
    (K + A₁ + B₁ + α₁ * γ₁ - β₁ * η₁)
      - (K + A₁ + B₂ + α₁ * γ₂ - β₁ * η₂)
      - (K + A₂ + B₁ + α₂ * γ₁ - β₂ * η₁)
      + (K + A₂ + B₂ + α₂ * γ₂ - β₂ * η₂) =
    (α₁ - α₂) * (γ₁ - γ₂) - (β₁ - β₂) * (η₁ - η₂) := by
  ring

example : (26 : ℤ)^2 < 809 := by norm_num

example :
    let q : ℤ := 809
    let D : ℤ := 26
    let triples : List (ℤ × ℤ × ℤ) :=
      [(377, 391, 449), (377, 440, 399),
       (349, 391, 485), (349, 440, 431),
       (440, 335, 449), (440, 377, 399)]
    ∀ t ∈ triples, |8 * t.1 * t.2.1 * t.2.2 - q^3| ≤ q * D := by
  norm_num

example :
    ((0 : ℤ) - (-8)) * ((0 : ℤ) - (-7))
      - ((0 : ℤ) - (-4)) * ((0 : ℤ) - 0) = 56 := by
  norm_num

end WeilCert.QPSimultaneousDivisorRDP
