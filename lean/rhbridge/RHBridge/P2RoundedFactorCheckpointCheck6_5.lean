import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk5 :
    P2RoundedFactorCheckpointData.panel6Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix20_eq :
    P2RoundedFactorCheckpointData.panel6Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk5.1

theorem panel6Prefix21_eq :
    P2RoundedFactorCheckpointData.panel6Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk5.2.1

theorem panel6Prefix22_eq :
    P2RoundedFactorCheckpointData.panel6Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk5.2.2.1

theorem panel6Prefix23_eq :
    P2RoundedFactorCheckpointData.panel6Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk5.2.2.2

end RHP2Bridge
