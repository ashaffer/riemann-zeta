import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk5 :
    P2RoundedFactorCheckpointData.panel7Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix20_eq :
    P2RoundedFactorCheckpointData.panel7Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk5.1

theorem panel7Prefix21_eq :
    P2RoundedFactorCheckpointData.panel7Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk5.2.1

theorem panel7Prefix22_eq :
    P2RoundedFactorCheckpointData.panel7Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk5.2.2.1

theorem panel7Prefix23_eq :
    P2RoundedFactorCheckpointData.panel7Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk5.2.2.2

end RHP2Bridge
