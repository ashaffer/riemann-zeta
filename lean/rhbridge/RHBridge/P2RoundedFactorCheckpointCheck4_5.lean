import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk5 :
    P2RoundedFactorCheckpointData.panel4Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix20_eq :
    P2RoundedFactorCheckpointData.panel4Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk5.1

theorem panel4Prefix21_eq :
    P2RoundedFactorCheckpointData.panel4Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk5.2.1

theorem panel4Prefix22_eq :
    P2RoundedFactorCheckpointData.panel4Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk5.2.2.1

theorem panel4Prefix23_eq :
    P2RoundedFactorCheckpointData.panel4Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk5.2.2.2

end RHP2Bridge
