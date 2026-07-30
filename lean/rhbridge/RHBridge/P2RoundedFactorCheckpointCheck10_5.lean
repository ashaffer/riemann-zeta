import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk5 :
    P2RoundedFactorCheckpointData.panel10Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix20_eq :
    P2RoundedFactorCheckpointData.panel10Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk5.1

theorem panel10Prefix21_eq :
    P2RoundedFactorCheckpointData.panel10Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk5.2.1

theorem panel10Prefix22_eq :
    P2RoundedFactorCheckpointData.panel10Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk5.2.2.1

theorem panel10Prefix23_eq :
    P2RoundedFactorCheckpointData.panel10Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk5.2.2.2

end RHP2Bridge
