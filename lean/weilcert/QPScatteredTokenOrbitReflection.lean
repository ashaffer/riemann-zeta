import Mathlib

/-!
# Rooted token orbit reflection

Exact polynomial certificates for the observation that the endpoint token
orbit is the negative of the centre token orbit.  These identities do not
assert the open scattered-path packing estimate.
-/

namespace QPScatteredTokenOrbitReflection

/-- If the centre token at index `-h` is `(-h,n)`, swapping its reconstructed
physical coordinates gives the endpoint reconstructed from `(h,-n)`. -/
theorem endpoint_is_reflected_center
    (c C u v h n : ℤ) :
    (-v * h + c * (-n), -u * h + C * (-n)) =
      (v * (-h) - c * n, u * (-h) - C * n) := by
  apply Prod.ext
  · ring
  · ring

/-- A middle pair therefore consists of the two cross-products of two points
of the single centre orbit. -/
theorem middle_difference_is_one_orbit_cross_product
    (b B c C u v h n : ℤ) :
    b * (-v * h + c * (-n)) - B * (-u * h + C * (-n)) =
      b * (v * (-h) - c * n) - B * (u * (-h) - C * n) := by
  ring

theorem middle_sum_is_one_orbit_cross_product
    (b B c C u v h n : ℤ) :
    b * (-v * h + c * (-n)) + B * (-u * h + C * (-n)) =
      b * (v * (-h) - c * n) + B * (u * (-h) - C * n) := by
  ring

/-- The exact width-one strip identity for a centre reconstruction. -/
theorem center_digital_strip_identity
    (C u delta n : ℤ) :
    C * n - u * delta = -(u * delta - C * n) := by
  ring

end QPScatteredTokenOrbitReflection
