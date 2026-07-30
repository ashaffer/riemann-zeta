import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk5 :
    P2RoundedFactorCheckpointData.panel31Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix20_eq :
    P2RoundedFactorCheckpointData.panel31Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk5.1

theorem panel31Prefix21_eq :
    P2RoundedFactorCheckpointData.panel31Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk5.2.1

theorem panel31Prefix22_eq :
    P2RoundedFactorCheckpointData.panel31Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk5.2.2.1

theorem panel31Prefix23_eq :
    P2RoundedFactorCheckpointData.panel31Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk5.2.2.2

end RHP2Bridge
