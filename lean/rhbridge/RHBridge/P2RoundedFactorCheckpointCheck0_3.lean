import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk3 :
    P2RoundedFactorCheckpointData.panel0Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix12_eq :
    P2RoundedFactorCheckpointData.panel0Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk3.1

theorem panel0Prefix13_eq :
    P2RoundedFactorCheckpointData.panel0Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk3.2.1

theorem panel0Prefix14_eq :
    P2RoundedFactorCheckpointData.panel0Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk3.2.2.1

theorem panel0Prefix15_eq :
    P2RoundedFactorCheckpointData.panel0Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk3.2.2.2

end RHP2Bridge
