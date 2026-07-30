import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk5 :
    P2RoundedFactorCheckpointData.panel21Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix20_eq :
    P2RoundedFactorCheckpointData.panel21Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk5.1

theorem panel21Prefix21_eq :
    P2RoundedFactorCheckpointData.panel21Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk5.2.1

theorem panel21Prefix22_eq :
    P2RoundedFactorCheckpointData.panel21Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk5.2.2.1

theorem panel21Prefix23_eq :
    P2RoundedFactorCheckpointData.panel21Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk5.2.2.2

end RHP2Bridge
