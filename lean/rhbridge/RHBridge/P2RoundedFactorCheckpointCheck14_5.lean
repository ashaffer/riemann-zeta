import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk5 :
    P2RoundedFactorCheckpointData.panel14Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix20_eq :
    P2RoundedFactorCheckpointData.panel14Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk5.1

theorem panel14Prefix21_eq :
    P2RoundedFactorCheckpointData.panel14Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk5.2.1

theorem panel14Prefix22_eq :
    P2RoundedFactorCheckpointData.panel14Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk5.2.2.1

theorem panel14Prefix23_eq :
    P2RoundedFactorCheckpointData.panel14Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk5.2.2.2

end RHP2Bridge
