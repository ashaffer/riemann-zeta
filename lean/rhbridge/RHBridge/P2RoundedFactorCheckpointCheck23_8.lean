import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk8 :
    P2RoundedFactorCheckpointData.panel23Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix32_eq :
    P2RoundedFactorCheckpointData.panel23Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk8.1

theorem panel23Prefix33_eq :
    P2RoundedFactorCheckpointData.panel23Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk8.2.1

theorem panel23Prefix34_eq :
    P2RoundedFactorCheckpointData.panel23Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk8.2.2.1

theorem panel23Prefix35_eq :
    P2RoundedFactorCheckpointData.panel23Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk8.2.2.2

end RHP2Bridge
