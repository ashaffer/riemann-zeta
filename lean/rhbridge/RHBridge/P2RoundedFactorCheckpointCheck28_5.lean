import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk5 :
    P2RoundedFactorCheckpointData.panel28Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix20_eq :
    P2RoundedFactorCheckpointData.panel28Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk5.1

theorem panel28Prefix21_eq :
    P2RoundedFactorCheckpointData.panel28Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk5.2.1

theorem panel28Prefix22_eq :
    P2RoundedFactorCheckpointData.panel28Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk5.2.2.1

theorem panel28Prefix23_eq :
    P2RoundedFactorCheckpointData.panel28Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk5.2.2.2

end RHP2Bridge
