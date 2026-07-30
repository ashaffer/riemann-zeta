import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk5 :
    P2RoundedFactorCheckpointData.panel2Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix20_eq :
    P2RoundedFactorCheckpointData.panel2Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk5.1

theorem panel2Prefix21_eq :
    P2RoundedFactorCheckpointData.panel2Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk5.2.1

theorem panel2Prefix22_eq :
    P2RoundedFactorCheckpointData.panel2Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk5.2.2.1

theorem panel2Prefix23_eq :
    P2RoundedFactorCheckpointData.panel2Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk5.2.2.2

end RHP2Bridge
