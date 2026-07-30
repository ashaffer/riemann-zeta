import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk8 :
    P2RoundedFactorCheckpointData.panel20Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix32_eq :
    P2RoundedFactorCheckpointData.panel20Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk8.1

theorem panel20Prefix33_eq :
    P2RoundedFactorCheckpointData.panel20Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk8.2.1

theorem panel20Prefix34_eq :
    P2RoundedFactorCheckpointData.panel20Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk8.2.2.1

theorem panel20Prefix35_eq :
    P2RoundedFactorCheckpointData.panel20Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk8.2.2.2

end RHP2Bridge
