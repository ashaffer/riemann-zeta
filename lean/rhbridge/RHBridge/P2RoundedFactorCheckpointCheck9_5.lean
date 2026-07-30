import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk5 :
    P2RoundedFactorCheckpointData.panel9Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix20_eq :
    P2RoundedFactorCheckpointData.panel9Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk5.1

theorem panel9Prefix21_eq :
    P2RoundedFactorCheckpointData.panel9Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk5.2.1

theorem panel9Prefix22_eq :
    P2RoundedFactorCheckpointData.panel9Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk5.2.2.1

theorem panel9Prefix23_eq :
    P2RoundedFactorCheckpointData.panel9Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk5.2.2.2

end RHP2Bridge
