import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk5 :
    P2RoundedFactorCheckpointData.panel29Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix20_eq :
    P2RoundedFactorCheckpointData.panel29Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk5.1

theorem panel29Prefix21_eq :
    P2RoundedFactorCheckpointData.panel29Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk5.2.1

theorem panel29Prefix22_eq :
    P2RoundedFactorCheckpointData.panel29Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk5.2.2.1

theorem panel29Prefix23_eq :
    P2RoundedFactorCheckpointData.panel29Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk5.2.2.2

end RHP2Bridge
