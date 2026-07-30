import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk3 :
    P2RoundedFactorCheckpointData.panel5Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix12_eq :
    P2RoundedFactorCheckpointData.panel5Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk3.1

theorem panel5Prefix13_eq :
    P2RoundedFactorCheckpointData.panel5Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk3.2.1

theorem panel5Prefix14_eq :
    P2RoundedFactorCheckpointData.panel5Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk3.2.2.1

theorem panel5Prefix15_eq :
    P2RoundedFactorCheckpointData.panel5Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk3.2.2.2

end RHP2Bridge
