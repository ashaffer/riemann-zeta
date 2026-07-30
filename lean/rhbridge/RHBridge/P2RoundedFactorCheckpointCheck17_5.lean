import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk5 :
    P2RoundedFactorCheckpointData.panel17Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix20_eq :
    P2RoundedFactorCheckpointData.panel17Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk5.1

theorem panel17Prefix21_eq :
    P2RoundedFactorCheckpointData.panel17Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk5.2.1

theorem panel17Prefix22_eq :
    P2RoundedFactorCheckpointData.panel17Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk5.2.2.1

theorem panel17Prefix23_eq :
    P2RoundedFactorCheckpointData.panel17Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk5.2.2.2

end RHP2Bridge
