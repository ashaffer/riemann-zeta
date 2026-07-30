import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk8 :
    P2RoundedFactorCheckpointData.panel9Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix32_eq :
    P2RoundedFactorCheckpointData.panel9Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk8.1

theorem panel9Prefix33_eq :
    P2RoundedFactorCheckpointData.panel9Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk8.2.1

theorem panel9Prefix34_eq :
    P2RoundedFactorCheckpointData.panel9Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk8.2.2.1

theorem panel9Prefix35_eq :
    P2RoundedFactorCheckpointData.panel9Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk8.2.2.2

end RHP2Bridge
