import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk5 :
    P2RoundedFactorCheckpointData.panel13Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix20_eq :
    P2RoundedFactorCheckpointData.panel13Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk5.1

theorem panel13Prefix21_eq :
    P2RoundedFactorCheckpointData.panel13Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk5.2.1

theorem panel13Prefix22_eq :
    P2RoundedFactorCheckpointData.panel13Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk5.2.2.1

theorem panel13Prefix23_eq :
    P2RoundedFactorCheckpointData.panel13Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk5.2.2.2

end RHP2Bridge
