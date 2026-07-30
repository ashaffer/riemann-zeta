import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk8 :
    P2RoundedFactorCheckpointData.panel0Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix32_eq :
    P2RoundedFactorCheckpointData.panel0Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk8.1

theorem panel0Prefix33_eq :
    P2RoundedFactorCheckpointData.panel0Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk8.2.1

theorem panel0Prefix34_eq :
    P2RoundedFactorCheckpointData.panel0Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk8.2.2.1

theorem panel0Prefix35_eq :
    P2RoundedFactorCheckpointData.panel0Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk8.2.2.2

end RHP2Bridge
