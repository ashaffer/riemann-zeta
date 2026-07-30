import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk5 :
    P2RoundedFactorCheckpointData.panel23Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix20_eq :
    P2RoundedFactorCheckpointData.panel23Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk5.1

theorem panel23Prefix21_eq :
    P2RoundedFactorCheckpointData.panel23Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk5.2.1

theorem panel23Prefix22_eq :
    P2RoundedFactorCheckpointData.panel23Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk5.2.2.1

theorem panel23Prefix23_eq :
    P2RoundedFactorCheckpointData.panel23Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk5.2.2.2

end RHP2Bridge
