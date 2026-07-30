import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk8 :
    P2RoundedFactorCheckpointData.panel3Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix32_eq :
    P2RoundedFactorCheckpointData.panel3Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk8.1

theorem panel3Prefix33_eq :
    P2RoundedFactorCheckpointData.panel3Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk8.2.1

theorem panel3Prefix34_eq :
    P2RoundedFactorCheckpointData.panel3Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk8.2.2.1

theorem panel3Prefix35_eq :
    P2RoundedFactorCheckpointData.panel3Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk8.2.2.2

end RHP2Bridge
