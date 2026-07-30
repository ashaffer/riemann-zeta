import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk8 :
    P2RoundedFactorCheckpointData.panel13Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix32_eq :
    P2RoundedFactorCheckpointData.panel13Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk8.1

theorem panel13Prefix33_eq :
    P2RoundedFactorCheckpointData.panel13Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk8.2.1

theorem panel13Prefix34_eq :
    P2RoundedFactorCheckpointData.panel13Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk8.2.2.1

theorem panel13Prefix35_eq :
    P2RoundedFactorCheckpointData.panel13Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk8.2.2.2

end RHP2Bridge
