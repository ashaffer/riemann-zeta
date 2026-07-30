import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk3 :
    P2RoundedFactorCheckpointData.panel4Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix12_eq :
    P2RoundedFactorCheckpointData.panel4Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk3.1

theorem panel4Prefix13_eq :
    P2RoundedFactorCheckpointData.panel4Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk3.2.1

theorem panel4Prefix14_eq :
    P2RoundedFactorCheckpointData.panel4Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk3.2.2.1

theorem panel4Prefix15_eq :
    P2RoundedFactorCheckpointData.panel4Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk3.2.2.2

end RHP2Bridge
