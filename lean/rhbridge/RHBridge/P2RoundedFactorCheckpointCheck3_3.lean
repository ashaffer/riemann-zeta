import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk3 :
    P2RoundedFactorCheckpointData.panel3Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix12_eq :
    P2RoundedFactorCheckpointData.panel3Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk3.1

theorem panel3Prefix13_eq :
    P2RoundedFactorCheckpointData.panel3Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk3.2.1

theorem panel3Prefix14_eq :
    P2RoundedFactorCheckpointData.panel3Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk3.2.2.1

theorem panel3Prefix15_eq :
    P2RoundedFactorCheckpointData.panel3Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk3.2.2.2

end RHP2Bridge
