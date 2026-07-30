import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk5 :
    P2RoundedFactorCheckpointData.panel25Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix20_eq :
    P2RoundedFactorCheckpointData.panel25Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk5.1

theorem panel25Prefix21_eq :
    P2RoundedFactorCheckpointData.panel25Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk5.2.1

theorem panel25Prefix22_eq :
    P2RoundedFactorCheckpointData.panel25Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk5.2.2.1

theorem panel25Prefix23_eq :
    P2RoundedFactorCheckpointData.panel25Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk5.2.2.2

end RHP2Bridge
