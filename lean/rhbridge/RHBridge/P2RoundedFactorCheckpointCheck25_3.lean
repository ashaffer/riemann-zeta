import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk3 :
    P2RoundedFactorCheckpointData.panel25Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix12_eq :
    P2RoundedFactorCheckpointData.panel25Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk3.1

theorem panel25Prefix13_eq :
    P2RoundedFactorCheckpointData.panel25Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk3.2.1

theorem panel25Prefix14_eq :
    P2RoundedFactorCheckpointData.panel25Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk3.2.2.1

theorem panel25Prefix15_eq :
    P2RoundedFactorCheckpointData.panel25Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk3.2.2.2

end RHP2Bridge
