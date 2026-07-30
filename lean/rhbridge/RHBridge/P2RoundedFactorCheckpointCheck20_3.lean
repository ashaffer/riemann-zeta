import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk3 :
    P2RoundedFactorCheckpointData.panel20Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix12_eq :
    P2RoundedFactorCheckpointData.panel20Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk3.1

theorem panel20Prefix13_eq :
    P2RoundedFactorCheckpointData.panel20Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk3.2.1

theorem panel20Prefix14_eq :
    P2RoundedFactorCheckpointData.panel20Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk3.2.2.1

theorem panel20Prefix15_eq :
    P2RoundedFactorCheckpointData.panel20Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk3.2.2.2

end RHP2Bridge
