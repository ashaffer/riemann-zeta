import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk8 :
    P2RoundedFactorCheckpointData.panel7Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix32_eq :
    P2RoundedFactorCheckpointData.panel7Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk8.1

theorem panel7Prefix33_eq :
    P2RoundedFactorCheckpointData.panel7Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk8.2.1

theorem panel7Prefix34_eq :
    P2RoundedFactorCheckpointData.panel7Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk8.2.2.1

theorem panel7Prefix35_eq :
    P2RoundedFactorCheckpointData.panel7Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk8.2.2.2

end RHP2Bridge
