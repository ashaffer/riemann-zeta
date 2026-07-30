import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk12 :
    P2RoundedFactorCheckpointData.panel29Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix48_eq :
    P2RoundedFactorCheckpointData.panel29Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk12.1

theorem panel29Prefix49_eq :
    P2RoundedFactorCheckpointData.panel29Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk12.2.1

theorem panel29Prefix50_eq :
    P2RoundedFactorCheckpointData.panel29Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk12.2.2.1

theorem panel29Prefix51_eq :
    P2RoundedFactorCheckpointData.panel29Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk12.2.2.2

end RHP2Bridge
