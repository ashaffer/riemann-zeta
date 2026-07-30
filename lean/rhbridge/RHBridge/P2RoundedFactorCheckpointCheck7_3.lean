import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk3 :
    P2RoundedFactorCheckpointData.panel7Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix12_eq :
    P2RoundedFactorCheckpointData.panel7Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk3.1

theorem panel7Prefix13_eq :
    P2RoundedFactorCheckpointData.panel7Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk3.2.1

theorem panel7Prefix14_eq :
    P2RoundedFactorCheckpointData.panel7Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk3.2.2.1

theorem panel7Prefix15_eq :
    P2RoundedFactorCheckpointData.panel7Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk3.2.2.2

end RHP2Bridge
