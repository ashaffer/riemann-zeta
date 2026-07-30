import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk8 :
    P2RoundedFactorCheckpointData.panel6Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix32_eq :
    P2RoundedFactorCheckpointData.panel6Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk8.1

theorem panel6Prefix33_eq :
    P2RoundedFactorCheckpointData.panel6Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk8.2.1

theorem panel6Prefix34_eq :
    P2RoundedFactorCheckpointData.panel6Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk8.2.2.1

theorem panel6Prefix35_eq :
    P2RoundedFactorCheckpointData.panel6Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk8.2.2.2

end RHP2Bridge
