import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk8 :
    P2RoundedFactorCheckpointData.panel17Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix32_eq :
    P2RoundedFactorCheckpointData.panel17Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk8.1

theorem panel17Prefix33_eq :
    P2RoundedFactorCheckpointData.panel17Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk8.2.1

theorem panel17Prefix34_eq :
    P2RoundedFactorCheckpointData.panel17Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk8.2.2.1

theorem panel17Prefix35_eq :
    P2RoundedFactorCheckpointData.panel17Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk8.2.2.2

end RHP2Bridge
