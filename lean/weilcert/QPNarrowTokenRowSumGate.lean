import Mathlib

/-!
# Narrow-token Cramer ledgers

These are polynomial identities used in the narrow-token audit.  They do
not assert the open anchored codegree-Carleson estimate.
-/

namespace WeilCert.QPNarrowTokenRowSumGate

def det (x y : ℤ × ℤ) : ℤ := x.1 * y.2 - x.2 * y.1

def token (p q u : ℤ × ℤ) : ℤ × ℤ :=
  (det p u, det u q)

/-- Cramer's reconstruction in the orientation used by the physical audit. -/
theorem cramer_reconstruction (p q u : ℤ × ℤ) :
    ((det p q) * u.1, (det p q) * u.2) =
      ((token p q u).2 * p.1 + (token p q u).1 * q.1,
       (token p q u).2 * p.2 + (token p q u).1 * q.2) := by
  rcases p with ⟨p₁, p₂⟩
  rcases q with ⟨q₁, q₂⟩
  rcases u with ⟨u₁, u₂⟩
  simp [det, token]
  constructor <;> ring

/-- The token map multiplies oriented areas by minus the base minor. -/
theorem token_determinant (p q u v : ℤ × ℤ) :
    det (token p q u) (token p q v) = -(det p q) * det u v := by
  rcases p with ⟨p₁, p₂⟩
  rcases q with ⟨q₁, q₂⟩
  rcases u with ⟨u₁, u₂⟩
  rcases v with ⟨v₁, v₂⟩
  simp [det, token]
  ring

end WeilCert.QPNarrowTokenRowSumGate
