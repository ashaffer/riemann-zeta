import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk12 :
    P2RoundedFactorCheckpointData.panel20Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix48_eq :
    P2RoundedFactorCheckpointData.panel20Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk12.1

theorem panel20Prefix49_eq :
    P2RoundedFactorCheckpointData.panel20Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk12.2.1

theorem panel20Prefix50_eq :
    P2RoundedFactorCheckpointData.panel20Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk12.2.2.1

theorem panel20Prefix51_eq :
    P2RoundedFactorCheckpointData.panel20Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk12.2.2.2

end RHP2Bridge
