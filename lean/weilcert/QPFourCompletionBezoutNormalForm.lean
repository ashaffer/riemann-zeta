import Mathlib

/-!
# Four-completion Bezout normal form

Polynomial certificates for the unimodular token chart.  These identities
do not assert the open occupied-cell estimate.
-/

namespace QPFourCompletionBezoutNormalForm

theorem center_reconstruction
    (c C u v delta n : ℤ) (hbez : c * u - C * v = 1) :
    c * (u * delta - C * n) - C * (v * delta - c * n) = delta := by
  calc
    c * (u * delta - C * n) - C * (v * delta - c * n) =
        (c * u - C * v) * delta := by ring
    _ = delta := by rw [hbez]; ring

theorem partner_reconstruction
    (c C u v h m : ℤ) (hbez : c * u - C * v = 1) :
    C * (-v * h + c * m) - c * (-u * h + C * m) = h := by
  calc
    C * (-v * h + c * m) - c * (-u * h + C * m) =
        (c * u - C * v) * h := by ring
    _ = h := by rw [hbez]; ring

theorem middle_determinant
    (c C u v delta n h m : ℤ) (hbez : c * u - C * v = 1) :
    (u * delta - C * n) * (-v * h + c * m) -
      (v * delta - c * n) * (-u * h + C * m) = delta * m - n * h := by
  calc
    (u * delta - C * n) * (-v * h + c * m) -
        (v * delta - c * n) * (-u * h + C * m) =
      (c * u - C * v) * (delta * m - n * h) := by ring
    _ = delta * m - n * h := by rw [hbez]; ring

theorem gram_determinant
    (c C u v : ℤ) (hbez : c * u - C * v = 1) :
    (-2 * u * v) * (-2 * c * C) - (c * u + C * v)^2 = -1 := by
  nlinarith

theorem lorentz_sum_identity
    (b B c C d E : ℤ) :
    2 * c * C * (b * d + B * E) =
      (b * c + B * C) * (C * d + c * E) +
        (b * c - B * C) * (C * d - c * E) := by
  ring

theorem lorentz_determinant_identity
    (b B c C d E : ℤ) :
    2 * c * C * (b * d - B * E) =
      (b * c + B * C) * (C * d - c * E) +
        (b * c - B * C) * (C * d + c * E) := by
  ring

theorem positive_factorisation
    (b B c C d E : ℤ) :
    ((b * c + B * C) + (b * c - B * C)) *
        ((C * d + c * E) + (C * d - c * E)) =
      2 * c * C * ((b * d + B * E) + (b * d - B * E)) := by
  ring

theorem negative_factorisation
    (b B c C d E : ℤ) :
    ((b * c + B * C) - (b * c - B * C)) *
        ((C * d + c * E) - (C * d - c * E)) =
      2 * c * C * ((b * d + B * E) - (b * d - B * E)) := by
  ring

theorem prime_fixture_nonzero_mixed_remainder :
    let c : ℤ := 2934109
    let C : ℤ := 2934103
    let b : ℤ := 2934091
    let B : ℤ := 2934097
    let d : ℤ := 2934103
    let E : ℤ := 2934097
    (c * b - C * B) * (C * d - c * E) = -2592 := by
  norm_num

end QPFourCompletionBezoutNormalForm
