import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk11 :
    P2RoundedFactorCheckpointData.panel29Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix44_eq :
    P2RoundedFactorCheckpointData.panel29Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk11.1

theorem panel29Prefix45_eq :
    P2RoundedFactorCheckpointData.panel29Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk11.2.1

theorem panel29Prefix46_eq :
    P2RoundedFactorCheckpointData.panel29Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk11.2.2.1

theorem panel29Prefix47_eq :
    P2RoundedFactorCheckpointData.panel29Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk11.2.2.2

end RHP2Bridge
