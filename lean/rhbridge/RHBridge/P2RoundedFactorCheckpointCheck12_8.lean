import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk8 :
    P2RoundedFactorCheckpointData.panel12Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix32_eq :
    P2RoundedFactorCheckpointData.panel12Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk8.1

theorem panel12Prefix33_eq :
    P2RoundedFactorCheckpointData.panel12Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk8.2.1

theorem panel12Prefix34_eq :
    P2RoundedFactorCheckpointData.panel12Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk8.2.2.1

theorem panel12Prefix35_eq :
    P2RoundedFactorCheckpointData.panel12Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk8.2.2.2

end RHP2Bridge
