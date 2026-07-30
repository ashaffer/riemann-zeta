import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk8 :
    P2RoundedFactorCheckpointData.panel4Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix32_eq :
    P2RoundedFactorCheckpointData.panel4Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk8.1

theorem panel4Prefix33_eq :
    P2RoundedFactorCheckpointData.panel4Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk8.2.1

theorem panel4Prefix34_eq :
    P2RoundedFactorCheckpointData.panel4Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk8.2.2.1

theorem panel4Prefix35_eq :
    P2RoundedFactorCheckpointData.panel4Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk8.2.2.2

end RHP2Bridge
