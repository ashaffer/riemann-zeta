import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk8 :
    P2RoundedFactorCheckpointData.panel10Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix32_eq :
    P2RoundedFactorCheckpointData.panel10Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk8.1

theorem panel10Prefix33_eq :
    P2RoundedFactorCheckpointData.panel10Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk8.2.1

theorem panel10Prefix34_eq :
    P2RoundedFactorCheckpointData.panel10Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk8.2.2.1

theorem panel10Prefix35_eq :
    P2RoundedFactorCheckpointData.panel10Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk8.2.2.2

end RHP2Bridge
