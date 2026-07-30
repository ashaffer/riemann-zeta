import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk5 :
    P2RoundedFactorCheckpointData.panel20Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix20_eq :
    P2RoundedFactorCheckpointData.panel20Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk5.1

theorem panel20Prefix21_eq :
    P2RoundedFactorCheckpointData.panel20Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk5.2.1

theorem panel20Prefix22_eq :
    P2RoundedFactorCheckpointData.panel20Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk5.2.2.1

theorem panel20Prefix23_eq :
    P2RoundedFactorCheckpointData.panel20Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk5.2.2.2

end RHP2Bridge
