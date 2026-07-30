import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk8 :
    P2RoundedFactorCheckpointData.panel5Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix32_eq :
    P2RoundedFactorCheckpointData.panel5Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk8.1

theorem panel5Prefix33_eq :
    P2RoundedFactorCheckpointData.panel5Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk8.2.1

theorem panel5Prefix34_eq :
    P2RoundedFactorCheckpointData.panel5Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk8.2.2.1

theorem panel5Prefix35_eq :
    P2RoundedFactorCheckpointData.panel5Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk8.2.2.2

end RHP2Bridge
