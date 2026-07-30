import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk5 :
    P2RoundedFactorCheckpointData.panel12Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix20_eq :
    P2RoundedFactorCheckpointData.panel12Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk5.1

theorem panel12Prefix21_eq :
    P2RoundedFactorCheckpointData.panel12Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk5.2.1

theorem panel12Prefix22_eq :
    P2RoundedFactorCheckpointData.panel12Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk5.2.2.1

theorem panel12Prefix23_eq :
    P2RoundedFactorCheckpointData.panel12Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk5.2.2.2

end RHP2Bridge
