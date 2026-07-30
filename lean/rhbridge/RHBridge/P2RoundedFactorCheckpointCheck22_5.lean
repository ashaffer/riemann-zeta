import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk5 :
    P2RoundedFactorCheckpointData.panel22Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix20_eq :
    P2RoundedFactorCheckpointData.panel22Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk5.1

theorem panel22Prefix21_eq :
    P2RoundedFactorCheckpointData.panel22Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk5.2.1

theorem panel22Prefix22_eq :
    P2RoundedFactorCheckpointData.panel22Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk5.2.2.1

theorem panel22Prefix23_eq :
    P2RoundedFactorCheckpointData.panel22Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk5.2.2.2

end RHP2Bridge
